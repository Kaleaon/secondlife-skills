---
name: secondlife_client_libraries
description: "Build thin, mobile, bot, and text clients with LibreMetaverse, Lumiya-Redux, Radegast, and node-metaverse, and port protocol code to TypeScript and Kotlin."
---

# Second Life Client Libraries

## Start with LibreMetaverse

- Use cinderblocks/libremetaverse as the default client library for new work: C#, BSD-3, .NET 8 to 10 with netstandard2.1 and net481 targets, NuGet LibreMetaverse 3.x.

- Pick only the 3.x packages you need: LibreMetaverse for the client and managers, .Protocol for packets and caps and login, .Transport for the UDP circuit, .StructuredData for LLSD, .Assets and .Types for inventory and primitives, .ModelFormats for Collada and glTF and OBJ, .Rendering.MeshFoundry for prim and mesh geometry and PBR, .Voice.WebRTC and .Voice.Vivox, .RLV, .LslTools, and .Archiving for OAR.

- Build with dotnet build -c Release so the source generators run first, and read MIGRATION.md before porting 2.x code because the 3.x split has breaking changes and old OpenMetaverse namespaces are obsolete.

- Run its examples as oracles before debugging your own port: TestClient, SimpleBot, InventoryExplorer, and PrimInspector under Programs/examples give you a packet capturable reference client.

- Do not start new work in openmetaversefoundation/libopenmetaverse, because it is the superseded predecessor still documenting .NET Framework 3.5 era tooling and it predates AIS3, PBR, and WebRTC voice.

## Use the mobile and text references for what they are

- Use Kaleaon/Lumiya-Redux as the Android Java reference: Apache-2.0 recovery of Lumiya 3.4.2 with 1302 Java classes, 477 UDP message classes, a GLES renderer, OkHttp caps, XML-RPC login, and Vivox in a separate plugin APK, built with Gradle on JDK 17 and SDK 34.

- Treat Lumiya-Redux as a recovery not a rewrite: expect decompiler artefacts, an old OpenJPEG 1.5 native library, and gaps its own analysis lists such as no shadows, no PBR, and no point lights, and reverify any grid claim in its docs against current viewer code.

- Use radegastdev/radegast as the worked example of a full non 3D client for chat, IM, inventory, map, dialogs, and accessibility UX, and note it pins an old libopenmetaverse submodule not LibreMetaverse 3.x and bundles FMOD under a non commercial licence.

- Treat SpeedLight as a closed web product reference only and AjaxLife and pyogp as dead historical architecture studies, because pyogp is Python 2 OGP era code whose login flow is not production login.

## Port to TypeScript and Kotlin honestly

- Use CasperTech/node-metaverse in TypeScript as a porting aid only: npm @caspertech/node-metaverse 0.7.x with @caspertech/llsd, pre 1.0 coverage, and React Native polyfills needed for UDP sockets and crypto.

- Budget for a real port in Kotlin, because no maintained Kotlin or Java full client library exists outside Lumiya Java code, so generate message and LLSD code from the template and YAML and keep it generated.

- Keep the semantic oracle in C# even when the shipping client is TypeScript or Kotlin: when behaviour differs, LibreMetaverse plus viewer code wins over the port.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for LibreMetaverse, Lumiya-Redux, Radegast, and node-metaverse repos.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for the library, package split, and examples.

- [Lumiya-Redux](https://github.com/Kaleaon/Lumiya-Redux) for the Android Java recovery and its gap analysis docs.

- [Radegast](https://github.com/radegastdev/radegast) for a text and accessibility client on libopenmetaverse lineage.


## LibreMetaverse package map in detail

- LibreMetaverse core: GridClient aggregating managers for login, network, inventory, appearance, friends, groups, parcels, self movement and chat, plus Settings for grid selection including custom OpenSim login URIs.

- LibreMetaverse.Protocol: every UDP packet class generated from the message template, caps clients, login request and response types, and the source generator project that must run before the main build.

- LibreMetaverse.Transport: UDP circuit, reliable delivery queue, resend timers, throttle buckets, packet acks, ping, and circuit timeout handling independent of any UI.

- LibreMetaverse.StructuredData: LLSD and OSD types with XML, binary, notation, JSON, and protobuf serialisers, the reference semantics for any port.

- LibreMetaverse.Types: UUID, Vector3, Vector3d, Quaternion, Color4, and bit packing helpers matching viewer maths conventions including quaternion compression.

- LibreMetaverse.Assets: Asset base and subclasses for textures, meshes, animations, sounds, wearables, and inventory item and folder model plus upload permission checks.

- LibreMetaverse.ModelFormats: Collada, glTF, and OBJ loading and mesh export, useful headless for asset inspection and conversion tools.

- LibreMetaverse.Rendering.MeshFoundry plus PrimMesher: turns prim parameters, sculpt maps, and LLMesh data into triangle geometry with rigging and PBR material handling for renderers including Unity and Godot style pipelines.

- LibreMetaverse.Imaging: JPEG2000 via CSJ2K lineage and TGA and other image helpers for texture decoding outside a viewer.

- LibreMetaverse.Voice.WebRTC and LibreMetaverse.Voice.Vivox: two separate voice stacks, negotiate which to initialise from region features, never both blindly.

- LibreMetaverse.RLV, LibreMetaverse.LslTools, LibreMetaverse.Archiving: RLV command handling, LSL lexer and parser for tooling, and OAR archive reading for OpenSim content.

## Porting playbook to TypeScript

- Start from node-metaverse for login, caps, and UDP scaffolding, then port missing messages from LibreMetaverse.Protocol generated classes one message at a time with template diffing.

- Replace Node UDP sockets and crypto with React Native or Capacitor plugins in React-Linkpoint style apps and test on a real device network, because emulators mask UDP behaviour.

- Port LLSD first and fuzz it against LibreMetaverse.StructuredData test cases for binary, dates, UUIDs, and large integers before porting any message that carries LLSD.

- Keep a golden packet test set: capture TestClient login, region handshake, and inventory fetch on OpenSim and replay the same expectations against the TypeScript client.

## Porting playbook to Kotlin and Java

- Start from Lumiya-Redux Java classes for Android lifecycle, GLES rendering, and OkHttp caps, and generate new Kotlin message classes from message_template.msg rather than hand translating 477 Java classes.

- Keep the Java LLSD and circuit code as the reference while Kotlin code is introduced module by module: auth with MFA, caps, inventory AIS3, then rendering, following the Lumiya repair roadmap pattern.

- Watch Android specifics: network on main thread bans, UDP socket lifecycle across activity pause, Doze and background Event Queue polling limits, and target SDK changes for storage and notifications.

## Radegast and text client patterns in detail

- Copy Radegast patterns for accessible chat: speech friendly IM and group chat tabs, LSL dialog button handling, inventory offer handling, map and radar lists, and plugin loading, all without a 3D view.

- Note its limits before reusing code: old libopenmetaverse APIs with OpenMetaverse namespaces, WinForms UI assumptions, and the FMOD licence rider.

## Bot and automation patterns

- Build bots on GridClient events rather than polling: OnChat, OnInstantMessage, OnObjectUpdate, friends and group events, and inventory offer events, with explicit reconnect and relogin backoff.

- Respect grid rules and TPV policy for bots: use a dedicated account, honour parcel bot restrictions and Linden Lab bot policy on Agni, and throttle object and chat actions.

- For OpenSim bots, the same LibreMetaverse client works against a local standalone login URI, which is the safest load and behaviour test bed.
