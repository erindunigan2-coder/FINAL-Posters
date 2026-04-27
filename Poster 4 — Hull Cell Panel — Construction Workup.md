---
Project: Plating Posters Inc
Poster Number: 4
Title: Reading Your Hull Cell Panel
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-03-19T00:00:00
Updated: 2026-03-19T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 4 — Reading Your Hull Cell Panel — Design Brief.md (v1.0)"
  - "Poster 4 — Hull Cell Panel — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Acid Zinc Plating Troubleshooting Guide v1 (Sections 4, 7, 8)
Watson Flags: ALL CLEARED (C1, C2, C3 — see Content and Layout Draft for details)
Process Scope: Acid zinc KCl/NH4Cl only — one process per poster (standing series rule)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HullCell
  - ConstructionWorkup
  - AcidZinc
---

# Poster # Poster #4 — Construction Workup
## Reading Your Hull Cell Panel

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-03-19*

This document is the construction workup for Poster #4. It translates the approved Design Brief (v1.0) and finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. All technical content is confirmed production-ready. All Watson flags are cleared.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 4 — Hull Cell Panel — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

**Source of truth for visual spec:** `Poster 4 — Reading Your Hull Cell Panel — Design Brief.md` — this workup translates those specs into the design workflow terms.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for table rows, callout boxes, and accent borders
- Table elements (using the native table tool or manually constructed grid of rectangles + text boxes)
- Color fills set to exact hex values
- Background page color set to exact hex
- Gradient shapes for zone band transitions (limited — see note below)
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Gradient mesh / complex surface gradients:** The tool supports simple linear gradients on shapes, but not gradient mesh (used in the spec for the Hull cell panel surface). The panel illustration's surface gradient should be simplified to a two-stop linear gradient (left edge `#D8E0E8` → right edge `#B8C0C8`) within the silver base. This is a workable simplification.

2. **Hull cell panel illustration:** The generation tool does not support freeform vector illustration from scratch. The panel illustration must either be: (a) built as a composite of simple geometric shapes (rectangles, gradient overlays, text), or (b) created externally (GIMP or Inkscape as a PNG/SVG) and placed into the design as an uploaded image. **Recommendation for Elara's prompt: use approach (a) — build the panel as layered rectangles with gradient overlays. This keeps everything in the design and Drew can build it without needing a separate tool for a first version.**

3. **4 pt left-border accents on table rows:** The generation tool does not have a "left border only" stroke option. Simulate with a narrow colored rectangle (4 pt equivalent width) positioned against the left edge of each table row rectangle. This is manual but straightforward .

4. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Producing the Light edition requires duplicating the design page and manually recoloring every element. Elara should instruct Drew to build the Dark edition first, duplicate the page, and then work through the remap table (Part 5 of this document) element by element. It is tedious but not difficult.

5. **Monospace font — JetBrains Mono:** The generation tool may not include JetBrains Mono in its standard font library. **Check: the tool supports font uploads. If Drew has the tool, upload JetBrains Mono from Google Fonts before beginning.** If not available, substitute Courier Prime (available ) for the data table fields. Flag this to Drew.

6. **Print size — 24×36":** The design canvas is 24×36". Set this at document creation. Elara should specify this exact size in the prompt. For 18×24" version, duplicate the design and resize — accept auto-resize for a starting point, then verify text sizing meets the floor (14 pt body text minimum).

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

These are the first steps Drew should complete before placing any content.

### Step 1 — Create the document
- Open the design tool. Create a new custom-size design.
- Width: 24 inches. Height: 36 inches.
- This creates the 24×36" master poster artboard.

### Step 2 — Set the background color
- Set the page background color to: **`#1A1F2E`** (Gunmetal Dark)
- This is the Dark edition background. Every subsequent element sits on this.

### Step 3 — Upload fonts (the Pro tier required)
- Upload from Google Fonts / JetBrains.org:
  - **Barlow Condensed ExtraBold** — for all headlines and zone labels
  - **Barlow SemiBold** — for all subheadings, section labels, callout titles
  - **Inter Regular** and **Inter Medium** — for all body text and table data
  - **JetBrains Mono Regular** — for all data/parameter table fields and zone sub-labels

### Step 4 — Set up color palette (save these as Brand Colors )
Save all of the following as Brand Colors for this design. Name them exactly as shown:

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | HCD zone, section titles, Amber row accents |
| Teal | `#2EC4B6` | LCD zone, callout borders and titles |
| Emerald | `#27AE60` | "Good bath" row accent |
| Coral | `#E05C5C` | Contamination row accents |
| Mid Slate | `#3A4055` | Table header fill, row rules, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills |
| Alt Row | `#252B3D` | Alternating table row backgrounds |
| Bright Silver | `#C8D0D8` | Hull cell panel surface base |
| Panel Edge | `#9AA0B0` | Panel border stroke |

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next.

```
ZONE 1 — HEADER BAND (top 8% of page / ~2.9")
  Block A: Headline (left) + Block B: Orientation Callout Box (right)

ZONE 2 — HULL CELL PANEL ILLUSTRATION (rows 9–38% / ~10.4" tall)
  Block D: Panel body + zone bands + zone labels + sub-labels + caption

ZONE 3A — DIAGNOSTIC TABLE (rows 38–75% / ~13.3" tall, left 58% of width)
  Block E: "What Your Panel Is Telling You" table — 11 data rows

ZONE 3B — RIGHT COLUMN (rows 38–75%, right 38% of width)
  Block C: Setup Parameters table (upper portion)
  Block G: SPC Tool callout box (lower portion)

ZONE 4 — ISOLATION PROTOCOL CALLOUT (rows 75–87% / ~4.3" tall, full width)
  Block F: "When the Diagnosis Isn't Clear" callout box

ZONE 5 — FOOTER BAND (bottom 6% / ~2.2", full width)
  Block H: Poster title | series name | disclaimer | logo placeholder | version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Height: ~2.9" from the top of the page.
**Background:** Same as page (`#1A1F2E`) — no separate fill needed. Optional: add a 1 pt horizontal rule in `#3A4055` along the bottom edge of this zone to separate it from Zone 2. Evaluate during build.

---

**BLOCK A — Headline**

Element type: Text box
Position: Left-aligned, 0.5" from left trim edge, vertically centered in the header band
Font: Barlow Condensed ExtraBold
Size: 96 pt (adjust down to 80 pt if the full headline runs past col 7 / the 58% mark)
Color: `#F0EDE8`
Letter spacing: Tight (−15 to −20 in Affinity terms; in the design use Spacing slider — set to approximately −3 to −5)
Text (all caps — uppercase or typed in caps):

> READING YOUR HULL CELL PANEL

**BLOCK A — Subheading**

Element type: Text box
Position: Left-aligned, 0.5" from left trim, 6–8 pt below the headline baseline
Font: Barlow SemiBold
Size: 42 pt
Color: `#E8A020` (Amber)
Text:

> Diagnose your plating bath before it diagnoses your scrap rate.

---

**BLOCK B — "What Is a Hull Cell?" Orientation Box**

This is a callout box positioned in the upper-right of the header band.

**Callout container:**
- Element type: Rounded rectangle
- Position: Right-aligned, 0.5" from right trim; vertically centered in the header band
- Width: ~38% of page width (~9.1")
- Height: Sized to fit ~5 lines of body text at 18 pt with 20 pt internal padding (~1.5–1.8")
- Fill color: `#1E2435` (Dark Callout)
- Border (stroke): 1.5 pt, color `#2EC4B6` (Teal)
- Corner radius: 8 pt

**Callout title:**
- Element type: Text box inside the container
- Font: Barlow SemiBold
- Size: 24 pt
- Color: `#2EC4B6` (Teal)
- Text: WHAT IS A HULL CELL?

**Callout body:**
- Element type: Text box inside the container
- Font: Inter Regular
- Size: 18 pt
- Color: `#F0EDE8`
- Text:

> The Hull cell is a 267 mL trapezoidal tank that simultaneously tests a range of current densities on a single cathode panel. The angled cathode creates a current density gradient — high at one end, low at the other — so one 5-minute test reveals how your bath performs across its entire operating range.

**Callout closing punch line:**
- Element type: Text box (separate from body — allows different style treatment)
- Font: Inter Medium (or SemiBold)
- Size: 18 pt
- Color: `#F0EDE8`
- Position: Below body text, with a thin top rule separator in `#3A4055` (add as a 0.5 pt horizontal line element)
- Text:

> One panel. One test. Every zone, all at once.

---

### ZONE 2 — Hull Cell Panel Illustration

**Dimensions:** Full page width (within 0.5" margins). Spans approximately rows 9%–38% of page height (~10.4" tall zone). The panel itself occupies most of this zone; labels and caption fill the space below.

This zone is built from geometric shapes layered together. There is no freeform vector drawing — everything is rectangles, gradient overlays, and text.

---

**Step 1 — Panel body rectangle**

- Element type: Rectangle
- Width: Page width minus 1" (0.5" margin each side) — approximately 23"
- Height: ~6.5"
- Position: Centered horizontally; sits in the upper portion of Zone 2
- Fill: Linear gradient, left to right
  - Left stop: `#D8E0E8` (slightly lighter than base silver — HCD end)
  - Right stop: `#B8C0C8` (slightly darker — LCD end)
  - Direction: horizontal, left to right
- Border (stroke): 2 pt, color `#9AA0B0` (Panel Edge)
- Corner radius: 0

*Design note: This gradient represents the visual character of a healthy zinc deposit — brighter and more active at high current (left), slightly softer and more uniform at low current (right). It is a simplification of the full gradient mesh spec from the Design Brief, but it reads correctly .*

---

**Step 2 — HCD zone band overlay**

- Element type: Rectangle
- Width: ~7.7" (one-third of the panel width)
- Height: ~0.75" (approximately 12% of the panel height — top edge only)
- Position: Left edge of the panel, flush with the top edge of the panel rectangle
- Fill: Linear gradient
  - Left stop: `#E8A020` at 70% opacity
  - Right stop: `#E8A020` at 0% opacity
  - Direction: horizontal, left to right (fades out toward center)
- No border
- Layer above the panel rectangle

---

**Step 3 — LCD zone band overlay**

- Element type: Rectangle
- Width: ~7.7" (one-third of the panel width)
- Height: ~0.75"
- Position: Right edge of the panel, flush with the top edge of the panel rectangle
- Fill: Linear gradient
  - Left stop: `#2EC4B6` at 0% opacity
  - Right stop: `#2EC4B6` at 70% opacity
  - Direction: horizontal, left to right (fades in from center toward right edge)
- No border
- Layer above the panel rectangle

*Note: The two gradient band overlays create a smooth zone color transition across the top edge of the panel — Amber bleeding in from the left, Teal bleeding in from the right, with the silver center reading through. This matches the Design Brief intent without requiring a gradient mesh.*

---

**Step 4 — Zone labels (below panel)**

Place three text groups below the panel rectangle, with approximately 8 pt spacing from the panel bottom edge.

**HCD Zone label (left third):**
- Text box centered under the left third of the panel
- Line 1: Font Barlow Condensed ExtraBold, 24 pt, color `#E8A020`
  - Text: HIGH CURRENT DENSITY
- Line 2 (sub-label): Font JetBrains Mono Regular (or Courier Prime if unavailable), 16 pt, color `#F0EDE8`
  - Text: ~10–50 A/dm² at 2 A

**Mid-Current Zone label (center):**
- Text box centered under the middle third of the panel
- Line 1: Font Barlow Condensed ExtraBold, 24 pt, color `#F0EDE8`
  - Text: MID-CURRENT
- Line 2 (sub-label): Font JetBrains Mono Regular, 16 pt, color `#F0EDE8`
  - Text: ~2–10 A/dm² at 2 A

**LCD Zone label (right third):**
- Text box centered under the right third of the panel
- Line 1: Font Barlow Condensed ExtraBold, 24 pt, color `#2EC4B6`
  - Text: LOW CURRENT DENSITY
- Line 2 (sub-label): Font JetBrains Mono Regular, 16 pt, color `#F0EDE8`
  - Text: ~0.1–1 A/dm² at 2 A

---

**Step 5 — Callout arrows**

Three leader lines from the bottom edge of the panel rectangle, one per zone, dropping downward toward the diagnostic table.

In the design, use the Line element with an arrowhead at the lower end:
- Line weight: 1.5 pt
- Color: `#3A4055` (Mid Slate)
- Arrowhead: small, at the bottom (pointing down toward the table)
- Start point: bottom edge of the panel, vertically aligned with the center of each zone
- End point: approximately 0.5" above the top edge of the diagnostic table
- the line tool allows click-to-draw with arrowheads — use this

*These arrows are navigation guides. They should be modest — visible but not dominant.*

---

**Step 6 — Diagram caption**

- Element type: Text box
- Position: Below the zone labels, centered horizontally
- Font: Inter Regular
- Size: 14 pt
- Color: `#F0EDE8` at 70% opacity (use the tool's transparency slider on the text element)
- Text:

> Current density values per Wagner scale. Left (narrow end) = high current density. Right (wide end) = low current density.
> Acid zinc KCl/NH₄Cl bath — 2 A total current standard.

---

### ZONE 3A — Diagnostic Interpretation Table

**Position:** Left 58% of page width (within 0.5" margins); rows 38%–75% of page height (~13.3" tall zone)
**Affinity equivalent:** `[DATA] Diagnostic Table` layer

---

**Section title:**
- Element type: Text box
- Position: Above the table, left-aligned within Zone 3A
- Font: Barlow SemiBold
- Size: 28 pt
- Color: `#E8A020`
- Text: WHAT YOUR PANEL IS TELLING YOU

---

**Table construction method for the design:**

A native Table element may have limited styling options. For this poster's level of detail (alternating row colors, per-row left-border accents in three different colors), the recommended approach is to build the table as a stack of layered rectangles and text boxes. This gives full control over every design decision.

**Column widths (within Zone 3A width):**
- Column 1 "Panel Appearance": 40% of zone width
- Column 2 "Most Likely Cause": 30% of zone width
- Column 3 "First Corrective Action": 30% of zone width

**Row height:** Each row should be approximately 1" tall to accommodate multi-line cell content at 18 pt with comfortable padding. Some rows will need slightly more height — adjust as needed.

**Build sequence for each row:**

1. Draw a rectangle spanning the full Zone 3A width at the appropriate row height. Fill with the row background color (see table below).
2. Draw a narrow rectangle (width: 6 pt, same height as the row) at the left edge of the row rectangle. Fill with the row's border accent color.
3. Place text boxes for each column inside the row bounds. Left padding: account for the 6 pt border rectangle — start text content 16 pt from the row left edge. Top/bottom padding: 8 pt.

**Row specifications:**

| Row | Content | Row background | Left-border color |
|-----|---------|---------------|-------------------|
| Header | PANEL APPEARANCE / MOST LIKELY CAUSE / FIRST CORRECTIVE ACTION | `#3A4055` | None |
| 1 | Good bath | `#1A1F2E` + 8% Emerald tint overlay | `#27AE60` Emerald |
| 2 | Brightener deficiency | `#252B3D` | `#E8A020` Amber |
| 3 | Brightener overload | `#1A1F2E` | `#E8A020` Amber |
| 4 | Carrier deficiency | `#252B3D` | `#E8A020` Amber |
| 5 | Carrier overload | `#1A1F2E` | `#E8A020` Amber |
| 6 | Iron contamination | `#252B3D` | `#E05C5C` Coral |
| 7 | Lead/cadmium contamination | `#1A1F2E` | `#E05C5C` Coral |
| 8 | Copper contamination | `#252B3D` | `#E05C5C` Coral |
| 9 | Organic contamination | `#1A1F2E` | `#E05C5C` Coral |
| 10 | Low zinc metal | `#252B3D` | `#E8A020` Amber |
| 11 | Suspended solids | `#1A1F2E` | `#E8A020` Amber |

*For Row 1 (Good bath): in addition to the Emerald left border, apply a second transparent rectangle over the full row at 8% opacity, filled `#27AE60`. This creates the subtle green tint that distinguishes the reference row.*

---

**Header row text:**
- Font: Barlow SemiBold, 22 pt, color `#E8A020`
- Column labels: PANEL APPEARANCE / MOST LIKELY CAUSE / FIRST CORRECTIVE ACTION

**Data row text:**
- Font: Inter Regular, 18 pt, color `#F0EDE8`
- Line height: 140% (set in the design text spacing)
- In the "Most Likely Cause" column: the cause name (first phrase) should be set in Inter Medium or SemiBold for scannability. Example: **Iron contamination** in SemiBold, then `(>50–75 ppm)` dropping to Regular. In the design, achieve this by using two separate inline text styles within the same text box, or by using separate text boxes positioned adjacently.

**Complete table cell content — all 11 rows:**

*Row 1 — Good bath (Emerald border):*
- Panel Appearance: Mirror bright from HCD through mid-current; slight softening at LCD; no skip plate
- Most Likely Cause: **Good bath**
- First Corrective Action: No action needed — archive this panel as your visual reference standard

*Row 2 — Brightener deficiency (Amber border):*
- Panel Appearance: Overall semi-bright or matte; burn zone at HCD enlarges toward mid-current
- Most Likely Cause: **Brightener deficiency**
- First Corrective Action: Add brightener in 0.1–0.5 mL/L increments; re-run panel after each addition

*Row 3 — Brightener overload (Amber border):*
- Panel Appearance: Mirror bright at HCD and mid-current; LCD progressively dull, advancing to skip plate at extremes
- Most Likely Cause: **Brightener overload**
- First Corrective Action: Carbon treat at 5–10 g/L; reconstitute additive system from fresh baseline

*Row 4 — Carrier deficiency (Amber border):*
- Panel Appearance: Pitting across the full panel; HCD burning prominent
- Most Likely Cause: **Carrier (wetting agent) deficiency**
- First Corrective Action: Check bath temperature vs. cloud point first; add carrier incrementally; re-run panel

*Row 5 — Carrier overload (Amber border):*
- Panel Appearance: Overall hazy or milky panel; reduced deposit brightness; foaming visible in production tank
- Most Likely Cause: **Carrier overload / temperature above cloud point**
- First Corrective Action: Check and lower bath temperature immediately; carbon treat if needed

*Row 6 — Iron contamination (Coral border):*
- Panel Appearance: Yellow to dark band at HCD; haze across mid-current; LCD coverage loss or skip plate
- Most Likely Cause: **Iron contamination** (>50–75 ppm)
- First Corrective Action: Add 1–2 mL/L of 30% H₂O₂; raise pH to 5.0–5.5; allow to settle; filter thoroughly

*Row 7 — Lead/cadmium contamination (Coral border):*
- Panel Appearance: Skip plate in LCD; HCD appears normal; no improvement after brightener adjustment
- Most Likely Cause: **Lead or cadmium contamination** (1–2 ppm threshold)
- First Corrective Action: Zinc dust treatment; dummy plate at low CD; identify and eliminate contamination source

*Row 8 — Copper contamination (Coral border):*
- Panel Appearance: Dark or black deposit visible after bright dip or passivation
- Most Likely Cause: **Copper contamination** (>10 ppm)
- First Corrective Action: Dummy plate at 0.1–0.3 A/dm² on steel cathodes; follow with zinc dust treatment

*Row 9 — Organic contamination (Coral border):*
- Panel Appearance: LCD dullness; streaking across panel; variable pitting not resolved by carrier addition
- Most Likely Cause: **Organic contamination**
- First Corrective Action: H₂O₂ pre-treat at 0.5–1 mL/L; then carbon treat at 5–10 g/L; reconstitute additives

*Row 10 — Low zinc metal (Amber border):*
- Panel Appearance: Burning advances from HCD into mid-current; LCD coverage is consistently poor
- Most Likely Cause: **Low zinc metal concentration**
- First Corrective Action: Analyze zinc by titration; add zinc metal source; verify anode area is adequate

*Row 11 — Suspended solids (Amber border):*
- Panel Appearance: Rough, nodular deposit; visible particles in bath; turbidity
- Most Likely Cause: **Suspended solids** — pH too high or filtration failure
- First Corrective Action: Check pH (target 4.8–5.2); inspect filter integrity and anode bags; clean tank bottom

---

**Table footnotes** (below the table, same width as Zone 3A):
- Font: Inter Regular, 13 pt, color `#F0EDE8` at 60% opacity (use transparency on text element)
- Three footnotes, each on its own line, preceded by an asterisk:

> *Scope: acid zinc KCl/NH₄Cl baths only. Results may differ for other zinc bath chemistries.*
>
> *Cadmium is highly toxic. Even trace cadmium contamination via parts warrants immediate bath analysis. Do not assume lead or cadmium without analytical confirmation.*
>
> *After any carbon treatment, brightener and carrier are partially removed. Always reconstitute the full additive system after carbon treatment.*

---

### ZONE 3B — Right Column

**Position:** Right 38% of page width (within 0.5" right margin); rows 38%–75% (same vertical band as Zone 3A). A 0.25" gutter separates Zone 3A and Zone 3B.

---

**BLOCK C — Hull Cell Setup Parameters**

**Section title:**
- Font: Barlow SemiBold, 24 pt, color `#E8A020`
- Text: HULL CELL SETUP PARAMETERS

**Table header:**
- Rectangle: full Zone 3B width, fill `#3A4055`
- Text: PARAMETER / VALUE — Barlow SemiBold 20 pt, color `#E8A020`
- Column proportions: Parameter 45% / Value 55%

**Table data (8 rows):**
Build using the same rectangle-stack method as Zone 3A. Row alternation: `#1A1F2E` / `#252B3D`. No left-border accents on this table.
- Font: JetBrains Mono Regular (or Courier Prime), 16–18 pt, color `#F0EDE8`

| Parameter | Value |
|---|---|
| Cell volume | 267 mL |
| Cathode material | Cold-rolled steel — cleaned and acid-activated |
| Anode material | SHG zinc — 99.99% pure (lower grades introduce Pb, Cd, Fe) |
| Test current — rack | 2 A (standard); 3 A for high-current diagnostic |
| Test current — barrel | 1 A |
| Test duration | 5 minutes |
| Agitation | Air agitation — required |
| Temperature | Match actual bath temperature |

*Design note: The anode row content is long — it may need to wrap to two lines. Allow the row to expand in height rather than truncating the contamination warning. That warning is the reason SHG zinc matters and it stays on the poster.*

**Cathode prep note (below table):**
- Add a 1 pt horizontal rule above this section in color `#3A4055`
- Label: "CATHODE PREPARATION" in Barlow SemiBold 16 pt, `#E8A020`
- Body: Inter Regular 14–16 pt, `#F0EDE8`
- Text:

> Degrease with acetone or electrocleaner. Activate in 5–10% HCl for 15–30 seconds. Rinse thoroughly. Use immediately. Do not touch with bare hands after activation.
>
> OPTIONAL: Bright dip or passivate the plated panel to reveal deposit quality — highly recommended for contamination diagnosis.

---

**BLOCK G — Make Your Hull Cell a Control Chart (Callout Box)**

Position: Lower portion of Zone 3B, bottom-aligned to match the bottom of Zone 3A. Evaluated at layout time — reduce internal padding in Block C if needed to fit both cleanly.

**Container:**
- Rounded rectangle
- Width: Full Zone 3B width
- Fill: `#1E2435` (Dark Callout)
- Border: 1.5 pt, `#2EC4B6` (Teal)
- Corner radius: 8 pt
- Internal padding: 16 pt all sides

**Title:**
- Font: Barlow SemiBold, 18 pt (may need to wrap to two lines given column width)
- Color: `#2EC4B6`
- Text: MAKE YOUR HULL CELL A CONTROL CHART

**Body bullets (4 items):**
- Font: Inter Regular, 15–16 pt, color `#F0EDE8`
- Bullet character: filled circle in `#2EC4B6` (use the tool's bullet list or a Unicode bullet `•` colored manually)
- Texts:

> - Run weekly at minimum — or every 500–1000 ampere-hours of production throughput
> - Archive every panel with: date, bath analysis results, ampere-hour reading, and all additions made
> - Laminate a known-good reference panel and mount it next to this poster
> - Visual trends across archived panels reveal bath drift before symptoms appear on production parts

---

### ZONE 4 — Isolation Protocol Callout

**Position:** Full page width (within 0.5" margins); rows 75%–87% (~4.3" tall zone)
**Affinity equivalent:** `[CALLOUT] Isolation Protocol` layer

**Container:**
- Rounded rectangle spanning full safe-zone width
- Fill: `#1E2435` (Dark Callout)
- Border: 1.5 pt, `#2EC4B6` (Teal)
- Corner radius: 8 pt
- Internal padding: 20 pt all sides

**Internal layout — two columns:**
This callout uses a two-column layout to avoid reading as a wall of text:
- Left column: ~40% of callout interior width — contains title and intro line
- Right column: ~56% — contains the four numbered steps and closing rule

In the design, simply position text boxes for the left and right columns within the container bounds. No column tool is needed — just position manually.

**Title (left column):**
- Font: Barlow SemiBold, 24 pt, color `#2EC4B6`
- Allow to wrap across two lines:
  - Line 1: WHEN THE DIAGNOSIS ISN'T CLEAR:
  - Line 2: THE ISOLATION PROTOCOL
- Leading: tight (reduce line spacing to 0.9)

**Intro line (left column, below title with 8 pt gap):**
- Font: Inter Regular, 16 pt, color `#F0EDE8`
- Text:

> When one corrective action doesn't solve the problem, test one variable at a time using separate aliquots of fresh bath solution.

**Numbered steps (right column):**
- Step numbers: Barlow SemiBold or JetBrains Mono, 18 pt, color `#2EC4B6`
- Step body: Inter Regular, 16 pt, color `#F0EDE8`
- Steps:

> 1. Add a brightener increment to a fresh aliquot — run panel. If HCD and mid-current improve: brightener was low.
> 2. Add a carrier increment to a fresh aliquot — run panel. If pitting clears: carrier was low.
> 3. Add boric acid to a fresh aliquot — run panel. If HCD burning reduces: boric acid was low.
> 4. Adjust pH in a fresh aliquot with HCl or zinc carbonate — run panel. Confirm whether pH drift was the driver.

**Closing rule (right column, below steps with 8 pt gap):**
- Add a narrow vertical rectangle (2 pt wide, full height of closing rule text, color `#E8A020`) to the left of this text — this is the Amber left accent rule from the Design Brief
- Font: Inter Medium, 16 pt, color `#E8A020`
- Text:

> THE RULE: Change one variable. Run one panel. Decide. Then move to the next variable.

---

### ZONE 5 — Footer Band

**Dimensions:** Full page width, bottom 6% (~2.2") of page height
**Background rectangle:** Full width, `#0D1020` (Deep Navy) fill — no corner radius

---

**Disclaimer line (above footer band, not inside it):**
- Position: Full width, centered, 8 pt above the top edge of the footer band
- Font: Inter Regular, 11 pt, color `#F0EDE8` at 50% opacity (transparency: 50%)
- Text:

> This poster is a diagnostic reference tool. Always consult your process supplier's documentation and applicable safety data sheets. Not a substitute for laboratory analysis.

---

**Within footer band — three sections, horizontal:**

Left section (~35% of band width):
- Font: Barlow SemiBold, 14 pt, color `#F0EDE8`
- Vertically centered in the band
- Text: Reading Your Hull Cell Panel

Center section (~40%):
- Font: Inter Regular, 12 pt, color `#F0EDE8` at 70% opacity
- Vertically centered
- Text: Plating Posters Inc — Metal Finishing Reference Series

Right section (~25%):
- Logo placeholder: a filled rectangle in `#3A4055`, approximately 40×40 pt equivalent
- Inside placeholder: text "LOGO" in JetBrains Mono 10 pt, `#F0EDE8`, centered
- Version line below or adjacent: "v1.0 — 2026" in JetBrains Mono 10 pt, `#F0EDE8` at 50% opacity

---

## Part 5 — Light Edition Conversion

After the Dark edition is complete, duplicate the entire design page . On the duplicate, manually remap every element's color using this table.

**Important:** Do not remap `#C8D0D8` Bright Silver — the panel illustration surface stays metallic in both editions.

| Dark edition color | Light edition replacement | Notes |
|---|---|---|
| `#1A1F2E` (Gunmetal Dark) | `#F5F4F0` (Off-White) | Background; also all dark fills |
| `#F0EDE8` (Warm White) | `#1A1F2E` (Gunmetal Dark) | All body text becomes dark on light |
| `#1E2435` (Dark Callout BG) | `#ECEEF4` (Light Callout) | All callout box fills |
| `#252B3D` (Alt Row) | `#E8E8F0` (Alt Row Light) | Alternating table rows |
| `#0D1020` (Deep Navy) | `#1A1F2E` | Footer band |
| `#E8A020` (Amber) | `#C8860A` (Amber Dark) | HCD zone, section titles, Amber accents |
| `#2EC4B6` (Teal) | `#1A8C82` (Teal Dark) | LCD zone, callout borders and titles |
| `#27AE60` (Emerald) | `#1E7A47` (Forest Green) | Good bath row accent |
| `#E05C5C` (Coral) | `#B83E3E` (Deep Coral) | Contamination row accents |
| `#3A4055` (Mid Slate) | `#D0D4DE` (Light Slate) | Table header fills, rules |
| `#C8D0D8` (Bright Silver) | `#C8D0D8` (unchanged) | Panel surface — always metallic |

**Post-remap check:**
- Panel surface `#C8D0D8` still reads as metallic against `#F5F4F0` — it should; silver on off-white is clean
- All body text passes WCAG AA (minimum 4.5:1 contrast ratio) against its background
- Zone band opacity may need adjustment in the Light edition — if the Amber band at 70% opacity looks too solid against the light background, reduce to 50–60%
- The Good bath row 8% Emerald tint overlay may need to increase to 12% opacity in the Light edition to remain visible against `#E8E8F0`
- Footnote text at 60% opacity and disclaimer at 50% opacity — verify both remain legible against `#F5F4F0`

---

## Part 6 — Export Specifications

Configure these exports . Name files exactly as shown.

| File name | Format | Size | Color mode | Bleed |
|---|---|---|---|---|
| `Hull-Cell-Panel-Dark-24x36-Print.pdf` | PDF (Print) | 24×36" | CMYK | Yes (0.125") |
| `Hull-Cell-Panel-Dark-18x24-Print.pdf` | PDF (Print) | 18×24" | CMYK | Yes |
| `Hull-Cell-Panel-Dark-Digital.pdf` | PDF (Digital) | 24×36" | RGB | No |
| `Hull-Cell-Panel-Light-24x36-Print.pdf` | PDF (Print) | 24×36" | CMYK | Yes |
| `Hull-Cell-Panel-Light-18x24-Print.pdf` | PDF (Print) | 18×24" | CMYK | Yes |
| `Hull-Cell-Panel-Light-Digital.pdf` | PDF (Digital) | 24×36" | RGB | No |

*Six export files per poster is the series standard.*

*Note on print export: the tool's "Print Bleed" PDF export option adds bleed and crop marks automatically. Use this setting for all print files. For digital PDFs, use standard PDF export.*

---

## Part 7 — Notes for Elara

The following items are judgment calls that Elara should work into the generation prompt with explicit instructions for Drew, rather than leaving them to interpretation at build time.

1. **Font upload first, before anything else.** If JetBrains Mono is not available in the design account, instruct Drew to substitute Courier Prime for all data table fields and zone sub-labels. Courier Prime is available in the design without upload. Flag this as the preferred fallback and note it should be updated if JetBrains Mono becomes available later.

2. **Panel illustration sequencing.** The Hull cell panel is the most visually complex element. Instruct Drew to build this element first, in isolation, before placing it into the layout. Group all panel elements (base rectangle, two gradient overlays, zone labels, sub-labels, callout arrows, caption) before positioning the group in Zone 2. This makes repositioning clean.

3. **Table construction.** The diagnostic table (Zone 3A, 11 rows) is the most time-consuming element. Instruct Drew to build one row completely (background rectangle + left-border rectangle + three text boxes) and then duplicate it 10 times before changing the content and border colors for each row. This is dramatically faster than building each row from scratch.

4. **Group each zone after completing it.** After finishing each of the five zones, Drew should select all elements in that zone and group them (Ctrl+G / Cmd+G). This prevents accidental element displacement while working on adjacent zones.

5. **Snap-to-guides.** ruler guides can be pulled from the ruler area at the top and left edges of the canvas. Instruct Drew to set guides at: the 0.5" safe zone margin on all four sides, and at the horizontal boundaries between each zone (Zone 1/2 border, Zone 2/3 border, Zone 3/4 border, Zone 4/5 border). This ensures zone boundaries are clean.

6. **Amber zone band gradient direction.** In the design, when applying a gradient fill to the HCD zone band overlay, ensure the gradient direction is set to horizontal (left to right). The default to top-to-bottom — Drew will need to rotate the gradient 90 degrees or set it manually.

7. **Light edition production sequence.** After the Dark edition is approved, instruct Drew to: (a) duplicate the page, (b) rename the duplicate "Light Edition," (c) work through the remap table in Part 5 from top to bottom, changing background first, then text, then UI element fills, then accent colors. Doing it in this order makes it easier to see progress and catch missed elements.

8. **Logo placeholder.** Until the Plating Posters Inc logo is finalized, a filled rectangle with "LOGO" text in the footer is the approved placeholder. Do not design around a logo that does not yet exist.

---

## Part 8 — Asset Summary Report for June

**Asset Name:** Poster #4 — Reading Your Hull Cell Panel — Construction Workup

**Version:** v1.0

**Date:** 2026-03-19

**Files produced this session:**

| File | Location | Status |
|---|---|---|
| `Poster 4 — Hull Cell Panel — Construction Workup.md` | `Plating Posters Inc/` | Complete — ready for Elara |

**Prior files this workup depends on:**

| File | Status |
|---|---|
| `Poster 4 — Reading Your Hull Cell Panel — Design Brief.md` (v1.0) | Approved |
| `Poster 4 — Hull Cell Panel — Content and Layout Draft.md` (v1.0) | All Watson flags cleared — production-ready |

**Current Poster #4 status:** Construction Workup complete. All content finalized. Ready for Elara to engineer the generation prompt.

**Recommended next steps:**

1. **Elara:** Receive this workup document. Engineer a detailed, step-by-step generation prompt for Drew that translates Part 3 and Part 4 of this document into precise generation instructions. Address all seven items in Part 7 (Notes for Elara) explicitly. Confirm JetBrains Mono font strategy before issuing the prompt.

2. **Drew:** Acquire design tool subscription (noted as planned for Monday). Confirm Pro tier (required for font upload). Once the generation prompt from Elara is in hand, build the Dark edition first, then Light edition as a duplicate.

3. **Tyler (evenings/weekends — not blocking):** Three low-priority validation items from the Content and Layout Draft (v1.0) Section 6 remain outstanding. These do not block the build but should be cleared before the first print run is treated as a commercial-release product.

4. **June:** Update Poster #4 status in project tracking to "Construction Workup Complete — Awaiting Elara Prompt." Flag Drew's design subscription as a prerequisite for the build.

5. **Alaina (next session):** Update the `project_poster_library.md` memory file with Poster #4 status. Assess which next poster in the library is ready to advance — Poster #1 (Surface Preparation) or Poster #3 (Acid vs. Alkaline Zinc) are strong candidates based on relevance to Drew's current customer base.

---

*Alaina — Plating Posters Inc Creative Lead*
*Construction Workup v1.0 — 2026-03-19*
*Technical source: Watson, Acid Zinc Plating Troubleshooting Guide v1 (2026-03-14). All Watson flags cleared.*
*This document is the design-optimized translation of Design Brief v1.0 and Content and Layout Draft v1.0.*
*Intended recipient: Elara — for the design construction prompt engineering.*
