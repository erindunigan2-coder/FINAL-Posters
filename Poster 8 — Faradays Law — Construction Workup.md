---
Project: Plating Posters Inc
Poster Number: 8
Title: "Faraday's Law in the Shop: Calculating Plating Thickness"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 8 — Faradays Law — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Faraday's Law Research Brief v1 (2026-04-03)
Watson Flags: TWO — cathode efficiency values + practical vs. theoretical rate display (both Drew, non-blocking)
Process Scope: Universal electroplating math — applies across all electrolytic processes
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FaradaysLaw
  - ConstructionWorkup
  - Calculations
---

# Poster # Poster #8 — Construction Workup
## Faraday's Law in the Shop: Calculating Plating Thickness

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #8. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. Two Watson flags remain open but are non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 8 — Faradays Law — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for table rows, callout boxes, accent borders, formula background, and bar chart segments
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Efficiency bar chart (Zone 4):** Each bar is two adjacent rectangles (Emerald for metal deposited, Coral for wasted). Width is proportional to percentage. This is straightforward — just place two rectangles side by side at calculated widths. The hard chrome bar will have a very narrow Emerald section (15%) and wide Coral section (85%).

2. **Variable legend strip below formula (Zone 2):** Four small colored squares with adjacent labels. Build as 4 small square shapes + text boxes. Straightforward.

3. **4 pt left-border accents on efficiency table rows and callout boxes:** Same technique as previous posters — narrow colored rectangle (approximately 0.06" wide) flush against the left edge.

4. **Global Colors / swatch remap for Light edition:** No Global Colors . Duplicate and manually recolor per Part 6.

5. **JetBrains Mono font:** Ensure font is available. Substitute **Courier Prime** if unavailable.

6. **Print size — 24x36":** Set exactly at document creation. For 18x24", duplicate and resize; verify 14 pt minimum floor.

7. **Sub/superscript characters:** Copy-paste Unicode characters exactly as provided (Cu²⁺, Cu⁺, Au⁺, Au³⁺, H₂, e⁻, etc.).

8. **Large formula text at 36 pt:** Verify the formula text box is wide enough that it does not wrap. At 36 pt JetBrains Mono, the formula line is approximately 18-19" wide — fits within the 23.0" safe zone.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org:
- **Barlow Condensed ExtraBold** — all headlines and zone labels
- **Barlow SemiBold** — all subheadings, section labels, callout titles
- **Inter Regular** and **Inter Medium** — all body text and table data
- **JetBrains Mono Regular** — all equations, ECE values, and data table values

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Subheading, ASF variable swatch, copper valence callout |
| Teal | `#2EC4B6` | Callout borders/titles, Rate column highlight, Faraday box |
| Emerald | `#27AE60` | High-efficiency bar segments, zinc example accent, Time swatch |
| Coral | `#E05C5C` | Low-efficiency bar segments, chrome example accent, Efficiency swatch |
| Mid Slate | `#3A4055` | Table header fills, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, formula background |
| Alt Row | `#252B3D` | Alternating table rows |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 3.2" — Zone 1/Zone 2 boundary
- 6.4" — Zone 2/Zone 3 boundary
- 19.7" — Zone 3/Zone 4 boundary
- 24.4" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (top 0"–3.2")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Three Questions" callout box (right ~45%)

ZONE 2 — THE MASTER FORMULA (3.2"–6.4" / ~3.2" tall)
  Block C: Large formula box + variable legend strip

ZONE 3 — ECE TABLE + EFFICIENCY (HERO) (6.4"–19.7" / ~13.3" tall)
  Block D: Electrochemical Equivalents master table (left 60%)
  Block E: Cathode Efficiency table (right 40%)

ZONE 4 — EFFICIENCY BAR CHART (19.7"–24.4" / ~4.7" tall)
  Block F: "Where Does the Current Go?" horizontal bar comparison

ZONE 5 — WORKED EXAMPLES + CONVERSIONS (24.4"–32.4" / ~8.0" tall)
  Block G: Two worked examples (left 65%)
  Block H: Unit conversion + Faraday's constant box (right 35%)

ZONE 6 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block I: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Height: 3.2" (Y: 0" to 3.2").
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 12.5"
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: approximately -4
- Text:

> FARADAY'S LAW IN THE SHOP

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: 1.6"
- Width: 12.5"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#E8A020`
- Text:

> Calculating Plating Thickness

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: 2.3"
- Width: 12.5"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> More amps x more time = more metal. Now do the math.

---

**BLOCK B — "Three Questions" Callout Box**

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 13.25". Y: 0.5"
- Width: 10.25". Height: 2.5"
- Fill: `#1E2435`
- Border: 1.5 pt, `#2EC4B6`
- Corner radius: 8 pt

**Callout title:**
- Position: X: 13.55". Y: 0.7"
- Font: Barlow SemiBold, 20 pt
- Color: `#2EC4B6`
- Text:

> EVERY PLATER ASKS THREE QUESTIONS

**Three questions:**
- Position: X: 13.55". Y: 1.15"
- Width: 9.65"
- Font: Inter Medium, 18 pt
- Color: `#F0EDE8`
- Line height: 160%
- Text:

> 1. How thick will my deposit be?
> 2. How long do I need to plate?
> 3. How much current do I need?

**Closing line:**
- Position: X: 13.55". Y: 2.35"
- Font: Inter Medium, 16 pt
- Color: `#2EC4B6`
- Text:

> Faraday's Law answers all three.

---

### ZONE 2 — The Master Formula

**Dimensions:** Full page width. Y: 3.2" to 6.4" (3.2" tall).

---

**BLOCK C — Formula background**

- Element type: Rectangle
- Position: X: 0". Y: 3.2"
- Width: 24.0". Height: 3.2"
- Fill: `#1E2435`

**Formula text:**
- Element type: Text box
- Position: X: centered. Y: 3.6"
- Width: 23.0"
- Font: JetBrains Mono Regular
- Size: 36 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> Thickness = Rate x ASF x Time x Efficiency

**Variable legend strip:**

Four legend items arranged horizontally below the formula, centered as a row.

*Legend item template:*
- Color swatch: Square, 0.3" x 0.3", filled with accent color
- Variable name: Text box, font Inter Medium 14 pt, color `#F0EDE8`, immediately right of swatch
- Description: Text box, font Inter Regular 12 pt, color `#F0EDE8` at 70%, below variable name

**Legend positions (evenly distributed across ~20" centered width):**

*Item 1 — Rate:*
- Swatch position: X: 2.5". Y: 4.6"
- Swatch fill: `#2EC4B6` (Teal)
- Name: `Rate`
- Description: `Plating rate (mil/Ah/ft²) — from the table below`

*Item 2 — ASF:*
- Swatch position: X: 8.0". Y: 4.6"
- Swatch fill: `#E8A020` (Amber)
- Name: `ASF`
- Description: `Current density (amps per square foot)`

*Item 3 — Time:*
- Swatch position: X: 13.5". Y: 4.6"
- Swatch fill: `#27AE60` (Emerald)
- Name: `Time`
- Description: `Hours`

*Item 4 — Efficiency:*
- Swatch position: X: 18.0". Y: 4.6"
- Swatch fill: `#E05C5C` (Coral)
- Name: `Efficiency`
- Description: `Cathode efficiency (decimal)`

---

### ZONE 3 — ECE Table + Efficiency (HERO)

**Dimensions:** Full page width. Y: 6.4" to 19.7" (13.3" tall).
**Background:** Same as page.

---

**BLOCK D — Electrochemical Equivalents Master Table (left 60%)**

**Position:** X: 0.5". Y: 6.4". Width: 13.5".

**Section label:**
- Position: X: 0.5". Y: 6.6"
- Font: Barlow Condensed ExtraBold, 26 pt
- Color: `#F0EDE8`
- Text:

> ELECTROCHEMICAL EQUIVALENTS

**Column header row:**
- Element type: Rectangle
- Position: X: 0.5". Y: 7.1"
- Width: 13.5". Height: 0.5"
- Fill: `#3A4055`

**Column header labels (6 text boxes):**
- Col 1: X: 0.7". Text: `Metal`. Width: 2.1". Font: Barlow SemiBold, 16 pt. Color: `#F0EDE8`
- Col 2: X: 2.8". Text: `Symbol`. Width: 1.1". Same font/size/color
- Col 3: X: 3.9". Text: `Valence`. Width: 1.3". Same
- Col 4: X: 5.2". Text: `ECE (g/Ah)`. Width: 2.4". Same
- Col 5: X: 7.6". Text: `Density (g/cm³)`. Width: 2.6". Same
- Col 6: X: 10.2". Text: `Rate (mil/Ah/ft²)`. Width: 3.5". Font: Barlow SemiBold, 16 pt. Color: `#2EC4B6` (Teal — highlighted column)

**Data rows (10 rows, each 0.6" tall, alternating fills):**

Row Y positions starting at 7.6", incrementing by 0.6":

| Row | Y | Fill | Metal | Symbol | Valence | ECE | Density | Rate |
|-----|---|------|-------|--------|---------|-----|---------|------|
| 1 | 7.60" | `#1A1F2E` | Zinc | Zn | 2 | 1.220 | 7.14 | 0.00152 |
| 2 | 8.20" | `#252B3D` | Nickel | Ni | 2 | 1.095 | 8.90 | 0.00109 |
| 3 | 8.80" | `#1A1F2E` | Copper (acid) | Cu | 2 | 1.186 | 8.96 | 0.00118 |
| 4 | 9.40" | `#252B3D` | Copper (cyanide) | Cu | 1 | 2.372 | 8.96 | 0.00236 |
| 5 | 10.00" | `#1A1F2E` | Chromium (hex) | Cr | 6 | 0.324 | 7.19 | 0.00040 |
| 6 | 10.60" | `#252B3D` | Silver | Ag | 1 | 4.025 | 10.49 | 0.00342 |
| 7 | 11.20" | `#1A1F2E` | Tin | Sn | 2 | 2.214 | 7.31 | 0.00270 |
| 8 | 11.80" | `#252B3D` | Gold (Au⁺) | Au | 1 | 7.349 | 19.32 | 0.00339 |
| 9 | 12.40" | `#1A1F2E` | Gold (Au³⁺) | Au | 3 | 2.450 | 19.32 | 0.00113 |
| 10 | 13.00" | `#252B3D` | Cadmium | Cd | 2 | 2.097 | 8.65 | 0.00216 |

Each row: Rectangle at (X: 0.5", Y: row Y), Width: 13.5", Height: 0.6".

Text positions within each row — same X positions as column headers. Font for Metal column: Inter Medium, 17 pt, `#F0EDE8`. Font for all other columns: JetBrains Mono, 17 pt, `#F0EDE8`. Rate column color: `#2EC4B6` (Teal).

**Table footnote:**
- Position: X: 0.5". Y: 13.7"
- Width: 13.5"
- Font: Inter Regular, 12 pt
- Color: `#F0EDE8` at 60% opacity
- Style: italic
- Text:

> ECE = Atomic Weight / (Valence x 26.80 Ah). Rate = ECE / (Density x 60.5). All values are theoretical — multiply by cathode efficiency for actual deposit.

**Copper valence callout:**
- Position: X: 0.5". Y: 14.2"
- Width: 13.5"
- Font: Inter Regular, 14 pt
- Color: `#E8A020`
- Text:

> Cyanide copper (Cu⁺) deposits 2x the mass per amp-hour vs. acid copper (Cu²⁺) — same element, different chemistry.

---

**BLOCK E — Cathode Efficiency Table (right 40%)**

**Position:** X: 14.5". Y: 6.4". Width: 9.0".

**Section label:**
- Position: X: 14.5". Y: 6.6"
- Font: Barlow Condensed ExtraBold, 22 pt
- Color: `#F0EDE8`
- Text:

> CATHODE EFFICIENCY

**Intro text:**
- Position: X: 14.5". Y: 7.0"
- Width: 9.0"
- Font: Inter Regular, 14 pt
- Color: `#F0EDE8`
- Line height: 140%
- Text:

> Not all current deposits metal. The rest generates hydrogen gas. Efficiency = actual deposit / theoretical maximum.

**Column header row:**
- Element type: Rectangle
- Position: X: 14.5". Y: 7.6"
- Width: 9.0". Height: 0.45"
- Fill: `#3A4055`

**Column headers:**
- Col 1: X: 14.7". Text: `Process`. Width: 5.0". Font: Barlow SemiBold, 16 pt. Color: `#F0EDE8`
- Col 2: X: 19.7". Text: `Efficiency`. Width: 3.6". Same font/color

**Data rows (11 rows, each 0.55" tall, alternating fills):**

Row Y positions starting at 8.05", incrementing by 0.55":

| Row | Y | Fill | Left Border | Process | Efficiency |
|-----|---|------|-------------|---------|-----------|
| 1 | 8.05" | `#1A1F2E` | `#27AE60` | Bright acid copper | 95-100% |
| 2 | 8.60" | `#252B3D` | `#27AE60` | Nickel sulfamate | 95-100% |
| 3 | 9.15" | `#1A1F2E` | `#27AE60` | Silver cyanide | 95-100% |
| 4 | 9.70" | `#252B3D` | `#27AE60` | Watts nickel | 93-97% |
| 5 | 10.25" | `#1A1F2E` | `#27AE60` | Acid chloride zinc | 95-98% |
| 6 | 10.80" | `#252B3D` | `#27AE60` | Matte tin (acid) | 90-95% |
| 7 | 11.35" | `#1A1F2E` | `#E8A020` | Alkaline NC zinc | 70-80% |
| 8 | 11.90" | `#252B3D` | `#E8A020` | Alkaline cyanide zinc | 65-80% |
| 9 | 12.45" | `#1A1F2E` | `#E05C5C` | Cyanide copper strike | 30-60% |
| 10 | 13.00" | `#252B3D` | `#E05C5C` | Hard chrome (hex) | 12-20% |
| 11 | 13.55" | `#1A1F2E` | `#E05C5C` | Decorative chrome (hex) | 10-18% |

Each row: Rectangle at (X: 14.5", Y: row Y), Width: 9.0", Height: 0.55".

**Left border accent:** Rectangle, X: 14.5", Width: 0.06", Height: 0.55", Fill: row-specific color from table above.

Process text: Inter Regular, 16 pt, `#F0EDE8`, X: 14.75".
Efficiency text: JetBrains Mono, 16 pt, `#F0EDE8`, X: 19.7".

---

### ZONE 4 — Efficiency Bar Chart

**Dimensions:** Full page width. Y: 19.7" to 24.4" (4.7" tall).
**Background:** Same as page.

---

**BLOCK F — "Where Does the Current Go?"**

**Section label:**
- Position: X: centered. Y: 19.9"
- Font: Barlow Condensed ExtraBold, 24 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> WHERE DOES THE CURRENT GO?

**Bar chart construction:**

4 horizontal bars, each 0.65" tall, spaced 0.15" apart. Full width from X: 0.5" to X: 23.5" (23.0" total bar width).

*Bar template:*
- Two adjacent rectangles: left = Emerald (metal deposited), right = Coral (wasted)
- Emerald rectangle width = 23.0" x (efficiency / 100)
- Coral rectangle width = 23.0" - Emerald width
- Process label: text box, X: 0.7", vertically centered in bar. Inter Medium, 16 pt, `#F0EDE8`
- Efficiency label on Emerald: JetBrains Mono, 14 pt, `#1A1F2E` (dark on green). Positioned at center of Emerald rectangle
- Waste label on Coral: JetBrains Mono, 12 pt, `#F0EDE8`. Positioned at center of Coral rectangle

**Bar 1 — Acid Copper:**
- Y: 20.5"
- Emerald width: 22.31" (97%). Coral width: 0.69" (3%)
- Label: `Acid Copper` | Emerald label: `97% metal` | Coral label: `3%`

**Bar 2 — Watts Nickel:**
- Y: 21.3"
- Emerald width: 21.85" (95%). Coral width: 1.15" (5%)
- Label: `Watts Nickel` | Emerald label: `95% metal` | Coral label: `5%`

**Bar 3 — Acid Zinc:**
- Y: 22.1"
- Emerald width: 22.08" (96%). Coral width: 0.92" (4%)
- Label: `Acid Zinc` | Emerald label: `96% metal` | Coral label: `4%`

**Bar 4 — Hard Chrome:**
- Y: 22.9"
- Emerald width: 3.45" (15%). Coral width: 19.55" (85%)
- Label: `Hard Chrome` | Emerald label: `15%` | Coral label: `85% wasted as H₂ + heat`

**Caption:**
- Position: X: centered. Y: 23.7"
- Font: Inter Medium, 16 pt
- Color: `#E05C5C`
- Alignment: Center
- Text:

> Hard chrome: 85% of the electrical energy becomes hydrogen gas and heat — not metal.

---

### ZONE 5 — Worked Examples + Conversions

**Dimensions:** Full page width. Y: 24.4" to 32.4" (8.0" tall).
**Background:** Same as page.

---

**BLOCK G — Worked Examples (left 65%)**

**Position:** X: 0.5". Y: 24.4". Width: 14.5".

**Section label:**
- Position: X: 0.5". Y: 24.6"
- Font: Barlow Condensed ExtraBold, 22 pt
- Color: `#F0EDE8`
- Text:

> WORKED EXAMPLES

---

**Example 1 — Zinc:**

*Callout container:*
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 25.1"
- Width: 14.5". Height: 3.0"
- Fill: `#1E2435`
- Corner radius: 6 pt

*Left accent:*
- Rectangle: X: 0.5". Y: 25.1". Width: 0.06". Height: 3.0". Fill: `#27AE60`

*Title:*
- Position: X: 0.85". Y: 25.3"
- Font: Barlow SemiBold, 18 pt
- Color: `#27AE60`
- Text:

> How long to plate 0.5 mil zinc at 20 ASF?

*Calculation:*
- Position: X: 0.85". Y: 25.8"
- Width: 13.9"
- Font: JetBrains Mono Regular, 14 pt
- Color: `#F0EDE8`
- Line height: 160%
- Text:

> Time = Thickness / (Rate x ASF x CE)
> Time = 0.5 / (0.00152 x 20 x 0.96)
> Time = 0.5 / 0.02918
> Time = 17.1 minutes

*Answer:*
- Position: X: 0.85". Y: 27.3"
- Font: Inter Medium, 16 pt
- Color: `#27AE60`
- Text:

> Approximately 17 minutes at 20 ASF.

---

**Example 2 — Hard Chrome:**

*Callout container:*
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 28.3"
- Width: 14.5". Height: 3.3"
- Fill: `#1E2435`
- Corner radius: 6 pt

*Left accent:*
- Rectangle: X: 0.5". Y: 28.3". Width: 0.06". Height: 3.3". Fill: `#E05C5C`

*Title:*
- Position: X: 0.85". Y: 28.5"
- Font: Barlow SemiBold, 18 pt
- Color: `#E05C5C`
- Text:

> How long for 2.0 mil hard chrome at 200 ASF?

*Calculation:*
- Position: X: 0.85". Y: 29.0"
- Width: 13.9"
- Font: JetBrains Mono Regular, 14 pt
- Color: `#F0EDE8`
- Line height: 160%
- Text:

> Time = 2.0 / (0.00040 x 200 x 0.15)
> Time = 2.0 / 0.012
> Time = 166.7 minutes ≈ 2 hr 47 min

*Answer:*
- Position: X: 0.85". Y: 30.5"
- Font: Inter Medium, 16 pt
- Color: `#E05C5C`
- Text:

> Nearly 3 hours — 10x the current density, still takes 10x longer than zinc.

---

**BLOCK H — Unit Conversions + Faraday's Constant (right 35%)**

**Position:** X: 15.5". Y: 24.4". Width: 8.0".

---

**Faraday's Constant callout:**

*Container:*
- Element type: Rounded rectangle
- Position: X: 15.5". Y: 24.8"
- Width: 8.0". Height: 2.8"
- Fill: `#1E2435`
- Border: 1.5 pt, `#2EC4B6`
- Corner radius: 8 pt

*Title:*
- Position: X: 15.8". Y: 25.0"
- Font: Barlow SemiBold, 18 pt
- Color: `#2EC4B6`
- Text:

> FARADAY'S CONSTANT

*Constant:*
- Position: X: centered within container. Y: 25.5"
- Font: JetBrains Mono Regular, 20 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> F = 96,485 C/mol = 26.80 Ah/eq

*Explanation:*
- Position: X: 15.8". Y: 26.2"
- Width: 7.4"
- Font: Inter Regular, 14 pt
- Color: `#F0EDE8`
- Line height: 140%
- Text:

> 26.80 ampere-hours will deposit exactly one gram-equivalent weight of any metal.

---

**Quick Conversions callout:**

*Container:*
- Element type: Rounded rectangle
- Position: X: 15.5". Y: 28.0"
- Width: 8.0". Height: 3.5"
- Fill: `#1E2435`
- Corner radius: 6 pt
- No border

*Title:*
- Position: X: 15.8". Y: 28.2"
- Font: Barlow SemiBold, 16 pt
- Color: `#F0EDE8`
- Text:

> QUICK CONVERSIONS

*Conversion list:*
- Position: X: 15.8". Y: 28.7"
- Width: 7.4"
- Font: JetBrains Mono Regular, 16 pt
- Color: `#F0EDE8`
- Line height: 180%
- Text:

> 1 mil = 25.4 um
> 1 um = 0.0394 mil
> ASF / 10 ≈ ASD
> 1 Ah = 3,600 C

---

### ZONE 6 — Footer Band

**Dimensions:** Full page width. Y: 32.4" to 36.0" (3.6" tall).

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.4"
- Width: 24.0". Height: 3.6"
- Fill: `#0D1020`

**Disclaimer:**
- Position: X: 0.5". Y: 32.8"
- Width: 23.0"
- Font: Inter Regular, 11 pt
- Color: `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster presents theoretical calculations from Faraday's Laws of Electrolysis. Actual deposit thickness depends on cathode efficiency, current distribution, agitation, and bath condition. Always verify critical thickness specifications by direct measurement.

**Poster title:**
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt
- Color: `#F0EDE8`
- Text:

> Faraday's Law in the Shop: Calculating Plating Thickness

**Series name:**
- Position: X: 0.5". Y: 34.0"
- Font: Inter Regular, 13 pt
- Color: `#F0EDE8` at 60% opacity
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Version:**
- Position: X: 0.5". Y: 34.4"
- Font: Inter Regular, 11 pt
- Color: `#F0EDE8` at 40% opacity
- Text:

> v1.0 — 2026

**Logo placeholder:**
- Position: X: 21.0". Y: 33.5"
- Width: 2.5". Height: 1.5"
- Font: Barlow SemiBold, 14 pt
- Color: `#F0EDE8` at 30% opacity
- Alignment: Center
- Text:

> [LOGO]

---

## Part 5 — Grouping and Layer Order

| Group Name | Contains | Lock After Grouping? |
|-----------|----------|---------------------|
| Zone 1 — Header | Blocks A + B | Yes |
| Zone 2 — Formula | Block C (background + formula + legend) | Yes |
| Zone 3 — Tables | Blocks D + E | Yes |
| Zone 4 — Bar Chart | Block F (4 bars + caption) | Yes |
| Zone 5 — Examples | Blocks G + H | Yes |
| Zone 6 — Footer | Block I | Yes |

---

## Part 6 — Light Edition Remap Table

| Element / Role | Dark Edition | Light Edition |
|---|---|---|
| Page background | `#1A1F2E` Gunmetal Dark | `#F0EDE8` Warm White |
| Primary text | `#F0EDE8` Warm White | `#1A1F2E` Gunmetal Dark |
| Amber accent | `#E8A020` | `#B87A10` (darkened 15%) |
| Teal accent | `#2EC4B6` | `#1E9A8F` (darkened 20%) |
| Emerald accent | `#27AE60` | `#1D8A4A` (darkened 20%) |
| Coral accent | `#E05C5C` | `#C43C3C` (darkened 20%) |
| Mid Slate fills | `#3A4055` | `#D0D4DC` (light neutral) |
| Deep Navy footer | `#0D1020` | `#E2E0DB` (light warm gray) |
| Dark Callout fills | `#1E2435` | `#E8E5E0` (light warm fill) |
| Alt Row fills | `#252B3D` | `#F5F3EF` (near-white alternating) |
| Text at reduced opacity | Adjust to match Dark percentages | Same percentages on light equivalents |

**Bar chart special note:** The Emerald bar segments remap to darkened Emerald; Coral segments remap to darkened Coral. Bar labels that are `#1A1F2E` on Emerald (dark text on green in Dark edition) become `#F0EDE8` on darkened Emerald (light text on dark green in Light edition). Verify readability.

**No other overrides required.**

---

## Part 7 — Export Checklist

| Export | Size | Edition | Format | Filename |
|--------|------|---------|--------|----------|
| 1 | 24x36" | Dark | PDF Print (300 DPI) | `Poster-08-Faradays-Law-24x36-Dark.pdf` |
| 2 | 24x36" | Light | PDF Print (300 DPI) | `Poster-08-Faradays-Law-24x36-Light.pdf` |
| 3 | 18x24" | Dark | PDF Print (300 DPI) | `Poster-08-Faradays-Law-18x24-Dark.pdf` |
| 4 | 18x24" | Light | PDF Print (300 DPI) | `Poster-08-Faradays-Law-18x24-Light.pdf` |
| 5 | 24x36" | Dark | PNG (digital download) | `Poster-08-Faradays-Law-24x36-Dark.png` |
| 6 | 24x36" | Light | PNG (digital download) | `Poster-08-Faradays-Law-24x36-Light.png` |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #8 — Faraday's Law — Construction Workup v1.0*
*2026-04-04*
