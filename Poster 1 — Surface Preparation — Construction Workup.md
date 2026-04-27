---
Project: Plating Posters Inc
Poster Number: 1
Title: "Surface Preparation: The Foundation of Every Flawless Finish"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 1 — Surface Preparation — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Surface Preparation — Alaina Research Brief v1 (2026-04-03)
Watson Flags: NONE — all data sourced directly from Research Brief v1
Process Scope: Surface preparation / pre-treatment (universal)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SurfacePreparation
  - ConstructionWorkup
---

# Poster # Poster #1 — Construction Workup
## Surface Preparation: The Foundation of Every Flawless Finish

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-03*

This document is the construction workup for Poster #1. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. All technical content is confirmed production-ready. All Watson flags are cleared.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 1 — Surface Preparation — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flowchart step blocks, callout boxes, accent borders, and table rows
- Circle shapes for step number badges
- Line elements with arrowheads for flowchart connectors
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for defect icons (Block F)
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Flowchart step blocks:** The generation tool does not have a dedicated flowchart tool with auto-connecting arrows. Each step block must be built as a manually grouped set of shapes (rounded rectangle + accent bar rectangle + number circle + text boxes). Arrows are separate line elements positioned between groups. This is tedious but straightforward — there are 7 steps to build.

2. **6 pt left accent bar on step blocks:** Same technique as Poster #4 and #10 table row left-borders — a narrow colored rectangle (approximately 0.08" wide) positioned flush against the left inside edge of each step block's rounded rectangle.

3. **Water break test illustration:** The "clean" panel water film can be simulated with a semi-transparent Teal rectangle overlay (25% opacity). The "contaminated" panel water beads are small Teal circles scattered on the part surface. Both are straightforward .

4. **Light edition production:** Same process as Posters #4 and #10 — duplicate the page, manually recolor per the remap table (Part 6). No Global Colors system .

5. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** If unavailable, substitute Courier Prime. This was flagged in Posters #4 and #10 — Drew should already have the font uploaded.

6. **Print size — 24x36":** Custom page size, same as all previous posters. For 18x24" version, duplicate and resize — verify 14 pt body text floor.

7. **Sub/superscript characters:** This poster uses: H₂, O₂, Al₂O₃, Cr₂O₃, NiCl₂, H₂SO₄, HCl, NaOH, KOH, Ca²⁺, Mg²⁺, Fe²⁺, Fe³⁺. Unicode characters are provided verbatim in the copy blocks — copy-paste them exactly.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org (if not already uploaded from Poster #4 or #10):
- **Barlow Condensed ExtraBold** — all headlines and section labels
- **Barlow SemiBold** — all subheadings, step names, callout titles
- **Inter Regular** and **Inter Medium** — all body text and table data
- **JetBrains Mono Regular** — all parameter data and version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )
Save all of the following as Brand Colors (if not already saved from previous posters):

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Acid step accent, subheadings, callout closings |
| Teal | `#2EC4B6` | Alkaline step accents, water film illustration, callout borders |
| Emerald | `#27AE60` | Plate step accent, "Clean" panel labels |
| Coral | `#E05C5C` | 80% stat, failure mode section, safety callout borders |
| Mid Slate | `#3A4055` | Rinse step accents, table headers, part shapes, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, parameter card fills |
| Alt Row | `#252B3D` | Alternating step block backgrounds |

### Step 5 — Set ruler guides
Pull guides from the design's ruler area to the following positions:

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 18.7" — Zone 2/Zone 3 boundary
- 23.7" — Zone 3/Zone 4 boundary
- 29.5" — Zone 4/Zone 5 boundary
- 32.7" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (top 0"-2.9")
  Block A: Headline + subheading + tagline (left ~60%)
  Block B: "The 80% Rule" callout box (right ~40%)

ZONE 2 — PROCESS FLOW DIAGRAM (2.9"-18.7" / ~15.8" tall)
  Block C: Vertical flowchart — 7 steps with parameter cards and connecting arrows

ZONE 3 — WATER BREAK TEST (18.7"-23.7" / ~5.0" tall)
  Block D: Two-panel illustration (Clean vs. Contaminated) + central callout banner

ZONE 4A — SUBSTRATE TABLE (23.7"-29.5" / ~5.8" tall, left 55%)
  Block E: 5-row substrate-specific sequence table

ZONE 4B — FAILURE MODES (23.7"-29.5", right 45%)
  Block F: 3x2 defect icon grid

ZONE 5 — STANDARDS + SAFETY (29.5"-32.7" / ~3.2" tall)
  Block G: Governing standards spec cards (left 55%)
  Block H: Chloride contamination safety callout (right 45%)

ZONE 6 — FOOTER BAND (32.7"-36.0" / ~3.3" tall)
  Block I: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Height: 2.9" from the top of the page (Y: 0" to 2.9").
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5" (left safe zone). Y: 0.5" (top safe zone)
- Width: 13.5" (approximately 58% of artboard width)
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> SURFACE PREPARATION

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#E8A020` (Amber)
- Text:

> The Foundation of Every Flawless Finish

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Skip the prep. Ruin the part.

---

**BLOCK B — "The 80% Rule" Callout Box**

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 14.5" (right-aligned, 0.5" from right trim). Y: 0.5" (top safe zone)
- Width: 9.0"
- Height: approximately 2.2"
- Fill color: `#1E2435` (Dark Callout)
- Border (stroke): 2 pt, color `#E05C5C` (Coral)
- Corner radius: 8 pt

**Large statistic:**
- Element type: Text box inside container
- Font: Barlow Condensed ExtraBold
- Size: 76 pt
- Color: `#E05C5C` (Coral)
- Alignment: Center
- Text:

> 80%+

**Statistic label:**
- Element type: Text box inside container, below the statistic
- Font: Inter Medium
- Size: 20 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> of plating defects originate in surface preparation — not the plating bath.

---

### ZONE 2 — Process Flow Diagram

**Dimensions:** Full page width. Y: 2.9" to 18.7" (15.8" tall).
**Background:** Same as page — no separate fill.

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 3.0" (just below Zone 1)
- Width: full content width (23.0")
- Font: Barlow Condensed ExtraBold
- Size: 34 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text (all caps):

> THE PRE-TREATMENT SEQUENCE

**Section sublabel:**
- Element type: Text box
- Position: X: 0.5". Y: below section label + 4 pt gap (approximately Y: 3.6")
- Width: 23.0"
- Font: Inter Regular
- Size: 18 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Alignment: Center
- Text:

> Every plating line. Every substrate. This sequence — or a variation of it — runs before every deposit.

---

**FLOWCHART STEP BLOCKS — Build Instructions**

Starting Y position: approximately 4.1" (below section sublabel + 0.3" gap)

Each step block is a group containing:
1. **Outer container:** Rounded rectangle, width 23.0" (full content width), corner radius 6 pt
2. **Left accent bar:** Rectangle, width 0.08", full height of container, positioned flush against left inside edge, no corner radius (or match outer container's left corners)
3. **Step number circle:** Circle, diameter 0.5" (36 pt), filled with accent color, positioned 0.3" from left edge, vertically centered
4. **Step name:** Text box, Barlow SemiBold 26 pt, accent color, positioned 1.0" from left edge
5. **Step role:** Text box, Inter Regular 18 pt, `#F0EDE8`, below step name with 4 pt gap
6. **Parameter card (process steps only):** Rounded rectangle, fill `#1E2435`, width 4.5", height 0.6", corner radius 4 pt, positioned right-aligned within container (0.3" from right inside edge). Text inside: JetBrains Mono Regular 16 pt, `#F0EDE8`, centered.
7. **Key insight (some steps):** Text box, Inter Medium 16 pt, accent color, below step role, with 2 pt left accent rule

**Arrow connectors:** After each step block, place a line element with a downward arrowhead. Line: `#3A4055` Mid Slate, 2 pt stroke, approximately 0.3" long, centered horizontally.

---

**STEP 1 — SOAK CLEAN**
- Container height: 2.0"
- Container fill: `#1A1F2E` (base row)
- Accent color: `#2EC4B6` Teal
- Number: **1**
- Step name text: `SOAK CLEAN`
- Role text: `Removes bulk oils, greases, cutting fluids, and shop dirt by chemical action.`
- Parameter card text: `140-180 deg F | 4-8 oz/gal | 3-10 min`
- Key insight: `The heavy lifter — if the soak cleaner fails, every step after it is compromised.`

**Arrow connector (0.3" gap)**

**STEP 2 — RINSE**
- Container height: 1.4"
- Container fill: `#252B3D` (alt row)
- Accent color: `#3A4055` Mid Slate
- Number: **2**
- Step name text: `RINSE`
- Role text: `Removes alkaline cleaner residue. Prevents cross-contamination into acid tanks.`
- Parameter card text: `Counterflow cascade | Min. 2 tanks | 70-120 deg F`
- No key insight

**Arrow connector**

**STEP 3 — ELECTROLYTIC CLEAN**
- Container height: 2.0"
- Container fill: `#1A1F2E` (base row)
- Accent color: `#2EC4B6` Teal
- Number: **3**
- Step name text: `ELECTROLYTIC CLEAN`
- Role text: `Alkaline chemistry + gas evolution scrubs final soil traces from the surface.`
- Parameter card text: `15-50 ASF | 30-120 sec | 140-180 deg F`
- Key insight: `Cathodic = 2x gas volume (maximum scrubbing). Anodic = surface activation. Always finish anodic.`

**Arrow connector**

**STEP 4 — RINSE**
- Container height: 1.4"
- Container fill: `#252B3D` (alt row)
- Accent color: `#3A4055` Mid Slate
- Number: **4**
- Step name text: `RINSE`
- Role text: `Removes alkaline electrocleaner before acid step. Prevents neutralization of the acid bath.`
- No parameter card
- No key insight

**Arrow connector**

**STEP 5 — ACID ACTIVATION**
- Container height: 2.0"
- Container fill: `#1A1F2E` (base row)
- Accent color: `#E8A020` Amber
- Number: **5**
- Step name text: `ACID ACTIVATION`
- Role text: `Brief acid immersion dissolves surface oxides and leaves bare, active metal ready for plating.`
- Parameter card text: `Room temp | 10-50% v/v | 15-60 sec`
- Key insight: `Seconds count. Too long = etching. Too short = oxide remains.`

**Arrow connector**

**STEP 6 — FINAL RINSE**
- Container height: 1.4"
- Container fill: `#252B3D` (alt row)
- Accent color: `#3A4055` Mid Slate
- Number: **6**
- Step name text: `FINAL RINSE`
- Role text: `Last rinse before plating. Must be extremely clean — acid drag-in alters bath pH and chemistry.`
- No parameter card
- No key insight

**Arrow connector**

**STEP 7 — PLATE**
- Container height: 1.6"
- Container fill: `#1A1F2E` (base row)
- Accent color: `#27AE60` Emerald
- Number: **7**
- Step name text: `PLATE`
- Role text: `Clean, active surface receives the plating deposit with full adhesion.`
- No parameter card
- Key insight: `A properly prepared surface is the foundation of every quality deposit.`

**Total flowchart height estimate:** Steps (2.0 + 1.4 + 2.0 + 1.4 + 2.0 + 1.4 + 1.6 = 11.8") + arrows (6 x 0.3" = 1.8") + section labels (~1.2") = approximately 14.8". This fits within the 15.8" zone allocation with 1.0" of breathing room.

---

### ZONE 3 — Water Break Test

**Dimensions:** Full page width. Y: 18.7" to 23.7" (5.0" tall).

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 18.8"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 30 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text (all caps):

> THE WATER BREAK TEST

---

**BLOCK D — Two-Panel Illustration**

**Overall illustration container:**
- Position: X: 0.5". Y: 19.4" (below section label)
- Width: 23.0". Height: approximately 3.8"

**Left Panel — "CLEAN"**
- Width: approximately 10.5" (45% of container)
- Panel title: Barlow Condensed ExtraBold, 22 pt, `#27AE60` Emerald, centered above panel

> CLEAN

- Part shape: Rounded rectangle, fill `#3A4055` Mid Slate, approximately 3.5" wide x 2.5" tall, centered in panel
- Water film overlay: Rectangle, fill `#2EC4B6` Teal at 25% transparency, same dimensions as part shape, layered directly on top
- Label below water film (Inter Regular, 16 pt, `#27AE60`):

> Water sheets uniformly

- Verdict label (Barlow SemiBold, 18 pt, `#27AE60`, centered below):

> PASS — proceed to plate

**Center divider:**
- Vertical line, `#3A4055` Mid Slate, 2 pt stroke
- Position: centered horizontally in the illustration container
- Height: 80% of container height, vertically centered

**Right Panel — "CONTAMINATED"**
- Width: approximately 10.5" (45% of container)
- Panel title: Barlow Condensed ExtraBold, 22 pt, `#E05C5C` Coral, centered above panel

> CONTAMINATED

- Part shape: Rounded rectangle, fill `#3A4055` Mid Slate, same dimensions as left panel
- Water beads: 8-12 small circles scattered across the part surface
  - Fill: `#2EC4B6` Teal at 60% transparency
  - Sizes: randomly vary between 12 pt and 24 pt diameter
  - Distribution: scattered unevenly — leave visible gaps of bare Mid Slate between beads
- Label below beads (Inter Regular, 16 pt, `#E05C5C`):

> Water beads up — oil or residue present

- Verdict label (Barlow SemiBold, 18 pt, `#E05C5C`, centered below):

> FAIL — return to cleaning

**Central callout banner:**
- Rounded rectangle, overlapping the center divider, centered vertically and horizontally within the illustration container
- Fill: `#1E2435` Dark Callout
- Border: `#E8A020` Amber, 1.5 pt
- Corner radius: 6 pt
- Width: approximately 10"
- Height: approximately 0.6"
- Text: Barlow Condensed ExtraBold, 24 pt, `#E8A020` Amber, centered:

> IF THE WATER BEADS, DON'T PLATE.

---

### ZONE 4A — Substrate-Specific Sequences (Left Column)

**Dimensions:** Left 55% of page (X: 0.5" to 13.2"). Y: 23.7" to 29.5" (5.8" tall).

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 23.8"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#E8A020` Amber
- Text:

> SUBSTRATE-SPECIFIC SEQUENCES

**Table header row:**
- Position: X: 0.5". Y: 24.4" (below section label)
- Width: 12.5" (left column width minus gutter)
- Height: 0.5"
- Fill: `#3A4055` Mid Slate
- Corner radius: 4 pt (top corners only)

Header text (Barlow SemiBold, 18 pt, `#E8A020`):
- Col 1 (2.5" wide): `SUBSTRATE`
- Col 2 (5.5" wide): `SEQUENCE VARIATION`
- Col 3 (4.5" wide): `KEY CONSIDERATION`

**Table data rows (5 rows):**

Each row: height approximately 0.85"
Row backgrounds: alternating `#1A1F2E` / `#252B3D`
Left accent bar: 0.06" wide rectangle, color per row specification
Row text: Inter Regular, 16 pt, `#F0EDE8`
Substrate name in Col 1: Inter Medium, 16 pt

| Row | Fill | Accent | Substrate | Sequence Variation | Key Consideration |
|-----|------|--------|-----------|-------------------|-------------------|
| 1 | `#1A1F2E` | Teal | Steel / Iron | Standard sequence | H₂ embrittlement risk above 39 HRC — minimize cathodic; bake within 4 hrs |
| 2 | `#252B3D` | Amber | Aluminum | Caustic etch + desmut | Al₂O₃ oxide requires alkaline removal; desmut removes smut |
| 3 | `#1A1F2E` | Amber | Zinc Die-Cast | Anodic EC only + mild H₂SO₄ + Cu strike | Porous — extended soak clean essential; cathodic EC deposits smuts |
| 4 | `#252B3D` | Coral | Stainless Steel | Standard + Wood's nickel strike | Passive Cr oxide requires Wood's (NiCl₂, pH <1.0, 50-250 ASF) |
| 5 | `#1A1F2E` | Teal | Copper / Brass | Standard + optional bright dip | Tarnishes rapidly — minimize acid-to-plate transfer time |

**Table footnote:**
- Position: below table, left-aligned
- Font: Inter Regular, 13 pt, `#F0EDE8` at 60% transparency
- Text:

> *All variations begin with soak clean and end with plate. Consult your process supplier for product-specific recommendations.*

---

### ZONE 4B — Failure Modes (Right Column)

**Dimensions:** Right 45% of page (X: 13.45" to 23.5"). Y: 23.7" to 29.5" (5.8" tall).

**Section label:**
- Position: X: 13.45". Y: 23.8"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#E05C5C` Coral
- Text:

> WHEN PREP FAILS

**Icon grid: 3 columns x 2 rows**

Grid position: X: 13.45". Y: 24.5" (below section label)
Cell size: approximately 3.2" wide x 2.3" tall
Grid gutter: 0.2" between cells

Each cell contains (top to bottom, vertically centered):
1. Icon: icon library, size 36 pt, color `#E05C5C` Coral
2. Defect name: Barlow SemiBold, 17 pt, `#F0EDE8`, centered
3. Root cause: Inter Regular, 14 pt, `#F0EDE8` at 75% transparency, centered

| Position | Icon Search Term | Defect Name | Root Cause |
|----------|-----------------|-------------|------------|
| Row 1, Col 1 | "layers" or "peel" | BLISTERING | Residual oil or oxide under deposit |
| Row 1, Col 2 | "circle dashed" | SKIP PLATING | Passive oxide not removed |
| Row 1, Col 3 | "dots" or "holes" | PITTING | H₂ trapped by organic contamination |
| Row 2, Col 1 | "broken" or "tear" | PEELING | Contamination between substrate and plate |
| Row 2, Col 2 | "texture" or "rough" | ROUGHNESS | Particulate from cleaning tanks |
| Row 2, Col 3 | "droplet" or "water" | STAINING | Alkaline or acid drag-out |

**Accessibility note:** Each cell has both an icon and text labels (defect name + root cause). The icons are reinforcement only — text carries the full information.

---

### ZONE 5 — Standards + Safety

**Dimensions:** Full page width. Y: 29.5" to 32.7" (3.2" tall).

**BLOCK G — Governing Standards (left 55%)**

Position: X: 0.5". Y: 29.6"
Width: 12.5"

Section label: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`, left-aligned:

> GOVERNING STANDARDS

**3 stacked spec cards:**

Each card: fill `#1E2435` Dark Callout; left border 4 pt `#2EC4B6` Teal; corner radius 4 pt; internal padding 10 pt; height approximately 0.65"; full column width; vertical gap between cards: 4 pt

| Card | Spec Code (JetBrains Mono ExtraBold, 18 pt, `#F0EDE8`) | Description (Inter Regular, 14 pt, `#F0EDE8` at 80% opacity) |
|------|-----------|-------------|
| 1 | ASTM B322 | Standard Guide for Cleaning Metals Prior to Electroplating |
| 2 | ASTM B850 | Post-Coating Hydrogen Embrittlement Relief |
| 3 | AMS 2759/9 | Hydrogen Embrittlement Relief for Steel Parts (Aerospace) |

---

**BLOCK H — Chloride Contamination Safety Callout (right 45%)**

Position: X: 13.45". Y: 29.6"
Width: 10.0"

Callout container:
- Rounded rectangle
- Fill: `#1E2435` Dark Callout
- Border: `#E05C5C` Coral, 2 pt
- Corner radius: 8 pt
- Internal padding: 16 pt
- Height: approximately 2.6" (fills the zone height)

Callout label (Barlow SemiBold, 18 pt, `#E05C5C`):

> WATCH YOUR ELECTROCLEANER

Callout body (Inter Regular, 16 pt, `#F0EDE8`):

> Chloride contamination above 10 g/L in the electrocleaner causes initial corrosion embedded in the substrate before plating. When plated over, this invisible damage leads to premature salt spray failure.

Callout closing (Inter Medium, 15 pt, `#E8A020`, with 2 pt Amber left accent rule):

> Titrate for chlorides periodically. Run a reverse-current Hull cell if etching is suspected.

---

### ZONE 6 — Footer Band

**Dimensions:** Full page width. Y: 32.7" to 36.0" (3.3" tall).

**Footer band background:**
- Rounded rectangle (bottom corners only, or full rectangle extending below trim)
- Fill: `#0D1020` Deep Navy
- Position: X: 0". Y: 32.7". Width: 24". Height: 3.3"

**Disclaimer (above main footer content):**
- Position: X: 0.5". Y: 33.0"
- Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency
- Alignment: Center
- Text:

> This poster is a technical reference tool. Always consult your process supplier's documentation, applicable safety data sheets, and product-specific TDS for operating parameters. Not a substitute for laboratory analysis or process qualification.

**Left — Poster title:**
- Position: X: 0.5". Y: 34.0"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> Surface Preparation: The Foundation of Every Flawless Finish

**Center — Series name:**
- Position: centered horizontally. Y: 34.0"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70% transparency
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Right — Logo placeholder:**
- Position: X: 22.6" (right-aligned). Y: 33.8"
- Rounded rectangle, fill `#3A4055`, width 0.8", height 0.4"
- Text inside: JetBrains Mono Regular, 12 pt, `#F0EDE8` at 50% transparency: `[LOGO]`

**Version:**
- Position: X: 22.6" (right-aligned). Y: 35.0"
- Font: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency
- Text:

> v1.0 — 2026

---

## Part 5 — Illustration Build Guide

### Water Break Test Panels (Block D)

**Clean panel — Part shape:**
1. Create a rounded rectangle: width 3.5", height 2.5", fill `#3A4055` Mid Slate, corner radius 6 pt
2. Create a second rectangle (same dimensions), fill `#2EC4B6` Teal, transparency 25%, layered directly on top of the part rectangle
3. Both rectangles should align exactly — the semi-transparent Teal overlay reads as a uniform water film

**Contaminated panel — Part shape + beads:**
1. Create a rounded rectangle: width 3.5", height 2.5", fill `#3A4055` Mid Slate, corner radius 6 pt (identical to Clean panel)
2. Create 8-12 circles scattered across the surface:
   - Each circle: fill `#2EC4B6` Teal, transparency 60%
   - Diameter: randomly vary between 0.15" and 0.30" per circle
   - Scatter randomly — do not align in a grid; leave visible Mid Slate gaps between beads
3. The bare Mid Slate visible between beads represents dry patches where water is not wetting the surface

### Flowchart Step Blocks

Each step block is a group of 5-7 elements. Build one complete step, group it, verify the layout, then duplicate-and-modify for the remaining 6 steps:

1. Start with Step 1 (Soak Clean) — build all elements
2. Group the entire step block (select all elements, Ctrl+G)
3. Duplicate the group (Ctrl+D), reposition Y to the next step position
4. Ungroup, change the text content, accent color, fill color per the step specifications
5. Re-group
6. Repeat for all 7 steps
7. Add arrow connectors between each group

This duplicate-and-modify approach saves significant time over building each step from scratch.

---

## Part 6 — Light Edition Remap Table

Duplicate the completed Dark edition page. Recolor every element per this table, working from top to bottom — background first, then text, then fills, then accents.

| Dark Hex | Light Hex | Elements Affected |
|----------|-----------|-------------------|
| `#1A1F2E` (BG) | `#F5F4F0` | Page background; base-row step blocks |
| `#F0EDE8` (text) | `#1A1F2E` | All primary text |
| `#1E2435` (callout) | `#ECEEF4` | Callout boxes, parameter cards |
| `#252B3D` (alt row) | `#E8E8F0` | Alternating step blocks and table rows |
| `#0D1020` (footer) | `#1A1F2E` | Footer band |
| `#E8A020` (Amber) | `#C8860A` | Acid step accent, subheadings, callout closings |
| `#2EC4B6` (Teal) | `#1A8C82` | Alkaline step accents, water film, callout borders |
| `#27AE60` (Emerald) | `#1E7A47` | Plate step accent, "Clean" panel labels |
| `#E05C5C` (Coral) | `#B83E3E` | 80% stat, failure modes, safety callout |
| `#3A4055` (Slate) | `#D0D4DE` | Rinse accents, table headers, part shapes, dividers |
| `#C8D0D8` (Silver) | `#C8D0D8` | **Unchanged** (not used on this poster, but standard) |

**No Light edition overrides required for this poster.** Standard remap table applies cleanly.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #1 — Surface Preparation — Construction Workup v1.0*
*2026-04-03*
