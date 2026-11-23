---
name: secondlife_linkpoint_design
description: "Build and theme Second Life viewer UI across React and Jetpack Compose using the six Linkpoint layout packs, 24+ Ktheme palettes, WCAG contrast enforcement, and Pass-2 HUD slots."
---

# Linkpoint Design System and Ktheme Adapter

## Separate layout geometry from Ktheme colour palettes

- Align visual tokens across `Kaleaon/react-linkpoint` / `Kaleaon/Linkpoint` (`@linkpoint/design-system`, TypeScript and React) and `Kaleaon/Linkpoint-stitch` (`com.example.linkpoint.designsystem`, Kotlin and Jetpack Compose) against the `Kaleaon/linkpoint-design` reference frame.

- Keep structural geometry and navigation (`LayoutPack` / `DesignLanguage`) orthogonal to colour mood (`Ktheme` JSON palettes) so any of the 6 layout packs can pair cleanly with any of the 24+ Ktheme palettes at runtime without hardcoded per-screen hex overrides.

- Treat synchronized `themes/*.json` files in `@linkpoint/design-system` as upstream artefacts from `Kaleaon/linkpoint-design`: conform strictly to the app-neutral Ktheme schema (`metadata`, `darkMode`, `colorScheme`, optional `effects` and `adaptation`) and keep typed token adapters in `src/` or `designsystem/`.

## Implement all six interchangeable layout packs faithfully

- **`Polished / Glass` (`glass` / `POLISHED`):** Translucent frosted spatial glass floaters (`12px`–`18px` / `16dp` radii, `panelOpacity ~0.84`), 1dp hairline borders, top-edge specular highlights, and soft elevation over the 3D scene.

- **`Terminal` (`terminal` / `TERMINAL`):** Monospace telemetry density (`JetBrains Mono`), `2dp`–`4px` crisp corners, `[HEADER]` and `> ACTION` framing, `0.26em` title tracking, phosphor borders, and subtle scanline texture.

- **`Sweep Console (LCARS)` (`sweep` / `LCARS`):** Follow CleverFerret Design's revised black-field LCARS reference — pure black (`#000000`) interior canvas void, concentric opposing-elbow split-frame geometry, `999px` pill end-caps, vertical rail segments that *are* interactive buttons (`01-COM`..`07-SYS`), and unboxed tabular telemetry readouts on black.

- **`Metro` (`tiles` / `METRO`):** Pure `0dp`/`0px` sharp corners, edge-to-edge flat typographic tiles, 3dp top accent blades, lowercase pivot headers, and zero filter-chip clutter.

- **`Rule & Rail` (`rules` / `RULE_AND_RAIL`):** Art Deco architectural discipline using `0px` sharp corners, `0.35em` tracked `Jost` headers, vertical accent rails, and 1dp horizontal hairline rules in place of filled card boxes.

- **`Press` (`press` / `PRESS`):** Print-inspired editorial hierarchy combining `Jost` headers with `Source Serif 4` / `Georgia` body copy at a `58ch` reading measure, `2px`–`6px` subtle radii, and crisp ink rules for long-form chat, IMs, and notecards.

## Organise the 24+ Ktheme palettes across the four families

- Group Ktheme selectors into the four canonical aesthetic families (plus optional community packs in `themes/community/`):
  - **Terminal & Neon:** `linkpoint-default` (`linkpoint_default`), `ink-terminal-modern`, `neo-noir-neon`, `slate-cyan`, `aurora-glass-night`.
  - **Console & Amber:** `lcars`, `cleverferret-gold` (`cleverferret_gold`), `firestorm`, `sl-classic` (`sl_classic`), `midnight-amber`, `obsidian-crimson` (plus community `lcars-tng`, `stargate-sg1`, `stargate-atlantis`).
  - **Metal & Jewel:** `slate-gunmetal`, `emerald-silver`, `royal-bronze`, `royal-silver`, `navy-gold`, `deep-purple-platinum`, `burgundy-rose-gold`, `charcoal-champagne`, `forest-copper`, `art-deco`, `windows-phone-metro`, `rose-gold` (plus community `metro-cyan`).
  - **Daylight:** `paper-ink`, `calm-clinical`, `solarpunk-civic`, `frutiger-aero`, `art-nouveau`.

## Enforce all-surface WCAG contrast and cockpit HUD ergonomics

- Run automatic WCAG 2.2 relative-luminance contrast correction (`contrast.ts` `luminance`, `contrastRatio`, `inkOn`, `ensureMinContrast`, and Kotlin `LinkpointContrast.kt`) across both `bg` and `surf` surfaces (`>= 4.5:1` for body/secondary/status text `ink2`, `sec`, `sec2`, `ok`, `err`, `warn`, `info`; `>= 3.0:1` for interactive chrome) while preserving hue in HSL space.

- Keep **85%+** of the mobile 3D viewport unobstructed in cockpit mode (`InWorldCockpitScreen.kt`): honour `WindowInsets.safeDrawing`, enforce `48dp` minimum touch targets, support thumb-zone dock (`BOTTOM`, `LEFT`, `RIGHT`) and thumbstick (`LEFT`, `RIGHT`, `HIDDEN`) placement, and provide a 1-tap **Zen 3D Mode**.

- Render scripted Second Life Avatar HUD attachments (`slots 31..38`, `ATTACH_HUD_CENTER_2` through `ATTACH_HUD_BOTTOM_RIGHT`) in a dedicated **Pass-2 orthographic OpenGL ES / WebGL overlay** inside `HudSafeRect` (depth-cleared over Pass-1 world geometry), and hit-test Pass-2 HUD quads with UV `STCoord` touch dispatch before orbiting the 3D world camera.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for `Kaleaon/linkpoint-design`, `Kaleaon/Linkpoint`, `Kaleaon/react-linkpoint`, and `Kaleaon/Linkpoint-stitch`.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Linkpoint Design Language](https://github.com/Kaleaon/linkpoint-design) for upstream Ktheme JSON definitions, layout pack specifications, and CleverFerret LCARS geometry rules.

- [Linkpoint Next](https://github.com/Kaleaon/Linkpoint) for `@linkpoint/design-system` (`packages/design-system`) in TypeScript and React.

- [Linkpoint Stitch](https://github.com/Kaleaon/Linkpoint-stitch) for Jetpack Compose `LinkpointTheme.kt`, `LinkpointChrome.kt`, `InWorldCockpitScreen.kt`, and Pass-2 OpenGL ES HUD composition.


## CleverFerret LCARS split-frame geometry in detail

- Never implement LCARS by merely colouring standard rounded cards orange and purple on a dark-grey background: set `canvasVoid` to pure `#000000` and confine saturated apricot, lilac, and periwinkle fills to the structural elbow frame and pill controls.

- Build the frame from concentric outer (`28dp`) and inner (`14dp`) elbow radii connecting the vertical side spine to the horizontal header bar, using opposing upper and lower sweeping elbows separated by `4px`–`6px` black gaps when splitting navigation from live telemetry.

- Make the left rail segments themselves the interactive buttons (`01-COM` Chat, `02-SEN` Radar, `03-NAV` Map, `04-INV` Inventory, `05-OBJ` Inspector, `06-HUD` HUDs, `07-SYS` Design Studio), and render interior radar/chat/parcel data unboxed with `tabular-nums` alignment.

## Dual-pass 3D + HUD viewport composition in detail

- Filter scene attachments strictly by `attachmentPoint`: body slots `1..30` and Bento/extended slots `39..55` attach to avatar skeleton bones in Pass 1 (perspective 3D), whereas slots `31..38` (`CENTER_2 = 31`, `TOP_RIGHT = 32`, `TOP_CENTER = 33`, `TOP_LEFT = 34`, `CENTER_1 = 35`, `BOTTOM_LEFT = 36`, `BOTTOM_CENTER = 37`, `BOTTOM_RIGHT = 38`) render only for the local agent in Pass 2 (orthographic 2D).

- Inset `HudSafeRect` clear of the top telemetry pill and bottom/rail dock so worn creator HUDs never occlude disconnect, Zen mode, or chat controls, and expose `hudGlobalScale` plus `hudTouchCaptureEnabled` in Design Studio (`07-SYS`) and HUD manager (`06-HUD`).

## Debugging playbook

- Symptom muted status badges or secondary labels turn unreadable on Daylight (`paper-ink`, `frutiger-aero`) or deep jewel (`burgundy-rose-gold`, `emerald-silver`) Kthemes: pass every semantic foreground token through `ensureMinContrast(token, bg, 4.5)` **and** `ensureMinContrast(adj, surf, 4.5)` instead of checking against `bg` alone.

- Symptom tapping an in-world AO or combat HUD spins the 3D camera instead of clicking the LSL button: ensure `NativeGlViewport` runs Pass-2 HUD quad hit-testing before Pass-1 camera drag/raycast when `hudTouchCaptureEnabled` is true, and compute accurate face `(u, v)` `STCoord` values for `ObjectGrab`.

- Symptom bottom telemetry pill collides with the bottom tool dock on compact phones: offset `TelemetryPosition.BOTTOM` by `56dp` whenever `DockPosition.BOTTOM` is active and wrap cockpit overlays in `WindowInsets.safeDrawing`.


## Deep references
Load these on demand from this skill's `references/` folder when the task needs exact data or full implementations rather than the summaries above.
- `references/ktheme-palettes-and-layouts.md` (21,782 bytes)
