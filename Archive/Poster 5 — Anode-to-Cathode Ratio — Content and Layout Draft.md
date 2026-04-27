---
Project: Plating Posters Inc
Poster Number: 5
Title: "Anode-to-Cathode Ratio: Why It Matters More Than You Think"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Anode-to-Cathode Ratio Research Brief v1 (2026-04-03)
Watson Flags: TWO — A:C ratio ranges by process + zinc anode note (both Drew confirmation, non-blocking)
Process Scope: Universal concept — applies across all electrolytic plating processes
Editions: Dark + Light
tags:
  - PosterDesign
  - AnodeCathodeRatio
  - ContentDraft
---

# Poster #5 — Content and Layout Draft
## Anode-to-Cathode Ratio: Why It Matters More Than You Think

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Anode-to-Cathode Ratio Research Brief v1. This poster visualizes one of the most overlooked process variables in plating — the ratio that controls current distribution, anode dissolution, and bath chemistry balance.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: TWO FLAGS — both Drew confirmation, non-blocking.**

**Flag 1 (Drew):** Confirm ideal A:C ratio ranges for each process, particularly acid chloride zinc (1:1 to 1.5:1 — high KCl may exacerbate zinc buildup at high A:C).

**Flag 2 (Drew):** Confirm zinc anode note from Quick Reference — "zinc slabs better than zinc balls in Ti baskets" applies to zinc-nickel alloy specifically, not plain zinc. Include on poster?

**Design decisions:**

- **Layout: HERO triple-tank comparison + data table.** The poster's centerpiece is three side-by-side tank cross-sections showing under-anoded, correct, and over-anoded conditions. This is the visual Watson identified as highest impact and I agree — it is the kind of diagram that does not exist anywhere in current industry publications. Below: the process-specific A:C ratio table and a worked calculation example.

- **Color coding for the HERO:** Under-anoded = Coral (problem). Correct = Emerald (good). Over-anoded = Amber (caution, not catastrophic). This maps to the established series color semantics.

- **This poster is about understanding, not fear.** Over-anoded is less dangerous than under-anoded. The poster should communicate this clearly — the visual shows that under-anoded conditions are the critical failure mode, while slight over-anoding is generally tolerable.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "The Definition" callout box (right ~45%)                      |
+------------------------------------------------------------------------+
| ZONE 2 — TRIPLE TANK COMPARISON (HERO) (~8-38% / 10.8")               |
| BLOCK C: Three side-by-side tank cross-sections                         |
| Under-Anoded (Coral) | Correct (Emerald) | Over-Anoded (Amber)          |
+------------------------------------------------------------------------+
| ZONE 3 — A:C RATIO TABLE (~38-62% / 8.6")                             |
| BLOCK D: Process-specific ideal ratio table + anode types                |
+------------------------------------------------------------------------+
| ZONE 4 — SYMPTOMS + CALCULATION (~62-80% / 6.5")                      |
| BLOCK E: "What Goes Wrong" two-column (left 55%)                        |
| BLOCK F: Calculation example + fist rule (right 45%)                     |
+------------------------------------------------------------------------+
| ZONE 5 — ANODE MAINTENANCE + PASSIVATION (~80-90% / 3.6")             |
| BLOCK G: Maintenance checklist (left 50%)                                |
| BLOCK H: Passivation warning callout (right 50%)                        |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK I: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + definition | 8% | 2.9" |
| 2 — Tank Comparison | HERO triple illustration | 30% | 10.8" |
| 3 — Ratio Table | Process-specific data | 24% | 8.6" |
| 4 — Symptoms + Calc | Two-column split | 18% | 6.5" |
| 5 — Maintenance | Checklist + passivation | 10% | 3.6" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`):**

> ANODE-TO-CATHODE RATIO

**Subheading (Barlow SemiBold, 36 pt, `#E8A020`):**

> Why It Matters More Than You Think

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> The ratio that controls your current, your anodes, and your bath chemistry.

---

### BLOCK B — "The Definition" Callout Box (Header Right)

**Callout box:** fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#2EC4B6`):**

> THE DEFINITION

**Formula (JetBrains Mono Regular, 22 pt, `#F0EDE8`, centered):**

> A:C = Anode Area / Cathode Area

**Examples (JetBrains Mono Regular, 15 pt, `#F0EDE8` at 80%):**

> 1:1 — anode equals cathode
> 2:1 — anode is 2x cathode
> 0.5:1 — anode is half cathode (under-anoded)

**Target line (Inter Medium, 16 pt, `#2EC4B6`):**

> Most processes: target 1:1 to 2:1.

---

### BLOCK C — Triple Tank Comparison (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 30 pt, `#F0EDE8`, centered):**

> WHAT HAPPENS WHEN THE RATIO IS WRONG

**Layout:** Three tank cross-sections side by side, each approximately 7.3" wide, separated by 0.2" gutters. Each tank is approximately 7.3" wide x 7.5" tall.

**General tank construction (identical structure, content varies):**
- Tank body: rounded rectangle, `#3A4055` stroke 2 pt, `#1E2435` fill
- Electrolyte suggestion: horizontal wavy line treatment at 20% opacity in `#2EC4B6`
- Anode: vertical rectangle, accent-colored outline, inside tank left side
- Cathode (part): vertical rectangle, `#C8D0D8` Bright Silver fill, inside tank right side
- Current flow lines: curved lines from anode to cathode representing current distribution

**Tank 1 — Under-Anoded (Coral `#E05C5C` accent):**
- Position: X: 0.5" (first column)
- Tank label above: `UNDER-ANODED` — Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Ratio label: `A:C = 0.5:1` — JetBrains Mono, 16 pt, `#E05C5C`
- Anode: SMALL rectangle (~0.8" wide x 3.5" tall), `#E05C5C` outline 2 pt
- Cathode (part): normal size (~1.2" wide x 5" tall)
- Current lines: CROWDED at the top edges of the cathode, sparse at the bottom/recesses — lines bunch together near HCD zones, thin out at LCD zones
  - Line style: 1 pt, `#E05C5C`, various curvature
- Deposit on cathode: UNEVEN — thick at top edges (heavy `#C8D0D8` rectangle), thin or absent in middle/bottom
- Call-out labels (JetBrains Mono, 12 pt):
  - `BURNING` — arrow to thick edge deposit, `#E05C5C`
  - `THIN / SKIP` — arrow to bare recess area, `#E05C5C`

Sub-label below tank (Inter Regular, 14 pt, `#F0EDE8`):
> Current crowds at the nearest cathode surfaces. Edges burn. Recesses starve.

**Tank 2 — Correct Ratio (Emerald `#27AE60` accent):**
- Position: X: 8.0" (center column)
- Tank label: `CORRECT RATIO` — `#27AE60`
- Ratio label: `A:C = 1.5:1` — `#27AE60`
- Anode: proper size (~1.5" wide x 5" tall), `#27AE60` outline
- Cathode: same as Tank 1
- Current lines: EVENLY DISTRIBUTED — parallel, consistent spacing from anode to cathode
  - Line style: 1 pt, `#27AE60`
- Deposit: UNIFORM thickness across the cathode face (~0.2" consistent)

Sub-label:
> Current distributes evenly. Uniform deposit. Bath stays balanced.

**Tank 3 — Over-Anoded (Amber `#E8A020` accent):**
- Position: X: 15.5" (right column)
- Tank label: `OVER-ANODED` — `#E8A020`
- Ratio label: `A:C = 3:1` — `#E8A020`
- Anode: LARGE rectangle (~2.5" wide x 5.5" tall), `#E8A020` outline
- Cathode: same as Tank 1
- Current lines: mostly even, with slight excess dissolution arrows from anode surface
  - Line style: 1 pt, `#E8A020`
- Deposit: reasonably uniform
- Dissolution arrows: extra small arrows from anode surface into solution, `#E8A020`, labeled `Excess dissolution`

Sub-label:
> Generally acceptable. Excess anode area may over-dissolve, raising metal concentration.

**Key insight banner (below all three tanks, centered):**
- Inter Medium, 18 pt, `#F0EDE8`
- Text: `Under-anoded is the critical failure. Over-anoded is usually tolerable.`

---

### BLOCK D — Process-Specific A:C Ratio Table (Zone 3)

**Section label (Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`):**

> IDEAL A:C RATIOS BY PROCESS

**Table structure — 4 columns:**
1. **Process** (~30%) — Inter Medium, 17 pt
2. **Ideal A:C** (~15%) — JetBrains Mono, 17 pt, `#2EC4B6` Teal
3. **Anode Type** (~25%) — Inter Regular, 16 pt
4. **Notes** (~30%) — Inter Regular, 15 pt

Column header row: `#3A4055` fill.

Data rows (alternating `#1A1F2E` / `#252B3D`):

| Process | Ideal A:C | Anode Type | Notes |
|---------|-----------|------------|-------|
| Acid copper sulfate | 1:1 to 2:1 | Cu-P (phosphorized) | Cu-P film regulates dissolution |
| Cyanide copper | 1:1 to 1.5:1 | OFHC copper | Higher A:C increases CN⁻ consumption |
| Watts nickel (bright) | 1:1 to 2:1 | Ni R-Rounds (Ti baskets) | Bag anodes to contain sludge |
| Nickel sulfamate | 1:1 to 2:1 | Ni S-Rounds (Ti baskets) | Higher A:C preferred — uniform dissolution |
| Acid chloride zinc | 1:1 to 1.5:1 | Zinc slabs/balls | High KCl increases dissolution rate |
| Alkaline NC zinc | 1:1 to 2:1 | Steel plates (insoluble) | Current distribution only — add ZnO |
| Alkaline cyanide zinc | 1:1 to 2:1 | Zinc balls (steel baskets) | Lower A:C may be preferred |
| Decorative chrome (hex) | 1:1 to 3:1 | Lead-tin (7% Sn) | A:C affects covering power |
| Hard chrome | 1:1 to 3:1 | Lead-tin or Pb-Sb | Conforming anodes → 1:1 at all points |
| Silver cyanide | 1:1 to 2:1 | High-purity Ag (>99.9%) | Maintain anode area >= cathode area |
| Matte tin | 1:1 to 1.5:1 | Pure tin (Zr baskets) | Ti baskets would passivate |

---

### BLOCK E — "What Goes Wrong" (Zone 4 — Left)

**Section label (Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`):**

> SYMPTOMS OF INCORRECT RATIO

**Two stacked callout boxes:**

**Under-Anoded (Coral `#E05C5C`):**

Callout box: fill `#1E2435`, left border 4 pt `#E05C5C`, corner radius 6 pt

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> UNDER-ANODED (A:C TOO LOW)

Bullet list (Inter Regular, 15 pt, `#F0EDE8`):
> - Burning at edges and HCD zones
> - Poor throwing power — thin LCD coverage
> - Rising bath voltage
> - Metal concentration dropping
> - Anode passivation risk

**Over-Anoded (Amber `#E8A020`):**

Callout box: fill `#1E2435`, left border 4 pt `#E8A020`, corner radius 6 pt

Title (Barlow SemiBold, 18 pt, `#E8A020`):
> OVER-ANODED (A:C TOO HIGH)

Bullet list (Inter Regular, 15 pt, `#F0EDE8`):
> - Rising metal concentration (some processes)
> - Sludge formation (nickel)
> - Wasted anode material
> - Generally less problematic than under-anoded

---

### BLOCK F — Worked Calculation + Fist Rule (Zone 4 — Right)

**Calculation Example:**

Callout box: fill `#1E2435`, border `#2EC4B6` Teal 1.5 pt, corner radius 8 pt

Title (Barlow SemiBold, 18 pt, `#2EC4B6`):
> QUICK CALCULATION

Calculation (JetBrains Mono Regular, 13 pt, `#F0EDE8`, line height 160%):
> 20 cylinders, 2" dia x 6" long
> Each: pi x 2 x 6 = 37.7 in² = 0.262 ft²
> Total cathode: 20 x 0.262 = 5.24 ft²
>
> 2 anode baskets, 6" x 24" x 2 sides
> Each: 288 in² / 144 = 2.0 ft²
> Total anode: 2 x 2.0 = 4.0 ft²
>
> A:C = 4.0 / 5.24 = 0.76:1

Answer (Inter Medium, 15 pt, `#E05C5C`):
> Under-anoded! Add a third basket.

---

**Fist Rule Callout:**

Small callout box: fill `#1E2435`, no border, corner radius 6 pt

Barlow SemiBold, 16 pt, `#E8A020`:
> THE FIST RULE

JetBrains Mono Regular, 18 pt, `#F0EDE8`:
> 1 clenched fist ≈ 0.33 ft²

Inter Regular, 13 pt, `#F0EDE8` at 70%:
> A quick estimation method for cathode surface area — from Drew's field notes.

---

### BLOCK G — Anode Maintenance Checklist (Zone 5 — Left)

Callout box: fill `#1E2435`, border `#27AE60` Emerald 1.5 pt, corner radius 8 pt

Title (Barlow SemiBold, 18 pt, `#27AE60`):
> ANODE MAINTENANCE

Bullet list (Inter Regular, 15 pt, `#F0EDE8`):
> - Bag all soluble anodes — contain sludge
> - Replace consumed anodes before they get too small
> - Clean anode contacts — corrosion = resistance
> - Verify anode composition — wrong alloy = wrong dissolution
> - Submerge anodes to proper depth — exposed surface = uneven current
> - Inspect anode bags — holes defeat the purpose

---

### BLOCK H — Anode Passivation Warning (Zone 5 — Right)

Callout box: fill `#1E2435`, border `#E05C5C` Coral 2 pt, corner radius 8 pt

Title (Barlow SemiBold, 18 pt, `#E05C5C`):
> ANODE PASSIVATION

Body (Inter Regular, 15 pt, `#F0EDE8`):
> When anode current density gets too high, a dense oxide film forms on the anode surface and stops dissolution entirely.

Symptoms (Inter Medium, 14 pt, `#E05C5C`):
> Voltage rises sharply | Metal drops | Current distribution degrades

Fix (Inter Medium, 14 pt, `#27AE60`):
> Increase anode area. Verify anode composition. Check chloride level.

---

### BLOCK I — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents general anode-to-cathode ratio guidelines. Specific ratios depend on tank geometry, anode type, and product formulation. Consult your process supplier for application-specific recommendations.`

**Poster title:** `Anode-to-Cathode Ratio: Why It Matters More Than You Think`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The triple tank comparison uses Coral, Emerald, and Amber as outline/accent colors — these remap to their darkened Light edition equivalents. Current flow lines will appear darker on the light background, which actually improves visibility. No overrides anticipated.

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Drew (OPEN):** Confirm A:C ratio ranges by process. Confirm zinc anode note (Ti basket passivation) — does it belong on this poster?

**Tyler:** No validation required.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #5 — Anode-to-Cathode Ratio — Content and Layout Draft v1.0*
*2026-04-04*
