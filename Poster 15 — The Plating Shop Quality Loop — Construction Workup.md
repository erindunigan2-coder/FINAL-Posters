---
Project: Plating Posters Inc
Poster Number: 15
Title: "The Plating Shop Quality Loop: From Incoming Part to Final Inspection"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 15 — The Plating Shop Quality Loop — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Plating Shop Quality Loop Research Brief v1 (2026-04-04)
Watson Flags: THREE — ZendoLIMS reference, AS9100D prominence, Nadcap naming (all Drew, non-blocking)
Process Scope: Cross-process quality control — applicable to all plating operations
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - QualityControl
  - ConstructionWorkup
---

# Poster # Poster #15 — Construction Workup
## The Plating Shop Quality Loop

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #15. All technical content is confirmed production-ready.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 15 — The Plating Shop Quality Loop — Content and Layout Draft.md`

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color control
- Circles and rounded rectangles for the quality wheel structure
- Line and arrow elements for directional flow between stations
- standard icon library for station icons
- Small card/callout boxes for station detail cards
- Background page color set to exact hex
- Export at print-quality PDF

### Limitations to Flag for Elara

1. **Circular quality wheel:** The generation tool does not have true arc/pie-slice shapes. **Recommended approach:** Build the wheel as a large circle with 7 station groups arranged around its perimeter. Each station is a small icon + label group positioned at the correct clock position. Connect stations with line/arrow elements that follow the perimeter. The visual reads as a wheel even though it is built from discrete positioned elements.

2. **Curved arrows between stations:** the arrow tool draws straight lines. For the perimeter flow arrows, use short straight arrow segments angled to approximate the curve. Alternatively, use a curved line tool (available under Elements > Lines) — search for "curved arrow." If unavailable, straight arrows at appropriate angles are acceptable.

3. **Feedback arrow through center:** A single curved arrow from Station 7 to Station 1 passing through the center. Build as a curved line or as 2-3 connected straight segments forming a swooping path. Color it `#E05C5C` Coral to distinguish it from the clockwise flow arrows.

4. **PDCA quadrant shading:** Very subtle background tinting. In the design, place 4 large quarter-circle or rectangular shapes behind the wheel, each filled with the quadrant accent color at 5% transparency. If this level of subtlety is hard to achieve, increase to 8-10% or omit entirely — the PDCA text labels carry the concept without the shading.

5. **Station detail cards (Zone 3):** 8 small cards (7 stations + 1 feedback loop summary) in two rows of 4. These are standard callout box construction — rectangle + text. Build one card as a template, duplicate 7 times, modify content and accent color.

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
- 12.0" — center
- 23.5" — right safe zone

**Horizontal guides (from top edge):**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 18.7" — Zone 2/Zone 3 boundary
- 25.9" — Zone 3/Zone 4 boundary
- 30.6" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"-2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "Special Process" callout box (right ~45%)

ZONE 2 — QUALITY WHEEL (2.9"-18.7" / 15.8" tall)
  Block C: Seven-station circular quality wheel with icons, labels, consequence tags, feedback arrow, and PDCA quadrants

ZONE 3 — STATION DETAIL CARDS (18.7"-25.9" / 7.2" tall)
  Block D: Two rows of 4 cards — Stations 1-4 (top row), Stations 5-7 + Feedback Loop (bottom row)

ZONE 4 — H2 EMBRITTLEMENT + CALIBRATION (25.9"-30.6" / 4.7" tall)
  Block E: Hydrogen embrittlement warning panel (left 55%)
  Block F: Calibration checklist (right 45%)

ZONE 5 — SPECIFICATION STRIP (30.6"-32.4" / 1.8" tall)
  Block G: Governing standards horizontal strip

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
- Font: Barlow Condensed ExtraBold, 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text: `THE QUALITY LOOP`

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.5"
- Font: Barlow SemiBold, 36 pt
- Color: `#E8A020`
- Text: `From Incoming Part to Final Inspection`

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.2"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8`, transparency 65%
- Text: `Quality isn't the final step. It's every step.`

---

**BLOCK B — "Special Process" Callout**

- Position: X: 13.5". Y: 0.5"
- Width: 9.5". Height: ~2.2"
- Fill: `#1E2435`
- Border: `#E05C5C` Coral, 2 pt
- Corner radius: 8 pt

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> PLATING IS A SPECIAL PROCESS

Body (Inter Regular, 15 pt, `#F0EDE8`):
> You cannot look at a plated part and know if it will pass salt spray. You cannot see hydrogen trapped in steel. Quality must be built in during the process — it cannot be inspected in afterward.

Standard (JetBrains Mono Regular, 12 pt, `#F0EDE8` at 70%):
> ISO 9001:2015 Section 8.5.1

---

### ZONE 2 — Quality Wheel (HERO)

**Dimensions:** Full width. Y: 2.9" to 18.7" (15.8" tall).

**Section label:**
- Position: X: 0.5". Y: 3.0"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered
- Text: `THE SEVEN STATIONS OF PLATING QUALITY`

---

**WHEEL CONSTRUCTION**

The wheel occupies the center of this zone, approximately 14" diameter.

**Step 1 — Draw the outer wheel ring:**
- Large circle: 14" diameter, centered at X: 12.0", Y: 11.5" (center of zone)
- Fill: none (transparent)
- Border: `#3A4055` Mid Slate, 2 pt

**Step 2 — Draw the inner circle (center area):**
- Circle: 5.0" diameter, centered same as outer circle
- Fill: `#1A1F2E` (matches page background)
- Border: `#3A4055` Mid Slate, 3 pt

**Step 3 — Center text (inside inner circle):**

Line 1 (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):
> CERTIFIED.

Line 2 (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):
> EVERY TIME.

Line 3 (Inter Regular, 14 pt, `#F0EDE8` at 60%, centered):
> Plan - Do - Check - Act

**Step 4 — Place station groups around the perimeter:**

Each station group consists of:
- A small circle (1.3" diameter) with the station accent color fill, positioned on the outer ring
- A station icon inside the circle (icon, `#1A1F2E` dark, 0.7" x 0.7")
- Station number + name label, positioned just outside the circle (radiating outward)
- Consequence label, positioned further outside in `#E05C5C` Coral

**Station positions and content:**

**Station 1 — INCOMING INSPECTION (12 o'clock)**
- Circle position: X: 12.0", Y: 5.3" (top of wheel)
- Circle fill: `#2EC4B6` Teal
- Icon: magnifying glass (search "inspect" or "magnifying glass")
- Label (Barlow SemiBold, 14 pt, `#2EC4B6`): `1. INCOMING`
- Sub-label (Inter Regular, 11 pt, `#F0EDE8` at 80%): `Part inspection`
- Consequence (Inter Medium, 11 pt, `#E05C5C`): `Skip → wrong alloy contaminates bath`

**Station 2 — PRE-TREATMENT (~2 o'clock)**
- Circle position: X: 15.8", Y: 7.0"
- Circle fill: `#2EC4B6` Teal
- Icon: water droplet (search "water drop")
- Label: `2. PRE-TREAT`
- Sub-label: `Surface verification`
- Consequence: `Skip → adhesion failure`

**Station 3 — BATH CHEMISTRY (~4 o'clock)**
- Circle position: X: 16.8", Y: 11.0"
- Circle fill: `#E8A020` Amber
- Icon: flask / beaker (search "chemistry" or "flask")
- Label: `3. BATH CONTROL`
- Sub-label: `Chemistry analysis`
- Consequence: `Drift → invisible degradation`

**Station 4 — IN-PROCESS (~5:30)**
- Circle position: X: 15.2", Y: 14.8"
- Circle fill: `#E8A020` Amber
- Icon: gauge / meter (search "gauge")
- Label: `4. IN-PROCESS`
- Sub-label: `Parameter monitoring`
- Consequence: `Bad contacts → non-uniform deposit`

**Station 5 — POST-TREATMENT (~7 o'clock)**
- Circle position: X: 11.5", Y: 16.5"
- Circle fill: `#E8A020` Amber
- Icon: thermometer (search "temperature")
- Label: `5. POST-TREAT`
- Sub-label: `Passivation + bake`
- Consequence: `Missed bake → catastrophic H₂ failure`

**Station 6 — MEASUREMENT (~9 o'clock)**
- Circle position: X: 7.5", Y: 14.0"
- Circle fill: `#27AE60` Emerald
- Icon: ruler / measurement tool (search "measure" or "ruler")
- Label: `6. MEASUREMENT`
- Sub-label: `Thickness + properties`
- Consequence: `Under-thickness → field failure`

**Station 7 — FINAL INSPECTION (~11 o'clock)**
- Circle position: X: 7.8", Y: 7.5"
- Circle fill: `#27AE60` Emerald
- Icon: clipboard with checkmark (search "checklist" or "clipboard")
- Label: `7. FINAL`
- Sub-label: `Inspection + CoC`
- Consequence: `No traceability → audit failure`

**Step 5 — Directional flow arrows:**
- Between each station pair (1→2, 2→3, 3→4, 4→5, 5→6, 6→7): line with arrowhead, `#3A4055` Mid Slate, 2 pt, running along the wheel perimeter between the station circles.

**Step 6 — Feedback arrow (Coral):**
- Curved line (or 2-3 connected straight segments) from Station 7 position to Station 1 position, arcing through or near the center of the wheel
- Color: `#E05C5C` Coral, 3 pt stroke
- Arrowhead at Station 1 end
- Label along arrow path (Barlow SemiBold, 14 pt, `#E05C5C`): `CORRECTIVE ACTION`

**Step 7 — PDCA quadrant labels (optional shading):**

Four text labels positioned at the quadrant midpoints, outside the wheel ring:
- Top-right (Stations 1-2): `PLAN` — Barlow SemiBold, 16 pt, `#2EC4B6` at 40% transparency
- Right-bottom (Stations 3-5): `DO` — Barlow SemiBold, 16 pt, `#E8A020` at 40%
- Bottom-left (Stations 6-7): `CHECK` — Barlow SemiBold, 16 pt, `#27AE60` at 40%
- Top-left (Feedback): `ACT` — Barlow SemiBold, 16 pt, `#E05C5C` at 40%

If desired, add very subtle background rectangles (5-8% opacity of the accent color) behind each quadrant. This is optional — the labels alone communicate the PDCA mapping.

---

### ZONE 3 — Station Detail Cards

**Dimensions:** Full width. Y: 18.7" to 25.9" (7.2" tall).

---

**BLOCK D — Station Detail Cards**

**Layout:** Two rows of 4 cards. Each card approximately 5.5" wide x 3.3" tall.

Row 1 (Y: 18.8"): Stations 1, 2, 3, 4 — from left to right with 0.33" gaps
Row 2 (Y: 22.4"): Stations 5, 6, 7, Feedback Loop — same spacing

Card X positions: 0.5", 6.33", 12.17", 18.0"

**Card template:**
- Width: 5.5". Height: 3.3"
- Fill: `#1E2435` Dark Callout
- Left-border accent: 4 pt, station color
- Corner radius: 6 pt
- Internal padding: 12 pt

**Card content per station:**

**Card 1 — INCOMING INSPECTION** (left border: `#2EC4B6`)
Title (Barlow SemiBold, 14 pt, `#2EC4B6`):
> STATION 1: INCOMING

Checks (Inter Regular, 12 pt, `#F0EDE8`, bullet list):
> - Surface condition (rust, scale, oil)
> - Material identification (alloy, heat treat)
> - Dimensional / drawing review
> - Quantity + PO documentation

Gate (Inter Medium, 11 pt, `#27AE60`):
> GATE: Quarantine or return — no entry to plating line.

**Card 2 — PRE-TREATMENT** (left border: `#2EC4B6`)
Title: `STATION 2: PRE-TREATMENT`
Checks:
> - Cleaner concentration (titration)
> - Electrocleaner V/A and polarity
> - Acid activation strength
> - Rinse conductivity + flow rate

Gate:
> GATE: Water break test — continuous film, no beading.

**Card 3 — BATH CHEMISTRY** (left border: `#E8A020`)
Title: `STATION 3: BATH CONTROL`
Checks:
> - pH (2-point calibrated meter)
> - Metal concentration (EDTA titration)
> - Salt/buffer levels (titration)
> - Hull cell + temperature

Gate:
> GATE: Out-of-spec = correct before production.

**Card 4 — IN-PROCESS** (left border: `#E8A020`)
Title: `STATION 4: IN-PROCESS`
Checks:
> - Rectifier V/A correct for load
> - Current density within range
> - Temperature continuous monitoring
> - Agitation + rack/barrel condition

Gate:
> GATE: Any deviation = operator intervention or hold.

**Card 5 — POST-TREATMENT** (left border: `#E8A020`)
Title: `STATION 5: POST-TREATMENT`
Checks:
> - Passivation pH / temp / time
> - Sealer concentration + dip time
> - H₂ bake within 4 hrs (>40 HRC)
> - Drying (prevent white rust)

Gate:
> GATE: Bake oven calibrated with recording chart.

**Card 6 — MEASUREMENT** (left border: `#27AE60`)
Title: `STATION 6: MEASUREMENT`
Checks:
> - XRF thickness (ASTM B568)
> - Magnetic induction (B499)
> - Salt spray per spec (B117)
> - Adhesion testing (B571)

Gate:
> GATE: Fail = quarantine and disposition.

**Card 7 — FINAL INSPECTION** (left border: `#27AE60`)
Title: `STATION 7: FINAL + DOCUMENTATION`
Checks:
> - Visual inspection (100% or sampling)
> - All test results documented
> - Certificate of Conformance (CoC)
> - Full lot traceability

Gate:
> GATE: Release authority sign-off. No ship without CoC.

**Card 8 — FEEDBACK LOOP** (left border: `#E05C5C`)
Title (Barlow SemiBold, 14 pt, `#E05C5C`):
> FEEDBACK: CORRECTIVE ACTION

Content (Inter Regular, 12 pt, `#F0EDE8`):
> - Salt spray failures → trace to Stations 3 + 5
> - Adhesion failures → trace to Stations 1 + 2
> - Customer complaints → 8D / CAPA process
> - Internal audits → verify all stations

Gate (Inter Medium, 11 pt, `#27AE60`):
> GATE: Management review per ISO 9001 Sec. 9.3.

---

### ZONE 4 — H₂ Embrittlement + Calibration

**Dimensions:** Full width. Y: 25.9" to 30.6" (4.7" tall).

---

**BLOCK E — Hydrogen Embrittlement Warning (left 55%)**

- Position: X: 0.5". Y: 26.0"
- Width: 12.5". Height: 4.3"
- Fill: `#1E2435`
- Border: `#E05C5C` Coral, 2 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Warning icon: "alert triangle" or "warning" icon, `#E05C5C`, 1.0" x 1.0", top-left inside box.

Title (Barlow Condensed ExtraBold, 22 pt, `#E05C5C`, positioned right of icon):
> HYDROGEN EMBRITTLEMENT — THE CRITICAL WINDOW

Body (Inter Regular, 15 pt, `#F0EDE8`):
> High-strength steel parts (>40 HRC / >1000 MPa) must be baked within 4 hours of plating completion. Some specs require 1 hour. Delayed or omitted baking risks catastrophic brittle fracture.

Key data (JetBrains Mono Regular, 16 pt, `#F0EDE8`, tabular layout):
> Bake temp:  190 C (375 F)
> Duration:   4-24 hours (per spec)
> Deadline:   Within 4 hrs of plating
> Threshold:  >40 HRC or >1000 MPa

Standards (JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%):
> ASTM B850 | AMS 2759/9 | ASTM B633

---

**BLOCK F — Calibration Checklist (right 45%)**

- Position: X: 13.25". Y: 26.0"
- Width: 10.25". Height: 4.3"
- Fill: `#1E2435`
- Border: `#27AE60` Emerald, 1.5 pt
- Corner radius: 8 pt
- Internal padding: 16 pt

Title (Barlow SemiBold, 18 pt, `#27AE60`):
> IF IT MEASURES, IT MUST BE CALIBRATED

Checklist (Inter Regular, 14 pt, `#F0EDE8`):
> - pH meter (2-point cal before each use)
> - Thermometer / RTD probe
> - XRF thickness gauge
> - Microhardness tester
> - Bake oven temperature controller
> - Rectifier ammeter and voltmeter
> - Ampere-hour meter

Standard (JetBrains Mono, 12 pt, `#F0EDE8` at 60%):
> ISO 9001:2015 Section 7.1.5

---

### ZONE 5 — Specification Strip

**Dimensions:** Full width. Y: 30.6" to 32.4" (1.8" tall).

---

**BLOCK G — Standards Strip**

- Position: X: 0.5". Y: 30.7"
- Width: 23.0". Height: 1.5"
- Fill: `#1E2435`
- Corner radius: 6 pt

Title (Barlow SemiBold, 16 pt, `#F0EDE8`, left-aligned):
> GOVERNING STANDARDS

Standards (JetBrains Mono Regular, 13 pt, `#F0EDE8` at 80%, horizontal row):
> ASTM B633  |  B117  |  B571  |  B568  |  B487  |  B499  |  ISO 9001  |  AS9100D  |  Nadcap AC7108

Vertical dividers: `#3A4055` Mid Slate, 1 pt, between each standard.

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).
**Band fill:** `#0D1020` Deep Navy

**Disclaimer:**
- Position: X: 0.5". Y: 32.6"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% transparency, centered
- Text:

> This poster presents a generalized plating shop quality loop applicable to most electroplating operations. Specific quality requirements vary by customer specification, industry sector, and regulatory environment. Consult your quality management system documentation for site-specific procedures.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`, X: 0.5", Y: 34.0"
> The Plating Shop Quality Loop

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70% transparency, centered, Y: 34.0"
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** `[LOGO]` box at X: 22.6", Y: 33.8"

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% transparency, X: 22.6", Y: 35.2"
> v1.0 — 2026

---

## Part 5 — Build Strategy for Elara

This poster's build complexity is in the quality wheel illustration, not repetitive table construction. Elara should structure the build prompt as follows:

1. **Build the outer and inner circles first** — these define the wheel structure.

2. **Build one station group** — small accent circle + icon + label + sub-label + consequence tag. Get the sizing, fonts, and positioning right on Station 1.

3. **Duplicate the station group 6 times** — reposition to each clock position, change icon, change text, change accent color.

4. **Add flow arrows** — 6 arrows connecting consecutive stations clockwise.

5. **Add the feedback arrow** — the bold Coral curved arrow from Station 7 to Station 1 through the center.

6. **Add center text and PDCA labels.**

7. **Build one station detail card** — template with accent bar, title, bullet checks, gate text. Duplicate 7 times.

8. **H₂ warning and calibration boxes** — standard callout construction.

Estimated total build time: 75-90 minutes. The wheel illustration is the most time-consuming element but involves no precision tabular data — it is creative positioning work.

---

## Part 6 — Light Edition Remap Table

Standard remap table applies. No overrides required.

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, card fills, strip fill |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds (if any) |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Wheel borders, dividers, flow arrows |

**PDCA shading note:** The 5% opacity quadrant tints may be invisible on the Light background. Either increase to 10-12% opacity, or omit entirely in the Light edition. The PDCA text labels alone carry the concept.

**Station circle fills:** The accent-colored station circles remap to their darkened equivalents. The dark icon color inside (`#1A1F2E`) remaps to `#F5F4F0` (light icon on dark-ish circle). Verify icon contrast on each darkened accent fill — all should pass WCAG AA.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #15 — The Plating Shop Quality Loop — Construction Workup v1.0*
*2026-04-04*
