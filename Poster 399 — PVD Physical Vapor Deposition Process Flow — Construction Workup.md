---
Project: Plating Posters Inc
Poster Number: 399
Title: "PVD (Physical Vapor Deposition) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD)"
Technical Source: Industry-standard PVD coating process covering magnetron sputtering and cathodic arc evaporation. Values are typical ranges for industrial hard coatings (TiN, TiAlN, CrN) on cutting tools and forming dies.
Process Scope: PVD -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PVD
  - VacuumCoating
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #399 -- Construction Workup
## PVD (Physical Vapor Deposition) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for PVD. It maps the complete 10-stage process from part preparation through final inspection -- every stage visible in a two-row flow diagram. A coating operator sees the full cycle, a process engineer checks parameters, a quality engineer identifies where problems originate. This poster is the "map" that Posters #400--#408 zoom into.

Design philosophy: clean two-row flow diagram as the hero, a compact parameter summary table for quick reference, a "Sputtering vs. Arc" comparison callout, and a common failures quick-hit strip. Dense but scannable -- the operator's wall reference for the entire PVD line.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a two-row flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box is color-coded by stage type. Arrows are simple right-pointing (top row) and left-pointing (bottom row) connectors with a vertical link between rows. Straightforward geometry.

2. **Parameter summary table (Block D):** A compact 10-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Sputtering vs. Arc" comparison callout (Block E):** Two side-by-side callout boxes comparing magnetron sputtering vs. cathodic arc evaporation. Established pattern from Poster #31.

4. **Common failures quick-hit strip (Block F):** A horizontal strip of 4 common failures with one-line fixes.

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
| Amber | `#E8A020` | Vacuum & parameter stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & preparation stages, structural positives |
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
  Block B: Ten-stage two-row flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 4 -- SPUTTERING VS. ARC COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Sputtering vs. Arc side-by-side callout

ZONE 5 -- COMMON FAILURES QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-failure strip with one-line fixes

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

> PHYSICAL VAPOR DEPOSITION (PVD)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 34 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Complete Process Flow -- 10 Stages from Cleaning to Final Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Thin-film hard coatings deposited in vacuum -- TiN, TiAlN, CrN, and DLC on cutting tools, dies, and wear components. Base vacuum below 5 x 10^-5 Torr. Hang this poster at the PVD bay entrance.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PVD CYCLE -- STAGE BY STAGE

---

**BLOCK B -- Ten-Stage Two-Row Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Two rows of five boxes.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.3". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1--5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Part Preparation | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Cleaning | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Fixturing & Loading | Box 3 | 9.7" | `#2EC4B6` (Teal) | Loading |
| 4. Vacuum Pump-Down | Box 4 | 14.3" | `#E8A020` (Amber) | Equipment |
| 5. Ion Etching | Box 5 | 18.9" | `#E8A020` (Amber) | Parameter |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.1", Y: 8.3" (bottom center Box 5)
- To: X: 21.1", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6--10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Deposition | Box 6 | 18.9" | `#27AE60` (Emerald) | Deposition |
| 7. Cooling | Box 7 | 14.3" | `#E8A020` (Amber) | Post-Treatment |
| 8. Unloading | Box 8 | 9.7" | `#2EC4B6` (Teal) | Handling |
| 9. Inspection & QA | Box 9 | 5.1" | `#27AE60` (Emerald) | Quality |
| 10. Packaging/Release | Box 10 | 0.5" | `#27AE60` (Emerald) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Part Preparation:*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Part Preparation`

Key parameters:
- JetBrains Mono Regular, 12 pt, `#F0EDE8`, line height 160%
```
Deburr / edge prep
Mask if required
Verify substrate type
```

Purpose:
- Inter Regular, 12 pt, `#F0EDE8` at 70%
- Text: `Ensure parts ready for cleaning -- no burrs, sharp edges radiused`

Critical check:
- Inter Medium, 11 pt, `#2EC4B6`
- Text: `CHECK: Substrate temp rating vs. coating temp`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Ultrasonic alkaline 50-70 C` / `Acetone/IPA rinse` / `DI water final rinse` / `Hot-air or vacuum dry`
- Purpose: `Remove oils, particulate, fingerprints -- #1 cause of PVD failure`
- Check: `CRITICAL: No water spots, no fingerprints` (`#E05C5C`)

*Box 3 -- Fixturing & Loading:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Fixturing & Loading`
- Parameters: `Nitrile gloves mandatory` / `Planetary rotation fixtures` / `Parts spaced for line-of-sight`
- Purpose: `Position parts for uniform coating coverage`
- Check: `Finger oils = delamination -- handle only with gloves`

*Box 4 -- Vacuum Pump-Down:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Vacuum Pump-Down`
- Parameters: `Rough pump to ~50 mTorr` / `Turbo/cryo to < 5 x 10^-5 Torr` / `30-90 min typical`
- Purpose: `Remove air and water vapor -- establish clean deposition environment`
- Check: `Leak rate < 2 mTorr/min; check O-rings if slow`

*Box 5 -- Ion Etching:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Ion Etching`
- Parameters: `Ar+ bombardment` / `Bias: -800 to -1200 V` / `1-5 mTorr, 5-30 min`
- Purpose: `Remove surface oxides, activate surface for adhesion`
- Check: `CAUTION: High voltage -- interlock must be engaged` (`#E05C5C`)

*Box 6 -- Deposition:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Deposition`
- Parameters: `Sputtering or arc` / `Bias: -50 to -300 V` / `200-500 C substrate` / `1-5 um/hr rate`
- Purpose: `Deposit hard coating (TiN, TiAlN, CrN, DLC)`
- Check: `Monitor reactive gas ratio for stoichiometry`

*Box 7 -- Cooling:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Cooling`
- Parameters: `Controlled cool-down in vacuum` / `30-120 min to < 150 C` / `Inert gas backfill optional`
- Purpose: `Prevent thermal shock and oxidation of fresh coating`
- Check: `Do not vent to air above 150 C -- oxidation risk`

*Box 8 -- Unloading:*
- Badge: `STAGE 8`, fill `#2EC4B6`
- Name: `Unloading`
- Parameters: `Heat-resistant gloves` / `Parts may be 100-200 C` / `Visual color check`
- Purpose: `Remove coated parts from chamber`
- Check: `CAUTION: Hot surfaces -- burn hazard` (`#E05C5C`)

*Box 9 -- Inspection & QA:*
- Badge: `STAGE 9`, fill `#27AE60`
- Name: `Inspection & QA`
- Parameters: `Color verification` / `Adhesion test (VDI 3198)` / `Thickness (calotest / XRF)`
- Purpose: `Verify coating quality before release`
- Check: `HF1-HF4 acceptable; HF5-HF6 reject`

*Box 10 -- Packaging / Release:*
- Badge: `STAGE 10`, fill `#27AE60`
- Name: `Packaging / Release`
- Parameters: `Soft wrap or tray` / `Document lot number` / `Certificate of conformance`
- Purpose: `Protect coated parts for shipment`
- Check: `Match coating color to spec reference`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Handling` |
| `#E8A020` (Amber) | `Equipment & Parameters` |
| `#27AE60` (Emerald) | `Deposition & Quality` |
| `#E05C5C` (Coral) | `Caution / Safety` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 10-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Key Spec (5.5") | Temperature (3.0") | Time (3.0") | Pressure/Voltage (4.0") | Key Control (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Stage | Key Spec | Temp | Time | Pressure/Voltage | Key Control |
|---|---|---|---|---|---|
| 1. Part Prep | Per substrate | Ambient | -- | -- | Edge prep, masking |
| 2. Cleaning | Alk + solvent + DI | 50-70 C (alk) | 5-15 min/step | -- | Water-break-free |
| 3. Fixturing | Planetary rotation | Ambient | -- | -- | Line-of-sight spacing |
| 4. Pump-Down | Rough + turbo/cryo | Ambient | 30-90 min | < 5 x 10^-5 Torr | Leak check |
| 5. Ion Etch | Ar+ bombardment | 200-400 C | 5-30 min | -800 to -1200 V bias | Oxide removal |
| 6. Deposition | TiN / TiAlN / CrN | 200-500 C | 1-4 hr | 1-10 mTorr working | Gas ratio control |
| 7. Cooling | In-vacuum cool | 500 -> < 150 C | 30-120 min | Maintain vacuum | No premature venting |
| 8. Unloading | Visual color check | < 200 C | -- | Atmospheric | Hot surface PPE |
| 9. Inspection | VDI 3198 / calotest | Ambient | -- | -- | HF1-HF4 pass |
| 10. Release | Lot documentation | Ambient | -- | -- | Cert of conformance |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Sputtering vs. Arc Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> SPUTTERING VS. ARC -- WHICH PVD METHOD?

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Magnetron Sputtering:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `MAGNETRON SPUTTERING` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `The Precision Method` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Power | DC 300-1000 V, 1-20 A |
| Working pressure | 1-10 mTorr |
| Ionization | ~5% of flux ionized |
| Deposition rate | 0.5-2 um/hr (lower) |
| Film quality | Very smooth, low defects |
| Macroparticles | None |
| Best for | Decorative, precision optics |
| Insulating targets | RF sputtering (13.56 MHz) |
| Uniformity | Excellent with rotation |
| Limitation | Lower adhesion energy |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Smoother films, better control -- preferred for decorative and optical coatings` -- Inter Medium, 13 pt, `#2EC4B6`

**Right -- Cathodic Arc Evaporation:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CATHODIC ARC EVAPORATION` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `The Workhorse Method` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Power | 20-40 V, 50-200 A per cathode |
| Working pressure | 5-50 mTorr |
| Ionization | 50-100% of flux ionized |
| Deposition rate | 2-6 um/hr (higher) |
| Film quality | Dense, high adhesion |
| Macroparticles | Present (droplets) |
| Best for | Cutting tools, wear parts |
| Insulating targets | Not compatible (DC only) |
| Uniformity | Good with rotation |
| Limitation | Macroparticle defects |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Higher ionization = denser films and better adhesion -- the standard for industrial tooling` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 5 -- Common Failures Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PVD FAILURES

---

**BLOCK F -- Four Failure Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DELAMINATION | Poor cleaning or inadequate ion etch | Rigorous clean protocol; verify -800 V min bias |
| 2 | 6.33" | NON-UNIFORM THICKNESS | No rotation or fixture shadowing | Check planetary drive; re-fixture parts |
| 3 | 12.16" | WRONG COLOR | Incorrect reactive gas ratio | Verify MFC calibration; check N2/Ar ratio |
| 4 | 18.0" | MACROPARTICLES | Arc current too high (arc process) | Reduce arc current; use filtered arc |

Interior per card:
- Failure: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for PVD hard coatings. Specific equipment settings, gas ratios, and cycle recipes vary by system manufacturer and coating type. Consult your equipment supplier and coating specification for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> PVD (Physical Vapor Deposition) -- Process Flow

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
| Zone 2 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 10-row table |
| Zone 4 - Sputtering vs Arc | Section label, two comparison callouts |
| Zone 5 - Common Failures | Section label, four failure cards |
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
| `PVD Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PVD Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PVD Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `PVD Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PVD Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `PVD Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire PVD cluster. The flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The remaining 9 posters (#400--#408) zoom into each stage individually. The sputtering vs. arc comparison answers the most common question in PVD coating: "which deposition method?" The answer depends on application -- arc for tooling (adhesion), sputtering for decorative (smoothness). Total cycle time is typically 3-8 hours including pump-down, heating, etching, deposition, and cooling.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #399 -- Construction Workup v1.0*
*2026-04-26*
