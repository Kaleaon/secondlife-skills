---
name: secondlife_protocol
description: "Implement and debug Second Life login, UDP circuits, capabilities, Event Queue, and LLSD in any language using the message template and viewer code as truth."
---

# Second Life Protocol and LLSD

## Start from the two planes

- Model every session as two planes at once: a UDP simulator circuit for realtime messages and HTTPS capabilities for inventory, assets, and most modern features.

- Start login with the login service, take the seed capability and circuit code from the LLSD login response, POST the cap names you want to the seed cap, and only then send UseCircuitCode and CompleteAgentMovement over UDP.

- Start the EventQueueGet long poll right after login and keep it running, because a stalled event queue looks like a dead session and it carries teleports, inventory offers, group notices, and lures.

## Build UDP correctly

- Parse the 6 byte packet header, flags, sequence, and extra header length before touching the body, and dispatch by message frequency: High is 1 byte, Medium is 2 bytes, Low is 4 bytes starting 0xFFFF, Fixed is 4 bytes.

- Honour the flags: 0x80 Zerocoded, 0x40 Reliable, 0x20 Resent, and 0x10 Ack with appended acknowledgements.

- Implement ZeroDecode and ZeroEncode only for messages and blocks the template marks zerocoded, and verify each flag against the viewer template copy because the master template has been wrong before, for example for ChatFromViewer.

- Implement reliability as resend until ACK with piggybacked or standalone PacketAck, plus StartPingCheck and CompletePingCheck, AgentThrottle token buckets, and clean LogoutRequest and CloseCircuit, or a mobile client on a lossy link will ghost.

- Treat object updates as latest wins: handle ObjectUpdate, ImprovedTerseObjectUpdate with its compressed position and rotation quantisation, ObjectUpdateCompressed, ObjectUpdateCached, and KillObject, and expect terse quantisation to be the first suspect for avatar jitter.

## Use capabilities correctly

- Request caps per region and per session and never cache a cap URL across a teleport or a new login, because cap URLs are unguessable, per region, and expire on region change.

- Check availability before use and fall back to UDP where the viewer does, because cap availability varies by grid and simulator version and OpenSim implements only a subset.

- Prioritise the caps a thin client needs first: EventQueueGet, FetchInventory2 and FetchLib2, InventoryAPIv3 and LibraryAPIv3 for AIS3, GetTexture, GetMesh and GetMesh2, SimulatorFeatures, ExtEnvironment and EnvironmentSettings, GetDisplayNames, ChatSessionRequest, and the voice caps.

- Query SimulatorFeatures instead of hardcoding limits, because it tells you mesh upload rules, physics shape types, PBR support, and voice type for that region.

- Use LLSD content type application/llsd+xml for caps unless an endpoint is documented as binary LLSD in viewer code.

## Implement LLSD faithfully

- Support all LLSD types: undefined, boolean, 32 bit integer, real as double, string, binary, UUID, date, URI, array, and map, in XML, binary, and notation serialisations.

- Watch the classic interop bugs in TypeScript and Kotlin ports: JavaScript number precision for 64 bit values, binary as base64 in XML, date formatting, and UUID string casing.

- Cross-check a new LLSD codec against LibreMetaverse.StructuredData, viewer llsdserialize.cpp test behaviour, and secondlife/python-llsd before trusting it, and use @caspertech/llsd in TypeScript rather than the pre npm Bitbucket code.

- Generate message classes from message_template.msg with a generator and regenerate on template changes, following the pattern of LibreMetaverse.Protocol source generation and Lumiya and its 477 Java message classes.

## Debug voice and teleport as protocol

- Branch voice on what the region offers: WebRTC is the primary provider since viewer 7.1.9 in 2024, Vivox is legacy via a separate SLVoice daemon and ProvisionVoiceAccountRequest, and there is no peer to peer bridging between WebRTC only and Vivox only viewers.

- Trace teleport as a sequence across both planes: TeleportStart, TeleportProgress, TeleportFinish or TeleportFailed over UDP plus cap handoff to the destination region, and rebuild the cap map and circuit on arrival.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for secondlife/viewer, secondlife/master-message-template, and LibreMetaverse protocol code.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Master message template](https://github.com/secondlife/master-message-template) for message_template.msg, always diffed against the viewer copy.

- [Current Sim Capabilities](https://wiki.secondlife.com/wiki/Current_Sim_Capabilities) for the human readable cap list.

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for LibreMetaverse.Protocol, Transport, and StructuredData as a runnable oracle.


## Login flow step by step

- Step 1: build the login request for https://login.agni.lindenlab.com/cgi-bin/login.cgi on Agni or the Aditi equivalent, with first and last name or username, password hash historically $1$ plus MD5 with newer MFA and token variants in current viewer code, start location, channel, version, and host identifiers such as MAC and id0 as current llstartup code requires.

- Step 2: parse the LLSD login response map for agent_id, session_id, secure_session_id, sim_ip, sim_port, circuit_code, seed_capability, inventory skeleton, buddy list, and login-flags, and branch on reason fields for MFA challenges instead of treating them as generic failure, following the Lumiya MFA fix pattern where SLAuthReply parses reason and mfa_hash and resubmits with a token.

- Step 3: POST an LLSD array of wanted cap names to seed_capability and store the returned map of name to unguessable https sim host cap UUID URL for this region and session only.

- Step 4: open the UDP socket to sim_ip and sim_port, send UseCircuitCode with the circuit code, agent id, and session id, then CompleteAgentMovement, then start AgentUpdate, ping, throttle, and EventQueueGet loops.

- Step 5: handle RegionHandshake by replying RegionHandshakeReply and recording sim product name, region flags, water height, and terrain detail before expecting object updates.

## Packet format reference

- Header layout: flags byte, sequence as U32, extra header length byte, then optional extra header, then message body, then optional appended ACKs as count plus U32 sequence list.

- Flags in detail: 0x80 Zerocoded means header and specified body portions are zero encoded, 0x40 Reliable means resend until acknowledged, 0x20 Resent marks a resend, 0x10 Ack means an appended ACK list follows the body.

- Message ID encoding by frequency: High frequency IDs are 1 byte from 0x01 to 0xFE range in template order, Medium are 2 bytes starting 0xFF, Low are 4 bytes starting 0xFFFF, Fixed are 4 bytes starting 0xFFFFFFxx for protocol level messages such as PacketAck and StartPingCheck.

- Field types in the template: U8, U16, U32, U64, S8, S16, S32, S64, F32, F64, LLUUID as 16 bytes, LLVector3 as 3 times F32, LLVector3d as 3 times F64, LLVector4, LLQuaternion sent as 3 times F32 with the scalar reconstructed, BOOL as U8, Variable 1 and Variable 2 as length prefixed blobs with 1 or 2 byte lengths, and Fixed as fixed length byte arrays.

- Zero coding in detail: encoding replaces each 0x00 byte with 0x00 followed by a count of consecutive zero bytes, decoding expands it, and it applies only where the template and viewer llmessage code say it applies, never blanket decode a whole packet.

## Reliability, throttle, and session health in detail

- Keep an unacked queue for reliable messages with resend timers and exponential handling per circuit code in viewer llcircuit and LibreMetaverse.Transport, and drop and log after the circuit timeout instead of resending forever.

- Send PacketAck promptly for reliable incoming messages, either piggybacked via the Ack flag or as standalone Fixed messages, because delayed ACKs cause simulator resends and duplicate object updates.

- Implement AgentThrottle as token buckets per category named in viewer and LibreMetaverse code: resend, land, wind, cloud, task, texture, and asset, and raise texture and asset buckets only within simulator limits on mobile links.

- Run StartPingCheck and CompletePingCheck to measure round trip and detect a dead circuit, track last packet time, and implement a clean logout with LogoutRequest followed by CloseCircuit so the avatar does not ghost in region.

## Message catalogue most clients need first

- Session: UseCircuitCode, CompleteAgentMovement, AgentUpdate with control flags and camera fields sent continuously, AgentDataUpdate, LogoutRequest, CloseCircuit, PacketAck, StartPingCheck, CompletePingCheck.

- World: ObjectUpdate full, ImprovedTerseObjectUpdate, ObjectUpdateCompressed, ObjectUpdateCached, KillObject, ObjectProperties and ObjectPropertiesFamily replies, RequestObjectPropertiesFamily, LayerData for terrain wind and cloud patches, CoarseLocationUpdate with 16 metre quantised minimap positions.

- Movement and teleport: TeleportRequest via caps and UDP mix, TeleportStart, TeleportProgress, TeleportFinish, TeleportLocal, TeleportFailed, CrossRegionHandshake on the receiving side, EnableSimulator and DisableSimulator for neighbour regions, ChildAgentUpdate for child agents in neighbours.

- Communication: ChatFromViewer, ChatFromSimulator, ImprovedInstantMessage for IM, group, and offline messages, ScriptDialog, ScriptQuestion, ChatterBox events arriving via Event Queue.

- Animation and appearance: AvatarAnimation, ObjectAnimation, AgentAnimation requests, UpdateAgentAppearance and AgentSetAppearance legacy paths plus modern appearance caps.

## Capabilities catalogue in detail

- EventQueueGet and EventQueueGet2: long poll POST with an LLSD map holding ack as the last event id and done flag, response is an LLSD map with id and events array, each event has message name and body map, and you must ack correctly or events repeat or stop.

- Inventory HTTP: FetchInventory2, FetchInventoryDescendents2, FetchLib2, FetchLibDescendents2 return LLSD inventory skeletons and items and replace most UDP fetch for browsing.

- AIS3: InventoryAPIv3 and LibraryAPIv3 perform create, update, remove, link, and copy operations as LLSD calls against agent and library roots, with Current Outfit Folder versioning via IncrementCOFVersion, and viewer llaisapi.cpp is the authority for request shapes including link creation payloads.

- Content delivery: GetTexture takes an LLSD or header driven request for texture UUID with range based discard level delivery, GetMesh and GetMesh2 fetch LLMesh by UUID, GetMetadata, GetObjectCost, and GetObjectPhysicsData expose mesh accounting.

- Region and agent info: SimulatorFeatures returns an LLSD feature map, ServerReleaseNotes, ProductInfoRequest, HomeLocation, LandResources, RemoteParcelRequest, MapLayer legacy, SearchStatRequest, SimConsole restricted, ViewerStats, and AgentPreferences, AgentState, AvatarRenderInfo, CharacterProperties, GetDisplayNames for names and rendering info.

- Social: ChatSessionRequest creates group and conference chat sessions, GroupAPIv1 and GroupMemberData serve group data, friendship accept and decline caps replace some UDP friendship messages, StartGroupProposal starts group voting.

- Upload and update: NewFileAgentInventory, InventoryThumbnailUpload, UpdateGestureAgentInventory and related Update caps, UpdateAgentInformation and UpdateAgentAppearance, RenderMaterials, EnvironmentSettings and ExtEnvironment for EEP.

- Voice: ProvisionVoiceAccountRequest is the legacy Vivox provisioning cap, VoiceSignalingRequest and WebRTC signaling caps serve current voice, always branch on SimulatorFeatures voice settings.

## LLSD serialisation reference

- XML LLSD example shape: an llsd root element with map, key, string, uuid, binary as base64, date, uri, integer, real, boolean, array, and undef elements, content type application/llsd+xml.

- Binary LLSD: single byte type markers prefix each value with big endian integers and length prefixed strings, used where viewer code specifies binary for compactness.

- Notation LLSD: human readable prefix letters such as i for integer, r for real, s for string, u for UUID, and quoted maps and arrays, mostly a debugging and legacy format today.

- JSON and protobuf: LibreMetaverse.StructuredData adds JSON and protobuf mappings for tooling convenience, these are not simulator wire formats unless an endpoint in viewer code says so.

## Debugging playbook

- Symptom no objects after login: check CompleteAgentMovement was sent, RegionHandshakeReply was sent, EventQueueGet is polling, and EnableSimulator handling exists, in that order.

- Symptom duplicate or flickering objects: check PacketAck timing and reliable resend handling and whether ObjectUpdateCached is being treated as a new object instead of a cache hit.

- Symptom inventory empty but login ok: check FetchInventory2 cap was granted, the inventory skeleton from login was parsed, and AIS3 root folder ids match the login skeleton.

- Symptom works on OpenSim fails on Agni: check cap availability differences, template zerocoded flags, and SimulatorFeatures gating, because OpenSim grants caps and flags more loosely.

- Capture a working oracle first: run LibreMetaverse TestClient against the same grid and region and compare its packet and cap sequence to yours message by message.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/capabilities.md` (23,528 bytes)
- `references/code-go.md` (120,412 bytes)
- `references/code-python.md` (91,137 bytes)
- `references/code-rust.md` (147,396 bytes)
- `references/message-stubs-csharp.md` (62,371 bytes)
- `references/message-stubs-kotlin.md` (53,685 bytes)
- `references/message-stubs-rust.md` (53,198 bytes)
- `references/message-stubs-typescript.md` (55,142 bytes)
- `references/udp-messages.md` (199,591 bytes)
