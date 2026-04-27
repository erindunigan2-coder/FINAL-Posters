---
Project: Plating Posters Inc
Poster Number: 357
Title: "Acid Pickling (Carbon Steel) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-3)"
Technical Source: Industry-standard acid pickling of carbon steel. Covers the complete 7-stage sequence from alkaline clean through inspection. HCl and H2SO4 as primary acids. Values are typical ranges -- the dominant pickling chemistries for carbon steel in job shops and production plating lines.
Process Scope: Acid pickling of carbon steel -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - CarbonSteel
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT03
---

# Poster #357 -- Construction Workup
## Acid Pickling (Carbon Steel) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-3: Acid Pickling (Carbon Steel). It shows the complete 7-stage process from alkaline cleaning through post-pickle inspection in a U-flow diagram. The hero is the flow itself -- every stage visible at a glance. A compact HCl vs. H2SO4 comparison answers the first question any shop person asks. A hydrogen embrittlement decision strip provides the critical risk callout. This poster is the "map" for the remaining 6 posters (#358--#363).

Design philosophy: clean U-flow diagram as the hero, HCl vs. H2SO4 side-by-side comparison, hydrogen embrittlement risk table, and a troubleshooting quick-hit strip. Dense but scannable -- the foreman's wall reference for the entire pickling line.

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

2. **HCl vs. H2SO4 comparison (Block E):** Two side-by-side callout boxes. Established pattern from Poster #31.

3. **Hydrogen embrittlement risk table (Block F):** 4-row table keyed by hardness range. Coral accent for high-risk rows.

4. **Troubleshooting quick-hit strip (Block G):** A horizontal strip of 4 common problems with one-line fixes.

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
| Emerald | `#27AE60` | Optimal / success reference |
| Coral | `#E05C5C` | Problems, defects, safety warnings, H-embrittlement |
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
- 14.5" -- Zone 2/Zone 3 boundary
- 21.0" -- Zone 3/Zone 4 boundary
- 27.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Seven-stage U-flow diagram (top row 4, bottom row 3)
  Block C: Stage legend strip (color key)

ZONE 3 -- HCL VS. H2SO4 COMPARISON (14.5"--21.0" / ~6.5" tall)
  Block D: Section label
  Block E: HCl vs. H2SO4 side-by-side callout

ZONE 4 -- HYDROGEN EMBRITTLEMENT RISK (21.0"--27.5" / ~6.5" tall)
  Block F: H-embrittlement hardness/risk table

ZONE 5 -- TROUBLESHOOTING QUICK HITS (27.5"--32.5" / ~5.0" tall)
  Block G: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
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

> ACID PICKLING (CARBON STEEL)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 7 Stages from Clean to Inspect

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Strip the scale. Expose clean metal. Control hydrogen risk. The acid pickle line at a glance.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 14.5" (~11.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 13.0" (~9.2" tall). Top row of four boxes, bottom row of three boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.0"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 7.8") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Pickle | Box 3 | 11.5" | `#E8A020` (Amber) | Treatment |
| 4. Rinse | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~5.8")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 7.8" (bottom center Box 4)
- To: X: 19.5", Y: 9.0" (top center Box 5)

**Bottom Row (Y: 9.0" to 13.0") -- Stages 5-7, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Neutralize (Optional) | Box 5 | 17.0" | `#E8A020` (Amber) | Treatment |
| 6. H-Embrittlement Bake | Box 6 | 11.5" | `#E05C5C` (Coral) | Critical |
| 7. Inspect / Next Step | Box 7 | 6.0" | `#27AE60` (Emerald) | QC |

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
140--195 F (60--90 C)
4--12 oz/gal NaOH
3--10 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, mill lubricants`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Pickle):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Pickle` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove alkaline cleaner before acid`
- Check: `Alkaline drag-in neutralizes pickle acid`

*Box 3 -- Acid Pickle:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Pickle`
- Parameters: `HCl 15--30% v/v, ambient` / `or H2SO4 10--25% v/v, 120--175 F` / `5--45 min (scale-dependent)`
- Purpose: `Dissolve oxide scale and rust`
- Check: `INHIBITOR REQUIRED -- prevents base metal attack and H2 absorption` (Coral `#E05C5C`)

*Box 4 -- Rinse (Post-Pickle):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Pickle`
- Parameters: `Ambient temp` / `Min. 2 stages`
- Purpose: `Remove residual acid before next step`
- Check: `IMMEDIATE rinse -- acid must not dry on surface`

*Box 5 -- Neutralize (Optional):*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Neutralize` / Subtitle: `Optional`
- Parameters: `1--3% NaHCO3` / `Ambient, 30--60 sec`
- Purpose: `Neutralize trapped acid in crevices/threads`
- Check: `Critical for complex geometry parts`

*Box 6 -- H-Embrittlement Bake:*
- Badge: `STAGE 6`, fill `#E05C5C`
- Name: `H-Embrittlement Bake` / Subtitle: `If Required`
- Parameters: `375--410 F (190--210 C)` / `4--24 hours per ASTM B849` / `Within 4 hrs of exposure`
- Purpose: `Drive out absorbed hydrogen`
- Check: `MANDATORY for steel >= 40 HRC` (Coral `#E05C5C`)

*Box 7 -- Inspect / Next Step:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Inspect` / Subtitle: `Proceed to Next Step`
- Parameters: `Visual: uniform matte gray` / `No remaining scale or rust`
- Purpose: `Confirm clean surface before plating/coating`
- Check: `Parts flash rust in 5--15 min -- move quickly`

---

**BLOCK C -- Stage Legend Strip**

Y: 13.3" to 14.3"

- Rounded rectangle, X: 0.5", Y: 13.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Treatment & Neutralize` |
| `#E05C5C` (Coral) | `Critical Safety Step` |
| `#27AE60` (Emerald) | `QC / Proceed` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- HCl vs. H2SO4 Comparison

**Dimensions:** Y: 14.5" to 21.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHICH ACID? -- HCL VS. H2SO4

---

**BLOCK E -- Side-by-Side Comparison**

Y: 15.4" to 20.8".

**Left -- Hydrochloric Acid (HCl):**
- Rounded rect, X: 0.5", Y: 15.4", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `HYDROCHLORIC ACID (HCl)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Fast Ambient Pickle` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Temperature | Ambient (68--95 F / 20--35 C) |
| Concentration | 15--30% v/v |
| Pickling rate | Faster at room temp |
| Fume generation | HIGH -- requires local exhaust |
| Scale preference | All types incl. tight mill scale |
| H-embrittlement risk | Moderate (shorter exposure) |
| Iron capacity | ~200 g/L FeCl2 -- high |
| Rinse behavior | FeCl2 very soluble, rinses easily |
| Disposal | Chloride discharge limits may apply |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Most common choice for job shops -- fast, ambient, no heating required` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Sulfuric Acid (H2SO4):**
- Rounded rect, X: 12.0", Y: 15.4", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `SULFURIC ACID (H2SO4)` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `The Hot Heavy-Scale Pickle` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Temperature | 120--175 F (50--80 C) -- requires heat |
| Concentration | 10--25% v/v |
| Pickling rate | Slower at room temp; fast when hot |
| Fume generation | Low at operating temperature |
| Scale preference | Heavy, thick scale |
| H-embrittlement risk | Higher (longer exposure, hot) |
| Iron capacity | ~120 g/L FeSO4 -- lower |
| Rinse behavior | FeSO4 less soluble; can precipitate |
| Disposal | Sulfate less restricted than chloride |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Lower acid cost per gallon; less fume -- preferred for high-volume continuous lines` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 4 -- Hydrogen Embrittlement Risk

**Dimensions:** Y: 21.0" to 27.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> HYDROGEN EMBRITTLEMENT -- KNOW YOUR RISK

**Sublabel:**
- Centered. Y: 21.7". Inter Regular, 16 pt, `#F0EDE8` at 60%

> Acid + Iron = Hydrogen. Higher hardness = higher risk. ASTM B849 is non-negotiable.

---

**BLOCK F -- Hardness/Risk Table**

Y: 22.4" to 27.3". Column widths (23.0" total):
- Hardness Range (4.5") | Risk Level (3.0") | Inhibitor (3.5") | Bake Requirement (6.0") | Notes (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Hardness | Risk | Inhibitor | Bake | Notes |
|---|---|---|---|---|
| < 31 HRC | LOW | Recommended | Not usually required | Standard pickling |
| 31--39 HRC | MODERATE | Required | 375 F, 4--8 hrs after plating | Bake within 4 hrs of exposure |
| 40--50 HRC | HIGH | MUST use | 375--410 F, 8--24 hrs | MANDATORY per ASTM B849 |
| > 50 HRC | EXTREME | Maximum dose | AVOID acid pickle if possible | Use mechanical cleaning (blast) |

Risk level color coding:
- LOW: `#27AE60` (Emerald)
- MODERATE: `#E8A020` (Amber)
- HIGH: `#E05C5C` (Coral)
- EXTREME: `#E05C5C` (Coral), bold

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Risk labels: Barlow SemiBold, 14 pt, color-coded. Notes: Inter Regular, 12 pt, `#F0EDE8` at 80%.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON FAILURES

---

**BLOCK G -- Four Problem Cards**

Y: 28.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 3.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | OVER-ETCHING | Too long in acid; no inhibitor; bath too hot | Reduce time; add inhibitor; check temp |
| 2 | 6.33" | UNDER-PICKLING | Acid exhausted; iron too high; temp too low (H2SO4) | Replenish acid; dump if iron limit hit |
| 3 | 12.16" | FLASH RUST | Delay between pickle and next step | Rinse immediately; proceed within 1--2 min |
| 4 | 18.0" | BLACK SMUT | Iron redeposited from overloaded bath | Improve rinsing; check iron level in bath |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for acid pickling of carbon steel using HCl or H2SO4. Specific formulations, concentrations, and process limits vary by proprietary product and application. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B849.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Acid Pickling (Carbon Steel) -- Process Flow

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
| Zone 3 - Acid Comparison | Section label, two comparison callouts |
| Zone 4 - H-Embrittlement | Section label, sublabel, hardness/risk table |
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
| `Acid Pickling Steel Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Acid Pickling Steel Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Acid Pickling Steel Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Acid Pickling Steel Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Acid Pickling Steel Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Acid Pickling Steel Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Carbon Steel Pickling cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The HCl vs. H2SO4 comparison answers the first question every shop asks. The hydrogen embrittlement table is the most critical safety reference on this poster -- the coral accent on high-risk rows must be unmissable. Flash rust timing (5--15 min) is a practical reality that belongs on the wall.

-> Watson: CT-3 data sourced from Watson Research Brief. Numerical ranges confirmed against brief. Drew spot-check recommended on HCl concentration range (15--30% v/v) and FeCl2 solubility limit (~200 g/L).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #357 -- Construction Workup v1.0*
*2026-04-26*
