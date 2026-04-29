---
Project: Plating Posters Inc
Poster Number: 418
Title: "Inspection & QA -- CVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 418 — Inspection and QA CVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - CVD
  - ChemicalVaporDeposition
  - Inspection
  - ThinFilm
  - ClusterTF02
  - v1
---

# Claude Chat Generation Prompt -- Poster #418
## Inspection & QA -- CVD
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
### Step 2 -- `CVD -- Stage 10 of 10 -- Thickness, Adhesion, Defects, and Documentation` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `A 24-hour CVD run produces nothing of value until it passes QA. Measure it. Test it. Document it. Then -- and only then -- ship it.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted.

---

## Phase 4 -- Thickness Measurement Hero

Y: 5.0" to 14.0".

```
PRINCIPLE: Steel ball (10-30 mm dia) rotated with
diamond paste against coated surface. Creates a
shallow crater that cuts through all coating layers
into the substrate.

MEASUREMENT: View crater under optical microscope.
Each layer appears as a concentric ring. Measure ring
diameters to calculate individual layer thicknesses.

RANGE: 0.1-50 um
ACCURACY: +/- 2-5%
DESTRUCTIVE: Yes (small crater, ~1 mm dia)
PRIMARY USE: Production QC for CVD cutting inserts
```

```
PRINCIPLE: X-ray beam excites atoms in coating.
Each element emits characteristic fluorescent X-rays.
Signal intensity correlates with thickness.

MEASUREMENT: Point measurement; automated multi-point
mapping available on benchtop XRF instruments.

RANGE: 0.01-50 um
ACCURACY: +/- 3-10% (requires calibration standards)
DESTRUCTIVE: No
LIMITATION: Cannot distinguish layers of same
element (e.g., two TiN layers in a stack)
```

```
PRINCIPLE: Cut, mount, and polish a coated sample.
View cross-section under scanning electron microscope.
Directly measure each layer thickness from image.

MEASUREMENT: Direct measurement from calibrated SEM
image. Also reveals grain structure, porosity, and
interface quality.

RANGE: 0.01-100+ um
ACCURACY: +/- 2%
DESTRUCTIVE: Yes (requires sacrificial sample)
PRIMARY USE: Detailed analysis; new recipe validation;
failure investigation
```

```
PRINCIPLE: Stylus or optical profilometer measures
step height between coated area and masked/uncoated
area on a witness coupon.

MEASUREMENT: Direct height measurement.

RANGE: 0.01-100 um
ACCURACY: +/- 1-5%
REQUIREMENT: Needs a witness coupon with a
masked (uncoated) reference area
PRIMARY USE: Process development; laboratory QC
```

---

## Phase 5 -- Adhesion Testing

Y: 15.3" to 21.5".
Section: `50-80 N for well-adhered coatings`.

```
METHOD:
Rockwell C indenter (diamond cone)
applied at 150 kgf (1471 N) load.
Indent examined under optical microscope
at 100-200x magnification.

CLASSIFICATION (HF1 to HF6):
  HF1: Fine radial cracks only -- PASS
  HF2: Slightly more cracking -- PASS
  HF3: Some coating lift at crack edges -- MARGINAL
  HF4: Significant delamination -- FAIL
  HF5: Large-area spallation -- FAIL
  HF6: Complete coating removal -- FAIL

ACCEPTANCE: HF1 to HF3 (application dependent)
```

```
METHOD:
Diamond stylus (200 um tip radius) drawn
across coating with linearly increasing
load (0 to 100-200 N).

CRITICAL LOADS RECORDED:
  Lc1: First crack (cohesive failure)
  Lc2: First delamination (adhesive failure)
  Lc3: Complete coating removal

TYPICAL VALUES (CVD on WC-Co):
  Lc2 > 50-80 N for well-adhered coatings

ADVANTAGES:
  Quantitative (force values)
  Standardized (ASTM/ISO)
  Can compare coatings objectively

DISADVANTAGES:
  Equipment expensive (~$50-100K)
  Requires trained operator
  Destructive (scratch track)
```

---

## Phase 6 -- Common Defects Matrix

Y: 22.8" to 27.8".

| Card | X | Defect | Appearance | Cause | Disposition |
|---|---|---|---|---|---|
| 1 | 0.5" | DELAMINATION | Coating peels or flakes from substrate | Eta-phase at interface; contamination; poor adhesion | REJECT. Root cause analysis. Verify cleaning, atmosphere, cooling. |
| 2 | 8.33" | EGG-SHELL CRACKING | Large visible cracks in coating; spalling | Coating too thick; cooling too fast; high CTE mismatch | REJECT. Reduce layer thickness or cooling rate. |
| 3 | 16.16" | SOOT / CARBON INCLUSIONS | Dark spots or dull areas in coating | Excess hydrocarbon precursor; CH4 cracking | REJECT if severe; light discoloration may pass after wet blasting. |

| Card | X | Defect | Appearance | Cause | Disposition |
|---|---|---|---|---|---|
| 4 | 0.5" | NON-UNIFORM THICKNESS | Thin areas on coupons; color variation | Temperature gradient; gas flow dead zones | Review if within spec (+/- 15%). Adjust tray loading. |
| 5 | 8.33" | WRONG Al2O3 PHASE | Incorrect color or performance in cutting test | Nucleation pulse error; kappa instead of alpha | REJECT for critical applications. Verify nucleation protocol. |
| 6 | 16.16" | COBALT DEPLETION | Brittle interface; premature tool failure in use | HCl attack on Co binder at high temp | Switch to MT-CVD for inner layers; add protective interlayer. |

---

## Phase 7 -- Batch Documentation

Y: 28.8" to 32.3".

```
[ ] Batch number and date
[ ] Substrate material and grade
[ ] Recipe ID and revision
[ ] Thermocouple readings (all zones, log)
[ ] Gas flow rates (MFC log data)
[ ] Deposition time per layer
[ ] Cooling rate and atmosphere
```

```
[ ] Witness coupon thickness (calotest or XRF)
[ ] Adhesion test results (VDI 3198 class)
[ ] Visual inspection (pass/fail per defect matrix)
[ ] Post-treatment parameters (blast pressure, time)
[ ] Non-conformance report (if applicable)
[ ] Operator signature and date
[ ] Release to packaging
```

---

## Phase 8 -- Footer

Standard. Title: `Inspection & QA -- CVD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: Watson Research Brief (Cluster 2); VDI 3198; ASTM C1624; ISO 20502. Acceptance criteria are application-dependent -- verify against customer specification.`

---

## Phase 9 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection & QA CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
