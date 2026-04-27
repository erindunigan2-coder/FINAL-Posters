---
Project: Plating Posters Inc
Poster Number: 529
Title: "D-Gun Spray -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: Industry-standard detonation gun (D-Gun) thermal spray process. Covers complete 10-stage sequence. Values are typical ranges for D-Gun systems using acetylene-oxygen detonation. Watson research brief sourced from ASM Handbook Vol 5A, Pawlowski, ITSA Handbook, and relevant ASTM/AMS standards. Originally proprietary to Union Carbide (now Praxair Surface Technologies / Oerlikon Metco).
Process Scope: D-Gun -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - ProcessFlow
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #529 -- Construction Workup
## D-Gun Spray -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for TS-06: Detonation Gun (D-Gun). The hero story is "controlled explosion" -- a precisely metered detonation of acetylene and oxygen accelerates powder particles to 750--1000 m/s, producing the densest, hardest, best-bonded coatings achievable by any thermal spray process. Porosity routinely below 0.5%, bond strength exceeding epoxy test limits. The poster shows the complete 10-stage process sequence in a U-flow diagram with a comparison callout (D-Gun vs. HVOF) and a troubleshooting strip.

D-Gun technology was originally proprietary to Union Carbide and remains a premium, semi-proprietary process. The loudest thermal spray process at 130--150 dB -- mandatory remote operation from outside a sound-isolated booth.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box is color-coded by stage type.
2. **"Controlled Detonation" hero callout (Block C):** Amber-tinted glass callout with the 750--1000 m/s stat and detonation mechanism.
3. **Parameter summary table (Block D):** Compact 10-row table.
4. **"D-Gun vs. HVOF" comparison callout (Block E):** Side-by-side -- D-Gun produces superior coatings but at higher cost and lower throughput.
5. **Troubleshooting quick-hit strip (Block F):** 4 common problems.
6. **4 pt left-border accents on callout boxes.**
7. **Global Colors / swatch remap for Light edition.**
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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Key parameters, warning headers, stat numbers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Spray application stage, optimal indicators |
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
- 5.0" -- Zone 2/Zone 3 boundary
- 16.5" -- Zone 3/Zone 4 boundary
- 22.5" -- Zone 4/Zone 5 boundary
- 28.5" -- Zone 5/Zone 6 boundary
- 32.5" -- Zone 6/Zone 7 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- "CONTROLLED DETONATION" HERO CALLOUT (2.9"--5.0" / ~2.1" tall)
  Block C: Big stat callout -- "750--1000 m/s" particle velocity, detonation mechanism

ZONE 3 -- PROCESS FLOW DIAGRAM (5.0"--16.5" / ~11.5" tall)
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block B2: Stage legend strip (color key)

ZONE 4 -- PARAMETER SUMMARY TABLE (16.5"--22.5" / ~6.0" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 5 -- D-GUN VS. HVOF COMPARISON (22.5"--28.5" / ~6.0" tall)
  Block E: D-Gun vs. HVOF side-by-side

ZONE 6 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 7 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> D-GUN SPRAY

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- Coatings by Controlled Detonation

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The densest coatings in thermal spray. Acetylene-oxygen detonation drives particles at 750--1000 m/s into the hardest, best-bonded deposits achievable.

---

### ZONE 2 -- "Controlled Detonation" Hero Callout

**Dimensions:** Full width within margins. Y: 2.9" to 5.0" (~2.1" tall).

**BLOCK C -- Big Stat Callout**

- Rounded rectangle, X: 0.5", Y: 3.1", W: 23.0", H: 1.6", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Amber-tinted glass treatment

**Stat number (left):**
- `750--1000 m/s` Barlow Condensed ExtraBold, 60 pt, `#E8A020`
- Position: X: 1.0", Y: 3.3"

**Label (right of stat):**
- `Particle velocity -- highest of any thermal spray process` Barlow SemiBold, 22 pt, `#F0EDE8`
- Position: X: 10.0", Y: 3.3"

**Sub-label:**
- `Acetylene + oxygen detonation at ~3500 m/s drives powder charges down a water-cooled barrel. Each controlled explosion deposits a 25 mm spot of near-fully-dense coating. Repeat 1--15 times per second.` Inter Regular, 14 pt, `#F0EDE8` at 70%
- Position: X: 10.0", Y: 4.0", W: 13.0"

---

### ZONE 3 -- Process Flow Diagram

**Dimensions:** Full page width within margins. Y: 5.0" to 16.5" (~11.5" tall).

---

**Section label:**
- Centered horizontally. Y: 5.2"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Ten-Stage U-Flow Diagram**

Y: 5.8" to 15.5" (~9.7" tall). Two rows of five boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.2"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 5.8" to 10.0") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Solvent Degrease | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Alkaline Clean | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Grit Blast | Box 3 | 9.7" | `#E8A020` (Amber) | Surface Prep |
| 4. Masking | Box 4 | 14.3" | `#C8D0D8` (Silver) | Fixturing |
| 5. Equipment Setup | Box 5 | 18.9" | `#3A4055` (Slate) | Setup |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~8.0")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.1", Y: 10.0" (bottom center Box 5)
- To: X: 21.1", Y: 11.3" (top center Box 6)

**Bottom Row (Y: 11.3" to 15.5") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Parameter Set | Box 6 | 18.9" | `#E8A020` (Amber) | Parameters |
| 7. Spray Application | Box 7 | 14.3" | `#27AE60` (Emerald) | Core Process |
| 8. Post-Treatment | Box 8 | 9.7" | `#E8A020` (Amber) | Post-Treatment |
| 9. Grinding | Box 9 | 5.1" | `#C8D0D8` (Silver) | Finishing |
| 10. Inspection & QA | Box 10 | 0.5" | `#2EC4B6` (Teal) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Solvent Degrease:*

Stage badge:
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Solvent Degrease`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Aqueous alkaline preferred
50--70 C immersion
Remove all oils & machining fluids
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Premium aerospace cleaning standard`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after DI rinse`

*Box 2 -- Alkaline Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `50--70 C (120--160 F)` / `pH 10--12` / `DI water rinse (aerospace)`
- Purpose: `Identical to HVOF protocol -- premium standard`
- Check: `Time to blast: < 4 hours (same shift preferred)`

*Box 3 -- Grit Blast:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Grit Blast`
- Parameters: `White Al2O3 36--60 mesh` / `40--60 PSI` / `Ra 3--6 um`
- Purpose: `Activate surface; create anchor profile`
- Check: `99.5%+ purity alumina -- no ferrous contamination` (`#E8A020`)

*Box 4 -- Masking:*
- Badge: `STAGE 4`, fill `#C8D0D8`
- Name: `Masking & Fixturing`
- Parameters: `Metal masks mandatory` / `Custom-machined SS or Inconel` / `Precision-balanced rotation fixtures`
- Purpose: `Define spray zone; withstand detonation impact`
- Check: `Full robotic operation -- no manual D-Gun spraying`

*Box 5 -- Equipment Setup:*
- Badge: `STAGE 5`, fill `#3A4055`, text `#F0EDE8`
- Name: `Equipment Setup`
- Parameters: `Water-cooled barrel (25--50 mm bore)` / `O2 + C2H2 metering` / `Spark ignition + N2 purge`
- Purpose: `Configure detonation barrel, gas supply, and robot`
- Check: `Sound-isolated booth MANDATORY (130--150 dB)`

*Box 6 -- Parameter Set:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Parameter Setup`
- Parameters: `Frequency: 1--15 Hz` / `O2/C2H2 ratio: 1.0--1.5` / `Standoff: 100--200 mm`
- Purpose: `Set detonation frequency, gas ratios, powder charge`
- Check: `Lean O2/C2H2 ratio reduces oxide content in coating`

*Box 7 -- Spray Application:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Spray Application`
- Parameters: `25 mm spot per cycle` / `5--20 um per spot` / `750--1000 m/s`
- Purpose: `Build coating by overlapping detonation spots`
- Check: `Total: 75--500 um; DE: 70--90%`

*Box 8 -- Post-Treatment:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Diamond grinding` / `Ra 0.05--0.4 um achievable` / `Superfinish for bearings`
- Purpose: `Achieve final surface finish and dimensions`
- Check: `No heat treatment required -- functional as-ground`

*Box 9 -- Grinding:*
- Badge: `STAGE 9`, fill `#C8D0D8`
- Name: `Grinding`
- Parameters: `Diamond wheel (resin bond)` / `Surface or cylindrical grind` / `Coolant: water-soluble`
- Purpose: `Remove as-sprayed roughness; achieve dimension`
- Check: `Avoid overheating -- use flood coolant`

*Box 10 -- Inspection & QA:*
- Badge: `STAGE 10`, fill `#2EC4B6`
- Name: `Inspection & QA`
- Parameters: `ASTM C633: > 80 MPa` / `ASTM E2109: < 0.5% porosity` / `ASTM E384: 1200--1500 HV300`
- Purpose: `Verify coating exceeds specification`
- Check: `Tighter tolerances than HVOF (+/- 25 um)`

---

**BLOCK B2 -- Stage Legend Strip**

Y: 15.7" to 16.3"

- Rounded rectangle, X: 0.5", Y: 15.7", W: 23.0", H: 0.5", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & QA` |
| `#E8A020` (Amber) | `Prep, Parameters & Post` |
| `#27AE60` (Emerald) | `Spray Application` |
| `#C8D0D8` (Silver) | `Masking & Grinding` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.25" x 0.25" rounded rect. Label: Inter Medium, 13 pt, `#F0EDE8`.

---

### ZONE 4 -- Parameter Summary Table

**Dimensions:** Y: 16.5" to 22.5" (~6.0" tall).

---

**Section label:**
- Centered. Y: 16.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 10-Row Parameter Table**

Y: 17.3" to 22.3". Column widths (23.0" total):
- Stage (3.5") | Key Spec (5.5") | Temperature (3.0") | Frequency/Speed (3.5") | Standoff/Pressure (3.5") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.4". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.45".

| Stage | Key Spec | Temp | Freq/Speed | Standoff/Pressure | Key Control |
|---|---|---|---|---|---|
| 1. Solvent Degrease | Aqueous alkaline | 50--70 C | 5--15 min | -- | Water-break-free |
| 2. Alkaline Clean | pH 10--12, DI rinse | 50--70 C | 5--15 min | -- | DI rinse (aerospace) |
| 3. Grit Blast | Al2O3 36--60 mesh | Ambient | Per coverage | 40--60 PSI | Ra 3--6 um |
| 4. Masking | Metal masks; SS/Inconel | -- | -- | -- | Robotic operation |
| 5. Equipment Setup | Water-cooled barrel | -- | -- | O2 + C2H2 | Sound booth mandatory |
| 6. Parameter Set | O2/C2H2 ratio 1.0--1.5 | 3500--4500 C (det.) | 1--15 Hz | 100--200 mm | Lean ratio = less oxide |
| 7. Spray | 750--1000 m/s | Controlled substrate | 1--15 cycles/s | 100--200 mm | 25 mm spot / cycle |
| 8. Post-Treatment | Diamond grind | Ambient | -- | -- | Ra < 0.4 um |
| 9. Grinding | Diamond wheel | Flood coolant | Per dimension | -- | Avoid overheating |
| 10. Inspection | C633, E2109, E384 | -- | -- | -- | +/- 25 um tolerance |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 5 -- D-Gun vs. HVOF Comparison

**Dimensions:** Y: 22.5" to 28.5" (~6.0" tall).

---

**Section label:**
- Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> D-GUN VS. HVOF -- THE PREMIUM DIFFERENCE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 23.3" to 28.3".

**Left -- D-Gun:**
- Rounded rect, X: 0.5", Y: 23.3", W: 11.0", H: 4.8", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `D-GUN (DETONATION GUN)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Gold Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Particle velocity | 750--1000 m/s (highest) |
| Porosity (WC-12Co) | < 0.5% (often < 0.2%) |
| Bond strength | > 80 MPa (exceeds epoxy) |
| Hardness (WC-12Co) | 1200--1500 HV300 |
| Deposition rate | 1--5 kg/hr |
| Noise | 130--150 dB (remote operation) |
| Cost | Premium (proprietary systems) |
| Typical parts | Turbine blades, seals, shafts |
| Oxide content | < 0.3% |
| Wear rate (ASTM G65) | 0.5--3 x 10^-7 mm3/Nm |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.5", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Premium process for the most demanding wear applications -- density and hardness exceed all alternatives` -- Inter Medium, 12 pt, `#E8A020`

**Right -- HVOF (Comparison):**
- Rounded rect, X: 12.0", Y: 23.3", W: 11.5", H: 4.8", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `HVOF (HIGH VELOCITY OXY-FUEL)` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `The Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Particle velocity | 600--900 m/s |
| Porosity (WC-12Co) | < 1% (typically < 0.5%) |
| Bond strength | > 70 MPa |
| Hardness (WC-12Co) | 1100--1400 HV300 |
| Deposition rate | 2--10 kg/hr (higher throughput) |
| Noise | 110--130 dB |
| Cost | Lower capital and operating cost |
| Typical parts | Landing gear, hydraulic rods, rolls |
| Oxide content | < 0.5% |
| Wear rate (ASTM G65) | 1--5 x 10^-7 mm3/Nm |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.5", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `More accessible, higher throughput, broader availability -- the standard for industrial hard-chrome replacement` -- Inter Medium, 12 pt, `#2EC4B6`

---

### ZONE 6 -- Troubleshooting Quick Hits

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
| 1 | 0.5" | POROSITY IN COATING | Insufficient particle velocity or poor gas ratios | Verify O2/C2H2 ratio; check barrel condition; increase frequency |
| 2 | 6.33" | POOR BOND STRENGTH | Surface contamination or stale grit blast | Re-blast; reduce time between blast and spray; verify cleanliness |
| 3 | 12.16" | UNEVEN THICKNESS | Robot path error or inconsistent powder charge | Re-program traverse; verify metering system calibration |
| 4 | 18.0" | EXCESSIVE NOISE / VIBRATION | Barrel wear or misalignment; fixture resonance | Inspect barrel bore; check water cooling; isolate fixture from detonation pulses |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for detonation gun (D-Gun) systems. D-Gun technology is semi-proprietary -- systems and parameters vary by manufacturer. Specific parameters depend on equipment configuration, feedstock material, and application specification. Consult your process engineer and equipment supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> D-Gun Spray -- Process Flow

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
| Zone 2 - Hero Callout | Big stat callout (velocity + detonation mechanism) |
| Zone 3 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 4 - Parameter Table | Section label, 10-row table |
| Zone 5 - D-Gun vs. HVOF | Section label, two comparison callouts |
| Zone 6 - Troubleshooting | Section label, four problem cards |
| Zone 7 - Footer | Footer band, disclaimer, title, series, logo, version |

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
| `D-Gun Spray Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `D-Gun Spray Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `D-Gun Spray Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `D-Gun Spray Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `D-Gun Spray Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `D-Gun Spray Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the D-Gun cluster. The hero story is CONTROLLED DETONATION -- the most violent and precise thermal spray process. The "750--1000 m/s" stat callout needs to land before the flow diagram, paired with the detonation mechanism explanation. The D-Gun vs. HVOF comparison is critical because HVOF is the most obvious competitor -- D-Gun wins on coating quality but loses on throughput, cost, and accessibility. The flow diagram uses the same U-flow layout as Cold Spray (poster 519) for series consistency across thermal spray clusters.

Stage 9 is labeled "Grinding" rather than "Machining" because D-Gun coatings (primarily WC-Co) require diamond grinding -- conventional machining tools cannot cut these extremely hard coatings. This is a key difference from Cold Spray where conventional machining works.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #529 -- Construction Workup v1.0*
*2026-04-26*
