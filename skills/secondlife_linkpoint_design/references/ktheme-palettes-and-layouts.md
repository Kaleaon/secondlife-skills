# Linkpoint Design System, Layout Packs & Ktheme Palette Reference

Derived from the `Kaleaon/linkpoint-design` reference frame, `@linkpoint/design-system` in `Kaleaon/Linkpoint` / `Kaleaon/react-linkpoint` (`packages/design-system/src/tokens/index.ts`, `src/tokens/contrast.ts`, `src/react/ConsoleFrame.tsx`, `themes/*.json`), and `Kaleaon/Linkpoint-stitch` (`com.example.linkpoint.designsystem.DesignModels.kt`, `LinkpointTheme.kt`, `LinkpointChrome.kt`, `InWorldCockpitScreen.kt`, `SceneModels.kt`). Written for Kaleaon's Linkpoint ecosystem.

---

## 1. Shared Visual Architecture (`linkpoint-design`)

Linkpoint separates **geometry & navigation grammar** (*Layout Packs*, 6 interchangeable structural modes) from **colour & surface mood** (*Ktheme Palettes*, 24+ app-neutral JSON theme files across 4 aesthetic families plus community packs), joined by a runtime **WCAG 2.2 relative-luminance contrast adapter** so every `(Layout Pack × Ktheme Palette)` combination remains legible over a live 3D Second Life viewport.

| Layer | TypeScript / React (`@linkpoint/design-system`) | Kotlin / Jetpack Compose (`Linkpoint-stitch`) | Upstream Source of Truth |
|---|---|---|---|
| **Layout packs (6)** | `LAYOUTS` (`glass`, `terminal`, `sweep`, `tiles`, `rules`, `press`) + `LayoutProvider` | `DesignLanguage` (`POLISHED`, `TERMINAL`, `LCARS`, `METRO`, extendable to `RULE_AND_RAIL`, `PRESS`) + `LinkpointPanelSurface` | `Kaleaon/linkpoint-design` layout specs |
| **Ktheme palettes (24+)** | `packages/design-system/themes/*.json` + `PALETTES` & `PALETTE_FAMILIES` | `LinkpointDesignTokens` + Ktheme JSON loader / `AccentPreset` | `linkpoint-design/docs/` Ktheme JSON schema (sync, never hand-diverge) |
| **Contrast adapter** | `src/tokens/contrast.ts` (`luminance`, `contrastRatio`, `inkOn`, `meetsAA`, `ensureMinContrast`) + `computeThemeTokens` | `LinkpointContrast.kt` (`relativeLuminance`, `contrastRatio`, `ensureMinContrast`) + `resolveLinkpointTokens` | WCAG 2.2 Criteria 1.4.3 (AA 4.5:1 text) & 1.4.11 (3:1 UI chrome) |
| **Cockpit & Pass-2 HUDs** | `World3DView` + floating HUD docks | `InWorldCockpitScreen.kt` + `LinkpointGlRenderer` + `HudAttachmentPoint` (`slots 31..38`) | Second Life `ATTACH_HUD_*` (`31..38`) specification |

---

## 2. The Six Interchangeable Layout Packs

Every layout pack defines corner radii (`rs` small, `rp` panel, `rl` sheet, `navr` nav), base spacing (`pad`, `gap`), display/body/mono typography, header transform, card edge treatment, and navigation model (`TABS`, `SWEEP`, `TILES`, `RAIL`, resolving to `floaters` on desktop viewports).

| # | Layout Pack | TS Key / Compose Enum | Nav Model | Radii (`rs` / `rp` / `rl`) | Typography (`dfont` / `font`) | Card & Chrome Grammar |
|---|---|---|---|---|---|---|
| 1 | **Polished / Glass** | `glass` / `POLISHED` (`POLISHED_DARK`) | `TABS` | `12px` / `16px` / `18px` (`12dp` / `16dp`) | `Space Grotesk` / `Plus Jakarta Sans` or `Nunito Sans` | Translucent frosted spatial glass (`panelOpacity ~0.84`), 1dp hairline outline, top-edge specular highlight, soft elevation over 3D world |
| 2 | **Terminal** | `terminal` / `TERMINAL` | `TABS` | `4px` / `4px` / `8px` (`2dp` crisp) | `JetBrains Mono` / `IBM Plex Mono` | Monospace telemetry density, `[HEADER]` brackets, `> ACTION` prompts, `0.26em` tracking, crisp phosphor borders, subtle 4dp scanline texture |
| 3 | **Sweep Console (LCARS)** | `sweep` / `LCARS` | `SWEEP` | `999px` pill / `22px` / `28px` (`99dp` pill / `24dp`) | `Antonio` or `Space Grotesk` (`0.16em` uppercase) + `JetBrains Mono` | **CleverFerret Design revised black-field LCARS reference:** pure `#000000` canvas void, concentric opposing-elbow split-frame geometry, rail segments *are* interactive buttons (`01-COM`..`07-SYS`), `999px` pill end-caps, and **unboxed** tabular readouts on black |
| 4 | **Metro** | `tiles` / `METRO` | `TILES` | `0px` / `0px` / `0px` (`0dp` sharp) | `Open Sans` / `Space Grotesk` (lowercase pivot headers) | Pure `0dp` sharp corners, flat typographic live tiles, 3dp top accent blade, pivot segmented tabs, no filter chip clutter |
| 5 | **Rule & Rail** | `rules` / `RULE_AND_RAIL` | `RAIL` | `0px` / `0px` / `0px` (`0dp` architectural) | `Jost` (`0.35em` tracked titles) | Art Deco architectural discipline: crisp 1dp hairline horizontal rules and vertical accent rails instead of heavy box fills (`gap: 0px`) |
| 6 | **Press** | `press` / `PRESS` | `TABS` | `2px` / `3px` / `6px` (`2dp`–`4dp`) | `Jost` display + `Source Serif 4` / `Georgia` body | Print-editorial hierarchy: `58ch` comfortable reading measure for chat/IM/notecards, crisp ink divider rules, tactile paper/card surfaces |

### 2.1 CleverFerret Revised Black-Field LCARS Split-Frame Specification

When implementing or auditing `Sweep Console (LCARS)` (`sweep` / `DesignLanguage.LCARS`), follow CleverFerret Design's revised black-field reference rather than generic rounded-box theming:

1. **Pure Black Field (`#000000`):** The interior readout canvas (`canvasVoid`) is pure `#000000` (not grey cards inside grey boxes). Colour lives exclusively in the structural frame bars, pill buttons, and typographic ink.
2. **Concentric Opposing-Elbow Split Frame:**
   - Upper frame: sweeping L-elbow with outer radius `28dp` (`topStart = 28.dp`) and concentric inner fillet radius `14dp` (`quadraticTo(spineW, topH, spineW, topH + innerR)`), joining a vertical left spine (`16dp`–`140px` rail) to a horizontal top header bar terminated by a `999px` pill end-cap.
   - Lower split frame (multi-zone consoles): opposing L-elbow mirroring the upper sweep across a crisp `4px`–`6px` black separation gap, dividing primary navigation/header controls from live region/chat/radar telemetry.
3. **Rail Segments Are Buttons:** Vertical spine segments (`accentPrimary` apricot, `accentSecondary` lilac, `accentTertiary` periwinkle) carry right-aligned numeric/functional codes (`01-COM`, `02-SEN`, `03-NAV`, `04-INV`, `05-OBJ`, `06-HUD`, `07-SYS`) separated by `4px` black gaps — never float standard Material rounded buttons inside an LCARS rail.
4. **Unboxed Telemetry Readouts:** Inside the elbow cavity, render chat lines, radar distances, FPS, and parcel coordinates directly on the `#000000` field with tabular monospace alignment (`font-variant-numeric: tabular-nums`) and no per-row card borders.

---

## 3. Complete Ktheme Palette Catalogue (28 Built-in + 4 Community Packs)

All JSON files under `packages/design-system/themes/` conform to the app-neutral **Ktheme** schema (`metadata`, `darkMode`, `colorScheme`, optional `effects` and `adaptation`) synchronized from `Kaleaon/linkpoint-design`.

### Family 1: Terminal & Neon (Dark-First Control & Telemetry)

| Ktheme ID (`themes/*.json`) | Short Key | Display Name | `darkMode` | `primary` | `secondary` | `background` | `surface` | Character |
|---|---|---|---|---|---|---|---|---|
| `linkpoint_default` (`linkpoint-default.json`) | `linkpoint-default` | Linkpoint Blue | `true` | `#1976D2` | `#00BCD4` | `#1A1A1A` | `#2D2D2D` | Default Linkpoint cobalt & cyan on dark neutral |
| `ink-terminal-modern` | `ink` | Ink Terminal Modern | `true` | `#6CFF9A` | `#3E4E5E` | `#0A1112` | `#101A1C` | Phosphor mint-green on deep CRT ink |
| `neo-noir-neon` | `noir` | Neo-Noir Neon | `true` | `#AA43FF` | `#00D1FF` | `#090A10` | `#111420` | Constrained electric violet & cyan on midnight |
| `slate-cyan` | `slatec` | Slate Cyan | `true` | `#00D9FF` | `#2A333D` | `#1A1F24` | `#232930` | Cool industrial slate with vivid cyan |
| `aurora-glass-night` | `aurora` | Aurora Glass Night | `true` | `#6DE8FF` | `#8C7CFF` | `#0A1224` | `#101C33` | Polar cyan & periwinkle glass on deep night blue |

### Family 2: Console & Amber (Bridge, Viewer Heritage & Warm Tactical)

| Ktheme ID (`themes/*.json`) | Short Key | Display Name | `darkMode` | `primary` | `secondary` | `background` | `surface` | Character |
|---|---|---|---|---|---|---|---|---|
| `lcars` | `lcars` | LCARS | `true` | `#F2A65A` | `#C5678D` | `#120C1C` | `#1C132A` | Warm apricot, mauve, and violet (`#A485F7`) console |
| `cleverferret_gold` (`cleverferret-gold.json`) | `cleverferret-gold` | CleverFerret Gold | `true` | `#E5A00D` | `#B8860B` | `#1E1E1E` | `#2A2A2A` | Signature CleverFerret warm gold on dark charcoal |
| `firestorm` | `firestorm` | Firestorm Viewer | `true` | `#E85D00` | `#FFB366` | `#121212` | `#1E1E1E` | Classic Firestorm TPV blaze orange on near-black |
| `sl_classic` (`sl-classic.json`) | `sl-classic` | Second Life Viewer | `true` | `#4AA3DF` | `#7FB3D5` | `#1B2430` | `#263548` | Classic Linden Lab viewer sky-blue on deep slate |
| `midnight-amber` | `amber` | Midnight Amber | `true` | `#FFBF00` | `#D4A76A` | `#0C1824` | `#15202E` | Avionics amber on midnight navy |
| `obsidian-crimson` | `crimson` | Obsidian Crimson | `true` | `#DC143C` | `#A8505A` | `#0A0A0A` | `#141414` | High-drama crimson on pure obsidian |

### Family 3: Metal & Jewel (Architectural, Metallic & Editorial Dark)

| Ktheme ID (`themes/*.json`) | Short Key | Display Name | `darkMode` | `primary` | `secondary` | `background` | `surface` | Character |
|---|---|---|---|---|---|---|---|---|
| `slate-gunmetal` | `slateg` | Slate Gunmetal | `true` | `#8F9CA8` | `#2D3844` | `#1A2029` | `#232C38` | Brushed gunmetal steel on slate |
| `emerald-silver` | `emerald` | Emerald Silver | `true` | `#C0C0C0` | `#50C878` | `#0D3B2E` | `#1A5544` | Sterling silver & emerald jewel tones |
| `royal-bronze` | `royalb` | Royal Bronze | `true` | `#CD7F32` | `#2D1550` | `#1A0A30` | `#220D40` | Aged bronze over imperial purple |
| `royal-silver` | `royals` | Royal Silver | `true` | `#C0C0C0` | `#2A1F50` | `#1A1535` | `#211A40` | Bright silver over royal indigo |
| `navy-gold` | `navy` | Navy Gold | `true` | `#D4AF37` | `#4A90E2` | `#0A1630` | `#1A2645` | Maritime dress navy with gold leaf |
| `deep-purple-platinum` | `deep` | Deep Purple Platinum | `true` | `#E5E4E2` | `#2E1A50` | `#1A0F2E` | `#24153D` | Platinum highlights on deep plum |
| `burgundy-rose-gold` | `burgundy` | Burgundy Rose Gold | `true` | `#B76E79` | `#4D1A2A` | `#2D0F1A` | `#3D1525` | Rose gold metallic on rich burgundy |
| `charcoal-champagne` | `charcoal` | Charcoal Champagne | `true` | `#F7E7CE` | `#3D3D3D` | `#1F1F1F` | `#2A2A2A` | Warm champagne ink on matte charcoal |
| `forest-copper` | `forest` | Forest Copper | `true` | `#B87333` | `#1A3D1A` | `#0D1F0D` | `#152915` | Burnished copper on deep pine green |
| `art-deco` | `deco` | Art Deco | `true` | `#D4AF37` | `#F4E7CF` | `#0B0A0A` | `#141314` | Stepped brass-gold & ivory on lacquer black |
| `windows-phone-metro` | `metro` | Windows Phone Metro | `true` | `#00AEEF` | `#005A9E` | `#001A33` | `#002448` | Vivid Metro cyan tiles on deep navy |
| `rose-gold` | `rose` | Rose Gold | `true` | `#C1818B` | `#D4A5A5` | `#3D1F2B` | `#4D2F3B` | Warm rose-gold & blush on velvet plum |

### Family 4: Daylight (Light-First High-Clarity & Outdoor Mobile)

| Ktheme ID (`themes/*.json`) | Short Key | Display Name | `darkMode` | `primary` | `secondary` | `background` | `surface` | Character |
|---|---|---|---|---|---|---|---|---|
| `paper-ink` | `paper` | Paper & Ink | `false` | `#2C2C2C` | `#595959` | `#F0F0EB` | `#FAF9F6` | Hueless warm paper & editorial ink; maximum daylight legibility |
| `calm-clinical` | `calm` | Calm Clinical | `false` | `#38779E` | `#61B48B` | `#F5FAFD` | `#FFFFFF` | Low-fatigue Ice/Cerulean daylight clarity |
| `solarpunk-civic` | `solarpunk` | Solarpunk Civic | `false` | `#38B56A` | `#4FAEEA` | `#F2FBF4` | `#FBFFFC` | Botanical green & sky blue on sunlit leaf |
| `frutiger-aero` | `aero` | Frutiger Aero | `false` | `#39B6F0` | `#79D87E` | `#EAF7FF` | `#F7FCFF` | Glossy sky-and-meadow translucent daylight glass |
| `art-nouveau` | `nouveau` | Art Nouveau | `false` | `#7B5737` | `#769762` | `#F6F0E6` | `#FFF8EE` | Warm parchment, chestnut wood, and sage linework |

### Community Ktheme Packs (`themes/community/*.json`)

| Ktheme ID | Display Name | `darkMode` | `primary` | `secondary` | `background` | `surface` | Character |
|---|---|---|---|---|---|---|---|
| `lcars-tng` | LCARS — TNG | `true` | `#F2A65A` | `#A485F7` | `#120C1C` | `#1C132A` | TNG-era amber & lilac tuned for Sweep Console |
| `metro-cyan` | Metro Cyan | `true` | `#00AEEF` | `#2D89EF` | `#001A33` | `#002448` | High-contrast Windows Phone cyan variant |
| `stargate-atlantis` | Stargate Atlantis | `true` | `#C4A062` | `#6FCFE8` | `#0B1B2E` | `#133355` | Atlantean blue glass & Deco bronze |
| `stargate-sg1` | Stargate SG-1 | `true` | `#FFC15A` | `#4FE0FF` | `#04141C` | `#0E2C3E` | Iris-bronze & event-horizon teal console |

---

## 4. All-Surface WCAG 2.2 Relative-Luminance Contrast Correction

Because users can pair **any** Ktheme JSON palette (including community or custom user-imported themes) with **any** of the 6 layout packs, raw palette tokens (`ink2`, `sec`, `sec2`, `ok`, `err`, `warn`, `info`, `onPrimary`) can fail WCAG contrast when placed on `bg`, `surf`, or `surf2`.

### Algorithm (`packages/design-system/src/tokens/contrast.ts` & `LinkpointContrast.kt`)

1. **sRGB linearisation & relative luminance (`L`):**
   For each 8-bit channel $c \in \{R, G, B\}$, let $c_s = c / 255$:
   $$f(c_s) = \begin{cases} c_s / 12.92 & \text{if } c_s \le 0.03928 \\ ((c_s + 0.055) / 1.055)^{2.4} & \text{otherwise} \end{cases}$$
   $$L = 0.2126 \cdot f(R_s) + 0.7152 \cdot f(G_s) + 0.0722 \cdot f(B_s)$$
2. **Contrast ratio (`1:1` to `21:1`):**
   $$\text{CR}(A, B) = \frac{\max(L_A, L_B) + 0.05}{\min(L_A, L_B) + 0.05}$$
3. **Hue-preserving lightness walk (`ensureMinContrast(fg, bg, minRatio = 4.5)`):**
   - If `CR(fg, bg) >= minRatio`, return `fg` unchanged.
   - Convert `fg` to HSL `(h, s, l)`. Choose primary walk direction `step = +1` (lighten) when `L_bg < 0.5 || L_fg >= L_bg`, else `-1` (darken).
   - Step `l` by `1%` toward `[0, 100]`, returning the **first** candidate meeting `minRatio` so hue `h` and saturation `s` stay maximally faithful to the Ktheme author's intent.
   - If clamping `l` in the primary direction still misses `minRatio` (e.g. mid-luminance saturated surface), try the opposite `l` direction, and finally desaturate `s` in `5%` steps at `l = 98%` (or `2%`) until `minRatio` (`4.5:1` for text, `3.0:1` for non-text chrome) is met.
4. **Dual-surface pass (`computeThemeTokens`):**
   Adjust semantic tokens (`ink2`, `sec`, `sec2`, `ok`, `err`, `warn`, `info`) sequentially against **both** `bg` and `surf`, and compute `onPrimary` / `onSecondary` via `inkOn(pri, [onpri, "#FFFFFF", "#000000"])`.

### Reference Kotlin Adapter (`LinkpointContrast.kt` for Jetpack Compose)

```kotlin
package com.example.linkpoint.designsystem

import androidx.compose.ui.graphics.Color
import androidx.core.graphics.ColorUtils
import kotlin.math.max
import kotlin.math.min
import kotlin.math.pow

object LinkpointContrast {
    fun relativeLuminance(color: Color): Float {
        fun ch(v: Float): Float =
            if (v <= 0.03928f) v / 12.92f else ((v + 0.055f) / 1.055f).pow(2.4f)
        return 0.2126f * ch(color.red) + 0.7152f * ch(color.green) + 0.0722f * ch(color.blue)
    }

    fun contrastRatio(a: Color, b: Color): Float {
        val la = relativeLuminance(a)
        val lb = relativeLuminance(b)
        return (max(la, lb) + 0.05f) / (min(la, lb) + 0.05f)
    }

    fun inkOn(background: Color, candidates: List<Color> = emptyList()): Color {
        return (candidates + listOf(Color.White, Color.Black))
            .maxByOrNull { contrastRatio(background, it) } ?: Color.White
    }

    fun ensureMinContrast(fg: Color, bg: Color, minRatio: Float = 4.5f): Color {
        if (contrastRatio(fg, bg) >= minRatio) return fg
        val bgLum = relativeLuminance(bg)
        val fgLum = relativeLuminance(fg)
        val hsl = FloatArray(3)
        ColorUtils.RGBToHSL(
            (fg.red * 255f).toInt().coerceIn(0, 255),
            (fg.green * 255f).toInt().coerceIn(0, 255),
            (fg.blue * 255f).toInt().coerceIn(0, 255),
            hsl
        )
        val shiftUp = bgLum < 0.5f || fgLum >= bgLum
        val origL = hsl[2]
        var best = fg
        var bestRatio = contrastRatio(fg, bg)

        for (dir in listOf(if (shiftUp) 0.01f else -0.01f, if (shiftUp) -0.01f else 0.01f)) {
            var curL = origL
            repeat(100) {
                curL += dir
                if (curL !in 0f..1f) return@repeat
                val cand = Color(ColorUtils.HSLToColor(floatArrayOf(hsl[0], hsl[1], curL)))
                val ratio = contrastRatio(cand, bg)
                if (ratio > bestRatio) {
                    bestRatio = ratio
                    best = cand
                }
                if (ratio >= minRatio) return cand
            }
        }
        val peakL = if (shiftUp) 0.98f else 0.02f
        var curS = hsl[1]
        while (curS >= 0f) {
            val cand = Color(ColorUtils.HSLToColor(floatArrayOf(hsl[0], curS, peakL)))
            val ratio = contrastRatio(cand, bg)
            if (ratio >= minRatio) return cand
            if (ratio > bestRatio) {
                bestRatio = ratio
                best = cand
            }
            curS -= 0.05f
        }
        return best
    }
}
```

---

## 5. Mobile Thumb-Zone Ergonomics & Responsive Breakpoints

A Second Life mobile/tablet viewer must never bury the 3D world under desktop-style stacked floaters.

### Viewport & Touch Rules (`InWorldCockpitScreen.kt` & `tokens/index.ts`)
- **85%+ Unobstructed 3D Viewport:** Keep default cockpit chrome minimal (compact top-start telemetry pill + bottom or side tool dock + translucent virtual thumbstick), and provide a 1-tap **Zen 3D Mode** (`zenMode`) that hides all chrome except a tiny translucent restore eye button in `TopEnd`.
- **Thumb-Zone Customisation (`PersonalDesignState`):**
  - `DockPosition`: `BOTTOM` (one-handed thumb bar), `LEFT` (LCARS rail), or `RIGHT` (right-handed rail).
  - `JoystickSide`: `LEFT` thumb, `RIGHT` thumb (One-Handed Explorer preset), or `HIDDEN` (touch-to-walk / gamepad).
  - `TelemetryPosition`: `COMPACT` pill, `TOP` edge, or `BOTTOM` edge (offset cleanly above `BOTTOM` dock by `56dp` so bars never overlap).
- **Minimum Touch Targets & Insets:** Enforce `48dp` (`minimumInteractiveComponentSize()`) on every action button, dock icon, and close button, and wrap HUD chrome in `WindowInsets.safeDrawing` so camera cutouts, Dynamic Islands, and gesture navigation bars never clip controls.
- **Responsive Breakpoints (`BREAKPOINTS`):**
  - `compact` (`< 600dp`): Single-floater modal/sheet over 3D world; bottom tabs (`tabs`) or `sweep` / `tiles`.
  - `medium` (`600dp..839dp`) & wide cockpit (`>= 680dp`): Side-anchored non-blocking floater cards (`widthIn(max = 380.dp)`) + rail navigation (`rail`).
  - `expanded` (`>= 1200dp` / desktop): Multi-floater workspace (`floaters`) with `MULTI_PANE_SPECS` (`splitRatio = 0.44`, `minPaneWidth = 320px`).

---

## 6. Pass-2 HUD Viewport Composition (`slots 31..38`)

In Second Life, scripted Avatar HUDs (animation overrides, combat meters, radar/collar HUDs, mesh body alpha HUDs) are real 3D prim/mesh linksets attached to **slots `31..38`**, rendered in a **second orthographic OpenGL ES / WebGL pass** over the 3D world *below* native Compose/React floaters.

### Canonical HUD Attachment Slot Map (`SceneModels.kt` & `lsl_definitions.yaml`)

| Slot ID | LSL Constant | Enum (`HudAttachmentPoint`) | Short Code | Safe-Rect Anchor `(anchorX, anchorY)` |
|---|---|---|---|---|
| `31` | `ATTACH_HUD_CENTER_2` | `CENTER_2` | `CTR2` | `(0.5, 0.5)` — Viewport centre (secondary layer) |
| `32` | `ATTACH_HUD_TOP_RIGHT` | `TOP_RIGHT` | `TR` | `(1.0, 0.0)` — Top-right corner inside `HudSafeRect` |
| `33` | `ATTACH_HUD_TOP_CENTER` | `TOP_CENTER` | `TC` | `(0.5, 0.0)` — Top-centre edge inside `HudSafeRect` |
| `34` | `ATTACH_HUD_TOP_LEFT` | `TOP_LEFT` | `TL` | `(0.0, 0.0)` — Top-left corner inside `HudSafeRect` |
| `35` | `ATTACH_HUD_CENTER_1` | `CENTER_1` | `CTR1` | `(0.5, 0.5)` — Viewport centre (primary layer) |
| `36` | `ATTACH_HUD_BOTTOM_LEFT` | `BOTTOM_LEFT` | `BL` | `(0.0, 1.0)` — Bottom-left corner inside `HudSafeRect` |
| `37` | `ATTACH_HUD_BOTTOM` | `BOTTOM_CENTER` | `BC` | `(0.5, 1.0)` — Bottom-centre edge inside `HudSafeRect` |
| `38` | `ATTACH_HUD_BOTTOM_RIGHT` | `BOTTOM_RIGHT` | `BR` | `(1.0, 1.0)` — Bottom-right corner inside `HudSafeRect` |

### Dual-Pass Rendering & Touch-Dispatch Rules

1. **Pass 1 (Perspective 3D World):** Clear colour + depth buffers; render sky/EEP, water, terrain, world prims, avatars, and body attachments (`attachmentPoint` in `1..30` and `39..55`). Never render `31..38` in world space!
2. **Pass 2 (Orthographic HUD Overlay):** Clear the **depth buffer only** (`glClear(GL_DEPTH_BUFFER_BIT)`), switch to a 2D orthographic projection scaled by `hudGlobalScale` inside `HudSafeRect` (inset from the top telemetry pill and bottom dock so scripted HUD buttons never collide with viewer chrome), and render only **self-avatar** attachments on slots `31..38` with unlit/fullbright HUD shading.
3. **Touch-First Hit Testing (`hudTouchCaptureEnabled`):**
   - On pointer down/up in `NativeGlViewport`, test Pass-2 HUD quads (`slots 31..38`) **first** in reverse draw order before casting a 3D world picking ray.
   - When a HUD face/button (`HudFaceButton` UV sub-rect `[uMin..uMax, vMin..vMax]`) is hit, consume the gesture (do not orbit the 3D camera!) and send `ObjectGrab` / `ObjectGrabUpdate` / `ObjectDeGrab` with accurate face index and `STCoord` `(u, v)` UV coordinates so LSL `touch_start` / `llDetectedTouchST(0)` scripts fire identically to the desktop viewer.
   - Provide a quick toggle (`hudTouchCaptureEnabled` + per-slot visibility in the `06-HUD` floater) so oversized creator HUDs can be collapsed or click-through on small phone screens.
