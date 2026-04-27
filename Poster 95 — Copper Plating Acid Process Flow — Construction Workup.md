---
Project: Plating Posters Inc
Poster Number: 95
Title: "Copper Plating (Acid) -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-09 technical reference (acid copper sulfate)"
Technical Source: Industry-standard acid copper sulfate plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Values are typical ranges for bright acid copper sulfate -- the dominant decorative and PCB copper plating system.
Process Scope: Acid copper sulfate plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CopperPlating
  - AcidCopper
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEP09
---

# Poster #95 -- Construction Workup
## Copper Plating (Acid) -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-09: Copper Plating (Acid Sulfate). It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Acid copper sulfate is one of the most forgiving and well-understood plating processes in the industry: bright, ductile deposits used for decorative undercoats, PCBs, electroforming, and salvage. The bath is simple -- copper sulfate, sulfuric acid, chloride ion, and organic additives -- but the devil is in the chloride control and brightener balance.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (acid copper vs. alkaline copper -- when to use each), and a troubleshooting quick-hit strip. Dense but scannable.

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
2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters.
3. **"Acid vs. Alkaline Copper" comparison callout (Block E):** Two side-by-side callout boxes. Established pattern.
4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.
5. **4 pt left-border accents on callout boxes.**
6. **Global Colors / swatch remap for Light edition.**
7. **JetBrains Mono font:** Fallback: Courier Prime.
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

ZONE 4 -- ACID VS. ALKALINE COPPER COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Acid vs. Alkaline copper side-by-side callout

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

> COPPER PLATING (ACID)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Final Rinse

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Acid copper sulfate -- bright, ductile, and forgiving. The backbone of decorative plating, PCB metallization, and electroforming.

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
| 1. Soak Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

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
| 5. Copper Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Anti-Tarnish / Post-Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Final Rinse / Dry | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Soak Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Soak Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
140--180 F (60--82 C)
4--8 oz/gal
3--10 min
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, drawing compounds`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Flowing or cascade`
- Purpose: `Remove alkaline cleaner before acid dip`
- Check: `Alkaline drag-in neutralizes acid activation`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `H2SO4 5--10% v/v (copper/brass)` / `HCl 10--30% (steel after strike)` / `Ambient, 15--30 sec`
- Purpose: `Remove surface oxides, expose clean metal`
- Check: `Substrate determines acid choice` (Teal `#2EC4B6`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient temp` / `Single overflow`
- Purpose: `Remove acid residue before copper tank`
- Check: `Acid drag-in disrupts brightener system`

*Box 5 -- Copper Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Copper Plate` / Subtitle: `Acid Sulfate`
- Parameters: `CuSO4-5H2O: 180--250 g/L` / `H2SO4: 45--100 g/L` / `Cl-: 30--80 ppm` / `70--80 F (21--27 C)` / `20--40 ASF (rack)`
- Purpose: `Electrodeposit bright copper`
- Check: `Cl- is THE critical additive control`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Ambient temp` / `Double overflow or cascade`
- Purpose: `Remove acid copper drag-out`
- Check: `CRITICAL: Cu is a contaminant in downstream baths` (Coral `#E05C5C`)

*Box 7 -- Anti-Tarnish / Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Anti-Tarnish`
- Parameters: `Chromate or organic inhibitor` / `Ambient, 15--60 sec`
- Purpose: `Prevent copper oxidation/tarnish`
- Check: `Skip if proceeding directly to nickel`

*Box 8 -- Final Rinse / Dry:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Final Rinse / Dry`
- Parameters: `Rinse: ambient, flowing` / `Dry: forced air or oven`
- Purpose: `Remove treatment chemistry, dry parts`
- Check: `Inspect for tarnish before packing`

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
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | No alkaline carry-over |
| 3. Activation | H2SO4 5--10% or HCl | Ambient | 15--30 sec | -- | Substrate-dependent |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | No acid carry-over |
| 5. Copper Plate | CuSO4 180--250 g/L, H2SO4 45--100, Cl- 30--80 ppm | 70--80 F | Per spec | 20--40 ASF (rack) | Cl- control |
| 6. Rinse | DI or city water | Ambient | 30--60 sec | -- | Cu drag-out critical |
| 7. Anti-Tarnish | Chromate or organic inhibitor | Ambient | 15--60 sec | -- | Skip if to nickel |
| 8. Final Rinse/Dry | Water / forced air | Ambient | 30--60 sec | -- | No tarnish before pack |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Acid vs. Alkaline Copper Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> ACID VS. ALKALINE COPPER -- WHEN TO USE EACH

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Acid Copper Sulfate:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `ACID COPPER SULFATE` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Bright Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| pH | -- (strongly acidic, not measured) |
| Copper source | CuSO4-5H2O |
| Temperature | 70--80 F (21--27 C) |
| Brightness | Excellent -- mirror-bright from bath |
| Leveling | Exceptional with proper additives |
| Throwing power | Moderate (improve with high acid:Cu) |
| Substrates | Cu, brass, nickel, steel (with strike) |
| Speed | High -- near 100% cathode efficiency |
| Typical use | Decorative, PCBs, electroforming |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Cannot plate directly on steel or zinc -- immersion deposit will peel. Strike required.` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Alkaline Non-Cyanide Copper:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `ALKALINE NON-CYANIDE COPPER` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Strike Alternative` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| pH | 8--11 (alkaline) |
| Copper source | CuSO4 + complexant (HEDP, citrate) |
| Temperature | 110--145 F (43--63 C) |
| Brightness | Matte to semi-bright |
| Leveling | Low to moderate |
| Throwing power | Good -- better than acid |
| Substrates | Steel, zinc die cast, ABS (direct) |
| Speed | Lower -- 40--70% cathode efficiency |
| Typical use | Strike layer before acid copper |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Cyanide-free strike for active metals -- plates directly on zinc die castings and steel.` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | HAZY/MILKY DEPOSIT | Low Cl- (<30 ppm) or organic contamination | Check Cl- by titration; carbon treat |
| 2 | 6.33" | PITTING | Oil drag-in, low carrier, poor agitation | Improve cleaning; add carrier; increase air |
| 3 | 12.16" | ROUGHNESS | Anode sludge, no anode bags, particulate | Install PP anode bags; increase filtration |
| 4 | 18.0" | BURNING AT HCD | CD too high, low copper metal, high acid | Reduce CD; add CuSO4; check acid:Cu ratio |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for acid copper sulfate plating. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: General industry knowledge; Modern Electroplating (Schlesinger & Paunovic).

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Copper Plating (Acid) -- Process Flow

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
| Zone 4 - Acid vs Alkaline | Section label, two comparison callouts |
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

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Copper Acid Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Copper Acid Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Copper Acid Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Copper Acid Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Copper Acid Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Copper Acid Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Acid Copper cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 7 posters (#96--#102) zoom into each stage individually. The acid vs. alkaline copper comparison answers the fundamental question: "when do I use acid copper vs. alkaline copper?" The answer: acid copper gives you brightness and leveling but cannot plate directly on active metals -- you need a strike first. Alkaline non-cyanide copper IS that strike.

Key technical note: acid copper pH is not measured. The bath is strongly acidic (contains 45--100 g/L H2SO4). This is different from acid zinc where pH is a critical control. Do not show a pH row for the acid copper main tank -- show "--" or "N/A (strongly acidic)."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #95 -- Construction Workup v1.0*
*2026-04-26*
