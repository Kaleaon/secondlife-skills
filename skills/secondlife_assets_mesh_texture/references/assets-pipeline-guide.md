
# Second Life Content Pipeline — Deep Reference Guide

This guide covers the whole authoring path for Second Life content: Blender setup and export for mesh, LOD generation strategy with numbers, physics shape authoring, rigging and weighting for wearables and Animesh, PBR material authoring in Blender and Substance terms mapped onto SL's glTF implementation, Bakes-on-Mesh wearable authoring, Animesh authoring, EEP sky and water authoring, texture budgets, and land impact mathematics with worked examples you can check against the viewer uploader. It assumes the protocol and asset facts in the companion skills: mesh uploads as Collada .dae, the grid stores LLMesh, textures are JPEG2000, and every number the uploader shows you — land impact above all — is computed from data you control at authoring time.

## Pipeline overview: where quality and cost are decided

Almost everything users experience as 'quality' and everything landowners experience as 'cost' is decided before upload, in four authoring choices: triangle distribution across LODs, physics representation, texture resolution and reuse, and material count (faces). The uploader is a measuring instrument, not an optimiser: it reports download weight from your LOD triangle counts, physics weight from your physics shape, and server weight from object complexity, and charges the maximum as land impact. Creators who iterate against the uploader's preview on Aditi — where uploads are effectively free for testing — ship content that is cheaper and better looking than creators who upload once to Agni and accept the first number. Treat every upload as: author, preview all LODs at distance, read the three weights, fix the dominant one, re-upload.

## Blender scene setup for SL

Work in metres with scene unit scale 1.0 — SL's Collada importer assumes metres, and a model authored in centimetres arrives 100x too small or, worse, scaled via object transforms that break rigging. Apply location, rotation, and scale to the mesh before export (Ctrl+A) so object transforms are identity; the uploader and the skeleton both assume it. Set the origin deliberately: for wearables the origin must match the avatar bone the mesh is rigged to; for rezzables the origin is where the object pivots and where llGetPos reports, so put it at the natural grab or floor point. Name objects and materials semantically (LOD and physics matching in the uploader is by name and by material where auto-generation is off). Keep a clean export copy of the .blend with modifiers unapplied in the file but applied on export, so you can re-export after fixes without rebuilding.

## Export settings: Collada that the uploader likes

Export .dae with triangulate on (the uploader triangulates anyway; doing it in Blender lets you see the actual triangles), apply modifiers, include UVs and vertex colours only if used, and export normals as authored — smooth versus flat shading is normal data, and the uploader preserves it. For rigged mesh, export with the armature and skin weights, deform bones only where the toolchain offers it, and never export with the armature in a posed state unless the pose is the intended bind. Common export failures and their signatures: mesh arrives rotated 90 degrees (axis conversion mismatch — fix in exporter axis settings, not by rotating the model), mesh arrives inside-out (negative scale was applied — mirror via mesh, not object scale), normals look faceted despite smooth shading (normals were not exported or were overwritten by an edge-split modifier at export), and weighted mesh collapses to origin in-world (bind pose or bone naming mismatch against avatar_skeleton.xml names).

## Anatomy of an upload: what the uploader computes

The mesh uploader (viewer llmeshrepository / model upload floater) parses the .dae into per-face geometry for up to four LODs plus a physics representation plus skin data. It shows triangle and vertex counts per LOD, generates missing LODs by decimation if asked, generates a physics shape by convex decomposition (HACD lineage) or accepts your physics mesh, calculates weights, and quotes the Linden dollar upload fee from model complexity. The fee and the land impact both rise with the same inputs, so the uploader screen is your cost dashboard: read high-LOD triangles, the generated LOD ratios, physics hull count and physics triangles, and the three weights before confirming. Upload to Aditi first and walk around the result at 5, 20, and 60 metres — LOD swaps and physics errors are visible at distance and underfoot, not in the preview window.

## LOD strategy: ratios, distances, and the silhouette rule

LOD swap distances scale with object size: a large object swaps later, which is why big builds need honest medium and low LODs while a small accessory can get away with aggressive reduction. A serviceable default ratio set for a hero object is High 100 percent, Medium about 50 percent of triangles, Low about 25 percent, Lowest about 10 to 12 percent or a simple impostor-like shell — but ratios serve the silhouette rule, which outranks them: at each LOD, preserve the outline, the holes, and the parts users recognise, and spend the reduction on flat interior detail, small bevels, and hidden faces. Decimation that preserves volume but destroys the outline (the classic melted look) comes from generic simplification with no silhouette protection; hand-reduce hero objects in Blender with decimate modifiers plus manual cleanup, and reserve full auto-generation for background clutter. Test swaps by flying away slowly in the viewer on Aditi: a good LOD chain is invisible in motion; a pop you can see at normal viewing distance is a failed LOD, whatever its triangle count.

## LOD worked example: a chair

A dining chair authored at 4,800 triangles high LOD (legs, spindles, bevelled seat). Medium hand-reduced to 2,200 by collapsing spindle pairs and removing underside bevels — silhouette from front, back, and side unchanged. Low at 900: spindles become a single slatted panel texture suggestion in geometry (four posts plus rails), seat loses bevel, legs go hexagonal. Lowest at 220: a box-form chair readable at 60 metres. Physics: a dedicated 48-triangle shape (four leg boxes, seat box, back box) instead of decomposition of the visual mesh. In the uploader this class of model typically lands at a download weight driven by the medium/low counts rather than the high, because streaming cost weights the LODs a viewer actually downloads at typical distances — which is the mechanical reason hand LODs beat a single pretty high LOD with auto-generated mush below it: you are paying for the whole chain, not the showcase level.

## Physics shapes: the three representations and when each wins

At upload and in prim settings a mesh has a physics shape type: Prim (use the physics mesh or hulls you supplied), Convex Hull (one hull generated from the visual mesh), or None (phantom-like for physics, still collides with nothing — used for foliage, decor, and anything avatars should walk through). Author a physics mesh when avatars interact with the shape: doorways they pass through, floors they stand on, furniture they sit near, vehicles. Rules for physics meshes: make them from boxes and simple forms, keep every hole a user walks through actually open (a convex decomposition will happily fill your doorway), keep triangle counts tiny (tens to low hundreds), and align the physics mesh origin and scale exactly with the visual mesh or collisions offset visibly. Convex hull per-object is right for solid props (rocks, crates, statues). Decomposition quality settings trade hull count against fit: more hulls fit better and cost more physics weight; a doorway needs the hulls, a boulder does not.

## Physics weight and walkability testing

Physics weight grows with physics triangle count, hull count and complexity, and whether the object is set physical (dynamic objects cost more to simulate). Test walkability on Aditi with an avatar, not by eye: walk through every opening, jump against every wall, stand on every floor at multiple points, and rez a physical ball and roll it across floors to find seams and phantom triangles. Vehicles need the floor test at speed — a physics seam that trips an avatar at walking pace flips a vehicle at thirty. In OpenSim, remember the mesher pairing rule from the server guide: the same physics mesh under Meshmerizer versus ubODEMeshmerizer can produce different effective collisions, so physics testing is per-grid-engine for serious content.

## Rigging for wearables: skeleton, weights, and Bento

Wearable mesh rigs to the avatar skeleton defined in avatar_skeleton.xml: the classic bones (mPelvis, mTorso, mChest, mNeck, mHead, limbs) plus Bento extension bones for fingers (mFace* and hand chains), tail, wings, and hind limbs. Weight rules that decide whether a garment moves like cloth or like armour: weights must be normalised, each vertex influenced by at most four bones (the SL limit the uploader enforces), transitions at joints should span several edge loops with graduated weights, and the bind pose is the skeleton's T-pose-ish default — rig in that pose. Avastar (paid, Machinimatrix) provides the armature, weight-copying from the system body, and fitted-mesh slider support; a manual Blender rig must reproduce bone names exactly, because a single renamed bone silently unriggs that limb in-world. Fitted mesh additionally deforms with shape sliders via the collision-volume bones — the fat and muscle sliders move collision bones, and fitted clothing weights to them; standard rigged mesh follows joint positions only and will clip on extreme shapes.

## Applique, standard sizing, and shape extremes

Because fitted mesh follows collision bones and standard mesh does not, creators ship either fitted versions, multiple standard sizes, or designs with enough clearance to survive shape variation. Test wearables on shape extremes on Aditi: tallest and shortest, maximum and minimum muscle and body fat sliders, and both a male and female base shape, because clipping that is invisible on your test shape is the top return reason for clothing. Alpha layers (system clothing alphas) remain part of the system: a wearable that needs the body hidden under it should ship or reference an alpha, and BoM-era bodies change which alpha approach works (see the BoM section).

## Texture authoring: resolution is a budget, not a virtue

Every texture is JPEG2000 on the grid whatever you upload (the uploader converts PNG/TGA/JPEG), stored at powers of two up to 2048x2048. Choose resolution by on-screen size: a texture on a 0.5 m object seen at arm's length earns 512; a building facade earns 1024 or a tiling 512; 2048 is for large hero surfaces and avatar skins where users zoom to centimetres. Memory math is exact and unforgiving — see the budget tables in the appendix: a 1024x1024 texture with mipmaps costs about 5.6 MB of GPU memory in RGBA terms before compression behaviour, a 2048 about 22 MB, and a scene's texture working set is the sum over everything visible, which is the viewer's TextureMemory budget and the reason texture-heavy regions thrash on modest GPUs. Reuse beats resolution: one 1024 atlas shared by a whole furniture set costs less than four private 512s and loads as one fetch.

## Texture budgets per content type (working targets)

Avatar skin set (head, upper, lower plus BoM-composited layers): authored at 1024 per bake channel is the ecosystem norm; 2048 skins exist and cost four times the memory for detail visible only in close-up photography. Clothing: 1024 for a hero garment's main fabric, 512 for secondary pieces, with normal maps at half the diffuse resolution as a safe default. Furniture and props: 512 diffuse typical, 256 for small clutter, tiling textures at 256 or 512 with world-space repeats instead of unique bakes. Buildings: tiling 512s plus trim atlases beat unique 2048 bakes on every metric users feel (load time, memory, sharpness at distance via mipmaps). Terrain-adjacent ground textures: 512 tiling. These are targets to argue with deliberately, not laws — a photography studio prop earns more texture than a background crate, and the budget tables let you price the argument.

## Normal, specular, and legacy materials

Legacy materials pair a diffuse texture with an optional normal map and specular map plus shininess and environment intensity in the material floater (and PRIM_SPECULAR / PRIM_NORMAL via scripts). Tangent-space normal maps must match SL's handedness: a normal map authored for a different engine's convention lights from the wrong side (the classic symptom is bumps that look carved-in under SL sun). The specular map's RGB carries specular colour and its alpha carries environment reflection strength in the legacy model, while shininess is a separate scalar — content that packs channels assuming a PBR layout will misbehave as a legacy material and vice versa. When in doubt about a second-hand asset's maps, test it at noon and midnight EEP on Aditi and look at the shading, not the file names.

## PBR authoring mapped to SL glTF

Author PBR in Blender's Principled BSDF or Substance Painter with a glTF export preset and the mapping is nearly one-to-one onto SL's LLGLTFMaterial: BaseColor texture and factor to Principled Base Color; Metallic to Metallic; Roughness to Roughness; the packed metallic-roughness texture SL expects follows glTF packing (roughness in G, metalness in B) with occlusion in R of that same texture per SL's mapping; Normal to the normal map slot (tangent space, +Y glTF convention as exported by standard presets); Emissive texture and factor to Emission. Alpha mode maps to glTF alphaMode: OPAQUE, MASK (with alphaCutoff) for foliage and lace, BLEND only where true translucency is needed because blend faces cost the transparent pass. Double-sided maps to the material's double-sided flag — set it for leaves, curtains, and open garments, and leave it off for solid objects to save fill. In Substance, the glTF PBR Metal Roughness preset with an SL-targeted export (or a channel repack for occlusion) produces upload-ready maps; upload the textures, create the material asset in the viewer, and apply it per face.

## PBR pitfalls specific to SL

Three recurring ones. First, environment lighting is EEP-driven, so a material balanced under Blender's HDRI will read differently under an SL midday sky — judge metals in-world, because metals are almost entirely environment reflections and an EEP sky with weak ambient makes correct metal look black. Second, SL's legacy content pipeline means a PBR material on one face and legacy materials on neighbouring faces of the same linkset shade through related but not identical paths; seams at face boundaries are a known mixed-content look to design around. Third, texture colour space: base colour and emissive are sRGB, data maps (normal, metallic-roughness) are linear — uploading a data map through a path that treats it as sRGB (or vice versa) produces the washed-out or overly rough look that gets misdiagnosed as a lighting bug.

## Bakes on Mesh wearable authoring

A BoM-ready mesh body or attachment declares, per face or per material, which bake channel it displays (head, upper, lower, eyes, hair, skirt, universal) — in practice via the viewer's BoM workflow and the attachment's texture being set to the bake placeholder for that channel. Authoring consequences: the mesh's UVs for a BoM channel must be the system avatar UV layout for that channel, because the bake is composited in system UV space from worn skins, tattoos, and clothing layers; a custom-UV body cannot consume standard bakes and must use applier-style private textures instead, which is the fundamental fork between BoM bodies (system-UV, wear-anything) and applier bodies (custom-UV, brand-locked layers). Universal wearables and universal layers let one texture asset serve across channels. Test BoM content by wearing a loud test skin and tattoo layer: if the tattoo appears undistorted on the mesh, the UVs are right; stretching localises exactly where your UVs depart from the system layout.

## Animesh authoring

Animesh is a rigged mesh object (not an attachment) flagged AnimatedObject, with its own skeleton instance, playing animations from its inventory via script control (llStartObjectAnimation and family) and ObjectAnimation messages. Author it like a wearable that nobody wears: rig to the avatar skeleton (or the subset your animations use), keep bone count and triangle count in pet/companion ranges (an animesh pet at avatar triangle counts is a land-impact and render-cost incident), and put animations in the object's inventory with the object as the animation source. Limits are per-object and per-region in the viewer's and simulator's accounting — animesh counts against region limits differently from attachments, and a region full of animesh shop displays can hit ceilings that surprise. Pathing and movement are script problems (llNavigateTo and friends on OpenSim/SL pathfinding where enabled), not rigging problems.

## EEP sky and water authoring

An EEP sky asset is a parameter set, not a texture: sun and moon colour and position offsets, ambient and horizon colours, density and haze, cloud coverage, density, colour and detail (clouds are procedural from these plus a cloud texture slot), star brightness, and sun glow size and focus. A day cycle asset sequences sky keyframes across a 24-hour (or custom-length) day with interpolation, and a water asset pairs with it carrying fresnel, normal scale, wave direction, fog colour and density, and reflection behaviour. Author in the viewer's environment editor on Aditi where you can scrub time of day live; judge a sky at its worst hour (usually the keyframe you spent least time on, often dawn) and at midnight for star and moon balance. Parcel environments override region ones, so a parcel sky is a content feature you can ship with a build — and a support burden when a buyer's parcel looks wrong because their sky, not your build, changed.

## Sculpties and prim building in a mesh era

Sculpted prims encode geometry in a texture (RGB = XYZ over a fixed grid topology) and remain right for some organic low-stakes shapes and for compatibility with ancient content, but they cannot hold hard edges, their UV and topology are fixed by the sculpt type, and their physics is approximate. Prim building itself is not dead: prims are zero-upload-cost, instantly editable in-world, and the correct choice for blockouts, simple architectural shells, and scripted objects where in-world editing is the feature. The pipeline sin is using either by default: choose per object — prim for simple and editable, mesh for shaped and performant, sculpt almost only for legacy repair.

## Land impact mathematics

Land impact (LI) for a linkset is the maximum of three weights, summed appropriately across links: download weight (streaming cost of the geometry — driven by LOD triangle counts and how many bytes a viewer must fetch), physics weight (cost of the physics representation, higher for physical/dynamic use), and server weight (simulation cost, roughly 0.5 per simple prim-like object rising with scripts and complexity, with a per-object base). Prims in a classic linkset traditionally count 1 each until mesh-era accounting applies (a linkset containing mesh, or set to convex hull physics, is recalculated under mesh accounting and prim counts change — the famous 'my 100-prim build became 400 LI' event is mesh accounting arriving via one mesh link or a physics change). Worked patterns are in the appendix: the levers, in order of usual dominance, are physics shape choice, LOD triangle counts, then object count and scripts. There is no legitimate way to argue with the number except by changing the inputs — and one illegitimate-looking but real lever: an object set to physics shape None removes its physics weight contribution almost entirely, which is correct for decor and cheating for floors.

## Upload economics and testing discipline

Upload fees on Agni are per asset in Linden dollars and scale with mesh complexity; textures cost a flat small fee each, which quietly makes texture count a budget line for big sets. The discipline that keeps costs sane: build and iterate on Aditi (test grid, free in practice), keep a local source archive (.blend, textures in lossless form, export presets) for everything uploaded because the grid copy is not your source of truth and LLMesh cannot be losslessly turned back into your .dae, and version uploads rather than overwriting by re-upload (there is no overwrite — every upload is a new UUID, and links, scripts, and BoM flags referencing the old UUID do not follow). Creators who treat UUIDs as permanent public API — because for anything scripted or linked, they are — do not break customers' builds with silent replacements.

## Content debugging playbook

Mesh invisible in-world but fine in preview: check physics shape type None versus a failed LOD (render it at arm's length), then alpha mode, then whether the lowest LOD is degenerate. Mesh black in-world: normals or missing/incorrect material, then EEP environment (PBR metal in a dark sky), then texture fetch failure leaving fallback. Clothing clips: shape extremes test, fitted versus standard rig, alpha layer missing. Texture blurry forever: resolution versus on-screen size (it may be correct behaviour), texture reuse across huge surfaces, or the viewer-side priority story from the internals guide. LI exploded after a small edit: mesh accounting triggered by a physics change or one mesh added to a prim linkset — find the trigger change before re-authoring anything.

## Appendix A: texture memory budget tables (computed)

Uncompressed RGBA memory including the full mipmap chain (factor 4/3). JPEG2000 storage on the grid and in the texture cache is far smaller; these are GPU-side working-set numbers, the ones the viewer's texture budget feels. Halve the base for DXT-style block compression where a viewer path uses it; SL's JPEG2000 decode path targets uncompressed GPU upload in the general case, so budget with these numbers.

- 64x64 RGBA — base 0.02 MiB, with mipmaps 0.02 MiB

- 128x128 RGBA — base 0.06 MiB, with mipmaps 0.08 MiB

- 256x256 RGBA — base 0.25 MiB, with mipmaps 0.33 MiB

- 512x512 RGBA — base 1.00 MiB, with mipmaps 1.33 MiB

- 1024x1024 RGBA — base 4.00 MiB, with mipmaps 5.33 MiB

- 2048x2048 RGBA — base 16.00 MiB, with mipmaps 21.33 MiB

Worked set: an avatar wearing a 1024 skin set across three bake channels (3 x 5.59 MiB with mips ≈ 16.8 MiB), a 1024 clothing diffuse plus 512 normal (≈ 7.5 MiB), hair at 512 alpha (≈ 1.9 MiB with mips) totals roughly 26 MiB of texture working set for one dressed avatar before attachments. Twenty such avatars in view is over 500 MiB of texture demand — the arithmetic behind texture thrash in crowded clubs and behind every 'lower your texture memory' support answer.

Worked set: a shop interior with one shared 1024 atlas (5.59 MiB), six tiling 512 wall and floor textures (≈ 11.2 MiB), and twelve product textures at 256 (≈ 4.2 MiB) totals about 21 MiB — less than one dressed avatar. Texture discipline in environments is almost free compared to avatar costs; spend scrutiny where the avatars are.

## Appendix B: land impact worked patterns

The uploader and in-world build floater are the only authoritative LI calculators; the patterns below are the recurring shapes experienced creators plan around, stated so you can predict which lever will dominate before you upload. Verify every real model in the uploader on Aditi.

- Solid decorative mesh prop (statue), physics None, hand LODs — download weight dominates and lands near the low single digits for a few thousand triangles; setting it Prim physics with a decomposed shape can multiply its LI several-fold for zero user benefit, the most common LI mistake in shipped decor.

- Door with a walk-through opening, physics mesh authored as frame boxes — physics weight is modest because the physics mesh is tens of triangles; the same door with uploader-decomposed physics from the visual mesh produces many hulls, higher physics weight, and a doorway that may test blocked at avatar capsule width.

- Vehicle body, set physical — physics weight dominates by design (dynamic objects are charged for simulation), and download weight from a detailed high LOD adds on the max() only if it exceeds physics; vehicles should budget LI in the tens and earn it back in triangle discipline.

- 100-prim classic linkset, all prim physics — counts about 100 under classic accounting; add one mesh wheel or flip the linkset physics to convex hull and mesh accounting recalculates the whole linkset, commonly raising the total substantially because prim server/download weights under mesh rules differ from the flat 1-per-prim habit.

- Scripted vendor, one prim plus a mesh front panel — server weight is rarely dominant until script count grows; each script adds simulation cost, and a linkset with dozens of scripts (multi-panel vendors, HUD servers) can become server-weight-bound even with trivial geometry.

- Animesh pet, 15k triangles, several animations — download weight from triangles plus the animesh accounting premium; halving triangles via a real low LOD chain is worth more than any other optimisation, and animation count affects inventory and start-up, not LI directly.

## Step by step: Blender to SL for a static mesh prop

1. Block out the prop at real-world size in metres and confirm dimensions against an avatar reference mesh or a 1.8 m cube, because scale errors are invisible until the object is next to an avatar.

2. Model the high LOD with clean topology, keeping quads where you will hand-reduce later and triangulating only at export.

3. Create the medium and low LODs as separate objects by duplicating and reducing, naming them consistently so the uploader's name-based matching pairs them with the high LOD instead of generating its own.

4. Create the lowest LOD last and judge it as a silhouette: if you cannot name the object from its outline at 64 metres, reduce differently.

5. Author the physics mesh as its own simple object (boxes and planes), or decide explicitly that this prop is Convex Hull or None and write that decision in your build notes.

6. UV unwrap each LOD to the same texture layout — LODs share materials and textures, and a LOD with different UVs will swim textures when it swaps in.

7. Assign materials per face deliberately: every distinct material is a face (max 8 per mesh), a draw call, and a texture set; merge materials that share a texture.

8. Apply all transforms, set the origin, and export each LOD and the physics mesh to .dae with the settings from the export section.

9. Upload on Aditi, walk the test matrix: near, far, LOD swap in motion, avatar collision, sit/stand if applicable, noon and midnight lighting.

10. Read the three weights, fix the dominant one at the authoring step that controls it, re-export, and only upload to Agni when the Aditi copy passes.

## Step by step: rigged wearable from Blender to worn

1. Start from a known-good skeleton: Avastar's armature or a manual skeleton whose bone names match avatar_skeleton.xml character for character, in bind pose.

2. Model or fit the garment around the standard body in bind pose with clearance at joints, keeping several edge loops across each joint for graduated weights.

3. Weight by copying from the body where the garment hugs it, then hand-paint joint transitions; check weight normalisation and the four-influence limit before export.

4. Decide fitted versus standard rigging: fitted weights to collision-volume bones for slider response, standard for joint-following only, and note that mixing them in one mesh produces half-responsive garments.

5. Export with armature and weights, upload on Aditi as a wearable test on a fresh avatar, and run the shape-extremes matrix (height, muscle, fat, both base shapes) plus a walk/run/sit animation set, watching elbows, shoulders, crotch, and ankles in motion, not in a T-pose screenshot.

6. Ship with or reference the alpha layer the design needs, and state BoM versus applier expectations in the product notes so buyers wear the right body setup.

## Step by step: PBR material in Substance Painter for SL

1. Set the project to a glTF-compatible metalness/roughness workflow and texture set sizes from the budget tables, not from the maximum the tool offers.

2. Paint base colour in sRGB, keeping albedo values in physical ranges: no pure white diffuse, metals' colour lives in base colour while non-metals stay mid-grey in metalness (black).

3. Paint roughness as variation, not a flat value — fingerprints, edge wear, and fabric weave in roughness are what make SL's EEP lighting read as material instead of plastic.

4. Export with a glTF PBR preset, then repack occlusion into the R channel of the metallic-roughness texture if your preset wrote it separately, matching SL's channel mapping.

5. Upload the textures to Aditi, create the material, apply it to a test prim and to the real mesh, and judge it under a neutral midday EEP and a warm sunset EEP before judging it under your parcel's mood lighting.

6. Record the material's texture UUIDs in your source archive: the material asset references them permanently, and losing the mapping makes the product unmaintainable.

## Face and material discipline

A mesh supports at most 8 materials (faces) and each face is a separate texture set, material assignment, and draw call. Face discipline is therefore an economic act: a chair with one wood face and one fabric face costs two texture sets; the same chair exported per-part from a modelling tool can arrive with fourteen faces of near-identical wood and be unuploadable as one mesh. Merge by material in Blender before export, use texture atlases to make one face do the work of many, and remember scripts address faces by number — reordering faces in a re-export breaks every llSetLinkPrimitiveParamsFast call, texture animation, and BoM flag that referenced the old numbering, which is why face order is part of a product's public interface once shipped.

## Texture atlases and tiling: choosing

Tile a texture when the surface is large, repetitive, and viewed at varying distance (walls, floors, ground, fabric bolts): tiling gives texel density independent of object size and reuses one fetch everywhere. Atlas when a set of small unique parts shares one material and one usage pattern (a furniture set, a product line, signage): one 1024 atlas replaces many small textures and their fetch and memory overhead. Bake unique textures when the object's identity is its surface detail (a specific worn leather chair, a painted sign) and accept the memory cost knowingly. The failure modes are mirror images: tiling a hero object looks generic, and uniquely baking a warehouse of crates bankrupts the texture budget of everyone who rezzes it.

## Animations for content: BVH and anim assets

Object and avatar animations upload as .bvh or .anim and are stored as animation assets with priority, loop, and ease parameters set at upload or by script defaults. Authoring points that matter downstream: animations are sampled against the skeleton, so an animation authored on a differently proportioned rig retargets approximately, not exactly; priority decides conflicts (a priority-4 hold beats a priority-2 walk's arms), and animesh and attachments obey the same priority arbitration as avatar animations; loop in/out points and ease-in/out are baked into the asset, so a sit that snaps is an upload-parameter problem, not a script problem. Keep source BVH files: like meshes, animation assets cannot be losslessly recovered from the grid.

## Sounds and particles as content pipeline

Sounds upload as Ogg Vorbis (short, mono, trimmed — loop points are sample-exact in the file, and a click at the loop seam is an authoring defect no script can hide) and are charged and cached like other assets. Particles are not assets at all: they are parameter recipes stored on the prim (PSYS_* rules via llParticleSystem) evaluated by each viewer, so particle 'authoring' is parameter tuning against the viewer's particle budget, and the same emitter looks different at different viewer particle counts — design emitters that read correctly at half density. Both belong in a product's source archive and test matrix even though neither appears in the mesh uploader.

## EEP parameter catalogue in practice

Sky parameters group into: sun and moon (colour, position offset via sun angle in day cycles, glow size and focus), atmosphere (ambient colour and intensity, blue horizon, blue density, haze horizon, density multiplier, distance multiplier, max altitude), clouds (coverage, colour, density, detail scale, scroll, opacity), and celestial (star brightness, moon brightness and size). Water parameters group into: colour and fresnel (fresnel scale and offset), normals (normal map, normal scale, wave directions), fog (underwater fog colour, fog density, fog modulation), and reflection behaviour. A day cycle is a timeline of sky keyframes with blend intervals; the two authored hours that decide whether a cycle feels professional are dawn and dusk, because sun angle, horizon colour, and ambient all move fastest there and interpolation between lazy keyframes greys them out. Author extra keyframes at transitions instead of polishing noon.

## Bake channels catalogue

Head channel: composited from skin head area, head tattoos, and head-region clothing and alpha layers — consumed by system heads and BoM mesh heads and hair bases. Upper channel: torso skin, undershirt/shirt layers, torso tattoos and alphas — consumed by mesh torsos and upper garments flagged BoM. Lower channel: legs and pelvis skin, pants layers, lower tattoos and alphas. Eyes channel: the eye texture area for system and BoM eyes. Hair channel: scalp and hair-base compositing for system hair and BoM hair bases. Skirt channel: the skirt layer area used by system skirts and some mesh garments. Universal layers: wearable layer type that can carry a texture intended to project across channels for effects like full-body tattoos and wetness or dirt overlays, consumed by attachments flagged for universal bake. When a layer 'does not show' on a BoM body, the checklist is: layer worn, channel correct, attachment flagged for that channel, COF/bake refreshed — in that order.

## Appendix C: content constants from lsl-definitions, with values and tooltips

Every constant in secondlife/lsl-definitions whose name belongs to the content families (PRIM_, TEXTURE_, MATERIAL_, STATUS_ physics bits, OBJECT_ detail keys, PSYS_ particle rules, VEHICLE_, and alpha and glow related families), with its canonical value and tooltip. These are the numbers scripts and authoring tools use to address the pipeline this guide describes.

- `OBJECT_ACCOUNT_LEVEL` = 41 — Flag used with llGetObjectDetails to retrieve an avatar's account level. Returns 0 for Basic, 1 for Premium, 5 for Plus, 10 for Premium Plus, or -1 if the target is not an avatar.

- `OBJECT_ANIMATED_COUNT` = 39 — Flag used with llGetObjectDetails. For an object, returns a boolean indicating if the root is set as 'Animated Mesh'. For an agent, returns the total number of 'Animated Mesh' attachments worn.

- `OBJECT_ANIMATED_SLOTS_AVAILABLE` = 40 — Flag used with llGetObjectDetails to get the avatar's available 'Animated Mesh' attachment slot count (returns 0 if the ID is not an avatar).

- `OBJECT_ATTACHED_POINT` = 19 — Flag used with llGetObjectDetails. Returns the integer attachment point matching an ATTACH_* constant, or 0 if the target is not an attachment (e.g., an avatar or unattached object).

- `OBJECT_ATTACHED_SLOTS_AVAILABLE` = 35 — Flag used with llGetObjectDetails to get an avatar's available attachment slot count. Returns 0 if the ID is not an avatar or if no slots are available.

- `OBJECT_BODY_SHAPE_TYPE` = 26 — Flag used with llGetObjectDetails to retrieve a float representing the gender/sex setting of an avatar's shape (0.0 is standard female, 1.0 is standard male, and values greater than or equal to 0.5 are considered male). Returns -1.0 if not an avatar or if no data is available.

- `OBJECT_CHARACTER_TIME` = 17 — Flag used with llGetObjectDetails to get the average CPU time (in seconds) spent on navigation if the target is a pathfinding character. Returns 0 for non-characters.

- `OBJECT_CLICK_ACTION` = 28 — Flag used with llGetObjectDetails to get the click action of a prim. Returns an integer corresponding to a CLICK_ACTION_* constant (default is 0).

- `OBJECT_CREATION_TIME` = 36 — Flag used with llGetObjectDetails to get the object's creation time (established via build-menu rezzing or mesh uploads, not via inventory/script rezzes, copying, or modifying). Returns an empty string for avatars.

- `OBJECT_CREATOR` = 8 — Flag used with llGetObjectDetails to get the key of the prim's creator. Returns NULL_KEY if the ID is an avatar.

- `OBJECT_DAMAGE` = 51 — Flag used with llGetObjectDetails to retrieve the amount of damage a prim inflicts upon collision.

- `OBJECT_DAMAGE_TYPE` = 52 — Flag used with llGetObjectDetails to retrieve the type of damage a prim inflicts on collision. Returns an integer matching a DAMAGE_TYPE_* constant, a custom type, or a value repurposed by a combat system.

- `OBJECT_DESC` = 2 — Flag used with llGetObjectDetails to retrieve the prim's description. Returns an empty string if the ID is an avatar.

- `OBJECT_GROUP` = 7 — Flag used with llGetObjectDetails to get the prim's group key. Returns NULL_KEY if the target is an avatar (which means a workaround is required to get an avatar's active group).

- `OBJECT_GROUP_TAG` = 33 — Flag used with llGetObjectDetails to get an avatar's active group tag/title. Returns an empty string if the target is not an avatar.

- `OBJECT_HEALTH` = 50 — Flag used with llGetObjectDetails to retrieve the current health value of an avatar or prim.

- `OBJECT_HOVER_HEIGHT` = 25 — Flag used with llGetObjectDetails to get the dynamic hover height of an avatar (default is 0.0). Returns 0.0 if not an avatar or if no data is available; does not reflect the shape's 'Hover' slider.

- `OBJECT_LAST_OWNER_ID` = 27 — Flag used with llGetObjectDetails to get the key of the previous owner. For group-owned objects, returns the avatar who deeded it. Returns NULL_KEY for avatars, untransferred objects, or objects taken to inventory and re-rezzed.

- `OBJECT_LINK_NUMBER` = 46 — Flag used with llGetObjectDetails to get the index of the prim within its linkset, or 0 if unlinked.

- `OBJECT_LOCKED` = 55 — Flag used with llGetObjectDetails to get a boolean, indicating if the object is locked.

- `OBJECT_MASS` = 43 — Flag used with llGetObjectDetails to retrieve the total mass (in kilograms) of the object's linkset.

- `OBJECT_MATERIAL` = 42 — Flag used with llGetObjectDetails to retrieve the physics material of the object, returning an integer matching a PRIM_MATERIAL_* constant.

- `OBJECT_NAME` = 1 — Flag used with llGetObjectDetails to get the prim's name, or the legacy name if the target is an avatar.

- `OBJECT_OMEGA` = 29 — Flag used with llGetObjectDetails to get the rotational (angular) velocity of an object in radians per second.

- `OBJECT_OWNER` = 6 — Flag used with llGetObjectDetails to get the owner's key. If the target is an avatar, their own key is returned. If group-owned, it returns NULL_KEY.

- `OBJECT_PATHFINDING_TYPE` = 20 — Flag used with llGetObjectDetails to get the pathfinding setting of an object in the region, returning an integer matching an OPT_* constant.

- `OBJECT_PERMS` = 53 — Flag used with llGetObjectDetails to retrieve the permissions of the object as five integers.

- `OBJECT_PERMS_COMBINED` = 54 — Flag used with llGetObjectDetails to retrieve the permissions of the object combined with all of its inventory items as five integers.

- `OBJECT_PHANTOM` = 22 — Flag used with llGetObjectDetails to get a boolean indicating if phantom is enabled on the object. Returns 0 if the target is an avatar or attachment.

- `OBJECT_PHYSICS` = 21 — Flag used with llGetObjectDetails to get a boolean indicating if physics is enabled on the object. Returns 0 if the target is an avatar or attachment.

- `OBJECT_PHYSICS_COST` = 16 — Flag used with llGetObjectDetails to get the physics cost of the object.

- `OBJECT_POS` = 3 — Flag used with llGetObjectDetails to get the prim's position in region coordinates. For an avatar outside the region, the returned position is relative to the script's region.

- `OBJECT_PRIM_COUNT` = 30 — Flag used with llGetObjectDetails to get the prim count of the object. Note that the script and target object must be owned by the same owner.

- `OBJECT_PRIM_EQUIVALENCE` = 13 — Flag used with llGetObjectDetails to get the prim equivalence of the object.

- `OBJECT_RENDER_WEIGHT` = 24 — Flag used with llGetObjectDetails to get the render weight (Avatar Rendering Cost) of an avatar based on viewer reports. Returns 0 for objects, -1 if unknown, and is capped at 500,000.

- `OBJECT_RETURN_PARCEL` = 1 — Scope flag used with llReturnObjectsByOwner to return all objects on the same parcel as the script owned by the specified owner. Requires the script owner to be an estate manager or the parcel owner.

- `OBJECT_RETURN_PARCEL_OWNER` = 2 — Scope flag used with llReturnObjectsByOwner to return all objects owned by the specified owner that are located on parcels owned by the script's owner.

- `OBJECT_RETURN_REGION` = 4 — Scope flag used with llReturnObjectsByOwner to return all objects in the region owned by the specified owner. Only works if the script is owned by the estate owner or an estate manager.

- `OBJECT_REZZER_KEY` = 32 — Flag used with llGetObjectDetails to retrieve the key of the object or avatar that rezzed the target object.

- `OBJECT_REZ_TIME` = 45 — Flag used with llGetObjectDetails to retrieve the timestamp of when the object was rezzed.

- `OBJECT_ROOT` = 18 — Flag used with llGetObjectDetails to get the ID of the root prim. For an avatar, returns the root prim of the linkset they are sitting on (or the avatar's own ID if not sitting).

- `OBJECT_ROT` = 4 — Flag used with llGetObjectDetails to get the prim's rotation.

- `OBJECT_RUNNING_SCRIPT_COUNT` = 9 — Flag used with llGetObjectDetails to get the total number of running scripts attached to the target object or agent.

- `OBJECT_SCALE` = 47 — Flag used with llGetObjectDetails to get the size (scale) of the object.

- `OBJECT_SCRIPT_MEMORY` = 11 — Flag used with llGetObjectDetails to get the allocated script memory (or its upper limit) in bytes for the object or agent. This value is recomputed every 10-20 seconds.

- `OBJECT_SCRIPT_TIME` = 12 — Flag used with llGetObjectDetails to get the average script CPU time (in seconds) used per frame. Reports a 30-minute average, or the average since entering the region if present for less than 30 minutes.

- `OBJECT_SELECT_COUNT` = 37 — Flag used with llGetObjectDetails to get the total number of agents/avatars actively selecting any link in the object. Returns 0 if the target is an avatar.

- `OBJECT_SERVER_COST` = 14 — Flag used with llGetObjectDetails to get the server cost of the object.

- `OBJECT_SIT_COUNT` = 38 — Flag used with llGetObjectDetails to get the total number of agents sitting on any links in the object. Returns 0 if the target is an avatar.

- `OBJECT_STREAMING_COST` = 15 — Flag used with llGetObjectDetails to get the streaming (download) cost of the object.

- `OBJECT_TEMP_ATTACHED` = 34 — Flag used with llGetObjectDetails to get a boolean indicating whether the object is temporarily attached.

- `OBJECT_TEMP_ON_REZ` = 23 — Flag used with llGetObjectDetails to get a boolean indicating if temporary-on-rez is enabled for the object.

- `OBJECT_TEXT` = 44 — Flag used with llGetObjectDetails to get the floating (hover) text displayed above the object.

- `OBJECT_TEXT_ALPHA` = 49 — Flag used with llGetObjectDetails to get the alpha value of the floating (hover) text displayed above the object.

- `OBJECT_TEXT_COLOR` = 48 — Flag used with llGetObjectDetails to get the color vector of the floating (hover) text displayed above the object.

- `OBJECT_TOTAL_INVENTORY_COUNT` = 31 — Flag used with llGetObjectDetails to get the total number of inventory items inside the object. Requires the script and target object to share the same owner.

- `OBJECT_TOTAL_SCRIPT_COUNT` = 10 — Flag used with llGetObjectDetails to get the total number of scripts (both running and stopped) attached to the target object or agent.

- `OBJECT_UNKNOWN_DETAIL` = -1 — Flag returned by llGetObjectDetails when an invalid flag is requested.

- `OBJECT_VELOCITY` = 5 — Flag used with llGetObjectDetails to get the velocity vector of the target object.

- `OBJECT_VOLUME_DETECT` = 56 — Flag used with llGetObjectDetails to get a boolean, indicating if the object is VolumeDetect.

- `PRIM_ALLOW_UNSIT` = 39 — Prim parameter for allowing or restricting manual standing for avatars seated on this prim within a valid experience. Ignored if the avatar was not seated via llSitOnLink. When restriction is active, participating seated avatars cannot manually stand or select another prim to sit on.

- `PRIM_ALPHA_MODE` = 38 — Prim parameter used to set diffuse texture alpha rendering mode attributes. Requires face, alpha_mode (PRIM_ALPHA_MODE_BLEND, _NONE, _MASK, or _EMISSIVE), and alpha_cutoff (used only for _MASK) parameters.

- `PRIM_ALPHA_MODE_BLEND` = 1 — Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to use alpha blending for diffuse texture rendering (if an alpha channel exists). Also used as the default value to clear material settings from a prim face.

- `PRIM_ALPHA_MODE_EMISSIVE` = 3 — Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel as an emissivity mask. Pixels render with an emissivity corresponding to their opacity under all lighting conditions (fully opaque pixels effectively render as 'full bright').

- `PRIM_ALPHA_MODE_MASK` = 2 — Prim parameter setting for PRIM_ALPHA_MODE. Renders the diffuse texture's alpha channel on a binary per-pixel basis; pixels more opaque than the alpha cutoff render as fully opaque, while pixels below the cutoff render as fully transparent.

- `PRIM_ALPHA_MODE_NONE` = 0 — Prim parameter setting for PRIM_ALPHA_MODE. Directs the face to ignore the alpha channel of the diffuse texture and render as completely opaque (default setting when a material face lacks an alpha channel).

- `PRIM_BUMP_BARK` = 4 — Face bump mapping setting: bark.

- `PRIM_BUMP_BLOBS` = 12 — Face bump mapping setting: petridish (blobby amoeba-like shapes).

- `PRIM_BUMP_BRICKS` = 5 — Face bump mapping setting: bricks.

- `PRIM_BUMP_BRIGHT` = 1 — Face bump mapping setting: brightness (generated from highlights).

- `PRIM_BUMP_CHECKER` = 6 — Face bump mapping setting: checker.

- `PRIM_BUMP_CONCRETE` = 7 — Face bump mapping setting: concrete.

- `PRIM_BUMP_DARK` = 2 — Face bump mapping setting: darkness (generated from lowlights).

- `PRIM_BUMP_DISKS` = 10 — Face bump mapping setting: discs (packed circles).

- `PRIM_BUMP_GRAVEL` = 11 — Face bump mapping setting: gravel.

- `PRIM_BUMP_LARGETILE` = 14 — Face bump mapping setting: stonetile (large tile).

- `PRIM_BUMP_NONE` = 0 — Face bump mapping setting: none (no bump map).

- `PRIM_BUMP_SHINY` = 19 — Prim parameter used to get or set both the shininess and bump mapping settings of a face.

- `PRIM_BUMP_SIDING` = 13 — Face bump mapping setting: siding.

- `PRIM_BUMP_STONE` = 9 — Face bump mapping setting: cutstone (blocks).

- `PRIM_BUMP_STUCCO` = 15 — Face bump mapping setting: stucco.

- `PRIM_BUMP_SUCTION` = 16 — Face bump mapping setting: suction (rings).

- `PRIM_BUMP_TILE` = 8 — Face bump mapping setting: crustytile.

- `PRIM_BUMP_WEAVE` = 17 — Face bump mapping setting: weave.

- `PRIM_BUMP_WOOD` = 3 — Face bump mapping setting: woodgrain.

- `PRIM_CAST_SHADOWS` = 24 — Deprecated prim parameter representing shadow casting settings for the primitive.

- `PRIM_CLICK_ACTION` = 43 — Prim parameter followed by a CLICK_ACTION_* constant to specify the default action taken when a user clicks or touches the prim.

- `PRIM_COLLISION_SOUND` = 53 — Prim parameter to set the collision sound UUID and volume level for the prim.

- `PRIM_COLOR` = 18 — Prim parameter to get or set the Blinn-Phong color and opacity of a face. integer face – face number or ALL_SIDES vector color – color in RGB <R, G, B> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white) float alpha – from 0.0 (clear) to 1.0 (solid) (0.0 <= alpha <= 1.0)

- `PRIM_DAMAGE` = 51 — Prim parameter used to get or set the damage amount and damage type delivered by the prim on collision.

- `PRIM_DESC` = 28 — Prim parameter [PRIM_DESC, string description] to get or set the prim's description (equivalent to llGetObjectDesc/llSetObjectDesc).

- `PRIM_FLEXIBLE` = 21 — Prim parameter to get or set the prim's flexible configuration. integer boolean – TRUE enables, FALSE disables integer softness – ranges from 0 to 3 float gravity – ranges from -10.0 to 10.0 float friction – ranges from 0.0 to 10.0 float wind – ranges from 0.0 to 10.0 float tension – ranges from 0.0 to 10.0 vector force

- `PRIM_FULLBRIGHT` = 20 — Prim parameter [PRIM_FULLBRIGHT, integer face, integer boolean] to get or set whether full-bright rendering is enabled on the specified face.

- `PRIM_GLOW` = 25 — Prim parameter [PRIM_GLOW, integer face, float intensity] to get or set the glow intensity on a face (the compiler integer value is 25 if the named constant is rejected).

- `PRIM_GLTF_ALPHA_MODE_BLEND` = 1 — GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material with transparency (alpha blending) in linear color space. Transparency from the texture is multiplied by the material's opacity multiplier. Note: This mode can suffer from depth sorting and performance issues.

- `PRIM_GLTF_ALPHA_MODE_MASK` = 2 — GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Renders the material as fully opaque where the alpha value is greater than the alpha cutoff, and fully transparent otherwise.

- `PRIM_GLTF_ALPHA_MODE_OPAQUE` = 0 — GLTF alpha mode setting for PRIM_GLTF_BASE_COLOR. Ignores the alpha channel entirely and renders the face material as completely opaque.

- `PRIM_GLTF_BASE_COLOR` = 48 — Prim parameter to get or set the GLTF base color override of an object's face. Requires face, texture, repeats, offsets, rotation, linear_color (in linear space; use llsRGB2Linear), alpha_mode (PRIM_GLTF_ALPHA_MODE_*), alpha_cutoff, and double_sided arguments.

- `PRIM_GLTF_EMISSIVE` = 46 — Prim parameter to get or set the GLTF emission override of a face. Requires face, texture, repeats, offsets, rotation, and emissive_tint (specified in linear space; use llsRGB2Linear).

- `PRIM_GLTF_METALLIC_ROUGHNESS` = 47 — Prim parameter to get or set the GLTF occlusion/metallic/roughness override of a face. Requires face, texture, repeats, offsets, rotation, metallic_factor, and roughness_factor arguments.

- `PRIM_GLTF_NORMAL` = 45 — Prim parameter to get or set the GLTF normal map override of a face. Requires face, texture, repeats, offsets, and rotation arguments.

- `PRIM_HEALTH` = 52 — Prim parameter used to get or set the health of the prim. Objects default to 0 health.

- `PRIM_HOLE_CIRCLE` = 0x10 — Parameter used with certain PRIM_TYPE_* flags to make a circular hole via the hole_shape parameter.

- `PRIM_HOLE_DEFAULT` = 0x00 — Parameter used with certain PRIM_TYPE_* flags to make a hole of the same shape as the outer shape via the hole_shape parameter.

- `PRIM_HOLE_SQUARE` = 0x20 — Parameter used with certain PRIM_TYPE_* flags to make a squarish hole via the hole_shape parameter.

- `PRIM_HOLE_TRIANGLE` = 0x30 — Parameter used with certain PRIM_TYPE_* flags to make a triangular hole via the hole_shape parameter.

- `PRIM_LINK_TARGET` = 34 — Prim parameter [PRIM_LINK_TARGET, integer link_target] used to get or set properties for multiple linked prims within a single primitive parameters call.

- `PRIM_MATERIAL` = 2 — Prim parameter [PRIM_MATERIAL, integer PRIM_MATERIAL_*] to get or set the prim's material. The material determines the default collision sound, sprite, friction coefficient, and restitution coefficient (elasticity) without affecting mass.

- `PRIM_MATERIAL_FLESH` = 4 — Prim material constant: flesh.

- `PRIM_MATERIAL_GLASS` = 2 — Prim material constant: glass (features very low friction).

- `PRIM_MATERIAL_LIGHT` = 7 — Deprecated prim material constant. Light is now a face property instead of a prim property; equivalent functionality is achieved using [PRIM_FULLBRIGHT, ALL_SIDES, TRUE].

- `PRIM_MATERIAL_METAL` = 1 — Prim material constant: metal.

- `PRIM_MATERIAL_PLASTIC` = 5 — Prim material constant: plastic.

- `PRIM_MATERIAL_RUBBER` = 6 — Prim material constant: rubber.

- `PRIM_MATERIAL_STONE` = 0 — Prim material constant: stone.

- `PRIM_MATERIAL_WOOD` = 3 — Prim material constant: wood.

- `PRIM_MEDIA_ALT_IMAGE_ENABLE` = 0 — Boolean. Gets or sets the default image state (the image a user sees before media is active) on a face. The default is specified by the server for that media type. Note: This flag is not currently implemented.

- `PRIM_MEDIA_AUTO_LOOP` = 4 — Boolean. Gets or sets whether auto-looping is enabled for the face media.

- `PRIM_MEDIA_AUTO_PLAY` = 5 — Boolean. Gets or sets whether media auto-plays when a resident is able to view it.

- `PRIM_MEDIA_AUTO_SCALE` = 6 — Boolean. Gets or sets whether auto-scaling is enabled, which forces the media to fill the entire texture size.

- `PRIM_MEDIA_AUTO_ZOOM` = 7 — Boolean. Gets or sets whether clicking the media triggers auto-zoom and auto-focus.

- `PRIM_MEDIA_CONTROLS` = 1 — Integer. Gets or sets the style of media controls (can be set to PRIM_MEDIA_CONTROLS_STANDARD or PRIM_MEDIA_CONTROLS_MINI).

- `PRIM_MEDIA_CONTROLS_MINI` = 1 — Mini web navigation controls constant; does not include an address bar.

- `PRIM_MEDIA_CONTROLS_STANDARD` = 0 — Standard web navigation controls constant.

- `PRIM_MEDIA_CURRENT_URL` = 2 — String. Gets or sets the current URL displayed on the chosen face (maximum 1024 characters). Changing this URL triggers media navigation.

- `PRIM_MEDIA_FIRST_CLICK_INTERACT` = 8 — Boolean. Gets or sets what happens when someone click on a playing, but unfocused media face: TRUE: Does the same thing a focused media face does, and forwards the click to the web browser. FALSE: Focuses the media prim so that future clicks are forwarded to the web browser. Note: Viewer settings affect this flag. It works by default on m

- `PRIM_MEDIA_HEIGHT_PIXELS` = 10 — Integer. Gets or sets the height of the media in pixels.

- `PRIM_MEDIA_HOME_URL` = 3 — String. Gets or sets the home URL for the chosen face (maximum 1024 characters).

- `PRIM_MEDIA_PERMS_CONTROL` = 14 — Integer. Gets or sets the permissions mask controlling who can see the media control bar (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).

- `PRIM_MEDIA_PERMS_INTERACT` = 13 — Integer. Gets or sets the permissions mask controlling who can interact with the media (PRIM_MEDIA_PERM_ANYONE, _GROUP, _NONE, or _OWNER).

- `PRIM_MEDIA_WHITELIST` = 12 — Gets or sets the media whitelist as an array of URL strings (up to 64 URLs or 1024 characters, whichever comes first). At the SLua level, provide a {string} array; the serializer encodes it as an escaped, comma-separated string for the underlying LSL API.

- `PRIM_MEDIA_WHITELIST_ENABLE` = 11 — Boolean. Gets or sets whether media navigation is restricted to the URLs listed in PRIM_MEDIA_WHITELIST.

- `PRIM_MEDIA_WIDTH_PIXELS` = 9 — Integer. Gets or sets the width of the media in pixels.

- `PRIM_NAME` = 27 — Prim parameter [PRIM_NAME, string name] to get or set the prim's name (equivalent to llGetObjectName/llSetObjectName).

- `PRIM_NORMAL` = 37 — Prim parameter to get or set the Blinn-Phong normal map texture settings of a face. Requires face, texture, repeats, offsets, and rotation_in_radians arguments.

- `PRIM_OMEGA` = 32 — Prim parameter to get, set, or disable a client-side physical-like rotation (analogous to llTargetOmega). vector axis – arbitrary axis to rotate the object around float spinrate – rate of rotation in radians per second float gain – also modulates the final spinrate and disables the rotation behavior if zero

- `PRIM_PHANTOM` = 5 — Prim parameter [PRIM_PHANTOM, integer boolean] to get or set whether phantom status is enabled.

- `PRIM_PHYSICS` = 3 — Prim parameter [PRIM_PHYSICS, integer boolean] to get or set whether the object responds to Second Life physics.

- `PRIM_PHYSICS_SHAPE_CONVEX` = 2 — Physics shape type setting. Uses the convex hull of the prim shape to generate its physics representation (the default for mesh objects).

- `PRIM_PHYSICS_SHAPE_NONE` = 1 — Physics shape type setting. Directs the physics engine to ignore this prim entirely, preventing it from contributing to the linkset's physics shape. Note: Cannot be applied to the root prim.

- `PRIM_PHYSICS_SHAPE_PRIM` = 0 — Physics shape type setting. Uses the actual visible shape of the prim to determine its physics representation (the default for all non-mesh objects).

- `PRIM_PHYSICS_SHAPE_TYPE` = 30 — Prim parameter used to get or set the type of shape the physics engine uses for the prim (PRIM_PHYSICS_SHAPE_NONE, _PRIM, or _CONVEX). Mainly used for physics optimization.

- `PRIM_POINT_LIGHT` = 23 — Prim parameter to configure local lighting. Accepts color in linear space (use llsRGB2Linear to convert from sRGB). integer boolean – TRUE enables, FALSE disables vector linear_color – linear color in RGB <R, G, B&> (<0.0, 0.0, 0.0> = black, <1.0, 1.0, 1.0> = white) float intensity – ranges from 0.0 to 1.0 float radius – ranges from 0.1 t

- `PRIM_POSITION` = 6 — Prim parameter [PRIM_POSITION, vector position] to get or set the position of the prim in region coordinates (or local coordinates depending on the script context).

- `PRIM_POS_LOCAL` = 33 — Prim parameter [PRIM_POS_LOCAL, vector position] to get or set the local position of a prim (equivalent to llGetLocalPos/llSetPos).

- `PRIM_PROJECTOR` = 42 — Prim parameter [PRIM_PROJECTOR, string texture, float fov, float focus, float ambiance] to configure light projection settings. If the prim is not configured as a projector, the texture key will return NULL_KEY.

- `PRIM_REFLECTION_PROBE` = 44 — Prim parameter to configure the object as a custom-placed reflection probe for Image-Based Lighting (IBL). Only affects objects inside its volume of influence.

- `PRIM_REFLECTION_PROBE_BOX` = 1 — Flag option used with PRIM_REFLECTION_PROBE. When set, the reflection probe volume is a box; when unset, it defaults to a sphere.

- `PRIM_REFLECTION_PROBE_DYNAMIC` = 2 — Flag option used with PRIM_REFLECTION_PROBE. When set, the probe dynamically includes avatars in its image-based lighting reflections (which carries a rendering performance cost).

- `PRIM_REFLECTION_PROBE_MIRROR` = 4 — Flag option used with PRIM_REFLECTION_PROBE. When set, intersecting low-roughness PBR materials act as mirrors. Note: Mirrors do not reflect avatars unless PRIM_REFLECTION_PROBE_DYNAMIC is also enabled, and they carry a performance cost.

- `PRIM_RENDER_MATERIAL` = 49 — Prim parameter [PRIM_RENDER_MATERIAL, integer face, string material] to get or set face material settings. Note: Setting this clears most PRIM_GLTF_* properties on the face, except for repeats, offsets, and rotation_in_radians.

- `PRIM_ROTATION` = 8 — Prim parameter [PRIM_ROTATION, rotation global_rot] to get or set the global rotation of the prim (equivalent to llGetRot/llSetRot; note that setting this on child prims may be broken).

- `PRIM_ROT_LOCAL` = 29 — Prim parameter [PRIM_ROT_LOCAL, rotation local_rot] to get or set the local rotation of a prim (equivalent to llGetLocalRot/llSetLocalRot).

- `PRIM_SCRIPTED_SIT_ONLY` = 40 — Prim parameter restricting manual sitting on this prim. When active, sitting can only be initiated via llSitOnLink; manual sitting attempts fail. This restriction applies even outside experience-enabled regions.

- `PRIM_SCULPT_FLAG_ANIMESH` = 32 — Read-only flag for PRIM_TYPE_SCULPT to query whether the object is an Animated Mesh (Animesh).

- `PRIM_SCULPT_FLAG_INVERT` = 64 — Flag for PRIM_TYPE_SCULPT to render the sculpted prim inside-out by inverting the normals of each polygon.

- `PRIM_SCULPT_FLAG_MIRROR` = 128 — Flag for PRIM_TYPE_SCULPT to render a mirror-image of the sculpted prim, mirrored across the X-axis.

- `PRIM_SCULPT_TYPE_CYLINDER` = 4 — Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right to produce a cylinder-shaped sculpted prim.

- `PRIM_SCULPT_TYPE_MASK` = 7 — Bitmask used when parsing sculpted prim properties (PRIM_TYPE_SCULPT) from llGetPrimitiveParams to separate the base sculpt type from modifying flags (invert or mirror).

- `PRIM_SCULPT_TYPE_MESH` = 5 — Sculpt type option for PRIM_TYPE_SCULPT indicating the object is a uploaded Mesh model.

- `PRIM_SCULPT_TYPE_PLANE` = 3 — Sculpt type option for PRIM_TYPE_SCULPT that performs no stitching or converging, producing a flat plane-shaped sculpted prim.

- `PRIM_SCULPT_TYPE_SPHERE` = 1 — Sculpt type option for PRIM_TYPE_SCULPT that stitches the left side to the right and separately converges the top and bottom to produce a sphere-shaped sculpted prim.

- `PRIM_SCULPT_TYPE_TORUS` = 2 — Sculpt type option for PRIM_TYPE_SCULPT that stitches top-to-bottom and left-to-right to produce a torus-shaped sculpted prim.

- `PRIM_SHINY_HIGH` = 3 — Sets the highest intensity legacy face shininess setting.

- `PRIM_SHINY_LOW` = 1 — Sets the lowest intensity legacy face shininess setting.

- `PRIM_SHINY_MEDIUM` = 2 — Sets a medium intensity legacy face shininess setting.

- `PRIM_SHINY_NONE` = 0 — Disables the legacy face shininess setting.

- `PRIM_SIT_FLAGS` = 50 — Prim parameter used to get or set sit-related flags currently active on the prim.

- `PRIM_SIT_TARGET` = 41 — Prim parameter [PRIM_SIT_TARGET, integer boolean, vector offset, rotation rot] to get or set the prim's sit target. Setting the boolean to FALSE deactivates the target. Unlike llLinkSitTarget, offset <0.0, 0.0, 0.0> can be explicitly set.

- `PRIM_SIZE` = 7 — Prim parameter [PRIM_SIZE, vector size] to get or set the prim's physical dimensions (equivalent to llGetScale/llSetScale).

- `PRIM_SLICE` = 35 — Prim parameter [PRIM_SLICE, vector slice] to get or set the prim's slice values (a shape attribute equivalent to advanced cut).

- `PRIM_SPECULAR` = 36 — Prim parameter to get or set the Blinn-Phong specular map texture settings of a face. Requires face, texture, repeats, offsets, rotation_in_radians, color, glossy, and environment arguments.

- `PRIM_TEMP_ON_REZ` = 4 — Prim parameter used to get or set the object's temporary status. Temporary objects live until the next garbage collection cycle (about 1 minute), do not count against normal prim limits, but are subject to regional limits.

- `PRIM_TEXGEN` = 22 — Prim parameter [PRIM_TEXGEN, integer face, integer mode] to get or set the texture mapping mode of the face.

- `PRIM_TEXGEN_DEFAULT` = 0 — Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in texture repeats per face.

- `PRIM_TEXGEN_PLANAR` = 1 — Texture mapping mode setting for PRIM_TEXGEN. Specifies that texture repeat units are measured in repeats per half-meter (unlike the in-world editor, which measures in repeats per meter).

- `PRIM_TEXT` = 26 — Prim parameter [PRIM_TEXT, string text, vector color, float alpha] to get or set the object's floating/hover text (equivalent to llSetText).

- `PRIM_TEXTURE` = 17 — Prim parameter [PRIM_TEXTURE, integer face, string texture, vector repeats, vector offsets, float rotation_in_radians] to get or set the Blinn-Phong diffuse texture settings of a face.

- `PRIM_TYPE` = 9 — Prim parameter used to get or set the geometric shape type (PRIM_TYPE_*) and its associated parameters.

- `PRIM_TYPE_BOX` = 0 — Shape parameter for PRIM_TYPE used to define the prim as a box and configure its shape properties.

- `PRIM_TYPE_CYLINDER` = 1 — Shape parameter for PRIM_TYPE used to define the prim as a cylinder and configure its shape properties.

- `PRIM_TYPE_PRISM` = 2 — Shape parameter for PRIM_TYPE used to define the prim as a prism and configure its shape properties.

- `PRIM_TYPE_RING` = 6 — Shape parameter for PRIM_TYPE used to define the prim as a ring and configure its shape properties.

- `PRIM_TYPE_SCULPT` = 7 — Shape parameter for PRIM_TYPE used to define the prim as a sculpted prim (sculpty) or mesh of a specific type.

- `PRIM_TYPE_SPHERE` = 3 — Shape parameter for PRIM_TYPE used to define the prim as a sphere and configure its shape properties.

- `PRIM_TYPE_TORUS` = 4 — Shape parameter for PRIM_TYPE used to define the prim as a torus and configure its shape properties.

- `PRIM_TYPE_TUBE` = 5 — Shape parameter for PRIM_TYPE used to define the prim as a tube and configure its shape properties.

- `PSYS_PART_BF_DEST_COLOR` = 2 — Scales the RGBA values by the RGBA values of the destination.

- `PSYS_PART_BF_ONE` = 0 — PSYS_PART_BF_ONE

- `PSYS_PART_BF_ONE_MINUS_DEST_COLOR` = 4 — Scales the RGBA values by the inverted RGBA values of the destination.

- `PSYS_PART_BF_ONE_MINUS_SOURCE_ALPHA` = 9 — Scales the RGBA values by the inverted alpha values of the particle source.

- `PSYS_PART_BF_ONE_MINUS_SOURCE_COLOR` = 5 — Scales the RGBA values by the inverted RGBA values of the particle source.

- `PSYS_PART_BF_SOURCE_ALPHA` = 7 — Scales the RGBA values by the alpha values of the particle source.

- `PSYS_PART_BF_SOURCE_COLOR` = 3 — Scales the RGBA values by the RGBA values of the particle source.

- `PSYS_PART_BF_ZERO` = 1 — Zeros out the source or destination RGBA values.

- `PSYS_PART_BLEND_FUNC_DEST` = 25 — Integer parameter defining the destination blending function.

- `PSYS_PART_BLEND_FUNC_SOURCE` = 24 — Integer parameter defining the source blending function.

- `PSYS_PART_BOUNCE_MASK` = 0x4 — Particle flag causing particles to bounce off a plane at the emitter object's Z height.

- `PSYS_PART_EMISSIVE_MASK` = 0x100 — Particle flag that makes particles full-bright and unaffected by global lighting (sunlight). Otherwise, particles are lit by current global lighting or local point lights.

- `PSYS_PART_END_ALPHA` = 4 — Float parameter that determines the ending alpha (transparency) of the particles.

- `PSYS_PART_END_COLOR` = 3 — Vector parameter <r, g, b> that determines the ending color of the particles.

- `PSYS_PART_END_GLOW` = 27 — Float parameter that determines the ending glow value of the particles.

- `PSYS_PART_END_SCALE` = 6 — Vector parameter <sx, sy, z> defining the ending size of the particle billboard in meters (z-axis value is ignored).

- `PSYS_PART_FLAGS` = 0 — Integer bitfield parameter specifying the simulation flags for emitted particles. Multiple flags can be combined using bitwise OR (|).

- `PSYS_PART_FOLLOW_SRC_MASK` = 0x10 — Particle flag causing particle positions to remain relative to the position and movement of the emitter. Enabling this flag disables the PSYS_SRC_BURST_RADIUS rule.

- `PSYS_PART_FOLLOW_VELOCITY_MASK` = 0x20 — Particle flag causing particles to rotate and orient their vertical 'top' toward their direction of movement or emission. Otherwise, they remain vertically oriented with the top of the texture facing up.

- `PSYS_PART_INTERP_COLOR_MASK` = 0x1 — Particle flag causing the particle's color and alpha to smoothly interpolate from their START values to their END values over its lifetime.

- `PSYS_PART_INTERP_SCALE_MASK` = 0x2 — Particle flag causing the particle's size/scale to transition from its START setting to its END setting over its lifetime.

- `PSYS_PART_MAX_AGE` = 7 — Float parameter specifying the lifetime (age in seconds) of an individual particle before it dies.

- `PSYS_PART_RIBBON_MASK` = 0x400 — Particle flag that joins emitted particles into a continuous ribbon strip. Textures stretch to join adjacent edges. Width is controlled by the 'x' start/end scale; 'y' controls maximum visibility distance. Ribbon segments are not camera-facing, mimic the emitter's Z-axis, and require horizontal movement to render.

- `PSYS_PART_START_ALPHA` = 2 — Float parameter that determines the starting alpha (transparency) of the particles.

- `PSYS_PART_START_COLOR` = 1 — Vector parameter <r, g, b> that determines the starting color of the particles.

- `PSYS_PART_START_GLOW` = 26 — Float parameter that determines the starting glow value of the particles.

- `PSYS_PART_START_SCALE` = 5 — Vector parameter <sx, sy, z> defining the starting size of the particle billboard in meters (z-axis value is ignored).

- `PSYS_PART_TARGET_LINEAR_MASK` = 0x80 — Particle flag causing emitted particles to move in a straight, evenly-spaced line toward the PSYS_SRC_TARGET_KEY target. Ignores non-DROP patterns, radius, burst speeds, angles, omega, acceleration, and wind. Combining with bounce while target is below emitter deflects particles upward.

- `PSYS_PART_TARGET_POS_MASK` = 0x40 — Particle flag causing emitted particles to change course and travel toward the target specified by PSYS_SRC_TARGET_KEY during their lifetime. If no valid or reachable target is set, particles target the emitting prim itself.

- `PSYS_PART_WIND_MASK` = 0x8 — Particle flag that applies wind as a secondary force on the particles, damping their velocity toward the wind velocity.

- `PSYS_SRC_ACCEL` = 8 — Vector parameter <x, y, z> specifying the constant acceleration to apply to particles.

- `PSYS_SRC_ANGLE_BEGIN` = 22 — Float parameter specifying the angle in radians where particles will not be created (for ANGLE patterns).

- `PSYS_SRC_ANGLE_END` = 23 — Float parameter specifying the ending angle in radians to be filled with particles (for ANGLE patterns). If smaller than angle_begin, their roles are swapped.

- `PSYS_SRC_BURST_PART_COUNT` = 15 — Integer parameter specifying the number of particles to release in each burst.

- `PSYS_SRC_BURST_RADIUS` = 16 — Float parameter specifying the radial distance from the emitter's center at which particles are created.

- `PSYS_SRC_BURST_RATE` = 13 — Float parameter specifying the interval in seconds between particle bursts.

- `PSYS_SRC_BURST_SPEED_MAX` = 18 — Float parameter specifying the maximum initial speed of emitted particles.

- `PSYS_SRC_BURST_SPEED_MIN` = 17 — Float parameter specifying the minimum initial speed of emitted particles.

- `PSYS_SRC_INNERANGLE` = 10 — Float parameter specifying the inner angle of the arc for ANGLE or ANGLE_CONE patterns. The specified inner area will not contain particles.

- `PSYS_SRC_MAX_AGE` = 19 — Float parameter specifying the active duration of the particle system in seconds (0.0 means forever).

- `PSYS_SRC_OMEGA` = 21 — Vector parameter setting the angular velocity used to rotate the emission axis for ANGLE and ANGLE_CONE patterns.

- `PSYS_SRC_OUTERANGLE` = 11 — Float parameter specifying the outer angle of the arc for ANGLE or ANGLE_CONE patterns. The area between the outer and inner angles is filled with particles.

- `PSYS_SRC_PATTERN` = 9 — Integer parameter specifying the generation pattern (PSYS_SRC_PATTERN_*) used to emit particles.

- `PSYS_SRC_PATTERN_ANGLE` = 0x04 — Emission pattern that sprays particles outward in a flat circular, semi-circular, arc, or ray-shaped 2D area (around the prim's local X-axis) as defined by the start/end and inner/outer angle parameters.

- `PSYS_SRC_PATTERN_ANGLE_CONE` = 0x08 — Emission pattern that sprays particles outward in a 3D spherical, conical, or ring-shaped area defined by the start/end and inner/outer angle parameters. Can emulate the EXPLODE pattern if angles are set to 0.0 and PI.

- `PSYS_SRC_PATTERN_ANGLE_CONE_EMPTY` = 0x10 — Incomplete emission pattern that behaves identically to the DROP pattern. Intended to invert the ANGLE parameters to define an empty area where particles are not sprayed.

- `PSYS_SRC_PATTERN_DROP` = 0x01 — Emission pattern that drops particles at the source position with no initial velocity. Overrides burst radius, minimum speed, and maximum speed settings to 0.0.

- `PSYS_SRC_PATTERN_EXPLODE` = 0x02 — Emission pattern that shoots particles outward in all directions using the burst parameters.

- `PSYS_SRC_TARGET_KEY` = 20 — Key (UUID) of the target object that particles travel toward when PSYS_PART_TARGET_POS_MASK or PSYS_PART_TARGET_LINEAR_MASK is enabled.

- `PSYS_SRC_TEXTURE` = 12 — String parameter specifying the inventory name or UUID asset key of the texture used for the particles.

- `STATUS_BLOCK_GRAB` = 0x40 — Status flag (default FALSE) that blocks click-and-drag grab movements on unlinked prims or the root prim of a linkset. Useful for preventing physical objects from being trivially disturbed.

- `STATUS_BLOCK_GRAB_OBJECT` = 0x400 — Status flag that blocks click-and-drag grab movements on all prims across the entire linkset.

- `STATUS_BOUNDS_ERROR` = 1002 — Status code indicating that one or more arguments passed to the function had a bounds error.

- `STATUS_CAST_SHADOWS` = 0x200 — Unused legacy status flag intended to configure an object's ability to cast shadows.

- `STATUS_DIE_AT_EDGE` = 0x80 — Status flag (default TRUE) that causes the object to be deleted (and not returned) if it goes off-world (useful for bullets or rockets). Overridden by STATUS_RETURN_AT_EDGE.

- `STATUS_DIE_AT_NO_ENTRY` = 0x800 — Status flag (default FALSE) that causes the object to be deleted if it attempts to enter an unauthorized or full parcel. No-copy objects ignore this setting and remain in-world.

- `STATUS_DIE_ON_NO_REZZER` = 0x1000 — Status flag (default FALSE) that causes the object to be deleted if the rezzing object or agent is not present.

- `STATUS_INTERNAL_ERROR` = 1999 — Status code indicating an internal error occurred.

- `STATUS_MALFORMED_PARAMS` = 1000 — Status code indicating the function was called with malformed parameters.

- `STATUS_NOT_FOUND` = 1003 — Status code indicating that the specified object or item was not found.

- `STATUS_NOT_SUPPORTED` = 1004 — Status code indicating the requested feature is not supported.

- `STATUS_OK` = 0 — Status code indicating the function call completed successfully.

- `STATUS_PHANTOM` = 0x10 — Status flag (default FALSE) that makes the entire object phantom/non-colliding when set to TRUE, allowing avatars and objects to pass through it. It is a good idea to use this for most objects that move or rotate, but are non-physical. It is also useful for simulating volumetric lighting.

- `STATUS_PHYSICS` = 0x1 — Status flag (default FALSE) that controls whether the object responds to physical interactions, gravity, and forces.

- `STATUS_RETURN_AT_EDGE` = 0x100 — Status flag causing the object to be returned to its owner when it goes off-world, overriding STATUS_DIE_AT_EDGE.

- `STATUS_ROTATE_X` = 0x2 — Status flag (default TRUE) that allows physical rotation on the object's local X-axis. Setting to FALSE prevents physical rotation around the local X-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.

- `STATUS_ROTATE_Y` = 0x4 — Status flag (default TRUE) that allows physical rotation on the object's local Y-axis. Setting to FALSE prevents physical rotation around the local Y-axis. For example, a sit-and-spin device spins around the Z axis (up) but not around the X or Y axes.

- `STATUS_ROTATE_Z` = 0x8 — Status flag (default TRUE) that allows physical rotation on the object's local Z-axis. Setting to FALSE prevents physical rotation around the local Z-axis.

- `STATUS_SANDBOX` = 0x20 — Status flag (default FALSE) that restricts the object's physical movement to within its creation region and a short distance (10 to 20 meters) from its creation point to prevent it from escaping.

- `STATUS_TYPE_MISMATCH` = 1001 — Status code indicating that one or more arguments passed to the function had a type mismatch.

- `STATUS_WHITELIST_FAILED` = 2001 — Status code indicating a media domain whitelist check has failed.

- `TEXTURE_BLANK` = 5748decc-f629-461c-9a36-a35a221fe21f — Asset UUID representing the default 'Blank' texture.

- `TEXTURE_MEDIA` = 8b5fec65-8d8d-9dc5-cda8-8fdf2716e361 — Asset UUID representing the default 'Default Media' texture.

- `TEXTURE_PLYWOOD` = 89556747-24cb-43ed-920b-47caed15465f — Asset UUID representing the default 'Plywood' texture.

- `TEXTURE_TRANSPARENT` = 8dcd4a48-2d37-4909-9f78-f7a9eb4ef903 — Asset UUID representing the '*Default Transparent Texture' in the library (included with viewers).

- `VEHICLE_ANGULAR_DEFLECTION_EFFICIENCY` = 32 — Vehicle float parameter (range 0.0 to 1.0) acting as a scalar to modulate the strength of angular deflection, reorienting the vehicle's preferred axis toward its true velocity.

- `VEHICLE_ANGULAR_DEFLECTION_TIMESCALE` = 33 — Vehicle float parameter specifying the exponential timescale for the vehicle to achieve full angular deflection, reorienting its preferred axis of motion to match its true velocity.

- `VEHICLE_ANGULAR_FRICTION_TIMESCALE` = 17 — Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of angular velocity about the vehicle's preferred axes (at, left, up).

- `VEHICLE_ANGULAR_MOTOR_DECAY_TIMESCALE` = 35 — Vehicle float parameter specifying the exponential timescale (in seconds) for the angular motor's magnitude and effectiveness to decay toward zero.

- `VEHICLE_ANGULAR_MOTOR_DIRECTION` = 19 — Vehicle vector parameter specifying the direction and magnitude of the angular velocity (in radians per second) that the vehicle's angular motor attempts to achieve.

- `VEHICLE_ANGULAR_MOTOR_TIMESCALE` = 34 — Vehicle float parameter specifying the exponential timescale for the vehicle's angular motor to achieve full power and velocity.

- `VEHICLE_BANKING_EFFICIENCY` = 38 — Vehicle float parameter (range -1.0 to 1.0) controlling banking efficiency, where negative values lean out of turns and positive values lean into turns. This parameter makes banking affect steering; use angular motors to bank. 0.0 means no banking.

- `VEHICLE_BANKING_MIX` = 39 — Vehicle float parameter (range 0.0 (static) to 1.0) (dynamic) controlling the mix between static banking (scales only with roll angle) and dynamic banking (additionally scales with linear speed).

- `VEHICLE_BANKING_TIMESCALE` = 40 — Vehicle float parameter specifying the exponential timescale for the banking behavior to take full effect. This is another way to scale the strength of the banking effect, however it affects the term that is proportional to the difference between what the banking behavior is trying to do, and what the vehicle is actually doing.

- `VEHICLE_BUOYANCY` = 27 — Vehicle float parameter (range -1.0 to 1.0) defining buoyancy, where -1.0 represents double gravity and 1.0 represents full anti-gravity.

- `VEHICLE_FLAG_BLOCK_INTERFERENCE` = 0x400 — Vehicle flag that prevents attachments worn by passengers from pushing the vehicle via llPushObject or other scripting functions.

- `VEHICLE_FLAG_CAMERA_DECOUPLED` = 0x200 — Vehicle flag used with mouselook steering/banking. When set, the passenger's mouselook camera rotates independently of the vehicle's orientation.

- `VEHICLE_FLAG_HOVER_GLOBAL_HEIGHT` = 0x10 — Vehicle flag that forces the hover behavior to maintain a global height rather than hovering relative to the ground or water.

- `VEHICLE_FLAG_HOVER_TERRAIN_ONLY` = 0x8 — Vehicle flag that forces the hover behavior to ignore water height and hover exclusively relative to the terrain/land.

- `VEHICLE_FLAG_HOVER_UP_ONLY` = 0x20 — Vehicle flag preventing hover from pushing downward, allowing hovering vehicles to jump or fly above their designated hover height.

- `VEHICLE_FLAG_HOVER_WATER_ONLY` = 0x4 — Vehicle flag that forces the hover behavior to ignore terrain height and hover exclusively relative to water.

- `VEHICLE_FLAG_LIMIT_MOTOR_UP` = 0x40 — Vehicle flag that prevents ground vehicles from motoring upward into the sky. When combined with banking, banking strength decays when the vehicle is airborne (no longer colliding) to prevent steering mid-jump.

- `VEHICLE_FLAG_LIMIT_ROLL_ONLY` = 0x2 — Vehicle flag for vehicles with a vertical attractor that need to climb or dive, allowing airplanes to use the banking feature.

- `VEHICLE_FLAG_MOUSELOOK_BANK` = 0x100 — Vehicle flag that enables mouselook control, remapping left-right camera motions (yaw) to rotations about the vehicle's local X-axis.

- `VEHICLE_FLAG_MOUSELOOK_STEER` = 0x80 — Vehicle flag that enables steering via mouse, directing the angular motor to align the vehicle's local X-axis with the direction of the client-side camera.

- `VEHICLE_FLAG_NO_DEFLECTION_UP` = 0x1 — Vehicle flag that prevents linear deflection parallel to the world Z-axis, preventing ground vehicles (such as bumper cars) from climbing into the sky.

- `VEHICLE_FLAG_NO_FLY_UP` = 0x1 — Obsolete legacy name for VEHICLE_FLAG_NO_DEFLECTION_UP.

- `VEHICLE_HOVER_EFFICIENCY` = 25 — Vehicle float parameter (range 0.0 to 1.0) controlling hover damping, where 0.0 is bouncy and 1.0 is critically damped.

- `VEHICLE_HOVER_HEIGHT` = 24 — Vehicle float parameter specifying the height at which the vehicle attempts to hover. Set to 0.0 to disable hover.

- `VEHICLE_HOVER_TIMESCALE` = 26 — Vehicle float parameter specifying the timescale (period of time in seconds) for the vehicle to achieve its hover height.

- `VEHICLE_LINEAR_DEFLECTION_EFFICIENCY` = 28 — Vehicle float parameter (range 0.0 to 1.0) modulating the efficiency and strength of linear deflection. That is, its a simple scalar for modulating the strength of linear deflection.

- `VEHICLE_LINEAR_DEFLECTION_TIMESCALE` = 29 — Vehicle float parameter specifying the exponential timescale for the vehicle to redirect its linear velocity along its preferred X-axis. It is another way to specify how much time it takes for the vehicle's linear velocity to be redirected to its preferred axis of motion.

- `VEHICLE_LINEAR_FRICTION_TIMESCALE` = 16 — Vehicle vector parameter specifying the timescales (range [0.07, infinity) seconds per axis) for the exponential decay of linear velocity along the vehicle's preferred axes (at, left, up).

- `VEHICLE_LINEAR_MOTOR_DECAY_TIMESCALE` = 31 — Vehicle float parameter specifying the exponential timescale (in seconds) for the linear motor's magnitude and effectiveness to decay toward zero.

- `VEHICLE_LINEAR_MOTOR_DIRECTION` = 18 — Vehicle vector parameter specifying the direction and magnitude of the linear velocity (range [0, 30] m/s) that the vehicle's linear motor attempts to achieve.

- `VEHICLE_LINEAR_MOTOR_OFFSET` = 20 — Vehicle vector parameter specifying the offset from the vehicle's center of mass where the linear motor force is applied.

- `VEHICLE_LINEAR_MOTOR_TIMESCALE` = 30 — Vehicle float parameter specifying the exponential timescale for the vehicle to reach its full linear motor velocity.

- `VEHICLE_REFERENCE_FRAME` = 44 — Vehicle rotation parameter setting the orientation of the vehicle's preferred axes of motion (at, left, up) relative to its local geometric frame (x, y, z).

- `VEHICLE_TYPE_AIRPLANE` = 4 — Vehicle type constant for aircraft that use linear deflection for lift, banking to turn, and no hover.

- `VEHICLE_TYPE_BALLOON` = 5 — Vehicle type constant for balloons that use hover and friction but no deflection.

- `VEHICLE_TYPE_BOAT` = 3 — Vehicle type constant for boats that hover over water with high friction and minor angular deflection.

- `VEHICLE_TYPE_CAR` = 2 — Vehicle type constant for land vehicles that bounce along the ground and rely on external controls or timer events to drive their motors.

- `VEHICLE_TYPE_NONE` = 0 — Constant used to disable and turn off vehicle physics support on the object.

- `VEHICLE_TYPE_SLED` = 1 — Vehicle type constant for sliding vehicles that bump along the ground and prefer to move along their local X-axis.

- `VEHICLE_VERTICAL_ATTRACTION_EFFICIENCY` = 36 — Vehicle float parameter (range 0.0 to 1.0) controlling vertical attraction stability (0.0 is wobbly/bouncy, 1.0 is critically damped/firm) to keep the vehicle upright.

- `VEHICLE_VERTICAL_ATTRACTION_TIMESCALE` = 37 — Vehicle float parameter specifying the exponential timescale (in seconds) for the vehicle to rotate and align its local Z-axis (up) with the world Z-axis (vertical).

Appendix C entries: 303 constants.
