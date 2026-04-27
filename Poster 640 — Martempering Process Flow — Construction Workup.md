---
Project: Plating Posters Inc
Poster Number: 640
Title: "Martempering -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10: Martempering)"
Technical Source: Industry-standard martempering (marquenching) -- interrupted quench process. Covers complete 9-stage sequence from pre-clean through inspection. Values are typical ranges from ASM Handbook and AMS 2759 series. Final structure is tempered martensite -- same as conventional Q&T but with dramatically less distortion.
Process Scope: Martempering -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HeatTreatment
  - Martempering
  - Marquenching
  - ProcessFlow
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #640 -- Construction Workup
## Martempering -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for HT-10: Martempering (Marquenching). It shows the complete 9-stage process sequence at a glance. Martempering is the interrupted-quench cousin of austempering -- same hot salt bath concept, completely different outcome. Where austempering holds until bainite forms, martempering holds just long enough for temperature equalization, then air cools to form martensite uniformly. Same martensite as conventional Q&T, but 50-80% less distortion. Temper is still required. This poster is the "map" that posters #641-#648 zoom into.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1-5), vertical connector, bottom row R-to-L (stages 6-9). Each box color-coded.
2. **Parameter summary table (Block D):** 9-row table with key parameters.
3. **"Martempering vs. Austempering vs. Conventional Q&T" comparison (Block E):** Three-column comparison.
4. **Failure-mode quick-hit strip (Block F):** 4 common defects.
5. **Standard design elements:** 4 pt top accents, light edition remap, JetBrains Mono with Courier Prime fallback.
6. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, descriptions
- **JetBrains Mono Regular** -- all parameter data, temperatures, times, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Heat/austenitizing stages, key numbers |
| Teal | `#2EC4B6` | Prep, cooling, and QA stages |
| Emerald | `#27AE60` | Equalization hold and key advantages |
| Coral | `#E05C5C` | Critical transfer, problems, defects |
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
  Block D: 9-row parameter table

ZONE 4 -- THREE-WAY COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Martempering vs. Austempering vs. Conventional Q&T

ZONE 5 -- FAILURE MODE QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-failure strip

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

> MARTEMPERING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 9 Stages from Pre-Clean to Inspect

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Interrupted quench for uniform martensite. Same hardness as conventional Q&T -- 50-80% less distortion. Temper required.

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

Y: 3.8" to 14.0" (~10.2" tall). Top row of five boxes, bottom row of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Pre-Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Load & Fixture | Box 2 | 5.1" | `#2EC4B6` (Teal) | Prep |
| 3. Preheat (Optional) | Box 3 | 9.7" | `#E8A020` (Amber) | Heat |
| 4. Austenitize | Box 4 | 14.3" | `#E8A020` (Amber) | Heat |
| 5. Quench into Hot Salt | Box 5 | 18.9" | `#E05C5C` (Coral) | Critical Quench |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.3"
- To: X: 21.0", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Air Cool | Box 6 | 18.9" | `#27AE60` (Emerald) | Transformation |
| 7. Wash | Box 7 | 14.3" | `#2EC4B6` (Teal) | Post-Process |
| 8. Temper | Box 8 | 9.7" | `#E8A020` (Amber) | Heat Treatment |
| 9. Inspect & QA | Box 9 | 5.1" | `#2EC4B6` (Teal) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

---

**Inside each flow box (top to bottom):**

*Box 1 -- Pre-Clean:*

Stage badge: Rounded rect, 1.0" x 0.35", fill `#2EC4B6`, text `STAGE 1` Barlow Condensed ExtraBold, 13 pt, `#1A1F2E`. Position: X: box left + 0.2", Y: box top + 0.5".

Stage name: Barlow SemiBold, 20 pt, `#F0EDE8`. Text: `Pre-Clean`

Key parameters: JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 155%
```
Solvent or alkaline wash
Dry completely -- salt bath
moisture safety critical
```

Purpose: Inter Regular, 12 pt, `#F0EDE8` at 70%
Text: `Remove all contaminants; ensure zero moisture`

Critical check: Inter Medium, 11 pt, `#2EC4B6`
Text: `CHECK: Parts MUST be bone dry before any salt bath contact`

*Box 2 -- Load & Fixture:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Load & Fixture`
- Parameters: `Salt bath fixtures` / `Drainage orientation` / `Transfer path clear`
- Purpose: `Orient for rapid immersion and salt drainage on extraction`
- Check: `Fixture rated for austenitizing temp (1500+ F)`

*Box 3 -- Preheat (Optional):*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Preheat` / Subtitle: `(Optional)`
- Parameters: `800--1000 F (427--538 C)` / `Heavy sections > 2" only` / `Reduces thermal shock`
- Purpose: `Equalize temperature in thick sections before austenitizing`
- Check: `Skip for thin sections; required for sections > 2"`

*Box 4 -- Austenitize:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Austenitize`
- Parameters: `1475--1600 F (802--871 C)` / `Hold: 30--90 min` / `Atmosphere or salt bath`
- Purpose: `Transform to 100% austenite (FCC) -- same as conventional hardening`
- Check: `Incomplete austenitization = soft spots`

*Box 5 -- Quench into Hot Salt:*
- Badge: `STAGE 5`, fill `#E05C5C`
- Name: `Quench into Hot Salt` / Subtitle: `or Hot Oil`
- Parameters: `Salt: just above Ms` / `350--600 F (177--316 C)` / `Hold: 5--15 min ONLY`
- Purpose: `Rapid cool to equalize surface and core temp -- NO transformation yet`
- Check: `CRITICAL: Equalization only -- do NOT hold until bainite forms` (Coral)

*Box 6 -- Air Cool:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Air Cool`
- Parameters: `Remove from salt` / `Still air to room temp` / `Martensite forms NOW`
- Purpose: `Uniform martensite transformation -- surface and core transform together`
- Check: `This is where the magic happens -- uniform transformation = minimal distortion`

*Box 7 -- Wash:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Wash`
- Parameters: `Hot water rinse` / `Remove all salt residue` / `Dry before temper`
- Purpose: `Salt left on parts causes corrosion and contaminates temper furnace`
- Check: `Inspect blind holes and recesses for trapped salt`

*Box 8 -- Temper:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Temper`
- Parameters: `300--1100 F (149--593 C)` / `Per grade & hardness target` / `1--4 hours`
- Purpose: `Relieve quench stress; achieve target hardness; improve toughness`
- Check: `TEMPER IS MANDATORY -- unlike austempering, martensite MUST be tempered`

*Box 9 -- Inspect & QA:*
- Badge: `STAGE 9`, fill `#2EC4B6`
- Name: `Inspect & QA`
- Parameters: `Hardness: Rockwell C` / `Microstructure: 100% tempered martensite` / `Distortion: measure and compare`
- Purpose: `Confirm properties, verify minimal distortion, release or reject`
- Check: `Any pearlite or bainite in micro = process deviation`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep, Wash & QA` |
| `#E8A020` (Amber) | `Heat Cycle & Temper` |
| `#27AE60` (Emerald) | `Martensite Formation (Air Cool)` |
| `#E05C5C` (Coral) | `Critical Quench / Caution` |

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
- Stage (3.0") | Medium (4.0") | Temperature (4.0") | Time (3.0") | Key Control (9.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".

| Stage | Medium | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Pre-Clean | Solvent / alkaline | Ambient | 5--15 min | Bone dry before salt contact |
| 2. Load | Alloy fixtures | -- | -- | Drainage orientation; transfer path clear |
| 3. Preheat | Furnace (optional) | 800--1000 F | 30--60 min | Heavy sections only (> 2") |
| 4. Austenitize | Endo gas / salt bath | 1475--1600 F | 30--90 min | Full transformation to austenite |
| 5. Quench (salt) | Hot salt / hot oil | 350--600 F | 5--15 min | Equalization ONLY -- no transformation |
| 6. Air Cool | Still air | Salt temp to RT | 15--60 min | Martensite forms uniformly |
| 7. Wash | Hot water rinse | -- | -- | Remove all salt residue |
| 8. Temper | Air atmosphere | 300--1100 F | 1--4 hr | Per grade and target hardness |
| 9. Inspect | -- | -- | -- | HRC, micro, distortion, crack check |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Three-Way Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> MARTEMPERING vs. AUSTEMPERING vs. CONVENTIONAL Q&T

---

**BLOCK E -- Three-Column Comparison**

Y: 22.9" to 28.3". Three equal-width callout boxes.

**Left -- Martempering (X: 0.5", W: 7.3"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`, radius 6
- Title: `MARTEMPERING` -- Barlow SemiBold, 18 pt, `#27AE60`

| Property | Value |
|---|---|
| Final structure | Tempered martensite |
| Salt hold purpose | Equalization only (5--15 min) |
| Transformation | During AIR COOL (after salt) |
| Temper required | YES |
| Distortion | 50--80% less than conv. Q&T |
| Hardness | 45--65 HRC (as-quenched) |
| Best for | Bearings, gears, tools |

**Center -- Austempering (X: 8.3", W: 7.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 6
- Title: `AUSTEMPERING` -- Barlow SemiBold, 18 pt, `#E8A020`

| Property | Value |
|---|---|
| Final structure | Bainite |
| Salt hold purpose | Full transformation (30--120 min) |
| Transformation | IN SALT BATH |
| Temper required | NO |
| Distortion | 60--90% less than conv. Q&T |
| Hardness | 35--55 HRC |
| Best for | Springs, clips, ADI |

**Right -- Conventional Q&T (X: 16.1", W: 7.4"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6
- Title: `CONVENTIONAL Q&T` -- Barlow SemiBold, 18 pt, `#E05C5C`

| Property | Value |
|---|---|
| Final structure | Tempered martensite |
| Quench | Rapid to RT (oil, water, polymer) |
| Transformation | During rapid quench |
| Temper required | YES |
| Distortion | Baseline (100%) |
| Hardness | 45--65 HRC (as-quenched) |
| Best for | General purpose; all section sizes |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Failure Mode Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON FAILURES

---

**BLOCK F -- Four Failure Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.25".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BAINITE IN MICRO | Salt bath temp too high or hold too long -- transformation started in salt | Lower salt temp to just above Ms; reduce hold to equalization only |
| 2 | 6.25" | PEARLITE (SOFT SPOTS) | Transfer too slow; hardenability insufficient for section | Faster transfer; higher-hardenability grade |
| 3 | 12.0" | CRACKING | Sharp stress risers; section variation; contaminated salt | Radius corners; preheat; maintain salt purity |
| 4 | 17.75" | EXCESSIVE DISTORTION | Salt temp too far below Ms; non-uniform agitation | Verify Ms; optimize salt temp; improve agitation |

Interior per card:
- Failure: Barlow SemiBold, 15 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for martempering (marquenching). Specific temperatures, hold times, and salt compositions vary by steel grade, section thickness, and specification. Consult your process engineer and applicable AMS/ASTM standards for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 4.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Martempering -- Process Flow

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
| Zone 4 - Three-Way Comparison | Section label, three comparison callouts |
| Zone 5 - Failure Modes | Section label, four failure cards |
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
| `Martempering Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Martempering Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Martempering Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Martempering Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Martempering Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Martempering Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Martempering cluster. The three-way comparison in Zone 4 is the educational hook -- it answers "how is this different from austempering AND from conventional Q&T?" in one visual. The key distinction is Stage 5 vs. Stage 6: the salt bath (Stage 5) is for equalization ONLY -- the actual martensite transformation happens during air cooling (Stage 6). This is the opposite of austempering where transformation happens IN the salt. The "temper is mandatory" callout in Stage 8 distinguishes martempering from austempering where no temper is needed.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #640 -- Construction Workup v1.0*
*2026-04-26*
