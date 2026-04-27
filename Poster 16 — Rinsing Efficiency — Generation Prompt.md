---
Project: Plating Posters Inc
Poster Number: 16
Title: "Rinsing Efficiency — The Hidden Cost of Poor Rinsing"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-20T00:00:00
Source: Poster 16 — Rinsing Efficiency — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Rinsing
  - DragOut
  - WaterConservation
  - v1
---

# Claude Chat Generation Prompt — Poster #16
## Rinsing Efficiency — The Hidden Cost of Poor Rinsing
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup v2.0. Adapted for Claude chat visual generation (2026-04-20). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS. The output should be a finished, print-ready poster design.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first** (dark background). The Light edition remap table is provided at the end.
- Follow the design specifications in each Phase below. They describe WHAT to render — layout zones, text content, colors, typography, and visual elements.
- Every color is specified as a hex code. Every font, size, and weight is specified. Follow them exactly.
- Chemical formulas use Unicode subscript/superscript characters. Reproduce them exactly as written in this document.
- Prioritize **readability at distance** — this poster will be read from 3-8 feet away on a shop wall.

---

## Phase 1 — Design Foundation

### Artboard
- **Size:** 24 x 36 inches (portrait)
- **Background color (Dark edition):** `#1A1F2E` (Gunmetal Dark)

### Typography
| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Headlines | Barlow Condensed | ExtraBold (800) | All caps, tight letter-spacing (-4) |
| Subheadings | Barlow | SemiBold (600) | Title case |
| Body text | Inter | Regular (400) / Medium (500) | Sentence case |
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for technical values |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Single-rinse accent, warnings, drag-out factors |
| Teal | `#2EC4B6` | Counterflow accent, water indicators, equation highlight |
| Emerald | `#27AE60` | Water savings percentages, positive outcomes |
| Coral | `#E05C5C` | Poor rinsing consequences, cost warnings |
| Mid Slate | `#3A4055` | Tank outlines, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Callout box fills, equation background |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Part shapes in tank diagrams |
| Teal Light | `#5ED4C8` | Middle rinse tank water fill |
| Teal Lightest | `#A0E8E0` | Cleanest rinse tank water fill |

### Layout Safe Zones
- **0.5" margin** on all sides (safe zone for print trimming)
- All content must stay within the 23" x 35" live area

---

## Phase 2 — Zone 1: Header Band

This zone occupies the top 2.9 inches. Headline, subheading, and tagline — left-aligned across full width.

### Step 6 — Place the headline
1. Add a heading text element: Type: `RINSING EFFICIENCY`
2. Font: Barlow Condensed ExtraBold, Size: `96`, Color: `#F0EDE8`, Letter spacing: `-4`, Alignment: Left
3. Position: X: **0.5"**, Y: **0.5"**. Width: `23.0"`.

### Step 7 — Place the subheading
1. Add text: `The Hidden Cost of Poor Rinsing`
2. Font: Barlow SemiBold, Size: `40`, Color: `#2EC4B6` (Teal), Alignment: Left
3. Position: X: **0.5"**, Y: approximately **1.6"**.

### Step 8 — Place the tagline
1. Add text: `Every plating line uses water. Most use far more than necessary.`
2. Font: Barlow SemiBold, Size: `22`, Color: `#F0EDE8`, Transparency: **65%**
3. Position: X: **0.5"**, Y: approximately **2.3"**.

### Step 9 — Group all of Zone 1
Select headline, subheading, tagline. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Counterflow Rinse Diagram (HERO)

This zone occupies Y: 2.9" to 14.5" (~11.6" tall). The hero illustration shows three rinse tanks with parts moving left-to-right (dirtiest to cleanest) and fresh water flowing right-to-left.

### Step 10 — Section label
1. Add text: `HOW COUNTERFLOW RINSING WORKS`
2. Font: Barlow Condensed ExtraBold, Size: `30`, Color: `#F0EDE8`, Alignment: Center
3. Position: Centered horizontally. Y: **3.1"**. Width: `23.0"`.

### Step 11 — Build the three rinse tanks

Three tanks evenly spaced across the safe zone:
- Tank 1 (Dirtiest): X: **0.5"** to **7.0"** (6.5" wide)
- Tank 2 (Middle): X: **8.5"** to **15.0"** (6.5" wide)
- Tank 3 (Cleanest): X: **16.5"** to **23.0"** (6.5" wide)

**Each tank consists of:**

**11a — Tank body (outer):**
- Rectangle. Width: `6.5"`. Height: `5.5"`. Fill: none (transparent). Border: 3 pt, `#3A4055` (Mid Slate).
- Y: **5.0"** to **10.5"**.

**11b — Water fill (inside tank):**
- Rectangle positioned inside the tank body, flush with inner edges.
- Width: `6.2"`. Height: `4.0"`. Y: **6.3"** to **10.3"**.
- Fill varies by tank:
  - Tank 1 (Dirtiest): `#2EC4B6` at **60%** opacity (dark teal, murky)
  - Tank 2 (Middle): `#5ED4C8` at **50%** opacity (medium teal)
  - Tank 3 (Cleanest): `#A0E8E0` at **40%** opacity (light teal, clear)

**11c — Parts in tank:**
- 2-3 small rounded rectangles per tank (W: `0.5"`, H: `0.8"`).
- Fill: `#C8D0D8` (Bright Silver). Position: Submerged in the water fill area, lower third of each tank.

**11d — Tank label (below tank):**
- Font: Barlow SemiBold, `20` pt. Position: Centered below each tank. Y: **11.0"**.
- Colors:
  - Tank 1: `#E05C5C` (Coral) — text: `RINSE 1 — Dirtiest`
  - Tank 2: `#E8A020` (Amber) — text: `RINSE 2 — Middle`
  - Tank 3: `#27AE60` (Emerald) — text: `RINSE 3 — Cleanest`

**11e — Number badge (inside tank, upper-left):**
- Circle. Diameter: `0.5"`. Fill: `#3A4055`. Position: 0.3" from tank left edge, 0.3" from tank top edge.
- Text inside: `1`, `2`, `3` — Barlow Condensed ExtraBold, `20` pt, `#F0EDE8`.

### Step 12 — Part movement arrows (left-to-right across top)

- Y: **4.5"** (above tanks). Three arrow segments spanning the 1.5" gaps between tanks.
- Stroke: `2.5` pt, `#C8D0D8` (Bright Silver). Arrowheads pointing right.
- Label above the arrow line:
  - Text: `PARTS MOVE →  (dirtiest to cleanest)`
  - Font: Barlow SemiBold, `18` pt, `#C8D0D8`. Position: Centered above arrows. Y: **3.9"**.

### Step 13 — Water flow arrows (right-to-left across bottom)

- Y: **12.0"** (below tank labels). Three arrow segments — arrowheads point LEFT.
- Stroke: `2.5` pt, `#2EC4B6` (Teal).
- Label below the arrow line:
  - Text: `← FRESH WATER FLOWS  (cleanest to dirtiest)`
  - Font: Barlow SemiBold, `18` pt, `#2EC4B6`. Position: Centered below arrows. Y: **12.6"**.

### Step 14 — Fresh water inlet indicator (at Tank 3)

- Short line with arrowhead entering Tank 3 from the right.
- Position: X: **23.5"** to **23.0"**, Y: **8.0"**. Stroke: 2 pt, `#27AE60` (Emerald).
- Label: `Fresh DI water in` — JetBrains Mono Regular, `12` pt, `#27AE60`.

### Step 15 — Drain/overflow indicator (at Tank 1)

- Short line with arrowhead exiting Tank 1 from the left.
- Position: X: **0.5"** to **0.0"**, Y: **8.0"**. Stroke: 2 pt, `#E05C5C` (Coral).
- Label: `To waste treatment` — JetBrains Mono Regular, `12` pt, `#E05C5C`.

### Step 16 — Drain time callout

- Text: `15–20 second drain time between stations — tilt parts to minimize drag-out`
- Font: Inter Medium, `16` pt, `#E8A020` (Amber). Position: Centered horizontally. Y: **13.2"**.

### Step 17 — Drag-out recovery tank (DRT)

A small DRT tank to the LEFT of Tank 1.

**17a — DRT tank body:**
- Rectangle. Width: `1.4"`. Height: `2.0"`. Fill: none. Border: 2 pt dashed, `#E8A020`.
- Position: X: approximately **-0.6"** to **0.4"**, Y: **6.5"** to **8.5"**.

**17b — DRT water fill:**
- Rectangle. W: `1.3"`, H: `1.4"`. Fill: `#E8A020` at 25% opacity.

**17c — DRT label:**
- `DRT` — Barlow SemiBold, `14` pt, `#E8A020`. Centered below tank.

**17d — DRT caption:**
- `Drag-out recovery → returns to process tank` — Inter Regular, `11` pt, `#E8A020`. Position: above the part-movement arrow line. Width: 4.5".

### Step 18 — Group all of Zone 2
Select all tank elements, arrows, labels, DRT elements. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Water Savings + Equation

This zone occupies Y: 14.5" to 21.5" (~7.0" tall).

### Step 19 — Section label
1. Add text: `THE MATH BEHIND THE SAVINGS`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `#F0EDE8`, Alignment: Center
3. Position: Centered horizontally. Y: **14.7"**.

### Step 20 — Water savings comparison (left half, X: 0.5" to 11.5")

**Bar 1 — Single Rinse:**
- Rectangle. Position: X: **2.0"**, Y: **15.8"**. Width: `2.5"`. Height: `3.0"` (full height = 100%).
- Fill: `#E05C5C` (Coral) at 80% opacity.
- Label above: `Single Rinse` — Barlow SemiBold, `18` pt, `#E05C5C`. Y: **15.4"**.
- Label inside (centered): `100%` — Barlow Condensed ExtraBold, `36` pt, `#F0EDE8`.
- Sub-label below: `Rinse ratio 100:1` — JetBrains Mono Regular, `14` pt, `#F0EDE8` at 60%.

**Bar 2 — 2-Stage Counterflow:**
- Rectangle. Position: X: **6.0"**, Y: **18.5"**. Width: `2.5"`. Height: `0.3"` (10% of Bar 1).
- Fill: `#27AE60` (Emerald).
- Label above: `2-Stage Counterflow` — Barlow SemiBold, `18` pt, `#27AE60`.
- Label beside (bar is very short): `10%` — Barlow Condensed ExtraBold, `28` pt, `#27AE60`.
- Sub-label below: `Same rinse ratio` — JetBrains Mono Regular, `14` pt, `#F0EDE8` at 60%.

**Savings callout between bars:**
- Text: `90% LESS WATER`
- Font: Barlow Condensed ExtraBold, `48` pt, `#27AE60`. Position: Centered between bars. Y: **17.0"**.

### Step 21 — Counterflow rinse equation (right half, X: 12.0" to 23.5")

**21a — Equation display box:**
- Rounded rectangle. Position: X: **12.0"**, Y: **15.4"**. Width: `11.5"`. Height: `5.4"`.
- Fill: `#1E2435`. Corner radius: `8`.

**21b — Left-border accent:**
- Rectangle. X: **12.0"**, Y: **15.4"**. Width: `0.06"`. Height: `5.4"`. Fill: `#2EC4B6`.

**21c — Equation title:**
- Text: `COUNTERFLOW RINSE EQUATION`
- Font: Barlow SemiBold, `20` pt, `#2EC4B6`. Position: X: **12.4"**, Y: **15.7"**.

**21d — Equation (large display):**
- Text: `FR = DI x (CT / CR)^(1/N)`
- Font: JetBrains Mono Regular, `28` pt, `#F0EDE8`, Alignment: Center.
- Position: X: **12.4"**, Y: **16.5"**. Width: `10.8"`.

**21e — Variable definitions:**
- Font: Inter Regular, `16` pt, `#F0EDE8`, Line height: 160%.
- Position: X: **12.4"**, Y: **17.6"**. Width: `10.8"`.
- Text:
  ```
  FR = Flow rate of fresh water (gal/hr)
  DI = Drag-in volume per rack (gal/rack)
  CT = Concentration in process tank
  CR = Maximum allowable rinse concentration
  N = Number of counterflow rinse stages

  CT/CR = Rinse ratio (typically 1,000:1 to 10,000:1)
  ```

**21f — Key insight:**
- Text: `Adding one rinse stage takes the Nth root of the rinse ratio — this is why 2 stages beats 1 by a factor of 10-100x in water savings.`
- Font: Inter Medium, `15` pt, `#E8A020`. Position: X: **12.4"**, Y: **20.0"**. Width: `10.8"`.

### Step 22 — Group all of Zone 3
Select all comparison and equation elements. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Drag-Out Factors + Best Practices

This zone occupies Y: 21.5" to 28.5" (~7.0" tall). Two side-by-side callouts.

### Step 23 — Section label
1. Add text: `CONTROLLING DRAG-OUT`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `#F0EDE8`, Alignment: Center
3. Position: Centered horizontally. Y: **21.7"**.

### Step 24 — Drag-Out Factors callout (left column)

**24a — Container:**
- Rounded rectangle. Position: X: **0.5"**, Y: **22.4"**. Width: `11.2"`. Height: `5.5"`.
- Fill: `#1E2435`. Corner radius: `6`.

**24b — Left accent:**
- Rectangle. X: **0.5"**, Y: **22.4"**. Width: `0.06"`. Height: `5.5"`. Fill: `#E8A020`.

**24c — Title:**
- Text: `WHAT INCREASES DRAG-OUT`
- Font: Barlow SemiBold, `22` pt, `#E8A020`. Position: X: **0.8"**, Y: **22.6"**.

**24d — Bullet list:**
- Font: Inter Regular, `18` pt, `#F0EDE8`, Line height: 150%.
- Position: X: **0.8"**, Y: **23.2"**. Width: `10.6"`.
- Text:
  ```
  - Higher solution viscosity (hot alkaline cleaners, thick acids)
  - Complex part geometry (cups, recesses, blind holes)
  - Rough or porous surfaces (cast parts, etched surfaces)
  - Fast withdrawal speed (less time for solution to sheet off)
  - High surface tension (no wetting agents in the bath)
  - Large surface-to-volume ratio (flat parts carry more film)
  ```

**24e — Key number:**
- Text: `Typical drag-out: 2–6 mL/ft² of part surface area`
- Font: JetBrains Mono Regular, `14` pt, `#E8A020`. Position: X: **0.8"**, Y: **26.8"**.

### Step 25 — Best Practices callout (right column)

**25a — Container:**
- Rounded rectangle. Position: X: **12.0"**, Y: **22.4"**. Width: `11.5"`. Height: `5.5"`.
- Fill: `#1E2435`. Corner radius: `6`.

**25b — Left accent:**
- Rectangle. X: **12.0"**, Y: **22.4"**. Width: `0.06"`. Height: `5.5"`. Fill: `#27AE60`.

**25c — Title:**
- Text: `DRAG-OUT REDUCTION BEST PRACTICES`
- Font: Barlow SemiBold, `22` pt, `#27AE60`. Position: X: **12.3"**, Y: **22.6"**.

**25d — Bullet list:**
- Font: Inter Regular, `18` pt, `#F0EDE8`, Line height: 150%.
- Position: X: **12.3"**, Y: **23.2"**. Width: `10.9"`.
- Text:
  ```
  - Drain 15–20 seconds over the process tank before moving
  - Tilt parts and racks to break surface tension
  - Use air knives or blow-offs for high-value baths
  - Install drip trays sloped BACK toward the process tank (never toward the rinse)
  - Add wetting agents to reduce solution surface tension
  - Use a drag-out recovery tank ahead of the first rinse to capture drag-out for return to the process tank
  - Orient parts to minimize cupping and pooling
  ```

**25e — Key number:**
- Text: `Target rinse ratio: 1,000:1 minimum for decorative work; 10,000:1+ for electronics and aerospace`
- Font: JetBrains Mono Regular, `14` pt, `#27AE60`. Position: X: **12.3"**, Y: **26.8"**.

### Step 26 — Group all of Zone 4
Select both callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Conductivity Monitoring Callout

This zone occupies Y: 28.5" to 32.5" (~4.0" tall). Full-width callout.

### Step 27 — Conductivity callout

**27a — Container:**
- Rounded rectangle. Position: X: **0.5"**, Y: **28.7"**. Width: `23.0"`. Height: `3.5"`.
- Fill: `#1E2435`. Corner radius: `8`.

**27b — Left accent:**
- Rectangle. X: **0.5"**, Y: **28.7"**. Width: `0.06"`. Height: `3.5"`. Fill: `#2EC4B6`.

**27c — Title:**
- Text: `MONITORING RINSE QUALITY — CONDUCTIVITY`
- Font: Barlow SemiBold, `22` pt, `#2EC4B6`. Position: X: **0.8"**, Y: **28.9"**.

**27d — Body text (left half):**
- Font: Inter Regular, `16` pt, `#F0EDE8`, Line height: 150%.
- Position: X: **0.8"**, Y: **29.5"**. Width: `10.5"`.
- Text: `Conductivity measurement is the simplest way to verify rinse water quality. As drag-out contaminates the rinse, dissolved salts raise the conductivity. A rising reading means the rinse is becoming less effective.`

**27e — Body text (right half):**
- Font: Inter Regular, `16` pt, `#F0EDE8`, Line height: 150%.
- Position: X: **12.5"**, Y: **29.5"**. Width: `10.5"`.
- Text: `Inductive (toroidal) conductivity sensors are preferred over electrode-type sensors in plating environments — they resist fouling from dissolved metals and organics that coat electrode surfaces and cause drift.`

**27f — Key data callout (bottom of box):**
- Text: `DI water baseline: < 5 µS/cm  |  Typical rinse alarm setpoint: 50–200 µS/cm — always set process-by-process against your spec, not by rule of thumb`
- Font: JetBrains Mono Regular, `14` pt, `#E8A020`, Alignment: Center.
- Position: Centered horizontally. Y: **31.4"**.

### Step 28 — Group all of Zone 5
Select all conductivity callout elements. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

### Step 29 — Footer band background
- Rectangle. Width: `24.0"`. Height: `3.5"`. Fill: `#0D1020`.
- Position: X: **0"**, Y: **32.5"**.

### Step 30 — Disclaimer
- Text: `This poster is an educational reference tool. Rinse system design depends on specific process chemistry, water quality, local discharge limits, and equipment configuration. Consult your process supplier and environmental engineer for application-specific guidance.`
- Font: Inter Regular, Size: `11`, Color: `#F0EDE8`, Transparency: **50%**, Alignment: Center.
- Position: X: **0.5"**, Y: **32.8"**. Width: `23.0"`.

### Step 31 — Poster title
- Text: `Rinsing Efficiency — The Hidden Cost of Poor Rinsing`
- Font: Barlow SemiBold, Size: `16`, Color: `#F0EDE8`.
- Position: X: **0.5"**, Y: **33.5"**.

### Step 32 — Series name
- Text: `Plating Posters Inc — Metal Finishing Reference Series`
- Font: Inter Regular, Size: `14`, Color: `#F0EDE8`, Transparency: **70%**, Alignment: Center.
- Position: Centered horizontally, Y: **34.2"**.

### Step 33 — Logo placeholder
- Rounded rectangle. Width: `0.8"`. Height: `0.4"`. Fill: `#3A4055`.
- Position: X: **22.5"**, Y: **33.3"**.
- Text: `[LOGO]` — JetBrains Mono Regular, `12` pt, `#F0EDE8`, Transparency: **50%**.

### Step 34 — Version
- Text: `v1.0 — 2026`
- Font: JetBrains Mono Regular, Size: `11`, Color: `#F0EDE8`, Transparency: **50%**.
- Position: X: **0.5"**, Y: **35.0"**.

### Step 35 — Group all of Zone 6
Select footer rectangle, disclaimer, poster title, series name, logo, version. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline: `RINSING EFFICIENCY` at 96 pt
- [ ] Subheading: `The Hidden Cost of Poor Rinsing` in Teal
- [ ] Section label: `HOW COUNTERFLOW RINSING WORKS`
- [ ] Three tanks present with labels: Dirtiest (Coral), Middle (Amber), Cleanest (Emerald)
- [ ] Part movement arrows point RIGHT; water flow arrows point LEFT
- [ ] Fresh DI water inlet at Tank 3; waste treatment outlet at Tank 1
- [ ] DRT tank present to left of Tank 1 with dashed Amber border
- [ ] Drain time callout: 15–20 second drain time
- [ ] Water savings comparison: 100% bar (Coral) vs. 10% bar (Emerald) with `90% LESS WATER` callout
- [ ] Equation: `FR = DI x (CT / CR)^(1/N)` with all 5 variable definitions
- [ ] Drag-out factors: 6 bullets + key number (2–6 mL/ft²)
- [ ] Best practices: 7 bullets + key number (rinse ratio targets)
- [ ] Conductivity callout: both body paragraphs + key data (µS/cm values)
- [ ] Disclaimer, footer title, series name, LOGO, version present

### Color verification
- [ ] Tank 1 water: Teal at 60% (dark/murky)
- [ ] Tank 2 water: Teal Light at 50%
- [ ] Tank 3 water: Teal Lightest at 40% (clear)
- [ ] Part arrows: Bright Silver
- [ ] Water arrows: Teal
- [ ] DRT: dashed Amber
- [ ] Equation box accent: Teal
- [ ] Drag-out callout accent: Amber
- [ ] Best practices accent: Emerald
- [ ] Conductivity callout accent: Teal
- [ ] Footer band: Deep Navy `#0D1020`

### Layout verification
- [ ] Three tanks evenly spaced with 1.5" gaps
- [ ] Parts submerged in lower third of each tank
- [ ] Water savings bars proportional (100% height vs. 10% height)
- [ ] Equation box and comparison side by side in Zone 3
- [ ] All text within 0.5-inch safe zone

### Readability check
- [ ] Zoom to 25% — tank diagram and `90% LESS WATER` readable
- [ ] Zoom to 50% — tank labels and equation visible
- [ ] Zoom to 75% — bullet lists and variable definitions readable
- [ ] Zoom to 100% — all body text, key data, and footnotes readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 36 — Duplicate the page
Duplicate the Dark edition design. Switch to the copy.

### Step 37 — Change the background
Change from `#1A1F2E` to `#F5F4F0` (Off-White).

### Step 38 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Card/callout fills** | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | `#252B3D` | `#E8E8F0` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |
| **Bright Silver** | `#C8D0D8` | `#C8D0D8` **(unchanged)** |
| **Teal Light** | `#5ED4C8` | `#3AAFA3` |
| **Teal Lightest** | `#A0E8E0` | `#6DC8BE` |

Water fill opacities may need adjustment in the Light edition to maintain visual distinction against the light background. Test at 50-70% opacity.

### Step 39 — Post-remap adjustments
1. **Tagline at 65%**: If too faint on light background, increase to **75-80%**.
2. **Key data at 60-70%**: If too faint, increase to **75-80%**.
3. **Disclaimer at 50%**: If too faint, increase to **65%**.

---

## Phase 10 — Export Instructions

### Step 40 — Export Dark edition

**40a — Print PDF, 24x36":**
- PDF Print. Check crop marks and bleed. Page 1.
- Rename: `Rinsing Efficiency — Dark — 24x36 — Print.pdf`

**40b — Digital PDF:**
- PDF Standard. Uncheck crop marks. Page 1.
- Rename: `Rinsing Efficiency — Dark — Digital.pdf`

**40c — Print PDF, 18x24":**
- Resize to 18 x 24 inches. Verify 14 pt body text minimum.
- Rename: `Rinsing Efficiency — Dark — 18x24 — Print.pdf`

### Step 41 — Export Light edition

Repeat with filenames:
- `Rinsing Efficiency — Light — 24x36 — Print.pdf`
- `Rinsing Efficiency — Light — Digital.pdf`
- `Rinsing Efficiency — Light — 18x24 — Print.pdf`

### Export file checklist
- [ ] `Rinsing Efficiency — Dark — 24x36 — Print.pdf`
- [ ] `Rinsing Efficiency — Dark — 18x24 — Print.pdf`
- [ ] `Rinsing Efficiency — Dark — Digital.pdf`
- [ ] `Rinsing Efficiency — Light — 24x36 — Print.pdf`
- [ ] `Rinsing Efficiency — Light — 18x24 — Print.pdf`
- [ ] `Rinsing Efficiency — Light — Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | Single-rinse bar, drag-out callout, DRT, key insights |
| `#2EC4B6` | Teal | Counterflow accent, Tank 1 water, equation, conductivity |
| `#27AE60` | Emerald | Water savings, best practices, Tank 3 label, fresh water inlet |
| `#E05C5C` | Coral | Single-rinse bar, Tank 1 label, waste treatment outlet |
| `#3A4055` | Mid Slate | Tank outlines, number badges |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout fills, equation box |
| `#252B3D` | Alt Row | Reserve |
| `#C8D0D8` | Bright Silver | Parts, part movement arrows |
| `#5ED4C8` | Teal Light | Tank 2 water fill |
| `#A0E8E0` | Teal Lightest | Tank 3 water fill |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Callout fills (Light edition) |
| `#E8E8F0` | Alt Row Light | Alt rows (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#1E7A47` | Forest Green | Emerald elements (Light edition) |
| `#B83E3E` | Deep Coral | Coral elements (Light edition) |
| `#D0D4DE` | Light Slate | Tank outlines/dividers (Light edition) |
| `#3AAFA3` | Teal Light Dark | Tank 2 water (Light edition) |
| `#6DC8BE` | Teal Lightest Dark | Tank 3 water (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-20 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v2.0. |
