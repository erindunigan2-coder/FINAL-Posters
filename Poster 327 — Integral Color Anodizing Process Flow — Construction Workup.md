---
Project: Plating Posters Inc
Poster Number: 327
Title: "Integral Color Anodizing -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7)"
Technical Source: Industry-standard integral color anodizing process. Color forms DURING anodizing via organic acid electrolyte decomposition products incorporating into the growing oxide. Values are typical ranges for oxalic/sulfosalicylic acid-based systems. Proprietary formulations vary.
Process Scope: Integral color anodizing -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - ProcessFlow
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #327 -- Construction Workup
## Integral Color Anodizing -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Integral Color Anodizing. It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. The key differentiator: no dye step. Color forms inside the oxide during anodizing from organic acid decomposition products. This poster is the "map" that the other 7 posters (#328--#334) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (integral color vs. two-step electrolytic color), and a troubleshooting quick-hit strip. Dense but scannable.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Integral vs. Two-Step" comparison callout (Block E):** Two side-by-side callout boxes comparing integral color vs. two-step electrolytic color. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font:** Fallback: Courier Prime.

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
| Amber | `#E8A020` | High voltage emphasis, activation stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Anodize stage, seal, optimal reference |
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

ZONE 4 -- INTEGRAL VS. TWO-STEP COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Integral Color vs. Two-Step Electrolytic side-by-side callout

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

> INTEGRAL COLOR ANODIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Color forms during anodizing -- no dye step. Organic acid electrolytes at high voltage produce bronze-to-black tones locked inside the oxide.

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
| 2. Rinse (Pre-Etch) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Caustic Etch | Box 3 | 11.5" | `#E8A020` (Amber) | Etch |
| 4. Rinse (Pre-Desmut) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

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
| 5. Desmut (HNO3) | Box 5 | 17.0" | `#E8A020` (Amber) | Chemical |
| 6. Rinse (Pre-Anodize) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Integral Color Anodize | Box 7 | 6.0" | `#27AE60` (Emerald) | Anodize |
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
- Text: `Remove oils, soils, fingerprints`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Etch):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Etch` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove alkaline cleaner carry-over`
- Check: `Prevents cleaner contamination of etch bath`

*Box 3 -- Caustic Etch:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Caustic Etch`
- Parameters: `NaOH 40--80 g/L` / `130--150 F (55--65 C)` / `1--5 min`
- Purpose: `Uniform matte surface for consistent color`
- Check: `CRITICAL: Etch uniformity drives color consistency` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Desmut):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Desmut`
- Parameters: `Ambient temp` / `Cascade preferred`
- Purpose: `Remove caustic carry-over`
- Check: `NaOH drag-in contaminates desmut bath`

*Box 5 -- Desmut (HNO3):*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Desmut` / Subtitle: `Deoxidize`
- Parameters: `HNO3 25--50% v/v` / `Ambient` / `30--120 sec`
- Purpose: `Remove etch smut -- insoluble residues`
- Check: `Standard HNO3 sufficient for 6063`

*Box 6 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize`
- Parameters: `DI water preferred` / `< 100 uS/cm target`
- Purpose: `Prevent electrolyte contamination`
- Check: `CRITICAL: Chloride > 25 ppm causes pitting` (Coral `#E05C5C`)

*Box 7 -- Integral Color Anodize:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Anodize` / Subtitle: `Integral Color`
- Parameters: `H2SO4 + organic acids` / `50--80 V` / `59--77 F (15--25 C)` / `20--45 min`
- Purpose: `Color forms IN the oxide during growth`
- Check: `Alloy controls color -- 6063 is the standard`

*Box 8 -- Seal:*
- Badge: `STAGE 8`, fill `#27AE60`
- Name: `Seal`
- Parameters: `Nickel acetate preferred` / `158--185 F (70--85 C)` / `20--30 min`
- Purpose: `Lock in color, close pores`
- Check: `No dye step -- color is already integral`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Etch & Desmut` |
| `#27AE60` (Emerald) | `Anodize & Seal` |
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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Voltage/CD (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Voltage/CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Alk cleaner 4--8 oz/gal | 130--160 F | 2--10 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Conductivity check |
| 3. Etch | NaOH 40--80 g/L | 130--150 F | 1--5 min | -- | Etch uniformity |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | No caustic carry-over |
| 5. Desmut | HNO3 25--50% v/v | Ambient | 30--120 sec | -- | Complete smut removal |
| 6. Rinse | DI water preferred | Ambient | 60--120 sec | -- | < 100 uS/cm |
| 7. Anodize | H2SO4 + oxalic/sulfo acids | 59--77 F | 20--45 min | 50--80 V / 10--20 ASF | Alloy + temp = color |
| 8. Seal | Nickel acetate 5--8 g/L | 158--185 F | 20--30 min | -- | Best color retention |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Integral Color vs. Two-Step Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> HOW DOES IT COMPARE? -- INTEGRAL COLOR VS. TWO-STEP

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Integral Color Anodizing:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `INTEGRAL COLOR` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Color Forms During Anodizing` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Color source | Organic acid decomposition in oxide |
| Electrolyte | H2SO4 + oxalic/sulfosalicylic acid |
| Voltage | 50--80 V (high) |
| Steps | One electrochemical step |
| Color range | Light bronze to black |
| UV stability | Excellent -- inorganic/embedded |
| Color control | Alloy-dependent -- tight lot control needed |
| Best alloys | 6063, 5005 |
| Applications | Architectural facades, curtain walls |
| Dye step | None -- color IS the process |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `One step, one tank -- color and oxide grow together. Simplest color process, but alloy variation is the #1 challenge.` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Two-Step Electrolytic Color:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `TWO-STEP ELECTROLYTIC` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Metal Deposited After Anodizing` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Color source | Metal particles (Sn, Co, Ni) in pore bases |
| Electrolyte | Step 1: H2SO4 / Step 2: metal salt + AC |
| Voltage | Step 1: 15--18 V / Step 2: 10--18 V AC |
| Steps | Two electrochemical steps |
| Color range | Champagne to black |
| UV stability | Excellent -- inorganic metal particles |
| Color control | Time-controlled -- more reproducible |
| Best alloys | 6063, 6061, 5005 |
| Applications | Architectural, automotive trim |
| Dye step | None -- metal deposit IS the color |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Two tanks, two steps -- but better color reproducibility. Time controls darkness. Industry standard for architectural color.` -- Inter Medium, 13 pt, `#2EC4B6`

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
| 1 | 0.5" | COLOR VARIATION | Alloy lot-to-lot chemistry shift | Tight alloy sourcing; match extrusion heats |
| 2 | 6.33" | FADING (RARE) | Not true integral color (organic dye used) | Verify process is genuine integral color |
| 3 | 12.16" | PITTING | Chloride > 25 ppm in anodize bath | Check rinse water quality; monitor Cl- |
| 4 | 18.0" | UNEVEN ETCH | Etch time/temp inconsistent | Tighten etch controls (+/- 15 sec, +/- 1 C) |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry ranges for integral color anodizing. Specific formulations (Kalcolor, Duranodic, Permalux) are proprietary and vary by supplier. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Integral Color Anodizing -- Process Flow

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
| Zone 4 - Integral vs Two-Step | Section label, two comparison callouts |
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
| `Integral Color Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Integral Color Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Integral Color Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Integral Color Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Integral Color Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Integral Color Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Integral Color cluster. The flow diagram must be readable at 6 feet. The key message: NO DYE STEP. Color forms during anodizing from organic acid decomposition products incorporating into the oxide at high voltage (50--80 V). The comparison zone highlights the fundamental difference: integral color = one electrochemical step with color built in; two-step = anodize first, then deposit metal in a second tank.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #327 -- Construction Workup v1.0*
*2026-04-26*
