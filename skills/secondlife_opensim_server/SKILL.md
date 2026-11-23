---
name: secondlife_opensim_server
description: "Run, configure, extend, and debug OpenSimulator grids and regions in C#, including ROBUST services, region modules, physics, and scripting engines."
---

# OpenSimulator Server

## Use the canonical source

- Clone OpenSim from its canonical git at opensimulator.org and treat github.com/opensim/opensim as a mirror that syncs about every 10 minutes, in C# under BSD on .NET 8 for 0.9.3 and later, built with Prebuild via prebuild.xml and runprebuild.sh.

- Remember its own README warning that it is alpha style software, and read config from OpenSim.ini, Robust.ini, and config-include, because behaviour is sprawling INI driven.

- Note that OpenSim bundles its own fork of libOpenMetaverse, with a dotnet6 branch for 0.9.3, and that fork is not interchangeable with LibreMetaverse.

## Run it as your test grid

- Start in standalone mode first: one process serves region plus grid services on port 9000 with a login URI like http://127.0.0.1:9000, so you can log a viewer or LibreMetaverse client in locally and breakpoint both sides.

- Move to grid mode with ROBUST only when you need separate services: Robust.exe hosts Asset, Inventory, Grid, User Accounts, Authentication, Friends, and Hypergrid gatekeeper and useragent services apart from region servers.

- Keep database choice explicit, because SQLite, MySQL, and PostgreSQL backends change asset and inventory behaviour and make some bugs backend specific.

## Extend in the right layer

- Put region behaviour in a region module: shared or non shared IRegionModule code under OpenSim/Region/CoreModules, OptionalModules, Physics, ScriptEngine, or ClientStack.

- Read the Linden client stack under OpenSim/Region/ClientStack/Linden/UDP and Linden/Caps when a viewer bug might be server side, because LLClientView, the packet pool, throttles, and caps handlers live there.

- Do not port Hypergrid trust or asset behaviour into Agni client code, because Hypergrid federation has no Second Life equivalent.

## Match physics and scripting to the mesher and engine

- Pick one physics stack and match its mesher: BulletSim with Meshmerizer, ubODE as the recent default with ubODEMeshmerizer, legacy ODE, or basicphysics as a null engine, and expect collisions to mismatch silently if mesher and engine disagree.

- Expect vehicle, raycast, and prim physics results to differ from SL Havok, so never tune physics constants against OpenSim alone.

- Configure scripting explicitly with YEngine as the current engine or XEngine as legacy, and set OSSL threat levels and osslEnable.ini allow lists before testing scripts that use os functions.

## Know the forks and their limits

- Treat AuroraSim as dead archaeology with development stopped in 2014, Halcyon as a 2010 fork for load behaviour, and WhiteCoreSim as an Aurora continuation whose current maintenance could not be verified in 2026, and verify any fork repo activity before depending on it.

- Use the OutWorldz and DreamGrid installer docs for plain English region, physics, and scripting explanations when core OpenSim docs are too terse.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for the opensim/opensim mirror and related OpenSim org repos.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [OpenSimulator wiki](http://opensimulator.org/wiki/Development) for developer docs, git access, and configuration.

- [OpenSim GitHub mirror](https://github.com/opensim/opensim) for browsable code, releases, and issues routing.

- [OutWorldz help](https://www.outworldz.com/Outworldz_installer/Help/Region.htm) for end user region and physics guidance.


## Architecture in detail

- Region server OpenSim.exe hosts one or more regions with a Scene per region, SceneObjectGroup and SceneObjectPart for linksets, terrain, land, and estates, and loads shared and per region modules at startup.

- ROBUST services in detail: Asset service stores asset blobs by UUID, Inventory service stores user inventory trees, Grid service registers regions, User Accounts and Authentication issue and validate tokens and passwords, Friends, Groups in grid mode, and Hypergrid Gatekeeper and UserAgent handle foreign visitors.

- Data layer: connectors for SQLite for zero config standalone, MySQL as the common production choice, and PostgreSQL, with migrations run at startup, and asset storage optionally on filesystem or external services in advanced configs.

- Client stack in detail: LLClientView per connected client in OpenSim/Region/ClientStack/Linden/UDP implements the Linden UDP protocol, packet pooling, resend, throttle, and object update prioritisation, and Linden/Caps implements the caps handlers OpenSim supports, which is a subset of Agni caps with some name differences.

## Configuration walkthrough

- First run standalone: start OpenSim.exe, create a user account at the console, create a region with a name, UUID, port, and estate, then log in with a viewer or LibreMetaverse client using the login URI http://127.0.0.1:9000.

- Key OpenSim.ini sections: Startup, Network with http_listener_port, Architecture, ClientStack, Caps, Messaging, Voice, Physics with physics engine selection, ScriptEngine with XEngine or YEngine selection, YEngine and XEngine subsections, OSSL with threat and enable settings pointing at osslEnable.ini, and GridInfo for login page info.

- Grid mode: configure Robust.ini for service connectors and ports, point each region OpenSim.ini at the ROBUST URLs for assets, inventory, grid, and auth, and open the documented TCP ports for services and UDP plus TCP for regions.

- Console commands worth knowing: show stats, show queues, show users, create user, create region, save prims, save oar, load oar, backup, kick user, alert, and shutdown, run from the region or ROBUST console.

## Region modules in detail

- Write a module by implementing IRegionModuleBase or the shared and non shared interfaces for your OpenSim version, register it via Mono.Addins extension points, drop the DLL in bin, and enable it in config where required.

- Shared modules load once for all regions in the process and suit services, non shared modules load per region and suit per region state such as in world features.

- OptionalModules and CoreModules in tree show canonical patterns for voice, groups, profiles, search, world map, terrain, and physics integration, copy their lifecycle handling for scene registration and event subscription.

## Physics in detail

- BulletSim: Bullet physics via a native bridge, supports varregions, vehicles with known quirks, and Meshmerizer meshing, configured in a BulletSim section.

- ubODE: Ubit Umarov ODE fork, default in recent OpenSim, requires ubODEMeshmerizer, often preferred for avatar and vehicle feel closer to current OpenSim expectations.

- ODE legacy and basicphysics: ODE is the older OpenDynamicsEngine path, basicphysics is a no collision placeholder for testing and headless runs.

- Always pair mesher and engine as documented for that release and restart clean after switching, because cached mesh shapes from the wrong mesher cause phantom collisions and fall through floors.

## Scripting engines in detail

- YEngine: from XMREngine, microthreaded script execution, state persistence across region restart, SL like expression evaluation order, and sane llSleep behaviour, the recommended engine for new installs.

- XEngine: legacy AppDomain based engine, historically opposite evaluation order in some expressions and llSleep stalls, still present for compatibility.

- Script limits and controls live in engine config: max script memory, allowed assemblies, sensor and timer behaviour, and OSSL enable files, set them before load testing content copied from SL.

## OAR, IAR, and content portability

- OAR archives save and load whole regions with terrain, objects, and assets via save oar and load oar, IAR archives do the same for user inventory, both are the standard OpenSim backup and migration path and LibreMetaverse.Archiving can read OAR.

- Hypergrid allows avatar travel and limited asset transfer between grids, with suitcase inventory semantics, never assume an Agni asset or script behaves identically after a Hypergrid transfer.

## Operations playbook

- Monitor with show stats and log files under bin, watch client queues for a viewer that cannot keep up, and separate region CPU, script CPU, and physics time in diagnosis.

- For a region that will not start, check in order: port already in use, database connection, ROBUST reachability in grid mode, physics native library load, and a module DLL built for the wrong .NET version.

- Forks reality check in detail: AuroraSim stopped in 2014, WhiteCoreSim continues Aurora lineage with unverified current activity, Halcyon forked in 2010 for InWorldz scale, SimianGrid is a PHP services alternative, DreamGrid is an installer distribution not a fork, use upstream OpenSim unless a fork feature is the explicit goal.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/config-estates-ini.md` (997 bytes)
- `references/config-flotsamcache-ini.md` (3,793 bytes)
- `references/config-grid-ini.md` (2,777 bytes)
- `references/config-gridcommon-ini.md` (8,689 bytes)
- `references/config-gridhypergrid-ini.md` (3,687 bytes)
- `references/config-opensimdefaults-ini.md` (80,168 bytes)
- `references/config-os-webrtc-janus-ini.md` (1,843 bytes)
- `references/config-ossldefaultenable-ini.md` (12,860 bytes)
- `references/config-osslenable-ini.md` (4,046 bytes)
- `references/config-pcampbot-ini.md` (949 bytes)
- `references/config-regions-ini.md` (3,796 bytes)
- `references/config-robust-hg-ini.md` (40,646 bytes)
- `references/config-robust-tests-ini.md` (20,588 bytes)
- `references/config-sqlitestandalone-ini.md` (1,778 bytes)
- `references/config-standalone-ini.md` (6,035 bytes)
- `references/config-standalonecommon-ini.md` (16,630 bytes)
- `references/config-standalonehypergrid-ini.md` (9,637 bytes)
- `references/opensim-api.md` (1,194,610 bytes)
- `references/opensim-console-commands.md` (5,980 bytes)
- `references/opensim-ini-reference.md` (55,858 bytes)
- `references/opensim-lsl-implementation.md` (116,693 bytes)
- `references/opensim-operations-guide.md` (87,952 bytes)
- `references/opensim-source-tree.md` (62,577 bytes)
- `references/ossl-functions.md` (95,151 bytes)
- `references/robust-ini-reference.md` (28,307 bytes)
