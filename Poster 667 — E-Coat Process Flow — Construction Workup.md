---
Project: Plating Posters Inc
Poster Number: 667
Title: "E-Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 3)"
Technical Source: Industry-standard cathodic electrodeposition (CED) e-coat process. Covers the complete sequence from cleaning through inspection. Values are typical ranges for cathodic epoxy e-coat -- the dominant automotive primer system worldwide.
Process Scope: Cathodic electrodeposition e-coat -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoating
  - Electrodeposition
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC03
---

# Poster #667 -- Construction Workup
## E-Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for E-Coating (Electrophoretic Deposition). It shows the complete process sequence at a glance -- every stage visible in one U-flow diagram. E-coat is the automotive body-in-white standard: cathodic electrodeposition drives coating into every recess, box section, and weld seam that spray painting cannot reach. This poster is the "map" that the other 8 posters (#669--#676) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (cathodic vs. anodic), and a troubleshooting quick-hit strip. Dense but scannable -- the line supervisor's wall reference for the entire e-coat system.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows.

2. **Parameter summary table (Block D):** A compact 9-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Cathodic vs. Anodic" comparison callout (Block E):** Two side-by-side callout boxes. Established pattern from Poster #31.

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
| Amber | `#E8A020` | E-coat bath stage, voltage highlights, warning headers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Pretreatment stage, optimal reference |
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
- 16.0" -- Zone 2/Zone 3 boundary
- 22.5" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Nine-stage U-flow diagram (top row 5, bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (16.0"--22.5" / ~6.5" tall)
  Block D: 9-row parameter table (one row per stage)

ZONE 4 -- CATHODIC VS. ANODIC COMPARISON (22.5"--28.5" / ~6.0" tall)
  Block E: Cathodic vs. Anodic side-by-side callout

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

> E-COATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Electrophoretic Deposition -- Complete Process Flow

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Cathodic electrodeposition -- the automotive body-in-white standard. >99% paint utilization. Unmatched throwing power into every cavity.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 16.0" (~13.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE E-COAT PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.8" (~11.0" tall). Top row of five boxes, bottom row of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse | Box 2 | 5.1" | `#2EC4B6` (Teal) | Rinse |
| 3. Zinc Phosphate | Box 3 | 9.7" | `#27AE60` (Emerald) | Pretreatment |
| 4. Rinse / Seal / DI | Box 4 | 14.3" | `#2EC4B6` (Teal) | Rinse |
| 5. E-Coat Tank | Box 5 | 18.9" | `#E8A020` (Amber) | Coating |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.1", Y: 8.3" (bottom center Box 5)
- To: X: 21.1", Y: 10.0" (top center Box 6)

**Bottom Row (Y: 10.0" to 14.5") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. UF Permeate Rinse | Box 6 | 18.0" | `#2EC4B6` (Teal) | Recovery/Rinse |
| 7. DI Rinse | Box 7 | 12.5" | `#2EC4B6` (Teal) | Rinse |
| 8. Bake / Cure | Box 8 | 7.0" | `#E8A020` (Amber) | Cure |
| 9. Inspect | Box 9 | 1.5" | `#C8D0D8` (Silver) | Inspection |

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
Spray + immersion
pH 10--12, 1--5%
120--150 F (49--66 C)
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove stamping oils, metal fines, weld flux`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface`

*Box 2 -- Rinse:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Clean` (16 pt, `#F0EDE8` at 60%)
- Parameters: `2 stages counterflow` / `Conductivity monitored`
- Purpose: `Remove cleaner residuals before phosphating`
- Check: `Silicate carry-over kills phosphate crystals`

*Box 3 -- Zinc Phosphate:*
- Badge: `STAGE 3`, fill `#27AE60`
- Name: `Zinc Phosphate`
- Parameters: `95--115 F (35--46 C)` / `120--180 sec immersion` / `150--400 mg/ft2 coating wt`
- Purpose: `Crystalline corrosion barrier -- adhesion foundation`
- Check: `Surface conditioning (colloidal TiPO4) refines crystal size` (`#27AE60`)

*Box 4 -- Rinse / Seal / DI:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse / Seal / DI`
- Parameters: `2 rinse + seal rinse + DI` / `DI: < 20 uS/cm`
- Purpose: `Remove phosphate residuals; seal crystal porosity`
- Check: `Body enters e-coat tank WET -- no dry-off oven`

*Box 5 -- E-Coat Tank:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `E-Coat Tank` / Subtitle: `Cathodic Electrodeposition`
- Parameters: `18--22% solids` / `pH 5.8--6.2` / `200--400 V DC` / `120--180 sec`
- Purpose: `Electrodeposit primer into every cavity`
- Check: `Self-limiting: OH- gels film, stops deposition at thickness` (`#E8A020`)

*Box 6 -- UF Permeate Rinse:*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `UF Permeate Rinse`
- Parameters: `2--3 stages counterflow` / `Permeate from UF membranes` / `Recovers >95% dragout`
- Purpose: `Closed-loop paint recovery -- the e-coat hero`
- Check: `CRITICAL: >99% total paint utilization` (`#27AE60`)

*Box 7 -- DI Rinse:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `DI Rinse`
- Parameters: `Final clean rinse` / `< 20 uS/cm`
- Purpose: `Remove residual permeate before bake`
- Check: `Prevents water spots and defects in cure`

*Box 8 -- Bake / Cure:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Bake / Cure`
- Parameters: `350--375 F (177--191 C) oven` / `340--360 F metal temp` / `20--30 min at metal temp`
- Purpose: `Cross-link blocked isocyanate + epoxy resin`
- Check: `Afterburner required -- blocking agent VOC emission` (`#E05C5C`)

*Box 9 -- Inspect:*
- Badge: `STAGE 9`, fill `#C8D0D8`
- Name: `Inspect`
- Parameters: `DFT: 0.6--1.2 mils` / `MEK rub: 100+ double rubs` / `Adhesion: 5B (ASTM D3359)`
- Purpose: `Verify film build, cure, and adhesion`
- Check: `Throwing power test: DFT ratio inside vs. outside box`

---

**BLOCK C -- Stage Legend Strip**

Y: 15.0" to 15.8"

- Rounded rectangle, X: 0.5", Y: 15.0", W: 23.0", H: 0.7", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#27AE60` (Emerald) | `Pretreatment` |
| `#E8A020` (Amber) | `Coating & Cure` |
| `#C8D0D8` (Silver) | `Inspection` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 16.0" to 22.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 9-Row Parameter Table**

Y: 16.8" to 22.3". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Voltage/CD (3.0") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Chemistry | Temp | Time | Voltage/CD | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | pH 10--12, 1--5% | 120--150 F | 60--180 sec | -- | Water-break-free |
| 2. Rinse | City water, counterflow | Ambient | 30--60 sec | -- | Conductivity |
| 3. Zinc Phosphate | Total acid 18--25 pts | 95--115 F | 120--180 sec | -- | Coating wt 150--400 mg/ft2 |
| 4. Rinse/Seal/DI | Seal rinse + DI | Ambient | 30--60 sec | -- | DI < 20 uS/cm |
| 5. E-Coat Tank | 18--22% solids, pH 5.8--6.2 | 85--95 F | 120--180 sec | 200--400 V DC | Self-limiting film |
| 6. UF Permeate Rinse | UF permeate, counterflow | Ambient | -- | -- | >99% paint recovery |
| 7. DI Rinse | DI water | Ambient | 30--60 sec | -- | < 20 uS/cm |
| 8. Bake/Cure | Blocked isocyanate + epoxy | 350--375 F | 20--30 min | -- | MEK rub >= 100 |
| 9. Inspect | -- | -- | -- | -- | DFT 0.6--1.2 mils |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Cathodic vs. Anodic Comparison

**Dimensions:** Y: 22.5" to 28.5" (~6.0" tall).

---

**Section label:**
- Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> CATHODIC VS. ANODIC -- WHICH E-COAT?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 23.3" to 28.3".

**Left -- Cathodic Epoxy E-Coat:**
- Rounded rect, X: 0.5", Y: 23.3", W: 11.0", H: 4.8", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CATHODIC EPOXY E-COAT` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `>95% of Automotive E-Coat Worldwide` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Part polarity | Cathode (no metal dissolution) |
| Voltage | 200--400 V DC |
| Solids | 18--22% |
| pH | 5.8--6.2 |
| DFT | 0.6--1.2 mils (15--30 um) |
| Throwing power | Excellent (8--12" into box sections) |
| Chemistry | Epoxy-amine resin, blocked isocyanate |
| Corrosion | 500--1,000+ hr B117 (primer alone) |
| Anode | 316 stainless steel in anode boxes |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `The standard. No metal dissolution at cathode -- superior corrosion protection.` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Anodic Acrylic E-Coat:**
- Rounded rect, X: 12.0", Y: 23.3", W: 11.5", H: 4.8", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `ANODIC ACRYLIC E-COAT` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Simpler Chemistry, Non-Critical Apps` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Part polarity | Anode (metal dissolves into bath) |
| Voltage | 50--250 V DC |
| Solids | 8--14% |
| pH | 7.5--8.5 |
| DFT | 0.4--0.8 mils |
| Throwing power | Moderate |
| Chemistry | Acrylic resin, base-neutralized |
| Corrosion | Lower than cathodic |
| Anode | Carbon/graphite (SS dissolves) |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Simpler but metal dissolution contaminates bath -- use for small appliances, general industrial.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON E-COAT PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CRATERS / PINHOLES | Phosphate porosity or bath contamination | Improve seal rinse; filter bath |
| 2 | 6.33" | THIN FILM IN CAVITIES | Voltage too low or bath conductivity off | Increase voltage; check conductivity 1,000--1,800 uS/cm |
| 3 | 12.16" | POOR CURE (MEK FAIL) | Low oven temp or insufficient time at metal temp | Verify metal temp 340--360 F for 20--30 min |
| 4 | 18.0" | ORANGE PEEL / ROUGHNESS | Bath solids too high or P/B ratio drift | Check solids 18--22%; verify P/B 0.15--0.25 |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for cathodic epoxy e-coat systems. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; automotive OEM specifications.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> E-Coating -- Process Flow

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
| Zone 2 - Process Flow | Section label, nine flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 9-row table |
| Zone 4 - Cathodic vs Anodic | Section label, two comparison callouts |
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
| `E-Coating Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Coating Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Coating Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `E-Coating Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Coating Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `E-Coating Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire E-Coating cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#669--#676) zoom into each stage individually. The cathodic vs. anodic comparison answers the most common question in e-coat: "why cathodic?" The answer is simple -- no metal dissolution at the cathode means superior corrosion protection and bath stability. E-coat's throwing power into enclosed cavities is the best of any liquid coating method -- that is the central message.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #668 -- Construction Workup v1.0*
*2026-04-26*
