---
Project: Plating Posters Inc
Poster Number: 428
Title: "Inspection & QA -- PECVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 428 — Inspection and QA PECVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PECVD
  - PlasmaEnhancedCVD
  - Inspection
  - ThinFilm
  - ClusterTF03
  - v1
---

# Claude Chat Generation Prompt -- Poster #428
## Inspection & QA -- PECVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION & QA` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PECVD -- Stage 9 of 10 -- Film Characterization and Acceptance` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Refractive index tells you if the stoichiometry is right. Thickness tells you if the rate was stable. Stress tells you if the film will survive. Measure all three.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted.

---

## Phase 4 -- Film Property Dashboard Hero

Y: 5.0" to 13.3".

| Film | Refractive Index (n) | Dielectric Constant (k) | Hardness | Film Stress | BOE Etch Rate |
|---|---|---|---|---|---|
| SiO2 | 1.46--1.47 | 4.0--4.5 | 6--8 GPa | < 200 MPa (comp.) | 200--400 nm/min |
| Si3N4 | 1.85--2.05 | 6.0--7.5 | 15--25 GPa | < 300 MPa (comp.) | Very slow (< 5 nm/min) |
| SiNx:H (solar) | 2.0--2.1 (tunable) | 5--7 | 12--18 GPa | < 200 MPa | Slow |
| a-Si:H | 3.5--4.5 | 11--12 | -- | Variable | -- |
| DLC (a-C:H) | 1.8--2.4 | 3--5 | 10--30 GPa | < 1 GPa (comp.) | -- |

Callout: `REFRACTIVE INDEX is the single most informative QA metric for PECVD films. If n matches the target, stoichiometry is correct. If n drifts, the gas ratio has shifted.`


---

## Phase 5 -- Measurement Techniques

Y: 14.3" to 20.3".

| Card | Technique | What It Measures | Accuracy | Destructive? | Accent |
|---|---|---|---|---|---|
| 1 | ELLIPSOMETRY | Thickness + refractive index | +/- 0.5 nm thickness; +/- 0.01 n | No | `#E8A020` |
| 2 | FTIR SPECTROSCOPY | Film composition -- Si-O, Si-N, Si-H, N-H bond peaks | Qualitative to semi-quantitative | No | `#2EC4B6` |
| 3 | WAFER BOW (STONEY EQUATION) | Film stress (tensile vs. compressive) | +/- 10 MPa | No | `#27AE60` |
| 4 | BOE ETCH RATE | Film density proxy -- lower etch rate = denser film | +/- 5% | Yes (partial etch) | `#C8D0D8` |
| 5 | TAPE / SCRATCH ADHESION | Film adhesion to substrate | Qualitative (pass/fail) | Yes (localized) | `#E05C5C` |

---

## Phase 6 -- FTIR Reference + Acceptance Criteria + Anneal

Y: 21.3" to 25.5".
Section: `continue`.

| Peak Position (cm-1) | Bond | Interpretation |
|---|---|---|
| ~1060 | Si-O stretch | Primary SiO2 peak -- shift indicates off-stoichiometry |
| ~810 | Si-O bend | Secondary SiO2 confirmation |
| ~880 | Si-N stretch | Primary Si3N4 peak |
| ~2100 | Si-H stretch | Hydrogen in film -- higher = more H, less dense |
| ~3340 | N-H stretch | Hydrogen bonded to nitrogen -- indicates Si3N4 quality |
| ~2350 | CO2 (atmospheric) | Ignore -- background artifact from spectrometer |

```
Drives out hydrogen -> densifies film
Reduces BOE etch rate (closer to thermal SiO2)
Lowers dielectric leakage current
Improves long-term stability
```

```
Substrate cannot survive 400 degC (polymers, assembled devices)
Film is intentionally H-rich (solar SiNx:H -- H provides passivation)
Application does not require densification (barrier coatings)
```

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- PECVD`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Film property targets and measurement techniques shown are representative of PECVD operations. Specific acceptance criteria depend on your application, customer specification, and equipment capabilities.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection & QA PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
