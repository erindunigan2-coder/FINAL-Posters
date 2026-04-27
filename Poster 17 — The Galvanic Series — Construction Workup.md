---
Project: Plating Posters Inc
Poster Number: 17
Title: "The Galvanic Series — Why Metals Corrode in Contact"
Document Type: Construction Workup
Status: v2.0 — Ready for Elara
Created: 2026-04-06T00:00:00
Updated: 2026-04-07T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 17)"
Technical Source: Watson research brief (galvanic series in seawater, EMF series, four components of a galvanic cell, anodic vs. cathodic protection)
Watson Flags: ONE OPEN — Confirm exact potential values for the full galvanic series chart against an authoritative source (NACE / ASM Handbook). Non-blocking; values used are general industry-accepted ranges.
Tyler Flags: NONE
v2 Changelog:
  - Sharpened the Block C key takeaway to use Watson's exact framing ("Eliminate any one to stop corrosion") and made it the visual focal point of the cell illustration.
  - Tightened chart footnote to clearly identify the values as reference-grade (relative comparison) rather than absolute laboratory values.
  - Added an explicit "reference data" disclaimer line above the chart to set expectations.
  - No layout, dimensions, or palette changes — drop-in replacement for v1.0.
Process Scope: Corrosion fundamentals (universal — applies to every plated assembly)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GalvanicSeries
  - Corrosion
  - ConstructionWorkup
---

# Poster # Poster #17 — Construction Workup
## The Galvanic Series — Why Metals Corrode in Contact

*Alaina — Plating Posters Inc Creative Lead*
*v2.0 — 2026-04-07 (v1.0 issued 2026-04-06)*

This document is the construction workup for Poster #17. The hero element is a large vertical galvanic series chart — the kind of reference data engineers look up constantly but never have on the wall. This poster is the conceptual backbone behind Posters #6 (Passivation), #7 (Metallic Contamination), and a planned future poster on Corrosion Testing. One Watson flag remains open (chart values verification) — non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**v2 refresh notes:** The cell-illustration takeaway now uses Watson's exact framing, the chart footnote and a new sub-label make it explicit that these are reference-grade comparison values (not lab-precision measurements), and a small "reference data" disclaimer was added above the chart. No layout, dimensions, or palette have changed.

**Content source:** Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 17), supplemented by general industry galvanic series data.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for the galvanic series chart bars, callout boxes, and accent borders
- Line elements with arrowheads for galvanic cell illustration
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Galvanic series chart (Block B — HERO):** The chart is the dominant visual. Built as a vertical stack of horizontal bar segments — one bar per metal/alloy. Each bar's color reflects its position on the gradient (Coral for active/anodic top → Amber middle → Emerald for noble/cathodic bottom). Each bar carries the metal name (left), potential value (right). This is straightforward in the design but requires careful vertical alignment of ~16 bars.

2. **Galvanic cell illustration (Block D):** Four-component diagram — anode block, cathode block, electronic path (wire arc), ionic path (electrolyte arrow). Built from rectangles and lines. The "Eliminate any one to stop corrosion" callout is the conceptual hook.

3. **Anodic vs. cathodic example panels (Block E):** Two side-by-side cross-sections — Zn-on-steel (zinc corrodes sacrificially) and Ni-on-steel (steel corrodes through pores). Built as layered rectangles with labels and arrows.

4. **4 pt left-border accents on callout boxes:** Same technique as all previous posters — narrow colored rectangle (~0.06" wide) flush against the left edge of each callout box.

5. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Light edition requires duplicating the page and manually recoloring per the remap table in Part 6. The galvanic series chart gradient is the most labor-intensive recolor — plan for it.

6. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** Substitute Courier Prime if unavailable.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org (if not already uploaded from previous posters):
- **Barlow Condensed ExtraBold** — all headlines and section labels
- **Barlow SemiBold** — all subheadings, callout titles
- **Inter Regular** and **Inter Medium** — all body text and metal names
- **JetBrains Mono Regular** — all potential values and version number

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Mid-galvanic-series bars, neutral metals |
| Teal | `#2EC4B6` | Galvanic cell illustration, callout borders |
| Emerald | `#27AE60` | Noble/cathodic metals (bottom of chart), protective examples |
| Coral | `#E05C5C` | Active/anodic metals (top of chart), corrosion examples |
| Mid Slate | `#3A4055` | Chart dividers, table headers, illustration outlines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills |
| Alt Row | `#252B3D` | Chart bar backgrounds (alternate spacing) |
| Bright Silver | `#C8D0D8` | Steel/substrate illustration fills |
| Coral Light | `#F08080` | Active end gradient (top) |
| Amber Mid | `#D89020` | Middle of gradient transition |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 12.0" — chart/right-content split
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 25.5" — Zone 2/Zone 3 boundary
- 32.5" — Zone 3/Zone 4 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — MAIN CONTENT (2.9"–25.5" / ~22.6" tall)
  LEFT COLUMN (X: 0.5"–11.5"): Galvanic Series Chart (HERO)
  RIGHT COLUMN (X: 12.5"–23.5"):
    Block C: Four components of a galvanic cell (illustration + labels)
    Block D: Anodic vs. Cathodic protection examples (two cross-sections)
    Block E: Key potential differences callout

ZONE 3 — DESIGN GUIDANCE STRIP (25.5"–32.5" / ~7.0" tall)
  Block F: "Mixing Metals" practical guidance — three callouts
  Block G: Stop-Corrosion key takeaway

ZONE 4 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A — Headline**
- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text:

> THE GALVANIC SERIES

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.6"
- Width: 23.0"
- Font: Barlow SemiBold, 40 pt, `#E8A020` (Amber)
- Text:

> Why Metals Corrode in Contact

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.3"
- Width: 23.0"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity
- Text:

> Corrosion is the reason plating exists.

---

### ZONE 2 — Main Content

**Dimensions:** Y: 2.9" to 25.5" (~22.6" tall). Two-column layout.

---

#### LEFT COLUMN — Galvanic Series Chart (HERO)

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 3.1"
- Width: 11.0"
- Font: Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`
- Alignment: Center within column
- Text:

> GALVANIC SERIES (SEAWATER)

**Sub-label:**
- Position: X: 0.5". Y: 3.7"
- Width: 11.0"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 60%
- Alignment: Center
- Text:

> Active (anodic) at top → Noble (cathodic) at bottom
> Reference data — relative comparison only, not lab-precision values

---

**BLOCK B — Galvanic Series Chart**

Y: 4.3" to 25.0" (~20.7" tall). 16 bars stacked vertically.

**Chart container:**
- Element type: Rectangle
- Position: X: 0.5". Y: 4.3"
- Width: 11.0". Height: 20.7"
- Fill: `#1E2435` (Dark Callout)
- No border

**Top axis label (Active end indicator):**
- Position: X: 0.5". Y: 4.4"
- Width: 11.0"
- Font: Barlow SemiBold, 14 pt, `#E05C5C` (Coral)
- Alignment: Center
- Text:

> ↑ ACTIVE / ANODIC (corrodes preferentially)

**Bar layout — 16 bars, each ~1.15" tall, stacked from Y: 4.9" to 24.4".**

Each bar is built as:
1. Bar rectangle:
   - Element type: Rectangle
   - Width: 10.6". Height: 1.1"
   - Position: X: 0.7". Y: starting at 4.9", incrementing by 1.2" per bar
   - Fill: graduated color (see table)
2. Metal name (left side of bar):
   - Element type: Text box
   - Font: Inter Medium, 18 pt
   - Color: `#F0EDE8` (or `#1A1F2E` if bar fill is light)
   - Position: X: 0.9" (inside bar, 0.2" padding). Vertically centered in bar.
3. Potential value (right side of bar):
   - Element type: Text box
   - Font: JetBrains Mono Regular, 16 pt
   - Color: `#F0EDE8` (or `#1A1F2E` for contrast on light fills)
   - Position: X: 9.5" to 11.2", right-aligned. Vertically centered.

**Bar list (top = active, bottom = noble):**

| # | Metal / Alloy | Potential vs. SCE (V) | Bar Fill |
|---|---------------|------------------------|----------|
| 1 | Magnesium | -1.60 | `#E05C5C` (Coral) |
| 2 | Zinc | -1.03 | `#E05C5C` |
| 3 | Aluminum (5052) | -0.85 | `#F08080` (Coral Light) |
| 4 | Cadmium | -0.80 | `#F08080` |
| 5 | Carbon Steel | -0.70 | `#E8A020` (Amber) |
| 6 | Cast Iron | -0.68 | `#E8A020` |
| 7 | 304 Stainless (active) | -0.53 | `#E8A020` |
| 8 | Lead | -0.31 | `#D89020` (Amber Mid) |
| 9 | Tin | -0.31 | `#D89020` |
| 10 | Brass | -0.30 | `#D89020` |
| 11 | Copper | -0.22 | `#D89020` |
| 12 | Bronze | -0.20 | `#27AE60` at 60% |
| 13 | Nickel (passive) | -0.07 | `#27AE60` at 70% |
| 14 | 304 Stainless (passive) | -0.05 | `#27AE60` at 80% |
| 15 | Silver | +0.13 | `#27AE60` |
| 16 | Platinum / Gold | +0.20 / +1.20 | `#27AE60` |

Use 1 pt borders between bars in `#1A1F2E` to give the chart a clean stacked appearance.

**Bottom axis label (Noble end indicator):**
- Position: X: 0.5". Y: 24.5"
- Width: 11.0"
- Font: Barlow SemiBold, 14 pt, `#27AE60` (Emerald)
- Alignment: Center
- Text:

> ↓ NOBLE / CATHODIC (resists corrosion)

---

#### RIGHT COLUMN — Cell Components, Examples, Potentials

X: 12.5" to 23.5" (11.0" wide). Y: 3.1" to 25.0".

---

**BLOCK C — Four Components of a Galvanic Cell**

Y: 3.1" to 11.0"

**Section label:**
- Position: X: 12.5". Y: 3.1"
- Width: 11.0"
- Font: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`
- Alignment: Center
- Text:

> THE FOUR COMPONENTS OF A GALVANIC CELL

**Cell illustration container:**
- Element type: Rounded rectangle
- Position: X: 12.5". Y: 3.7"
- Width: 11.0". Height: 7.0"
- Fill: `#1E2435`
- Corner radius: 8 pt

Left-border accent:
- Width: 0.06". Height: 7.0". Fill: `#2EC4B6` (Teal)

**Anode block (left side of illustration):**
- Element type: Rectangle
- Position: X: 13.5". Y: 6.0"
- Width: 1.5". Height: 3.0"
- Fill: `#E05C5C` (Coral)
- Label below: `ANODE` — Barlow SemiBold, 14 pt, `#E05C5C`. Centered below block.
- Sub-label: `(loses electrons,` newline `corrodes)` — Inter Regular, 11 pt, `#F0EDE8` at 70%

**Cathode block (right side of illustration):**
- Element type: Rectangle
- Position: X: 21.0". Y: 6.0"
- Width: 1.5". Height: 3.0"
- Fill: `#27AE60` (Emerald)
- Label below: `CATHODE` — Barlow SemiBold, 14 pt, `#27AE60`. Centered below block.
- Sub-label: `(gains electrons,` newline `protected)` — Inter Regular, 11 pt, `#F0EDE8` at 70%

**Electronic path (wire arc connecting anode top to cathode top):**
- Element type: Curved line with arrowhead
- Stroke: 2 pt, `#E8A020` (Amber)
- Arrowhead: at the cathode end (electrons flow from anode to cathode externally)
- Label above arc: `Electronic path (wire)` — Inter Regular, 12 pt, `#E8A020`
- Position: arc spans X: 14.25" to 21.75", Y: 4.5" to 5.8"

**Ionic path (electrolyte zone between blocks):**
- Element type: Rectangle
- Position: X: 15.0". Y: 7.0"
- Width: 6.0". Height: 1.5"
- Fill: `#2EC4B6` at 25% opacity
- Border: 1 pt dashed, `#2EC4B6`
- Label inside: `Ionic path (electrolyte)` — Inter Regular, 12 pt, `#2EC4B6`. Centered.
- Small ion arrows (dashed) flowing left-to-right inside the rectangle: 1 pt, `#2EC4B6`

**Key takeaway callout (below illustration, inside the container):**
- Position: X: 12.8". Y: 9.7"
- Width: 10.4"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Alignment: Center
- Text:

> Eliminate any one component to stop corrosion.

---

**BLOCK D — Anodic vs. Cathodic Protection Examples**

Y: 11.4" to 19.5"

**Section label:**
- Position: X: 12.5". Y: 11.4"
- Width: 11.0"
- Font: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`
- Alignment: Center
- Text:

> ANODIC vs. CATHODIC COATINGS

---

**Example 1 — Zinc on Steel (anodic / protective):**

Container:
- Element type: Rounded rectangle
- Position: X: 12.5". Y: 12.0"
- Width: 11.0". Height: 3.5"
- Fill: `#1E2435`
- Corner radius: 6 pt

Left-border accent:
- Width: 0.06". Height: 3.5". Fill: `#27AE60` (Emerald)

Title:
- Position: X: 12.8". Y: 12.2"
- Font: Barlow SemiBold, 18 pt, `#27AE60`
- Text:

> ZINC ON STEEL — Sacrificial Protection

Cross-section illustration (right side of callout):
- Steel substrate: Rectangle, X: 18.0", Y: 13.5", W: 5.0", H: 0.8", fill `#C8D0D8` (Bright Silver)
- Zinc coating: Rectangle, X: 18.0", Y: 13.0", W: 5.0", H: 0.5", fill `#E05C5C` (Coral)
- Pore in zinc: small rectangle gap, fill matches background, X: 20.5", W: 0.3"
- Label: `Zinc (corrodes)` — 10 pt, `#E05C5C`, above zinc layer
- Label: `Steel (protected)` — 10 pt, `#27AE60`, below steel layer
- Arrow showing zinc dissolving away into solution (small, upward dashed arrows above zinc)

Body text (left of illustration):
- Position: X: 12.8". Y: 12.7"
- Width: 5.0"
- Font: Inter Regular, 13 pt, `#F0EDE8`
- Line height: 140%
- Text:

> Even at a coating breach, the zinc continues to corrode preferentially and protect the exposed steel.

---

**Example 2 — Nickel on Steel (cathodic / risky):**

Container:
- Element type: Rounded rectangle
- Position: X: 12.5". Y: 15.7"
- Width: 11.0". Height: 3.5"
- Fill: `#1E2435`
- Corner radius: 6 pt

Left-border accent:
- Width: 0.06". Height: 3.5". Fill: `#E05C5C` (Coral)

Title:
- Position: X: 12.8". Y: 15.9"
- Font: Barlow SemiBold, 18 pt, `#E05C5C`
- Text:

> NICKEL ON STEEL — Pore = Failure

Cross-section illustration (right side):
- Steel substrate: Rectangle, X: 18.0", Y: 17.2", W: 5.0", H: 0.8", fill `#C8D0D8`
- Nickel coating: Rectangle, X: 18.0", Y: 16.7", W: 5.0", H: 0.5", fill `#27AE60`
- Pore: small gap in nickel, X: 20.5", W: 0.3"
- Pit forming in steel BELOW the pore: small Coral circle, X: 20.5", Y: 17.5"
- Label: `Nickel (intact)` — 10 pt, `#27AE60`, above nickel
- Label: `Steel (corrodes at pore)` — 10 pt, `#E05C5C`, below steel

Body text (left of illustration):
- Position: X: 12.8". Y: 16.4"
- Width: 5.0"
- Font: Inter Regular, 13 pt, `#F0EDE8`
- Line height: 140%
- Text:

> Any pore in the nickel exposes the steel and concentrates corrosion at a single point — pitting failure.

---

**BLOCK E — Key Potential Differences Callout**

Y: 19.9" to 24.8"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 12.5". Y: 19.9"
- Width: 11.0". Height: 4.9"
- Fill: `#1E2435`
- Corner radius: 8 pt

Left-border accent:
- Width: 0.06". Height: 4.9". Fill: `#E8A020` (Amber)

Title:
- Position: X: 12.8". Y: 20.1"
- Font: Barlow SemiBold, 20 pt, `#E8A020`
- Text:

> KEY POTENTIAL DIFFERENCES

Sub-title:
- Position: X: 12.8". Y: 20.7"
- Font: Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text:

> Larger ΔV = more aggressive galvanic corrosion

Data table (3 rows):
- Header row at Y: 21.2", height 0.4", fill `#3A4055`
- Headers: `COUPLE` (X: 12.9"), `ΔV` (X: 17.9"), `RISK` (X: 20.0") — Barlow SemiBold, 13 pt, `#F0EDE8`

Row 1 (Y: 21.7"):
- `Zn / Steel` — Inter Medium, 14 pt, `#F0EDE8`
- `0.31 V` — JetBrains Mono Regular, 14 pt, `#27AE60`
- `Mild — protective` — Inter Regular, 13 pt, `#27AE60`

Row 2 (Y: 22.5"):
- `Cu / Steel` — Inter Medium, 14 pt, `#F0EDE8`
- `0.48 V` — JetBrains Mono Regular, 14 pt, `#E8A020`
- `Moderate` — Inter Regular, 13 pt, `#E8A020`

Row 3 (Y: 23.3"):
- `Au / Ni (active)` — Inter Medium, 14 pt, `#F0EDE8`
- `1.93 V` — JetBrains Mono Regular, 14 pt, `#E05C5C`
- `Severe — destructive` — Inter Regular, 13 pt, `#E05C5C`

Footnote:
- Position: X: 12.8". Y: 24.2"
- Width: 10.4"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 60%, italic
- Text:

> Potentials measured in flowing seawater vs. SCE. These are reference-grade comparison values, not lab-precision measurements — actual field corrosion rates depend on electrolyte chemistry, temperature, area ratio, oxygen, and surface condition.

---

### ZONE 3 — Design Guidance Strip

**Dimensions:** Full page width within margins. Y: 25.5" to 32.5" (~7.0" tall).

---

**Section label:**
- Position: Centered horizontally. Y: 25.7"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Alignment: Center
- Text:

> WHEN METALS MUST TOUCH

---

**BLOCK F — Three Practical Callouts**

Y: 26.4" to 30.4". Three equal-width columns with 0.3" gutters.

**Column widths:** Each column ~7.5" wide. Column 1: X: 0.5"–8.0", Column 2: X: 8.3"–15.8", Column 3: X: 16.1"–23.6"

**Callout 1 — Pick metals close together:**

Container:
- Rounded rectangle, X: 0.5", Y: 26.4", W: 7.5", H: 4.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 4.0", fill `#27AE60`

Title:
- Position: X: 0.8". Y: 26.6"
- Font: Barlow SemiBold, 18 pt, `#27AE60`
- Text:

> KEEP ΔV SMALL

Body:
- Position: X: 0.8". Y: 27.2"
- Width: 7.0"
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Line height: 145%
- Text:

> Choose metals within 0.15–0.25 V on the galvanic series. The smaller the potential gap, the slower the corrosion.

---

**Callout 2 — Break the path:**

Container:
- Rounded rectangle, X: 8.3", Y: 26.4", W: 7.5", H: 4.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 4.0", fill `#2EC4B6`

Title:
- Position: X: 8.6". Y: 26.6"
- Font: Barlow SemiBold, 18 pt, `#2EC4B6`
- Text:

> ISOLATE THE COUPLE

Body:
- Position: X: 8.6". Y: 27.2"
- Width: 7.0"
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Line height: 145%
- Text:

> Use insulating gaskets, sleeves, washers, or coatings to break the electronic OR ionic path between dissimilar metals.

---

**Callout 3 — Manage the area ratio:**

Container:
- Rounded rectangle, X: 16.1", Y: 26.4", W: 7.5", H: 4.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" x 4.0", fill `#E8A020`

Title:
- Position: X: 16.4". Y: 26.6"
- Font: Barlow SemiBold, 18 pt, `#E8A020`
- Text:

> WATCH AREA RATIO

Body:
- Position: X: 16.4". Y: 27.2"
- Width: 7.0"
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Line height: 145%
- Text:

> A small anode connected to a large cathode corrodes catastrophically. Never use anodic fasteners in cathodic structures.

---

**BLOCK G — Stop-Corrosion Key Takeaway Strip**

Position: X: 0.5". Y: 30.7"
- Element type: Rounded rectangle
- Width: 23.0". Height: 1.6"
- Fill: `#1E2435`
- Corner radius: 8 pt
- Left accent: 0.06" x 1.6", fill `#E05C5C`

Text:
- Position: X: 0.8". Y: 30.95"
- Width: 22.4"
- Font: Barlow Condensed ExtraBold, 32 pt, `#F0EDE8`
- Alignment: Center
- Text:

> CORROSION NEEDS ALL FOUR — REMOVE ANY ONE TO STOP IT.

---

### ZONE 4 — Footer Band

**Dimensions:** Full page width. Y: 32.5" to 36.0" (~3.5" tall).

---

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.5"
- Width: 24.0". Height: 3.5"
- Fill: `#0D1020`

**Disclaimer:**
- Position: X: 0.5". Y: 32.8"
- Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50%, alignment center
- Text:

> The galvanic series shown is for flowing seawater and is intended as a relative reference. Real-world corrosion rates depend on electrolyte chemistry, temperature, area ratio, oxygenation, and surface condition. Consult a corrosion engineer for service-critical assemblies.

**Poster title:**
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> The Galvanic Series — Why Metals Corrode in Contact

**Series name:**
- Position: Centered. Y: 34.2"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70%, center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Position: X: 22.5". Y: 33.3"
- Width: 0.83". Height: 0.42"
- Fill: `#3A4055`
- Text inside: `[LOGO]` — 10 pt, `#F0EDE8` at 50%

**Version:**
- Position: X: 0.5". Y: 35.0"
- Font: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%
- Text:

> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Galvanic Chart | Section label, sub-label, chart container, all 16 bars + labels, axis indicators |
| Zone 2 - Cell Components | Block C: section label, illustration container, anode/cathode blocks, paths, labels |
| Zone 2 - Anodic vs Cathodic | Block D: section label, both example callouts with cross-sections |
| Zone 2 - Potential Differences | Block E: callout, table, footnote |
| Zone 3 - Design Guidance | Section label, three callouts, key takeaway strip |
| Zone 4 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout fills, chart container |
| `#252B3D` | `#E8E8F0` | Alternate backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents (and noble bars on chart) |
| `#E05C5C` | `#B83E3E` | Coral accents (and active bars on chart) |
| `#F08080` | `#D04646` | Coral Light (chart upper-mid) |
| `#D89020` | `#A06808` | Amber Mid (chart middle) |
| `#3A4055` | `#D0D4DE` | Dividers, table headers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

The galvanic series chart bars require manual recoloring per bar. Plan extra time for this zone — it is the most labor-intensive Light edition step.

---

## Part 7 — Export Checklist

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Galvanic Series — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Galvanic Series — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Galvanic Series — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Galvanic Series — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Galvanic Series — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Galvanic Series — Light — Digital.pdf` | RGB | PDF Standard | No |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #17 — The Galvanic Series — Construction Workup v2.0*
*2026-04-07 (v1.0 issued 2026-04-06)*
