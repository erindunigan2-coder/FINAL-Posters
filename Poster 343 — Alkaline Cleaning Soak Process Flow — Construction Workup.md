---
Project: Plating Posters Inc
Poster Number: 343
Title: "Alkaline Cleaning (Soak) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-1)"
Technical Source: Industry-standard alkaline soak cleaning process. Covers the complete 7-stage poster sequence for the CT-01 cluster. Values are typical ranges for NaOH-based soak cleaning of steel, aluminum, and zinc die cast substrates.
Process Scope: Alkaline soak cleaning -- complete process flow (cluster overview)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AlkalineCleaning
  - SoakClean
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT01
---

# Poster #343 -- Construction Workup
## Alkaline Cleaning (Soak) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-01: Alkaline Cleaning (Soak). It shows the complete cleaning sequence at a glance -- from incoming dirty parts through final inspection. A shop operator sees the full flow, a supervisor checks parameters, a quality engineer understands the soil removal mechanism. This poster is the "map" that the remaining 6 posters (#344--#349) zoom into.

Design philosophy: clean linear flow diagram as the hero, a substrate routing table (steel vs. aluminum vs. zinc die cast), a soil classification callout (ASTM B322), and a troubleshooting quick-hit strip. Dense but scannable -- the foreman's wall reference for the entire cleaning line.

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

1. **Process flow diagram (Block B -- HERO):** Five rounded rectangles in a linear left-to-right top row plus a decision diamond for "secondary clean required?" routing to a second row. Each box is color-coded by stage type. Arrows are simple right-pointing connectors with a vertical decision link.

2. **Soil classification table (Block D):** Three-row table based on ASTM B322 classification -- saponifiable, non-saponifiable, and semi-solid/particulate. Standard table construction.

3. **Substrate routing callout (Block E):** Four-column comparison showing steel, aluminum, zinc die cast, and copper/brass with key cautions per substrate. Established pattern.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common cleaning failures with one-line fixes.

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
| Amber | `#E8A020` | Decision points, warning headers, temperature data |
| Teal | `#2EC4B6` | Cleaning and rinse stages, structural positives |
| Emerald | `#27AE60` | Pass/success states, optimal indicators |
| Coral | `#E05C5C` | Problems, failures, contamination callouts |
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
- 15.0" -- Zone 2/Zone 3 boundary
- 21.5" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.0" / ~12.1" tall)
  Block B: Five-stage flow diagram with decision branch
  Block C: Stage legend strip (color key)

ZONE 3 -- SOIL CLASSIFICATION TABLE (15.0"--21.5" / ~6.5" tall)
  Block D: ASTM B322 soil classification (3 types)

ZONE 4 -- SUBSTRATE ROUTING (21.5"--28.5" / ~7.0" tall)
  Block E: Four-substrate comparison (steel / aluminum / zinc die cast / copper-brass)

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

> ALKALINE CLEANING (SOAK)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- From Dirty Parts to Clean Surface

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The first step in every plating line. Good cleaning is to plating what a solid foundation is to a building -- skip it and everything above fails.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.0" (~12.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE ALKALINE SOAK CLEAN -- STAGE BY STAGE

---

**BLOCK B -- Five-Stage Flow Diagram with Decision Branch**

Y: 3.8" to 13.5" (~9.7" tall). Top row of 5 boxes left-to-right, with a decision branch below for secondary cleaning.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.0"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 7.8") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Incoming Parts | Box 1 | 0.5" | `#3A4055` (Slate) | Entry |
| 2. Alkaline Soak Clean | Box 2 | 5.2" | `#2EC4B6` (Teal) | Cleaning |
| 3. Drag-Out Rinse | Box 3 | 9.9" | `#2EC4B6` (Teal) | Rinse |
| 4. Running Water Rinse | Box 4 | 14.6" | `#2EC4B6` (Teal) | Rinse |
| 5. Water Break Test | Box 5 | 19.3" | `#27AE60` (Emerald) | Inspection |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~5.8")

**Decision diamond below Box 5 (Y: 8.5"):**
- Diamond shape, W: 2.0", H: 1.5", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Center X: 20.4"
- Text: `PASS?` Barlow SemiBold 16 pt `#E8A020`
- Arrow down-right labeled `YES` -> `To Electroclean or Acid Activate` (text box, Inter Medium 14 pt `#27AE60`)
- Arrow down-left labeled `NO` -> loops back to Box 2 (line with arrowhead, `#E05C5C`)

**Bottom Row (Y: 10.5" to 13.5") -- Secondary/Heavy-Duty Path:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| Alt. Heavy-Duty Soak | Box 6 | 2.0" | `#E8A020` (Amber) | Heavy Clean |
| Alt. Maintenance Soak | Box 7 | 9.0" | `#2EC4B6` (Teal) | Maintenance |

Box 6:
- Badge: `HEAVY SOIL`, fill `#E8A020`
- Name: `Heavy-Duty Soak`
- Parameters: `Higher concentration` / `Higher temp: 80-90 C` / `5-10 min`
- Purpose: `Strip gross soil: heavy buffing compound, drawing compound, carbonized oils`

Box 7:
- Badge: `MAINTENANCE`, fill `#2EC4B6`
- Name: `Maintenance Soak`
- Parameters: `Lower concentration` / `Cleaner bath` / `3-5 min`
- Purpose: `Final cleaning pass -- remove residual soil missed by heavy-duty stage`

Arrow from Box 7 right back to Box 4 (Running Water Rinse): `Return to main flow` Inter Regular 12 pt `#F0EDE8` at 60%.

**Inside each main flow box (top to bottom):**

*Box 1 -- Incoming Parts:*

Stage badge:
- Rounded rect, 1.2" x 0.4", fill `#3A4055`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8`

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Incoming Parts`

Key info:
- Inter Regular, 13 pt, `#F0EDE8` at 70%, line height 155%
```
Identify soil type
Classify per ASTM B322
Route to correct cleaner
```

*Box 2 -- Alkaline Soak Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Alkaline Soak Clean`
- Parameters: JetBrains Mono 13 pt `#F0EDE8`:
```
Steel: 45-90 g/L NaOH
Aluminum: 10-30 g/L NaOH
140-195 F (60-90 C)
3-10 min (substrate dependent)
```
- Purpose: `Saponification + emulsification of oils and soils`
- Check: `CAUTION: Aluminum etches above 30 g/L NaOH` (Coral `#E05C5C`)

*Box 3 -- Drag-Out Rinse:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Drag-Out Rinse` / Subtitle: `Optional -- Recovery` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Still rinse (no overflow)` / `Recovers 50-70% of cleaner`
- Purpose: `Capture cleaner drag-out for return to tank`
- Check: `Extends bath life and reduces chemical cost`

*Box 4 -- Running Water Rinse:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Running Water Rinse`
- Parameters: `Ambient temp` / `Flowing or counterflow cascade` / `30-60 sec`
- Purpose: `Remove all remaining alkaline residue`
- Check: `Rinse pH < 9.0 -- closer to neutral = better` Inter Medium 12 pt `#2EC4B6`

*Box 5 -- Water Break Test:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Water Break Test`
- Parameters: `Per ASTM F22` / `Perform within 30 sec of rinse`
- Purpose: `Confirm surface is free of organic contamination`
- Check: `Water must sheet uniformly -- any break = contamination` Inter Medium 12 pt `#27AE60`

---

**BLOCK C -- Stage Legend Strip**

Y: 13.8" to 14.8"

- Rounded rectangle, X: 0.5", Y: 13.8", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#3A4055` (Slate) | `Entry / Identification` |
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Heavy-Duty / Decision` |
| `#27AE60` (Emerald) | `Inspection / Pass` |
| `#E05C5C` (Coral) | `Caution / Fail` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Soil Classification Table

**Dimensions:** Y: 15.0" to 21.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> KNOW YOUR ENEMY -- SOIL CLASSIFICATION (ASTM B322)

---

**BLOCK D -- Soil Classification Table**

Y: 15.9" to 21.3". Column widths (23.0" total):
- Soil Type (4.5") | Examples (6.5") | Removal Mechanism (6.5") | Cleaner Requirement (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.4".

| Soil Type | Examples | Mechanism | Requirement |
|---|---|---|---|
| Saponifiable (Polar) | Lard oil, tallow, palm oil, stearic acid | Saponification -- alkali reacts with fatty acid to form water-soluble soap + glycerol | Elevated temperature (>60 C); sufficient NaOH concentration |
| Non-Saponifiable (Non-Polar) | Mineral oil, petroleum grease, silicone oil, synthetic coolants | Emulsification -- surfactants encapsulate oil droplets in micelles | Surfactant above CMC (typically 0.1-1 g/L nonionic); temp below cloud point |
| Semi-Solid / Particulate | Buffing compound (grease + abrasive), metal fines, carbon | Combination of emulsification + mechanical displacement | May require pre-soak, spray, or two-stage clean; most stubborn soil type |

Data: Inter Regular, 13 pt, `#F0EDE8`. Soil Type names: Barlow SemiBold, 15 pt, accent-colored per type.
- Saponifiable: `#27AE60`
- Non-Saponifiable: `#2EC4B6`
- Semi-Solid: `#E8A020`

**Callout below table (Y: 20.6"):**
- Rounded rect, W: 23.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Rule of thumb: if you can identify the soil, you can select the cleaner. Saponifiable soils are easy. Non-saponifiable need surfactant. Buffing compound needs everything.` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 4 -- Substrate Routing

**Dimensions:** Y: 21.5" to 28.5" (~7.0" tall).

---

**Section label:**
- Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> SUBSTRATE ROUTING -- ONE CLEANER DOES NOT FIT ALL

---

**BLOCK E -- Four-Substrate Comparison**

Y: 22.4" to 28.3". Four side-by-side callout boxes.

| Substrate | X | W | Accent |
|---|---|---|---|
| Steel / Iron | 0.5" | 5.5" | `#2EC4B6` (Teal) |
| Aluminum | 6.25" | 5.5" | `#E8A020` (Amber) |
| Zinc Die Cast | 12.0" | 5.5" | `#E05C5C` (Coral) |
| Copper / Brass | 17.75" | 5.75" | `#27AE60` (Emerald) |

Each box: Rounded rect H: 5.5", fill `#1E2435`, left accent 0.06".

*Steel / Iron box:*
- Title: `STEEL / IRON` Barlow SemiBold 18 pt `#2EC4B6`
- JetBrains Mono 14 pt for parameters:
```
NaOH: 45-90 g/L (6-12 oz/gal)
Temp: 150-195 F (65-90 C)
Time: 3-10 min
```
- Inter Regular 13 pt: `Standard high-caustic cleaner. No special restrictions. Most forgiving substrate.`
- Check: `Water-break-free after rinse` Inter Medium 12 pt `#2EC4B6`

*Aluminum box:*
- Title: `ALUMINUM` Barlow SemiBold 18 pt `#E8A020`
- Parameters:
```
NaOH: 10-30 g/L (1.3-4 oz/gal)
Silicate: 30-60 g/L inhibitor
Temp: 120-150 F (50-65 C)
Time: 1-3 min
```
- `Low caustic + silicate inhibitor required. NaOH etches aluminum above ~30 g/L and ~60 C.`
- Check: `CAUTION: Silicate residue may require desmut step` `#E05C5C`

*Zinc Die Cast box:*
- Title: `ZINC DIE CAST` Barlow SemiBold 18 pt `#E05C5C`
- Parameters:
```
NaOH: 30-60 g/L (4-8 oz/gal)
Temp: 130-160 F (55-70 C)
Time: 2-5 min MAX
```
- `Moderate caustic, shorter immersion. Zinc dissolves in strong caustic -- limit exposure.`
- Check: `CAUTION: Exceeding 5 min causes substrate attack` `#E05C5C`

*Copper / Brass box:*
- Title: `COPPER / BRASS` Barlow SemiBold 18 pt `#27AE60`
- Parameters:
```
NaOH: Low-caustic formula
Non-silicated preferred
Temp: 130-160 F (55-70 C)
Time: 2-5 min
```
- `Low-caustic, non-silicated preferred. High silicate can leave residual film on copper alloys.`
- Check: `Non-etch formulations preferred` Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON CLEANING FAILURES

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WATER BREAK | Insufficient time/temp; bath exhausted; surfactant depleted | Increase time/temp; rebuild bath; add surfactant |
| 2 | 6.33" | SILICATE RESIDUE | Silicate too high on aluminum; rinse inadequate | Reduce silicate; improve rinse; add acid desmut |
| 3 | 12.16" | SUBSTRATE ETCH | NaOH too high for substrate; temp too high | Reduce caustic; add silicate inhibitor; lower temp |
| 4 | 18.0" | FOAM OVERFLOW | Surfactant overdose; incompatible drag-in chemistry | Check surfactant level; use low-foam grade for spray |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for alkaline soak cleaning. Specific formulations, concentrations, and process limits vary by proprietary product and substrate. Consult your process supplier for application-specific guidance. Reference: ASTM B322, ASTM F22; general industry knowledge.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Alkaline Cleaning (Soak) -- Process Flow

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
| Zone 2 - Process Flow | Section label, five flow boxes + decision diamond + two alternate boxes, arrows, legend strip |
| Zone 3 - Soil Classification | Section label, 3-row classification table, callout |
| Zone 4 - Substrate Routing | Section label, four substrate comparison callouts |
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
| `Alkaline Cleaning Soak Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Alkaline Cleaning Soak Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Alkaline Cleaning Soak Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Alkaline Cleaning Soak Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Alkaline Cleaning Soak Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Alkaline Cleaning Soak Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Alkaline Cleaning cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The substrate routing section is the most unique feature of this cluster overview -- it answers the question every new operator asks: "Can I use the same cleaner for aluminum that I use for steel?" (No. Emphatically no.) The ASTM B322 soil classification gives the poster lasting reference value beyond a simple process chart.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #343 -- Construction Workup v1.0*
*2026-04-26*
