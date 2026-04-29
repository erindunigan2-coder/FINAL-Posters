---
Project: Plating Posters Inc
Poster Number: 426
Title: "Deposition Stage -- PECVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 426 — Deposition Stage PECVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PECVD
  - PlasmaEnhancedCVD
  - MainStage
  - ThinFilm
  - ClusterTF03
  - v1
---

# Claude Chat Generation Prompt -- Poster #426
## Deposition Stage -- PECVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `DEPOSITION STAGE` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PECVD -- Stage 6 of 10 -- Plasma On, Film Growing` -- `32` pt `#27AE60`. Y: **1.4"**.
### Step 3 -- `The plasma breaks the bonds. The surface catches the pieces. Every second of glow discharge builds your film -- angstrom by angstrom.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 8 of 10 highlighted.

---

## Phase 4 -- Film Growth Mechanism Hero

Y: 5.0" to 13.8".
Section: `SiH3 + H (radical)`.

```
SiH4  -->  SiH3 + H (radical)
N2O   -->  O + N2 (radical + inert)
SiH3 + O  -->  SiH2O (precursor to film)
```

```
SiH4  -->  SiH2 + 2H (radical)
NH3   -->  NH2 + H (radical)
SiH2 + NH2  -->  film precursors
```

```
1. Reactive species adsorb on substrate surface
2. Surface migration to energetically favorable sites
3. Chemical bonds form -- Si-O or Si-N network grows
4. Byproducts (H2, CH4) desorb and are pumped away
5. Film grows layer by layer (amorphous structure)
```

Callout: `PECVD films are AMORPHOUS (no crystal structure) and contain 1--30 at% hydrogen. This hydrogen affects density, etch rate, refractive index, and long-term stability.`


---

## Phase 5 -- In-Situ Monitoring + Deposition Rates

Y: 14.8" to 19.8".

| Card | Technique | What It Measures | Accent |
|---|---|---|---|
| 1 | LASER INTERFEROMETRY | Film thickness in real-time (fringe counting -- each fringe = lambda/2n) | `#27AE60` |
| 2 | OPTICAL EMISSION (OES) | Plasma species composition -- detects gas ratio drift | `#E8A020` |
| 3 | RESIDUAL GAS ANALYZER (RGA) | Gas-phase composition by mass spectrometry -- detects leaks, contamination | `#2EC4B6` |

| Film | Rate | Time for 100 nm | Time for 1 um |
|---|---|---|---|
| SiO2 (SiH4 + N2O) | 50--200 nm/min | 30 sec--2 min | 5--20 min |
| Si3N4 (SiH4 + NH3) | 10--50 nm/min | 2--10 min | 20--100 min |
| a-Si:H | 5--30 nm/min | 3--20 min | 30--200 min |
| SiNx:H (solar) | 10--30 nm/min | 3--10 min | 30--100 min |
| DLC (a-C:H) | 5--30 nm/min | 3--20 min | 30--200 min |

---

## Phase 6 -- Defects + Stability Indicators

Y: 20.2" to 27.0".
Section: `2% -- MFC drift | `#2EC4B6` |`.

| Defect | Cause | Prevention | Indicator |
|---|---|---|---|
| Particles in film | Gas-phase nucleation; wall flaking | Lower pressure; clean chamber every 5--50 um accumulated | Particle counts on test wafer |
| Pinholes | Particles on substrate; film too thin | Proper cleaning; minimum 50 nm film thickness | Visual inspection; electrical test |
| High hydrogen content | Low temperature; high SiH4 flow | Increase temp; reduce SiH4 flow; post-anneal at 400--450 degC | FTIR: Si-H peak at ~2100 cm-1 |
| Poor step coverage | Geometry limitations of PECVD | Use TEOS-based SiO2; consider HDP-CVD for gap fill | SEM cross-section of test structure |
| Film cracking | Excessive tensile stress; film too thick | Adjust RF power/pressure for low stress; multilayer approach | Wafer bow measurement (Stoney equation) |
| Non-uniformity | Showerhead clogging; gas flow dead zones | Clean showerhead; optimize electrode spacing | 49-point ellipsometry map |

| Position | Indicator | Normal | Alarm | Accent |
|---|---|---|---|---|
| R1C1 | RF Forward Power | Stable at setpoint +/- 2% | Drifting or fluctuating | `#27AE60` |
| R1C2 | Reflected Power | < 5% of forward | Rising -- matching network losing tune | `#E05C5C` |
| R1C3 | Chamber Pressure | Stable at recipe pressure +/- 5% | Drifting -- gas flow or pump issue | `#E8A020` |
| R2C1 | Substrate Temperature | At setpoint +/- 3 degC | Drifting -- heater or thermocouple fault | `#E8A020` |
| R2C2 | Gas Flow (MFC readback) | Matches setpoint | Deviation > 2% -- MFC drift | `#2EC4B6` |
| R2C3 | Plasma Glow Color | Consistent, characteristic of recipe | Color shift -- gas ratio changing | `#C8D0D8` |

---

## Phase 7 -- Footer

Standard. Title: `Deposition Stage -- PECVD`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Deposition parameters and rates shown are typical industry values. Actual results depend on specific equipment, gas purity, and chamber condition. Consult your equipment manufacturer for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `DEPOSITION STAGE` 88pt
- [ ] Orientation strip with poster 8 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Deposition Stage PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
