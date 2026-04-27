---
Project: Plating Posters Inc
Poster Number: 438
Title: "Characterization & QA -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.7-4.8)"
Technical Source: ALD post-deposition characterization -- ex-situ thickness measurement (ellipsometry, XRR), composition analysis (XPS, SIMS), conformality verification (TEM/SEM cross-section), and the quality metrics that determine whether an ALD film meets specification. ALD inspection differs from PVD/CVD because the films are 1-100 nm -- most traditional coating inspection methods (calotest, micrometer) are useless at this scale.
Process Scope: ALD characterization and quality assurance (Stage 10 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ALD
  - Characterization
  - QualityAssurance
  - Ellipsometry
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #438 -- Construction Workup
## Characterization & QA -- ALD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of 10. ALD films are measured in nanometers, not micrometers. The characterization toolbox is completely different from the calotest-and-micrometer world of CVD and PVD. Ellipsometry is the workhorse. XRR provides thickness + density + roughness. XPS and SIMS reveal composition and impurities. TEM cross-sections confirm conformality in 3D structures. This poster maps the full characterization workflow and the acceptance criteria that close out an ALD run.

Hero visual: characterization method comparison matrix -- six methods with their capabilities, accuracy, and use cases.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Characterization method matrix (Block B -- HERO):** Six-method comparison grid.
2. **Ellipsometry deep-dive (Block C):** How wafer mapping works.
3. **Conformality verification (Block D):** TEM cross-section explanation.
4. **Common ALD defects (Block E):** Defect identification table.
5. **Acceptance criteria and documentation (Block F):** What closes out a run.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 10 highlighted (Amber)
ZONE 3 -- CHARACTERIZATION METHOD MATRIX HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ELLIPSOMETRY MAPPING + CONFORMALITY (14.5"--22.0" / ~7.5")
ZONE 5 -- COMMON DEFECTS (22.0"--28.0" / ~6.0")
ZONE 6 -- ACCEPTANCE CRITERIA + DOCUMENTATION (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CHARACTERIZATION & QA` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 10 of 10 -- Measuring Films One Nanometer at a Time` -- 28 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `You cannot use a micrometer on a 10 nm film. ALD characterization demands optical, X-ray, and electron-beam techniques. The precision of the measurement must match the precision of the deposition.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 10 (`Characterization & QA`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: Substrate unloaded, ALD film deposited (Stage 9) --> Output: Film characterized, accepted or rejected, documentation complete`

---

### ZONE 3 -- Characterization Method Matrix Hero

**Section label:** `CHARACTERIZATION METHODS -- THE ALD TOOLBOX` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Six-Method Grid (Y: 5.0" to 14.0")**

Two rows of three panels. Each panel: Rounded rect W: 7.33", H: 4.2", fill `#1E2435`, radius 6.

**Row 1 (Y: 5.0"):**

Panel 1 -- SPECTROSCOPIC ELLIPSOMETRY (X: 0.5"):
- Top accent 4 pt `#E8A020`
- Title: `ELLIPSOMETRY` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

Panel 2 -- X-RAY REFLECTIVITY (XRR) (X: 8.33"):
- Top accent 4 pt `#2EC4B6`
- Title: `XRR (X-RAY REFLECTIVITY)` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

Panel 3 -- XPS (X-RAY PHOTOELECTRON SPECTROSCOPY) (X: 16.16"):
- Top accent 4 pt `#27AE60`
- Title: `XPS` Barlow SemiBold 18 pt `#27AE60`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

**Row 2 (Y: 9.5"):**

Panel 4 -- SIMS (X: 0.5"):
- Top accent 4 pt `#E05C5C`
- Title: `SIMS` Barlow SemiBold 18 pt `#E05C5C`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

Panel 5 -- TEM CROSS-SECTION (X: 8.33"):
- Top accent 4 pt `#E8A020`
- Title: `TEM CROSS-SECTION` Barlow SemiBold 16 pt `#E8A020`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

Panel 6 -- SEM (X: 16.16"):
- Top accent 4 pt `#2EC4B6`
- Title: `SEM CROSS-SECTION` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 12 pt `#F0EDE8`):
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

### ZONE 4 -- Ellipsometry Mapping + Conformality

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Wafer Mapping (X: 0.5", W: 11.0")**

**Section label:** `ELLIPSOMETRY WAFER MAP` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Mapping Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
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

Conceptual wafer map (circular diagram):
- Circle representing wafer, `#3A4055` fill
- 49 measurement points shown as dots
- Color gradient from center to edge showing thickness variation
- Legend: `Blue = thin, Green = on-target, Red = thick`

**Right -- Conformality Verification (X: 12.0", W: 11.5")**

**Section label:** `CONFORMALITY -- THE ALD ADVANTAGE` -- Y: 14.7".

**BLOCK D -- Conformality Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
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

Key stat:
- Rounded rect, fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `ALD achieves > 99% step coverage in structures with aspect ratios > 100:1. No other deposition method can do this.` Barlow SemiBold 12 pt `#27AE60`

---

### ZONE 5 -- Common ALD Defects

**Section label:** `COMMON ALD DEFECTS` -- Y: 22.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Five-Defect Table (Y: 22.8" to 27.5")**

| Defect | Symptom | Root Cause | Prevention |
|---|---|---|---|
| Non-self-limiting growth (GPC too high) | Thickness above target; poor uniformity | Insufficient purge; precursor overlap | Extend purge times; verify saturation curves |
| Island growth (incomplete film) | Patchy coverage; high leakage current in device testing | Surface contamination; lack of -OH nucleation sites | O2 plasma pretreatment; proper cleaning |
| Thickness non-uniformity (> 1%) | Variation across wafer map | Temperature gradient; gas depletion in reactor | Optimize heater calibration; improve gas distribution |
| High carbon (> 2 at%) | Low refractive index (Al2O3); high etch rate | Low temp (< 150 C); short purges | Increase temp into ALD window; use plasma-ALD |
| Unwanted crystallization | Changes in electrical properties; rough surface | HfO2/ZrO2 crystallize at higher ALD temps | Lower temp; use nanolaminate approach (HfO2/Al2O3 stack) |

Header: Barlow SemiBold 11 pt, fill `#3A4055`. Data: Inter Regular 11 pt `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

---

### ZONE 6 -- Acceptance Criteria + Documentation

**Section label:** `ACCEPTANCE CRITERIA & RUN DOCUMENTATION` -- Y: 28.2". Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

**Two-column layout (Y: 28.8" to 32.3"):**

**Left -- Acceptance Criteria (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

| Parameter | Semiconductor | Industrial/Solar |
|---|---|---|
| Thickness | +/- 1% of target | +/- 5% of target |
| Uniformity | < 1% (49-pt map) | < 3% |
| Refractive index (Al2O3) | 1.62-1.65 | 1.60-1.66 |
| Carbon content | < 2 at% | < 5 at% |
| Conformality | > 95% (test structure) | Visual SEM pass |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Documentation Checklist (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`.

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

JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Characterization & QA -- ALD`. Version `v1.0 -- 2026`.

Disclaimer: `Source: Watson Research Brief (Cluster 4); George, S.M., Chemical Reviews (2010). Acceptance criteria vary by application -- verify against customer or device specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Characterization QA ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The six-method characterization matrix as hero reflects the reality that ALD QA requires a fundamentally different toolbox than traditional coating inspection. An electroplater who walks up to this poster expecting to see a micrometer or calotest will immediately understand why ALD operates in a different world. The conformality section with its step coverage ratio is ALD's "killer feature" and deserves the visual emphasis it gets here.

This poster closes out the ALD cluster. Together, Posters 429-438 give a complete picture of ALD from process flow through characterization -- enough for an engineer to understand the process, set up a reactor, run a deposition, and verify the result.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #438 -- Construction Workup v1.0*
*2026-04-26*
