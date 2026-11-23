---
name: secondlife_lsl_scripting
description: "Write, lint, optimise, and port LSL scripts and understand SLua, OSSL, and the SL versus OpenSim scripting differences that break scripts."
---

# Second Life LSL and SLua Scripting

## Write LSL as a state machine

- Structure every script as event driven states starting with default and state_entry, with named states and state_entry and state_exit on every transition, and no threads and no main function.

- Use only the LSL types: integer as 32 bit and boolean, float, string, key as UUID, vector as 3 floats, rotation as quaternion 4 floats, and list as a heterogeneous list with no arrays or structs.

- Budget memory first: Mono scripts get 64 KB and legacy LSO gets 16 KB, and string and list operations are the usual cause of stack heap collisions and out of memory failures.

- Expect built in delays and throttles on many ll functions and per parcel and per object limits, and check the LSL Portal page for a function's delay, energy, and caveats before calling it in a loop or timer.

## Get signatures from the canonical source

- Take function, event, and constant signatures from secondlife/lsl-definitions lsl_definitions.yaml and slua_definitions.yaml, because Linden Lab calls that repo the authoritative source of truth for editors.

- Use the LSL Portal on wiki.secondlife.com for human readable per function docs and examples, and verify any wiki signature against the YAML before shipping.

- Handle the roughly 40 events explicitly, including touch, collision, listen, sensor and no_sensor, timer, money, attach, changed, http_request and http_response, dataserver, link_message, run_time_permissions, control, and experience events.

- Request run time permissions before sensitive calls and handle permission denial as a silent failure path, because missing PERMISSION_DEBIT, TELEPORT, ATTACH, TAKE_CONTROLS, or CHANGE_LINKS is the most common LSL bug class.

## Lint and preprocess with the right tools

- Lint with tailslide, the embeddable LSL parser and compiler based on LSLint in the secondlife org, or with lslint itself, and remember lslint faithfully reproduces around 2006 compiler quirks so treat it as a lint tool not a compiler oracle.

- Expand Firestorm preprocessor code before expecting it to compile elsewhere: hash include and hash define plus Firestorm extensions such as switch, lazy list indexing like list[i], and duplicate function definitions do not compile in the stock Linden Lab editor or OpenSim without preprocessing.

- Optimise with Sei-Lisa LSL-PyOptimizer only for SL Mono scripts, because it is GPL-3, Python 2, and explicitly does not support LSO, OpenSim, or Luau, and do not copy its code into a permissive or LGPL client.

- Use the official secondlife/sl-vscode-plugin for LSL and SLua editing with preprocessing and viewer integration, and LibreMetaverse.LslTools when you need an LSL lexer or parser in .NET tooling.

## Port between SL and OpenSim deliberately

- Test every non trivial script on both a local OpenSim and Aditi, because timer resolution, sensor limits, link limits, JSON behaviour in llJson functions, and ll function edge cases differ.

- Gate all OSSL os functions, mod functions, and LightShare wl functions behind a grid check, because they do not exist on Agni and OSSL is also gated in OpenSim by threat levels from None to Severe and by osslEnable.ini allow lists per owner and estate and parcel.

- Know the engine you are on: OpenSim XEngine is legacy with different evaluation order and llSleep stalls, YEngine is current with microthreading and SL like evaluation order, and SL itself runs Mono bytecode server side with neither engine.

- Treat SLua as the growth path alongside LSL: it is Linden Lab's Luau fork in secondlife/slua with serializable scripts, LSL is not going away, and LSLint and PyOptimizer do not cover SLua.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for secondlife/lsl-definitions, tailslide, slua, and the VS Code plugin.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [LSL Portal](https://wiki.secondlife.com/wiki/LSL_Portal) for per function documentation and examples.

- [lsl-definitions](https://github.com/secondlife/lsl-definitions) for canonical LSL and SLua YAML signatures.

- [LSL-PyOptimizer](https://github.com/Sei-Lisa/LSL-PyOptimizer) for Mono memory optimisation, with its licence and flavour limits noted above.


## Language reference essentials

- Types and literals in detail: integer is signed 32 bit and also serves as boolean with TRUE 1 and FALSE 0, float is 32 bit in LSL variables even though LLSD reals are doubles, string is UTF-8, key is a UUID string type, vector literals use angle brackets with 3 floats, rotation literals use angle brackets with x y z s quaternion components, list literals use square brackets with mixed types.

- Operators and flow: standard arithmetic, comparison, logical, and bitwise operators, if and else, while, do while, for, jump with labels, return, and state changes with the state keyword, and no user function pointers, no recursion guarantees to rely on, and no exceptions.

- String and list work dominates real scripts: llGetListLength, llList2String and typed llList2* getters, llDumpList2String, llParseString2List and llParseStringKeepNulls, llStringLength, llSubStringIndex, llGetSubString, llInsertString, and the memory cost of every concatenation.

- Key maths and world functions: llGetPos, llGetRot, llSetPos and llSetRot with 10 metre and rotation limits and energy costs, llRezObject and llRezAtRoot, llSetPrimitiveParams and llGetPrimitiveParams with the large PRIM_* constant family, llSetLinkPrimitiveParamsFast for linksets, llRayCast, llCastRay, sensors with llSensor and llSensorRepeat, and physics functions llSetStatus, llSetBuoyancy, llApplyImpulse.

## Event catalogue in detail

- Lifecycle: state_entry, state_exit, on_rez with start parameter, attach with avatar key or NULL_KEY on detach, changed with CHANGED_* flags for inventory, link, scale, teleport, region, and owner.

- Interaction: touch_start, touch, touch_end with detected functions llDetectedKey, llDetectedPos, llDetectedTouchUV and face, collision_start, collision, collision_end, land_collision variants, control with PERMISSION_TAKE_CONTROLS, at_target and not_at_target, at_rot_target and not_at_rot_target.

- Communication: listen on channels with llListen and llListenRemove, link_message between prims in a linkset, dataserver for notecard lines and other async data, http_request and http_response for in world web, email legacy, remote_data legacy XML-RPC, money on payment, transaction_result for Linden dollar transfers.

- Movement and objects: moving_start, moving_end, object_rez, sensor and no_sensor, timer from llSetTimerEvent, run_time_permissions after llRequestPermissions, experience_permission and experience_permission_denied for Experiences.

## Permissions system in detail

- Request with llRequestPermissions with a bitmask of PERMISSION_DEBIT, PERMISSION_TAKE_CONTROLS, PERMISSION_TRIGGER_ANIMATION, PERMISSION_ATTACH, PERMISSION_TRACK_CAMERA, PERMISSION_CONTROL_CAMERA, PERMISSION_TELEPORT, PERMISSION_SILENT_ESTATE_MANAGEMENT, PERMISSION_OVERRIDE_ANIMATIONS, PERMISSION_RETURN_OBJECTS, PERMISSION_CHANGE_LINKS, PERMISSION_CHANGE_JOINTS, PERMISSION_CHANGE_PERMISSIONS, and PERMISSION_RUN_SCRIPTS and others per current definitions YAML.

- Handle the run_time_permissions event and also poll llGetPermissions, because grant can be silent for some permissions and denial is often silent with no event error.

- Debit permission is special: only grant it to objects you trust, it allows llGiveMoney and llAdjustCredit style calls to take Linden dollars, and it is the classic scam vector in freebie scripts.

## Mono, memory, and performance in detail

- Mono scripts report memory via llGetObjectMemory and llScriptProfiler in SL, stack heap collision means stack plus heap exceeded the 64 KB Mono limit, and large lists and long strings are the usual cause.

- Use PyOptimizer patterns by hand even without the tool: fold constants, remove unused functions and globals, shorten strings, avoid building lists by repeated concatenation in loops, and prefer llListReplaceList and slice operations carefully.

- Throttles to design around: llSay, llWhisper, and llShout range and channel rules, llInstantMessage delays in bulk use, llEmail delays, llHTTPRequest throttles per object, llSetPrimitiveParams historical 0.2 second delay versus llSetLinkPrimitiveParamsFast, and per parcel script and chat limits enforced server side.

## OSSL catalogue highlights

- NPC functions: osNpcCreate, osNpcMoveTo, osNpcSay, osNpcRemove, osAvatarPlayAnimation and related, OpenSim only and central to bot content there.

- Teleport and world: osTeleportAgent, osTeleportObject, osSetDynamicTextureURL and osSetDynamicTextureData for dynamic textures, osSetPrimFloatOnWater, osWindActiveModelPluginName, osGetGridName and osGetGridLoginURI for grid aware scripts.

- Threat levels in detail: None, VeryLow, Low, Moderate, High, VeryHigh, Severe, assigned per function in OpenSim docs and enforced against estate owner, estate manager, parcel owner, and parcel group in osslEnable.ini with per function Allow_ lists, so the same script can work for the owner and silently fail for a buyer.

## SLua in detail

- SLua is Linden Lab Luau: typed optional annotations, string interpolation, continue statements, compound assignment, and Luau standard library patterns, with serializable and relocatable script state as the design goal for region crossings.

- Tooling for SLua comes from lsl-definitions slua_definitions.yaml and the official VS Code plugin, and LSL optimisers and linters do not apply, so keep LSL and SLua code paths and tests separate.

## Debugging playbook

- Add llOwnerSay debug output gated by a debug flag, because owners see it and it does not spam public chat, and remove or gate it before sale.

- Reproduce on Aditi for SL behaviour and on a local OpenSim for engine behaviour, and record grid, region, engine, and compiler in the bug report, because LSL without an engine label is not reproducible.

- For a script that does nothing, check in order: script is set running and compiled with no error, the object has the needed permissions, the event you expect is actually firing, listen handles are not filtered to a different channel or key, and OSSL threat level is not blocking the call.
