---
Project: Plating Posters Inc
Poster Number: 20
Title: "Precious Metals Plating — Gold and Silver Quick Reference"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-07T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 18 — Precious Metals)"
Technical Source: Tyler research brief (gold and silver bath types, strike requirements, efficiency ranges, troy vs. avoirdupois unit differences, sulfite stability)
Watson Flags: ONE OPEN — Confirm sulfite gold pH stability floor (pH 8.0) and verify hard gold cathode efficiency range (25–35%) against current proprietary bath datasheets. Non-blocking; values clearly attributed as "typical."
Tyler Flags: ONE OPEN — Confirm troy oz vs. avdp oz unit convention used in shop assays (this is the same convention question raised in Tyler's PRE-LM-010B queue). Non-blocking; both values printed verbatim with conversion note.
Process Scope: Gold and silver electroplating reference data (decorative, electronic, and engineering applications)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PreciousMetals
  - GoldPlating
  - SilverPlating
  - ConstructionWorkup
---

# Poster # Poster #20 — Construction Workup
## Precious Metals Plating — Gold and Silver Quick Reference

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-07*

This document is the construction workup for Poster #20, drawn directly from Tyler's CEF research brief (Concept 18). It provides shop-floor-grade reference data for gold and silver plating — bath types, parameter ranges, the mandatory silver strike rule, and the troy/avoirdupois unit pitfall that has cost more than one lab a costly assay error.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

This poster is structured as a **side-by-side reference card** — Gold on the left, Silver on the right — with a shared header, a shared footer, and three full-width "rules of the trade" callouts at the bottom. It is intended to live in a precious-metals lab or engineering office.

**Content source:** Tyler — New Poster Concepts from CEF — 2026-04-06.md (Concept 18), supplemented by general industry knowledge of cyanide and sulfite gold/silver chemistries.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Side-by-side two-column layout with distinct accent colors per column (gold = Amber, silver = Bright Silver)
- Comparison tables built from rectangle row backgrounds + text boxes (no native table tool needed)
- Full-width callout strips for the "rules of the trade"
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag for Elara

1. **Two parallel comparison tables (Blocks B and C):** Each table has 5 rows × 4 columns. Build as alternating-fill row rectangles with text boxes layered on top. Same technique used in Posters #11 and #18.

2. **Troy vs. avoirdupois unit callout (Block E):** This is the high-value teaching moment. Build as a dedicated full-width callout with two large numbers ("31.1 g" and "28.35 g") set in JetBrains Mono so the digits align cleanly.

3. **4 pt left-border accents on callout boxes:** Same technique as all previous posters — narrow colored rectangle (~0.06" wide) flush against the left edge of each callout box.

4. **Global Colors / swatch remap for Light edition:** No Global Colors system is available. Light edition requires duplicating the page and manually recoloring per the remap table in Part 6.

5. **JetBrains Mono font:** The generation tool may not include JetBrains Mono natively. **Ensure font is available.** Substitute **Courier Prime** if unavailable.

6. **Print size — 24x36":** Set to exactly 24 inches wide by 36 inches tall.

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
- **Barlow SemiBold** — all subheadings, callout titles, table headers
- **Inter Regular** and **Inter Medium** — all body text and table cell content
- **JetBrains Mono Regular** — all numeric data, parameter values, and version number

### Step 4 — Set up color palette (save as Brand Colors )

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Gold column accents, gold-bath rows |
| Teal | `#2EC4B6` | Strike-rule callout, neutral data accents |
| Emerald | `#27AE60` | Soft gold efficiency highlights, "do this" callouts |
| Coral | `#E05C5C` | Hard gold low-efficiency warnings, "don't do this" callouts |
| Mid Slate | `#3A4055` | Table headers, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, comparison table backgrounds |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Silver column accents, silver-bath rows |
| Pale Amber | `#F5C870` | Soft accent for gold sub-rows |

### Step 5 — Set ruler guides

**Vertical guides (from left edge):**
- 0.5" — left safe zone margin
- 11.75" — column gutter centerline (0.25" gutter on each side)
- 12.25" — right column left edge
- 23.5" — right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" — top safe zone margin
- 2.9" — Zone 1/Zone 2 boundary
- 22.5" — Zone 2/Zone 3 boundary
- 32.5" — Zone 3/Zone 4 boundary
- 35.5" — bottom safe zone margin

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline

ZONE 2 — TWO-COLUMN COMPARISON (2.9"–22.5" / ~19.6" tall)
  LEFT COLUMN (X: 0.5"–11.75"):
    Block B: GOLD — bath comparison table + key parameters
  RIGHT COLUMN (X: 12.25"–23.5"):
    Block C: SILVER — bath comparison table + key parameters

ZONE 3 — RULES OF THE TRADE (22.5"–32.5" / ~10.0" tall)
  Block D: The Silver Strike Rule (full-width callout)
  Block E: Troy vs. Avoirdupois — the assay-error pitfall (full-width callout)
  Block F: Sulfite Gold pH Stability + Hard vs. Soft Gold Efficiency (paired callouts)

ZONE 4 — FOOTER BAND (32.5"–36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A — Headline**
- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 96 pt, `#F0EDE8`
- Letter spacing: -4
- Text:

> PRECIOUS METALS

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.6". Width: 23.0"
- Font: Barlow SemiBold, 40 pt, `#E8A020` (Amber)
- Text:

> Gold and Silver — Quick Reference

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.3". Width: 23.0"
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity
- Text:

> A wrong assay can cost more than a wrong recipe.

---

### ZONE 2 — Two-Column Comparison

**Dimensions:** Y: 2.9" to 22.5" (~19.6" tall). Two columns with 0.5" gutter.

---

#### LEFT COLUMN — BLOCK B: GOLD

X: 0.5" to 11.75" (11.25" wide)

**Column header bar:**
- Element type: Rectangle
- Position: X: 0.5". Y: 3.1". Width: 11.25". Height: 0.8"
- Fill: `#E8A020` (Amber)

Header text:
- Position: X: 0.7". Y: 3.25"
- Font: Barlow Condensed ExtraBold, 40 pt, `#1A1F2E`
- Text:

> GOLD (Au)

Atomic-data sub-line (right side of header bar):
- Position: X: 8.0". Y: 3.4". Width: 3.5". Right-aligned.
- Font: JetBrains Mono Regular, 14 pt, `#1A1F2E`
- Text:

> Z=79  |  ρ=19.3 g/cm³

---

**Bath comparison table — Gold**

Y: 4.1" to 13.5" (~9.4" tall). 5 bath rows + 1 header row = 6 rows.

**Table header row:**
- Element type: Rectangle, X: 0.5", Y: 4.1", W: 11.25", H: 0.6"
- Fill: `#3A4055`
- Headers (Barlow SemiBold, 13 pt, `#F0EDE8`):
  - `BATH TYPE` — X: 0.7", Y: 4.25"
  - `pH` — X: 4.5", Y: 4.25"
  - `CD (A/ft²)` — X: 5.8", Y: 4.25"
  - `EFF.` — X: 8.2", Y: 4.25"
  - `USE` — X: 9.4", Y: 4.25"

**Bath rows** (each 1.4" tall, alternating fills):

| Row | Bath | pH | CD (A/ft²) | Eff. | Use |
|-----|------|----|------------|------|-----|
| 1 | Alkaline cyanide | 9.0–13 | 1–10 | 95–100% | Decorative, color match |
| 2 | Neutral cyanide | 6.0–8.0 | 1–5 | 95–100% | Electronic, soft gold |
| 3 | Acid cyanide | 3.5–5.0 | 1–10 | 25–35% | Hard gold, contacts |
| 4 | Sulfite (non-CN) | 8.0–10 | 1–5 | 90–95% | Photoresist-compatible |
| 5 | Pure-gold strike | 8.0–10 | 5–20 | 30–60% | Adhesion strike |

Row build (repeat for each row, Y position incrementing by 1.4"):
- Row background rectangle: W: 11.25", H: 1.4"
  - Odd rows (1, 3, 5): Fill `#1E2435`
  - Even rows (2, 4): Fill `#252B3D`
- Bath name: Inter Medium, 15 pt, `#E8A020`. Position: X: 0.7", vertically centered in row.
- pH value: JetBrains Mono Regular, 14 pt, `#F0EDE8`. Position: X: 4.5".
- CD value: JetBrains Mono Regular, 14 pt, `#F0EDE8`. Position: X: 5.8".
- Efficiency: JetBrains Mono Regular, 14 pt, color-coded — `#27AE60` if ≥90%, `#E8A020` if 60–89%, `#E05C5C` if <60%. Position: X: 8.2".
- Use: Inter Regular, 13 pt, `#F0EDE8`. Position: X: 9.4". Wrap to second line if needed.

---

**Gold key-data callout (below table):**

Position: X: 0.5". Y: 13.7". Width: 11.25". Height: 8.5"

- Container: Rounded rectangle, fill `#1E2435`, radius 6 pt
- Left accent: 0.06" × 8.5", fill `#E8A020`

Title:
- Position: X: 0.8". Y: 13.9"
- Font: Barlow SemiBold, 20 pt, `#E8A020`
- Text:

> GOLD — KEY OPERATING DATA

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 150%):
- Position: X: 0.8". Y: 14.5". Width: 10.7"

> **Soft gold (cyanide):** 99.9%+ purity, Knoop 60–90, ductile. Used for wire bonding and decorative work. Cathode efficiency 95–100%.
>
> **Hard gold (Co/Ni-alloyed acid cyanide):** 99.5–99.7% purity, Knoop 130–200, wear-resistant. Used for electrical contacts. Cathode efficiency drops to 25–35% — plan tank ampere-hours accordingly.
>
> **Sulfite gold:** Cyanide-free, photoresist-compatible. **pH must not drop below 8.0** — the sulfite complex decomposes and the bath crashes. Monitor pH daily.
>
> **Always strike** over copper, brass, or nickel before plating gold — pure-gold strike at high CD for 10–30 seconds.

---

#### RIGHT COLUMN — BLOCK C: SILVER

X: 12.25" to 23.5" (11.25" wide). Mirror of the gold column.

**Column header bar:**
- Element type: Rectangle, X: 12.25", Y: 3.1", W: 11.25", H: 0.8"
- Fill: `#C8D0D8` (Bright Silver)

Header text:
- Position: X: 12.45". Y: 3.25"
- Font: Barlow Condensed ExtraBold, 40 pt, `#1A1F2E`
- Text:

> SILVER (Ag)

Atomic-data sub-line:
- Position: X: 19.75". Y: 3.4". Width: 3.5". Right-aligned.
- Font: JetBrains Mono Regular, 14 pt, `#1A1F2E`
- Text:

> Z=47  |  ρ=10.5 g/cm³

---

**Bath comparison table — Silver**

Y: 4.1" to 13.5". 3 bath rows + 1 header row = 4 rows. (Silver has fewer commercial bath types than gold; rows are 2.0" tall instead of 1.4" to balance the column visually.)

**Table header row:** Identical structure to gold table, X: 12.25".

| Row | Bath | pH | CD (A/ft²) | Eff. | Use |
|-----|------|----|------------|------|-----|
| 1 | Cyanide strike | 11.5–12.5 | 15–30 | 75–90% | Mandatory pre-plate |
| 2 | Normal Rochelle | 11.5–12.5 | 5–15 | 95–100% | General decorative |
| 3 | High-speed bright | 11.0–12.0 | 20–60 | 95–100% | Tableware, jewelry |

Row build follows the same pattern as the gold table — alternating fills, Inter Medium for bath name (in `#C8D0D8` instead of Amber), JetBrains Mono for numeric columns.

---

**Silver key-data callout (below table):**

Position: X: 12.25". Y: 13.7". Width: 11.25". Height: 8.5"

- Container: Rounded rectangle, fill `#1E2435`, radius 6 pt
- Left accent: 0.06" × 8.5", fill `#C8D0D8`

Title:
- Position: X: 12.55". Y: 13.9"
- Font: Barlow SemiBold, 20 pt, `#C8D0D8`
- Text:

> SILVER — KEY OPERATING DATA

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 150%):
- Position: X: 12.55". Y: 14.5". Width: 10.7"

> **Mandatory cyanide strike** before plating silver over copper or nickel. Without the strike, copper undergoes immersion deposition into the silver bath surface — a loose, non-adherent layer that destroys adhesion.
>
> **Antimony brighteners** (used in bright silver baths) reduce the conductivity of the deposit to 10–25% of pure silver. For electrical applications, specify a non-brightened bath.
>
> **Normal Rochelle** is the workhorse decorative bath. Free cyanide 4–8 oz/gal; carbonate buildup is the most common control issue.
>
> Silver tarnishes rapidly in sulfur-containing atmospheres — specify a chromate or organic post-treat for shelf life.

---

### ZONE 3 — Rules of the Trade

**Dimensions:** Full page width within margins. Y: 22.5" to 32.5" (~10.0" tall).

---

**Section label:**
- Position: Centered horizontally. Y: 22.7"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Alignment: Center
- Text:

> RULES OF THE TRADE

---

**BLOCK D — The Silver Strike Rule** (full-width callout)

Position: X: 0.5". Y: 23.4". Width: 23.0". Height: 2.4"

- Container: Rounded rectangle, fill `#1E2435`, radius 8 pt
- Left accent: 0.06" × 2.4", fill `#2EC4B6` (Teal)

Title:
- Position: X: 0.8". Y: 23.6"
- Font: Barlow SemiBold, 22 pt, `#2EC4B6`
- Text:

> THE SILVER STRIKE RULE

Body:
- Position: X: 0.8". Y: 24.2". Width: 22.4"
- Font: Inter Regular, 17 pt, `#F0EDE8`, line height 145%
- Text:

> Always run a cyanide silver strike before plating silver over copper or nickel. The instant a copper part contacts a silver cyanide bath, copper begins immersion-displacing onto the surface — producing a non-adherent layer that no amount of plating time will fix. The strike's high CD and short time deposit a thin adherent film that breaks the immersion path before the main bath is reached.

---

**BLOCK E — Troy vs. Avoirdupois Pitfall** (full-width callout)

Position: X: 0.5". Y: 26.2". Width: 23.0". Height: 2.6"

- Container: Rounded rectangle, fill `#1E2435`, radius 8 pt
- Left accent: 0.06" × 2.6", fill `#E05C5C` (Coral)

Title:
- Position: X: 0.8". Y: 26.4"
- Font: Barlow SemiBold, 22 pt, `#E05C5C`
- Text:

> TROY vs. AVOIRDUPOIS — THE ASSAY ERROR THAT KEEPS HAPPENING

Two large value blocks centered:

**Troy ounce (precious metals standard):**
- Position: X: 4.0". Y: 27.0"
- Font: JetBrains Mono Regular, 36 pt, `#E8A020`
- Text:

> 1 troy oz = 31.1 g

**Avoirdupois ounce (everything else):**
- Position: X: 13.5". Y: 27.0"
- Font: JetBrains Mono Regular, 36 pt, `#C8D0D8`
- Text:

> 1 avdp oz = 28.35 g

Body footer:
- Position: X: 0.8". Y: 28.0". Width: 22.4"
- Font: Inter Medium, 14 pt, `#F0EDE8`, alignment center
- Text:

> Precious metals are sold and assayed in TROY ounces. Lab balances read in grams or avoirdupois. Mixing the two has cost more than one shop a five-figure refining error — always confirm units on every assay.

---

**BLOCK F — Paired Callouts: Sulfite pH + Hard/Soft Gold Efficiency**

Y: 29.0" to 32.0". Two equal-width callouts.

**Callout F1 — Sulfite Gold pH** (left half):

- Container: Rounded rectangle, X: 0.5", Y: 29.0", W: 11.25", H: 3.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" × 3.0", fill `#E8A020`

Title:
- Position: X: 0.8". Y: 29.2"
- Font: Barlow SemiBold, 18 pt, `#E8A020`
- Text:

> SULFITE GOLD — pH IS LIFE

Body:
- Position: X: 0.8". Y: 29.7". Width: 10.7"
- Font: Inter Regular, 14 pt, `#F0EDE8`, line height 145%
- Text:

> Sulfite gold complexes are stable only above pH 8.0. Drop below 8.0 and the bath decomposes — the gold drops out as a black sludge and the entire tank is lost. Monitor pH daily; never let it drift.

---

**Callout F2 — Hard vs. Soft Gold Efficiency** (right half):

- Container: Rounded rectangle, X: 12.25", Y: 29.0", W: 11.25", H: 3.0", fill `#1E2435`, radius 6 pt
- Left accent: 0.06" × 3.0", fill `#27AE60` (Emerald)

Title:
- Position: X: 12.55". Y: 29.2"
- Font: Barlow SemiBold, 18 pt, `#27AE60`
- Text:

> SOFT vs. HARD GOLD — EFFICIENCY GAP

Two-column data layout inside the callout:

Left side (Soft):
- `SOFT GOLD` — Barlow SemiBold, 14 pt, `#27AE60`. X: 12.55", Y: 29.7"
- `95–100%` — JetBrains Mono Regular, 28 pt, `#27AE60`. X: 12.55", Y: 30.1"
- `cathode efficiency` — Inter Regular, 11 pt, `#F0EDE8` at 70%. X: 12.55", Y: 30.85"

Right side (Hard):
- `HARD GOLD` — Barlow SemiBold, 14 pt, `#E05C5C`. X: 17.85", Y: 29.7"
- `25–35%` — JetBrains Mono Regular, 28 pt, `#E05C5C`. X: 17.85", Y: 30.1"
- `cathode efficiency` — Inter Regular, 11 pt, `#F0EDE8` at 70%. X: 17.85", Y: 30.85"

Footer line:
- Position: X: 12.55". Y: 31.4". Width: 10.7"
- Font: Inter Medium, 12 pt, `#F0EDE8`
- Text:

> A hard gold tank uses 3x the ampere-hours per gram plated. Quote and cost accordingly.

---

### ZONE 4 — Footer Band

**Dimensions:** Full page width. Y: 32.5" to 36.0" (~3.5" tall).

---

**Footer band background:**
- Element type: Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5"
- Fill: `#0D1020`

**Disclaimer:**
- Position: X: 0.5". Y: 32.8". Width: 23.0"
- Font: Inter Regular, 11 pt, `#F0EDE8` at 50%, alignment center
- Text:

> This poster is an educational quick reference. Operating parameters for proprietary precious-metals baths must always be verified against the supplier's current technical data sheet. Cyanide chemistries are hazardous — follow all applicable health, safety, and waste-treatment regulations.

**Poster title:**
- Position: X: 0.5". Y: 33.5"
- Font: Barlow SemiBold, 16 pt, `#F0EDE8`
- Text:

> Precious Metals — Gold and Silver Quick Reference

**Series name:**
- Position: Centered. Y: 34.2"
- Font: Inter Regular, 14 pt, `#F0EDE8` at 70%, alignment center
- Text:

> Plating Posters Inc — Metal Finishing Reference Series

**Logo placeholder:**
- Position: X: 22.5". Y: 33.3"
- W: 0.83". H: 0.42". Fill: `#3A4055`
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
| Zone 2 - Gold Column | Block B header bar, gold table, gold key-data callout |
| Zone 2 - Silver Column | Block C header bar, silver table, silver key-data callout |
| Zone 3 - Silver Strike Rule | Block D full-width callout |
| Zone 3 - Troy vs Avdp | Block E full-width callout with both value blocks |
| Zone 3 - Sulfite + Efficiency | Blocks F1 and F2 paired callouts |
| Zone 4 - Footer | Footer band, disclaimer, poster title, series name, logo placeholder, version |

---

## Part 6 — Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout fills, table backgrounds |
| `#252B3D` | `#E8E8F0` | Alternate row backgrounds |
| `#0D1020` | `#1A1F2E` | Footer strip background |
| `#E8A020` | `#C8860A` | Amber / gold column accents |
| `#2EC4B6` | `#1A8C82` | Teal accents (silver strike rule) |
| `#27AE60` | `#1E7A47` | Emerald accents (soft gold efficiency) |
| `#E05C5C` | `#B83E3E` | Coral accents (hard gold, troy/avdp warning) |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#5A6470` | Silver column accents — darken for contrast against light BG |
| `#F5C870` | `#A87015` | Pale Amber sub-accents |

The silver column header bar (`#C8D0D8`) needs special handling in the Light edition — at light-on-light it loses contrast. Use `#5A6470` and switch the header text color from `#1A1F2E` to `#F0EDE8`.

---

## Part 7 — Export Checklist

| File Name | Mode | Quality | Bleed + Marks |
|---|---|---|---|
| `Precious Metals — Dark — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Precious Metals — Dark — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Precious Metals — Dark — Digital.pdf` | RGB | PDF Standard | No |
| `Precious Metals — Light — 24x36 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Precious Metals — Light — 18x24 — Print.pdf` | RGB | PDF Print (300 DPI) | Yes |
| `Precious Metals — Light — Digital.pdf` | RGB | PDF Standard | No |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #20 — Precious Metals Quick Reference — Construction Workup v1.0*
*2026-04-07*
