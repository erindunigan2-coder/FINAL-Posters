---
Project: Plating Posters Inc
Poster Number: 3
Title: "Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 3 — Zinc Plating at a Glance — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Zinc Plating at a Glance Research Brief v1 (2026-04-04)
Watson Flags: THREE — throwing power ratios (Tyler), NZP P1/P2 (Tyler), KCl emphasis (Drew) — non-blocking
Process Scope: Zinc plating — acid chloride and alkaline non-cyanide
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincPlating
  - ConstructionWorkup
---

# Poster # Poster #3 — Construction Workup
## Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #3. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 3 — Zinc Plating at a Glance — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

This is a comparison poster — the core is a two-column data table and supporting illustrations built from simple shapes. The design handles:
- Text boxes with precise font, size, weight, color control
- Solid-color rectangles for table rows, column headers, accent bars
- Manually constructed table grids (recommended over a native table tool)
- Line segments for the CE concept graph
- Rectangles for the throwing power illustration (deposit thickness layers)
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Two-column comparison table:** The master table has 16 data rows + 1 column header row. Same manual-grid construction as all previous posters. **Recommendation: build the column header row and one data row as template groups. Duplicate and modify for all remaining rows.**

2. **Throwing power cross-sections:** Built as layered rectangles — same technique validated on Poster #4 (Hull cell panel) and Poster #10 (U-channel deposit). The U-channel/recess shape is a set of three rectangles forming a trough, with `#C8D0D8` deposit-layer rectangles of varying widths layered on top.

3. **CE concept graph:** Built from the line tool. The acid zinc "flat line" is a single horizontal line segment. The alkaline zinc "curve" is 3-4 connected line segments approximating a decline. Axis lines are simple vertical/horizontal lines.

4. **Left accent bars on table rows:** Same technique as all previous posters — narrow colored rectangles (0.06" wide) flush against left edge.

5. **Amber and Teal column header fills:** These serve as column identification throughout the table. In the Light edition, keep text as `#F0EDE8` on these fills per the accent-fill override.

6. **JetBrains Mono / font upload:** Same as all previous posters. Should already be uploaded.

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
- 12.0" — center column divider (approximate mid-point for two-column content)
- 23.5" — right safe zone

**Horizontal guides (from top edge):**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 18.0" — Zone 2/Zone 3 boundary
- 24.5" — Zone 3/Zone 4 boundary
- 29.5" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Why Two Systems?" callout box (right ~45%)

ZONE 2 — MASTER COMPARISON TABLE (2.9"-18.0" / 15.1" tall)
  Block C: Full-width two-column comparison table — 16 parameter rows

ZONE 3 — THROWING POWER + CE CONCEPT (18.0"-24.5" / 6.5" tall)
  Block D: Throwing power illustration (left 55%)
  Block E: Cathode efficiency concept graph (right 45%)

ZONE 4 — DECISION GUIDE + PASSIVATION (24.5"-29.5" / 5.0" tall)
  Block F: "When to choose which" checklist (left 55%)
  Block G: Passivation compatibility table (right 45%)

ZONE 5 — SPECS + COMMON PROBLEMS (29.5"-32.4" / 2.9" tall)
  Block H: ASTM B633 service conditions (left 50%)
  Block I: Common problems quick reference (right 50%)

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
- Text: `ZINC PLATING AT A GLANCE`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.5"
- Font: Barlow SemiBold, 36 pt
- Color: `#E8A020`
- Text: `Acid Chloride vs. Alkaline Non-Cyanide`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.2"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `Same goal. Different chemistry. Know the difference.`

---

**BLOCK B — "Why Two Systems?" Callout**

- Position: X: 13.5". Y: 0.5"
- Width: 9.5". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#2EC4B6` Teal, 1.5 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 18 pt, `#2EC4B6`):
> WHY TWO SYSTEMS?

Body (Inter Regular, 16 pt, `#F0EDE8`):
> Both produce sacrificial zinc coatings that protect steel from corrosion. Acid zinc is fast and bright. Alkaline zinc throws better and bends without cracking. The right choice depends on your part and your spec.

Contact your process chemistry supplier for recommended products for each system (JetBrains Mono Regular, 14 pt, `#E8A020` at 60%):
> Consult your supplier's TDS for acid chloride and alkaline non-cyanide zinc formulations

---

### ZONE 2 — Master Comparison Table

**Dimensions:** Full width. Y: 2.9" to 18.0" (15.1" tall).

**Section label:**
- Position: X: 0.5". Y: 3.0"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered
- Text: `HEAD-TO-HEAD: EVERY PARAMETER THAT MATTERS`

---

**TABLE CONSTRUCTION**

Table starts at Y: 3.6" (below section label).
Table width: 23.0" (full content width).

**Column widths:**
| Column | Width | % |
|--------|-------|---|
| Parameter | 6.4" | 28% |
| Acid Chloride | 8.3" | 36% |
| Alkaline Non-Cyanide | 8.3" | 36% |

**Column header row:**
- Height: 0.60"
- Parameter column: `#3A4055` Mid Slate fill. Text: `PARAMETER` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Acid column: `#E8A020` Amber fill. Text: `ACID CHLORIDE` — Barlow SemiBold, 18 pt, `#1A1F2E`
- Alkaline column: `#2EC4B6` Teal fill. Text: `ALKALINE NON-CYANIDE` — Barlow SemiBold, 18 pt, `#1A1F2E`
- Corner radius: 4 pt (top corners only)

**Data rows:**
- Height: 0.65" per row
- Alternating fill: `#1A1F2E` (base) / `#252B3D` (alt)
- Parameter column text: Inter Medium, 16 pt, `#F0EDE8`, left-aligned
- Data column text: JetBrains Mono Regular, 16 pt, `#F0EDE8` for numerical values; Inter Regular, 16 pt for text-only values; centered

---

**ROW-BY-ROW DATA**

*Build the column header first, then one data row as a template. Duplicate the row 15 times and modify content/fills.*

| Row | Fill | Parameter | Acid Chloride | Alkaline Non-Cyanide |
|-----|------|-----------|---------------|----------------------|
| 1 | base | Primary salt | KCl 180-250 g/L | NaOH 100-140 g/L |
| 2 | alt | Zinc metal | 15-30 g/L (2.0-4.0 oz/gal) | 8-15 g/L (1.1-2.0 oz/gal) |
| 3 | base | pH | 4.5-5.5 (target 4.8-5.2) | 13-14 |
| 4 | alt | Temperature | 20-30 C (68-86 F) | 22-30 C (72-86 F) |
| 5 | base | Rack CD | 2-5 A/dm² (19-46 ASF) | 1-4 A/dm² (9-37 ASF) |
| 6 | alt | Barrel CD | 0.3-1.5 A/dm² (3-14 ASF) | 0.3-1.5 A/dm² (3-14 ASF) |
| 7 | base | Cathode efficiency | 95-98% | 60-80% |
| 8 | alt | Throwing power | Moderate | Excellent |
| 9 | base | Anode type | Soluble zinc (SHG 99.99%) | Insoluble mild steel |
| 10 | alt | A:C ratio | 2:1 | 2:1 rack / 2.5:1 barrel |
| 11 | base | Buffer | Boric acid (25-45 g/L) | NaOH (inherent stability) |
| 12 | alt | Critical ratio | Zn:boric acid balance | NaOH:Zn 9:1-12:1 |
| 13 | base | Deposit appearance | Bright to semi-bright | Semi-bright to matte |
| 14 | alt | Deposit ductility | Good | Excellent |
| 15 | base | Iron limit | <50 ppm (action at 25) | <20 ppm (action at 10) |
| 16 | alt | Copper limit | <10 ppm (action at 5) | <5 ppm (action at 2) |

**Table height estimate:** Column header (0.60") + 16 data rows (16 x 0.65" = 10.4") + section label (0.6") + gaps = approximately 12.0". This fits well within the 15.1" allocation, leaving room for the footnote and breathing space.

**Table footnote:**
- Position: below last row + 0.2" gap
- Font: Inter Regular, 13 pt, `#F0EDE8` at 60% transparency
- Text:

> *Ranges are for normal production plating. NH₄Cl systems: similar parameters with additional buffering capacity and ammonia-bearing wastewater. Consult your product TDS for formulation-specific operating ranges.*

---

### ZONE 3 — Throwing Power + CE Concept

**Dimensions:** Full width. Y: 18.0" to 24.5" (6.5" tall).

---

**BLOCK D — Throwing Power Illustration (left 55%)**

- Position: X: 0.5". Y: 18.1"
- Width: 12.5". Height: 6.2"

Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):
> THROWING POWER — THE KEY DIFFERENCE

**Two U-channel cross-sections, side by side, centered in the block area:**

Each U-channel is built from three rectangles forming a trough shape:
- Base rectangle (horizontal): 2.5" wide x 0.3" tall, `#3A4055`
- Left wall (vertical): 0.3" wide x 2.0" tall, `#3A4055`
- Right wall (vertical): 0.3" wide x 2.0" tall, `#3A4055`

**Left U-channel — Acid Zinc:**
- Position: centered at X ~2.5"
- Deposit layer (`#C8D0D8` Bright Silver) applied to all inner surfaces:
  - Top edges of walls: 0.15" thick (wide)
  - Inner wall surfaces: 0.08" thick (medium)
  - Bottom of recess: 0.03" thick (thin)
- Label above: `ACID CHLORIDE` — Barlow SemiBold, 14 pt, `#E8A020`
- Annotation arrows (Inter Regular, 11 pt, `#F0EDE8` at 80%):
  - Arrow to thick edge: `Thick at HCD`
  - Arrow to thin recess: `Thin at LCD`
- Below channel: `3:1 to 5:1 variation` — JetBrains Mono, 13 pt, `#E8A020`

**Right U-channel — Alkaline Zinc:**
- Position: centered at X ~8.5"
- Deposit layer (`#C8D0D8`) applied more uniformly:
  - Top edges: 0.10" thick
  - Inner walls: 0.08" thick
  - Bottom recess: 0.07" thick
- Label above: `ALKALINE NC` — Barlow SemiBold, 14 pt, `#2EC4B6`
- Annotation: `Uniform coverage` — Inter Regular, 11 pt, `#F0EDE8` at 80%
- Below channel: `1.5:1 to 2:1 variation` — JetBrains Mono, 13 pt, `#2EC4B6`

**Caption (centered below both channels):**
Inter Medium, 14 pt, `#F0EDE8`:
> Same part. Same spec. Different distribution. Alkaline zinc's variable efficiency redistributes metal toward recesses.

---

**BLOCK E — Cathode Efficiency Concept (right 45%)**

- Position: X: 13.5". Y: 18.1"
- Width: 10.0". Height: 6.2"

Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):
> WHY ALKALINE ZINC THROWS BETTER

**Graph construction:**

Graph area: 9.0" wide x 3.5" tall, positioned below section label.

- Y-axis line: vertical, `#3A4055`, 2 pt, from bottom-left to top-left of graph area
- X-axis line: horizontal, `#3A4055`, 2 pt, along bottom of graph area
- Y-axis label: `Cathode Efficiency (%)` — JetBrains Mono, 12 pt, `#F0EDE8` at 70%, rotated 90 degrees (vertical text)
- X-axis label: `Current Density (ASF)` — JetBrains Mono, 12 pt, `#F0EDE8` at 70%
- Y-axis tick marks: `60%`, `80%`, `100%` — JetBrains Mono, 11 pt, `#F0EDE8` at 60%
- X-axis tick marks: `Low`, `High` — JetBrains Mono, 11 pt, `#F0EDE8` at 60%

**Acid zinc line:**
- Single horizontal line from left to right at ~95% height
- Color: `#E8A020` Amber, 3 pt stroke
- Label (right end): `Acid: 95-98%` — Inter Medium, 13 pt, `#E8A020`

**Alkaline zinc line:**
- 3-4 connected line segments from ~80% at left edge declining to ~60% at right edge
- Color: `#2EC4B6` Teal, 3 pt stroke
- Label (right end): `Alkaline: 80% → 60%` — Inter Medium, 13 pt, `#2EC4B6`

**Key insight (below graph):**
Inter Medium, 14 pt, `#2EC4B6`:
> Variable efficiency = self-leveling. LCD areas plate more efficiently, naturally pushing metal into recesses.

---

### ZONE 4 — Decision Guide + Passivation

**Dimensions:** Full width. Y: 24.5" to 29.5" (5.0" tall).

---

**BLOCK F — "When to Choose Which" (left 55%)**

- Position: X: 0.5". Y: 24.6"
- Width: 12.5". Height: 4.6"
- Fill: `#1E2435` Dark Callout
- Corner radius: 8 pt
- Internal padding: 16 pt

Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`, centered inside box):
> WHEN TO CHOOSE WHICH

Two sub-columns inside, side by side:

**Left sub-column — CHOOSE ACID**
- Title: Barlow SemiBold, 16 pt, `#E8A020`
- Text: `CHOOSE ACID WHEN:`
- Bullet list (Inter Regular, 14 pt, `#F0EDE8`):
  - `Simple geometry (flat, cylindrical)`
  - `High throughput required`
  - `Bright appearance matters`
  - `Barrel plating small parts`
  - `New installation — easier operation`
  - `Ammonia-free wastewater (KCl)`

**Right sub-column — CHOOSE ALKALINE**
- Title: Barlow SemiBold, 16 pt, `#2EC4B6`
- Text: `CHOOSE ALKALINE WHEN:`
- Bullet list (Inter Regular, 14 pt, `#F0EDE8`):
  - `Complex geometry (recesses, threads)`
  - `Tight thickness tolerance`
  - `Paint/powder coat adhesion critical`
  - `High-strength steel (reduced H₂ risk)`
  - `Uniform passivate color needed`
  - `Customer spec requires it`

Center divider: vertical line, `#3A4055` Mid Slate, 1 pt, 80% of box height.

Closing (Inter Medium, 13 pt, `#F0EDE8` at 70%, centered below columns):
> Neither is universally better. The right choice depends on the part and the spec.

---

**BLOCK G — Passivation Compatibility (right 45%)**

- Position: X: 13.25". Y: 24.6"
- Width: 10.25". Height: 4.6"

Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):
> PASSIVATION COMPATIBILITY

**Passivation table:**

Table width: 9.75". Column header: `#3A4055` fill.

| Column | Width |
|--------|-------|
| Passivation | 4.0" |
| Salt Spray (white) | 3.0" |
| RoHS | 2.75" |

Header text: Barlow SemiBold, 14 pt, `#F0EDE8`.

| Row | Fill | Passivation | Salt Spray | RoHS |
|-----|------|-------------|------------|------|
| 1 | base | Clear/blue trivalent | 72-120 hrs | Yes |
| 2 | alt | Yellow trivalent | 120-200 hrs | Yes |
| 3 | base | Black trivalent | 72-120 hrs | Yes |
| 4 | alt | Yellow hex (legacy) | 96-240 hrs | No |
| 5 | base | Olive drab hex | 200+ hrs | No |

Row height: 0.50". Font: Inter Regular, 13 pt, `#F0EDE8`. JetBrains Mono for hour values.

**RoHS column color coding:**
- "Yes" text: `#27AE60` Emerald
- "No" text: `#E05C5C` Coral

**Key note (below table, Inter Medium, 13 pt, `#27AE60`):**
> Both zinc bath types are compatible with trivalent and hexavalent passivation chemistries. Consult your supplier for recommended passivate products.

---

### ZONE 5 — Specs + Common Problems

**Dimensions:** Full width. Y: 29.5" to 32.4" (2.9" tall).

---

**BLOCK H — ASTM B633 Service Conditions (left 50%)**

- Position: X: 0.5". Y: 29.6"
- Width: 11.0". Height: 2.5"

Label (Barlow SemiBold, 16 pt, `#E8A020`):
> ASTM B633 — SERVICE CONDITIONS

Compact table (3 columns: SC | Environment | Min Thickness):

| Row | Fill | SC | Environment | Min Thickness |
|-----|------|----|-------------|---------------|
| 1 | base | SC1 | Indoor, dry | 5 um (0.2 mil) |
| 2 | alt | SC2 | Moderate | 8 um (0.3 mil) |
| 3 | base | SC3 | Severe, outdoor | 12 um (0.5 mil) |
| 4 | alt | SC4 | Very severe | 25 um (1.0 mil) |

Row height: 0.40". Font: Inter Regular, 13 pt. Thickness values in JetBrains Mono, 13 pt.

---

**BLOCK I — Common Problems (right 50%)**

- Position: X: 12.0". Y: 29.6"
- Width: 11.5". Height: 2.5"

Section label (Barlow SemiBold, 16 pt, `#E05C5C`):
> COMMON PROBLEMS — QUICK REFERENCE

Compact table (3 columns):

| Row | Fill | Problem | Acid Cause | Alkaline Cause |
|-----|------|---------|-----------|----------------|
| 1 | base | Burning | Low Zn; low boric acid | Low Zn; low NaOH:Zn |
| 2 | alt | Pitting | Low carrier; organics | Low carrier; H₂ adhesion |
| 3 | base | Roughness | pH >5.5; anode bags | High carbonate; filtration |
| 4 | alt | Dullness | High temp; low brightener | Brightener deficient |

Row height: 0.40". Font: Inter Regular, 12 pt, `#F0EDE8`. Left-border accents: `#E05C5C` Coral, 4 pt.

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 32.6"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster presents industry-typical operating parameters for acid chloride and alkaline non-cyanide zinc plating. Specific ranges vary by vendor formulation — always consult your product TDS. Analysis by titration is the authoritative method for confirming bath composition.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> Zinc Plating at a Glance: Acid Chloride vs. Alkaline Non-Cyanide

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.2"
> v1.0 — 2026

---

## Part 5 — Build Strategy for Elara

This poster's build time is dominated by the 16-row comparison table and the throwing power illustration. Elara should structure the build prompt as follows:

1. **Build the column header row** — get all 3 column widths, fills, and positions correct. This is the most important element because the Amber/Teal column fills establish the visual identity of the two systems.

2. **Build one data row** — all 3 cells, correct fonts, alternating fill. Group it.

3. **Duplicate the group 15 times** — reposition vertically, change text content, toggle base/alt fill.

4. **Throwing power illustration** — build one U-channel from 3 rectangles + deposit layers. Duplicate for the second channel. Adjust deposit thickness widths.

5. **CE graph** — axis lines first, then the two data lines. Labels last.

6. **Decision guide** — callout box with two text columns and center divider. Standard callout construction.

Estimated total build time: 60-75 minutes.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. Two overrides required.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills |
| `#252B3D` | `#E8E8F0` | Alternate table rows |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table rules, dividers, U-channel shapes |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

**Override 1:** Column header text on Amber and Teal fills — keep as `#F0EDE8` (Warm White) in Light edition. The darkened accent fills (`#C8860A` and `#1A8C82`) have insufficient contrast with `#1A1F2E` text.

**Override 2:** CE graph line colors — verify the darkened Teal (`#1A8C82`) and Amber (`#C8860A`) lines are clearly distinguishable against `#F5F4F0`. Both should be visible; if not, increase line stroke to 4 pt in Light edition.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #3 — Zinc Plating at a Glance — Construction Workup v1.0*
*2026-04-04*
