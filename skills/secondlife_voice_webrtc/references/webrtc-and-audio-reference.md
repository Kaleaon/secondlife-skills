# Second Life WebRTC Voice and Spatial Audio Reference

Derived from canonical upstream sources: `secondlife/viewer` (`indra/newview/llvoicewebrtc.cpp`, `indra/llwebrtc/llwebrtc.cpp`, `indra/llaudio/llaudioengine.h`, `indra/llmessage/message_template.msg` — LGPL-2.1), `cinderblocks/libremetaverse` (`LibreMetaverse.Voice.WebRTC`, `LibreMetaverse.Voice.Vivox`, `LibreMetaverse.Protocol` — BSD-3), and `Kaleaon/react-linkpoint` (`src/linkpoint/voice-protocol.ts`, `core/sl-sounds.cjs`) / `Kaleaon/Linkpoint` (`WebRtcVoiceSession.kt`, `SLWebRTCTransportAdapter.kt`, `SoundFlags.kt`). Do not copy LGPL-2.1 C++ files verbatim into permissive codebases; port wire contracts and algorithms from `LibreMetaverse.Voice.WebRTC` (BSD-3) and verify behaviour against `secondlife/viewer`.

---

## 1. Dual Voice Architecture & Provider Selection

Second Life regions and OpenSimulator grids expose incompatible voice backends. A client must negotiate the active backend per region from `SimulatorFeatures` rather than hardcoding a single provider or starting two stacks concurrently.

| Provider key (`VoiceServerType`) | Status on Agni (2024+) | Transport & media | Normative / reference implementations | Licensing & redistribution |
|---|---|---|---|---|
| `"webrtc"` | **Primary** since official viewer `7.1.9` (`2024-08-13`) | HTTPS LLSD capability signaling + SRTP Opus 48 kHz stereo + SCTP `"SLData"` data channel | `secondlife/viewer` (`indra/newview/llvoicewebrtc.cpp`, `indra/llwebrtc/llwebrtc.cpp`, `secondlife/3p-webrtc-build`), `LibreMetaverse.Voice.WebRTC` (BSD-3), `Kaleaon/react-linkpoint` (`src/linkpoint/voice-protocol.ts`) | Open standards (WebRTC / libwebrtc BSD); safe to ship in open viewers, web clients, and mobile apps |
| `"vivox"` | **Legacy** fallback during region/account transition | Out-of-process `SLVoice` daemon over local TCP/XML control pipe (`TCPPipe`) + SIP/RTP | `secondlife/viewer` (`llvoicevivox.cpp`), `LibreMetaverse.Voice.Vivox` (`VoiceGateway`, BSD-3 wrapper only), `Kaleaon/Lumiya-Redux` separate voice plugin APK | `SLVoice` binary is **proprietary and closed**; never plan to redistribute `SLVoice` from open sources |
| OpenSim modules (`janus`, `freeswitch`, `mumble`) | Third-party OpenSim grids only | Grid-specific (`os-webrtc-janus` WebRTC gateway, FreeSWITCH SIP, or Whisper/Mumble) | `opensim/opensim` (`bin/config-include/os-webrtc-janus.ini.example`, `FreeSwitchVoiceModule`) | BSD server modules; inspect `SimulatorFeatures` and `ProvisionVoiceAccountRequest` per region |

### Critical Architecture Rules

- **Gate strictly on `SimulatorFeatures`:** Request `SimulatorFeatures`, `ProvisionVoiceAccountRequest`, `ParcelVoiceInfoRequest`, and `VoiceSignalingRequest` (plus `ChatSessionRequest` for group and peer-to-peer calls) from the per-region `seed_capability` on every region entry and teleport.
- **Inspect `SimulatorFeatures["VoiceServerType"]`:** When `"webrtc"` is returned (or `ParcelVoiceInfoRequest` reports `voice_credentials["voice_server_type"] == "webrtc"`), initialise **only** the WebRTC stack. When `"vivox"` is returned, either attach to an external user-supplied `SLVoice` connector or surface a clean "Legacy Vivox region — WebRTC unavailable" state on mobile/web clients.
- **Never initialise both stacks blindly:** Spawning `LibreMetaverse.Voice.Vivox` alongside `LibreMetaverse.Voice.WebRTC` races on `ProvisionVoiceAccountRequest`, steals audio capture devices, and corrupts `viewer_session` state.
- **No peer-to-peer audio bridge:** There is **no** audio bridge between WebRTC-only clients and Vivox-only clients on the same channel, and WebRTC voice intentionally omits legacy Vivox voice morphing.
- **Neighbouring region sessions:** Spatial WebRTC voice connects one `RTCPeerConnection` per neighbouring region within hearing range, marking **at most one** session as `primary = true` via `"SLData"` `{"j": {"p": true}}` (the simulator whose mixed audio stream is rendered to the user). Crossing a region border swaps which session sends `{"j": {"p": true}}` versus `{"j": {"p": false}}` without tearing down and renegotiating from scratch.

---

## 2. STUN / TURN Topology by Grid

Prefer ICE servers returned dynamically by `ProvisionVoiceAccountRequest` (`ice_servers` array of `{ urls, username, credential }`). When falling back to grid STUN defaults, match official Linden Lab host counts:

| Grid | Default STUN URIs | Host count | Notes |
|---|---|---|---|
| **Agni** (production) | `stun:stun1.agni.secondlife.io:3478`<br>`stun:stun2.agni.secondlife.io:3478`<br>`stun:stun3.agni.secondlife.io:3478` | **3 hosts** (`stun1..stun3`) | Production Second Life grid; pair with provisioned TURN relays for CGNAT / mobile carriers |
| **Aditi** (beta grid) | `stun:stun1.aditi.secondlife.io:3478`<br>`stun:stun2.aditi.secondlife.io:3478` | **2 hosts** (`stun1..stun2`) | Beta test grid (e.g. `webRTC1`, `webRTC2` test regions) |
| **Other SL test grids** (`<grid>`) | `stun:stun1.<grid>.secondlife.io:3478`<br>`stun:stun2.<grid>.secondlife.io:3478` | **2 hosts** (`stun1..stun2`) | Pattern `stun1..stunN.<grid>.secondlife.io:3478` (`N = 3` on Agni, `N = 2` elsewhere) |

PeerConnection configuration requirements (`indra/llwebrtc/llwebrtc.cpp` and `LibreMetaverse.Voice.WebRTC`):
- `sdpSemantics = "unified-plan"`
- `bundlePolicy = "max-bundle"`
- `rtcpMuxPolicy = "require"`

---

## 3. HTTPS Capability Signaling & LLSD Payloads

Second Life WebRTC signaling uses **HTTPS POSTs carrying XML LLSD (`application/llsd+xml`)** to per-region capabilities — **not** WebSockets.

### 3.1 Mandatory Negotiation Order

1. Query `ParcelVoiceInfoRequest` (POST empty LLSD map `<llsd><map /></llsd>`) to learn whether parcel voice is enabled, `parcel_local_id`, `region_name`, and `voice_credentials` (`channel_uri`, `channel_credentials`, `voice_server_type`).
2. Instantiate `RTCPeerConnection` (`unified-plan`, `max-bundle`, `require` RTCP mux) and attach the microphone audio track (`echoCancellation`, `noiseSuppression`, `autoGainControl`).
3. **Create the `"SLData"` data channel BEFORE `createOffer()`:** `pc.createDataChannel("SLData", { ordered: true, negotiated: false })`. If `"SLData"` is created after `createOffer()`, the `m=application ... webrtc-datachannel` SCTP media section is missing from the offer SDP and the Second Life voice server rejects or silences spatial control.
4. Generate the SDP offer via `createOffer()`, **munge the Opus 48 kHz stereo `rtpmap` and `fmtp` lines** (Section 4), and call `setLocalDescription(mungedOffer)`.
5. Queue any local `onicecandidate` events emitted before the answer arrives.
6. POST the offer LLSD map to `ProvisionVoiceAccountRequest`, parse `jsep.sdp` (`type == "answer"`) and `viewer_session`, and call `setRemoteDescription(answer)`.
7. Drain queued ICE candidates to `VoiceSignalingRequest`, trickle subsequent candidates as they arrive, and send the `{ completed: true }` sentinel once `iceGatheringState === "complete"`.

### 3.2 `ParcelVoiceInfoRequest` Response Shape

```xml
<llsd>
  <map>
    <key>parcel_local_id</key><integer>1</integer>
    <key>region_name</key><string>Sandbox WebRTC</string>
    <key>voice_credentials</key>
    <map>
      <key>channel_uri</key><string>https://voice.agni.secondlife.io/...</string>
      <key>channel_credentials</key><string>opaque-token</string>
      <key>voice_server_type</key><string>webrtc</string>
    </map>
  </map>
</llsd>
```

Note: When parcel voice is disabled (`AllowVoice` off on parcel or estate), `channel_uri` is empty — disconnect any active spatial `local` channel cleanly without tearing down active `multiagent` group or P2P calls.

### 3.3 `ProvisionVoiceAccountRequest` — Spatial (`local`) Offer

```xml
<llsd>
  <map>
    <key>channel_type</key><string>local</string>
    <key>parcel_local_id</key><integer>1</integer>
    <key>voice_server_type</key><string>webrtc</string>
    <key>jsep</key>
    <map>
      <key>type</key><string>offer</string>
      <key>sdp</key><string>v=0&#13;&#10;...</string>
    </map>
  </map>
</llsd>
```

- Omit `parcel_local_id` when joining region-wide spatial chat (estate/region channel without parcel isolation); include `parcel_local_id` as an LLSD `<integer>` when parcel-scoped spatial voice is active.

### 3.4 `ProvisionVoiceAccountRequest` — Group / P2P (`multiagent`) Offer

Group, ad-hoc conference, and P2P IM voice sessions obtain `channel` and `credentials` from `ChatSessionRequest` (`method: "start conference"` or `"fetch history"` / voice session event on `EventQueueGet`), then POST to `ProvisionVoiceAccountRequest`:

```xml
<llsd>
  <map>
    <key>channel_type</key><string>multiagent</string>
    <key>channel</key><string>channel-uri-from-chatsession</string>
    <key>credentials</key><string>credentials-from-chatsession</string>
    <key>voice_server_type</key><string>webrtc</string>
    <key>jsep</key>
    <map>
      <key>type</key><string>offer</string>
      <key>sdp</key><string>v=0&#13;&#10;...</string>
    </map>
  </map>
</llsd>
```

### 3.5 `ProvisionVoiceAccountRequest` — Answer & Logout Payloads

**Server answer:**

```xml
<llsd>
  <map>
    <key>viewer_session</key><string>b8f4c1f2-...</string>
    <key>voice_server_type</key><string>webrtc</string>
    <key>jsep</key>
    <map>
      <key>type</key><string>answer</string>
      <key>sdp</key><string>v=0&#13;&#10;...</string>
    </map>
  </map>
</llsd>
```

**Explicit session logout** (sent on channel leave, region teardown, or client logout; ignore HTTP `404` if the server already reaped the session):

```xml
<llsd>
  <map>
    <key>logout</key><boolean>1</boolean>
    <key>viewer_session</key><string>b8f4c1f2-...</string>
    <key>voice_server_type</key><string>webrtc</string>
  </map>
</llsd>
```

### 3.6 `VoiceSignalingRequest` — Trickle ICE Batch vs Completion Sentinel

**CRITICAL PROTOCOL INVARIANT:** A `VoiceSignalingRequest` POST must contain **either** `candidates` (an LLSD array of trickle ICE candidate maps) **or** `candidate` (`{ completed: true }`), **never both in the same request**. Sending both keys in one LLSD map causes signaling failure on the voice gateway.

**Batch trickle ICE payload:**

```xml
<llsd>
  <map>
    <key>viewer_session</key><string>b8f4c1f2-...</string>
    <key>voice_server_type</key><string>webrtc</string>
    <key>candidates</key>
    <array>
      <map>
        <key>candidate</key><string>candidate:842163049 1 udp 1677729535 ...</string>
        <key>sdpMid</key><string>0</string>
        <key>sdpMLineIndex</key><integer>0</integer>
      </map>
    </array>
  </map>
</llsd>
```

**End-of-candidates sentinel payload:**

```xml
<llsd>
  <map>
    <key>viewer_session</key><string>b8f4c1f2-...</string>
    <key>voice_server_type</key><string>webrtc</string>
    <key>candidate</key>
    <map>
      <key>completed</key><boolean>1</boolean>
    </map>
  </map>
</llsd>
```

---

## 4. Opus 48 kHz Stereo SDP `fmtp` Munging

The Second Life WebRTC SFU/mixer mixes 3D spatialised audio server-side into a stereo 48 kHz Opus stream per listener. Standard WebRTC `createOffer()` defaults to mono capture/playback hints unless the Opus `rtpmap` and `fmtp` lines inside the `m=audio` section are rewritten before `setLocalDescription` and before POSTing `jsep.sdp`.

### Canonical `fmtp` String (`llvoicewebrtc.cpp` / `voice-protocol.ts`)

```text
minptime=10;useinbandfec=1;stereo=1;sprop-stereo=1;maxplaybackrate=48000;sprop-maxplaybackrate=48000;sprop-maxcapturerate=48000
```

| Parameter | Value | Purpose |
|---|---|---|
| `minptime` | `10` | Allows low-latency 10 ms Opus frames |
| `useinbandfec` | `1` | Enables Opus in-band forward error correction for lossy UDP links |
| `stereo` | `1` | Signals decoder readiness to receive stereo spatialised mix from the region voice server |
| `sprop-stereo` | `1` | Signals stereo capability on the stream |
| `maxplaybackrate` | `48000` | Fullband 48 kHz playback |
| `sprop-maxplaybackrate` | `48000` | Sender fullband 48 kHz playback hint |
| `sprop-maxcapturerate` | `48000` | 48 kHz capture hint |

### Reference TypeScript Implementation (`src/linkpoint/voice-protocol.ts` pattern)

```ts
export const SL_OPUS_FMTP =
  "minptime=10;useinbandfec=1;stereo=1;sprop-stereo=1;maxplaybackrate=48000;sprop-maxplaybackrate=48000;sprop-maxcapturerate=48000";

export function mungeSecondLifeOpusSdp(sdp: string): string {
  const lines = sdp.split(/\r?\n/);
  const out: string[] = [];
  let inAudio = false;
  let opusPt: string | null = null;
  let wroteFmtp = false;

  for (const line of lines) {
    if (line.startsWith("m=audio ")) {
      inAudio = true;
      opusPt = null;
      wroteFmtp = false;
      out.push(line);
      continue;
    }
    if (inAudio && line.startsWith("m=")) {
      if (opusPt && !wroteFmtp) {
        out.push(`a=fmtp:${opusPt} ${SL_OPUS_FMTP}`);
      }
      inAudio = false;
      out.push(line);
      continue;
    }
    if (inAudio) {
      const rtpmap = line.match(/^a=rtpmap:(\d+)\s+opus\/48000(?:\/\d+)?/i);
      if (rtpmap) {
        opusPt = rtpmap[1];
        out.push(`a=rtpmap:${opusPt} opus/48000/2`);
        continue;
      }
      if (opusPt && line.startsWith(`a=fmtp:${opusPt} `)) {
        out.push(`a=fmtp:${opusPt} ${SL_OPUS_FMTP}`);
        wroteFmtp = true;
        continue;
      }
    }
    out.push(line);
  }
  if (inAudio && opusPt && !wroteFmtp) {
    out.push(`a=fmtp:${opusPt} ${SL_OPUS_FMTP}`);
  }
  return out.join("\r\n");
}
```

---

## 5. `"SLData"` WebRTC Data Channel Protocol, Constants & Gain Quirk

`"SLData"` is a UTF-8 JSON SCTP data channel (`ordered: true`) carrying spatial positions, session primary handoff, per-peer mutes/gains, and live 100 ms mixer power/VAD frames.

### 5.1 Canonical Constants (`indra/newview/llvoicewebrtc.cpp`)

| Constant | Value | Meaning in `llvoicewebrtc.cpp` |
|---|---|---|
| `MAX_AUDIO_DIST` | `50.0` (`50m`) | Maximum spatial voice attenuation / culling radius in metres |
| `POSITION_UPDATE_INTERVAL_MS` | `100` (`100ms`) | Minimum throttle interval between outbound `"SLData"` spatial updates; skip sending when delta is unchanged |
| `VoiceEarLocation = 0` | `Camera` (`0`) | Listener position (`lp`) and heading (`lh`) follow the viewer camera (default in `settings.xml`) |
| `VoiceEarLocation = 1` | `Avatar` (`1`) | Listener position (`lp`) and heading (`lh`) follow the user's avatar head/pelvis, while speaker (`sp`/`sh`) stays at avatar |
| `VoiceEarLocation = 2` | `Mixed` (`2`) | Listener position (`lp`) at avatar position, listener orientation (`lh`) from camera heading |
| `LEVEL_SCALE` | `0.005` | Linear multiplier converting raw mixer power `p` into UI meter range |
| `LEVEL_START_POINT` | `0.18` | Base offset added above silence floor when mapping power into `[0.0, 1.0]` UI speaking rings |
| `SPEAKING_AUDIO_LEVEL` | `0.3` | Threshold on normalised level above which the avatar speaking dot / lip-sync indicator lights green |
| `JOIN_USER_VOLUME_SCALE` | `volume * 200` | Initial per-peer gain sent in `"ug"` when a participant first joins (`1.0` unity → `200`) |
| `SET_USER_VOLUME_SCALE` | `volume * 220` | Per-peer gain sent in `"ug"` from `LLVoiceWebRTCChannel::setUserVolume` (`1.0` slider → `220`) |

### 5.2 Official Viewer Per-Participant Gain Quirk (`* 200` vs `* 220`)

In `indra/newview/llvoicewebrtc.cpp`, the voice server expects integer per-user gains (`"ug": { "<agent-uuid>": <int> }`) where `200` represents nominal unity (`100%` × 2):
- **On participant join:** the viewer sends `int(volume * 200)` (so default `volume = 1.0f` maps to `200`, max `2.0f` maps to `400`).
- **In `setUserVolume(id, volume)`:** the official viewer multiplies by **`220`** (`int(volume * 220)`), producing a slight `+10%` boost when a user adjusts a participant's volume slider relative to the initial join gain.
- Document and preserve this distinction when comparing captured `"SLData"` frames or porting slider curves between `secondlife/viewer`, `LibreMetaverse.Voice.WebRTC`, and `react-linkpoint`.

### 5.3 Speaking Meter Mapping Formula

Given an inbound `"SLData"` peer frame `{"<agent-uuid>": {"p": powerRaw, "V": vad}}`:

```ts
export const LEVEL_SCALE = 0.005;
export const LEVEL_START_POINT = 0.18;
export const SPEAKING_AUDIO_LEVEL = 0.3;

export function computeVoiceLevel(powerRaw: number, vad: boolean): {
  level: number;
  isSpeaking: boolean;
} {
  if (!vad && powerRaw <= 0) {
    return { level: 0, isSpeaking: false };
  }
  // Map mixer power into [0, 1] matching viewer speaking visualizer curve
  const scaled = Math.min(1.0, Math.max(0.0, LEVEL_START_POINT + powerRaw * LEVEL_SCALE));
  const isSpeaking = vad || scaled >= SPEAKING_AUDIO_LEVEL;
  return { level: scaled, isSpeaking };
}
```

### 5.4 `"SLData"` Client → Server JSON Payloads

All spatial coordinates in `"SLData"` are **global world coordinates in centimetres** (`Math.round((regionOriginMeters + localMeters) * 100)` as `{ x, y, z }` integers), and headings are unit quaternions scaled by `100` and rounded to integers (`{ x, y, z, w }`).

| Message | JSON shape | When to send |
|---|---|---|
| **Join / Primary role** | `{"j": {"p": true}}` or `{"j": {"p": false}}` | Immediately after `"SLData"` opens, and when crossing between neighbouring region voice sessions |
| **Leave session** | `{"l": true}` | Before closing a spatial or multiagent session |
| **Spatial position & ear** | `{"sp":{"x":25612800,"y":25612800,"z":2520},"sh":{"x":0,"y":0,"z":71,"w":71},"lp":{"x":25612500,"y":25612800,"z":2680},"lh":{"x":0,"y":0,"z":71,"w":71}}` | Spatial (`local`) channels only, throttled to `>= 100ms`, applying `VoiceEarLocation` (`0` Camera, `1` Avatar, `2` Mixed) to `lp`/`lh` while keeping `sp`/`sh` on the avatar |
| **Per-peer mute map** | `{"m": {"00000000-0000-4000-8000-000000000001": true}}` | When local user mutes/unmutes a speaker |
| **Per-peer gain map** | `{"ug": {"00000000-0000-4000-8000-000000000001": 220}}` | `Math.round(volume * 200)` on initial join sync; `Math.round(volume * 220)` on user slider change (`setUserVolume`) |
| **Liveness ping** | `{"ping": true}` | Optional periodic data-channel liveness probe (`LibreMetaverse.Voice.WebRTC`) |

### 5.5 `"SLData"` Server → Client JSON Payloads

| Key / shape | Example | Meaning |
|---|---|---|
| `<uuid>.j` | `{"<agent-uuid>": {"j": {"p": true}}}` | Participant joined channel (`p` indicates primary session) |
| `<uuid>.l` | `{"<agent-uuid>": {"l": true}}` | Participant left channel |
| `<uuid>.p` / `<uuid>.V` | `{"<agent-uuid>": {"p": 42, "V": true}}` | 100 ms mixer energy (`p`) and voice activity detection (`V`) |
| `m` | `{"m": {"<agent-uuid>": true}}` | Estate / group moderator-enforced mute state |
| `ug` | `{"ug": {"<agent-uuid>": 200}}` | Server / moderator gain state |

---

## 6. Parcel Audio & Media Streams (`ParcelProperties`)

Second Life parcels carry two distinct streaming endpoints:
1. **`MusicURL`**: Shoutcast / Icecast / HTTP audio stream (`audio/mpeg`, `audio/ogg`, `audio/aac`) controlled by `AudioLevelMusic`.
2. **`MediaURL`** + `MediaType` / `MediaID` / `MediaAutoScale` / `MediaLoop`: Parcel media texture or video stream controlled by `AudioLevelMedia`.

### `EventQueueGet` Primary Path vs LLUDP Fallback

In `message_template.msg`, UDP `ParcelProperties` is marked `High 23 Trusted Zerocoded UDPDeprecated`:
- **Agni / Aditi (Capabilities primary):** Parse `ParcelProperties` events from the `EventQueueGet` LLSD response (`event["message"] == "ParcelProperties"`, `event["body"]["ParcelData"][0]["MusicURL"]` and `["MediaURL"]`).
- **OpenSimulator fallback:** Many OpenSim configurations still deliver `ParcelProperties` over UDP (`High 23`, packet ID byte `0x17`, **`Zerocoded`** — apply `ZeroDecode` before reading fields!). Support both paths deduplicated by `SequenceID` and `LocalID`, trimming whitespace on `MusicURL` and stopping playback cleanly when `MusicURL` becomes `""` or the user disables parcel musicautoplay.

---

## 7. Spatial & Attached LLUDP Sound Messages (`Unencoded`)

All four simulator-to-viewer sound packets in `message_template.msg` are **`Unencoded`** (never zero-decode their bodies unless the packet header itself explicitly sets `0x80` `MSG_ZEROCODED`, which simulators do not set on these four messages). Sound assets (`AssetType.Sound = 1`) are Ogg Vorbis streams fetched by `SoundID` UUID over HTTP asset/capability paths (or legacy Xfer on old OpenSim).

### 7.1 Wire Layout Catalogue (Verified Against `message_template.msg`)

| Message | Frequency & ID | Wire ID bytes | Trust / Encoding | Block & exact field order |
|---|---|---|---|---|
| `SoundTrigger` | `High 29` | `0x1D` (1 byte) | `NotTrusted` / **`Unencoded`** | `SoundData Single`: `SoundID` (`LLUUID`, 16B), `OwnerID` (`LLUUID`, 16B), `ObjectID` (`LLUUID`, 16B), `ParentID` (`LLUUID`, 16B), `Handle` (`U64`, 8B), `Position` (`LLVector3`, 12B), `Gain` (`F32`, 4B) — **total payload 88 bytes** |
| `AttachedSound` | `Medium 13` | `0xFF 0x0D` (2 bytes) | `Trusted` / **`Unencoded`** | `DataBlock Single`: `SoundID` (`LLUUID`, 16B), `ObjectID` (`LLUUID`, 16B), `OwnerID` (`LLUUID`, 16B), `Gain` (`F32`, 4B), `Flags` (`U8`, 1B) — **total payload 53 bytes** |
| `AttachedSoundGainChange` | `Medium 14` | `0xFF 0x0E` (2 bytes) | `Trusted` / **`Unencoded`** | `DataBlock Single`: `ObjectID` (`LLUUID`, 16B), `Gain` (`F32`, 4B) — **total payload 20 bytes** |
| `PreloadSound` | `Medium 15` | `0xFF 0x0F` (2 bytes) | `Trusted` / **`Unencoded`** | `DataBlock Variable`: `Count` (`U8`, 1B) + `Count ×` (`ObjectID` `LLUUID` 16B, `OwnerID` `LLUUID` 16B, `SoundID` `LLUUID` 16B — 48B per entry) |

Note on UUID endianness vs scalars in LLUDP: `LLUUID` is 16 raw big-endian network bytes, whereas `U64` (`Handle`), `LLVector3` (`3 × F32`), and `F32` (`Gain`) in `message_template.msg` body blocks are **little-endian**!

### 7.2 `AttachedSound` `Flags` Bitmask vs LSL `SOUND_*` Constants

Watch the classic protocol trap: the `Flags` (`U8`) byte inside `AttachedSound` (`indra/llaudio/llaudioengine.h` / `llsoundflags.h` and `core/sl-sounds.cjs`) uses **different bit values** from the newer LSL `llSound()` script constants in `lsl_definitions.yaml`!

#### Wire `AttachedSound.DataBlock.Flags` (`U8` on UDP `Medium 13`)

| Wire constant (`llsoundflags.h`) | Hex / bit | Behaviour required in viewer audio engine |
|---|---|---|
| `SOUND_PLAY` | `0x00` | Default one-shot attached playback moving with `ObjectID` |
| `SOUND_LOOP` | `0x01` | Loop continuously on `ObjectID` until replaced, stopped (`0x10` or `NULL_KEY`), or `KillObject` removes `ObjectID` |
| `SOUND_SYNC_MASTER` | `0x02` | Marks `ObjectID`'s audio source as a phase-sync master (`llLoopSoundMaster` / `llPlaySound` sync) |
| `SOUND_SYNC_SLAVE` | `0x04` | Aligns playback cursor (`currentTime` / sample offset) to the active `SOUND_SYNC_MASTER` owned by the same `OwnerID` (`llLoopSoundSlave` / `llPlaySoundSlave`) |
| `SOUND_QUEUE` | `0x08` | **Single-slot queue (`llSetSoundQueueing`):** if `ObjectID` is already playing a sound, place this sound in `ObjectID`'s **1-deep pending slot** (overwriting any previous queued entry, never growing an unbounded queue) and start it seamlessly when the current clip finishes |
| `SOUND_STOP` | `0x10` | Immediately stop active and queued sounds on `ObjectID` (`llStopSound`) |

*(For comparison, inside LSL script source code `llSound(sound, volume, queue, flags)` in `lsl_definitions.yaml` uses `SOUND_PLAY = 0x00`, `SOUND_LOOP = 0x01`, `SOUND_TRIGGER = 0x02`, `SOUND_SYNC = 0x04` — the simulator translates LSL script calls into either `SoundTrigger` or `AttachedSound` wire flags above.)*

### 7.3 Spatialisation, HUD Bypass & Attenuation Rules (`core/sl-sounds.cjs`)

- **`SoundTrigger` (`High 29`):** Plays a non-attached one-shot world sound fixed at `(Handle, Position)` even if `ObjectID` later moves or is deleted. If `SoundID == NULL_KEY` (`00000000-0000-0000-0000-000000000000`), ignore silently.
- **`AttachedSound` (`Medium 13`):** Binds an audio source to `ObjectID` (one active voice + **one** queued slot per prim):
  - **HUD attachments (`attachmentPoint` in `31..38`, `ATTACH_HUD_*`):** Play **non-spatially** (head-locked stereo/mono at `Gain * AudioLevelSFX * AudioLevelMaster`) audible only to the wearing agent, never attenuated by world camera distance.
  - **In-world prims & body attachments:** Track `ObjectID`'s live world transform each frame (resolving child prims via `ParentID`), applying OpenAL / WebAudio PannerNode inverse-distance rolloff (`DEFAULT_MIN_DISTANCE = 2.0m`, `AudioLevelRolloff`, `MAX_AUDIO_DIST` culling).
  - **Unlisted object fallback:** Because `AttachedSound` (`Medium 13`) can arrive over UDP slightly before `ObjectUpdate` on region entry, hold or attenuate unlisted `ObjectID`s safely and bind their 3D position as soon as the object enters the scene table (expiring orphan sources after `ATTACHED_OBJECT_TIMEOUT = 5.0s`).
- **`AttachedSoundGainChange` (`Medium 14`):** Clamp `Gain` to `[0.0, 1.0]` and update the live `GainNode` / OpenAL source gain on `ObjectID` without restarting sample playback.
- **`PreloadSound` (`Medium 15`):** Prefetch and decode each `SoundID` into the LRU audio buffer cache without playing it so subsequent `AttachedSound` or `SoundTrigger` calls start with zero decode latency.

### 7.4 Reference TypeScript Audio Packet & Queue Handler (`core/sl-sounds.cjs` pattern)

```ts
export const WireSoundFlags = {
  SOUND_PLAY: 0x00,
  SOUND_LOOP: 0x01,
  SOUND_SYNC_MASTER: 0x02,
  SOUND_SYNC_SLAVE: 0x04,
  SOUND_QUEUE: 0x08,
  SOUND_STOP: 0x10,
} as const;

export interface PrimSoundSlot {
  activeSoundId: string | null;
  activeFlags: number;
  gain: number;
  /** Single-slot queue matching llSetSoundQueueing(TRUE): max depth 1. */
  queued: { soundId: string; gain: number; flags: number } | null;
}

export function applyAttachedSound(
  slots: Map<string, PrimSoundSlot>,
  objectId: string,
  soundId: string,
  gain: number,
  flags: number
): { action: "stop" | "queue" | "play"; slot: PrimSoundSlot } {
  const clampedGain = Math.max(0, Math.min(1, gain));
  const NULL_UUID = "00000000-0000-0000-0000-000000000000";
  const slot = slots.get(objectId) ?? {
    activeSoundId: null,
    activeFlags: 0,
    gain: clampedGain,
    queued: null,
  };

  if ((flags & WireSoundFlags.SOUND_STOP) !== 0 || soundId === NULL_UUID) {
    slot.activeSoundId = null;
    slot.activeFlags = 0;
    slot.queued = null;
    slots.set(objectId, slot);
    return { action: "stop", slot };
  }

  if ((flags & WireSoundFlags.SOUND_QUEUE) !== 0 && slot.activeSoundId !== null) {
    // Single-slot replacement: overwrites any previously queued clip on this prim
    slot.queued = { soundId, gain: clampedGain, flags };
    slots.set(objectId, slot);
    return { action: "queue", slot };
  }

  slot.activeSoundId = soundId;
  slot.activeFlags = flags;
  slot.gain = clampedGain;
  slot.queued = null;
  slots.set(objectId, slot);
  return { action: "play", slot };
}
```

---

## 8. Upstream File & Settings Cross-Check Index

### `secondlife/viewer` (LGPL-2.1)
- `indra/newview/llvoicewebrtc.cpp` & `.h`: `LLVoiceWebRTCClient`, `LLVoiceWebRTCChannel`, `ProvisionVoiceAccountRequest` / `VoiceSignalingRequest` LLSD builders, Opus SDP munging, `"SLData"` handler, `MAX_AUDIO_DIST = 50.0`, `LEVEL_SCALE = 0.005`, `LEVEL_START_POINT = 0.18`, `SPEAKING_AUDIO_LEVEL = 0.3`, `volume * 200` vs `volume * 220` gain scaling.
- `indra/llwebrtc/llwebrtc.cpp` & `llwebrtc_impl.h`: Native `libwebrtc` wrapper (`secondlife/3p-webrtc-build`), `RTCPeerConnection` and `"SLData"` SCTP wiring.
- `indra/llaudio/llaudioengine.cpp`, `llaudioengine_openal.cpp`, `indra/newview/llaudiosourcevo.cpp`: OpenAL 3D rolloff, attached prim source lifecycle, sync master/slave phase matching, single-slot sound queueing, and HUD non-spatial routing.
- `indra/newview/llviewerparcelmedia.cpp` & `llviewerparcelmgr.cpp`: `ParcelProperties` `MusicURL` and `MediaURL` stream lifecycle.
- `indra/newview/app_settings/settings.xml`: `EnableVoiceChat` (`1`), `VoiceEarLocation` (`0`), `VoiceServerType` (`""`), `AudioLevelMaster` (`1.0`), `AudioLevelVoice` (`0.5`), `AudioLevelSFX` (`0.5`), `AudioLevelMusic` (`0.3`), `AudioLevelMedia` (`0.3`), `AudioLevelAmbient` (`0.5`), `AudioLevelRolloff` (`1.0`), `AudioLevelUnderwaterRolloff` (`5.0`).

### `cinderblocks/libremetaverse` (BSD-3)
- `LibreMetaverse.Voice.WebRTC/VoiceManager.cs`: `ConnectPrimaryRegionAsync`, `RequestParcelVoiceInfoAsync`, `JoinGroupVoiceAsync`, `StartP2PCallAsync`, `AcceptP2PCallAsync`, `SetPeerMute`, `SetPeerGain`.
- `LibreMetaverse.Voice.WebRTC/VoiceSession.cs`: `CreatePeerConnectionAsync`, `RequestProvisionAsync`, `SendJoin`, `SendLeave`, `SendPosition`, `SendMuteMap`, `SendGainMap`, `CloseSessionAsync`.
- `LibreMetaverse.Voice.WebRTC/PeerManager.cs` & `OpusEncoder.cs`: SSRC-to-UUID peer mapping, `"SLData"` JSON/OSD parsing, and 48 kHz Opus encode/decode contexts.
- `LibreMetaverse.Voice.Vivox/VoiceGateway.cs`: Legacy `SLVoice` daemon TCP XML connector (keep isolated from WebRTC).
