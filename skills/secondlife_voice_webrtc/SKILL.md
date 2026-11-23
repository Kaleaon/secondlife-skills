---
name: secondlife_voice_webrtc
description: "Implement Second Life WebRTC voice signaling, Opus 48 kHz stereo SDP munging, SLData spatial updates, parcel media streams, and Unencoded LLUDP spatial and attached audio."
---

# Second Life WebRTC Voice and Spatial Audio

## Gate voice on SimulatorFeatures first

- Request `SimulatorFeatures`, `ProvisionVoiceAccountRequest`, `ParcelVoiceInfoRequest`, and `VoiceSignalingRequest`, plus `ChatSessionRequest` for group and peer-to-peer calls, from the per-region seed capability on every region entry and teleport.

- Branch voice initialisation strictly on `SimulatorFeatures["VoiceServerType"]`: `"webrtc"` has been the primary provider since official viewer 7.1.9 in August 2024 (`indra/newview/llvoicewebrtc.cpp` and `indra/llwebrtc/llwebrtc.cpp`), while `"vivox"` is the legacy out-of-process `SLVoice` daemon.

- Never initialise both voice stacks blindly in `LibreMetaverse` (`.Voice.WebRTC` versus `.Voice.Vivox`) or in a mobile or web client, because concurrent provisioning races on `ProvisionVoiceAccountRequest` and corrupts `viewer_session` state.

- Remember there is no peer-to-peer audio bridge between WebRTC-only and Vivox-only clients, WebRTC voice has no legacy voice morphing, and `SLVoice` is proprietary and closed so open clients ship WebRTC only.

- On OpenSimulator grids, inspect `SimulatorFeatures` and region voice caps before connecting, because OpenSim regions split across Janus WebRTC (`os-webrtc-janus`), FreeSWITCH, Mumble, or licensed Vivox.

## Negotiate WebRTC caps, STUN, and Opus SDP in exact order

- Configure `RTCPeerConnection` with Unified Plan SDP, `max-bundle`, and `require` RTCP mux, preferring `ice_servers` returned by `ProvisionVoiceAccountRequest` and falling back to `stun:stun1..stun3.agni.secondlife.io:3478` on Agni (3 hosts) versus `stun:stun1..stun2.<grid>.secondlife.io:3478` on Aditi and other Second Life grids (2 hosts).

- Create the ordered `"SLData"` WebRTC data channel (`pc.createDataChannel("SLData", { ordered: true })`) **before** calling `createOffer()`, or the SCTP media line will be absent from the offer SDP and the Second Life voice server will reject spatial control.

- Munge the offer SDP's Opus `rtpmap` to `opus/48000/2` and its `a=fmtp:<PT>` line to `minptime=10;useinbandfec=1;stereo=1;sprop-stereo=1;maxplaybackrate=48000;sprop-maxplaybackrate=48000;sprop-maxcapturerate=48000` before `setLocalDescription` so the server streams a fullband 48 kHz stereo spatial mix with forward error correction.

- Queue local ICE candidates gathered prior to receiving the SDP answer, POST the offer LLSD to `ProvisionVoiceAccountRequest`, apply `setRemoteDescription(answer)`, and only then trickle candidates to `VoiceSignalingRequest`.

- Enforce the `VoiceSignalingRequest` mutual-exclusion rule: send **either** `candidates` (batch array of `{ candidate, sdpMid, sdpMLineIndex }`) **or** `candidate = { completed: true }`, **never both** in the same LLSD request.

- Tear down sessions cleanly by POSTing `{ logout: true, viewer_session, voice_server_type: "webrtc" }` to `ProvisionVoiceAccountRequest`, treating HTTP 404 as benign when the server has already closed the session.

## Drive the SLData channel and respect viewer meter and gain quirks

- Send `"SLData"` JSON `{"j": {"p": true}}` on the primary region voice session and `{"j": {"p": false}}` on neighbouring region sessions within hearing range, swapping primary role on region crossing instead of disconnecting and renegotiating.

- Throttle spatial position updates on `"SLData"` to `100ms` (`MAX_AUDIO_DIST = 50m`) in global world centimetres (`sp`, `lp`) and integer-scaled (`×100`) quaternions (`sh`, `lh`), applying `VoiceEarLocation`: `0` Camera, `1` Avatar, or `2` Mixed (avatar position with camera heading).

- Map mixer power frames `{"<uuid>": {"p": power, "V": vad}}` using `indra/newview/llvoicewebrtc.cpp` constants: `LEVEL_SCALE = 0.005`, `LEVEL_START_POINT = 0.18`, and `SPEAKING_AUDIO_LEVEL = 0.3` for speaking indicators and lip-sync triggers.

- Preserve the official viewer's per-participant gain scaling quirk in `"ug"` maps: `llvoicewebrtc.cpp` sends `int(volume * 200)` when a participant first joins, whereas `setUserVolume` sends `int(volume * 220)`.

## Handle parcel streams and Unencoded LLUDP spatial audio

- Parse parcel `MusicURL` and `MediaURL` from `ParcelProperties` events over `EventQueueGet` LLSD on Agni (where UDP `ParcelProperties` is `UDPDeprecated`), while keeping a `High 23` (`0x17`, `Zerocoded`) UDP fallback for OpenSim.

- Decode all four simulator sound packets strictly as **`Unencoded`** per `message_template.msg`: `SoundTrigger` (`High 29 = 0x1D`), `AttachedSound` (`Medium 13 = 0xFF0D`), `AttachedSoundGainChange` (`Medium 14 = 0xFF0E`), and `PreloadSound` (`Medium 15 = 0xFF0F`).

- Honour `AttachedSound` wire bitflags (`SOUND_PLAY = 0x00`, `SOUND_LOOP = 0x01`, `SOUND_SYNC_MASTER = 0x02`, `SOUND_SYNC_SLAVE = 0x04`, `SOUND_QUEUE = 0x08`, `SOUND_STOP = 0x10`), play HUD attachments (`slots 31..38`) non-spatially for the wearer only, and implement single-slot sound queueing (`llSetSoundQueueing` depth 1, overwriting any pending clip on that prim).

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for `secondlife/viewer`, `secondlife/3p-webrtc-build`, `cinderblocks/libremetaverse`, and `Kaleaon/react-linkpoint`.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Second Life Viewer](https://github.com/secondlife/viewer) for normative `indra/newview/llvoicewebrtc.cpp`, `indra/llwebrtc/llwebrtc.cpp`, and `indra/llaudio/` code.

- [WebRTC Voice on SL Wiki](https://wiki.secondlife.com/wiki/WebRTC_Voice) for Linden Lab's architecture overview and Aditi test region notes, verified against current viewer code.

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for `LibreMetaverse.Voice.WebRTC` and `LibreMetaverse.Voice.Vivox` in BSD-3 C#.


## Capability payload shapes in detail

- `ParcelVoiceInfoRequest`: POST an empty LLSD map to fetch `parcel_local_id`, `region_name`, and `voice_credentials` (`channel_uri`, `channel_credentials`, `voice_server_type`), and disconnect spatial `local` voice cleanly if `channel_uri` comes back empty on a voice-disabled parcel.

- `ProvisionVoiceAccountRequest` for spatial voice: send `voice_server_type = "webrtc"`, `channel_type = "local"`, optional integer `parcel_local_id` when parcel-scoped, and `jsep = { type: "offer", sdp }` containing the Opus-munged offer SDP with the `"SLData"` SCTP section included.

- `ProvisionVoiceAccountRequest` for group, conference, and P2P calls: start or join the session via `ChatSessionRequest`, then send `voice_server_type = "webrtc"`, `channel_type = "multiagent"`, `channel`, `credentials`, and `jsep = { type: "offer", sdp }`.

- `VoiceSignalingRequest` trickle ICE: include `viewer_session` and `voice_server_type = "webrtc"`, plus either `candidates` (array of maps with `candidate`, `sdpMid`, `sdpMLineIndex`) or `candidate = { completed: true }`, and never combine `candidates` and `candidate` in one map.

## Reference codebase map in detail

- `secondlife/viewer` (LGPL-2.1): `indra/newview/llvoicewebrtc.cpp` and `.h` implement capability signaling, Opus `fmtp` munging, `"SLData"` position/gain/meter handling, and multi-region session handoff; `indra/llwebrtc/llwebrtc.cpp` wraps `libwebrtc`; `indra/llaudio/llaudioengine_openal.cpp` and `indra/newview/llaudiosourcevo.cpp` implement spatial rolloff, sync master/slave phase alignment, and attached prim sounds.

- `cinderblocks/libremetaverse` (BSD-3): `LibreMetaverse.Voice.WebRTC` (`VoiceManager.cs`, `VoiceSession.cs`, `PeerManager.cs`, `OpusEncoder.cs`) provides a clean BSD-3 implementation of SDP munging, `"SLData"` JSON processing, reprovisioning on ICE failure, and group/P2P call flows; `LibreMetaverse.Voice.Vivox` (`VoiceGateway.cs`) wraps legacy `SLVoice` XML pipes.

- `Kaleaon/react-linkpoint` and `Kaleaon/Linkpoint`: `src/linkpoint/voice-protocol.ts` and `WebRtcVoiceSession.kt` / `SLWebRTCTransportAdapter.kt` implement browser and Android WebRTC signaling, Agni 3-host versus Aditi 2-host STUN selection, and `"SLData"` framing, while `core/sl-sounds.cjs` and `SoundFlags.kt` handle `Unencoded` LLUDP sound triggers, single-slot queueing, and parcel audio streams.

## Spatial and parcel audio pipeline in detail

- Distinguish wire sound flags from LSL constants: on the wire in `AttachedSound.DataBlock.Flags` (`U8`), `0x00` is `SOUND_PLAY`, `0x01` is `SOUND_LOOP`, `0x02` is `SOUND_SYNC_MASTER`, `0x04` is `SOUND_SYNC_SLAVE`, `0x08` is `SOUND_QUEUE`, and `0x10` is `SOUND_STOP`, whereas LSL `llSound()` script constants assign `0x02` to `SOUND_TRIGGER` and `0x04` to `SOUND_SYNC` before simulator translation.

- Track moving prims for `AttachedSound`: resolve child prim positions through `ParentID` each frame, attenuate world sources with inverse-distance rolloff (`DEFAULT_MIN_DISTANCE = 2.0m`, `AudioLevelRolloff`), and hold unlisted `ObjectID`s briefly (`5.0s` timeout) when `AttachedSound` arrives over UDP ahead of `ObjectUpdate`.

- Separate audio gain buses the way viewer `settings.xml` does: `AudioLevelMaster` multiplies `AudioLevelVoice`, `AudioLevelSFX`, `AudioLevelMusic`, `AudioLevelMedia`, and `AudioLevelAmbient` independently so muting parcel music never silences voice or UI cues.

## Debugging playbook

- Symptom WebRTC answer arrives but spatial audio never starts or stays mono: check that `"SLData"` was created before `createOffer()`, `{"j": {"p": true}}` was sent once `"SLData"` opened, and Opus `rtpmap`/`fmtp` stereo 48 kHz munging ran before `setLocalDescription`.

- Symptom `VoiceSignalingRequest` returns HTTP 400/500 during ICE gathering: check whether candidates gathered before `setRemoteDescription(answer)` were sent prematurely without `viewer_session`, or whether `candidates` and `candidate: { completed: true }` were accidentally merged into one LLSD payload.

- Symptom `SoundTrigger` or `AttachedSound` decodes garbage UUIDs or NaN gains: check that your UDP packet parser did **not** run `ZeroDecode` on `High 29` or `Medium 13..15` (`Unencoded`), and read `LLUUID` big-endian versus `U64`/`LLVector3`/`F32` little-endian.

- Symptom parcel music works on OpenSim but stays silent on Agni: read `ParcelProperties` from `EventQueueGet` LLSD (`UDPDeprecated` on Agni) rather than waiting for UDP `High 23` alone.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/webrtc-and-audio-reference.md` (29,037 bytes)
