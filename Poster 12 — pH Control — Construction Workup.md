---
Project: Plating Posters Inc
Poster Number: 12
Title: "The pH Control Poster"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 12 — pH Control — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — pH Control Research Brief v1 (2026-04-03)
Watson Flags: THREE — A Brite product pH ranges (Drew), acid copper pH listing (Drew), NiCO3 (Tyler) — non-blocking
Process Scope: pH measurement and control — universal across all plating processes
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - pHControl
  - ConstructionWorkup
---

# Poster # Poster #12 — Construction Workup
## The pH Control Poster

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #12. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 12 — pH Control — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

This poster's hero element is a large vertical pH scale with colored process range bars — a visually striking infographic-style element. The design handles:
- Text boxes with precise font, size, weight, color control
- Colored rectangles for the pH scale gradient, process range bars, and data tables
- Rounded rectangles for callout boxes
- Line elements for the pH scale axis and target indicators
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Vertical pH scale with gradient:** The scale runs from pH 0 (top) to pH 14 (bottom), with a color gradient behind it. The generation tool does not support true gradients on custom shapes. **Recommended approach:** Build the gradient as 15 stacked rectangles (one per pH unit), each approximately 0.73" tall, with graduated fill colors. The visual effect approximates a gradient and is fully controllable.

2. **Process range bars:** 13 horizontal bars positioned at their correct pH height on the scale. Each bar is a rounded rectangle with accent-colored fill at 70% opacity, with text labels on left and right ends. These are straightforward rectangles — no special techniques needed.

3. **Target line within each bar:** A thin vertical line (2 pt) at the target pH value inside each bar. This is a simple line element positioned precisely.

4. **Drift effects tables (Zone 3):** Two side-by-side tables with 4 rows each. Standard manual table construction.

5. **Adjustment chemicals table (Zone 4):** 7 rows, 4 columns. Standard table construction.

6. **Buffer concept callout (Zone 5):** Full-width callout box with an embedded compact table. Build the callout box first, then place the table elements inside it.

7. **JetBrains Mono / font upload:** Same as all previous posters.

8. **Print size 24x36":** Same as all previous posters.

---

## Part 2 — Document Setup Instructions

### Step 1 — Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (if not already done)
- Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular, Inter Medium, JetBrains Mono Regular

### Step 4 — Brand Colors (if not already saved)
Same palette as all previous posters — see Series Design Standards Section 3.

### Step 5 — Ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone
- 4.0" — pH scale right edge (scale occupies 0.5"-4.0")
- 12.0" — center divider for two-column sections
- 23.5" — right safe zone

**Horizontal guides (from top edge):**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 14.4" — Zone 2/Zone 3 boundary
- 21.6" — Zone 3/Zone 4 boundary
- 28.8" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Logarithmic Scale" callout box (right ~45%)

ZONE 2 — THE pH SCALE (HERO) (2.9"-14.4" / 11.5" tall)
  Block C: Vertical pH scale (left ~15%) with process range bars (right ~85%)

ZONE 3 — WHAT HAPPENS WHEN pH DRIFTS (14.4"-21.6" / 7.2" tall)
  Block D: "pH Too Low" effects table (left 50%)
  Block E: "pH Too High" effects table (right 50%)

ZONE 4 — ADJUSTMENT + MEASUREMENT (21.6"-28.8" / 7.2" tall)
  Block F: Adjustment chemicals table (left 55%)
  Block G: pH measurement best practices callout (right 45%)

ZONE 5 — BUFFER CONCEPT (28.8"-32.4" / 3.6" tall)
  Block H: Full-width buffer explanation callout with embedded table

ZONE 6 — FOOTER BAND (32.4"-36.0" / 3.6")
  Block I: Disclaimer + title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full width. Y: 0" to 2.9".

---

**BLOCK A — Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 12.5"
- Font: Barlow Condensed ExtraBold, 96 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text: `pH CONTROL`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.6"
- Font: Barlow SemiBold, 40 pt
- Color: `#E8A020`
- Text: `The Number Every Bath Depends On`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.3"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `Small numbers, big chemistry. Know your range.`

---

**BLOCK B — "Logarithmic Scale" Callout**

- Position: X: 13.5". Y: 0.5"
- Width: 9.5". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 18 pt, `#2EC4B6`):
> THE LOGARITHMIC SCALE

Body (Inter Regular, 16 pt, `#F0EDE8`):
> Each whole pH number = 10x change in H⁺ concentration. A bath at pH 4.0 has 10x more acid than pH 5.0, and 100x more than pH 6.0.

Formula (JetBrains Mono Regular, 18 pt, `#F0EDE8`):
> pH = -log[H⁺]

Closing (Inter Medium, 14 pt, `#2EC4B6`):
> Small pH changes = big chemical changes.

---

### ZONE 2 — The pH Scale (HERO)

**Dimensions:** Full width. Y: 2.9" to 14.4" (11.5" tall).

**Section label:**
- Position: centered, Y: 3.0"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `OPERATING pH FOR EVERY MAJOR PROCESS`

---

**SCALE CONSTRUCTION**

The pH scale occupies the left portion of the zone. Process range bars extend to the right.

**pH scale column (left 15%):**

- Position: X: 0.5" to 3.5" (3.0" wide)
- Y: 3.7" to 14.2" (10.5" tall)

**Gradient background:** 15 stacked rectangles, each 3.0" wide x 0.70" tall, positioned vertically from pH 0 (top) to pH 14 (bottom).

Gradient fill colors:
| pH | Fill |
|----|------|
| 0 | `#E05C5C` at 100% |
| 1 | `#E05C5C` at 80% |
| 2 | `#E05C5C` at 60% |
| 3 | `#E8A020` at 60% |
| 4 | `#E8A020` at 40% |
| 5 | `#E8A020` at 25% |
| 6 | `#E8A020` at 15% |
| 7 | `#3A4055` (neutral) |
| 8 | `#2EC4B6` at 15% |
| 9 | `#2EC4B6` at 20% |
| 10 | `#2EC4B6` at 30% |
| 11 | `#2EC4B6` at 40% |
| 12 | `#2EC4B6` at 60% |
| 13 | `#2EC4B6` at 80% |
| 14 | `#2EC4B6` at 100% |

**pH number labels:** On left edge of each rectangle, JetBrains Mono Regular, 18 pt, `#F0EDE8`:
> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

**Axis line:** Vertical line at X: 3.5", from top to bottom of scale, `#3A4055`, 2 pt.

**Scale endpoint labels:**
- Top: `STRONGLY ACIDIC` — Barlow SemiBold, 12 pt, `#E05C5C`
- Middle (pH 7): `NEUTRAL` — Barlow SemiBold, 14 pt, `#F0EDE8`
- Bottom: `STRONGLY ALKALINE` — Barlow SemiBold, 12 pt, `#2EC4B6`

---

**PROCESS RANGE BARS (right 85%):**

Each bar is a horizontal rounded rectangle extending from just right of the axis line (X: 3.8") to the right, positioned vertically at its pH range on the scale.

Bar specifications:
- Height: 0.50" each
- Corner radius: 4 pt
- Opacity: 70%
- Process name label: left end, Inter Medium, 14 pt, `#F0EDE8`
- pH range label: right end, JetBrains Mono, 14 pt, `#F0EDE8`
- Target line: thin vertical line (2 pt, `#F0EDE8`) at target pH within bar

**Bar data and positions:**

Calculate Y position from: Y = 3.7" + (pH value x 0.70")

| Process | pH Range | Bar Color | Y Start | Bar Width |
|---------|----------|-----------|---------|-----------|
| Hard chrome | <1.0 | `#E05C5C` Coral | 3.7" | 12.0" |
| Matte tin | 0.5-2.0 | `#E05C5C` | 4.05" | 12.0" |
| Hex passivation | 0.5-2.0 | `#E05C5C` | 4.05" (offset 0.55" below matte tin) | 10.0" |
| Trivalent passivation | 1.5-2.5 | `#E8A020` Amber | 4.75" | 10.0" |
| Nickel sulfamate | 3.5-4.5 | `#E8A020` | 6.15" | 10.0" |
| Watts nickel | 3.8-4.5 | `#E8A020` | 6.36" (offset below sulfamate) | 12.0" |
| EN (Mid-P) | 4.5-5.2 | `#E8A020` | 6.85" | 12.0" |
| Acid chloride zinc | 4.8-5.8 | `#27AE60` Emerald | 7.06" | 12.0" |
| Alkaline cleaners | 10-13 | `#2EC4B6` Teal | 10.70" | 14.0" |
| Cyanide copper strike | 11-13 | `#2EC4B6` | 11.40" | 12.0" |
| Silver cyanide | 11.5-13 | `#2EC4B6` | 11.75" | 10.0" |
| Alkaline CN zinc | 12-13.5 | `#2EC4B6` | 12.10" | 10.0" |
| Alkaline NC zinc | 12.5-14 | `#2EC4B6` | 12.45" | 12.0" |

**Note:** Where bars overlap in pH space (e.g., Watts nickel and nickel sulfamate), offset the bars vertically by 0.55" so they don't overlap visually. Shorten some bars' horizontal width to prevent visual crowding. Prioritize readability over precise horizontal alignment.

**Key annotation (near EN bar):**
Inter Regular, 11 pt, `#E8A020`:
> EN: ±0.2 tolerance — check every 30-60 min

**Acid copper note (at bottom of scale area):**
Inter Regular, 12 pt, `#F0EDE8` at 60%:
> Acid copper is not pH-controlled — H₂SO₄ concentration is the control variable.

---

### ZONE 3 — What Happens When pH Drifts

**Dimensions:** Full width. Y: 14.4" to 21.6" (7.2" tall).

---

**BLOCK D — "pH Too Low" (left 50%)**

- Position: X: 0.5". Y: 14.5"
- Width: 11.0". Height: 6.8"

Title (Barlow Condensed ExtraBold, 22 pt, `#E05C5C`):
> pH TOO LOW — MORE ACIDIC THAN TARGET

Table (2 columns: Process | Effect):

Table width: 10.5". Column header: `#3A4055` fill.

| Column | Width |
|--------|-------|
| Process | 3.5" |
| Effect | 7.0" |

| Row | Fill | Process | Effect |
|-----|------|---------|--------|
| 1 | base | Acid zinc | Excessive anode dissolution; zinc rises uncontrollably |
| 2 | alt | Watts nickel | Increased H₂ evolution; pitting; embrittlement risk |
| 3 | base | EN (Mid-P) | Higher P content; slower deposition; stabilizer imbalance |
| 4 | alt | Trivalent passivation | Aggressive zinc attack; thinner film; etching |

Row height: 0.70". Font: Inter Regular, 15 pt, `#F0EDE8`. Process column: Inter Medium.
Left-border accent: `#E05C5C` Coral, 4 pt.
Header text: Barlow SemiBold, 16 pt, `#F0EDE8`.

---

**BLOCK E — "pH Too High" (right 50%)**

- Position: X: 12.0". Y: 14.5"
- Width: 11.5". Height: 6.8"

Title (Barlow Condensed ExtraBold, 22 pt, `#E8A020`):
> pH TOO HIGH — MORE ALKALINE THAN TARGET

Same table structure as Block D:

| Row | Fill | Process | Effect |
|-----|------|---------|--------|
| 1 | base | Acid zinc | Brightener precipitation; cloudy solution; Zn(OH)₂ at >6.5 |
| 2 | alt | Watts nickel | Ni(OH)₂ precipitation (green sludge); roughness |
| 3 | base | EN (Mid-P) | Lower P content; faster rate; bath decomposition risk |
| 4 | alt | Trivalent passivation | Thicker film (intentional at 2.5 — Drew's note) |

Left-border accent: `#E8A020` Amber, 4 pt.

---

### ZONE 4 — Adjustment + Measurement

**Dimensions:** Full width. Y: 21.6" to 28.8" (7.2" tall).

---

**BLOCK F — Adjustment Chemicals Table (left 55%)**

- Position: X: 0.5". Y: 21.7"
- Width: 12.5". Height: 6.8"

Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):
> HOW TO ADJUST pH

Table (4 columns):

Table width: 12.0". Column header: `#3A4055` fill.

| Column | Width |
|--------|-------|
| Chemical | 3.0" |
| Formula | 1.8" |
| Direction | 1.5" |
| Typical Process | 5.7" |

Header text: Barlow SemiBold, 15 pt, `#F0EDE8`.

| Row | Fill | Chemical | Formula | Direction | Typical Process |
|-----|------|----------|---------|-----------|-----------------|
| 1 | base | Sodium hydroxide | NaOH | Raise | Acid zinc, nickel, alkaline zinc |
| 2 | alt | Potassium hydroxide | KOH | Raise | Silver baths; some alkaline zinc |
| 3 | base | Nickel carbonate | NiCO₃ | Raise (Ni) | Watts, sulfamate — preferred (adds Ni) |
| 4 | alt | Ammonium hydroxide | NH₄OH | Raise (EN) | EN — avoids cation contamination |
| 5 | base | Sulfuric acid | H₂SO₄ | Lower | Watts nickel, EN, acid copper |
| 6 | alt | Hydrochloric acid | HCl | Lower | Acid zinc (also adds Cl⁻ — caution) |
| 7 | base | Sulfamic acid | H₃NSO₃ | Lower | Sulfamate nickel (avoids Cl⁻/SO₄²⁻) |

Row height: 0.65". Font: Inter Regular, 14 pt, `#F0EDE8`. Chemical column: Inter Medium. Formula column: JetBrains Mono, 14 pt.

**Direction column color coding:**
- "Raise" rows: left accent `#27AE60` Emerald
- "Lower" rows: left accent `#E05C5C` Coral

**Safety callout (below table):**
Inter Medium, 14 pt, `#E05C5C`:
> Always add acid or base slowly, with mixing. Concentrated additions cause exothermic reactions and dangerous splashing.

---

**BLOCK G — pH Measurement Best Practices (right 45%)**

- Position: X: 13.25". Y: 21.7"
- Width: 10.25". Height: 6.8"
- Fill: `#1E2435`
- Border: `#27AE60` Emerald, 1.5 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Title (Barlow SemiBold, 18 pt, `#27AE60`):
> pH MEASUREMENT BEST PRACTICES

Bullet list (Inter Regular, 15 pt, `#F0EDE8`):
> - Calibrate with TWO buffers before every use
>   (pH 4 + 7 for acid; pH 7 + 10 for alkaline)
> - Calibrate at operating temperature (or apply temp correction)
> - Store electrode in KCl storage solution — NEVER in DI water
> - Replace electrode annually (or when response slows)
> - Rinse with DI water between samples

pH paper note (Inter Regular, 13 pt, `#F0EDE8` at 60%):
> pH paper: ±0.5 accuracy — acceptable for cleaners and rinses. Not accurate enough for nickel, EN, or passivation (±0.2 required).

---

### ZONE 5 — Buffer Concept

**Dimensions:** Full width. Y: 28.8" to 32.4" (3.6" tall).

---

**BLOCK H — Buffer Concept Callout**

- Position: X: 0.5". Y: 28.9"
- Width: 23.0". Height: 3.2"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Title (Barlow SemiBold, 20 pt, `#2EC4B6`):
> WHY YOUR BATH HAS BORIC ACID — THE BUFFER CONCEPT

Body (Inter Regular, 16 pt, `#F0EDE8`):
> Buffers resist pH change when acid or base is added. Boric acid — the most common buffer in electroplating — keeps nickel and zinc baths stable during plating, even as the cathode reaction produces H⁺. Without it, pH would swing wildly during operation.

**Embedded buffer table (right side of callout):**

Position: right-aligned inside callout, 8.0" wide.

| Column | Width |
|--------|-------|
| Bath | 3.0" |
| Buffer | 2.5" |
| Range | 2.5" |

| Row | Bath | Buffer | Range |
|-----|------|--------|-------|
| 1 | Watts nickel | Boric acid | pH 3.5-5.0 |
| 2 | Acid zinc | Boric acid | pH 4.5-6.0 |
| 3 | EN baths | Succinic/lactic acid | pH 4.0-5.5 |

Row height: 0.40". Font: Inter Regular, 14 pt. Buffer/Range: JetBrains Mono, 14 pt.

**Closing (below table, Inter Medium, 15 pt, `#2EC4B6`):**
> A well-buffered bath = stable pH = consistent deposits.

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 32.6"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster presents industry-typical pH ranges and adjustment methods. Specific operating parameters vary by product formulation — always consult your product TDS. pH measurement instruments require regular calibration for accurate results.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> The pH Control Poster

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.2"
> v1.0 — 2026

---

## Part 5 — Build Strategy for Elara

This poster's hero element is the pH scale — visually striking but moderately complex to build. Elara should structure the prompt as follows:

1. **Build the pH scale gradient** — 15 stacked rectangles with graduated colors. This is the visual foundation. Place the axis line and pH number labels.

2. **Build one process range bar** — rounded rectangle at correct Y position, with process name and pH range labels. Duplicate 12 times, reposition, change color and text.

3. **Add target lines and annotations** to the bars.

4. **Drift effects tables** (Zone 3) — two side-by-side 4-row tables. Build one, duplicate the structure for the other.

5. **Adjustment chemicals table** — 7 rows, standard construction.

6. **Best practices callout** — standard callout box with bullet list.

7. **Buffer callout** — full-width callout with embedded compact table.

Estimated total build time: 60-75 minutes. The pH scale is the most time-consuming element but involves mostly rectangle duplication and repositioning.

**Build tip for the pH scale:** Build all 15 gradient rectangles first without labels. Then add the 13 process bars. Then add all labels. Working in layers (shapes first, text second) is faster than building each bar completely before moving to the next.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. No overrides required.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout fills |
| `#252B3D` | `#E8E8F0` | Alternate rows |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber elements |
| `#2EC4B6` | `#1A8C82` | Teal elements |
| `#27AE60` | `#1E7A47` | Emerald elements |
| `#E05C5C` | `#B83E3E` | Coral elements |
| `#3A4055` | `#D0D4DE` | Scale axis, table rules, dividers |

**pH scale gradient note:** The gradient rectangles use palette colors at reduced opacity. In the Light edition, remap the base colors (Coral, Amber, Teal) to their darkened equivalents, and maintain the same opacity percentages. The gradient will appear as darkened accent colors on a light background — this actually produces a more vivid gradient effect in the Light edition, which is a visual bonus.

**Process range bars:** Bars use accent colors at 70% opacity. After remap, the darkened accents at 70% on `#F5F4F0` should be clearly visible. Verify bar text (`#1A1F2E` after remap) remains readable against each bar fill. If any bar color is too light, increase opacity to 80-85% in the Light edition.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #12 — pH Control — Construction Workup v1.0*
*2026-04-04*
