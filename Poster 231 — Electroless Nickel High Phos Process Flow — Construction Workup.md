---
Project: Plating Posters Inc
Poster Number: 231
Title: "Electroless Nickel (High Phos) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 3: EN High-P)"
Technical Source: Industry-standard electroless nickel high-phosphorus (10-13% P) process. Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for acid-pH autocatalytic Ni-P deposition. ASTM B733 Type V. No brand names.
Process Scope: Electroless nickel high-phosphorus -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickel
  - HighPhosphorus
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEN03
---

# Poster #231 -- Construction Workup
## Electroless Nickel (High Phos) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EN-03: Electroless Nickel High Phosphorus. It shows the complete 8-stage process at a glance -- every stage visible in one U-flow diagram. The hero property of High-P EN is corrosion resistance: 1,000+ hours salt spray from a fully amorphous, non-magnetic deposit. Oil/gas downhole tools, chemical processing, and offshore equipment live and die by this coating.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (High-P vs. Mid-P vs. Low-P), and a troubleshooting quick-hit strip. Dense but scannable -- the operator's wall reference for the entire electroless nickel high-phos line.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1-4), vertical connector, bottom row R-to-L (stages 5-8). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why High-P?" comparison callout (Block E):** Three side-by-side callout boxes comparing Low-P vs. Mid-P vs. High-P EN. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

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

ZONE 4 -- WHY HIGH-P? COMPARISON (22.0"--28.5" / ~6.5" tall)
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

> ELECTROLESS NICKEL (HIGH PHOS)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Post-Treatment

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> 10-13% phosphorus. Fully amorphous. Non-magnetic. 1,000+ hours salt spray. The corrosion king of electroless nickel.

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
| 5. EN High-P Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post-Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Final Inspect | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

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
3--10 min (soak)
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, greases, oxides, shop soils`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Counterflow (2-stage min)` / `<50 uS/cm target`
- Purpose: `Remove alkaline cleaner before acid activation`
- Check: `Alkaline drag-in = pH spike in activation = poor results`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `HCl 10--20% v/v or H2SO4 10--30%` / `Ambient, 30--120 sec` / `Zincate for aluminum substrates`
- Purpose: `Remove oxide layer; expose catalytic surface`
- Check: `CAUTION: H-embrittlement risk on high-strength steel (>40 HRC)` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `DI preferred` / `<20 uS/cm for critical work` / `30--60 sec`
- Purpose: `Remove acid/activation chemistry drag-in`
- Check: `CRITICAL: Chloride drag-in causes pitting in EN bath` (Coral `#E05C5C`)

*Box 5 -- EN High-P Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `EN High-P Plate` / Subtitle: `Main Tank`
- Parameters: `pH: 4.2--4.8` / `82--90 C (180--194 F)` / `Ni: 4.5--6.5 g/L` / `Rate: 10--13 um/hr`
- Purpose: `Autocatalytic Ni-P deposition (10-13% P)`
- Check: `No rectifier. No anode. Uniform thickness +/-2 um.`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient (cold preferred)` / `Double counterflow` / `30--60 sec`
- Purpose: `Stop EN reaction; remove drag-out`
- Check: `Do not let parts air-dry before rinsing -- causes staining` (Coral `#E05C5C`)

*Box 7 -- Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post-Treatment` / Subtitle: `Heat Treatment / Passivation`
- Parameters: `HE relief: 190--210 C, 2--23 hr` / `Max hardness: 350--400 C, 1 hr` / `Passivation: optional trivalent chromate`
- Purpose: `Relieve hydrogen; harden; enhance corrosion`
- Check: `HE relief within 4 hours of plating on high-strength steel` (Coral `#E05C5C`)

*Box 8 -- Final Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Final Inspection`
- Parameters: `Thickness: XRF or micrometer` / `P%: XRF or ICP or wet chem` / `Non-magnetic: ASTM F2088`
- Purpose: `Verify deposit meets specification`
- Check: `ASTM B733 Type V: 10-13% P required`

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

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Rate/Loading (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Rate/Loading | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30-60 g/L + surfactant | 60-80 C | 3-10 min | -- | Water-break-free |
| 2. Rinse | DI or RO water | Ambient | 30-60 sec | -- | <50 uS/cm |
| 3. Activation | HCl 10-20% or H2SO4 10-30% | Ambient | 30-120 sec | -- | Substrate-dependent |
| 4. Rinse | DI water | Ambient | 30-60 sec | -- | <20 uS/cm (critical) |
| 5. EN High-P | Ni 4.5-6.5 g/L, hypo 20-30 g/L | 82-90 C | Per spec | 10-13 um/hr | pH 4.2-4.8 |
| 6. Rinse | DI or city water | Ambient | 30-60 sec | -- | Cold rinse preferred |
| 7. Post-Treat | HE bake or hardness HT | 190-400 C | 1-23 hr | -- | Within 4 hr (HE) |
| 8. Inspect | XRF / ICP / ASTM F2088 | -- | -- | -- | 10-13% P verified |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why High-P? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE THREE EN-P CLASSES -- KNOW YOUR PHOSPHORUS

---

**BLOCK E -- Three-Column Comparison**

Y: 22.9" to 28.3". Three equal-width callout boxes.

**Left -- Low-P (2-4% P):**
- Rounded rect, X: 0.5", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `LOW PHOSPHORUS` -- Barlow SemiBold, 18 pt, `#E8A020`
- Subtitle: `2-4% P` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 13 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Structure | Microcrystalline |
| Magnetic | Yes (ferromagnetic) |
| Hardness (as-plated) | 650-750 HV |
| Salt spray (25 um) | 96-240 hours |
| Solderability | Excellent |
| Bath pH | 6.0-9.0 (alkaline) |
| Best for | Electronics, wear, hardness |

Bottom highlight:
- Rounded rect, W: 6.5", H: 0.5", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Highest hardness. Ferromagnetic. Best solderability.` -- Inter Medium, 12 pt, `#E8A020`

**Center -- Mid-P (5-9% P):**
- Rounded rect, X: 8.17", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `MID PHOSPHORUS` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Subtitle: `5-9% P` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Structure | Mixed crystalline/amorphous |
| Magnetic | Weakly to non-magnetic |
| Hardness (as-plated) | 500-600 HV |
| Salt spray (25 um) | 240-500 hours |
| Solderability | Moderate |
| Bath pH | 4.6-5.2 (acid) |
| Best for | General engineering, ENIG |

Bottom highlight:
- Fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Industry workhorse. Fastest rate. Balanced properties.` -- Inter Medium, 12 pt, `#2EC4B6`

**Right -- High-P (10-13% P):**
- Rounded rect, X: 15.83", Y: 22.9", W: 7.67", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `HIGH PHOSPHORUS` -- Barlow SemiBold, 18 pt, `#27AE60`
- Subtitle: `10-13% P -- THIS POSTER` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Structure | Fully amorphous (metallic glass) |
| Magnetic | Non-magnetic (paramagnetic) |
| Hardness (as-plated) | 450-550 HV |
| Salt spray (25 um) | 1,000+ hours |
| Chemical resistance | Excellent |
| Bath pH | 4.2-4.8 (low acid) |
| Best for | Oil/gas, chemical, corrosion |

Bottom highlight:
- Fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Maximum corrosion resistance. No grain boundaries. The amorphous advantage.` -- Inter Medium, 12 pt, `#27AE60`

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
| 1 | 0.5" | SKIP PLATING | Poor cleaning or surface contamination | Improve clean; verify water-break-free |
| 2 | 6.33" | PITTING | Chloride drag-in or particulate | Improve pre-plate rinse; filter bath (5 um) |
| 3 | 12.16" | ROUGH DEPOSIT | Bath aging (high MTO) or particulate | Check orthophosphite; carbon treat; filter |
| 4 | 18.0" | SPONTANEOUS DECOMP | Low stabilizer, under-loaded, hot spots | Add stabilizer; maintain load; check heaters |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless nickel high-phosphorus (10-13% P) plating per ASTM B733 Type V. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B733; Nickel Plating Handbook.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Nickel (High Phos) -- Process Flow

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
| Zone 4 - Why High-P | Section label, three comparison callouts |
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
| `EN High-P Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN High-P Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN High-P Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `EN High-P Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN High-P Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `EN High-P Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire EN High-P cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#232-#238) zoom into each stage individually. The three-column EN class comparison is the key educational element -- operators need to understand that phosphorus percentage is controlled by pH, and that High-P's corrosion advantage comes from its amorphous (grain-boundary-free) structure. The autocatalytic nature of EN (no rectifier, no anode) should be prominently called out -- this is the fundamental difference from electrolytic plating.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #231 -- Construction Workup v1.0*
*2026-04-26*
