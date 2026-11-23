---
name: secondlife_assets_mesh_texture
description: "Handle Second Life prims, sculpties, mesh, textures, PBR materials, Bakes on Mesh, Animesh, and EEP across viewer, LibreMetaverse, and Blender pipelines."
---

# Second Life Assets Mesh and PBR

## Keep the asset identities straight

- Track asset_id, item_id, and folder_id as different UUIDs for every object, and keep asset types and inventory types as separate enums synced from viewer llassettype.h and llinventorytype.h and LibreMetaverse Types and Assets.

- Log UUID and cap URL when an asset is missing or grey, not the display name, because names are not unique and the asset server is HTTP.

- Choose the upload path the viewer uses for that type: caps such as NewFileAgentInventory and AIS3 updates for modern inventory, with legacy UDP AssetUploadRequest only where viewer code still uses it.

## Build geometry in the format the grid stores

- Treat prims as parametric objects defined by PrimitiveParams and ObjectUpdate fields for profile, hollow, twist, taper, shear, and path cuts, and copy a proven codec such as viewer llvolume or LibreMetaverse PrimMesher instead of reinventing the packed forms, because UDP, LLSD, and internal packings differ.

- Treat sculpties as legacy: a texture encodes XYZ vertices on a fixed grid, tessellated by viewer and OpenSim, and new content should be mesh.

- Author mesh as Collada .dae from Blender at metric scale 1.0 with explicit High, Medium, Low, and Lowest LOD models plus a physics shape, upload through the viewer mesh uploader in llmeshrepository and model loader code, and remember the server stores LLMesh binary not Collada or glTF.

- Use glTF as import, export, and PBR source format through LibreMetaverse.ModelFormats for Collada, glTF, and OBJ, and MeshFoundry for geometry and rigging, not as the wire format fetched via GetMesh and GetMesh2 caps.

## Decode textures as JPEG2000

- Fetch textures over the GetTexture HTTP cap with range requests and progressive discard levels, and drive fetch priority by discard level and viewer texture cache logic.

- Decode JPEG2000 codestreams with Kakadu in Linden Lab builds or OpenJPEG in open builds, and suspect the codec first when the same texture looks different across viewers, because OpenJPEG and Kakadu differ in partial decode artefacts and speed and Lumiya ships an old OpenJPEG 1.5.

## Apply current materials and appearance

- Support legacy diffuse, normal, and specular plus shininess and current glTF 2.0 PBR materials as LLGLTFMaterial inventory assets with base colour, metallic roughness, normal, emissive, and occlusion, applied via prim params and the RenderMaterials area in viewer code.

- Implement EEP as inventory environment assets for sky, water, and day cycles fetched via EnvironmentSettings and ExtEnvironment caps, replacing old Windlight settings.

- Handle Bakes on Mesh by managing wearable bake channels and universal wearables correctly, because server side compositing of system avatar layers onto mesh bodies bakes grey when appearance data is wrong.

- Handle Animesh as rigged mesh objects with AnimatedObject parameters and ObjectAnimation and AvatarAnimation messages, animated as pseudo avatars rather than attachments.

## Use the Blender pipeline safely

- Export from Blender with metric units, applied transforms, and separate LOD and physics meshes, test uploads on Aditi before paying upload fees on Agni, and use Avastar as a paid closed Machinimatrix addon for SL armature, weighting, and Bento bones when you need it, knowing Primstar is legacy sculptie tooling and neither has an open GitHub repo.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for viewer mesh and texture code and LibreMetaverse ModelFormats and MeshFoundry.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Second Life Viewer](https://github.com/secondlife/viewer) for llmeshrepository, texture cache, GLTF material, EEP, and Bakes on Mesh code.

- [LibreMetaverse](https://github.com/cinderblocks/libremetaverse) for ModelFormats, MeshFoundry, PrimMesher, and imaging libraries.


## Prim parameter reference in detail

- Shape families: PRIM_TYPE box, cylinder, prism, sphere, torus, tube, ring, and sculpt with PRIM_TYPE_SCULPT plus sculpt texture UUID and stitching type, each with hole shapes and size, hole size, twist, taper, shear, path cut, profile cut, hollow, and slice parameters packed into PRIM_* calls.

- Material and face data: PRIM_TEXTURE per face with texture UUID, repeats, offsets, rotation, PRIM_NORMAL, PRIM_SPECULAR, PRIM_COLOR, PRIM_GLOW, PRIM_FULLBRIGHT, PRIM_BUMP_SHINY, PRIM_POINT_LIGHT, PRIM_FLEXIBLE, PRIM_TEXGEN, and media via PRIM_MEDIA, all face indexed so off by one face bugs are endemic.

- Extra params and physics: PRIM_PHYSICS_SHAPE_TYPE prim, convex, or none per link, PRIM_PHYSICS, PRIM_TEMP_ON_REZ, PRIM_PHANTOM, and return and land impact accounting driven by mesh and physics shape choices.

- Codec warning in detail: the same prim is represented as UDP ObjectUpdate fields, as LLSD in caps and inventory, and as internal viewer and LibreMetaverse objects with different packing for rotations, scale, and extra params, always round trip test a codec against viewer or LibreMetaverse values for tapered, twisted, and hollow shapes.

## LLMesh format in detail

- An LLMesh asset contains a header describing LOD sections and skin and physics submeshes, with high, medium, low, and lowest LOD geometry, a physics representation as convex hulls or a mesh, and skin weight data for rigged mesh.

- LOD generation in the uploader can auto generate lower LODs with triangle and vertex limits you set, and land impact is calculated from download weight, physics weight, and server weight with the highest dominating, which is why a badly decimated physics mesh surprises creators.

- Fetch path in detail: viewer requests GetMesh or GetMesh2 cap with mesh UUID, caches by UUID, and falls back through llmeshrepository retry and priority logic, and a missing cap or truncated asset renders as invisible or as a low LOD impostor.

## Texture pipeline in detail

- JPEG2000 codestream structure gives progressive resolution layers that map to discard levels: discard 0 is full resolution, higher discards are lower resolution previews decoded first for fast appearance.

- Viewer fetch prioritises by camera distance, screen area, and boost flags for avatars and HUDs in lltexturefetch and the texture cache, and cache size and bandwidth throttle settings change which textures appear sharp.

- OpenJPEG versus Kakadu in detail: Kakadu is faster and handles some partial codestreams more gracefully in Linden Lab builds, OpenJPEG builds can show different artefacts on damaged assets and slower decode on large 1024 and 2048 textures, and Cool VL ships a patched OpenJPEG 1.5 claiming fixes for partial decode LOD bugs.

- Texture sizes in practice: powers of two up to 2048 in current SL, alpha modes blend, mask with alpha cutoff, and emissive, and normal maps expected in tangent space with specific handedness that flips shading if imported wrong from Blender.

## PBR and glTF in detail

- A glTF material asset carries baseColor texture and factor, metallicRoughness texture with metalness in B and roughness in G channels, normal texture, emissive texture and factor, occlusion in the metallic roughness texture R channel per glTF spec mapping used by SL, alpha mode and cutoff, and double sided flag.

- Overrides: PBR can be applied per face via render material parameters and terrain PBR arrived after object PBR, and legacy blended materials and PBR materials coexist on different faces of the same linkset.

- Import path: author PBR in Blender Principled BSDF terms, export glTF for reference, upload textures and create the material asset in viewer, then apply, and expect viewer tonemapping and environment lighting from EEP to change the look versus Blender.

## Bakes on Mesh, Animesh, and EEP in detail

- Bakes on Mesh channels: head, upper body, lower body, eyes, hair, skirt and universal wearable layers composite system avatar textures server side and project them onto mesh attachments flagged for the matching bake channel, and the client must wear the universal wearable and set attachment bake flags or the mesh stays grey or shows the system body texture wrongly.

- Animesh in detail: a rigged mesh object with an AnimatedObject flag plays animations like an avatar using its own skeleton, counts against land impact and avatar limits differently from attachments, and is controlled by llStartObjectAnimation style calls and ObjectAnimation messages.

- EEP in detail: sky, water, and day cycle are inventory assets with shader and lighting parameters replacing Windlight presets, applied at parcel, region, and avatar level via EnvironmentSettings and ExtEnvironment, and a client that ignores EEP renders the wrong time of day and water even if geometry is perfect.

## Blender pipeline in detail

- Rigging: use the SL skeleton with Bento extension bones for fingers, tail, wings, and face when needed, Avastar provides this armature and weight tools as a paid addon from Machinimatrix, or build it manually from viewer character files and LibreMetaverse bone definitions.

- Export checklist: apply scale and rotation, triangulate or let the uploader do it knowingly, name LOD and physics meshes consistently, keep materials per face under the viewer limit of 8 faces per mesh, and keep each mesh under the vertex and triangle limits documented for the current uploader.

- Upload checklist: test on Aditi, inspect all LODs in the uploader preview at distance, set physics shape type deliberately, check land impact before and after, and only then upload on Agni where each upload costs Linden dollars.

## Debugging playbook

- Grey avatar: check bake channel wearables and COF first, then texture fetch, then materials, in that order.

- Invisible mesh: check GetMesh cap success and LLMesh parse, then LOD selection at camera distance, then alpha mode, before suspecting prim data.

- Shiny or dark PBR object: check metallic roughness channel mapping, environment EEP lighting, and normal map handedness, in that order.

- Works in one viewer not another: suspect JPEG2000 codec differences and PBR support level first, especially on V1 lineage viewers with no PBR pipeline.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/asset-inventory-enums.md` (12,641 bytes)
- `references/assets-pipeline-guide.md` (85,481 bytes)
