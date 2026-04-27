---
Project: Plating Posters Inc
Poster Number: 17
Title: "The Galvanic Series — Why Metals Corrode in Contact"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-20T00:00:00
Source: Poster 17 — The Galvanic Series — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - GalvanicSeries
  - Corrosion
  - v1
---

# Claude Chat Generation Prompt — Poster #17
## The Galvanic Series — Why Metals Corrode in Contact
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup v2.0. Adapted for Claude chat visual generation (2026-04-20). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS. The output should be a finished, print-ready poster design.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first** (dark background). The Light edition remap table is provided at the end.
- Follow the design specifications in each Phase below. They describe WHAT to render — layout zones, text content, colors, typography, and visual elements.
- Every color is specified as a hex code. Every font, size, and weight is specified. Follow them exactly.
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
| Amber | `#E8A020` | Mid-series bars, neutral metals |
| Teal | `#2EC4B6` | Cell illustration, callout borders |
| Emerald | `#27AE60` | Noble/cathodic metals (bottom of chart) |
| Coral | `#E05C5C` | Active/anodic metals (top of chart) |
| Mid Slate | `#3A4055` | Chart dividers, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Callout fills |
| Alt Row | `#252B3D` | Reserve |
| Bright Silver | `#C8D0D8` | Steel/substrate illustration fills |
| Coral Light | `#F08080` | Active end gradient (upper-mid chart) |
| Amber Mid | `#D89020` | Middle of gradient transition |

### Layout Safe Zones
- **0.5" margin** on all sides
- All content must stay within the 23" x 35" live area

---

## Phase 2 — Zone 1: Header Band

This zone occupies the top 2.9 inches.

### Step 6 — Place the headline
1. Text: `THE GALVANIC SERIES`
2. Font: Barlow Condensed ExtraBold, Size: `96`, Color: `#F0EDE8`, Letter spacing: `-4`
3. Position: X: **0.5"**, Y: **0.5"**. Width: `23.0"`.

### Step 7 — Place the subheading
1. Text: `Why Metals Corrode in Contact`
2. Font: Barlow SemiBold, Size: `40`, Color: `#E8A020` (Amber)
3. Position: X: **0.5"**, Y: **1.6"**.

### Step 8 — Place the tagline
1. Text: `Corrosion is the reason plating exists.`
2. Font: Barlow SemiBold, Size: `22`, Color: `#F0EDE8`, Transparency: **65%**
3. Position: X: **0.5"**, Y: **2.3"**.

### Step 9 — Group all of Zone 1

---

## Phase 3 — Zone 2: Main Content (Two-Column Layout)

This zone occupies Y: 2.9" to 25.5" (~22.6" tall). Left column = Galvanic Series Chart. Right column = Cell components, examples, and potential differences.

### LEFT COLUMN — Galvanic Series Chart (HERO)

### Step 10 — Section label
1. Text: `GALVANIC SERIES (SEAWATER)`
2. Font: Barlow Condensed ExtraBold, `26` pt, `#F0EDE8`, Alignment: Center within column
3. Position: X: **0.5"**, Y: **3.1"**. Width: `11.0"`.

### Step 11 — Sub-label
1. Text (two lines):
   ```
   Active (anodic) at top → Noble (cathodic) at bottom
   Reference data — relative comparison only, not lab-precision values
   ```
2. Font: Inter Regular, `14` pt, `#F0EDE8` at 60%, Alignment: Center
3. Position: X: **0.5"**, Y: **3.7"**. Width: `11.0"`.

### Step 12 — Chart container
- Rectangle. Position: X: **0.5"**, Y: **4.3"**. Width: `11.0"`. Height: `20.7"`.
- Fill: `#1E2435`. No border.

### Step 13 — Top axis label
- Text: `↑ ACTIVE / ANODIC (corrodes preferentially)`
- Font: Barlow SemiBold, `14` pt, `#E05C5C`. Alignment: Center.
- Position: X: **0.5"**, Y: **4.4"**. Width: `11.0"`.

### Step 14 — Build 16 chart bars

Each bar: Rectangle, Width: `10.6"`, Height: `1.1"`, positioned at X: **0.7"**, stacked from Y: **4.9"** incrementing by **1.2"** per bar. Use 1 pt borders between bars in `#1A1F2E`.

Each bar contains:
- Metal name (left): Inter Medium, `18` pt, `#F0EDE8` (or `#1A1F2E` on light fills). X: **0.9"**.
- Potential value (right): JetBrains Mono Regular, `16` pt, `#F0EDE8` (or `#1A1F2E`). Right-aligned at X: ~**11.2"**.

| # | Metal / Alloy | Potential vs. SCE (V) | Bar Fill |
|---|---------------|------------------------|----------|
| 1 | Magnesium | -1.60 | `#E05C5C` (Coral) |
| 2 | Zinc | -1.03 | `#E05C5C` |
| 3 | Aluminum (5052) | -0.85 | `#F08080` (Coral Light) |
| 4 | Cadmium | -0.80 | `#F08080` |
| 5 | Carbon Steel | -0.70 | `#E8A020` (Amber) |
| 6 | Cast Iron | -0.68 | `#E8A020` |
| 7 | 304 Stainless (active) | -0.53 | `#E8A020` |
| 8 | Lead | -0.31 | `#D89020` (Amber Mid) |
| 9 | Tin | -0.31 | `#D89020` |
| 10 | Brass | -0.30 | `#D89020` |
| 11 | Copper | -0.22 | `#D89020` |
| 12 | Bronze | -0.20 | `#27AE60` at 60% |
| 13 | Nickel (passive) | -0.07 | `#27AE60` at 70% |
| 14 | 304 Stainless (passive) | -0.05 | `#27AE60` at 80% |
| 15 | Silver | +0.13 | `#27AE60` |
| 16 | Platinum / Gold | +0.20 / +1.20 | `#27AE60` |

### Step 15 — Bottom axis label
- Text: `↓ NOBLE / CATHODIC (resists corrosion)`
- Font: Barlow SemiBold, `14` pt, `#27AE60`. Alignment: Center.
- Position: X: **0.5"**, Y: **24.5"**. Width: `11.0"`.

### RIGHT COLUMN — Cell Components, Examples, Potentials

### Step 16 — Four Components of a Galvanic Cell (Block C)

**16a — Section label:**
- Text: `THE FOUR COMPONENTS OF A GALVANIC CELL`
- Font: Barlow Condensed ExtraBold, `22` pt, `#F0EDE8`, Center. Position: X: **12.5"**, Y: **3.1"**. Width: `11.0"`.

**16b — Cell illustration container:**
- Rounded rectangle. X: **12.5"**, Y: **3.7"**. Width: `11.0"`. Height: `7.0"`.
- Fill: `#1E2435`. Corner radius: `8`. Left-border accent: `0.06"` wide, `#2EC4B6`.

**16c — Anode block:**
- Rectangle. X: **13.5"**, Y: **6.0"**. Width: `1.5"`. Height: `3.0"`. Fill: `#E05C5C`.
- Label below: `ANODE` — Barlow SemiBold, `14` pt, `#E05C5C`.
- Sub-label: `(loses electrons, corrodes)` — Inter Regular, `11` pt, `#F0EDE8` at 70%.

**16d — Cathode block:**
- Rectangle. X: **21.0"**, Y: **6.0"**. Width: `1.5"`. Height: `3.0"`. Fill: `#27AE60`.
- Label below: `CATHODE` — Barlow SemiBold, `14` pt, `#27AE60`.
- Sub-label: `(gains electrons, protected)` — Inter Regular, `11` pt, `#F0EDE8` at 70%.

**16e — Electronic path (wire arc):**
- Curved line from anode top to cathode top. Stroke: 2 pt, `#E8A020`. Arrowhead at cathode end.
- Label above: `Electronic path (wire)` — Inter Regular, `12` pt, `#E8A020`.
- Arc spans X: **14.25"** to **21.75"**, Y: **4.5"** to **5.8"**.

**16f — Ionic path (electrolyte zone):**
- Rectangle. X: **15.0"**, Y: **7.0"**. Width: `6.0"`. Height: `1.5"`.
- Fill: `#2EC4B6` at 25% opacity. Border: 1 pt dashed, `#2EC4B6`.
- Label inside: `Ionic path (electrolyte)` — Inter Regular, `12` pt, `#2EC4B6`. Centered.

**16g — Key takeaway:**
- Text: `Eliminate any one component to stop corrosion.`
- Font: Barlow SemiBold, `16` pt, `#F0EDE8`, Center.
- Position: X: **12.8"**, Y: **9.7"**. Width: `10.4"`.

### Step 17 — Anodic vs. Cathodic Coatings (Block D)

**17a — Section label:**
- Text: `ANODIC vs. CATHODIC COATINGS`
- Font: Barlow Condensed ExtraBold, `22` pt, `#F0EDE8`, Center.
- Position: X: **12.5"**, Y: **11.4"**. Width: `11.0"`.

**17b — Example 1: Zinc on Steel (anodic / protective):**
- Container: Rounded rectangle, X: **12.5"**, Y: **12.0"**, W: `11.0"`, H: `3.5"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `3.5"`, fill `#27AE60`.
- Title: `ZINC ON STEEL — Sacrificial Protection` — Barlow SemiBold, `18` pt, `#27AE60`. X: **12.8"**, Y: **12.2"**.
- Cross-section (right side):
  - Steel substrate: Rectangle, X: **18.0"**, Y: **13.5"**, W: `5.0"`, H: `0.8"`, fill `#C8D0D8`.
  - Zinc coating: Rectangle, X: **18.0"**, Y: **13.0"**, W: `5.0"`, H: `0.5"`, fill `#E05C5C`.
  - Pore gap in zinc: small rectangle at X: **20.5"**, W: `0.3"`, fill matches background.
  - Label: `Zinc (corrodes)` — `10` pt, `#E05C5C`, above zinc.
  - Label: `Steel (protected)` — `10` pt, `#27AE60`, below steel.
- Body text (left): `Even at a coating breach, the zinc continues to corrode preferentially and protect the exposed steel.`
  - Inter Regular, `13` pt, `#F0EDE8`, Width: `5.0"`. X: **12.8"**, Y: **12.7"**.

**17c — Example 2: Nickel on Steel (cathodic / risky):**
- Container: Rounded rectangle, X: **12.5"**, Y: **15.7"**, W: `11.0"`, H: `3.5"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `3.5"`, fill `#E05C5C`.
- Title: `NICKEL ON STEEL — Pore = Failure` — Barlow SemiBold, `18` pt, `#E05C5C`. X: **12.8"**, Y: **15.9"**.
- Cross-section (right side):
  - Steel substrate: Rectangle, X: **18.0"**, Y: **17.2"**, W: `5.0"`, H: `0.8"`, fill `#C8D0D8`.
  - Nickel coating: Rectangle, X: **18.0"**, Y: **16.7"**, W: `5.0"`, H: `0.5"`, fill `#27AE60`.
  - Pore: small gap at X: **20.5"**, W: `0.3"`.
  - Pit in steel below pore: small Coral circle at X: **20.5"**, Y: **17.5"**.
  - Label: `Nickel (intact)` — `10` pt, `#27AE60`.
  - Label: `Steel (corrodes at pore)` — `10` pt, `#E05C5C`.
- Body text (left): `Any pore in the nickel exposes the steel and concentrates corrosion at a single point — pitting failure.`
  - Inter Regular, `13` pt, `#F0EDE8`, Width: `5.0"`. X: **12.8"**, Y: **16.4"**.

### Step 18 — Key Potential Differences (Block E)

**18a — Container:**
- Rounded rectangle. X: **12.5"**, Y: **19.9"**. W: `11.0"`. H: `4.9"`. Fill: `#1E2435`. Radius: `8`.
- Left accent: `0.06"` x `4.9"`, `#E8A020`.

**18b — Title:**
- Text: `KEY POTENTIAL DIFFERENCES`
- Font: Barlow SemiBold, `20` pt, `#E8A020`. X: **12.8"**, Y: **20.1"**.

**18c — Sub-title:**
- Text: `Larger ΔV = more aggressive galvanic corrosion`
- Font: Inter Regular, `13` pt, `#F0EDE8` at 70%. X: **12.8"**, Y: **20.7"**.

**18d — Data table:**

Header row (Y: **21.2"**, H: `0.4"`, fill `#3A4055`):
- `COUPLE` (X: **12.9"**) | `ΔV` (X: **17.9"**) | `RISK` (X: **20.0"**) — Barlow SemiBold, `13` pt, `#F0EDE8`.

Row 1 (Y: **21.7"**):
- `Zn / Steel` — Inter Medium, `14` pt, `#F0EDE8`
- `0.31 V` — JetBrains Mono Regular, `14` pt, `#27AE60`
- `Mild — protective` — Inter Regular, `13` pt, `#27AE60`

Row 2 (Y: **22.5"**):
- `Cu / Steel` — `#F0EDE8`
- `0.48 V` — `#E8A020`
- `Moderate` — `#E8A020`

Row 3 (Y: **23.3"**):
- `Au / Ni (active)` — `#F0EDE8`
- `1.93 V` — `#E05C5C`
- `Severe — destructive` — `#E05C5C`

**18e — Footnote:**
- Text: `Potentials measured in flowing seawater vs. SCE. These are reference-grade comparison values, not lab-precision measurements — actual field corrosion rates depend on electrolyte chemistry, temperature, area ratio, oxygen, and surface condition.`
- Font: Inter Regular, `11` pt, `#F0EDE8` at 60%, italic.
- Position: X: **12.8"**, Y: **24.2"**. Width: `10.4"`.

### Step 19 — Group all of Zone 2

---

## Phase 4 — Zone 3: Design Guidance Strip

This zone occupies Y: 25.5" to 32.5" (~7.0" tall). Three practical callouts + key takeaway strip.

### Step 20 — Section label
- Text: `WHEN METALS MUST TOUCH`
- Font: Barlow Condensed ExtraBold, `28` pt, `#F0EDE8`, Center. Y: **25.7"**.

### Step 21 — Three practical callouts (Y: 26.4" to 30.4")

Three equal-width columns: Column 1 (X: **0.5"**), Column 2 (X: **8.3"**), Column 3 (X: **16.1"**). Each W: `7.5"`, H: `4.0"`.

**Callout 1 — Keep ΔV Small:**
- Container: Rounded rectangle, fill `#1E2435`, radius `6`. Left accent: `#27AE60`.
- Title: `KEEP ΔV SMALL` — Barlow SemiBold, `18` pt, `#27AE60`. X: **0.8"**, Y: **26.6"**.
- Body: `Choose metals within 0.15–0.25 V on the galvanic series. The smaller the potential gap, the slower the corrosion.`
  - Inter Regular, `15` pt, `#F0EDE8`, line height 145%. X: **0.8"**, Y: **27.2"**. Width: `7.0"`.

**Callout 2 — Isolate the Couple:**
- Container: fill `#1E2435`. Left accent: `#2EC4B6`.
- Title: `ISOLATE THE COUPLE` — `#2EC4B6`. X: **8.6"**, Y: **26.6"**.
- Body: `Use insulating gaskets, sleeves, washers, or coatings to break the electronic OR ionic path between dissimilar metals.`
  - X: **8.6"**, Y: **27.2"**. Width: `7.0"`.

**Callout 3 — Watch Area Ratio:**
- Container: fill `#1E2435`. Left accent: `#E8A020`.
- Title: `WATCH AREA RATIO` — `#E8A020`. X: **16.4"**, Y: **26.6"**.
- Body: `A small anode connected to a large cathode corrodes catastrophically. Never use anodic fasteners in cathodic structures.`
  - X: **16.4"**, Y: **27.2"**. Width: `7.0"`.

### Step 22 — Stop-Corrosion key takeaway strip

- Rounded rectangle. X: **0.5"**, Y: **30.7"**. W: `23.0"`. H: `1.6"`. Fill: `#1E2435`. Radius: `8`.
- Left accent: `0.06"` x `1.6"`, `#E05C5C`.
- Text: `CORROSION NEEDS ALL FOUR — REMOVE ANY ONE TO STOP IT.`
- Font: Barlow Condensed ExtraBold, `32` pt, `#F0EDE8`, Center.
- Position: X: **0.8"**, Y: **30.95"**. Width: `22.4"`.

### Step 23 — Group all of Zone 3

---

## Phase 5 — Zone 4: Footer Band

### Step 24 — Footer band background
- Rectangle. W: `24.0"`. H: `3.5"`. Fill: `#0D1020`. Position: X: **0"**, Y: **32.5"**.

### Step 25 — Disclaimer
- Text: `The galvanic series shown is for flowing seawater and is intended as a relative reference. Real-world corrosion rates depend on electrolyte chemistry, temperature, area ratio, oxygenation, and surface condition. Consult a corrosion engineer for service-critical assemblies.`
- Font: Inter Regular, `11` pt, `#F0EDE8` at 50%, Center. X: **0.5"**, Y: **32.8"**. Width: `23.0"`.

### Step 26 — Poster title
- Text: `The Galvanic Series — Why Metals Corrode in Contact`
- Font: Barlow SemiBold, `16` pt, `#F0EDE8`. X: **0.5"**, Y: **33.5"**.

### Step 27 — Series name
- Text: `Plating Posters Inc — Metal Finishing Reference Series`
- Font: Inter Regular, `14` pt, `#F0EDE8` at 70%, Center. Y: **34.2"**.

### Step 28 — Logo placeholder
- Rounded rectangle. W: `0.8"`. H: `0.4"`. Fill: `#3A4055`. X: **22.5"**, Y: **33.3"**.
- Text: `[LOGO]` — JetBrains Mono Regular, `12` pt, `#F0EDE8` at 50%.

### Step 29 — Version
- Text: `v1.0 — 2026` — JetBrains Mono Regular, `11` pt, `#F0EDE8` at 50%. X: **0.5"**, Y: **35.0"**.

### Step 30 — Group all of Zone 4

---

## Phase 6 — Final Review Checklist

### Text verification
- [ ] Headline: `THE GALVANIC SERIES` at 96 pt
- [ ] Subheading in Amber; tagline at 65% opacity
- [ ] Galvanic series chart: 16 bars from Magnesium (-1.60V) to Platinum/Gold (+0.20/+1.20V)
- [ ] Top axis: `ACTIVE / ANODIC` in Coral; bottom axis: `NOBLE / CATHODIC` in Emerald
- [ ] Cell illustration: anode (Coral), cathode (Emerald), wire (Amber), electrolyte (Teal)
- [ ] Key takeaway: `Eliminate any one component to stop corrosion.`
- [ ] Zinc-on-steel example (Emerald accent); Nickel-on-steel example (Coral accent)
- [ ] Potential differences table: 3 rows (Zn/Steel, Cu/Steel, Au/Ni)
- [ ] Three practical callouts: Keep ΔV Small, Isolate the Couple, Watch Area Ratio
- [ ] Strip: `CORROSION NEEDS ALL FOUR — REMOVE ANY ONE TO STOP IT.`
- [ ] Disclaimer, footer title, series name, LOGO, version present

### Color verification
- [ ] Chart bars gradient: Coral (top) → Coral Light → Amber → Amber Mid → Emerald (bottom)
- [ ] Anode block: Coral; Cathode block: Emerald
- [ ] Footer band: `#0D1020`

### Layout verification
- [ ] Left column (chart) X: 0.5"–11.5"; Right column X: 12.5"–23.5"
- [ ] 16 chart bars vertically stacked with consistent spacing
- [ ] Cross-section illustrations show pore/breach clearly
- [ ] All text within 0.5-inch safe zone

---

## Phase 7 — Light Edition: Remap Instructions

### Step 31 — Duplicate and remap

| Element Type | Change From | Change To |
|---|---|---|
| **Background** | `#1A1F2E` | `#F5F4F0` |
| **All body text** | `#F0EDE8` | `#1A1F2E` |
| **Callout fills / chart container** | `#1E2435` | `#ECEEF4` |
| **Alt backgrounds** | `#252B3D` | `#E8E8F0` |
| **Footer band** | `#0D1020` | `#1A1F2E` |
| **Amber elements** | `#E8A020` | `#C8860A` |
| **Teal elements** | `#2EC4B6` | `#1A8C82` |
| **Emerald elements** | `#27AE60` | `#1E7A47` |
| **Coral elements** | `#E05C5C` | `#B83E3E` |
| **Coral Light** | `#F08080` | `#D04646` |
| **Amber Mid** | `#D89020` | `#A06808` |
| **Mid Slate** | `#3A4055` | `#D0D4DE` |
| **Bright Silver** | `#C8D0D8` | `#C8D0D8` **(unchanged)** |

The galvanic series chart bars require per-bar recoloring. Plan extra time for this zone.

---

## Phase 8 — Export Instructions

### Export file checklist
- [ ] `Galvanic Series — Dark — 24x36 — Print.pdf`
- [ ] `Galvanic Series — Dark — 18x24 — Print.pdf`
- [ ] `Galvanic Series — Dark — Digital.pdf`
- [ ] `Galvanic Series — Light — 24x36 — Print.pdf`
- [ ] `Galvanic Series — Light — 18x24 — Print.pdf`
- [ ] `Galvanic Series — Light — Digital.pdf`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-20 | Initial build prompt (Claude Chat generation). Engineered by Elara from Alaina's Construction Workup v2.0. |
