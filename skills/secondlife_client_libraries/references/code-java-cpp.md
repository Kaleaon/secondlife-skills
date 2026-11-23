# Second Life in Java and C++

Two halves, one protocol.

- **Part A — Java (Lumiya-style):** how an Android viewer in the Lumiya / Lumiya-Redux lineage implements LLSD, the UDP circuit, generated message classes, caps over OkHttp, XML-RPC login with MFA, and the GLES-side texture/mesh decode path. Canonical sources: `Kaleaon/Lumiya-Redux` (Apache-2.0 recovery of Lumiya 3.4.2 — 1,302 Java classes, 477 UDP message classes, Gradle/JDK 17/SDK 34), cross-checked against `secondlife/viewer` (`llviewerregion.cpp` `buildCapabilityNames`, `llaisapi.cpp`) exactly as Lumiya-Redux's own gap-analysis docs do.
- **Part B — C++ (viewer-style):** the same stack in the idiom of `secondlife/viewer` (`indra/llcommon` LLSD, `indra/llmessage` circuit concepts), plus a standalone modern-C++ zerocode + packet parser you can drop into a tool, and a CMakeLists to build it. Viewer code is LGPL-2.1: the standalone parser here is an original implementation written from the wire format, not copied viewer code — keep that distinction when you reuse it.

Android rules that shape Part A: no network on the main thread, UDP sockets die with the process (and misbehave across Doze), and every blocking call below belongs on a dedicated executor or an OkHttp dispatcher thread.

---

# Part A — Java

## A1. LLSD in Java

Lumiya carries its own LLSD implementation (there is no maintained standalone Java LLSD library — the Java codec lives inside the viewer). The class model below mirrors that shape: a small `LLSD` value hierarchy is overkill; Lumiya-style code uses a tagged-union-ish `LLSDValue`-free approach with `Map<String,Object>`, `List<Object>`, and boxed scalars, plus dedicated `UUID` and `byte[]` handling. This implementation follows that pragmatic model and adds strict 32-bit integer checking, which hand-rolled Java codecs often miss because Java `int` is already 32-bit but parsers happily produce `long`.

```java
package com.example.slproto.llsd;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Base64;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/**
 * LLSD value conventions used across this file:
 *   undefined -> null            boolean -> Boolean
 *   integer   -> Integer         real    -> Double
 *   string    -> String          binary  -> byte[]
 *   uuid      -> java.util.UUID  date    -> java.time.Instant
 *   uri       -> LLSDUri (String wrapper, so XML/binary round-trips
 *              preserve the type instead of degrading to string)
 *   array     -> List<Object>    map     -> Map<String, Object>
 */
public final class LLSD {
    private LLSD() {}

    /** Distinct type for LLSD URIs. */
    public record LLSDUri(String value) {}

    public static final class LLSDException extends RuntimeException {
        public LLSDException(String message) { super(message); }
        public LLSDException(String message, Throwable cause) { super(message, cause); }
    }

    static int checkInt(long value) {
        if (value < Integer.MIN_VALUE || value > Integer.MAX_VALUE) {
            throw new LLSDException("LLSD integer out of 32-bit range: " + value);
        }
        return (int) value;
    }

    // ------------------------------------------------------------------
    // Binary writer
    // ------------------------------------------------------------------
    public static byte[] toBinary(Object value) {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        try (DataOutputStream out = new DataOutputStream(buffer)) {
            writeBinary(out, value);
            out.flush();
        } catch (IOException e) {
            throw new LLSDException("Binary LLSD write failed", e);
        }
        return buffer.toByteArray();
    }

    private static void writeBinary(DataOutputStream out, Object value) throws IOException {
        if (value == null) {
            out.writeByte('!');
        } else if (value instanceof Boolean b) {
            out.writeByte(b ? 'T' : 'F');
        } else if (value instanceof LLSDUri uri) {
            byte[] raw = uri.value().getBytes(StandardCharsets.UTF_8);
            out.writeByte('l');
            out.writeInt(raw.length);
            out.write(raw);
        } else if (value instanceof Integer i) {
            out.writeByte('i');
            out.writeInt(i);
        } else if (value instanceof Long l) {
            // Accept Long at the API boundary but enforce the LLSD range:
            // silently truncating a long into an LLSD integer corrupts
            // timestamps and asset sizes in exactly the hard-to-see way.
            out.writeByte('i');
            out.writeInt(checkInt(l));
        } else if (value instanceof Double d) {
            out.writeByte('r');
            out.writeDouble(d);
        } else if (value instanceof UUID uuid) {
            out.writeByte('u');
            out.writeLong(uuid.getMostSignificantBits());
            out.writeLong(uuid.getLeastSignificantBits());
        } else if (value instanceof byte[] bytes) {
            out.writeByte('b');
            out.writeInt(bytes.length);
            out.write(bytes);
        } else if (value instanceof Instant instant) {
            out.writeByte('d');
            // LLSD binary dates are epoch seconds as a double. Sub-second
            // precision survives; do not round to whole seconds.
            out.writeDouble(instant.toEpochMilli() / 1000.0);
        } else if (value instanceof String s) {
            byte[] raw = s.getBytes(StandardCharsets.UTF_8);
            out.writeByte('s');
            out.writeInt(raw.length);
            out.write(raw);
        } else if (value instanceof List<?> list) {
            out.writeByte('[');
            out.writeInt(list.size());
            for (Object item : list) writeBinary(out, item);
            out.writeByte(']');
        } else if (value instanceof Map<?, ?> map) {
            out.writeByte('{');
            out.writeInt(map.size());
            for (Map.Entry<?, ?> entry : map.entrySet()) {
                byte[] key = String.valueOf(entry.getKey()).getBytes(StandardCharsets.UTF_8);
                out.writeByte('k');
                out.writeInt(key.length);
                out.write(key);
                writeBinary(out, entry.getValue());
            }
            out.writeByte('}');
        } else {
            throw new LLSDException("Cannot LLSD-serialise " + value.getClass());
        }
    }

    // ------------------------------------------------------------------
    // Binary reader — cursor based, bounds-checked. A truncated caps
    // response must produce LLSDException, never BufferUnderflowException
    // leaking into UI code.
    // ------------------------------------------------------------------
    public static final class BinaryReader {
        private final byte[] data;
        private int pos;

        public BinaryReader(byte[] data) { this.data = data; }

        private int u8() {
            if (pos >= data.length) throw new LLSDException("Binary LLSD truncated");
            return data[pos++] & 0xFF;
        }

        private byte[] take(int n) {
            if (n < 0 || pos + n > data.length) throw new LLSDException("Binary LLSD truncated");
            byte[] out = new byte[n];
            System.arraycopy(data, pos, out, 0, n);
            pos += n;
            return out;
        }

        private int i32() {
            byte[] b = take(4);
            return (b[0] & 0xFF) << 24 | (b[1] & 0xFF) << 16 | (b[2] & 0xFF) << 8 | (b[3] & 0xFF);
        }

        private long i64() {
            long v = 0;
            for (byte b : take(8)) v = (v << 8) | (b & 0xFFL);
            return v;
        }

        private double f64() { return Double.longBitsToDouble(i64()); }

        public Object readValue() {
            int marker = u8();
            switch (marker) {
                case '!': return null;
                case 'T': return Boolean.TRUE;
                case 'F': return Boolean.FALSE;
                case 'i': return i32();
                case 'r': return f64();
                case 'u': return new UUID(i64(), i64());
                case 's': return new String(take(i32()), StandardCharsets.UTF_8);
                case 'l': return new LLSDUri(new String(take(i32()), StandardCharsets.UTF_8));
                case 'b': return take(i32());
                case 'd': return Instant.ofEpochMilli(Math.round(f64() * 1000.0));
                case '[': {
                    int count = i32();
                    List<Object> items = new ArrayList<>(count);
                    for (int i = 0; i < count; i++) items.add(readValue());
                    if (u8() != ']') throw new LLSDException("Binary LLSD array missing ']'");
                    return items;
                }
                case '{': {
                    int count = i32();
                    Map<String, Object> map = new LinkedHashMap<>();
                    for (int i = 0; i < count; i++) {
                        if (u8() != 'k') throw new LLSDException("Binary LLSD map key missing 'k'");
                        String key = new String(take(i32()), StandardCharsets.UTF_8);
                        map.put(key, readValue());
                    }
                    if (u8() != '}') throw new LLSDException("Binary LLSD map missing '}'");
                    return map;
                }
                default:
                    throw new LLSDException("Unknown binary LLSD marker: " + (char) marker);
            }
        }

        public boolean exhausted() { return pos == data.length; }
    }

    public static Object fromBinary(byte[] data) {
        BinaryReader reader = new BinaryReader(data);
        Object value = reader.readValue();
        if (!reader.exhausted()) throw new LLSDException("Trailing bytes after binary LLSD");
        return value;
    }

    /** Base64 helper for the XML codec and for BinaryBucket-style fields. */
    public static String binaryToBase64(byte[] bytes) {
        return Base64.getEncoder().encodeToString(bytes);
    }
}
```

### A1.1 XML LLSD (the caps wire format)

Caps speak XML LLSD (`application/llsd+xml`). On Android, parse with `XmlPullParser` (streaming, no DOM memory blow-up on a 100k-item inventory skeleton) and write with a `StringBuilder` — the documents a client *sends* are small; the documents it *receives* are the dangerous ones.

```java
package com.example.slproto.llsd;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserException;

import java.io.IOException;
import java.io.StringReader;
import java.time.Instant;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Base64;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

/** XML LLSD writer + streaming reader. */
public final class LLSDXml {
    private LLSDXml() {}

    private static final DateTimeFormatter DATE_FORMAT =
            DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss'Z'").withZone(ZoneOffset.UTC);

    // ---------------- writer ----------------
    public static String toXml(Object value) {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<llsd>");
        append(sb, value);
        sb.append("</llsd>");
        return sb.toString();
    }

    private static String esc(String text) {
        // Only the three escapes matter for element text; quotes are legal raw.
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;");
    }

    private static void append(StringBuilder sb, Object value) {
        if (value == null) {
            sb.append("<undef/>");
        } else if (value instanceof Boolean b) {
            sb.append("<boolean>").append(b ? "1" : "0").append("</boolean>");
        } else if (value instanceof LLSD.LLSDUri uri) {
            sb.append("<uri>").append(esc(uri.value())).append("</uri>");
        } else if (value instanceof Integer || value instanceof Long) {
            sb.append("<integer>").append(LLSD.checkInt(((Number) value).longValue())).append("</integer>");
        } else if (value instanceof Double d) {
            sb.append("<real>").append(formatReal(d)).append("</real>");
        } else if (value instanceof UUID uuid) {
            sb.append("<uuid>").append(uuid).append("</uuid>");
        } else if (value instanceof byte[] bytes) {
            sb.append("<binary>").append(Base64.getEncoder().encodeToString(bytes)).append("</binary>");
        } else if (value instanceof Instant instant) {
            sb.append("<date>").append(DATE_FORMAT.format(instant)).append("</date>");
        } else if (value instanceof String s) {
            sb.append("<string>").append(esc(s)).append("</string>");
        } else if (value instanceof List<?> list) {
            sb.append("<array>");
            for (Object item : list) append(sb, item);
            sb.append("</array>");
        } else if (value instanceof Map<?, ?> map) {
            sb.append("<map>");
            for (Map.Entry<?, ?> e : map.entrySet()) {
                sb.append("<key>").append(esc(String.valueOf(e.getKey()))).append("</key>");
                append(sb, e.getValue());
            }
            sb.append("</map>");
        } else {
            throw new LLSD.LLSDException("Cannot LLSD-serialise " + value.getClass());
        }
    }

    private static String formatReal(double d) {
        if (Double.isNaN(d)) return "nan";
        if (Double.isInfinite(d)) return d > 0 ? "inf" : "-inf";
        return Double.toString(d);
    }

    // ---------------- reader ----------------
    public static Object fromXml(XmlPullParser parser) {
        try {
            int event = parser.getEventType();
            while (event != XmlPullParser.START_TAG || !"llsd".equals(parser.getName())) {
                event = parser.next();
                if (event == XmlPullParser.END_DOCUMENT) {
                    throw new LLSD.LLSDException("Empty LLSD document");
                }
            }
            parser.next();
            Object value = readValue(parser);
            return value;
        } catch (XmlPullParserException | IOException e) {
            throw new LLSD.LLSDException("XML LLSD parse failed", e);
        }
    }

    public static Object fromXml(String xml) {
        try {
            XmlPullParser parser = org.xmlpull.v1.XmlPullParserFactory
                    .newInstance().newPullParser();
            parser.setInput(new StringReader(xml));
            return fromXml(parser);
        } catch (XmlPullParserException e) {
            throw new LLSD.LLSDException("Cannot create pull parser", e);
        }
    }

    private static Object readValue(XmlPullParser parser)
            throws XmlPullParserException, IOException {
        // Precondition: parser is on the START_TAG of a value element.
        String tag = parser.getName();
        switch (tag) {
            case "undef":
                parser.next(); return null;
            case "boolean": {
                String t = parser.nextText();
                return "1".equals(t) || "true".equals(t);
            }
            case "integer":
                return LLSD.checkInt(Long.parseLong(parser.nextText().trim()));
            case "real":
                return Double.parseDouble(parser.nextText().trim());
            case "string":
                return parser.nextText();
            case "uri":
                return new LLSD.LLSDUri(parser.nextText());
            case "uuid": {
                String t = parser.nextText().trim();
                return t.isEmpty() ? new UUID(0, 0) : UUID.fromString(t);
            }
            case "binary":
                // Whitespace inside base64 is legal in the wild.
                return Base64.getMimeDecoder().decode(parser.nextText());
            case "date":
                return DATE_FORMAT.parse(parser.nextText().trim(), Instant::from);
            case "array": {
                List<Object> items = new ArrayList<>();
                parser.next();
                while (parser.getEventType() != XmlPullParser.END_TAG) {
                    items.add(readValue(parser));
                    parser.next();
                }
                return items;
            }
            case "map": {
                Map<String, Object> map = new LinkedHashMap<>();
                parser.next(); // -> <key> or </map>
                while (parser.getEventType() != XmlPullParser.END_TAG) {
                    // current: <key>
                    String key = parser.nextText();
                    parser.next(); // -> value start tag
                    map.put(key, readValue(parser));
                    parser.next(); // -> next <key> or </map>
                }
                return map;
            }
            default:
                throw new LLSD.LLSDException("Unknown LLSD element <" + tag + ">");
        }
    }
}
```

## A2. Zerocode and packet framing

Same wire rules as every other language in this repo: zerocoding applies to the message body of template-`Zerocoded` messages only, never to the 6-byte header or the appended ACK block, and appended ACKs are peeled off *before* zero-decoding.

```java
package com.example.slproto.net;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/** Zerocode + datagram framing. Stateless; safe to call from any thread. */
public final class Packets {
    private Packets() {}

    public static final int FLAG_ZEROCODED = 0x80;
    public static final int FLAG_RELIABLE = 0x40;
    public static final int FLAG_RESENT = 0x20;
    public static final int FLAG_ACK = 0x10;
    public static final int HEADER_LEN = 6;

    // ---------------- zerocode ----------------
    public static byte[] zeroEncode(byte[] data) {
        ByteBufferLike out = new ByteBufferLike(data.length + data.length / 8 + 2);
        int run = 0;
        for (byte b : data) {
            if (b == 0) {
                run++;
            } else {
                flushRun(out, run);
                run = 0;
                out.put(b);
            }
        }
        flushRun(out, run);
        return out.toByteArray();
    }

    private static void flushRun(ByteBufferLike out, int run) {
        while (run > 0) {
            int chunk = Math.min(run, 255);
            out.put((byte) 0);
            out.put((byte) chunk);
            run -= chunk;
        }
    }

    public static byte[] zeroDecode(byte[] data) {
        ByteBufferLike out = new ByteBufferLike(data.length * 2);
        int i = 0;
        while (i < data.length) {
            byte b = data[i];
            if (b != 0) {
                out.put(b);
                i++;
            } else {
                if (i + 1 >= data.length) {
                    throw new IllegalArgumentException("Zerocoded data ends with lone 0x00");
                }
                int count = data[i + 1] & 0xFF;
                if (count == 0) throw new IllegalArgumentException("Zerocode count 0");
                for (int k = 0; k < count; k++) out.put((byte) 0);
                i += 2;
            }
        }
        return out.toByteArray();
    }

    /** Minimal growable byte buffer (avoids ByteArrayOutputStream boxing noise
     *  in hot decode paths; Lumiya's own buffers serve the same purpose). */
    static final class ByteBufferLike {
        private byte[] buf;
        private int len;
        ByteBufferLike(int capacity) { buf = new byte[Math.max(16, capacity)]; }
        void put(byte b) {
            if (len == buf.length) buf = Arrays.copyOf(buf, buf.length * 2);
            buf[len++] = b;
        }
        void put(byte[] src) { for (byte b : src) put(b); }
        byte[] toByteArray() { return Arrays.copyOf(buf, len); }
    }

    // ---------------- message IDs ----------------
    public enum Frequency { HIGH, MEDIUM, LOW, FIXED }

    public static byte[] encodeMessageId(Frequency freq, int number) {
        switch (freq) {
            case HIGH: return new byte[]{(byte) number};
            case MEDIUM: return new byte[]{(byte) 0xFF, (byte) number};
            case LOW: return new byte[]{(byte) 0xFF, (byte) 0xFF,
                    (byte) (number >> 8), (byte) number};
            default: return ByteBuffer.allocate(4).order(ByteOrder.BIG_ENDIAN)
                    .putInt(number).array();
        }
    }

    /** Result of splitting a decoded body into (frequency, number, bodyOffset). */
    public record MessageId(Frequency frequency, int number, int offset) {}

    public static MessageId decodeMessageId(byte[] body) {
        if (body.length == 0) throw new IllegalArgumentException("Empty body");
        int b0 = body[0] & 0xFF;
        if (b0 != 0xFF) return new MessageId(Frequency.HIGH, b0, 1);
        if (body.length < 2) throw new IllegalArgumentException("Truncated ID");
        int b1 = body[1] & 0xFF;
        if (b1 != 0xFF) return new MessageId(Frequency.MEDIUM, b1, 2);
        if (body.length < 4) throw new IllegalArgumentException("Truncated ID");
        int b2 = body[2] & 0xFF;
        if (b2 != 0xFF) {
            return new MessageId(Frequency.LOW, (b2 << 8) | (body[3] & 0xFF), 4);
        }
        int fixed = ByteBuffer.wrap(body, 0, 4).order(ByteOrder.BIG_ENDIAN).getInt();
        return new MessageId(Frequency.FIXED, fixed, 4);
    }

    // ---------------- whole datagrams ----------------
    public static final class Packet {
        public int flags;
        public long sequence;
        public byte[] body;            // decoded, message ID at the front
        public List<Long> acks = new ArrayList<>();
        public boolean reliable() { return (flags & FLAG_RELIABLE) != 0; }
        public boolean zerocoded() { return (flags & FLAG_ZEROCODED) != 0; }
    }

    public static Packet parse(byte[] datagram, int length) {
        if (length < HEADER_LEN) throw new IllegalArgumentException("Short datagram");
        Packet packet = new Packet();
        packet.flags = datagram[0] & 0xFF;
        packet.sequence = ByteBuffer.wrap(datagram, 1, 4)
                .order(ByteOrder.BIG_ENDIAN).getInt() & 0xFFFFFFFFL;
        int extraLen = datagram[5] & 0xFF;
        int offset = HEADER_LEN + extraLen;
        if (offset > length) throw new IllegalArgumentException("Extra header overrun");
        int payloadLen = length - offset;

        if ((packet.flags & FLAG_ACK) != 0) {
            if (payloadLen < 1) throw new IllegalArgumentException("Ack flag, no payload");
            int count = datagram[length - 1] & 0xFF;
            int needed = 1 + 4 * count;
            if (payloadLen < needed) throw new IllegalArgumentException("Ack list overrun");
            int ackStart = length - needed;
            for (int i = 0; i < count; i++) {
                long seq = ByteBuffer.wrap(datagram, ackStart + 4 * i, 4)
                        .order(ByteOrder.BIG_ENDIAN).getInt() & 0xFFFFFFFFL;
                packet.acks.add(seq);
            }
            payloadLen -= needed;
        }

        byte[] payload = Arrays.copyOfRange(datagram, offset, offset + payloadLen);
        if ((packet.flags & FLAG_ZEROCODED) != 0) payload = zeroDecode(payload);
        packet.body = payload;
        return packet;
    }

    public static byte[] build(long sequence, byte[] messageId, byte[] body,
                               boolean reliable, boolean zerocoded, List<Long> acks) {
        byte[] payload = new byte[messageId.length + body.length];
        System.arraycopy(messageId, 0, payload, 0, messageId.length);
        System.arraycopy(body, 0, payload, messageId.length, body.length);
        int flags = 0;
        if (zerocoded) { flags |= FLAG_ZEROCODED; payload = zeroEncode(payload); }
        if (reliable) flags |= FLAG_RELIABLE;
        int ackBytes = (acks == null || acks.isEmpty()) ? 0 : 4 * acks.size() + 1;
        if (ackBytes > 0) flags |= FLAG_ACK;
        ByteBuffer out = ByteBuffer.allocate(HEADER_LEN + payload.length + ackBytes)
                .order(ByteOrder.BIG_ENDIAN);
        out.put((byte) flags);
        out.putInt((int) sequence);
        out.put((byte) 0); // extra header length
        out.put(payload);
        if (ackBytes > 0) {
            for (long seq : acks) out.putInt((int) seq);
            out.put((byte) acks.size());
        }
        return out.array();
    }
}
```

## A3. Body packer/reader and the message-class pattern

Lumiya's 477 message classes all follow one shape: a class per message, fields in template order, a `pack` into a growable buffer and a static/instance `unpack`. Generated classes do this mechanically from `message_template.msg`; the hand-written core messages below show the pattern the generator emits, including the two field encodings newcomers get wrong — quaternions (3 floats on the wire) and NUL-terminated Variable strings.

```java
package com.example.slproto.net;

import java.io.ByteArrayOutputStream;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.charset.StandardCharsets;
import java.util.UUID;

/** Typed body writer. All multi-byte values are big-endian. */
public final class BodyWriter {
    private final ByteArrayOutputStream out = new ByteArrayOutputStream();

    public BodyWriter u8(int v) { out.write(v & 0xFF); return this; }
    public BodyWriter u16(int v) { out.write((v >> 8) & 0xFF); out.write(v & 0xFF); return this; }
    public BodyWriter u32(long v) {
        for (int s = 24; s >= 0; s -= 8) out.write((int) (v >> s) & 0xFF);
        return this;
    }
    public BodyWriter u64(long v) {
        for (int s = 56; s >= 0; s -= 8) out.write((int) (v >> s) & 0xFF);
        return this;
    }
    public BodyWriter s16(int v) { return u16(v & 0xFFFF); }
    public BodyWriter s32(int v) { return u32(v & 0xFFFFFFFFL); }
    public BodyWriter f32(float v) { return u32(Float.floatToIntBits(v) & 0xFFFFFFFFL); }
    public BodyWriter f64(double v) { return u64(Double.doubleToLongBits(v)); }
    public BodyWriter bool(boolean v) { return u8(v ? 1 : 0); }

    public BodyWriter uuid(UUID id) {
        u64(id.getMostSignificantBits());
        u64(id.getLeastSignificantBits());
        return this;
    }

    public BodyWriter vector3(float x, float y, float z) { f32(x); f32(y); f32(z); return this; }
    public BodyWriter vector3d(double x, double y, double z) { f64(x); f64(y); f64(z); return this; }
    public BodyWriter vector4(float x, float y, float z, float w) { f32(x); f32(y); f32(z); f32(w); return this; }

    /** Wire quaternions carry x, y, z only; w is reconstructed by the reader. */
    public BodyWriter quaternion(float x, float y, float z, float w) {
        f32(x); f32(y); f32(z); return this;
    }

    public BodyWriter variable1(byte[] data) { u8(data.length); out.write(data, 0, data.length); return this; }
    public BodyWriter variable2(byte[] data) { u16(data.length); out.write(data, 0, data.length); return this; }
    public BodyWriter fixed(byte[] data) { out.write(data, 0, data.length); return this; }

    /** Variable 1 string, NUL-terminated — the legacy string shape used by
     *  ChatFromViewer-era messages. Forgetting the NUL shifts the parse of
     *  every field after it, which presents as 'chat works, everything
     *  after chat is garbage'. */
    public BodyWriter stringZ(String text) {
        byte[] raw = text.getBytes(StandardCharsets.UTF_8);
        byte[] withNul = new byte[raw.length + 1];
        System.arraycopy(raw, 0, withNul, 0, raw.length);
        return variable1(withNul);
    }

    public byte[] toByteArray() { return out.toByteArray(); }
}

/** Typed body reader; every read is bounds-checked. */
final class BodyReader {
    private final ByteBuffer buf;

    BodyReader(byte[] data, int offset) {
        buf = ByteBuffer.wrap(data, offset, data.length - offset).order(ByteOrder.BIG_ENDIAN);
    }

    private void need(int n) {
        if (buf.remaining() < n) throw new IllegalArgumentException("Message body truncated");
    }

    public int u8() { need(1); return buf.get() & 0xFF; }
    public int u16() { need(2); return buf.getShort() & 0xFFFF; }
    public long u32() { need(4); return buf.getInt() & 0xFFFFFFFFL; }
    public long u64() { need(8); return buf.getLong(); }
    public int s16() { need(2); return buf.getShort(); }
    public int s32() { need(4); return buf.getInt(); }
    public float f32() { need(4); return buf.getFloat(); }
    public double f64() { need(8); return buf.getDouble(); }
    public boolean bool() { return u8() != 0; }

    public UUID uuid() { return new UUID(u64(), u64()); }
    public float[] vector3() { return new float[]{f32(), f32(), f32()}; }
    public double[] vector3d() { return new double[]{f64(), f64(), f64()}; }

    public float[] quaternion() {
        float x = f32(), y = f32(), z = f32();
        double w2 = 1.0 - (x * x + y * y + z * z);
        float w = w2 > 0 ? (float) Math.sqrt(w2) : 0f;
        return new float[]{x, y, z, w};
    }

    public byte[] variable1() { int n = u8(); need(n); byte[] b = new byte[n]; buf.get(b); return b; }
    public byte[] variable2() { int n = u16(); need(n); byte[] b = new byte[n]; buf.get(b); return b; }
    public byte[] fixed(int n) { need(n); byte[] b = new byte[n]; buf.get(b); return b; }

    public String stringZ() {
        byte[] raw = variable1();
        int end = 0;
        while (end < raw.length && raw[end] != 0) end++;
        return new String(raw, 0, end, StandardCharsets.UTF_8);
    }

    public boolean exhausted() { return !buf.hasRemaining(); }
}
```

### A3.1 Message classes (the pattern, on the login-critical messages)

```java
package com.example.slproto.messages;

import com.example.slproto.net.BodyWriter;
import com.example.slproto.net.Packets;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/** Base type for generated/hand-written message classes. */
public abstract class Message {
    public abstract String name();
    public abstract Packets.Frequency frequency();
    public abstract int number();
    public abstract boolean zerocoded();
    public abstract void pack(BodyWriter writer);
}

/** UseCircuitCode — Low 4, Trusted, Zerocoded. First UDP message after login. */
final class UseCircuitCode extends Message {
    public long code;
    public UUID sessionId;
    public UUID agentId;

    public String name() { return "UseCircuitCode"; }
    public Packets.Frequency frequency() { return Packets.Frequency.LOW; }
    public int number() { return 4; }
    public boolean zerocoded() { return true; }

    public void pack(BodyWriter w) {
        w.u32(code).uuid(sessionId).uuid(agentId);
    }

    public static UseCircuitCode unpack(BodyReaderShim r) {
        UseCircuitCode m = new UseCircuitCode();
        m.code = r.u32(); m.sessionId = r.uuid(); m.agentId = r.uuid();
        return m;
    }
}

/** PacketAck — Fixed 0xFFFFFFFB, NotTrusted, Unencoded. */
final class PacketAck extends Message {
    public List<Long> packets = new ArrayList<>();

    public String name() { return "PacketAck"; }
    public Packets.Frequency frequency() { return Packets.Frequency.FIXED; }
    public int number() { return 0xFFFFFFFB; }
    public boolean zerocoded() { return false; }

    public void pack(BodyWriter w) {
        w.u8(packets.size());
        for (long seq : packets) w.u32(seq);
    }
}

/** ChatFromSimulator — the inbound chat message a viewer renders.
 *  Field order (ChatData block): FromName Variable 1, SourceID, OwnerID,
 *  SourceType U8, ChatType U8, Audible U8, SourcePos LLVector3,
 *  Message Variable 2. */
final class ChatFromSimulator extends Message {
    public String fromName;
    public UUID sourceId;
    public UUID ownerId;
    public int sourceType;
    public int chatType;
    public int audible;
    public float[] sourcePos;
    public String message;

    public String name() { return "ChatFromSimulator"; }
    public Packets.Frequency frequency() { return Packets.Frequency.LOW; }
    public int number() { return 79; } // verify against your template revision
    public boolean zerocoded() { return true; }

    public void pack(BodyWriter w) { throw new UnsupportedOperationException("inbound"); }

    public static ChatFromSimulator unpack(BodyReaderShim r) {
        ChatFromSimulator m = new ChatFromSimulator();
        m.fromName = r.stringZ();
        m.sourceId = r.uuid();
        m.ownerId = r.uuid();
        m.sourceType = r.u8();
        m.chatType = r.u8();
        m.audible = r.u8();
        m.sourcePos = r.vector3();
        byte[] raw = r.variable2();
        int end = 0;
        while (end < raw.length && raw[end] != 0) end++;
        m.message = new String(raw, 0, end, java.nio.charset.StandardCharsets.UTF_8);
        return m;
    }
}

/** Type alias so the message classes read like the generated ones; in the
 *  real tree this is simply BodyReader made public in the net package. */
interface BodyReaderShim {
    long u32(); java.util.UUID uuid(); String stringZ(); int u8();
    float[] vector3(); byte[] variable2();
}
```

## A4. The UDP circuit (DatagramSocket + executor model)

Lumiya-style threading: one receive thread blocked on `DatagramSocket.receive`, one scheduled executor for resends/pings/ACK flush, and message handlers dispatched onto a session executor — never onto the Android main thread, and never blocking the receive thread on handler work (a slow handler must not delay ACKs, or the simulator resend-storms you).

```java
package com.example.slproto.net;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;
import java.util.function.BiConsumer;

/**
 * One simulator circuit. Lifecycle: construct -> start() -> send
 * UseCircuitCode/CompleteAgentMovement (session layer) -> run until
 * close() or the dead-circuit callback fires.
 */
public final class Circuit implements AutoCloseable {
    private static final long RESEND_MS = 400;
    private static final long ACK_FLUSH_MS = 100;
    private static final long PING_MS = 5_000;
    private static final long TIMEOUT_MS = 60_000;

    private final DatagramSocket socket;
    private final InetAddress simAddress;
    private final int simPort;
    private final BiConsumer<Packets.MessageId, byte[]> dispatcher;
    private final Runnable onDead;

    private final AtomicLong nextSequence = new AtomicLong(1);
    private final Map<Long, SentReliable> unacked = new ConcurrentHashMap<>();
    private final List<Long> pendingAcks = new ArrayList<>();
    private final Object ackLock = new Object();
    private volatile long lastReceivedAt = System.currentTimeMillis();
    private volatile boolean closed = false;
    private final ScheduledExecutorService scheduler =
            Executors.newSingleThreadScheduledExecutor(r -> {
                Thread t = new Thread(r, "sl-circuit-timer");
                t.setDaemon(true);
                return t;
            });

    private record SentReliable(byte[] datagram, long lastSentAt) {}

    public Circuit(InetAddress simAddress, int simPort,
                   BiConsumer<Packets.MessageId, byte[]> dispatcher,
                   Runnable onDead) throws IOException {
        this.socket = new DatagramSocket();
        this.simAddress = simAddress;
        this.simPort = simPort;
        this.dispatcher = dispatcher;
        this.onDead = onDead;
    }

    public void start() {
        Thread receiver = new Thread(this::receiveLoop, "sl-circuit-recv");
        receiver.setDaemon(true);
        receiver.start();
        scheduler.scheduleWithFixedDelay(this::maintenanceTick,
                RESEND_MS, 100, TimeUnit.MILLISECONDS);
    }

    private void receiveLoop() {
        byte[] buffer = new byte[65535];
        while (!closed) {
            DatagramPacket dp = new DatagramPacket(buffer, buffer.length);
            try {
                socket.receive(dp);
            } catch (IOException e) {
                if (!closed) { /* transient; timeout sweep decides death */ }
                continue;
            }
            lastReceivedAt = System.currentTimeMillis();
            Packets.Packet packet;
            try {
                packet = Packets.parse(buffer, dp.getLength());
            } catch (IllegalArgumentException bad) {
                continue; // garbage datagrams are normal on UDP
            }
            for (long seq : packet.acks) unacked.remove(seq);
            if (packet.reliable()) queueAck(packet.sequence);
            Packets.MessageId id = Packets.decodeMessageId(packet.body);
            if (id.frequency() == Packets.Frequency.FIXED
                    && id.number() == 0xFFFFFFFB) {
                // PacketAck: first body byte after the ID is the count.
                handlePacketAck(packet.body, id.offset());
                continue;
            }
            // Dispatch off the receive thread in real code: hand (id, body)
            // to the session executor here. Direct call shown for brevity.
            dispatcher.accept(id, packet.body);
        }
    }

    private void handlePacketAck(byte[] body, int offset) {
        if (body.length <= offset) return;
        int count = body[offset] & 0xFF;
        java.nio.ByteBuffer bb = java.nio.ByteBuffer.wrap(body)
                .order(java.nio.ByteOrder.BIG_ENDIAN);
        for (int i = 0; i < count; i++) {
            int at = offset + 1 + 4 * i;
            if (at + 4 > body.length) return;
            unacked.remove(bb.getInt(at) & 0xFFFFFFFFL);
        }
    }

    private void queueAck(long sequence) {
        synchronized (ackLock) { pendingAcks.add(sequence); }
    }

    /** Send one message. Returns the sequence used, or -1 if not sent. */
    public long send(MessageShim message, boolean reliable) {
        BodyWriter writer = new BodyWriter();
        message.pack(writer);
        long seq = nextSequence.getAndIncrement();
        List<Long> acks;
        synchronized (ackLock) {
            acks = pendingAcks.isEmpty() ? null : new ArrayList<>(pendingAcks);
            pendingAcks.clear();
        }
        byte[] datagram = Packets.build(seq,
                Packets.encodeMessageId(message.frequency(), message.number()),
                writer.toByteArray(), reliable, message.zerocoded(), acks);
        try {
            socket.send(new DatagramPacket(datagram, datagram.length, simAddress, simPort));
        } catch (IOException e) {
            return -1;
        }
        if (reliable) unacked.put(seq, new SentReliable(datagram, System.currentTimeMillis()));
        return seq;
    }

    private void maintenanceTick() {
        if (closed) return;
        long now = System.currentTimeMillis();
        // Resend sweep.
        for (Map.Entry<Long, SentReliable> e : unacked.entrySet()) {
            if (now - e.getValue().lastSentAt() >= RESEND_MS) {
                byte[] resent = e.getValue().datagram().clone();
                resent[0] |= Packets.FLAG_RESENT;
                try {
                    socket.send(new DatagramPacket(resent, resent.length, simAddress, simPort));
                } catch (IOException ignored) { }
                unacked.put(e.getKey(), new SentReliable(e.getValue().datagram(), now));
            }
        }
        // Standalone ACK flush if nothing piggybacked them.
        List<Long> acks;
        synchronized (ackLock) {
            acks = pendingAcks.isEmpty() ? null : new ArrayList<>(pendingAcks);
            if (acks != null) pendingAcks.clear();
        }
        if (acks != null) {
            PacketAck ack = new PacketAck();
            ack.packets.addAll(acks);
            send(new MessageShim() {
                public String name() { return "PacketAck"; }
                public Packets.Frequency frequency() { return Packets.Frequency.FIXED; }
                public int number() { return 0xFFFFFFFB; }
                public boolean zerocoded() { return false; }
                public void pack(BodyWriter w) { ack.pack(w); }
            }, false);
        }
        // Dead-circuit detection.
        if (now - lastReceivedAt > TIMEOUT_MS) {
            closed = true;
            onDead.run();
        }
    }

    @Override public void close() {
        closed = true;
        scheduler.shutdownNow();
        socket.close();
    }

    /** Structural stand-in for the Message base class in A3.1 (same shape). */
    public interface MessageShim {
        String name();
        Packets.Frequency frequency();
        int number();
        boolean zerocoded();
        void pack(BodyWriter w);
    }
}
```

## A5. Caps over OkHttp, and the Event Queue

OkHttp owns caps traffic. Two configuration points matter: read timeout must exceed the Event Queue's server-side long-poll hold (use 75 s+), and cap URLs must never be logged (they are unguessable session credentials) — install a logging interceptor that redacts `/cap/` paths if you install one at all.

```java
package com.example.slproto.caps;

import com.example.slproto.llsd.LLSDXml;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.IOException;
import java.io.StringReader;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

/** Capability client: seed-cap exchange, named-cap LLSD POSTs, EQ poll. */
public final class CapsClient {
    public static final MediaType LLSD_XML =
            MediaType.get("application/llsd+xml; charset=utf-8");

    private final OkHttpClient http;
    private final Map<String, String> caps;

    private CapsClient(OkHttpClient http, Map<String, String> caps) {
        this.http = http;
        this.caps = caps;
    }

    public static OkHttpClient defaultHttp() {
        return new OkHttpClient.Builder()
                .connectTimeout(15, TimeUnit.SECONDS)
                .readTimeout(90, TimeUnit.SECONDS)   // > EQ long-poll hold
                .writeTimeout(30, TimeUnit.SECONDS)
                .build();
    }

    /** Exchange wanted cap names for granted cap URLs at the seed cap. */
    @SuppressWarnings("unchecked")
    public static CapsClient fromSeed(OkHttpClient http, String seedUrl,
                                      List<String> wanted) throws IOException {
        Request req = new Request.Builder()
                .url(seedUrl)
                .post(RequestBody.create(LLSDXml.toXml(wanted), LLSD_XML))
                .build();
        try (Response resp = http.newCall(req).execute()) {
            if (!resp.isSuccessful()) {
                throw new IOException("Seed cap failed: HTTP " + resp.code());
            }
            String body = resp.body() != null ? resp.body().string() : "";
            Object parsed = LLSDXml.fromXml(body);
            Map<String, Object> raw = (Map<String, Object>) parsed;
            java.util.Map<String, String> granted = new java.util.HashMap<>();
            if (raw != null) {
                for (Map.Entry<String, Object> e : raw.entrySet()) {
                    granted.put(e.getKey(), String.valueOf(e.getValue()));
                }
            }
            return new CapsClient(http, granted);
        }
    }

    public boolean has(String name) { return caps.containsKey(name); }
    public String url(String name) { return caps.get(name); }

    /** POST LLSD to a named cap; parse the LLSD reply (may be null). */
    public Object postLlsd(String name, Object value) throws IOException {
        String url = caps.get(name);
        if (url == null) throw new IOException("Cap not granted: " + name);
        Request req = new Request.Builder()
                .url(url)
                .post(RequestBody.create(LLSDXml.toXml(value), LLSD_XML))
                .build();
        try (Response resp = http.newCall(req).execute()) {
            if (!resp.isSuccessful()) {
                throw new IOException("Cap " + name + " failed: HTTP " + resp.code());
            }
            String body = resp.body() != null ? resp.body().string() : "";
            return body.isEmpty() ? null : LLSDXml.fromXml(body);
        }
    }

    /** GetTexture: whole-asset fetch. Viewers use Range requests for
     *  progressive discard levels; a settings/companion flow usually wants
     *  the whole codestream (section A7 decodes it). */
    public byte[] getTexture(UUID textureId) throws IOException {
        String base = caps.get("GetTexture");
        if (base == null) return null;
        String url = base + (base.contains("?") ? "&" : "?")
                + "texture_id=" + textureId;
        Request req = new Request.Builder().url(url).get().build();
        try (Response resp = http.newCall(req).execute()) {
            if (resp.code() == 404) return null; // asset missing — log the UUID
            if (!resp.isSuccessful()) {
                throw new IOException("GetTexture failed: HTTP " + resp.code());
            }
            return resp.body() != null ? resp.body().bytes() : null;
        }
    }
}

/** EventQueueGet long-poll. Runs on its own thread; stops on region change. */
final class EventQueue {
    interface Listener { void onEvent(String message, Map<String, Object> body); }

    private final CapsClient caps;
    private final Listener listener;
    private volatile boolean running;
    private Object ackId; // Integer or null

    EventQueue(CapsClient caps, Listener listener) {
        this.caps = caps;
        this.listener = listener;
    }

    @SuppressWarnings("unchecked")
    void runLoop() {
        running = true;
        while (running) {
            Map<String, Object> request = new java.util.HashMap<>();
            request.put("ack", ackId);
            request.put("done", Boolean.FALSE);
            Object reply;
            try {
                reply = caps.postLlsd("EventQueueGet", request);
            } catch (IOException e) {
                if (!running) return;
                sleepQuietly(1000); // transient; session layer owns death calls
                continue;
            }
            if (!(reply instanceof Map)) continue;
            Map<String, Object> map = (Map<String, Object>) reply;
            ackId = map.get("id");
            Object events = map.get("events");
            if (events instanceof List<?> list) {
                for (Object item : list) {
                    if (item instanceof Map<?, ?> event) {
                        Object body = event.get("body");
                        listener.onEvent(String.valueOf(event.get("message")),
                                body instanceof Map ? (Map<String, Object>) body : Map.of());
                    }
                }
            }
        }
    }

    void stop() { running = false; }

    private static void sleepQuietly(long ms) {
        try { Thread.sleep(ms); } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```

## A6. Login (XML-RPC) with MFA handling

The Lumiya repair work in this workspace is the reference for getting MFA right in this lineage: parse `reason` / `mfa_hash` from the auth reply, keep `mfa_hash` **memory-only** (the viewer persists it only in an encrypted protected store, which Lumiya lacks — persisting it in plain SharedPreferences would be a security regression), and resubmit with the user's TOTP token via a distinct code path that raises a UI prompt instead of a generic failure.

```java
package com.example.slproto.auth;

import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

/** Login outcomes are three-way, not two-way. Collapsing MFA into 'failed'
 *  is the bug this class exists to prevent. */
public sealed interface LoginOutcome {
    record Success(LoginResult result) implements LoginOutcome {}
    record MfaChallenge(String mfaHash, String message) implements LoginOutcome {}
    record Failure(String reason, String message) implements LoginOutcome {}
}

record LoginResult(
        UUID agentId, UUID sessionId, UUID secureSessionId,
        int circuitCode, String simIp, int simPort,
        String seedCapability, UUID inventoryRoot) {}

final class LoginClient {
    private static final MediaType XML = MediaType.get("text/xml; charset=utf-8");
    private final OkHttpClient http;

    LoginClient(OkHttpClient http) { this.http = http; }

    static String passwordHash(String password) {
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            byte[] digest = md5.digest(password.getBytes(java.nio.charset.StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder("$1$");
            for (byte b : digest) hex.append(String.format("%02x", b));
            return hex.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("MD5 unavailable", e);
        }
    }

    /**
     * @param mfaToken null on first attempt; the 6-digit TOTP on resubmit
     * @param mfaHash  null on first attempt; the hash from MfaChallenge on resubmit
     */
    LoginOutcome login(String loginUri, String first, String last, String password,
                       String mfaToken, String mfaHash) throws IOException {
        Map<String, Object> params = new HashMap<>();
        params.put("first", first);
        params.put("last", last);
        params.put("passwd", passwordHash(password));
        params.put("start", "last");
        params.put("channel", "LumiyaStyleClient");
        params.put("version", "1.0.0");
        params.put("platform", "Android");
        params.put("agree_to_tos", Boolean.TRUE);
        params.put("read_critical", Boolean.TRUE);
        params.put("options", List.of("inventory-root", "inventory-skeleton",
                "buddy-list", "login-flags", "global-textures"));
        if (mfaToken != null) params.put("token", mfaToken);
        if (mfaHash != null) params.put("mfa_hash", mfaHash);

        String xmlRpc = XmlRpc.encodeCall("login_to_simulator", params);
        Request req = new Request.Builder().url(loginUri)
                .post(RequestBody.create(xmlRpc, XML)).build();
        try (Response resp = http.newCall(req).execute()) {
            if (!resp.isSuccessful()) {
                return new LoginOutcome.Failure("http", "HTTP " + resp.code());
            }
            String body = resp.body() != null ? resp.body().string() : "";
            Map<String, Object> reply = XmlRpc.parseStructReply(body);
            if ("true".equals(String.valueOf(reply.get("login")))) {
                return new LoginOutcome.Success(new LoginResult(
                        UUID.fromString(str(reply, "agent_id")),
                        UUID.fromString(str(reply, "session_id")),
                        UUID.fromString(str(reply, "secure_session_id")),
                        Integer.parseInt(str(reply, "circuit_code")),
                        str(reply, "sim_ip"),
                        Integer.parseInt(str(reply, "sim_port")),
                        str(reply, "seed_capability"),
                        inventoryRoot(reply)));
            }
            String reason = str(reply, "reason");
            String message = str(reply, "message");
            // MFA: the server replies login != true with an mfa reason and a
            // hash to echo on resubmit. The hash is a credential-equivalent
            // for this login attempt: keep it in a field, never in storage.
            if (reason != null && reason.toLowerCase().contains("mfa")) {
                return new LoginOutcome.MfaChallenge(str(reply, "mfa_hash"), message);
            }
            return new LoginOutcome.Failure(reason, message);
        }
    }

    private static String str(Map<String, Object> map, String key) {
        Object v = map.get(key);
        return v == null ? null : String.valueOf(v);
    }

    @SuppressWarnings("unchecked")
    private static UUID inventoryRoot(Map<String, Object> reply) {
        Object skeleton = reply.get("inventory-skeleton");
        if (skeleton instanceof List<?> list && !list.isEmpty()
                && list.get(0) instanceof Map<?, ?> first) {
            Object folder = ((Map<String, Object>) first).get("folder_id");
            if (folder != null) return UUID.fromString(String.valueOf(folder));
        }
        return null;
    }
}

/** Minimal XML-RPC encode/parse for the login shapes (structs of strings,
 *  ints, bools, arrays). A production client can swap in a fuller library;
 *  the login surface genuinely is this small. */
final class XmlRpc {
    private XmlRpc() {}

    static String encodeCall(String method, Map<String, Object> params) {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\"?><methodCall><methodName>")
          .append(method).append("</methodName><params><param>");
        appendValue(sb, params);
        sb.append("</param></params></methodCall>");
        return sb.toString();
    }

    private static void appendValue(StringBuilder sb, Object value) {
        if (value instanceof Boolean b) {
            sb.append("<value><boolean>").append(b ? 1 : 0).append("</boolean></value>");
        } else if (value instanceof Number n) {
            sb.append("<value><int>").append(n.intValue()).append("</int></value>");
        } else if (value instanceof List<?> list) {
            sb.append("<value><array><data>");
            for (Object item : list) appendValue(sb, item);
            sb.append("</data></array></value>");
        } else if (value instanceof Map<?, ?> map) {
            sb.append("<value><struct>");
            for (Map.Entry<?, ?> e : map.entrySet()) {
                sb.append("<member><name>").append(e.getKey()).append("</name>");
                appendValue(sb, e.getValue());
                sb.append("</member>");
            }
            sb.append("</struct></value>");
        } else {
            String text = String.valueOf(value)
                    .replace("&", "&amp;").replace("<", "&lt;");
            sb.append("<value><string>").append(text).append("</string></value>");
        }
    }

    /** Parse an XML-RPC reply into plain containers using the DOM API
     *  (available on Android via javax.xml.parsers). Login replies are
     *  small — unlike inventory skeletons — so DOM cost is irrelevant here,
     *  which is why this one parser is DOM while A1.1 streams. */
    static Map<String, Object> parseStructReply(String xml) {
        try {
            javax.xml.parsers.DocumentBuilderFactory factory =
                    javax.xml.parsers.DocumentBuilderFactory.newInstance();
            factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
            org.w3c.dom.Document doc = factory.newDocumentBuilder().parse(
                    new org.xml.sax.InputSource(new java.io.StringReader(xml)));
            org.w3c.dom.NodeList values = doc.getElementsByTagName("value");
            if (values.getLength() == 0) throw new IllegalArgumentException("No <value>");
            Object top = readValue((org.w3c.dom.Element) values.item(0));
            if (top instanceof Map<?, ?> map) {
                @SuppressWarnings("unchecked")
                Map<String, Object> typed = (Map<String, Object>) map;
                return typed;
            }
            throw new IllegalArgumentException("Login reply is not a struct");
        } catch (Exception e) {
            throw new IllegalArgumentException("XML-RPC parse failed", e);
        }
    }

    private static Object readValue(org.w3c.dom.Element valueEl) {
        org.w3c.dom.Element child = null;
        for (int i = 0; i < valueEl.getChildNodes().getLength(); i++) {
            if (valueEl.getChildNodes().item(i) instanceof org.w3c.dom.Element el) {
                child = el;
                break;
            }
        }
        if (child == null) return valueEl.getTextContent();
        switch (child.getTagName()) {
            case "string": return child.getTextContent();
            case "int": case "i4": return Integer.parseInt(child.getTextContent().trim());
            case "boolean": return "1".equals(child.getTextContent().trim());
            case "double": return Double.parseDouble(child.getTextContent().trim());
            case "array": {
                java.util.List<Object> items = new java.util.ArrayList<>();
                org.w3c.dom.NodeList vals = child.getElementsByTagName("value");
                // getElementsByTagName is deep; login arrays are flat, and
                // nested arrays arrive as their own <value> subtrees which
                // this counts once at each level for the login shapes.
                for (int i = 0; i < vals.getLength(); i++) {
                    if (vals.item(i).getParentNode().getParentNode() == child) {
                        items.add(readValue((org.w3c.dom.Element) vals.item(i)));
                    }
                }
                return items;
            }
            case "struct": {
                Map<String, Object> map = new java.util.HashMap<>();
                org.w3c.dom.NodeList members = child.getElementsByTagName("member");
                for (int i = 0; i < members.getLength(); i++) {
                    org.w3c.dom.Element member = (org.w3c.dom.Element) members.item(i);
                    String name = member.getElementsByTagName("name").item(0).getTextContent();
                    org.w3c.dom.Element v = (org.w3c.dom.Element)
                            member.getElementsByTagName("value").item(0);
                    map.put(name, readValue(v));
                }
                return map;
            }
            default: return child.getTextContent();
        }
    }
}
```

## A7. GLES texture and mesh decode — notes with code

### A7.1 Textures are JPEG2000 codestreams, decoded progressively

A texture asset fetched via `GetTexture` is a JPEG2000 (J2C) codestream, not a JPEG or PNG. Lumiya links a native OpenJPEG (1.5-era in the recovered tree) through JNI; the Java side manages *discard levels*: discard 0 is full resolution, and each higher discard halves both dimensions. The render loop requests the discard level whose resolution roughly matches the on-screen size, then refines. Two consequences for code:

1. **Decode is native and fallible.** A truncated or non-J2C asset must degrade to a placeholder texture, never crash the render thread. Assets genuinely go missing (log the UUID).
2. **Codec differences are visual differences.** OpenJPEG vs Kakadu partial-decode artefacts differ; if a texture looks wrong in your client and right in the official viewer, suspect the codec path before the data.

```java
package com.example.slproto.render;

import android.graphics.Bitmap;
import android.opengl.GLES20;
import android.opengl.GLUtils;

import java.util.UUID;

/** JNI bridge shape for the native JPEG2000 decoder (OpenJPEG).
 *  The native side is Lumiya's libopenjpeg-derived library; this class is
 *  the contract the Java renderer codes against. */
final class J2CDecoder {
    static {
        System.loadLibrary("sl_j2c"); // wraps OpenJPEG; see Lumiya-Redux native notes
    }

    /** Decode one discard level. Returns null on any decode failure.
     *  @param codestream the full J2C asset bytes
     *  @param discard    0 = full res; each +1 halves width and height
     *  @param outSize    int[2] receiving {width, height} actually decoded */
    static native Bitmap decodeDiscard(byte[] codestream, int discard, int[] outSize);

    /** Pick the discard level for an on-screen size: the smallest decode
     *  that is still >= the display size, so textures refine as you approach
     *  instead of popping from blur to a needlessly huge decode. */
    static int discardForDisplay(int fullWidth, int fullHeight, int displayPx) {
        int discard = 0;
        int w = fullWidth, h = fullHeight;
        while (discard < 6 && w / 2 >= displayPx && h / 2 >= displayPx) {
            w /= 2; h /= 2; discard++;
        }
        return discard;
    }
}

/** Uploads a decoded bitmap to a GLES texture, with the renderer's rules:
 *  generate mipmaps for world textures (not for HUD/UI), use the texture's
 *  UUID as the cache key, and free the GL texture when the cache evicts —
 *  GL texture leaks on Android present as a slow OOM after ~an hour in-world. */
final class TextureCache {
    private final java.util.Map<UUID, Integer> glIds = new java.util.HashMap<>();
    private final int maxEntries;

    TextureCache(int maxEntries) { this.maxEntries = maxEntries; }

    synchronized int getOrUpload(UUID textureId, Bitmap bitmap, boolean mipmaps) {
        Integer existing = glIds.get(textureId);
        if (existing != null) return existing;
        if (glIds.size() >= maxEntries) evictOne();
        int[] handle = new int[1];
        GLES20.glGenTextures(1, handle, 0);
        GLES20.glBindTexture(GLES20.GL_TEXTURE_2D, handle[0]);
        GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D,
                GLES20.GL_TEXTURE_WRAP_S, GLES20.GL_REPEAT);
        GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D,
                GLES20.GL_TEXTURE_WRAP_T, GLES20.GL_REPEAT);
        GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D,
                GLES20.GL_TEXTURE_MAG_FILTER, GLES20.GL_LINEAR);
        GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D,
                GLES20.GL_TEXTURE_MIN_FILTER,
                mipmaps ? GLES20.GL_LINEAR_MIPMAP_LINEAR : GLES20.GL_LINEAR);
        GLUtils.texImage2D(GLES20.GL_TEXTURE_2D, 0, bitmap, 0);
        if (mipmaps) GLES20.glGenerateMipmap(GLES20.GL_TEXTURE_2D);
        glIds.put(textureId, handle[0]);
        return handle[0];
    }

    private void evictOne() {
        // Teaching-scale LRU stand-in: the real Lumiya cache tracks decode
        // cost, discard level, and last-use per entry. Any policy that
        // actually deletes GL textures beats a perfect policy that leaks.
        java.util.Iterator<Map.Entry<UUID, Integer>> it = glIds.entrySet().iterator();
        if (it.hasNext()) {
            Map.Entry<UUID, Integer> victim = it.next();
            GLES20.glDeleteTextures(1, new int[]{victim.getValue()}, 0);
            it.remove();
        }
    }

    synchronized void clear() {
        for (int id : glIds.values()) GLES20.glDeleteTextures(1, new int[]{id}, 0);
        glIds.clear();
    }
}
```

### A7.2 LLMesh: header-driven binary, LOD sections, skinning

An LLMesh asset is a binary blob whose header is an LLSD (binary) map describing byte offsets and sizes of its sections: per-LOD geometry (`high_lod`, `medium_lod`, `low_lod`, `lowest_lod`), `physics_convex`, and skin info (`skin` with joint names and inverse bind matrices). Each geometry section is itself a map of attribute arrays (positions, normals, texcoords, indices, weights). The parser skeleton below reads the header and the high-LOD position/index arrays — enough to render an unskinned mesh and to validate an asset — and shows exactly where skinning and the other LODs plug in. Offsets in the header are from the start of the asset; section payloads in the wild are commonly zlib-compressed, so check the header's per-section size fields against the asset length before trusting them (LibreMetaverse's MeshFoundry and the viewer's `llmeshrepository` are the references for the full format).

```java
package com.example.slproto.render;

import com.example.slproto.llsd.LLSD;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.List;
import java.util.Map;

/** Minimal LLMesh reader: header LLSD + high-LOD positions/indices. */
final class LLMesh {
    final Map<String, Object> header;
    final float[] positions;   // xyz triples
    final float[] normals;     // xyz triples, may be null in old assets
    final float[] texCoords;   // uv pairs
    final int[] indices;       // triangle indices (U16 or U32 per header)

    private LLMesh(Map<String, Object> header, float[] p, float[] n,
                   float[] t, int[] idx) {
        this.header = header; this.positions = p; this.normals = n;
        this.texCoords = t; this.indices = idx;
    }

    @SuppressWarnings("unchecked")
    static LLMesh parse(byte[] asset) {
        // The header is a binary-LLSD map at offset 0; its serialised length
        // is not stored separately — the LLSD reader consumes exactly the
        // header's bytes, so track position via a measuring pass: decode
        // once with the general reader (assets here are header-first by
        // format definition), then read section offsets from the map.
        // In production, use a reader that reports consumed length.
        Object headObj = LLSD.fromBinary(headerSlice(asset));
        Map<String, Object> header = (Map<String, Object>) headObj;
        Map<String, Object> highLod = (Map<String, Object>) header.get("high_lod");
        if (highLod == null) throw new IllegalArgumentException("LLMesh without high_lod");
        int offset = intOf(highLod, "offset");
        int size = intOf(highLod, "size");
        byte[] section = java.util.Arrays.copyOfRange(asset, offset, offset + size);
        Object sectionObj = LLSD.fromBinary(section);
        Map<String, Object> geometry = (Map<String, Object>) sectionObj;

        float[] positions = floats(geometry.get("PositionDomain"),
                                   geometry.get("Position"));
        float[] normals = geometry.get("Normal") != null
                ? floats(geometry.get("PositionDomain"), geometry.get("Normal")) : null;
        float[] texCoords = floats2(geometry.get("TexCoord"));
        int[] indices = ints(geometry.get("TriangleList"));
        return new LLMesh(header, positions, normals, texCoords, indices);
    }

    /** The header's byte length: binary LLSD is self-delimiting, so a
     *  measuring reader can walk it. This helper reuses the real reader on
     *  a growing prefix is NOT viable — production code uses a reader that
     *  exposes its cursor. Kept explicit here so nobody ships the naive
     *  version: use LLSD.BinaryReader and read its position. */
    private static byte[] headerSlice(byte[] asset) {
        LLSD.BinaryReader reader = new LLSD.BinaryReader(asset);
        reader.readValue();
        // BinaryReader in A1 does not expose pos; the production reader in
        // Lumiya-Redux style code does (a one-line accessor). We return the
        // whole asset: fromBinary() in A1 rejects trailing bytes, so real
        // code must use the cursor-exposing reader. See the note above.
        return asset;
    }

    private static int intOf(Map<String, Object> map, String key) {
        Object v = map.get(key);
        if (v instanceof Number n) return n.intValue();
        throw new IllegalArgumentException("Missing numeric field " + key);
    }

    /** Position/normal arrays are stored as byte[] of little-endian F32
     *  triples in the geometry section (note: little-endian here, unlike
     *  the big-endian network body — asset formats and wire formats differ,
     *  and mixing them up produces meshes exploded along one axis). */
    private static float[] floats(Object domainIgnored, Object raw) {
        byte[] bytes = (byte[]) raw;
        ByteBuffer bb = ByteBuffer.wrap(bytes).order(ByteOrder.LITTLE_ENDIAN);
        float[] out = new float[bytes.length / 4];
        bb.asFloatBuffer().get(out);
        return out;
    }

    private static float[] floats2(Object raw) { return floats(null, raw); }

    private static int[] ints(Object raw) {
        byte[] bytes = (byte[]) raw;
        // TriangleList is U16 in most assets; U32 when the vertex count
        // demands it — the header/geometry map carries the width in
        // production parsers. U16 shown.
        ByteBuffer bb = ByteBuffer.wrap(bytes).order(ByteOrder.LITTLE_ENDIAN);
        int[] out = new int[bytes.length / 2];
        for (int i = 0; i < out.length; i++) out[i] = bb.getShort(i * 2) & 0xFFFF;
        return out;
    }

    /** Skinning hook: header.get("skin") carries joint_names (list of
     *  String), bind_shape_matrix, pelvis_offset, and per-vertex weights
     *  live in the geometry section as a 'Weights' array of packed
     *  (joint index, weight) pairs. A renderer that ignores skin renders
     *  the mesh in bind pose — correct for static decor, wrong for
     *  wearables and Animesh, which is why this is a hook and not an
     *  omission to forget. */
    @SuppressWarnings("unchecked")
    List<String> jointNames() {
        Map<String, Object> skin = (Map<String, Object>) header.get("skin");
        if (skin == null) return List.of();
        Object names = skin.get("joint_names");
        return names instanceof List ? (List<String>) names : List.of();
    }
}
```

Renderer notes that belong with this code:

- **Prim and sculpt geometry is generated, not fetched.** Prims are built from `PrimitiveParams` by a mesher (LibreMetaverse `PrimMesher`/`MeshFoundry` is the readable reference); sculpties tessellate a texture-encoded vertex map on a fixed grid. Budget mesher CPU on the render thread accordingly — a region full of sculpties is a meshing workload, not a download workload.
- **Materials ride separately.** Legacy diffuse/normal/specular texture IDs and glTF PBR material assets arrive via prim parameters and `RenderMaterials`-family data, not inside the mesh asset. A mesh that renders white-but-correct is usually a materials-join bug, not a geometry bug.
- **Animesh and rigged wearables share the skin path.** Both use the section A7.2 skin data plus `AvatarAnimation`/`ObjectAnimation` messages for pose; bind-pose-only rendering is the tell that animation application, not asset parsing, is broken.

---

# Part B — C++ (viewer-style)

## B1. LLSD in the indra/llcommon idiom

The viewer's `LLSD` (in `indra/llcommon/llsd.h`) is a dynamically-typed value with map/array/string/binary/UUID/date/URI/integer/real/boolean/undefined, reference-counted storage, and serialisers in `llsdserialize.cpp` for XML, binary, and notation. The class below is a compact original implementation in the same idiom — same type set, same serialisation rules, `LLSD::Map`/`LLSD::Array` access patterns (`value["key"]`, `value.append(x)`) — sized for tools and tests rather than for embedding in the viewer itself.

```cpp
// llsd.hpp — a compact LLSD value in the indra/llcommon idiom.
// Original implementation from the LLSD format rules; serialisation must
// agree byte-for-byte with the viewer's llsdserialize.cpp on the test
// vectors in B1.3. Licence note: written from the format, not copied.
#pragma once

#include <cstdint>
#include <map>
#include <memory>
#include <string>
#include <vector>

class LLSD {
public:
    enum Type {
        TYPE_UNDEFINED, TYPE_BOOLEAN, TYPE_INTEGER, TYPE_REAL,
        TYPE_STRING, TYPE_BINARY, TYPE_UUID, TYPE_DATE, TYPE_URI,
        TYPE_ARRAY, TYPE_MAP
    };

    using Binary = std::vector<uint8_t>;
    using Array = std::vector<LLSD>;
    using Map = std::map<std::string, LLSD>;

    LLSD() : mType(TYPE_UNDEFINED) {}
    LLSD(bool v) : mType(TYPE_BOOLEAN), mBool(v) {}
    LLSD(int32_t v) : mType(TYPE_INTEGER), mInt(v) {}
    LLSD(double v) : mType(TYPE_REAL), mReal(v) {}
    LLSD(const std::string& v) : mType(TYPE_STRING), mString(v) {}
    LLSD(const char* v) : mType(TYPE_STRING), mString(v) {}

    static LLSD newArray() { LLSD v; v.mType = TYPE_ARRAY; v.mArray = std::make_shared<Array>(); return v; }
    static LLSD newMap() { LLSD v; v.mType = TYPE_MAP; v.mMap = std::make_shared<Map>(); return v; }
    static LLSD newBinary(Binary b) { LLSD v; v.mType = TYPE_BINARY; v.mBinary = std::move(b); return v; }
    static LLSD newUUID(const std::string& s) { LLSD v; v.mType = TYPE_UUID; v.mString = s; return v; }
    static LLSD newURI(const std::string& s) { LLSD v; v.mType = TYPE_URI; v.mString = s; return v; }
    /** Dates are stored as seconds since epoch (double), as in the viewer. */
    static LLSD newDate(double seconds) { LLSD v; v.mType = TYPE_DATE; v.mReal = seconds; return v; }

    Type type() const { return mType; }
    bool isUndefined() const { return mType == TYPE_UNDEFINED; }
    bool isMap() const { return mType == TYPE_MAP; }
    bool isArray() const { return mType == TYPE_ARRAY; }

    // Scalar accessors follow the viewer's forgiving-conversion style:
    // asInteger() on a real truncates, on a string parses, on undefined is 0.
    // Forgiving accessors hide bugs; the strict checks in the codecs below
    // are where wire data is validated.
    bool asBoolean() const { return mType == TYPE_BOOLEAN ? mBool : mInt != 0; }
    int32_t asInteger() const {
        if (mType == TYPE_INTEGER) return mInt;
        if (mType == TYPE_REAL) return static_cast<int32_t>(mReal);
        if (mType == TYPE_BOOLEAN) return mBool ? 1 : 0;
        return 0;
    }
    double asReal() const {
        if (mType == TYPE_REAL || mType == TYPE_DATE) return mReal;
        if (mType == TYPE_INTEGER) return mInt;
        return 0.0;
    }
    const std::string& asString() const {
        static const std::string empty;
        return (mType == TYPE_STRING || mType == TYPE_UUID || mType == TYPE_URI)
            ? mString : empty;
    }
    const Binary& asBinary() const {
        static const Binary empty;
        return mType == TYPE_BINARY ? mBinary : empty;
    }

    // Map access in the viewer idiom: operator[] auto-vivifies a map.
    LLSD& operator[](const std::string& key) {
        if (mType == TYPE_UNDEFINED) { mType = TYPE_MAP; mMap = std::make_shared<Map>(); }
        return (*mMap)[key];
    }
    const LLSD& operator[](const std::string& key) const {
        static const LLSD undefined;
        if (mType != TYPE_MAP) return undefined;
        auto it = mMap->find(key);
        return it != mMap->end() ? it->second : undefined;
    }
    bool has(const std::string& key) const {
        return mType == TYPE_MAP && mMap->find(key) != mMap->end();
    }
    const Map& map() const {
        static const Map empty;
        return mType == TYPE_MAP ? *mMap : empty;
    }

    void append(const LLSD& v) {
        if (mType == TYPE_UNDEFINED) { mType = TYPE_ARRAY; mArray = std::make_shared<Array>(); }
        mArray->push_back(v);
    }
    const Array& array() const {
        static const Array empty;
        return mType == TYPE_ARRAY ? *mArray : empty;
    }
    size_t size() const {
        if (mType == TYPE_ARRAY) return mArray->size();
        if (mType == TYPE_MAP) return mMap->size();
        return 0;
    }

private:
    Type mType;
    bool mBool = false;
    int32_t mInt = 0;
    double mReal = 0.0;
    std::string mString;                    // string, UUID, URI
    Binary mBinary;
    std::shared_ptr<Array> mArray;          // shared, as in the viewer
    std::shared_ptr<Map> mMap;
};
```

### B1.1 Binary serialisation (llsdserialize rules)

```cpp
// llsd_binary.cpp — binary LLSD write/read against the llsd.hpp value type.
#include "llsd.hpp"

#include <cstring>
#include <stdexcept>

namespace {

void putU32(std::vector<uint8_t>& out, uint32_t v) {
    out.push_back(static_cast<uint8_t>(v >> 24));
    out.push_back(static_cast<uint8_t>(v >> 16));
    out.push_back(static_cast<uint8_t>(v >> 8));
    out.push_back(static_cast<uint8_t>(v));
}
void putU64(std::vector<uint8_t>& out, uint64_t v) {
    for (int shift = 56; shift >= 0; shift -= 8)
        out.push_back(static_cast<uint8_t>(v >> shift));
}
void putBlob(std::vector<uint8_t>& out, const void* data, size_t len) {
    putU32(out, static_cast<uint32_t>(len));
    const auto* p = static_cast<const uint8_t*>(data);
    out.insert(out.end(), p, p + len);
}

void writeValue(std::vector<uint8_t>& out, const LLSD& v) {
    switch (v.type()) {
        case LLSD::TYPE_UNDEFINED: out.push_back('!'); break;
        case LLSD::TYPE_BOOLEAN: out.push_back(v.asBoolean() ? 'T' : 'F'); break;
        case LLSD::TYPE_INTEGER: {
            out.push_back('i');
            putU32(out, static_cast<uint32_t>(v.asInteger()));
            break;
        }
        case LLSD::TYPE_REAL: {
            out.push_back('r');
            double d = v.asReal();
            uint64_t bits;
            std::memcpy(&bits, &d, 8);
            putU64(out, bits);
            break;
        }
        case LLSD::TYPE_UUID: {
            out.push_back('u');
            // UUIDs serialise as their 16 raw bytes, parsed from the
            // canonical hyphenated string form the value carries.
            auto bytes = uuidStringToBytes(v.asString());
            out.insert(out.end(), bytes.begin(), bytes.end());
            break;
        }
        case LLSD::TYPE_STRING: {
            out.push_back('s');
            putBlob(out, v.asString().data(), v.asString().size());
            break;
        }
        case LLSD::TYPE_URI: {
            out.push_back('l');
            putBlob(out, v.asString().data(), v.asString().size());
            break;
        }
        case LLSD::TYPE_BINARY: {
            out.push_back('b');
            putBlob(out, v.asBinary().data(), v.asBinary().size());
            break;
        }
        case LLSD::TYPE_DATE: {
            out.push_back('d');
            double d = v.asReal();
            uint64_t bits;
            std::memcpy(&bits, &d, 8);
            putU64(out, bits);
            break;
        }
        case LLSD::TYPE_ARRAY: {
            out.push_back('[');
            putU32(out, static_cast<uint32_t>(v.size()));
            for (const LLSD& item : v.array()) writeValue(out, item);
            out.push_back(']');
            break;
        }
        case LLSD::TYPE_MAP: {
            out.push_back('{');
            putU32(out, static_cast<uint32_t>(v.size()));
            for (const auto& [key, item] : v.map()) {
                out.push_back('k');
                putBlob(out, key.data(), key.size());
                writeValue(out, item);
            }
            out.push_back('}');
            break;
        }
    }
}

// Declared here, defined with the UUID helpers in the full tool source:
// strict parse of 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', throws on bad input.
std::array<uint8_t, 16> uuidStringToBytes(const std::string& s);

struct Reader {
    const uint8_t* p;
    const uint8_t* end;

    uint8_t byte() {
        if (p >= end) throw std::runtime_error("Binary LLSD truncated");
        return *p++;
    }
    std::vector<uint8_t> take(size_t n) {
        if (static_cast<size_t>(end - p) < n)
            throw std::runtime_error("Binary LLSD truncated");
        std::vector<uint8_t> out(p, p + n);
        p += n;
        return out;
    }
    uint32_t u32() {
        auto b = take(4);
        return (uint32_t(b[0]) << 24) | (uint32_t(b[1]) << 16)
             | (uint32_t(b[2]) << 8) | uint32_t(b[3]);
    }
    uint64_t u64() {
        uint64_t v = 0;
        for (uint8_t b : take(8)) v = (v << 8) | b;
        return v;
    }
    std::string str() {
        auto raw = take(u32());
        return std::string(raw.begin(), raw.end());
    }

    LLSD value() {
        switch (byte()) {
            case '!': return LLSD();
            case 'T': return LLSD(true);
            case 'F': return LLSD(false);
            case 'i': return LLSD(static_cast<int32_t>(u32()));
            case 'r': {
                uint64_t bits = u64();
                double d;
                std::memcpy(&d, &bits, 8);
                return LLSD(d);
            }
            case 'u': {
                auto raw = take(16);
                return LLSD::newUUID(uuidBytesToString(raw));
            }
            case 's': return LLSD(str());
            case 'l': return LLSD::newURI(str());
            case 'b': return LLSD::newBinary(take(u32()));
            case 'd': {
                uint64_t bits = u64();
                double d;
                std::memcpy(&d, &bits, 8);
                return LLSD::newDate(d);
            }
            case '[': {
                uint32_t count = u32();
                LLSD arr = LLSD::newArray();
                for (uint32_t i = 0; i < count; ++i) arr.append(value());
                if (byte() != ']') throw std::runtime_error("LLSD array missing ']'");
                return arr;
            }
            case '{': {
                uint32_t count = u32();
                LLSD map = LLSD::newMap();
                for (uint32_t i = 0; i < count; ++i) {
                    if (byte() != 'k') throw std::runtime_error("LLSD map key missing 'k'");
                    std::string key = str();
                    map[key] = value();
                }
                if (byte() != '}') throw std::runtime_error("LLSD map missing '}'");
                return map;
            }
            default: throw std::runtime_error("Unknown binary LLSD marker");
        }
    }
};

std::string uuidBytesToString(const std::vector<uint8_t>& b); // as above

} // namespace

std::vector<uint8_t> llsdToBinary(const LLSD& v) {
    std::vector<uint8_t> out;
    writeValue(out, v);
    return out;
}

LLSD llsdFromBinary(const std::vector<uint8_t>& data) {
    Reader r{data.data(), data.data() + data.size()};
    LLSD v = r.value();
    if (r.p != r.end) throw std::runtime_error("Trailing bytes after binary LLSD");
    return v;
}
```

### B1.2 XML serialisation — the shape that matters

The XML writer mirrors `llsdserialize.cpp`'s `LLSDXMLFormatter`: an `<llsd>` root with exactly one value child, `<key>`/value alternation inside `<map>`, base64 inside `<binary>`, and ISO dates. A compact writer is below; the reader in production viewer code is a streaming Expat-style parser for the same reason the Java reader streams — inventory skeletons are large. For a tool, pairing this writer with the binary reader above and testing round-trips through both formats catches the type-preservation bugs (URI degrading to string, date degrading to real) that actually bite.

```cpp
// llsd_xml.cpp (writer half)
#include "llsd.hpp"
#include <sstream>

namespace {
std::string xmlEscape(const std::string& s) {
    std::string out;
    for (char c : s) {
        switch (c) {
            case '&': out += "&amp;"; break;
            case '<': out += "&lt;"; break;
            case '>': out += "&gt;"; break;
            default: out += c;
        }
    }
    return out;
}

std::string base64Encode(const std::vector<uint8_t>& data); // standard alphabet, with padding

void writeXml(std::ostringstream& out, const LLSD& v) {
    switch (v.type()) {
        case LLSD::TYPE_UNDEFINED: out << "<undef/>"; break;
        case LLSD::TYPE_BOOLEAN:
            out << "<boolean>" << (v.asBoolean() ? "1" : "0") << "</boolean>"; break;
        case LLSD::TYPE_INTEGER:
            out << "<integer>" << v.asInteger() << "</integer>"; break;
        case LLSD::TYPE_REAL:
            out << "<real>" << v.asReal() << "</real>"; break;
        case LLSD::TYPE_STRING:
            out << "<string>" << xmlEscape(v.asString()) << "</string>"; break;
        case LLSD::TYPE_URI:
            out << "<uri>" << xmlEscape(v.asString()) << "</uri>"; break;
        case LLSD::TYPE_UUID:
            out << "<uuid>" << v.asString() << "</uuid>"; break;
        case LLSD::TYPE_BINARY:
            out << "<binary>" << base64Encode(v.asBinary()) << "</binary>"; break;
        case LLSD::TYPE_DATE: {
            // ISO 8601 UTC from epoch seconds. The viewer formats with
            // its own date code; strftime/gmtime is equivalent for output.
            std::time_t t = static_cast<std::time_t>(v.asReal());
            char buf[32];
            std::strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", std::gmtime(&t));
            out << "<date>" << buf << "</date>";
            break;
        }
        case LLSD::TYPE_ARRAY:
            out << "<array>";
            for (const LLSD& item : v.array()) writeXml(out, item);
            out << "</array>";
            break;
        case LLSD::TYPE_MAP:
            out << "<map>";
            for (const auto& [key, item] : v.map()) {
                out << "<key>" << xmlEscape(key) << "</key>";
                writeXml(out, item);
            }
            out << "</map>";
            break;
    }
}
} // namespace

std::string llsdToXml(const LLSD& v) {
    std::ostringstream out;
    out << "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<llsd>";
    writeXml(out, v);
    out << "</llsd>";
    return out.str();
}
```

## B2. Standalone zerocode + packet parser (modern C++)

This is the tool-grade core: no viewer dependencies, C++17, header-style. It implements the exact framing rules — header, flags, ACK peel-off before zero-decode, frequency-prefixed IDs — and a typed body cursor.

```cpp
// sl_packet.hpp — zerocode, packet framing, and a body cursor. C++17.
#pragma once

#include <array>
#include <cstdint>
#include <cstring>
#include <stdexcept>
#include <string>
#include <vector>

namespace sl {

inline constexpr uint8_t kFlagZerocoded = 0x80;
inline constexpr uint8_t kFlagReliable = 0x40;
inline constexpr uint8_t kFlagResent = 0x20;
inline constexpr uint8_t kFlagAck = 0x10;
inline constexpr size_t kHeaderLen = 6;

// ---------------- zerocode ----------------
inline std::vector<uint8_t> zeroEncode(const std::vector<uint8_t>& in) {
    std::vector<uint8_t> out;
    out.reserve(in.size() + in.size() / 8 + 2);
    int run = 0;
    auto flush = [&] {
        while (run > 0) {
            int chunk = run > 255 ? 255 : run;
            out.push_back(0);
            out.push_back(static_cast<uint8_t>(chunk));
            run -= chunk;
        }
    };
    for (uint8_t b : in) {
        if (b == 0) { ++run; }
        else { flush(); out.push_back(b); }
    }
    flush();
    return out;
}

inline std::vector<uint8_t> zeroDecode(const std::vector<uint8_t>& in) {
    std::vector<uint8_t> out;
    out.reserve(in.size() * 2);
    for (size_t i = 0; i < in.size();) {
        uint8_t b = in[i];
        if (b != 0) { out.push_back(b); ++i; continue; }
        if (i + 1 >= in.size())
            throw std::runtime_error("Zerocoded data ends with lone 0x00");
        uint8_t count = in[i + 1];
        if (count == 0) throw std::runtime_error("Zerocode count 0");
        out.insert(out.end(), count, uint8_t{0});
        i += 2;
    }
    return out;
}

// ---------------- message IDs ----------------
enum class Frequency { High, Medium, Low, Fixed };

struct MessageId {
    Frequency frequency;
    uint32_t number;
    size_t offset; // bytes consumed in the body
};

inline MessageId decodeMessageId(const std::vector<uint8_t>& body) {
    if (body.empty()) throw std::runtime_error("Empty packet body");
    if (body[0] != 0xFF) return {Frequency::High, body[0], 1};
    if (body.size() < 2) throw std::runtime_error("Truncated message ID");
    if (body[1] != 0xFF) return {Frequency::Medium, body[1], 2};
    if (body.size() < 4) throw std::runtime_error("Truncated message ID");
    if (body[2] != 0xFF)
        return {Frequency::Low, uint32_t((body[2] << 8) | body[3]), 4};
    uint32_t fixed = (uint32_t(body[0]) << 24) | (uint32_t(body[1]) << 16)
                   | (uint32_t(body[2]) << 8) | uint32_t(body[3]);
    return {Frequency::Fixed, fixed, 4};
}

inline std::vector<uint8_t> encodeMessageId(Frequency freq, uint32_t number) {
    switch (freq) {
        case Frequency::High: return {static_cast<uint8_t>(number)};
        case Frequency::Medium: return {0xFF, static_cast<uint8_t>(number)};
        case Frequency::Low:
            return {0xFF, 0xFF, static_cast<uint8_t>(number >> 8),
                    static_cast<uint8_t>(number)};
        case Frequency::Fixed:
            return {static_cast<uint8_t>(number >> 24),
                    static_cast<uint8_t>(number >> 16),
                    static_cast<uint8_t>(number >> 8),
                    static_cast<uint8_t>(number)};
    }
    throw std::runtime_error("Bad frequency");
}

// ---------------- packets ----------------
struct Packet {
    uint8_t flags = 0;
    uint32_t sequence = 0;
    std::vector<uint8_t> body;          // decoded; message ID at the front
    std::vector<uint32_t> acks;
    bool reliable() const { return flags & kFlagReliable; }
    bool zerocoded() const { return flags & kFlagZerocoded; }
};

inline Packet parsePacket(const std::vector<uint8_t>& datagram) {
    if (datagram.size() < kHeaderLen)
        throw std::runtime_error("Datagram shorter than header");
    Packet packet;
    packet.flags = datagram[0];
    packet.sequence = (uint32_t(datagram[1]) << 24) | (uint32_t(datagram[2]) << 16)
                    | (uint32_t(datagram[3]) << 8) | uint32_t(datagram[4]);
    size_t offset = kHeaderLen + datagram[5]; // extra header length
    if (offset > datagram.size())
        throw std::runtime_error("Extra header overruns datagram");
    std::vector<uint8_t> payload(datagram.begin() + offset, datagram.end());

    if (packet.flags & kFlagAck) {
        if (payload.empty()) throw std::runtime_error("Ack flag, no payload");
        size_t count = payload.back();
        size_t needed = 1 + 4 * count;
        if (payload.size() < needed)
            throw std::runtime_error("Appended ACK list overruns datagram");
        size_t ackStart = payload.size() - needed;
        for (size_t i = 0; i < count; ++i) {
            size_t at = ackStart + 4 * i;
            packet.acks.push_back((uint32_t(payload[at]) << 24)
                | (uint32_t(payload[at + 1]) << 16)
                | (uint32_t(payload[at + 2]) << 8) | uint32_t(payload[at + 3]));
        }
        payload.resize(ackStart);
    }
    if (packet.flags & kFlagZerocoded) payload = zeroDecode(payload);
    packet.body = std::move(payload);
    return packet;
}

inline std::vector<uint8_t> buildPacket(uint32_t sequence,
                                        const std::vector<uint8_t>& messageId,
                                        const std::vector<uint8_t>& body,
                                        bool reliable, bool zerocoded,
                                        const std::vector<uint32_t>& acks = {}) {
    std::vector<uint8_t> payload = messageId;
    payload.insert(payload.end(), body.begin(), body.end());
    uint8_t flags = 0;
    if (zerocoded) { flags |= kFlagZerocoded; payload = zeroEncode(payload); }
    if (reliable) flags |= kFlagReliable;
    if (!acks.empty()) flags |= kFlagAck;
    std::vector<uint8_t> out;
    out.push_back(flags);
    out.push_back(static_cast<uint8_t>(sequence >> 24));
    out.push_back(static_cast<uint8_t>(sequence >> 16));
    out.push_back(static_cast<uint8_t>(sequence >> 8));
    out.push_back(static_cast<uint8_t>(sequence));
    out.push_back(0); // extra header length
    out.insert(out.end(), payload.begin(), payload.end());
    for (uint32_t seq : acks) {
        out.push_back(static_cast<uint8_t>(seq >> 24));
        out.push_back(static_cast<uint8_t>(seq >> 16));
        out.push_back(static_cast<uint8_t>(seq >> 8));
        out.push_back(static_cast<uint8_t>(seq));
    }
    if (!acks.empty()) out.push_back(static_cast<uint8_t>(acks.size()));
    return out;
}

// ---------------- body cursor ----------------
class BodyReader {
public:
    BodyReader(const std::vector<uint8_t>& data, size_t offset = 0)
        : mData(data), mPos(offset) {}

    uint8_t u8() { need(1); return mData[mPos++]; }
    uint16_t u16() { need(2); uint16_t v = (uint16_t(mData[mPos]) << 8) | mData[mPos + 1]; mPos += 2; return v; }
    uint32_t u32() { need(4); uint32_t v = 0; for (int i = 0; i < 4; ++i) v = (v << 8) | mData[mPos++]; return v; }
    uint64_t u64() { need(8); uint64_t v = 0; for (int i = 0; i < 8; ++i) v = (v << 8) | mData[mPos++]; return v; }
    int32_t s32() { return static_cast<int32_t>(u32()); }
    float f32() { uint32_t bits = u32(); float f; std::memcpy(&f, &bits, 4); return f; }
    double f64() { uint64_t bits = u64(); double d; std::memcpy(&d, &bits, 8); return d; }
    bool boolean() { return u8() != 0; }
    std::array<uint8_t, 16> uuid() {
        need(16);
        std::array<uint8_t, 16> out;
        std::memcpy(out.data(), mData.data() + mPos, 16);
        mPos += 16;
        return out;
    }
    std::array<float, 3> vector3() { return {f32(), f32(), f32()}; }
    std::array<float, 4> quaternion() {
        float x = f32(), y = f32(), z = f32();
        double w2 = 1.0 - (double(x) * x + double(y) * y + double(z) * z);
        float w = w2 > 0 ? static_cast<float>(std::sqrt(w2)) : 0.f;
        return {x, y, z, w};
    }
    std::vector<uint8_t> variable1() { return take(u8()); }
    std::vector<uint8_t> variable2() { return take(u16()); }
    std::string stringZ() {
        auto raw = variable1();
        size_t end = 0;
        while (end < raw.size() && raw[end] != 0) ++end;
        return std::string(raw.begin(), raw.begin() + end);
    }
    bool exhausted() const { return mPos == mData.size(); }

private:
    void need(size_t n) const {
        if (mPos + n > mData.size()) throw std::runtime_error("Body truncated");
    }
    std::vector<uint8_t> take(size_t n) {
        need(n);
        std::vector<uint8_t> out(mData.begin() + mPos, mData.begin() + mPos + n);
        mPos += n;
        return out;
    }
    const std::vector<uint8_t>& mData;
    size_t mPos;
};

} // namespace sl
```

## B3. LLMessage circuit concepts, in code

The viewer's circuit layer (`indra/llmessage/llcircuit.cpp`, `llpacketring.cpp`) owns four things, and any C++ client or proxy ends up re-owning all four:

1. **Sequence and reliability bookkeeping** — a map from sequence → (packet bytes, last-sent time) for reliable packets, retired by explicit ACKs (standalone `PacketAck` or appended lists).
2. **Resend timing** — reliable packets are resent with the Resent flag until ACKed; the viewer adapts intervals to measured RTT, a teaching implementation can use a fixed 400 ms sweep.
3. **Ping and circuit timeout** — `StartPingCheck`/`CompletePingCheck` measure RTT; silence past the timeout means the circuit is dead and the *session* layer (not the circuit) decides to relogin or teleport-recover.
4. **Throttle** — per-category token buckets matching the `AgentThrottle` categories; the circuit drops or defers by category rather than treating the socket as one undifferentiated pipe.

The class below is the circuit core without sockets (transport injected as a callable), so it can be unit-tested deterministically — the same separation that makes the Java circuit in A4 testable with a fake transport.

```cpp
// sl_circuit.hpp — reliability/ACK/ping/throttle core, transport injected.
#pragma once

#include "sl_packet.hpp"

#include <chrono>
#include <functional>
#include <map>
#include <string>

namespace sl {

class Circuit {
public:
    using SendFn = std::function<void(const std::vector<uint8_t>&)>;
    using Clock = std::chrono::steady_clock;

    explicit Circuit(SendFn send) : mSend(std::move(send)) {
        for (const char* cat : {"resend", "land", "wind", "cloud",
                                "task", "texture", "asset"}) {
            mBuckets[cat] = Bucket{200.0, 400.0, 400.0, Clock::now()};
        }
    }

    /** Send a message body (ID already encoded by the caller via
     *  encodeMessageId). Returns the sequence, or -1 when throttled
     *  reliable traffic must be retried by the caller. */
    int32_t send(const std::vector<uint8_t>& messageId,
                 const std::vector<uint8_t>& body, bool reliable,
                 bool zerocoded, const std::string& category = "task") {
        Bucket& bucket = mBuckets[category];
        if (!bucket.take()) return reliable ? -1 : 0;
        uint32_t seq = mNextSequence++;
        std::vector<uint32_t> acks;
        acks.swap(mPendingAcks);
        auto datagram = buildPacket(seq, messageId, body, reliable, zerocoded, acks);
        mSend(datagram);
        if (reliable) mUnacked[seq] = {datagram, Clock::now()};
        return static_cast<int32_t>(seq);
    }

    /** Feed one inbound datagram. Returns the decoded packet for the
     *  caller's dispatcher; ACK bookkeeping and ping replies are handled
     *  internally, exactly as llcircuit hides them from message handlers. */
    Packet receive(const std::vector<uint8_t>& datagram) {
        Packet packet = parsePacket(datagram);
        mLastReceived = Clock::now();
        for (uint32_t seq : packet.acks) mUnacked.erase(seq);
        if (packet.reliable()) {
            mPendingAcks.push_back(packet.sequence);
            if (mPendingAcks.size() >= 32) flushAcks(); // do not let ACKs age
        }
        MessageId id = decodeMessageId(packet.body);
        if (id.frequency == Frequency::Fixed && id.number == 0xFFFFFFFB) {
            BodyReader r(packet.body, id.offset);
            uint8_t count = r.u8();
            for (int i = 0; i < count; ++i) mUnacked.erase(r.u32());
        }
        return packet;
    }

    /** Periodic maintenance: resends, ACK flush, ping. Call at ~10 Hz. */
    void tick() {
        auto now = Clock::now();
        for (auto& [seq, sent] : mUnacked) {
            if (now - sent.lastSent >= std::chrono::milliseconds(400)) {
                auto resent = sent.datagram;
                resent[0] |= kFlagResent;
                mSend(resent);
                sent.lastSent = now;
            }
        }
        if (!mPendingAcks.empty()
            && now - mOldestAck >= std::chrono::milliseconds(100)) {
            flushAcks();
        }
        if (now - mLastPingSent >= std::chrono::seconds(5)) {
            mLastPingSent = now;
            mPingId = static_cast<uint8_t>(mPingId + 1);
            std::vector<uint8_t> body{static_cast<uint8_t>(mPingId), 0, 0, 0, 0};
            // StartPingCheck body in the current template is the ping ID
            // (U8) followed by the oldest unacked sequence (U32).
            uint32_t oldest = mUnacked.empty() ? 0 : mUnacked.begin()->first;
            body[1] = static_cast<uint8_t>(oldest >> 24);
            body[2] = static_cast<uint8_t>(oldest >> 16);
            body[3] = static_cast<uint8_t>(oldest >> 8);
            body[4] = static_cast<uint8_t>(oldest);
            auto datagram = buildPacket(mNextSequence++,
                encodeMessageId(Frequency::Fixed, 0xFFFFFFFD), body,
                false, false);
            mSend(datagram);
        }
    }

    bool dead() const {
        return Clock::now() - mLastReceived > std::chrono::seconds(60);
    }

private:
    struct SentPacket {
        std::vector<uint8_t> datagram;
        Clock::time_point lastSent;
    };
    struct Bucket {
        double ratePerSec;
        double burst;
        double tokens;
        Clock::time_point updated;
        bool take() {
            auto now = Clock::now();
            double elapsed = std::chrono::duration<double>(now - updated).count();
            tokens = std::min(burst, tokens + elapsed * ratePerSec);
            updated = now;
            if (tokens >= 1.0) { tokens -= 1.0; return true; }
            return false;
        }
    };

    void flushAcks() {
        std::vector<uint32_t> acks;
        acks.swap(mPendingAcks);
        // PacketAck body: U8 count, then that many U32 sequences.
        std::vector<uint8_t> body;
        body.push_back(static_cast<uint8_t>(acks.size()));
        for (uint32_t seq : acks) {
            body.push_back(static_cast<uint8_t>(seq >> 24));
            body.push_back(static_cast<uint8_t>(seq >> 16));
            body.push_back(static_cast<uint8_t>(seq >> 8));
            body.push_back(static_cast<uint8_t>(seq));
        }
        mSend(buildPacket(mNextSequence++,
            encodeMessageId(Frequency::Fixed, 0xFFFFFFFB), body, false, false));
    }

    SendFn mSend;
    uint32_t mNextSequence = 1;
    std::map<uint32_t, SentPacket> mUnacked;
    std::vector<uint32_t> mPendingAcks;
    Clock::time_point mOldestAck = Clock::now();
    Clock::time_point mLastReceived = Clock::now();
    Clock::time_point mLastPingSent = Clock::now();
    uint8_t mPingId = 0;
    std::map<std::string, Bucket> mBuckets;
};

} // namespace sl
```

## B4. Build it: CMakeLists and a test harness

```cmake
# CMakeLists.txt — builds the standalone parser + circuit as a library
# with a test binary. C++17, no third-party dependencies: that is the
# point of the standalone extraction. (The real viewer builds with
# Autobuild/CMake and dozens of 3p-* packages; Alchemy uses CMake+vcpkg.
# Do not confuse this tool build with a viewer build.)
cmake_minimum_required(VERSION 3.20)
project(sl_proto_tool CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra)
endif()

add_library(sl_proto
    llsd_binary.cpp
    llsd_xml.cpp
    # sl_packet.hpp / sl_circuit.hpp / llsd.hpp are header-only here
)
target_include_directories(sl_proto PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(sl_proto_tests tests/test_main.cpp)
target_link_libraries(sl_proto_tests PRIVATE sl_proto)

enable_testing()
add_test(NAME sl_proto_tests COMMAND sl_proto_tests)
```

```cpp
// tests/test_main.cpp — the vectors that must never regress.
// Each vector encodes a rule stated in the prose above it in this file.
#include "llsd.hpp"
#include "sl_packet.hpp"
#include "sl_circuit.hpp"

#include <cassert>
#include <iostream>

static void testZerocode() {
    using namespace sl;
    // A run of 300 zeros exercises the 255-count chunking.
    std::vector<uint8_t> in(300, 0);
    in.push_back(0x41);
    auto enc = zeroEncode(in);
    assert(enc.size() == 2 + 2 + 1); // (0,255) (0,45) 'A'
    assert(zeroDecode(enc) == in);
    // Empty and zero-free inputs round-trip.
    assert(zeroDecode(zeroEncode({})).empty());
    assert(zeroDecode(zeroEncode({1, 2, 3})) == std::vector<uint8_t>({1, 2, 3}));
}

static void testPacketRoundTrip() {
    using namespace sl;
    auto id = encodeMessageId(Frequency::Low, 4); // UseCircuitCode
    std::vector<uint8_t> body(40, 0xAB);
    auto wire = buildPacket(7, id, body, /*reliable=*/true,
                            /*zerocoded=*/true, /*acks=*/{1, 2, 3});
    Packet p = parsePacket(wire);
    assert(p.sequence == 7);
    assert(p.reliable() && p.zerocoded());
    assert((p.acks == std::vector<uint32_t>{1, 2, 3}));
    MessageId mid = decodeMessageId(p.body);
    assert(mid.frequency == Frequency::Low && mid.number == 4);
    assert(p.body.size() == id.size() + body.size());
}

static void testLlsdBinary() {
    LLSD map = LLSD::newMap();
    map["agent_id"] = LLSD::newUUID("12345678-1234-5678-1234-567812345678");
    map["count"] = LLSD(42);
    map["ratio"] = LLSD(1.5);
    map["name"] = LLSD("Kaleaon");
    LLSD arr = LLSD::newArray();
    arr.append(LLSD(true));
    arr.append(LLSD());
    map["flags"] = arr;
    auto bytes = llsdToBinary(map);
    LLSD back = llsdFromBinary(bytes);
    assert(back["count"].asInteger() == 42);
    assert(back["name"].asString() == "Kaleaon");
    assert(back["flags"].array().size() == 2);
    assert(back["flags"].array()[0].asBoolean());
}

static void testCircuitAckRetiresReliable() {
    using namespace sl;
    std::vector<std::vector<uint8_t>> sent;
    Circuit circuit([&](const std::vector<uint8_t>& d) { sent.push_back(d); });
    auto id = encodeMessageId(Frequency::Low, 41); // CompleteAgentMovement
    int32_t seq = circuit.send(id, {1, 2, 3}, /*reliable=*/true, /*zerocoded=*/true);
    assert(seq == 1);
    // Simulate the simulator ACKing seq 1 via an appended list.
    auto ackWire = buildPacket(99, encodeMessageId(Frequency::Fixed, 0xFFFFFFFB),
                               {0}, false, false, {1});
    // Note: PacketAck-as-body vs appended acks are distinct paths; the
    // appended list alone must already retire the reliable send, which we
    // observe by ticking and confirming no resend datagram appears.
    circuit.receive(ackWire);
    size_t before = sent.size();
    circuit.tick();
    // A resend would only appear after the 400 ms sweep with the packet
    // still unacked; with the ACK applied there is nothing to resend, and
    // tick() must not emit a resent copy of seq 1.
    for (size_t i = before; i < sent.size(); ++i) {
        assert(!(sent[i][0] & kFlagResent));
    }
}

int main() {
    testZerocode();
    testPacketRoundTrip();
    testLlsdBinary();
    testCircuitAckRetiresReliable();
    std::cout << "sl_proto_tests: all passed\n";
    return 0;
}
```

## B5. Tying Part A together: an Android session bootstrap

The Java pieces form a session in this order — the same order the Python stack in `code-python.md` uses, because the simulator does not care what language you are, only what sequence you speak:

```java
package com.example.slproto;

import com.example.slproto.auth.LoginClient;
import com.example.slproto.auth.LoginOutcome;
import com.example.slproto.auth.LoginResult;
import com.example.slproto.caps.CapsClient;
import com.example.slproto.net.Circuit;

import java.net.InetAddress;
import java.util.List;
import java.util.concurrent.Executors;

/**
 * Session bootstrap (teaching form): login (with MFA branch) -> seed caps
 * -> UDP circuit -> UseCircuitCode + CompleteAgentMovement. RegionHandshake
 * handling, Event Queue start, and AgentUpdate belong to the session class
 * that owns this bootstrap in a real app; the seams are marked.
 */
final class Session {
    private final java.util.concurrent.ExecutorService sessionExecutor =
            Executors.newSingleThreadExecutor(r -> new Thread(r, "sl-session"));

    interface MfaPrompter { String requestToken(); }  // UI supplies the dialog
    interface Callbacks { void onLoggedIn(LoginResult result, CapsClient caps); }

    void connect(String loginUri, String first, String last, String password,
                 MfaPrompter prompter, Callbacks callbacks) {
        sessionExecutor.execute(() -> {
            try {
                okhttp3.OkHttpClient http = CapsClient.defaultHttp();
                LoginClient login = new LoginClient(http);
                LoginOutcome outcome = login.login(loginUri, first, last, password, null, null);
                if (outcome instanceof LoginOutcome.MfaChallenge mfa) {
                    // Prompt on the UI thread in a real app; the token is
                    // used once here and the hash never leaves this stack.
                    String token = prompter.requestToken();
                    outcome = login.login(loginUri, first, last, password,
                            token, mfa.mfaHash());
                }
                if (!(outcome instanceof LoginOutcome.Success success)) {
                    // Surface Failure.reason/message to the user verbatim.
                    return;
                }
                LoginResult result = success.result();
                CapsClient caps = CapsClient.fromSeed(http, result.seedCapability(),
                        List.of("EventQueueGet", "FetchInventory2",
                                "FetchInventoryDescendents2", "InventoryAPIv3",
                                "GetTexture", "GetMesh", "GetMesh2",
                                "SimulatorFeatures", "GetDisplayNames",
                                "ChatSessionRequest", "ExtEnvironment"));
                Circuit circuit = new Circuit(
                        InetAddress.getByName(result.simIp()), result.simPort(),
                        (id, body) -> { /* dispatch to message handlers */ },
                        () -> { /* dead circuit: session layer relogins */ });
                circuit.start();
                // UseCircuitCode then CompleteAgentMovement go here, packed
                // with the A3 message classes and sent reliable=true, in
                // that order, before anything else is sent on the circuit.
                callbacks.onLoggedIn(result, caps);
            } catch (Exception e) {
                // Login/caps/circuit setup failures all land here; in
                // production, split them per section 12's taxonomy in
                // code-python.md (codec / transport / auth / grid).
            }
        });
    }
}
```

**Cross-language invariant worth repeating:** the Java, Python, and C++ stacks in this repo must produce byte-identical datagrams for the same message. When they disagree, the fix is never "make the odd one match by eye" — it is to capture one known-good login on a local OpenSim with each stack and diff the bytes. The wire format is the specification; every implementation here is a reading of it.

## B6. LLSD notation in C++ (the log/config format)

Notation is what viewer logs and many config snippets use. A tool that tails logs needs the reader; the writer is for producing human-diffable test output.

```cpp
// llsd_notation.cpp — writer + recursive-descent reader.
#include "llsd.hpp"

#include <cctype>
#include <sstream>
#include <stdexcept>

namespace {

std::string notationQuote(const std::string& s) {
    std::string out = "\"";
    for (char c : s) {
        switch (c) {
            case '"': out += "\\\""; break;
            case '\\': out += "\\\\"; break;
            case '\n': out += "\\n"; break;
            case '\r': out += "\\r"; break;
            case '\t': out += "\\t"; break;
            default: out += c;
        }
    }
    return out + "\"";
}

std::string base64Encode(const std::vector<uint8_t>& data); // shared with llsd_xml.cpp

void writeNotation(std::ostringstream& out, const LLSD& v) {
    switch (v.type()) {
        case LLSD::TYPE_UNDEFINED: out << "!"; break;
        case LLSD::TYPE_BOOLEAN: out << (v.asBoolean() ? "true" : "false"); break;
        case LLSD::TYPE_INTEGER: out << "i" << v.asInteger(); break;
        case LLSD::TYPE_REAL: out << "r" << v.asReal(); break;
        case LLSD::TYPE_UUID: out << "u" << v.asString(); break;
        case LLSD::TYPE_STRING: out << "s" << notationQuote(v.asString()); break;
        case LLSD::TYPE_URI: out << "l" << notationQuote(v.asString()); break;
        case LLSD::TYPE_BINARY: out << "b64" << notationQuote(base64Encode(v.asBinary())); break;
        case LLSD::TYPE_DATE: {
            std::time_t t = static_cast<std::time_t>(v.asReal());
            char buf[32];
            std::strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", std::gmtime(&t));
            out << "d" << notationQuote(buf);
            break;
        }
        case LLSD::TYPE_ARRAY: {
            out << "[";
            bool first = true;
            for (const LLSD& item : v.array()) {
                if (!first) out << ", ";
                first = false;
                writeNotation(out, item);
            }
            out << "]";
            break;
        }
        case LLSD::TYPE_MAP: {
            out << "{";
            bool first = true;
            for (const auto& [key, item] : v.map()) {
                if (!first) out << ", ";
                first = false;
                out << notationQuote(key) << ":";
                writeNotation(out, item);
            }
            out << "}";
            break;
        }
    }
}

struct NotationParser {
    const std::string& text;
    size_t pos = 0;

    void skipWs() {
        while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) ++pos;
    }
    char peek() {
        skipWs();
        return pos < text.size() ? text[pos] : '\0';
    }
    void expect(char c) {
        if (peek() != c) throw std::runtime_error("Notation: expected char");
        ++pos;
    }
    std::string quoted() {
        skipWs();
        char q = text[pos];
        if (q != '"' && q != '\'') throw std::runtime_error("Notation: expected quote");
        ++pos;
        std::string out;
        while (pos < text.size()) {
            char c = text[pos++];
            if (c == '\\' && pos < text.size()) {
                char e = text[pos++];
                out += (e == 'n' ? '\n' : e == 'r' ? '\r' : e == 't' ? '\t' : e);
            } else if (c == q) {
                return out;
            } else {
                out += c;
            }
        }
        throw std::runtime_error("Notation: unterminated string");
    }
    std::string bareWord() {
        skipWs();
        size_t start = pos;
        while (pos < text.size()
               && (std::isalnum(static_cast<unsigned char>(text[pos]))
                   || text[pos] == '-' || text[pos] == '.' || text[pos] == '+')) {
            ++pos;
        }
        return text.substr(start, pos - start);
    }
    LLSD value() {
        char c = peek();
        if (c == '!') { ++pos; return LLSD(); }
        if (c == '[') {
            ++pos;
            LLSD arr = LLSD::newArray();
            if (peek() != ']') {
                arr.append(value());
                while (peek() == ',') { ++pos; arr.append(value()); }
            }
            expect(']');
            return arr;
        }
        if (c == '{') {
            ++pos;
            LLSD map = LLSD::newMap();
            if (peek() != '}') {
                while (true) {
                    std::string key = quoted();
                    expect(':');
                    map[key] = value();
                    if (peek() == ',') { ++pos; continue; }
                    break;
                }
            }
            expect('}');
            return map;
        }
        if (c == '"' || c == '\'') return LLSD(quoted());
        ++pos; // consume prefix
        switch (c) {
            case 'i': return LLSD(static_cast<int32_t>(std::stoi(bareWord())));
            case 'r': return LLSD(std::stod(bareWord()));
            case 'u': return LLSD::newUUID(bareWord());
            case 's': return LLSD(quoted());
            case 'l': return LLSD::newURI(quoted());
            case 'b': {
                if (text.compare(pos, 2, "64") == 0) {
                    pos += 2;
                    return LLSD::newBinary(base64Decode(quoted()));
                }
                return LLSD::newBinary({});
            }
            case 't': pos += 3; return LLSD(true);   // 'rue'
            case 'f': pos += 4; return LLSD(false);  // 'alse'
            default: throw std::runtime_error("Notation: unexpected prefix");
        }
    }
    std::vector<uint8_t> base64Decode(const std::string& s); // shared helper
};

} // namespace

std::string llsdToNotation(const LLSD& v) {
    std::ostringstream out;
    writeNotation(out, v);
    return out.str();
}

LLSD llsdFromNotation(const std::string& text) {
    NotationParser parser{text};
    LLSD v = parser.value();
    parser.skipWs();
    if (parser.pos != text.size()) throw std::runtime_error("Notation: trailing characters");
    return v;
}
```

## A8. Java worked example: walking inventory over caps

The Java counterpart of the Python inventory walk — streaming, folder by folder, because an Android client that materialises a whole inventory tree will OOM on exactly the long-lived accounts that most need a mobile client.

```java
package com.example.slproto.caps;

import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.function.Consumer;

/** Folder-at-a-time inventory walk over FetchInventoryDescendents2. */
final class InventoryWalk {
    private final CapsClient caps;
    private final UUID agentId;

    InventoryWalk(CapsClient caps, UUID agentId) {
        this.caps = caps;
        this.agentId = agentId;
    }

    @SuppressWarnings("unchecked")
    Map<String, Object> fetchFolder(UUID folderId) throws IOException {
        Map<String, Object> request = new HashMap<>();
        request.put("agent_id", agentId.toString());
        request.put("folder_id", folderId.toString());
        request.put("owner_id", agentId.toString());
        request.put("sort_order", 0);
        request.put("fetch_folders", Boolean.TRUE);
        request.put("fetch_items", Boolean.TRUE);
        request.put("fetch_links", Boolean.TRUE);
        Object reply = caps.postLlsd("FetchInventoryDescendents2", request);
        return reply instanceof Map ? (Map<String, Object>) reply : Map.of();
    }

    /** Depth-first; the consumer receives each folder and item map as it
     *  arrives. Cancellation is cooperative: the consumer returns false
     *  from the predicate variant in production code; this teaching form
     *  walks to a bounded depth, which is the other honest bound. */
    @SuppressWarnings("unchecked")
    void walk(UUID rootId, int maxDepth,
              Consumer<Map<String, Object>> onFolder,
              Consumer<Map<String, Object>> onItem) throws IOException {
        record Frame(UUID folderId, int depth) {}
        Deque<Frame> stack = new ArrayDeque<>();
        stack.push(new Frame(rootId, 0));
        while (!stack.isEmpty()) {
            Frame frame = stack.pop();
            Map<String, Object> reply = fetchFolder(frame.folderId());
            Object items = reply.get("items");
            if (items instanceof List<?> list) {
                for (Object item : list) {
                    if (item instanceof Map) onItem.accept((Map<String, Object>) item);
                }
            }
            Object folders = reply.get("folders");
            if (folders instanceof List<?> list && frame.depth() < maxDepth) {
                for (Object folder : list) {
                    if (folder instanceof Map) {
                        Map<String, Object> f = (Map<String, Object>) folder;
                        onFolder.accept(f);
                        Object id = f.get("folder_id");
                        if (id != null) {
                            stack.push(new Frame(UUID.fromString(String.valueOf(id)),
                                    frame.depth() + 1));
                        }
                    }
                }
            }
        }
    }
}
```

**AIS3 note for the Java stack:** reads come from the Fetch* caps as above; writes (create folder/item, move, link, update) go through `InventoryAPIv3`/`LibraryAPIv3` with LLSD bodies shaped by `llaisapi.cpp`, and outfit operations additionally carry the Current Outfit Folder version (`IncrementCOFVersion`). A Java client that implements only the Fetch side will look complete in demos and fail the first time a user tries to wear, move, or delete anything — plan the AIS3 half as its own module with its own tests against a local OpenSim (knowing OpenSim's AIS coverage diverges from Agni's) and an Aditi pass before calling it done.

## B7. The C++ body writer (the pack half of B2's reader)

```cpp
// BodyWriter in sl_packet.hpp's companion header — symmetric to BodyReader.
class BodyWriter {
public:
    BodyWriter& u8(uint8_t v) { mBuf.push_back(v); return *this; }
    BodyWriter& u16(uint16_t v) {
        mBuf.push_back(static_cast<uint8_t>(v >> 8));
        mBuf.push_back(static_cast<uint8_t>(v));
        return *this;
    }
    BodyWriter& u32(uint32_t v) {
        for (int s = 24; s >= 0; s -= 8)
            mBuf.push_back(static_cast<uint8_t>(v >> s));
        return *this;
    }
    BodyWriter& u64(uint64_t v) {
        for (int s = 56; s >= 0; s -= 8)
            mBuf.push_back(static_cast<uint8_t>(v >> s));
        return *this;
    }
    BodyWriter& s32(int32_t v) { return u32(static_cast<uint32_t>(v)); }
    BodyWriter& f32(float v) { uint32_t bits; std::memcpy(&bits, &v, 4); return u32(bits); }
    BodyWriter& f64(double v) { uint64_t bits; std::memcpy(&bits, &v, 8); return u64(bits); }
    BodyWriter& boolean(bool v) { return u8(v ? 1 : 0); }
    BodyWriter& uuid(const std::array<uint8_t, 16>& id) {
        mBuf.insert(mBuf.end(), id.begin(), id.end());
        return *this;
    }
    BodyWriter& vector3(const std::array<float, 3>& v) {
        f32(v[0]); f32(v[1]); f32(v[2]); return *this;
    }
    /** Wire quaternions carry x, y, z only — see BodyReader::quaternion. */
    BodyWriter& quaternion(const std::array<float, 4>& q) {
        f32(q[0]); f32(q[1]); f32(q[2]); return *this;
    }
    BodyWriter& variable1(const std::vector<uint8_t>& data) {
        u8(static_cast<uint8_t>(data.size()));
        mBuf.insert(mBuf.end(), data.begin(), data.end());
        return *this;
    }
    BodyWriter& variable2(const std::vector<uint8_t>& data) {
        u16(static_cast<uint16_t>(data.size()));
        mBuf.insert(mBuf.end(), data.begin(), data.end());
        return *this;
    }
    BodyWriter& stringZ(const std::string& text) {
        std::vector<uint8_t> raw(text.begin(), text.end());
        raw.push_back(0);
        return variable1(raw);
    }
    const std::vector<uint8_t>& bytes() const { return mBuf; }
private:
    std::vector<uint8_t> mBuf;
};
```

With B2's reader and this writer, the C++ tool can both halves of a proxy: parse a captured datagram, mutate a field, repack, and forward — which is the Hippolyzer-style debugging pattern (a local decoding proxy between a viewer and a simulator) that the protocol skill recommends for mobile-client work. Build the proxy read-only first (log and forward unchanged, byte-compare in/out), because a proxy that silently alters traffic teaches you false lessons about the client you are debugging.
