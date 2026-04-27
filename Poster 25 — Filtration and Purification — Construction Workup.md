---
Project: Plating Posters Inc
Poster Number: 25
Title: "Filtration and Purification — Keeping Your Bath Clean"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-24T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - General industry knowledge (filtration methods, carbon treatment, dummy plating, purification procedures)
Technical Source: General industry knowledge — filter types, micron ratings, turnover rates, carbon treatment procedures, dummy plating protocols. Products Finishing and NASF/AESF reference material on bath maintenance and purification.
Watson Flags: TWO OPEN — (1) Confirm recommended filter turnover rates (3-5 turnovers/hour for nickel, higher for chrome) against current industry guidance. (2) Verify activated carbon treatment dosage ranges (1-3 g/L for batch treatment) and contact time recommendations. Both non-blocking; values presented as industry-typical.
Tyler Flags: ONE OPEN — (1) Validate the carbon treatment procedure sequence (pH adjust -> carbon addition -> mix -> filter) against Tyler's current lab procedures, particularly the pH adjustment step for nickel baths. Non-blocking.
Process Scope: Filtration equipment, purification methods, and bath maintenance for plating solutions (universal — applies to every plating process)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Filtration
  - Purification
  - CarbonTreatment
  - BathMaintenance
  - ConstructionWorkup
---

# Poster #25 — Construction Workup
## Filtration and Purification — Keeping Your Bath Clean

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-24*

This document is the construction workup for Poster #25. It covers the two pillars of bath maintenance that most plating shops underinvest in: mechanical filtration and chemical purification. This poster makes the case that filtration is not overhead — it is quality insurance — and gives operators the reference data to do it right.

> **Workflow note:** Poster generation uses claude.ai chat (SVG/HTML visual artifacts). These specs feed the Claude Chat Generation Prompt engineered by Elara. If Drew approves the generated output, it proceeds to final production.

**What makes this poster valuable:** Contamination is the #1 cause of plating defects. Poster #7 (Metallic Contamination) covers the "what" — this poster covers the "how do we prevent and remove it." Together, they form a complete contamination management reference. Every plating shop has filters; most are undersized, under-maintained, or using the wrong media.

**Who it's for:** Tank operators, maintenance staff, process engineers, and lab technicians. The operator learns when to change a filter; the engineer learns how to size a system; the lab tech learns when carbon treatment is needed.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for callout boxes, table rows, filter comparison cards, and accent borders
- Simple shapes for filter cross-section diagrams (cylinders from rectangles, flow arrows from triangles)
- Color fills set to exact hex values
- Background page color set to exact hex
- Icon library search for filter, water drop, beaker, wrench icons
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Filter type comparison (Block B — HERO):** Four tall cards showing filter types. Each card has a simplified cross-section diagram built from rectangles and lines (cartridge = tall narrow rectangle with internal pleated lines; bag = trapezoidal shape; pump-and-filter = rectangle with circle pump symbol). These are schematic, not photorealistic.

2. **Carbon treatment flowchart (Block E):** A horizontal step sequence (6 steps) connected by arrows. Built from rounded rectangles with arrow lines between them. Same pattern as Poster #1's surface prep flowchart.

3. **4 pt left-border accents on callout boxes:** Same technique as all previous posters.

4. **Global Colors / swatch remap for Light edition:** Manual recolor per remap table.

5. **JetBrains Mono font:** Ensure font is available. Fallback: Courier Prime.

6. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall at document creation.

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts
Same as all previous posters (Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular).

### Step 4 — Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Warning thresholds, pressure differential callouts, caution indicators |
| Teal | `#2EC4B6` | Filtration flow indicators, micron ratings, turnover rates |
| Emerald | `#27AE60` | Best practice callouts, clean bath indicators, carbon treatment success |
| Coral | `#E05C5C` | Contamination indicators, neglect warnings, critical maintenance alerts |
| Mid Slate | `#3A4055` | Table headers, filter diagram outlines, divider lines |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, filter card backgrounds |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Filter media representations, neutral elements |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 11.5" — Zone 2/Zone 3 boundary
- 16.0" — Zone 3/Zone 4 boundary
- 22.0" — Zone 4/Zone 5 boundary
- 27.5" — Zone 5/Zone 6 boundary
- 32.5" — Zone 6/Zone 7 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — FILTER TYPE COMPARISON (2.9"–11.5" / ~8.6" tall)
  Block B: Four filter type cards (HERO) — Cartridge, Bag, Carbon Canister, Pump/Filter Unit
  Block C: Micron rating quick reference strip

ZONE 3 — TURNOVER RATES AND SIZING (11.5"–16.0" / ~4.5" tall)
  Block D: Turnover rate table by process type
  Block DD: Sizing formula callout

ZONE 4 — CARBON TREATMENT PROCEDURE (16.0"–22.0" / ~6.0" tall)
  Block E: Step-by-step carbon treatment flowchart
  Block EE: Carbon treatment do's and don'ts (side by side)

ZONE 5 — DUMMY PLATING AND ADVANCED PURIFICATION (22.0"–27.5" / ~5.5" tall)
  Block F: Dummy plating reference (left half)
  Block G: Advanced purification methods overview (right half)

ZONE 6 — MAINTENANCE SCHEDULE (27.5"–32.5" / ~5.0" tall)
  Block H: Filter maintenance schedule table
  Block HH: Warning signs callout

ZONE 7 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block J: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A — Headline**

- Position: X: 0.5". Y: 0.5"
- Font: Barlow Condensed ExtraBold, 84 pt, `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> FILTRATION AND PURIFICATION

**BLOCK A — Subheading**

- Position: X: 0.5". Y: ~1.5"
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text:

> Keeping Your Bath Clean — The Most Underrated Quality Tool in the Shop

**BLOCK A — Tagline**

- Position: X: 0.5". Y: ~2.3"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text:

> If you can see particles in your solution, your filter stopped working two weeks ago.

---

### ZONE 2 — Filter Type Comparison (HERO)

**Dimensions:** Y: 2.9" to 11.5" (~8.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> FILTER TYPES — KNOW YOUR OPTIONS

---

**BLOCK B — Four Filter Type Cards**

Y: 3.8" to 10.5" (~6.7" tall). Four tall cards evenly spaced.

Each card:
- Width: 5.5". Height: 6.5"
- Fill: `#1E2435`. Corner radius: 6 pt. Border: 2 pt in accent color.

| Card | X | Accent | Filter Type |
|---|---|---|---|
| 1 | 0.5" | `#2EC4B6` | Cartridge Filter |
| 2 | 6.25" | `#E8A020` | Bag Filter |
| 3 | 12.0" | `#27AE60` | Carbon Canister |
| 4 | 17.75" | `#E05C5C` | Pump & Filter Unit |

**Inside each card (top to bottom):**

*Card 1 — Cartridge Filter:*

Title:
- Font: Barlow Condensed ExtraBold, 22 pt, `#2EC4B6`
- Text: `CARTRIDGE FILTER`

Diagram area (centered, 4.0" wide x 2.5" tall):
- Simplified cross-section: tall narrow rectangle (housing) with internal pleated lines (zigzag pattern) representing filter media. Inlet arrow on one side, outlet arrow on other side.
- Housing outline: `#3A4055`, 2 pt. Media: `#C8D0D8`. Flow arrows: `#2EC4B6`.

Specs:
- Font: JetBrains Mono Regular, 13 pt, `#F0EDE8`
- Text:

> Rating: 1–50 micron
> Type: Depth or pleated
> Flow: Low to moderate

Description:
- Font: Inter Regular, 14 pt, `#F0EDE8`
- Text:

> The workhorse. Disposable or cleanable. Depth cartridges trap particles throughout the media; pleated cartridges capture on the surface for higher flow rates. Most common in individual tank filtration.

Best for:
- Font: Inter Medium, 13 pt, `#2EC4B6`
- Text: `Best for: Individual tank circulation loops`

*Card 2 — Bag Filter:*

Title: `BAG FILTER` — `#E8A020`

Diagram: Trapezoidal shape (bag) inside rectangular housing. Inlet at top, outlet at bottom.

Specs:
> Rating: 1–200 micron
> Type: Surface capture
> Flow: High volume

Description:
> Lower cost per change than cartridges. Higher flow capacity. Less efficient at fine filtration but excellent for heavy-solids baths (barrel plating, acid copper). Easy to change — just pull the bag.

Best for: `Best for: High-flow, heavy-particle applications`

*Card 3 — Carbon Canister:*

Title: `CARBON CANISTER` — `#27AE60`

Diagram: Cylindrical vessel (rectangle with rounded top) filled with small dots representing granular activated carbon. Inlet at bottom, outlet at top.

Specs:
> Media: Granular activated carbon
> Purpose: Organic removal
> Method: Continuous or batch

Description:
> Removes organic contamination — brightener breakdown products, oil, surfactant residue. Continuous carbon filtration runs solution through a GAC bed 24/7. Batch carbon treatment uses powdered carbon mixed directly into the bath, then filtered out.

Best for: `Best for: Organic contamination control (nickel, copper)`

*Card 4 — Pump & Filter Unit:*

Title: `PUMP & FILTER UNIT` — `#E05C5C`

Diagram: Rectangle (pump symbol with circle) connected by lines to rectangle (filter housing). Arrows showing flow direction. Return line back to tank.

Specs:
> Pump type: Centrifugal (mag-drive) or air-operated
> Media: Cartridge or bag (interchangeable)
> Flow: Sized to tank volume

Description:
> The complete package — pump, housing, and filter media as an integrated unit. Mag-drive pumps are standard for corrosive plating solutions. Air-operated diaphragm pumps for viscous or heated solutions. Size the pump to achieve target turnover rate.

Best for: `Best for: Dedicated tank filtration systems`

---

**BLOCK C — Micron Rating Quick Reference Strip**

Y: 10.7" to 11.3" (~0.6" tall)

Horizontal strip with four data points:

- Element type: Rounded rectangle
- Position: X: 0.5". Y: 10.7"
- Width: 23.0". Height: 0.5"
- Fill: `#252B3D`. Corner radius: 4 pt.

Four entries evenly spaced:

| Entry | Color | Text |
|---|---|---|
| 1 | `#2EC4B6` | `1 micron = fine Ni/Cr filtration` |
| 2 | `#27AE60` | `5 micron = standard plating filtration` |
| 3 | `#E8A020` | `10-25 micron = acid copper / barrel` |
| 4 | `#E05C5C` | `>25 micron = coarse pre-filtration only` |

Font: JetBrains Mono Regular, 13 pt, respective colors.

---

### ZONE 3 — Turnover Rates and Sizing

**Dimensions:** Y: 11.5" to 16.0" (~4.5" tall).

---

**Section label:**
- Centered horizontally. Y: 11.7"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> HOW MUCH FILTRATION IS ENOUGH?

---

**BLOCK D — Turnover Rate Table**

Y: 12.3" to 15.3" (~3.0" tall). Full safe zone width.

Header row:
- Fill: `#3A4055`. Barlow SemiBold, 14 pt, `#F0EDE8`.
- Labels: `Process` | `Minimum Turnovers/Hour` | `Target` | `Filter Rating` | `Notes`

| Process | Min | Target | Rating | Notes |
|---|---|---|---|---|
| Watts nickel (bright) | 3 | 5 | 1-5 micron | Continuous; carbon canister recommended |
| Hard chrome | 2 | 3 | 5-10 micron | Trivalent chrome higher — consult supplier |
| Acid copper | 2 | 3-4 | 5-10 micron | Carbon treatment as needed for organics |
| Zinc (acid chloride) | 2 | 3 | 5-10 micron | Filter before and after carbon treatment |
| Zinc (alkaline) | 1 | 2-3 | 10-25 micron | Lower requirements; watch for carbonate buildup |
| Electroless nickel | 3 | 10-20 | 1-5 micron | Critical — particles nucleate out-plating; aggressive filtration required |
| Gold / Precious metals | 3 | 5 | 1 micron | Filter media must be compatible with cyanide |

Data font: Inter Regular, 14 pt, `#F0EDE8`. Process names: Inter Medium, `#F0EDE8`. Target values in `#27AE60`. Alternating rows: `#1E2435` / `#252B3D`.

---

**BLOCK DD — Sizing Formula Callout**

Y: 15.5" to 15.8"

- Position: Centered, Y: 15.5"
- Element type: Rounded rectangle
- Width: 15.0". Height: 0.5". Fill: `#252B3D`. Corner radius: 4 pt.
- Text (centered inside):
- Font: JetBrains Mono Regular, 16 pt, `#E8A020`
- Text:

> Pump flow rate (GPM) = Tank volume (gal) x Turnovers/hr / 60

---

### ZONE 4 — Carbon Treatment Procedure

**Dimensions:** Y: 16.0" to 22.0" (~6.0" tall).

---

**Section label:**
- Centered horizontally. Y: 16.2"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text:

> CARBON TREATMENT — THE ORGANIC DETOX

---

**BLOCK E — Step-by-Step Flowchart**

Y: 16.8" to 19.0" (~2.2" tall). A horizontal sequence of 6 steps connected by arrows.

Each step:
- Element type: Rounded rectangle
- Width: 3.3". Height: 1.8"
- Fill: `#1E2435`. Corner radius: 6 pt. Border: 2 pt.
- Gap between steps: 0.3" (arrow fills the gap)
- Arrow: Triangle element, `#C8D0D8`, pointing right

Steps arranged in two rows of 3 (if single row is too cramped):

Row 1 (Y: 16.8"):

| Step | Border Color | Title | Body |
|---|---|---|---|
| 1 | `#2EC4B6` | `ANALYZE` | Test Hull cell for organic symptoms: hazy deposits, skip plate, reduced ductility |
| 2 | `#E8A020` | `ADJUST pH` | Lower pH to 3.0–3.5 with dilute sulfuric acid (nickel) — promotes iron co-precipitation and maximizes carbon adsorption efficiency. Use nickel carbonate to raise pH back to operating range after filtering. |
| 3 | `#27AE60` | `ADD CARBON` | Add 2-5 g/L powdered activated carbon. Stir thoroughly for 2-4 hours minimum (overnight for heavy organic loading) |

Row 2 (Y: 19.0"):

| Step | Border Color | Title | Body |
|---|---|---|---|
| 4 | `#27AE60` | `FILTER` | Filter through 1-5 micron media to remove all carbon particles — carbon left in = rough deposits |
| 5 | `#E8A020` | `RE-ADJUST` | Raise pH to operating range with nickel carbonate. Replenish ALL organic additives — brighteners, carrier, and wetting agent (carbon removes all organics). |
| 6 | `#2EC4B6` | `VERIFY` | Run Hull cell to confirm organic removal. Deposit should be bright and ductile across panel. |

Step title: Barlow SemiBold, 16 pt, border color.
Step body: Inter Regular, 12 pt, `#F0EDE8`.
Step number badge (small circle, top-left of each step): Barlow Condensed ExtraBold, 16 pt, `#1A1F2E` on accent-color circle fill.

---

**BLOCK EE — Do's and Don'ts** (side by side, below flowchart)

Y: 21.0" to 21.8" (~0.8" tall, compact)

Two callout strips:

**Left — Do:**
- Width: 11.0". Fill: `#1E2435`. Left-border: `#27AE60`.
- Title: `DO` — Barlow SemiBold, 16 pt, `#27AE60`
- Bullets: Inter Regular, 13 pt, `#F0EDE8`
- Text:

> - Test Hull cell BEFORE and AFTER treatment  - Add wetting agent after filtering  - Use food-grade or reagent-grade carbon  - Filter until solution runs clear through white filter pad

**Right — Don't:**
- X: 12.0". Width: 11.5". Fill: `#1E2435`. Left-border: `#E05C5C`.
- Title: `DON'T` — Barlow SemiBold, 16 pt, `#E05C5C`
- Text:

> - Return bath to service without removing ALL carbon by filtration  - Skip the post-treatment pH adjustment back to operating range  - Use carbon treatment as a substitute for proper filtration  - Treat a bath that has metallic contamination — carbon won't help

---

### ZONE 5 — Dummy Plating and Advanced Purification

**Dimensions:** Y: 22.0" to 27.5" (~5.5" tall).

---

**BLOCK F — Dummy Plating Reference** (left half, X: 0.5" to 11.5")

Y: 22.0" to 27.3"

**Callout container:**
- Width: 11.0". Height: 5.0". Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border accent: `#2EC4B6` (Teal)

Title: `DUMMY PLATING (ELECTROLYTIC PURIFICATION)` — Barlow SemiBold, 18 pt, `#2EC4B6`

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> Dummy plating removes metallic contaminants by plating them out on a sacrificial cathode. The cathode (corrugated steel sheet for maximum surface area) is run at LOW current density — 2-5 ASF — so contaminant metals deposit preferentially over the desired metal.

Key parameters (JetBrains Mono Regular, 13 pt):

> Current density: 2-5 ASF
> Cathode: Corrugated mild steel
> Duration: 4-24 hours (Hull cell to monitor)
> Removes: Cu, Zn, Pb, Cd (metals more noble than Ni at low CD)

Callout (Inter Medium, 14 pt, `#E8A020`):

> Run the dummy at LCD — you want the contaminants, not good nickel. High CD defeats the purpose.

---

**BLOCK G — Advanced Purification Methods** (right half, X: 12.0" to 23.5")

Y: 22.0" to 27.3"

**Callout container:**
- Width: 11.5". Height: 5.0". Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border accent: `#E8A020` (Amber)

Title: `ADVANCED PURIFICATION METHODS` — Barlow SemiBold, 18 pt, `#E8A020`

Four mini-cards stacked vertically inside:

| Method | Description |
|---|---|
| **Permanganate treatment** | Oxidizes organics that carbon cannot remove. Potassium permanganate added, reacted, then excess removed by carbon treatment and filtration. Used when carbon alone fails. |
| **Hydrogen peroxide treatment** | Oxidizes dissolved metallic impurities (Fe²⁺ to Fe³⁺ for precipitation). Must control pH and dosage carefully — excess peroxide damages some brighteners. |
| **Electrodialysis** | Selective ion-exchange membranes remove contaminants while retaining bath chemicals. Capital-intensive but effective for high-value baths (gold, palladium). |
| **Freezing (carbonate removal)** | For alkaline zinc: cool bath to precipitate sodium carbonate. Filter or decant. Simple but effective for carbonate-heavy baths. |

Method name: Inter Medium, 14 pt, `#E8A020`.
Description: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 6 — Maintenance Schedule

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**BLOCK H — Filter Maintenance Schedule Table**

Y: 27.5" to 31.0" (~3.5" tall). Left two-thirds (X: 0.5" to 16.0").

Section label:
- Font: Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `MAINTENANCE SCHEDULE`

Table (6 rows):

| Task | Frequency | Notes |
|---|---|---|
| Check filter pressure differential | Daily | Replace cartridge/bag when delta-P exceeds manufacturer spec |
| Inspect filter housing seals | Weekly | Bypass leaks defeat the filter entirely |
| Change cartridge/bag filters | As needed (pressure) | Do NOT run on a calendar — run on pressure differential |
| Carbon canister media replacement | Monthly or by Hull cell | Replace when Hull cell shows organic symptoms returning |
| Clean pump strainer / inlet screen | Weekly | Clogged strainer starves the pump |
| Full system inspection | Quarterly | Check pump seals, hose connections, housing cracks |

Header: Barlow SemiBold, 14 pt, `#F0EDE8` on `#3A4055`. Data: Inter Regular, 14 pt, `#F0EDE8`. Frequency values in `#E8A020`. Alternating rows.

---

**BLOCK HH — Warning Signs Callout** (right third, X: 16.5" to 23.5")

Y: 27.5" to 31.0"

- Width: 7.0". Height: 3.3". Fill: `#1E2435`. Corner radius: 6 pt.
- Left-border: `#E05C5C`

Title: `YOUR FILTER IS FAILING WHEN...` — Barlow SemiBold, 16 pt, `#E05C5C`

Bullets (Inter Regular, 15 pt, `#F0EDE8`, line height 145%):

> - Rough deposits appear that weren't there last week
> - Filter pressure gauge reads zero (bypass or clogged)
> - Solution clarity decreases visibly
> - Hull cell panel shows pitting or roughness
> - Flow rate from return line drops noticeably
> - You can't remember the last filter change

Key callout below (JetBrains Mono Regular, 13 pt, `#E05C5C`):

> The cheapest filter change you'll ever do is the one you do on time.

---

### ZONE 7 — Footer Band

**Dimensions:** Full page width. Y: 32.5" to 36.0" (~3.5" tall).

Standard footer per series convention:

**Footer band background:** Rectangle, X: 0", Y: 32.5", Width: 24.0", Height: 3.5", Fill: `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, centered:

> This poster is an educational reference tool. Filter types, turnover rates, and purification procedures are typical industry values. Specific filtration requirements, carbon treatment dosages, and maintenance intervals vary by process chemistry and equipment manufacturer. Consult your chemical supplier and filter manufacturer for application-specific guidance.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`:
> Filtration and Purification — Keeping Your Bath Clean

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, centered:
> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", 0.83" x 0.42", Fill: `#3A4055`, `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%:
> v1.0 — 2026

---

## Part 5 — Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Filter Types | Section label, four filter cards, micron rating strip |
| Zone 3 - Turnover Rates | Section label, turnover rate table, sizing formula |
| Zone 4 - Carbon Treatment | Section label, six-step flowchart, do's and don'ts |
| Zone 5 - Advanced Purification | Dummy plating reference, advanced methods callout |
| Zone 6 - Maintenance | Maintenance schedule table, warning signs callout |
| Zone 7 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout box fills, filter card backgrounds |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds, micron strip |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber accent elements |
| `#2EC4B6` | `#1A8C82` | Teal accent elements |
| `#27AE60` | `#1E7A47` | Emerald accent elements |
| `#E05C5C` | `#B83E3E` | Coral accent elements |
| `#3A4055` | `#D0D4DE` | Table headers, filter outlines, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver — **unchanged** |

---

## Part 7 — Export Checklist

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Filtration and Purification — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Filtration and Purification — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Filtration and Purification — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Filtration and Purification — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Filtration and Purification — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Filtration and Purification — Light — Digital.pdf` | RGB | PDF Standard | No |

---

## Design Notes

This poster pairs naturally with Poster #7 (Metallic Contamination). Together they form the "contamination management duo" — #7 tells you what the contaminants are and what damage they cause; #25 tells you how to prevent and remove them. A shop that hangs both posters side by side has a complete contamination reference wall.

The carbon treatment flowchart (Zone 4) is the poster's most practically actionable section. Many shops know they should do carbon treatments but fumble the procedure — particularly the pH adjustment step and the wetting agent replenishment. Getting these details on the wall prevents the two most common carbon treatment mistakes.

The "Your filter is failing when..." callout (Zone 6) is deliberately blunt. Filtration is one of those areas where shops let maintenance slide because nothing seems wrong until everything is suddenly wrong. The callout's tone matches the shop-floor reality: if you can't remember the last filter change, you've already waited too long.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #25 — Filtration and Purification — Construction Workup v1.0*
*2026-04-24*
