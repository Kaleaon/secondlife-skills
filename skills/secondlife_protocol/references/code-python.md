# Second Life in Python — LLSD, Zerocode, UDP Circuit, Caps, Login, and Bots

Canonical sources this file is built from:

- `secondlife/python-llsd` and `secondlife/python-llbase` (MIT) — the reference Python LLSD semantics. This file hand-rolls the same codec so the format is visible end to end; in production, prefer `llbase.llsd` where it is available.
- `secondlife/viewer` — `indra/llcommon/llsdserialize.cpp` (C++ twin of the Python codec, useful as a second vote on edge cases) and `indra/llmessage/` (circuit, zerocode, reliability).
- `secondlife/master-message-template` — `message_template.msg`, the data file the template parser in section 4 consumes.
- `cinderblocks/libremetaverse` — `LibreMetaverse.StructuredData` (BSD-3) for LLSD semantics in a third implementation, and its TestClient as the model for the bot in section 7.
- Historical only: `pyogp` (Python 2, Apache-2.0, dead) — its message-template parser and Event Queue code are good teaching material, but its OGP login flow is **not** production login. Nothing here uses pyogp code.

Conventions: Python 3.11+, `asyncio` for the circuit, `httpx` for caps and login. All grid traffic in the examples targets a local OpenSim standalone or Aditi unless you change the login URI — test there before Agni.

---

## 1. LLSD value model

LLSD has exactly ten types. Every codec below maps them to Python types the same way `llbase.llsd` does:

| LLSD type | Python type | Notes |
|---|---|---|
| undefined | `None` | Serialises as an empty element / `!` in notation |
| boolean | `bool` | Check `bool` **before** `int` — `bool` subclasses `int` in Python |
| integer | `int` | **32-bit signed on the wire.** Clamp or raise outside -2^31..2^31-1 |
| real | `float` | Double precision |
| string | `str` | UTF-8 |
| binary | `bytes` | Base64 in XML, raw length-prefixed in binary |
| UUID | `uuid.UUID` | 16 bytes in binary, hyphenated string in XML |
| date | `datetime` (aware, UTC) | Seconds since epoch as a double in binary |
| URI | `str` (wrapped below) | Kept distinct so round-trips preserve the type |
| array | `list` / `tuple` | |
| map | `dict` with `str` keys | Keys are always strings |

```python
"""llsd_codec.py — a hand-rolled LLSD codec (XML, binary, notation).

Kept deliberately close to llbase.llsd semantics so test vectors can be
diffed against the canonical library. Where this codec and llbase disagree,
llbase (and the viewer's llsdserialize.cpp) win — file a bug here.
"""
from __future__ import annotations

import base64
import math
import re
import struct
import uuid
from datetime import datetime, timezone
from xml.etree import ElementTree as ET

LLSD_INT_MIN = -(2 ** 31)
LLSD_INT_MAX = 2 ** 31 - 1


class URI(str):
    """An LLSD URI. A str subclass so it behaves like a string everywhere,
    but the codecs can still tell it apart from a plain LLSD string."""


class LLSDParseError(ValueError):
    """Raised for any malformed LLSD input. Never let a bare struct.error
    or binascii.Error escape a codec: callers treat LLSDParseError as
    'the simulator / cap endpoint sent garbage', which is a session-level
    event, not a programming error."""


def _check_int(value: int) -> int:
    if not (LLSD_INT_MIN <= value <= LLSD_INT_MAX):
        raise LLSDParseError(
            f"LLSD integer {value} outside 32-bit range. LLSD integers are "
            "32-bit; a Python int is unbounded, so this is the single most "
            "common silent-corruption bug when porting LLSD to Python."
        )
    return value


def _datetime_to_seconds(value: datetime) -> float:
    if value.tzinfo is None:
        # LLSD dates are UTC. A naive datetime is a caller bug; assume UTC
        # (matching llbase) but this is worth a warning in real code.
        value = value.replace(tzinfo=timezone.utc)
    return value.timestamp()


def _seconds_to_datetime(seconds: float) -> datetime:
    return datetime.fromtimestamp(seconds, tz=timezone.utc)
```

### 1.1 XML serialisation

XML LLSD is the wire format for most caps responses (`application/llsd+xml`). Element names are the type names; a `<map>` alternates `<key>` and value elements.

```python
def format_xml(value) -> bytes:
    """Serialise a Python value to XML LLSD bytes."""
    root = ET.Element("llsd")
    _xml_append(root, value)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def _xml_append(parent: ET.Element, value) -> None:
    if value is None:
        ET.SubElement(parent, "undef")
    elif isinstance(value, bool):  # before int!
        el = ET.SubElement(parent, "boolean")
        el.text = "1" if value else "0"
    elif isinstance(value, URI):
        el = ET.SubElement(parent, "uri")
        el.text = str(value)
    elif isinstance(value, int):
        el = ET.SubElement(parent, "integer")
        el.text = str(_check_int(value))
    elif isinstance(value, float):
        el = ET.SubElement(parent, "real")
        el.text = _format_real(value)
    elif isinstance(value, uuid.UUID):
        el = ET.SubElement(parent, "uuid")
        el.text = str(value)
    elif isinstance(value, (bytes, bytearray)):
        el = ET.SubElement(parent, "binary")
        el.text = base64.b64encode(bytes(value)).decode("ascii")
    elif isinstance(value, datetime):
        el = ET.SubElement(parent, "date")
        el.text = value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    elif isinstance(value, str):
        el = ET.SubElement(parent, "string")
        el.text = value
    elif isinstance(value, (list, tuple)):
        el = ET.SubElement(parent, "array")
        for item in value:
            _xml_append(el, item)
    elif isinstance(value, dict):
        el = ET.SubElement(parent, "map")
        for key, item in value.items():
            k = ET.SubElement(el, "key")
            k.text = str(key)
            _xml_append(el, item)
    else:
        raise TypeError(f"Cannot LLSD-serialise {type(value)!r}")


def _format_real(value: float) -> str:
    # The viewer writes nan/inf spellings explicitly; Python's repr would
    # produce 'nan'/'inf' which the C++ parser also accepts, but matching
    # llbase's spellings keeps diff-based debugging sane.
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return repr(value)
```

### 1.2 XML parsing

```python
def parse_xml(data: bytes):
    """Parse XML LLSD bytes back into Python values."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise LLSDParseError(f"Malformed XML LLSD: {exc}") from exc
    if root.tag != "llsd":
        raise LLSDParseError(f"Expected <llsd> root, got <{root.tag}>")
    children = list(root)
    if not children:
        return None  # <llsd/> is undefined
    if len(children) > 1:
        raise LLSDParseError("LLSD document has more than one top-level value")
    return _xml_read(children[0])


def _xml_read(el: ET.Element):
    tag = el.tag
    if tag == "undef":
        return None
    if tag == "boolean":
        return (el.text or "").strip() in ("1", "true")
    if tag == "integer":
        return _check_int(int((el.text or "0").strip()))
    if tag == "real":
        return float((el.text or "0").strip())
    if tag == "string":
        return el.text or ""
    if tag == "uri":
        return URI(el.text or "")
    if tag == "uuid":
        text = (el.text or "").strip()
        return uuid.UUID(text) if text else uuid.UUID(int=0)
    if tag == "binary":
        # XML binary is base64. Whitespace inside is legal in the wild.
        return base64.b64decode(re.sub(r"\s+", "", el.text or ""))
    if tag == "date":
        text = (el.text or "").strip()
        dt = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
        return dt.replace(tzinfo=timezone.utc)
    if tag == "array":
        return [_xml_read(child) for child in el]
    if tag == "map":
        result = {}
        kids = list(el)
        if len(kids) % 2:
            raise LLSDParseError("<map> with an odd number of children")
        for i in range(0, len(kids), 2):
            if kids[i].tag != "key":
                raise LLSDParseError("<map> child is not a <key>")
            result[kids[i].text or ""] = _xml_read(kids[i + 1])
        return result
    raise LLSDParseError(f"Unknown LLSD element <{tag}>")
```

### 1.3 Binary serialisation

Binary LLSD prefixes every value with a one-byte type marker. All integers are big-endian. Strings, binary, URIs, keys, arrays, and maps are length-prefixed with a 32-bit count (bytes for blobs, elements for containers).

```python
# Type markers, from llsdserialize.cpp / llbase.llsd — do not invent your own.
_B_UNDEF = b"!"
_B_TRUE = b"T"
_B_FALSE = b"F"
_B_INT = b"i"
_B_REAL = b"r"
_B_UUID = b"u"
_B_STR = b"s"
_B_BIN = b"b"
_B_URI = b"l"   # 'l' for link
_B_DATE = b"d"
_B_ARRAY_OPEN, _B_ARRAY_CLOSE = b"[", b"]"
_B_MAP_OPEN, _B_MAP_CLOSE = b"{", b"}"
_B_KEY = b"k"


def format_binary(value) -> bytes:
    out = bytearray()
    _binary_append(out, value)
    return bytes(out)


def _binary_append(out: bytearray, value) -> None:
    if value is None:
        out += _B_UNDEF
    elif isinstance(value, bool):
        out += _B_TRUE if value else _B_FALSE
    elif isinstance(value, URI):
        raw = str(value).encode("utf-8")
        out += _B_URI + struct.pack(">I", len(raw)) + raw
    elif isinstance(value, int):
        out += _B_INT + struct.pack(">i", _check_int(value))
    elif isinstance(value, float):
        out += _B_REAL + struct.pack(">d", value)
    elif isinstance(value, uuid.UUID):
        out += _B_UUID + value.bytes
    elif isinstance(value, (bytes, bytearray)):
        out += _B_BIN + struct.pack(">I", len(value)) + bytes(value)
    elif isinstance(value, datetime):
        out += _B_DATE + struct.pack(">d", _datetime_to_seconds(value))
    elif isinstance(value, str):
        raw = value.encode("utf-8")
        out += _B_STR + struct.pack(">I", len(raw)) + raw
    elif isinstance(value, (list, tuple)):
        out += _B_ARRAY_OPEN + struct.pack(">I", len(value))
        for item in value:
            _binary_append(out, item)
        out += _B_ARRAY_CLOSE
    elif isinstance(value, dict):
        out += _B_MAP_OPEN + struct.pack(">I", len(value))
        for key, item in value.items():
            raw = str(key).encode("utf-8")
            out += _B_KEY + struct.pack(">I", len(raw)) + raw
            _binary_append(out, item)
        out += _B_MAP_CLOSE
    else:
        raise TypeError(f"Cannot LLSD-serialise {type(value)!r}")


class _BinaryReader:
    """Cursor over a bytes buffer. Every read is bounds-checked so a
    truncated cap response raises LLSDParseError, not struct.error."""

    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def take(self, n: int) -> bytes:
        if self.pos + n > len(self.data):
            raise LLSDParseError("Binary LLSD truncated")
        chunk = self.data[self.pos:self.pos + n]
        self.pos += n
        return chunk

    def byte(self) -> bytes:
        return self.take(1)

    def u32(self) -> int:
        return struct.unpack(">I", self.take(4))[0]

    def read_value(self):
        marker = self.byte()
        if marker == _B_UNDEF:
            return None
        if marker == _B_TRUE:
            return True
        if marker == _B_FALSE:
            return False
        if marker == _B_INT:
            return struct.unpack(">i", self.take(4))[0]
        if marker == _B_REAL:
            return struct.unpack(">d", self.take(8))[0]
        if marker == _B_UUID:
            return uuid.UUID(bytes=self.take(16))
        if marker == _B_STR:
            return self.take(self.u32()).decode("utf-8")
        if marker == _B_URI:
            return URI(self.take(self.u32()).decode("utf-8"))
        if marker == _B_BIN:
            return self.take(self.u32())
        if marker == _B_DATE:
            return _seconds_to_datetime(struct.unpack(">d", self.take(8))[0])
        if marker == _B_ARRAY_OPEN:
            count = self.u32()
            items = [self.read_value() for _ in range(count)]
            if self.byte() != _B_ARRAY_CLOSE:
                raise LLSDParseError("Binary LLSD array missing ']'")
            return items
        if marker == _B_MAP_OPEN:
            count = self.u32()
            result = {}
            for _ in range(count):
                if self.byte() != _B_KEY:
                    raise LLSDParseError("Binary LLSD map key missing 'k'")
                key = self.take(self.u32()).decode("utf-8")
                result[key] = self.read_value()
            if self.byte() != _B_MAP_CLOSE:
                raise LLSDParseError("Binary LLSD map missing '}'")
            return result
        raise LLSDParseError(f"Unknown binary LLSD marker {marker!r}")


def parse_binary(data: bytes):
    reader = _BinaryReader(data)
    value = reader.read_value()
    if reader.pos != len(data):
        raise LLSDParseError("Trailing bytes after binary LLSD value")
    return value
```

### 1.4 Notation serialisation

Notation is the human-readable LLSD form used in config files, logs, and debugging. It is rarely a wire format for caps, but log output from the viewer and OpenSim uses it, so a Python tool that cannot *read* notation cannot read those logs.

```python
# Notation grammar (llsdserialize.cpp, LLSDNotationParser):
#   undef '!'  bool 'true'/'false' (also T/F in some writers)
#   integer 'i123'  real 'r1.5'  uuid 'u<uuid>'  date 'd"..."'
#   string: s"..." with \-escapes, or '...' single-quoted, or bare in maps keys
#   binary 'b64"...."' (base64) or 'b"raw"' in old writers — we write b64.
#   uri 'l"..."'  array '[v, v]'  map '{'key':v, ...}'

_NOTATION_ESCAPES = {'"': '\\"', "\\": "\\\\", "\n": "\\n", "\r": "\\r", "\t": "\\t"}


def _notation_quote(text: str) -> str:
    return '"' + "".join(_NOTATION_ESCAPES.get(ch, ch) for ch in text) + '"'


def format_notation(value) -> str:
    if value is None:
        return "!"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, URI):
        return "l" + _notation_quote(str(value))
    if isinstance(value, int):
        return f"i{_check_int(value)}"
    if isinstance(value, float):
        return f"r{_format_real(value)}"
    if isinstance(value, uuid.UUID):
        return f"u{value}"
    if isinstance(value, (bytes, bytearray)):
        return 'b64' + _notation_quote(base64.b64encode(bytes(value)).decode())
    if isinstance(value, datetime):
        iso = value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return f"d{_notation_quote(iso)}"
    if isinstance(value, str):
        return "s" + _notation_quote(value)
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(format_notation(v) for v in value) + "]"
    if isinstance(value, dict):
        inner = ", ".join(
            f"{_notation_quote(str(k))}:{format_notation(v)}" for k, v in value.items()
        )
        return "{" + inner + "}"
    raise TypeError(f"Cannot LLSD-serialise {type(value)!r}")


class _NotationParser:
    """Recursive-descent notation reader. Whitespace is insignificant
    except inside quoted strings."""

    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def _skip_ws(self) -> None:
        while self.pos < len(self.text) and self.text[self.pos] in " \t\r\n":
            self.pos += 1

    def _peek(self) -> str:
        self._skip_ws()
        return self.text[self.pos] if self.pos < len(self.text) else ""

    def _expect(self, ch: str) -> None:
        if self._peek() != ch:
            raise LLSDParseError(f"Notation: expected {ch!r} at {self.pos}")
        self.pos += 1

    def _quoted(self) -> str:
        self._skip_ws()
        quote = self.text[self.pos]
        if quote not in "\"'":
            raise LLSDParseError(f"Notation: expected quote at {self.pos}")
        self.pos += 1
        out = []
        while self.pos < len(self.text):
            ch = self.text[self.pos]
            self.pos += 1
            if ch == "\\" and self.pos < len(self.text):
                esc = self.text[self.pos]
                self.pos += 1
                out.append({"n": "\n", "r": "\r", "t": "\t"}.get(esc, esc))
            elif ch == quote:
                return "".join(out)
            else:
                out.append(ch)
        raise LLSDParseError("Notation: unterminated string")

    def _bare_word(self) -> str:
        self._skip_ws()
        start = self.pos
        while self.pos < len(self.text) and (
            self.text[self.pos].isalnum() or self.text[self.pos] in "-.+"
        ):
            self.pos += 1
        return self.text[start:self.pos]

    def parse(self):
        value = self._value()
        self._skip_ws()
        if self.pos != len(self.text):
            raise LLSDParseError("Notation: trailing characters")
        return value

    def _value(self):
        ch = self._peek()
        if ch == "!":
            self.pos += 1
            return None
        if ch == "[":
            self.pos += 1
            items = []
            if self._peek() != "]":
                items.append(self._value())
                while self._peek() == ",":
                    self.pos += 1
                    items.append(self._value())
            self._expect("]")
            return items
        if ch == "{":
            self.pos += 1
            result = {}
            if self._peek() != "}":
                while True:
                    key = self._quoted()  # map keys are quoted strings
                    self._expect(":")
                    result[key] = self._value()
                    if self._peek() == ",":
                        self.pos += 1
                        continue
                    break
            self._expect("}")
            return result
        if ch in "\"'":
            return self._quoted()
        # Prefixed scalars.
        self.pos += 1  # consume prefix / first letter
        if ch == "i":
            return _check_int(int(self._bare_word()))
        if ch == "r":
            return float(self._bare_word())
        if ch == "u":
            return uuid.UUID(self._bare_word())
        if ch == "s":
            return self._quoted()
        if ch == "l":
            return URI(self._quoted())
        if ch == "d":
            text = self._quoted()
            dt = datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
            return dt.replace(tzinfo=timezone.utc)
        if ch == "b":
            # b64"..." — the '64' follows the b.
            if self.text[self.pos:self.pos + 2] == "64":
                self.pos += 2
                return base64.b64decode(self._quoted())
            return self._quoted().encode("utf-8")
        if ch == "t":  # true
            self.pos += len("rue") if self.text[self.pos:self.pos + 3] == "rue" else 0
            return True
        if ch == "f":  # false
            self.pos += len("alse") if self.text[self.pos:self.pos + 4] == "alse" else 0
            return False
        raise LLSDParseError(f"Notation: unexpected character {ch!r} at {self.pos}")


def parse_notation(text: str):
    return _NotationParser(text).parse()


# --- Codec self-test vectors -------------------------------------------------
# These mirror the shape of vectors in llsdserialize test code: a value, and
# its three serialisations. If you change a codec, these must still pass and
# must still cross-parse (xml -> value == binary -> value == notation -> value).
SELF_TEST_VALUES = [
    None, True, False, 0, -2147483648, 2147483647, 1.5, -0.25,
    "", "hello", "snowman: \u2603", URI("https://example.com/cap/abc"),
    uuid.UUID("12345678-1234-5678-1234-567812345678"),
    b"\x00\x01\x02binary",
    datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc),
    [1, "two", 3.0, [True]],
    {"agent_id": uuid.UUID(int=7), "flags": [1, 2], "nested": {"x": None}},
]


def codec_self_test() -> None:
    for value in SELF_TEST_VALUES:
        assert parse_xml(format_xml(value)) == value, f"XML round-trip: {value!r}"
        assert parse_binary(format_binary(value)) == value, f"bin round-trip: {value!r}"
        assert parse_notation(format_notation(value)) == value, f"notation: {value!r}"
```

---

## 2. Zerocode (zero encoding)

Zerocoded messages replace runs of `0x00` bytes with the two-byte (or, for long runs, repeated) sequence `0x00 <count>`, where count is 1..255. It applies to the message body of messages the template marks `Zerocoded` — **not** to the 6-byte packet header, and not to appended ACKs. The classic bug is zerocoding the whole datagram; the second classic bug is the master template's flag being wrong for a message (the documented `ChatFromViewer` case), so flags come from the viewer's shipped template copy in production code.

```python
def zero_encode(data: bytes) -> bytes:
    """Encode zero runs. A run of N zeros (1 <= N) becomes one or more
    (0x00, count) pairs with count capped at 255."""
    out = bytearray()
    run = 0

    def flush(run_len: int) -> None:
        while run_len > 0:
            chunk = min(run_len, 255)
            out.extend((0, chunk))
            run_len -= chunk

    for byte in data:
        if byte == 0:
            run += 1
        else:
            if run:
                flush(run)
                run = 0
            out.append(byte)
    if run:
        flush(run)
    return bytes(out)


def zero_decode(data: bytes) -> bytes:
    """Inverse of zero_encode. A trailing lone 0x00 is malformed input —
    the encoder never produces one — so raise rather than guess."""
    out = bytearray()
    i = 0
    while i < len(data):
        byte = data[i]
        if byte != 0:
            out.append(byte)
            i += 1
        else:
            if i + 1 >= len(data):
                raise ValueError("Zerocoded data ends with a lone 0x00")
            count = data[i + 1]
            if count == 0:
                raise ValueError("Zerocode count of 0 is invalid")
            out.extend(b"\x00" * count)
            i += 2
    return bytes(out)
```

## 3. Packet build and parse

Wire layout of one UDP datagram:

```
byte 0      flags: 0x80 Zerocoded | 0x40 Reliable | 0x20 Resent | 0x10 Ack-appended
bytes 1..4  sequence number, big-endian U32
byte 5      extra header length (almost always 0; if non-zero, that many
            extra header bytes follow and are part of the header, not the body)
then        message ID, length by frequency:
              High:   1 byte  (0x01..0xFE range in practice)
              Medium: 2 bytes (0xFF, id)
              Low:    4 bytes (0xFF, 0xFF, id as U16)
              Fixed:  4 bytes (0xFF, 0xFF, 0xFF, 0xFB..0xFE style)
then        message body (zerocoded iff the Zerocoded flag is set)
then        if Ack flag: 1 byte count, then count x U32 sequence numbers
```

```python
import enum

FLAG_ZEROCODED = 0x80
FLAG_RELIABLE = 0x40
FLAG_RESENT = 0x20
FLAG_ACK = 0x10
HEADER_LEN = 6


class Frequency(enum.Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    FIXED = "Fixed"


def encode_message_id(freq: Frequency, number: int) -> bytes:
    if freq is Frequency.HIGH:
        if not (0 < number < 0xFF):
            raise ValueError(f"High message number {number} out of range")
        return bytes((number,))
    if freq is Frequency.MEDIUM:
        return bytes((0xFF, number & 0xFF))
    if freq is Frequency.LOW:
        return b"\xff\xff" + struct.pack(">H", number & 0xFFFF)
    # Fixed messages carry their full 32-bit ID (e.g. PacketAck 0xFFFFFFFB).
    return struct.pack(">I", number & 0xFFFFFFFF)


def decode_message_id(body: bytes) -> tuple[int, int]:
    """Return (raw_id_value, bytes_consumed). The caller maps the raw value
    to a message via the template: the encoding prefix determines frequency,
    so the raw value alone is not a unique key across frequencies — the
    template lookup in section 4 keys on (frequency, number)."""
    if not body:
        raise ValueError("Empty packet body")
    if body[0] != 0xFF:
        return body[0], 1                      # High
    if len(body) < 2:
        raise ValueError("Truncated message ID")
    if body[1] != 0xFF:
        return body[1], 2                      # Medium
    if len(body) < 4:
        raise ValueError("Truncated message ID")
    if body[2] != 0xFF:
        return struct.unpack(">H", body[2:4])[0], 4   # Low
    return struct.unpack(">I", body[0:4])[0], 4      # Fixed


class Packet:
    """One decoded datagram. `body` is the *decoded* message body with the
    message ID still at its front (use split_message below), and with
    zerocoding already undone. `acks` are sequence numbers this packet
    piggybacks."""

    __slots__ = ("flags", "sequence", "extra_header", "body", "acks")

    def __init__(self, flags: int, sequence: int, extra_header: bytes,
                 body: bytes, acks: list[int]):
        self.flags = flags
        self.sequence = sequence
        self.extra_header = extra_header
        self.body = body
        self.acks = acks

    @property
    def reliable(self) -> bool:
        return bool(self.flags & FLAG_RELIABLE)

    @property
    def zerocoded(self) -> bool:
        return bool(self.flags & FLAG_ZEROCODED)


def parse_packet(datagram: bytes) -> Packet:
    if len(datagram) < HEADER_LEN:
        raise ValueError("Datagram shorter than the 6-byte header")
    flags = datagram[0]
    sequence = struct.unpack(">I", datagram[1:5])[0]
    extra_len = datagram[5]
    offset = HEADER_LEN + extra_len
    if offset > len(datagram):
        raise ValueError("Extra header length overruns the datagram")
    extra_header = datagram[HEADER_LEN:offset]
    payload = datagram[offset:]

    acks: list[int] = []
    if flags & FLAG_ACK:
        # The ACK block is at the very end and is never zerocoded, so it
        # must be peeled off *before* zero-decoding the body.
        if not payload:
            raise ValueError("Ack flag set but no payload")
        count = payload[-1]
        needed = 1 + 4 * count
        if len(payload) < needed:
            raise ValueError("Appended ACK list overruns the datagram")
        ack_bytes = payload[len(payload) - needed: len(payload) - 1]
        acks = [struct.unpack(">I", ack_bytes[i:i + 4])[0]
                for i in range(0, len(ack_bytes), 4)]
        payload = payload[:len(payload) - needed]

    if flags & FLAG_ZEROCODED:
        payload = zero_decode(payload)

    return Packet(flags, sequence, extra_header, payload, acks)


def build_packet(sequence: int, message_id_bytes: bytes, body: bytes, *,
                 reliable: bool = False, zerocoded: bool = False,
                 resent: bool = False, acks: list[int] | None = None) -> bytes:
    """Assemble a datagram. `body` is the message body *after* the ID."""
    flags = 0
    payload = message_id_bytes + body
    if zerocoded:
        flags |= FLAG_ZEROCODED
        payload = zero_encode(payload)
    if reliable:
        flags |= FLAG_RELIABLE
    if resent:
        flags |= FLAG_RESENT
    ack_block = b""
    if acks:
        if len(acks) > 255:
            raise ValueError("At most 255 appended ACKs per packet")
        flags |= FLAG_ACK
        ack_block = b"".join(struct.pack(">I", a) for a in acks)
        ack_block += bytes((len(acks),))
    header = bytes((flags,)) + struct.pack(">I", sequence) + b"\x00"
    return header + payload + ack_block
```

### 3.1 Field-level body packing

Message bodies are sequences of typed fields in template order. Blocks repeat: `Single` once, `Multiple N` exactly N times, `Variable` preceded by a count (U8 for Variable 1-style blocks in most messages; the template parser in section 4 records the count width per block). The packer below is the small typed cursor both directions use.

```python
class BodyWriter:
    def __init__(self):
        self.buf = bytearray()

    def u8(self, v): self.buf.append(v & 0xFF); return self
    def u16(self, v): self.buf += struct.pack(">H", v & 0xFFFF); return self
    def u32(self, v): self.buf += struct.pack(">I", v & 0xFFFFFFFF); return self
    def u64(self, v): self.buf += struct.pack(">Q", v & 0xFFFFFFFFFFFFFFFF); return self
    def s8(self, v): self.buf += struct.pack(">b", v); return self
    def s16(self, v): self.buf += struct.pack(">h", v); return self
    def s32(self, v): self.buf += struct.pack(">i", v); return self
    def f32(self, v): self.buf += struct.pack(">f", v); return self
    def f64(self, v): self.buf += struct.pack(">d", v); return self
    def boolean(self, v): return self.u8(1 if v else 0)
    def uuid(self, v: uuid.UUID): self.buf += v.bytes; return self
    def vector3(self, v):  # tuple of 3 floats, F32 each
        for c in v: self.f32(c)
        return self
    def vector3d(self, v):
        for c in v: self.f64(c)
        return self
    def vector4(self, v):
        for c in v: self.f32(c)
        return self
    def quaternion(self, v):
        # On the wire a quaternion is 3 x F32 (x, y, z); w is reconstructed
        # as sqrt(1 - x^2 - y^2 - z^2) by the receiver. Sending all four is
        # a classic porting bug that shifts every following field.
        for c in v[:3]: self.f32(c)
        return self
    def variable1(self, data: bytes):
        self.u8(len(data)); self.buf += data; return self
    def variable2(self, data: bytes):
        self.u16(len(data)); self.buf += data; return self
    def fixed(self, data: bytes):
        self.buf += data; return self
    def string_z(self, text: str):
        # Many legacy Variable 1 string fields are NUL-terminated on the wire.
        return self.variable1(text.encode("utf-8") + b"\x00")
    def bytes(self) -> bytes:
        return bytes(self.buf)


class BodyReader:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def take(self, n: int) -> bytes:
        if self.pos + n > len(self.data):
            raise ValueError("Message body truncated")
        chunk = self.data[self.pos:self.pos + n]
        self.pos += n
        return chunk

    def u8(self): return self.take(1)[0]
    def u16(self): return struct.unpack(">H", self.take(2))[0]
    def u32(self): return struct.unpack(">I", self.take(4))[0]
    def u64(self): return struct.unpack(">Q", self.take(8))[0]
    def s8(self): return struct.unpack(">b", self.take(1))[0]
    def s16(self): return struct.unpack(">h", self.take(2))[0]
    def s32(self): return struct.unpack(">i", self.take(4))[0]
    def f32(self): return struct.unpack(">f", self.take(4))[0]
    def f64(self): return struct.unpack(">d", self.take(8))[0]
    def boolean(self): return self.u8() != 0
    def uuid(self): return uuid.UUID(bytes=self.take(16))
    def vector3(self): return (self.f32(), self.f32(), self.f32())
    def vector3d(self): return (self.f64(), self.f64(), self.f64())
    def vector4(self): return (self.f32(), self.f32(), self.f32(), self.f32())

    def quaternion(self):
        x, y, z = self.f32(), self.f32(), self.f32()
        w2 = 1.0 - (x * x + y * y + z * z)
        w = math.sqrt(w2) if w2 > 0 else 0.0
        return (x, y, z, w)

    def variable1(self): return self.take(self.u8())
    def variable2(self): return self.take(self.u16())
    def fixed(self, n: int): return self.take(n)

    def string_z(self) -> str:
        raw = self.variable1()
        return raw.split(b"\x00", 1)[0].decode("utf-8", "replace")

    @property
    def exhausted(self) -> bool:
        return self.pos == len(self.data)
```

---

## 4. A message-template parser that generates dataclasses

`message_template.msg` is a brace-structured text file. Grammar sketch:

```
{
    MessageName  Low  123  NotTrusted  Zerocoded
    {
        BlockName  Single            // or: Variable, or: Multiple 4
        {   FieldName   U32   }
        {   OtherField  Variable 1   }
    }
}
```

The parser below produces an in-memory model, then a code generator emits one `@dataclass` per message with `pack()` / `unpack()` methods driven by the field-type table. Generating from the template — instead of hand-writing 480+ message classes — is what LibreMetaverse's source generators and Lumiya's 477 Java classes both do, and it is the only approach that survives a template rev.

```python
"""template_parser.py — parse message_template.msg and generate dataclasses."""
from dataclasses import dataclass, field as dc_field

# Template field type -> (BodyWriter method, BodyReader method, python type)
FIELD_TYPES = {
    "U8": ("u8", "u8", "int"), "U16": ("u16", "u16", "int"),
    "U32": ("u32", "u32", "int"), "U64": ("u64", "u64", "int"),
    "S8": ("s8", "s8", "int"), "S16": ("s16", "s16", "int"),
    "S32": ("s32", "s32", "int"), "F32": ("f32", "f32", "float"),
    "F64": ("f64", "f64", "float"), "BOOL": ("boolean", "boolean", "bool"),
    "LLUUID": ("uuid", "uuid", "uuid.UUID"),
    "LLVector3": ("vector3", "vector3", "tuple"),
    "LLVector3d": ("vector3d", "vector3d", "tuple"),
    "LLVector4": ("vector4", "vector4", "tuple"),
    "LLQuaternion": ("quaternion", "quaternion", "tuple"),
    "Variable 1": ("variable1", "variable1", "bytes"),
    "Variable 2": ("variable2", "variable2", "bytes"),
    "Fixed": ("fixed", "fixed", "bytes"),  # length comes from the template count
    "IPADDR": ("u32", "u32", "int"), "IPPORT": ("u16", "u16", "int"),
}


@dataclass
class TemplateField:
    name: str
    type_name: str
    fixed_len: int = 0  # only for Fixed


@dataclass
class TemplateBlock:
    name: str
    kind: str            # 'Single' | 'Variable' | 'Multiple'
    count: int = 1       # for Multiple
    fields: list[TemplateField] = dc_field(default_factory=list)


@dataclass
class TemplateMessage:
    name: str
    frequency: str       # 'High' | 'Medium' | 'Low' | 'Fixed'
    number: int
    trusted: bool
    zerocoded: bool
    deprecated: bool = False
    blocks: list[TemplateBlock] = dc_field(default_factory=list)

    @property
    def key(self) -> tuple[str, int]:
        return (self.frequency, self.number)


def _tokenise_template(text: str):
    """Yield tokens: braces and whitespace-separated words, with // comments
    stripped. The template file is not free-form C; a simple lexer suffices
    and is exactly what the historical parsers (pyogp, libomv) did."""
    for line in text.splitlines():
        line = line.split("//", 1)[0]
        for tok in line.replace("{", " { ").replace("}", " } ").split():
            yield tok


class TemplateParser:
    def __init__(self, text: str):
        self.tokens = list(_tokenise_template(text))
        self.pos = 0

    def peek(self) -> str | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def next(self) -> str:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, tok: str) -> None:
        got = self.next()
        if got != tok:
            raise ValueError(f"Template: expected {tok!r}, got {got!r}")

    def parse(self) -> dict[tuple[str, int], TemplateMessage]:
        messages = {}
        while self.peek() is not None:
            if self.peek() != "{":
                # The file header has bare words (version lines etc.) in
                # some revisions; skip anything outside a message block.
                self.next()
                continue
            msg = self._parse_message()
            messages[msg.key] = msg
        return messages

    def _parse_message(self) -> TemplateMessage:
        self.expect("{")
        name = self.next()
        frequency = self.next()
        number_tok = self.next()
        number = int(number_tok, 0)  # Fixed IDs are hex (0xFFFFFFFB)
        trust = self.next()
        encoding = self.next()
        msg = TemplateMessage(
            name=name, frequency=frequency, number=number,
            trusted=(trust == "Trusted"), zerocoded=(encoding == "Zerocoded"),
        )
        # Optional trailing flags on the header line: Deprecated, UDPBlackListed.
        while self.peek() not in ("{", "}", None):
            flag = self.next()
            if flag == "Deprecated":
                msg.deprecated = True
        while self.peek() == "{":
            msg.blocks.append(self._parse_block())
        self.expect("}")
        return msg

    def _parse_block(self) -> TemplateBlock:
        self.expect("{")
        name = self.next()
        kind = self.next()
        count = 1
        if kind == "Multiple":
            count = int(self.next())
        block = TemplateBlock(name=name, kind=kind, count=count)
        while self.peek() == "{":
            self.expect("{")
            fname = self.next()
            # Field type may be two tokens ('Variable 1', 'Variable 2').
            ftype = self.next()
            if ftype == "Variable":
                ftype = "Variable " + self.next()
            fixed_len = 0
            if ftype == "Fixed":
                fixed_len = int(self.next())
            block.fields.append(TemplateField(fname, ftype, fixed_len))
            self.expect("}")
        self.expect("}")
        return block
```

### 4.1 The code generator

```python
def generate_dataclasses(messages: dict[tuple[str, int], TemplateMessage]) -> str:
    """Emit Python source: one dataclass per message, with pack/unpack.

    Variable blocks are emitted as list fields with a U8 count prefix —
    correct for the overwhelming majority of messages. The handful of
    messages whose variable-block count is a different width are listed in
    OVERRIDES in real generators (LibreMetaverse hand-tunes the same few);
    check any message whose unpack leaves the reader non-exhausted.
    """
    lines = [
        '"""GENERATED from message_template.msg — do not hand-edit.',
        'Regenerate with template_parser.generate_dataclasses()."""',
        "import uuid",
        "from dataclasses import dataclass, field",
        "",
    ]
    for msg in sorted(messages.values(), key=lambda m: (m.frequency, m.number)):
        lines.append("@dataclass")
        lines.append(f"class {msg.name}:")
        lines.append(f'    """{msg.frequency} {msg.number} '
                     f'{"Trusted" if msg.trusted else "NotTrusted"} '
                     f'{"Zerocoded" if msg.zerocoded else "Unencoded"}"""')
        for block in msg.blocks:
            for f in block.fields:
                py_type = FIELD_TYPES[f.type_name][2]
                if block.kind == "Single":
                    default = "field(default_factory=list)" if py_type == "list" else _default_for(py_type)
                    lines.append(f"    {block.name}_{f.name}: {py_type} = {default}")
                else:
                    lines.append(f"    {block.name}: list = field(default_factory=list)")
                    break  # one list field per repeating block
        lines.append("")
        lines.append("    def pack(self, w):  # w: BodyWriter")
        for block in msg.blocks:
            if block.kind == "Single":
                for f in block.fields:
                    writer = FIELD_TYPES[f.type_name][0]
                    if f.type_name == "Fixed":
                        lines.append(f"        w.fixed(self.{block.name}_{f.name})")
                    else:
                        lines.append(f"        w.{writer}(self.{block.name}_{f.name})")
            elif block.kind == "Multiple":
                lines.append(f"        for _blk in self.{block.name}:")
                for f in block.fields:
                    writer = FIELD_TYPES[f.type_name][0]
                    lines.append(f"            w.{writer}(_blk['{f.name}'])")
            else:  # Variable
                lines.append(f"        w.u8(len(self.{block.name}))")
                lines.append(f"        for _blk in self.{block.name}:")
                for f in block.fields:
                    writer = FIELD_TYPES[f.type_name][0]
                    lines.append(f"            w.{writer}(_blk['{f.name}'])")
        lines.append("        return w")
        lines.append("")
        lines.append("    @classmethod")
        lines.append("    def unpack(cls, r):  # r: BodyReader")
        lines.append("        obj = cls()")
        for block in msg.blocks:
            if block.kind == "Single":
                for f in block.fields:
                    reader = FIELD_TYPES[f.type_name][1]
                    if f.type_name == "Fixed":
                        lines.append(f"        obj.{block.name}_{f.name} = r.fixed({f.fixed_len})")
                    else:
                        lines.append(f"        obj.{block.name}_{f.name} = r.{reader}()")
            else:
                count_expr = str(block.count) if block.kind == "Multiple" else "r.u8()"
                lines.append(f"        obj.{block.name} = []")
                lines.append(f"        for _ in range({count_expr}):")
                lines.append("            _blk = {}")
                for f in block.fields:
                    reader = FIELD_TYPES[f.type_name][1]
                    lines.append(f"            _blk['{f.name}'] = r.{reader}()")
                lines.append(f"            obj.{block.name}.append(_blk)")
        lines.append("        return obj")
        lines.append("")
        lines.append("")
    return "\n".join(lines)


def _default_for(py_type: str) -> str:
    return {"int": "0", "float": "0.0", "bool": "False", "bytes": "b''",
            "tuple": "(0.0, 0.0, 0.0)", "uuid.UUID": "uuid.UUID(int=0)"}[py_type]
```

### 4.2 Hand-written versions of the messages every client needs first

Generated classes are the production path, but the login-adjacent messages are worth seeing once in full hand-written form, because every port (this one, Lumiya's Java, node-metaverse's TypeScript) starts by getting exactly these right.

```python
@dataclass
class UseCircuitCode:
    """Low 4, Trusted, Zerocoded. First UDP message after login."""
    CircuitCode_Code: int = 0
    CircuitCode_SessionID: uuid.UUID = uuid.UUID(int=0)
    CircuitCode_ID: uuid.UUID = uuid.UUID(int=0)  # agent ID

    def pack(self, w):
        return w.u32(self.CircuitCode_Code).uuid(self.CircuitCode_SessionID).uuid(self.CircuitCode_ID)

    @classmethod
    def unpack(cls, r):
        return cls(r.u32(), r.uuid(), r.uuid())


@dataclass
class CompleteAgentMovement:
    """Low 41, Trusted, Zerocoded. Tells the simulator the agent is ready
    to be put in-world. Until this arrives, no object updates flow."""
    AgentData_AgentID: uuid.UUID = uuid.UUID(int=0)
    AgentData_SessionID: uuid.UUID = uuid.UUID(int=0)
    AgentData_CircuitCode: int = 0

    def pack(self, w):
        return (w.uuid(self.AgentData_AgentID).uuid(self.AgentData_SessionID)
                 .u32(self.AgentData_CircuitCode))

    @classmethod
    def unpack(cls, r):
        return cls(r.uuid(), r.uuid(), r.u32())


@dataclass
class PacketAck:
    """Fixed 0xFFFFFFFB, NotTrusted, Unencoded. Standalone ACK packet;
    most ACKs should instead be appended to outgoing packets (section 5)."""
    Packets: list = dc_field(default_factory=list)  # list of U32 sequence ids

    def pack(self, w):
        w.u8(len(self.Packets))
        for seq in self.Packets:
            w.u32(seq)
        return w

    @classmethod
    def unpack(cls, r):
        count = r.u8()
        return cls([r.u32() for _ in range(count)])
```

---

## 5. An asyncio UDP circuit with reliability, ACKs, ping, and throttle

The circuit owns: the outgoing sequence counter, the unacked-reliable resend queue, ACK collection (piggybacked, with a standalone `PacketAck` fallback timer), ping/pong for liveness and RTT, and a per-category token-bucket throttle. This mirrors `indra/llmessage/llcircuit.cpp` and `LibreMetaverse.Transport` at teaching scale — production circuits add congestion tuning and packet-size MTU handling (keep datagrams under ~1200 bytes of body to survive real networks; the simulator fragments nothing for you).

```python
"""circuit.py — asyncio UDP circuit for one simulator connection."""
import asyncio
import time

RESEND_INTERVAL = 0.4     # seconds between reliable resend sweeps
ACK_FLUSH_DELAY = 0.1     # piggyback window before a standalone PacketAck
PING_INTERVAL = 5.0
CIRCUIT_TIMEOUT = 60.0    # no inbound packet for this long => dead circuit


class TokenBucket:
    """One AgentThrottle category. Refills at `rate` units/sec up to
    `burst`. send() costs 1 unit per packet in that category."""

    def __init__(self, rate: float, burst: float):
        self.rate, self.burst = rate, burst
        self.tokens = burst
        self.updated = time.monotonic()

    def take(self) -> bool:
        now = time.monotonic()
        self.tokens = min(self.burst, self.tokens + (now - self.updated) * self.rate)
        self.updated = now
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False


# AgentThrottle categories, in the order the AgentThrottle message sends them.
THROTTLE_CATEGORIES = ("resend", "land", "wind", "cloud", "task", "texture", "asset")


class Circuit(asyncio.DatagramProtocol):
    def __init__(self, template: dict, on_message, on_dead=None):
        self.template = template          # (freq, number) -> TemplateMessage
        self.on_message = on_message      # callable(msg_name, BodyReader, Packet)
        self.on_dead = on_dead            # callable() when the circuit times out
        self.transport: asyncio.DatagramTransport | None = None
        self.peer: tuple[str, int] | None = None
        self.next_sequence = 1
        self.unacked: dict[int, tuple[bytes, float]] = {}  # seq -> (datagram, last sent)
        self.pending_acks: list[int] = []
        self._ack_task: asyncio.Task | None = None
        self.last_received = time.monotonic()
        self.last_ping_id = 0
        self.rtt_seconds: float | None = None
        self._ping_sent_at: dict[int, float] = {}
        self.throttles = {c: TokenBucket(rate=200.0, burst=400.0)
                          for c in THROTTLE_CATEGORIES}
        self.closed = False

    # -- asyncio.DatagramProtocol -------------------------------------------
    def connection_made(self, transport):
        self.transport = transport
        self.peer = transport.get_extra_info("peername")

    def datagram_received(self, data: bytes, addr) -> None:
        self.last_received = time.monotonic()
        try:
            packet = parse_packet(data)
        except ValueError:
            return  # garbage on a UDP socket is normal; drop, never crash
        # Any appended ACKs retire our reliable sends.
        for seq in packet.acks:
            self.unacked.pop(seq, None)
        if packet.reliable:
            self._queue_ack(packet.sequence)
        self._dispatch(packet)

    def error_received(self, exc) -> None:
        # ICMP port-unreachable etc. On some platforms this is how a dead
        # simulator first shows up; the timeout sweep is the real detector.
        pass

    def connection_lost(self, exc) -> None:
        self.closed = True

    # -- dispatch -------------------------------------------------------------
    def _dispatch(self, packet: Packet) -> None:
        raw_id, consumed = decode_message_id(packet.body)
        freq = _frequency_of(packet.body)
        msg_def = self.template.get((freq.value, raw_id))
        if msg_def is None:
            return  # unknown message: newer simulator than template. Skip.
        if msg_def.name == "PacketAck":
            reader = BodyReader(packet.body[consumed:])
            ack = PacketAck.unpack(reader)
            for seq in ack.Packets:
                self.unacked.pop(seq, None)
            return
        if msg_def.name == "StartPingCheck":
            reader = BodyReader(packet.body[consumed:])
            ping_id = reader.u8()
            self._send_ping_reply(ping_id)
            return
        reader = BodyReader(packet.body[consumed:])
        self.on_message(msg_def.name, reader, packet)

    # -- sending ---------------------------------------------------------------
    def send_message(self, msg_name: str, pack_fn, *, reliable: bool = False,
                     category: str = "task") -> int:
        """pack_fn(BodyWriter) writes the body after the message ID."""
        msg_def = _by_name(self.template, msg_name)
        if not self.throttles[category].take():
            # Throttled: for unreliable traffic, dropping is correct. For
            # reliable traffic the caller should retry — we surface it by
            # returning -1 rather than silently queueing forever.
            if reliable:
                return -1
            return 0
        writer = BodyWriter()
        pack_fn(writer)
        seq = self.next_sequence
        self.next_sequence += 1
        acks, self.pending_acks = self.pending_acks, []
        datagram = build_packet(
            seq,
            encode_message_id(Frequency(msg_def.frequency), msg_def.number),
            writer.bytes(),
            reliable=reliable, zerocoded=msg_def.zerocoded, acks=acks,
        )
        self.transport.sendto(datagram, self.peer)
        if reliable:
            self.unacked[seq] = (datagram, time.monotonic())
        return seq

    def _queue_ack(self, sequence: int) -> None:
        self.pending_acks.append(sequence)
        if self._ack_task is None or self._ack_task.done():
            loop = asyncio.get_event_loop()
            self._ack_task = loop.create_task(self._flush_acks_later())

    async def _flush_acks_later(self) -> None:
        await asyncio.sleep(ACK_FLUSH_DELAY)
        if not self.pending_acks or self.closed:
            return
        # Nothing outgoing carried our ACKs in the window: send PacketAck.
        acks, self.pending_acks = self.pending_acks, []
        writer = BodyWriter()
        PacketAck(acks).pack(writer)
        seq = self.next_sequence
        self.next_sequence += 1
        datagram = build_packet(seq, encode_message_id(Frequency.FIXED, 0xFFFFFFFB),
                                writer.bytes())
        self.transport.sendto(datagram, self.peer)

    def _send_ping_reply(self, ping_id: int) -> None:
        # CompletePingCheck: Fixed 0xFFFFFFFC family in the template's fixed
        # block; body is the echoed ping ID (U8) plus an unused U32 in the
        # current template revision. Echo exactly what StartPingCheck sent.
        writer = BodyWriter()
        writer.u8(ping_id)
        seq = self.next_sequence
        self.next_sequence += 1
        datagram = build_packet(seq, encode_message_id(Frequency.FIXED, 0xFFFFFFFC),
                                writer.bytes())
        self.transport.sendto(datagram, self.peer)

    # -- background maintenance --------------------------------------------------
    async def run_maintenance(self) -> None:
        """Resends, pings, and the dead-circuit detector. Run as a task for
        the life of the session; cancel it on logout."""
        while not self.closed:
            await asyncio.sleep(0.1)
            now = time.monotonic()
            # Resend sweep.
            for seq, (datagram, last) in list(self.unacked.items()):
                if now - last >= RESEND_INTERVAL:
                    # Mark resent: set the Resent flag byte in a copy.
                    resent = bytearray(datagram)
                    resent[0] |= FLAG_RESENT
                    self.transport.sendto(bytes(resent), self.peer)
                    self.unacked[seq] = (datagram, now)
            # Ping sweep (StartPingCheck from us measures our RTT view).
            if now - getattr(self, "_last_ping", 0) >= PING_INTERVAL:
                self._last_ping = now
                self.last_ping_id = (self.last_ping_id + 1) & 0xFF
                self._ping_sent_at[self.last_ping_id] = now
                writer = BodyWriter()
                writer.u8(self.last_ping_id).u32(0)
                seq = self.next_sequence
                self.next_sequence += 1
                self.transport.sendto(build_packet(
                    seq, encode_message_id(Frequency.FIXED, 0xFFFFFFFD),
                    writer.bytes()), self.peer)
            # Dead circuit.
            if now - self.last_received > CIRCUIT_TIMEOUT:
                self.closed = True
                if self.on_dead:
                    self.on_dead()
                return


def _frequency_of(body: bytes) -> Frequency:
    if body[0] != 0xFF:
        return Frequency.HIGH
    if body[1] != 0xFF:
        return Frequency.MEDIUM
    if body[2] != 0xFF:
        return Frequency.LOW
    return Frequency.FIXED


def _by_name(template: dict, name: str) -> TemplateMessage:
    for msg in template.values():
        if msg.name == name:
            return msg
    raise KeyError(f"Message {name} not in template")
```

## 6. Caps client and the Event Queue

Caps are HTTPS endpoints whose URLs come from the seed capability at login. Rules that matter: cap URLs are per-region, per-session, and unguessable — never persist them; a `404`/`499` from a cap usually means the region changed under you; the Event Queue is a long-poll where the client sends the last event ID it acked and the simulator holds the request open until events arrive or it times out empty (which is normal — repoll immediately).

```python
"""caps.py — capability client + EventQueueGet long-poll."""
import httpx

CAP_CONTENT_TYPE = "application/llsd+xml"


class CapsClient:
    def __init__(self, caps: dict[str, str], http: httpx.AsyncClient):
        self.caps = caps          # name -> URL, from the seed-cap exchange
        self.http = http

    def has(self, name: str) -> bool:
        return name in self.caps

    async def post_llsd(self, name: str, value) -> object:
        """POST an LLSD value to a named cap and parse the LLSD reply.
        Raises KeyError if the region did not grant the cap — callers must
        branch on has() and fall back to UDP where the viewer does."""
        url = self.caps[name]
        resp = await self.http.post(
            url, content=format_xml(value),
            headers={"Content-Type": CAP_CONTENT_TYPE},
        )
        resp.raise_for_status()
        if not resp.content:
            return None
        return parse_xml(resp.content)

    async def get_texture(self, texture_id: uuid.UUID) -> bytes | None:
        """GetTexture cap: HTTP fetch of a JPEG2000 codestream.
        Real clients send Range headers to pull progressive discard levels;
        this fetches the whole asset, which is what a bot usually wants."""
        if not self.has("GetTexture"):
            return None
        url = self.caps["GetTexture"]
        resp = await self.http.get(url, params={"texture_id": str(texture_id)})
        if resp.status_code == 404:
            return None  # asset genuinely missing — log the UUID, not a name
        resp.raise_for_status()
        return resp.content


class EventQueue:
    """Long-poll loop for EventQueueGet. Events arrive as an LLSD map:
    {'id': <next id>, 'events': [{'message': name, 'body': {...}}, ...]}.
    You must send back the id you received as 'ack' on the next poll, or
    events repeat. A poll that errors with the simulator's error id means
    the queue is dead (region restart / teleport) — stop and let the
    session layer rebuild it."""

    def __init__(self, caps: CapsClient, on_event):
        self.caps = caps
        self.on_event = on_event  # callable(message_name: str, body: dict)
        self.ack_id: int | None = None
        self.running = False

    async def run(self) -> None:
        self.running = True
        while self.running:
            body = {"ack": self.ack_id, "done": False}
            try:
                result = await self.caps.post_llsd("EventQueueGet", body)
            except httpx.HTTPError:
                if not self.running:
                    return
                await asyncio.sleep(1.0)  # transient; the session layer owns death detection
                continue
            if not isinstance(result, dict):
                continue
            self.ack_id = result.get("id", self.ack_id)
            for event in result.get("events", []) or []:
                self.on_event(event.get("message", ""), event.get("body", {}) or {})

    def stop(self) -> None:
        self.running = False
```

---

## 7. Login flow

Production login is an XML-RPC (or LLSD, depending on endpoint revision) POST to the grid's login URI — Agni: `https://login.agni.lindenlab.com/cgi-bin/login.cgi`; OpenSim standalone: `http://127.0.0.1:9000/` (its login service speaks the same request shape). The password field historically is `"$1$" + md5(password)`; current Agni login also has MFA/token variants — read the current viewer `llstartup` code and LibreMetaverse login before changing anything here, and never log the password, the hash, `session_id`, or `secure_session_id`.

Response fields used below: `agent_id`, `session_id`, `secure_session_id`, `sim_ip`, `sim_port`, `circuit_code`, `seed_capability`, `inventory-skeleton`, `buddy-list`, `login-flags`, and on failure `login` != `"true"` plus `message` / `reason` (MFA challenges arrive as a distinct reason — surface them to the user, do not retry blindly).

```python
"""login.py — login request, seed-cap exchange, and session bootstrap."""
import hashlib
import xml.etree.ElementTree as ET

AGNI_LOGIN_URI = "https://login.agni.lindenlab.com/cgi-bin/login.cgi"
OPENSIM_LOGIN_URI = "http://127.0.0.1:9000/"


def _xmlrpc_value(value) -> str:
    """Minimal XML-RPC value encoder for the login request shapes.
    Strings, ints, bools, arrays, and structs only — that is all login uses."""
    if isinstance(value, bool):
        return f"<value><boolean>{1 if value else 0}</boolean></value>"
    if isinstance(value, int):
        return f"<value><int>{value}</int></value>"
    if isinstance(value, (list, tuple)):
        inner = "".join(_xmlrpc_value(v) for v in value)
        return f"<value><array><data>{inner}</data></array></value>"
    if isinstance(value, dict):
        inner = "".join(
            f"<member><name>{k}</name>{_xmlrpc_value(v)}</member>"
            for k, v in value.items()
        )
        return f"<value><struct>{inner}</struct></value>"
    text = str(value).replace("&", "&amp;").replace("<", "&lt;")
    return f"<value><string>{text}</string></value>"


def build_login_request(first: str, last: str, password: str, *,
                        start: str = "last", channel: str = "PythonClient",
                        version: str = "1.0.0", mac: str = "00:00:00:00:00:00",
                        id0: str = "") -> bytes:
    """`start` is 'home', 'last', or a 'uri:&region&x&y&z' string."""
    passwd = "$1$" + hashlib.md5(password.encode("utf-8")).hexdigest()
    params = {
        "first": first, "last": last, "passwd": passwd,
        "start": start, "channel": channel, "version": version,
        "platform": "Linux", "mac": mac, "id0": id0,
        "agree_to_tos": True, "read_critical": True,
        # Options ask the server to include these blocks in the response.
        "options": ["inventory-root", "inventory-skeleton", "buddy-list",
                    "gestures", "event_categories", "classified_categories",
                    "avatar-picker-url", "login-flags", "global-textures"],
    }
    body = ('<?xml version="1.0"?><methodCall><methodName>login_to_simulator'
            "</methodName><params><param>" + _xmlrpc_value(params) +
            "</param></params></methodCall>")
    return body.encode("utf-8")


def _xmlrpc_parse(data: bytes) -> dict:
    """Parse the login response: an XML-RPC struct whose values are mostly
    strings, with nested structs/arrays for inventory-skeleton etc. LLSD-ish
    enough that we convert into plain Python containers."""
    root = ET.fromstring(data)

    def read_value(el):
        child = list(el)[0] if len(el) else None
        if child is None:
            return el.text or ""
        if child.tag == "string":
            return child.text or ""
        if child.tag in ("int", "i4"):
            return int(child.text or 0)
        if child.tag == "boolean":
            return (child.text or "0") == "1"
        if child.tag == "double":
            return float(child.text or 0)
        if child.tag == "array":
            data_el = child.find("data")
            return [read_value(v) for v in data_el.findall("value")] if data_el is not None else []
        if child.tag == "struct":
            out = {}
            for member in child.findall("member"):
                name = member.findtext("name") or ""
                out[name] = read_value(member.find("value"))
            return out
        return child.text or ""

    value_el = root.find("./params/param/value")
    if value_el is None:
        raise LLSDParseError("Login response has no value")
    return read_value(value_el)


@dataclass
class LoginResult:
    agent_id: uuid.UUID
    session_id: uuid.UUID
    secure_session_id: uuid.UUID
    circuit_code: int
    sim_ip: str
    sim_port: int
    seed_capability: str
    inventory_root: uuid.UUID | None
    raw: dict


async def login(http: httpx.AsyncClient, login_uri: str, first: str, last: str,
                password: str, **kwargs) -> LoginResult:
    request = build_login_request(first, last, password, **kwargs)
    resp = await http.post(login_uri, content=request,
                           headers={"Content-Type": "text/xml"})
    resp.raise_for_status()
    data = _xmlrpc_parse(resp.content)
    if data.get("login") != "true":
        # 'reason' distinguishes bad password from MFA challenge from
        # grid-down maintenance. Pass it through verbatim to the user.
        raise RuntimeError(f"Login failed: {data.get('message', '')} "
                           f"(reason={data.get('reason', 'unknown')})")
    root = None
    skeleton = data.get("inventory-skeleton") or []
    if skeleton:
        root = uuid.UUID(skeleton[0]["folder_id"])
    return LoginResult(
        agent_id=uuid.UUID(data["agent_id"]),
        session_id=uuid.UUID(data["session_id"]),
        secure_session_id=uuid.UUID(data["secure_session_id"]),
        circuit_code=int(data["circuit_code"]),
        sim_ip=data["sim_ip"], sim_port=int(data["sim_port"]),
        seed_capability=data["seed_capability"],
        inventory_root=root, raw=data,
    )


# Caps every thin client should request from the seed cap on login.
WANTED_CAPS = [
    "EventQueueGet", "FetchInventory2", "FetchInventoryDescendents2",
    "FetchLib2", "FetchLibDescendents2", "InventoryAPIv3", "LibraryAPIv3",
    "GetTexture", "GetMesh", "GetMesh2", "SimulatorFeatures",
    "GetDisplayNames", "ChatSessionRequest", "AgentPreferences",
    "ExtEnvironment", "EnvironmentSettings", "RenderMaterials",
    "NewFileAgentInventory", "UpdateAgentInformation",
]


async def fetch_caps(http: httpx.AsyncClient, seed_url: str,
                     wanted: list[str] = WANTED_CAPS) -> dict[str, str]:
    """POST the wanted cap names (LLSD array of strings) to the seed cap;
    the reply is an LLSD map of name -> URL for the caps actually granted.
    Missing names are normal — grids and regions grant different subsets."""
    resp = await http.post(seed_url, content=format_xml(list(wanted)),
                           headers={"Content-Type": CAP_CONTENT_TYPE})
    resp.raise_for_status()
    granted = parse_xml(resp.content)
    return {k: str(v) for k, v in (granted or {}).items()}


async def bootstrap_session(http, login_uri, first, last, password, template, on_message):
    """Full bootstrap: login -> caps -> UDP circuit -> UseCircuitCode ->
    CompleteAgentMovement -> RegionHandshakeReply is handled by the caller
    when RegionHandshake arrives (it needs the circuit, below). Returns
    (LoginResult, CapsClient, Circuit)."""
    result = await login(http, login_uri, first, last, password)
    caps_map = await fetch_caps(http, result.seed_capability)
    caps = CapsClient(caps_map, http)
    loop = asyncio.get_event_loop()
    transport, circuit = await loop.create_datagram_endpoint(
        lambda: Circuit(template, on_message),
        remote_addr=(result.sim_ip, result.sim_port),
    )
    circuit.transport = transport
    # UseCircuitCode: Code, SessionID, ID (agent).
    circuit.send_message("UseCircuitCode", lambda w: UseCircuitCode(
        result.circuit_code, result.session_id, result.agent_id).pack(w),
        reliable=True)
    # CompleteAgentMovement: AgentID, SessionID, CircuitCode.
    circuit.send_message("CompleteAgentMovement", lambda w: CompleteAgentMovement(
        result.agent_id, result.session_id, result.circuit_code).pack(w),
        reliable=True)
    return result, caps, circuit
```

## 8. A TestClient-style bot

Modelled on LibreMetaverse's TestClient: log in, say what you hear, answer IMs with a canned reply, follow simple chat commands (`follow`, `stay`, `logout`), and log out cleanly. Object/chat message bodies below use the hand-written field order from the current template — verify against your generated classes (section 4) when the template revs.

```python
"""bot.py — a minimal in-world bot on the circuit + caps stack above."""

CHAT_TYPE_NORMAL = 0
CHAT_SOURCE_AGENT = 2


def pack_chat_from_viewer(text: str, channel: int = 0, chat_type: int = CHAT_TYPE_NORMAL):
    """ChatFromViewer: AgentData(AgentID, SessionID), ChatData(Message, Type, Channel).
    NOTE: ChatFromViewer is the documented case where the master template's
    zerocoded flag was wrong — the session's template table, built from the
    viewer's copy, decides encoding in send_message; do not hardcode it."""
    def _pack(w: BodyWriter):
        # AgentData block is filled by the session layer in real code; here
        # the bot's session injects IDs via closure in run_bot below.
        raise NotImplementedError
    return _pack


class Bot:
    def __init__(self, first: str, last: str):
        self.name = f"{first} {last}"
        self.login_result: LoginResult | None = None
        self.circuit: Circuit | None = None
        self.caps: CapsClient | None = None
        self.event_queue: EventQueue | None = None
        self.maintenance_task: asyncio.Task | None = None
        self.eq_task: asyncio.Task | None = None
        self.heard: list[tuple[str, str]] = []   # (from name, text) chat log

    # -- inbound ------------------------------------------------------------
    def on_message(self, name: str, reader: BodyReader, packet: Packet) -> None:
        handler = getattr(self, f"msg_{name}", None)
        if handler:
            handler(reader, packet)

    def msg_RegionHandshake(self, reader: BodyReader, packet: Packet) -> None:
        # RegionData: RegionFlags U32, SimAccess U8, SimName Variable 1,
        # SimOwner LLUUID, IsEstateManager BOOL, WaterHeight F32,
        # BillOverFactor F32, CacheID LLUUID, TerrainBase0..3, TerrainDetail0..1,
        # TerrainStartHeight00..11, TerrainHeightRange00..11 (all LLUUID/F32).
        # A bot does not need most of it — but it MUST reply, or the
        # simulator never finishes putting the agent in-world.
        region_flags = reader.u32()
        reader.u8()                      # SimAccess
        sim_name = reader.string_z()
        reader.uuid()                    # SimOwner
        reader.boolean()                 # IsEstateManager
        reader.f32(); reader.f32()       # WaterHeight, BillOverFactor
        reader.uuid()                    # CacheID
        for _ in range(4 + 2 + 4 + 4):   # terrain UUIDs + heights
            reader.take(16) if _ < 6 else reader.f32()
        lr = self.login_result
        # RegionHandshakeReply: AgentData(AgentID, SessionID),
        # RegionInfo(RegionFlags U32, SimAccess U8, SimName, SimOwner,
        # IsEstateManager, WaterHeight, BillOverFactor, CacheID, 6 terrain UUIDs)
        # For a bot, echoing the handshake values back is the accepted pattern
        # (TestClient does the equivalent through LibreMetaverse managers).
        self._reply_handshake(region_flags, sim_name)

    def _reply_handshake(self, region_flags: int, sim_name: str) -> None:
        lr = self.login_result
        def _pack(w: BodyWriter):
            w.uuid(lr.agent_id).uuid(lr.session_id)
            w.u32(region_flags).u8(0).string_z(sim_name)
            w.uuid(uuid.UUID(int=0)).boolean(False)
            w.f32(20.0).f32(1.0).uuid(uuid.UUID(int=0))
            for _ in range(6):
                w.uuid(uuid.UUID(int=0))
        self.circuit.send_message("RegionHandshakeReply", _pack, reliable=True)

    def msg_ChatFromSimulator(self, reader: BodyReader, packet: Packet) -> None:
        # ChatData: FromName Variable 1, SourceID LLUUID, OwnerID LLUUID,
        # SourceType U8, ChatType U8, Audible U8, SourcePos LLVector3,
        # Message Variable 2.
        from_name = reader.string_z()
        reader.uuid(); reader.uuid()
        source_type = reader.u8()
        reader.u8(); reader.u8()
        reader.vector3()
        message = reader.variable2().split(b"\x00", 1)[0].decode("utf-8", "replace")
        if source_type == CHAT_SOURCE_AGENT and from_name != self.name:
            self.heard.append((from_name, message))
            print(f"[chat] {from_name}: {message}")
            self._chat_command(from_name, message)

    def _chat_command(self, from_name: str, message: str) -> None:
        cmd = message.strip().lower()
        if cmd == "ping":
            self.say("pong")
        elif cmd.startswith("echo "):
            self.say(message[5:])

    # -- outbound -------------------------------------------------------------
    def say(self, text: str, channel: int = 0) -> None:
        lr = self.login_result
        def _pack(w: BodyWriter):
            w.uuid(lr.agent_id).uuid(lr.session_id)
            w.variable2(text.encode("utf-8") + b"\x00")  # Message (Variable 2 in ChatFromViewer is Message, Type, Channel order below)
            w.u8(CHAT_TYPE_NORMAL)
            w.s32(channel)
        # Field order for ChatFromViewer ChatData is: Message, Type, Channel.
        self.circuit.send_message("ChatFromViewer", _pack, category="task")

    def on_event(self, message: str, body: dict) -> None:
        # Event Queue events a bot typically cares about: teleport offers
        # (TeleportOffer / Lure), inventory offers, group notices,
        # ChatterBoxInvitation for group chat sessions.
        if message in ("TeleportOffer", "Lure"):
            print(f"[eq] teleport lure: {body}")
        elif message == "ChatterBoxInvitation":
            print(f"[eq] group chat invitation: {body.get('session_id')}")

    # -- lifecycle --------------------------------------------------------------
    async def run(self, login_uri: str, password: str, template) -> None:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0, read=75.0)) as http:
            # EventQueue long-polls can block ~50s server-side; the read
            # timeout above must exceed that or every poll looks like an error.
            self.login_result, self.caps, self.circuit = await bootstrap_session(
                http, login_uri, *self.name.split(" ", 1), password, template,
                self.on_message)
            self.circuit.on_message = self.on_message
            self.maintenance_task = asyncio.create_task(self.circuit.run_maintenance())
            self.event_queue = EventQueue(self.caps, self.on_event)
            self.eq_task = asyncio.create_task(self.event_queue.run())
            print(f"[bot] logged in as {self.name}")
            try:
                await self.maintenance_task  # returns when the circuit dies
            finally:
                await self.logout()

    async def logout(self) -> None:
        if self.event_queue:
            self.event_queue.stop()
        if self.circuit and not self.circuit.closed:
            lr = self.login_result
            def _pack(w: BodyWriter):
                w.uuid(lr.agent_id).uuid(lr.session_id)
            try:
                self.circuit.send_message("LogoutRequest", _pack, reliable=True)
                await asyncio.sleep(0.3)  # let the packet + ACKs flush
            finally:
                self.circuit.transport.close()
                self.circuit.closed = True
        for task in (self.eq_task, self.maintenance_task):
            if task and not task.done():
                task.cancel()


async def main() -> None:
    template_text = open("message_template.msg", encoding="utf-8").read()
    template = TemplateParser(template_text).parse()
    bot = Bot("Test", "Bot")
    await bot.run(OPENSIM_LOGIN_URI, "password-from-env-not-source", template)


if __name__ == "__main__":
    codec_self_test()
    asyncio.run(main())
```

---

## 9. Worked examples on top of the stack

### 9.1 Fetching inventory with FetchInventory2 / AIS3 thinking

HTTP inventory returns LLSD. A folder fetch is a map with `agent_id` and `folder_id`; the reply carries `folders` and `items` arrays whose entries are LLSD maps with `item_id`, `parent_id`, `name`, `type` (inventory type), `asset_id`, and permission blocks. AIS3 (`InventoryAPIv3`) is the write path — create/update/link as LLSD PUT/POST-style cap calls with Current Outfit Folder versioning — while Fetch* caps are the read path. Mixing them up (trying to write via Fetch, or read via legacy UDP as the primary path) is the most common inventory bug in new clients; the viewer checks AIS first (`llaisapi.cpp`), and so should you.

```python
async def fetch_folder(caps: CapsClient, agent_id: uuid.UUID,
                       folder_id: uuid.UUID) -> dict:
    """One FetchInventoryDescendents2 call. Returns {'folders': [...], 'items': [...]}
    with UUIDs still as strings — convert at your model layer, not here."""
    reply = await caps.post_llsd("FetchInventoryDescendents2", {
        "agent_id": agent_id,
        "folder_id": folder_id,
        "owner_id": agent_id,
        "sort_order": 0,          # by name
        "fetch_folders": True,
        "fetch_items": True,
        "fetch_links": True,
    })
    return reply or {}


async def walk_inventory(caps: CapsClient, agent_id: uuid.UUID,
                         root_id: uuid.UUID, max_depth: int = 6):
    """Depth-first inventory walk yielding (depth, folder_or_item_map).
    Inventory trees are user data and can be enormous (100k+ items on old
    accounts): this is a generator on purpose. Never materialise a whole
    inventory to answer a question about one folder."""
    stack = [(root_id, 0)]
    while stack:
        folder_id, depth = stack.pop()
        reply = await fetch_folder(caps, agent_id, folder_id)
        for item in reply.get("items", []) or []:
            yield depth, item
        if depth < max_depth:
            for folder in reply.get("folders", []) or []:
                yield depth, folder
                stack.append((uuid.UUID(folder["folder_id"]), depth + 1))
```

### 9.2 Decoding a terse object update (why avatars jitter when you get this wrong)

`ImprovedTerseObjectUpdate` packs position, velocity, acceleration, rotation, and angular velocity in a compressed, quantised form. Two traps account for nearly all "my port jitters / sinks into the floor" bugs: the position is relative to a per-message reference and scaled, and the rotation omits W (section 3.1). The decoder skeleton below shows the field order and the quantisation shape; the exact scale factors live in the viewer's `lldatapacker` / message handling and in LibreMetaverse's terse-update code — copy those constants from source for the template revision you target, do not tune them by eye.

```python
def decode_terse_block(reader: BodyReader) -> dict:
    """One ObjectData block of ImprovedTerseObjectUpdate, schematic form.
    Block layout (template): ObjectLocalID U32, State U8, Avatar flag in
    state bits, then a Variable 1 'Data' blob holding the packed terse
    fields, followed by texture/animation variable blocks in some revisions."""
    local_id = reader.u32()
    state = reader.u8()
    data = reader.variable1()
    inner = BodyReader(data)
    # Packed terse payload, in order (see viewer llviewerobject handling):
    # position (3 x U16 quantised over the region, or F32 in the avatar
    # variant), velocity (3 x S16 scaled), acceleration (3 x S16 scaled),
    # rotation (4 x S16 normalised, W present in this packing), angular
    # velocity (3 x S16 scaled). The avatar/attachment state bits change
    # which variant you are reading — branch on `state`, never on guesswork.
    return {"local_id": local_id, "state": state, "raw": data,
            "note": "decode per viewer llviewerobject / LibreMetaverse terse code"}
```

### 9.3 Teleport: the session-layer view

A teleport is not a message, it is a sequence across both planes: a lure or a `TeleportRequest`, simulator-side `TeleportStart` → `TeleportProgress` (zero or more, with messages) → on success a new region's caps + circuit (your seed-cap-derived map and UDP peer **both change**), `TeleportFinish` carrying the new sim IP/port and a new seed capability, then `UseCircuitCode`/`CompleteAgentMovement` on the new circuit and an `AgentMovementComplete`-era handshake — while the old circuit gets `CloseCircuit`. In code terms: everything in `Bot.run` from `bootstrap_session` onward must be re-runnable against a new (sim_ip, sim_port, seed_capability) triple, and the Event Queue must be restarted because its URL belonged to the old region. Structure session code as "connect to a region" called repeatedly, not as "log in once".

```python
async def reconnect_to_region(bot: Bot, http, finish_body: dict, template) -> None:
    """Sketch: TeleportFinish body fields (LLSD-ish over UDP in the real
    message) give SimIP, SimPort, SeedCapability, RegionX/RegionY.
    The bot tears down the old EQ + circuit and bootstraps the new region
    with the SAME agent/session IDs and the NEW circuit code from the
    finish message. Getting the circuit code from the old session instead
    is the classic 'teleport lands but nothing loads' bug."""
    if bot.event_queue:
        bot.event_queue.stop()
    if bot.circuit and not bot.circuit.closed:
        bot.circuit.transport.close()
        bot.circuit.closed = True
    # ... rebuild caps from finish_body['SeedCapability'], open a new
    # datagram endpoint to (finish_body['SimIP'], finish_body['SimPort']),
    # send UseCircuitCode + CompleteAgentMovement, restart maintenance + EQ.
    raise NotImplementedError("wire to your session manager")
```

## 10. Testing, packaging, and pitfalls

```text
# requirements.txt for everything in this file
httpx>=0.27
# No other runtime deps: the LLSD codec, zerocode, template parser, and
# circuit are stdlib-only (asyncio, struct, xml, hashlib) on purpose.
```

- **Test the codecs against llbase.** `codec_self_test()` above is necessary, not sufficient: add a differential test that feeds the same values through `llbase.llsd` (XML and binary) and compares bytes. Date and binary fields are where hand-rolled codecs drift first.
- **Test the template parser against counts.** The current master template parses to roughly 480 messages; assert the count and assert known anchors (`PacketAck` is Fixed `0xFFFFFFFB`, `UseCircuitCode` is Low 4) in CI so a bad template drop fails loudly.
- **Never test a new circuit against Agni first.** Local OpenSim standalone gives you a server you can breakpoint; Aditi gives you Linden Lab's real stack without production consequences. A ghosting bug (missed ACKs, no `CloseCircuit`) on Agni leaves your avatar in-world.
- **Passwords and session IDs are secrets.** The login request contains a password hash that is password-equivalent for login purposes. Do not log requests, do not put credentials in source (the bot above takes a placeholder for exactly this reason), and do not persist cap URLs or session IDs to disk.
- **UDP on real networks.** Keep bodies small, expect loss and reordering (object updates are latest-wins — do not queue them), and expect NAT timeouts on mobile links: the ping sweep in section 5 is load-bearing, not decoration.
- **OpenSim is not Agni.** Caps granted, template flags honoured, and throttle behaviour all differ in detail. Code that "works on my OpenSim" still needs an Aditi pass before it is Second Life code.


## 11. AgentUpdate, IM, and group chat — the remaining session loops

### 11.1 AgentUpdate is a heartbeat, not an event

The simulator expects a continuous stream of `AgentUpdate` messages (camera position/look-at, body rotation, control flags, state flags) at roughly 10 Hz while in-world, throttled by the `task`/`resend` buckets. Stop sending it and the simulator concludes the agent is idle-then-gone; send it from a blocking loop and you starve your own receive path. It belongs in its own asyncio task, reading the latest desired camera/agent state from a shared object (latest-wins, never a queue).

```python
CONTROL_AT_POS = 0x00000001      # W / up arrow
CONTROL_AT_NEG = 0x00000002      # S / down arrow
CONTROL_LEFT_POS = 0x00000004    # A / rotate-left family — see template/viewer
CONTROL_LEFT_NEG = 0x00000008
CONTROL_UP_POS = 0x00000010      # E / page-up (fly up)
CONTROL_UP_NEG = 0x00000020      # C / page-down
CONTROL_FAST_AT = 0x00000100
CONTROL_FLY = 0x00000800
# Full flag table: viewer llagent / LLAgent::controlFlags and the AgentUpdate
# handling in the simulator. Treat this subset as illustrative.

AGENT_STATE_NONE = 0x00
AGENT_STATE_TYPING = 0x04        # shows the typing animation to others


class AgentState:
    """Mutable desired state, written by command handlers, read by the
    AgentUpdate loop. Plain attributes, no locks: asyncio is single-threaded
    and each loop iteration reads a consistent-enough snapshot."""

    def __init__(self, agent_id, session_id):
        self.agent_id = agent_id
        self.session_id = session_id
        self.body_rotation = (0.0, 0.0, 0.0, 1.0)     # quaternion x,y,z,w
        self.head_rotation = (0.0, 0.0, 0.0, 1.0)
        self.camera_center = (128.0, 128.0, 20.0)     # region-local metres
        self.camera_at = (1.0, 0.0, 0.0)
        self.camera_left = (0.0, 1.0, 0.0)
        self.camera_up = (0.0, 0.0, 1.0)
        self.far = 128.0
        self.control_flags = 0
        self.state_flags = AGENT_STATE_NONE


def pack_agent_update(state: AgentState):
    def _pack(w: BodyWriter):
        w.uuid(state.agent_id).uuid(state.session_id)
        w.quaternion(state.body_rotation).quaternion(state.head_rotation)
        w.u8(state.state_flags)
        w.vector3(state.camera_center)
        w.vector3(state.camera_at).vector3(state.camera_left).vector3(state.camera_up)
        w.f32(state.far)
        w.u32(state.control_flags)
        w.u8(0)  # Flags (HideTitle group bit etc. — see template)
    return _pack


async def agent_update_loop(circuit: Circuit, state: AgentState,
                            interval: float = 0.1) -> None:
    """10 Hz AgentUpdate task. Runs until the circuit closes."""
    while not circuit.closed:
        circuit.send_message("AgentUpdate", pack_agent_update(state),
                             category="task")
        await asyncio.sleep(interval)
```

### 11.2 Instant messages: ImprovedInstantMessage

IM is one message type carrying many dialog codes (message, inventory offer, teleport offer, group notice, session start…). The fields that matter for a bot: `AgentData(AgentID, SessionID)`, `MessageBlock(FromAgentName Variable 1, ToAgentID, ParentEstateID, RegionID, Position, Offline, Dialog, ID (session/message UUID), Timestamp, Message Variable 2, BinaryBucket Variable 2)`. `Offline=1` means the simulator stored it while you were away — those arrive in a burst at login and must not be treated as live conversation for rate-limiting or auto-reply purposes (replying to a week-old offline IM burst is how bots get muted).

```python
IM_DIALOG_MESSAGE = 0
IM_DIALOG_INVENTORY_OFFERED = 3
IM_DIALOG_INVENTORY_ACCEPTED = 4
IM_DIALOG_INVENTORY_DECLINED = 5
IM_DIALOG_GROUP_NOTICE = 7
IM_DIALOG_TELEPORT_OFFER = 13     # (dialog values per template/viewer llmessage)
IM_DIALOG_SESSION_GROUP_START = 15
IM_DIALOG_SESSION_CONFERENCE_START = 16
IM_DIALOG_SESSION_SEND = 17


def pack_im(state: AgentState, to_agent: uuid.UUID, text: str,
            dialog: int = IM_DIALOG_MESSAGE,
            session_id: uuid.UUID | None = None) -> callable:
    """For 1:1 IM, the session ID is derived from the two agent IDs
    (the well-known XOR/pairing convention used by viewers); for group and
    conference sessions it is the session's own UUID from ChatSessionRequest
    or the invitation event. Getting this wrong delivers your message to a
    session nobody is listening to — silently."""
    sid = session_id or state.agent_id  # placeholder: use the pairing rule in real code
    def _pack(w: BodyWriter):
        w.uuid(state.agent_id).uuid(state.session_id)
        w.variable1(b"")                       # FromGroup? see template order below
        w.uuid(to_agent)
        w.u32(0)                               # ParentEstateID
        w.uuid(uuid.UUID(int=0))               # RegionID (0 = not region-scoped)
        w.vector3((0.0, 0.0, 0.0))            # Position
        w.u8(0)                                # Offline: 0 = deliver/store by server rules
        w.u8(dialog)
        w.uuid(sid)                            # ID: session / transaction id
        w.u32(int(time.time()))                # Timestamp
        w.string_z("PythonBot")                # FromAgentName
        w.variable2(text.encode("utf-8") + b"\x00")  # Message
        w.variable2(b"")                       # BinaryBucket (dialog-specific payload)
    return _pack
```

Field-order warning, stated once and applicable everywhere in this file: the pack functions above follow the current template's block/field order for their messages. When you adopt this code, generate the same messages with section 4's generator and diff the bytes on a local OpenSim login — byte-diffing one known-good capture is worth more than re-reading any prose description, including this one.

### 11.3 Group chat sessions via caps

Group chat does not ride plain IM to the group UUID. The flow is: POST `ChatSessionRequest` (LLSD: `{'method': 'start conference'|'start session', 'session-id': <group or session UUID>, 'params': …}` — exact body per viewer `llimpanel` / LibreMetaverse `InstantMessage` handling) → the simulator creates the session and invites members → messages then flow as `ImprovedInstantMessage` with the session dialog codes and as Event Queue `ChatterBox*` events for membership changes. A client that sends IM straight at the group ID and waits will wait forever; a client that ignores `ChatterBoxSessionStartReply` / error events cannot tell a dead session from a quiet one. Handle at minimum: invitation (join or decline by policy), session start reply (record the session ID), member added/removed events (maintain the roster), and session error (drop the session, do not retry in a tight loop).

```python
async def start_group_session(caps: CapsClient, group_id: uuid.UUID) -> dict | None:
    """Ask the simulator to start (or join) the group chat session.
    Returns the LLSD reply map, or None if the region granted no cap —
    in which case group chat is unavailable in this region, full stop."""
    if not caps.has("ChatSessionRequest"):
        return None
    reply = await caps.post_llsd("ChatSessionRequest", {
        "method": "start session",
        "session-id": group_id,
    })
    return reply if isinstance(reply, dict) else None
```

## 12. Error taxonomy for the whole stack

Keep these failure classes distinct in logs and UI; collapsing them is what makes Second Life client bugs undebuggable:

- **Codec errors** (`LLSDParseError`, body truncation): the peer sent bytes that do not parse. Log a hex prefix and the cap/message name. Never include session IDs or cap URLs in the log line.
- **Template drift**: a message ID or cap that your template/code does not know. Normal across grid updates — degrade (skip the message, note the missing cap), do not crash.
- **Transport death**: circuit timeout, ICMP errors, EQ error IDs. Owned by the session layer: full region reconnect (section 9.3), not by retrying the single failed call.
- **Auth/session errors**: login `reason` values, MFA challenges, `LogoutRequest` races. Surface to the user verbatim; automated retry of a failed login is both futile and a good way to get rate-limited.
- **Grid differences**: a call that works on OpenSim and fails on Aditi/Agni (or the reverse). Record which grid every bug report came from — "Second Life" is three different servers in this workflow (your OpenSim, Aditi, Agni), and a report that does not say which one is not actionable.

## 13. Minimal end-to-end smoke script

The smallest useful integration test: log in to a local OpenSim, fetch caps, sit in-world for ten seconds counting object updates and chat, log out. Run this before and after any change to sections 1–6; if it regresses, nothing else matters yet.

```python
"""smoke.py — login, count traffic for 10 s, logout. Exit code = success."""
import collections
import os
import sys


async def smoke() -> int:
    template = TemplateParser(open("message_template.msg").read()).parse()
    counts: collections.Counter = collections.Counter()

    def counting_handler(name, reader, packet):
        counts[name] += 1

    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0, read=75.0)) as http:
        result, caps, circuit = await bootstrap_session(
            http,
            os.environ.get("SL_LOGIN_URI", OPENSIM_LOGIN_URI),
            os.environ["SL_FIRST"], os.environ["SL_LAST"],
            os.environ["SL_PASSWORD"], template, counting_handler,
        )
        print(f"caps granted: {len(caps.caps)} "
              f"(EventQueueGet={'EventQueueGet' in caps.caps})")
        maint = asyncio.create_task(circuit.run_maintenance())
        eq = EventQueue(caps, lambda m, b: counts[f"EQ:{m}"] + 0)
        eq_task = asyncio.create_task(eq.run())
        await asyncio.sleep(10)
        eq.stop()
        # Clean logout: LogoutRequest is AgentData only.
        def _logout(w: BodyWriter):
            w.uuid(result.agent_id).uuid(result.session_id)
        circuit.send_message("LogoutRequest", _logout, reliable=True)
        await asyncio.sleep(0.3)
        circuit.transport.close()
        circuit.closed = True
        maint.cancel(); eq_task.cancel()
    top = counts.most_common(8)
    print("top traffic:", top)
    # A healthy in-world idle should at least see object updates or pings.
    return 0 if counts else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(smoke()))
```

Credentials come from the environment (`SL_FIRST`, `SL_LAST`, `SL_PASSWORD`, `SL_LOGIN_URI`) — never from source, never from a committed `.env`. That rule is not style; login hashes are password-equivalent, and a skills repo is exactly the kind of repo that gets cloned widely.
