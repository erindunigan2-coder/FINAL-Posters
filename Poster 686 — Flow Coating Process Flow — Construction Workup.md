---
Project: Plating Posters Inc
Poster Number: 686
Title: "Flow Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating)"
Technical Source: Industry-standard flow coating (flood/flow) process. Covers the complete 7-stage sequence from surface preparation through inspection. Values are typical ranges for industrial flood/flow coating systems with recirculation.
Process Scope: Flow coating -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #686 -- Construction Workup
## Flow Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Flow Coating. It shows the complete 7-stage sequence at a glance -- every stage visible in one U-flow diagram. Flow coating is the simplest application method in the painting family: pump coating over the part, let gravity do the work, collect the excess and recirculate. The poster is the "map" that the remaining 8 posters (#687--#694) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (flow coating vs. spray), and a troubleshooting quick-hit strip. The recirculation system and viscosity drift are the dominant control themes.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Flow vs. Spray" comparison callout (Block E):** Two side-by-side callout boxes comparing flow coating vs. spray painting. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes. Similar to defect grid cards but in a single row.

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
| Amber | `#E8A020` | Application & cure stages, key parameters |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Optimal reference, pass states |
| Coral | `#E05C5C` | Problems, defects, caution callouts |
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

ZONE 4 -- FLOW VS. SPRAY COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Flow Coating vs. Spray side-by-side callout

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

> FLOW COATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 7 Stages from Prep to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Flood it. Drain it. Cure it. The simplest coating method -- 90-95% transfer efficiency with nothing but gravity and a pump.

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
| 1. Surface Prep | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Clean | Box 2 | 6.0" | `#2EC4B6` (Teal) | Cleaning |
| 3. Rinse / Dry | Box 3 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 4. Pretreatment | Box 4 | 17.0" | `#E8A020` (Amber) | Treatment |

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
| 5. Flow Application | Box 5 | 17.0" | `#E8A020` (Amber) | Application |
| 6. Drain / Coverage | Box 6 | 11.5" | `#E8A020` (Amber) | Leveling |
| 7. Cure | Box 7 | 6.0" | `#27AE60` (Emerald) | Cure |

Note: Box at X: 0.5" on bottom row is reserved for an **Inspection callout card** -- not a flow box but a summary card:
- Same dimensions (5.0" x 4.5"), fill `#1E2435`, top accent `#27AE60`
- Text: `INSPECT` badge + `ASTM D7091 DFT` + `Multiple locations -- flow coat has +/- 30-50% variation`

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Surface Prep:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Surface Prep`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
SSPC-SP6 min (structural)
1.5--3.0 mil profile
Mechanical or blast
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove mill scale, rust, old coatings`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Profile depth per spec`

*Box 2 -- Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Clean`
- Parameters: `Solvent wipe or alkaline wash` / `Multi-stage spray washer (lines)` / `Water break free`
- Purpose: `Remove oils, soils, grinding dust`
- Check: `Residual oil ruins adhesion in thin-film flow systems`

*Box 3 -- Rinse / Dry:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Rinse / Dry`
- Parameters: `DI or city water rinse` / `Complete dry -- forced air or oven` / `No trapped moisture`
- Purpose: `Remove cleaner residue, eliminate water`
- Check: `CAUTION: Trapped water in recesses blisters under coating` (`#E05C5C`)

*Box 4 -- Pretreatment:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Pretreatment`
- Parameters: `Iron phosphate (general)` / `Zinc phosphate (high-perf)` / `Per spec`
- Purpose: `Promote adhesion, corrosion resistance`
- Check: `Coating weight per supplier TDS`

*Box 5 -- Flow Application:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Flow Application`
- Parameters: `Viscosity: 15--40 sec (Zahn #2)` / `Flow rate: 1--5 gal/min/nozzle` / `DFT: 0.5--3.0 mils`
- Purpose: `Apply coating by flood or curtain flow`
- Check: `Viscosity drift from solvent evaporation -- check hourly`

*Box 6 -- Drain / Coverage:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Drain / Coverage`
- Parameters: `Drain time: 30--120 sec` / `Part angle: orient for runoff` / `Recirculate excess`
- Purpose: `Remove excess coating, level the film`
- Check: `Holidays in shielded areas -- inner corners, upward faces`

*Box 7 -- Cure:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Cure`
- Parameters: `Air dry, force dry, or bake` / `Bake: 250--350 F` / `Force dry: 120--160 F`
- Purpose: `Crosslink or dry the coating film`
- Check: `Confirm PMT or dry-through per coating TDS`

*Inspection Callout (X: 0.5"):*
- Badge: `INSPECT`, fill `#27AE60`
- Name: `Final Inspection`
- Parameters: `ASTM D7091 (DFT)` / `Measure top, middle, bottom` / `Min DFT spec, not target`
- Purpose: `Verify coverage and film build`
- Check: `Flow coat variation: +/- 30-50% -- measure everywhere`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Rinse` |
| `#E8A020` (Amber) | `Application & Leveling` |
| `#27AE60` (Emerald) | `Cure & Inspection` |
| `#E05C5C` (Coral) | `Caution / Defect` |

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
- Stage (3.5") | Method (5.5") | Temperature (3.0") | Time (2.5") | Key Metric (4.0") | Key Control (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Method | Temp | Time | Key Metric | Key Control |
|---|---|---|---|---|---|
| 1. Surface Prep | Blast or mechanical | Ambient | Per spec | 1.5--3.0 mil profile | SSPC-SP6 minimum |
| 2. Clean | Solvent or alkaline wash | 130--160 F (lines) | 2--5 min | Water break free | Oil removal |
| 3. Rinse / Dry | DI rinse + forced air | Ambient--160 F | Until dry | No trapped moisture | Recess drainage |
| 4. Pretreatment | Iron or zinc phosphate | Per spec | Per spec | Coating weight | Adhesion promotion |
| 5. Flow Application | Flood/flow or curtain | Ambient | Continuous | 0.5--3.0 mil DFT | Viscosity (Zahn #2) |
| 6. Drain / Coverage | Gravity drain | Ambient | 30--120 sec | Film uniformity | Part orientation |
| 7. Cure | Air/force/bake | 250--350 F (bake) | Per TDS | Hardness, adhesion | PMT confirmation |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Flow vs. Spray Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> FLOW VS. SPRAY -- WHEN DOES EACH WIN?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Flow Coating:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `FLOW COATING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Gravity Does the Work` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Transfer efficiency | 90-95% (recirculation) |
| Equipment | Pump, nozzles, drain pan, tank |
| Film uniformity | +/- 30-50% (moderate) |
| Interior coverage | Excellent -- flows into recesses |
| Appearance grade | Low to medium (primer, industrial) |
| Part size range | Large / irregular preferred |
| Line complexity | Simple -- minimal infrastructure |
| Compressed air | Not required |
| Overspray waste | None (recirculated) |
| Best for | Tanks, enclosures, structural steel |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Lowest cost per sq ft for large parts -- nearly zero overspray waste` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Spray Painting:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `SPRAY PAINTING` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Precision and Appearance` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Transfer efficiency | 30-65% (conventional); 65-85% (HVLP) |
| Equipment | Spray gun, booth, compressed air, exhaust |
| Film uniformity | +/- 5-15% (excellent) |
| Interior coverage | Limited -- line-of-sight |
| Appearance grade | High (automotive, aerospace capable) |
| Part size range | Any size |
| Line complexity | Moderate to high |
| Compressed air | Required |
| Overspray waste | Significant (captured in booth) |
| Best for | Appearance-critical, tight-tolerance DFT |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Best film control and finish quality -- the standard for appearance-critical work` -- Inter Medium, 13 pt, `#2EC4B6`

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
| 1 | 0.5" | CURTAINING / SAGS | Viscosity too low or drain time too short | Increase viscosity; orient parts for drainage |
| 2 | 6.33" | HOLIDAYS / MISSED AREAS | Shielded surfaces (inner corners, upward faces) | Reposition parts; add nozzles; touch-up spray |
| 3 | 12.16" | SKINNING IN TANK | Stagnant coating surface in recirculation tank | Keep tank agitated or covered; strain continuously |
| 4 | 18.0" | VISCOSITY DRIFT | Solvent evaporation from recirculation | Check viscosity hourly; add solvent per TDS |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for industrial flow coating (flood/flow) systems. Specific formulations, viscosities, and cure schedules vary by coating manufacturer. Consult your coating supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Flow Coating -- Process Flow

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
| Zone 2 - Process Flow | Section label, seven flow boxes, inspection card, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 7-row table |
| Zone 4 - Flow vs Spray | Section label, two comparison callouts |
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
| `Flow Coating Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flow Coating Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flow Coating Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Flow Coating Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flow Coating Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flow Coating Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Flow Coating cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#687--#694) zoom into each stage individually. The flow vs. spray comparison answers the most common question: "why not just spray it?" The answer is cost and waste -- flow coating achieves 90-95% transfer efficiency because everything recirculates. The viscosity drift callout is critical because it is the #1 day-to-day control challenge on any flow coat line.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #686 -- Construction Workup v1.0*
*2026-04-26*
