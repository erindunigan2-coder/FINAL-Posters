---
Project: Plating Posters Inc
Poster Number: 519
Title: "Cold Spray -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Industry-standard cold spray (kinetic metallization) process. Covers complete 10-stage sequence from cleaning through final inspection. Values are typical ranges for high-pressure cold spray (HPCS) systems using nitrogen carrier gas. Watson research brief sourced from ASM Handbook Vol 5A, Pawlowski, ITSA Handbook, and ASTM/MIL-STD-3021.
Process Scope: Cold spray -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - ProcessFlow
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #519 -- Construction Workup
## Cold Spray -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for TS-05: Cold Spray. The hero story is the "no melting" principle -- particles bond in the solid state via supersonic impact and plastic deformation. No other thermal spray process can make this claim. The poster shows the complete process sequence at a glance in a U-flow diagram, with a comparison callout (Cold Spray vs. Conventional Thermal Spray) and a troubleshooting quick-hit strip.

Cold spray is unique: zero oxidation, zero phase change, zero thermal residual stress, compressive stress in the deposit, and near-bulk material properties. The Process Flow poster must make this the unmistakable headline.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **"No Melting" hero callout (Block C):** A prominent amber-tinted glass callout box directly below the headline, before the flow diagram, delivering the key differentiator: particles stay solid. Big stat number format.

3. **Parameter summary table (Block D):** A compact 10-row table (one row per stage) with key parameters.

4. **"Why Cold Spray?" comparison callout (Block E):** Two side-by-side callout boxes comparing Cold Spray vs. Conventional Thermal Spray.

5. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

6. **4 pt left-border accents on callout boxes.**

7. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

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

ZONE 2 -- "NO MELTING" HERO CALLOUT (2.9"--5.0" / ~2.1" tall)
  Block C: Big stat callout -- "600--1200 m/s" particle velocity, solid-state bonding message

ZONE 3 -- PROCESS FLOW DIAGRAM (5.0"--16.5" / ~11.5" tall)
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block B2: Stage legend strip (color key)

ZONE 4 -- PARAMETER SUMMARY TABLE (16.5"--22.5" / ~6.0" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 5 -- WHY COLD SPRAY? COMPARISON (22.5"--28.5" / ~6.0" tall)
  Block E: Cold Spray vs. Conventional Thermal Spray side-by-side

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

> COLD SPRAY

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- Solid-State Coating by Supersonic Impact

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> No melting. No oxidation. No phase change. Particles bond in the solid state -- the only thermal spray process that can say that.

---

### ZONE 2 -- "No Melting" Hero Callout

**Dimensions:** Full width within margins. Y: 2.9" to 5.0" (~2.1" tall).

**BLOCK C -- Big Stat Callout**

- Rounded rectangle, X: 0.5", Y: 3.1", W: 23.0", H: 1.6", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Amber-tinted glass treatment

**Stat number (left):**
- `600--1200 m/s` Barlow Condensed ExtraBold, 60 pt, `#E8A020`
- Position: X: 1.0", Y: 3.3"

**Label (right of stat):**
- `Particle velocity -- supersonic, solid-state impact` Barlow SemiBold, 22 pt, `#F0EDE8`
- Position: X: 10.0", Y: 3.3"

**Sub-label:**
- `Gas heated to 300--1100 C but particles NEVER MELT. Bonding is 100% kinetic -- adiabatic shear instability breaks oxide films and creates metallurgical welds at the interface.` Inter Regular, 14 pt, `#F0EDE8` at 70%
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
| 9. Machining | Box 9 | 5.1" | `#C8D0D8` (Silver) | Finishing |
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
Vapor degrease (legacy)
Remove all oils & machining fluids
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Eliminate organic contamination before blast`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after rinse`

*Box 2 -- Alkaline Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `50--70 C (120--160 F)` / `pH 10--12` / `5--15 min immersion`
- Purpose: `Remove residual soils; DI rinse for aerospace`
- Check: `Time to blast: < 4 hours (same shift preferred)`

*Box 3 -- Grit Blast:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Grit Blast`
- Parameters: `Al2O3 36--80 mesh` / `30--60 PSI` / `Ra 3--8 um`
- Purpose: `Activate surface; create anchor profile`
- Check: `Some applications skip grit blast -- CS impact self-activates` (`#E8A020`)

*Box 4 -- Masking:*
- Badge: `STAGE 4`, fill `#C8D0D8`
- Name: `Masking & Fixturing`
- Parameters: `Metal masks required` / `Tape NOT reliable (erosion)` / `Robot manipulation essential`
- Purpose: `Define spray zone; protect non-spray areas`
- Check: `Focused footprint: 5--15 mm diameter`

*Box 5 -- Equipment Setup:*
- Badge: `STAGE 5`, fill `#3A4055`, text `#F0EDE8`
- Name: `Equipment Setup`
- Parameters: `Gas: N2 or He at 20--60 bar` / `Heater: 300--1100 C` / `De Laval nozzle (WC-Co throat)`
- Purpose: `Configure gas, powder feeder, and nozzle`
- Check: `HPCS vs. LPCS: verify system class for material`

*Box 6 -- Parameter Set:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Parameter Setup`
- Parameters: `Pressure: 20--60 bar` / `Gas temp: 300--1100 C` / `Standoff: 10--50 mm`
- Purpose: `Achieve material-specific critical velocity`
- Check: `He = 2.6x velocity vs. N2 but 10--50x cost`

*Box 7 -- Spray Application:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Spray Application`
- Parameters: `50--500 um per pass` / `No substrate preheat needed` / `600--1200 m/s (HPCS)`
- Purpose: `Build coating by solid-state particle impact`
- Check: `Ductile metals only: Cu, Al, Ti, Ni, Ag, Zn`

*Box 8 -- Post-Treatment:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Heat treat optional` / `Cu: 200--400 C anneal` / `Ti: 500--700 C vacuum anneal`
- Purpose: `Recover ductility; improve inter-particle bonding`
- Check: `Sealing rarely needed (porosity < 1%)`

*Box 9 -- Machining:*
- Badge: `STAGE 9`, fill `#C8D0D8`
- Name: `Machining`
- Parameters: `Conventional turning/milling/drilling` / `Machines like wrought material` / `Tight tolerances achievable`
- Purpose: `Achieve final dimensions and surface finish`
- Check: `Major advantage: no special tooling required`

*Box 10 -- Inspection & QA:*
- Badge: `STAGE 10`, fill `#2EC4B6`
- Name: `Inspection & QA`
- Parameters: `ASTM C633 bond strength` / `ASTM E2109 porosity` / `ASTM E384 microhardness`
- Purpose: `Verify coating meets specification`
- Check: `MIL-STD-3021 for aerospace cold spray repair`

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
| `#C8D0D8` (Silver) | `Masking & Machining` |
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
- Stage (3.5") | Key Spec (5.5") | Temperature (3.0") | Time/Speed (3.5") | Standoff/Pressure (3.5") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.4". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.45".

| Stage | Key Spec | Temp | Time/Speed | Standoff/Pressure | Key Control |
|---|---|---|---|---|---|
| 1. Solvent Degrease | Aqueous alkaline or vapor | Ambient--70 C | 5--15 min | -- | Water-break-free |
| 2. Alkaline Clean | pH 10--12, immersion | 50--70 C | 5--15 min | -- | DI rinse (aerospace) |
| 3. Grit Blast | Al2O3 36--80 mesh | Ambient | Per coverage | 30--60 PSI | Ra 3--8 um |
| 4. Masking | Metal masks; no tape | -- | -- | -- | 5--15 mm footprint |
| 5. Equipment Setup | De Laval nozzle, N2/He | -- | -- | 20--60 bar | HPCS vs. LPCS class |
| 6. Parameter Set | Gas temp + pressure | 300--1100 C (gas) | -- | 20--60 bar | Critical velocity |
| 7. Spray | 600--1200 m/s (HPCS) | Substrate stays cool | 100--500 mm/s | 10--50 mm | Ductile metals only |
| 8. Post-Treatment | Anneal (optional) | Material-dependent | 1--4 hr | -- | Recover ductility |
| 9. Machining | Conventional tools | Ambient | Per dimension | -- | Machines like wrought |
| 10. Inspection | C633, E2109, E384 | -- | -- | -- | MIL-STD-3021 |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 5 -- Why Cold Spray? Comparison

**Dimensions:** Y: 22.5" to 28.5" (~6.0" tall).

---

**Section label:**
- Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY COLD SPRAY? -- VS. CONVENTIONAL THERMAL SPRAY

---

**BLOCK E -- Side-by-Side Comparison**

Y: 23.3" to 28.3".

**Left -- Cold Spray:**
- Rounded rect, X: 0.5", Y: 23.3", W: 11.0", H: 4.8", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `COLD SPRAY` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Solid-State Revolution` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Particle state | SOLID -- no melting |
| Oxidation | ZERO -- no thermal exposure |
| Residual stress | Compressive (beneficial) |
| Phase change | None -- feedstock = coating |
| Porosity | < 1% (Cu < 0.5%) |
| Heat-affected zone | None |
| Substrate heating | Minimal -- spray polymers & composites |
| Materials | Ductile metals: Cu, Al, Ti, Ni, Ag |
| Fume generation | Minimal (no melting) |
| Thickness limit | Virtually unlimited (additive buildup) |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.5", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `The only thermal spray that preserves feedstock properties -- no oxide, no decomposition` -- Inter Medium, 12 pt, `#2EC4B6`

**Right -- Conventional Thermal Spray (Plasma/HVOF/Flame):**
- Rounded rect, X: 12.0", Y: 23.3", W: 11.5", H: 4.8", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CONVENTIONAL THERMAL SPRAY` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Melt-and-Splat` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Particle state | Molten or semi-molten |
| Oxidation | Significant (oxide stringers in coating) |
| Residual stress | Tensile (can cause cracking) |
| Phase change | Common -- decarburization, amorphous phases |
| Porosity | 0.5--15% (process dependent) |
| Heat-affected zone | Yes -- substrate affected |
| Substrate heating | Significant -- limits substrate choice |
| Materials | Metals, ceramics, cermets |
| Fume generation | High (molten particles) |
| Thickness limit | Typically < 2 mm (stress buildup) |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.5", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Broader material range (ceramics, cermets) but thermal damage is inherent to the process` -- Inter Medium, 12 pt, `#E8A020`

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
| 1 | 0.5" | LOW DEPOSITION EFFICIENCY | Velocity below critical threshold | Increase gas pressure or gas temperature; verify powder size |
| 2 | 6.33" | POOR ADHESION | Surface contamination or insufficient profile | Re-blast; verify water-break-free; reduce time to spray |
| 3 | 12.16" | POROSITY IN DEPOSIT | Velocity too low or wrong powder morphology | Increase pressure; use spherical gas-atomized powder |
| 4 | 18.0" | NOZZLE CLOGGING | Powder buildup on nozzle throat (especially with Al, Cu) | Clean nozzle; reduce gas temp; use WC-Co nozzle throat |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for high-pressure cold spray (HPCS) systems. Low-pressure cold spray (LPCS) operates at reduced pressures and velocities. Specific parameters vary by equipment manufacturer, feedstock material, and application specification. Consult your process engineer and equipment supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Cold Spray -- Process Flow

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
| Zone 2 - Hero Callout | Big stat callout (velocity + no melting) |
| Zone 3 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 4 - Parameter Table | Section label, 10-row table |
| Zone 5 - Why Cold Spray | Section label, two comparison callouts |
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
| `Cold Spray Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cold Spray Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cold Spray Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Cold Spray Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cold Spray Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Cold Spray Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Cold Spray cluster. The hero story is NO MELTING -- the single concept that separates cold spray from every other thermal spray process. The "600--1200 m/s" stat callout should hit the viewer before the flow diagram. The comparison section (Zone 5) must make it viscerally clear: cold spray preserves the powder's properties because nothing melts. The limitation is equally clear: ductile metals only -- no ceramics.

The flow diagram shows 10 stages (vs. 8 for electroplating) because thermal spray has distinct grit blast, masking, equipment setup, and machining stages that don't exist in wet plating. The U-flow fits 5 boxes per row comfortably at 24" width.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #519 -- Construction Workup v1.0*
*2026-04-26*
