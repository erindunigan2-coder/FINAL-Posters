---
Project: Plating Posters Inc
Poster Number: 5
Title: "Anode-to-Cathode Ratio: Why It Matters More Than You Think"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 5 — Anode-to-Cathode Ratio — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - AnodeCathodeRatio
  - v1
---

# Claude Chat Generation Prompt — Poster #5
## Anode-to-Cathode Ratio: Why It Matters More Than You Think
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

## Phase 2 — Zone 1: Header Band

This zone occupies the top 2.9 inches. Headline + subheading + tagline on the left (~55%), "The Definition" callout on the right (~45%).

### Step 6 — Place the headline
1. Add a heading text element: Type: `ANODE-TO-CATHODE RATIO`
2. Font: Barlow Condensed ExtraBold, Size: `88`, Color: `F0EDE8`, Letter spacing: `-4`, Alignment: Left
3. Position: X: **0.5"**. Y: **0.5"**. Width: **12.5"**.

### Step 7 — Place the subheading
1. Add subheading. Type: `Why It Matters More Than You Think`
2. Font: Barlow SemiBold, Size: `36`, Color: `E8A020`, Alignment: Left
3. Position: X: **0.5"**. Y: approximately **1.5"**.

### Step 8 — Place the tagline
1. Add body text. Type: `The ratio that controls your current, your anodes, and your bath chemistry.`
2. Font: Barlow SemiBold, Size: `22`, Color: `F0EDE8`, Transparency: **65%**, Alignment: Left
3. Position: X: **0.5"**. Y: approximately **2.1"**.

### Step 9 — Build "The Definition" callout box

**9a — Container:**
1. Add Rounded Rectangle. Width: `10.25"`. Height: `2.2"`.
2. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6`. Corner radius: `8`.
3. Position: X: **13.25"**. Y: **0.5"**.

**9b — Title:**
1. Add text: `THE DEFINITION`
2. Font: Barlow SemiBold, Size: `18`, Color: `2EC4B6`
3. Position: X: **13.55"**. Y: **0.7"**.

**9c — Formula:**
1. Add text: `A:C = Anode Area / Cathode Area`
2. Font: JetBrains Mono Regular, Size: `22`, Color: `F0EDE8`, Alignment: Center
3. Position: centered in container. Y: approximately **1.0"**.

**9d — Examples:**
1. Add text (3 lines):
   `1:1 — anode equals cathode`
   `2:1 — anode is 2x cathode`
   `0.5:1 — anode is half cathode (under-anoded)`
2. Font: JetBrains Mono Regular, Size: `15`, Color: `F0EDE8`, Transparency: **80%**. Line height: `1.5`.
3. Position: X: **13.55"**. Y: **1.5"**.

**9e — Target line:**
1. Add text: `Most processes: target 1:1 to 2:1.`
2. Font: Inter Medium, Size: `16`, Color: `2EC4B6`
3. Position: X: **13.55"**. Y: **2.2"**.

**9f — Group callout.** Press **Ctrl+G**.

### Step 10 — Group all of Zone 1
Select headline, subheading, tagline, callout group. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 3 — Zone 2: Triple Tank Comparison (HERO)

This zone occupies Y: 2.9" to 13.7" (10.8 inches tall). Three plating tank cross-sections side by side showing under-anoded, correct ratio, and over-anoded conditions.

### Step 11 — Section label
1. Add text: `WHAT HAPPENS WHEN THE RATIO IS WRONG`
2. Font: Barlow Condensed ExtraBold, Size: `30`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally. Y: **3.1"**. Width: **23.0"**.

---

### Step 12 — TANK 1: Under-Anoded (Coral)

**12a — Tank label:**
1. Add text: `UNDER-ANODED`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `E05C5C`
3. Position: X: **0.5"**. Y: **3.8"**.

**12b — Ratio label:**
1. Add text: `A:C = 0.5:1`
2. Font: JetBrains Mono, Size: `16`, Color: `E05C5C`
3. Position: X: **5.5"** (right-aligned above tank). Y: **3.85"**.

**12c — Tank body:**
1. Add Rounded Rectangle. Width: `7.2"`. Height: `5.5"`.
2. Fill: `1E2435`. Border: 2 pt, `3A4055`. Corner radius: `4`.
3. Position: X: **0.5"**. Y: **4.3"**.

**12d — Electrolyte suggestion (optional):**
1. Add 2-3 horizontal lines inside the tank at `2EC4B6` (Teal), Transparency: **15%**, 1 pt stroke.

**12e — Anode (SMALL — this is the problem):**
1. Add Rectangle. Width: `0.8"`. Height: `3.5"`.
2. Fill: none. Border: 2 pt, `E05C5C`.
3. Position: X: **1.3"**. Y: **5.0"**.

**12f — Cathode (the part):**
1. Add Rectangle. Width: `1.2"`. Height: `4.5"`.
2. Fill: `C8D0D8` (Bright Silver).
3. Position: X: **5.5"**. Y: **4.8"**.

**12g — Deposit — UNEVEN:**
1. Top deposit (thick): Add Rectangle. Width: `0.3"`. Height: `1.5"`. Fill: `F0EDE8` at 80%.
   Position: X: **5.2"**. Y: **4.8"**.
2. Bottom deposit: NO rectangle — bare cathode face shows. This represents the skip/thin area.

**12h — Current flow lines (crowded at top):**
1. Add 4 lines from anode right face toward cathode top-left area. Bunch them close together.
   Stroke: 1 pt, `E05C5C`.
2. Add 1 sparse line toward cathode mid-section at **40%** opacity.

**12i — Callout labels:**
1. Add text: `BURNING` — JetBrains Mono, 12 pt, `E05C5C`. Position near top of cathode with a small arrow line.
2. Add text: `THIN / SKIP` — JetBrains Mono, 12 pt, `E05C5C`. Position near bottom of cathode.

**12j — Sub-label:**
1. Add text: `Current crowds at the nearest cathode surfaces. Edges burn. Recesses starve.`
2. Font: Inter Regular, Size: `14`, Color: `F0EDE8`, Alignment: Center
3. Position: X: **0.5"**. Y: **10.0"**. Width: **7.2"**.

**12k — Group Tank 1.** Select all Tank 1 elements. Press **Ctrl+G**.

---

### Step 13 — TANK 2: Correct Ratio (Emerald)

**13a — Tank label:** `CORRECT RATIO`
Font: Barlow Condensed ExtraBold, 22 pt, `27AE60`. Position: X: **8.05"**. Y: **3.8"**.

**13b — Ratio label:** `A:C = 1.5:1`
Font: JetBrains Mono, 16 pt, `27AE60`. Position: X: **13.0"**. Y: **3.85"**.

**13c — Tank body:**
Rounded Rectangle. Width: `7.2"`. Height: `5.5"`.
Fill: `1E2435`. Border: 2 pt, `3A4055`. Corner radius: `4`.
Position: X: **8.05"**. Y: **4.3"**.

**13d — Anode (PROPER size):**
Rectangle. Width: `1.5"`. Height: `4.5"`. Fill: none. Border: 2 pt, `27AE60`.
Position: X: **8.85"**. Y: **4.7"**.

**13e — Cathode:**
Rectangle. Width: `1.2"`. Height: `4.5"`. Fill: `C8D0D8`.
Position: X: **13.0"**. Y: **4.8"**.

**13f — Deposit — UNIFORM:**
Rectangle. Width: `0.25"`. Height: `4.5"`. Fill: `F0EDE8` at 80%.
Position: X: **12.75"**. Y: **4.8"**.

**13g — Current flow lines (evenly spaced):**
5 parallel lines from anode to cathode, evenly distributed vertically. Stroke: 1 pt, `27AE60`.

**13h — Sub-label:**
`Current distributes evenly. Uniform deposit. Bath stays balanced.`
Font: Inter Regular, 14 pt, `F0EDE8`, Center. Position: X: **8.05"**. Y: **10.0"**. Width: **7.2"**.

**13i — Group Tank 2.** Press **Ctrl+G**.

---

### Step 14 — TANK 3: Over-Anoded (Amber)

**14a — Tank label:** `OVER-ANODED`
Font: Barlow Condensed ExtraBold, 22 pt, `E8A020`. Position: X: **15.6"**. Y: **3.8"**.

**14b — Ratio label:** `A:C = 3:1`
Font: JetBrains Mono, 16 pt, `E8A020`. Position: X: **20.5"**. Y: **3.85"**.

**14c — Tank body:**
Rounded Rectangle. Width: `7.2"`. Height: `5.5"`.
Fill: `1E2435`. Border: 2 pt, `3A4055`. Corner radius: `4`.
Position: X: **15.6"**. Y: **4.3"**.

**14d — Anode (LARGE — over-anoded):**
Rectangle. Width: `2.5"`. Height: `5.0"`. Fill: none. Border: 2 pt, `E8A020`.
Position: X: **16.2"**. Y: **4.5"**.

**14e — Cathode:**
Rectangle. Width: `1.2"`. Height: `4.5"`. Fill: `C8D0D8`.
Position: X: **20.5"**. Y: **4.8"**.

**14f — Deposit — reasonably uniform:**
Rectangle. Width: `0.25"`. Height: `4.5"`. Fill: `F0EDE8` at 80%.
Position: X: **20.25"**. Y: **4.8"**.

**14g — Current flow lines (evenly spaced):**
5 parallel lines, evenly distributed. Stroke: 1 pt, `E8A020`.

**14h — Dissolution arrows (excess):**
1. Add 3 small lines from the anode LEFT face into the solution, pointing left.
2. Stroke: 1.5 pt, `E8A020`, with arrowheads.
3. Add label: `Excess dissolution` — Inter Regular, 11 pt, `E8A020`.

**14i — Sub-label:**
`Generally acceptable. Excess anode area may over-dissolve, raising metal concentration.`
Font: Inter Regular, 14 pt, `F0EDE8`, Center. Position: X: **15.6"**. Y: **10.0"**. Width: **7.2"**.

**14j — Group Tank 3.** Press **Ctrl+G**.

---

### Step 15 — Key insight banner
1. Add text: `Under-anoded is the critical failure. Over-anoded is usually tolerable.`
2. Font: Inter Medium, Size: `18`, Color: `F0EDE8`, Alignment: Center
3. Position: centered horizontally. Y: **10.6"**. Width: **22.0"**.

### Step 16 — Group all of Zone 2
Select the section label, all 3 tank groups, and the insight banner. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 4 — Zone 3: A:C Ratio Table

This zone occupies Y: 13.7" to 22.3" (8.6 inches tall). An 11-row process table with recommended ratios.

### Step 17 — Section label
1. Add text: `IDEAL A:C RATIOS BY PROCESS`
2. Font: Barlow Condensed ExtraBold, Size: `26`, Color: `F0EDE8`
3. Position: X: **0.5"**. Y: **13.9"**.

### Step 18 — Column header row
1. Add Rectangle. Width: `23.0"`. Height: `0.5"`. Fill: `3A4055`.
2. Position: X: **0.5"**. Y: **14.4"**.
3. Add 4 header texts:
   - `Process` — X: **0.7"**, Barlow SemiBold, 18 pt, `F0EDE8`
   - `Ideal A:C` — X: **7.2"**, Barlow SemiBold, 18 pt, `2EC4B6` (Teal)
   - `Anode Type` — X: **10.7"**, Barlow SemiBold, 18 pt, `F0EDE8`
   - `Notes` — X: **16.2"**, Barlow SemiBold, 18 pt, `F0EDE8`

### Step 19 — Build Row 1 (Template): Acid copper sulfate

**19a — Row background:**
Rectangle. Width: `23.0"`. Height: `0.6"`. Fill: `1A1F2E`. No border.
Position: X: **0.5"**. Y: **14.9"**.

**19b — Process:** `Acid copper sulfate` — Inter Medium, 17 pt, `F0EDE8`. X: **0.7"**.
**19c — Ideal A:C:** `1:1 to 2:1` — JetBrains Mono, 17 pt, `2EC4B6`. X: **7.2"**.
**19d — Anode Type:** `Cu-P (phosphorized)` — Inter Regular, 16 pt, `F0EDE8`. X: **10.7"**.
**19e — Notes:** `Cu-P film regulates dissolution` — Inter Regular, 15 pt, `F0EDE8`. X: **16.2"**.

**19f — Group Row 1.** Press **Ctrl+G**.

### Step 20 — Build Rows 2–11 (Duplicate and Modify)

Duplicate Row 1, reposition flush below, alternate base/alt fills. Each row is 0.6" tall.

| Row | Y | Fill | Process | Ideal A:C | Anode Type | Notes |
|-----|---|------|---------|-----------|------------|-------|
| 2 | 15.50" | alt | Cyanide copper | 1:1 to 1.5:1 | OFHC copper | Higher A:C increases CN⁻ consumption |
| 3 | 16.10" | base | Watts nickel (bright) | 1:1 to 2:1 | Ni R-Rounds (Ti baskets) | Bag anodes to contain sludge |
| 4 | 16.70" | alt | Nickel sulfamate | 1:1 to 2:1 | Ni S-Rounds (Ti baskets) | Higher A:C preferred — uniform dissolution |
| 5 | 17.30" | base | Acid chloride zinc | 1:1 to 1.5:1 | Zinc slabs/balls | High KCl increases dissolution rate |
| 6 | 17.90" | alt | Alkaline NC zinc | 1:1 to 2:1 | Steel plates (insoluble) | Current distribution only — add ZnO |
| 7 | 18.50" | base | Alkaline cyanide zinc | 1:1 to 2:1 | Zinc balls (steel baskets) | Lower A:C may be preferred |
| 8 | 19.10" | alt | Decorative chrome (hex) | 1:1 to 3:1 | Lead-tin (7% Sn) | A:C affects covering power |
| 9 | 19.70" | base | Hard chrome | 1:1 to 3:1 | Lead-tin or Pb-Sb | Conforming anodes → 1:1 at all points |
| 10 | 20.30" | alt | Silver cyanide | 1:1 to 2:1 | High-purity Ag (>99.9%) | Maintain anode area >= cathode area |
| 11 | 20.90" | base | Matte tin | 1:1 to 1.5:1 | Pure tin (Zr baskets) | Ti baskets would passivate |

**Copy-paste the CN⁻ in Row 2 from this document.**

---

### Step 21 — Group all of Zone 3
Select section label, column header, and all 11 data rows. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 5 — Zone 4: Symptoms + Calculation

This zone occupies Y: 22.3" to 28.8" (6.5 inches tall). Left 55% has two symptom callouts. Right 45% has a worked calculation and fist rule.

### Step 22 — Section label (left)
1. Add text: `SYMPTOMS OF INCORRECT RATIO`
2. Font: Barlow Condensed ExtraBold, Size: `22`, Color: `F0EDE8`
3. Position: X: **0.5"**. Y: **22.5"**.

### Step 23 — Under-Anoded symptom callout

**23a — Container:**
Rounded Rectangle. Width: `12.5"`. Height: `2.4"`. Fill: `1E2435`. Corner radius: `6`. No border.
Position: X: **0.5"**. Y: **23.0"**.

**23b — Left accent bar:**
Rectangle. Width: `0.06"`. Height: `2.4"`. Fill: `E05C5C`.
Position: X: **0.5"**. Y: **23.0"**.

**23c — Title:**
`UNDER-ANODED (A:C TOO LOW)` — Barlow SemiBold, 18 pt, `E05C5C`. X: **0.85"**. Y: **23.15"**.

**23d — Bullets:**
Type these 5 lines:
`- Burning at edges and HCD zones`
`- Poor throwing power — thin LCD coverage`
`- Rising bath voltage`
`- Metal concentration dropping`
`- Anode passivation risk`

Font: Inter Regular, 15 pt, `F0EDE8`. Line height: `1.5`. Width: **12.0"**.
Position: X: **0.85"**. Y: **23.55"**.

**23e — Group.** Press **Ctrl+G**.

### Step 24 — Over-Anoded symptom callout

**24a — Container:**
Rounded Rectangle. Width: `12.5"`. Height: `2.0"`. Fill: `1E2435`. Corner radius: `6`.
Position: X: **0.5"**. Y: **25.6"**.

**24b — Left accent bar:**
Rectangle. Width: `0.06"`. Height: `2.0"`. Fill: `E8A020`.
Position: X: **0.5"**. Y: **25.6"**.

**24c — Title:**
`OVER-ANODED (A:C TOO HIGH)` — Barlow SemiBold, 18 pt, `E8A020`. X: **0.85"**. Y: **25.75"**.

**24d — Bullets:**
`- Rising metal concentration (some processes)`
`- Sludge formation (nickel)`
`- Wasted anode material`
`- Generally less problematic than under-anoded`

Font: Inter Regular, 15 pt, `F0EDE8`. Line height: `1.5`.
Position: X: **0.85"**. Y: **26.15"**.

**24e — Group.** Press **Ctrl+G**.

### Step 25 — Worked calculation callout (right side)

**25a — Container:**
Rounded Rectangle. Width: `10.0"`. Height: `4.2"`.
Fill: `1E2435`. Border: 1.5 pt, `2EC4B6`. Corner radius: `8`.
Position: X: **13.5"**. Y: **22.6"**.

**25b — Title:**
`QUICK CALCULATION` — Barlow SemiBold, 18 pt, `2EC4B6`. X: **13.8"**. Y: **22.8"**.

**25c — Calculation text:**
Copy-paste these lines exactly:
`20 cylinders, 2" dia x 6" long`
`Each: pi x 2 x 6 = 37.7 in² = 0.262 ft²`
`Total cathode: 20 x 0.262 = 5.24 ft²`
(blank line)
`2 anode baskets, 6" x 24" x 2 sides`
`Each: 288 in² / 144 = 2.0 ft²`
`Total anode: 2 x 2.0 = 4.0 ft²`
(blank line)
`A:C = 4.0 / 5.24 = 0.76:1`

Font: JetBrains Mono Regular, Size: `13`, Color: `F0EDE8`. Line height: `1.6`. Width: **9.4"**.
Position: X: **13.8"**. Y: **23.2"**.

**25d — Answer:**
`Under-anoded! Add a third basket.` — Inter Medium, 15 pt, `E05C5C`.
Position: X: **13.8"**. Y: **26.0"**.

**25e — Group.** Press **Ctrl+G**.

### Step 26 — Fist Rule callout

**26a — Container:**
Rounded Rectangle. Width: `10.0"`. Height: `1.5"`.
Fill: `1E2435`. Corner radius: `6`. No border.
Position: X: **13.5"**. Y: **27.1"**.

**26b — Title:**
`THE FIST RULE` — Barlow SemiBold, 16 pt, `E8A020`. X: **13.8"**. Y: **27.25"**.

**26c — Value:**
Copy-paste: `1 clenched fist ≈ 0.33 ft²`
Font: JetBrains Mono Regular, Size: `18`, Color: `F0EDE8`. X: **13.8"**. Y: **27.6"**.

**26d — Description:**
`A quick estimation method for cathode surface area — from Drew's field notes.`
Font: Inter Regular, 13 pt, `F0EDE8`, Transparency: **70%**. X: **13.8"**. Y: **28.0"**.

**26e — Group.** Press **Ctrl+G**.

### Step 27 — Group all of Zone 4
Select section label, both symptom callouts, calculation callout, and fist rule callout. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 6 — Zone 5: Maintenance + Passivation Warning

This zone occupies Y: 28.8" to 32.4" (3.6 inches tall). Left 50% is a maintenance checklist. Right 50% is a passivation warning.

### Step 28 — Anode Maintenance callout (left)

**28a — Container:**
Rounded Rectangle. Width: `11.2"`. Height: `3.3"`.
Fill: `1E2435`. Border: 1.5 pt, `27AE60` (Emerald). Corner radius: `8`.
Position: X: **0.5"**. Y: **28.8"**.

**28b — Title:**
`ANODE MAINTENANCE` — Barlow SemiBold, 18 pt, `27AE60`. X: **0.8"**. Y: **29.0"**.

**28c — Bullets:**
`- Bag all soluble anodes — contain sludge`
`- Replace consumed anodes before they get too small`
`- Clean anode contacts — corrosion = resistance`
`- Verify anode composition — wrong alloy = wrong dissolution`
`- Submerge anodes to proper depth — exposed surface = uneven current`
`- Inspect anode bags — holes defeat the purpose`

Font: Inter Regular, 15 pt, `F0EDE8`. Line height: `1.45`. Width: **10.6"**.
Position: X: **0.8"**. Y: **29.4"**.

**28d — Group.** Press **Ctrl+G**.

### Step 29 — Anode Passivation warning (right)

**29a — Container:**
Rounded Rectangle. Width: `11.5"`. Height: `3.3"`.
Fill: `1E2435`. Border: 2 pt, `E05C5C` (Coral). Corner radius: `8`.
Position: X: **12.0"**. Y: **28.8"**.

**29b — Title:**
`ANODE PASSIVATION` — Barlow SemiBold, 18 pt, `E05C5C`. X: **12.3"**. Y: **29.0"**.

**29c — Body:**
`When anode current density gets too high, a dense oxide film forms on the anode surface and stops dissolution entirely.`
Font: Inter Regular, 15 pt, `F0EDE8`. Line height: `1.4`. Width: **10.9"**.
Position: X: **12.3"**. Y: **29.4"**.

**29d — Symptoms:**
`Voltage rises sharply | Metal drops | Current distribution degrades`
Font: Inter Medium, 14 pt, `E05C5C`. Position: X: **12.3"**. Y: **30.3"**.

**29e — Fix:**
`Increase anode area. Verify anode composition. Check chloride level.`
Font: Inter Medium, 14 pt, `27AE60`. Position: X: **12.3"**. Y: **30.8"**.

**29f — Group.** Press **Ctrl+G**.

### Step 30 — Group all of Zone 5
Select both callout groups. Press **Ctrl+G**. Right-click > **Lock**.

---

## Phase 7 — Zone 6: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 31 — Footer band background
Rectangle. Width: `24"`. Height: `3.6"`. Fill: `0D1020`. No border.
Position: X: **0"**. Y: **32.4"**.

### Step 32 — Disclaimer
`This poster presents general anode-to-cathode ratio guidelines. Specific ratios depend on tank geometry, anode type, and product formulation. Consult your process supplier for application-specific recommendations.`
Font: Inter Regular, 11 pt, `F0EDE8`, Transparency: **50%**, Alignment: Center. Width: **23.0"**.
Position: centered horizontally. Y: **32.8"**.

### Step 33 — Poster title
`Anode-to-Cathode Ratio: Why It Matters More Than You Think`
Font: Barlow SemiBold, 16 pt, `F0EDE8`. X: **0.5"**. Y: **33.5"**.

### Step 34 — Series name
`Plating Posters Inc — Metal Finishing Reference Series`
Font: Inter Regular, 13 pt, `F0EDE8`, Transparency: **60%**. X: **0.5"**. Y: **34.0"**.

### Step 35 — Version
`v1.0 — 2026` — Inter Regular, 11 pt, `F0EDE8`, Transparency: **40%**. X: **0.5"**. Y: **34.4"**.

### Step 36 — Logo placeholder
`[LOGO]` — Barlow SemiBold, 14 pt, `F0EDE8`, Transparency: **30%**, Center. X: **21.0"**. Y: **33.5"**. Width: **2.5"**.

### Step 37 — Group all of Zone 6. Press **Ctrl+G**.

---

## Phase 8 — Final Review Checklist

### Text verification
- [ ] Headline: `ANODE-TO-CATHODE RATIO`
- [ ] Callout formula: `A:C = Anode Area / Cathode Area`
- [ ] Tank 1 labeled `UNDER-ANODED` with `A:C = 0.5:1` in Coral
- [ ] Tank 2 labeled `CORRECT RATIO` with `A:C = 1.5:1` in Emerald
- [ ] Tank 3 labeled `OVER-ANODED` with `A:C = 3:1` in Amber
- [ ] Tank 1 anode is SMALL, deposit is UNEVEN (thick top, bare bottom)
- [ ] Tank 2 anode is PROPER size, deposit is UNIFORM
- [ ] Tank 3 anode is LARGE, has dissolution arrows
- [ ] Insight banner: `Under-anoded is the critical failure...`
- [ ] Ratio table has 11 rows (Acid copper through Matte tin)
- [ ] Worked calculation arrives at `A:C = 0.76:1` → `Under-anoded!`
- [ ] Fist Rule: `1 clenched fist ≈ 0.33 ft²`
- [ ] Maintenance checklist has 6 bullet points
- [ ] Passivation warning has symptoms and fix lines

### Color verification
- [ ] Coral for under-anoded throughout
- [ ] Emerald for correct ratio throughout
- [ ] Amber for over-anoded throughout
- [ ] Teal for callout borders and Ideal A:C column

### Readability check
- [ ] 25% zoom — headline and tank labels readable
- [ ] 50% zoom — ratio labels and section titles readable
- [ ] 75% zoom — table data and calculation readable
- [ ] 100% — footnotes, disclaimer, fist rule description readable

---

## Phase 9 — Light Edition: Remap Instructions

### Step 38 — Duplicate the page. Switch to Page 2.

### Step 39 — Change background from `1A1F2E` to `F5F4F0`.

### Step 40 — Remap all elements

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Callout fills** | `#1E2435` | `#ECEEF4` |
| **Alt row fills** | `#252B3D` | `#E8E8F0` |
| **Base row fills** | `#1A1F2E` | `#F5F4F0` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Mid Slate elements** | `#3A4055` | `#D0D4DE` |
| **Bright Silver cathode** | `#C8D0D8` | `#3A4055` |

**No overrides required.** Standard remap applies throughout.

### Step 41 — Post-remap adjustments
1. Verify tank outlines (remapped Mid Slate to light neutral) are clearly visible on the Off-White background.
2. Verify footnotes and disclaimer are readable at reduced opacity.
3. Verify deposit (now dark on light cathode) is clearly distinguishable.

---

## Phase 10 — Export Instructions

### Step 42 — Export Dark edition
- PDF Print 24x36" → `Anode-Cathode-Ratio-Dark-24x36-Print.pdf`
- PDF Standard → `Anode-Cathode-Ratio-Dark-Digital.pdf`
- Resize 18x24" → `Anode-Cathode-Ratio-Dark-18x24-Print.pdf`

### Step 43 — Export Light edition
- `Anode-Cathode-Ratio-Light-24x36-Print.pdf`
- `Anode-Cathode-Ratio-Light-Digital.pdf`
- `Anode-Cathode-Ratio-Light-18x24-Print.pdf`

### Export file checklist
- [ ] 6 files total (Dark + Light, each in 24x36 Print, 18x24 Print, Digital)

---

## Quick Reference — All Hex Codes Used

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background, base rows |
| `#F0EDE8` | Warm White | Body text |
| `#F5F4F0` | Off-White | Light edition background |
| `#E8A020` | Amber | Over-anoded, subheading |
| `#2EC4B6` | Teal | Callout borders, A:C column |
| `#27AE60` | Emerald | Correct ratio, maintenance |
| `#E05C5C` | Coral | Under-anoded, passivation |
| `#3A4055` | Mid Slate | Tank outlines, headers |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout/tank fills |
| `#252B3D` | Alt Row | Alternating rows |
| `#C8D0D8` | Bright Silver | Cathode/deposit |

---

*Originally engineered by Elara — Plating Posters Inc Prompt Architect*
*Poster #5 — Anode-to-Cathode Ratio — Claude Chat Generation Prompt v2.0*
*2026-04-04*
