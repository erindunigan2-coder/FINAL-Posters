---
Project: Plating Posters Inc
Poster Number: 425
Title: "Parameter Setup -- PECVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 425 — Parameter Setup PECVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PECVD
  - PlasmaEnhancedCVD
  - BathPreparation
  - ThinFilm
  - ClusterTF03
  - v1
---

# Claude Chat Generation Prompt -- Poster #425
## Parameter Setup -- PECVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PARAMETER SETUP` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PECVD -- Stage 5 of 10 -- Gas Flows, RF Power, Pressure, and Temperature` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Every parameter controls a film property. Change one, measure the result, build the recipe. PECVD is a four-knob instrument -- learn what each knob does.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted.

---

## Phase 4 -- Representative Recipes Hero

Y: 5.0" to 15.3".

| Parameter | Value |
|---|---|
| Precursor 1 | SiH4 at 30--100 sccm |
| Precursor 2 | N2O at 300--1000 sccm |
| SiH4 : N2O ratio | 1:5 to 1:10 |
| Carrier gas | N2 or Ar |
| RF power | 100--300 W (13.56 MHz) |
| Pressure | 1--3 Torr |
| Substrate temp | 300--400 degC |
| Electrode gap | 15--25 mm |
| Deposition rate | 50--200 nm/min |

| Parameter | Value |
|---|---|
| Precursor 1 | SiH4 at 50--200 sccm |
| Precursor 2 | NH3 at 20--100 sccm |
| Dilution gas | N2 at 500--2000 sccm |
| SiH4 : NH3 ratio | 1:1 to 5:1 (tunable) |
| RF power | 100--500 W (13.56 MHz) |
| Pressure | 1--3 Torr |
| Substrate temp | 300--400 degC |
| Electrode gap | 15--25 mm |
| Deposition rate | 10--50 nm/min |

```
Refractive index:  n = 1.46--1.47
Dielectric const:  k = 4.0--4.5
Film stress:       < 200 MPa (compressive)
```

```
Refractive index:  n = 1.85--2.05 (tunable)
Dielectric const:  k = 6.0--7.5
Film stress:       < 300 MPa (compressive)
```

---

## Phase 5 -- Tuning Relationships

Y: 16.3" to 21.3".

| Position | Parameter Change | Effect on Film | Accent |
|---|---|---|---|
| R1C1 | INCREASE RF POWER | Denser film, higher stress, faster rate, less hydrogen | `#E8A020` |
| R1C2 | INCREASE TEMPERATURE | Less hydrogen, denser, more stable, higher refractive index | `#E05C5C` |
| R1C3 | INCREASE PRESSURE | More gas-phase reactions, risk of particles, better step coverage | `#C8D0D8` |
| R2C1 | INCREASE SiH4 : N2O RATIO | Si-rich SiOx -- higher n, higher leakage current | `#2EC4B6` |
| R2C2 | INCREASE SiH4 : NH3 RATIO | Si-rich SiNx -- higher n, higher absorption | `#2EC4B6` |
| R2C3 | INCREASE ELECTRODE GAP | Better uniformity, lower rate, more particles at extreme | `#27AE60` |

---

## Phase 6 -- Gas-to-Film Chart + Film Targets + Safety

Y: 22.3" to 27.5".

| Film | Precursors | Carrier | Notes |
|---|---|---|---|
| SiO2 | SiH4 + N2O | N2 or Ar | Or TEOS + O2 for better step coverage |
| Si3N4 | SiH4 + NH3 | N2 | Or SiH4 + N2 (lower quality) |
| SiON | SiH4 + N2O + NH3 | N2 | Tunable n between SiO2 and Si3N4 |
| a-Si:H | SiH4 | H2 or Ar | Amorphous silicon for TFT, solar |
| SiC | SiH4 + CH4 | Ar | Hard, chemically resistant |
| DLC (a-C:H) | C2H2 or CH4 | Ar | Diamond-like carbon; see Cluster 5 |

| Film | Refractive Index (n) | Dielectric Constant (k) | Hardness | BOE Etch Rate |
|---|---|---|---|---|
| PECVD SiO2 | 1.46--1.47 | 4.0--4.5 | 6--8 GPa | 200--400 nm/min |
| PECVD Si3N4 | 1.85--2.05 | 6.0--7.5 | 15--25 GPa | Very slow |
| PECVD SiNx:H (solar) | 2.0--2.1 | 5--7 | 12--18 GPa | -- |
| PECVD a-Si:H | 3.5--4.5 | 11--12 | -- | -- |
| PECVD DLC (a-C:H) | 1.8--2.4 | 3--5 | 10--30 GPa | -- |

```
MFC responding correctly
No pressure spikes during flow change
Exhaust scrubber running
LEL detector reading zero
```

```
Test on dummy substrates first
Measure film properties (n, thickness, stress)
Compare to target before committing
Log all recipe changes with date and operator
```

---

## Phase 7 -- Footer

Standard. Title: `Parameter Setup -- PECVD`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for PECVD. Specific recipes vary by equipment manufacturer and application. Consult your equipment manual for exact parameter ranges.`

---

## Phase 8 -- Review

- [ ] Headline `PARAMETER SETUP` 88pt
- [ ] Orientation strip with poster 7 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Parameter Setup PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
