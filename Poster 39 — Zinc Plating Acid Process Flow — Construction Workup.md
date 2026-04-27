---
Project: Plating Posters Inc
Poster Number: 39
Title: "Zinc Plating (Acid) -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-02 technical reference (acid chloride zinc)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Industry-standard acid chloride zinc plating process (potassium chloride type). Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for KCl-type acid zinc -- the dominant acid zinc system in modern shops.
Process Scope: Acid chloride zinc plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincPlating
  - AcidChloride
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEP02
---

# Poster #39 -- Construction Workup
## Zinc Plating (Acid) -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-02: Zinc Plating (Acid / Chloride). It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Acid chloride zinc is the most widely used zinc process in job shops and captive lines. Higher deposition rate and brighter deposits than alkaline, but lower throwing power and more sensitive to metallic contamination. This poster is the "map" for the cluster; Posters #40--#46 zoom into each stage.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (why acid vs. alkaline?), and a troubleshooting quick-hit strip. Dense but scannable -- the foreman's wall reference for the entire acid zinc line.

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

3. **"Why Acid?" comparison callout (Block E):** Two side-by-side callout boxes comparing acid vs. alkaline zinc. Mirror image of Poster #31's "Why Alkaline?" block -- acid gets the left (featured) position here.

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

ZONE 4 -- WHY ACID? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Acid vs. Alkaline side-by-side callout

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

> ZINC PLATING (ACID)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Cure

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Acid chloride zinc -- the job shop workhorse. High efficiency, bright deposits, and the most common zinc bath in the industry.

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
| 1. Soak Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
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
| 5. Zinc Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Passivate/Chromate | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry/Cure | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Soak Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Soak Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
140--180 F (60--82 C)
4--8 oz/gal
3--10 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, drawing compounds`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Non-silicated cleaner -- silicate = skip plating`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Overflow or cascade`
- Purpose: `Remove alkaline cleaner residues`
- Check: `< 500 uS/cm conductivity target`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `HCl 10--50% v/v` / `Ambient, 15--60 sec` / `HCl preferred for steel`
- Purpose: `Remove surface oxides, expose clean metal`
- Check: `CAUTION: H-embrittlement risk >= 31 HRC` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `Single overflow`
- Purpose: `Remove activation acid`
- Check: `Acid drag-in drops pH and wrecks brightener`

*Box 5 -- Zinc Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Zinc Plate` / Subtitle: `Acid Chloride`
- Parameters: `Zn: 25--35 g/L` / `KCl: 180--200 g/L` / `pH 5.0--5.4` / `20--40 ASF (rack)`
- Purpose: `Electrodeposit zinc onto substrate`
- Check: `pH is the #1 control parameter`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `Double counterflow`
- Purpose: `Remove chloride drag-out before passivate`
- Check: `CRITICAL: Chloride in passivate = short bath life` (Coral `#E05C5C`)

*Box 7 -- Passivate/Chromate:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Passivate` / Subtitle: `Chromate Conversion`
- Parameters: `Tri: pH 1.5--2.5, 30--90 sec` / `Hex: pH 1.0--2.5, 15--30 sec` / `70--90 F`
- Purpose: `Corrosion-resistant conversion coating`
- Check: `Trivalent (RoHS) vs. Hex -- know your spec`

*Box 8 -- Dry/Cure:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Cure`
- Parameters: `Forced air or oven` / `150--170 F` / `15--20 min minimum`
- Purpose: `Cure passivate film, remove moisture`
- Check: `Sealer optional: 150--180 F, 30--60 sec`

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
- Stage (3.5") | Chemistry (5.0") | Temperature (3.0") | Time (2.5") | Current Density (3.5") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Soak Clean | Alk cleaner 4--8 oz/gal | 140--180 F | 3--10 min | -- | Non-silicated only |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | < 500 uS/cm |
| 3. Activation | HCl 10--50% v/v | Ambient | 15--60 sec | -- | HCl preferred for steel |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | < 200 uS/cm |
| 5. Zinc Plate | Zn 25--35 g/L, KCl 180--200, H3BO3 25--30 | 70--85 F | Per spec | 20--40 ASF (rack) | pH 5.0--5.4 |
| 6. Rinse | DI or city water | Ambient | 30--60 sec | -- | < 100 uS/cm before passivate |
| 7. Passivate | Tri pH 1.5--2.5 / Hex pH 1.0--2.5 | 70--90 F | Tri 30--90 sec / Hex 15--30 sec | -- | pH + immersion time |
| 8. Dry/Cure | -- | 150--170 F | 15--20 min | -- | Sealer optional |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Acid? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY ACID? -- ACID VS. ALKALINE ZINC

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Acid Chloride Zinc (featured):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `ACID CHLORIDE ZINC` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Job Shop Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Bath pH | 4.8--5.8 (mildly acidic) |
| Zinc source | ZnCl2 dissolved in chloride bath |
| Temperature | 70--85 F (ambient to mild heat) |
| Throwing power | Moderate -- less uniform in recesses |
| Cathode efficiency | 95--98% -- highest of any zinc bath |
| HCD tolerance | Excellent -- handles high CD well |
| Brightness | Bright as-plated -- best in class |
| Waste treatment | Standard acid neutralization |
| Key weakness | Sensitive to Fe, Cu, Pb contamination |
| Bath types | KCl (modern) or NH4Cl (legacy) |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Highest efficiency and brightness -- the default choice when throwing power isn't the limiting factor` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Alkaline Non-Cyanide Zinc:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `ALKALINE NON-CYANIDE ZINC` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Throwing Power Champion` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Bath pH | > 12.5 (highly alkaline) |
| Zinc source | ZnO dissolved in NaOH |
| Temperature | Ambient (65--85 F) -- no heating |
| Throwing power | EXCELLENT -- best in class |
| Cathode efficiency | 70--85% -- significantly lower |
| HCD tolerance | Lower -- burns easier at high CD |
| Brightness | Semi-bright -- not as shiny |
| Waste treatment | Simpler -- no chelated complexes |
| Key weakness | Lower efficiency, narrower CD range |
| Bath types | Non-cyanide (dominant) or cyanide (legacy) |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Unmatched throwing power -- the choice for complex geometries, barrels, and blind recesses` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | DULL/HAZY DEPOSIT | Low brightener, high iron (> 50 ppm), or organic contamination | Hull cell check; H2O2 treat for iron; carbon treat |
| 2 | 6.33" | BURNING AT HCD | CD too high, low zinc metal, or high temperature | Reduce CD; add ZnCl2; check temp < 85 F |
| 3 | 12.16" | PITTING | Low wetting agent, oil drag-in, or poor agitation | Add wetter; carbon treat; improve air agitation |
| 4 | 18.0" | DARK LCD AREAS | Iron contamination, high pH, or low primary brightener | H2O2 + filter; adjust pH; Hull cell |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for acid chloride zinc plating (potassium chloride type). Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; Metal Finishing Guidebook.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Zinc Plating (Acid) -- Process Flow

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
| Zone 4 - Why Acid | Section label, two comparison callouts |
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
| `Zinc Acid Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Acid Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Acid Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Zinc Acid Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Acid Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Acid Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Acid Zinc cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#40--#46) zoom into each stage individually. The acid vs. alkaline comparison answers the most common question from the opposite perspective of Poster #31: "why acid instead of alkaline?" The answer is efficiency and brightness -- acid wins for simple geometries and fastener work where throwing power isn't the limiting factor.

Key technical differentiator from Poster #31: pH is now a measured parameter (4.8--5.8 range), cathode efficiency is dramatically higher (95--98% vs. 70--85%), and the bath contains boric acid as a buffer -- a component absent from alkaline zinc.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #39 -- Construction Workup v1.0*
*2026-04-26*
