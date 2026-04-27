---
Project: Plating Posters Inc
Poster Number: 2
Title: "The Electroplating Process — Step by Step"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 2 — The Electroplating Process — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — The Electroplating Process Research Brief v1 (2026-04-03)
Watson Flags: TWO — ion migration conventions + soluble vs. insoluble anode presentation (both Drew, non-blocking)
Process Scope: General electroplating — the foundational "how it works" poster
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroplating
  - ConstructionWorkup
  - Foundational
---

# Poster # Poster #2 — Construction Workup
## The Electroplating Process — Step by Step

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #2. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. Two Watson flags remain open but are non-blocking — standard electrochemistry conventions.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 2 — The Electroplating Process — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for table rows, callout boxes, accent borders, panel cards, and illustration components
- Line elements with arrowheads for ion flow and electron flow arrows in the cell diagram
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for electrolyte/cathode/anode/rectifier icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Electroplating cell illustration (HERO):** Complex freeform vector illustration requires geometric shape composites. The tank cross-section must be built as a composite of geometric shapes — large rounded rectangle for the tank, vertical rectangles for anode and cathode, smaller rectangles for the rectifier and deposit layer, lines with arrowheads for ion flow and electron flow, and text labels for all elements. **Recommendation: build as layered geometric shapes.** This approach was validated on Posters #4, #10, and #13.

2. **Ion flow arrows inside the tank:** Use line element with arrowhead. Place 3-4 horizontal arrow lines from the anode side toward the cathode side in Teal. Place 2-3 lighter arrows in the opposite direction at reduced opacity. This is straightforward.

3. **Electron flow arrows (external circuit):** Use line elements with arrowheads in Coral, routed along the bus bars between rectifier and electrodes. These are straight lines — no curves needed.

4. **Electrolyte fill:** Represent the solution inside the tank with a rectangle fill at 30% opacity in Teal, or 2-3 horizontal wavy-style lines in Teal at 20% opacity. the line element works; alternatively, search for a "wave" graphic element at low opacity.

5. **Four Essentials panel strip (Zone 3):** Four rounded rectangles with colored top accent bars. Straightforward in the design — build each panel as a grouped set of shapes and text boxes.

6. **4 pt left-border accents on callout boxes:** Same technique as previous posters — simulate with a narrow colored rectangle (approximately 0.06" wide) positioned flush against the left edge.

7. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Producing the Light edition requires duplicating the design page and manually recoloring every element per the remap table in Part 6.

8. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** If unavailable, substitute **Courier Prime**. Flag substitution visibly.

9. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation. For 18x24", duplicate and resize; verify all text meets the 14 pt minimum floor.

10. **Sub/superscript characters:** The tool does not natively support subscript/superscript formatting. For chemical formulas (M²⁺, M⁰, e⁻, SO₄²⁻, Cl⁻, H₂), type the Unicode subscript/superscript characters directly. These are provided verbatim in the copy blocks below — copy-paste them exactly.

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
- **JetBrains Mono Regular** — all parameter/data table values, chemical formulas, and equations

If JetBrains Mono upload fails, substitute **Courier Prime** for all JetBrains Mono specifications below.

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Subheading, anode elements, "Soluble Anodes" accent |
| Teal | `#2EC4B6` | Callout borders/titles, ion flow arrows, "Insoluble Anodes" accent |
| Emerald | `#27AE60` | Cathode/deposit elements, cathode panel |
| Coral | `#E05C5C` | Electron flow arrows, rectifier panel, defect callout |
| Mid Slate | `#3A4055` | Table header fills, tank outline, bus bars, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, panel card fills |
| Alt Row | `#252B3D` | Alternating table rows, rectifier fill |
| Bright Silver | `#C8D0D8` | Deposit layer on cathode |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 16.2" — Zone 2/Zone 3 boundary
- 20.9" — Zone 3/Zone 4 boundary
- 25.9" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it** to prevent accidental displacement while working on adjacent zones.

```
ZONE 1 — HEADER BAND (top 0"–2.9")
  Block A: Headline + subheading + tagline (left ~60%)
  Block B: "The Core Reaction" callout box (right ~40%)

ZONE 2 — THE ELECTROPLATING CELL (HERO) (2.9"–16.2" / ~13.3" tall)
  Block C: Large labeled tank cross-section with rectifier, anode, cathode,
           electrolyte, ion flow arrows, electron flow arrows, reaction labels

ZONE 3 — THE FOUR ESSENTIALS STRIP (16.2"–20.9" / ~4.7" tall)
  Block D: 4 equal panels — Electrolyte | Cathode | Anode | Rectifier

ZONE 4 — SOLUBLE vs. INSOLUBLE ANODES (20.9"–25.9" / ~5.0" tall)
  Block E: Two-column comparison — soluble (left) vs. insoluble (right)

ZONE 5 — PROCESS VARIABLES + DEFECT STRIP (25.9"–32.4" / ~6.5" tall)
  Block F: Key process variables table (left 55%)
  Block G: Common defects callout (right 45%)

ZONE 6 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block H: Disclaimer + poster title + series name + logo + version
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
- Width: 13.5" (approximately 59% of artboard width — leaves room for Block B at right)
- Font: Barlow Condensed ExtraBold
- Size: 96 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> THE ELECTROPLATING PROCESS

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.6")
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 40 pt
- Color: `#E8A020` (Amber)
- Text:

> Step by Step

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 13.5"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65% (transparency slider on the text element — set to 65)
- Text:

> Metal ions in. Solid metal out. That's plating.

---

**BLOCK B — "The Core Reaction" Callout Box**

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 14.25". Y: 0.5"
- Width: 9.25" (extends to X: 23.5", flush with right safe zone guide)
- Height: 2.2" (sized to fit all content with 20 pt internal padding)
- Fill color: `#1E2435` (Dark Callout)
- Border (stroke): 1.5 pt, color `#2EC4B6` (Teal)
- Corner radius: 8 pt

**Callout title:**
- Element type: Text box inside the container
- Position: X: 14.55" (container left + 20 pt padding). Y: 0.7"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#2EC4B6` (Teal)
- Text:

> THE CORE REACTION

**Reaction equation:**
- Element type: Text box inside the container
- Position: X: centered horizontally within container. Y: 1.05"
- Width: 8.85"
- Font: JetBrains Mono Regular
- Size: 24 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text (copy-paste Unicode exactly):

> M²⁺ + 2e⁻ → M⁰

**Translation text:**
- Element type: Text box inside the container
- Position: X: 14.55". Y: 1.45"
- Width: 8.85"
- Font: Inter Regular
- Size: 17 pt
- Color: `#F0EDE8`
- Line height: 140% (spacing: 1.4)
- Text:

> Metal ions in solution gain electrons at the cathode surface and become solid metal atoms. That's electroplating — one atom at a time.

**Closing label:**
- Element type: Text box inside the container
- Position: X: 14.55". Y: 2.15"
- Font: Inter Medium
- Size: 16 pt
- Color: `#2EC4B6`
- Text:

> Over 30 distinct electroplating processes use this reaction.

---

### ZONE 2 — The Electroplating Cell (HERO)

**Dimensions:** Full page width. Y: 2.9" to 16.2" (13.3" tall).
**Background:** Same as page — no separate fill.

---

**Section label:**
- Element type: Text box
- Position: X: centered. Y: 3.1"
- Font: Barlow Condensed ExtraBold
- Size: 30 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE ELECTROPLATING CELL

---

**BLOCK C — Tank Cross-Section Illustration**

This is the poster's centerpiece. Build all elements in this order, bottom to top (back to front in the tool's layer stack).

**C1 — Plating tank (container):**
- Element type: Rounded rectangle
- Position: X: 2.0". Y: 4.2"
- Width: 20.0"
- Height: 9.0"
- Fill: `#1E2435` (Dark Callout)
- Border: 3 pt, `#3A4055` (Mid Slate)
- Corner radius: 6 pt

**C2 — Electrolyte fill (inside tank):**
- Element type: Rectangle
- Position: X: 2.15". Y: 5.2" (below bus bar level, showing solution starts below surface)
- Width: 19.7"
- Height: 7.85" (fills to near bottom of tank)
- Fill: `#2EC4B6` (Teal) at **15% opacity**
- No border

**C3 — Electrolyte surface line:**
- Element type: Line
- Position: from (X: 2.15", Y: 5.2") to (X: 21.85", Y: 5.2")
- Stroke: 1.5 pt, `#2EC4B6` at 40% opacity
- Style: dashed (if The tool supports; otherwise solid)

**C4 — Rectifier (above tank):**
- Element type: Rounded rectangle
- Position: X: 10.0" (centered). Y: 3.5"
- Width: 4.0"
- Height: 1.2"
- Fill: `#252B3D` (Alt Row)
- Border: 1.5 pt, `#3A4055`
- Corner radius: 6 pt

**C4a — Rectifier label:**
- Element type: Text box
- Position: centered within rectifier rectangle
- Font: Barlow SemiBold, 18 pt
- Color: `#F0EDE8`
- Text:

> DC RECTIFIER

**C4b — Terminal labels:**
- Element type: Two text boxes, positioned at left and right edges of rectifier
- Left terminal: X: 10.2". Font: JetBrains Mono, 16 pt. Color: `#F0EDE8`. Text: `(-)`
- Right terminal: X: 13.5". Font: JetBrains Mono, 16 pt. Color: `#F0EDE8`. Text: `(+)`

**C5 — Bus bar (cathode side — left):**
- Element type: Line
- From: (X: 10.2", Y: 4.7") — bottom of rectifier left terminal
- To: (X: 6.5", Y: 4.7") then down to (X: 6.5", Y: 5.0") — into the tank
- Use two line segments: horizontal from rectifier to above cathode, then vertical down into tank
- Stroke: 2 pt, `#3A4055`

**C6 — Bus bar (anode side — right):**
- Element type: Line
- From: (X: 13.8", Y: 4.7") — bottom of rectifier right terminal
- To: (X: 17.5", Y: 4.7") then down to (X: 17.5", Y: 5.0") — into the tank
- Same two-segment construction
- Stroke: 2 pt, `#3A4055`

**C7 — Cathode (the part — left side of tank):**
- Element type: Rectangle
- Position: X: 5.5". Y: 5.5"
- Width: 2.0"
- Height: 6.5"
- Fill: `#27AE60` (Emerald)
- Corner radius: 2 pt

**C7a — Deposit layer (on cathode face nearest anode):**
- Element type: Rectangle
- Position: X: 7.5" (flush against right face of cathode). Y: 5.5"
- Width: 0.3"
- Height: 6.5"
- Fill: `#C8D0D8` (Bright Silver)
- No border

**C7b — Cathode label:**
- Element type: Text box
- Position: X: 5.0". Y: 4.9" (above the cathode, inside tank)
- Font: Barlow SemiBold, 16 pt
- Color: `#27AE60`
- Text:

> CATHODE (Part)

**C7c — Cathode sub-label:**
- Element type: Text box
- Position: X: 5.0". Y: 5.2"
- Font: JetBrains Mono Regular, 12 pt
- Color: `#F0EDE8` at 70% opacity
- Text:

> Connected to (-) terminal

**C7d — Cathode reaction label:**
- Element type: Text box
- Position: X: 3.0". Y: 8.5" (to the left of the cathode)
- Font: JetBrains Mono Regular, 14 pt
- Color: `#27AE60`
- Text:

> M²⁺ + 2e⁻ → M⁰

**C7e — Cathode reaction sub-label:**
- Element type: Text box
- Position: X: 3.0". Y: 9.0"
- Font: Inter Regular, 12 pt
- Color: `#27AE60`
- Text:

> Metal deposits here

**C8 — Anode (right side of tank):**
- Element type: Rectangle
- Position: X: 16.5". Y: 5.5"
- Width: 2.0"
- Height: 6.5"
- Fill: `#E8A020` (Amber)
- Corner radius: 2 pt

**C8a — Anode label:**
- Element type: Text box
- Position: X: 16.0". Y: 4.9"
- Font: Barlow SemiBold, 16 pt
- Color: `#E8A020`
- Text:

> ANODE (Metal)

**C8b — Anode sub-label:**
- Element type: Text box
- Position: X: 16.0". Y: 5.2"
- Font: JetBrains Mono Regular, 12 pt
- Color: `#F0EDE8` at 70% opacity
- Text:

> Connected to (+) terminal

**C8c — Dissolution arrows (from anode into solution):**
- Element type: 4 line elements with arrowheads
- Starting points: spaced vertically along the anode's left face (X: 16.5"), at Y: 6.5", 7.5", 8.5", 9.5"
- Ending points: approximately 1.0" to the left of each starting point (X: 15.5")
- Stroke: 1.5 pt, `#E8A020`
- Arrowhead: at the left end (pointing away from anode)

**C8d — Dissolution label (near arrows):**
- Element type: Text box
- Position: X: 14.5". Y: 7.5"
- Font: JetBrains Mono Regular, 12 pt
- Color: `#E8A020`
- Text:

> M²⁺

**C8e — Anode reaction label:**
- Element type: Text box
- Position: X: 19.0". Y: 8.5" (to the right of the anode)
- Font: JetBrains Mono Regular, 14 pt
- Color: `#E8A020`
- Text:

> M⁰ → M²⁺ + 2e⁻

**C8f — Anode reaction sub-label:**
- Element type: Text box
- Position: X: 19.0". Y: 9.0"
- Font: Inter Regular, 12 pt
- Color: `#E8A020`
- Text:

> Metal dissolves here

**C9 — Ion flow arrows (cations — anode to cathode, through solution):**
- Element type: 4 line elements with arrowheads
- Starting X: approximately 15.0" (near anode dissolution arrows)
- Ending X: approximately 8.5" (near cathode deposit face)
- Y positions: 6.8", 7.8", 8.8", 9.8" (staggered vertically within the electrolyte)
- Stroke: 2 pt, `#2EC4B6` (Teal)
- Arrowhead: at the LEFT end (pointing toward cathode)

**C9a — Cation flow label:**
- Element type: Text box
- Position: X: 10.5" (centered between electrodes). Y: 6.3"
- Font: Inter Regular, 13 pt
- Color: `#2EC4B6`
- Text:

> Cations (M²⁺) → toward cathode

**C10 — Ion flow arrows (anions — cathode to anode, through solution):**
- Element type: 3 line elements with arrowheads
- Starting X: approximately 9.0"
- Ending X: approximately 14.0"
- Y positions: 10.5", 11.0", 11.5"
- Stroke: 1.5 pt, `#2EC4B6` at **50% opacity**
- Arrowhead: at the RIGHT end (pointing toward anode)

**C10a — Anion flow label:**
- Element type: Text box
- Position: X: 10.0". Y: 11.8"
- Font: Inter Regular, 12 pt
- Color: `#2EC4B6` at 60% opacity
- Text:

> Anions (SO₄²⁻, Cl⁻) → toward anode

**C11 — Electron flow arrows (external circuit — cathode side):**
- Element type: 2 line elements with arrowheads
- Arrow 1: Along left bus bar from rectifier (-) terminal DOWN to cathode connection point
  - From (X: 6.5", Y: 4.7") to (X: 6.5", Y: 5.0")
  - Place a second arrow along the horizontal segment pointing left toward cathode
- Stroke: 1.5 pt, `#E05C5C` (Coral)
- Arrowhead: pointing toward cathode (downward)

**C12 — Electron flow arrows (external circuit — anode side):**
- Element type: 2 line elements with arrowheads
- Arrow along right bus bar from anode connection point UP to rectifier (+) terminal
  - From (X: 17.5", Y: 5.0") to (X: 17.5", Y: 4.7")
- Stroke: 1.5 pt, `#E05C5C`
- Arrowhead: pointing toward rectifier (upward)

**C13 — Electron flow label:**
- Element type: Text box
- Position: X: 8.5". Y: 3.8" (near rectifier, above the bus bars)
- Font: JetBrains Mono Regular, 12 pt
- Color: `#E05C5C`
- Text:

> Electron flow (e⁻)

**C14 — Key simplification banner (below the tank):**
- Element type: Text box
- Position: X: centered. Y: 13.8" (below tank bottom)
- Width: 20.0"
- Font: Inter Medium, 18 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> Metal ions travel through the solution toward the part. When they arrive, they pick up electrons and become solid metal.

---

### ZONE 3 — The Four Essentials Strip

**Dimensions:** Full page width. Y: 16.2" to 20.9" (4.7" tall).
**Background:** Same as page — no separate fill.

---

**Section label:**
- Element type: Text box
- Position: X: centered. Y: 16.4"
- Font: Barlow Condensed ExtraBold, 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> EVERY ELECTROPLATING SYSTEM REQUIRES FOUR THINGS

---

**BLOCK D — Four panels, side by side**

**Panel dimensions and positions:**
- Each panel: 5.375" wide x 3.5" tall (4 panels + 3 gutters of 0.2" = 23.0" total = fits within safe zone)
- Panel 1: X: 0.5". Y: 17.0"
- Panel 2: X: 6.075". Y: 17.0"
- Panel 3: X: 11.65". Y: 17.0"
- Panel 4: X: 17.225". Y: 17.0"

**Panel template (repeat for all 4 — substitute accent color, icon, title, and body per panel):**

*Panel container:*
- Element type: Rounded rectangle
- Width: 5.375". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt
- No border

*Top accent bar:*
- Element type: Rectangle
- Position: flush with top of panel container (same X, same Y)
- Width: 5.375". Height: 0.3"
- Fill: panel accent color
- Corner radius: top-left and top-right 6 pt, bottom 0 pt (clip to container if needed)

*Icon:*
- Element type: icon search (see icon search term per panel below)
- Position: centered horizontally in panel. Y: panel top + 0.5"
- Size: 0.6" x 0.6"
- Color: panel accent color

*Panel title:*
- Element type: Text box
- Position: centered horizontally. Y: below icon + 0.15" gap
- Font: Barlow SemiBold, 20 pt
- Color: panel accent color
- Alignment: Center

*Panel body:*
- Element type: Text box
- Position: X: panel left + 0.25" padding. Y: below title + 0.1" gap
- Width: 4.875" (panel width minus 0.5" total horizontal padding)
- Font: Inter Regular, 16 pt
- Color: `#F0EDE8`
- Alignment: Center
- Line height: 140%

---

**Panel 1 — Electrolyte** (Teal `#2EC4B6` accent):
- Icon search: "beaker" or "flask" or "droplet"
- Title: `ELECTROLYTE`
- Body: `The solution — dissolved metal ions, supporting salts, and additives. The medium through which current flows as ions.`

**Panel 2 — Cathode** (Emerald `#27AE60` accent):
- Icon search: "cube" or "layers"
- Title: `CATHODE`
- Body: `The part being plated. Connected to the (-) terminal. Metal ions arrive here, gain electrons, and become solid metal. Cathode = coating.`

**Panel 3 — Anode** (Amber `#E8A020` accent):
- Icon search: "arrow up" or "dissolve" or "mining"
- Title: `ANODE`
- Body: `The counterelectrode. Connected to the (+) terminal. Soluble anodes dissolve to replenish the bath. Insoluble anodes conduct current only.`

**Panel 4 — Rectifier** (Coral `#E05C5C` accent):
- Icon search: "lightning" or "power" or "battery"
- Title: `RECTIFIER`
- Body: `The DC power supply. Converts AC line power to direct current. Controls amperage (deposition rate) and voltage. Typical range: 3-12 V.`

---

### ZONE 4 — Soluble vs. Insoluble Anodes

**Dimensions:** Full page width. Y: 20.9" to 25.9" (5.0" tall).
**Background:** Same as page — no separate fill.

---

**Section label:**
- Element type: Text box
- Position: X: centered. Y: 21.1"
- Font: Barlow Condensed ExtraBold, 26 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> TWO ANODE SYSTEMS — ONE PRINCIPLE

---

**BLOCK E — Two-column comparison**

**Column dimensions:**
- Left column (Soluble): X: 0.5". Width: 11.1" (gutter at 11.6")
- Right column (Insoluble): X: 11.9". Width: 11.1" (to 23.0")
- Both columns: Y: 21.7". Height: 3.8"

---

**Left column — "Soluble Anodes"**

*Container:*
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 21.7"
- Width: 11.1". Height: 3.8"
- Fill: `#1E2435`
- Corner radius: 6 pt
- No full border

*Left accent bar:*
- Element type: Rectangle
- Position: X: 0.5". Y: 21.7"
- Width: 0.06" (4 pt equivalent). Height: 3.8"
- Fill: `#E8A020` (Amber)

*Title:*
- Element type: Text box
- Position: X: 0.85". Y: 21.9"
- Font: Barlow SemiBold, 20 pt
- Color: `#E8A020`
- Text:

> SOLUBLE ANODES

*Equation:*
- Element type: Text box
- Position: X: 0.85". Y: 22.35"
- Font: JetBrains Mono Regular, 16 pt
- Color: `#F0EDE8`
- Text:

> M⁰ (anode) → M²⁺ (solution) → M⁰ (deposit)

*Body:*
- Element type: Text box
- Position: X: 0.85". Y: 22.8"
- Width: 10.5"
- Font: Inter Regular, 16 pt
- Color: `#F0EDE8`
- Line height: 140%
- Text:

> The anode dissolves, releasing metal ions into solution. The cathode consumes those ions as deposit. The bath is self-replenishing — metal concentration stays stable.

*Process examples:*
- Element type: Text box
- Position: X: 0.85". Y: 23.8"
- Font: JetBrains Mono Regular, 14 pt
- Color: `#F0EDE8` at 80% opacity
- Text:

> Acid copper (Cu-P) | Watts nickel (R-Rounds)
> Silver (Ag) | Tin (Sn) | Acid zinc (Zn)

*Principle line:*
- Element type: Text box
- Position: X: 0.85". Y: 24.5"
- Font: Inter Medium, 16 pt
- Color: `#E8A020`
- Text:

> What the anode gives up, the cathode builds.

---

**Right column — "Insoluble Anodes"**

*Container:*
- Element type: Rounded rectangle
- Position: X: 11.9". Y: 21.7"
- Width: 11.1". Height: 3.8"
- Fill: `#1E2435`
- Corner radius: 6 pt

*Left accent bar:*
- Element type: Rectangle
- Position: X: 11.9". Y: 21.7"
- Width: 0.06". Height: 3.8"
- Fill: `#2EC4B6` (Teal)

*Title:*
- Element type: Text box
- Position: X: 12.25". Y: 21.9"
- Font: Barlow SemiBold, 20 pt
- Color: `#2EC4B6`
- Text:

> INSOLUBLE ANODES

*Equation:*
- Element type: Text box
- Position: X: 12.25". Y: 22.35"
- Font: JetBrains Mono Regular, 16 pt
- Color: `#F0EDE8`
- Text:

> Anode conducts current only → no dissolution

*Body:*
- Element type: Text box
- Position: X: 12.25". Y: 22.8"
- Width: 10.5"
- Font: Inter Regular, 16 pt
- Color: `#F0EDE8`
- Line height: 140%
- Text:

> The anode does not dissolve. Metal ions are consumed at the cathode, depleting the bath. The operator must analyze and add metal salts to maintain concentration.

*Process examples:*
- Element type: Text box
- Position: X: 12.25". Y: 23.8"
- Font: JetBrains Mono Regular, 14 pt
- Color: `#F0EDE8` at 80% opacity
- Text:

> Hard chrome (Pb-Sn alloy) | Alk. zinc (steel)
> Trivalent chrome (carbon)

*Principle line:*
- Element type: Text box
- Position: X: 12.25". Y: 24.5"
- Font: Inter Medium, 16 pt
- Color: `#2EC4B6`
- Text:

> Operator adds chemistry. The anode just conducts.

---

### ZONE 5 — Process Variables + Defect Strip

**Dimensions:** Full page width. Y: 25.9" to 32.4" (6.5" tall).
**Background:** Same as page — no separate fill.

---

**BLOCK F — Key Process Variables Table (left 55%)**

**Position:** X: 0.5". Y: 25.9". Width: 12.5". Height: 6.2".

**Section label:**
- Element type: Text box
- Position: X: 0.5". Y: 26.1"
- Font: Barlow Condensed ExtraBold, 24 pt
- Color: `#F0EDE8`
- Text:

> WHAT THE OPERATOR CONTROLS

**Table construction:**

*Column header row:*
- Element type: Rectangle
- Position: X: 0.5". Y: 26.6"
- Width: 12.5". Height: 0.45"
- Fill: `#3A4055` (Mid Slate)

*Column header labels (3 text boxes across the header row):*
- Col 1: X: 0.7". Text: `Variable`. Width: 3.0". Font: Barlow SemiBold, 18 pt. Color: `#F0EDE8`
- Col 2: X: 3.7". Text: `What It Affects`. Width: 5.0". Font: Barlow SemiBold, 18 pt. Color: `#F0EDE8`
- Col 3: X: 8.7". Text: `How It's Controlled`. Width: 4.3". Font: Barlow SemiBold, 18 pt. Color: `#F0EDE8`

*Data rows (7 rows, each 0.55" tall, alternating fills):*

Row Y positions starting at 27.05", incrementing by 0.55":
- Row 1: Y: 27.05" — fill `#1A1F2E`
- Row 2: Y: 27.60" — fill `#252B3D`
- Row 3: Y: 28.15" — fill `#1A1F2E`
- Row 4: Y: 28.70" — fill `#252B3D`
- Row 5: Y: 29.25" — fill `#1A1F2E`
- Row 6: Y: 29.80" — fill `#252B3D`
- Row 7: Y: 30.35" — fill `#1A1F2E`

Each row: Rectangle at (X: 0.5", Y: row Y), Width: 12.5", Height: 0.55".

*Row data (3 text boxes per row at column X positions):*

| Row | Variable (Inter Medium, 16 pt) | What It Affects (Inter Regular, 15 pt) | How It's Controlled (Inter Regular, 15 pt) |
|-----|------|------|------|
| 1 | Current density (ASF) | Deposition rate, deposit quality | Rectifier amperage + surface area |
| 2 | Temperature | Bath conductivity, brightener activity | Heaters, chillers, thermostats |
| 3 | Time | Deposit thickness | Timer or operator judgment |
| 4 | Agitation | Uniformity, limiting CD | Air sparging, mechanical movement |
| 5 | Bath chemistry | Deposit properties, throwing power | Analysis + chemical additions |
| 6 | pH | Stress, brightness, efficiency | Acid or alkali additions |
| 7 | Filtration | Smoothness, particle freedom | Filter pump, carbon treatment |

All text color: `#F0EDE8`. Vertically center text within each row.

---

**BLOCK G — Common Defects Quick Reference (right 45%)**

**Position:** X: 13.25". Y: 25.9". Width: 10.25". Height: 6.2".

**Section label:**
- Element type: Text box
- Position: X: 13.25". Y: 26.1"
- Font: Barlow Condensed ExtraBold, 24 pt
- Color: `#F0EDE8`
- Text:

> WHEN SOMETHING GOES WRONG

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 13.25". Y: 26.6"
- Width: 10.25". Height: 5.2"
- Fill: `#1E2435`
- Border: 1.5 pt, `#E05C5C` (Coral)
- Corner radius: 8 pt

**Defect rows (7 rows, each 0.6" tall, inside the callout):**

Each row construction:
- Left accent: Rectangle, 0.06" wide, `#E05C5C`, flush against inner left edge of callout
- Defect name: Text box, X: callout left + 0.25". Font: Inter Medium, 15 pt. Color: `#E05C5C`
- Parenthetical: appended to defect name in same text box. Color: `#F0EDE8` at 70%
- Cause: Text box, X: callout left + 0.25". Below defect name. Font: Inter Regular, 14 pt. Color: `#F0EDE8`

Row Y positions starting at 26.8", incrementing by 0.6":

| Row | Defect Name | Parenthetical | Cause |
|-----|------------|---------------|-------|
| 1 | Burning | (dark, rough at edges) | Current density too high (HCD) |
| 2 | Skip plating | (bare spots) | CD too low; poor cleaning (LCD) |
| 3 | Pitting | (random pinholes) | H₂ gas adhesion; organics |
| 4 | Peeling | (adhesion failure) | Surface prep failure |
| 5 | Dullness | (matte finish) | Brightener depletion; low temp |
| 6 | Roughness | (gritty surface) | Particles; metallic contamination |
| 7 | Streaking | (vertical lines) | Inadequate rinsing; drag-in |

**Footer note:**
- Element type: Text box
- Position: X: 13.5". Y: 31.2" (below last defect row)
- Font: Inter Regular, 13 pt
- Color: `#F0EDE8` at 60% opacity
- Style: italic
- Text:

> See Poster #1 (Surface Preparation) and Poster #7 (Metallic Contamination) for detailed troubleshooting.

---

### ZONE 6 — Footer Band

**Dimensions:** Full page width. Y: 32.4" to 36.0" (3.6" tall).

**Footer band background:**
- Element type: Rectangle
- Position: X: 0". Y: 32.4"
- Width: 24.0". Height: 3.6"
- Fill: `#0D1020` (Deep Navy)

**Disclaimer:**
- Element type: Text box
- Position: X: 0.5". Y: 32.8"
- Width: 23.0"
- Font: Inter Regular, 11 pt
- Color: `#F0EDE8` at 50% opacity
- Alignment: Center
- Text:

> This poster is a conceptual reference. Specific operating parameters vary by process and product formulation. Consult your process supplier for application-specific guidance.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt
- Color: `#F0EDE8`
- Text:

> The Electroplating Process — Step by Step

**Series name:**
- Element type: Text box
- Position: X: 0.5". Y: 34.0"
- Font: Inter Regular, 13 pt
- Color: `#F0EDE8` at 60% opacity
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Version:**
- Element type: Text box
- Position: X: 0.5". Y: 34.4"
- Font: Inter Regular, 11 pt
- Color: `#F0EDE8` at 40% opacity
- Text:

> v1.0 — 2026

**Logo placeholder:**
- Element type: Text box (or image placeholder)
- Position: X: 21.0". Y: 33.5"
- Width: 2.5". Height: 1.5"
- Font: Barlow SemiBold, 14 pt
- Color: `#F0EDE8` at 30% opacity
- Alignment: Center
- Text:

> [LOGO]

---

## Part 5 — Grouping and Layer Order

After building all zones, verify the following group structure:

| Group Name | Contains | Lock After Grouping? |
|-----------|----------|---------------------|
| Zone 1 — Header | Blocks A + B | Yes |
| Zone 2 — Cell Diagram | All C-series elements (tank, electrodes, arrows, labels) | Yes |
| Zone 3 — Four Essentials | Block D (4 panel groups) | Yes |
| Zone 4 — Anode Comparison | Block E (two columns) | Yes |
| Zone 5 — Variables + Defects | Blocks F + G | Yes |
| Zone 6 — Footer | Block H (all footer elements) | Yes |

**Important:** The cell diagram (Zone 2) contains the most elements. Build it methodically — tank first, then electrodes, then arrows, then labels. Group sub-components (e.g., "cathode assembly" = cathode rectangle + deposit layer + label + reaction label) before grouping the entire zone.

---

## Part 6 — Light Edition Remap Table

To produce the Light edition, duplicate the entire Dark edition page, then recolor every element per this table:

| Element / Role | Dark Edition | Light Edition |
|---|---|---|
| Page background | `#1A1F2E` Gunmetal Dark | `#F0EDE8` Warm White |
| Primary text | `#F0EDE8` Warm White | `#1A1F2E` Gunmetal Dark |
| Amber accent | `#E8A020` | `#B87A10` (darkened 15%) |
| Teal accent | `#2EC4B6` | `#1E9A8F` (darkened 20%) |
| Emerald accent | `#27AE60` | `#1D8A4A` (darkened 20%) |
| Coral accent | `#E05C5C` | `#C43C3C` (darkened 20%) |
| Mid Slate fills | `#3A4055` | `#D0D4DC` (light neutral) |
| Deep Navy footer | `#0D1020` | `#E2E0DB` (light warm gray) |
| Dark Callout fills | `#1E2435` | `#E8E5E0` (light warm fill) |
| Alt Row fills | `#252B3D` | `#F5F3EF` (near-white alternating) |
| Bright Silver deposit | `#C8D0D8` | `#3A4055` (inverted — dark on light) |
| Text at reduced opacity | Adjust to 65/50/40% on dark | Adjust to same % on light equivalents |

**Electrolyte fill (C2):** Remap the Teal fill at 15% opacity to the darkened Teal at 15% opacity on the light background. The wash of color will be subtle but present.

**No overrides required.** Standard remap applies throughout.

---

## Part 7 — Export Checklist

| Export | Size | Edition | Format | Filename |
|--------|------|---------|--------|----------|
| 1 | 24×36" | Dark | PDF Print (300 DPI) | `Poster-02-Electroplating-Process-24x36-Dark.pdf` |
| 2 | 24×36" | Light | PDF Print (300 DPI) | `Poster-02-Electroplating-Process-24x36-Light.pdf` |
| 3 | 18×24" | Dark | PDF Print (300 DPI) | `Poster-02-Electroplating-Process-18x24-Dark.pdf` |
| 4 | 18×24" | Light | PDF Print (300 DPI) | `Poster-02-Electroplating-Process-18x24-Light.pdf` |
| 5 | 24×36" | Dark | PNG (digital download) | `Poster-02-Electroplating-Process-24x36-Dark.png` |
| 6 | 24×36" | Light | PNG (digital download) | `Poster-02-Electroplating-Process-24x36-Light.png` |

For the 18×24" versions: duplicate the 24×36" pages, resize to 18×24", and verify all text meets the 14 pt minimum floor. Adjust element sizes proportionally.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #2 — The Electroplating Process — Construction Workup v1.0*
*2026-04-04*
