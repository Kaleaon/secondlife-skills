# Capabilities Reference (detailed)

Per-capability reference for the caps a client actually encounters. Cap URLs are per-region, per-session, and unguessable: request them from the seed capability on every region entry, check presence before use, and never cache across teleports. Authority order: viewer llviewerregion.cpp buildCapabilityNames and llaisapi.cpp, then this reference, then the wiki list.


## EventQueueGet

- Category: Core

- What it does: Long-poll event queue. POST LLSD {ack, done} and receive {id, events[]}. Ack only after dispatching events. A stalled loop is indistinguishable from a dead session, so supervise it with a watchdog and restart on repeated 404/499 or malformed LLSD.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## EventQueueGet2

- Category: Core

- What it does: Version 2 of the event queue with the same ack discipline. Prefer it when the region offers it and fall back to EventQueueGet.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## FetchInventory2

- Category: Inventory

- What it does: HTTP inventory fetch for agent inventory. Returns LLSD agent and skeleton plus items for requested folder IDs. Replaces most UDP fetch for browsing. Cache by folder version, not by time.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## FetchInventoryDescendents2

- Category: Inventory

- What it does: Fetch descendants of inventory folders over HTTP. Pair with FetchInventory2 for lazy tree loading in mobile clients.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## FetchLib2

- Category: Inventory

- What it does: Library inventory fetch, the Linden Library root equivalent of FetchInventory2.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## FetchLibDescendents2

- Category: Inventory

- What it does: Library descendants fetch over HTTP.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## InventoryAPIv3

- Category: Inventory AIS3

- What it does: AIS3 agent inventory operations: create, update, remove, link, and copy items and folders as LLSD calls. Viewer llaisapi.cpp is the authority for payload shapes, including link creation which must reference the target item and carry the correct type fields.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## LibraryAPIv3

- Category: Inventory AIS3

- What it does: AIS3 library operations, the library twin of InventoryAPIv3.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## IncrementCOFVersion

- Category: Inventory AIS3

- What it does: Bumps the Current Outfit Folder version after outfit changes so other sessions and the bake service see a consistent outfit. Skipping it causes stale outfits and bake mismatches across sessions.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetTexture

- Category: Content

- What it does: HTTP texture fetch by UUID with range requests mapped to JPEG2000 discard levels. The main texture path for modern clients. Handle 404 as a genuinely missing asset and log the UUID.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetMesh

- Category: Content

- What it does: HTTP mesh fetch by UUID returning LLMesh data. Parse header, LOD, physics, and skin sections per the LLMesh layout.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetMesh2

- Category: Content

- What it does: Version 2 mesh fetch. Prefer when offered, fall back to GetMesh.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetMetadata

- Category: Content

- What it does: Asset and object metadata lookup. Check viewer code for the exact LLSD keys per asset class.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetObjectCost

- Category: Content

- What it does: Land impact and cost accounting for objects and meshes. Use before rez or upload decisions in tools.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetObjectPhysicsData

- Category: Content

- What it does: Physics shape data for objects, used by cost and editing tools.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## RenderMaterials

- Category: Content

- What it does: PBR and material rendering data for regions that serve materials over caps.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## MeshData

- Category: Content

- What it does: Historical mesh data endpoint. Do not design new code around it without checking current viewer usage.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## SimulatorFeatures

- Category: Region

- What it does: LLSD feature map for the region: mesh upload limits, physics shape types, PBR support, voice configuration, and more. Query on every region entry and gate features from it instead of hardcoding.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ServerReleaseNotes

- Category: Region

- What it does: Release notes URL or text for the simulator version running the region. Useful in support and bug reports.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ProductInfoRequest

- Category: Region

- What it does: Simulator product name and SKU style information for the region.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## EnvironmentSettings

- Category: Environment

- What it does: EEP environment settings for the region and parcel. Returns the environment asset data used to render sky and water.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ExtEnvironment

- Category: Environment

- What it does: Extended EEP operations: get and set parcel and region environments with the extended payloads in viewer environment code.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## AgentPreferences

- Category: Agent

- What it does: Agent preferences including hover height and related settings.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## AgentState

- Category: Agent

- What it does: Lightweight agent state queries used by the viewer.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## AvatarRenderInfo

- Category: Agent

- What it does: Avatar rendering information used for complexity and render decisions.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## CharacterProperties

- Category: Agent

- What it does: Character properties for agents in region.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GetDisplayNames

- Category: Agent

- What it does: Resolve agent IDs to display names and usernames in bulk. Cache aggressively and respect the returned next update times.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## UpdateAgentInformation

- Category: Agent

- What it does: Update agent information fields over HTTP.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## UpdateAgentAppearance

- Category: Agent

- What it does: Appearance update path. Coordinate with COF versioning or bakes will disagree.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## HomeLocation

- Category: Agent

- What it does: Set and query the agent home location.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ChatSessionRequest

- Category: Social

- What it does: Create group and conference chat sessions. The response carries the session credentials and temp chat channel data used by group IM.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GroupAPIv1

- Category: Social

- What it does: Group data API: profiles, roles, members, and notices in LLSD form.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## GroupMemberData

- Category: Social

- What it does: Group member data download for large groups.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## StartGroupProposal

- Category: Social

- What it does: Start a group proposal vote.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## LandResources

- Category: Land

- What it does: Land and estate resource information.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## RemoteParcelRequest

- Category: Land

- What it does: Resolve a parcel by location or ID for info panels and teleports.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ParcelPropertiesUpdate

- Category: Land

- What it does: Parcel property updates over caps where offered. Verify against viewer parcel code.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## MapLayer

- Category: Map

- What it does: Legacy map tile layer information. Modern clients mostly use the map tile CDN directly.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## SearchStatRequest

- Category: Search

- What it does: Search statistics reporting from the viewer.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ViewerStats

- Category: Telemetry

- What it does: Viewer statistics submission. Respect user privacy settings before sending anything.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ViewerStartAuction

- Category: Land

- What it does: Start a land auction from the viewer.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## SimConsole

- Category: Admin

- What it does: Simulator console access. Estate and god restricted. Never expose to untrusted UI.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## NewFileAgentInventory

- Category: Upload

- What it does: Caps upload for new inventory assets: POST the asset and receive the new item and asset IDs. The modern replacement for UDP AssetUploadRequest in most flows.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## InventoryThumbnailUpload

- Category: Upload

- What it does: Upload inventory item thumbnails.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## UpdateGestureAgentInventory

- Category: Upload

- What it does: Update gesture assets in inventory.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## UpdateScriptAgent

- Category: Upload

- What it does: Upload and compile scripts to agent inventory.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## UpdateTaskInventory

- Category: Upload

- What it does: Update script and inventory inside in-world tasks (objects). Pair with the in-world editing flow and handle compile errors returned in the response.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## LSLSyntax

- Category: Scripting

- What it does: Server-side LSL syntax and help data used by script editors for the region's actual compiler version. Prefer it over stale local keyword files.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ProvisionVoiceAccountRequest

- Category: Voice

- What it does: Legacy Vivox provisioning: returns SIP credentials and voice account data for the SLVoice daemon model.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## VoiceSignalingRequest

- Category: Voice

- What it does: Voice signaling for current voice stacks. Branch on SimulatorFeatures to decide between WebRTC and Vivox flows.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ResourceCostSelected

- Category: Editing

- What it does: Cost of the current selection for editing tools.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ObjectMedia

- Category: Media

- What it does: Media on a prim data for the region.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ObjectMediaNavigate

- Category: Media

- What it does: Media navigation events for MOAP faces.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## ParcelMediaUpdate

- Category: Media

- What it does: Parcel media stream updates.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## TerrainSettings

- Category: Environment

- What it does: Region terrain and environment settings used by newer environment code.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.


## RegionObjectsCache

- Category: World

- What it does: Region object cache information for interest and streaming decisions.

- Failure handling: if the cap is absent from the seed response, disable the feature for this region and use the UDP or legacy fallback only where viewer code has one. If the cap returns an error, log the cap name, region, and LLSD error body, not the cap URL.
