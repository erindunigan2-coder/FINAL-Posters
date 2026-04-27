---
Project: Plating Posters Inc
Poster Number: 559
Title: "Gas Carburizing -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing)"
Technical Source: Industry-standard gas (atmosphere) carburizing process. Endothermic atmosphere, boost/diffuse carbon cycle, oil quench, temper. Values are typical production ranges per ASM Handbook and AMS 2759/7.
Process Scope: Gas carburizing -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasCarburizing
  - HeatTreatment
  - Diffusion
  - ProcessFlow
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #559 -- Construction Workup
## Gas Carburizing -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Gas Carburizing (Atmosphere Carburizing). It shows the complete 9-stage process at a glance -- from part preparation through temper and inspection. A heat treat operator sees the full cycle, a supervisor checks atmosphere and temperature parameters, a quality engineer spots where problems originate. This poster is the "map" that the other 8 posters (#560--#567) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a case depth reference chart, and a troubleshooting quick-hit strip. Dense but scannable -- the foreman's wall reference for the entire carburizing line.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Each box is color-coded by stage type. Arrows are simple connectors. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 9-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **Case depth reference chart (Block E):** Table showing ECD vs. total cycle time at 1700 deg F -- the most referenced data point for any carburizing operation.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common failures with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36".**

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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, temperature ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Atmosphere/gas stages, warning headers, temperature callouts |
| Teal | `#2EC4B6` | Cleaning/prep stages, structural positives |
| Emerald | `#27AE60` | Carburizing cycle (boost/diffuse), optimal reference |
| Coral | `#E05C5C` | Safety hazards, failures, CO/explosion warnings |
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

ZONE 4 -- CASE DEPTH REFERENCE (22.0"--28.5" / ~6.5" tall)
  Block E: ECD vs. time table + key metallurgical notes

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`).

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> GAS CARBURIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 9 Stages from Part Prep to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Endothermic atmosphere carburizing -- the workhorse thermochemical hardening process for gears, bearings, and shafts. Hang this poster at the furnace control station.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row: 5 boxes left to right. Bottom row: 4 boxes right to left. U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.3"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.1") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Preparation | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Loading & Fixturing | Box 2 | 5.0" | `#2EC4B6` (Teal) | Prep |
| 3. Furnace Purge | Box 3 | 9.5" | `#E8A020` (Amber) | Atmosphere |
| 4. Heat to Temp | Box 4 | 14.0" | `#E8A020` (Amber) | Atmosphere |
| 5. Carburize (Boost+Diffuse) | Box 5 | 18.5" | `#27AE60` (Emerald) | Core Process |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.0")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 20.6", Y: 8.1" (bottom center Box 5)
- To: X: 20.6", Y: 9.7" (top center Box 6)

**Bottom Row (Y: 9.7" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Quench | Box 6 | 17.5" | `#E05C5C` (Coral) | Critical |
| 7. Wash | Box 7 | 12.0" | `#2EC4B6` (Teal) | Prep |
| 8. Temper | Box 8 | 6.5" | `#E8A020` (Amber) | Heat |
| 9. Inspection & QA | Box 9 | 1.0" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Preparation:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Clean: oil, grease, scale free
Mask: Cu plate 0.001" stop-off
Surface: machined condition
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Remove contaminants; protect non-case areas`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: Cu stop-off per AMS 2759/7`

*Box 2 -- Loading & Fixturing:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Loading & Fixturing`
- Parameters: `HT alloy fixtures (Inconel/RA330)` / `Min 0.25" part spacing` / `Orient for uniform gas flow`
- Purpose: `Proper fixturing prevents soft spots and distortion`
- Check: `No nesting -- gas must contact all surfaces`

*Box 3 -- Furnace Purge:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Furnace Purge`
- Parameters: `N2 purge: 5 volume changes min` / `Burn-off pilot MUST be lit` / `Before introducing endo gas`
- Purpose: `Remove oxygen to prevent explosion on endo gas introduction`
- Check: `CRITICAL: Purge failure = explosion risk` (Coral `#E05C5C`)

*Box 4 -- Heat to Temperature:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Heat to Temperature`
- Parameters: `1650--1700 F (900--925 C)` / `Endo atmosphere established` / `Cp control active`
- Purpose: `Austenitize steel; FCC crystal structure enables carbon diffusion`
- Check: `Verify O2 probe and Cp reading before boost`

*Box 5 -- Carburize (Boost + Diffuse):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Carburize` / Subtitle: `Boost + Diffuse Cycle`
- Parameters: `Boost Cp: 0.90--1.10% C` / `Diffuse Cp: 0.75--0.85% C` / `Boost:Diffuse ~ 2:1 ratio`
- Purpose: `Drive carbon into austenite surface; redistribute for uniform profile`
- Check: `Cp > 1.1% = carbide network risk` (Coral `#E05C5C`)

*Box 6 -- Quench:*
- Badge: `STAGE 6`, fill `#E05C5C`
- Name: `Oil Quench`
- Parameters: `Fast quench oil 120--180 F` / `Agitated (H = 0.50--0.70)` / `Direct from carb temp or 1475--1550 F`
- Purpose: `Transform austenite to martensite (58--63 HRC surface)`
- Check: `FIRE RISK: Oil + 1500 F parts` (Coral `#E05C5C`)

*Box 7 -- Wash:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Post-Quench Wash`
- Parameters: `Alkaline wash or solvent` / `Remove all quench oil` / `Before tempering`
- Purpose: `Oil residue on parts will smoke/burn in temper furnace`
- Check: `Parts must be oil-free before temper`

*Box 8 -- Temper:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Temper`
- Parameters: `300--375 F (150--190 C)` / `2 hours minimum` / `Air or N2 atmosphere`
- Purpose: `Relieve internal stresses; improve toughness without losing surface hardness`
- Check: `Per AMS 2759/7; double temper for high-C tool steels`

*Box 9 -- Inspection & QA:*
- Badge: `STAGE 9`, fill `#27AE60`
- Name: `Inspection & QA`
- Parameters: `ECD to 50 HRC (ASTM E384)` / `Surface: 58--63 HRC` / `Microstructure: tempered martensite`
- Purpose: `Verify case depth, hardness, and microstructure meet specification`
- Check: `IGO, retained austenite, carbide network per spec`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Wash` |
| `#E8A020` (Amber) | `Atmosphere & Heat` |
| `#27AE60` (Emerald) | `Core Process & QA` |
| `#E05C5C` (Coral) | `Critical / Hazard` |
| `#C8D0D8` (Silver) | `Equipment Reference` |

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
- Stage (3.0") | Key Action (5.0") | Temperature (3.5") | Time (3.0") | Atmosphere/Media (4.5") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Key Action | Temp | Time | Atmosphere/Media | Key Control |
|---|---|---|---|---|---|
| 1. Part Prep | Clean + mask (Cu stop-off) | Ambient | -- | -- | Oil/grease free |
| 2. Load | Fixture in HT alloy baskets | Ambient | -- | -- | 0.25" min spacing |
| 3. Purge | N2 purge, burn-off pilot lit | Ambient | 5 vol changes | Nitrogen | No air in furnace |
| 4. Heat | Ramp to austenitizing temp | 1650--1700 F | 30--90 min | Endothermic gas | Cp control active |
| 5. Carburize | Boost + Diffuse cycle | 1650--1700 F | 2--28 hr (per ECD) | Endo + CH4 enrich | Cp 0.90--1.10 / 0.75--0.85 |
| 6. Quench | Oil quench (agitated) | Oil: 120--180 F | Seconds to minutes | Fast quench oil | H-value 0.50--0.70 |
| 7. Wash | Remove quench oil | Ambient--160 F | 5--15 min | Alkaline wash | Oil-free before temper |
| 8. Temper | Stress relief | 300--375 F | 2 hr min | Air or N2 | Per AMS 2759/7 |
| 9. Inspect | ECD, hardness, micro | Ambient | -- | -- | 50 HRC = ECD boundary |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Case Depth Reference

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> CASE DEPTH VS. TIME -- THE CARBURIZER'S REFERENCE

---

**BLOCK E -- Left: ECD Table (X: 0.5", W: 11.0")**

Y: 22.9" to 27.5". Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `ECD AT 1700 F (925 C)` Barlow SemiBold 18 pt `#27AE60`
Subtitle: `Effective Case Depth to 50 HRC` JetBrains Mono 13 pt `#F0EDE8` at 60%

| ECD (inch) | ECD (mm) | Total Cycle | TCD (approx.) |
|---|---|---|---|
| 0.020 | 0.5 | 2--3 hr | 0.030--0.035" |
| 0.030 | 0.75 | 3--5 hr | 0.045--0.055" |
| 0.040 | 1.0 | 5--7 hr | 0.060--0.070" |
| 0.060 | 1.5 | 8--12 hr | 0.085--0.100" |
| 0.080 | 2.0 | 14--20 hr | 0.110--0.130" |
| 0.100 | 2.5 | 20--28 hr | 0.140--0.160" |

Data: JetBrains Mono 12 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt.

Bottom note: `Rule of thumb: case depth is proportional to sqrt(time). Double the depth = 4x the time.` Inter Medium 12 pt `#E8A020`.

**BLOCK E -- Right: Key Metallurgical Notes (X: 12.0", W: 11.5")**

Y: 22.9" to 27.5". Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `METALLURGICAL ESSENTIALS` Barlow SemiBold 18 pt `#E8A020`

Bullet items (Inter Regular 13 pt `#F0EDE8`, line height 155%):

```
- Austenite dissolves up to ~2.1% C (at 2098 F)
  vs. ferrite max ~0.02% C -- this is WHY we heat

- Surface carbon target: 0.75--0.95% C
  Too high (>1.0%) = carbide network = REJECT

- Cp control: O2 probe + CO2 IR analyzer
  Cross-check with shim stock method

- Best steels: 8620, 9310, 4320, 5120
  (0.15--0.25% base carbon, good hardenability)

- ECD defined as depth to 50 HRC
  (~0.40% C for most carburizing steels)

- TCD = 1.3--1.6x ECD (total to core carbon)
```

**Full-width callout bar (Y: 27.8" to 28.3"):**
- Rounded rect, pill shape (radius 999), fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Carbon diffusion follows Fick's second law -- temperature is the throttle, time is the dial.` Inter Medium 14 pt `#27AE60`, center.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON FAILURES

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SOFT SPOTS | Part nesting; oil/grease residue blocking carbon absorption | Improve spacing; thorough cleaning |
| 2 | 6.33" | CARBIDE NETWORK | Cp too high (>1.1%) during boost; inadequate diffuse cycle | Reduce boost Cp; extend diffuse time |
| 3 | 12.16" | EXCESSIVE DISTORTION | Non-uniform quench; parts not fixtured properly; residual machining stress | Stress relieve pre-carb; press quench for gears |
| 4 | 18.0" | HIGH RETAINED AUSTENITE | Surface C too high (>1.0%); quench not severe enough | Control Cp; sub-zero treat (-100 to -120 F) |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for gas (atmosphere) carburizing. Specific equipment settings, cycle times, and acceptance criteria vary by specification and part design. Consult AMS 2759/7, CQI-9, and your process engineer for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Carburizing -- Process Flow

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
| Zone 4 - Case Depth Ref | Section label, ECD table, metallurgical notes, callout bar |
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
| `Gas Carburizing Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Carburizing Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Carburizing Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Carburizing Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Carburizing Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Carburizing Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Gas Carburizing cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#560--#567) zoom into each stage individually. The case depth table is the single most-consulted reference for any carburizing operation -- operators and engineers will look at this poster specifically for that data. The sqrt(t) rule callout is the one metallurgical insight that sticks.

Safety note: Endothermic gas is ~20% CO + ~40% H2 -- both explosive and toxic. The purge stage (Stage 3) is the most dangerous moment in the entire process. The poster should convey this gravity without panic.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #559 -- Construction Workup v1.0*
*2026-04-26*
