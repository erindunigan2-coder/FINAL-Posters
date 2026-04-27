---
Project: Plating Posters Inc
Poster Number: 613
Title: "Induction Hardening -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7)"
Technical Source: Industry-standard induction hardening process. Covers the complete 7-stage sequence from part preparation through final inspection. Values are typical ranges for medium-carbon steels (1045/4140 class). No atmosphere control required -- rapid electromagnetic heating limits oxidation.
Process Scope: Induction hardening -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - HeatTreatment
  - ProcessFlow
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #613 -- Construction Workup
## Induction Hardening -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Induction Hardening. It shows the complete 7-stage process sequence at a glance -- every stage visible in one U-flow diagram. An operator sees the full line, a supervisor checks parameters, a quality engineer spots where problems originate. This poster is the "map" that the other 8 posters (#614--#621) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (induction vs. flame), and a troubleshooting quick-hit strip. Dense but scannable -- the heat treat foreman's wall reference.

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

3. **"Induction vs. Flame" comparison callout (Block E):** Two side-by-side callout boxes comparing induction vs. flame hardening. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Heating/energy stages, key parameters |
| Teal | `#2EC4B6` | Prep and cooling stages, structural positives |
| Emerald | `#27AE60` | Optimal/pass states, coil setup (hero stage) |
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

ZONE 4 -- INDUCTION VS. FLAME COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Induction vs. Flame side-by-side callout

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

> INDUCTION HARDENING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 7 Stages from Part Prep to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Electromagnetic induction heats only the surface -- hard case, tough core, no atmosphere required. Hang this poster at the induction cell.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row: four boxes. Bottom row: three boxes (right-aligned with vertical connector from Stage 4).

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Prep | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Fixturing | Box 2 | 6.0" | `#2EC4B6` (Teal) | Setup |
| 3. Coil Setup | Box 3 | 11.5" | `#27AE60` (Emerald) | Setup (Hero) |
| 4. Heating Cycle | Box 4 | 17.0" | `#E8A020` (Amber) | Heating |

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
| 5. Quench | Box 5 | 17.0" | `#2EC4B6` (Teal) | Cooling |
| 6. Temper | Box 6 | 11.5" | `#E8A020` (Amber) | Heating |
| 7. Inspection & QA | Box 7 | 6.0" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Prep:*

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
Clean: scale, rust, oil free
Prior micro: fine pearlite or Q&T
No stop-off coating needed
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Clean surface ensures uniform electromagnetic coupling`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Decarburized surface will not harden`

*Box 2 -- Fixturing:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Fixturing`
- Parameters: `Between centers or chuck` / `Non-magnetic fixture (SS, brass)` / `Part rotation: 60--300 RPM`
- Purpose: `Position part for uniform coil coupling`
- Check: `Ferrous fixtures will heat -- use non-magnetic only`

*Box 3 -- Coil Setup:*
- Badge: `STAGE 3`, fill `#27AE60`
- Name: `Coil Setup` / Subtitle: `THE HERO STAGE` (14 pt, `#27AE60`)
- Parameters: `Coil gap: 0.040--0.125 in` / `Freq: 1--450 kHz` / `Power: 10--1000+ kW`
- Purpose: `Coil geometry + frequency = case depth and pattern`
- Check: `CRITICAL: Coil shape determines heat pattern` (Emerald `#27AE60`)

*Box 4 -- Heating Cycle:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Heating Cycle`
- Parameters: `1550--1650 F (845--900 C)` / `0.5--30 sec (single-shot)` / `Power density: 1--50 kW/in2`
- Purpose: `Rapid austenitization of surface layer only`
- Check: `CAUTION: Overheating causes grain growth + cracking risk` (Coral `#E05C5C`)

*Box 5 -- Quench:*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Quench`
- Parameters: `Polymer (PAG) 5--15% in water` / `or water spray` / `Delay: 0.1--2.0 sec`
- Purpose: `Transform austenite to martensite`
- Check: `CRITICAL: Quench delay too long = heat soak to core` (Coral `#E05C5C`)

*Box 6 -- Temper:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Temper`
- Parameters: `300--400 F (150--205 C)` / `1--2 hours furnace` / `or inline induction temper`
- Purpose: `Relieve internal stresses, improve toughness`
- Check: `Temper immediately after quench -- never skip`

*Box 7 -- Inspection & QA:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Inspection & QA`
- Parameters: `Surface HRC per ASTM E18` / `Case depth per ASTM E384` / `MPI per ASTM E1444`
- Purpose: `Verify hardness, case depth, and crack-free condition`
- Check: `Pattern verification by nital etch on cross-section`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep & Cooling` |
| `#27AE60` (Emerald) | `Coil Setup & QA` |
| `#E8A020` (Amber) | `Heating & Temper` |
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
- Stage (3.5") | Frequency/Setup (5.0") | Temperature (3.0") | Time (2.5") | Quench/Media (3.5") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Frequency/Setup | Temp | Time | Quench/Media | Key Control |
|---|---|---|---|---|---|
| 1. Part Prep | -- | -- | -- | -- | Clean surface, proper prior micro |
| 2. Fixturing | Non-magnetic | -- | -- | -- | Coil-to-part gap uniform |
| 3. Coil Setup | 1--450 kHz | -- | -- | -- | Frequency determines case depth |
| 4. Heating | Per recipe | 1550--1650 F | 0.5--30 sec | -- | Power density + time |
| 5. Quench | -- | 60--100 F | 0.1--2.0 sec delay | PAG 5--15% or water | Quench delay critical |
| 6. Temper | -- | 300--400 F | 1--2 hr | Air / induction | Temper immediately |
| 7. Inspection | -- | -- | -- | -- | HRC, ECD, MPI, nital etch |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Induction vs. Flame Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> INDUCTION VS. FLAME -- WHICH SURFACE HARDENING?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Induction Hardening:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `INDUCTION HARDENING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Precision & Speed` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Heat source | Electromagnetic induction (eddy currents) |
| Precision | Excellent -- coil shape defines pattern exactly |
| Case depth control | +/- 0.005--0.010 inch |
| Heating rate | 100--1000 F/second |
| Cycle time | Seconds (single-shot) |
| Atmosphere | None required -- major advantage |
| Best for | High-volume; precision patterns; small-to-medium parts |
| Capital cost | High (power supply + custom coils) |
| Automation | Fully CNC-controlled; recipe-stored |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Fastest surface hardening method -- seconds per part in production` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Flame Hardening:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `FLAME HARDENING` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Flexibility & Simplicity` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Heat source | Oxy-fuel flame (acetylene/O2 or propane/O2) |
| Precision | Moderate -- operator/torch dependent |
| Case depth control | +/- 0.020--0.030 inch |
| Heating rate | 50--200 F/second |
| Cycle time | Minutes (progressive) |
| Atmosphere | None required |
| Best for | Large parts; low volume; field repairs; irregular shapes |
| Capital cost | Low (standard torch equipment) |
| Automation | Manual or semi-automated |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `No custom coil needed -- adapts to any geometry with standard torch equipment` -- Inter Medium, 13 pt, `#2EC4B6`

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
| 1 | 0.5" | QUENCH CRACKING | Excessive power, sharp corners, severe quench | Control power/time; generous radii; proper quenchant |
| 2 | 6.33" | SOFT SPOTS | Non-uniform coupling, part not rotating | Verify coil gap; check rotation; verify surface carbon |
| 3 | 12.16" | SHALLOW CASE | Frequency too high, power too low, short time | Adjust parameters; verify frequency selection |
| 4 | 18.0" | THROUGH-HARDENED | Frequency too low or time too long for section | Reduce time; increase frequency; redesign coil |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for induction hardening of medium-carbon steels. Specific power settings, frequencies, and cycle times vary by equipment and part geometry. Consult your equipment manufacturer and applicable specifications for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Induction Hardening -- Process Flow

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
| Zone 4 - Induction vs Flame | Section label, two comparison callouts |
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
| `Induction Hardening Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Induction Hardening Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Induction Hardening Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Induction Hardening Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Induction Hardening Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Induction Hardening Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Induction Hardening cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#614--#621) zoom into each stage individually. The induction vs. flame comparison answers the most common question in surface hardening: "when do I use induction vs. flame?" The answer is precision and volume -- induction wins for high-production, repeatable patterns; flame wins for large parts, low volume, and field work.

Note: This is a 7-stage flow (not 8 like electroplating) because induction hardening is inherently simpler -- no atmosphere control, no chemical baths. The bottom row has only 3 boxes, which creates visual asymmetry with the top row of 4. This is intentional -- the empty space in the bottom-left can be used for a "key insight" callout or left clean for visual breathing room.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #613 -- Construction Workup v1.0*
*2026-04-26*
