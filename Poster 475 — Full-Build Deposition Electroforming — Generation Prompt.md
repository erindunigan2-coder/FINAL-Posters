---
Project: Plating Posters Inc
Poster Number: 475
Title: "Full-Build Deposition -- Electroforming"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 475 — Full-Build Deposition Electroforming — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Electroforming
  - Deposition
  - FullBuild
  - FaradaysLaw
  - SpecialtyAdvanced
  - ClusterSA08
  - v1
---

# Claude Chat Generation Prompt -- Poster #475
## Full-Build Deposition -- Electroforming
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `FULL-BUILD DEPOSITION` -- `72` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Electroforming -- Building to Target Thickness at Production Current` -- `28` pt `#2EC4B6`. Y: **1.5"**.
### Step 3 -- `Electroforming is a marathon, not a sprint. A 5 mm nickel shell takes 83 hours at 5 A/dm2. Bath chemistry, stress, and patience are all required in equal measure.` -- `20` pt at 65%. Y: **2.1"**.

**Rule Card:** Big number `~12` in 60pt `#E8A020` | `um/hr AT 1 A/dm2` | `Nickel deposition rate (Faraday's law)`.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted. Deposition stage highlighted (Teal).

---

## Phase 4 -- Build Time Chart Hero

Y: 4.2" to 14.5". Section label: `BUILD TIME -- FARADAY'S LAW IN ACTION`.

**Left -- Chart:** X-axis: Time (hours) 0-120. Y-axis: Thickness (mm) 0-8. Three lines:

| Line | CD | Rate | Color |
|---|---|---|---|
| 1 | 1 A/dm2 | 12 um/hr | `#2EC4B6` |
| 2 | 3 A/dm2 | 36 um/hr | `#E8A020` |
| 3 | 5 A/dm2 | 60 um/hr | `#27AE60` |

Faraday's law: `Thickness (um) = (CD x t x M) / (n x F x rho x 10^-4)` -- for Ni: ~12 um/hr per A/dm2 at 97% efficiency.

**Right -- Build Time Reference Table:**

| Target | At 3 A/dm2 | At 5 A/dm2 |
|---|---|---|
| 100 um | ~3 hr | ~2 hr |
| 250 um | ~7 hr | ~4 hr |
| 500 um | ~14 hr | ~8 hr |
| 1 mm | ~28 hr | ~17 hr |
| 2 mm | ~56 hr (2.3 days) | ~33 hr (1.4 days) |
| 5 mm | ~139 hr (5.8 days) | ~83 hr (3.5 days) |
| 10 mm | ~278 hr (11.6 days) | ~167 hr (7 days) |

**Bottom insight:** `Higher CD = faster build, but also higher stress, rougher deposit, and more risk of burning. Most Ni sulfamate EF runs at 3-5 A/dm2 as best compromise.`

---

## Phase 5 -- Parameters + Stress Control

Y: 14.5" to 22.0". Two-column layout.

**Left -- Ni SULFAMATE PARAMETERS:**

| Parameter | Range | Optimal |
|---|---|---|
| Current density | 1-10 A/dm2 | 3-5 A/dm2 |
| Temperature | 40-55 C | 50-54 C |
| pH | 3.5-4.5 | 3.8-4.2 |
| Ni(NH2SO3)2 | 300-450 g/L | 400 g/L |
| NiCl2 | 5-30 g/L | 15 g/L |
| H3BO3 | 30-45 g/L | 40 g/L |
| Saccharin | 0.5-3 g/L | Per Hull cell |
| Wetting agent | 0.01-0.05 g/L | Per Hull cell |
| Cathode efficiency | 95-99% | ~97% |
| Deposit hardness | 150-250 HV | Application-dependent |

**Right -- INTERNAL STRESS CONTROL (`#E05C5C`):**

```
TARGET: < 35 MPa tensile. IDEAL: Near-zero or compressive.

High stress = cracking, curling, distortion, mechanical failure.

TOOLS:
1. SACCHARIN -- 0.5-3 g/L; reduces tensile; too much = brittle
2. TEMPERATURE -- 50-55 C = lower stress; < 45 C stress increases sharply
3. CURRENT DENSITY -- higher CD = higher stress; keep 3-5 A/dm2
4. BATH PURITY -- organics increase stress; carbon treat every 2-4 weeks
5. PULSE PLATING -- on/off pulsing reduces average stress; 8 ms on / 2 ms off
```

---

## Phase 6 -- Bath Maintenance + Inspection + Problems

Y: 22.0" to 32.5".

**Bath Maintenance Schedule (Y: 22.0" to 28.5"):**

| Frequency | Action |
|---|---|
| Every shift (8-12 hr) | Check temp, pH; record amp-hours |
| Daily | Ni conc (SG or titration); adjust pH; replenish wetting agent |
| Every 48-72 hr | Hull cell test (2 A, 10 min); check stress, pitting |
| Weekly | Full analysis; boric acid; evaluate filtration |
| As needed | Carbon treatment; dummy plate 0.2-0.5 A/dm2 overnight |
| Anode maintenance | Check Ni round fill; replace anode bags |

**Thickness Check Protocol (`#E8A020`):**
1. Calculate expected from amp-hours (Faraday's law). 2. Measure with micrometer (mandrel + deposit, subtract mandrel). 3. Compare calculated vs. measured. 4. Inspect for roughness, burning, pitting, edge buildup. 5. Adjust shields, CD, carbon treat as needed. For runs > 5 days: consider midpoint removal for full measurement.

**Build Problems (Y: 28.5" to 32.5"):** Four cards.

| Problem | Cause | Fix |
|---|---|---|
| HIGH STRESS / CRACKING | Contamination; saccharin depleted; CD high | Carbon treat; replenish saccharin; reduce CD |
| PITTING | Low wetting agent; pH < 3.5; H2 | Add wetting agent; adjust pH; increase agitation |
| BURNING (ROUGH/DARK) | CD too high for Ni conc; temp low | Reduce CD or increase Ni; raise temp 50-54 C |
| ROUGH DEPOSIT (NODULES) | Particulate; anode sludge | Check filtration; replace anode bags; carbon treat |

---

## Phase 7 -- Footer

Standard. Title: `Full-Build Deposition -- Electroforming`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B832; ASM Handbook Vol. 5. Saccharin dosing must be verified by Hull cell testing -- do not dose by calculation alone.`

---

## Phase 8 -- Review

- [ ] Headline `FULL-BUILD DEPOSITION` 72pt
- [ ] Rule card with `~12 um/hr` big number
- [ ] Build time chart with three CD lines
- [ ] Build time reference table
- [ ] Ni sulfamate parameter table
- [ ] Stress control panel with five tools
- [ ] Bath maintenance schedule
- [ ] Orientation strip with poster 7 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Full-Build Deposition Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
