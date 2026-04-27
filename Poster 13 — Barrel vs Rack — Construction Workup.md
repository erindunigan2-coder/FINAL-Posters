---
Project: Plating Posters Inc
Poster Number: 13
Title: "Barrel vs. Rack Plating — Choosing the Right Method"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 13 — Barrel vs Rack — Content and Layout Draft.md (v1.0)"
Technical Source: Drew's Quick Reference Notes; Watson's Current Density Research Brief v1; general industry knowledge
Watson Flags: ONE OPEN — barrel weight/size limits (non-blocking; qualified range used)
Process Scope: Comparison poster — barrel vs. rack plating methods
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - BarrelPlating
  - RackPlating
  - ConstructionWorkup
---

# Poster # Poster #13 — Construction Workup
## Barrel vs. Rack Plating — Choosing the Right Method

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #13. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. One Watson flag remains open (barrel weight/size limits) but is non-blocking — the poster uses qualified ranges.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 13 — Barrel vs Rack — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for table rows, callout boxes, accent borders, and decision boxes
- Line elements with arrowheads for the decision flowchart connectors
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for barrel/rack visual elements
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Barrel cross-section illustration:** Complex freeform vector illustration requires geometric shape composites. The barrel must be built as a composite of geometric shapes — a large rounded rectangle for the barrel body, small circles for perforations, small rounded rectangles for tumbling parts, a curved line with arrowhead for rotation, and small circles for cathode buttons. **Recommendation: build as layered geometric shapes.** This approach was validated on Posters #4 and #10.

2. **Rack illustration:** Build as rectangles for the spine and crossbars, small rectangles with hook connectors (short lines) for hanging parts, and rectangles with amber outlines for anodes. Straightforward .

3. **Decision flowchart strip (Block E):** Four rounded-rectangle boxes connected by right-pointing arrows. This is straightforward with line elements and arrowheads. Position the boxes evenly across the full width with consistent gaps.

4. **4 pt left-border accents on callout boxes:** Same technique as Posters #4 and #10 — simulate with a narrow colored rectangle (approximately 0.06" wide) positioned flush against the left edge of each callout box.

5. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Producing the Light edition requires duplicating the design page and manually recoloring every element per the remap table in Part 6.

6. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** If unavailable, substitute **Courier Prime**. Flag substitution visibly.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation. For 18x24", duplicate and resize; verify all text meets the 14 pt minimum floor.

8. **Center divider between barrel and rack panels:** A simple 2 pt vertical line in Mid Slate. This is straightforward.

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
- **JetBrains Mono Regular** — all parameter/data table values and sub-labels

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Rack accent, section titles |
| Teal | `#2EC4B6` | Barrel accent, callout borders/titles |
| Emerald | `#27AE60` | Not primary on this poster (reserve) |
| Coral | `#E05C5C` | Not primary on this poster (reserve) |
| Mid Slate | `#3A4055` | Table header fills, row rules, dividers, illustration outlines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, decision strip background |
| Alt Row | `#252B3D` | Alternating table row backgrounds, decision boxes |
| Bright Silver | `#C8D0D8` | Parts in illustrations |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 12.0" — center divider (Zone 2 barrel/rack split)
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 11.5" — Zone 2/Zone 3 boundary
- 25.2" — Zone 3/Zone 4 boundary
- 32.4" — Zone 4/Zone 5 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — SIDE-BY-SIDE ILLUSTRATION (2.9"–11.5" / ~8.6" tall)
  Block B-LEFT: Barrel cross-section (left 50%)
  Block B-RIGHT: Rack illustration (right 50%)
  Section label + center divider

ZONE 3 — HEAD-TO-HEAD COMPARISON TABLE (11.5"–25.2" / ~13.7" tall)
  Block C: Full-width 10-row comparison matrix (HERO data block)
  Section label + table footnote

ZONE 4 — DECISION GUIDE (25.2"–32.4" / ~7.2" tall)
  Block D: "When to Choose" two-column callout (upper portion)
  Block E: Decision flowchart strip (lower portion)
  Section label

ZONE 5 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
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

> BARREL vs. RACK

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#E8A020` (Amber)
- Text:

> Choosing the Right Plating Method

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Not every part belongs in a barrel.

---

### ZONE 2 — Side-by-Side Illustration

**Dimensions:** Full page width within margins. Y: 2.9" to 11.5" (~8.6" tall).

---

**Section label (above illustration):**
- Element type: Text box
- Position: Centered horizontally on artboard. Y: 3.1" (0.2" below Zone 1 boundary)
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 30 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> HOW EACH METHOD WORKS

---

**Illustration area:** Y: 3.6" to 11.0" (~7.4" available). Divided into two equal panels.

**Left panel — Barrel Plating:** X: 0.5" to 11.5" (11.0" wide)
**Center divider:** X: 12.0"
**Right panel — Rack Plating:** X: 12.5" to 23.5" (11.0" wide)

---

**Left panel title:**
- Element type: Text box
- Position: Centered within left panel (X center: ~6.0"). Y: 3.6"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#2EC4B6` (Teal)
- Alignment: Center
- Text:

> BARREL PLATING

**Left panel — Barrel cross-section illustration:**

Build the barrel as a composite of geometric shapes:

1. **Barrel body (outer):**
   - Element type: Rounded rectangle
   - Position: X: 2.5". Y: 4.5"
   - Width: 7.0". Height: 4.0"
   - Fill: none (transparent)
   - Border (stroke): 3 pt, `#3A4055` (Mid Slate)
   - Corner radius: 20 pt (gives the barrel a slightly rounded look)

2. **Perforations (suggested by circles):**
   - 8-10 small circles, diameter 0.15", arranged in two rows across the barrel body
   - Fill: `#1A1F2E` (same as background — creates "hole" effect)
   - Border: 1 pt, `#3A4055`
   - Position: Evenly spaced across the barrel body at Y: 5.0" and Y: 7.5" (top and bottom row)

3. **Tumbling parts (inside barrel):**
   - 6-8 small rounded rectangles in varying sizes (W: 0.4-0.8", H: 0.3-0.5")
   - Fill: `#C8D0D8` (Bright Silver)
   - Position: Clustered in the bottom third of the barrel (Y: 7.0" to 8.0"), slightly rotated at various angles to suggest tumbling
   - No border

4. **Rotation arrow:**
   - Element type: Curved line with arrowhead (Elements > Lines & Shapes > curved arrow)
   - Position: Outside the barrel body, right side, X: 9.8", Y: 5.5" to 7.5"
   - Stroke: 2 pt, `#2EC4B6` (Teal)
   - Arrowhead: at the bottom end, pointing clockwise

5. **Cathode buttons:**
   - 3 small circles, diameter 0.2"
   - Fill: `#2EC4B6` (Teal)
   - Position: Along the interior bottom curve of the barrel (X: 4.0", 5.5", 7.0"; Y: 8.0")

6. **Solution flow arrows:**
   - 3-4 short wavy or straight lines passing through the barrel perforations
   - Stroke: 1 pt, `#F0EDE8` at 30% opacity
   - Arrowheads: small, at exit points

**Left panel sub-labels:**
- Element type: Text boxes below the barrel illustration
- Font: JetBrains Mono Regular
- Size: 14 pt
- Color: `#F0EDE8`
- Position: Centered under barrel, Y: 9.0", 9.4", 9.8" (three lines, stacked)
- Text (three separate text boxes):

> 6-8 RPM rotation

> Parts tumble through current field

> Intermittent electrical contact

**Cathode contact label:**
- Element type: Text box + line with arrowhead pointing to one cathode button
- Font: JetBrains Mono Regular, 12 pt, `#2EC4B6`
- Text: `Cathode contact`
- Arrow: 1 pt, `#2EC4B6`, from label to nearest button

---

**Center divider:**
- Element type: Line
- Start: X: 12.0", Y: 3.8". End: X: 12.0", Y: 10.8"
- Stroke: 2 pt, `#3A4055` (Mid Slate)

---

**Right panel title:**
- Element type: Text box
- Position: Centered within right panel (X center: ~18.0"). Y: 3.6"
- Font: Barlow Condensed ExtraBold
- Size: 24 pt
- Color: `#E8A020` (Amber)
- Alignment: Center
- Text:

> RACK PLATING

**Right panel — Rack illustration:**

Build the rack as a composite of geometric shapes:

1. **Power bus bar (horizontal at top):**
   - Element type: Rectangle
   - Position: X: 14.0". Y: 4.5"
   - Width: 8.0". Height: 0.25"
   - Fill: `#3A4055` (Mid Slate)

2. **Rack spine (vertical):**
   - Element type: Rectangle
   - Position: X: 17.75". Y: 4.75"
   - Width: 0.2". Height: 3.5"
   - Fill: `#3A4055`

3. **Crossbars (3 horizontal):**
   - Element type: 3 rectangles
   - Width: 4.0". Height: 0.12"
   - Fill: `#3A4055`
   - Position: Centered on spine (X: 15.85"), Y: 5.5", 6.5", 7.5"

4. **Hanging parts (4 parts on crossbars):**
   - Element type: 4 rectangles
   - Width: 0.8". Height: 1.8"
   - Fill: `#C8D0D8` (Bright Silver)
   - Position: 2 on top crossbar (X: 16.2" and 17.6", Y: 5.7"), 2 on middle crossbar (X: 16.2" and 17.6", Y: 6.7")
   - Connect to crossbars with small hook lines: short curved lines (0.15" tall), 1 pt, `#3A4055`

5. **Anodes (2 flanking the rack):**
   - Element type: 2 rectangles
   - Width: 0.5". Height: 3.0"
   - Fill: none (transparent)
   - Border: 2 pt, `#E8A020` (Amber)
   - Position: X: 14.5" and X: 21.0", Y: 5.0"

6. **Anode labels:**
   - Element type: 2 text boxes
   - Font: JetBrains Mono Regular, 12 pt, `#E8A020`
   - Text: `Anode`
   - Position: Centered below each anode rectangle

7. **Current arrows (from bus bar to rack):**
   - Element type: 2 lines with arrowheads
   - Start: top of bus bar. End: top of rack spine
   - Stroke: 1.5 pt, `#E8A020` (Amber)
   - Arrowhead: pointing down toward rack

**Right panel sub-labels:**
- Element type: Text boxes below the rack illustration
- Font: JetBrains Mono Regular
- Size: 14 pt
- Color: `#F0EDE8`
- Position: Centered under rack, Y: 9.0", 9.4", 9.8"
- Text:

> Continuous direct contact

> Parts fixed in position

> Full current exposure — 100% of cycle

---

### ZONE 3 — Head-to-Head Comparison Table (HERO)

**Dimensions:** Full page width within margins. Y: 11.5" to 25.2" (~13.7" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 11.7"
- Font: Barlow Condensed ExtraBold
- Size: 32 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> HEAD-TO-HEAD COMPARISON

---

**Table structure:**
- Full width within safe zone: X: 0.5" to 23.5" (23.0" wide)
- Y: 12.3" to 24.5" (~12.2" tall for header + 10 data rows + footnote)
- 3 columns:
  - Column 1 (Factor): X: 0.5" to 7.5" (~30% width, 7.0" wide)
  - Column 2 (Barrel): X: 7.5" to 15.5" (~35% width, 8.0" wide)
  - Column 3 (Rack): X: 15.5" to 23.5" (~35% width, 8.0" wide)

**Column header row:**
- Element type: Rectangle
- Position: X: 0.5". Y: 12.3"
- Width: 23.0". Height: 0.55"
- Fill: `#3A4055` (Mid Slate)

Header text boxes:
- `FACTOR` — Barlow SemiBold, 22 pt, `#F0EDE8`, X: 0.7", Y: 12.35"
- `BARREL` — Barlow SemiBold, 22 pt, `#2EC4B6` (Teal), X: 7.7", Y: 12.35"
- `RACK` — Barlow SemiBold, 22 pt, `#E8A020` (Amber), X: 15.7", Y: 12.35"

**Data rows — 10 rows, alternating fills:**

Each row: Height ~1.1" (may vary slightly based on text length). Build each row as:
1. Background rectangle (full row width): fill alternates `#1A1F2E` (odd) / `#252B3D` (even)
2. Three text boxes — one per column, with 0.2" internal padding from column edges

Row heights are estimated at ~1.1" each. Actual height should be set to fit the longest text in that row with comfortable padding (10 pt above and below text).

**Row 1 — Part Size** (Y: ~12.85", odd row `#1A1F2E`):
- Factor: `Part size` (Inter Medium, 18 pt, `#F0EDE8`)
- Barrel: `Small — typically < 6-8" longest dimension; < 1-2 lbs per part` (Inter Regular, 18 pt, `#F0EDE8`)
- Rack: `No practical upper limit — limited by tank size and rack capacity` (Inter Regular, 18 pt, `#F0EDE8`)

**Row 2 — Part Geometry** (even row `#252B3D`):
- Factor: `Part geometry`
- Barrel: `Must tumble freely; no nesting, tangling, or fragile features`
- Rack: `Any geometry — complex, delicate, or asymmetric parts accommodated`

**Row 3 — Volume** (odd row):
- Factor: `Volume`
- Barrel: `High volume — hundreds to thousands of parts per load`
- Rack: `Low to medium volume — parts individually fixtured`

**Row 4 — Electrical Contact** (even row):
- Factor: `Electrical contact`
- Barrel: `Intermittent — parts tumble against cathode buttons (~30-50% of cycle)`
- Rack: `Continuous — direct fixture-to-part contact (100% of cycle)`

**Row 5 — Current Density** (odd row):
- Factor: `Current density`
- Barrel: `Lower CD required (e.g., zinc: 5-10 ASF barrel vs. 15-20 ASF rack)`
- Rack: `Higher CD achievable — uniform current distribution`

**Row 6 — Deposit Uniformity** (even row):
- Factor: `Deposit uniformity`
- Barrel: `Less uniform — contact points get heavier deposit; recesses may plate thin`
- Rack: `More uniform — part position controls thickness distribution`

**Row 7 — Throwing Power** (odd row):
- Factor: `Throwing power`
- Barrel: `Higher throwing power required — current must reach buried parts`
- Rack: `Moderate — anode-to-cathode geometry can be optimized`

**Row 8 — Throughput** (even row):
- Factor: `Throughput (cost/part)`
- Barrel: `Lower cost per part at high volume — labor is loading/unloading only`
- Rack: `Higher cost per part — individual fixturing is labor-intensive`

**Row 9 — Surface Finish Risk** (odd row):
- Factor: `Surface finish risk`
- Barrel: `Part-to-part contact causes dings, scratches — not for cosmetic surfaces`
- Rack: `No part-to-part contact — suitable for cosmetic and decorative finishes`

**Row 10 — Plating Time** (even row):
- Factor: `Plating time`
- Barrel: `Longer — intermittent contact means effective plating time is 30-50% of total`
- Rack: `Shorter — full current exposure for the entire cycle`

---

**Table footnote:**
- Element type: Text box
- Position: X: 0.5". Y: immediately below last data row + 8 pt gap (approximately Y: 23.9")
- Width: 23.0"
- Font: Inter Regular
- Size: 13 pt
- Color: `#F0EDE8` at 60% opacity
- Style: Italic
- Text:

> CD ranges shown are representative for acid zinc plating (Drew's Quick Reference). Actual ranges vary by process — see Poster #11 Current Density Quick Reference for full process-specific CD data.

---

### ZONE 4 — Decision Guide

**Dimensions:** Full page width within margins. Y: 25.2" to 32.4" (~7.2" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 25.4"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> WHEN TO CHOOSE

---

**BLOCK D — Two-Column "Wins When" Callouts**

Y: 26.0" to 29.6" (~3.6" tall). Two columns with 0.3" gutter.

**Left column — "Barrel Wins When..."**

Callout container:
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 26.0"
- Width: 11.2". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt
- No border stroke on the rounded rectangle itself

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 26.0"
- Width: 0.06" (4 pt equivalent). Height: 3.5"
- Fill: `#2EC4B6` (Teal)
- Corner radius: 0

Callout title:
- Element type: Text box
- Position: X: 0.8" (inside container + 20 pt padding). Y: 26.2"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#2EC4B6` (Teal)
- Text:

> BARREL WINS WHEN...

Bullet list:
- Element type: Text box
- Position: X: 0.8". Y: 26.7"
- Width: 10.6"
- Font: Inter Regular
- Size: 18 pt
- Color: `#F0EDE8`
- Line height: 150%
- Text (use bullet list formatting):

> - Parts are small, durable, and can tumble freely
> - Volume is high and cost per part must be low
> - Cosmetic finish is not critical
> - Parts do not nest or tangle
> - Throwing power of the bath chemistry is adequate

**Right column — "Rack Wins When..."**

Callout container:
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 26.0"
- Width: 11.5". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 12.0". Y: 26.0"
- Width: 0.06". Height: 3.5"
- Fill: `#E8A020` (Amber)

Callout title:
- Element type: Text box
- Position: X: 12.3". Y: 26.2"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#E8A020` (Amber)
- Text:

> RACK WINS WHEN...

Bullet list:
- Element type: Text box
- Position: X: 12.3". Y: 26.7"
- Width: 10.9"
- Font: Inter Regular
- Size: 18 pt
- Color: `#F0EDE8`
- Line height: 150%
- Text:

> - Parts are large, fragile, or have complex geometry
> - Deposit uniformity or thickness control is critical
> - Surface finish is cosmetic or decorative
> - Volume is low to medium (custom or job-shop work)
> - Specifications require measurable thickness at specific locations

---

**BLOCK E — Decision Flowchart Strip**

- Element type: Rounded rectangle (strip background)
- Position: X: 0.5". Y: 30.0"
- Width: 23.0". Height: 2.0"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt

Four decision boxes, evenly spaced across the strip (each ~5.0" wide, 0.3" gaps between boxes, 0.25" padding from strip edges):

**Box 1 — Part Size:**
- Element type: Rounded rectangle
- Position: X: 0.75". Y: 30.25"
- Width: 5.0". Height: 1.5"
- Fill: `#252B3D`
- Border: 1 pt, `#3A4055`
- Corner radius: 6 pt

Question text:
- Font: Inter Medium, 16 pt, `#F0EDE8`
- Position: Centered in upper half of box
- Text: `Small and durable?`

Answer text:
- Font: JetBrains Mono Regular, 14 pt
- Position: Centered in lower half of box
- Text line 1: `YES` in `#2EC4B6` (Teal) + ` → Barrel` in `#F0EDE8`
- Text line 2: `NO` in `#E8A020` (Amber) + ` → Rack` in `#F0EDE8`

**Box 2 — Volume:**
- Position: X: 6.25". Y: 30.25"
- Same dimensions and styling as Box 1
- Question: `High volume?`
- Answers: `YES → Barrel` / `NO → Rack`

**Box 3 — Cosmetic:**
- Position: X: 11.75". Y: 30.25"
- Same dimensions and styling
- Question: `Cosmetic finish required?`
- Answers: `YES → Rack` (note: reversed — YES means Rack) / `NO → Barrel`

**Box 4 — Thickness Spec:**
- Position: X: 17.25". Y: 30.25"
- Same dimensions and styling
- Question: `Tight thickness spec?`
- Answers: `YES → Rack` / `NO → Either` (in `#F0EDE8`)

**Arrow connectors between boxes:**
- Element type: Line with arrowhead
- 3 arrows: Box 1 right edge to Box 2 left edge, Box 2 to Box 3, Box 3 to Box 4
- Stroke: 2 pt, `#3A4055` (Mid Slate)
- Arrowhead: at the right end (pointing right)
- Y position: Centered vertically in the strip (approximately Y: 31.0")
- Length: spans the 0.3" gap between boxes (short connectors)

---

### ZONE 5 — Footer Band

**Dimensions:** Full page width. Y: 32.4" to 36.0" (~3.6" tall).

---

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.4"
- Width: 24.0". Height: 3.6"
- Fill: `#0D1020` (Deep Navy)

**Bold disclaimer:**
- Element type: Text box
- Position: X: 0.5". Y: 32.7"
- Width: 23.0"
- Font: Inter Regular
- Size: 11 pt
- Color: `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster is a decision reference tool. Process selection depends on specific part geometry, specification requirements, and bath chemistry. Consult your process supplier for application-specific guidance.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Barrel vs. Rack Plating — Choosing the Right Method

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
| Zone 2 - Barrel vs Rack Illustration | Section label, barrel illustration, rack illustration, center divider, sub-labels |
| Zone 3 - Comparison Table | Section label, header row, 10 data rows, footnote |
| Zone 4 - Decision Guide | Section label, Barrel Wins callout, Rack Wins callout, decision flowchart strip |
| Zone 5 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

After grouping, lock each completed zone (right-click > Lock) before proceeding to the next.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, decision strip background |
| `#252B3D` | `#E8E8F0` | Alternate table row backgrounds, decision boxes |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements (Rack headers, titles) |
| `#2EC4B6` | `#1A8C82` | Teal accent elements (Barrel headers, titles) |
| `#27AE60` | `#1E7A47` | Emerald accent elements (if used) |
| `#E05C5C` | `#B83E3E` | Coral accent elements (if used) |
| `#3A4055` | `#D0D4DE` | Table rules, dividers, illustration outlines |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

Column headers use Teal and Amber as text accents (not fills), so standard remap is sufficient. No overrides required.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Barrel vs Rack — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Barrel vs Rack — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Barrel vs Rack — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Barrel vs Rack — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Barrel vs Rack — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Barrel vs Rack — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #13 — Barrel vs. Rack Plating — Construction Workup v1.0*
*2026-04-04*
