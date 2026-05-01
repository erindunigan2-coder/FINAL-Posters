---
Project: Plating Posters Inc
Poster Number: 535
Title: "Parameter Setup -- D-Gun"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 535 — Parameter Setup D-Gun — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - DGun
  - DetonationGun
  - Parameters
  - ClusterTS06
  - v1
---

# Claude Chat Generation Prompt -- Poster #535
## Parameter Setup -- D-Gun
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PARAMETER SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `D-Gun -- Tuning the Controlled Explosion` -- `32` pt `#E8A020`. Y: **1.5"**.
### Step 3 -- `Gas ratio. Frequency. Powder charge. Standoff. Every detonation cycle is a precision event -- parameters determine whether you get the gold standard or a reject.` -- `22` pt at 65%. Y: **2.2"**.

Rule card (right): Big number `1.0--1.5` 60pt `#E8A020`. Label: `O2/C2H2 ratio -- the master control variable`.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted. Stage 7 highlighted (Amber).

---

## Phase 4 -- Parameter Table + O2/C2H2 Callout (HERO)

Y: 2.9" to 14.0". Section label: `OPERATING PARAMETER RANGES`.

### Master Parameter Table (Left, W: 14.5")

13-row table. Columns: Parameter (4.0") | Typical Range (4.5") | Notes (6.0").

| Parameter | Typical Range | Notes |
|---|---|---|
| Detonation frequency | 1--15 Hz | Higher = more deposition + more heat |
| O2 fill volume | Barrel-dependent | Not operator-adjustable in most systems |
| C2H2 fill volume | Barrel-dependent | O2/C2H2 ratio is the key variable |
| O2/C2H2 ratio | 1.0--1.5 | Stoichiometric to lean; lean = less oxide |
| Detonation velocity | ~3500 m/s | Inherent to detonation gas dynamics |
| Particle velocity | 750--1000 m/s | Highest of all thermal spray |
| Detonation temperature | 3500--4500 C | Peak gas temp during wave |
| Powder charge | 0.5--3 g/cycle | Determines spot thickness |
| Standoff distance | 100--200 mm | Closer than HVOF; rapid deceleration |
| N2 purge volume | 1--3x barrel vol | Must clear previous cycle |
| Deposition rate | 1--5 kg/hr | Lower than HVOF |
| Deposition efficiency | 70--90% | High velocity + good melting |
| Spot diameter | ~25 mm | Per cycle; overlap for continuous coating |

Header fill `#3A4055`. Data: JetBrains Mono 12pt.

### O2/C2H2 Ratio Callout (Right, W: 8.0")

Amber-tinted glass. Title: `O2/C2H2 RATIO` 28pt `#E8A020`. Subtitle: `The Master Control Variable`.

Ratio effects (JetBrains Mono):

```
1.0  Stoichiometric  Max temp; highest oxide
1.1  Slightly lean   Reduced temp; standard WC-Co
1.3--1.5  Lean       Lowest oxide; best for WC-Co, CrC
```

Key insight (emerald callout): `LEAN RATIO = LESS OXIDE. For WC-Co, lean O2/C2H2 reduces decarburization -- preserving the WC phase that provides hardness and wear resistance.`

---

## Phase 5 -- Frequency vs. Heat + Material Notes

Y: 14.0" to 22.0".

### Left -- Frequency Guide (W: 11.5")

Section label: `DETONATION FREQUENCY -- THE THROUGHPUT vs. HEAT TRADE-OFF`. Three range cards:

| Range | Accent | Hz | Rate | Heat | Best For |
|---|---|---|---|---|---|
| LOW | `#27AE60` | 1--4 | 1--2 kg/hr | Minimal | Heat-sensitive; thin coatings; precision |
| MEDIUM | `#E8A020` | 4--8 | 2--3 kg/hr | Moderate | Standard production; most WC-Co |
| HIGH | `#E05C5C` | 8--15 | 3--5 kg/hr | Significant | Max throughput; thick coatings; robust substrates |

Heat note: `At high frequencies, cooling air between cycles is critical. Monitor substrate temp continuously.`

### Right -- Material-Specific Notes (W: 11.0")

Section label: `MATERIAL-SPECIFIC PARAMETER ADJUSTMENTS`. Three material cards:

| Material | Accent | Adjustment | Rationale |
|---|---|---|---|
| WC-Co (WC-12Co, WC-17Co) | `#E8A020` | Lean ratio 1.1--1.5; moderate freq | Minimize decarburization; preserve WC/W2C |
| Cr2O3 (Chrome Oxide) | `#27AE60` | Stoichiometric to slightly lean; higher charge | Ceramic needs full melting; larger charge builds faster |
| CrC-NiCr (Chrome Carbide) | `#2EC4B6` | Lean ratio; lower freq for heat-sensitive | Protect carbide phase from decomposition |

---

## Phase 6 -- Parameter Interactions + Common Errors

Y: 22.0" to 32.5".

### Left -- Parameter Interactions (W: 12.0")

Section label: `PARAMETER INTERACTIONS`. Six stacked cards:

| If You Change... | Accent | Effect | Counter-Adjustment |
|---|---|---|---|
| INCREASE frequency | `#E8A020` | Higher rate + higher heat | Increase cooling; reduce passes; monitor temp |
| INCREASE O2/C2H2 (leaner) | `#27AE60` | Lower oxide + lower particle temp | May need higher frequency for rate |
| INCREASE powder charge | `#E8A020` | Thicker spot; higher rate | May reduce velocity (more mass) |
| DECREASE standoff | `#2EC4B6` | Denser coat; smaller spot; more heat | More cooling; slower traverse |
| INCREASE standoff | `#E05C5C` | Particles decelerate; lower density | Reduce standoff (limited by gas dynamics) |
| INCREASE barrel length | `#C8D0D8` | Higher velocity; longer acceleration | Equipment design decision; not field-adjustable |

Counter-adjustments in `#27AE60`.

### Right -- Common Errors (W: 10.5")

Section label: `COMMON PARAMETER ERRORS`. Five stacked cards:

| Error | Color | Symptom | Correction |
|---|---|---|---|
| O2/C2H2 TOO RICH | `#E05C5C` | Excessive oxide; dark color; low hardness | Increase O2 or decrease C2H2; verify metering |
| FREQUENCY TOO HIGH | `#E05C5C` | Overheating; cracking; distortion | Reduce frequency; increase cooling; pause |
| POWDER OVERLOADED | `#E8A020` | Unmelted particles; porosity | Reduce charge; verify feeder calibration |
| STANDOFF TOO FAR | `#E8A020` | Porous; low bond; deceleration | Reduce to 100--200 mm; verify robot |
| N2 PURGE INSUFFICIENT | `#E05C5C` | Premature detonation; barrel damage risk | Increase to 2--3x barrel vol; verify N2 supply |

---

## Phase 7 -- Footer

Standard. Title: `Parameter Setup -- D-Gun`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Operating parameters shown are typical ranges for D-Gun systems. Specific parameter settings depend on equipment configuration, feedstock material, and coating specification. Consult your equipment manufacturer and process specification for application-specific values.`

---

## Phase 8 -- Review

- [ ] Headline `PARAMETER SETUP` 80pt
- [ ] 1.0--1.5 rule card (O2/C2H2 ratio)
- [ ] 13-row master parameter table
- [ ] O2/C2H2 ratio callout with ratio effects
- [ ] 3 frequency range cards (low/med/high)
- [ ] 3 material-specific adjustment cards
- [ ] 6 parameter interaction cards
- [ ] 5 common error cards
- [ ] Footer with disclaimer

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Parameter Setup D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
