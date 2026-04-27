---
Project: Plating Posters Inc
Poster Number: 15
Title: "The Plating Shop Quality Loop: From Incoming Part to Final Inspection"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 15 — The Plating Shop Quality Loop — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - QualityControl
  - v1
---

# Claude Chat Generation Prompt — Poster #15
## The Plating Shop Quality Loop
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup. Adapted for Claude chat visual generation (2026-04-14). All technical content production-ready.*

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
| Amber | `#E8A020` | Accent, subheadings |
| Teal | `#2EC4B6` | Callout borders, secondary accent |
| Emerald | `#27AE60` | Positive/success accent |
| Coral | `#E05C5C` | Warning/alert accent |
| Mid Slate | `#3A4055` | Dividers, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card/callout box fills |
| Alt Row | `#252B3D` | Alternating row backgrounds |

### Layout Safe Zones
- **0.5" margin** on all sides (safe zone for print trimming)
- All content must stay within the 23" x 35" live area

---

## Phase 2 — Zone 1: Header Band

This zone occupies the top 2.9 inches. Headline + subheading + tagline on the left (~55%), "Special Process" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element: Type: `THE QUALITY LOOP`
2. Font: Barlow Condensed ExtraBold, Size: `88`, Color: `F0EDE8`, Letter spacing: `-4`, Alignment: Left
3. Position: X: **0.5"**, Y: **0.5"**. Width: `12.5"`.

### Step 7 — Place the subheading
1. Add text: `From Incoming Part to Final Inspection`
2. Font: Barlow SemiBold, Size: `36`, Color: `E8A020` (Amber), Alignment: Left
3. Position: X: **0.5"**, Y: approximately **1.5"**.

### Step 8 — Place the tagline
1. Add text: `Quality isn't the final step. It's every step.`
2. Font: Barlow SemiBold, Size: `22`, Color: `F0EDE8`, Transparency: **65%**
3. Position: X: **0.5"**, Y: approximately **2.2"**.

### Step 9 — Build "Special Process" callout

**9a — Container:**
1. Add rounded rectangle. Width: `9.5"`. Height: `2.2"`. Fill: `1E2435`. Border: 2 pt, `E05C5C` (Coral). Corner radius: `8`.
2. Position: X: **13.5"**, Y: **0.5"**.

**9b — Title:**
1. Add text: `PLATING IS A SPECIAL PROCESS`
2. Font: Barlow SemiBold, Size: `18`, Color: `E05C5C`
3. Position: inside container, top-left with 0.15" padding.

**9c — Body:**
1. Add text. Copy-paste:
   `You cannot look at a plated part and know if it will pass salt spray. You cannot see hydrogen trapped in steel. Quality must be built in during the process — it cannot be inspected in afterward.`
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`, Line height: `1.4`
3. Position: below title. Width: approximately `9.0"`.

**9d — Standard reference:**
1. Add text: `ISO 9001:2015 Section 8.5.1`
2. Font: JetBrains Mono Regular, Size: `12`, Color: `F0EDE8`, Transparency: **70%**
3. Position: near bottom of container.

**9e — Group the callout.**

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Quality Wheel (Hero Visual)

This zone occupies Y: 2.9" to 18.7" (15.8 inches tall). A circular quality wheel with 7 stations, directional arrows, a feedback loop, PDCA labels, and center text.

**Build strategy:** Build the wheel structure first (circles), then build one station group, duplicate 6 times, then add arrows and labels.

### Step 11 — Section label
1. Add text: `THE SEVEN STATIONS OF PLATING QUALITY`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: X: **0.5"**, Y: **3.0"**. Width: `23.0"`.

### Step 12 — Draw the outer wheel ring
1. Add a **circle** shape.
2. Width: `14.0"`. Height: `14.0"` (hold Shift while resizing to keep it circular).
3. Fill: none (transparent). Border: 2 pt, `3A4055` (Mid Slate).
4. Position: centered at X: **12.0"** (center of page), Y: **11.5"** (center of zone). This means the circle's left edge is at X: **5.0"**, top edge at Y: **4.5"**.

### Step 13 — Draw the inner circle
1. Add another circle. Width: `5.0"`. Height: `5.0"`.
2. Fill: `1A1F2E` (matches background). Border: 3 pt, `3A4055`.
3. Position: centered same as outer circle (left edge X: **9.5"**, top edge Y: **9.0"**).

### Step 14 — Center text
Add three text elements inside the inner circle, stacked vertically and centered:

**14a — Line 1:**
1. Add text: `CERTIFIED.`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered in the inner circle, approximately Y: **10.5"**.

**14b — Line 2:**
1. Add text: `EVERY TIME.`
2. Same font/size/color. Position: below Line 1, Y: approximately **11.1"**.

**14c — Line 3:**
1. Add text: `Plan - Do - Check - Act`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **60%**, Alignment: Center
3. Position: below Line 2, Y: approximately **11.8"**.

### Step 15 — Build Station 1 (Template): INCOMING INSPECTION

Each station consists of: accent circle + icon + station label + sub-label + consequence tag.

**15a — Station accent circle:**
1. Add a circle. Width: `1.3"`. Height: `1.3"`.
2. Fill: `2EC4B6` (Teal).
3. Position: X: **12.0"** (centered), Y: **5.3"** (12 o'clock position on the wheel).
   (The circle's center should sit on or near the outer wheel ring.)

**15b — Station icon:**
1. Click **Elements** > search `magnifying glass` (or "inspect"). Place the icon inside the accent circle.
2. Icon size: `0.7"` x `0.7"`. Color: `1A1F2E` (Gunmetal Dark).
3. Center the icon within the accent circle using alignment tools.

**15c — Station label:**
1. Add text: `1. INCOMING`
2. Font: Barlow SemiBold, Size: `14`, Color: `2EC4B6` (Teal)
3. Position: just outside the accent circle, radiating outward from the wheel center. For Station 1 (12 o'clock), place it directly above the circle.

**15d — Sub-label:**
1. Add text: `Part inspection`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **80%**
3. Position: below the station label.

**15e — Consequence tag:**
1. Add text: `Skip → wrong alloy contaminates bath`
2. Font: Inter Medium, Size: `11`, Color: `E05C5C` (Coral)
3. Position: below the sub-label, further outside the wheel.

**15f — Group Station 1:**
Select accent circle, icon, label, sub-label, consequence tag. Press **Ctrl+G**.

### Step 16 — Duplicate and modify for Stations 2-7

Duplicate the Station 1 group 6 times. Reposition each to its clock position around the wheel. Ungroup each temporarily, change the accent circle color, icon, labels, and consequence text per the table below. Re-group each when done.

| Station | Clock Pos | Circle X | Circle Y | Fill | Icon Search | Label | Sub-label | Consequence |
|---------|-----------|----------|----------|------|-------------|-------|-----------|-------------|
| 1 | 12:00 | 12.0" | 5.3" | `#2EC4B6` Teal | magnifying glass | `1. INCOMING` | `Part inspection` | `Skip → wrong alloy contaminates bath` |
| 2 | ~2:00 | 15.8" | 7.0" | `#2EC4B6` Teal | water drop | `2. PRE-TREAT` | `Surface verification` | `Skip → adhesion failure` |
| 3 | ~4:00 | 16.8" | 11.0" | `#E8A020` Amber | flask / chemistry | `3. BATH CONTROL` | `Chemistry analysis` | `Drift → invisible degradation` |
| 4 | ~5:30 | 15.2" | 14.8" | `#E8A020` Amber | gauge / meter | `4. IN-PROCESS` | `Parameter monitoring` | `Bad contacts → non-uniform deposit` |
| 5 | ~7:00 | 11.5" | 16.5" | `#E8A020` Amber | thermometer | `5. POST-TREAT` | `Passivation + bake` | Copy-paste: `Missed bake → catastrophic H₂ failure` |
| 6 | ~9:00 | 7.5" | 14.0" | `#27AE60` Emerald | ruler / measure | `6. MEASUREMENT` | `Thickness + properties` | `Under-thickness → field failure` |
| 7 | ~11:00 | 7.8" | 7.5" | `#27AE60` Emerald | clipboard / checklist | `7. FINAL` | `Inspection + CoC` | `No traceability → audit failure` |

**Label positioning:** For stations on the right side of the wheel (2, 3, 4), place labels to the right of the circle. For stations on the bottom-left (5, 6), place labels below or to the left. For station 7 (top-left), place labels to the left.

### Step 17 — Directional flow arrows (clockwise)

Add 6 arrow lines connecting consecutive stations around the wheel perimeter:
- Station 1 → 2, 2 → 3, 3 → 4, 4 → 5, 5 → 6, 6 → 7
- Each arrow: line with arrowhead. Stroke: 2 pt, `3A4055` (Mid Slate). Arrowhead at the destination end.
- Route each arrow along the wheel perimeter between the station circles. Use straight lines angled to approximate the curve. Use curved/arced lines or arrows to connect stations along the wheel perimeter.

### Step 18 — Feedback arrow (Coral)

This is the bold return arrow from Station 7 back to Station 1, arcing through or near the center.

1. Draw a curved line (or 2-3 connected straight segments) from the Station 7 circle position to the Station 1 circle position, sweeping through or near the inner circle.
2. Stroke: 3 pt, `E05C5C` (Coral). Arrowhead at the Station 1 end.
3. Add label along the arrow path:
   - Text: `CORRECTIVE ACTION`
   - Font: Barlow SemiBold, Size: `14`, Color: `E05C5C`

### Step 19 — PDCA quadrant labels

Four text labels positioned outside the wheel ring at the quadrant midpoints:

1. **Top-right** (between Stations 1-2): `PLAN`
   - Font: Barlow SemiBold, Size: `16`, Color: `2EC4B6`, Transparency: **40%**

2. **Right-bottom** (between Stations 3-5): `DO`
   - Font: Barlow SemiBold, Size: `16`, Color: `E8A020`, Transparency: **40%**

3. **Bottom-left** (between Stations 6-7): `CHECK`
   - Font: Barlow SemiBold, Size: `16`, Color: `27AE60`, Transparency: **40%**

4. **Top-left** (Feedback zone): `ACT`
   - Font: Barlow SemiBold, Size: `16`, Color: `E05C5C`, Transparency: **40%**

**Optional PDCA shading:** Add 4 very subtle rectangles behind each quadrant (5-8% opacity of the accent color). If too difficult or the effect is invisible, skip — the text labels alone carry the concept.

### Step 20 — Group all of Zone 2
Select outer circle, inner circle, center text, all 7 station groups, all 6 flow arrows, feedback arrow + label, and PDCA labels. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Station Detail Cards

This zone occupies Y: 18.7" to 25.9" (7.2 inches tall). Two rows of 4 cards = 8 cards total (7 stations + 1 feedback loop).

**Card dimensions:** Width: `5.5"`. Height: `3.3"`. Fill: `1E2435`. Corner radius: `6`. Left-border accent: 4 pt (0.06" wide).

**Card positions:**
- Row 1 (Y: **18.8"**): X: **0.5"**, **6.33"**, **12.17"**, **18.0"**
- Row 2 (Y: **22.4"**): X: **0.5"**, **6.33"**, **12.17"**, **18.0"**

### Step 21 — Build Card 1 (Template): INCOMING INSPECTION

**21a — Card container:**
1. Add rounded rectangle. Width: `5.5"`. Height: `3.3"`. Fill: `1E2435`. Corner radius: `6`.
2. Position: X: **0.5"**, Y: **18.8"**.

**21b — Left accent bar:**
1. Add rectangle. Width: `0.06"`. Height: `3.3"`. Fill: `2EC4B6` (Teal).
2. Position: X: **0.5"**, Y: **18.8"** (flush left).

**21c — Title:**
1. Add text: `STATION 1: INCOMING`
2. Font: Barlow SemiBold, Size: `14`, Color: `2EC4B6` (Teal)
3. Position: inside card, top-left with 12 pt padding from edges.

**21d — Checklist:**
1. Add text. Copy-paste:
   ```
   - Surface condition (rust, scale, oil)
   - Material identification (alloy, heat treat)
   - Dimensional / drawing review
   - Quantity + PO documentation
   ```
2. Font: Inter Regular, Size: `12`, Color: `F0EDE8`, Line height: `1.4`
3. Position: below title with 0.1" gap. Width: approximately `5.0"`.

**21e — Gate label:**
1. Add text: `GATE: Quarantine or return — no entry to plating line.`
2. Font: Inter Medium, Size: `11`, Color: `27AE60` (Emerald)
3. Position: near bottom of card, with 8 pt padding from bottom edge.

**21f — Group the card.**

### Step 22 — Duplicate and modify for Cards 2-8

Duplicate Card 1 seven times. Reposition per the grid positions above. For each, ungroup, change accent bar color, title, checklist, and gate text.

---

**Card 2 — PRE-TREATMENT** (Row 1, position 2: X: **6.33"**, Y: **18.8"**)
- Accent: `#2EC4B6` (Teal)
- Title: `STATION 2: PRE-TREATMENT`
- Checks:
  ```
  - Cleaner concentration (titration)
  - Electrocleaner V/A and polarity
  - Acid activation strength
  - Rinse conductivity + flow rate
  ```
- Gate: `GATE: Water break test — continuous film, no beading.`

**Card 3 — BATH CHEMISTRY** (Row 1, position 3: X: **12.17"**, Y: **18.8"**)
- Accent: `#E8A020` (Amber)
- Title: `STATION 3: BATH CONTROL`
- Checks:
  ```
  - pH (2-point calibrated meter)
  - Metal concentration (EDTA titration)
  - Salt/buffer levels (titration)
  - Hull cell + temperature
  ```
- Gate: `GATE: Out-of-spec = correct before production.`

**Card 4 — IN-PROCESS** (Row 1, position 4: X: **18.0"**, Y: **18.8"**)
- Accent: `#E8A020` (Amber)
- Title: `STATION 4: IN-PROCESS`
- Checks:
  ```
  - Rectifier V/A correct for load
  - Current density within range
  - Temperature continuous monitoring
  - Agitation + rack/barrel condition
  ```
- Gate: `GATE: Any deviation = operator intervention or hold.`

**Card 5 — POST-TREATMENT** (Row 2, position 1: X: **0.5"**, Y: **22.4"**)
- Accent: `#E8A020` (Amber)
- Title: `STATION 5: POST-TREATMENT`
- Checks: Copy-paste (contains Unicode):
  ```
  - Passivation pH / temp / time
  - Sealer concentration + dip time
  - H₂ bake within 4 hrs (>40 HRC)
  - Drying (prevent white rust)
  ```
- Gate: `GATE: Bake oven calibrated with recording chart.`

**Card 6 — MEASUREMENT** (Row 2, position 2: X: **6.33"**, Y: **22.4"**)
- Accent: `#27AE60` (Emerald)
- Title: `STATION 6: MEASUREMENT`
- Checks:
  ```
  - XRF thickness (ASTM B568)
  - Magnetic induction (B499)
  - Salt spray per spec (B117)
  - Adhesion testing (B571)
  ```
- Gate: `GATE: Fail = quarantine and disposition.`

**Card 7 — FINAL INSPECTION** (Row 2, position 3: X: **12.17"**, Y: **22.4"**)
- Accent: `#27AE60` (Emerald)
- Title: `STATION 7: FINAL + DOCUMENTATION`
- Checks:
  ```
  - Visual inspection (100% or sampling)
  - All test results documented
  - Certificate of Conformance (CoC)
  - Full lot traceability
  ```
- Gate: `GATE: Release authority sign-off. No ship without CoC.`

**Card 8 — FEEDBACK LOOP** (Row 2, position 4: X: **18.0"**, Y: **22.4"**)
- Accent: `#E05C5C` (Coral)
- Title: `FEEDBACK: CORRECTIVE ACTION` (Color: `E05C5C`)
- Content (instead of standard checklist):
  ```
  - Salt spray failures → trace to Stations 3 + 5
  - Adhesion failures → trace to Stations 1 + 2
  - Customer complaints → 8D / CAPA process
  - Internal audits → verify all stations
  ```
- Gate: `GATE: Management review per ISO 9001 Sec. 9.3.`

### Step 23 — Group all of Zone 3
Select all 8 card groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: H₂ Embrittlement + Calibration

This zone occupies Y: 25.9" to 30.6" (4.7 inches tall). Two side-by-side callout boxes.

### Step 24 — Block E: Hydrogen Embrittlement Warning (left 55%)

**24a — Container:**
1. Add rounded rectangle. Width: `12.5"`. Height: `4.3"`. Fill: `1E2435`. Border: 2 pt, `E05C5C` (Coral). Corner radius: `8`.
2. Position: X: **0.5"**, Y: **26.0"**.

**24b — Warning icon:**
1. Click **Elements** > search `alert triangle` or `warning`. Place icon inside box, top-left.
2. Icon size: `1.0"` x `1.0"`. Color: `E05C5C`.

**24c — Title (positioned right of icon):**
1. Add text: Copy-paste: `HYDROGEN EMBRITTLEMENT — THE CRITICAL WINDOW`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E05C5C`
3. Position: right of the warning icon, Y: approximately **26.3"**.

**24d — Body:**
1. Add text. Copy-paste:
   `High-strength steel parts (>40 HRC / >1000 MPa) must be baked within 4 hours of plating completion. Some specs require 1 hour. Delayed or omitted baking risks catastrophic brittle fracture.`
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`
3. Position: below title. Width: approximately `12.0"`.

**24e — Key data (tabular):**
1. Add text. Copy-paste:
   ```
   Bake temp:  190 C (375 F)
   Duration:   4-24 hours (per spec)
   Deadline:   Within 4 hrs of plating
   Threshold:  >40 HRC or >1000 MPa
   ```
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`
3. Position: below body text.

**24f — Standards:**
1. Add text: `ASTM B850 | AMS 2759/9 | ASTM B633`
2. Font: JetBrains Mono Regular, Size: `12`, Color: `F0EDE8`, Transparency: **60%**
3. Position: near bottom of container.

### Step 25 — Block F: Calibration Checklist (right 45%)

**25a — Container:**
1. Rounded rectangle. Width: `10.25"`. Height: `4.3"`. Fill: `1E2435`. Border: 1.5 pt, `27AE60` (Emerald). Corner radius: `8`.
2. Position: X: **13.25"**, Y: **26.0"**.

**25b — Title:**
1. Add text: `IF IT MEASURES, IT MUST BE CALIBRATED`
2. Font: Barlow SemiBold, Size: `18`, Color: `27AE60` (Emerald)
3. Position: inside container, top-left with 16 pt padding.

**25c — Checklist:**
1. Add text. Copy-paste:
   ```
   - pH meter (2-point cal before each use)
   - Thermometer / RTD probe
   - XRF thickness gauge
   - Microhardness tester
   - Bake oven temperature controller
   - Rectifier ammeter and voltmeter
   - Ampere-hour meter
   ```
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Line height: `1.45`
3. Position: below title. Width: approximately `9.5"`.

**25d — Standard:**
1. Add text: `ISO 9001:2015 Section 7.1.5`
2. Font: JetBrains Mono Regular, Size: `12`, Color: `F0EDE8`, Transparency: **60%**
3. Position: near bottom of container.

### Step 26 — Group all of Zone 4
Select both callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Specification Strip

This zone occupies Y: 30.6" to 32.4" (1.8 inches tall). A single full-width standards reference strip.

### Step 27 — Standards strip container
1. Add rounded rectangle. Width: `23.0"`. Height: `1.5"`. Fill: `1E2435`. Corner radius: `6`.
2. Position: X: **0.5"**, Y: **30.7"**.

### Step 28 — Strip title
1. Add text: `GOVERNING STANDARDS`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`, Alignment: Left
3. Position: inside strip, left side with 0.15" padding from left edge.

### Step 29 — Standards list
1. Add text. Copy-paste:
   `ASTM B633  |  B117  |  B571  |  B568  |  B487  |  B499  |  ISO 9001  |  AS9100D  |  Nadcap AC7108`
2. Font: JetBrains Mono Regular, Size: `13`, Color: `F0EDE8`, Transparency: **80%**
3. Position: below title, centered within strip.

**Optional dividers:** Add thin vertical lines (1 pt, `3A4055` Mid Slate) between each standard name. If too tedious, the pipe characters `|` in the text already provide visual separation — skip the lines.

### Step 30 — Group all of Zone 5
Select strip container, title, and standards text. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

### Step 31 — Footer band background
1. Add rectangle. Width: `24.0"`. Height: `3.6"`. Fill: `0D1020`.
2. Position: X: **0"**, Y: **32.4"**.

### Step 32 — Disclaimer
1. Add text. Copy-paste:
   `This poster presents a generalized plating shop quality loop applicable to most electroplating operations. Specific quality requirements vary by customer specification, industry sector, and regulatory environment. Consult your quality management system documentation for site-specific procedures.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: X: **0.5"**, Y: **32.6"**. Width: `23.0"`.

### Step 33 — Poster title
1. Add text: `The Plating Shop Quality Loop`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.5"**, Y: **34.0"**.

### Step 34 — Series name
1. Add text: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, Y: **34.0"**.

### Step 35 — Logo placeholder
1. Add rounded rectangle. Width: `0.8"`. Height: `0.4"`. Fill: `3A4055`.
2. Position: X: **22.6"**, Y: **33.8"**.
3. Add text: `[LOGO]` — JetBrains Mono Regular, `12` pt, `F0EDE8`, Transparency: **50%**.

### Step 36 — Version
1. Add text: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: **22.6"**, Y: **35.2"**.

### Step 37 — Group all of Zone 6
Select footer rectangle, disclaimer, poster title, series name, logo, version. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline: `THE QUALITY LOOP` at 88 pt
- [ ] Subheading: `From Incoming Part to Final Inspection` in Amber
- [ ] "Special Process" callout references ISO 9001:2015 Section 8.5.1
- [ ] Section label: `THE SEVEN STATIONS OF PLATING QUALITY`
- [ ] Center text: `CERTIFIED. EVERY TIME.` with `Plan - Do - Check - Act` below
- [ ] All 7 station groups present on wheel with correct icons, labels, and consequence tags
- [ ] Feedback arrow labeled `CORRECTIVE ACTION` in Coral
- [ ] 4 PDCA labels present (PLAN/DO/CHECK/ACT)
- [ ] 8 detail cards present (7 stations + 1 feedback loop)
- [ ] Each card has: title, 4 checklist items, gate label
- [ ] H₂ embrittlement warning includes bake data table + 3 ASTM references
- [ ] Calibration checklist: 7 instruments
- [ ] Standards strip: 9 standards listed
- [ ] All Unicode: H₂ displays correctly
- [ ] Disclaimer, footer title, series name, LOGO, version present

### Color verification
- [ ] Stations 1-2: Teal circles and card accents
- [ ] Stations 3-5: Amber circles and card accents
- [ ] Stations 6-7: Emerald circles and card accents
- [ ] Feedback: Coral arrow and card accent
- [ ] All consequence tags in Coral
- [ ] All gate labels in Emerald
- [ ] Wheel borders and flow arrows in Mid Slate
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] Wheel is visually circular with stations evenly spaced
- [ ] Station labels don't overlap wheel ring or other stations
- [ ] 8 cards in 2 rows of 4 with consistent spacing
- [ ] H₂ and Calibration callouts side by side
- [ ] All text within 0.5-inch safe zone

### Readability check
- [ ] Zoom to 25% — wheel structure and station positions clear
- [ ] Zoom to 50% — station labels and consequence tags readable
- [ ] Zoom to 75% — card checklists and gate labels readable
- [ ] Zoom to 100% — all body text, standards strip, and footnotes readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 38 — Duplicate the page
1. **...** menu on page thumbnail > **Duplicate page**. Switch to Page 2.

### Step 39 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 40 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Card/callout fills** | `#1E2435` | `#ECEEF4` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |

**Station circle fills:** The accent-colored station circles remap to their darkened equivalents. The dark icon color inside (`#1A1F2E`) remaps to `#F5F4F0` (light icon on darkened circle). Verify icon contrast on each — all should pass WCAG AA.

**PDCA shading:** The 5% opacity quadrant tints (if used) may be invisible on light background. Either increase to 10-12% or omit entirely. The text labels alone carry the PDCA mapping.

**Inner circle fill:** Change from `#1A1F2E` to `#F5F4F0` so it matches the background.

### Step 41 — Post-remap adjustments
1. **Tagline at 65%**: If too faint, increase to **75-80%**.
2. **Consequence tags**: Verify Coral text (now `#B83E3E`) is readable on `#F5F4F0`.
3. **PDCA labels at 40%**: If too faint on light background, increase to **55%**.
4. **Standard references at 60-70%**: If too faint, increase to **75-80%**.
5. **Disclaimer at 50%**: If too faint, increase to **65%**.
6. **Station icons**: Verify `#F5F4F0` icons are visible on darkened accent circles.

### Post-remap verification checklist
- [ ] All body text passes WCAG AA
- [ ] Station circles clearly visible with readable icons inside
- [ ] Consequence tags readable against light background
- [ ] PDCA labels visible (even if faint — they are intentionally subtle)
- [ ] Feedback arrow clearly visible in Deep Coral
- [ ] Inner circle matches page background

---

## Phase 10 — Export Instructions

### Step 42 — Export Dark edition (Page 1)

**42a — Print PDF, 24x36":**
1. **Share** > **Download** > **PDF Print**. Check **Crop marks and bleed**. Page 1.
2. Rename: `Quality Loop — Dark — 24x36 — Print.pdf`

**42b — Digital PDF:**
1. **PDF Standard**. Uncheck crop marks. Page 1.
2. Rename: `Quality Loop — Dark — Digital.pdf`

**42c — Print PDF, 18x24":**
1. **Resize** > **18 x 24 inches** > **Copy & resize**. Verify 14 pt body text minimum. Card text (12 pt) will need verification at this size.
2. Export PDF Print. Rename: `Quality Loop — Dark — 18x24 — Print.pdf`

### Step 43 — Export Light edition (Page 2)

Repeat with these filenames:
- `Quality Loop — Light — 24x36 — Print.pdf`
- `Quality Loop — Light — Digital.pdf`
- `Quality Loop — Light — 18x24 — Print.pdf`

### Export file checklist
- [ ] `Quality Loop — Dark — 24x36 — Print.pdf`
- [ ] `Quality Loop — Dark — 18x24 — Print.pdf`
- [ ] `Quality Loop — Dark — Digital.pdf`
- [ ] `Quality Loop — Light — 24x36 — Print.pdf`
- [ ] `Quality Loop — Light — 18x24 — Print.pdf`
- [ ] `Quality Loop — Light — Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), inner circle fill, station icon fill, body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark), center text |
| `#E8A020` | Amber | Stations 3-5, "DO" PDCA, subheading |
| `#2EC4B6` | Teal | Stations 1-2, "PLAN" PDCA, callout borders |
| `#27AE60` | Emerald | Stations 6-7, "CHECK" PDCA, gate labels, calibration border |
| `#E05C5C` | Coral | Feedback arrow, consequence tags, H₂ warning, "ACT" PDCA, Special Process callout |
| `#3A4055` | Mid Slate | Wheel borders, flow arrows, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Card fills, callout fills, strip fill |
| `#252B3D` | Alt Row | Reserve (not primary) |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Card/callout fills (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#1E7A47` | Forest Green | Emerald elements (Light edition) |
| `#B83E3E` | Deep Coral | Coral elements (Light edition) |
| `#D0D4DE` | Light Slate | Wheel borders/dividers (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0. Watson flags non-blocking (Drew items). |
