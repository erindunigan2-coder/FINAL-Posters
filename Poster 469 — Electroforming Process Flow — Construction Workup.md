---
Project: Plating Posters Inc
Poster Number: 469
Title: "Electroforming -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 8: Electroforming)"
Technical Source: Industry-standard electroforming process using nickel sulfamate or copper sulfate baths. Covers the complete 10-stage sequence from mandrel fabrication through post-processing. Values are typical ranges for the dominant Ni sulfamate system.
Process Scope: Electroforming -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #469 -- Construction Workup
## Electroforming -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Electroforming -- the process that makes electroplating's product the final part rather than a coating. The key conceptual distinction is front and center: in electroplating, the deposit stays on the part; in electroforming, the deposit IS the part, and the mandrel is removed. The hero is a 10-stage U-flow (two rows of five) covering the full sequence from mandrel fabrication to final post-processing.

Design philosophy: clean U-flow diagram, a compact parameter table, a "How Electroforming Differs from Electroplating" callout panel, and an applications showcase. Dense but scannable.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box color-coded by stage type.
2. **Parameter summary table (Block D):** Compact 10-row table with key parameters.
3. **"How EF Differs" callout (Block E):** Single callout comparing electroforming to electroplating.
4. **Applications strip (Block F):** Industry applications with metal and thickness.

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
| Amber | `#E8A020` | Key parameters, mandrel-related stages |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Electroforming deposition stage, optimal reference |
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
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table

ZONE 4 -- HOW ELECTROFORMING DIFFERS (22.0"--28.5" / ~6.5" tall)
  Block E: Electroforming vs Electroplating comparison

ZONE 5 -- APPLICATIONS SHOWCASE (28.5"--32.5" / ~4.0" tall)
  Block F: Industry applications strip

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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> ELECTROFORMING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 10 Stages from Mandrel to Finished Part

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Electrodeposition where the deposit IS the product. The mandrel shapes it. The bath builds it. Separation reveals it.

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
| 1. Mandrel Fabrication | Box 1 | 0.5" | `#E8A020` (Amber) | Mandrel Prep |
| 2. Mandrel Surface Prep | Box 2 | 5.0" | `#E8A020` (Amber) | Mandrel Prep |
| 3. Release Agent / Conductive Layer | Box 3 | 9.5" | `#E8A020` (Amber) | Mandrel Prep |
| 4. Rack & Connect | Box 4 | 14.0" | `#2EC4B6` (Teal) | Setup |
| 5. Initial Low-Current Strike | Box 5 | 18.5" | `#27AE60` (Emerald) | Deposition |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 20.6", Y: 8.3"
- To: X: 20.6", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Full-Current Electroform | Box 6 | 18.5" | `#27AE60` (Emerald) | Core Process |
| 7. Remove & Rinse | Box 7 | 14.0" | `#2EC4B6` (Teal) | Rinse |
| 8. Mandrel Separation | Box 8 | 9.5" | `#E8A020` (Amber) | Separation |
| 9. Post-Processing | Box 9 | 5.0" | `#C8D0D8` (Silver) | Finishing |
| 10. Inspect & Document | Box 10 | 0.5" | `#C8D0D8` (Silver) | QA |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Mandrel Fabrication:*
- Badge: `STAGE 1`, fill `#E8A020`, text `#1A1F2E`
- Name: `Mandrel Fabrication`
- Parameters: `Machine, cast, or 3D-print` / `Shape = final part shape` / `Include draft angles (1--3 deg)`
- Purpose: `Create the form the deposit will grow on`
- Check: `Dimensional accuracy of mandrel = dimensional accuracy of part`

*Box 2 -- Mandrel Surface Prep:*
- Badge: `STAGE 2`, fill `#E8A020`
- Name: `Mandrel Surface Prep`
- Parameters: `Polish to required finish` / `Mandrel Ra = part exterior Ra` / `Optical: Ra < 0.01 um`
- Purpose: `Mandrel surface IS the part's exterior surface`
- Check: `Defects in mandrel = defects in part`

*Box 3 -- Release Agent / Conductive Layer:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Release Agent / Make Conductive`
- Parameters: `Permanent: Cr passivation dip` / `Expendable: no release needed` / `Non-conductive: electroless Ni or Ag paint`
- Purpose: `Enable separation + ensure conductivity`
- Check: `Fresh release agent each cycle for permanent mandrels`

*Box 4 -- Rack & Connect:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rack & Connect`
- Parameters: `Mount mandrel in tank` / `Connect as CATHODE (-)` / `Position anodes (Ni or Cu)`
- Purpose: `Establish electrical circuit for deposition`
- Check: `Good electrical contact; conforming anode placement`

*Box 5 -- Initial Low-Current Strike:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Low-Current Strike`
- Parameters: `50--75% of full CD` / `10--30 min` / `Ensures uniform nucleation`
- Purpose: `Seed the deposit before full-rate build`
- Check: `Avoids burning at edges and high-CD areas`

*Box 6 -- Full-Current Electroform:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Electroform` / Subtitle: `MANDREL IS CATHODE (-)` (16 pt, `#27AE60`)
- Parameters: `Ni sulfamate: 3--5 A/dm2` / `40--55 C, pH 3.5--4.5` / `Build to target thickness` / `Hours to weeks`
- Purpose: `Grow the deposit to required wall thickness`
- Check: `CRITICAL: Monitor stress, thickness, bath chemistry` (Coral `#E05C5C`)

*Box 7 -- Remove & Rinse:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Remove & Rinse`
- Parameters: `Remove from bath` / `Thorough DI water rinse` / `Remove all electrolyte`
- Purpose: `Stop deposition; clean before separation`
- Check: `Electrolyte trapped in recesses causes staining`

*Box 8 -- Mandrel Separation:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Mandrel Separation`
- Parameters: `Mechanical (pry, flex)` / `Thermal differential` / `Chemical dissolution (NaOH, HCl)` / `Melt-out (low-mp alloy)`
- Purpose: `Free the electroformed part from the mandrel`
- Check: `Interior surface is the precision surface -- handle with care`

*Box 9 -- Post-Processing:*
- Badge: `STAGE 9`, fill `#C8D0D8`
- Name: `Post-Processing`
- Parameters: `Trim flash at edges` / `Machine to final dimensions` / `Anneal (optional): 400--600 C` / `External plating if needed`
- Purpose: `Bring part to final specification`
- Check: `Interior surface must not be damaged during machining`

*Box 10 -- Inspect & Document:*
- Badge: `STAGE 10`, fill `#C8D0D8`
- Name: `Inspect & Document`
- Parameters: `Thickness uniformity` / `Interior surface finish (Ra)` / `Hardness, ductility, stress` / `Dimensional accuracy (CMM)`
- Purpose: `Verify part meets all specifications`
- Check: `Full documentation per ASTM B832`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#E8A020` (Amber) | `Mandrel Preparation` |
| `#2EC4B6` (Teal) | `Setup & Rinse` |
| `#27AE60` (Emerald) | `Electroforming (Core)` |
| `#C8D0D8` (Silver) | `Post-Process & QA` |
| `#E05C5C` (Coral) | `Caution / Critical` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

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
- Stage (3.0") | Chemistry/Material (5.5") | Temperature (2.5") | Time (2.5") | Current Density (3.5") | Key Control (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

| Stage | Chemistry/Material | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Mandrel Fab | SS, Al, wax, plastic, low-mp alloy | -- | -- | -- | Shape + draft angle |
| 2. Surface Prep | Grinding, polishing compounds | -- | -- | -- | Ra matches part spec |
| 3. Release/Conduct | K2Cr2O7 2--5%; electroless Ni; Ag paint | 20--50 C | 30--60 sec | -- | Fresh each cycle |
| 4. Rack & Connect | Ti or Cu fixtures; Ni or Cu anodes | -- | -- | -- | Contact + anode placement |
| 5. Strike | Ni sulfamate or Cu sulfate | 40--55 C | 10--30 min | 1.5--3.5 A/dm2 | Uniform nucleation |
| 6. Electroform | Ni sulfamate: 300--450 g/L Ni(NH2SO3)2 | 40--55 C | Hours--weeks | 3--5 A/dm2 | Stress < 35 MPa; thickness |
| 7. Remove/Rinse | DI water | Ambient | 2--5 min | -- | Remove all electrolyte |
| 8. Separation | NaOH 10--20%; HCl; heat; mechanical | 20--80 C | Varies | -- | Protect interior surface |
| 9. Post-Process | Trimming, machining, annealing | 400--600 C anneal | 1--2 hr anneal | -- | Do not damage interior |
| 10. Inspect | Micrometer, CMM, profilometer | -- | -- | -- | ASTM B832 |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.
Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 4 -- How Electroforming Differs

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> ELECTROFORMING VS. ELECTROPLATING

---

**BLOCK E -- Two-Panel Comparison**

Y: 22.9" to 28.3".

**Left -- Electroforming (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.2", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `ELECTROFORMING` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `The deposit IS the product` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
- Deposit is separated from the mandrel
- The mandrel is temporary (removed)
- Thickness: 25 um to 25 mm
- Build time: hours to weeks
- Interior surface replicates mandrel finish
- Applications: waveguides, molds, screens,
  printing plates, precision reflectors
- Bath chemistry: same as electroplating
  (Ni sulfamate, acid Cu, etc.)
```

**Right -- Electroplating (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.2", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `ELECTROPLATING` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `The deposit stays on the part` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
- Deposit permanently bonds to substrate
- The substrate is the final part
- Thickness: 1 um to 250 um (typical)
- Build time: minutes to hours
- Exterior surface is the visible surface
- Applications: corrosion protection,
  wear resistance, decorative finish
- Same bath chemistry, different goal
```

Bottom callout spanning both panels (Y: 28.0"):
- Rounded rect, X: 0.5", W: 23.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Same chemistry. Same physics. Different intent. In electroforming, the plating bath is not a surface treatment -- it is a manufacturing process.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Applications Showcase

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> KEY APPLICATIONS

---

**BLOCK F -- Six Application Cards (Y: 29.4" to 32.3")**

Six cards in a single row. Gap: 0.2".

Each card: Rounded rect, W: 3.6", H: 2.7", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | X | Application | Metal | Thickness | Accent |
|---|---|---|---|---|---|
| 1 | 0.5" | Waveguides & Reflectors | Ni, Cu | 0.5--5 mm | `#27AE60` |
| 2 | 4.3" | Printing Plates & Holograms | Ni | 100--500 um | `#E8A020` |
| 3 | 8.1" | Precision Screens & Meshes | Ni, Cu | 25--250 um | `#2EC4B6` |
| 4 | 11.9" | Mold Inserts & Tooling | Ni, Ni-Co | 2--10 mm | `#E8A020` |
| 5 | 15.7" | CD/DVD Stampers | Ni | 100--300 um | `#2EC4B6` |
| 6 | 19.5" | LIGA Microstructures | Ni | 10--1000 um | `#27AE60` |

Interior per card:
- Application: Barlow SemiBold, 13 pt, accent color
- Metal: JetBrains Mono 11 pt, `#F0EDE8`
- Thickness: JetBrains Mono 11 pt, `#F0EDE8` at 70%

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for nickel sulfamate electroforming. Specific formulations, current densities, and process limits vary by metal, mandrel type, and application. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B832; ASM Handbook Vol. 5.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroforming -- Process Flow

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
| Zone 4 - EF vs EP | Section label, two comparison panels, bottom callout |
| Zone 5 - Applications | Section label, six application cards |
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

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Electroforming Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroforming Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroforming Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electroforming Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroforming Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroforming Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Electroforming cluster. The key conceptual breakthrough for the audience is: this is electroplating, but the deposit IS the product. That distinction must be visually unmistakable in the Zone 4 comparison. The mandrel-heavy first three stages (all Amber) visually signal that mandrel preparation is half the process -- which it is. The build times in Box 6 (hours to weeks) will surprise plating shop audiences accustomed to minutes-to-hours cycle times.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #469 -- Construction Workup v1.0*
*2026-04-26*
