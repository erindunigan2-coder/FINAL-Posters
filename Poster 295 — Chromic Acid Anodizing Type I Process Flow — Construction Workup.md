---
Project: Plating Posters Inc
Poster Number: 295
Title: "Chromic Acid Anodizing (Type I) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3: Chromic Acid Anodizing)"
Technical Source: Industry-standard chromic acid anodizing per MIL-A-8625F Type I / Type IB. Voltage-controlled process using CrO3 electrolyte. Thinnest anodize film (0.5--2.5 um). Aerospace legacy process under severe regulatory pressure due to Cr(VI). Being replaced by BSAA (Posters 303--310).
Process Scope: Chromic acid anodizing (Type I) -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - ProcessFlow
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #295 -- Construction Workup
## Chromic Acid Anodizing (Type I) -- Process Flow

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Chromic Acid Anodizing (Type I). It shows the complete 8-stage process at a glance. The framing is critical: Type I is the aerospace legacy standard -- thin, fatigue-friendly, self-healing -- but it uses hexavalent chromium, a confirmed human carcinogen. The poster must convey both the technical elegance of the process and the regulatory reality that it is being phased out in favor of BSAA (Poster 303). Every poster in this cluster carries a Cr(VI) safety warning.

Design philosophy: U-flow diagram as hero, parameter summary table, "Type I vs. BSAA" comparison callout (the regulatory transition story), troubleshooting quick-hits, and a prominent Cr(VI) safety banner. The safety banner is non-negotiable on every Type I poster.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box color-coded by stage type. Standard geometry.

2. **Cr(VI) safety banner (Block C1):** Full-width coral-tinted banner immediately below the flow diagram. This is the single most important non-technical element on every Type I poster.

3. **Parameter summary table (Block D):** Compact 8-row table (one row per stage) with key parameters.

4. **"Type I vs. BSAA" comparison callout (Block E):** Two side-by-side callout boxes showing the legacy process alongside its Cr(VI)-free replacement. The regulatory transition narrative.

5. **Troubleshooting quick-hit strip (Block F):** Horizontal strip of 4 common problems.

6. **4 pt left-border accents on callout boxes.**

7. **Global Colors / swatch remap for Light edition.**

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
| Amber | `#E8A020` | Key parameters, voltage ramp stages |
| Teal | `#2EC4B6` | Cleaning & rinse stages |
| Emerald | `#27AE60` | Anodize stage (main tank) |
| Coral | `#E05C5C` | Safety warnings, Cr(VI) banner, defects |
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
- 29.0" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline + Cr(VI) warning flag

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip
  Block C1: Cr(VI) SAFETY BANNER (full width, coral)

ZONE 3 -- PARAMETER SUMMARY TABLE (16.0"--22.5" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- TYPE I vs. BSAA COMPARISON (22.5"--29.0" / ~6.5" tall)
  Block E: Legacy vs. replacement side-by-side callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (29.0"--32.5" / ~3.5" tall)
  Block F: 4-problem strip with one-line fixes

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
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> CHROMIC ACID ANODIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Type I -- Complete Process Flow -- 8 Stages from Cleaning to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.1"
- Width: 18.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> The aerospace legacy process. Thinnest film, lowest fatigue impact, self-healing Cr(VI) -- and being phased out. Know it before it's gone.

**BLOCK A -- Cr(VI) Flag (right side)**

- Rounded rect, X: 19.0", Y: 2.0", W: 4.5", H: 0.7", fill `#E05C5C` at 25%, border 1 pt `#E05C5C`, radius 4
- Text: `CONTAINS Cr(VI) -- CARCINOGEN` Barlow SemiBold 14 pt `#E05C5C`, center

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 16.0" (~13.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 12.5" (~8.7" tall). Two rows of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 3.8"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 7.6") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Etch) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Light Etch or None | Box 3 | 11.5" | `#E8A020` (Amber) | Etch |
| 4. Desmut | Box 4 | 17.0" | `#E8A020` (Amber) | Activation |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~5.7")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 7.6" (bottom center Box 4)
- To: X: 19.5", Y: 8.5" (top center Box 5)

**Bottom Row (Y: 8.5" to 12.3") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Rinse (Pre-Anodize) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. Chromic Acid Anodize | Box 6 | 11.5" | `#27AE60` (Emerald) | Anodize |
| 7. Rinse (Post-Anodize) | Box 7 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 8. Seal / Post Treatment | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Alkaline Clean:*

Stage badge:
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Alkaline Clean`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
130--160 F (55--70 C)
4--8 oz/gal
3--10 min
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, fingerprints`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `NO silicated cleaners -- blocks thin oxide growth`

*Box 2 -- Rinse (Pre-Etch):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Etch` (14 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove alkaline cleaner carry-over`
- Check: `Prevents cleaner drag-in to etch`

*Box 3 -- Light Etch or None:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Etch` / Subtitle: `Light or None` (14 pt, `#F0EDE8` at 60%)
- Parameters: `NaOH 20--40 g/L (if used)` / `50--55 C, 15--60 sec` / `Often skipped entirely`
- Purpose: `Minimal surface prep -- thin coating cannot hide roughness`
- Check: `2024 alloy: light etch or skip` (`#E8A020`)

*Box 4 -- Desmut:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Desmut` / Subtitle: `Deoxidize` (14 pt, `#F0EDE8` at 60%)
- Parameters: `HNO3 25--50% v/v` / `HNO3/HF for 2024, 7075` / `Ambient, 30--120 sec`
- Purpose: `Remove etch smut -- visible under thin Type I coating`
- Check: `CAUTION: HF is a systemic toxin -- calcium gluconate on site` (`#E05C5C`)

*Box 5 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize (Critical)` (14 pt, `#F0EDE8` at 60%)
- Parameters: `DI water mandatory` / `Triple cascade (aerospace)` / `Conductivity < 100 uS/cm`
- Purpose: `Protect chromic acid bath from contamination`
- Check: `Cl- < 10 ppm | SO4 2- < 0.5 g/L in bath` (`#E05C5C`)

*Box 6 -- Chromic Acid Anodize:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Chromic Acid Anodize` / Subtitle: `Type I Main Tank` (14 pt, `#F0EDE8` at 60%)
- Parameters: `CrO3 40--80 g/L` / `89--100 F (32--38 C)` / `Voltage ramp to 40V` / `0.5--2.5 um film`
- Purpose: `Thin, fatigue-friendly anodic oxide with Cr(VI)`
- Check: `Voltage-controlled -- NOT current-controlled` (`#27AE60`)

*Box 7 -- Rinse (Post-Anodize):*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Anodize` (14 pt, `#F0EDE8` at 60%)
- Parameters: `DI water` / `Ambient temp`
- Purpose: `Remove Cr(VI) electrolyte before seal`
- Check: `Cr(VI) rinse water is hazardous waste (D007)`

*Box 8 -- Seal / Post Treatment:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Seal` / Subtitle: `Post Treatment` (14 pt, `#F0EDE8` at 60%)
- Parameters: `Hot DI water: 96--100 C, 15 min` / `or Nickel acetate: 75--85 C` / `or Unsealed (paint base)`
- Purpose: `Close pores, lock in corrosion resistance`
- Check: `Dyeing rarely specified -- thin coating = pale colors`

---

**BLOCK C -- Stage Legend Strip**

Y: 12.6" to 13.4"

- Rounded rectangle, X: 0.5", Y: 12.6", W: 23.0", H: 0.7", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Etch, Desmut & Post-Treatment` |
| `#27AE60` (Emerald) | `Anodize (Main Tank)` |
| `#E05C5C` (Coral) | `Caution / Cr(VI) Warning` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 13 pt, `#F0EDE8`.

---

**BLOCK C1 -- Cr(VI) Safety Banner**

Y: 13.7" to 15.8"

- Rounded rectangle, X: 0.5", Y: 13.7", W: 23.0", H: 2.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 6

**Banner headline:**
- Barlow Condensed ExtraBold, 24 pt, `#E05C5C`, center
- Text:

> HEXAVALENT CHROMIUM (Cr6+) -- CONFIRMED HUMAN CARCINOGEN

**Banner body:**
- Inter Medium, 14 pt, `#F0EDE8`, center, line height 155%

```
OSHA PEL: 0.005 mg/m3 (8-hr TWA) | IARC Group 1 Carcinogen
Engineering controls: enclosed tanks, mist suppressants, HEPA filtration, local exhaust ventilation
PPE: respiratory protection (P100 or supplied air), chemical splash goggles, face shield, Cr(VI)-rated gloves
Medical surveillance: REQUIRED for all Cr(VI)-exposed workers (OSHA 1910.1026)
Waste: EPA hazardous waste code D007 -- reduce Cr(VI) to Cr(III) before discharge
```

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 16.0" to 22.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 8-Row Parameter Table**

Y: 16.8" to 22.3". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Voltage/CD (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Voltage/CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Alk cleaner 4--8 oz/gal | 130--160 F | 3--10 min | -- | No silicates |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Cascade |
| 3. Etch | NaOH 20--40 g/L (if used) | 120--130 F | 15--60 sec | -- | Light or skip |
| 4. Desmut | HNO3 25--50% v/v | Ambient | 30--120 sec | -- | HF for Cu alloys |
| 5. Rinse | DI water (mandatory) | Ambient | 60--120 sec | -- | Cl- < 10 ppm |
| 6. Anodize | CrO3 40--80 g/L | 89--100 F | 30--60 min | Ramp to 40V | Voltage control |
| 7. Rinse | DI water | Ambient | 30--60 sec | -- | Haz waste rinse |
| 8. Seal | Hot DI or Ni acetate | 185--212 F | 15--30 min | -- | Unsealed for paint |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Type I vs. BSAA Comparison

**Dimensions:** Y: 22.5" to 29.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE TRANSITION -- TYPE I vs. BSAA (TYPE IC)

---

**BLOCK E -- Side-by-Side Comparison**

Y: 23.4" to 28.8".

**Left -- Chromic Acid Anodizing (Type I):**
- Rounded rect, X: 0.5", Y: 23.4", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `CHROMIC ACID ANODIZING (TYPE I)` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Subtitle: `The Legacy Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 13 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Electrolyte | CrO3 (chromic acid) |
| Cr(VI) content | YES -- confirmed carcinogen |
| Film thickness | 0.5--2.5 um (thinnest anodize) |
| Fatigue impact | Minimal -- preserves substrate life |
| Voltage | Ramp to 40V (5-step profile) |
| Temperature | 89--100 F (32--38 C) |
| Self-healing | YES -- residual Cr(VI) passivates scratches |
| 2024 alloy | Good -- better than Type II |
| Regulatory status | BEING PHASED OUT |
| Waste treatment | Hazardous waste (EPA D007) |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `Under severe regulatory pressure -- REACH, RoHS, OSHA driving replacement` -- Inter Medium, 12 pt, `#E05C5C`

**Right -- BSAA (Type IC):**
- Rounded rect, X: 12.0", Y: 23.4", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `BSAA ANODIZING (TYPE IC)` -- Barlow SemiBold, 18 pt, `#27AE60`
- Subtitle: `The Cr(VI)-Free Replacement` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Electrolyte | H2SO4 + H3BO3 (dilute) |
| Cr(VI) content | NONE -- total Cr(VI)-free line |
| Film thickness | 1--5 um (comparable) |
| Fatigue impact | Minimal -- thin film |
| Voltage | 15V constant |
| Temperature | 77--81 F (25--27 C) |
| Self-healing | No -- no Cr(VI) reservoir |
| 2024 alloy | Good -- handles Cu alloys well |
| Regulatory status | GROWING -- the future |
| Waste treatment | Standard acid neutralization |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Boeing BAC 5632 origin -- now MIL-A-8625F Type IC -- eliminates all Cr(VI)` -- Inter Medium, 12 pt, `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 29.0" to 32.5" (~3.5" tall).

---

**Section label:**
- Centered. Y: 29.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 29.8" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BURNING AT EDGES | Voltage ramp too fast or surface geometry | Slow the ramp; review rack design |
| 2 | 6.33" | THIN/NO COATING | Sulfate contamination > 0.5 g/L; high Cr3+ | Analyze bath; control Cr3+ < 20 g/L |
| 3 | 12.16" | DISCOLORATION | High dissolved Al; organic contamination | Carbon treat; partial bath replacement |
| 4 | 18.0" | SOFT COATING | Excessive Cr3+; bath temp too high | Monitor Cr3+/Cr6+ ratio; cool bath |

Interior per card:
- Problem: Barlow SemiBold, 15 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for chromic acid anodizing per MIL-A-8625F Type I. Specific formulations and limits vary by specification and facility. Cr(VI) safety requirements are regulatory minimums -- consult your facility's EHS program for site-specific protocols.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.6"

> Chromic Acid Anodizing (Type I) -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline, Cr(VI) flag |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip, Cr(VI) safety banner |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Type I vs BSAA | Section label, two comparison callouts |
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

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Chromic Acid Anodizing Type I Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromic Acid Anodizing Type I Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromic Acid Anodizing Type I Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Chromic Acid Anodizing Type I Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromic Acid Anodizing Type I Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromic Acid Anodizing Type I Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Type I cluster. The dual narrative is essential: (1) the technical elegance of chromic acid anodizing -- thinnest film, best fatigue performance, unique self-healing from residual Cr(VI); and (2) the regulatory reality -- Cr(VI) is a confirmed carcinogen and the process is being replaced. The Type I vs. BSAA comparison panel is unique to this process flow poster and tells the transition story. The Cr(VI) safety banner must be visually prominent -- coral background, bold text, cannot be missed at wall distance.

---

*Alaina -- Plating Posters Inc*
*Poster #295 -- Construction Workup v1.0*
*2026-04-26*
