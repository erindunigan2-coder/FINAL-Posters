---
Project: Plating Posters Inc
Poster Number: 279
Title: "Sulfuric Anodizing (Type II) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1: Type II)"
Technical Source: Industry-standard sulfuric acid anodizing per MIL-A-8625F Type II. Covers the complete 8-stage sequence from alkaline cleaning through seal. Values are typical ranges for conventional Type II sulfuric acid anodizing -- the most common anodizing process globally.
Process Scope: Sulfuric acid anodizing (Type II) -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - SulfuricAcid
  - ProcessFlow
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #279 -- Construction Workup
## Sulfuric Anodizing (Type II) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Sulfuric Acid Anodizing (Type II). It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. This is the "map" that posters #280--#286 zoom into. Type II sulfuric acid anodizing is the workhorse -- the process most people mean when they say "anodizing." The concept hook for this poster: same H2SO4 electrolyte as Type III hardcoat, but room-temperature operation and moderate current density produce a completely different film -- thinner, softer, dyeable in every color.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Each box color-coded by stage type. Arrows are simple connectors. Straightforward geometry.
2. **Parameter summary table (Block D):** Compact 8-row table (one row per stage) with key parameters.
3. **"Same Chemistry, Different Film" concept callout (Block E):** Side-by-side comparison of Type II vs. Type III -- same H2SO4 electrolyte, different temperature and current, completely different result. This is the concept hook.
4. **Troubleshooting quick-hit strip (Block F):** Horizontal strip of 4 common problems with one-line fixes.
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
| Amber | `#E8A020` | Key parameters, warning headers, section accents |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Anodize stage (main tank), optimal reference |
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

ZONE 4 -- SAME CHEMISTRY, DIFFERENT FILM (22.0"--28.5" / ~6.5" tall)
  Block E: Type II vs. Type III side-by-side comparison

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

> SULFURIC ACID ANODIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Type II -- Complete Process Flow -- 8 Stages from Clean to Seal

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The workhorse anodizing process. Decorative, corrosion-protective, and dyeable in every color. MIL-A-8625F Type II.

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
| 2. Rinse (Pre-Etch) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Caustic Etch | Box 3 | 11.5" | `#E8A020` (Amber) | Etch |
| 4. Desmut | Box 4 | 17.0" | `#E8A020` (Amber) | Chemical Treatment |

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
| 5. Rinse (Pre-Anodize) | Box 5 | 17.0" | `#2EC4B6` (Teal) | Rinse |
| 6. Anodize (Main Tank) | Box 6 | 11.5" | `#27AE60` (Emerald) | Anodize |
| 7. Dye (Optional) | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Seal | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

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
130--160 F (55--70 C)
30--60 g/L (4--8 oz/gal)
2--10 min soak
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, compounds, fingerprints`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Etch):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Etch` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Cascade preferred` / `<500 uS/cm target`
- Purpose: `Remove alkaline cleaner before etch`
- Check: `Dwell 10--15 sec over cleaner to drain`

*Box 3 -- Caustic Etch:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Caustic Etch`
- Parameters: `NaOH 40--80 g/L` / `130--150 F (55--65 C)` / `1--5 min (alloy-dependent)`
- Purpose: `Uniform matte surface, remove mill finish`
- Check: `CAUTION: H2 gas -- ventilation required` (Coral `#E05C5C`)

*Box 4 -- Desmut:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Deoxidize / Desmut`
- Parameters: `HNO3 25--50% v/v` / `Ambient, 30--120 sec` / `HF for Cu alloys (2024, 7075)`
- Purpose: `Remove etch smut (Cu, Si, Fe residues)`
- Check: `HF: calcium gluconate required at station` (Coral `#E05C5C`)

*Box 5 -- Rinse (Pre-Anodize):*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Anodize (CRITICAL)`
- Parameters: `DI water preferred` / `<100 uS/cm target` / `60--120 sec, double cascade`
- Purpose: `Prevent electrolyte contamination`
- Check: `Cl- and F- dragover destroy coating quality` (Coral `#E05C5C`)

*Box 6 -- Anodize (Main Tank):*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Anodize` / Subtitle: `Main Tank`
- Parameters: `H2SO4 150--200 g/L` / `64--72 F (18--22 C)` / `12--18 ASF (1.2--1.8 A/dm2)` / `20--60 min`
- Purpose: `Grow anodic oxide film (5--25 um)`
- Check: `Temperature is the #1 parameter` (Emerald `#27AE60`)

*Box 7 -- Dye (Optional):*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Dye` / Subtitle: `(Optional -- Class 2)`
- Parameters: `Organic dye 1--3 g/L` / `120--150 F (50--65 C)` / `pH 5.0--6.5, 5--30 min`
- Purpose: `Color the porous oxide before sealing`
- Check: `Min 8 um coating for good color uptake`

*Box 8 -- Seal:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Seal`
- Parameters: `Hot DI: 205--212 F (96--100 C)` / `or Ni acetate: 158--185 F` / `15--30 min`
- Purpose: `Close pores, lock dye, corrosion protection`
- Check: `Dye spot test (ASTM B680) to verify seal`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Etch, Desmut & Post-Treatment` |
| `#27AE60` (Emerald) | `Anodize (Main Tank)` |
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
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Key Control (8.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alkaline Clean | Non-silicated alk cleaner 30--60 g/L | 130--160 F | 2--10 min | Water-break-free test |
| 2. Rinse (Pre-Etch) | City or DI water | Ambient | 30--60 sec | <500 uS/cm; cascade |
| 3. Caustic Etch | NaOH 40--80 g/L | 130--150 F | 1--5 min | Alloy-specific time |
| 4. Desmut | HNO3 25--50% v/v (+HF for Cu alloys) | Ambient | 30--180 sec | Complete smut removal |
| 5. Rinse (Pre-Anodize) | DI water (<50 uS/cm) | Ambient | 60--120 sec | <100 uS/cm; Cl- < 25 ppm |
| 6. Anodize | H2SO4 150--200 g/L | 64--72 F | 20--60 min | Temp +/-1 C; 12--18 ASF |
| 7. Dye | Organic dye 1--3 g/L; pH 5--6.5 | 120--150 F | 5--30 min | Min 8 um coating thickness |
| 8. Seal | Hot DI or Ni acetate 5--8 g/L | 158--212 F | 15--30 min | Dye spot test (B680) |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Same Chemistry, Different Film

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> SAME CHEMISTRY, DIFFERENT FILM -- TYPE II VS. TYPE III

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Type II (This Poster):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `TYPE II -- SULFURIC ACID` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Decorative Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Electrolyte | H2SO4 150--200 g/L |
| Temperature | 64--72 F (18--22 C) -- room temp |
| Current density | 12--18 ASF |
| Film thickness | 5--25 um (0.2--1.0 mil) |
| Hardness | 200--350 HV |
| Dyeable | YES -- full color spectrum |
| Best alloys | 6061, 6063, 5052, 1100 |
| MIL spec | MIL-A-8625F Type II |
| Salt fog (sealed) | 336+ hours (ASTM B117) |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Same H2SO4 electrolyte as Type III -- temperature and current make ALL the difference` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Type III (Hardcoat):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `TYPE III -- HARDCOAT` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Engineering Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Electrolyte | H2SO4 150--200 g/L (SAME) |
| Temperature | 28--41 F (0--5 C) -- NEAR FREEZING |
| Current density | 24--36 ASF |
| Film thickness | 25--100+ um (1.0--4.0+ mil) |
| Hardness | 400--600+ HV -- harder than mild steel |
| Dyeable | Dark colors only (black, dark blue) |
| Best alloys | 6061, 6063, 5052 |
| MIL spec | MIL-A-8625F Type III |
| Abrasion (Taber) | 1--5 mg/1000 cycles |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Refrigeration required. Temperature control is THE critical challenge for hardcoat.` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | BURNING | Excessive CD, high temp, or low acid | Reduce CD; check temperature |
| 2 | 6.33" | POWDERING | Bath temp >77 F (>25 C) or too long | Cool bath; reduce cycle time |
| 3 | 12.16" | PITTING | Chloride >25 ppm in anodize bath | Analyze bath; improve pre-anodize rinse |
| 4 | 18.0" | POOR DYE UPTAKE | Coating too thin (<8 um) or sealed too early | Increase anodize time; verify seal timing |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for conventional sulfuric acid anodizing (Type II) per MIL-A-8625F. Specific formulations, concentrations, and process limits vary by application and specification. Consult your process supplier and applicable spec for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Sulfuric Anodizing (Type II) -- Process Flow

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
| Zone 4 - Type II vs III | Section label, two comparison callouts |
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
| `Sulfuric Anodizing Type II Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Sulfuric Anodizing Type II Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Sulfuric Anodizing Type II Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Sulfuric Anodizing Type II Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Sulfuric Anodizing Type II Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Sulfuric Anodizing Type II Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Type II anodizing cluster. The U-flow must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The Type II vs. Type III comparison is the concept hook: same electrolyte, different temperature and current, completely different film properties. This should be the most visually prominent callout on the poster. Temperature is the hero variable -- emphasize it everywhere. Alloy compatibility is referenced but detailed in the Main Tank poster (#285).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #279 -- Construction Workup v1.0*
*2026-04-26*
