---
Project: Plating Posters Inc
Poster Number: 4
Title: Reading Your Hull Cell Panel — Acid Zinc Edition
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-03T00:00:00
Source: Poster 4 — Hull Cell Panel — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - HullCell
  - AcidZinc
  - v1
---

# Claude Chat Generation Prompt — Poster #4
## Reading Your Hull Cell Panel — Acid Zinc Edition
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

This zone occupies the top 2.9 inches of the poster. It contains the headline (left side) and an orientation callout box (right side).

### Step 6 — Place the headline
1. Add a heading text element:
2. Text content:
   `READING YOUR HULL CELL PANEL`
3. With the text box selected, set these properties in the top toolbar:
   - **Font**: Click the font name dropdown and search for **Barlow Condensed**. Select **Barlow Condensed ExtraBold** (or "ExtraBold 800").
   - **Size**: Click the font size number and type `96`. (If the text overflows past the 13.8-inch vertical guide — roughly the left 58% of the page — reduce to `80`.)
   - **Color**: Click the text color button (the "A" with a colored bar). Use hex `F0EDE8`. Press Enter.
   - **Letter spacing**: Click the three-dot menu (**...**) or the **Spacing** button in the toolbar. Find **Letter spacing** and set it to `-4` (negative four). This tightens the letters together for a more industrial look.
   - **Alignment**: Left-aligned (click the left-align button if it is not already selected).
4. Drag the text box so its left edge sits at the **0.5-inch** vertical guide and it is vertically centered within the header band (roughly at 1.0-1.2 inches from the top).

### Step 7 — Place the subheading
1. Add a subheading text element:
2. Select all placeholder text and type:
   `Diagnose your plating bath before it diagnoses your scrap rate.`
3. Set these properties:
   - **Font**: Barlow SemiBold (search for "Barlow" — select the SemiBold weight, not Condensed)
   - **Size**: `42`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left-aligned
4. Position this text box directly below the headline, left edge at the 0.5-inch guide, with a small gap (about 0.1 inches) between the bottom of the headline and the top of this line.

### Step 8 — Build the "What Is a Hull Cell?" callout box

**8a — Draw the box background:**
1. Add shape elements:
2. 
3. Use a **Rounded Rectangle** shape. 
4. With the rectangle selected, set these properties:
   - **Width**: `9.1` inches (type this in the Width field — look for "W" in the position/size toolbar, which appears when you click the element; you may need to click the position icon or right-click > "Show position")
   - **Height**: `1.7` inches
   - **Fill color**:  Type hex `1E2435`.
   - **Border**: Click the **Border** button in the toolbar (it may look like a square outline icon). Set border weight to `1.5` pt. Set border color to `2EC4B6` (Teal).
   - **Corner radius**: If visible in the shape controls, set to approximately `8`. Use rounded corners.
5. Position the rectangle so its right edge aligns with the **23.5-inch** vertical guide (0.5 inches from the right edge of the page) and it is vertically centered in the header band (roughly 0.6 inches from the top).

**8b — Add the callout title:**
1. Add a subheading text element:
2. Type: `WHAT IS A HULL CELL?`
3. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `24`
   - **Color**: `2EC4B6` (Teal)
4. Position this text box inside the rounded rectangle, near the top-left corner, with about 0.15 inches of padding from the top and left edges of the box.

**8c — Add the callout body text:**
1. Add a body text element:
2. Select all placeholder text and type (or paste) exactly:
   `The Hull cell is a 267 mL trapezoidal tank that simultaneously tests a range of current densities on a single cathode panel. The angled cathode creates a current density gradient — high at one end, low at the other — so one 5-minute test reveals how your bath performs across its entire operating range.`
3. Set properties:
   - **Font**: Inter Regular
   - **Size**: `18`
   - **Color**: `F0EDE8` (Warm White)
   - **Line spacing**: Click **Spacing** > set line height to `1.4`
4. Position inside the box, below the title, with 0.1 inches between the title and this text. Set the text box width so it fits within the rounded rectangle with 0.15 inches padding on each side.

**8d — Add the separator line:**
1. Add shape elements: Search for **line**.
2. Select a basic straight line and place it inside the callout box, horizontally, below the body text.
3. Set the line color to `3A4055` (Mid Slate) and the thickness to `0.5` pt.
4. Stretch the line to match the width of the body text above it.

**8e — Add the closing punch line:**
1. Add a body text element:
2. Type: `One panel. One test. Every zone, all at once.`
3. Set properties:
   - **Font**: Inter Medium (or Inter SemiBold if Medium is not available)
   - **Size**: `18`
   - **Color**: `F0EDE8`
4. Position below the separator line, inside the callout box, with 0.05 inches gap.

**8f — Group the callout box:**
Select the rounded rectangle, the title, the body text, the separator line, and the punch line. Press **Ctrl+G** (or Cmd+G) to group them.

### Step 9 — Optional: Header band bottom rule
1. Draw a straight horizontal line across the full page width at the 2.9-inch guide position.
2. Set color to `3A4055` (Mid Slate), thickness `1` pt.
3. This visually separates the header from the illustration below. If it looks too busy, delete it — it is optional.

### Step 10 — Group all of Zone 1
Select everything in the header band (headline, subheading, callout group, optional rule). Press **Ctrl+G** to group.

---

## Phase 3 — Zone 2: Hull Cell Panel Illustration

This is the most visually complex zone. Build it piece by piece. It occupies roughly 2.9 inches to 13.3 inches from the top (about 10.4 inches tall).

**Important: Build the panel and its labels as standalone elements first, then position the group.**

### Step 11 — Panel body rectangle
1. Click **Elements** > search **rectangle** > select a basic rectangle (sharp corners, not rounded).
2. Set dimensions:
   - **Width**: `23` inches (page width minus 1 inch for margins)
   - **Height**: `6.5` inches
3. Set the fill to a **gradient**:
   - 
   - At the top of the color picker, you will see options for "Solid" and "Gradient." Click **Gradient**.
   - The gradient should have a bar with two color stops (circles on the bar).
   - Click the **left stop** (circle). Set its color to `D8E0E8`.
   - Click the **right stop** (circle). Set its color to `B8C0C8`.
   - Make sure the gradient direction is **horizontal** (left to right). If the gradient runs top-to-bottom, click the rotate button on the gradient controls (or drag the angle handle) until it runs left to right.
4. Add a border:
   - Click the **Border** button. Set weight to `2` pt. Set color to `9AA0B0` (Panel Edge).
5. Position: center it horizontally on the page (left edge at the 0.5-inch guide). Place the top edge at about **3.2 inches** from the top of the page (leaving a 0.3-inch gap below the header band).

The result should look like a wide, shallow, metallic-silver rectangle — brighter on the left, slightly darker on the right. This represents a healthy zinc deposit on a Hull cell panel.

### Step 12 — HCD zone band overlay (left side amber glow)
1. Add another rectangle (sharp corners).
2. Set dimensions:
   - **Width**: `7.7` inches (one-third of the panel width)
   - **Height**: `0.75` inches
3. Set the fill to a **gradient**:
   - Left stop: color `E8A020`, **opacity 70%** (after selecting the color, look for a transparency/opacity slider — set it to 70).
   - Right stop: color `E8A020`, **opacity 0%** (fully transparent — set opacity to 0).
   - Direction: horizontal, left to right.
4. Remove any border (set border to none or 0 pt).
5. Position: place this rectangle so its **left edge** is flush with the left edge of the panel body rectangle, and its **top edge** is flush with the top edge of the panel body rectangle.

This creates an amber glow fading in from the left edge of the panel — the high-current-density zone indicator.

### Step 13 — LCD zone band overlay (right side teal glow)
1. Add another rectangle.
2. Set dimensions:
   - **Width**: `7.7` inches
   - **Height**: `0.75` inches
3. Set the fill to a gradient:
   - Left stop: color `2EC4B6`, **opacity 0%** (fully transparent).
   - Right stop: color `2EC4B6`, **opacity 70%**.
   - Direction: horizontal, left to right.
4. No border.
5. Position: place so its **right edge** is flush with the right edge of the panel body rectangle, and its **top edge** is flush with the top edge of the panel body rectangle.

This creates a teal glow fading in from the right edge — the low-current-density zone indicator. Together with Step 12, the top edge of the panel now shows amber on the left, silver in the center, and teal on the right.

### Step 14 — Zone labels (below the panel)

Place three text groups below the panel, centered under each third of the panel width. Leave about 0.1 inches between the bottom edge of the panel and the top of these labels.

**14a — HCD Zone label (left third):**
1. Add a text element. Type: `HIGH CURRENT DENSITY`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `E8A020` (Amber)
3. Center this text under the left third of the panel (roughly centered at 4.3 inches from the left edge of the page).

**14b — HCD sub-label:**
1. Add a text element. Type: `~10-50 A/dm` then add the superscript: type `2` and Use Unicode superscript if available, otherwise render as: `~10-50 A/dm2 at 2 A`
   - Ideal text if you can paste Unicode: `~10–50 A/dm² at 2 A`
2. Font: JetBrains Mono Regular (or Courier Prime), Size: `16`, Color: `F0EDE8`
3. Position directly below the HCD zone label, centered to match.

**14c — Mid-Current Zone label (center):**
1. Add a text element. Type: `MID-CURRENT`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `F0EDE8` (Warm White)
3. Center under the middle third of the panel.

**14d — Mid-Current sub-label:**
1. Add a text element. Type: `~2–10 A/dm² at 2 A`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`
3. Position directly below the Mid-Current label.

**14e — LCD Zone label (right third):**
1. Add a text element. Type: `LOW CURRENT DENSITY`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `2EC4B6` (Teal)
3. Center under the right third of the panel.

**14f — LCD sub-label:**
1. Add a text element. Type: `~0.1–1 A/dm² at 2 A`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `F0EDE8`
3. Position directly below the LCD label.

### Step 15 — Callout arrows
1. In the left sidebar, click **Elements** > search **line**.
2. Select a line with an arrowhead (look for a line style with an arrow at one end).
3. Draw three vertical lines, each dropping from the bottom edge of the panel rectangle down toward where the diagnostic table will sit:
   - **Arrow 1**: starts at the bottom-center of the left third of the panel, extends downward about 0.5 inches.
   - **Arrow 2**: starts at the bottom-center of the middle third, extends downward about 0.5 inches.
   - **Arrow 3**: starts at the bottom-center of the right third, extends downward about 0.5 inches.
4. For each arrow line:
   - Color: `3A4055` (Mid Slate)
   - Thickness: `1.5` pt
   - The arrowhead should be at the **bottom** (pointing down). If it defaults to the top, look for a "flip" option or swap the start and end arrowhead settings.

These are subtle navigation lines — they guide the eye from the diagram to the table. They should be visible but not bold.

### Step 16 — Diagram caption
1. Add a text element. Type (or paste):
   `Current density values per Wagner scale. Left (narrow end) = high current density. Right (wide end) = low current density.`
   Then press Enter and type the second line:
   `Acid zinc KCl/NH₄Cl bath — 2 A total current standard.`
2. Set properties:
   - Font: Inter Regular, Size: `14`, Color: `F0EDE8`
   - **Transparency**: With the text element selected, click the **transparency** button in the top toolbar (it looks like a checkerboard pattern or says "Transparency"). Set to **70%**.
   - Alignment: Center
3. Position below the zone labels, centered horizontally on the page.

### Step 17 — Group all of Zone 2
Select all elements from Steps 11-16 (panel rectangle, both gradient overlays, all six zone label/sub-label text boxes, three arrow lines, caption). Press **Ctrl+G** to group.

---

## Phase 4 — Zone 3A: Diagnostic Interpretation Table (Left Column)

This is the largest and most detailed section of the poster. It occupies the **left 58%** of the page width, from about 13.3 inches to 27.0 inches from the top. It contains 1 header row + 11 data rows.

**Work area**: Left edge at the 0.5-inch guide, right edge at the 13.8-inch guide.

### Step 18 — Section title
1. Add a text element. Type: `WHAT YOUR PANEL IS TELLING YOU`
2. Font: Barlow SemiBold, Size: `28`, Color: `E8A020` (Amber)
3. Alignment: Left
4. Position: left edge at 0.5-inch guide, top at about 13.5 inches from page top (0.2 inches below your Zone 2/3 horizontal guide).

### Step 19 — Build the table header row

**19a — Header row background:**
1. Add a rectangle. Set dimensions:
   - **Width**: `13.3` inches (from 0.5-inch to 13.8-inch guide)
   - **Height**: `0.6` inches
2. Fill color: `3A4055` (Mid Slate). No border.
3. Position: top edge about 0.15 inches below the section title.

**19b — Header text — Column 1:**
1. Add a text element. Type: `PANEL APPEARANCE`
2. Font: Barlow SemiBold, Size: `22`, Color: `E8A020`
3. Position: inside the header rectangle, left edge at about 0.7 inches from page left (accounting for left-border space).
4. Set text box width to approximately 5.1 inches (40% of the table width).

**19c — Header text — Column 2:**
1. Add a text element. Type: `MOST LIKELY CAUSE`
2. Same font, size, color as Column 1.
3. Position: starting at about 5.8 inches from page left. Text box width: about 3.9 inches (30%).

**19d — Header text — Column 3:**
1. Add a text element. Type: `FIRST CORRECTIVE ACTION`
2. Same font, size, color.
3. Position: starting at about 9.7 inches from page left. Text box width: about 3.9 inches (30%).

### Step 20 — Build one template data row (you will duplicate this 10 times)

**Build Row 1 (Good bath) first as your template:**

**20a — Row background rectangle:**
1. Add a rectangle.
   - Width: `13.3` inches
   - Height: `1.0` inch (adjust later if text needs more room)
   - Fill: `1A1F2E` (same as page background — it will be barely visible but structurally important)
   - No border.
2. Position directly below the header row.

**20b — Left-border accent rectangle:**
1. Add a small rectangle.
   - Width: `0.08` inches (about 6 pt — this is the colored left-border stripe)
   - Height: same as the row background (1.0 inch)
   - Fill: `27AE60` (Emerald — for Row 1 "Good bath")
   - No border.
2. Position: flush with the left edge of the row background rectangle.

**20c — Emerald tint overlay (Row 1 only):**
1. Add a rectangle.
   - Width: `13.3` inches (full row width)
   - Height: `1.0` inch
   - Fill: `27AE60` (Emerald)
   - **Transparency**: Set to **8%** (click the transparency button, set to 8)
   - No border.
2. Position: directly on top of the row background rectangle, same size and position. This gives Row 1 a very subtle green tint to mark it as the "good bath" reference row.

**20d — Column 1 text:**
1. Add a text element. Type:
   `Mirror bright from HCD through mid-current; slight softening at LCD; no skip plate`
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`
3. Line spacing: set to `1.4`
4. Set text box width to about 5.0 inches.
5. Position: inside the row, left edge at about 0.7 inches from the page left (leaving room for the border accent). Top padding: about 0.1 inches from the row top.

**20e — Column 2 text:**
1. Add a text element. Type: `Good bath`
2. Font: Inter Medium (or Inter SemiBold), Size: `18`, Color: `F0EDE8`
   - The cause name is set in Medium/SemiBold to make scanning the column fast.
3. Position: at about 5.8 inches from page left.

**20f — Column 3 text:**
1. Add a text element. Type:
   `No action needed — archive this panel as your visual reference standard`
2. Font: Inter Regular, Size: `18`, Color: `F0EDE8`
3. Position: at about 9.7 inches from page left.

**20g — Group this row:**
Select the row background, left-border accent, Emerald tint overlay, and all three text boxes. Press **Ctrl+G** to group.

### Step 21 — Duplicate and modify for Rows 2-11

Now you will duplicate the Row 1 group 10 times and modify each copy. For each row:
1. Click the Row 1 group. Press **Ctrl+D** (or Cmd+D) to duplicate.
2. Drag the duplicate directly below the previous row (align elements precisely).
3. Ungroup temporarily (**Ctrl+Shift+G**) to edit individual elements.
4. Change the **row background color** (see the table below).
5. Change the **left-border accent color** (see the table below).
6. Delete the Emerald tint overlay (only Row 1 has this).
7. Update the three text boxes with the correct content.
8. Re-group when done.

**Row-by-row specifications:**

---

**Row 2 — Brightener deficiency:**
- Background: `252B3D` (Alt Row)
- Left border: `E8A020` (Amber)
- Col 1: `Overall semi-bright or matte; burn zone at HCD enlarges toward mid-current`
- Col 2: **`Brightener deficiency`** (Inter Medium/SemiBold)
- Col 3: `Add brightener in 0.1–0.5 mL/L increments; re-run panel after each addition`

**Row 3 — Brightener overload:**
- Background: `1A1F2E` (Gunmetal Dark)
- Left border: `E8A020` (Amber)
- Col 1: `Mirror bright at HCD and mid-current; LCD progressively dull, advancing to skip plate at extremes`
- Col 2: **`Brightener overload`** (Inter Medium/SemiBold)
- Col 3: `Carbon treat at 5–10 g/L; reconstitute additive system from fresh baseline`

**Row 4 — Carrier deficiency:**
- Background: `252B3D`
- Left border: `E8A020`
- Col 1: `Pitting across the full panel; HCD burning prominent`
- Col 2: **`Carrier (wetting agent) deficiency`** (Inter Medium/SemiBold)
- Col 3: `Check bath temperature vs. cloud point first; add carrier incrementally; re-run panel`

**Row 5 — Carrier overload:**
- Background: `1A1F2E`
- Left border: `E8A020`
- Col 1: `Overall hazy or milky panel; reduced deposit brightness; foaming visible in production tank`
- Col 2: **`Carrier overload / temperature above cloud point`** (Inter Medium/SemiBold)
- Col 3: `Check and lower bath temperature immediately; carbon treat if needed`

**Row 6 — Iron contamination:**
- Background: `252B3D`
- Left border: `E05C5C` (Coral)
- Col 1: `Yellow to dark band at HCD; haze across mid-current; LCD coverage loss or skip plate`
- Col 2: **`Iron contamination`** in Inter Medium/SemiBold, then on the same line or just below in Inter Regular: `(>50–75 ppm)`
- Col 3: `Add 1–2 mL/L of 30% H₂O₂; raise pH to 5.0–5.5; allow to settle; filter thoroughly`

**Row 7 — Lead/cadmium contamination:**
- Background: `1A1F2E`
- Left border: `E05C5C` (Coral)
- Col 1: `Skip plate in LCD; HCD appears normal; no improvement after brightener adjustment`
- Col 2: **`Lead or cadmium contamination`** in Inter Medium/SemiBold, then: `(1–2 ppm threshold)`
- Col 3: `Zinc dust treatment; dummy plate at low CD; identify and eliminate contamination source`

**Row 8 — Copper contamination:**
- Background: `252B3D`
- Left border: `E05C5C` (Coral)
- Col 1: `Dark or black deposit visible after bright dip or passivation`
- Col 2: **`Copper contamination`** in Inter Medium/SemiBold, then: `(>10 ppm)`
- Col 3: `Dummy plate at 0.1–0.3 A/dm² on steel cathodes; follow with zinc dust treatment`

**Row 9 — Organic contamination:**
- Background: `1A1F2E`
- Left border: `E05C5C` (Coral)
- Col 1: `LCD dullness; streaking across panel; variable pitting not resolved by carrier addition`
- Col 2: **`Organic contamination`** (Inter Medium/SemiBold)
- Col 3: `H₂O₂ pre-treat at 0.5–1 mL/L; then carbon treat at 5–10 g/L; reconstitute additives`

**Row 10 — Low zinc metal:**
- Background: `252B3D`
- Left border: `E8A020` (Amber)
- Col 1: `Burning advances from HCD into mid-current; LCD coverage is consistently poor`
- Col 2: **`Low zinc metal concentration`** (Inter Medium/SemiBold)
- Col 3: `Analyze zinc by titration; add zinc metal source; verify anode area is adequate`

**Row 11 — Suspended solids:**
- Background: `1A1F2E`
- Left border: `E8A020` (Amber)
- Col 1: `Rough, nodular deposit; visible particles in bath; turbidity`
- Col 2: **`Suspended solids`** in Inter Medium/SemiBold, then: `— pH too high or filtration failure`
- Col 3: `Check pH (target 4.8–5.2); inspect filter integrity and anode bags; clean tank bottom`

---

**Row height note:** Some rows will need more than 1.0 inch to fit the text comfortably. Adjust individual row background rectangles taller as needed. Make sure the left-border accent rectangle matches the row height. The total table height should not exceed about 12.5 inches — if it does, reduce body text to `16` pt and adjust row heights down.

### Step 22 — Table footnotes
1. Add a text element below the last row of the table.
2. Type these three lines (each starting with an asterisk):
   ```
   *Scope: acid zinc KCl/NH₄Cl baths only. Results may differ for other zinc bath chemistries.*

   *Cadmium is highly toxic. Even trace cadmium contamination via parts warrants immediate bath analysis. Do not assume lead or cadmium without analytical confirmation.*

   *After any carbon treatment, brightener and carrier are partially removed. Always reconstitute the full additive system after carbon treatment.*
   ```
3. Font: Inter Regular, Size: `13`, Color: `F0EDE8`
4. **Transparency**: Set to **60%**.
5. Position: left edge at 0.5-inch guide, about 0.15 inches below the last table row.

### Step 23 — Group all of Zone 3A
Select the section title, header row (rectangle + text), all 11 data row groups, and the footnotes text. Press **Ctrl+G** to group.

---

## Phase 5 — Zone 3B: Right Column (Setup Parameters + SPC Callout)

This column occupies the **right 38%** of the page width, from the 14.1-inch vertical guide to the 23.5-inch guide. It shares the same vertical band as Zone 3A (13.3 inches to 27.0 inches from the top).

### Step 24 — Setup Parameters section title
1. Add a text element. Type: `HULL CELL SETUP PARAMETERS`
2. Font: Barlow SemiBold, Size: `24`, Color: `E8A020`
3. Alignment: Left
4. Position: left edge at 14.1-inch guide, top at about 13.5 inches (aligned with the Zone 3A section title).

### Step 25 — Setup Parameters table header
1. Add a rectangle.
   - Width: `9.4` inches (from 14.1-inch to 23.5-inch guide)
   - Height: `0.5` inches
   - Fill: `3A4055`
2. Position directly below the section title.
3. Add two text elements inside the header:
   - Left: `PARAMETER` — Barlow SemiBold, `20` pt, color `E8A020`. Position at about 14.3 inches from left.
   - Right: `VALUE` — same font/size/color. Position at about 18.4 inches from left.

### Step 26 — Setup Parameters data rows

Build 8 rows using the same rectangle-stack method as Zone 3A, but **without** left-border accents. Alternate backgrounds between `1A1F2E` and `252B3D`. Each row is about 0.65 inches tall.

Font for all data: JetBrains Mono Regular (or Courier Prime), Size: `16`, Color: `F0EDE8`.

| Row | Parameter | Value |
|-----|-----------|-------|
| 1 (BG: `1A1F2E`) | `Cell volume` | `267 mL` |
| 2 (BG: `252B3D`) | `Cathode material` | `Cold-rolled steel — cleaned and acid-activated` |
| 3 (BG: `1A1F2E`) | `Anode material` | `SHG zinc — 99.99% pure (lower grades introduce Pb, Cd, Fe)` |
| 4 (BG: `252B3D`) | `Test current — rack` | `2 A (standard); 3 A for high-current diagnostic` |
| 5 (BG: `1A1F2E`) | `Test current — barrel` | `1 A` |
| 6 (BG: `252B3D`) | `Test duration` | `5 minutes` |
| 7 (BG: `1A1F2E`) | `Agitation` | `Air agitation — required` |
| 8 (BG: `252B3D`) | `Temperature` | `Match actual bath temperature` |

**Note on Row 3 (Anode material):** The value text is long. Let it wrap to two lines and make that row taller (about 0.9 inches instead of 0.65). Never cut the contamination warning — it is the reason this specification matters.

### Step 27 — Cathode preparation note
1. Draw a horizontal line across the full Zone 3B width.
   - Color: `3A4055`, Thickness: `1` pt.
   - Position: about 0.1 inches below the last table row.
2. Add a text element. Type: `CATHODE PREPARATION`
   - Font: Barlow SemiBold, Size: `16`, Color: `E8A020`
   - Position below the line.
3. Add a text element below the label. Type:
   `Degrease with acetone or electrocleaner. Activate in 5–10% HCl for 15–30 seconds. Rinse thoroughly. Use immediately. Do not touch with bare hands after activation.`
   Then press Enter and add:
   `OPTIONAL: Bright dip or passivate the plated panel to reveal deposit quality — highly recommended for contamination diagnosis.`
4. Font: Inter Regular, Size: `14`, Color: `F0EDE8`
5. Line spacing: `1.4`

### Step 28 — SPC Tool callout box

**28a — Draw the box:**
1. Add a rounded rectangle.
   - Width: `9.4` inches (full Zone 3B width)
   - Height: approximately `3.0` inches (adjust to fit content)
   - Fill: `1E2435` (Dark Callout)
   - Border: `1.5` pt, color `2EC4B6` (Teal)
   - Corner radius: approximately `8`
2. Position in the lower portion of Zone 3B. Leave a 0.25-inch gap between the cathode prep note and this box.

**28b — Callout title:**
1. Add a text element. Type: `MAKE YOUR HULL CELL A CONTROL CHART`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6`
3. Position inside the box, near the top, with 0.15 inches padding.

**28c — Bullet points:**
1. Add a text element. Type these four lines (use the bullet character at the start of each — type the dot manually or use a bulleted list format):
   ```
   - Run weekly at minimum — or every 500–1000 ampere-hours of production throughput

   - Archive every panel with: date, bath analysis results, ampere-hour reading, and all additions made

   - Laminate a known-good reference panel and mount it next to this poster

   - Visual trends across archived panels reveal bath drift before symptoms appear on production parts
   ```
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`
3. Line spacing: `1.5`
4. If using bullet list formatting, change the bullet color to `2EC4B6` (Teal) if the option is available. If not, the default color is fine.
5. Position inside the box below the title, with 0.15 inches side padding.

**28d — Group the callout box:**
Select the rounded rectangle, title, and bullet text. Press **Ctrl+G**.

### Step 29 — Group all of Zone 3B
Select the section title, header row, all 8 data rows, cathode prep line and text, and the SPC callout group. Press **Ctrl+G**.

---

## Phase 6 — Zone 4: Isolation Protocol Callout

This is a full-width callout box spanning from about 27.0 inches to 31.3 inches from the top (about 4.3 inches tall).

### Step 30 — Draw the container
1. Add a rounded rectangle.
   - Width: `23` inches (from 0.5-inch to 23.5-inch guides)
   - Height: `4.3` inches
   - Fill: `1E2435` (Dark Callout)
   - Border: `1.5` pt, color `2EC4B6` (Teal)
   - Corner radius: approximately `8`
2. Position: top edge at the 27.0-inch horizontal guide.

### Step 31 — Left column content (inside the callout, left 40%)

**31a — Title:**
1. Add a text element. Type on two lines:
   `WHEN THE DIAGNOSIS ISN'T CLEAR:`
   (press Enter)
   `THE ISOLATION PROTOCOL`
2. Font: Barlow SemiBold, Size: `24`, Color: `2EC4B6`
3. Line spacing: set to `0.9` (tighter than normal)
4. Position: inside the callout, top-left area, with 0.2 inches padding from the top and left edges of the box.

**31b — Intro line:**
1. Add a text element. Type:
   `When one corrective action doesn't solve the problem, test one variable at a time using separate aliquots of fresh bath solution.`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`
3. Set text box width to about 8.5 inches (the left 40% of the callout interior).
4. Position below the title with a 0.1-inch gap.

### Step 32 — Right column content (right 56% of the callout interior)

**32a — Numbered steps:**
1. Add a text element. Type the following (each step on its own line with a blank line between):
   ```
   1. Add a brightener increment to a fresh aliquot — run panel. If HCD and mid-current improve: brightener was low.

   2. Add a carrier increment to a fresh aliquot — run panel. If pitting clears: carrier was low.

   3. Add boric acid to a fresh aliquot — run panel. If HCD burning reduces: boric acid was low.

   4. Adjust pH in a fresh aliquot with HCl or zinc carbonate — run panel. Confirm whether pH drift was the driver.
   ```
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`
3. For the step numbers (1. 2. 3. 4.): If you can select just the numbers and change them individually, set them to Barlow SemiBold, color `2EC4B6`. If not, leave them as Inter Regular — this is a minor visual enhancement, not critical.
4. Position: in the right portion of the callout box (starting at roughly the 10-inch mark from page left), top-aligned with the title.

**32b — Closing rule with amber accent:**
1. Add a narrow vertical rectangle:
   - Width: `0.03` inches (about 2 pt)
   - Height: approximately `0.3` inches (match the height of the closing text)
   - Fill: `E8A020` (Amber)
   - No border.
2. Position this thin amber bar to the left of where the closing text will go.
3. Add a text element. Type:
   `THE RULE: Change one variable. Run one panel. Decide. Then move to the next variable.`
4. Font: Inter Medium, Size: `16`, Color: `E8A020` (Amber)
5. Position to the right of the amber bar, with a small gap (about 0.05 inches).
6. Place this closing rule below the numbered steps, with a 0.1-inch gap.

### Step 33 — Group all of Zone 4
Select the rounded rectangle container, all text elements inside it, and the amber accent bar. Press **Ctrl+G**.

---

## Phase 7 — Zone 5: Footer Band

This occupies the bottom 2.2 inches of the poster (from about 33.8 inches to 36 inches).

### Step 34 — Footer band background
1. Add a rectangle.
   - Width: `24` inches (full page width — edge to edge, no margins)
   - Height: `2.0` inches
   - Fill: `0D1020` (Deep Navy)
   - No border.
2. Position: bottom edge flush with the bottom of the page.

### Step 35 — Disclaimer text (above the footer band)
1. Add a text element. Type:
   `This poster is a diagnostic reference tool. Always consult your process supplier's documentation and applicable safety data sheets. Not a substitute for laboratory analysis.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`
3. **Transparency**: Set to **50%**.
4. Alignment: Center
5. Position: centered horizontally, about 0.1 inches above the top edge of the Deep Navy footer band.

### Step 36 — Footer content (inside the band)

**36a — Left: Poster title**
1. Add a text element. Type: `Reading Your Hull Cell Panel`
2. Font: Barlow SemiBold, Size: `14`, Color: `F0EDE8`
3. Position: left side of the footer band, left edge at about 0.7 inches from page left, vertically centered in the band.

**36b — Center: Series name**
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `12`, Color: `F0EDE8`
3. **Transparency**: Set to **70%**.
4. Position: horizontally centered in the footer band, vertically centered.

**36c — Right: Logo placeholder**
1. Add a small square rectangle.
   - Width: `0.55` inches, Height: `0.55` inches
   - Fill: `3A4055` (Mid Slate)
   - No border.
2. Add a text element inside it. Type: `LOGO`
3. Font: JetBrains Mono Regular, Size: `10`, Color: `F0EDE8`. Center the text in the square.
4. Position the square in the right side of the footer band, right edge at about 23.3 inches from page left, vertically centered.

**36d — Version number**
1. Add a text element. Type: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `10`, Color: `F0EDE8`
3. **Transparency**: Set to **50%**.
4. Position: below the logo placeholder square, right-aligned.

### Step 37 — Group all of Zone 5
Select the Deep Navy rectangle, disclaimer text, and all footer content. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

Before exporting, ungroup all zones and verify each item. Re-group after review.

### Text verification
- [ ] Headline reads: `READING YOUR HULL CELL PANEL` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Diagnose your plating bath before it diagnoses your scrap rate.` in Barlow SemiBold, `#E8A020`
- [ ] "What Is a Hull Cell?" callout box has Teal border and all text present
- [ ] All three zone labels are present below the panel illustration: HIGH CURRENT DENSITY (Amber), MID-CURRENT (Warm White), LOW CURRENT DENSITY (Teal)
- [ ] All three zone sub-labels show correct current density values
- [ ] Diagnostic table has exactly 11 data rows plus 1 header row
- [ ] Setup Parameters table has exactly 8 data rows plus 1 header row
- [ ] Cathode Preparation note is present below the Setup Parameters table
- [ ] Isolation Protocol callout has all 4 numbered steps and the closing rule
- [ ] SPC Tool callout has all 4 bullet points
- [ ] Three footnotes are present below the diagnostic table
- [ ] Disclaimer text is present above the footer band
- [ ] Footer shows: poster title (left), series name (center), LOGO placeholder (right), version (bottom-right)

### Color verification
- [ ] Background is `#1A1F2E` (dark gunmetal)
- [ ] All body text is `#F0EDE8` (warm white) — not pure white
- [ ] Section titles and header row text are `#E8A020` (amber)
- [ ] Callout box borders are `#2EC4B6` (teal)
- [ ] Row 1 (Good bath) has Emerald left border and subtle green tint
- [ ] Rows 2-5, 10-11 have Amber left borders
- [ ] Rows 6-9 have Coral left borders
- [ ] Footer band is `#0D1020` (deep navy) — darker than the main background

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone on all four sides
- [ ] Zone 3A (diagnostic table) and Zone 3B (setup parameters) sit side by side with a visible gutter
- [ ] All rows in both tables have consistent height (within each table)
- [ ] Three callout arrows connect the panel illustration to the diagnostic table area
- [ ] No text is cut off or overlapping other elements

### Readability check
- [ ] Zoom to 25% view — can you read the headline and zone labels? (These should be clear from across a room.)
- [ ] Zoom to 50% view — can you read the table headers and cause names? (Readable from 6-8 feet.)
- [ ] Zoom to 75% view — can you read the table cell content? (Readable from 4 feet.)
- [ ] Zoom to 100% — can you read the footnotes and disclaimer? (Readable from 2-3 feet.)

---

## Phase 9 — Light Edition: Remap Instructions

After the Dark edition is reviewed and approved, produce the Light edition.

### Step 38 — Duplicate the page
1. 
2. Duplicate the Dark edition design.
3. 
4. 
5. Rename it "Light Edition" 

### Step 39 — Change the background
1. Click on the empty background area of Page 2 (not on any element).
2. Change the background color from `1A1F2E` to `F5F4F0` (Off-White).

### Step 40 — Remap all elements

Work through this table top to bottom. For each color change, click on elements that use the old color and change them to the new color. Work systematically through each zone.

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | 3 rounded rectangles (Block B, Block G, Block F/Zone 4) | `#1E2435` | `#ECEEF4` |
| **Alt Row backgrounds** | Even-numbered table row rectangles | `#252B3D` | `#E8E8F0` |
| **Odd row backgrounds** | Odd-numbered table row rectangles (currently same as BG) | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Section titles, header text, HCD zone label, Amber borders, HCD gradient band | `#E8A020` | `#C8860A` |
| **Teal elements** | Callout borders, callout titles, LCD zone label, LCD gradient band, bullet dots | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | Row 1 left border, Row 1 tint overlay | `#27AE60` | `#1E7A47` |
| **Coral elements** | Rows 6-9 left borders | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Table header fill rectangles, rules, dividers, arrows | `#3A4055` | `#D0D4DE` |
| **Panel surface** | Hull cell panel body rectangle gradient | **DO NOT CHANGE** | Stays `#C8D0D8` — always metallic |

### Step 41 — Post-remap adjustments

Check these specific items after remapping:

1. **Zone band overlays**: The HCD and LCD gradient bands at the top of the panel illustration were set to 70% opacity. On the light background, they may look too solid. If they appear as hard color blocks instead of gentle fades, reduce their opacity to **50-60%**.
2. **Good bath row tint**: The 8% Emerald overlay on Row 1 may be invisible on the light background. If you cannot see the green tint, increase the overlay opacity from 8% to **12%**.
3. **Footnote text**: At 60% opacity, verify the three footnotes are readable against the off-white background. If too faint, increase opacity to **75%**.
4. **Disclaimer text**: At 50% opacity, verify it is readable. If too faint, increase to **65%**.
5. **Caption text** (below the panel diagram): at 70% opacity, verify readability. Increase to **85%** if needed.

---

## Phase 10 — Export Instructions

### Step 42 — Export the Dark edition (Page 1)

**42a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed** if the option is available.
4. Select only **Page 1** (Dark edition).
5. Click Download.
6. Rename the downloaded file to: `Hull-Cell-Panel-Dark-24x36-Print.pdf`

**42b — Digital PDF, 24x36":**
1. 
2. File type: **PDF Standard** (not Print).
3. Uncheck crop marks/bleed.
4. Select only Page 1.
5. Download and rename to: `Hull-Cell-Panel-Dark-Digital.pdf`

**42c — Print PDF, 18x24" (scaled version):**
1. 
2. Set custom size to **18 x 24 inches**.
3. Click **Copy & resize** (this creates a new design — it does not destroy the original).
4. In the resized copy, check that all text is legible. Verify body text is at least 14 pt. If any text dropped below 14 pt, increase it.
5. Export as PDF Print (with crop marks and bleed).
6. Rename to: `Hull-Cell-Panel-Dark-18x24-Print.pdf`

### Step 43 — Export the Light edition (Page 2)

Repeat Steps 42a, 42b, and 42c but select **Page 2** (Light edition) and use these filenames:
- `Hull-Cell-Panel-Light-24x36-Print.pdf`
- `Hull-Cell-Panel-Light-Digital.pdf`
- `Hull-Cell-Panel-Light-18x24-Print.pdf`

### Export file checklist
After exporting, confirm you have all six files:

- [ ] `Hull-Cell-Panel-Dark-24x36-Print.pdf`
- [ ] `Hull-Cell-Panel-Dark-18x24-Print.pdf`
- [ ] `Hull-Cell-Panel-Dark-Digital.pdf`
- [ ] `Hull-Cell-Panel-Light-24x36-Print.pdf`
- [ ] `Hull-Cell-Panel-Light-18x24-Print.pdf`
- [ ] `Hull-Cell-Panel-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | HCD zone, section titles, Amber accents |
| `#2EC4B6` | Teal | LCD zone, callout borders/titles |
| `#27AE60` | Emerald | Good bath row accent |
| `#E05C5C` | Coral | Contamination row accents |
| `#3A4055` | Mid Slate | Table headers, rules, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout box fills |
| `#252B3D` | Alt Row | Even-numbered table rows |
| `#C8D0D8` | Bright Silver | Panel surface (both editions) |
| `#9AA0B0` | Panel Edge | Panel border stroke |
| `#D8E0E8` | Light Silver | Panel gradient left stop |
| `#B8C0C8` | Muted Silver | Panel gradient right stop |
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
| v1.0 | 2026-04-03 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0 (2026-03-19). All technical content production-ready. |
