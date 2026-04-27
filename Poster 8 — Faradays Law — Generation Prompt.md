---
Project: Plating Posters Inc
Poster Number: 8
Title: "Faraday's Law in the Shop: Calculating Plating Thickness"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 8 — Faradays Law — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - FaradaysLaw
  - Calculations
  - v1
---

# Claude Chat Generation Prompt — Poster #8
## Faraday's Law in the Shop: Calculating Plating Thickness
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup. Adapted for Claude chat visual generation (2026-04-14). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS. The output should be a finished, print-ready poster design.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first** (dark background). The Light edition remap table is provided at the end.
- Follow the design specifications in each Phase below. They describe WHAT to render — layout zones, text content, colors, typography, and visual elements.
- Every color is specified as a hex code. Every font, size, and weight is specified. Follow them exactly.
- Chemical formulas use Unicode subscript/superscript characters. Reproduce them exactly as written in this document.
- Prioritize **readability at distance** — this poster will be read from 3-8 feet away on a shop wall.

---

## Phase 1 — Design Foundation

### Artboard
- **Size:** 24 x 36 inches (portrait)
- **Background color (Dark edition):** `#1A1F2E` (Gunmetal Dark)

### Typography
| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Headlines | Barlow Condensed | ExtraBold (800) | All caps, tight letter-spacing (-4) |
| Subheadings | Barlow | SemiBold (600) | Title case |
| Body text | Inter | Regular (400) / Medium (500) | Sentence case |
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for technical values |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Accent, subheadings |
| Teal | `#2EC4B6` | Callout borders, secondary accent |
| Emerald | `#27AE60` | Positive/success accent |
| Coral | `#E05C5C` | Warning/alert accent |
| Mid Slate | `#3A4055` | Dividers, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card/callout box fills |
| Alt Row | `#252B3D` | Alternating row backgrounds |

### Layout Safe Zones
- **0.5" margin** on all sides (safe zone for print trimming)
- All content must stay within the 23" x 35" live area

---

## Phase 2 — Zone 1: Header Band (Top of Poster)

This zone occupies the top 3.2 inches. Headline, subheading, and tagline on the left (~55%), "Three Questions" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element:
2. Select all placeholder text and type: `FARADAY'S LAW IN THE SHOP`
3. Set properties:
   - **Font**: Barlow Condensed ExtraBold
   - **Size**: `96`
   - **Color**: `F0EDE8`
   - **Letter spacing**: `-4`
   - **Alignment**: Left
4. Position: left edge at 0.5 inches, top edge at 0.5 inches.
5. Set text box width to approximately **12.5 inches**.

### Step 7 — Place the subheading
1. Add a subheading text element: Type: `Calculating Plating Thickness`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `40`
   - **Color**: `E8A020` (Amber)
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **1.6 inches**.

### Step 8 — Place the tagline
1. Add a body text element: Type: `More amps x more time = more metal. Now do the math.`
2. Set properties:
   - **Font**: Barlow SemiBold
   - **Size**: `22`
   - **Color**: `F0EDE8`
   - **Transparency**: **65%**
   - **Alignment**: Left
3. Position: left edge at 0.5 inches, top edge at approximately **2.3 inches**.

### Step 9 — Build the "Three Questions" callout box

**9a — Callout container:**
1. Click **Elements** > search **rectangle** > find **Rounded Rectangle**. Click to place.
2. Set properties:
   - **Width**: `10.25` inches
   - **Height**: `2.5` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **Border**: 1.5 pt, color `2EC4B6` (Teal)
   - **Corner radius**: `8`
3. Position: left edge at 13.25 inches, top edge at 0.5 inches.

**9b — Callout title:**
1. Add a text element. Type: `EVERY PLATER ASKS THREE QUESTIONS`
2. Font: Barlow SemiBold, Size: `20`, Color: `2EC4B6` (Teal)
3. Position: X: 13.55", Y: 0.7".

**9c — Three questions:**
1. Add a text element. Type (each on its own line):
   ```
   1. How thick will my deposit be?
   2. How long do I need to plate?
   3. How much current do I need?
   ```
2. Font: Inter Medium, Size: `18`, Color: `F0EDE8`. Line height: **160%**.
3. Position: X: 13.55", Y: 1.15". Width: 9.65".

**9d — Closing line:**
1. Add a text element. Type: `Faraday's Law answers all three.`
2. Font: Inter Medium, Size: `16`, Color: `2EC4B6` (Teal)
3. Position: X: 13.55", Y: 2.35".

**9e — Group the callout box:**
Select the container, title, questions, and closing line. Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, and callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: The Master Formula

This zone occupies Y: 3.2" to 6.4" (3.2 inches tall). A full-width formula display with a color-coded variable legend.

### Step 11 — Formula background
1. Add a Rectangle (sharp corners).
   - **Width**: `24.0` inches
   - **Height**: `3.2` inches
   - **Fill**: `1E2435` (Dark Callout)
   - **No border**.
2. Position: X: 0", Y: 3.2".

### Step 12 — Formula text
1. Add a text element. Type: `Thickness = Rate x ASF x Time x Efficiency`
2. Font: JetBrains Mono Regular, Size: `36`, Color: `F0EDE8`, Alignment: Center
3. Width: **23.0 inches**.
4. Position: centered horizontally, Y: 3.6".

**Note:** At 36 pt JetBrains Mono, this formula is approximately 18-19" wide — it fits within the 23.0" safe zone with room to spare. If it wraps to two lines, widen the text box.

### Step 13 — Variable legend strip

Four legend items arranged horizontally below the formula. Each item has a small colored swatch + variable name + description.

**Item 1 — Rate:**
1. Add a small Rectangle. Width: `0.3"`. Height: `0.3"`. Fill: `2EC4B6` (Teal). Position: X: 2.5", Y: 4.6".
2. Add text: `Rate` — Inter Medium, `14` pt, `F0EDE8`. Position: right of the swatch.
3. Add text: `Plating rate (mil/Ah/ft²) — from the table below` — Inter Regular, `12` pt, `F0EDE8`, Transparency: **70%**. Position: below the name.

**Item 2 — ASF:**
1. Swatch: `0.3"` x `0.3"`, fill `E8A020` (Amber). Position: X: 8.0", Y: 4.6".
2. Name: `ASF`. Description: `Current density (amps per square foot)`.

**Item 3 — Time:**
1. Swatch: `0.3"` x `0.3"`, fill `27AE60` (Emerald). Position: X: 13.5", Y: 4.6".
2. Name: `Time`. Description: `Hours`.

**Item 4 — Efficiency:**
1. Swatch: `0.3"` x `0.3"`, fill `E05C5C` (Coral). Position: X: 18.0", Y: 4.6".
2. Name: `Efficiency`. Description: `Cathode efficiency (decimal)`.

### Step 14 — Group all of Zone 2
Select the formula background, formula text, and all 4 legend items (swatches + text). Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: ECE Table + Efficiency (HERO)

This zone occupies Y: 6.4" to 19.7" (13.3 inches tall). The ECE master table occupies the left 60%, and the Cathode Efficiency table occupies the right 40%.

### Step 15 — ECE section label
1. Add a text element. Type: `ELECTROCHEMICAL EQUIVALENTS`
2. Font: Barlow Condensed ExtraBold, Size: `26`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 6.6".

### Step 16 — ECE table column header row

**16a — Header background:**
1. Add a Rectangle. Width: `13.5"`. Height: `0.5"`. Fill: `3A4055` (Mid Slate).
2. Position: X: 0.5", Y: 7.1".

**16b — Column header labels (6 text boxes):**
All text: Barlow SemiBold, `16` pt, `F0EDE8`.

| Header | X position | Width |
|---|---|---|
| `Metal` | 0.7" | 2.1" |
| `Symbol` | 2.8" | 1.1" |
| `Valence` | 3.9" | 1.3" |
| `ECE (g/Ah)` | 5.2" | 2.4" |
| `Density (g/cm³)` | 7.6" | 2.6" |
| `Rate (mil/Ah/ft²)` | 10.2" | 3.5" |

**Special:** The Rate column header uses color `2EC4B6` (Teal) instead of `F0EDE8` — this highlights the most practically useful column.

### Step 17 — ECE table data row template (Row 1: Zinc)

**17a — Row background:**
1. Add a Rectangle. Width: `13.5"`. Height: `0.6"`. Fill: `1A1F2E` (base).
2. Position: X: 0.5", Y: 7.6".

**17b — Row text (6 text boxes):**
- Metal column: `Zinc` — Inter Medium, `17` pt, `F0EDE8`. X: 0.7".
- Symbol: `Zn` — JetBrains Mono, `17` pt, `F0EDE8`. X: 2.8".
- Valence: `2` — JetBrains Mono, `17` pt, `F0EDE8`. X: 3.9".
- ECE: `1.220` — JetBrains Mono, `17` pt, `F0EDE8`. X: 5.2".
- Density: `7.14` — JetBrains Mono, `17` pt, `F0EDE8`. X: 7.6".
- Rate: `0.00152` — JetBrains Mono, `17` pt, `2EC4B6` (Teal). X: 10.2".

**17c — Group the row.**

### Step 18 — Duplicate and modify for Rows 2-10

Duplicate Row 1 group, reposition below, toggle base/alt fills. Each row is 0.6" tall.

| Row | Y | Fill | Metal | Symbol | Valence | ECE | Density | Rate |
|-----|---|------|-------|--------|---------|-----|---------|------|
| 2 | 8.20" | `#252B3D` | Nickel | Ni | 2 | 1.095 | 8.90 | 0.00109 |
| 3 | 8.80" | `#1A1F2E` | Copper (acid) | Cu | 2 | 1.186 | 8.96 | 0.00118 |
| 4 | 9.40" | `#252B3D` | Copper (cyanide) | Cu | 1 | 2.372 | 8.96 | 0.00236 |
| 5 | 10.00" | `#1A1F2E` | Chromium (hex) | Cr | 6 | 0.324 | 7.19 | 0.00040 |
| 6 | 10.60" | `#252B3D` | Silver | Ag | 1 | 4.025 | 10.49 | 0.00342 |
| 7 | 11.20" | `#1A1F2E` | Tin | Sn | 2 | 2.214 | 7.31 | 0.00270 |
| 8 | 11.80" | `#252B3D` | Copy-paste: `Gold (Au⁺)` | Au | 1 | 7.349 | 19.32 | 0.00339 |
| 9 | 12.40" | `#1A1F2E` | Copy-paste: `Gold (Au³⁺)` | Au | 3 | 2.450 | 19.32 | 0.00113 |
| 10 | 13.00" | `#252B3D` | Cadmium | Cd | 2 | 2.097 | 8.65 | 0.00216 |

For each row: duplicate the previous row group, reposition, ungroup, change the fill and text values, re-group.

**Remember:** Rate column text is always `2EC4B6` (Teal). All other numeric columns are `F0EDE8`.

### Step 19 — Table footnote
1. Add a text element. Copy-paste:
   `ECE = Atomic Weight / (Valence x 26.80 Ah). Rate = ECE / (Density x 60.5). All values are theoretical — multiply by cathode efficiency for actual deposit.`
2. Font: Inter Regular, Size: `12`, Color: `F0EDE8`, Transparency: **60%**, Style: *italic*
3. Position: X: 0.5", Y: 13.7". Width: 13.5".

### Step 20 — Copper valence callout
1. Add a text element. Copy-paste: `Cyanide copper (Cu⁺) deposits 2x the mass per amp-hour vs. acid copper (Cu²⁺) — same element, different chemistry.`
2. Font: Inter Regular, Size: `14`, Color: `E8A020` (Amber)
3. Position: X: 0.5", Y: 14.2". Width: 13.5".

### Step 21 — Cathode Efficiency section label
1. Add a text element. Type: `CATHODE EFFICIENCY`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: 14.5", Y: 6.6".

### Step 22 — Cathode Efficiency intro text
1. Add a text element. Type: `Not all current deposits metal. The rest generates hydrogen gas. Efficiency = actual deposit / theoretical maximum.`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`. Line height: **140%**.
3. Position: X: 14.5", Y: 7.0". Width: 9.0".

### Step 23 — Cathode Efficiency table header row

**23a — Header background:**
1. Add a Rectangle. Width: `9.0"`. Height: `0.45"`. Fill: `3A4055` (Mid Slate).
2. Position: X: 14.5", Y: 7.6".

**23b — Column headers:**
- `Process` — Barlow SemiBold, `16` pt, `F0EDE8`. X: 14.7". Width: 5.0".
- `Efficiency` — same font/size/color. X: 19.7". Width: 3.6".

### Step 24 — Cathode Efficiency data row template (Row 1: Bright Acid Copper)

**24a — Row background:**
1. Add a Rectangle. Width: `9.0"`. Height: `0.55"`. Fill: `1A1F2E` (base).
2. Position: X: 14.5", Y: 8.05".

**24b — Left border accent:**
1. Add a Rectangle. Width: `0.06"`. Height: `0.55"`. Fill: `27AE60` (Emerald).
2. Position: X: 14.5", Y: 8.05".

**24c — Process text:**
`Bright acid copper` — Inter Regular, `16` pt, `F0EDE8`. X: 14.75".

**24d — Efficiency text:**
`95-100%` — JetBrains Mono, `16` pt, `F0EDE8`. X: 19.7".

**24e — Group the row.**

### Step 25 — Duplicate and modify for Rows 2-11

| Row | Y | Fill | Left Border | Process | Efficiency |
|-----|---|------|-------------|---------|-----------|
| 2 | 8.60" | `#252B3D` | `#27AE60` | Nickel sulfamate | 95-100% |
| 3 | 9.15" | `#1A1F2E` | `#27AE60` | Silver cyanide | 95-100% |
| 4 | 9.70" | `#252B3D` | `#27AE60` | Watts nickel | 93-97% |
| 5 | 10.25" | `#1A1F2E` | `#27AE60` | Acid chloride zinc | 95-98% |
| 6 | 10.80" | `#252B3D` | `#27AE60` | Matte tin (acid) | 90-95% |
| 7 | 11.35" | `#1A1F2E` | `#E8A020` | Alkaline NC zinc | 70-80% |
| 8 | 11.90" | `#252B3D` | `#E8A020` | Alkaline cyanide zinc | 65-80% |
| 9 | 12.45" | `#1A1F2E` | `#E05C5C` | Cyanide copper strike | 30-60% |
| 10 | 13.00" | `#252B3D` | `#E05C5C` | Hard chrome (hex) | 12-20% |
| 11 | 13.55" | `#1A1F2E` | `#E05C5C` | Decorative chrome (hex) | 10-18% |

For each: duplicate, reposition, ungroup, change fill, accent bar color, process text, efficiency text, re-group.

### Step 26 — Group all of Zone 3
Select both section labels, intro text, both tables (headers + all rows), footnote, and copper valence callout. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Efficiency Bar Chart

This zone occupies Y: 19.7" to 24.4" (4.7 inches tall). Four horizontal bars comparing how much current goes to metal vs. waste.

### Step 27 — Section label
1. Add a text element. Type: `WHERE DOES THE CURRENT GO?`
2. Font: Barlow Condensed ExtraBold, Size: `24`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally, Y: 19.9". Width: 23.0".

### Step 28 — Build Bar 1 (Acid Copper — template)

Each bar consists of two adjacent rectangles: Emerald (metal deposited) on the left, Coral (wasted) on the right. Full bar width = 23.0" (from 0.5" to 23.5").

**28a — Emerald rectangle (metal deposited):**
1. Add a Rectangle. Width: `22.31"` (97% of 23.0"). Height: `0.65"`. Fill: `27AE60` (Emerald).
2. Position: X: 0.5", Y: 20.5".

**28b — Coral rectangle (wasted):**
1. Add a Rectangle. Width: `0.69"` (3% of 23.0"). Height: `0.65"`. Fill: `E05C5C` (Coral).
2. Position: X: 22.81" (flush against the right edge of the Emerald rectangle), Y: 20.5".

**28c — Process label:**
1. Add text: `Acid Copper` — Inter Medium, `16` pt, `F0EDE8`. Position: X: 0.7", vertically centered in the bar.

**28d — Emerald label:**
1. Add text: `97% metal` — JetBrains Mono, `14` pt, `1A1F2E` (dark text on green). Position: centered within the Emerald rectangle.

**28e — Coral label:**
1. Add text: `3%` — JetBrains Mono, `12` pt, `F0EDE8`. Position: centered within the Coral rectangle. (This bar is narrow — the text may barely fit. If it does not fit, place it just outside the Coral rectangle to the right.)

**28f — Group the bar.**

### Step 29 — Bar 2: Watts Nickel

1. Duplicate Bar 1 group. Reposition: Y: 21.3".
2. Ungroup. Changes:
   - Emerald width: `21.85"` (95%). Coral width: `1.15"` (5%). Reposition Coral: X: 22.35".
   - Process label: `Watts Nickel`
   - Emerald label: `95% metal`
   - Coral label: `5%`
3. Re-group.

### Step 30 — Bar 3: Acid Zinc

1. Duplicate Bar 1 group. Reposition: Y: 22.1".
2. Ungroup. Changes:
   - Emerald width: `22.08"` (96%). Coral width: `0.92"` (4%). Reposition Coral: X: 22.58".
   - Process label: `Acid Zinc`
   - Emerald label: `96% metal`
   - Coral label: `4%`
3. Re-group.

### Step 31 — Bar 4: Hard Chrome

1. Duplicate Bar 1 group. Reposition: Y: 22.9".
2. Ungroup. Changes:
   - **Emerald width: `3.45"` (15%)**. Position: X: 0.5".
   - **Coral width: `19.55"` (85%)**. Reposition Coral: X: 3.95".
   - Process label: `Hard Chrome`
   - Emerald label: `15%` (the bar is narrow — position the label centered in the green section; if it does not fit, place it just to the right of the green bar)
   - Coral label: Copy-paste: `85% wasted as H₂ + heat`
3. Re-group.

### Step 32 — Bar chart caption
1. Add a text element. Type: `Hard chrome: 85% of the electrical energy becomes hydrogen gas and heat — not metal.`
2. Font: Inter Medium, Size: `16`, Color: `E05C5C` (Coral), Alignment: Center
3. Position: centered horizontally, Y: 23.7".

### Step 33 — Group all of Zone 4
Select the section label, all 4 bar groups, and the caption. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Worked Examples + Conversions

This zone occupies Y: 24.4" to 32.4" (8.0 inches tall). Two worked examples on the left (65%), Faraday's constant + conversions on the right (35%).

### Step 34 — Worked Examples section label
1. Add a text element. Type: `WORKED EXAMPLES`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 24.6".

### Step 35 — Example 1: Zinc

**35a — Callout container:**
1. Add a Rounded Rectangle. Width: `14.5"`. Height: `3.0"`. Fill: `1E2435`. Corner radius: `6`.
2. Position: X: 0.5", Y: 25.1".

**35b — Left accent bar:**
1. Add a Rectangle. Width: `0.06"`. Height: `3.0"`. Fill: `27AE60` (Emerald).
2. Position: X: 0.5", Y: 25.1".

**35c — Title:**
1. Add text: `How long to plate 0.5 mil zinc at 20 ASF?`
2. Font: Barlow SemiBold, `18` pt, `27AE60` (Emerald). Position: X: 0.85", Y: 25.3".

**35d — Calculation:**
1. Add a text element. Copy-paste (each line separated by pressing Enter):
   ```
   Time = Thickness / (Rate x ASF x CE)
   Time = 0.5 / (0.00152 x 20 x 0.96)
   Time = 0.5 / 0.02918
   Time = 17.1 minutes
   ```
2. Font: JetBrains Mono Regular, `14` pt, `F0EDE8`. Line height: **160%**.
3. Position: X: 0.85", Y: 25.8". Width: 13.9".

**35e — Answer:**
1. Add text: `Approximately 17 minutes at 20 ASF.`
2. Font: Inter Medium, `16` pt, `27AE60` (Emerald). Position: X: 0.85", Y: 27.3".

**35f — Group Example 1.**

### Step 36 — Example 2: Hard Chrome

**36a — Callout container:**
1. Add a Rounded Rectangle. Width: `14.5"`. Height: `3.3"`. Fill: `1E2435`. Corner radius: `6`.
2. Position: X: 0.5", Y: 28.3".

**36b — Left accent bar:**
1. Add a Rectangle. Width: `0.06"`. Height: `3.3"`. Fill: `E05C5C` (Coral).
2. Position: X: 0.5", Y: 28.3".

**36c — Title:**
1. Add text: `How long for 2.0 mil hard chrome at 200 ASF?`
2. Font: Barlow SemiBold, `18` pt, `E05C5C` (Coral). Position: X: 0.85", Y: 28.5".

**36d — Calculation:**
1. Add a text element. Copy-paste:
   ```
   Time = 2.0 / (0.00040 x 200 x 0.15)
   Time = 2.0 / 0.012
   Time = 166.7 minutes ≈ 2 hr 47 min
   ```
2. Font: JetBrains Mono Regular, `14` pt, `F0EDE8`. Line height: **160%**.
3. Position: X: 0.85", Y: 29.0". Width: 13.9".

**36e — Answer:**
1. Add text: `Nearly 3 hours — 10x the current density, still takes 10x longer than zinc.`
2. Font: Inter Medium, `16` pt, `E05C5C` (Coral). Position: X: 0.85", Y: 30.5".

**36f — Group Example 2.**

### Step 37 — Faraday's Constant callout (right 35%)

**37a — Container:**
1. Add a Rounded Rectangle. Width: `8.0"`. Height: `2.8"`. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6` (Teal). Corner radius: `8`.
2. Position: X: 15.5", Y: 24.8".

**37b — Title:**
1. Add text: `FARADAY'S CONSTANT`
2. Font: Barlow SemiBold, `18` pt, `2EC4B6` (Teal). Position: X: 15.8", Y: 25.0".

**37c — Constant value:**
1. Add text: `F = 96,485 C/mol = 26.80 Ah/eq`
2. Font: JetBrains Mono Regular, `20` pt, `F0EDE8`, Alignment: Center
3. Position: centered within the container, Y: 25.5".

**37d — Explanation:**
1. Add text: `26.80 ampere-hours will deposit exactly one gram-equivalent weight of any metal.`
2. Font: Inter Regular, `14` pt, `F0EDE8`. Line height: **140%**.
3. Position: X: 15.8", Y: 26.2". Width: 7.4".

**37e — Group the Faraday callout.**

### Step 38 — Quick Conversions callout

**38a — Container:**
1. Add a Rounded Rectangle. Width: `8.0"`. Height: `3.5"`. Fill: `1E2435`. No border. Corner radius: `6`.
2. Position: X: 15.5", Y: 28.0".

**38b — Title:**
1. Add text: `QUICK CONVERSIONS`
2. Font: Barlow SemiBold, `16` pt, `F0EDE8`. Position: X: 15.8", Y: 28.2".

**38c — Conversion list:**
1. Add a text element. Copy-paste (each on its own line):
   ```
   1 mil = 25.4 um
   1 um = 0.0394 mil
   ASF / 10 ≈ ASD
   1 Ah = 3,600 C
   ```
2. Font: JetBrains Mono Regular, `16` pt, `F0EDE8`. Line height: **180%**.
3. Position: X: 15.8", Y: 28.7". Width: 7.4".

**38d — Group the conversions callout.**

### Step 39 — Group all of Zone 5
Select the section label, both example groups, and both right-side callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 40 — Footer band background
1. Add a Rectangle (sharp corners). Width: `24"`. Height: `3.6"`. Fill: `0D1020` (Deep Navy). No border.
2. Position: X: 0", Y: 32.4".

### Step 41 — Disclaimer text
1. Add a text element. Type:
   `This poster presents theoretical calculations from Faraday's Laws of Electrolysis. Actual deposit thickness depends on cathode efficiency, current distribution, agitation, and bath condition. Always verify critical thickness specifications by direct measurement.`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **50%**, Alignment: Center
3. Position: centered horizontally, Y: 32.8". Width: 23.0".

### Step 42 — Poster title (left)
1. Add a text element. Type: `Faraday's Law in the Shop: Calculating Plating Thickness`
2. Font: Barlow SemiBold, Size: `16`, Color: `F0EDE8`
3. Position: X: 0.5", Y: 33.5".

### Step 43 — Series name
1. Add a text element. Type: `Plating Posters Inc — Metal Finishing Reference Series`
2. Font: Inter Regular, Size: `13`, Color: `F0EDE8`, Transparency: **60%**
3. Position: X: 0.5", Y: 34.0".

### Step 44 — Version
1. Add a text element. Type: `v1.0 — 2026`
2. Font: Inter Regular, Size: `11`, Color: `F0EDE8`, Transparency: **40%**
3. Position: X: 0.5", Y: 34.4".

### Step 45 — Logo placeholder
1. Add a Rounded Rectangle. Width: `2.5"`. Height: `1.5"`. No fill or light fill `3A4055`. Position: X: 21.0", Y: 33.5".
2. Add text inside: `[LOGO]` — Barlow SemiBold, `14` pt, `F0EDE8`, Transparency: **30%**, Alignment: Center.

### Step 46 — Group all of Zone 6
Select the Deep Navy rectangle, disclaimer, poster title, series name, version, and logo placeholder. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline reads: `FARADAY'S LAW IN THE SHOP` in Barlow Condensed ExtraBold, `#F0EDE8`
- [ ] Subheading reads: `Calculating Plating Thickness` in Barlow SemiBold, `#E8A020`
- [ ] Tagline reads: `More amps x more time = more metal. Now do the math.` at 65% transparency
- [ ] "Three Questions" callout has Teal border and all 3 questions
- [ ] Formula reads: `Thickness = Rate x ASF x Time x Efficiency` in JetBrains Mono
- [ ] 4 variable legend items present with correct color swatches (Teal, Amber, Emerald, Coral)
- [ ] ECE table has 10 data rows with Rate column in Teal
- [ ] Cathode Efficiency table has 11 data rows with colored left accent bars
- [ ] Copper valence callout mentions Cu⁺ vs Cu²⁺
- [ ] 4 efficiency bars present: Acid Copper (97%), Watts Nickel (95%), Acid Zinc (96%), Hard Chrome (15%)
- [ ] Bar chart caption highlights chrome's 85% waste in Coral
- [ ] Zinc example: answer is approximately 17 minutes
- [ ] Chrome example: answer is approximately 2 hr 47 min
- [ ] Faraday's Constant callout shows 96,485 C/mol = 26.80 Ah/eq
- [ ] Quick Conversions has 4 entries
- [ ] Disclaimer, footer title, series name, LOGO placeholder, and version all present

### Color verification
- [ ] Background is `#1A1F2E`
- [ ] All body text is `#F0EDE8` — not pure white
- [ ] Rate column text is `#2EC4B6` (Teal)
- [ ] High-efficiency rows (Emerald accent): bright acid copper through matte tin
- [ ] Medium-efficiency rows (Amber accent): alkaline NC zinc, alkaline cyanide zinc
- [ ] Low-efficiency rows (Coral accent): cyanide copper strike, hard chrome, decorative chrome
- [ ] Emerald bar segments, Coral bar segments in chart
- [ ] Zinc example accent: Emerald. Chrome example accent: Coral.
- [ ] Footer band is `#0D1020`

### Layout verification
- [ ] All text stays within the 0.5-inch safe zone
- [ ] ECE table (left 60%) and Efficiency table (right 40%) do not overlap
- [ ] Bar chart bars span full content width (0.5" to 23.5")
- [ ] Worked examples and right-side callouts sit side by side
- [ ] No text is cut off or overlapping

### Readability check
- [ ] Zoom to 25% — headline, formula, and bar chart visible
- [ ] Zoom to 50% — metal names and efficiency values readable
- [ ] Zoom to 75% — ECE values and calculation steps readable
- [ ] Zoom to 100% — footnote and disclaimer readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 47 — Duplicate the page
1. Click the **...** menu on the page thumbnail > **Duplicate page**.
2. Switch to Page 2. Rename "Light Edition" if possible.

### Step 48 — Change the background
Change from `1A1F2E` to `F5F4F0` (Off-White).

### Step 49 — Remap all elements

Work through this table top to bottom, zone by zone:

| Element Type | What to Find | Change From | Change To |
|---|---|---|---|
| **Background** | Page background | `#1A1F2E` | `#F5F4F0` |
| **All body text** | Every text element in Warm White | `#F0EDE8` | `#1A1F2E` |
| **Callout box fills** | Formula background, callout containers, example containers, conversions box | `#1E2435` | `#ECEEF4` |
| **Alt row backgrounds** | Even-numbered data rows in both tables | `#252B3D` | `#E8E8F0` |
| **Base row backgrounds** | Odd-numbered data rows | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | Deep Navy rectangle | `#0D1020` | `#1A1F2E` |
| **Amber elements** | Subheading, ASF swatch, copper valence callout, Amber accent bars | `#E8A020` | `#C8860A` |
| **Teal elements** | Callout borders/titles, Rate column text, Rate header, Teal swatch, Faraday border | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | High-eff accent bars, Emerald swatch, Emerald bar segments, zinc example accent | `#27AE60` | `#1E7A47` |
| **Coral elements** | Low-eff accent bars, Coral swatch, Coral bar segments, chrome example accent | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | Table header fills, dividers | `#3A4055` | `#D0D4DE` |

### Step 50 — Post-remap adjustments

1. **Bar chart labels on Emerald bars:** The Dark edition uses `#1A1F2E` (dark text on green). In the Light edition, the darkened Emerald (`#1E7A47`) is dark — change these bar labels to `#F0EDE8` (Warm White, light text on dark green). Verify readability.
2. **Footnote text**: At 60% opacity, verify readability on Off-White. If too faint, increase to **75%**.
3. **Disclaimer text**: At 50% opacity, verify readability. If too faint, increase to **65%**.
4. **Tagline**: At 65% opacity, verify readability. Increase to **80%** if needed.
5. **Variable legend descriptions**: At 70% opacity, verify readability. Increase to **85%** if needed.

---

## Phase 10 — Export Instructions

### Step 51 — Export the Dark edition (Page 1)

**51a — Print PDF, 24x36":**
1. 
2. File type: **PDF Print**.
3. Check **Crop marks and bleed**.
4. Select only **Page 1**.
5. Download and rename to: `Faradays-Law-Dark-24x36-Print.pdf`

**51b — Digital PDF, 24x36":**
1. **Share** > **Download** > **PDF Standard**. Uncheck crop marks.
2. Select Page 1. Rename to: `Faradays-Law-Dark-Digital.pdf`

**51c — Print PDF, 18x24":**
1. 
2. Verify body text is at least 14 pt.
3. Export as PDF Print (with crop marks and bleed).
4. Rename to: `Faradays-Law-Dark-18x24-Print.pdf`

### Step 52 — Export the Light edition (Page 2)

Repeat Step 51 for Page 2 with these filenames:
- `Faradays-Law-Light-24x36-Print.pdf`
- `Faradays-Law-Light-Digital.pdf`
- `Faradays-Law-Light-18x24-Print.pdf`

### Export file checklist
- [ ] `Faradays-Law-Dark-24x36-Print.pdf`
- [ ] `Faradays-Law-Dark-18x24-Print.pdf`
- [ ] `Faradays-Law-Dark-Digital.pdf`
- [ ] `Faradays-Law-Light-24x36-Print.pdf`
- [ ] `Faradays-Law-Light-18x24-Print.pdf`
- [ ] `Faradays-Law-Light-Digital.pdf`

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background (Dark), body text (Light), bar chart dark text |
| `#F0EDE8` | Warm White | Body text (Dark) |
| `#E8A020` | Amber | Subheading, ASF swatch, copper valence callout, medium-eff accents |
| `#2EC4B6` | Teal | Callout borders, Rate column, Faraday box, Rate swatch |
| `#27AE60` | Emerald | High-eff accents, bar chart metal segments, zinc example, Time swatch |
| `#E05C5C` | Coral | Low-eff accents, bar chart waste segments, chrome example, Efficiency swatch |
| `#3A4055` | Mid Slate | Table header fills, dividers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout fills, formula background, example containers |
| `#252B3D` | Alt Row | Even-numbered data rows |
| `#F5F4F0` | Off-White | Background (Light edition) |
| `#ECEEF4` | Light Callout | Callout fills (Light edition) |
| `#E8E8F0` | Alt Row Light | Even rows (Light edition) |
| `#C8860A` | Amber Dark | Amber elements (Light edition) |
| `#1A8C82` | Teal Dark | Teal elements (Light edition) |
| `#1E7A47` | Forest Green | Emerald elements (Light edition) |
| `#B83E3E` | Deep Coral | Coral elements (Light edition) |
| `#D0D4DE` | Light Slate | Rules/dividers (Light edition) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-04 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v1.0 (2026-04-04). All technical content production-ready. Watson flags are non-blocking. |
