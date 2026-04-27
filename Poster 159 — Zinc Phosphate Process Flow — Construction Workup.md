---
Project: Plating Posters Inc
Poster Number: 159
Title: "Zinc Phosphate -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-02 technical reference (zinc phosphate conversion coating)"
Technical Source: Industry-standard zinc phosphate conversion coating process. Covers the complete 7+ stage sequence from cleaning through seal/dry. Values are typical ranges for automotive, military, and heavy-duty zinc phosphate pretreatment lines.
Process Scope: Zinc phosphate conversion coating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincPhosphate
  - ConversionCoating
  - ProcessFlow
  - ConstructionWorkup
  - ClusterCC02
---

# Poster #159 -- Construction Workup
## Zinc Phosphate -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CC-02: Zinc Phosphate Conversion Coating. It shows the complete 8-stage process sequence in a U-flow diagram. Zinc phosphate is the heavy-duty phosphate standard -- automotive body-in-white, military hardware, and any application requiring maximum paint adhesion and corrosion resistance.

The poster must make two things unmistakable: (1) Surface conditioning with Ti colloid is THE most critical step in the entire process, and (2) DO NOT rinse between conditioner and phosphate bath. These two points differentiate zinc phosphate from every other phosphate process.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box is color-coded by stage type. The conditioner-to-phosphate transition has a special "NO RINSE" callout.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage).

3. **"Why Zinc Phosphate?" comparison callout (Block E):** Zinc phosphate vs. iron phosphate positioning.

4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

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
| Amber | `#E8A020` | Coating stage, activation, key highlights |
| Teal | `#2EC4B6` | Cleaning, rinse stages, conditioning |
| Emerald | `#27AE60` | Optimal ranges, seal/post-treatment |
| Coral | `#E05C5C` | Problems, defects, critical warnings |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides:**
- 0.5" / 23.5"

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table

ZONE 4 -- ZINC PHOSPHATE vs. IRON PHOSPHATE (22.0"--28.5" / ~6.5" tall)
  Block E: Side-by-side comparison callout

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text (all caps):

> ZINC PHOSPHATE

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> The heavy-duty phosphate. Crystalline, controlled, spec-driven. Automotive OEM, military, and anywhere paint adhesion is mission-critical.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Two rows of four boxes.

Each flow box:
- Rounded rectangle, W: 5.0", H: 4.5"
- Fill: `#1E2435`
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Cond) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Surface Condition | Box 3 | 11.5" | `#E8A020` (Amber) | Conditioning |
| 4. Zn Phosphate Coat | Box 4 | 17.0" | `#E8A020` (Amber) | Coating |

**CRITICAL: Between Box 3 and Box 4 -- NO RINSE callout:**
- Arrow from Box 3 to Box 4 is `#E05C5C` (Coral) instead of standard `#3A4055`
- Small banner below arrow: `NO RINSE BETWEEN THESE STAGES` Barlow SemiBold 12 pt `#E05C5C`
- Sub-text: `Ti colloid must remain on surface` Inter Regular 11 pt `#E05C5C`

**Arrows between other top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Down arrow.

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Rinse (Post-Coat) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. Seal Rinse | Box 6 | 11.5" | `#27AE60` (Emerald) | Post-Treatment |
| 7. DI Final Rinse | Box 7 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 8. Dry-Off Oven | Box 8 | 0.5" | `#E8A020` (Amber) | Drying |

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `Spray: 130--160 F | 2--6 oz/gal` / `Immersion: 140--180 F | 4--8 oz/gal` / `pH 10--13 | 1--10 min`
- Purpose: `Remove all oils, soils, stamping compounds`
- Check: `Silicate-free cleaners strongly preferred`

*Box 2 -- Rinse (Pre-Condition):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Condition`
- Parameters: `Ambient to 80 F` / `Counter-flow (2-stage) common`
- Purpose: `Remove alkaline cleaner before conditioner`
- Check: `Conductivity < 300 uS/cm | pH < 8.0`

*Box 3 -- Surface Conditioning:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Surface Conditioning`
- Parameters: `Ti colloid activator 1--5 g/L` / `pH 7.5--9.5 | Ambient to 100 F` / `30 sec--2 min`
- Purpose: `Create millions of nucleation sites for fine crystals`
- Check: `THE MOST CRITICAL STEP -- fine crystals = good coating` (`#E8A020`)

*Box 4 -- Zinc Phosphate Coat:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Zinc Phosphate`
- Parameters: `Spray: 95--130 F | 1--3 min` / `Immersion: 130--200 F | 3--10 min` / `pH 2.5--3.5`
- Purpose: `Crystalline Zn3(PO4)2 coating for paint adhesion`
- Check: `Target: 150--350 mg/ft2 (automotive OEM)` (`#E8A020`)

*Box 5 -- Rinse (Post-Coat):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Coat`
- Parameters: `Ambient to 80 F` / `Two-stage counter-flow`
- Purpose: `Remove acid residues and soluble salts`
- Check: `Prompt transfer -- white salt efflorescence if delayed`

*Box 6 -- Seal Rinse:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Seal Rinse`
- Parameters: `Non-chrome: 0.5--3% in DI water` / `Chrome: 0.01--0.1% CrO3 (mil-spec)`
- Purpose: `Passivate crystal surfaces, fill micropores`
- Check: `Chrome seal required by MIL-DTL-16232 Class 2`

*Box 7 -- DI Final Rinse:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `DI Water Rinse`
- Parameters: `< 50 uS/cm conductivity` / `Ambient`
- Purpose: `Spot-free drying, remove seal chemistry residue`
- Check: `Some sealers skip this stage -- check supplier TDS`

*Box 8 -- Dry-Off Oven:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry-Off Oven`
- Parameters: `250--350 F (121--177 C)` / `5--15 min`
- Purpose: `Complete drying before e-coat or paint`
- Check: `Do not exceed 400 F` (Coral `#E05C5C`)

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, fill `#252B3D`, radius 4

Five legend items:

| Swatch | Label |
|---|---|
| `#2EC4B6` | `Cleaning & Rinse` |
| `#E8A020` | `Conditioning, Coating & Drying` |
| `#27AE60` | `Seal / Post-Treatment` |
| `#E05C5C` | `Caution / Critical Warning` |

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0".

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Chemistry (5.5") | Temperature (2.5") | Time (2.0") | Key Control (10.0")

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alk Clean | pH 10--13, 2--8 oz/gal | 130--180 F | 1--10 min | Silicate-free; water-break-free |
| 2. Rinse | Fresh water | Ambient--80 F | 30--60 sec | Conductivity < 300 uS/cm |
| 3. Condition | Ti colloid 1--5 g/L, pH 7.5--9.5 | Ambient--100 F | 30 sec--2 min | NEVER heat; colloid viability |
| 4. Zn Phosphate | pH 2.5--3.5, FA 0.5--2.0 pts | 95--200 F | 1--10 min | FA:TA ratio 1:10--1:20; crystal size |
| 5. Rinse (Post) | Fresh water | Ambient--80 F | 30--60 sec | Prompt transfer; no efflorescence |
| 6. Seal | Non-chrome 0.5--3% or CrO3 | Ambient--150 F | 15 sec--2 min | Chrome for mil-spec only |
| 7. DI Rinse | DI water < 50 uS/cm | Ambient | 15--30 sec | Spot-free |
| 8. Dry-Off | -- | 250--350 F | 5--15 min | Do not exceed 400 F |

---

### ZONE 4 -- Zinc Phosphate vs. Iron Phosphate

**Dimensions:** Y: 22.0" to 28.5".

**Section label:** `WHY ZINC PHOSPHATE? -- ZINC vs. IRON PHOSPHATE` -- Y: 22.2".

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Zinc Phosphate (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.2", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ZINC PHOSPHATE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `The Heavy-Duty Standard` -- 14 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Coating type | Crystalline (hopeite / phosphophyllite) |
| Coating weight | 150--1000+ mg/ft2 |
| Crystal size (conditioned) | 2--10 um -- dense, adherent |
| Corrosion (painted) | 500--1500+ hr SST |
| Conditioner | REQUIRED -- Ti colloid |
| Substrates | Steel, aluminum, galvanized |
| Complexity | High -- multi-component, tight control |
| Specifications | MIL-DTL-16232, GM 6041M, Ford WSS-M2P188 |

Bottom: `When the spec says zinc phosphate, there is no substitute.` Inter Medium 13 pt `#E8A020`

**Right -- Iron Phosphate (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.2", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `IRON PHOSPHATE` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `The Lightweight Alternative` -- 14 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Coating type | Amorphous (no crystal structure) |
| Coating weight | 20--80 mg/ft2 |
| Crystal size | N/A -- amorphous film |
| Corrosion (bare) | 2--24 hr SST |
| Conditioner | Not required |
| Substrates | Steel (primarily) |
| Complexity | Low -- simple pH/acid control |
| Specifications | TT-C-490, OEM paint specs |

Bottom: `Lower cost, simpler operation, but less protection. Spec-dependent.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards, gap 0.33".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | COARSE CRYSTALS | Conditioner failure (pH wrong, dead, contaminated) | Check conditioner pH 7.5--9.5; replace if needed |
| 2 | 6.33" | LIGHT COATING | Low total acid, low temp, short time, high free acid | Increase TA; reduce FA; increase time/temp |
| 3 | 12.16" | INCOMPLETE COVERAGE | Oil contamination; cleaner failure; passive substrate | Improve cleaning; check substrate condition |
| 4 | 18.0" | EXCESS SLUDGE | High iron carryover; insufficient filtration | Improve filtration; reduce drag-over |

Interior: Problem `#E05C5C` 16 pt. Cause: `#F0EDE8` 13 pt. Fix: `#27AE60` 13 pt.

---

### ZONE 6 -- Footer Band

**Footer background:** fill `#0D1020`

**Disclaimer:**
> This poster is an educational reference tool. Process parameters shown are typical industry values for zinc phosphate conversion coating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; MIL-DTL-16232; Products Finishing.

**Poster title:** `Zinc Phosphate -- Process Flow`
**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, NO RINSE callout, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Zn vs Fe Phosphate | Section label, two comparison callouts |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | Primary text |
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
| `Zinc Phosphate Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Phosphate Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Phosphate Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Zinc Phosphate Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Phosphate Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Zinc Phosphate Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The "NO RINSE" callout between the conditioner and phosphate stages is the most important single element on this poster. It is the most common setup error in zinc phosphate lines and the most counterintuitive process rule. Make it visually impossible to miss -- coral arrow, coral banner, coral text. The conditioner stage badge should also carry extra visual weight (larger text, brighter accent) to signal its importance relative to other stages.

The zinc vs. iron phosphate comparison mirrors Poster #151's comparison from the opposite perspective. Both posters acknowledge the other process; neither dismisses it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #159 -- Construction Workup v1.0*
*2026-04-26*
