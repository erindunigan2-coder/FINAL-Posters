---
Project: Plating Posters Inc
Poster Number: 8
Title: "Faraday's Law in the Shop: Calculating Plating Thickness"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Faraday's Law Research Brief v1 (2026-04-03)
Watson Flags: TWO — cathode efficiency values + practical vs. theoretical plating rate display (both Drew confirmation, non-blocking)
Process Scope: Universal electroplating math — applies across all electrolytic processes
Editions: Dark + Light
tags:
  - PosterDesign
  - FaradaysLaw
  - ContentDraft
  - Calculations
---

# Poster #8 — Content and Layout Draft
## Faraday's Law in the Shop: Calculating Plating Thickness

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Faraday's Law Research Brief v1. This poster makes the math of plating thickness calculation accessible — answering the three questions every plater asks daily. All ECE values are calculated from physical constants and verified by Watson.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: TWO FLAGS — both Drew confirmation, non-blocking.**

**Flag 1 (Drew):** Confirm cathode efficiency ranges match field experience, particularly acid chloride zinc (95-98%), alkaline zinc (70-80%), cyanide copper strike (30-60%), and hard chrome (12-20%).

**Flag 2 (Drew):** Confirm whether to show theoretical plating rate only, or include a practical rate column that incorporates typical efficiency.

**Design decisions:**

- **Layout: formula-centric with big data table.** The HERO is a dual element: the master formula (large, legible from 8 feet) and the electrochemical equivalents table (the reference operators walk up to use). Supporting elements: efficiency comparison bar, worked examples, and a unit conversion box.

- **The "Three Questions" framing.** Watson's brief nails it — every plater asks: (1) How thick? (2) How long? (3) How much current? Faraday answers all three. These three questions open the poster and frame everything that follows.

- **Chrome efficiency as dramatic contrast.** The worked examples must include a chrome calculation to show why chrome takes hours. The efficiency bar chart makes this visual — 97% of acid copper's current deposits metal, while only 15% of chrome's does.

- **No Faraday portrait.** Tempting but unnecessary — the data is the hero, not the history. A small attribution line in the footer is sufficient.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-9% / 3.2")                                    |
| BLOCK A: Headline + subheading (left ~55%)                              |
| BLOCK B: "Three Questions" callout (right ~45%)                         |
+------------------------------------------------------------------------+
| ZONE 2 — THE MASTER FORMULA (~9-18% / 3.2")                            |
| BLOCK C: Large formula box + variable legend strip                       |
+------------------------------------------------------------------------+
| ZONE 3 — ECE TABLE + EFFICIENCY (HERO) (~18-55% / 13.3")              |
| BLOCK D: Electrochemical Equivalents master table (left 60%)            |
| BLOCK E: Cathode Efficiency table (right 40%)                           |
+------------------------------------------------------------------------+
| ZONE 4 — EFFICIENCY BAR CHART (~55-68% / 4.7")                         |
| BLOCK F: "Where Does the Current Go?" horizontal bar comparison          |
+------------------------------------------------------------------------+
| ZONE 5 — WORKED EXAMPLES + CONVERSIONS (~68-90% / 7.9")               |
| BLOCK G: Two worked examples (left 65%)                                  |
| BLOCK H: Unit conversion + Faraday's constant box (right 35%)           |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK I: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + Three Questions | 9% | 3.2" |
| 2 — Formula | Master formula + legend | 9% | 3.2" |
| 3 — Tables | ECE table + efficiency table | 37% | 13.3" |
| 4 — Bar Chart | Efficiency comparison visual | 13% | 4.7" |
| 5 — Examples | Worked problems + conversions | 22% | 7.9" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 96 pt, `#F0EDE8`):**

> FARADAY'S LAW IN THE SHOP

**Subheading (Barlow SemiBold, 40 pt, `#E8A020`):**

> Calculating Plating Thickness

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> More amps x more time = more metal. Now do the math.

---

### BLOCK B — "Three Questions" Callout Box (Header Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 20 pt, `#2EC4B6`):**

> EVERY PLATER ASKS THREE QUESTIONS

**Three numbered questions (Inter Medium, 18 pt, `#F0EDE8`):**

> 1. How thick will my deposit be?
> 2. How long do I need to plate?
> 3. How much current do I need?

**Closing line (Inter Medium, 16 pt, `#2EC4B6`):**

> Faraday's Law answers all three.

---

### BLOCK C — The Master Formula (Zone 2)

**Background treatment:** Full-width rectangle, fill `#1E2435`, spanning Zone 2 height. This visually frames the formula as the poster's foundation.

**Formula (JetBrains Mono Regular, 36 pt, `#F0EDE8`, centered):**

> Thickness = Rate x ASF x Time x Efficiency

**Variable legend strip:** Four labeled color blocks below the formula, evenly spaced:

| Variable | Label | Accent Color |
|----------|-------|-------------|
| Rate | Plating rate (mil/Ah/ft²) — from the table below | `#2EC4B6` Teal |
| ASF | Current density (amps per square foot) | `#E8A020` Amber |
| Time | Hours | `#27AE60` Emerald |
| Efficiency | Cathode efficiency (decimal) | `#E05C5C` Coral |

Each block: small colored rectangle (0.3" x 0.3"), label text in Inter Regular 14 pt `#F0EDE8`, description in Inter Regular 12 pt, `#F0EDE8` at 70%.

---

### BLOCK D — Electrochemical Equivalents Master Table (Zone 3 — Left)

**Section label (Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`):**

> ELECTROCHEMICAL EQUIVALENTS

**Table structure — 6 columns:**
1. **Metal** (~16%) — Inter Medium, 17 pt, `#F0EDE8`
2. **Symbol** (~8%) — JetBrains Mono, 17 pt, `#F0EDE8`
3. **Valence** (~10%) — JetBrains Mono, 17 pt, `#F0EDE8`
4. **ECE (g/Ah)** (~18%) — JetBrains Mono, 17 pt, `#F0EDE8`
5. **Density (g/cm³)** (~18%) — JetBrains Mono, 17 pt, `#F0EDE8`
6. **Rate (mil/Ah/ft²)** (~18%) — JetBrains Mono, 17 pt, `#2EC4B6` Teal

Column header row: `#3A4055` Mid Slate fill, Barlow SemiBold 18 pt.

Data rows (alternating `#1A1F2E` / `#252B3D`):

| Metal | Symbol | Valence | ECE (g/Ah) | Density (g/cm³) | Rate (mil/Ah/ft²) |
|-------|--------|---------|------------|------------------|--------------------|
| Zinc | Zn | 2 | 1.220 | 7.14 | 0.00152 |
| Nickel | Ni | 2 | 1.095 | 8.90 | 0.00109 |
| Copper (acid) | Cu | 2 | 1.186 | 8.96 | 0.00118 |
| Copper (cyanide) | Cu | 1 | 2.372 | 8.96 | 0.00236 |
| Chromium (hex) | Cr | 6 | 0.324 | 7.19 | 0.00040 |
| Silver | Ag | 1 | 4.025 | 10.49 | 0.00342 |
| Tin | Sn | 2 | 2.214 | 7.31 | 0.00270 |
| Gold (Au⁺) | Au | 1 | 7.349 | 19.32 | 0.00339 |
| Gold (Au³⁺) | Au | 3 | 2.450 | 19.32 | 0.00113 |
| Cadmium | Cd | 2 | 2.097 | 8.65 | 0.00216 |

**Table footnote (Inter Regular, 12 pt, `#F0EDE8` at 60%, italic):**

> ECE = Atomic Weight / (Valence x 26.80 Ah). Rate = ECE / (Density x 60.5). All values are theoretical — multiply by cathode efficiency for actual deposit.

**Copper valence callout (Inter Regular, 14 pt, `#E8A020`, below table):**

> Cyanide copper (Cu⁺) deposits 2x the mass per amp-hour vs. acid copper (Cu²⁺) — same element, different chemistry.

---

### BLOCK E — Cathode Efficiency Table (Zone 3 — Right)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> CATHODE EFFICIENCY

**Intro text (Inter Regular, 14 pt, `#F0EDE8`):**

> Not all current deposits metal. The rest generates hydrogen gas. Efficiency = actual deposit / theoretical maximum.

**Table structure — 2 columns:**
1. **Process** (~55%) — Inter Regular, 16 pt
2. **Efficiency** (~45%) — JetBrains Mono, 16 pt

Column header row: `#3A4055` fill.

Data rows (alternating fills, left-border accent by severity):

| Process | Efficiency | Left Border Color |
|---------|-----------|-------------------|
| Bright acid copper | 95-100% | `#27AE60` Emerald |
| Nickel sulfamate | 95-100% | `#27AE60` |
| Silver cyanide | 95-100% | `#27AE60` |
| Watts nickel | 93-97% | `#27AE60` |
| Acid chloride zinc | 95-98% | `#27AE60` |
| Matte tin (acid) | 90-95% | `#27AE60` |
| Alkaline NC zinc | 70-80% | `#E8A020` Amber |
| Alkaline cyanide zinc | 65-80% | `#E8A020` |
| Cyanide copper strike | 30-60% | `#E05C5C` Coral |
| Hard chrome (hex) | 12-20% | `#E05C5C` |
| Decorative chrome (hex) | 10-18% | `#E05C5C` |

---

### BLOCK F — "Where Does the Current Go?" Efficiency Bar Chart (Zone 4)

**Section label (Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`, centered):**

> WHERE DOES THE CURRENT GO?

**Layout:** 4 horizontal bars, full width within margins.

Each bar: full-width rectangle (23.0" total), divided into two segments:
- Left segment (Emerald `#27AE60`): metal deposited
- Right segment (Coral `#E05C5C`): wasted (hydrogen + heat)

**Bar 1 — Acid Copper:**
- Emerald: 97% width | Coral: 3% width
- Label left: `Acid Copper` — Inter Medium, 16 pt
- Label on emerald segment: `97% metal` — JetBrains Mono, 14 pt
- Label on coral segment: `3%` — JetBrains Mono, 12 pt

**Bar 2 — Watts Nickel:**
- Emerald: 95% | Coral: 5%
- Label: `Watts Nickel`

**Bar 3 — Acid Zinc:**
- Emerald: 96% | Coral: 4%
- Label: `Acid Zinc`

**Bar 4 — Hard Chrome:**
- Emerald: 15% | Coral: 85%
- Label: `Hard Chrome`
- **This bar is visually dramatic** — the coral section dominates

**Caption below (Inter Medium, 16 pt, `#E05C5C`):**

> Hard chrome: 85% of the electrical energy becomes hydrogen gas and heat — not metal.

---

### BLOCK G — Worked Examples (Zone 5 — Left)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> WORKED EXAMPLES

Two example callout boxes, stacked vertically.

**Example 1 — Zinc:**

Callout box: fill `#1E2435`, left border 4 pt `#27AE60` Emerald, corner radius 6 pt

Title (Barlow SemiBold, 18 pt, `#27AE60`):
> How long to plate 0.5 mil zinc at 20 ASF?

Calculation (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 160%):
> Time = Thickness / (Rate x ASF x CE)
> Time = 0.5 / (0.00152 x 20 x 0.96)
> Time = 0.5 / 0.02918
> Time = 17.1 minutes

Answer (Inter Medium, 16 pt, `#27AE60`):
> Approximately 17 minutes at 20 ASF.

**Example 2 — Hard Chrome:**

Callout box: fill `#1E2435`, left border 4 pt `#E05C5C` Coral, corner radius 6 pt

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> How long for 2.0 mil hard chrome at 200 ASF?

Calculation (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 160%):
> Time = 2.0 / (0.00040 x 200 x 0.15)
> Time = 2.0 / 0.012
> Time = 166.7 minutes ≈ 2 hr 47 min

Answer (Inter Medium, 16 pt, `#E05C5C`):
> Nearly 3 hours — 10x the current density, still takes 10x longer than zinc.

---

### BLOCK H — Unit Conversions + Faraday's Constant (Zone 5 — Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#2EC4B6`):**

> FARADAY'S CONSTANT

**Constant (JetBrains Mono Regular, 20 pt, `#F0EDE8`, centered):**

> F = 96,485 C/mol = 26.80 Ah/eq

**Explanation (Inter Regular, 14 pt, `#F0EDE8`):**

> 26.80 ampere-hours will deposit exactly one gram-equivalent weight of any metal.

---

**Second callout — Unit Conversions:**

Callout box: fill `#1E2435`, no border, corner radius 6 pt

**Title (Barlow SemiBold, 16 pt, `#F0EDE8`):**

> QUICK CONVERSIONS

**Conversion list (JetBrains Mono Regular, 16 pt, `#F0EDE8`, line height 180%):**

> 1 mil = 25.4 um
> 1 um = 0.0394 mil
> ASF / 10 ≈ ASD
> 1 Ah = 3,600 C

---

### BLOCK I — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents theoretical calculations from Faraday's Laws of Electrolysis. Actual deposit thickness depends on cathode efficiency, current distribution, agitation, and bath condition. Always verify critical thickness specifications by direct measurement.`

**Poster title:** `Faraday's Law in the Shop: Calculating Plating Thickness`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The efficiency bar chart uses Emerald and Coral as large fill areas — both darken for the Light edition. Verify the bar labels remain readable on darkened fills (they should, as labels use `#F0EDE8` which remaps to `#1A1F2E` — dark text on darkened accent fills should work).

The Four Essentials strip top accent bars also use series colors — verify after remap per the Light edition override rule in the Design Standards.

---

## Section 5 — Collaboration Flags

**Watson:** All ECE values verified from first principles. No additional research needed.

**Drew (OPEN):** Confirm cathode efficiency ranges. Confirm preference for theoretical-only or theoretical + practical plating rates in the table.

**Tyler (OPEN):** Verify ECE calculations match any existing A Brite TDS thickness tables.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #8 — Faraday's Law in the Shop — Content and Layout Draft v1.0*
*2026-04-04*
