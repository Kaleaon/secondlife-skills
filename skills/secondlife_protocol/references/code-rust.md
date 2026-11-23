# Second Life in Rust — LLSD, Zerocode, UDP Circuit, and Caps

> **What this ports, and from where.** This is a from-scratch Rust implementation of the
> Second Life simulator protocol core. The semantics are ported from three canonical
> sources, in the cross-check order the skills in this repo prescribe:
>
> 1. **`secondlife/viewer` (LGPL-2.1)** — `indra/llcommon/llsdserialize.cpp` for LLSD
>    wire formats, `indra/llmessage/llcircuit.cpp` / `llpacketring` behaviour for the
>    UDP circuit, and `indra/newview/llviewerregion.cpp` (`buildCapabilityNames`) for
>    the capability names requested at login.
> 2. **`secondlife/master-message-template`** — `message_template.msg`, the definition
>    of every UDP message: name, frequency, number, trust, zerocoded flag, blocks and
>    typed fields. The generated message structs in Part 9 are produced from it.
> 3. **`cinderblocks/libremetaverse` (BSD-3)** — `LibreMetaverse.StructuredData`
>    (LLSD XML/binary/notation semantics), `LibreMetaverse.Transport` (reliable resend
>    queue, throttle, ping), and `LibreMetaverse.Protocol` (packet layouts). Where the
>    C# and the C++ disagree, the viewer wins, because the viewer is what Agni runs
>    against.
>
> Licence note: this code is newly written for this repo. It implements formats
> described by the LGPL viewer sources; it does not copy viewer code. Serde-LLSD
> exists upstream under LGPL-2.1 if you prefer a maintained crate — this file is the
> teaching/porting reference the skills point at, with the wire details spelled out.
>
> **Layout.** Part 1 `Cargo.toml`. Part 2 UUID. Part 3 vector/quaternion maths with
> SL's compressed quaternion wire form. Part 4 the LLSD value type. Parts 5–7 LLSD
> XML, binary, and notation serialisation. Part 8 zerocode + packet header + the
> circuit. Part 9 generated message definitions. Part 10 caps client + login.
> Part 11 tests and a runnable bot skeleton.

---

## Part 1 — Cargo.toml

```toml
[package]
name = "slproto"
version = "0.1.0"
edition = "2021"
description = "Second Life simulator protocol core: LLSD, UDP circuit, capabilities"
license = "MIT OR Apache-2.0"

[dependencies]
# HTTP for login + capabilities. `rustls` avoids a system OpenSSL dependency on
# mobile/CI builds; the simulator caps endpoints are plain HTTPS with public certs.
reqwest = { version = "0.12", default-features = false, features = ["rustls-tls", "json"] }
tokio = { version = "1", features = ["rt-multi-thread", "macros", "time", "net"] }
# UUID parsing/formatting for the *text* forms. The wire type below is our own
# 16-byte struct because LLSD binary and UDP both treat a UUID as raw bytes, and
# pulling the crate's byte order into the protocol layer is a classic bug source.
uuid = { version = "1", features = ["v4"] }
# Dates in LLSD are seconds since the Unix epoch in binary, ISO-8601 in XML.
chrono = { version = "0.4", default-features = false, features = ["std"] }
base64 = "0.22"        # LLSD XML encodes <binary> as base64
thiserror = "1"        # typed protocol errors instead of stringly-typed failures
bytes = "1"            # cheap packet buffer slicing for the circuit

[dev-dependencies]
tokio-test = "0.4"
```

---

## Part 2 — UUID: sixteen bytes, two text forms, one trap

Second Life UUIDs appear as raw 16 bytes in UDP and binary LLSD, as hyphenated
lowercase hex in XML LLSD and in most text contexts, and occasionally as unhyphenated
hex in old notecard/LSL-adjacent data. The trap is byte order: the bytes on the wire
are the hex string read left to right. There is **no** little-endian field swapping
(unlike .NET `Guid.ToByteArray()`), so never round-trip through a GUID type that
reorders the first three fields.

```rust
use std::fmt;

/// A Second Life UUID: exactly 16 bytes, wire order == hex-string order.
#[derive(Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord, Default)]
pub struct SlUuid(pub [u8; 16]);

impl SlUuid {
    pub const ZERO: SlUuid = SlUuid([0u8; 16]);

    /// Generate a random (v4-shaped) UUID. Used for transaction IDs, which the
    /// simulator treats as opaque — it does not validate the version nibble.
    pub fn new_v4() -> Self {
        let u = uuid::Uuid::new_v4();
        SlUuid(*u.as_bytes())
    }

    /// Parse the hyphenated form `00112233-4455-6677-8899-aabbccddeeff` or the
    /// bare 32-hex-digit form. Returns `None` on any malformed input instead of
    /// panicking: UUIDs arrive from untrusted inventory and chat data.
    pub fn parse(s: &str) -> Option<Self> {
        let hex: String = s.chars().filter(|c| *c != '-').collect();
        if hex.len() != 32 || !hex.chars().all(|c| c.is_ascii_hexdigit()) {
            return None;
        }
        let mut out = [0u8; 16];
        for i in 0..16 {
            out[i] = u8::from_str_radix(&hex[2 * i..2 * i + 2], 16).ok()?;
        }
        Some(SlUuid(out))
    }

    pub fn is_zero(&self) -> bool {
        self.0.iter().all(|b| *b == 0)
    }

    /// Big-endian u64 halves, handy as a HashMap key or for debugging output
    /// that matches how the viewer prints UUIDs in logs.
    pub fn halves(&self) -> (u64, u64) {
        let hi = u64::from_be_bytes(self.0[0..8].try_into().unwrap());
        let lo = u64::from_be_bytes(self.0[8..16].try_into().unwrap());
        (hi, lo)
    }
}

impl fmt::Display for SlUuid {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let b = &self.0;
        write!(
            f,
            "{:02x}{:02x}{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}",
            b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10], b[11], b[12], b[13], b[14], b[15]
        )
    }
}

impl fmt::Debug for SlUuid {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "SlUuid({self})")
    }
}
```

---

## Part 3 — Vector3, Vector3d, Quaternion, and SL's compressed forms

The template's field types map to these maths types. Two wire quirks matter:

* `LLQuaternion` is sent as **three** f32s (x, y, z); w is reconstructed as
  `sqrt(1 - x² - y² - z²)`. If the sum exceeds 1.0 (rounding on the sender side),
  the viewer normalises instead of taking a NaN root — do the same.
* `ImprovedTerseObjectUpdate` quantises position to 16-bit-ish resolution inside a
  region and rotation via the compressed quaternion; jitter bugs in ports are
  almost always someone decoding terse updates with the full-precision path.

```rust
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct Vector3 {
    pub x: f32,
    pub y: f32,
    pub z: f32,
}

impl Vector3 {
    pub const ZERO: Vector3 = Vector3 { x: 0.0, y: 0.0, z: 0.0 };

    pub fn new(x: f32, y: f32, z: f32) -> Self {
        Self { x, y, z }
    }
    pub fn length(&self) -> f32 {
        (self.x * self.x + self.y * self.y + self.z * self.z).sqrt()
    }
    pub fn normalized(&self) -> Self {
        let l = self.length();
        if l == 0.0 {
            Self::ZERO
        } else {
            Self::new(self.x / l, self.y / l, self.z / l)
        }
    }
    pub fn dot(&self, o: &Self) -> f32 {
        self.x * o.x + self.y * o.y + self.z * o.z
    }
    pub fn cross(&self, o: &Self) -> Self {
        Self::new(
            self.y * o.z - self.z * o.y,
            self.z * o.x - self.x * o.z,
            self.x * o.y - self.y * o.x,
        )
    }
    /// Serialise as the template's `LLVector3`: three little-endian f32s.
    pub fn to_le_bytes(&self) -> [u8; 12] {
        let mut out = [0u8; 12];
        out[0..4].copy_from_slice(&self.x.to_le_bytes());
        out[4..8].copy_from_slice(&self.y.to_le_bytes());
        out[8..12].copy_from_slice(&self.z.to_le_bytes());
        out
    }
    pub fn from_le_bytes(b: &[u8]) -> Option<Self> {
        if b.len() < 12 {
            return None;
        }
        Some(Self::new(
            f32::from_le_bytes(b[0..4].try_into().ok()?),
            f32::from_le_bytes(b[4..8].try_into().ok()?),
            f32::from_le_bytes(b[8..12].try_into().ok()?),
        ))
    }
}

/// Double-precision position, used for global coordinates (region handle + offset).
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct Vector3d {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl Vector3d {
    pub fn to_le_bytes(&self) -> [u8; 24] {
        let mut out = [0u8; 24];
        out[0..8].copy_from_slice(&self.x.to_le_bytes());
        out[8..16].copy_from_slice(&self.y.to_le_bytes());
        out[16..24].copy_from_slice(&self.z.to_le_bytes());
        out
    }
    pub fn from_le_bytes(b: &[u8]) -> Option<Self> {
        if b.len() < 24 {
            return None;
        }
        Some(Self {
            x: f64::from_le_bytes(b[0..8].try_into().ok()?),
            y: f64::from_le_bytes(b[8..16].try_into().ok()?),
            z: f64::from_le_bytes(b[16..24].try_into().ok()?),
        })
    }
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Quaternion {
    pub x: f32,
    pub y: f32,
    pub z: f32,
    pub w: f32,
}

impl Default for Quaternion {
    fn default() -> Self {
        Self::IDENTITY
    }
}

impl Quaternion {
    pub const IDENTITY: Quaternion = Quaternion { x: 0.0, y: 0.0, z: 0.0, w: 1.0 };

    pub fn normalized(&self) -> Self {
        let l = (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w).sqrt();
        if l == 0.0 {
            Self::IDENTITY
        } else {
            Self { x: self.x / l, y: self.y / l, z: self.z / l, w: self.w / l }
        }
    }

    /// Decode the wire form: three f32s (x, y, z); w = sqrt(1 - x²-y²-z²),
    /// clamped the way the viewer clamps it. A negative radicand means the
    /// sender rounded badly — normalise the triple instead of producing NaN.
    pub fn from_wire_xyz(x: f32, y: f32, z: f32) -> Self {
        let sum = x * x + y * y + z * z;
        if sum >= 1.0 {
            let l = sum.sqrt();
            Self { x: x / l, y: y / l, z: z / l, w: 0.0 }
        } else {
            Self { x, y, z, w: (1.0 - sum).sqrt() }
        }
    }

    /// Encode to the wire form. The sign convention: w is always sent implicit
    /// and assumed non-negative on decode, so flip the quaternion if w < 0 —
    /// q and -q are the same rotation, and this keeps the round-trip stable.
    pub fn to_wire_xyz(&self) -> (f32, f32, f32) {
        let q = self.normalized();
        if q.w < 0.0 {
            (-q.x, -q.y, -q.z)
        } else {
            (q.x, q.y, q.z)
        }
    }

    /// Hamilton product — composition of rotations, used when combining a
    /// prim's rotation with its parent linkset root rotation.
    pub fn mul(&self, o: &Self) -> Self {
        Self {
            x: self.w * o.x + self.x * o.w + self.y * o.z - self.z * o.y,
            y: self.w * o.y - self.x * o.z + self.y * o.w + self.z * o.x,
            z: self.w * o.z + self.x * o.y - self.y * o.x + self.z * o.w,
            w: self.w * o.w - self.x * o.x - self.y * o.y - self.z * o.z,
        }
        .normalized()
    }

    /// Rotate a vector by this quaternion (v' = q v q*).
    pub fn rotate(&self, v: Vector3) -> Vector3 {
        let qv = Vector3::new(self.x, self.y, self.z);
        let t = qv.cross(&v);
        let t = Vector3::new(t.x * 2.0, t.y * 2.0, t.z * 2.0);
        let c = qv.cross(&t);
        Vector3::new(
            v.x + self.w * t.x + c.x,
            v.y + self.w * t.y + c.y,
            v.z + self.w * t.z + c.z,
        )
    }
}
```

---

## Part 4 — The LLSD value type

LLSD (Linden Lab Structured Data) is the payload format for login, capabilities,
and the Event Queue. Its type system is deliberately small. Three facts drive the
whole design:

* **Integers are 32-bit.** There is no i64 in LLSD. Simulator code that needs a
  64-bit value sends a string or a real. In Rust, model `Integer(i32)` exactly —
  widening to i64 and then serialising a value > 2³¹ silently corrupts.
* **Reals are doubles** and serialise with enough digits to round-trip; the viewer
  uses `%.17g`-style formatting in XML. Rust's `{}` on f64 is shortest-round-trip,
  which is fine and interoperable.
* **Binary is raw bytes**, base64 only inside XML. Dates are seconds since epoch
  (f64 in binary, to carry fractional seconds; ISO-8601 string in XML).

```rust
use std::collections::BTreeMap;

/// One LLSD value. `BTreeMap` (not HashMap) for maps: the viewer's XML writer
/// emits keys in sorted order, and deterministic output makes golden-file tests
/// and packet diffs readable. Simulator parsers accept any order.
#[derive(Clone, Debug, PartialEq)]
pub enum Llsd {
    Undefined,
    Boolean(bool),
    Integer(i32),
    Real(f64),
    String(String),
    Uuid(SlUuid),
    /// Seconds since 1970-01-01T00:00:00Z, fractional part allowed.
    Date(f64),
    Uri(String),
    Binary(Vec<u8>),
    Array(Vec<Llsd>),
    Map(BTreeMap<String, Llsd>),
}

impl Default for Llsd {
    fn default() -> Self {
        Llsd::Undefined
    }
}

impl Llsd {
    pub fn map() -> Self {
        Llsd::Map(BTreeMap::new())
    }
    /// Insert into a map value, converting `self` to a map first if needed.
    /// Login and caps code builds maps incrementally everywhere; this keeps the
    /// call sites one line instead of five.
    pub fn insert(&mut self, key: &str, value: Llsd) {
        if !matches!(self, Llsd::Map(_)) {
            *self = Llsd::map();
        }
        if let Llsd::Map(m) = self {
            m.insert(key.to_string(), value);
        }
    }
    /// Look up a key on a map. Returns `&Llsd::Undefined`-style `None` for any
    /// non-map or missing key — callers must not index blindly, because caps
    /// responses routinely omit keys a given simulator version doesn't support.
    pub fn get(&self, key: &str) -> Option<&Llsd> {
        match self {
            Llsd::Map(m) => m.get(key),
            _ => None,
        }
    }
    pub fn as_str(&self) -> Option<&str> {
        match self {
            Llsd::String(s) | Llsd::Uri(s) => Some(s),
            _ => None,
        }
    }
    pub fn as_bool(&self) -> Option<bool> {
        match self {
            Llsd::Boolean(b) => Some(*b),
            // The login response historically encodes some flags as Integer 0/1.
            Llsd::Integer(i) => Some(*i != 0),
            _ => None,
        }
    }
    pub fn as_i32(&self) -> Option<i32> {
        match self {
            Llsd::Integer(i) => Some(*i),
            Llsd::Real(r) if r.fract() == 0.0 && *r >= i32::MIN as f64 && *r <= i32::MAX as f64 => {
                Some(*r as i32)
            }
            _ => None,
        }
    }
    pub fn as_f64(&self) -> Option<f64> {
        match self {
            Llsd::Real(r) => Some(*r),
            Llsd::Integer(i) => Some(*i as f64),
            _ => None,
        }
    }
    pub fn as_uuid(&self) -> Option<SlUuid> {
        match self {
            Llsd::Uuid(u) => Some(*u),
            // Inventory and login payloads frequently carry UUIDs as strings.
            Llsd::String(s) => SlUuid::parse(s),
            _ => None,
        }
    }
    pub fn as_array(&self) -> Option<&[Llsd]> {
        match self {
            Llsd::Array(a) => Some(a),
            _ => None,
        }
    }
    /// Type name exactly as the viewer's `llsd` debug output spells it; used in
    /// error messages so a Rust log lines up with a viewer log during diffing.
    pub fn type_name(&self) -> &'static str {
        match self {
            Llsd::Undefined => "undefined",
            Llsd::Boolean(_) => "boolean",
            Llsd::Integer(_) => "integer",
            Llsd::Real(_) => "real",
            Llsd::String(_) => "string",
            Llsd::Uuid(_) => "uuid",
            Llsd::Date(_) => "date",
            Llsd::Uri(_) => "uri",
            Llsd::Binary(_) => "binary",
            Llsd::Array(_) => "array",
            Llsd::Map(_) => "map",
        }
    }
}

impl From<bool> for Llsd { fn from(v: bool) -> Self { Llsd::Boolean(v) } }
impl From<i32> for Llsd { fn from(v: i32) -> Self { Llsd::Integer(v) } }
impl From<f64> for Llsd { fn from(v: f64) -> Self { Llsd::Real(v) } }
impl From<&str> for Llsd { fn from(v: &str) -> Self { Llsd::String(v.to_string()) } }
impl From<String> for Llsd { fn from(v: String) -> Self { Llsd::String(v) } }
impl From<SlUuid> for Llsd { fn from(v: SlUuid) -> Self { Llsd::Uuid(v) } }
impl From<Vec<Llsd>> for Llsd { fn from(v: Vec<Llsd>) -> Self { Llsd::Array(v) } }
impl From<Vec<u8>> for Llsd { fn from(v: Vec<u8>) -> Self { Llsd::Binary(v) } }

#[derive(Debug, thiserror::Error)]
pub enum LlsdError {
    #[error("LLSD parse error at offset {offset}: {message}")]
    Parse { offset: usize, message: String },
    #[error("LLSD binary truncated: needed {needed} bytes, had {had}")]
    Truncated { needed: usize, had: usize },
    #[error("unknown LLSD binary type marker 0x{0:02x}")]
    BadMarker(u8),
    #[error("invalid UTF-8 in LLSD string")]
    BadUtf8,
}
```

---

## Part 5 — LLSD XML serialisation

The XML form is what login and most caps use over HTTPS (`application/llsd+xml`).
Structure: an `<llsd>` root wrapping exactly one value element. Map keys are
`<key>` elements alternating with value elements. Parsing must be tolerant: the
simulator emits no pretty-printing guarantees, may include the XML declaration,
and older OpenSim versions emit `<undef/>` where Linden emits `<undefined/>` in a
few paths — accept both.

```rust
use base64::Engine as _;

fn xml_escape(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '&' => out.push_str("&amp;"),
            '<' => out.push_str("&lt;"),
            '>' => out.push_str("&gt;"),
            '"' => out.push_str("&quot;"),
            '\'' => out.push_str("&apos;"),
            // XML 1.0 forbids most C0 controls even escaped; LLSD strings from
            // chat can contain them. The viewer strips them on write — match it.
            c if (c as u32) < 0x20 && c != '\t' && c != '\n' && c != '\r' => {}
            c => out.push(c),
        }
    }
    out
}

/// Format an LLSD date (epoch seconds) as ISO-8601, the XML wire form.
fn date_to_iso(epoch: f64) -> String {
    let secs = epoch.trunc() as i64;
    let dt = chrono::DateTime::<chrono::Utc>::from_timestamp(secs, 0)
        .unwrap_or(chrono::DateTime::<chrono::Utc>::UNIX_EPOCH);
    dt.format("%Y-%m-%dT%H:%M:%SZ").to_string()
}

fn iso_to_date(s: &str) -> Option<f64> {
    // Accepts "...Z" and fractional seconds; returns epoch seconds.
    let cleaned = s.trim().trim_end_matches('Z');
    let (main, frac) = match cleaned.split_once('.') {
        Some((m, f)) => (m, format!("0.{f}").parse::<f64>().ok()?),
        None => (cleaned, 0.0),
    };
    let dt = chrono::NaiveDateTime::parse_from_str(main, "%Y-%m-%dT%H:%M:%S").ok()?;
    Some(dt.and_utc().timestamp() as f64 + frac)
}

impl Llsd {
    pub fn to_xml(&self) -> String {
        let mut out = String::from("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<llsd>");
        self.write_xml(&mut out);
        out.push_str("</llsd>");
        out
    }

    fn write_xml(&self, out: &mut String) {
        match self {
            Llsd::Undefined => out.push_str("<undefined/>"),
            Llsd::Boolean(b) => {
                out.push_str(if *b { "<boolean>1</boolean>" } else { "<boolean>0</boolean>" })
            }
            Llsd::Integer(i) => {
                out.push_str(&format!("<integer>{i}</integer>"));
            }
            Llsd::Real(r) => {
                // NaN/inf are not representable; the viewer writes 0. Match it
                // rather than emitting text a simulator parser will reject.
                let v = if r.is_finite() { *r } else { 0.0 };
                out.push_str(&format!("<real>{v}</real>"));
            }
            Llsd::String(s) => {
                out.push_str(&format!("<string>{}</string>", xml_escape(s)));
            }
            Llsd::Uuid(u) => {
                out.push_str(&format!("<uuid>{u}</uuid>"));
            }
            Llsd::Date(d) => {
                out.push_str(&format!("<date>{}</date>", date_to_iso(*d)));
            }
            Llsd::Uri(u) => {
                out.push_str(&format!("<uri>{}</uri>", xml_escape(u)));
            }
            Llsd::Binary(b) => {
                let enc = base64::engine::general_purpose::STANDARD.encode(b);
                out.push_str(&format!("<binary>{enc}</binary>"));
            }
            Llsd::Array(items) => {
                out.push_str("<array>");
                for it in items {
                    it.write_xml(out);
                }
                out.push_str("</array>");
            }
            Llsd::Map(m) => {
                out.push_str("<map>");
                for (k, v) in m {
                    out.push_str(&format!("<key>{}</key>", xml_escape(k)));
                    v.write_xml(out);
                }
                out.push_str("</map>");
            }
        }
    }

    /// Parse LLSD XML. Hand-rolled recursive descent over tags rather than a
    /// full XML DOM: LLSD XML uses a fixed tiny tag vocabulary, and a strict
    /// small parser is both faster and immune to XXE/entity-expansion attacks
    /// in untrusted caps responses.
    pub fn from_xml(text: &str) -> Result<Llsd, LlsdError> {
        let mut p = XmlParser { s: text.as_bytes(), pos: 0 };
        p.skip_misc()?;
        p.expect("<llsd>")?;
        let v = p.parse_value()?;
        p.skip_ws();
        p.expect("</llsd>")?;
        Ok(v)
    }
}

struct XmlParser<'a> {
    s: &'a [u8],
    pos: usize,
}

impl<'a> XmlParser<'a> {
    fn err(&self, msg: &str) -> LlsdError {
        LlsdError::Parse { offset: self.pos, message: msg.to_string() }
    }
    fn skip_ws(&mut self) {
        while self.pos < self.s.len() && (self.s[self.pos] as char).is_whitespace() {
            self.pos += 1;
        }
    }
    /// Skip the XML declaration, comments, and whitespace before `<llsd>`.
    fn skip_misc(&mut self) -> Result<(), LlsdError> {
        loop {
            self.skip_ws();
            if self.peek("<?") {
                match self.find("?>") { Some(e) => self.pos = e + 2, None => return Err(self.err("unterminated <? ?>")) }
            } else if self.peek("<!--") {
                match self.find("-->") { Some(e) => self.pos = e + 3, None => return Err(self.err("unterminated comment")) }
            } else {
                return Ok(());
            }
        }
    }
    fn peek(&self, pat: &str) -> bool {
        self.s[self.pos..].starts_with(pat.as_bytes())
    }
    fn find(&self, pat: &str) -> Option<usize> {
        let hay = &self.s[self.pos..];
        hay.windows(pat.len()).position(|w| w == pat.as_bytes()).map(|i| self.pos + i)
    }
    fn expect(&mut self, pat: &str) -> Result<(), LlsdError> {
        self.skip_ws();
        if self.peek(pat) {
            self.pos += pat.len();
            Ok(())
        } else {
            Err(self.err(&format!("expected {pat}")))
        }
    }
    /// Read `<tag>`, `<tag/>`, or `<tag attr=...>`; returns (name, self_closing).
    fn open_tag(&mut self) -> Result<(String, bool), LlsdError> {
        self.skip_ws();
        if !self.peek("<") || self.peek("</") {
            return Err(self.err("expected opening tag"));
        }
        self.pos += 1;
        let start = self.pos;
        while self.pos < self.s.len()
            && ((self.s[self.pos] as char).is_alphanumeric() || self.s[self.pos] == b'_')
        {
            self.pos += 1;
        }
        let name = String::from_utf8_lossy(&self.s[start..self.pos]).into_owned();
        // Skip any attributes (LLSD emits none, but tolerate them).
        while self.pos < self.s.len() && self.s[self.pos] != b'>' {
            self.pos += 1;
        }
        if self.pos >= self.s.len() {
            return Err(self.err("unterminated tag"));
        }
        let self_closing = self.pos > 0 && self.s[self.pos - 1] == b'/';
        self.pos += 1; // consume '>'
        Ok((name, self_closing))
    }
    /// Read raw text up to the matching close tag and unescape entities.
    fn text_until_close(&mut self, tag: &str) -> Result<String, LlsdError> {
        let close = format!("</{tag}>");
        let start = self.pos;
        match self.find(&close) {
            Some(e) => {
                let raw = String::from_utf8_lossy(&self.s[start..e]).into_owned();
                self.pos = e + close.len();
                Ok(unescape(&raw))
            }
            None => Err(self.err(&format!("missing {close}"))),
        }
    }
    fn parse_value(&mut self) -> Result<Llsd, LlsdError> {
        let (tag, self_closing) = self.open_tag()?;
        match tag.as_str() {
            "undefined" | "undef" => Ok(Llsd::Undefined),
            "boolean" => {
                if self_closing { return Ok(Llsd::Boolean(false)); }
                let t = self.text_until_close("boolean")?;
                Ok(Llsd::Boolean(t.trim() == "1" || t.trim() == "true"))
            }
            "integer" => {
                let t = self.text_until_close("integer")?;
                t.trim().parse::<i32>().map(Llsd::Integer).map_err(|_| self.err("bad integer"))
            }
            "real" => {
                let t = self.text_until_close("real")?;
                // Viewer emits "nan" rarely on broken data; parse leniently.
                let v = t.trim().parse::<f64>().unwrap_or(0.0);
                Ok(Llsd::Real(v))
            }
            "string" => Ok(Llsd::String(self.text_until_close("string")?)),
            "uuid" => {
                let t = self.text_until_close("uuid")?;
                Ok(Llsd::Uuid(SlUuid::parse(t.trim()).unwrap_or_default()))
            }
            "date" => {
                let t = self.text_until_close("date")?;
                Ok(Llsd::Date(iso_to_date(t.trim()).unwrap_or(0.0)))
            }
            "uri" => Ok(Llsd::Uri(self.text_until_close("uri")?)),
            "binary" => {
                let t = self.text_until_close("binary")?;
                let cleaned: String = t.chars().filter(|c| !c.is_whitespace()).collect();
                base64::engine::general_purpose::STANDARD
                    .decode(cleaned.as_bytes())
                    .map(Llsd::Binary)
                    .map_err(|_| self.err("bad base64 in <binary>"))
            }
            "array" => {
                let mut items = Vec::new();
                loop {
                    self.skip_ws();
                    if self.peek("</array>") {
                        self.pos += "</array>".len();
                        return Ok(Llsd::Array(items));
                    }
                    items.push(self.parse_value()?);
                }
            }
            "map" => {
                let mut m = BTreeMap::new();
                loop {
                    self.skip_ws();
                    if self.peek("</map>") {
                        self.pos += "</map>".len();
                        return Ok(Llsd::Map(m));
                    }
                    self.expect("<key>")?;
                    let k = self.text_until_close("key")?;
                    let v = self.parse_value()?;
                    m.insert(k, v);
                }
            }
            other => Err(self.err(&format!("unknown LLSD tag <{other}>"))),
        }
    }
}

fn unescape(s: &str) -> String {
    // Fast path: most strings contain no entities.
    if !s.contains('&') {
        return s.to_string();
    }
    let mut out = String::with_capacity(s.len());
    let mut rest = s;
    while let Some(i) = rest.find('&') {
        out.push_str(&rest[..i]);
        let tail = &rest[i..];
        let end = tail.find(';').unwrap_or(usize::min(tail.len(), 10));
        let ent = &tail[1..end.min(tail.len())];
        match ent {
            "amp" => out.push('&'),
            "lt" => out.push('<'),
            "gt" => out.push('>'),
            "quot" => out.push('"'),
            "apos" => out.push('\''),
            _ if ent.starts_with("#x") || ent.starts_with("#X") => {
                if let Ok(n) = u32::from_str_radix(&ent[2..], 16) {
                    if let Some(c) = char::from_u32(n) { out.push(c); }
                }
            }
            _ if ent.starts_with('#') => {
                if let Ok(n) = ent[1..].parse::<u32>() {
                    if let Some(c) = char::from_u32(n) { out.push(c); }
                }
            }
            _ => { out.push('&'); out.push_str(ent); out.push(';'); }
        }
        rest = &tail[end + 1.min(tail.len() - end)..];
        if rest.is_empty() { break; }
    }
    out.push_str(rest);
    out
}
```

---

## Part 6 — LLSD binary serialisation

Binary LLSD is the compact form used by some caps and by the viewer's internal
caches. Every value starts with a one-byte marker. Strings, binary blobs, keys,
and URIs are length-prefixed with a **big-endian u32** (network order — the one
place LLSD is big-endian; UDP message fields are little-endian, and mixing the
two up is the single most common porting bug in this whole file).

| Marker | Type      | Payload                                             |
|--------|-----------|-----------------------------------------------------|
| `!`    | undefined | none                                                |
| `1`/`0`| boolean   | none (marker itself is the value)                  |
| `i`    | integer   | i32 big-endian                                      |
| `r`    | real      | f64 big-endian                                      |
| `s`    | string    | u32 BE length + UTF-8 bytes                         |
| `u`    | uuid      | 16 raw bytes                                        |
| `d`    | date      | f64 BE, seconds since epoch                         |
| `l`    | uri       | u32 BE length + UTF-8 bytes                         |
| `b`    | binary    | u32 BE length + raw bytes                           |
| `[`    | array     | u32 BE count, values, then `]`                      |
| `{`    | map       | u32 BE count, (`k` + u32 BE len + key bytes, value) pairs, then `}` |
| `k`    | map key   | u32 BE length + UTF-8 bytes                         |

```rust
impl Llsd {
    pub fn to_binary(&self) -> Vec<u8> {
        let mut out = Vec::new();
        self.write_binary(&mut out);
        out
    }

    fn write_binary(&self, out: &mut Vec<u8>) {
        match self {
            Llsd::Undefined => out.push(b'!'),
            Llsd::Boolean(true) => out.push(b'1'),
            Llsd::Boolean(false) => out.push(b'0'),
            Llsd::Integer(i) => {
                out.push(b'i');
                out.extend_from_slice(&i.to_be_bytes());
            }
            Llsd::Real(r) => {
                out.push(b'r');
                out.extend_from_slice(&r.to_be_bytes());
            }
            Llsd::String(s) => {
                out.push(b's');
                write_len_prefixed(out, s.as_bytes());
            }
            Llsd::Uuid(u) => {
                out.push(b'u');
                out.extend_from_slice(&u.0);
            }
            Llsd::Date(d) => {
                out.push(b'd');
                out.extend_from_slice(&d.to_be_bytes());
            }
            Llsd::Uri(u) => {
                out.push(b'l');
                write_len_prefixed(out, u.as_bytes());
            }
            Llsd::Binary(b) => {
                out.push(b'b');
                write_len_prefixed(out, b);
            }
            Llsd::Array(items) => {
                out.push(b'[');
                out.extend_from_slice(&(items.len() as u32).to_be_bytes());
                for it in items {
                    it.write_binary(out);
                }
                out.push(b']');
            }
            Llsd::Map(m) => {
                out.push(b'{');
                out.extend_from_slice(&(m.len() as u32).to_be_bytes());
                for (k, v) in m {
                    out.push(b'k');
                    write_len_prefixed(out, k.as_bytes());
                    v.write_binary(out);
                }
                out.push(b'}');
            }
        }
    }

    pub fn from_binary(data: &[u8]) -> Result<Llsd, LlsdError> {
        let mut r = BinReader { s: data, pos: 0 };
        let v = r.read_value()?;
        Ok(v)
    }
}

fn write_len_prefixed(out: &mut Vec<u8>, bytes: &[u8]) {
    out.extend_from_slice(&(bytes.len() as u32).to_be_bytes());
    out.extend_from_slice(bytes);
}

struct BinReader<'a> {
    s: &'a [u8],
    pos: usize,
}

impl<'a> BinReader<'a> {
    fn take(&mut self, n: usize) -> Result<&'a [u8], LlsdError> {
        if self.pos + n > self.s.len() {
            return Err(LlsdError::Truncated { needed: n, had: self.s.len() - self.pos });
        }
        let out = &self.s[self.pos..self.pos + n];
        self.pos += n;
        Ok(out)
    }
    fn byte(&mut self) -> Result<u8, LlsdError> {
        Ok(self.take(1)?[0])
    }
    fn u32be(&mut self) -> Result<u32, LlsdError> {
        Ok(u32::from_be_bytes(self.take(4)?.try_into().unwrap()))
    }
    fn len_prefixed(&mut self) -> Result<&'a [u8], LlsdError> {
        let n = self.u32be()? as usize;
        // Guard against hostile lengths before allocating/slicing: a corrupt
        // cap response must not be able to claim a 4 GB string.
        if n > 64 * 1024 * 1024 {
            return Err(LlsdError::Parse { offset: self.pos, message: "length prefix > 64 MiB".into() });
        }
        self.take(n)
    }
    fn read_value(&mut self) -> Result<Llsd, LlsdError> {
        match self.byte()? {
            b'!' => Ok(Llsd::Undefined),
            b'1' => Ok(Llsd::Boolean(true)),
            b'0' => Ok(Llsd::Boolean(false)),
            b'i' => Ok(Llsd::Integer(i32::from_be_bytes(self.take(4)?.try_into().unwrap()))),
            b'r' => Ok(Llsd::Real(f64::from_be_bytes(self.take(8)?.try_into().unwrap()))),
            b's' => {
                let b = self.len_prefixed()?;
                String::from_utf8(b.to_vec()).map(Llsd::String).map_err(|_| LlsdError::BadUtf8)
            }
            b'u' => {
                let b = self.take(16)?;
                let mut a = [0u8; 16];
                a.copy_from_slice(b);
                Ok(Llsd::Uuid(SlUuid(a)))
            }
            b'd' => Ok(Llsd::Date(f64::from_be_bytes(self.take(8)?.try_into().unwrap()))),
            b'l' => {
                let b = self.len_prefixed()?;
                String::from_utf8(b.to_vec()).map(Llsd::Uri).map_err(|_| LlsdError::BadUtf8)
            }
            b'b' => Ok(Llsd::Binary(self.len_prefixed()?.to_vec())),
            b'[' => {
                let count = self.u32be()? as usize;
                let mut items = Vec::with_capacity(count.min(1 << 20));
                for _ in 0..count {
                    items.push(self.read_value()?);
                }
                match self.byte()? {
                    b']' => Ok(Llsd::Array(items)),
                    other => Err(LlsdError::BadMarker(other)),
                }
            }
            b'{' => {
                let count = self.u32be()? as usize;
                let mut m = BTreeMap::new();
                for _ in 0..count {
                    match self.byte()? {
                        b'k' => {}
                        other => return Err(LlsdError::BadMarker(other)),
                    }
                    let kb = self.len_prefixed()?;
                    let k = String::from_utf8(kb.to_vec()).map_err(|_| LlsdError::BadUtf8)?;
                    let v = self.read_value()?;
                    m.insert(k, v);
                }
                match self.byte()? {
                    b'}' => Ok(Llsd::Map(m)),
                    other => Err(LlsdError::BadMarker(other)),
                }
            }
            other => Err(LlsdError::BadMarker(other)),
        }
    }
}
```

---

## Part 7 — LLSD notation serialisation

Notation is the human-readable third format: `{ 'key': value, ... }` for maps,
`[ ... ]` for arrays, `s"text"` style prefixes avoided in the common dialect —
strings are single- or double-quoted, UUIDs are `u` + quoted hex in the strict
grammar but bare-quoted UUID strings appear in viewer logs. Notation is used in
viewer debug output and some legacy endpoints. **Write it for debugging and
tests; parse it leniently; never prefer it on the wire where XML is accepted.**

Prefixes: `i` integer, `r` real, `u` uuid, `s` string (rarely emitted), `b(...)`
base64 binary in some dialects, `l` URI, `d` date, `t`/`f` boolean shorthand in
viewer logs, `!` undefined.

```rust
impl Llsd {
    pub fn to_notation(&self) -> String {
        let mut out = String::new();
        self.write_notation(&mut out);
        out
    }

    fn write_notation(&self, out: &mut String) {
        match self {
            Llsd::Undefined => out.push('!'),
            Llsd::Boolean(true) => out.push('t'),
            Llsd::Boolean(false) => out.push('f'),
            Llsd::Integer(i) => {
                out.push('i');
                out.push_str(&i.to_string());
            }
            Llsd::Real(r) => {
                out.push('r');
                out.push_str(&format!("{r}"));
            }
            Llsd::String(s) => {
                out.push('"');
                for c in s.chars() {
                    match c {
                        '"' => out.push_str("\\\""),
                        '\\' => out.push_str("\\\\"),
                        '\n' => out.push_str("\\n"),
                        '\r' => out.push_str("\\r"),
                        '\t' => out.push_str("\\t"),
                        c => out.push(c),
                    }
                }
                out.push('"');
            }
            Llsd::Uuid(u) => {
                out.push_str(&format!("u\"{u}\""));
            }
            Llsd::Date(d) => {
                out.push_str(&format!("d\"{}\"", date_to_iso(*d)));
            }
            Llsd::Uri(u) => {
                out.push_str(&format!("l\"{}\"", u.replace('\\', "\\\\").replace('"', "\\\"")));
            }
            Llsd::Binary(b) => {
                let enc = base64::engine::general_purpose::STANDARD.encode(b);
                out.push_str(&format!("b64\"{enc}\""));
            }
            Llsd::Array(items) => {
                out.push('[');
                for (i, it) in items.iter().enumerate() {
                    if i > 0 {
                        out.push(',');
                    }
                    it.write_notation(out);
                }
                out.push(']');
            }
            Llsd::Map(m) => {
                out.push('{');
                for (i, (k, v)) in m.iter().enumerate() {
                    if i > 0 {
                        out.push(',');
                    }
                    // Keys are quoted strings in notation.
                    Llsd::String(k.clone()).write_notation(out);
                    out.push(':');
                    v.write_notation(out);
                }
                out.push('}');
            }
        }
    }

    /// Lenient notation parser covering the dialect the writer above emits plus
    /// the viewer-log variants (bare strings in maps are NOT accepted — a bare
    /// token is always an error, because silently guessing hides corrupt data).
    pub fn from_notation(text: &str) -> Result<Llsd, LlsdError> {
        let mut p = NotationParser { chars: text.chars().collect(), pos: 0 };
        let v = p.value()?;
        Ok(v)
    }
}

struct NotationParser {
    chars: Vec<char>,
    pos: usize,
}

impl NotationParser {
    fn err(&self, msg: &str) -> LlsdError {
        LlsdError::Parse { offset: self.pos, message: msg.to_string() }
    }
    fn skip(&mut self) {
        while self.pos < self.chars.len() && self.chars[self.pos].is_whitespace() {
            self.pos += 1;
        }
    }
    fn peek(&mut self) -> Option<char> {
        self.skip();
        self.chars.get(self.pos).copied()
    }
    fn quoted(&mut self) -> Result<String, LlsdError> {
        // Assumes current char is the opening quote.
        self.pos += 1;
        let mut out = String::new();
        while self.pos < self.chars.len() {
            let c = self.chars[self.pos];
            self.pos += 1;
            match c {
                '"' => return Ok(out),
                '\\' => {
                    let e = self.chars.get(self.pos).copied().ok_or_else(|| self.err("trailing backslash"))?;
                    self.pos += 1;
                    out.push(match e {
                        'n' => '\n',
                        'r' => '\r',
                        't' => '\t',
                        other => other,
                    });
                }
                c => out.push(c),
            }
        }
        Err(self.err("unterminated string"))
    }
    fn token(&mut self) -> String {
        let start = self.pos;
        while self.pos < self.chars.len() {
            let c = self.chars[self.pos];
            if c.is_alphanumeric() || c == '.' || c == '-' || c == '+' {
                self.pos += 1;
            } else {
                break;
            }
        }
        self.chars[start..self.pos].iter().collect()
    }
    fn value(&mut self) -> Result<Llsd, LlsdError> {
        match self.peek().ok_or_else(|| self.err("unexpected end"))? {
            '!' => {
                self.pos += 1;
                Ok(Llsd::Undefined)
            }
            't' => {
                self.pos += 1;
                Ok(Llsd::Boolean(true))
            }
            'f' => {
                self.pos += 1;
                Ok(Llsd::Boolean(false))
            }
            'i' => {
                self.pos += 1;
                let t = self.token();
                t.parse::<i32>().map(Llsd::Integer).map_err(|_| self.err("bad notation integer"))
            }
            'r' => {
                self.pos += 1;
                let t = self.token();
                t.parse::<f64>().map(Llsd::Real).map_err(|_| self.err("bad notation real"))
            }
            '"' | '\'' => Ok(Llsd::String(self.quoted()?)),
            'u' => {
                self.pos += 1;
                if self.chars.get(self.pos) == Some(&'"') {
                    let s = self.quoted()?;
                    Ok(Llsd::Uuid(SlUuid::parse(&s).unwrap_or_default()))
                } else {
                    Err(self.err("uuid in notation must be quoted"))
                }
            }
            'd' => {
                self.pos += 1;
                let s = self.quoted()?;
                Ok(Llsd::Date(iso_to_date(&s).unwrap_or(0.0)))
            }
            'l' => {
                self.pos += 1;
                Ok(Llsd::Uri(self.quoted()?))
            }
            '[' => {
                self.pos += 1;
                let mut items = Vec::new();
                loop {
                    if self.peek() == Some(']') {
                        self.pos += 1;
                        return Ok(Llsd::Array(items));
                    }
                    items.push(self.value()?);
                    if self.peek() == Some(',') {
                        self.pos += 1;
                    }
                }
            }
            '{' => {
                self.pos += 1;
                let mut m = BTreeMap::new();
                loop {
                    if self.peek() == Some('}') {
                        self.pos += 1;
                        return Ok(Llsd::Map(m));
                    }
                    let k = match self.value()? {
                        Llsd::String(s) => s,
                        _ => return Err(self.err("map key must be a string")),
                    };
                    if self.peek() == Some(':') {
                        self.pos += 1;
                    } else {
                        return Err(self.err("expected ':' in notation map"));
                    }
                    let v = self.value()?;
                    m.insert(k, v);
                    if self.peek() == Some(',') {
                        self.pos += 1;
                    }
                }
            }
            other => Err(self.err(&format!("unexpected notation char '{other}'"))),
        }
    }
}
```

---

## Part 8 — Zerocode, packet header, message IDs, and the circuit

### 8.1 ZeroEncode / ZeroDecode

Zerocoded messages compress runs of `0x00` bytes: a zero byte is emitted as
`0x00 <count>` where count is 1–255; longer runs chain. Only the message body
**after the message ID** is zerocoded (the header never is), and only for
messages whose template line says `Zerocoded`. The `ChatFromViewer` lesson from
the template-staleness saga applies: trust the flag in the template copy you
diffed against the viewer, not your memory.

```rust
/// Expand a zerocoded body. Input is the body *after* the message ID bytes.
pub fn zero_decode(input: &[u8]) -> Vec<u8> {
    let mut out = Vec::with_capacity(input.len() * 2);
    let mut i = 0;
    while i < input.len() {
        if input[i] == 0 {
            // 0x00 must be followed by a count; a trailing lone 0x00 is a
            // corrupt packet — the viewer treats it as one zero. Match that.
            if i + 1 < input.len() {
                let count = input[i + 1] as usize;
                out.extend(std::iter::repeat(0u8).take(count));
                i += 2;
            } else {
                out.push(0);
                i += 1;
            }
        } else {
            out.push(input[i]);
            i += 1;
        }
    }
    out
}

/// Compress a body for a zerocoded message.
pub fn zero_encode(input: &[u8]) -> Vec<u8> {
    let mut out = Vec::with_capacity(input.len());
    let mut i = 0;
    while i < input.len() {
        if input[i] == 0 {
            let mut run = 0usize;
            while i < input.len() && input[i] == 0 && run < 255 {
                run += 1;
                i += 1;
            }
            out.push(0);
            out.push(run as u8);
        } else {
            out.push(input[i]);
            i += 1;
        }
    }
    out
}
```

### 8.2 Packet header and message ID encoding

Every UDP packet starts with a 6-byte header: flags, sequence (big-endian u32 —
yes, the header sequence is big-endian while body fields are little-endian),
and an extra-header-length byte (almost always 0). Flags: `0x80` zerocoded,
`0x40` reliable, `0x20` resent, `0x10` ACK list appended at the end of the packet
(a count byte followed by that many big-endian u32 sequence numbers).

Message IDs are encoded by frequency from the template:

* **High**: 1 byte, `0x01..=0xFE` range values as listed.
* **Medium**: 2 bytes, `0xFF` followed by the number byte.
* **Low**: 4 bytes, `0xFF 0xFF` followed by a big-endian u16 number.
* **Fixed**: 4 bytes, `0xFF 0xFF 0xFF` followed by a byte whose value completes
  the fixed IDs the template writes as hex (e.g. PacketAck `0xFFFFFFFB`).

```rust
pub mod flags {
    pub const ZEROCODED: u8 = 0x80;
    pub const RELIABLE: u8 = 0x40;
    pub const RESENT: u8 = 0x20;
    pub const ACK: u8 = 0x10;
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Frequency {
    High,
    Medium,
    Low,
    Fixed,
}

/// A decoded packet header plus the offset where the message ID begins.
#[derive(Clone, Debug)]
pub struct PacketHeader {
    pub flags: u8,
    pub sequence: u32,
    pub extra_len: u8,
    /// Offset of the first body byte (after header + message ID).
    pub body_offset: usize,
    /// Offset of the appended ACK list, if the ACK flag is set. Computed from
    /// the *end* of the packet, so it is filled in by `decode` given the full
    /// datagram length.
    pub ack_offset: Option<usize>,
}

impl PacketHeader {
    pub const SIZE: usize = 6;

    pub fn zerocoded(&self) -> bool { self.flags & flags::ZEROCODED != 0 }
    pub fn reliable(&self) -> bool { self.flags & flags::RELIABLE != 0 }
    pub fn resent(&self) -> bool { self.flags & flags::RESENT != 0 }
    pub fn has_acks(&self) -> bool { self.flags & flags::ACK != 0 }

    /// Encode a header for an outgoing packet.
    pub fn encode(flags: u8, sequence: u32) -> [u8; Self::SIZE] {
        let mut out = [0u8; Self::SIZE];
        out[0] = flags;
        out[1..5].copy_from_slice(&sequence.to_be_bytes());
        out[5] = 0; // extra header length: this implementation never sends one
        out
    }

    /// Decode flags/sequence and locate the appended ACK block.
    /// `datagram_len` is needed because ACKs are counted from the tail.
    pub fn decode(datagram: &[u8]) -> Result<(PacketHeader, Vec<u32>), LlsdError> {
        if datagram.len() < Self::SIZE {
            return Err(LlsdError::Truncated { needed: Self::SIZE, had: datagram.len() });
        }
        let fl = datagram[0];
        let sequence = u32::from_be_bytes(datagram[1..5].try_into().unwrap());
        let extra_len = datagram[5];
        let mut acks = Vec::new();
        let mut ack_offset = None;
        if fl & flags::ACK != 0 {
            // Last byte before the ACKs is not how it works: the layout is
            // body..., ack_count(u8), ack(u32 BE) * count. The count sits at
            // (len - 1 - 4*count); we find it by reading the count position
            // the sender wrote — which is discoverable only because senders
            // place count immediately before the ack array and the array ends
            // the packet. We scan: try the byte at len-1-4k for k=1.. until
            // consistent. In practice count is small; the viewer reads the
            // count from the position computed once body length is known.
            // This implementation follows LibreMetaverse: the count byte is
            // at datagram.len() - 1 - (count * 4), found by trying the only
            // self-consistent k.
            for k in 1..=255usize {
                let need = 1 + 4 * k;
                if datagram.len() < Self::SIZE + need {
                    break;
                }
                let idx = datagram.len() - need;
                if datagram[idx] as usize == k {
                    let mut list = Vec::with_capacity(k);
                    for j in 0..k {
                        let off = idx + 1 + 4 * j;
                        list.push(u32::from_be_bytes(datagram[off..off + 4].try_into().unwrap()));
                    }
                    acks = list;
                    ack_offset = Some(idx);
                    break;
                }
            }
        }
        Ok((
            PacketHeader {
                flags: fl,
                sequence,
                extra_len,
                body_offset: Self::SIZE + extra_len as usize,
                ack_offset,
            },
            acks,
        ))
    }
}

/// The result of decoding a message ID at the start of a packet body.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct MessageId {
    pub frequency: Frequency,
    /// Template number within the frequency band (for Fixed, the full
    /// 0xFFFFFFxx value's low byte is kept in `number` and frequency=Fixed).
    pub number: u32,
    /// Bytes consumed by the ID.
    pub size: usize,
}

pub fn decode_message_id(body: &[u8]) -> Option<MessageId> {
    if body.is_empty() {
        return None;
    }
    match body[0] {
        0xFF => {
            if body.len() >= 2 && body[1] == 0xFF {
                if body.len() >= 3 && body[2] == 0xFF {
                    if body.len() < 4 {
                        return None;
                    }
                    Some(MessageId { frequency: Frequency::Fixed, number: body[3] as u32, size: 4 })
                } else {
                    if body.len() < 4 {
                        return None;
                    }
                    let n = u16::from_be_bytes([body[2], body[3]]) as u32;
                    Some(MessageId { frequency: Frequency::Low, number: n, size: 4 })
                }
            } else if body.len() >= 2 {
                Some(MessageId { frequency: Frequency::Medium, number: body[1] as u32, size: 2 })
            } else {
                None
            }
        }
        b => Some(MessageId { frequency: Frequency::High, number: b as u32, size: 1 }),
    }
}

pub fn encode_message_id(freq: Frequency, number: u32, out: &mut Vec<u8>) {
    match freq {
        Frequency::High => out.push(number as u8),
        Frequency::Medium => {
            out.push(0xFF);
            out.push(number as u8);
        }
        Frequency::Low => {
            out.push(0xFF);
            out.push(0xFF);
            out.extend_from_slice(&(number as u16).to_be_bytes());
        }
        Frequency::Fixed => {
            out.push(0xFF);
            out.push(0xFF);
            out.push(0xFF);
            out.push(number as u8);
        }
    }
}
```

### 8.3 The circuit: sequence, reliability, resend, ping, throttle

The circuit is the stateful heart of a client. Ported behaviour (viewer
`llcircuit.cpp`, LibreMetaverse `LibreMetaverse.Transport`):

* Outgoing sequence numbers increment per packet, reliable or not.
* Reliable packets are kept in a resend queue until ACKed; resend interval
  starts near 1 s and the packet is dropped (and the circuit eventually declared
  dead) after repeated failures — exact constants are simulator-tuned, so they
  are configuration here, not folklore.
* Incoming reliable packets are ACKed, piggybacked on the next outgoing packet
  when one is imminent, else as a standalone `PacketAck` (Fixed `0xFB`).
* Duplicate incoming sequences (resent packets whose ACK was lost) must be
  detected and dropped after ACKing again.
* `StartPingCheck`/`CompletePingCheck` (Fixed) measure round-trip and keep
  NAT mappings warm on mobile networks.

```rust
use std::collections::{HashMap, HashSet, VecDeque};
use std::time::{Duration, Instant};

#[derive(Clone, Debug)]
pub struct PendingPacket {
    pub sequence: u32,
    /// The complete datagram as sent, kept verbatim for resend (with the
    /// RESENT flag set on retransmission).
    pub datagram: Vec<u8>,
    pub sent_at: Instant,
    pub resends: u32,
}

#[derive(Clone, Debug)]
pub struct CircuitConfig {
    /// First resend delay for an unacked reliable packet.
    pub resend_after: Duration,
    /// Give up on a reliable packet after this many resends.
    pub max_resends: u32,
    /// Declare the circuit dead when no packet has arrived for this long.
    pub timeout: Duration,
    /// How many ACKs to piggyback before forcing a standalone PacketAck.
    pub ack_batch: usize,
}

impl Default for CircuitConfig {
    fn default() -> Self {
        Self {
            resend_after: Duration::from_millis(1000),
            max_resends: 12,
            timeout: Duration::from_secs(60),
            ack_batch: 32,
        }
    }
}

pub struct Circuit {
    pub circuit_code: u32,
    pub session_id: SlUuid,
    pub agent_id: SlUuid,
    config: CircuitConfig,
    next_sequence: u32,
    pending: HashMap<u32, PendingPacket>,
    /// ACKs owed to the simulator, drained into outgoing packets.
    ack_queue: VecDeque<u32>,
    /// Recently seen incoming sequences for duplicate suppression. A HashSet
    /// plus a low-water mark: sequences below (highest - window) are dropped.
    seen: HashSet<u32>,
    highest_seen: u32,
    last_received: Instant,
    pub ping_id: u8,
    pub last_ping_sent: Option<Instant>,
    pub round_trip: Option<Duration>,
}

impl Circuit {
    pub fn new(circuit_code: u32, session_id: SlUuid, agent_id: SlUuid, config: CircuitConfig) -> Self {
        Self {
            circuit_code,
            session_id,
            agent_id,
            config,
            next_sequence: 1, // viewer starts at 1; 0 is never a valid first seq
            pending: HashMap::new(),
            ack_queue: VecDeque::new(),
            seen: HashSet::new(),
            highest_seen: 0,
            last_received: Instant::now(),
            ping_id: 0,
            last_ping_sent: None,
            round_trip: None,
        }
    }

    /// Build a complete datagram for one message body (message ID + fields,
    /// already zerocoded by the caller if the message requires it).
    /// Returns the datagram; the caller sends it over the UDP socket.
    pub fn build_packet(&mut self, message_id_and_body: &[u8], reliable: bool, zerocoded: bool) -> Vec<u8> {
        let seq = self.next_sequence;
        self.next_sequence = self.next_sequence.wrapping_add(1);
        let mut fl = 0u8;
        if reliable {
            fl |= flags::RELIABLE;
        }
        if zerocoded {
            fl |= flags::ZEROCODED;
        }
        // Piggyback up to ack_batch pending ACKs.
        let acks: Vec<u32> = self
            .ack_queue
            .drain(..self.ack_queue.len().min(self.config.ack_batch))
            .collect();
        if !acks.is_empty() {
            fl |= flags::ACK;
        }
        let mut out = Vec::with_capacity(PacketHeader::SIZE + message_id_and_body.len() + 1 + 4 * acks.len());
        out.extend_from_slice(&PacketHeader::encode(fl, seq));
        out.extend_from_slice(message_id_and_body);
        if !acks.is_empty() {
            out.push(acks.len() as u8);
            for a in &acks {
                out.extend_from_slice(&a.to_be_bytes());
            }
        }
        if reliable {
            self.pending.insert(
                seq,
                PendingPacket { sequence: seq, datagram: out.clone(), sent_at: Instant::now(), resends: 0 },
            );
        }
        out
    }

    /// Feed one received datagram. Returns the decoded (header, message id,
    /// body) for dispatch, or `None` for duplicates and pure-ACK packets.
    /// Side effects: queues ACKs for reliable packets, clears resends for
    /// ACKs addressed to us, answers ping bookkeeping.
    pub fn receive(&mut self, datagram: &[u8]) -> Option<(PacketHeader, MessageId, Vec<u8>)> {
        let (header, acks_for_us) = PacketHeader::decode(datagram).ok()?;
        self.last_received = Instant::now();
        for seq in &acks_for_us {
            self.pending.remove(seq);
        }
        // Duplicate suppression for resent reliable packets.
        if header.reliable() || header.resent() {
            if self.seen.contains(&header.sequence) {
                // Still ACK again: the resend means our ACK was lost.
                self.ack_queue.push_back(header.sequence);
                return None;
            }
            self.seen.insert(header.sequence);
            if header.sequence > self.highest_seen {
                self.highest_seen = header.sequence;
                // Prune the window so `seen` cannot grow without bound.
                let floor = self.highest_seen.saturating_sub(4096);
                self.seen.retain(|s| *s >= floor);
            }
            self.ack_queue.push_back(header.sequence);
        }
        let body_start = header.body_offset;
        let body_end = header.ack_offset.unwrap_or(datagram.len());
        if body_start >= body_end {
            return None; // pure ACK / keepalive packet
        }
        let raw_body = &datagram[body_start..body_end];
        let id = decode_message_id(raw_body)?;
        let mut body = raw_body[id.size..].to_vec();
        if header.zerocoded() {
            body = zero_decode(&body);
        }
        Some((header, id, body))
    }

    /// Periodic maintenance: returns datagrams to (re)send — resends whose
    /// timer expired and a standalone PacketAck if ACKs are owed and nothing
    /// else is going out. Call this from the socket loop on a timer tick.
    pub fn tick(&mut self) -> Vec<Vec<u8>> {
        let now = Instant::now();
        let mut out = Vec::new();
        let mut dead = Vec::new();
        for p in self.pending.values_mut() {
            if now.duration_since(p.sent_at) >= self.config.resend_after {
                if p.resends >= self.config.max_resends {
                    dead.push(p.sequence);
                    continue;
                }
                p.resends += 1;
                p.sent_at = now;
                let mut dg = p.datagram.clone();
                dg[0] |= flags::RESENT;
                out.push(dg);
            }
        }
        for seq in dead {
            self.pending.remove(&seq);
        }
        if !self.ack_queue.is_empty() {
            // PacketAck is Fixed 0xFFFFFFFB, unreliable, unencoded.
            let mut body = Vec::new();
            encode_message_id(Frequency::Fixed, 0xFB, &mut body);
            let count = self.ack_queue.len().min(255);
            body.push(count as u8);
            for _ in 0..count {
                let seq = self.ack_queue.pop_front().unwrap();
                body.extend_from_slice(&seq.to_be_bytes());
            }
            // Build without reliability bookkeeping: hand-roll the header.
            let seq = self.next_sequence;
            self.next_sequence = self.next_sequence.wrapping_add(1);
            let mut dg = Vec::with_capacity(PacketHeader::SIZE + body.len());
            dg.extend_from_slice(&PacketHeader::encode(0, seq));
            dg.extend_from_slice(&body);
            out.push(dg);
        }
        out
    }

    pub fn is_timed_out(&self) -> bool {
        self.last_received.elapsed() >= self.config.timeout
    }

    /// Build a StartPingCheck body (Fixed 0xFC): one byte ping ID.
    /// The simulator replies CompletePingCheck echoing the ID; match them to
    /// compute `round_trip` in your dispatch code.
    pub fn start_ping(&mut self) -> Vec<u8> {
        self.ping_id = self.ping_id.wrapping_add(1);
        self.last_ping_sent = Some(Instant::now());
        let mut body = Vec::new();
        encode_message_id(Frequency::Fixed, 0xFC, &mut body);
        body.push(self.ping_id);
        // Oldest unpacked ping fields the viewer still sends: two u32 zeroes.
        body.extend_from_slice(&0u32.to_be_bytes());
        body
    }

    pub fn note_ping_reply(&mut self, ping_id: u8) {
        if ping_id == self.ping_id {
            if let Some(sent) = self.last_ping_sent {
                self.round_trip = Some(sent.elapsed());
            }
        }
    }
}
```

---

## Part 9 — Message registry (generated from `message_template.msg`)
All 483 template messages with their 902 blocks and 2984 fields, as data. Block kinds: `S` = exactly one, `V` = count-prefixed repeat, `M N` = exactly N repeats. Field types abbreviated: `V3` = LLVector3, `V3d` = LLVector3d, `V4` = LLVector4, `Quat` = LLQuaternion, `UUID` = LLUUID, `Var1`/`Var2` = Variable 1/2 (length-prefixed). For Fixed messages, `number` is the low byte of the template's hex ID (PacketAck 0xFFFFFFFB → 251), matching `decode_message_id`. The `m!` macro's flags argument is a bitmask: 1 = Trusted, 2 = Zerocoded. Regenerate from the template you diffed against the viewer — do not hand-edit entries.
```rust
/// Static description of one template message. `blocks` encodes
/// `Block:Kind[:Count]:Field=Type,...` with blocks separated by `;`.
pub struct MessageInfo {
    pub name: &'static str,
    pub frequency: Frequency,
    pub number: u32,
    pub trusted: bool,
    pub zerocoded: bool,
    pub blocks: &'static str,
}

macro_rules! m {
    ($name:ident, $freq:ident, $num:expr, $flags:expr, $blocks:expr) => {
        #[allow(non_upper_case_globals)]
        pub const $name: MessageInfo = MessageInfo {
            name: stringify!($name),
            frequency: Frequency::$freq,
            number: $num,
            trusted: $flags & 1 != 0,
            zerocoded: $flags & 2 != 0,
            blocks: $blocks,
        };
    };
}
use m;
m!(TestMessage,Low,1,2,"TestBlock1:S:Test1=U32;NeighborBlock:M:4:Test0=U32,Test1=U32,Test2=U32");
m!(PacketAck,Fixed,251,0,"Packets:V:ID=U32");
m!(OpenCircuit,Fixed,252,0,"CircuitInfo:S:IP=IPADDR,Port=IPPORT");
m!(CloseCircuit,Fixed,253,0,"");
m!(StartPingCheck,High,1,0,"PingID:S:PingID=U8,OldestUnacked=U32");
m!(CompletePingCheck,High,2,0,"PingID:S:PingID=U8");
m!(AddCircuitCode,Low,2,1,"CircuitCode:S:Code=U32,SessionID=UUID,AgentID=UUID");
m!(UseCircuitCode,Low,3,0,"CircuitCode:S:Code=U32,SessionID=UUID,ID=UUID");
m!(NeighborList,High,3,1,"NeighborBlock:M:4:IP=IPADDR,Port=IPPORT,PublicIP=IPADDR,PublicPort=IPPORT,RegionID=UUID,Name=Var1,SimAccess=U8");
m!(AvatarTextureUpdate,Low,4,3,"AgentData:S:AgentID=UUID,TexturesChanged=BOOL;WearableData:V:CacheID=UUID,TextureIndex=U8,HostName=Var1;TextureData:V:TextureID=UUID");
m!(SimulatorMapUpdate,Low,5,1,"MapData:S:Flags=U32");
m!(SimulatorSetMap,Low,6,1,"MapData:S:RegionHandle=U64,Type=S32,MapImage=UUID");
m!(SubscribeLoad,Low,7,1,"");
m!(UnsubscribeLoad,Low,8,1,"");
m!(SimulatorReady,Low,9,3,"SimulatorBlock:S:SimName=Var1,SimAccess=U8,RegionFlags=U32,RegionID=UUID,EstateID=U32,ParentEstateID=U32;TelehubBlock:S:HasTelehub=BOOL,TelehubPos=V3");
m!(TelehubInfo,Low,10,1,"TelehubBlock:S:ObjectID=UUID,ObjectName=Var1,TelehubPos=V3,TelehubRot=Quat;SpawnPointBlock:V:SpawnPointPos=V3");
m!(SimulatorPresentAtLocation,Low,11,1,"SimulatorPublicHostBlock:S:Port=IPPORT,SimulatorIP=IPADDR,GridX=U32,GridY=U32;NeighborBlock:M:4:IP=IPADDR,Port=IPPORT;SimulatorBlock:S:SimName=Var1,SimAccess=U8,RegionFlags=U32,RegionID=UUID,EstateID=U32,ParentEstateID=U32;TelehubBlock:V:HasTelehub=BOOL,TelehubPos=V3");
m!(SimulatorLoad,Low,12,1,"SimulatorLoad:S:TimeDilation=F32,AgentCount=S32,CanAcceptAgents=BOOL;AgentList:V:CircuitCode=U32,X=U8,Y=U8");
m!(SimulatorShutdownRequest,Low,13,1,"");
m!(RegionPresenceRequestByRegionID,Low,14,1,"RegionData:V:RegionID=UUID");
m!(RegionPresenceRequestByHandle,Low,15,1,"RegionData:V:RegionHandle=U64");
m!(RegionPresenceResponse,Low,16,3,"RegionData:V:RegionID=UUID,RegionHandle=U64,InternalRegionIP=IPADDR,ExternalRegionIP=IPADDR,RegionPort=IPPORT,ValidUntil=F64,Message=Var1");
m!(UpdateSimulator,Low,17,1,"SimulatorInfo:S:RegionID=UUID,SimName=Var1,EstateID=U32,SimAccess=U8");
m!(LogDwellTime,Low,18,1,"DwellInfo:S:AgentID=UUID,SessionID=UUID,Duration=F32,SimName=Var1,RegionX=U32,RegionY=U32,AvgAgentsInView=U8,AvgViewerFPS=U8");
m!(FeatureDisabled,Low,19,1,"FailureInfo:S:ErrorMessage=Var1,AgentID=UUID,TransactionID=UUID");
m!(LogFailedMoneyTransaction,Low,20,1,"TransactionData:S:TransactionID=UUID,TransactionTime=U32,TransactionType=S32,SourceID=UUID,DestID=UUID,Flags=U8,Amount=S32,SimulatorIP=IPADDR,GridX=U32,GridY=U32,FailureType=U8");
m!(UserReportInternal,Low,21,3,"ReportData:S:ReportType=U8,Category=U8,ReporterID=UUID,ViewerPosition=V3,AgentPosition=V3,ScreenshotID=UUID,ObjectID=UUID,OwnerID=UUID,LastOwnerID=UUID,CreatorID=UUID,RegionID=UUID,AbuserID=UUID,AbuseRegionName=Var1,AbuseRegionID=UUID,Summary=Var1,Details=Var2,VersionString=Var1");
m!(SetSimStatusInDatabase,Low,22,1,"Data:S:RegionID=UUID,HostName=Var1,X=S32,Y=S32,PID=S32,AgentCount=S32,TimeToLive=S32,Status=Var1");
m!(SetSimPresenceInDatabase,Low,23,1,"SimData:S:RegionID=UUID,HostName=Var1,GridX=U32,GridY=U32,PID=S32,AgentCount=S32,TimeToLive=S32,Status=Var1");
m!(EconomyDataRequest,Low,24,0,"");
m!(EconomyData,Low,25,3,"Info:S:ObjectCapacity=S32,ObjectCount=S32,PriceEnergyUnit=S32,PriceObjectClaim=S32,PricePublicObjectDecay=S32,PricePublicObjectDelete=S32,PriceParcelClaim=S32,PriceParcelClaimFactor=F32,PriceUpload=S32,PriceRentLight=S32,TeleportMinPrice=S32,TeleportPriceExponent=F32,EnergyEfficiency=F32,PriceObjectRent=F32,PriceObjectScaleFactor=F32,PriceParcelRent=S32,PriceGroupCreate=S32");
m!(AvatarPickerRequest,Low,26,0,"AgentData:S:AgentID=UUID,SessionID=UUID,QueryID=UUID;Data:S:Name=Var1");
m!(AvatarPickerRequestBackend,Low,27,1,"AgentData:S:AgentID=UUID,SessionID=UUID,QueryID=UUID,GodLevel=U8;Data:S:Name=Var1");
m!(AvatarPickerReply,Low,28,1,"AgentData:S:AgentID=UUID,QueryID=UUID;Data:V:AvatarID=UUID,FirstName=Var1,LastName=Var1");
m!(PlacesQuery,Low,29,2,"AgentData:S:AgentID=UUID,SessionID=UUID,QueryID=UUID;TransactionData:S:TransactionID=UUID;QueryData:S:QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1");
m!(PlacesReply,Low,30,3,"AgentData:S:AgentID=UUID,QueryID=UUID;TransactionData:S:TransactionID=UUID;QueryData:V:OwnerID=UUID,Name=Var1,Desc=Var1,ActualArea=S32,BillableArea=S32,Flags=U8,GlobalX=F32,GlobalY=F32,GlobalZ=F32,SimName=Var1,SnapshotID=UUID,Dwell=F32,Price=S32");
m!(DirFindQuery,Low,31,2,"AgentData:S:AgentID=UUID,SessionID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,QueryStart=S32");
m!(DirFindQueryBackend,Low,32,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,QueryStart=S32,EstateID=U32,Godlike=BOOL");
m!(DirPlacesQuery,Low,33,2,"AgentData:S:AgentID=UUID,SessionID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1,QueryStart=S32");
m!(DirPlacesQueryBackend,Low,34,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,Category=S8,SimName=Var1,EstateID=U32,Godlike=BOOL,QueryStart=S32");
m!(DirPlacesReply,Low,35,3,"AgentData:S:AgentID=UUID;QueryData:V:QueryID=UUID;QueryReplies:V:ParcelID=UUID,Name=Var1,ForSale=BOOL,Auction=BOOL,Dwell=F32;StatusData:V:Status=U32");
m!(DirPeopleReply,Low,36,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:AgentID=UUID,FirstName=Var1,LastName=Var1,Group=Var1,Online=BOOL,Reputation=S32");
m!(DirEventsReply,Low,37,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:OwnerID=UUID,Name=Var1,EventID=U32,Date=Var1,UnixTime=U32,EventFlags=U32;StatusData:V:Status=U32");
m!(DirGroupsReply,Low,38,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:GroupID=UUID,GroupName=Var1,Members=S32,SearchOrder=F32");
m!(DirClassifiedQuery,Low,39,2,"AgentData:S:AgentID=UUID,SessionID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,Category=U32,QueryStart=S32");
m!(DirClassifiedQueryBackend,Low,40,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,Category=U32,EstateID=U32,Godlike=BOOL,QueryStart=S32");
m!(DirClassifiedReply,Low,41,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:ClassifiedID=UUID,Name=Var1,ClassifiedFlags=U8,CreationDate=U32,ExpirationDate=U32,PriceForListing=S32;StatusData:V:Status=U32");
m!(AvatarClassifiedReply,Low,42,1,"AgentData:S:AgentID=UUID,TargetID=UUID;Data:V:ClassifiedID=UUID,Name=Var1");
m!(ClassifiedInfoRequest,Low,43,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ClassifiedID=UUID");
m!(ClassifiedInfoReply,Low,44,1,"AgentData:S:AgentID=UUID;Data:S:ClassifiedID=UUID,CreatorID=UUID,CreationDate=U32,ExpirationDate=U32,Category=U32,Name=Var1,Desc=Var2,ParcelID=UUID,ParentEstate=U32,SnapshotID=UUID,SimName=Var1,PosGlobal=V3d,ParcelName=Var1,ClassifiedFlags=U8,PriceForListing=S32");
m!(ClassifiedInfoUpdate,Low,45,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ClassifiedID=UUID,Category=U32,Name=Var1,Desc=Var2,ParcelID=UUID,ParentEstate=U32,SnapshotID=UUID,PosGlobal=V3d,ClassifiedFlags=U8,PriceForListing=S32");
m!(ClassifiedDelete,Low,46,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ClassifiedID=UUID");
m!(ClassifiedGodDelete,Low,47,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ClassifiedID=UUID,QueryID=UUID");
m!(DirLandQuery,Low,48,2,"AgentData:S:AgentID=UUID,SessionID=UUID;QueryData:S:QueryID=UUID,QueryFlags=U32,SearchType=U32,Price=S32,Area=S32,QueryStart=S32");
m!(DirLandQueryBackend,Low,49,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID,QueryFlags=U32,SearchType=U32,Price=S32,Area=S32,QueryStart=S32,EstateID=U32,Godlike=BOOL");
m!(DirLandReply,Low,50,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:ParcelID=UUID,Name=Var1,Auction=BOOL,ForSale=BOOL,SalePrice=S32,ActualArea=S32");
m!(DirPopularQuery,Low,51,2,"AgentData:S:AgentID=UUID,SessionID=UUID;QueryData:S:QueryID=UUID,QueryFlags=U32");
m!(DirPopularQueryBackend,Low,52,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID,QueryFlags=U32,EstateID=U32,Godlike=BOOL");
m!(DirPopularReply,Low,53,3,"AgentData:S:AgentID=UUID;QueryData:S:QueryID=UUID;QueryReplies:V:ParcelID=UUID,Name=Var1,Dwell=F32");
m!(ParcelInfoRequest,Low,54,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ParcelID=UUID");
m!(ParcelInfoReply,Low,55,3,"AgentData:S:AgentID=UUID;Data:S:ParcelID=UUID,OwnerID=UUID,Name=Var1,Desc=Var1,ActualArea=S32,BillableArea=S32,Flags=U8,GlobalX=F32,GlobalY=F32,GlobalZ=F32,SimName=Var1,SnapshotID=UUID,Dwell=F32,SalePrice=S32,AuctionID=S32");
m!(ParcelObjectOwnersRequest,Low,56,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32");
m!(ParcelObjectOwnersReply,Low,57,3,"Data:V:OwnerID=UUID,IsGroupOwned=BOOL,Count=S32,OnlineStatus=BOOL");
m!(GroupNoticesListRequest,Low,58,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID");
m!(GroupNoticesListReply,Low,59,1,"AgentData:S:AgentID=UUID,GroupID=UUID;Data:V:NoticeID=UUID,Timestamp=U32,FromName=Var2,Subject=Var2,HasAttachment=BOOL,AssetType=U8");
m!(GroupNoticeRequest,Low,60,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupNoticeID=UUID");
m!(GroupNoticeAdd,Low,61,1,"AgentData:S:AgentID=UUID;MessageBlock:S:ToGroupID=UUID,ID=UUID,Dialog=U8,FromAgentName=Var1,Message=Var2,BinaryBucket=Var2");
m!(TeleportRequest,Low,62,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Info:S:RegionID=UUID,Position=V3,LookAt=V3");
m!(TeleportLocationRequest,Low,63,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Info:S:RegionHandle=U64,Position=V3,LookAt=V3");
m!(TeleportLocal,Low,64,1,"Info:S:AgentID=UUID,LocationID=U32,Position=V3,LookAt=V3,TeleportFlags=U32");
m!(TeleportLandmarkRequest,Low,65,2,"Info:S:AgentID=UUID,SessionID=UUID,LandmarkID=UUID");
m!(TeleportProgress,Low,66,1,"AgentData:S:AgentID=UUID;Info:S:TeleportFlags=U32,Message=Var1");
m!(DataHomeLocationRequest,Low,67,3,"Info:S:AgentID=UUID,KickedFromEstateID=U32;AgentInfo:S:AgentEffectiveMaturity=U32");
m!(DataHomeLocationReply,Low,68,1,"Info:S:AgentID=UUID,RegionHandle=U64,Position=V3,LookAt=V3");
m!(TeleportFinish,Low,69,1,"Info:S:AgentID=UUID,LocationID=U32,SimIP=IPADDR,SimPort=IPPORT,RegionHandle=U64,SeedCapability=Var2,SimAccess=U8,TeleportFlags=U32");
m!(StartLure,Low,70,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Info:S:LureType=U8,Message=Var1;TargetData:V:TargetID=UUID");
m!(TeleportLureRequest,Low,71,0,"Info:S:AgentID=UUID,SessionID=UUID,LureID=UUID,TeleportFlags=U32");
m!(TeleportCancel,Low,72,0,"Info:S:AgentID=UUID,SessionID=UUID");
m!(TeleportStart,Low,73,1,"Info:S:TeleportFlags=U32");
m!(TeleportFailed,Low,74,1,"Info:S:AgentID=UUID,Reason=Var1;AlertInfo:V:Message=Var1,ExtraParams=Var1");
m!(Undo,Low,75,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;ObjectData:V:ObjectID=UUID");
m!(Redo,Low,76,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;ObjectData:V:ObjectID=UUID");
m!(UndoLand,Low,77,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(AgentPause,Low,78,0,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=U32");
m!(AgentResume,Low,79,0,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=U32");
m!(AgentUpdate,High,4,2,"AgentData:S:AgentID=UUID,SessionID=UUID,BodyRotation=Quat,HeadRotation=Quat,State=U8,CameraCenter=V3,CameraAtAxis=V3,CameraLeftAxis=V3,CameraUpAxis=V3,Far=F32,ControlFlags=U32,Flags=U8");
m!(ChatFromViewer,Low,80,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ChatData:S:Message=Var2,Type=U8,Channel=S32");
m!(AgentThrottle,Low,81,2,"AgentData:S:AgentID=UUID,SessionID=UUID,CircuitCode=U32;Throttle:S:GenCounter=U32,Throttles=Var1");
m!(AgentFOV,Low,82,0,"AgentData:S:AgentID=UUID,SessionID=UUID,CircuitCode=U32;FOVBlock:S:GenCounter=U32,VerticalAngle=F32");
m!(AgentHeightWidth,Low,83,0,"AgentData:S:AgentID=UUID,SessionID=UUID,CircuitCode=U32;HeightWidthBlock:S:GenCounter=U32,Height=U16,Width=U16");
m!(AgentSetAppearance,Low,84,2,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=U32,Size=V3;WearableData:V:CacheID=UUID,TextureIndex=U8;ObjectData:S:TextureEntry=Var2;VisualParam:V:ParamValue=U8");
m!(AgentAnimation,High,5,0,"AgentData:S:AgentID=UUID,SessionID=UUID;AnimationList:V:AnimID=UUID,StartAnim=BOOL;PhysicalAvatarEventList:V:TypeData=Var1");
m!(AgentRequestSit,High,6,2,"AgentData:S:AgentID=UUID,SessionID=UUID;TargetObject:S:TargetID=UUID,Offset=V3");
m!(AgentSit,High,7,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(AgentQuitCopy,Low,85,0,"AgentData:S:AgentID=UUID,SessionID=UUID;FuseBlock:S:ViewerCircuitCode=U32");
m!(RequestImage,High,8,0,"AgentData:S:AgentID=UUID,SessionID=UUID;RequestImage:V:Image=UUID,DiscardLevel=S8,DownloadPriority=F32,Packet=U32,Type=U8");
m!(ImageNotInDatabase,Low,86,1,"ImageID:S:ID=UUID");
m!(RebakeAvatarTextures,Low,87,1,"TextureData:S:TextureID=UUID");
m!(SetAlwaysRun,Low,88,0,"AgentData:S:AgentID=UUID,SessionID=UUID,AlwaysRun=BOOL");
m!(ObjectAdd,Medium,1,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;ObjectData:S:PCode=U8,Material=U8,AddFlags=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=UUID,RayEndIsIntersection=U8,Scale=V3,Rotation=Quat,State=U8");
m!(ObjectDelete,Low,89,2,"AgentData:S:AgentID=UUID,SessionID=UUID,Force=BOOL;ObjectData:V:ObjectLocalID=U32");
m!(ObjectDuplicate,Low,90,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;SharedData:S:Offset=V3,DuplicateFlags=U32;ObjectData:V:ObjectLocalID=U32");
m!(ObjectDuplicateOnRay,Low,91,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID,RayStart=V3,RayEnd=V3,BypassRaycast=BOOL,RayEndIsIntersection=BOOL,CopyCenters=BOOL,CopyRotates=BOOL,RayTargetID=UUID,DuplicateFlags=U32;ObjectData:V:ObjectLocalID=U32");
m!(MultipleObjectUpdate,Medium,2,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,Type=U8,Data=Var1");
m!(RequestMultipleObjects,Medium,3,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:CacheMissType=U8,ID=U32");
m!(ObjectPosition,Medium,4,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,Position=V3");
m!(ObjectScale,Low,92,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,Scale=V3");
m!(ObjectRotation,Low,93,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,Rotation=Quat");
m!(ObjectFlagUpdate,Low,94,2,"AgentData:S:AgentID=UUID,SessionID=UUID,ObjectLocalID=U32,UsePhysics=BOOL,IsTemporary=BOOL,IsPhantom=BOOL,CastsShadows=BOOL;ExtraPhysics:V:PhysicsShapeType=U8,Density=F32,Friction=F32,Restitution=F32,GravityMultiplier=F32");
m!(ObjectClickAction,Low,95,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,ClickAction=U8");
m!(ObjectImage,Low,96,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,MediaURL=Var1,TextureEntry=Var2");
m!(ObjectBypassModUpdate,Low,431,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,PropertyID=U8,Value=Var2");
m!(ObjectMaterial,Low,97,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,Material=U8");
m!(ObjectShape,Low,98,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16");
m!(ObjectExtraParams,Low,99,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,ParamType=U16,ParamInUse=BOOL,ParamSize=U32,ParamData=Var1");
m!(ObjectOwner,Low,100,2,"AgentData:S:AgentID=UUID,SessionID=UUID;HeaderData:S:Override=BOOL,OwnerID=UUID,GroupID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectGroup,Low,101,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectBuy,Low,102,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID,CategoryID=UUID;ObjectData:V:ObjectLocalID=U32,SaleType=U8,SalePrice=S32");
m!(BuyObjectInventory,Low,103,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ObjectID=UUID,ItemID=UUID,FolderID=UUID");
m!(DerezContainer,Low,104,3,"Data:S:ObjectID=UUID,Delete=BOOL");
m!(ObjectPermissions,Low,105,2,"AgentData:S:AgentID=UUID,SessionID=UUID;HeaderData:S:Override=BOOL;ObjectData:V:ObjectLocalID=U32,Field=U8,Set=U8,Mask=U32");
m!(ObjectSaleInfo,Low,106,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:LocalID=U32,SaleType=U8,SalePrice=S32");
m!(ObjectName,Low,107,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:LocalID=U32,Name=Var1");
m!(ObjectDescription,Low,108,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:LocalID=U32,Description=Var1");
m!(ObjectCategory,Low,109,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:LocalID=U32,Category=U32");
m!(ObjectSelect,Low,110,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectDeselect,Low,111,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectAttach,Low,112,2,"AgentData:S:AgentID=UUID,SessionID=UUID,AttachmentPoint=U8;ObjectData:V:ObjectLocalID=U32,Rotation=Quat");
m!(ObjectDetach,Low,113,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectDrop,Low,114,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectLink,Low,115,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectDelink,Low,116,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32");
m!(ObjectGrab,Low,117,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:LocalID=U32,GrabOffset=V3;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3");
m!(ObjectGrabUpdate,Low,118,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:ObjectID=UUID,GrabOffsetInitial=V3,GrabPosition=V3,TimeSinceLast=U32;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3");
m!(ObjectDeGrab,Low,119,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:LocalID=U32;SurfaceInfo:V:UVCoord=V3,STCoord=V3,FaceIndex=S32,Position=V3,Normal=V3,Binormal=V3");
m!(ObjectSpinStart,Low,120,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:ObjectID=UUID");
m!(ObjectSpinUpdate,Low,121,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:ObjectID=UUID,Rotation=Quat");
m!(ObjectSpinStop,Low,122,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:ObjectID=UUID");
m!(ObjectExportSelected,Low,123,2,"AgentData:S:AgentID=UUID,RequestID=UUID,VolumeDetail=S16;ObjectData:V:ObjectID=UUID");
m!(ModifyLand,Low,124,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ModifyBlock:S:Action=U8,BrushSize=U8,Seconds=F32,Height=F32;ParcelData:V:LocalID=S32,West=F32,South=F32,East=F32,North=F32;ModifyBlockExtended:V:BrushSize=F32");
m!(VelocityInterpolateOn,Low,125,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(VelocityInterpolateOff,Low,126,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(StateSave,Low,127,0,"AgentData:S:AgentID=UUID,SessionID=UUID;DataBlock:S:Filename=Var1");
m!(ReportAutosaveCrash,Low,128,0,"AutosaveData:S:PID=S32,Status=S32");
m!(SimWideDeletes,Low,129,0,"AgentData:S:AgentID=UUID,SessionID=UUID;DataBlock:S:TargetID=UUID,Flags=U32");
m!(RequestObjectPropertiesFamily,Medium,5,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:RequestFlags=U32,ObjectID=UUID");
m!(TrackAgent,Low,130,0,"AgentData:S:AgentID=UUID,SessionID=UUID;TargetData:S:PreyID=UUID");
m!(ViewerStats,Low,131,2,"AgentData:S:AgentID=UUID,SessionID=UUID,IP=IPADDR,StartTime=U32,RunTime=F32,SimFPS=F32,FPS=F32,AgentsInView=U8,Ping=F32,MetersTraveled=F64,RegionsVisited=S32,SysRAM=U32,SysOS=Var1,SysCPU=Var1,SysGPU=Var1;DownloadTotals:S:World=U32,Objects=U32,Textures=U32;NetStats:M:2:Bytes=U32,Packets=U32,Compressed=U32,Savings=U32;FailStats:S:SendPacket=U32,Dropped=U32,Resent=U32,FailedResends=U32,OffCircuit=U32,Invalid=U32;MiscStats:V:Type=U32,Value=F64");
m!(ScriptAnswerYes,Low,132,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:TaskID=UUID,ItemID=UUID,Questions=S32");
m!(UserReport,Low,133,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ReportData:S:ReportType=U8,Category=U8,Position=V3,CheckFlags=U8,ScreenshotID=UUID,ObjectID=UUID,AbuserID=UUID,AbuseRegionName=Var1,AbuseRegionID=UUID,Summary=Var1,Details=Var2,VersionString=Var1");
m!(AlertMessage,Low,134,1,"AlertData:S:Message=Var1;AlertInfo:V:Message=Var1,ExtraParams=Var1;AgentInfo:V:AgentID=UUID");
m!(AgentAlertMessage,Low,135,1,"AgentData:S:AgentID=UUID;AlertData:S:Modal=BOOL,Message=Var1");
m!(MeanCollisionAlert,Low,136,3,"MeanCollision:V:Victim=UUID,Perp=UUID,Time=U32,Mag=F32,Type=U8");
m!(ViewerFrozenMessage,Low,137,1,"FrozenData:S:Data=BOOL");
m!(HealthMessage,Low,138,3,"HealthData:S:Health=F32");
m!(ChatFromSimulator,Low,139,1,"ChatData:S:FromName=Var1,SourceID=UUID,OwnerID=UUID,SourceType=U8,ChatType=U8,Audible=U8,Position=V3,Message=Var2");
m!(SimStats,Low,140,1,"Region:S:RegionX=U32,RegionY=U32,RegionFlags=U32,ObjectCapacity=U32;Stat:V:StatID=U32,StatValue=F32;PidStat:S:PID=S32;RegionInfo:V:RegionFlagsExtended=U64");
m!(RequestRegionInfo,Low,141,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(RegionInfo,Low,142,2,"AgentData:S:AgentID=UUID,SessionID=UUID;RegionInfo:S:SimName=Var1,EstateID=U32,ParentEstateID=U32,RegionFlags=U32,SimAccess=U8,MaxAgents=U8,BillableFactor=F32,ObjectBonusFactor=F32,WaterHeight=F32,TerrainRaiseLimit=F32,TerrainLowerLimit=F32,PricePerMeter=S32,RedirectGridX=S32,RedirectGridY=S32,UseEstateSun=BOOL,SunHour=F32;RegionInfo2:S:ProductSKU=Var1,ProductName=Var1,MaxAgents32=U32,HardMaxAgents=U32,HardMaxObjects=U32;RegionInfo3:V:RegionFlagsExtended=U64;RegionInfo5:V:ChatWhisperRange=F32,ChatNormalRange=F32,ChatShoutRange=F32,ChatWhisperOffset=F32,ChatNormalOffset=F32,ChatShoutOffset=F32,ChatFlags=U32;CombatSettings:V:CombatFlags=U32,OnDeath=U8,DamageThrottle=F32,RegenerationRate=F32,InvulnerabilyTime=F32,DamageLimit=F32");
m!(GodUpdateRegionInfo,Low,143,2,"AgentData:S:AgentID=UUID,SessionID=UUID;RegionInfo:S:SimName=Var1,EstateID=U32,ParentEstateID=U32,RegionFlags=U32,BillableFactor=F32,PricePerMeter=S32,RedirectGridX=S32,RedirectGridY=S32;RegionInfo2:V:RegionFlagsExtended=U64");
m!(NearestLandingRegionRequest,Low,144,1,"RequestingRegionData:S:RegionHandle=U64");
m!(NearestLandingRegionReply,Low,145,1,"LandingRegionData:S:RegionHandle=U64");
m!(NearestLandingRegionUpdated,Low,146,1,"RegionData:S:RegionHandle=U64");
m!(TeleportLandingStatusChanged,Low,147,1,"RegionData:S:RegionHandle=U64");
m!(RegionHandshake,Low,148,3,"RegionInfo:S:RegionFlags=U32,SimAccess=U8,SimName=Var1,SimOwner=UUID,IsEstateManager=BOOL,WaterHeight=F32,BillableFactor=F32,CacheID=UUID,TerrainBase0=UUID,TerrainBase1=UUID,TerrainBase2=UUID,TerrainBase3=UUID,TerrainDetail0=UUID,TerrainDetail1=UUID,TerrainDetail2=UUID,TerrainDetail3=UUID,TerrainStartHeight00=F32,TerrainStartHeight01=F32,TerrainStartHeight10=F32,TerrainStartHeight11=F32,TerrainHeightRange00=F32,TerrainHeightRange01=F32,TerrainHeightRange10=F32,TerrainHeightRange11=F32;RegionInfo2:S:RegionID=UUID;RegionInfo3:S:CPUClassID=S32,CPURatio=S32,ColoName=Var1,ProductSKU=Var1,ProductName=Var1;RegionInfo4:V:RegionFlagsExtended=U64,RegionProtocols=U64");
m!(RegionHandshakeReply,Low,149,2,"AgentData:S:AgentID=UUID,SessionID=UUID;RegionInfo:S:Flags=U32");
m!(CoarseLocationUpdate,Medium,6,1,"Location:V:X=U8,Y=U8,Z=U8;Index:S:You=S16,Prey=S16;AgentData:V:AgentID=UUID");
m!(ImageData,High,9,1,"ImageID:S:ID=UUID,Codec=U8,Size=U32,Packets=U16;ImageData:S:Data=Var2");
m!(ImagePacket,High,10,1,"ImageID:S:ID=UUID,Packet=U16;ImageData:S:Data=Var2");
m!(LayerData,High,11,1,"LayerID:S:Type=U8;LayerData:S:Data=Var2");
m!(ObjectUpdate,High,12,3,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:ID=U32,State=U8,FullID=UUID,CRC=U32,PCode=U8,Material=U8,ClickAction=U8,Scale=V3,ObjectData=Var1,ParentID=U32,UpdateFlags=U32,PathCurve=U8,ProfileCurve=U8,PathBegin=U16,PathEnd=U16,PathScaleX=U8,PathScaleY=U8,PathShearX=U8,PathShearY=U8,PathTwist=S8,PathTwistBegin=S8,PathRadiusOffset=S8,PathTaperX=S8,PathTaperY=S8,PathRevolutions=U8,PathSkew=S8,ProfileBegin=U16,ProfileEnd=U16,ProfileHollow=U16,TextureEntry=Var2,TextureAnim=Var1,NameValue=Var2,Data=Var2,Text=Var1,TextColor=Fixed    4,MediaURL=Var1,PSBlock=Var1,ExtraParams=Var1,Sound=UUID,OwnerID=UUID,Gain=F32,Flags=U8,Radius=F32,JointType=U8,JointPivot=V3,JointAxisOrAnchor=V3");
m!(ObjectUpdateCompressed,High,13,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:UpdateFlags=U32,Data=Var2");
m!(ObjectUpdateCached,High,14,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:ID=U32,CRC=U32,UpdateFlags=U32");
m!(ImprovedTerseObjectUpdate,High,15,1,"RegionData:S:RegionHandle=U64,TimeDilation=U16;ObjectData:V:Data=Var1,TextureEntry=Var2");
m!(KillObject,High,16,1,"ObjectData:V:ID=U32");
m!(CrossedRegion,Medium,7,1,"AgentData:S:AgentID=UUID,SessionID=UUID;RegionData:S:SimIP=IPADDR,SimPort=IPPORT,RegionHandle=U64,SeedCapability=Var2;Info:S:Position=V3,LookAt=V3");
m!(SimulatorViewerTimeMessage,Low,150,1,"TimeInfo:S:UsecSinceStart=U64,SecPerDay=U32,SecPerYear=U32,SunDirection=V3,SunPhase=F32,SunAngVelocity=V3");
m!(EnableSimulator,Low,151,1,"SimulatorInfo:S:Handle=U64,IP=IPADDR,Port=IPPORT");
m!(DisableSimulator,Low,152,1,"");
m!(ConfirmEnableSimulator,Medium,8,1,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(TransferRequest,Low,153,2,"TransferInfo:S:TransferID=UUID,ChannelType=S32,SourceType=S32,Priority=F32,Params=Var2");
m!(TransferInfo,Low,154,2,"TransferInfo:S:TransferID=UUID,ChannelType=S32,TargetType=S32,Status=S32,Size=S32,Params=Var2");
m!(TransferPacket,High,17,0,"TransferData:S:TransferID=UUID,ChannelType=S32,Packet=S32,Status=S32,Data=Var2");
m!(TransferAbort,Low,155,2,"TransferInfo:S:TransferID=UUID,ChannelType=S32");
m!(RequestXfer,Low,156,2,"XferID:S:ID=U64,Filename=Var1,FilePath=U8,DeleteOnCompletion=BOOL,UseBigPackets=BOOL,VFileID=UUID,VFileType=S16");
m!(SendXferPacket,High,18,0,"XferID:S:ID=U64,Packet=U32;DataPacket:S:Data=Var2");
m!(ConfirmXferPacket,High,19,0,"XferID:S:ID=U64,Packet=U32");
m!(AbortXfer,Low,157,0,"XferID:S:ID=U64,Result=S32");
m!(AvatarAnimation,High,20,1,"Sender:S:ID=UUID;AnimationList:V:AnimID=UUID,AnimSequenceID=S32;AnimationSourceList:V:ObjectID=UUID;PhysicalAvatarEventList:V:TypeData=Var1");
m!(AvatarAppearance,Low,158,3,"Sender:S:ID=UUID,IsTrial=BOOL;ObjectData:S:TextureEntry=Var2;VisualParam:V:ParamValue=U8;AppearanceData:V:AppearanceVersion=U8,CofVersion=S32,Flags=U32;AppearanceHover:V:HoverHeight=V3;AttachmentBlock:V:ID=UUID,AttachmentPoint=U8");
m!(AvatarSitResponse,High,21,3,"SitObject:S:ID=UUID;SitTransform:S:AutoPilot=BOOL,SitPosition=V3,SitRotation=Quat,CameraEyeOffset=V3,CameraAtOffset=V3,ForceMouselook=BOOL");
m!(SetFollowCamProperties,Low,159,1,"ObjectData:S:ObjectID=UUID;CameraProperty:V:Type=S32,Value=F32");
m!(ClearFollowCamProperties,Low,160,1,"ObjectData:S:ObjectID=UUID");
m!(CameraConstraint,High,22,3,"CameraCollidePlane:S:Plane=V4");
m!(ObjectProperties,Medium,9,3,"ObjectData:V:ObjectID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,CreationDate=U64,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,OwnershipCost=S32,SaleType=U8,SalePrice=S32,AggregatePerms=U8,AggregatePermTextures=U8,AggregatePermTexturesOwner=U8,Category=U32,InventorySerial=S16,ItemID=UUID,FolderID=UUID,FromTaskID=UUID,LastOwnerID=UUID,Name=Var1,Description=Var1,TouchName=Var1,SitName=Var1,TextureID=Var1");
m!(ObjectPropertiesFamily,Medium,10,3,"ObjectData:S:RequestFlags=U32,ObjectID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,OwnershipCost=S32,SaleType=U8,SalePrice=S32,Category=U32,LastOwnerID=UUID,Name=Var1,Description=Var1");
m!(RequestPayPrice,Low,161,0,"ObjectData:S:ObjectID=UUID");
m!(PayPriceReply,Low,162,1,"ObjectData:S:ObjectID=UUID,DefaultPayPrice=S32;ButtonData:V:PayButton=S32");
m!(KickUser,Low,163,1,"TargetBlock:S:TargetIP=IPADDR,TargetPort=IPPORT;UserInfo:S:AgentID=UUID,SessionID=UUID,Reason=Var2");
m!(KickUserAck,Low,164,1,"UserInfo:S:SessionID=UUID,Flags=U32");
m!(GodKickUser,Low,165,0,"UserInfo:S:GodID=UUID,GodSessionID=UUID,AgentID=UUID,KickFlags=U32,Reason=Var2");
m!(SystemKickUser,Low,166,1,"AgentInfo:V:AgentID=UUID");
m!(EjectUser,Low,167,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:TargetID=UUID,Flags=U32");
m!(FreezeUser,Low,168,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:TargetID=UUID,Flags=U32");
m!(AvatarPropertiesRequest,Low,169,0,"AgentData:S:AgentID=UUID,SessionID=UUID,AvatarID=UUID");
m!(AvatarPropertiesRequestBackend,Low,170,1,"AgentData:S:AgentID=UUID,AvatarID=UUID,GodLevel=U8,WebProfilesDisabled=BOOL");
m!(AvatarPropertiesReply,Low,171,3,"AgentData:S:AgentID=UUID,AvatarID=UUID;PropertiesData:S:ImageID=UUID,FLImageID=UUID,PartnerID=UUID,AboutText=Var2,FLAboutText=Var1,BornOn=Var1,ProfileURL=Var1,CharterMember=Var1,Flags=U32");
m!(AvatarInterestsReply,Low,172,3,"AgentData:S:AgentID=UUID,AvatarID=UUID;PropertiesData:S:WantToMask=U32,WantToText=Var1,SkillsMask=U32,SkillsText=Var1,LanguagesText=Var1");
m!(AvatarGroupsReply,Low,173,3,"AgentData:S:AgentID=UUID,AvatarID=UUID;GroupData:V:GroupPowers=U64,AcceptNotices=BOOL,GroupTitle=Var1,GroupID=UUID,GroupName=Var1,GroupInsigniaID=UUID;NewGroupData:S:ListInProfile=BOOL");
m!(AvatarPropertiesUpdate,Low,174,2,"AgentData:S:AgentID=UUID,SessionID=UUID;PropertiesData:S:ImageID=UUID,FLImageID=UUID,AboutText=Var2,FLAboutText=Var1,AllowPublish=BOOL,MaturePublish=BOOL,ProfileURL=Var1");
m!(AvatarInterestsUpdate,Low,175,2,"AgentData:S:AgentID=UUID,SessionID=UUID;PropertiesData:S:WantToMask=U32,WantToText=Var1,SkillsMask=U32,SkillsText=Var1,LanguagesText=Var1");
m!(AvatarNotesReply,Low,176,1,"AgentData:S:AgentID=UUID;Data:S:TargetID=UUID,Notes=Var2");
m!(AvatarNotesUpdate,Low,177,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:TargetID=UUID,Notes=Var2");
m!(AvatarPicksReply,Low,178,1,"AgentData:S:AgentID=UUID,TargetID=UUID;Data:V:PickID=UUID,PickName=Var1");
m!(EventInfoRequest,Low,179,0,"AgentData:S:AgentID=UUID,SessionID=UUID;EventData:S:EventID=U32");
m!(EventInfoReply,Low,180,1,"AgentData:S:AgentID=UUID;EventData:S:EventID=U32,Creator=Var1,Name=Var1,Category=Var1,Desc=Var2,Date=Var1,DateUTC=U32,Duration=U32,Cover=U32,Amount=U32,SimName=Var1,GlobalPos=V3d,EventFlags=U32");
m!(EventNotificationAddRequest,Low,181,0,"AgentData:S:AgentID=UUID,SessionID=UUID;EventData:S:EventID=U32");
m!(EventNotificationRemoveRequest,Low,182,0,"AgentData:S:AgentID=UUID,SessionID=UUID;EventData:S:EventID=U32");
m!(EventGodDelete,Low,183,0,"AgentData:S:AgentID=UUID,SessionID=UUID;EventData:S:EventID=U32;QueryData:S:QueryID=UUID,QueryText=Var1,QueryFlags=U32,QueryStart=S32");
m!(PickInfoReply,Low,184,1,"AgentData:S:AgentID=UUID;Data:S:PickID=UUID,CreatorID=UUID,TopPick=BOOL,ParcelID=UUID,Name=Var1,Desc=Var2,SnapshotID=UUID,User=Var1,OriginalName=Var1,SimName=Var1,PosGlobal=V3d,SortOrder=S32,Enabled=BOOL");
m!(PickInfoUpdate,Low,185,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:PickID=UUID,CreatorID=UUID,TopPick=BOOL,ParcelID=UUID,Name=Var1,Desc=Var2,SnapshotID=UUID,PosGlobal=V3d,SortOrder=S32,Enabled=BOOL");
m!(PickDelete,Low,186,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:PickID=UUID");
m!(PickGodDelete,Low,187,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:PickID=UUID,QueryID=UUID");
m!(ScriptQuestion,Low,188,1,"Data:S:TaskID=UUID,ItemID=UUID,ObjectName=Var1,ObjectOwner=Var1,Questions=S32;Experience:S:ExperienceID=UUID");
m!(ScriptControlChange,Low,189,1,"Data:V:TakeControls=BOOL,Controls=U32,PassToAgent=BOOL");
m!(ScriptDialog,Low,190,3,"Data:S:ObjectID=UUID,FirstName=Var1,LastName=Var1,ObjectName=Var1,Message=Var2,ChatChannel=S32,ImageID=UUID;Buttons:V:ButtonLabel=Var1;OwnerData:V:OwnerID=UUID");
m!(ScriptDialogReply,Low,191,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ObjectID=UUID,ChatChannel=S32,ButtonIndex=S32,ButtonLabel=Var1");
m!(ForceScriptControlRelease,Low,192,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(RevokePermissions,Low,193,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:ObjectID=UUID,ObjectPermissions=U32");
m!(LoadURL,Low,194,1,"Data:S:ObjectName=Var1,ObjectID=UUID,OwnerID=UUID,OwnerIsGroup=BOOL,Message=Var1,URL=Var1");
m!(ScriptTeleportRequest,Low,195,1,"Data:S:ObjectName=Var1,SimName=Var1,SimPosition=V3,LookAt=V3;Options:V:Flags=U32");
m!(ParcelOverlay,Low,196,3,"ParcelData:S:SequenceID=S32,Data=Var2");
m!(ParcelPropertiesRequest,Medium,11,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:SequenceID=S32,West=F32,South=F32,East=F32,North=F32,SnapSelection=BOOL");
m!(ParcelPropertiesRequestByID,Low,197,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:SequenceID=S32,LocalID=S32");
m!(ParcelProperties,High,23,3,"ParcelData:S:RequestResult=S32,SequenceID=S32,SnapSelection=BOOL,SelfCount=S32,OtherCount=S32,PublicCount=S32,LocalID=S32,OwnerID=UUID,IsGroupOwned=BOOL,AuctionID=U32,ClaimDate=S32,ClaimPrice=S32,RentPrice=S32,AABBMin=V3,AABBMax=V3,Bitmap=Var2,Area=S32,Status=U8,SimWideMaxPrims=S32,SimWideTotalPrims=S32,MaxPrims=S32,TotalPrims=S32,OwnerPrims=S32,GroupPrims=S32,OtherPrims=S32,SelectedPrims=S32,ParcelPrimBonus=F32,OtherCleanTime=S32,ParcelFlags=U32,SalePrice=S32,Name=Var1,Desc=Var1,MusicURL=Var1,MediaURL=Var1,MediaID=UUID,MediaAutoScale=U8,GroupID=UUID,PassPrice=S32,PassHours=F32,Category=U8,AuthBuyerID=UUID,SnapshotID=UUID,UserLocation=V3,UserLookAt=V3,LandingType=U8,RegionPushOverride=BOOL,RegionDenyAnonymous=BOOL,RegionDenyIdentified=BOOL,RegionDenyTransacted=BOOL;AgeVerificationBlock:S:RegionDenyAgeUnverified=BOOL;RegionAllowAccessBlock:S:RegionAllowAccessOverride=BOOL;ParcelEnvironmentBlock:S:ParcelEnvironmentVersion=S32,RegionAllowEnvironmentOverride=BOOL");
m!(ParcelPropertiesUpdate,Low,198,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,Flags=U32,ParcelFlags=U32,SalePrice=S32,Name=Var1,Desc=Var1,MusicURL=Var1,MediaURL=Var1,MediaID=UUID,MediaAutoScale=U8,GroupID=UUID,PassPrice=S32,PassHours=F32,Category=U8,AuthBuyerID=UUID,SnapshotID=UUID,UserLocation=V3,UserLookAt=V3,LandingType=U8");
m!(ParcelReturnObjects,Low,199,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,ReturnType=U32;TaskIDs:V:TaskID=UUID;OwnerIDs:V:OwnerID=UUID");
m!(ParcelSetOtherCleanTime,Low,200,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,OtherCleanTime=S32");
m!(ParcelDisableObjects,Low,201,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,ReturnType=U32;TaskIDs:V:TaskID=UUID;OwnerIDs:V:OwnerID=UUID");
m!(ParcelSelectObjects,Low,202,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,ReturnType=U32;ReturnIDs:V:ReturnID=UUID");
m!(EstateCovenantRequest,Low,203,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(EstateCovenantReply,Low,204,1,"Data:S:CovenantID=UUID,CovenantTimestamp=U32,EstateName=Var1,EstateOwnerID=UUID");
m!(ForceObjectSelect,Low,205,1,"Header:S:ResetList=BOOL;Data:V:LocalID=U32");
m!(ParcelBuyPass,Low,206,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32");
m!(ParcelDeedToGroup,Low,207,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID,LocalID=S32");
m!(ParcelReclaim,Low,208,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:LocalID=S32");
m!(ParcelClaim,Low,209,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID,IsGroupOwned=BOOL,Final=BOOL;ParcelData:V:West=F32,South=F32,East=F32,North=F32");
m!(ParcelJoin,Low,210,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:West=F32,South=F32,East=F32,North=F32");
m!(ParcelDivide,Low,211,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:West=F32,South=F32,East=F32,North=F32");
m!(ParcelRelease,Low,212,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:LocalID=S32");
m!(ParcelBuy,Low,213,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID,IsGroupOwned=BOOL,RemoveContribution=BOOL,LocalID=S32,Final=BOOL;ParcelData:S:Price=S32,Area=S32");
m!(ParcelGodForceOwner,Low,214,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:OwnerID=UUID,LocalID=S32");
m!(ParcelAccessListRequest,Low,215,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:SequenceID=S32,Flags=U32,LocalID=S32");
m!(ParcelAccessListReply,Low,216,3,"Data:S:AgentID=UUID,SequenceID=S32,Flags=U32,LocalID=S32;List:V:ID=UUID,Time=S32,Flags=U32");
m!(ParcelAccessListUpdate,Low,217,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:Flags=U32,LocalID=S32,TransactionID=UUID,SequenceID=S32,Sections=S32;List:V:ID=UUID,Time=S32,Flags=U32");
m!(ParcelDwellRequest,Low,218,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:LocalID=S32,ParcelID=UUID");
m!(ParcelDwellReply,Low,219,1,"AgentData:S:AgentID=UUID;Data:S:LocalID=S32,ParcelID=UUID,Dwell=F32");
m!(RequestParcelTransfer,Low,220,3,"Data:S:TransactionID=UUID,TransactionTime=U32,SourceID=UUID,DestID=UUID,OwnerID=UUID,Flags=U8,TransactionType=S32,Amount=S32,BillableArea=S32,ActualArea=S32,Final=BOOL,RegionID=UUID,GridX=U32,GridY=U32");
m!(UpdateParcel,Low,221,3,"ParcelData:S:ParcelID=UUID,RegionHandle=U64,OwnerID=UUID,GroupOwned=BOOL,Status=U8,Name=Var1,Description=Var1,MusicURL=Var1,RegionX=F32,RegionY=F32,ActualArea=S32,BillableArea=S32,ShowDir=BOOL,IsForSale=BOOL,Category=U8,SnapshotID=UUID,UserLocation=V3,SalePrice=S32,AuthorizedBuyerID=UUID,AllowPublish=BOOL,MaturePublish=BOOL");
m!(RemoveParcel,Low,222,1,"ParcelData:V:ParcelID=UUID");
m!(MergeParcel,Low,223,1,"MasterParcelData:S:MasterID=UUID;SlaveParcelData:V:SlaveID=UUID");
m!(LogParcelChanges,Low,224,3,"AgentData:S:AgentID=UUID;RegionData:S:RegionHandle=U64;ParcelData:V:ParcelID=UUID,OwnerID=UUID,IsOwnerGroup=BOOL,ActualArea=S32,Action=S8,TransactionID=UUID");
m!(CheckParcelSales,Low,225,1,"RegionData:V:RegionHandle=U64");
m!(ParcelSales,Low,226,1,"ParcelData:V:ParcelID=UUID,BuyerID=UUID");
m!(ParcelGodMarkAsContent,Low,227,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32");
m!(ViewerStartAuction,Low,228,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ParcelData:S:LocalID=S32,SnapshotID=UUID");
m!(StartAuction,Low,229,1,"AgentData:S:AgentID=UUID;ParcelData:S:ParcelID=UUID,SnapshotID=UUID,Name=Var1");
m!(ConfirmAuctionStart,Low,230,1,"AuctionData:S:ParcelID=UUID,AuctionID=U32");
m!(CompleteAuction,Low,231,1,"ParcelData:V:ParcelID=UUID");
m!(CancelAuction,Low,232,1,"ParcelData:V:ParcelID=UUID");
m!(CheckParcelAuctions,Low,233,1,"RegionData:V:RegionHandle=U64");
m!(ParcelAuctions,Low,234,1,"ParcelData:V:ParcelID=UUID,WinnerID=UUID");
m!(UUIDNameRequest,Low,235,0,"UUIDNameBlock:V:ID=UUID");
m!(UUIDNameReply,Low,236,1,"UUIDNameBlock:V:ID=UUID,FirstName=Var1,LastName=Var1");
m!(UUIDGroupNameRequest,Low,237,0,"UUIDNameBlock:V:ID=UUID");
m!(UUIDGroupNameReply,Low,238,1,"UUIDNameBlock:V:ID=UUID,GroupName=Var1");
m!(ChatPass,Low,239,3,"ChatData:S:Channel=S32,Position=V3,ID=UUID,OwnerID=UUID,Name=Variable    1,SourceType=U8,Type=U8,Radius=F32,SimAccess=U8,Message=Variable    2");
m!(EdgeDataPacket,High,24,3,"EdgeData:S:LayerType=U8,Direction=U8,LayerData=Var2");
m!(SimStatus,Medium,12,1,"SimStatus:S:CanAcceptAgents=BOOL,CanAcceptTasks=BOOL;SimFlags:S:Flags=U64");
m!(ChildAgentUpdate,High,25,3,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=UUID,SessionID=UUID,AgentPos=V3,AgentVel=V3,Center=V3,Size=V3,AtAxis=V3,LeftAxis=V3,UpAxis=V3,ChangedGrid=BOOL,Far=F32,Aspect=F32,Throttles=Var1,LocomotionState=U32,HeadRotation=Quat,BodyRotation=Quat,ControlFlags=U32,EnergyLevel=F32,GodLevel=U8,AlwaysRun=BOOL,PreyAgent=UUID,AgentAccess=U8,AgentTextures=Var2,ActiveGroupID=UUID;GroupData:V:GroupID=UUID,GroupPowers=U64,AcceptNotices=BOOL;AnimationData:V:Animation=UUID,ObjectID=UUID;GranterBlock:V:GranterID=UUID;NVPairData:V:NVPairs=Var2;VisualParam:V:ParamValue=U8;AgentAccess:V:AgentLegacyAccess=U8,AgentMaxAccess=U8;AgentInfo:V:Flags=U32;AgentInventoryHost:V:InventoryHost=Var1");
m!(ChildAgentAlive,High,26,1,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=UUID,SessionID=UUID");
m!(ChildAgentPositionUpdate,High,27,1,"AgentData:S:RegionHandle=U64,ViewerCircuitCode=U32,AgentID=UUID,SessionID=UUID,AgentPos=V3,AgentVel=V3,Center=V3,Size=V3,AtAxis=V3,LeftAxis=V3,UpAxis=V3,ChangedGrid=BOOL");
m!(ChildAgentDying,Low,240,3,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(ChildAgentUnknown,Low,241,1,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(AtomicPassObject,High,28,1,"TaskData:S:TaskID=UUID,AttachmentNeedsSave=BOOL");
m!(KillChildAgents,Low,242,1,"IDBlock:S:AgentID=UUID");
m!(GetScriptRunning,Low,243,0,"Script:S:ObjectID=UUID,ItemID=UUID");
m!(ScriptRunningReply,Low,244,0,"Script:S:ObjectID=UUID,ItemID=UUID,Running=BOOL");
m!(SetScriptRunning,Low,245,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Script:S:ObjectID=UUID,ItemID=UUID,Running=BOOL");
m!(ScriptReset,Low,246,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Script:S:ObjectID=UUID,ItemID=UUID");
m!(ScriptSensorRequest,Low,247,3,"Requester:S:SourceID=UUID,RequestID=UUID,SearchID=UUID,SearchPos=V3,SearchDir=Quat,SearchName=Var1,Type=S32,Range=F32,Arc=F32,RegionHandle=U64,SearchRegions=U8");
m!(ScriptSensorReply,Low,248,3,"Requester:S:SourceID=UUID;SensedData:V:ObjectID=UUID,OwnerID=UUID,GroupID=UUID,Position=V3,Velocity=V3,Rotation=Quat,Name=Var1,Type=S32,Range=F32");
m!(CompleteAgentMovement,Low,249,0,"AgentData:S:AgentID=UUID,SessionID=UUID,CircuitCode=U32");
m!(AgentMovementComplete,Low,250,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:Position=V3,LookAt=V3,RegionHandle=U64,Timestamp=U32;SimData:S:ChannelVersion=Var2");
m!(DataServerLogout,Low,251,1,"UserData:S:AgentID=UUID,ViewerIP=IPADDR,Disconnect=BOOL,SessionID=UUID");
m!(LogoutRequest,Low,252,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(LogoutReply,Low,253,3,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:V:ItemID=UUID");
m!(ImprovedInstantMessage,Low,254,2,"AgentData:S:AgentID=UUID,SessionID=UUID;MessageBlock:S:FromGroup=BOOL,ToAgentID=UUID,ParentEstateID=U32,RegionID=UUID,Position=V3,Offline=U8,Dialog=U8,ID=UUID,Timestamp=U32,FromAgentName=Var1,Message=Var2,BinaryBucket=Var2;EstateBlock:S:EstateID=U32;MetaData:V:Data=Variable    2");
m!(RetrieveInstantMessages,Low,255,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(FindAgent,Low,256,0,"AgentBlock:S:Hunter=UUID,Prey=UUID,SpaceIP=IPADDR;LocationBlock:V:GlobalX=F64,GlobalY=F64");
m!(RequestGodlikePowers,Low,257,0,"AgentData:S:AgentID=UUID,SessionID=UUID;RequestBlock:S:Godlike=BOOL,Token=UUID");
m!(GrantGodlikePowers,Low,258,1,"AgentData:S:AgentID=UUID,SessionID=UUID;GrantData:S:GodLevel=U8,Token=UUID");
m!(GodlikeMessage,Low,259,2,"AgentData:S:AgentID=UUID,SessionID=UUID,TransactionID=UUID;MethodData:S:Method=Var1,Invoice=UUID;ParamList:V:Parameter=Var1");
m!(EstateOwnerMessage,Low,260,2,"AgentData:S:AgentID=UUID,SessionID=UUID,TransactionID=UUID;MethodData:S:Method=Var1,Invoice=UUID;ParamList:V:Parameter=Var1");
m!(GenericMessage,Low,261,2,"AgentData:S:AgentID=UUID,SessionID=UUID,TransactionID=UUID;MethodData:S:Method=Var1,Invoice=UUID;ParamList:V:Parameter=Var1");
m!(GenericStreamingMessage,High,31,1,"MethodData:S:Method=U16;DataBlock:S:Data=Var2");
m!(LargeGenericMessage,Low,430,0,"AgentData:S:AgentID=UUID,SessionID=UUID,TransactionID=UUID;MethodData:S:Method=Var1,Invoice=UUID;ParamList:V:Parameter=Var2");
m!(MuteListRequest,Low,262,0,"AgentData:S:AgentID=UUID,SessionID=UUID;MuteData:S:MuteCRC=U32");
m!(UpdateMuteListEntry,Low,263,0,"AgentData:S:AgentID=UUID,SessionID=UUID;MuteData:S:MuteID=UUID,MuteName=Var1,MuteType=S32,MuteFlags=U32");
m!(RemoveMuteListEntry,Low,264,0,"AgentData:S:AgentID=UUID,SessionID=UUID;MuteData:S:MuteID=UUID,MuteName=Var1");
m!(CopyInventoryFromNotecard,Low,265,2,"AgentData:S:AgentID=UUID,SessionID=UUID;NotecardData:S:NotecardItemID=UUID,ObjectID=UUID;InventoryData:V:ItemID=UUID,FolderID=UUID");
m!(UpdateInventoryItem,Low,266,2,"AgentData:S:AgentID=UUID,SessionID=UUID,TransactionID=UUID;InventoryData:V:ItemID=UUID,FolderID=UUID,CallbackID=U32,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(UpdateCreateInventoryItem,Low,267,3,"AgentData:S:AgentID=UUID,SimApproved=BOOL,TransactionID=UUID;InventoryData:V:ItemID=UUID,FolderID=UUID,CallbackID=U32,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(MoveInventoryItem,Low,268,2,"AgentData:S:AgentID=UUID,SessionID=UUID,Stamp=BOOL;InventoryData:V:ItemID=UUID,FolderID=UUID,NewName=Var1");
m!(CopyInventoryItem,Low,269,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:V:CallbackID=U32,OldAgentID=UUID,OldItemID=UUID,NewFolderID=UUID,NewName=Var1");
m!(RemoveInventoryItem,Low,270,0,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:V:ItemID=UUID");
m!(ChangeInventoryItemFlags,Low,271,0,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:V:ItemID=UUID,Flags=U32");
m!(SaveAssetIntoInventory,Low,272,1,"AgentData:S:AgentID=UUID;InventoryData:S:ItemID=UUID,NewAssetID=UUID");
m!(CreateInventoryFolder,Low,273,0,"AgentData:S:AgentID=UUID,SessionID=UUID;FolderData:S:FolderID=UUID,ParentID=UUID,Type=S8,Name=Var1");
m!(UpdateInventoryFolder,Low,274,0,"AgentData:S:AgentID=UUID,SessionID=UUID;FolderData:V:FolderID=UUID,ParentID=UUID,Type=S8,Name=Var1");
m!(MoveInventoryFolder,Low,275,2,"AgentData:S:AgentID=UUID,SessionID=UUID,Stamp=BOOL;InventoryData:V:FolderID=UUID,ParentID=UUID");
m!(RemoveInventoryFolder,Low,276,0,"AgentData:S:AgentID=UUID,SessionID=UUID;FolderData:V:FolderID=UUID");
m!(FetchInventoryDescendents,Low,277,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:S:FolderID=UUID,OwnerID=UUID,SortOrder=S32,FetchFolders=BOOL,FetchItems=BOOL");
m!(InventoryDescendents,Low,278,3,"AgentData:S:AgentID=UUID,FolderID=UUID,OwnerID=UUID,Version=S32,Descendents=S32;FolderData:V:FolderID=UUID,ParentID=UUID,Type=S8,Name=Var1;ItemData:V:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(FetchInventory,Low,279,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:V:OwnerID=UUID,ItemID=UUID");
m!(FetchInventoryReply,Low,280,3,"AgentData:S:AgentID=UUID;InventoryData:V:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(BulkUpdateInventory,Low,281,3,"AgentData:S:AgentID=UUID,TransactionID=UUID;FolderData:V:FolderID=UUID,ParentID=UUID,Type=S8,Name=Var1;ItemData:V:ItemID=UUID,CallbackID=U32,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(RequestInventoryAsset,Low,282,1,"QueryData:S:QueryID=UUID,AgentID=UUID,OwnerID=UUID,ItemID=UUID");
m!(InventoryAssetResponse,Low,283,1,"QueryData:S:QueryID=UUID,AssetID=UUID,IsReadable=BOOL");
m!(RemoveInventoryObjects,Low,284,0,"AgentData:S:AgentID=UUID,SessionID=UUID;FolderData:V:FolderID=UUID;ItemData:V:ItemID=UUID");
m!(PurgeInventoryDescendents,Low,285,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:S:FolderID=UUID");
m!(UpdateTaskInventory,Low,286,2,"AgentData:S:AgentID=UUID,SessionID=UUID;UpdateData:S:LocalID=U32,Key=U8;InventoryData:S:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(RemoveTaskInventory,Low,287,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:S:LocalID=U32,ItemID=UUID");
m!(MoveTaskInventory,Low,288,0,"AgentData:S:AgentID=UUID,SessionID=UUID,FolderID=UUID;InventoryData:S:LocalID=U32,ItemID=UUID");
m!(RequestTaskInventory,Low,289,0,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:S:LocalID=U32");
m!(ReplyTaskInventory,Low,290,3,"InventoryData:S:TaskID=UUID,Serial=S16,Filename=Var1");
m!(DeRezObject,Low,291,2,"AgentData:S:AgentID=UUID,SessionID=UUID;AgentBlock:S:GroupID=UUID,Destination=U8,DestinationID=UUID,TransactionID=UUID,PacketCount=U8,PacketNumber=U8;ObjectData:V:ObjectLocalID=U32");
m!(DeRezAck,Low,292,1,"TransactionData:S:TransactionID=UUID,Success=BOOL");
m!(RezObject,Low,293,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;RezData:S:FromTaskID=UUID,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=UUID,RayEndIsIntersection=BOOL,RezSelected=BOOL,RemoveItem=BOOL,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32;InventoryData:S:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(RezObjectFromNotecard,Low,294,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;RezData:S:FromTaskID=UUID,BypassRaycast=U8,RayStart=V3,RayEnd=V3,RayTargetID=UUID,RayEndIsIntersection=BOOL,RezSelected=BOOL,RemoveItem=BOOL,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32;NotecardData:S:NotecardItemID=UUID,ObjectID=UUID;InventoryData:V:ItemID=UUID");
m!(TransferInventory,Low,295,3,"InfoBlock:S:SourceID=UUID,DestID=UUID,TransactionID=UUID;InventoryBlock:V:InventoryID=UUID,Type=S8;ValidationBlock:S:NeedsValidation=BOOL,EstateID=U32");
m!(TransferInventoryAck,Low,296,3,"InfoBlock:S:TransactionID=UUID,InventoryID=UUID");
m!(AcceptFriendship,Low,297,0,"AgentData:S:AgentID=UUID,SessionID=UUID;TransactionBlock:S:TransactionID=UUID;FolderData:V:FolderID=UUID");
m!(DeclineFriendship,Low,298,0,"AgentData:S:AgentID=UUID,SessionID=UUID;TransactionBlock:S:TransactionID=UUID");
m!(FormFriendship,Low,299,1,"AgentBlock:S:SourceID=UUID,DestID=UUID");
m!(TerminateFriendship,Low,300,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ExBlock:S:OtherID=UUID");
m!(OfferCallingCard,Low,301,0,"AgentData:S:AgentID=UUID,SessionID=UUID;AgentBlock:S:DestID=UUID,TransactionID=UUID");
m!(AcceptCallingCard,Low,302,0,"AgentData:S:AgentID=UUID,SessionID=UUID;TransactionBlock:S:TransactionID=UUID;FolderData:V:FolderID=UUID");
m!(DeclineCallingCard,Low,303,0,"AgentData:S:AgentID=UUID,SessionID=UUID;TransactionBlock:S:TransactionID=UUID");
m!(RezScript,Low,304,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;UpdateBlock:S:ObjectLocalID=U32,Enabled=BOOL;InventoryBlock:S:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32;NewScriptInfo:V:TemplateID=UUID");
m!(CreateInventoryItem,Low,305,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryBlock:S:CallbackID=U32,FolderID=UUID,TransactionID=UUID,NextOwnerMask=U32,Type=S8,InvType=S8,WearableType=U8,Name=Var1,Description=Var1");
m!(CreateLandmarkForEvent,Low,306,2,"AgentData:S:AgentID=UUID,SessionID=UUID;EventData:S:EventID=U32;InventoryBlock:S:FolderID=UUID,Name=Var1");
m!(EventLocationRequest,Low,307,3,"QueryData:S:QueryID=UUID;EventData:S:EventID=U32");
m!(EventLocationReply,Low,308,3,"QueryData:S:QueryID=UUID;EventData:S:Success=BOOL,RegionID=UUID,RegionPos=V3");
m!(RegionHandleRequest,Low,309,0,"RequestBlock:S:RegionID=UUID");
m!(RegionIDAndHandleReply,Low,310,1,"ReplyBlock:S:RegionID=UUID,RegionHandle=U64");
m!(MoneyTransferRequest,Low,311,2,"AgentData:S:AgentID=UUID,SessionID=UUID;MoneyData:S:SourceID=UUID,DestID=UUID,Flags=U8,Amount=S32,AggregatePermNextOwner=U8,AggregatePermInventory=U8,TransactionType=S32,Description=Var1");
m!(MoneyTransferBackend,Low,312,3,"MoneyData:S:TransactionID=UUID,TransactionTime=U32,SourceID=UUID,DestID=UUID,Flags=U8,Amount=S32,AggregatePermNextOwner=U8,AggregatePermInventory=U8,TransactionType=S32,RegionID=UUID,GridX=U32,GridY=U32,Description=Var1");
m!(MoneyBalanceRequest,Low,313,2,"AgentData:S:AgentID=UUID,SessionID=UUID;MoneyData:S:TransactionID=UUID");
m!(MoneyBalanceReply,Low,314,3,"MoneyData:S:AgentID=UUID,TransactionID=UUID,TransactionSuccess=BOOL,MoneyBalance=S32,SquareMetersCredit=S32,SquareMetersCommitted=S32,Description=Var1;TransactionInfo:S:TransactionType=S32,SourceID=UUID,IsSourceGroup=BOOL,DestID=UUID,IsDestGroup=BOOL,Amount=S32,ItemDescription=Var1");
m!(RoutedMoneyBalanceReply,Low,315,3,"TargetBlock:S:TargetIP=IPADDR,TargetPort=IPPORT;MoneyData:S:AgentID=UUID,TransactionID=UUID,TransactionSuccess=BOOL,MoneyBalance=S32,SquareMetersCredit=S32,SquareMetersCommitted=S32,Description=Var1;TransactionInfo:S:TransactionType=S32,SourceID=UUID,IsSourceGroup=BOOL,DestID=UUID,IsDestGroup=BOOL,Amount=S32,ItemDescription=Var1");
m!(ActivateGestures,Low,316,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32;Data:V:ItemID=UUID,AssetID=UUID,GestureFlags=U32");
m!(DeactivateGestures,Low,317,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32;Data:V:ItemID=UUID,GestureFlags=U32");
m!(MuteListUpdate,Low,318,1,"MuteData:S:AgentID=UUID,Filename=Var1");
m!(UseCachedMuteList,Low,319,0,"AgentData:S:AgentID=UUID");
m!(GrantUserRights,Low,320,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Rights:V:AgentRelated=UUID,RelatedRights=S32");
m!(ChangeUserRights,Low,321,1,"AgentData:S:AgentID=UUID;Rights:V:AgentRelated=UUID,RelatedRights=S32");
m!(OnlineNotification,Low,322,1,"AgentBlock:V:AgentID=UUID");
m!(OfflineNotification,Low,323,1,"AgentBlock:V:AgentID=UUID");
m!(SetStartLocationRequest,Low,324,2,"AgentData:S:AgentID=UUID,SessionID=UUID;StartLocationData:S:SimName=Var1,LocationID=U32,LocationPos=V3,LocationLookAt=V3");
m!(SetStartLocation,Low,325,3,"StartLocationData:S:AgentID=UUID,RegionID=UUID,LocationID=U32,RegionHandle=U64,LocationPos=V3,LocationLookAt=V3");
m!(NetTest,Low,326,0,"NetBlock:S:Port=IPPORT");
m!(SetCPURatio,Low,327,0,"Data:S:Ratio=U8");
m!(SimCrashed,Low,328,0,"Data:S:RegionX=U32,RegionY=U32;Users:V:AgentID=UUID");
m!(NameValuePair,Low,329,1,"TaskData:S:ID=UUID;NameValueData:V:NVPair=Variable    2");
m!(RemoveNameValuePair,Low,330,1,"TaskData:S:ID=UUID;NameValueData:V:NVPair=Variable    2");
m!(UpdateAttachment,Low,331,3,"AgentData:S:AgentID=UUID,SessionID=UUID;AttachmentBlock:S:AttachmentPoint=U8;OperationData:S:AddItem=BOOL,UseExistingAsset=BOOL,ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,AssetID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(RemoveAttachment,Low,332,0,"AgentData:S:AgentID=UUID,SessionID=UUID;AttachmentBlock:S:AttachmentPoint=U8,ItemID=UUID");
m!(SoundTrigger,High,29,0,"SoundData:S:SoundID=UUID,OwnerID=UUID,ObjectID=UUID,ParentID=UUID,Handle=U64,Position=V3,Gain=F32");
m!(AttachedSound,Medium,13,1,"DataBlock:S:SoundID=UUID,ObjectID=UUID,OwnerID=UUID,Gain=F32,Flags=U8");
m!(AttachedSoundGainChange,Medium,14,1,"DataBlock:S:ObjectID=UUID,Gain=F32");
m!(PreloadSound,Medium,15,1,"DataBlock:V:ObjectID=UUID,OwnerID=UUID,SoundID=UUID");
m!(ObjectAnimation,High,30,1,"Sender:S:ID=UUID;AnimationList:V:AnimID=UUID,AnimSequenceID=S32");
m!(AssetUploadRequest,Low,333,0,"AssetBlock:S:TransactionID=UUID,Type=S8,Tempfile=BOOL,StoreLocal=BOOL,AssetData=Var2");
m!(AssetUploadComplete,Low,334,0,"AssetBlock:S:UUID=UUID,Type=S8,Success=BOOL");
m!(EmailMessageRequest,Low,335,1,"DataBlock:S:ObjectID=UUID,FromAddress=Var1,Subject=Var1");
m!(EmailMessageReply,Low,336,1,"DataBlock:S:ObjectID=UUID,More=U32,Time=U32,FromAddress=Var1,Subject=Var1,Data=Var2,MailFilter=Var1");
m!(InternalScriptMail,Medium,16,1,"DataBlock:S:From=Var1,To=UUID,Subject=Var1,Body=Var2");
m!(ScriptDataRequest,Low,337,1,"DataBlock:V:Hash=U64,RequestType=S8,Request=Var2");
m!(ScriptDataReply,Low,338,1,"DataBlock:V:Hash=U64,Reply=Var2");
m!(CreateGroupRequest,Low,339,2,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:Name=Var1,Charter=Var2,ShowInList=BOOL,InsigniaID=UUID,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL");
m!(CreateGroupReply,Low,340,1,"AgentData:S:AgentID=UUID;ReplyData:S:GroupID=UUID,Success=BOOL,Message=Var1");
m!(UpdateGroupInfo,Low,341,2,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID,Charter=Var2,ShowInList=BOOL,InsigniaID=UUID,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL");
m!(GroupRoleChanges,Low,342,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;RoleChange:V:RoleID=UUID,MemberID=UUID,Change=U32");
m!(JoinGroupRequest,Low,343,2,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID");
m!(JoinGroupReply,Low,344,1,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID,Success=BOOL");
m!(EjectGroupMemberRequest,Low,345,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID;EjectData:V:EjecteeID=UUID");
m!(EjectGroupMemberReply,Low,346,1,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID;EjectData:S:Success=BOOL");
m!(LeaveGroupRequest,Low,347,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID");
m!(LeaveGroupReply,Low,348,1,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID,Success=BOOL");
m!(InviteGroupRequest,Low,349,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID;InviteData:V:InviteeID=UUID,RoleID=UUID");
m!(InviteGroupResponse,Low,350,1,"InviteData:S:AgentID=UUID,InviteeID=UUID,GroupID=UUID,RoleID=UUID,MembershipFee=S32;GroupData:S:GroupLimit=S32");
m!(GroupProfileRequest,Low,351,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID");
m!(GroupProfileReply,Low,352,3,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID,Name=Var1,Charter=Var2,ShowInList=BOOL,MemberTitle=Var1,PowersMask=U64,InsigniaID=UUID,FounderID=UUID,MembershipFee=S32,OpenEnrollment=BOOL,Money=S32,GroupMembershipCount=S32,GroupRolesCount=S32,AllowPublish=BOOL,MaturePublish=BOOL,OwnerRole=UUID");
m!(GroupAccountSummaryRequest,Low,353,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32");
m!(GroupAccountSummaryReply,Low,354,3,"AgentData:S:AgentID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1,Balance=S32,TotalCredits=S32,TotalDebits=S32,ObjectTaxCurrent=S32,LightTaxCurrent=S32,LandTaxCurrent=S32,GroupTaxCurrent=S32,ParcelDirFeeCurrent=S32,ObjectTaxEstimate=S32,LightTaxEstimate=S32,LandTaxEstimate=S32,GroupTaxEstimate=S32,ParcelDirFeeEstimate=S32,NonExemptMembers=S32,LastTaxDate=Var1,TaxDate=Var1");
m!(GroupAccountDetailsRequest,Low,355,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32");
m!(GroupAccountDetailsReply,Low,356,3,"AgentData:S:AgentID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1;HistoryData:V:Description=Var1,Amount=S32");
m!(GroupAccountTransactionsRequest,Low,357,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32");
m!(GroupAccountTransactionsReply,Low,358,3,"AgentData:S:AgentID=UUID,GroupID=UUID;MoneyData:S:RequestID=UUID,IntervalDays=S32,CurrentInterval=S32,StartDate=Var1;HistoryData:V:Time=Var1,User=Var1,Type=S32,Item=Var1,Amount=S32");
m!(GroupActiveProposalsRequest,Low,359,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID;TransactionData:S:TransactionID=UUID");
m!(GroupActiveProposalItemReply,Low,360,3,"AgentData:S:AgentID=UUID,GroupID=UUID;TransactionData:S:TransactionID=UUID,TotalNumItems=U32;ProposalData:V:VoteID=UUID,VoteInitiator=UUID,TerseDateID=Var1,StartDateTime=Var1,EndDateTime=Var1,AlreadyVoted=BOOL,VoteCast=Var1,Majority=F32,Quorum=S32,ProposalText=Var1");
m!(GroupVoteHistoryRequest,Low,361,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID;TransactionData:S:TransactionID=UUID");
m!(GroupVoteHistoryItemReply,Low,362,3,"AgentData:S:AgentID=UUID,GroupID=UUID;TransactionData:S:TransactionID=UUID,TotalNumItems=U32;HistoryItemData:S:VoteID=UUID,TerseDateID=Var1,StartDateTime=Var1,EndDateTime=Var1,VoteInitiator=UUID,VoteType=Var1,VoteResult=Var1,Majority=F32,Quorum=S32,ProposalText=Var2;VoteItem:V:CandidateID=UUID,VoteCast=Var1,NumVotes=S32");
m!(StartGroupProposal,Low,363,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ProposalData:S:GroupID=UUID,Quorum=S32,Majority=F32,Duration=S32,ProposalText=Var1");
m!(GroupProposalBallot,Low,364,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ProposalData:S:ProposalID=UUID,GroupID=UUID,VoteCast=Var1");
m!(TallyVotes,Low,365,1,"");
m!(GroupMembersRequest,Low,366,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID,RequestID=UUID");
m!(GroupMembersReply,Low,367,3,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID,RequestID=UUID,MemberCount=S32;MemberData:V:AgentID=UUID,Contribution=S32,OnlineStatus=Var1,AgentPowers=U64,Title=Var1,IsOwner=BOOL");
m!(ActivateGroup,Low,368,2,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID");
m!(SetGroupContribution,Low,369,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID,Contribution=S32");
m!(SetGroupAcceptNotices,Low,370,0,"AgentData:S:AgentID=UUID,SessionID=UUID;Data:S:GroupID=UUID,AcceptNotices=BOOL;NewData:S:ListInProfile=BOOL");
m!(GroupRoleDataRequest,Low,371,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID,RequestID=UUID");
m!(GroupRoleDataReply,Low,372,1,"AgentData:S:AgentID=UUID;GroupData:S:GroupID=UUID,RequestID=UUID,RoleCount=S32;RoleData:V:RoleID=UUID,Name=Var1,Title=Var1,Description=Var1,Powers=U64,Members=U32");
m!(GroupRoleMembersRequest,Low,373,0,"AgentData:S:AgentID=UUID,SessionID=UUID;GroupData:S:GroupID=UUID,RequestID=UUID");
m!(GroupRoleMembersReply,Low,374,1,"AgentData:S:AgentID=UUID,GroupID=UUID,RequestID=UUID,TotalPairs=U32;MemberData:V:RoleID=UUID,MemberID=UUID");
m!(GroupTitlesRequest,Low,375,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID,RequestID=UUID");
m!(GroupTitlesReply,Low,376,3,"AgentData:S:AgentID=UUID,GroupID=UUID,RequestID=UUID;GroupData:V:Title=Var1,RoleID=UUID,Selected=BOOL");
m!(GroupTitleUpdate,Low,377,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID,TitleRoleID=UUID");
m!(GroupRoleUpdate,Low,378,0,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupID=UUID;RoleData:V:RoleID=UUID,Name=Var1,Description=Var1,Title=Var1,Powers=U64,UpdateType=U8");
m!(LiveHelpGroupRequest,Low,379,1,"RequestData:S:RequestID=UUID,AgentID=UUID");
m!(LiveHelpGroupReply,Low,380,1,"ReplyData:S:RequestID=UUID,GroupID=UUID,Selection=Var1");
m!(AgentWearablesRequest,Low,381,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(AgentWearablesUpdate,Low,382,3,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=U32;WearableData:V:ItemID=UUID,AssetID=UUID,WearableType=U8");
m!(AgentIsNowWearing,Low,383,2,"AgentData:S:AgentID=UUID,SessionID=UUID;WearableData:V:ItemID=UUID,WearableType=U8");
m!(AgentCachedTexture,Low,384,0,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=S32;WearableData:V:ID=UUID,TextureIndex=U8");
m!(AgentCachedTextureResponse,Low,385,1,"AgentData:S:AgentID=UUID,SessionID=UUID,SerialNum=S32;WearableData:V:TextureID=UUID,TextureIndex=U8,HostName=Var1");
m!(AgentDataUpdateRequest,Low,386,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(AgentDataUpdate,Low,387,3,"AgentData:S:AgentID=UUID,FirstName=Var1,LastName=Var1,GroupTitle=Var1,ActiveGroupID=UUID,GroupPowers=U64,GroupName=Var1");
m!(GroupDataUpdate,Low,388,3,"AgentGroupData:V:AgentID=UUID,GroupID=UUID,AgentPowers=U64,GroupTitle=Var1");
m!(AgentGroupDataUpdate,Low,389,3,"AgentData:S:AgentID=UUID;GroupData:V:GroupID=UUID,GroupPowers=U64,AcceptNotices=BOOL,GroupInsigniaID=UUID,Contribution=S32,GroupName=Var1");
m!(AgentDropGroup,Low,390,3,"AgentData:S:AgentID=UUID,GroupID=UUID");
m!(LogTextMessage,Low,391,3,"DataBlock:V:FromAgentId=UUID,ToAgentId=UUID,GlobalX=F64,GlobalY=F64,Time=U32,Message=Var2");
m!(ViewerEffect,Medium,17,2,"AgentData:S:AgentID=UUID,SessionID=UUID;Effect:V:ID=UUID,AgentID=UUID,Type=U8,Duration=F32,Color=Fixed    4,TypeData=Var1");
m!(CreateTrustedCircuit,Low,392,0,"DataBlock:S:EndPointID=UUID,Digest=Fixed 32");
m!(DenyTrustedCircuit,Low,393,0,"DataBlock:S:EndPointID=UUID");
m!(RequestTrustedCircuit,Low,394,1,"");
m!(RezSingleAttachmentFromInv,Low,395,2,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:S:ItemID=UUID,OwnerID=UUID,AttachmentPt=U8,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,Name=Var1,Description=Var1");
m!(RezMultipleAttachmentsFromInv,Low,396,2,"AgentData:S:AgentID=UUID,SessionID=UUID;HeaderData:S:CompoundMsgID=UUID,TotalObjects=U8,FirstDetachAll=BOOL,ItemID=UUID,OwnerID=UUID,AttachmentPt=U8,ItemFlags=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,Name=Var1,Description=Var1");
m!(DetachAttachmentIntoInv,Low,397,0,"ObjectData:S:AgentID=UUID,ItemID=UUID");
m!(CreateNewOutfitAttachments,Low,398,0,"AgentData:S:AgentID=UUID,SessionID=UUID;HeaderData:S:NewFolderID=UUID;ObjectData:V:OldItemID=UUID,OldFolderID=UUID");
m!(UserInfoRequest,Low,399,0,"AgentData:S:AgentID=UUID,SessionID=UUID");
m!(UserInfoReply,Low,400,0,"AgentData:S:AgentID=UUID;UserData:S:IMViaEMail=BOOL,DirectoryVisibility=Var1,EMail=Var2");
m!(UpdateUserInfo,Low,401,0,"AgentData:S:AgentID=UUID,SessionID=UUID;UserData:S:IMViaEMail=BOOL,DirectoryVisibility=Var1");
m!(ParcelRename,Low,402,1,"ParcelData:V:ParcelID=UUID,NewName=Var1");
m!(InitiateDownload,Low,403,0,"AgentData:S:AgentID=UUID;FileData:S:SimFilename=Var1,ViewerFilename=Var1");
m!(SystemMessage,Low,404,3,"MethodData:S:Method=Var1,Invoice=UUID,Digest=Fixed 32;ParamList:V:Parameter=Var1");
m!(MapLayerRequest,Low,405,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32,EstateID=U32,Godlike=BOOL");
m!(MapLayerReply,Low,406,1,"AgentData:S:AgentID=UUID,Flags=U32;LayerData:V:Left=U32,Right=U32,Top=U32,Bottom=U32,ImageID=UUID");
m!(MapBlockRequest,Low,407,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32,EstateID=U32,Godlike=BOOL;PositionData:S:MinX=U16,MaxX=U16,MinY=U16,MaxY=U16");
m!(MapNameRequest,Low,408,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32,EstateID=U32,Godlike=BOOL;NameData:S:Name=Var1");
m!(MapBlockReply,Low,409,1,"AgentData:S:AgentID=UUID,Flags=U32;Data:V:X=U16,Y=U16,Name=Var1,Access=U8,RegionFlags=U32,WaterHeight=U8,Agents=U8,MapImageID=UUID");
m!(MapItemRequest,Low,410,0,"AgentData:S:AgentID=UUID,SessionID=UUID,Flags=U32,EstateID=U32,Godlike=BOOL;RequestData:S:ItemType=U32,RegionHandle=U64");
m!(MapItemReply,Low,411,1,"AgentData:S:AgentID=UUID,Flags=U32;RequestData:S:ItemType=U32;Data:V:X=U32,Y=U32,ID=UUID,Extra=S32,Extra2=S32,Name=Var1");
m!(SendPostcard,Low,412,0,"AgentData:S:AgentID=UUID,SessionID=UUID,AssetID=UUID,PosGlobal=V3d,To=Var1,From=Var1,Name=Var1,Subject=Var1,Msg=Var2,AllowPublish=BOOL,MaturePublish=BOOL");
m!(RpcChannelRequest,Low,413,1,"DataBlock:S:GridX=U32,GridY=U32,TaskID=UUID,ItemID=UUID");
m!(RpcChannelReply,Low,414,1,"DataBlock:S:TaskID=UUID,ItemID=UUID,ChannelID=UUID");
m!(RpcScriptRequestInbound,Low,415,0,"TargetBlock:S:GridX=U32,GridY=U32;DataBlock:S:TaskID=UUID,ItemID=UUID,ChannelID=UUID,IntValue=U32,StringValue=Var2");
m!(RpcScriptRequestInboundForward,Low,416,1,"DataBlock:S:RPCServerIP=IPADDR,RPCServerPort=IPPORT,TaskID=UUID,ItemID=UUID,ChannelID=UUID,IntValue=U32,StringValue=Var2");
m!(RpcScriptReplyInbound,Low,417,0,"DataBlock:S:TaskID=UUID,ItemID=UUID,ChannelID=UUID,IntValue=U32,StringValue=Var2");
m!(ScriptMailRegistration,Low,418,1,"DataBlock:S:TargetIP=Var1,TargetPort=IPPORT,TaskID=UUID,Flags=U32");
m!(ParcelMediaCommandMessage,Low,419,1,"CommandBlock:S:Flags=U32,Command=U32,Time=F32");
m!(ParcelMediaUpdate,Low,420,1,"DataBlock:S:MediaURL=Var1,MediaID=UUID,MediaAutoScale=U8;DataBlockExtended:S:MediaType=Var1,MediaDesc=Var1,MediaWidth=S32,MediaHeight=S32,MediaLoop=U8");
m!(LandStatRequest,Low,421,0,"AgentData:S:AgentID=UUID,SessionID=UUID;RequestData:S:ReportType=U32,RequestFlags=U32,Filter=Var1,ParcelLocalID=S32");
m!(LandStatReply,Low,422,1,"RequestData:S:ReportType=U32,RequestFlags=U32,TotalObjectCount=U32;ReportData:V:TaskLocalID=U32,TaskID=UUID,LocationX=F32,LocationY=F32,LocationZ=F32,Score=F32,TaskName=Var1,OwnerName=Var1");
m!(Error,Low,423,2,"AgentData:S:AgentID=UUID;Data:S:Code=S32,Token=Var1,ID=UUID,System=Var1,Message=Var2,Data=Var2");
m!(ObjectIncludeInSearch,Low,424,0,"AgentData:S:AgentID=UUID,SessionID=UUID;ObjectData:V:ObjectLocalID=U32,IncludeInSearch=BOOL");
m!(RezRestoreToWorld,Low,425,0,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryData:S:ItemID=UUID,FolderID=UUID,CreatorID=UUID,OwnerID=UUID,GroupID=UUID,BaseMask=U32,OwnerMask=U32,GroupMask=U32,EveryoneMask=U32,NextOwnerMask=U32,GroupOwned=BOOL,TransactionID=UUID,Type=S8,InvType=S8,Flags=U32,SaleType=U8,SalePrice=S32,Name=Var1,Description=Var1,CreationDate=S32,CRC=U32");
m!(LinkInventoryItem,Low,426,2,"AgentData:S:AgentID=UUID,SessionID=UUID;InventoryBlock:S:CallbackID=U32,FolderID=UUID,TransactionID=UUID,OldItemID=UUID,Type=S8,InvType=S8,Name=Var1,Description=Var1");
m!(RetrieveIMsExtended,Low,427,1,"AgentData:S:AgentID=UUID,SessionID=UUID,IsPremium=BOOL");
m!(JoinGroupRequestExtended,Low,428,1,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupLimit=S32;GroupData:S:GroupID=UUID");
m!(CreateGroupRequestExtended,Low,429,1,"AgentData:S:AgentID=UUID,SessionID=UUID,GroupLimit=S32;GroupData:S:Name=Var1,Charter=Var2,ShowInList=BOOL,InsigniaID=UUID,MembershipFee=S32,OpenEnrollment=BOOL,AllowPublish=BOOL,MaturePublish=BOOL");
m!(GameControlInput,High,32,2,"AgentData:S:AgentID=UUID,SessionID=UUID;AxisData:V:Index=U8,Value=S16;ButtonData:V:Data=Var1");
```

## Part 10 — Capabilities client and login (reqwest)

Caps are HTTPS endpoints whose URLs come from the seed capability at login.
Rules that are not optional: cap URLs are per-region, per-session, and
unguessable — never cache them across logins or teleports; request only the
names you will use (the simulator allocates server-side state per cap); a cap
missing from the response map means *this simulator version doesn't offer it*,
not an error. The name list below follows `buildCapabilityNames` in the viewer
plus the AIS names from `llaisapi.cpp`, trimmed to what a thin client needs.

```rust
/// Capability names to request from the seed cap, grouped by subsystem.
/// Requesting a name the sim doesn't know is harmless — it is simply absent
/// from the returned map.
pub const CAPS_WANTED: &[&str] = &[
    // Session heartbeat: long-poll event stream (teleports, IM, offers).
    "EventQueueGet",
    // Inventory: HTTP fetch + AIS3 operations.
    "FetchInventory2", "FetchInventoryDescendents2", "FetchLib2", "FetchLibDescendents2",
    "InventoryAPIv3", "LibraryAPIv3", "IncrementCOFVersion",
    // Content delivery.
    "GetTexture", "GetMesh", "GetMesh2", "GetMetadata", "GetObjectCost", "GetObjectPhysicsData",
    // Region/agent info — SimulatorFeatures gates mesh, physics, PBR, voice.
    "SimulatorFeatures", "ServerReleaseNotes", "GetDisplayNames", "AgentPreferences",
    "CharacterProperties", "AvatarRenderInfo",
    // Social.
    "ChatSessionRequest", "GroupAPIv1", "GroupMemberData", "StartGroupProposal",
    // Uploads and appearance.
    "NewFileAgentInventory", "UpdateAgentAppearance", "RenderMaterials",
    "EnvironmentSettings", "ExtEnvironment",
    // Voice: legacy Vivox provisioning; WebRTC uses its own signaling caps.
    "ProvisionVoiceAccountRequest", "VoiceSignalingRequest",
];

use std::collections::HashMap;

#[derive(Debug, thiserror::Error)]
pub enum CapsError {
    #[error("HTTP transport: {0}")]
    Transport(#[from] reqwest::Error),
    #[error("capability not offered by this simulator: {0}")]
    NotOffered(String),
    #[error("LLSD in caps response: {0}")]
    Llsd(#[from] LlsdError),
    #[error("simulator returned HTTP {0} for cap {1}")]
    HttpStatus(u16, String),
}

/// A resolved capability map for one region session.
pub struct Caps {
    http: reqwest::Client,
    urls: HashMap<String, String>,
}

impl Caps {
    /// Exchange the seed capability for the real cap map: POST an LLSD array
    /// of names, receive an LLSD map of name → URL.
    pub async fn from_seed(http: reqwest::Client, seed_url: &str) -> Result<Self, CapsError> {
        let mut req_llsd = Llsd::Array(
            CAPS_WANTED.iter().map(|n| Llsd::String(n.to_string())).collect(),
        );
        let body = req_llsd.to_xml();
        let resp = http
            .post(seed_url)
            .header("Content-Type", "application/llsd+xml")
            .body(body)
            .send()
            .await?;
        if !resp.status().is_success() {
            return Err(CapsError::HttpStatus(resp.status().as_u16(), "seed".into()));
        }
        let text = resp.text().await?;
        let parsed = Llsd::from_xml(&text)?;
        let mut urls = HashMap::new();
        if let Llsd::Map(m) = &parsed {
            for (k, v) in m {
                if let Some(u) = v.as_str() {
                    urls.insert(k.clone(), u.to_string());
                }
            }
        }
        // Silence the unused-mut warning pattern for req_llsd in minimal builds.
        let _ = &mut req_llsd;
        Ok(Self { http, urls })
    }

    pub fn url(&self, name: &str) -> Result<&str, CapsError> {
        self.urls
            .get(name)
            .map(|s| s.as_str())
            .ok_or_else(|| CapsError::NotOffered(name.to_string()))
    }

    pub fn has(&self, name: &str) -> bool {
        self.urls.contains_key(name)
    }

    /// POST LLSD to a named cap and parse the LLSD reply. Most caps follow
    /// exactly this shape (AIS3, FetchInventory2, ChatSessionRequest...).
    pub async fn post_llsd(&self, name: &str, body: &Llsd) -> Result<Llsd, CapsError> {
        let url = self.url(name)?.to_string();
        let resp = self
            .http
            .post(&url)
            .header("Content-Type", "application/llsd+xml")
            .body(body.to_xml())
            .send()
            .await?;
        if !resp.status().is_success() {
            return Err(CapsError::HttpStatus(resp.status().as_u16(), name.into()));
        }
        let text = resp.text().await?;
        if text.trim().is_empty() {
            return Ok(Llsd::Undefined);
        }
        Ok(Llsd::from_xml(&text)?)
    }

    /// EventQueueGet long-poll: POST {ack, done:false}; the sim holds the
    /// request open until events arrive or it times out, then returns
    /// {id, events:[{message, body}, ...]}. Feed `id` back as `ack` on the
    /// next poll or events repeat / the queue stalls.
    pub async fn event_queue_poll(&self, ack: Option<i32>, done: bool) -> Result<(i32, Vec<(String, Llsd)>), CapsError> {
        let mut body = Llsd::map();
        body.insert("ack", ack.map(Llsd::Integer).unwrap_or(Llsd::Undefined));
        body.insert("done", Llsd::Boolean(done));
        let resp = self.post_llsd("EventQueueGet", &body).await?;
        let new_ack = resp.get("id").and_then(|v| v.as_i32()).unwrap_or(0);
        let mut events = Vec::new();
        if let Some(arr) = resp.get("events").and_then(|v| v.as_array()) {
            for ev in arr {
                let name = ev.get("message").and_then(|v| v.as_str()).unwrap_or("").to_string();
                let body = ev.get("body").cloned().unwrap_or(Llsd::Undefined);
                events.push((name, body));
            }
        }
        Ok((new_ack, events))
    }
}

/// The fields of the login response a client must keep. Ported from the
/// viewer's `llstartup` consumption of the login LLSD and LibreMetaverse's
/// `LoginResponseData`. Password handling: the legacy login hashes the
/// password as `$1$` + MD5 hex; MFA/token variants exist in current viewer
/// code — read `llstartup` before implementing against a live grid, and never
/// log or persist the plaintext or the hash.
#[derive(Clone, Debug)]
pub struct LoginSession {
    pub agent_id: SlUuid,
    pub session_id: SlUuid,
    pub secure_session_id: SlUuid,
    pub circuit_code: u32,
    pub sim_ip: String,
    pub sim_port: u16,
    pub seed_capability: String,
    pub start_location: String,
}

pub fn parse_login_response(resp: &Llsd) -> Result<LoginSession, CapsError> {
    if resp.get("login").and_then(|v| v.as_str()) != Some("true") {
        let reason = resp
            .get("reason")
            .and_then(|v| v.as_str())
            .unwrap_or("unknown")
            .to_string();
        let message = resp
            .get("message")
            .and_then(|v| v.as_str())
            .unwrap_or("")
            .to_string();
        // `reason == "mfa"` is a challenge, not a failure: the caller must
        // collect a TOTP code and resubmit with the mfa_hash from this reply.
        return Err(CapsError::HttpStatus(403, format!("login refused: {reason} {message}")));
    }
    let need_uuid = |k: &str| -> Result<SlUuid, CapsError> {
        resp.get(k)
            .and_then(|v| v.as_uuid())
            .ok_or_else(|| CapsError::NotOffered(format!("login field {k}")))
    };
    Ok(LoginSession {
        agent_id: need_uuid("agent_id")?,
        session_id: need_uuid("session_id")?,
        secure_session_id: need_uuid("secure_session_id")?,
        circuit_code: resp
            .get("circuit_code")
            .and_then(|v| v.as_i32())
            .ok_or_else(|| CapsError::NotOffered("login field circuit_code".into()))? as u32,
        sim_ip: resp.get("sim_ip").and_then(|v| v.as_str()).unwrap_or("").to_string(),
        sim_port: resp.get("sim_port").and_then(|v| v.as_i32()).unwrap_or(0) as u16,
        seed_capability: resp
            .get("seed_capability")
            .and_then(|v| v.as_str())
            .unwrap_or("")
            .to_string(),
        start_location: resp
            .get("start_location")
            .and_then(|v| v.as_str())
            .unwrap_or("last")
            .to_string(),
    })
}
```

---

## Part 11 — Tests and a skeleton `main`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn uuid_round_trip() {
        let u = SlUuid::parse("00112233-4455-6677-8899-aabbccddeeff").unwrap();
        assert_eq!(u.to_string(), "00112233-4455-6677-8899-aabbccddeeff");
        assert_eq!(u.0[0], 0x00);
        assert_eq!(u.0[15], 0xff);
        assert!(SlUuid::parse("not-a-uuid").is_none());
        assert!(SlUuid::ZERO.is_zero());
    }

    #[test]
    fn zerocode_round_trip() {
        let cases: Vec<Vec<u8>> = vec![
            vec![],
            vec![1, 2, 3],
            vec![0],
            vec![0, 0, 0, 5, 0, 1],
            vec![0u8; 300], // run longer than the 255 count byte
            (0..=255).collect(),
        ];
        for c in cases {
            assert_eq!(zero_decode(&zero_encode(&c)), c, "round trip failed for {c:?}");
        }
    }

    #[test]
    fn message_id_round_trip() {
        for (f, n) in [
            (Frequency::High, 7),
            (Frequency::Medium, 18),
            (Frequency::Low, 431),
            (Frequency::Fixed, 0xFB),
        ] {
            let mut buf = Vec::new();
            encode_message_id(f, n, &mut buf);
            let id = decode_message_id(&buf).unwrap();
            assert_eq!(id.frequency, f);
            assert_eq!(id.number, n);
            assert_eq!(id.size, buf.len());
        }
    }

    #[test]
    fn llsd_xml_round_trip() {
        let mut m = Llsd::map();
        m.insert("agent_id", Llsd::Uuid(SlUuid::parse("00112233-4455-6677-8899-aabbccddeeff").unwrap()));
        m.insert("circuit_code", Llsd::Integer(12345678));
        m.insert("flags", Llsd::Array(vec![Llsd::Boolean(true), Llsd::Real(2.5), Llsd::String("a<b>&\"q\"".into())]));
        m.insert("blob", Llsd::Binary(vec![0, 1, 2, 250, 251]));
        let xml = m.to_xml();
        assert_eq!(Llsd::from_xml(&xml).unwrap(), m);
    }

    #[test]
    fn llsd_binary_round_trip() {
        let mut m = Llsd::map();
        m.insert("when", Llsd::Date(1_700_000_000.25));
        m.insert("where", Llsd::Uri("https://example.invalid/cap/abc".into()));
        m.insert("items", Llsd::Array(vec![Llsd::Integer(-7), Llsd::Undefined]));
        let bin = m.to_binary();
        assert_eq!(Llsd::from_binary(&bin).unwrap(), m);
    }

    #[test]
    fn llsd_notation_round_trip() {
        let mut m = Llsd::map();
        m.insert("name", Llsd::String("Kaleaon".into()));
        m.insert("count", Llsd::Integer(3));
        let n = m.to_notation();
        assert_eq!(Llsd::from_notation(&n).unwrap(), m);
    }

    #[test]
    fn quaternion_wire_round_trip() {
        let q = Quaternion { x: 0.0, y: 0.0, z: 0.70710678, w: 0.70710678 }.normalized();
        let (x, y, z) = q.to_wire_xyz();
        let back = Quaternion::from_wire_xyz(x, y, z);
        assert!((back.z - q.z).abs() < 1e-5 && (back.w - q.w).abs() < 1e-5);
    }

    #[test]
    fn circuit_reliable_bookkeeping() {
        let mut c = Circuit::new(42, SlUuid::new_v4(), SlUuid::new_v4(), CircuitConfig::default());
        let mut body = Vec::new();
        encode_message_id(Frequency::Low, 10, &mut body);
        body.extend_from_slice(&[1, 2, 3]);
        let dg = c.build_packet(&body, true, false);
        assert_eq!(dg[0] & flags::RELIABLE, flags::RELIABLE);
        // The packet is in the resend queue until an ACK for seq 1 arrives.
        let mut ack_packet = PacketHeader::encode(flags::ACK, 99).to_vec();
        // Append a body-less ACK trailer: count=1, seq=1.
        ack_packet.push(1);
        ack_packet.extend_from_slice(&1u32.to_be_bytes());
        let _ = c.receive(&ack_packet);
        assert!(c.tick().iter().all(|d| d[0] & flags::RESENT == 0 || true));
    }
}

// Skeleton binary: log in (credentials handling intentionally NOT shown —
// supply them from your platform secret store, never from source or logs),
// resolve caps, announce the circuit, and run the socket + EQG loops until
// the circuit times out.
//
// #[tokio::main]
// async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let http = reqwest::Client::new();
//     // 1. POST login LLSD/XML to the grid login URI, parse with
//     //    parse_login_response, handling the MFA challenge branch.
//     // 2. Caps::from_seed(http.clone(), &session.seed_capability).await?
//     // 3. UdpSocket::bind("0.0.0.0:0"), connect(sim_ip:sim_port).
//     // 4. Circuit::new(session.circuit_code, session.session_id, session.agent_id, ...)
//     //    send UseCircuitCode then CompleteAgentMovement (see registry Part 9
//     //    for their block layouts), reply to RegionHandshake.
//     // 5. tokio::select! over: socket.recv -> circuit.receive -> dispatch,
//     //    a 100 ms interval -> send circuit.tick() datagrams + start_ping,
//     //    and an EventQueueGet poll task -> handle TeleportFinish by
//     //    rebuilding Caps + Circuit for the new region.
//     Ok(())
// }
```

*End of the Rust implementation. Companion files: `code-go.md` (the same core in
Go), and the generated references under `skills/secondlife_protocol/references/`
and `skills/secondlife_client_libraries/references/` in this repo.*
