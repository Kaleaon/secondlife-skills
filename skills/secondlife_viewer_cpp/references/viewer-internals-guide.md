
# Second Life Viewer Internals — Deep Reference Guide

This guide describes how the Linden Lab viewer (secondlife/viewer, C++, LGPL-2.1) and its Firestorm and Alchemy forks actually work inside: the render pipeline pass by pass, how texture fetch decides what to download first, how the mesh repository turns a UUID into geometry, how an avatar gets baked, how EEP lighting is evaluated, how shadows and the PBR lighting model are implemented, which caches exist and how they evict, the login state machine in llstartup.cpp, and the region and circuit lifecycle including neighbour handoffs and object-update interpolation. File names are the upstream indra/ paths. Where Firestorm or Alchemy diverge in a way that changes behaviour, the divergence is named. Settings names are real viewer settings; the appendix extracts the rendering-relevant subset from the shipped settings.xml with type, default, and comment.

How to use it: read the section that matches the subsystem you are touching, then check the named source file before changing a constant. Almost every number in the viewer that looks arbitrary — a discard threshold, a ping interval, a cascade split — is load-bearing against simulator behaviour, and the sections below explain what each one is load-bearing against.

## The frame at a glance: from packet to pixel

The viewer's main loop in LLAppViewer (indra/newview/llappviewer.cpp) interleaves four kinds of work every frame: network pumping of the UDP circuit and the HTTP cap stack, simulation-state updates (object updates, avatar interpolation, wind and cloud), culling and render-list building in LLPipeline, and the actual GL draw in LLDrawPool passes. Network work is deliberately not decoupled into a free-running thread for the UDP circuit: message handling happens on the main thread so that LLViewerObject mutation never needs locking, while texture fetch, mesh fetch, and image decode run on worker threads and hand results back through thread-safe queues. That single decision explains most viewer architecture: anything that touches the scene graph is main-thread, anything that touches bytes is worker-thread, and the seams between them are explicit queues with discard and cancellation semantics.

## Render pipeline organisation: LLPipeline and spatial groups

LLPipeline (llpipeline.cpp) owns the visible scene. The world is partitioned into LLSpatialGroups arranged in an octree (LLOctree / LLSpatialPartition, with partitions for volume objects, avatar, terrain, water, sky, particles, and HUD). Each frame, the camera frustum walks the octree and groups that pass culling are asked to rebuild their geometry buffers if dirty (rebuildGeom), or to reuse the previous frame's vertex buffers. Rebuild cost is why a busy region spikes when you first turn: hundreds of groups go dirty at once as object updates land, and the viewer spreads rebuilds over frames with a budget. Draw pools (LLDrawPool and subclasses: terrain, tree, simple, alpha, water, sky, avatar, bump, materials, glow) then consume those buffers in pass order. A spatial group is also the unit of occlusion culling and of the 'render cost' accounting used by avatar complexity limits.

## Render passes in order: gbuffer, lighting, shadows, water, transparent, post

In deferred-capable configurations the viewer builds a G-buffer (deferred materials pass) holding albedo, normal, specular/PBR parameters, and emissive in render targets managed by LLRenderTarget. The lighting pass then evaluates lights against that buffer: the sun/moon directional, the local point-light set selected per group, and image-based ambient from the current EEP sky. Shadow maps render before the lighting pass (see the shadow section). Water renders with its own reflection/refraction targets when water quality allows, otherwise as a cheaper opaque-ish pool. Transparent objects (LLDrawPoolAlpha) render after opaque, sorted back-to-front per object, with a separate pre-pass for alpha masks. Glow/bloom is a post chain: bright-pass, downsample blur, composite. UI renders last, orthographic, from the same draw infrastructure. On forward-rendering fallbacks (low graphics tiers, some TPV V1 modes) the same pools run but lighting is evaluated per-object in shaders with a capped light count, which is why identical scenes can light differently across graphics presets.

## Deferred vs forward: what changes for content

Deferred rendering makes local light count effectively a per-pixel cost rather than a hard per-object cap, enables screen-space effects, and makes PBR materials behave consistently. It also raises the cost of transparency, because alpha objects do not write the G-buffer the same way and are lit in a forward sub-path. Content consequences: alpha-blended hair and foliage are disproportionately expensive in deferred mode; emissive faces contribute to bloom only above the glow threshold; and a material that looks correct on a forward-rendering low-end viewer can look flat on deferred if its normal or roughness maps were authored against the old Blinn-Phong specular model. Firestorm exposes more of these toggles than stock; Alchemy tends to default more of them on.

## Texture fetch: the priority algorithm in LLTextureFetch

Texture fetch (lltexturefetch.cpp, lltexturecache.cpp, llimageworker / LLImageDecodeThread) is a scored work queue, not FIFO. Each requested texture carries a desired discard level (0 = full res) computed from its on-screen size: the viewer estimates the texel density the object needs from its projected area and distance, then asks for the lowest discard level that covers it. Priority combines that desired discard, the object's boost category (your own avatar and HUD attachments are boosted, as are textures on objects near the camera centre), how long the request has waited, and whether a lower discard of the same texture is already resident — a texture already visible at discard 2 gets its discard 1 request promoted, because improving a visible blurry texture beats fetching an unseen one. Requests flow HTTP-first via the GetTexture cap with Range requests that map to JPEG2000 layers; the legacy UDP image path exists only as fallback history. Decode runs on worker threads with its own priority queue, and decoded images are written into the texture cache so a restart does not refetch.

## Discard levels and JPEG2000 progression

A Second Life texture is a JPEG2000 codestream whose resolution layers map to discard levels: discard 0 is full resolution, 1 is half in each dimension (quarter the pixels), and so on down to a tiny thumbnail. Fetching 'the first N bytes' of the codestream yields a decodable lower discard, which is why Range requests work: the fetcher requests progressively larger byte ranges as the desired discard falls. The classic visual artefact of a texture stuck blurry is usually not a network failure: it is the priority score never promoting the request because the object is small on screen, or the decode queue saturated, or the texture cache evicting the higher discard under memory pressure from newer arrivals. Settings TextureFetchConcurrency, TextureMemory, and the cache size settings in the appendix control the knobs; raising memory without raising decode concurrency changes little.

## Texture cache, VFS, and eviction

Three storage layers sit under textures. The in-RAM LLViewerTexture / LLImageGL layer holds GPU-ready images with a global texture memory budget; when the budget is exceeded, textures are demoted to higher discard or unloaded by last-use and priority. The on-disk texture cache (lltexturecache) stores raw JPEG2000 codestreams keyed by UUID in a header-plus-body file layout with its own size cap and LRU-style purge; it survives restarts. The legacy VFS (LLVFile / xfer system) still underlies some asset types and cache bookkeeping. Eviction bugs present as textures that load, sharpen, then blur again in a cycle: the working set exceeds the RAM budget, so the viewer thrashes. The correct fix is almost always budget or boost tuning, not fetch code.

## Mesh repository: LLMeshRepository state machine

Mesh fetch (llmeshrepository.cpp) mirrors texture fetch but for LLMesh assets via the GetMesh and GetMesh2 caps. A mesh request moves through states: queued, HTTP in flight (with retries and a per-host concurrency limit shared through the mesh thread), downloaded bytes handed to LLMeshSkinInfo / LLVolume parsing, LOD selection, and finally construction of LLVolumeFace geometry for the requesting LLViewerObject. Skin info is a separate sub-fetch and a frequent failure point: a rigged mesh whose skin block fails to parse renders unrigged at the origin or not at all. The repository also tracks mesh accounting — download weight, streaming cost — because the simulator charges land impact from the same LOD and physics data the viewer downloads. MeshData-era UDP mesh is historical; all current mesh is HTTP.

## LOD selection and streaming cost

The viewer picks a mesh LOD (high, medium, low, lowest) from the object's screen size using the same projected-area logic as textures, with hysteresis so an object near a threshold does not flicker between LODs every frame. LOD switching is also where 'my mesh melts when I walk away' comes from: the low LOD was auto-generated by decimation at upload, not authored, and silhouettes collapse. Because land impact takes the worst of download, physics, and server weights, and download weight grows with the triangle counts of the LODs the viewer will actually stream, LOD authoring is a cost decision as much as a visual one — the assets guide works the numbers.

## Avatar pipeline: LLVOAvatar, appearance, and the bake

LLVOAvatar (llvoavatar.cpp and friends) is the most complex object in the viewer: it owns the skeleton (LLJoint hierarchy from avatar_skeleton.xml, including Bento extension bones), morphs driven by shape parameters, wearable-driven mesh replacement (the system body parts), and attachment points. Appearance arrives as a mix of UDP appearance messages, caps (AgentPreferences, appearance-related AIS operations), and the Current Outfit Folder state. The viewer computes what the avatar should look like locally, requests a bake from the simulator-side bake service for the system layers, and composites Bakes-on-Mesh channels for mesh bodies. An avatar that appears as a cloud, grey, or ruthlessly untextured is almost always a bake or COF problem, not a rendering problem.

## Bakes on Mesh internals

BoM defines bake channels — head, upper, lower, eyes, hair, skirt, and universal layers — each composited server-side from the worn system textures (skin, tattoos, alpha masks, clothing layers in wear order) into a single texture per channel. The viewer sends appearance changes, the bake service (simulator-side, reached through appearance caps and the bake host) returns baked texture UUIDs, and mesh attachments flagged for a channel display that channel's bake instead of their own diffuse. Failure modes are specific: a mesh body showing the system skin stretched means the attachment is flagged for a channel but its UVs are not the system UV layout the bake assumes; a body stuck grey means the bake never arrived (COF version mismatch is the common cause — the viewer increments COF version via IncrementCOFVersion and the bake keys off it); Ruth-era fallback textures mean the bake service rejected the request. Firestorm and stock differ mainly in UI around this; the protocol path is the same.

## EEP: environment as data, evaluated per frame

The Environmental Enhancement Project replaced Windlight presets with inventory assets: sky settings, water settings, and day cycles (llsettings* — LLSettingsSky, LLSettingsWater, LLSettingsDay). The viewer fetches the region and parcel environment via EnvironmentSettings / ExtEnvironment caps, blends parcel-over-region-over-default, and interpolates day-cycle keyframes by time of day. LLSettingsSky carries sun and moon position and colour, ambient, blue horizon and density, cloud coverage and colour, star brightness, and glow parameters; these feed both the sky draw pool (a procedural sky shader, not a texture) and the lighting pass IBL ambient. Water settings drive the water pool's fresnel, normal perturbation, and fog colour. Because environment is data, two viewers side by side can legitimately render different skies if one has a local day-cycle override — a classic false bug report.

## Shadows: cascaded shadow maps and their costs

Directional shadows use cascaded shadow maps (LLShadowMap render targets, typically 4 cascades in stock configurations) split logarithmically between near and far so texel density tracks need. Cascade count, shadow map resolution, shadow bias, and the shadow far plane are the governing settings (appendix: RenderShadow* family). Local-light shadows are far more restricted — historically only a small number of shadow-casting local lights, and many builds disable local shadows entirely for performance. Shadow artefacts map to causes precisely: peter-panning is excess bias, acne is insufficient bias for the map resolution at that cascade, and shimmering at distance is the far cascade's texel size beating the normal offset. Vegetation and alpha-tested materials need alpha-aware depth materials or they cast quad-shaped shadows.

## The PBR lighting model as implemented

Second Life PBR follows the glTF 2.0 metallic-roughness model: a GGX microfacet BRDF with Smith geometry term and Schlick Fresnel, evaluated for the directional sun/moon and for local lights, plus image-based lighting from the EEP sky split into irradiance and prefiltered radiance terms approximated in the viewer's shaders. Material data comes from LLGLTFMaterial assets: base colour texture and factor, metallic-roughness texture (metalness in B, roughness in G), normal map in tangent space, emissive, occlusion in the R channel of the metallic-roughness texture per the SL mapping, alpha mode (opaque, mask with cutoff, blend), and double-sided flag. Legacy materials (diffuse/normal/specular with shininess) are converted into the same shading path with an approximated roughness from specular exponent, which is why old content shifted appearance when PBR shipped. HDR rendering with tonemapping sits after lighting; emissive above the tonemap knee feeds bloom.

## Local lights: selection and falloff

Local point lights are selected per spatial group by distance and intensity, sorted, and capped by shader capacity in forward paths or evaluated in the deferred lighting pass with per-light volumes. Falloff in SL is not physical inverse-square by default for legacy content; radius and falloff parameters on the prim feature map to the shader's attenuation curve, and PBR-era lights behave closer to physical falloff. A room lit by thirty point lights will not show thirty contributions on every surface: per-group selection means lights pop in and out as you cross group boundaries if the scene is over the effective budget. Designing under the budget beats raising it, because deferred local-light cost scales with screen coverage of light volumes.

## Cache systems beyond textures

The viewer layers several caches with different lifetimes. The asset cache (newer builds) stores HTTP-fetched assets by UUID with a size cap, separate from the texture cache. The mesh cache is in-RAM LLVolume retention keyed by mesh UUID and LOD. The name cache holds display names and usernames fetched via GetDisplayNames caps in bulk. The inventory cache is an on-disk snapshot of the inventory skeleton used to paint the inventory UI instantly at login before FetchInventory2 completes — a stale or corrupt inventory cache explains 'my inventory is wrong until I relog' better than any server theory. The region and object cache (objectcache file per region) stores static object data so revisiting a region does not re-download every prim: it is keyed by region and invalidated by object cache version in the region handshake.

## Login state machine: llstartup.cpp in detail

LLStartup (llstartup.cpp) is an explicit state machine (STATE_LOGIN_* and related enums in LLStartupState) driven each idle tick. Broadly: initialise and show login UI; collect credentials and grid choice; POST the login request (XML-RPC historically, LLSD-shaped in modern code paths) to the grid login URI; handle failure reasons distinctly — bad credentials, MFA challenge (the modern flow resubmits with an MFA token and hash), grid down, update required, account suspended; on success parse the LLSD response (agent and session ids, circuit code, sim ip/port, seed capability, inventory skeleton roots, buddy list, initial outfit, login flags); request the region capability map from the seed cap; establish the UDP circuit with UseCircuitCode; send CompleteAgentMovement; wait for RegionHandshake and reply; fetch initial world state (region info, parcel, terrain LayerData, simulator features); start EventQueueGet; transition to in-world idle. Each transition has its own timeout and its own user-facing error, and 'stuck at login' is meaningless without naming the state — the viewer's logs print the state, and any mobile client should copy this state granularity in its own login diagnostics.

## Circuit and region lifecycle

A circuit is the UDP association with one simulator: circuit code plus agent and session ids, sequence counters, reliable-resend queue, ping (StartPingCheck/CompletePingCheck), and throttle buckets. The viewer keeps a circuit to the current region as the agent circuit and lightweight child-agent circuits to neighbour regions (ChildAgentUpdate) so crossing is warm. Region arrival sequence: simulator sends RegionHandshake (product name, region flags, water height, terrain base textures and detail, cache version), viewer replies RegionHandshakeReply with its cache and feature state, then object updates, LayerData patches for terrain/wind/cloud, and CoarseLocationUpdate begin. Leaving is the reverse: TeleportFinish or a border crossing promotes a child circuit to the agent circuit, the old circuit receives CloseCircuit, and caps are rebuilt for the new region — cap URLs never carry over.

## Neighbour regions, border crossing, and teleports

The current simulator informs the viewer of neighbours via EnableSimulator, and the viewer establishes child circuits and pre-fetches coarse state so the neighbour's objects can render at the border. On crossing, AgentCrossing / crossing handling promotes the child, the avatar's attachments and scripts are re-established server-side, and the viewer reconciles its object list against the new region's updates — objects that vanish at borders are usually reconciliation deleting an object whose full update has not yet arrived, not the simulator dropping it. Teleports differ: they are cap-and-UDP orchestrated (TeleportStart, progress, finish/failed), tear down the old circuit entirely, and rebuild caps and circuits at the destination, which is why a failed teleport can leave a client with no valid caps at all. Region restarts announce themselves and drop circuits; the viewer's response (and any client's) should be a clean relogin path, not a resend storm.

## Object updates and interpolation

The simulator sends full ObjectUpdate for new or materially changed objects and ImprovedTerseObjectUpdate for moving ones: position, velocity, acceleration, rotation, and angular velocity in compressed form. The viewer (LLViewerObject / LLVOAvatar update logic, and the interp helpers in llviewerobject) extrapolates between updates using the velocity terms — dead reckoning — and eases corrections when the next update disagrees, trading a small visual slide against network jitter. Terse quantisation (positions packed relative to region origin, rotations as packed small quaternions) puts a floor under achievable smoothness: slow-moving objects step in quanta, which reads as jitter and is a data limit, not a bug. Avatar animation is separate: AvatarAnimation carries animation UUIDs and sequence ids, the viewer plays them against the skeleton with priority and easing rules, and ObjectAnimation does the same for animesh and animated objects.

## Particles, wind, clouds, and LayerData

Terrain, wind, and cloud arrive as LayerData patches (16x16 patch grids with compressed heightfield or vector data) decoded into the surface and atmosphere models. Wind feeds vegetation sway, prim flexi, and audio; cloud data feeds the procedural cloud layer in the sky. Particles are entirely client-side simulations spawned from ObjectUpdate particle parameters (LLViewerPartSim): the simulator sends the emitter recipe, never particle positions, so particle cost is a client GPU/CPU setting (RenderParticleCount and friends), and a 'laggy region' full of emitters is a client budget problem. Flexiprims and prim ribbon effects are likewise client simulations driven by parameters and wind.

## Voice: Vivox legacy and WebRTC current

Legacy voice spawns the closed SLVoice daemon (Vivox SDK) provisioned via ProvisionVoiceAccountRequest; the viewer talks to the daemon over a local control channel and the daemon owns SIP and media. Current voice (viewer 7.1.9+, 2024) is WebRTC: the viewer embeds a WebRTC stack (indra/llwebrtc, 3p-webrtc-build), negotiates per-region voice servers through caps and SimulatorFeatures, and handles spatial audio in-process. There is no peer-to-peer bridging between a WebRTC-only client and a Vivox-only client in the same parcel — they simply cannot hear each other — and OpenSim grids add a third set of mutually incompatible options (Vivox where licensed, FreeSWITCH/mumble modules, Janus experiments). Any client must select its voice stack from region features at runtime.

## Media, CEF, and shared media (MoAP)

In-world web content renders through Dullahan, Linden Lab's CEF (Chromium Embedded Framework) wrapper (secondlife/dullahan): media-on-a-prim faces get a CEF browser instance whose texture is uploaded as a dynamic texture, and the in-viewer browser and search use the same stack. Media cost is Chromium cost — each MoAP face is a browser — and the viewer caps concurrent instances and resolution by settings. Parcel media streams (audio and video URLs) are separate: parcel audio plays through the audio engine (FMOD in stock builds) from the parcel's stream URL, which is why parcel music keeps working when MoAP is disabled.

## Audio engine

Stock viewer audio uses FMOD for parcel streams, UI sounds, and spatialised in-world sounds triggered by llPlaySound-family LSL and object sound properties, with distance and cone attenuation computed client-side. Master, ambient, media, and voice volumes are separate buses in settings. Sound assets themselves are Ogg Vorbis fetched as assets; a sound that plays in one viewer and not another is usually a stream codec or parcel URL issue for streams, or an asset fetch failure for object sounds.

## Settings, command line, and debug surfaces

The viewer is one of the most settings-driven applications in production: settings.xml ships well over a thousand named settings (appendix extracts the rendering, texture, mesh, cache, network, and shadow subsets verbatim). Debug settings are live-editable in the debug console and Advanced menu; many 'bugs' are a persisted debug setting from months earlier. Command-line options select grid (--grid), login URI override, settings file, and logging. The viewer's own logs (SecondLife.log) with session and state markers are the first diagnostic for login and crash work, and crash reporting uploads minidumps keyed by the viewer version and channel — TPV policy requires listed viewers to handle crash reporting and identification honestly.

## Performance diagnosis order

Diagnose viewer performance in data order, not vibes: draw calls and triangle count by pool (stats bar / render debug), texture memory working set versus TextureMemory budget, texture decode queue depth, spatial group rebuild rate when turning, shadow cascade cost at the current preset, local light count in the current groups, particle count, and only then network. The simulator's contribution to perceived lag (script time, physics time, agent update dilation in region stats) is separate from client frame time, and conflating them wastes days: a region at time dilation 0.5 makes everything move slowly on a client rendering at a perfect 120 fps.

## Worked diagnosis: texture that never sharpens

Reproduce with the object centred and filling a quarter of the screen for 30 seconds. If it stays at a low discard: check its boost category (attachments to others and distant objects score low), check the texture cache purge rate in the log (a purge loop means the cache cap is too small for the region's texture population), check decode queue saturation (many large textures arriving together starve later ones), and check TextureMemory versus the working set in the texture console. Changing fetch code before these four checks is how texture bugs live for years.

## Worked diagnosis: avatar bake never completes

Confirm the COF version increments when an outfit item is worn (AIS3 IncrementCOFVersion in the log), confirm the appearance caps were granted in the region cap list, confirm the bake host returned new baked UUIDs, and only then look at BoM channel flags on the mesh. In Lumiya-derived clients the equivalent sequence is: outfit change sent, COF version bumped, bake request answered, baked textures fetched via GetTexture — a break at any step presents identically as a grey avatar, so log each step by name.

## Appendix: rendering, texture, mesh, cache, and network settings from settings.xml

Extracted from the shipped settings.xml in secondlife/viewer (name, type, default, comment). This is the subset whose names match render, texture, mesh, cache, shadow, water, sky, particle, avatar, network, throttle, or login patterns. Defaults are build defaults; user machines will differ wherever a setting persists.

- `AnimateTextures` (Boolean, default 1) — Enable texture animation (debug)

- `TextureLivePreview` (Boolean, default 1) — Preview selections in texture picker or material picker immediately

- `AudioLevelUnderwaterRolloff` (F32, default 5.0) — Same as AudioLevelRolloff, while the camera is underwater

- `AutoLogin` (Boolean, default 0) — Login automatically using last username/password combination

- `RenderSnapshotNoPost` (Boolean, default 0) — Disable tone mapping and exposure correction when snapshot is being rendered

- `AvatarAxisDeadZone0` (F32, default 0.1) — Avatar axis 0 dead zone.

- `AvatarAxisDeadZone1` (F32, default 0.1) — Avatar axis 1 dead zone.

- `AvatarAxisDeadZone2` (F32, default 0.1) — Avatar axis 2 dead zone.

- `AvatarAxisDeadZone3` (F32, default 0.1) — Avatar axis 3 dead zone.

- `AvatarAxisDeadZone4` (F32, default 0.1) — Avatar axis 4 dead zone.

- `AvatarAxisDeadZone5` (F32, default 0.1) — Avatar axis 5 dead zone.

- `AvatarAxisScale0` (F32, default 1.0) — Avatar axis 0 scaler.

- `AvatarAxisScale1` (F32, default 1.0) — Avatar axis 1 scaler.

- `AvatarAxisScale2` (F32, default 1.0) — Avatar axis 2 scaler.

- `AvatarAxisScale3` (F32, default 1.0) — Avatar axis 3 scaler.

- `AvatarAxisScale4` (F32, default 1.0) — Avatar axis 4 scaler.

- `AvatarAxisScale5` (F32, default 1.0) — Avatar axis 5 scaler.

- `AvatarFeathering` (F32, default 16.0) — Avatar feathering (less is softer)

- `AvatarWelcomePack` (String, default https://lecs-viewer-web-components.s3.amazonaws.com/v3.0/[GRID_LOWERCASE]/vawp/index.html) — Avatar Welcome Pack contents

- `AvatarBakedTextureUploadTimeout` (U32, default 60) — Specifes the maximum time in seconds to wait before sending your baked textures for avatar appearance.  Set to 0 to disable and wait until all baked textures are at highest resolution.

- `AvatarRotateThresholdSlow` (F32, default 60) — Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving slowly (degrees)

- `AvatarRotateThresholdFast` (F32, default 2) — Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving fast (degrees)

- `AvatarPhysics` (Boolean, default 1) — Enable avatar physics.

- `BlockAvatarAppearanceMessages` (Boolean, default 0) — Ignores appearance messages (for simulating Ruth)

- `BulkChangeIncludeTextures` (Boolean, default 1) — Bulk permission changes affect textures

- `BulkUpload2KTextures` (Boolean, default 1) — Bulk upload scales textures to 2K if true, to 1K if false

- `EnableDiskCacheDebugInfo` (Boolean, default 0) — When set, display additional cache debugging information

- `DiskCachePercentOfTotal` (F32, default 35.0) — The percent of total cache size (defined by CacheSize) to use for the disk cache (ex: asset storage, excludes textures)

- `DiskCacheDirName` (String, default cache) — The name of the disk cache (within the standard Viewer disk cache directory)

- `CacheLocation` (String, default ?) — Controls the location of the local disk cache

- `CacheLocationTopFolder` (String, default ?) — Controls the top folder location of the the local disk cache

- `CacheSize` (U32, default 6144) — Controls amount of hard drive space reserved for local file caching in MB

- `CacheValidateCounter` (U32, default 0) — Used to distribute cache validation

- `RestoreCameraPosOnLogin` (Boolean, default 0) — Reset camera position to location at logout

- `CmdLineLoginURI` (LLSD, default ?) — Command line specified login server and CGI prefix to use.

- `CmdLineLoginLocation` (String, default ?) — Startup destination requested on command line

- `DebugObjectLODs` (Boolean, default 0) — Show info related to lod calculations for attached or animated objects

- `DebugSelectionLODs` (S32, default -1) — Force selection to show specific LOD, -1 for off, 0 - lowest, 4 - high.

- `AvatarExtentRefreshPeriodBatch` (S32, default 4) — how many frames do we spread over by default when refreshing extents (default is 4)

- `AvatarExtentRefreshMaxPerBatch` (S32, default 5) — how many avatars do we want to handle in total per batch (default is 5)

- `DebugAvatarAppearanceMessage` (Boolean, default 0) — Dump a bunch of XML files when handling appearance messages

- `DebugAvatarExperimentalServerAppearanceUpdate` (Boolean, default 0) — Experiment with sending full cof_contents instead of cof_version

- `DebugAvatarAppearanceServiceURLOverride` (String, default ?) — URL to use for baked texture requests; overrides value returned by login server.

- `DebugAvatarJoints` (String, default ?) — List of joints to emit additional debugging info about.

- `DebugAvatarRezTime` (Boolean, default 0) — Display times for avatars to resolve.

- `DebugAvatarLocalTexLoadedTime` (Boolean, default 1) — Display time for loading avatar local textures.

- `DebugAvatarCompositeBaked` (Boolean, default 0) — Colorize avatar meshes based on baked/composite state.

- `DebugShowAvatarRenderInfo` (Boolean, default 0) — Show avatar render cost information

- `DebugShowRenderInfo` (Boolean, default 0) — Show stats about current scene

- `DebugShowRenderMatrices` (Boolean, default 0) — Display values of current view and projection matrices.

- `DebugShowTextureInfo` (Boolean, default 0) — Show inertested texture info

- `DefaultFemaleAvatar` (String, default Female Shape &amp; Outfit) — Default Female Avatar

- `DefaultLoginLocation` (String, default ?) — Startup destination default (if not specified on command line)

- `DefaultMaleAvatar` (String, default Male Shape &amp; Outfit) — Default Male Avatar

- `RenderVSyncEnable` (Boolean, default 1) — Update frames between display scans (FALSE = Update frames as fast as possible).

- `EffectScriptChatParticles` (Boolean, default 1) — 1 = normal behavior, 0 = disable display of swirling lights when scripts communicate

- `FirstPersonAvatarVisible` (Boolean, default 0) — Display avatar and attachments below neck while in mouselook

- `FirstLoginThisInstall` (Boolean, default 1) — Specifies that you have not logged in with the viewer since you performed a clean install

- `AvatarSitRotation` (LLSD, default ?) — Avatar real sitting rotation used in preset

- `ForceLoginURL` (String, default ) — Force a specified URL for login page content - used if exists

- `IgnoreFOVZoomForLODs` (Boolean, default 0) — Ignore zoom effect(CTRL+0) when calculating lods.

- `InBandwidth` (F32, default 0.0) — Incoming bandwidth throttle (bps)

- `JoystickAvatarEnabled` (Boolean, default 1) — Enables the Joystick to control Avatar movement.

- `LocalCacheVersion` (S32, default 0) — Version number of cache

- `DiskCacheVersion` (S32, default 0) — Version number of disk cache

- `LoginContentVersion` (String, default 2) — Version of login page web based content to display

- `LoginSRVTimeout` (F32, default 90.0) — Duration in seconds of the login SRV request timeout

- `LogTextureNetworkTraffic` (Boolean, default 0) — Log network traffic for textures

- `LoginLocation` (String, default last) — Default Login location ('last', 'home') preference

- `LoginPage` (String, default ?) — Login authentication page.

- `MeshEnabled` (Boolean, default 1) — Expose UI for mesh functionality (may require restart to take effect).

- `MeshImportUseSLM` (Boolean, default 0) — Use cached copy of last upload for a dae if available instead of loading dae file from scratch.

- `MeshUploadLogXML` (Boolean, default 0) — Verbose XML logging on mesh upload

- `MeshUploadFakeErrors` (S32, default 0) — Force upload errors (for testing)

- `MeshUploadTimeOut` (S32, default 600) — Maximum time in seconds for llcurl to execute a mesh uoloading request

- `MigrateCacheDirectory` (Boolean, default 1) — Check for old version of disk cache to migrate to current location

- `NewObjectCreationThrottle` (S32, default 200) — maximum number of new objects created per frame, -1 to disable this throttle

- `NewObjectCreationThrottleDelayTime` (F32, default 2.0) — time in seconds NewObjectCreationThrottle to take effect after the progress screen is lifted

- `NewCacheLocation` (String, default ?) — Change the location of the local disk cache to this

- `NewCacheLocationTopFolder` (String, default ?) — Change the top folder location of the local disk cache to this

- `NextLoginLocation` (String, default ?) — Location to log into for this session - set from command line or the login panel, cleared following a successfull login.

- `ObjectCacheEnabled` (Boolean, default 1) — Enable the object cache.

- `RequestFullRegionCache` (Boolean, default 1) — If set, ask sim to send full region object cache. Needs to restart viewer.

- `OpenDebugStatRender` (Boolean, default 1) — Expand Render performance stats display

- `OpenDebugStatTexture` (Boolean, default 0) — Expand Texture performance stats display

- `OutBandwidth` (F32, default 0.0) — Outgoing bandwidth throttle (bps)

- `PingInterpolate` (Boolean, default 0) — Extrapolate object position along velocity vector based on ping delay

- `PlayTypingAnim` (Boolean, default 1) — Your avatar plays the typing animation whenever you type in the chat bar

- `PostFirstLoginIntroURL` (String, default ) — URL of intro presenatation after first time users first login

- `PostFirstLoginIntroViewed` (Boolean, default 0) — Flag indicating if user has seen intro presenatation after first time users first login

- `PurgeCacheOnNextStartup` (Boolean, default 0) — Clear local file cache next time viewer is run

- `PurgeCacheOnStartup` (Boolean, default 0) — Clear local file cache every time viewer is run

- `QuitOnLoginActivated` (Boolean, default 0) — Quit if login page is activated (used when auto login is on and users must not be able to login manually)

- `RegionTextureSize` (U32, default 256) — Terrain texture dimensions (power of 2)

- `RegionCheckTextureHeights` (Boolean, default 1) — Don't allow user to set low heights greater than high

- `RenderAnisotropic` (Boolean, default 0) — [OBSOLETE] Render textures using anisotropic filtering

- `RenderAnisotropicLevel` (U32, default 0) — Anisotropic filtering strength(0(Disable), 2x, 4x, 8x, 16x

- `RenderAppleUseMultGL` (Boolean, default 0) — Whether we want to use multi-threaded OpenGL on Apple hardware (requires restart of SL).

- `RenderAttachedLights` (Boolean, default 1) — Render lighted prims that are attached to avatars

- `RenderAttachedParticles` (Boolean, default 1) — Render particle systems that are attached to avatars

- `RenderAvatarCloth` (Boolean, default 0) — Controls if system avatar clothes use wavy cloth

- `RenderCanUseGLTFPBROpaqueShaders` (Boolean, default 1) — Hardware has support for GLTF scene shaders

- `RenderCanUseTerrainBakeShaders` (Boolean, default 1) — Hardware has support for Terrain Bake shaders

- `RenderClass1MemoryBandwidth` (F32, default 48.0) — Memory bandwidth at which to default to Class 1 in gigabytes per second.  Used as basis for higher classes.

- `RenderCPUBasis` (F32, default 3000.0) — Reference CPU clockspeed to use to bias GPU class (in MHz).

- `RenderComplexityColorMin` (Color4, default ?) — Unused obsolete setting

- `RenderComplexityColorMid` (Color4, default ?) — Unused obsolete setting

- `RenderComplexityColorMax` (Color4, default ?) — Unused obsolete setting

- `RenderComplexityThreshold` (S32, default -1) — Unused obsolete setting

- `RenderComplexityStaticMax` (S32, default -1) — Unused obsolete setting

- `RenderAvatarLODFactor` (F32, default 0.5) — Controls level of detail of avatars (multiplier for current screen area when calculated level of detail)

- `RenderAvatarMaxVisible` (S32, default 0) — OBSOLETE and UNUSED. See RenderAvatarMaxNonImpostors

- `RenderAvatarPhysicsLODFactor` (F32, default 1.0) — Controls level of detail of avatar physics (such as breast physics).

- `RenderBufferVisualization` (S32, default -1) — Outputs a selected buffer to the screen.  -1 = final render buffer.  0 = Albedo, 1 = Specular/ORM, 2 = Normal, 3 = Emissive, 4 = Eye luminance, 5 = FXAA Luminance/SMAA Edge Tex, 6 = SMAA Blend Weights

- `RenderCompressTextures` (Boolean, default 0) — Enable texture compression on OpenGL 3.0 and later implementations (EXPERIMENTAL, requires restart)

- `RenderHiDPI` (Boolean, default 0) — Enable support for HiDPI displays, like Retina (macOS and Linux ONLY, requires restart)

- `RenderPerformanceTest` (Boolean, default 0) — Disable rendering of everything but in-world content for                 performance testing

- `RenderNsightDebugSupport` (Boolean, default 0) — Disable features which prevent nVidia nSight from being usable with SL. Requires restart.

- `RenderLocalLightCount` (S32, default 256) — Number of local lights to render.

- `RenderShadowSplitExponent` (Vector3, default ?) — Near clip plane split distances for shadow map frusta (x=perspective, y=ortho, z=transition rate).

- `RenderShadowProjOffset` (F32, default 2.0) — Amount to scale distance to virtual origin of shadow perspective projection.

- `RenderShadowSlopeThreshold` (F32, default 0.0) — Cutoff slope value for points to affect perspective shadow generation

- `RenderShadowProjExponent` (F32, default 0.5) — Exponent applied to transition between ortho and perspective shadow projections based on viewing angle and light vector.

- `RenderShadowSplits` (S32, default 3) — Amount of shadow map splits to render (0 - 3).

- `RenderSSAOScale` (F32, default 500.0) — Scaling factor for the area to sample for occluders (pixels at 1 meter away, inversely varying with distance)

- `RenderSSAOIrradianceScale` (F32, default 0.6) — Scaling factor for irradiance input to SSAO

- `RenderSSAOIrradianceMax` (F32, default 0.18) — Max factor for irradiance input to SSAO

- `RenderSSAOMaxScale` (U32, default 200) — Maximum screen radius for sampling (pixels)

- `RenderSSAOFactor` (F32, default 0.30) — Occlusion sensitivity factor for ambient occlusion (larger is more)

- `RenderSSAOEffect` (Vector3, default ?) — Multiplier for (1) value and (2) saturation (HSV definition), for areas which are totally occluded.  Blends with original color for partly-occluded areas.  (Third component is unused.)

- `RenderMirrors` (Boolean, default 0) — Renders realtime mirrors.

- `RenderScreenSpaceReflections` (Boolean, default 0) — Renders screen space reflections to better account for dynamic objects with reflection probes.

- `RenderScreenSpaceReflectionIterations` (S32, default 25) — Number of times the ray march algorithm runs to find a potential hit.

- `RenderScreenSpaceReflectionRayStep` (F32, default 0.1) — How big the step is between each run.

- `RenderScreenSpaceReflectionDistanceBias` (F32, default 0.015) — Distance bias to apply when rejecting a potential sample.

- `RenderScreenSpaceReflectionDepthRejectBias` (F32, default 0.001) — Bias against the depth buffer before rejecting a sample.

- `RenderScreenSpaceReflectionAdaptiveStepMultiplier` (F32, default 1.6) — Multiplier to scale adaptive stepping.

- `RenderScreenSpaceReflectionGlossySamples` (S32, default 4) — Maximum number of samples to apply for glossy SSR.

- `RenderBumpmapMinDistanceSquared` (F32, default 100.0) — Maximum distance at which to render bumpmapped primitives (distance in meters, squared)

- `RenderNormalMapScale` (F32, default 64.0) — Scaler applied to height map when generating normal maps

- `RenderCubeMap` (Boolean, default 1) — Whether we can render the cube map or not

- `RenderDesaturateIrradiance` (Boolean, default 1) — Desaturate irradiance to remove blue tint

- `RenderDebugAlphaMask` (F32, default 0.5) — Test Alpha Masking Cutoffs.

- `RenderDebugGLSession` (Boolean, default 0) — Enable strict GL debugging on the start of next session.

- `RenderDebugNormalScale` (F32, default 0.1) — Scale of normals in debug display.

- `RenderDebugPipeline` (Boolean, default 0) — Enable strict pipeline debugging.

- `RenderDisablePostProcessing` (Boolean, default 0) — Disable tone mapping and exposure correction when build floater is open (for artists developing materials)

- `RenderEnableEmissiveBuffer` (Boolean, default 1) — Enable emissive buffer in gbuffer.  Should only be disabled in GL3 mode.

- `RenderHDRIExposure` (F32, default 0.0) — Exposure adjustment of HDRI when previewing an HDRI.  Units are EV.  Sane values would be -10 to 10.

- `RenderHDRIRotation` (F32, default 0.0) — Rotation (in degrees) of environment when previewing an HDRI.

- `RenderHDRISplitScreen` (F32, default 1.0) — What percentage of screen to render using HDRI vs EEP sky.

- `RenderHDRIIrradianceOnly` (Boolean, default 0) — Only use HDRI sky for irradiance map when RenderHDRISplitScreen is 0

- `RenderMaxOpenGLVersion` (F32, default 4.6) — Maximum OpenGL version to attempt use (minimum 3.1 maximum 4.6).  Requires restart. Windows only.

- `RenderMaxVRAMBudget` (U32, default 0) — Maximum amount of texture memory to budget for (in MB), or 0 for autodetect.

- `RenderTextureVRAMDivisor` (U32, default 1) — Divisor for maximum amount of VRAM the viewer will use for textures. 1 = all the VRAM.  Used in conjunction with RenderMaxVRAMBudget.

- `RenderMinFreeMainMemoryThreshold` (U32, default 512) — If available free physical memory is below this value textures get agresively scaled down

- `RenderLowMemMinDiscardIncrement` (F32, default 0.1) — Minimum increment of discard bias if available texture memory gets low

- `RenderHighMemMinDiscardDecrement` (F32, default 0.1) — Minimum decrement of discard bias if excess texture memory is available

- `RenderMaxTextureIndex` (U32, default 16) — Maximum texture index to use for indexed texture rendering.

- `RenderMaxTextureResolution` (U32, default 2048) — Maximum texture resolution to download for non-boosted textures.

- `RenderDownScaleMethod` (U32, default 0) — Method to use to downscale images.  0 - FBO, 1 - PBO

- `RenderDebugTextureBind` (Boolean, default 0) — Enable texture bind performance test.

- `RenderDelayCreation` (Boolean, default 0) — Throttle creation of drawables.

- `RenderAnimateRes` (Boolean, default 0) — Animate rezing prims.

- `RenderBakeSunlight` (Boolean, default 0) — Bake sunlight into vertex buffers for static objects.

- `RenderNoAlpha` (Boolean, default 0) — Disable rendering of alpha objects (render all alpha objects as alpha masks).

- `RenderMinimumLODTriangleCount` (U32, default 16) — Triangle count threshold at which automatic LOD generation stops

- `RenderEdgeDepthCutoff` (F32, default 0.01) — Cutoff for depth difference that amounts to an edge.

- `RenderEdgeNormCutoff` (F32, default 0.25) — Cutoff for normal difference that amounts to an edge.

- `RenderDeferredAlphaSoften` (F32, default 0.75) — Scalar for softening alpha surfaces (for soft particles).

- `RenderDeferredNoise` (F32, default 4.0) — Noise scalar to hide banding in deferred render.

- `RenderDeferredSpotShadowBias` (F32, default -64.0) — Bias value for spot shadows (prevent shadow acne).

- `RenderDeferredSpotShadowOffset` (F32, default 0.8) — Offset value for spot shadows (prevent shadow acne).

- `RenderShadowBias` (F32, default -0.002) — Bias value for shadows (prevent shadow acne).

- `RenderShadowOffset` (F32, default 0.01) — Offset value for shadows (prevent shadow acne).

- `RenderShadowBiasError` (F32, default -0.007) — Error scale for shadow bias (based on altitude).

- `RenderShadowOffsetError` (F32, default 0.0) — Error scale for shadow offset (based on altitude).

- `RenderDepthPrePass` (Boolean, default 0) — EXPERIMENTAL: Prime the depth buffer with simple prim geometry before rendering with textures.

- `RenderDepthOfField` (Boolean, default 0) — Whether to use depth of field effect when Advanced Lighting Model is enabled

- `RenderDepthOfFieldInEditMode` (Boolean, default 0) — Whether to use depth of field effect when in edit mode

- `RenderSpotLightsInNondeferred` (Boolean, default 0) — Whether to support projectors as spotlights when Advanced Lighting Model is disabled

- `RenderSpotShadowBias` (F32, default -0.0002) — Bias value for shadows (prevent shadow acne).

- `RenderSpotShadowOffset` (F32, default 0.04) — Offset value for shadows (prevent shadow acne).

- `RenderShadowResolutionScale` (F32, default 1.0) — Scale of shadow map resolution vs. screen resolution (only positivie values are allowed)

- `RenderDeferredTreeShadowBias` (F32, default 1.0) — Bias value for tree shadows (prevent shadow acne).

- `RenderDeferredTreeShadowOffset` (F32, default 1.0) — Offset value for tree shadows (prevent shadow acne).

- `RenderHoverGlowEnable` (Boolean, default 0) — DEPRECATED --- Show glow effect when hovering on interactive objects.

- `RenderHighlightFadeTime` (F32, default 0.1) — Transition time for mouseover highlights.

- `RenderHighlightBrightness` (F32, default 4.0) — Brightness of mouseover highlights.

- `RenderHighlightThickness` (F32, default 0.6) — Thickness of mouseover highlights.

- `RenderHighlightColor` (Color4, default ?) — Brightness of mouseover highlights.

- `RenderSpecularPrecision` (U32, default 0) — Force 32-bit floating point LUT

- `RenderSpecularResX` (U32, default 1024) — Spec map resolution.

- `RenderSpecularResY` (U32, default 256) — Spec map resolution.

- `RenderSpecularExponent` (F32, default 368.0) — Specular exponent for generating spec map

- `RenderDeferred` (Boolean, default 1) — DEPRECATED (only true supported) - Use deferred rendering pipeline (Advanced Lighting Model).

- `RenderDeferredSun` (Boolean, default 1) — Execute sunlight shader in deferred renderer.

- `RenderDeferredAtmospheric` (Boolean, default 1) — Execute atmospheric shader in deferred renderer.

- `RenderDeferredSSAO` (Boolean, default 1) — Execute screen space ambient occlusion shader in deferred renderer.

- `RenderDeferredBlurLight` (Boolean, default 1) — Execute shadow softening shader in deferred renderer.

- `RenderDeferredSunWash` (F32, default 0.5) — Amount local lights are washed out by sun.

- `RenderShadowNoise` (F32, default -0.0001) — Magnitude of noise on shadow samples.

- `RenderShadowErrorCutoff` (F32, default 5.0) — Cutoff error value to use ortho instead of perspective projection.

- `RenderShadowFOVCutoff` (F32, default 0.8) — Cutoff FOV to use ortho instead of perspective projection.

- `RenderShadowGaussian` (Vector3, default ?) — Gaussian coefficients for the two shadow/SSAO blurring passes (z component unused).

- `RenderShadowBlurSize` (F32, default 1.4) — Scale of shadow softening kernel.

- `RenderShadowBlurSamples` (U32, default 4) — Number of samples to take for each pass of shadow blur (value range 1-16).  Actual number of samples is value * 2 - 1.

- `RenderShadowBlurDistFactor` (F32, default 0) — Distance scaler for shadow blur.

- `RenderDynamicLOD` (Boolean, default 1) — Dynamically adjust level of detail.

- `RenderFSAASamples` (U32, default 0) — Quality of antialiasing: 0 = Low, 1 = Medium, 2 = High, 3 = Ultra

- `RenderFSAAType` (U32, default 0) — Type of Antialiasing to use: 0 = None, 1 = FXAA, 2 = SMAA

- `RenderFarClip` (F32, default 256.0) — Distance of far clip plane from camera (meters)

- `RenderAutoMaskAlphaNonDeferred` (Boolean, default 1) — Use alpha masks where appropriate when not using the Advanced Lighting Model

- `RenderAutoMaskAlphaDeferred` (Boolean, default 1) — Use alpha masks where appropriate in the Advanced Lighting Model

- `RenderFlexTimeFactor` (F32, default 1.0) — Controls level of detail of flexible objects (multiplier for amount of time spent processing flex objects)

- `RenderFogRatio` (F32, default 4.0) — DEPRECATED - Distance from camera where fog reaches maximum density (fraction or multiple of far clip distance)

- `RenderGamma` (F32, default 0.0) — DEPRECATED - Sets gamma exponent for renderer

- `RenderGammaFull` (Boolean, default 1.0) — Use fully controllable gamma correction, instead of faster, hard-coded gamma correction of 2.

- `RenderDeferredDisplayGamma` (F32, default 2.2) — Gamma ramp exponent for final correction before display gamma.

- `RenderGLContextCoreProfile` (Boolean, default 0) — Don't use a compatibility profile OpenGL context.  Requires restart.

- `RenderGLMultiThreadedTextures` (Boolean, default 0) — Allow OpenGL to use multiple render contexts for loading textures (may reduce frame stutters, doesn't play nice with Intel drivers).

- `RenderGLMultiThreadedMedia` (Boolean, default 0) — Allow OpenGL to use multiple render contexts for playing media (may reduce frame stutters, doesn't play nice with Intel drivers)

- `RenderGlow` (Boolean, default 1) — Render bloom post effect.

- `RenderGlowIterations` (S32, default 2) — Number of times to iterate the glow (higher = wider and smoother but slower)

- `RenderGlowLumWeights` (Vector3, default ?) — Weights for each color channel to be used in calculating luminance (should add up to 1.0)

- `RenderGlowMaxExtractAlpha` (F32, default 0.25) — Max glow alpha value for brightness extraction to auto-glow.

- `RenderGlowMinLuminance` (F32, default 9999) — Min luminance intensity necessary to consider an object bright enough to automatically glow.

- `RenderGlowResolutionPow` (S32, default 9) — Glow map resolution power of two.

- `RenderGlowHDR` (Boolean, default 0) — Enable HDR for glow map

- `RenderGlowStrength` (F32, default 0.325) — Additive strength of glow.

- `RenderGlowWarmthAmount` (F32, default 0.0) — Amount of warmth extraction to use (versus luminance extraction). 0 = lum, 1.0 = warmth

- `RenderGlowWarmthWeights` (Vector3, default ?) — Weight of each color channel used before finding the max warmth

- `RenderGlowWidth` (F32, default 1.3) — Glow sample size (higher = wider and softer but eventually more pixelated)

- `RenderGlowNoise` (Boolean, default 1) — Enables glow noise (dithering). Reduces banding from glow in certain cases.

- `DisableAllRenderTypes` (Boolean, default 0) — Disables all rendering types.

- `DisableAllRenderFeatures` (Boolean, default 0) — Disables all rendering features.

- `RenderHUDInSnapshot` (Boolean, default 0) — Display HUD attachments in snapshot

- `RenderHUDParticles` (Boolean, default 0) — Display particle systems in HUD attachments (experimental)

- `RenderHighlightSelections` (Boolean, default 1) — Show selection outlines on objects

- `RenderHiddenSelections` (Boolean, default 0) — Show selection lines on objects that are behind other objects

- `RenderHideGroupTitle` (Boolean, default 0) — Don't show my group title in my name label

- `NametagOverWater` (Boolean, default 1) — Render name tag over the transparent water while camera is above the water

- `RenderInitError` (Boolean, default 0) — Error occured while initializing GL

- `RenderLightRadius` (Boolean, default 0) — Render the radius of selected lights

- `RenderHeroProbeResolution` (S32, default 1024) — Resolution to render hero probes used for mirrors, water, etc.

- `RenderHeroProbeDistance` (F32, default 8) — Distance in meters for hero probes to render out to.

- `RenderHeroProbeUpdateRate` (S32, default 2) — How many frames to wait for until it's time to render the probe. E.g., every other frame (1), every two frames (2), every three frames (3) etc.

- `RenderHeroProbeConservativeUpdateMultiplier` (S32, default 16) — How many probe updates to wait until it's time to update faces that are not directly facing the camera.  Acts as a multiplier.  E.g., frames to the periphery of the camera updating once every 3 updates, vs ones directly facing the camera updating every update.

- `RenderReflectionProbeShowTransparent` (Boolean, default 1) — Show reflection probes in the transparency debug view

- `RenderReflectionProbeVolumes` (Boolean, default 0) — Render influence volumes of Reflection Probes

- `RenderMaxPartCount` (S32, default 4096) — Maximum number of particles to display on screen

- `RenderMaxNodeSize` (S32, default 65536) — Maximum size of a single node's vertex data (in KB).

- `RenderMaxVBOSize` (S32, default 4096) — Maximum size of a vertex buffer (in KB).

- `RenderNameFadeDuration` (F32, default 1.0) — Time interval over which to fade avatar names (seconds)

- `RenderNameShowSelf` (Boolean, default 1) — Display own name above avatar

- `RenderNameShowTime` (F32, default 10.0) — Fade avatar names after specified time (seconds)

- `RenderObjectBump` (Boolean, default 1) — DEPRECATED (only TRUE supported) Show bumpmapping on primitives

- `RenderQualityPerformance` (U32, default 1) — Which graphics settings you've chosen. Don't use this setting to change quality directly from debug settings.

- `RenderReflectionDetail` (S32, default 2) — DEPRECATED -- use RenderTransparentWater and RenderReflectionProbeDetail -- Detail of reflection render pass.

- `RenderShadowDetail` (S32, default 2) — Detail of shadows.

- `RenderReflectionsEnabled` (Boolean, default 1) — Enable/disable reflection probes

- `RenderReflectionProbeDetail` (S32, default 1) — Detail of reflections. (-1 - Disabled, 0 - Static Only, 1 - Static + Dynamic, 2 - Realtime)

- `RenderReflectionProbeDynamicAllocation` (S32, default -1) — Enable dynamic allocation of reflection probes. -1 means no dynamic allocation. Sets a buffer to allocate when a dynamic allocation occurs otherwise.

- `RenderReflectionProbeCount` (U32, default 256) — Number of probes to render.  Maximum of 256.  Clamps to the nearest power of 2.

- `RenderReflectionProbeResolution` (U32, default 128) — Resolution of reflection probe radiance maps (requires restart).  Will be set to the next highest power of two clamped to [64, 512].  Note that changing this value may consume a massive amount of video memory.

- `RenderExposure` (F32, default 1.0) — Exposure value to send to tonemapper.

- `RenderReflectionProbeDrawDistance` (F32, default 64.0) — Camera far clip to use when updating reflection probes.

- `RenderReflectionProbeAmbiance` (F32, default 0) — Amount reflection probes contribute to ambient light.

- `RenderDefaultProbeUpdatePeriod` (F32, default 2.0) — When RenderReflectionProbeLevel is 0, amount of time in seconds to wait between updates to reflection map.

- `RenderReflectionProbeLevel` (S32, default 3) — Reflection probes control.  0 - disable (one probe to rule them all), 1 - manual probes only, 2 - manual + terrain/water, 3 - Manual + Terrain/water + objects.

- `RenderReflectionRes` (S32, default 64) — Reflection map resolution.

- `RenderReservedTextureIndices` (S32, default 14) — Count of texture indices to reserve for shadow and reflection maps when using indexed texture rendering.  Probably only want to set from the login screen.

- `RenderResolutionDivisor` (U32, default 1) — Divisor for rendering 3D scene at reduced resolution.

- `RenderShaderLightingMaxLevel` (S32, default 3) — Max lighting level to use in the shader (class 3 is default, 2 is less lights, 1 is sun/moon only.  Works around shader compiler bugs on certain platforms.)

- `RenderSkyAutoAdjustLegacy` (Boolean, default 0) — If true, automatically adjust legacy skies (those without a probe ambiance value) to take advantage of probes and HDR.  This is the "opt-out" button for HDR and tonemapping when coupled with a sky setting that predates PBR.

- `RenderSkyAutoAdjustAmbientScale` (F32, default 1.0) — Amount to scale ambient when auto-adjusting legacy skies

- `RenderSkyAutoAdjustHDRScale` (F32, default 1.0) — HDR Scale value to use when auto-adjusting legacy skies

- `RenderSkyAutoAdjustBlueHorizonScale` (F32, default 1.0) — Blue Horizon Scale value to use when auto-adjusting legacy skies

- `RenderSkyAutoAdjustBlueDensityScale` (F32, default 1.0) — Blue Horizon Scale value to use when auto-adjusting legacy skies

- `RenderSkyAutoAdjustSunColorScale` (F32, default 1.0) — Sun color scalar when auto-adjusting legacy skies

- `RenderSkyAutoAdjustProbeAmbiance` (F32, default 0.01) — Probe ambiance value when auto-adjusting legacy skies

- `RenderSkySunlightScale` (F32, default 1.0) — Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is disabled

- `RenderHDRSkySunlightScale` (F32, default 1.0) — Sunlight scale fudge factor for matching with pre-PBR viewer when HDR is enabled

- `RenderSkyAmbientScale` (F32, default 1.0) — Ambient scale fudge factor for matching with pre-PBR viewer

- `RenderReflectionProbeMaxLocalLightAmbiance` (F32, default 4.0) — Maximum effective probe ambiance for local lights

- `RenderUseExposureSkySettings` (Boolean, default 0) — Use exposure sky settings instead of deriving from HDR scale.

- `RenderDynamicExposureCoefficient` (F32, default 0.5) — Luminance coefficient for dynamic exposure

- `RenderDiffuseLuminanceScale` (F32, default 0.5) — Luminance adjustment for diffuse surfaces to aid auto-exposure behavior

- `RenderShaderLODThreshold` (F32, default 1.0) — Fraction of draw distance defining the switch to a different shader LOD

- `RenderShaderParticleThreshold` (F32, default 0.25) — Fraction of draw distance to not use shader on particles

- `RenderSunDynamicRange` (F32, default 1.0) — Defines what percent brighter the sun is than local point lights (1.0 = 100% brighter. Value should not be less than 0. ).

- `RenderTerrainDetail` (S32, default 1) — Detail applied to terrain texturing (0 = none, 1 = full)

- `RenderTerrainLODFactor` (F32, default 1.0) — Controls level of detail of terrain (multiplier for current screen area when calculated level of detail)

- `RenderTerrainScale` (F32, default 12.0) — Terrain detail texture scale (meters)

- `RenderTerrainPBREnabled` (Boolean, default 0) — Enable PBR Terrain features.

- `RenderTerrainPBRDetail` (S32, default 0) — Detail level for PBR terrain. 0 is full detail. Negative values drop rendering features, in accordance with the GLTF specification when possible, which reduces the number of texture binds.

- `RenderTerrainPBRScale` (F32, default 8.0) — PBR terrain detail texture scale (meters)

- `RenderTerrainPBRPlanarSampleCount` (S32, default 3) — How many UV planes to sample PBR terrain textures from. 1 is "flat", 3 is triplanar mapping (aka box mapping)

- `RenderTerrainPBRTriplanarBlendFactor` (F32, default 8.0) — Higher values create sharper transitions, but are more likely to produce artifacts.

- `RenderTerrainPBRTransformsEnabled` (Boolean, default 0) — EXPERIMENTAL: Enable PBR Terrain texture transforms.

- `RenderTerrainPBRNormalsEnabled` (Boolean, default 0) — EXPERIMENTAL: Change normal gen for PBR Terrain.

- `RenderTrackerBeacon` (Boolean, default 1) — Display tracking arrow and beacon to target avatar, teleport destination

- `RenderTransparentWater` (Boolean, default 1) — Render water as transparent.  Setting to false renders water as opaque with a simple texture applied.

- `RenderTreeLODFactor` (F32, default 0.5) — Controls level of detail of vegetation (multiplier for current screen area when calculated level of detail)

- `RenderUIInSnapshot` (Boolean, default 0) — Display user interface in snapshot

- `RenderBalanceInSnapshot` (Boolean, default 1) — Display L$ balance in snapshot

- `RenderUIBuffer` (Boolean, default 0) — Cache ui render in a screen aligned buffer.

- `RenderUnloadedAvatar` (Boolean, default 0) — Show avatars which haven't finished loading

- `RenderUseAdvancedAtmospherics` (Boolean, default 0) — Use fancy precomputed atmospherics and stuff.

- `RenderUseTriStrips` (Boolean, default 0) — DEPRECATED - now always assumed to be false - Use triangle strips for rendering prims.

- `RenderUseFarClip` (Boolean, default 1) — If false, frustum culling will ignore far clip plane.

- `RenderAvatarFriendsOnly` (Boolean, default 0) — When enabled hides all avatars that aren't friends. Does not affect inworld control avatars (animeshes), nor self.

- `RenderAvatarComplexityMode` (S32, default 0) — 0 - complexity limit applies to everyone, 1 - always show friends, 2 - only show friends

- `RenderAvatarMaxNonImpostors` (U32, default 12) — Maximum number of avatars to fully render at one time;     over this limit uses impostor rendering (simplified rendering     with less frequent updates), reducing client lag.

- `RenderAutoMuteRenderWeightLimit` (U32, default 0) — OBSOLETE. This setting has been renamed RenderAvatarMaxNonImpostors.

- `RenderAvatarMaxComplexity` (U32, default 0) — Maximum Avatar Complexity; above this value, the avatar is     rendered as a solid color outline (0 to disable this limit).

- `RenderHUDObjectsWarning` (U32, default 1000) — Viewer will warn user about HUD containing to many objects if objects count is above this value

- `RenderHUDTexturesWarning` (U32, default 200) — Viewer will warn user about HUD containing to many textures if texture count is above this value

- `RenderHUDOversizedTexturesWarning` (U32, default 6) — How many textures with size 1024 * 1024 or bigger HUD can contain before notifying user

- `RenderHUDTexturesMemoryWarning` (U32, default 32000000) — Viewer will warn user about HUD textures using memory above this value (in bytes)

- `RenderAutoMuteSurfaceAreaLimit` (F32, default 1000.0) — Maximum surface area of attachments before an avatar is     rendered as a simple impostor (to not use this limit, set to zero     or set RenderAvatarMaxComplexity to zero).

- `RenderAutoMuteLogging` (Boolean, default 0) — Show extra information in viewer logs about avatar rendering costs

- `RenderAutoHideSurfaceAreaLimit` (F32, default 10.0E6) — Maximum surface area of a set of proximal objects inworld before automatically hiding geometry to prevent system overload.

- `RenderVBOEnable` (Boolean, default 1) — Use GL Vertex Buffer Objects

- `RenderUseVAO` (Boolean, default 0) — [EXPERIMENTAL] Use GL Vertex Array Objects.

- `RenderVBOMappingDisable` (Boolean, default 1) — Disable VBO glMapBufferARB

- `RenderUseStreamVBO` (Boolean, default 1) — Use VBO's for stream buffers

- `RenderPreferStreamDraw` (Boolean, default 0) — Use GL_STREAM_DRAW in place of GL_DYNAMIC_DRAW

- `RenderVolumeLODFactor` (F32, default 1.0) — Controls level of detail of primitives (multiplier for current screen area when calculated level of detail)

- `RenderWater` (Boolean, default 1) — Display water

- `RenderWaterMaterials` (S32, default 0) — Water planar reflections include materials rendering.

- `RenderWaterMipNormal` (Boolean, default 1) — Use mip maps for water normal map.

- `RenderWaterRefResolution` (S32, default 512) — Water planar reflection resolution.

- `RenderParcelSelection` (Boolean, default 1) — Display selected parcel outline

- `RenderShaderCacheEnabled` (Boolean, default 1) — Enable binary shader cache

- `RenderShaderCacheVersion` (String, default 00000000-0000-0000-0000-000000000000) — Current version hash for shader cache

- `RenderCASSharpness` (F32, default 0.4) — Level of sharpening to apply via Contrast Adaptive Sharpening (0.0(off) - 1.0)

- `RenderTonemapMix` (F32, default 0.7) — Mix between linear and tonemapped colors (0.0(Linear) - 1.0(Tonemapped)

- `RenderTonemapType` (U32, default 1) — What tonemapper to use: 0 = Khronos Neutral, 1 = ACES

- `RenderHighPrecisionPostProcess` (Boolean, default 0) — Use 16-bit floating point buffers for post process rendering

- `MeshTriangleBudget` (U32, default 250000) — Target visible triangle budget to use when estimating streaming cost.

- `MeshMetaDataDiscount` (U32, default 384) — Number of bytes to deduct for metadata when determining streaming cost.

- `MeshMinimumByteSize` (U32, default 16) — Minimum number of bytes per LoD block when determining streaming cost.

- `MeshBytesPerTriangle` (U32, default 16) — Approximation of bytes per triangle to use for determining mesh streaming cost.

- `Mesh2MaxConcurrentRequests` (U32, default 8) — Number of connections to use for loading meshes.

- `MeshMaxConcurrentRequests` (U32, default 32) — Number of connections to use for loading meshes (legacy system).

- `MeshUseHttpRetryAfter` (Boolean, default 1) — If TRUE, use Retry-After response headers when rescheduling a mesh request that fails with an HTTP 503 status.  Static.

- `MeshUseGetMesh1` (Boolean, default 0) — If TRUE, use the legacy GetMesh capability for mesh download requests.  Semi-dynamic (read at region crossings).

- `ScaleStretchTextures` (Boolean, default 1) — Stretch textures along with object when scaling

- `SelectionHighlightAlpha` (F32, default 0.40000000596) — Opacity of selection highlight (0.0 = completely transparent, 1.0 = completely opaque)

- `SelectionHighlightAlphaTest` (F32, default 0.1) — Alpha value below which pixels are displayed on selection highlight line (0.0 = show all pixels, 1.0 = show now pixels)

- `SelectionHighlightThickness` (F32, default 0.00999999977648) — Thickness of selection highlight line (fraction of view distance)

- `SelectionHighlightUAnim` (F32, default 0.0) — Rate at which texture animates along U direction in selection highlight line (fraction of texture per second)

- `SelectionHighlightUScale` (F32, default 0.1) — Scale of texture display on selection highlight line (fraction of texture size)

- `SelectionHighlightVAnim` (F32, default 0.5) — Rate at which texture animates along V direction in selection highlight line (fraction of texture per second)

- `SelectionHighlightVScale` (F32, default 1.0) — Scale of texture display on selection highlight line (fraction of texture size)

- `AvatarNameTagMode` (S32, default 1) — Select Avatar Name Tag Mode

- `ShowObjectRenderingCost` (Boolean, default 1) — Show the object rendering cost  in  build tools

- `SkyAmbientScale` (F32, default 0.300000011921) — Controls strength of ambient, or non-directional light from the sun and moon (fraction or multiple of default ambient level)

- `SkyMoonDefaultPosition` (Vector3, default ?) — Default position of sun in sky (direction in world coordinates)

- `SkyNightColorShift` (Color3, default ?) — Controls moonlight color (base color applied to moon as light source)

- `SkySunDefaultPosition` (Vector3, default ?) — Default position of sun in sky (direction in world coordinates)

- `TextureCameraBoost` (F32, default 8.0) — Amount to boost resolution of textures that are important to the camera.

- `TextureDecodeDisabled` (Boolean, default 0) — If TRUE, do not fetch and decode any textures

- `TextureDisable` (Boolean, default 0) — If TRUE, do not load textures for in-world content

- `TextureDiscardLevel` (U32, default 0) — Specify texture resolution (0 = highest, 5 = lowest)

- `TextureDiscardBackgroundedTime` (F32, default 60.0) — Specify how long to wait before discarding texture data after viewer is backgrounded.  (zero or negative to disable)

- `TextureDiscardMinimizedTime` (F32, default 1.0) — Specify how long to wait before discarding texture data after viewer is minimized.  (zero or negative to disable)

- `TextureFetchConcurrency` (U32, default 0) — Maximum number of HTTP connections used for texture fetches

- `TextureFetchMinTimeToLog` (F32, default 2.0) — If texture fetching time exceeds this value, texture fetch tester will log info

- `TextureFetchFakeFailureRate` (F32, default 0.0) — Simulate HTTP fetch failures for some server bake textures.

- `TextureFetchUpdateMinCount` (S32, default 32) — Minimum number of textures to update per frame

- `TextureLoadFullRes` (Boolean, default 0) — If TRUE, always load textures at full resolution (discard = 0)

- `TextureNewByteRange` (Boolean, default 1) — Use the new more accurate byte range computation for j2c discard levels

- `TextureReverseByteRange` (S32, default 50) — Minimal percent of the optimal byte range allowed to render a given discard level

- `TextureSaveLocation` (String, default ?) — Current location for bulk saving textures to disk

- `TextureScaleMinAreaFactor` (F32, default 0.0095) — Limits how texture scale affects area calculation.

- `TextureScaleMaxAreaFactor` (F32, default 25.0) — Limits how texture scale affects area calculation.

- `ThrottleBandwidthKBPS` (F32, default 3000.0) — Maximum allowable downstream bandwidth (kilo bits per second)

- `UISndChatPing` (String, default 7dd36df6-2624-5438-f988-fdf8588a0ad9) — Sound file for chat ping(uuid for sound asset)

- `UISndTyping` (String, default 5e191c7b-8996-9ced-a177-b2ac32bfea06) — Sound file for starting to type a chat message (uuid for sound asset)

- `UseCircuitCodeMaxRetries` (S32, default 3) — Max timeout count for the initial UseCircuitCode message

- `UseCircuitCodeTimeout` (F32, default 5.0) — Timeout duration in seconds for the initial UseCircuitCode message

- `UseDebugLogin` (Boolean, default 0) — Provides extra control over which grid to connect to

- `EnvironmentPersistAcrossLogin` (Boolean, default 0) — Keep Environment settings consistent across sessions

- `RenderOcclusionTimeout` (U32, default 8) — Maximum number of frames to wait on an occlusion query before forcibly reading it back

- `UseObjectCacheOcclusion` (Boolean, default 1) — Enable object cache level object culling based on occlusion (coverage) by other objects

- `RenderDelayVBUpdate` (Boolean, default 0) — Delay vertex buffer updates until just before rendering

- `UserLoginInfo` (LLSD, default ?) — User login data.

- `RegionCrossingInterpolationTime` (F32, default 1) — How long to extrapolate object motion after crossing regions

- `WaterGLFogDensityScale` (F32, default 0.02) — Maps shader water fog density to gl fog density

- `WaterGLFogDepthFloor` (F32, default 0.25) — Controls how dark water gl fog can get

- `WaterGLFogDepthScale` (F32, default 50.0) — Controls how quickly gl fog gets dark under water

- `WindLightUseAtmosShaders` (Boolean, default 1) — DEPRECATED (only true supported) - Whether to enable or disable WindLight atmospheric shaders.

- `XferThrottle` (F32, default 150000.0) — Maximum allowable downstream bandwidth for asset transfers (bits per second)

- `particlesbeacon` (Boolean, default 0) — Beacon / Highlight particle generators

- `renderbeacons` (Boolean, default 0) — Beacon / Highlight particle generators

- `renderhighlights` (Boolean, default 1) — Beacon / Highlight scripted objects with touch function

- `LogTextureDownloadsToViewerLog` (Boolean, default 0) — Send texture download details to the viewer log

- `LogTextureDownloadsToSimulator` (Boolean, default 0) — Send a digest of texture info to the sim

- `TextureLoggingThreshold` (U32, default 1) — Specifies the byte threshold at which texture download data should be sent to the sim.

- `max_texture_dimension_X` (S32, default 1024) — Maximum texture width for user uploaded textures

- `max_texture_dimension_Y` (S32, default 1024) — Maximum texture height for user uploaded textures

- `EnableAvatarPay` (Boolean, default 1) — Enable paying other avatars from web link

- `EnableAvatarShare` (Boolean, default 1) — Enable sharing from web link

- `LogInventoryDecline` (Boolean, default 1) — Log in system chat whenever an inventory offer is declined

- `AllowSelectAvatar` (Boolean, default 0) — Allows user to select and move avatars, move is viewer sided, does not propagate to server, also supresses avatar position updates while avatars are selected

- `ShowHelpOnFirstLogin` (Boolean, default 0) — Show Help Floater on first login

- `PathfindingRetrieveNeighboringRegion` (U32, default 99) — Download a neighboring region when visualizing a pathfinding navmesh (default val 99 means do not download neighbors).

- `PathfindingNavMeshClear` (Color4, default ?) — Background color when displaying pathfinding navmesh.

- `PathfindingWaterColor` (Color4, default ?) — Color of water plane when displaying pathfinding navmesh.

- `RenderAvatarMaxART` (F32, default 4.699) — Render Time Limit in microseconds (0.0 = no limit)

- `AutoTuneRenderFarClipMin` (F32, default 32.0) — The lowest draw distance that auto tune is allowed to use

- `AutoTuneRenderFarClipTarget` (F32, default 256.0) — The draw distance that auto tune will try to achieve

- `360CaptureHideAvatars` (Boolean, default 0) — Flag if set, removes all the avatars from the 360 snapshot

- `360CaptureNumRenderPasses` (U32, default 3) — Number of times to render the scene while taking a snapshot

- `RenderHDREnabled` (Boolean, default 1) — Enable HDR rendering.

- `RenderDisableVintageMode` (Boolean, default 1) — Enables additional rendering pipeline features on newer machines such as HDR and emissive textures on PBR content.

- `PurgeDiskCacheOnStartup` (Boolean, default 0) — Whether or not to LRU purge the disk cache during startup on main thread

- `ScriptEditorDisableSyntaxHighlight` (Boolean, default 0) — Disable syntax highlighting in script editor for performance testing

Appendix entries: 420 settings extracted.

## Login states in detail: reading an llstartup log

LLStartup logs its state transitions, and a stuck login names its state if you read the last transition rather than the spinner. States before credentials cover app initialisation, VFS and cache init, and login UI display — a hang here is local (corrupt cache or settings) and deleting the cache folder is a legitimate test. The credential and request states cover grid resolution and the login POST: failures here are network, grid status, or an update-required response the UI should surface. MFA sits in its own sub-flow in current viewers: the first POST returns a challenge reason, the viewer prompts, and the resubmission carries the token — a client that maps every non-success login response to 'wrong password' will lock users out of MFA accounts, which is exactly the bug class fixed in the Lumiya repair work where SLAuthReply learned to parse reason and mfa_hash. Post-login states cover seed-cap exchange, circuit establishment, handshake wait, and initial inventory and world fetch: a hang in handshake wait with a live circuit is a simulator-side or UDP-path problem, while a hang in cap exchange is HTTPS. Timeout values differ per state because the operations differ; copying one global login timeout across all of them is a porting error.

## RegionHandshake fields and what the viewer does with them

RegionHandshake carries the simulator's product name and SKU, region flags (sandbox, damage, mature rating bits), water height, terrain base texture UUIDs and detail texture parameters, the region's cache version, and billing and other legacy fields. The viewer uses water height for the water pool plane and for avatar swimming logic, terrain textures to build the ground surface before LayerData detail arrives, region flags to gate UI (damage indicators, maturity access), and the cache version to decide whether the per-region object cache file can be trusted. RegionHandshakeReply returns the viewer's cached-object state and feature declarations. A client that hardcodes water height at the SL default 20 metres will render OpenSim varregions and custom-water regions wrongly, because water height is per-region data, not a constant.

## Object cache file: format and invalidation

On leaving or crashing, the viewer can persist a region's static objects to an object cache file (LLSD/binary hybrid managed by LLViewerObjectList and the region's cache id). On re-entry, if the handshake cache version matches, the viewer instantiates objects from cache instantly and reconciles against fresh updates, which is why a familiar region 'pops in' complete while a new one builds object by object. Invalidation failures present as ghost objects that are not really there or missing objects that are: the cache said one thing, the simulator another, and reconciliation trusted the wrong side. Deleting the object cache for one region is a safe diagnostic; a client port should implement the same version-keyed invalidation rather than caching objects by name or by region name alone, because region names are not unique across grids.

## Interpolation mathematics the viewer actually uses

For a terse-updated object the viewer stores the last authoritative state (position P0, velocity V, acceleration A, rotation Q0, angular velocity W, timestamp t0) and extrapolates P(t) = P0 + V*dt + 0.5*A*dt^2, integrating rotation from W, until either a new update arrives or the extrapolation window expires and the object freezes at its last reckoned position. When a new update lands ahead of or behind the extrapolated pose, the viewer does not snap unless the error exceeds a threshold: it eases by blending the rendered pose toward the authoritative track over a short window, which is the visible 'rubber-band then settle' on laggy crossings. Ping time feeds the window: the viewer estimates one-way delay from circuit ping and times updates accordingly. Two consequences for porting: first, using wall-clock arrival time instead of the update's embedded timing makes extrapolation systematically late by the jitter amount; second, applying easing to avatars but not to their attachments (or vice versa) visibly tears held objects off hands, so interp policy must be per-linkset, not per-prim.

## Camera, interest, and why the simulator sends what it sends

The viewer sends AgentUpdate continuously (throttled to a few Hz when idle, faster when moving) carrying camera position and orientation, head rotation, control flags, and far-clip (draw distance). The simulator uses camera and far plane to decide which objects to stream and at what priority — your draw distance literally shapes server-side send queues. Lowering draw distance is therefore both a client and a server load reduction, and a mobile client should treat its AgentUpdate rate and far value as protocol behaviour, not UI trivia. Interest management on the simulator side culls objects behind the camera and beyond far; the viewer's job is to handle objects appearing via full updates at the far plane without rebuild storms, which the spatial-group rebuild budget exists to absorb.

## Draw pools in detail

LLDrawPoolTerrain renders the ground surface built from LayerData heightfields with detail-texture blending and, in current builds, terrain PBR materials. LLDrawPoolTree renders legacy sculpt-and-prim trees with impostor behaviour at distance in some builds. LLDrawPoolSimple and its alpha and bump/material variants render the bulk of prim and mesh geometry from spatial group buffers. LLDrawPoolAvatar renders avatars with skinning shaders, separate from ordinary mesh because of joint palette handling and morph targets. LLDrawPoolWater renders the water plane with reflection and refraction targets when enabled. LLDrawPoolSky renders the procedural EEP sky and celestial bodies. LLDrawPoolGlow and the post chain handle bloom. Knowing the pool tells you which shader family and which settings govern a visual bug: water colour is a sky/water-settings plus water-pool question, never a texture question.

## Vertex buffer management and rebuild budgets

Spatial groups build interleaved vertex buffers (LLVertexBuffer) per draw pool type with attribute sets matched to the material type: position, normal, tangent for normal-mapped and PBR, texcoords (two channels where materials need them), colour, and skin weights for rigged geometry. A group marks itself dirty on object updates that change geometry, material, or transform beyond a threshold; LLPipeline rebuilds a bounded amount of buffer data per frame, prioritising near and large groups. This is why entering a mesh-dense region shows geometry 'filling in' over seconds even after all assets are downloaded: the data is present, the buffers are queued. Buffer memory is a real budget on mobile GPUs, and a port that rebuilds every group every frame will thermal-throttle a phone in minutes.

## HUD, attachments, and render order exceptions

HUD attachments render in a separate orthographic pass after the world, using their own spatial partition, and are exempt from most world culling and lighting — they use simplified lighting so HUD text stays readable. In-world attachments render with the avatar, inherit its interpolation, and are subject to avatar complexity accounting. Complexity (render weight) is computed from geometry, texture, and shader features per avatar; viewers can render over-limit avatars as simplified impostors ('jelly dolls') per the AvatarComplexity settings. The number is an estimate with known distortions — Black Dragon's non-standard complexity values are the documented example of a fork changing the metric — so cross-viewer complexity comparisons are only meaningful within one viewer's accounting.

## Crashes: the common viewer crash families

Viewer crashes cluster: GPU driver and shader compile failures at preset changes; texture decode of malformed JPEG2000 in worker threads (isolated so a bad asset should log, not crash — a crash here is a decoder bug); mesh parsing of malformed LLMesh skin data; CEF media crashes that should be contained to the media plugin process; and null spatial-group dereferences during region teardown, the classic crossing-crash family where an object is deleted while a rebuild is queued. Crash logs plus the last llstartup or region state in SecondLife.log usually name the family before any debugger does. TPV policy expects crash handling that does not leak credentials in dumps — login form contents must never be in a crash report.

## Firestorm and Alchemy internals worth knowing

Firestorm adds, inside the same architecture: the LSL preprocessor in the script editor (Boost.Wave), RLVa as a restriction layer over outfit and attachment operations, an area-search index over the object list, a more aggressive set of render debug toggles, and OpenSim grid management. Alchemy modernises the build (CMake presets and vcpkg) and tracks upstream rendering changes sooner, and is the better reference for how the codebase builds without Autobuild. Singularity and V1-lineage viewers keep an older forward pipeline; Cool VL carries Henri Beauchamp's long-running patch set including HTTP and OpenJPEG fixes that upstream has periodically absorbed. When a behaviour differs between two viewers on the same region, diff in this order: settings defaults, pipeline mode (deferred vs forward), codec (Kakadu vs OpenJPEG), then code.

## Appendix B: settings index, first 260 documented settings (name and comment)

Extracted verbatim from the shipped settings.xml. Use it to find the exact setting name before writing code that reads or documents one — setting names are API surface and typos fail silently to defaults.

- `ImporterDebugVerboseLogging` — Enable debug output to more precisely identify sources of import errors. Warning: the output can slow down import on many machines.

- `ImporterLegacyMatching` — Enable index based model matching.

- `ImporterModelLimit` — Limits amount of importer generated (when over 8 faces) models for dae and gltf files

- `ImporterDebugMode` — At 0 does nothing, at 1 dumps skinning data near orifinal file, at 2 dumps skining data and positions/weights of first 5 models, at 3 dumps skinning data and models as llsd

- `ImporterPreprocessDAE` — Enable preprocessing for DAE files to fix some ColladaDOM related problems (like support for space characters within names and ids).

- `IMShowTime` — Enable(disable) timestamp showing in the chat.

- `IMShowNamesForP2PConv` — Enable(disable) showing of a names in the chat.

- `CrashHostUrl` — A URL pointing to a crash report handler; overrides cluster negotiation to locate crash handler.

- `AFKTimeout` — Time before automatically setting AFK (away from keyboard) mode (seconds, 0=never).         Valid values are: 0, 120, 300, 600, 1800

- `AckCollectTime` — Ack messages collection and grouping time

- `AdminMenu` — Enable the debug admin menu from the main menu.  Note: This will just allow the menu to be shown; this does not grant admin privileges.

- `ActiveFloaterTransparency` — Transparency of active floaters (floaters that have focus)

- `AdvanceSnapshot` — Display advanced parameter settings in snaphot interface

- `AgentPause` — Ask the simulator to stop updating the agent while enabled

- `AlertedUnsupportedHardware` — Set if there's unsupported hardware and we've already done a notification.

- `AllowMultipleViewers` — Allow multiple viewers.

- `AllowTapTapHoldRun` — Tapping a direction key twice and holding it down makes avatar run

- `AnalyzePerformance` — Request performance analysis for a particular viewer run

- `AnimateTextures` — Enable texture animation (debug)

- `AppearanceCameraMovement` — When entering appearance editing mode, camera zooms in on currently selected portion of avatar

- `ApplyColorImmediately` — Preview selections in color picker immediately

- `TextureLivePreview` — Preview selections in texture picker or material picker immediately

- `ArrowKeysAlwaysMove` — While cursor is in chat entry box, arrow keys still control your avatar

- `AuctionShowFence` — When auctioning land, include parcel boundary marker in snapshot

- `AudioLevelAmbient` — Audio level of environment sounds

- `AudioLevelDoppler` — Scale of the Doppler effect on moving sounds (1.0 = normal, 0 = off, higher = stronger)

- `AudioLevelMaster` — Master audio level, or overall volume

- `AudioLevelMedia` — Audio level of parcel Media

- `AudioLevelMic` — Audio level of microphone input

- `AudioLevelMusic` — Audio level of streaming music

- `AudioLevelRolloff` — Scale of the distance fall-off of sounds (1.0 = normal, 0 = none, higher = faster)

- `AudioLevelSFX` — Audio level of in-world sound effects

- `AudioLevelUI` — Audio level of UI sound effects

- `AudioLevelUnderwaterRolloff` — Same as AudioLevelRolloff, while the camera is underwater

- `AudioLevelVoice` — Audio level of voice chat

- `AudioLevelWind` — Audio level of wind noise when standing still

- `AudioStreamingMusic` — Enable streaming audio

- `AutoReplace` — Replaces keywords with a configured word or phrase

- `AutoAcceptNewInventory` — Automatically accept new notecards/textures/landmarks

- `AutoLogin` — Login automatically using last username/password combination

- `AutoMimeDiscovery` — Enable viewer mime type discovery of media URLs

- `AutoPilotLocksCamera` — Keep camera position locked when avatar walks to selected position

- `AutoSnapshot` — Update snapshot when camera stops moving, or any parameter changes

- `RenderSnapshotNoPost` — Disable tone mapping and exposure correction when snapshot is being rendered

- `AutomaticFly` — Fly by holding jump key or using "Fly" command (FALSE = fly by using "Fly" command only)

- `RecentJumpThresholdSecs` — Seconds after jump input during which landing finish-anim is suppressed to avoid interrupting rapid successive jumps.

- `AvatarAxisDeadZone0` — Avatar axis 0 dead zone.

- `AvatarAxisDeadZone1` — Avatar axis 1 dead zone.

- `AvatarAxisDeadZone2` — Avatar axis 2 dead zone.

- `AvatarAxisDeadZone3` — Avatar axis 3 dead zone.

- `AvatarAxisDeadZone4` — Avatar axis 4 dead zone.

- `AvatarAxisDeadZone5` — Avatar axis 5 dead zone.

- `AvatarAxisScale0` — Avatar axis 0 scaler.

- `AvatarAxisScale1` — Avatar axis 1 scaler.

- `AvatarAxisScale2` — Avatar axis 2 scaler.

- `AvatarAxisScale3` — Avatar axis 3 scaler.

- `AvatarAxisScale4` — Avatar axis 4 scaler.

- `AvatarAxisScale5` — Avatar axis 5 scaler.

- `AvatarFeathering` — Avatar feathering (less is softer)

- `AvatarWelcomePack` — Avatar Welcome Pack contents

- `AvatarBakedTextureUploadTimeout` — Specifes the maximum time in seconds to wait before sending your baked textures for avatar appearance.  Set to 0 to disable and wait until all baked textures are at highest resolution.

- `AvatarRotateThresholdSlow` — Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving slowly (degrees)

- `AvatarRotateThresholdFast` — Angle between avatar facing and camera facing at which avatar turns to face same direction as camera, when moving fast (degrees)

- `AvatarPhysics` — Enable avatar physics.

- `BackgroundYieldTime` — Amount of time to yield every frame to other applications when SL is not the foreground window (milliseconds)

- `BrowserIgnoreSSLCertErrors` — FOR TESTING ONLY: Tell the built-in web browser to ignore SSL cert errors.

- `BrowserEnableJSObject` — (WARNING: Advanced feature. Use if you are aware of the implications). Enable or disable the viewer to Javascript bridge object.

- `BlockAvatarAppearanceMessages` — Ignores appearance messages (for simulating Ruth)

- `BrowserProxyAddress` — Address for the Web Proxy]

- `HttpProxyType` — Proxy type to use for HTTP operations

- `Socks5AuthType` — Selected Auth mechanism for Socks5

- `BuildAxisDeadZone0` — Build axis 0 dead zone.

- `BuildAxisDeadZone1` — Build axis 1 dead zone.

- `BuildAxisDeadZone2` — Build axis 2 dead zone.

- `BuildAxisDeadZone3` — Build axis 3 dead zone.

- `BuildAxisDeadZone4` — Build axis 4 dead zone.

- `BuildAxisDeadZone5` — Build axis 5 dead zone.

- `BuildAxisScale0` — Build axis 0 scaler.

- `BuildAxisScale1` — Build axis 1 scaler.

- `BuildAxisScale2` — Build axis 2 scaler.

- `BuildAxisScale3` — Build axis 3 scaler.

- `BuildAxisScale4` — Build axis 4 scaler.

- `BuildAxisScale5` — Build axis 5 scaler.

- `BuildFeathering` — Build feathering (less is softer)

- `BulkChangeIncludeAnimations` — Bulk permission changes affect animations

- `BulkChangeIncludeBodyParts` — Bulk permission changes affect body parts

- `BulkChangeIncludeClothing` — Bulk permission changes affect clothing

- `BulkChangeIncludeGestures` — Bulk permission changes affect gestures

- `BulkChangeIncludeNotecards` — Bulk permission changes affect notecards

- `BulkChangeIncludeObjects` — Bulk permission changes affect objects

- `BulkChangeIncludeScripts` — Bulk permission changes affect scripts

- `BulkChangeIncludeSounds` — Bulk permission changes affect sounds

- `BulkChangeIncludeTextures` — Bulk permission changes affect textures

- `BulkChangeIncludeSettings` — Bulk permission changes affect environment settings

- `BulkChangeIncludeMaterials` — Bulk permission changes affect materials

- `BulkChangeEveryoneCopy` — Bulk changed objects can be copied by everyone

- `BulkChangeNextOwnerCopy` — Bulk changed objects can be copied by next owner

- `BulkChangeNextOwnerModify` — Bulk changed objects can be modified by next owner

- `BulkChangeNextOwnerTransfer` — Bulk changed objects can be resold or given away by next owner

- `BulkChangeShareWithGroup` — Bulk changed objects are shared with the currently active group

- `BulkUpload2KTextures` — Bulk upload scales textures to 2K if true, to 1K if false

- `BuyCurrencyHTML` — Use HTML based L$ packs floater instead of legacy XUI version

- `BuyCurrencyPacksURL` — URL for the L$ packs purchase floater

- `BuyCurrencyAddPaymentURL` — URL the viewer probes at login; a 200 means the L$ packs floater handles residents without a payment method

- `PaymentMethodURL` — URL for adding a payment method

- `PaymentMethodStagingURL` — URL for adding a payment method on the Damballah

- `EnableButtonFlashing` — Allow UI to flash buttons to get your attention

- `EnableDiscord` — When set, connect to Discord to enable Rich Presence

- `ShowDiscordActivityDetails` — When set, show avatar name on Discord Rich Presence

- `ShowDiscordActivityState` — When set, show location on Discord Rich Presence

- `EnableDiskCacheDebugInfo` — When set, display additional cache debugging information

- `DiskCachePercentOfTotal` — The percent of total cache size (defined by CacheSize) to use for the disk cache (ex: asset storage, excludes textures)

- `DiskCacheDirName` — The name of the disk cache (within the standard Viewer disk cache directory)

- `CacheLocation` — Controls the location of the local disk cache

- `CacheLocationTopFolder` — Controls the top folder location of the the local disk cache

- `CacheSize` — Controls amount of hard drive space reserved for local file caching in MB

- `CacheValidateCounter` — Used to distribute cache validation

- `CameraMouseWheelZoom` — Camera zooms in and out with mousewheel

- `CameraAngle` — Camera field of view angle (Radians)

- `CameraOffset` — Render with camera offset from view frustum (rendering debug)

- `CameraOffsetBuild` — Default camera position relative to focus point when entering build mode

- `CameraOffsetRearView` — Initial camera offset from avatar in Rear View

- `CameraOffsetScale` — Scales the default offset

- `CameraZoomFraction` — Mousewheel driven fraction of zoom

- `CameraPosOnLogout` — Camera position when last logged out (global coordinates)

- `RestoreCameraPosOnLogin` — Reset camera position to location at logout

- `CameraPositionSmoothing` — Smooths camera position over time

- `CameraFocusTransitionTime` — How many seconds it takes the camera to transition between focal distances

- `CameraMaxCoF` — Maximum camera circle of confusion for DoF effect

- `CameraFNumber` — Camera f-number value for DoF effect

- `CameraFocalLength` — Camera focal length for DoF effect (in millimeters)

- `CameraFieldOfView` — Vertical camera field of view for DoF effect (in degrees)

- `CertStore` — Specifies the Certificate Store for certificate trust verification

- `ChatAutocompleteGestures` — Auto-complete gestures in nearby chat

- `LetterKeysFocusChatBar` — When printable characters keys (possibly with Shift held) are pressed, the chatbar takes focus

- `ChatBubbleOpacity` — Opacity of chat bubble background (0.0 = completely transparent, 1.0 = completely opaque)

- `ChatFontSize` — Size of chat text in chat console (0 = small, 1 = big)

- `ChatFullWidth` — Chat console takes up full width of SL window

- `ChatLoadGroupMaxMembers` — Max number of active members we'll show up for an unresponsive group

- `ChatOnlineNotification` — Provide notifications for when friend log on and off of SL

- `CheesyBeacon` — Enable cheesy beacon effects

- `ClientSettingsFile` — Client settings file name (per install).

- `ConversationSortOrder` — Specifies sort key for conversations

- `CloseChatOnReturn` — Close chat after hitting return

- `CmdLineChannel` — Command line specified channel name

- `CmdLineGridChoice` — The user's grid choice or ip address.

- `CmdLineUpdateService` — Override the url base for the update query.

- `CmdLineHelperURI` — Command line specified helper web CGI prefix to use.

- `CmdLineLoginURI` — Command line specified login server and CGI prefix to use.

- `CmdLineLoginLocation` — Startup destination requested on command line

- `CmdLineSkipUpdater` — Command line skip updater check.

- `ConnectAsGod` — Log in a god if you have god access.

- `ConnectionPort` — Custom connection port number

- `ConnectionPortEnabled` — Use the custom connection port?

- `ConsoleBackgroundOpacity` — Opacity of chat console (0.0 = completely transparent, 1.0 = completely opaque)

- `ConsoleBufferSize` — Size of chat console history (lines of chat)

- `ConsoleMaxLines` — Max number of lines of chat text visible in console.

- `CookiesEnabled` — Accept cookies from Web sites?

- `BrowserJavascriptEnabled` — Enable Javascript in the built-in Web browser?

- `BrowserFileAccessFromFileUrls` — Allow access to local files via file urls in the embedded browser

- `BrowserPluginsEnabled` — Enable Web plugins in the built-in Web browser?

- `CoroutineStackSize` — Size (in bytes) for each coroutine stack

- `CrashOnStartup` — User-requested crash on viewer startup

- `CreateToolKeepSelected` — After using create tool, keep the create tool active

- `CurlRequestTimeOut` — Max idle time of a curl request before killed (requires restart)

- `Cursor3D` — Treat Joystick values as absolute positions (not deltas).

- `CurrentGrid` — Currently Selected Grid

- `DebugAnimatedObjects` — Show info related to animated objects

- `DebugObjectLODs` — Show info related to lod calculations for attached or animated objects

- `DebugSelectionLODs` — Force selection to show specific LOD, -1 for off, 0 - lowest, 4 - high.

- `AnimatedObjectsAllowLeftClick` — Allow left-click interaction with animated objects. Uncertain how much performance impact this will have.

- `AnimatedObjectsMaxLegalOffset` — Max visual offset between object position and rendered position

- `AnimatedObjectsMaxLegalSize` — Max bounding box size for animated object's rendered position

- `AvatarExtentRefreshPeriodBatch` — how many frames do we spread over by default when refreshing extents (default is 4)

- `AvatarExtentRefreshMaxPerBatch` — how many avatars do we want to handle in total per batch (default is 5)

- `DebugAvatarAppearanceMessage` — Dump a bunch of XML files when handling appearance messages

- `DebugAvatarExperimentalServerAppearanceUpdate` — Experiment with sending full cof_contents instead of cof_version

- `DebugAvatarAppearanceServiceURLOverride` — URL to use for baked texture requests; overrides value returned by login server.

- `DebugAvatarJoints` — List of joints to emit additional debugging info about.

- `DebugAvatarRezTime` — Display times for avatars to resolve.

- `DebugAvatarLocalTexLoadedTime` — Display time for loading avatar local textures.

- `DebugAvatarCompositeBaked` — Colorize avatar meshes based on baked/composite state.

- `DebugBeaconLineWidth` — Size of lines for Debug Beacons

- `DebugForceAppearanceRequestFailure` — Request wrong cof version to test the failure path for server appearance update requests.

- `DebugHideEmptySystemFolders` — Hide empty system folders when on

- `DebugPermissions` — Log permissions for selected inventory items

- `DebugPluginDisableTimeout` — Disable the code which watches for plugins that are crashed or hung

- `DebugSession` — Request debugging for a particular viewer session

- `DebugShowAvatarRenderInfo` — Show avatar render cost information

- `DebugShowColor` — Show color under cursor

- `DebugShowMemory` — Show Total Allocated Memory

- `DebugShowRenderInfo` — Show stats about current scene

- `DebugShowRenderMatrices` — Display values of current view and projection matrices.

- `DebugShowTextureInfo` — Show inertested texture info

- `DebugShowUploadCost` — Show mesh upload cost

- `DebugShowXUINames` — Show tooltips with XUI path to widget

- `SimPendingUploads` — Mode of stat in Statistics floater

- `DebugStatModeSimTotalUnackedBytes` — Mode of stat in Statistics floater

- `DebugStatModeSimFrameMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimNetMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSimPhysicsMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSimOtherMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimAgentMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimImagesMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimScriptMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSpareMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSimPhysicsStepMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSimPhysicsShapeUpdateMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSimPhysicsOtherMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimSleepMsec` — Mode of stat in Statistics floater

- `DebugStatModeSimPumpIOMsec` — Mode of stat in Statistics floater

- `DebugViews` — Display debugging info for views.

- `DebugWindowProc` — Log windows messages

- `DefaultFemaleAvatar` — Default Female Avatar

- `DefaultLoginLocation` — Startup destination default (if not specified on command line)

- `DestinationGuideURL` — Destination guide contents

- `DisableCameraConstraints` — Disable the normal bounds put on the camera by avatar position

- `DisableCrashLogger` — Do not send crash report to Linden server

- `MouseWarpMode` — Controls warping of the mouse to the center of the screen during alt-zoom and mouse look. Useful with certain input devices, mouse sharing programs like Synergy, or running under Parallels. 0 - automatic, 1 - on, 2 - off

- `DisableExternalBrowser` — Disable opening an external browser.

- `HeadlessClient` — Run in headless mode by disabling GL rendering, keyboard, etc

- `DisableTextHyperlinkActions` — Disable highlighting and linking of URLs in XUI text boxes

- `RenderVSyncEnable` — Update frames between display scans (FALSE = Update frames as fast as possible).

- `EnableGroupChatPopups` — Enable Incoming Group Chat Popups

- `UseGroupMemberPagination` — Enable pagination of group memeber list 50 members at a time.

- `DisplayTimecode` — Display timecode on screen

- `Disregard128DefaultDrawDistance` — Whether to use the auto default to 128 draw distance

- `Disregard96DefaultDrawDistance` — Whether to use the auto default to 96 draw distance

- `DoubleClickAutoPilot` — (Obsolete)Enable double-click auto pilot

- `DoubleClickTeleport` — Enable double-click to teleport where allowed (afects minimap and people panel)

- `DoubleClickShowWorldMap` — Enable double-click to show world map from mini map

- `DynamicCameraStrength` — Amount camera lags behind avatar motion (0 = none, 30 = avatar velocity)

- `EditCameraMovement` — When entering build mode, camera moves up above avatar

- `EditLinkedParts` — Select individual parts of linked objects

- `MinObjectsForUnlinkConfirm` — Minimum amount of objects in linkset for showing confirmation dialog

- `EffectScriptChatParticles` — 1 = normal behavior, 0 = disable display of swirling lights when scripts communicate

- `EnableGrab` — Use Ctrl+mouse to grab and manipulate objects

- `EnableAltZoom` — Use Alt+mouse to look at and zoom in on objects

- `DebugShowControllerState` — Display internal controller state values

- `GameControl` — Game controller settings: global per-mode action mappings plus per-device hardware config. Empty means use built-in defaults.

- `EnableGestureSounds` — Play sounds from gestures

- `EnableCollisionSounds` — Play sounds on collision

- `EnableMouselook` — Allow first person perspective and mouse control of camera

- `EnableUIHints` — Toggles UI hint popups

- `EnableVoiceChat` — Enable talking to other residents with a microphone

- `EventURL` — URL for Event website, displayed in the event floater

- `MainWorkTime` — Max time per frame devoted to mainloop work queue (in milliseconds)

- `FirstPersonAvatarVisible` — Display avatar and attachments below neck while in mouselook

- `FirstRunThisInstall` — Specifies that you have not run the viewer since you performed a clean install

- `FirstLoginThisInstall` — Specifies that you have not logged in with the viewer since you performed a clean install

- `FirstSelectedDisabledPopups` — Return false if there is not disabled popup selected in the list of floater preferences popups

- `FirstSelectedEnabledPopups` — Return false if there is not enable popup selected in the list of floater preferences popups

- `FixedWeather` — Weather effects do not change over time

- `FloaterActiveSpeakersSortAscending` — Whether to sort up or down

- `FloaterActiveSpeakersSortColumn` — Column name to sort on

- `FloaterMapNorth` — Floater Map North Label

- `FloaterMapNorthEast` — Floater Map North-East Label

- `FloaterMapNorthWest` — Floater Map North-West Label

- `FloaterMapEast` — Floater Map East Label

- `FloaterMapWest` — Floater Map West Label

Appendix B entries: 260 settings (subset; the full settings.xml ships well over a thousand).
