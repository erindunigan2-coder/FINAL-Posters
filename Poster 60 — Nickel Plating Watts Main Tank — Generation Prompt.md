---
Project: Plating Posters Inc
Poster Number: 60
Title: "Nickel Plating (Watts) -- Main Tank"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 60 -- Nickel Plating Watts Main Tank -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - NickelPlating
  - Watts
  - MainTank
  - Series2
  - ClusterEP03
  - v1
---

# Claude Chat Generation Prompt -- Poster #60
## Nickel Plating (Watts) -- Main Tank
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone.

---

## Phase 2 -- Header

### Step 1 -- `NICKEL PLATING` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Watts Bath -- Main Tank -- Stage 5 of 8` -- `32` pt `#27AE60`. Y: **1.4"**.
### Step 3 -- `Where the nickel goes on. pH is the master variable. Control the pH and everything else follows.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

**Stage 5 highlighted** (fill `#27AE60`). Below: `Before: Clean, activated substrate --> After: Nickel-plated surface ready for chrome, gold, or topcoat`

---

## Phase 4 -- Plating Tank Hero

Y: 4.2" to 14.5". Section: `THE WATTS NICKEL PLATING TANK`.

### Step 5 -- Tank cross-section (Y: 5.0" to 14.0")

**Tank body:** Rounded rect X: 1.5", W: 21.0", H: 7.5", fill `#252B3D`, border 3pt `#C8D0D8`.

**Anodes (both sides):** Vertical rects, W: 1.0", H: 5.5", fill `#C8D0D8`. Label: `Ni ANODES (S-ROUNDS)` -- `99.9%+ Ni in Ti baskets, double-bagged`.

**Cathode (center):** Vertical rect, W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2pt `#27AE60`. Label: `CATHODE (WORKPIECE)`.

**Current flow lines:** 6--8 curved dashed arrows (2pt `#E8A020`) from anodes to cathode. Label: `Current flow (Ni2+ migration)`.

**Rectifier symbol (above tank):** Small rect, fill `#1E2435`, border `#E8A020`. Text: `DC RECTIFIER`. (+) to anodes, (-) to cathode.

**Bath parameter labels inside tank:**

Right side:
- `NiSO4: 270--330 g/L (36--44 oz/gal)` `#27AE60`
- `NiCl2: 37--55 g/L (5--7 oz/gal)` `#2EC4B6`
- `H3BO3: 37--45 g/L (5--6 oz/gal)` `#E8A020`
- `Ni metal: 60--90 g/L total`

Left side:
- `pH: 3.8--4.2` 16pt `#27AE60` (prominent)
- `Temp: 130--150 F (54--66 C)`
- `CD: 30--50 ASF (rack)` `#E8A020`
- `CD: 8--15 ASF (barrel)` at 70%
- `Cathode eff: 92--98%` at 70%
- `A:C ratio: 1:1 to 2:1` at 70%

Bottom callout: `Heated bath (130--150 F). Below 115 F: poor brightness, high stress. Above 160 F: brightener destruction, soft deposit.` `#E8A020`

---

## Phase 5 -- Bath Composition + pH Control

Y: 14.5" to 20.5". Section: `BATH CHEMISTRY -- THE THREE ESSENTIALS`.

### Step 6 -- Three-component breakdown (Y: 15.3" to 18.5")

Three side-by-side callout boxes (each H: 3.0", fill `#1E2435`):

**NICKEL SULFATE** (accent `#27AE60`):
- `270--330 g/L (36--44 oz/gal)`
- Source: NiSO4 * 6H2O (~22% Ni by weight)
- Role: Primary Ni2+ source
- Low: thin deposit, poor coverage | High: no significant penalty

**NICKEL CHLORIDE** (accent `#2EC4B6`):
- `37--55 g/L (5--7 oz/gal)`
- Source: NiCl2 * 6H2O (~25% Ni by weight)
- Role: Anode depolarization + conductivity
- Low: anode passivation, metal depletion, pH rise, voltage spike | High: increased internal stress

**BORIC ACID** (accent `#E8A020`):
- `37--45 g/L (5--6 oz/gal)`
- Source: H3BO3
- Role: Cathode film pH buffer (prevents Ni(OH)2 co-deposition)
- Low: pitting, burning, poor LCD | High: precipitation risk below operating temp
- Solubility: 39 g/L at 68 F, 54 g/L at 140 F. Maintain near saturation.

### Step 7 -- pH control gauge (Y: 18.8" to 20.3")

Full-width, fill `#1E2435`. Title: `THE MASTER VARIABLE -- Bath pH`.

Horizontal bar gauge:
- `< 3.5` `#E05C5C`: low efficiency, brittle, poor LCD
- `3.8--4.2` `#27AE60`: OPTIMAL
- `> 4.5` `#E05C5C`: dark deposit, Ni(OH)2, stress, peeling

Optimal marker: triangle at 4.0 `#27AE60`.

---

## Phase 6 -- Defect Diagnosis Grid

Y: 20.5" to 26.5". Section: `WHAT GOES WRONG -- 6 COMMON DEFECTS`.

3x2 grid. Each card: W: 7.33", H: 2.3", fill `#1E2435`, left accent in defect color.

| Defect | Color | Cause | Fix |
|---|---|---|---|
| PITTING | `#E05C5C` | Low wetting agent, oil contamination, poor agitation | Add anti-pit; carbon treat; improve filtration |
| BURNING (HCD) | `#E8A020` | CD too high, low metal, high pH, low H3BO3 | Reduce CD; add NiSO4; check boric acid |
| DULL / MILKY | `#2EC4B6` | Organic contamination, metallic impurities | Carbon treat; low-pH dummy (pH 3.0, 2--5 ASF) |
| PEELING | `#E05C5C` | Poor cleaning, inadequate activation, no strike on stainless | Improve clean; check water-break test |
| DARK LCD | `#E8A020` | Cu, Cr contamination; high pH; low brightener | Dummy plate; adjust pH; Hull cell check |
| HIGH STRESS / CRACKING | `#2EC4B6` | Low primary brightener, excess secondary, organic breakdown | Adjust brightener balance; carbon treat |

---

## Phase 7 -- Hull Cell Strip + Contamination

Y: 26.5" to 32.5". Two-column layout.

**Left -- Hull Cell (X: 0.5", W: 11.0"):**
Title: `THE HULL CELL`. Test conditions: `267 mL | 2 A | 10 min | 140 F`.

5-segment strip:
- HCD edge `#E8A020` at 40%: `Burned = high CD or low H3BO3`
- Upper mid `#27AE60` at 50%: `Bright + level = good brightener balance`
- Center `#27AE60` at 70% OPTIMAL: `Full brightness = balanced bath`
- Lower mid `#27AE60` at 40%: `Semi-bright = acceptable; check primary brightener`
- LCD edge `#3A4055` at 60%: `Dull/dark = metallic contamination or low brightener`

Note: `Good Watts panel: bright across 70--80% of width. LCD slightly dull is acceptable.` `#27AE60`

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**
Title: `CONTAMINATION THRESHOLDS`.

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 5 ppm | Dark/black LCD, tree growths at HCD |
| Zinc | > 10 ppm | Dull, streaky deposits, peeling |
| Iron | > 25 ppm | Roughness, dark LCD, co-deposited iron |
| Chromium (Cr6+) | > 1 ppm | Skip plating, then dark at all CDs |
| Lead | > 1 ppm | Dark streaks, embrittlement |
| Organic (decomposed) | Variable | Pitting, haze, brittleness, peeling |

Thresholds in `#E05C5C`.

Remediation: `Low-pH dummying (pH 3.0, 2--5 ASF, 4--8 hr) removes Cu, Zn, metals. Carbon treatment (2--5 g/L, stir 2--4 hr, filter through pre-coat) removes organics. H2O2 (0.5--1 mL/L of 30%) oxidizes Fe2+ for filtration.` `#2EC4B6`

---

## Phase 8 -- Footer

Standard. Title: `Nickel Plating (Watts) -- Main Tank`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Modern Electroplating; ASM Handbook Vol. 5; Nickel Institute publications.`

---

## Phase 9 -- Review

- [ ] Headline `NICKEL PLATING` 80pt
- [ ] Stage 5 highlighted (Emerald)
- [ ] Plating tank cross-section with anodes, cathode, current flow, rectifier
- [ ] Bath parameters labeled inside tank (NiSO4, NiCl2, H3BO3, pH, temp, CD)
- [ ] Three-component breakdown boxes (sulfate, chloride, boric acid)
- [ ] pH control gauge with optimal marker
- [ ] 6-defect diagnosis grid (3x2)
- [ ] Hull cell strip (5 segments)
- [ ] Contamination thresholds table (6 rows)
- [ ] Footer with source references

---

## Phase 10 -- Light Remap & Export

Standard remap. Tank body and current flow lines: verify contrast on light background.

Six files: `Nickel Watts Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
