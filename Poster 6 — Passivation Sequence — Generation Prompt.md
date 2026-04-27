---
Project: Plating Posters Inc
Poster Number: 6
Title: "The Passivation Sequence: From Plated Part to Protected Part"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-04T00:00:00
Source: Poster 6 — Passivation Sequence — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Passivation
  - ChromateConversion
  - v1
---

# Claude Chat Generation Prompt — Poster #6
## The Passivation Sequence: From Plated Part to Protected Part
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

Top 2.9 inches. Headline + subheading + tagline (left ~55%), "Why Passivate?" callout (right ~45%).

### Step 6 — Headline
1. Add heading: `THE PASSIVATION SEQUENCE`
2. Font: Barlow Condensed ExtraBold, Size: `88`, Color: `F0EDE8`, Letter spacing: `-4`, Alignment: Left
3. Position: X: **0.5"**. Y: **0.5"**. Width: **12.5"**.

### Step 7 — Subheading
`From Plated Part to Protected Part`
Font: Barlow SemiBold, 36 pt, `E8A020`. X: **0.5"**. Y: **1.5"**.

### Step 8 — Tagline
`The step that determines whether your parts pass salt spray.`
Font: Barlow SemiBold, 22 pt, `F0EDE8`, Transparency: **65%**. X: **0.5"**. Y: **2.1"**.

### Step 9 — "Why Passivate?" callout

**9a — Container:**
Rounded Rectangle. Width: `10.25"`. Height: `2.2"`. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6`. Corner radius: `8`.
Position: X: **13.25"**. Y: **0.5"**.

**9b — Title:**
`WHY PASSIVATE?` — Barlow SemiBold, 18 pt, `2EC4B6`. X: **13.55"**. Y: **0.7"**.

**9c — Body:**
`Bare zinc corrodes to white rust within hours. The passivation step forms a chromium-zinc barrier film that extends corrosion life by 10x to 100x — turning hours of protection into hundreds.`
Font: Inter Regular, 16 pt, `F0EDE8`. Line height: `1.4`. Width: **9.65"**. X: **13.55"**. Y: **1.05"**.

**9d — Key fact:**
`This is a chemical conversion — not plating. No current required.`
Font: Inter Medium, 16 pt, `2EC4B6`. X: **13.55"**. Y: **2.0"**.

**9e — Group callout.** Press **Ctrl+G**.

### Step 10 — Group all of Zone 1. Press **Ctrl+G**. **Lock**.

---

## Phase 3 — Zone 2: Post-Plating Process Flow

This zone occupies Y: 2.9" to 6.5" (3.6 inches tall). A horizontal strip with 7 process boxes connected by arrows.

### Step 11 — Background band
Rectangle. Width: `24"`. Height: `3.6"`. Fill: `1E2435`. No border.
Position: X: **0"**. Y: **2.9"**.

### Step 12 — Build 7 process boxes + 6 connecting arrows

Each box: Rounded Rectangle, Width: `2.6"`, Height: `1.3"`. Corner radius: `4`.
Default fill: `252B3D`. Default border: 1 pt, `3A4055`.
All boxes at Y: **4.0"** (centered vertically in the strip).

Arrows between boxes: line elements, 2 pt, `3A4055`, with arrowheads, spanning the 0.3" gaps.

**Box positions and labels:**

| Box | X | Label | Border Override | Sub-label |
|-----|---|-------|-----------------|-----------|
| 1 | 0.6" | `ZINC PLATE` | — | — |
| 2 | 3.5" | `RINSE` | — | — |
| 3 | 6.4" | `BRIGHT DIP` | — | `(optional)` in `E8A020` |
| 4 | 9.3" | `RINSE` | — | — |
| 5 | 12.2" | `PASSIVATE` | **2 pt, `E8A020` (Amber)** | — |
| 6 | 15.1" | `RINSE` | — | `(gentle)` in `2EC4B6` |
| 7 | 18.0" | `DRY` | — | — |

Box labels: Barlow SemiBold, 14 pt, `F0EDE8`, centered in each box.
Sub-labels: Inter Regular, 11 pt, positioned below the box name inside the same box.

**Build Box 1 completely, group it. Build the arrow to the right. Then build Box 2, etc.** Or build all 7 boxes first, then add 6 arrows between them.

### Step 13 — Strip footnote
`Optional sealant/topcoat step omitted for clarity — see operating parameters.`
Font: Inter Regular, 13 pt, `F0EDE8`, Transparency: **60%**. X: **0.5"**. Y: **5.6"**.

### Step 14 — Group all of Zone 2
Select background band, all 7 boxes, all 6 arrows, and footnote. Press **Ctrl+G**. **Lock**.

---

## Phase 4 — Zone 3: Color Spectrum (HERO)

This zone occupies Y: 6.5" to 18.0" (11.5 inches tall). Two rows of 4 color panels each — Trivalent (top) and Hexavalent (bottom). This is the poster's visual centerpiece.

### Step 15 — Section label
`THE COLOR SPECTRUM — PROTECTION BY PASSIVATION TYPE`
Font: Barlow Condensed ExtraBold, 28 pt, `F0EDE8`, Center. Y: **6.7"**. Width: **23.0"**.

---

### ROW 1 — TRIVALENT (Y: 7.3" to 12.3")

### Step 16 — Row label
Copy-paste: `TRIVALENT (Cr³⁺) — RoHS COMPLIANT`
Font: Barlow SemiBold, 20 pt, `27AE60` (Emerald). X: **0.5"**. Y: **7.3"**.

### Step 17 — Build Panel 1 (Template): Clear/Blue Trivalent

Panel dimensions: 5.5" wide x 4.2" tall. Panels separated by 0.2" gutters.
Panel 1 position: X: **0.5"**. Y: **7.8"**.

**17a — Panel body:**
Rounded Rectangle. Width: `5.5"`. Height: `4.2"`. Fill: `1E2435`. Corner radius: `6`.

**17b — Top color bar:**
Rectangle. Width: `5.5"`. Height: `0.6"`. Fill: `B0D0E8` (Tri Clear/Blue appearance color).
Position: flush with top of panel. If possible, match top corner radius to panel (6 pt top corners, 0 bottom).

**17c — Title:**
`CLEAR / BLUE` — Barlow Condensed ExtraBold, 18 pt, `F0EDE8`, Center.
Position: centered in panel. Y: panel top + 0.8".

**17d — Film label:**
`Thinnest` — Inter Regular, 14 pt, `F0EDE8`, Transparency: **70%**, Center.
Y: panel top + 1.2".

**17e — White rust hours:**
`White rust: 24-72 hrs` — JetBrains Mono, 16 pt, `E8A020` (Amber), Center.
Y: panel top + 1.7".

**17f — Red rust hours:**
`Red rust: 72-200 hrs` — JetBrains Mono, 16 pt, `E05C5C` (Coral), Center.
Y: panel top + 2.1".

**17g — Note:**
`Most common; cosmetically bright` — Inter Regular, 12 pt, `F0EDE8`, Transparency: **70%**, Center. Width: **5.0"**.
Y: panel top + 2.7".

**17h — Group Panel 1.** Press **Ctrl+G**.

### Step 18 — Build Panels 2–4 (Duplicate and Modify)

Duplicate Panel 1 for each. Reposition at the correct X position. Ungroup, change the data, re-group.

**Panel 2** (X: **6.2"**, Y: **7.8"**):
- Color bar fill: `D4A830` (Tri Yellow)
- Title: `YELLOW (IRIDESCENT)`
- Film: `Medium`
- White rust: `White rust: 72-120 hrs`
- Red rust: `Red rust: 200-400 hrs`
- Note: `Proprietary formulations; mimics hex yellow`

**Panel 3** (X: **11.9"**, Y: **7.8"**):
- Color bar fill: `1A1A1A` (Black)
- Title: `BLACK`
- Film: `Medium-heavy`
- White rust: `White rust: 72-120 hrs`
- Red rust: `Red rust: 200-400 hrs`
- Note: `A Brite: BriteGuard NZP P1 / NZP P2`

**Panel 4** (X: **17.6"**, Y: **7.8"**):
- Color bar fill: `4A5568` (Tri Thick Film)
- Title: `THICK FILM / HIGH-PERF`
- Film: `Heaviest`
- White rust: `White rust: 120-200 hrs`
- Red rust: `Red rust: 400-720+ hrs`
- Note: `Latest generation — approaching hex yellow`

---

### ROW 2 — HEXAVALENT (Y: 12.6" to 17.6")

### Step 19 — Row label
Copy-paste: `HEXAVALENT (Cr⁶⁺) — RESTRICTED (RoHS/REACH/ELV)`
Font: Barlow SemiBold, 20 pt, `E05C5C` (Coral). X: **0.5"**. Y: **12.6"**.

### Step 20 — Build Hex Panels 1–4

Same panel dimensions and template as trivalent. Y position for all hex panels: **13.1"**.

**Hex Panel 1** (X: **0.5"**):
- Color bar fill: `A8C8E0` (Hex Clear/Blue)
- Title: `CLEAR / BLUE`
- White rust: `White rust: 12-24 hrs`
- Red rust: `Red rust: 72-150 hrs`
- Note: (leave blank or omit note text box)

**Hex Panel 2** (X: **6.2"**):
- Color bar fill: `C89820` (Hex Yellow)
- Title: `YELLOW / IRIDESCENT`
- White rust: `White rust: 96-200 hrs`
- Red rust: `Red rust: 200-500 hrs`
- Note: `The industry workhorse for decades`

**Hex Panel 3** (X: **11.9"**):
- Color bar fill: `1A1A1A` (Black)
- Title: `BLACK`
- White rust: `White rust: 72-120 hrs`
- Red rust: `Red rust: 200-400 hrs`
- Note: (leave blank or omit)

**Hex Panel 4** (X: **17.6"**):
- Color bar fill: `5A6644` (Olive Drab)
- Title: `OLIVE DRAB (OD)`
- White rust: `White rust: 200-500 hrs`
- Red rust: `Red rust: 500-1000+ hrs`
- Note: `Military/defense; MIL-DTL-5541; heaviest hex film`

### Step 21 — Group all of Zone 3
Group each row (4 panels + row label) as sub-groups first. Then group both rows + section label. Press **Ctrl+G**. **Lock**.

---

## Phase 5 — Zone 4: Operating Parameters

This zone occupies Y: 18.0" to 23.8" (5.8 inches tall). Two side-by-side parameter tables — Trivalent (left) and Hexavalent (right).

### Step 22 — Trivalent parameters (left)

**22a — Title:**
`TRIVALENT OPERATING PARAMETERS` — Barlow SemiBold, 20 pt, `27AE60`. X: **0.5"**. Y: **18.2"**.

**22b — Table header:**
Rectangle. Width: `11.2"`. Height: `0.45"`. Fill: `3A4055`. X: **0.5"**. Y: **18.7"**.
Headers: `Parameter` (X: 0.7") and `Range` (X: 4.5") — Barlow SemiBold, 16 pt, `F0EDE8`.

**22c — Data rows** (6 rows, 0.55" each, alternating fills):

| Row | Y | Fill | Parameter | Range |
|-----|---|------|-----------|-------|
| 1 | 19.15" | base | Chemistry | Copy-paste: Cr³⁺ sulfate or chloride based |
| 2 | 19.70" | alt | pH | 1.5-2.5 (up to 3.0 for thicker films) |
| 3 | 20.25" | base | Temperature | 70-140 deg F (21-60 deg C) |
| 4 | 20.80" | alt | Immersion | 30-90 sec (clear); 60-180 sec (thick) |
| 5 | 21.35" | base | Agitation | Gentle — avoid turbulence |
| 6 | 21.90" | alt | Max dry temp | < 150 deg F (65 deg C) |

Parameter: Inter Medium, 16 pt, `F0EDE8`. Range: Inter Regular, 15 pt, `F0EDE8`.

**22d — Drew's note:**
`Raising pH to 2.5 allows thicker film build — part stays longer without zinc degradation.`
Font: Inter Regular, 13 pt, `E8A020`. X: **0.5"**. Y: **22.6"**.

### Step 23 — Hexavalent parameters (right)

**23a — Title:**
`HEXAVALENT OPERATING PARAMETERS` — Barlow SemiBold, 20 pt, `E05C5C`. X: **12.3"**. Y: **18.2"**.

**23b — Table header:**
Rectangle. Width: `11.2"`. Height: `0.45"`. Fill: `3A4055`. X: **12.3"**. Y: **18.7"**.
Same header text positions relative to the right column.

**23c — Data rows:**

| Row | Y | Fill | Parameter | Range |
|-----|---|------|-----------|-------|
| 1 | 19.15" | base | Chemistry | Copy-paste: CrO₃-based (dichromate, chromic acid) |
| 2 | 19.70" | alt | pH | 1.0-2.0 (clear); 0.5-1.5 (yellow) |
| 3 | 20.25" | base | Temperature | 70-100 deg F (21-38 deg C) |
| 4 | 20.80" | alt | Immersion | 5-30 sec (clear); 15-60 sec (yellow); 30-120 sec (OD) |
| 5 | 21.35" | base | Agitation | Gentle rack movement |
| 6 | 21.90" | alt | Max dry temp | < 300 deg F (150 deg C) |

### Step 24 — Group all of Zone 4
Select both titles, both tables, and Drew's note. Press **Ctrl+G**. **Lock**.

---

## Phase 6 — Zone 5: Contamination + Post-Passivation Care

This zone occupies Y: 23.8" to 30.6" (6.8 inches tall). Left 55% is a contamination table. Right 45% has rinse and drying callouts.

### Step 25 — Contamination section label
`WHAT KILLS THE PASSIVATION BATH` — Barlow Condensed ExtraBold, 22 pt, `F0EDE8`.
X: **0.5"**. Y: **24.0"**.

### Step 26 — Contamination table header
Rectangle. Width: `12.5"`. Height: `0.45"`. Fill: `3A4055`. X: **0.5"**. Y: **24.5"**.
Headers: `Contaminant` (X: 0.7"), `Source` (X: 3.0"), `Threshold` (X: 6.2"), `Effect` (X: 8.5") — Barlow SemiBold, 16 pt, `F0EDE8`.

### Step 27 — Contamination data rows

5 rows, 0.6" each, alternating fills:

| Row | Y | Fill | Contaminant | Source | Threshold | Effect |
|-----|---|------|-------------|--------|-----------|--------|
| 1 | 24.95" | base | Copy-paste: Iron (Fe³⁺) | Steel racks, parts | >100-150 ppm | Yellow/brown discoloration |
| 2 | 25.55" | alt | Copy-paste: Zinc (Zn²⁺) | Drag-in from plating | High levels | Film discoloration |
| 3 | 26.15" | base | Copy-paste: Copper (Cu²⁺) | Drag-in, rack corrosion | >30 ppm | Darkens film |
| 4 | 26.75" | alt | Organics | Brightener drag-in | Variable | Spotty passivation |
| 5 | 27.35" | base | Chloride | Acid zinc KCl drag-in | Variable | Accelerates zinc attack |

Contaminant: Inter Medium, 16 pt, `F0EDE8`. Other columns: Inter Regular, 15 pt, `F0EDE8`.

### Step 28 — Prevention callout
`Drag-in is the #1 source of passivation bath contamination. Rinse thoroughly between plating and passivation.`
Font: Inter Medium, 15 pt, `E8A020`. X: **0.5"**. Y: **28.1"**. Width: **12.5"**.

### Step 29 — Rinse Warning callout (right)

**29a — Container:**
Rounded Rectangle. Width: `10.0"`. Height: `2.4"`. Fill: `1E2435`. Border: 1.5 pt, `2EC4B6`. Corner radius: `6`.
Position: X: **13.5"**. Y: **24.2"**.

**29b — Title:**
`RINSE AFTER PASSIVATION` — Barlow SemiBold, 16 pt, `2EC4B6`. X: **13.8"**. Y: **24.4"**.

**29c — Body:**
`Use cold to warm water — NOT hot. Minimal agitation. Brief immersion. Aggressive rinsing or hot water damages the freshly formed film.`
Font: Inter Regular, 14 pt, `F0EDE8`. Line height: `1.4`. Width: **9.4"**. X: **13.8"**. Y: **24.8"**.

**29d — Group.** Press **Ctrl+G**.

### Step 30 — Drying Warning callout (right, below rinse)

**30a — Container:**
Rounded Rectangle. Width: `10.0"`. Height: `2.6"`. Fill: `1E2435`. Border: 1.5 pt, `E8A020` (Amber). Corner radius: `6`.
Position: X: **13.5"**. Y: **26.9"**.

**30b — Title:**
`DRYING TEMPERATURE` — Barlow SemiBold, 16 pt, `E8A020`. X: **13.8"**. Y: **27.1"**.

**30c — Body:**
`Trivalent: below 150 deg F (65 deg C). Hexavalent: below 300 deg F (150 deg C). Excessive heat destroys corrosion resistance.`
Font: Inter Regular, 14 pt, `F0EDE8`. Line height: `1.4`. Width: **9.4"**. X: **13.8"**. Y: **27.5"**.

**30d — Group.** Press **Ctrl+G**.

### Step 31 — Group all of Zone 5
Select contamination label, table, prevention note, rinse callout, and drying callout. Press **Ctrl+G**. **Lock**.

---

## Phase 7 — Zone 6: Self-Healing + Compliance Badges

This zone occupies Y: 30.6" to 32.4" (1.8 inches tall). Left ~60% is a self-healing note. Right ~40% has two compliance badges.

### Step 32 — Self-healing note
Copy-paste this text:
`Self-healing (hexavalent only): Hex passivation films contain soluble Cr⁶⁺ that migrates to scratches and re-passivates exposed zinc. Trivalent films do not self-heal — once damaged, the barrier is compromised.`

For the opening phrase "Self-healing (hexavalent only):" — use **Inter Medium**. For the rest, use **Inter Regular**. Both at 14 pt, `F0EDE8`. Line height: `1.4`.

**Simplified approach:** Type it all in one text box as Inter Regular, 14 pt, `F0EDE8`. If you can bold the opening phrase in the design (select it, press Ctrl+B), do so. If not, the full sentence in regular weight is fine.

Position: X: **0.5"**. Y: **30.8"**. Width: **13.5"**.

### Step 33 — Compliance badges

**Badge 1 — Trivalent (Emerald):**
1. Add Rounded Rectangle. Width: `4.2"`. Height: `0.65"`. Fill: `1E2435`. Border: 2 pt, `27AE60`. Corner radius: `4`.
2. Position: X: **14.5"**. Y: **30.7"**.
3. Add text (centered): `TRIVALENT — RoHS/REACH COMPLIANT`
4. Font: Inter Medium, 12 pt, `27AE60`.

**Badge 2 — Hexavalent (Coral):**
1. Add Rounded Rectangle. Width: `4.5"`. Height: `0.65"`. Fill: `1E2435`. Border: 2 pt, `E05C5C`. Corner radius: `4`.
2. Position: X: **19.0"**. Y: **30.7"**.
3. Add text (centered): `HEXAVALENT — RESTRICTED SUBSTANCE`
4. Font: Inter Medium, 12 pt, `E05C5C`.

### Step 34 — Group all of Zone 6
Select self-healing note and both badges. Press **Ctrl+G**. **Lock**.

---

## Phase 8 — Zone 7: Footer Band

This zone occupies Y: 32.4" to 36.0" (3.6 inches tall).

### Step 35 — Footer band background
Rectangle. Width: `24"`. Height: `3.6"`. Fill: `0D1020`. No border.
Position: X: **0"**. Y: **32.4"**.

### Step 36 — Disclaimer
`This poster presents general passivation guidelines. Salt spray performance varies by vendor formulation, zinc thickness, and sealant use. Consult your process supplier for product-specific data. This poster does not replace your SDS.`
Font: Inter Regular, 11 pt, `F0EDE8`, Transparency: **50%**, Center. Width: **23.0"**. Y: **32.8"**.

### Step 37 — Poster title
`The Passivation Sequence: From Plated Part to Protected Part`
Font: Barlow SemiBold, 16 pt, `F0EDE8`. X: **0.5"**. Y: **33.5"**.

### Step 38 — Series name
`Plating Posters Inc — Metal Finishing Reference Series`
Font: Inter Regular, 13 pt, `F0EDE8`, Transparency: **60%**. X: **0.5"**. Y: **34.0"**.

### Step 39 — Version
`v1.0 — 2026` — Inter Regular, 11 pt, `F0EDE8`, Transparency: **40%**. X: **0.5"**. Y: **34.4"**.

### Step 40 — Logo placeholder
`[LOGO]` — Barlow SemiBold, 14 pt, `F0EDE8`, Transparency: **30%**, Center. X: **21.0"**. Y: **33.5"**. Width: **2.5"**.

### Step 41 — Group all of Zone 7. Press **Ctrl+G**.

---

## Phase 9 — Final Review Checklist

### Text verification
- [ ] Headline: `THE PASSIVATION SEQUENCE`
- [ ] Subheading: `From Plated Part to Protected Part` in Amber
- [ ] Callout: `WHY PASSIVATE?` with key fact about chemical conversion
- [ ] Flow strip has 7 boxes in order: ZINC PLATE, RINSE, BRIGHT DIP, RINSE, PASSIVATE, RINSE, DRY
- [ ] PASSIVATE box has Amber border (distinct from others)
- [ ] BRIGHT DIP has `(optional)` sub-label
- [ ] RINSE box 6 has `(gentle)` sub-label
- [ ] 4 trivalent panels: Clear/Blue, Yellow, Black, Thick Film
- [ ] 4 hexavalent panels: Clear/Blue, Yellow, Black, Olive Drab
- [ ] Panel 3 (trivalent black) mentions `BriteGuard NZP P1 / NZP P2`
- [ ] Both parameter tables have 6 rows each
- [ ] Drew's note about pH 2.5 is present
- [ ] Contamination table has 5 rows (Iron through Chloride)
- [ ] Self-healing note mentions hex only
- [ ] Two compliance badges present

### Color verification
- [ ] Trivalent row label and accents: Emerald `#27AE60`
- [ ] Hexavalent row label and accents: Coral `#E05C5C`
- [ ] Top color bars use APPEARANCE colors (not palette): `#B0D0E8`, `#D4A830`, `#1A1A1A`, `#4A5568`, `#A8C8E0`, `#C89820`, `#5A6644`
- [ ] White rust values in Amber, red rust values in Coral
- [ ] PASSIVATE flow box has Amber border

### Readability check
- [ ] 25% zoom — headline, section labels, row labels readable
- [ ] 50% zoom — panel titles and flow box labels readable
- [ ] 75% zoom — salt spray values, parameter data readable
- [ ] 100% — footnotes, disclaimer, badge text readable

---

## Phase 10 — Light Edition: Remap Instructions

### Step 42 — Duplicate the page. Switch to Page 2.

### Step 43 — Change background from `1A1F2E` to `F5F4F0`.

### Step 44 — Remap all elements

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

**CRITICAL OVERRIDE — Passivation color bars:**
The top color bars on ALL 8 spectrum panels are **NOT remapped**. These represent actual passivation appearance colors and must remain unchanged:
`#B0D0E8`, `#D4A830`, `#1A1A1A`, `#4A5568`, `#A8C8E0`, `#C89820`, `#5A6644`

Only the panel bodies, text, borders, and structural elements remap.

**Note on black panel bars:** The `#1A1A1A` bars will appear very dark on the light background — this is intentional and correct (black passivation IS black).

### Step 45 — Post-remap adjustments
1. Verify the color bars are still clearly visible against the remapped panel fills.
2. Verify footnotes and disclaimer are readable at reduced opacity.
3. Verify badge text is legible with the darkened accent colors.

---

## Phase 11 — Export Instructions

### Step 46 — Export Dark edition
- PDF Print 24x36" → `Passivation-Sequence-Dark-24x36-Print.pdf`
- PDF Standard → `Passivation-Sequence-Dark-Digital.pdf`
- Resize 18x24" → `Passivation-Sequence-Dark-18x24-Print.pdf`

### Step 47 — Export Light edition
- `Passivation-Sequence-Light-24x36-Print.pdf`
- `Passivation-Sequence-Light-Digital.pdf`
- `Passivation-Sequence-Light-18x24-Print.pdf`

### Export file checklist
- [ ] 6 files total (Dark + Light, each in 24x36 Print, 18x24 Print, Digital)

---

## Quick Reference — All Hex Codes Used

**Series palette:**

| Code | Name | Used For |
|---|---|---|
| `#1A1F2E` | Gunmetal Dark | Background, base rows |
| `#F0EDE8` | Warm White | Body text |
| `#F5F4F0` | Off-White | Light edition background |
| `#E8A020` | Amber | Subheading, PASSIVATE box, Drew's notes |
| `#2EC4B6` | Teal | Callout borders, rinse labels |
| `#27AE60` | Emerald | Trivalent labels, RoHS badge |
| `#E05C5C` | Coral | Hexavalent labels, restricted badge |
| `#3A4055` | Mid Slate | Table headers, flow arrows |
| `#0D1020` | Deep Navy | Footer band |
| `#1E2435` | Dark Callout | Callout/panel fills |
| `#252B3D` | Alt Row | Flow boxes, alternating rows |

**Passivation appearance colors (exempt from Light edition remap):**

| Code | Panel |
|---|---|
| `#B0D0E8` | Trivalent clear/blue |
| `#D4A830` | Trivalent yellow |
| `#1A1A1A` | Black (both rows) |
| `#4A5568` | Trivalent thick film |
| `#A8C8E0` | Hexavalent clear/blue |
| `#C89820` | Hexavalent yellow |
| `#5A6644` | Hexavalent olive drab |

---

*Originally engineered by Elara — Plating Posters Inc Prompt Architect*
*Poster #6 — The Passivation Sequence — Claude Chat Generation Prompt v2.0*
*2026-04-04*
