---
Project: Plating Posters Inc
Poster Number: 10
Title: Electroless Nickel — Process Overview and Bath Control
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-03T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 10 — Electroless Nickel — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Electroless Nickel — Alaina Research Brief v2 (2026-03-21)
Watson Flags: NONE — all data sourced directly from Research Brief v2; no new flags raised
Process Scope: Electroless nickel (Ni-P autocatalytic) only — one process per poster
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickel
  - ConstructionWorkup
---

# Poster # Poster #10 — Construction Workup
## Electroless Nickel — Process Overview and Bath Control

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-03*

This document is the construction workup for Poster #10. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. All technical content is confirmed production-ready. All Watson flags are cleared.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 10 — Electroless Nickel — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for table rows, callout boxes, accent borders, and gauge segments
- Table elements (manually constructed grid of rectangles + text boxes — recommended over the native table tool for full styling control)
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for application industry icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Uniform coating illustration:** Complex freeform vector illustration requires geometric shape composites. The cross-section diagram (Block C) must be built as a composite of simple geometric shapes (rectangles for substrates, rectangles for deposit layers, line elements for arrows). **Recommendation: build as layered rectangles.** This approach was validated on Poster #4's Hull cell panel illustration and works well.

2. **MTO gauge with rounded corners:** The MTO gauge (Block F) requires three adjacent colored rectangles masked by a single rounded-corner container. In the design, build the outer rounded rectangle as a border, place three flat-edge rectangles inside for the color zones, then group and use the clip-mask (right-click > "Use as mask") to round the corners uniformly. If clip-mask behavior is inconsistent, build as three separate rounded rectangles with corner radius only on the outer edges (left-only radius on the green zone, no radius on amber, right-only radius on coral). The tool supports per-corner radius adjustments on rectangles.

3. **4 pt left-border accents on table rows:** Same technique as Poster #4 — simulate with a narrow colored rectangle (4 pt equivalent width, approximately 0.06") positioned flush against the left edge of each row rectangle.

4. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Producing the Light edition requires duplicating the design page and manually recoloring every element per the remap table in Part 6. Work through the table from top to bottom — background first, then text, then fills, then accents.

5. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** If Drew has the tool, upload JetBrains Mono Regular from Google Fonts before beginning. If unavailable, substitute **Courier Prime** (available in the standard library). Flag this substitution visibly in the build.

6. **Print size — 24x36":** The tool supports custom page sizes. Set to exactly 24 inches wide by 36 inches tall at document creation. For the 18x24" version, duplicate and resize — accept the tool's auto-resize for a starting point, then verify all text meets the 14 pt minimum floor.

7. **Shield and magnet icons in P% table:** standard icon library has shield shapes and magnet shapes. Search for "shield" and "magnet" respectively. If exact matches are unavailable, use simple geometric shapes (pentagon for shield, U-shape for magnet) or Unicode characters as fallbacks. The text labels are the primary indicators — icons are reinforcement only.

8. **Sub/superscript characters:** The tool does not natively support subscript/superscript formatting. For chemical formulas (Ni2+, H2PO2-, H2O, H2, H+, Cr6+, H2SO4, NaOH, NH4OH), type the Unicode subscript/superscript characters directly. These are provided verbatim in the copy blocks below — copy-paste them exactly.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

These are the first steps Drew should complete before placing any content.

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: **24 inches**. Height: **36 inches**.
- This creates the 24x36" master poster artboard.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)
- This is the Dark edition background. Every subsequent element sits on this.

### Step 3 — Upload fonts (the Pro tier required)
Upload from Google Fonts / JetBrains.org:
- **Barlow Condensed ExtraBold** — all headlines and zone labels
- **Barlow SemiBold** — all subheadings, section labels, callout titles
- **Inter Regular** and **Inter Medium** — all body text and table data
- **JetBrains Mono Regular** — all parameter/data table values and sub-labels

If JetBrains Mono upload fails, substitute **Courier Prime** for all JetBrains Mono specifications below.

### Step 4 — Set up color palette (save as Brand Colors )
Save all of the following as Brand Colors for this design. Name them exactly as shown:

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Section titles, Mid-P column, MTO warning zone |
| Teal | `#2EC4B6` | Callout borders/titles, Low-P column, Electroless panel labels |
| Emerald | `#27AE60` | MTO normal zone |
| Coral | `#E05C5C` | High-P column, critical callouts, Electrolytic panel labels |
| Mid Slate | `#3A4055` | Table header fills, row rules, dividers, substrate shapes |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, row label column background |
| Alt Row | `#252B3D` | Alternating table row backgrounds |
| Bright Silver | `#C8D0D8` | Nickel deposit illustration |

### Step 5 — Set ruler guides
Pull guides from the design's ruler area to the following positions:

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 3.2" — Zone 1/Zone 2 boundary
- 9.3" — Zone 2/Zone 3 boundary
- 21.5" — Zone 3/Zone 4 boundary
- 26.5" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it** to prevent accidental displacement while working on adjacent zones.

```
ZONE 1 — HEADER BAND (top 0"–3.2")
  Block A: Headline + subheading + tagline (left ~60%)
  Block B: "How It Works" autocatalytic reaction callout (right ~40%)

ZONE 2 — UNIFORM COATING ILLUSTRATION (3.2"–9.3" / ~6.1" tall)
  Block C: Two-panel cross-section — Electrolytic (left) vs. Electroless (right)
  Section label + central comparison banner + sub-labels

ZONE 3 — PHOSPHORUS PROPERTY SPECTRUM TABLE (9.3"–21.5" / ~12.2" tall)
  Block D: Full-width three-column P% comparison table (HERO data block)
  Section label + sub-label + 10 data rows + heat treatment note + footnote

ZONE 4A — BATH CONTROL PARAMETERS (21.5"–26.5" / ~5.0" tall, left 58%)
  Block E: Parameter reference table + critical pH callout

ZONE 4B — BATH LIFE / MTO GAUGE (21.5"–26.5", right 42%)
  Block F: Visual MTO gauge + MTO definition + discard threshold

ZONE 5 — APPLICATIONS + SPECIFICATIONS (26.5"–32.4" / ~5.9" tall)
  Block G: 6-icon industry applications grid (left 62%)
  Block H: Governing specifications card stack (right 38%)

ZONE 6 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block I: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Height: 3.2" from the top of the page (Y: 0" to 3.2").
**Background:** Same as page (`#1A1F2E`) — no separate fill needed.

---

**BLOCK A — Headline**

- Element type: Text box
- Position: X: 0.5" (left safe zone). Y: 0.5" (top safe zone)
- Width: 13.0" (approximately 56% of artboard width — leaves room for Block B at right)
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> ELECTROLESS NICKEL

**BLOCK A — Subheading Line 1**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 13.0"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#E8A020` (Amber)
- Text:

> Process Overview and Bath Control

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 13.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65% (transparency slider on the text element — set to 65)
- Text:

> Uniform thickness. No current. No compromises.

---

**BLOCK B — "How It Works" Autocatalytic Reaction Callout Box**

This is a callout box positioned in the upper-right of the header band.

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 13.75" (right-aligned with 0.5" right margin, accounting for box width). Y: 0.5"
- Width: 9.25" (from X: 13.75" to X: 23.0", plus 0.5" right safe zone = flush with 23.5" guide)
- Height: 2.5" (sized to fit all content with 20 pt internal padding)
- Fill color: `#1E2435` (Dark Callout)
- Border (stroke): 1.5 pt, color `#2EC4B6` (Teal)
- Corner radius: 8 pt

**Callout title:**
- Element type: Text box inside the container
- Position: X: 14.05" (container left edge + 20 pt padding). Y: 0.75" (container top + 20 pt padding)
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#2EC4B6` (Teal)
- Text:

> HOW IT WORKS

**Reaction equation:**
- Element type: Text box inside the container
- Position: X: centered horizontally within container. Y: below title + 10 pt gap (approximately Y: 1.1")
- Width: 8.85" (container width minus 40 pt total padding)
- Font: JetBrains Mono Regular
- Size: 18 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text (copy-paste these Unicode characters exactly):

> Ni²⁺ + H₂PO₂⁻ + H₂O → Ni-P + H₂ + H⁺

**Body explanation:**
- Element type: Text box inside the container
- Position: X: 14.05". Y: below equation + 10 pt gap (approximately Y: 1.5")
- Width: 8.85"
- Font: Inter Regular
- Size: 17 pt
- Color: `#F0EDE8`
- Line height: 140% (spacing: 1.4)
- Text:

> Sodium hypophosphite donates electrons, reducing nickel ions to metallic Ni-P alloy directly on the part surface — no rectifier, no anodes, no external current required.

**Closing label:**
- Element type: Text box inside the container + narrow accent rectangle
- Accent rectangle: Width 2 pt, height matching text line height (~20 pt), fill `#2EC4B6`, positioned at X: 14.05", flush left
- Text position: X: 14.25" (right of accent rule + 8 pt gap). Y: below body + 8 pt gap (approximately Y: 2.4")
- Font: Inter Medium
- Size: 16 pt
- Color: `#2EC4B6` (Teal)
- Text:

> No external current — chemistry does the work.

---

### ZONE 2 — Uniform Coating Illustration

**Dimensions:** Full page width within margins. Y: 3.2" to 9.3" (~6.1" tall).

---

**Section label (above illustration):**
- Element type: Text box
- Position: Centered horizontally on artboard. Y: 3.4" (0.2" below Zone 1 boundary)
- Width: 23.0" (full safe zone width)
- Font: Barlow Condensed ExtraBold
- Size: 30 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE UNIFORM COATING ADVANTAGE

---

**Illustration area:** Y: 3.9" to 8.5" (~4.6" available for the two-panel diagram). The illustration is divided into two side-by-side panels with a center divider.

**Left panel — Electrolytic Nickel:** X: 0.5" to 10.85" (45% of 23.0" safe zone = 10.35" wide)
**Center divider:** X: 11.0" (vertical line)
**Right panel — Electroless Nickel:** X: 11.15" to 23.5" (45% of 23.0" = 10.35" wide)
**Center gap for divider:** 0.3" (10.85" to 11.15")

---

**Left panel title:**
- Element type: Text box
- Position: Centered within left panel (X center: ~5.68"). Y: 3.9"
- Font: Barlow Condensed ExtraBold
- Size: 22 pt
- Color: `#E05C5C` (Coral)
- Alignment: Center
- Text:

> ELECTROLYTIC NICKEL

**Left panel substrate (inverted U-channel):**

Build the substrate as three rectangles forming an inverted U-shape:

1. **Top horizontal bar:**
   - Element type: Rectangle
   - Position: X: 2.5". Y: 5.0"
   - Width: 6.5". Height: 0.6"
   - Fill: `#3A4055` (Mid Slate)
   - No corner radius

2. **Left vertical wall:**
   - Element type: Rectangle
   - Position: X: 2.5". Y: 5.6"
   - Width: 1.0". Height: 2.0"
   - Fill: `#3A4055`

3. **Right vertical wall:**
   - Element type: Rectangle
   - Position: X: 8.0". Y: 5.6"
   - Width: 1.0". Height: 2.0"
   - Fill: `#3A4055`

**Left panel deposit rectangles (Bright Silver `#C8D0D8`) — UNEVEN thickness:**

4. **Top surface deposit (THICK — HCD):**
   - Rectangle: X: 2.3". Y: 4.55". Width: 6.9". Height: 0.45"
   - Fill: `#C8D0D8`
   - *This sits on top of the substrate bar — exaggerated thick*

5. **Left outer corner buildup (THICK):**
   - Rectangle: X: 2.05". Y: 4.55". Width: 0.45". Height: 2.0"
   - Fill: `#C8D0D8`

6. **Right outer corner buildup (THICK):**
   - Rectangle: X: 9.0". Y: 4.55". Width: 0.45". Height: 2.0"
   - Fill: `#C8D0D8`

7. **Internal recess floor deposit (THIN — LCD):**
   - Rectangle: X: 3.5". Y: 7.5". Width: 4.5". Height: 0.1"
   - Fill: `#C8D0D8`
   - *Barely visible — this is intentional*

8. **Left internal wall deposit (THIN):**
   - Rectangle: X: 3.4". Y: 5.6". Width: 0.1". Height: 1.9"
   - Fill: `#C8D0D8`

9. **Right internal wall deposit (THIN):**
   - Rectangle: X: 8.0". Y: 5.6". Width: 0.1". Height: 1.9"
   - Fill: `#C8D0D8`

**Left panel labels and arrows:**

10. **Arrow to thick corner deposit:**
    - Element type: Line with arrowhead
    - Start: X: 1.3", Y: 4.8". End: X: 2.1", Y: 4.8"
    - Stroke: 1.5 pt, `#E05C5C` (Coral). Arrowhead at end (right side).

11. **Label for thick deposit:**
    - Text box: X: 0.5". Y: 4.6"
    - Font: JetBrains Mono Regular, 14 pt, `#E05C5C`
    - Text: `THICK — HCD`

12. **Arrow to thin recess deposit:**
    - Element type: Line with arrowhead
    - Start: X: 4.5", Y: 8.2". End: X: 5.0", Y: 7.65"
    - Stroke: 1.5 pt, `#E05C5C`. Arrowhead at end.

13. **Label for thin deposit:**
    - Text box: X: 3.5". Y: 8.2"
    - Font: JetBrains Mono Regular, 14 pt, `#E05C5C`
    - Text: `THIN — LCD`

**Left panel sub-label:**
- Element type: Text box
- Position: Centered under left panel. Y: 8.0"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70% opacity
- Alignment: Center
- Text:

> 5-10x thickness variation edge-to-recess

---

**Center divider:**
- Element type: Line
- Start: X: 11.0", Y: 4.3". End: X: 11.0", Y: 8.0"
- Stroke: 2 pt, `#3A4055` (Mid Slate)

---

**Right panel title:**
- Element type: Text box
- Position: Centered within right panel (X center: ~17.33"). Y: 3.9"
- Font: Barlow Condensed ExtraBold
- Size: 22 pt
- Color: `#2EC4B6` (Teal)
- Alignment: Center
- Text:

> ELECTROLESS NICKEL

**Right panel substrate (identical U-channel shape):**

Build with same three-rectangle construction, shifted right:

14. **Top horizontal bar:**
    - Position: X: 13.15". Y: 5.0". Width: 6.5". Height: 0.6"
    - Fill: `#3A4055`

15. **Left vertical wall:**
    - Position: X: 13.15". Y: 5.6". Width: 1.0". Height: 2.0"
    - Fill: `#3A4055`

16. **Right vertical wall:**
    - Position: X: 18.65". Y: 5.6". Width: 1.0". Height: 2.0"
    - Fill: `#3A4055`

**Right panel deposit rectangles (Bright Silver `#C8D0D8`) — UNIFORM thickness:**

All deposit rectangles are the same thickness (0.2" height or 0.2" width):

17. **Top surface deposit:**
    - Rectangle: X: 12.95". Y: 4.8". Width: 6.9". Height: 0.2"
    - Fill: `#C8D0D8`

18. **Left outer wall deposit:**
    - Rectangle: X: 12.95". Y: 4.8". Width: 0.2". Height: 2.8"
    - Fill: `#C8D0D8`

19. **Right outer wall deposit:**
    - Rectangle: X: 19.65". Y: 4.8". Width: 0.2". Height: 2.8"
    - Fill: `#C8D0D8`

20. **Internal recess floor deposit:**
    - Rectangle: X: 14.15". Y: 7.4". Width: 4.5". Height: 0.2"
    - Fill: `#C8D0D8`

21. **Left internal wall deposit:**
    - Rectangle: X: 14.05". Y: 5.6". Width: 0.2". Height: 2.0"
    - Fill: `#C8D0D8`

22. **Right internal wall deposit:**
    - Rectangle: X: 18.55". Y: 5.6". Width: 0.2". Height: 2.0"
    - Fill: `#C8D0D8`

**Right panel labels and arrows:**

23. **Arrow to corner deposit:**
    - Start: X: 12.2", Y: 4.9". End: X: 12.95", Y: 4.9"
    - Stroke: 1.5 pt, `#2EC4B6` (Teal). Arrowhead at end.

24. **Label "UNIFORM":**
    - Text box: X: 11.3". Y: 4.7"
    - Font: JetBrains Mono Regular, 14 pt, `#2EC4B6`
    - Text: `UNIFORM`

25. **Arrow to recess deposit:**
    - Start: X: 15.2", Y: 8.2". End: X: 15.8", Y: 7.65"
    - Stroke: 1.5 pt, `#2EC4B6`. Arrowhead at end.

26. **Label "UNIFORM" (second):**
    - Text box: X: 14.5". Y: 8.2"
    - Font: JetBrains Mono Regular, 14 pt, `#2EC4B6`
    - Text: `UNIFORM`

**Right panel sub-label:**
- Element type: Text box
- Position: Centered under right panel. Y: 8.0"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70% opacity
- Alignment: Center
- Text:

> plus-minus 1-2 micrometer across all surfaces

*Note: Type the actual Unicode characters: ±1–2 µm across all surfaces*

---

**Central callout banner (overlays the divider, centered across both panels):**
- Element type: Rounded rectangle + text box
- Rectangle position: Centered at X: 7.0" to 17.0" (10.0" wide). Y: 6.3" to 6.8" (0.5" tall)
- Fill: `#1E2435` (Dark Callout)
- Border: 1 pt, `#2EC4B6` (Teal)
- Corner radius: 6 pt
- Text position: Centered within rectangle
- Font: Barlow SemiBold, 18 pt, `#F0EDE8`
- Alignment: Center
- Text:

> ±1–2 µm uniformity vs. 5–10x variation for electroplating

**Layer order within Zone 2 (bottom to top):**
1. Left panel substrate rectangles (`#3A4055`)
2. Left panel deposit rectangles (`#C8D0D8`) — thick/thin
3. Left panel labels, arrows (Coral)
4. Left panel title text
5. Right panel substrate rectangles (`#3A4055`)
6. Right panel deposit rectangles (`#C8D0D8`) — uniform
7. Right panel labels, arrows (Teal)
8. Right panel title text
9. Center divider rule (`#3A4055`)
10. Central callout banner (on top of divider)
11. Sub-labels and section label (topmost text layer)

**Group all Zone 2 elements after completion.**

---

### ZONE 3 — Phosphorus Property Spectrum Table

**Dimensions:** Full page width within margins. Y: 9.3" to 21.5" (~12.2" tall).
**This is the HERO data element of the poster** — it occupies the largest single zone and contains the primary data payload.

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 9.5" (0.2" below Zone 2 boundary)
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 34 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE PHOSPHORUS PROPERTY SPECTRUM

**Section sub-label:**
- Element type: Text box
- Position: Centered horizontally. Y: 10.1" (below section label + 8 pt gap)
- Width: 20.0" (slightly narrower to create visual breathing room)
- Font: Inter Regular
- Size: 18 pt
- Color: `#F0EDE8` at 65% opacity
- Alignment: Center
- Text:

> Phosphorus content is the single most important characteristic of an EN deposit — it governs hardness, corrosion resistance, and magnetic behavior.

---

**Table construction method:**

Build the table as a stack of layered rectangles and text boxes — do NOT use the native table tool. This gives full control over per-cell colors, left-border accents, and alternating row fills.

**Table position:** X: 0.5" to 23.5" (full safe zone width = 23.0"). Y: 10.7" to approximately 20.7" (~10.0" table height).

**Column widths (total = 23.0"):**
- Column 0 — Row labels: 5.06" (22% of 23.0")
- Column 1 — Low-P: 5.98" (26%)
- Column 2 — Mid-P: 5.98" (26%)
- Column 3 — High-P: 5.98" (26%)

**Column X positions:**
- Row label column: X: 0.5" to 5.56"
- Low-P column: X: 5.56" to 11.54"
- Mid-P column: X: 11.54" to 17.52"
- High-P column: X: 17.52" to 23.5"

**Row height:** Each row approximately 0.7" (to accommodate 18–20 pt text with 12 pt top/bottom padding). Header row: 0.7". Sub-header row (P% range): 0.5". Data rows: 0.7" each. Heat treatment note: 0.5". Total: 0.7 + 0.5 + (10 x 0.7) + 0.5 = 8.7". This fits within the 10.0" allocation.

---

**Build sequence for the table:**

**Step 1 — Column header row**

Starting Y: 10.7". Row height: 0.7".

| Cell | X Start | Width | Fill | Text | Font | Text Color |
|---|---|---|---|---|---|---|
| PROPERTY label | 0.5" | 5.06" | `#3A4055` | PROPERTY | Barlow SemiBold, 22 pt | `#F0EDE8` |
| LOW-PHOSPHORUS | 5.56" | 5.98" | `#2EC4B6` (Teal) | LOW-PHOSPHORUS | Barlow Condensed ExtraBold, 24 pt | `#1A1F2E` |
| MID-PHOSPHORUS | 11.54" | 5.98" | `#E8A020` (Amber) | MID-PHOSPHORUS | Barlow Condensed ExtraBold, 24 pt | `#1A1F2E` |
| HIGH-PHOSPHORUS | 17.52" | 5.98" | `#E05C5C` (Coral) | HIGH-PHOSPHORUS | Barlow Condensed ExtraBold, 24 pt | `#F0EDE8` |

Build each cell as a rectangle + text box layered on top. Text is center-aligned within each cell rectangle.

*Contrast note: Teal and Amber headers use dark text `#1A1F2E` for WCAG compliance. Coral is dark enough that Warm White `#F0EDE8` passes WCAG AAA.*

**Step 2 — P% range sub-header row**

Starting Y: 11.4". Row height: 0.5".

| Cell | Fill | Text | Font | Text Color |
|---|---|---|---|---|
| Row label (empty) | `#1E2435` | (leave blank) | — | — |
| Low-P range | `#2EC4B6` at 40% opacity | 1–4% by weight | JetBrains Mono Regular, 18 pt | `#F0EDE8` |
| Mid-P range | `#E8A020` at 40% opacity | 5–9% by weight | JetBrains Mono Regular, 18 pt | `#F0EDE8` |
| High-P range | `#E05C5C` at 40% opacity | 10–14% by weight | JetBrains Mono Regular, 18 pt | `#F0EDE8` |

*Set the rectangle fill to the accent color, then reduce the rectangle's transparency to 40% using the transparency slider. Place white text on top — the text remains at 100% opacity.*

**Step 3 — Data rows (10 rows)**

Starting Y: 11.9". Each row 0.7" tall.

For every data row, build:
1. **Row label column rectangle:** X: 0.5", width 5.06", fill `#1E2435` (Dark Callout)
2. **Left-border accent rectangle:** X: 0.5", width 0.06" (4 pt), full row height, color per row spec below
3. **Three data cell rectangles** at columns 1/2/3 positions, fill alternating between `#1A1F2E` (odd rows) and `#252B3D` (even rows)
4. **Text boxes** for each cell

**Complete row specifications:**

*Build one complete row first (all 4 rectangles + left-border + 4 text boxes), then duplicate it 9 times and update content, fills, and border colors.*

**Row 1 — Bath pH** (Y: 11.9")
- Row background: `#1A1F2E` (odd)
- Left-border: `#2EC4B6` Teal, 0.06" wide
- Row label: **Bath pH** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **6.0–9.0** — JetBrains Mono Regular, 18 pt, `#F0EDE8`
- Mid-P: **4.7–5.0** — JetBrains Mono Regular, 18 pt, `#F0EDE8`
- High-P: **4.4–4.8** — JetBrains Mono Regular, 18 pt, `#F0EDE8`

**Row 2 — Bath Temp** (Y: 12.6")
- Row background: `#252B3D` (even)
- Left-border: `#2EC4B6` Teal
- Row label: **Bath Temp** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **65–80°C**
- Mid-P: **85–91°C**
- High-P: **82–90°C**

**Row 3 — Deposition Rate** (Y: 13.3")
- Row background: `#1A1F2E` (odd)
- Left-border: `#E8A020` Amber
- Row label: **Deposition Rate** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **10–15 µm/hr**
- Mid-P: **→ 18–25 µm/hr** (include a right-pointing arrow character `→` in Amber `#E8A020` before the value to flag "fastest" — secondary indicator)
- High-P: **10–13 µm/hr**

**Row 4 — Hardness As-Plated** (Y: 14.0")
- Row background: `#252B3D` (even)
- Left-border: `#E8A020` Amber
- Row label: **Hardness — As-Plated** — Inter Medium, 18 pt, `#F0EDE8`. Below the label, add **(HV)** in JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70% opacity
- Low-P: **650–750 HV**
- Mid-P: **500–600 HV**
- High-P: **450–550 HV**

**Row 5 — Hardness After HT** (Y: 14.7")
- Row background: `#1A1F2E` (odd)
- Left-border: `#E8A020` Amber
- Row label: **Hardness — After 400°C HT** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **1000–1100 HV** — use Inter Medium weight (not Regular) to emphasize this value approaches hard chrome territory
- Mid-P: **850–1000 HV**
- High-P: **800–900 HV**

**Row 6 — Salt Spray** (Y: 15.4")
- Row background: `#252B3D` (even)
- Left-border: `#2EC4B6` Teal
- Row label: **Salt Spray (ASTM B117)** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **~96–240 hrs** + small shield icon (search: "shield") sized ~16x16 pt, color `#2EC4B6`, positioned after the text
- Mid-P: **~240–500 hrs** + medium shield icon sized ~20x20 pt, color `#E8A020`
- High-P: **1,000+ hrs** + large shield icon sized ~24x24 pt with a "+" inside, color `#E05C5C`
- *Shield icons are secondary indicators for the corrosion gradient — text values are primary.*

**Row 7 — Magnetic Behavior** (Y: 16.1")
- Row background: `#1A1F2E` (odd)
- Left-border: `#3A4055` Mid Slate (neutral property)
- Row label: **Magnetic Behavior** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **Ferromagnetic** + magnet icon (search: "magnet"), filled, ~16x16 pt, color `#2EC4B6`
- Mid-P: **Weakly mag. to non-mag.** + half-filled magnet icon (or magnet with "~"), ~16x16 pt, color `#E8A020`
- High-P: **Non-magnetic** + magnet icon with X through it (or magnet with line-through), ~16x16 pt, color `#E05C5C`
- *Icons are secondary indicators — text labels are primary.*

**Row 8 — Solderability** (Y: 16.8")
- Row background: `#252B3D` (even)
- Left-border: `#3A4055` Mid Slate
- Row label: **Solderability** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **Excellent** + filled circle `●` in `#F0EDE8`
- Mid-P: **Moderate** + half circle `◑` in `#F0EDE8`
- High-P: **Poor** + empty circle `○` in `#F0EDE8`

**Row 9 — ASTM B733 Type** (Y: 17.5")
- Row background: `#1A1F2E` (odd)
- Left-border: `#3A4055` Mid Slate
- Row label: **ASTM B733 Type** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **Type II / III** — JetBrains Mono Regular, 16 pt (slightly reduced)
- Mid-P: **Type IV** — JetBrains Mono Regular, 16 pt
- High-P: **Type V** — JetBrains Mono Regular, 16 pt

**Row 10 — Primary Applications** (Y: 18.2", height 0.9" — taller to allow text wrap)
- Row background: `#252B3D` (even)
- Left-border: `#2EC4B6` Teal
- Row label: **Primary Applications** — Inter Medium, 18 pt, `#F0EDE8`
- Low-P: **Electronics, contacts, wear after HT** — Inter Regular (not Mono), 18 pt, `#F0EDE8`, line height 140%
- Mid-P: **Aerospace, automotive, tooling** — Inter Regular, 18 pt, `#F0EDE8`, line height 140%
- High-P: **Oil & gas downhole, chemical processing** — Inter Regular, 18 pt, `#F0EDE8`, line height 140%

---

**Step 4 — Heat Treatment Note (inline callout)**

Position: Below Row 10. Y: 19.2" (after last data row). Full table width (23.0").

- Element type: Rounded rectangle + text
- Rectangle: X: 0.5". Width: 23.0". Height: 0.55"
- Fill: `#1E2435` (Dark Callout)
- Border: 1 pt, `#E8A020` (Amber)
- Corner radius: 6 pt
- Text position: Centered vertically within box, 14 pt left padding
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Text:

> After 400°C / 1 hr heat treatment — Low-P approaches hard chrome hardness (900–1100 HV). No Cr⁶⁺. No environmental burden.

---

**Step 5 — Table footnote**

Position: Below heat treatment note. Y: 19.85". Left-aligned at X: 0.5".

- Element type: Text box
- Width: 23.0"
- Font: Inter Regular, 13 pt, `#F0EDE8` at 60% opacity
- Line height: 150%
- Text (italic):

> *Mid-P baths at 8–9% P may approach the non-magnetic threshold — confirm by testing per ASTM F2088 when non-magnetism is specified. | Salt spray hours at 25 µm deposit thickness. | HV = Vickers hardness.*

---

**Group all Zone 3 elements after completion.**

---

### ZONE 4A — Bath Control Parameters (Left Column)

**Dimensions:** X: 0.5" to 13.9" (58% of 23.0" safe zone = 13.34", rounded to 13.4"). Y: 21.5" to 26.5" (~5.0" tall).

---

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 21.7"
- Font: Barlow Condensed ExtraBold
- Size: 26 pt
- Color: `#E8A020` (Amber)
- Text:

> BATH CONTROL PARAMETERS

---

**Table header row:**

Starting Y: 22.2". Row height: 0.5".

- Rectangle: X: 0.5". Width: 13.4". Fill: `#3A4055`
- Column 1 "PARAMETER": X: 0.5", width 7.0". Text: Barlow SemiBold, 20 pt, `#E8A020`
- Column 2 "TARGET / RANGE": X: 7.5", width 6.4". Text: Barlow SemiBold, 20 pt, `#E8A020`

**Table data rows (7 rows, each 0.45" tall):**

Build using rectangle-stack method. Alternating fills: `#1A1F2E` (odd) / `#252B3D` (even). No left-border accents on this table.

All text: JetBrains Mono Regular, 18 pt, `#F0EDE8`.

| Row | Y Start | Background | Parameter | Target / Range |
|---|---|---|---|---|
| 1 | 22.7" | `#1A1F2E` | pH — acid baths (Mid-P, High-P) | 4.4–5.0 (hold ±0.2) |
| 2 | 23.15" | `#252B3D` | pH — alkaline baths (Low-P) | 6.0–9.0 (hold ±0.2) |
| 3 | 23.6" | `#1A1F2E` | Temperature — all classes | 65–91°C (±2°C min; ±1°C pref.) |
| 4 | 24.05" | `#252B3D` | Ni²⁺ concentration | 4.5–6.5 g/L |
| 5 | 24.5" | `#1A1F2E` | Hypophosphite concentration | 20–30 g/L |
| 6 | 24.95" | `#252B3D` | Bath loading factor | 0.25–0.50 dm²/L |
| 7 | 25.4" | `#1A1F2E` | Orthophosphite — discard at | > 120 g/L |

---

**Critical pH callout (below table):**

Position: X: 0.5". Y: 25.95". Width: 13.4". Height: ~0.5" (auto-expand to fit content).

- Element type: Rounded rectangle + text
- Fill: `#1E2435` (Dark Callout)
- Border: 2 pt, `#E05C5C` (Coral)
- Corner radius: 6 pt
- Internal padding: 12 pt

**Callout label:**
- Font: Barlow SemiBold, 16 pt, `#E05C5C` (Coral)
- Text:

> CRITICAL — pH CONTROL

**Callout body:**
- Font: Inter Regular, 15 pt, `#F0EDE8`
- Line height: 140%
- Text:

> pH drops continuously as plating proceeds — H⁺ is produced by the reaction with every deposit cycle. Check pH every 30–60 minutes in production. Adjust up: NaOH or NH₄OH. Adjust down: dilute H₂SO₄.

*Design note: The full-length pH callout text from the Content Draft has been condensed here to fit the available 0.5" height. The critical information — continuous pH drop, check frequency, and adjustment chemicals — is preserved. If more height is available during build, expand to include the second sentence about automatic pH controllers.*

---

**Group all Zone 4A elements after completion.**

---

### ZONE 4B — Bath Life / MTO Gauge (Right Column)

**Dimensions:** X: 14.15" (after 0.25" gutter from Zone 4A). Width: 9.35" (to X: 23.5"). Y: 21.5" to 26.5" (~5.0" tall).

---

**Section label:**
- Element type: Text box
- Position: X: 14.15". Y: 21.7"
- Width: 9.35"
- Font: Barlow Condensed ExtraBold
- Size: 26 pt
- Color: `#E8A020` (Amber)
- Text:

> BATH LIFE — METAL TURNOVERS (MTO)

---

**MTO gauge construction:**

Position: X: 14.15". Y: 22.4". Width: 9.35". Height: 1.2".

**Step 1 — Outer container (mask):**
- Rounded rectangle: X: 14.15". Width: 9.35". Height: 1.2"
- Border: 2 pt, `#3A4055` (Mid Slate)
- No fill (or transparent fill)
- Corner radius: 8 pt

**Step 2 — Three inner zone rectangles (no corner radius — the mask handles rounding):**

| Zone | X Start | Width | Fill | % of gauge |
|---|---|---|---|---|
| Green (Normal) | 14.15" | 5.61" | `#27AE60` Emerald | 60% |
| Amber (Warning) | 19.76" | 1.87" | `#E8A020` Amber | 20% |
| Coral (Discard) | 21.63" | 1.87" | `#E05C5C` Coral | 20% |

All three: Height 1.2", Y: 22.4".

**Step 3 — Boundary lines inside gauge:**
- Green/Amber boundary: Line at X: 19.76", from Y: 22.4" to Y: 23.6". Stroke: 2 pt, `#1A1F2E`
- Amber/Coral boundary: Line at X: 21.63", from Y: 22.4" to Y: 23.6". Stroke: 2 pt, `#1A1F2E`

**Step 4 — Zone labels INSIDE the bar:**
- Green zone: Text "NORMAL OPERATION" — Barlow Condensed ExtraBold, 16 pt, `#1A1F2E`. Centered in green rectangle.
- Amber zone: Text "WARNING" — Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`. Centered in amber rectangle.
- Coral zone: Text "DISCARD" — Barlow Condensed ExtraBold, 14 pt, `#F0EDE8`. Centered in coral rectangle.

**Step 5 — Tick mark labels BELOW the gauge:**
- Font: JetBrains Mono Regular, 14 pt, `#F0EDE8`
- Position: Y: 23.7" (below gauge bottom edge)
- `0 MTO` — left-aligned at X: 14.15"
- `6 MTO` — centered at X: 19.76" (Green/Amber boundary)
- `8 MTO` — centered at X: 21.63" (Amber/Coral boundary)
- `10 MTO` — right-aligned at X: 23.5"

**Step 6 — Secondary text indicators below boundaries:**
- Font: Inter Regular, 12 pt, `#F0EDE8` at 70% opacity
- Below `6 MTO`: "Monitor quality closely" — Y: 24.0"
- Below `8 MTO`: "Discard or dilute" — Y: 24.0"

**Step 7 — Group gauge elements:** Select outer container + three zone rectangles + boundary lines + all text → Group (Ctrl+G).

---

**"What is an MTO?" definition:**

Position: X: 14.15". Y: 24.3". Width: 9.35".

- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 140%
- Text:

> 1 MTO (metal turnover) = the bath has deposited an amount of nickel equal to its original Ni²⁺ charge. Fresh bath: 0 MTO. As MTOs accumulate, orthophosphite builds up, deposit quality declines, and corrosion resistance drops.

---

**Closing note (with Teal left accent):**

Position: Y: 25.3".

- Accent rectangle: X: 14.15". Width: 0.03" (2 pt). Height: 0.3". Fill: `#2EC4B6` (Teal)
- Text: X: 14.35" (right of accent + gap). Width: 9.15"
- Font: Inter Medium, 15 pt, `#2EC4B6`
- Text:

> Unlike electrolytic baths, EN baths have a finite life — track your MTOs or accept the consequences in deposit quality.

---

**Discard threshold reminder:**

Position: X: 14.15". Y: 25.7".

- Font: JetBrains Mono Regular, 14 pt, `#E05C5C` (Coral)
- Text:

> Discard at: > 120 g/L orthophosphite OR 8–10 MTO — whichever comes first.

---

**Group all Zone 4B elements after completion.**

---

### ZONE 5 — Applications + Specifications

**Dimensions:** Full width within margins. Y: 26.5" to 32.4" (~5.9" tall).

This zone is split into two columns:
- **Block G (Applications):** X: 0.5" to 14.8" (left 62% of 23.0" = 14.26", rounded to 14.3")
- **Block H (Specifications):** X: 15.05" to 23.5" (right 38% = 8.74", rounded to 8.45")
- Gutter: 0.25"

---

**BLOCK G — Industry Applications Grid**

**Section label:**
- Position: X: 0.5". Y: 26.7"
- Font: Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text:

> WHERE EN GOES TO WORK

**Icon grid: 3 columns x 2 rows**

Grid area: X: 0.5" to 14.8". Y: 27.2" to 32.0". Available: 14.3" wide x 4.8" tall.

Cell dimensions: Width: 4.6" each (14.3" / 3 = 4.77", with 0.1" gaps between = 4.57" per cell). Height: 2.3" each (4.8" / 2 = 2.4", with 0.1" gap = 2.3" per cell).

**Cell construction (build one, duplicate 5 times):**

Each cell is a rounded rectangle card:
- Fill: `#1E2435` (Dark Callout)
- Border: 1 pt, `#3A4055` (Mid Slate)
- Corner radius: 6 pt
- Internal padding: 10 pt

Inside each card, top to bottom:
1. **Icon** (icon library — line/outline style preferred): ~32x32 pt, color `#F0EDE8`, centered horizontally
2. **Industry name**: Barlow SemiBold, 16 pt, `#F0EDE8`, centered, 4 pt below icon
3. **Application note**: Inter Regular, 13 pt, `#F0EDE8` at 70% opacity, centered, 2 pt below name
4. **P-class tag**: JetBrains Mono Regular, 12 pt, colored per class (see table), centered, 4 pt below note

**Cell specifications (left to right, top row then bottom row):**

| Cell | Position | Icon Search | Industry | Application Note | P-Class Tag | Tag Color |
|---|---|---|---|---|---|---|
| 1 (top-left) | X: 0.5", Y: 27.2" | "airplane" | AEROSPACE | Hydraulic actuators, landing gear, fuel control valves | Mid-P — AMS 2404 | `#E8A020` Amber |
| 2 (top-center) | X: 5.2", Y: 27.2" | "circuit board" | ELECTRONICS / PCB | ENIG surface finish — solderable base + diffusion barrier | Low-P / Mid-P — IPC-4552B | `#2EC4B6` Teal |
| 3 (top-right) | X: 9.9", Y: 27.2" | "oil drill" or "derrick" | OIL AND GAS | Non-magnetic MWD tools; downhole pump components | High-P — non-magnetic | `#E05C5C` Coral |
| 4 (bottom-left) | X: 0.5", Y: 29.6" | "molecule" or "flask" | CHEMICAL PROCESSING | Pump impellers, reactor internals, acid-service components | High-P — 1,000+ hr salt spray | `#E05C5C` Coral |
| 5 (bottom-center) | X: 5.2", Y: 29.6" | "car engine" or "fuel" | AUTOMOTIVE | Fuel injectors, transmission components, ABS parts | Mid-P — wear + fuel compatibility | `#E8A020` Amber |
| 6 (bottom-right) | X: 9.9", Y: 29.6" | "medical cross" or "scalpel" | MEDICAL / MRI | Surgical instruments; MRI-compatible components | High-P (non-mag) / Low-P (hard) | `#E05C5C` / `#2EC4B6` (split — type both with respective colors) |

*Accessibility note: The P-class color tags match the column colors in the P% Spectrum table (Block D). The spelled-out text "Low-P / Mid-P / High-P" is the primary indicator — color is reinforcement only.*

---

**BLOCK H — Governing Specifications Card Stack**

**Section label:**
- Position: X: 15.05". Y: 26.7"
- Font: Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`
- Text:

> GOVERNING SPECIFICATIONS

**Spec cards: 5 stacked horizontal cards**

Card area: X: 15.05" to 23.5" (width: 8.45"). Y: 27.2" to 32.0". Available height: 4.8" for 5 cards = ~0.9" per card with 0.06" gaps.

**Card construction (build one, duplicate 4 times):**

Each card:
- Rounded rectangle: Width 8.45". Height: 0.85"
- Fill: `#1E2435` (Dark Callout)
- Left-border accent: Rectangle 0.06" wide (4 pt), full card height, flush left
- Corner radius: 4 pt
- Internal padding: 12 pt vertical, 14 pt horizontal (starting after left-border)

Inside each card:
- **Spec code**: JetBrains Mono Regular, 20 pt — positioned at left after left-border + padding
- **Description**: Inter Regular, 13 pt — positioned below spec code with 4 pt gap

| Card | Y Start | Left Border Color | Spec Code | Code Color | Description |
|---|---|---|---|---|---|
| 1 | 27.2" | `#2EC4B6` Teal | ASTM B733 | `#2EC4B6` | North American EN standard — Types by P%, Classes by heat treatment |
| 2 | 28.15" | `#E8A020` Amber | AMS 2404 | `#E8A020` | Aerospace EN (steel substrates) — includes pre/post bake requirements |
| 3 | 29.1" | `#E8A020` Amber | AMS 2405 | `#E8A020` | Aerospace EN (aluminum and magnesium) — zincate pre-treatment required |
| 4 | 30.05" | `#3A4055` Mid Slate | MIL-C-26074 | `#F0EDE8` | Military / legacy EN — broadly consistent with ASTM B733; appears on older defense drawings |
| 5 | 31.0" | `#2EC4B6` Teal | IPC-4552B | `#2EC4B6` | ENIG PCB surface finish — EN 3–6 µm (Mid-P), gold 0.05–0.10 µm |

Description text color: `#F0EDE8` at 70% opacity.

*Accessibility: Left-border color groups specs by domain (Teal = general/electronics; Amber = aerospace; Slate = military/legacy). Text labels fully describe each spec — color is grouping reinforcement only.*

---

**Group all Zone 5 elements after completion.**

---

### ZONE 6 — Footer Band

**Dimensions:** Full page width. Y: 32.4" to 36.0" (~3.6" tall).

---

**Disclaimer line (above the footer band fill):**

- Element type: Text box
- Position: Centered horizontally. Y: 32.5" (0.1" below Zone 5 boundary)
- Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster is a technical reference tool. Always consult your process supplier's documentation, applicable specifications, and safety data sheets. Deposit properties vary by formulation, substrate, and bath condition. Not a substitute for laboratory analysis or process qualification.

---

**Footer band background:**

- Element type: Rectangle
- Position: X: 0". Y: 33.2". Width: 24.0" (full bleed). Height: 2.8" (to page bottom)
- Fill: `#0D1020` (Deep Navy)
- No corner radius

---

**Footer content (inside the band):**

**Left — Poster title:**
- Position: X: 0.5". Y: 34.0" (vertically centered in band)
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> Electroless Nickel — Process Overview and Bath Control

**Center — Series name:**
- Position: Centered horizontally. Y: 34.0"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70% opacity
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Right — Logo placeholder:**
- Rectangle: X: 22.5". Y: 33.8". Width: 0.85" (60 pt). Height: 0.42" (30 pt)
- Fill: `#3A4055`
- Corner radius: 2 pt
- Inside: Text "LOGO" — JetBrains Mono Regular, 12 pt, `#F0EDE8`, centered

**Version number:**
- Position: X: 22.5". Y: 35.0" (below logo placeholder)
- Font: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50% opacity
- Text:

> v1.0 — 2026

---

**Group all Zone 6 elements after completion.**

---

## Part 5 — Build Sequence Summary

Build the poster in this exact order:

1. **Document setup** (Steps 1–5 from Part 2) — background color, fonts, brand colors, ruler guides
2. **Zone 2 — Uniform Coating Illustration** (build this first — it is the most visually complex element; build in isolation, group, then position)
3. **Zone 1 — Header Band** (headline, subheading, tagline, reaction callout)
4. **Zone 3 — P% Spectrum Table** (HERO data block — most time-consuming; build one row first, duplicate 9x)
5. **Zone 4A — Bath Control Parameters** (left column table + pH callout)
6. **Zone 4B — MTO Gauge** (right column gauge + definition text)
7. **Zone 5 — Applications + Specifications** (icon cards + spec cards)
8. **Zone 6 — Footer** (band + disclaimer + metadata)
9. **Final alignment check** — verify all zones align to ruler guides; scan for orphaned elements
10. **Light edition** — duplicate page, apply remap table from Part 6

---

## Part 6 — Light Edition Remap Table

After the Dark edition is complete, duplicate the entire design page . On the duplicate, manually remap every element's color using this table. Work from top to bottom — background first, then text, then fills, then accents.

**Important:** Do not remap `#C8D0D8` Bright Silver — the illustration deposit surfaces stay metallic in both editions.

| Element / Role | Dark Hex | Light Hex | Notes |
|---|---|---|---|
| Background (full artboard) | `#1A1F2E` | `#F5F4F0` | Page background fill |
| All primary text | `#F0EDE8` | `#1A1F2E` | Body, labels, headline, data values |
| Callout box fills | `#1E2435` | `#ECEEF4` | All callout boxes, icon cards, spec cards, row label column |
| Alternating table row fills | `#252B3D` | `#E8E8F0` | Even-numbered data rows |
| Footer band | `#0D1020` | `#1A1F2E` | Footer background rectangle |
| Amber accent | `#E8A020` | `#C8860A` | Section titles, Mid-P column header, MTO warning zone, Amber left-borders |
| Teal accent | `#2EC4B6` | `#1A8C82` | Callout borders/titles, Low-P column header, EN panel labels |
| Emerald accent | `#27AE60` | `#1E7A47` | MTO normal zone |
| Coral accent | `#E05C5C` | `#B83E3E` | High-P column header, critical callout border, Electrolytic panel labels |
| Table rules / Dividers | `#3A4055` | `#D0D4DE` | Table header fills, row rules, substrate shapes, spec card borders |
| Bright Silver deposits | `#C8D0D8` | `#C8D0D8` | **UNCHANGED** — always metallic |
| P% Low-P column header text | `#1A1F2E` on `#2EC4B6` | `#1A1F2E` on `#1A8C82` | Verify contrast: #1A1F2E on Teal Dark — passes AAA |
| P% Mid-P column header text | `#1A1F2E` on `#E8A020` | **`#F0EDE8` on `#C8860A`** | **TEXT COLOR OVERRIDE REQUIRED** — #1A1F2E on Amber Dark #C8860A is marginal for WCAG AA. Switch text to Warm White `#F0EDE8` in Light edition only. This is the ONLY element requiring a text-color override beyond the standard remap. |
| P% High-P column header text | `#F0EDE8` on `#E05C5C` | `#F0EDE8` on `#B83E3E` | Warm White on Deep Coral improves in Light edition — no concern |
| MTO gauge Amber zone label text | `#1A1F2E` on `#E8A020` | `#1A1F2E` on `#C8860A` | Check at build — may also need text override to `#F0EDE8`. Apply same fix as Mid-P header if contrast fails. |
| Sub-labels at 65–70% opacity | `#F0EDE8` at 65–70% | `#1A1F2E` at 65–70% | Evaluate — if 65% opacity text is too faint on `#F5F4F0`, increase to 75–80% |
| Footnote/disclaimer at 50–60% opacity | `#F0EDE8` at 50–60% | `#1A1F2E` at 50–60% | Evaluate — may need 65–70% on light background for legibility |

**Post-remap verification checklist:**
- [ ] Silver deposits `#C8D0D8` still read as metallic against `#F5F4F0` — they should
- [ ] Mid-P column header text overridden to `#F0EDE8` (NOT the standard `#1A1F2E` remap)
- [ ] MTO gauge Amber zone label text verified or overridden
- [ ] All body text passes WCAG AA (4.5:1 minimum) against its background
- [ ] Opacity-reduced text (tagline, sub-labels, footnotes, disclaimer) remains legible
- [ ] Substrate shapes (`#D0D4DE` Light Slate) still read as steel/metal against `#F5F4F0`
- [ ] Shield and magnet icons recolored to Light edition accent equivalents
- [ ] P-class tags in application cards recolored to Light edition accent equivalents

---

## Part 7 — Export Specifications

Configure these exports . Name files exactly as shown.

| File Name | Format | Size | Color Mode | Bleed |
|---|---|---|---|---|
| `Electroless Nickel — Dark — 24x36 — Print.pdf` | PDF (Print) | 24x36" | CMYK | Yes (0.125") |
| `Electroless Nickel — Dark — 18x24 — Print.pdf` | PDF (Print) | 18x24" | CMYK | Yes (0.125") |
| `Electroless Nickel — Dark — Digital.pdf` | PDF (Digital) | 24x36" | RGB | No |
| `Electroless Nickel — Light — 24x36 — Print.pdf` | PDF (Print) | 24x36" | CMYK | Yes (0.125") |
| `Electroless Nickel — Light — 18x24 — Print.pdf` | PDF (Print) | 18x24" | CMYK | Yes (0.125") |
| `Electroless Nickel — Light — Digital.pdf` | PDF (Digital) | 24x36" | RGB | No |

*Six export files per poster — series standard.*

*print export: use the tool's "Print Bleed" PDF export option, which adds bleed and crop marks automatically. For digital PDFs, use standard PDF export without bleed.*

*18x24" version: duplicate the 24x36" design, resize to 18x24". Accept auto-resize, then verify all text meets the 14 pt minimum floor (scale at ~75%).*

---

## Part 8 — Notes for Elara

The following items are judgment calls that Elara should work into the generation prompt with explicit instructions for Drew, rather than leaving them to interpretation at build time.

1. **Font upload first.** Before anything else, verify JetBrains Mono is available. If not, instruct Drew to substitute Courier Prime and flag the substitution. All four fonts must be confirmed before placing any content.

2. **Build the illustration first.** The Uniform Coating cross-section (Zone 2) is the most visually complex element. Instruct Drew to build it in isolation — all substrate rectangles, deposit rectangles, arrows, labels, and the central callout banner — then group everything before positioning it in the layout. This prevents accidental displacement.

3. **P% Spectrum table efficiency.** The 10-row table is the most time-consuming element. Instruct Drew to build one complete row (row label background + data cell backgrounds + left-border accent + 4 text boxes) and then duplicate it 9 times. Change content, fill colors, and border colors on each duplicate. This is dramatically faster than building each row from scratch.

4. **MTO gauge layering.** Build the three colored zone rectangles first, then the outer rounded container on top. If the clip-mask is inconsistent, build as three separate rectangles with manually adjusted corner radii on the end pieces only (8 pt radius on the left side of the green zone rectangle, 8 pt on the right side of the coral zone rectangle, 0 pt on all other corners).

5. **Group each zone after completion.** After finishing each of the six zones, Drew should select all elements in that zone and group them (Ctrl+G / Cmd+G). This prevents accidental element displacement while working on adjacent zones. The illustration (Zone 2) should be grouped before being positioned.

6. **Snap-to-guides.** Instruct Drew to set guides at the positions specified in Part 2, Step 5. These guides define the zone boundaries and ensure clean alignment.

7. **Chemical formula characters.** All chemical formulas in this document use Unicode subscript/superscript characters (Ni²⁺, H₂PO₂⁻, H₂O, Cr⁶⁺, H₂SO₄, NaOH, NH₄OH). Instruct Drew to copy-paste these directly from this document — do not attempt to type them manually. Unicode characters render correctly.

8. **Shield and magnet icons in the P% table.** These are secondary indicators — if exact icon matches are not available in the library, simple alternatives work fine. A circle for the shield, a U-shape for the magnet. The text values and labels carry the primary data. Do not spend excessive time searching for perfect icons.

9. **Light edition — Mid-P header text override.** This is the single most important Light edition note. The standard remap changes all `#1A1F2E` text to `#1A1F2E` (no change needed since it was already dark text on the amber header). But in the Light edition, the Amber background becomes `#C8860A` (darker), and the contrast with `#1A1F2E` text may fail WCAG AA. Override the text color in this specific cell to `#F0EDE8` (Warm White). Apply the same fix to the MTO gauge Amber zone label if contrast fails there as well.

10. **Logo placeholder.** Until the Plating Posters Inc logo is finalized, the filled rectangle with "LOGO" text in the footer is the approved placeholder. Do not design around a logo that does not yet exist.

---

## Part 9 — Asset Summary Report for June

**Asset Name:** Poster #10 — Electroless Nickel — Process Overview and Bath Control — Construction Workup

**Version:** v1.0

**Date:** 2026-04-03

**Files produced this session:**

| File | Location | Status |
|---|---|---|
| `Poster 10 — Electroless Nickel — Construction Workup.md` | `Plating Posters Inc/` | Complete — ready for Elara |

**Prior files this workup depends on:**

| File | Status |
|---|---|
| `Poster 10 — Electroless Nickel — Content and Layout Draft.md` (v1.0) | All Watson flags cleared — production-ready |
| Watson Research Brief v2 — Electroless Nickel (2026-03-21) | Complete — at `Research Briefs/Electroless Nickel — Alaina Research Brief.md` |

**Current Poster #10 status:** Construction Workup v1.0 complete. All content finalized. Ready for Elara to engineer the generation prompt.

**Recommended next steps:**

1. **Elara:** Receive this workup document. Engineer a detailed, step-by-step generation prompt for Drew that translates Parts 3–4 of this document into precise generation instructions. Address all 10 items in Part 8 (Notes for Elara) explicitly. Confirm JetBrains Mono font strategy before issuing the prompt.

2. **Drew:** Confirm Pro tier is active (required for font upload). Once the generation prompt from Elara is in hand, build the Dark edition first, then Light edition as a duplicate per Part 6.

3. **Tyler (evenings/weekends — not blocking):** No blocking items. Tyler may be consulted in a future session to validate the heat treatment hardness values and salt spray hours if Drew requests additional confidence before the first commercial print run.

4. **June:** Update Poster #10 status in project tracking to "Construction Workup v1.0 — Ready for Elara." Update the master note at `Plating Posters Inc/Plating Posters Inc.md`.

5. **Alaina (next session):** Update `project_poster_library.md` memory file. Assess which next poster in the library is ready to advance — potential candidates include Poster #1 (Surface Preparation), Poster #3 (Acid vs. Alkaline Zinc), or Poster #7 (Metallic Contamination).

---

*Alaina — Plating Posters Inc Creative Lead*
*Construction Workup v1.0 — 2026-04-03*
*Technical source: Watson, Electroless Nickel — Alaina Research Brief v2 (2026-03-21). All Watson flags cleared.*
*This document is the design-optimized translation of Content and Layout Draft v1.0.*
*Intended recipient: Elara — for the design construction prompt engineering.*
