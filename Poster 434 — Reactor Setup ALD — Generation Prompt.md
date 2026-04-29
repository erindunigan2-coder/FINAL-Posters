---
Project: Plating Posters Inc
Poster Number: 434
Title: "Reactor Setup -- ALD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 434 — Reactor Setup ALD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - BathPreparation
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #434
## Reactor Setup -- ALD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `REACTOR SETUP` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 4 of 10 -- Precursor Delivery and System Preparation` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `The bubbler controls the dose. The heated lines prevent condensation. The carrier gas moves the molecules. Every component must work in concert.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 6 of 10 highlighted.

---

## Phase 4 -- Precursor Delivery Hero

Y: 5.0" to 14.3".
Section: `valve -> reactor path`.

```
Liquid precursor (TMA, TDMAT, etc.)
Temperature bath: +/- 1 degC
Carrier gas (N2/Ar) inlet at bottom
Precursor vapor exits at top
Typical: 20--80 degC depending on precursor
```

---

## Phase 5 -- Precursor Pairs + Bubbler Operation


| Film | Precursor A | Co-Reactant B | Bubbler Temp (A) | ALD Temp |
|---|---|---|---|---|
| Al2O3 | TMA (trimethylaluminum) | H2O | 20--25 degC | 150--300 degC |
| HfO2 | TEMAH or HfCl4 | H2O or O3 | 50--80 degC | 200--350 degC |
| TiO2 | TDMAT or TiCl4 | H2O or O3 | 40--75 degC | 150--350 degC |
| ZrO2 | TEMAZ | H2O | 40--60 degC | 200--350 degC |
| ZnO | DEZ (diethylzinc) | H2O | 0--25 degC | 100--250 degC |
| TiN | TDMAT | NH3 | 40--75 degC | 250--400 degC |
| SiO2 | BDEAS or 3DMAS | O2 plasma | 30--50 degC | 50--400 degC |
| Pt | MeCpPtMe3 | O2 or O3 | 60--80 degC | 250--350 degC |

```
PRINCIPLE:
  Carrier gas (N2/Ar) flows through liquid
  precursor, picking up vapor molecules.
  The amount of vapor depends on:

  1. BUBBLER TEMPERATURE
     Higher temp = higher vapor pressure = more precursor per pulse
     Must be controlled to +/- 1 degC for consistent dosing

  2. CARRIER GAS FLOW RATE
     Higher flow = more precursor delivered per unit time
     Typical: 10--200 sccm

  3. BUBBLER PRESSURE
     Some systems use pressure-controlled delivery
     instead of flow-controlled

CRITICAL: If bubbler temp drifts, dose changes.
If dose changes, GPC changes. If GPC changes,
your film thickness drifts from target.
```

---

## Phase 6 -- Line Heating + Pre-Run Checks

Y: 23.2" to 27.5".

```
If a delivery line is cooler than the
precursor's condensation point, precursor
vapor condenses inside the line.

CONSEQUENCES:
- Inconsistent dosing (no vapor reaches reactor)
- Clogged lines (TMA residue is sticky)
- For pyrophoric precursors (TMA, DEZ):
  condensate + air on maintenance = FIRE
```

```
HEAT ALL LINES above precursor condensation
temperature. Typical: 10--20 degC above.

LINE HEATING ZONES:
  Bubbler outlet to valve: heated jacket
  Valve body: heated
  Valve to reactor: heated
  Reactor walls: heated
  Exhaust line: heated (prevent buildup)

VERIFY: All zone thermocouples reading
correctly. One cold spot = one blockage.
```

```
[ ] Bubbler A temperature at setpoint (+/- 1 degC)
[ ] Bubbler B (or H2O/O3) ready
[ ] All heated lines at setpoint (verify all zones)
[ ] Carrier gas flow confirmed (MFC responding)
[ ] ALD valves tested (listen for click)
[ ] Base pressure achieved (0.1--1 Torr)
```

```
[ ] Substrate temperature stable (within ALD window)
[ ] Exhaust/pump running
[ ] Precursor level in bubbler sufficient for run
[ ] Recipe loaded: pulse times, purge times, cycle count
[ ] Safety interlocks green
[ ] If TMA/DEZ: Class D extinguisher at station
```

---

## Phase 7 -- Footer

Standard. Title: `Reactor Setup -- ALD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `REACTOR SETUP` 88pt
- [ ] Orientation strip with poster 6 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Reactor Setup ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
