---
Project: Plating Posters Inc
Poster Number: 71
Title: "Nickel-Cobalt Plating -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Industry-standard nickel-cobalt alloy electroplating process. Modified Watts or sulfamate Ni bath with cobalt sulfate addition. Deposits 15-35% Co by weight, yielding 400-700 HV hardness for aerospace turbine, magnetic, and high-wear applications. Watson flagged this as lower-confidence cluster -- formulations are often OEM-specific.
Process Scope: Nickel-cobalt alloy plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #71 -- Construction Workup
## Nickel-Cobalt Plating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-06: Nickel-Cobalt Plating. It shows the complete 8-stage process at a glance -- every stage visible in one U-flow diagram. Nickel-cobalt is a specialty alloy process used primarily in aerospace and high-wear applications. The cobalt co-deposits with nickel to produce a harder, more wear-resistant deposit than pure nickel. Formulations are frequently OEM-specific (Pratt & Whitney, GE, etc.), so this poster presents general sulfamate-based NiCo ranges -- not a single proprietary recipe.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a "Why NiCo?" callout comparing it to standard nickel, and a troubleshooting quick-hit strip. Same architecture as Poster #31 (Zinc Alkaline Process Flow).

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1-4), vertical connector, bottom row R-to-L (stages 5-8). Each box is color-coded by stage type. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters.

3. **"Why NiCo?" comparison callout (Block E):** Two side-by-side callout boxes comparing Ni-Co alloy vs. standard Watts/sulfamate nickel.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

8. **Print size -- 24x36":** Set to exactly 24 inches wide by 36 inches tall.

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

ZONE 4 -- WHY NICKEL-COBALT? COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: NiCo alloy vs. standard nickel side-by-side callout

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

> NICKEL-COBALT PLATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Post-Treatment

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Nickel-cobalt alloy -- harder than pure nickel, built for turbines and high-wear tooling. Formulations are often OEM-specific. This poster covers general sulfamate-based NiCo ranges.

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
| 1. Alkaline Soak Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
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
| 5. Nickel-Cobalt Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post-Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry / Final Inspection | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Alkaline Soak Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Alkaline Soak Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
140--180 F (60--82 C)
4--8 oz/gal
3--10 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, machining compounds`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove alkaline cleaner residue`
- Check: `Prevents neutralizing the acid activation`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `HCl 20--50% v/v (steel)` / `Wood's strike (Inconel/Ti)` / `Ambient, 15--60 sec`
- Purpose: `Remove surface oxides, expose clean metal`
- Check: `AEROSPACE: Wood's strike mandatory for superalloys` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove activation acid`
- Check: `Acid drag-in contaminates the NiCo bath`

*Box 5 -- Nickel-Cobalt Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Nickel-Cobalt Plate` / Subtitle: `Main Tank`
- Parameters: `Ni sulfamate 300--400 g/L` / `CoSO4 10--60 g/L` / `pH 3.5--4.5` / `120--140 F (49--60 C)` / `20--60 ASF`
- Purpose: `Electrodeposit Ni-Co alloy onto substrate`
- Check: `Co% controlled by bath ratio + CD`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `Flowing, multi-stage`
- Purpose: `Remove plating solution drag-out`
- Check: `CRITICAL: Thorough rinse before any post-treatment` (Coral `#E05C5C`)

*Box 7 -- Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Chromium topcoat (wear)` / `or heat treat 300 C / 1--4 hr` / `or final deposit (magnetic)`
- Purpose: `Maximize hardness or apply protective topcoat`
- Check: `Heat treat can push hardness to 600--700 HV`

*Box 8 -- Dry / Final Inspection:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Final Inspect`
- Parameters: `Forced air or oven` / `XRF for Co% verification` / `Hardness test (Vickers)`
- Purpose: `Verify deposit composition and properties`
- Check: `AMS 2424 specifies Co% and hardness requirements`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
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
- Stage (3.5") | Chemistry (5.0") | Temperature (3.0") | Time (2.5") | Current Density (3.5") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Soak Clean | Alk cleaner 4--8 oz/gal | 140--180 F | 3--10 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Conductivity check |
| 3. Activation | HCl 20--50% or Wood's strike | Ambient | 15--60 sec | -- | Substrate-dependent |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | No acid carry-over |
| 5. NiCo Plate | Ni sulfa 300--400 g/L, Co 10--60 | 120--140 F | Per spec | 20--60 ASF | Co% + pH |
| 6. Rinse | DI or city water | Ambient | 30--60 sec | -- | Thorough multi-stage |
| 7. Post-Treatment | Cr topcoat or heat treat 300 C | Per process | Per process | Per process | Application-dependent |
| 8. Dry/Inspect | -- | Oven or forced air | -- | -- | XRF + hardness |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Why Nickel-Cobalt? Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY NICKEL-COBALT? -- NiCo ALLOY VS. STANDARD NICKEL

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Nickel-Cobalt Alloy:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `NICKEL-COBALT ALLOY` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Hardness Advantage` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Deposit composition | 65--85% Ni / 15--35% Co |
| Hardness (as-plated) | 400--500 HV |
| Hardness (heat treated) | 600--700 HV |
| Wear resistance | Superior to pure nickel |
| Magnetic permeability | High (tunable via Co%) |
| Internal stress | Higher than sulfamate Ni |
| Primary applications | Aerospace turbine, molds, tooling |
| Key spec | AMS 2424 |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Higher cobalt = higher hardness. But formulations are OEM-specific -- always verify against the governing spec.` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Standard Nickel (Watts/Sulfamate):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `STANDARD NICKEL` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The General-Purpose Baseline` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Deposit composition | 99%+ Ni |
| Hardness (Watts, as-plated) | 150--250 HV |
| Hardness (sulfamate) | 180--300 HV |
| Wear resistance | Good but lower than NiCo |
| Magnetic permeability | Moderate |
| Internal stress | Low (especially sulfamate) |
| Primary applications | Decorative, corrosion, engineering |
| Key spec | AMS 2403, ASTM B689 |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Standard nickel covers 90% of applications. NiCo is for when pure nickel is not hard enough.` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | CO% OUT OF SPEC | Bath ratio imbalance, temp drift, CD mismatch | Analyze bath metals; adjust CoSO4; check temperature |
| 2 | 6.33" | CRACKING (POST HEAT TREAT) | Too rapid heating, excess cobalt, hydrogen | Slow ramp rate; verify Co%; H2 bake before heat treat |
| 3 | 12.16" | ROUGH / NODULAR | Particulate contamination, anode sludge | Inspect anode bags; increase filtration; filter bath |
| 4 | 18.0" | LOW HARDNESS | Cobalt too low, organic contamination | Add CoSO4; carbon treat; verify by XRF |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Nickel-cobalt alloy plating parameters shown are typical industry values for sulfamate-based NiCo baths. Specific formulations, alloy targets, and process limits are frequently OEM-specific. Consult your process supplier and governing specification (e.g., AMS 2424) for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5; Modern Electroplating.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Nickel-Cobalt Plating -- Process Flow

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
| Zone 4 - Why NiCo | Section label, two comparison callouts |
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
| `NiCo Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `NiCo Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `NiCo Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `NiCo Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `NiCo Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `NiCo Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Nickel-Cobalt cluster. Watson flagged EP-06 as lower-confidence -- the tagline and disclaimer both call out that NiCo formulations are often OEM-specific. The comparison callout answers the most common question: "why NiCo instead of straight nickel?" The answer is hardness -- NiCo can reach 600-700 HV heat-treated, versus 150-300 HV for standard nickel. The flow diagram must be readable at 6 feet. The remaining 7 posters (#72-#78) zoom into each stage individually.

Cobalt safety note (IARC Group 2B -- possibly carcinogenic) is flagged on the activation poster and main tank poster where it is most relevant, not on this overview.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #71 -- Construction Workup v1.0*
*2026-04-26*
