---
Project: Plating Posters Inc
Poster Number: 459
Title: "Electropolishing -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7: Electropolishing)"
Technical Source: Industry-standard electropolishing process for stainless steel (300/400 series) using phosphoric/sulfuric acid electrolyte. Covers the complete 8-stage sequence from cleaning through final handling. Values are typical ranges -- the dominant industrial EP system.
Process Scope: Electropolishing -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electropolishing
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #459 -- Construction Workup
## Electropolishing -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Electropolishing. It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Key differentiator from plating posters: the workpiece is the ANODE, not the cathode. That reversal is the single most important concept on this poster and must be visually prominent. A shop operator sees the full line, a quality engineer checks where surface finish specs originate.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a "How It Works" callout explaining the viscous film mechanism, and a troubleshooting quick-hit strip. Dense but scannable.

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
2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.
3. **"How EP Works" callout (Block E):** Single callout panel explaining the viscous film mechanism and the polishing plateau. The conceptual core of the poster.
4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.
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
| Amber | `#E8A020` | Current/voltage parameters, key warnings |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Electropolishing stage, optimal reference |
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

ZONE 4 -- HOW ELECTROPOLISHING WORKS (22.0"--28.5" / ~6.5" tall)
  Block E: Viscous film mechanism + polishing plateau explanation

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

> ELECTROPOLISHING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Final Handling

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Controlled anodic dissolution -- the part IS the anode. Smoothing, brightening, and passivation in one operation.

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
| 2. Rinse | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Dip (optional) | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 8.3"
- To: X: 19.5", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Electropolish | Box 5 | 17.0" | `#27AE60` (Emerald) | Core Process |
| 6. Rinse (Post-EP) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Neutralize/Passivate | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry / Inspect | Box 8 | 0.5" | `#E8A020` (Amber) | Final |

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
50--70 C (120--160 F)
Soak or ultrasonic
5--15 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, grease, fingerprints`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free surface after rinse`

*Box 2 -- Rinse:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Clean` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove alkaline cleaner residue`
- Check: `Prevents cleaner drag-in to acid dip`

*Box 3 -- Acid Dip (Optional):*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Dip`
- Subtitle: `(Optional -- substrate dependent)` (14 pt, `#F0EDE8` at 60%)
- Parameters: `HCl 10--20% or HNO3 10--20%` / `Ambient, 1--5 min`
- Purpose: `Remove scale and surface oxides`
- Check: `Skip if surface is already clean and oxide-free`

*Box 4 -- Rinse:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Polish`
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove acid residue before EP tank`
- Check: `Acid drag-in contaminates electrolyte`

*Box 5 -- Electropolish (ANODE):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Electropolish` / Subtitle: `PART IS ANODE (+)` (16 pt, `#27AE60`)
- Parameters: `H3PO4 50% + H2SO4 30%` / `65--80 C (150--175 F)` / `10--20 A/dm2 (100--200 A/ft2)` / `8--14 V (on plateau)`
- Purpose: `Anodic dissolution -- preferential peak removal`
- Check: `CRITICAL: Must operate on polishing plateau` (Coral `#E05C5C`)

*Box 6 -- Rinse (Post-EP):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Polish`
- Parameters: `DI water` / `Immediate -- no delay` / `Drag-out recovery first`
- Purpose: `Remove concentrated acid electrolyte`
- Check: `CRITICAL: Delay causes staining and streaks` (Coral `#E05C5C`)

*Box 7 -- Neutralize/Passivate:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Neutralize / Passivate`
- Parameters: `Citric acid 4--10%` / `or HNO3 20--30%` / `Per ASTM A967`
- Purpose: `Enhance Cr-enriched passive layer`
- Check: `Pharma/biotech often require this step per ASME BPE`

*Box 8 -- Dry / Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Inspect`
- Parameters: `Hot air or N2 blow-off` / `No water spots` / `DI water final rinse > 1 MOhm-cm`
- Purpose: `Remove moisture; verify surface finish`
- Check: `Ra measurement per ISO 4287 / ASME B46.1`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Electropolishing (Core)` |
| `#E05C5C` (Coral) | `Caution / Critical` |

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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Current/Voltage (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Current/Voltage | Key Control |
|---|---|---|---|---|---|
| 1. Alk Clean | Alkaline cleaner | 50--70 C | 5--15 min | -- | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Conductivity check |
| 3. Acid Dip | HCl 10--20% or HNO3 | Ambient | 1--5 min | -- | Optional per substrate |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | No acid carry-over |
| 5. Electropolish | H3PO4 50% + H2SO4 30% | 65--80 C | 5--45 min | 10--20 A/dm2, 8--14 V | Polishing plateau |
| 6. Rinse | DI water | Ambient | Immediate | -- | No delay -- staining risk |
| 7. Passivate | Citric 4--10% or HNO3 20--30% | Ambient--50 C | 20--60 min | -- | Per ASTM A967 |
| 8. Dry/Inspect | -- | Hot air | -- | -- | Ra check, visual |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- How Electropolishing Works

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> HOW IT WORKS -- THE VISCOUS FILM MECHANISM

---

**BLOCK E -- Two-Panel Explanation**

Y: 22.9" to 28.3".

**Left -- The Mechanism:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `ANODIC DISSOLUTION` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Part Is The Anode` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

```
1. Part made anodic (+) in acid electrolyte
2. Viscous film forms on surface -- rich in dissolved metal ions
3. Film is THINNER over microscopic peaks
4. Higher current density at peaks = faster dissolution
5. Peaks dissolve preferentially -- surface smooths
6. Result: 50--75% Ra improvement typical
```

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Electropolishing does not create a finish -- it reveals and improves the substrate's metallurgical surface` -- Inter Medium, 13 pt, `#27AE60`

**Right -- The Polishing Plateau:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `THE POLISHING PLATEAU` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Voltage vs. Current Behavior` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Voltage Region | What Happens |
|---|---|
| Low voltage | Active etching -- NOT polishing |
| Polishing plateau | Current stays constant as voltage rises -- THIS is the sweet spot |
| High voltage | Oxygen evolution -- pitting and gas streaks |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Always verify you are on the polishing plateau before production. Voltage too low = etching. Too high = pitting.` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | PITTING | Above polishing plateau (O2 evolution) or Cl- contamination | Verify voltage on plateau; test for chloride |
| 2 | 6.33" | ORANGE PEEL | Below polishing plateau; insufficient time | Increase voltage to plateau; extend time |
| 3 | 12.16" | STREAKING | Non-uniform current; gas entrapment | Reposition parts; tilt for gas escape |
| 4 | 18.0" | STAINING | Slow removal from tank; poor rinsing | Immediate rinse; quick transfer |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electropolishing of stainless steel using phosphoric/sulfuric acid electrolyte. Specific formulations, concentrations, and process limits vary by proprietary product and substrate. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B912; ASME BPE.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electropolishing -- Process Flow

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
| Zone 4 - How EP Works | Section label, two explanation panels |
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
| `Electropolishing Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electropolishing Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electropolishing Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electropolishing Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electropolishing Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electropolishing Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Electropolishing cluster. The most critical concept to convey is the polarity reversal -- the part is the ANODE. This should be visually unmistakable in Box 5. The viscous film mechanism (Zone 4) is what separates EP from chemical etching -- the preferential peak dissolution is the magic. No perchloric acid references anywhere on this poster per Watson safety flag.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #459 -- Construction Workup v1.0*
*2026-04-26*
