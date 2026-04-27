---
Project: Plating Posters Inc
Poster Number: 263
Title: "Electroless Cobalt -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt)"
Technical Source: Industry-standard electroless cobalt plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for hypophosphite-based Co-P and DMAB-based Co-B alloy baths. Watson compiled from domain expertise (Gemini quota exhausted); Tyler spot-check recommended for deposition rates.
Process Scope: Electroless cobalt plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #263 -- Construction Workup
## Electroless Cobalt -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EL-07: Electroless Cobalt. It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Electroless cobalt is a niche but technically fascinating process: ferromagnetic deposits with tunable coercivity, historically the backbone of magnetic recording media, and now finding renewed life in MEMS and advanced semiconductor packaging as Co-W-P diffusion barriers. This poster is the "map" that the other 7 posters (#264--#270) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (Co-P vs. Co-W-P alloy), and a troubleshooting quick-hit strip. Dense but scannable -- the reference for the entire electroless cobalt line.

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

3. **"Co-P vs. Co-W-P" comparison callout (Block E):** Two side-by-side callout boxes comparing the binary and ternary alloy systems. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

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

ZONE 4 -- CO-P VS. CO-W-P COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Binary vs. ternary alloy side-by-side callout

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

> ELECTROLESS COBALT

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Anneal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Ferromagnetic autocatalytic coating -- tunable coercivity for magnetic media, MEMS, and advanced packaging. No rectifier required.

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
| 5. Electroless Co Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Anneal / Passivate | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Final Inspection | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

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
140--176 F (60--80 C)
NaOH 30--60 g/L
3--10 min soak
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, oxides -- catalytic surface required`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `DI counterflow (2-stage min)`
- Purpose: `Remove alkaline cleaner before acid activation`
- Check: `Conductivity <50 uS/cm in final stage`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `Substrate-dependent` / `Cu/Ni: catalytic (direct)` / `Non-conductive: Sn/Pd colloidal` / `Si wafers: HF + Pd seed`
- Purpose: `Create catalytically active surface for Co deposition`
- Check: `CAUTION: HF for silicon -- extreme hazard` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `DI preferred`
- Purpose: `Remove activation chemistry drag-in`
- Check: `Short transfer time -- prevent surface re-oxidation`

*Box 5 -- Electroless Co Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Electroless Co` / Subtitle: `Main Tank`
- Parameters: `Co2+: 15--30 g/L` / `NaH2PO2: 15--30 g/L` / `pH 8.0--10.0` / `158--194 F (70--90 C)`
- Purpose: `Autocatalytic Co-P or Co-W-P deposition`
- Check: `Bath life: 2--4 MTO -- monitor stabilizer`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `DI counterflow`
- Purpose: `Remove bath chemistry before post-treatment`
- Check: `CRITICAL: Co surfaces oxidize readily in air` (Coral `#E05C5C`)

*Box 7 -- Anneal / Passivate:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Anneal / Passivate`
- Parameters: `Anneal: 200--400 C in vacuum/inert` / `Passivate: Tri-Cr or BTA derivative`
- Purpose: `Optimize magnetic properties or protect surface`
- Check: `Application-specific -- magnetic vs. barrier`

*Box 8 -- Final Inspection:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Final Inspection`
- Parameters: `Thickness: XRF or gravimetric` / `Magnetic: VSM or coercimeter` / `Composition: XRF or ICP`
- Purpose: `Verify deposit meets application specification`
- Check: `No ASTM standard -- characterize per application`

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
- Stage (3.5") | Chemistry (5.0") | Temperature (3.0") | Time (2.5") | pH (2.5") | Key Control (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | pH | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30--60 g/L + surfactant | 140--176 F | 3--10 min | >12 | Water-break-free |
| 2. Rinse | DI counterflow | Ambient | 30--60 sec | -- | <50 uS/cm |
| 3. Activation | Substrate-dependent (see poster #266) | Ambient | 30--120 sec | -- | Coverage verification |
| 4. Rinse | DI counterflow | Ambient | 30--60 sec | -- | Minimize transfer time |
| 5. E-Co Plate | CoSO4 + NaH2PO2 + citrate | 158--194 F | Per spec | 8--10 | Stabilizer level |
| 6. Rinse | DI counterflow | Ambient | 30--60 sec | -- | Prevent oxidation |
| 7. Anneal/Passivate | Vacuum/inert or tri-Cr | 200--400 C (anneal) | Per spec | -- | Application-specific |
| 8. Inspection | XRF, VSM, ICP | -- | -- | -- | No ASTM standard |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Co-P vs. Co-W-P Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> ALLOY SELECTION -- CO-P VS. CO-W-P

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Co-P (Binary Alloy):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `CO-P ALLOY (BINARY)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Magnetic Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| P content | 2--12 wt% (tunable) |
| Reducing agent | Sodium hypophosphite |
| Temperature | 70--90 C (158--194 F) |
| pH | 8.0--10.0 |
| Deposition rate | 3--8 um/hr |
| Hardness (as-plated) | 400--700 HV |
| Coercivity (low P) | >500 Oe (hard magnetic) |
| Coercivity (high P) | <100 Oe (soft magnetic) |
| Bath life | 2--4 MTO |
| Primary use | Magnetic recording media |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Ferromagnetic with tunable coercivity -- P content controls magnetic behavior` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Co-W-P (Ternary Alloy):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CO-W-P ALLOY (TERNARY)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Thermal Barrier` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Composition | 2--8% P + 2--15% W |
| Reducing agent | Sodium hypophosphite |
| Temperature | 65--85 C (150--185 F) |
| pH | 8.5--10.5 |
| Deposition rate | 1--5 um/hr |
| Hardness (as-plated) | 500--800 HV |
| Thermal stability | Excellent (W inhibits crystallization) |
| Corrosion resistance | Very good |
| Bath life | 1--3 MTO |
| Primary use | Diffusion barrier, advanced packaging |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Tungsten co-deposition enhances thermal stability -- diffusion barrier to 500--600 C` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | SKIP PLATING | Insufficient activation or stabilizer poisoning | Verify activation coverage; check stabilizer level |
| 2 | 6.33" | BATH DECOMPOSITION | Under-loaded at temp; depleted stabilizer; Fe/Cu particles | Never idle at temp without load; filter continuously |
| 3 | 12.16" | PITTING | H2 bubble adhesion; poor agitation; organic contamination | Increase agitation; add wetting agent; carbon treat |
| 4 | 18.0" | POOR ADHESION | Inadequate cleaning/activation; excessive transfer time | Review activation; minimize transfer time to bath |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless cobalt plating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. No governing ASTM standard exists for electroless cobalt -- characterize deposits per application specification.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Cobalt -- Process Flow

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
| Zone 4 - Co-P vs Co-W-P | Section label, two comparison callouts |
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
| `Electroless Cobalt Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Cobalt Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Cobalt Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electroless Cobalt Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Cobalt Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Cobalt Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Electroless Cobalt cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#264--#270) zoom into each stage individually. The Co-P vs. Co-W-P comparison is unique to this process -- no other electroless cluster has a binary/ternary alloy decision this significant. The lack of a governing ASTM standard should be noted prominently; characterization is application-specific. Watson flagged this as a niche process with shorter bath life than EN -- that instability story is worth emphasizing.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #263 -- Construction Workup v1.0*
*2026-04-26*
