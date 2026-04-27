---
Project: Plating Posters Inc
Poster Number: 409
Title: "CVD (Chemical Vapor Deposition) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD)"
Technical Source: Industry-standard thermal CVD coating process covering hot-wall reactor systems for cemented carbide cutting inserts. Values are typical ranges for TiC, TiN, TiCN (MT-CVD), and Al2O3 multilayer stacks. Temperatures 700-1100 C, H2 carrier gas, chloride precursors.
Process Scope: CVD -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - ThermalCVD
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #409 -- Construction Workup
## CVD (Chemical Vapor Deposition) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CVD. It maps the complete 10-stage process from part inspection through post-treatment and release -- every stage visible in a two-row flow diagram. CVD operates at much higher temperatures than PVD (800-1100 C vs. 200-500 C), uses chemical reactions instead of physical transfer, and is the dominant coating method for cemented carbide cutting inserts worldwide.

Design philosophy: mirrors the PVD Process Flow poster (#399) structure -- two-row flow diagram as hero, parameter summary table, a "Thermal CVD vs. MT-CVD" comparison callout, and a common failures strip. Operators familiar with the PVD poster will instantly navigate this one.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a two-row flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Same geometry as PVD #399.
2. **Parameter summary table (Block D):** Compact 10-row table (one row per stage).
3. **"Thermal CVD vs. MT-CVD" comparison callout (Block E):** Two side-by-side callout boxes.
4. **Common failures quick-hit strip (Block F):** Horizontal strip of 4 common failures.
5. **4 pt left-border accents on callout boxes.**
6. **Global Colors / swatch remap for Light edition.**

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
| Amber | `#E8A020` | Equipment & temperature stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & preparation stages, structural positives |
| Emerald | `#27AE60` | Deposition stage, optimal reference |
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
  Block B: Ten-stage two-row flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 4 -- THERMAL CVD VS. MT-CVD COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Thermal CVD vs. MT-CVD side-by-side callout

ZONE 5 -- COMMON FAILURES QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-failure strip with one-line fixes

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

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> CHEMICAL VAPOR DEPOSITION (CVD)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- 10 Stages from Part Inspection to Post-Treatment

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Chemical reactions at 800-1100 C deposit TiC, TiN, TiCN, and Al2O3 onto cemented carbide inserts. H2 carrier gas, chloride precursors, hot-wall furnace. The dominant coating method for indexable cutting tools worldwide.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE CVD CYCLE -- STAGE BY STAGE

---

**BLOCK B -- Ten-Stage Two-Row Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Two rows of five boxes.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1--5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Inspection | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Cleaning | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Loading | Box 3 | 9.7" | `#2EC4B6` (Teal) | Loading |
| 4. Seal & Purge | Box 4 | 14.3" | `#E8A020` (Amber) | Equipment |
| 5. Heat to Temp | Box 5 | 18.9" | `#E8A020` (Amber) | Equipment |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.1", Y: 8.3"
- To: X: 21.1", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6--10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Stabilize | Box 6 | 18.9" | `#E8A020` (Amber) | Equipment |
| 7. Deposition | Box 7 | 14.3" | `#27AE60` (Emerald) | Deposition |
| 8. Purge Between Layers | Box 8 | 9.7" | `#27AE60` (Emerald) | Deposition |
| 9. Cooldown | Box 9 | 5.1" | `#E8A020` (Amber) | Post-Treatment |
| 10. Inspect & Post-Treat | Box 10 | 0.5" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Inspection:*
- Stage badge: Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Stage name: `Part Inspection` Barlow SemiBold, 20 pt, `#F0EDE8`
- Key parameters: JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Verify dimensions
Check surface condition
Confirm material grade (WC-Co)
```
- Purpose: Inter Regular, 12 pt, `#F0EDE8` at 70%
- `Ensure substrates meet specification before coating`
- Critical check: Inter Medium, 11 pt, `#2EC4B6`
- `CHECK: No grinding burn or cobalt depletion`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Ultrasonic alkaline wash` / `DI water rinse` / `Dry` / `H2 pre-bake in furnace`
- Purpose: `Remove contaminants; H2 bake removes surface oxides in situ`
- Check: `Organic contamination = carbon inclusions in coating` (`#E05C5C`)

*Box 3 -- Loading:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Loading`
- Parameters: `Graphite or ceramic trays` / `Stack in furnace retort` / `Ensure gas flow paths clear`
- Purpose: `Position parts for uniform gas exposure`
- Check: `Overloading = gas depletion at center of load`

*Box 4 -- Seal & Purge:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Seal & Purge`
- Parameters: `Close retort` / `Purge with Ar or N2` / `Displace all air (O2 < 100 ppm)`
- Purpose: `Remove oxygen to prevent oxidation during heat-up`
- Check: `CRITICAL: Air + H2 at temperature = explosion risk` (`#E05C5C`)

*Box 5 -- Heat to Temperature:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Heat to Temperature`
- Parameters: `Ramp 5-15 C/min` / `Under H2 flow` / `Target: 900-1050 C`
- Purpose: `Reach deposition temperature without thermal shock`
- Check: `Multi-zone uniformity: +/- 5 C across work zone`

*Box 6 -- Stabilize:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Stabilize`
- Parameters: `Hold at temperature 15-30 min` / `Confirm uniform temp distribution` / `H2 flow continues`
- Purpose: `Ensure all parts at target temperature before precursor introduction`
- Check: `Thermocouple readings must converge within +/- 5 C`

*Box 7 -- Deposition:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Deposition`
- Parameters: `Introduce precursors (TiCl4, CH4, N2, AlCl3, CO2)` / `H2 carrier gas` / `50-500 mbar` / `1-8 hrs per layer`
- Purpose: `Chemical reaction deposits solid coating from gaseous precursors`
- Check: `Monitor gas flows, pressure, temperature continuously`

*Box 8 -- Purge Between Layers:*
- Badge: `STAGE 8`, fill `#27AE60`
- Name: `Purge Between Layers`
- Parameters: `H2 purge 10-30 min` / `Clear previous precursors` / `Before introducing next layer chemistry`
- Purpose: `Prevent cross-contamination between coating layers`
- Check: `Essential for multilayer stacks (TiN/TiCN/Al2O3)`

*Box 9 -- Cooldown:*
- Badge: `STAGE 9`, fill `#E8A020`
- Name: `Cooldown`
- Parameters: `2-10 C/min controlled` / `Under H2 or Ar atmosphere` / `Critical 900-700 C range for WC-Co`
- Purpose: `Prevent thermal shock, oxidation, and eta-phase formation`
- Check: `Too fast = coating cracks; too slow = eta-phase in WC-Co` (`#E05C5C`)

*Box 10 -- Inspect & Post-Treat:*
- Badge: `STAGE 10`, fill `#27AE60`
- Name: `Inspect & Post-Treat`
- Parameters: `Visual + thickness` / `Wet/dry blasting (optional)` / `Edge honing` / `Documentation`
- Purpose: `Verify quality; smooth surface; prepare for use`
- Check: `Post-coat blasting improves surface finish and adds compressive stress`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Loading` |
| `#E8A020` (Amber) | `Equipment & Temperature` |
| `#27AE60` (Emerald) | `Deposition & Quality` |
| `#E05C5C` (Coral) | `Caution / Safety` |

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
- Stage (3.5") | Key Spec (5.5") | Temperature (3.0") | Time (3.0") | Pressure (4.0") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Stage | Key Spec | Temp | Time | Pressure | Key Control |
|---|---|---|---|---|---|
| 1. Part Inspection | WC-Co grade verify | Ambient | -- | -- | Surface condition |
| 2. Cleaning | Alk wash + H2 bake | 50-60 C (wash) | 5-15 min | -- | No organics |
| 3. Loading | Graphite trays | Ambient | -- | -- | Gas flow paths |
| 4. Seal & Purge | Ar/N2 purge | Ambient | 15-30 min | Atmospheric | O2 < 100 ppm |
| 5. Heat-Up | H2 flow, ramp | 900-1050 C | 1-2 hr | Sub-atm | +/- 5 C uniformity |
| 6. Stabilize | H2 flow, hold | 900-1050 C | 15-30 min | Sub-atm | Thermocouple convergence |
| 7. Deposition | TiCl4/CH4/N2/AlCl3 | 700-1050 C | 1-8 hr/layer | 50-500 mbar | Gas ratio control |
| 8. Layer Purge | H2 purge | Process temp | 10-30 min | Sub-atm | Clear precursors |
| 9. Cooldown | Controlled cool | 1050 -> ambient | 2-8 hr | H2 or Ar atm | 2-10 C/min |
| 10. Inspect/Post | Blast + measure | Ambient | -- | -- | Thickness + adhesion |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Thermal CVD vs. MT-CVD Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THERMAL CVD VS. MT-CVD -- WHICH APPROACH?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Thermal CVD (HT-CVD):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `THERMAL CVD (HT-CVD)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Classic Method` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Temperature | 1000-1050 C |
| Pressure | 50-200 mbar |
| Carrier gas | H2 (balance) |
| Precursors | TiCl4, CH4, N2, AlCl3, CO2 |
| Key coatings | TiC, TiN, alpha-Al2O3 |
| Deposition rate | 0.5-3 um/hr |
| Grain structure | Columnar, coarse (1-5 um grains) |
| Substrate limit | WC-Co only (HSS too soft at this temp) |
| Adhesion | Excellent (chemical bonding) |
| Limitation | High temp degrades WC-Co toughness |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Best for alpha-Al2O3 top coats -- the gold standard oxide layer for high-temperature cutting` -- Inter Medium, 13 pt, `#E8A020`

**Right -- MT-CVD (Moderate Temperature):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `MT-CVD (MODERATE TEMPERATURE)` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `The Modern Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Temperature | 700-900 C |
| Pressure | 50-200 mbar |
| Carrier gas | H2 (balance) |
| Precursors | TiCl4, CH3CN (acetonitrile) |
| Key coatings | TiCN (the thick wear layer) |
| Deposition rate | 2-5 um/hr (faster) |
| Grain structure | Finer columnar (0.5-2 um grains) |
| Substrate limit | WC-Co; less toughness loss vs. HT |
| Adhesion | Good (lower temp = less diffusion bonding) |
| Limitation | Cannot produce alpha-Al2O3 |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `TiCN by MT-CVD is the thick functional layer in modern inserts -- 8-12 um of wear resistance at lower substrate damage` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 5 -- Common Failures Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON CVD FAILURES

---

**BLOCK F -- Four Failure Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DELAMINATION / ETA-PHASE | Co3W3C at interface from high-temp HCl attack on cobalt | Use TiN interlayer; consider MT-CVD for inner layers |
| 2 | 6.33" | EGG-SHELL CRACKING | Thermal expansion mismatch; cooling too fast | Control cooling rate 2-10 C/min; limit single-layer thickness |
| 3 | 12.16" | SOOT / CARBON INCLUSIONS | Excess CH4; hydrocarbon cracking | Optimize gas ratios; maintain furnace cleanliness |
| 4 | 18.0" | WRONG Al2O3 PHASE | Nucleation conditions incorrect | Control oxidation pulse precisely; verify temperature |

Interior per card:
- Failure: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for thermal CVD hard coatings on cemented carbide cutting inserts. Specific furnace settings, gas compositions, and cycle recipes vary by equipment manufacturer and coating specification. Consult your equipment supplier and process documentation.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> CVD (Chemical Vapor Deposition) -- Process Flow

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
| Zone 4 - CVD vs MT-CVD | Section label, two comparison callouts |
| Zone 5 - Common Failures | Section label, four failure cards |
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
| `CVD Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `CVD Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `CVD Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `CVD Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `CVD Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `CVD Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This poster mirrors the PVD Process Flow (#399) in structure, making the entire SA cluster family feel cohesive. The key difference: CVD is a chemical process at much higher temperatures, uses H2 carrier gas (explosion hazard), produces HCl byproducts (corrosion/toxicity), and is primarily used for cemented carbide cutting inserts rather than the broader range of substrates that PVD can handle. Total cycle time is 12-24 hours -- much longer than PVD's 4-10 hours.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #409 -- Construction Workup v1.0*
*2026-04-26*
