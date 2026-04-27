---
Project: Plating Posters Inc
Poster Number: 649
Title: "Powder Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1"
Technical Source: Industry-standard thermoset powder coating process. Covers the complete 9-stage sequence from racking through inspection. Values are typical ranges for electrostatic spray application of thermoset powder on steel and aluminum substrates.
Process Scope: Powder coating -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - ProcessFlow
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #649 -- Construction Workup
## Powder Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Powder Coating. It shows the complete 9-stage process sequence at a glance -- every stage visible in one U-flow diagram. A line operator sees the full sequence, a supervisor checks parameters, a quality engineer spots where problems originate. This poster is the "map" that the other 8 posters (#650--#657) zoom into.

The sustainability story is front and center: zero VOC, 95-98% material utilization with reclaim. Powder coating is the cleanest high-performance finish in industrial coating -- this poster should make that obvious at first glance.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Each box is color-coded by stage type. Arrows connect boxes sequentially.

2. **Parameter summary table (Block D):** A compact 9-row table (one row per stage) with key parameters.

3. **"Zero VOC" sustainability callout (Block E):** Side-by-side comparison of powder vs. liquid paint on VOC, transfer efficiency, and waste.

4. **Chemistry family quick reference (Block F):** Horizontal strip showing 6 powder chemistries with UV durability rating.

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
| Amber | `#E8A020` | Application & cure stages, key numbers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Powder application stage, sustainability callouts |
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
- 27.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Nine-stage U-flow diagram (top row 5 + bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 9-row parameter table (one row per stage)

ZONE 4 -- ZERO VOC / POWDER vs. LIQUID (22.0"--27.5" / ~5.5" tall)
  Block E: Side-by-side sustainability comparison

ZONE 5 -- CHEMISTRY FAMILIES + TROUBLESHOOTING (27.5"--32.5" / ~5.0" tall)
  Block F: 6-chemistry quick reference strip
  Block G: 4-problem troubleshooting strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> POWDER COATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 9 Stages from Racking to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Zero VOC. 95%+ material utilization. The cleanest high-performance finish in industrial coating. Hang this poster at the head of your powder line.

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

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row of five boxes, bottom row of four boxes, U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.3"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.1") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Rack / Load | Box 1 | 0.5" | `#3A4055` (Slate) | Handling |
| 2. Pretreatment Wash | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Dry-Off Oven | Box 3 | 9.7" | `#E8A020` (Amber) | Thermal |
| 4. Cool Down | Box 4 | 14.3" | `#2EC4B6` (Teal) | Conditioning |
| 5. Powder Application | Box 5 | 18.9" | `#27AE60` (Emerald) | Application |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.0")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.1" (bottom center Box 5)
- To: X: 21.0", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 13.8") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Cure Oven | Box 6 | 18.9" | `#E8A020` (Amber) | Thermal |
| 7. Cool Down | Box 7 | 14.3" | `#2EC4B6` (Teal) | Conditioning |
| 8. Inspect | Box 8 | 9.7" | `#E8A020` (Amber) | QC |
| 9. Unrack / Pack / Ship | Box 9 | 0.5" | `#3A4055` (Slate) | Handling |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Rack / Load:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#3A4055`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Rack / Load`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Grounded hooks / fixtures
Faraday-aware orientation
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Mount parts on grounded racks for electrostatic charging`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Ground path continuity -- no coated hooks`

*Box 2 -- Pretreatment Wash:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Pretreatment Wash`
- Parameters: `5-stage spray tunnel` / `Clean -> Rinse -> Convert -> Rinse -> Seal`
- Purpose: `Remove soils, apply conversion coating for adhesion`
- Check: `Water-break-free after clean (ASTM F22)`

*Box 3 -- Dry-Off Oven:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Dry-Off Oven`
- Parameters: `250--300 F (121--149 C)` / `10--15 min at metal temp`
- Purpose: `Remove all moisture -- blistering source if incomplete`
- Check: `CRITICAL: Parts must be bone dry` (Coral `#E05C5C`)

*Box 4 -- Cool Down:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Cool Down`
- Parameters: `Cool to < 90 F (32 C)` / `Ambient air or forced`
- Purpose: `Hot parts attract powder unevenly`
- Check: `Exception: hot flocking for thermoplastic powders`

*Box 5 -- Powder Application:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Powder Application` / Subtitle: `Electrostatic Spray`
- Parameters: `60--100 kV corona` / `6--12 in gun distance` / `Target: 2--4 mils DFT`
- Purpose: `Electrostatically deposit powder onto grounded parts`
- Check: `Faraday cage effect: recesses need manual touch-up`

*Box 6 -- Cure Oven:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Cure Oven`
- Parameters: `350--400 F (177--204 C)` / `10--20 min at METAL temp` / `Convection or IR+convection`
- Purpose: `Melt, flow, cross-link -- irreversible thermoset cure`
- Check: `METAL temp, not oven air temp -- profile with datalogger` (Coral `#E05C5C`)

*Box 7 -- Cool Down:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Cool Down`
- Parameters: `Cool to < 120 F (49 C)` / `Before handling`
- Purpose: `Prevent fingerprint embedding in warm film`
- Check: `Clean nitrile gloves -- silicone = fish-eye on next batch`

*Box 8 -- Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Inspect`
- Parameters: `DFT: magnetic or eddy current` / `Adhesion: cross-cut D3359` / `Cure: MEK rub D4752`
- Purpose: `Verify thickness, adhesion, and full cure`
- Check: `50+ MEK double rubs = fully cured`

*Box 9 -- Unrack / Pack / Ship:*
- Badge: `STAGE 9`, fill `#3A4055`
- Name: `Unrack / Pack / Ship`
- Parameters: `Foam dividers` / `Kraft paper interleaving`
- Purpose: `Protect finish during transport`
- Check: `No surface-to-surface contact between coated parts`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#3A4055` (Slate) | `Handling` |
| `#2EC4B6` (Teal) | `Cleaning / Conditioning` |
| `#E8A020` (Amber) | `Thermal / QC` |
| `#27AE60` (Emerald) | `Application` |
| `#E05C5C` (Coral) | `Caution / Safety` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Process (4.5") | Temperature (3.0") | Time (2.5") | Key Spec (4.5") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Process | Temp | Time | Key Spec | Key Control |
|---|---|---|---|---|---|
| 1. Rack/Load | Ground parts on hooks | Ambient | -- | Ground path < 1 ohm | Hook cleanliness |
| 2. Pretreatment | 5-stage spray wash | 120--150 F | 60--120 sec/stage | Iron phos 25--75 mg/ft2 | Water-break-free |
| 3. Dry-Off | Convection oven | 250--300 F | 10--15 min at metal | 0% moisture | No standing water |
| 4. Cool | Ambient or forced | < 90 F target | Until cool | -- | Hot = uneven powder |
| 5. Application | Electrostatic spray | Ambient | Per line speed | 2--4 mils DFT | Faraday cage areas |
| 6. Cure | Convection/IR oven | 350--400 F | 10--20 min at metal | Full cross-link | Oven profile datalogger |
| 7. Cool | Ambient or forced | < 120 F | Until cool | -- | No handling warm |
| 8. Inspect | DFT + adhesion + MEK | Ambient | -- | 4B--5B adhesion | 50+ MEK double rubs |
| 9. Unrack/Ship | Pack with dividers | Ambient | -- | -- | No surface contact |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Zero VOC / Powder vs. Liquid

**Dimensions:** Y: 22.0" to 27.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY POWDER? -- THE ZERO-VOC ADVANTAGE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 27.3".

**Left -- Powder Coating:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 4.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `POWDER COATING` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Clean Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| VOC Content | ZERO -- no solvents |
| Transfer Efficiency | 60--70% first-pass |
| Total Material Utilization | 95--98% with reclaim |
| Waste Stream | Minimal -- overspray reclaimed |
| Typical DFT | 2--4 mils (single coat) |
| Cure | 350--400 F, 10--20 min |
| Durability | Excellent (polyester outdoor) |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `No solvent. No overspray waste. No VOC permits. The sustainability story writes itself.` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Liquid Spray Paint:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 4.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `LIQUID SPRAY PAINT` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Flexible Alternative` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| VOC Content | 2.0--4.2 lb/gal (regulated) |
| Transfer Efficiency | 25--45% conventional |
| Total Material Utilization | 50--75% typical |
| Waste Stream | Solvent waste, booth filters |
| Typical DFT | 1--3 mils (multi-coat) |
| Cure | Air dry to 350 F bake |
| Durability | Chemistry-dependent |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Greater color flexibility and field-repairability -- but at a VOC and waste cost` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 5 -- Chemistry Families + Troubleshooting

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> POWDER CHEMISTRY FAMILIES

---

**BLOCK F -- Six-Chemistry Strip (Y: 28.3" to 29.8")**

Six cards in a single row. Gap: 0.2".

Each card: Rounded rect, W: 3.7", H: 1.3", fill `#1E2435`, radius 4, top accent 3 pt.

| Card | X | Chemistry | Accent | UV Rating | Typical Use |
|---|---|---|---|---|---|
| 1 | 0.5" | EPOXY | `#E05C5C` | Poor (interior only) | Pipe, rebar, electrical |
| 2 | 4.4" | HYBRID | `#E8A020` | Moderate | Furniture, shelving |
| 3 | 8.3" | POLYESTER TGIC | `#27AE60` | Excellent | Architectural, outdoor |
| 4 | 12.2" | POLYESTER HAA | `#27AE60` | Excellent | TGIC-free alternative |
| 5 | 16.1" | URETHANE | `#2EC4B6` | Excellent | Auto wheels, high-appearance |
| 6 | 20.0" | ACRYLIC | `#2EC4B6` | Excellent | Auto clearcoat, high DOI |

Interior per card:
- Chemistry name: Barlow SemiBold, 13 pt, accent color
- UV: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 70%
- Use: Inter Regular, 11 pt, `#F0EDE8` at 60%

---

**Section label:**
- Centered. Y: 30.1". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK G -- Four Problem Cards (Y: 30.7" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 1.4", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ORANGE PEEL | Insufficient flow time or wrong particle size | Check cure schedule; verify powder D50 30--45 um |
| 2 | 6.33" | OUTGASSING / PINHOLES | Trapped gas in substrate (cast Al, galv.) | Pre-bake substrate at cure temp 10--20 min |
| 3 | 12.16" | POOR COVERAGE IN RECESSES | Faraday cage effect | Reduce voltage; use tribo gun; manual touch-up |
| 4 | 18.0" | ADHESION FAILURE | Contamination or poor pretreatment | Water-break test; check conversion coating weight |

Interior per card:
- Problem: Barlow SemiBold, 14 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for thermoset powder coating applied by electrostatic spray. Specific formulations, cure schedules, and process limits vary by powder supplier. Consult your powder manufacturer for application-specific guidance. Source: General industry knowledge; Powder Coating Institute references.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Powder Coating -- Process Flow

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
| Zone 4 - Why Powder | Section label, two comparison callouts |
| Zone 5 - Chemistry + Troubleshooting | Chemistry strip, four problem cards |
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
| `Powder Coating Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Powder Coating Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Powder Coating Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Powder Coating Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Powder Coating Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Powder Coating Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Powder Coating cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#650--#657) zoom into each stage individually. The sustainability comparison answers the most compelling question in industrial finishing: "why powder instead of liquid?" The answer is zero VOC, near-total material reclaim, and single-coat coverage at 2--4 mils -- a story that sells itself.

NFPA 654 combustible dust hazard is real and belongs on the Application poster (#655), not this overview. Keep this poster aspirational and process-oriented.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #649 -- Construction Workup v1.0*
*2026-04-26*
