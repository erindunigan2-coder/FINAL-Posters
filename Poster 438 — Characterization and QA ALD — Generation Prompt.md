---
Project: Plating Posters Inc
Poster Number: 438
Title: "Characterization & QA -- ALD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 438 — Characterization and QA ALD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - Inspection
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #438
## Characterization & QA -- ALD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `CHARACTERIZATION & QA` -- `72` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 10 of 10 -- Measuring Films One Nanometer at a Time` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `You cannot use a micrometer on a 10 nm film. ALD characterization demands optical, X-ray, and electron-beam techniques. The precision of the measurement must match the precision of the deposition.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted.

---

## Phase 4 -- Characterization Method Matrix Hero

Y: 5.0" to 14.0".
Section: `20 nm.`.

```
MEASURES: Thickness, refractive index (n),
extinction coefficient (k)
ACCURACY: +/- 0.1 nm thickness; +/- 0.01 n
RANGE: 0.5 nm to 10+ um
DESTRUCTIVE: No
SPEED: 1-5 sec per point

THE WORKHORSE for ALD QA.
Single-point or 49-point wafer map.
Requires optical model fitting.
Works on flat, reflective substrates.
```

```
MEASURES: Thickness, density, roughness
ACCURACY: +/- 0.1 nm thickness
RANGE: 1-200 nm
DESTRUCTIVE: No
SPEED: 10-30 min per scan

Gold standard for ultra-thin films.
Measures density independently of
thickness (ellipsometry cannot).
Requires flat substrate.
```

```
MEASURES: Elemental composition,
chemical bonding states
ACCURACY: +/- 0.5 at% for major elements
DEPTH: Top 1-10 nm (surface technique)
DESTRUCTIVE: No (surface only);
  depth profiling requires Ar ion sputtering

Key for detecting carbon contamination
(< 2 at% target for good Al2O3).
Identifies bonding states (Al-O vs Al-C).
```

```
MEASURES: Trace impurities, depth profile
SENSITIVITY: ppb to ppm level
RANGE: Full film depth + into substrate
DESTRUCTIVE: Yes (sputters through film)

Detects trace metallic contamination
and light elements (H, C, N, O).
Reveals impurity distribution through
the film thickness. Expensive -- used
for process development, not routine QA.
```

```
MEASURES: Direct visual of film on 3D
structures; conformality; interface quality
RESOLUTION: Sub-nm (atomic resolution)
DESTRUCTIVE: Yes (requires FIB sample prep)
SPEED: Hours (sample prep + imaging)

THE CONFORMALITY PROOF.
Only method that directly shows whether
ALD coated the bottom of a 100:1 trench
as well as the top. Critical for
semiconductor process qualification.
```

```
MEASURES: Film thickness on cross-section;
surface morphology (top-down)
RESOLUTION: 1-5 nm (field-emission SEM)
DESTRUCTIVE: Yes (requires cleaving/FIB)
SPEED: 30-60 min

Faster and cheaper than TEM but lower
resolution. Good for films > 20 nm.
Sufficient for industrial ALD QA.
For ultra-thin films (< 10 nm), TEM
is required.
```

---

## Phase 5 -- Ellipsometry Mapping + Conformality

Y: 14.5" to 21.8".
Section: `95% (often > 99%)`.

```
A 49-POINT MAP measures thickness at 49
positions across the wafer (or substrate).

FROM THE MAP:
- Average thickness: e.g., 10.2 nm
- Std deviation: e.g., 0.08 nm
- Non-uniformity: (max - min) / (2 x avg)
  Target: < 1% for semiconductor
  Target: < 3% for industrial/solar

WHAT THE MAP REVEALS:
- Center-to-edge gradient:
  indicates gas depletion or temperature
  gradient in reactor
- Edge exclusion zone:
  typically 3-5 mm from wafer edge
  excluded from uniformity calculation
- Local thin spots:
  indicate contamination or fixture shadow
```

```
STEP COVERAGE = thickness at bottom of feature
               / thickness at top of feature

ALD TARGET: > 95% (often > 99%)
PVD COMPARISON: 10-50% in same geometry
CVD COMPARISON: 50-90% in same geometry

HOW TO VERIFY:
1. Prepare test structure with known
   aspect ratio (e.g., 10:1, 50:1, 100:1)
2. Deposit ALD film
3. FIB cross-section through feature
4. Image by TEM or high-res SEM
5. Measure film thickness at:
   - Top of feature
   - Sidewall (mid-depth)
   - Bottom of feature
6. Calculate step coverage ratio

WHY IT MATTERS:
Semiconductor devices have features with
aspect ratios > 100:1. If ALD cannot coat
the bottom, the device fails.
```

---

## Phase 6 -- Common ALD Defects

Y: 22.8" to 27.5".
Section: `1%) | Variation across wafer map | Temperature gradient; gas depletion in reactor | Optimize heater calibration; improve gas distribution |`.

| Defect | Symptom | Root Cause | Prevention |
|---|---|---|---|
| Non-self-limiting growth (GPC too high) | Thickness above target; poor uniformity | Insufficient purge; precursor overlap | Extend purge times; verify saturation curves |
| Island growth (incomplete film) | Patchy coverage; high leakage current in device testing | Surface contamination; lack of -OH nucleation sites | O2 plasma pretreatment; proper cleaning |
| Thickness non-uniformity (> 1%) | Variation across wafer map | Temperature gradient; gas depletion in reactor | Optimize heater calibration; improve gas distribution |
| High carbon (> 2 at%) | Low refractive index (Al2O3); high etch rate | Low temp (< 150 C); short purges | Increase temp into ALD window; use plasma-ALD |
| Unwanted crystallization | Changes in electrical properties; rough surface | HfO2/ZrO2 crystallize at higher ALD temps | Lower temp; use nanolaminate approach (HfO2/Al2O3 stack) |

---

## Phase 7 -- Acceptance Criteria + Documentation

Y: 28.8" to 32.3".
Section: `95% (test structure) | Visual SEM pass |`.

| Parameter | Semiconductor | Industrial/Solar |
|---|---|---|
| Thickness | +/- 1% of target | +/- 5% of target |
| Uniformity | < 1% (49-pt map) | < 3% |
| Refractive index (Al2O3) | 1.62-1.65 | 1.60-1.66 |
| Carbon content | < 2 at% | < 5 at% |
| Conformality | > 95% (test structure) | Visual SEM pass |

```
[ ] Recipe ID, version, and cycle count
[ ] Substrate ID and pre-deposition condition
[ ] In-situ monitoring data (ellipsometry/QCM)
[ ] Post-deposition thickness (49-pt map)
[ ] Refractive index
[ ] Composition (XPS) if required
[ ] Conformality verification (if 3D substrates)
[ ] Non-conformance report (if any metric fails)
[ ] Operator signature and date
```

---

## Phase 8 -- Footer

Standard. Title: `Characterization & QA -- ALD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: Watson Research Brief (Cluster 4); George, S.M., Chemical Reviews (2010). Acceptance criteria vary by application -- verify against customer or device specification.`

---

## Phase 9 -- Review

- [ ] Headline `CHARACTERIZATION & QA` 72pt
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Characterization & QA ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
