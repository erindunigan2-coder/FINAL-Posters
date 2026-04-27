---
Project: Plating Posters Inc
Poster Number: 455
Title: "Parameter Setup -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.5)"
Process Scope: Implantation parameter selection -- energy, dose, species, tilt, and scan pattern
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - ParameterSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #455 -- Construction Workup
## Parameter Setup -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the recipe -- the specific combination of ion species, energy, dose, tilt angle, and scan pattern that defines an implantation run. The hero visual shows the relationship between energy and depth (higher energy = deeper implant) and between dose and concentration (higher dose = more implanted atoms). A semiconductor recipe table and an industrial recipe table provide concrete examples. The parameter interaction matrix shows how changing one parameter affects others.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Energy-depth / dose-concentration hero (Block B):** Two conceptual relationships showing how the key parameters control the implant profile.
2. **Semiconductor recipe examples (Block D):** Common implant recipes for transistor fabrication.
3. **Industrial recipe examples (Block E):** N+ and C+ implant recipes for steel and titanium.
4. **Parameter interaction matrix (Block F):** How parameters affect each other.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ENERGY-DEPTH & DOSE-CONCENTRATION HERO (2.9"--14.5" / ~11.6")
  Block B: Two parameter relationship panels
ZONE 3 -- SEMICONDUCTOR RECIPES (14.5"--20.5" / ~6.0")
  Block D: Example implant recipes for common doping steps
ZONE 4 -- INDUSTRIAL RECIPES (20.5"--26.5" / ~6.0")
  Block E: N+, C+, B+ recipes for metals
ZONE 5 -- PARAMETER INTERACTION MATRIX (26.5"--32.5" / ~6.0")
  Block F: How changing one parameter affects others
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Energy, Dose, Species & Scan Configuration` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Energy controls depth. Dose controls concentration. Species controls what you are putting in there. Get all three right, and you have precision surface modification at the atomic level.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Energy-Depth & Dose-Concentration Hero

**Section label:** `THE TWO FUNDAMENTAL RELATIONSHIPS` -- Y: 3.1".

**BLOCK B -- Two Parameter Panels**

Y: 3.8" to 14.3". Two side-by-side panels.

**Left Panel -- Energy vs. Depth (X: 0.5", W: 11.0"):**
- Rounded rect, H: 10.0", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `ENERGY CONTROLS DEPTH` -- Barlow SemiBold, 22 pt, `#E8A020`. Y: 4.2".

Conceptual depth profile visualization (Y: 5.0" to 9.5"):
- Vertical axis: `DEPTH INTO SUBSTRATE` Inter Medium 11 pt `#F0EDE8`
- Three overlapping bell-curve-style concentration profiles at different depths:
  - Low energy (10 keV): shallow peak, fill `#2EC4B6` at 20%, label `10 keV -- shallow`
  - Medium energy (100 keV): medium peak, fill `#E8A020` at 20%, label `100 keV -- medium`
  - High energy (500 keV): deep peak, fill `#E05C5C` at 20%, label `500 keV -- deep`

Each profile: Rounded rect approximation of a Gaussian, positioned at increasing depth.

Key data table (Y: 10.0" to 14.0"):

| Species | Energy | Rp in Steel | Rp in Silicon |
|---|---|---|---|
| N+ | 50 keV | ~40 nm | ~90 nm |
| N+ | 100 keV | ~70 nm | ~170 nm |
| N+ | 200 keV | ~120 nm | ~320 nm |
| C+ | 50 keV | ~50 nm | ~130 nm |
| B+ | 50 keV | ~80 nm | ~170 nm |
| As+ | 100 keV | ~25 nm | ~50 nm |

Data: JetBrains Mono 11 pt `#F0EDE8`. Energy: `#E8A020`.

**Right Panel -- Dose vs. Concentration (X: 12.0", W: 11.5"):**
- Rounded rect, H: 10.0", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `DOSE CONTROLS CONCENTRATION` -- Barlow SemiBold, 22 pt, `#27AE60`. Y: 4.2".

Conceptual concentration visualization (Y: 5.0" to 9.5"):
- Three bars of increasing intensity at the same depth:
  - Low dose (10^14 ions/cm2): faint fill `#27AE60` at 10%, label `10^14 -- trace modification`
  - Medium dose (10^16 ions/cm2): medium fill `#27AE60` at 30%, label `10^16 -- significant`
  - High dose (10^18 ions/cm2): strong fill `#27AE60` at 60%, label `10^18 -- saturation`

Key data table (Y: 10.0" to 14.0"):

| Dose (ions/cm2) | Peak Concentration (approx.) | Effect on Steel (N+) | Effect on Si (B+) |
|---|---|---|---|
| 10^14 | < 0.01 at% | Minimal surface change | Low doping (threshold adjust) |
| 10^15 | ~0.1 at% | Measurable hardness increase | Source/drain extension |
| 10^16 | ~1 at% | Significant wear improvement | Heavy doping (source/drain) |
| 10^17 | ~10 at% | Maximum hardness; near-surface alloy | Amorphization dose for Si |
| 10^18 | Saturation | Sputtering competes with implantation | Research only |

Data: JetBrains Mono 11 pt `#F0EDE8`. Dose: `#27AE60`.

---

### ZONE 3 -- Semiconductor Recipes

**Section label:** `SEMICONDUCTOR IMPLANT RECIPES -- COMMON EXAMPLES` -- Y: 14.7".

**BLOCK D -- Recipe Table**

Y: 15.3" to 20.3".

| Implant Step | Species | Energy (keV) | Dose (ions/cm2) | Tilt (deg) | Purpose |
|---|---|---|---|---|---|
| Threshold adjust | B+ | 10--30 | 10^12--10^13 | 7 | Set transistor turn-on voltage |
| Source/drain extension | As+ or BF2+ | 2--10 | 10^14--10^15 | 0--7 | Shallow junction formation |
| Source/drain | As+ (n) or B+ (p) | 20--80 | 10^15--10^16 | 7 | Heavy doping for low-resistance contacts |
| Deep n-well | P+ | 500--2000 | 10^13 | 7 | Form n-type well deep in substrate |
| Deep p-well | B+ | 200--1000 | 10^13 | 7 | Form p-type well |
| Anti-punchthrough | B+ or As+ | 50--150 | 10^12--10^13 | 7 | Prevent current leakage between source and drain |
| Channel stop | B+ | 100--200 | 10^13 | 7 | Prevent parasitic transistor formation |
| Pre-amorphization | Si+ or Ge+ | 10--30 | 10^14--10^15 | 0 | Amorphize surface for subsequent shallow implant |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 4 -- Industrial Recipes

**Section label:** `INDUSTRIAL IMPLANT RECIPES` -- Y: 20.7".

**BLOCK E -- Industrial Recipe Table**

Y: 21.3" to 26.3".

| Application | Substrate | Species | Energy (keV) | Dose (ions/cm2) | Expected Improvement |
|---|---|---|---|---|---|
| Tool steel hardening | M2, D2 HSS | N+ | 50--150 | 10^17 | Surface hardness +50--100%; wear life 2x--5x |
| Medical implant (hip) | Ti-6Al-4V | N+ | 50--100 | 5x10^17 | Reduced wear; improved biocompatibility |
| Bearing race | 52100 steel | N+ or C+ | 100--200 | 10^17 | Fatigue life 3x--5x; reduced friction |
| Piston ring | Cast iron | N+ | 100--200 | 10^17 | Wear reduction; scuffing resistance |
| Cutting blade | WC-Co | C+ | 50--100 | 10^17 | Surface hardening without embrittlement |
| Mold surface | H13 tool steel | N+ | 100 | 10^17 | Wear resistance; reduced sticking |
| Stainless corrosion | 316L SS | N+ | 50--100 | 10^17 | Passive film stabilization; pitting resistance |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. JetBrains Mono 11 pt `#F0EDE8`. Improvement: Inter Medium 11 pt `#27AE60`.

---

### ZONE 5 -- Parameter Interaction Matrix

**Section label:** `PARAMETER INTERACTIONS -- CHANGE ONE, AFFECT ALL` -- Y: 26.7".

**BLOCK F -- Interaction Grid**

Y: 27.3" to 32.3".

| If You Change... | Effect on Depth | Effect on Dose | Effect on Damage | Effect on Temp |
|---|---|---|---|---|
| INCREASE ENERGY | Deeper implant (Rp increases) | No direct effect | More lattice damage per ion | Higher substrate heating |
| INCREASE DOSE | No effect on Rp | Higher peak concentration | More total damage (cumulative) | Higher total energy deposition |
| HEAVIER ION SPECIES | Shallower Rp (heavier ions stop sooner) | Same dose = same count | More damage per ion (heavier = more collisions) | More heating per ion |
| INCREASE BEAM CURRENT | No effect | Faster dose delivery | Same total damage (dose-limited) | MUCH higher instantaneous heating |
| INCREASE TILT ANGLE | Slightly shallower effective Rp | No effect | No direct effect | No direct effect |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 12 pt `#F0EDE8`.
Key words (Deeper, Higher, Shallower, MUCH higher): Inter Medium, accent color per severity (`#27AE60` for neutral, `#E8A020` for caution, `#E05C5C` for critical).

---

### ZONE 6 -- Footer

Standard. Title: `Parameter Setup -- Ion Implantation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically dense poster in the Ion Implantation cluster. The two-panel hero (Zone 2) communicates the two fundamental control knobs -- energy and dose -- in a way that makes physical sense. The recipe tables (Zones 3 and 4) provide concrete, real-world examples that an engineer can reference when specifying an implant. The parameter interaction matrix (Zone 5) is for experienced users who need to understand the trade-offs when adjusting a recipe. Together with Poster 454 (Beam Setup), this poster gives a complete picture of how to configure an implantation run.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #455 -- Construction Workup v1.0*
*2026-04-26*
