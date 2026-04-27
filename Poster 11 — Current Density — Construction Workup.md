---
Project: Plating Posters Inc
Poster Number: 11
Title: "Current Density Quick Reference Chart"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 11 — Current Density — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Current Density Quick Reference — Alaina Research Brief v1 (2026-04-03)
Watson Flags: NONE — Drew confirmation on CD ranges is courtesy, not blocking
Process Scope: Multi-process reference chart
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CurrentDensity
  - ConstructionWorkup
---

# Poster # Poster #11 — Construction Workup
## Current Density Quick Reference Chart

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-03*

This document is the construction workup for Poster #11. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 11 — Current Density — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

This is the most table-heavy poster in the series — approximately 70% of the poster is a single large data table. The design handles:
- Text boxes with precise font, size, weight, color control
- Solid-color rectangles for table rows, section headers, accent bars
- Manually constructed table grids (recommended over a native table tool)
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Large table construction:** The master table has 7 section headers + 21 data rows + 1 column header row = 29 rows total. Building this manually is time-intensive but straightforward. **Recommendation: build the column header row, one section header row, and one data row as template groups. Duplicate and modify for all remaining rows.** This saves 70%+ of the build time.

2. **Left accent bars:** Same technique as all previous posters — narrow colored rectangles (0.06" wide) flush against the left edge of each row.

3. **Section header rows with tinted background:** Use the process family accent color at 15% opacity overlaid on the base background. In the design: create a rectangle with the accent color fill, then set transparency to 85% (which gives 15% opacity of the accent over the dark background). Alternatively, calculate the blended hex and use it directly — see the blended hex values provided below.

4. **"—" in Barrel column for rack-only processes:** Use an em dash character, not a hyphen. The Content Draft uses "—" throughout.

5. **JetBrains Mono / font upload:** Same as all previous posters. Should already be uploaded.

6. **Print size 24x36":** Same as all previous posters.

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
- 23.5" — right safe zone

**Horizontal guides (from top edge):**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 28.1" — Zone 2/Zone 3 boundary
- 32.8" — Zone 3/Zone 4 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~60%)
  Block B: CD Formula callout box (right ~40%)

ZONE 2 — MASTER CURRENT DENSITY TABLE (2.9"-28.1" / 25.2" tall)
  Block C: Full-width master table — 7 process family sections, 21 data rows

ZONE 3 — WHAT GOES WRONG + CONVERSION (28.1"-32.8" / 4.7" tall)
  Block D: Too High / Too Low callout (left 60%)
  Block E: Conversion quick reference + cross-ref (right 40%)

ZONE 4 — FOOTER BAND (32.8"-36.0" / 3.2")
  Block F: Disclaimer + title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full width. Y: 0" to 2.9".

---

**BLOCK A — Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 13.5"
- Font: Barlow Condensed ExtraBold, 96 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text: `CURRENT DENSITY`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.6"
- Font: Barlow SemiBold, 40 pt
- Color: `#E8A020`
- Text: `Quick Reference Chart`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.3"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `Right range. Right deposit. Every time.`

---

**BLOCK B — CD Formula Callout**

- Position: X: 14.5". Y: 0.5"
- Width: 9.0". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 20 pt, `#2EC4B6`):
> THE FORMULA

Formula (JetBrains Mono Regular, 28 pt, `#F0EDE8`, centered):
> ASF = Amps / Area (ft²)

Example (Inter Regular, 16 pt, `#F0EDE8` at 80% transparency):
> 10 bolts at 2.5 ft² total, 75 A applied:
> 75 / 2.5 = 30 ASF

Conversion (JetBrains Mono Regular, 14 pt, `#E8A020`):
> ASF / 10 ~ ASD

---

### ZONE 2 — Master Current Density Table

**Dimensions:** Full width. Y: 2.9" to 28.1" (25.2" tall).

**Section label:**
- Position: X: 0.5". Y: 3.0"
- Font: Barlow Condensed ExtraBold, 32 pt, `#F0EDE8`, centered
- Text: `CURRENT DENSITY RANGES BY PROCESS`

---

**TABLE CONSTRUCTION**

Table starts at Y: 3.6" (below section label).
Table width: 23.0" (full content width).

**Column widths:**
| Column | Width | % |
|--------|-------|---|
| Process | 8.1" | 35% |
| Rack (ASF) | 3.7" | 16% |
| Barrel (ASF) | 3.7" | 16% |
| Efficiency | 3.7" | 16% |
| Notes | 3.8" | 17% |

**Column header row:**
- Height: 0.55"
- Fill: `#3A4055` Mid Slate
- Corner radius: 4 pt (top corners only)
- Text: Barlow SemiBold, 20 pt, `#E8A020` Amber
- Headers: `PROCESS` | `RACK (ASF)` | `BARREL (ASF)` | `EFFICIENCY` | `NOTES`
- Alignment: Process = left-aligned; Rack/Barrel/Efficiency = centered; Notes = left-aligned

**Process family section header rows:**
- Height: 0.50"
- Left accent bar: 6 pt, process family accent color
- Background: process family accent color at 15% opacity (pre-blended hex values below)
- Text: Barlow Condensed ExtraBold, 22 pt, process family accent color
- Text spans the full row width (no column splits)

Pre-blended hex values for section header backgrounds (accent at 15% over `#1A1F2E`):
| Family | Accent | Blended BG hex |
|--------|--------|---------------|
| Zinc | Teal `#2EC4B6` | `#1E2740` |
| Copper | Amber `#E8A020` | `#2D2833` |
| Nickel | White `#F0EDE8` | `#22262F` (very subtle) |
| Chrome | Coral `#E05C5C` | `#2D2434` |
| Silver | Emerald `#27AE60` | `#1C2534` |
| Tin | Emerald `#27AE60` | `#1C2534` |
| Other | Slate `#3A4055` | `#212536` |

*Note: These blended values are approximations. In the design, it may be easier to use a rectangle with the accent color fill and set transparency to 85%. Either approach works.*

**Data rows:**
- Height: 0.75" per row (allows for text wrap in Notes column)
- Alternating fill: `#1A1F2E` (base) / `#252B3D` (alt)
- Left accent bar: 4 pt, process family accent color
- Process column: Inter Medium, 18 pt, `#F0EDE8`
- Rack/Barrel/Efficiency columns: JetBrains Mono Regular, 18 pt, `#F0EDE8`, centered
- Notes column: Inter Regular, 14 pt, `#F0EDE8` at 80% transparency

---

**ROW-BY-ROW DATA**

*Build order: Column header > Section header > Data rows for each family. Duplicate the first data row as a template for all subsequent rows.*

**ZINC PLATING** (Teal)
Section header text: `ZINC PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 1 | base | Acid Chloride Zinc (KCl) | 10-40 | 3-15 | 95-98% | Most common zinc process |
| 2 | alt | Alkaline Non-Cyanide Zinc | 10-30 | 5-15 | 70-80% | Insoluble anodes; lower eff. |
| 3 | base | Alkaline Cyanide Zinc | 10-40 | 5-15 | 65-80% | Legacy NaCN; high throwing power |

**COPPER PLATING** (Amber)
Section header text: `COPPER PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 4 | alt | Bright Acid Copper | 15-40 | 5-15 | 95-100% | CuSO₄/H₂SO₄; phosphorized anodes |
| 5 | base | Cyanide Copper Strike | 5-20 | 3-10 | 30-60% | Thin flash — adhesion layer only |

**NICKEL PLATING** (Warm White `#F0EDE8`)
Section header text: `NICKEL PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 6 | alt | Watts Nickel (bright/semi-bright) | 20-60 | 5-20 | 93-97% | Standard decorative + functional |
| 7 | base | Nickel Sulfamate | 20-140 | — | 95-100% | Engineering; 400+ ASF w/ agitation |
| 8 | alt | Nickel Strike (Watts) | 10-50 | — | 90-95% | Active substrates |
| 9 | base | Nickel Strike (Wood's) | 50-250 | — | 50-70% | Stainless steel activation |

**CHROMIUM PLATING** (Coral)
Section header text: `CHROMIUM PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 10 | alt | Decorative Chrome (hex) | 150-300 | — | 10-18% | 5-10x current of other processes |
| 11 | base | Decorative Chrome (trivalent) | 40-150 | 40-100 | 15-25% | Wider window; won't burn |
| 12 | alt | Hard Chrome (conventional) | 150-300 | — | 12-20% | 1-3 A/in²; functional |
| 13 | base | Hard Chrome (mixed catalyst) | 150-300 | — | 20-25% | Fluoride catalyst; higher eff. |

**SILVER PLATING** (Emerald)
Section header text: `SILVER PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 14 | alt | Silver Cyanide Strike | 10-30 | 5-15 | 95-100% | High initial CD; short time |
| 15 | base | Silver Cyanide Plate | 5-15 | 3-10 | 95-100% | Low CD for smooth deposit |

**TIN PLATING** (Emerald)
Section header text: `TIN PLATING`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 16 | alt | Acid Tin (matte, MSA/sulfate) | 10-30 | 5-15 | 90-95% | Zirconium anode baskets |
| 17 | base | Acid Tin (bright) | 10-25 | 5-15 | 90-95% | Organic brighteners added |

**OTHER PROCESSES** (Mid Slate `#3A4055`)
Section header text: `OTHER PROCESSES`

| Row | Fill | Process | Rack | Barrel | Efficiency | Notes |
|-----|------|---------|------|--------|------------|-------|
| 18 | alt | Cadmium (alkaline cyanide) | 5-70 | 5-7 | 90-95% | 15-25 ASF common for still |
| 19 | base | Brass (cyanide) | 10-20 | 10-20 | 50-70% | Color shifts with CD |
| 20 | alt | Zinc-Nickel (acid) | 10-40 | 5-15 | 85-95% | Alloy ratio affected by CD |
| 21 | base | Sulfuric Acid Anodize (Type II) | 12-18 | — | N/A | Oxide growth, not deposition |
| 22 | alt | Hard Coat Anodize (Type III) | 24-36 | — | N/A | Lower temp, higher voltage |

**Table height estimate:** Column header (0.55") + 7 section headers (7 x 0.50" = 3.50") + 22 data rows (22 x 0.75" = 16.50") + section label (0.6") + gaps = approximately 21.8". This fits comfortably within the 25.2" allocation.

**Table footnote:**
- Position: below last row + 0.2" gap
- Font: Inter Regular, 13 pt, `#F0EDE8` at 60% transparency
- Text:

> *All ranges are for normal production plating at typical bath concentrations and temperatures. Extreme conditions (high-speed, pulse, hone) excluded. Barrel CD typically 1/3 to 1/2 of rack CD. "—" = not typically barrel-plated. Efficiency = cathode efficiency. N/A = anodizing (oxide growth, not metal deposition).*

---

### ZONE 3 — What Goes Wrong + Conversion

**Dimensions:** Full width. Y: 28.1" to 32.8" (4.7" tall).

---

**BLOCK D — "What Goes Wrong" (left 60%)**

- Position: X: 0.5". Y: 28.2"
- Width: 13.5". Height: 4.3"
- Fill: `#1E2435` Dark Callout
- Corner radius: 8 pt
- Internal padding: 16 pt

Section label (Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`, centered inside box):
> WHAT GOES WRONG

Two sub-columns inside, side by side:

**Left sub-column — TOO HIGH**
- Title: Barlow SemiBold, 18 pt, `#E05C5C` Coral
- Text: `TOO HIGH`
- Bullet list (Inter Regular, 16 pt, `#F0EDE8`):
  - `Burning — dark, rough, powdery edges`
  - `Hydrogen pitting — trapped gas bubbles`
  - `Poor adhesion — stressed deposit`
  - `Reduced throwing power`

**Right sub-column — TOO LOW**
- Title: Barlow SemiBold, 18 pt, `#2EC4B6` Teal
- Text: `TOO LOW`
- Bullet list (Inter Regular, 16 pt, `#F0EDE8`):
  - `Skip plating — bare spots in LCD zones`
  - `Dull or hazy deposits`
  - `Slow deposition — throughput loss`
  - `Alloy composition shift`

Center divider between sub-columns: vertical line, `#3A4055` Mid Slate, 1 pt, 80% of box height.

---

**BLOCK E — Conversion + Cross-Reference (right 40%)**

- Position: X: 14.25". Y: 28.2"
- Width: 9.25". Height: 4.3"
- Fill: `#1E2435` Dark Callout
- Border: `#3A4055` Mid Slate, 1 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Title (Barlow SemiBold, 18 pt, `#E8A020`):
> QUICK CONVERSIONS

Data (JetBrains Mono Regular, 17 pt, `#F0EDE8`, left-aligned with 8 pt vertical spacing):
> ASF / 10 ~ ASD (exact: / 10.76)
> 1 A/in² = 144 ASF
> 1 A/m² = 0.0929 ASF

Cross-reference (Inter Regular, 15 pt, `#2EC4B6`, with 2 pt Teal left accent rule, positioned below conversions with 16 pt gap):
> See Poster #4 — Reading Your Hull Cell Panel — to visualize current density distribution across a test panel.

---

### ZONE 4 — Footer Band

**Dimensions:** Full width. Y: 32.8" to 36.0" (3.2" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 33.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster is a technical reference tool. Current density ranges reflect general industry practice — consult your process supplier's TDS for product-specific recommendations. Not a substitute for process qualification.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> Current Density Quick Reference Chart

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.0"
> v1.0 — 2026

---

## Part 5 — Table Build Strategy for Elara

This poster's build time is dominated by the 29-row table. Elara should structure the build prompt to minimize repetitive work:

1. **Build the column header row** — get all 5 column widths and positions correct
2. **Build one section header row** — full width, accent bar, text
3. **Build one data row** — all 5 cells, accent bar, correct fonts and sizes
4. **Group the data row** (Ctrl+G)
5. **Duplicate the group 21 times** (Ctrl+D, reposition Y)
6. **For each duplicate:** ungroup, change text content, change fill color (base/alt), change accent bar color per process family
7. **Build section headers** by duplicating the template and changing accent color + text
8. **Stack all rows vertically** with no gap (rows should be flush against each other, separated only by the 1 pt implicit border from adjacent fills)

Estimated build time with this approach: 45-60 minutes for the table alone.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. No overrides required.

| Dark Hex | Light Hex |
|----------|-----------|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

Section header tinted backgrounds: recalculate blends for Light edition, or simply use the Light accent color at 15% opacity over `#F5F4F0`.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #11 — Current Density Quick Reference Chart — Construction Workup v1.0*
*2026-04-03*
