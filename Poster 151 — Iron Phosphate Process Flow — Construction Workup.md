---
Project: Plating Posters Inc
Poster Number: 151
Title: "Iron Phosphate -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-01 technical reference (iron phosphate conversion coating)"
Technical Source: Industry-standard iron phosphate conversion coating process. Covers the complete process sequence from cleaning through seal/dry. Values are typical ranges for spray and immersion iron phosphate pretreatment lines.
Process Scope: Iron phosphate conversion coating -- complete process flow (6 stages, expandable to 8 in 5-stage systems)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IronPhosphate
  - ConversionCoating
  - ProcessFlow
  - ConstructionWorkup
  - ClusterCC01
---

# Poster #151 -- Construction Workup
## Iron Phosphate -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CC-01: Iron Phosphate Conversion Coating. It shows the complete process sequence at a glance -- every stage visible in one U-flow diagram. Iron phosphate is the workhorse paint pretreatment for general industrial, appliance, HVAC, and powder coat lines. This poster is the "map" that the other 7 posters (#152--#158) zoom into.

The poster must make one thing unmistakable: iron phosphate exists to make paint stick. It is NOT a standalone corrosion barrier. That message goes in the header and gets reinforced in the comparison callout.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Process flow diagram (Block B -- HERO):** Six rounded rectangles in a U-flow: top row L-to-R (stages 1--3), vertical connector, bottom row R-to-L (stages 4--6). Each box is color-coded by stage type. Arrows connect boxes sequentially. Additionally, a "configuration callout" shows 1-stage, 3-stage, and 5-stage variants.

2. **Parameter summary table (Block D):** A compact 6-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why Iron Phosphate?" comparison callout (Block E):** Two side-by-side callout boxes comparing iron phosphate vs. zinc phosphate positioning.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

6. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, and descriptions
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Coating stage, key parameter highlights |
| Teal | `#2EC4B6` | Cleaning & rinse stages |
| Emerald | `#27AE60` | Optimal ranges, seal/post-treatment |
| Coral | `#E05C5C` | Problems, defects, warnings |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 15.5" -- Zone 2/Zone 3 boundary
- 22.0" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Six-stage U-flow diagram (2 rows of 3)
  Block B2: Configuration callout (1-stage / 3-stage / 5-stage)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 6-row parameter table (one row per stage)

ZONE 4 -- IRON PHOSPHATE VS. ZINC PHOSPHATE (22.0"--28.5" / ~6.5" tall)
  Block E: Side-by-side comparison callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`) -- no separate fill needed.

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> IRON PHOSPHATE

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- Paint Pretreatment from Cleaning to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Iron phosphate makes paint stick. The lightest phosphate coating, the simplest chemistry, and the most forgiving line in the pretreatment world.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Six-Stage U-Flow Diagram**

Y: 3.8" to 12.0" (~8.2" tall). Two rows of three boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 7.0". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 7.3") -- Stages 1-3, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse | Box 2 | 8.25" | `#2EC4B6` (Teal) | Rinse |
| 3. Iron Phosphate Coat | Box 3 | 16.0" | `#E8A020` (Amber) | Coating |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~5.5")

**Vertical connector (Stage 3 to Stage 4):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 7.3" (bottom center Box 3)
- To: X: 19.5", Y: 8.5" (top center Box 4)

**Bottom Row (Y: 8.5" to 12.0") -- Stages 4-6, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 4. Rinse (Post-Coat) | Box 4 | 16.0" | `#2EC4B6` (Teal) | Rinse |
| 5. Seal Rinse | Box 5 | 8.25" | `#27AE60` (Emerald) | Post-Treatment |
| 6. Dry-Off Oven | Box 6 | 0.5" | `#E8A020` (Amber) | Drying |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Alkaline Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Alkaline Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Spray: 120--150 F | 2--4 oz/gal
Immersion: 130--160 F | 4--8 oz/gal
pH 9.5--11.5 | 1--5 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, stamping compounds`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `No silicate residue -- it kills the phosphate`

*Box 2 -- Rinse:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Coat` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient to 80 F` / `Overflow 1--3 gal/min`
- Purpose: `Remove cleaner drag-over`
- Check: `Conductivity < 500 uS/cm | pH < 9.0`

*Box 3 -- Iron Phosphate Coat:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Iron Phosphate`
- Parameters: `Spray: 100--140 F | pH 3.8--5.5` / `Immersion: 110--150 F | pH 3.5--5.0` / `1--5 min`
- Purpose: `Amorphous iron phosphate film for paint adhesion`
- Check: `Target: 40--60 mg/ft2 coating weight` (`#E8A020`)

*Box 4 -- Rinse (Post-Coat):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Coat`
- Parameters: `Ambient to 80 F` / `Clean overflow`
- Purpose: `Remove unreacted phosphate acid`
- Check: `CRITICAL: No hot water -- thermal shock damages film` (Coral `#E05C5C`)

*Box 5 -- Seal Rinse:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Seal Rinse`
- Parameters: `Non-chrome: 0.5--3% in DI water` / `Ambient to 100 F | 30 sec--2 min`
- Purpose: `Fill micropores, boost corrosion resistance`
- Check: `Chrome seals (CrO3) being phased out -- non-chrome is the standard`

*Box 6 -- Dry-Off Oven:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Dry-Off Oven`
- Parameters: `250--350 F (121--177 C)` / `5--15 min`
- Purpose: `Complete drying before paint`
- Check: `Do not exceed 400 F -- degrades phosphate film` (Coral `#E05C5C`)

---

**BLOCK B2 -- Configuration Callout**

Y: 12.3" to 13.5". Full width within margins.

Rounded rectangle, X: 0.5", Y: 12.3", W: 23.0", H: 1.2", fill `#1E2435`, radius 6, left accent 0.06" `#E8A020`.

Title: `LINE CONFIGURATIONS` -- Barlow SemiBold, 16 pt, `#E8A020`

Three inline items:

| Config | Stages | Note |
|---|---|---|
| 1-STAGE | Clean + Coat (combined) | Simplest. Lighter coating (15--40 mg/ft2). Small shops. |
| 3-STAGE | Clean --> Phosphate --> Seal | Most common industrial configuration. |
| 5-STAGE | Clean --> Rinse --> Phosphate --> Rinse --> Seal | Best quality. OEM paint specs. |

Config labels: Barlow SemiBold 14 pt `#E8A020`. Stage text: JetBrains Mono 12 pt `#F0EDE8`. Notes: Inter Regular 12 pt `#F0EDE8` at 60%.

---

**BLOCK C -- Stage Legend Strip**

Y: 13.8" to 14.6"

- Rounded rectangle, X: 0.5", Y: 13.8", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Coating & Drying` |
| `#27AE60` (Emerald) | `Seal / Post-Treatment` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 6-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Key Control (8.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alk Clean | pH 9.5--11.5, 2--8 oz/gal | 120--160 F | 1--5 min | Water-break-free; no silicate residue |
| 2. Rinse | Fresh water | Ambient--80 F | 30--60 sec | Conductivity < 500 uS/cm |
| 3. Fe Phosphate | pH 3.5--5.5, FA 0.5--3 pts | 100--150 F | 1--5 min | Coating wt 40--60 mg/ft2 |
| 4. Rinse (Post) | Fresh water | Ambient--80 F | 30--60 sec | No hot water; prompt transfer |
| 5. Seal Rinse | Non-chrome 0.5--3% in DI | Ambient--100 F | 30 sec--2 min | DI water < 50 uS/cm |
| 6. Dry-Off | -- | 250--350 F | 5--15 min | Do not exceed 400 F |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Iron Phosphate vs. Zinc Phosphate

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY IRON PHOSPHATE? -- IRON vs. ZINC PHOSPHATE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Iron Phosphate:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `IRON PHOSPHATE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Paint Prep Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Coating type | Amorphous (no crystal structure) |
| Coating weight | 20--80 mg/ft2 |
| Primary purpose | Paint adhesion |
| Corrosion resistance | Low (bare: 2--24 hr salt spray) |
| Conditioner required? | NO -- cleaning IS the conditioning |
| Chemistry complexity | Simple -- pH + free acid + accelerator |
| Temperature | 100--150 F |
| Substrates | Steel (primarily) |
| Cost | Low |
| Typical applications | Appliances, HVAC, powder coat, general industrial |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Simplest phosphate line. Lowest operating cost. Best fit when the paint does the protecting.` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Zinc Phosphate:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `ZINC PHOSPHATE` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `The Heavy-Duty Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Coating type | Crystalline (hopeite / phosphophyllite) |
| Coating weight | 150--1000+ mg/ft2 |
| Primary purpose | Paint adhesion + corrosion base |
| Corrosion resistance | High (painted: 500--1500+ hr SST) |
| Conditioner required? | YES -- Ti colloid is mandatory |
| Chemistry complexity | Complex -- multi-component, tight ratios |
| Temperature | 95--200 F |
| Substrates | Steel, aluminum, galvanized |
| Cost | High |
| Typical applications | Automotive OEM, military, aerospace |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Heavier coating, tighter control, higher cost -- justified when the spec demands it.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BARE SPOTS | Oil contamination, silicate residue, low acid | Improve cleaning; check cleaner for silicates |
| 2 | 6.33" | HEAVY/POWDERY COAT | Excess acid, time, or temp; dead accelerator | Reduce concentration/time/temp; replenish accelerator |
| 3 | 12.16" | FLASH RUST | Dwell between phosphate and rinse too long | Speed up line; move parts promptly |
| 4 | 18.0" | POOR PAINT ADHESION | Coating too light or too heavy; contaminated seal | Optimize to 40--60 mg/ft2; check seal rinse |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for iron phosphate conversion coating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; Products Finishing.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Iron Phosphate -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, six flow boxes, arrows, config callout, legend strip |
| Zone 3 - Parameter Table | Section label, 6-row table |
| Zone 4 - Fe vs Zn Phosphate | Section label, two comparison callouts |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout/flow box fills |
| `#252B3D` | `#E8E8F0` | Alternate rows, legend strip |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers, arrows |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

Stage badges: Verify text legibility on darkened fills -- may need `#F5F4F0` text.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Iron Phosphate Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Iron Phosphate Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Iron Phosphate Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Iron Phosphate Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Iron Phosphate Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Iron Phosphate Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Iron Phosphate cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#152--#158) zoom into each stage individually. The Fe vs. Zn phosphate comparison answers the most common pretreatment question: "Do I need zinc phosphate or is iron phosphate enough?" The answer is spec-dependent -- if the paint does the protecting and the spec allows it, iron phosphate wins on cost and simplicity.

The configuration callout (1-stage / 3-stage / 5-stage) is unique to this process and must be prominent. Many shops run a cleaner-coater (1-stage) and do not realize they have options.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #151 -- Construction Workup v1.0*
*2026-04-26*
