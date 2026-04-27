---
Project: Plating Posters Inc
Poster Number: 9
Title: "Anodizing Fundamentals: Type I, II, and III at a Glance"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 9 — Anodizing Fundamentals — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Anodizing
  - v1
---

# Claude Chat Generation Prompt — Poster #9
## Anodizing Fundamentals: Type I, II, and III at a Glance
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

## Phase 2 — Zone 1: Header Band (Top of Poster)

This zone occupies the top 2.9 inches. Headline, subheading, and tagline on the left (~55%), "Not Electroplating" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element:
2. Select all placeholder text and type: `ANODIZING FUNDAMENTALS`
3. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `88`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
4. Position: left edge at 0.5 inches, top edge at 0.5 inches.
5. Set text box width to approximately **12.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Type I, II, and III at a Glance`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `36`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.5 inches**.

### Step 8 — Place the tagline
1. Add a body text element: Type: `The part IS the anode. The coating grows from the aluminum itself.`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: **65%**
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.2 inches**.

### Step 9 — Build the "Not Electroplating" callout box

**9a — Callout container:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Set properties:
   - **Width**: `9.5` inches
   - **Height**: `2.2` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 1.5 pt, color `2EC4B6` (Teal)
   - **Corner radius**: `8`
3. Position: left edge at 13.5 inches, top edge at 0.5 inches.

**9b — Callout title:**
1. Add a text element. Type: `NOT ELECTROPLATING`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6` (Teal)
3. Position: inside the container, top-left area, approximately 0.2 inches from the left edge and 0.15 inches from the top.

**9c — Callout body:**
1. Add a text element. Type: `In electroplating, the part is the cathode — metal deposits ON it from solution. In anodizing, the part is the anode — aluminum oxide grows FROM the surface. The coating IS the substrate, chemically converted.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`. Line height: **140%**.
3. Position: below the title with 0.1" gap. Width: approximately 9.0".

**9d — Reaction formula:**
1. Add a text element. Copy-paste: `2Al + 3H₂O → Al₂O₃ + 6H⁺ + 6e⁻`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`
3. Position: below the body text with 0.1" gap.

**9e — Group the callout box:**
Select the container, title, body, and reaction. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Three-Type Comparison Table (HERO)

This zone occupies Y: 2.9" to 16.2" (13.3 inches tall). This is the poster's primary visual — a four-column comparison table (row labels + Type I + Type II + Type III).

**Build strategy:** Build the column header row with accent fills, then build one data row as a template. Duplicate the template for all 11 data rows.

### Step 11 — Section label
1. Add a text element. Type: `THE THREE TYPES — MIL-A-8625`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, top edge at **3.0 inches**. Width: **23.0 inches**.

### Step 12 — Build the column header row

The column header row is 1.0" tall and consists of 4 adjacent rectangles with text inside each.

**Column widths:**
| Column | Width | X position (left edge) |
|--------|-------|----------------------|
| Row label | 3.7" | 0.5" |
| Type I | 6.1" | 4.2" |
| Type II | 6.1" | 10.3" |
| Type III | 7.1" | 16.4" |

**12a — Row label column header:**
1. Add a Rectangle. Width: `3.7"`. Height: `1.0"`. Fill: `3A4055` (Mid Slate). Corner radius: `6` (top-left corner only if possible; all corners is fine).
2. Position: X: 0.5", Y: 3.7".
3. No text inside this rectangle (it is the label column — just a gray block).

**12b — Type I column header:**
1. Add a Rounded Rectangle. Width: `6.1"`. Height: `1.0"`. Fill: `E8A020` (Amber). Corner radius: `6`.
2. Position: X: 4.2", Y: 3.7".
3. Add text inside (two lines):
   Line 1: `TYPE I` — Barlow Condensed ExtraBold, `24` pt, `1A1F2E` (dark text on Amber fill)
   Line 2: `CHROMIC ACID` — Barlow SemiBold, `16` pt, `1A1F2E`
4. Center both lines inside the rectangle.

**12c — Type II column header:**
1. Add a Rounded Rectangle. Width: `6.1"`. Height: `1.0"`. Fill: `2EC4B6` (Teal). Corner radius: `6`.
2. Position: X: 10.3", Y: 3.7".
3. Add text:
   Line 1: `TYPE II` — Barlow Condensed ExtraBold, `24` pt, `1A1F2E`
   Line 2: `SULFURIC ACID` — Barlow SemiBold, `16` pt, `1A1F2E`
4. Center inside.

**12d — Type III column header:**
1. Add a Rounded Rectangle. Width: `7.1"`. Height: `1.0"`. Fill: `E05C5C` (Coral). Corner radius: `6`.
2. Position: X: 16.4", Y: 3.7".
3. Add text:
   Line 1: `TYPE III` — Barlow Condensed ExtraBold, `24` pt, `1A1F2E`
   Line 2: `HARD COAT` — Barlow SemiBold, `16` pt, `1A1F2E`
4. Center inside.

### Step 13 — Build the first Data Row template (Row 1: Electrolyte)

**13a — Row label cell:**
1. Add a Rectangle. Width: `3.7"`. Height: `0.70"`. Fill: `1A1F2E` (base — same as background).
2. Position: X: 0.5", Y: 4.7" (directly below the column headers).
3. Add text: `Electrolyte` — Inter Medium, `15` pt, `F0EDE8`, Transparency: **80%**. Position: vertically centered, 0.15" padding from left edge.

**13b — Type I data cell:**
1. Add a Rectangle. Width: `6.1"`. Height: `0.70"`. Fill: `1A1F2E`.
2. Position: X: 4.2", Y: 4.7".
3. Add text: Copy-paste: `CrO₃, 3-10%` — JetBrains Mono Regular, `16` pt, `F0EDE8`, Alignment: Center.

**13c — Type II data cell:**
1. Add a Rectangle. Width: `6.1"`. Height: `0.70"`. Fill: `1A1F2E`.
2. Position: X: 10.3", Y: 4.7".
3. Add text: Copy-paste: `H₂SO₄, 15-20%` — JetBrains Mono, `16` pt, `F0EDE8`, Alignment: Center.

**13d — Type III data cell:**
1. Add a Rectangle. Width: `7.1"`. Height: `0.70"`. Fill: `1A1F2E`.
2. Position: X: 16.4", Y: 4.7".
3. Add text: Copy-paste: `H₂SO₄, 10-12%` — JetBrains Mono, `16` pt, `F0EDE8`, Alignment: Center.

**13e — Group the row:**
Select all 4 cell rectangles and all 4 text elements. Press **Ctrl+G**.

### Step 14 — Duplicate and modify for Rows 2-11

Duplicate Row 1, reposition below (each row is 0.70" tall), toggle base/alt fills. For text values that are plain text (not formulas), use Inter Regular `16` pt instead of JetBrains Mono.

| Row | Y | Fill | Label | Type I | Type II | Type III |
|-----|---|------|-------|--------|---------|----------|
| 2 | 5.40" | `#252B3D` | Temperature | 90-100 deg F | 68-72 deg F | 28-36 deg F |
| 3 | 6.10" | `#1A1F2E` | Current density | 5-10 ASF | 12-18 ASF | 24-36 ASF |
| 4 | 6.80" | `#252B3D` | Voltage | 0-40 V (ramped) | 15-21 V | 40-100+ V |
| 5 | 7.50" | `#1A1F2E` | Thickness | 0.05-0.15 mil | 0.2-1.0 mil | 1.0-4.0 mil |
| 6 | 8.20" | `#252B3D` | Hardness | Moderate | 300-400 HV | 500-700 HV |
| 7 | 8.90" | `#1A1F2E` | Color | Gray (undyed) | Clear; wide dye range | Dark bronze to black |
| 8 | 9.60" | `#252B3D` | Dyeability | Limited | Excellent | Limited (dark only) |
| 9 | 10.30" | `#1A1F2E` | Fatigue impact | Minimal (thin) | Moderate | Significant |
| 10 | 11.00" | `#252B3D` | Environmental | Copy-paste: `Cr⁶⁺ — restricted` | Copy-paste: `No Cr⁶⁺` | Copy-paste: `No Cr⁶⁺` |
| 11 | 11.70" | `#1A1F2E` | Primary use | Aerospace fatigue-critical | Decorative / general | Wear / engineering |

For each row: duplicate the previous row group, reposition, ungroup, change all 4 cell fills (all cells in a row share the same fill), change text, re-group.

**Text font guidance:** Use JetBrains Mono for numerical values (temperatures, ASF, voltages, thicknesses, hardness). Use Inter Regular for descriptive text (Color, Dyeability, Fatigue impact, Environmental, Primary use).

### Step 15 — Temperature callout
1. Add a text element. Type: `Near freezing — refrigeration required.`
2. Font: Inter Medium, Size: `14`, Color: `E05C5C` (Coral)
3. Position: right-aligned under the Type III column, approximately Y: 12.5".

### Step 16 — Dimensional growth callout
1. Add a text element. Type: `Dimensional growth: ~50% outward, ~50% inward. Net gain ≈ half of total oxide thickness.`
2. Font: Inter Medium, Size: `16`, Color: `F0EDE8`, Alignment: Center
3. Position: centered, approximately Y: 13.0". Width: 23.0".

### Step 17 — Group all of Zone 2
Select the section label, column header row (4 rectangles + text), all 11 data rows, and both callouts. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Concept Diagrams

This zone occupies Y: 16.2" to 23.4" (7.2 inches tall). "Part = Anode" circuit diagram on the left (45%), pore structure cross-section on the right (55%).

### Step 18 — Circuit diagram section label
1. Add a text element. Type: `HOW ANODIZING WORKS`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 16.3".

### Step 19 — Build the rectifier block
1. Add a Rounded Rectangle. Width: `3.0"`. Height: `1.0"`. Fill: `252B3D` (Alt Row). Border: 2 pt, `3A4055` (Mid Slate).
2. Position: centered at X: 5.5", Y: 17.5".
3. Add text inside: `DC RECTIFIER` — Barlow SemiBold, `14` pt, `F0EDE8`. Center.
4. Add text on the left side of the rectifier: `(+)` — JetBrains Mono, `14` pt, `E05C5C` (Coral).
5. Add text on the right side: `(-)` — JetBrains Mono, `14` pt, `2EC4B6` (Teal).

### Step 20 — Build the tank
1. Add a Rounded Rectangle. Width: `8.0"`. Height: `2.5"`. Fill: `1E2435` (Dark Callout). Border: 2 pt, `3A4055`.
2. Position: centered at X: 5.5", Y: 21.0".
3. Add a horizontal line inside at 70% height. Color: `2EC4B6`, Transparency: **20%**, Thickness: `1` pt.
4. Add text below the tank: Copy-paste: `H₂SO₄ or CrO₃ electrolyte` — Inter Regular, `11` pt, `F0EDE8`, Transparency: **60%**.

### Step 21 — Build the wires

**21a — Positive wire (left — to the anode/part):**
1. Add a line from the (+) terminal of the rectifier down to the left element inside the tank (the part).
2. Color: `E05C5C` (Coral). Thickness: `2` pt.

**21b — Negative wire (right — to the cathode):**
1. Add a line from the (-) terminal of the rectifier down to the right element inside the tank.
2. Color: `2EC4B6` (Teal). Thickness: `2` pt.

### Step 22 — Build the part (anode) inside the tank

1. Add a Rectangle. Width: `1.5"`. Height: `1.5"`. Fill: `C8D0D8` (Bright Silver — aluminum).
2. Position: left side of the tank interior.
3. Add a thin rectangle on the surface of the part: Width: `1.5"`. Height: `0.1"`. Fill: `E8A020` (Amber), Transparency: **40%**. This represents the oxide layer growing.
4. Add label below the part: `ANODE — The Part` — Barlow SemiBold, `12` pt, `E8A020` (Amber).
5. Add an arrow pointing outward from the oxide layer with label: `Oxide grows FROM surface` — Inter Medium, `12` pt, `2EC4B6` (Teal).

### Step 23 — Build the counter-electrode (cathode) inside the tank

1. Add a Rectangle. Width: `0.8"`. Height: `1.5"`. Fill: `3A4055` (Mid Slate).
2. Position: right side of the tank interior.
3. Add label below: `CATHODE` — Barlow SemiBold, `12` pt, `2EC4B6` (Teal).
4. Add a small upward arrow with bubbles near the cathode with label: Copy-paste: `H₂ gas` — Inter Regular, `11` pt, `F0EDE8`, Transparency: **70%**.

### Step 24 — Key contrast callout (below the circuit diagram)
1. Add a text element. Type (two lines):
   `Electroplating: part is cathode, metal deposits ON it.`
   `Anodizing: part is anode, oxide grows FROM it.`
2. Font: Inter Medium, Size: `15`, Color: `E8A020` (Amber)
3. Position: X: 0.5", Y: approximately 22.5".

### Step 25 — Pore Structure section label
1. Add a text element. Type: `THE PORE STRUCTURE`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: 11.0", Y: 16.3".

### Step 26 — Build the pore structure cross-section

Build from bottom to top, all elements centered within the right block area (X: 11.0" to 23.5").

**26a — Aluminum substrate (bottom):**
1. Add a Rectangle. Width: `8.0"`. Height: `0.8"`. Fill: `3A4055` (Mid Slate).
2. Position: centered in the block area, Y: approximately 22.0".
3. Add text inside: `ALUMINUM` — Barlow SemiBold, `14` pt, `F0EDE8`. Center.

**26b — Barrier layer (on top of substrate):**
1. Add a Rectangle. Width: `8.0"`. Height: `0.15"`. Fill: `E8A020` (Amber).
2. Position: directly on top of the substrate rectangle.
3. Add label to the right side (with a small arrow pointing at the layer): `Barrier layer (dense oxide)` — Inter Regular, `11` pt, `E8A020`.

**26c — Porous columns (rising from barrier layer):**
Build 7 narrow vertical rectangles:
1. Each: Width: `0.4"`. Height: `2.5"`. Fill: `2EC4B6` (Teal), Transparency: **60%**.
2. Space them evenly across the 8.0" width with approximately `0.35"` gaps between them.
3. Position: rising from the top of the barrier layer.

The gaps between the columns (where the dark background shows through) represent the pore channels.

**26d — Dye dots (inside pore channels):**
1. Add 3-4 small circles. Diameter: `0.2"` each.
2. Place them inside the gaps (pore channels) between columns, at mid-height.
3. Colors: Use `E05C5C` (red dye), `2EC4B6` (blue dye), and `1A1F2E` (black dye) — one color per dot.
4. Add label with arrow from the dots: `Dye trapped in pores` — Inter Regular, `11` pt, `F0EDE8`.

**26e — Sealed top (across column tops):**
1. Add a Rectangle. Width: `8.0"`. Height: `0.12"`. Fill: `C8D0D8` (Bright Silver).
2. Position: across the top of all columns.
3. Add label with arrow: `Sealed (hydrated oxide)` — Inter Regular, `11` pt, `C8D0D8`.

### Step 27 — Pore structure caption
1. Add a text element. Type: `The hexagonal cell structure gives anodizing its unique properties: permanent dye absorption, corrosion resistance, and electrical insulation.`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`
3. Position: below the cross-section, approximately Y: 22.8". Width: 12.0".

### Step 28 — Group all of Zone 3
Select both section labels, all circuit diagram elements, all pore structure elements, the key contrast callout, and the caption. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Alloy Compatibility + Pre-Treatment

This zone occupies Y: 23.4" to 29.5" (6.1 inches tall). Alloy chart on the left (55%), pre-treatment flow + defects on the right (45%).

### Step 29 — Alloy Compatibility section label
1. Add a text element. Type: `ALLOY COMPATIBILITY`
2. Font: Barlow Condensed ExtraBold, Size: `20`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 23.5".

### Step 30 — Alloy table header row

**30a — Header background:**
1. Add a Rectangle. Width: `12.0"`. Height: `0.45"`. Fill: `3A4055`.
2. Position: X: 0.5", Y: 24.0".

**30b — Header labels:**
- `ALLOY SERIES` — Barlow SemiBold, `15` pt, `F0EDE8`. X: 0.7". Width: 3.5".
- `EXAMPLE` — same. X: 4.2". Width: 3.0".
- `ANODIZING QUALITY` — same. X: 7.2". Width: 5.3".

### Step 31 — Alloy table data row template (Row 1: 1xxx)

**31a — Row background:**
1. Add a Rectangle. Width: `12.0"`. Height: `0.60"`. Fill: `1A1F2E`.
2. Position: X: 0.5", Y: 24.45".

**31b — Left accent bar:**
1. Add a Rectangle. Width: `0.06"`. Height: `0.60"`. Fill: `27AE60` (Emerald).
2. Position: flush left.

**31c — Row text:**
- Alloy Series: `1xxx (pure Al)` — Inter Regular, `14` pt, `F0EDE8`. X: 0.7".
- Example: `1100` — Inter Regular, `14` pt, `F0EDE8`. X: 4.2".
- Quality: `Excellent — clear, consistent` — Inter Regular, `14` pt, `F0EDE8`. X: 7.2".

**31d — Group the row.**

### Step 32 — Duplicate and modify for Rows 2-6

| Row | Y | Fill | Left accent | Alloy Series | Example | Quality |
|-----|---|------|-------------|-------------|---------|---------|
| 2 | 25.05" | `#252B3D` | Emerald | 5xxx (Al-Mg) | 5052 | Very good — clear to light gray |
| 3 | 25.65" | `#1A1F2E` | Emerald | 6xxx (Al-Mg-Si) | 6061, 6063 | Very good — 6063 = best architectural |
| 4 | 26.25" | `#252B3D` | Amber | 2xxx (Al-Cu) | 2024 | Fair to poor — yellowish oxide |
| 5 | 26.85" | `#1A1F2E` | Amber | 7xxx (Al-Zn) | 7075 | Fair — color inconsistency |
| 6 | 27.45" | `#252B3D` | Coral | Cast alloys | A356, 380 | Variable — silicon causes dark/grainy |

For Rows 4-5: Left accent bar fill = `E8A020` (Amber).
For Row 6: Left accent bar fill = `E05C5C` (Coral).

### Step 33 — Alloy key note
1. Add a text element. Type: `Higher alloying elements (Cu, Si) = worse anodizing. Pure Al and 6xxx produce the best results.`
2. Font: Inter Medium, Size: `14`, Color: `E8A020` (Amber)
3. Position: X: 0.5", Y: approximately 28.2".

### Step 34 — Pre-Treatment Flow section (right 45%)

**Position:** X: 13.25", Y: 23.5". Width: 10.25".

**Build 6 boxes connected by arrows in two rows of 3:**

Row 1: `CLEAN` -> `ETCH` -> `DESMUT`
Row 2: `ANODIZE` -> `DYE` -> `SEAL`

**For each box:**
1. Add a Rectangle. Width: `2.5"`. Height: `0.6"`. Fill: `252B3D`. Border: 1 pt, `3A4055`. Corner radius: `4`.
2. Add text inside: the step name — Barlow SemiBold, `12` pt, `F0EDE8`. Center.

**Box positions (approximate):**
| Box | X | Y |
|-----|---|---|
| CLEAN | 13.5" | 24.0" |
| ETCH | 16.3" | 24.0" |
| DESMUT | 19.1" | 24.0" |
| ANODIZE | 13.5" | 25.0" |
| DYE | 16.3" | 25.0" |
| SEAL | 19.1" | 25.0" |

**Arrows:** Add horizontal lines with arrowheads between boxes in each row. Color: `3A4055`, Thickness: `1.5` pt. Add a downward arrow from DESMUT to ANODIZE area.

### Step 35 — Process notes
1. Add a text element. Type (two lines):
   `Caustic etch: NaOH, 4-8 oz/gal, 140 deg F, 1-5 min`
   Copy-paste: `Desmut: HNO₃ or HNO₃/HF, room temp, 15-60 sec`
2. Font: Inter Regular, Size: `12`, Color: `F0EDE8`, Transparency: **70%**
3. Position: X: 13.25", Y: approximately 25.9".

### Step 36 — Common Defects table

**36a — Title:**
1. Add text: `COMMON DEFECTS`
2. Font: Barlow SemiBold, Size: `16`, Color: `E05C5C` (Coral)
3. Position: X: 13.25", Y: approximately 26.5".

**36b — Build Row 1 (template):**
1. Add a Rectangle. Width: `10.0"`. Height: `0.45"`. Fill: `1A1F2E`.
2. Left accent bar: Width: `0.06"`. Height: `0.45"`. Fill: `E05C5C` (Coral). Flush left.
3. Defect text: `Uneven color` — Inter Regular, `13` pt, `F0EDE8`. X: 13.5".
4. Cause text: `Inconsistent oxide; alloy variation` — Inter Regular, `13` pt, `F0EDE8`. X: ~17.5".
5. Group.

**36c — Duplicate for Rows 2-5:**

| Row | Y | Fill | Defect | Cause |
|-----|---|------|--------|-------|
| 2 | ~27.1" | `#252B3D` | Chalky oxide | Temp too high; over-processed |
| 3 | ~27.55" | `#1A1F2E` | Burning | High CD; poor contact |
| 4 | ~28.0" | `#252B3D` | Poor dye absorption | Oxide too thin; over-sealed |
| 5 | ~28.45" | `#1A1F2E` | Streaking | Poor cleaning; alloy segregation |

### Step 37 — Group all of Zone 4
Select all alloy table elements, key note, flow boxes, arrows, process notes, defect title, and defect table rows. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Spec Badge + Sealing Methods

This zone occupies Y: 29.5" to 32.4" (2.9 inches tall). MIL badge on the left (~40%), sealing methods on the right (~60%).

### Step 38 — MIL-A-8625 badge

**38a — Badge container:**
1. Add a Rounded Rectangle. Width: `9.0"`. Height: `2.5"`. Fill: `1E2435`. Border: 2 pt, `2EC4B6` (Teal). Corner radius: `8`.
2. Position: X: 0.5", Y: 29.6".

**38b — Spec title:**
1. Add text: `MIL-A-8625F`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `2EC4B6` (Teal)
3. Position: inside the badge, approximately 0.3" from top, centered or left-aligned.

**38c — Sub-text:**
1. Add text: `The governing specification for anodic coatings on aluminum`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`
3. Position: below the spec title.

**38d — Group the badge.**

### Step 39 — Sealing Methods

**39a — Title:**
1. Add text: `SEALING METHODS`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: 10.0", Y: 29.6".

**39b — Four sealing entries:**

Build 4 lines, each with a small Teal dot (circle, 0.15" diameter, fill `2EC4B6`) followed by text.

1. Add a circle. Width: `0.15"`. Height: `0.15"`. Fill: `2EC4B6`. Position: X: 10.3", Y: 30.3".
2. Add text next to it: `Hot water: 200-212 deg F — standard` — JetBrains Mono, `13` pt, `F0EDE8`.

Repeat for:
- `Nickel acetate: 180-200 deg F — aerospace` (Y: ~30.7")
- `Cold seal (NiF): 75-85 deg F — energy savings` (Y: ~31.1")
- `PTFE: variable — lubricity for hard coat` (Y: ~31.5")

### Step 40 — Group all of Zone 5
Select the badge group, title, and all 4 sealing entries (dots + text). Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 41 — Footer band background
1. Add a Rectangle (sharp corners). Width: `24"`. Height: `3.6"`. Fill: `0D1020` (Deep Navy). No border.
2. Position: X: 0", Y: 32.4".

### Step 42 — Disclaimer text
1. Add a text element. Type:
   `This poster presents anodizing fundamentals per MIL-A-8625F. Operating parameters vary by alloy, tank configuration, and product specification. Consult your process supplier for application-specific guidance.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: centered horizontally, Y: 32.6". Width: 23.0".

### Step 43 — Poster title (left)
1. Add a text element. Type: `Anodizing Fundamentals: Type I, II, and III at a Glance`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 34.0".

### Step 44 — Series name (center)
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, Y: 34.0".

### Step 45 — Logo placeholder (right)
1. Add a small Rounded Rectangle. Width: `0.8"`. Height: `0.4"`. Fill: `3A4055`. No border.
2. Position: X: 22.6", Y: 33.8".
3. Add text inside: `[LOGO]` — JetBrains Mono Regular, `12` pt, `F0EDE8`, Transparency: **50%**, Alignment: Center.

### Step 46 — Version number
1. Add a text element. Type: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: 22.6", Y: 35.2".

### Step 47 — Group all of Zone 6
Select the Deep Navy rectangle, disclaimer, poster title, series name, logo placeholder, and version. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline reads: `ANODIZING FUNDAMENTALS` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Type I, II, and III at a Glance` in Barlow SemiBold, `#E8A020`
- [ ] Tagline reads: `The part IS the anode. The coating grows from the aluminum itself.` at 65% transparency
- [ ] "Not Electroplating" callout has Teal border, body text, and chemical reaction formula
- [ ] Section label reads: `THE THREE TYPES — MIL-A-8625`
- [ ] Column headers: blank (Mid Slate) | TYPE I / CHROMIC ACID (Amber) | TYPE II / SULFURIC ACID (Teal) | TYPE III / HARD COAT (Coral)
- [ ] 11 data rows present with correct values per row
- [ ] Temperature callout under Type III: `Near freezing — refrigeration required.`
- [ ] Dimensional growth callout present
- [ ] Circuit diagram has: rectifier, tank, anode (silver), cathode, wires, labels
- [ ] Pore structure has: substrate, barrier layer, 7 columns, dye dots, sealed top
- [ ] Key contrast callout compares electroplating vs. anodizing
- [ ] Alloy table has 6 rows with correct accent colors (Emerald, Amber, Coral)
- [ ] Pre-treatment flow has 6 boxes in correct order: CLEAN > ETCH > DESMUT > ANODIZE > DYE > SEAL
- [ ] Defect table has 5 rows with Coral accents
- [ ] MIL-A-8625F badge present with Teal border
- [ ] 4 sealing methods listed with Teal dots
- [ ] Disclaimer, footer title, series name, LOGO placeholder, and version all present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] All body text is `#F0EDE8` — not pure white
- [ ] Type I column header: Amber fill with dark text
- [ ] Type II column header: Teal fill with dark text
- [ ] Type III column header: Coral fill with dark text
- [ ] Anode wire and (+) terminal: Coral
- [ ] Cathode wire and (-) terminal: Teal
- [ ] Aluminum part: Bright Silver
- [ ] Pore columns: Teal at 60% transparency
- [ ] Barrier layer: Amber
- [ ] Excellent alloy rows: Emerald accent. Fair: Amber. Variable: Coral.
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone
- [ ] Three-column table columns are aligned at guides
- [ ] Circuit diagram (left 45%) and pore structure (right 55%) sit side by side
- [ ] Alloy table (left 55%) and pre-treatment flow (right 45%) sit side by side
- [ ] No text is cut off or overlapping

### Readability check
- [ ] Zoom to 25% — headline, section labels, and column headers readable
- [ ] Zoom to 50% — parameter values and illustration labels readable
- [ ] Zoom to 75% — alloy data and defect entries readable
- [ ] Zoom to 100% — sealing methods, process notes, and disclaimer readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 48 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2. Rename "Light Edition" if possible.

### Step 49 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 50 — Remap all elements

Work through this table top to bottom, zone by zone:

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | "Not Electroplating" callout, tank fill, badge fill | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | Even-numbered rows, flow boxes, rectifier fill | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | Odd-numbered rows | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Type I column header fill, barrier layer, anode label, oxide layer, alloy notes, alloy Amber accents | `#E8A020` | `#C8860A` |
| **Teal elements** | Type II column header fill, callout borders/titles, pore columns, cathode label, sealing dots, electrolyte line | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | Alloy Emerald accent bars | `#27AE60` | `#1E7A47` |
| **Coral elements** | Type III column header fill, defect accents, (+) terminal, anode wire, temperature callout | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Row label column fill, substrate, tank border, flow box borders, cathode rectangle | `#3A4055` | `#D0D4DE` |
| **Bright Silver** | Aluminum part, sealed top | `#C8D0D8` | `#C8D0D8` — **UNCHANGED** |

### Step 51 — Critical Override: Column header text

**This override is required.** The column header text on the accent fills (Type I, Type II, Type III) uses `#1A1F2E` (dark text) in the Dark edition. In the Light edition, the darkened accent fills (`#C8860A`, `#1A8C82`, `#B83E3E`) do not have sufficient contrast with `#1A1F2E` text.

**Change the column header text to `#F0EDE8` (Warm White) in the Light edition.** This applies to:
- `TYPE I` and `CHROMIC ACID` inside the Amber column header
- `TYPE II` and `SULFURIC ACID` inside the Teal column header
- `TYPE III` and `HARD COAT` inside the Coral column header

### Step 52 — Post-remap adjustments

1. **Pore columns**: The Teal columns at 60% transparency become darkened Teal (`#1A8C82`) at 60% on `#F5F4F0`. Verify they are still clearly visible. If too faint, increase opacity to **70%**.
2. **Dye dots**: The dye dots inside pore channels retain their original colors — they represent actual dye colors, not design accent colors. Do not remap the blue or red dye dots.
3. **Footnote and disclaimer text**: At 50% opacity, verify readability on Off-White. If too faint, increase to **65%**.
4. **Tagline**: At 65% opacity, verify readability. Increase to **80%** if needed.
5. **Process notes**: At 70% opacity, verify readability. Increase to **85%** if needed.

---

## Phase 10 — Export Instructions

### Step 53 — Export the Dark edition (Page 1)

**53a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed**.
4. Select only **Page 1**.
5. Download and rename to: `Anodizing-Fundamentals-Dark-24x36-Print.pdf`

**53b — Digital PDF, 24x36":**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks.
2. Select Page 1. Rename to: `Anodizing-Fundamentals-Dark-Digital.pdf`

**53c — Print PDF, 18x24":**
1. 
2. Verify body text is at least 14 pt.
3. Export as PDF Print (with crop marks and bleed).
4. Rename to: `Anodizing-Fundamentals-Dark-18x24-Print.pdf`

### Step 54 — Export the Light edition (Page 2)

Repeat Step 53 for Page 2 with these filenames:
- `Anodizing-Fundamentals-Light-24x36-Print.pdf`
- `Anodizing-Fundamentals-Light-Digital.pdf`
- `Anodizing-Fundamentals-Light-18x24-Print.pdf`

### Export file checklist
- [ ] `Anodizing-Fundamentals-Dark-24x36-Print.pdf`
- [ ] `Anodizing-Fundamentals-Dark-18x24-Print.pdf`
- [ ] `Anodizing-Fundamentals-Dark-Digital.pdf`
- [ ] `Anodizing-Fundamentals-Light-24x36-Print.pdf`
- [ ] `Anodizing-Fundamentals-Light-18x24-Print.pdf`
- [ ] `Anodizing-Fundamentals-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light), column header text |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | Type I column, barrier layer, anode label, alloy notes |
| `#2EC4B6` | Teal | Type II column, callout borders, pore columns, cathode, sealing |
| `#27AE60` | Emerald | Excellent alloy accents |
| `#E05C5C` | Coral | Type III column, defect accents, anode wire, (+) terminal |
| `#3A4055` | Mid Slate | Row label column, substrate, tank, cathode, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout fills, tank fill, badge fill |
| `#252B3D` | Alt Row | Even rows, flow boxes, rectifier |
| `#C8D0D8` | Bright Silver | Aluminum part, sealed top (both editions) |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Callout fills (Light edition) |
| `#E8E8F0` | Alt Row Light | Even rows (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#1E7A47` | Forest Green | Emerald elements (Light edition) |
| `#B83E3E` | Deep Coral | Coral elements (Light edition) |
| `#D0D4DE` | Light Slate | Rules/dividers (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0 (2026-04-04). All technical content production-ready. Watson flags are non-blocking. |
