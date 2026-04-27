---
Project: Plating Posters Inc
Poster Number: 16
Title: "Rinsing Efficiency — The Hidden Cost of Poor Rinsing"
Document Type: Construction Workup
Status: v2.0 — Ready for Elara
Created: 2026-04-06T00:00:00
Updated: 2026-04-07T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 16)"
  - "Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 16, Filtration — for turnover-rate clarification only)"
Technical Source: Watson research brief (counterflow rinse equation, drag-out factors, conductivity monitoring); general industry knowledge (NASF/CEF curriculum)
Watson Flags: ONE OPEN — Confirm exact form of counterflow rinse equation (FR = DI x (CT/CR)^(1/N)) and define all variables. Non-blocking; equation is presented with full variable definitions.
Tyler Flags: ONE OPEN — Validate drag-out volume ranges (mL/ft²) and 15-20 second drain time rule against shop practice. Non-blocking; qualified ranges used.
v2 Changelog:
  - Corrected misplaced filtration metric in Block F (the "4–5 tank turnovers/hour for 97% particulate removal" line belongs to filtration, not rinsing — replaced with a rinse-relevant target).
  - Added explicit drip-tray slope direction language to Best Practices bullet (Watson brief callout).
  - Added a small drag-out recovery tank ("DRT") visual cue ahead of Tank 1 in the counterflow diagram, with a one-line label explaining its role (Watson brief callout).
  - Tightened Block G conductivity setpoint range with a clearer "process-dependent" qualifier.
Process Scope: Rinsing and drag-out management (universal — applies to every plating line)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Rinsing
  - DragOut
  - WaterConservation
  - ConstructionWorkup
---

# Poster # Poster #16 — Construction Workup
## Rinsing Efficiency — The Hidden Cost of Poor Rinsing

*Alaina — Plating Posters Inc Creative Lead*
*v2.0 — 2026-04-07 (v1.0 issued 2026-04-06)*

This document is the construction workup for Poster #16. It translates Watson's research brief concept into a full design specification usable by Elara to engineer a generation prompt for Drew. One Watson flag and one Tyler flag remain open — both are non-blocking. The poster uses qualified ranges and clearly defined variables.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**v2 refresh notes:** Corrected a misplaced filtration metric in Block F, added the drag-out recovery tank visual cue Watson called out, added the drip-tray slope direction language to the Best Practices bullets, and tightened the conductivity setpoint qualifier. No layout zones, dimensions, or color palette have changed — Elara can use this as a drop-in replacement for v1.0.

**Content source:** Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 16), supplemented by general industry knowledge on rinse system design.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for tank diagrams, callout boxes, accent borders, and table rows
- Line elements with arrowheads for flow direction indicators (water flow, part movement)
- Circle shapes for step number badges in the counterflow diagram
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for water droplet, factory, conductivity meter icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Counterflow rinse tank diagram (Block B — HERO):** The three-tank diagram must be built from geometric shapes — rectangles for tanks, arrows for water flow and part movement, gradient-like effect achieved by using three progressively lighter shades of Teal for the water fill in each tank. This is the poster's centerpiece and needs to be visually clear. Straightforward in the design but will require careful positioning.

2. **Water savings comparison (Block C):** Two side-by-side bar-style comparisons (single rinse vs. counterflow). Build as rectangles with proportional heights. Label with exact percentages. Simple and effective .

3. **4 pt left-border accents on callout boxes:** Same technique as all previous posters — narrow colored rectangle (approximately 0.06" wide) positioned flush against the left edge of each callout box.

4. **Conductivity meter icon:** Search the icon library for "meter" or "gauge." If nothing suitable, build as a simple circle with a needle line and scale arc — geometric shapes can handle this.

5. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Producing the Light edition requires duplicating the design page and manually recoloring every element per the remap table in Part 6.

6. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** If unavailable, substitute **Courier Prime**. Drew should already have the font uploaded from prior posters.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation. For 18x24", duplicate and resize; verify all text meets the 14 pt minimum floor.

8. **Sub/superscript characters:** This poster uses minimal chemical notation. Unicode characters are provided verbatim in copy blocks — copy-paste exactly.

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
- **Inter Regular** and **Inter Medium** — all body text and table data
- **JetBrains Mono Regular** — all parameter data, equation variables, and version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Single-rinse accent, warning callouts, drag-out factors |
| Teal | `#2EC4B6` | Counterflow accent, clean-water indicators, equation highlight |
| Emerald | `#27AE60` | Water savings percentages, positive outcomes |
| Coral | `#E05C5C` | Poor rinsing consequences, cost warnings |
| Mid Slate | `#3A4055` | Tank outlines, table headers, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, equation display background |
| Alt Row | `#252B3D` | Alternating table rows, secondary tank fills |
| Bright Silver | `#C8D0D8` | Part shapes in tank diagrams |
| Teal Light | `#5ED4C8` | Middle rinse tank water fill (lighter shade) |
| Teal Lightest | `#A0E8E0` | Cleanest rinse tank water fill (lightest shade) |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 14.5" — Zone 2/Zone 3 boundary
- 21.5" — Zone 3/Zone 4 boundary
- 28.5" — Zone 4/Zone 5 boundary
- 32.5" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — COUNTERFLOW RINSE DIAGRAM (2.9"–14.5" / ~11.6" tall)
  Block B: Three-tank counterflow diagram (HERO illustration)
  Flow arrows, part movement direction, water flow direction
  Tank labels and numbered badges

ZONE 3 — WATER SAVINGS COMPARISON + EQUATION (14.5"–21.5" / ~7.0" tall)
  Block C: Side-by-side single-rinse vs. counterflow comparison bars
  Block D: Counterflow rinse equation display with variable definitions

ZONE 4 — DRAG-OUT FACTORS + BEST PRACTICES (21.5"–28.5" / ~7.0" tall)
  Block E: Drag-out factors callout (left column)
  Block F: Best practices callout (right column)

ZONE 5 — CONDUCTIVITY MONITORING CALLOUT (28.5"–32.5" / ~4.0" tall)
  Block G: Full-width callout — conductivity monitoring for rinse quality

ZONE 6 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block H: Disclaimer + poster title + series name + logo placeholder + version
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

> RINSING EFFICIENCY

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#2EC4B6` (Teal)
- Text:

> The Hidden Cost of Poor Rinsing

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Every plating line uses water. Most use far more than necessary.

---

### ZONE 2 — Counterflow Rinse Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 14.5" (~11.6" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold
- Size: 30 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> HOW COUNTERFLOW RINSING WORKS

---

**BLOCK B — Three-Tank Counterflow Diagram**

Y: 3.8" to 13.5" (~9.7" available).

This is the poster's hero illustration. It shows three rinse tanks in a row with parts moving left-to-right (dirtiest to cleanest) and fresh water flowing right-to-left (cleanest tank receives fresh water, overflows to the next dirtiest).

**Overall layout:** Three tanks evenly spaced across the safe zone width.
- Tank 1 (Dirtiest): X: 0.5" to 7.0" (6.5" wide)
- Tank 2 (Middle): X: 8.5" to 15.0" (6.5" wide)
- Tank 3 (Cleanest): X: 16.5" to 23.0" (6.5" wide)
- Gaps between tanks: 1.5"

**Each tank is built as:**

1. **Tank body (outer):**
   - Element type: Rectangle
   - Width: 6.5". Height: 5.5"
   - Fill: none (transparent)
   - Border: 3 pt, `#3A4055` (Mid Slate)
   - Y: 5.0" to 10.5"

2. **Water fill (inside tank):**
   - Element type: Rectangle (positioned inside the tank body, flush with inner edges)
   - Width: 6.2". Height: 4.0" (water does not fill the entire tank — leave headspace)
   - Y: 6.3" to 10.3"
   - Fill varies by tank:
     - Tank 1 (Dirtiest): `#2EC4B6` at 60% opacity (dark teal, murky)
     - Tank 2 (Middle): `#5ED4C8` at 50% opacity (medium teal)
     - Tank 3 (Cleanest): `#A0E8E0` at 40% opacity (light teal, clear)

3. **Parts in tank:**
   - 2-3 small rounded rectangles per tank (W: 0.5", H: 0.8")
   - Fill: `#C8D0D8` (Bright Silver)
   - Position: Submerged in the water fill area, lower third of each tank

4. **Tank label (below tank):**
   - Element type: Text box
   - Font: Barlow SemiBold, 20 pt
   - Position: Centered below each tank. Y: 11.0"
   - Color varies:
     - Tank 1: `#E05C5C` (Coral) — text: `RINSE 1 — Dirtiest`
     - Tank 2: `#E8A020` (Amber) — text: `RINSE 2 — Middle`
     - Tank 3: `#27AE60` (Emerald) — text: `RINSE 3 — Cleanest`

5. **Number badge (inside tank, upper-left):**
   - Element type: Circle
   - Diameter: 0.5"
   - Fill: `#3A4055` (Mid Slate)
   - Position: X: 0.3" from tank left edge, Y: 0.3" from tank top edge (inside)
   - Text inside: `1`, `2`, `3` — Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`

**Part movement arrows (left-to-right across top):**
- Element type: Line with arrowhead
- Y: 4.5" (above tanks)
- Three arrow segments: Tank 1 right edge to Tank 2 left edge, Tank 2 to Tank 3
- Each arrow spans the 1.5" gap between tanks
- Stroke: 2.5 pt, `#C8D0D8` (Bright Silver)
- Arrowhead: pointing right
- Label above the arrow line:
  - Text box, Barlow SemiBold, 18 pt, `#C8D0D8`
  - Position: Centered above the arrows. Y: 3.9"
  - Text: `PARTS MOVE →  (dirtiest to cleanest)`

**Water flow arrows (right-to-left across bottom, below tanks):**
- Element type: Line with arrowhead
- Y: 12.0" (below tank labels)
- Three arrow segments: Tank 3 left edge to Tank 2 right edge, Tank 2 to Tank 1
- Direction is reversed — arrowheads point LEFT
- Stroke: 2.5 pt, `#2EC4B6` (Teal)
- Arrowhead: pointing left
- Label below the arrow line:
  - Text box, Barlow SemiBold, 18 pt, `#2EC4B6`
  - Position: Centered below the arrows. Y: 12.6"
  - Text: `← FRESH WATER FLOWS  (cleanest to dirtiest)`

**Fresh water inlet indicator (at Tank 3):**
- Element type: Short line with arrowhead entering Tank 3 from the right
- Position: X: 23.5" to 23.0", Y: 8.0" (pointing into tank from outside)
- Stroke: 2 pt, `#27AE60` (Emerald)
- Label: `Fresh DI water in` — JetBrains Mono Regular, 12 pt, `#27AE60`, positioned to the right of the tank

**Drain/overflow indicator (at Tank 1):**
- Element type: Short line with arrowhead exiting Tank 1 from the left
- Position: X: 0.5" to 0.0", Y: 8.0" (pointing out from tank)
- Stroke: 2 pt, `#E05C5C` (Coral)
- Label: `To waste treatment` — JetBrains Mono Regular, 12 pt, `#E05C5C`, positioned to the left

**Drain time callout (between part arrows and tanks):**
- Element type: Text box
- Position: Centered horizontally. Y: 13.2"
- Font: Inter Medium, 16 pt, `#E8A020` (Amber)
- Text:

> 15–20 second drain time between stations — tilt parts to minimize drag-out

**Drag-out recovery tank (DRT) visual cue (v2 addition):**

A small "DRT" tank is added to the LEFT of Tank 1 to show the drag-out recovery tank position in a properly designed line.

- Element type: Rectangle (small tank body)
  - Width: 1.4". Height: 2.0"
  - Position: X: -1.0" to 0.4" (extends slightly past safe zone — acceptable as a graphic element; ensure no text falls outside the bleed)
  - Y: 6.5" to 8.5"
  - Fill: none. Border: 2 pt dashed, `#E8A020` (Amber)
- Inner water fill: Rectangle, W: 1.3", H: 1.4", fill `#E8A020` at 25% opacity
- Label below tank: `DRT` — Barlow SemiBold, 14 pt, `#E8A020`. Centered below tank.
- Caption (small, set above the part-movement arrow line): `Drag-out recovery → returns to process tank` — Inter Regular, 11 pt, `#E8A020`. Position: X: -1.0", Y: 4.1", width 4.5".
- Small dashed return-arrow from DRT top-left back toward the process tank (off-page direction): 1 pt dashed, `#E8A020`, arrowhead pointing left.

*Elara note:* If the DRT cluster crowds the page edge, drop the dashed return-arrow and keep only the tank, label, and caption — the visual hierarchy still reads.

---

### ZONE 3 — Water Savings + Equation

**Dimensions:** Full page width within margins. Y: 14.5" to 21.5" (~7.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 14.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE MATH BEHIND THE SAVINGS

---

**BLOCK C — Water Savings Comparison** (left half, X: 0.5" to 11.5")

Y: 15.4" to 18.8" (~3.4" tall)

Two side-by-side vertical bars comparing water use:

**Bar 1 — Single Rinse:**
- Element type: Rectangle
- Position: X: 2.0". Y: 15.8"
- Width: 2.5". Height: 3.0" (full height = 100%)
- Fill: `#E05C5C` (Coral) at 80% opacity
- Label above: `Single Rinse` — Barlow SemiBold, 18 pt, `#E05C5C`. Y: 15.4"
- Label inside (centered): `100%` — Barlow Condensed ExtraBold, 36 pt, `#F0EDE8`
- Sub-label below: `Rinse ratio 100:1` — JetBrains Mono Regular, 14 pt, `#F0EDE8` at 60%

**Bar 2 — 2-Stage Counterflow:**
- Element type: Rectangle
- Position: X: 6.0". Y: 18.5"
- Width: 2.5". Height: 0.3" (10% of Bar 1 height — showing 90% reduction)
- Fill: `#27AE60` (Emerald)
- Label above: `2-Stage Counterflow` — Barlow SemiBold, 18 pt, `#27AE60`. Positioned above bar
- Label inside or beside (bar is very short): `10%` — Barlow Condensed ExtraBold, 28 pt, `#27AE60`, positioned beside the bar
- Sub-label below: `Same rinse ratio` — JetBrains Mono Regular, 14 pt, `#F0EDE8` at 60%

**Savings callout between bars:**
- Element type: Text box
- Position: Centered between the two bars. Y: 17.0"
- Font: Barlow Condensed ExtraBold, 48 pt, `#27AE60`
- Text:

> 90% LESS WATER

---

**BLOCK D — Counterflow Rinse Equation** (right half, X: 12.0" to 23.5")

Y: 15.4" to 20.8"

**Equation display box:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 15.4"
- Width: 11.5". Height: 5.4"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 12.0". Y: 15.4"
- Width: 0.06". Height: 5.4"
- Fill: `#2EC4B6` (Teal)

**Equation title:**
- Element type: Text box
- Position: X: 12.4". Y: 15.7"
- Font: Barlow SemiBold, 20 pt, `#2EC4B6`
- Text:

> COUNTERFLOW RINSE EQUATION

**Equation (large display):**
- Element type: Text box
- Position: X: 12.4". Y: 16.5"
- Width: 10.8"
- Font: JetBrains Mono Regular, 28 pt, `#F0EDE8`
- Alignment: Center
- Text:

> FR = DI x (CT / CR)^(1/N)

**Variable definitions (below equation):**
- Element type: Text box
- Position: X: 12.4". Y: 17.6"
- Width: 10.8"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 160%
- Text:

> FR = Flow rate of fresh water (gal/hr)
> DI = Drag-in volume per rack (gal/rack)
> CT = Concentration in process tank
> CR = Maximum allowable rinse concentration
> N = Number of counterflow rinse stages
>
> CT/CR = Rinse ratio (typically 1,000:1 to 10,000:1)

**Key insight callout:**
- Element type: Text box
- Position: X: 12.4". Y: 20.0"
- Width: 10.8"
- Font: Inter Medium, 15 pt, `#E8A020` (Amber)
- Text:

> Adding one rinse stage takes the Nth root of the rinse ratio — this is why 2 stages beats 1 by a factor of 10-100x in water savings.

---

### ZONE 4 — Drag-Out Factors + Best Practices

**Dimensions:** Full page width within margins. Y: 21.5" to 28.5" (~7.0" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 21.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> CONTROLLING DRAG-OUT

---

**BLOCK E — Drag-Out Factors** (left column)

Y: 22.4" to 28.0"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 22.4"
- Width: 11.2". Height: 5.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 22.4"
- Width: 0.06". Height: 5.5"
- Fill: `#E8A020` (Amber)

Callout title:
- Element type: Text box
- Position: X: 0.8". Y: 22.6"
- Font: Barlow SemiBold, 22 pt, `#E8A020`
- Text:

> WHAT INCREASES DRAG-OUT

Bullet list:
- Element type: Text box
- Position: X: 0.8". Y: 23.2"
- Width: 10.6"
- Font: Inter Regular, 18 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Higher solution viscosity (hot alkaline cleaners, thick acids)
> - Complex part geometry (cups, recesses, blind holes)
> - Rough or porous surfaces (cast parts, etched surfaces)
> - Fast withdrawal speed (less time for solution to sheet off)
> - High surface tension (no wetting agents in the bath)
> - Large surface-to-volume ratio (flat parts carry more film)

**Key number callout:**
- Element type: Text box
- Position: X: 0.8". Y: 26.8"
- Width: 10.6"
- Font: JetBrains Mono Regular, 14 pt, `#E8A020`
- Text:

> Typical drag-out: 2–6 mL/ft² of part surface area

---

**BLOCK F — Best Practices** (right column)

Y: 22.4" to 28.0"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 22.4"
- Width: 11.5". Height: 5.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 12.0". Y: 22.4"
- Width: 0.06". Height: 5.5"
- Fill: `#27AE60` (Emerald)

Callout title:
- Element type: Text box
- Position: X: 12.3". Y: 22.6"
- Font: Barlow SemiBold, 22 pt, `#27AE60`
- Text:

> DRAG-OUT REDUCTION BEST PRACTICES

Bullet list:
- Element type: Text box
- Position: X: 12.3". Y: 23.2"
- Width: 10.9"
- Font: Inter Regular, 18 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Drain 15–20 seconds over the process tank before moving
> - Tilt parts and racks to break surface tension
> - Use air knives or blow-offs for high-value baths
> - Install drip trays sloped BACK toward the process tank (never toward the rinse)
> - Add wetting agents to reduce solution surface tension
> - Use a drag-out recovery tank ahead of the first rinse to capture drag-out for return to the process tank
> - Orient parts to minimize cupping and pooling

**Key number callout:**
- Element type: Text box
- Position: X: 12.3". Y: 26.8"
- Width: 10.9"
- Font: JetBrains Mono Regular, 14 pt, `#27AE60`
- Text:

> Target rinse ratio: 1,000:1 minimum for decorative work; 10,000:1+ for electronics and aerospace

---

### ZONE 5 — Conductivity Monitoring Callout

**Dimensions:** Full page width within margins. Y: 28.5" to 32.5" (~4.0" tall).

---

**BLOCK G — Full-Width Callout**

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 28.7"
- Width: 23.0". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 28.7"
- Width: 0.06". Height: 3.5"
- Fill: `#2EC4B6` (Teal)

Callout title:
- Element type: Text box
- Position: X: 0.8". Y: 28.9"
- Font: Barlow SemiBold, 22 pt, `#2EC4B6`
- Text:

> MONITORING RINSE QUALITY — CONDUCTIVITY

Body text (left half, X: 0.8" to 11.5"):
- Element type: Text box
- Position: X: 0.8". Y: 29.5"
- Width: 10.5"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text:

> Conductivity measurement is the simplest way to verify rinse water quality. As drag-out contaminates the rinse, dissolved salts raise the conductivity. A rising reading means the rinse is becoming less effective.

Body text (right half, X: 12.5" to 23.5"):
- Element type: Text box
- Position: X: 12.5". Y: 29.5"
- Width: 10.5"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text:

> Inductive (toroidal) conductivity sensors are preferred over electrode-type sensors in plating environments — they resist fouling from dissolved metals and organics that coat electrode surfaces and cause drift.

**Key data callout (bottom of box):**
- Element type: Text box
- Position: Centered horizontally. Y: 31.4"
- Font: JetBrains Mono Regular, 14 pt, `#E8A020` (Amber)
- Alignment: Center
- Text:

> DI water baseline: < 5 µS/cm  |  Typical rinse alarm setpoint: 50–200 µS/cm — always set process-by-process against your spec, not by rule of thumb

---

### ZONE 6 — Footer Band

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

> This poster is an educational reference tool. Rinse system design depends on specific process chemistry, water quality, local discharge limits, and equipment configuration. Consult your process supplier and environmental engineer for application-specific guidance.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Rinsing Efficiency — The Hidden Cost of Poor Rinsing

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
| Zone 2 - Counterflow Diagram | Section label, three tanks, parts, water fills, flow arrows, labels, drain time callout |
| Zone 3 - Water Savings and Equation | Section label, comparison bars, savings callout, equation box |
| Zone 4 - Drag-Out Control | Section label, drag-out factors callout, best practices callout |
| Zone 5 - Conductivity Monitoring | Full-width callout with body text and data |
| Zone 6 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

After grouping, lock each completed zone (right-click > Lock) before proceeding to the next.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, equation display background |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Tank outlines, table rules, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |
| `#5ED4C8` | `#3AAFA3` | Middle tank water fill (darken for light BG) |
| `#A0E8E0` | `#6DC8BE` | Cleanest tank water fill (darken for light BG) |

Water fill opacities may need adjustment in the Light edition to maintain visual distinction against the light background. Test at 50-70% opacity.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Rinsing Efficiency — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rinsing Efficiency — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rinsing Efficiency — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Rinsing Efficiency — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rinsing Efficiency — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Rinsing Efficiency — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #16 — Rinsing Efficiency — Construction Workup v2.0*
*2026-04-07 (v1.0 issued 2026-04-06)*
