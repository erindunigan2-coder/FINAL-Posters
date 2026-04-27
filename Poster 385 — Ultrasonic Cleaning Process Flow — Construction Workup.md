---
Project: Plating Posters Inc
Poster Number: 385
Title: "Ultrasonic Cleaning -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Technical Source: Industry-standard ultrasonic cleaning process. Covers the complete 6-stage sequence from pre-clean assessment through inspection and handling. Frequency selection (20-170 kHz) and cavitation mechanism are the defining concepts.
Process Scope: Ultrasonic cleaning -- complete process flow (6 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #385 -- Construction Workup
## Ultrasonic Cleaning -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-07: Ultrasonic Cleaning. It shows the complete 6-stage sequence at a glance -- every stage visible in one U-flow diagram. The hero concept is cavitation: microscopic bubbles imploding at 5,000 K and 1,000+ atm to blast contaminants off surfaces. A shop operator sees the full cleaning line, a supervisor checks parameters, and a quality engineer spots where problems originate.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a frequency selection guide (the key decision in ultrasonic), and a troubleshooting quick-hit strip. Dense but scannable -- the wall reference for the entire ultrasonic cleaning line.

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

1. **Process flow diagram (Block B -- HERO):** Six rounded rectangles in a U-flow: top row L-to-R (stages 1--3), vertical connector, bottom row R-to-L (stages 4--6). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows.

2. **Frequency selection guide (Block E):** Four-column comparison showing 20-25 kHz, 40 kHz, 68-80 kHz, and 120-170 kHz with application guidance. The defining technical decision for ultrasonic cleaning.

3. **Parameter summary table (Block D):** A compact 6-row table (one row per stage) with key parameters.

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
| Amber | `#E8A020` | Frequency/power parameters, warning headers |
| Teal | `#2EC4B6` | Cleaning stages, rinse stages, structural positives |
| Emerald | `#27AE60` | Optimal ranges, success states |
| Coral | `#E05C5C` | Problems, defects, safety warnings |
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
- 15.0" -- Zone 2/Zone 3 boundary
- 21.0" -- Zone 3/Zone 4 boundary
- 28.0" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.0" / ~12.1" tall)
  Block B: Six-stage U-flow diagram (2 rows of 3)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.0"--21.0" / ~6.0" tall)
  Block D: 6-row parameter table (one row per stage)

ZONE 4 -- FREQUENCY SELECTION GUIDE (21.0"--28.0" / ~7.0" tall)
  Block E: Four-frequency comparison with application guidance

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.0"--32.5" / ~4.5" tall)
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

> ULTRASONIC CLEANING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- 6 Stages from Assessment to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Cavitation does what soaking cannot -- microscopic explosions blasting contaminants from every blind hole, thread, and undercut.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.0" (~12.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Six-Stage U-Flow Diagram**

Y: 3.8" to 13.8" (~10.0" tall). Two rows of three boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 7.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-3, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Assess & Pre-Clean | Box 1 | 0.5" | `#E8A020` (Amber) | Preparation |
| 2. Degas & Heat Solution | Box 2 | 8.0" | `#2EC4B6` (Teal) | Bath Prep |
| 3. Ultrasonic Clean | Box 3 | 15.5" | `#27AE60` (Emerald) | Main Process |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 3 to Stage 4):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.0", Y: 8.3" (bottom center Box 3)
- To: X: 19.0", Y: 9.5" (top center Box 4)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 4-6, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 4. Rinse (Post-Clean) | Box 4 | 15.5" | `#2EC4B6` (Teal) | Rinse |
| 5. Dry | Box 5 | 8.0" | `#E8A020` (Amber) | Drying |
| 6. Inspect & Handle | Box 6 | 0.5" | `#E8A020` (Amber) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Assess & Pre-Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#E8A020`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Assess & Pre-Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Heavy soil? Pre-clean first
Select frequency for substrate
Load basket -- wire mesh only
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Evaluate soil type, select frequency, pre-clean if needed`

Critical check:
- Inter Medium, 12 pt, `#E8A020`
- Text: `NEVER skip pre-clean on heavy grease or buffing compound`

*Box 2 -- Degas & Heat Solution:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Degas & Heat`
- Parameters: `Run ultrasonics 10--15 min (no parts)` / `Heat to 120--150 F (50--65 C)` / `Solution level covers transducers + 2--4"`
- Purpose: `Remove dissolved gas; bring bath to operating temperature`
- Check: `Degassed solution cleans dramatically better` (`#27AE60`)

*Box 3 -- Ultrasonic Clean (Main Step):*
- Badge: `STAGE 3`, fill `#27AE60`
- Name: `Ultrasonic Clean`
- Parameters: `3--10 min general` / `1--3 min light particulate` / `15--20 min tenacious soil` / `Power: 5--10 W/L`
- Purpose: `Cavitation removes contaminants from all surfaces`
- Check: `Do NOT lay parts on tank bottom -- blocks transducer energy` (`#E05C5C`)

*Box 4 -- Rinse (Post-Clean):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Clean`
- Parameters: `Running water (general)` / `DI cascade (precision)` / `Ambient temp`
- Purpose: `Remove cleaning solution and loosened contaminants`
- Check: `Precision apps: ultrasonic rinse in DI water`

*Box 5 -- Dry:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Dry`
- Parameters: `Forced air or oven` / `Clean, filtered air` / `Hot DI rinse assists drying`
- Purpose: `Remove all moisture before next process step`
- Check: `Water spots = contaminated rinse or hard water`

*Box 6 -- Inspect & Handle:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Inspect & Handle`
- Parameters: `Water break test` / `UV (365 nm) fluorescence` / `Visual under bright light`
- Purpose: `Verify cleanliness; handle with clean gloves only`
- Check: `Process to next step without delay -- re-contamination is real` (`#E05C5C`)

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.0"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.6", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#E8A020` (Amber) | `Preparation & Drying` |
| `#2EC4B6` (Teal) | `Bath Prep & Rinse` |
| `#27AE60` (Emerald) | `Main Cleaning Stage` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.0" to 21.0" (~6.0" tall).

---

**Section label:**
- Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 6-Row Parameter Table**

Y: 15.8" to 20.8". Column widths (23.0" total):
- Stage (3.5") | Solution (5.5") | Temperature (3.0") | Time (3.0") | Power/Freq (4.0") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Stage | Solution | Temp | Time | Power/Freq | Key Control |
|---|---|---|---|---|---|
| 1. Assess/Pre-Clean | Per soil type | -- | -- | -- | Frequency selection |
| 2. Degas & Heat | Alkaline 30--60 g/L | 120--150 F | 10--15 min degas | Per unit spec | Solution level |
| 3. Ultrasonic Clean | Same bath | 120--150 F | 3--10 min | 5--10 W/L | Basket loading |
| 4. Rinse | DI or city water | Ambient | 30--60 sec | -- | Conductivity check |
| 5. Dry | -- | Per spec | Until dry | -- | Spot-free surface |
| 6. Inspect | -- | -- | -- | -- | Water break / UV |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Frequency Selection Guide

**Dimensions:** Y: 21.0" to 28.0" (~7.0" tall).

---

**Section label:**
- Centered. Y: 21.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> FREQUENCY SELECTION -- THE CRITICAL DECISION

**Sublabel:**
- Centered. Y: 21.7". Inter Regular, 16 pt, `#F0EDE8` at 60%

> Lower frequency = larger bubbles = more aggressive. Higher frequency = smaller bubbles = gentler but reaches finer features.

---

**BLOCK E -- Four-Frequency Comparison**

Y: 22.3" to 27.8". Four side-by-side callout boxes.

| Frequency | X | W | Accent | Title |
|---|---|---|---|---|
| 20--25 kHz | 0.5" | 5.38" | `#E05C5C` | AGGRESSIVE |
| 40 kHz | 6.13" | 5.38" | `#E8A020` | STANDARD |
| 68--80 kHz | 11.75" | 5.38" | `#2EC4B6` | GENTLE |
| 120--170 kHz | 17.38" | 6.12" | `#27AE60` | MEGASONIC |

Each box: Rounded rect H: 5.3", fill `#1E2435`, left accent 0.06", radius 6.

*20--25 kHz box:*
- Frequency: `20--25 kHz` JetBrains Mono 18 pt `#E05C5C`
- Bubble size: `~170 micrometers`
- Energy: `HIGH -- aggressive`
- Best for: `Heavy soil, castings, steel, scale, buffing compound`
- Caution: `Can erode soft metals, thin walls, coatings`
- Substrates: `Hardened steel, cast iron, heavy stampings`

*40 kHz box:*
- Frequency: `40 kHz` JetBrains Mono 18 pt `#E8A020`
- Bubble size: `~85 micrometers`
- Energy: `Moderate -- standard`
- Best for: `General cleaning, most plating pre-treatment`
- Note: `Best balance of cleaning power and surface safety`
- Substrates: `Steel, stainless, brass, copper`

*68--80 kHz box:*
- Frequency: `68--80 kHz` JetBrains Mono 18 pt `#2EC4B6`
- Bubble size: `~45 micrometers`
- Energy: `Lower -- gentle`
- Best for: `Precision parts, thin-walled, soft metals, electronics`
- Note: `Aluminum and brass safe at these frequencies`
- Substrates: `Aluminum, brass, thin-wall, zinc die cast`

*120--170 kHz box:*
- Frequency: `120--170 kHz` JetBrains Mono 18 pt `#27AE60`
- Bubble size: `~20 micrometers`
- Energy: `Very low -- ultra-gentle`
- Best for: `Semiconductor wafers, optics, medical devices`
- Note: `Sub-micron particle removal without surface damage`
- Substrates: `Silicon, glass, ceramics, MEMS, PCBs`

Interior per box:
- Frequency: JetBrains Mono, 18 pt, accent color
- Bubble size / Energy: JetBrains Mono, 12 pt, `#F0EDE8` at 70%
- Best for: Inter Regular, 13 pt, `#F0EDE8`
- Caution/Note: Inter Medium, 12 pt, accent color
- Substrates: Inter Regular, 12 pt, `#F0EDE8` at 60%

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.0" to 32.5" (~4.5" tall).

---

**Section label:**
- Centered. Y: 28.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 28.9" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 3.2", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | UNEVEN CLEANING | Overloaded basket; parts shielding each other | Reduce load; reposition; use sweep frequency |
| 2 | 6.33" | SURFACE EROSION | Frequency too low for substrate; time too long | Increase frequency; reduce time; add spacers |
| 3 | 12.16" | NO IMPROVEMENT OVER SOAK | Solution not degassed; temp too high; transducer failure | Degas; reduce temp to optimum; foil test |
| 4 | 18.0" | RE-CONTAMINATION | Dirty solution; no filtration; sludge buildup | Filter continuously; clean tank; replace solution |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for ultrasonic cleaning. Specific equipment settings, solution types, and cycle times vary by application. Consult your equipment manufacturer and process supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Ultrasonic Cleaning -- Process Flow

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
| Zone 2 - Process Flow | Section label, six flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 6-row table |
| Zone 4 - Frequency Guide | Section label, sublabel, four frequency comparison boxes |
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
| `Ultrasonic Cleaning Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ultrasonic Cleaning Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ultrasonic Cleaning Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Ultrasonic Cleaning Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ultrasonic Cleaning Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ultrasonic Cleaning Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Ultrasonic Cleaning cluster. The flow diagram must be readable at 6 feet -- large boxes, clear stage numbers. The remaining 6 posters (#386--#391) zoom into each stage or topic individually. The frequency selection guide (Zone 4) is the signature content -- this is the decision every shop must make when specifying an ultrasonic system. Cavitation is THE concept: microscopic implosions creating micro-jets at 400 km/hr that reach where nothing else can.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #385 -- Construction Workup v1.0*
*2026-04-26*
