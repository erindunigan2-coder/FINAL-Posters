---
Project: Plating Posters Inc
Poster Number: 18
Title: "Deposit Thickness Testing — Methods, Ranges, and When to Use Each"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-06T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 18)"
  - "Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 17, supplementary unit conversion data)"
Technical Source: Watson research brief (XRF, coulometric, eddy current, magnetic gage, cross-section, ASTM standards); Tyler supplementary content (unit conversion ladder, Knoop minimum thickness)
Watson Flags: ONE OPEN — Verify ASTM B244 eddy current accuracy range and ASTM B568 XRF accuracy claims against current ASTM editions. Non-blocking; ranges presented as typical industry values.
Tyler Flags: NONE — Tyler's supplementary data integrated; full hardness/adhesion methods deferred to a possible future companion poster.
Process Scope: Deposit thickness measurement (universal — applies to every plated part)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DepositTesting
  - Thickness
  - QualityControl
  - ConstructionWorkup
---

# Poster # Poster #18 — Construction Workup
## Deposit Thickness Testing — Methods, Ranges, and When to Use Each

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-06*

This document is the construction workup for Poster #18. It combines Watson's thickness testing concept with Tyler's supplementary unit conversion data. The hero is a six-method comparison grid; the secondary feature is the unit conversion ladder. Designed to live above the QC bench and be referenced every time someone asks "which method should I use?"

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Content sources:**
- Watson — New Poster Concepts from CEF — 2026-04-06.md (Concept 18) — primary
- Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 17) — unit conversion ladder

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles for the six-method comparison grid (large data table)
- Rounded rectangles for callout boxes
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for tool/instrument icons (one per method)
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Six-method comparison grid (Block B — HERO):** Built as a 7-row × 6-column table (header row + 6 method rows). Or alternatively, six side-by-side method "cards" stacked vertically. The card-based approach is more visually compelling at a poster scale and allows each method to have its own icon and color accent. **Recommendation: build as 6 stacked horizontal method cards.**

2. **Method icons:** Each method gets a small icon (XRF gun, electrochemical cell, eddy current probe, magnetic gage, microscope, balance). Search the icon library; if not found, use simple geometric placeholders (the icon is decorative — the data is what matters).

3. **Unit conversion ladder (Block C):** Visual ladder/staircase showing equivalent thickness units. Built as five connected rectangles with conversion arrows between them. Straightforward .

4. **4 pt left-border accents on cards and callouts:** Same technique as all previous posters — narrow colored rectangle (~0.06" wide) flush against the left edge of each method card.

5. **Global Colors / swatch remap for Light edition:** Manual recolor required — duplicate page and work through remap table.

6. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. Ensure font is available. Substitute Courier Prime if unavailable.

7. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Open the design tool. Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- Page background: **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
- **Barlow Condensed ExtraBold** — headlines, section labels
- **Barlow SemiBold** — subheadings, method names, callout titles
- **Inter Regular** and **Inter Medium** — body text, descriptions
- **JetBrains Mono Regular** — ASTM numbers, accuracy values, unit conversions

### Step 4 — Set up color palette (save as Brand Colors)

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | Primary text |
| Amber | `#E8A020` | Coulometric (semi-destructive) accent |
| Teal | `#2EC4B6` | XRF (non-destructive, primary) accent |
| Emerald | `#27AE60` | Eddy Current, Magnetic Gage (non-destructive) accents |
| Coral | `#E05C5C` | Cross-section, Weigh-Strip-Weigh (destructive) accents |
| Mid Slate | `#3A4055` | Dividers, table headers, ladder backgrounds |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout fills, method card fills |
| Alt Row | `#252B3D` | Alternate ladder steps |
| Bright Silver | `#C8D0D8` | Coating layer in cross-section illustration |

### Step 5 — Set ruler guides

**Vertical guides:**
- 0.5" — left safe zone
- 23.5" — right safe zone

**Horizontal guides:**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 24.5" — Zone 2/Zone 3 boundary
- 32.5" — Zone 3/Zone 4 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — SIX-METHOD COMPARISON (2.9"–24.5" / ~21.6" tall)
  Block B: Six stacked horizontal method cards (HERO)
    Each card: icon, method name, ASTM #, principle, range, destructive flag, best for

ZONE 3 — UNIT CONVERSION + DECISION CALLOUT (24.5"–32.5" / ~8.0" tall)
  Block C: Unit conversion ladder (left half)
  Block D: "Which method should I use?" decision callout (right half)

ZONE 4 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block E: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Y: 0" to 2.9".

**BLOCK A — Headline**
- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`
- Letter spacing: -4
- Text:

> DEPOSIT THICKNESS TESTING

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.5". Width: 23.0"
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text:

> Methods, Ranges, and When to Use Each

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.2". Width: 23.0"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity
- Text:

> The most common QC measurement in the plating shop — done six different ways.

---

### ZONE 2 — Six-Method Comparison (HERO)

**Dimensions:** Y: 2.9" to 24.5" (~21.6" tall).

---

**Section label:**
- Position: Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 30 pt, `#F0EDE8`
- Alignment: Center
- Text:

> SIX METHODS — KNOW WHICH ONE TO PICK

---

**BLOCK B — Six Method Cards**

Y: 3.8" to 24.2" (~20.4" available). Six cards stacked vertically, each ~3.3" tall with 0.1" gaps.

**Card structure (used for all six methods):**

Each card is built as:
1. **Card container:** Rounded rectangle, X: 0.5", W: 23.0", H: 3.2", fill `#1E2435`, corner radius 6 pt
2. **Left accent bar:** Rectangle, X: 0.5", W: 0.06", H: 3.2", fill = method-specific color
3. **Method icon area:** Square zone, X: 0.8" to 2.8" (2.0" wide). Centered vertically in card.
4. **Method name:** Barlow Condensed ExtraBold, 28 pt, method color, X: 3.0", Y: top of card + 0.2"
5. **ASTM standard:** JetBrains Mono Regular, 16 pt, `#F0EDE8` at 70%, X: 3.0", below method name
6. **Principle (one line):** Inter Medium, 16 pt, `#F0EDE8`, X: 3.0", below ASTM
7. **Three data tags (right side of card):** Each tag is a small pill — JetBrains Mono Regular, 13 pt, on a `#3A4055` background pill
   - Range tag (e.g., `0.0001"–0.002"`)
   - Destructive/non-destructive tag
   - Speed tag
8. **"Best for" line:** Inter Regular, 14 pt, `#F0EDE8` at 80%, italic, X: 3.0", bottom of card

---

**Card 1 — XRF (X-Ray Fluorescence)** — Y: 3.8"

- Card fill: `#1E2435`. Left accent: `#2EC4B6` (Teal)
- Icon: Stylized XRF gun or radiation symbol. Color: `#2EC4B6`
- Method name: `XRF` — `#2EC4B6`
- ASTM: `ASTM B568`
- Principle: `Excites coating atoms with X-rays; measures characteristic fluorescence energy.`
- Tags: `Range: 0.000004"–0.002"` | `NON-DESTRUCTIVE` | `~1 min/reading`
- Best for: `Multi-layer plating, precious metals, production QC, any metal-on-metal`

---

**Card 2 — Coulometric Stripping** — Y: 7.2"

- Left accent: `#E8A020` (Amber)
- Icon: Electrochemical cell glyph
- Method name: `COULOMETRIC` — `#E8A020`
- ASTM: `ASTM B504`
- Principle: `Strips coating electrochemically; uses Faraday's Law to convert charge to thickness.`
- Tags: `Range: 0.00002"–0.002"` | `SEMI-DESTRUCTIVE` | `~2 min/reading`
- Best for: `High-accuracy single-layer measurement; calibration of XRF; small spot testing`

---

**Card 3 — Eddy Current** — Y: 10.6"

- Left accent: `#27AE60` (Emerald)
- Icon: Coil/probe glyph
- Method name: `EDDY CURRENT` — `#27AE60`
- ASTM: `ASTM B244`
- Principle: `Induces eddy currents in the substrate; measures coating-induced impedance change.`
- Tags: `Range: 0.0001"–0.002"` | `NON-DESTRUCTIVE` | `Instant`
- Best for: `Non-conductive coatings (anodize, paint) on conductive substrates`

---

**Card 4 — Magnetic Gage** — Y: 14.0"

- Left accent: `#27AE60` (Emerald)
- Icon: Magnet/probe glyph
- Method name: `MAGNETIC GAGE` — `#27AE60`
- ASTM: `ASTM B499`
- Principle: `Measures magnetic flux pull between probe and ferrous substrate through the coating.`
- Tags: `Range: 0.0004"+ (10 µm)` | `NON-DESTRUCTIVE` | `Instant`
- Best for: `Non-magnetic coatings (Zn, Cu, Ni-P, paint) on steel or iron`

---

**Card 5 — Cross-Section Microscopy** — Y: 17.4"

- Left accent: `#E05C5C` (Coral)
- Icon: Microscope glyph
- Method name: `CROSS-SECTION` — `#E05C5C`
- ASTM: `ASTM B487`
- Principle: `Cuts, mounts, polishes, and measures the coating directly under a calibrated microscope.`
- Tags: `Range: any thickness` | `DESTRUCTIVE` | `~30+ min/sample`
- Best for: `Referee method — calibrates all others; failure analysis; complex multilayer systems`

---

**Card 6 — Weigh-Strip-Weigh** — Y: 20.8"

- Left accent: `#E05C5C` (Coral)
- Icon: Balance/scale glyph
- Method name: `WEIGH-STRIP-WEIGH` — `#E05C5C`
- ASTM: `ASTM B767`
- Principle: `Weighs part, strips coating chemically, weighs again; calculates from area and density.`
- Tags: `Range: any uniform coating` | `DESTRUCTIVE` | `~15 min/sample`
- Best for: `Average coating weight on simple geometry; statistical sampling`

---

### ZONE 3 — Unit Conversion + Decision Callout

**Dimensions:** Y: 24.5" to 32.5" (~8.0" tall). Two-column layout.

---

**Section label:**
- Position: Centered horizontally. Y: 24.7"
- Font: Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`
- Alignment: Center
- Text:

> KNOW YOUR UNITS

---

**BLOCK C — Unit Conversion Ladder** (left half, X: 0.5" to 11.5")

Y: 25.4" to 31.8"

**Container:**
- Rounded rectangle, X: 0.5", Y: 25.4", W: 11.0", H: 6.4", fill `#1E2435`, radius 8 pt
- Left accent: 0.06" x 6.4", fill `#E8A020` (Amber)

**Title:**
- Position: X: 0.8". Y: 25.6"
- Font: Barlow SemiBold, 20 pt, `#E8A020`
- Text:

> THICKNESS UNIT LADDER

**Sub-title:**
- Position: X: 0.8". Y: 26.1"
- Font: Inter Regular, 13 pt, `#F0EDE8` at 70%
- Text:

> All five values below are EQUIVALENT — same thickness, different units.

**Ladder rows (5 stacked rows, each ~0.85" tall, X: 0.8" to 11.2"):**

Each row is a rectangle (W: 10.4", H: 0.85") alternating fill `#252B3D` and `#1A1F2E`.
Each row contains: unit name (left), value (right), conversion note (center, italic small text).

Row 1 (Y: 26.6"):
- Unit name: `INCH` — Barlow SemiBold, 18 pt, `#F0EDE8`, X: 1.0"
- Value: `0.0002"` — JetBrains Mono Regular, 22 pt, `#2EC4B6`, X: 8.5", right-aligned
- Note: `(common spec unit, USA)` — Inter Regular, 12 pt italic, `#F0EDE8` at 60%, centered

Row 2 (Y: 27.5"):
- Unit name: `TENTHS` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Value: `2 tenths` — JetBrains Mono Regular, 22 pt, `#2EC4B6`
- Note: `(1 tenth = 0.0001 inch)`

Row 3 (Y: 28.4"):
- Unit name: `MICRO-INCH` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Value: `200 µin` — JetBrains Mono Regular, 22 pt, `#2EC4B6`
- Note: `(common XRF/precious metals unit)`

Row 4 (Y: 29.3"):
- Unit name: `MICRON` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Value: `5.1 µm` — JetBrains Mono Regular, 22 pt, `#2EC4B6`
- Note: `(SI / international standard)`

Row 5 (Y: 30.2"):
- Unit name: `MIL` — Barlow SemiBold, 18 pt, `#F0EDE8`
- Value: `0.2 mil` — JetBrains Mono Regular, 22 pt, `#2EC4B6`
- Note: `(1 mil = 25.4 microns = 0.001 inch)`

**Conversion key (bottom of ladder):**
- Position: X: 0.8". Y: 31.2"
- Width: 10.4"
- Font: JetBrains Mono Regular, 13 pt, `#E8A020`
- Alignment: Center
- Text:

> 1 mil = 25.4 µm = 1000 µin   |   1 µm = 39.37 µin

---

**BLOCK D — "Which Method?" Decision Callout** (right half, X: 12.0" to 23.5")

Y: 25.4" to 31.8"

**Container:**
- Rounded rectangle, X: 12.0", Y: 25.4", W: 11.5", H: 6.4", fill `#1E2435`, radius 8 pt
- Left accent: 0.06" x 6.4", fill `#2EC4B6` (Teal)

**Title:**
- Position: X: 12.3". Y: 25.6"
- Font: Barlow SemiBold, 20 pt, `#2EC4B6`
- Text:

> WHICH METHOD SHOULD I USE?

**Decision rows (5 stacked decision tips):**

Each row uses Inter Regular 15 pt for the question (gray) and Inter Medium 15 pt for the answer (white). Question color: `#F0EDE8` at 70%. Answer color: `#F0EDE8`.

Row 1 (Y: 26.2"):
- `Need fast non-destructive readings on production parts? → ` (gray)
- `XRF` (white)

Row 2 (Y: 27.0"):
- `Coating on steel and you only need average thickness? → `
- `MAGNETIC GAGE`

Row 3 (Y: 27.8"):
- `Anodize or paint over aluminum? → `
- `EDDY CURRENT`

Row 4 (Y: 28.6"):
- `Need maximum accuracy or to settle a dispute? → `
- `CROSS-SECTION (referee)`

Row 5 (Y: 29.4"):
- `XRF reads questionable — need to verify? → `
- `COULOMETRIC`

**Critical reminder callout (bottom of box):**
- Position: X: 12.3". Y: 30.4"
- Width: 11.0"
- Font: Inter Medium, 14 pt, `#E8A020`
- Line height: 140%
- Text:

> EVERY method requires periodic calibration against a traceable standard. Cross-section is the only true referee — all others measure something INDIRECTLY proportional to thickness.

---

### ZONE 4 — Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer band background:**
- Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:**
- Position: X: 0.5". Y: 32.8". Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50%, center
- Text:

> Accuracy ranges shown are typical industry values. Performance depends on instrument calibration, coating system, substrate, operator skill, and ambient conditions. Always follow the relevant ASTM standard and your QMS procedure.

**Poster title:**
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> Deposit Thickness Testing — Methods, Ranges, and When to Use Each

**Series name:**
- Position: Centered. Y: 34.2"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70%, center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Position: X: 22.5". Y: 33.3". W: 0.83", H: 0.42", fill `#3A4055`
- Text inside: `[LOGO]` — 10 pt, `#F0EDE8` at 50%

**Version:**
- Position: X: 0.5". Y: 35.0"
- Font: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%
- Text:

> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Six Method Cards | Section label + all six method cards (each card pre-grouped) |
| Zone 3 - Unit Ladder | Ladder container, 5 rows, conversion key |
| Zone 3 - Which Method | Decision callout container, 5 decision rows, critical reminder |
| Zone 4 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

**Tip:** Build Card 1 fully, then duplicate it five times and modify each. This ensures consistent geometry and saves significant build time.

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Card and callout fills |
| `#252B3D` | `#E8E8F0` | Alternate ladder rows |
| `#0D1020` | `#1A1F2E` | Footer strip |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Pills, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

---

## Part 7 — Export Checklist

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Thickness Testing — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Thickness Testing — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Thickness Testing — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Thickness Testing — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Thickness Testing — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Thickness Testing — Light — Digital.pdf` | RGB | PDF Standard | No |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #18 — Deposit Thickness Testing — Construction Workup v1.0*
*2026-04-06*
