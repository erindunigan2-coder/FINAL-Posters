---
Project: Plating Posters Inc
Poster Number: 415
Title: "Gas & Parameter Setup -- CVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 415 — Gas and Parameter Setup CVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - CVD
  - ChemicalVaporDeposition
  - BathPreparation
  - ThinFilm
  - ClusterTF02
  - v1
---

# Claude Chat Generation Prompt -- Poster #415
## Gas & Parameter Setup -- CVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `GAS & PARAMETER SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `CVD -- Stage 7 of 10 -- Precursor Recipes, Multilayer Stacks, and Gas-Phase Chemistry` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `A modern CVD cutting insert has 4+ layers deposited sequentially over 12-24 hours. Each layer has its own gas recipe, temperature, and pressure. The recipe defines the coating -- there is no shortcut.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted.

---

## Phase 4 -- Multilayer Recipe Diagram (HERO)

Y: 5.0" to 14.3".
Section: `Layer 1 (TiN) -> Purge -> Layer 2 (MT-CVD TiCN) -> Purge -> Layer 3 (Al2O3) -> Purge -> Layer 4 (TiN top) -> Cool-down.`.

| Layer | Color | X Start | Width | Y | Height | Label |
|---|---|---|---|---|---|---|
| Heat-up | `#3A4055` | 0.5" | 2.5" | 8.5" | 0.8" | `HEAT-UP (2 hr)` |
| TiN base (0.5 um) | `#C8A020` (gold) | 3.2" | 2.0" | 7.0" | 1.3" | `TiN BASE` |
| Purge | `#3A4055` | 5.4" | 0.8" | 8.5" | 0.8" | `PURGE` |
| MT-CVD TiCN (8-12 um) | `#5A6A8A` (blue-gray) | 6.4" | 5.5" | 5.5" | 2.8" | `MT-CVD TiCN` |
| Purge | `#3A4055` | 12.1" | 0.8" | 8.5" | 0.8" | `PURGE` |
| Al2O3 (4-8 um) | `#E05C5C` at 60% | 13.1" | 5.0" | 6.2" | 2.1" | `alpha-Al2O3` |
| Purge | `#3A4055` | 18.3" | 0.8" | 8.5" | 0.8" | `PURGE` |
| TiN top (1 um) | `#C8A020` (gold) | 19.3" | 1.5" | 7.5" | 0.8" | `TiN TOP` |
| Cool-down | `#3A4055` | 21.0" | 2.5" | 8.5" | 0.8" | `COOL-DOWN (4+ hr)` |

---

## Phase 5 -- Layer Parameter Table

Y: 15.3" to 21.3".

| Parameter | TiN (HT) | MT-CVD TiCN | Al2O3 (alpha) | TiC (HT) |
|---|---|---|---|---|
| Temperature | 1000-1050 C | 700-900 C | 1000-1050 C | 1000-1050 C |
| Pressure | 50-200 mbar | 50-200 mbar | 50-100 mbar | 50-200 mbar |
| TiCl4 | 2-5% of total | 2-5% of total | -- | 2-5% of total |
| N2 | 20-40% | -- | -- | -- |
| CH4 | -- | -- | -- | 3-6% |
| CH3CN (acetonitrile) | -- | 0.5-2% | -- | -- |
| AlCl3 | -- | -- | 2-5% | -- |
| CO2 | -- | -- | 3-6% | -- |
| H2 (carrier) | Balance | Balance | Balance | Balance |
| Deposition rate | 0.5-2 um/hr | 2-5 um/hr | 0.5-1.5 um/hr | 1-3 um/hr |
| Typical thickness | 0.5-3 um | 8-12 um | 4-8 um | 3-10 um |
| Layer time | 1-3 hr | 2-4 hr | 4-8 hr | 2-5 hr |
| Hardness | 2000-2400 HV | 2500-3000 HV | 2000-2200 HV | 2800-3200 HV |

---

## Phase 6 -- Precursor Chemistry + Recipe Notes

Y: 21.5" to 26.8".
Section: `TiN + 4 HCl``.

- `TiCl4 + 1/2 N2 + 2 H2 -> TiN + 4 HCl`
- `TiCl4 + CH4 -> TiC + 4 HCl`
- `TiCl4 + CH3CN + H2 -> TiCN + HCl + ...`
- `2 AlCl3 + 3 CO2 + 3 H2 -> Al2O3 + 3 CO + 6 HCl`
- `TiCl4 is a liquid (bp 136 C) -- delivery rate depends on bubbler temperature. +/- 1 C bubbler drift = measurable composition change.`
- `AlCl3 is a solid that sublimes -- requires its own heated delivery system (sublimator at 150-180 C).`
- `MT-CVD uses CH3CN (acetonitrile) as combined carbon + nitrogen source -- simpler gas system than separate CH4 + N2.`
- `Alpha-Al2O3 nucleation requires a precise oxidation pulse at the start of the Al2O3 step -- this controls crystal phase.`
- `Pre-hardened steel substrates (HSS) cannot tolerate any CVD temperature above 550 C -- use PVD instead.`

---

## Phase 7 -- Common Parameter Failures

Y: 27.8" to 32.3".

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WRONG Al2O3 PHASE | Nucleation pulse incorrect -- kappa instead of alpha | Verify oxidation pulse protocol; check temperature and timing |
| 2 | 6.33" | COBALT DEPLETION | TiC/TiN layer at HT (1050 C) + HCl attacks cobalt binder | Use MT-CVD TiCN for thick inner layers (700-900 C) |
| 3 | 12.16" | SOOT IN COATING | CH4 flow too high -- thermal cracking produces free carbon | Reduce CH4 ratio; verify MFC calibration; increase H2 flow |
| 4 | 18.0" | LAYER CONTAMINATION | Insufficient H2 purge between layers | Increase purge time to 20-30 min; verify gas switching valves |

---

## Phase 8 -- Footer

Standard. Title: `Gas & Parameter Setup -- CVD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 9 -- Review

- [ ] Headline `GAS & PARAMETER SETUP` 80pt
- [ ] Orientation strip with poster 7 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Gas & Parameter Setup CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
