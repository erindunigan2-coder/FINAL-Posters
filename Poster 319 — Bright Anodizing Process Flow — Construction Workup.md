---
Project: Plating Posters Inc
Poster Number: 319
Title: "Bright Anodizing -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 6: Bright Anodizing)"
Technical Source: Industry-standard bright anodizing process. Not a different anodize chemistry -- it is standard Type II sulfuric acid anodize performed on a chemically polished (bright dipped) surface. The bright dip replaces the caustic etch. H3PO4 + HNO3 at near-boiling temperature produces a specular mirror finish. Values are typical industry ranges.
Process Scope: Bright anodizing -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BrightAnodizing
  - BrightDip
  - ProcessFlow
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #319 -- Construction Workup
## Bright Anodizing -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Bright Anodizing (AN-06). It shows the complete 8-stage process sequence at a glance. The key differentiator from standard Type II: the caustic etch is REPLACED by a bright dip (H3PO4 + HNO3 at 190--210 F). This produces a mirror-like specular finish instead of a matte surface. The anodize itself is standard Type II sulfuric acid. Safety is a dominant theme -- the bright dip is the single most hazardous operation in any anodizing shop.

Design philosophy: clean U-flow diagram as the hero, a parameter summary table, a comparison callout (bright anodize vs. standard matte Type II), and a safety-critical rules strip. The bright dip box must be visually prominent and flagged with safety warnings.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Stage 3 (Bright Dip) gets a Coral safety accent to flag the hazard.

2. **Parameter summary table (Block D):** 8 rows (one per stage).

3. **"Bright vs. Standard" comparison callout (Block E):** Side-by-side highlighting mirror finish vs. matte finish.

4. **Safety rules strip (Block F):** Four safety cards emphasizing NOx fumes, PPE, temperature, and automation.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font.** Fallback: Courier Prime.

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
| Amber | `#E8A020` | Key parameters, bright dip stage accent, temperature data |
| Teal | `#2EC4B6` | Cleaning & rinse stages |
| Emerald | `#27AE60` | Anodize stage, seal, optimal conditions |
| Coral | `#E05C5C` | Safety warnings, bright dip hazards, failure modes |
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

ZONE 4 -- BRIGHT VS. STANDARD COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Bright Anodize vs. Standard Matte Anodize side-by-side callout

ZONE 5 -- SAFETY RULES (28.5"--32.5" / ~4.0" tall)
  Block F: 4 safety cards for bright dip hazards

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

> BRIGHT ANODIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Clean to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> The mirror finish. Chemical polishing replaces caustic etch to produce specular reflectivity. Standard Type II anodize on a bright-dipped surface.

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
| 2. Rinse (Pre-Polish) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Bright Dip | Box 3 | 11.5" | `#E05C5C` (Coral) | Chemical Polish |
| 4. Desmut (if needed) | Box 4 | 17.0" | `#E8A020` (Amber) | Surface Prep |

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
| 5. Rinse (Pre-Anodize) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. Anodize (Type II) | Box 6 | 11.5" | `#27AE60` (Emerald) | Anodize |
| 7. Dye (Optional) | Box 7 | 6.0" | `#E8A020` (Amber) | Color |
| 8. Seal | Box 8 | 0.5" | `#27AE60` (Emerald) | Post-Treatment |

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
130--160 F (55--70 C)
4--8 oz/gal
2--10 min (soak)
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, buffing compounds`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `Cleanliness critical -- defects visible on mirror finish`

*Box 2 -- Rinse (Pre-Polish):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Polish` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove alkaline cleaner before bright dip`
- Check: `Cleaner carryover degrades bright dip chemistry`

*Box 3 -- Bright Dip:*
- Badge: `STAGE 3`, fill `#E05C5C`
- Name: `Bright Dip`
- Parameters: `H3PO4 85% + HNO3 5%` / `190--210 F (88--99 C)` / `30--120 sec`
- Purpose: `Chemical polish -- specular mirror finish`
- Check: `HAZARD: Toxic NOx fumes at operating temperature` (Coral `#E05C5C`)

*Box 4 -- Desmut (if needed):*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Desmut` / Subtitle: `If Needed`
- Parameters: `HNO3 25--50% v/v` / `Ambient` / `30--60 sec`
- Purpose: `Remove smut from Cu/Si alloys`
- Check: `Not required for most bright alloys (1xxx, 5xxx)`

*Box 5 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize`
- Parameters: `DI water preferred` / `< 100 uS/cm target`
- Purpose: `Prevent electrolyte contamination`
- Check: `Chloride > 25 ppm causes pitting on bright surface`

*Box 6 -- Anodize (Type II):*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Anodize` / Subtitle: `Standard Type II`
- Parameters: `H2SO4 150--200 g/L` / `68--72 F (20--22 C)` / `15--21V` / `15--40 min`
- Purpose: `Grow oxide over bright-dipped surface`
- Check: `Thin coat (0.2--0.5 mil) for maximum clarity`

*Box 7 -- Dye (Optional):*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Dye` / Subtitle: `Optional`
- Parameters: `Organic dyes 0.5--10 g/L` / `120--140 F (49--60 C)` / `10--30 min`
- Purpose: `Brilliant transparent color over reflective base`
- Check: `Dye BEFORE seal -- pores must be open`

*Box 8 -- Seal:*
- Badge: `STAGE 8`, fill `#27AE60`
- Name: `Seal`
- Parameters: `NiAc or cold seal` / `180--200 F (NiAc)` / `20--30 min`
- Purpose: `Lock in color, close pores`
- Check: `Hot water seal may slightly cloud bright finish`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E05C5C` (Coral) | `Bright Dip (Hazardous)` |
| `#E8A020` (Amber) | `Desmut & Dye` |
| `#27AE60` (Emerald) | `Anodize & Seal` |

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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Voltage/CD (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Voltage/CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Alk cleaner 4--8 oz/gal | 130--160 F | 2--10 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | No cleaner carryover |
| 3. Bright Dip | H3PO4 85% + HNO3 5% | 190--210 F | 30--120 sec | -- | NOx ventilation! |
| 4. Desmut | HNO3 25--50% (if needed) | Ambient | 30--60 sec | -- | Most bright alloys skip |
| 5. Rinse | DI water preferred | Ambient | 60--120 sec | -- | < 100 uS/cm |
| 6. Anodize | H2SO4 150--200 g/L | 68--72 F | 15--40 min | 15--21V / 12--18 ASF | Temp critical for clarity |
| 7. Dye | Organic dye 0.5--10 g/L | 120--140 F | 10--30 min | -- | Optional (clear = mirror) |
| 8. Seal | NiAc 5--8 g/L or cold seal | 180--200 F | 20--30 min | -- | NiAc clearer than hot water |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Bright vs. Standard Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> BRIGHT ANODIZE VS. STANDARD MATTE -- SAME OXIDE, DIFFERENT SURFACE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Bright Anodize:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `BRIGHT ANODIZE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Mirror Finish -- Chemically Polished` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Surface prep | Bright dip (H3PO4 + HNO3, 190--210 F) |
| Finish | Specular mirror (>80% reflectance) |
| Anodize | Standard Type II (same chemistry) |
| Coating thickness | 0.2--0.5 mil (thin for clarity) |
| Dye result | Brilliant transparent jewel tones |
| Clear result | Classic mirror -- "bright clear" |
| Best alloys | 1100, 5657, 5252, 6463 |
| Safety | HIGH -- NOx fumes, near-boiling acid |
| Applications | Automotive trim, reflectors, cosmetic hardware |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `The bright dip replaces caustic etch. Same anodize, different surface texture. Mirror clarity depends on alloy purity.` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Standard Matte (Type II):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `STANDARD MATTE TYPE II` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Satin Finish -- Caustic Etched` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Surface prep | Caustic etch (NaOH, 130--160 F) |
| Finish | Uniform matte / satin |
| Anodize | Standard Type II (identical) |
| Coating thickness | 0.2--1.0 mil |
| Dye result | Opaque saturated colors |
| Clear result | Uniform matte silver |
| Best alloys | 6063, 6061, 5052 (broad range) |
| Safety | Standard -- alkaline splash |
| Applications | Architectural, industrial, general purpose |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Caustic etch produces the familiar satin finish. Broader alloy compatibility. Lower safety risk than bright dip.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 5 -- Safety Rules

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> SAFETY -- BRIGHT DIP IS THE MOST HAZARDOUS ANODIZING OPERATION

---

**BLOCK F -- Four Safety Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Hazard | Detail |
|---|---|---|---|
| 1 | 0.5" | TOXIC NOx FUMES | Brown NO2 gas evolves vigorously at operating temperature. Garage-style hood + double-stage fume scrubber required. |
| 2 | 6.33" | NEAR-BOILING ACID | 190--210 F phosphoric/nitric mix. Full face shield, butyl rubber gloves, acid-resistant suit required. |
| 3 | 12.16" | AUTOMATE IF POSSIBLE | Many shops automate bright dip to minimize operator exposure. Manual operation requires continuous respiratory monitoring. |
| 4 | 18.0" | TANK CONSTRUCTION | Double-walled polypropylene or PVDF. No stainless steel (HNO3 attacks it). Integrated spill containment. |

Interior per card:
- Hazard: Barlow SemiBold, 16 pt, `#E05C5C`
- Detail: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry ranges for bright anodizing. Specific bright dip formulations and operating conditions vary by supplier. The bright dip step involves significant safety hazards -- consult your facility EHS program and applicable OSHA regulations.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Bright Anodizing -- Process Flow

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
| Zone 4 - Bright vs Standard | Section label, two comparison callouts |
| Zone 5 - Safety Rules | Section label, four safety cards |
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
| `Bright Anodizing Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bright Anodizing Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bright Anodizing Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Bright Anodizing Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bright Anodizing Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Bright Anodizing Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Bright anodizing is the glamour process of anodizing, but the bright dip is the single most dangerous operation in any anodizing shop. This poster must balance the appeal of the mirror finish with the gravity of the safety requirements. Stage 3 (Bright Dip) is intentionally flagged with Coral instead of the typical Amber used for etch/surface prep -- it is a safety-critical operation that demands visual differentiation. The comparison zone educates operators that bright anodize and standard matte use the SAME anodize chemistry -- only the surface prep differs.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #319 -- Construction Workup v1.0*
*2026-04-26*
