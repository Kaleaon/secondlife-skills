# Second Life in Go — LLSD, Zerocode, UDP Circuit, Caps, and Login

> **What this ports, and from where.** A from-scratch Go implementation of the
> Second Life simulator protocol core, ported from the same canonical sources
> as the Rust companion (`code-rust.md`), in cross-check order:
>
> 1. **`secondlife/viewer` (LGPL-2.1)** — `indra/llcommon/llsdserialize.cpp` for
>    LLSD semantics, `indra/llmessage` circuit behaviour, and
>    `indra/newview/llviewerregion.cpp` for capability names.
> 2. **`secondlife/master-message-template`** — `message_template.msg`; the
>    message registry in Part 8 is generated from it (483 messages, 902 blocks,
>    2,984 fields at generation time).
> 3. **`cinderblocks/libremetaverse` (BSD-3)** — `LibreMetaverse.StructuredData`,
>    `.Transport`, and `.Protocol` as the reference implementation whose
>    behaviour this code mirrors.
> 4. **`bennettgoble/go-llsd` (MIT)** — the existing Go LLSD library is the
>    conceptual starting point for the Go type mapping (`interface{}`-based
>    values), but the code here is written fresh: it uses a typed `Value`
>    struct instead, because untyped `interface{}` LLSD makes the
>    integer/real distinction — which the simulator *does* enforce — too easy
>    to lose. If you only need LLSD parsing in production Go, evaluate go-llsd
>    first; use this file when you need the full protocol stack and the
>    teaching detail.
>
> **Layout.** Part 1 `go.mod`. Part 2 core types (UUID, vectors, quaternion).
> Part 3 the LLSD `Value` type. Part 4 LLSD XML marshal/unmarshal. Part 5 LLSD
> binary marshal/unmarshal. Part 6 zerocode + packet header + message IDs.
> Part 7 the circuit over `net.UDPConn`. Part 8 the generated message registry.
> Part 9 caps client, login request/response, and the EventQueueGet goroutine.
> Part 10 tests and a runnable main skeleton.

---

## Part 1 — go.mod

```go
module slproto

go 1.22

// No third-party dependencies. LLSD XML is handled with encoding/xml plus a
// small hand-rolled reader for the parts encoding/xml cannot express (LLSD's
// alternating <key>/value map children). Keeping the dependency list empty is
// deliberate for a protocol library: every dependency is a supply-chain and
// version-skew risk against a simulator that never changes its formats.
```

Package layout in a real repo: everything below lives in `package slproto`
except the Part 10 main skeleton, which is `package main` in `cmd/slbot`.

---

## Part 2 — Core types

```go
package slproto

import (
	"encoding/binary"
	"fmt"
	"math"
	"net"
	"strings"
)

// UUID is a Second Life UUID: 16 raw bytes, wire order == hex string order.
// Do NOT convert through any GUID type that reorders fields.
type UUID [16]byte

// ZeroUUID is the all-zeroes UUID ("NULL_KEY" in LSL terms).
var ZeroUUID UUID

// ParseUUID accepts the hyphenated form or bare 32-hex form.
func ParseUUID(s string) (UUID, error) {
	hex := strings.ReplaceAll(strings.TrimSpace(s), "-", "")
	if len(hex) != 32 {
		return ZeroUUID, fmt.Errorf("uuid: want 32 hex digits, got %d", len(hex))
	}
	var u UUID
	for i := 0; i < 16; i++ {
		var v int
		_, err := fmt.Sscanf(hex[2*i:2*i+2], "%02x", &v)
		if err != nil {
			return ZeroUUID, fmt.Errorf("uuid: bad hex at byte %d: %w", i, err)
		}
		u[i] = byte(v)
	}
	return u, nil
}

func (u UUID) String() string {
	return fmt.Sprintf("%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x",
		u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12], u[13], u[14], u[15])
}

func (u UUID) IsZero() bool { return u == ZeroUUID }

// Vector3 is the template's LLVector3: three little-endian float32s on the wire.
type Vector3 struct{ X, Y, Z float32 }

func (v Vector3) Length() float32 {
	return float32(math.Sqrt(float64(v.X*v.X + v.Y*v.Y + v.Z*v.Z)))
}

func (v Vector3) Normalized() Vector3 {
	l := v.Length()
	if l == 0 {
		return Vector3{}
	}
	return Vector3{v.X / l, v.Y / l, v.Z / l}
}

func (v Vector3) Dot(o Vector3) float32 { return v.X*o.X + v.Y*o.Y + v.Z*o.Z }

func (v Vector3) Cross(o Vector3) Vector3 {
	return Vector3{v.Y*o.Z - v.Z*o.Y, v.Z*o.X - v.X*o.Z, v.X*o.Y - v.Y*o.X}
}

func (v Vector3) MarshalLE() [12]byte {
	var out [12]byte
	binary.LittleEndian.PutUint32(out[0:4], math.Float32bits(v.X))
	binary.LittleEndian.PutUint32(out[4:8], math.Float32bits(v.Y))
	binary.LittleEndian.PutUint32(out[8:12], math.Float32bits(v.Z))
	return out
}

func UnmarshalVector3LE(b []byte) (Vector3, error) {
	if len(b) < 12 {
		return Vector3{}, fmt.Errorf("vector3: need 12 bytes, have %d", len(b))
	}
	return Vector3{
		math.Float32frombits(binary.LittleEndian.Uint32(b[0:4])),
		math.Float32frombits(binary.LittleEndian.Uint32(b[4:8])),
		math.Float32frombits(binary.LittleEndian.Uint32(b[8:12])),
	}, nil
}

// Vector3d is LLVector3d (global coordinates): three float64s.
type Vector3d struct{ X, Y, Z float64 }

func (v Vector3d) MarshalLE() [24]byte {
	var out [24]byte
	binary.LittleEndian.PutUint64(out[0:8], math.Float64bits(v.X))
	binary.LittleEndian.PutUint64(out[8:16], math.Float64bits(v.Y))
	binary.LittleEndian.PutUint64(out[16:24], math.Float64bits(v.Z))
	return out
}

// Quaternion is sent on the wire as three float32s (x, y, z); w is rebuilt as
// sqrt(1-x²-y²-z²), clamped the way the viewer clamps it.
type Quaternion struct{ X, Y, Z, W float32 }

var IdentityQuaternion = Quaternion{0, 0, 0, 1}

func (q Quaternion) Normalized() Quaternion {
	l := math.Sqrt(float64(q.X*q.X + q.Y*q.Y + q.Z*q.Z + q.W*q.W))
	if l == 0 {
		return IdentityQuaternion
	}
	f := float32(l)
	return Quaternion{q.X / f, q.Y / f, q.Z / f, q.W / f}
}

// QuaternionFromWire builds a quaternion from the 3-float wire form.
func QuaternionFromWire(x, y, z float32) Quaternion {
	sum := x*x + y*y + z*z
	if sum >= 1 {
		l := float32(math.Sqrt(float64(sum)))
		return Quaternion{x / l, y / l, z / l, 0}
	}
	return Quaternion{x, y, z, float32(math.Sqrt(float64(1 - sum)))}
}

// Wire returns the 3-float wire form, flipping sign if w < 0 (q and -q are
// the same rotation; decode assumes the non-negative root).
func (q Quaternion) Wire() (float32, float32, float32) {
	n := q.Normalized()
	if n.W < 0 {
		return -n.X, -n.Y, -n.Z
	}
	return n.X, n.Y, n.Z
}

// IP/port field helpers: the template's IPADDR is 4 bytes in *network* order
// as an IPv4 address, IPPORT is a big-endian uint16 — one of the few big-endian
// body fields. Getting these backwards produces a client that connects to a
// nonsense address only on some simulators, which is why they are isolated here.
func MarshalIPAddr(ip net.IP) [4]byte {
	var out [4]byte
	copy(out[:], ip.To4())
	return out
}

func MarshalIPPort(port uint16) [2]byte {
	var out [2]byte
	binary.BigEndian.PutUint16(out[:], port)
	return out
}
```

---

## Part 3 — The LLSD Value type

Go mapping decisions, stated once so the rest of the file is predictable:

* LLSD integers are **int32**. A Go `int` or `int64` field would silently
  accept values the simulator truncates. `KindInt` stores `int32`, always.
* LLSD reals are `float64`.
* Maps are `map[string]Value` plus a `Keys` slice is *not* kept: Go map
  iteration order is random, and LLSD does not require key order. Tests that
  compare XML byte-for-byte must sort keys — the XML writer below does.
* Undefined is a distinct kind, not `nil`, because a key present with an
  undefined value is different from an absent key in several caps payloads
  (notably EventQueueGet ack handling).

```go
// Kind enumerates the LLSD types.
type Kind int

const (
	KindUndefined Kind = iota
	KindBoolean
	KindInt
	KindReal
	KindString
	KindUUID
	KindDate // seconds since Unix epoch, fractional allowed
	KindURI
	KindBinary
	KindArray
	KindMap
)

func (k Kind) String() string {
	switch k {
	case KindUndefined:
		return "undefined"
	case KindBoolean:
		return "boolean"
	case KindInt:
		return "integer"
	case KindReal:
		return "real"
	case KindString:
		return "string"
	case KindUUID:
		return "uuid"
	case KindDate:
		return "date"
	case KindURI:
		return "uri"
	case KindBinary:
		return "binary"
	case KindArray:
		return "array"
	case KindMap:
		return "map"
	}
	return "unknown"
}

// Value is one LLSD value. Only the field matching Kind is meaningful.
type Value struct {
	Kind Kind
	Bool bool
	Int  int32
	Real float64
	Str  string // string, URI, and (as ISO text during XML parse) date source
	UUID UUID
	Date float64 // epoch seconds when Kind == KindDate
	Bin  []byte
	Arr  []Value
	Map  map[string]Value
}

// Constructors keep call sites short and make the kind impossible to mistype.
func Undefined() Value                 { return Value{Kind: KindUndefined} }
func Boolean(b bool) Value             { return Value{Kind: KindBoolean, Bool: b} }
func Int(i int32) Value                { return Value{Kind: KindInt, Int: i} }
func Real(r float64) Value             { return Value{Kind: KindReal, Real: r} }
func Str(s string) Value               { return Value{Kind: KindString, Str: s} }
func UUIDVal(u UUID) Value             { return Value{Kind: KindUUID, UUID: u} }
func DateVal(epoch float64) Value      { return Value{Kind: KindDate, Date: epoch} }
func URIVal(u string) Value            { return Value{Kind: KindURI, Str: u} }
func BinaryVal(b []byte) Value         { return Value{Kind: KindBinary, Bin: b} }
func ArrayVal(items ...Value) Value    { return Value{Kind: KindArray, Arr: items} }
func MapVal(pairs map[string]Value) Value {
	if pairs == nil {
		pairs = map[string]Value{}
	}
	return Value{Kind: KindMap, Map: pairs}
}

// Get returns the map entry for key, or (Undefined, false). Caps responses
// routinely omit keys on some simulator versions — always use Get, never
// index a map you received from the wire without checking.
func (v Value) Get(key string) (Value, bool) {
	if v.Kind != KindMap {
		return Undefined(), false
	}
	out, ok := v.Map[key]
	return out, ok
}

// AsString coerces string/URI values.
func (v Value) AsString() (string, bool) {
	switch v.Kind {
	case KindString, KindURI:
		return v.Str, true
	}
	return "", false
}

// AsBool accepts booleans and the integer 0/1 encoding the login response
// historically uses for some flags.
func (v Value) AsBool() (bool, bool) {
	switch v.Kind {
	case KindBoolean:
		return v.Bool, true
	case KindInt:
		return v.Int != 0, true
	}
	return false, false
}

func (v Value) AsInt() (int32, bool) {
	switch v.Kind {
	case KindInt:
		return v.Int, true
	case KindReal:
		if v.Real == math.Trunc(v.Real) && v.Real >= math.MinInt32 && v.Real <= math.MaxInt32 {
			return int32(v.Real), true
		}
	}
	return 0, false
}

func (v Value) AsUUID() (UUID, bool) {
	switch v.Kind {
	case KindUUID:
		return v.UUID, true
	case KindString:
		u, err := ParseUUID(v.Str)
		return u, err == nil
	}
	return ZeroUUID, false
}
```

---

## Part 4 — LLSD XML marshal / unmarshal

The wire form for login and most caps (`application/llsd+xml`). Writing uses a
`strings.Builder` directly — `encoding/xml` cannot express LLSD's map layout
without a thicket of custom types, and the output must be exact. Reading uses
`encoding/xml`'s token stream, which *can* express it: a `<map>` is a sequence
of `<key>` elements alternating with value elements.

```go
import (
	"encoding/base64"
	"encoding/xml"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func xmlEscapeText(s string) string {
	var b strings.Builder
	for _, r := range s {
		switch r {
		case '&':
			b.WriteString("&amp;")
		case '<':
			b.WriteString("&lt;")
		case '>':
			b.WriteString("&gt;")
		case '"':
			b.WriteString("&quot;")
		case '\'':
			b.WriteString("&apos;")
		default:
			// XML 1.0 forbids most C0 controls; the viewer strips them on
			// write. Chat-derived strings can contain them — match the viewer.
			if r < 0x20 && r != '\t' && r != '\n' && r != '\r' {
				continue
			}
			b.WriteRune(r)
		}
	}
	return b.String()
}

// DateToISO renders an LLSD date (epoch seconds) in the XML wire form.
func DateToISO(epoch float64) string {
	return time.Unix(int64(epoch), 0).UTC().Format("2006-01-02T15:04:05Z")
}

// ISOToDate parses the XML date form, with or without fractional seconds.
func ISOToDate(s string) (float64, error) {
	s = strings.TrimSpace(s)
	for _, layout := range []string{
		"2006-01-02T15:04:05.999999999Z07:00",
		"2006-01-02T15:04:05Z07:00",
	} {
		if t, err := time.Parse(layout, s); err == nil {
			return float64(t.Unix()) + float64(t.Nanosecond())/1e9, nil
		}
	}
	return 0, fmt.Errorf("llsd date: cannot parse %q", s)
}

// MarshalXML renders the full document: declaration, <llsd> root, one value.
func (v Value) MarshalXML() ([]byte, error) {
	var b strings.Builder
	b.WriteString("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<llsd>")
	if err := v.writeXML(&b); err != nil {
		return nil, err
	}
	b.WriteString("</llsd>")
	return []byte(b.String()), nil
}

func (v Value) writeXML(b *strings.Builder) error {
	switch v.Kind {
	case KindUndefined:
		b.WriteString("<undefined/>")
	case KindBoolean:
		if v.Bool {
			b.WriteString("<boolean>1</boolean>")
		} else {
			b.WriteString("<boolean>0</boolean>")
		}
	case KindInt:
		fmt.Fprintf(b, "<integer>%d</integer>", v.Int)
	case KindReal:
		r := v.Real
		if math.IsNaN(r) || math.IsInf(r, 0) {
			r = 0 // not representable; the viewer writes 0
		}
		fmt.Fprintf(b, "<real>%s</real>", strconv.FormatFloat(r, 'g', -1, 64))
	case KindString:
		fmt.Fprintf(b, "<string>%s</string>", xmlEscapeText(v.Str))
	case KindUUID:
		fmt.Fprintf(b, "<uuid>%s</uuid>", v.UUID)
	case KindDate:
		fmt.Fprintf(b, "<date>%s</date>", DateToISO(v.Date))
	case KindURI:
		fmt.Fprintf(b, "<uri>%s</uri>", xmlEscapeText(v.Str))
	case KindBinary:
		fmt.Fprintf(b, "<binary>%s</binary>", base64.StdEncoding.EncodeToString(v.Bin))
	case KindArray:
		b.WriteString("<array>")
		for _, item := range v.Arr {
			if err := item.writeXML(b); err != nil {
				return err
			}
		}
		b.WriteString("</array>")
	case KindMap:
		keys := make([]string, 0, len(v.Map))
		for k := range v.Map {
			keys = append(keys, k)
		}
		sort.Strings(keys) // deterministic output: diffable logs, golden tests
		b.WriteString("<map>")
		for _, k := range keys {
			fmt.Fprintf(b, "<key>%s</key>", xmlEscapeText(k))
			if err := v.Map[k].writeXML(b); err != nil {
				return err
			}
		}
		b.WriteString("</map>")
	default:
		return fmt.Errorf("llsd xml: unhandled kind %v", v.Kind)
	}
	return nil
}

// UnmarshalXML parses an LLSD XML document.
func UnmarshalXML(data []byte) (Value, error) {
	dec := xml.NewDecoder(strings.NewReader(string(data)))
	// Find the <llsd> start element, tolerating the XML declaration and
	// comments before it (the decoder surfaces them as ProcInst/Comment).
	for {
		tok, err := dec.Token()
		if err != nil {
			return Undefined(), fmt.Errorf("llsd xml: %w", err)
		}
		if se, ok := tok.(xml.StartElement); ok {
			if se.Name.Local != "llsd" {
				return Undefined(), fmt.Errorf("llsd xml: root is <%s>, want <llsd>", se.Name.Local)
			}
			break
		}
	}
	v, err := parseXMLValue(dec)
	if err != nil {
		return Undefined(), err
	}
	return v, nil
}

// errEndOfContainer is returned by parseXMLValue when it meets the end
// element that closes the container it was called from (</array>, </map>,
// or </llsd>). Container loops treat it as "done", not as an error.
var errEndOfContainer = fmt.Errorf("llsd xml: end of container")

// parseXMLValue reads one value element from the token stream.
func parseXMLValue(dec *xml.Decoder) (Value, error) {
	for {
		tok, err := dec.Token()
		if err != nil {
			return Undefined(), err
		}
		switch tok := tok.(type) {
		case xml.EndElement:
			return Undefined(), errEndOfContainer
		case xml.StartElement:
			se := tok
			switch se.Name.Local {
			case "undefined", "undef": // older OpenSim emits <undef/> in places
				if err := skipXMLValue(dec, se.Name.Local); err != nil {
					return Undefined(), err
				}
				return Undefined(), nil
			case "boolean":
				s, err := xmlText(dec, "boolean")
				if err != nil {
					return Undefined(), err
				}
				return Boolean(s == "1" || strings.EqualFold(s, "true")), nil
			case "integer":
				s, err := xmlText(dec, "integer")
				if err != nil {
					return Undefined(), err
				}
				n, err := strconv.ParseInt(strings.TrimSpace(s), 10, 32)
				if err != nil {
					return Undefined(), fmt.Errorf("llsd xml: bad integer %q", s)
				}
				return Int(int32(n)), nil
			case "real":
				s, err := xmlText(dec, "real")
				if err != nil {
					return Undefined(), err
				}
				f, err := strconv.ParseFloat(strings.TrimSpace(s), 64)
				if err != nil {
					f = 0 // viewer emits "nan" on broken data; be lenient
				}
				return Real(f), nil
			case "string":
				s, err := xmlText(dec, "string")
				if err != nil {
					return Undefined(), err
				}
				return Str(s), nil
			case "uuid":
				s, err := xmlText(dec, "uuid")
				if err != nil {
					return Undefined(), err
				}
				u, _ := ParseUUID(s) // zero UUID on malformed input, like the viewer
				return UUIDVal(u), nil
			case "date":
				s, err := xmlText(dec, "date")
				if err != nil {
					return Undefined(), err
				}
				d, _ := ISOToDate(s)
				return DateVal(d), nil
			case "uri":
				s, err := xmlText(dec, "uri")
				if err != nil {
					return Undefined(), err
				}
				return URIVal(s), nil
			case "binary":
				s, err := xmlText(dec, "binary")
				if err != nil {
					return Undefined(), err
				}
				raw, err := base64.StdEncoding.DecodeString(strings.Join(strings.Fields(s), ""))
				if err != nil {
					return Undefined(), fmt.Errorf("llsd xml: bad base64: %w", err)
				}
				return BinaryVal(raw), nil
			case "array":
				var items []Value
				for {
					item, err := parseXMLValue(dec)
					if err == errEndOfContainer {
						return ArrayVal(items...), nil
					}
					if err != nil {
						return Undefined(), err
					}
					items = append(items, item)
				}
			case "map":
				m := map[string]Value{}
				for {
					ktok, err := dec.Token()
					if err != nil {
						return Undefined(), err
					}
					switch kt := ktok.(type) {
					case xml.EndElement:
						return MapVal(m), nil
					case xml.StartElement:
						if kt.Name.Local != "key" {
							return Undefined(), fmt.Errorf("llsd xml: expected <key> in <map>, got <%s>", kt.Name.Local)
						}
						key, err := xmlText(dec, "key")
						if err != nil {
							return Undefined(), err
						}
						val, err := parseXMLValue(dec)
						if err != nil {
							return Undefined(), err
						}
						m[key] = val
					}
				}
			default:
				return Undefined(), fmt.Errorf("llsd xml: unknown tag <%s>", se.Name.Local)
			}
		}
	}
}

// xmlText reads character data up to the matching end element. Entity
// references are already decoded by encoding/xml.
func xmlText(dec *xml.Decoder, tag string) (string, error) {
	var b strings.Builder
	for {
		tok, err := dec.Token()
		if err != nil {
			return "", err
		}
		switch t := tok.(type) {
		case xml.CharData:
			b.Write([]byte(t))
		case xml.EndElement:
			if t.Name.Local == tag {
				return b.String(), nil
			}
			return "", fmt.Errorf("llsd xml: unexpected </%s> inside <%s>", t.Name.Local, tag)
		}
	}
}

func skipXMLValue(dec *xml.Decoder, tag string) error {
	_, err := xmlText(dec, tag)
	return err
}

```

---

## Part 5 — LLSD binary marshal / unmarshal

Binary LLSD: one marker byte per value; length-prefixed strings/keys/binary
use **big-endian** u32 counts (network order) — the one big-endian island in
an otherwise little-endian protocol. Markers: `!` undefined, `1`/`0` boolean,
`i` i32 BE, `r` f64 BE, `s` string, `u` UUID, `d` date, `l` URI, `b` binary,
`[`/`]` array, `{`/`}` map (entries: `k` + key + value).

```go
import (
	"bytes"
	"encoding/binary"
	"fmt"
	"math"
)

// MarshalBinary renders v in binary LLSD.
func (v Value) MarshalBinary() ([]byte, error) {
	var buf bytes.Buffer
	if err := v.writeBinary(&buf); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func writeBE32(buf *bytes.Buffer, n uint32) {
	var b [4]byte
	binary.BigEndian.PutUint32(b[:], n)
	buf.Write(b[:])
}

func writeLenPrefixed(buf *bytes.Buffer, data []byte) {
	writeBE32(buf, uint32(len(data)))
	buf.Write(data)
}

func (v Value) writeBinary(buf *bytes.Buffer) error {
	switch v.Kind {
	case KindUndefined:
		buf.WriteByte('!')
	case KindBoolean:
		if v.Bool {
			buf.WriteByte('1')
		} else {
			buf.WriteByte('0')
		}
	case KindInt:
		buf.WriteByte('i')
		writeBE32(buf, uint32(v.Int))
	case KindReal:
		buf.WriteByte('r')
		var b [8]byte
		binary.BigEndian.PutUint64(b[:], math.Float64bits(v.Real))
		buf.Write(b[:])
	case KindString:
		buf.WriteByte('s')
		writeLenPrefixed(buf, []byte(v.Str))
	case KindUUID:
		buf.WriteByte('u')
		buf.Write(v.UUID[:])
	case KindDate:
		buf.WriteByte('d')
		var b [8]byte
		binary.BigEndian.PutUint64(b[:], math.Float64bits(v.Date))
		buf.Write(b[:])
	case KindURI:
		buf.WriteByte('l')
		writeLenPrefixed(buf, []byte(v.Str))
	case KindBinary:
		buf.WriteByte('b')
		writeLenPrefixed(buf, v.Bin)
	case KindArray:
		buf.WriteByte('[')
		writeBE32(buf, uint32(len(v.Arr)))
		for _, item := range v.Arr {
			if err := item.writeBinary(buf); err != nil {
				return err
			}
		}
		buf.WriteByte(']')
	case KindMap:
		buf.WriteByte('{')
		writeBE32(buf, uint32(len(v.Map)))
		for k, val := range v.Map {
			buf.WriteByte('k')
			writeLenPrefixed(buf, []byte(k))
			if err := val.writeBinary(buf); err != nil {
				return err
			}
		}
		buf.WriteByte('}')
	default:
		return fmt.Errorf("llsd binary: unhandled kind %v", v.Kind)
	}
	return nil
}

type binReader struct {
	data []byte
	pos  int
}

func (r *binReader) take(n int) ([]byte, error) {
	if r.pos+n > len(r.data) {
		return nil, fmt.Errorf("llsd binary: truncated: need %d bytes, have %d", n, len(r.data)-r.pos)
	}
	out := r.data[r.pos : r.pos+n]
	r.pos += n
	return out, nil
}

func (r *binReader) byte() (byte, error) {
	b, err := r.take(1)
	if err != nil {
		return 0, err
	}
	return b[0], nil
}

func (r *binReader) u32be() (uint32, error) {
	b, err := r.take(4)
	if err != nil {
		return 0, err
	}
	return binary.BigEndian.Uint32(b), nil
}

func (r *binReader) lenPrefixed() ([]byte, error) {
	n, err := r.u32be()
	if err != nil {
		return nil, err
	}
	// Hostile-length guard: a corrupt caps response must not claim 4 GiB.
	if n > 64*1024*1024 {
		return nil, fmt.Errorf("llsd binary: length prefix %d exceeds 64 MiB guard", n)
	}
	return r.take(int(n))
}

func (r *binReader) value() (Value, error) {
	marker, err := r.byte()
	if err != nil {
		return Undefined(), err
	}
	switch marker {
	case '!':
		return Undefined(), nil
	case '1':
		return Boolean(true), nil
	case '0':
		return Boolean(false), nil
	case 'i':
		n, err := r.u32be()
		if err != nil {
			return Undefined(), err
		}
		return Int(int32(n)), nil
	case 'r':
		b, err := r.take(8)
		if err != nil {
			return Undefined(), err
		}
		return Real(math.Float64frombits(binary.BigEndian.Uint64(b))), nil
	case 's':
		b, err := r.lenPrefixed()
		if err != nil {
			return Undefined(), err
		}
		return Str(string(b)), nil
	case 'u':
		b, err := r.take(16)
		if err != nil {
			return Undefined(), err
		}
		var u UUID
		copy(u[:], b)
		return UUIDVal(u), nil
	case 'd':
		b, err := r.take(8)
		if err != nil {
			return Undefined(), err
		}
		return DateVal(math.Float64frombits(binary.BigEndian.Uint64(b))), nil
	case 'l':
		b, err := r.lenPrefixed()
		if err != nil {
			return Undefined(), err
		}
		return URIVal(string(b)), nil
	case 'b':
		b, err := r.lenPrefixed()
		if err != nil {
			return Undefined(), err
		}
		return BinaryVal(append([]byte(nil), b...)), nil
	case '[':
		count, err := r.u32be()
		if err != nil {
			return Undefined(), err
		}
		items := make([]Value, 0, count)
		for i := uint32(0); i < count; i++ {
			item, err := r.value()
			if err != nil {
				return Undefined(), err
			}
			items = append(items, item)
		}
		end, err := r.byte()
		if err != nil {
			return Undefined(), err
		}
		if end != ']' {
			return Undefined(), fmt.Errorf("llsd binary: array not closed, got marker %q", end)
		}
		return ArrayVal(items...), nil
	case '{':
		count, err := r.u32be()
		if err != nil {
			return Undefined(), err
		}
		m := make(map[string]Value, count)
		for i := uint32(0); i < count; i++ {
			km, err := r.byte()
			if err != nil {
				return Undefined(), err
			}
			if km != 'k' {
				return Undefined(), fmt.Errorf("llsd binary: map key marker is %q, want 'k'", km)
			}
			kb, err := r.lenPrefixed()
			if err != nil {
				return Undefined(), err
			}
			val, err := r.value()
			if err != nil {
				return Undefined(), err
			}
			m[string(kb)] = val
		}
		end, err := r.byte()
		if err != nil {
			return Undefined(), err
		}
		if end != '}' {
			return Undefined(), fmt.Errorf("llsd binary: map not closed, got marker %q", end)
		}
		return MapVal(m), nil
	}
	return Undefined(), fmt.Errorf("llsd binary: unknown marker 0x%02x at offset %d", marker, r.pos-1)
}

// UnmarshalBinary parses binary LLSD.
func UnmarshalBinary(data []byte) (Value, error) {
	r := &binReader{data: data}
	return r.value()
}
```

---

## Part 6 — Zerocode, packet header, message IDs

```go
import (
	"encoding/binary"
	"fmt"
)

// ZeroDecode expands a zerocoded message body (the part after the message
// ID). A 0x00 byte is followed by a count (1–255) of total zeroes.
func ZeroDecode(in []byte) []byte {
	out := make([]byte, 0, len(in)*2)
	for i := 0; i < len(in); {
		if in[i] == 0 {
			if i+1 < len(in) {
				count := int(in[i+1])
				for j := 0; j < count; j++ {
					out = append(out, 0)
				}
				i += 2
			} else {
				out = append(out, 0) // trailing lone zero: corrupt, viewer treats as one zero
				i++
			}
		} else {
			out = append(out, in[i])
			i++
		}
	}
	return out
}

// ZeroEncode compresses a body for a Zerocoded message.
func ZeroEncode(in []byte) []byte {
	out := make([]byte, 0, len(in))
	for i := 0; i < len(in); {
		if in[i] == 0 {
			run := 0
			for i < len(in) && in[i] == 0 && run < 255 {
				run++
				i++
			}
			out = append(out, 0, byte(run))
		} else {
			out = append(out, in[i])
			i++
		}
	}
	return out
}

// Packet flags (first header byte).
const (
	FlagZerocoded byte = 0x80
	FlagReliable  byte = 0x40
	FlagResent    byte = 0x20
	FlagAck       byte = 0x10
)

// Frequency bands from the message template.
type Frequency int

const (
	FreqHigh Frequency = iota
	FreqMedium
	FreqLow
	FreqFixed
)

func (f Frequency) String() string {
	switch f {
	case FreqHigh:
		return "High"
	case FreqMedium:
		return "Medium"
	case FreqLow:
		return "Low"
	case FreqFixed:
		return "Fixed"
	}
	return "?"
}

// Header is the 6-byte UDP packet header. Sequence is BIG-endian on the wire
// (body fields are little-endian — do not unify these).
type Header struct {
	Flags     byte
	Sequence  uint32
	ExtraLen  byte
	BodyOff   int   // offset of the message ID
	AckOff    int   // offset of the appended ACK block, -1 when absent
	Acks      []uint32
}

const headerSize = 6

func (h Header) Zerocoded() bool { return h.Flags&FlagZerocoded != 0 }
func (h Header) Reliable() bool  { return h.Flags&FlagReliable != 0 }
func (h Header) Resent() bool    { return h.Flags&FlagResent != 0 }
func (h Header) HasAcks() bool   { return h.Flags&FlagAck != 0 }

// EncodeHeader builds a header with no extra header bytes.
func EncodeHeader(flags byte, sequence uint32) [headerSize]byte {
	var out [headerSize]byte
	out[0] = flags
	binary.BigEndian.PutUint32(out[1:5], sequence)
	out[5] = 0
	return out
}

// DecodeHeader parses a datagram's header and any appended ACK list. The ACK
// layout is: body..., count(u8), count × u32 BE, at the very end of the
// packet. The count byte position is found by self-consistency, the same
// approach LibreMetaverse uses.
func DecodeHeader(dgram []byte) (Header, error) {
	if len(dgram) < headerSize {
		return Header{}, fmt.Errorf("packet: %d bytes, header needs %d", len(dgram), headerSize)
	}
	h := Header{
		Flags:    dgram[0],
		Sequence: binary.BigEndian.Uint32(dgram[1:5]),
		ExtraLen: dgram[5],
		AckOff:   -1,
	}
	h.BodyOff = headerSize + int(h.ExtraLen)
	if h.HasAcks() {
		for k := 1; k <= 255; k++ {
			need := 1 + 4*k
			if len(dgram) < headerSize+need {
				break
			}
			idx := len(dgram) - need
			if int(dgram[idx]) == k {
				h.AckOff = idx
				for j := 0; j < k; j++ {
					off := idx + 1 + 4*j
					h.Acks = append(h.Acks, binary.BigEndian.Uint32(dgram[off:off+4]))
				}
				break
			}
		}
	}
	return h, nil
}

// MessageID is a decoded template message identifier.
type MessageID struct {
	Frequency Frequency
	Number    uint32 // for FreqFixed: the low byte of the 0xFFFFFFxx ID
	Size      int    // bytes consumed
}

// DecodeMessageID reads the ID at the start of a packet body.
func DecodeMessageID(body []byte) (MessageID, error) {
	if len(body) == 0 {
		return MessageID{}, fmt.Errorf("message id: empty body")
	}
	switch body[0] {
	case 0xFF:
		if len(body) >= 2 && body[1] == 0xFF {
			if len(body) >= 3 && body[2] == 0xFF {
				if len(body) < 4 {
					return MessageID{}, fmt.Errorf("message id: truncated fixed")
				}
				return MessageID{FreqFixed, uint32(body[3]), 4}, nil
			}
			if len(body) < 4 {
				return MessageID{}, fmt.Errorf("message id: truncated low")
			}
			return MessageID{FreqLow, uint32(binary.BigEndian.Uint16(body[2:4])), 4}, nil
		}
		if len(body) < 2 {
			return MessageID{}, fmt.Errorf("message id: truncated medium")
		}
		return MessageID{FreqMedium, uint32(body[1]), 2}, nil
	default:
		return MessageID{FreqHigh, uint32(body[0]), 1}, nil
	}
}

// AppendMessageID encodes an ID onto a packet body under construction.
func AppendMessageID(dst []byte, freq Frequency, number uint32) []byte {
	switch freq {
	case FreqHigh:
		return append(dst, byte(number))
	case FreqMedium:
		return append(dst, 0xFF, byte(number))
	case FreqLow:
		var b [2]byte
		binary.BigEndian.PutUint16(b[:], uint16(number))
		return append(dst, 0xFF, 0xFF, b[0], b[1])
	case FreqFixed:
		return append(dst, 0xFF, 0xFF, 0xFF, byte(number))
	}
	return dst
}
```

---

## Part 7 — The circuit over net.UDPConn

The circuit mirrors the viewer's `llcircuit` and LibreMetaverse.Transport:
outgoing sequence per packet; reliable packets held until ACKed and resent
with the RESENT flag; incoming reliable packets ACKed (piggybacked when
possible, standalone PacketAck otherwise); duplicate sequences suppressed;
ping for round-trip and NAT keepalive. All state is guarded by a mutex so the
read loop, the caller's send paths, and the maintenance goroutine can share
one Circuit safely.

```go
import (
	"context"
	"errors"
	"net"
	"sync"
	"time"
)

// CircuitConfig tunes reliability behaviour. Defaults match the values the
// Rust companion uses; they are configuration, not protocol constants —
// the simulator tolerates a range, and lossy mobile links want shorter
// resend timers than a datacentre bot does.
type CircuitConfig struct {
	ResendAfter time.Duration // first resend of an unacked reliable packet
	MaxResends  int           // give up on a packet after this many resends
	Timeout     time.Duration // no inbound traffic for this long => dead
	AckBatch    int           // max ACKs piggybacked per outgoing packet
}

func DefaultCircuitConfig() CircuitConfig {
	return CircuitConfig{
		ResendAfter: 1 * time.Second,
		MaxResends:  12,
		Timeout:     60 * time.Second,
		AckBatch:    32,
	}
}

type pendingPacket struct {
	sequence uint32
	datagram []byte // verbatim, resent with FlagResent set
	sentAt   time.Time
	resends  int
}

// Circuit is one simulator circuit (one region connection).
type Circuit struct {
	CircuitCode uint32
	SessionID   UUID
	AgentID     UUID

	conn *net.UDPConn
	cfg  CircuitConfig

	mu          sync.Mutex
	nextSeq     uint32
	pending     map[uint32]*pendingPacket
	ackQueue    []uint32
	seen        map[uint32]struct{}
	highestSeen uint32
	lastRecv    time.Time
	pingID      byte
	pingSent    time.Time
	RoundTrip   time.Duration
}

func NewCircuit(conn *net.UDPConn, code uint32, session, agent UUID, cfg CircuitConfig) *Circuit {
	return &Circuit{
		CircuitCode: code,
		SessionID:   session,
		AgentID:     agent,
		conn:        conn,
		cfg:         cfg,
		nextSeq:     1, // viewer starts at 1
		pending:     map[uint32]*pendingPacket{},
		seen:        map[uint32]struct{}{},
		lastRecv:    time.Now(),
	}
}

// BuildPacket frames one message (ID + body, already zerocoded by the caller
// when the template says so) into a datagram and records it for resend when
// reliable. It does not write to the socket; Send does.
func (c *Circuit) BuildPacket(idAndBody []byte, reliable, zerocoded bool) []byte {
	c.mu.Lock()
	defer c.mu.Unlock()
	seq := c.nextSeq
	c.nextSeq++
	var flags byte
	if reliable {
		flags |= FlagReliable
	}
	if zerocoded {
		flags |= FlagZerocoded
	}
	nAck := len(c.ackQueue)
	if nAck > c.cfg.AckBatch {
		nAck = c.cfg.AckBatch
	}
	if nAck > 0 {
		flags |= FlagAck
	}
	hdr := EncodeHeader(flags, seq)
	out := make([]byte, 0, headerSize+len(idAndBody)+1+4*nAck)
	out = append(out, hdr[:]...)
	out = append(out, idAndBody...)
	if nAck > 0 {
		out = append(out, byte(nAck))
		for _, a := range c.ackQueue[:nAck] {
			var b [4]byte
			binary.BigEndian.PutUint32(b[:], a)
			out = append(out, b[:]...)
		}
		c.ackQueue = c.ackQueue[nAck:]
	}
	if reliable {
		cp := append([]byte(nil), out...)
		c.pending[seq] = &pendingPacket{sequence: seq, datagram: cp, sentAt: time.Now()}
	}
	return out
}

// Send builds and writes one datagram.
func (c *Circuit) Send(idAndBody []byte, reliable, zerocoded bool) error {
	dgram := c.BuildPacket(idAndBody, reliable, zerocoded)
	_, err := c.conn.Write(dgram)
	return err
}

// ErrDuplicate is returned by Receive for resent packets already handled.
var ErrDuplicate = errors.New("circuit: duplicate packet")

// Receive processes one inbound datagram: clears resends for ACKs addressed
// to us, suppresses duplicates, queues an ACK for reliable packets, decodes
// zerocoding, and returns header + message ID + body for dispatch.
func (c *Circuit) Receive(dgram []byte) (Header, MessageID, []byte, error) {
	h, err := DecodeHeader(dgram)
	if err != nil {
		return h, MessageID{}, nil, err
	}
	c.mu.Lock()
	c.lastRecv = time.Now()
	for _, seq := range h.Acks {
		delete(c.pending, seq)
	}
	if h.Reliable() || h.Resent() {
		if _, dup := c.seen[h.Sequence]; dup {
			// ACK again — the resend means our earlier ACK was lost.
			c.ackQueue = append(c.ackQueue, h.Sequence)
			c.mu.Unlock()
			return h, MessageID{}, nil, ErrDuplicate
		}
		c.seen[h.Sequence] = struct{}{}
		if h.Sequence > c.highestSeen {
			c.highestSeen = h.Sequence
			floor := c.highestSeen - 4096
			if c.highestSeen > 4096 {
				for s := range c.seen {
					if s < floor {
						delete(c.seen, s)
					}
				}
			}
		}
		c.ackQueue = append(c.ackQueue, h.Sequence)
	}
	c.mu.Unlock()

	end := len(dgram)
	if h.AckOff >= 0 {
		end = h.AckOff
	}
	if h.BodyOff >= end {
		return h, MessageID{}, nil, nil // pure ACK / keepalive
	}
	raw := dgram[h.BodyOff:end]
	id, err := DecodeMessageID(raw)
	if err != nil {
		return h, MessageID{}, nil, err
	}
	body := append([]byte(nil), raw[id.Size:]...)
	if h.Zerocoded() {
		body = ZeroDecode(body)
	}
	return h, id, body, nil
}

// Tick performs maintenance: expired resends and, when ACKs are owed, a
// standalone PacketAck (Fixed 0xFB). Returned datagrams are ready to write.
func (c *Circuit) Tick() [][]byte {
	c.mu.Lock()
	defer c.mu.Unlock()
	now := time.Now()
	var out [][]byte
	for seq, p := range c.pending {
		if now.Sub(p.sentAt) < c.cfg.ResendAfter {
			continue
		}
		if p.resends >= c.cfg.MaxResends {
			delete(c.pending, seq)
			continue
		}
		p.resends++
		p.sentAt = now
		dg := append([]byte(nil), p.datagram...)
		dg[0] |= FlagResent
		out = append(out, dg)
	}
	if len(c.ackQueue) > 0 {
		n := len(c.ackQueue)
		if n > 255 {
			n = 255
		}
		body := AppendMessageID(nil, FreqFixed, 0xFB)
		body = append(body, byte(n))
		for _, a := range c.ackQueue[:n] {
			var b [4]byte
			binary.BigEndian.PutUint32(b[:], a)
			body = append(body, b[:]...)
		}
		c.ackQueue = c.ackQueue[n:]
		seq := c.nextSeq
		c.nextSeq++
		hdr := EncodeHeader(0, seq)
		dg := append(append([]byte(nil), hdr[:]...), body...)
		out = append(out, dg)
	}
	return out
}

// TimedOut reports whether the circuit has seen no traffic within Timeout.
func (c *Circuit) TimedOut() bool {
	c.mu.Lock()
	defer c.mu.Unlock()
	return time.Since(c.lastRecv) >= c.cfg.Timeout
}

// StartPing builds a StartPingCheck body (Fixed 0xFC): ping ID + the two
// legacy zero u32 fields the viewer still sends.
func (c *Circuit) StartPing() []byte {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.pingID++
	c.pingSent = time.Now()
	body := AppendMessageID(nil, FreqFixed, 0xFC)
	body = append(body, c.pingID)
	body = append(body, 0, 0, 0, 0)
	return body
}

// NotePingReply records the round trip for a CompletePingCheck echo.
func (c *Circuit) NotePingReply(id byte) {
	c.mu.Lock()
	defer c.mu.Unlock()
	if id == c.pingID && !c.pingSent.IsZero() {
		c.RoundTrip = time.Since(c.pingSent)
	}
}

```

---

---

## Part 8 — Message registry (generated from `message_template.msg`)
All 483 template messages with their 902 blocks and 2984 fields, as data. Block kinds: `S` = exactly one, `V` = count-prefixed repeat, `M N` = exactly N. Field types abbreviated: `V3` = LLVector3, `V3d` = LLVector3d, `V4` = LLVector4, `Q` = LLQuaternion, `U` = LLUUID, `Var1`/`Var2` = Variable 1/2. For Fixed messages, `Number` is the low byte of the template's hex ID (PacketAck 0xFFFFFFFB → 251), matching `DecodeMessageID`. `Flags` is a bitmask: 1 = Trusted, 2 = Zerocoded. Regenerate from the template you diffed against the viewer — do not hand-edit entries.
```go
// Frequency band shorthands for the registry table.
const (
	FH = FreqHigh
	FM = FreqMedium
	FL = FreqLow
	FF = FreqFixed
)

// MessageInfo describes one template message. Blocks encodes
// `Block:Kind[:Count]:Field=Type,...` with blocks separated by `;`.
type MessageInfo struct {
	Name      string
	Frequency Frequency
	Number    uint32
	Flags     uint8 // 1 = Trusted, 2 = Zerocoded
	Blocks    string
}

func (m MessageInfo) Trusted() bool   { return m.Flags&1 != 0 }
func (m MessageInfo) Zerocoded() bool { return m.Flags&2 != 0 }

// Messages is the full template registry.
var Messages = []MessageInfo{
	{"TestMessage",FL,1,2,"TestBlock1:S:Test1=U32;NeighborBlock:M:4:Test0=U32,Test1=U32,Test2=U32"},
	{"PacketAck",FF,251,0,"Packets:V:ID=U32"},
	{"OpenCircuit",FF,252,0,"CircuitInfo:S:IP=IPADDR,Port=IPPORT"},
	{"CloseCircuit",FF,253,0,""},
	{"StartPingCheck",FH,1,0,"PingID:S:PingID=U8,OldestUnacked=U32"},
	{"CompletePingCheck",FH,2,0,"PingID:S:PingID=U8"},
	{"AddCircuitCode",FL,2,1,"CircuitCode:S:Code=U32,SessionID=U,AgentID=U"},
	{"UseCircuitCode",FL,3,0,"CircuitCode:S:Code=U32,SessionID=U,ID=U"},
	{"NeighborList",FH,3,1,"NeighborBlock:M:4:IP=IPADDR,Port=IPPORT,PublicIP=IPADDR,PublicPort=IPPORT,RegionID=U,Name=Var1,SimAccess=U8"},
	{"AvatarTextureUpdate",FL,4,3,"AgentData:S:AgentID=U,TexturesChanged=BOOL;WearableData:V:CacheID=U,TextureIndex=U8,HostName=Var1;TextureData:V:TextureID=U"},
	{"SimulatorMapUpdate",FL,5,1,"MapData:S:Flags=U32"},
	{"SimulatorSetMap",FL,6,1,"MapData:S:RegionHandle=U64,Type=S32,MapImage=U"},
	{"SubscribeLoad",FL,7,1,""},
	{"UnsubscribeLoad",FL,8,1,""},
	{"SimulatorReady",FL,9,3,"SimulatorBlock:S:SimName=Var1,SimAccess=U8,RegionFlags=U32,RegionID=U,EstateID=U32,ParentEstateID=U32;TelehubBlock:S:HasTelehub=BOOL,TelehubPos=V3"},
	{"TelehubInfo",FL,10,1,"TelehubBlock:S:ObjectID=U,ObjectName=Var1,TelehubPos=V3,TelehubRot=Q;SpawnPointBlock:V:SpawnPointPos=V3"},
	{"SimulatorPresentAtLocation",FL,11,1,"SimulatorPublicHostBlock:S:Port=IPPORT,SimulatorIP=IPADDR,GridX=U32,GridY=U32;NeighborBlock:M:4:IP=IPADDR,Port=IPPORT;SimulatorBlock:S:SimName=Var1,SimAccess=U8,RegionFlags=U32,RegionID=U,EstateID=U32,ParentEstateID=U32;TelehubBlock:V:HasTelehub=BOOL,TelehubPos=V3"},
	{"SimulatorLoad",FL,12,1,"SimulatorLoad:S:TimeDilation=F32,AgentCount=S32,CanAcceptAgents=BOOL;AgentList:V:CircuitCode=U32,X=U8,Y=U8"},
	{"SimulatorShutdownRequest",FL,13,1,""},
	{"RegionPresenceRequestByRegionID",FL,14,1,"RegionData:V:RegionID=U"},
	{"RegionPresenceRequestByHandle",FL,15,1,"RegionData:V:RegionHandle=U64"},
	{"RegionPresenceResponse",FL,16,3,"RegionData:V:RegionID=U,RegionHandle=U64,InternalRegionIP=IPADDR,ExternalRegionIP=IPADDR,RegionPort=IPPORT,ValidUntil=F64,Message=Var1"},
	{"UpdateSimulator",FL,17,1,"SimulatorInfo:S:RegionID=U,SimName=Var1,EstateID=U32,SimAccess=U8"},
	{"LogDwellTime",FL,18,1,"DwellInfo:S:AgentID=U,SessionID=U,Duration=F32,SimName=Var1,RegionX=U32,RegionY=U32,AvgAgentsInView=U8,AvgViewerFPS=U8"},
	{"FeatureDisabled",FL,19,1,"FailureInfo:S:ErrorMessage=Var1,AgentID=U,TransactionID=U"},
	{"LogFailedMoneyTransaction",FL,20,1,"TransactionData:S:TransactionID=U,TransactionTime=U32,TransactionType=S32,SourceID=U,DestID=U,Flags=U8,Amount=S32,SimulatorIP=IPADDR,GridX=U32,GridY=U32,FailureType=U8"},
	{"UserReportInternal",FL,21,3,"ReportData:S:ReportType=U8,Category=U8,ReporterID=U,ViewerPosition=V3,AgentPosition=V3,ScreenshotID=U,ObjectID=U,OwnerID=U,LastOwnerID=U,CreatorID=U,RegionID=U,AbuserID=U,AbuseRegionName=Var1,AbuseRegionID=U,Summary=Var1,Details=Var2,VersionString=Var1"},
	{"SetSimStatusInDatabase",FL,22,1,"Data:S:RegionID=U,HostName=Var1,X=S32,Y=S32,PID=S32,AgentCount=S32,TimeToLive=S32,Status=Var1"},
	{"SetSimPresenceInDatabase",FL,23,1,"SimData:S:RegionID=U,HostName=Var1,GridX=U32,GridY=U32,PID=S32,AgentCount=S32,TimeToLive=S32,Status=Var1"},
	{"EconomyDataRequest",FL,24,0,""},
	{"EconomyData",FL,25,3,"Info:S:ObjectCapacity=S32,ObjectCount=S32,PriceEnergyUnit=S32,PriceObjectClaim=S32,PricePublicObjectDecay=S32,PricePublicObjectDelete=S32,PriceParcelClaim=S32,PriceParcelClaimFactor=F32,PriceUpload=S32,PriceRentLight=S32,TeleportMinPrice=S32,TeleportPriceExponent=F32,EnergyEfficiency=F32,PriceObjectRent=F32,PriceObjectScaleFactor=F32,PriceParcelRent=S32,PriceGroupCreate=S32"},
	{"AvatarPickerRequest",FL,26,0,"AgentData:S:AgentID=U,SessionID=U,QueryID=U;Data:S:Name=Var1"},
	{"AvatarPickerRequestBackend",FL,27,1,"AgentData:S:AgentID=U,SessionID=U,QueryID=U,GodLevel=U8;Data:S:Name=Var1"},
	{"AvatarPickerReply",FL,28,1,"AgentData:S:AgentID=U,QueryID=U;Data:V:AvatarID=U,FirstName=Var1,LastName=Var1"},
	{"PlacesQuery",FL,29,2,"AgentData:S:AgentID=U,SessionID=U,QueryID=U;TransactionData:S:TransactionID=U;QueryData:S:QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1"},
	{"PlacesReply",FL,30,3,"AgentData:S:AgentID=U,QueryID=U;TransactionData:S:TransactionID=U;QueryData:V:OwnerID=U,Name=Var1,Desc=Var1,ActualArea=S32,BillableArea=S32,Flags=U8,GlobalX=F32,GlobalY=F32,GlobalZ=F32,SimName=Var1,SnapshotID=U,Dwell=F32,Price=S32"},
	{"DirFindQuery",FL,31,2,"AgentData:S:AgentID=U,SessionID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,QueryStart=S32"},
	{"DirFindQueryBackend",FL,32,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,QueryStart=S32,EstateID=U32,Godlike=BOOL"},
	{"DirPlacesQuery",FL,33,2,"AgentData:S:AgentID=U,SessionID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1,QueryStart=S32"},
	{"DirPlacesQueryBackend",FL,34,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1,EstateID=U32,Godlike=BOOL,QueryStart=S32"},
	{"DirPlacesReply",FL,35,3,"AgentData:S:AgentID=U;QueryData:V:QueryID=U;QueryReplies:V:ParcelID=U,Name=Var1,ForSale=BOOL,Auction=BOOL,Dwell=F32;StatusData:V:Status=U32"},
	{"DirPeopleReply",FL,36,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:AgentID=U,FirstName=Var1,LastName=Var1,Group=Var1,Online=BOOL,Reputation=S32"},
	{"DirEventsReply",FL,37,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:OwnerID=U,Name=Var1,EventID=U32,Date=Var1,UnixTime=U32,EventFlags=U32;StatusData:V:Status=U32"},
	{"DirGroupsReply",FL,38,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:GroupID=U,GroupName=Var1,Members=S32,SearchOrder=F32"},
	{"DirClassifiedQuery",FL,39,2,"AgentData:S:AgentID=U,SessionID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,Category=U32,QueryStart=S32"},
	{"DirClassifiedQueryBackend",FL,40,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,Category=U32,EstateID=U32,Godlike=BOOL,QueryStart=S32"},
	{"DirClassifiedReply",FL,41,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:ClassifiedID=U,Name=Var1,ClassifiedFlags=U8,CreationDate=U32,ExpirationDate=U32,PriceForListing=S32;StatusData:V:Status=U32"},
	{"AvatarClassifiedReply",FL,42,1,"AgentData:S:AgentID=U,TargetID=U;Data:V:ClassifiedID=U,Name=Var1"},
	{"ClassifiedInfoRequest",FL,43,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:ClassifiedID=U"},
	{"ClassifiedInfoReply",FL,44,1,"AgentData:S:AgentID=U;Data:S:ClassifiedID=U,CreatorID=U,CreationDate=U32,ExpirationDate=U32,Category=U32,Name=Var1,Desc=Var2,ParcelID=U,ParentEstate=U32,SnapshotID=U,SimName=Var1,PosGlobal=V3d,ParcelName=Var1,ClassifiedFlags=U8,PriceForListing=S32"},
	{"ClassifiedInfoUpdate",FL,45,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:ClassifiedID=U,Category=U32,Name=Var1,Desc=Var2,ParcelID=U,ParentEstate=U32,SnapshotID=U,PosGlobal=V3d,ClassifiedFlags=U8,PriceForListing=S32"},
	{"ClassifiedDelete",FL,46,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:ClassifiedID=U"},
	{"ClassifiedGodDelete",FL,47,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:ClassifiedID=U,QueryID=U"},
	{"DirLandQuery",FL,48,2,"AgentData:S:AgentID=U,SessionID=U;QueryData:S:QueryID=U,QueryFlags=U32,SearchType=U32,Price=S32,Area=S32,QueryStart=S32"},
	{"DirLandQueryBackend",FL,49,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U,QueryFlags=U32,SearchType=U32,Price=S32,Area=S32,QueryStart=S32,EstateID=U32,Godlike=BOOL"},
	{"DirLandReply",FL,50,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:ParcelID=U,Name=Var1,Auction=BOOL,ForSale=BOOL,SalePrice=S32,ActualArea=S32"},
	{"DirPopularQuery",FL,51,2,"AgentData:S:AgentID=U,SessionID=U;QueryData:S:QueryID=U,QueryFlags=U32"},
	{"DirPopularQueryBackend",FL,52,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U,QueryFlags=U32,EstateID=U32,Godlike=BOOL"},
	{"DirPopularReply",FL,53,3,"AgentData:S:AgentID=U;QueryData:S:QueryID=U;QueryReplies:V:ParcelID=U,Name=Var1,Dwell=F32"},
	{"ParcelInfoRequest",FL,54,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:ParcelID=U"},
	{"ParcelInfoReply",FL,55,3,"AgentData:S:AgentID=U;Data:S:ParcelID=U,OwnerID=U,Name=Var1,Desc=Var1,ActualArea=S32,BillableArea=S32,Flags=U8,GlobalX=F32,GlobalY=F32,GlobalZ=F32,SimName=Var1,SnapshotID=U,Dwell=F32,SalePrice=S32,AuctionID=S32"},
	{"ParcelObjectOwnersRequest",FL,56,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32"},
	{"ParcelObjectOwnersReply",FL,57,3,"Data:V:OwnerID=U,IsGroupOwned=BOOL,Count=S32,OnlineStatus=BOOL"},
	{"GroupNoticesListRequest",FL,58,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U"},
	{"GroupNoticesListReply",FL,59,1,"AgentData:S:AgentID=U,GroupID=U;Data:V:NoticeID=U,Timestamp=U32,FromName=Var2,Subject=Var2,HasAttachment=BOOL,AssetType=U8"},
	{"GroupNoticeRequest",FL,60,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupNoticeID=U"},
	{"GroupNoticeAdd",FL,61,1,"AgentData:S:AgentID=U;MessageBlock:S:ToGroupID=U,ID=U,Dialog=U8,FromAgentName=Var1,Message=Var2,BinaryBucket=Var2"},
	{"TeleportRequest",FL,62,0,"AgentData:S:AgentID=U,SessionID=U;Info:S:RegionID=U,Position=V3,LookAt=V3"},
	{"TeleportLocationRequest",FL,63,0,"AgentData:S:AgentID=U,SessionID=U;Info:S:RegionHandle=U64,Position=V3,LookAt=V3"},
	{"TeleportLocal",FL,64,1,"Info:S:AgentID=U,LocationID=U32,Position=V3,LookAt=V3,TeleportFlags=U32"},
	{"TeleportLandmarkRequest",FL,65,2,"Info:S:AgentID=U,SessionID=U,LandmarkID=U"},
	{"TeleportProgress",FL,66,1,"AgentData:S:AgentID=U;Info:S:TeleportFlags=U32,Message=Var1"},
	{"DataHomeLocationRequest",FL,67,3,"Info:S:AgentID=U,KickedFromEstateID=U32;AgentInfo:S:AgentEffectiveMaturity=U32"},
	{"DataHomeLocationReply",FL,68,1,"Info:S:AgentID=U,RegionHandle=U64,Position=V3,LookAt=V3"},
	{"TeleportFinish",FL,69,1,"Info:S:AgentID=U,LocationID=U32,SimIP=IPADDR,SimPort=IPPORT,RegionHandle=U64,SeedCapability=Var2,SimAccess=U8,TeleportFlags=U32"},
	{"StartLure",FL,70,0,"AgentData:S:AgentID=U,SessionID=U;Info:S:LureType=U8,Message=Var1;TargetData:V:TargetID=U"},
	{"TeleportLureRequest",FL,71,0,"Info:S:AgentID=U,SessionID=U,LureID=U,TeleportFlags=U32"},
	{"TeleportCancel",FL,72,0,"Info:S:AgentID=U,SessionID=U"},
	{"TeleportStart",FL,73,1,"Info:S:TeleportFlags=U32"},
	{"TeleportFailed",FL,74,1,"Info:S:AgentID=U,Reason=Var1;AlertInfo:V:Message=Var1,ExtraParams=Var1"},
	{"Undo",FL,75,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;ObjectData:V:ObjectID=U"},
	{"Redo",FL,76,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;ObjectData:V:ObjectID=U"},
	{"UndoLand",FL,77,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"AgentPause",FL,78,0,"AgentData:S:AgentID=U,SessionID=U,SerialNum=U32"},
	{"AgentResume",FL,79,0,"AgentData:S:AgentID=U,SessionID=U,SerialNum=U32"},
	{"AgentUpdate",FH,4,2,"AgentData:S:AgentID=U,SessionID=U,BodyRotation=Q,HeadRotation=Q,State=U8,CameraCenter=V3,CameraAtAxis=V3,CameraLeftAxis=V3,CameraUpAxis=V3,Far=F32,ControlFlags=U32,Flags=U8"},
	{"ChatFromViewer",FL,80,2,"AgentData:S:AgentID=U,SessionID=U;ChatData:S:Message=Var2,Type=U8,Channel=S32"},
	{"AgentThrottle",FL,81,2,"AgentData:S:AgentID=U,SessionID=U,CircuitCode=U32;Throttle:S:GenCounter=U32,Throttles=Var1"},
	{"AgentFOV",FL,82,0,"AgentData:S:AgentID=U,SessionID=U,CircuitCode=U32;FOVBlock:S:GenCounter=U32,VerticalAngle=F32"},
	{"AgentHeightWidth",FL,83,0,"AgentData:S:AgentID=U,SessionID=U,CircuitCode=U32;HeightWidthBlock:S:GenCounter=U32,Height=U16,Width=U16"},
	{"AgentSetAppearance",FL,84,2,"AgentData:S:AgentID=U,SessionID=U,SerialNum=U32,Size=V3;WearableData:V:CacheID=U,TextureIndex=U8;ObjectData:S:TextureEntry=Var2;VisualParam:V:ParamValue=U8"},
	{"AgentAnimation",FH,5,0,"AgentData:S:AgentID=U,SessionID=U;AnimationList:V:AnimID=U,StartAnim=BOOL;PhysicalAvatarEventList:V:TypeData=Var1"},
	{"AgentRequestSit",FH,6,2,"AgentData:S:AgentID=U,SessionID=U;TargetObject:S:TargetID=U,Offset=V3"},
	{"AgentSit",FH,7,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"AgentQuitCopy",FL,85,0,"AgentData:S:AgentID=U,SessionID=U;FuseBlock:S:ViewerCircuitCode=U32"},
	{"RequestImage",FH,8,0,"AgentData:S:AgentID=U,SessionID=U;RequestImage:V:Image=U,DiscardLevel=S8,DownloadPriority=F32,Packet=U32,Type=U8"},
	{"ImageNotInDatabase",FL,86,1,"ImageID:S:ID=U"},
	{"RebakeAvatarTextures",FL,87,1,"TextureData:S:TextureID=U"},
	{"SetAlwaysRun",FL,88,0,"AgentData:S:AgentID=U,SessionID=U,AlwaysRun=BOOL"},
	{"ObjectAdd",FM,1,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;ObjectData:S:PCode=U8,Material=U8,AddFlags=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=U,RayEndIsIntersection=U8,Scale=V3,Rotation=Q,State=U8"},
	{"ObjectDelete",FL,89,2,"AgentData:S:AgentID=U,SessionID=U,Force=BOOL;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectDuplicate",FL,90,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;SharedData:S:Offset=V3,DuplicateFlags=U32;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectDuplicateOnRay",FL,91,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U,RayStart=V3,RayEnd=V3,BypassRaycast=BOOL,RayEndIsIntersection=BOOL,CopyCenters=BOOL,CopyRotates=BOOL,RayTargetID=U,DuplicateFlags=U32;ObjectData:V:ObjectLocalID=U32"},
	{"MultipleObjectUpdate",FM,2,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,Type=U8,Data=Var1"},
	{"RequestMultipleObjects",FM,3,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:CacheMissType=U8,ID=U32"},
	{"ObjectPosition",FM,4,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,Position=V3"},
	{"ObjectScale",FL,92,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,Scale=V3"},
	{"ObjectRotation",FL,93,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,Rotation=Q"},
	{"ObjectFlagUpdate",FL,94,2,"AgentData:S:AgentID=U,SessionID=U,ObjectLocalID=U32,UsePhysics=BOOL,IsTemporary=BOOL,IsPhantom=BOOL,CastsShadows=BOOL;ExtraPhysics:V:PhysicsShapeType=U8,Density=F32,Friction=F32,Restitution=F32,GravityMultiplier=F32"},
	{"ObjectClickAction",FL,95,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,ClickAction=U8"},
	{"ObjectImage",FL,96,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,MediaURL=Var1,TextureEntry=Var2"},
	{"ObjectBypassModUpdate",FL,431,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,PropertyID=U8,Value=Var2"},
	{"ObjectMaterial",FL,97,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,Material=U8"},
	{"ObjectShape",FL,98,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16"},
	{"ObjectExtraParams",FL,99,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,ParamType=U16,ParamInUse=BOOL,ParamSize=U32,ParamData=Var1"},
	{"ObjectOwner",FL,100,2,"AgentData:S:AgentID=U,SessionID=U;HeaderData:S:Override=BOOL,OwnerID=U,GroupID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectGroup",FL,101,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectBuy",FL,102,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U,CategoryID=U;ObjectData:V:ObjectLocalID=U32,SaleType=U8,SalePrice=S32"},
	{"BuyObjectInventory",FL,103,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:ObjectID=U,ItemID=U,FolderID=U"},
	{"DerezContainer",FL,104,3,"Data:S:ObjectID=U,Delete=BOOL"},
	{"ObjectPermissions",FL,105,2,"AgentData:S:AgentID=U,SessionID=U;HeaderData:S:Override=BOOL;ObjectData:V:ObjectLocalID=U32,Field=U8,Set=U8,Mask=U32"},
	{"ObjectSaleInfo",FL,106,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:LocalID=U32,SaleType=U8,SalePrice=S32"},
	{"ObjectName",FL,107,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:LocalID=U32,Name=Var1"},
	{"ObjectDescription",FL,108,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:LocalID=U32,Description=Var1"},
	{"ObjectCategory",FL,109,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:LocalID=U32,Category=U32"},
	{"ObjectSelect",FL,110,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectDeselect",FL,111,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectAttach",FL,112,2,"AgentData:S:AgentID=U,SessionID=U,AttachmentPoint=U8;ObjectData:V:ObjectLocalID=U32,Rotation=Q"},
	{"ObjectDetach",FL,113,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectDrop",FL,114,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectLink",FL,115,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectDelink",FL,116,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32"},
	{"ObjectGrab",FL,117,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:LocalID=U32,GrabOffset=V3;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3"},
	{"ObjectGrabUpdate",FL,118,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:ObjectID=U,GrabOffsetInitial=V3,GrabPosition=V3,TimeSinceLast=U32;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3"},
	{"ObjectDeGrab",FL,119,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:LocalID=U32;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3"},
	{"ObjectSpinStart",FL,120,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:ObjectID=U"},
	{"ObjectSpinUpdate",FL,121,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:ObjectID=U,Rotation=Q"},
	{"ObjectSpinStop",FL,122,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:ObjectID=U"},
	{"ObjectExportSelected",FL,123,2,"AgentData:S:AgentID=U,RequestID=U,VolumeDetail=S16;ObjectData:V:ObjectID=U"},
	{"ModifyLand",FL,124,2,"AgentData:S:AgentID=U,SessionID=U;ModifyBlock:S:Action=U8,BrushSize=U8,Seconds=F32,Height=F32;ParcelData:V:LocalID=S32,West=F32,South=F32,East=F32,North=F32;ModifyBlockExtended:V:BrushSize=F32"},
	{"VelocityInterpolateOn",FL,125,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"VelocityInterpolateOff",FL,126,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"StateSave",FL,127,0,"AgentData:S:AgentID=U,SessionID=U;DataBlock:S:Filename=Var1"},
	{"ReportAutosaveCrash",FL,128,0,"AutosaveData:S:PID=S32,Status=S32"},
	{"SimWideDeletes",FL,129,0,"AgentData:S:AgentID=U,SessionID=U;DataBlock:S:TargetID=U,Flags=U32"},
	{"RequestObjectPropertiesFamily",FM,5,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:RequestFlags=U32,ObjectID=U"},
	{"TrackAgent",FL,130,0,"AgentData:S:AgentID=U,SessionID=U;TargetData:S:PreyID=U"},
	{"ViewerStats",FL,131,2,"AgentData:S:AgentID=U,SessionID=U,IP=IPADDR,StartTime=U32,RunTime=F32,SimFPS=F32,FPS=F32,AgentsInView=U8,Ping=F32,MetersTraveled=F64,RegionsVisited=S32,SysRAM=U32,SysOS=Var1,SysCPU=Var1,SysGPU=Var1;DownloadTotals:S:World=U32,Objects=U32,Textures=U32;NetStats:M:2:Bytes=U32,Packets=U32,Compressed=U32,Savings=U32;FailStats:S:SendPacket=U32,Dropped=U32,Resent=U32,FailedResends=U32,OffCircuit=U32,Invalid=U32;MiscStats:V:Type=U32,Value=F64"},
	{"ScriptAnswerYes",FL,132,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:TaskID=U,ItemID=U,Questions=S32"},
	{"UserReport",FL,133,2,"AgentData:S:AgentID=U,SessionID=U;ReportData:S:ReportType=U8,Category=U8,Position=V3,CheckFlags=U8,ScreenshotID=U,ObjectID=U,AbuserID=U,AbuseRegionName=Var1,AbuseRegionID=U,Summary=Var1,Details=Var2,VersionString=Var1"},
	{"AlertMessage",FL,134,1,"AlertData:S:Message=Var1;AlertInfo:V:Message=Var1,ExtraParams=Var1;AgentInfo:V:AgentID=U"},
	{"AgentAlertMessage",FL,135,1,"AgentData:S:AgentID=U;AlertData:S:Modal=BOOL,Message=Var1"},
	{"MeanCollisionAlert",FL,136,3,"MeanCollision:V:Victim=U,Perp=U,Time=U32,Mag=F32,Type=U8"},
	{"ViewerFrozenMessage",FL,137,1,"FrozenData:S:Data=BOOL"},
	{"HealthMessage",FL,138,3,"HealthData:S:Health=F32"},
	{"ChatFromSimulator",FL,139,1,"ChatData:S:FromName=Var1,SourceID=U,OwnerID=U,SourceType=U8,ChatType=U8,Audible=U8,Position=V3,Message=Var2"},
	{"SimStats",FL,140,1,"Region:S:RegionX=U32,RegionY=U32,RegionFlags=U32,ObjectCapacity=U32;Stat:V:StatID=U32,StatValue=F32;PidStat:S:PID=S32;RegionInfo:V:RegionFlagsExtended=U64"},
	{"RequestRegionInfo",FL,141,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"RegionInfo",FL,142,2,"AgentData:S:AgentID=U,SessionID=U;RegionInfo:S:SimName=Var1,EstateID=U32,ParentEstateID=U32,RegionFlags=U32,SimAccess=U8,MaxAgents=U8,BillableFactor=F32,ObjectBonusFactor=F32,WaterHeight=F32,TerrainRaiseLimit=F32,TerrainLowerLimit=F32,PricePerMeter=S32,RedirectGridX=S32,RedirectGridY=S32,UseEstateSun=BOOL,SunHour=F32;RegionInfo2:S:ProductSKU=Var1,ProductName=Var1,MaxAgents32=U32,HardMaxAgents=U32,HardMaxObjects=U32;RegionInfo3:V:RegionFlagsExtended=U64;RegionInfo5:V:ChatWhisperRange=F32,ChatNormalRange=F32,ChatShoutRange=F32,ChatWhisperOffset=F32,ChatNormalOffset=F32,ChatShoutOffset=F32,ChatFlags=U32;CombatSettings:V:CombatFlags=U32,OnDeath=U8,DamageThrottle=F32,RegenerationRate=F32,InvulnerabilyTime=F32,DamageLimit=F32"},
	{"GodUpdateRegionInfo",FL,143,2,"AgentData:S:AgentID=U,SessionID=U;RegionInfo:S:SimName=Var1,EstateID=U32,ParentEstateID=U32,RegionFlags=U32,BillableFactor=F32,PricePerMeter=S32,RedirectGridX=S32,RedirectGridY=S32;RegionInfo2:V:RegionFlagsExtended=U64"},
	{"NearestLandingRegionRequest",FL,144,1,"RequestingRegionData:S:RegionHandle=U64"},
	{"NearestLandingRegionReply",FL,145,1,"LandingRegionData:S:RegionHandle=U64"},
	{"NearestLandingRegionUpdated",FL,146,1,"RegionData:S:RegionHandle=U64"},
	{"TeleportLandingStatusChanged",FL,147,1,"RegionData:S:RegionHandle=U64"},
	{"RegionHandshake",FL,148,3,"RegionInfo:S:RegionFlags=U32,SimAccess=U8,SimName=Var1,SimOwner=U,IsEstateManager=BOOL,WaterHeight=F32,BillableFactor=F32,CacheID=U,TerrainBase0=U,TerrainBase1=U,TerrainBase2=U,TerrainBase3=U,TerrainDetail0=U,TerrainDetail1=U,TerrainDetail2=U,TerrainDetail3=U,TerrainStartHeight00=F32,TerrainStartHeight01=F32,TerrainStartHeight10=F32,TerrainStartHeight11=F32,TerrainHeightRange00=F32,TerrainHeightRange01=F32,TerrainHeightRange10=F32,TerrainHeightRange11=F32;RegionInfo2:S:RegionID=U;RegionInfo3:S:CPUClassID=S32,CPURatio=S32,ColoName=Var1,ProductSKU=Var1,ProductName=Var1;RegionInfo4:V:RegionFlagsExtended=U64,RegionProtocols=U64"},
	{"RegionHandshakeReply",FL,149,2,"AgentData:S:AgentID=U,SessionID=U;RegionInfo:S:Flags=U32"},
	{"CoarseLocationUpdate",FM,6,1,"Location:V:X=U8,Y=U8,Z=U8;Index:S:You=S16,Prey=S16;AgentData:V:AgentID=U"},
	{"ImageData",FH,9,1,"ImageID:S:ID=U,Codec=U8,Size=U32,Packets=U16;ImageData:S:Data=Var2"},
	{"ImagePacket",FH,10,1,"ImageID:S:ID=U,Packet=U16;ImageData:S:Data=Var2"},
	{"LayerData",FH,11,1,"LayerID:S:Type=U8;LayerData:S:Data=Var2"},
	{"ObjectUpdate",FH,12,3,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:ID=U32,State=U8,FullID=U,CRC=U32,PCode=U8,Material=U8,ClickAction=U8,Scale=V3,ObjectData=Var1,ParentID=U32,UpdateFlags=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16,TextureEntry=Var2,TextureAnim=Var1,NameValue=Var2,Data=Var2,Text=Var1,TextColor=Fixed    4,MediaURL=Var1,PSBlock=Var1,ExtraParams=Var1,Sound=U,OwnerID=U,Gain=F32,Flags=U8,Radius=F32,JointType=U8,JointPivot=V3,JointAxisOrAnchor=V3"},
	{"ObjectUpdateCompressed",FH,13,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:UpdateFlags=U32,Data=Var2"},
	{"ObjectUpdateCached",FH,14,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:ID=U32,CRC=U32,UpdateFlags=U32"},
	{"ImprovedTerseObjectUpdate",FH,15,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:Data=Var1,TextureEntry=Var2"},
	{"KillObject",FH,16,1,"ObjectData:V:ID=U32"},
	{"CrossedRegion",FM,7,1,"AgentData:S:AgentID=U,SessionID=U;RegionData:S:SimIP=IPADDR,SimPort=IPPORT,RegionHandle=U64,SeedCapability=Var2;Info:S:Position=V3,LookAt=V3"},
	{"SimulatorViewerTimeMessage",FL,150,1,"TimeInfo:S:UsecSinceStart=U64,SecPerDay=U32,SecPerYear=U32,SunDirection=V3,SunPhase=F32,SunAngVelocity=V3"},
	{"EnableSimulator",FL,151,1,"SimulatorInfo:S:Handle=U64,IP=IPADDR,Port=IPPORT"},
	{"DisableSimulator",FL,152,1,""},
	{"ConfirmEnableSimulator",FM,8,1,"AgentData:S:AgentID=U,SessionID=U"},
	{"TransferRequest",FL,153,2,"TransferInfo:S:TransferID=U,ChannelType=S32,SourceType=S32,Priority=F32,Params=Var2"},
	{"TransferInfo",FL,154,2,"TransferInfo:S:TransferID=U,ChannelType=S32,TargetType=S32,Status=S32,Size=S32,Params=Var2"},
	{"TransferPacket",FH,17,0,"TransferData:S:TransferID=U,ChannelType=S32,Packet=S32,Status=S32,Data=Var2"},
	{"TransferAbort",FL,155,2,"TransferInfo:S:TransferID=U,ChannelType=S32"},
	{"RequestXfer",FL,156,2,"XferID:S:ID=U64,Filename=Var1,FilePath=U8,DeleteOnCompletion=BOOL,UseBigPackets=BOOL,VFileID=U,VFileType=S16"},
	{"SendXferPacket",FH,18,0,"XferID:S:ID=U64,Packet=U32;DataPacket:S:Data=Var2"},
	{"ConfirmXferPacket",FH,19,0,"XferID:S:ID=U64,Packet=U32"},
	{"AbortXfer",FL,157,0,"XferID:S:ID=U64,Result=S32"},
	{"AvatarAnimation",FH,20,1,"Sender:S:ID=U;AnimationList:V:AnimID=U,AnimSequenceID=S32;AnimationSourceList:V:ObjectID=U;PhysicalAvatarEventList:V:TypeData=Var1"},
	{"AvatarAppearance",FL,158,3,"Sender:S:ID=U,IsTrial=BOOL;ObjectData:S:TextureEntry=Var2;VisualParam:V:ParamValue=U8;AppearanceData:V:AppearanceVersion=U8,CofVersion=S32,Flags=U32;AppearanceHover:V:HoverHeight=V3;AttachmentBlock:V:ID=U,AttachmentPoint=U8"},
	{"AvatarSitResponse",FH,21,3,"SitObject:S:ID=U;SitTransform:S:AutoPilot=BOOL,SitPosition=V3,SitRotation=Q,CameraEyeOffset=V3,CameraAtOffset=V3,ForceMouselook=BOOL"},
	{"SetFollowCamProperties",FL,159,1,"ObjectData:S:ObjectID=U;CameraProperty:V:Type=S32,Value=F32"},
	{"ClearFollowCamProperties",FL,160,1,"ObjectData:S:ObjectID=U"},
	{"CameraConstraint",FH,22,3,"CameraCollidePlane:S:Plane=V4"},
	{"ObjectProperties",FM,9,3,"ObjectData:V:ObjectID=U,CreatorID=U,OwnerID=U,GroupID=U,CreationDate=U64,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,OwnershipCost=S32,SaleType=U8,SalePrice=S32,AggregatePerms=U8,AggregatePermTextures=U8,AggregatePermTexturesOwner=U8,Category=U32,InventorySerial=S16,ItemID=U,FolderID=U,FromTaskID=U,LastOwnerID=U,Name=Var1,Description=Var1,TouchName=Var1,SitName=Var1,TextureID=Var1"},
	{"ObjectPropertiesFamily",FM,10,3,"ObjectData:S:RequestFlags=U32,ObjectID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,OwnershipCost=S32,SaleType=U8,SalePrice=S32,Category=U32,LastOwnerID=U,Name=Var1,Description=Var1"},
	{"RequestPayPrice",FL,161,0,"ObjectData:S:ObjectID=U"},
	{"PayPriceReply",FL,162,1,"ObjectData:S:ObjectID=U,DefaultPayPrice=S32;ButtonData:V:PayButton=S32"},
	{"KickUser",FL,163,1,"TargetBlock:S:TargetIP=IPADDR,TargetPort=IPPORT;UserInfo:S:AgentID=U,SessionID=U,Reason=Var2"},
	{"KickUserAck",FL,164,1,"UserInfo:S:SessionID=U,Flags=U32"},
	{"GodKickUser",FL,165,0,"UserInfo:S:GodID=U,GodSessionID=U,AgentID=U,KickFlags=U32,Reason=Var2"},
	{"SystemKickUser",FL,166,1,"AgentInfo:V:AgentID=U"},
	{"EjectUser",FL,167,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:TargetID=U,Flags=U32"},
	{"FreezeUser",FL,168,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:TargetID=U,Flags=U32"},
	{"AvatarPropertiesRequest",FL,169,0,"AgentData:S:AgentID=U,SessionID=U,AvatarID=U"},
	{"AvatarPropertiesRequestBackend",FL,170,1,"AgentData:S:AgentID=U,AvatarID=U,GodLevel=U8,WebProfilesDisabled=BOOL"},
	{"AvatarPropertiesReply",FL,171,3,"AgentData:S:AgentID=U,AvatarID=U;PropertiesData:S:ImageID=U,FLImageID=U,PartnerID=U,AboutText=Var2,FLAboutText=Var1,BornOn=Var1,ProfileURL=Var1,CharterMember=Var1,Flags=U32"},
	{"AvatarInterestsReply",FL,172,3,"AgentData:S:AgentID=U,AvatarID=U;PropertiesData:S:WantToMask=U32,WantToText=Var1,SkillsMask=U32,SkillsText=Var1,LanguagesText=Var1"},
	{"AvatarGroupsReply",FL,173,3,"AgentData:S:AgentID=U,AvatarID=U;GroupData:V:GroupPowers=U64,AcceptNotices=BOOL,GroupTitle=Var1,GroupID=U,GroupName=Var1,GroupInsigniaID=U;NewGroupData:S:ListInProfile=BOOL"},
	{"AvatarPropertiesUpdate",FL,174,2,"AgentData:S:AgentID=U,SessionID=U;PropertiesData:S:ImageID=U,FLImageID=U,AboutText=Var2,FLAboutText=Var1,AllowPublish=BOOL,MaturePublish=BOOL,ProfileURL=Var1"},
	{"AvatarInterestsUpdate",FL,175,2,"AgentData:S:AgentID=U,SessionID=U;PropertiesData:S:WantToMask=U32,WantToText=Var1,SkillsMask=U32,SkillsText=Var1,LanguagesText=Var1"},
	{"AvatarNotesReply",FL,176,1,"AgentData:S:AgentID=U;Data:S:TargetID=U,Notes=Var2"},
	{"AvatarNotesUpdate",FL,177,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:TargetID=U,Notes=Var2"},
	{"AvatarPicksReply",FL,178,1,"AgentData:S:AgentID=U,TargetID=U;Data:V:PickID=U,PickName=Var1"},
	{"EventInfoRequest",FL,179,0,"AgentData:S:AgentID=U,SessionID=U;EventData:S:EventID=U32"},
	{"EventInfoReply",FL,180,1,"AgentData:S:AgentID=U;EventData:S:EventID=U32,Creator=Var1,Name=Var1,Category=Var1,Desc=Var2,Date=Var1,DateUTC=U32,Duration=U32,Cover=U32,Amount=U32,SimName=Var1,GlobalPos=V3d,EventFlags=U32"},
	{"EventNotificationAddRequest",FL,181,0,"AgentData:S:AgentID=U,SessionID=U;EventData:S:EventID=U32"},
	{"EventNotificationRemoveRequest",FL,182,0,"AgentData:S:AgentID=U,SessionID=U;EventData:S:EventID=U32"},
	{"EventGodDelete",FL,183,0,"AgentData:S:AgentID=U,SessionID=U;EventData:S:EventID=U32;QueryData:S:QueryID=U,QueryText=Var1,QueryFlags=U32,QueryStart=S32"},
	{"PickInfoReply",FL,184,1,"AgentData:S:AgentID=U;Data:S:PickID=U,CreatorID=U,TopPick=BOOL,ParcelID=U,Name=Var1,Desc=Var2,SnapshotID=U,User=Var1,OriginalName=Var1,SimName=Var1,PosGlobal=V3d,SortOrder=S32,Enabled=BOOL"},
	{"PickInfoUpdate",FL,185,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:PickID=U,CreatorID=U,TopPick=BOOL,ParcelID=U,Name=Var1,Desc=Var2,SnapshotID=U,PosGlobal=V3d,SortOrder=S32,Enabled=BOOL"},
	{"PickDelete",FL,186,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:PickID=U"},
	{"PickGodDelete",FL,187,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:PickID=U,QueryID=U"},
	{"ScriptQuestion",FL,188,1,"Data:S:TaskID=U,ItemID=U,ObjectName=Var1,ObjectOwner=Var1,Questions=S32;Experience:S:ExperienceID=U"},
	{"ScriptControlChange",FL,189,1,"Data:V:TakeControls=BOOL,Controls=U32,PassToAgent=BOOL"},
	{"ScriptDialog",FL,190,3,"Data:S:ObjectID=U,FirstName=Var1,LastName=Var1,ObjectName=Var1,Message=Var2,ChatChannel=S32,ImageID=U;Buttons:V:ButtonLabel=Var1;OwnerData:V:OwnerID=U"},
	{"ScriptDialogReply",FL,191,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:ObjectID=U,ChatChannel=S32,ButtonIndex=S32,ButtonLabel=Var1"},
	{"ForceScriptControlRelease",FL,192,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"RevokePermissions",FL,193,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:ObjectID=U,ObjectPermissions=U32"},
	{"LoadURL",FL,194,1,"Data:S:ObjectName=Var1,ObjectID=U,OwnerID=U,OwnerIsGroup=BOOL,Message=Var1,URL=Var1"},
	{"ScriptTeleportRequest",FL,195,1,"Data:S:ObjectName=Var1,SimName=Var1,SimPosition=V3,LookAt=V3;Options:V:Flags=U32"},
	{"ParcelOverlay",FL,196,3,"ParcelData:S:SequenceID=S32,Data=Var2"},
	{"ParcelPropertiesRequest",FM,11,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:SequenceID=S32,West=F32,South=F32,East=F32,North=F32,SnapSelection=BOOL"},
	{"ParcelPropertiesRequestByID",FL,197,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:SequenceID=S32,LocalID=S32"},
	{"ParcelProperties",FH,23,3,"ParcelData:S:RequestResult=S32,SequenceID=S32,SnapSelection=BOOL,SelfCount=S32,OtherCount=S32,PublicCount=S32,LocalID=S32,OwnerID=U,IsGroupOwned=BOOL,AuctionID=U32,ClaimDate=S32,ClaimPrice=S32,RentPrice=S32,AABBMin=V3,AABBMax=V3,Bitmap=Var2,Area=S32,Status=U8,SimWideMaxPrims=S32,SimWideTotalPrims=S32,MaxPrims=S32,TotalPrims=S32,OwnerPrims=S32,GroupPrims=S32,OtherPrims=S32,SelectedPrims=S32,ParcelPrimBonus=F32,OtherCleanTime=S32,ParcelFlags=U32,SalePrice=S32,Name=Var1,Desc=Var1,MusicURL=Var1,MediaURL=Var1,MediaID=U,MediaAutoScale=U8,GroupID=U,PassPrice=S32,PassHours=F32,Category=U8,AuthBuyerID=U,SnapshotID=U,UserLocation=V3,UserLookAt=V3,LandingType=U8,RegionPushOverride=BOOL,RegionDenyAnonymous=BOOL,RegionDenyIdentified=BOOL,RegionDenyTransacted=BOOL;AgeVerificationBlock:S:RegionDenyAgeUnverified=BOOL;RegionAllowAccessBlock:S:RegionAllowAccessOverride=BOOL;ParcelEnvironmentBlock:S:ParcelEnvironmentVersion=S32,RegionAllowEnvironmentOverride=BOOL"},
	{"ParcelPropertiesUpdate",FL,198,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,Flags=U32,ParcelFlags=U32,SalePrice=S32,Name=Var1,Desc=Var1,MusicURL=Var1,MediaURL=Var1,MediaID=U,MediaAutoScale=U8,GroupID=U,PassPrice=S32,PassHours=F32,Category=U8,AuthBuyerID=U,SnapshotID=U,UserLocation=V3,UserLookAt=V3,LandingType=U8"},
	{"ParcelReturnObjects",FL,199,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,ReturnType=U32;TaskIDs:V:TaskID=U;OwnerIDs:V:OwnerID=U"},
	{"ParcelSetOtherCleanTime",FL,200,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,OtherCleanTime=S32"},
	{"ParcelDisableObjects",FL,201,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,ReturnType=U32;TaskIDs:V:TaskID=U;OwnerIDs:V:OwnerID=U"},
	{"ParcelSelectObjects",FL,202,2,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,ReturnType=U32;ReturnIDs:V:ReturnID=U"},
	{"EstateCovenantRequest",FL,203,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"EstateCovenantReply",FL,204,1,"Data:S:CovenantID=U,CovenantTimestamp=U32,EstateName=Var1,EstateOwnerID=U"},
	{"ForceObjectSelect",FL,205,1,"Header:S:ResetList=BOOL;Data:V:LocalID=U32"},
	{"ParcelBuyPass",FL,206,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32"},
	{"ParcelDeedToGroup",FL,207,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U,LocalID=S32"},
	{"ParcelReclaim",FL,208,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:LocalID=S32"},
	{"ParcelClaim",FL,209,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U,IsGroupOwned=BOOL,Final=BOOL;ParcelData:V:West=F32,South=F32,East=F32,North=F32"},
	{"ParcelJoin",FL,210,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:West=F32,South=F32,East=F32,North=F32"},
	{"ParcelDivide",FL,211,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:West=F32,South=F32,East=F32,North=F32"},
	{"ParcelRelease",FL,212,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:LocalID=S32"},
	{"ParcelBuy",FL,213,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U,IsGroupOwned=BOOL,RemoveContribution=BOOL,LocalID=S32,Final=BOOL;ParcelData:S:Price=S32,Area=S32"},
	{"ParcelGodForceOwner",FL,214,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:OwnerID=U,LocalID=S32"},
	{"ParcelAccessListRequest",FL,215,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:SequenceID=S32,Flags=U32,LocalID=S32"},
	{"ParcelAccessListReply",FL,216,3,"Data:S:AgentID=U,SequenceID=S32,Flags=U32,LocalID=S32;List:V:ID=U,Time=S32,Flags=U32"},
	{"ParcelAccessListUpdate",FL,217,2,"AgentData:S:AgentID=U,SessionID=U;Data:S:Flags=U32,LocalID=S32,TransactionID=U,SequenceID=S32,Sections=S32;List:V:ID=U,Time=S32,Flags=U32"},
	{"ParcelDwellRequest",FL,218,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:LocalID=S32,ParcelID=U"},
	{"ParcelDwellReply",FL,219,1,"AgentData:S:AgentID=U;Data:S:LocalID=S32,ParcelID=U,Dwell=F32"},
	{"RequestParcelTransfer",FL,220,3,"Data:S:TransactionID=U,TransactionTime=U32,SourceID=U,DestID=U,OwnerID=U,Flags=U8,TransactionType=S32,Amount=S32,BillableArea=S32,ActualArea=S32,Final=BOOL,RegionID=U,GridX=U32,GridY=U32"},
	{"UpdateParcel",FL,221,3,"ParcelData:S:ParcelID=U,RegionHandle=U64,OwnerID=U,GroupOwned=BOOL,Status=U8,Name=Var1,Description=Var1,MusicURL=Var1,RegionX=F32,RegionY=F32,ActualArea=S32,BillableArea=S32,ShowDir=BOOL,IsForSale=BOOL,Category=U8,SnapshotID=U,UserLocation=V3,SalePrice=S32,AuthorizedBuyerID=U,AllowPublish=BOOL,MaturePublish=BOOL"},
	{"RemoveParcel",FL,222,1,"ParcelData:V:ParcelID=U"},
	{"MergeParcel",FL,223,1,"MasterParcelData:S:MasterID=U;SlaveParcelData:V:SlaveID=U"},
	{"LogParcelChanges",FL,224,3,"AgentData:S:AgentID=U;RegionData:S:RegionHandle=U64;ParcelData:V:ParcelID=U,OwnerID=U,IsOwnerGroup=BOOL,ActualArea=S32,Action=S8,TransactionID=U"},
	{"CheckParcelSales",FL,225,1,"RegionData:V:RegionHandle=U64"},
	{"ParcelSales",FL,226,1,"ParcelData:V:ParcelID=U,BuyerID=U"},
	{"ParcelGodMarkAsContent",FL,227,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32"},
	{"ViewerStartAuction",FL,228,0,"AgentData:S:AgentID=U,SessionID=U;ParcelData:S:LocalID=S32,SnapshotID=U"},
	{"StartAuction",FL,229,1,"AgentData:S:AgentID=U;ParcelData:S:ParcelID=U,SnapshotID=U,Name=Var1"},
	{"ConfirmAuctionStart",FL,230,1,"AuctionData:S:ParcelID=U,AuctionID=U32"},
	{"CompleteAuction",FL,231,1,"ParcelData:V:ParcelID=U"},
	{"CancelAuction",FL,232,1,"ParcelData:V:ParcelID=U"},
	{"CheckParcelAuctions",FL,233,1,"RegionData:V:RegionHandle=U64"},
	{"ParcelAuctions",FL,234,1,"ParcelData:V:ParcelID=U,WinnerID=U"},
	{"UUIDNameRequest",FL,235,0,"UUIDNameBlock:V:ID=U"},
	{"UUIDNameReply",FL,236,1,"UUIDNameBlock:V:ID=U,FirstName=Var1,LastName=Var1"},
	{"UUIDGroupNameRequest",FL,237,0,"UUIDNameBlock:V:ID=U"},
	{"UUIDGroupNameReply",FL,238,1,"UUIDNameBlock:V:ID=U,GroupName=Var1"},
	{"ChatPass",FL,239,3,"ChatData:S:Channel=S32,Position=V3,ID=U,OwnerID=U,Name=Variable    1,SourceType=U8,Type=U8,Radius=F32,SimAccess=U8,Message=Variable    2"},
	{"EdgeDataPacket",FH,24,3,"EdgeData:S:LayerType=U8,Direction=U8,LayerData=Var2"},
	{"SimStatus",FM,12,1,"SimStatus:S:CanAcceptAgents=BOOL,CanAcceptTasks=BOOL;SimFlags:S:Flags=U64"},
	{"ChildAgentUpdate",FH,25,3,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=U,SessionID=U,AgentPos=V3,AgentVel=V3,Center=V3,Size=V3,AtAxis=V3,LeftAxis=V3,UpAxis=V3,ChangedGrid=BOOL,Far=F32,Aspect=F32,Throttles=Var1,LocomotionState=U32,HeadRotation=Q,BodyRotation=Q,ControlFlags=U32,EnergyLevel=F32,GodLevel=U8,AlwaysRun=BOOL,PreyAgent=U,AgentAccess=U8,AgentTextures=Var2,ActiveGroupID=U;GroupData:V:GroupID=U,GroupPowers=U64,AcceptNotices=BOOL;AnimationData:V:Animation=U,ObjectID=U;GranterBlock:V:GranterID=U;NVPairData:V:NVPairs=Var2;VisualParam:V:ParamValue=U8;AgentAccess:V:AgentLegacyAccess=U8,AgentMaxAccess=U8;AgentInfo:V:Flags=U32;AgentInventoryHost:V:InventoryHost=Var1"},
	{"ChildAgentAlive",FH,26,1,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=U,SessionID=U"},
	{"ChildAgentPositionUpdate",FH,27,1,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=U,SessionID=U,AgentPos=V3,AgentVel=V3,Center=V3,Size=V3,AtAxis=V3,LeftAxis=V3,UpAxis=V3,ChangedGrid=BOOL"},
	{"ChildAgentDying",FL,240,3,"AgentData:S:AgentID=U,SessionID=U"},
	{"ChildAgentUnknown",FL,241,1,"AgentData:S:AgentID=U,SessionID=U"},
	{"AtomicPassObject",FH,28,1,"TaskData:S:TaskID=U,AttachmentNeedsSave=BOOL"},
	{"KillChildAgents",FL,242,1,"IDBlock:S:AgentID=U"},
	{"GetScriptRunning",FL,243,0,"Script:S:ObjectID=U,ItemID=U"},
	{"ScriptRunningReply",FL,244,0,"Script:S:ObjectID=U,ItemID=U,Running=BOOL"},
	{"SetScriptRunning",FL,245,0,"AgentData:S:AgentID=U,SessionID=U;Script:S:ObjectID=U,ItemID=U,Running=BOOL"},
	{"ScriptReset",FL,246,0,"AgentData:S:AgentID=U,SessionID=U;Script:S:ObjectID=U,ItemID=U"},
	{"ScriptSensorRequest",FL,247,3,"Requester:S:SourceID=U,RequestID=U,SearchID=U,SearchPos=V3,SearchDir=Q,SearchName=Var1,Type=S32,Range=F32,Arc=F32,RegionHandle=U64,SearchRegions=U8"},
	{"ScriptSensorReply",FL,248,3,"Requester:S:SourceID=U;SensedData:V:ObjectID=U,OwnerID=U,GroupID=U,Position=V3,Velocity=V3,Rotation=Q,Name=Var1,Type=S32,Range=F32"},
	{"CompleteAgentMovement",FL,249,0,"AgentData:S:AgentID=U,SessionID=U,CircuitCode=U32"},
	{"AgentMovementComplete",FL,250,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:Position=V3,LookAt=V3,RegionHandle=U64,Timestamp=U32;SimData:S:ChannelVersion=Var2"},
	{"DataServerLogout",FL,251,1,"UserData:S:AgentID=U,ViewerIP=IPADDR,Disconnect=BOOL,SessionID=U"},
	{"LogoutRequest",FL,252,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"LogoutReply",FL,253,3,"AgentData:S:AgentID=U,SessionID=U;InventoryData:V:ItemID=U"},
	{"ImprovedInstantMessage",FL,254,2,"AgentData:S:AgentID=U,SessionID=U;MessageBlock:S:FromGroup=BOOL,ToAgentID=U,ParentEstateID=U32,RegionID=U,Position=V3,Offline=U8,Dialog=U8,ID=U,Timestamp=U32,FromAgentName=Var1,Message=Var2,BinaryBucket=Var2;EstateBlock:S:EstateID=U32;MetaData:V:Data=Variable    2"},
	{"RetrieveInstantMessages",FL,255,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"FindAgent",FL,256,0,"AgentBlock:S:Hunter=U,Prey=U,SpaceIP=IPADDR;LocationBlock:V:GlobalX=F64,GlobalY=F64"},
	{"RequestGodlikePowers",FL,257,0,"AgentData:S:AgentID=U,SessionID=U;RequestBlock:S:Godlike=BOOL,Token=U"},
	{"GrantGodlikePowers",FL,258,1,"AgentData:S:AgentID=U,SessionID=U;GrantData:S:GodLevel=U8,Token=U"},
	{"GodlikeMessage",FL,259,2,"AgentData:S:AgentID=U,SessionID=U,TransactionID=U;MethodData:S:Method=Var1,Invoice=U;ParamList:V:Parameter=Var1"},
	{"EstateOwnerMessage",FL,260,2,"AgentData:S:AgentID=U,SessionID=U,TransactionID=U;MethodData:S:Method=Var1,Invoice=U;ParamList:V:Parameter=Var1"},
	{"GenericMessage",FL,261,2,"AgentData:S:AgentID=U,SessionID=U,TransactionID=U;MethodData:S:Method=Var1,Invoice=U;ParamList:V:Parameter=Var1"},
	{"GenericStreamingMessage",FH,31,1,"MethodData:S:Method=U16;DataBlock:S:Data=Var2"},
	{"LargeGenericMessage",FL,430,0,"AgentData:S:AgentID=U,SessionID=U,TransactionID=U;MethodData:S:Method=Var1,Invoice=U;ParamList:V:Parameter=Var2"},
	{"MuteListRequest",FL,262,0,"AgentData:S:AgentID=U,SessionID=U;MuteData:S:MuteCRC=U32"},
	{"UpdateMuteListEntry",FL,263,0,"AgentData:S:AgentID=U,SessionID=U;MuteData:S:MuteID=U,MuteName=Var1,MuteType=S32,MuteFlags=U32"},
	{"RemoveMuteListEntry",FL,264,0,"AgentData:S:AgentID=U,SessionID=U;MuteData:S:MuteID=U,MuteName=Var1"},
	{"CopyInventoryFromNotecard",FL,265,2,"AgentData:S:AgentID=U,SessionID=U;NotecardData:S:NotecardItemID=U,ObjectID=U;InventoryData:V:ItemID=U,FolderID=U"},
	{"UpdateInventoryItem",FL,266,2,"AgentData:S:AgentID=U,SessionID=U,TransactionID=U;InventoryData:V:ItemID=U,FolderID=U,CallbackID=U32,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"UpdateCreateInventoryItem",FL,267,3,"AgentData:S:AgentID=U,SimApproved=BOOL,TransactionID=U;InventoryData:V:ItemID=U,FolderID=U,CallbackID=U32,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"MoveInventoryItem",FL,268,2,"AgentData:S:AgentID=U,SessionID=U,Stamp=BOOL;InventoryData:V:ItemID=U,FolderID=U,NewName=Var1"},
	{"CopyInventoryItem",FL,269,2,"AgentData:S:AgentID=U,SessionID=U;InventoryData:V:CallbackID=U32,OldAgentID=U,OldItemID=U,NewFolderID=U,NewName=Var1"},
	{"RemoveInventoryItem",FL,270,0,"AgentData:S:AgentID=U,SessionID=U;InventoryData:V:ItemID=U"},
	{"ChangeInventoryItemFlags",FL,271,0,"AgentData:S:AgentID=U,SessionID=U;InventoryData:V:ItemID=U,Flags=U32"},
	{"SaveAssetIntoInventory",FL,272,1,"AgentData:S:AgentID=U;InventoryData:S:ItemID=U,NewAssetID=U"},
	{"CreateInventoryFolder",FL,273,0,"AgentData:S:AgentID=U,SessionID=U;FolderData:S:FolderID=U,ParentID=U,Type=S8,Name=Var1"},
	{"UpdateInventoryFolder",FL,274,0,"AgentData:S:AgentID=U,SessionID=U;FolderData:V:FolderID=U,ParentID=U,Type=S8,Name=Var1"},
	{"MoveInventoryFolder",FL,275,2,"AgentData:S:AgentID=U,SessionID=U,Stamp=BOOL;InventoryData:V:FolderID=U,ParentID=U"},
	{"RemoveInventoryFolder",FL,276,0,"AgentData:S:AgentID=U,SessionID=U;FolderData:V:FolderID=U"},
	{"FetchInventoryDescendents",FL,277,2,"AgentData:S:AgentID=U,SessionID=U;InventoryData:S:FolderID=U,OwnerID=U,SortOrder=S32,FetchFolders=BOOL,FetchItems=BOOL"},
	{"InventoryDescendents",FL,278,3,"AgentData:S:AgentID=U,FolderID=U,OwnerID=U,Version=S32,Descendents=S32;FolderData:V:FolderID=U,ParentID=U,Type=S8,Name=Var1;ItemData:V:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"FetchInventory",FL,279,2,"AgentData:S:AgentID=U,SessionID=U;InventoryData:V:OwnerID=U,ItemID=U"},
	{"FetchInventoryReply",FL,280,3,"AgentData:S:AgentID=U;InventoryData:V:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"BulkUpdateInventory",FL,281,3,"AgentData:S:AgentID=U,TransactionID=U;FolderData:V:FolderID=U,ParentID=U,Type=S8,Name=Var1;ItemData:V:ItemID=U,CallbackID=U32,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"RequestInventoryAsset",FL,282,1,"QueryData:S:QueryID=U,AgentID=U,OwnerID=U,ItemID=U"},
	{"InventoryAssetResponse",FL,283,1,"QueryData:S:QueryID=U,AssetID=U,IsReadable=BOOL"},
	{"RemoveInventoryObjects",FL,284,0,"AgentData:S:AgentID=U,SessionID=U;FolderData:V:FolderID=U;ItemData:V:ItemID=U"},
	{"PurgeInventoryDescendents",FL,285,2,"AgentData:S:AgentID=U,SessionID=U;InventoryData:S:FolderID=U"},
	{"UpdateTaskInventory",FL,286,2,"AgentData:S:AgentID=U,SessionID=U;UpdateData:S:LocalID=U32,Key=U8;InventoryData:S:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"RemoveTaskInventory",FL,287,2,"AgentData:S:AgentID=U,SessionID=U;InventoryData:S:LocalID=U32,ItemID=U"},
	{"MoveTaskInventory",FL,288,0,"AgentData:S:AgentID=U,SessionID=U,FolderID=U;InventoryData:S:LocalID=U32,ItemID=U"},
	{"RequestTaskInventory",FL,289,0,"AgentData:S:AgentID=U,SessionID=U;InventoryData:S:LocalID=U32"},
	{"ReplyTaskInventory",FL,290,3,"InventoryData:S:TaskID=U,Serial=S16,Filename=Var1"},
	{"DeRezObject",FL,291,2,"AgentData:S:AgentID=U,SessionID=U;AgentBlock:S:GroupID=U,Destination=U8,DestinationID=U,TransactionID=U,PacketCount=U8,PacketNumber=U8;ObjectData:V:ObjectLocalID=U32"},
	{"DeRezAck",FL,292,1,"TransactionData:S:TransactionID=U,Success=BOOL"},
	{"RezObject",FL,293,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;RezData:S:FromTaskID=U,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=U,RayEndIsIntersection=BOOL,RezSelected=BOOL,RemoveItem=BOOL,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32;InventoryData:S:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"RezObjectFromNotecard",FL,294,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;RezData:S:FromTaskID=U,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=U,RayEndIsIntersection=BOOL,RezSelected=BOOL,RemoveItem=BOOL,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32;NotecardData:S:NotecardItemID=U,ObjectID=U;InventoryData:V:ItemID=U"},
	{"TransferInventory",FL,295,3,"InfoBlock:S:SourceID=U,DestID=U,TransactionID=U;InventoryBlock:V:InventoryID=U,Type=S8;ValidationBlock:S:NeedsValidation=BOOL,EstateID=U32"},
	{"TransferInventoryAck",FL,296,3,"InfoBlock:S:TransactionID=U,InventoryID=U"},
	{"AcceptFriendship",FL,297,0,"AgentData:S:AgentID=U,SessionID=U;TransactionBlock:S:TransactionID=U;FolderData:V:FolderID=U"},
	{"DeclineFriendship",FL,298,0,"AgentData:S:AgentID=U,SessionID=U;TransactionBlock:S:TransactionID=U"},
	{"FormFriendship",FL,299,1,"AgentBlock:S:SourceID=U,DestID=U"},
	{"TerminateFriendship",FL,300,0,"AgentData:S:AgentID=U,SessionID=U;ExBlock:S:OtherID=U"},
	{"OfferCallingCard",FL,301,0,"AgentData:S:AgentID=U,SessionID=U;AgentBlock:S:DestID=U,TransactionID=U"},
	{"AcceptCallingCard",FL,302,0,"AgentData:S:AgentID=U,SessionID=U;TransactionBlock:S:TransactionID=U;FolderData:V:FolderID=U"},
	{"DeclineCallingCard",FL,303,0,"AgentData:S:AgentID=U,SessionID=U;TransactionBlock:S:TransactionID=U"},
	{"RezScript",FL,304,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;UpdateBlock:S:ObjectLocalID=U32,Enabled=BOOL;InventoryBlock:S:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32;NewScriptInfo:V:TemplateID=U"},
	{"CreateInventoryItem",FL,305,2,"AgentData:S:AgentID=U,SessionID=U;InventoryBlock:S:CallbackID=U32,FolderID=U,TransactionID=U,NextOwnerMask=U32,Type=S8,InvType=S8,WearableType=U8,Name=Var1,Description=Var1"},
	{"CreateLandmarkForEvent",FL,306,2,"AgentData:S:AgentID=U,SessionID=U;EventData:S:EventID=U32;InventoryBlock:S:FolderID=U,Name=Var1"},
	{"EventLocationRequest",FL,307,3,"QueryData:S:QueryID=U;EventData:S:EventID=U32"},
	{"EventLocationReply",FL,308,3,"QueryData:S:QueryID=U;EventData:S:Success=BOOL,RegionID=U,RegionPos=V3"},
	{"RegionHandleRequest",FL,309,0,"RequestBlock:S:RegionID=U"},
	{"RegionIDAndHandleReply",FL,310,1,"ReplyBlock:S:RegionID=U,RegionHandle=U64"},
	{"MoneyTransferRequest",FL,311,2,"AgentData:S:AgentID=U,SessionID=U;MoneyData:S:SourceID=U,DestID=U,Flags=U8,Amount=S32,AggregatePermNextOwner=U8,AggregatePermInventory=U8,TransactionType=S32,Description=Var1"},
	{"MoneyTransferBackend",FL,312,3,"MoneyData:S:TransactionID=U,TransactionTime=U32,SourceID=U,DestID=U,Flags=U8,Amount=S32,AggregatePermNextOwner=U8,AggregatePermInventory=U8,TransactionType=S32,RegionID=U,GridX=U32,GridY=U32,Description=Var1"},
	{"MoneyBalanceRequest",FL,313,2,"AgentData:S:AgentID=U,SessionID=U;MoneyData:S:TransactionID=U"},
	{"MoneyBalanceReply",FL,314,3,"MoneyData:S:AgentID=U,TransactionID=U,TransactionSuccess=BOOL,MoneyBalance=S32,SquareMetersCredit=S32,SquareMetersCommitted=S32,Description=Var1;TransactionInfo:S:TransactionType=S32,SourceID=U,IsSourceGroup=BOOL,DestID=U,IsDestGroup=BOOL,Amount=S32,ItemDescription=Var1"},
	{"RoutedMoneyBalanceReply",FL,315,3,"TargetBlock:S:TargetIP=IPADDR,TargetPort=IPPORT;MoneyData:S:AgentID=U,TransactionID=U,TransactionSuccess=BOOL,MoneyBalance=S32,SquareMetersCredit=S32,SquareMetersCommitted=S32,Description=Var1;TransactionInfo:S:TransactionType=S32,SourceID=U,IsSourceGroup=BOOL,DestID=U,IsDestGroup=BOOL,Amount=S32,ItemDescription=Var1"},
	{"ActivateGestures",FL,316,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32;Data:V:ItemID=U,AssetID=U,GestureFlags=U32"},
	{"DeactivateGestures",FL,317,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32;Data:V:ItemID=U,GestureFlags=U32"},
	{"MuteListUpdate",FL,318,1,"MuteData:S:AgentID=U,Filename=Var1"},
	{"UseCachedMuteList",FL,319,0,"AgentData:S:AgentID=U"},
	{"GrantUserRights",FL,320,0,"AgentData:S:AgentID=U,SessionID=U;Rights:V:AgentRelated=U,RelatedRights=S32"},
	{"ChangeUserRights",FL,321,1,"AgentData:S:AgentID=U;Rights:V:AgentRelated=U,RelatedRights=S32"},
	{"OnlineNotification",FL,322,1,"AgentBlock:V:AgentID=U"},
	{"OfflineNotification",FL,323,1,"AgentBlock:V:AgentID=U"},
	{"SetStartLocationRequest",FL,324,2,"AgentData:S:AgentID=U,SessionID=U;StartLocationData:S:SimName=Var1,LocationID=U32,LocationPos=V3,LocationLookAt=V3"},
	{"SetStartLocation",FL,325,3,"StartLocationData:S:AgentID=U,RegionID=U,LocationID=U32,RegionHandle=U64,LocationPos=V3,LocationLookAt=V3"},
	{"NetTest",FL,326,0,"NetBlock:S:Port=IPPORT"},
	{"SetCPURatio",FL,327,0,"Data:S:Ratio=U8"},
	{"SimCrashed",FL,328,0,"Data:S:RegionX=U32,RegionY=U32;Users:V:AgentID=U"},
	{"NameValuePair",FL,329,1,"TaskData:S:ID=U;NameValueData:V:NVPair=Variable    2"},
	{"RemoveNameValuePair",FL,330,1,"TaskData:S:ID=U;NameValueData:V:NVPair=Variable    2"},
	{"UpdateAttachment",FL,331,3,"AgentData:S:AgentID=U,SessionID=U;AttachmentBlock:S:AttachmentPoint=U8;OperationData:S:AddItem=BOOL,UseExistingAsset=BOOL,ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"RemoveAttachment",FL,332,0,"AgentData:S:AgentID=U,SessionID=U;AttachmentBlock:S:AttachmentPoint=U8,ItemID=U"},
	{"SoundTrigger",FH,29,0,"SoundData:S:SoundID=U,OwnerID=U,ObjectID=U,ParentID=U,Handle=U64,Position=V3,Gain=F32"},
	{"AttachedSound",FM,13,1,"DataBlock:S:SoundID=U,ObjectID=U,OwnerID=U,Gain=F32,Flags=U8"},
	{"AttachedSoundGainChange",FM,14,1,"DataBlock:S:ObjectID=U,Gain=F32"},
	{"PreloadSound",FM,15,1,"DataBlock:V:ObjectID=U,OwnerID=U,SoundID=U"},
	{"ObjectAnimation",FH,30,1,"Sender:S:ID=U;AnimationList:V:AnimID=U,AnimSequenceID=S32"},
	{"AssetUploadRequest",FL,333,0,"AssetBlock:S:TransactionID=U,Type=S8,Tempfile=BOOL,StoreLocal=BOOL,AssetData=Var2"},
	{"AssetUploadComplete",FL,334,0,"AssetBlock:S:UUID=U,Type=S8,Success=BOOL"},
	{"EmailMessageRequest",FL,335,1,"DataBlock:S:ObjectID=U,FromAddress=Var1,Subject=Var1"},
	{"EmailMessageReply",FL,336,1,"DataBlock:S:ObjectID=U,More=U32,Time=U32,FromAddress=Var1,Subject=Var1,Data=Var2,MailFilter=Var1"},
	{"InternalScriptMail",FM,16,1,"DataBlock:S:From=Var1,To=U,Subject=Var1,Body=Var2"},
	{"ScriptDataRequest",FL,337,1,"DataBlock:V:Hash=U64,RequestType=S8,Request=Var2"},
	{"ScriptDataReply",FL,338,1,"DataBlock:V:Hash=U64,Reply=Var2"},
	{"CreateGroupRequest",FL,339,2,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:Name=Var1,Charter=Var2,ShowInList=BOOL,InsigniaID=U,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL"},
	{"CreateGroupReply",FL,340,1,"AgentData:S:AgentID=U;ReplyData:S:GroupID=U,Success=BOOL,Message=Var1"},
	{"UpdateGroupInfo",FL,341,2,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U,Charter=Var2,ShowInList=BOOL,InsigniaID=U,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL"},
	{"GroupRoleChanges",FL,342,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;RoleChange:V:RoleID=U,MemberID=U,Change=U32"},
	{"JoinGroupRequest",FL,343,2,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U"},
	{"JoinGroupReply",FL,344,1,"AgentData:S:AgentID=U;GroupData:S:GroupID=U,Success=BOOL"},
	{"EjectGroupMemberRequest",FL,345,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U;EjectData:V:EjecteeID=U"},
	{"EjectGroupMemberReply",FL,346,1,"AgentData:S:AgentID=U;GroupData:S:GroupID=U;EjectData:S:Success=BOOL"},
	{"LeaveGroupRequest",FL,347,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U"},
	{"LeaveGroupReply",FL,348,1,"AgentData:S:AgentID=U;GroupData:S:GroupID=U,Success=BOOL"},
	{"InviteGroupRequest",FL,349,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U;InviteData:V:InviteeID=U,RoleID=U"},
	{"InviteGroupResponse",FL,350,1,"InviteData:S:AgentID=U,InviteeID=U,GroupID=U,RoleID=U,MembershipFee=S32;GroupData:S:GroupLimit=S32"},
	{"GroupProfileRequest",FL,351,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U"},
	{"GroupProfileReply",FL,352,3,"AgentData:S:AgentID=U;GroupData:S:GroupID=U,Name=Var1,Charter=Var2,ShowInList=BOOL,MemberTitle=Var1,PowersMask=U64,InsigniaID=U,FounderID=U,MembershipFee=S32,OpenEnrollment=BOOL,Money=S32,GroupMembershipCount=S32,GroupRolesCount=S32,AllowPublish=BOOL,MaturePublish=BOOL,OwnerRole=U"},
	{"GroupAccountSummaryRequest",FL,353,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32"},
	{"GroupAccountSummaryReply",FL,354,3,"AgentData:S:AgentID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1,Balance=S32,TotalCredits=S32,TotalDebits=S32,ObjectTaxCurrent=S32,LightTaxCurrent=S32,LandTaxCurrent=S32,GroupTaxCurrent=S32,ParcelDirFeeCurrent=S32,ObjectTaxEstimate=S32,LightTaxEstimate=S32,LandTaxEstimate=S32,GroupTaxEstimate=S32,ParcelDirFeeEstimate=S32,NonExemptMembers=S32,LastTaxDate=Var1,TaxDate=Var1"},
	{"GroupAccountDetailsRequest",FL,355,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32"},
	{"GroupAccountDetailsReply",FL,356,3,"AgentData:S:AgentID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1;HistoryData:V:Description=Var1,Amount=S32"},
	{"GroupAccountTransactionsRequest",FL,357,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32"},
	{"GroupAccountTransactionsReply",FL,358,3,"AgentData:S:AgentID=U,GroupID=U;MoneyData:S:RequestID=U,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1;HistoryData:V:Time=Var1,User=Var1,Type=S32,Item=Var1,Amount=S32"},
	{"GroupActiveProposalsRequest",FL,359,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U;TransactionData:S:TransactionID=U"},
	{"GroupActiveProposalItemReply",FL,360,3,"AgentData:S:AgentID=U,GroupID=U;TransactionData:S:TransactionID=U,TotalNumItems=U32;ProposalData:V:VoteID=U,VoteInitiator=U,TerseDateID=Var1,StartDateTime=Var1,EndDateTime=Var1,AlreadyVoted=BOOL,VoteCast=Var1,Majority=F32,Quorum=S32,ProposalText=Var1"},
	{"GroupVoteHistoryRequest",FL,361,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U;TransactionData:S:TransactionID=U"},
	{"GroupVoteHistoryItemReply",FL,362,3,"AgentData:S:AgentID=U,GroupID=U;TransactionData:S:TransactionID=U,TotalNumItems=U32;HistoryItemData:S:VoteID=U,TerseDateID=Var1,StartDateTime=Var1,EndDateTime=Var1,VoteInitiator=U,VoteType=Var1,VoteResult=Var1,Majority=F32,Quorum=S32,ProposalText=Var2;VoteItem:V:CandidateID=U,VoteCast=Var1,NumVotes=S32"},
	{"StartGroupProposal",FL,363,2,"AgentData:S:AgentID=U,SessionID=U;ProposalData:S:GroupID=U,Quorum=S32,Majority=F32,Duration=S32,ProposalText=Var1"},
	{"GroupProposalBallot",FL,364,0,"AgentData:S:AgentID=U,SessionID=U;ProposalData:S:ProposalID=U,GroupID=U,VoteCast=Var1"},
	{"TallyVotes",FL,365,1,""},
	{"GroupMembersRequest",FL,366,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U,RequestID=U"},
	{"GroupMembersReply",FL,367,3,"AgentData:S:AgentID=U;GroupData:S:GroupID=U,RequestID=U,MemberCount=S32;MemberData:V:AgentID=U,Contribution=S32,OnlineStatus=Var1,AgentPowers=U64,Title=Var1,IsOwner=BOOL"},
	{"ActivateGroup",FL,368,2,"AgentData:S:AgentID=U,SessionID=U,GroupID=U"},
	{"SetGroupContribution",FL,369,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U,Contribution=S32"},
	{"SetGroupAcceptNotices",FL,370,0,"AgentData:S:AgentID=U,SessionID=U;Data:S:GroupID=U,AcceptNotices=BOOL;NewData:S:ListInProfile=BOOL"},
	{"GroupRoleDataRequest",FL,371,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U,RequestID=U"},
	{"GroupRoleDataReply",FL,372,1,"AgentData:S:AgentID=U;GroupData:S:GroupID=U,RequestID=U,RoleCount=S32;RoleData:V:RoleID=U,Name=Var1,Title=Var1,Description=Var1,Powers=U64,Members=U32"},
	{"GroupRoleMembersRequest",FL,373,0,"AgentData:S:AgentID=U,SessionID=U;GroupData:S:GroupID=U,RequestID=U"},
	{"GroupRoleMembersReply",FL,374,1,"AgentData:S:AgentID=U,GroupID=U,RequestID=U,TotalPairs=U32;MemberData:V:RoleID=U,MemberID=U"},
	{"GroupTitlesRequest",FL,375,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U,RequestID=U"},
	{"GroupTitlesReply",FL,376,3,"AgentData:S:AgentID=U,GroupID=U,RequestID=U;GroupData:V:Title=Var1,RoleID=U,Selected=BOOL"},
	{"GroupTitleUpdate",FL,377,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U,TitleRoleID=U"},
	{"GroupRoleUpdate",FL,378,0,"AgentData:S:AgentID=U,SessionID=U,GroupID=U;RoleData:V:RoleID=U,Name=Var1,Description=Var1,Title=Var1,Powers=U64,UpdateType=U8"},
	{"LiveHelpGroupRequest",FL,379,1,"RequestData:S:RequestID=U,AgentID=U"},
	{"LiveHelpGroupReply",FL,380,1,"ReplyData:S:RequestID=U,GroupID=U,Selection=Var1"},
	{"AgentWearablesRequest",FL,381,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"AgentWearablesUpdate",FL,382,3,"AgentData:S:AgentID=U,SessionID=U,SerialNum=U32;WearableData:V:ItemID=U,AssetID=U,WearableType=U8"},
	{"AgentIsNowWearing",FL,383,2,"AgentData:S:AgentID=U,SessionID=U;WearableData:V:ItemID=U,WearableType=U8"},
	{"AgentCachedTexture",FL,384,0,"AgentData:S:AgentID=U,SessionID=U,SerialNum=S32;WearableData:V:ID=U,TextureIndex=U8"},
	{"AgentCachedTextureResponse",FL,385,1,"AgentData:S:AgentID=U,SessionID=U,SerialNum=S32;WearableData:V:TextureID=U,TextureIndex=U8,HostName=Var1"},
	{"AgentDataUpdateRequest",FL,386,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"AgentDataUpdate",FL,387,3,"AgentData:S:AgentID=U,FirstName=Var1,LastName=Var1,GroupTitle=Var1,ActiveGroupID=U,GroupPowers=U64,GroupName=Var1"},
	{"GroupDataUpdate",FL,388,3,"AgentGroupData:V:AgentID=U,GroupID=U,AgentPowers=U64,GroupTitle=Var1"},
	{"AgentGroupDataUpdate",FL,389,3,"AgentData:S:AgentID=U;GroupData:V:GroupID=U,GroupPowers=U64,AcceptNotices=BOOL,GroupInsigniaID=U,Contribution=S32,GroupName=Var1"},
	{"AgentDropGroup",FL,390,3,"AgentData:S:AgentID=U,GroupID=U"},
	{"LogTextMessage",FL,391,3,"DataBlock:V:FromAgentId=U,ToAgentId=U,GlobalX=F64,GlobalY=F64,Time=U32,Message=Var2"},
	{"ViewerEffect",FM,17,2,"AgentData:S:AgentID=U,SessionID=U;Effect:V:ID=U,AgentID=U,Type=U8,Duration=F32,Color=Fixed    4,TypeData=Var1"},
	{"CreateTrustedCircuit",FL,392,0,"DataBlock:S:EndPointID=U,Digest=Fixed 32"},
	{"DenyTrustedCircuit",FL,393,0,"DataBlock:S:EndPointID=U"},
	{"RequestTrustedCircuit",FL,394,1,""},
	{"RezSingleAttachmentFromInv",FL,395,2,"AgentData:S:AgentID=U,SessionID=U;ObjectData:S:ItemID=U,OwnerID=U,AttachmentPt=U8,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,Name=Var1,Description=Var1"},
	{"RezMultipleAttachmentsFromInv",FL,396,2,"AgentData:S:AgentID=U,SessionID=U;HeaderData:S:CompoundMsgID=U,TotalObjects=U8,FirstDetachAll=BOOL,ItemID=U,OwnerID=U,AttachmentPt=U8,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,Name=Var1,Description=Var1"},
	{"DetachAttachmentIntoInv",FL,397,0,"ObjectData:S:AgentID=U,ItemID=U"},
	{"CreateNewOutfitAttachments",FL,398,0,"AgentData:S:AgentID=U,SessionID=U;HeaderData:S:NewFolderID=U;ObjectData:V:OldItemID=U,OldFolderID=U"},
	{"UserInfoRequest",FL,399,0,"AgentData:S:AgentID=U,SessionID=U"},
	{"UserInfoReply",FL,400,0,"AgentData:S:AgentID=U;UserData:S:IMViaEMail=BOOL,DirectoryVisibility=Var1,EMail=Var2"},
	{"UpdateUserInfo",FL,401,0,"AgentData:S:AgentID=U,SessionID=U;UserData:S:IMViaEMail=BOOL,DirectoryVisibility=Var1"},
	{"ParcelRename",FL,402,1,"ParcelData:V:ParcelID=U,NewName=Var1"},
	{"InitiateDownload",FL,403,0,"AgentData:S:AgentID=U;FileData:S:SimFilename=Var1,ViewerFilename=Var1"},
	{"SystemMessage",FL,404,3,"MethodData:S:Method=Var1,Invoice=U,Digest=Fixed 32;ParamList:V:Parameter=Var1"},
	{"MapLayerRequest",FL,405,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32,EstateID=U32,Godlike=BOOL"},
	{"MapLayerReply",FL,406,1,"AgentData:S:AgentID=U,Flags=U32;LayerData:V:Left=U32,Right=U32,Top=U32,Bottom=U32,ImageID=U"},
	{"MapBlockRequest",FL,407,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32,EstateID=U32,Godlike=BOOL;PositionData:S:MinX=U16,MaxX=U16,MinY=U16,MaxY=U16"},
	{"MapNameRequest",FL,408,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32,EstateID=U32,Godlike=BOOL;NameData:S:Name=Var1"},
	{"MapBlockReply",FL,409,1,"AgentData:S:AgentID=U,Flags=U32;Data:V:X=U16,Y=U16,Name=Var1,Access=U8,RegionFlags=U32,WaterHeight=U8,Agents=U8,MapImageID=U"},
	{"MapItemRequest",FL,410,0,"AgentData:S:AgentID=U,SessionID=U,Flags=U32,EstateID=U32,Godlike=BOOL;RequestData:S:ItemType=U32,RegionHandle=U64"},
	{"MapItemReply",FL,411,1,"AgentData:S:AgentID=U,Flags=U32;RequestData:S:ItemType=U32;Data:V:X=U32,Y=U32,ID=U,Extra=S32,Extra2=S32,Name=Var1"},
	{"SendPostcard",FL,412,0,"AgentData:S:AgentID=U,SessionID=U,AssetID=U,PosGlobal=V3d,To=Var1,From=Var1,Name=Var1,Subject=Var1,Msg=Var2,AllowPublish=BOOL,MaturePublish=BOOL"},
	{"RpcChannelRequest",FL,413,1,"DataBlock:S:GridX=U32,GridY=U32,TaskID=U,ItemID=U"},
	{"RpcChannelReply",FL,414,1,"DataBlock:S:TaskID=U,ItemID=U,ChannelID=U"},
	{"RpcScriptRequestInbound",FL,415,0,"TargetBlock:S:GridX=U32,GridY=U32;DataBlock:S:TaskID=U,ItemID=U,ChannelID=U,IntValue=U32,StringValue=Var2"},
	{"RpcScriptRequestInboundForward",FL,416,1,"DataBlock:S:RPCServerIP=IPADDR,RPCServerPort=IPPORT,TaskID=U,ItemID=U,ChannelID=U,IntValue=U32,StringValue=Var2"},
	{"RpcScriptReplyInbound",FL,417,0,"DataBlock:S:TaskID=U,ItemID=U,ChannelID=U,IntValue=U32,StringValue=Var2"},
	{"ScriptMailRegistration",FL,418,1,"DataBlock:S:TargetIP=Var1,TargetPort=IPPORT,TaskID=U,Flags=U32"},
	{"ParcelMediaCommandMessage",FL,419,1,"CommandBlock:S:Flags=U32,Command=U32,Time=F32"},
	{"ParcelMediaUpdate",FL,420,1,"DataBlock:S:MediaURL=Var1,MediaID=U,MediaAutoScale=U8;DataBlockExtended:S:MediaType=Var1,MediaDesc=Var1,MediaWidth=S32,MediaHeight=S32,MediaLoop=U8"},
	{"LandStatRequest",FL,421,0,"AgentData:S:AgentID=U,SessionID=U;RequestData:S:ReportType=U32,RequestFlags=U32,Filter=Var1,ParcelLocalID=S32"},
	{"LandStatReply",FL,422,1,"RequestData:S:ReportType=U32,RequestFlags=U32,TotalObjectCount=U32;ReportData:V:TaskLocalID=U32,TaskID=U,LocationX=F32,LocationY=F32,LocationZ=F32,Score=F32,TaskName=Var1,OwnerName=Var1"},
	{"Error",FL,423,2,"AgentData:S:AgentID=U;Data:S:Code=S32,Token=Var1,ID=U,System=Var1,Message=Var2,Data=Var2"},
	{"ObjectIncludeInSearch",FL,424,0,"AgentData:S:AgentID=U,SessionID=U;ObjectData:V:ObjectLocalID=U32,IncludeInSearch=BOOL"},
	{"RezRestoreToWorld",FL,425,0,"AgentData:S:AgentID=U,SessionID=U;InventoryData:S:ItemID=U,FolderID=U,CreatorID=U,OwnerID=U,GroupID=U,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=U,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32"},
	{"LinkInventoryItem",FL,426,2,"AgentData:S:AgentID=U,SessionID=U;InventoryBlock:S:CallbackID=U32,FolderID=U,TransactionID=U,OldItemID=U,Type=S8,InvType=S8,Name=Var1,Description=Var1"},
	{"RetrieveIMsExtended",FL,427,1,"AgentData:S:AgentID=U,SessionID=U,IsPremium=BOOL"},
	{"JoinGroupRequestExtended",FL,428,1,"AgentData:S:AgentID=U,SessionID=U,GroupLimit=S32;GroupData:S:GroupID=U"},
	{"CreateGroupRequestExtended",FL,429,1,"AgentData:S:AgentID=U,SessionID=U,GroupLimit=S32;GroupData:S:Name=Var1,Charter=Var2,ShowInList=BOOL,InsigniaID=U,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL"},
	{"GameControlInput",FH,32,2,"AgentData:S:AgentID=U,SessionID=U;AxisData:V:Index=U8,Value=S16;ButtonData:V:Data=Var1"},
}

// LookupMessage finds a registry entry by dispatch key.
func LookupMessage(freq Frequency, number uint32) (MessageInfo, bool) {
	for _, m := range Messages {
		if m.Frequency == freq && m.Number == number {
			return m, true
		}
	}
	return MessageInfo{}, false
}
```

## Part 9 — Caps client, login, and the EventQueueGet goroutine

```go
import (
	"bytes"
	"context"
	"fmt"
	"io"
	"net/http"
	"time"
)

// CapsWanted is the thin-client capability request list, following the
// viewer's buildCapabilityNames plus the AIS names in llaisapi.cpp.
var CapsWanted = []string{
	"EventQueueGet",
	"FetchInventory2", "FetchInventoryDescendents2", "FetchLib2", "FetchLibDescendents2",
	"InventoryAPIv3", "LibraryAPIv3", "IncrementCOFVersion",
	"GetTexture", "GetMesh", "GetMesh2", "GetMetadata", "GetObjectCost", "GetObjectPhysicsData",
	"SimulatorFeatures", "ServerReleaseNotes", "GetDisplayNames", "AgentPreferences",
	"CharacterProperties", "AvatarRenderInfo",
	"ChatSessionRequest", "GroupAPIv1", "GroupMemberData", "StartGroupProposal",
	"NewFileAgentInventory", "UpdateAgentAppearance", "RenderMaterials",
	"EnvironmentSettings", "ExtEnvironment",
	"ProvisionVoiceAccountRequest", "VoiceSignalingRequest",
}

// ErrCapNotOffered means this simulator version does not provide the cap.
// It is a normal condition (especially on OpenSim), not a failure.
var ErrCapNotOffered = fmt.Errorf("capability not offered by this simulator")

// Caps holds the resolved capability URLs for one region session. URLs are
// per-session and unguessable: never persist them, never reuse them after a
// teleport or relogin — build a fresh Caps from the new seed each time.
type Caps struct {
	http *http.Client
	urls map[string]string
}

// NewCaps exchanges the seed capability for the real cap map.
func NewCaps(ctx context.Context, httpClient *http.Client, seedURL string) (*Caps, error) {
	names := make([]Value, len(CapsWanted))
	for i, n := range CapsWanted {
		names[i] = Str(n)
	}
	body, err := ArrayVal(names...).MarshalXML()
	if err != nil {
		return nil, err
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, seedURL, bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/llsd+xml")
	resp, err := httpClient.Do(req)
	if err != nil {
		return nil, fmt.Errorf("seed cap exchange: %w", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("seed cap exchange: HTTP %d", resp.StatusCode)
	}
	raw, err := io.ReadAll(io.LimitReader(resp.Body, 16<<20))
	if err != nil {
		return nil, err
	}
	parsed, err := UnmarshalXML(raw)
	if err != nil {
		return nil, fmt.Errorf("seed cap response: %w", err)
	}
	urls := map[string]string{}
	if parsed.Kind == KindMap {
		for name, v := range parsed.Map {
			if s, ok := v.AsString(); ok {
				urls[name] = s
			}
		}
	}
	return &Caps{http: httpClient, urls: urls}, nil
}

// URL returns the cap URL or ErrCapNotOffered (wrapped with the cap name).
func (c *Caps) URL(name string) (string, error) {
	u, ok := c.urls[name]
	if !ok {
		return "", fmt.Errorf("%w: %s", ErrCapNotOffered, name)
	}
	return u, nil
}

// Has reports whether the simulator offered the named cap.
func (c *Caps) Has(name string) bool {
	_, ok := c.urls[name]
	return ok
}

// PostLLSD posts one LLSD value to a named cap and parses the LLSD reply.
// Most caps (AIS3, FetchInventory2, ChatSessionRequest) follow this shape.
func (c *Caps) PostLLSD(ctx context.Context, name string, body Value) (Value, error) {
	url, err := c.URL(name)
	if err != nil {
		return Undefined(), err
	}
	raw, err := body.MarshalXML()
	if err != nil {
		return Undefined(), err
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, url, bytes.NewReader(raw))
	if err != nil {
		return Undefined(), err
	}
	req.Header.Set("Content-Type", "application/llsd+xml")
	resp, err := c.http.Do(req)
	if err != nil {
		return Undefined(), fmt.Errorf("cap %s: %w", name, err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return Undefined(), fmt.Errorf("cap %s: HTTP %d", name, resp.StatusCode)
	}
	data, err := io.ReadAll(io.LimitReader(resp.Body, 64<<20))
	if err != nil {
		return Undefined(), err
	}
	if len(bytes.TrimSpace(data)) == 0 {
		return Undefined(), nil
	}
	return UnmarshalXML(data)
}

// LoginRequest is the LLSD login payload. Password handling: the legacy
// scheme sends "$1$" + hex MD5 of the password; current viewer code adds
// MFA/token variants (see llstartup). Credentials come from a secret store,
// never from source, config files in a repo, or logs.
type LoginRequest struct {
	FirstName string
	LastName  string // resident-style "Resident" last name for username logins
	// PasswordHash is the already-hashed credential, never the plaintext.
	PasswordHash string
	Start        string // "last", "home", or "specify" + SimName/x/y/z via options
	Channel      string // your viewer's unique channel name (TPV policy)
	Version      string
	// MFAHash and MFAToken are set on the resubmission after an MFA challenge.
	MFAHash  string
	MFAToken string
}

// ToLLSD renders the login request as the login service expects it.
func (r LoginRequest) ToLLSD() Value {
	m := map[string]Value{
		"first":   Str(r.FirstName),
		"last":    Str(r.LastName),
		"passwd":  Str(r.PasswordHash),
		"start":   Str(r.Start),
		"channel": Str(r.Channel),
		"version": Str(r.Version),
		// The login service expects these legacy fields to be present even
		// when empty; omitting them changes failure modes on some grids.
		"platform": Str("Lin"),
		"mac": Str("00:00:00:00:00:00"),
		"id0": Str(""),
		"agree_to_tos": Boolean(true),
		"read_critical": Boolean(true),
		"viewer_digest": Str(""),
		"address_size": Int(64),
		"extended_errors": Boolean(true),
		"last_exec_event": Int(0),
		"requested_options": ArrayVal(Str("inventory-root"), Str("inventory-skeleton"), Str("buddy-list"), Str("login-flags")),
	}
	if r.MFAHash != "" {
		m["mfa_hash"] = Str(r.MFAHash)
		m["token"] = Str(r.MFAToken)
	}
	return MapVal(m)
}

// LoginSession is what a client keeps from a successful login response.
type LoginSession struct {
	AgentID         UUID
	SessionID       UUID
	SecureSessionID UUID
	CircuitCode     uint32
	SimIP           string
	SimPort         uint16
	SeedCapability  string
	StartLocation   string
	RegionX         int32 // region handle halves, when present
	RegionY         int32
}

// LoginError is a refused login. Reason "mfa" (or the presence of an
// mfa_hash in the response) is a challenge, not a refusal: collect a TOTP
// code and resubmit with MFAHash/MFAToken set.
type LoginError struct {
	Reason  string
	Message string
	MFAHash string
}

func (e *LoginError) Error() string {
	return fmt.Sprintf("login refused: reason=%q message=%q", e.Reason, e.Message)
}

// ParseLoginResponse validates a login reply and extracts the session.
func ParseLoginResponse(resp Value) (LoginSession, error) {
	loginFlag, _ := resp.Get("login")
	if s, ok := loginFlag.AsString(); !ok || s != "true" {
		le := &LoginError{}
		if v, ok := resp.Get("reason"); ok {
			le.Reason, _ = v.AsString()
		}
		if v, ok := resp.Get("message"); ok {
			le.Message, _ = v.AsString()
		}
		if v, ok := resp.Get("mfa_hash"); ok {
			le.MFAHash, _ = v.AsString()
		}
		return LoginSession{}, le
	}
	needUUID := func(key string) (UUID, error) {
		v, ok := resp.Get(key)
		if !ok {
			return ZeroUUID, fmt.Errorf("login response missing %s", key)
		}
		u, ok := v.AsUUID()
		if !ok {
			return ZeroUUID, fmt.Errorf("login response %s is not a UUID", key)
		}
		return u, nil
	}
	var s LoginSession
	var err error
	if s.AgentID, err = needUUID("agent_id"); err != nil {
		return s, err
	}
	if s.SessionID, err = needUUID("session_id"); err != nil {
		return s, err
	}
	if s.SecureSessionID, err = needUUID("secure_session_id"); err != nil {
		return s, err
	}
	if v, ok := resp.Get("circuit_code"); ok {
		if n, ok2 := v.AsInt(); ok2 {
			s.CircuitCode = uint32(n)
		}
	}
	if v, ok := resp.Get("sim_ip"); ok {
		s.SimIP, _ = v.AsString()
	}
	if v, ok := resp.Get("sim_port"); ok {
		if n, ok2 := v.AsInt(); ok2 {
			s.SimPort = uint16(n)
		}
	}
	if v, ok := resp.Get("seed_capability"); ok {
		s.SeedCapability, _ = v.AsString()
	}
	if v, ok := resp.Get("start_location"); ok {
		s.StartLocation, _ = v.AsString()
	}
	return s, nil
}

// Login performs one login attempt against a grid login URI
// (Agni: https://login.agni.lindenlab.com/cgi-bin/login.cgi).
func Login(ctx context.Context, httpClient *http.Client, loginURI string, req LoginRequest) (LoginSession, error) {
	body, err := req.ToLLSD().MarshalXML()
	if err != nil {
		return LoginSession{}, err
	}
	httpReq, err := http.NewRequestWithContext(ctx, http.MethodPost, loginURI, bytes.NewReader(body))
	if err != nil {
		return LoginSession{}, err
	}
	httpReq.Header.Set("Content-Type", "application/llsd+xml")
	resp, err := httpClient.Do(httpReq)
	if err != nil {
		return LoginSession{}, fmt.Errorf("login transport: %w", err)
	}
	defer resp.Body.Close()
	raw, err := io.ReadAll(io.LimitReader(resp.Body, 16<<20))
	if err != nil {
		return LoginSession{}, err
	}
	parsed, err := UnmarshalXML(raw)
	if err != nil {
		return LoginSession{}, fmt.Errorf("login response parse: %w", err)
	}
	return ParseLoginResponse(parsed)
}

// EQEvent is one Event Queue event: a message name plus its LLSD body.
type EQEvent struct {
	Message string
	Body    Value
}

// EventQueue runs the EventQueueGet long-poll loop on a goroutine (started
// by RunEventQueue). Ack handling is the heartbeat of a thin client: feed
// each response's id back as the next request's ack, or events repeat and
// the queue stalls — which looks exactly like a dead session.
type EventQueue struct {
	caps *Caps
	ack  int32
	done bool
}

// Poll performs one long-poll round and returns the events that arrived.
// The simulator holds the request open; pass a context with a generous
// timeout (the server-side poll is typically ~30 s or longer).
func (q *EventQueue) Poll(ctx context.Context) ([]EQEvent, error) {
	body := MapVal(map[string]Value{
		"ack":  Int(q.ack),
		"done": Boolean(q.done),
	})
	resp, err := q.caps.PostLLSD(ctx, "EventQueueGet", body)
	if err != nil {
		return nil, err
	}
	if v, ok := resp.Get("id"); ok {
		if n, ok2 := v.AsInt(); ok2 {
			q.ack = n
		}
	}
	var events []EQEvent
	if v, ok := resp.Get("events"); ok && v.Kind == KindArray {
		for _, ev := range v.Arr {
			name, _ := ev.Get("message")
			ns, _ := name.AsString()
			b, _ := ev.Get("body")
			events = append(events, EQEvent{Message: ns, Body: b})
		}
	}
	return events, nil
}

// RunEventQueue is the goroutine loop: poll, deliver events on out, back off
// briefly on transport errors (a stalled or failing EQG must not spin), and
// stop cleanly on context cancellation, sending a final done=true poll so
// the simulator can release the queue.
func RunEventQueue(ctx context.Context, caps *Caps, out chan<- EQEvent, errs chan<- error) {
	q := &EventQueue{caps: caps}
	backoff := time.Second
	for {
		if ctx.Err() != nil {
			q.done = true
			finalCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
			_, _ = q.Poll(finalCtx) // best effort: release the server queue
			cancel()
			return
		}
		events, err := q.Poll(ctx)
		if err != nil {
			if errs != nil {
				select {
				case errs <- fmt.Errorf("event queue: %w", err):
				default:
				}
			}
			select {
			case <-ctx.Done():
				return
			case <-time.After(backoff):
			}
			if backoff < 30*time.Second {
				backoff *= 2
			}
			continue
		}
		backoff = time.Second
		for _, ev := range events {
			select {
			case out <- ev:
			case <-ctx.Done():
				return
			}
		}
	}
}
```

---

## Part 10 — Tests and main skeleton

```go
package slproto

import (
	"bytes"
	"testing"
)

func TestUUIDRoundTrip(t *testing.T) {
	u, err := ParseUUID("00112233-4455-6677-8899-aabbccddeeff")
	if err != nil {
		t.Fatal(err)
	}
	if u.String() != "00112233-4455-6677-8899-aabbccddeeff" {
		t.Fatalf("round trip: %s", u)
	}
	if _, err := ParseUUID("nope"); err == nil {
		t.Fatal("expected error for malformed UUID")
	}
}

func TestZeroRoundTrip(t *testing.T) {
	cases := [][]byte{
		{}, {1, 2, 3}, {0}, {0, 0, 0, 5, 0, 1},
		bytes.Repeat([]byte{0}, 300), // run longer than the 255 count byte
	}
	for _, c := range cases {
		if got := ZeroDecode(ZeroEncode(c)); !bytes.Equal(got, c) {
			t.Fatalf("zerocode round trip failed for %v", c)
		}
	}
}

func TestMessageIDRoundTrip(t *testing.T) {
	for _, tc := range []struct {
		f Frequency
		n uint32
	}{
		{FreqHigh, 7}, {FreqMedium, 18}, {FreqLow, 431}, {FreqFixed, 0xFB},
	} {
		enc := AppendMessageID(nil, tc.f, tc.n)
		id, err := DecodeMessageID(enc)
		if err != nil {
			t.Fatal(err)
		}
		if id.Frequency != tc.f || id.Number != tc.n || id.Size != len(enc) {
			t.Fatalf("id round trip: got %+v want %v/%d", id, tc.f, tc.n)
		}
	}
}

func TestLLSDXMLRoundTrip(t *testing.T) {
	uid, _ := ParseUUID("00112233-4455-6677-8899-aabbccddeeff")
	v := MapVal(map[string]Value{
		"agent_id":     UUIDVal(uid),
		"circuit_code": Int(12345678),
		"flags":        ArrayVal(Boolean(true), Real(2.5), Str(`a<b>&"q"`)),
		"blob":         BinaryVal([]byte{0, 1, 2, 250, 251}),
		"when":         DateVal(1700000000.25),
	})
	raw, err := v.MarshalXML()
	if err != nil {
		t.Fatal(err)
	}
	back, err := UnmarshalXML(raw)
	if err != nil {
		t.Fatal(err)
	}
	if got, _ := back.Get("circuit_code"); got.Int != 12345678 {
		t.Fatalf("circuit_code = %v", got)
	}
	if got, _ := back.Get("agent_id"); got.UUID != uid {
		t.Fatalf("agent_id = %v", got)
	}
}

func TestLLSDBinaryRoundTrip(t *testing.T) {
	v := MapVal(map[string]Value{
		"items": ArrayVal(Int(-7), Undefined(), Str("x")),
		"where": URIVal("https://example.invalid/cap/abc"),
	})
	raw, err := v.MarshalBinary()
	if err != nil {
		t.Fatal(err)
	}
	back, err := UnmarshalBinary(raw)
	if err != nil {
		t.Fatal(err)
	}
	items, _ := back.Get("items")
	if len(items.Arr) != 3 || items.Arr[0].Int != -7 {
		t.Fatalf("items = %+v", items)
	}
}

func TestQuaternionWire(t *testing.T) {
	q := Quaternion{0, 0, 0.70710678, 0.70710678}.Normalized()
	x, y, z := q.Wire()
	back := QuaternionFromWire(x, y, z)
	if back.Z-q.Z > 1e-5 || q.W-back.W > 1e-5 {
		t.Fatalf("quat round trip: %+v vs %+v", back, q)
	}
}

func TestRegistryLookup(t *testing.T) {
	m, ok := LookupMessage(FreqLow, 3)
	if !ok || m.Name != "UseCircuitCode" {
		t.Fatalf("UseCircuitCode lookup: %+v ok=%v", m, ok)
	}
	if m.Blocks == "" {
		t.Fatal("UseCircuitCode must have blocks")
	}
	m, ok = LookupMessage(FreqFixed, 0xFB)
	if !ok || m.Name != "PacketAck" {
		t.Fatalf("PacketAck lookup: %+v ok=%v", m, ok)
	}
	if len(Messages) < 480 {
		t.Fatalf("registry has %d messages, want the full template set", len(Messages))
	}
}
```

Main skeleton (`cmd/slbot/main.go`): log in with `Login` (credentials from
your secret store — never from source), build `Caps` from
`session.SeedCapability`, dial `net.DialUDP` to `SimIP:SimPort`, construct a
`Circuit`, send UseCircuitCode then CompleteAgentMovement (block layouts are
in the Part 8 registry), reply to RegionHandshake, then run three goroutines:
the socket read loop (`Circuit.Receive` → dispatch, answering
StartPingCheck with CompletePingCheck and calling `NotePingReply`), a
100 ms maintenance ticker (`Circuit.Tick` writes + `StartPing`), and
`RunEventQueue` — rebuilding `Caps` and `Circuit` from the new seed on every
TeleportFinish.

*End of the Go implementation. Companion: `code-rust.md` in this folder, and
the generated references under `skills/secondlife_protocol/references/` and
`skills/secondlife_client_libraries/references/` in this repo.*
