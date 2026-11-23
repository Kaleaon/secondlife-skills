# Kotlin / Android for a Native Second Life Client

> **What this file ports, and from where.** This is a complete, working
> Kotlin implementation of the Second Life client protocol core for
> Android — the native counterpart to the React/TypeScript file in this
> folder, and a modernisation path for the Java code recovered in
> `Kaleaon/Lumiya-Redux` (Apache-2.0 recovery of Lumiya 3.4.2: 1,302
> Java classes, 477 UDP message classes, OkHttp caps, XML-RPC-era login
> since extended with LLSD + MFA).
>
> Canonical sources, per section:
>
> - LLSD model and serialisations — `indra/llcommon/llsdserialize.cpp`
>   in `secondlife/viewer`, cross-checked against
>   `LibreMetaverse.StructuredData` (C#) and the Java LLSD code inside
>   Lumiya-Redux.
> - Packet format, flags, frequency encoding, ZeroCode, reliability —
>   `message_template.msg` (`secondlife/master-message-template`,
>   diffed against the viewer copy) and `LibreMetaverse.Transport`.
> - Message block/field layouts — the template itself; the core message
>   set in §5 is written in the same generated style a template code
>   generator emits (the production Lumiya tree generates its 477
>   classes this way; never hand-edit generated output).
> - Caps — `llviewerregion.cpp` `buildCapabilityNames` and
>   `llaisapi.cpp` (AIS3) in `secondlife/viewer`.
> - Login + MFA — `llstartup.cpp`, LibreMetaverse `Login`, and the
>   MFA pattern from the Lumiya repair work: parse `reason`/`mfa_hash`
>   from the failed-login reply, prompt, resubmit with token + hash,
>   keep the hash in memory only (no encrypted store ⇒ no persistence).
>
> **Stack.** Kotlin coroutines + Flow for all I/O, `DatagramSocket` on
> `Dispatchers.IO` for the UDP circuit (NIO `DatagramChannel` variant
> in §6.4), OkHttp for caps/login (Ktor variant notes in §7.3),
> Jetpack Compose for UI, `ViewModel` + lifecycle for the circuit.
>
> **Licence note.** Protocol facts are interoperability data; this code
> is original Kotlin for this repo. Port semantics from LGPL viewer
> code, do not transliterate it.

---

## 0. Build setup

```kotlin
// build.gradle.kts (app module, excerpts)
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

android {
    namespace = "app.linkpoint"
    compileSdk = 34

    defaultConfig {
        applicationId = "app.linkpoint"
        minSdk = 26          // Lumiya-Redux floor; DatagramChannel + NIO.2 paths assume 26+
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
    }
    buildFeatures { compose = true }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1")
    implementation("com.squareup.okhttp3:okhttp:4.12.0")     // Lumiya modernisation line: 3.14 -> 4.12
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.8.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.8.0")
    implementation(platform("androidx.compose:compose-bom:2024.10.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.activity:activity-compose:1.9.0")
    testImplementation("junit:junit:4.13.2")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.8.1")
}
```

```xml
<!-- AndroidManifest.xml (excerpts): the three declarations a viewer needs -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<!-- Voice later: RECORD_AUDIO. Foreground service (see §10.3):
     FOREGROUND_SERVICE + a service entry with foregroundServiceType="connectedDevice|dataSync" per current Play policy. -->
<application android:usesCleartextTraffic="false">
    <!-- Cleartext stays OFF: login, caps, and grid services are HTTPS.
         Local OpenSim testing uses a networkSecurityConfig exception
         scoped to 10.0.2.2 / 192.168.0.0/16 in the debug source set ONLY. -->
</application>
```

---

## 1. Core types

```kotlin
// app/src/main/java/app/linkpoint/sl/Types.kt
// UUID / Vector3 / Quaternion with the wire conventions of the protocol.
// Ported from LibreMetaverse.Types and indra/llmath.

package app.linkpoint.sl

import java.nio.ByteBuffer
import java.util.UUID

/** The all-zeros UUID ("null key") — template default and "none" sentinel. */
val NULL_KEY: UUID = UUID(0L, 0L)

fun UUID.toBytes(): ByteArray {
    val buf = ByteBuffer.allocate(16)
    buf.putLong(this.mostSignificantBits)
    buf.putLong(this.leastSignificantBits)
    return buf.array()
}

fun ByteArray.uuidAt(offset: Int): UUID {
    require(offset + 16 <= size) { "UUID read past end of buffer" }
    val buf = ByteBuffer.wrap(this, offset, 16)
    return UUID(buf.long, buf.long)
}

fun String.toUUIDOrNull(): UUID? = try {
    // The simulator is strict about canonical form; UUID.fromString is
    // lenient about some malformed inputs, so round-trip check.
    val u = UUID.fromString(this.trim().lowercase())
    if (u.toString() == this.trim().lowercase()) u else null
} catch (e: IllegalArgumentException) {
    null
}

/** Second Life vector: x east, y north, z up. f32 on the wire. */
data class Vector3(val x: Float, val y: Float, val z: Float) {
    operator fun plus(o: Vector3) = Vector3(x + o.x, y + o.y, z + o.z)
    operator fun minus(o: Vector3) = Vector3(x - o.x, y - o.y, z - o.z)
    operator fun times(s: Float) = Vector3(x * s, y * s, z * s)
    fun length(): Float = kotlin.math.sqrt(x * x + y * y + z * z)
    companion object {
        val ZERO = Vector3(0f, 0f, 0f)
    }
}

/** f64 variant used for global positions (region corners, teleports). */
data class Vector3d(val x: Double, val y: Double, val z: Double)

/**
 * Quaternion. On the wire an LLQuaternion is 3 x f32 (x, y, z); w is
 * reconstructed as sqrt(1 - x² - y² - z²). See PacketIO.readQuaternion.
 */
data class Quaternion(val x: Float, val y: Float, val z: Float, val w: Float) {
    companion object {
        val IDENTITY = Quaternion(0f, 0f, 0f, 1f)
        fun fromWire(x: Float, y: Float, z: Float): Quaternion {
            val w2 = 1f - x * x - y * y - z * z
            return Quaternion(x, y, z, if (w2 > 0f) kotlin.math.sqrt(w2) else 0f)
        }
    }
}
```

---

## 2. LLSD in Kotlin: sealed model + XML and binary codecs

LLSD is the data model for login, caps, the event queue, and inventory:
undefined, boolean, i32 integer, f64 real, string, binary, UUID, date,
URI, array, map. The sealed class below keeps integer and real distinct
(the #1 LLSD interop bug is collapsing `1` and `1.0`), and keeps UUID
distinct from string (AIS3 rejects UUID fields echoed back as strings).

```kotlin
// app/src/main/java/app/linkpoint/sl/llsd/LLSD.kt
// Ported from llsdserialize.cpp semantics + LibreMetaverse.StructuredData.

package app.linkpoint.sl.llsd

import java.time.Instant
import java.util.UUID

sealed class LLSD {
    object Undef : LLSD()
    data class Bool(val value: Boolean) : LLSD()
    data class Int(val value: Int) : LLSD()          // signed 32-bit, always
    data class Real(val value: Double) : LLSD()      // f64, always
    data class Str(val value: String) : LLSD()
    data class Uuid(val value: UUID) : LLSD()
    data class Binary(val data: ByteArray) : LLSD() {
        // ByteArray in a data class: equals/hashCode must be content-based.
        override fun equals(other: Any?): Boolean =
            other is Binary && data.contentEquals(other.data)
        override fun hashCode(): Int = data.contentHashCode()
    }
    data class Date(val value: Instant) : LLSD()
    data class Uri(val value: String) : LLSD()
    data class Arr(val items: List<LLSD>) : LLSD()
    data class Map(val entries: kotlin.collections.Map<String, LLSD>) : LLSD()

    // -- Typed accessors. Caps payloads are untyped; never cast blindly. --
    fun asMap(): kotlin.collections.Map<String, LLSD> =
        (this as? Map)?.entries ?: throw LLSDException("expected map, got $this")
    fun asArr(): List<LLSD> =
        (this as? Arr)?.items ?: throw LLSDException("expected array, got $this")
    fun asStr(default: String = ""): String = (this as? Str)?.value ?: default
    fun asInt(default: Int = 0): Int = when (this) {
        is Int -> value
        is Real -> value.toInt()
        else -> default
    }
    fun asBool(default: Boolean = false): Boolean = (this as? Bool)?.value ?: default
    fun asUuid(): UUID =
        (this as? Uuid)?.value ?: throw LLSDException("expected uuid, got $this")
}

class LLSDException(message: String) : Exception(message)

// Ergonomic builders for request payloads.
fun llsdMapOf(vararg pairs: Pair<String, LLSD>): LLSD.Map = LLSD.Map(mapOf(*pairs))
fun llsdArrOf(vararg items: LLSD): LLSD.Arr = LLSD.Arr(items.toList())
fun String.llsd(): LLSD = LLSD.Str(this)
fun Int.llsd(): LLSD = LLSD.Int(this)
fun Boolean.llsd(): LLSD = LLSD.Bool(this)
fun UUID.llsd(): LLSD = LLSD.Uuid(this)
```

### 2.1 XML codec (the caps format, `application/llsd+xml`)

```kotlin
// app/src/main/java/app/linkpoint/sl/llsd/LLSDXml.kt
// Writer is string-built (LLSD XML is a tiny, regular grammar).
// Reader uses XmlPullParser — available on Android with no extra dep,
// streaming, and safe against the huge FetchInventory replies that
// would blow up a DOM parse on a phone.

package app.linkpoint.sl.llsd

import android.util.Base64
import org.xmlpull.v1.XmlPullParser
import org.xmlpull.v1.XmlPullParserFactory
import java.io.StringReader
import java.time.Instant
import java.util.UUID

object LLSDXml {
    fun write(value: LLSD): String = buildString {
        append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<llsd>")
        writeValue(value)
        append("</llsd>")
    }

    private fun StringBuilder.writeValue(v: LLSD) {
        when (v) {
            is LLSD.Undef -> append("<undef/>")
            is LLSD.Bool -> append("<boolean>").append(if (v.value) 1 else 0).append("</boolean>")
            is LLSD.Int -> append("<integer>").append(v.value).append("</integer>")
            is LLSD.Real -> {
                // Always emit a decimal point: a strict parser reads a
                // bare "1" back as an integer. The viewer writer does this too.
                val s = if (v.value == v.value.toLong().toDouble()) "${v.value.toLong()}.0" else v.value.toString()
                append("<real>").append(s).append("</real>")
            }
            is LLSD.Str -> append("<string>").append(escape(v.value)).append("</string>")
            is LLSD.Uuid -> append("<uuid>").append(v.value).append("</uuid>")
            is LLSD.Binary -> append("<binary>")
                .append(Base64.encodeToString(v.data, Base64.NO_WRAP)).append("</binary>")
            is LLSD.Date -> append("<date>").append(v.value.toString()).append("</date>")
            is LLSD.Uri -> append("<uri>").append(escape(v.value)).append("</uri>")
            is LLSD.Arr -> {
                append("<array>")
                v.items.forEach { writeValue(it) }
                append("</array>")
            }
            is LLSD.Map -> {
                append("<map>")
                for ((k, value) in v.entries) {
                    append("<key>").append(escape(k)).append("</key>")
                    writeValue(value)
                }
                append("</map>")
            }
        }
    }

    private fun escape(s: String): String = buildString(s.length) {
        for (c in s) when (c) {
            '&' -> append("&amp;")
            '<' -> append("&lt;")
            '>' -> append("&gt;")
            '"' -> append("&quot;")
            else -> append(c)
        }
    }

    fun parse(xml: String): LLSD {
        val factory = XmlPullParserFactory.newInstance()
        val parser = factory.newPullParser()
        parser.setInput(StringReader(xml))
        // Advance to the <llsd> root.
        var event = parser.eventType
        while (event != XmlPullParser.END_DOCUMENT) {
            if (event == XmlPullParser.START_TAG && parser.name == "llsd") {
                parser.nextTag()
                return readValue(parser)
            }
            event = parser.next()
        }
        throw LLSDException("no <llsd> root element")
    }

    private fun readValue(p: XmlPullParser): LLSD {
        val name = p.name ?: throw LLSDException("expected element at ${p.positionDescription}")
        return when (name) {
            "undef" -> { consumeEmpty(p); LLSD.Undef }
            "boolean" -> LLSD.Bool(readText(p) in listOf("1", "true"))
            "integer" -> LLSD.Int(readText(p).trim().toInt())
            "real" -> LLSD.Real(readText(p).trim().toDouble())
            "string" -> LLSD.Str(readText(p))
            "uuid" -> LLSD.Uuid(UUID.fromString(readText(p).trim()))
            "binary" -> LLSD.Binary(Base64.decode(readText(p).filterNot { it.isWhitespace() }, Base64.DEFAULT))
            "date" -> LLSD.Date(Instant.parse(readText(p).trim()))
            "uri" -> LLSD.Uri(readText(p))
            "array" -> {
                val items = mutableListOf<LLSD>()
                while (true) {
                    val ev = p.nextTag()
                    if (ev == XmlPullParser.END_TAG && p.name == "array") break
                    items += readValue(p)
                }
                LLSD.Arr(items)
            }
            "map" -> {
                val map = LinkedHashMap<String, LLSD>()
                while (true) {
                    val ev = p.nextTag()
                    if (ev == XmlPullParser.END_TAG && p.name == "map") break
                    if (p.name != "key") throw LLSDException("expected <key> in map, got <${p.name}>")
                    val key = readText(p)
                    p.nextTag()
                    map[key] = readValue(p)
                }
                LLSD.Map(map)
            }
            else -> throw LLSDException("unknown LLSD element <$name>")
        }
    }

    /** Read the text of a scalar element and consume its end tag. */
    private fun readText(p: XmlPullParser): String {
        var text = ""
        if (p.next() == XmlPullParser.TEXT) {
            text = p.text ?: ""
            p.nextTag()
        }
        return text
    }

    private fun consumeEmpty(p: XmlPullParser) {
        // <undef/> arrives as START_TAG + END_TAG on XmlPullParser.
        if (p.next() != XmlPullParser.END_TAG) {
            // Tolerate <undef></undef> too.
        }
    }
}
```

### 2.2 Binary codec

Binary LLSD prefixes each value with a one-byte marker: `!` undef,
`1`/`0` boolean, `i` integer, `r` real, `s` string, `$` binary, `u`
UUID (16 raw bytes, no length), `d` date (f64 epoch seconds), `l` URI,
`[` array, `{` map. Multi-byte numbers are big-endian — unlike message
bodies, which are little-endian (§4). Confusing the two is a classic
porting bug that still "parses".

```kotlin
// app/src/main/java/app/linkpoint/sl/llsd/LLSD Binary.kt
package app.linkpoint.sl.llsd

import app.linkpoint.sl.toBytes
import app.linkpoint.sl.uuidAt
import java.io.ByteArrayOutputStream
import java.io.DataOutputStream
import java.time.Instant
import java.util.UUID

object LLSDBinary {
    fun write(value: LLSD): ByteArray {
        val baos = ByteArrayOutputStream()
        val out = DataOutputStream(baos) // DataOutputStream is big-endian throughout
        writeValue(out, value)
        out.flush()
        return baos.toByteArray()
    }

    private fun writeValue(out: DataOutputStream, v: LLSD) {
        when (v) {
            is LLSD.Undef -> out.writeByte('!'.code)
            is LLSD.Bool -> out.writeByte((if (v.value) '1' else '0').code)
            is LLSD.Int -> { out.writeByte('i'.code); out.writeInt(v.value) }
            is LLSD.Real -> { out.writeByte('r'.code); out.writeDouble(v.value) }
            is LLSD.Str -> { out.writeByte('s'.code); writeStringBody(out, v.value) }
            is LLSD.Uuid -> { out.writeByte('u'.code); out.write(v.value.toBytes()) }
            is LLSD.Binary -> {
                out.writeByte('$'.code); out.writeInt(v.data.size); out.write(v.data)
            }
            is LLSD.Date -> { out.writeByte('d'.code); out.writeDouble(v.value.epochSecond.toDouble()) }
            is LLSD.Uri -> { out.writeByte('l'.code); writeStringBody(out, v.value) }
            is LLSD.Arr -> {
                out.writeByte('['.code); out.writeInt(v.items.size)
                v.items.forEach { writeValue(out, it) }
                out.writeByte(']'.code)
            }
            is LLSD.Map -> {
                out.writeByte('{'.code); out.writeInt(v.entries.size)
                for ((k, value) in v.entries) {
                    out.writeByte('s'.code); writeStringBody(out, k)
                    writeValue(out, value)
                }
                out.writeByte('}'.code)
            }
        }
    }

    private fun writeStringBody(out: DataOutputStream, s: String) {
        val bytes = s.toByteArray(Charsets.UTF_8)
        out.writeInt(bytes.size)
        out.write(bytes)
    }

    fun parse(data: ByteArray): LLSD {
        val reader = Reader(data)
        val v = reader.readValue()
        return v
    }

    private class Reader(private val buf: ByteArray) {
        var pos = 0
        private fun byte(): Int = buf[pos++].toInt() and 0xFF
        private fun marker(): Char = byte().toChar()
        private fun u32(): Int {
            var n = 0
            repeat(4) { n = (n shl 8) or byte() }
            return n
        }
        private fun f64(): Double {
            var bits = 0L
            repeat(8) { bits = (bits shl 8) or byte().toLong() }
            return Double.fromBits(bits)
        }
        private fun take(n: Int): ByteArray {
            val out = buf.copyOfRange(pos, pos + n); pos += n; return out
        }
        private fun stringBody(): String {
            val len = u32()
            return String(take(len), Charsets.UTF_8)
        }

        fun readValue(): LLSD = when (val m = marker()) {
            '!' -> LLSD.Undef
            '1' -> LLSD.Bool(true)
            '0' -> LLSD.Bool(false)
            'i' -> LLSD.Int(u32())
            'r' -> LLSD.Real(f64())
            's' -> LLSD.Str(stringBody())
            '$' -> LLSD.Binary(take(u32()))
            'u' -> LLSD.Uuid(buf.uuidAt(pos).also { pos += 16 })
            'd' -> LLSD.Date(Instant.ofEpochMilli((f64() * 1000).toLong()))
            'l' -> LLSD.Uri(stringBody())
            '[' -> {
                val count = u32()
                val items = List(count) { readValue() }
                check(marker() == ']') { "binary LLSD: array missing ]" }
                LLSD.Arr(items)
            }
            '{' -> {
                val count = u32()
                val map = LinkedHashMap<String, LLSD>()
                repeat(count) {
                    check(marker() == 's') { "binary LLSD: map key must be string" }
                    map[stringBody()] = readValue()
                }
                check(marker() == '}') { "binary LLSD: map missing }" }
                LLSD.Map(map)
            }
            else -> throw LLSDException("binary LLSD: unknown marker '$m' at ${pos - 1}")
        }
    }
}
```

### 2.3 Notation (log/debug rendering)

```kotlin
// app/src/main/java/app/linkpoint/sl/llsd/LLSDNotation.kt
package app.linkpoint.sl.llsd

/** Render an LLSD value in notation form for logs: {'count':i42,'id':u…}.
 *  Read-only — notation is a debugging format, not a wire format to send. */
fun LLSD.toNotation(): String = when (this) {
    is LLSD.Undef -> "!"
    is LLSD.Bool -> if (value) "1" else "0"
    is LLSD.Int -> "i$value"
    is LLSD.Real -> "r$value"
    is LLSD.Str -> "'${value.replace("'", "\\'")}'"
    is LLSD.Uuid -> "u$value"
    is LLSD.Binary -> "b${data.size}\"<${data.size} bytes>\""
    is LLSD.Date -> "d\"$value\""
    is LLSD.Uri -> "l\"$value\""
    is LLSD.Arr -> items.joinToString(",", "[", "]") { it.toNotation() }
    is LLSD.Map -> entries.entries.joinToString(",", "{", "}") {
        "'${it.key}':${it.value.toNotation()}"
    }
}
```

---

## 3. Packet framing and ZeroCode

A simulator datagram is: 1-byte flags, u32 **big-endian** sequence,
1-byte extra-header length, body (message ID + blocks), and — when the
Ack flag is set — a trailing ACK block (count byte + count × u32 BE).
Flags: `0x80` Zerocoded, `0x40` Reliable, `0x20` Resent, `0x10` Ack.
Message IDs encode by frequency: High 1 byte, Medium 2 (`0xFF` + id),
Low 4 (`0xFF 0xFF` + u16), Fixed 4 (`0xFF 0xFF 0xFF` + id byte of the
0xFFFFFFxx value). ZeroCode applies only to the body of Zerocoded
messages, never to the header and never to the appended ACK block.

```kotlin
// app/src/main/java/app/linkpoint/sl/Packet.kt
package app.linkpoint.sl

import java.nio.ByteBuffer
import java.nio.ByteOrder

object PacketFlags {
    const val ZEROCODED = 0x80
    const val RELIABLE = 0x40
    const val RESENT = 0x20
    const val ACK = 0x10
}

enum class Frequency { HIGH, MEDIUM, LOW, FIXED }

object MessageIdCodec {
    fun encode(freq: Frequency, id: Int): ByteArray = when (freq) {
        Frequency.HIGH -> {
            require(id in 1..0xFE) { "high-frequency id out of range: $id" }
            byteArrayOf(id.toByte())
        }
        Frequency.MEDIUM -> {
            require(id in 1..0xFE) { "medium-frequency id out of range: $id" }
            byteArrayOf(0xFF.toByte(), id.toByte())
        }
        Frequency.LOW -> {
            require(id in 1..0xFFFE) { "low-frequency id out of range: $id" }
            byteArrayOf(0xFF.toByte(), 0xFF.toByte(), (id shr 8).toByte(), id.toByte())
        }
        Frequency.FIXED -> byteArrayOf(
            (id ushr 24).toByte(), (id ushr 16).toByte(),
            (id ushr 8).toByte(), id.toByte(),
        )
    }

    data class Decoded(val id: Int, val freq: Frequency, val bytes: Int)

    fun decode(buf: ByteArray, offset: Int): Decoded {
        val b0 = buf[offset].toInt() and 0xFF
        if (b0 != 0xFF) return Decoded(b0, Frequency.HIGH, 1)
        val b1 = buf[offset + 1].toInt() and 0xFF
        if (b1 != 0xFF) return Decoded(b1, Frequency.MEDIUM, 2)
        val b2 = buf[offset + 2].toInt() and 0xFF
        if (b2 != 0xFF) {
            val id = (b2 shl 8) or (buf[offset + 3].toInt() and 0xFF)
            return Decoded(id, Frequency.LOW, 4)
        }
        val id = (0xFF shl 24) or (0xFF shl 16) or (0xFF shl 8) or
            (buf[offset + 3].toInt() and 0xFF)
        return Decoded(id, Frequency.FIXED, 4)
    }

    fun encodedLength(freq: Frequency): Int = when (freq) {
        Frequency.HIGH -> 1
        Frequency.MEDIUM -> 2
        Frequency.LOW, Frequency.FIXED -> 4
    }
}

object ZeroCode {
    /** Encode: each run of n zero bytes (n ≤ 255) becomes 0x00, n. */
    fun encode(body: ByteArray): ByteArray {
        val out = java.io.ByteArrayOutputStream(body.size)
        var i = 0
        while (i < body.size) {
            if (body[i].toInt() == 0) {
                var run = 0
                while (i < body.size && body[i].toInt() == 0 && run < 255) { run++; i++ }
                out.write(0); out.write(run)
            } else {
                out.write(body[i].toInt()); i++
            }
        }
        return out.toByteArray()
    }

    /** Decode. Throws on a truncated run — a corrupt packet must not
     *  silently decode into a shorter, plausible-looking body. */
    fun decode(data: ByteArray): ByteArray {
        val out = java.io.ByteArrayOutputStream(data.size * 2)
        var i = 0
        while (i < data.size) {
            val b = data[i].toInt() and 0xFF
            if (b == 0) {
                require(i + 1 < data.size) { "zerocode: truncated zero run" }
                val count = data[i + 1].toInt() and 0xFF
                repeat(count) { out.write(0) }
                i += 2
            } else {
                out.write(b); i++
            }
        }
        return out.toByteArray()
    }
}

data class DecodedPacket(
    val flags: Int,
    val sequence: Int,
    val messageId: Int,
    val frequency: Frequency,
    /** Body starting AT the message ID, ZeroCode already expanded. */
    val body: ByteArray,
    val appendedAcks: List<Int>,
) {
    val reliable: Boolean get() = flags and PacketFlags.RELIABLE != 0
    val zerocoded: Boolean get() = flags and PacketFlags.ZEROCODED != 0
}

fun decodePacket(raw: ByteArray): DecodedPacket {
    require(raw.size >= 6) { "packet shorter than 6-byte header" }
    val flags = raw[0].toInt() and 0xFF
    val header = ByteBuffer.wrap(raw).order(ByteOrder.BIG_ENDIAN)
    val sequence = header.getInt(1)
    val extraLen = raw[5].toInt() and 0xFF
    var bodyEnd = raw.size

    var acks: List<Int> = emptyList()
    if (flags and PacketFlags.ACK != 0) {
        val count = raw[raw.size - 1].toInt() and 0xFF
        val ackBytes = 1 + count * 4
        acks = (0 until count).map { i ->
            header.getInt(raw.size - ackBytes + i * 4)
        }
        bodyEnd = raw.size - ackBytes
    }

    var body = raw.copyOfRange(6 + extraLen, bodyEnd)
    if (flags and PacketFlags.ZEROCODED != 0) body = ZeroCode.decode(body)
    val id = MessageIdCodec.decode(body, 0)
    return DecodedPacket(flags, sequence, id.id, id.freq, body, acks)
}

fun encodePacket(
    sequence: Int,
    body: ByteArray, // starts with the encoded message ID
    zerocoded: Boolean,
    reliable: Boolean,
    appendedAcks: List<Int> = emptyList(),
): ByteArray {
    var flags = 0
    if (zerocoded) flags = flags or PacketFlags.ZEROCODED
    if (reliable) flags = flags or PacketFlags.RELIABLE
    if (appendedAcks.isNotEmpty()) flags = flags or PacketFlags.ACK
    val wireBody = if (zerocoded) ZeroCode.encode(body) else body
    val ackBytes = if (appendedAcks.isEmpty()) 0 else 1 + appendedAcks.size * 4
    val out = ByteBuffer.allocate(6 + wireBody.size + ackBytes)
        .order(ByteOrder.BIG_ENDIAN)
    out.put(flags.toByte())
    out.putInt(sequence)
    out.put(0) // extra header length: none
    out.put(wireBody)
    for (ack in appendedAcks) out.putInt(ack)
    if (appendedAcks.isNotEmpty()) out.put(appendedAcks.size.toByte())
    return out.array()
}
```

---

## 4. Field-level body IO (little-endian)

Message **bodies** are little-endian (headers are big-endian). UUIDs
are raw 16 bytes. `Variable 1` = u8 length prefix, `Variable 2` = u16
LE length prefix. LLQuaternion travels as 3 × f32.

```kotlin
// app/src/main/java/app/linkpoint/sl/PacketIO.kt
package app.linkpoint.sl

import java.io.ByteArrayOutputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.util.UUID

class PacketWriter {
    private val out = ByteArrayOutputStream()
    private val scratch = ByteBuffer.allocate(8).order(ByteOrder.LITTLE_ENDIAN)

    private fun emitScratch(n: Int): PacketWriter {
        out.write(scratch.array(), 0, n); return this
    }
    fun u8(v: Int): PacketWriter { out.write(v and 0xFF); return this }
    fun u16(v: Int): PacketWriter {
        scratch.clear(); scratch.putShort(v.toShort()); return emitScratch(2)
    }
    fun u32(v: Int): PacketWriter {
        scratch.clear(); scratch.putInt(v); return emitScratch(4)
    }
    fun u64(v: Long): PacketWriter {
        scratch.clear(); scratch.putLong(v); return emitScratch(8)
    }
    /** Signed fields share the u32 bit pattern (e.g. ChatFromViewer channel is S32). */
    fun s32(v: Int): PacketWriter = u32(v)
    fun f32(v: Float): PacketWriter {
        scratch.clear(); scratch.putFloat(v); return emitScratch(4)
    }
    fun f64(v: Double): PacketWriter {
        scratch.clear(); scratch.putDouble(v); return emitScratch(8)
    }
    fun bool(v: Boolean): PacketWriter = u8(if (v) 1 else 0)
    fun uuid(id: UUID): PacketWriter { out.write(id.toBytes()); return this }
    fun vector3(v: Vector3): PacketWriter = f32(v.x).f32(v.y).f32(v.z)
    fun quaternion(q: Quaternion): PacketWriter = f32(q.x).f32(q.y).f32(q.z) // w reconstructed by reader
    fun variable1(data: ByteArray): PacketWriter {
        require(data.size <= 255) { "Variable 1 too long" }
        u8(data.size); out.write(data); return this
    }
    fun variable2(data: ByteArray): PacketWriter {
        require(data.size <= 65535) { "Variable 2 too long" }
        u16(data.size); out.write(data); return this
    }
    fun stringVar1(s: String): PacketWriter = variable1(s.toByteArray(Charsets.UTF_8))
    fun stringVar2(s: String): PacketWriter = variable2(s.toByteArray(Charsets.UTF_8))
    fun fixed(data: ByteArray): PacketWriter { out.write(data); return this }
    fun bytes(): ByteArray = out.toByteArray()
}

class PacketReader(private val buf: ByteArray, offset: Int = 0) {
    var pos: Int = offset
        private set
    private val view = ByteBuffer.wrap(buf).order(ByteOrder.LITTLE_ENDIAN)
    val remaining: Int get() = buf.size - pos

    fun u8(): Int = buf[pos++].toInt() and 0xFF
    fun u16(): Int { val v = view.getShort(pos).toInt() and 0xFFFF; pos += 2; return v }
    fun u32(): Int { val v = view.getInt(pos); pos += 4; return v }
    fun u64(): Long { val v = view.getLong(pos); pos += 8; return v }
    fun f32(): Float { val v = view.getFloat(pos); pos += 4; return v }
    fun f64(): Double { val v = view.getDouble(pos); pos += 8; return v }
    fun bool(): Boolean = u8() != 0
    fun uuid(): UUID { val id = buf.uuidAt(pos); pos += 16; return id }
    fun vector3(): Vector3 = Vector3(f32(), f32(), f32())
    fun quaternion(): Quaternion = Quaternion.fromWire(f32(), f32(), f32())
    fun take(n: Int): ByteArray {
        val out = buf.copyOfRange(pos, pos + n); pos += n; return out
    }
    fun variable1(): ByteArray = take(u8())
    fun variable2(): ByteArray = take(u16())
    fun stringVar1(): String = String(variable1(), Charsets.UTF_8)
    fun stringVar2(): String = String(variable2(), Charsets.UTF_8)
    fun fixed(n: Int): ByteArray = take(n)
}
```

---

## 5. Message table and the core message set (generated style)

In the production tree these classes are generated from
`message_template.msg` by a code generator run at build time — the
same approach as LibreMetaverse.Protocol's source generator and the
477 Java classes in Lumiya. What follows is that generated shape,
hand-written for the core set so the generator's output can be
validated against it. **Never hand-edit generated files in the real
tree; fix the generator or the template diff instead.**

```kotlin
// app/src/main/java/app/linkpoint/sl/messages/MessageTable.kt
// GENERATED from message_template.msg — do not edit by hand.
package app.linkpoint.sl.messages

import app.linkpoint.sl.Frequency

data class MessageDef(
    val name: String,
    val frequency: Frequency,
    val id: Int,
    val trusted: Boolean,
    val zerocoded: Boolean,
    val deprecated: Boolean = false,
)

object MessageTable {
    val PacketAck = MessageDef("PacketAck", Frequency.FIXED, 0xFFFFFFFB.toInt(), false, false)
    val StartPingCheck = MessageDef("StartPingCheck", Frequency.FIXED, 0xFFFFFFF9.toInt(), false, false)
    val CompletePingCheck = MessageDef("CompletePingCheck", Frequency.FIXED, 0xFFFFFFF8.toInt(), false, false)
    val UseCircuitCode = MessageDef("UseCircuitCode", Frequency.LOW, 3, false, false)
    val CompleteAgentMovement = MessageDef("CompleteAgentMovement", Frequency.LOW, 249, false, false)
    val AgentUpdate = MessageDef("AgentUpdate", Frequency.HIGH, 4, false, true)
    val ChatFromViewer = MessageDef("ChatFromViewer", Frequency.LOW, 80, false, false) // NOT zerocoded — master-template trap
    val ChatFromSimulator = MessageDef("ChatFromSimulator", Frequency.LOW, 81, false, false)
    val ImprovedInstantMessage = MessageDef("ImprovedInstantMessage", Frequency.LOW, 254, false, false)
    val ObjectUpdate = MessageDef("ObjectUpdate", Frequency.LOW, 12, false, true)
    val ImprovedTerseObjectUpdate = MessageDef("ImprovedTerseObjectUpdate", Frequency.HIGH, 15, false, false)
    val ObjectUpdateCompressed = MessageDef("ObjectUpdateCompressed", Frequency.LOW, 13, false, true)
    val ObjectUpdateCached = MessageDef("ObjectUpdateCached", Frequency.LOW, 14, false, false)
    val KillObject = MessageDef("KillObject", Frequency.HIGH, 11, false, false)
    val RegionHandshake = MessageDef("RegionHandshake", Frequency.LOW, 148, false, true)
    val RegionHandshakeReply = MessageDef("RegionHandshakeReply", Frequency.LOW, 149, false, false)
    val CoarseLocationUpdate = MessageDef("CoarseLocationUpdate", Frequency.LOW, 6, false, false)
    val TeleportStart = MessageDef("TeleportStart", Frequency.LOW, 72, false, false)
    val TeleportProgress = MessageDef("TeleportProgress", Frequency.LOW, 73, false, false)
    val TeleportFinish = MessageDef("TeleportFinish", Frequency.LOW, 69, false, false)
    val TeleportFailed = MessageDef("TeleportFailed", Frequency.LOW, 70, false, false)
    val LogoutRequest = MessageDef("LogoutRequest", Frequency.LOW, 252, false, false)
    val AvatarAnimation = MessageDef("AvatarAnimation", Frequency.LOW, 20, false, false)
    val ObjectAnimation = MessageDef("ObjectAnimation", Frequency.LOW, 21, false, false)
    val ScriptDialog = MessageDef("ScriptDialog", Frequency.LOW, 380, false, false)
    val AgentAnimation = MessageDef("AgentAnimation", Frequency.LOW, 378, false, false)
    val RequestObjectPropertiesFamily = MessageDef("RequestObjectPropertiesFamily", Frequency.LOW, 245, false, false)
    val ObjectPropertiesFamily = MessageDef("ObjectPropertiesFamily", Frequency.LOW, 246, false, false)

    val ALL: List<MessageDef> = listOf(
        PacketAck, StartPingCheck, CompletePingCheck, UseCircuitCode,
        CompleteAgentMovement, AgentUpdate, ChatFromViewer, ChatFromSimulator,
        ImprovedInstantMessage, ObjectUpdate, ImprovedTerseObjectUpdate,
        ObjectUpdateCompressed, ObjectUpdateCached, KillObject,
        RegionHandshake, RegionHandshakeReply, CoarseLocationUpdate,
        TeleportStart, TeleportProgress, TeleportFinish, TeleportFailed,
        LogoutRequest, AvatarAnimation, ObjectAnimation, ScriptDialog,
        AgentAnimation, RequestObjectPropertiesFamily, ObjectPropertiesFamily,
    )

    private val byKey: Map<Pair<Frequency, Int>, MessageDef> =
        ALL.associateBy { it.frequency to it.id }

    fun lookup(freq: Frequency, id: Int): MessageDef? = byKey[freq to id]
}
```

```kotlin
// app/src/main/java/app/linkpoint/sl/messages/CoreMessages.kt
// GENERATED-style typed messages for the core set.
package app.linkpoint.sl.messages

import app.linkpoint.sl.MessageIdCodec
import app.linkpoint.sl.PacketReader
import app.linkpoint.sl.PacketWriter
import app.linkpoint.sl.Quaternion
import app.linkpoint.sl.Vector3
import java.util.UUID

/** Base for encodable messages: writes the frequency-encoded ID, then blocks. */
abstract class OutMessage(private val def: MessageDef) {
    protected fun writer(): PacketWriter {
        val w = PacketWriter()
        for (b in MessageIdCodec.encode(def.frequency, def.id)) w.u8(b.toInt())
        return w
    }
    abstract fun encode(): ByteArray
    val definition: MessageDef get() = def
}

class UseCircuitCode(
    val circuitCode: Int, val sessionId: UUID, val agentId: UUID,
) : OutMessage(MessageTable.UseCircuitCode) {
    override fun encode(): ByteArray = writer()
        .u32(circuitCode).uuid(sessionId).uuid(agentId) // CircuitInfo block (Single)
        .bytes()
}

class CompleteAgentMovement(
    val agentId: UUID, val sessionId: UUID, val circuitCode: Int,
) : OutMessage(MessageTable.CompleteAgentMovement) {
    override fun encode(): ByteArray = writer()
        .uuid(agentId).uuid(sessionId).u32(circuitCode)
        .bytes()
}

object AgentControl {
    const val AT_POS = 0x0000_0001; const val AT_NEG = 0x0000_0002
    const val LEFT_POS = 0x0000_0004; const val LEFT_NEG = 0x0000_0008
    const val UP_POS = 0x0000_0010; const val UP_NEG = 0x0000_0020
    const val PITCH_POS = 0x0000_0040; const val PITCH_NEG = 0x0000_0080
    const val YAW_POS = 0x0000_0100; const val YAW_NEG = 0x0000_0200
    const val FAST_AT = 0x0000_0400; const val FAST_LEFT = 0x0000_0800
    const val FAST_UP = 0x0000_1000; const val FLY = 0x0000_2000
    const val STOP = 0x0000_4000; const val FINISH_ANIM = 0x0000_8000
    const val STAND_UP = 0x0001_0000; const val SIT_ON_GROUND = 0x0002_0000
    const val MOUSELOOK = 0x0004_0000; const val AWAY = 0x0800_0000
    const val LBUTTON_DOWN = 0x1000_0000; const val LBUTTON_UP = 0x2000_0000
}

class AgentUpdate(
    val agentId: UUID, val sessionId: UUID,
    val bodyRotation: Quaternion, val headRotation: Quaternion,
    val state: Int, // u8
    val cameraCenter: Vector3, val cameraAtAxis: Vector3,
    val cameraLeftAxis: Vector3, val cameraUpAxis: Vector3,
    val far: Float, val controlFlags: Int, val flags: Int, // u8
) : OutMessage(MessageTable.AgentUpdate) {
    override fun encode(): ByteArray = writer()
        .uuid(agentId).uuid(sessionId)
        .quaternion(bodyRotation).quaternion(headRotation)
        .u8(state)
        .vector3(cameraCenter).vector3(cameraAtAxis)
        .vector3(cameraLeftAxis).vector3(cameraUpAxis)
        .f32(far).u32(controlFlags).u8(flags)
        .bytes()
}

object ChatType {
    const val WHISPER = 0; const val NORMAL = 1; const val SHOUT = 2
    const val START_TYPING = 4; const val STOP_TYPING = 5
    const val DEBUG = 6; const val OWNER_SAY = 8
    const val REGION_SAY = 9; const val REGION_SAY_TO = 10
}

class ChatFromViewer(
    val agentId: UUID, val sessionId: UUID,
    val message: String, val type: Int, val channel: Int,
) : OutMessage(MessageTable.ChatFromViewer) {
    override fun encode(): ByteArray = writer()
        .uuid(agentId).uuid(sessionId)          // AgentData block
        .stringVar2(message).u8(type).s32(channel) // ChatData block
        .bytes()
}

data class ChatFromSimulator(
    val fromName: String, val sourceId: UUID, val ownerId: UUID,
    val sourceType: Int, val chatType: Int, val audible: Int,
    val position: Vector3, val message: String,
) {
    companion object {
        fun decode(r: PacketReader): ChatFromSimulator = ChatFromSimulator(
            fromName = r.stringVar1(),
            sourceId = r.uuid(),
            ownerId = r.uuid(),
            sourceType = r.u8(),
            chatType = r.u8(),
            audible = r.u8(),
            position = r.vector3(),
            message = r.stringVar2(),
        )
    }
}

object IMDialog {
    const val MESSAGE = 0
    const val INVENTORY_OFFERED = 3; const val INVENTORY_ACCEPTED = 4
    const val GROUP_INVITATION = 25; const val GROUP_NOTICE = 27
    const val GOTO_URL = 28; const val BUSY_AUTO_RESPONSE = 32
    const val SESSION_GROUP_START = 35; const val SESSION_CONFERENCE_START = 38
    const val SESSION_SEND = 39; const val SESSION_DROP = 40
    const val MESSAGE_BOX = 41; const val LURE_USER = 44
    const val LURE_RESPONSE = 45; const val TELEPORT_REQUEST = 47
}

data class ImprovedInstantMessage(
    val agentId: UUID, val sessionId: UUID,
    val fromGroup: Boolean, val toAgentId: UUID,
    val parentEstateId: Int, val regionId: UUID,
    val position: Vector3, val offline: Int, val dialog: Int,
    val imSessionId: UUID, val timestamp: Int,
    val fromAgentName: String, val message: String,
    val binaryBucket: ByteArray,
) : OutMessage(MessageTable.ImprovedInstantMessage) {
    override fun encode(): ByteArray = writer()
        .uuid(agentId).uuid(sessionId)               // AgentData block
        .bool(fromGroup).uuid(toAgentId).u32(parentEstateId)
        .uuid(regionId).vector3(position)
        .u8(offline).u8(dialog).uuid(imSessionId)
        .u32(timestamp).stringVar1(fromAgentName)
        .stringVar2(message).variable2(binaryBucket) // MessageBlock
        .bytes()

    companion object {
        fun decode(r: PacketReader): ImprovedInstantMessage {
            val agentId = r.uuid(); val sessionId = r.uuid()
            val fromGroup = r.bool(); val toAgentId = r.uuid()
            val parentEstateId = r.u32(); val regionId = r.uuid()
            val position = r.vector3(); val offline = r.u8()
            val dialog = r.u8(); val imSessionId = r.uuid()
            val timestamp = r.u32(); val fromName = r.stringVar1()
            val message = r.stringVar2(); val bucket = r.variable2()
            return ImprovedInstantMessage(
                agentId, sessionId, fromGroup, toAgentId, parentEstateId,
                regionId, position, offline, dialog, imSessionId,
                timestamp, fromName, message, bucket,
            )
        }
    }
}

data class RegionHandshake(
    val regionFlags: Int, val simAccess: Int, val simName: String,
    val simOwner: UUID, val isEstateManager: Boolean,
    val waterHeight: Float, val billableFactor: Float,
    val cacheId: UUID, val cpuClassId: Int, val cpuRatio: Float,
    val coloVersion: String, val gridUrl: String,
    val productSku: String, val productName: String,
) {
    companion object {
        /** Walk EVERY field in template order — guessing lengths to
         *  "skip" blocks is how handshake parsers desynchronise. */
        fun decode(r: PacketReader): RegionHandshake = RegionHandshake(
            regionFlags = r.u32(),
            simAccess = r.u8(),
            simName = r.stringVar1(),
            simOwner = r.uuid(),
            isEstateManager = r.bool(),
            waterHeight = r.f32(),
            billableFactor = r.f32(),
            cacheId = r.uuid(),
            cpuClassId = r.u32(),
            cpuRatio = r.f32(),
            coloVersion = r.stringVar1(),
            gridUrl = r.stringVar1(),
            productSku = r.stringVar1(),
            productName = r.stringVar1(),
        )
    }
}

class RegionHandshakeReply(
    val agentId: UUID, val sessionId: UUID,
) : OutMessage(MessageTable.RegionHandshakeReply) {
    override fun encode(): ByteArray = writer()
        .uuid(agentId).uuid(sessionId)
        .u32(0) // RegionInfo flags: none
        .bytes()
}

/** Coarse (radar) locations: parallel byte arrays, 16 m cells in X/Y. */
data class CoarseLocationUpdate(val agents: List<Entry>) {
    data class Entry(val x: Int, val y: Int, val z: Int, val isYou: Boolean)

    companion object {
        fun decode(r: PacketReader): CoarseLocationUpdate {
            val xs = r.variable1(); val ys = r.variable1(); val zs = r.variable1()
            val count = minOf(xs.size, ys.size, zs.size)
            val entries = MutableList(count) { i ->
                Entry(
                    x = (xs[i].toInt() and 0xFF) * 16,
                    y = (ys[i].toInt() and 0xFF) * 16,
                    z = (zs[i].toInt() and 0xFF) * 4,
                    isYou = false,
                )
            }
            if (r.remaining >= 2) {
                val you = r.u16()
                if (you in entries.indices) {
                    entries[you] = entries[you].copy(isYou = true)
                }
                if (r.remaining >= 2) r.u16() // Prey — unused by radar
            }
            return CoarseLocationUpdate(entries)
        }
    }
}

class PacketAckMessage(val sequences: List<Int>) : OutMessage(MessageTable.PacketAck) {
    override fun encode(): ByteArray {
        val w = writer()
        w.u8(sequences.size) // Packets block is Variable (count byte)
        for (s in sequences) w.u32(s)
        return w.bytes()
    }
}

class CompletePingCheck(val pingId: Int) : OutMessage(MessageTable.CompletePingCheck) {
    override fun encode(): ByteArray = writer().u8(pingId).bytes()
}

class LogoutRequest(
    val agentId: UUID, val sessionId: UUID,
) : OutMessage(MessageTable.LogoutRequest) {
    override fun encode(): ByteArray = writer().uuid(agentId).uuid(sessionId).bytes()
}
```

---

## 6. The UDP circuit with coroutines

One `Circuit` per region. It owns the socket, sequence numbers, the
unacked-reliable queue with resend timers, ACK batching, duplicate
suppression, ping handling, and dispatch. All socket work runs on
`Dispatchers.IO`; handlers are invoked on the circuit's scope — UI
state flows out through `StateFlow` (§9), never by touching Compose
state from the IO dispatcher directly.

### 6.1 Socket transport abstraction

```kotlin
// app/src/main/java/app/linkpoint/sl/transport/UdpTransport.kt
package app.linkpoint.sl.transport

import java.net.InetSocketAddress

/** Raw datagram transport. The circuit speaks SL; this only moves bytes. */
interface UdpTransport {
    suspend fun send(to: InetSocketAddress, packet: ByteArray)
    /** Inbound datagrams as a cold flow: (sender, bytes). */
    fun packets(): kotlinx.coroutines.flow.Flow<Pair<InetSocketAddress, ByteArray>>
    fun close()
}
```

### 6.2 DatagramSocket transport (default)

```kotlin
// app/src/main/java/app/linkpoint/sl/transport/DatagramSocketTransport.kt
package app.linkpoint.sl.transport

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn
import kotlinx.coroutines.isActive
import kotlinx.coroutines.withContext
import java.net.DatagramPacket
import java.net.DatagramSocket
import java.net.InetSocketAddress
import kotlin.coroutines.coroutineContext

class DatagramSocketTransport : UdpTransport {
    // One socket for all regions (the simulator replies to the source
    // endpoint it sees). Do NOT bind a fixed local port: Android NAT /
    // CGNAT mappings are per-flow, and the circuit code in the viewer
    // makes the same choice.
    private val socket = DatagramSocket()

    @Volatile private var closed = false

    override suspend fun send(to: InetSocketAddress, packet: ByteArray) {
        withContext(Dispatchers.IO) {
            socket.send(DatagramPacket(packet, packet.size, to.address, to.port))
        }
    }

    override fun packets(): Flow<Pair<InetSocketAddress, ByteArray>> = flow {
        val buffer = ByteArray(65535) // max UDP payload; SL packets are far smaller, but never truncate silently
        while (coroutineContext.isActive && !closed) {
            val pkt = DatagramPacket(buffer, buffer.size)
            try {
                socket.receive(pkt) // blocking call — this flow is pinned to IO below
            } catch (e: Exception) {
                if (closed || socket.isClosed) break else throw e
            }
            val from = InetSocketAddress(pkt.address, pkt.port)
            // copyOf: the receive buffer is reused on the next iteration.
            emit(from to pkt.data.copyOf(pkt.length))
        }
    }.flowOn(Dispatchers.IO)

    override fun close() {
        closed = true
        socket.close() // unblocks receive() with a SocketException, ending the flow
    }
}
```

### 6.3 The circuit itself

```kotlin
// app/src/main/java/app/linkpoint/sl/Circuit.kt
// Ported in structure from LibreMetaverse.Transport.UDPClient and the
// viewer's LLCircuit. Constants are tuned for lossy mobile links.
package app.linkpoint.sl

import app.linkpoint.sl.messages.CompletePingCheck
import app.linkpoint.sl.messages.MessageTable
import app.linkpoint.sl.messages.OutMessage
import app.linkpoint.sl.messages.PacketAckMessage
import app.linkpoint.sl.transport.UdpTransport
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import java.net.InetSocketAddress
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicInteger

class Circuit(
    private val transport: UdpTransport,
    val endpoint: InetSocketAddress,
    private val scope: CoroutineScope,
) {
    companion object {
        const val RESEND_BASE_MS = 100L
        const val MAX_RESENDS = 8
        const val ACK_FLUSH_MS = 50L
        const val ACK_BATCH_MAX = 255
    }

    private val sequenceCounter = AtomicInteger(0)
    private fun nextSequence(): Int {
        var next: Int
        do {
            next = (sequenceCounter.get() + 1) and 0x7FFF_FFFF
            if (next == 0) next = 1 // 0 is never a valid sequence
        } while (!sequenceCounter.compareAndSet(sequenceCounter.get(), next))
        return next
    }

    private data class Pending(
        val packet: ByteArray,
        val sequence: Int,
        var lastSentAt: Long,
        var resends: Int,
    )

    private val pending = ConcurrentHashMap<Int, Pending>()
    private val seenSequences = ConcurrentHashMap.newKeySet<Int>()
    private val ackQueue = ArrayDeque<Int>()
    private val ackLock = Any()

    private var jobs: List<Job> = emptyList()
    @Volatile private var open = false

    /** Fires when a reliable message exhausts resends: the region is
     *  unreachable. The session layer treats this as a disconnect —
     *  never keep "sending into the void" and ghosting the avatar. */
    var onDead: (() -> Unit)? = null

    /** Unhandled inbound messages, for logging / incremental support. */
    private val _unhandled = MutableSharedFlow<Pair<String, PacketReader>>(extraBufferCapacity = 64)
    val unhandled: SharedFlow<Pair<String, PacketReader>> = _unhandled.asSharedFlow()

    private val handlers = HashMap<String, (PacketReader) -> Unit>()
    fun on(name: String, handler: (PacketReader) -> Unit) {
        handlers[name] = handler
    }

    fun start() {
        check(!open) { "circuit already started" }
        open = true
        val receiveJob = scope.launch {
            transport.packets().collect { (from, raw) ->
                if (from.address == endpoint.address && from.port == endpoint.port) {
                    handleInbound(raw)
                }
            }
        }
        val resendJob = scope.launch {
            while (open) {
                delay(RESEND_BASE_MS)
                pumpResends()
            }
        }
        val ackJob = scope.launch {
            while (open) {
                delay(ACK_FLUSH_MS)
                flushAcks()
            }
        }
        jobs = listOf(receiveJob, resendJob, ackJob)
    }

    /** Send a message; reliability defaults off, table zerocoded flag rules. */
    fun send(message: OutMessage, reliable: Boolean = false) {
        val def = message.definition
        val seq = nextSequence()
        val packet = encodePacket(
            sequence = seq,
            body = message.encode(),
            zerocoded = def.zerocoded,
            reliable = reliable,
        )
        scope.launch { transport.send(endpoint, packet) }
        if (reliable) {
            pending[seq] = Pending(packet, seq, System.currentTimeMillis(), 0)
        }
    }

    fun sendReliable(message: OutMessage) = send(message, reliable = true)

    private fun pumpResends() {
        val now = System.currentTimeMillis()
        for ((seq, p) in pending) {
            val due = RESEND_BASE_MS * (1 + p.resends)
            if (now - p.lastSentAt < due) continue
            if (p.resends >= MAX_RESENDS) {
                pending.remove(seq)
                onDead?.invoke()
                return
            }
            p.resends++
            p.lastSentAt = now
            val copy = p.packet.copyOf()
            copy[0] = (copy[0].toInt() or PacketFlags.RESENT).toByte()
            scope.launch { transport.send(endpoint, copy) }
        }
    }

    private fun queueAck(sequence: Int) {
        synchronized(ackLock) {
            ackQueue.addLast(sequence)
        }
    }

    private fun flushAcks() {
        val batch: List<Int> = synchronized(ackLock) {
            if (ackQueue.isEmpty()) return
            val n = minOf(ackQueue.size, ACK_BATCH_MAX)
            List(n) { ackQueue.removeFirst() }
        }
        // PacketAck goes out unreliably with a fresh sequence.
        val seq = nextSequence()
        val packet = encodePacket(
            sequence = seq,
            body = PacketAckMessage(batch).encode(),
            zerocoded = false,
            reliable = false,
        )
        scope.launch { transport.send(endpoint, packet) }
    }

    private fun handleInbound(raw: ByteArray) {
        val pkt = try {
            decodePacket(raw)
        } catch (e: Exception) {
            return // malformed datagram: drop, never crash the session on wire garbage
        }
        for (acked in pkt.appendedAcks) pending.remove(acked)
        if (pkt.reliable) {
            queueAck(pkt.sequence)
            if (!seenSequences.add(pkt.sequence)) return // duplicate resend of an already-handled packet
            if (seenSequences.size > 4096) {
                // Bounded window; at session scale this is plenty.
                seenSequences.clear()
                seenSequences.add(pkt.sequence)
            }
        }

        val def = MessageTable.lookup(pkt.frequency, pkt.messageId) ?: return
        val idLen = MessageIdCodec.encodedLength(pkt.frequency)
        val reader = PacketReader(pkt.body, idLen)

        when (def.name) {
            "PacketAck" -> {
                val count = reader.u8()
                repeat(count) { pending.remove(reader.u32()) }
                return
            }
            "StartPingCheck" -> {
                val pingId = reader.u8()
                send(CompletePingCheck(pingId))
                return
            }
        }

        val handler = handlers[def.name]
        if (handler != null) handler(reader) else _unhandled.tryEmit(def.name to reader)
    }

    fun close() {
        open = false
        jobs.forEach { it.cancel() }
        pending.clear()
    }
}
```

### 6.4 NIO DatagramChannel variant

On a desktop/JVM target (or an Android build that multiplexes many
circuits), a non-blocking `DatagramChannel` driven by a selector is
cleaner than one blocking socket per flow. The circuit does not care:
it only sees `UdpTransport`.

```kotlin
// app/src/main/java/app/linkpoint/sl/transport/DatagramChannelTransport.kt
package app.linkpoint.sl.transport

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn
import kotlinx.coroutines.isActive
import kotlinx.coroutines.withContext
import java.net.InetSocketAddress
import java.nio.ByteBuffer
import java.nio.channels.DatagramChannel
import kotlin.coroutines.coroutineContext

class DatagramChannelTransport : UdpTransport {
    private val channel: DatagramChannel = DatagramChannel.open().apply {
        configureBlocking(true) // blocking mode + IO dispatcher: simplest correct model
        bind(null)              // ephemeral local port
    }

    override suspend fun send(to: InetSocketAddress, packet: ByteArray) {
        withContext(Dispatchers.IO) {
            channel.send(ByteBuffer.wrap(packet), to)
        }
    }

    override fun packets(): Flow<Pair<InetSocketAddress, ByteArray>> = flow {
        val buffer = ByteBuffer.allocate(65535)
        while (coroutineContext.isActive && channel.isOpen) {
            buffer.clear()
            val from = channel.receive(buffer) as? InetSocketAddress ?: continue
            buffer.flip()
            val bytes = ByteArray(buffer.remaining())
            buffer.get(bytes)
            emit(from to bytes)
        }
    }.flowOn(Dispatchers.IO)

    override fun close() {
        channel.close()
    }
}
```

### 6.5 AgentUpdate loop

```kotlin
// app/src/main/java/app/linkpoint/sl/AgentUpdateLoop.kt
package app.linkpoint.sl

import app.linkpoint.sl.messages.AgentUpdate
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import java.util.UUID

class AgentUpdateLoop(
    private val circuit: Circuit,
    private val agentId: UUID,
    private val sessionId: UUID,
    private val scope: CoroutineScope,
) {
    @Volatile var controlFlags: Int = 0
    @Volatile var cameraCenter: Vector3 = Vector3(128f, 128f, 24f)
    @Volatile var cameraAtAxis: Vector3 = Vector3(0f, 1f, 0f)
    @Volatile var cameraLeftAxis: Vector3 = Vector3(-1f, 0f, 0f)
    @Volatile var cameraUpAxis: Vector3 = Vector3(0f, 0f, 1f)
    @Volatile var bodyRotation: Quaternion = Quaternion.IDENTITY
    @Volatile var headRotation: Quaternion = Quaternion.IDENTITY
    @Volatile var drawDistance: Float = 128f

    private var job: Job? = null

    /** ~15 Hz, matching the viewer's throttled cadence on constrained links. */
    fun start(intervalMs: Long = 66) {
        if (job != null) return
        job = scope.launch {
            while (true) {
                circuit.send(
                    AgentUpdate(
                        agentId, sessionId, bodyRotation, headRotation,
                        state = 0,
                        cameraCenter, cameraAtAxis, cameraLeftAxis, cameraUpAxis,
                        far = drawDistance, controlFlags = controlFlags, flags = 0,
                    ),
                )
                delay(intervalMs)
            }
        }
    }

    fun setControl(flag: Int, down: Boolean) {
        controlFlags = if (down) controlFlags or flag else controlFlags and flag.inv()
    }

    fun stop() {
        job?.cancel(); job = null
        controlFlags = 0
    }
}
```

---

## 7. Capabilities with OkHttp

After login you hold a seed capability. POST it an LLSD array of cap
names, receive an LLSD map of name → per-region URL. Rules: URLs are
per-region and per-session (re-negotiate on teleport), availability
varies by grid (check before use, fall back to UDP where the viewer
does), and feature limits come from `SimulatorFeatures`, never from
constants in your code.

```kotlin
// app/src/main/java/app/linkpoint/sl/Caps.kt
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.LLSDXml
import app.linkpoint.sl.llsd.llsdArrOf
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.IOException
import java.util.concurrent.TimeUnit

class CapsException(message: String, val cap: String, val status: Int) :
    IOException("$message (cap=$cap, http=$status)")

class Caps private constructor(
    private val http: OkHttpClient,
    private val urls: Map<String, String>,
) {
    fun has(name: String): Boolean = urls.containsKey(name)
    fun url(name: String): String =
        urls[name] ?: throw CapsException("capability not granted by this region", name, 0)
    fun maybeUrl(name: String): String? = urls[name]
    fun grantedNames(): Set<String> = urls.keys

    /** POST an LLSD payload and parse an LLSD reply. */
    suspend fun post(name: String, payload: LLSD): LLSD = withContext(Dispatchers.IO) {
        val request = Request.Builder()
            .url(url(name))
            .header("Content-Type", "application/llsd+xml")
            .post(LLSDXml.write(payload).toRequestBody(LLSD_MEDIA_TYPE))
            .build()
        http.newCall(request).execute().use { res ->
            if (!res.isSuccessful) throw CapsException("cap POST failed", name, res.code)
            val text = res.body?.string().orEmpty()
            if (text.isBlank()) LLSD.Map(emptyMap()) else LLSDXml.parse(text)
        }
    }

    /** Raw bytes path for GetTexture / GetMesh (headers + ranges live here). */
    suspend fun getBytes(
        name: String,
        query: Map<String, String> = emptyMap(),
        headers: Map<String, String> = emptyMap(),
    ): ByteArray = withContext(Dispatchers.IO) {
        var url = url(name)
        if (query.isNotEmpty()) {
            val qs = query.entries.joinToString("&") { (k, v) ->
                "${java.net.URLEncoder.encode(k, "UTF-8")}=${java.net.URLEncoder.encode(v, "UTF-8")}"
            }
            url = if (url.contains("?")) "$url&$qs" else "$url?$qs"
        }
        val builder = Request.Builder().url(url)
        for ((k, v) in headers) builder.header(k, v)
        http.newCall(builder.build()).execute().use { res ->
            if (!res.isSuccessful && res.code != 206) {
                throw CapsException("cap GET failed", name, res.code)
            }
            res.body?.bytes() ?: throw CapsException("empty body", name, res.code)
        }
    }

    companion object {
        val LLSD_MEDIA_TYPE = "application/llsd+xml".toMediaType()

        /** Caps a thin/mobile client should request on every region entry. */
        val WANTED: List<String> = listOf(
            "EventQueueGet",
            "FetchInventory2", "FetchInventoryDescendents2",
            "FetchLib2", "FetchLibDescendents2",
            "InventoryAPIv3", "LibraryAPIv3",
            "GetTexture", "GetMesh", "GetMesh2",
            "GetMetadata", "GetObjectCost", "GetObjectPhysicsData",
            "SimulatorFeatures", "ServerReleaseNotes",
            "ExtEnvironment", "EnvironmentSettings", "RenderMaterials",
            "AgentPreferences", "AgentState", "AvatarRenderInfo",
            "CharacterProperties", "GetDisplayNames",
            "ChatSessionRequest", "GroupAPIv1", "GroupMemberData",
            "HomeLocation", "LandResources", "RemoteParcelRequest",
            "NewFileAgentInventory", "InventoryThumbnailUpload",
            "UpdateAgentAppearance", "UpdateAgentInformation",
            "ProductInfoRequest", "SearchStatRequest",
            "VoiceSignalingRequest", "ProvisionVoiceAccountRequest",
            "IncrementCOFVersion",
        )

        suspend fun negotiate(
            seedCap: String,
            http: OkHttpClient,
            wanted: List<String> = WANTED,
        ): Caps = withContext(Dispatchers.IO) {
            val body = LLSDXml.write(llsdArrOf(*wanted.map { LLSD.Str(it) }.toTypedArray()))
            val request = Request.Builder()
                .url(seedCap)
                .header("Content-Type", "application/llsd+xml")
                .post(body.toRequestBody(LLSD_MEDIA_TYPE))
                .build()
            http.newCall(request).execute().use { res ->
                if (!res.isSuccessful) {
                    throw CapsException("seed cap negotiation failed", "<seed>", res.code)
                }
                val map = LLSDXml.parse(res.body?.string().orEmpty()).asMap()
                val urls = map.entries.mapNotNull { (k, v) ->
                    (v as? LLSD.Str)?.value?.takeIf { it.startsWith("http") }?.let { k to it }
                }.toMap()
                Caps(http, urls)
            }
        }

        /** Shared client factory: caps calls are latency-tolerant but
         *  the event queue long-poll needs a long read timeout (§9). */
        fun httpClient(): OkHttpClient = OkHttpClient.Builder()
            .connectTimeout(15, TimeUnit.SECONDS)
            .readTimeout(60, TimeUnit.SECONDS) // EventQueueGet holds ~30 s by design
            .writeTimeout(15, TimeUnit.SECONDS)
            .retryOnConnectionFailure(true)
            .build()
    }
}

/** SimulatorFeatures: query, never hardcode. */
data class SimulatorFeatures(
    val meshUploadEnabled: Boolean,
    val pbrEnabled: Boolean,
    val voiceMode: String, // "webrtc" | "vivox" | "none" | other
    val raw: Map<String, LLSD>,
)

suspend fun Caps.fetchSimulatorFeatures(): SimulatorFeatures {
    val raw = post("SimulatorFeatures", LLSD.Map(emptyMap())).asMap()
    val voice = (raw["VoiceVersion"] as? LLSD.Str)?.value
        ?: (raw["voice"] as? LLSD.Str)?.value
    return SimulatorFeatures(
        meshUploadEnabled = raw["MeshUploadEnabled"]?.asBool(true) ?: true,
        pbrEnabled = raw["PBREnabled"]?.asBool() == true || raw["GLTFEnabled"]?.asBool() == true,
        voiceMode = when {
            voice?.contains("webrtc", ignoreCase = true) == true -> "webrtc"
            voice != null -> "vivox"
            else -> "none"
        },
        raw = raw,
    )
}
```

### 7.1 Inventory: FetchInventoryDescendents2 + AIS3

```kotlin
// app/src/main/java/app/linkpoint/sl/Inventory.kt
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.llsdMapOf
import java.util.UUID

enum class AssetType(val id: Int) {
    TEXTURE(0), SOUND(1), CALLING_CARD(2), LANDMARK(3), SCRIPT(5),
    CLOTHING(6), OBJECT(7), NOTECARD(8), CATEGORY(9), SOUND_WAV(10),
    TEXTURE_TGA(11), BODYPART(13), TRASH(14), SNAPSHOT(15),
    ATTACHMENT(17), WEARABLE(18), ANIMATION(19), GESTURE(20),
    MESH(22), LINK(24), LINK_FOLDER(25), MATERIAL(26), UNKNOWN(-1);

    companion object {
        fun fromId(id: Int): AssetType = entries.firstOrNull { it.id == id } ?: UNKNOWN
    }
}

enum class InventoryType(val id: Int) {
    TEXTURE(0), SOUND(1), LANDMARK(3), CLOTHING(5), OBJECT(6),
    NOTECARD(7), CATEGORY(8), SCRIPT(10), SNAPSHOT(15), ATTACHMENT(17),
    WEARABLE(18), ANIMATION(19), GESTURE(20), MESH(22), MATERIAL(26),
    UNKNOWN(-1);

    companion object {
        fun fromId(id: Int): InventoryType = entries.firstOrNull { it.id == id } ?: UNKNOWN
    }
}

data class InventoryItem(
    val itemId: UUID, val parentId: UUID, val name: String,
    val assetId: UUID, val assetType: AssetType, val invType: InventoryType,
    val isLink: Boolean, val createdAt: Int, val flags: Int,
    val baseMask: Int, val ownerMask: Int, val groupMask: Int,
    val everyoneMask: Int, val nextOwnerMask: Int,
)

data class InventoryFolder(
    val folderId: UUID, val parentId: UUID, val name: String,
    val typeDefault: Int, val version: Int,
)

data class FolderContents(
    val folders: List<InventoryFolder>,
    val items: List<InventoryItem>,
    val version: Int,
)

private fun LLSD.mapOrEmpty(): Map<String, LLSD> = (this as? LLSD.Map)?.entries ?: emptyMap()
private fun LLSD.arrOrEmpty(): List<LLSD> = (this as? LLSD.Arr)?.items ?: emptyList()
private fun Map<String, LLSD>.str(key: String, default: String = ""): String =
    (this[key] as? LLSD.Str)?.value ?: default
private fun Map<String, LLSD>.int(key: String, default: Int = 0): Int =
    (this[key] as? LLSD.Int)?.value ?: (this[key] as? LLSD.Real)?.value?.toInt() ?: default
private fun Map<String, LLSD>.uuid(key: String): UUID =
    (this[key] as? LLSD.Uuid)?.value ?: throw IllegalStateException("missing uuid '$key'")

/**
 * Fetch one folder lazily. Cache by (folderId, version) in the caller —
 * eager whole-tree fetch at login is the classic mobile stall, and
 * accounts routinely hold tens of thousands of items.
 */
suspend fun Caps.fetchFolder(agentId: UUID, folderId: UUID): FolderContents {
    val resp = post(
        "FetchInventoryDescendents2",
        llsdMapOf(
            "agent_id" to LLSD.Uuid(agentId),
            "folder_id" to LLSD.Uuid(folderId),
            "owner_id" to LLSD.Uuid(agentId),
            "sort_order" to LLSD.Int(0),
            "fetch_folders" to LLSD.Int(1),
            "fetch_items" to LLSD.Int(1),
            "fetch_links" to LLSD.Int(1),
        ),
    ).mapOrEmpty()

    val folders = resp["folders"].arrOrEmpty().map { raw ->
        val m = raw.mapOrEmpty()
        InventoryFolder(
            folderId = m.uuid("folder_id"), parentId = m.uuid("parent_id"),
            name = m.str("name"), typeDefault = m.int("type_default", -1),
            version = m.int("version"),
        )
    }
    val items = resp["items"].arrOrEmpty().map { raw ->
        val m = raw.mapOrEmpty()
        val perms = m["permissions"].mapOrEmpty()
        val type = AssetType.fromId(m.int("type", -1))
        InventoryItem(
            itemId = m.uuid("item_id"), parentId = m.uuid("parent_id"),
            name = m.str("name"), assetId = m.uuid("asset_id"),
            assetType = type,
            invType = InventoryType.fromId(m.int("inv_type", -1)),
            isLink = type == AssetType.LINK || type == AssetType.LINK_FOLDER,
            createdAt = m.int("created_at"), flags = m.int("flags"),
            baseMask = perms.int("base_mask"), ownerMask = perms.int("owner_mask"),
            groupMask = perms.int("group_mask"), everyoneMask = perms.int("everyone_mask"),
            nextOwnerMask = perms.int("next_owner_mask"),
        )
    }
    return FolderContents(folders, items, resp.int("version"))
}

/** AIS3 link creation (Current Outfit Folder and friends). */
suspend fun Caps.aisCreateLink(
    agentId: UUID, folderId: UUID, targetItemId: UUID,
    name: String, linkFolder: Boolean,
): UUID {
    val resp = post(
        "InventoryAPIv3",
        llsdMapOf(
            "agent-id" to LLSD.Uuid(agentId),
            "folder-id" to LLSD.Uuid(folderId),
            "item-name" to LLSD.Str(name),
            "linked-id" to LLSD.Uuid(targetItemId),
            "type" to LLSD.Int(if (linkFolder) AssetType.LINK_FOLDER.id else AssetType.LINK.id),
            "inv-type" to LLSD.Int(if (linkFolder) InventoryType.CATEGORY.id else InventoryType.OBJECT.id),
        ),
    ).mapOrEmpty()
    return resp.uuid("item_id")
}
```

### 7.2 GetTexture / GetMesh helpers

```kotlin
// app/src/main/java/app/linkpoint/sl/AssetFetch.kt
package app.linkpoint.sl

import java.util.UUID

/** Fetch a texture codestream (JPEG 2000). Decoding is platform work:
 *  pass the bytes to your OpenJPEG-backed decoder (Lumiya ships a
 *  native OpenJPEG build; a modern tree should use a maintained J2C
 *  decoder module behind the same seam). Discard-level refinement is
 *  driven by fetching progressively larger prefixes of the stream. */
suspend fun Caps.fetchTexture(textureId: UUID): ByteArray =
    getBytes(
        if (has("GetTexture")) "GetTexture" else error("GetTexture not granted"),
        query = mapOf("texture_id" to textureId.toString()),
        headers = mapOf("Accept" to "image/x-j2c"),
    )

suspend fun Caps.fetchMesh(meshId: UUID): ByteArray =
    getBytes(
        if (has("GetMesh2")) "GetMesh2" else "GetMesh",
        query = mapOf("mesh_id" to meshId.toString()),
        headers = mapOf("Accept" to "application/octet-stream"),
    )
```

### 7.3 Ktor variant notes

Swap §7's OkHttp calls for Ktor `HttpClient` when the same code must
run on JVM desktop tests: keep the `Caps` public surface identical
(`post`, `getBytes`, `negotiate` as suspend functions), back it with
`HttpClient(OkHttp)` or `CIO`, set `ContentType.parse("application/llsd+xml")`
explicitly (Ktor will otherwise default to JSON plugins if installed),
and disable any JSON content-negotiation plugin for cap calls — LLSD
XML is not negotiable. The Lumiya line stays on OkHttp because the
recovered codebase and its interceptors (logging, retry, proxy) are
already OkHttp-shaped.

---

## 8. Login + MFA flow

Login is a state machine. The MFA challenge arrives as a *failed*
login whose reply carries `reason` + `mfa_hash`: prompt for the TOTP
code, resubmit the same request plus `token` + `mfa_hash`. Keep the
hash in memory only — the desktop viewer persists it in an encrypted
protected store; an app without one must not write it to disk
(SharedPreferences is not an encrypted store).

```kotlin
// app/src/main/java/app/linkpoint/sl/Login.kt
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.LLSDXml
import app.linkpoint.sl.llsd.llsdArrOf
import app.linkpoint.sl.llsd.llsdMapOf
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.withContext
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import java.util.UUID

const val AGNI_LOGIN_URI = "https://login.agni.lindenlab.com/cgi-bin/login.cgi"
const val ADITI_LOGIN_URI = "https://login.aditi.lindenlab.com/cgi-bin/login.cgi"

sealed class LoginState {
    object Idle : LoginState()
    object Authenticating : LoginState()
    data class MfaChallenge(val mfaHash: String, val message: String) : LoginState()
    data class EstablishingCircuit(val session: LoginSession) : LoginState()
    data class InWorld(val session: LoginSession) : LoginState()
    data class Failed(val reason: String, val detail: String? = null) : LoginState()
}

data class LoginSession(
    val agentId: UUID, val sessionId: UUID, val secureSessionId: UUID,
    val circuitCode: Int, val simHost: String, val simPort: Int,
    val seedCapability: String,
    val firstName: String, val lastName: String,
    val inventoryRootFolderId: UUID, val libraryRootFolderId: UUID,
    val regionX: Int, val regionY: Int,
)

data class LoginRequest(
    val firstName: String,
    val lastName: String,
    /** Credential token as the login service expects it ("$1$"+md5 legacy
     *  scheme). Derived in the platform layer; NEVER logged, NEVER stored. */
    val credentialToken: String,
    val start: String = "last", // "home" | "last" | "uri:Region&x&y&z"
    val channel: String,        // unique viewer channel — TPV policy
    val version: String,
    val platform: String = "and",
    val mac: String,
    val id0: String,
    val mfaToken: String? = null,
    val mfaHash: String? = null,
)

class LoginMachine(
    private val http: OkHttpClient,
    private val loginUri: String = AGNI_LOGIN_URI,
) {
    private val _state = MutableStateFlow<LoginState>(LoginState.Idle)
    val state: StateFlow<LoginState> = _state.asStateFlow()

    private var pending: LoginRequest? = null

    suspend fun login(request: LoginRequest) {
        pending = request
        _state.value = LoginState.Authenticating
        submit(request)
    }

    suspend fun submitMfa(code: String) {
        val current = _state.value as? LoginState.MfaChallenge
            ?: error("submitMfa outside an MFA challenge")
        val base = pending ?: error("no pending login request")
        _state.value = LoginState.Authenticating
        submit(base.copy(mfaToken = code, mfaHash = current.mfaHash))
    }

    fun markInWorld() {
        val current = _state.value
        if (current is LoginState.EstablishingCircuit) {
            _state.value = LoginState.InWorld(current.session)
        }
    }

    fun markFailed(reason: String) {
        _state.value = LoginState.Failed(reason)
    }

    private suspend fun submit(request: LoginRequest) {
        val reply: Map<String, LLSD> = try {
            withContext(Dispatchers.IO) {
                val req = Request.Builder()
                    .url(loginUri)
                    .header("Content-Type", "application/llsd+xml")
                    .post(LLSDXml.write(buildBody(request)).toRequestBody(Caps.LLSD_MEDIA_TYPE))
                    .build()
                http.newCall(req).execute().use { res ->
                    if (!res.isSuccessful) {
                        _state.value = LoginState.Failed("Login service HTTP ${res.code}")
                        return@withContext emptyMap()
                    }
                    (LLSDXml.parse(res.body?.string().orEmpty()) as? LLSD.Map)?.entries
                        ?: emptyMap()
                }
            }
        } catch (e: Exception) {
            _state.value = LoginState.Failed("Login service unreachable", e.message)
            return
        }
        if (reply.isEmpty() && _state.value is LoginState.Failed) return

        fun str(key: String, default: String = ""): String =
            (reply[key] as? LLSD.Str)?.value ?: default
        fun int(key: String, default: Int = 0): Int =
            (reply[key] as? LLSD.Int)?.value ?: default
        fun uuid(key: String): UUID = (reply[key] as? LLSD.Uuid)?.value
            ?: throw IllegalStateException("login reply missing uuid '$key'")

        when (str("login")) {
            "false" -> {
                val reason = str("reason")
                val mfaHash = str("mfa_hash")
                if ((reason == "mfa" || reason == "mfa_challenge") && mfaHash.isNotEmpty()) {
                    _state.value = LoginState.MfaChallenge(
                        mfaHash = mfaHash,
                        message = str("message", "Enter the code from your authenticator app."),
                    )
                } else {
                    _state.value = LoginState.Failed(
                        reason = str("message", "Login failed"),
                        detail = reason.ifEmpty { null },
                    )
                }
            }
            "true" -> {
                val skeletonRoot = (reply["inventory-skeleton"] as? LLSD.Arr)
                    ?.items?.firstOrNull()
                val inventoryRoot = (skeletonRoot as? LLSD.Map)
                    ?.entries?.get("folder_id")?.let { (it as? LLSD.Uuid)?.value } ?: NULL_KEY
                val libraryRoot = ((reply["inventory-lib-root"] as? LLSD.Arr)
                    ?.items?.firstOrNull() as? LLSD.Map)
                    ?.entries?.get("folder_id")?.let { (it as? LLSD.Uuid)?.value } ?: NULL_KEY

                val session = LoginSession(
                    agentId = uuid("agent_id"),
                    sessionId = uuid("session_id"),
                    secureSessionId = uuid("secure_session_id"),
                    circuitCode = int("circuit_code"),
                    simHost = str("sim_ip"),
                    simPort = int("sim_port"),
                    seedCapability = str("seed_capability"),
                    firstName = request.firstName,
                    lastName = request.lastName,
                    inventoryRootFolderId = inventoryRoot,
                    libraryRootFolderId = libraryRoot,
                    regionX = int("region_x"),
                    regionY = int("region_y"),
                )
                // Region bring-up (caps, circuit, event queue) is the
                // session layer's job — §9 — observing this state.
                _state.value = LoginState.EstablishingCircuit(session)
            }
            else -> _state.value = LoginState.Failed("Unexpected login reply")
        }
    }

    private fun buildBody(request: LoginRequest): LLSD {
        val entries = mutableMapOf<String, LLSD>(
            "first" to LLSD.Str(request.firstName),
            "last" to LLSD.Str(request.lastName),
            "passwd" to LLSD.Str(request.credentialToken),
            "start" to LLSD.Str(request.start),
            "channel" to LLSD.Str(request.channel),
            "version" to LLSD.Str(request.version),
            "platform" to LLSD.Str(request.platform),
            "mac" to LLSD.Str(request.mac),
            "id0" to LLSD.Str(request.id0),
            "agree_to_tos" to LLSD.Bool(true),
            "read_critical" to LLSD.Bool(true),
            "options" to llsdArrOf(
                *listOf(
                    "inventory-root", "inventory-skeleton", "inventory-lib-root",
                    "inventory-lib-owner", "inventory-skel-lib", "buddy-list",
                    "gestures", "event_categories", "event_notifications",
                    "classified_categories", "adult_compliant", "newuser-config",
                    "advanced-mode", "max-agent-groups", "map-server-url",
                    "voice-config", "tutorial_setting", "login-flags", "global-textures",
                ).map { LLSD.Str(it) }.toTypedArray(),
            ),
        )
        request.mfaToken?.let { entries["token"] = LLSD.Str(it) }
        request.mfaHash?.let { entries["mfa_hash"] = LLSD.Str(it) }
        return LLSD.Map(entries)
    }
}
```

---

## 9. EventQueueGet coroutine loop + the session layer

`EventQueueGet` is a long-poll: POST `{ack, done=false}`; the
simulator holds the call until events exist, replies `{id, events}`,
and you ack the new `id` on the next poll. Teleport offers, inventory
offers, group notices, and ChatterBox session events ride this queue.
A stalled queue is indistinguishable from a dead session, so the loop
is supervised: backoff on failure, instant teardown on region change
(the cap URL dies with the region), and a best-effort `done=true`
final post.

```kotlin
// app/src/main/java/app/linkpoint/sl/EventQueue.kt
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.llsdMapOf
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

data class EQEvent(val message: String, val body: Map<String, LLSD>)

class EventQueue(
    private val caps: Caps,
    private val scope: CoroutineScope,
) {
    private val _events = MutableSharedFlow<EQEvent>(extraBufferCapacity = 128)
    val events: SharedFlow<EQEvent> = _events.asSharedFlow()

    private var ackId: Int = 0
    private var job: Job? = null
    @Volatile private var running = false

    fun start() {
        if (running) return
        running = true
        job = scope.launch {
            var failures = 0
            while (isActive && running) {
                try {
                    val doc = caps.post(
                        "EventQueueGet",
                        llsdMapOf(
                            "ack" to LLSD.Int(ackId),
                            "done" to LLSD.Bool(false),
                        ),
                    )
                    failures = 0
                    val map = (doc as? LLSD.Map)?.entries ?: continue
                    (map["id"] as? LLSD.Int)?.let { ackId = it.value }
                    val events = (map["events"] as? LLSD.Arr)?.items.orEmpty()
                    for (raw in events) {
                        val ev = (raw as? LLSD.Map)?.entries ?: continue
                        val message = (ev["message"] as? LLSD.Str)?.value ?: continue
                        val body = (ev["body"] as? LLSD.Map)?.entries ?: emptyMap()
                        _events.emit(EQEvent(message, body))
                    }
                } catch (e: Exception) {
                    if (!running) break
                    failures++
                    // Exponential backoff, capped — a dead region cap
                    // must not spin a hot retry loop on a phone battery.
                    val backoff = minOf(30_000L, 1_000L * (1L shl minOf(failures, 5)))
                    delay(backoff)
                }
            }
        }
    }

    fun stop() {
        running = false
        job?.cancel(); job = null
        // Best effort: tell the simulator the queue is done.
        scope.launch {
            try {
                caps.post(
                    "EventQueueGet",
                    llsdMapOf("ack" to LLSD.Int(ackId), "done" to LLSD.Bool(true)),
                )
            } catch (_: Exception) {
                // Region may already be gone; nothing to clean up.
            }
        }
    }
}
```

### 9.1 SessionViewModel: bring-up, handlers, chat/IM state, teardown

```kotlin
// app/src/main/java/app/linkpoint/ui/SessionViewModel.kt
package app.linkpoint.ui

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import app.linkpoint.sl.AgentUpdateLoop
import app.linkpoint.sl.Caps
import app.linkpoint.sl.Circuit
import app.linkpoint.sl.EventQueue
import app.linkpoint.sl.LoginMachine
import app.linkpoint.sl.LoginRequest
import app.linkpoint.sl.LoginSession
import app.linkpoint.sl.LoginState
import app.linkpoint.sl.fetchSimulatorFeatures
import app.linkpoint.sl.messages.ChatFromSimulator
import app.linkpoint.sl.messages.ChatFromViewer
import app.linkpoint.sl.messages.ChatType
import app.linkpoint.sl.messages.CoarseLocationUpdate
import app.linkpoint.sl.messages.CompleteAgentMovement
import app.linkpoint.sl.messages.IMDialog
import app.linkpoint.sl.messages.ImprovedInstantMessage
import app.linkpoint.sl.messages.LogoutRequest
import app.linkpoint.sl.messages.RegionHandshake
import app.linkpoint.sl.messages.RegionHandshakeReply
import app.linkpoint.sl.messages.UseCircuitCode
import app.linkpoint.sl.transport.DatagramSocketTransport
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import java.net.InetSocketAddress
import java.util.UUID

data class ChatLine(
    val atMillis: Long,
    val fromName: String,
    val sourceId: UUID,
    val chatType: Int,
    val message: String,
    val isSystem: Boolean,
)

data class ImLine(val atMillis: Long, val fromId: UUID, val fromName: String, val message: String)

data class ImSessionUi(
    val sessionId: UUID,
    val kind: String, // "dm" | "group" | "conference"
    val title: String,
    val lines: List<ImLine> = emptyList(),
    val unread: Int = 0,
)

data class RadarEntry(val x: Int, val y: Int, val z: Int)

data class SessionUiState(
    val login: LoginState = LoginState.Idle,
    val regionName: String = "",
    val chat: List<ChatLine> = emptyList(),
    val imSessions: Map<String, ImSessionUi> = emptyMap(),
    val activeImSession: String? = null,
    val nearby: List<RadarEntry> = emptyList(),
)

class SessionViewModel(app: Application) : AndroidViewModel(app) {

    private val _ui = MutableStateFlow(SessionUiState())
    val ui: StateFlow<SessionUiState> = _ui.asStateFlow()

    private val http = Caps.httpClient()
    private var loginMachine: LoginMachine? = null
    private var transport: DatagramSocketTransport? = null
    private var circuit: Circuit? = null
    private var eventQueue: EventQueue? = null
    private var agentUpdateLoop: AgentUpdateLoop? = null
    private var session: LoginSession? = null
    private var loginObserver: Job? = null

    fun login(request: LoginRequest) {
        val machine = LoginMachine(http)
        loginMachine = machine
        loginObserver?.cancel()
        loginObserver = viewModelScope.launch {
            machine.state.collect { state ->
                _ui.update { it.copy(login = state) }
                if (state is LoginState.EstablishingCircuit) {
                    bringUpRegion(state.session)
                }
            }
        }
        viewModelScope.launch { machine.login(request) }
    }

    fun submitMfa(code: String) {
        val machine = loginMachine ?: return
        viewModelScope.launch { machine.submitMfa(code) }
    }

    private fun bringUpRegion(sess: LoginSession) {
        session = sess
        viewModelScope.launch {
            try {
                val caps = Caps.negotiate(sess.seedCapability, http)
                // Features are advisory for the UI (voice mode, PBR);
                // a failure here must not block entering the world.
                runCatching { caps.fetchSimulatorFeatures() }

                val udp = DatagramSocketTransport()
                transport = udp
                val circ = Circuit(
                    transport = udp,
                    endpoint = InetSocketAddress(sess.simHost, sess.simPort),
                    scope = viewModelScope,
                )
                circuit = circ
                registerHandlers(circ, sess)
                circ.onDead = {
                    loginMachine?.markFailed("Connection to the region was lost")
                }
                circ.start()
                circ.send(UseCircuitCode(sess.circuitCode, sess.sessionId, sess.agentId))
                circ.send(CompleteAgentMovement(sess.agentId, sess.sessionId, sess.circuitCode))

                val eq = EventQueue(caps, viewModelScope)
                eventQueue = eq
                eq.start()
                viewModelScope.launch {
                    eq.events.collect { ev -> handleEventQueueEvent(ev.message) }
                }

                val loop = AgentUpdateLoop(circ, sess.agentId, sess.sessionId, viewModelScope)
                agentUpdateLoop = loop
                loop.start()
            } catch (e: Exception) {
                loginMachine?.markFailed(e.message ?: "Region bring-up failed")
            }
        }
    }

    private fun registerHandlers(circ: Circuit, sess: LoginSession) {
        circ.on("RegionHandshake") { r ->
            val hs = RegionHandshake.decode(r)
            _ui.update { it.copy(regionName = hs.simName) }
            circ.send(RegionHandshakeReply(sess.agentId, sess.sessionId))
            loginMachine?.markInWorld()
        }
        circ.on("ChatFromSimulator") { r ->
            val chat = ChatFromSimulator.decode(r)
            appendChat(
                ChatLine(
                    atMillis = System.currentTimeMillis(),
                    fromName = chat.fromName,
                    sourceId = chat.sourceId,
                    chatType = chat.chatType,
                    message = chat.message,
                    isSystem = chat.sourceType == 0,
                ),
            )
        }
        circ.on("ImprovedInstantMessage") { r ->
            val im = ImprovedInstantMessage.decode(r)
            if (im.dialog != IMDialog.MESSAGE && im.dialog != IMDialog.BUSY_AUTO_RESPONSE) {
                appendChat(
                    ChatLine(
                        System.currentTimeMillis(), im.fromAgentName, im.agentId,
                        ChatType.NORMAL, "[dialog ${im.dialog}] ${im.message}", isSystem = true,
                    ),
                )
                return@on
            }
            val key = im.imSessionId.toString()
            _ui.update { state ->
                val existing = state.imSessions[key]
                val entry = (existing ?: ImSessionUi(
                    sessionId = im.imSessionId,
                    kind = if (im.fromGroup) "group" else "dm",
                    title = im.fromAgentName,
                )).let { e ->
                    e.copy(
                        lines = e.lines + ImLine(
                            System.currentTimeMillis(), im.agentId, im.fromAgentName, im.message,
                        ),
                        unread = if (state.activeImSession == key) 0 else e.unread + 1,
                    )
                }
                state.copy(imSessions = state.imSessions + (key to entry))
            }
        }
        circ.on("CoarseLocationUpdate") { r ->
            val coarse = CoarseLocationUpdate.decode(r)
            _ui.update {
                it.copy(nearby = coarse.agents.filter { a -> !a.isYou }
                    .map { a -> RadarEntry(a.x, a.y, a.z) })
            }
        }
    }

    private fun handleEventQueueEvent(message: String) {
        // Teleport offers / inventory offers / group notices get typed
        // UI in the full app; the reference behaviour records them as
        // system lines so nothing arrives silently.
        when (message) {
            "TeleportOffered", "OfferInventory", "GroupNotice" -> appendChat(
                ChatLine(
                    System.currentTimeMillis(), "System",
                    UUID(0, 0), ChatType.NORMAL, message, isSystem = true,
                ),
            )
        }
    }

    private fun appendChat(line: ChatLine) {
        _ui.update { it.copy(chat = (it.chat + line).takeLast(500)) }
    }

    fun say(message: String, channel: Int = 0, type: Int = ChatType.NORMAL) {
        val circ = circuit ?: return
        val sess = session ?: return
        circ.sendReliable(ChatFromViewer(sess.agentId, sess.sessionId, message, type, channel))
        if (channel == 0) {
            appendChat(
                ChatLine(
                    System.currentTimeMillis(),
                    "${sess.firstName} ${sess.lastName}",
                    sess.agentId, type, message, isSystem = false,
                ),
            )
        }
    }

    fun sendIm(target: ImSessionUi, message: String) {
        val circ = circuit ?: return
        val sess = session ?: return
        circ.sendReliable(
            ImprovedInstantMessage(
                agentId = sess.agentId, sessionId = sess.sessionId,
                fromGroup = target.kind == "group",
                toAgentId = target.sessionId,
                parentEstateId = 0, regionId = UUID(0, 0),
                position = app.linkpoint.sl.Vector3.ZERO,
                offline = 0, dialog = IMDialog.MESSAGE,
                imSessionId = target.sessionId, timestamp = 0,
                fromAgentName = "${sess.firstName} ${sess.lastName}",
                message = message, binaryBucket = ByteArray(0),
            ),
        )
        val key = target.sessionId.toString()
        _ui.update { state ->
            val entry = state.imSessions[key] ?: return@update state
            state.copy(
                imSessions = state.imSessions + (key to entry.copy(
                    lines = entry.lines + ImLine(
                        System.currentTimeMillis(), sess.agentId,
                        "${sess.firstName} ${sess.lastName}", message,
                    ),
                )),
            )
        }
    }

    fun setActiveImSession(id: String?) {
        _ui.update { state ->
            if (id == null) return@update state.copy(activeImSession = null)
            val entry = state.imSessions[id] ?: return@update state.copy(activeImSession = id)
            state.copy(
                activeImSession = id,
                imSessions = state.imSessions + (id to entry.copy(unread = 0)),
            )
        }
    }

    fun logout() {
        val circ = circuit
        val sess = session
        viewModelScope.launch {
            if (circ != null && sess != null) {
                circ.sendReliable(LogoutRequest(sess.agentId, sess.sessionId))
                delay(150) // let the reliable packet flush before teardown
            }
            teardown()
            _ui.value = SessionUiState()
        }
    }

    private fun teardown() {
        agentUpdateLoop?.stop(); agentUpdateLoop = null
        eventQueue?.stop(); eventQueue = null
        circuit?.close(); circuit = null
        transport?.close(); transport = null
        session = null
    }

    /**
     * Called from the Activity when the app is truly finishing, and
     * from §10's lifecycle handling when the process is being torn
     * down. viewModelScope survives rotation, so onCleared is the
     * right place for socket teardown — NOT onStop.
     */
    override fun onCleared() {
        teardown()
        loginObserver?.cancel()
        super.onCleared()
    }
}
```

---

## 10. Jetpack Compose UI

### 10.1 Login + MFA screens

```kotlin
// app/src/main/java/app/linkpoint/ui/LoginScreen.kt
package app.linkpoint.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import app.linkpoint.sl.LoginState

@Composable
fun LoginScreen(
    state: LoginState,
    onLogin: (first: String, last: String, credentialToken: String) -> Unit,
    onMfa: (code: String) -> Unit,
) {
    when (state) {
        is LoginState.Authenticating, is LoginState.EstablishingCircuit -> {
            Column(Modifier.padding(24.dp)) {
                CircularProgressIndicator()
                Spacer(Modifier.height(12.dp))
                Text(
                    if (state is LoginState.Authenticating) "Authenticating…"
                    else "Connecting to region…",
                )
            }
        }
        is LoginState.MfaChallenge -> MfaPrompt(state, onMfa)
        else -> LoginForm(
            failedReason = (state as? LoginState.Failed)?.reason,
            onLogin = onLogin,
        )
    }
}

@Composable
private fun LoginForm(
    failedReason: String?,
    onLogin: (first: String, last: String, credentialToken: String) -> Unit,
) {
    var first by remember { mutableStateOf("") }
    var last by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }

    Column(Modifier.padding(24.dp)) {
        Text("Second Life", style = MaterialTheme.typography.headlineMedium)
        if (failedReason != null) {
            Spacer(Modifier.height(8.dp))
            Text(failedReason, color = MaterialTheme.colorScheme.error)
        }
        Spacer(Modifier.height(16.dp))
        OutlinedTextField(
            value = first, onValueChange = { first = it },
            label = { Text("First name") },
            singleLine = true,
            modifier = Modifier.fillMaxWidth(),
        )
        OutlinedTextField(
            value = last, onValueChange = { last = it },
            label = { Text("Last name") },
            singleLine = true,
            modifier = Modifier.fillMaxWidth(),
        )
        OutlinedTextField(
            value = password, onValueChange = { password = it },
            label = { Text("Password") },
            singleLine = true,
            visualTransformation = PasswordVisualTransformation(),
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password),
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(Modifier.height(16.dp))
        Button(
            onClick = {
                // Token derivation lives in the platform layer and the
                // raw password is dropped immediately after this call.
                onLogin(first.trim(), last.trim().ifEmpty { "Resident" }, deriveCredentialToken(password))
                password = ""
            },
            enabled = first.isNotBlank() && password.isNotEmpty(),
            modifier = Modifier.fillMaxWidth(),
        ) { Text("Log in") }
    }
}

@Composable
private fun MfaPrompt(state: LoginState.MfaChallenge, onMfa: (String) -> Unit) {
    var code by remember { mutableStateOf("") }
    Column(Modifier.padding(24.dp)) {
        Text("Two-factor authentication", style = MaterialTheme.typography.headlineSmall)
        Spacer(Modifier.height(8.dp))
        Text(state.message)
        Spacer(Modifier.height(16.dp))
        OutlinedTextField(
            value = code, onValueChange = { code = it.filter { c -> c.isDigit() } },
            label = { Text("Authenticator code") },
            singleLine = true,
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(Modifier.height(16.dp))
        Button(
            onClick = { onMfa(code) },
            enabled = code.length >= 6,
            modifier = Modifier.fillMaxWidth(),
        ) { Text("Verify") }
        // No "trust this device" checkbox in the reference build: the
        // mfa_hash stays in memory only (§8), so there is nothing to
        // persist even if the user asks. Add the checkbox ONLY together
        // with an EncryptedFile/Keystore-backed store for the hash.
    }
}

/** Legacy "$1$"+md5 token. Isolated: grid credential policy changes land here. */
fun deriveCredentialToken(password: String): String {
    val digest = java.security.MessageDigest.getInstance("MD5")
        .digest(password.toByteArray(Charsets.UTF_8))
    return "\$1\$" + digest.joinToString("") { "%02x".format(it) }
}
```

### 10.2 Chat screen

```kotlin
// app/src/main/java/app/linkpoint/ui/ChatScreen.kt
package app.linkpoint.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import app.linkpoint.sl.messages.ChatType

@Composable
fun ChatScreen(
    chat: List<ChatLine>,
    onSay: (message: String, channel: Int) -> Unit,
) {
    var draft by remember { mutableStateOf("") }
    val listState = rememberLazyListState()

    // Keep the newest line visible — chat is append-mostly.
    LaunchedEffect(chat.size) {
        if (chat.isNotEmpty()) listState.animateScrollToItem(chat.size - 1)
    }

    Column(Modifier.fillMaxSize()) {
        LazyColumn(
            state = listState,
            modifier = Modifier.weight(1f).fillMaxWidth().padding(12.dp),
        ) {
            items(chat, key = { it.atMillis to it.message.hashCode() }) { line ->
                Text(
                    buildAnnotatedString {
                        val label = when (line.chatType) {
                            ChatType.SHOUT -> "${line.fromName} shouts"
                            ChatType.WHISPER -> "${line.fromName} whispers"
                            else -> line.fromName
                        }
                        withStyle(SpanStyle(fontWeight = FontWeight.SemiBold)) {
                            append("$label: ")
                        }
                        append(line.message)
                    },
                    modifier = Modifier.padding(vertical = 2.dp),
                )
            }
        }
        Row(Modifier.fillMaxWidth().padding(8.dp)) {
            OutlinedTextField(
                value = draft,
                onValueChange = { draft = it },
                placeholder = { Text("Say something…  (/5 = channel 5)") },
                singleLine = true,
                modifier = Modifier.weight(1f),
            )
            Button(
                onClick = {
                    val text = draft.trim()
                    if (text.isEmpty()) return@Button
                    // Viewer syntax: "/5 hello" sends on channel 5 —
                    // how mobile users drive HUDs and scripted menus.
                    val match = Regex("""^(-?\d+)\s+(.*)""", RegexOption.DOT_MATCHES_ALL)
                        .matchEntire(text.removePrefix("/"))
                    if (text.startsWith("/") && match != null) {
                        onSay(match.groupValues[2], match.groupValues[1].toInt())
                    } else {
                        onSay(text, 0)
                    }
                    draft = ""
                },
                modifier = Modifier.padding(start = 8.dp),
            ) { Text("Send") }
        }
    }
}
```

### 10.3 Inventory screen (lazy tree)

```kotlin
// app/src/main/java/app/linkpoint/ui/InventoryScreen.kt
package app.linkpoint.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import app.linkpoint.sl.AssetType
import app.linkpoint.sl.Caps
import app.linkpoint.sl.FolderContents
import app.linkpoint.sl.InventoryFolder
import app.linkpoint.sl.InventoryItem
import app.linkpoint.sl.fetchFolder
import kotlinx.coroutines.launch
import java.util.UUID

/**
 * Lazy inventory tree. Each folder fetches on first expand and caches
 * by (folderId -> contents with version). Refetch only when the
 * simulator-side version advances — the ViewModel owns version
 * tracking on inventory-offer / AIS events; this composable owns only
 * expansion and display state.
 */
@Composable
fun InventoryScreen(
    caps: Caps?,
    agentId: UUID?,
    rootFolderId: UUID?,
    onItemClick: (InventoryItem) -> Unit = {},
) {
    if (caps == null || agentId == null || rootFolderId == null) {
        Text("Not logged in.", Modifier.padding(16.dp))
        return
    }
    val root = remember(rootFolderId) {
        InventoryFolder(rootFolderId, rootFolderId, "My Inventory", -1, 0)
    }
    Column(
        Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(8.dp),
    ) {
        FolderNode(caps, agentId, root, depth = 0, startExpanded = true, onItemClick)
    }
}

@Composable
private fun FolderNode(
    caps: Caps,
    agentId: UUID,
    folder: InventoryFolder,
    depth: Int,
    startExpanded: Boolean = false,
    onItemClick: (InventoryItem) -> Unit,
) {
    var expanded by remember(folder.folderId) { mutableStateOf(startExpanded) }
    var contents by remember(folder.folderId) { mutableStateOf<FolderContents?>(null) }
    var loading by remember(folder.folderId) { mutableStateOf(false) }
    var error by remember(folder.folderId) { mutableStateOf<String?>(null) }
    val scope = rememberCoroutineScope()

    fun load() {
        if (loading || contents != null) return
        loading = true
        scope.launch {
            try {
                contents = caps.fetchFolder(agentId, folder.folderId)
            } catch (e: Exception) {
                error = e.message ?: "Fetch failed"
            } finally {
                loading = false
            }
        }
    }

    LaunchedEffect(folder.folderId, startExpanded) {
        if (startExpanded) load()
    }

    Column(Modifier.padding(start = (depth * 14).dp)) {
        Row(
            Modifier.clickable {
                expanded = !expanded
                if (expanded) load()
            }.padding(vertical = 4.dp),
        ) {
            Text(if (expanded) "▾ " else "▸ ", fontWeight = FontWeight.Bold)
            Text("📁 ${folder.name}", fontWeight = FontWeight.SemiBold)
            if (loading) CircularProgressIndicator(Modifier.padding(start = 8.dp))
        }
        error?.let { Text(it, color = Color.Red) }
        if (expanded) {
            contents?.folders?.forEach { child ->
                FolderNode(caps, agentId, child, depth + 1, false, onItemClick)
            }
            contents?.items?.forEach { item ->
                Text(
                    "  ${iconFor(item.assetType)} ${item.name}${if (item.isLink) " (link)" else ""}",
                    Modifier.clickable { onItemClick(item) }.padding(vertical = 2.dp),
                )
            }
            if (contents != null && contents!!.folders.isEmpty() && contents!!.items.isEmpty()) {
                Text("  (empty)", color = Color.Gray)
            }
        }
    }
}

private fun iconFor(type: AssetType): String = when (type) {
    AssetType.TEXTURE, AssetType.TEXTURE_TGA, AssetType.SNAPSHOT -> "🖼"
    AssetType.SOUND, AssetType.SOUND_WAV -> "🔊"
    AssetType.LANDMARK -> "📍"
    AssetType.NOTECARD -> "📝"
    AssetType.SCRIPT -> "📜"
    AssetType.OBJECT -> "📦"
    AssetType.CLOTHING, AssetType.WEARABLE, AssetType.BODYPART -> "👕"
    AssetType.ANIMATION -> "🕺"
    AssetType.GESTURE -> "✋"
    AssetType.MESH -> "🧊"
    AssetType.MATERIAL -> "🎨"
    else -> "•"
}
```

### 10.4 App activity + navigation shell

```kotlin
// app/src/main/java/app/linkpoint/MainActivity.kt
package app.linkpoint

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import app.linkpoint.sl.LoginRequest
import app.linkpoint.sl.LoginState
import app.linkpoint.ui.ChatScreen
import app.linkpoint.ui.InventoryScreen
import app.linkpoint.ui.LoginScreen
import app.linkpoint.ui.SessionViewModel

class MainActivity : ComponentActivity() {
    private val viewModel: SessionViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val ui by viewModel.ui.collectAsState()
            if (ui.login !is LoginState.InWorld && ui.login !is LoginState.EstablishingCircuit) {
                LoginScreen(
                    state = ui.login,
                    onLogin = { first, last, token ->
                        viewModel.login(
                            LoginRequest(
                                firstName = first,
                                lastName = last,
                                credentialToken = token,
                                start = "last",
                                channel = "Linkpoint Kotlin Reference",
                                version = "1.0.0",
                                platform = "and",
                                mac = deviceMacPlaceholder(),
                                id0 = deviceId0Placeholder(),
                            ),
                        )
                    },
                    onMfa = { code -> viewModel.submitMfa(code) },
                )
            } else {
                SessionShell(viewModel)
            }
        }
    }

    // Real builds read these from device identity providers; they must
    // be stable per install (the login service uses them for account
    // security heuristics) — random-per-launch values cause lockouts.
    private fun deviceMacPlaceholder(): String = "00:00:00:00:00:00"
    private fun deviceId0Placeholder(): String = "reference-build"
}

@Composable
private fun SessionShell(viewModel: SessionViewModel) {
    val ui by viewModel.ui.collectAsState()
    var tab by remember { mutableStateOf("chat") }
    val sessionCapsNote = "Caps live in the ViewModel session layer; " +
        "the inventory tab receives them via ui state in the full app."

    Column(Modifier.fillMaxSize()) {
        Row(Modifier.fillMaxWidth().padding(8.dp)) {
            Text(
                ui.regionName.ifEmpty { "Connecting…" },
                fontWeight = FontWeight.Bold,
                modifier = Modifier.weight(1f),
            )
            TextButton(onClick = { viewModel.logout() }) { Text("Log out") }
        }
        Column(Modifier.weight(1f)) {
            when (tab) {
                "chat" -> ChatScreen(
                    chat = ui.chat,
                    onSay = { message, channel -> viewModel.say(message, channel) },
                )
                "inventory" -> Text(
                    "Inventory tab: wire Caps + agent + root folder from " +
                        "the session layer into InventoryScreen. $sessionCapsNote",
                    Modifier.padding(16.dp),
                )
                "people" -> Text(
                    "Nearby (radar cells): " +
                        ui.nearby.joinToString { "(${it.x}, ${it.y})" }
                            .ifEmpty { "no one else in region" },
                    Modifier.padding(16.dp),
                )
            }
        }
        Row(Modifier.fillMaxWidth().padding(8.dp)) {
            Button(onClick = { tab = "chat" }, modifier = Modifier.weight(1f)) { Text("Chat") }
            Button(onClick = { tab = "people" }, modifier = Modifier.weight(1f)) { Text("People") }
            Button(onClick = { tab = "inventory" }, modifier = Modifier.weight(1f)) { Text("Inventory") }
        }
    }
}
```

---

## 11. Android lifecycle handling for the circuit

The circuit is a *process-lifetime* resource with *session-lifetime*
semantics. The rules that keep it correct:

1. **Rotation must not kill the session.** The circuit lives in the
   `ViewModel` (survives configuration change), never in an Activity
   or a composable. `remember` is for UI state only.
2. **`onStop` must not log you out.** Users switch apps to answer a
   message; the simulator's agent timeout is on the order of a minute
   or more of total silence, and `AgentUpdate` + ping handling keep
   the agent present while the process lives.
3. **Background execution limits are real.** From Android 8+, a
   backgrounded app's sockets keep working only while the process is
   cached; under Doze, network is batched and the circuit WILL stall.
   For a viewer expected to stay logged in while backgrounded, run a
   foreground service with a persistent "Logged in as …" notification
   (§11.2). Without it, treat long backgrounding as a probable
   disconnect and re-login on resume (§11.3).
4. **Process death is a logout.** If the OS kills the process, the
   simulator times the agent out on its own. On next launch, log in
   fresh — never try to resurrect a circuit code from disk.

### 11.1 Network change handling

Wi-Fi → cellular switches change the source address; the simulator
sees packets from a new endpoint and the old circuit is dead even
though your socket "works". Detect, tear down, and re-login.

```kotlin
// app/src/main/java/app/linkpoint/sl/NetworkWatcher.kt
package app.linkpoint.sl

import android.content.Context
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

/**
 * Emits a monotonically increasing "network generation" every time the
 * default network changes identity. The session layer compares the
 * generation at circuit-open time with the current one: a change means
 * the circuit's source endpoint changed under it.
 */
class NetworkWatcher(context: Context) {
    private val cm = context.getSystemService(ConnectivityManager::class.java)
    private val _generation = MutableStateFlow(0)
    val generation: StateFlow<Int> = _generation.asStateFlow()
    private var currentNetwork: Network? = null

    private val callback = object : ConnectivityManager.NetworkCallback() {
        override fun onAvailable(network: Network) {
            if (currentNetwork != null && currentNetwork != network) {
                _generation.value += 1
            }
            currentNetwork = network
        }
        override fun onLost(network: Network) {
            if (network == currentNetwork) {
                _generation.value += 1
                currentNetwork = null
            }
        }
    }

    fun start() {
        val request = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()
        cm.registerNetworkCallback(request, callback)
    }

    fun stop() {
        runCatching { cm.unregisterNetworkCallback(callback) }
    }
}
```

```kotlin
// Session-layer integration (add to SessionViewModel):
//
// private var circuitNetworkGeneration: Int = -1
//
// // In bringUpRegion():
// circuitNetworkGeneration = networkWatcher.generation.value
//
// // Observed alongside login state:
// viewModelScope.launch {
//     networkWatcher.generation.collect { gen ->
//         if (session != null && circuitNetworkGeneration >= 0 && gen != circuitNetworkGeneration) {
//             // Source endpoint changed: the simulator will not accept
//             // the old circuit from the new address. Clean teardown +
//             // back to Idle with a visible reason beats ghosting.
//             teardown()
//             loginMachine?.markFailed(
//                 "Network changed — please log in again"
//             )
//             _ui.update { it.copy(login = LoginState.Failed("Network changed")) }
//         }
//     }
// }
```

### 11.2 Foreground service for background presence

```kotlin
// app/src/main/java/app/linkpoint/service/SessionService.kt
package app.linkpoint.service

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Intent
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.IBinder
import androidx.core.app.NotificationCompat
import app.linkpoint.MainActivity
import android.app.PendingIntent

/**
 * Keeps the process (and therefore the ViewModel's circuit) alive
 * while the user is logged in and the app is backgrounded. The service
 * owns NOTHING protocol-shaped — it is a lifecycle shell around the
 * process. Start it on InWorld, stop it on logout.
 */
class SessionService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val channelId = "sl-session"
        val nm = getSystemService(NotificationManager::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            nm.createNotificationChannel(
                NotificationChannel(channelId, "Session", NotificationManager.IMPORTANCE_LOW),
            )
        }
        val openApp = PendingIntent.getActivity(
            this, 0, Intent(this, MainActivity::class.java),
            PendingIntent.FLAG_IMMUTABLE,
        )
        val notification: Notification = NotificationCompat.Builder(this, channelId)
            .setContentTitle("Second Life")
            .setContentText("Logged in — tap to return")
            .setSmallIcon(android.R.drawable.ic_dialog_info)
            .setContentIntent(openApp)
            .setOngoing(true)
            .build()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
            startForeground(
                1, notification,
                ServiceInfo.FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE,
            )
        } else {
            startForeground(1, notification)
        }
        return START_STICKY
    }
}
```

### 11.3 Resume policy

```kotlin
// Resume decision table, implemented in the Activity's onResume ->
// ViewModel.onAppResumed(backgroundedForMs):
//
//  background < 30 s   -> do nothing; circuit timers kept running.
//  30 s .. 5 min       -> send a StartPingCheck-triggering probe: in
//                         practice, force one AgentUpdate + watch the
//                         reliable queue; if a reliable test message
//                         (e.g. a ChatFromViewer to a script channel)
//                         exhausts resends, Circuit.onDead fires and
//                         the UI shows the disconnect.
//  > 5 min, no FGS     -> assume dead: teardown + Idle with reason
//                         "Session timed out while the app was closed".
//  any, FGS running    -> trust onDead / network-generation signals
//                         only; Android kept the process schedulable.
//
// The asymmetry is deliberate: a false "still connected" (ghost avatar,
// missed IMs, stuck teleport) is worse for the user than a false
// "please log in again".
```

---

## 12. Teleport flow

Teleport crosses both planes: initiated over caps/UDP, progressed by
`TeleportStart` / `TeleportProgress`, and finished by
`TeleportFinish`, which carries the *new* region's seed capability,
sim IP/port, and circuit details. On finish you must, in order:

1. Stop the AgentUpdate loop and the event queue (old cap dies here).
2. Close the old circuit (after sending nothing more on it).
3. Negotiate caps from the new seed.
4. Open a new circuit to the new endpoint, `UseCircuitCode` +
   `CompleteAgentMovement`, await `RegionHandshake`, reply, restart
   the event queue and AgentUpdate loop.

```kotlin
// app/src/main/java/app/linkpoint/sl/Teleport.kt (session-layer sketch)
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.llsdMapOf

/** Ask the current region to teleport us to a landmark / location.
 *  The request goes through the TeleportLocationRequest-style cap
 *  flow where available and falls back to the viewer's UDP path on
 *  grids without it; progress arrives as UDP Teleport* messages
 *  handled by the session layer, NOT here. */
suspend fun Caps.requestTeleportTo(
    agentId: java.util.UUID,
    regionHandle: Long,
    position: Vector3,
    lookAt: Vector3,
) {
    // Region handles pack the global region coordinates: high 32 bits
    // are x * 256, low 32 bits are y * 256 (metres at region scale).
    post(
        "TeleportLocationRequest",
        llsdMapOf(
            "agent_id" to LLSD.Uuid(agentId),
            "region_handle" to LLSD.Str(regionHandle.toString()),
            "position" to LLSD.Arr(listOf(
                LLSD.Real(position.x.toDouble()),
                LLSD.Real(position.y.toDouble()),
                LLSD.Real(position.z.toDouble()),
            )),
            "look_at" to LLSD.Arr(listOf(
                LLSD.Real(lookAt.x.toDouble()),
                LLSD.Real(lookAt.y.toDouble()),
                LLSD.Real(lookAt.z.toDouble()),
            )),
        ),
    )
}

/** Decode a TeleportFinish body. Field order per the template's
 *  Info block: agent/session, location, look-at, seed cap, sim IP/port,
 *  teleport flags. The session layer feeds this into the same
 *  bring-up path as login (§9.1) with a fresh LoginSession. */
data class TeleportFinishInfo(
    val seedCapability: String,
    val simHost: String,
    val simPort: Int,
    val regionHandle: Long,
    val teleportFlags: Int,
)

fun decodeTeleportFinish(r: PacketReader): TeleportFinishInfo {
    // AgentData block
    r.uuid(); r.uuid()
    // Info block
    val seed = r.stringVar2()
    val simIp = r.u32()
    val simPort = r.u16()
    val regionHandle = r.u64()
    val flags = r.u32()
    val host = listOf(
        simIp and 0xFF, (simIp ushr 8) and 0xFF,
        (simIp ushr 16) and 0xFF, (simIp ushr 24) and 0xFF,
    ).joinToString(".")
    return TeleportFinishInfo(seed, host, simPort, regionHandle, flags)
}
```

---

## 13. Tests

```kotlin
// app/src/test/java/app/linkpoint/sl/PacketTest.kt
package app.linkpoint.sl

import app.linkpoint.sl.llsd.LLSD
import app.linkpoint.sl.llsd.LLSDBinary
import app.linkpoint.sl.llsd.LLSDXml
import app.linkpoint.sl.messages.ChatFromViewer
import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import java.util.UUID

class PacketTest {
    @Test
    fun zerocodeRoundTrip() {
        val body = byteArrayOf(1, 0, 0, 0, 2, 0, 3)
        assertArrayEquals(body, ZeroCode.decode(ZeroCode.encode(body)))
    }

    @Test
    fun zerocodeSingleZero() {
        assertArrayEquals(byteArrayOf(0, 1), ZeroCode.encode(byteArrayOf(0)))
    }

    @Test
    fun chatPacketIsNotZerocoded() {
        val id = UUID.fromString("11111111-2222-3333-4444-555555555555")
        val body = ChatFromViewer(id, id, "hello", 1, 0).encode()
        val packet = encodePacket(
            sequence = 7, body = body, zerocoded = false, reliable = true,
        )
        val decoded = decodePacket(packet)
        assertEquals(7, decoded.sequence)
        assertTrue(decoded.reliable)
        assertEquals(false, decoded.zerocoded)
    }

    @Test
    fun llsdIntegerAndRealStayDistinctInBinary() {
        val doc = LLSD.Map(mapOf("count" to LLSD.Int(1), "ratio" to LLSD.Real(1.0)))
        val back = LLSDBinary.parse(LLSDBinary.write(doc)) as LLSD.Map
        assertTrue(back.entries["count"] is LLSD.Int)
        assertTrue(back.entries["ratio"] is LLSD.Real)
    }

    @Test
    fun llsdXmlRoundTrip() {
        val doc = LLSD.Map(
            mapOf(
                "agent_id" to LLSD.Uuid(UUID.fromString("12345678-1234-1234-1234-123456789012")),
                "name" to LLSD.Str("a & b <test>"),
                "items" to LLSD.Arr(listOf(LLSD.Int(3), LLSD.Bool(true))),
            ),
        )
        assertEquals(doc, LLSDXml.parse(LLSDXml.write(doc)))
    }
}
```

```kotlin
// app/src/test/java/app/linkpoint/sl/CircuitTest.kt (sketch)
// A fake UdpTransport that records sent packets and injects inbound
// ones makes the circuit fully testable without a simulator — this is
// also how you test against OpenSim: swap the fake for a real
// transport pointed at a localhost standalone instance and drive the
// same script of assertions at integration level.
package app.linkpoint.sl

import app.linkpoint.sl.transport.UdpTransport
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableSharedFlow
import java.net.InetSocketAddress

class FakeTransport : UdpTransport {
    val sent = mutableListOf<Pair<InetSocketAddress, ByteArray>>()
    val inbound = MutableSharedFlow<Pair<InetSocketAddress, ByteArray>>()

    override suspend fun send(to: InetSocketAddress, packet: ByteArray) {
        sent += to to packet.copyOf()
    }
    override fun packets(): Flow<Pair<InetSocketAddress, ByteArray>> = inbound
    override fun close() {}
}
```

---

## 14. What this file leaves to the app layer

- **Rendering.** GLES/Vulkan scene rendering (Lumiya's renderer is
  the reference) consumes `ObjectUpdate`-family decodes and the mesh /
  texture fetchers in §7.2. The decode pattern is §5's; the scene
  graph is its own subsystem — see the viewer-internals guide.
- **Full LLMesh parsing.** Behind the `fetchMesh` seam in §7.2; port
  from LibreMetaverse MeshFoundry semantics.
- **Voice.** WebRTC on current grids (negotiate via caps/features,
  then a platform WebRTC client); Vivox only for legacy grids, via
  its native SDK in a separate module — Lumiya shipped it as a
  plugin APK for exactly this isolation.
- **Generated messages beyond the core set.** §5 is the contract the
  generator must reproduce; generate the remaining ~450 messages from
  the template at build time and diff the output against §5.

---

*End of the Kotlin/Android file. Companion: `code-react-typescript.md`
implements the same protocol core for React / React Native targets.*
