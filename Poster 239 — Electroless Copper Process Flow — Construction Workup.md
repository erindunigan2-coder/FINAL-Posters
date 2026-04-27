---
Project: Plating Posters Inc
Poster Number: 239
Title: "Electroless Copper -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper)"
Technical Source: Industry-standard electroless (autocatalytic) copper plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for formaldehyde-based alkaline E-Cu baths per IPC-TM-650 and general industry practice.
Process Scope: Electroless copper -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCopper
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #239 -- Construction Workup
## Electroless Copper -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EL-04: Electroless Copper. Electroless copper is a fundamentally different beast from electroless nickel. The reducing agent is formaldehyde (HCHO) instead of hypophosphite. The bath is strongly alkaline (pH 11.5-13.0) instead of acid. The deposit is pure copper -- no phosphorus, no boron, no alloy. And the primary application is radically different: E-Cu is a thin-film seed layer (0.5-2.5 um) deposited on non-conductive surfaces to make them electrically conductive for subsequent electrolytic copper buildup. PCB through-hole plating is the dominant use case.

The 8-stage flow for PCB applications includes sensitization/activation via colloidal Sn/Pd catalyst and an accelerator step -- steps that do not exist in EN-P processes on metallic substrates. This makes the E-Cu process flow more complex than EN.

Design philosophy: U-flow diagram as the hero (8 stages), a compact parameter summary table, an application comparison callout (PCB vs. plastics metallization vs. EMI shielding), and a troubleshooting quick-hit strip. A formaldehyde safety callout is mandatory.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box color-coded by stage type.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters.

3. **Application comparison callout (Block E):** Three side-by-side callout boxes -- PCB Through-Hole vs. Plastics Metallization vs. EMI Shielding.

4. **Troubleshooting + formaldehyde safety strip (Block F):** Combined problem cards and HCHO safety warning.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, descriptions
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Activation stages, warning headers, formaldehyde safety |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Plating stage (main tank), optimal reference |
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
  Block B: Eight-stage U-flow diagram (top row 4, bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- APPLICATION COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: PCB vs. Plastics vs. EMI Shielding

ZONE 5 -- TROUBLESHOOTING + FORMALDEHYDE SAFETY (28.5"--32.5" / ~4.0" tall)
  Block F: 3-problem strip + HCHO safety callout

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Position: X: 0.5". Y: 0.5"
- Text (all caps):

> ELECTROLESS COPPER

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Font: Barlow SemiBold, 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Autocatalytic Copper -- Complete Process Flow -- 8 Stages

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Pure copper on any surface. The seed layer that makes non-conductors conductive. Formaldehyde-based alkaline bath at pH 11.5-13.0 -- the chemistry PCB fabrication is built on.

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

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row of four boxes, bottom row of four boxes, U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Cleaner/Conditioner | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Sn/Pd Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 8.3" (bottom center Box 4)
- To: X: 19.5", Y: 9.5" (top center Box 5)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Electroless Cu Bath | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Anti-Tarnish | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Electrolytic Cu Buildup | Box 8 | 0.5" | `#27AE60` (Emerald) | Next Step |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box:**

*Box 1 -- Cleaner/Conditioner:*

Stage badge: `STAGE 1`, fill `#2EC4B6`
Stage name: `Cleaner / Conditioner`
Key parameters:
```
40-55 C (105-130 F)
Alkaline surfactant (pH 10-12)
3-5 min
```
Purpose: `Remove drilling smear; condition dielectric for catalyst adsorption`
Check: `PCB: permanganate desmear for multilayer boards` (`#E8A020`)

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Ambient` / `DI counterflow 2-3 stage`
- Purpose: `Remove cleaner and permanganate residues`
- Check: `CRITICAL: Residual oxidizer poisons Pd catalyst` (Coral `#E05C5C`)

*Box 3 -- Sn/Pd Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Sn/Pd Activation`
- Parameters: `Pre-dip: HCl 150-250 mL/L` / `Catalyst: Sn/Pd colloidal, 35-45 C` / `Accelerator: HCl 50-100 mL/L`
- Purpose: `Deposit Pd nuclei on non-conductive surfaces`
- Check: `3-step process: Pre-dip --> Catalyst --> Accelerator`

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `DI counterflow 2-3 stage` / `Ambient`
- Purpose: `Remove acid from accelerator before alkaline E-Cu bath`
- Check: `CRITICAL: Acid drag-in to pH 12+ bath = pH crash` (Coral `#E05C5C`)

*Box 5 -- Electroless Cu Bath (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Electroless Cu Bath` / Subtitle: `Main Tank`
- Parameters: `CuSO4: 1.5-3.0 g/L Cu2+` / `HCHO: 1-3 g/L` / `EDTA: 25-40 g/L` / `pH 11.5-13.0 (NaOH)`
- Purpose: `Autocatalytic Cu deposition on Pd nuclei`
- Check: `Rate: 1-5 um/hr | Temp: 28-45 C (82-113 F)`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient` / `Double counterflow`
- Purpose: `Stop E-Cu reaction; remove drag-out`
- Check: `CRITICAL: Freshly plated Cu oxidizes rapidly in air` (Coral `#E05C5C`)

*Box 7 -- Anti-Tarnish (Optional):*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Anti-Tarnish`
- Parameters: `Benzotriazole or trivalent chromate` / `15-30 sec dip`
- Purpose: `Prevent Cu oxidation before electrolytic buildup`
- Check: `PCB: often skipped -- proceed directly to acid Cu`

*Box 8 -- Electrolytic Cu Buildup:*
- Badge: `STAGE 8`, fill `#27AE60`
- Name: `Electrolytic Cu Buildup` / Subtitle: `(Next Step)`
- Parameters: `Acid copper sulfate bath` / `25-50 um target thickness`
- Purpose: `Build conductive copper layer on E-Cu seed`
- Check: `This is ELECTROLYTIC plating -- rectifier required` (`#E8A020`)

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (E-Cu & Electrolytic)` |
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

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Key Control (8.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Cleaner/Conditioner | Alkaline + surfactant (pH 10-12) | 40-55 C | 3-5 min | Condition dielectric for Pd |
| 2. Rinse | DI counterflow | Ambient | 1-3 min | No oxidizer residue |
| 3. Sn/Pd Activation | Pre-dip + Sn/Pd catalyst + accelerator | 35-45 C | 3-7 min (catalyst) | Expose Pd nuclei |
| 4. Rinse | DI counterflow | Ambient | 1-2 min | < 30 uS/cm; no acid drag-in |
| 5. Electroless Cu Bath | CuSO4 + HCHO + EDTA, pH 11.5-13.0 | 28-45 C | Per spec | 1-5 um/hr; air agitation req'd |
| 6. Rinse | DI or city water | Ambient | 1-2 min | No air-dry |
| 7. Anti-Tarnish | Benzotriazole or Cr3+ | Ambient | 15-30 sec | Optional for PCB |
| 8. Electrolytic Cu | Acid copper sulfate | 20-30 C | Per spec | 25-50 um buildup |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Application Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THREE PRIMARY APPLICATIONS

---

**BLOCK E -- Three-Column Comparison**

Y: 22.9" to 28.3". Three side-by-side callout boxes.

**Left -- PCB Through-Hole (THIS POSTER'S PRIMARY APPLICATION):**
- Rounded rect, X: 0.5", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Full border: 2 pt `#27AE60` (highlighted)
- Title: `PCB THROUGH-HOLE` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Primary Application` -- 12 pt `#27AE60`

| Property | Value |
|---|---|
| Purpose | Seed layer on FR4 dielectric |
| Thickness | 0.5-2.5 um |
| Next step | Electrolytic acid Cu buildup (25-50 um) |
| Activation | Sn/Pd colloidal catalyst |
| Standard | IPC-TM-650, IPC-4562 |
| Volume | Highest volume E-Cu application |

Bottom: `The seed layer that makes through-holes conductive. Every multilayer PCB depends on this step.` Inter Medium, 12 pt, `#27AE60`

**Center -- Plastics Metallization:**
- Rounded rect, X: 8.17", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `PLASTICS METALLIZATION` -- Barlow SemiBold, 20 pt, `#E8A020`

| Property | Value |
|---|---|
| Purpose | Conductive base on ABS, PC, ceramics |
| Thickness | 0.5-2 um (seed) then electrolytic |
| Next step | Electrolytic Ni/Cu/Cr decorative |
| Activation | Chromic etch + Sn/Pd catalyst |
| Substrates | ABS, polycarbonate, ceramic |
| Note | Cr6+ etch required -- RoHS concern |

Bottom: `Decorative chrome on plastic. Automotive trim, consumer electronics.` Inter Medium, 12 pt, `#E8A020`

**Right -- EMI Shielding:**
- Rounded rect, X: 15.84", Y: 22.9", W: 7.66", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `EMI SHIELDING` -- Barlow SemiBold, 20 pt, `#2EC4B6`

| Property | Value |
|---|---|
| Purpose | Conductive Cu layer for EMI/RFI shielding |
| Thickness | 25-50 um (heavy-build E-Cu) |
| Next step | Anti-tarnish or electroless Ni overcoat |
| Substrates | Plastic housings, composites |
| Rate | 5-8 um/hr (heavy-build formulation) |
| Note | Only E-Cu application with thick deposit |

Bottom: `Heavy-build electroless copper. Electronics enclosures, aerospace composites.` Inter Medium, 12 pt, `#2EC4B6`

---

### ZONE 5 -- Troubleshooting + Formaldehyde Safety

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING + FORMALDEHYDE SAFETY

---

**BLOCK F -- Three Problem Cards + HCHO Safety Box**

Y: 29.4" to 32.3".

**Three problem cards (left):**
Each: W: 5.0", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NO DEPOSITION | Insufficient Pd activation or HCHO depleted | Check catalyst coverage; replenish formaldehyde |
| 2 | 5.83" | VOIDING / PITTING | H2 entrapment or insufficient wetting agent | Increase surfactant; improve air agitation |
| 3 | 11.16" | BATH DECOMPOSITION | Stabilizer low or temperature too high | Check stabilizer ppm; reduce temp |

Interior per card:
- Problem: Barlow SemiBold, 14 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

**HCHO Safety Box (right):**
- X: 16.5", W: 7.0", H: 2.7", fill `#1E2435`, FULL border 2 pt `#E05C5C`
- Title: `FORMALDEHYDE (HCHO) SAFETY` Barlow SemiBold 16 pt `#E05C5C`
- `OSHA PEL: 0.75 ppm TWA / 2 ppm STEL`
- `IARC Group 1: known human carcinogen`
- `Local exhaust ventilation REQUIRED`
- `Continuous air monitoring recommended`
- `Formaldehyde-free alternatives (glyoxylic acid) are emerging`
- Inter Regular 11 pt `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center.

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless (autocatalytic) copper plating. Specific formulations, concentrations, and process limits vary by proprietary product. Formaldehyde is a regulated substance -- comply with all OSHA, EPA, and local regulations. Source: General industry knowledge; IPC-TM-650.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Copper -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`.

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Application Comparison | Section label, three application callouts |
| Zone 5 - Troubleshooting + Safety | Section label, three problem cards, HCHO safety box |
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
| `E-Cu Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Cu Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Cu Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `E-Cu Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Cu Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Cu Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Electroless copper is fundamentally different from electroless nickel in every respect except the autocatalytic principle. The visual language should emphasize: (1) formaldehyde as the reducing agent -- not hypophosphite; (2) strongly alkaline pH 11.5-13.0 -- much higher than even EN Low-P; (3) thin-film seed layer, not a standalone functional coating; (4) the deposit is pure copper, not an alloy; (5) Sn/Pd colloidal activation is required on non-conductive surfaces.

The 8-stage flow includes the Sn/Pd activation complex (pre-dip, catalyst, accelerator) which makes it inherently more complex than the 7-stage EN flow. Stage 8 (Electrolytic Cu Buildup) is technically the next process, not part of E-Cu -- but it is included because E-Cu has no standalone function without it in PCB applications.

The formaldehyde safety callout is non-negotiable. HCHO is IARC Group 1 (known human carcinogen) and OSHA-regulated. Every E-Cu poster in this cluster should reference HCHO safety.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #239 -- Construction Workup v1.0*
*2026-04-26*
