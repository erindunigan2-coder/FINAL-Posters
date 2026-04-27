---
Project: Plating Posters Inc
Poster Number: 489
Title: "HVOF -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF)"
Technical Source: Industry-standard high velocity oxy-fuel (HVOF) process. Covers complete 10-stage sequence from cleaning through final inspection. Supersonic combustion jet, 600-900 m/s particle velocity, <1% porosity coatings. Values are typical ranges per ASM Handbook Vol 5A and ITSA references.
Process Scope: HVOF thermal spray -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - ProcessFlow
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #489 -- Construction Workup
## HVOF -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for TS-02: High Velocity Oxy-Fuel (HVOF). Same U-flow architecture as the APS Process Flow (#479), but the content, comparisons, and parameters are all HVOF-specific. HVOF is the hard chrome killer -- the poster must convey that this process produces the densest, hardest thermal spray coatings available, at supersonic particle velocities. The comparison callout flips: here we compare HVOF vs. Hard Chrome (the transition story) rather than APS vs. HVOF.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (HVOF vs. Hard Chrome -- why the industry is switching), and a troubleshooting quick-hit strip. Dense but scannable -- the booth operator's wall reference for the entire HVOF process.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box is color-coded by stage type. Arrows connect boxes sequentially. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 10-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"HVOF vs. Hard Chrome" comparison callout (Block E):** Two side-by-side callout boxes comparing HVOF WC-Co vs. hard chrome plating. The transition story.

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
| Amber | `#E8A020` | Activation & post-treatment stages, warning headers |
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
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 4 -- HVOF vs. HARD CHROME COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: HVOF vs. Hard Chrome side-by-side callout

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

> HVOF

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 10 Stages from Cleaning to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> High Velocity Oxy-Fuel -- supersonic combustion jet (Mach 1.5-3.0), 600-900 m/s particle velocity, <1% porosity. The hard chrome replacement.

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

**BLOCK B -- Ten-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Two rows of five boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Grit Blast | Box 2 | 5.0" | `#E8A020` (Amber) | Surface Prep |
| 3. Mask & Fixture | Box 3 | 9.5" | `#E8A020` (Amber) | Preparation |
| 4. Equipment Setup | Box 4 | 14.0" | `#3A4055` (Slate) | Setup |
| 5. Parameter Set | Box 5 | 18.5" | `#3A4055` (Slate) | Setup |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 20.6", Y: 8.3" (bottom center Box 5)
- To: X: 20.6", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Preheat | Box 6 | 18.5" | `#E8A020` (Amber) | Pre-Spray |
| 7. Spray Application | Box 7 | 14.0" | `#27AE60` (Emerald) | Coating |
| 8. Cool & Inspect | Box 8 | 9.5" | `#2EC4B6` (Teal) | Post-Spray |
| 9. Post-Treatment | Box 9 | 5.0" | `#E8A020` (Amber) | Finishing |
| 10. Final QA | Box 10 | 0.5" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Clean`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Solvent degrease or alk wash
50-70 degC, pH 10-12, 5-15 min
Water-break-free (ASTM F22)
```

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `Surface cleanliness is even more critical for HVOF -- dense coatings trap interface contaminants`

*Box 2 -- Grit Blast:*
- Badge: `STAGE 2`, fill `#E8A020`
- Name: `Grit Blast`
- Parameters: `White Al2O3, 36-60 mesh` / `40-60 PSI` / `Ra 3-6 um (125-250 uin)` / `SSPC-SP 5 or SP 10`
- Check: `Profile need not be aggressive -- HVOF velocity provides excellent interlocking`

*Box 3 -- Mask & Fixture:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Mask & Fixture`
- Parameters: `Metal masks (SS, Cu) preferred` / `Silicone tape for non-critical areas` / `Lathe fixture for cylinders` / `Surface speed 0.5-2.0 m/s`
- Check: `HVOF generates more localized heat -- masking sees higher thermal load`

*Box 4 -- Equipment Setup:*
- Badge: `STAGE 4`, fill `#3A4055`
- Name: `Equipment Setup`
- Parameters: `Gas-fuel or liquid-fuel system` / `Combustion chamber + de Laval nozzle` / `Water cooling 15-25 L/min` / `6-axis robot`
- Check: `Verify O2 fittings are oil-free -- O2 + grease = fire`

*Box 5 -- Parameter Set:*
- Badge: `STAGE 5`, fill `#3A4055`
- Name: `Parameter Setup`
- Parameters: `Standoff 150-400 mm` / `Traverse 300-1000 mm/s` / `Feed rate 30-100 g/min` / `Combustion pressure 60-150 PSI`
- Check: `Gas-fuel vs. liquid-fuel parameters differ significantly -- use correct recipe`

*Box 6 -- Preheat:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Preheat Substrate`
- Parameters: `HVOF gun, no powder` / `Target: 60-100 degC` / `Less preheat needed than APS` / `High KE bonding compensates`
- Check: `Monitor with IR pyrometer`

*Box 7 -- Spray Application:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Spray Application`
- Parameters: `15-30 um per pass (WC-Co)` / `Total: 100-500 um typical` / `Chrome replacement: 200-400 um` / `DE: 50-70%`
- Check: `Keep substrate < 150 degC -- compressed air cooling between passes`

*Box 8 -- Cool & Inspect:*
- Badge: `STAGE 8`, fill `#2EC4B6`
- Name: `Cool & In-Process Check`
- Parameters: `Cool to ambient` / `Thickness check (eddy current)` / `Visual: no spalling or blisters`
- Check: `Compare deposition rate to qualification data`

*Box 9 -- Post-Treatment:*
- Badge: `STAGE 9`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Grind: diamond or CBN wheels` / `Wet grinding mandatory` / `Finish Ra 0.1-0.4 um` / `Sealing generally NOT required`
- Check: `Infeed 5-15 um/pass -- light cuts to avoid pullout`

*Box 10 -- Final QA:*
- Badge: `STAGE 10`, fill `#27AE60`
- Name: `Final Inspection & QA`
- Parameters: `Bond: ASTM C633 (> 70 MPa)` / `Porosity: ASTM E2109 (< 1%)` / `Hardness: ASTM E384 (1100-1400 HV)` / `Visual + 10x loupe`
- Check: `AMS 2448 requires destructive test coupons alongside production`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Inspection` |
| `#E8A020` (Amber) | `Preparation & Post-Treatment` |
| `#27AE60` (Emerald) | `Spray Application & QA` |
| `#3A4055` (Slate) | `Equipment & Parameter Setup` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 10-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Key Spec (5.5") | Temperature (3.0") | Time/Speed (3.0") | Critical Control (8.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Stage | Key Spec | Temp | Time/Speed | Critical Control |
|---|---|---|---|---|
| 1. Clean | Alk wash pH 10-12; DI rinse (aero) | 50-70 degC | 5-15 min | Water-break-free test |
| 2. Grit Blast | Al2O3 36-60 mesh, 40-60 PSI | Ambient | -- | Ra 3-6 um; SSPC-SP 5 |
| 3. Mask & Fixture | Metal masks; lathe fixture | -- | 0.5-2.0 m/s | No shadow on spray path |
| 4. Equip Setup | Gas-fuel or liquid-fuel HVOF | -- | -- | O2 fittings oil-free |
| 5. Parameters | Standoff 150-400 mm | -- | 300-1000 mm/s | Match recipe to fuel type |
| 6. Preheat | HVOF gun, no powder | 60-100 degC | -- | IR pyrometer verification |
| 7. Spray | 15-30 um/pass; DE 50-70% | Monitor sub | Per robot prog | Substrate < 150 degC |
| 8. Cool/Check | Ambient cool-down | Ambient | -- | Compare to qual data |
| 9. Post-Treat | Grind (diamond/CBN); seal if spec'd | Varies | 5-15 um/pass | Wet grinding mandatory |
| 10. Final QA | ASTM C633, E2109, E384; AMS 2448 | -- | -- | Destructive test coupons |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- HVOF vs. Hard Chrome Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE TRANSITION -- HVOF VS. HARD CHROME

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- HVOF WC-12Co:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `HVOF WC-12Co` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Hard Chrome Replacement` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Hardness | 1100-1400 HV300 |
| Porosity | < 1% (typically < 0.5%) |
| Bond strength | > 70 MPa (exceeds epoxy) |
| Wear rate (ASTM G65) | 1-5 x 10^-7 mm3/Nm |
| Fatigue life impact | Neutral to beneficial (compressive stress) |
| Oxide content | < 0.5% |
| Max service temp | 500 degC |
| Cr(VI) exposure | ZERO |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 12 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `HVOF WC-Co matches or exceeds hard chrome in every measurable property` -- Inter Medium, 12 pt, `#E8A020`

**Right -- Hard Chrome (Reference):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `HARD CHROME PLATING` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `The Incumbent (Under Regulatory Pressure)` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Hardness | 800-1000 HV |
| Porosity | < 1% (micro-cracked network) |
| Bond strength | 40-80 MPa |
| Wear rate (ASTM G65) | 5-15 x 10^-7 mm3/Nm |
| Fatigue life impact | Detrimental (tensile stress; H2 embrittlement) |
| Oxide content | N/A (metallic) |
| Max service temp | 400 degC (begins softening) |
| Cr(VI) exposure | YES -- NESHAP + REACH regulated |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `EPA NESHAP and EU REACH are driving the transition away from hexavalent chromium` -- Inter Medium, 12 pt, `#E05C5C`

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
| 1 | 0.5" | DELAMINATION | Poor surface prep or residual chrome from strip | Verify SP-5; confirm no residual chrome |
| 2 | 6.33" | LOW HARDNESS | Decarburization (WC decomposing) | Reduce flame temp; shorten dwell time |
| 3 | 12.16" | SUBSTRATE OVERHEATING | Insufficient cooling between passes | Add compressed air jets; increase traverse |
| 4 | 18.0" | POROSITY > 1% | Standoff too far or powder too coarse | Reduce standoff; verify powder 5-45 um |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for high velocity oxy-fuel (HVOF) thermal spray. Specific equipment, powder, and process limits vary by application and OEM. Consult your thermal spray equipment supplier and applicable specifications (AMS 2447, AMS 2448, ASTM, MIL-STD) for application-specific guidance. Source: ASM Handbook Vol 5A; ITSA references.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> HVOF -- Process Flow

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
| Zone 2 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 10-row table |
| Zone 4 - HVOF vs Hard Chrome | Section label, two comparison callouts |
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
| `HVOF Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `HVOF Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `HVOF Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `HVOF Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `HVOF Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `HVOF Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire HVOF cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 9 posters (#490--#498) zoom into each stage individually. The HVOF vs. Hard Chrome comparison is THE story of this cluster -- it is the reason HVOF exists in its current market dominance. Every property favors HVOF except one: hard chrome is cheaper and simpler for non-critical applications. But regulatory pressure (NESHAP, REACH) is making that cost advantage disappear.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #489 -- Construction Workup v1.0*
*2026-04-26*
