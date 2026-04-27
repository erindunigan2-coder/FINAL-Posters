---
Project: Plating Posters Inc
Poster Number: 21
Title: "Alloy Plating Fundamentals — Brass, Bronze, and Zinc Alloys"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-11T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 19)"
Technical Source: Watson research brief (Nernst equation applied to co-deposition, complexing agent potential shift, alloy Faraday constant, four major alloy systems)
Watson Flags: TWO OPEN — (1) Verify Cu standard potential shift from +0.34V to -1.17V via cyanide complexing — confirm the -1.17V figure against an authoritative electrochemistry reference. (2) Confirm zinc-cobalt composition target (0.5-1% Co) and its salt spray improvement factor vs. pure zinc. Both non-blocking; values presented as "typical industry" with qualification.
Tyler Flags: ONE OPEN — Validate zinc-nickel 12-15% Ni composition target and the "3-5x salt spray vs. pure zinc" claim against current OEM specifications (GM, Ford, Chrysler). Non-blocking; value qualified as "typical."
Process Scope: Alloy electroplating co-deposition fundamentals (brass, bronze, zinc-nickel, zinc-cobalt)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AlloyPlating
  - ZincNickel
  - Brass
  - Bronze
  - ConstructionWorkup
---

# Poster # Poster #21 — Construction Workup
## Alloy Plating Fundamentals — Brass, Bronze, and Zinc Alloys

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-11*

This document is the construction workup for Poster #21. It translates Watson's research concept into a full design specification usable by Elara to engineer a generation prompt for Drew. Two Watson flags and one Tyler flag remain open — all non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Content source:** Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 19 — Alloy Plating Fundamentals).

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, and accent borders
- Line elements for the potential number line illustration (the hero visual)
- Circle shapes for element badges on the number line
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for alloy/metal icons (gear, shield, corrosion)
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Potential number line (Block B — HERO):** The horizontal number line showing standard reduction potentials and the complexing shift must be built from geometric shapes — a long horizontal line with positioned circles and labels. The "shift arrow" from Cu at +0.34V to Cu-CN at -1.17V is a curved or angled arrow. If a true curved arrow is difficult , use a straight dashed arrow with a label. The visual impact is the dramatic 1.5V shift.

2. **Four-system comparison table (Block D):** A four-column table with 6-7 rows. Built as alternating rectangles with text overlays. Established pattern from prior posters.

3. **Alloy Faraday equation (Block E):** A single equation in JetBrains Mono inside a callout box. Same treatment as Poster #16's counterflow rinse equation.

4. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

5. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

6. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

8. **Sub/superscript characters:** Unicode characters provided verbatim for Ni2+, Cu2+, Zn2+ notation.

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
| Amber | `#E8A020` | Brass and bronze accent, complexing shift arrow, warning elements |
| Teal | `#2EC4B6` | Zinc alloy accent, potential number line, equation highlight |
| Emerald | `#27AE60` | Corrosion protection benefits, salt spray improvement callouts |
| Coral | `#E05C5C` | Problem indicators, cathodic failure examples |
| Mid Slate | `#3A4055` | Table headers, divider lines, number line base |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, equation display background |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Metal badges on number line, neutral reference elements |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 12.5" — Zone 2/Zone 3 boundary
- 17.0" — Zone 3/Zone 4 boundary
- 28.5" — Zone 4/Zone 5 boundary
- 32.5" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

Build in this sequence. Each zone is a discrete group of elements. Complete one zone before moving to the next. **Group each zone (Ctrl+G / Cmd+G) after completing it.**

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — POTENTIAL NUMBER LINE + COMPLEXING SHIFT (2.9"–12.5" / ~9.6" tall)
  Block B: Horizontal potential number line (HERO illustration)
  Block C: The "aha moment" — complexing shift callout

ZONE 3 — KEY CONCEPT CALLOUT (12.5"–17.0" / ~4.5" tall)
  Block CC: Full-width callout — the 0.2V co-deposition rule

ZONE 4 — FOUR-SYSTEM COMPARISON TABLE (17.0"–28.5" / ~11.5" tall)
  Block D: Four-column alloy comparison table (brass, bronze, Zn-Ni, Zn-Co)

ZONE 5 — ALLOY FARADAY EQUATION + APPLICATIONS (28.5"–32.5" / ~4.0" tall)
  Block E: Equation display (left half)
  Block F: Applications callout (right half)

ZONE 6 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
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
- Size: 90 pt
- Color: `#F0EDE8`
- Letter spacing: Tight (spacing slider: approximately -4)
- Text (all caps):

> ALLOY PLATING FUNDAMENTALS

**BLOCK A — Subheading**

- Element type: Text box
- Position: X: 0.5". Y: immediately below headline baseline + 6 pt gap (approximately Y: 1.5")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 38 pt
- Color: `#E8A020` (Amber)
- Text:

> Brass, Bronze, and Zinc Alloys — Co-Deposition in Practice

**BLOCK A — Tagline**

- Element type: Text box
- Position: X: 0.5". Y: immediately below subheading baseline + 6 pt gap (approximately Y: 2.3")
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8`
- Transparency: 65%
- Text:

> Two metals. One bath. The electrochemistry that makes it possible.

---

### ZONE 2 — Potential Number Line + Complexing Shift (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 12.5" (~9.6" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE CO-DEPOSITION PRINCIPLE

---

**BLOCK B — Horizontal Potential Number Line**

Y: 3.8" to 10.5" (~6.7" available).

This is the poster's hero illustration. It shows a horizontal number line of standard reduction potentials with metal badges positioned at their natural potentials, and a dramatic shift arrow showing how cyanide complexing moves copper's potential from +0.34V down to -1.17V — bringing it within co-deposition range of zinc at -0.76V.

**Number line baseline:**
- Element type: Line (horizontal)
- Position: X: 1.5" to 22.5" (21.0" wide). Y: 7.0"
- Stroke: 3 pt, `#3A4055` (Mid Slate)

**Scale markers** (vertical tick marks at each 0.5V increment):
- Positions along the line from left to right: -2.0V, -1.5V, -1.0V, -0.5V, 0.0V, +0.5V, +1.0V, +1.5V
- Element type: Short vertical lines (0.4" tall)
- Stroke: 2 pt, `#3A4055`
- Labels below each tick: JetBrains Mono Regular, 14 pt, `#F0EDE8` at 60%

**End labels:**
- Left end: `ACTIVE (anodic)` — Barlow SemiBold, 16 pt, `#E05C5C` (Coral)
- Right end: `NOBLE (cathodic)` — Barlow SemiBold, 16 pt, `#E8A020` (Amber)

**Metal badges** (positioned on the number line at their standard potential):

Each badge is a circle with the element symbol inside:

| Metal | Symbol | Potential (V) | Badge Color | Position (X approx.) |
|---|---|---|---|---|
| Magnesium | Mg | -2.37 | `#3A4055` | 1.0" (off-scale left, with arrow) |
| Zinc | Zn | -0.76 | `#2EC4B6` (Teal) | 8.4" |
| Iron | Fe | -0.44 | `#C8D0D8` (Silver) | 10.6" |
| Nickel | Ni | -0.25 | `#C8D0D8` (Silver) | 11.9" |
| Tin | Sn | -0.14 | `#C8D0D8` (Silver) | 12.6" |
| Copper | Cu | +0.34 | `#E8A020` (Amber) | 15.9" |
| Silver | Ag | +0.80 | `#C8D0D8` (Silver) | 19.1" |
| Gold | Au | +1.50 | `#E8A020` (Amber) | 22.0" |

Each badge:
- Element type: Circle
- Diameter: 0.7"
- Fill: color per table above
- Text inside: Element symbol — Barlow Condensed ExtraBold, 18 pt, `#1A1F2E` (dark text on colored badge)
- Potential value label below badge: JetBrains Mono Regular, 12 pt, `#F0EDE8`
- Metal name label above badge: Inter Medium, 12 pt, `#F0EDE8`

**Copper shifted badge (Cu-CN complex):**
- Element type: Circle (dashed border)
- Diameter: 0.7"
- Position: X: 5.6" (at -1.17V on the scale). Y: same as other badges
- Fill: `#E8A020` at 30% opacity (ghost version of copper)
- Border: 2 pt dashed, `#E8A020`
- Text inside: `Cu*` — Barlow Condensed ExtraBold, 16 pt, `#E8A020`
- Label below: `-1.17V (CN⁻ complex)` — JetBrains Mono Regular, 12 pt, `#E8A020`

**Shift arrow (THE "AHA MOMENT"):**
- Element type: Line with arrowhead (or curved arrow if The tool supports it)
- From: Cu badge at +0.34V (X: 15.9")
- To: Cu* ghost badge at -1.17V (X: 5.6")
- Y: 5.5" (above the number line)
- Stroke: 3 pt dashed, `#E8A020`
- Arrowhead: pointing left
- Label centered above the arrow:

> CYANIDE COMPLEXING SHIFTS Cu POTENTIAL BY 1.51V

- Font: Barlow SemiBold, 18 pt, `#E8A020`

**Co-deposition zone highlight:**
- Element type: Rectangle (semi-transparent highlight band)
- Position: Centered on the Zn badge. X: 6.5" to 10.5" (approximately 0.2V on either side of Zn)
- Width: 4.0". Height: 2.0" (spans above and below the number line)
- Y: 6.0" to 8.0"
- Fill: `#2EC4B6` at 10% opacity
- Border: 1 pt dashed, `#2EC4B6`
- Label inside (top): `CO-DEPOSITION ZONE` — Barlow SemiBold, 14 pt, `#2EC4B6`
- Label inside (bottom): `~0.2V window` — JetBrains Mono Regular, 12 pt, `#2EC4B6`

---

**BLOCK C — Complexing Shift Explanation Callout**

Y: 10.0" to 12.2"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 10.0"
- Width: 23.0". Height: 2.2"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 10.0"
- Width: 0.06". Height: 2.2"
- Fill: `#E8A020` (Amber)

Body text:
- Element type: Text box
- Position: X: 0.8". Y: 10.2"
- Width: 22.4"
- Font: Inter Medium, 18 pt, `#F0EDE8`
- Line height: 150%
- Text:

> Copper at +0.34V and zinc at -0.76V are 1.10V apart — far too wide for co-deposition. Cyanide complexing shifts copper's deposition potential to -1.17V, placing it within the ~0.2V window of zinc. This is why brass plating requires a cyanide bath: the complexing agent is not optional — it is the electrochemistry that makes co-deposition possible.

Key fact (right-aligned at bottom of callout):
- Element type: Text box
- Position: X: 12.0". Y: 11.5"
- Width: 11.0"
- Font: JetBrains Mono Regular, 14 pt, `#E8A020`
- Alignment: Right
- Text:

> Free CN⁻ controls composition: more CN⁻ = more zinc in the alloy

---

### ZONE 3 — Co-Deposition Rule Callout

**Dimensions:** Full page width within margins. Y: 12.5" to 17.0" (~4.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 12.7"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE RULE

---

**BLOCK CC — Full-Width Principle Callout**

Y: 13.3" to 16.7"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 2.0". Y: 13.3"
- Width: 20.0". Height: 3.4"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Border: 2 pt, `#2EC4B6` (Teal)

**Principle statement (large text, centered):**
- Element type: Text box
- Position: Centered inside callout. Y: 13.8"
- Width: 18.0"
- Font: Barlow Condensed ExtraBold, 36 pt, `#F0EDE8`
- Alignment: Center
- Text:

> TWO METALS CAN ONLY CO-DEPOSIT WHEN THEIR DEPOSITION POTENTIALS ARE WITHIN ~0.2V OF EACH OTHER

**Explanation (below principle):**
- Element type: Text box
- Position: Centered inside callout. Y: 15.2"
- Width: 18.0"
- Font: Inter Regular, 18 pt, `#F0EDE8` at 70%
- Alignment: Center
- Text:

> If the potentials are too far apart, the more noble metal deposits preferentially and the less noble metal stays in solution. Complexing agents shift potentials to bring them into range.

---

### ZONE 4 — Four-System Comparison Table

**Dimensions:** Full page width within margins. Y: 17.0" to 28.5" (~11.5" tall).

---

**Section label:**
- Element type: Text box
- Position: Centered horizontally. Y: 17.2"
- Font: Barlow Condensed ExtraBold
- Size: 28 pt
- Color: `#F0EDE8`
- Alignment: Center
- Text:

> THE FOUR MAJOR ALLOY SYSTEMS

---

**BLOCK D — Comparison Table**

Y: 17.9" to 28.0" (~10.1" available).

This is a four-column comparison table with a header row and 7 data rows. Total width: 23.0" (within safe zone). Each column is 5.75" wide.

**Column headers (row 0):**

| Column | X Position | Label | Accent Color |
|---|---|---|---|
| Brass (Cu-Zn) | 0.5" | BRASS (Cu-Zn) | `#E8A020` (Amber) |
| Bronze (Cu-Sn) | 6.25" | BRONZE (Cu-Sn) | `#E8A020` (Amber) |
| Zinc-Nickel | 12.0" | ZINC-NICKEL | `#2EC4B6` (Teal) |
| Zinc-Cobalt | 17.75" | ZINC-COBALT | `#2EC4B6` (Teal) |

Each column header:
- Element type: Rectangle
- Width: 5.5". Height: 0.7"
- Fill: accent color per table above
- Text inside: Barlow Condensed ExtraBold, 20 pt, `#1A1F2E` (dark text on colored fill)
- Y: 17.9"

**Row labels and data** (rows 1-7, built as alternating-color rectangles with text overlays):

Row height: 1.2" each. Alternating fills: `#1E2435` (odd rows) and `#252B3D` (even rows).

Each row has a left-side label (Inter Medium, 14 pt, `#F0EDE8` at 60%) and four data cells (Inter Regular, 16 pt, `#F0EDE8`).

**Row 1 — Composition Target:**
- Label: `Composition`
- Brass: `60-80% Cu, bal. Zn`
- Bronze: `80-90% Cu, bal. Sn`
- Zn-Ni: `12-15% Ni, bal. Zn`
- Zn-Co: `0.5-1% Co, bal. Zn`

**Row 2 — Bath Type:**
- Label: `Bath Type`
- Brass: `Cyanide`
- Bronze: `Cyanide / stannate`
- Zn-Ni: `Alkaline or acid chloride`
- Zn-Co: `Alkaline or acid chloride`

**Row 3 — Complexing Agent:**
- Label: `Complexing Agent`
- Brass: `Free cyanide (NaCN)`
- Bronze: `Free cyanide + stannate`
- Zn-Ni: `Amines / ammonium`
- Zn-Co: `Amines / ammonium`

**Row 4 — Key Control Parameter:**
- Label: `Key Control`
- Brass: `Free CN⁻ controls Cu:Zn ratio → color`
- Bronze: `Cu:Sn ratio → white vs. yellow bronze`
- Zn-Ni: `Ni% in deposit → corrosion performance`
- Zn-Co: `Co% in deposit → passivation response`

**Row 5 — Primary Application:**
- Label: `Applications`
- Brass: `Decorative, hardware, furniture`
- Bronze: `Chrome substitute ("white bronze"), connectors`
- Zn-Ni: `Automotive, aerospace, cadmium replacement`
- Zn-Co: `Budget alternative to Zn-Ni, fasteners`

**Row 6 — Corrosion Advantage:**
- Label: `Corrosion Edge`
- Brass: `Aesthetic only — limited corrosion value`
- Bronze: `Aesthetic + mild corrosion barrier`
- Zn-Ni: `3-5x salt spray hours vs. pure zinc` (use Emerald `#27AE60` for this text)
- Zn-Co: `1.5-2x salt spray hours vs. pure zinc` (use Emerald `#27AE60` for this text)

**Row 7 — Industry Trend:**
- Label: `Trend`
- Brass: `Stable — decorative demand consistent`
- Bronze: `Growing — chrome-free demand rising`
- Zn-Ni: `Growing fast — OEM spec adoption` (use Emerald `#27AE60` for this text)
- Zn-Co: `Moderate — cost-driven adoption`

---

### ZONE 5 — Alloy Faraday Equation + Applications

**Dimensions:** Full page width within margins. Y: 28.5" to 32.5" (~4.0" tall).

---

**BLOCK E — Alloy Faraday Equation** (left half, X: 0.5" to 11.5")

Y: 28.5" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 0.5". Y: 28.7"
- Width: 11.0". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 0.5". Y: 28.7"
- Width: 0.06". Height: 3.5"
- Fill: `#2EC4B6` (Teal)

Callout title:
- Element type: Text box
- Position: X: 0.8". Y: 28.9"
- Font: Barlow SemiBold, 20 pt, `#2EC4B6`
- Text:

> ALLOY FARADAY CONSTANT

**Equation (large display):**
- Element type: Text box
- Position: X: 0.8". Y: 29.6"
- Width: 10.4"
- Font: JetBrains Mono Regular, 24 pt, `#F0EDE8`
- Alignment: Center
- Text:

> F_alloy = 100 / [(W1/F1) + (W2/F2)]

**Variable definitions:**
- Element type: Text box
- Position: X: 0.8". Y: 30.5"
- Width: 10.4"
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Line height: 150%
- Text:

> W1, W2 = weight % of each metal in the alloy
> F1, F2 = electrochemical equivalent of each metal
> F_alloy = effective Faraday constant for the alloy

---

**BLOCK F — Why Alloy Plating Is Growing** (right half, X: 12.0" to 23.5")

Y: 28.5" to 32.3"

**Callout container:**
- Element type: Rounded rectangle
- Position: X: 12.0". Y: 28.7"
- Width: 11.5". Height: 3.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 6 pt

Left-border accent:
- Element type: Rectangle
- Position: X: 12.0". Y: 28.7"
- Width: 0.06". Height: 3.5"
- Fill: `#27AE60` (Emerald)

Callout title:
- Element type: Text box
- Position: X: 12.3". Y: 28.9"
- Font: Barlow SemiBold, 20 pt, `#27AE60`
- Text:

> WHY ALLOY PLATING IS GROWING

Bullet list:
- Element type: Text box
- Position: X: 12.3". Y: 29.5"
- Width: 10.9"
- Font: Inter Regular, 16 pt, `#F0EDE8`
- Line height: 150%
- Text:

> - Zinc-nickel replacing cadmium in aerospace and defense (ELV/RoHS compliance)
> - White bronze replacing hexavalent chrome in decorative markets
> - OEM specifications increasingly mandate alloy deposits over pure zinc
> - Alloy deposits offer tunable corrosion properties single metals cannot match

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

> This poster is an educational reference tool. Alloy compositions, potentials, and performance data are typical industry values. Specific bath chemistry, operating parameters, and corrosion performance depend on the proprietary additive system, substrate preparation, and test conditions. Consult your process supplier for application-specific guidance.

**Poster title:**
- Element type: Text box
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold
- Size: 16 pt
- Color: `#F0EDE8`
- Text:

> Alloy Plating Fundamentals — Brass, Bronze, and Zinc Alloys

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
| Zone 2 - Potential Number Line | Section label, number line, metal badges, shift arrow, co-deposition zone highlight, explanation callout |
| Zone 3 - Co-Deposition Rule | Section label, principle callout |
| Zone 4 - Alloy Comparison Table | Section label, four-column table with header and 7 data rows |
| Zone 5 - Equation and Applications | Alloy Faraday equation callout, "why growing" callout |
| Zone 6 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

After grouping, lock each completed zone (right-click > Lock) before proceeding to the next.

---

## Part 6 — Light Edition Color Remap Table

Duplicate the completed Dark edition page. Work through this table from top to bottom:

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table rules, dividers, number line base |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

Column header fills (Amber and Teal) become their darkened Light edition variants. Verify text inside column headers remains legible — may need `#F5F4F0` text override on darkened fills.

---

## Part 7 — Export Checklist

Six files per poster:

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Alloy Plating Fundamentals — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Alloy Plating Fundamentals — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Alloy Plating Fundamentals — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Alloy Plating Fundamentals — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Alloy Plating Fundamentals — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Alloy Plating Fundamentals — Light — Digital.pdf` | RGB | PDF Standard | No |

For 18x24" versions: duplicate the 24x36" design, use the resize feature, then verify all text meets the 14 pt body text minimum floor.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #21 — Alloy Plating Fundamentals — Construction Workup v1.0*
*2026-04-11*
