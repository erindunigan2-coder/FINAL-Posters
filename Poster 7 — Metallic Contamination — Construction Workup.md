---
Project: Plating Posters Inc
Poster Number: 7
Title: "Metallic Contamination — Know Your Thresholds"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 7 — Metallic Contamination — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Metallic Contamination Research Brief v1 (2026-04-03)
Watson Flags: TWO — Cu-in-Ni threshold (Drew), include treatment methods (Drew) — non-blocking
Process Scope: Cross-process contamination reference — nickel, copper, chrome, zinc, passivation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - MetallicContamination
  - ConstructionWorkup
---

# Poster # Poster #7 — Construction Workup
## Metallic Contamination — Know Your Thresholds

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #7. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 7 — Metallic Contamination — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

This is the most data-dense poster in the series — the master contamination threshold table is the hero element, supplemented by a tank diagram illustration and treatment callout boxes. The design handles:
- Text boxes with precise font, size, weight, color control
- Solid-color rectangles for table rows, section headers, accent bars, severity indicators
- Manually constructed table grids (recommended over a native table tool)
- Simple shape illustrations for the tank diagram (rectangles + arrows + text labels)
- Callout boxes with accent borders
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Large contamination table:** The hero table has 4 bath-type section headers + 22 data rows + 1 column header row = 27 rows total. Same manual-grid construction as Poster #11. **Recommendation: build the column header, one section header, and one data row as template groups. Duplicate and modify for all remaining rows.** This is critical for time management.

2. **Severity-colored left accent bars:** Each data row has a 4 pt (0.06") left-border accent colored by severity — Coral for danger, Amber for warning, Emerald for safe. Same technique as all previous posters.

3. **Tank diagram illustration (Block C):** A simplified plating tank cross-section built from rectangles (tank walls, electrolyte fill) with 6 labeled arrow groups pointing to contamination sources. This is the same construction approach validated on Posters #4 and #10.

4. **Treatment callout boxes (Block F):** Three stacked callout boxes with different accent colors. Standard callout construction.

5. **Prevention checklist strip (Block G):** A horizontal strip with 6 items. Each item has a checkmark icon and a text label. Use standard checkmark icon (search "checkmark" or "check").

6. **JetBrains Mono / font upload:** Same as all previous posters.

7. **Print size 24x36":** Same as all previous posters.

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
- 7.9" — Zone 2/Zone 3 boundary
- 25.9" — Zone 3/Zone 4 boundary
- 30.9" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Most Dangerous" callout box (right ~45%)

ZONE 2 — HOW METALS GET IN (2.9"-7.9" / 5.0" tall)
  Block C: Tank diagram with 6 contamination source arrows

ZONE 3 — CONTAMINATION TABLE (HERO) (7.9"-25.9" / 18.0" tall)
  Block D: Four-section master threshold table — Nickel | Acid Copper | Hard Chrome | Acid Zinc

ZONE 4 — DETECTION + TREATMENT (25.9"-30.9" / 5.0" tall)
  Block E: Detection methods (left 40%)
  Block F: Treatment quick reference — 3 callout boxes (right 60%)

ZONE 5 — PREVENTION STRIP (30.9"-32.4" / 1.5" tall)
  Block G: Horizontal prevention checklist strip

ZONE 6 — FOOTER BAND (32.4"-36.0" / 3.6")
  Block H: Disclaimer + title + series name + logo + version
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
- Text: `METALLIC CONTAMINATION`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.6"
- Font: Barlow SemiBold, 40 pt
- Color: `#E8A020`
- Text: `Know Your Thresholds`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.3"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `Contamination is always easier to prevent than to remove.`

---

**BLOCK B — "Most Dangerous" Callout**

- Position: X: 13.5". Y: 0.5"
- Width: 9.5". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#E05C5C` Coral, 2 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> MOST DANGEROUS CONTAMINANT PER BATH

List (JetBrains Mono Regular, 15 pt, `#F0EDE8`):
> Nickel:      Cu > 3 ppm
> Acid copper:  Cr⁶⁺ > 2 ppm
> Hard chrome: Cl⁻ > 50 ppm
> Acid zinc:   Cr⁶⁺ > 1 ppm
> Passivation: Fe > 100 ppm

Closing (Inter Medium, 14 pt, `#E05C5C`):
> These are the numbers that turn good parts into scrap.

---

### ZONE 2 — How Metals Get In

**Dimensions:** Full width. Y: 2.9" to 7.9" (5.0" tall).

---

**BLOCK C — Tank Diagram**

**Section label:**
- Position: centered, Y: 3.0"
- Font: Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`
- Text: `HOW CONTAMINATION ENTERS YOUR BATH`

**Tank illustration:**
- Position: centered at X: 12.0", Y: 5.5"
- Tank: Rounded rectangle, 16.0" wide x 3.0" tall
- Fill: `#1E2435` Dark Callout
- Border: `#3A4055` Mid Slate, 2 pt
- Corner radius: 8 pt
- Interior electrolyte suggestion: Two horizontal lines at 30% and 60% height inside tank, `#2EC4B6` at 20% transparency

**Six contamination source arrow groups:**

Each group: a line with arrowhead pointing into the tank, a label (Inter Medium, 14 pt), and a sub-label (Inter Regular, 11 pt, `#F0EDE8` at 70%). Arrow stroke: 2 pt.

**Arrow 1 — Top left (above tank):**
- Arrow points down into tank from above-left
- Arrow color: `#E8A020` Amber
- Position: X: ~3.0", Y: 3.8" (arrow tip touches tank top)
- Label: `Impure anodes` — `#E8A020`
- Sub: `Lead, copper in anode material` — `#F0EDE8` at 70%

**Arrow 2 — Top right (above tank):**
- Arrow points down into tank from above-right
- Arrow color: `#E8A020` Amber
- Position: X: ~19.0", Y: 3.8"
- Label: `Drag-in from other tanks` — `#E8A020`
- Sub: `Chrome, acid, organics carried on parts/racks`

**Arrow 3 — Left side:**
- Arrow points right into tank left wall
- Arrow color: `#E05C5C` Coral
- Position: X: ~1.0", Y: 5.5"
- Label: `Corroding equipment` — `#E05C5C`
- Sub: `Heaters, pumps, tank linings`

**Arrow 4 — Right side:**
- Arrow points left into tank right wall
- Arrow color: `#E05C5C` Coral
- Position: X: ~22.5", Y: 5.5"
- Label: `Dissolving racks` — `#E05C5C`
- Sub: `Iron, copper from steel/brass fixtures`

**Arrow 5 — Bottom center (inside tank):**
- Arrow points down toward tank floor
- Arrow color: `#E05C5C` Coral
- Position: X: ~10.0", Y: 6.5" (inside tank)
- Label: `Dropped parts` — `#E05C5C`
- Sub: `Dissolve in bath over time`

**Arrow 6 — Bottom right:**
- Arrow points left into tank from lower right
- Arrow color: `#E8A020` Amber
- Position: X: ~20.0", Y: 7.0"
- Label: `Make-up water` — `#E8A020`
- Sub: `Iron, copper, calcium from municipal supply`

---

### ZONE 3 — Contamination Table (HERO)

**Dimensions:** Full width. Y: 7.9" to 25.9" (18.0" tall).

**Section label:**
- Position: centered, Y: 8.0"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `CONTAMINATION THRESHOLDS BY BATH TYPE`

---

**TABLE CONSTRUCTION**

Table starts at Y: 8.7" (below section label).
Table width: 23.0" (full content width).

**Column widths:**
| Column | Width | % |
|--------|-------|---|
| Contaminant | 4.1" | 18% |
| Threshold | 3.5" | 15% |
| Effect | 6.9" | 30% |
| Treatment | 5.8" | 25% |
| Severity (accent bar) | 2.7" | 12% |

Note: The "Severity" column is implemented as a left-border accent bar on each row, not as a text column. The 12% width allocation provides visual breathing room on the right side of each row.

**Column header row:**
- Height: 0.50"
- Fill: `#3A4055` Mid Slate
- Corner radius: 4 pt (top corners only)
- Text: Barlow SemiBold, 18 pt, `#F0EDE8`
- Headers: `CONTAMINANT` | `THRESHOLD` | `EFFECT` | `TREATMENT`
- Alignment: all left-aligned

**Bath-type section header rows:**
- Height: 0.45"
- Fill: `#3A4055` Mid Slate
- Text: Barlow SemiBold, 20 pt, accent color per bath type
- Text spans the full row width

Section header accent colors:
| Bath Type | Accent Color |
|-----------|-------------|
| NICKEL BATHS | `#E8A020` Amber |
| ACID COPPER BATHS | `#2EC4B6` Teal |
| HARD CHROME BATHS | `#E05C5C` Coral |
| ACID ZINC BATHS | `#27AE60` Emerald |

**Data rows:**
- Height: 0.65" per row (allows text wrap in Effect and Treatment columns)
- Alternating fill: `#1A1F2E` (base) / `#252B3D` (alt)
- Left accent bar: 4 pt (0.06"), severity-colored
- Contaminant: Inter Medium, 16 pt, `#F0EDE8`
- Threshold: JetBrains Mono Regular, 16 pt, severity-colored (Coral for danger, Amber for warning)
- Effect: Inter Regular, 15 pt, `#F0EDE8`
- Treatment: Inter Regular, 14 pt, `#F0EDE8`

---

**ROW-BY-ROW DATA**

*Build order: Column header > Section header (Nickel) > first data row as template. Duplicate template for all subsequent rows. Then add remaining section headers.*

**SECTION A — NICKEL BATHS** (section header: Amber)

| Row | Fill | Contaminant | Threshold | Effect | Treatment | Severity |
|-----|------|-------------|-----------|--------|-----------|----------|
| 1 | base | Copper (Cu) | >3-5 ppm | Dark LCD deposits; poor adhesion | Dummy at 2-5 ASF | Coral |
| 2 | alt | Zinc (Zn) | >20-50 ppm | White/dark LCD; shiny black streaks | Dummy at 2-5 ASF; pH 5.5 | Coral |
| 3 | base | Iron (Fe) | >50-150 ppm | Speckling; roughness; discoloration | pH 5.0-5.5 + H₂O₂ → filter | Amber |
| 4 | alt | Lead (Pb) | >1-5 ppm | Dark streaks; brittleness | Carbon + electrolytic | Coral |
| 5 | base | Chromium (Cr⁶⁺) | >5-10 ppm | Brightness loss; pitting | Dummy at 1-2 ASF | Coral |
| 6 | alt | Aluminum (Al) | >60 ppm | Reduced limiting CD; rough | Cannot remove — dilute | Amber |
| 7 | base | Cadmium (Cd) | >1-2 ppm | Brittleness; adhesion failure | Dummy; prevent ingress | Coral |

**SECTION B — ACID COPPER BATHS** (section header: Teal)

| Row | Fill | Contaminant | Threshold | Effect | Treatment | Severity |
|-----|------|-------------|-----------|--------|-----------|----------|
| 8 | alt | Iron (Fe) | >500-1000 ppm | Reduced conductivity; rough | Dilute; prevent ingress | Amber |
| 9 | base | Zinc (Zn) | >25 ppm | Brittle, brassy deposits | Dummy at 2 ASF | Amber |
| 10 | alt | Tin (Sn) | >60 ppm | Rough, dark deposits | Dummy plate | Amber |
| 11 | base | Chromium (Cr⁶⁺) | >2-5 ppm | Skip plating; dull deposits | Na₂S₂O₅ → filter | Coral |
| 12 | alt | Chloride (Cl⁻) | >50-80 ppm | Pitting; anode corrosion | Prevent drag-in; no removal | Coral |

**SECTION C — HARD CHROME BATHS** (section header: Coral)

| Row | Fill | Contaminant | Threshold | Effect | Treatment | Severity |
|-----|------|-------------|-----------|--------|-----------|----------|
| 13 | base | Iron (Fe) | >5 g/L | Roughness; reduced coverage | Dummy at low CD (limited) | Amber |
| 14 | alt | Copper (Cu) | >2 g/L | Dark deposits; roughness | Dummy at low CD | Amber |
| 15 | base | Trivalent Cr (Cr³⁺) | >2-3% of total | Poor coverage; dull | Porous pot electrolysis | Coral |
| 16 | alt | Chloride (Cl⁻) | >50 ppm | Severe pitting; etching | Low area/high CD; prevent | Coral |

**SECTION D — ACID ZINC BATHS** (section header: Emerald)

| Row | Fill | Contaminant | Threshold | Effect | Treatment | Severity |
|-----|------|-------------|-----------|--------|-----------|----------|
| 17 | base | Iron (Fe) | >25-50 ppm | Dark; roughness; poor brightness | H₂O₂ at pH 5.5-6.0 → filter | Amber |
| 18 | alt | Copper (Cu) | >10-20 ppm | Dark/reddish LCD; immersion | Dummy at 2-5 ASF | Coral |
| 19 | base | Lead (Pb) | >2-5 ppm | Dark streaks; brittleness | Dummy; prevent ingress | Coral |
| 20 | alt | Chromium (Cr⁶⁺) | >1-2 ppm | Skip plating; poor coverage | Na₂S₂O₅ → filter | Coral |

**Table height estimate:** Column header (0.50") + 4 section headers (4 x 0.45" = 1.80") + 20 data rows (20 x 0.65" = 13.0") + section label (0.7") + gaps = approximately 16.5". Fits within the 18.0" allocation.

---

### ZONE 4 — Detection + Treatment

**Dimensions:** Full width. Y: 25.9" to 30.9" (5.0" tall).

---

**BLOCK E — Detection Methods (left 40%)**

- Position: X: 0.5". Y: 26.0"
- Width: 9.0". Height: 4.6"

Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):
> HOW TO DETECT

Detection table (2 columns: Method | Use):

Table width: 8.5". Column header: `#3A4055` fill.

| Column | Width |
|--------|-------|
| Method | 3.5" |
| Use | 5.0" |

Header text: Barlow SemiBold, 15 pt, `#F0EDE8`.

| Row | Fill | Method | Use |
|-----|------|--------|-----|
| 1 | base | Atomic Absorption (AA) | Gold standard — sub-ppm sensitivity |
| 2 | alt | ICP-OES | Multiple metals simultaneously |
| 3 | base | Hull cell (low CD) | Shop-floor screening — visual |
| 4 | alt | Colorimetric kits | Quick field check (5-50 ppm) |
| 5 | base | Dummying response | Diagnostic — "does dummying help?" |

Row height: 0.55". Font: Inter Regular, 14 pt, `#F0EDE8`. Method column: Inter Medium.

---

**BLOCK F — Treatment Quick Reference (right 60%)**

- Position: X: 9.75". Y: 26.0"
- Width: 13.75". Height: 4.6"

**Three stacked callout boxes, each approximately 4.4" wide x 1.35" tall, positioned vertically:**

**Box 1 — Dummy Plating (Emerald accent):**
- Fill: `#1E2435`. Border: `#27AE60`, 1.5 pt. Corner radius: 6 pt.
- Title (Barlow SemiBold, 15 pt, `#27AE60`): `DUMMY PLATING`
- Body (Inter Regular, 13 pt, `#F0EDE8`): `Corrugated mild steel cathodes at 2-5 ASF for 4-24 hours. Contaminant metals plate out preferentially at low CD. Monitor by Hull cell.`

**Box 2 — Iron Removal (Amber accent):**
- Fill: `#1E2435`. Border: `#E8A020`, 1.5 pt. Corner radius: 6 pt.
- Title (Barlow SemiBold, 15 pt, `#E8A020`): `IRON REMOVAL (NICKEL BATHS)`
- Body (Inter Regular, 13 pt, `#F0EDE8`): `Raise pH to 5.0-5.5. Add H₂O₂ (30%) at 0.1-0.3 mL/L. Iron precipitates as Fe(OH)₃. Filter through 1 um. Lower pH to operating range.`

**Box 3 — Carbon Treatment (Teal accent):**
- Fill: `#1E2435`. Border: `#2EC4B6`, 1.5 pt. Corner radius: 6 pt.
- Title (Barlow SemiBold, 15 pt, `#2EC4B6`): `CARBON TREATMENT`
- Body (Inter Regular, 13 pt, `#F0EDE8`): `2-5 g/L powdered activated carbon. Mix, settle 2-4 hrs, filter through 1 um. Removes organic breakdown products alongside metallic contamination.`

**Stacking:** Box 1 at top, Box 2 in middle, Box 3 at bottom, with 0.15" gaps between boxes.

---

### ZONE 5 — Prevention Strip

**Dimensions:** Full width. Y: 30.9" to 32.4" (1.5" tall).

---

**BLOCK G — Prevention Checklist Strip**

- Position: X: 0.5". Y: 31.0"
- Width: 23.0". Height: 1.2"
- Fill: `#1E2435` Dark Callout
- Corner radius: 6 pt

Title (left-aligned, Barlow SemiBold, 16 pt, `#27AE60`):
> PREVENTION IS CHEAPER THAN TREATMENT

**6 items in a horizontal row across the strip:**

Each item: checkmark icon (`#27AE60`, 0.4" x 0.4") + text label (Inter Regular, 13 pt, `#F0EDE8`).

Items spaced evenly across 23.0" width (~3.6" per item):

1. `Bag your anodes`
2. `Maintain your racks`
3. `Rinse thoroughly`
4. `Test monthly (Ni) / quarterly (Cu, Zn)`
5. `Use pure water (DI/RO)`
6. `Use pure anodes`

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 32.6"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster presents industry-typical contamination thresholds. Specific limits vary by vendor formulation — always check the product TDS. Analysis by AA or ICP is the authoritative method for confirming contamination levels.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> Metallic Contamination — Know Your Thresholds

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.2"
> v1.0 — 2026

---

## Part 5 — Build Strategy for Elara

This poster's build is dominated by the 27-row contamination table and the tank diagram. Elara should structure the prompt as follows:

1. **Build the column header row** — 4 visible columns with correct widths.

2. **Build one section header row** — full width, accent-colored text.

3. **Build one data row** — all 4 cells + left accent bar. Group it.

4. **Duplicate the data row 19 times** — reposition, change text, toggle base/alt fill, change severity accent color.

5. **Build remaining 3 section headers** by duplicating the first and changing accent color + text.

6. **Tank diagram** — tank rectangle first, then 6 arrow groups positioned around it. Each arrow group: line with arrowhead + label + sub-label. Build one, duplicate 5 times, reposition and modify.

7. **Treatment boxes** — build one callout box, duplicate twice, change accent color and text.

8. **Prevention strip** — rectangle + 6 checkmark-label pairs.

Estimated total build time: 60-75 minutes. The table dominates build time but the template-and-duplicate strategy keeps it manageable.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. No overrides required.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, strip fill, tank fill |
| `#252B3D` | `#E8E8F0` | Alternate table rows |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber elements |
| `#2EC4B6` | `#1A8C82` | Teal elements |
| `#27AE60` | `#1E7A47` | Emerald elements |
| `#E05C5C` | `#B83E3E` | Coral elements |
| `#3A4055` | `#D0D4DE` | Table rules, tank border, dividers |

Severity-colored threshold text (Coral, Amber) remaps to darkened Light equivalents. Verify readability against the Light row fills — the darkened Coral (`#B83E3E`) on `#F5F4F0` and `#E8E8F0` should pass WCAG AA easily.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #7 — Metallic Contamination — Construction Workup v1.0*
*2026-04-04*
