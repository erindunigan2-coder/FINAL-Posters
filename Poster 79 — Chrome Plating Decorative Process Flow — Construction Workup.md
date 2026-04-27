---
Project: Plating Posters Inc
Poster Number: 79
Title: "Chrome Plating (Decorative) -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-07 technical reference (decorative chrome plating)"
Technical Source: Industry-standard decorative chrome plating process. Covers the complete 8-stage sequence from cleaning through post-treatment. Modern decorative chrome is predominantly trivalent (Cr III) -- positioned as current industry standard with hexavalent noted as legacy. Always plated over nickel (or copper + nickel).
Process Scope: Decorative chrome plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ChromePlating
  - Decorative
  - Trivalent
  - ProcessFlow
  - ConstructionWorkup
  - ClusterEP07
---

# Poster #79 -- Construction Workup
## Chrome Plating (Decorative) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-07: Chrome Plating (Decorative). It shows the complete 8-stage process sequence at a glance -- every stage visible in one U-flow diagram. Decorative chrome is always the final layer in a multi-layer system: copper (leveling) -> nickel (corrosion barrier) -> chrome (aesthetic/hard surface). The chrome itself is extremely thin (0.1-0.75 microns) -- the nickel underneath does most of the corrosion work. This poster makes that system context explicit.

Modern decorative chrome is predominantly trivalent (Cr III), driven by RoHS/REACH regulation. Hexavalent (Cr VI) decorative lines still exist, especially older installations, but trivalent is the current industry standard and is positioned as such throughout this cluster.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a hex vs. tri comparison callout, and a troubleshooting quick-hit strip. Dense but scannable -- the foreman's wall reference for the entire decorative chrome line.

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

2. **Parameter summary table (Block D):** A compact 8-row table (one row per stage) with key parameters. Standard alternating-row construction.

3. **"Hex vs. Tri" comparison callout (Block E):** Two side-by-side callout boxes comparing hexavalent vs. trivalent decorative chrome. Critical for regulatory context.

4. **Troubleshooting quick-hit strip (Block F):** A horizontal strip of 4 common problems with one-line fixes.

5. **Multi-layer system callout (Block C2):** Small callout beneath the legend showing the Cu -> Ni -> Cr layer stack.

6. **Regulatory banner:** Prominent amber banner noting RoHS/REACH status and trivalent as current standard.

7. **4 pt left-border accents on callout boxes.**

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
  Block A: Headline + subheading + tagline + regulatory banner

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip
  Block C2: Multi-layer system callout (Cu -> Ni -> Cr)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- HEX VS. TRI COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Hexavalent vs. Trivalent side-by-side callout

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

> CHROME PLATING (DECORATIVE)

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 32 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Final Finish

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.1"
- Width: 16.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> The thinnest plating layer with the biggest visual impact. Always over nickel. Trivalent is the modern standard.

**BLOCK A -- Regulatory Banner**

- Position: X: 17.0". Y: 2.0"
- Width: 6.5". Height: 0.7"
- Rounded rect, fill `#E8A020` at 15%, border 1 pt `#E8A020`, radius 4
- Text: `TRIVALENT (Cr III) = CURRENT INDUSTRY STANDARD` -- Barlow SemiBold, 13 pt, `#E8A020`
- Sub-text: `RoHS/REACH compliant` -- Inter Regular, 11 pt, `#E8A020` at 70%

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
| 1. Clean (Nickel Surface) | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Activation) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Chrome) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

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
| 5. Chrome Plate (Main Tank) | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Chrome) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post-Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Dry / Final Inspection | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Clean (Nickel Surface):*

Stage badge (top-left inside box):
- Rounded rect, 1.2" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Position: X: box left + 0.3", Y: box top + 0.6"

Stage name:
- Barlow SemiBold, 22 pt, `#F0EDE8`
- Text: `Clean`

Key parameters:
- JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%
```
Nickel surface must be active
No separate tank -- minimal delay
<30 sec from Ni rinse to Cr
```

Purpose:
- Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text: `Ensure nickel is not passivated before chrome`

Critical check:
- Inter Medium, 12 pt, `#2EC4B6`
- Text: `CHECK: Parts must not dry between Ni and Cr`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation` (16 pt, `#F0EDE8` at 60%)
- Parameters: `Single rinse, ambient` / `Minimize dwell time`
- Purpose: `Remove nickel drag-out`
- Check: `Speed is everything -- nickel passivates in air`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `Mild acid: 1--5% H2SO4 or 1--3% HCl` / `Ambient, 10--30 sec` / `Or: initial seconds in chrome bath`
- Purpose: `Remove nickel passive film for chrome adhesion`
- Check: `Many lines skip separate tank -- activate in the chrome bath itself`

*Box 4 -- Rinse (Pre-Chrome):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Chrome`
- Parameters: `Single rinse if separate activation` / `Ambient temp`
- Purpose: `Remove acid before chrome immersion`
- Check: `Optional if activating in-tank`

*Box 5 -- Chrome Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Chrome Plate` / Subtitle: `Main Tank`
- Parameters (trivalent focus): `Cr3+: 4--8 g/L` / `pH 2.5--4.0` / `80--120 F (27--49 C)` / `50--200 ASF`
- Purpose: `Deposit thin, brilliant chrome over nickel`
- Check: `Thickness: 0.15--0.50 microns (Cr III)`

*Box 6 -- Rinse (Post-Chrome):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Chrome`
- Parameters: `Multi-stage, flowing` / `Ambient temp`
- Purpose: `Remove chrome drag-out`
- Check: `CRITICAL: Cr(VI) in drag-out is hazardous waste` (Coral `#E05C5C`)

*Box 7 -- Post-Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post-Treatment`
- Parameters: `Anti-tarnish dip (optional)` / `Hot DI water rinse` / `Ambient--160 F`
- Purpose: `Enhance tarnish resistance, improve appearance`
- Check: `Not always required -- depends on end-use spec`

*Box 8 -- Dry / Final Inspection:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Dry / Inspect`
- Parameters: `Forced air or oven` / `120--150 F` / `Visual + thickness check`
- Purpose: `Remove moisture, verify finish quality`
- Check: `Measure total system thickness (Cu+Ni+Cr)`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.0"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.6", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Chrome Plating (Main Tank)` |
| `#E05C5C` (Coral) | `Caution / Hazard` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

**BLOCK C2 -- Multi-Layer System Callout**

Y: 15.0" to 15.4"

- Rounded rectangle, X: 0.5", W: 23.0", H: 0.35", fill `#1E2435`, radius 4
- Text (centered): `THE DECORATIVE CHROME SYSTEM: Copper (leveling) -> Nickel (corrosion barrier) -> Chrome (aesthetic + hardness)` -- Inter Medium, 13 pt, `#E8A020`
- Sub-text: `The chrome is 0.1--0.75 microns. The nickel does the heavy lifting.` -- Inter Regular, 11 pt, `#F0EDE8` at 60%

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS (TRIVALENT FOCUS)

---

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | Current Density (3.0") | Key Control (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Ensure Ni surface active | Ambient | Minimal | -- | No drying between Ni and Cr |
| 2. Rinse | DI or city water | Ambient | 15--30 sec | -- | Speed -- Ni passivates fast |
| 3. Activation | 1--5% H2SO4 or in-tank | Ambient | 10--30 sec | -- | Remove Ni passive film |
| 4. Rinse | DI or city water | Ambient | 15--30 sec | -- | Optional if in-tank activation |
| 5. Chrome Plate | Cr3+ 4--8 g/L, pH 2.5--4.0 | 80--120 F | 2--8 min | 50--200 ASF | Thickness 0.15--0.50 um |
| 6. Rinse | DI or city water | Ambient | 30--60 sec | -- | Multi-stage for Cr recovery |
| 7. Post-Treatment | Anti-tarnish (optional) | Ambient--160 F | 15--60 sec | -- | Per end-use specification |
| 8. Dry/Inspect | -- | 120--150 F | 5--10 min | -- | Total system thickness check |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- Hex vs. Tri Comparison

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> HEXAVALENT VS. TRIVALENT -- KNOW THE DIFFERENCE

---

**BLOCK E -- Side-by-Side Comparison**

Y: 22.9" to 28.3".

**Left -- Trivalent Chrome (Cr III):**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `TRIVALENT CHROME (Cr III)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `The Modern Standard` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Chemistry | Cr(III) sulfate or chloride based |
| Concentration | 4--8 g/L as Cr3+ |
| pH | 2.5--4.0 |
| Temperature | 80--120 F (27--49 C) |
| CD | 50--200 ASF |
| Cathode efficiency | 15--30% |
| Deposit color | Slightly warmer than hex |
| Thickness | 0.15--0.50 microns |
| Anodes | Graphite or MMO on titanium |
| Regulatory | RoHS/REACH compliant |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Automotive OEMs increasingly mandate trivalent. No carcinogenic Cr(VI) mist.` -- Inter Medium, 13 pt, `#27AE60`

**Right -- Hexavalent Chrome (Cr VI):**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.2", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `HEXAVALENT CHROME (Cr VI)` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `Legacy -- Still in Service` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Chemistry | CrO3 (chromic acid) + H2SO4 catalyst |
| Concentration | 200--400 g/L CrO3 |
| CrO3:SO4 ratio | 100:1 to 150:1 (CRITICAL) |
| Temperature | 95--120 F (35--49 C) |
| CD | 100--300 ASF |
| Cathode efficiency | 10--18% |
| Deposit color | Brilliant blue-white |
| Thickness | 0.25--0.75 microns |
| Anodes | Lead or lead-tin alloy (93:7) |
| Regulatory | RESTRICTED -- RoHS/REACH |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `OSHA PEL 5 ug/m3. Known carcinogen (IARC Group 1). Enclosed ventilation required.` -- Inter Medium, 13 pt, `#E05C5C`

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
| 1 | 0.5" | DULL / MILKY CHROME | CrO3:SO4 ratio off, Cr3+ too high, temp too low | Check ratio; dummy plate to reduce Cr3+ |
| 2 | 6.33" | CHROME PEELING | Nickel passivated before chrome immersion | Minimize Ni-to-Cr transfer time; improve activation |
| 3 | 12.16" | BURNING | CD too high for temperature, poor racking | Reduce CD; check temp-CD bright range |
| 4 | 18.0" | PITTING | Nickel pitting transferred through thin chrome | Fix nickel first; check wetting agent |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for decorative chrome plating (trivalent focus). Hexavalent chrome is a known human carcinogen -- comply with all OSHA, EPA, RoHS, and REACH requirements. Specific formulations and process limits vary by proprietary product. Consult your process supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Chrome Plating (Decorative) -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline, regulatory banner |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip, multi-layer callout |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Hex vs Tri | Section label, two comparison callouts |
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
| `Chrome Decorative Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chrome Decorative Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chrome Decorative Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Chrome Decorative Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chrome Decorative Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Chrome Decorative Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the entire Decorative Chrome cluster. The key message: decorative chrome is a system, not a standalone process. Copper -> Nickel -> Chrome. The chrome itself is thinner than a sheet of paper. The hex vs. tri comparison is front-and-center because this is the defining industry transition in decorative chrome right now. Every flow box in the hero should be readable at 6 feet. The regulatory banner in Zone 1 sets the tone immediately -- this is not a poster that pretends hex chrome does not exist, but it clearly positions trivalent as the path forward.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #79 -- Construction Workup v1.0*
*2026-04-26*
