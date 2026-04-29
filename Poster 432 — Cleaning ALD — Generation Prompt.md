---
Project: Plating Posters Inc
Poster Number: 432
Title: "Cleaning -- ALD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 432 — Cleaning ALD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - Stage
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #432
## Cleaning -- ALD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `CLEANING` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 2 of 10 -- Contaminant Removal + Surface Activation` -- `32` pt `#2EC4B6`. Y: **1.4"**.
### Step 3 -- `For ALD, "clean" means two things: no contamination AND correct surface chemistry. Remove the dirt, then set the stage for the first precursor pulse.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 4 of 10 highlighted.

---

## Phase 4 -- Dual-Purpose Cleaning Hero

Y: 5.0" to 12.8".
Section: `island growth`.

```
ORGANIC CONTAMINATION
- Fingerprints, oils, grease
- Photoresist residue
- Adventitious carbon from air exposure
EFFECT: Carbon blocks -OH sites -> island growth

PARTICULATE CONTAMINATION
- Dust, fibers, packaging debris
- Less critical than for PVD (ALD coats around particles)
- BUT particles still create bump defects

METALLIC CONTAMINATION
- Metal ions from previous processing steps
- Fe, Cu, Na from handling or chemicals
EFFECT: Metals can act as unwanted catalysts or dopants
```

```
CREATE NUCLEATION SITES
- -OH (hydroxyl) groups for oxide ALD
- -NH2 (amine) groups for nitride ALD
- Uniform density across entire surface

METHODS:
- Native oxide provides -OH on Si, Al, glass
- UV-ozone CREATES -OH on bare metals
- O2 plasma CREATES -OH/-COOH on polymers
- HF dip REMOVES oxide (H-terminated Si)

GOAL: Every surface site has a functional
group ready to react with Precursor A.
```

---

## Phase 5 -- Cleaning Methods + RCA Detail

Y: 13.2" to 18.0".

| Substrate | Wet Clean | Activation | Final Surface | Cleanroom Class |
|---|---|---|---|---|
| Si wafers | RCA SC-1 + SC-2 | Optional HF dip | -OH (oxide) or -H (HF last) | ISO 5 (Class 100) |
| Metals | Ultrasonic alkaline + IPA | UV-ozone 5--30 min | -OH on oxide layer | ISO 6--7 |
| Polymers | IPA wipe (gentle) | O2 plasma 1--5 min | -OH / -COOH | ISO 6--7 |
| Glass | Solvent + DI rinse | UV-ozone (optional) | Native Si-OH | ISO 6 |
| Powders | None (no wet clean) | Thermal bake in reactor | Variable | N/A |
| Porous | Solvent rinse + vacuum bake | UV-ozone or thermal | -OH in pores | ISO 7 |

---

## Phase 6 -- Activation Techniques + Contamination Effects

Y: 22.2" to 27.5".

| Contaminant | Effect on Nucleation | Detection | Impact |
|---|---|---|---|
| Carbon (organics) | Blocks -OH sites; causes island growth | XPS (C 1s peak); contact angle | Pinholes; non-uniform film; poor barrier |
| Water residue | Premature reaction with TMA in gas phase | RGA; extended pump-down | Particles; CVD-like growth; rough film |
| Metal ions (Na, Fe, Cu) | Act as dopants; alter film electrical properties | TXRF; SIMS | Shift dielectric constant; leakage current |
| Particulates | ALD coats around them; bump defects | Optical inspection; particle counter | Localized defects; acceptable in non-critical apps |
| Native oxide (too thick) | Adds uncontrolled thickness to total stack | Ellipsometry | May exceed spec; strip with HF if needed |

```
Mechanism: 185 + 254 nm UV light generates
O3 and atomic oxygen from air O2
These species oxidize organics and create
-OH groups on metal/oxide surfaces

Parameters:
  Time: 5--30 min
  Distance: sample 5--20 mm from UV lamp
  Atmosphere: air (ambient)
  Equipment: UV-ozone cleaner (benchtop)

Best for: metals, inorganics
Not suitable for: polymers (UV damages)
```

```
Mechanism: RF plasma generates reactive
oxygen species that functionalize surfaces
Creates -OH and -COOH groups on polymers
Also removes ~1 nm/min of organic material

Parameters:
  Power: 50--200 W
  Time: 1--5 min
  Pressure: 100--500 mTorr
  Gas: O2 or O2/Ar mixture

Best for: polymers, assembled devices
CRITICAL for: PET, PC, PTFE substrates
```

---

## Phase 7 -- Footer

Standard. Title: `Cleaning -- ALD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `CLEANING` 88pt
- [ ] Orientation strip with poster 4 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Cleaning ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
