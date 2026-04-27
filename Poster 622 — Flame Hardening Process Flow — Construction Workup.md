---
Project: Plating Posters Inc
Poster Number: 622
Title: "Flame Hardening -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8)"
Technical Source: Industry-standard flame hardening process. Covers the complete 9-stage sequence from material verification through final inspection. Values are typical ranges for medium-carbon steels (1045/4140 class) using oxy-acetylene or oxy-propane flame. The simplest and most versatile localized surface hardening method.
Process Scope: Flame hardening -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlameHardening
  - HeatTreatment
  - ProcessFlow
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #622 -- Construction Workup
## Flame Hardening -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Flame Hardening. If induction hardening is the precision instrument, flame hardening is the versatile field tool. No custom coils. No high-frequency power supplies. An oxy-fuel flame, a water spray, and an operator who knows how to read cherry red. This poster maps the complete 9-stage sequence -- the "how" that the remaining 8 posters (#623--#630) zoom into.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a comparison callout (flame vs. induction -- when to choose each), and a troubleshooting quick-hit strip. This process is operator-skill-dependent in a way that induction is not, and the poster reflects that.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Each box is color-coded by stage type.

2. **Parameter summary table (Block D):** A compact 9-row table (one row per stage) with key parameters.

3. **"Flame vs. Induction" comparison callout (Block E):** Two side-by-side callout boxes.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

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
| Amber | `#E8A020` | Flame/heating stages, key parameters |
| Teal | `#2EC4B6` | Prep and quench stages, structural positives |
| Emerald | `#27AE60` | Optimal/pass states, setup stages |
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
  Block B: Nine-stage U-flow diagram (top row 5, bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 9-row parameter table (one row per stage)

ZONE 4 -- FLAME VS. INDUCTION COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Flame vs. Induction side-by-side callout

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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> FLAME HARDENING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 9 Stages from Material Verification to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The simplest and most versatile surface hardening method. Oxy-fuel flame, water spray, and operator skill. No power supply. No custom coils. No atmosphere.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row: five boxes. Bottom row: four boxes (right-aligned with vertical connector from Stage 5).

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Verify Material | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Pre-Clean | Box 2 | 5.1" | `#2EC4B6` (Teal) | Preparation |
| 3. Setup Equipment | Box 3 | 9.7" | `#27AE60` (Emerald) | Setup |
| 4. Position Part | Box 4 | 14.3" | `#27AE60` (Emerald) | Setup |
| 5. Preheat (Optional) | Box 5 | 18.9" | `#E8A020` (Amber) | Heating |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.05", Y: 8.3" (bottom center Box 5)
- To: X: 21.05", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Heat | Box 6 | 18.9" | `#E8A020` (Amber) | Heating |
| 7. Quench | Box 7 | 14.3" | `#2EC4B6` (Teal) | Cooling |
| 8. Temper | Box 8 | 9.7" | `#E8A020` (Amber) | Post-Process |
| 9. Inspect & QA | Box 9 | 5.1" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Verify Material:*

Stage badge (top-left inside box):
- Rounded rect, 1.0" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Verify Material`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Min 0.40% C for HRC 55+
Medium carbon or cast iron
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Confirm carbon content is adequate for target hardness`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: MTR or spark test for carbon content`

*Box 2 -- Pre-Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Pre-Clean`
- Parameters: `Remove oil, grease, scale` / `Flame won't penetrate heavy scale`
- Purpose: `Clean surface for uniform heating`
- Check: `Scale = hot/cold spots = non-uniform case`

*Box 3 -- Setup Equipment:*
- Badge: `STAGE 3`, fill `#27AE60`
- Name: `Setup Equipment`
- Parameters: `Select torch tip` / `Adjust oxy-fuel ratio` / `Neutral to slight reducing flame`
- Purpose: `Configure flame for part geometry`
- Check: `Flashback arrestors on BOTH hoses`

*Box 4 -- Position Part:*
- Badge: `STAGE 4`, fill `#27AE60`
- Name: `Position Part`
- Parameters: `Rotary table, between centers,` / `or bed for progressive` / `Flame-to-part: 0.25--0.75 in`
- Purpose: `Secure part for uniform flame coverage`
- Check: `Manual or CNC traverse -- operator skill critical`

*Box 5 -- Preheat (Optional):*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Preheat` / Subtitle: `(OPTIONAL)` (12 pt, `#E8A020`)
- Parameters: `300--400 F (149--204 C)` / `Large or complex parts only` / `Reduces thermal shock`
- Purpose: `Prevent cracking on large or complex sections`
- Check: `Skip for simple geometries and thin sections`

*Box 6 -- Heat:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Heat` / Subtitle: `THE MAIN STAGE` (12 pt, `#E8A020`)
- Parameters: `1500--1650 F (816--899 C)` / `Cherry red to bright orange` / `Traverse: 2--12 in/min`
- Purpose: `Austenitize the surface layer`
- Check: `CAUTION: Overheating causes melting at 5600+ F flame temp` (Coral `#E05C5C`)

*Box 7 -- Quench:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Quench`
- Parameters: `Water spray (standard)` / `Follows 0.5--2.0 in behind flame` / `Immersion for spot/spin`
- Purpose: `Transform austenite to martensite`
- Check: `CRITICAL: Quench must follow flame immediately`

*Box 8 -- Temper:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Temper`
- Parameters: `300--400 F (149--204 C)` / `1--2 hours` / `Oven temper (standard)`
- Purpose: `Relieve quench stresses, improve toughness`
- Check: `Temper immediately after quench`

*Box 9 -- Inspect & QA:*
- Badge: `STAGE 9`, fill `#27AE60`
- Name: `Inspect & QA`
- Parameters: `Hardness per ASTM E18` / `Pattern: acid etch` / `Cracks: MPI or dye penetrant`
- Purpose: `Verify hardness, pattern, and crack-free condition`
- Check: `Check overlap zones in progressive hardening`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Quench` |
| `#27AE60` (Emerald) | `Setup & QA` |
| `#E8A020` (Amber) | `Heating & Temper` |
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

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Method/Setup (4.5") | Temperature (3.0") | Time/Speed (3.0") | Quench (3.0") | Key Control (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Method/Setup | Temp | Time/Speed | Quench | Key Control |
|---|---|---|---|---|---|
| 1. Verify | -- | -- | -- | -- | Min 0.40% C for HRC 55+ |
| 2. Clean | -- | -- | 5--15 min | -- | Scale and oil free |
| 3. Setup | Torch tip, oxy-fuel ratio | -- | -- | -- | Neutral/reducing flame |
| 4. Position | Rotary/bed/centers | -- | -- | -- | 0.25--0.75 in flame distance |
| 5. Preheat | Optional | 300--400 F | As needed | -- | Large/complex parts only |
| 6. Heat | Spot/progressive/spin | 1500--1650 F | 2--12 in/min | -- | Cherry red to bright orange |
| 7. Quench | -- | 60--80 F water | Immediate | Water spray | 0.5--2.0 in behind flame |
| 8. Temper | Oven | 300--400 F | 1--2 hr | -- | Temper within 1 hour |
| 9. Inspect | -- | -- | -- | -- | Hardness, pattern, MPI |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Flame vs. Induction Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> FLAME VS. INDUCTION -- WHICH SURFACE HARDENING?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Flame Hardening:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `FLAME HARDENING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Flexibility & Simplicity` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Heat source | Oxy-fuel flame (acetylene or propane) |
| Precision | Moderate -- operator/torch dependent |
| Case depth range | 0.050--0.250 in (1.3--6.4 mm) |
| Case depth tolerance | +/- 0.030 in (0.76 mm) |
| Heating rate | 50--200 F/second |
| Cycle time | Minutes (progressive) |
| Best for | Large parts; low volume; field repairs; irregular shapes |
| Capital cost | Low (standard torch equipment) |
| Operator dependency | HIGH -- skill-based process |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `No custom coil needed -- adapts to any geometry with standard torch equipment` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Induction Hardening:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `INDUCTION HARDENING` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Precision & Speed` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Heat source | Electromagnetic induction (eddy currents) |
| Precision | Excellent -- coil shape defines pattern exactly |
| Case depth range | 0.020--0.300 in (0.5--7.6 mm) |
| Case depth tolerance | +/- 0.005--0.010 in |
| Heating rate | 100--1000 F/second |
| Cycle time | Seconds (single-shot) |
| Best for | High-volume; precision patterns; small-to-medium parts |
| Capital cost | High (power supply + custom coils) |
| Operator dependency | LOW -- recipe-controlled |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Fastest surface hardening method -- seconds per part in production` -- Inter Medium, 13 pt, `#2EC4B6`

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
| 1 | 0.5" | OVERHEATING / MELTING | Flame too close; dwell too long; wrong tip | Increase distance; increase traverse speed; select proper tip |
| 2 | 6.33" | SOFT SPOTS | Insufficient temp; uneven flame coverage; overlap zone | Verify temperature (pyrometer); improve flame head design |
| 3 | 12.16" | CRACKING | Quench too severe; section too thin; pre-existing stress | Reduce quench; preheat; stress relieve before hardening |
| 4 | 18.0" | NON-UNIFORM CASE | Manual technique variation; inconsistent traverse speed | Automate traverse; use CNC control; verify with test coupons |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for flame hardening of medium-carbon steels. Specific torch settings, flame-to-part distances, and traverse speeds vary by part geometry and equipment. Consult your process engineer for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Flame Hardening -- Process Flow

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
| Zone 4 - Flame vs Induction | Section label, two comparison callouts |
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
| `Flame Hardening Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Hardening Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Hardening Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Flame Hardening Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Hardening Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Flame Hardening Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Flame Hardening cluster. Flame hardening is the most operator-dependent heat treatment process -- the operator IS the CNC. The comparison with induction answers the core question: flame is for large parts, low volume, field work, and flexibility; induction is for precision, speed, and high volume. Both use the same metallurgy (austenitize + quench = martensite) but deliver it through completely different means. The 9-stage flow has 5 boxes on top and 4 on bottom -- the top row is slightly tighter than the induction cluster's 4/3 split.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #622 -- Construction Workup v1.0*
*2026-04-26*
