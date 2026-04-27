---
Project: Plating Posters Inc
Poster Number: 143
Title: "Tin-Lead Plating -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-15 technical reference (tin-lead / solder plating)"
Technical Source: Industry-standard tin-lead (solder) plating process. Covers the complete 8-stage sequence from cleaning through post-treatment (reflow). Values are typical ranges for MSA-based tin-lead baths -- the dominant chemistry replacing legacy fluoborate systems. 60Sn/40Pb and 90Sn/10Pb compositions.
Process Scope: Tin-lead plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - TinLeadPlating
  - SolderPlating
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEP15
---

# Poster #143 -- Construction Workup
## Tin-Lead Plating -- Process Flow

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-15: Tin-Lead (Solder) Plating. It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Tin-lead plating is the original solder finish for electronics -- 60/40 solder on every PCB before RoHS. The process is declining in commercial electronics but remains essential for military, aerospace, and high-reliability applications under RoHS exemptions. The poster covers MSA-based chemistry (the modern standard) with legacy fluoborate referenced for comparison, and calls out the regulatory reality front and center: lead is a restricted substance, and the waste stream is hazardous.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (MSA vs. fluoborate), a RoHS/regulatory awareness strip, and a troubleshooting quick-hit strip. The operator sees the full line. The engineer sees where alloy control begins.

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

3. **"MSA vs. Fluoborate" comparison callout (Block E):** Two side-by-side callout boxes comparing modern MSA tin-lead vs. legacy fluoborate tin-lead. The defining chemistry decision for any tin-lead shop.

4. **RoHS / Regulatory awareness strip (Block F):** A prominent warning panel covering lead restrictions, exemptions, and waste obligations.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

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
| Coral | `#E05C5C` | Problems, defects, contamination callouts, RoHS warnings |
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

ZONE 4 -- MSA VS. FLUOBORATE COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: MSA vs. fluoborate side-by-side callout

ZONE 5 -- RoHS / REGULATORY AWARENESS (28.5"--32.5" / ~4.0" tall)
  Block F: Lead restriction warning + exemptions + waste stream

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

> TIN-LEAD PLATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Reflow

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Solder plating -- the original solderable finish. Lead is restricted, but mil/aero still needs it. Know the process. Respect the lead.

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
| 5. Tin-Lead Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Hot Water Rinse / Dry | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Reflow / Inspect | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

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
Mild alkaline, 3--6 oz/gal
120--150 F (49--66 C)
3--5 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, fingerprints, shop soil from electronics substrates`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Flowing or cascade` / `DI recommended`
- Purpose: `Remove alkaline cleaner residue`
- Check: `Prevents alkaline drag-in to acid activation`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `5--10% MSA or fluoboric acid` / `Ambient, 15--30 sec`
- Purpose: `Remove surface oxides, expose clean metal for plating`
- Check: `Substrate-dependent -- copper/brass standard`

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `Flowing or cascade` / `DI recommended`
- Purpose: `Remove activation acid before plating`
- Check: `MSA drag-in is compatible with MSA bath but still dilutes`

*Box 5 -- Tin-Lead Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Tin-Lead Plate` / Subtitle: `Main Tank`
- Parameters: `Sn2+: 35--55 g/L (60/40)` / `Pb2+: 15--25 g/L (60/40)` / `MSA: 100--200 g/L` / `75--85 F (24--29 C)` / `15--25 ASF (rack)`
- Purpose: `Co-deposit tin-lead solder alloy onto substrate`
- Check: `Alloy composition control -- verify by XRF` (Coral `#E05C5C`)

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `Double counterflow` / `DI recommended`
- Purpose: `Remove acid drag-out, prepare for reflow or dry`
- Check: `LEAD WASTE: segregate rinse water -- regulated discharge` (Coral `#E05C5C`)

*Box 7 -- Hot Water Rinse / Dry:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Hot Water Rinse / Dry`
- Parameters: `Hot DI water: 140--160 F` / `Or forced warm air dry`
- Purpose: `Remove rinse water, accelerate drying, prevent water spots`
- Check: `Rapid dry prevents oxidation of fresh solder surface`

*Box 8 -- Reflow / Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Reflow / Inspect`
- Parameters: `Reflow: 400--450 F (204--232 C)` / `IR, hot air, or oven` / `XRF alloy check`
- Purpose: `Fuse solder deposit -- bright, dense, fully solderable surface`
- Check: `Reflow is REQUIRED for solder finish -- not optional` (Coral `#E05C5C`)

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Post-Treatment & Activation` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
| `#E05C5C` (Coral) | `Caution / Regulatory` |

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
| 1. Alk Clean | Mild alkaline 3--6 oz/gal | 120--150 F | 3--5 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | No alkaline carry-over |
| 3. Activation | MSA 5--10% or HBF4 5--10% | Ambient | 15--30 sec | -- | Substrate-dependent |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | No acid carry-over |
| 5. Sn-Pb Plate | Sn2+ 35--55, Pb2+ 15--25, MSA 100--200 g/L | 75--85 F | Per spec | 15--25 ASF (rack) | Alloy ratio by XRF |
| 6. Rinse | DI water (double counterflow) | Ambient | 30--60 sec | -- | Lead waste segregation |
| 7. Hot Rinse/Dry | Hot DI water | 140--160 F | 1--3 min | -- | Spot-free surface |
| 8. Reflow/Inspect | -- | 400--450 F (reflow) | 2--5 sec | -- | Alloy comp + solderability |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- MSA vs. Fluoborate Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> MSA VS. FLUOBORATE -- WHICH SOLDER BATH?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- MSA Tin-Lead:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `MSA TIN-LEAD` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Modern Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Tin source | Stannous methanesulfonate |
| Lead source | Lead methanesulfonate |
| Acid | Methanesulfonic acid (MSA) |
| Sn2+ range | 35--55 g/L (60/40 alloy) |
| Pb2+ range | 15--25 g/L (60/40 alloy) |
| Temp | 60--100 F (16--38 C) |
| CD (rack) | 10--40 ASF |
| Cathode eff. | 90--98% |
| Waste treatment | MSA is biodegradable |
| Best for | Modern mil/aero, reel-to-reel |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `MSA is the clear replacement -- biodegradable acid, better performance, no fluoride waste` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Fluoborate Tin-Lead (Legacy):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `FLUOBORATE TIN-LEAD` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Legacy -- Being Phased Out` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Tin source | Stannous fluoborate |
| Lead source | Lead fluoborate |
| Acid | Fluoboric acid (HBF4) |
| SnBF4 | 100--200 g/L |
| PbBF4 | 25--75 g/L |
| Boric acid | 20--30 g/L |
| Grain refiner | Peptone or gelatin, 2--5 g/L |
| Waste treatment | Fluoride treatment required |
| Best for | Legacy installations only |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Being phased out due to fluoride wastewater issues -- convert to MSA when possible` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 5 -- RoHS / Regulatory Awareness

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#E05C5C`

> LEAD IS RESTRICTED -- KNOW YOUR OBLIGATIONS

---

**BLOCK F -- Regulatory Awareness Strip**

Y: 29.4" to 32.3". Three cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 7.33", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Header | Content |
|---|---|---|---|
| 1 | 0.5" | RoHS RESTRICTION | EU RoHS limits Pb to <0.1% in electronics. Tin-lead solder plate is prohibited for commercial electronics. Exemptions exist for military, aerospace, and high-reliability applications. |
| 2 | 8.16" | OSHA LEAD EXPOSURE | PEL: 50 ug/m3 (TWA). Action level: 30 ug/m3. Blood lead monitoring required. Hygiene program per 29 CFR 1910.1025. No eating/drinking in plating area. |
| 3 | 15.83" | HAZARDOUS WASTE | Lead wastewater: 0.43 mg/L daily max (40 CFR 433). Lead-bearing sludge may be F006 hazardous waste. Segregate all lead-containing rinse water. |

Interior per card:
- Header: Barlow SemiBold, 16 pt, `#E05C5C`
- Content: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for MSA-based tin-lead (solder) plating. Lead is a restricted substance under EU RoHS and a regulated occupational hazard under OSHA. Specific formulations, concentrations, and regulatory requirements vary by jurisdiction. Consult your process supplier and environmental compliance officer.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Tin-Lead Plating -- Process Flow

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
| Zone 4 - MSA vs Fluoborate | Section label, two comparison callouts |
| Zone 5 - Regulatory | Section label, three regulatory cards |
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
| `Tin-Lead Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Tin-Lead Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Tin-Lead Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Tin-Lead Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Tin-Lead Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Tin-Lead Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Tin-Lead cluster. The U-flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#144--#150) zoom into each stage individually. The MSA vs. fluoborate comparison answers the chemistry question every tin-lead shop faces -- MSA is the future and fluoborate is legacy. The regulatory strip in Zone 5 is unique to this cluster and non-negotiable: lead is a serious hazard and a regulatory burden. No other cluster in the series needs a full regulatory awareness zone in the process flow poster. This poster sets that tone for the entire EP-15 cluster.

---

*Alaina -- Plating Posters Inc*
*Poster #143 -- Construction Workup v1.0*
*2026-04-26*
