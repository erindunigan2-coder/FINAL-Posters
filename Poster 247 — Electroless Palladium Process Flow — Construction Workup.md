---
Project: Plating Posters Inc
Poster Number: 247
Title: "Electroless Palladium -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Technical Source: Industry-standard electroless palladium plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Hypophosphite-based (Pd-P alloy) and hydrazine-based (pure Pd) variants. Primary application is ENEPIG diffusion barrier per IPC-4556.
Process Scope: Electroless palladium -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessPalladium
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #247 -- Construction Workup
## Electroless Palladium -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Electroless Palladium. It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Electroless palladium is the critical diffusion barrier layer in the ENEPIG stack (Electroless Nickel / Electroless Palladium / Immersion Gold) per IPC-4556. Its sole job is to prevent nickel from migrating into the gold layer, eliminating the "black pad" failure mode that plagues conventional ENIG. Also used for hydrogen permeation membranes on porous ceramic substrates.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (Pd-P alloy vs. pure Pd deposits), and a troubleshooting quick-hit strip. Dense but scannable -- the reference for the entire electroless palladium line.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Pd-P vs. Pure Pd" comparison callout (Block E):** Two side-by-side callout boxes comparing hypophosphite-reduced Pd-P alloy versus hydrazine-reduced pure palladium. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes. Similar to defect grid cards but in a single row.

5. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

6. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

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
| Amber | `#E8A020` | Activation & post-treatment stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Plating stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, contamination callouts |
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
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- Pd-P vs. PURE Pd COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Pd-P alloy vs. Pure Pd side-by-side callout

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

> ELECTROLESS PALLADIUM

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Post-Treatment

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The ENEPIG diffusion barrier. Ultra-thin Pd prevents nickel migration into gold -- eliminating black pad at the source.

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

Y: 3.8" to 14.0" (~10.2" tall). Two rows of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
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
| 5. Electroless Pd | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry/Final | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Alkaline Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Alkaline Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
60--80 C (140--176 F)
NaOH 30--60 g/L
3--10 min soak
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, organic films that inhibit catalytic activity`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `DI counterflow (2-stage min)`
- Purpose: `Remove alkaline cleaner before activation`
- Check: `Alkaline drag-in raises activation bath pH`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `ENEPIG: EN surface is catalytic` / `Non-conductive: Sn/Pd colloidal` / `Membranes: Sn sensitize + Pd activate`
- Purpose: `Create catalytic surface for Pd deposition`
- Check: `ENEPIG needs no separate Pd activation -- EN is catalytic` (Emerald `#27AE60`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `DI preferred`
- Purpose: `Remove activation chemistry drag-in`
- Check: `Minimize transfer time -- Pd oxidizes in air`

*Box 5 -- Electroless Palladium (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Electroless Pd` / Subtitle: `Main Tank`
- Parameters: `Pd: 0.5--3.0 g/L` / `pH 5.0--7.0 (hypo) or 9.0--11.0 (hydrazine)` / `40--70 C (105--158 F)` / `Rate: 1--5 um/hr`
- Purpose: `Deposit Pd or Pd-P diffusion barrier layer`
- Check: `ENEPIG target: 0.05--0.3 um thickness`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `DI counterflow`
- Purpose: `Remove Pd bath drag-out; stop deposition`
- Check: `Quick transfer to immersion gold in ENEPIG`

*Box 7 -- Post Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post Treatment`
- Parameters: `ENEPIG: proceed to Au` / `Membranes: anneal 400--600 C in N2/Ar` / `Connectors: optional Au flash`
- Purpose: `Application-specific finishing step`
- Check: `ENEPIG has no heat treatment between Pd and Au`

*Box 8 -- Dry/Final:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Final`
- Parameters: `Air knife + oven 60--80 C` / `ENEPIG: rinse, dry, N2 storage` / `Membranes: controlled atmosphere`
- Purpose: `Remove moisture; prepare for assembly or storage`
- Check: `Store ENEPIG in N2 or vacuum-sealed bags`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Rate/Thickness (4.0") | Key Control (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Rate/Thickness | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30--60 g/L + surfactant | 60--80 C | 3--10 min | -- | Water-break-free |
| 2. Rinse | DI counterflow | Ambient | 30--60 sec | -- | <50 uS/cm |
| 3. Activation | ENEPIG: none; Sn/Pd or PdCl2 | Ambient--45 C | 30 sec--5 min | -- | Substrate-dependent |
| 4. Rinse | DI counterflow | Ambient | 30--60 sec | -- | Minimize transfer time |
| 5. Electroless Pd | Pd 0.5--3.0 g/L + reducing agent | 40--70 C | Per spec | 1--5 um/hr | pH + temp critical |
| 6. Rinse | DI counterflow | Ambient | 30--60 sec | -- | Quick to next step |
| 7. Post Treatment | Application-specific | Varies | Varies | -- | ENEPIG: proceed to Au |
| 8. Dry/Final | Air knife + oven | 60--80 C | Per spec | -- | N2 storage for ENEPIG |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Pd-P vs. Pure Pd Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> REDUCING AGENT MATTERS -- Pd-P ALLOY VS. PURE Pd

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Pd-P Alloy (Hypophosphite Reduced):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `Pd-P ALLOY (HYPOPHOSPHITE)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Most Common Commercial` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Reducing agent | Sodium hypophosphite |
| Deposit | Pd-P alloy (1--7% P) |
| Structure | Amorphous |
| pH | 5.0--7.0 |
| Temperature | 40--70 C (105--158 F) |
| Hardness | 400--600 HV |
| H2 permeability | Moderate (P inhibits) |
| Bath life | 3--5 MTO |
| Safety | Standard chemical handling |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Industry standard for ENEPIG -- proven IPC-4556 compliance` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Pure Pd (Hydrazine Reduced):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `PURE Pd (HYDRAZINE)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Phosphorus-Free Deposit` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Reducing agent | Hydrazine hydrate |
| Deposit | Pure palladium (>99% Pd) |
| Structure | Crystalline |
| pH | 9.0--11.0 |
| Temperature | 50--70 C (122--158 F) |
| Hardness | 200--300 HV |
| H2 permeability | Excellent |
| Bath life | 2--4 MTO |
| Safety | Hydrazine is toxic / suspected carcinogen |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Preferred for hydrogen permeation membranes -- maximum H2 selectivity` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | SKIP PLATING | Contaminated surface; poor activation | Improve cleaning; verify catalytic surface |
| 2 | 6.33" | BATH DECOMPOSITION | Overheating, low stabilizer, under-loaded | Check stabilizer ppm; maintain loading ratio |
| 3 | 12.16" | THICKNESS VARIATION | Temperature or pH drift across bath | Improve agitation; tighten pH/temp control |
| 4 | 18.0" | BLACK PAD (ENEPIG) | Pd layer too thin; Ni migrates to Au | Verify Pd thickness 0.05--0.3 um per IPC-4556 |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless palladium plating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; IPC-4556.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Palladium -- Process Flow

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
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Pd-P vs Pure Pd | Section label, two comparison callouts |
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
| `Electroless Palladium Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Palladium Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Palladium Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electroless Palladium Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Palladium Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Palladium Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Electroless Palladium cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#248--#254) zoom into each stage individually. The Pd-P vs. Pure Pd comparison answers the most important chemistry question: which reducing agent should you choose? For ENEPIG, the answer is hypophosphite (proven, commercial, IPC-4556 compliant). For hydrogen membranes, the answer is hydrazine (maximum H2 permeability). The "black pad" callout in the troubleshooting strip is the single most important quality concern in the entire ENEPIG process -- if the Pd barrier layer fails, the whole stack fails.

---

*Alaina -- Poster #247 -- Construction Workup v1.0 -- 2026-04-26*
