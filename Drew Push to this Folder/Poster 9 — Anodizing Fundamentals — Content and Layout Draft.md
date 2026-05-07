---
Project: Plating Posters Inc
Poster Number: 9
Title: "Anodizing Fundamentals: Type I, II, and III at a Glance"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Anodizing Fundamentals Research Brief v1 (2026-04-03)
Watson Flags: THREE — Type II CD range, alloy compatibility notes, A Brite product names on poster (all Drew, non-blocking)
Process Scope: Anodizing (Types I, II, III per MIL-A-8625) — aluminum only
Editions: Dark + Light
tags:
  - PosterDesign
  - Anodizing
  - ContentDraft
---

# Poster #9 — Content and Layout Draft
## Anodizing Fundamentals: Type I, II, and III at a Glance

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Anodizing Fundamentals Research Brief v1. This poster clarifies the three anodizing types and the critical distinction from electroplating — the part IS the anode.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: THREE FLAGS — all Drew, non-blocking.**

**Flag 1 (Drew):** Confirm Type II CD range — 12-18 ASF used (MIL-A-8625 standard).

**Flag 2 (Drew):** Confirm alloy compatibility notes, especially cast alloys (A356, 380).

**Flag 3 (Drew):** A Brite products (ALE-680, ALE-650, NC-620) appear in pre-treatment. Keep product names on poster or use generic terms?

**Design decisions:**

- **HERO: three-column comparison table.** Type I | Type II | Type III side by side — the "at a glance" promised in the title. This is the core reference content. Each column gets a distinct accent color to reinforce the three types visually.

- **Color assignment for anodizing types:** Type I = Amber `#E8A020` (caution — Cr6+ content). Type II = Teal `#2EC4B6` (standard, versatile, the most common). Type III = Coral `#E05C5C` (heavy-duty, extreme conditions). This differs from Watson's suggestion of Emerald for Type III — I chose Coral because it better represents the extreme operating conditions (near-freezing temperature, 100V+), and Emerald is reserved for "positive/good" semantics across the series.

- **The "Part = Anode" concept diagram.** This must be prominent — it is the single most important educational element on this poster. Most people coming from an electroplating background assume the part is always the cathode. Anodizing inverts that, and the poster needs to make this impossible to miss.

- **Pore structure illustration.** The hexagonal cell structure is iconic and unique to anodizing. A simplified cross-section showing the barrier layer, porous columns, and sealed tops reinforces why anodizing produces permanent color (dye trapped in pores) and excellent corrosion resistance.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "Not Electroplating" callout (right ~45%)                      |
+------------------------------------------------------------------------+
| ZONE 2 — THREE-TYPE COMPARISON TABLE (HERO) (~8-45% / 13.3")          |
| BLOCK C: Three-column comparison — Type I | Type II | Type III          |
+------------------------------------------------------------------------+
| ZONE 3 — CONCEPT + PORE STRUCTURE (~45-65% / 7.2")                    |
| BLOCK D: "Part = Anode" diagram (left 45%)                              |
| BLOCK E: Pore structure cross-section (right 55%)                        |
+------------------------------------------------------------------------+
| ZONE 4 — ALLOY COMPAT + PRE-TREATMENT (~65-82% / 6.1")               |
| BLOCK F: Alloy compatibility chart (left 55%)                            |
| BLOCK G: Pre-treatment flow + defects (right 45%)                        |
+------------------------------------------------------------------------+
| ZONE 5 — SPECIFICATION + SEALING (~82-90% / 2.9")                     |
| BLOCK H: MIL-A-8625 badge (left) + Sealing methods strip (right)        |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK I: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + not electroplating | 8% | 2.9" |
| 2 — Comparison | HERO three-type table | 37% | 13.3" |
| 3 — Concepts | Anode diagram + pore structure | 20% | 7.2" |
| 4 — Alloy + Pre-Treat | Compatibility + flow | 17% | 6.1" |
| 5 — Spec + Sealing | MIL-A-8625 + methods | 8% | 2.9" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`):**

> ANODIZING FUNDAMENTALS

**Subheading (Barlow SemiBold, 36 pt, `#E8A020`):**

> Type I, II, and III at a Glance

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> The part IS the anode. The coating grows from the aluminum itself.

---

### BLOCK B — "Not Electroplating" Callout (Header Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#2EC4B6`):**

> NOT ELECTROPLATING

**Body (Inter Regular, 16 pt, `#F0EDE8`):**

> In electroplating, the part is the cathode — metal deposits ON it from solution. In anodizing, the part is the anode — aluminum oxide grows FROM the surface. The coating IS the substrate, chemically converted.

**Reaction (JetBrains Mono Regular, 16 pt, `#F0EDE8`):**

> 2Al + 3H₂O → Al₂O₃ + 6H⁺ + 6e⁻

---

### BLOCK C — Three-Type Comparison Table (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):**

> THE THREE TYPES — MIL-A-8625

**Layout:** Three columns, each approximately 7.3" wide. Each column is a distinct accent color.

**Column structure:**

| Row | Type I (Amber) | Type II (Teal) | Type III (Coral) |
|-----|----------------|----------------|-------------------|
| **Type label** | `TYPE I` | `TYPE II` | `TYPE III` |
| **Name** | `CHROMIC ACID` | `SULFURIC ACID` | `HARD COAT` |
| **Electrolyte** | CrO₃, 3-10% | H₂SO₄, 15-20% | H₂SO₄, 10-12% |
| **Temperature** | 90-100 deg F | 68-72 deg F | 28-36 deg F |
| **Current density** | 5-10 ASF | 12-18 ASF | 24-36 ASF |
| **Voltage** | 0-40 V (ramped) | 15-21 V | 40-100+ V |
| **Thickness** | 0.05-0.15 mil | 0.2-1.0 mil | 1.0-4.0 mil |
| **Hardness** | Moderate | 300-400 HV | 500-700 HV |
| **Color** | Gray (undyed) | Clear; wide dye range | Dark bronze to black |
| **Dyeability** | Limited | Excellent | Limited (dark only) |
| **Fatigue impact** | Minimal (thin) | Moderate | Significant |
| **Environmental** | Cr⁶⁺ — restricted | No Cr⁶⁺ | No Cr⁶⁺ |
| **Primary use** | Aerospace fatigue-critical | Decorative / general | Wear / engineering |

**Column header construction:** Each column header is a large rounded rectangle with accent color fill (`#E8A020`, `#2EC4B6`, `#E05C5C`) containing the Type label and name in Barlow Condensed ExtraBold, 22 pt, `#1A1F2E` (dark text on accent fill).

Data rows: alternating `#1A1F2E` / `#252B3D`, text in Inter Regular 16 pt `#F0EDE8`, numerical data in JetBrains Mono 16 pt.

**Temperature callout (below Type III column, Inter Medium 14 pt, `#E05C5C`):**

> Near freezing — refrigeration required.

**Thickness callout (below table, Inter Medium 16 pt, `#F0EDE8`):**

> Dimensional growth: ~50% outward, ~50% inward. Net gain ≈ half of total oxide thickness.

---

### BLOCK D — "Part = Anode" Concept Diagram (Zone 3 — Left)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> HOW ANODIZING WORKS

**Illustration:** Simple circuit diagram.
- Rectifier block at top (rounded rectangle, `#252B3D`, labeled `DC RECTIFIER`)
- (+) terminal wire going down to the aluminum part (labeled `ANODE — The Part`)
- (-) terminal wire going down to a counter-electrode (labeled `CATHODE — Counter-electrode`)
- Electrolyte bath (tank, `#3A4055` outline, `#1E2435` fill) containing both
- Arrow from part surface: `Oxide grows FROM the aluminum surface` — Inter Medium, 14 pt, `#2EC4B6`
- Arrow at cathode: `H₂ gas evolves here` — Inter Regular, 12 pt, `#F0EDE8` at 70%

**Key contrast callout (below diagram):**

Inter Medium, 15 pt, `#E8A020`:
> Electroplating: part is cathode, metal deposits ON it.
> Anodizing: part is anode, oxide grows FROM it.

---

### BLOCK E — Pore Structure Cross-Section (Zone 3 — Right)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> THE PORE STRUCTURE

**Illustration:** Simplified cross-section showing the anodic oxide structure.

Build as stacked rectangles:
1. **Aluminum substrate** — bottom, `#3A4055` Mid Slate, 2" wide x 0.8" tall, labeled `ALUMINUM`
2. **Barrier layer** — thin rectangle on top of substrate, `#E8A020` Amber, 0.1" tall, labeled `Barrier layer (dense oxide)`
3. **Porous columnar structure** — 6-8 vertical narrow rectangles rising from the barrier layer, `#2EC4B6` Teal at 60% opacity, ~0.15" wide x 2" tall, spaced evenly with 0.15" gaps between them (representing the pore walls)
4. **Pore channels** — the gaps between columns (background shows through — `#1A1F2E`)
5. **Dye dots** — small colored circles (assorted colors: red, blue, black) placed inside the pore channels at mid-height, labeled `Dye trapped in pores`
6. **Sealed tops** — thin horizontal rectangle across the top of the columns, `#C8D0D8` Bright Silver, 0.1" tall, labeled `Sealed (hydrated oxide)`

**Caption (Inter Regular, 14 pt, `#F0EDE8`):**

> The hexagonal cell structure gives anodizing its unique properties: permanent dye absorption, corrosion resistance, and electrical insulation.

---

### BLOCK F — Alloy Compatibility Chart (Zone 4 — Left)

**Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):**

> ALLOY COMPATIBILITY

**Table (3 columns: Series | Example | Quality):**

| Alloy Series | Example | Anodizing Quality |
|--------------|---------|-------------------|
| 1xxx (pure Al) | 1100 | Excellent — clear, consistent |
| 5xxx (Al-Mg) | 5052 | Very good — clear to light gray |
| 6xxx (Al-Mg-Si) | 6061, 6063 | Very good — 6063 = best architectural |
| 2xxx (Al-Cu) | 2024 | Fair to poor — yellowish oxide |
| 7xxx (Al-Zn) | 7075 | Fair — color inconsistency |
| Cast alloys | A356, 380 | Variable — silicon causes dark/grainy |

Quality column: color-coded left-border accent — Emerald for Excellent/Very Good, Amber for Fair, Coral for Variable/Poor.

**Key note (Inter Medium, 14 pt, `#E8A020`):**

> Higher alloying elements (Cu, Si) = worse anodizing. Pure Al and 6xxx produce the best results.

---

### BLOCK G — Pre-Treatment Flow + Common Defects (Zone 4 — Right)

**Pre-treatment flow (compact horizontal strip):**

5 boxes: `CLEAN` → `ETCH` → `DESMUT` → `ANODIZE` → `DYE` → `SEAL`

Font: Barlow SemiBold 12 pt, `#F0EDE8`. Boxes: `#252B3D` fill, 1 pt `#3A4055` border. Arrows: 1 pt `#3A4055`.

Below: Inter Regular, 12 pt, `#F0EDE8` at 70%:
> Caustic etch: NaOH, 4-8 oz/gal, 140 deg F, 1-5 min
> Desmut: HNO₃ or HNO₃/HF, room temp, 15-60 sec

**Common defects (compact list):**

Title: `COMMON DEFECTS` — Barlow SemiBold, 16 pt, `#E05C5C`

| Defect | Cause |
|--------|-------|
| Uneven color | Inconsistent oxide; alloy variation |
| Chalky oxide | Temp too high; over-processed |
| Burning | High CD; poor contact |
| Poor dye absorption | Oxide too thin; over-sealed |
| Streaking | Poor cleaning; alloy segregation |

Font: Inter Regular, 13 pt, `#F0EDE8`.

---

### BLOCK H — MIL-A-8625 Badge + Sealing Methods (Zone 5)

**Left: Specification badge:**

Rounded rectangle, `#2EC4B6` border 2 pt, `#1E2435` fill, corner radius 8 pt

Text: `MIL-A-8625F` — Barlow Condensed ExtraBold, 24 pt, `#2EC4B6`
Sub: `The governing specification for anodic coatings on aluminum` — Inter Regular, 13 pt, `#F0EDE8`

**Right: Sealing methods strip:**

Title: `SEALING METHODS` — Barlow SemiBold, 16 pt, `#F0EDE8`

4 compact entries (JetBrains Mono 13 pt, `#F0EDE8`):
> Hot water: 200-212 deg F — standard
> Nickel acetate: 180-200 deg F — aerospace
> Cold seal (NiF): 75-85 deg F — energy savings
> PTFE: variable — lubricity for hard coat

---

### BLOCK I — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents anodizing fundamentals per MIL-A-8625F. Operating parameters vary by alloy, tank configuration, and product specification. Consult your process supplier for application-specific guidance.`

**Poster title:** `Anodizing Fundamentals: Type I, II, and III at a Glance`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The three-column comparison table uses accent colors as column header fills — verify text contrast after remap. Keep column header text as `#F0EDE8` (Warm White) in both editions since the darkened accent fills may have insufficient contrast with `#1A1F2E` text. Apply the Light edition override noted in Design Standards Section 3.

The pore structure illustration colors are structural, not decorative — remap normally. The dye dots inside pores are decorative/representative and should retain their original colors (they represent actual dye colors).

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Drew (OPEN):** Type II CD range, alloy compatibility, A Brite product names on poster.

**Tyler:** No validation required.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #9 — Anodizing Fundamentals — Content and Layout Draft v1.0*
*2026-04-04*
