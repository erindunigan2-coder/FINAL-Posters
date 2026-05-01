---
Project: Plating Posters Inc
Poster Number: 703
Title: "Industrial Priming -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Industry-standard industrial priming systems. Covers zinc-rich primers (IOZ and OZ), epoxy primers, and aerospace primers. Complete 8-stage process flow from surface preparation through inspection and recoat readiness. Values are typical ranges -- zero brand names.
Process Scope: Industrial priming systems -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IndustrialPriming
  - ZincRichPrimer
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #703 -- Construction Workup
## Industrial Priming -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Cluster 7: Industrial Priming Systems. It shows the complete 8-stage priming sequence at a glance -- from solvent cleaning through inspection and recoat readiness. The hero is a U-flow diagram. Zinc-rich primer is the star of this cluster -- galvanic (sacrificial) protection of steel, the same principle as hot-dip galvanizing but applied as a paint film.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table for quick reference, a comparison callout (IOZ vs. OZ zinc-rich), and a troubleshooting quick-hit strip. Dense but scannable -- the coating foreman's wall reference for the entire priming line.

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

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"IOZ vs. OZ" comparison callout (Block E):** Two side-by-side callout boxes comparing inorganic zinc vs. organic zinc primers. Established pattern from Poster #31.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

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
| Amber | `#E8A020` | Application stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Primer cure, optimal reference |
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

ZONE 4 -- IOZ VS. OZ COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Inorganic zinc vs. organic zinc side-by-side callout

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

> INDUSTRIAL PRIMING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- 8 Stages from Surface Prep to Recoat Readiness

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Zinc-rich primers -- galvanic protection of steel, applied as paint. The foundation coat that everything else depends on.

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
| 1. Solvent Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Surface Prep (Blast) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Preparation |
| 3. Compressed Air Blow-Down | Box 3 | 11.5" | `#2EC4B6` (Teal) | Cleaning |
| 4. Pretreatment | Box 4 | 17.0" | `#E8A020` (Amber) | Pretreatment |

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
| 5. Primer Application | Box 5 | 17.0" | `#E8A020` (Amber) | Application |
| 6. Flash / Set Time | Box 6 | 11.5" | `#27AE60` (Emerald) | Cure |
| 7. Cure | Box 7 | 6.0" | `#27AE60` (Emerald) | Cure |
| 8. Inspection & Recoat | Box 8 | 0.5" | `#C8D0D8` (Silver) | Inspection |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Solvent Clean:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Solvent Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
SSPC-SP1
Wipe or vapor degrease
Remove oils, greases, waxes
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Remove contaminants that blasting cannot`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: No visible oil residue before blast`

*Box 2 -- Surface Prep (Blast):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Surface Prep` / Subtitle: `Abrasive Blast` (16 pt, `#F0EDE8` at 60%)
- Parameters: `SSPC-SP10 min (IOZ: SP5)` / `Profile: 1.5--3.0 mils` / `ASTM D4417 Method C`
- Purpose: `Expose clean steel, create anchor profile`
- Check: `CRITICAL: Blast within 4-8 hr of priming` (Coral `#E05C5C`)

*Box 3 -- Compressed Air Blow-Down:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Blow-Down` / Subtitle: `Post-Blast Cleaning`
- Parameters: `Oil-free compressed air` / `ASTM D4285 blotter test` / `or vacuum pickup`
- Purpose: `Remove blast residue and dust`
- Check: `Verify air is oil-free -- blotter test mandatory`

*Box 4 -- Pretreatment:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Pretreatment`
- Parameters: `IOZ: NONE (blast profile IS prep)` / `Epoxy: optional iron phosphate` / `Aero: chromate conversion or anodize`
- Purpose: `Depends on primer type -- see comparison`
- Check: `CAUTION: Phosphate under IOZ defeats galvanic protection` (Coral `#E05C5C`)

*Box 5 -- Primer Application:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Primer Application`
- Parameters: `IOZ: 2.5--4.0 mils DFT` / `OZ: 2.0--3.5 mils DFT` / `Epoxy: 1.0--3.0 mils DFT`
- Purpose: `Apply protective primer coat`
- Check: `Continuous agitation -- zinc settles rapidly`

*Box 6 -- Flash / Set Time:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Flash / Set`
- Parameters: `IOZ: 30--60 min (50% RH)` / `OZ (epoxy): per pot life` / `Stripe coat edges first`
- Purpose: `Allow solvent flash-off before cure`
- Check: `CRITICAL: Too thick IOZ = mud cracking` (Coral `#E05C5C`)

*Box 7 -- Cure:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Cure`
- Parameters: `IOZ: 24--72 hr (moisture-dependent)` / `OZ: 7--14 days full cure` / `Epoxy: 7--14 days ambient`
- Purpose: `Develop full cross-link / hardness`
- Check: `IOZ requires moisture (>40% RH) to cure`

*Box 8 -- Inspection & Recoat:*
- Badge: `STAGE 8`, fill `#C8D0D8`
- Name: `Inspection` / Subtitle: `Recoat Readiness`
- Parameters: `DFT: ASTM D7091` / `SSPC-PA 2 acceptance` / `Adhesion: ASTM D4541`
- Purpose: `Verify thickness, adhesion, cure before topcoat`
- Check: `Mist coat required over IOZ before full topcoat`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Prep` |
| `#E8A020` (Amber) | `Pretreatment & Application` |
| `#27AE60` (Emerald) | `Flash & Cure` |
| `#C8D0D8` (Silver) | `Inspection` |

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
- Stage (3.5") | Method/Chemistry (5.5") | Profile/DFT (3.5") | Time (3.0") | Primer Type (3.0") | Key Control (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Method/Chemistry | Profile/DFT | Time | Primer Type | Key Control |
|---|---|---|---|---|---|
| 1. Solvent Clean | SSPC-SP1, wipe/vapor | -- | Per soil load | All | No residue |
| 2. Blast | SSPC-SP10/SP5 | 1.5--3.0 mils | Per spec | IOZ demands SP5 | Profile + cleanliness |
| 3. Blow-Down | Oil-free air / vacuum | -- | Immediate | All | ASTM D4285 |
| 4. Pretreatment | None (IOZ) / optional (epoxy) | -- | -- | IOZ: none; Epoxy: optional | No phosphate under IOZ |
| 5. Application | Airless spray primary | 2.0--4.0 mils | Per coverage | IOZ/OZ/Epoxy | Continuous agitation |
| 6. Flash | Solvent evaporation | -- | 30--60 min | IOZ critical | No mud cracking |
| 7. Cure | Hydrolysis (IOZ) / amine (epoxy) | -- | 24 hr--14 days | Varies | RH > 40% for IOZ |
| 8. Inspection | DFT + adhesion + visual | Per SSPC-PA 2 | -- | All | Mist coat before topcoat |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- IOZ vs. OZ Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> ZINC-RICH PRIMER -- INORGANIC VS. ORGANIC

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Inorganic Zinc (IOZ):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `INORGANIC ZINC (IOZ)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Gold Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Binder | Ethyl silicate (solvent) or alkali silicate (water) |
| Zinc content (dry film) | 75--85% by weight (SSPC-PS 12.01) |
| Target DFT | 2.5--4.0 mils (64--102 um) |
| Surface prep required | SSPC-SP5 White Metal or SP10 Near-White |
| Cure mechanism | Hydrolysis + condensation (needs moisture) |
| Full cure | 24--72 hours (RH-dependent) |
| Salt spray (3 mil alone) | 1,500--3,000+ hours B117 |
| Application | Airless spray; continuous agitation essential |
| Key weakness | Mud cracking if over-applied (> 5 mils) |
| Topcoating | Mist coat required; recoat window 24 hr--30 days |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Best long-term galvanic protection -- the industry standard for bridges, ships, and offshore steel` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Organic Zinc (OZ):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `ORGANIC ZINC (OZ)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Forgiving Alternative` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Binder | Epoxy, polyurethane, or moisture-cure urethane |
| Zinc content (dry film) | 65--80% by weight |
| Target DFT | 2.0--3.5 mils (51--89 um) |
| Surface prep required | SSPC-SP10 minimum |
| Cure mechanism | Binder-dependent (amine, moisture, etc.) |
| Full cure | 7--14 days (epoxy); 24--72 hr (moisture-cure PU) |
| Salt spray (3 mil alone) | 500--1,500 hours B117 |
| Application | Airless, air spray, brush, roll |
| Key advantage | Easier application; brush/roll for field repair |
| Topcoating | Standard recoat; no mist coat needed |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Easier to apply and repair -- preferred for field maintenance and brush/roll touch-up` -- Inter Medium, 13 pt, `#E8A020`

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
| 1 | 0.5" | MUD CRACKING | IOZ applied too thick (> 5 mils) | Reduce DFT to 2.5--4.0 mils; apply thinner coats |
| 2 | 6.33" | POOR ADHESION | Insufficient blast profile or contamination | Re-blast to SP10/SP5; check soluble salts |
| 3 | 12.16" | FLASH RUST | Blast-to-prime delay too long (humidity) | Prime within 4 hr in humid conditions |
| 4 | 18.0" | TOPCOAT BUBBLING | Solvent trapped in porous IOZ film | Apply mist coat first; allow full IOZ cure |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for industrial priming systems. Specific formulations, DFT requirements, and cure conditions vary by product. Consult your coating supplier and applicable specification for application-specific guidance. Source: General industry knowledge; SSPC standards; Watson Research Brief.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Industrial Priming -- Process Flow

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
| Zone 4 - IOZ vs OZ | Section label, two comparison callouts |
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
| `Industrial Priming Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Industrial Priming Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Industrial Priming Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Industrial Priming Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Industrial Priming Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Industrial Priming Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Industrial Priming cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 8 posters (#705--#712) zoom into each stage individually. The IOZ vs. OZ comparison answers the most common question in zinc-rich priming: "inorganic or organic?" The answer depends on service environment -- IOZ for maximum galvanic protection (bridges, offshore), OZ for easier application and field repair.

The key concept that ties this cluster together: zinc-rich primer provides cathodic (sacrificial) protection -- the zinc corrodes preferentially to protect the steel, the same principle as hot-dip galvanizing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #704 -- Construction Workup v1.0*
*2026-04-26*
