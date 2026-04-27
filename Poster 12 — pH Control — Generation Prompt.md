---
Project: Plating Posters Inc
Poster Number: 12
Title: "The pH Control Poster"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 12 — pH Control — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - pHControl
  - v1
---

# Claude Chat Generation Prompt — Poster #12
## The pH Control Poster
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

This zone occupies the top 2.9 inches of the poster. Headline + subheading + tagline on the left (~55%) and a "Logarithmic Scale" callout box on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element:
2. Text content:
   `pH CONTROL`
3. With the text box selected, set these properties in the top toolbar:
   - **Font**: Click the font name dropdown and search for **Barlow Condensed**. Select **Barlow Condensed ExtraBold** (or "ExtraBold 800").
   - **Size**: Click the font size number and type `96`.
   - **Color**: Click the text color button (the "A" with a colored bar). Use hex `F0EDE8`. Press Enter.
   - **Letter spacing**: Click the three-dot menu (**...**) or the **Spacing** button in the toolbar. Find **Letter spacing** and set it to `-4` (negative four).
   - **Alignment**: Left-aligned.
4. Drag the text box so its left edge sits at the **0.5-inch** vertical guide and its top edge sits at the **0.5-inch** horizontal guide.
5. Set the text box width to approximately **12.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element:
2. Select all placeholder text and type:
   `The Number Every Bath Depends On`
3. Set these properties:
   - **Font**: Barlow SemiBold
   - **Size**: `40`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left-aligned
4. Position this text box so its left edge is at the 0.5-inch guide, top edge at approximately **1.6 inches** from the top.

### Step 8 — Place the tagline
1. Add a body text element:
2. Select all placeholder text and type:
   `Small numbers, big chemistry. Know your range.`
3. Set these properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: Set to **65%**.
   - **Alignment**: Left-aligned
4. Position: left edge at 0.5-inch guide, top edge at approximately **2.3 inches** from the top.

### Step 9 — Build "The Logarithmic Scale" callout box

**9a — Draw the callout box background:**
1. Add shape elements:
2. Search for **rectangle**. Find **Rounded Rectangle**. Click to place.
3. Set properties:
   - **Width**: `9.5` inches
   - **Height**: `2.2` inches
   - **Fill color**: `1E2435`
   - **Border**: 1.5 pt, color `2EC4B6` (Teal)
   - **Corner radius**: `8`
4. Position: right edge at the **23.5-inch** guide, top edge at **0.5 inches** from top.

**9b — Callout title:**
1. Add a text element. Type: `THE LOGARITHMIC SCALE`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6` (Teal)
3. Position: inside the container, top-left area, approximately 0.15 inches from the left edge and 0.15 inches from the top.

**9c — Callout body text:**
1. Add a text element. Copy-paste this exactly:
   `Each whole pH number = 10x change in H⁺ concentration. A bath at pH 4.0 has 10x more acid than pH 5.0, and 100x more than pH 6.0.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Line height: `1.4`
3. Position: inside the container, below the title, with 0.1 inches gap. Set text box width to fit within the container with 0.15 inches padding each side.

**9d — Formula:**
1. Add a text element. Type: `pH = -log[H⁺]`
2. Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally inside the container, below the body text.

**9e — Closing line:**
1. Add a text element. Type: `Small pH changes = big chemical changes.`
2. Font: Inter Medium, Size: `14`, Color: `2EC4B6` (Teal)
3. Position: centered inside the container, at the bottom with 0.1 inches padding.

**9f — Group the callout box:**
Select the rounded rectangle, all text elements inside it. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select the headline, subheading, tagline, and callout box group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: The pH Scale (Hero Visual)

This zone occupies Y: 2.9" to 14.4" (11.5 inches tall). It contains a section label, a vertical pH gradient scale on the left, and 13 horizontal process range bars extending to the right. This is the poster's primary visual.

**Build strategy:** First build all 15 gradient rectangles. Then add the pH number labels and axis line. Then build one process range bar as a template, duplicate 12 times, and modify each.

### Step 11 — Section label
1. Add a text element. Type: `OPERATING pH FOR EVERY MAJOR PROCESS`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, top edge at **3.0 inches**. Width: **23.0 inches**.

### Step 12 — Build the pH gradient scale

You will create 15 stacked rectangles forming a vertical color gradient from acidic (red/coral at top) through neutral (gray) to alkaline (teal at bottom).

**12a — Build pH 0 rectangle (topmost):**
1. Click **Elements** > search **rectangle** > select basic rectangle (sharp corners).
2. Set dimensions:
   - **Width**: `3.0` inches
   - **Height**: `0.70` inches
3. Set fill color: `E05C5C` (Coral). Leave at **100%** transparency (fully opaque).
4. Position: X: **0.5"**. Y: **3.7"**.

**12b — Duplicate for pH 1:**
1. Select the pH 0 rectangle. Press **Ctrl+D** to duplicate.
2. Drag the duplicate directly below pH 0 (Y: **4.4"**).
3. Change transparency to **80%** (the fill color stays `E05C5C`).

**12c — Continue duplicating for pH 2 through 14:**

Repeat the duplicate-and-reposition process for each pH value. Each rectangle is 0.70" tall and stacks directly below the previous one. Here are all 15 rectangles:

| pH | Y Position | Fill Color | Transparency |
|----|-----------|------------|-------------|
| 0 | 3.70" | `#E05C5C` Coral | 100% |
| 1 | 4.40" | `#E05C5C` Coral | 80% |
| 2 | 5.10" | `#E05C5C` Coral | 60% |
| 3 | 5.80" | `#E8A020` Amber | 60% |
| 4 | 6.50" | `#E8A020` Amber | 40% |
| 5 | 7.20" | `#E8A020` Amber | 25% |
| 6 | 7.90" | `#E8A020` Amber | 15% |
| 7 | 8.60" | `#3A4055` Mid Slate | 100% |
| 8 | 9.30" | `#2EC4B6` Teal | 15% |
| 9 | 10.00" | `#2EC4B6` Teal | 20% |
| 10 | 10.70" | `#2EC4B6` Teal | 30% |
| 11 | 11.40" | `#2EC4B6` Teal | 40% |
| 12 | 12.10" | `#2EC4B6` Teal | 60% |
| 13 | 12.80" | `#2EC4B6` Teal | 80% |
| 14 | 13.50" | `#2EC4B6` Teal | 100% |

**Tip:** To set transparency in the design, select the rectangle, then click the **transparency** button in the toolbar (checkerboard pattern icon). Set the value shown in the table above.

### Step 13 — Add pH number labels

Add a text element for each pH value (0 through 14), positioned on the left edge of each gradient rectangle.

1. Add a text element. Type: `0`
2. Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`
3. Position: inside the pH 0 rectangle, approximately X: **0.6"**, vertically centered within the rectangle.
4. Duplicate this text element 14 times. Reposition each one to the corresponding pH rectangle and change the text to `1`, `2`, `3`, ... `14`.

### Step 14 — Add the axis line
1. Click **Elements** > search **line**. Select a basic straight line.
2. Draw a vertical line from the top of the pH 0 rectangle to the bottom of the pH 14 rectangle.
   - Start: X: **3.5"**, Y: **3.7"**
   - End: X: **3.5"**, Y: **14.2"**
3. Set color: `3A4055` (Mid Slate), thickness: `2` pt.

### Step 15 — Add scale endpoint labels

**15a — Top label:**
1. Add a text element. Type: `STRONGLY ACIDIC`
2. Font: Barlow SemiBold, Size: `12`, Color: `E05C5C` (Coral)
3. Position: just above the pH 0 rectangle, X: **1.0"**, Y: **3.5"**.

**15b — Middle label (pH 7):**
1. Add a text element. Type: `NEUTRAL`
2. Font: Barlow SemiBold, Size: `14`, Color: `F0EDE8`
3. Position: centered on the pH 7 rectangle, to the right of the pH number.

**15c — Bottom label:**
1. Add a text element. Type: `STRONGLY ALKALINE`
2. Font: Barlow SemiBold, Size: `12`, Color: `2EC4B6` (Teal)
3. Position: just below the pH 14 rectangle.

### Step 16 — Build Process Range Bar 1 (Template): Hard Chrome

Each process range bar is a horizontal rounded rectangle positioned at the correct pH height, with a process name on the left end and a pH range on the right end.

**16a — Bar rectangle:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Set properties:
   - **Width**: `12.0` inches
   - **Height**: `0.50` inches
   - **Fill color**: `E05C5C` (Coral)
   - **Transparency**: `70%`
   - **Corner radius**: `4`
3. Position: X: **3.8"** (just right of the axis line). Y: **3.7"** (aligned with pH 0).

**16b — Process name label:**
1. Add a text element. Type: `Hard chrome`
2. Font: Inter Medium, Size: `14`, Color: `F0EDE8`
3. Position: inside the left end of the bar, approximately X: **4.0"**, vertically centered.

**16c — pH range label:**
1. Add a text element. Type: `<1.0`
2. Font: JetBrains Mono Regular, Size: `14`, Color: `F0EDE8`
3. Position: inside the right end of the bar.

**16d — Target line:**
1. Draw a short vertical line inside the bar at the target pH position.
2. Length: 0.50" (matching bar height). Stroke: `2` pt, `F0EDE8`.
3. Position: at the approximate pH target value within the bar.

**16e — Group the bar:**
Select the rounded rectangle, process name, pH range label, and target line. Press **Ctrl+G**.

### Step 17 — Duplicate and modify for remaining 12 process bars

Duplicate the Hard Chrome bar group 12 times. For each copy, reposition to the correct Y position, resize the width if needed, change the fill color, and update all text. Use the table below.

**Important:** Where bars overlap in pH space (e.g., Watts nickel and nickel sulfamate), offset the bars vertically by approximately 0.55 inches so they don't overlap visually. Some bars have shorter horizontal widths to prevent visual crowding.

| # | Process | pH Range | Bar Color | Y Position | Bar Width |
|---|---------|----------|-----------|-----------|-----------|
| 1 | Hard chrome | <1.0 | `#E05C5C` Coral | 3.70" | 12.0" |
| 2 | Matte tin | 0.5-2.0 | `#E05C5C` Coral | 4.05" | 12.0" |
| 3 | Hex passivation | 0.5-2.0 | `#E05C5C` Coral | 4.60" | 10.0" |
| 4 | Trivalent passivation | 1.5-2.5 | `#E8A020` Amber | 4.75" | 10.0" |
| 5 | Nickel sulfamate | 3.5-4.5 | `#E8A020` Amber | 6.15" | 10.0" |
| 6 | Watts nickel | 3.8-4.5 | `#E8A020` Amber | 6.70" | 12.0" |
| 7 | EN (Mid-P) | 4.5-5.2 | `#E8A020` Amber | 6.85" | 12.0" |
| 8 | Acid chloride zinc | 4.8-5.8 | `#27AE60` Emerald | 7.06" | 12.0" |
| 9 | Alkaline cleaners | 10-13 | `#2EC4B6` Teal | 10.70" | 14.0" |
| 10 | Cyanide copper strike | 11-13 | `#2EC4B6` Teal | 11.40" | 12.0" |
| 11 | Silver cyanide | 11.5-13 | `#2EC4B6` Teal | 11.75" | 10.0" |
| 12 | Alkaline CN zinc | 12-13.5 | `#2EC4B6` Teal | 12.10" | 10.0" |
| 13 | Alkaline NC zinc | 12.5-14 | `#2EC4B6` Teal | 12.45" | 12.0" |

For each bar:
1. Duplicate the template bar group.
2. Ungroup temporarily (**Ctrl+Shift+G**).
3. Resize the bar rectangle width per the table.
4. Change the fill color per the table. Keep transparency at **70%**.
5. Reposition to the Y value in the table. Keep X at **3.8"**.
6. Update the process name text and pH range text.
7. Reposition the target line to the approximate target pH within the bar.
8. Re-group (**Ctrl+G**).

**Note:** Bar 9 (Alkaline cleaners) is 14.0 inches wide — it extends further right than the others to visually emphasize the broad pH range of cleaners. Make sure it does not extend past the 23.5" right safe zone guide.

### Step 18 — Add EN annotation
1. Add a text element. Type: `EN: ±0.2 tolerance — check every 30-60 min`
2. Font: Inter Regular, Size: `11`, Color: `E8A020` (Amber)
3. Position: near the EN bar, slightly above or to the right of it.

### Step 19 — Add acid copper note
1. Add a text element. Type: `Acid copper is not pH-controlled — H₂SO₄ concentration is the control variable.`
2. Font: Inter Regular, Size: `12`, Color: `F0EDE8`, Transparency: **60%**
3. Position: at the bottom of the scale area, approximately Y: **14.0"**, X: **4.0"**.

### Step 20 — Group all of Zone 2
Select the section label, all 15 gradient rectangles, all pH labels, the axis line, endpoint labels, all 13 process bar groups, the EN annotation, and the acid copper note. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: What Happens When pH Drifts

This zone occupies Y: 14.4" to 21.6" (7.2 inches tall). Two side-by-side tables: "pH Too Low" on the left and "pH Too High" on the right.

### Step 21 — Block D: "pH Too Low" section title
1. Add a text element. Type: `pH TOO LOW — MORE ACIDIC THAN TARGET`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E05C5C` (Coral)
3. Position: X: **0.5"**, Y: **14.5"**.

### Step 22 — Block D: Table header row
**22a — Header background:**
1. Add a rectangle. Width: `10.5"`. Height: `0.5"`. Fill: `3A4055`. No border.
2. Position: X: **0.5"**, Y: **15.0"**.

**22b — Header text "PROCESS":**
1. Add text: `PROCESS`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.7"**, vertically centered in the header row. Width: `3.5"`.

**22c — Header text "EFFECT":**
1. Add text: `EFFECT`
2. Same font/size/color.
3. Position: X: **4.2"**. Width: `6.8"`.

### Step 23 — Block D: Build Row 1 (Template): Acid zinc

**23a — Row background:**
1. Add a rectangle. Width: `10.5"`. Height: `0.70"`. Fill: `1A1F2E` (base row). No border.
2. Position: X: **0.5"**, directly below header row (Y: **15.5"**).

**23b — Left accent bar:**
1. Add a narrow rectangle. Width: `0.06"`. Height: `0.70"`. Fill: `E05C5C` (Coral).
2. Position: flush against the left edge of the row (X: **0.5"**, Y: **15.5"**).

**23c — Process text:**
1. Add text: `Acid zinc`
2. Font: Inter Medium, Size: `15`, Color: `F0EDE8`
3. Position: X: **0.7"**, vertically centered in the row.

**23d — Effect text:**
1. Add text: `Excessive anode dissolution; zinc rises uncontrollably`
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`
3. Position: X: **4.2"**, vertically centered. Width: `6.8"`.

**23e — Group the row:**
Select row background, accent bar, and both text elements. Press **Ctrl+G**.

### Step 24 — Duplicate and modify for Rows 2-4

**Row 2 — Watts nickel:**
1. Duplicate Row 1. Reposition directly below (Y: **16.2"**).
2. Ungroup. Changes:
   - **Row background fill**: `252B3D` (Alt Row)
   - **Process**: `Watts nickel`
   - **Effect**: Copy-paste: `Increased H₂ evolution; pitting; embrittlement risk`
3. Re-group.

**Row 3 — EN (Mid-P):**
1. Duplicate Row 1. Reposition below Row 2 (Y: **16.9"**).
2. Ungroup. Changes:
   - **Row background fill**: `1A1F2E` (base)
   - **Process**: `EN (Mid-P)`
   - **Effect**: `Higher P content; slower deposition; stabilizer imbalance`
3. Re-group.

**Row 4 — Trivalent passivation:**
1. Duplicate Row 2. Reposition below Row 3 (Y: **17.6"**).
2. Ungroup. Changes:
   - **Row background fill**: `252B3D` (alt)
   - **Process**: `Trivalent passivation`
   - **Effect**: `Aggressive zinc attack; thinner film; etching`
3. Re-group.

### Step 25 — Block E: "pH Too High" section title
1. Add a text element. Type: `pH TOO HIGH — MORE ALKALINE THAN TARGET`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E8A020` (Amber)
3. Position: X: **12.0"**, Y: **14.5"**.

### Step 26 — Block E: Table header row
1. Add a rectangle. Width: `11.5"`. Height: `0.5"`. Fill: `3A4055`.
2. Position: X: **12.0"**, Y: **15.0"**.
3. Add header text: `PROCESS` (X: **12.2"**) and `EFFECT` (X: **15.7"**). Same font/size/color as Block D headers.

### Step 27 — Block E: Data rows

Build exactly like Block D rows, but positioned in the right column. Left accent bars use `E8A020` (Amber).

**Row 1 — Acid zinc** (Y: **15.5"**, base row):
- Process: `Acid zinc`
- Effect: Copy-paste: `Brightener precipitation; cloudy solution; Zn(OH)₂ at >6.5`

**Row 2 — Watts nickel** (Y: **16.2"**, alt row):
- Process: `Watts nickel`
- Effect: Copy-paste: `Ni(OH)₂ precipitation (green sludge); roughness`

**Row 3 — EN (Mid-P)** (Y: **16.9"**, base row):
- Process: `EN (Mid-P)`
- Effect: `Lower P content; faster rate; bath decomposition risk`

**Row 4 — Trivalent passivation** (Y: **17.6"**, alt row):
- Process: `Trivalent passivation`
- Effect: `Thicker film (intentional at 2.5 — Drew's note)`

### Step 28 — Group all of Zone 3
Select both section titles, both table header rows, and all 8 data row groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Adjustment + Measurement

This zone occupies Y: 21.6" to 28.8" (7.2 inches tall). Left 55%: adjustment chemicals table. Right 45%: pH measurement best practices callout.

### Step 29 — Block F: Section label
1. Add a text element. Type: `HOW TO ADJUST pH`
2. Font: Barlow Condensed ExtraBold, Size: `20`, Color: `F0EDE8`
3. Position: X: **0.5"**, Y: **21.7"**.

### Step 30 — Block F: Table header row

**30a — Header background:**
1. Add a rectangle. Width: `12.0"`. Height: `0.5"`. Fill: `3A4055`.
2. Position: X: **0.5"**, Y: **22.2"**.

**30b — Header texts:**
- `CHEMICAL` — Barlow SemiBold, `15` pt, `F0EDE8`, X: **0.7"**
- `FORMULA` — same, X: **3.7"**
- `DIRECTION` — same, X: **5.5"**
- `TYPICAL PROCESS` — same, X: **7.0"**

### Step 31 — Block F: Build Row 1 (Template): Sodium hydroxide

**31a — Row background:**
1. Add rectangle. Width: `12.0"`. Height: `0.65"`. Fill: `1A1F2E`. No border.
2. Position: X: **0.5"**, Y: **22.7"**.

**31b — Left accent bar:**
1. Add narrow rectangle. Width: `0.06"`. Height: `0.65"`. Fill: `27AE60` (Emerald — "Raise" row).
2. Position: flush left (X: **0.5"**, Y: **22.7"**).

**31c — Text columns:**
- Chemical: `Sodium hydroxide` — Inter Medium, `14` pt, `F0EDE8`, X: **0.7"**
- Formula: `NaOH` — JetBrains Mono Regular, `14` pt, `F0EDE8`, X: **3.7"**
- Direction: `Raise` — Inter Regular, `14` pt, `F0EDE8`, X: **5.5"**
- Typical Process: `Acid zinc, nickel, alkaline zinc` — Inter Regular, `14` pt, `F0EDE8`, X: **7.0"**

**31d — Group the row.**

### Step 32 — Duplicate and modify for Rows 2-7

**Row 2 — Potassium hydroxide** (Y: **23.35"**, alt `252B3D`, accent `27AE60` Emerald):
- Chemical: `Potassium hydroxide` | Formula: `KOH` | Direction: `Raise` | Process: `Silver baths; some alkaline zinc`

**Row 3 — Nickel carbonate** (Y: **24.0"**, base `1A1F2E`, accent `27AE60`):
- Chemical: `Nickel carbonate` | Formula: Copy-paste: `NiCO₃` | Direction: `Raise (Ni)` | Process: `Watts, sulfamate — preferred (adds Ni)`

**Row 4 — Ammonium hydroxide** (Y: **24.65"**, alt `252B3D`, accent `27AE60`):
- Chemical: `Ammonium hydroxide` | Formula: Copy-paste: `NH₄OH` | Direction: `Raise (EN)` | Process: `EN — avoids cation contamination`

**Row 5 — Sulfuric acid** (Y: **25.3"**, base `1A1F2E`, accent `E05C5C` Coral — "Lower" row):
- Chemical: `Sulfuric acid` | Formula: Copy-paste: `H₂SO₄` | Direction: `Lower` | Process: `Watts nickel, EN, acid copper`

**Row 6 — Hydrochloric acid** (Y: **25.95"**, alt `252B3D`, accent `E05C5C`):
- Chemical: `Hydrochloric acid` | Formula: `HCl` | Direction: `Lower` | Process: Copy-paste: `Acid zinc (also adds Cl⁻ — caution)`

**Row 7 — Sulfamic acid** (Y: **26.6"**, base `1A1F2E`, accent `E05C5C`):
- Chemical: `Sulfamic acid` | Formula: Copy-paste: `H₃NSO₃` | Direction: `Lower` | Process: Copy-paste: `Sulfamate nickel (avoids Cl⁻/SO₄²⁻)`

### Step 33 — Safety callout below table
1. Add a text element. Copy-paste:
   `Always add acid or base slowly, with mixing. Concentrated additions cause exothermic reactions and dangerous splashing.`
2. Font: Inter Medium, Size: `14`, Color: `E05C5C` (Coral)
3. Position: X: **0.5"**, Y: approximately **27.4"**.

### Step 34 — Block G: pH Measurement Best Practices callout

**34a — Callout container:**
1. Add a rounded rectangle. Width: `10.25"`. Height: `6.8"`. Fill: `1E2435`. Border: 1.5 pt, `27AE60` (Emerald). Corner radius: `8`.
2. Position: X: **13.25"**, Y: **21.7"**.

**34b — Callout title:**
1. Add text: `pH MEASUREMENT BEST PRACTICES`
2. Font: Barlow SemiBold, Size: `18`, Color: `27AE60` (Emerald)
3. Position: inside the container, top-left area with 16 pt padding.

**34c — Bullet list:**
1. Add a text element. Copy-paste all of this as one text block:
   ```
   - Calibrate with TWO buffers before every use
     (pH 4 + 7 for acid; pH 7 + 10 for alkaline)
   - Calibrate at operating temperature (or apply temp correction)
   - Store electrode in KCl storage solution — NEVER in DI water
   - Replace electrode annually (or when response slows)
   - Rinse with DI water between samples
   ```
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`, Line height: `1.5`
3. Position: inside container, below the title with 0.15 inches gap. Width: approximately 9.5 inches.

**34d — pH paper note:**
1. Add a text element. Copy-paste:
   `pH paper: ±0.5 accuracy — acceptable for cleaners and rinses. Not accurate enough for nickel, EN, or passivation (±0.2 required).`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`, Transparency: **60%**
3. Position: inside container, near the bottom with 0.15 inches padding.

### Step 35 — Group all of Zone 4
Select the section label, adjustment table (header + 7 rows), safety callout, and best practices callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Buffer Concept

This zone occupies Y: 28.8" to 32.4" (3.6 inches tall). A single full-width callout box with an embedded compact table.

### Step 36 — Buffer callout container
1. Add a rounded rectangle. Width: `23.0"`. Height: `3.2"`. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6` (Teal). Corner radius: `8`.
2. Position: X: **0.5"**, Y: **28.9"**.

### Step 37 — Buffer callout title
1. Add text. Copy-paste: `WHY YOUR BATH HAS BORIC ACID — THE BUFFER CONCEPT`
2. Font: Barlow SemiBold, Size: `20`, Color: `2EC4B6` (Teal)
3. Position: inside the container, top-left, 16 pt padding from edges.

### Step 38 — Buffer callout body text
1. Add a text element. Copy-paste:
   `Buffers resist pH change when acid or base is added. Boric acid — the most common buffer in electroplating — keeps nickel and zinc baths stable during plating, even as the cathode reaction produces H⁺. Without it, pH would swing wildly during operation.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Line height: `1.4`
3. Position: inside container, below the title, left side (about 12 inches wide). Leave room on the right for the table.

### Step 39 — Embedded buffer table (right side of callout)

**39a — Table header:**
1. Add a rectangle. Width: `8.0"`. Height: `0.35"`. Fill: `3A4055`.
2. Position: inside the callout, right-aligned, Y: approximately 0.4 inches below the title.
3. Add header texts: `BATH` (X: left of cell), `BUFFER` (center), `RANGE` (right) — Barlow SemiBold, `13` pt, `F0EDE8`.

**39b — Row 1:**
1. Add rectangle. Width: `8.0"`. Height: `0.40"`. Fill: `1A1F2E`. No border.
2. Position directly below header.
3. Text: `Watts nickel` | `Boric acid` | `pH 3.5-5.0`
4. Font: Inter Regular / JetBrains Mono (for buffer/range), Size: `14`, Color: `F0EDE8`.

**39c — Row 2:**
1. Duplicate Row 1. Reposition below. Change fill to `252B3D`.
2. Text: `Acid zinc` | `Boric acid` | `pH 4.5-6.0`

**39d — Row 3:**
1. Duplicate Row 1. Reposition below.
2. Text: `EN baths` | `Succinic/lactic acid` | `pH 4.0-5.5`

### Step 40 — Buffer closing line
1. Add text: `A well-buffered bath = stable pH = consistent deposits.`
2. Font: Inter Medium, Size: `15`, Color: `2EC4B6` (Teal)
3. Position: inside the callout, below the embedded table, with 0.1 inches gap.

### Step 41 — Group all of Zone 5
Select the callout container, title, body text, embedded table elements, and closing line. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

### Step 42 — Footer band background
1. Add a rectangle. Width: `24.0"`. Height: `3.6"`. Fill: `0D1020` (Deep Navy).
2. Position: X: **0"**, Y: **32.4"**.

### Step 43 — Disclaimer text
1. Add a text element. Copy-paste:
   `This poster presents industry-typical pH ranges and adjustment methods. Specific operating parameters vary by product formulation — always consult your product TDS. pH measurement instruments require regular calibration for accurate results.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: X: **0.5"**, Y: **32.6"**. Width: **23.0"**.

### Step 44 — Poster title
1. Add a text element. Type: `The pH Control Poster`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: **0.5"**, Y: **34.0"**.

### Step 45 — Series name
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, Y: **34.0"**.

### Step 46 — Logo placeholder
1. Add a small rounded rectangle. Width: `0.8"`. Height: `0.4"`. Fill: `3A4055`. No border.
2. Position: X: **22.6"**, Y: **33.8"**.
3. Add text inside: `[LOGO]` — JetBrains Mono Regular, `12` pt, `F0EDE8`, Transparency: **50%**, Alignment: Center.

### Step 47 — Version number
1. Add a text element. Type: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: **22.6"**, Y: **35.2"**.

### Step 48 — Group all of Zone 6
Select the Deep Navy rectangle, disclaimer, poster title, series name, logo placeholder, and version. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

Before exporting, unlock and ungroup all zones and verify each item. Re-group and re-lock after review.

### Text verification
- [ ] Headline reads: `pH CONTROL` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `The Number Every Bath Depends On` in Barlow SemiBold, `#E8A020`
- [ ] Tagline reads: `Small numbers, big chemistry. Know your range.` at 65% transparency
- [ ] Logarithmic Scale callout shows formula: `pH = -log[H⁺]` with Teal border
- [ ] Section label reads: `OPERATING pH FOR EVERY MAJOR PROCESS`
- [ ] 15 gradient rectangles are present (pH 0 through 14)
- [ ] 13 process range bars are present and positioned at correct pH heights
- [ ] EN annotation is present near the EN bar
- [ ] Acid copper note is present at bottom of scale
- [ ] Both drift tables have 4 data rows each
- [ ] Adjustment table has 7 rows with correct Emerald (Raise) and Coral (Lower) accents
- [ ] Best practices callout has 5 bullet points
- [ ] Buffer callout has embedded 3-row table
- [ ] All Unicode characters display correctly (H⁺, Zn(OH)₂, Ni(OH)₂, NiCO₃, NH₄OH, H₂SO₄, HCl, H₃NSO₃, Cl⁻, SO₄²⁻)
- [ ] Disclaimer, footer title, series name, LOGO placeholder, and version are all present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] All body text is `#F0EDE8` — not pure white
- [ ] pH gradient transitions from Coral (top) through Amber to Mid Slate (pH 7) to Teal (bottom)
- [ ] Process bars use correct accent colors at 70% opacity
- [ ] "Raise" rows have Emerald accent bars; "Lower" rows have Coral accent bars
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone
- [ ] pH gradient rectangles are flush (no visible gaps)
- [ ] Process bars start just right of the axis line
- [ ] No text is cut off or overlapping

### Readability check
- [ ] Zoom to 25% — headline and section labels readable
- [ ] Zoom to 50% — process names on bars readable
- [ ] Zoom to 75% — pH numbers and range values readable
- [ ] Zoom to 100% — callout body text and adjustment table readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 49 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2. Rename "Light Edition" if possible.

### Step 50 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 51 — Remap all elements

Work through this table top to bottom, zone by zone:

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | Logarithmic Scale callout, best practices callout, buffer callout | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | Even-numbered table data rows | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | Odd-numbered table data rows | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Subheading, Amber process bars, "pH Too High" title | `#E8A020` | `#C8860A` |
| **Teal elements** | Callout borders/titles, Teal process bars | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | Acid zinc bar, "Raise" accent bars, best practices border | `#27AE60` | `#1E7A47` |
| **Coral elements** | Strong acid bars, "Lower" accent bars, "pH Too Low" title, safety callout | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Scale axis, table header fills, dividers | `#3A4055` | `#D0D4DE` |

**pH scale gradient note:** The gradient rectangles use palette colors at reduced opacity. Remap the base colors (Coral, Amber, Teal) to their darkened equivalents and maintain the same opacity percentages. The gradient will appear as darkened accent colors on a light background — this actually produces a more vivid gradient effect.

**Process range bars:** Bars use accent colors at 70% opacity. After remap, verify bar text (`#1A1F2E` after remap) remains readable against each bar fill. If any bar color is too light, increase opacity to 80-85%.

### Step 52 — Post-remap adjustments
1. **Tagline at 65% opacity**: If too faint on `#F5F4F0`, increase to **75-80%**.
2. **Footnote/annotation text at 60% opacity**: If too faint, increase to **70-75%**.
3. **Disclaimer text at 50% opacity**: If too faint, increase to **65%**.
4. **pH number labels**: Verify they remain readable against the gradient rectangles in Light edition.
5. **Process bar labels**: Verify `#1A1F2E` text is readable on each remapped bar fill at 70% opacity.

### Post-remap verification checklist
- [ ] All body text passes WCAG AA (4.5:1 minimum) against its background
- [ ] pH scale gradient is visually coherent (acidic warm tones at top, alkaline cool tones at bottom)
- [ ] Process bar labels readable on all 13 bars
- [ ] All opacity-reduced text remains legible on the light background

---

## Phase 10 — Export Instructions

### Step 53 — Export the Dark edition (Page 1)

**53a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed** if available.
4. Select only **Page 1** (Dark edition).
5. Download and rename to: `pH Control — Dark — 24x36 — Print.pdf`

**53b — Digital PDF, 24x36":**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks.
2. Select Page 1. Rename to: `pH Control — Dark — Digital.pdf`

**53c — Print PDF, 18x24":**
1. 
2. Verify body text is at least 14 pt. Adjust if needed.
3. Export as PDF Print with crop marks and bleed.
4. Rename to: `pH Control — Dark — 18x24 — Print.pdf`

### Step 54 — Export the Light edition (Page 2)

Repeat Steps 53a, 53b, and 53c for Page 2 with these filenames:
- `pH Control — Light — 24x36 — Print.pdf`
- `pH Control — Light — Digital.pdf`
- `pH Control — Light — 18x24 — Print.pdf`

### Export file checklist
- [ ] `pH Control — Dark — 24x36 — Print.pdf`
- [ ] `pH Control — Dark — 18x24 — Print.pdf`
- [ ] `pH Control — Dark — Digital.pdf`
- [ ] `pH Control — Light — 24x36 — Print.pdf`
- [ ] `pH Control — Light — 18x24 — Print.pdf`
- [ ] `pH Control — Light — Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark), target lines |
| `#E8A020` | Amber | Subheading, mid-range acid process bars, "pH Too High" |
| `#2EC4B6` | Teal | Alkaline process bars, callout borders |
| `#27AE60` | Emerald | Acid zinc bar, "Raise" accent, best practices border |
| `#E05C5C` | Coral | Strong acid bars, "Lower" accent, "pH Too Low", safety callout |
| `#3A4055` | Mid Slate | Scale axis, table headers, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout box fills |
| `#252B3D` | Alt Row | Even-numbered table rows |
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
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0. Watson flags non-blocking (Drew items). |
