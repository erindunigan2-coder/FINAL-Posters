---
Project: Plating Posters Inc
Poster Number: 311
Title: "Phosphoric Acid Anodizing (PAA) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA)"
  - "ASTM D3933; Boeing BAC 5555"
Technical Source: Industry-standard phosphoric acid anodizing process per ASTM D3933 and Boeing BAC 5555. PAA is a bonding surface preparation process -- NOT a protective coating. Produces whisker-like pore morphology for structural adhesive interlocking.
Process Scope: Phosphoric acid anodizing -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - PhosphoricAcid
  - ProcessFlow
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #311 -- Construction Workup
## Phosphoric Acid Anodizing (PAA) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Phosphoric Acid Anodizing. It shows the complete process sequence at a glance -- every stage visible in one U-flow diagram. PAA is the outlier in anodizing: it is NEVER sealed, NEVER dyed, and exists solely to create a surface for structural adhesive bonding. The poster must make this distinction visually unmistakable from all other anodizing process flows.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a "PAA vs. Type II" comparison callout (emphasizing that PAA is NOT a protective coating), and a critical rules strip. The 72-hour prime window is the defining constraint of this process.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Stage 7 includes a prominent "PRIME WITHIN 72 HRS" callout. Note: PAA has 7 functional stages (no seal/dye), but the final stage is "Post Treatment (Bond Prep)" which replaces seal. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters.

3. **"PAA vs. Type II" comparison callout (Block E):** Two side-by-side callout boxes. This is the most important educational element -- PAA is fundamentally different from all other anodizing.

4. **Critical Rules strip (Block F):** Three large-format warning cards emphasizing NEVER SEAL, NEVER DYE, PRIME WITHIN 72 HOURS.

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
| Amber | `#E8A020` | Key parameters, warning headers, voltage/CD data |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Anodize stage, optimal reference |
| Coral | `#E05C5C` | NEVER SEAL / NEVER DYE warnings, failure modes |
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

ZONE 4 -- PAA VS. TYPE II COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: PAA vs. Standard Anodize side-by-side callout

ZONE 5 -- CRITICAL RULES (28.5"--32.5" / ~4.0" tall)
  Block F: Three non-negotiable rules cards

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

> PHOSPHORIC ACID ANODIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- Bonding Surface Preparation

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> PAA per ASTM D3933 / Boeing BAC 5555 -- the aerospace standard for structural adhesive bonding prep. This is NOT a protective coating.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PAA PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row of four boxes, bottom row of three boxes in a U-flow pattern.

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
| 2. Rinse (Pre-Etch) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Etch / Grit Blast | Box 3 | 11.5" | `#E8A020` (Amber) | Surface Prep |
| 4. Desmut | Box 4 | 17.0" | `#E8A020` (Amber) | Surface Prep |

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
| 5. Rinse (Pre-Anodize) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. PAA Anodize | Box 6 | 11.5" | `#27AE60` (Emerald) | Anodize |
| 7. Post Treatment (Bond Prep) | Box 7 | 0.5" | `#E8A020` (Amber) | Post Treatment |

Box 7 is wider (W: 10.0") to accommodate the 72-hour prime callout.

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
- Text: `NEVER use silicated cleaners before anodizing`

*Box 2 -- Rinse (Pre-Etch):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Etch` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove alkaline cleaner before etch`
- Check: `Prevents contamination of etch bath`

*Box 3 -- Etch / Grit Blast:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Etch / Grit Blast`
- Parameters: `NaOH 40--60 g/L, 55--60 C, 1--3 min` / `OR: 180--220 grit alumina, 30--40 psi` / `OR: FPL etch (legacy, uses Cr6+)`
- Purpose: `Uniform surface for oxide growth`
- Check: `P2 etch = Cr6+-free FPL replacement` (Teal `#2EC4B6`)

*Box 4 -- Desmut:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Desmut`
- Parameters: `HNO3 25--50% v/v` / `Ambient, 30--120 sec` / `HNO3/HF for Cu alloys`
- Purpose: `Remove insoluble smut from etch`
- Check: `CAUTION: HF requires calcium gluconate on site` (Coral `#E05C5C`)

*Box 5 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize`
- Parameters: `DI water required` / `< 100 uS/cm target` / `Double cascade minimum`
- Purpose: `Prevent contamination of PAA bath`
- Check: `Fluoride dragover destroys oxide structure`

*Box 6 -- PAA Anodize:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `PAA Anodize` / Subtitle: `Bonding Surface`
- Parameters: `H3PO4 100--120 g/L` / `20--25 C (68--77 F)` / `10--15V (BAC 5555: 10V +/- 1V)` / `20--25 min`
- Purpose: `Create whisker-like pore structure for adhesive interlocking`
- Check: `0.5--1.5 um coating -- intentionally thin` (Emerald `#27AE60`)

*Box 7 -- Post Treatment (Bond Prep):*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post Treatment` / Subtitle: `Bond Prep`
- Parameters: `DI rinse, ambient` / `Dry: warm air < 60 C` / `Apply primer within 72 hours`
- Purpose: `Prepare PAA surface for adhesive bonding`
- Check -- LARGE FORMAT, Coral:
- Inter Medium, 16 pt, `#E05C5C`
- Text: `NEVER SEAL -- sealing destroys bonding effectiveness`
- Below: Inter Medium, 14 pt, `#E8A020`
- Text: `72-HOUR WINDOW: Prime or restart the entire process`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Surface Prep & Post-Treatment` |
| `#27AE60` (Emerald) | `Anodize (PAA)` |
| `#E05C5C` (Coral) | `Caution / Critical Rule` |

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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Voltage/CD (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Chemistry | Temp | Time | V / CD | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | Non-silicated alk cleaner 4--8 oz/gal | 130--160 F | 2--10 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Cascade preferred |
| 3. Etch / Grit Blast | NaOH 40--60 g/L or 180--220 grit | 130--150 F (etch) | 1--3 min | -- | Alloy-dependent |
| 4. Desmut | HNO3 25--50% v/v (+/- HF) | Ambient | 30--120 sec | -- | HF for Cu alloys |
| 5. Rinse | DI water | Ambient | 60--120 sec | -- | < 100 uS/cm |
| 6. PAA Anodize | H3PO4 100--120 g/L | 68--77 F | 20--25 min | 10--15V / 5--15 ASF | BAC 5555: 10V +/- 1V |
| 7. Post Treatment | DI rinse + warm air dry | < 140 F dry | Per spec | -- | PRIME WITHIN 72 HRS |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- PAA vs. Type II Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> PAA VS. STANDARD ANODIZE -- FUNDAMENTALLY DIFFERENT

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Phosphoric Acid Anodize (PAA):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `PHOSPHORIC ACID ANODIZE (PAA)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Bonding Surface Prep` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Purpose | Structural adhesive bonding prep |
| Electrolyte | H3PO4 100--120 g/L |
| Coating thickness | 0.5--1.5 um (extremely thin) |
| Oxide morphology | Open whisker/dendrite pore structure |
| Sealed? | NEVER -- sealing destroys bond surface |
| Dyed? | NEVER -- no decorative function |
| Corrosion protection | Virtually none (not the purpose) |
| Time-to-prime | < 72 hours or restart |
| Primary spec | ASTM D3933 / BAC 5555 |
| Application | Aerospace fuselage skins, honeycomb panels |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `PAA creates micro-roughness for adhesive interlocking -- bond strength > 40 MPa (6000 psi)` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Standard Type II Anodize:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `TYPE II SULFURIC ACID ANODIZE` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Protective / Decorative Coating` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Purpose | Corrosion protection + decoration |
| Electrolyte | H2SO4 150--200 g/L |
| Coating thickness | 5--25 um (10--50x thicker) |
| Oxide morphology | Ordered hexagonal pore array |
| Sealed? | Always (hot water or nickel acetate) |
| Dyed? | Full color spectrum available |
| Corrosion protection | 336--1000+ hrs ASTM B117 |
| Time-to-prime | Not applicable |
| Primary spec | MIL-A-8625F Type II |
| Application | Decorative, architectural, industrial |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Type II is the workhorse -- corrosion protection, dyeability, and durability in one coating` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 5 -- Critical Rules

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> NON-NEGOTIABLE RULES -- PAA

---

**BLOCK F -- Three Rule Cards**

Y: 29.4" to 32.3". Three cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 7.33", H: 2.7", fill `#1E2435`, radius 6.

| Card | X | Accent | Rule | Explanation |
|---|---|---|---|---|
| 1 | 0.5" | `#E05C5C` (left 0.06") | NEVER SEAL | Sealing closes the pores that provide mechanical interlocking for adhesive. Sealed PAA = failed bonds. |
| 2 | 8.16" | `#E05C5C` (left 0.06") | NEVER DYE | PAA has no decorative function. Dye molecules contaminate the bond surface. |
| 3 | 15.83" | `#E8A020` (left 0.06") | PRIME WITHIN 72 HOURS | Atmospheric hydration closes pores over time. After 72 hours, bond strength degrades significantly. Some specs require priming within one shift. |

Interior per card:
- Rule: Barlow SemiBold, 22 pt, `#E05C5C` (cards 1--2) or `#E8A020` (card 3)
- Explanation: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for phosphoric acid anodizing per ASTM D3933. Specific process limits vary by OEM specification (Boeing, Airbus, etc.). Consult your process engineer and applicable specifications for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Phosphoric Acid Anodizing (PAA) -- Process Flow

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
| Zone 4 - PAA vs Type II | Section label, two comparison callouts |
| Zone 5 - Critical Rules | Section label, three rule cards |
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
| `PAA Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PAA Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PAA Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `PAA Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PAA Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PAA Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

PAA is the outlier of anodizing. This poster must visually scream "this is different" -- the NEVER SEAL / NEVER DYE rules and the 72-hour prime window are the defining constraints. The comparison callout against Type II is essential because many operators who work Type II lines will misapply their instincts to PAA (wanting to seal, wanting to dye, etc.). The flow diagram has only 7 functional stages because there is no seal or dye step -- the "post treatment" is primer application and bond prep. Use Coral prominently for the critical rules to ensure they cannot be overlooked.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #311 -- Construction Workup v1.0*
*2026-04-26*
