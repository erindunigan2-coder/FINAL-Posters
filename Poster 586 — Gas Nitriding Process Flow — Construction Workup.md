---
Project: Plating Posters Inc
Poster Number: 586
Title: "Gas Nitriding -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding)"
Technical Source: Industry-standard gas nitriding process per AMS 2759/6D and AMS 2759/10A. Covers the complete 9-stage sequence from pre-heat-treatment through final inspection. Values are typical ranges for ammonia-based gas nitriding on nitriding-grade and alloy steels. All numerical data verified against ASM Handbook Vol. 4 and AMS specifications.
Process Scope: Gas nitriding -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - HeatTreatment
  - Diffusion
  - ProcessFlow
  - ConstructionWorkup
---

# Poster #586 -- Construction Workup
## Gas Nitriding -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Gas Nitriding. It shows the complete 9-stage process at a glance -- from pre-heat-treatment through final inspection. A furnace operator sees the full sequence, a metallurgist checks parameters, a quality engineer spots where problems originate. This poster is the "map" that the remaining 8 posters (#587--#594) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (gas nitriding vs. carburizing -- why no quench?), and a troubleshooting quick-hit strip. Dense but scannable -- the nitriding department's wall reference.

The defining characteristic of gas nitriding: no phase transformation, no quench, near-zero distortion. Hardness comes from nitride precipitates in ferrite, not martensite. That fundamental distinction should echo through the entire poster.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Each box is color-coded by stage type. Arrows are simple connectors.

2. **Parameter summary table (Block D):** A compact 9-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why Gas Nitriding?" comparison callout (Block E):** Two side-by-side callout boxes comparing gas nitriding vs. carburizing. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36":** Set to exactly 24 inches wide by 36 inches tall.

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
| Amber | `#E8A020` | Furnace/atmosphere stages, key parameter highlights |
| Teal | `#2EC4B6` | Prep and cooling stages, structural positives |
| Emerald | `#27AE60` | Nitriding cycle (main process), optimal reference |
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
  Block B: Nine-stage U-flow diagram (top row 5, bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 9-row parameter table (one row per stage)

ZONE 4 -- WHY GAS NITRIDING? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Gas Nitriding vs. Carburizing side-by-side callout

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

> GAS NITRIDING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 9 Stages from Pre-Heat-Treat to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Nitrogen diffusion below the critical temperature -- no quench, no phase transformation, near-zero distortion. Hardness by precipitation, not martensite.

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

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row of five boxes, bottom row of four boxes, U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Pre-Heat-Treat | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Pre-Clean | Box 2 | 5.1" | `#2EC4B6` (Teal) | Prep |
| 3. Surface Activation | Box 3 | 9.7" | `#2EC4B6` (Teal) | Prep |
| 4. Load & Fixture | Box 4 | 14.3" | `#2EC4B6` (Teal) | Prep |
| 5. Furnace Purge | Box 5 | 18.9" | `#E8A020` (Amber) | Furnace |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.3" (bottom center Box 5)
- To: X: 21.0", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Stage 1 Nitriding | Box 6 | 18.9" | `#27AE60` (Emerald) | Core Process |
| 7. Stage 2 Nitriding | Box 7 | 14.3" | `#27AE60` (Emerald) | Core Process |
| 8. Furnace Cool | Box 8 | 9.7" | `#E8A020` (Amber) | Cooling |
| 9. Inspect & Test | Box 9 | 5.1" | `#2EC4B6` (Teal) | QA |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Pre-Heat-Treat:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Pre-Heat-Treat`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Q&T to final core hardness
Temper > nitride temp + 50 F
Stress relieve after rough machining
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Part MUST be in final heat-treated condition before nitriding`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: Temper temp must exceed nitriding temp by 50 F minimum -- or core softens`

*Box 2 -- Pre-Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Pre-Clean`
- Parameters: `Solvent wash / vapor degrease` / `Remove all oils, oxides, passive films` / `No fingerprints (wear gloves)`
- Purpose: `Contaminants block nitrogen diffusion and poison nitriding reaction`
- Check: `Sulfur-bearing cutting fluids are worst -- complete removal critical`

*Box 3 -- Surface Activation:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Surface Activation`
- Parameters: `Light abrasive blast` / `OR chemical activation` / `Removes Cr2O3 on high-Cr steels`
- Purpose: `Break passive chromium oxide film so nitrogen can penetrate`
- Check: `High-Cr steels (H13, 4340) may need activation -- plain carbon does not`

*Box 4 -- Load & Fixture:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Load & Fixture`
- Parameters: `Hang parts vertically (preferred)` / `0.5--1.0 in spacing minimum` / `Fixtures support 40--90 hr at temp`
- Purpose: `Position parts for uniform ammonia gas flow over all surfaces`
- Check: `Fixture creep -- long cycles demand robust alloy fixtures`

*Box 5 -- Furnace Purge:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Furnace Purge` / Subtitle: `& Introduce Ammonia`
- Parameters: `N2 purge to remove air` / `Ramp to 925--1050 F (496--566 C)` / `Introduce NH3 after purge`
- Purpose: `Establish protective atmosphere before nitriding begins`
- Check: `CAUTION: Dissociated NH3 contains H2 -- burn-off pilot MUST be lit` (Coral `#E05C5C`)

*Box 6 -- Stage 1 Nitriding:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Stage 1 Nitriding` / Subtitle: `Case Building`
- Parameters: `925--975 F (496--524 C)` / `15--30% NH3 dissociation` / `15--40 hours` / `Builds case depth`
- Purpose: `High nitriding potential drives nitrogen deep into the ferrite`
- Check: `Monitor dissociation rate at exhaust -- key process control`

*Box 7 -- Stage 2 Nitriding:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Stage 2 Nitriding` / Subtitle: `White Layer Control`
- Parameters: `1000--1050 F (538--566 C)` / `75--85% NH3 dissociation` / `10--30 hours` / `Controls white layer`
- Purpose: `Higher dissociation reduces nitriding potential at surface -- limits compound zone growth`
- Check: `Skip Stage 2 only if white layer is acceptable at Stage 1 thickness`

*Box 8 -- Furnace Cool:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Furnace Cool`
- Parameters: `Cool under NH3 to 300 F` / `Then air cool` / `NO QUENCH`
- Purpose: `Slow controlled cooling -- no phase transformation occurs`
- Check: `NO QUENCH REQUIRED -- this is NOT carburizing. Hardness is from precipitates, not martensite`

*Box 9 -- Inspect & Test:*
- Badge: `STAGE 9`, fill `#2EC4B6`
- Name: `Inspect & Test`
- Parameters: `Superficial Rockwell (HR15N)` / `Microhardness traverse` / `White layer metallography`
- Purpose: `Verify surface hardness, case depth, and compound zone per specification`
- Check: `White layer class (0, 1, or 2) per AMS 2759/10 -- measure on cross-section`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & QA` |
| `#E8A020` (Amber) | `Furnace & Cooling` |
| `#27AE60` (Emerald) | `Nitriding Cycle (Core)` |
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

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Atmosphere (4.5") | Temperature (3.0") | Time (3.0") | Key Output (4.0") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Atmosphere | Temp | Time | Key Output | Key Control |
|---|---|---|---|---|---|
| 1. Pre-Heat-Treat | -- | Per steel spec | Per spec | Core hardness set | Temper > nitride + 50 F |
| 2. Pre-Clean | -- | Ambient | 10--15 min | Oil-free surface | No sulfur residue |
| 3. Surface Activate | -- | Ambient | As needed | Passive film removed | High-Cr steels only |
| 4. Load & Fixture | -- | -- | -- | Uniform spacing | 0.5--1.0 in min gap |
| 5. Furnace Purge | N2 then NH3 | 925--1050 F | Ramp | Atmosphere established | Burn-off pilot lit |
| 6. Stage 1 Nitride | NH3, 15--30% diss. | 925--975 F | 15--40 hr | Case depth built | Dissociation rate |
| 7. Stage 2 Nitride | NH3, 75--85% diss. | 1000--1050 F | 10--30 hr | White layer controlled | KN potential |
| 8. Furnace Cool | NH3 then air | Cool to 300 F | 2--6 hr | No quench stress | Pilot lit during cool |
| 9. Inspect | -- | Ambient | -- | Hardness + case + WL | White layer class |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Why Gas Nitriding? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY GAS NITRIDING? -- NITRIDING VS. CARBURIZING

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Gas Nitriding:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `GAS NITRIDING` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Nitrogen Precipitation -- No Quench` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Temperature | 925--1050 F (below Ac1) |
| Hardening mechanism | Nitride precipitates in ferrite |
| Case depth | 0.005--0.030 in (shallow) |
| Cycle time | 15--90 hours (long) |
| Quench | NONE -- furnace cool |
| Distortion | Near zero (no phase change) |
| Surface hardness | 700--1200 HV (steel dependent) |
| Best for | Nitralloy, H13, 4140, 4340 |
| Pre-treatment | Q&T required BEFORE nitriding |
| White layer | Controllable (2-stage Floe process) |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Zero distortion + extreme surface hardness -- when you cannot tolerate quench warpage` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Carburizing:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CARBURIZING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Carbon Diffusion + Quench` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Temperature | 1650--1750 F (above Ac3) |
| Hardening mechanism | Martensite from quench |
| Case depth | 0.020--0.250 in (deep) |
| Cycle time | 2--50 hours (moderate) |
| Quench | Oil or gas quench (required) |
| Distortion | Moderate to high (phase change + quench) |
| Surface hardness | 58--63 HRC (580--770 HV) |
| Best for | 8620, 9310, 4320, gears |
| Pre-treatment | Not required (hardened by the process) |
| White layer | N/A |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Deep cases on alloy steels -- the workhorse for gears and power transmission` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | EXCESSIVE WHITE LAYER | Nitriding potential (KN) too high; single-stage only | Implement 2-stage Floe process; reduce KN in Stage 2 |
| 2 | 6.33" | SOFT SPOTS | Surface contamination; Cr oxide passive film | Improve cleaning; abrasive activate high-Cr steels |
| 3 | 12.16" | CORE SOFTENING | Nitriding temp exceeded original temper temp | Verify pre-treat temper was nitride temp + 50 F minimum |
| 4 | 18.0" | SPALLING / FLAKING | Thick brittle epsilon white layer | Control compound zone to gamma-prime; reduce WL thickness |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for gas nitriding per AMS 2759/6D and AMS 2759/10A. Specific equipment settings, atmosphere compositions, and process limits vary by steel grade and application specification. Consult your process engineer and applicable standards for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Process Flow

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
| Zone 2 - Process Flow | Section label, nine flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 9-row table |
| Zone 4 - Why Gas Nitriding | Section label, two comparison callouts |
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
| `Gas Nitriding Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Gas Nitriding cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#587--#594) zoom into each stage individually. The comparison section answers the most common question: "When do I nitride instead of carburize?" The answer is when distortion is unacceptable -- nitriding has no quench, no phase transformation, and near-zero dimensional change.

The 2-stage (Floe) process is a critical concept -- Stage 1 builds the case, Stage 2 controls the white layer. Both stages appear as separate flow boxes (Stages 6 and 7) because they are distinct process segments with different temperatures and dissociation targets.

The total cycle time (25-70+ hours) makes gas nitriding the longest process in the DH cluster series. Emphasize that this is a SLOW, CONTROLLED, PRECISION process -- the opposite of induction hardening's seconds-long heat cycle.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #586 -- Construction Workup v1.0*
*2026-04-26*
