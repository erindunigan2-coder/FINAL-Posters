---
Project: Plating Posters Inc
Poster Number: 9
Title: "Anodizing Fundamentals: Type I, II, and III at a Glance"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 9 — Anodizing Fundamentals — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Anodizing Fundamentals Research Brief v1 (2026-04-03)
Watson Flags: THREE — Type II CD range, alloy compatibility, A Brite product names (all Drew, non-blocking)
Process Scope: Anodizing (Types I, II, III per MIL-A-8625) — aluminum only
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - ConstructionWorkup
---

# Poster # Poster #9 — Construction Workup
## Anodizing Fundamentals: Type I, II, and III at a Glance

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #9. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 9 — Anodizing Fundamentals — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

This poster combines a three-column comparison table with two technical illustrations (circuit diagram and pore structure cross-section). The design handles:
- Text boxes with precise font, size, weight, color control
- Three-column table with accent-colored column headers
- Simple circuit diagram built from rectangles, lines, and text (validated approach)
- Pore structure cross-section built from narrow vertical rectangles (columnar structure) on top of horizontal rectangles (substrate and barrier layer)
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Three-column comparison table:** 12 parameter rows + 3 column headers. Each column header is a large accent-colored rounded rectangle. Same manual-grid construction as all previous posters. **Recommendation: build one column header and one data row as templates, then duplicate.**

2. **"Part = Anode" circuit diagram (Block D):** Built from rectangles (rectifier block, tank) and lines (wires, arrows). The rectifier is a rounded rectangle with (+) and (-) labels. Two wire lines run from the rectifier down into a tank rectangle. The part (anode) and counter-electrode (cathode) are rectangles inside the tank. Arrow labels indicate oxide growth direction and H₂ evolution. This is simpler than Poster #10's U-channel illustration.

3. **Pore structure cross-section (Block E):** Built from stacked rectangles. The substrate is a wide horizontal rectangle. The barrier layer is a thin horizontal rectangle on top. The porous columns are 6-8 narrow vertical rectangles rising from the barrier layer. The sealed top is a thin horizontal rectangle across the column tops. Small colored circles (dye dots) are placed in the gaps between columns. This is all standard shape work.

4. **Pre-treatment flow strip (Block G):** 6 boxes connected by arrows. Same construction as any horizontal flowchart — rectangles + text + line arrows.

5. **MIL-A-8625 badge (Block H):** A rounded rectangle with accent border and spec text. Standard callout construction.

6. **Column header text on accent fills:** Amber, Teal, and Coral fills with `#1A1F2E` dark text. In the Light edition, keep text as `#F0EDE8` (Warm White) per the accent-fill override.

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
- 8.17" — column 1/2 boundary (approximate)
- 15.83" — column 2/3 boundary (approximate)
- 23.5" — right safe zone

**Horizontal guides (from top edge):**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 16.2" — Zone 2/Zone 3 boundary
- 23.4" — Zone 3/Zone 4 boundary
- 29.5" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Not Electroplating" callout box (right ~45%)

ZONE 2 — THREE-TYPE COMPARISON TABLE (HERO) (2.9"-16.2" / 13.3" tall)
  Block C: Three-column comparison — Type I | Type II | Type III

ZONE 3 — CONCEPT DIAGRAMS (16.2"-23.4" / 7.2" tall)
  Block D: "Part = Anode" circuit diagram (left 45%)
  Block E: Pore structure cross-section (right 55%)

ZONE 4 — ALLOY + PRE-TREATMENT (23.4"-29.5" / 6.1" tall)
  Block F: Alloy compatibility chart (left 55%)
  Block G: Pre-treatment flow + common defects (right 45%)

ZONE 5 — SPEC + SEALING (29.5"-32.4" / 2.9" tall)
  Block H: MIL-A-8625 badge (left ~40%)
  Block I: Sealing methods strip (right ~60%)

ZONE 6 — FOOTER BAND (32.4"-36.0" / 3.6")
  Block J: Disclaimer + title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full width. Y: 0" to 2.9".

---

**BLOCK A — Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 12.5"
- Font: Barlow Condensed ExtraBold, 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text: `ANODIZING FUNDAMENTALS`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.5"
- Font: Barlow SemiBold, 36 pt
- Color: `#E8A020`
- Text: `Type I, II, and III at a Glance`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.2"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `The part IS the anode. The coating grows from the aluminum itself.`

---

**BLOCK B — "Not Electroplating" Callout**

- Position: X: 13.5". Y: 0.5"
- Width: 9.5". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 18 pt, `#2EC4B6`):
> NOT ELECTROPLATING

Body (Inter Regular, 16 pt, `#F0EDE8`):
> In electroplating, the part is the cathode — metal deposits ON it from solution. In anodizing, the part is the anode — aluminum oxide grows FROM the surface. The coating IS the substrate, chemically converted.

Reaction (JetBrains Mono Regular, 16 pt, `#F0EDE8`):
> 2Al + 3H₂O → Al₂O₃ + 6H⁺ + 6e⁻

---

### ZONE 2 — Three-Type Comparison Table (HERO)

**Dimensions:** Full width. Y: 2.9" to 16.2" (13.3" tall).

**Section label:**
- Position: centered, Y: 3.0"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE THREE TYPES — MIL-A-8625`

---

**TABLE CONSTRUCTION**

Table starts at Y: 3.7" (below section label).
Table width: 23.0" (full content width).

**Column widths:**
| Column | Width |
|--------|-------|
| Row label (left) | 3.7" |
| Type I | 6.1" |
| Type II | 6.1" |
| Type III | 7.1" |

**Column header row:**
- Height: 1.0"
- Row label column: `#3A4055` Mid Slate fill, no text (or blank)
- Type I column: `#E8A020` Amber fill
- Type II column: `#2EC4B6` Teal fill
- Type III column: `#E05C5C` Coral fill
- Corner radius: 6 pt (top corners only)

Column header text (inside accent fills):
- Line 1: Barlow Condensed ExtraBold, 24 pt, `#1A1F2E`
  - `TYPE I` | `TYPE II` | `TYPE III`
- Line 2: Barlow SemiBold, 16 pt, `#1A1F2E`
  - `CHROMIC ACID` | `SULFURIC ACID` | `HARD COAT`

**Data rows:**
- Height: 0.70" per row
- Alternating fill: `#1A1F2E` (base) / `#252B3D` (alt)
- Row label: Inter Medium, 15 pt, `#F0EDE8` at 80%
- Data cells: JetBrains Mono Regular, 16 pt for numerical values, Inter Regular, 16 pt for text values, `#F0EDE8`, centered

---

**ROW-BY-ROW DATA**

| Row | Fill | Label | Type I | Type II | Type III |
|-----|------|-------|--------|---------|----------|
| 1 | base | Electrolyte | CrO₃, 3-10% | H₂SO₄, 15-20% | H₂SO₄, 10-12% |
| 2 | alt | Temperature | 90-100 deg F | 68-72 deg F | 28-36 deg F |
| 3 | base | Current density | 5-10 ASF | 12-18 ASF | 24-36 ASF |
| 4 | alt | Voltage | 0-40 V (ramped) | 15-21 V | 40-100+ V |
| 5 | base | Thickness | 0.05-0.15 mil | 0.2-1.0 mil | 1.0-4.0 mil |
| 6 | alt | Hardness | Moderate | 300-400 HV | 500-700 HV |
| 7 | base | Color | Gray (undyed) | Clear; wide dye range | Dark bronze to black |
| 8 | alt | Dyeability | Limited | Excellent | Limited (dark only) |
| 9 | base | Fatigue impact | Minimal (thin) | Moderate | Significant |
| 10 | alt | Environmental | Cr⁶⁺ — restricted | No Cr⁶⁺ | No Cr⁶⁺ |
| 11 | base | Primary use | Aerospace fatigue-critical | Decorative / general | Wear / engineering |

**Table height estimate:** Column header (1.0") + 11 data rows (11 x 0.70" = 7.7") + section label (0.7") + gaps = approximately 10.0". Fits within the 13.3" allocation, leaving room for callouts below.

**Temperature callout (below table, right-aligned under Type III column):**
- Inter Medium, 14 pt, `#E05C5C`
- Text: `Near freezing — refrigeration required.`

**Dimensional growth callout (centered below table):**
- Inter Medium, 16 pt, `#F0EDE8`
- Text: `Dimensional growth: ~50% outward, ~50% inward. Net gain ≈ half of total oxide thickness.`

---

### ZONE 3 — Concept Diagrams

**Dimensions:** Full width. Y: 16.2" to 23.4" (7.2" tall).

---

**BLOCK D — "Part = Anode" Circuit Diagram (left 45%)**

- Position: X: 0.5". Y: 16.3"
- Width: 10.0". Height: 6.8"

Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):
> HOW ANODIZING WORKS

**Diagram construction:**

**Rectifier block:**
- Rounded rectangle, 3.0" wide x 1.0" tall, `#252B3D` fill, `#3A4055` border 2 pt
- Centered at X: 5.5", Y: 17.5"
- Text inside: `DC RECTIFIER` — Barlow SemiBold, 14 pt, `#F0EDE8`
- (+) label on left side: JetBrains Mono, 14 pt, `#E05C5C`
- (-) label on right side: JetBrains Mono, 14 pt, `#2EC4B6`

**Tank:**
- Rounded rectangle, 8.0" wide x 2.5" tall, `#1E2435` fill, `#3A4055` border 2 pt
- Centered at X: 5.5", Y: 21.0"
- Electrolyte suggestion: horizontal line at 70% height, `#2EC4B6` at 20% opacity
- Label below tank: `H₂SO₄ or CrO₃ electrolyte` — Inter Regular, 11 pt, `#F0EDE8` at 60%

**Wires:**
- Line from (+) terminal down to left element in tank (the part/anode): `#E05C5C`, 2 pt
- Line from (-) terminal down to right element in tank (cathode): `#2EC4B6`, 2 pt

**Part (anode) — left side of tank:**
- Rectangle, 1.5" wide x 1.5" tall, `#C8D0D8` Bright Silver (aluminum)
- Label below: `ANODE — The Part` — Barlow SemiBold, 12 pt, `#E8A020`
- Oxide layer: thin rectangle on surface, `#E8A020` at 40% opacity, 0.1" thick
- Arrow from oxide layer outward: `Oxide grows FROM surface` — Inter Medium, 12 pt, `#2EC4B6`

**Counter-electrode (cathode) — right side of tank:**
- Rectangle, 0.8" wide x 1.5" tall, `#3A4055` Mid Slate
- Label below: `CATHODE` — Barlow SemiBold, 12 pt, `#2EC4B6`
- Small arrow with bubbles: `H₂ gas` — Inter Regular, 11 pt, `#F0EDE8` at 70%

**Key contrast callout (below diagram):**
Inter Medium, 15 pt, `#E8A020`:
> Electroplating: part is cathode, metal deposits ON it.
> Anodizing: part is anode, oxide grows FROM it.

---

**BLOCK E — Pore Structure Cross-Section (right 55%)**

- Position: X: 11.0". Y: 16.3"
- Width: 12.5". Height: 6.8"

Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):
> THE PORE STRUCTURE

**Cross-section construction:**

All elements centered within block area.

**1. Aluminum substrate (bottom):**
- Rectangle: 8.0" wide x 0.8" tall
- Fill: `#3A4055` Mid Slate
- Label inside: `ALUMINUM` — Barlow SemiBold, 14 pt, `#F0EDE8`
- Position: Y: ~22.0"

**2. Barrier layer (on top of substrate):**
- Rectangle: 8.0" wide x 0.15" tall
- Fill: `#E8A020` Amber
- Label (right side, arrow pointing): `Barrier layer (dense oxide)` — Inter Regular, 11 pt, `#E8A020`

**3. Porous columns (rising from barrier layer):**
- 7 narrow vertical rectangles
- Each: 0.4" wide x 2.5" tall
- Fill: `#2EC4B6` Teal at 60% transparency
- Spaced evenly with 0.35" gaps between them (the pore channels)
- The gaps (background showing through as `#1A1F2E`) represent the pore channels

**4. Dye dots (inside pore channels):**
- Small circles, 0.2" diameter, placed in 3-4 of the pore channels at mid-height
- Colors: varied — use `#E05C5C` (red dye), `#2EC4B6` (blue dye), `#1A1F2E` (black dye)
- Label (arrow from dots): `Dye trapped in pores` — Inter Regular, 11 pt, `#F0EDE8`

**5. Sealed tops (across column tops):**
- Rectangle: 8.0" wide x 0.12" tall
- Fill: `#C8D0D8` Bright Silver
- Label (arrow pointing): `Sealed (hydrated oxide)` — Inter Regular, 11 pt, `#C8D0D8`

**Caption (below cross-section):**
Inter Regular, 14 pt, `#F0EDE8`:
> The hexagonal cell structure gives anodizing its unique properties: permanent dye absorption, corrosion resistance, and electrical insulation.

---

### ZONE 4 — Alloy Compatibility + Pre-Treatment

**Dimensions:** Full width. Y: 23.4" to 29.5" (6.1" tall).

---

**BLOCK F — Alloy Compatibility Chart (left 55%)**

- Position: X: 0.5". Y: 23.5"
- Width: 12.5". Height: 5.8"

Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):
> ALLOY COMPATIBILITY

**Table (3 columns):**

Table width: 12.0". Column header: `#3A4055` fill.

| Column | Width |
|--------|-------|
| Alloy Series | 3.5" |
| Example | 3.0" |
| Anodizing Quality | 5.5" |

Header text: Barlow SemiBold, 15 pt, `#F0EDE8`.

| Row | Fill | Alloy Series | Example | Quality | Left accent |
|-----|------|-------------|---------|---------|-------------|
| 1 | base | 1xxx (pure Al) | 1100 | Excellent — clear, consistent | Emerald |
| 2 | alt | 5xxx (Al-Mg) | 5052 | Very good — clear to light gray | Emerald |
| 3 | base | 6xxx (Al-Mg-Si) | 6061, 6063 | Very good — 6063 = best architectural | Emerald |
| 4 | alt | 2xxx (Al-Cu) | 2024 | Fair to poor — yellowish oxide | Amber |
| 5 | base | 7xxx (Al-Zn) | 7075 | Fair — color inconsistency | Amber |
| 6 | alt | Cast alloys | A356, 380 | Variable — silicon causes dark/grainy | Coral |

Row height: 0.60". Font: Inter Regular, 14 pt, `#F0EDE8`. Left accent: 4 pt, colored per quality rating.

**Key note (below table):**
Inter Medium, 14 pt, `#E8A020`:
> Higher alloying elements (Cu, Si) = worse anodizing. Pure Al and 6xxx produce the best results.

---

**BLOCK G — Pre-Treatment Flow + Common Defects (right 45%)**

- Position: X: 13.25". Y: 23.5"
- Width: 10.25". Height: 5.8"

**Pre-treatment flow strip:**

6 boxes connected by arrows, arranged horizontally in two rows of 3:

Row 1: `CLEAN` → `ETCH` → `DESMUT`
Row 2: `ANODIZE` → `DYE` → `SEAL`

Each box: 2.5" wide x 0.6" tall, `#252B3D` fill, `#3A4055` border 1 pt, corner radius 4 pt.
Text: Barlow SemiBold, 12 pt, `#F0EDE8`.
Arrows: `#3A4055`, 1.5 pt, with arrowheads.

**Process notes (below flow):**
Inter Regular, 12 pt, `#F0EDE8` at 70%:
> Caustic etch: NaOH, 4-8 oz/gal, 140 deg F, 1-5 min
> Desmut: HNO₃ or HNO₃/HF, room temp, 15-60 sec

**Common Defects table:**

Title: Barlow SemiBold, 16 pt, `#E05C5C`:
> COMMON DEFECTS

| Row | Fill | Defect | Cause |
|-----|------|--------|-------|
| 1 | base | Uneven color | Inconsistent oxide; alloy variation |
| 2 | alt | Chalky oxide | Temp too high; over-processed |
| 3 | base | Burning | High CD; poor contact |
| 4 | alt | Poor dye absorption | Oxide too thin; over-sealed |
| 5 | base | Streaking | Poor cleaning; alloy segregation |

Row height: 0.45". Font: Inter Regular, 13 pt, `#F0EDE8`. Left accent: `#E05C5C` Coral, 4 pt.

---

### ZONE 5 — Spec Badge + Sealing Methods

**Dimensions:** Full width. Y: 29.5" to 32.4" (2.9" tall).

---

**BLOCK H — MIL-A-8625 Badge (left ~40%)**

- Position: X: 0.5". Y: 29.6"
- Width: 9.0". Height: 2.5"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 2 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Spec title (Barlow Condensed ExtraBold, 24 pt, `#2EC4B6`):
> MIL-A-8625F

Sub-text (Inter Regular, 13 pt, `#F0EDE8`):
> The governing specification for anodic coatings on aluminum

---

**BLOCK I — Sealing Methods (right ~60%)**

- Position: X: 10.0". Y: 29.6"
- Width: 13.5". Height: 2.5"

Title (Barlow SemiBold, 16 pt, `#F0EDE8`):
> SEALING METHODS

4 entries in a compact grid (JetBrains Mono, 13 pt, `#F0EDE8`):

> Hot water: 200-212 deg F — standard
> Nickel acetate: 180-200 deg F — aerospace
> Cold seal (NiF): 75-85 deg F — energy savings
> PTFE: variable — lubricity for hard coat

Each entry on its own line. Left accent dots: small circles (0.15" diameter) in `#2EC4B6` Teal preceding each entry.

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 32.6"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster presents anodizing fundamentals per MIL-A-8625F. Operating parameters vary by alloy, tank configuration, and product specification. Consult your process supplier for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> Anodizing Fundamentals: Type I, II, and III at a Glance

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.2"
> v1.0 — 2026

---

## Part 5 — Build Strategy for Elara

This poster has diverse elements — a comparison table, two illustrations, an alloy table, a flowchart, and a defect table. Elara should structure the prompt in this order:

1. **Three-column comparison table** — build column headers with accent fills first. Build one data row, duplicate 10 times. This is the HERO and should be completed first.

2. **Circuit diagram** — rectifier block, tank, two wire lines, anode/cathode rectangles, labels. Build top to bottom.

3. **Pore structure** — substrate rectangle, barrier layer, 7 column rectangles, dye dots, sealed top. Build bottom to top.

4. **Alloy table** — 6 rows with quality-coded left accents. Standard table construction.

5. **Pre-treatment flow** — 6 boxes with arrows. Build one box, duplicate 5 times, connect.

6. **Defect table** — 5 compact rows. Standard construction.

7. **MIL-A-8625 badge and sealing strip** — standard callout construction.

Estimated total build time: 75-90 minutes. The two illustrations add time but are built from simple shapes.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. One override required.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout fills, badge fill, tank fill |
| `#252B3D` | `#E8E8F0` | Alternate rows, flow boxes, rectifier |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber elements (Type I, barrier layer) |
| `#2EC4B6` | `#1A8C82` | Teal elements (Type II, columns) |
| `#27AE60` | `#1E7A47` | Emerald elements |
| `#E05C5C` | `#B83E3E` | Coral elements (Type III, defects) |
| `#3A4055` | `#D0D4DE` | Table rules, dividers, substrate, tank border |
| `#C8D0D8` | `#C8D0D8` | Bright Silver (sealed top, aluminum part) — **unchanged** |

**Override:** Column header text on Amber, Teal, and Coral fills — keep as `#F0EDE8` (Warm White) in Light edition. The darkened accent fills have insufficient contrast with `#1A1F2E` text.

**Pore structure note:** The column rectangles use `#2EC4B6` at 60% opacity. In the Light edition, the darkened Teal (`#1A8C82`) at 60% opacity should still read clearly against `#F5F4F0`. Verify at build time. The dye dots inside pore channels retain their original colors — they represent actual dye colors, not design accent colors.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #9 — Anodizing Fundamentals — Construction Workup v1.0*
*2026-04-04*
