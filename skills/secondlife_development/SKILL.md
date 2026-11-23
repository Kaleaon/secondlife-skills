---
name: secondlife_development
description: "Route and coordinate any Second Life coding task across protocol, viewer, client libraries, LSL, OpenSim, assets, WebRTC voice, RLVa, and Linkpoint design using the canonical cross-check stack."
---

# Second Life Development

## Route the task first

- Classify the bug or feature before editing code: protocol or LLSD, viewer C++, client library, LSL or SLua, OpenSim server, assets and rendering, WebRTC voice and spatial audio, RLV or RLVa viewer behaviour, or Linkpoint UI design and Ktheme palettes.

- Load the matching specialist skill for the domain and keep this skill as the router when a task spans two or more domains.

- Treat Joe's active stacks as first-class targets: React-Linkpoint in TypeScript and React, Linkpoint-stitch and Linkpoint in Kotlin and Jetpack Compose, Linkpoint Design (`@linkpoint/design-system`), Lumiya-Redux in Java for Android, and LibreMetaverse in C#.

## Apply the cross-check stack in order

- Check packet or message definitions in secondlife/master-message-template diffed against the template shipped in secondlife/viewer under indra/llmessage.

- Check capability names and payloads in secondlife/viewer indra/newview/llviewerregion.cpp buildCapabilityNames and llaisapi.cpp, then the wiki Current Sim Capabilities page.

- Check LLSD semantics in LibreMetaverse.StructuredData and viewer indra/llcommon/llsdserialize.cpp, then secondlife/python-llsd.

- Check login, teleport, and session flow in LibreMetaverse and its TestClient first, then viewer llstartup code, then Lumiya-Redux login code.

- Check inventory, AIS3, and Current Outfit Folder behaviour in viewer llaisapi.cpp and llinventory code before trusting OpenSim, because OpenSim diverges from Agni.

- Check mesh, texture, PBR, EEP, and Bakes on Mesh rendering in viewer code first, Firestorm second, and LibreMetaverse MeshFoundry for geometry parsing in isolation.

- Check WebRTC voice signaling, Opus SDP munging, `"SLData"` spatial updates, parcel media streams, and LLUDP sound triggers in secondlife/viewer `llvoicewebrtc.cpp`, `llwebrtc.cpp`, and `llaudioengine_openal.cpp` first, `LibreMetaverse.Voice.WebRTC` second, and `Kaleaon/react-linkpoint` `voice-protocol.ts` and `sl-sounds.cjs` third.

- Check RLV and RLVa `llOwnerSay` command parsing, per-object restriction maps, and positive-channel handshakes in `FirestormViewer/phoenix-firestorm` release branches (`indra/newview/rlva/`) first, `LibreMetaverse.RLV` second, and `Kaleaon/react-linkpoint` `rlv*.ts` third.

- Check Linkpoint layout packs, CleverFerret LCARS split-frame geometry, 24+ Ktheme palettes, WCAG relative-luminance contrast adjustment, and Pass-2 HUD slots in `Kaleaon/linkpoint-design` (`@linkpoint/design-system`) across `Kaleaon/react-linkpoint`, `Kaleaon/Linkpoint`, and `Kaleaon/Linkpoint-stitch`.

## Respect the source hierarchy

- Put secondlife/viewer first as normative truth for what Agni actually accepts, even when a wiki or an older library disagrees.

- Put LibreMetaverse second as the reusable implementation to port semantics from, because it is BSD-3 and actively maintained for .NET 8 to 10.

- Put OpenSimulator third as a local test server you can run and breakpoint, not as proof of Agni behaviour.

- Treat wiki.secondlife.com as a human readable starting point only and check its revision date, because many pages are 5 to 15 years stale.

- Never cite github.com/secondlife/llsd, because that repo returned 404 in November 2026, and never invent a GitHub repo for Catznip, Kokua, Black Dragon, or the Marine Kelley Restrained Love viewer, because none was verified — cite the official Third Party Viewer Directory instead.

## Test on the right grid

- Test protocol changes against a local OpenSim standalone first, then Aditi the beta grid, then Agni production.

- Remember Aditi inventory and passwords can diverge from Agni, so a login failure on Aditi alone is not proof the code is broken.

- Keep generated code generated: derive message classes, LLSD helpers, and LSL tables from message_template.msg and lsl-definitions YAML and never hand edit the generated output.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for searching and working with viewer, LibreMetaverse, OpenSim, and Lumiya repos.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Second Life Viewer](https://github.com/secondlife/viewer) for the normative C++ viewer and protocol implementation.

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for the BSD C# client library and runnable examples.

- [SL Wiki](https://wiki.secondlife.com) for LSL Portal, capabilities, and protocol overviews, with revision dates checked.


## Detailed repo catalogue

- Official Linden Lab, verified November 2026: secondlife/viewer at https://github.com/secondlife/viewer, C++, LGPL-2.1, branch develop, Autobuild wrapping CMake, layout indra/ plus autobuild.xml, normative for all protocol and rendering behaviour.

- secondlife/autobuild at https://github.com/secondlife/autobuild, Python, MIT, the tool that fetches 3p-* prebuilt packages and drives viewer builds, not GNU Autoconf.

- secondlife org at https://github.com/orgs/secondlife/repositories, about 110 repos including slua, lsl-definitions, python-llsd, python-llbase, tailslide, sl-vscode-plugin, dullahan for CEF, and 3p-* packages including 3p-webrtc-build.

- secondlife/master-message-template at https://github.com/secondlife/master-message-template, the data repo holding message_template.msg, historically stale for years per a Linden Lab feedback ticket and re-synced after, so always diff it.

- FirestormViewer/phoenix-firestorm at https://github.com/FirestormViewer/phoenix-firestorm, C++, LGPL-2.1, Autobuild, master is nightly and release branches are named like Firestorm_7.1.13, most used third party viewer and canonical open tree for RLVa (`indra/newview/rlva/`).

- AlchemyViewer/Alchemy at https://github.com/AlchemyViewer/Alchemy, C++, LGPL-2.1, CMake plus vcpkg with indra/vcpkg.json, branch develop, the modern build exemplar.

- singularity-viewer/SingularityViewer at https://github.com/singularity-viewer/SingularityViewer, C++, Autobuild, Snowglobe 1.5 lineage, V1 UI with backported protocol.

- cinderblocks/libremetaverse at https://github.com/cinderblocks/libremetaverse, C#, BSD-3, .NET 8 to 10, NuGet LibreMetaverse 3.2.1 verified, the reusable client library and semantic oracle for ports including `LibreMetaverse.Voice.WebRTC`, `LibreMetaverse.Voice.Vivox`, and `LibreMetaverse.RLV`.

- openmetaversefoundation/libopenmetaverse, the superseded predecessor, C# with Prebuild and .NET Framework 3.5 era docs, historical reference only.

- radegastdev/radegast at https://github.com/radegastdev/radegast, C#, BSD style, full text client pinning old libopenmetaverse as a submodule, slowly maintained with org activity in 2024.

- Kaleaon/Lumiya-Redux at https://github.com/Kaleaon/Lumiya-Redux, Java, Apache-2.0, Gradle JDK 17 SDK 34, recovery of Lumiya 3.4.2 with 1302 classes and 477 UDP message classes.

- Kaleaon/react-linkpoint and Kaleaon/Linkpoint at https://github.com/Kaleaon/Linkpoint, TypeScript/React and Kotlin/Android viewers sharing `@linkpoint/design-system`, WebRTC voice (`src/linkpoint/voice-protocol.ts`, `WebRtcVoiceSession.kt`), LLUDP audio (`core/sl-sounds.cjs`, `SoundFlags.kt`), and RLVa (`src/linkpoint/rlv*.ts`, `RLVController.kt`).

- Kaleaon/Linkpoint-stitch at https://github.com/Kaleaon/Linkpoint-stitch and Kaleaon/linkpoint-design (`packages/design-system`), Jetpack Compose and TypeScript Linkpoint UI architecture defining the 6 layout packs (including CleverFerret Sweep Console LCARS), 24+ Ktheme JSON palettes, WCAG contrast correction, and Pass-2 HUD composition (`slots 31..38`).

- CasperTech/node-metaverse at https://github.com/CasperTech/node-metaverse, TypeScript, MIT, npm @caspertech/node-metaverse 0.7.28 with @caspertech/llsd, the only credible TypeScript client library found.

- opensim/opensim at https://github.com/opensim/opensim is a mirror only, canonical git is at opensimulator.org, C#, BSD, .NET 8, Prebuild, with ROBUST services and region modules.

- secondlife/lsl-definitions at https://github.com/secondlife/lsl-definitions, YAML, MIT, files lsl_definitions.yaml and slua_definitions.yaml, canonical LSL and SLua signatures.

- Sei-Lisa/LSL-PyOptimizer at https://github.com/Sei-Lisa/LSL-PyOptimizer, Python 2, GPL-3, SL Mono only optimiser, and Makopo/lslint at https://github.com/Makopo/lslint, public domain, about 2006 compiler quirks.

## Decision tree in detail

- If the symptom is login fails, session dies, teleport hangs, chat or IM missing, inventory will not fetch, or objects never appear, start in secondlife_protocol.

- If the symptom is in C++ viewer code, a build failure, a rendering pipeline change, or a Firestorm or Alchemy cherry pick, start in secondlife_viewer_cpp.

- If you are writing a bot, a companion app, a mobile client, or porting code to TypeScript or Kotlin, start in secondlife_client_libraries.

- If the content is a script inside an object, an ll function call, a permission error, a timer, a sensor, or an OSSL failure, start in secondlife_lsl_scripting.

- If you control the server, the region will not start, ROBUST will not connect, physics collides wrong, or a region module misbehaves, start in secondlife_opensim_server.

- If the symptom is grey textures, invisible mesh, wrong PBR shine, bake failures, animesh frozen, or sky and water wrong, start in secondlife_assets_mesh_texture.

- If the symptom is WebRTC voice failing to connect, `VoiceSignalingRequest` rejecting ICE candidates, spatial voice staying mono or silent, parcel music failing on Agni, or `SoundTrigger` and `AttachedSound` packets corrupting audio, start in secondlife_voice_webrtc.

- If the task involves `@cmd[:option]=param` owner-say restrictions, RLV relays, attachment locks, `@version` or `@getstatus` channel replies, or camera, chat, inventory, and teleport gating, start in secondlife_rlva.

- If the task builds or themes Linkpoint UI floaters, HUD docks, Ktheme selectors, CleverFerret LCARS split-frame chrome, WCAG contrast correction, or mobile thumb-zone cockpits across React or Jetpack Compose, start in secondlife_linkpoint_design.

## Worked cross-check examples

- Example, inventory link creation fails in React-Linkpoint: first confirm the AIS3 operation shape in viewer llaisapi.cpp, then confirm the cap name in llviewerregion.cpp buildCapabilityNames, then compare the LLSD body against LibreMetaverse inventory code, then test against local OpenSim knowing its AIS support diverges, then test on Aditi.

- Example, avatar jitters in Lumiya: first check ImprovedTerseObjectUpdate quantisation in the message template and LibreMetaverse.Transport decoding, then viewer terse update handling, then Lumiya Java message class for that packet, in that order, before touching the renderer.

- Example, a script works in OpenSim and fails on Agni: first check for os, mod, or wl functions, then check OSSL threat level assumptions, then check llJson and sensor and timer differences in the LSL skill, then retest on Aditi.

## Licensing map to check before copying code

- Viewer and all viewer forks are LGPL-2.1, so copied code carries LGPL obligations and TPV Policy duties.

- LibreMetaverse and OpenSim are BSD, the most permissive reuse path, and Radegast is BSD style with an FMOD non commercial rider to remove for commercial use.

- Lumiya-Redux recovery is Apache-2.0, node-metaverse and Linden Lab tools such as autobuild, python-llsd, lsl-definitions, and tailslide are MIT, and LSL-PyOptimizer is GPL-3 and must not be mixed into LGPL or permissive client code without review.

- Kakadu, Havok, and Vivox SLVoice are proprietary and closed, so never plan to ship them from open sources, use OpenJPEG, BulletSim or ubODE, and WebRTC respectively.

## Verification checklist before calling a fix done

- Name the exact source file in the exact repo that proves the protocol, cap, or API shape you implemented.

- Show a test against at least one runnable oracle: LibreMetaverse TestClient, a local OpenSim standalone login, or Aditi.

- State which grid the test ran on, Agni, Aditi, OpenSim standalone, or OpenSim grid mode, because results do not transfer silently between them.

- State the licence of any code copied or ported and where it landed in the target tree.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/master-index.md` (5,803 bytes)
