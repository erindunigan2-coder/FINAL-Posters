---
Project: Plating Posters Inc
Poster Number: 7
Title: "Metallic Contamination — Know Your Thresholds"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 7 — Metallic Contamination — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - MetallicContamination
  - v1
---

# Claude Chat Generation Prompt — Poster #7
## Metallic Contamination — Know Your Thresholds
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

This zone occupies the top 2.9 inches. Headline, subheading, and tagline on the left (~55%), "Most Dangerous" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element:
2. Select all placeholder text and type: `METALLIC CONTAMINATION`
3. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `96`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
4. Position: left edge at 0.5 inches, top edge at 0.5 inches.
5. Set text box width to approximately **12.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Know Your Thresholds`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `40`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.6 inches**.

### Step 8 — Place the tagline
1. Add a body text element: Type: `Contamination is always easier to prevent than to remove.`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: **65%**
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.3 inches**.

### Step 9 — Build the "Most Dangerous" callout box

**9a — Callout container:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Set properties:
   - **Width**: `9.5` inches
   - **Height**: `2.2` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 2 pt, color `E05C5C` (Coral)
   - **Corner radius**: `8`
3. Position: left edge at 13.5 inches (right edge at the 23.5-inch guide), top edge at 0.5 inches.

**9b — Callout title:**
1. Add a text element. Type: `MOST DANGEROUS CONTAMINANT PER BATH`
2. Font: Barlow SemiBold, Size: `18`, Color: `E05C5C` (Coral)
3. Position: inside the container, top-left area, approximately 0.2 inches from the left edge and 0.15 inches from the top.

**9c — Contaminant list:**
1. Add a text element. Copy-paste this text exactly (the spacing is intentional — it creates aligned columns):
   ```
   Nickel:      Cu > 3 ppm
   Acid copper:  Cr⁶⁺ > 2 ppm
   Hard chrome: Cl⁻ > 50 ppm
   Acid zinc:   Cr⁶⁺ > 1 ppm
   Passivation: Fe > 100 ppm
   ```
2. Font: JetBrains Mono Regular, Size: `15`, Color: `F0EDE8`
3. Line spacing: `1.5`
4. Position: inside the container, below the title with about 0.15 inches gap.

**9d — Closing line:**
1. Add a text element. Type: `These are the numbers that turn good parts into scrap.`
2. Font: Inter Medium, Size: `14`, Color: `E05C5C` (Coral)
3. Position: inside the container, below the list with about 0.1 inches gap.

**9e — Group the callout box:**
Select the container, title, list, and closing line. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: How Metals Get In (Tank Diagram)

This zone occupies Y: 2.9" to 7.9" (5.0 inches tall). It contains a section label and a tank diagram with 6 contamination source arrows.

### Step 11 — Section label
1. Add a text element. Type: `HOW CONTAMINATION ENTERS YOUR BATH`
2. Font: Barlow Condensed ExtraBold, Size: `26`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, top edge at **3.0 inches**. Width: **23.0 inches**.

### Step 12 — Build the tank

**12a — Tank rectangle:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**.
2. Set properties:
   - **Width**: `16.0` inches
   - **Height**: `3.0` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 2 pt, color `3A4055` (Mid Slate)
   - **Corner radius**: `8`
3. Position: centered horizontally (left edge at approximately 4.0 inches), top edge at approximately **4.5 inches**.

**12b — Electrolyte lines (inside the tank):**
1. Add a horizontal line inside the tank at about 30% from the top of the tank.
   - Color: `2EC4B6` (Teal), Thickness: `1` pt, Transparency: **20%**
   - Width: approximately 15.5 inches (just inside the tank walls).
2. Add a second horizontal line at about 60% from the top of the tank with the same settings.

These faint lines suggest the electrolyte surface inside the tank.

### Step 13 — Build Arrow 1 (template — then duplicate for the remaining 5)

Each arrow group consists of: a line with arrowhead, a label (bold), and a sub-label (smaller, faded). **Build Arrow 1 completely, group it, then duplicate 5 times and modify.**

**Arrow 1 — Impure anodes (top left, above tank):**

**13a — Draw the arrow:**
1. Click **Elements** > search **line** > select a basic straight line.
2. Set the line color to `E8A020` (Amber) and thickness to `2` pt.
3. Add an arrowhead: with the line selected, look for the line endpoint controls in the toolbar. Set one end to an arrowhead (the end pointing into the tank).
4. Position: start the line above and to the left of the tank (approximately X: 3.0", Y: 3.8"), angled so the arrowhead points down into the top of the tank.
5. Length: approximately 1.5 inches.

**13b — Arrow label:**
1. Add a text element. Type: `Impure anodes`
2. Font: Inter Medium, Size: `14`, Color: `E8A020` (Amber)
3. Position: next to the non-arrow end of the line (above/beside the tail).

**13c — Arrow sub-label:**
1. Add a text element. Type: `Lead, copper in anode material`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **70%**
3. Position: directly below the label.

**13d — Group this arrow:**
Select the line, label, and sub-label. Press **Ctrl+G**.

### Step 14 — Arrow 2: Drag-in from other tanks (top right, above tank)

1. Duplicate Arrow 1 group (**Ctrl+D**). Reposition to the top-right area above the tank (approximately X: 19.0", Y: 3.8").
2. Ungroup. Change:
   - Arrow color stays `E8A020` (Amber). Angle the arrowhead down into the tank from the right.
   - Label: `Drag-in from other tanks`
   - Sub-label: `Chrome, acid, organics carried on parts/racks`
3. Re-group.

### Step 15 — Arrow 3: Corroding equipment (left side of tank)

1. Duplicate Arrow 1 group. Reposition to the left of the tank (approximately X: 1.0", Y: 5.5").
2. Ungroup. Change:
   - Arrow color: `E05C5C` (Coral). Arrow points right, into the left wall of the tank.
   - Label: `Corroding equipment` — color `E05C5C`
   - Sub-label: `Heaters, pumps, tank linings`
3. Re-group.

### Step 16 — Arrow 4: Dissolving racks (right side of tank)

1. Duplicate Arrow 1 group. Reposition to the right of the tank (approximately X: 22.5", Y: 5.5").
2. Ungroup. Change:
   - Arrow color: `E05C5C` (Coral). Arrow points left, into the right wall of the tank.
   - Label: `Dissolving racks` — color `E05C5C`
   - Sub-label: `Iron, copper from steel/brass fixtures`
3. Re-group.

### Step 17 — Arrow 5: Dropped parts (inside tank, bottom center)

1. Duplicate Arrow 1 group. Reposition inside the tank, lower area (approximately X: 10.0", Y: 6.5").
2. Ungroup. Change:
   - Arrow color: `E05C5C` (Coral). Arrow points downward toward the tank floor.
   - Label: `Dropped parts` — color `E05C5C`
   - Sub-label: `Dissolve in bath over time`
3. Re-group.

### Step 18 — Arrow 6: Make-up water (bottom right, below tank)

1. Duplicate Arrow 1 group. Reposition to the lower-right area near the tank (approximately X: 20.0", Y: 7.0").
2. Ungroup. Change:
   - Arrow color: `E8A020` (Amber). Arrow points left into the tank from the lower right.
   - Label: `Make-up water` — color `E8A020`
   - Sub-label: `Iron, copper, calcium from municipal supply`
3. Re-group.

### Step 19 — Group all of Zone 2
Select the section label, tank rectangle, electrolyte lines, and all 6 arrow groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: Contamination Threshold Table (HERO)

This zone occupies Y: 7.9" to 25.9" (18.0 inches tall). This is the poster's primary reference payload — a 27-row master contamination table.

**Build strategy:** Build the column header row, one section header, and one data row as templates. Then duplicate for all remaining rows. This cuts build time by 70%.

### Step 20 — Section label
1. Add a text element. Type: `CONTAMINATION THRESHOLDS BY BATH TYPE`
2. Font: Barlow Condensed ExtraBold, Size: `28`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, top edge at **8.0 inches**. Width: **23.0 inches**.

### Step 21 — Build the column header row

**21a — Header row background:**
1. Add a Rounded Rectangle.
   - **Width**: `23.0` inches
   - **Height**: `0.50` inches
   - **Fill**: `3A4055` (Mid Slate)
   - **Corner radius**: `4` (top corners only if possible; all corners 4 is fine)
2. Position: left edge at 0.5 inches, top edge at **8.7 inches**.

**21b — Header text: CONTAMINANT**
1. Add a text element. Type: `CONTAMINANT`
2. Font: Barlow SemiBold, Size: `18`, Color: `F0EDE8`, Alignment: Left
3. Position: inside header row, left edge at approximately **0.7 inches**, vertically centered.
4. Width: approximately **4.0 inches**.

**21c — Header text: THRESHOLD**
1. Add a text element. Type: `THRESHOLD`
2. Same font, size, color. Alignment: Left.
3. Position: left edge at approximately **4.8 inches**. Width: **3.4 inches**.

**21d — Header text: EFFECT**
1. Add a text element. Type: `EFFECT`
2. Same font, size, color. Alignment: Left.
3. Position: left edge at approximately **8.3 inches**. Width: **6.8 inches**.

**21e — Header text: TREATMENT**
1. Add a text element. Type: `TREATMENT`
2. Same font, size, color. Alignment: Left.
3. Position: left edge at approximately **15.2 inches**. Width: **5.7 inches**.

### Step 22 — Build the first Section Header row (NICKEL BATHS)

**22a — Section header background:**
1. Add a Rectangle (sharp corners).
   - **Width**: `23.0` inches
   - **Height**: `0.45` inches
   - **Fill**: `3A4055` (Mid Slate)
2. Position: left edge at 0.5 inches, directly below the column header row (top edge at approximately **9.2 inches**).

**22b — Section header text:**
1. Add a text element. Type: `NICKEL BATHS`
2. Font: Barlow SemiBold, Size: `20`, Color: `E8A020` (Amber)
3. Position: left edge at approximately **0.8 inches**, vertically centered in the section header row.

**22c — Group the section header:**
Select the background and text. Press **Ctrl+G**.

### Step 23 — Build the first Data Row template (Row 1: Copper in Nickel)

**23a — Row background:**
1. Add a Rectangle.
   - **Width**: `23.0` inches
   - **Height**: `0.65` inches
   - **Fill**: `1A1F2E` (base row — same as page background)
2. Position: directly below the NICKEL BATHS section header.

**23b — Left accent bar:**
1. Add a Rectangle.
   - **Width**: `0.06` inches (approximately 4 pt)
   - **Height**: `0.65` inches
   - **Fill**: `E05C5C` (Coral — danger severity)
2. Position: flush against the left edge of the row background.

**23c — Contaminant text:**
1. Add a text element. Type: `Copper (Cu)`
2. Font: Inter Medium, Size: `16`, Color: `F0EDE8`, Alignment: Left
3. Position: left edge at approximately **0.7 inches**, vertically centered.
4. Width: approximately **4.0 inches**.

**23d — Threshold text:**
1. Add a text element. Type: `>3-5 ppm`
2. Font: JetBrains Mono Regular, Size: `16`, Color: `E05C5C` (Coral — matches severity)
3. Position: left edge at approximately **4.8 inches**, vertically centered.
4. Width: approximately **3.4 inches**.

**23e — Effect text:**
1. Add a text element. Type: `Dark LCD deposits; poor adhesion`
2. Font: Inter Regular, Size: `15`, Color: `F0EDE8`
3. Position: left edge at approximately **8.3 inches**, vertically centered.
4. Width: approximately **6.8 inches**.

**23f — Treatment text:**
1. Add a text element. Type: `Dummy at 2-5 ASF`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`
3. Position: left edge at approximately **15.2 inches**, vertically centered.
4. Width: approximately **5.7 inches**.

**23g — Group the data row:**
Select the background, accent bar, and all 4 text elements. Press **Ctrl+G**.

### Step 24 — Build Row 2: Zinc in Nickel (Duplicate and Modify)

1. Duplicate Row 1 group (**Ctrl+D**). Reposition directly below Row 1 (flush, no gap).
2. Ungroup. Make these changes:
   - **Row background fill**: `252B3D` (Alt Row)
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: `Zinc (Zn)`
   - **Threshold**: `>20-50 ppm` — color `E05C5C`
   - **Effect**: `White/dark LCD; shiny black streaks`
   - **Treatment**: `Dummy at 2-5 ASF; pH 5.5`
3. Re-group.

### Step 25 — Row 3: Iron in Nickel

1. Duplicate Row 1 group. Reposition below Row 2.
2. Ungroup. Changes:
   - **Row background fill**: `1A1F2E` (base)
   - **Left accent bar fill**: `E8A020` (Amber — warning)
   - **Contaminant**: `Iron (Fe)`
   - **Threshold**: `>50-150 ppm` — color `E8A020` (Amber)
   - **Effect**: `Speckling; roughness; discoloration`
   - **Treatment**: Copy-paste: `pH 5.0-5.5 + H₂O₂ → filter`
3. Re-group.

### Step 26 — Row 4: Lead in Nickel

1. Duplicate Row 2 (alt template). Reposition below Row 3.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: `Lead (Pb)`
   - **Threshold**: `>1-5 ppm` — color `E05C5C`
   - **Effect**: `Dark streaks; brittleness`
   - **Treatment**: `Carbon + electrolytic`
3. Re-group.

### Step 27 — Row 5: Chromium in Nickel

1. Duplicate Row 1 (base template). Reposition below Row 4.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Chromium (Cr⁶⁺)`
   - **Threshold**: `>5-10 ppm` — color `E05C5C`
   - **Effect**: `Brightness loss; pitting`
   - **Treatment**: `Dummy at 1-2 ASF`
3. Re-group.

### Step 28 — Row 6: Aluminum in Nickel

1. Duplicate Row 2 (alt). Reposition below Row 5.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Aluminum (Al)`
   - **Threshold**: `>60 ppm` — color `E8A020`
   - **Effect**: `Reduced limiting CD; rough`
   - **Treatment**: `Cannot remove — dilute`
3. Re-group.

### Step 29 — Row 7: Cadmium in Nickel

1. Duplicate Row 1 (base). Reposition below Row 6.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: `Cadmium (Cd)`
   - **Threshold**: `>1-2 ppm` — color `E05C5C`
   - **Effect**: `Brittleness; adhesion failure`
   - **Treatment**: `Dummy; prevent ingress`
3. Re-group.

### Step 30 — ACID COPPER BATHS section header

1. Duplicate the NICKEL BATHS section header group. Reposition below Row 7.
2. Ungroup. Changes:
   - **Text**: `ACID COPPER BATHS`. Color: `2EC4B6` (Teal)
3. Re-group.

### Step 31 — Row 8: Iron in Acid Copper

1. Duplicate Row 2 (alt). Reposition below ACID COPPER header.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Iron (Fe)`
   - **Threshold**: `>500-1000 ppm` — color `E8A020`
   - **Effect**: `Reduced conductivity; rough`
   - **Treatment**: `Dilute; prevent ingress`
3. Re-group.

### Step 32 — Row 9: Zinc in Acid Copper

1. Duplicate Row 1 (base). Reposition below Row 8.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Zinc (Zn)`
   - **Threshold**: `>25 ppm` — color `E8A020`
   - **Effect**: `Brittle, brassy deposits`
   - **Treatment**: `Dummy at 2 ASF`
3. Re-group.

### Step 33 — Row 10: Tin in Acid Copper

1. Duplicate Row 2 (alt). Reposition below Row 9.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Tin (Sn)`
   - **Threshold**: `>60 ppm` — color `E8A020`
   - **Effect**: `Rough, dark deposits`
   - **Treatment**: `Dummy plate`
3. Re-group.

### Step 34 — Row 11: Chromium in Acid Copper

1. Duplicate Row 1 (base). Reposition below Row 10.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Chromium (Cr⁶⁺)`
   - **Threshold**: `>2-5 ppm` — color `E05C5C`
   - **Effect**: `Skip plating; dull deposits`
   - **Treatment**: Copy-paste: `Na₂S₂O₅ → filter`
3. Re-group.

### Step 35 — Row 12: Chloride in Acid Copper

1. Duplicate Row 2 (alt). Reposition below Row 11.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Chloride (Cl⁻)`
   - **Threshold**: `>50-80 ppm` — color `E05C5C`
   - **Effect**: `Pitting; anode corrosion`
   - **Treatment**: `Prevent drag-in; no removal`
3. Re-group.

### Step 36 — HARD CHROME BATHS section header

1. Duplicate the NICKEL BATHS section header group. Reposition below Row 12.
2. Ungroup. Changes:
   - **Text**: `HARD CHROME BATHS`. Color: `E05C5C` (Coral)
3. Re-group.

### Step 37 — Row 13: Iron in Hard Chrome

1. Duplicate Row 1 (base). Reposition below HARD CHROME header.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Iron (Fe)`
   - **Threshold**: `>5 g/L` — color `E8A020`
   - **Effect**: `Roughness; reduced coverage`
   - **Treatment**: `Dummy at low CD (limited)`
3. Re-group.

### Step 38 — Row 14: Copper in Hard Chrome

1. Duplicate Row 2 (alt). Reposition below Row 13.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Copper (Cu)`
   - **Threshold**: `>2 g/L` — color `E8A020`
   - **Effect**: `Dark deposits; roughness`
   - **Treatment**: `Dummy at low CD`
3. Re-group.

### Step 39 — Row 15: Trivalent Chromium in Hard Chrome

1. Duplicate Row 1 (base). Reposition below Row 14.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Trivalent Cr (Cr³⁺)`
   - **Threshold**: `>2-3% of total` — color `E05C5C`
   - **Effect**: `Poor coverage; dull`
   - **Treatment**: `Porous pot electrolysis`
3. Re-group.

### Step 40 — Row 16: Chloride in Hard Chrome

1. Duplicate Row 2 (alt). Reposition below Row 15.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Chloride (Cl⁻)`
   - **Threshold**: `>50 ppm` — color `E05C5C`
   - **Effect**: `Severe pitting; etching`
   - **Treatment**: `Low area/high CD; prevent`
3. Re-group.

### Step 41 — ACID ZINC BATHS section header

1. Duplicate the NICKEL BATHS section header group. Reposition below Row 16.
2. Ungroup. Changes:
   - **Text**: `ACID ZINC BATHS`. Color: `27AE60` (Emerald)
3. Re-group.

### Step 42 — Row 17: Iron in Acid Zinc

1. Duplicate Row 1 (base). Reposition below ACID ZINC header.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E8A020` (Amber)
   - **Contaminant**: `Iron (Fe)`
   - **Threshold**: `>25-50 ppm` — color `E8A020`
   - **Effect**: `Dark; roughness; poor brightness`
   - **Treatment**: Copy-paste: `H₂O₂ at pH 5.5-6.0 → filter`
3. Re-group.

### Step 43 — Row 18: Copper in Acid Zinc

1. Duplicate Row 2 (alt). Reposition below Row 17.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: `Copper (Cu)`
   - **Threshold**: `>10-20 ppm` — color `E05C5C`
   - **Effect**: `Dark/reddish LCD; immersion`
   - **Treatment**: `Dummy at 2-5 ASF`
3. Re-group.

### Step 44 — Row 19: Lead in Acid Zinc

1. Duplicate Row 1 (base). Reposition below Row 18.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: `Lead (Pb)`
   - **Threshold**: `>2-5 ppm` — color `E05C5C`
   - **Effect**: `Dark streaks; brittleness`
   - **Treatment**: `Dummy; prevent ingress`
3. Re-group.

### Step 45 — Row 20: Chromium in Acid Zinc

1. Duplicate Row 2 (alt). Reposition below Row 19.
2. Ungroup. Changes:
   - **Left accent bar fill**: `E05C5C` (Coral)
   - **Contaminant**: Copy-paste: `Chromium (Cr⁶⁺)`
   - **Threshold**: `>1-2 ppm` — color `E05C5C`
   - **Effect**: `Skip plating; poor coverage`
   - **Treatment**: Copy-paste: `Na₂S₂O₅ → filter`
3. Re-group.

### Step 46 — Group all of Zone 3
Select the section label, column header row, all 4 section headers, all 20 data rows. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Detection + Treatment

This zone occupies Y: 25.9" to 30.9" (5.0 inches tall). Detection methods table on the left (40%), three treatment callout boxes on the right (60%).

### Step 47 — Detection Methods section label
1. Add a text element. Type: `HOW TO DETECT`
2. Font: Barlow Condensed ExtraBold, Size: `20`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 26.0".

### Step 48 — Detection table header row

**48a — Header background:**
1. Add a Rectangle.
   - **Width**: `8.5` inches
   - **Height**: `0.40` inches
   - **Fill**: `3A4055` (Mid Slate)
2. Position: X: 0.5", top edge at approximately **26.5 inches**.

**48b — Header text:**
1. Add text: `METHOD` — Barlow SemiBold, `15` pt, `F0EDE8`. Position: X: 0.7", vertically centered.
2. Add text: `USE` — same font/size/color. Position: X: 4.3", vertically centered.

### Step 49 — Detection table data rows

Build Row 1 as a template, then duplicate for Rows 2-5.

**Row 1 — Atomic Absorption:**
1. Add a Rectangle. Width: `8.5"`. Height: `0.55"`. Fill: `1A1F2E` (base). Position below header row.
2. Add text: `Atomic Absorption (AA)` — Inter Medium, `14` pt, `F0EDE8`. Position: X: 0.7".
3. Add text: `Gold standard — sub-ppm sensitivity` — Inter Regular, `14` pt, `F0EDE8`. Position: X: 4.3".
4. Group the row.

**Row 2 — ICP-OES:**
1. Duplicate Row 1. Reposition below.
2. Ungroup. Change fill to `252B3D` (alt).
3. Method: `ICP-OES`. Use: `Multiple metals simultaneously`.
4. Re-group.

**Row 3 — Hull cell:**
1. Duplicate Row 1. Reposition below Row 2.
2. Fill: `1A1F2E` (base).
3. Method: `Hull cell (low CD)`. Use: `Shop-floor screening — visual`.
4. Re-group.

**Row 4 — Colorimetric kits:**
1. Duplicate Row 2. Reposition below Row 3.
2. Fill: `252B3D` (alt).
3. Method: `Colorimetric kits`. Use: `Quick field check (5-50 ppm)`.
4. Re-group.

**Row 5 — Dummying response:**
1. Duplicate Row 1. Reposition below Row 4.
2. Fill: `1A1F2E` (base).
3. Method: `Dummying response`. Use: `Diagnostic — "does dummying help?"`.
4. Re-group.

### Step 50 — Treatment Quick Reference section (right 60%)

Build one callout box as a template, then duplicate twice.

**Box 1 — Dummy Plating (Emerald accent):**

**50a — Container:**
1. Add a Rounded Rectangle.
   - Width: `4.4"`. Height: `1.35"`.
   - Fill: `1E2435` (Dark Callout).
   - Border: 1.5 pt, `27AE60` (Emerald).
   - Corner radius: `6`.
2. Position: X: 9.75", Y: 26.0".

**50b — Title:**
1. Add text: `DUMMY PLATING`
2. Font: Barlow SemiBold, `15` pt, `27AE60` (Emerald)
3. Position: inside the container, top area with 0.1" padding.

**50c — Body:**
1. Add text: `Corrugated mild steel cathodes at 2-5 ASF for 4-24 hours. Contaminant metals plate out preferentially at low CD. Monitor by Hull cell.`
2. Font: Inter Regular, `13` pt, `F0EDE8`. Line spacing: `1.3`.
3. Position: below the title, inside container. Width: approximately 4.0".

**50d — Group Box 1:**
Select container, title, and body. Press **Ctrl+G**.

**Box 2 — Iron Removal (Amber accent):**

1. Duplicate Box 1 group. Reposition: X: 9.75", Y: 27.5" (below Box 1 with 0.15" gap).
2. Ungroup. Changes:
   - Border color: `E8A020` (Amber)
   - Title: `IRON REMOVAL (NICKEL BATHS)` — color `E8A020`
   - Body: Copy-paste: `Raise pH to 5.0-5.5. Add H₂O₂ (30%) at 0.1-0.3 mL/L. Iron precipitates as Fe(OH)₃. Filter through 1 um. Lower pH to operating range.`
3. Re-group.

**Box 3 — Carbon Treatment (Teal accent):**

1. Duplicate Box 1 group. Reposition: X: 9.75", Y: 29.0" (below Box 2 with 0.15" gap).
2. Ungroup. Changes:
   - Border color: `2EC4B6` (Teal)
   - Title: `CARBON TREATMENT` — color `2EC4B6`
   - Body: `2-5 g/L powdered activated carbon. Mix, settle 2-4 hrs, filter through 1 um. Removes organic breakdown products alongside metallic contamination.`
3. Re-group.

**Additional treatment boxes (wider layout):**

The three boxes above are stacked vertically in the right 60% of Zone 4. If you have additional horizontal space, you may widen them to fill from X: 9.75" to X: 23.5" (width: 13.75"). The height may need to shrink slightly. Adjust as needed to fit all three within the 5.0" zone height.

### Step 51 — Group all of Zone 4
Select the detection section label, detection table (header + 5 rows), and all 3 treatment callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Prevention Strip

This zone occupies Y: 30.9" to 32.4" (1.5 inches tall).

### Step 52 — Prevention strip background
1. Add a Rounded Rectangle.
   - **Width**: `23.0` inches
   - **Height**: `1.2` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Corner radius**: `6`
2. Position: X: 0.5", Y: 31.0".

### Step 53 — Prevention strip title
1. Add a text element. Type: `PREVENTION IS CHEAPER THAN TREATMENT`
2. Font: Barlow SemiBold, Size: `16`, Color: `27AE60` (Emerald), Alignment: Left
3. Position: X: 0.8", Y: 31.1".

### Step 54 — Prevention checklist items

Build 6 items arranged horizontally across the strip, each consisting of a checkmark icon + text label. Space them evenly (~3.6" per item).

**For each item:**
1. In **Elements**, search **checkmark**. Select a simple checkmark icon. Set size to `0.4"` x `0.4"`. Set color to `27AE60` (Emerald).
2. Add a text element next to the icon with the label text. Font: Inter Regular, `13` pt, `F0EDE8`.

**Item positions and labels (approximate X positions for the checkmark icon):**

| # | X position | Label text |
|---|---|---|
| 1 | 0.8" | `Bag your anodes` |
| 2 | 4.5" | `Maintain your racks` |
| 3 | 8.2" | `Rinse thoroughly` |
| 4 | 11.5" | `Test monthly (Ni) / quarterly (Cu, Zn)` |
| 5 | 16.5" | `Use pure water (DI/RO)` |
| 6 | 20.2" | `Use pure anodes` |

If the exact checkmark icon is not available, use a small Emerald circle (0.15" diameter) as a bullet instead.

### Step 55 — Group all of Zone 5
Select the strip background, title, and all 6 checkmark-label pairs. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 56 — Footer band background
1. Add a Rectangle (sharp corners).
   - **Width**: `24` inches
   - **Height**: `3.6` inches
   - **Fill**: `0D1020` (Deep Navy)
   - **No border**.
2. Position: left edge at 0 inches, top edge at **32.4 inches**.

### Step 57 — Disclaimer text
1. Add a text element. Type:
   `This poster presents industry-typical contamination thresholds. Specific limits vary by vendor formulation — always check the product TDS. Analysis by AA or ICP is the authoritative method for confirming contamination levels.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: centered horizontally, top edge at approximately **32.6 inches**. Width: **23.0 inches**.

### Step 58 — Poster title (left)
1. Add a text element. Type: `Metallic Contamination — Know Your Thresholds`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: left edge at 0.5 inches, top edge at approximately **34.0 inches**.

### Step 59 — Series name (center)
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Transparency: **70%**, Alignment: Center
3. Position: centered horizontally, top edge at approximately **34.0 inches**.

### Step 60 — Logo placeholder (right)
1. Add a small Rounded Rectangle.
   - **Width**: `0.8` inches, **Height**: `0.4` inches
   - **Fill**: `3A4055` (Mid Slate). **No border**.
2. Position: X: 22.6", Y: 33.8".
3. Add text inside: `[LOGO]`
4. Font: JetBrains Mono Regular, Size: `12`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center

### Step 61 — Version number
1. Add a text element. Type: `v1.0 — 2026`
2. Font: JetBrains Mono Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**
3. Position: X: 22.6", Y: 35.2".

### Step 62 — Group all of Zone 6
Select the Deep Navy rectangle, disclaimer, poster title, series name, logo placeholder, and version. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

Before exporting, unlock and ungroup all zones and verify each item. Re-group and re-lock after review.

### Text verification
- [ ] Headline reads: `METALLIC CONTAMINATION` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Know Your Thresholds` in Barlow SemiBold, `#E8A020`
- [ ] Tagline reads: `Contamination is always easier to prevent than to remove.` at 65% transparency
- [ ] "Most Dangerous" callout has Coral border and all 5 bath entries
- [ ] Section label reads: `HOW CONTAMINATION ENTERS YOUR BATH`
- [ ] Tank diagram has 6 arrow groups with labels and sub-labels
- [ ] Section label reads: `CONTAMINATION THRESHOLDS BY BATH TYPE`
- [ ] Column header shows: CONTAMINANT | THRESHOLD | EFFECT | TREATMENT
- [ ] 4 section headers present: NICKEL BATHS (Amber), ACID COPPER BATHS (Teal), HARD CHROME BATHS (Coral), ACID ZINC BATHS (Emerald)
- [ ] 20 data rows present (7 nickel + 5 acid copper + 4 hard chrome + 4 acid zinc = 20)
- [ ] Detection table has 5 rows
- [ ] 3 treatment callout boxes present: Dummy Plating (Emerald), Iron Removal (Amber), Carbon Treatment (Teal)
- [ ] Prevention strip has 6 checkmark items
- [ ] Disclaimer, footer title, series name, LOGO placeholder, and version all present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] All body text is `#F0EDE8` — not pure white
- [ ] Danger severity rows have Coral left accent bars and Coral threshold text
- [ ] Warning severity rows have Amber left accent bars and Amber threshold text
- [ ] Section headers use correct accent colors per bath type
- [ ] Treatment boxes have correct accent borders (Emerald, Amber, Teal)
- [ ] Prevention strip checkmarks are Emerald
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone
- [ ] Table rows are flush (no visible gaps)
- [ ] All 4 columns are aligned consistently across all 20 data rows
- [ ] Detection table and treatment boxes sit side by side (not overlapping)
- [ ] Tank diagram is centered with arrows pointing into the tank
- [ ] No text is cut off or overlapping

### Readability check
- [ ] Zoom to 25% — headline, section headers, and tank labels readable
- [ ] Zoom to 50% — contaminant names and section headers readable
- [ ] Zoom to 75% — threshold values and effect text readable
- [ ] Zoom to 100% — treatment text and disclaimer readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 63 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2. Rename "Light Edition" if possible.

### Step 64 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 65 — Remap all elements

Work through this table top to bottom, zone by zone:

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | "Most Dangerous" callout, tank fill, treatment boxes, prevention strip, detection table | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | Even-numbered data rows | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | Odd-numbered data rows | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Nickel section header text, arrow labels, Iron removal border, Amber threshold text, Amber accent bars | `#E8A020` | `#C8860A` |
| **Teal elements** | Acid Copper section header text, callout borders, Carbon treatment border, electrolyte lines | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | Acid Zinc section header text, Dummy plating border, prevention checkmarks, prevention title | `#27AE60` | `#1E7A47` |
| **Coral elements** | Hard Chrome section header text, "Most Dangerous" border/title/closing, Coral threshold text, Coral accent bars | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Column header fills, section header fills, tank border, dividers | `#3A4055` | `#D0D4DE` |

### Step 66 — Post-remap adjustments

1. **Severity-colored threshold text**: The darkened Coral (`#B83E3E`) and Amber (`#C8860A`) on `#F5F4F0` and `#E8E8F0` backgrounds should pass WCAG AA. Verify visually — if any threshold text is hard to read, darken it further by 10%.
2. **Footnote and disclaimer text**: At 50% opacity on Off-White, verify readability. If too faint, increase to **65%**.
3. **Tagline**: At 65% opacity, verify readability on light background. Increase to **80%** if needed.
4. **Arrow sub-labels**: At 70% opacity, verify readability. Increase to **85%** if needed.
5. **Prevention checkmark items**: Verify darkened Emerald checkmarks are visible against `#ECEEF4` strip background.

---

## Phase 10 — Export Instructions

### Step 67 — Export the Dark edition (Page 1)

**67a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed**.
4. Select only **Page 1**.
5. Download and rename to: `Metallic-Contamination-Dark-24x36-Print.pdf`

**67b — Digital PDF, 24x36":**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks.
2. Select Page 1. Rename to: `Metallic-Contamination-Dark-Digital.pdf`

**67c — Print PDF, 18x24":**
1. 
2. Verify body text is at least 14 pt.
3. Export as PDF Print (with crop marks and bleed).
4. Rename to: `Metallic-Contamination-Dark-18x24-Print.pdf`

### Step 68 — Export the Light edition (Page 2)

Repeat Step 67 for Page 2 with these filenames:
- `Metallic-Contamination-Light-24x36-Print.pdf`
- `Metallic-Contamination-Light-Digital.pdf`
- `Metallic-Contamination-Light-18x24-Print.pdf`

### Export file checklist
- [ ] `Metallic-Contamination-Dark-24x36-Print.pdf`
- [ ] `Metallic-Contamination-Dark-18x24-Print.pdf`
- [ ] `Metallic-Contamination-Dark-Digital.pdf`
- [ ] `Metallic-Contamination-Light-24x36-Print.pdf`
- [ ] `Metallic-Contamination-Light-18x24-Print.pdf`
- [ ] `Metallic-Contamination-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light) |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | Nickel section, arrow labels, Amber severity |
| `#2EC4B6` | Teal | Acid Copper section, callout borders, Carbon treatment |
| `#27AE60` | Emerald | Acid Zinc section, Dummy plating, prevention strip |
| `#E05C5C` | Coral | Hard Chrome section, danger severity, "Most Dangerous" |
| `#3A4055` | Mid Slate | Column headers, section headers, tank border, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout fills, tank fill, prevention strip, treatment boxes |
| `#252B3D` | Alt Row | Even-numbered data rows |
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
