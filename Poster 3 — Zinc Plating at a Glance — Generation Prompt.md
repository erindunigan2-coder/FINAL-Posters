---
Project: Plating Posters Inc
Poster Number: 3
Title: "Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 3 — Zinc Plating at a Glance — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ZincPlating
  - v1
---

# Claude Chat Generation Prompt — Poster #3
## Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide
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

This zone occupies the top 2.9 inches. Headline + subheading + tagline on the left (~55%), "Why Two Systems?" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element: Type: `ZINC PLATING AT A GLANCE`
2. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `88`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at 0.5 inches. Width: **12.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Acid Chloride vs. Alkaline Non-Cyanide`
2. Font: Barlow SemiBold, Size: `36`, Color: `E8A020` (Amber), Alignment: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.5 inches**.

### Step 8 — Place the tagline
1. Add body text. Type: `Same goal. Different chemistry. Know the difference.`
2. Font: Barlow SemiBold, Size: `22`, Color: `F0EDE8`, Transparency: **65%**, Alignment: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.2 inches**.

### Step 9 — Build "Why Two Systems?" callout box

**9a — Callout container:**
1. Add a Rounded Rectangle. Width: `9.5` inches. Height: `2.2` inches.
2. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6` (Teal). Corner radius: `8`.
3. Position: X: **13.5 inches**. Y: **0.5 inches**.

**9b — Callout title:**
1. Add text: `WHY TWO SYSTEMS?`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6`
3. Position: inside container, approximately 0.2 inches from left edge and 0.15 inches from top.

**9c — Body text:**
1. Add text: `Both produce sacrificial zinc coatings that protect steel from corrosion. Acid zinc is fast and bright. Alkaline zinc throws better and bends without cracking. The right choice depends on your part and your spec.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`. Line spacing: `1.4`. Width: approximately **9.0 inches**.
3. Position: below title with 0.1 inches gap.

**9d — Supplier note:**
1. Add text: `Consult your supplier's TDS for acid chloride and alkaline non-cyanide zinc formulations`
2. Font: JetBrains Mono Regular, Size: `14`, Color: `E8A020` at 60% opacity.
3. Position: below body text with 0.1 inches gap.

**9e — Group the callout.** Select all callout elements. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Master Comparison Table (The Hero)

This zone occupies Y: 2.9" to 18.0" (15.1 inches tall). A section label plus a 16-row comparison table with 3 columns (Parameter, Acid Chloride, Alkaline Non-Cyanide).

### Step 11 — Section label
1. Add text: `HEAD-TO-HEAD: EVERY PARAMETER THAT MATTERS`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, Y: **3.0 inches**. Width: **23.0 inches**.

### Step 12 — Build the column header row

**12a — Parameter column header:**
1. Add a Rectangle (sharp corners or 4 pt top-corner radius).
   - **Width**: `6.4` inches. **Height**: `0.60` inches.
   - **Fill**: `3A4055` (Mid Slate)
2. Position: X: **0.5 inches**. Y: **3.6 inches**.
3. Add text inside: `PARAMETER`
4. Font: Barlow SemiBold, Size: `18`, Color: `F0EDE8`. Position: centered in this column area.

**12b — Acid Chloride column header:**
1. Add a Rectangle. Width: `8.3` inches. Height: `0.60` inches. Fill: `E8A020` (Amber).
2. Position: X: **6.9 inches**. Y: **3.6 inches** (flush with the parameter column).
3. Add text inside: `ACID CHLORIDE`
4. Font: Barlow SemiBold, Size: `18`, Color: `1A1F2E` (dark text on amber fill).

**12c — Alkaline NC column header:**
1. Add a Rectangle. Width: `8.3` inches. Height: `0.60` inches. Fill: `2EC4B6` (Teal).
2. Position: X: **15.2 inches**. Y: **3.6 inches**.
3. Add text inside: `ALKALINE NON-CYANIDE`
4. Font: Barlow SemiBold, Size: `18`, Color: `1A1F2E` (dark text on teal fill).

### Step 13 — Build Row 1 (Template Row): Primary salt

**13a — Row background (3 cells):**
1. Add 3 rectangles spanning the full table width, matching column widths:
   - Parameter cell: Width `6.4"`, Height `0.65"`, Fill `1A1F2E`
   - Acid cell: Width `8.3"`, Height `0.65"`, Fill `1A1F2E`
   - Alkaline cell: Width `8.3"`, Height `0.65"`, Fill `1A1F2E`
2. Position: directly below the column header row (Y: approximately **4.2 inches**). Each cell flush with the cell above it.

**Simpler approach:** Use a single rectangle spanning the full table width (23.0 inches) for the row background, then place text at the appropriate column X positions.

1. Add a Rectangle. Width: `23.0` inches. Height: `0.65` inches. Fill: `1A1F2E`. No border.
2. Position: X: **0.5 inches**. Y: **4.2 inches**.

**13b — Parameter text:**
1. Add text: `Primary salt`
2. Font: Inter Medium, Size: `16`, Color: `F0EDE8`, Alignment: Left
3. Position: X: **0.7 inches**, vertically centered in the row.

**13c — Acid Chloride value:**
1. Add text: `KCl 180-250 g/L`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`, Alignment: Center
3. Position: centered in the Acid column (approximately X: **7.0 inches**). Width: **8.1 inches**.

**13d — Alkaline NC value:**
1. Add text: `NaOH 100-140 g/L`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`, Alignment: Center
3. Position: centered in the Alkaline column (approximately X: **15.3 inches**). Width: **8.1 inches**.

**13e — Group Row 1:** Select the background rectangle and all 3 text elements. Press **Ctrl+G**.

### Step 14 — Build Rows 2–16 (Duplicate and Modify)

Duplicate Row 1 for each remaining row. Reposition each flush below the previous (each is 0.65" tall). Alternate fills: base `#1A1F2E` / alt `#252B3D`.

| Row | Y | Fill | Parameter | Acid Chloride | Alkaline Non-Cyanide |
|-----|---|------|-----------|---------------|----------------------|
| 2 | 4.85" | alt | Zinc metal | 15-30 g/L (2.0-4.0 oz/gal) | 8-15 g/L (1.1-2.0 oz/gal) |
| 3 | 5.50" | base | pH | 4.5-5.5 (target 4.8-5.2) | 13-14 |
| 4 | 6.15" | alt | Temperature | 20-30 C (68-86 F) | 22-30 C (72-86 F) |
| 5 | 6.80" | base | Rack CD | 2-5 A/dm² (19-46 ASF) | 1-4 A/dm² (9-37 ASF) |
| 6 | 7.45" | alt | Barrel CD | 0.3-1.5 A/dm² (3-14 ASF) | 0.3-1.5 A/dm² (3-14 ASF) |
| 7 | 8.10" | base | Cathode efficiency | 95-98% | 60-80% |
| 8 | 8.75" | alt | Throwing power | Moderate | Excellent |
| 9 | 9.40" | base | Anode type | Soluble zinc (SHG 99.99%) | Insoluble mild steel |
| 10 | 10.05" | alt | A:C ratio | 2:1 | 2:1 rack / 2.5:1 barrel |
| 11 | 10.70" | base | Buffer | Boric acid (25-45 g/L) | NaOH (inherent stability) |
| 12 | 11.35" | alt | Critical ratio | Zn:boric acid balance | NaOH:Zn 9:1-12:1 |
| 13 | 12.00" | base | Deposit appearance | Bright to semi-bright | Semi-bright to matte |
| 14 | 12.65" | alt | Deposit ductility | Good | Excellent |
| 15 | 13.30" | base | Iron limit | <50 ppm (action at 25) | <20 ppm (action at 10) |
| 16 | 13.95" | alt | Copper limit | <10 ppm (action at 5) | <5 ppm (action at 2) |

**Font notes for data columns:** Use JetBrains Mono for numerical values and ranges. Use Inter Regular for text-only values (like "Moderate," "Excellent," "Soluble zinc").

### Step 15 — Table footnote
1. Add text. Copy-paste:
   `*Ranges are for normal production plating. NH₄Cl systems: similar parameters with additional buffering capacity and ammonia-bearing wastewater. Consult your product TDS for formulation-specific operating ranges.*`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`, Transparency: **60%**
3. Position: X: **0.5 inches**, Y: approximately **14.8 inches** (0.2" below the last row).

### Step 16 — Group all of Zone 2
Select the section label, column header row, all 16 data rows, and the footnote. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Throwing Power + CE Concept

This zone occupies Y: 18.0" to 24.5" (6.5 inches tall). Left 55% is a throwing power illustration. Right 45% is a cathode efficiency concept graph.

### Step 17 — Block D section label
1. Add text: `THROWING POWER — THE KEY DIFFERENCE`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: **0.5 inches**. Y: **18.1 inches**.

### Step 18 — Build Acid Zinc U-channel (left)

Build a U-channel (trough) from three rectangles representing a steel part cross-section.

**18a — Base (floor):**
1. Add a Rectangle. Width: `2.5` inches. Height: `0.3` inches. Fill: `3A4055` (Mid Slate).
2. Position: centered at approximately X: **2.5 inches**. Y: approximately **22.2 inches**.

**18b — Left wall:**
1. Add a Rectangle. Width: `0.3` inches. Height: `2.0` inches. Fill: `3A4055`.
2. Position: X: **2.5 inches**. Y: **20.2 inches**.

**18c — Right wall:**
1. Add a Rectangle. Width: `0.3` inches. Height: `2.0` inches. Fill: `3A4055`.
2. Position: X: **4.7 inches**. Y: **20.2 inches**.

**18d — Deposit layers (UNEVEN — acid zinc has poor throwing power):**
- Top edges of walls — THICK deposit: Add a Rectangle. Width: `0.15` inches. Height: `0.3` inches. Fill: `C8D0D8`. Position at top-outer edge of each wall.
- Inner wall surfaces — MEDIUM: Add a Rectangle. Width: `0.08` inches. Height: `2.0` inches. Fill: `C8D0D8`. Position along each inner wall face.
- Bottom of recess — THIN: Add a Rectangle. Width: `1.9` inches. Height: `0.03` inches. Fill: `C8D0D8`. Position along the inside floor of the U-channel.

**18e — Label above:** Add text: `ACID CHLORIDE`
Font: Barlow SemiBold, Size: `14`, Color: `E8A020` (Amber). Position: centered above the U-channel.

**18f — Annotations (use small arrow lines from the design tool Elements + text):**
- Near thick deposit: `Thick at HCD` — Inter Regular, 11 pt, `F0EDE8` at 80%
- Near thin recess: `Thin at LCD` — same styling

**18g — Ratio below channel:**
Add text: `3:1 to 5:1 variation`
Font: JetBrains Mono, Size: `13`, Color: `E8A020`. Position: centered below the U-channel.

### Step 19 — Build Alkaline Zinc U-channel (right of left block)

**19a — Build the same 3-rectangle U-channel** centered at approximately X: **8.5 inches**. Same dimensions and `#3A4055` fill.

**19b — Deposit layers (UNIFORM — alkaline zinc has excellent throwing power):**
- Top edges: `0.10` inches thick
- Inner walls: `0.08` inches thick
- Bottom recess: `0.07` inches thick
All fill: `C8D0D8`.

**19c — Label above:** `ALKALINE NC`
Font: Barlow SemiBold, 14 pt, `2EC4B6` (Teal).

**19d — Annotation:** `Uniform coverage` — Inter Regular, 11 pt, `F0EDE8` at 80%.

**19e — Ratio below:** `1.5:1 to 2:1 variation`
Font: JetBrains Mono, 13 pt, `2EC4B6`.

### Step 20 — Caption below both channels
1. Add text:
   `Same part. Same spec. Different distribution. Alkaline zinc's variable efficiency redistributes metal toward recesses.`
2. Font: Inter Medium, Size: `14`, Color: `F0EDE8`, Alignment: Center
3. Position: centered below both channels. Width: approximately **12.0 inches**.

### Step 21 — Block E: CE Concept Graph

**Section label:**
1. Add text: `WHY ALKALINE ZINC THROWS BETTER`
2. Font: Barlow Condensed ExtraBold, Size: `20`, Color: `F0EDE8`
3. Position: X: **13.5 inches**. Y: **18.1 inches**.

**Graph construction (graph area: 9.0" wide x 3.5" tall, below section label):**

**21a — Y-axis line:**
1. Add a vertical line from bottom-left to top-left of graph area.
2. Stroke: 2 pt, `3A4055`.

**21b — X-axis line:**
1. Add a horizontal line along the bottom of the graph area.
2. Stroke: 2 pt, `3A4055`.

**21c — Y-axis label:**
1. Add text: `Cathode Efficiency (%)`
2. Font: JetBrains Mono, Size: `12`, Color: `F0EDE8`, Transparency: **70%**
3. Rotate the text 90 degrees (use the rotation handle in the design). Position vertically along the Y-axis.

**21d — X-axis label:**
1. Add text: `Current Density (ASF)`
2. Font: JetBrains Mono, Size: `12`, Color: `F0EDE8`, Transparency: **70%**
3. Position: centered below the X-axis.

**21e — Y-axis tick marks:**
Add text elements for `60%`, `80%`, `100%` — JetBrains Mono, 11 pt, `F0EDE8` at 60%. Position at appropriate heights along the Y-axis.

**21f — X-axis tick marks:**
Add text elements for `Low`, `High` — JetBrains Mono, 11 pt, `F0EDE8` at 60%.

**21g — Acid zinc line (flat):**
1. Add a single horizontal line at approximately 95% height across the graph area.
2. Stroke: 3 pt, `E8A020` (Amber).
3. Add label at right end: `Acid: 95-98%` — Inter Medium, 13 pt, `E8A020`.

**21h — Alkaline zinc line (declining curve):**
1. Add 3-4 connected line segments from approximately 80% at left edge declining to 60% at right edge.
2. Stroke: 3 pt, `2EC4B6` (Teal).
3. Add label at right end: `Alkaline: 80% → 60%` — Inter Medium, 13 pt, `2EC4B6`.

**21i — Key insight:**
1. Add text: `Variable efficiency = self-leveling. LCD areas plate more efficiently, naturally pushing metal into recesses.`
2. Font: Inter Medium, Size: `14`, Color: `2EC4B6`
3. Position: below the graph, within the Block E area.

### Step 22 — Group all of Zone 3
Select all throwing power elements, all CE graph elements, and the caption. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Decision Guide + Passivation

This zone occupies Y: 24.5" to 29.5" (5.0 inches tall). Left 55% is a decision guide callout. Right 45% is a passivation compatibility table.

### Step 23 — Build "When to Choose Which" callout

**23a — Container:**
1. Add a Rounded Rectangle. Width: `12.5` inches. Height: `4.6` inches.
2. Fill: `1E2435` (Dark Callout). Corner radius: `8`. No border.
3. Position: X: **0.5 inches**. Y: **24.6 inches**.

**23b — Section label (inside box):**
1. Add text: `WHEN TO CHOOSE WHICH`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`, Alignment: Center
3. Position: centered inside the box, near the top.

**23c — Left sub-column: CHOOSE ACID**
1. Add text: `CHOOSE ACID WHEN:`
2. Font: Barlow SemiBold, Size: `16`, Color: `E8A020`
3. Position: left area of box, approximately X: **0.85 inches**.

4. Add bullet list:
   `Simple geometry (flat, cylindrical)`
   `High throughput required`
   `Bright appearance matters`
   `Barrel plating small parts`
   `New installation — easier operation`
   `Ammonia-free wastewater (KCl)`
5. Font: Inter Regular, Size: `14`, Color: `F0EDE8`. Line spacing: `1.4`.

**23d — Right sub-column: CHOOSE ALKALINE**
1. Add text: `CHOOSE ALKALINE WHEN:`
2. Font: Barlow SemiBold, Size: `16`, Color: `2EC4B6`
3. Position: right area of box, approximately X: **7.0 inches**.

4. Add bullet list:
   `Complex geometry (recesses, threads)`
   `Tight thickness tolerance`
   `Paint/powder coat adhesion critical`
   Copy-paste: `High-strength steel (reduced H₂ risk)`
   `Uniform passivate color needed`
   `Customer spec requires it`
5. Font: Inter Regular, Size: `14`, Color: `F0EDE8`. Line spacing: `1.4`.

**23e — Center divider:**
1. Add a vertical line between the two sub-columns.
2. Stroke: 1 pt, `3A4055`. Height: approximately 80% of the box height.

**23f — Closing text:**
1. Add text: `Neither is universally better. The right choice depends on the part and the spec.`
2. Font: Inter Medium, Size: `13`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered below the two columns, near bottom of box.

**23g — Group the callout.** Press **Ctrl+G**.

### Step 24 — Passivation compatibility section label
1. Add text: `PASSIVATION COMPATIBILITY`
2. Font: Barlow Condensed ExtraBold, Size: `20`, Color: `F0EDE8`
3. Position: X: **13.25 inches**. Y: **24.6 inches**.

### Step 25 — Passivation table header row
1. Add a Rectangle. Width: `9.75` inches. Height: `0.45` inches. Fill: `3A4055`.
2. Position: X: **13.25 inches**. Y: **25.1 inches**.
3. Add 3 header texts:
   - `Passivation` — X: **13.45"**, Barlow SemiBold, 14 pt, `F0EDE8`
   - `Salt Spray (white)` — X: **17.45"**, same styling
   - `RoHS` — X: **20.45"**, same styling

### Step 26 — Build passivation data rows

Each row: 0.50" tall, full table width (9.75"). Alternate base/alt fills.

**Row 1** (Y: 25.55", base fill):
- Passivation: `Clear/blue trivalent`
- Salt Spray: `72-120 hrs` (JetBrains Mono, 13 pt)
- RoHS: `Yes` (color: `27AE60` Emerald)

**Row 2** (Y: 26.05", alt fill `252B3D`):
- Passivation: `Yellow trivalent`
- Salt Spray: `120-200 hrs`
- RoHS: `Yes` (Emerald)

**Row 3** (Y: 26.55", base fill):
- Passivation: `Black trivalent`
- Salt Spray: `72-120 hrs`
- RoHS: `Yes` (Emerald)

**Row 4** (Y: 27.05", alt fill):
- Passivation: `Yellow hex (legacy)`
- Salt Spray: `96-240 hrs`
- RoHS: `No` (color: `E05C5C` Coral)

**Row 5** (Y: 27.55", base fill):
- Passivation: `Olive drab hex`
- Salt Spray: `200+ hrs`
- RoHS: `No` (Coral)

All other text: Inter Regular, 13 pt, `F0EDE8`.

### Step 27 — Passivation key note
1. Add text: `Both zinc bath types are compatible with trivalent and hexavalent passivation chemistries. Consult your supplier for recommended passivate products.`
2. Font: Inter Medium, Size: `13`, Color: `27AE60` (Emerald)
3. Position: below the last table row.

### Step 28 — Group all of Zone 4
Select the decision guide group, passivation section label, table header, all 5 data rows, and key note. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Specs + Common Problems

This zone occupies Y: 29.5" to 32.4" (2.9 inches tall). Left 50% has ASTM B633 specs, right 50% has common problems.

### Step 29 — ASTM B633 label
1. Add text: `ASTM B633 — SERVICE CONDITIONS`
2. Font: Barlow SemiBold, Size: `16`, Color: `E8A020`
3. Position: X: **0.5 inches**. Y: **29.6 inches**.

### Step 30 — ASTM B633 table

Compact table: 3 columns (SC, Environment, Min Thickness). Table width: **11.0 inches**. Row height: 0.40".

**Header row** (Y: 29.95"): Rectangle, `3A4055` fill. Header text: Barlow SemiBold, 13 pt, `F0EDE8`.

**Data rows:**
| Row | Y | Fill | SC | Environment | Min Thickness |
|-----|---|------|----|-------------|---------------|
| 1 | 30.35" | base | SC1 | Indoor, dry | 5 um (0.2 mil) |
| 2 | 30.75" | alt | SC2 | Moderate | 8 um (0.3 mil) |
| 3 | 31.15" | base | SC3 | Severe, outdoor | 12 um (0.5 mil) |
| 4 | 31.55" | alt | SC4 | Very severe | 25 um (1.0 mil) |

SC text: Inter Medium, 13 pt. Environment: Inter Regular, 13 pt. Thickness: JetBrains Mono, 13 pt.

### Step 31 — Common Problems label
1. Add text: `COMMON PROBLEMS — QUICK REFERENCE`
2. Font: Barlow SemiBold, Size: `16`, Color: `E05C5C` (Coral)
3. Position: X: **12.0 inches**. Y: **29.6 inches**.

### Step 32 — Common problems table

Table width: **11.5 inches**. Row height: 0.40". 3 columns: Problem, Acid Cause, Alkaline Cause.

**Header row** (Y: 29.95"): Rectangle, `3A4055` fill.

**Data rows:**
| Row | Y | Fill | Problem | Acid Cause | Alkaline Cause |
|-----|---|------|---------|-----------|----------------|
| 1 | 30.35" | base | Burning | Low Zn; low boric acid | Low Zn; low NaOH:Zn |
| 2 | 30.75" | alt | Pitting | Low carrier; organics | Copy-paste: Low carrier; H₂ adhesion |
| 3 | 31.15" | base | Roughness | pH >5.5; anode bags | High carbonate; filtration |
| 4 | 31.55" | alt | Dullness | High temp; low brightener | Brightener deficient |

Problem text: Inter Medium, 12 pt, `F0EDE8`. Cause text: Inter Regular, 12 pt, `F0EDE8`.
Left-border accents: 0.06" wide rectangles, `E05C5C` (Coral), on each row.

### Step 33 — Group all of Zone 5
Select both labels, both tables, and all rows. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 34 — Footer band background
1. Add a Rectangle. Width: `24` inches. Height: `3.6` inches. Fill: `0D1020` (Deep Navy). No border.
2. Position: X: **0 inches**. Y: **32.4 inches**.

### Step 35 — Disclaimer
1. Add text:
   `This poster presents industry-typical operating parameters for acid chloride and alkaline non-cyanide zinc plating. Specific ranges vary by vendor formulation — always consult your product TDS. Analysis by titration is the authoritative method for confirming bath composition.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: centered horizontally. Y: **32.6 inches**. Width: **23.0 inches**.

### Step 36 — Poster title
1. Add text: `Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.5 inches**. Y: **34.0 inches**.

### Step 37 — Series name
1. Add text: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally. Y: **34.0 inches**.

### Step 38 — Logo placeholder
1. Add text: `[LOGO]`
2. Font: Barlow SemiBold, Size: `14`, Color: `F0EDE8`, Transparency: **30%**, Alignment: Center
3. Position: X: **22.6 inches**. Y: **33.8 inches**.

### Step 39 — Version
1. Add text: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: **22.6 inches**. Y: **35.2 inches**.

### Step 40 — Group all of Zone 6
Select all footer elements. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline: `ZINC PLATING AT A GLANCE`
- [ ] Subheading: `Acid Chloride vs. Alkaline Non-Cyanide` in Amber
- [ ] Callout contains generic supplier note directing reader to their process chemistry supplier TDS
- [ ] Table has 16 data rows with correct parameter names
- [ ] Row 7 (Cathode efficiency): Acid = 95-98%, Alkaline = 60-80%
- [ ] Row 8 (Throwing power): Acid = Moderate, Alkaline = Excellent
- [ ] Throwing power illustration has 2 U-channels — left (uneven), right (uniform)
- [ ] CE graph has flat Amber line and declining Teal line
- [ ] Decision guide has two sub-columns: CHOOSE ACID and CHOOSE ALKALINE
- [ ] Passivation table has 5 rows with RoHS Yes/No color-coded
- [ ] ASTM B633 table has 4 service conditions (SC1–SC4)
- [ ] Common problems table has 4 rows (Burning, Pitting, Roughness, Dullness)

### Color verification
- [ ] Amber (`#E8A020`) used consistently for Acid Chloride column and accents
- [ ] Teal (`#2EC4B6`) used consistently for Alkaline NC column and accents
- [ ] Column headers have dark text (`#1A1F2E`) on Amber/Teal fills
- [ ] RoHS "Yes" is Emerald, "No" is Coral

### Readability check
- [ ] Zoom to 25% — headline and section labels readable
- [ ] Zoom to 50% — column headers and throwing power labels readable
- [ ] Zoom to 75% — table data readable
- [ ] Zoom to 100% — footnotes and disclaimer readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 41 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2.

### Step 42 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 43 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |
| **Bright Silver** | `#C8D0D8` | `#C8D0D8` (**unchanged**) |

**Override 1 — Column header text:** The text on the Amber and Teal column header fills must KEEP its original color `#F0EDE8` (Warm White) in the Light edition. Do NOT remap it to `#1A1F2E`. The darkened accent fills (`#C8860A` and `#1A8C82`) have insufficient contrast with dark text.

**Override 2 — CE graph lines:** Verify the darkened Teal (`#1A8C82`) and Amber (`#C8860A`) lines are clearly visible against `#F5F4F0`. If not, increase line stroke to 4 pt in the Light edition.

### Step 44 — Post-remap adjustments
1. **Footnotes and disclaimer:** Verify readability at reduced opacity on the light background. Increase opacity by 10-15% if too faint.
2. **Decision guide closing text:** At 70% opacity, verify readability. Adjust if needed.

---

## Phase 10 — Export Instructions

### Step 45 — Export Dark edition (Page 1)
- PDF Print 24x36" with crop marks → `Zinc-Plating-Glance-Dark-24x36-Print.pdf`
- PDF Standard 24x36" → `Zinc-Plating-Glance-Dark-Digital.pdf`
- Resize to 18x24" → PDF Print → `Zinc-Plating-Glance-Dark-18x24-Print.pdf`

### Step 46 — Export Light edition (Page 2)
- `Zinc-Plating-Glance-Light-24x36-Print.pdf`
- `Zinc-Plating-Glance-Light-Digital.pdf`
- `Zinc-Plating-Glance-Light-18x24-Print.pdf`

### Export file checklist
- [ ] `Zinc-Plating-Glance-Dark-24x36-Print.pdf`
- [ ] `Zinc-Plating-Glance-Dark-18x24-Print.pdf`
- [ ] `Zinc-Plating-Glance-Dark-Digital.pdf`
- [ ] `Zinc-Plating-Glance-Light-24x36-Print.pdf`
- [ ] `Zinc-Plating-Glance-Light-18x24-Print.pdf`
- [ ] `Zinc-Plating-Glance-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#F5F4F0` | Off-White | Background (Light) |
| `#E8A020` | Amber | Acid chloride column, accents |
| `#2EC4B6` | Teal | Alkaline NC column, callout borders |
| `#27AE60` | Emerald | RoHS "Yes," passivation note |
| `#E05C5C` | Coral | RoHS "No," common problems |
| `#3A4055` | Mid Slate | Parameter column, U-channel shapes |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout/panel fills |
| `#252B3D` | Alt Row | Alternating table rows |
| `#C8D0D8` | Bright Silver | Deposit layers |

---

*Originally engineered by Elara — Plating Posters Inc Prompt Architect*
*Poster #3 — Zinc Plating at a Glance — Claude Chat Generation Prompt v2.0*
*2026-04-04*
