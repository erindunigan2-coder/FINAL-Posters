---
Project: Plating Posters Inc
Poster Number: 13
Title: "Barrel vs. Rack Plating — Choosing the Right Method"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 13 — Barrel vs Rack — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - BarrelPlating
  - RackPlating
  - v1
---

# Claude Chat Generation Prompt — Poster #13
## Barrel vs. Rack Plating — Choosing the Right Method
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

This zone occupies the top 2.9 inches. Full-width headline, subheading, and tagline.

### Step 6 — Place the headline
1. Add a heading text element: Type: `BARREL vs. RACK`
2. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `96`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at 0.5 inches. Width: `23.0"`.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Choosing the Right Plating Method`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `40`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.6 inches**.

### Step 8 — Place the tagline
1. Add a body text element: Type: `Not every part belongs in a barrel.`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: **65%**
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.3 inches**.

### Step 9 — Group all of Zone 1
Select headline, subheading, tagline. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Side-by-Side Illustration

This zone occupies Y: 2.9" to 11.5" (~8.6 inches tall). Left half: barrel cross-section. Right half: rack illustration. Center divider line.

### Step 10 — Section label
1. Add a text element. Type: `HOW EACH METHOD WORKS`
2. Font: Barlow Condensed ExtraBold, Size: `30`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, Y: **3.1"**. Width: **23.0"**.

### Step 11 — Left panel title: BARREL PLATING
1. Add a text element. Type: `BARREL PLATING`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `2EC4B6` (Teal), Alignment: Center
3. Position: centered within left panel (X center: ~6.0"). Y: **3.6"**.

### Step 12 — Build the barrel cross-section illustration

**12a — Barrel body (outer):**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Width: `7.0"`. Height: `4.0"`.
3. Fill: none (transparent). Border: 3 pt, `3A4055` (Mid Slate). Corner radius: `20`.
4. Position: X: **2.5"**, Y: **4.5"**.

**12b — Perforations (8-10 small circles):**
1. Click **Elements** > search **circle**. Place a small circle.
2. Diameter: `0.15"`. Fill: `1A1F2E` (matches background — "hole" effect). Border: 1 pt, `3A4055`.
3. Duplicate 7-9 times. Arrange in two horizontal rows across the barrel body:
   - Top row: Y: **5.0"**, spaced evenly across the barrel width.
   - Bottom row: Y: **7.5"**, same spacing.

**12c — Tumbling parts inside barrel:**
1. Add 6-8 small rounded rectangles in varying sizes (W: 0.4"-0.8", H: 0.3"-0.5").
2. Fill: `C8D0D8` (Bright Silver). No border.
3. Position: clustered in the bottom third of the barrel (Y: 7.0" to 8.0"). Rotate some slightly (10-20 degrees) to suggest tumbling.

**12d — Rotation arrow:**
1. Click **Elements** > search **curved arrow**. Place outside the barrel on the right side.
2. Stroke: 2 pt, `2EC4B6` (Teal). Arrowhead: pointing clockwise (downward).
3. Position: X: **9.8"**, spanning Y: 5.5" to 7.5" along the barrel's right edge.

**12e — Cathode buttons:**
1. Add 3 small circles, diameter `0.2"`. Fill: `2EC4B6` (Teal).
2. Position: along the interior bottom of the barrel: X: **4.0"**, **5.5"**, **7.0"**; Y: **8.0"**.

**12f — Solution flow arrows (optional):**
1. Add 3-4 short lines passing through the perforations.
2. Stroke: 1 pt, `F0EDE8` at 30% opacity. Small arrowheads.

**12g — Cathode contact label:**
1. Add text: `Cathode contact`
2. Font: JetBrains Mono Regular, Size: `12`, Color: `2EC4B6`
3. Draw a short line (1 pt, `2EC4B6`) from label to one cathode button.

### Step 13 — Left panel sub-labels
Add three text boxes below the barrel illustration, centered under it:

1. `6-8 RPM rotation` — Y: **9.0"**
2. `Parts tumble through current field` — Y: **9.4"**
3. `Intermittent electrical contact` — Y: **9.8"**

All: JetBrains Mono Regular, Size: `14`, Color: `F0EDE8`, Alignment: Center.

### Step 14 — Center divider
1. Add a straight vertical line.
2. Start: X: **12.0"**, Y: **3.8"**. End: X: **12.0"**, Y: **10.8"**.
3. Stroke: 2 pt, `3A4055` (Mid Slate).

### Step 15 — Right panel title: RACK PLATING
1. Add text: `RACK PLATING`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `E8A020` (Amber), Alignment: Center
3. Position: centered within right panel (X center: ~18.0"). Y: **3.6"**.

### Step 16 — Build the rack illustration

**16a — Power bus bar:**
1. Add a rectangle. Width: `8.0"`. Height: `0.25"`. Fill: `3A4055`.
2. Position: X: **14.0"**, Y: **4.5"**.

**16b — Rack spine (vertical):**
1. Add rectangle. Width: `0.2"`. Height: `3.5"`. Fill: `3A4055`.
2. Position: X: **17.75"**, Y: **4.75"**.

**16c — Crossbars (3 horizontal):**
1. Add 3 rectangles. Each: Width: `4.0"`, Height: `0.12"`. Fill: `3A4055`.
2. Position: centered on spine (X: **15.85"**), at Y: **5.5"**, **6.5"**, **7.5"**.

**16d — Hanging parts (4 rectangles):**
1. Add 4 rectangles. Each: Width: `0.8"`, Height: `1.8"`. Fill: `C8D0D8` (Bright Silver).
2. Position: 2 on top crossbar (X: **16.2"** and **17.6"**, Y: **5.7"**), 2 on middle crossbar (same X, Y: **6.7"**).
3. Connect to crossbars with small hook lines: short curved lines (0.15" tall), 1 pt, `3A4055`.

**16e — Anodes (2 flanking rectangles):**
1. Add 2 rectangles. Each: Width: `0.5"`, Height: `3.0"`. Fill: none. Border: 2 pt, `E8A020` (Amber).
2. Position: X: **14.5"** and **21.0"**, Y: **5.0"**.

**16f — Anode labels:**
1. Add 2 text elements: `Anode`
2. Font: JetBrains Mono Regular, Size: `12`, Color: `E8A020`
3. Position: centered below each anode rectangle.

**16g — Current arrows:**
1. Add 2 lines with arrowheads, from bus bar down toward rack.
2. Stroke: 1.5 pt, `E8A020`. Arrowheads pointing down.

### Step 17 — Right panel sub-labels
Three text boxes below the rack, centered:

1. `Continuous direct contact` — Y: **9.0"**
2. `Parts fixed in position` — Y: **9.4"**
3. `Full current exposure — 100% of cycle` — Y: **9.8"**

All: JetBrains Mono Regular, Size: `14`, Color: `F0EDE8`, Alignment: Center.

### Step 18 — Group all of Zone 2
Select the section label, all barrel elements, center divider, all rack elements, and all sub-labels. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Head-to-Head Comparison Table (Hero)

This zone occupies Y: 11.5" to 25.2" (~13.7 inches tall). Full-width, 3-column, 10-row comparison matrix.

### Step 19 — Section label
1. Add text: `HEAD-TO-HEAD COMPARISON`
2. Font: Barlow Condensed ExtraBold, Size: `32`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, Y: **11.7"**.

### Step 20 — Column header row

**20a — Header background:**
1. Add a rectangle. Width: `23.0"`. Height: `0.55"`. Fill: `3A4055`.
2. Position: X: **0.5"**, Y: **12.3"**.

**20b — Header texts:**
- `FACTOR` — Barlow SemiBold, `22` pt, `F0EDE8`, X: **0.7"**
- `BARREL` — Barlow SemiBold, `22` pt, `2EC4B6` (Teal), X: **7.7"**
- `RACK` — Barlow SemiBold, `22` pt, `E8A020` (Amber), X: **15.7"**

### Step 21 — Build Row 1 (Template): Part Size

**21a — Row background:**
1. Add rectangle. Width: `23.0"`. Height: `1.1"`. Fill: `1A1F2E` (base row). No border.
2. Position: X: **0.5"**, Y: **12.85"**.

**21b — Factor text:**
1. Add text: `Part size`
2. Font: Inter Medium, Size: `18`, Color: `F0EDE8`
3. Position: X: **0.7"**, vertically centered. Width: `6.8"`.

**21c — Barrel text:**
1. Add text: `Small — typically < 6-8" longest dimension; < 1-2 lbs per part`
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`
3. Position: X: **7.7"**, vertically centered. Width: `7.8"`.

**21d — Rack text:**
1. Add text: `No practical upper limit — limited by tank size and rack capacity`
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`
3. Position: X: **15.7"**, vertically centered. Width: `7.8"`.

**21e — Group the row.**

### Step 22 — Duplicate and modify for Rows 2-10

Duplicate the Row 1 group for each remaining row. Alternate backgrounds between `1A1F2E` (odd) and `252B3D` (even). Row height ~1.1" each. Reposition each row flush below the previous one.

**Row 2 — Part geometry** (even `252B3D`):
- Factor: `Part geometry`
- Barrel: `Must tumble freely; no nesting, tangling, or fragile features`
- Rack: `Any geometry — complex, delicate, or asymmetric parts accommodated`

**Row 3 — Volume** (odd `1A1F2E`):
- Factor: `Volume`
- Barrel: `High volume — hundreds to thousands of parts per load`
- Rack: `Low to medium volume — parts individually fixtured`

**Row 4 — Electrical contact** (even `252B3D`):
- Factor: `Electrical contact`
- Barrel: `Intermittent — parts tumble against cathode buttons (~30-50% of cycle)`
- Rack: `Continuous — direct fixture-to-part contact (100% of cycle)`

**Row 5 — Current density** (odd `1A1F2E`):
- Factor: `Current density`
- Barrel: `Lower CD required (e.g., zinc: 5-10 ASF barrel vs. 15-20 ASF rack)`
- Rack: `Higher CD achievable — uniform current distribution`

**Row 6 — Deposit uniformity** (even `252B3D`):
- Factor: `Deposit uniformity`
- Barrel: `Less uniform — contact points get heavier deposit; recesses may plate thin`
- Rack: `More uniform — part position controls thickness distribution`

**Row 7 — Throwing power** (odd `1A1F2E`):
- Factor: `Throwing power`
- Barrel: `Higher throwing power required — current must reach buried parts`
- Rack: `Moderate — anode-to-cathode geometry can be optimized`

**Row 8 — Throughput** (even `252B3D`):
- Factor: `Throughput (cost/part)`
- Barrel: `Lower cost per part at high volume — labor is loading/unloading only`
- Rack: `Higher cost per part — individual fixturing is labor-intensive`

**Row 9 — Surface finish risk** (odd `1A1F2E`):
- Factor: `Surface finish risk`
- Barrel: `Part-to-part contact causes dings, scratches — not for cosmetic surfaces`
- Rack: `No part-to-part contact — suitable for cosmetic and decorative finishes`

**Row 10 — Plating time** (even `252B3D`):
- Factor: `Plating time`
- Barrel: `Longer — intermittent contact means effective plating time is 30-50% of total`
- Rack: `Shorter — full current exposure for the entire cycle`

**Row height note:** If any row's text wraps to more than 2 lines, increase that row's background rectangle height. Make sure the Factor, Barrel, and Rack text boxes are vertically centered within the row.

### Step 23 — Table footnote
1. Add a text element below the last row. Copy-paste:
   `CD ranges shown are representative for acid zinc plating (Drew's Quick Reference). Actual ranges vary by process — see Poster #11 Current Density Quick Reference for full process-specific CD data.`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`, Transparency: **60%**
3. Apply italic if possible; otherwise leave as regular.
4. Position: X: **0.5"**, approximately 0.1 inches below the last row. Width: `23.0"`.

### Step 24 — Group all of Zone 3
Select section label, header row, all 10 data row groups, and footnote. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Decision Guide

This zone occupies Y: 25.2" to 32.4" (~7.2 inches tall). Section label, two "Wins When" callout columns, and a decision flowchart strip.

### Step 25 — Section label
1. Add text: `WHEN TO CHOOSE`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, Y: **25.4"**.

### Step 26 — "Barrel Wins When..." callout (left column)

**26a — Callout container:**
1. Add a rounded rectangle. Width: `11.2"`. Height: `3.5"`. Fill: `1E2435`. No border. Corner radius: `6`.
2. Position: X: **0.5"**, Y: **26.0"**.

**26b — Left accent bar:**
1. Add narrow rectangle. Width: `0.06"`. Height: `3.5"`. Fill: `2EC4B6` (Teal).
2. Position: X: **0.5"**, Y: **26.0"** (flush left).

**26c — Title:**
1. Add text: `BARREL WINS WHEN...`
2. Font: Barlow SemiBold, Size: `22`, Color: `2EC4B6` (Teal)
3. Position: X: **0.8"**, Y: **26.2"**.

**26d — Bullet list:**
1. Add text element. Copy-paste:
   ```
   - Parts are small, durable, and can tumble freely
   - Volume is high and cost per part must be low
   - Cosmetic finish is not critical
   - Parts do not nest or tangle
   - Throwing power of the bath chemistry is adequate
   ```
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`, Line height: `1.5`
3. Position: X: **0.8"**, Y: **26.7"**. Width: `10.6"`.

### Step 27 — "Rack Wins When..." callout (right column)

**27a — Callout container:**
1. Rounded rectangle. Width: `11.5"`. Height: `3.5"`. Fill: `1E2435`. No border. Corner radius: `6`.
2. Position: X: **12.0"**, Y: **26.0"**.

**27b — Left accent bar:**
1. Width: `0.06"`. Height: `3.5"`. Fill: `E8A020` (Amber).
2. Position: X: **12.0"**, Y: **26.0"**.

**27c — Title:**
1. Add text: `RACK WINS WHEN...`
2. Font: Barlow SemiBold, Size: `22`, Color: `E8A020` (Amber)
3. Position: X: **12.3"**, Y: **26.2"**.

**27d — Bullet list:**
1. Copy-paste:
   ```
   - Parts are large, fragile, or have complex geometry
   - Deposit uniformity or thickness control is critical
   - Surface finish is cosmetic or decorative
   - Volume is low to medium (custom or job-shop work)
   - Specifications require measurable thickness at specific locations
   ```
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`, Line height: `1.5`
3. Position: X: **12.3"**, Y: **26.7"**. Width: `10.9"`.

### Step 28 — Decision flowchart strip

**28a — Strip background:**
1. Add rounded rectangle. Width: `23.0"`. Height: `2.0"`. Fill: `1E2435`. Corner radius: `8`.
2. Position: X: **0.5"**, Y: **30.0"**.

**28b — Build Decision Box 1 — Part Size:**
1. Add a rounded rectangle. Width: `5.0"`. Height: `1.5"`. Fill: `252B3D`. Border: 1 pt, `3A4055`. Corner radius: `6`.
2. Position: X: **0.75"**, Y: **30.25"**.

3. Add question text: `Small and durable?`
   Font: Inter Medium, Size: `16`, Color: `F0EDE8`. Position: centered in upper half.

4. Add answer text — two lines:
   Line 1: `YES` in `2EC4B6` (Teal) followed by ` → Barrel` in `F0EDE8`
   Line 2: `NO` in `E8A020` (Amber) followed by ` → Rack` in `F0EDE8`
   Font: JetBrains Mono Regular, Size: `14`. Position: centered in lower half.

**28c — Duplicate for Box 2 — Volume:**
1. Duplicate Box 1. Reposition: X: **6.25"**, Y: **30.25"**.
2. Change question to: `High volume?`
3. Answers same: `YES → Barrel` / `NO → Rack`

**28d — Duplicate for Box 3 — Cosmetic:**
1. Duplicate. Reposition: X: **11.75"**, Y: **30.25"**.
2. Question: `Cosmetic finish required?`
3. **Note — answers reversed:** `YES` in `E8A020` (Amber) + ` → Rack` / `NO` in `2EC4B6` (Teal) + ` → Barrel`

**28e — Duplicate for Box 4 — Thickness Spec:**
1. Duplicate. Reposition: X: **17.25"**, Y: **30.25"**.
2. Question: `Tight thickness spec?`
3. Answers: `YES → Rack` / `NO → Either` (both "NO" and "Either" in `F0EDE8`)

**28f — Arrow connectors:**
1. Add 3 horizontal lines with arrowheads connecting the boxes:
   - Box 1 right edge to Box 2 left edge
   - Box 2 to Box 3
   - Box 3 to Box 4
2. Stroke: 2 pt, `3A4055`. Arrowheads pointing right.
3. Y position: centered in the strip (~Y: **31.0"**).

### Step 29 — Group all of Zone 4
Select section label, both "Wins When" callout groups, strip background, all 4 decision boxes, and all 3 arrows. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Footer Band

### Step 30 — Footer band background
1. Add rectangle. Width: `24.0"`. Height: `3.6"`. Fill: `0D1020` (Deep Navy).
2. Position: X: **0"**, Y: **32.4"**.

### Step 31 — Disclaimer
1. Add text. Copy-paste:
   `This poster is a decision reference tool. Process selection depends on specific part geometry, specification requirements, and bath chemistry. Consult your process supplier for application-specific guidance.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: X: **0.5"**, Y: **32.7"**. Width: `23.0"`.

### Step 32 — Poster title
1. Add text: `Barrel vs. Rack Plating — Choosing the Right Method`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.5"**, Y: **33.5"**.

### Step 33 — Series name
1. Add text: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, Y: **34.2"**.

### Step 34 — Logo placeholder
1. Add rounded rectangle. Width: `0.83"`. Height: `0.42"`. Fill: `3A4055`. No border.
2. Position: X: **22.5"**, Y: **33.3"**.
3. Add text: `[LOGO]` — JetBrains Mono Regular, `10` pt, `F0EDE8`, Transparency: **50%**.

### Step 35 — Version number
1. Add text: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: **0.5"**, Y: **35.0"**.

### Step 36 — Group all of Zone 5
Select footer rectangle, disclaimer, poster title, series name, logo placeholder, version. Press **Ctrl+G**.

---

## Phase 7 — Final Review Checklist

### Text verification
- [ ] Headline reads: `BARREL vs. RACK` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Choosing the Right Plating Method` in Barlow SemiBold, `#E8A020`
- [ ] Tagline at 65% transparency
- [ ] Section labels: `HOW EACH METHOD WORKS`, `HEAD-TO-HEAD COMPARISON`, `WHEN TO CHOOSE`
- [ ] `BARREL PLATING` title in Teal, `RACK PLATING` title in Amber
- [ ] Column headers: `FACTOR`, `BARREL` (Teal), `RACK` (Amber)
- [ ] 10 data rows present (Part size through Plating time)
- [ ] Table footnote references Poster #11
- [ ] Barrel Wins: 5 bullet points. Rack Wins: 5 bullet points.
- [ ] Decision strip: 4 boxes connected by 3 arrows
- [ ] Box 3 answers reversed (YES → Rack, NO → Barrel)
- [ ] Disclaimer, footer title, series name, LOGO, version present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] Barrel elements use Teal (`#2EC4B6`)
- [ ] Rack elements use Amber (`#E8A020`)
- [ ] Parts in illustrations are Bright Silver (`#C8D0D8`)
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] Barrel and rack illustrations are balanced (left and right halves)
- [ ] Center divider is at 12.0 inches
- [ ] All text within 0.5-inch safe zone
- [ ] Table rows flush with no gaps

### Readability check
- [ ] Zoom to 25% — headline, section labels, illustration titles readable
- [ ] Zoom to 50% — table factor column and illustration sub-labels readable
- [ ] Zoom to 100% — all body text, decision box answers readable

---

## Phase 8 — Light Edition: Remap Instructions

### Step 37 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2.

### Step 38 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 39 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Callout fills** | `#1E2435` | `#ECEEF4` |
| **Alt row / decision boxes** | `#252B3D` | `#E8E8F0` |
| **Base rows** | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |
| **Bright Silver** | `#C8D0D8` | `#C8D0D8` — **unchanged** |

### Step 40 — Post-remap adjustments
1. **Tagline at 65%**: If too faint on light background, increase to **75-80%**.
2. **Footnote at 60%**: If too faint, increase to **70-75%**.
3. **Disclaimer at 50%**: If too faint, increase to **65%**.
4. **Silver parts (`#C8D0D8`)**: Verify they still read against `#F5F4F0`. They should — tested on Poster #4.
5. **Barrel perforations**: The "holes" used `#1A1F2E` fill to match dark background. Change to `#F5F4F0` to match light background.

---

## Phase 9 — Export Instructions

### Step 41 — Export Dark edition (Page 1)

**41a — Print PDF, 24x36":**
1. **Share** > **Download** > **PDF Print**. Check **Crop marks and bleed**. Select Page 1.
2. Rename: `Barrel vs Rack — Dark — 24x36 — Print.pdf`

**41b — Digital PDF:**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks. Page 1.
2. Rename: `Barrel vs Rack — Dark — Digital.pdf`

**41c — Print PDF, 18x24":**
1. **Resize** > **18 x 24 inches** > **Copy & resize**. Verify 14 pt minimum. Export PDF Print.
2. Rename: `Barrel vs Rack — Dark — 18x24 — Print.pdf`

### Step 42 — Export Light edition (Page 2)

Repeat with these filenames:
- `Barrel vs Rack — Light — 24x36 — Print.pdf`
- `Barrel vs Rack — Light — Digital.pdf`
- `Barrel vs Rack — Light — 18x24 — Print.pdf`

### Export file checklist
- [ ] `Barrel vs Rack — Dark — 24x36 — Print.pdf`
- [ ] `Barrel vs Rack — Dark — 18x24 — Print.pdf`
- [ ] `Barrel vs Rack — Dark — Digital.pdf`
- [ ] `Barrel vs Rack — Light — 24x36 — Print.pdf`
- [ ] `Barrel vs Rack — Light — 18x24 — Print.pdf`
- [ ] `Barrel vs Rack — Light — Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | Rack accent, section titles |
| `#2EC4B6` | Teal | Barrel accent, callout borders |
| `#27AE60` | Emerald | Reserve |
| `#E05C5C` | Coral | Reserve |
| `#3A4055` | Mid Slate | Table headers, illustration outlines, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout fills, decision strip |
| `#252B3D` | Alt Row | Even table rows, decision boxes |
| `#C8D0D8` | Bright Silver | Illustrated parts (both editions) |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Callout fills (Light edition) |
| `#E8E8F0` | Alt Row Light | Even rows (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#D0D4DE` | Light Slate | Rules/dividers (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0. One Watson flag open (barrel weight/size limits) — non-blocking. |
