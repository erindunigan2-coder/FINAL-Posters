---
Project: Plating Posters Inc
Poster Number: 20
Title: "Precious Metals Plating — Gold and Silver Quick Reference"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-20T00:00:00
Source: Poster 20 — Precious Metals Quick Reference — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PreciousMetals
  - GoldPlating
  - SilverPlating
  - v1
---

# Claude Chat Generation Prompt — Poster #20
## Precious Metals Plating — Gold and Silver Quick Reference
### Version 1.0 | Dark Edition (Primary) + Light Edition (Remap)

*Originally engineered by Elara from Alaina's Construction Workup v1.0. Adapted for Claude chat visual generation (2026-04-20). All technical content production-ready.*

---

**Workflow: Claude Chat Visual Generation**

> **IMPORTANT:** This poster is to be generated as a visual artifact in claude.ai chat (SVG or HTML recommended). Do NOT use any external design tools. Generate the poster visually in the chat as a complete SVG or HTML artifact.

**Instructions for Claude:**

- Generate this poster as a **complete visual artifact** — either SVG or HTML with inline CSS.
- The poster is **24 x 36 inches** (portrait orientation). Design at this aspect ratio.
- Produce the **Dark edition first**. Light edition remap table provided at the end.
- Follow all specifications exactly. Every hex code, font, and size is intentional.
- Prioritize **readability at distance** — 3-8 feet on a shop wall.

---

## Phase 1 — Design Foundation

### Artboard
- **Size:** 24 x 36 inches (portrait)
- **Background color (Dark edition):** `#1A1F2E` (Gunmetal Dark)

### Typography
| Role | Font | Weight | Notes |
|------|------|--------|-------|
| Headlines | Barlow Condensed | ExtraBold (800) | All caps, letter-spacing -4 |
| Subheadings | Barlow | SemiBold (600) | Title case |
| Body text | Inter | Regular (400) / Medium (500) | Sentence case |
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for pH, CD, efficiency values |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Gold column accents, gold-bath rows |
| Teal | `#2EC4B6` | Strike-rule callout, neutral data accents |
| Emerald | `#27AE60` | Soft gold efficiency highlights |
| Coral | `#E05C5C` | Hard gold low-efficiency warnings, troy/avdp warning |
| Mid Slate | `#3A4055` | Table headers, dividers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card fills |
| Alt Row | `#252B3D` | Alternate table rows |
| Bright Silver | `#C8D0D8` | Silver column accents, silver-bath rows |
| Pale Amber | `#F5C870` | Soft accent for gold sub-rows |

### Layout Safe Zones
- **0.5" margin** on all sides

---

## Phase 2 — Zone 1: Header Band

### Step 6 — Headline
- Text: `PRECIOUS METALS`
- Font: Barlow Condensed ExtraBold, `96` pt, `#F0EDE8`, letter spacing `-4`. X: **0.5"**, Y: **0.5"**.

### Step 7 — Subheading
- Text: `Gold and Silver — Quick Reference`
- Font: Barlow SemiBold, `40` pt, `#E8A020` (Amber). X: **0.5"**, Y: **1.6"**.

### Step 8 — Tagline
- Text: `A wrong assay can cost more than a wrong recipe.`
- Font: Barlow SemiBold, `22` pt, `#F0EDE8` at 65%. X: **0.5"**, Y: **2.3"**.

---

## Phase 3 — Zone 2: Two-Column Comparison

Y: 2.9" to 22.5" (~19.6" tall). Two columns with 0.5" gutter.

### Step 9 — Gold column header bar (left)
- Rectangle, X: **0.5"**, Y: **3.1"**, W: `11.25"`, H: `0.8"`, fill `#E8A020`.
- Header text: `GOLD (Au)` — Barlow Condensed ExtraBold, `40` pt, `#1A1F2E`. X: **0.7"**, Y: **3.25"**.
- Atomic data (right side): `Z=79  |  ρ=19.3 g/cm³` — JetBrains Mono Regular, `14` pt, `#1A1F2E`. X: **8.0"**, Y: **3.4"**, right-aligned.

### Step 10 — Gold bath comparison table

Y: 4.1" to 13.5". Table header row + 5 bath rows.

**10a — Table header row:**
- Rectangle, X: **0.5"**, Y: **4.1"**, W: `11.25"`, H: `0.6"`, fill `#3A4055`.
- Headers (Barlow SemiBold, `13` pt, `#F0EDE8`):
  - `BATH TYPE` — X: **0.7"**
  - `pH` — X: **4.5"**
  - `CD (A/ft²)` — X: **5.8"**
  - `EFF.` — X: **8.2"**
  - `USE` — X: **9.4"**

**10b — Five bath rows** (each 1.4" tall, alternating `#1E2435` / `#252B3D`):

| Row | Y | Bath | pH | CD | Eff. | Use |
|-----|---|------|----|----|------|-----|
| 1 | 4.7" | Alkaline cyanide | 9.0–13 | 1–10 | 95–100% | Decorative, color match |
| 2 | 6.1" | Neutral cyanide | 6.0–8.0 | 1–5 | 95–100% | Electronic, soft gold |
| 3 | 7.5" | Acid cyanide | 3.5–5.0 | 1–10 | 25–35% | Hard gold, contacts |
| 4 | 8.9" | Sulfite (non-CN) | 8.0–10 | 1–5 | 90–95% | Photoresist-compatible |
| 5 | 10.3" | Pure-gold strike | 8.0–10 | 5–20 | 30–60% | Adhesion strike |

- Bath name: Inter Medium, `15` pt, `#E8A020`. X: **0.7"**.
- pH: JetBrains Mono Regular, `14` pt, `#F0EDE8`. X: **4.5"**.
- CD: JetBrains Mono Regular, `14` pt, `#F0EDE8`. X: **5.8"**.
- Efficiency: JetBrains Mono Regular, `14` pt — color-coded: `#27AE60` if >=90%, `#E8A020` if 60-89%, `#E05C5C` if <60%. X: **8.2"**.
- Use: Inter Regular, `13` pt, `#F0EDE8`. X: **9.4"**.

### Step 11 — Gold key-data callout

**11a — Container:**
- Rounded rectangle, X: **0.5"**, Y: **13.7"**, W: `11.25"`, H: `8.5"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `8.5"`, fill `#E8A020`.

**11b — Title:** `GOLD — KEY OPERATING DATA` — Barlow SemiBold, `20` pt, `#E8A020`. X: **0.8"**, Y: **13.9"**.

**11c — Body:**
- Font: Inter Regular, `15` pt, `#F0EDE8`, line height 150%. X: **0.8"**, Y: **14.5"**, Width: `10.7"`.
- Text:

> **Soft gold (cyanide):** 99.9%+ purity, Knoop 60–90, ductile. Used for wire bonding and decorative work. Cathode efficiency 95–100%.
>
> **Hard gold (Co/Ni-alloyed acid cyanide):** 99.5–99.7% purity, Knoop 130–200, wear-resistant. Used for electrical contacts. Cathode efficiency drops to 25–35% — plan tank ampere-hours accordingly.
>
> **Sulfite gold:** Cyanide-free, photoresist-compatible. **pH must not drop below 8.0** — the sulfite complex decomposes and the bath crashes. Monitor pH daily.
>
> **Always strike** over copper, brass, or nickel before plating gold — pure-gold strike at high CD for 10–30 seconds.

### Step 12 — Silver column header bar (right)
- Rectangle, X: **12.25"**, Y: **3.1"**, W: `11.25"`, H: `0.8"`, fill `#C8D0D8` (Bright Silver).
- Header text: `SILVER (Ag)` — Barlow Condensed ExtraBold, `40` pt, `#1A1F2E`. X: **12.45"**, Y: **3.25"**.
- Atomic data (right side): `Z=47  |  ρ=10.5 g/cm³` — JetBrains Mono Regular, `14` pt, `#1A1F2E`. X: **19.75"**, Y: **3.4"**, right-aligned.

### Step 13 — Silver bath comparison table

Y: 4.1" to 13.5". Table header row + 3 bath rows (rows are 2.0" tall to balance visually against the gold column).

**13a — Table header row:**
- Rectangle, X: **12.25"**, Y: **4.1"**, W: `11.25"`, H: `0.6"`, fill `#3A4055`.
- Headers: same labels as gold table, positioned at X: **12.45"**, **16.25"**, **17.55"**, **19.95"**, **21.15"**.

**13b — Three bath rows** (each 2.0" tall, alternating `#1E2435` / `#252B3D`):

| Row | Y | Bath | pH | CD | Eff. | Use |
|-----|---|------|----|----|------|-----|
| 1 | 4.7" | Cyanide strike | 11.5–12.5 | 15–30 | 75–90% | Mandatory pre-plate |
| 2 | 6.7" | Normal Rochelle | 11.5–12.5 | 5–15 | 95–100% | General decorative |
| 3 | 8.7" | High-speed bright | 11.0–12.0 | 20–60 | 95–100% | Tableware, jewelry |

- Bath name: Inter Medium, `15` pt, `#C8D0D8`. X: **12.45"**.
- Numeric columns: JetBrains Mono Regular, `14` pt, `#F0EDE8`.
- Efficiency color-coded same as gold table.

### Step 14 — Silver key-data callout

**14a — Container:**
- Rounded rectangle, X: **12.25"**, Y: **13.7"**, W: `11.25"`, H: `8.5"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `8.5"`, fill `#C8D0D8`.

**14b — Title:** `SILVER — KEY OPERATING DATA` — Barlow SemiBold, `20` pt, `#C8D0D8`. X: **12.55"**, Y: **13.9"**.

**14c — Body:**
- Font: Inter Regular, `15` pt, `#F0EDE8`, line height 150%. X: **12.55"**, Y: **14.5"**, Width: `10.7"`.
- Text:

> **Mandatory cyanide strike** before plating silver over copper or nickel. Without the strike, copper undergoes immersion deposition into the silver bath surface — a loose, non-adherent layer that destroys adhesion.
>
> **Antimony brighteners** (used in bright silver baths) reduce the conductivity of the deposit to 10–25% of pure silver. For electrical applications, specify a non-brightened bath.
>
> **Normal Rochelle** is the workhorse decorative bath. Free cyanide 4–8 oz/gal; carbonate buildup is the most common control issue.
>
> Silver tarnishes rapidly in sulfur-containing atmospheres — specify a chromate or organic post-treat for shelf life.

### Step 15 — Group all of Zone 2

---

## Phase 4 — Zone 3: Rules of the Trade

Y: 22.5" to 32.5" (~10.0" tall).

### Step 16 — Section label
- Text: `RULES OF THE TRADE`
- Font: Barlow Condensed ExtraBold, `28` pt, `#F0EDE8`, Center. Y: **22.7"**.

### Step 17 — Silver Strike Rule callout (Block D)

**17a — Container:**
- Rounded rectangle, X: **0.5"**, Y: **23.4"**, W: `23.0"`, H: `2.4"`, fill `#1E2435`, radius `8`.
- Left accent: `0.06"` x `2.4"`, fill `#2EC4B6` (Teal).

**17b — Title:** `THE SILVER STRIKE RULE` — Barlow SemiBold, `22` pt, `#2EC4B6`. X: **0.8"**, Y: **23.6"**.

**17c — Body:**
- Font: Inter Regular, `17` pt, `#F0EDE8`, line height 145%. X: **0.8"**, Y: **24.2"**, Width: `22.4"`.
- Text: `Always run a cyanide silver strike before plating silver over copper or nickel. The instant a copper part contacts a silver cyanide bath, copper begins immersion-displacing onto the surface — producing a non-adherent layer that no amount of plating time will fix. The strike's high CD and short time deposit a thin adherent film that breaks the immersion path before the main bath is reached.`

### Step 18 — Troy vs. Avoirdupois callout (Block E)

**18a — Container:**
- Rounded rectangle, X: **0.5"**, Y: **26.2"**, W: `23.0"`, H: `2.6"`, fill `#1E2435`, radius `8`.
- Left accent: `0.06"` x `2.6"`, fill `#E05C5C` (Coral).

**18b — Title:** `TROY vs. AVOIRDUPOIS — THE ASSAY ERROR THAT KEEPS HAPPENING` — Barlow SemiBold, `22` pt, `#E05C5C`. X: **0.8"**, Y: **26.4"**.

**18c — Two large value blocks:**

Troy ounce (left):
- `1 troy oz = 31.1 g` — JetBrains Mono Regular, `36` pt, `#E8A020`. X: **4.0"**, Y: **27.0"**.

Avoirdupois ounce (right):
- `1 avdp oz = 28.35 g` — JetBrains Mono Regular, `36` pt, `#C8D0D8`. X: **13.5"**, Y: **27.0"**.

**18d — Body footer:**
- Font: Inter Medium, `14` pt, `#F0EDE8`, Center. X: **0.8"**, Y: **28.0"**, Width: `22.4"`.
- Text: `Precious metals are sold and assayed in TROY ounces. Lab balances read in grams or avoirdupois. Mixing the two has cost more than one shop a five-figure refining error — always confirm units on every assay.`

### Step 19 — Paired callouts (Block F)

Y: 29.0" to 32.0".

**19a — Sulfite Gold pH callout (left half):**
- Rounded rectangle, X: **0.5"**, Y: **29.0"**, W: `11.25"`, H: `3.0"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `3.0"`, fill `#E8A020`.
- Title: `SULFITE GOLD — pH IS LIFE` — Barlow SemiBold, `18` pt, `#E8A020`. X: **0.8"**, Y: **29.2"**.
- Body: Inter Regular, `14` pt, `#F0EDE8`, line height 145%. X: **0.8"**, Y: **29.7"**, Width: `10.7"`.
  - Text: `Sulfite gold complexes are stable only above pH 8.0. Drop below 8.0 and the bath decomposes — the gold drops out as a black sludge and the entire tank is lost. Monitor pH daily; never let it drift.`

**19b — Hard vs. Soft Gold Efficiency callout (right half):**
- Rounded rectangle, X: **12.25"**, Y: **29.0"**, W: `11.25"`, H: `3.0"`, fill `#1E2435`, radius `6`.
- Left accent: `0.06"` x `3.0"`, fill `#27AE60` (Emerald).
- Title: `SOFT vs. HARD GOLD — EFFICIENCY GAP` — Barlow SemiBold, `18` pt, `#27AE60`. X: **12.55"**, Y: **29.2"**.

Two-column data inside:

Left side (Soft):
- `SOFT GOLD` — Barlow SemiBold, `14` pt, `#27AE60`. X: **12.55"**, Y: **29.7"**.
- `95–100%` — JetBrains Mono Regular, `28` pt, `#27AE60`. X: **12.55"**, Y: **30.1"**.
- `cathode efficiency` — Inter Regular, `11` pt, `#F0EDE8` at 70%. X: **12.55"**, Y: **30.85"**.

Right side (Hard):
- `HARD GOLD` — Barlow SemiBold, `14` pt, `#E05C5C`. X: **17.85"**, Y: **29.7"**.
- `25–35%` — JetBrains Mono Regular, `28` pt, `#E05C5C`. X: **17.85"**, Y: **30.1"**.
- `cathode efficiency` — Inter Regular, `11` pt, `#F0EDE8` at 70%. X: **17.85"**, Y: **30.85"**.

Footer line:
- `A hard gold tank uses 3x the ampere-hours per gram plated. Quote and cost accordingly.` — Inter Medium, `12` pt, `#F0EDE8`. X: **12.55"**, Y: **31.4"**, Width: `10.7"`.

### Step 20 — Group all of Zone 3

---

## Phase 5 — Zone 4: Footer Band

### Step 21 — Footer band
- Rectangle. W: `24.0"`. H: `3.5"`. Fill: `#0D1020`. X: **0"**, Y: **32.5"**.

### Step 22 — Disclaimer
- Text: `This poster is an educational quick reference. Operating parameters for proprietary precious-metals baths must always be verified against the supplier's current technical data sheet. Cyanide chemistries are hazardous — follow all applicable health, safety, and waste-treatment regulations.`
- Font: Inter Regular, `11` pt, `#F0EDE8` at 50%, Center. X: **0.5"**, Y: **32.8"**.

### Step 23 — Poster title
- Text: `Precious Metals — Gold and Silver Quick Reference`
- Font: Barlow SemiBold, `16` pt, `#F0EDE8`. X: **0.5"**, Y: **33.5"**.

### Step 24 — Series name, logo, version
- Series: `Plating Posters Inc — Metal Finishing Reference Series` — Inter Regular, `14` pt, `#F0EDE8` at 70%, Center. Y: **34.2"**.
- Logo: Rectangle `0.83"` x `0.42"`, fill `#3A4055`. Text: `[LOGO]`. X: **22.5"**, Y: **33.3"**.
- Version: `v1.0 — 2026` — JetBrains Mono Regular, `11` pt, `#F0EDE8` at 50%. X: **0.5"**, Y: **35.0"**.

---

## Phase 6 — Final Review Checklist

- [ ] Headline: `PRECIOUS METALS` at 96 pt
- [ ] Gold column: Amber header bar with `GOLD (Au)`, 5-row bath table, key-data callout
- [ ] Silver column: Bright Silver header bar with `SILVER (Ag)`, 3-row bath table, key-data callout
- [ ] Efficiency values color-coded: green (>=90%), amber (60-89%), coral (<60%)
- [ ] Silver Strike Rule full-width callout with Teal accent
- [ ] Troy vs. Avoirdupois callout with two large value blocks (31.1 g vs. 28.35 g)
- [ ] Sulfite pH callout (left) + Hard/Soft efficiency callout (right)
- [ ] All text within safe zone; footer complete

---

## Phase 7 — Light Edition: Remap

| Change From | Change To |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#5A6470` |
| `#F5C870` | `#A87015` |

**Light edition override:** The silver column header bar (`#C8D0D8`) becomes `#5A6470` in Light edition. Switch header text from `#1A1F2E` to `#F0EDE8` for legibility on the darkened silver fill.

---

## Phase 8 — Export

### Export file checklist
- [ ] `Precious Metals — Dark — 24x36 — Print.pdf`
- [ ] `Precious Metals — Dark — 18x24 — Print.pdf`
- [ ] `Precious Metals — Dark — Digital.pdf`
- [ ] `Precious Metals — Light — 24x36 — Print.pdf`
- [ ] `Precious Metals — Light — 18x24 — Print.pdf`
- [ ] `Precious Metals — Light — Digital.pdf`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-20 | Initial build prompt. Engineered by Elara from Alaina's Construction Workup v1.0. |
