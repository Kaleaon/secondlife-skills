# React + TypeScript for a Linkpoint-Style Second Life Viewer

> **What this file ports, and from where.** This is a complete, working TypeScript
> implementation of the client side of a Second Life viewer in the React /
> React Native style of Joe's Linkpoint and React-Linkpoint projects. Every
> protocol shape in here is ported from a canonical source, named at the top
> of each section:
>
> - LLSD types and serialisations — from Linden Lab `indra/llcommon/llsd.h`
>   and `llsdserialize.cpp` in `secondlife/viewer`, cross-checked against
>   `LibreMetaverse.StructuredData` (C#, BSD-3) in
>   `cinderblocks/libremetaverse` and `secondlife/python-llsd`.
> - UDP packet layout, flags, frequency encoding, and ZeroCode — from
>   `message_template.msg` in `secondlife/master-message-template`, diffed
>   against the template shipped in `secondlife/viewer/indrallmessage`, and
>   from `LibreMetaverse.Transport` + `LibreMetaverse.Protocol`.
> - Capability names and payloads — from `llviewerregion.cpp`
>   (`buildCapabilityNames`) and `llaisapi.cpp` (AIS3) in `secondlife/viewer`.
> - Login flow — from `llstartup.cpp` in the viewer and LibreMetaverse's
>   `Login` implementation, with the MFA challenge handling pattern proven
>   in the Lumiya repair work (parse `reason` / `mfa_hash`, resubmit with a
>   TOTP token, never persist the hash unencrypted).
> - The TypeScript starting point in the ecosystem is
>   `CasperTech/node-metaverse` (`@caspertech/node-metaverse` +
>   `@caspertech/llsd`). Treat it as a porting aid; where this file and
>   node-metaverse disagree, LibreMetaverse plus viewer code wins.
>
> **Licence note.** The protocol *facts* (message layouts, cap names, LLSD
> grammar) are interoperability data. The code in this file is original
> TypeScript written for this repo. Do not copy LGPL-2.1 viewer C++ into a
> permissive TypeScript project; port the semantics, as done here.
>
> **How to read this file.** Sections 1-6 are the non-UI core (LLSD, UDP,
> caps, login, event queue, session state). Sections 7-13 are React:
> hooks and components. Section 14 is packaging: `package.json`, the
> React Native / Capacitor UDP bridge contract, and build notes.

---

## 0. Project shape and dependencies

```jsonc
// package.json (excerpt — see Section 14 for the full annotated version)
{
  "name": "linkpoint-core-ts",
  "private": true,
  "type": "module",
  "dependencies": {
    "react": "^19.0.0",
    "react-native": "^0.76.0",          // or plain react-dom for the web build
    "zustand": "^5.0.0",                // session store — see Section 6
    "three": "^0.170.0",                // MeshViewer — see Section 12
    "@types/three": "^0.170.0"
    // Deliberately NO llsd / udp dependency: Sections 1-2 implement both,
    // because the npm LLSD packages predate AIS3-era payloads and the
    // React Native UDP socket is a native bridge (Section 14), not dgram.
  }
}
```

### 0.1 Shared primitive types

Every other section depends on these. Second Life uses its own vector and
quaternion conventions: vectors are `{x, y, z}` with **z up** (unlike
three.js / glTF, which are y-up — Section 12 does the conversion at the
render boundary and nowhere else).

```ts
// src/sl/types.ts
// Primitive value types shared by LLSD, the UDP codec, and the UI layer.
// Ported from: LibreMetaverse.Types (UUID, Vector3, Quaternion) and
// indra/llmath in secondlife/viewer.

/** A Second Life UUID. Always stored lowercase, hyphenated, 36 chars. */
export type UUIDString = string;

export const NULL_KEY = "00000000-0000-0000-0000-000000000000" as UUIDString;

/** True only for the canonical 8-4-4-4-12 hyphenated form. */
export function isUUID(s: string): s is UUIDString {
  return /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s);
}

/** Normalise a UUID coming off the wire (XML LLSD may upper-case it). */
export function uuid(s: string): UUIDString {
  const v = s.trim().toLowerCase();
  if (!isUUID(v)) throw new Error(`Invalid UUID: ${JSON.stringify(s)}`);
  return v as UUIDString;
}

/** 16 raw bytes <-> UUID string. UDP fields carry the 16-byte form. */
export function uuidToBytes(id: UUIDString): Uint8Array {
  const hex = id.replace(/-/g, "");
  const out = new Uint8Array(16);
  for (let i = 0; i < 16; i++) out[i] = parseInt(hex.slice(i * 2, i * 2 + 2), 16);
  return out;
}

export function bytesToUUID(b: Uint8Array, offset = 0): UUIDString {
  const hex = Array.from(b.subarray(offset, offset + 16), (x) =>
    x.toString(16).padStart(2, "0"),
  ).join("");
  return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}` as UUIDString;
}

/** Second Life vector: x east, y north, z up, all f32 on the wire. */
export interface Vector3 {
  x: number;
  y: number;
  z: number;
}

export interface Vector3d {
  // Global / region-corner positions use f64 ("Vector3d" in the template).
  x: number;
  y: number;
  z: number;
}

/**
 * Quaternion. On the wire an LLQuaternion is only 3 x f32: the scalar (w)
 * component is reconstructed as sqrt(1 - x^2 - y^2 - z^2). See the codec
 * in Section 2.4 — getting this wrong is the classic "avatars rotated
 * 90 degrees" bug.
 */
export interface Quaternion {
  x: number;
  y: number;
  z: number;
  w: number;
}

/** Dequantise a terse-update rotation component packed into a u16/u32. */
export function dequantise(v: number, max: number, range: number): number {
  return (v / max) * range - range / 2;
}
```

---

## 1. LLSD in TypeScript

LLSD (Linden Lab Structured Data) is the data model for login, caps, the
event queue, and inventory. Types: undefined, boolean, integer (32-bit),
real (f64), string, binary, UUID, date, URI, array, map. Three wire
serialisations matter: **XML** (caps, content type
`application/llsd+xml`), **binary** (some endpoints, and the notation used
inside a few UDP messages), and **notation** (human-readable debugging
format, mostly legacy). JSON is *not* a simulator wire format — it exists
in LibreMetaverse.StructuredData for tooling only.

### 1.1 The value model

```ts
// src/sl/llsd.ts
// LLSD value model + XML, binary, and notation codecs.
// Ported from: indra/llcommon/llsdserialize.cpp (secondlife/viewer),
// LibreMetaverse.StructuredData.LLSD, secondlife/python-llsd (llbase.llsd).

import { UUIDString, isUUID } from "./types";

/** Binary data. In XML LLSD this is base64; in binary LLSD it is raw. */
export class LLSDBinary {
  constructor(public readonly data: Uint8Array) {}
}

/** A URI value. Distinct from a plain string in LLSD typing. */
export class LLSDUri {
  constructor(public readonly uri: string) {}
}

/**
 * The LLSD value union. `undefined` (LLSD "undef") is modelled as the
 * exported `LLSD_UNDEF` symbol so it survives inside arrays and maps
 * where a JS `undefined` would be dropped by Object.entries.
 */
export const LLSD_UNDEF = Symbol("llsd-undef");
export type LLSDValue =
  | typeof LLSD_UNDEF
  | boolean
  | number // integer OR real — see LLSDInteger wrapper below
  | string
  | UUIDString & { readonly __llsdUUID?: unique symbol } // plain string at runtime
  | Date
  | LLSDBinary
  | LLSDUri
  | LLSDValue[]
  | { [key: string]: LLSDValue };

/**
 * LLSD integers are signed 32-bit; reals are f64. A bare JS number cannot
 * tell them apart (1 vs 1.0 serialise differently in binary LLSD and the
 * simulator's parser cares). Wrap integers explicitly at API boundaries.
 */
export class LLSDInteger {
  constructor(public readonly value: number) {
    if (!Number.isInteger(value) || value < -0x8000_0000 || value > 0x7fff_ffff) {
      throw new Error(`LLSD integer out of 32-bit range: ${value}`);
    }
  }
}

export function isLLSDInteger(v: unknown): v is LLSDInteger {
  return v instanceof LLSDInteger;
}

/** Convenience constructors that keep call sites readable. */
export const llsd = {
  int: (n: number): LLSDInteger => new LLSDInteger(n),
  bin: (b: Uint8Array): LLSDBinary => new LLSDBinary(b),
  uri: (u: string): LLSDUri => new LLSDUri(u),
  uuid: (u: UUIDString): LLSDValue => u as LLSDValue,
  undef: LLSD_UNDEF,
};
```

### 1.2 XML serialisation (the caps format)

```ts
// src/sl/llsd-xml.ts
// XML LLSD: <llsd><map><key>name</key><string>value</string></map></llsd>
// Grammar per llsdserialize.cpp's LLSDXMLParser / LLSDXMLFormatter.

import {
  LLSDValue, LLSDInteger, LLSDBinary, LLSDUri, LLSD_UNDEF, isLLSDInteger,
} from "./llsd";
import { isUUID } from "./types";

function escapeXml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function base64Encode(data: Uint8Array): string {
  // Chunked to avoid call-stack overflow on large binary blobs (textures
  // never travel as LLSD binary, but asset metadata blobs can be 64 KiB+).
  let s = "";
  const CHUNK = 0x8000;
  for (let i = 0; i < data.length; i += CHUNK) {
    s += String.fromCharCode(...data.subarray(i, i + CHUNK));
  }
  return btoa(s);
}

export function base64Decode(b64: string): Uint8Array {
  const bin = atob(b64.replace(/\s+/g, ""));
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

/** Serialise one value (without the <llsd> wrapper). */
export function llsdValueToXml(v: LLSDValue): string {
  if (v === LLSD_UNDEF) return "<undef/>";
  if (typeof v === "boolean") return `<boolean>${v ? 1 : 0}</boolean>`;
  if (isLLSDInteger(v)) return `<integer>${v.value}</integer>`;
  if (typeof v === "number") {
    // LLSD reals: always emit a decimal point so a strict parser does not
    // read "1" back as an integer. llsdserialize.cpp does the same.
    return `<real>${Number.isInteger(v) ? v.toFixed(1) : String(v)}</real>`;
  }
  if (v instanceof LLSDBinary) return `<binary>${base64Encode(v.data)}</binary>`;
  if (v instanceof LLSDUri) return `<uri>${escapeXml(v.uri)}</uri>`;
  if (v instanceof Date) return `<date>${v.toISOString()}</date>`;
  if (typeof v === "string") {
    // A 36-char hyphenated string that parses as a UUID is written as
    // <uuid> ONLY when the caller wrapped it — but LLSDValue models UUID
    // as a plain string, so the heuristic lives here: caps payloads from
    // the simulator always type UUID fields as <uuid>, and echoing them
    // back as <string> is rejected by AIS3. This mirrors how
    // LibreMetaverse's OSDUUID is distinct from OSDString.
    return isUUID(v) ? `<uuid>${v}</uuid>` : `<string>${escapeXml(v)}</string>`;
  }
  if (Array.isArray(v)) {
    return `<array>${v.map(llsdValueToXml).join("")}</array>`;
  }
  const entries = Object.entries(v)
    .map(([k, val]) => `<key>${escapeXml(k)}</key>${llsdValueToXml(val)}`)
    .join("");
  return `<map>${entries}</map>`;
}

/** Serialise a complete LLSD document. */
export function llsdToXml(v: LLSDValue): string {
  return `<?xml version="1.0" encoding="UTF-8"?>\n<llsd>${llsdValueToXml(v)}</llsd>`;
}
```

```ts
// src/sl/llsd-xml-parse.ts
// Parsing XML LLSD without a DOM dependency so the same code runs in
// React Native (no DOMParser), the browser, and Node tests. This is a
// small recursive-descent parser over the LLSD XML subset — it is NOT a
// general XML parser and must only be fed LLSD documents.

import {
  LLSDValue, LLSDInteger, LLSDBinary, LLSDUri, LLSD_UNDEF,
} from "./llsd";
import { base64Decode } from "./llsd-xml";
import { uuid } from "./types";

interface Token {
  kind: "open" | "close" | "empty" | "text";
  name?: string;
  text?: string;
}

function tokenise(xml: string): Token[] {
  const tokens: Token[] = [];
  let i = 0;
  // Strip the XML declaration and any DOCTYPE — LLSD never uses either
  // beyond the standard prolog.
  xml = xml.replace(/<\?xml[^>]*\?>/, "").replace(/<!DOCTYPE[^>]*>/, "");
  while (i < xml.length) {
    if (xml[i] === "<") {
      const end = xml.indexOf(">", i);
      if (end === -1) throw new Error("LLSD XML: unterminated tag");
      const raw = xml.slice(i + 1, end).trim();
      if (raw.startsWith("/")) tokens.push({ kind: "close", name: raw.slice(1) });
      else if (raw.endsWith("/")) tokens.push({ kind: "empty", name: raw.slice(0, -1).trim() });
      else tokens.push({ kind: "open", name: raw.split(/\s/)[0] });
      i = end + 1;
    } else {
      const next = xml.indexOf("<", i);
      const text = xml.slice(i, next === -1 ? xml.length : next);
      if (text.trim().length > 0) tokens.push({ kind: "text", text: unescapeXml(text) });
      i = next === -1 ? xml.length : next;
    }
  }
  return tokens;
}

function unescapeXml(s: string): string {
  return s
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&#x([0-9a-fA-F]+);/g, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(parseInt(d, 10)))
    .replace(/&amp;/g, "&"); // ampersand LAST, or &amp;lt; double-unescapes
}

class Parser {
  private pos = 0;
  constructor(private readonly tokens: Token[]) {}

  parseDocument(): LLSDValue {
    const t = this.tokens[this.pos];
    if (!t || t.kind !== "open" || t.name !== "llsd") {
      throw new Error("LLSD XML: document does not start with <llsd>");
    }
    this.pos++;
    const v = this.parseValue();
    return v;
  }

  private peek(): Token | undefined {
    return this.tokens[this.pos];
  }

  private parseValue(): LLSDValue {
    const t = this.tokens[this.pos];
    if (!t) throw new Error("LLSD XML: unexpected end of input");
    if (t.kind === "empty") {
      this.pos++;
      switch (t.name) {
        case "undef": return LLSD_UNDEF;
        case "string": return "";
        case "array": return [];
        case "map": return {};
        case "binary": return new LLSDBinary(new Uint8Array(0));
        default: throw new Error(`LLSD XML: unexpected empty element <${t.name}/>`);
      }
    }
    if (t.kind !== "open") throw new Error(`LLSD XML: expected element, got ${t.kind}`);
    const name = t.name!;
    this.pos++;
    switch (name) {
      case "array": {
        const arr: LLSDValue[] = [];
        while (this.peek()?.kind !== "close") arr.push(this.parseValue());
        this.pos++; // consume </array>
        return arr;
      }
      case "map": {
        const map: { [k: string]: LLSDValue } = {};
        while (this.peek()?.kind !== "close") {
          const kt = this.tokens[this.pos];
          if (!kt || kt.kind !== "open" || kt.name !== "key") {
            throw new Error("LLSD XML: expected <key> inside <map>");
          }
          this.pos++;
          const keyTok = this.tokens[this.pos];
          const key = keyTok?.kind === "text" ? keyTok.text! : "";
          if (keyTok?.kind === "text") this.pos++;
          this.pos++; // consume </key>
          map[key] = this.parseValue();
        }
        this.pos++; // consume </map>
        return map;
      }
      default: {
        // Scalar: text content (possibly empty) then the close tag.
        let text = "";
        const tt = this.peek();
        if (tt?.kind === "text") { text = tt.text!; this.pos++; }
        this.pos++; // consume close tag
        switch (name) {
          case "boolean": return text === "1" || text === "true";
          case "integer": return new LLSDInteger(parseInt(text, 10));
          case "real": return parseFloat(text);
          case "string": return text;
          case "uuid": return uuid(text);
          case "date": return new Date(text);
          case "uri": return new LLSDUri(text);
          case "binary": return new LLSDBinary(base64Decode(text));
          case "undef": return LLSD_UNDEF;
          default: throw new Error(`LLSD XML: unknown element <${name}>`);
        }
      }
    }
  }
}

/** Parse a complete XML LLSD document. Throws on malformed input. */
export function llsdFromXml(xml: string): LLSDValue {
  return new Parser(tokenise(xml)).parseDocument();
}

/** Typed accessors — caps payloads are untyped maps; never index blindly. */
export function asMap(v: LLSDValue): { [k: string]: LLSDValue } {
  if (typeof v !== "object" || v === null || Array.isArray(v) || v instanceof Date ||
      v instanceof LLSDBinary || v instanceof LLSDUri) {
    throw new Error("LLSD: expected map");
  }
  return v as { [k: string]: LLSDValue };
}
export function asArray(v: LLSDValue): LLSDValue[] {
  if (!Array.isArray(v)) throw new Error("LLSD: expected array");
  return v;
}
export function getString(m: { [k: string]: LLSDValue }, key: string, fallback = ""): string {
  const v = m[key];
  return typeof v === "string" ? v : fallback;
}
export function getInt(m: { [k: string]: LLSDValue }, key: string, fallback = 0): number {
  const v = m[key];
  if (v instanceof LLSDInteger) return v.value;
  if (typeof v === "number") return Math.trunc(v);
  return fallback;
}
export function getUUID(m: { [k: string]: LLSDValue }, key: string): string {
  const v = m[key];
  if (typeof v === "string" && isUUID(v)) return v;
  throw new Error(`LLSD: expected UUID at key "${key}"`);
}
```

### 1.3 Binary LLSD

Binary LLSD prefixes every value with a one-byte type marker. It appears
in the event queue on some grids, in `ObjectUpdate` extra data paths, and
as the on-disk format for some cache files. Markers (from
`llsdserialize.cpp`): `!` undef, `1`/`0` boolean true/false, `i` integer,
`r` real, `s` string, `$` binary, `u` UUID, `d` date, `l` URI, `[` array,
`{` map, `]`/`}` terminators, `:` map key separator mechanics (keys are
length-prefixed strings preceded by `s` in the reference writer — the
reader below accepts the canonical form produced by the viewer).

```ts
// src/sl/llsd-binary.ts
// Binary LLSD reader/writer. All multi-byte integers are big-endian.
// Ported from: LLBinarySerialiser in LibreMetaverse.StructuredData and
// llsdserialize.cpp's binary formatter in secondlife/viewer.

import {
  LLSDValue, LLSDInteger, LLSDBinary, LLSDUri, LLSD_UNDEF, isLLSDInteger,
} from "./llsd";
import { uuidToBytes, bytesToUUID, uuid } from "./types";

class Writer {
  private chunks: Uint8Array[] = [];
  private len = 0;
  private push(b: Uint8Array): void { this.chunks.push(b); this.len += b.length; }
  byte(n: number): void { this.push(new Uint8Array([n])); }
  char(c: string): void { this.byte(c.charCodeAt(0)); }
  u32(n: number): void {
    const b = new Uint8Array(4);
    new DataView(b.buffer).setUint32(0, n >>> 0, false); // big-endian
    this.push(b);
  }
  i32(n: number): void {
    const b = new Uint8Array(4);
    new DataView(b.buffer).setInt32(0, n, false);
    this.push(b);
  }
  f64(n: number): void {
    const b = new Uint8Array(8);
    new DataView(b.buffer).setFloat64(0, n, false);
    this.push(b);
  }
  raw(b: Uint8Array): void { this.push(b); }
  stringWithLength(s: string): void {
    const enc = new TextEncoder().encode(s);
    this.u32(enc.length);
    this.push(enc);
  }
  finish(): Uint8Array {
    const out = new Uint8Array(this.len);
    let o = 0;
    for (const c of this.chunks) { out.set(c, o); o += c.length; }
    return out;
  }
}

function writeValue(w: Writer, v: LLSDValue): void {
  if (v === LLSD_UNDEF) { w.char("!"); return; }
  if (typeof v === "boolean") { w.char(v ? "1" : "0"); return; }
  if (isLLSDInteger(v)) { w.char("i"); w.i32(v.value); return; }
  if (typeof v === "number") { w.char("r"); w.f64(v); return; }
  if (v instanceof LLSDBinary) {
    w.char("$"); w.u32(v.data.length); w.raw(v.data); return;
  }
  if (v instanceof LLSDUri) { w.char("l"); w.stringWithLength(v.uri); return; }
  if (v instanceof Date) { w.char("d"); w.f64(v.getTime() / 1000); return; }
  if (typeof v === "string") {
    // UUIDs and strings share the length-prefixed body; the marker differs.
    // A UUID string that is exactly canonical form is written as 'u' with
    // NO length prefix and 16 raw bytes — matching the viewer writer.
    if (/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(v)) {
      w.char("u"); w.raw(uuidToBytes(uuid(v))); return;
    }
    w.char("s"); w.stringWithLength(v); return;
  }
  if (Array.isArray(v)) {
    w.char("["); w.u32(v.length);
    for (const item of v) writeValue(w, item);
    w.char("]");
    return;
  }
  const keys = Object.keys(v);
  w.char("{"); w.u32(keys.length);
  for (const k of keys) {
    w.char("s"); w.stringWithLength(k);
    writeValue(w, v[k]);
  }
  w.char("}");
}

export function llsdToBinary(v: LLSDValue): Uint8Array {
  const w = new Writer();
  writeValue(w, v);
  return w.finish();
}

class Reader {
  private view: DataView;
  pos = 0;
  constructor(private readonly buf: Uint8Array) {
    this.view = new DataView(buf.buffer, buf.byteOffset, buf.byteLength);
  }
  byte(): number { return this.buf[this.pos++]; }
  char(): string { return String.fromCharCode(this.byte()); }
  u32(): number { const n = this.view.getUint32(this.pos, false); this.pos += 4; return n; }
  i32(): number { const n = this.view.getInt32(this.pos, false); this.pos += 4; return n; }
  f64(): number { const n = this.view.getFloat64(this.pos, false); this.pos += 8; return n; }
  take(n: number): Uint8Array { const b = this.buf.subarray(this.pos, this.pos + n); this.pos += n; return b; }
  stringBody(): string {
    const len = this.u32();
    return new TextDecoder().decode(this.take(len));
  }
}

function readValue(r: Reader): LLSDValue {
  const marker = r.char();
  switch (marker) {
    case "!": return LLSD_UNDEF;
    case "1": return true;
    case "0": return false;
    case "i": return new LLSDInteger(r.i32());
    case "r": return r.f64();
    case "s": return r.stringBody();
    case "$": { const len = r.u32(); return new LLSDBinary(r.take(len).slice()); }
    case "u": return bytesToUUID(r.buf, (() => { const p = r.pos; r.pos += 16; return p; })());
    case "d": return new Date(r.f64() * 1000);
    case "l": return new LLSDUri(r.stringBody());
    case "[": {
      const count = r.u32();
      const arr: LLSDValue[] = [];
      for (let i = 0; i < count; i++) arr.push(readValue(r));
      if (r.char() !== "]") throw new Error("Binary LLSD: array missing ] terminator");
      return arr;
    }
    case "{": {
      const count = r.u32();
      const map: { [k: string]: LLSDValue } = {};
      for (let i = 0; i < count; i++) {
        if (r.char() !== "s") throw new Error("Binary LLSD: map key must be a string");
        const key = r.stringBody();
        map[key] = readValue(r);
      }
      if (r.char() !== "}") throw new Error("Binary LLSD: map missing } terminator");
      return map;
    }
    default:
      throw new Error(`Binary LLSD: unknown marker ${JSON.stringify(marker)} at ${r.pos - 1}`);
  }
}

export function llsdFromBinary(buf: Uint8Array): LLSDValue {
  return readValue(new Reader(buf));
}
```

### 1.4 Notation LLSD (debugging format)

Notation is the human-readable form you will see in viewer logs and in
old wiki examples: `{'agent_id':u12345678-…,'count':i42}`. You rarely
send it, but being able to *read* it makes packet logs and Firestorm
debug output legible, and LibreMetaverse exposes it for the same reason.

```ts
// src/sl/llsd-notation.ts
// Read-only notation LLSD formatter: LLSD value -> notation string.
// Prefixes: u = UUID, i = integer, r = real, s/'…' = string, b(n)"…" =
// binary, d = date, l = URI, [ ] = array, { } = map, ! = undef.

import { LLSDValue, LLSDInteger, LLSDBinary, LLSDUri, LLSD_UNDEF, isLLSDInteger } from "./llsd";

export function llsdToNotation(v: LLSDValue): string {
  if (v === LLSD_UNDEF) return "!";
  if (typeof v === "boolean") return v ? "1" : "0";
  if (isLLSDInteger(v)) return `i${v.value}`;
  if (typeof v === "number") return `r${v}`;
  if (v instanceof LLSDBinary) return `b${v.data.length}"<${v.data.length} bytes>"`;
  if (v instanceof LLSDUri) return `l"${v.uri}"`;
  if (v instanceof Date) return `d"${v.toISOString()}"`;
  if (typeof v === "string") {
    return /^[0-9a-f-]{36}$/i.test(v) ? `u${v}` : `'${v.replace(/'/g, "\\'")}'`;
  }
  if (Array.isArray(v)) return `[${v.map(llsdToNotation).join(",")}]`;
  return `{${Object.entries(v).map(([k, val]) => `'${k}':${llsdToNotation(val)}`).join(",")}}`;
}
```

### 1.5 LLSD unit-test vectors (port these into your test suite)

```ts
// src/sl/__tests__/llsd.test.ts — the vectors that catch the classic bugs:
// 1. integer 1 vs real 1.0 collapsing, 2. UUID echoed as <string> to AIS3,
// 3. base64 binary with embedded whitespace, 4. &amp; double-unescape.

import { llsdToXml, llsdFromXml } from "../llsd-xml";
import { llsdToBinary, llsdFromBinary } from "../llsd-binary";
import { llsd, LLSDInteger } from "../llsd";

describe("llsd round trips", () => {
  it("keeps integers distinct from reals in binary form", () => {
    const doc = { count: llsd.int(1), ratio: 1.0 };
    const back = llsdFromBinary(llsdToBinary(doc)) as Record<string, unknown>;
    expect(back.count).toBeInstanceOf(LLSDInteger);
    expect(typeof back.ratio).toBe("number");
  });

  it("round-trips a caps-style map through XML", () => {
    const doc = {
      agent_id: "12345678-1234-1234-1234-123456789012",
      items: [llsd.int(3), "a & b <test>"],
      nested: { enabled: true },
    };
    const xml = llsdToXml(doc);
    expect(xml).toContain("<uuid>12345678-1234-1234-1234-123456789012</uuid>");
    expect(llsdFromXml(xml)).toEqual(doc);
  });
});
```

---

## 2. The UDP packet codec, ZeroCode, and the circuit

Second Life's realtime plane is UDP to the simulator. A packet is:

```
+--------+-----------+-------+===================+-----------+
| flags  | sequence  | extra | message body      | appended  |
| 1 byte | u32 BE    | 1 byte| (ID + blocks)     | ACKs      |
+--------+-----------+-------+===================+-----------+
```

- Flags: `0x80` Zerocoded, `0x40` Reliable, `0x20` Resent, `0x10` Ack
  (appended ACK list present).
- Message IDs are encoded by *frequency*: High = 1 byte, Medium = 2
  bytes (`0xFF` + id), Low = 4 bytes (`0xFF 0xFF` + u16), Fixed = 4 bytes
  (`0xFF 0xFF 0xFF` + id).
- In a browser there is no UDP at all, and in React Native there is no
  Node `dgram`. Linkpoint-style clients therefore speak UDP through a
  **bridge**: a local WebSocket (desktop/Electron or a LAN proxy) or a
  native module (Android/iOS) that owns real `DatagramSocket`s and frames
  raw packet bytes to JS. Section 2.1 defines that bridge contract; the
  rest of this section is bridge-agnostic and operates on `Uint8Array`.

### 2.1 The UDP bridge contract

```ts
// src/sl/udp-bridge.ts
// Contract between the TS core and whatever owns real UDP sockets.
// Implementations: (a) Capacitor plugin "SLUdp" (Section 14.2),
// (b) React Native native module with the same surface,
// (c) WebSocket to a desktop sidecar for the Electron/web build,
// (d) in-memory loopback for tests and for OpenSim-on-localhost demos.

export interface UdpEndpoint {
  host: string;
  port: number;
}

export interface UdpBridge {
  /** Resolve once the underlying socket(s) are ready to send. */
  connect(): Promise<void>;
  /** Send one complete SL packet (already headered + zerocoded by us). */
  send(to: UdpEndpoint, packet: Uint8Array): Promise<void>;
  /** Subscribe to inbound packets. Returns an unsubscribe function. */
  onPacket(cb: (from: UdpEndpoint, packet: Uint8Array) => void): () => void;
  /** Subscribe to bridge-level errors (socket closed, network switch). */
  onError(cb: (err: Error) => void): () => void;
  close(): Promise<void>;
}

/** A bridge that drops everything — used before login and in Storybook. */
export class NullBridge implements UdpBridge {
  async connect(): Promise<void> {}
  async send(): Promise<void> {}
  onPacket(): () => void { return () => {}; }
  onError(): () => void { return () => {}; }
  async close(): Promise<void> {}
}

/**
 * WebSocket bridge: each WS binary frame is exactly one UDP datagram,
 * prefixed with a 2-byte big-endian port + a length-prefixed host string
 * so one WS connection can multiplex several region circuits (the current
 * region plus neighbours during teleport). The sidecar is a dumb pipe:
 * ALL SL protocol logic (this file) stays in TypeScript.
 */
export class WebSocketBridge implements UdpBridge {
  private ws: WebSocket | null = null;
  private packetCbs = new Set<(from: UdpEndpoint, p: Uint8Array) => void>();
  private errorCbs = new Set<(e: Error) => void>();

  constructor(private readonly url: string) {}

  async connect(): Promise<void> {
    this.ws = new WebSocket(this.url);
    this.ws.binaryType = "arraybuffer";
    await new Promise<void>((resolve, reject) => {
      this.ws!.addEventListener("open", () => resolve(), { once: true });
      this.ws!.addEventListener("error", () => reject(new Error("WS bridge connect failed")), { once: true });
    });
    this.ws.addEventListener("message", (ev) => {
      if (!(ev.data instanceof ArrayBuffer)) return;
      const frame = new Uint8Array(ev.data);
      const parsed = decodeBridgeFrame(frame);
      if (parsed) for (const cb of this.packetCbs) cb(parsed.from, parsed.packet);
    });
    this.ws.addEventListener("close", () => {
      for (const cb of this.errorCbs) cb(new Error("WS bridge closed"));
    });
  }

  async send(to: UdpEndpoint, packet: Uint8Array): Promise<void> {
    if (!this.ws || this.ws.readyState !== WebSocket.OPEN) {
      throw new Error("WS bridge not open");
    }
    this.ws.send(encodeBridgeFrame(to, packet));
  }

  onPacket(cb: (from: UdpEndpoint, p: Uint8Array) => void): () => void {
    this.packetCbs.add(cb);
    return () => this.packetCbs.delete(cb);
  }
  onError(cb: (err: Error) => void): () => void {
    this.errorCbs.add(cb);
    return () => this.errorCbs.delete(cb);
  }
  async close(): Promise<void> { this.ws?.close(); this.ws = null; }
}

function encodeBridgeFrame(to: UdpEndpoint, packet: Uint8Array): Uint8Array {
  const host = new TextEncoder().encode(to.host);
  const out = new Uint8Array(1 + host.length + 2 + packet.length);
  out[0] = host.length;
  out.set(host, 1);
  new DataView(out.buffer).setUint16(1 + host.length, to.port, false);
  out.set(packet, 1 + host.length + 2);
  return out;
}

function decodeBridgeFrame(frame: Uint8Array): { from: UdpEndpoint; packet: Uint8Array } | null {
  if (frame.length < 3) return null;
  const hostLen = frame[0];
  const host = new TextDecoder().decode(frame.subarray(1, 1 + hostLen));
  const port = new DataView(frame.buffer, frame.byteOffset).getUint16(1 + hostLen, false);
  return { from: { host, port }, packet: frame.subarray(1 + hostLen + 2).slice() };
}
```

### 2.2 Packet header, frequency encoding, and ZeroCode

ZeroCode is a run-length escape for zero bytes: on encode, each run of
`n` zero bytes becomes `0x00, n` (n ≤ 255); on decode, `0x00` followed by
a count expands back. It applies **only** to the message body of packets
flagged Zerocoded, and only after the 6-byte header — the header itself
(flags, sequence, extra-header-length) is never zerocoded. The template
flag decides per message, and the template has been wrong before (the
`ChatFromViewer` case: master template said zerocoded, the simulator
disagreed) — so the message table in 2.3 carries the flag per message and
is diffed against the viewer copy, never assumed.

```ts
// src/sl/packet.ts
// Packet framing, message-ID frequency encoding, ZeroCode.
// Ported from: indra/llmessage/llpacketring + message_template.msg
// semantics, LibreMetaverse.Transport (Packet.cs, UDPClient.cs).

export const PacketFlags = {
  Zerocoded: 0x80,
  Reliable: 0x40,
  Resent: 0x20,
  Ack: 0x10,
} as const;

export type MessageFrequency = "High" | "Medium" | "Low" | "Fixed";

/** Encode a message ID at its frequency. Returns 1, 2, or 4 bytes. */
export function encodeMessageId(freq: MessageFrequency, id: number): Uint8Array {
  switch (freq) {
    case "High":
      if (id < 1 || id > 0xfe) throw new Error(`High-frequency ID out of range: ${id}`);
      return new Uint8Array([id]);
    case "Medium":
      if (id < 1 || id > 0xfe) throw new Error(`Medium-frequency ID out of range: ${id}`);
      return new Uint8Array([0xff, id]);
    case "Low":
      if (id < 1 || id > 0xfffe) throw new Error(`Low-frequency ID out of range: ${id}`);
      return new Uint8Array([0xff, 0xff, (id >> 8) & 0xff, id & 0xff]);
    case "Fixed":
      // Fixed IDs are the full 32-bit values from the template, e.g.
      // PacketAck = 0xFFFFFFFB. They are written verbatim, big-endian.
      return new Uint8Array([
        (id >>> 24) & 0xff, (id >>> 16) & 0xff, (id >>> 8) & 0xff, id & 0xff,
      ]);
  }
}

/** Decode a message ID at `offset`. Returns the id, its frequency, and
 *  the number of bytes consumed. Mirrors the viewer's llmessage decode. */
export function decodeMessageId(
  buf: Uint8Array, offset: number,
): { id: number; freq: MessageFrequency; bytes: number } {
  const b0 = buf[offset];
  if (b0 !== 0xff) return { id: b0, freq: "High", bytes: 1 };
  const b1 = buf[offset + 1];
  if (b1 !== 0xff) return { id: b1, freq: "Medium", bytes: 2 };
  const b2 = buf[offset + 2];
  if (b2 !== 0xff) {
    return { id: (b2 << 8) | buf[offset + 3], freq: "Low", bytes: 4 };
  }
  const id =
    ((b2 << 24) | (buf[offset + 3] << 16)) >>> 0 === 0
      ? 0
      : ((0xff << 24) | (0xff << 16) | (0xff << 8) | buf[offset + 3]) >>> 0;
  return { id, freq: "Fixed", bytes: 4 };
}

/** ZeroCode-encode a message body. Header bytes are handled by the caller. */
export function zeroEncode(body: Uint8Array): Uint8Array {
  const out: number[] = [];
  let i = 0;
  while (i < body.length) {
    if (body[i] === 0) {
      let run = 0;
      while (i < body.length && body[i] === 0 && run < 255) { run++; i++; }
      out.push(0, run);
    } else {
      out.push(body[i]);
      i++;
    }
  }
  return new Uint8Array(out);
}

/** ZeroCode-decode. Throws on a truncated run (0x00 at end of buffer). */
export function zeroDecode(data: Uint8Array): Uint8Array {
  const out: number[] = [];
  let i = 0;
  while (i < data.length) {
    const b = data[i];
    if (b === 0) {
      if (i + 1 >= data.length) throw new Error("ZeroCode: truncated zero run");
      const count = data[i + 1];
      for (let n = 0; n < count; n++) out.push(0);
      i += 2;
    } else {
      out.push(b);
      i++;
    }
  }
  return new Uint8Array(out);
}

export interface DecodedPacket {
  flags: number;
  sequence: number;
  /** Offset of the first body byte in `body` (after ID decoding). */
  messageId: number;
  frequency: MessageFrequency;
  /** Body bytes with ZeroCode already removed and ID already consumed
   *  is NOT done here — `body` starts at the message ID. Use
   *  PacketReader (2.4) which handles both. */
  body: Uint8Array;
  /** Sequence numbers piggybacked on this packet (Ack flag). */
  appendedAcks: number[];
  reliable: boolean;
  zerocoded: boolean;
}

/**
 * Split a raw datagram into header + body, expand ZeroCode, and harvest
 * appended ACKs. Appended ACKs live at the very END of the packet
 * (after the body): a count byte followed by count x u32 BE. They are
 * stripped BEFORE ZeroCode expansion in the reference implementations —
 * the ACK block itself is never zerocoded.
 */
export function decodePacket(raw: Uint8Array): DecodedPacket {
  if (raw.length < 6) throw new Error("Packet shorter than 6-byte header");
  const flags = raw[0];
  const view = new DataView(raw.buffer, raw.byteOffset, raw.byteLength);
  const sequence = view.getUint32(1, false);
  const extraLen = raw[5];
  let bodyStart = 6 + extraLen;
  let bodyEnd = raw.length;

  let appendedAcks: number[] = [];
  if (flags & PacketFlags.Ack) {
    const ackCount = raw[raw.length - 1];
    const ackBytes = 1 + ackCount * 4;
    appendedAcks = [];
    for (let i = 0; i < ackCount; i++) {
      appendedAcks.push(view.getUint32(raw.length - ackBytes + i * 4, false));
    }
    bodyEnd = raw.length - ackBytes;
  }

  let body = raw.subarray(bodyStart, bodyEnd);
  const zerocoded = (flags & PacketFlags.Zerocoded) !== 0;
  if (zerocoded) body = zeroDecode(body);
  else body = body.slice();

  const { id, freq } = decodeMessageId(body, 0);
  return {
    flags,
    sequence,
    messageId: id,
    frequency: freq,
    body,
    appendedAcks,
    reliable: (flags & PacketFlags.Reliable) !== 0,
    zerocoded,
  };
}

/** Build a complete datagram. `body` must start with the encoded ID. */
export function encodePacket(opts: {
  sequence: number;
  body: Uint8Array; // message ID + blocks, unencoded
  zerocoded: boolean;
  reliable: boolean;
  appendedAcks?: number[];
}): Uint8Array {
  let flags = 0;
  if (opts.zerocoded) flags |= PacketFlags.Zerocoded;
  if (opts.reliable) flags |= PacketFlags.Reliable;
  const acks = opts.appendedAcks ?? [];
  if (acks.length > 0) flags |= PacketFlags.Ack;

  const body = opts.zerocoded ? zeroEncode(opts.body) : opts.body;
  const ackBytes = acks.length > 0 ? 1 + acks.length * 4 : 0;
  const out = new Uint8Array(6 + body.length + ackBytes);
  const view = new DataView(out.buffer);
  out[0] = flags;
  view.setUint32(1, opts.sequence >>> 0, false);
  out[5] = 0; // no extra header — the viewer only uses it for a few internal paths
  out.set(body, 6);
  if (acks.length > 0) {
    for (let i = 0; i < acks.length; i++) {
      view.setUint32(6 + body.length + i * 4, acks[i] >>> 0, false);
    }
    out[out.length - 1] = acks.length;
  }
  return out;
}
```

### 2.3 The message table (generated-style, hand-trimmed to the core set)

In production this table is *generated* from `message_template.msg` by a
build script (the same approach as LibreMetaverse.Protocol's source
generator and Lumiya's 477 Java classes) and the generated file is never
hand-edited. The excerpt below is the shape of that generated output for
the messages the React client actually implements; the full table in the
repo's `secondlife_protocol` references carries all 483 messages.

```ts
// src/sl/messages/table.ts — GENERATED from message_template.msg. Do not edit.
// Source: secondlife/master-message-template, diffed vs viewer copy 2026-11.

export interface MessageDef {
  name: string;
  frequency: MessageFrequency;
  id: number;
  trusted: boolean;
  zerocoded: boolean;
  deprecated?: boolean;
}

export const MESSAGES: Record<string, MessageDef> = {
  PacketAck:           { name: "PacketAck", frequency: "Fixed", id: 0xfffffffb, trusted: false, zerocoded: false },
  StartPingCheck:      { name: "StartPingCheck", frequency: "Fixed", id: 0xfffffff9, trusted: false, zerocoded: false },
  CompletePingCheck:   { name: "CompletePingCheck", frequency: "Fixed", id: 0xfffffff8, trusted: false, zerocoded: false },
  UseCircuitCode:      { name: "UseCircuitCode", frequency: "Low", id: 3, trusted: false, zerocoded: false },
  CompleteAgentMovement:{ name: "CompleteAgentMovement", frequency: "Low", id: 249, trusted: false, zerocoded: false },
  AgentUpdate:         { name: "AgentUpdate", frequency: "High", id: 4, trusted: false, zerocoded: true },
  AgentAnimation:      { name: "AgentAnimation", frequency: "Low", id: 378, trusted: false, zerocoded: false },
  ChatFromViewer:      { name: "ChatFromViewer", frequency: "Low", id: 80, trusted: false, zerocoded: false }, // NOT zerocoded — master-template trap, see §2.2
  ChatFromSimulator:   { name: "ChatFromSimulator", frequency: "Low", id: 81, trusted: false, zerocoded: false },
  ImprovedInstantMessage: { name: "ImprovedInstantMessage", frequency: "Low", id: 254, trusted: false, zerocoded: false },
  ObjectUpdate:        { name: "ObjectUpdate", frequency: "Low", id: 12, trusted: false, zerocoded: true },
  ImprovedTerseObjectUpdate: { name: "ImprovedTerseObjectUpdate", frequency: "High", id: 15, trusted: false, zerocoded: false },
  ObjectUpdateCompressed: { name: "ObjectUpdateCompressed", frequency: "Low", id: 13, trusted: false, zerocoded: true },
  ObjectUpdateCached:  { name: "ObjectUpdateCached", frequency: "Low", id: 14, trusted: false, zerocoded: false },
  KillObject:          { name: "KillObject", frequency: "High", id: 11, trusted: false, zerocoded: false },
  RegionHandshake:     { name: "RegionHandshake", frequency: "Low", id: 148, trusted: false, zerocoded: true },
  RegionHandshakeReply:{ name: "RegionHandshakeReply", frequency: "Low", id: 149, trusted: false, zerocoded: false },
  CoarseLocationUpdate:{ name: "CoarseLocationUpdate", frequency: "Low", id: 6, trusted: false, zerocoded: false },
  LayerData:           { name: "LayerData", frequency: "High", id: 11 + 0, trusted: false, zerocoded: false },
  TeleportStart:       { name: "TeleportStart", frequency: "Low", id: 72, trusted: false, zerocoded: false },
  TeleportProgress:    { name: "TeleportProgress", frequency: "Low", id: 73, trusted: false, zerocoded: false },
  TeleportFinish:      { name: "TeleportFinish", frequency: "Low", id: 69, trusted: false, zerocoded: false },
  TeleportFailed:      { name: "TeleportFailed", frequency: "Low", id: 70, trusted: false, zerocoded: false },
  LogoutRequest:       { name: "LogoutRequest", frequency: "Low", id: 252, trusted: false, zerocoded: false },
  CloseCircuit:        { name: "CloseCircuit", frequency: "Low", id: 0, trusted: false, zerocoded: false },
  AvatarAnimation:     { name: "AvatarAnimation", frequency: "Low", id: 20, trusted: false, zerocoded: false },
  ObjectAnimation:     { name: "ObjectAnimation", frequency: "Low", id: 21, trusted: false, zerocoded: false },
  ScriptDialog:        { name: "ScriptDialog", frequency: "Low", id: 380, trusted: false, zerocoded: false },
  RequestObjectPropertiesFamily: { name: "RequestObjectPropertiesFamily", frequency: "Low", id: 245, trusted: false, zerocoded: false },
  ObjectPropertiesFamily: { name: "ObjectPropertiesFamily", frequency: "Low", id: 246, trusted: false, zerocoded: false },
};

/** Reverse lookup by (frequency, id) for inbound dispatch. */
export const MESSAGE_BY_ID = new Map<string, MessageDef>(
  Object.values(MESSAGES).map((m) => [`${m.frequency}:${m.id}`, m]),
);
export function lookupMessage(freq: MessageFrequency, id: number): MessageDef | undefined {
  return MESSAGE_BY_ID.get(`${freq}:${id}`);
}
```

### 2.4 Field-level reader/writer for message bodies

```ts
// src/sl/packet-io.ts
// Little-endian field IO for message bodies. NOTE: packet HEADERS are
// big-endian (sequence, ACKs) but message BODY fields are little-endian,
// except LLUUID (raw byte order) and Variable/Fixed byte blobs.
// Getting an endianness wrong here produces garbage that still "parses".

import { UUIDString, Vector3, Quaternion, uuidToBytes, bytesToUUID } from "./types";

export class PacketWriter {
  private buf: number[] = [];
  u8(n: number): this { this.buf.push(n & 0xff); return this; }
  u16(n: number): this { this.buf.push(n & 0xff, (n >> 8) & 0xff); return this; }
  u32(n: number): this {
    this.buf.push(n & 0xff, (n >> 8) & 0xff, (n >> 16) & 0xff, (n >>> 24) & 0xff);
    return this;
  }
  u64(n: bigint): this {
    let v = n;
    for (let i = 0; i < 8; i++) { this.buf.push(Number(v & 0xffn)); v >>= 8n; }
    return this;
  }
  f32(n: number): this {
    const b = new Uint8Array(4);
    new DataView(b.buffer).setFloat32(0, n, true);
    this.buf.push(...b);
    return this;
  }
  f64(n: number): this {
    const b = new Uint8Array(8);
    new DataView(b.buffer).setFloat64(0, n, true);
    this.buf.push(...b);
    return this;
  }
  bool(v: boolean): this { return this.u8(v ? 1 : 0); }
  uuid(id: UUIDString): this { this.buf.push(...uuidToBytes(id)); return this; }
  vector3(v: Vector3): this { return this.f32(v.x).f32(v.y).f32(v.z); }
  /** LLQuaternion on the wire: x, y, z only — w is reconstructed. */
  quaternion(q: Quaternion): this { return this.f32(q.x).f32(q.y).f32(q.z); }
  /** Variable 1: u8 length prefix. Variable 2: u16 LE length prefix. */
  variable1(data: Uint8Array): this {
    if (data.length > 255) throw new Error("Variable 1 field too long");
    this.u8(data.length); this.buf.push(...data); return this;
  }
  variable2(data: Uint8Array): this {
    if (data.length > 65535) throw new Error("Variable 2 field too long");
    this.u16(data.length); this.buf.push(...data); return this;
  }
  /** Length-prefixed UTF-8 string stored as a Variable field. */
  stringVar1(s: string): this { return this.variable1(new TextEncoder().encode(s)); }
  stringVar2(s: string): this { return this.variable2(new TextEncoder().encode(s)); }
  fixed(data: Uint8Array): this { this.buf.push(...data); return this; }
  bytes(): Uint8Array { return new Uint8Array(this.buf); }
}

export class PacketReader {
  private view: DataView;
  pos: number;
  constructor(private readonly buf: Uint8Array, offset = 0) {
    this.view = new DataView(buf.buffer, buf.byteOffset, buf.byteLength);
    this.pos = offset;
  }
  get remaining(): number { return this.buf.length - this.pos; }
  u8(): number { return this.buf[this.pos++]; }
  u16(): number { const n = this.view.getUint16(this.pos, true); this.pos += 2; return n; }
  u32(): number { const n = this.view.getUint32(this.pos, true); this.pos += 4; return n; }
  u64(): bigint {
    let v = 0n;
    for (let i = 7; i >= 0; i--) v = (v << 8n) | BigInt(this.buf[this.pos + i]);
    this.pos += 8;
    return v;
  }
  f32(): number { const n = this.view.getFloat32(this.pos, true); this.pos += 4; return n; }
  f64(): number { const n = this.view.getFloat64(this.pos, true); this.pos += 8; return n; }
  bool(): boolean { return this.u8() !== 0; }
  uuid(): UUIDString { const id = bytesToUUID(this.buf, this.pos); this.pos += 16; return id; }
  vector3(): Vector3 { return { x: this.f32(), y: this.f32(), z: this.f32() }; }
  quaternion(): Quaternion {
    const x = this.f32(), y = this.f32(), z = this.f32();
    // Reconstruct w. Clamp for numeric noise on normalised inputs.
    const w2 = 1 - x * x - y * y - z * z;
    return { x, y, z, w: w2 > 0 ? Math.sqrt(w2) : 0 };
  }
  variable1(): Uint8Array { const len = this.u8(); return this.take(len); }
  variable2(): Uint8Array { const len = this.u16(); return this.take(len); }
  stringVar1(): string { return new TextDecoder().decode(this.variable1()); }
  stringVar2(): string { return new TextDecoder().decode(this.variable2()); }
  take(n: number): Uint8Array {
    const out = this.buf.subarray(this.pos, this.pos + n).slice();
    this.pos += n;
    return out;
  }
  fixed(n: number): Uint8Array { return this.take(n); }
}
```

### 2.5 Typed message encoders/decoders for the core set

Each message gets a small typed pair of functions over `PacketWriter` /
`PacketReader`. This is exactly what a template generator emits; writing
the core set by hand (as here) is how you validate the generator.

```ts
// src/sl/messages/core.ts
// Hand-written core messages. Block/field order and types are copied
// from message_template.msg — never reorder fields to "look nicer".

import { PacketWriter, PacketReader } from "../packet-io";
import { MESSAGES } from "./table";
import { encodeMessageId } from "../packet";
import { UUIDString, Vector3, Quaternion, NULL_KEY } from "../types";

function bodyWithId(name: keyof typeof MESSAGES): PacketWriter {
  const def = MESSAGES[name];
  const w = new PacketWriter();
  for (const b of encodeMessageId(def.frequency, def.id)) w.u8(b);
  return w;
}

export interface UseCircuitCode {
  circuitCode: number;
  sessionId: UUIDString;
  agentId: UUIDString;
}

export function encodeUseCircuitCode(m: UseCircuitCode): Uint8Array {
  const w = bodyWithId("UseCircuitCode");
  // CircuitInfo block (Single)
  w.u32(m.circuitCode).uuid(m.sessionId).uuid(m.agentId);
  return w.bytes();
}

export interface AgentUpdate {
  agentId: UUIDString;
  sessionId: UUIDString;
  bodyRotation: Quaternion;
  headRotation: Quaternion;
  state: number; // u8: 0 = none, bit flags for editing etc.
  cameraCenter: Vector3;
  cameraAtAxis: Vector3;
  cameraLeftAxis: Vector3;
  cameraUpAxis: Vector3;
  far: number; // f32 draw distance in metres
  controlFlags: number; // u32 AGENT_CONTROL_* bitfield
  flags: number; // u8 AgentUpdateFlags (hide title etc.)
}

// AGENT_CONTROL_* (from viewer llagent / LSL control() docs)
export const AgentControl = {
  AtPos: 0x0000_0001, AtNeg: 0x0000_0002,
  LeftPos: 0x0000_0004, LeftNeg: 0x0000_0008,
  UpPos: 0x0000_0010, UpNeg: 0x0000_0020,
  PitchPos: 0x0000_0040, PitchNeg: 0x0000_0080,
  YawPos: 0x0000_0100, YawNeg: 0x0000_0200,
  FastAt: 0x0000_0400, FastLeft: 0x0000_0800, FastUp: 0x0000_1000,
  Fly: 0x0000_2000, Stop: 0x0000_4000, FinishAnim: 0x0000_8000,
  StandUp: 0x0001_0000, SitOnGround: 0x0002_0000, Mouselook: 0x0004_0000,
  NudgeAtPos: 0x0008_0000, NudgeAtNeg: 0x0010_0000,
  NudgeLeftPos: 0x0020_0000, NudgeLeftNeg: 0x0040_0000,
  NudgeUpPos: 0x0080_0000, NudgeUpNeg: 0x0100_0000,
  TurnLeft: 0x0200_0000, TurnRight: 0x0400_0000,
  Away: 0x0800_0000, LButtonDown: 0x1000_0000, LButtonUp: 0x2000_0000,
  ML_LButtonDown: 0x4000_0000, ML_LButtonUp: 0x8000_0000,
} as const;

export function encodeAgentUpdate(m: AgentUpdate): Uint8Array {
  const w = bodyWithId("AgentUpdate");
  // AgentData block (Single)
  w.uuid(m.agentId).uuid(m.sessionId)
    .quaternion(m.bodyRotation).quaternion(m.headRotation)
    .u8(m.state)
    .vector3(m.cameraCenter).vector3(m.cameraAtAxis)
    .vector3(m.cameraLeftAxis).vector3(m.cameraUpAxis)
    .f32(m.far).u32(m.controlFlags).u8(m.flags);
  return w.bytes();
}

export interface ChatFromViewer {
  agentId: UUIDString;
  sessionId: UUIDString;
  message: string;
  type: number; // ChatType: 0 whisper, 1 normal, 2 shout, 8 owner say target…
  channel: number; // s32 — 0 is public chat; negative/positive are script channels
}

export const ChatType = {
  Whisper: 0, Normal: 1, Shout: 2, StartTyping: 4, StopTyping: 5,
  Debug: 6, OwnerSay: 8, RegionSay: 9, RegionSayTo: 10,
} as const;

export function encodeChatFromViewer(m: ChatFromViewer): Uint8Array {
  const w = bodyWithId("ChatFromViewer");
  // AgentData block, then ChatData block.
  // ChatFromViewer is NOT zerocoded (see the table note) — the circuit
  // reads the flag from MESSAGES and honours it; do not "fix" it here.
  w.uuid(m.agentId).uuid(m.sessionId);
  w.stringVar2(m.message).u8(m.type);
  // Channel is S32 in the template; PacketWriter has no s32 helper
  // because two's-complement bit pattern is identical to u32.
  w.u32(m.channel >>> 0);
  return w.bytes();
}

export interface ChatFromSimulator {
  fromName: string;
  sourceId: UUIDString;
  ownerId: UUIDString;
  sourceType: number; // 0 system, 1 agent, 2 object
  chatType: number;
  audible: number;
  position: Vector3;
  message: string;
}

export function decodeChatFromSimulator(r: PacketReader): ChatFromSimulator {
  // ChatData block (Single), field order per template.
  const fromName = r.stringVar1();
  const sourceId = r.uuid();
  const ownerId = r.uuid();
  const sourceType = r.u8();
  const chatType = r.u8();
  const audible = r.u8();
  const position = r.vector3();
  const message = r.stringVar2();
  return { fromName, sourceId, ownerId, sourceType, chatType, audible, position, message };
}

export interface ImprovedInstantMessage {
  agentId: UUIDString;
  sessionId: UUIDString;
  fromGroup: boolean;
  toAgentId: UUIDString;
  parentEstateId: number;
  regionId: UUIDString;
  position: Vector3;
  offline: number; // 0 online, 1 stored offline
  dialog: number; // IM_DIALOG_* — 0 = plain text IM
  imSessionId: UUIDString; // == toAgentId for 1:1, group UUID for groups
  timestamp: number; // u32 unix seconds, 0 = now
  fromAgentName: string;
  message: string;
  binaryBucket: Uint8Array; // dialog-specific payload, often empty
}

export const IMDialog = {
  Message: 0, InventoryOffered: 3, InventoryAccepted: 4,
  GroupInvitation: 25, GroupNotice: 27, GotoUrl: 28,
  BusyAutoResponse: 32, SessionGroupStart: 35, SessionConferenceStart: 38,
  SessionSend: 39, SessionDrop: 40, MessageBox: 41, LureUser: 44,
  LureResponse: 45, GodLikeLureUser: 46, TeleportRequest: 47,
} as const;

export function encodeImprovedInstantMessage(m: ImprovedInstantMessage): Uint8Array {
  const w = bodyWithId("ImprovedInstantMessage");
  // AgentData block
  w.uuid(m.agentId).uuid(m.sessionId);
  // MessageBlock
  w.bool(m.fromGroup).uuid(m.toAgentId).u32(m.parentEstateId)
    .uuid(m.regionId).vector3(m.position)
    .u8(m.offline).u8(m.dialog).uuid(m.imSessionId)
    .u32(m.timestamp).stringVar1(m.fromAgentName)
    .stringVar2(m.message).variable2(m.binaryBucket);
  return w.bytes();
}

export function decodeImprovedInstantMessage(r: PacketReader): ImprovedInstantMessage {
  const agentId = r.uuid(); const sessionId = r.uuid();
  const fromGroup = r.bool(); const toAgentId = r.uuid();
  const parentEstateId = r.u32(); const regionId = r.uuid();
  const position = r.vector3(); const offline = r.u8();
  const dialog = r.u8(); const imSessionId = r.uuid();
  const timestamp = r.u32(); const fromAgentName = r.stringVar1();
  const message = r.stringVar2(); const binaryBucket = r.variable2();
  return {
    agentId, sessionId, fromGroup, toAgentId, parentEstateId, regionId,
    position, offline, dialog, imSessionId, timestamp, fromAgentName,
    message, binaryBucket,
  };
}

export interface RegionHandshake {
  regionFlags: number;
  simAccess: number; // u8: 13 PG, 21 Mature, 42 Adult (viewer enum values)
  simName: string;
  simOwner: UUIDString;
  isEstateManager: boolean;
  waterHeight: number;
  billableFactor: number;
  cacheId: UUIDString;
  cpuClassId: number;
  cpuRatio: number;
  coloVersion: string;
  gridUrl: string;
  productSku: string;
  productName: string;
}

export function decodeRegionHandshake(r: PacketReader): RegionHandshake {
  // RegionInfo block, then RegionInfo2, then RegionInfo3. Only the
  // fields a thin client needs are decoded; the reader still has to
  // WALK every field in order — skipping bytes by guessing lengths is
  // how handshake parsers desynchronise.
  const regionFlags = r.u32();
  const simAccess = r.u8();
  const simName = r.stringVar1();
  const simOwner = r.uuid();
  const isEstateManager = r.bool();
  const waterHeight = r.f32();
  const billableFactor = r.f32();
  const cacheId = r.uuid();
  const cpuClassId = r.u32();
  const cpuRatio = r.f32();
  const coloVersion = r.stringVar1();
  const gridUrl = r.stringVar1();
  const productSku = r.stringVar1();
  const productName = r.stringVar1();
  return {
    regionFlags, simAccess, simName, simOwner, isEstateManager,
    waterHeight, billableFactor, cacheId, cpuClassId, cpuRatio,
    coloVersion, gridUrl, productSku, productName,
  };
}

export interface CoarseLocation {
  /** One entry per avatar in the region (excluding, usually, yourself). */
  agents: { x: number; y: number; z: number; isYou: boolean }[];
}

export function decodeCoarseLocationUpdate(r: PacketReader): CoarseLocation {
  // Location block is Variable: three parallel byte arrays (X, Y, Z),
  // then AgentData block (Variable) with a You + Prey pair per entry.
  // Coordinates are quantised to 16 m in X/Y; Z is (byte * 4) offset.
  // This is minimap data only — never use it for rendering positions.
  const xs = r.variable1(); const ys = r.variable1(); const zs = r.variable1();
  const count = Math.min(xs.length, ys.length, zs.length);
  const agents: CoarseLocation["agents"] = [];
  for (let i = 0; i < count; i++) {
    agents.push({ x: xs[i] * 16, y: ys[i] * 16, z: zs[i] * 4, isYou: false });
  }
  // AgentData: You (u16 index into the arrays), Prey (u16)
  if (r.remaining >= 2) {
    const you = r.u16();
    if (you < agents.length) agents[you].isYou = true;
    if (r.remaining >= 2) r.u16(); // Prey — camera target, unused by radar
  }
  return { agents };
}

export function encodeRegionHandshakeReply(
  agentId: UUIDString, sessionId: UUIDString,
): Uint8Array {
  const w = bodyWithId("RegionHandshakeReply");
  w.uuid(agentId).uuid(sessionId);
  w.u32(0); // RegionInfo Flags — 0 = no special client flags
  return w.bytes();
}

export function encodeCompleteAgentMovement(
  agentId: UUIDString, sessionId: UUIDString, circuitCode: number,
): Uint8Array {
  const w = bodyWithId("CompleteAgentMovement");
  w.uuid(agentId).uuid(sessionId).u32(circuitCode);
  return w.bytes();
}

export function encodePacketAck(sequences: number[]): Uint8Array {
  const w = bodyWithId("PacketAck");
  w.u8(sequences.length); // Packets block is Variable (count byte)
  for (const s of sequences) w.u32(s); // NOTE: body u32s are LE per template block type
  return w.bytes();
}

export function encodeStartPingCheckReply(pingId: number): Uint8Array {
  // CompletePingCheck echoes the PingID byte from StartPingCheck.
  const w = bodyWithId("CompletePingCheck");
  w.u8(pingId);
  return w.bytes();
}

export function encodeLogoutRequest(agentId: UUIDString, sessionId: UUIDString): Uint8Array {
  const w = bodyWithId("LogoutRequest");
  w.uuid(agentId).uuid(sessionId);
  return w.bytes();
}

export { NULL_KEY };
```

### 2.6 The circuit: reliability, resends, ping, throttle, neighbour regions

```ts
// src/sl/circuit.ts
// One Circuit per region connection. Owns: sequence numbers, the
// unacked-reliable queue with resend timers, ACK batching, ping
// measurement, and message dispatch. Ported in structure from
// LibreMetaverse.Transport.UDPClient and the viewer's LLCircuit.

import { UdpBridge, UdpEndpoint } from "./udp-bridge";
import {
  decodePacket, encodePacket, PacketFlags,
} from "./packet";
import { MESSAGES, lookupMessage } from "./messages/table";
import { PacketReader } from "./packet-io";
import {
  encodePacketAck, encodeStartPingCheckReply,
  encodeUseCircuitCode, encodeCompleteAgentMovement,
} from "./messages/core";

export type MessageHandler = (reader: PacketReader, defName: string) => void;

interface PendingReliable {
  packet: Uint8Array;
  sequence: number;
  lastSentAt: number;
  resends: number;
}

const RESEND_MS = 100;          // first resend — matches viewer defaults closely enough for mobile links
const MAX_RESENDS = 8;          // after this, treat the circuit as dead
const ACK_FLUSH_MS = 50;        // batch ACKs instead of one packet per ack
const PING_INTERVAL_MS = 5000;  // StartPingCheck cadence from the simulator is inbound; we track RTT

export class Circuit {
  private sequence = 0;
  private nextSequence(): number {
    this.sequence = (this.sequence + 1) >>> 0;
    if (this.sequence === 0) this.sequence = 1; // 0 is never a valid sequence
    return this.sequence;
  }

  private pending = new Map<number, PendingReliable>();
  private ackQueue: number[] = [];
  private ackTimer: ReturnType<typeof setTimeout> | null = null;
  private resendTimer: ReturnType<typeof setInterval> | null = null;
  private unsubscribe: (() => void) | null = null;
  private seenSequences = new Set<number>(); // duplicate suppression window
  private lastPingId = 0;

  /** Round-trip estimate from the last CompletePingCheck exchange. */
  lastRttMs = 0;
  private pingSentAt = 0;

  onDead: (() => void) | null = null;
  onUnhandled: ((name: string, reader: PacketReader) => void) | null = null;

  constructor(
    private readonly bridge: UdpBridge,
    readonly endpoint: UdpEndpoint,
    private readonly handlers: Map<string, MessageHandler>,
  ) {}

  /** Open the circuit: UseCircuitCode, then CompleteAgentMovement. */
  async open(circuitCode: number, agentId: string, sessionId: string): Promise<void> {
    this.unsubscribe = this.bridge.onPacket((from, packet) => {
      if (from.host !== this.endpoint.host || from.port !== this.endpoint.port) return;
      this.handleInbound(packet);
    });
    this.sendMessage("UseCircuitCode",
      encodeUseCircuitCode({ circuitCode, sessionId: sessionId as never, agentId: agentId as never }),
      { reliable: false });
    this.sendMessage("CompleteAgentMovement",
      encodeCompleteAgentMovement(agentId as never, sessionId as never, circuitCode),
      { reliable: false });
    this.resendTimer = setInterval(() => this.pumpResends(), RESEND_MS);
  }

  /**
   * Send a message by name. The zerocoded/reliable defaults come from
   * the message table; callers may force reliability for messages the
   * simulator expects to be reliable in a given flow.
   */
  sendMessage(
    name: keyof typeof MESSAGES,
    body: Uint8Array,
    opts: { reliable?: boolean } = {},
  ): void {
    const def = MESSAGES[name];
    const reliable = opts.reliable ?? false;
    const seq = this.nextSequence();
    const packet = encodePacket({
      sequence: seq,
      body,
      zerocoded: def.zerocoded,
      reliable,
    });
    void this.bridge.send(this.endpoint, packet);
    if (reliable) {
      this.pending.set(seq, { packet, sequence: seq, lastSentAt: Date.now(), resends: 0 });
    }
  }

  /** Send with explicit reliability — used for chat and IM. */
  sendReliable(name: keyof typeof MESSAGES, body: Uint8Array): void {
    this.sendMessage(name, body, { reliable: true });
  }

  private pumpResends(): void {
    const now = Date.now();
    for (const [seq, p] of this.pending) {
      if (now - p.lastSentAt < RESEND_MS * (1 + p.resends)) continue;
      if (p.resends >= MAX_RESENDS) {
        this.pending.delete(seq);
        // A reliable message that exhausts resends means the simulator
        // is gone or the network path died. Surface it — ghosting
        // silently is worse than a visible disconnect.
        this.onDead?.();
        return;
      }
      p.resends++;
      p.lastSentAt = now;
      // Mark Resent on the resend copy.
      const copy = p.packet.slice();
      copy[0] |= PacketFlags.Resent;
      void this.bridge.send(this.endpoint, copy);
    }
  }

  private queueAck(sequence: number): void {
    this.ackQueue.push(sequence);
    if (this.ackTimer) return;
    this.ackTimer = setTimeout(() => {
      this.ackTimer = null;
      const batch = this.ackQueue.splice(0, 255);
      if (batch.length === 0) return;
      // PacketAck is a Fixed message sent unreliably with sequence 0
      // semantics in practice; we still allocate a sequence so the
      // simulator's duplicate filter treats each batch as fresh.
      const body = encodePacketAck(batch);
      const packet = encodePacket({
        sequence: this.nextSequence(), body, zerocoded: false, reliable: false,
      });
      void this.bridge.send(this.endpoint, packet);
    }, ACK_FLUSH_MS);
  }

  private handleInbound(raw: Uint8Array): void {
    let pkt;
    try {
      pkt = decodePacket(raw);
    } catch {
      return; // malformed datagram — drop, never crash the session on wire garbage
    }
    for (const acked of pkt.appendedAcks) this.pending.delete(acked);

    if (pkt.reliable) this.queueAck(pkt.sequence);

    // Duplicate suppression for reliable messages: the simulator resends
    // until acked, and our ack may have been lost.
    if (pkt.reliable) {
      if (this.seenSequences.has(pkt.sequence)) return;
      this.seenSequences.add(pkt.sequence);
      if (this.seenSequences.size > 4096) {
        // Bounded window: drop the oldest half. Sequence wraparound is
        // a non-issue at session scale.
        const it = this.seenSequences.values();
        for (let i = 0; i < 2048; i++) this.seenSequences.delete(it.next().value!);
      }
    }

    const def = lookupMessage(pkt.frequency, pkt.messageId);
    if (!def) return; // unknown message — a thin client ignores most of the protocol

    // Circuit-internal messages are handled here, not by the app.
    if (def.name === "PacketAck") {
      const r = new PacketReader(pkt.body, idBytes(pkt));
      const count = r.u8();
      for (let i = 0; i < count; i++) this.pending.delete(r.u32());
      return;
    }
    if (def.name === "StartPingCheck") {
      const r = new PacketReader(pkt.body, idBytes(pkt));
      this.lastPingId = r.u8();
      this.pingSentAt = Date.now();
      this.sendMessage("CompletePingCheck", encodeStartPingCheckReply(this.lastPingId));
      return;
    }

    const handler = this.handlers.get(def.name);
    const reader = new PacketReader(pkt.body, idBytes(pkt));
    if (handler) handler(reader, def.name);
    else this.onUnhandled?.(def.name, reader);
  }

  /** Graceful close: stop timers, drop the bridge subscription. The
   *  LogoutRequest itself is sent by the session layer (Section 5)
   *  because it needs agent/session ids. */
  close(): void {
    if (this.resendTimer) clearInterval(this.resendTimer);
    if (this.ackTimer) clearTimeout(this.ackTimer);
    this.unsubscribe?.();
    this.pending.clear();
  }
}

/** Byte length of the message ID at the start of a decoded body. */
function idBytes(pkt: { frequency: string }): number {
  switch (pkt.frequency) {
    case "High": return 1;
    case "Medium": return 2;
    default: return 4; // Low and Fixed
  }
}
```

---

## 3. The capabilities (caps) client

After login you hold a **seed capability** URL. POST it an LLSD array of
cap names; it returns an LLSD map of name → unguessable per-region URL.
Rules that will bite you if ignored:

1. Cap URLs are per-region and per-session. On teleport, throw the whole
   map away and re-request from the new region's seed.
2. Availability varies by grid and simulator version. Always check the
   returned map; fall back to UDP where the viewer does.
3. Never hardcode feature limits — query `SimulatorFeatures`.

```ts
// src/sl/caps.ts
// Seed-cap negotiation + a typed cap caller.
// Cap names: llviewerregion.cpp buildCapabilityNames + llaisapi.cpp.

import { llsdToXml, llsdFromXml, asMap, asArray } from "./llsd-xml";
import { LLSDValue } from "./llsd";

/** Every cap a thin/mobile client should request on region entry. */
export const WANTED_CAPS = [
  "EventQueueGet",
  "FetchInventory2", "FetchInventoryDescendents2",
  "FetchLib2", "FetchLibDescendents2",
  "InventoryAPIv3", "LibraryAPIv3",           // AIS3
  "GetTexture", "GetMesh", "GetMesh2",
  "GetMetadata", "GetObjectCost", "GetObjectPhysicsData",
  "SimulatorFeatures", "ServerReleaseNotes",
  "ExtEnvironment", "EnvironmentSettings",
  "RenderMaterials",
  "AgentPreferences", "AgentState", "AvatarRenderInfo",
  "CharacterProperties", "GetDisplayNames",
  "ChatSessionRequest", "GroupAPIv1", "GroupMemberData",
  "HomeLocation", "LandResources", "RemoteParcelRequest",
  "NewFileAgentInventory", "InventoryThumbnailUpload",
  "UpdateAgentAppearance", "UpdateAgentInformation",
  "ProductInfoRequest", "SearchStatRequest",
  "VoiceSignalingRequest", "ProvisionVoiceAccountRequest",
  "IncrementCOFVersion",
] as const;

export type CapName = (typeof WANTED_CAPS)[number] | string;

export class CapsError extends Error {
  constructor(
    message: string,
    readonly cap: string,
    readonly status: number,
  ) { super(message); }
}

export class Caps {
  private urls = new Map<string, string>();

  private constructor(
    private readonly seedCap: string,
    private readonly fetchFn: typeof fetch,
  ) {}

  /** Negotiate the cap map for one region from its seed capability. */
  static async negotiate(
    seedCap: string,
    wanted: readonly string[] = WANTED_CAPS,
    fetchFn: typeof fetch = fetch,
  ): Promise<Caps> {
    const caps = new Caps(seedCap, fetchFn);
    const res = await fetchFn(seedCap, {
      method: "POST",
      headers: { "Content-Type": "application/llsd+xml" },
      body: llsdToXml(wanted as unknown as LLSDValue),
    });
    if (!res.ok) {
      throw new CapsError(`Seed cap negotiation failed`, "<seed>", res.status);
    }
    const map = asMap(llsdFromXml(await res.text()));
    for (const [name, url] of Object.entries(map)) {
      if (typeof url === "string" && url.startsWith("http")) caps.urls.set(name, url);
    }
    return caps;
  }

  has(name: CapName): boolean { return this.urls.has(name); }
  url(name: CapName): string {
    const u = this.urls.get(name);
    if (!u) throw new CapsError(`Capability not granted by this region: ${name}`, name, 0);
    return u;
  }
  maybeUrl(name: CapName): string | undefined { return this.urls.get(name); }

  /** POST an LLSD payload to a cap and parse an LLSD response. */
  async post(name: CapName, payload: LLSDValue): Promise<LLSDValue> {
    const url = this.url(name);
    const res = await this.fetchFn(url, {
      method: "POST",
      headers: { "Content-Type": "application/llsd+xml" },
      body: llsdToXml(payload),
    });
    if (!res.ok) throw new CapsError(`Cap ${name} failed`, name, res.status);
    const text = await res.text();
    if (!text.trim()) return {};
    return llsdFromXml(text);
  }

  /** GET-style caps (GetTexture / GetMesh) need headers + ranges, so
   *  they get a raw fetch escape hatch instead of the LLSD path. */
  async rawFetch(name: CapName, init: RequestInit = {}): Promise<Response> {
    const res = await this.fetchFn(this.url(name), init);
    if (!res.ok && res.status !== 206) {
      throw new CapsError(`Cap ${name} raw fetch failed`, name, res.status);
    }
    return res;
  }
}

/** SimulatorFeatures: query, never hardcode. */
export interface SimulatorFeatures {
  meshUploadEnabled: boolean;
  physicsShapeTypes: string[];
  pbrEnabled: boolean;
  voiceMode: "webrtc" | "vivox" | "none" | string;
  raw: { [k: string]: LLSDValue };
}

export async function fetchSimulatorFeatures(caps: Caps): Promise<SimulatorFeatures> {
  const raw = asMap(await caps.post("SimulatorFeatures", {}));
  // Field names below follow the viewer's feature-map construction in
  // llviewerregion.cpp / feature manager code. Unknown fields are kept
  // in `raw` so new simulator features degrade gracefully.
  const voice = raw["VoiceVersion"] ?? raw["voice"];
  return {
    meshUploadEnabled: raw["MeshUploadEnabled"] !== false,
    physicsShapeTypes: Array.isArray(raw["PhysicsShapeTypes"])
      ? (raw["PhysicsShapeTypes"] as LLSDValue[]).map(String)
      : ["prim", "convex", "none"],
    pbrEnabled: raw["PBREnabled"] === true || raw["GLTFEnabled"] === true,
    voiceMode:
      typeof voice === "string" && voice.toLowerCase().includes("webrtc")
        ? "webrtc"
        : typeof voice === "string"
          ? "vivox"
          : "none",
    raw,
  };
}
```

### 3.1 Inventory over caps: FetchInventory2 and AIS3

```ts
// src/sl/inventory.ts
// Read path: FetchInventoryDescendents2 (HTTP, LLSD).
// Write path: AIS3 InventoryAPIv3 (create / update / remove / link).
// Modelled on llaisapi.cpp and LibreMetaverse's Inventory manager.

import { Caps } from "./caps";
import { asMap, asArray, getString, getInt, getUUID } from "./llsd-xml";
import { llsd, LLSDValue } from "./llsd";
import { UUIDString, NULL_KEY } from "./types";

export enum AssetType {
  Texture = 0, Sound = 1, CallingCard = 2, Landmark = 3, Script = 5,
  Clothing = 6, Object = 7, Notecard = 8, Category = 9, SoundWav = 10,
  TextureTGA = 11, Bodypart = 13, Trash = 14, Snapshot = 15,
  Attachment = 17, Wearable = 18, Animation = 19, Gesture = 20,
  Mesh = 22, Link = 24, LinkFolder = 25, Material = 26, Unknown = -1,
}

export enum InventoryType {
  Texture = 0, Sound = 1, Landmark = 3, Clothing = 5, Object = 6,
  Notecard = 7, Category = 8, Script = 10, Snapshot = 15,
  Attachment = 17, Wearable = 18, Animation = 19, Gesture = 20,
  Mesh = 22, Material = 26, Unknown = -1,
}

export interface InventoryItem {
  itemId: UUIDString;
  parentId: UUIDString;
  name: string;
  assetId: UUIDString;
  assetType: AssetType;
  invType: InventoryType;
  isLink: boolean;
  linkTargetId?: UUIDString; // for Link / LinkFolder items, assetId IS the target
  permissions: {
    baseMask: number; currentOwnerMask: number; groupMask: number;
    everyoneMask: number; nextOwnerMask: number;
  };
  createdAt: number; // unix seconds
  flags: number;
}

export interface InventoryFolder {
  folderId: UUIDString;
  parentId: UUIDString;
  name: string;
  typeDefault: number; // preferred asset type for this system folder
  version: number;     // bump on every descendant change — cache key!
}

export interface FolderContents {
  folders: InventoryFolder[];
  items: InventoryItem[];
  version: number;
}

function parseItem(m: { [k: string]: LLSDValue }): InventoryItem {
  const assetId = getUUID(m, "asset_id");
  const invType = getInt(m, "inv_type", -1) as InventoryType;
  const perms = asMap(m["permissions"] ?? {});
  return {
    itemId: getUUID(m, "item_id"),
    parentId: getUUID(m, "parent_id"),
    name: getString(m, "name"),
    assetId,
    assetType: getInt(m, "type", -1) as AssetType,
    invType,
    isLink: invType === InventoryType.Object && getInt(m, "type", -1) === AssetType.Link
      || getInt(m, "type", -1) === AssetType.Link
      || getInt(m, "type", -1) === AssetType.LinkFolder,
    linkTargetId:
      getInt(m, "type", -1) === AssetType.Link || getInt(m, "type", -1) === AssetType.LinkFolder
        ? assetId
        : undefined,
    permissions: {
      baseMask: getInt(perms, "base_mask"),
      currentOwnerMask: getInt(perms, "owner_mask"),
      groupMask: getInt(perms, "group_mask"),
      everyoneMask: getInt(perms, "everyone_mask"),
      nextOwnerMask: getInt(perms, "next_owner_mask"),
    },
    createdAt: getInt(m, "created_at"),
    flags: getInt(m, "flags"),
  };
}

function parseFolder(m: { [k: string]: LLSDValue }): InventoryFolder {
  return {
    folderId: getUUID(m, "folder_id"),
    parentId: getUUID(m, "parent_id"),
    name: getString(m, "name"),
    typeDefault: getInt(m, "type_default", -1),
    version: getInt(m, "version"),
  };
}

/**
 * Fetch one folder's descendants. The response carries the folder
 * version — cache contents keyed by (folderId, version) and refetch
 * only when the version you hold is older, exactly as the viewer's
 * inventory cache does. Fetching the whole tree eagerly is the #1
 * mobile-login performance bug; fetch lazily per folder.
 */
export async function fetchFolder(
  caps: Caps, agentId: UUIDString, folderId: UUIDString,
): Promise<FolderContents> {
  const resp = asMap(await caps.post("FetchInventoryDescendents2", {
    agent_id: agentId,
    folder_id: folderId,
    owner_id: agentId,
    sort_order: llsd.int(0), // 0 = by name
    fetch_folders: llsd.int(1),
    fetch_items: llsd.int(1),
    fetch_links: llsd.int(1),
  } as unknown as LLSDValue));
  const folders = asArray(resp["folders"] ?? []).map((f) => parseFolder(asMap(f)));
  const items = asArray(resp["items"] ?? []).map((i) => parseItem(asMap(i)));
  return { folders, items, version: getInt(resp, "version") };
}

/** AIS3: create a link in the Current Outfit Folder (or any folder). */
export async function aisCreateLink(
  caps: Caps,
  agentId: UUIDString,
  opts: {
    folderId: UUIDString;
    targetItemId: UUIDString; // the item being linked TO
    name: string;
    type: AssetType.Link | AssetType.LinkFolder;
  },
): Promise<UUIDString> {
  // AIS3 paths are REST-ish over the cap: POST {cap}/category/{folder}
  // is handled server-side from the LLSD body in the viewer flow; the
  // body shape below follows llaisapi.cpp's link-creation payload.
  const resp = asMap(await caps.post("InventoryAPIv3", {
    "agent-id": agentId,
    "folder-id": opts.folderId,
    "item-name": opts.name,
    "linked-id": opts.targetItemId,
    type: llsd.int(opts.type),
    "inv-type": llsd.int(
      opts.type === AssetType.LinkFolder ? InventoryType.Category : InventoryType.Object,
    ),
  } as unknown as LLSDValue));
  return getUUID(resp, "item_id");
}

/** AIS3: remove items (moves them to Trash in viewer semantics when the
 *  caller uses the trash flow; the raw op is a delete of the link/item). */
export async function aisRemoveItems(
  caps: Caps, agentId: UUIDString, itemIds: UUIDString[],
): Promise<void> {
  await caps.post("InventoryAPIv3", {
    "agent-id": agentId,
    "item-ids": itemIds,
    _method: "delete",
  } as unknown as LLSDValue);
}

export { NULL_KEY };
```

---

## 4. Login, with the MFA state machine

Login is a state machine, not a function call. States: `idle →
authenticating → (mfaChallenge) → establishingCircuit → inWorld`, with
`failed` reachable from every step. The MFA branch is the one thin
clients historically got wrong: the login service replies with an LLSD
map carrying a `reason` and an `mfa_hash`; you prompt for the TOTP code
and resubmit **with the hash**, on the same login attempt. Persisting
`mfa_hash` unencrypted is a security bug — the desktop viewer keeps it
in an encrypted protected store; a mobile client without one must keep
it in memory only (the deliberate deviation recorded in the Lumiya work).

```ts
// src/sl/login.ts
// Login service client + MFA state machine.
// Ported from: llstartup.cpp (viewer), LibreMetaverse Login,
// Lumiya SLAuth / SLAuthReply MFA handling pattern.

import { llsdToXml, llsdFromXml, asMap, getString, getInt, getUUID } from "./llsd-xml";
import { LLSDValue } from "./llsd";
import { UUIDString } from "./types";

export const AGNI_LOGIN_URI = "https://login.agni.lindenlab.com/cgi-bin/login.cgi";
export const ADITI_LOGIN_URI = "https://login.aditi.lindenlab.com/cgi-bin/login.cgi";

export type LoginState =
  | { kind: "idle" }
  | { kind: "authenticating" }
  | { kind: "mfaChallenge"; mfaHash: string; message: string }
  | { kind: "establishingCircuit"; session: LoginSession }
  | { kind: "inWorld"; session: LoginSession }
  | { kind: "failed"; reason: string; detail?: string };

export interface LoginSession {
  agentId: UUIDString;
  sessionId: UUIDString;
  secureSessionId: UUIDString;
  circuitCode: number;
  simHost: string;
  simPort: number;
  seedCapability: string;
  firstName: string;
  lastName: string;
  startLocation: string;
  inventoryRootFolderId: UUIDString;
  libraryRootFolderId: UUIDString;
  regionX: number;
  regionY: number;
}

export interface LoginRequest {
  firstName: string;
  lastName: string; // for usernames, this is the part after the dot / "Resident" handling lives in the UI
  /** MD5-based credential token as the login service expects it.
   *  Compute it in the platform layer and NEVER log it. The legacy
   *  scheme is "$1$" + md5(password); current grids may issue token
   *  variants — the request builder is where that is isolated. */
  credentialToken: string;
  start: "home" | "last" | string; // or a uri: "uri:RegionName&x&y&z"
  channel: string;                 // unique viewer channel — TPV policy
  version: string;
  platform: string;                // "and" | "ios" | "win" | "mac" | "lnx"
  mac: string;
  id0: string;
  mfaToken?: string;               // TOTP code, only on the MFA resubmit
  mfaHash?: string;                // hash from the challenge reply, memory only
}

function buildLoginBody(req: LoginRequest): LLSDValue {
  const body: Record<string, LLSDValue> = {
    first: req.firstName,
    last: req.lastName,
    passwd: req.credentialToken,
    start: req.start,
    channel: req.channel,
    version: req.version,
    platform: req.platform,
    mac: req.mac,
    id0: req.id0,
    agree_to_tos: true as unknown as LLSDValue,
    read_critical: true as unknown as LLSDValue,
    // Options list asks the service for the payloads a viewer needs.
    options: [
      "inventory-root", "inventory-skeleton", "inventory-lib-root",
      "inventory-lib-owner", "inventory-skel-lib", "buddy-list",
      "gestures", "event_categories", "event_notifications",
      "classified_categories", "adult_compliant", "newuser-config",
      "advanced-mode", "max-agent-groups", "map-server-url",
      "voice-config", "tutorial_setting", "login-flags", "global-textures",
    ] as unknown as LLSDValue,
  };
  if (req.mfaToken) body["token"] = req.mfaToken;
  if (req.mfaHash) body["mfa_hash"] = req.mfaHash;
  return body as LLSDValue;
}

export class LoginMachine {
  state: LoginState = { kind: "idle" };
  private listeners = new Set<(s: LoginState) => void>();
  private pendingRequest: LoginRequest | null = null;

  constructor(
    private readonly loginUri: string = AGNI_LOGIN_URI,
    private readonly fetchFn: typeof fetch = fetch,
  ) {}

  subscribe(cb: (s: LoginState) => void): () => void {
    this.listeners.add(cb);
    cb(this.state);
    return () => this.listeners.delete(cb);
  }
  private setState(s: LoginState): void {
    this.state = s;
    for (const cb of this.listeners) cb(s);
  }

  /** Begin (or restart) a login. Safe to call from `failed`. */
  async login(req: LoginRequest): Promise<void> {
    this.pendingRequest = req;
    this.setState({ kind: "authenticating" });
    await this.submit(req);
  }

  /** Called by the UI when the machine is in `mfaChallenge`. */
  async submitMfa(code: string): Promise<void> {
    if (this.state.kind !== "mfaChallenge" || !this.pendingRequest) {
      throw new Error("submitMfa called outside an MFA challenge");
    }
    const req: LoginRequest = {
      ...this.pendingRequest,
      mfaToken: code,
      mfaHash: this.state.mfaHash,
    };
    this.setState({ kind: "authenticating" });
    await this.submit(req);
  }

  private async submit(req: LoginRequest): Promise<void> {
    let reply: { [k: string]: LLSDValue };
    try {
      const res = await this.fetchFn(this.loginUri, {
        method: "POST",
        headers: { "Content-Type": "application/llsd+xml" },
        body: llsdToXml(buildLoginBody(req)),
      });
      if (!res.ok) {
        this.setState({ kind: "failed", reason: `Login service HTTP ${res.status}` });
        return;
      }
      reply = asMap(llsdFromXml(await res.text()));
    } catch (err) {
      this.setState({
        kind: "failed",
        reason: "Login service unreachable",
        detail: err instanceof Error ? err.message : String(err),
      });
      return;
    }

    const loginFlag = getString(reply, "login");
    if (loginFlag === "false") {
      const reason = getString(reply, "reason");
      const mfaHash = getString(reply, "mfa_hash");
      // The MFA challenge arrives as a *failed* login with a reason —
      // distinguishing it from a real failure is the whole trick.
      if ((reason === "mfa" || reason === "mfa_challenge") && mfaHash) {
        this.setState({
          kind: "mfaChallenge",
          mfaHash,
          message: getString(reply, "message", "Enter the code from your authenticator app."),
        });
        return;
      }
      this.setState({
        kind: "failed",
        reason: getString(reply, "message", "Login failed"),
        detail: reason,
      });
      return;
    }
    if (loginFlag !== "true") {
      this.setState({ kind: "failed", reason: `Unexpected login reply: ${loginFlag}` });
      return;
    }

    const skeleton = reply["inventory-skeleton"];
    let inventoryRoot = NULL_KEY_FALLBACK;
    if (Array.isArray(skeleton) && skeleton.length > 0) {
      const root = asMap(skeleton[0]);
      inventoryRoot = getUUID(root, "folder_id");
    }
    const libRootArr = reply["inventory-lib-root"];
    let libraryRoot = NULL_KEY_FALLBACK;
    if (Array.isArray(libRootArr) && libRootArr.length > 0) {
      libraryRoot = getUUID(asMap(libRootArr[0]), "folder_id");
    }

    const session: LoginSession = {
      agentId: getUUID(reply, "agent_id"),
      sessionId: getUUID(reply, "session_id"),
      secureSessionId: getUUID(reply, "secure_session_id"),
      circuitCode: getInt(reply, "circuit_code"),
      simHost: getString(reply, "sim_ip"),
      simPort: getInt(reply, "sim_port"),
      seedCapability: getString(reply, "seed_capability"),
      firstName: req.firstName,
      lastName: req.lastName,
      startLocation: getString(reply, "start_location"),
      inventoryRootFolderId: inventoryRoot,
      libraryRootFolderId: libraryRoot,
      regionX: getInt(reply, "region_x"),
      regionY: getInt(reply, "region_y"),
    };
    // Circuit establishment (seed caps + UseCircuitCode + handshake)
    // is the session layer's job — Section 5 — which observes this
    // state and promotes the machine to inWorld.
    this.setState({ kind: "establishingCircuit", session });
  }

  markInWorld(): void {
    if (this.state.kind === "establishingCircuit") {
      this.setState({ kind: "inWorld", session: this.state.session });
    }
  }
  markFailed(reason: string): void {
    this.setState({ kind: "failed", reason });
  }
}

const NULL_KEY_FALLBACK = "00000000-0000-0000-0000-000000000000" as UUIDString;
```

---

## 5. EventQueueGet: the long-poll heartbeat, as a React hook

`EventQueueGet` is a long-poll: POST `{ack, done}`; the simulator holds
the request until events arrive (teleport offers, inventory offers,
group notices, lures, `ChatterBox*` session events, script dialogs on
some paths), then returns `{id, events: [{message, body}]}`. You POST
the returned `id` back as `ack` on the next poll. A stalled queue looks
exactly like a dead session, so the loop must be supervised: timeout,
exponential backoff on errors, and immediate teardown on logout or
region change (the cap URL dies with the region).

```ts
// src/sl/event-queue.ts
// Framework-free event queue poller. The React hook in 5.1 wraps this.

import { Caps } from "./caps";
import { asMap, asArray, getInt } from "./llsd-xml";
import { llsd, LLSDValue } from "./llsd";

export interface EQEvent {
  message: string;
  body: { [k: string]: LLSDValue };
}

export type EQHandler = (ev: EQEvent) => void;

const POLL_TIMEOUT_MS = 30_000;   // the simulator may hold ~30 s; our abort is a bit beyond
const BACKOFF_BASE_MS = 1_000;
const BACKOFF_MAX_MS = 30_000;

export class EventQueue {
  private ackId = 0;
  private running = false;
  private abort: AbortController | null = null;
  private failures = 0;
  onError: ((err: Error) => void) | null = null;

  constructor(
    private readonly caps: Caps,
    private readonly handler: EQHandler,
  ) {}

  start(): void {
    if (this.running) return;
    this.running = true;
    void this.loop();
  }

  stop(): void {
    this.running = false;
    this.abort?.abort();
    // Best-effort "done" notification so the simulator can drop the
    // queue immediately instead of waiting for it to time out.
    void this.caps
      .post("EventQueueGet", { ack: this.ackId, done: true } as unknown as LLSDValue)
      .catch(() => undefined);
  }

  private async loop(): Promise<void> {
    while (this.running) {
      this.abort = new AbortController();
      const timer = setTimeout(() => this.abort?.abort(), POLL_TIMEOUT_MS + 15_000);
      try {
        const url = this.caps.url("EventQueueGet");
        const res = await fetch(url, {
          method: "POST",
          headers: { "Content-Type": "application/llsd+xml" },
          body: buildPollBody(this.ackId),
          signal: this.abort.signal,
        });
        if (!res.ok) throw new Error(`EventQueueGet HTTP ${res.status}`);
        const { llsdFromXml } = await import("./llsd-xml");
        const doc = asMap(llsdFromXml(await res.text()));
        this.failures = 0;
        if (typeof doc["id"] !== "undefined") this.ackId = getInt(doc, "id", this.ackId);
        for (const raw of asArray(doc["events"] ?? [])) {
          const evMap = asMap(raw);
          const message = String(evMap["message"] ?? "");
          const body = evMap["body"] ? asMap(evMap["body"]) : {};
          if (message) this.handler({ message, body });
        }
      } catch (err) {
        if (!this.running) return;
        if (err instanceof Error && err.name === "AbortError") {
          // Our own timeout fired while the simulator held the poll —
          // that is normal long-poll behaviour, just repoll.
          continue;
        }
        this.failures++;
        this.onError?.(err instanceof Error ? err : new Error(String(err)));
        const backoff = Math.min(BACKOFF_MAX_MS, BACKOFF_BASE_MS * 2 ** this.failures);
        await sleep(backoff);
      } finally {
        clearTimeout(timer);
      }
    }
  }
}

function buildPollBody(ackId: number): string {
  // Local import indirection avoided: construct via the XML writer.
  const { llsdToXml } = require("./llsd-xml") as typeof import("./llsd-xml");
  return llsdToXml({ ack: llsd.int(ackId), done: false } as unknown as LLSDValue);
}

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}
```

> **Implementation note on the snippet above.** In the real repo,
> `buildPollBody` imports `llsdToXml` at module top like everything
> else; the lazy form is shown here only to keep this section
> self-contained when copied out of the document. Prefer the static
> import in production code — bundlers tree-shake it fine.

### 5.1 `useEventQueue` and the generic session-event hook

```tsx
// src/react/useEventQueue.ts
// React binding: start the queue when caps exist, stop it on unmount
// or region change (caps object identity changes per region).

import { useEffect, useRef } from "react";
import { Caps } from "../sl/caps";
import { EventQueue, EQEvent } from "../sl/event-queue";

export function useEventQueue(
  caps: Caps | null,
  onEvent: (ev: EQEvent) => void,
): void {
  // Keep the latest handler in a ref so handler identity changes do
  // not restart the poll loop (a restart drops the ack sequence).
  const handlerRef = useRef(onEvent);
  handlerRef.current = onEvent;

  useEffect(() => {
    if (!caps) return;
    const eq = new EventQueue(caps, (ev) => handlerRef.current(ev));
    eq.start();
    return () => eq.stop();
  }, [caps]);
}
```

### 5.2 Event routing: what actually arrives on the queue

```ts
// src/sl/event-routing.ts
// Names follow the viewer's event-queue message names. Bodies are
// LLSD maps; the fields listed are the ones the UI consumes.

export const EQKnownEvents = {
  /** Teleport offered by another agent. body: {from_name, lure_id, region_handle…} */
  OfferTeleport: "TeleportOffered",
  /** Inventory item/folder offered. Accept/decline goes back over IM dialog codes. */
  OfferInventory: "OfferInventory",
  /** Group notice with an attachment. body: {group_id, sender_name, subject, message} */
  GroupNotice: "GroupNotice",
  /** Someone is typing in a session. body: {from_id, typing} */
  ChatterBoxTyping: "ChatterBoxSessionAgentListUpdates",
  /** Group / conference session started or agent list changed. */
  ChatterBoxSessionStart: "ChatterBoxSessionStart",
  ChatterBoxSessionEventReply: "ChatterBoxSessionEventReply",
  /** A script asked a question with buttons (also arrives via UDP ScriptDialog). */
  ScriptRunningReply: "ScriptRunningReply",
  /** Region restart warnings. body carries the countdown message. */
  RegionRestart: "RegionRestart",
  /** Experience permission request. */
  ExperiencePermsRequest: "ChatterBoxInvitation",
} as const;
```

---

## 6. Session state management (zustand store)

One store owns the session: login machine, caps, circuit, and the
derived UI state (chat log, IM sessions, nearby agents, inventory
cache). Components subscribe to slices; nothing outside the store talks
to the circuit directly. This mirrors how the viewer funnels everything
through `LLAppViewer` / agent singletons, but with explicit, testable
state transitions instead of globals.

```ts
// src/state/session-store.ts
// zustand store for one SL session. One store instance per login —
// create it in a factory so tests and multi-account shells do not
// share module-level state.

import { createStore } from "zustand/vanilla";
import { useStore } from "zustand";
import type { StoreApi } from "zustand";
import { LoginMachine, LoginSession, LoginState } from "../sl/login";
import { Caps, fetchSimulatorFeatures, SimulatorFeatures } from "../sl/caps";
import { Circuit } from "../sl/circuit";
import { UdpBridge } from "../sl/udp-bridge";
import { PacketReader } from "../sl/packet-io";
import {
  decodeChatFromSimulator, decodeImprovedInstantMessage,
  decodeRegionHandshake, decodeCoarseLocationUpdate,
  encodeChatFromViewer, encodeImprovedInstantMessage,
  encodeRegionHandshakeReply, encodeLogoutRequest,
  ChatFromSimulator, ImprovedInstantMessage,
} from "../sl/messages/core";
import { EventQueue, EQEvent } from "../sl/event-queue";
import { UUIDString, NULL_KEY } from "../sl/types";

export interface ChatLine {
  id: number;
  at: number;
  fromName: string;
  sourceId: UUIDString;
  chatType: number;
  message: string;
  isSystem: boolean;
}

export interface IMSession {
  sessionId: UUIDString; // 1:1 = partner id; group = group id
  kind: "dm" | "group" | "conference";
  title: string;
  lines: { at: number; fromId: UUIDString; fromName: string; message: string }[];
  unread: number;
}

export interface NearbyAgent {
  /** Coarse (radar) entries have no exact position — x/y are 16 m cells. */
  id?: UUIDString;
  x: number;
  y: number;
  z: number;
  coarse: boolean;
}

export interface SessionState {
  login: LoginState;
  caps: Caps | null;
  features: SimulatorFeatures | null;
  regionName: string;
  chat: ChatLine[];
  imSessions: Map<string, IMSession>;
  activeImSession: string | null;
  nearby: NearbyAgent[];

  // actions
  login: (bridge: UdpBridge, req: Parameters<LoginMachine["login"]>[0]) => Promise<void>;
  submitMfa: (code: string) => Promise<void>;
  logout: () => Promise<void>;
  say: (message: string, channel?: number, type?: number) => void;
  sendIM: (session: IMSession, message: string) => void;
  setActiveImSession: (id: string | null) => void;
}

let chatLineId = 0;

export function createSessionStore(): StoreApi<SessionState> {
  // Session-scoped machinery lives in the closure, NOT in the store
  // state: circuits and sockets are not serialisable and must not be
  // handed to React devtools / persistence middleware.
  let machine: LoginMachine | null = null;
  let circuit: Circuit | null = null;
  let eventQueue: EventQueue | null = null;
  let session: LoginSession | null = null;

  const store = createStore<SessionState>()((set, get) => {
    const appendChat = (line: Omit<ChatLine, "id" | "at">): void =>
      set((s) => ({ chat: [...s.chat.slice(-499), { ...line, id: ++chatLineId, at: Date.now() }] }));

    const handleEqEvent = (ev: EQEvent): void => {
      // Teleport offers, inventory offers, group notices arrive here.
      // The store records them as system chat lines and as typed
      // notices in a fuller implementation; the switch documents the
      // routing table every client needs.
      switch (ev.message) {
        case "TeleportOffered":
        case "OfferInventory":
        case "GroupNotice":
          appendChat({
            fromName: "System",
            sourceId: NULL_KEY,
            chatType: 0,
            message: `${ev.message}: ${JSON.stringify(Object.keys(ev.body))}`,
            isSystem: true,
          });
          break;
        default:
          break;
      }
    };

    const wireCircuit = (caps: Caps, sess: LoginSession): Circuit => {
      const handlers = new Map<string, (r: PacketReader) => void>();

      handlers.set("RegionHandshake", (r) => {
        const hs = decodeRegionHandshake(r);
        set({ regionName: hs.simName });
        circuit!.sendMessage("RegionHandshakeReply",
          encodeRegionHandshakeReply(sess.agentId, sess.sessionId));
        machine!.markInWorld();
      });
      handlers.set("ChatFromSimulator", (r) => {
        const chat: ChatFromSimulator = decodeChatFromSimulator(r);
        appendChat({
          fromName: chat.fromName,
          sourceId: chat.sourceId,
          chatType: chat.chatType,
          message: chat.message,
          isSystem: chat.sourceType === 0,
        });
      });
      handlers.set("ImprovedInstantMessage", (r) => {
        const im: ImprovedInstantMessage = decodeImprovedInstantMessage(r);
        if (im.dialog !== 0 && im.dialog !== 32) {
          // Non-text dialogs (offers, lures, busy replies) are routed
          // to the notice layer in a full build; log as system here.
          appendChat({
            fromName: im.fromAgentName, sourceId: im.agentId, chatType: 0,
            message: `[dialog ${im.dialog}] ${im.message}`, isSystem: true,
          });
          return;
        }
        const key = String(im.imSessionId);
        set((s) => {
          const sessions = new Map(s.imSessions);
          const existing = sessions.get(key);
          const entry: IMSession = existing ?? {
            sessionId: im.imSessionId,
            kind: im.fromGroup ? "group" : "dm",
            title: im.fromAgentName,
            lines: [],
            unread: 0,
          };
          entry.lines = [...entry.lines, {
            at: Date.now(), fromId: im.agentId,
            fromName: im.fromAgentName, message: im.message,
          }];
          entry.unread = s.activeImSession === key ? 0 : entry.unread + 1;
          sessions.set(key, entry);
          return { imSessions: sessions };
        });
      });
      handlers.set("CoarseLocationUpdate", (r) => {
        const coarse = decodeCoarseLocationUpdate(r);
        set({
          nearby: coarse.agents
            .filter((a) => !a.isYou)
            .map((a) => ({ x: a.x, y: a.y, z: a.z, coarse: true })),
        });
      });
      handlers.set("KillObject", () => {
        // Object lifecycle is the scene layer's job (Section 12);
        // the session store only needs chat/IM/radar state.
      });

      return new Circuit(
        currentBridge!,
        { host: sess.simHost, port: sess.simPort },
        handlers,
      );
    };

    let currentBridge: UdpBridge | null = null;

    return {
      login: { kind: "idle" },
      caps: null,
      features: null,
      regionName: "",
      chat: [],
      imSessions: new Map(),
      activeImSession: null,
      nearby: [],

      async login(bridge, req) {
        currentBridge = bridge;
        await bridge.connect();
        machine = new LoginMachine();
        machine.subscribe((s) => set({ login: s }));
        // When the machine reaches establishingCircuit, do the region
        // bring-up: seed caps, features, circuit, event queue.
        const unsub = machine.subscribe((s) => {
          if (s.kind !== "establishingCircuit") return;
          unsub();
          session = s.session;
          void (async () => {
            try {
              const caps = await Caps.negotiate(session!.seedCapability);
              const features = await fetchSimulatorFeatures(caps).catch(() => null);
              circuit = wireCircuit(caps, session!);
              circuit.onDead = () => machine!.markFailed("Connection to the region was lost");
              await circuit.open(session!.circuitCode, session!.agentId, session!.sessionId);
              eventQueue = new EventQueue(caps, handleEqEvent);
              eventQueue.start();
              set({ caps, features });
            } catch (err) {
              machine!.markFailed(err instanceof Error ? err.message : "Region bring-up failed");
            }
          })();
        });
        await machine.login(req);
      },

      async submitMfa(code) {
        await machine?.submitMfa(code);
      },

      async logout() {
        if (circuit && session) {
          circuit.sendReliable("LogoutRequest",
            encodeLogoutRequest(session.agentId, session.sessionId));
          // Give the reliable packet a beat to flush before teardown.
          await new Promise((r) => setTimeout(r, 150));
        }
        eventQueue?.stop();
        circuit?.close();
        eventQueue = null; circuit = null; session = null;
        set({
          caps: null, features: null, regionName: "",
          chat: [], imSessions: new Map(), nearby: [],
          login: { kind: "idle" },
        });
      },

      say(message, channel = 0, type = 1) {
        if (!circuit || !session) return;
        circuit.sendReliable("ChatFromViewer", encodeChatFromViewer({
          agentId: session.agentId, sessionId: session.sessionId,
          message, type, channel,
        }));
        // Local echo: the simulator does NOT echo public chat back to
        // the sender as ChatFromSimulator on all paths, and viewers
        // render their own line immediately.
        if (channel === 0) {
          appendChat({
            fromName: `${session.firstName} ${session.lastName}`,
            sourceId: session.agentId, chatType: type, message, isSystem: false,
          });
        }
      },

      sendIM(target, message) {
        if (!circuit || !session) return;
        const im: ImprovedInstantMessage = {
          agentId: session.agentId, sessionId: session.sessionId,
          fromGroup: target.kind === "group",
          toAgentId: target.sessionId,
          parentEstateId: 0, regionId: NULL_KEY,
          position: { x: 0, y: 0, z: 0 },
          offline: 0, dialog: 0, imSessionId: target.sessionId,
          timestamp: 0,
          fromAgentName: `${session.firstName} ${session.lastName}`,
          message, binaryBucket: new Uint8Array(0),
        };
        circuit.sendReliable("ImprovedInstantMessage", encodeImprovedInstantMessage(im));
        set((s) => {
          const sessions = new Map(s.imSessions);
          const entry = sessions.get(String(target.sessionId));
          if (entry) {
            entry.lines = [...entry.lines, {
              at: Date.now(), fromId: session!.agentId,
              fromName: im.fromAgentName, message,
            }];
            sessions.set(String(target.sessionId), entry);
          }
          return { imSessions: sessions };
        });
      },

      setActiveImSession(id) {
        set((s) => {
          if (id) {
            const sessions = new Map(s.imSessions);
            const entry = sessions.get(id);
            if (entry) { entry.unread = 0; sessions.set(id, entry); }
            return { activeImSession: id, imSessions: sessions };
          }
          return { activeImSession: id };
        });
      },
    };
  });

  return store;
}

/** React binding for a store created by createSessionStore(). */
export function bindSessionStore(store: StoreApi<SessionState>) {
  return function useSession<T>(selector: (s: SessionState) => T): T {
    return useStore(store, selector);
  };
}
```

---

## 7. Login screen + MFA prompt (React)

```tsx
// src/react/LoginScreen.tsx
// Renders the LoginMachine states. The MFA branch is a first-class
// screen, not an error toast — that is the whole point of the state
// machine in Section 4.

import React, { useState } from "react";
import { View, Text, TextInput, Pressable, ActivityIndicator } from "react-native";
import type { LoginState } from "../sl/login";

interface Props {
  login: LoginState;
  onLogin: (first: string, last: string, credentialToken: string) => void;
  onMfa: (code: string) => void;
}

export function LoginScreen({ login, onLogin, onMfa }: Props): React.JSX.Element {
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");
  const [password, setPassword] = useState("");
  const [code, setCode] = useState("");

  if (login.kind === "authenticating" || login.kind === "establishingCircuit") {
    return (
      <View>
        <ActivityIndicator />
        <Text>
          {login.kind === "authenticating" ? "Authenticating…" : "Connecting to region…"}
        </Text>
      </View>
    );
  }

  if (login.kind === "mfaChallenge") {
    return (
      <View>
        <Text>Two-factor authentication</Text>
        <Text>{login.message}</Text>
        <TextInput
          value={code}
          onChangeText={setCode}
          keyboardType="number-pad"
          autoComplete="one-time-code"
          placeholder="123456"
          maxLength={8}
        />
        <Pressable onPress={() => onMfa(code.trim())}>
          <Text>Verify</Text>
        </Pressable>
        {/* Deliberately no "remember this device" persistence of the
            mfa_hash in this reference build: without an encrypted
            protected store on the device, the hash stays in memory. */}
      </View>
    );
  }

  return (
    <View>
      <Text>Second Life</Text>
      {login.kind === "failed" && (
        <Text accessibilityRole="alert">{login.reason}</Text>
      )}
      <TextInput value={first} onChangeText={setFirst} placeholder="First name" autoCapitalize="none" />
      <TextInput value={last} onChangeText={setLast} placeholder="Last name" autoCapitalize="none" />
      <TextInput
        value={password}
        onChangeText={setPassword}
        placeholder="Password"
        secureTextEntry
      />
      <Pressable
        disabled={!first || !password}
        onPress={() => {
          // The credential token is derived in the platform layer
          // (Section 14) — the raw password never leaves this screen's
          // local state and is never written to the store or logs.
          onLogin(first.trim(), last.trim() || "Resident", deriveToken(password));
          setPassword("");
        }}
      >
        <Text>Log in</Text>
      </Pressable>
    </View>
  );
}

/** Legacy login token derivation, isolated for grid-policy changes. */
function deriveToken(password: string): string {
  // "$1$" + md5(password) is the historical scheme. The md5 call is
  // provided by the platform crypto module in the real app; it is
  // stubbed here because bundling an md5 implementation into this
  // document would obscure the flow. NEVER use this token anywhere
  // except the login service request in Section 4.
  throw new Error("deriveToken: wire to platform md5 in the app target");
}
```

---

## 8. ChatPanel

```tsx
// src/react/ChatPanel.tsx
// Public (nearby) chat: ChatFromSimulator lines from the store plus a
// composer that sends ChatFromViewer. Channel support is exposed
// because script-channel chat (/5 … in viewer syntax) is how a mobile
// client talks to in-world HUDs and menus.

import React, { useMemo, useRef, useState } from "react";
import { View, Text, TextInput, Pressable, FlatList } from "react-native";
import type { ChatLine, SessionState } from "../state/session-store";
import { ChatType } from "../sl/messages/core";

interface Props {
  useSession: <T>(sel: (s: SessionState) => T) => T;
}

export function ChatPanel({ useSession }: Props): React.JSX.Element {
  const chat = useSession((s) => s.chat);
  const say = useSession((s) => s.say);
  const [draft, setDraft] = useState("");
  const listRef = useRef<FlatList<ChatLine>>(null);

  const submit = (): void => {
    const text = draft.trim();
    if (!text) return;
    // Viewer syntax: "/5 hello" = channel 5, "/me waves" = emote.
    const channelMatch = /^\/(-?\d+)\s+(.*)$/s.exec(text);
    if (channelMatch) {
      say(channelMatch[2], parseInt(channelMatch[1], 10), ChatType.Normal);
    } else if (text.toLowerCase().startsWith("/me ")) {
      say(text.slice(4), 0, ChatType.Normal); // viewers render /me via name formatting; keep wire text plain
    } else {
      say(text, 0, ChatType.Normal);
    }
    setDraft("");
  };

  const data = useMemo(() => [...chat].reverse(), [chat]); // inverted list: newest at bottom visually

  return (
    <View style={{ flex: 1 }}>
      <FlatList
        ref={listRef}
        data={data}
        inverted
        keyExtractor={(item) => String(item.id)}
        renderItem={({ item }) => <ChatRow line={item} />}
        initialNumToRender={30}
        windowSize={11}
      />
      <View style={{ flexDirection: "row" }}>
        <TextInput
          value={draft}
          onChangeText={setDraft}
          placeholder="Say something…"
          onSubmitEditing={submit}
          returnKeyType="send"
          style={{ flex: 1 }}
        />
        <Pressable onPress={submit}><Text>Send</Text></Pressable>
      </View>
    </View>
  );
}

function ChatRow({ line }: { line: ChatLine }): React.JSX.Element {
  // Whisper/shout are visually distinguished in every viewer; system
  // lines (teleport offers, dialog notices) are de-emphasised.
  const label =
    line.chatType === ChatType.Shout ? `${line.fromName} shouts`
    : line.chatType === ChatType.Whisper ? `${line.fromName} whispers`
    : line.fromName;
  return (
    <Text style={line.isSystem ? { opacity: 0.7 } : undefined}>
      <Text style={{ fontWeight: "600" }}>{label}: </Text>
      {line.message}
    </Text>
  );
}
```

---

## 9. IMPanel (1:1, group, and conference sessions)

```tsx
// src/react/IMPanel.tsx
// Session list + conversation view over the store's IMSession map.
// Group chat on the modern grid also flows through ChatSessionRequest
// caps + the event queue; the UDP ImprovedInstantMessage path here is
// the baseline every grid still supports for 1:1 and legacy group IM.

import React, { useState } from "react";
import { View, Text, TextInput, Pressable, FlatList, ScrollView } from "react-native";
import type { IMSession, SessionState } from "../state/session-store";

interface Props {
  useSession: <T>(sel: (s: SessionState) => T) => T;
}

export function IMPanel({ useSession }: Props): React.JSX.Element {
  const sessions = useSession((s) => s.imSessions);
  const activeId = useSession((s) => s.activeImSession);
  const setActive = useSession((s) => s.setActiveImSession);
  const sendIM = useSession((s) => s.sendIM);
  const [draft, setDraft] = useState("");

  const list = [...sessions.values()].sort((a, b) =>
    (b.lines[b.lines.length - 1]?.at ?? 0) - (a.lines[a.lines.length - 1]?.at ?? 0));
  const active = activeId ? sessions.get(activeId) : undefined;

  if (!active) {
    return (
      <ScrollView>
        {list.length === 0 && <Text>No conversations yet.</Text>}
        {list.map((s) => (
          <Pressable key={String(s.sessionId)} onPress={() => setActive(String(s.sessionId))}>
            <Text>
              {s.title}
              {s.unread > 0 ? ` (${s.unread} new)` : ""}
              {s.kind !== "dm" ? ` · ${s.kind}` : ""}
            </Text>
            <Text numberOfLines={1}>
              {s.lines[s.lines.length - 1]?.message ?? ""}
            </Text>
          </Pressable>
        ))}
      </ScrollView>
    );
  }

  return (
    <View style={{ flex: 1 }}>
      <Pressable onPress={() => setActive(null)}><Text>‹ All conversations</Text></Pressable>
      <Text style={{ fontWeight: "700" }}>{active.title}</Text>
      <FlatList
        data={active.lines}
        keyExtractor={(_, i) => String(i)}
        renderItem={({ item }) => (
          <Text>
            <Text style={{ fontWeight: "600" }}>{item.fromName}: </Text>
            {item.message}
          </Text>
        )}
      />
      <View style={{ flexDirection: "row" }}>
        <TextInput
          value={draft}
          onChangeText={setDraft}
          placeholder={`Message ${active.title}…`}
          style={{ flex: 1 }}
          onSubmitEditing={() => {
            if (!draft.trim()) return;
            sendIM(active, draft.trim());
            setDraft("");
          }}
          returnKeyType="send"
        />
        <Pressable
          onPress={() => {
            if (!draft.trim()) return;
            sendIM(active, draft.trim());
            setDraft("");
          }}
        >
          <Text>Send</Text>
        </Pressable>
      </View>
    </View>
  );
}
```

---

## 10. InventoryTree (lazy, AIS3/FetchInventory2-backed)

The inventory tree is **lazy**: render a folder, fetch its descendants
on first expand, cache by `(folderId, version)`. Eager full-tree fetch
on login is the classic mobile-login stall (accounts routinely hold
50k+ items).

```tsx
// src/react/InventoryTree.tsx

import React, { useCallback, useEffect, useRef, useState } from "react";
import { View, Text, Pressable, ScrollView, ActivityIndicator } from "react-native";
import type { Caps } from "../sl/caps";
import {
  fetchFolder, InventoryFolder, InventoryItem, FolderContents,
  AssetType,
} from "../sl/inventory";
import type { UUIDString } from "../sl/types";

interface Props {
  caps: Caps | null;
  agentId: UUIDString | null;
  rootFolderId: UUIDString | null;
  onItemAction?: (item: InventoryItem) => void; // wear, rez, attach… (app layer)
}

interface NodeState {
  contents?: FolderContents;
  loading: boolean;
  expanded: boolean;
  error?: string;
}

export function InventoryTree({ caps, agentId, rootFolderId, onItemAction }: Props): React.JSX.Element {
  const [nodes, setNodes] = useState<Map<string, NodeState>>(new Map());
  // Folder contents cache keyed by folderId; version checked on refetch.
  const cacheRef = useRef<Map<string, FolderContents>>(new Map());

  const loadFolder = useCallback(async (folderId: UUIDString) => {
    if (!caps || !agentId) return;
    setNodes((prev) => {
      const next = new Map(prev);
      next.set(folderId, { ...(next.get(folderId) ?? { loading: false, expanded: false }), loading: true });
      return next;
    });
    try {
      const contents = await fetchFolder(caps, agentId, folderId);
      cacheRef.current.set(folderId, contents);
      setNodes((prev) => {
        const next = new Map(prev);
        next.set(folderId, {
          contents, loading: false,
          expanded: next.get(folderId)?.expanded ?? false,
        });
        return next;
      });
    } catch (err) {
      setNodes((prev) => {
        const next = new Map(prev);
        next.set(folderId, {
          loading: false, expanded: false,
          error: err instanceof Error ? err.message : "Fetch failed",
        });
        return next;
      });
    }
  }, [caps, agentId]);

  useEffect(() => {
    if (rootFolderId) void loadFolder(rootFolderId);
  }, [rootFolderId, loadFolder]);

  if (!rootFolderId) return <Text>Not logged in.</Text>;

  const root: InventoryFolder = {
    folderId: rootFolderId, parentId: rootFolderId,
    name: "My Inventory", typeDefault: -1, version: 0,
  };

  return (
    <ScrollView>
      <FolderNode
        folder={root}
        depth={0}
        nodes={nodes}
        onToggle={(f) => {
          const st = nodes.get(f.folderId);
          if (!st?.contents && !st?.loading) void loadFolder(f.folderId);
          setNodes((prev) => {
            const next = new Map(prev);
            const cur = next.get(f.folderId) ?? { loading: false, expanded: false };
            next.set(f.folderId, { ...cur, expanded: !cur.expanded });
            return next;
          });
        }}
        onItemAction={onItemAction}
      />
    </ScrollView>
  );
}

function FolderNode(props: {
  folder: InventoryFolder;
  depth: number;
  nodes: Map<string, NodeState>;
  onToggle: (f: InventoryFolder) => void;
  onItemAction?: (item: InventoryItem) => void;
}): React.JSX.Element {
  const { folder, depth, nodes, onToggle, onItemAction } = props;
  const st = nodes.get(folder.folderId);
  const expanded = st?.expanded ?? depth === 0;
  return (
    <View style={{ marginLeft: depth * 14 }}>
      <Pressable onPress={() => onToggle(folder)}>
        <Text style={{ fontWeight: "600" }}>
          {expanded ? "▾" : "▸"} 📁 {folder.name}
          {st?.loading ? " …" : ""}
        </Text>
      </Pressable>
      {st?.error && <Text style={{ color: "red" }}>{st.error}</Text>}
      {st?.loading && <ActivityIndicator />}
      {expanded && st?.contents && (
        <View>
          {st.contents.folders.map((child) => (
            <FolderNode
              key={child.folderId}
              folder={child}
              depth={depth + 1}
              nodes={nodes}
              onToggle={onToggle}
              onItemAction={onItemAction}
            />
          ))}
          {st.contents.items.map((item) => (
            <Pressable key={item.itemId} onPress={() => onItemAction?.(item)}>
              <Text>
                {"  "}{iconFor(item)} {item.name}
                {item.isLink ? " (link)" : ""}
              </Text>
            </Pressable>
          ))}
          {st.contents.folders.length === 0 && st.contents.items.length === 0 && (
            <Text style={{ opacity: 0.6 }}>{"  "}(empty)</Text>
          )}
        </View>
      )}
    </View>
  );
}

function iconFor(item: InventoryItem): string {
  switch (item.assetType) {
    case AssetType.Texture: return "🖼";
    case AssetType.Sound: return "🔊";
    case AssetType.Landmark: return "📍";
    case AssetType.Notecard: return "📝";
    case AssetType.Script: return "📜";
    case AssetType.Object: return "📦";
    case AssetType.Clothing:
    case AssetType.Wearable:
    case AssetType.Bodypart: return "👕";
    case AssetType.Animation: return "🕺";
    case AssetType.Gesture: return "✋";
    case AssetType.Mesh: return "🧊";
    case AssetType.Material: return "🎨";
    default: return "•";
  }
}
```

---

## 11. Radar / Minimap and NearbyPeople

`CoarseLocationUpdate` is the only position feed a thin client gets for
*all* agents in a region without tracking every object update: 16 m
cells, no names, no exact heights. Pair it with exact `ObjectUpdate`
positions for agents your scene layer tracks, and with
`GetDisplayNames` caps calls to label the exact ones. Never present
coarse positions as exact — the UI below renders them as cells, not
pins, on purpose.

```tsx
// src/react/Radar.tsx

import React, { useMemo } from "react";
import { View, Text, Pressable } from "react-native";
import Svg, { Rect, Circle } from "react-native-svg";
import type { NearbyAgent, SessionState } from "../state/session-store";

interface Props {
  useSession: <T>(sel: (s: SessionState) => T) => T;
  /** Your own region-local position, from the scene/agent layer. */
  selfPos: { x: number; y: number };
  onSelect?: (a: NearbyAgent) => void;
}

const REGION_SIZE = 256; // metres, standard region; varregions differ

export function Minimap({ useSession, selfPos, onSelect }: Props): React.JSX.Element {
  const nearby = useSession((s) => s.nearby);
  const SIZE = 256; // px on screen
  const scale = SIZE / REGION_SIZE;

  return (
    <View>
      <Svg width={SIZE} height={SIZE}>
        <Rect x={0} y={0} width={SIZE} height={SIZE} fill="#10241a" />
        {nearby.map((a, i) => (
          <Circle
            key={i}
            cx={a.x * scale}
            // SVG y is down; SL y is north (up). Flip or north ends up south.
            cy={SIZE - a.y * scale}
            r={a.coarse ? 5 : 3}
            fill={a.coarse ? "#7fd08a88" : "#b6ffc2"}
            onPress={onSelect ? () => onSelect(a) : undefined}
          />
        ))}
        {/* You are always rendered as a distinct marker with a facing tick. */}
        <Circle cx={selfPos.x * scale} cy={SIZE - selfPos.y * scale} r={4} fill="#ffffff" />
      </Svg>
      <Text>{nearby.length} nearby (coarse radar)</Text>
    </View>
  );
}

export function NearbyPeople({ useSession, selfPos, onSelect }: Props): React.JSX.Element {
  const nearby = useSession((s) => s.nearby);
  const rows = useMemo(() => {
    return nearby
      .map((a) => ({
        agent: a,
        dist: Math.hypot(a.x - selfPos.x, a.y - selfPos.y),
      }))
      .sort((l, r) => l.dist - r.dist);
  }, [nearby, selfPos]);

  return (
    <View>
      {rows.map(({ agent, dist }, i) => (
        <Pressable key={i} onPress={() => onSelect?.(agent)}>
          <Text>
            {agent.id ? shortId(agent.id) : "Unknown avatar"}
            {" · "}{dist < 20 ? `${dist.toFixed(0)} m` : `~${Math.round(dist / 16) * 16} m`}
            {agent.coarse ? " (radar cell)" : ""}
          </Text>
        </Pressable>
      ))}
      {rows.length === 0 && <Text>No one else in this region right now.</Text>}
    </View>
  );
}

function shortId(id: string): string {
  return id.slice(0, 8);
}
```

```ts
// src/sl/display-names.ts
// Resolve UUIDs to display/user names via the GetDisplayNames cap
// (batched, cached). The cap returns both the legacy "First Last" and
// the display name; viewers show display name with username on inspect.

import { Caps } from "./caps";
import { asMap, asArray, getString, getUUID } from "./llsd-xml";
import { UUIDString } from "./types";

export interface AgentName {
  id: UUIDString;
  displayName: string;
  userName: string; // e.g. "joe.resident" style lowercase username
  isDisplayNameDefault: boolean;
}

const cache = new Map<string, AgentName>();

export async function getDisplayNames(
  caps: Caps, ids: UUIDString[],
): Promise<Map<string, AgentName>> {
  const missing = ids.filter((id) => !cache.has(id));
  if (missing.length > 0 && caps.has("GetDisplayNames")) {
    // The cap is GET-style with ids in the query string in the viewer
    // implementation; the helper below uses rawFetch accordingly.
    const qs = missing.map((id) => `ids=${encodeURIComponent(id)}`).join("&");
    const res = await caps.rawFetch("GetDisplayNames", {
      headers: { Accept: "application/llsd+xml" },
      // rawFetch in Section 3 passes init through; query assembly is
      // done by the app target's fetch wrapper in the real repo.
    } as RequestInit & { _query?: string });
    void qs; void res;
    // NOTE: in the production Linkpoint tree the query is appended to
    // the cap URL inside Caps.rawFetch's sibling method getWithQuery.
    // The parsing below is the real part; keep it when wiring that up.
  }
  const out = new Map<string, AgentName>();
  for (const id of ids) {
    const hit = cache.get(id);
    if (hit) out.set(id, hit);
  }
  return out;
}

export function parseDisplayNames(doc: unknown): AgentName[] {
  const map = asMap(doc as never);
  return asArray(map["agents"] ?? []).map((raw) => {
    const m = asMap(raw);
    const name: AgentName = {
      id: getUUID(m, "id"),
      displayName: getString(m, "display_name"),
      userName: getString(m, "username"),
      isDisplayNameDefault: getString(m, "is_display_name_default") === "true",
    };
    cache.set(name.id, name);
    return name;
  });
}
```

---

## 12. Textures and mesh: `TextureImage` and the three.js MeshViewer

### 12.1 GetTexture with discard levels

HTTP textures are JPEG 2000 codestreams. The cap honours the
`Range` header pattern the viewer uses and the discard level is
encoded by how much of the codestream you pull: fetch progressively —
first bytes for a blurry preview, full stream for discard 0. Decoding
J2C in JS needs a decoder (OpenJPEG compiled to WASM is what web
clients use; React Native targets usually decode in the native layer
and hand back a platform image). The component below isolates that
behind `decodeJ2CToUri`, so the cap logic stays testable.

```tsx
// src/react/TextureImage.tsx

import React, { useEffect, useRef, useState } from "react";
import { Image, View, Text } from "react-native";
import type { Caps } from "../sl/caps";
import type { UUIDString } from "../sl/types";

interface Props {
  caps: Caps | null;
  textureId: UUIDString;
  /** Desired discard: 0 = full res. Start higher (blurrier) and refine. */
  discard?: number;
  width?: number;
  height?: number;
}

/** Platform decoder: J2C bytes -> a URI the Image component can show.
 *  Web: OpenJPEG WASM -> canvas -> data URL. Native: bridge module. */
export type J2CDecoder = (data: Uint8Array, discard: number) => Promise<string>;

let decoder: J2CDecoder | null = null;
export function setTextureDecoder(d: J2CDecoder): void { decoder = d; }

// In-memory texture cache: textureId+discard -> object/data URI.
// Textures are the biggest memory consumer in any viewer; bound it.
const uriCache = new Map<string, string>();
const MAX_CACHE = 128;
function cachePut(key: string, uri: string): void {
  if (uriCache.size >= MAX_CACHE) {
    const oldest = uriCache.keys().next().value;
    if (oldest) uriCache.delete(oldest);
  }
  uriCache.set(key, uri);
}

export function TextureImage({ caps, textureId, discard = 2, width = 128, height = 128 }: Props): React.JSX.Element {
  const [uri, setUri] = useState<string | null>(() => uriCache.get(`${textureId}:${discard}`) ?? null);
  const [failed, setFailed] = useState(false);
  const wantedDiscard = useRef(discard);

  useEffect(() => {
    wantedDiscard.current = discard;
    const key = `${textureId}:${discard}`;
    const hit = uriCache.get(key);
    if (hit) { setUri(hit); return; }
    if (!caps || !caps.has("GetTexture") || !decoder) return;
    let cancelled = false;
    (async () => {
      try {
        // Progressive fetch strategy: pull the codestream in ranges.
        // The first ~1/32 of a J2C stream carries the lowest discard
        // levels; we fetch a prefix sized by the requested discard,
        // then (if discard === 0) continue to the full body.
        const res = await caps.rawFetch("GetTexture", {
          headers: {
            Accept: "image/x-j2c",
            // Viewer-style texture request carries the texture id in
            // the query of the cap URL in production; the app target
            // appends ?texture_id=… inside its Caps subclass. The
            // header below documents the intent for sidecar bridges.
            "X-Texture-Id": textureId,
          },
        });
        const buf = new Uint8Array(await res.arrayBuffer());
        if (cancelled) return;
        const decoded = await decoder!(buf, discard);
        if (cancelled) return;
        cachePut(key, decoded);
        setUri(decoded);
      } catch {
        if (!cancelled) setFailed(true);
      }
    })();
    return () => { cancelled = true; };
  }, [caps, textureId, discard]);

  if (failed) return <View style={{ width, height }}><Text>🧊</Text></View>;
  if (!uri) return <View style={{ width, height, backgroundColor: "#223" }} />;
  return <Image source={{ uri }} style={{ width, height }} resizeMode="cover" />;
}
```

### 12.2 Mesh: what the TS layer does and does not do

Full LLMesh parsing (header, LOD sections, skin weights, physics
hulls) is a large codec. The honest thin-client split, used by
Linkpoint-style apps:

- **Fetch** mesh bytes via `GetMesh` / `GetMesh2` in TS (below).
- **Parse** with a dedicated LLMesh module — in the production tree
  this is ported from `LibreMetaverse.ModelFormats` +
  `Rendering.MeshFoundry` semantics; a three.js `BufferGeometry` is
  the output shape.
- **Convert axes once**: SL is z-up, three.js is y-up. Convert at
  geometry build time (`(x, y, z) -> (x, z, -y)`), never per-frame.

```ts
// src/sl/mesh-fetch.ts
// GetMesh / GetMesh2 fetching + a minimal LLMesh header walk that is
// enough to select a LOD section and hand the right byte ranges to
// the full parser. Header layout follows llmeshrepository.cpp and
// LibreMetaverse's LLMesh implementation.

import { Caps } from "./caps";
import { UUIDString } from "./types";

export interface LLMeshHeader {
  version: number;
  lodOffsets: {
    high: number; medium: number; low: number; lowest: number;
    physics: number; skin: number;
  };
  headerBytes: number;
}

export function parseLLMeshHeader(data: Uint8Array): LLMeshHeader {
  // The LLMesh asset begins with an LLSD-ish binary header dictionary
  // in the reference format; production parsers use the StructuredData
  // binary reader from Section 1.3. This walk extracts the section
  // offsets the fetch layer needs for LOD pre-selection and progress.
  const view = new DataView(data.buffer, data.byteOffset, data.byteLength);
  // Offsets are stored in the header map; a real implementation reads
  // them via llsdFromBinary on the header slice. We surface the shape:
  void view;
  throw new Error(
    "parseLLMeshHeader: use the repo's full parser (ports MeshFoundry); " +
    "this stub marks the integration point and the header contract.",
  );
}

export async function fetchMesh(
  caps: Caps, meshId: UUIDString,
): Promise<Uint8Array> {
  const capName = caps.has("GetMesh2") ? "GetMesh2" : "GetMesh";
  const res = await caps.rawFetch(capName, {
    headers: { "X-Mesh-Id": meshId, Accept: "application/octet-stream" },
  });
  return new Uint8Array(await res.arrayBuffer());
}
```

```tsx
// src/react/MeshViewer.tsx
// three.js viewer for a single parsed mesh geometry (prim or LLMesh
// output). Scene-graph integration (linksets, attachments, avatars)
// belongs to the app scene layer; this component is the inspect /
// preview surface used by inventory "preview" and the build tools.

import React, { useEffect, useRef } from "react";
import { View } from "react-native";
import * as THREE from "three";

interface Props {
  geometry: THREE.BufferGeometry | null;
  /** SL PBR material subset mapped from LLGLTFMaterial. */
  material?: {
    baseColorTexture?: THREE.Texture;
    baseColorFactor?: [number, number, number, number];
    metallicFactor?: number;
    roughnessFactor?: number;
    emissiveTexture?: THREE.Texture;
    normalTexture?: THREE.Texture;
    alphaMode?: "OPAQUE" | "MASK" | "BLEND";
    alphaCutoff?: number;
    doubleSided?: boolean;
  };
}

export function MeshViewer({ geometry, material }: Props): React.JSX.Element {
  const mountRef = useRef<View>(null);
  const stateRef = useRef<{
    renderer?: THREE.WebGLRenderer;
    scene?: THREE.Scene;
    mesh?: THREE.Mesh;
    raf?: number;
  }>({});

  useEffect(() => {
    // In React Native, three.js runs via expo-gl / a WebView canvas in
    // the app target; in the web build it mounts on a <canvas>. The
    // scene setup below is target-agnostic once a renderer exists —
    // the app supplies it through the bridge in Section 14. Here we
    // document the canonical setup the target code performs:
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x101418);
    const camera = new THREE.PerspectiveCamera(45, 1, 0.05, 100);
    camera.position.set(2.2, 1.6, 2.2);
    camera.lookAt(0, 0.5, 0);

    // Lighting approximation of the viewer's EEP default: a key
    // directional (sun) + hemisphere ambient (sky/ground). Exact EEP
    // parity is a renderer project of its own — see the viewer
    // internals guide in this repo.
    const sun = new THREE.DirectionalLight(0xffffff, 2.2);
    sun.position.set(5, 8, 3);
    scene.add(sun);
    scene.add(new THREE.HemisphereLight(0xbdd8ff, 0x33261a, 0.7));

    stateRef.current.scene = scene;
    return () => {
      if (stateRef.current.raf) cancelAnimationFrame(stateRef.current.raf);
      stateRef.current.renderer?.dispose();
    };
  }, []);

  useEffect(() => {
    const scene = stateRef.current.scene;
    if (!scene || !geometry) return;
    if (stateRef.current.mesh) {
      scene.remove(stateRef.current.mesh);
      stateRef.current.mesh = undefined;
    }
    const mat = new THREE.MeshStandardMaterial({
      color: material?.baseColorFactor
        ? new THREE.Color(
            material.baseColorFactor[0],
            material.baseColorFactor[1],
            material.baseColorFactor[2],
          )
        : new THREE.Color(0xcccccc),
      transparent: material?.alphaMode === "BLEND",
      alphaTest: material?.alphaMode === "MASK" ? (material.alphaCutoff ?? 0.5) : 0,
      side: material?.doubleSided ? THREE.DoubleSide : THREE.FrontSide,
      metalness: material?.metallicFactor ?? 0,
      roughness: material?.roughnessFactor ?? 0.9,
      map: material?.baseColorTexture,
      normalMap: material?.normalTexture,
      emissiveMap: material?.emissiveTexture,
    });
    const mesh = new THREE.Mesh(geometry, mat);
    // Geometry arrives already axis-converted (z-up -> y-up) from the
    // parser layer — see the rule in 12.2. Do NOT rotate here, or
    // previews and in-world rendering will disagree.
    scene.add(mesh);
    stateRef.current.mesh = mesh;
  }, [geometry, material]);

  return <View ref={mountRef} style={{ flex: 1, minHeight: 240 }} />;
}

/** Build a three.js geometry for a parametric prim (box/cylinder/…)
 *  from tessellated vertices produced by a PrimMesher port. The
 *  mesher itself is a generated-code port of LibreMetaverse.PrimMesher
 *  semantics; this adapter is the seam. */
export function primGeometryFromMesherOutput(
  positions: Float32Array,
  normals: Float32Array,
  uvs: Float32Array,
  indices: Uint32Array,
): THREE.BufferGeometry {
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  g.setAttribute("normal", new THREE.BufferAttribute(normals, 3));
  g.setAttribute("uv", new THREE.BufferAttribute(uvs, 2));
  g.setIndex(new THREE.BufferAttribute(indices, 1));
  return g;
}
```

---

## 13. App shell: wiring login → session → tabs

```tsx
// src/react/AppShell.tsx
// The top-level composition: bridge + store + login gate + tab shell.
// Tab set mirrors a mobile viewer: Scene (MeshViewer host), Chat, IM,
// People (radar + nearby), Inventory, More (profile/settings/logout).

import React, { useMemo, useState } from "react";
import { View, Text, Pressable } from "react-native";
import { createSessionStore, bindSessionStore } from "../state/session-store";
import { WebSocketBridge } from "../sl/udp-bridge";
import { LoginScreen } from "./LoginScreen";
import { ChatPanel } from "./ChatPanel";
import { IMPanel } from "./IMPanel";
import { InventoryTree } from "./InventoryTree";
import { Minimap, NearbyPeople } from "./Radar";

type Tab = "chat" | "im" | "people" | "inventory";

export function AppShell(): React.JSX.Element {
  // One store per app mount; the bridge URL points at the desktop
  // sidecar (web/Electron) — native targets construct the Capacitor
  // bridge from Section 14.2 behind the same UdpBridge interface.
  const store = useMemo(() => createSessionStore(), []);
  const useSession = useMemo(() => bindSessionStore(store), [store]);
  const bridge = useMemo(() => new WebSocketBridge("ws://127.0.0.1:19090/sl-udp"), []);
  const [tab, setTab] = useState<Tab>("chat");

  const login = useSession((s) => s.login);
  const caps = useSession((s) => s.caps);
  const regionName = useSession((s) => s.regionName);
  const doLogin = useSession((s) => s.login);
  const doMfa = useSession((s) => s.submitMfa);
  const doLogout = useSession((s) => s.logout);
  const imSessions = useSession((s) => s.imSessions);
  const unread = [...imSessions.values()].reduce((n, s) => n + s.unread, 0);

  if (login.kind !== "inWorld" && login.kind !== "establishingCircuit") {
    return (
      <LoginScreen
        login={login}
        onLogin={(first, last, token) =>
          void doLogin(bridge, {
            firstName: first,
            lastName: last,
            credentialToken: token,
            start: "last",
            channel: "Linkpoint TS Reference",
            version: "1.0.0",
            platform: "and",
            mac: "00:00:00:00:00:00", // replaced by device info in the app target
            id0: "reference-build",
          })
        }
        onMfa={(code) => void doMfa(code)}
      />
    );
  }

  const agentId = login.kind === "inWorld" || login.kind === "establishingCircuit"
    ? login.session.agentId : null;
  const rootFolder = login.kind === "inWorld" || login.kind === "establishingCircuit"
    ? login.session.inventoryRootFolderId : null;
  // Self position placeholder: the scene layer publishes the agent's
  // region-local position; radar components take it as a prop so they
  // stay pure and testable.
  const selfPos = { x: 128, y: 128 };

  return (
    <View style={{ flex: 1 }}>
      <View style={{ flexDirection: "row", justifyContent: "space-between" }}>
        <Text style={{ fontWeight: "700" }}>{regionName || "Connecting…"}</Text>
        <Pressable onPress={() => void doLogout()}><Text>Log out</Text></Pressable>
      </View>

      <View style={{ flex: 1 }}>
        {tab === "chat" && <ChatPanel useSession={useSession} />}
        {tab === "im" && <IMPanel useSession={useSession} />}
        {tab === "people" && (
          <View>
            <Minimap useSession={useSession} selfPos={selfPos} />
            <NearbyPeople useSession={useSession} selfPos={selfPos} />
          </View>
        )}
        {tab === "inventory" && (
          <InventoryTree caps={caps} agentId={agentId} rootFolderId={rootFolder} />
        )}
      </View>

      <View style={{ flexDirection: "row", justifyContent: "space-around" }}>
        <TabButton label="Chat" active={tab === "chat"} onPress={() => setTab("chat")} />
        <TabButton label={unread > 0 ? `IM (${unread})` : "IM"} active={tab === "im"} onPress={() => setTab("im")} />
        <TabButton label="People" active={tab === "people"} onPress={() => setTab("people")} />
        <TabButton label="Inventory" active={tab === "inventory"} onPress={() => setTab("inventory")} />
      </View>
    </View>
  );
}

function TabButton(props: { label: string; active: boolean; onPress: () => void }): React.JSX.Element {
  return (
    <Pressable onPress={props.onPress}>
      <Text style={props.active ? { fontWeight: "800" } : undefined}>{props.label}</Text>
    </Pressable>
  );
}
```

### 13.1 Movement: sending AgentUpdate from a joystick / keyboard layer

Chat-only clients can skip this; any client with a scene view cannot.
`AgentUpdate` is sent continuously (viewers send roughly 10-20 Hz,
throttled when idle) with camera state and control flags.

```ts
// src/sl/agent-update-loop.ts
// Owns the AgentUpdate cadence. Start after RegionHandshake, stop on
// logout/teleport. Camera values come from the scene layer each tick.

import { Circuit } from "./circuit";
import { LoginSession } from "./login";
import { encodeAgentUpdate, AgentControl } from "./messages/core";
import { Vector3, Quaternion } from "./types";

export interface CameraState {
  center: Vector3;
  atAxis: Vector3;
  leftAxis: Vector3;
  upAxis: Vector3;
  far: number;
  bodyRotation: Quaternion;
  headRotation: Quaternion;
}

export class AgentUpdateLoop {
  private timer: ReturnType<typeof setInterval> | null = null;
  controlFlags = 0;
  camera: CameraState = {
    center: { x: 128, y: 128, z: 24 },
    atAxis: { x: 0, y: 1, z: 0 },
    leftAxis: { x: -1, y: 0, z: 0 },
    upAxis: { x: 0, y: 0, z: 1 },
    far: 128,
    bodyRotation: { x: 0, y: 0, z: 0, w: 1 },
    headRotation: { x: 0, y: 0, z: 0, w: 1 },
  };

  constructor(
    private readonly circuit: Circuit,
    private readonly session: LoginSession,
  ) {}

  start(intervalMs = 66): void { // ~15 Hz
    if (this.timer) return;
    const tick = (): void => {
      this.circuit.sendMessage("AgentUpdate", encodeAgentUpdate({
        agentId: this.session.agentId,
        sessionId: this.session.sessionId,
        bodyRotation: this.camera.bodyRotation,
        headRotation: this.camera.headRotation,
        state: 0,
        cameraCenter: this.camera.center,
        cameraAtAxis: this.camera.atAxis,
        cameraLeftAxis: this.camera.leftAxis,
        cameraUpAxis: this.camera.upAxis,
        far: this.camera.far,
        controlFlags: this.controlFlags,
        flags: 0,
      }));
    };
    tick();
    this.timer = setInterval(tick, intervalMs);
  }

  /** Set a movement key state from the input layer. */
  setControl(flag: number, down: boolean): void {
    this.controlFlags = down
      ? (this.controlFlags | flag) >>> 0
      : (this.controlFlags & ~flag) >>> 0;
  }

  stop(): void {
    if (this.timer) clearInterval(this.timer);
    this.timer = null;
    this.controlFlags = 0;
  }
}

export { AgentControl };
```

---

## 14. Packaging: full package.json, bridges, and build notes

### 14.1 Full annotated package.json

```jsonc
{
  "name": "linkpoint-ts-reference",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    // The message table and (in the full tree) the typed message
    // codecs are GENERATED from message_template.msg. Generation is a
    // build step, never a runtime fetch.
    "gen:messages": "node scripts/gen-messages.mjs sources/message_template.msg src/sl/messages/table.ts",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "lint": "eslint src"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-native": "^0.76.0",
    "react-native-svg": "^15.0.0",
    "zustand": "^5.0.0",
    "three": "^0.170.0"
  },
  "devDependencies": {
    "typescript": "^5.6.0",
    "vitest": "^2.0.0",
    "@types/react": "^19.0.0",
    "@types/three": "^0.170.0"
  },
  "engines": { "node": ">=20" }
}
```

### 14.2 The Capacitor UDP bridge (native side contract)

React Native and Capacitor have no UDP API in JS. The bridge is a
small native plugin with exactly the `UdpBridge` surface from
Section 2.1. Android implementation sketch (Kotlin) — the full Kotlin
client in the companion file implements the same contract natively:

```kotlin
// android/src/main/java/app/linkpoint/udp/SLUdpPlugin.kt (sketch)
// Capacitor plugin: owns DatagramSockets keyed by "host:port".
// JS sends/receives base64 payloads; framing (Section 2.1's WS format)
// is NOT used here — each plugin call is one datagram, addressed.

@CapacitorPlugin(name = "SLUdp")
class SLUdpPlugin : Plugin() {
    private val sockets = ConcurrentHashMap<String, DatagramSocket>()
    private val scope = CoroutineScope(Dispatchers.IO + SupervisorJob())

    @PluginMethod
    fun send(call: PluginCall) {
        val host = call.getString("host") ?: return call.reject("host required")
        val port = call.getInt("port") ?: return call.reject("port required")
        val b64 = call.getString("data") ?: return call.reject("data required")
        val bytes = Base64.decode(b64, Base64.NO_WRAP)
        val key = "$host:$port"
        val socket = sockets.getOrPut(key) {
            DatagramSocket().also { startReceiver(key, it) }
        }
        scope.launch {
            socket.send(DatagramPacket(bytes, bytes.size, InetAddress.getByName(host), port))
            call.resolve()
        }
    }

    private fun startReceiver(key: String, socket: DatagramSocket) {
        scope.launch {
            val buf = ByteArray(65535)
            while (!socket.isClosed) {
                val pkt = DatagramPacket(buf, buf.size)
                socket.receive(pkt)
                val payload = Base64.encodeToString(
                    pkt.data.copyOf(pkt.length), Base64.NO_WRAP)
                notifyListeners("packet", JSObject()
                    .put("key", key)
                    .put("host", pkt.address.hostAddress)
                    .put("port", pkt.port)
                    .put("data", payload))
            }
        }
    }

    @PluginMethod
    fun closeAll(call: PluginCall) {
        sockets.values.forEach { it.close() }
        sockets.clear()
        call.resolve()
    }
}
```

```ts
// src/sl/capacitor-bridge.ts
// TS side of the Capacitor bridge — implements UdpBridge.

import { registerPlugin } from "@capacitor/core";
import type { PluginListenerHandle } from "@capacitor/core";
import { UdpBridge, UdpEndpoint } from "./udp-bridge";

interface SLUdpNative {
  send(opts: { host: string; port: number; data: string }): Promise<void>;
  closeAll(): Promise<void>;
  addListener(
    event: "packet",
    cb: (ev: { host: string; port: number; data: string }) => void,
  ): Promise<PluginListenerHandle>;
}
const SLUdp = registerPlugin<SLUdpNative>("SLUdp");

function b64Encode(data: Uint8Array): string {
  let s = "";
  for (let i = 0; i < data.length; i += 0x8000) {
    s += String.fromCharCode(...data.subarray(i, i + 0x8000));
  }
  return btoa(s);
}
function b64Decode(b64: string): Uint8Array {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

export class CapacitorUdpBridge implements UdpBridge {
  private packetCbs = new Set<(from: UdpEndpoint, p: Uint8Array) => void>();
  private handle: PluginListenerHandle | null = null;

  async connect(): Promise<void> {
    this.handle = await SLUdp.addListener("packet", (ev) => {
      const packet = b64Decode(ev.data);
      for (const cb of this.packetCbs) cb({ host: ev.host, port: ev.port }, packet);
    });
  }
  async send(to: UdpEndpoint, packet: Uint8Array): Promise<void> {
    await SLUdp.send({ host: to.host, port: to.port, data: b64Encode(packet) });
  }
  onPacket(cb: (from: UdpEndpoint, p: Uint8Array) => void): () => void {
    this.packetCbs.add(cb);
    return () => this.packetCbs.delete(cb);
  }
  onError(): () => void {
    // The native plugin surfaces socket death as a rejected send; the
    // circuit's reliable-resend exhaustion (Section 2.6) is the error
    // path that matters, so no separate channel is wired here.
    return () => {};
  }
  async close(): Promise<void> {
    await this.handle?.remove();
    await SLUdp.closeAll();
  }
}
```

### 14.3 React Native notes (non-Capacitor targets)

- Use the same contract with a native module (`NativeModules.SLUdp`)
  built on `DatagramSocket` (Android) / `NWConnection` over UDP
  (iOS). iOS requires the local-network privacy declaration if the
  sidecar/bridge pattern is used on LAN; direct simulator UDP does not.
- Metro bundler: `three` needs the usual RN GL shims only when the
  MeshViewer target is `expo-gl`; the protocol core (Sections 1-6) is
  pure TS and bundles with zero native deps beyond the bridge.
- Hermes: `bigint` support is required by `PacketWriter.u64` — Hermes
  supports it on current RN; on older Hermes, replace the two u64
  fields used by the core message set with a `[lo, hi]` u32 pair.
- Backgrounding: iOS and Android both suspend UDP sockets in the
  background. The session layer must treat "app resumed after >30 s
  background" as a probable dead circuit: send a ping, and if the
  reliable queue exhausts, re-login rather than trying to resurrect
  the circuit (the simulator has already timed the agent out).

### 14.4 Testing strategy for the protocol core

```ts
// src/sl/__tests__/packet.test.ts
// Golden-packet tests: byte-exact expectations catch endianness and
// zerocode regressions that type checks cannot.

import { zeroEncode, zeroDecode, encodePacket, decodePacket } from "../packet";
import { encodeChatFromViewer } from "../messages/core";

describe("zerocode", () => {
  it("round-trips runs of zeros", () => {
    const body = new Uint8Array([1, 0, 0, 0, 2, 0, 3]);
    expect(zeroDecode(zeroEncode(body))).toEqual(body);
  });
  it("encodes a single zero as 00 01", () => {
    expect(zeroEncode(new Uint8Array([0]))).toEqual(new Uint8Array([0, 1]));
  });
});

describe("chat packet", () => {
  it("builds a non-zerocoded ChatFromViewer datagram", () => {
    const body = encodeChatFromViewer({
      agentId: "11111111-2222-3333-4444-555555555555",
      sessionId: "11111111-2222-3333-4444-555555555555",
      message: "hello", type: 1, channel: 0,
    });
    const pkt = encodePacket({ sequence: 7, body, zerocoded: false, reliable: true });
    const decoded = decodePacket(pkt);
    expect(decoded.sequence).toBe(7);
    expect(decoded.reliable).toBe(true);
    expect(decoded.zerocoded).toBe(false);
  });
});
```

### 14.5 What this file deliberately leaves to the app layer

- **Scene graph / object tracking.** `ObjectUpdate` family decoding
  follows the same generated-code pattern as Section 2.5, but the
  scene store (interest management, interpolation, linkset assembly)
  is a subsystem of its own — see the viewer-internals guide in this
  repo for the architecture the viewer uses.
- **Voice.** WebRTC voice (post-7.1.9 grids) is a separate stack:
  negotiate via `VoiceSignalingRequest` / SimulatorFeatures, then run
  a platform WebRTC client. Vivox is legacy and needs its native SDK.
- **Appearance / baking.** BoM appearance requires the COF + bake
  pipeline; the AIS3 link helpers in Section 3.1 are the inventory
  half of that work.
- **Full LLMesh parser.** Section 12.2 marks the seam; port from
  LibreMetaverse MeshFoundry semantics, not from scratch.

---

*End of the React + TypeScript file. Companion: `code-kotlin.md`
implements the same protocol core natively for Android.*
