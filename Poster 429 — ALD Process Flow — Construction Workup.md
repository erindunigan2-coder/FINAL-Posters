---
Project: Plating Posters Inc
Poster Number: 429
Title: "ALD -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD)"
Technical Source: Industry-standard ALD (atomic layer deposition) process. Self-limiting surface reactions deposit films one atomic layer (~0.1 nm) per cycle. Alternating precursor pulses separated by purge steps give angstrom-level thickness control and 100% conformality on high-aspect-ratio structures. Covers the complete 10-stage sequence.
Process Scope: ALD -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ALD
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #429 -- Construction Workup
## ALD -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for ALD. It maps the complete 10-stage process at a glance -- every stage visible in a two-row flow diagram. ALD is the precision instrument of thin film deposition: self-limiting reactions, digital thickness control by cycle count, and conformal coating of features that no other method can reach. This poster is the "map" that the other 9 posters (#430--#438) zoom into.

Design philosophy: two-row U-flow diagram as the hero, a compact parameter summary table, a "What Makes ALD Different?" comparison callout (ALD vs. CVD vs. PVD), and a troubleshooting quick-hit strip. Dense but scannable.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box color-coded by stage type.
2. **Parameter summary table (Block D):** A compact 10-row table (one per stage) with key parameters.
3. **"What Makes ALD Different?" comparison callout (Block E):** ALD vs. CVD vs. PVD comparison.
4. **Troubleshooting quick-hit strip (Block F):** 4 common ALD problems with one-line fixes.
5. **4 pt top-border accents on flow boxes.**
6. **Global Colors / swatch remap for Light edition.**

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
| Amber | `#E8A020` | Equipment stages, safety/pyrophoric accents |
| Teal | `#2EC4B6` | Preparation & cleaning stages |
| Emerald | `#27AE60` | Deposition/cycling stages, optimal reference |
| Coral | `#E05C5C` | Problems, defects, safety hazards |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents, post-process |

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
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 10-row parameter table (one row per stage)

ZONE 4 -- WHAT MAKES ALD DIFFERENT? (22.0"--28.5" / ~6.5" tall)
  Block E: ALD vs. CVD vs. PVD comparison

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

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> ATOMIC LAYER DEPOSITION (ALD)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 34 pt, `#2EC4B6` (Teal)

> Complete Process Flow -- 10 Stages from Substrate Prep to Inspection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%

> Self-limiting surface reactions. One atomic layer per cycle. Angstrom-level control on any geometry -- the ultimate precision coating.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Ten-Stage U-Flow Diagram**

Y: 3.8" to 14.0" (~10.2" tall). Two rows of five boxes in a U-flow pattern.

Each flow box:
- Rounded rectangle, W: 4.2", H: 4.5", fill `#1E2435`, corner radius 8
- Top border accent: 4 pt colored strip

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Substrate Prep | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Cleaning | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Loading | Box 3 | 9.7" | `#C8D0D8` (Silver) | Fixturing |
| 4. Reactor Setup | Box 4 | 14.3" | `#E8A020` (Amber) | Equipment |
| 5. Cycle Programming | Box 5 | 18.9" | `#E8A020` (Amber) | Equipment |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right. Y: ~6.1"

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.3". To: X: 21.0", Y: 9.5"

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Deposition Cycles | Box 6 | 18.9" | `#27AE60` (Emerald) | Core Process |
| 7. In-Situ Monitoring | Box 7 | 14.3" | `#E8A020` (Amber) | Quality |
| 8. Final Purge & Cooldown | Box 8 | 9.7" | `#C8D0D8` (Silver) | Post-Process |
| 9. Unloading | Box 9 | 5.1" | `#C8D0D8` (Silver) | Post-Process |
| 10. Inspection & QA | Box 10 | 0.5" | `#E8A020` (Amber) | Quality |

**Arrows between bottom-row boxes:** Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Substrate Prep:*
- Badge: `STAGE 1`, fill `#2EC4B6`, text `#1A1F2E`, 14 pt
- Name: `Substrate Preparation`
- Parameters:
```
RCA clean (semiconductor)
UV-ozone or O2 plasma (metals)
Surface functionalization (-OH groups)
```
- Purpose: `Create nucleation sites for first ALD precursor`
- Check: `Hydrophilic surface = good nucleation`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Wet chemical clean` / `or plasma activation` / `DI rinse + dry`
- Purpose: `Remove organics, particles, and native oxides`
- Check: `Carbon contamination blocks ALD nucleation`

*Box 3 -- Loading:*
- Badge: `STAGE 3`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Loading`
- Parameters: `Place on heated susceptor` / `Close reactor` / `Pump to base pressure`
- Purpose: `Secure substrate in reactor at ALD temperature`
- Check: `CHECK: Substrate temperature stable before cycling`

*Box 4 -- Reactor Setup:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Reactor Setup`
- Parameters: `Base pressure 0.1--10 Torr` / `Precursor lines heated` / `Carrier gas flowing (N2/Ar)`
- Purpose: `Prepare reactor for ALD cycling`
- Check: `Verify precursor delivery -- bubblers at setpoint temp`

*Box 5 -- Cycle Programming:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Cycle Programming`
- Parameters: `Set pulse times (0.015--0.2 sec)` / `Set purge times (5--30 sec)` / `Set cycle count for target thickness`
- Purpose: `Program the recipe -- N cycles = N x GPC thickness`
- Check: `CAUTION: TMA is PYROPHORIC -- verify inert atmosphere` (Coral `#E05C5C`)

*Box 6 -- Deposition Cycles:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Deposition Cycles`
- Parameters: `Precursor A pulse -> Purge -> Precursor B pulse -> Purge` / `Repeat N cycles` / `~0.1 nm/cycle (Al2O3)`
- Purpose: `Build film one atomic layer at a time`
- Check: `Self-limiting: thickness = cycles x GPC`

*Box 7 -- In-Situ Monitoring:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `In-Situ Monitoring`
- Parameters: `Ellipsometry (thickness per cycle)` / `QCM (mass gain per cycle)` / `Verify GPC matches target`
- Purpose: `Confirm self-limiting growth in real time`
- Check: `GPC drift = precursor delivery or temperature problem`

*Box 8 -- Final Purge & Cooldown:*
- Badge: `STAGE 8`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Final Purge & Cooldown`
- Parameters: `Extended N2/Ar purge` / `Heater off or ramp down` / `Cool to < 80 degC`
- Purpose: `Remove residual precursors; prevent oxidation`
- Check: `Do NOT vent hot -- oxidation degrades film surface`

*Box 9 -- Unloading:*
- Badge: `STAGE 9`, fill `#C8D0D8`, text `#1A1F2E`
- Name: `Unloading`
- Parameters: `Vent to atmosphere (N2)` / `Open reactor` / `Handle with clean gloves`
- Purpose: `Remove coated substrates without contamination`
- Check: `Inspect reactor for precursor residue buildup`

*Box 10 -- Inspection & QA:*
- Badge: `STAGE 10`, fill `#E8A020`
- Name: `Inspection & QA`
- Parameters: `Ellipsometry (thickness + n)` / `XRR (density + roughness)` / `SEM cross-section (conformality)`
- Purpose: `Verify film meets specification`
- Check: `Non-uniformity < 1% for semiconductor; conformality > 95%`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3".

Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4.

Five legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Cleaning` |
| `#C8D0D8` (Silver) | `Fixturing & Post-Process` |
| `#E8A020` (Amber) | `Equipment Setup & QA` |
| `#27AE60` (Emerald) | `Deposition Cycles (Core Process)` |
| `#E05C5C` (Coral) | `Safety / Caution` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

**BLOCK D -- 10-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Key Action (5.0") | Temperature / Pressure (4.5") | Time (3.0") | Key Control (7.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.5".

| Stage | Key Action | Temp / Pressure | Time | Key Control |
|---|---|---|---|---|
| 1. Substrate Prep | Clean, functionalize surface | Ambient | 10--60 min | -OH surface groups present |
| 2. Cleaning | Wet clean or plasma activation | 75--80 degC (RCA) | 10--30 min | No carbon contamination |
| 3. Loading | Mount, pump down, heat | ALD temp / 0.1--10 Torr | 15--60 min | Temperature stable |
| 4. Reactor Setup | Precursor lines, carrier gas | 150--300 degC | 10--20 min | Bubbler temps at setpoint |
| 5. Cycle Programming | Set pulse, purge, count | -- | 5 min | TMA interlocks verified |
| 6. Deposition Cycles | A-purge-B-purge x N | 150--300 degC / 0.1--10 Torr | 25--100 min (10 nm) | GPC matches literature |
| 7. Monitoring | Ellipsometry / QCM | -- | Continuous | GPC stable cycle-to-cycle |
| 8. Purge & Cool | Extended purge, cool down | Cool to < 80 degC | 15--30 min | No hot venting |
| 9. Unloading | Vent, remove substrates | Ambient | 5--10 min | Clean gloves |
| 10. Inspection | Ellipsometry, XRR, SEM | Ambient | 15--60 min | Non-uniformity < 1% |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- What Makes ALD Different?

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHAT MAKES ALD DIFFERENT? -- ALD VS. CVD VS. PVD

**BLOCK E -- Three-Way Comparison**

Y: 22.9" to 28.3". Three panels side by side.

**Left -- ALD (X: 0.5", W: 7.33"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`, 0.06"
- Title: `ALD` -- Barlow SemiBold, 22 pt, `#27AE60`
- Subtitle: `The Precision Instrument` -- 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Thickness control | +/- 0.1 nm (by cycle count) |
| Conformality | 100% (any aspect ratio) |
| Temperature | 50--400 degC |
| Rate | Slow (0.1 nm/cycle) |
| Films | Al2O3, HfO2, TiO2, ZrO2, ZnO, TiN, SiO2 |
| Mechanism | Self-limiting surface reactions |

Highlight: `Digital thickness control. Every cycle = one layer. No geometry limitations.` -- `#27AE60`

**Center -- CVD (X: 8.17", W: 7.33"):**
- Left accent `#E8A020`
- Title: `CVD / PECVD` -- Barlow SemiBold, 22 pt, `#E8A020`
- Subtitle: `The Workhorse` -- 14 pt

| Property | Value |
|---|---|
| Thickness control | +/- 5--10% (time-based) |
| Conformality | Good (PECVD) to Excellent (LPCVD) |
| Temperature | 25--1100 degC |
| Rate | Fast (10--200 nm/min) |
| Films | SiO2, Si3N4, poly-Si, DLC, TiN, W |
| Mechanism | Continuous chemical reaction |

Highlight: `High throughput. Versatile. But no self-limiting control.` -- `#E8A020`

**Right -- PVD (X: 15.83", W: 7.67"):**
- Left accent `#2EC4B6`
- Title: `PVD (SPUTTERING)` -- Barlow SemiBold, 22 pt, `#2EC4B6`
- Subtitle: `The Physical Method` -- 14 pt

| Property | Value |
|---|---|
| Thickness control | +/- 5--20% |
| Conformality | Poor (line-of-sight) |
| Temperature | 25--500 degC |
| Rate | Medium (0.5--5 um/hr) |
| Films | TiN, CrN, TiAlN, Al, Cu, metals |
| Mechanism | Physical transfer from target |

Highlight: `Hard coatings, metals. Fast. But poor on 3D geometry.` -- `#2EC4B6`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON ALD PROBLEMS

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".
Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | GPC TOO HIGH | Insufficient purge -- precursors overlap (CVD mode) | Increase purge time; verify pump speed |
| 2 | 6.33" | ISLAND GROWTH | Surface lacking -OH nucleation sites | O2 plasma or UV-ozone surface treatment |
| 3 | 12.16" | THICKNESS NON-UNIFORM | Temperature gradient in reactor | Improve heater uniformity; calibrate zones |
| 4 | 18.0" | HIGH CARBON IN FILM | Low temperature or short purge | Increase temp (within ALD window); extend purge; use plasma-ALD |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for ALD thin film deposition. Specific recipes, precursor systems, and cycle parameters vary by equipment and application. Consult your equipment manufacturer for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> ALD -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 10-row table |
| Zone 4 - ALD Comparison | Section label, three comparison panels |
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
| `ALD Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `ALD Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `ALD Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `ALD Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `ALD Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `ALD Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire ALD cluster. The U-flow diagram must be readable at 6 feet -- large boxes, clear arrows, bold stage numbers. The three-way ALD vs. CVD vs. PVD comparison is the most important educational element: it answers "why would I use a process this slow?" The answer is precision and conformality -- ALD does what no other method can do on high-aspect-ratio structures.

The self-limiting nature of ALD is THE concept to communicate. Every cycle deposits exactly one sub-monolayer regardless of exposure time, gas flow pattern, or substrate geometry. That is why ALD achieves 100% conformality and +/- 0.1 nm control. This poster should make that concept viscerally clear.

---

*Alaina -- Poster #429 -- Construction Workup v1.0 -- 2026-04-26*
