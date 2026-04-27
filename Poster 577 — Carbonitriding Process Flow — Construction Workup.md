---
Project: Plating Posters Inc
Poster Number: 577
Title: "Carbonitriding -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding)"
Technical Source: Industry-standard gas carbonitriding process. Covers the complete 7-stage sequence from part prep through temper. Values are typical ranges for ammonia-enriched endothermic atmosphere carbonitriding on low-carbon and free-machining steels.
Process Scope: Carbonitriding -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Carbonitriding
  - HeatTreatment
  - Diffusion
  - ProcessFlow
  - ConstructionWorkup
---

# Poster #577 -- Construction Workup
## Carbonitriding -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Carbonitriding. It shows the complete 7-stage process at a glance -- from part cleaning through temper. A furnace operator sees the full sequence, a metallurgist checks parameters, a quality engineer spots where problems originate. This poster is the "map" that the remaining 8 posters (#578--#585) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (carbonitriding vs. carburizing -- why choose one over the other?), and a troubleshooting quick-hit strip. Dense but scannable -- the heat treat supervisor's wall reference.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type. Arrows are simple connectors.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why Carbonitriding?" comparison callout (Block E):** Two side-by-side callout boxes comparing carbonitriding vs. carburizing. Established pattern from Poster #31.

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
| Teal | `#2EC4B6` | Prep and quench stages, structural positives |
| Emerald | `#27AE60` | Carbonitriding cycle (main process), optimal reference |
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

ZONE 4 -- WHY CARBONITRIDING? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Carbonitriding vs. Carburizing side-by-side callout

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

> CARBONITRIDING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 7 Stages from Prep to Temper

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Carbon + nitrogen together -- the budget-friendly case hardening process for low-hardenability steels and thin sections.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row of four boxes, bottom row of three boxes, U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Clean & Degrease | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Load & Fixture | Box 2 | 6.0" | `#2EC4B6` (Teal) | Prep |
| 3. Furnace Purge & Heat | Box 3 | 11.5" | `#E8A020` (Amber) | Furnace |
| 4. Carbonitriding Cycle | Box 4 | 17.0" | `#27AE60` (Emerald) | Main Process |

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
| 5. Oil Quench | Box 5 | 15.0" | `#E8A020` (Amber) | Quench |
| 6. Temper | Box 6 | 8.0" | `#E8A020` (Amber) | Post-Process |
| 7. Inspect & Test | Box 7 | 1.0" | `#2EC4B6` (Teal) | QA |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Clean & Degrease:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Clean & Degrease`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Alkaline wash or solvent
Oil/grease-free surface
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove all surface contaminants that block C/N absorption`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Surface must be chemically clean -- residue = soft spots`

*Box 2 -- Load & Fixture:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Load & Fixture`
- Parameters: `HT alloy baskets (Inconel, RA330)` / `Min 0.25 in clearance`
- Purpose: `Position parts for uniform gas contact and quench entry`
- Check: `Parts touching = soft spots from blocked gas`

*Box 3 -- Furnace Purge & Heat:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Furnace Purge` / Subtitle: `& Heat to Temperature`
- Parameters: `N2 purge: 5 volume changes min` / `Heat to 1400--1600 F (760--870 C)` / `Endo gas introduced after purge`
- Purpose: `Establish protective atmosphere before introducing ammonia`
- Check: `CAUTION: Endo gas is explosive -- burn-off pilot MUST be lit` (Coral `#E05C5C`)

*Box 4 -- Carbonitriding Cycle:*
- Badge: `STAGE 4`, fill `#27AE60`
- Name: `Carbonitriding Cycle` / Subtitle: `C + N Diffusion`
- Parameters: `1400--1600 F (760--870 C)` / `Endo gas + 2--10% NH3` / `Cp: 0.5--0.8% C` / `1--6 hours (case depth dependent)`
- Purpose: `Simultaneous carbon and nitrogen diffusion into austenite`
- Check: `NH3 > 10% risks retained austenite and porosity`

*Box 5 -- Oil Quench:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Oil Quench`
- Parameters: `Fast quench oil: 120--180 F` / `H-value: 0.50--0.70` / `Agitation required`
- Purpose: `Transform C+N enriched austenite to hard martensite`
- Check: `N lowers critical cooling rate -- even moderate quench hardens low-alloy steels`

*Box 6 -- Temper:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Temper`
- Parameters: `300--400 F (150--205 C)` / `1--2 hours minimum` / `Air atmosphere`
- Purpose: `Relieve quench stresses; improve toughness`
- Check: `Temper immediately after quench -- never skip`

*Box 7 -- Inspect & Test:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Inspect & Test`
- Parameters: `Microhardness traverse` / `Surface: 58--63 HRC` / `ECD per spec`
- Purpose: `Verify case depth, hardness, and microstructure`
- Check: `Check retained austenite -- carbonitriding has higher RA risk than carburizing`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & QA` |
| `#E8A020` (Amber) | `Furnace, Quench & Temper` |
| `#27AE60` (Emerald) | `Carbonitriding Cycle (Main)` |
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

**BLOCK D -- 7-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Atmosphere (5.0") | Temperature (3.5") | Time (2.5") | CD/Quench (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Atmosphere | Temp | Time | CD/Quench | Key Control |
|---|---|---|---|---|---|
| 1. Clean | -- | Ambient | 5--15 min | -- | Oil-free surface |
| 2. Load | -- | -- | -- | -- | 0.25 in min spacing |
| 3. Purge & Heat | Endo gas after N2 purge | 1400--1600 F | 30--60 min heat-up | -- | Burn-off pilot lit |
| 4. Carbonitride | Endo + 2--10% NH3, Cp 0.5--0.8% | 1400--1600 F | 1--6 hr | -- | NH3 % + Cp balance |
| 5. Oil Quench | -- | Oil 120--180 F | Immediate | H: 0.50--0.70 | Agitation on |
| 6. Temper | Air or N2 | 300--400 F | 1--2 hr min | -- | Temper within 1 hr |
| 7. Inspect | -- | -- | -- | -- | RA check critical |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Carbonitriding? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY CARBONITRIDING? -- CARBONITRIDING VS. CARBURIZING

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Carbonitriding:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `CARBONITRIDING` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `C + N Together` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Temperature | 1400--1600 F (lower) |
| Case depth | 0.003--0.030 in (thin) |
| Cycle time | 1--6 hours (short) |
| Atmosphere | Endo + ammonia (NH3) |
| Quench | Oil quench (standard) |
| Best for | Low-alloy, free-machining steels |
| Hardenability boost | YES -- nitrogen lowers critical cooling rate |
| Retained austenite | Higher risk (monitor closely) |
| Distortion | Less than carburizing (lower temp, thinner case) |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Nitrogen makes martensite possible in steels too lean to carburize alone` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Carburizing:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CARBURIZING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Carbon Only` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Temperature | 1650--1750 F (higher) |
| Case depth | 0.020--0.100+ in (deep) |
| Cycle time | 2--28 hours (long) |
| Atmosphere | Endo gas only (no NH3) |
| Quench | Oil quench (standard) |
| Best for | Medium-alloy steels (8620, 9310) |
| Hardenability boost | No -- steel must have inherent hardenability |
| Retained austenite | Moderate (manageable) |
| Distortion | More (higher temp, deeper case, thicker sections) |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Deep cases on alloy steels -- the workhorse for gears, shafts, and bearings` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | EXCESSIVE RETAINED AUSTENITE | Too much ammonia; N stabilizes austenite | Reduce NH3 %; sub-zero treatment (-120 F) |
| 2 | 6.33" | SURFACE POROSITY | Excess ammonia; N2 gas entrapment | Reduce NH3; avoid ammonia spikes |
| 3 | 12.16" | SHALLOW CASE | Temp too low; time too short; excess NH3 blocking C diffusion | Optimize temp/time; reduce NH3 if case is shallow |
| 4 | 18.0" | SOFT SPOTS | Part nesting; surface contamination | Proper fixturing; thorough cleaning |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for gas carbonitriding. Specific equipment settings, atmosphere compositions, and process limits vary by application and specification. Consult your process engineer and applicable standards (AMS 2759 series, CQI-9) for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Carbonitriding -- Process Flow

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
| Zone 4 - Why Carbonitriding | Section label, two comparison callouts |
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
| `Carbonitriding Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Carbonitriding Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Carbonitriding Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Carbonitriding Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Carbonitriding Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Carbonitriding Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Carbonitriding cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The comparison section answers the most common question: "When do I carbonitriding instead of carburize?" The answer is thin cases on cheap steels -- nitrogen makes martensite possible in steels that would otherwise form soft pearlite under oil quench.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #577 -- Construction Workup v1.0*
*2026-04-26*
