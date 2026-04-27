---
Project: Plating Posters Inc
Poster Number: 539
Title: "Suspension Plasma Spray (SPS) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: Industry-standard SPS process. Covers the complete sequence from substrate preparation through final inspection. SPS is a next-generation variant of APS that uses liquid-suspended submicron/nano feedstock to produce columnar microstructures rivaling EB-PVD TBCs at a fraction of the cost. Parameter ranges are less standardized than conventional APS -- note where values are process-specific.
Process Scope: Suspension Plasma Spray -- complete process flow
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - ProcessFlow
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #539 -- Construction Workup
## Suspension Plasma Spray (SPS) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for TS-07: Suspension Plasma Spray. It shows the complete process sequence at a glance -- every stage visible in one U-flow diagram. SPS is the "next-generation APS" -- same plasma gun infrastructure, but submicron powder in liquid carrier instead of dry powder. The result: columnar TBC microstructures that rival EB-PVD at a fraction of the cost. This poster is the map; the other 9 posters in the cluster zoom in.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, an SPS vs. APS comparison callout (the key positioning story), and a troubleshooting quick-hit strip. Dense but scannable.

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
3. **"SPS vs. APS" comparison callout (Block E):** Two side-by-side callout boxes comparing SPS to conventional APS -- the key differentiator story.
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
| Amber | `#E8A020` | Post-treatment stages, warning headers |
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
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- SPS VS. APS COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: SPS vs. Conventional APS side-by-side callout

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
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> SUSPENSION PLASMA SPRAY

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 32 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- Next-Generation TBC Technology

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.1"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Submicron powder in liquid carrier. Columnar microstructures that rival EB-PVD at a fraction of the cost. This is the future of thermal barrier coatings.

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
| 1. Clean & Degrease | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Grit Blast | Box 2 | 6.0" | `#E8A020` (Amber) | Surface Prep |
| 3. Mask & Fixture | Box 3 | 11.5" | `#E8A020` (Amber) | Preparation |
| 4. APS Bond Coat | Box 4 | 17.0" | `#27AE60` (Emerald) | Spray |

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
| 5. SPS Topcoat | Box 5 | 17.0" | `#27AE60` (Emerald) | Spray (SPS) |
| 6. Cool & Inspect | Box 6 | 11.5" | `#2EC4B6` (Teal) | Inspection |
| 7. Post-Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Final QA | Box 8 | 0.5" | `#2EC4B6` (Teal) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Clean & Degrease:*

Stage badge:
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Clean & Degrease`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Alkaline wash 50--70 degC
pH 10--12, 5--15 min
Solvent degrease backup
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove all oils, greases, machining fluids`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free (ASTM F22)`

*Box 2 -- Grit Blast:*
- Badge: `STAGE 2`, fill `#E8A020`
- Name: `Grit Blast`
- Parameters: `White alumina (Al2O3)` / `24--36 mesh, 40--80 PSI` / `Ra 3--8 um, SSPC-SP 5`
- Purpose: `Create anchor profile for mechanical interlocking`
- Check: `Blast-to-spray: < 4 hrs (spec-dependent)`

*Box 3 -- Mask & Fixture:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Mask & Fixture`
- Parameters: `Hi-temp tape (260 degC+)` / `Metal masks, silicone plugs` / `Rotation fixture 60--200 RPM`
- Purpose: `Protect non-spray areas; enable uniform coverage`
- Check: `Shield for liquid overspray (SPS-specific)`

*Box 4 -- APS Bond Coat:*
- Badge: `STAGE 4`, fill `#27AE60`
- Name: `APS Bond Coat`
- Parameters: `MCrAlY or NiCrAlY powder` / `75--150 um thickness` / `Standard APS parameters`
- Purpose: `Oxidation barrier + topcoat adhesion layer`
- Check: `Bond coat applied by conventional APS -- not SPS`

*Box 5 -- SPS Topcoat:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `SPS Topcoat` / Subtitle: `(The Core SPS Step)` (16 pt, `#27AE60`)
- Parameters: `YSZ suspension 5--30 wt%` / `Ethanol or water carrier` / `Standoff 40--80 mm` / `100--400 um total`
- Purpose: `Columnar TBC microstructure via fine-particle deposition`
- Check: `Substrate temp 200--400 degC -- cooling critical` (`#E05C5C`)

*Box 6 -- Cool & Inspect:*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Cool & Inspect`
- Parameters: `Controlled cool-down` / `Visual + thickness check` / `No quenching`
- Purpose: `Prevent thermal shock to columnar structure`
- Check: `Verify columnar morphology on test coupon (SEM)`

*Box 7 -- Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Typically NONE for TBCs` / `No grinding (destroys columns)` / `No sealing (porosity is functional)`
- Purpose: `TBC porosity reduces thermal conductivity -- leave it`
- Check: `Light polish only for non-TBC SPS apps`

*Box 8 -- Final QA:*
- Badge: `STAGE 8`, fill `#2EC4B6`
- Name: `Final QA`
- Parameters: `Cross-section SEM` / `Thermal cycling test` / `XRD phase analysis`
- Purpose: `Confirm columnar structure + phase stability`
- Check: `No monoclinic ZrO2 -- must be tetragonal prime`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Inspection` |
| `#E8A020` (Amber) | `Surface Prep & Post-Treatment` |
| `#27AE60` (Emerald) | `Spray Application` |
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
- Stage (3.5") | Key Spec (5.5") | Temperature (3.0") | Time (2.5") | Standoff/CD (3.5") | Key Control (5.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Key Spec | Temp | Time | Standoff/CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Alk wash pH 10--12 | 50--70 degC | 5--15 min | -- | Water-break-free |
| 2. Grit Blast | Al2O3 24--36 mesh | Ambient | Until profile | 100--200 mm nozzle | Ra 3--8 um |
| 3. Mask/Fixture | Hi-temp tape + metal masks | -- | -- | -- | Shield liquid overspray |
| 4. APS Bond Coat | MCrAlY 75--150 um | Per APS spec | Per APS spec | 75--150 mm | Bond coat before SPS |
| 5. SPS Topcoat | YSZ 5--30 wt% suspension | 200--400 degC sub | 2--10 um/pass | 40--80 mm | Columnar structure |
| 6. Cool/Inspect | Controlled cool-down | Ambient target | -- | -- | Visual + thickness |
| 7. Post-Treatment | None (TBC) | -- | -- | -- | Do NOT grind TBCs |
| 8. Final QA | SEM + XRD + cycling test | -- | -- | -- | Tetragonal prime phase |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- SPS vs. APS Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHY SPS? -- SPS VS. CONVENTIONAL APS

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Suspension Plasma Spray (SPS):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `SUSPENSION PLASMA SPRAY (SPS)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Next-Generation TBCs` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Feedstock | Submicron suspension (0.05--5 um) |
| Carrier | Ethanol or water |
| Microstructure | COLUMNAR (mimics EB-PVD) |
| Porosity | 10--25% (intentional) |
| Thermal conductivity | 0.7--1.2 W/mK |
| Strain tolerance | HIGH -- columns flex independently |
| Bond strength | > 15 MPa (on bond coat) |
| Standoff | 40--80 mm (closer than APS) |
| Cost | Medium (between APS and EB-PVD) |
| Status | Emerging -- less standardized |

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `EB-PVD performance at 1/10 the cost -- no vacuum chamber required` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Conventional APS:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CONVENTIONAL APS` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Established Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Feedstock | Dry powder (10--90 um) |
| Carrier | Argon carrier gas |
| Microstructure | LAMELLAR (splat-based) |
| Porosity | 10--20% |
| Thermal conductivity | 0.8--1.2 W/mK |
| Strain tolerance | LOW -- lamellae crack under cycling |
| Bond strength | > 10 MPa |
| Standoff | 75--150 mm |
| Cost | Low (most economical TBC method) |
| Status | Mature -- well standardized |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Proven workhorse for 50+ years -- but lamellar structure limits thermal cycling life` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | LAMELLAR INSTEAD OF COLUMNAR | Standoff too far; particle size too large | Reduce standoff to 40--60 mm; verify suspension particle size < 5 um |
| 2 | 6.33" | DELAMINATION FROM BOND COAT | Contaminated interface or inadequate bond coat | Verify APS bond coat quality; minimize time between bond coat and SPS |
| 3 | 12.16" | INJECTOR CLOGGING | Suspension sedimentation or high solids loading | Agitate suspension; reduce solids loading; check shelf life |
| 4 | 18.0" | SUBSTRATE OVERHEATING | Standoff too close; insufficient cooling | Increase cooling air; monitor substrate temp < 400 degC |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for suspension plasma spray (SPS). SPS is an emerging technology with less standardized parameters than conventional APS -- specific values vary by equipment, feedstock, and application. Consult your coating supplier and applicable specifications for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Suspension Plasma Spray (SPS) -- Process Flow

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
| Zone 4 - SPS vs APS | Section label, two comparison callouts |
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
| `SPS Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `SPS Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `SPS Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `SPS Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `SPS Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `SPS Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

SPS is a niche, advanced process -- the audience for this poster is coating service providers and aerospace R&D, not general plating shops. Position it clearly as "next-generation APS" that builds on existing APS infrastructure. The comparison callout (Zone 4) is the most important storytelling element -- it answers "why bother with SPS when APS works?" The answer: columnar microstructure for superior thermal cycling life, at a fraction of EB-PVD cost. Watson flagged that parameters are less standardized than conventional APS -- the disclaimer reflects this.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #539 -- Construction Workup v1.0*
*2026-04-26*
