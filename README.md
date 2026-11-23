# secondlife-skills

Second Life coding skills for Muse (Muse Spark) and other skill loaders — covering the whole open-source Second Life ecosystem, with deep generated references from canonical upstream sources and complete multi-language implementations of the protocol stack.

## Skills

| Skill | Covers |
|---|---|
| `skills/secondlife_development` | Router + cross-check stack, repo catalogue, licensing map |
| `skills/secondlife_protocol` | Login, UDP circuit, message template, capabilities, EventQueueGet, LLSD — plus a generated per-message UDP reference (483 messages) |
| `skills/secondlife_viewer_cpp` | Official viewer + Firestorm/Alchemy, `indra/` map, builds, TPV policy — plus generated viewer settings reference (1,495 settings) and full source-tree indexes for viewer, Firestorm, and Alchemy |
| `skills/secondlife_client_libraries` | LibreMetaverse 3.x, Lumiya-Redux, Radegast, node-metaverse, TS/Kotlin porting — plus a generated LibreMetaverse API catalogue scanned from source |
| `skills/secondlife_lsl_scripting` | LSL/SLua/OSSL — plus generated references for 529 LSL functions, 1,082 constants, 43 events, 133 enum groups, from `secondlife/lsl-definitions` |
| `skills/secondlife_opensim_server` | OpenSim, ROBUST, region modules, physics, scripting engines — plus generated OSSL function reference, OpenSim LSL implementation index, and annotated OpenSim.ini / Robust.ini references |
| `skills/secondlife_assets_mesh_texture` | Prims, LLMesh, JPEG2000, glTF PBR, BoM, Animesh, EEP — plus generated asset/inventory enum reference |


## Code in every language

The protocol and client stack (LLSD, zerocode, UDP circuit, caps, login, EventQueueGet) is implemented end-to-end in each of these, as full commented reference code in the skills' `references/` folders:

| Language | File | Lives in |
|---|---|---|
| Rust | `code-rust.md` | `secondlife_protocol` |
| Go | `code-go.md` | `secondlife_protocol` |
| Python | `code-python.md` | `secondlife_protocol` |
| React / TypeScript | `code-react-typescript.md` | `secondlife_client_libraries` |
| Kotlin (Android) | `code-kotlin.md` | `secondlife_client_libraries` |
| Java + C++ | `code-java-cpp.md` | `secondlife_client_libraries` |
| C# (LibreMetaverse programs) | `code-csharp.md` | `secondlife_client_libraries` |

Plus per-message stubs for all 483 UDP messages in TypeScript, Kotlin, Rust, and C# (`message-stubs-*.md` in `secondlife_protocol`), 34 complete LSL scripts (`examples-lsl.md`), and 21 worked client examples (`examples-clients.md`).

Total instruction size: **8.2 MB and growing** across 7 skills and 70+ files. **There is no size cap.** The layout is built to scale to **1 GB or more** of instructions: each `SKILL.md` stays a lean routing layer (frontmatter + judgement + links), and all bulk lives in per-topic files under `references/` that a loader pulls in only when a task needs them. Grow the corpus by adding reference files and regenerating catalogues — never by bloating `SKILL.md`.

## Verifying the conversions

`verify_refs.py` checks every converted reference against its canonical source: SKILL.md frontmatter and `skill.yaml` validity, markdown fence balance and UTF-8 cleanliness for all files, JSON validity of the complete LSL definitions dump, and exact entry-count matches (529 LSL functions, 483 UDP messages in the catalogue and in all four stub languages, 1,495 viewer settings, 2,438 Firestorm settings, per-file sizes in the master index). Run it after any regeneration:

```bash
python3 verify_refs.py   # PASS 271 checks, FAIL 0
```

Each skill folder contains `SKILL.md` (with YAML frontmatter: `name` + `description`), `skill.yaml`, and a `references/` folder.

## Install

Clone this repo and copy the skill folders into your Muse custom-skills directory (`~/workspace/custom-skills/`), or point your loader at `skills/`.

```bash
git clone https://github.com/Kaleaon/secondlife-skills.git
cp -r secondlife-skills/skills/secondlife_* ~/workspace/custom-skills/
```

## Regenerating the references

The `references/` catalogues are generated from canonical upstream sources (Linden Lab `lsl-definitions` and message template, viewer `settings.xml`, LibreMetaverse and OpenSim source trees). The generators are `gen_refs.py` through `gen_refs7.py` in this repo; fetched upstream files live in `sources/` (git-ignored). Re-run them after upstream revs to refresh the catalogues.

## Key traps encoded in these skills

- There is **no** `github.com/secondlife/llsd` repo (404) — use `secondlife/python-llsd` + LibreMetaverse.StructuredData.
- The master message template has been stale before — always diff against the viewer copy.
- Catznip, Kokua, and Black Dragon have **no verified GitHub repo** — check the TPV Directory source link.
- `github.com/opensim/opensim` is a **mirror** — canonical git is at opensimulator.org.

## Licence

Skill text: written for Kaleaon. Generated references derive from upstream projects under their own licences (MIT for lsl-definitions, BSD-3 for LibreMetaverse and OpenSim, LGPL-2.1 for viewer-derived indexes) — see each reference file's header for its source.
