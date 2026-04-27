---
Project: Plating Posters Inc
Poster Number: 11
Title: "Current Density Quick Reference Chart"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 11 — Current Density — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - CurrentDensity
  - v1
---

# Claude Chat Generation Prompt — Poster #11
## Current Density Quick Reference Chart
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

This zone occupies the top 2.9 inches. Headline and tagline on the left (~60%), CD Formula callout on the right (~40%).

### Step 6 — Place the headline
1. Add a heading text element:
2. Select all placeholder text and type: `CURRENT DENSITY`
3. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `96`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
4. Position: left edge at 0.5 inches, top edge at 0.5 inches.
5. Set text box width to approximately **13.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Quick Reference Chart`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `40`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.6 inches**.

### Step 8 — Place the tagline
1. Add a body text element: Type: `Right range. Right deposit. Every time.`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: **65%**
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.3 inches**.

### Step 9 — Build the CD Formula callout box

**9a — Callout container:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Set properties:
   - **Width**: `9.0` inches
   - **Height**: `2.2` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 1.5 pt, color `2EC4B6` (Teal)
   - **Corner radius**: `8`
3. Position: right edge at the 23.5-inch guide, top edge at 0.5 inches.

**9b — Callout title:**
1. Add a text element. Type: `THE FORMULA`
2. Font: Barlow SemiBold, Size: `20`, Color: `2EC4B6` (Teal)
3. Position: inside the container, top-left area, approximately 0.2 inches from the left edge and 0.15 inches from the top.

**9c — Formula:**
1. Add a text element. Type: `ASF = Amps / Area (ft²)`
2. Font: JetBrains Mono Regular, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally inside the container, below the title with about 0.15 inches gap.

**9d — Worked example (line 1):**
1. Add a text element. Type: `10 bolts at 2.5 ft² total, 75 A applied:`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Transparency: **80%**
3. Position: centered inside the container, below the formula.

**9e — Worked example (line 2):**
1. Add a text element. Type: `75 / 2.5 = 30 ASF`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`, Transparency: **80%**
3. Position: centered inside the container, directly below line 1.

**9f — Conversion note:**
1. Add a text element. Type: `ASF / 10 ~ ASD`
2. Font: JetBrains Mono Regular, Size: `14`, Color: `E8A020` (Amber)
3. Position: centered inside the container, below the worked example with about 0.1 inches gap.

**9g — Group the callout box:**
Select the container, title, formula, both example lines, and conversion note. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and formula callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Master Current Density Table (The Hero)

This zone occupies Y: 2.9" to 28.1" (25.2 inches tall). It contains a section label plus a 29-row table (1 column header + 7 section headers + 21 data rows).

**Build strategy:** Build the column header row, one section header row template, and one data row template. Then duplicate the templates for all remaining rows and change the text. This cuts the build time by 70%.

### Step 11 — Section label
1. Add a text element. Type: `CURRENT DENSITY RANGES BY PROCESS`
2. Font: Barlow Condensed ExtraBold, Size: `32`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, top edge at **3.0 inches**. Width: **23.0 inches**.

### Step 12 — Build the column header row

**12a — Header row background:**
1. Add a Rounded Rectangle.
   - **Width**: `23.0` inches
   - **Height**: `0.55` inches
   - **Fill**: `3A4055` (Mid Slate)
   - **Corner radius**: `4` (top corners only if possible; all corners 4 is fine)
2. Position: left edge at 0.5 inches, top edge at **3.6 inches**.

**12b — Header text: PROCESS**
1. Add a text element. Type: `PROCESS`
2. Font: Barlow SemiBold, Size: `20`, Color: `E8A020` (Amber), Alignment: Left
3. Position: inside header row, left edge at approximately **0.7 inches**, vertically centered.
4. Set text box width to approximately **8.0 inches**.

**12c — Header text: RACK (ASF)**
1. Add a text element. Type: `RACK (ASF)`
2. Font: Barlow SemiBold, Size: `20`, Color: `E8A020`, Alignment: Center
3. Position: left edge at approximately **8.6 inches**, vertically centered.
4. Width: approximately **3.7 inches**.

**12d — Header text: BARREL (ASF)**
1. Add a text element. Type: `BARREL (ASF)`
2. Same font, size, color, alignment.
3. Position: left edge at approximately **12.3 inches**. Width: **3.7 inches**.

**12e — Header text: EFFICIENCY**
1. Add a text element. Type: `EFFICIENCY`
2. Same font, size, color, alignment.
3. Position: left edge at approximately **16.0 inches**. Width: **3.7 inches**.

**12f — Header text: NOTES**
1. Add a text element. Type: `NOTES`
2. Font: Barlow SemiBold, Size: `20`, Color: `E8A020`, Alignment: Left
3. Position: left edge at approximately **19.7 inches**. Width: **3.8 inches**.

### Step 13 — Build one Section Header Row template (ZINC PLATING)

**13a — Section header background:**
1. Add a Rectangle (sharp corners).
   - **Width**: `23.0` inches
   - **Height**: `0.50` inches
   - **Fill**: `1E2740` (pre-blended Teal at 15% over Gunmetal Dark)
   - **No border**.
2. Position: left edge at 0.5 inches, directly below the column header row (top edge at approximately **4.15 inches**).

**13b — Left accent bar:**
1. Add a Rectangle.
   - **Width**: `0.08` inches
   - **Height**: `0.50` inches
   - **Fill**: `2EC4B6` (Teal)
2. Position: flush against the left edge of the section header background.

**13c — Section header text:**
1. Add a text element. Type: `ZINC PLATING`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `2EC4B6` (Teal)
3. Position: left edge at approximately **0.8 inches**, vertically centered in the section header row.

**13d — Group the section header:**
Select the background, accent bar, and text. Press **Ctrl+G**.

### Step 14 — Build one Data Row template (Row 1: Acid Chloride Zinc)

**14a — Row background:**
1. Add a Rectangle.
   - **Width**: `23.0` inches
   - **Height**: `0.75` inches
   - **Fill**: `1A1F2E` (base row — same as page background)
   - **No border**.
2. Position: directly below the ZINC PLATING section header.

**14b — Left accent bar:**
1. Add a Rectangle.
   - **Width**: `0.06` inches (approximately 4 pt)
   - **Height**: `0.75` inches
   - **Fill**: `2EC4B6` (Teal — matches the Zinc family)
2. Position: flush against the left edge of the row background.

**14c — Process column text:**
1. Add a text element. Type: `Acid Chloride Zinc (KCl)`
2. Font: Inter Medium, Size: `18`, Color: `F0EDE8`, Alignment: Left
3. Position: left edge at approximately **0.7 inches**, vertically centered in the row.
4. Width: approximately **7.9 inches**.

**14d — Rack column text:**
1. Add a text element. Type: `10-40`
2. Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`, Alignment: Center
3. Position: left edge at approximately **8.6 inches**, vertically centered.
4. Width: approximately **3.7 inches**.

**14e — Barrel column text:**
1. Add a text element. Type: `3-15`
2. Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`, Alignment: Center
3. Position: left edge at approximately **12.3 inches**, vertically centered.
4. Width: approximately **3.7 inches**.

**14f — Efficiency column text:**
1. Add a text element. Type: `95-98%`
2. Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`, Alignment: Center
3. Position: left edge at approximately **16.0 inches**, vertically centered.
4. Width: approximately **3.7 inches**.

**14g — Notes column text:**
1. Add a text element. Type: `Most common zinc process`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **80%**, Alignment: Left
3. Position: left edge at approximately **19.7 inches**, vertically centered.
4. Width: approximately **3.5 inches**.

**14h — Group the data row:**
Select the background, accent bar, and all 5 text elements. Press **Ctrl+G**.

### Step 15 — Build Row 2: Alkaline Non-Cyanide Zinc (Duplicate and Modify)

1. Duplicate the Row 1 group (Ctrl+D). Reposition directly below Row 1 (flush, no gap).
2. Ungroup. Make these changes:
   - **Row background fill**: `252B3D` (Alt Row)
   - **Process**: `Alkaline Non-Cyanide Zinc`
   - **Rack**: `10-30`
   - **Barrel**: `5-15`
   - **Efficiency**: `70-80%`
   - **Notes**: `Insoluble anodes; lower eff.`
3. Re-group.

### Step 16 — Build Row 3: Alkaline Cyanide Zinc

1. Duplicate Row 1 group. Reposition below Row 2.
2. Ungroup. Changes:
   - **Row background fill**: `1A1F2E` (base)
   - **Process**: `Alkaline Cyanide Zinc`
   - **Rack**: `10-40`
   - **Barrel**: `5-15`
   - **Efficiency**: `65-80%`
   - **Notes**: `Legacy NaCN; high throwing power`
3. Re-group.

### Step 17 — COPPER PLATING section header

1. Duplicate the ZINC PLATING section header group. Reposition below Row 3.
2. Ungroup. Changes:
   - **Background fill**: `2D2833` (pre-blended Amber at 15%)
   - **Accent bar fill**: `E8A020` (Amber)
   - **Text**: `COPPER PLATING`. Color: `E8A020` (Amber)
3. Re-group.

### Step 18 — Row 4: Bright Acid Copper

1. Duplicate Row 2 (the alt-row template). Reposition below COPPER header.
2. Ungroup. Changes:
   - **Row background fill**: `252B3D` (alt)
   - **Accent bar fill**: `E8A020` (Amber)
   - **Process**: Copy-paste: `Bright Acid Copper`
   - **Rack**: `15-40`
   - **Barrel**: `5-15`
   - **Efficiency**: `95-100%`
   - **Notes**: Copy-paste: `CuSO₄/H₂SO₄; phosphorized anodes`
3. Re-group.

### Step 19 — Row 5: Cyanide Copper Strike

1. Duplicate Row 1 (base-row template). Reposition below Row 4.
2. Ungroup. Changes:
   - **Accent bar fill**: `E8A020` (Amber)
   - **Process**: `Cyanide Copper Strike`
   - **Rack**: `5-20`
   - **Barrel**: `3-10`
   - **Efficiency**: `30-60%`
   - **Notes**: `Thin flash — adhesion layer only`
3. Re-group.

### Step 20 — NICKEL PLATING section header

1. Duplicate the ZINC section header. Reposition below Row 5.
2. Ungroup. Changes:
   - **Background fill**: `22262F` (pre-blended White at 15% — very subtle)
   - **Accent bar fill**: `F0EDE8` (Warm White)
   - **Text**: `NICKEL PLATING`. Color: `F0EDE8` (Warm White)
3. Re-group.

### Step 21 — Row 6: Watts Nickel

1. Duplicate Row 2 (alt template). Reposition below NICKEL header.
2. Ungroup. Changes:
   - **Accent bar fill**: `F0EDE8` (Warm White)
   - **Process**: `Watts Nickel (bright/semi-bright)`
   - **Rack**: `20-60`
   - **Barrel**: `5-20`
   - **Efficiency**: `93-97%`
   - **Notes**: `Standard decorative + functional`
3. Re-group.

### Step 22 — Row 7: Nickel Sulfamate

1. Duplicate Row 1 (base template). Reposition below Row 6.
2. Ungroup. Changes:
   - **Accent bar fill**: `F0EDE8` (Warm White)
   - **Process**: `Nickel Sulfamate`
   - **Rack**: `20-140`
   - **Barrel**: Copy-paste this em dash: `—`
   - **Efficiency**: `95-100%`
   - **Notes**: `Engineering; 400+ ASF w/ agitation`
3. Re-group.

### Step 23 — Row 8: Nickel Strike (Watts)

1. Duplicate Row 2 (alt). Reposition below Row 7.
2. Ungroup. Changes:
   - **Accent bar fill**: `F0EDE8` (Warm White)
   - **Process**: `Nickel Strike (Watts)`
   - **Rack**: `10-50`
   - **Barrel**: `—`
   - **Efficiency**: `90-95%`
   - **Notes**: `Active substrates`
3. Re-group.

### Step 24 — Row 9: Nickel Strike (Wood's)

1. Duplicate Row 1 (base). Reposition below Row 8.
2. Ungroup. Changes:
   - **Accent bar fill**: `F0EDE8` (Warm White)
   - **Process**: `Nickel Strike (Wood's)`
   - **Rack**: `50-250`
   - **Barrel**: `—`
   - **Efficiency**: `50-70%`
   - **Notes**: `Stainless steel activation`
3. Re-group.

### Step 25 — CHROMIUM PLATING section header

1. Duplicate ZINC section header. Reposition below Row 9.
2. Ungroup. Changes:
   - **Background fill**: `2D2434` (pre-blended Coral at 15%)
   - **Accent bar fill**: `E05C5C` (Coral)
   - **Text**: `CHROMIUM PLATING`. Color: `E05C5C` (Coral)
3. Re-group.

### Step 26 — Row 10: Decorative Chrome (hex)

1. Duplicate Row 2 (alt). Reposition below CHROMIUM header.
2. Ungroup. Changes:
   - **Accent bar fill**: `E05C5C` (Coral)
   - **Process**: `Decorative Chrome (hex)`
   - **Rack**: `150-300`
   - **Barrel**: `—`
   - **Efficiency**: `10-18%`
   - **Notes**: `5-10x current of other processes`
3. Re-group.

### Step 27 — Row 11: Decorative Chrome (trivalent)

1. Duplicate Row 1 (base). Reposition below Row 10.
2. Ungroup. Changes:
   - **Accent bar fill**: `E05C5C` (Coral)
   - **Process**: `Decorative Chrome (trivalent)`
   - **Rack**: `40-150`
   - **Barrel**: `40-100`
   - **Efficiency**: `15-25%`
   - **Notes**: `Wider window; won't burn`
3. Re-group.

### Step 28 — Row 12: Hard Chrome (conventional)

1. Duplicate Row 2 (alt). Reposition below Row 11.
2. Ungroup. Changes:
   - **Accent bar fill**: `E05C5C` (Coral)
   - **Process**: `Hard Chrome (conventional)`
   - **Rack**: `150-300`
   - **Barrel**: `—`
   - **Efficiency**: `12-20%`
   - **Notes**: Copy-paste: `1-3 A/in²; functional`
3. Re-group.

### Step 29 — Row 13: Hard Chrome (mixed catalyst)

1. Duplicate Row 1 (base). Reposition below Row 12.
2. Ungroup. Changes:
   - **Accent bar fill**: `E05C5C` (Coral)
   - **Process**: `Hard Chrome (mixed catalyst)`
   - **Rack**: `150-300`
   - **Barrel**: `—`
   - **Efficiency**: `20-25%`
   - **Notes**: `Fluoride catalyst; higher eff.`
3. Re-group.

### Step 30 — SILVER PLATING section header

1. Duplicate ZINC section header. Reposition below Row 13.
2. Ungroup. Changes:
   - **Background fill**: `1C2534` (pre-blended Emerald at 15%)
   - **Accent bar fill**: `27AE60` (Emerald)
   - **Text**: `SILVER PLATING`. Color: `27AE60` (Emerald)
3. Re-group.

### Step 31 — Row 14: Silver Cyanide Strike

1. Duplicate Row 2 (alt). Reposition below SILVER header.
2. Ungroup. Changes:
   - **Accent bar fill**: `27AE60` (Emerald)
   - **Process**: `Silver Cyanide Strike`
   - **Rack**: `10-30`
   - **Barrel**: `5-15`
   - **Efficiency**: `95-100%`
   - **Notes**: `High initial CD; short time`
3. Re-group.

### Step 32 — Row 15: Silver Cyanide Plate

1. Duplicate Row 1 (base). Reposition below Row 14.
2. Ungroup. Changes:
   - **Accent bar fill**: `27AE60` (Emerald)
   - **Process**: `Silver Cyanide Plate`
   - **Rack**: `5-15`
   - **Barrel**: `3-10`
   - **Efficiency**: `95-100%`
   - **Notes**: `Low CD for smooth deposit`
3. Re-group.

### Step 33 — TIN PLATING section header

1. Duplicate SILVER section header. Reposition below Row 15.
2. Ungroup. Changes:
   - **Text**: `TIN PLATING`
   - (Background fill and accent bar stay the same — Tin uses Emerald like Silver)
3. Re-group.

### Step 34 — Row 16: Acid Tin (matte, MSA/sulfate)

1. Duplicate Row 2 (alt). Reposition below TIN header.
2. Ungroup. Changes:
   - **Accent bar fill**: `27AE60` (Emerald)
   - **Process**: `Acid Tin (matte, MSA/sulfate)`
   - **Rack**: `10-30`
   - **Barrel**: `5-15`
   - **Efficiency**: `90-95%`
   - **Notes**: `Zirconium anode baskets`
3. Re-group.

### Step 35 — Row 17: Acid Tin (bright)

1. Duplicate Row 1 (base). Reposition below Row 16.
2. Ungroup. Changes:
   - **Accent bar fill**: `27AE60` (Emerald)
   - **Process**: `Acid Tin (bright)`
   - **Rack**: `10-25`
   - **Barrel**: `5-15`
   - **Efficiency**: `90-95%`
   - **Notes**: `Organic brighteners added`
3. Re-group.

### Step 36 — OTHER PROCESSES section header

1. Duplicate ZINC section header. Reposition below Row 17.
2. Ungroup. Changes:
   - **Background fill**: `212536` (pre-blended Slate at 15%)
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Text**: `OTHER PROCESSES`. Color: `3A4055` (Mid Slate)
3. Re-group.

### Step 37 — Row 18: Cadmium (alkaline cyanide)

1. Duplicate Row 2 (alt). Reposition below OTHER header.
2. Ungroup. Changes:
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Process**: `Cadmium (alkaline cyanide)`
   - **Rack**: `5-70`
   - **Barrel**: `5-7`
   - **Efficiency**: `90-95%`
   - **Notes**: `15-25 ASF common for still`
3. Re-group.

### Step 38 — Row 19: Brass (cyanide)

1. Duplicate Row 1 (base). Reposition below Row 18.
2. Ungroup. Changes:
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Process**: `Brass (cyanide)`
   - **Rack**: `10-20`
   - **Barrel**: `10-20`
   - **Efficiency**: `50-70%`
   - **Notes**: `Color shifts with CD`
3. Re-group.

### Step 39 — Row 20: Zinc-Nickel (acid)

1. Duplicate Row 2 (alt). Reposition below Row 19.
2. Ungroup. Changes:
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Process**: `Zinc-Nickel (acid)`
   - **Rack**: `10-40`
   - **Barrel**: `5-15`
   - **Efficiency**: `85-95%`
   - **Notes**: `Alloy ratio affected by CD`
3. Re-group.

### Step 40 — Row 21: Sulfuric Acid Anodize (Type II)

1. Duplicate Row 1 (base). Reposition below Row 20.
2. Ungroup. Changes:
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Process**: `Sulfuric Acid Anodize (Type II)`
   - **Rack**: `12-18`
   - **Barrel**: `—`
   - **Efficiency**: `N/A`
   - **Notes**: `Oxide growth, not deposition`
3. Re-group.

### Step 41 — Row 22: Hard Coat Anodize (Type III)

1. Duplicate Row 2 (alt). Reposition below Row 21.
2. Ungroup. Changes:
   - **Accent bar fill**: `3A4055` (Mid Slate)
   - **Process**: `Hard Coat Anodize (Type III)`
   - **Rack**: `24-36`
   - **Barrel**: `—`
   - **Efficiency**: `N/A`
   - **Notes**: `Lower temp, higher voltage`
3. Re-group.

### Step 42 — Table footnote

1. Add a text element. Copy-paste this text exactly:
   `*All ranges are for normal production plating at typical bath concentrations and temperatures. Extreme conditions (high-speed, pulse, hone) excluded. Barrel CD typically 1/3 to 1/2 of rack CD. "—" = not typically barrel-plated. Efficiency = cathode efficiency. N/A = anodizing (oxide growth, not metal deposition).*`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`, Transparency: **60%**
3. Position: left edge at 0.5 inches, top edge approximately 0.2 inches below the bottom of Row 22. Width: **23.0 inches**.

### Step 43 — Group all of Zone 2
Select the section label, column header row, all 7 section headers, all 22 data rows, and the footnote. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: What Goes Wrong + Conversion

This zone occupies Y: 28.1" to 32.8" (4.7 inches tall). Left 60% has the "What Goes Wrong" callout. Right 40% has conversion + cross-reference.

### Step 44 — "What Goes Wrong" callout (left 60%)

**44a — Callout container:**
1. Add a Rounded Rectangle.
   - **Width**: `13.5` inches
   - **Height**: `4.3` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Corner radius**: `8`
   - **No border**.
2. Position: left edge at 0.5 inches, top edge at **28.2 inches**.

**44b — Section label:**
1. Add a text element. Type: `WHAT GOES WRONG`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally within the callout container, top edge approximately 0.15 inches from the container top.

**44c — Center divider:**
1. Add a vertical line:
   - Color: `3A4055` (Mid Slate)
   - Thickness: `1` pt
   - Length: approximately 3.4 inches (80% of the container height)
2. Position: centered horizontally within the container, vertically centered.

**44d — "TOO HIGH" title (left sub-column):**
1. Add a text element. Type: `TOO HIGH`
2. Font: Barlow SemiBold, Size: `18`, Color: `E05C5C` (Coral)
3. Position: left quarter of the container, approximately X: 1.5 inches, Y: 28.8 inches.

**44e — "TOO HIGH" bullet list:**
1. Add a text element. Type (each line on its own line — press Enter between items):
   `Burning — dark, rough, powdery edges`
   `Hydrogen pitting — trapped gas bubbles`
   `Poor adhesion — stressed deposit`
   `Reduced throwing power`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`
3. Line spacing: `1.6`
4. Position: below the "TOO HIGH" title with about 0.1 inches gap. Left edge at approximately **1.5 inches**.
5. To add bullet points: select the text, then click the **Lists** button in the toolbar and choose the bullet list option (a list with dots).

**44f — "TOO LOW" title (right sub-column):**
1. Add a text element. Type: `TOO LOW`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6` (Teal)
3. Position: right quarter of the container, approximately X: 7.5 inches, Y: 28.8 inches.

**44g — "TOO LOW" bullet list:**
1. Add a text element. Type:
   `Skip plating — bare spots in LCD zones`
   `Dull or hazy deposits`
   `Slow deposition — throughput loss`
   `Alloy composition shift`
2. Font: Inter Regular, Size: `16`, Color: `F0EDE8`
3. Line spacing: `1.6`
4. Apply bullet list formatting (same as 44e).
5. Position: below the "TOO LOW" title, same gap as the left column.

**44h — Group the callout:**
Select the container, section label, divider, both titles, and both bullet lists. Press **Ctrl+G**.

### Step 45 — Conversion + Cross-Reference callout (right 40%)

**45a — Callout container:**
1. Add a Rounded Rectangle.
   - **Width**: `9.25` inches
   - **Height**: `4.3` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 1 pt, color `3A4055` (Mid Slate)
   - **Corner radius**: `8`
2. Position: left edge at **14.25 inches**, top edge at **28.2 inches**.

**45b — "QUICK CONVERSIONS" title:**
1. Add a text element. Type: `QUICK CONVERSIONS`
2. Font: Barlow SemiBold, Size: `18`, Color: `E8A020` (Amber)
3. Position: inside the container, top-left, approximately 0.2 inches from the left edge and 0.15 inches from the top.

**45c — Conversion data (3 lines):**
1. Add a text element. Type (each formula on its own line):
   `ASF / 10 ~ ASD (exact: / 10.76)`
   `1 A/in² = 144 ASF`
   `1 A/m² = 0.0929 ASF`
2. Font: JetBrains Mono Regular, Size: `17`, Color: `F0EDE8`
3. Line spacing: Set to **1.6** (this gives approximately 8 pt spacing between lines)
4. Alignment: Left
5. Position: below the title with about 0.2 inches gap.

**45d — Cross-reference accent rule:**
1. Add a small vertical line:
   - Color: `2EC4B6` (Teal)
   - Thickness: `2` pt
   - Length: approximately **0.5 inches**
2. Position: left side of where the cross-reference text will go, approximately X: 14.6 inches, Y: approximately 30.5 inches (below the conversion data with about 0.25 inches gap).

**45e — Cross-reference text:**
1. Add a text element. Type:
   `See Poster #4 — Reading Your Hull Cell Panel — to visualize current density distribution across a test panel.`
2. Font: Inter Regular, Size: `15`, Color: `2EC4B6` (Teal)
3. Position: to the right of the accent rule, at approximately X: 14.9 inches. Width: approximately 8.0 inches.

**45f — Group the callout:**
Select the container, title, conversion data, accent rule, and cross-reference text. Press **Ctrl+G**.

### Step 46 — Group all of Zone 3
Select both callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Footer Band

This zone occupies Y: 32.8" to 36.0" (3.2 inches tall).

### Step 47 — Footer band background
1. Add a Rectangle (sharp corners).
   - **Width**: `24` inches
   - **Height**: `3.2` inches
   - **Fill**: `0D1020` (Deep Navy)
   - **No border**.
2. Position: left edge at 0 inches, top edge at **32.8 inches**.

### Step 48 — Disclaimer text
1. Add a text element. Type:
   `This poster is a technical reference tool. Current density ranges reflect general industry practice — consult your process supplier's TDS for product-specific recommendations. Not a substitute for process qualification.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: centered horizontally, top edge at approximately **33.0 inches**. Width: **23.0 inches**.

### Step 49 — Poster title (left)
1. Add a text element. Type: `Current Density Quick Reference Chart`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: left edge at 0.5 inches, top edge at approximately **34.0 inches**.

### Step 50 — Series name (center)
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, top edge at approximately **34.0 inches**.

### Step 51 — Logo placeholder (right)
1. Add a small Rounded Rectangle.
   - **Width**: `0.8` inches, **Height**: `0.4` inches
   - **Fill**: `3A4055` (Mid Slate), **No border**.
2. Position: right edge at approximately 23.4 inches, top at approximately 33.8 inches.
3. Add text inside: `[LOGO]`
4. Font: JetBrains Mono Regular, Size: `12`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center

### Step 52 — Version number
1. Add a text element. Type: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: right-aligned, right edge at approximately 23.4 inches, top at approximately **35.0 inches**.

### Step 53 — Group all of Zone 4
Select the Deep Navy rectangle, disclaimer, poster title, series name, logo placeholder, and version. Press **Ctrl+G**.

---

## Phase 6 — Final Review Checklist

Before exporting, unlock and ungroup all zones and verify each item. Re-group and re-lock after review.

### Text verification
- [ ] Headline reads: `CURRENT DENSITY` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Quick Reference Chart` in Barlow SemiBold, `#E8A020`
- [ ] Tagline reads: `Right range. Right deposit. Every time.` at 65% transparency
- [ ] Formula callout shows: `ASF = Amps / Area (ft²)` with Teal border
- [ ] Section label reads: `CURRENT DENSITY RANGES BY PROCESS`
- [ ] Column header row shows all 5 headers: PROCESS, RACK (ASF), BARREL (ASF), EFFICIENCY, NOTES
- [ ] 7 section headers are present: ZINC PLATING, COPPER PLATING, NICKEL PLATING, CHROMIUM PLATING, SILVER PLATING, TIN PLATING, OTHER PROCESSES
- [ ] 22 data rows are present (count them — 3 zinc + 2 copper + 4 nickel + 4 chrome + 2 silver + 2 tin + 5 other = 22)
- [ ] All em dashes "—" in Barrel column are present (not hyphens)
- [ ] All "N/A" entries are present for anodize rows
- [ ] "WHAT GOES WRONG" callout has both "TOO HIGH" (Coral) and "TOO LOW" (Teal) sub-columns with 4 bullets each
- [ ] "QUICK CONVERSIONS" box shows 3 conversion formulas
- [ ] Cross-reference to Poster #4 is present with Teal accent
- [ ] Footnote is present below the table
- [ ] Disclaimer, footer title, series name, LOGO placeholder, and version are all present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] All body text is `#F0EDE8` — not pure white
- [ ] Zinc rows have Teal accent bars
- [ ] Copper rows have Amber accent bars
- [ ] Nickel rows have Warm White accent bars
- [ ] Chrome rows have Coral accent bars
- [ ] Silver and Tin rows have Emerald accent bars
- [ ] Other rows have Mid Slate accent bars
- [ ] Section header backgrounds show subtle tinted colors (not solid accent)
- [ ] Footer band is `#0D1020` (Deep Navy)

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone
- [ ] Table rows are flush (no visible gaps between rows)
- [ ] All 5 columns are aligned consistently across all 22 data rows
- [ ] Zone 3 callouts sit side by side (not overlapping)
- [ ] No text is cut off or overlapping

### Readability check
- [ ] Zoom to 25% — headline and section headers readable
- [ ] Zoom to 50% — process names and section headers readable
- [ ] Zoom to 75% — CD values and efficiency percentages readable
- [ ] Zoom to 100% — notes column and footnote readable

---

## Phase 7 — Light Edition: Remap Instructions

### Step 54 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2. Rename "Light Edition" if possible.

### Step 55 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 56 — Remap all elements

Work through this table top to bottom, zone by zone:

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | Formula callout, What Goes Wrong box, Conversion box | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | Even-numbered data rows | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | Odd-numbered data rows | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Subheading, column headers, copper accents, conversion title | `#E8A020` | `#C8860A` |
| **Teal elements** | Formula callout border/title, zinc accents, "Too Low" title, cross-ref text | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | Silver and Tin accent bars, section headers | `#27AE60` | `#1E7A47` |
| **Coral elements** | Chrome accent bars, section header, "Too High" title | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Column header fill, Other accent bars, dividers | `#3A4055` | `#D0D4DE` |
| **Nickel accent (Warm White)** | Nickel accent bars and section header | `#F0EDE8` | `#1A1F2E` |

**Section header tinted backgrounds:** The pre-blended hex values for Dark edition section headers will not look right on the Light background. For each section header:
- Either recalculate: use the Light edition accent color at 15% opacity over `#F5F4F0`
- Or simpler method: change the section header background fill to a rectangle with the Light accent color, then set transparency to **85%** (which gives 15% opacity of the accent over the light background)

### Step 57 — Post-remap adjustments

1. **Footnote text**: At 60% opacity, verify readability on Off-White. If too faint, increase to **75%**.
2. **Disclaimer text**: At 50% opacity, verify readability. If too faint, increase to **65%**.
3. **Tagline**: At 65% opacity, verify readability on light background. Adjust if needed.
4. **Notes column**: At 80% opacity, verify readability. If too faint, increase to **90%**.
5. **Nickel section header**: The Warm White text remapped to `#1A1F2E` on the subtle light tinted background — verify it is clearly readable. If the tinted background is too subtle to see, that is fine — the accent bar provides the grouping signal.

---

## Phase 8 — Export Instructions

### Step 58 — Export the Dark edition (Page 1)

**58a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed**.
4. Select only **Page 1**.
5. Download and rename to: `Current-Density-Dark-24x36-Print.pdf`

**58b — Digital PDF, 24x36":**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks.
2. Select Page 1. Rename to: `Current-Density-Dark-Digital.pdf`

**58c — Print PDF, 18x24":**
1. 
2. Verify body text is at least 14 pt. Table text should remain legible.
3. Export as PDF Print (with crop marks and bleed).
4. Rename to: `Current-Density-Dark-18x24-Print.pdf`

### Step 59 — Export the Light edition (Page 2)

Repeat Step 58 for Page 2 with these filenames:
- `Current-Density-Light-24x36-Print.pdf`
- `Current-Density-Light-Digital.pdf`
- `Current-Density-Light-18x24-Print.pdf`

### Export file checklist
- [ ] `Current-Density-Dark-24x36-Print.pdf`
- [ ] `Current-Density-Dark-18x24-Print.pdf`
- [ ] `Current-Density-Dark-Digital.pdf`
- [ ] `Current-Density-Light-24x36-Print.pdf`
- [ ] `Current-Density-Light-18x24-Print.pdf`
- [ ] `Current-Density-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark), Nickel accent |
| `#E8A020` | Amber | Column headers, subheading, Copper accent |
| `#2EC4B6` | Teal | Zinc accent, formula border, cross-ref |
| `#27AE60` | Emerald | Silver and Tin accents |
| `#E05C5C` | Coral | Chrome accent, "Too High" callout |
| `#3A4055` | Mid Slate | Column header fill, Other accent, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout box fills |
| `#252B3D` | Alt Row | Even-numbered data rows |
| `#1E2740` | Zinc Tint | Zinc section header BG (blended) |
| `#2D2833` | Copper Tint | Copper section header BG (blended) |
| `#22262F` | Nickel Tint | Nickel section header BG (blended) |
| `#2D2434` | Chrome Tint | Chrome section header BG (blended) |
| `#1C2534` | Silver/Tin Tint | Silver/Tin section header BG (blended) |
| `#212536` | Other Tint | Other section header BG (blended) |
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
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0 (2026-04-03). All technical content production-ready. Watson flags are courtesy only. |
