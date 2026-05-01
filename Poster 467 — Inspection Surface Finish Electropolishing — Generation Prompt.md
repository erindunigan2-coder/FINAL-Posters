---
Project: Plating Posters Inc
Poster Number: 467
Title: "Inspection -- Surface Finish -- Electropolishing"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 467 — Inspection Surface Finish Electropolishing — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Electropolishing
  - Inspection
  - SurfaceFinish
  - SpecialtyAdvanced
  - ClusterSA07
  - v1
---

# Claude Chat Generation Prompt -- Poster #467
## Inspection -- Surface Finish -- Electropolishing
### Version 1.0 | Dark + Light

*Alaina from CW v1.0 (2026-04-26).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Electropolishing -- Surface Finish Verification & Quality Control` -- `36` pt `#E8A020`. Y: **1.5"**.
### Step 3 -- `Ra, Rz, Cr:Fe ratio, ferroxyl, visual -- the complete QC toolkit for electropolished surfaces. Measure what matters. Document everything.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 9 of 10 highlighted. Stage 8 highlighted (Amber -- Inspect portion).

---

## Phase 4 -- Measurement Methods (HERO)

Y: 4.2" to 15.0".

Section label: `SURFACE FINISH MEASUREMENT METHODS`

| Method | What It Measures | Range | Accuracy | Destr.? | Standard | Notes |
|---|---|---|---|---|---|---|
| Stylus profilometer | Ra, Rz, Rq, Rmax | 0.005--50 um | +/- 5--10% | No | ISO 4287, ASME B46.1 | Primary QC tool |
| Optical profilometer | Ra, Rz, 3D topography | 0.001--50 um | +/- 2--5% | No | ISO 25178 | Non-contact; soft metals |
| Glossmeter | Reflectivity / gloss | 0--1000 GU | +/- 2 GU | No | ASTM D523 | Correlates to appearance |
| ESCA / XPS | Cr:Fe ratio, oxide thickness | Top 1--10 nm | Quantitative | No | -- | Passive layer analysis |
| Ferroxyl test | Free iron | Pass/fail | Qualitative | No | ASTM A380 | Passivation QC |
| Copper sulfate test | Free iron | Pass/fail | Qualitative | No | ASTM A967/A380 | Passivation QC |
| Water-break test | Surface cleanliness | Pass/fail | Qualitative | No | Visual | Contamination screen |
| Weight loss | Average material removal | mg/cm2 | +/- 1% | No | Gravimetric | Avg removal depth |

**Key surface roughness parameters (Teal accent):**

| Param | Definition |
|---|---|
| **Ra** | Arithmetic average of deviations from mean. Most commonly specified. |
| **Rz** | Average of 5 highest peaks to 5 deepest valleys. More sensitive to extremes. |
| **Rq** | Root mean square of deviations. Statistically more rigorous than Ra. |
| **Rmax** | Maximum peak-to-valley height. Catches worst-case defects. |

---

## Phase 5 -- Specification Targets + Visual Inspection

Y: 15.0" to 21.5".

Section label: `TARGET VALUES BY APPLICATION`

| Application | Ra (um) | Ra (uin) | Rz (um) | Spec | Notes |
|---|---|---|---|---|---|
| General industrial | < 0.8 | < 32 | < 3.2 | Customer spec | Visible brightness improvement |
| Food/beverage (3A) | < 0.8 | < 32 | < 3.2 | 3-A 605-04 | Sanitary finish |
| Pharma (ASME BPE SF4) | < 0.5 | < 20 | < 2.5 | ASME BPE | Standard EP finish |
| Pharma high-purity | < 0.25 | < 10 | < 1.5 | ASME BPE SF6 | Premium EP; multi-step |
| Semiconductor | < 0.25 | < 10 | < 1.0 | SEMI F19 | Ultra-clean |
| Medical implants | < 0.4 | < 16 | < 2.0 | ASTM F86 | Biocompatible |
| Decorative (mirror) | < 0.1 | < 4 | < 0.5 | Visual | Requires excellent starting surface |

Conversion note: `1 um = 39.37 uin. Rz is typically 4--6x Ra for EP surfaces.`

**Visual inspection guide (Amber accent):**
`Inspect under diffuse white light at 18--24 in. Rotate part at multiple angles. Look for: orange peel, pitting, streaking, staining, uneven brightness, contact marks, water spots. Critical apps: direct AND diffuse lighting. Document deviations with photos.`

---

## Phase 6 -- Passivation Verification + Accept/Reject

Y: 21.5" to 32.5".

**Passivation test cards (3 in row):**

| Test | Procedure | Pass | Fail | Standard |
|---|---|---|---|---|
| FERROXYL | K3Fe(CN)6 solution on surface | No blue spots in 15 min | Blue = free iron | ASTM A380 |
| COPPER SULFATE | CuSO4 swab, wait 6 min | No copper (pink) deposit | Copper = active iron | ASTM A967/A380 |
| ESCA/XPS | X-ray photoelectron spectroscopy | Cr:Fe > 1.5:1 (EP typically 3:1+) | Below target | Research/high-spec |

**Documentation checklist (Emerald accent):**

Left column:
```
[ ] Part ID / serial number
[ ] Alloy grade (e.g., 316L)
[ ] EP process parameters (CD, time, temp)
[ ] Pre-EP surface condition (starting Ra)
[ ] Post-EP Ra measurement (locations noted)
```

Right column:
```
[ ] Post-EP Rz measurement (if required)
[ ] Passivation method (citric/nitric, time, temp)
[ ] Ferroxyl test result (pass/fail)
[ ] Visual inspection result (accept/reject)
[ ] Inspector signature / date
```

**Accept / Reject panels:**

| ACCEPT (Emerald) | REJECT / REWORK (Coral) |
|---|---|
| Ra meets spec target | Ra exceeds limit |
| Uniform brightness, no defects | Pitting, orange peel, streaking |
| Ferroxyl PASS | Ferroxyl FAIL -> re-passivate |
| Copper sulfate PASS (if required) | Staining -> light re-polish may recover |
| No water spots, staining, contact marks | Contact marks -> reprocess with new fixtures |
| Dimensional tolerance met (EP removes 5--25 um/side) | Out of dimensional tolerance -> SCRAP |
| Documentation complete | |

---

## Phase 7 -- Footer

Standard. Title: `Inspection -- Surface Finish -- Electropolishing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ISO 4287; ASME B46.1; ASTM B912; ASME BPE; ASTM A967; ASTM A380. Specific acceptance criteria vary by customer specification and application. Consult your quality engineer.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION` 88pt
- [ ] Orientation strip with poster 9 of 10 highlighted
- [ ] Measurement methods matrix (8 methods)
- [ ] Surface roughness parameter definitions
- [ ] Ra/Rz target table (7 applications)
- [ ] Visual inspection guide
- [ ] Passivation test cards (3 tests)
- [ ] Documentation checklist
- [ ] Accept/reject panels
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection Surface Finish Electropolishing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
