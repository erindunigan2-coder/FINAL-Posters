---
Project: Plating Posters Inc
Poster Number: 458
Title: "Inspection & QA -- Ion Implantation"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 458 — Inspection and QA Ion Implantation — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - IonImplantation
  - IonImplantation
  - Inspection
  - ThinFilm
  - ClusterTF06
  - v1
---

# Claude Chat Generation Prompt -- Poster #458
## Inspection & QA -- Ion Implantation
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
### Step 2 -- `Ion Implantation -- Verifying What You Cannot See` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `The implanted layer is 50--500 nm deep and invisible to the naked eye. Your coating thickness gauge is useless here. The only way to verify implant quality is analytical instrumentation.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted.

---

## Phase 4 -- Characterization Methods

Y: 15.3" to 20.3".

| Method | Standard | What It Measures | Equipment | Application |
|---|---|---|---|---|
| SIMS | ASTM E1438 | Depth profile of implanted species (concentration vs. depth) | Secondary ion mass spectrometer | Gold standard for dose and depth verification; destructive |
| 4-point probe | ASTM F84 | Sheet resistance (ohms/square) after anneal | Four-point probe station | Semiconductor inline QC; fast, non-destructive |
| Spreading resistance (SRP) | ASTM F525 | Carrier concentration vs. depth | Spreading resistance profiler | Detailed electrical profile; destructive |
| Nanoindentation | ISO 14577 | Surface hardness and elastic modulus | Nanoindenter (Berkovich tip) | Industrial -- verifies hardness improvement |
| Pin-on-disc wear test | ASTM G99 | Friction coefficient and wear rate | Tribometer | Industrial -- verifies wear improvement |
| Rutherford Backscattering (RBS) | -- | Composition and dose (non-destructive) | MeV ion beam + detector | Research; quantitative without standards |
| Cross-section TEM | -- | Lattice damage, amorphous zones, precipitates | Transmission electron microscope | Research -- direct observation of implant damage |

---

## Phase 5 -- Semiconductor Inline QC

Y: 21.3" to 26.3".

| Metric | Specification | Typical Requirement |
|---|---|---|
| Rs mean | Within +/- 3--5% of target | Process control; tight spec |
| Rs uniformity (1 sigma) | < 1--2% across wafer | Indicates uniform dose and anneal |
| Wafer-to-wafer Rs | < 1--3% variation | Indicates stable implanter and anneal |
| Lot-to-lot Rs | < 2--5% variation | Long-term process stability |

```
Four equally-spaced probes touch the wafer surface.
Current flows through the outer two probes.
Voltage is measured across the inner two probes.

Sheet resistance Rs = (pi / ln2) x (V / I)
                    = 4.532 x (V / I)

Units: ohms/square (ohms/sq)

Lower Rs = higher dose and/or better activation.
Measurement time: < 5 seconds per site.
Typical: 9-point or 49-point wafer map.
```

---

## Phase 6 -- Accept/Reject Criteria

Y: 27.3" to 32.3".
Section: `5%; channeling tail |`.

| Test | Accept | Reject |
|---|---|---|
| Sheet resistance (Rs) | Within +/- 5% of target; uniformity < 2% | Outside spec; non-uniform map |
| SIMS profile (if measured) | Rp within +/- 5% of target; dose within +/- 3% | Peak shifted; dose deviation > 5%; channeling tail |
| Visual | Clean, no particles, no resist residue | Particles, staining, resist residue |
| Wafer warpage | Within spec for downstream processing | Exceeds bow/warp limit |

| Test | Accept | Reject |
|---|---|---|
| Nanoindentation hardness | Within spec range; improvement > 30% over baseline | Below minimum hardness; no measurable improvement |
| Wear test (if specified) | Wear rate reduction > 2x vs. untreated baseline | No improvement; inconsistent results |
| SIMS (if specified) | Dose and depth within tolerance | Dose deviation > 10%; depth shifted |
| Visual | Uniform color (discoloration normal at high dose); no defects | Uneven treatment; mask alignment errors |
| Dimensional check | Zero measurable change | Should never fail -- if it does, process is wrong |

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- Ion Implantation`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Characterization methods shown are industry-standard techniques for ion implantation verification. Specific acceptance criteria vary by device specification, customer requirements, and application. SIMS depth profiling, sheet resistance measurement, and nanoindentation follow published ASTM and ISO standards. Source: General industry knowledge; ASM Handbook Vol. 5; semiconductor process literature; ASTM E1438; ASTM F84; ISO 14577.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection & QA Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
