---
Project: Plating Posters Inc
Poster Number: 23
Title: "Watts Nickel Plating — The Workhorse Bath"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-11T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watts Nickel Plating — Research Brief v1.md"
Technical Source: Watson research brief v1 (2026-04-11) — Nickel Institute Nickel Plating Handbook 2023 (Tables 2-3, pp.13-18), 1993 Metal Finishing Guidebook, Gemini research queries. Covers bath composition, operating parameters, Big 3 additives, bright vs. semi-bright, Hull cell interpretation, defect diagnosis, and contamination thresholds.
Watson Flags: TWO OPEN — (1) Confirm cathode efficiency 90-97% range and the 95.5% standard estimation figure against the Nickel Institute Handbook Table 2 (Watson cites this but Alaina has not independently verified). (2) Confirm the STEP test 100-125 mV minimum potential difference specification source. Both non-blocking; values attributed to authoritative sources.
Tyler Flags: TWO OPEN — (1) Validate the "Big 3" additive consumption model (brighteners consumed by plating / carriers consumed by dragout) against Tyler's shop experience — confirm this simplification is fair for a poster audience. (2) Confirm that the 30-45 g/L boric acid range and the boric acid solubility caveat (dissolve in hot water before addition) match Tyler's current lab procedures. Both non-blocking; values from Nickel Institute Handbook.
Process Scope: Watts nickel electroplating (decorative and functional nickel)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - WattsNickel
  - NickelPlating
  - Additives
  - HullCell
  - ConstructionWorkup
---

# Poster # Poster #23 — Construction Workup
## Watts Nickel Plating — The Workhorse Bath

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-11*

This document is the construction workup for Poster #23. It translates Watson's comprehensive Watts Nickel research brief into a dense, scannable wall reference that covers the complete bath — chemistry, parameters, additives, defect diagnosis, and Hull cell interpretation. Two Watson flags and two Tyler flags remain open — all non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

This is one of the most content-rich posters in the series. The design philosophy here is "everything a nickel plater needs on one wall" — which means careful information hierarchy is essential. The poster uses a three-pillar hero visual (the bath composition triangle), a gauge-style parameter dashboard, and a defect diagnosis grid to make the density scannable rather than overwhelming.

**Content source:** Watts Nickel Plating — Research Brief v1.md (Watson, 2026-04-11).

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, gauge backgrounds, and accent borders
- Circle shapes for gauge-style parameter displays
- Line elements for gauge needles and divider lines
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for beaker, thermometer, lightning bolt icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Three-pillar bath composition visual (Block B — HERO):** Three tall rounded rectangles side by side, each representing one essential bath component (NiSO4, NiCl2, H3BO3). Each pillar contains the chemical formula, concentration range, role, and a one-word "nickname." Straightforward in the design — essentially three styled callout boxes.

2. **Parameter gauge cluster (Block D):** Four circle-based "gauges" showing pH, temperature, current density, and surface tension. Each gauge is a circle with a colored arc segment and a "needle" line. The arc segments can be built using the tool's donut chart shape (or a circle with a thick border, masked to show only the desired arc). If true arcs are difficult, simplify to horizontal bar gauges with green/yellow/red zones — still effective and easier to build. Elara should choose the approach that looks cleanest.

3. **Defect diagnosis grid (Block F):** A 3x2 grid of mini-cards, each with an icon placeholder, defect name, and primary cause. Same construction as Poster #14's GHS hazard grid — established pattern.

4. **Hull cell panel strip (Block G):** A horizontal rectangle with a gradient-like fill from dark (left/HCD) to light (right/LCD) with labeled zones. The gradient effect can be faked with 4-5 adjacent thin vertical rectangles in progressively lighter shades of Teal. Elara should test this approach.

5. **Bright vs. Semi-Bright comparison (Block E):** Two side-by-side callout boxes. Established pattern.

6. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

7. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

8. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

9. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

10. **Sub/superscript characters:** Unicode characters provided verbatim — NiSO₄, NiCl₂, H₃BO₃, Ni²⁺, H₂SO₄, NiCO₃, H⁺, Ni(OH)₂. Copy-paste exactly.

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
- **Inter Regular** and **Inter Medium** — all body text, table data, and descriptions
- **JetBrains Mono Regular** — all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Nickel Chloride pillar, HCD zone, warning callouts, burning defect |
| Teal | `#2EC4B6` | Boric Acid pillar, LCD zone, Hull cell accents, parameter gauges |
| Emerald | `#27AE60` | Nickel Sulfate pillar, good panel zone, optimal ranges |
| Coral | `#E05C5C` | Defect indicators, contamination thresholds, problem callouts |
| Mid Slate | `#3A4055` | Table headers, gauge backgrounds, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, defect grid card backgrounds |
| Alt Row | `#252B3D` | Alternating table rows, secondary elements |
| Bright Silver | `#C8D0D8` | Anode diagram elements, neutral reference |
| Gauge Green | `#27AE60` | Optimal zone on gauges (same as Emerald) |
| Gauge Yellow | `#E8A020` | Caution zone on gauges (same as Amber) |
| Gauge Red | `#E05C5C` | Danger zone on gauges (same as Coral) |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 10.5" — Zone 2/Zone 3 boundary
- 15.0" — Zone 3/Zone 4 boundary
- 20.0" — Zone 4/Zone 5 boundary
- 23.0" — Zone 5/Zone 6 boundary
- 28.0" — Zone 6/Zone 7 boundary
- 32.5" — Zone 7/Zone 8 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — BATH COMPOSITION TRIANGLE (2.9"–10.5" / ~7.6" tall)
  Block B: Three-pillar hero visual (NiSO4, NiCl2, H3BO3)
  Block C: Composition summary table (compact)

ZONE 3 — THE "BIG 3" ADDITIVES (10.5"–15.0" / ~4.5" tall)
  Block D: Three-column additive panel (Carrier, Brightener, Wetting Agent)

ZONE 4 — OPERATING PARAMETER DASHBOARD (15.0"–20.0" / ~5.0" tall)
  Block E: Four gauge-style parameter displays (pH, temp, CD, surface tension)

ZONE 5 — BRIGHT VS. SEMI-BRIGHT (20.0"–23.0" / ~3.0" tall)
  Block EE: Side-by-side comparison callout

ZONE 6 — DEFECT DIAGNOSIS GRID (23.0"–28.0" / ~5.0" tall)
  Block F: 3x2 grid of common defects with cause and indicator color

ZONE 7 — HULL CELL STRIP + CONTAMINATION TABLE (28.0"–32.5" / ~4.5" tall)
  Block G: Hull cell panel strip with zone labels (left half)
  Block H: Key contamination thresholds table (right half)

ZONE 8 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5" (left safe zone). Y: 0.5" (top safe zone)
- Width: 23.0" (full safe zone width)
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> WATTS NICKEL PLATING

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 38 pt
- Color: `#27AE60` (Emerald)
- Text:

> The Workhorse Bath — Invented 1916, Still the Standard

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Three chemicals. One bath. The foundation of decorative and functional nickel plating worldwide.

---

### ZONE 2 — Bath Composition Triangle (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 10.5" (~7.6" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE THREE ESSENTIAL COMPONENTS

---

**BLOCK B — Three Pillars**

Y: 3.8" to 9.0" (~5.2" tall). Three tall rounded rectangles evenly spaced across the safe zone.

Each pillar:
- Element type: Rounded rectangle
- Width: 7.0". Height: 5.0"
- Corner radius: 8 pt

| Pillar | X Position | Fill | Border | Accent Color |
|---|---|---|---|---|
| Nickel Sulfate | 0.5" | `#1E2435` | 2 pt, `#27AE60` (Emerald) | Emerald |
| Nickel Chloride | 8.0" | `#1E2435` | 2 pt, `#E8A020` (Amber) | Amber |
| Boric Acid | 15.5" | `#1E2435` | 2 pt, `#2EC4B6` (Teal) | Teal |

**Inside each pillar (top to bottom):**

*Pillar 1 — Nickel Sulfate:*

Nickname badge (top, centered):
- Element type: Rounded rectangle (small badge)
- Width: 3.5". Height: 0.5"
- Fill: `#27AE60` (Emerald)
- Position: Centered inside pillar, Y: 4.0"
- Text: `THE METAL` — Barlow Condensed ExtraBold, 20 pt, `#1A1F2E`

Chemical formula:
- Position: Centered, Y: 4.8"
- Font: JetBrains Mono Regular, 24 pt, `#F0EDE8`
- Text: `NiSO₄ · 6H₂O`

Concentration:
- Position: Centered, Y: 5.5"
- Font: JetBrains Mono Regular, 20 pt, `#27AE60`
- Text: `240–300 g/L (32–40 oz/gal)`

Role description:
- Position: X: 1.0", Y: 6.3"
- Width: 6.0"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 145%
- Text:

> Primary source of Ni²⁺ ions for deposition. Higher concentration allows higher current density and faster plating rates. At 300 g/L, push to 60–75 ASF with proper agitation.

Key fact (bottom of pillar):
- Position: Centered, Y: 8.2"
- Font: Inter Medium, 14 pt, `#27AE60`
- Text:

> 95.5% cathode efficiency — the standard estimation figure

*Pillar 2 — Nickel Chloride:*

Nickname badge:
- Fill: `#E8A020` (Amber)
- Text: `THE ACTIVATOR`

Chemical formula:
- Font: JetBrains Mono Regular, 24 pt, `#F0EDE8`
- Text: `NiCl₂ · 6H₂O`

Concentration:
- Font: JetBrains Mono Regular, 20 pt, `#E8A020`
- Text: `30–90 g/L (4–12 oz/gal)`

Role description:
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Text:

> Two critical jobs: (1) Prevents passive oxide film on anodes — without chloride, anodes go passive and the bath starves. (2) Boosts conductivity — lower voltage, better throwing power. Also increases deposit stress.

Key fact:
- Font: Inter Medium, 14 pt, `#E8A020`
- Text:

> Chloride is the anode's lifeline — below 30 g/L, expect passivation

*Pillar 3 — Boric Acid:*

Nickname badge:
- Fill: `#2EC4B6` (Teal)
- Text: `THE BUFFER`

Chemical formula:
- Font: JetBrains Mono Regular, 24 pt, `#F0EDE8`
- Text: `H₃BO₃`

Concentration:
- Font: JetBrains Mono Regular, 20 pt, `#2EC4B6`
- Text: `30–45 g/L (4–6 oz/gal)`

Role description:
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Text:

> pH buffer at the cathode film — NOT the bulk solution. During plating, H⁺ is consumed at the cathode. Without boric acid, local pH spikes above 5.5 and Ni(OH)₂ precipitates directly on the part: burned, dark, rough deposits.

Key fact:
- Font: Inter Medium, 14 pt, `#2EC4B6`
- Text:

> Consumed by dragout, not electrolysis — relatively stable in the bath

---

**BLOCK C — Composition Summary Table** (compact, below pillars)

Y: 9.2" to 10.3"

A single-row summary strip reinforcing the three components:

- Element type: Rounded rectangle
- Position: X: 0.5". Y: 9.2"
- Width: 23.0". Height: 1.0"
- Fill: `#252B3D` (Alt Row)
- Corner radius: 4 pt

Three data points evenly spaced inside:

| Data | Font | Color |
|---|---|---|
| `pH adjust down: dilute H₂SO₄  ·  pH adjust up: NiCO₃` | JetBrains Mono Regular, 14 pt | `#F0EDE8` |
| `SG: 1.20–1.25 (24–29 Be)` | JetBrains Mono Regular, 14 pt | `#F0EDE8` at 70% |
| `Anode type: electrolytic Ni S-Rounds in Ti baskets + PP bags` | JetBrains Mono Regular, 13 pt | `#F0EDE8` at 70% |

---

### ZONE 3 — The "Big 3" Additives

**Dimensions:** Full page width within margins. Y: 10.5" to 15.0" (~4.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 10.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE "BIG 3" ADDITIVES

---

**BLOCK D — Three Additive Columns**

Y: 11.3" to 14.8" (~3.5" tall). Three callout boxes side by side.

Each callout:
- Element type: Rounded rectangle
- Width: 7.33". Height: 3.3"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

| Column | X Position | Accent Color | Title | Nickname |
|---|---|---|---|---|
| Carrier (Class I) | 0.5" | `#27AE60` | CARRIERS | "The Foundation" |
| Brightener (Class II) | 8.0" | `#E8A020` | BRIGHTENERS | "The Mirror" |
| Wetting Agent | 15.5" | `#2EC4B6` | WETTING AGENTS | "The Bubble Releaser" |

Each callout interior (top to bottom):

Left-border accent:
- Element type: Rectangle, 0.06" wide, full height, accent color

Title line:
- Font: Barlow SemiBold, 20 pt, accent color
- Text: `CARRIERS (CLASS I)` / `BRIGHTENERS (CLASS II)` / `WETTING AGENTS`

Nickname:
- Font: Barlow Condensed ExtraBold, 16 pt, `#F0EDE8` at 50%
- Text: `"The Foundation"` / `"The Mirror"` / `"The Bubble Releaser"`

What they do:
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Line height: 140%

*Carrier text:*
> Refine grain structure. Reduce internal stress (saccharin is the primary stress reliever). Enable brighteners to function across a wider CD range. Introduce sulfur into the deposit.

*Brightener text:*
> Produce mirror brightness and leveling. Preferentially deposit in valleys, filling surface imperfections. Present in very low concentration but dramatic effect on appearance.

*Wetting Agent text:*
> Lower surface tension. Allow H₂ gas bubbles to release from the cathode before plating over them. Without wetter, bubbles cling and create pits.

Consumption note (bottom of each callout):
- Font: JetBrains Mono Regular, 12 pt, accent color

*Carrier:* `Consumed by: DRAGOUT`
*Brightener:* `Consumed by: PLATING (amp-hours)`
*Wetting Agent:* `Consumed by: DRAGOUT + carbon adsorption`

---

### ZONE 4 — Operating Parameter Dashboard

**Dimensions:** Full page width within margins. Y: 15.0" to 20.0" (~5.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 15.2"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> OPERATING PARAMETERS

---

**BLOCK E — Four Parameter Gauges**

Y: 15.8" to 19.8" (~4.0" tall). Four gauge displays evenly spaced.

Each gauge is a self-contained visual unit — a large circle with a colored arc (or horizontal bar if circles prove difficult), a numerical range, an optimal value callout, and red-zone warning labels.

**Gauge layout — option A (circle gauges):**

Each gauge unit occupies a 5.5" wide column:
- Gauge 1 (pH): X: 0.5"
- Gauge 2 (Temperature): X: 6.25"
- Gauge 3 (Current Density): X: 12.0"
- Gauge 4 (Surface Tension): X: 17.75"

Each gauge:
- Circle: Diameter 3.0". Fill: `#1E2435`. Border: 4 pt, `#3A4055`.
- Inside the circle: the optimal value in large text, the parameter name below it.
- A colored arc segment around the top 180 degrees of the circle:
  - Green zone (`#27AE60`): optimal range
  - Yellow zone (`#E8A020`): caution
  - Red zone (`#E05C5C`): danger
- If true arcs are not possible , Elara may substitute **horizontal bar gauges** — a wide rectangle divided into green/yellow/red segments with a marker for the optimal value.

**Gauge 1 — pH:**
- Optimal: `4.0` — Barlow Condensed ExtraBold, 36 pt, `#27AE60`
- Range: `3.5–4.5` — JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Label: `pH` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Red low: `< 3.0: excess H₂ evolution` — Inter Regular, 11 pt, `#E05C5C`
- Red high: `> 4.5: Ni(OH)₂ precipitation` — Inter Regular, 11 pt, `#E05C5C`

**Gauge 2 — Temperature:**
- Optimal: `130°F` — Barlow Condensed ExtraBold, 32 pt, `#27AE60`
- Range: `104–140°F (40–60°C)` — JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Label: `TEMPERATURE` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Note: `Higher = better conductivity + ductility but faster additive breakdown` — Inter Regular, 11 pt, `#E8A020`

**Gauge 3 — Current Density (rack):**
- Optimal: `30–50` — Barlow Condensed ExtraBold, 30 pt, `#27AE60`
- Range: `20–75 ASF` — JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Label: `CURRENT DENSITY (ASF)` — Barlow SemiBold, 16 pt, `#F0EDE8`
- Sub-label: `Barrel: 3–20 ASF` — JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%

**Gauge 4 — Surface Tension:**
- Optimal: `33–35` — Barlow Condensed ExtraBold, 30 pt, `#27AE60`
- Range: `30–40 dynes/cm` — JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Label: `SURFACE TENSION` — Barlow SemiBold, 16 pt, `#F0EDE8`
- Red low: `< 30: excess foam` — Inter Regular, 11 pt, `#E05C5C`
- Red high: `> 40: pitting` — Inter Regular, 11 pt, `#E05C5C`

---

### ZONE 5 — Bright vs. Semi-Bright Comparison

**Dimensions:** Full page width within margins. Y: 20.0" to 23.0" (~3.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 20.2"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> BRIGHT VS. SEMI-BRIGHT — THE DUPLEX SYSTEM

---

**BLOCK EE — Side-by-Side Comparison**

Y: 20.7" to 22.8" (~2.1" tall). Two callout boxes.

**Left — Bright Nickel:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 20.7"
- Width: 11.0". Height: 2.0"
- Fill: `#1E2435`
- Left-border accent: `#E8A020` (Amber)
- Title: `BRIGHT NICKEL` — Barlow SemiBold, 18 pt, `#E8A020`
- Data (two columns inside):

| Property | Value |
|---|---|
| Additive system | Carriers + brighteners + wetters |
| Sulfur in deposit | Yes (from carriers) |
| Grain structure | Laminar (banded layers) |
| Appearance | Mirror-bright |
| Corrosion role | Sacrificial (less noble) — corrodes laterally |

Font: Inter Regular, 13 pt, `#F0EDE8`. Property labels: Inter Medium, 13 pt, `#F0EDE8` at 60%.

**Right — Semi-Bright Nickel:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 20.7"
- Width: 11.5". Height: 2.0"
- Fill: `#1E2435`
- Left-border accent: `#2EC4B6` (Teal)
- Title: `SEMI-BRIGHT NICKEL` — Barlow SemiBold, 18 pt, `#2EC4B6`
- Data:

| Property | Value |
|---|---|
| Additive system | Sulfur-free levelers + wetters |
| Sulfur in deposit | No — sulfur-free mandatory |
| Grain structure | Columnar (perpendicular) |
| Appearance | Satiny, lustrous |
| Corrosion role | Noble base layer — resists penetration |

**Key fact strip (between the two boxes or below):**
- Element type: Text box
- Position: Centered horizontally. Y: 22.8" (or fits between boxes if space allows)
- Font: JetBrains Mono Regular, 13 pt, `#E8A020`
- Text:

> STEP test minimum: 100–125 mV potential difference between layers for duplex corrosion protection to function

---

### ZONE 6 — Defect Diagnosis Grid

**Dimensions:** Full page width within margins. Y: 23.0" to 28.0" (~5.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 23.2"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> WHAT GOES WRONG — THE 6 COMMON DEFECTS

---

**BLOCK F — 3x2 Defect Grid**

Y: 23.8" to 27.8" (~4.0" tall).

Six defect cards in a 3-column by 2-row grid. Each card:
- Element type: Rounded rectangle
- Width: 7.33". Height: 1.8"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 4 pt
- Column gap: 0.25". Row gap: 0.2"

Row 1 Y: 23.8". Row 2 Y: 25.9".

Left-border accent on each card (0.06" wide, full height) in the defect's indicator color.

**Card contents (per defect):**

Each card has:
- Defect name: Barlow SemiBold, 18 pt, indicator color
- Primary cause: Inter Regular, 15 pt, `#F0EDE8`
- Key fix: Inter Regular, 13 pt, `#F0EDE8` at 60%

| Position | Defect | Indicator Color | Primary Cause | Key Fix |
|---|---|---|---|---|
| R1C1 (X: 0.5") | PITTING | `#E05C5C` (Coral) | Low wetting agent — surface tension above 35 dynes/cm | Add anti-pit agent to 33–35 dynes/cm |
| R1C2 (X: 8.0") | BURNING (HCD) | `#E8A020` (Amber) | Low boric acid (below 30 g/L) — cathode film pH spike | Replenish H₃BO₃ to 37–45 g/L |
| R1C3 (X: 15.5") | DULL / HAZY | `#2EC4B6` (Teal) | Low brightener (Class II) or organic contamination | Add brightener per Hull cell; carbon treat |
| R2C1 (X: 0.5") | STRESS CRACKING | `#E05C5C` (Coral) | Excess brightener or low carrier — stress imbalance | Rebalance brightener/carrier ratio |
| R2C2 (X: 8.0") | ROUGH / GRAINY | `#E8A020` (Amber) | Torn anode bags, poor filtration, undissolved boric acid | Inspect bags; increase filtration to 3–5 turnovers/hr |
| R2C3 (X: 15.5") | DARK LCD | `#E05C5C` (Coral) | Metallic contamination — Cu, Zn, or Pb | Dummy plate at 2–5 ASF on corrugated cathodes |

---

### ZONE 7 — Hull Cell Strip + Contamination Thresholds

**Dimensions:** Full page width within margins. Y: 28.0" to 32.5" (~4.5" tall).

---

**BLOCK G — Hull Cell Panel Strip** (left half, X: 0.5" to 11.5")

Y: 28.0" to 32.3"

**Section label:**
- Position: X: 0.5". Y: 28.2"
- Font: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`
- Text:

> THE HULL CELL TELLS ALL

**Test conditions:**
- Position: X: 0.5". Y: 28.7"
- Font: JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%
- Text:

> 267 mL  |  2 A  |  10 min  |  120–140°F

**Panel strip:**
- Element type: Rectangle (the simulated Hull cell panel)
- Position: X: 0.5". Y: 29.2"
- Width: 11.0". Height: 1.8"
- This rectangle is divided into 5 vertical segments (each ~2.2" wide) to simulate the HCD-to-LCD gradient. From left to right:

| Segment | X | Fill | Label Above | Diagnosis Below |
|---|---|---|---|---|
| 1 (HCD edge) | 0.5" | `#E8A020` at 40% | `HCD` | `Burned = low boric acid` |
| 2 | 2.7" | `#27AE60` at 50% | | `Smooth = good` |
| 3 (center) | 4.9" | `#27AE60` at 70% | `SWEET SPOT` | `Bright + leveled = balanced` |
| 4 | 7.1" | `#27AE60` at 40% | | `Bright = good` |
| 5 (LCD edge) | 9.3" | `#3A4055` at 60% | `LCD` | `Dark = metal contamination` |

Segment labels above:
- Font: Barlow SemiBold, 12 pt, respective accent colors

Diagnosis labels below:
- Font: Inter Regular, 11 pt, `#F0EDE8`
- Position: Y: 31.2"

**Pitting indicator:**
- A small dashed callout across the full panel strip (mid-height):
- Text: `Pitting anywhere = low wetting agent` — Inter Medium, 12 pt, `#E05C5C`
- Dashed line: 1 pt, `#E05C5C`, full width of panel strip

**Good panel callout:**
- Position: X: 0.5". Y: 31.8"
- Font: Inter Medium, 13 pt, `#27AE60`
- Text:

> A good Watts nickel panel is bright across 70–80% of the width from HCD to LCD.

---

**BLOCK H — Key Contamination Thresholds** (right half, X: 12.0" to 23.5")

Y: 28.0" to 32.3"

**Section label:**
- Position: X: 12.0". Y: 28.2"
- Font: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`
- Text:

> CONTAMINATION THRESHOLDS

**Table (7 rows, 3 columns):**

Built as alternating rectangles with text overlays. Column widths: Contaminant (3.0"), Threshold (2.5"), Effect (6.0"). Total: 11.5".

Header row:
- Element type: Rectangle, fill `#3A4055`
- Text: Barlow SemiBold, 14 pt, `#F0EDE8`
- Labels: `Contaminant` | `Threshold` | `Effect`

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 10 ppm | Dark LCD deposits |
| Zinc | > 20 ppm | Dark LCD, hazy, stress increase |
| Lead | > 2 ppm | Black LCD streaks, brittle |
| Iron | > 50 ppm | Rough deposits, hydroxide pptn at pH > 4.5 |
| Chromium | > 5 ppm | Dull deposits, poor coverage |
| Cadmium | > 5 ppm | Brittle deposits, stress cracking |

Data font: JetBrains Mono Regular, 14 pt, `#F0EDE8` (thresholds in `#E05C5C` Coral for visual emphasis).
Contaminant names: Inter Medium, 14 pt, `#F0EDE8`.
Effect text: Inter Regular, 13 pt, `#F0EDE8`.

Lead row callout: Add a small `!` badge or highlight to the lead row — `#E05C5C` fill badge with `!` in Barlow Condensed ExtraBold 12 pt `#1A1F2E` — to visually emphasize that 2 ppm is an extremely low and dangerous threshold.

---

### ZONE 8 — Footer Band

**Dimensions:** Full page width. Y: 32.5" to 36.0" (~3.5" tall).

---

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.5"
- Width: 24.0". Height: 3.5"
- Fill: `#0D1020` (Deep Navy)

**Disclaimer:**
- Element type: Text box
- Position: X: 0.5". Y: 32.8"
- Width: 23.0"
- Font: Inter Regular
- Size: 11 pt
- Color: `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster is an educational reference tool. Bath compositions, operating parameters, and contamination thresholds are typical industry values for the Watts nickel bath. Specific formulations, additive systems, and process limits vary by proprietary product. Consult your process supplier and additive manufacturer for application-specific guidance. Source: Nickel Institute Nickel Plating Handbook 2023; general industry knowledge.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Watts Nickel Plating — The Workhorse Bath

**Series name:**
- Element type: Text box
- Position: Centered horizontally. Y: 34.2"
- Font: Inter Regular
- Size: 14 pt
- Color: `#F0EDE8` at 70% opacity
- Alignment: Center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Element type: Rectangle (placeholder)
- Position: X: 22.5". Y: 33.3"
- Width: 0.83" (60 pt). Height: 0.42" (30 pt)
- Fill: `#3A4055`
- Text inside: `[LOGO]` — Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:**
- Element type: Text box
- Position: X: 0.5". Y: 35.0"
- Font: JetBrains Mono Regular
- Size: 11 pt
- Color: `#F0EDE8` at 50% opacity
- Text:

> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

After building each zone, select all elements within that zone and group them (Ctrl+G / Cmd+G). Name each group:

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Bath Composition | Section label, three pillars, composition summary strip |
| Zone 3 - Big 3 Additives | Section label, three additive columns |
| Zone 4 - Parameter Dashboard | Section label, four gauge displays |
| Zone 5 - Bright vs Semi-Bright | Section label, two comparison callouts, STEP test callout |
| Zone 6 - Defect Grid | Section label, 3x2 defect cards |
| Zone 7 - Hull Cell and Contamination | Hull cell strip with diagnoses, contamination threshold table |
| Zone 8 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

After grouping, lock each completed zone (right-click > Lock) before proceeding to the next.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, defect card fills, pillar fills |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds, composition strip |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table headers, gauge backgrounds, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

Pillar borders (Emerald, Amber, Teal) become their darkened Light variants. Verify nickname badges remain legible with darkened fills — may need `#F5F4F0` text on darkened badge fills.

Hull cell panel strip: The gradient segments need adjusted fills for the light background — test at 60-80% opacity to maintain visual distinction.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Watts Nickel Plating — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Watts Nickel Plating — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Watts Nickel Plating — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Watts Nickel Plating — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Watts Nickel Plating — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Watts Nickel Plating — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor. This poster is content-dense — the 18x24" version may require some font size adjustments in the defect grid (Zone 6) and contamination table (Zone 7). Elara should flag any text that drops below 12 pt after resize.

---

## Design Notes

This is the densest poster in the series to date. Every zone earns its space:
- Zone 2 (Pillars) is the educational anchor — if someone reads nothing else, they learn the three-component system.
- Zone 4 (Gauges) is the at-a-glance reference — a shop foreman can check parameters in 5 seconds.
- Zone 6 (Defect Grid) is the troubleshooting quick reference — "what does this look like, and what caused it?"
- Zone 7 (Hull Cell + Contamination) ties it all together — the diagnostic tool and the threshold data.

The poster deliberately omits detailed additive chemistry (specific compound names, concentrations) because these are proprietary to each supplier's system. The focus is on principles and categories, not brand-specific formulations. This is a poster for every Watts nickel line, regardless of who supplies the chemistry.

Watson's research brief includes additional content (anode diagram, deposition rate table, specific gravity details) that was triaged out to keep the poster scannable. If Drew wants a companion "Watts Nickel — Advanced Reference" poster, the material is ready.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #23 — Watts Nickel Plating — Construction Workup v1.0*
*2026-04-11*
