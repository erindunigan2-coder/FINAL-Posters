---
Project: Plating Posters Inc
Poster Number: 5
Title: "Anode-to-Cathode Ratio: Why It Matters More Than You Think"
Document Type: Construction Workup
Status: v1.0 — Ready for Elara
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Poster 5 — Anode-to-Cathode Ratio — Content and Layout Draft.md (v1.0)"
Technical Source: Watson — Anode-to-Cathode Ratio Research Brief v1 (2026-04-03)
Watson Flags: TWO — A:C ratio ranges + zinc anode note (both Drew, non-blocking)
Process Scope: Universal concept — applies across all electrolytic plating processes
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow: Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AnodeCathodeRatio
  - ConstructionWorkup
---

# Poster # Poster #5 — Construction Workup
## Anode-to-Cathode Ratio: Why It Matters More Than You Think

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*

This document is the construction workup for Poster #5. It translates the finalized Content and Layout Draft (v1.0) into specifications directly usable by Elara to engineer a generation prompt for Drew. Two Watson flags remain open but are non-blocking.

> **Workflow update (2026-04-14):** Poster generation now uses claude.ai chat (SVG/HTML visual artifacts) These specs feed the Claude Chat Generation Prompt. If Drew approves the generated output, it proceeds to final production.

**Source of truth for content:** `Poster 5 — Anode-to-Cathode Ratio — Content and Layout Draft.md` — all copy is reproduced here verbatim. If any discrepancy exists, the Content and Layout Draft governs.

---

## Part 1 — Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for tank outlines, anode/cathode shapes, table rows, callout boxes
- Line elements for current flow lines between anode and cathode
- Small arrow elements for dissolution arrows
- Color fills set to exact hex values
- Export at print-quality PDF (300 DPI equivalent)

### Limitations to Flag for Elara

1. **Triple tank cross-section (HERO):** Three plating tanks side by side, each containing anode and cathode rectangles with current flow lines. Build each tank as a composite of geometric shapes — rounded rectangle for tank, vertical rectangles for anode and cathode, line elements for current flow. **Key difference between the three tanks:** the anode sizes are different (small, correct, large) and the current flow patterns vary (crowded, even, even-with-excess). Validated approach from Posters #2, #4, #10, #13.

2. **Current flow lines (curved):** the line element does not support true curves easily. **Workaround:** Use straight angled lines to approximate current paths. For the "Under-Anoded" tank, bunch 5-6 lines at the top/edges of the cathode with 1-2 sparse lines at the bottom. For "Correct," space lines evenly. For "Over-Anoded," use evenly spaced lines plus small dissolution arrows from anode.

3. **Deposit thickness variation on cathode:** In the Under-Anoded tank, the deposit on the cathode face should be thick at the top and thin/absent at the bottom. Build as two stacked rectangles of different widths — wide `#C8D0D8` rectangle at the top half, very narrow or no rectangle at the bottom half.

4. **4 pt left-border accents:** Same technique as previous posters — narrow 0.06" rectangle.

5. **Global Colors / swatch remap for Light edition:** Manual recolor per Part 6.

6. **JetBrains Mono:** Ensure font is available. Substitute Courier Prime if unavailable.

7. **Print size — 24x36".** 18x24" by duplicate and resize.

8. **Sub/superscript:** Copy-paste Unicode (CN⁻, ZnO, Cu²⁺, etc.).

---

## Part 2 — Document Setup Instructions (for Elara's prompt)

### Step 1 — Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 — Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 — Upload fonts (the Pro tier required)
- **Barlow Condensed ExtraBold** — headlines, zone labels
- **Barlow SemiBold** — subheadings, callout titles
- **Inter Regular** and **Inter Medium** — body text, table data
- **JetBrains Mono Regular** — ratios, equations, data values

### Step 4 — Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Primary text |
| Amber | `#E8A020` | Over-anoded accent, subheading |
| Teal | `#2EC4B6` | Callout borders, ideal ratio column |
| Emerald | `#27AE60` | Correct ratio accent, maintenance |
| Coral | `#E05C5C` | Under-anoded accent, passivation warning |
| Mid Slate | `#3A4055` | Table headers, tank outlines |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Callout fills, tank interior |
| Alt Row | `#252B3D` | Alternating rows |
| Bright Silver | `#C8D0D8` | Cathode/deposit illustration |

### Step 5 — Set ruler guides

**Vertical guides:**
- 0.5" — left safe zone
- 23.5" — right safe zone

**Horizontal guides:**
- 0.5" — top safe zone
- 2.9" — Zone 1/Zone 2 boundary
- 13.7" — Zone 2/Zone 3 boundary
- 22.3" — Zone 3/Zone 4 boundary
- 28.8" — Zone 4/Zone 5 boundary
- 32.4" — Zone 5/Zone 6 boundary
- 35.5" — bottom safe zone

---

## Part 3 — Layout Zones and Build Order

```
ZONE 1 — HEADER BAND (0"–2.9")
  Block A: Headline + subheading + tagline (left ~55%)
  Block B: "The Definition" callout box (right ~45%)

ZONE 2 — TRIPLE TANK COMPARISON (HERO) (2.9"–13.7" / ~10.8" tall)
  Block C: Three tank cross-sections — Under-Anoded | Correct | Over-Anoded

ZONE 3 — A:C RATIO TABLE (13.7"–22.3" / ~8.6" tall)
  Block D: 11-process ratio table with anode types and notes

ZONE 4 — SYMPTOMS + CALCULATION (22.3"–28.8" / ~6.5" tall)
  Block E: "What Goes Wrong" two callouts (left 55%)
  Block F: Worked calculation + fist rule (right 45%)

ZONE 5 — MAINTENANCE + PASSIVATION (28.8"–32.4" / ~3.6" tall)
  Block G: Maintenance checklist (left 50%)
  Block H: Passivation warning (right 50%)

ZONE 6 — FOOTER BAND (32.4"–36.0" / ~3.6" tall)
  Block I: Disclaimer + poster title + series name + logo + version
```

---

## Part 4 — Zone-by-Zone Build Specifications

### ZONE 1 — Header Band

**Dimensions:** Full width. Y: 0" to 2.9".
**Background:** Same as page.

---

**BLOCK A — Headline**
- Position: X: 0.5". Y: 0.5"
- Width: 12.5"
- Font: Barlow Condensed ExtraBold, 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text:

> ANODE-TO-CATHODE RATIO

**BLOCK A — Subheading**
- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 36 pt
- Color: `#E8A020`
- Text:

> Why It Matters More Than You Think

**BLOCK A — Tagline**
- Position: X: 0.5". Y: 2.1"
- Font: Barlow SemiBold, 22 pt
- Color: `#F0EDE8` at 65% opacity
- Text:

> The ratio that controls your current, your anodes, and your bath chemistry.

---

**BLOCK B — "The Definition" Callout Box**

*Container:*
- Position: X: 13.25". Y: 0.5"
- Width: 10.25". Height: 2.2"
- Fill: `#1E2435`
- Border: 1.5 pt, `#2EC4B6`
- Corner radius: 8 pt

*Title:*
- Position: X: 13.55". Y: 0.7"
- Font: Barlow SemiBold, 18 pt. Color: `#2EC4B6`
- Text:

> THE DEFINITION

*Formula:*
- Position: X: centered in container. Y: 1.0"
- Font: JetBrains Mono Regular, 22 pt. Color: `#F0EDE8`. Alignment: Center
- Text:

> A:C = Anode Area / Cathode Area

*Examples:*
- Position: X: 13.55". Y: 1.5"
- Font: JetBrains Mono Regular, 15 pt. Color: `#F0EDE8` at 80%
- Line height: 150%
- Text:

> 1:1 — anode equals cathode
> 2:1 — anode is 2x cathode
> 0.5:1 — anode is half cathode (under-anoded)

*Target line:*
- Position: X: 13.55". Y: 2.2"
- Font: Inter Medium, 16 pt. Color: `#2EC4B6`
- Text:

> Most processes: target 1:1 to 2:1.

---

### ZONE 2 — Triple Tank Comparison (HERO)

**Dimensions:** Full width. Y: 2.9" to 13.7" (10.8" tall).

---

**Section label:**
- Position: X: centered. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 30 pt. Color: `#F0EDE8`. Alignment: Center
- Text:

> WHAT HAPPENS WHEN THE RATIO IS WRONG

---

**BLOCK C — Three Tanks Side by Side**

**Tank dimensions:** Each 7.2" wide x 7.0" tall, separated by 0.35" gutters.
- Tank 1 position: X: 0.5". Y: 3.8"
- Tank 2 position: X: 8.05". Y: 3.8"
- Tank 3 position: X: 15.6". Y: 3.8"

---

**TANK 1 — UNDER-ANODED (Coral)**

*Tank label:*
- Position: X: 0.5" (left-aligned above tank). Y: 3.8"
- Font: Barlow Condensed ExtraBold, 22 pt. Color: `#E05C5C`
- Text: `UNDER-ANODED`

*Ratio label:*
- Position: X: 5.5" (right-aligned above tank). Y: 3.85"
- Font: JetBrains Mono, 16 pt. Color: `#E05C5C`
- Text: `A:C = 0.5:1`

*Tank body:*
- Rounded rectangle. Position: X: 0.5". Y: 4.3"
- Width: 7.2". Height: 5.5"
- Fill: `#1E2435`. Border: 2 pt, `#3A4055`. Corner radius: 4 pt

*Electrolyte suggestion:*
- 2-3 horizontal lines inside tank, `#2EC4B6` at 15% opacity, 1 pt

*Anode (small — under-anoded):*
- Rectangle. Position: X: 1.3". Y: 5.0"
- Width: 0.8". Height: 3.5"
- Fill: none. Border: 2 pt, `#E05C5C`

*Cathode (part):*
- Rectangle. Position: X: 5.5". Y: 4.8"
- Width: 1.2". Height: 4.5"
- Fill: `#C8D0D8` (Bright Silver)

*Deposit — uneven:*
- Top deposit (thick): Rectangle. X: 5.2". Y: 4.8". Width: 0.3". Height: 1.5". Fill: `#F0EDE8` at 80%
- Bottom deposit (absent/thin): no rectangle — bare cathode face shows

*Current flow lines (crowded at top):*
- 4 lines from anode right face toward cathode top-left area, bunching together. Stroke: 1 pt, `#E05C5C`
- 1 sparse line toward cathode mid-section. Stroke: 1 pt, `#E05C5C` at 40%

*Callout labels:*
- `BURNING` — JetBrains Mono, 12 pt, `#E05C5C`. Position near top of cathode with small arrow line
- `THIN / SKIP` — JetBrains Mono, 12 pt, `#E05C5C`. Position near bottom of cathode

*Sub-label:*
- Position: X: 0.5". Y: 10.0"
- Width: 7.2"
- Font: Inter Regular, 14 pt. Color: `#F0EDE8`. Alignment: Center
- Text:

> Current crowds at the nearest cathode surfaces. Edges burn. Recesses starve.

---

**TANK 2 — CORRECT RATIO (Emerald)**

*Tank label:*
- Position: X: 8.05". Y: 3.8"
- Font: Barlow Condensed ExtraBold, 22 pt. Color: `#27AE60`
- Text: `CORRECT RATIO`

*Ratio label:*
- Position: X: 13.0". Y: 3.85"
- Font: JetBrains Mono, 16 pt. Color: `#27AE60`
- Text: `A:C = 1.5:1`

*Tank body:*
- Rounded rectangle. Position: X: 8.05". Y: 4.3"
- Width: 7.2". Height: 5.5"
- Fill: `#1E2435`. Border: 2 pt, `#3A4055`. Corner radius: 4 pt

*Anode (proper size):*
- Rectangle. Position: X: 8.85". Y: 4.7"
- Width: 1.5". Height: 4.5"
- Fill: none. Border: 2 pt, `#27AE60`

*Cathode:*
- Rectangle. Position: X: 13.0". Y: 4.8"
- Width: 1.2". Height: 4.5"
- Fill: `#C8D0D8`

*Deposit — uniform:*
- Rectangle. Position: X: 12.75". Y: 4.8"
- Width: 0.25". Height: 4.5"
- Fill: `#F0EDE8` at 80%

*Current flow lines (evenly spaced):*
- 5 parallel lines from anode to cathode, evenly distributed vertically. Stroke: 1 pt, `#27AE60`

*Sub-label:*
- Position: X: 8.05". Y: 10.0"
- Width: 7.2". Alignment: Center
- Font: Inter Regular, 14 pt. Color: `#F0EDE8`
- Text:

> Current distributes evenly. Uniform deposit. Bath stays balanced.

---

**TANK 3 — OVER-ANODED (Amber)**

*Tank label:*
- Position: X: 15.6". Y: 3.8"
- Font: Barlow Condensed ExtraBold, 22 pt. Color: `#E8A020`
- Text: `OVER-ANODED`

*Ratio label:*
- Position: X: 20.5". Y: 3.85"
- Font: JetBrains Mono, 16 pt. Color: `#E8A020`
- Text: `A:C = 3:1`

*Tank body:*
- Rounded rectangle. Position: X: 15.6". Y: 4.3"
- Width: 7.2". Height: 5.5"
- Fill: `#1E2435`. Border: 2 pt, `#3A4055`. Corner radius: 4 pt

*Anode (large — over-anoded):*
- Rectangle. Position: X: 16.2". Y: 4.5"
- Width: 2.5". Height: 5.0"
- Fill: none. Border: 2 pt, `#E8A020`

*Cathode:*
- Rectangle. Position: X: 20.5". Y: 4.8"
- Width: 1.2". Height: 4.5"
- Fill: `#C8D0D8`

*Deposit — reasonably uniform:*
- Rectangle. Position: X: 20.25". Y: 4.8"
- Width: 0.25". Height: 4.5"
- Fill: `#F0EDE8` at 80%

*Current flow lines (evenly spaced):*
- 5 parallel lines, evenly distributed. Stroke: 1 pt, `#E8A020`

*Dissolution arrows (excess):*
- 3 small arrow lines from anode left face into solution, pointing left. Stroke: 1.5 pt, `#E8A020`, with arrowheads
- Label: `Excess dissolution` — Inter Regular, 11 pt, `#E8A020`

*Sub-label:*
- Position: X: 15.6". Y: 10.0"
- Width: 7.2". Alignment: Center
- Font: Inter Regular, 14 pt. Color: `#F0EDE8`
- Text:

> Generally acceptable. Excess anode area may over-dissolve, raising metal concentration.

---

**Key insight banner:**
- Position: X: centered. Y: 10.6"
- Width: 22.0"
- Font: Inter Medium, 18 pt. Color: `#F0EDE8`. Alignment: Center
- Text:

> Under-anoded is the critical failure. Over-anoded is usually tolerable.

---

### ZONE 3 — A:C Ratio Table

**Dimensions:** Full width. Y: 13.7" to 22.3" (8.6" tall).

---

**BLOCK D — Process-Specific Ratio Table**

**Section label:**
- Position: X: 0.5". Y: 13.9"
- Font: Barlow Condensed ExtraBold, 26 pt. Color: `#F0EDE8`
- Text:

> IDEAL A:C RATIOS BY PROCESS

**Column header row:**
- Rectangle. X: 0.5". Y: 14.4". Width: 23.0". Height: 0.5". Fill: `#3A4055`

**Column headers (4 text boxes):**
- Col 1: X: 0.7". Text: `Process`. Width: 6.5". Barlow SemiBold, 18 pt, `#F0EDE8`
- Col 2: X: 7.2". Text: `Ideal A:C`. Width: 3.5". Barlow SemiBold, 18 pt, `#2EC4B6`
- Col 3: X: 10.7". Text: `Anode Type`. Width: 5.5". Barlow SemiBold, 18 pt, `#F0EDE8`
- Col 4: X: 16.2". Text: `Notes`. Width: 7.0". Barlow SemiBold, 18 pt, `#F0EDE8`

**Data rows (11 rows, each 0.6" tall, alternating fills):**

Row Y positions starting at 14.9", incrementing by 0.6":

| Row | Y | Fill | Process | Ideal A:C | Anode Type | Notes |
|-----|---|------|---------|-----------|------------|-------|
| 1 | 14.90" | `#1A1F2E` | Acid copper sulfate | 1:1 to 2:1 | Cu-P (phosphorized) | Cu-P film regulates dissolution |
| 2 | 15.50" | `#252B3D` | Cyanide copper | 1:1 to 1.5:1 | OFHC copper | Higher A:C increases CN⁻ consumption |
| 3 | 16.10" | `#1A1F2E` | Watts nickel (bright) | 1:1 to 2:1 | Ni R-Rounds (Ti baskets) | Bag anodes to contain sludge |
| 4 | 16.70" | `#252B3D` | Nickel sulfamate | 1:1 to 2:1 | Ni S-Rounds (Ti baskets) | Higher A:C preferred — uniform dissolution |
| 5 | 17.30" | `#1A1F2E` | Acid chloride zinc | 1:1 to 1.5:1 | Zinc slabs/balls | High KCl increases dissolution rate |
| 6 | 17.90" | `#252B3D` | Alkaline NC zinc | 1:1 to 2:1 | Steel plates (insoluble) | Current distribution only — add ZnO |
| 7 | 18.50" | `#1A1F2E` | Alkaline cyanide zinc | 1:1 to 2:1 | Zinc balls (steel baskets) | Lower A:C may be preferred |
| 8 | 19.10" | `#252B3D` | Decorative chrome (hex) | 1:1 to 3:1 | Lead-tin (7% Sn) | A:C affects covering power |
| 9 | 19.70" | `#1A1F2E` | Hard chrome | 1:1 to 3:1 | Lead-tin or Pb-Sb | Conforming anodes → 1:1 at all points |
| 10 | 20.30" | `#252B3D` | Silver cyanide | 1:1 to 2:1 | High-purity Ag (>99.9%) | Maintain anode area >= cathode area |
| 11 | 20.90" | `#1A1F2E` | Matte tin | 1:1 to 1.5:1 | Pure tin (Zr baskets) | Ti baskets would passivate |

Each row: Rectangle at (X: 0.5", Y: row Y), Width: 23.0", Height: 0.6".

Process text: Inter Medium, 17 pt, `#F0EDE8`, X: 0.7"
Ideal A:C text: JetBrains Mono, 17 pt, `#2EC4B6`, X: 7.2"
Anode Type text: Inter Regular, 16 pt, `#F0EDE8`, X: 10.7"
Notes text: Inter Regular, 15 pt, `#F0EDE8`, X: 16.2"

---

### ZONE 4 — Symptoms + Calculation

**Dimensions:** Full width. Y: 22.3" to 28.8" (6.5" tall).

---

**BLOCK E — "What Goes Wrong" (left 55%)**

**Position:** X: 0.5". Y: 22.3". Width: 12.5".

**Section label:**
- Position: X: 0.5". Y: 22.5"
- Font: Barlow Condensed ExtraBold, 22 pt. Color: `#F0EDE8`
- Text:

> SYMPTOMS OF INCORRECT RATIO

---

**Under-Anoded callout:**

*Container:*
- Rounded rectangle. X: 0.5". Y: 23.0". Width: 12.5". Height: 2.4"
- Fill: `#1E2435`. Corner radius: 6 pt

*Left accent:*
- Rectangle. X: 0.5". Y: 23.0". Width: 0.06". Height: 2.4". Fill: `#E05C5C`

*Title:*
- X: 0.85". Y: 23.15"
- Barlow SemiBold, 18 pt. Color: `#E05C5C`
- Text:

> UNDER-ANODED (A:C TOO LOW)

*Bullets:*
- X: 0.85". Y: 23.55". Width: 12.0"
- Inter Regular, 15 pt. Color: `#F0EDE8`. Line height: 150%
- Text:

> - Burning at edges and HCD zones
> - Poor throwing power — thin LCD coverage
> - Rising bath voltage
> - Metal concentration dropping
> - Anode passivation risk

---

**Over-Anoded callout:**

*Container:*
- Rounded rectangle. X: 0.5". Y: 25.6". Width: 12.5". Height: 2.0"
- Fill: `#1E2435`. Corner radius: 6 pt

*Left accent:*
- Rectangle. X: 0.5". Y: 25.6". Width: 0.06". Height: 2.0". Fill: `#E8A020`

*Title:*
- X: 0.85". Y: 25.75"
- Barlow SemiBold, 18 pt. Color: `#E8A020`
- Text:

> OVER-ANODED (A:C TOO HIGH)

*Bullets:*
- X: 0.85". Y: 26.15". Width: 12.0"
- Inter Regular, 15 pt. Color: `#F0EDE8`. Line height: 150%
- Text:

> - Rising metal concentration (some processes)
> - Sludge formation (nickel)
> - Wasted anode material
> - Generally less problematic than under-anoded

---

**BLOCK F — Worked Calculation + Fist Rule (right 45%)**

**Position:** X: 13.5". Y: 22.3". Width: 10.0".

---

**Calculation callout:**

*Container:*
- Rounded rectangle. X: 13.5". Y: 22.6". Width: 10.0". Height: 4.2"
- Fill: `#1E2435`. Border: 1.5 pt, `#2EC4B6`. Corner radius: 8 pt

*Title:*
- X: 13.8". Y: 22.8"
- Barlow SemiBold, 18 pt. Color: `#2EC4B6`
- Text:

> QUICK CALCULATION

*Calculation text:*
- X: 13.8". Y: 23.2". Width: 9.4"
- JetBrains Mono Regular, 13 pt. Color: `#F0EDE8`. Line height: 160%
- Text:

> 20 cylinders, 2" dia x 6" long
> Each: pi x 2 x 6 = 37.7 in² = 0.262 ft²
> Total cathode: 20 x 0.262 = 5.24 ft²
>
> 2 anode baskets, 6" x 24" x 2 sides
> Each: 288 in² / 144 = 2.0 ft²
> Total anode: 2 x 2.0 = 4.0 ft²
>
> A:C = 4.0 / 5.24 = 0.76:1

*Answer:*
- X: 13.8". Y: 26.0"
- Inter Medium, 15 pt. Color: `#E05C5C`
- Text:

> Under-anoded! Add a third basket.

---

**Fist Rule callout:**

*Container:*
- Rounded rectangle. X: 13.5". Y: 27.1". Width: 10.0". Height: 1.5"
- Fill: `#1E2435`. Corner radius: 6 pt. No border

*Title:*
- X: 13.8". Y: 27.25"
- Barlow SemiBold, 16 pt. Color: `#E8A020`
- Text:

> THE FIST RULE

*Value:*
- X: 13.8". Y: 27.6"
- JetBrains Mono Regular, 18 pt. Color: `#F0EDE8`
- Text:

> 1 clenched fist ≈ 0.33 ft²

*Description:*
- X: 13.8". Y: 28.0"
- Inter Regular, 13 pt. Color: `#F0EDE8` at 70%
- Text:

> A quick estimation method for cathode surface area — from Drew's field notes.

---

### ZONE 5 — Maintenance + Passivation

**Dimensions:** Full width. Y: 28.8" to 32.4" (3.6" tall).

---

**BLOCK G — Anode Maintenance Checklist (left 50%)**

*Container:*
- Rounded rectangle. X: 0.5". Y: 28.8". Width: 11.2". Height: 3.3"
- Fill: `#1E2435`. Border: 1.5 pt, `#27AE60`. Corner radius: 8 pt

*Title:*
- X: 0.8". Y: 29.0"
- Barlow SemiBold, 18 pt. Color: `#27AE60`
- Text:

> ANODE MAINTENANCE

*Bullets:*
- X: 0.8". Y: 29.4". Width: 10.6"
- Inter Regular, 15 pt. Color: `#F0EDE8`. Line height: 145%
- Text:

> - Bag all soluble anodes — contain sludge
> - Replace consumed anodes before they get too small
> - Clean anode contacts — corrosion = resistance
> - Verify anode composition — wrong alloy = wrong dissolution
> - Submerge anodes to proper depth — exposed surface = uneven current
> - Inspect anode bags — holes defeat the purpose

---

**BLOCK H — Passivation Warning (right 50%)**

*Container:*
- Rounded rectangle. X: 12.0". Y: 28.8". Width: 11.5". Height: 3.3"
- Fill: `#1E2435`. Border: 2 pt, `#E05C5C`. Corner radius: 8 pt

*Title:*
- X: 12.3". Y: 29.0"
- Barlow SemiBold, 18 pt. Color: `#E05C5C`
- Text:

> ANODE PASSIVATION

*Body:*
- X: 12.3". Y: 29.4". Width: 10.9"
- Inter Regular, 15 pt. Color: `#F0EDE8`. Line height: 140%
- Text:

> When anode current density gets too high, a dense oxide film forms on the anode surface and stops dissolution entirely.

*Symptoms:*
- X: 12.3". Y: 30.3"
- Inter Medium, 14 pt. Color: `#E05C5C`
- Text:

> Voltage rises sharply | Metal drops | Current distribution degrades

*Fix:*
- X: 12.3". Y: 30.8"
- Inter Medium, 14 pt. Color: `#27AE60`
- Text:

> Increase anode area. Verify anode composition. Check chloride level.

---

### ZONE 6 — Footer Band

**Dimensions:** Full width. Y: 32.4" to 36.0" (3.6" tall).

**Footer band background:**
- Rectangle. X: 0". Y: 32.4". Width: 24.0". Height: 3.6". Fill: `#0D1020`

**Disclaimer:**
- X: 0.5". Y: 32.8". Width: 23.0"
- Inter Regular, 11 pt. Color: `#F0EDE8` at 50%. Alignment: Center
- Text:

> This poster presents general anode-to-cathode ratio guidelines. Specific ratios depend on tank geometry, anode type, and product formulation. Consult your process supplier for application-specific recommendations.

**Poster title:**
- X: 0.5". Y: 33.5". Barlow SemiBold, 16 pt. Color: `#F0EDE8`
- Text: `Anode-to-Cathode Ratio: Why It Matters More Than You Think`

**Series name:**
- X: 0.5". Y: 34.0". Inter Regular, 13 pt. Color: `#F0EDE8` at 60%
- Text: `Plating Posters Inc — Metal Finishing Reference Series`

**Version:**
- X: 0.5". Y: 34.4". Inter Regular, 11 pt. Color: `#F0EDE8` at 40%
- Text: `v1.0 — 2026`

**Logo placeholder:**
- X: 21.0". Y: 33.5". Width: 2.5". Height: 1.5"
- Barlow SemiBold, 14 pt. Color: `#F0EDE8` at 30%. Alignment: Center
- Text: `[LOGO]`

---

## Part 5 — Grouping and Layer Order

| Group Name | Contains | Lock? |
|-----------|----------|-------|
| Zone 1 — Header | Blocks A + B | Yes |
| Zone 2 — Tanks | Block C (3 tank sub-groups) | Yes |
| Zone 3 — Ratio Table | Block D | Yes |
| Zone 4 — Symptoms + Calc | Blocks E + F | Yes |
| Zone 5 — Maintenance | Blocks G + H | Yes |
| Zone 6 — Footer | Block I | Yes |

**Sub-grouping for Zone 2:** Group each tank (tank body + anode + cathode + deposit + current lines + labels) as a sub-group before grouping the full zone. This prevents displacement when positioning the three tanks relative to each other.

---

## Part 6 — Light Edition Remap Table

| Element / Role | Dark Edition | Light Edition |
|---|---|---|
| Page background | `#1A1F2E` | `#F0EDE8` |
| Primary text | `#F0EDE8` | `#1A1F2E` |
| Amber accent | `#E8A020` | `#B87A10` |
| Teal accent | `#2EC4B6` | `#1E9A8F` |
| Emerald accent | `#27AE60` | `#1D8A4A` |
| Coral accent | `#E05C5C` | `#C43C3C` |
| Mid Slate fills | `#3A4055` | `#D0D4DC` |
| Deep Navy footer | `#0D1020` | `#E2E0DB` |
| Dark Callout fills | `#1E2435` | `#E8E5E0` |
| Alt Row fills | `#252B3D` | `#F5F3EF` |
| Bright Silver cathode | `#C8D0D8` | `#3A4055` |

**Tank outlines** remap from Mid Slate to light neutral — the tanks become light gray boxes on a white background, which still reads cleanly.

**No overrides required.**

---

## Part 7 — Export Checklist

| Export | Size | Edition | Format | Filename |
|--------|------|---------|--------|----------|
| 1 | 24x36" | Dark | PDF Print | `Poster-05-Anode-Cathode-Ratio-24x36-Dark.pdf` |
| 2 | 24x36" | Light | PDF Print | `Poster-05-Anode-Cathode-Ratio-24x36-Light.pdf` |
| 3 | 18x24" | Dark | PDF Print | `Poster-05-Anode-Cathode-Ratio-18x24-Dark.pdf` |
| 4 | 18x24" | Light | PDF Print | `Poster-05-Anode-Cathode-Ratio-18x24-Light.pdf` |
| 5 | 24x36" | Dark | PNG | `Poster-05-Anode-Cathode-Ratio-24x36-Dark.png` |
| 6 | 24x36" | Light | PNG | `Poster-05-Anode-Cathode-Ratio-24x36-Light.png` |

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #5 — Anode-to-Cathode Ratio — Construction Workup v1.0*
*2026-04-04*
