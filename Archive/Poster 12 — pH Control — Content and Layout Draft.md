---
Project: Plating Posters Inc
Poster Number: 12
Title: "The pH Control Poster"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — pH Control Research Brief v1 (2026-04-03)
Watson Flags: THREE — A Brite product pH ranges, acid copper pH listing, NiCO3 as nickel pH agent (Drew + Tyler, non-blocking)
Process Scope: pH measurement and control — universal across all plating processes
Editions: Dark + Light
tags:
  - PosterDesign
  - pHControl
  - ContentDraft
---

# Poster #12 — Content and Layout Draft
## The pH Control Poster

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's pH Control Research Brief v1. This poster transforms pH from a number operators hit into a variable they understand — what it is, where each process lives on the scale, what happens when it drifts, and how to adjust it.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: THREE FLAGS — non-blocking.**

**Flag 1 (Drew):** Confirm pH ranges for A Brite products, especially Brite-Zinc 404, CN-707, AG-1, SN-M.

**Flag 2 (Drew):** Confirm acid copper listing as "not pH-controlled" — some labs report pH as a convenience.

**Flag 3 (Tyler):** Confirm NiCO3 as the recommended pH raise agent for nickel baths in A Brite procedures.

**Design decisions:**

- **HERO: the pH Scale with process bars.** A large, prominent pH scale (0-14) with every major plating process marked as a colored horizontal bar at its operating range. This is the poster's visual anchor — the thing you see from across the room. It communicates instantly where each process lives and how different they are from each other.

- **This poster is visually striking because the data is striking.** Hard chrome operates below pH 1 while alkaline zinc operates above pH 13 — they share the same industry and the same shops, yet they occupy opposite extremes of the pH scale. The visual makes this fact dramatic and memorable.

- **"What happens when pH drifts" is the action section.** Two comparison tables (pH too low / pH too high) for the most common processes. This is the section an operator reads when they get an out-of-range pH reading.

- **Buffer concept included.** Most operators do not know why boric acid is in their bath. A brief buffer explanation elevates understanding.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "The Logarithmic Fact" callout (right ~45%)                    |
+------------------------------------------------------------------------+
| ZONE 2 — THE pH SCALE (HERO) (~8-40% / 11.5")                         |
| BLOCK C: Full-width vertical pH scale with process range bars            |
+------------------------------------------------------------------------+
| ZONE 3 — WHAT HAPPENS WHEN pH DRIFTS (~40-60% / 7.2")                 |
| BLOCK D: "pH Too Low" effects table (left 50%)                          |
| BLOCK E: "pH Too High" effects table (right 50%)                        |
+------------------------------------------------------------------------+
| ZONE 4 — ADJUSTMENT + MEASUREMENT (~60-80% / 7.2")                    |
| BLOCK F: Adjustment chemicals table (left 55%)                           |
| BLOCK G: pH measurement best practices (right 45%)                       |
+------------------------------------------------------------------------+
| ZONE 5 — BUFFER CONCEPT (~80-90% / 3.6")                              |
| BLOCK H: Buffer explanation callout + boric acid note                    |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK I: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + logarithmic fact | 8% | 2.9" |
| 2 — pH Scale | HERO visual | 32% | 11.5" |
| 3 — Drift Effects | Low/high tables | 20% | 7.2" |
| 4 — Adjustment | Chemicals + measurement | 20% | 7.2" |
| 5 — Buffers | Buffer concept | 10% | 3.6" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 96 pt, `#F0EDE8`):**

> pH CONTROL

**Subheading (Barlow SemiBold, 40 pt, `#E8A020`):**

> The Number Every Bath Depends On

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> Small numbers, big chemistry. Know your range.

---

### BLOCK B — "The Logarithmic Fact" Callout (Header Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#2EC4B6`):**

> THE LOGARITHMIC SCALE

**Body (Inter Regular, 16 pt, `#F0EDE8`):**

> Each whole pH number = 10x change in H⁺ concentration. A bath at pH 4.0 has 10x more acid than pH 5.0, and 100x more than pH 6.0.

**Formula (JetBrains Mono Regular, 18 pt, `#F0EDE8`):**

> pH = -log[H⁺]

**Closing (Inter Medium, 14 pt, `#2EC4B6`):**

> Small pH changes = big chemical changes.

---

### BLOCK C — The pH Scale (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):**

> OPERATING pH FOR EVERY MAJOR PROCESS

**Scale construction:** A vertical pH scale from 0 (top) to 14 (bottom), occupying the left ~15% of the zone width. Process range bars extend horizontally to the right from the scale.

**pH scale column (left):**
- Vertical line, 2 pt, `#3A4055`, from Y top to Y bottom of zone
- Number labels at each integer (0, 1, 2... 14) — JetBrains Mono Regular, 18 pt, `#F0EDE8`
- Color gradient background behind the scale: deep red at pH 0 → orange at pH 3 → neutral gray at pH 7 → blue at pH 10 → deep blue at pH 14 (built as stacked rectangles in Canva, each ~0.8" tall, with graduated fills)
  - pH 0-2: `#E05C5C` Coral at varying opacity (100% to 60%)
  - pH 3-6: `#E8A020` Amber at varying opacity (60% to 20%)
  - pH 7: `#3A4055` Mid Slate (neutral)
  - pH 8-11: `#2EC4B6` Teal at varying opacity (20% to 60%)
  - pH 12-14: `#2EC4B6` Teal at higher opacity (60% to 100%)

**Process range bars (right of scale):**

Each bar: horizontal rounded rectangle, 0.5" tall, accent-colored fill at 70% opacity, with process name at left edge and pH range at right edge.

Bars positioned at their pH range on the scale:

| Process | pH Range | Bar Color |
|---------|----------|-----------|
| Hard chrome | <1.0 | `#E05C5C` Coral |
| Matte tin | 0.5-2.0 | `#E05C5C` |
| Hex passivation | 0.5-2.0 | `#E05C5C` |
| Trivalent passivation | 1.5-2.5 | `#E8A020` Amber |
| Watts nickel | 3.8-4.5 | `#E8A020` |
| EN (Mid-P) | 4.5-5.2 | `#E8A020` |
| Acid chloride zinc | 4.8-5.8 | `#27AE60` Emerald |
| Nickel sulfamate | 3.5-4.5 | `#E8A020` |
| Alkaline cleaners | 10-13 | `#2EC4B6` Teal |
| Cyanide copper strike | 11-13 | `#2EC4B6` |
| Silver cyanide | 11.5-13 | `#2EC4B6` |
| Alkaline NC zinc | 12.5-14 | `#2EC4B6` |
| Alkaline CN zinc | 12-13.5 | `#2EC4B6` |

Bar labels: Process name in Inter Medium 14 pt `#F0EDE8` (left side), pH range in JetBrains Mono 14 pt `#F0EDE8` (right side).

**Target line within each bar:** A thin vertical line at the target pH value, 2 pt, `#F0EDE8`.

**Key callouts on the scale:**

- At pH 7: `NEUTRAL` label — Barlow SemiBold 14 pt, `#F0EDE8`
- At acid zinc bar: `EN: ±0.2 tolerance — check every 30-60 min` — Inter Regular, 11 pt, `#E8A020`
- At top: `STRONGLY ACIDIC` — Barlow SemiBold 12 pt, `#E05C5C`
- At bottom: `STRONGLY ALKALINE` — Barlow SemiBold 12 pt, `#2EC4B6`

**Note for acid copper (Inter Regular, 12 pt, `#F0EDE8` at 60%):**
> Acid copper is not pH-controlled — H₂SO₄ concentration is the control variable.

---

### BLOCK D — "pH Too Low" Effects Table (Zone 3 — Left)

**Title (Barlow Condensed ExtraBold, 22 pt, `#E05C5C`):**

> pH TOO LOW — MORE ACIDIC THAN TARGET

Table (2 columns: Process | Effect):

| Process | Effect |
|---------|--------|
| Acid zinc | Excessive anode dissolution; zinc rises uncontrollably |
| Watts nickel | Increased H₂ evolution; pitting; embrittlement risk |
| EN (Mid-P) | Higher P content; slower deposition; stabilizer imbalance |
| Trivalent passivation | Aggressive zinc attack; thinner film; etching |

Font: Inter Regular 15 pt. Left-border accents: `#E05C5C` Coral.

---

### BLOCK E — "pH Too High" Effects Table (Zone 3 — Right)

**Title (Barlow Condensed ExtraBold, 22 pt, `#E8A020`):**

> pH TOO HIGH — MORE ALKALINE THAN TARGET

| Process | Effect |
|---------|--------|
| Acid zinc | Brightener precipitation; cloudy solution; Zn(OH)₂ at >6.5 |
| Watts nickel | Ni(OH)₂ precipitation (green sludge); roughness |
| EN (Mid-P) | Lower P content; faster rate; bath decomposition risk |
| Trivalent passivation | Thicker film (intentional at 2.5 — Drew's note) |

Font: Inter Regular 15 pt. Left-border accents: `#E8A020` Amber.

---

### BLOCK F — Adjustment Chemicals Table (Zone 4 — Left)

**Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):**

> HOW TO ADJUST pH

**Table (4 columns: Chemical | Formula | Direction | Typical Process):**

| Chemical | Formula | Direction | Typical Process |
|----------|---------|-----------|-----------------|
| Sodium hydroxide | NaOH | Raise | Acid zinc, nickel, alkaline zinc |
| Potassium hydroxide | KOH | Raise | Silver baths; some alkaline zinc |
| Nickel carbonate | NiCO₃ | Raise (Ni baths) | Watts, sulfamate — preferred (adds Ni) |
| Ammonium hydroxide | NH₄OH | Raise (EN) | EN — avoids cation contamination |
| Sulfuric acid | H₂SO₄ | Lower | Watts nickel, EN, acid copper |
| Hydrochloric acid | HCl | Lower | Acid zinc (also adds Cl⁻ — caution) |
| Sulfamic acid | H₃NSO₃ | Lower | Sulfamate nickel (avoids Cl⁻/SO₄²⁻) |

**Safety callout (Inter Medium, 14 pt, `#E05C5C`):**

> Always add acid or base slowly, with mixing. Concentrated additions cause exothermic reactions and dangerous splashing.

---

### BLOCK G — pH Measurement Best Practices (Zone 4 — Right)

**Callout box:** fill `#1E2435`, border `#27AE60` Emerald 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#27AE60`):**

> pH MEASUREMENT BEST PRACTICES

**Bullet list (Inter Regular, 15 pt, `#F0EDE8`):**

> - Calibrate with TWO buffers before every use (pH 4 + 7 for acid; pH 7 + 10 for alkaline)
> - Calibrate at operating temperature (or apply temp correction)
> - Store electrode in KCl storage solution — NEVER in DI water
> - Replace electrode annually (or when response slows)
> - Rinse with DI water between samples

**pH paper note (Inter Regular, 13 pt, `#F0EDE8` at 60%):**

> pH paper: ±0.5 accuracy — acceptable for cleaners and rinses. Not accurate enough for nickel, EN, or passivation (±0.2 required).

---

### BLOCK H — Buffer Concept (Zone 5)

**Full-width callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 20 pt, `#2EC4B6`):**

> WHY YOUR BATH HAS BORIC ACID — THE BUFFER CONCEPT

**Body (Inter Regular, 16 pt, `#F0EDE8`):**

> Buffers resist pH change when acid or base is added. Boric acid — the most common buffer in electroplating — keeps nickel and zinc baths stable during plating, even as the cathode reaction produces H⁺. Without it, pH would swing wildly during operation.

**Buffer table (compact, 3 columns):**

| Bath | Buffer | Range |
|------|--------|-------|
| Watts nickel | Boric acid | pH 3.5-5.0 |
| Acid zinc | Boric acid | pH 4.5-6.0 |
| EN baths | Succinic/lactic acid | pH 4.0-5.5 |

**Closing (Inter Medium, 15 pt, `#2EC4B6`):**

> A well-buffered bath = stable pH = consistent deposits.

---

### BLOCK I — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents industry-typical pH ranges and adjustment methods. Specific operating parameters vary by product formulation — always consult your product TDS. pH measurement instruments require regular calibration for accurate results.`

**Poster title:** `The pH Control Poster`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The pH scale color gradient uses series palette colors at reduced opacity — remap the base colors per standard table. The gradient will appear inverted (Coral on a light background, Teal on a light background) which actually works well for readability.

Process range bars use accent colors at 70% opacity — after remap to darkened Light equivalents, verify bar text remains readable. No overrides anticipated.

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Drew (OPEN):** A Brite product pH ranges. Acid copper as "not pH-controlled."

**Tyler (OPEN):** NiCO₃ as the recommended pH raise agent for nickel.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #12 — The pH Control Poster — Content and Layout Draft v1.0*
*2026-04-04*
