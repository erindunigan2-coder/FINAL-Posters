---
Project: Plating Posters Inc
Poster Number: 631
Title: "Austempering -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering)"
Technical Source: Industry-standard austempering (isothermal bainite transformation). Covers complete 7-stage sequence from part prep through inspection. Values are typical ranges from ASM Handbook and AMS 2759. No temper stage -- bainite is the final structure.
Process Scope: Austempering -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - ProcessFlow
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #631 -- Construction Workup
## Austempering -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for HT-09: Austempering. It shows the complete 7-stage process sequence at a glance -- every stage visible in one U-flow diagram. Austempering is the isothermal alternative to conventional quench-and-temper -- the part goes into a molten salt bath above the martensite start temperature and STAYS there until austenite transforms to bainite. No temper needed. Less distortion. Better toughness at equivalent hardness. This poster is the "map" that the remaining 8 posters (#632--#639) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (why austempering vs. conventional Q&T?), and a failure-mode quick-hit strip. Dense but scannable -- the heat treater's wall reference for the entire line.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters.

3. **"Why Austempering?" comparison callout (Block E):** Two side-by-side callout boxes comparing austempering (bainite) vs. conventional Q&T (martensite).

4. **Failure-mode quick-hit strip (Block F):** A horizontal strip of 4 common failures with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

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
- **JetBrains Mono Regular** -- all parameter data, temperatures, times, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Heat/austenitizing stages, warning headers, key numbers |
| Teal | `#2EC4B6` | Transfer and cooling stages, structural positives |
| Emerald | `#27AE60` | Salt bath / transformation stages (the hero step) |
| Coral | `#E05C5C` | Problems, defects, safety callouts |
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
  Block B: Seven-stage U-flow diagram (top row 4, bottom row 3)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 7-row parameter table (one row per stage)

ZONE 4 -- WHY AUSTEMPERING? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Austempering (bainite) vs. Conventional Q&T (martensite) side-by-side

ZONE 5 -- FAILURE MODE QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-failure strip with one-line fixes

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

> AUSTEMPERING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 7 Stages from Austenitize to Inspect

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Isothermal transformation to bainite. Same hardness as tempered martensite -- better toughness, less distortion, no temper required.

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

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row of four boxes, bottom row of three boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Preparation | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Load Furnace | Box 2 | 6.0" | `#2EC4B6` (Teal) | Loading |
| 3. Austenitize | Box 3 | 11.5" | `#E8A020` (Amber) | Heat Cycle |
| 4. Transfer to Salt | Box 4 | 17.0" | `#E05C5C` (Coral) | Critical Transfer |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 8.3" (bottom center Box 4)
- To: X: 19.5", Y: 9.5" (top center Box 5)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-7, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Isothermal Hold | Box 5 | 17.0" | `#27AE60` (Emerald) | Transformation (HERO) |
| 6. Air Cool | Box 6 | 11.5" | `#2EC4B6` (Teal) | Cooling |
| 7. Inspect & QA | Box 7 | 6.0" | `#E8A020` (Amber) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Preparation:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Clean: oil, grease, scale-free
Stress relieve if required
Verify steel grade & section
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove contaminants that block uniform heat transfer`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Section thickness vs. hardenability -- max ~0.5" plain carbon`

*Box 2 -- Load Furnace:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Load Furnace`
- Parameters: `HT alloy fixtures` / `Min 0.25" part spacing` / `Quench orientation planned`
- Purpose: `Ensure uniform heating and unobstructed transfer path to salt bath`
- Check: `Fixture must survive 1500+ F without embrittlement`

*Box 3 -- Austenitize:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Austenitize`
- Parameters: `1500--1650 F (815--900 C)` / `Hold: 30--90 min` / `Atmosphere: endo or N2`
- Purpose: `Transform microstructure fully to austenite (FCC)`
- Check: `Incomplete austenitization = mixed structures = inconsistent results`

*Box 4 -- Transfer to Salt Bath:*
- Badge: `STAGE 4`, fill `#E05C5C`
- Name: `Transfer to Salt`
- Parameters: `RAPID -- 10 sec max` / `Avoid pearlite nose on TTT` / `Parts at 1500+ F`
- Purpose: `Move parts into isothermal salt bath before pearlite begins`
- Check: `CRITICAL: Slow transfer = pearlite = scrap` (Coral `#E05C5C`)

*Box 5 -- Isothermal Hold (THE HERO STEP):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Isothermal Hold` / Subtitle: `Salt Bath`
- Parameters: `Salt: 400--700 F (205--370 C)` / `Hold: 30 min -- 4 hr` / `NaNO3/NaNO2/KNO3 blend`
- Purpose: `Hold at constant temp until austenite transforms completely to bainite`
- Check: `Incomplete hold = retained austenite = martensite on cooling (BAD)`

*Box 6 -- Air Cool:*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Air Cool`
- Parameters: `Still air to room temp` / `No quench required` / `Wash to remove salt residue`
- Purpose: `Bainite is already formed -- cooling is non-critical`
- Check: `No temper needed -- bainite is the final structure`

*Box 7 -- Inspect & QA:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Inspect & QA`
- Parameters: `Hardness: Rockwell C` / `Microstructure: nital etch` / `Dimensional check`
- Purpose: `Confirm bainite, verify hardness range, check distortion`
- Check: `Any pearlite in micro = process failure`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep & Cooling` |
| `#E8A020` (Amber) | `Heat Cycle & QA` |
| `#27AE60` (Emerald) | `Isothermal Transformation` |
| `#E05C5C` (Coral) | `Critical Transfer / Caution` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 7-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Medium (4.5") | Temperature (4.0") | Time (3.0") | Key Control (8.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Medium | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Part Prep | Solvent / alkaline wash | Ambient | -- | Section thickness vs. hardenability |
| 2. Load | HT alloy fixtures | -- | -- | 0.25" min spacing; quench path clear |
| 3. Austenitize | Endo gas or N2 atmosphere | 1500--1650 F | 30--90 min | Full transformation to austenite |
| 4. Transfer | Open air (rapid) | 1500+ F to salt | < 10 sec | Must beat the pearlite nose |
| 5. Isothermal Hold | Molten salt (NaNO3/NaNO2/KNO3) | 400--700 F | 30 min -- 4 hr | Complete bainite transformation |
| 6. Air Cool | Still air | Salt temp to ambient | Varies | Wash salt residue; no temper needed |
| 7. Inspect & QA | -- | -- | -- | HRC, microstructure, dimensional |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Austempering? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY AUSTEMPERING? -- BAINITE VS. MARTENSITE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Austempering (Bainite):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `AUSTEMPERING (BAINITE)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Isothermal Alternative` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Final structure | Bainite (lower or upper) |
| Hardness range | 30--55 HRC (temperature dependent) |
| Toughness | EXCELLENT -- superior to Q&T at same hardness |
| Ductility | Significantly better than martensite |
| Distortion | 60--90% less than conventional quench |
| Temper required | NO -- bainite is already tempered |
| Section limit | ~0.5" plain carbon; 1.0--1.5" alloy |
| Quench medium | Molten salt 400--700 F |
| Best for | Springs, clips, chain, thin sections, ADI |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Same hardness as tempered martensite -- but tougher, more ductile, and less distortion` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Conventional Quench & Temper (Martensite):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CONVENTIONAL Q&T (MARTENSITE)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Baseline Process` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Final structure | Tempered martensite |
| Hardness range | 28--63 HRC (temper dependent) |
| Toughness | Good -- but less than bainite at same HRC |
| Ductility | Lower than bainite |
| Distortion | Baseline (100%) |
| Temper required | YES -- mandatory; martensite is brittle as-quenched |
| Section limit | No practical limit with proper hardenability |
| Quench medium | Oil, water, or polymer |
| Best for | Broad range; large sections; maximum hardness |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `More versatile across section sizes -- but higher distortion and temper is mandatory` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 5 -- Failure Mode Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON FAILURES

---

**BLOCK F -- Four Failure Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PEARLITE IN MICRO | Transfer too slow; section too thick for hardenability | Use higher-alloy steel; rapid transfer; increase salt agitation |
| 2 | 6.33" | RETAINED AUSTENITE | Hold time too short; transformation incomplete | Extend isothermal hold; verify by metallography on test coupon |
| 3 | 12.16" | LOW HARDNESS | Salt bath temp too high; or incomplete austenitization | Lower salt bath temp; increase austenitizing time |
| 4 | 18.0" | CRACKING (RARE) | Thermal shock on salt bath entry | Pre-heat parts; control immersion rate |

Interior per card:
- Failure: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for austempering. Specific temperatures, hold times, and salt compositions vary by steel grade, section thickness, and specification. Consult your process engineer and applicable AMS/ASTM standards for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Austempering -- Process Flow

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
| Zone 2 - Process Flow | Section label, seven flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 7-row table |
| Zone 4 - Why Austempering | Section label, two comparison callouts |
| Zone 5 - Failure Modes | Section label, four failure cards |
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
| `Austempering Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Austempering Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Austempering Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Austempering Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Austempering Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Austempering Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Austempering cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The key differentiator from conventional heat treatment is Stage 5 (Isothermal Hold) -- this is where bainite forms instead of martensite. The comparison callout answers the most common question: "why austemper instead of quench and temper?" The answer is toughness at equivalent hardness, dramatically less distortion, and no temper cycle. Transfer speed (Stage 4) is the process-critical bottleneck -- if you miss the pearlite nose, you scrap the load.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #631 -- Construction Workup v1.0*
*2026-04-26*
