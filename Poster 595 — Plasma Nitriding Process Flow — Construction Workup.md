---
Project: Plating Posters Inc
Poster Number: 595
Title: "Plasma Nitriding / Ion Nitriding -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5: Plasma Nitriding)"
Technical Source: Industry-standard plasma (ion) nitriding process. Covers the complete 7-stage sequence from part preparation through final inspection. Values are typical ranges for DC glow-discharge plasma nitriding in N2/H2 atmosphere at low vacuum (0.5-10 mbar). No ammonia required.
Process Scope: Plasma nitriding -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PlasmaNitriding
  - IonNitriding
  - ProcessFlow
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #595 -- Construction Workup
## Plasma Nitriding / Ion Nitriding -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Plasma Nitriding. It shows the complete 7-stage process sequence at a glance -- every stage visible in one U-flow diagram. A furnace operator sees the full cycle, a quality engineer checks parameters, a maintenance tech understands the sequence. This poster is the "map" that the other 8 posters (#596--#603) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (plasma vs. gas nitriding -- why choose plasma?), and a troubleshooting quick-hit strip. Dense but scannable -- the operator's wall reference for the entire process.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Why Plasma?" comparison callout (Block E):** Two side-by-side callout boxes comparing plasma vs. gas nitriding. Established pattern from Poster #31.

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
| Amber | `#E8A020` | Heating stages, warning headers, plasma glow accent |
| Teal | `#2EC4B6` | Preparation & cooling stages, structural positives |
| Emerald | `#27AE60` | Nitriding cycle (core process), optimal reference |
| Coral | `#E05C5C` | Problems, defects, safety callouts |
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

ZONE 4 -- WHY PLASMA? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Plasma vs. Gas Nitriding side-by-side callout

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

> PLASMA NITRIDING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 7 Stages from Part Prep to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Glow-discharge diffusion hardening in N2/H2 -- no ammonia, no quench, total compound layer control. Hang this poster at the furnace.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row has four boxes, bottom row has three boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Preparation | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Loading / Fixturing | Box 2 | 6.0" | `#2EC4B6` (Teal) | Preparation |
| 3. Vacuum Pumpdown | Box 3 | 11.5" | `#E8A020` (Amber) | System Setup |
| 4. Plasma Ignition & Heat-Up | Box 4 | 17.0" | `#E8A020` (Amber) | System Setup |

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
| 5. Nitriding Cycle | Box 5 | 17.0" | `#27AE60` (Emerald) | Core Process |
| 6. Cooling | Box 6 | 11.5" | `#2EC4B6` (Teal) | Cooling |
| 7. Inspection & QA | Box 7 | 6.0" | `#E8A020` (Amber) | Quality |

Box 7 width adjusted to 5.0" (same as others). Remaining space (0.5"--5.5") left open for visual balance.

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Preparation:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Degrease / solvent clean
Verify Q&T condition
Temper > nitride temp + 50 F
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove contaminants; ensure prior heat treatment is correct`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Surface must be chemically clean -- oil blocks nitrogen`

*Box 2 -- Loading / Fixturing:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Loading`
- Parameters: `Min spacing 10 mm` / `Non-magnetic fixtures` / `Electrical contact to cathode`
- Purpose: `Position parts on cathode for uniform plasma coverage`
- Check: `Avoid hollow cathode geometry -- holes < 3x depth cause arcing`

*Box 3 -- Vacuum Pumpdown:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Vacuum Pumpdown`
- Parameters: `Pump to < 0.1 mbar` / `Mechanical pump + Roots blower` / `Leak rate check`
- Purpose: `Remove air and moisture from chamber`
- Check: `Moisture causes oxidation -- base vacuum must be verified`

*Box 4 -- Plasma Ignition & Heat-Up:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Plasma Ignition` / Subtitle: `& Heat-Up`
- Parameters: `400--1000 V DC (pulsed)` / `N2/H2 @ 1--5 mbar` / `Sputter clean surface`
- Purpose: `Ignite glow discharge; heat parts to nitriding temperature`
- Check: `Visible purple/violet glow confirms plasma -- uniform glow = good`

*Box 5 -- Nitriding Cycle:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Nitriding Cycle` / Subtitle: `Core Process`
- Parameters: `930--1000 F (500--540 C)` / `25% N2 / 75% H2 typical` / `4--40 hours` / `1--5 mbar`
- Purpose: `Nitrogen diffusion into surface -- hardness by nitride precipitation`
- Check: `Gas ratio controls compound layer: more H2 = thinner/no white layer`

*Box 6 -- Cooling:*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Cooling`
- Parameters: `Cool under N2 or N2/H2` / `No quench required` / `Slow cool in vacuum`
- Purpose: `Controlled cool-down; no phase transformation needed`
- Check: `NO QUENCH -- hardness is from precipitation, not martensite`

*Box 7 -- Inspection & QA:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Inspection & QA`
- Parameters: `Microhardness traverse` / `White layer metallography` / `Dimensional check`
- Purpose: `Verify case depth, surface hardness, compound layer to specification`
- Check: `Use Vickers/Knoop -- HRC penetrates through thin cases`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Cooling` |
| `#E8A020` (Amber) | `System Setup & Quality` |
| `#27AE60` (Emerald) | `Nitriding Cycle (Core)` |
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
- Stage (3.5") | Gas / Atmosphere (5.5") | Temperature (3.0") | Time (2.5") | Pressure (3.0") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Gas / Atm | Temp | Time | Pressure | Key Control |
|---|---|---|---|---|---|
| 1. Part Prep | -- | Ambient | -- | -- | Q&T verified; chemically clean |
| 2. Loading | -- | Ambient | -- | Atmospheric | 10 mm min spacing; cathode contact |
| 3. Pumpdown | Evacuate | Ambient | 10--30 min | < 0.1 mbar | Leak rate verification |
| 4. Plasma Ignition | N2/H2 mix | Ramp to 930--1000 F | 1--3 hr ramp | 1--5 mbar | Uniform glow; pulsed DC 400--1000 V |
| 5. Nitriding | 25% N2 / 75% H2 | 930--1000 F | 4--40 hr | 1--5 mbar | Gas ratio = compound layer control |
| 6. Cooling | N2 or N2/H2 | Cool to < 300 F | 2--6 hr | Low vacuum | No quench; slow cool |
| 7. Inspection | -- | Ambient | -- | -- | Microhardness; white layer check |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Plasma? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY PLASMA? -- PLASMA VS. GAS NITRIDING

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Plasma (Ion) Nitriding:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `PLASMA (ION) NITRIDING` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Precision Option` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Atmosphere | N2 + H2 (no ammonia) |
| Temperature | 650--1050 F (wider range) |
| Compound layer | Fully controllable (incl. NONE) |
| Stainless steel | YES -- breaks passive film by sputtering |
| Masking | Mechanical (close-fit steel masks) |
| Cycle time | 20--30% shorter than gas |
| Uniformity risk | Edge effect; hollow cathode on small holes |
| Capital cost | Higher (vacuum vessel + DC power supply) |
| Safety | No ammonia; H2 + electrical hazards |
| Active screen (ASPN) | Eliminates arcing issues |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Total compound layer control -- the only nitriding method that can produce ZERO white layer` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Gas Nitriding:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `GAS NITRIDING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Established Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Atmosphere | Ammonia (NH3) |
| Temperature | 925--1050 F (narrower range) |
| Compound layer | Limited control (two-stage Floe reduces) |
| Stainless steel | Difficult (passive film blocks nitrogen) |
| Masking | Tin or copper electroplate stop-off |
| Cycle time | 10--90+ hours |
| Uniformity risk | Blind holes; gas circulation dependent |
| Capital cost | Lower (sealed retort furnace) |
| Safety | Ammonia handling required (TLV 25 ppm) |
| Dissociation control | Burette analysis; Kn monitoring |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Lower capital cost and simpler equipment -- the workhorse for high-volume, long-cycle nitriding` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | ARCING / HOLLOW CATHODE | Small holes, sharp edges, parts too close | Min hole dia 3x depth; 10 mm spacing; use ASPN |
| 2 | 6.33" | NON-UNIFORM CASE | Complex load geometry; temp variation | Pulsed DC duty cycle; supplemental heaters; multi-point TC |
| 3 | 12.16" | EDGE EFFECT | Higher plasma density at corners/edges | Generally acceptable; active screen minimizes |
| 4 | 18.0" | NO COMPOUND LAYER (WHEN SPECIFIED) | Gas ratio too H2-rich; temp too high | Increase N2 %; reduce temperature |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for DC glow-discharge plasma nitriding. Specific equipment configurations, gas ratios, and process limits vary by furnace manufacturer and application specification. Consult your equipment supplier and applicable standards (AMS 2759/10) for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Plasma Nitriding / Ion Nitriding -- Process Flow

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
| Zone 4 - Why Plasma | Section label, two comparison callouts |
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
| `Plasma Nitriding Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Plasma Nitriding Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Plasma Nitriding Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Plasma Nitriding Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Plasma Nitriding Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Plasma Nitriding Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Plasma Nitriding cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#596--#603) zoom into each stage individually. The plasma vs. gas nitriding comparison answers the most common question: "why choose plasma over gas?" The answer is compound layer control -- plasma is the only nitriding method that can eliminate the white layer entirely, and it can treat stainless steel by sputtering through the passive film.

The visible purple/violet plasma glow is iconic for this process -- consider using a subtle violet tint or gradient accent somewhere in the hero zone as a visual signature.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #595 -- Construction Workup v1.0*
*2026-04-26*
