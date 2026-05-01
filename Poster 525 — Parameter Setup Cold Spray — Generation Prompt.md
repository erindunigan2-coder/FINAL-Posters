---
Project: Plating Posters Inc
Poster Number: 525
Title: "Parameter Setup -- Cold Spray"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 525 — Parameter Setup Cold Spray — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ColdSpray
  - ThermalSpray
  - Parameters
  - ClusterTS05
  - v1
---

# Claude Chat Generation Prompt -- Poster #525
## Parameter Setup -- Cold Spray
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PARAMETER SETUP` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Cold Spray -- Achieving Critical Velocity` -- `36` pt `#E8A020`. Y: **1.5"**.
### Step 3 -- `Every parameter serves one goal: accelerate particles past the critical velocity threshold. Below it, they bounce. Above it, they bond.` -- `22` pt at 65%. Y: **2.2"**.

Rule card (right): Big number `Vc` 72pt `#E8A020`. Label: `critical velocity -- the threshold that defines bonding`.

---

## Phase 3 -- Parameter Table + Critical Velocity (HERO)

Y: 2.9" to 14.0". Section label: `OPERATING PARAMETERS -- HPCS VS. LPCS`.

**Dual Parameter Table (full width):**

12-row table. Columns: Parameter (4.5") | HPCS (5.5") | LPCS (5.5") | Notes (7.5").

| Parameter | HPCS | LPCS | Notes |
|---|---|---|---|
| Gas type | N2 or He | Air or N2 | He for hard metals only (cost) |
| Gas pressure | 20--60 bar | 5--10 bar | Primary velocity driver |
| Gas temperature | 300--1100 C | 200--600 C | Heats GAS, not particles |
| Particle velocity | 600--1200 m/s | 300--600 m/s | Must exceed critical velocity |
| Powder feed rate | 2--10 kg/hr | 1--5 kg/hr | Higher = faster buildup |
| Powder size | 5--50 um | 5--50 um | Finer = higher velocity |
| Standoff distance | 10--50 mm | 10--30 mm | VERY close vs. other TS |
| Spray angle | 75--90 deg | 75--90 deg | Perpendicular preferred |
| Traverse speed | 100--500 mm/s | 100--500 mm/s | Robot-controlled |
| Nozzle type | WC-Co or SiC | Polymer or steel | Wear-resistant for HPCS |
| Deposition efficiency | 50--95% | 30--70% | Material-dependent |
| Deposition rate | 1--8 kg/hr | 0.5--3 kg/hr | Lower than HVOF |

Header fill `#3A4055`. "Primary velocity driver" notes in `#E8A020`.

**Critical Velocity Concept (below table, Y: 11.0"--13.8"):**

Coral-accented glass card. Title: `THE CRITICAL VELOCITY THRESHOLD`.

Horizontal velocity gauge bar (W: 20.0"):
- Red zone left (0--400 m/s): `#E05C5C`, label `BOUNCE`
- Transition (400--600 m/s): gradient coral-to-amber
- Green zone right (600--1200 m/s): `#27AE60`, label `BOND`
- Critical velocity marker at ~500--600 m/s: `Vc (critical)` in `#E8A020`

Explanation: `Below Vc: particles rebound elastically -- no deposition. Above Vc: adiabatic shear instability breaks oxide films, creates metallurgical bond. Every CS parameter is tuned to exceed Vc for the specific feedstock.`

---

## Phase 4 -- Material Velocity Requirements

Y: 14.0" to 22.0". Section label: `CRITICAL VELOCITY BY MATERIAL`.

10-row table. Columns: Material (4.0") | Critical Velocity (4.0") | Typical Spray Velocity (4.5") | System (4.0") | DE (6.5").

| Material | Critical Velocity | Spray Velocity | System | DE |
|---|---|---|---|---|
| Copper (Cu) | 300--400 m/s | 500--800 m/s | HPCS (N2) or LPCS | 80--95% |
| Aluminum (Al) | 350--450 m/s | 500--900 m/s | HPCS (N2) or LPCS | 70--90% |
| Zinc (Zn) | 250--350 m/s | 400--600 m/s | LPCS adequate | 70--85% |
| Tin (Sn) | 200--300 m/s | 300--500 m/s | LPCS adequate | 75--90% |
| Nickel (Ni) | 500--600 m/s | 700--1000 m/s | HPCS (N2 or He) | 50--70% |
| Titanium (Ti-6Al-4V) | 600--750 m/s | 800--1200 m/s | HPCS (He preferred) | 50--70% |
| Stainless steel (316L) | 550--700 m/s | 700--1000 m/s | HPCS (N2 or He) | 40--60% |
| Silver (Ag) | 300--400 m/s | 500--700 m/s | HPCS (N2) or LPCS | 75--90% |
| Inconel 625 | 600--800 m/s | 800--1200 m/s | HPCS (He recommended) | 40--60% |
| Tantalum (Ta) | 600--800 m/s | 900--1200 m/s | HPCS (He required) | 30--50% |

Critical velocity in `#E05C5C`. Spray velocity in `#27AE60`. "He preferred/required" in `#E8A020`.

Callout: `Softer, more ductile metals have lower critical velocities -- easier to cold spray. Hard metals require HPCS with helium.` in `#2EC4B6`.

---

## Phase 5 -- Parameter Interactions + DE

Y: 22.0" to 32.5".

**Left -- Parameter Interactions (W: 11.0"):**

Section label: `PARAMETER INTERACTIONS`. Three primary levers:

| Lever | Increase Effect |
|---|---|
| GAS PRESSURE | Higher particle velocity; higher DE |
| GAS TEMPERATURE | Higher gas velocity (expansion); higher particle velocity |
| POWDER SIZE (smaller) | Higher velocity (less mass to accelerate) |

Three secondary effects:

| Factor | Effect |
|---|---|
| Standoff too close (< 10 mm) | Bow shock decelerates particles |
| Standoff too far (> 50 mm) | Particles decelerate in ambient air |
| Spray angle < 75 deg | Reduced normal velocity; porosity increases |

Warning: `Bow shock at very close standoff decelerates particles. Optimal: 15--30 mm for most HPCS.` in `#E8A020`.

**Right -- Deposition Efficiency Chart (W: 11.5"):**

Section label: `DEPOSITION EFFICIENCY`. Horizontal bar chart:

| Material | DE | Bar |
|---|---|---|
| Cu | 80--95% | `#27AE60` |
| Al | 70--90% | `#27AE60` |
| Zn, Sn, Ag | 70--90% | `#27AE60` |
| Ni | 50--70% | `#E8A020` |
| Ti | 50--70% | `#E8A020` |
| Steel | 40--60% | `#E8A020` |
| Inconel | 40--60% | `#E8A020` |
| Ta | 30--50% | `#E05C5C` |

**Verdict banner (Y: 30.5", full width, pill shape):**
`Copper is the benchmark cold spray material -- highest DE, lowest critical velocity, near-bulk properties.` in `#E8A020`.

---

## Phase 6 -- Footer

Standard. Title: `Parameter Setup -- Cold Spray`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Critical velocity values are approximate and depend on powder morphology, size distribution, and oxide content. Validate parameters for each material-substrate combination. Consult your equipment manufacturer and specification.`

---

## Phase 7 -- Review

- [ ] Headline `PARAMETER SETUP` 88pt
- [ ] Vc rule card
- [ ] 12-row HPCS vs. LPCS parameter table
- [ ] Critical velocity gauge (BOUNCE / BOND visual)
- [ ] 10-material critical velocity table
- [ ] Parameter interaction diagram (3 levers + 3 effects)
- [ ] DE horizontal bar chart (8 materials)
- [ ] Copper benchmark verdict banner
- [ ] Footer with disclaimer and version

---

## Phase 8 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Parameter Setup Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
