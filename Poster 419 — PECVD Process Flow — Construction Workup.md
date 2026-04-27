---
Project: Plating Posters Inc
Poster Number: 419
Title: "PECVD -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD)"
Technical Source: Industry-standard PECVD (plasma-enhanced chemical vapor deposition) process. RF plasma at 13.56 MHz enables conformal thin film deposition at 25-400 degC -- far below thermal CVD temperatures. Covers the complete 10-stage sequence from part prep through inspection.
Process Scope: PECVD -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #419 -- Construction Workup
## PECVD -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for PECVD. It maps the complete 10-stage process at a glance -- every stage visible in a two-row flow diagram. An operator sees the full sequence, an engineer checks parameters, a process technician spots where problems originate. This poster is the "map" that the other 9 posters (#420--#428) zoom into.

Design philosophy: two-row U-flow diagram as the hero, a compact parameter summary table, a "Why PECVD?" comparison callout (PECVD vs. thermal CVD), and a troubleshooting quick-hit strip. Dense but scannable.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box color-coded by stage type. Arrows connecting boxes.
2. **Parameter summary table (Block D):** A compact 10-row table (one per stage) with key parameters.
3. **"Why PECVD?" comparison callout (Block E):** Two side-by-side boxes comparing PECVD vs. thermal CVD.
4. **Troubleshooting quick-hit strip (Block F):** Horizontal strip of 4 common problems with one-line fixes.
5. **4 pt left-border accents on callout boxes.**
6. **Global Colors / swatch remap for Light edition.**
7. **JetBrains Mono font:** Fallback: Courier Prime.
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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Safety stages, warning headers, plasma/RF accents |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Deposition stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, safety hazards |
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
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 4 -- WHY PECVD? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: PECVD vs. Thermal CVD side-by-side callout

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

> PLASMA-ENHANCED CVD (PECVD)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- 10 Stages from Part Prep to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> RF plasma drives thin film deposition at 25--400 degC. Conformal coatings on temperature-sensitive substrates -- no furnace required.

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

**BLOCK B -- Ten-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Two rows of five boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Prep | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Cleaning | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Loading | Box 3 | 9.7" | `#C8D0D8` (Silver) | Fixturing |
| 4. Plasma System Setup | Box 4 | 14.3" | `#E8A020` (Amber) | Equipment |
| 5. Parameter Setup | Box 5 | 18.9" | `#E8A020` (Amber) | Equipment |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.3"
- To: X: 21.0", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Deposition | Box 6 | 18.9" | `#27AE60` (Emerald) | Core Process |
| 7. Cooling | Box 7 | 14.3" | `#C8D0D8` (Silver) | Post-Process |
| 8. Unloading | Box 8 | 9.7" | `#C8D0D8` (Silver) | Post-Process |
| 9. Inspection & QA | Box 9 | 5.1" | `#E8A020` (Amber) | Quality |
| 10. Safety & PPE | Box 10 | 0.5" | `#E05C5C` (Coral) | Safety |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Prep:*

Stage badge:
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Inspect for burrs, defects
Verify substrate compatibility
Mask non-coat areas
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Ensure parts are suitable for vacuum processing`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: No loose debris -- particles ruin thin films`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Solvent clean (acetone, IPA)` / `or alkaline ultrasonic` / `DI rinse + dry`
- Purpose: `Remove oils, oxides, organics from surface`
- Check: `Plasma pre-clean in-chamber follows loading`

*Box 3 -- Loading:*
- Badge: `STAGE 3`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Loading` / Subtitle: `Fixturing`
- Parameters: `Mount on electrode/holder` / `Ensure thermal contact` / `Close chamber, pump down`
- Purpose: `Secure parts for vacuum deposition`
- Check: `CHECK: No fingerprints after fixturing -- wear nitrile gloves`

*Box 4 -- Plasma System Setup:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Plasma System Setup`
- Parameters: `Base vacuum < 50 mTorr` / `RF 13.56 MHz connected` / `Gas lines leak-checked`
- Purpose: `Prepare chamber for plasma ignition`
- Check: `Verify MFC calibration before each run`

*Box 5 -- Parameter Setup:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Parameter Setup`
- Parameters: `Set gas flows (SiH4, NH3, etc.)` / `Set RF power 100--2000 W` / `Set substrate temp 25--400 degC`
- Purpose: `Dial in recipe for target film`
- Check: `CAUTION: SiH4 is PYROPHORIC -- verify interlocks` (Coral `#E05C5C`)

*Box 6 -- Deposition:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Deposition`
- Parameters: `Pressure 50 mTorr--5 Torr` / `Plasma on -- film growing` / `Monitor via OES or ellipsometry`
- Purpose: `Grow SiO2, Si3N4, DLC, or barrier film`
- Check: `Film thickness = time x deposition rate`

*Box 7 -- Cooling:*
- Badge: `STAGE 7`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Cooling`
- Parameters: `Plasma off, gas off` / `Pump/purge cycle` / `Cool to < 80 degC before vent`
- Purpose: `Prevent thermal shock and oxidation`
- Check: `Do NOT vent hot -- thermal stress cracks films`

*Box 8 -- Unloading:*
- Badge: `STAGE 8`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Unloading`
- Parameters: `Vent to atmosphere (N2)` / `Open chamber` / `Handle with clean gloves`
- Purpose: `Remove coated parts without contamination`
- Check: `Inspect chamber walls -- schedule cleaning if buildup visible`

*Box 9 -- Inspection & QA:*
- Badge: `STAGE 9`, fill `#E8A020`
- Name: `Inspection & QA`
- Parameters: `Ellipsometry (thickness)` / `Adhesion test (tape/scratch)` / `Visual + color check`
- Purpose: `Verify film meets specification`
- Check: `Refractive index confirms film identity (SiO2 n=1.46, Si3N4 n=2.0)`

*Box 10 -- Safety & PPE (Always Active):*
- Badge: `ALL STAGES`, fill `#E05C5C`
- Name: `Safety & PPE`
- Parameters: `SiH4: PYROPHORIC gas` / `RF radiation: stay clear` / `Vacuum: implosion hazard`
- Purpose: `Safety applies to every stage -- not just one`
- Check: `SILANE IGNITES IN AIR -- gas cabinet interlocks mandatory` (Coral `#E05C5C`)

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Cleaning` |
| `#C8D0D8` (Silver) | `Fixturing & Post-Process` |
| `#E8A020` (Amber) | `Equipment Setup & QA` |
| `#27AE60` (Emerald) | `Deposition (Core Process)` |
| `#E05C5C` (Coral) | `Safety / Caution` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 10-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Key Action (5.5") | Temperature / Pressure (4.0") | Time (3.0") | Key Control (7.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Stage | Key Action | Temp / Pressure | Time | Key Control |
|---|---|---|---|---|
| 1. Part Prep | Inspect, mask, verify | Ambient | -- | No loose particles |
| 2. Cleaning | Solvent or alkaline clean | 50--70 degC (alk.) | 5--15 min | Water-break-free |
| 3. Loading | Mount, pump down | Ambient -> vacuum | 15--60 min pump | No fingerprints |
| 4. System Setup | Leak check, base vacuum | < 50 mTorr base | 10--30 min | MFC calibration |
| 5. Param. Setup | Set gas, power, temp | 25--400 degC | 5--15 min ramp | SiH4 interlocks verified |
| 6. Deposition | Plasma on, film growth | 50 mTorr--5 Torr | Per recipe | OES / ellipsometry |
| 7. Cooling | Plasma off, purge | Cool to < 80 degC | 15--60 min | No hot venting |
| 8. Unloading | Vent, remove parts | Ambient | 5--10 min | Clean gloves |
| 9. Inspection | Ellipsometry, adhesion | Ambient | 5--30 min | n = 1.46 (SiO2) |
| 10. Safety | PPE, gas monitoring | All stages | Continuous | SiH4 LEL detector |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Why PECVD? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY PECVD? -- PECVD VS. THERMAL CVD

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- PECVD:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `PLASMA-ENHANCED CVD (PECVD)` -- Barlow SemiBold, 18 pt, `#27AE60`
- Subtitle: `The Low-Temperature Alternative` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 13 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Deposition temp | 25--400 degC |
| Activation energy | RF plasma (13.56 MHz) |
| Substrate range | Si, glass, polymers, Al alloys, steel |
| Conformality | Good (not as perfect as thermal) |
| Film quality | Amorphous; 5--30 at.% hydrogen |
| Deposition rate | 0.5--3 um/hr |
| Key coatings | SiO2, Si3N4, DLC (a-C:H), SiOx barriers |
| Equipment | Parallel plate, ICP, or pulsed DC |
| Environment | Cleanroom typical (semiconductor) |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Temperature is the advantage. Coat polymers, glass, and assembled components that would melt in a CVD furnace.` -- Inter Medium, 12 pt, `#27AE60`

**Right -- Thermal CVD:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `THERMAL CVD` -- Barlow SemiBold, 18 pt, `#E8A020`
- Subtitle: `The High-Temperature Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Deposition temp | 800--1100 degC |
| Activation energy | Thermal only |
| Substrate range | Cemented carbide, ceramics, graphite |
| Conformality | Excellent -- best in class |
| Film quality | Crystalline or high-density amorphous |
| Deposition rate | 1--5 um/hr |
| Key coatings | TiN, TiC, Al2O3, diamond, TiCN |
| Equipment | Hot-wall reactor, exhaust scrubber |
| Environment | Industrial batch furnace |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Dense, crystalline films with exceptional hardness -- but only on substrates that survive 800+ degC.` -- Inter Medium, 12 pt, `#E8A020`

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
| 1 | 0.5" | PARTICLES IN FILM | Chamber wall flaking (buildup) | Clean chamber every 5--50 um accumulated |
| 2 | 6.33" | POOR ADHESION | Inadequate surface activation | O2 plasma pre-treat 1--5 min; use interlayer |
| 3 | 12.16" | NON-UNIFORM THICKNESS | Standing wave effects or bad gap | Optimize electrode gap; showerhead gas distribution |
| 4 | 18.0" | FILM CRACKING | Excessive thickness or stress | Limit single layer; use multilayer or graded design |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for PECVD thin film deposition. Specific recipes, gas flows, and process limits vary by equipment and application. Consult your equipment manufacturer for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> PECVD -- Process Flow

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
| Zone 2 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 10-row table |
| Zone 4 - Why PECVD | Section label, two comparison callouts |
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
| `PECVD Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PECVD Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PECVD Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `PECVD Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PECVD Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PECVD Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire PECVD cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 9 posters (#420--#428) zoom into individual stages. The PECVD vs. thermal CVD comparison answers the fundamental question: "why use plasma instead of heat?" The answer is temperature -- PECVD opens CVD-type coatings to substrates that would be destroyed by thermal CVD temperatures.

Safety callout: Stage 10 (Safety) gets Coral treatment because PECVD uses pyrophoric silane. This must be visually prominent -- it is not just another stage.

---

*Alaina -- Poster #419 -- Construction Workup v1.0 -- 2026-04-26*
