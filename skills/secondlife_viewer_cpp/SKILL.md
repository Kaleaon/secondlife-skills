---
name: secondlife_viewer_cpp
description: "Work in the official Second Life viewer and third-party viewer C++ codebases, with Autobuild and CMake builds, indra layout, and TPV policy."
---

# Second Life Viewer C++

## Know the one codebase rule

- Treat all graphical viewers as forks of one C++ codebase: Linden Lab secondlife/viewer under LGPL-2.1, with Firestorm, Alchemy, and Singularity as the verifiable GitHub forks.

- Read code in indra/ by area: indra/newview for viewer logic and rendering, indra/llmessage for UDP and the message template, indra/llcommon for LLSD and common types, indra/llcorehttp for HTTP, and indra/llwebrtc for current voice.

- Go to the exact files other clients sync against: llviewerregion.cpp for buildCapabilityNames, llaisapi.cpp for AIS3 caps, llmeshrepository.cpp for mesh fetch, and the texture cache and llvoavatar files for avatar rendering.

## Build the way that viewer builds

- Build the official viewer and Firestorm and Singularity with Autobuild wrapping CMake, driven by autobuild.xml and the matching secondlife/3p-* prebuilt packages.

- Build Alchemy with CMake and vcpkg presets instead, for example cmake -S indra --preset with indra/vcpkg.json, and do not apply Autobuild recipes to it.

- Never transfer build instructions across viewers, because toolchain, 3p versions, and viewer-build-variables differ per fork, and follow that viewer's own wiki for Visual Studio, Xcode, or GCC versions.

- Reuse Firestorm code only from release branches for a distributed viewer, per its own README warning, and expect a cherry picked file from Firestorm rarely to compile cleanly against upstream because the diff is huge.

## Choose the right fork to cross-check

- Use Firestorm second for worked examples beyond Linden Lab: RLVa, the LSL preprocessor, area search, inventory features, OpenSim support, and PBR.

- Use Alchemy for the cleanest modern build system and bleeding edge Linden Lab features and performance work.

- Use Singularity only for V1 style UI ideas and lightweight rendering, because its architecture predates the PBR era pipeline.

- Do not invent source URLs for Catznip, Kokua, Cool VL, or Black Dragon: check the Third Party Viewer Directory source link at time of use, because Catznip and Kokua trace to Mercurial and GitLab or Bitbucket, Cool VL ships tarballs from sldev.free.fr, and Black Dragon traces to Bitbucket and Alchemy GitLab.

## Stay TPV compliant

- Check the Third Party Viewer Policy and Directory before distributing any viewer: self certify, use a unique viewer identifier and channel, never log or share user credentials, respect creator permissions and export controls, and publish a privacy policy and crash reporting.

- Remember listing is self certification only and Linden Lab does not endorse listed viewers, and an unlisted distributed viewer risks being blocked from Agni.

- Keep LGPL-2.1 obligations when copying viewer code and keep proprietary pieces out: Kakadu for JPEG2000, Havok for physics, and Vivox are closed, so open builds substitute OpenJPEG, and WebRTC replaces Vivox as primary voice.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for secondlife/viewer, FirestormViewer/phoenix-firestorm, and AlchemyViewer/Alchemy.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Official viewer](https://github.com/secondlife/viewer) for normative code on the develop branch.

- [Firestorm](https://github.com/FirestormViewer/phoenix-firestorm) for the most used third-party viewer.

- [Alchemy](https://github.com/AlchemyViewer/Alchemy) for the CMake and vcpkg viewer build.

- [Third Party Viewer Directory](https://wiki.secondlife.com/wiki/Third_Party_Viewer_Directory) for the current active viewer list and source links.


## indra directory map in detail

- indra/llcommon: LLSD in llsd.h and llsdserialize.cpp, LLUUID, maths types, threading, logging, and timing used by every other library.

- indra/llmessage: llcircuit, llpacketring, llmessagetemplate and message_template.msg, lltransfermanager, and the UDP reliability and zerocoding implementation that defines the wire protocol.

- indra/llcorehttp: the HTTP client stack used for caps, textures, and mesh, with coroutine style operations in newer code.

- indra/newview: the viewer application, including llviewerregion.cpp and its capability name builder, llaisapi.cpp for AIS3, llstartup.cpp for login state machine, llvoavatar.cpp and related avatar files, llmeshrepository.cpp, lltexturecache and lltexturefetch, llgltfmaterial code, EEP environment code, and the rendering pipeline in llpipeline and shader classes.

- indra/llaudio and indra/llwebrtc and media plugin hosts: audio, WebRTC voice integration, and dullahan CEF web media.

- indra/test and indra/integration_tests: unit and integration tests that show intended LLSD, message, and maths behaviour with test vectors worth porting.

## Build workflow in detail

- Official and Firestorm flow: install the supported compiler for the platform, install Autobuild with pip, run autobuild install to fetch 3p packages from autobuild.xml, run autobuild configure with the viewer-build-variables for your channel, then build with CMake generated projects, following Get source and compile on the wiki for that branch.

- Alchemy flow: clone, initialise vcpkg per its docs, configure with cmake -S indra --preset naming a preset from CMakePresets, then build the preset, with dependencies from indra/vcpkg.json instead of Autobuild packages.

- Expect a full viewer build to need tens of gigabytes, a supported Visual Studio on Windows or Xcode on macOS or a pinned GCC on Linux, and prebuilt proprietary or licensed 3p artefacts for some components, and do not attempt it on a phone or a small VM.

- For code reading and small fixes, use GitHub code search and local sparse checkouts of indra/llmessage, indra/llcommon, and the specific newview files you need instead of cloning the whole monorepo repeatedly.

## Fork differences that matter in code

- Firestorm adds RLVa in its restrained love implementation, a Boost.Wave based LSL preprocessor with includes and extensions, extended inventory and area search UI, OpenSim grid manager support, and many rendering options, spread across newview files that diverge heavily from upstream.

- Alchemy tracks upstream features quickly, modernises build and defaults, and is the best place to see PBR and performance work in a cleaner tree.

- Singularity keeps a V1 derived UI and older pipeline, useful for low end hardware patterns, not for PBR era rendering reference.

- Cool VL by Henri Beauchamp ships source tarballs from sldev.free.fr with notable patches including a patched OpenJPEG 1.5 and HTTP fixes, diff manually against upstream when investigating a texture or HTTP bug.

- Catznip is the origin of RLVa by Kitty Barnett and strong inventory usability, Kokua offers RLV and no RLV variants and an OpenSim variant, Black Dragon is Windows only and photography focused with non standard avatar complexity values you must not copy, check the TPV Directory source link for each at time of use.

## TPV Policy checklist in detail

- Self certify to the TPV Policy, list in the Third Party Viewer Directory via the secondlife/third-party-viewers process, and keep the listing current.

- Use a unique channel name and viewer version identifier in login so Linden Lab can distinguish and if needed block only your viewer.

- Never store, log, or transmit a user password except to the login service, never share credentials between viewers, and disclose any proxy or server side rendering model like SpeedLight uses.

- Respect creator permissions: do not add exporters that defeat object, texture, or animation permissions, and honour the export policy fields on assets.

- Provide a privacy policy, crash reporting disclosure, and update mechanism, and respond to Linden Lab security notices for listed viewers.

## Common viewer bug patterns

- Cap added in server but viewer never requests it: add the name in buildCapabilityNames and the AIS list if it is an inventory cap, in both places, or the cap map will never contain it.

- Texture or mesh stall: trace lltexturefetch and llmeshrepository priority and discard logic before blaming the network, most stalls are priority starvation or cache thrash.

- Avatar bake grey: trace appearance and Bakes on Mesh code paths and COF state before touching materials code.

- Cherry pick from Firestorm fails to compile: expect missing Firestorm only helpers, settings, and UI strings, port the logic not the file.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/alchemy-source-tree.md` (349,869 bytes)
- `references/firestorm-settings.md` (386,264 bytes)
- `references/firestorm-source-tree.md` (817,039 bytes)
- `references/viewer-internals-guide.md` (106,445 bytes)
- `references/viewer-settings.md` (578,093 bytes)
- `references/viewer-source-tree.md` (267,635 bytes)
