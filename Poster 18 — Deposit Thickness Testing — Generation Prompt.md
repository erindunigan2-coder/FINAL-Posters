---
Project: Plating Posters Inc
Poster Number: 18
Title: "Deposit Thickness Testing — Methods, Ranges, and When to Use Each"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-20T00:00:00
Source: Poster 18 — Deposit Thickness Testing — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - DepositTesting
  - Thickness
  - QualityControl
  - v1
---

# Claude Chat Generation Prompt — Poster #18
## Deposit Thickness Testing — Methods, Ranges, and When to Use Each
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
| Data/formulas | JetBrains Mono | Regular (400) | Monospace for ASTM numbers, values |

### Brand Colors (Dark Edition)

| Name | Hex | Role |
|------|-----|------|
| Gunmetal Dark | `#1A1F2E` | Background |
| Warm White | `#F0EDE8` | Body text |
| Amber | `#E8A020` | Coulometric (semi-destructive) accent |
| Teal | `#2EC4B6` | XRF (non-destructive, primary) accent |
| Emerald | `#27AE60` | Eddy Current, Magnetic Gage accents |
| Coral | `#E05C5C` | Cross-section, Weigh-Strip-Weigh (destructive) accents |
| Mid Slate | `#3A4055` | Dividers, pills, table headers |
| Deep Navy | `#0D1020` | Footer band |
| Dark Callout | `#1E2435` | Card fills |
| Alt Row | `#252B3D` | Alternate ladder steps |

### Layout Safe Zones
- **0.5" margin** on all sides

---

## Phase 2 — Zone 1: Header Band

### Step 6 — Headline
- Text: `DEPOSIT THICKNESS TESTING`
- Font: Barlow Condensed ExtraBold, `88` pt, `#F0EDE8`, letter spacing `-4`. X: **0.5"**, Y: **0.5"**.

### Step 7 — Subheading
- Text: `Methods, Ranges, and When to Use Each`
- Font: Barlow SemiBold, `36` pt, `#2EC4B6`. X: **0.5"**, Y: **1.5"**.

### Step 8 — Tagline
- Text: `The most common QC measurement in the plating shop — done six different ways.`
- Font: Barlow SemiBold, `22` pt, `#F0EDE8` at 65%. X: **0.5"**, Y: **2.2"**.

---

## Phase 3 — Zone 2: Six-Method Comparison (HERO)

Y: 2.9" to 24.5" (~21.6" tall). Six stacked horizontal method cards.

### Step 9 — Section label
- Text: `SIX METHODS — KNOW WHICH ONE TO PICK`
- Font: Barlow Condensed ExtraBold, `30` pt, `#F0EDE8`, Center. Y: **3.1"**.

### Step 10 — Build six method cards

Each card: Rounded rectangle, X: **0.5"**, W: `23.0"`, H: `3.2"`, fill `#1E2435`, radius `6`.
Left accent bar: `0.06"` wide, full height, method-specific color.

Card internal layout:
- **Icon area:** X: **0.8"** to **2.8"** (2.0" wide), centered vertically. Use a simple geometric icon or glyph representing the method.
- **Method name:** Barlow Condensed ExtraBold, `28` pt, method color. X: **3.0"**, top of card + 0.2".
- **ASTM standard:** JetBrains Mono Regular, `16` pt, `#F0EDE8` at 70%. Below method name.
- **Principle:** Inter Medium, `16` pt, `#F0EDE8`. Below ASTM.
- **Three data tags (right side):** Small pills (rounded rectangles, fill `#3A4055`) with JetBrains Mono Regular `13` pt text.
- **"Best for" line:** Inter Regular, `14` pt, `#F0EDE8` at 80%, italic. Bottom of card.

---

**Card 1 — XRF (X-Ray Fluorescence)** — Y: **3.8"**
- Accent: `#2EC4B6` (Teal). Name: `XRF` in Teal.
- ASTM: `ASTM B568`
- Principle: `Excites coating atoms with X-rays; measures characteristic fluorescence energy.`
- Tags: `Range: 0.000004"–0.002"` | `NON-DESTRUCTIVE` | `~1 min/reading`
- Best for: `Multi-layer plating, precious metals, production QC, any metal-on-metal`

**Card 2 — Coulometric Stripping** — Y: **7.2"**
- Accent: `#E8A020` (Amber). Name: `COULOMETRIC` in Amber.
- ASTM: `ASTM B504`
- Principle: `Strips coating electrochemically; uses Faraday's Law to convert charge to thickness.`
- Tags: `Range: 0.00002"–0.002"` | `SEMI-DESTRUCTIVE` | `~2 min/reading`
- Best for: `High-accuracy single-layer measurement; calibration of XRF; small spot testing`

**Card 3 — Eddy Current** — Y: **10.6"**
- Accent: `#27AE60` (Emerald). Name: `EDDY CURRENT` in Emerald.
- ASTM: `ASTM B244`
- Principle: `Induces eddy currents in the substrate; measures coating-induced impedance change.`
- Tags: `Range: 0.0001"–0.002"` | `NON-DESTRUCTIVE` | `Instant`
- Best for: `Non-conductive coatings (anodize, paint) on conductive substrates`

**Card 4 — Magnetic Gage** — Y: **14.0"**
- Accent: `#27AE60` (Emerald). Name: `MAGNETIC GAGE` in Emerald.
- ASTM: `ASTM B499`
- Principle: `Measures magnetic flux pull between probe and ferrous substrate through the coating.`
- Tags: `Range: 0.0004"+ (10 µm)` | `NON-DESTRUCTIVE` | `Instant`
- Best for: `Non-magnetic coatings (Zn, Cu, Ni-P, paint) on steel or iron`

**Card 5 — Cross-Section Microscopy** — Y: **17.4"**
- Accent: `#E05C5C` (Coral). Name: `CROSS-SECTION` in Coral.
- ASTM: `ASTM B487`
- Principle: `Cuts, mounts, polishes, and measures the coating directly under a calibrated microscope.`
- Tags: `Range: any thickness` | `DESTRUCTIVE` | `~30+ min/sample`
- Best for: `Referee method — calibrates all others; failure analysis; complex multilayer systems`

**Card 6 — Weigh-Strip-Weigh** — Y: **20.8"**
- Accent: `#E05C5C` (Coral). Name: `WEIGH-STRIP-WEIGH` in Coral.
- ASTM: `ASTM B767`
- Principle: `Weighs part, strips coating chemically, weighs again; calculates from area and density.`
- Tags: `Range: any uniform coating` | `DESTRUCTIVE` | `~15 min/sample`
- Best for: `Average coating weight on simple geometry; statistical sampling`

### Step 11 — Group all of Zone 2

---

## Phase 4 — Zone 3: Unit Conversion + Decision Callout

Y: 24.5" to 32.5" (~8.0" tall). Two-column layout.

### Step 12 — Section label
- Text: `KNOW YOUR UNITS`
- Font: Barlow Condensed ExtraBold, `26` pt, `#F0EDE8`, Center. Y: **24.7"**.

### Step 13 — Unit Conversion Ladder (left half, X: 0.5" to 11.5")

**13a — Container:**
- Rounded rectangle. X: **0.5"**, Y: **25.4"**. W: `11.0"`. H: `6.4"`. Fill: `#1E2435`. Radius: `8`.
- Left accent: `0.06"` x `6.4"`, `#E8A020`.

**13b — Title:** `THICKNESS UNIT LADDER` — Barlow SemiBold, `20` pt, `#E8A020`. X: **0.8"**, Y: **25.6"**.

**13c — Sub-title:** `All five values below are EQUIVALENT — same thickness, different units.` — Inter Regular, `13` pt, `#F0EDE8` at 70%. X: **0.8"**, Y: **26.1"**.

**13d — Five ladder rows** (each 0.85" tall, alternating `#252B3D` / `#1A1F2E`):

| Row | Y | Unit Name | Value | Note |
|-----|---|-----------|-------|------|
| 1 | 26.6" | `INCH` | `0.0002"` | `(common spec unit, USA)` |
| 2 | 27.5" | `TENTHS` | `2 tenths` | `(1 tenth = 0.0001 inch)` |
| 3 | 28.4" | `MICRO-INCH` | `200 µin` | `(common XRF/precious metals unit)` |
| 4 | 29.3" | `MICRON` | `5.1 µm` | `(SI / international standard)` |
| 5 | 30.2" | `MIL` | `0.2 mil` | `(1 mil = 25.4 microns = 0.001 inch)` |

- Unit name: Barlow SemiBold, `18` pt, `#F0EDE8`. X: **1.0"**.
- Value: JetBrains Mono Regular, `22` pt, `#2EC4B6`. X: **8.5"**, right-aligned.
- Note: Inter Regular, `12` pt italic, `#F0EDE8` at 60%. Centered.

**13e — Conversion key:**
- Text: `1 mil = 25.4 µm = 1000 µin   |   1 µm = 39.37 µin`
- Font: JetBrains Mono Regular, `13` pt, `#E8A020`, Center. X: **0.8"**, Y: **31.2"**. Width: `10.4"`.

### Step 14 — "Which Method?" Decision Callout (right half, X: 12.0" to 23.5")

**14a — Container:**
- Rounded rectangle. X: **12.0"**, Y: **25.4"**. W: `11.5"`. H: `6.4"`. Fill: `#1E2435`. Radius: `8`.
- Left accent: `0.06"` x `6.4"`, `#2EC4B6`.

**14b — Title:** `WHICH METHOD SHOULD I USE?` — Barlow SemiBold, `20` pt, `#2EC4B6`. X: **12.3"**, Y: **25.6"**.

**14c — Decision rows** (question in `#F0EDE8` at 70%, answer in `#F0EDE8` full):

| Y | Question → | Answer |
|---|-----------|--------|
| 26.2" | `Need fast non-destructive readings on production parts? →` | `XRF` |
| 27.0" | `Coating on steel and you only need average thickness? →` | `MAGNETIC GAGE` |
| 27.8" | `Anodize or paint over aluminum? →` | `EDDY CURRENT` |
| 28.6" | `Need maximum accuracy or to settle a dispute? →` | `CROSS-SECTION (referee)` |
| 29.4" | `XRF reads questionable — need to verify? →` | `COULOMETRIC` |

Font: Inter Regular `15` pt (question), Inter Medium `15` pt (answer).

**14d — Critical reminder:**
- Text: `EVERY method requires periodic calibration against a traceable standard. Cross-section is the only true referee — all others measure something INDIRECTLY proportional to thickness.`
- Font: Inter Medium, `14` pt, `#E8A020`. X: **12.3"**, Y: **30.4"**. Width: `11.0"`.

### Step 15 — Group all of Zone 3

---

## Phase 5 — Zone 4: Footer Band

### Step 16 — Footer band
- Rectangle. W: `24.0"`. H: `3.5"`. Fill: `#0D1020`. X: **0"**, Y: **32.5"**.

### Step 17 — Disclaimer
- Text: `Accuracy ranges shown are typical industry values. Performance depends on instrument calibration, coating system, substrate, operator skill, and ambient conditions. Always follow the relevant ASTM standard and your QMS procedure.`
- Font: Inter Regular, `11` pt, `#F0EDE8` at 50%, Center. X: **0.5"**, Y: **32.8"**.

### Step 18 — Poster title
- Text: `Deposit Thickness Testing — Methods, Ranges, and When to Use Each`
- Font: Barlow SemiBold, `16` pt, `#F0EDE8`. X: **0.5"**, Y: **33.5"**.

### Step 19 — Series name, logo, version
- Series: `Plating Posters Inc — Metal Finishing Reference Series` — Inter Regular, `14` pt, `#F0EDE8` at 70%, Center. Y: **34.2"**.
- Logo: Rectangle `0.83"` x `0.42"`, fill `#3A4055`. Text: `[LOGO]`. X: **22.5"**, Y: **33.3"**.
- Version: `v1.0 — 2026` — JetBrains Mono Regular, `11` pt, `#F0EDE8` at 50%. X: **0.5"**, Y: **35.0"**.

---

## Phase 6 — Final Review Checklist

- [ ] Headline: `DEPOSIT THICKNESS TESTING` at 88 pt
- [ ] Six method cards present: XRF, Coulometric, Eddy Current, Magnetic Gage, Cross-Section, Weigh-Strip-Weigh
- [ ] Each card has: icon area, method name, ASTM #, principle, 3 data tags, "best for" line
- [ ] Color coding: Teal (XRF), Amber (Coulometric), Emerald (Eddy Current + Magnetic), Coral (Cross-Section + WSW)
- [ ] Unit ladder: 5 rows all equivalent to 0.0002"
- [ ] Decision callout: 5 question→answer rows
- [ ] Critical reminder about calibration present
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

---

## Phase 8 — Export

### Export file checklist
- [ ] `Thickness Testing — Dark — 24x36 — Print.pdf`
- [ ] `Thickness Testing — Dark — 18x24 — Print.pdf`
- [ ] `Thickness Testing — Dark — Digital.pdf`
- [ ] `Thickness Testing — Light — 24x36 — Print.pdf`
- [ ] `Thickness Testing — Light — 18x24 — Print.pdf`
- [ ] `Thickness Testing — Light — Digital.pdf`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-20 | Initial build prompt. Engineered by Elara from Alaina's Construction Workup v1.0. |
