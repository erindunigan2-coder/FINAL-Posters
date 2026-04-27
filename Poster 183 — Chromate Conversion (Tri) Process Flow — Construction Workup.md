---
Project: Plating Posters Inc
Poster Number: 183
Title: "Chromate Conversion (Tri) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Trivalent Chromate)"
Technical Source: Industry-standard trivalent chromium process (TCP) conversion coating on aluminum. MIL-DTL-5541 Type II. Complete 7-stage sequence from cleaning through air dry. Values are typical ranges -- no proprietary product names.
Process Scope: Trivalent chromate conversion coating on aluminum -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - ProcessFlow
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #183 -- Construction Workup
## Chromate Conversion (Tri) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CC-05: Trivalent Chromate Conversion Coating on Aluminum. It shows the complete 7-stage process sequence at a glance -- every stage visible in one U-flow diagram. This poster is the "map" that the other 7 posters (#184--#190) zoom into.

Key framing: Trivalent chromate is the RoHS/REACH-compliant replacement for hexavalent chromate (MIL-DTL-5541 Type II). The fundamental trade-off must be stated clearly -- NO self-healing property, narrower pH window, but full regulatory compliance. This poster should explicitly contrast with the hex chromate cluster.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a "Tri vs. Hex -- The Honest Trade-Off" comparison callout, and a troubleshooting quick-hit strip.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 7-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Tri vs. Hex -- The Honest Trade-Off" comparison callout (Block E):** Two side-by-side callout boxes comparing trivalent vs. hexavalent chromate. This is the most important educational element on the poster.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

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
| Amber | `#E8A020` | Post-treatment stages, warning headers, key numbers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Main coating stage, pass/optimal reference |
| Coral | `#E05C5C` | Problems, defects, hex-chromate warnings |
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
  Block B: Seven-stage U-flow diagram (top row: 4 stages, bottom row: 3 stages)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 7-row parameter table (one row per stage)

ZONE 4 -- TRI VS. HEX COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Trivalent vs. Hexavalent side-by-side callout

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
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> CHROMATE CONVERSION (TRIVALENT)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 7 Stages from Cleaning to Air Dry

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> MIL-DTL-5541 Type II. The RoHS-compliant replacement for hex chromate on aluminum. No Cr6+. No self-healing. Know the trade-off.

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

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Top row: four boxes L-to-R. Bottom row: three boxes R-to-L.

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
| 2. Rinse (Pre-Deox) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Deoxidize / Desmut | Box 3 | 11.5" | `#E8A020` (Amber) | Surface Conditioning |
| 4. Rinse (Pre-Coat) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 19.5", Y: 8.3" (bottom center Box 4)
- To: X: 19.5", Y: 9.5" (top center Box 5)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-7, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Tri Chromate Coat | Box 5 | 17.0" | `#27AE60` (Emerald) | Conversion Coating |
| 6. Rinse (Post-Coat) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Air Dry | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |

**Note:** Box 8 position (0.5") is EMPTY on the bottom row. The 7th stage ends at Box 7 (X: 6.0"). The empty space at X: 0.5" can hold a "WHY ONLY 7?" callout note: `No heated cure required. Trivalent coatings air dry at ambient. Full hardness in 24 hours.` Inter Medium 14 pt `#27AE60`.

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
Non-etch, pH 9--11
120--160 F (49--71 C)
3--10 min immersion
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove oils, soils, shop contaminants`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `Silicate-inhibited cleaners preferred for aluminum`

*Box 2 -- Rinse (Pre-Deox):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Deoxidize` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Ambient temp` / `Double rinse standard` / `DI or RO preferred`
- Purpose: `Remove alkaline cleaner before acid deox`
- Check: `Chloride/sulfate in rinse water causes pitting on aluminum`

*Box 3 -- Deoxidize / Desmut:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Deoxidize / Desmut`
- Parameters: `HNO3 30--50% or non-chrome` / `HNO3/HF for high-Cu alloys` / `Ambient, 1--5 min`
- Purpose: `Remove oxide layer and alloying smut`
- Check: `CRITICAL: Tri baths less forgiving than hex -- deox must be thorough` (Coral `#E05C5C`)

*Box 4 -- Rinse (Pre-Coat):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Coat`
- Parameters: `Ambient temp` / `Double rinse standard`
- Purpose: `Remove acid and dissolved metals before coating`
- Check: `< 5 min to coating bath -- aluminum reoxidizes fast`

*Box 5 -- Trivalent Chromate Coat (Main Stage):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Tri Chromate Coat` / Subtitle: `Main Stage`
- Parameters: `pH 3.5--4.2 (narrow!)` / `65--95 F (18--35 C)` / `2--5 min immersion`
- Purpose: `Cr3+/Zr/Ti mixed oxide barrier film`
- Check: `NO Cr6+ in the film -- no self-healing`

*Box 6 -- Rinse (Post-Coat):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Coat`
- Parameters: `Ambient to 100 F` / `15--60 sec` / `DI preferred`
- Purpose: `Remove residual coating solution`
- Check: `Coating more robust than fresh hex -- but still handle carefully`

*Box 7 -- Air Dry:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Air Dry`
- Parameters: `Ambient temperature` / `Forced air acceptable` / `Full cure: 24 hours`
- Purpose: `Harden conversion film`
- Check: `Some tri coatings tolerate up to 150 F -- check supplier TDS`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Conditioning & Post-Treatment` |
| `#27AE60` (Emerald) | `Conversion Coating (Main Stage)` |
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

**BLOCK D -- 7-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | pH (2.0") | Key Control (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.65".

| Stage | Chemistry | Temp | Time | pH | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | Non-etch alk cleaner, pH 9--11 | 120--160 F | 3--10 min | 9--11 | Silicate-inhibited preferred |
| 2. Rinse | DI or RO water | Ambient | 30--60 sec | -- | Double rinse; < 500 uS/cm |
| 3. Deoxidize | HNO3 30--50% or non-chrome | Ambient | 1--5 min | < 2 | Alloy-matched deoxidizer |
| 4. Rinse | DI or RO water | Ambient | 30--60 sec | -- | < 5 min transit to coat |
| 5. Tri Chromate | Cr3+ 0.5--2 g/L; Zr/Ti fluorocomplexes | 65--95 F | 2--5 min | 3.5--4.2 | pH window is NARROW |
| 6. Rinse | DI water preferred | Amb--100 F | 15--60 sec | -- | Gentle -- film is thin |
| 7. Air Dry | -- | Ambient | 24 hr cure | -- | Up to 150 F per some TDS |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Tri vs. Hex Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> TRI VS. HEX -- THE HONEST TRADE-OFF

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Trivalent Chromate (Type II):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `TRIVALENT CHROMATE (TYPE II)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The RoHS-Compliant Future` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Cr6+ content | ZERO -- fully compliant |
| Self-healing | NO -- no mobile Cr6+ reservoir |
| Film thickness | 0.02--0.10 um (much thinner than hex) |
| Appearance | Clear to pale blue/iridescent |
| Salt spray (bare) | 168 hr min (MIL-DTL-5541 Type II) |
| pH window | 3.5--4.2 (narrow -- tight control needed) |
| Thermal stability | More stable than hex (no Cr6+ to degrade) |
| Electrical resistance | Very low -- excellent for Class 3 |
| Regulatory status | RoHS + REACH compliant |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Full regulatory compliance -- the direction the industry is moving` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Hexavalent Chromate (Type I):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `HEXAVALENT CHROMATE (TYPE I)` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `The Legacy Gold Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Cr6+ content | 10--30% of total Cr (carcinogen) |
| Self-healing | YES -- Cr6+ migrates to repassivate damage |
| Film thickness | 0.25--1.0 um (thicker gel) |
| Appearance | Gold to golden-brown |
| Salt spray (bare) | 168--336 hr (Class 1A) |
| pH window | 1.3--1.8 (wider tolerance) |
| Thermal stability | Degrades above 140 F (Cr6+ lost) |
| Electrical resistance | Low (Class 3: thinner coat) |
| Regulatory status | REACH restricted; OSHA PEL 5 ug/m3 |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `Superior self-healing -- but regulatory clock is ticking` -- Inter Medium, 13 pt, `#E05C5C`

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
| 1 | 0.5" | NO COATING | pH > 4.5 or fluoride depleted or surface not deoxidized | Adjust pH to 3.5--4.2; add fluoride; check deox step |
| 2 | 6.33" | WHITE HAZE | Over-immersion or pH < 3.0 or excess fluoride | Reduce time; adjust pH; check fluoride level |
| 3 | 12.16" | FAILED 168 HR SST | Coating too thin or surface contamination or no sealer | Increase time; improve cleaning; add sealer |
| 4 | 18.0" | BLUE/PURPLE FILM | Zirconium precipitation or bath contamination | Check bath chemistry; filter; verify pH |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for trivalent chromium conversion coating on aluminum per MIL-DTL-5541 Type II. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Chromate Conversion (Trivalent) -- Process Flow

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
| Zone 2 - Process Flow | Section label, seven flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 7-row table |
| Zone 4 - Tri vs Hex | Section label, two comparison callouts |
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
| `Chromate Tri Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromate Tri Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromate Tri Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Chromate Tri Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromate Tri Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chromate Tri Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the Trivalent Chromate cluster. The flow diagram must be readable at 6 feet. The Tri vs. Hex comparison is THE educational centerpiece -- frame it honestly. Tri wins on regulation, hex wins on self-healing. Neither is "better" in absolute terms; the choice depends on the specification. The remaining 7 posters (#184--#190) zoom into each stage individually.

Watson flag: Salt spray performance data (96--168 hrs tri vs. 168--336 hrs hex) should be verified against current MIL-DTL-5541 revision.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #183 -- Construction Workup v1.0*
*2026-04-26*
