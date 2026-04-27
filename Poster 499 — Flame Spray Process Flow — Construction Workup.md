---
Project: Plating Posters Inc
Poster Number: 499
Title: "Flame Spray -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Technical Source: Industry-standard oxy-fuel flame spray process (wire and powder variants). Covers the complete 8-stage sequence from cleaning through inspection. Values are typical ranges from ASM Handbook Vol 5A, Pawlowski, and AWS C2.18.
Process Scope: Flame spray (wire and powder) -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - ProcessFlow
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #499 -- Construction Workup
## Flame Spray -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for TS-03: Flame Spray (Wire and Powder). It shows the complete 8-stage process at a glance in a U-flow diagram. Flame spray is the oldest and most accessible thermal spray technology -- many shops already own oxy-acetylene equipment. This poster is the "map" that the other 9 posters (#500--#508) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a wire-vs-powder comparison callout, and a troubleshooting quick-hit strip. The foreman's wall reference for the entire flame spray line.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box is color-coded by stage type. Straightforward geometry.
2. **Parameter summary table (Block D):** Compact 8-row table (one row per stage) with key parameters.
3. **"Wire vs. Powder" comparison callout (Block E):** Two side-by-side callout boxes comparing the two flame spray feedstock types.
4. **Troubleshooting quick-hit strip (Block F):** Horizontal strip of 4 common problems with one-line fixes.
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
| Amber | `#E8A020` | Post-treatment stages, warning headers, flame-related accents |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Spray application stage, optimal reference |
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
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- WIRE VS. POWDER COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Wire vs. Powder side-by-side callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> FLAME SPRAY

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The oldest and most accessible thermal spray method. Oxy-fuel flame melts wire or powder -- no plasma, no arc, just combustion and compressed air.

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
| 1. Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Grit Blast | Box 2 | 6.0" | `#2EC4B6` (Teal) | Surface Prep |
| 3. Mask & Fixture | Box 3 | 11.5" | `#E8A020` (Amber) | Setup |
| 4. Equipment Setup | Box 4 | 17.0" | `#E8A020` (Amber) | Setup |

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
| 5. Set Parameters | Box 5 | 17.0" | `#E8A020` (Amber) | Setup |
| 6. Spray | Box 6 | 11.5" | `#27AE60` (Emerald) | Application |
| 7. Post-Treat | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Inspect | Box 8 | 0.5" | `#2EC4B6` (Teal) | QA |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Solvent wipe or alk wash
50--70 degC (122--158 F)
Water-break-free test
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, greases, machining fluids`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Clean BEFORE masking -- never mask contaminated surfaces`

*Box 2 -- Grit Blast:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Grit Blast`
- Parameters: `Al2O3 or steel grit 16--36 mesh` / `60--100 PSI` / `Ra: 4--12 um`
- Purpose: `Create anchor profile for mechanical interlock`
- Check: `Spray within 4 hours of blast`

*Box 3 -- Mask & Fixture:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Mask & Fixture`
- Parameters: `Hi-temp tape, metal shields` / `Silicone plugs for holes` / `Turntable for cylinders`
- Purpose: `Protect non-spray surfaces; position workpiece`
- Check: `Simpler masking than plasma/HVOF -- lower overspray penetration`

*Box 4 -- Equipment Setup:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Equipment Setup`
- Parameters: `O2: 15--40 PSI` / `C2H2: 10--15 PSI (NEVER >15)` / `Air: 40--80 PSI`
- Purpose: `Configure gun, gas pressures, wire/powder feed`
- Check: `CAUTION: Acetylene unstable above 15 PSI` (Coral `#E05C5C`)

*Box 5 -- Set Parameters:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Set Parameters`
- Parameters: `Standoff: 150--300 mm` / `Spray angle: 60--90 deg` / `Feed: 1--8 m/min (wire)`
- Purpose: `Dial in spray pattern and deposition rate`
- Check: `Run test coupon before production spray`

*Box 6 -- Spray Application:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Spray Application`
- Parameters: `Preheat substrate 80--120 degC` / `25--75 um per pass` / `Total: 100--2000 um`
- Purpose: `Build coating to specified thickness`
- Check: `Multiple passes -- do not attempt full thickness in one pass`

*Box 7 -- Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Seal: epoxy or wax` / `Fuse: 1000--1100 degC (NiCrBSi)` / `Machine: grind or turn`
- Purpose: `Seal porosity, fuse self-fluxing alloys, finish to dimension`
- Check: `CRITICAL: Fusing exceeds many substrate temp limits` (Coral `#E05C5C`)

*Box 8 -- Inspect:*
- Badge: `STAGE 8`, fill `#2EC4B6`
- Name: `Inspect & QA`
- Parameters: `Bond: ASTM C633 >10 MPa` / `Porosity: ASTM E2109` / `Thickness: mag gauge`
- Purpose: `Verify coating meets specification`
- Check: `Visual first -- uniform coverage, no bare spots or blisters`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & QA` |
| `#E8A020` (Amber) | `Setup & Post-Treatment` |
| `#27AE60` (Emerald) | `Spray Application` |
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
- Stage (3.0") | Method (4.5") | Key Values (5.0") | Dep Rate (3.0") | Dep Efficiency (3.0") | Key Control (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Method | Key Values | Dep Rate | Dep Eff | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Solvent + alk wash | 50--70 degC, 5--15 min | -- | -- | Water-break-free |
| 2. Grit Blast | Al2O3 / steel grit | 60--100 PSI, Ra 4--12 um | -- | -- | SSPC-SP 5 or SP 10 |
| 3. Mask & Fixture | Tape, shields, plugs | Hi-temp rated | -- | -- | Line-of-sight access |
| 4. Equip Setup | Oxy-fuel + air | O2 15--40, C2H2 10--15 PSI | -- | -- | Flashback arrestors |
| 5. Parameters | Standoff + angle | 150--300 mm, 60--90 deg | -- | -- | Test coupon first |
| 6. Spray | Wire or powder | 80--200 m/s (wire) | 2--8 kg/hr (W) | 50--70% (W) | Multiple passes |
| 7. Post-Treat | Seal / fuse / machine | Fuse 1000--1100 degC | -- | -- | Substrate temp limit |
| 8. Inspect | ASTM C633 / E2109 | Bond >10 MPa (as-sprayed) | -- | -- | Visual + instruments |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Wire vs. Powder Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WIRE VS. POWDER -- TWO FEEDSTOCK PATHS

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Wire Flame Spray:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `WIRE FLAME SPRAY` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Simpler, Cheaper, Higher Output` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Feedstock | Wire 1.6--4.8 mm diameter |
| Common materials | Zn, Al, stainless, carbon steel, bronze, Monel, Mo |
| Particle velocity | 80--200 m/s |
| Deposition rate | 2--8 kg/hr |
| Deposition efficiency | 50--70% |
| Atomization | Compressed air blast |
| Typical use | Corrosion protection (Zn/Al on steel) |
| Complexity | Low -- many shops already own oxy-acet equipment |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Wire is the workhorse -- higher feed rates, lower cost, and simpler operation` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Powder Flame Spray:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `POWDER FLAME SPRAY` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Broader Material Selection` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Feedstock | Powder 40--120 microns |
| Common materials | NiCrBSi, stellite, WC blends, ceramics, bronze |
| Particle velocity | 40--100 m/s |
| Deposition rate | 1--4 kg/hr |
| Deposition efficiency | 30--50% |
| Feed method | Gravity hopper or carrier gas |
| Typical use | Self-fluxing alloys, wear coatings, repair buildups |
| Unique capability | NiCrBSi can be fused to near-zero porosity |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Powder unlocks self-fluxing alloys -- fuse after spray for metallurgical bond and <1% porosity` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | POOR ADHESION | Inadequate blast profile or contamination | Re-blast to Ra 4--12 um; verify clean surface |
| 2 | 6.33" | HIGH POROSITY | Standoff too far or particle velocity too low | Reduce standoff; check gas pressures |
| 3 | 12.16" | SPITTING (WIRE) | Wire feed speed mismatch or moisture in air | Adjust feed rate; install air dryer |
| 4 | 18.0" | COATING DELAMINATION | Substrate overheated or oxide layer at interface | Monitor temp <150 degC; spray within 4 hr of blast |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for oxy-fuel flame spray. Specific equipment settings, coating specifications, and process limits vary by application and feedstock material. Consult your equipment OEM and coating specification for application-specific guidance. Source: ASM Handbook Vol 5A; AWS C2.18; general industry knowledge.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Flame Spray -- Process Flow

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
| Zone 4 - Wire vs Powder | Section label, two comparison callouts |
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
| `Flame Spray Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Spray Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Spray Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Flame Spray Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Spray Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Spray Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Flame Spray cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 9 posters (#500--#508) zoom into each stage individually. The wire vs. powder comparison answers the most common question in flame spray: "which feedstock should I use?" Wire wins for corrosion protection and simplicity; powder wins for self-fluxing alloys and exotic materials.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #499 -- Construction Workup v1.0*
*2026-04-26*
