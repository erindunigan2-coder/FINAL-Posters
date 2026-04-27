---
Project: Plating Posters Inc
Poster Number: 439
Title: "DLC Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC)"
Technical Source: Industry-standard Diamond-Like Carbon coating process. Covers both PECVD (a-C:H) and filtered cathodic arc (ta-C) methods. DLC classification per Robertson diagram and VDI 2840. Values are typical ranges across industrial DLC systems.
Process Scope: Diamond-Like Carbon coating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DLC
  - DiamondLikeCarbon
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #439 -- Construction Workup
## DLC Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for DLC (Diamond-Like Carbon). It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. DLC is a family of amorphous carbon coatings classified by sp3/sp2 bonding ratio and hydrogen content. The interlayer architecture (Cr/CrC gradient or Si/SiC gradient) is critical for adhesion and must be prominently called out. A vacuum-process poster -- no wet chemistry, no tanks.

Design philosophy: clean U-flow diagram as the hero, a DLC classification callout (Robertson diagram types), a compact parameter summary table, and a troubleshooting quick-hit strip. The poster must convey that DLC is a FAMILY of coatings, not a single material.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **DLC classification callout (Block E):** A compact table showing the Robertson diagram types (a-C:H, ta-C, ta-C:H, metal-doped) with hardness ranges and deposition methods. Visual anchor for the "DLC is a family" message.

3. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

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
| Amber | `#E8A020` | Vacuum/plasma stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & prep stages, structural positives |
| Emerald | `#27AE60` | Deposition stage, optimal reference |
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

ZONE 4 -- DLC CLASSIFICATION (22.0"--28.5" / ~6.5" tall)
  Block E: Robertson diagram DLC types comparison

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

> DLC COATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Diamond-Like Carbon -- a family of amorphous carbon coatings with hardness from 1,000 to 8,000 HV and friction as low as 0.05. Vacuum deposited. No wet chemistry.

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
| 1. Part Preparation | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Cleaning | Box 2 | 6.0" | `#2EC4B6` (Teal) | Cleaning |
| 3. Fixturing | Box 3 | 11.5" | `#2EC4B6` (Teal) | Loading |
| 4. Vacuum / Plasma Setup | Box 4 | 17.0" | `#E8A020` (Amber) | Equipment |

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
| 5. Parameter Setup | Box 5 | 17.0" | `#E8A020` (Amber) | Parameters |
| 6. Deposition | Box 6 | 11.5" | `#27AE60` (Emerald) | Deposition |
| 7. Cooling | Box 7 | 6.0" | `#2EC4B6` (Teal) | Post-Process |
| 8. Inspection & QA | Box 8 | 0.5" | `#E8A020` (Amber) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Preparation:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Surface Ra < 0.05 um (bearing)
No burrs, sharp edges
Mask non-coat areas
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Verify dimensions, mask, inspect surface finish`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `DLC replicates substrate -- polish BEFORE coating`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Alkaline ultrasonic 50--70 C` / `IPA or acetone final` / `Vacuum dry -- zero water spots`
- Purpose: `Remove all oils, particles, fingerprints`
- Check: `Contamination = delamination. No exceptions.`

*Box 3 -- Fixturing:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Fixturing`
- Parameters: `Planetary rotation fixtures` / `1--20 rpm` / `Uniform exposure all surfaces`
- Purpose: `Mount parts for uniform coating access`
- Check: `Contact points will show no coating`

*Box 4 -- Vacuum / Plasma Setup:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Vacuum / Plasma Setup`
- Parameters: `Base: < 10^-5 Torr (PECVD)` / `Base: < 10^-6 Torr (arc)` / `Ar+ ion etch: -400 to -800 V`
- Purpose: `Evacuate chamber, ion-etch substrate surface`
- Check: `CRITICAL: Ion etch removes oxide -- enables adhesion` (Coral `#E05C5C`)

*Box 5 -- Parameter Setup:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Parameter Setup`
- Parameters: `Bias: -100 to -500 V (PECVD)` / `C2H2 or CH4 precursor` / `Interlayer: Cr or Si 100--300 nm`
- Purpose: `Set bias, gas flow, interlayer recipe`
- Check: `Interlayer architecture = adhesion insurance`

*Box 6 -- Deposition:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Deposition` / Subtitle: `DLC Layer`
- Parameters: `a-C:H: 1--3 um (PECVD)` / `ta-C: 0.5--2 um (arc)` / `Rate: 0.5--3 um/hr`
- Purpose: `Grow amorphous carbon film on interlayer`
- Check: `Substrate temp < 200 C -- hardened steel safe`

*Box 7 -- Cooling:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Cooling`
- Parameters: `In-vacuum cool-down` / `Controlled vent to atmosphere` / `Gradual -- avoid thermal shock`
- Purpose: `Prevent stress cracking from rapid cooling`
- Check: `DLC under high compressive stress -- cool slowly`

*Box 8 -- Inspection & QA:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Inspection & QA`
- Parameters: `Nanoindentation (ISO 14577)` / `Rockwell adhesion (VDI 3198)` / `Raman: sp3 content check`
- Purpose: `Verify hardness, adhesion, thickness, friction`
- Check: `Adhesion test: HF1--HF4 acceptable`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep & Cleaning` |
| `#E8A020` (Amber) | `Vacuum Setup & Parameters` |
| `#27AE60` (Emerald) | `Deposition` |
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
- Stage (3.5") | Key Spec (5.5") | Vacuum / Gas (4.5") | Temperature (3.0") | Time (3.0") | Key Control (3.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Key Spec | Vacuum / Gas | Temp | Time | Key Control |
|---|---|---|---|---|---|
| 1. Part Prep | Ra < 0.05 um (bearing) | -- | Ambient | -- | Final finish before coat |
| 2. Cleaning | Alk + IPA/acetone | -- | 50--70 C (alk) | 10--20 min | Zero contamination |
| 3. Fixturing | Planetary rotation | -- | -- | -- | Contact point placement |
| 4. Vacuum Setup | Ar+ etch -400 to -800 V | < 10^-5 Torr | 50--200 C | 5--20 min etch | Oxide removal |
| 5. Parameter Setup | Cr/Si interlayer + gradient | C2H2 or CH4 + Ar | 80--150 C | Per recipe | Interlayer thickness |
| 6. Deposition | a-C:H 1--3 um / ta-C 0.5--2 um | 100--300 mTorr (PECVD) | < 200 C | 2--6 hr total | sp3 content via bias |
| 7. Cooling | In-vacuum slow cool | Controlled vent | Ambient target | 30--120 min | No thermal shock |
| 8. Inspection | Nanoindent + Raman + adhesion | -- | Ambient | -- | VDI 3198 HF1--HF4 |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- DLC Classification

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> DLC IS A FAMILY -- KNOW YOUR TYPE (VDI 2840)

---

**BLOCK E -- DLC Types Comparison**

Y: 22.9" to 28.3".

**Five-row table with colored accents (Robertson diagram summary):**

Rounded rect container, X: 0.5", Y: 22.9", W: 23.0", H: 5.2", fill `#1E2435`.

Header row: fill `#3A4055`, H: 0.5".
Columns: Type (3.5") | Designation (3.0") | sp3 % (2.0") | H Content (2.5") | Hardness HV (3.0") | Method (4.0") | Best For (5.0")

| Type | Designation | sp3 % | H (at.%) | Hardness (HV) | Method | Best For |
|---|---|---|---|---|---|---|
| Hydrogenated amorphous C | a-C:H | 30--50 | 20--40 | 1,000--2,000 | PECVD | General wear, automotive |
| Tetrahedral amorphous C | ta-C | 60--85 | < 2 | 4,000--8,000 | Filtered arc | Cutting tools, extreme wear |
| Hydrogenated ta-C | ta-C:H | 50--70 | 15--30 | 2,000--4,000 | High-density PECVD | Bearings, seals |
| Metal-doped DLC | a-C:H:Me | 20--40 | 10--25 | 1,000--2,000 | Sputtering + PECVD | Low stress, thick films |
| Silicon-doped DLC | a-C:H:Si | 30--50 | 15--30 | 1,500--2,500 | PECVD + TMS | Humidity-stable friction |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Headers: Barlow SemiBold, 13 pt.

**Bottom highlight:**
- Rounded rect, W: 22.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `All DLC types share ultra-low friction (0.05--0.15 dry) -- that is the defining commercial advantage` -- Inter Medium, 13 pt, `#27AE60`

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
| 1 | 0.5" | DELAMINATION | Poor interlayer, contamination, excess stress | Verify Cr/CrC gradient; improve cleaning |
| 2 | 6.33" | BUCKLING / SPALLING | Compressive stress > adhesion; thermal cycling | Stress management: metal-doped or multilayer |
| 3 | 12.16" | HIGH FRICTION | Humidity (ta-C); contamination on surface | Use Si-doped DLC for humid environments |
| 4 | 18.0" | GRAPHITIZATION | Service temp exceeded (> 300 C for a-C:H) | Verify service temp; use ta-C for higher temps |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for Diamond-Like Carbon coating. DLC type classification per VDI 2840. Specific process recipes vary by equipment manufacturer and coating house. Consult your process supplier for application-specific guidance. Source: General industry knowledge; VDI 2840; ISO 20523.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> DLC Coating -- Process Flow

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
| Zone 4 - DLC Classification | Section label, five-row DLC type comparison |
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
| `DLC Coating Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `DLC Coating Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `DLC Coating Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `DLC Coating Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `DLC Coating Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `DLC Coating Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire DLC cluster. The flow diagram must be readable at 6 feet. DLC is fundamentally different from electroplating -- it is a vacuum deposition process with no wet chemistry. The classification table (Zone 4) is essential because DLC is not a single material. Operators and engineers must understand that a-C:H at 1,500 HV and ta-C at 7,000 HV are vastly different coatings for different applications. The interlayer callout in Box 5 is the single most important technical detail -- without a proper Cr/CrC or Si/SiC gradient, the coating WILL delaminate.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #439 -- Construction Workup v1.0*
*2026-04-26*
