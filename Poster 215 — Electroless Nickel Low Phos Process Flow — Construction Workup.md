---
Project: Plating Posters Inc
Poster Number: 215
Title: "Electroless Nickel (Low Phos) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 1: EN Low-P)"
Technical Source: Industry-standard electroless nickel low phosphorus (2-4% P) plating process. Covers the complete 7-stage autocatalytic sequence from cleaning through post-treatment. Values are typical ranges for alkaline-pH EN Low-P baths per ASTM B733 Type II/III.
Process Scope: Electroless nickel low phosphorus (2-4% P) -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickel
  - LowPhosphorus
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEN-LP
---

# Poster #215 -- Construction Workup
## Electroless Nickel (Low Phos) -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EN Low-P: Electroless Nickel Low Phosphorus (2-4% P). It shows the complete 7-stage process sequence at a glance -- every stage visible in one U-flow diagram. Electroless nickel is fundamentally different from electroplating: no rectifier, no anodes, no external current. The deposit is autocatalytic -- the freshly deposited nickel itself catalyzes the next layer. This poster is the "map" for the other 7 posters (#216--#222) in this cluster.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (why Low-P vs. Mid-P vs. High-P?), and a troubleshooting quick-hit strip. Dense but scannable -- the engineer's wall reference for the entire EN Low-P line.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box color-coded by stage type. Arrows are simple connectors. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why Low-P?" comparison callout (Block E):** Three side-by-side callout boxes comparing Low-P vs. Mid-P vs. High-P -- the three EN-P classes. Established pattern.

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
| Amber | `#E8A020` | Activation stages, warning headers, key parameters |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Plating stage (main tank), optimal reference |
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
  Block B: Seven-stage U-flow diagram (top row 4, bottom row 3)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 7-row parameter table (one row per stage)

ZONE 4 -- WHY LOW-P? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Low-P vs. Mid-P vs. High-P side-by-side callout

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
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> ELECTROLESS NICKEL

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Low Phosphorus (2-4% P) -- Complete Process Flow -- 7 Stages

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> No rectifier. No anode. The deposit grows itself. Autocatalytic Ni-P at 650-750 HV as-plated -- the hardest EN class straight out of the bath.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row of four boxes, bottom row of three boxes, U-flow pattern.

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

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-7, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. EN Low-P Bath | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |

Note: Box 7 is at X: 6.0" (leaving the X: 0.5" position empty on the bottom row -- this creates visual asymmetry that reinforces the U-flow direction).

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
60-80 C (140-176 F)
NaOH 30-60 g/L
3-10 min soak
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, oxides, soils that inhibit catalytic activity`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Counterflow 2-stage min`
- Purpose: `Remove alkaline cleaner before acid activation`
- Check: `Target: < 50 uS/cm conductivity in final stage`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `HCl 10-20% v/v (steel)` / `or Zincate (aluminum)` / `Ambient, 30-120 sec`
- Purpose: `Remove oxides, create catalytic surface for EN initiation`
- Check: `Steel is self-catalytic -- no Pd needed` (`#27AE60`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `DI preferred` / `Ambient, 30-60 sec`
- Purpose: `Remove acid/zincate drag-in -- most critical rinse`
- Check: `CRITICAL: Chloride drag-in causes pitting in EN bath` (Coral `#E05C5C`)

*Box 5 -- EN Low-P Bath (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `EN Low-P Bath` / Subtitle: `Main Tank`
- Parameters: `Ni2+: 4.5-6.0 g/L` / `NaH2PO2: 20-35 g/L` / `pH 8.5-9.5 (alkaline)` / `65-80 C (150-176 F)`
- Purpose: `Autocatalytic Ni-P deposition (2-4% P)`
- Check: `Rate: 10-15 um/hr | Bath life: 6-8 MTO`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Cold water preferred` / `Double counterflow or spray`
- Purpose: `Stop EN reaction; remove drag-out`
- Check: `CRITICAL: Do not air-dry -- watermarks stain deposit` (Coral `#E05C5C`)

*Box 7 -- Post Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post Treatment`
- Parameters: `HE bake: 190-210 C, 2-23 hr` / `Hardness HT: 350-400 C, 1 hr` / `Within 4 hr of plating (HE)`
- Purpose: `Relieve hydrogen; develop max hardness (1000-1100 HV)`
- Check: `MANDATORY for high-strength steel (>1000 MPa)` (Coral `#E05C5C`)

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

**BLOCK D -- 7-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Key Control (8.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30-60 g/L + surfactant | 60-80 C | 3-10 min | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30-60 sec | < 50 uS/cm conductivity |
| 3. Activation | HCl 10-20% (steel) / Zincate (Al) | Ambient | 30-120 sec | Substrate-dependent |
| 4. Rinse | DI preferred | Ambient | 30-60 sec | No chloride drag-in |
| 5. EN Low-P Bath | Ni2+ 4.5-6.0 g/L, pH 8.5-9.5 | 65-80 C | Per spec | 10-15 um/hr, 6-8 MTO |
| 6. Rinse | DI or city water | Ambient (cold) | 30-60 sec | No air-dry |
| 7. Post Treatment | Oven / furnace | 190-400 C | 1-23 hr | HE bake within 4 hr |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Low-P? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE THREE EN-P CLASSES -- LOW VS. MID VS. HIGH

---

**BLOCK E -- Three-Column Comparison**

Y: 22.9" to 28.3". Three side-by-side callout boxes.

**Left -- Low-P (2-4% P) -- THIS POSTER:**
- Rounded rect, X: 0.5", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Full border: 2 pt `#27AE60` (highlighted -- this is the current poster's class)
- Title: `LOW-P (2-4% P)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `This Poster` -- Barlow Condensed ExtraBold, 12 pt, `#27AE60`

Properties (Inter Regular 13 pt `#F0EDE8`, line height 150%):

| Property | Value |
|---|---|
| pH | Alkaline (8.5-9.5) |
| Structure | Microcrystalline |
| Magnetic | Yes (ferromagnetic) |
| Hardness (as-plated) | 650-750 HV |
| Hardness (HT) | 1000-1100 HV |
| Corrosion (SST 25 um) | 96-240 hr |
| Solderability | Excellent |
| Deposition rate | 10-15 um/hr |

Bottom highlight:
- Text: `Highest as-plated hardness. Ferromagnetic. Excellent solderability.` -- Inter Medium, 12 pt, `#27AE60`

**Center -- Mid-P (5-9% P):**
- Rounded rect, X: 8.17", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `MID-P (5-9% P)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Industry Workhorse` -- Barlow Condensed ExtraBold, 12 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| pH | Acid (4.6-5.2) |
| Structure | Mixed cryst/amorphous |
| Magnetic | Weakly to non-magnetic |
| Hardness (as-plated) | 500-600 HV |
| Hardness (HT) | 850-1000 HV |
| Corrosion (SST 25 um) | 240-500 hr |
| Solderability | Moderate |
| Deposition rate | 18-25 um/hr |

Bottom: `Fastest deposition. ENIG standard (IPC-4552B). Most widely used.` -- Inter Medium, 12 pt, `#E8A020`

**Right -- High-P (10-13% P):**
- Rounded rect, X: 15.84", Y: 22.9", W: 7.66", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `HIGH-P (10-13% P)` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Maximum Corrosion Resistance` -- Barlow Condensed ExtraBold, 12 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| pH | Acid (4.2-4.8) |
| Structure | Fully amorphous |
| Magnetic | Non-magnetic |
| Hardness (as-plated) | 450-550 HV |
| Hardness (HT) | 800-950 HV |
| Corrosion (SST 25 um) | 1000+ hr |
| Solderability | Poor |
| Deposition rate | 10-13 um/hr |

Bottom: `Amorphous -- no grain boundaries. Oil/gas, chemical processing, MRI-compatible.` -- Inter Medium, 12 pt, `#2EC4B6`

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
| 1 | 0.5" | SKIP PLATING | Contamination or poor activation -- no catalytic initiation | Improve cleaning; check activation time |
| 2 | 6.33" | PITTING | Chloride drag-in from HCl activation or particulate | DI rinse; filter bath (5-10 um) |
| 3 | 12.16" | BATH DECOMPOSITION | Low stabilizer or bath left hot without load | Check stabilizer ppm; never idle at temp |
| 4 | 18.0" | LOW DEPOSITION RATE | pH drift low, low temperature, or reducer depletion | Check pH, temp, hypophosphite level |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless nickel low phosphorus (2-4% P) plating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B733; AMS 2404/2405.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Nickel (Low Phos) -- Process Flow

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
| Zone 4 - EN-P Comparison | Section label, three comparison callouts |
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
| `EN Low-P Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN Low-P Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN Low-P Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `EN Low-P Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN Low-P Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN Low-P Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire EN Low-P cluster. The key differentiator from electroplating process flows: NO rectifier, NO anode boxes in the diagram. The flow diagram must emphasize the autocatalytic nature -- call it out visually. The three-class comparison (Low/Mid/High P) is the most-asked question in EN shops: "what's the difference?" The answer is pH controls phosphorus, and phosphorus controls everything else.

EN Low-P is the niche specialist: ferromagnetic (used in shielding), highest hardness as-plated, excellent solderability (electronics), but lowest corrosion resistance of the three classes. The poster should convey "precision specialty" not "general workhorse."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #215 -- Construction Workup v1.0*
*2026-04-26*
