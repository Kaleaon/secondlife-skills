
# OpenSimulator Production Operations — Deep Reference Guide

This guide is for running OpenSimulator (opensim/opensim mirror; canonical git at opensimulator.org; C#, BSD, .NET 8 for 0.9.3+) as more than a weekend standalone: scaling ROBUST grid services, choosing and tuning database and asset backends, consolidating and sizing regions including varregions, Hypergrid configuration, monitoring that catches failure before users do, backup and OAR strategy, an honest physics-engine comparison, script-engine tuning for XEngine and YEngine, security hardening for a public grid, and an upgrade playbook that does not strand a grid on a dead version. Config names are taken from the stock OpenSim.ini.example and Robust.ini.example reproduced in the appendix, so every option named here can be found in those files.

## Reference architectures: standalone, grid, and hypergrid-enabled grid

Standalone collapses region and all services into one process (OpenSim.exe, default port 9000) with SQLite or a local MySQL — correct for development, testing viewers, and single-user worlds, wrong for anything public because every scaling and backup axis is fused. Grid mode splits services into ROBUST (Robust.exe) — assets, inventory, grid registry, user accounts, authentication, friends, groups, presence — and one or more region processes that connect to it; this is the smallest production shape and the one this guide assumes. A Hypergrid-enabled grid additionally runs Gatekeeper and UserAgent services so foreign avatars can visit and locals can leave, which changes the trust model fundamentally (see the Hypergrid section). Plan the split before you need it: moving a busy standalone to grid mode means migrating its database into service schemas under user load, which is the worst time to learn your asset store's quirks.

## Scaling ROBUST: what actually bottlenecks

ROBUST services are mostly stateless HTTP handlers over a database, so they scale by adding processes behind the service URLs regions are configured with — but the database is the shared truth and becomes the bottleneck first. In practice: the asset service dominates by request count (every texture, mesh, and sound a viewer fetches through grid services on login and teleport), inventory dominates by query complexity (deep folder trees, per-item permission checks), and authentication spikes at login storms (events, restarts). Scale order that works: put the database on its own host with fast storage first, then split asset reads (the asset service is the most cache-friendly and the safest to replicate read-side), then separate inventory onto its own ROBUST instance and port, and only then multiply region hosts. Each ROBUST service is configured independently in Robust.ini with its own connector and port, so 'one ROBUST' is a deployment choice, not an architecture limit.

## Database choice and tuning: SQLite, MySQL/MariaDB, PostgreSQL

SQLite is zero-administration and entirely adequate for standalone and tiny grids; its write serialisation collapses under multi-region grid load and it should never host a public grid's inventory. MySQL/MariaDB with InnoDB is the common production choice: give InnoDB a buffer pool sized to the working set (assets metadata and inventory tables are hot; asset blobs belong in the asset store, not in oversized DB rows where a backend allows separation), watch slow queries on inventory folder traversal and asset existence checks, and index discipline matters more than raw hardware. PostgreSQL is supported and behaves well, with a smaller operational community in OpenSim specifically — expect fewer grid-operator recipes. Whichever engine: regions and ROBUST both hold connection pools, total connections scale with region count, and an un-tuned max_connections is a classic cause of 'grid dies at 40 regions' that is actually the database refusing the 41st process.

## Asset service backends and asset hygiene

Assets are immutable blobs keyed by UUID — create once, never modify, delete only by garbage collection — which makes them the easiest service to scale and the easiest to bloat. Backends and strategies in use: database-backed assets (simple, couples blob IO to your DB), filesystem and clustered file stores, and external object storage via community connectors, plus asset caching layers in front (including HTTP caches for viewer-facing fetches, since GetTexture/GetMesh traffic is cacheable by UUID). Hygiene decides long-term cost: every upload, every temp prim, every OAR import creates assets that nothing automatically reclaims on most grids, so du growth is monotonic without a garbage-collection policy. Measure assets by count and bytes monthly, sample what is growing (uploaded textures and meshes from building activity dominate), and never run an untested asset GC against the only copy — asset deletion bugs are unrecoverable by definition.

## Inventory service: the fragile one

Inventory is a per-user tree with per-item permissions, links, and wearables semantics that AIS-style operations from viewers exercise hard. It is the service most sensitive to database latency and the one whose corruption hurts users most visibly (missing folders, broken links, unwearable outfits). Operational rules: back inventory up separately and more often than assets (it changes constantly; assets barely change), test restores by logging a test account in against the restored copy, and treat any migration that rewrites item or folder UUIDs as a breaking event for every link and outfit in the grid. When consolidating grids or merging user bases, inventory is the long pole, not regions.

## Region sizing: regions per process, per host, and the prim/script budget

A region process can host multiple regions, but they share CPU, memory, and the process's fate: one region's script storm or crash takes its housemates down. Production practice separates busy public regions into their own processes and packs quiet, low-prim regions together. The real budgets are script count and physics load, not prim count alone: a 15,000-prim region of static unscripted prims is cheap; a 2,000-prim region with 800 active scripts and pathfinding vehicles is not. Measure per region: script time per frame, physics time, agent count, and memory growth over uptime (a region that leaks will show it in a week-long memory graph before it crashes). Restart regions on a schedule during quiet hours rather than waiting for the leak to choose the moment.

## Varregions: what changes operationally

A varregion is a single region larger than the legacy 256x256 m (512, 768, 1024 and up, in 256 m multiples) configured by region size in the region ini. Benefits are real: no border crossings inside the varregion, continuous terrain and water, simpler land layout. Costs are equally real: viewers must support the sizes (modern ones do), physics and terrain data scale with area, a varregion concentrates load into one process that cannot be split across hosts, and backup/OAR handling for very large varregions produces very large archives. Neighbour and teleport behaviour at varregion edges differs from classic regions, and Hypergrid destinations may not accept all sizes gracefully. Choose varregions for contiguous mainland-style builds; keep classic 256 regions for dense social hubs you may need to move or split.

## Region consolidation and splitting playbook

Consolidating quiet regions: take OARs of each source region, create the target region, load OARs with displacement offsets where the tooling supports merging, reconcile estate and parcel ownership (parcel UUIDs and land layout do not survive naive merges — plan to rebuild parcels and re-deed objects), and communicate a freeze window because building during a merge loses work. Splitting a busy region is the reverse with one addition: inventory and object ownership stay stable, but landmark and scripted-object references to region-local coordinates and region names must be audited. In both directions, test with a copy of the grid database and a test viewer login before touching production: most consolidation failures are permission and ownership surprises, not data loss.

## Hypergrid: gatekeeper, useragent, and the trust model

Hypergrid links grids: a local user teleports via the Gatekeeper service to a foreign grid, which validates the visitor with the home grid's UserAgent service, and the visitor arrives with a suffixed name (avatar@home-grid) and a suitcase inventory subset. Enabling it is a policy decision wearing a config costume: foreign visitors can bring assets your grid then serves and stores, your users can carry grid assets out (subject to permissions as enforced by foreign code you do not control), and name/identity spoofing resistance depends on both grids behaving. Operationally: run gatekeeper on its own well-known port and hostname (HG addresses are baked into links and landmarks — changing your HG hostname later breaks every external reference), set the home URI consistently across Robust.ini and region config, test both directions with a friendly grid, and monitor foreign-agent counts separately from locals because abuse arrives through the same door as tourism.

## Monitoring: metrics that predict failure

Monitor three layers. Host: CPU steal, memory, disk IO latency (asset and DB hosts are IO-bound before they are CPU-bound), and disk growth rate with alerts on projected-full date, not percentage. Process: per-region frame time breakdown (physics, scripts, agent updates, and time dilation — dilation below ~0.9 sustained is users feeling lag), script count and top script consumers, agent counts, and ROBUST request latency per service with the asset service charted separately. Synthetic: a bot account (LibreMetaverse TestClient pattern) that logs in every few minutes, teleports between two regions, and fetches a known asset — this catches the class of failure where every process is 'up' but login is broken, which is the class users report. Log aggregation matters because OpenSim logs are verbose and per-process; centralise them or you will debug outages by ssh-ing between hosts reading tails.

## Backup strategy: databases, assets, and OARs are three different backups

Database backup: consistent dumps or snapshots of the grid database(s) on a schedule matched to change rate (inventory hourly-to-daily, accounts with it), tested by restore. Asset backup: the asset store is large and mostly immutable, so back it up incrementally and completely, and remember a database restore pointing at a truncated asset store yields a grid of grey textures and missing meshes that still 'works' in every superficial check. OAR/IAR backup: per-region OAR exports on a rotation give you region-level portability that database backups do not — you can load an OAR onto a different grid, a database dump you cannot. The three are complements, not substitutes. Keep at least one copy off the host (and one offline or immutable if ransomware is in your threat model), and run a full restore drill — fresh host, restore DB, restore assets, load one OAR, log in — at least twice a year, timing it.

## Physics engines compared: BulletSim, ubODE, ODE, basicphysics

BulletSim (Bullet via the native bridge): the long-standing default in many distributions, supports varregions, vehicles behave recognisably to SL users in most cases, meshing via Meshmerizer. Its costs: native library versioning per platform, and vehicle and collision edge cases that differ from both SL Havok and ubODE. ubODE (Ubit Umarov's ODE fork): default in recent OpenSim, generally preferred for avatar movement feel and for prim and vehicle behaviour in current builds, requires ubODEMeshmerizer — pairing ubODE with the wrong mesher is the single most common cause of 'collisions are wrong everywhere' after an engine switch. Legacy ODE: kept for compatibility, not a choice for new grids. basicphysics/POS: no real collision — for headless, testing, and script-only regions where physics cost is pure waste. There are no trustworthy cross-engine benchmark numbers published by the project that transfer to your content: measure on your own regions by loading the same OAR under each engine and timing physics frame time with the same avatar load, because mesh density and vehicle count dominate engine choice in practice. Whatever you choose, choose once per grid if you can — physics feel is content-visible and switching engines re-tunes every vehicle and physical object on the grid.

## Script engines: YEngine vs XEngine tuning

YEngine is the current engine: microthreaded execution, state saved across region restarts, SL-like evaluation order, and sane llSleep semantics. XEngine is the legacy AppDomain engine with different evaluation order in places and llSleep stalls; keep it only for content that provably depends on it. Tuning that matters in YEngine: script memory limits per script and per object, the thread and priority behaviour under load, and sensor/timer resolution floors that stop pathological scripts from consuming a region. The operational lever is measurement: OpenSim exposes per-script and per-object script time; publish a fair-use expectation, find the top consumers, and work with their owners — a handful of badly written timer-and-sensor scripts is the normal cause of 'region script lag', not the engine. OSSL threat-level configuration (osslEnable.ini) is a security control as much as a feature switch: enabling os* functions for everyone at high threat levels hands region-control primitives to any visitor's script.

## Security hardening for a public grid

Patch and version discipline first: run a supported OpenSim and .NET, because grid software with public UDP and HTTP surfaces accumulates known exploits. Network: expose only the ports the grid needs (region UDP/TCP, ROBUST HTTP services viewers and regions actually call), put service-to-service endpoints (the ones regions use to write assets and inventory) out of public reach where your topology allows, and terminate viewer-facing HTTP cleanly. Accounts: registration is an abuse magnet — email verification, rate limits, and a manual approval option are grid policy decisions to make before opening, not after the first spam wave. Estate and god powers: audit who holds them, log their use, and never run day-to-day building on a god account. OSSL and scripting: default threat levels low, raise per-function for trusted creators. Uploads: asset and mesh upload is untrusted content parsing — keep the native libraries (mesh, JPEG2000) patched via the OpenSim build you ship. Backups are a security control too (see backup section) — the grid you can restore is the grid ransomware cannot keep.

## Upgrade playbook

Never upgrade in place on the only copy. Sequence that works: read the release notes for config changes (OpenSim upgrades routinely add, rename, or re-default ini options, and the example files are the diff that matters — the appendix reproduces the current examples so you can diff yours against them); snapshot or dump the database; build the new version beside the old; run one test region and the ROBUST services from the new build against a copy of the database and log in with a test viewer, exercising login, teleport, inventory, scripted objects, and physics; then upgrade services first or regions first according to the release notes' compatibility statement, in a maintenance window, keeping the old binaries and the pre-upgrade database dump until the new build has survived a full busy period. Database migrations run automatically at startup on both ROBUST and regions — that is convenient and irreversible, which is why the dump comes first.

## Capacity planning and cost shape

A grid's costs are dominated by: region host CPU during peak concurrency (scripts and physics), asset storage growth (monotonic), asset bandwidth on login and teleport peaks (viewer fetches are bursty and cache-sensitive), and operator time. Plan capacity in concurrent avatars per region host measured on your content, not in regions per host quoted from forums. Keep a month of headroom graphs before events, and pre-scale for announced events by splitting the event region onto its own process and host and raising its script and agent limits deliberately rather than discovering them mid-event.

## Troubleshooting field guide

Login fails for everyone but processes are up: check authentication service and database connectivity from ROBUST, then the synthetic login bot's exact failure stage. Teleports fail one direction: check region-to-region and region-to-ROBUST reachability and the destination region's handshake in logs; HG teleports add gatekeeper DNS and port checks. Assets grey for many users: asset service latency and errors, then cache/CDN if present, then database asset table health. One region lags: read its frame-time breakdown before touching the host — scripts, physics, or agent count will name themselves. Inventory missing for one user: that user's inventory rows and the inventory service log for their UUID, not a grid-wide restore. Memory climbs until crash: per-region memory graph, suspect script state growth or a leaking module, mitigate with scheduled restarts while you bisect by disabling modules on a copy.

## Console commands: the operator's real interface

Region console essentials: 'show info' and 'show stats' for health, 'show users' and 'show agents' for occupancy, 'show queues' for client queue backlogs that reveal a viewer or network problem, 'show threads' and 'show memory' when diagnosing leaks, 'create user' and 'reset user password' for account work, 'create region' and 'remove-region' for layout, 'save oar <file>' and 'load oar <file>' for region archives, 'save prims' and 'load prims' for XML object export, 'export-map' for map tiles, 'terrain load', 'terrain fill', and 'terrain elevate' family for land work, 'kick user' and 'alert' for live moderation, 'backup' to force persistence flush, 'config show' to print the effective merged configuration — the single most underused diagnostic, because half of all 'the ini is ignored' bugs are an override in config-include winning over OpenSim.ini — and 'shutdown'. ROBUST console has its own smaller set including service status and user account commands. Script the console over its HTTP or telnet interface for monitoring rather than screen-scraping interactive sessions.

## Ports and endpoints map

Standalone: one HTTP listener (default 9000) carries login, caps, and services, plus region UDP on the region's port (default 9000 range per region ini). Grid: ROBUST public services conventionally on 8002 (the port in the stock examples' PublicPort guidance for grids), private service endpoints on 8003 which the stock configuration comments explicitly warn must be firewalled from the outside because regions use them for operations that must not be world-accessible, and each region with its own TCP HTTP listener and UDP port from its region ini. Hypergrid gatekeeper rides the public services port with its well-known path. Voice modules, map tiles, and web front ends (Wifi and similar) add their own listeners. Draw this map for your grid and keep it current: every outage runbook and every firewall review starts from it, and the 8002/8003 public/private split is the security decision the stock files are quietly making for you.

## Login and presence: how a session is assembled

A viewer login hits the login service (ROBUST in grid mode), which authenticates against UserAccounts, asks Presence and Grid services where the user should land, creates a session, and returns the seed capability and circuit data the viewer uses to reach the region. The region then validates the arriving agent with the services, pulls inventory root and appearance data, and registers presence. Each arrow in that chain is a separate failure with a separate log line on a separate process, which is why 'login is down' triage starts by naming which stage the synthetic bot died at. Presence is also why abrupt region crashes leave ghost logins: presence cleanup depends on logout or timeout paths, and a grid that restarts regions ungracefully will accumulate stale presence until timeouts clear it.

## Groups, friends, and profiles services

In grid mode these are ROBUST-provided or module-provided services with their own connectors and tables; in standalone they collapse into the single process. Groups in particular has two historical implementations (the core groups module and the external XmlRpc/Flotsam-style groups) with different performance and feature profiles — know which one your grid runs before debugging group chat lag, because group IM fan-out is a real load: one message to a 500-member group is 500 deliveries through the messaging path, and event-day group chat is a measurable ROBUST and region load. Profiles and classifieds are often served by external PHP modules in older grids; a modern build keeps them in ROBUST-adjacent services, but any external dependency is another failure domain to monitor.

## Map, search, and the web tier

The world map is generated from region registrations and map tile images regions upload; stale map tiles after region moves are a registration and tile-cache problem, not a viewer problem. Search (events, classifieds, places) is served by data snapshot modules that periodically index region and parcel data — search lagging reality by hours is the snapshot interval working as designed. Web front ends for account registration and grid status (Wifi-style) talk to ROBUST services; treat them as public web applications with public web vulnerabilities, patch them like it, and never let the web tier hold god-level service credentials.

## Data migrations and schema ownership

OpenSim stores data per service with its own tables and migration versions: accounts, auth, grid regions, presence, inventory folders and items, assets metadata, friends, groups. Migrations run automatically at service startup when the code version advances. Two operational consequences: first, you cannot trivially downgrade after a migration, so backups precede upgrades, always; second, running mixed old and new builds against one database during a rolling upgrade is only safe when the release notes say the schemas are compatible — assume they are not. When moving a grid between database engines (SQLite to MySQL is the common one), use the service-level export paths and test logins against the result rather than hand-copying tables whose column semantics shifted between versions.

## Event operations: running a 100-avatar event on a normal grid

Two weeks out: move the event region to its own process and host, raise agent limits deliberately, and load-test with bots at half the expected concurrency while watching script and physics time. One week out: freeze content changes in the region, take an OAR, and rehearse the stream and voice path (parcel media is external — test the actual stream URL from outside your network). Day of: staff on estate powers but building on non-god accounts, a second empty overflow region with a landmark ready, group chat moderated and announcements rehearsed, and one operator whose only job is watching dilation, agent count, and the synthetic login. After: keep the region on its own process until traffic decays naturally; consolidating it back the same night is how post-event crashes happen.

## Costed example: small public grid on one host versus split

One-host shape: a single 8-core host runs ROBUST, MySQL, and four region processes. It works until the first busy evening couples every failure domain: a script storm in one region starves the asset service of CPU, logins slow, and the operator cannot tell which layer is at fault because all graphs move together. Split shape: database and ROBUST on a services host with fast SSD, regions on one or two compute hosts, assets backed up off-box. The split costs an extra host and buys independent scaling, independent failure, and graphs that name the guilty layer. For most small grids the trigger to split is not avatar count, it is the first time an event in one region degraded login for the whole grid.

## Disaster recovery runbook skeleton

Detect: synthetic login failure or user reports plus process checks. Triage in order: host alive, database accepting connections, ROBUST services answering on public and private ports, regions registered in the grid service, asset fetch of a known UUID succeeding. Recover: restart the smallest guilty unit (a region, then a service, then the stack), never the whole grid at once unless the database itself is the fault. Restore path: if data is corrupt, restore the database dump to a parallel instance, point a test standalone at it, verify a login and inventory, then cut over. Communicate at each stage on an out-of-band channel (a status page not hosted on the grid's own web tier). Write the post-incident note the same day: cause, detection gap, and the one monitoring or automation change that would have caught it sooner.

## Appendix: documented options from the stock example configurations

Every option declared with a ;# directive in OpenSim.ini.example and Robust.ini.example, with the description text that follows the directive in the stock file. These are the options the stock configuration itself documents; OpenSimDefaults.ini carries further defaults. Use 'config show' on a running region to see effective values after all includes merge.

### OpenSim.ini.example

- `ConsolePrompt` — Console prompt Certain special characters can be used to customize the prompt Currently, these are \R - substitute region name

- `ConsoleHistoryFileEnabled` — Console commands can be saved to a file, so the command history persists after a restart. (default is false)

- `ConsoleHistoryFile` — The history file can be just a filename (relative to OpenSim's bin/ directory or it can be a full path to somewhere else. (default is OpenSimConsoleHistory.txt in bin/)

- `ConsoleHistoryFileLines` — How many lines of command history should we keep? (default is 100)

- `ConsoleHistoryTimeStamp` — Time stamp commands in history file (default false)

- `save_crashes` — Set this to true if you want to log crashes to disk this can be useful when submitting bug reports. However, this will only log crashes within OpenSimulator that cause the entire program to exit

- `crash_dir` — Directory to save crashes to if above is enabled (default is /opensimdir/crashes/*.txt or C:\opensim\crashes\*.txt)

- `PIDFile` — Place to create a PID file

- `region_info_source` — Determine where OpenSimulator looks for the files which tell it which regions to server Default is "filesystem"

- `regionload_regionsdir` — Determines where the region XML files are stored if you are loading these from the filesystem. Defaults to bin/Regions in your OpenSimulator installation directory

- `regionload_webserver_url` — Determines the page from which regions xml is retrieved if you are loading these from the web. The XML here has the same format as it does on the filesystem (including the <Root> tag), except that everything is also enclosed

- `allow_regionless` — Allow the simulator to start up if there are no region configuration available from the selected region_info_source.

- `NonPhysicalPrimMin` — Minimum size for non-physical prims.  Affects resizing of existing prims.  This can be overridden in the region config file (as NonPhysicalPrimMin!).

- `NonPhysicalPrimMax` — Maximum size for non-physical prims.  Affects resizing of existing prims. This can be overridden in the region config file (as NonPhysicalPrimMax!).

- `PhysicalPrimMin` — Minimum size where a prim can be physical.  Affects resizing of existing prims.  This can be overridden in the region config file.

- `PhysicalPrimMax` — Maximum size where a prim can be physical.  Affects resizing of existing prims.  This can be overridden in the region config file.

- `ClampPrimSize` — If a viewer attempts to rez a prim larger than the non-physical or physical prim max, clamp the dimensions to the appropriate maximum This can be overridden in the region config file.

- `LinksetPrims` — Maximum number of prims allowable in a linkset. Affects creating new linksets. Ignored if less than or equal to zero. This can be overridden in the region config file.

- `AllowScriptCrossing` — Allow scripts to keep running when they cross region boundaries, rather than being restarted.  State is reloaded on the destination region. This only applies when crossing to a region running in a different simulator.

- `TrustBinaries` — Allow compiled script binary code to cross region boundaries. If you set this to "true", any region that can teleport to you can inject ARBITRARY BINARY CODE into your system. Use at your own risk. YOU HAVE BEEN WARNED!!!

- `InworldRestartShutsDown` — If you have only one region in an instance, or to avoid the many bugs that you can trigger in modules by restarting a region, set this to true to make the entire instance exit instead of restarting the region. This is meant to be used on systems where some ext

- `MinimumTimeBeforePersistenceConsidered` — Objects will be considered for persistance in the next sweep when they have not changed for this number of seconds.

- `MaximumTimeBeforePersistenceConsidered` — Objects will always be considered for persistance in the next sweep if the first change occurred this number of seconds ago.

- `physical_prim` — if you would like to allow prims to be physical and move by physics with the physical checkbox in the client set this to true.

- `meshing` — ZeroMesher is faster but leaves the physics engine to model the mesh using the basic shapes that it supports. Usually this is only a box or a sphere Default is ubODEMeshmerizer

- `DefaultScriptEngine` — Default script engine to use. Currently, we only have YEngine

- `HttpProxy` — Http proxy setting for llHTTPRequest and dynamic texture loading, if required

- `HttpProxyExceptions` — If you're using HttpProxy, then you can set HttpProxyExceptions to a list of regular expressions for URLs that you don't want to go through the proxy. For example, servers inside your firewall.

- `emailmodule` — The email module requires some configuration. It needs an SMTP server to send mail through.

- `SpawnPointRouting` — SpawnPointRouting adjusts the landing for incoming avatars. "closest" will place the avatar at the SpawnPoint located in the closest available spot to the destination (typically map click/landmark). "random" will place the avatar on a randomly selected spawnpo

- `TelehubAllowLandmark` — TelehubAllowLandmark allows users with landmarks to override telehub routing and land at the landmark coordinates when set to true default is false

- `AllowedClients` — Bar (|) separated list of viewers which may gain access to the regions. One can use a substring of the viewer name to enable only certain versions Example: Agent uses the viewer "Imprudence 1.3.2.0"

- `DeniedClients` — Bar (|) separated list of viewers which may not gain access to the regions. One can use a Substring of the viewer name to disable only certain versions Example: Agent uses the viewer "Imprudence 1.3.2.0"

- `GenerateMaptiles` — Map tile options. If true, then maptiles are generated using the MapImageModule below. If false then the texture referenced by MaptileStaticUUID is used instead, which can also be overridden in individual region config file(s).  If you do not want to upload ma

- `MapImageModule` — The module to use in order to generate map images. MapImageModule is the default.  Warp3DImageModule is an alternative experimental module that can generate better images.

- `MaptileRefresh` — If desired, a running region can update the map tiles periodically to reflect building activity. This names no sense of you don't have prims on maptiles. Value is in seconds.

- `MaptileStaticUUID` — If not generating maptiles, use this static texture asset ID This may be overridden on a per region basis in Regions.ini

- `TextureOnMapTile` — Use terrain texture for maptiles if true, use shaded green if false

- `DrawPrimOnMapTile` — Draw objects on maptile.  This step might take a long time if you've got a large number of objects, so you can turn it off here if you'd like.

- `TexturePrims` — Texture the faces of the prims that are rendered on the map tiles.

- `TexturePrimSize` — Only texture prims that have a diagonal size greater than this number

- `RenderMeshes` — Attempt to render meshes and sculpties on the map.

- `permissionmodules` — Permission modules to use, separated by comma. Possible modules are DefaultPermissionsModule, PrimLimitsModule

- `serverside_object_permissions` — These are the parameters for the default permissions module If set to false, then, in theory, the server never carries out permission checks (allowing anybody to copy any item, etc).  This may not yet be implemented uniformally.

- `allow_grid_gods` — This allows users with a UserLevel of 200 or more to assume god powers in the regions in this simulator. if you don't trust grid admins, what are you doing there?

- `region_owner_is_god` — Allow region owners to assume god powers in their regions

- `region_manager_is_god` — Allow region managers to assume god powers in regions they manage

- `simple_build_permissions` — More control over permissions This is definitely not SL! Provides a simple control for land owners to give build rights to specific avatars in publicly accessible parcels that disallow object

- `DefaultEstateName` — Name for the default estate

- `DefaultEstateOwnerName` — Name for default estate owner

- `DefaultEstateOwnerUUID` — If DefaultEstateOwnerUUID is left at UUID.Zero (as below) then a random UUID will be assigned. This is normally what you want

- `DefaultEstateOwnerEMail` — Email address for the default estate owner

- `DefaultEstateOwnerPassword` — Password for the default estate owner

- `enabled` — Enable the email module

- `enabled` — Enable sending email to regions not on current opensimulator instance. Currently does not work

- `enabled` — Enable sending email to the world.

- `ConsoleUser` — Configure the remote console user here. This will not actually be used unless you use -console=rest at startup.

- `http_listener_port` — Simulator HTTP port. This is not the region port, but the port the entire simulator listens on. This port uses the TCP protocol, while the region ports use UDP.

- `HttpBodyMaxLenMAX` — By default, llHTTPRequest limits the response body to 2048 bytes. This limit can be extended using HTTP_BODY_MAXLENGTH to a maximum of HttpBodyMaxLenMAX bytes. Please be aware that the limit can be set to insanely high values,

- `ExternalHostNameForLSL` — Hostname to use in llRequestURL/llRequestSecureURL if not defined - llRequestURL/llRequestSecureURL are disabled this should be reachable from internet and point this machine for standalones it can be

- `shard` — What is reported as the "X-Secondlife-Shard" Defaults to the user server url if not set The old default is "OpenSim", set here for compatibility The below is not commented for compatibility.

- `user_agent` — What is reported as the "User-Agent" when using llHTTPRequest Defaults to not sent if not set here. See the notes section in the wiki at http://wiki.secondlife.com/wiki/LlHTTPRequest for comments on adding " (Mozilla Compatible)" to the text where there are pr

- `XmlRpcRouterModule` — If enabled and set to XmlRpcRouterModule, this will post an event, "xmlrpc_uri(string)" to the script concurrently with the first remote_data event. This will contain the fully qualified URI an external site needs to use to send XMLRPC requests to that script

- `XmlRpcHubURI` — If XmlRpcRouterModule is set to XmlRpcGridRouterModule, the simulator will use this address to register xmlrpc channels on the external service

- `DisableFacelights` — Quash and remove any light properties from attachments not on the hands. This allows flashlights and lanterns to function, but kills silly vanity "Facelights" dead. Sorry, head mounted miner's lamps will also be affected.

- `SearchServerURI` — Optional. If given this serves the same purpose as the grid wide [LoginServices] SearchURL setting and will override that where supported by viewers.

- `DestinationGuideURI` — Optional. If given this serves the same purpose as the grid wide [LoginServices] DestinationGuide setting and will override that where supported by viewers.

- `whisper_distance` — Distance in meters that whispers should travel.

- `say_distance` — Distance in meters that ordinary chat should travel.

- `shout_distance` — Distance in meters that shouts should travel.

- `DisableInterRegionTeleportCancellation` — This option exists because cancelling at certain points can result in an unuseable session (frozen avatar, etc.) Disabling cancellation can be okay in small closed grids where all teleports are highly likely to suceed.

- `LandingPointBehavior` — This option exists to control the behavior of teleporting gods into places that have landing points and telehubs. Historically, there has been a difference: OpenSim (OS) has honored landing points and telehubs even for avatars with god permissions; SL lets god

- `OfflineMessageModule` — Module to handle offline messaging. The core module requires an external web service to do this. See OpenSim wiki.

- `OfflineMessageURL` — URL of web service for offline message storage. Leave it commented if your service is local to the sim.

- `StorageProvider` — For standalones, this is the storage dll.

- `port` — Set this to a nonzero value to have remote admin use a different port

- `access_password` — This password is required to make any XMLRPC call (should be set as the "password" parameter)

- `access_ip_addresses` — List the IP addresses allowed to call RemoteAdmin If access_ip_addresses isn't set, then all IP addresses can access RemoteAdmin. access_ip_addresses = 0.0.0.0, 0.0.0.0 ...

- `create_region_enable_voice` — set this variable to true if you want the create_region XmlRpc call to unconditionally enable voice on all parcels for a newly created region

- `create_region_public` — set this variable to false if you want the create_region XmlRpc call to create all regions as private per default (can be overridden in the XmlRpc call)

- `enabled_methods` — enable only those methods you deem to be appropriate using a | delimited whitelist. For example: enabled_methods = admin_broadcast|admin_save_oar|admin_save_xml

- `enabled` — Enables the wind module.

- `wind_update_rate` — How often should wind be updated, as a function of world frames. Approximately 50 frames a second

- `strength` — This setting is specific to the SimpleRandomWind plugin Adjusts wind strength. 0.0 = no wind, 1.0 = normal wind.

- `enable_materials` — This enables the use of Materials.

- `index_sims` — The following set of configs pertains to search. Set index_sims to true to enable search engines to index your searchable data. If false, no data will be exposed, DataSnapshot module will be off,

- `data_exposure` — The variable data_exposure controls what the regions expose: minimum: exposes only things explicitly marked for search all: exposes everything

- `gridname` — If search is on, change this to your grid name; will be ignored for standalones

- `default_snapshot_period` — Period between data snapshots, in seconds. 20 minutes, for starters, so that you see the initial changes fast. Later, you may want to increase this to 3600 (1 hour) or more

- `PriceUpload` — Money Unit fee to upload textures, animations etc.  Default is 0.

- `PriceGroupCreate` — Money Unit fee to create groups.  Default is 0.

- `ScriptDelayFactor` — Sets the multiplier for the scripting delays

- `ScriptDistanceLimitFactor` — The factor the 10 m distances limits are multiplied by

- `NotecardLineReadCharsMax` — Maximum length of notecard line read Increasing this to large values potentially opens up the system to malicious scripters

- `ScriptEnginesPath` — Path to script engine assemblies Default is ./bin/ScriptEngines

- `Include-osslDefaultEnable` — If this INI file is not included, the OSSL functions are disabled.

- `Enabled` — Enables the groups module

- `LevelGroupCreate` — Minimum user level required to create groups

- `Module` — The default module can use a PHP XmlRpc server from the Flotsam project at http://code.google.com/p/flotsam/

- `ServicesConnectorModule` — Service connectors to the Groups Service as used in the GroupsModule.  Select one as follows: -- for Flotsam Groups use XmlRpcGroupsServicesConnector -- for V2 Groups, standalone, non-HG use "Groups Local Service Connector" -- for V2 Groups, grided sim, non-HG

- `LocalService` — Used for V2 in HG only. If standalone, set this to local; if grided sim, set this to remote

- `SecretKey` — Used for V2 in Remote only.

- `GroupsServerURI` — URI for the groups services of this grid e.g. http://yourxmlrpcserver.com/xmlrpc.php for Flotsam XmlRpc or ${Const|PrivURL}:${Const|PrivatePort} for robust, V2 Leave it commented for standalones, V2

- `HomeURI` — http://mygridserver.com:9000 or http://mygridserver.com:8002 If you have this set in [Hypergrid] section of GridCommon.ini or StandaloneCommon.ini files in config-include folder, leave it commented

- `UpdatePrioritizationScheme` — Valid values are BestAvatarResponsiveness and SimpleAngularDistance SimpleAngularDistance does use more cpu

- `Enabled` — Enable media on a prim facilities

- `AllowNotOwned` — allow NPCs to be created not Owned {true false} default: true

- `AllowSenseAsAvatar` — allow NPCs to set to be sensed as Avatars {true false} default: true

- `AllowCloneOtherAvatars` — allow NPCs to created cloning any avatar in region {true false} default: true

- `NoNPCGroup` — if true NPCs will have no group title, if false display "- NPC -" for easy identification {true false} default: true

- `ProfileServiceURL` — Set the value of the url to your UserProfilesService If un-set / "" the module is disabled ProfileServiceURL = ${Const|BaseURL}:${Const|PublicPort}

- `AllowUserProfileWebURLs` — set this to false to prevent your users to be sent to unknown web sites by other users on their profiles

- `URL` — Sets the URL for the baked texture ROBUST service. Disabled when unset. URL = ${Const|PrivURL}:${Const|PrivatePort}

- `Include-Architecture` — Uncomment one of the following includes as required.  For instance, to create a standalone OpenSim, uncomment Include-Architecture = "config-include/Standalone.ini" Then you will need to copy and edit the corresponding *Common.example file in config-include/ t

OpenSim.ini.example: 114 documented options listed.

### Robust.ini.example

- `AllowedClients` — Bar (|) separated list of viewers which may gain access to the regions. One can use a substring of the viewer name to enable only certain versions Example: Agent uses the viewer "Imprudence 1.3.2.0"

- `DeniedClients` — Bar (|) separated list of viewers which may not gain access to the regions. One can use a Substring of the viewer name to disable only certain versions Example: Agent uses the viewer "Imprudence 1.3.2.0"

- `DSTZone` — Viewers do not receive timezone information from the server - almost all (?) default to Pacific Standard Time However, they do rely on the server to tell them whether it's Daylight Saving Time or not. Hence, calculating DST based on a different timezone can re

Robust.ini.example: 3 documented options listed.

## Asset garbage collection in practice

Because assets are immutable and referenced from inventory, regions, and scripts by UUID, safe deletion requires proving a negative: nothing anywhere references this UUID. Practical GC approaches used by grids: mark-and-sweep against a full scan of inventory items, region objects (from OARs or live region stores), and script byte-code references, run first in report-only mode for at least one full cycle; age-based candidate lists (assets created by temp uploads and never referenced within N days) reviewed before deletion; and du-style growth accounting per asset type so the operator knows whether growth is textures, meshes, or sounds before choosing a policy. Never GC against a database copy that excludes any region — an unloaded region's objects still reference assets, and deleting them corrupts that region on next load. Keep the deleted-UUID list forever: it is tiny, and it turns a future 'missing asset' mystery into a lookup.

## Mailing, messaging, and offline IM

Offline instant messages and group notices are stored by messaging services and delivered at login; on grids with web integration they may also forward to email. The operational traps are queue growth (offline IM storage for inactive accounts grows without bound unless retention is set), group notice fan-out cost on large groups, and the mute/block semantics differing between viewers when messages arrive via different paths. Set a retention policy, monitor the offline message table size as a first-class metric, and test delivery with the synthetic bot account receiving an offline IM while logged out.

## Land, estates, and permissions operations

Estates group regions under an estate owner and manager set with estate-wide controls (teleport restrictions, maturity, sun position, ban lists at estate scope). Operationally: keep estate ownership on a dedicated account, not a personal avatar; document manager grants; and remember region-level and estate-level bans interact — a user banned at estate scope is banned in every region of the estate, which is the point and also the accident that happens when an operator meant one region. Parcel operations that generate tickets: autoreturn settings eating builds (set and announce them deliberately), parcel media URL changes breaking streams, and deed-to-group mistakes that transfer build ownership to a group with no officers able to manage it. All three are policy-and-communication failures with config causes, and the runbook for each is restore-from-OAR plus fix the setting, in that order.

## Search, classifieds, and event listings operations

Search data comes from snapshot/index modules that crawl parcel, classified, and event data on an interval and serve queries from the snapshot. Operators should know their grid's snapshot interval, watch the indexing job's success as a metric (a silently dead indexer presents as 'search is broken' weeks later), and understand that classifieds are paid listings with expiry — the money and expiry logic lives with the currency/economy modules a grid chooses to run, which on most OpenSim grids means a third-party money module or none at all. A grid with no economy module should say so plainly in its registration flow rather than letting users discover dead Buy buttons in-world.

## Appendix B: every stock ;# option directive in OpenSim.ini.example

Parsed from the directive lines themselves: option name, the question the stock file asks for it, and its choices where given. This is the complete documented option surface of the main region configuration file.

- `BaseHostname` — BaseHostname Choices: "example.com" "127.0.0.1".

- `BaseURL` — BaseURL Choices: "http://${Const|BaseHostname".

- `PublicPort` — PublicPort Choices: 8002 9000.

- `PrivURL` — PrivURL Choices: "http://${Const|BaseURL.

- `PrivatePort` — PrivatePort Choices: 8003.

- `ConsolePrompt` — ConsolePrompt

- `ConsoleHistoryFileEnabled` — Save console commands to a history file? Choices: true false.

- `ConsoleHistoryFile` — Filename in which to save history

- `ConsoleHistoryFileLines` — How many lines of history to save?

- `ConsoleHistoryTimeStamp` — Time stamp commands in history file

- `save_crashes` — Save crashes to disk? Choices: true false.

- `crash_dir` — Directory to save crashes to?

- `PIDFile` — Path to PID file?

- `RegistryLocation` — Addins Registry Location

- `ConfigDirectory` — Set path to directory for modular ini files

- `region_info_source` — Where to load region from? Choices: filesystem web.

- `regionload_regionsdir` — Location of file?

- `regionload_webserver_url` — URL to load region from?

- `allow_regionless` — Allow simulator to start up with no regions configured. Choices: true false.

- `NonPhysicalPrimMin` — Minimum size of nonphysical prims?

- `NonPhysicalPrimMax` — Maximum size of nonphysical prims?

- `PhysicalPrimMin` — Minimum size of physical prims?

- `PhysicalPrimMax` — Maximum size of physical prims?

- `ClampPrimSize` — Clamp viewer rezzed prims to max sizes? Choices: true false.

- `LinksetPrims` — Max prims an object will hold?

- `AllowScriptCrossing` — Allow scripts to cross into this region Choices: true false.

- `TrustBinaries` — Accept compiled binary script code? (DANGEROUS!) Choices: true false.

- `InworldRestartShutsDown` — Shutdown instance on region restart? Choices: true false.

- `MinimumTimeBeforePersistenceConsidered` — Time before un-changed object may be persisted

- `MaximumTimeBeforePersistenceConsidered` — Time before changed objects may be persisted?

- `physical_prim` — Allow prims to be physical? Choices: true false.

- `meshing` — Select mesher Choices: Meshmerizer ZeroMesher.

- `physics` — Select physics engine Choices: OpenDynamicsEngine BulletSim basicphysics POS.

- `DefaultScriptEngine` — Default script engine Choices: YEngine.

- `HttpProxy` — Proxy URL for llHTTPRequest and dynamic texture loading

- `HttpProxyExceptions` — Set of regular expressions defining URL that should not be proxied

- `emailmodule` — Provide llEmail and llGetNextEmail functionality? (requires SMTP server) Choices: DefaultEmailModule.

- `SpawnPointRouting` — Set routing method for Telehub Spawnpoints Choices: closest random sequence.

- `TelehubAllowLandmark` — Allow users with landmarks to override telehub routing Choices: true false.

- `EnableCertConverter` — Enable pem to pkcs12 certificates converter Choices: true false.

- `PemCertPublicKey` — Set the path of the public key .pem

- `PemCertPrivateKey` — Set the path of the private key .pem

- `outputCertName` — Set the name of the resulting .p12 and .pfx

- `outputCertPassword` — Set the .p12 and .pfx password

- `EnableSelfsignedCertSupport` — Enable selfsigned certificate creation and renew Choices: true false.

- `CertRenewOnStartup` — renew the selfsigned certificate on the server startup Choices: true false.

- `CertFileName` — set the certificate file name

- `CertPassword` — set the certificate password

- `CertHostName` — set the certificate host name

- `CertHostIp` — set the certificate host IP

- `NoVerifyCertChain` — do not verify SSL Cert Chain Choices: true false.

- `NoVerifyCertHostname` — do not verify SSL Cert name versus peer name Choices: true false.

- `AllowedClients` — Bar (|) separated list of allowed clients

- `DeniedClients` — Bar (|) separated list of denied clients

- `GenerateMaptiles` — Generate map tiles? Choices: true false.

- `MapImageModule` — The map image module to use Choices: MapImageModule Warp3DImageModule.

- `MaptileRefresh` — Maptile refresh period?

- `MaptileStaticUUID` — Asset ID for static map texture

- `TextureOnMapTile` — Use terrain textures for map tiles? Choices: true false.

- `DrawPrimOnMapTile` — Draw prim shapes on map tiles? Choices: true false.

- `TexturePrims` — Texture prims on map tiles? Choices: true false.

- `TexturePrimSize` — Size of prims to texture faces?

- `RenderMeshes` — Render meshes and sculpties on map tiles? Choices: true false.

- `MapColorWater` — Water color for textured and shaded maps Choices: "#1D475F".

- `MapColor1` — Terrain color 1 for textured maps Choices: "#A58976".

- `MapColor2` — Terrain color 2 for textured maps Choices: "#455931".

- `MapColor3` — Terrain color 3 for textured maps Choices: "#A29A8D".

- `MapColor4` — Terrain color 4 for textured maps Choices: "#C8C8C8".

- `permissionmodules` — Permission modules to use (may specify multiple modules, separated by comma

- `serverside_object_permissions` — Activate permission handling by the sim? Choices: true false.

- `allow_grid_gods` — Allow grid gods? Choices: true false.

- `region_owner_is_god` — Allow region owner gods Choices: true false.

- `region_manager_is_god` — Allow region manager gods Choices: true false.

- `simple_build_permissions` — Allow building in parcel by access list (no groups) Choices: true false.

- `DefaultEstateName` — Default name for estate?

- `DefaultEstateOwnerName` — Default estate owner name?

- `DefaultEstateOwnerUUID` — Default estate owner UUID?

- `DefaultEstateOwnerEMail` — Default estate owner email?

- `DefaultEstateOwnerPassword` — Default estate owner password

- `enabled` — Enable module? Choices: true false.

- `enabled` — Enable send to objects to regions not on instance? Choices: true false.

- `enabled` — maximum number of emails from a object owner per hour

- `enabled` — maximum number of emails to a prim address per hour

- `enabled` — maximum number of emails via smtp per day

- `enabled` — maximum number of emails to a SMTP address per hour

- `enabled` — Enable send to the world? Choices: true false.

- `internal_object_host` — Host name to treat as internal (object to object) email?

- `host_domain_header_from` — From address to use in the sent email header?

- `SMTP_SERVER_FROM` — SMTP server from name?

- `email_pause_time` — Period in seconds to delay after an email is sent.

- `email_max_size` — Maximum total size of email in bytes.

- `SMTP_SERVER_TLS` — SMTP use TLS?

- `SMTP_SERVER_HOSTNAME` — SMTP server name?

- `SMTP_SERVER_PORT` — SMTP server name? Choices: SMTP server port?.

- `SMTP_SERVER_LOGIN` — SMTP server user name?

- `SMTP_SERVER_PASSWORD` — SMTP server password

- `SMTP_VerifyCertChain` — SMTP Verify cert chain option

- `SMTP_VerifyCertNames` — SMTP Verify cert chain option

- `ConsoleUser` — User name for console account

- `ConsolePass` — Password for console account

- `console_port` — Port for console connections

- `http_listener_port` — TCP Port for this simulator to listen on? (This must be unique to the simulator!)

- `http_listener_ssl` — enable main server ssl port

- `http_listener_sslport` — main server ssl port

- `http_listener_cn` — main server ssl externalHostName

- `http_listener_cert_path` — main server ssl certificate file path

- `http_listener_cert_pass` — main server ssl certificate password

- `HttpBodyMaxLenMAX` — Maximum bytes allowed for HTTP_BODY_MAXLENGTH

- `ExternalHostNameForLSL` — Hostname to use for HTTP-IN URLs. This should be reachable from the internet.

- `shard` — Name to use for X-Secondlife-Shard header? (press enter if unsure)

- `user_agent` — User agent to report to web servers?

- `XmlRpcRouterModule` — Module used to route incoming llRemoteData calls Choices: XmlRpcRouterModule XmlRpcGridRouterModule.

- `XmlRpcPort` — Port for incoming llRemoteData xmlrpc calls

- `XmlRpcHubURI` — URI for external service used to register xmlrpc channels created in the simulator. This depends on XmlRpcRouterModule being set to XmlRpcGridRouterModule

- `DisableFacelights` — Stop facelights from working? Choices: true false.

- `SearchServerURI` — URL of the search server

- `DestinationGuideURI` — URL of the destination guide

- `whisper_distance` — Distance at which a whisper is heard, in meters?

- `say_distance` — Distance at which normal chat is heard, in meters?

- `shout_distance` — Distance at which a shout is heard, in meters?

- `DisableInterRegionTeleportCancellation` — Determine whether the cancel button is shown at all during teleports. Choices: false true.

- `LandingPointBehavior` — How to honor landing points and telehubs for gods. Choices: LandingPointBehavior_OS LandingPointBehavior_SL.

- `OfflineMessageModule` — Module to use for offline message storage Choices: OfflineMessageModule "Offline Message Module V2" *.

- `OfflineMessageURL` — URL of offline messaging service

- `StorageProvider` — DLL that provides the storage interface Choices: OpenSim.Data.MySQL.dll.

- `AvatarToAvatarCollisionsByDefault` — Should avatars collide with each other? Choices: true false.

- `enabled` — Enable the remote admin interface? Choices: true false.

- `port` — Port to use for the remote admin interface? (0 = default)

- `access_password` — Password for the remote admin interface

- `access_ip_addresses` — List the IP addresses allowed to call RemoteAdmin?

- `create_region_enable_voice` — Enable voice for newly created regions? Choices: true false.

- `create_region_public` — Make newly created regions public? Choices: true false.

- `enabled_methods` — List of methods to allow, separated by |

- `enabled` — Enable wind module? Choices: true false.

- `wind_update_rate` — Wind update rate in frames?

- `strength` — Wind strength?

- `enable_materials` — Enable Materials support? Choices: true false.

- `index_sims` — Enable data snapshotting (search)? Choices: true false.

- `data_exposure` — How much data should be exposed? Choices: minimum all.

- `gridname` — Enter the name fo your grid

- `default_snapshot_period` — Period between data snapshots?

- `data_services` — Data service URLs to register with?

- `SellEnabled` — Enable selling for 0? Choices: true false.

- `PriceUpload` — Price for uploading?

- `PriceGroupCreate` — Fee for group creation

- `Enabled` — Enable the YEngine scripting engine? Choices: true false.

- `ScriptDelayFactor` — Multiplier for scripting delays

- `ScriptDistanceLimitFactor` — Multiplier for 10.0m distance limits?

- `NotecardLineReadCharsMax` — Maximum length of notecard line?

- `SensorMaxRange` — Sensor range

- `SensorMaxResults` — Max sensor results returned?

- `ScriptEnginesPath` — Path to script assemblies

- `Include-osslDefaultEnable` — Include file for enabling and permissions for OSSL functions

- `Enabled` — Enable groups? Choices: true false.

- `LevelGroupCreate` — User level for creating groups

- `Module` — Groups module to use? (Use GroupsModule to use Flotsam) Choices: Default "Groups Module V2".

- `StorageProvider` — The DLL that provides the storage for V2 Choices: OpenSim.Data.MySQL.dll.

- `ServicesConnectorModule` — Service connector to use for groups Choices: XmlRpcGroupsServicesConnector "Groups Local Service Connector" "Groups Remote Service Connector" "Groups HG Service Connector".

- `LocalService` — Is the group service in this process or elsewhere? Choices: local remote.

- `SecretKey` — Secret key between sim and remote group service

- `GroupsServerURI` — Groups Server URI

- `HomeURI` — What's the home address of this world?

- `MessagingEnabled` — Is groups messaging enabled? Choices: true false.

- `MessagingModule` — Module to use for groups messaging Choices: GroupsMessagingModule "Groups Messaging Module V2".

- `NoticesEnabled` — Enable group notices? Choices: true false.

- `MessageOnlineUsersOnly` — Message online users only? Choices: true false.

- `UpdatePrioritizationScheme` — Update prioritization scheme? Choices: BestAvatarResponsiveness SimpleAngularDistance.

- `Enabled` — Enable Media-on-a-Prim (MOAP) Choices: true false.

- `Enabled` — Enable Non Player Character (NPC) facilities Choices: true false.

- `AllowNotOwned` — allow NPCs to be created not Owned Choices: true false.

- `AllowSenseAsAvatar` — allow NPCs to set to be sensed as Avatars Choices: true false.

- `AllowCloneOtherAvatars` — allow NPCs to created cloning any avatar in region Choices: true false.

- `NoNPCGroup` — if true NPCs will have no group title, if false display "- NPC -" Choices: true false.

- `InitialTerrain` — Initial terrain type Choices: pinhead-island flat.

- `ProfileServiceURL` — Set url to UserProfilesService

- `AllowUserProfileWebURLs` — allow user profiles web urls Choices: true false.

- `URL` — Set URL for Baked texture service

- `Include-Architecture` — Choose one of the following architectures Choices: config-include/Standalone.ini config-include/StandaloneHypergrid.ini config-include/Grid.ini config-include/GridHypergrid.ini.

Appendix B entries: 178.

## Appendix C: Robust.ini.example service sections and connectors

Robust is configured as a list of service connectors per section. The sections and connector assignments below are the stock example's map of which service runs where — the starting point for splitting services across instances and ports.

### Robust section [Const]

- `BaseHostname` = "127.0.0.1"

- `BaseURL` = "http://${Const|BaseHostname}"

- `PublicPort` = "8002"

- `PrivatePort` = "8003"

### Robust section [Startup]

- `RegistryLocation` = "."

- `ConfigDirectory` = "robust-include"

- `ConsoleHistoryFileEnabled` = true

- `ConsoleHistoryFile` = "RobustConsoleHistory.txt"

- `ConsoleHistoryFileLines` = 100

- `EnableRobustSelfsignedCertSupport` = false

- `RobustCertRenewOnStartup` = false

- `RobustCertFileName` = "Robust"

- `RobustCertPassword` = "mycertpass"

- `RobustCertHostName` = ${Const|BaseHostname}

- `RobustCertHostIp` = "127.0.0.1"

- `NoVerifyCertChain` = true

- `NoVerifyCertHostname` = true

### Robust section [ServiceList]

- `AssetServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:AssetServiceConnector"

- `InventoryInConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:XInventoryInConnector"

- `GridServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:GridServiceConnector"

- `GridInfoServerInConnector` = "${Const|PublicPort}/OpenSim.Server.Handlers.dll:GridInfoServerInConnector"

- `AuthenticationServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:AuthenticationServiceConnector"

- `AvatarServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:AvatarServiceConnector"

- `LLLoginServiceInConnector` = "${Const|PublicPort}/OpenSim.Server.Handlers.dll:LLLoginServiceInConnector"

- `PresenceServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:PresenceServiceConnector"

- `UserAccountServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:UserAccountServiceConnector"

- `GridUserServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:GridUserServiceConnector"

- `AgentPreferencesServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:AgentPreferencesServiceConnector"

- `FriendsServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:FriendsServiceConnector"

- `MapAddServiceConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:MapAddServiceConnector"

- `MapGetServiceConnector` = "${Const|PublicPort}/OpenSim.Server.Handlers.dll:MapGetServiceConnector"

- `MuteListConnector` = "${Const|PrivatePort}/OpenSim.Server.Handlers.dll:MuteListServiceConnector"

### Robust section [Network]

- `port` = ${Const|PrivatePort}

- `AllowllHTTPRequestIn` = false

### Robust section [AccessControl]

### Robust section [DatabaseService]

- `StorageProvider` = "OpenSim.Data.MySQL.dll"

- `ConnectionString` = "Data Source=localhost;Database=opensim;User ID=opensim;Password=*****;Old Guids=true;SslMode=None;"

### Robust section [AssetService]

- `LocalServiceModule` = "OpenSim.Services.AssetService.dll:AssetService"

- `DefaultAssetLoader` = "OpenSim.Framework.AssetLoader.Filesystem.dll"

- `AssetLoaderArgs` = "./assets/AssetSets.xml"

- `AllowRemoteDelete` = false

- `AllowRemoteDeleteAllTypes` = false

### Robust section [InventoryService]

- `LocalServiceModule` = "OpenSim.Services.InventoryService.dll:XInventoryService"

- `AllowDelete` = true

### Robust section [GridService]

- `LocalServiceModule` = "OpenSim.Services.GridService.dll:GridService"

- `ExportSupported` = true

### Robust section [FreeswitchService]

- `LocalServiceModule` = "OpenSim.Services.FreeswitchService.dll:FreeswitchService"

### Robust section [AuthenticationService]

- `LocalServiceModule` = "OpenSim.Services.AuthenticationService.dll:PasswordAuthenticationService"

### Robust section [OpenIdService]

- `AuthenticationServiceModule` = "OpenSim.Services.AuthenticationService.dll:PasswordAuthenticationService"

- `UserAccountServiceModule` = "OpenSim.Services.UserAccountService.dll:UserAccountService"

### Robust section [UserAccountService]

- `LocalServiceModule` = "OpenSim.Services.UserAccountService.dll:UserAccountService"

- `AuthenticationService` = "OpenSim.Services.AuthenticationService.dll:PasswordAuthenticationService"

- `PresenceService` = "OpenSim.Services.PresenceService.dll:PresenceService"

- `GridService` = "OpenSim.Services.GridService.dll:GridService"

- `InventoryService` = "OpenSim.Services.InventoryService.dll:XInventoryService"

- `AvatarService` = "OpenSim.Services.AvatarService.dll:AvatarService"

- `GridUserService` = "OpenSim.Services.UserAccountService.dll:GridUserService"

- `CreateDefaultAvatarEntries` = true

### Robust section [GridUserService]

- `LocalServiceModule` = "OpenSim.Services.UserAccountService.dll:GridUserService"

### Robust section [AgentPreferencesService]

- `LocalServiceModule` = "OpenSim.Services.UserAccountService.dll:AgentPreferencesService"

### Robust section [PresenceService]

- `LocalServiceModule` = "OpenSim.Services.PresenceService.dll:PresenceService"

### Robust section [AvatarService]

- `LocalServiceModule` = "OpenSim.Services.AvatarService.dll:AvatarService"

### Robust section [FriendsService]

- `LocalServiceModule` = "OpenSim.Services.FriendsService.dll:FriendsService"

### Robust section [EstateService]

- `LocalServiceModule` = "OpenSim.Services.EstateService.dll:EstateDataService"

### Robust section [LibraryService]

- `LibraryName` = "OpenSim Library"

- `DefaultLibrary` = "./inventory/Libraries.xml"

### Robust section [LoginService]

- `LocalServiceModule` = "OpenSim.Services.LLLoginService.dll:LLLoginService"

- `UserAccountService` = "OpenSim.Services.UserAccountService.dll:UserAccountService"

- `GridUserService` = "OpenSim.Services.UserAccountService.dll:GridUserService"

- `AuthenticationService` = "OpenSim.Services.AuthenticationService.dll:PasswordAuthenticationService"

- `InventoryService` = "OpenSim.Services.InventoryService.dll:XInventoryService"

- `AvatarService` = "OpenSim.Services.AvatarService.dll:AvatarService"

- `PresenceService` = "OpenSim.Services.PresenceService.dll:PresenceService"

- `GridService` = "OpenSim.Services.GridService.dll:GridService"

- `SimulationService` = "OpenSim.Services.Connectors.dll:SimulationServiceConnector"

- `LibraryService` = "OpenSim.Services.InventoryService.dll:LibraryService"

- `FriendsService` = "OpenSim.Services.FriendsService.dll:FriendsService"

- `WelcomeMessage` = "Welcome, Avatar!"

- `AllowRemoteSetLoginLevel` = "false"

- `MapTileURL` = "${Const|BaseURL}:${Const|PublicPort}/map/";

- `DSTZone` = "America/Los_Angeles;Pacific Standard Time"

- `AllowLoginFallbackToAnyRegion` = false

### Robust section [MapImageService]

- `LocalServiceModule` = "OpenSim.Services.MapImageService.dll:MapImageService"

### Robust section [GridInfoService]

- `login` = ${Const|BaseURL}:${Const|PublicPort}/

- `gridname` = "the lost continent of hippo"

- `gridnick` = "hippogrid"

### Robust section [Messaging]

- `OfflineIMService` = "OpenSim.Addons.OfflineIM.dll:OfflineIMService"

### Robust section [Groups]

### Robust section [UserProfilesService]

- `LocalServiceModule` = "OpenSim.Services.UserProfilesService.dll:UserProfilesService"

- `Enabled` = false

- `UserAccountService` = OpenSim.Services.UserAccountService.dll:UserAccountService

- `AuthenticationServiceModule` = "OpenSim.Services.AuthenticationService.dll:PasswordAuthenticationService"

### Robust section [BakedTextureService]

- `LocalServiceModule` = "OpenSim.Server.Handlers.dll:XBakes"

- `BaseDirectory` = "./bakes"

### Robust section [MuteListService]

- `LocalServiceModule` = "OpenSim.Services.MuteListService.dll:MuteListService"

Appendix C entries: 93 connector assignments.

## Appendix D: OSSL function surface (IOSSL_Api) — what your threat-level policy governs

Method signatures extracted from OpenSim's IOSSL_Api.cs in the opensim source tree. Every function here is an os* capability that does not exist in Second Life and is gated by threat level and osslEnable.ini on your grid. Enabling the engine defaults without reading this list is how grids hand out teleport, NPC, and dynamic-texture powers unintentionally.

- `void CheckThreatLevel(ThreatLevel level, string function)`

- `string osSetDynamicTextureURL(string dynamicID, string contentType, string url, string extraParams, int timer)`

- `string osSetDynamicTextureURLBlend(string dynamicID, string contentType, string url, string extraParams, int timer, int alpha)`

- `string osSetDynamicTextureURLBlendFace(string dynamicID, string contentType, string url, string extraParams, bool blend, int disp, int timer, int alpha, int face)`

- `string osSetDynamicTextureData(string dynamicID, string contentType, string data, string extraParams, int timer)`

- `string osSetDynamicTextureDataFace(string dynamicID, string contentType, string data, string extraParams, int timer, int face)`

- `string osSetDynamicTextureDataBlend(string dynamicID, string contentType, string data, string extraParams, int timer, int alpha)`

- `string osSetDynamicTextureDataBlendFace(string dynamicID, string contentType, string data, string extraParams, bool blend, int disp, int timer, int alpha, int face)`

- `LSL_Float osGetTerrainHeight(int x, int y)`

- `LSL_Float osTerrainGetHeight(int x, int y)`

- `LSL_Integer osSetTerrainHeight(int x, int y, double val)`

- `LSL_Integer osTerrainSetHeight(int x, int y, double val)`

- `void osTerrainFlush()`

- `int osRegionRestart(double seconds)`

- `int osRegionRestart(double seconds, string msg)`

- `void osRegionNotice(string msg)`

- `void osRegionNotice(LSL_Key agentID, string msg)`

- `bool osConsoleCommand(string Command)`

- `void osSetParcelMusicURL(LSL_String url)`

- `void osSetParcelMediaURL(LSL_String url)`

- `void osSetPrimFloatOnWater(int floatYN)`

- `void osSetParcelSIPAddress(string SIPAddress)`

- `LSL_List osGetAgents()`

- `string osGetAgentIP(string agent)`

- `void osLocalTeleportAgent(LSL_Key agent, LSL_Types.Vector3 position, LSL_Types.Vector3 velocity, LSL_Types.Vector3 lookat, LSL_Integer flags)`

- `void osTeleportAgent(string agent, string regionName, LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osTeleportAgent(string agent, int regionX, int regionY, LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osTeleportAgent(string agent, LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osTeleportOwner(string regionName, LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osTeleportOwner(int regionX, int regionY, LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osTeleportOwner(LSL_Types.Vector3 position, LSL_Types.Vector3 lookat)`

- `void osAvatarPlayAnimation(LSL_Key avatarId, string animation)`

- `void osAvatarStopAnimation(LSL_Key avatarId, string animation)`

- `void osForceAttachToAvatar(int attachment)`

- `void osForceAttachToAvatarFromInventory(string itemName, int attachment)`

- `void osForceAttachToOtherAvatarFromInventory(string rawAvatarId, string itemName, int attachmentPoint)`

- `void osForceDetachFromAvatar()`

- `LSL_List osGetNumberOfAttachments(LSL_Key avatar, LSL_List attachmentPoints)`

- `void osMessageAttachments(LSL_Key avatar, string message, LSL_List attachmentPoints, int flags)`

- `string osMovePen(string drawList, int x, int y)`

- `string osDrawLine(string drawList, int startX, int startY, int endX, int endY)`

- `string osDrawLine(string drawList, int endX, int endY)`

- `string osDrawText(string drawList, string text)`

- `string osDrawEllipse(string drawList, int width, int height)`

- `string osDrawFilledEllipse(string drawList, int width, int height)`

- `string osDrawRectangle(string drawList, int width, int height)`

- `string osDrawFilledRectangle(string drawList, int width, int height)`

- `string osDrawPolygon(string drawList, LSL_List x, LSL_List y)`

- `string osDrawFilledPolygon(string drawList, LSL_List x, LSL_List y)`

- `string osDrawResetTransform(string drawList)`

- `string osDrawRotationTransform(string drawList, LSL_Float x)`

- `string osDrawScaleTransform(string drawList, LSL_Float x, LSL_Float y)`

- `string osDrawTranslationTransform(string drawList, LSL_Float x, LSL_Float y)`

- `string osSetFontName(string drawList, string fontName)`

- `string osSetFontSize(string drawList, int fontSize)`

- `string osSetPenSize(string drawList, int penSize)`

- `string osSetPenColor(string drawList, string color)`

- `string osSetPenColor(string drawList, LSL_Types.Vector3 color)`

- `string osSetPenColor(string drawList, LSL_Types.Vector3 color, LSL_Float alpha)`

- `string osSetPenColour(string drawList, string colour)`

- `string osSetPenCap(string drawList, string direction, string type)`

- `string osDrawImage(string drawList, int width, int height, string image)`

- `vector osGetDrawStringSize(string contentType, string text, string fontName, int fontSize)`

- `void osSetRegionWaterHeight(double height)`

- `void osSetRegionSunSettings(bool useEstateSun, bool sunFixed, double sunHour)`

- `void osSetEstateSunSettings(bool sunFixed, double sunHour)`

- `LSL_Float osGetCurrentSunHour()`

- `LSL_Float osGetSunParam(LSL_String param)`

- `void osSetSunParam(string param, double value)`

- `void osSunSetParam(string param, double value)`

- `string osWindActiveModelPluginName()`

- `void osSetWindParam(string plugin, string param, LSL_Float value)`

- `LSL_Float osGetWindParam(string plugin, string param)`

- `LSL_Integer osGetParcelDwell(vector pos)`

- `void osParcelJoin(vector pos1, vector pos2)`

- `void osParcelSubdivide(vector pos1, vector pos2)`

- `void osSetParcelDetails(vector pos, LSL_List rules)`

- `void osParcelSetDetails(vector pos, LSL_List rules)`

- `string osGetScriptEngineName()`

- `string osGetSimulatorVersion()`

- `LSL_Integer osCheckODE()`

- `string osGetPhysicsEngineType()`

- `string osGetPhysicsEngineName()`

- `void osMessageObject(key objectUUID, string message)`

- `void osMakeNotecard(string notecardName, LSL_String contents)`

- `void osMakeNotecard(string notecardName, LSL_List contents)`

- `string osGetNotecardLine(string name, int line)`

- `string osGetNotecard(string name)`

- `int osGetNumberOfNotecardLines(string name)`

- `string osAvatarName2Key(string firstname, string lastname)`

- `string osKey2Name(string id)`

- `string osSHA256(string input)`

- `string osGetGridNick()`

- `string osGetGridName()`

- `string osGetGridLoginURI()`

- `string osGetGridHomeURI()`

- `string osGetGridGatekeeperURI()`

- `string osGetGridCustom(string key)`

- `string osGetAvatarHomeURI(string uuid)`

- `LSL_String osFormatString(string str, LSL_List strings)`

- `LSL_List osMatchString(string src, string pattern, int start)`

- `LSL_String osReplaceString(string src, string pattern, string replace, int count, int start)`

- `string osLoadedCreationDate()`

- `string osLoadedCreationTime()`

- `string osLoadedCreationID()`

- `LSL_List osGetLinkPrimitiveParams(int linknumber, LSL_List rules)`

- `void osForceCreateLink(string target, int parent)`

- `void osForceBreakLink(int linknum)`

- `void osForceBreakAllLinks()`

- `void osDie(LSL_Key objectUUID)`

- `LSL_Integer osIsNpc(LSL_Key npc)`

- `key osNpcCreate(string user, string name, vector position, string notecard)`

- `key osNpcCreate(string user, string name, vector position, string notecard, int options)`

- `LSL_Key osNpcSaveAppearance(key npc, LSL_String notecard)`

- `LSL_Key osNpcSaveAppearance(key npc, LSL_String notecard, LSL_Integer includeHuds)`

- `void osNpcLoadAppearance(key npc, string notecard)`

- `vector osNpcGetPos(key npc)`

- `void osNpcMoveTo(key npc, vector position)`

- `void osNpcMoveToTarget(key npc, vector target, int options)`

- `LSL_Key osNpcGetOwner(key npc)`

- `rotation osNpcGetRot(key npc)`

- `void osNpcSetRot(LSL_Key npc, rotation rot)`

- `void osNpcStopMoveToTarget(LSL_Key npc)`

- `void osNpcSetProfileAbout(LSL_Key npc, string about)`

- `void osNpcSetProfileImage(LSL_Key npc, string image)`

- `void osNpcSay(key npc, string message)`

- `void osNpcSay(key npc, int channel, string message)`

- `void osNpcSayTo(LSL_Key npc, LSL_Key target, int channel, string msg)`

- `void osNpcShout(key npc, int channel, string message)`

- `void osNpcSit(key npc, key target, int options)`

- `void osNpcStand(LSL_Key npc)`

- `void osNpcRemove(key npc)`

- `void osNpcPlayAnimation(LSL_Key npc, string animation)`

- `void osNpcStopAnimation(LSL_Key npc, string animation)`

- `void osNpcTouch(LSL_Key npcLSL_Key, LSL_Key object_key, LSL_Integer link_num)`

- `void osNpcWhisper(key npc, int channel, string message)`

- `LSL_Key osOwnerSaveAppearance(LSL_String notecard)`

- `LSL_Key osOwnerSaveAppearance(LSL_String notecard, LSL_Integer includeHuds)`

- `LSL_Key osAgentSaveAppearance(key agentId, LSL_String notecard)`

- `LSL_Key osAgentSaveAppearance(key agentId, LSL_String notecard, LSL_Integer includeHuds)`

- `LSL_String osGetGender(LSL_Key rawAvatarId)`

- `LSL_Key osGetMapTexture()`

- `LSL_Key osGetRegionMapTexture(string regionNameOrID)`

- `LSL_List osGetRegionStats()`

- `vector osGetRegionSize()`

- `int osGetSimulatorMemory()`

- `int osGetSimulatorMemoryKB()`

- `void osKickAvatar(string FirstName, string SurName, string alert)`

- `void osKickAvatar(LSL_Key agentId, string alert)`

- `void osSetSpeed(string UUID, LSL_Float SpeedModifier)`

- `void osSetOwnerSpeed(LSL_Float SpeedModifier)`

- `LSL_Float osGetHealth(key agentId)`

- `void osCauseHealing(key agentId, LSL_Float healing)`

- `void osSetHealth(key agentId, LSL_Float health)`

- `void osSetHealRate(key agentId, LSL_Float health)`

- `LSL_Float osGetHealRate(key agentId)`

- `void osCauseDamage(key avatar, LSL_Float damage)`

- `void osForceOtherSit(string avatar)`

- `void osForceOtherSit(string avatar, string target)`

- `LSL_List osGetPrimitiveParams(LSL_Key prim, LSL_List rules)`

- `void osSetPrimitiveParams(LSL_Key prim, LSL_List rules)`

- `void osSetProjectionParams(LSL_Integer projection, LSL_Key texture, LSL_Float fov, LSL_Float focus, LSL_Float amb)`

- `void osSetProjectionParams(LSL_Key prim, LSL_Integer projection, LSL_Key texture, LSL_Float fov, LSL_Float focus, LSL_Float amb)`

- `void osSetProjectionParams(LSL_Integer linknumber, LSL_Integer projection, LSL_Key texture, LSL_Float fov, LSL_Float focus, LSL_Float amb)`

- `LSL_List osGetAvatarList()`

- `LSL_List osGetNPCList()`

- `LSL_String osUnixTimeToTimestamp(LSL_Integer time)`

- `LSL_Integer osInviteToGroup(LSL_Key agentId)`

- `LSL_Integer osEjectFromGroup(LSL_Key agentId)`

- `void osSetTerrainTexture(int level, LSL_Key texture)`

- `void osSetTerrainTextures(LSL_List textures, LSL_Integer types)`

- `void osSetTerrainTextureHeight(int corner, double low, double high)`

- `LSL_Integer osIsUUID(string thing)`

- `LSL_Float osMin(double a, double b)`

- `LSL_Float osMax(double a, double b)`

- `LSL_Key osGetRezzingObject()`

- `void osSetContentType(LSL_Key id, string type)`

- `void osDropAttachment()`

- `void osForceDropAttachment()`

- `void osDropAttachmentAt(vector pos, rotation rot)`

- `void osForceDropAttachmentAt(vector pos, rotation rot)`

- `LSL_Integer osListenRegex(int channelID, string name, string ID, string msg, int regexBitfield)`

- `LSL_Integer osRegexIsMatch(string input, string pattern)`

- `LSL_Key osRequestURL(LSL_List options)`

- `LSL_Key osRequestSecureURL(LSL_List options)`

- `void osCollisionSound(string impact_sound, double impact_volume)`

- `void osVolumeDetect(int detect)`

- `LSL_List osGetInertiaData()`

- `void osClearInertia()`

- `void osSetInertia(LSL_Float mass, vector centerOfMass, vector principalInertiaScaled, rotation rot)`

- `void osSetInertiaAsBox(LSL_Float mass, vector boxSize, vector centerOfMass, rotation rot)`

- `void osSetInertiaAsSphere(LSL_Float mass, LSL_Float radius, vector centerOfMass)`

- `void osSetInertiaAsCylinder(LSL_Float mass, LSL_Float radius, LSL_Float length, vector centerOfMass,rotation lslrot)`

- `LSL_Integer osTeleportObject(LSL_Key objectUUID, vector targetPos, rotation targetrotation, LSL_Integer flags)`

- `LSL_Integer osGetLinkNumber(LSL_String name)`

- `LSL_Float osRound(LSL_Float value, LSL_Integer digits)`

- `LSL_Float osVecMagSquare(vector a)`

- `LSL_Float osVecDistSquare(vector a, vector b)`

- `LSL_Float osAngleBetween(vector a, vector b)`

- `void osAdjustSoundVolume(LSL_Integer linknum, LSL_Float volume)`

- `void osLoopSound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osLoopSoundMaster(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osLoopSoundSlave(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osPlaySound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osPlaySoundSlave(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osPreloadSound(LSL_Integer linknum, LSL_String sound)`

- `void osSetSoundRadius(LSL_Integer linknum, LSL_Float radius)`

- `void osStopSound(LSL_Integer linknum)`

- `void osTriggerSound(LSL_Integer linknum, LSL_String sound, LSL_Float volume)`

- `void osTriggerSoundLimited(LSL_Integer linknum, LSL_String sound, LSL_Float volume, vector top_north_east, vector bottom_south_west)`

- `LSL_String osDetectedCountry(LSL_Integer number)`

- `LSL_String osGetAgentCountry(LSL_Key agentId)`

- `LSL_String osStringSubString(LSL_String src, LSL_Integer start)`

- `LSL_String osStringSubString(LSL_String src, LSL_Integer start, LSL_Integer length)`

- `LSL_Integer osStringStartsWith(LSL_String src, LSL_String value, LSL_Integer ignorecase)`

- `LSL_Integer osStringEndsWith(LSL_String src, LSL_String value, LSL_Integer ignorecase)`

- `LSL_Integer osStringIndexOf(LSL_String src, LSL_String value, LSL_Integer ignorecase)`

- `LSL_Integer osStringIndexOf(LSL_String src, LSL_String value, LSL_Integer start, LSL_Integer count, LSL_Integer ignorecase)`

- `LSL_Integer osStringLastIndexOf(LSL_String src, LSL_String value, LSL_Integer ignorecase)`

- `LSL_Integer osStringLastIndexOf(LSL_String src, LSL_String value, LSL_Integer start, LSL_Integer count, LSL_Integer ignorecase)`

- `LSL_String osStringRemove(LSL_String src, LSL_Integer start, LSL_Integer count)`

- `LSL_String osStringReplace(LSL_String src, LSL_String oldvalue, LSL_String newvalue)`

- `LSL_Integer osApproxEquals(LSL_Float a, LSL_Float b)`

- `LSL_Integer osApproxEquals(LSL_Float a, LSL_Float b, LSL_Float margin)`

- `LSL_Integer osApproxEquals(vector va, vector vb)`

- `LSL_Integer osApproxEquals(vector va, vector vb, LSL_Float margin)`

- `LSL_Integer osApproxEquals(rotation ra, rotation rb)`

- `LSL_Integer osApproxEquals(rotation ra, rotation rb, LSL_Float margin)`

- `LSL_Key osGetInventoryLastOwner(LSL_String itemNameOrId)`

- `LSL_Key osGetInventoryItemKey(LSL_String name)`

- `LSL_Key osGetLinkInventoryKey(LSL_Integer linkNumber, LSL_String name, LSL_Integer type)`

- `LSL_List osGetLinkInventoryKeys(LSL_Integer linkNumber, LSL_Integer type)`

- `LSL_Key osGetLinkInventoryItemKey(LSL_Integer linkNumber, LSL_String name)`

- `LSL_String osGetInventoryName(LSL_Key itemId)`

- `LSL_String osGetLinkInventoryName(LSL_Integer linkNumber, LSL_Key itemId)`

- `LSL_String osGetInventoryDesc(LSL_String itemNameOrId)`

- `LSL_String osGetLinkInventoryDesc(LSL_Integer linkNumber, LSL_String itemNameorid)`

- `LSL_List osGetInventoryItemKeys(LSL_Integer type)`

- `LSL_List osGetLinkInventoryItemKeys(LSL_Integer linkNumber, LSL_Integer type)`

- `LSL_List osGetInventoryNames(LSL_Integer type)`

- `LSL_List osGetLinkInventoryNames(LSL_Integer linkNumber, LSL_Integer type)`

- `void osRemoveLinkInventory(LSL_Integer linkNumber, LSL_String name)`

- `void osGiveLinkInventory(LSL_Integer linkNumber, LSL_Key destination, LSL_String inventory)`

- `void osGiveLinkInventoryList(LSL_Integer linkNumber, LSL_Key destination, LSL_String folderName, LSL_List inventory)`

- `LSL_Key osGetLastChangedEventKey()`

- `LSL_Float osGetPSTWallclock()`

- `vector osSlerp(vector a, vector b, LSL_Float amount)`

- `void osResetAllScripts(LSL_Integer AllLinkset)`

- `LSL_Integer osIsNotValidNumber(LSL_Float v)`

- `void osSetSitActiveRange(LSL_Float v)`

- `void osSetLinkSitActiveRange(LSL_Integer linkNumber, LSL_Float v)`

- `LSL_Float osGetSitActiveRange()`

- `LSL_Float osGetLinkSitActiveRange(LSL_Integer linkNumber)`

- `vector osGetSitTargetPos()`

- `rotation osGetSitTargetRot()`

- `void osSetStandTarget(vector v)`

- `void osSetLinkStandTarget(LSL_Integer linkNumber, vector v)`

- `vector osGetStandTarget()`

- `vector osGetLinkStandTarget(LSL_Integer linkNumber)`

- `LSL_Integer osClearObjectAnimations()`

- `LSL_Float osGetApparentTime()`

- `LSL_String osGetApparentTimeString(LSL_Integer format24)`

- `LSL_Float osGetApparentRegionTime()`

- `LSL_String osGetApparentRegionTimeString(LSL_Integer format24)`

- `LSL_Integer osReplaceAgentEnvironment(LSL_Key agentkey, LSL_Integer transition, LSL_String daycycle)`

- `LSL_Integer osReplaceParcelEnvironment(LSL_Integer transition, LSL_String daycycle)`

- `LSL_Integer osReplaceRegionEnvironment(LSL_Integer transition, LSL_String daycycle, LSL_Float daylen, LSL_Float dayoffset, LSL_Float altitude1, LSL_Float altitude2, LSL_Float altitude3)`

- `LSL_Integer osResetEnvironment(LSL_Integer parcelOrRegion, LSL_Integer transition)`

- `void osParticleSystem(LSL_List rules)`

- `void osLinkParticleSystem(LSL_Integer linknumber, LSL_List rules)`

- `LSL_Integer osNpcLookAt(LSL_Key npckey, LSL_Integer type, LSL_Key objkey, vector offset)`

- `LSL_Integer osAvatarType(LSL_Key avkey)`

- `LSL_Integer osAvatarType(LSL_String sFirstName, LSL_String sLastName)`

- `void osListSortInPlace(LSL_List src, LSL_Integer stride, LSL_Integer ascending)`

- `void osListSortInPlaceStrided(LSL_List src, LSL_Integer stride, LSL_Integer stride_index, LSL_Integer ascending)`

- `LSL_List osGetParcelDetails(LSL_Key id, LSL_List details)`

- `LSL_List osGetParcelIDs()`

- `LSL_Key osGetParcelID()`

- `LSL_List osOldList2ListStrided(LSL_List src, int start, int end, int stride)`

- `LSL_Integer osGetPrimCount()`

- `LSL_Integer osGetPrimCount(LSL_Key object_id)`

- `LSL_Integer osGetSittingAvatarsCount()`

- `LSL_Integer osGetSittingAvatarsCount(LSL_Key object_id)`

- `LSL_String osAESEncrypt(string secret, string plainText)`

- `LSL_String osAESEncryptTo(string secret, string plainText, string ivString)`

- `LSL_String osAESDecrypt(string secret, string encryptedText)`

- `LSL_String osAESDecryptFrom(string secret, string encryptedText, string ivString)`

- `vector osGetLinkColor(LSL_Integer linknum, LSL_Integer face)`

- `vector osTemperature2sRGB(LSL_Float dtemp)`

- `LSL_Integer osListFindListNext(LSL_List src, LSL_List test, LSL_Integer start, LSL_Integer end, LSL_Integer instance)`

- `LSL_String osListAsString(LSL_List src, int index)`

- `LSL_Integer osListAsInteger(LSL_List src, int index)`

- `LSL_Float osListAsFloat(LSL_List src, int index)`

- `vector osListAsVector(LSL_List src, int index)`

Appendix D entries: 294 OSSL functions.
