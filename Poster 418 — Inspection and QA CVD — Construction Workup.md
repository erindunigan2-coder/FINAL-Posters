---
Project: Plating Posters Inc
Poster Number: 418
Title: "Inspection & QA -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.8)"
Technical Source: CVD inspection and quality assurance -- thickness measurement (calotest, XRF, SEM cross-section), adhesion testing (Rockwell HRC indent per VDI 3198, scratch test), common defect identification and root cause analysis. Post-deposition quality gates that determine whether a batch ships or gets recoated.
Process Scope: CVD inspection and quality assurance (Stage 10 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #418 -- Construction Workup
## Inspection & QA -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of 10. The final gate. Every batch of CVD-coated inserts must pass thickness, adhesion, visual, and (in many cases) performance testing before it ships. This poster covers the measurement methods, acceptance criteria, the common defects table that QA inspectors reference daily, and the documentation requirements that close out each production batch.

Hero visual: the defect identification matrix -- a visual grid of common CVD defects with photos/illustrations, causes, and dispositions.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Thickness measurement methods (Block B -- HERO):** Comparison of calotest, XRF, SEM cross-section, and profilometry with accuracy and use cases.
2. **Adhesion testing (Block C):** Rockwell HRC indent classification (VDI 3198) and scratch test.
3. **Common defects matrix (Block D):** Six-defect identification grid.
4. **Batch documentation checklist (Block E):** What records close out a CVD run.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 10 highlighted (Amber -- inspection)
ZONE 3 -- THICKNESS MEASUREMENT HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ADHESION TESTING (14.5"--22.0" / ~7.5")
ZONE 5 -- COMMON DEFECTS MATRIX (22.0"--28.0" / ~6.0")
ZONE 6 -- BATCH DOCUMENTATION (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 10 of 10 -- Thickness, Adhesion, Defects, and Documentation` -- 28 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `A 24-hour CVD run produces nothing of value until it passes QA. Measure it. Test it. Document it. Then -- and only then -- ship it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 10 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts cooled, post-treated, ready for QA (Stage 9) --> After: Batch approved, documented, packaged for shipment`

---

### ZONE 3 -- Thickness Measurement Hero

**Section label:** `THICKNESS MEASUREMENT -- HOW THICK IS THE COATING?` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Four Measurement Method Panels (Y: 5.0" to 14.0")**

Four panels in a 2x2 grid:

**Panel 1 -- Calotest / Ball Crater (X: 0.5", Y: 5.0", W: 11.0", H: 4.2"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `CALOTEST (BALL CRATER)` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):
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

**Panel 2 -- XRF (X: 12.0", Y: 5.0", W: 11.5", H: 4.2"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `X-RAY FLUORESCENCE (XRF)` Barlow SemiBold 18 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`):
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

**Panel 3 -- SEM Cross-Section (X: 0.5", Y: 9.5", W: 11.0", H: 4.2"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `SEM CROSS-SECTION` Barlow SemiBold 18 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`):
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

**Panel 4 -- Profilometry / Step Height (X: 12.0", Y: 9.5", W: 11.5", H: 4.2"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `PROFILOMETRY (STEP HEIGHT)` Barlow SemiBold 18 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`):
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

### ZONE 4 -- Adhesion Testing

**Section label:** `ADHESION TESTING -- DOES THE COATING STICK?` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Two-column layout (Y: 15.3" to 21.5"):**

**Left -- Rockwell Indent Test (X: 0.5", W: 11.0")**

**BLOCK C1 -- Rockwell Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Title: `ROCKWELL INDENT TEST (VDI 3198)` Barlow SemiBold 18 pt `#E8A020`

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
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

Bottom note:
- `This is the workhorse adhesion test for PVD and CVD hard coatings in the cutting tool industry. Fast, cheap, and tells you immediately if something went wrong.` Inter Medium 12 pt `#2EC4B6`

**Right -- Scratch Test (X: 12.0", W: 11.5")**

**BLOCK C2 -- Scratch Test Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Title: `SCRATCH TEST (ASTM C1624 / ISO 20502)` Barlow SemiBold 16 pt `#2EC4B6`

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
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

### ZONE 5 -- Common Defects Matrix

**Section label:** `DEFECT IDENTIFICATION MATRIX` -- Y: 22.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Six-Defect Grid (Y: 22.8" to 27.8")**

Two rows of three cards. Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 6.

Row 1 (Y: 22.8"):

| Card | X | Defect | Appearance | Cause | Disposition |
|---|---|---|---|---|---|
| 1 | 0.5" | DELAMINATION | Coating peels or flakes from substrate | Eta-phase at interface; contamination; poor adhesion | REJECT. Root cause analysis. Verify cleaning, atmosphere, cooling. |
| 2 | 8.33" | EGG-SHELL CRACKING | Large visible cracks in coating; spalling | Coating too thick; cooling too fast; high CTE mismatch | REJECT. Reduce layer thickness or cooling rate. |
| 3 | 16.16" | SOOT / CARBON INCLUSIONS | Dark spots or dull areas in coating | Excess hydrocarbon precursor; CH4 cracking | REJECT if severe; light discoloration may pass after wet blasting. |

Row 2 (Y: 25.3"):

| Card | X | Defect | Appearance | Cause | Disposition |
|---|---|---|---|---|---|
| 4 | 0.5" | NON-UNIFORM THICKNESS | Thin areas on coupons; color variation | Temperature gradient; gas flow dead zones | Review if within spec (+/- 15%). Adjust tray loading. |
| 5 | 8.33" | WRONG Al2O3 PHASE | Incorrect color or performance in cutting test | Nucleation pulse error; kappa instead of alpha | REJECT for critical applications. Verify nucleation protocol. |
| 6 | 16.16" | COBALT DEPLETION | Brittle interface; premature tool failure in use | HCl attack on Co binder at high temp | Switch to MT-CVD for inner layers; add protective interlayer. |

Interior per card:
- Defect name: Barlow SemiBold 14 pt `#E05C5C`
- Appearance: Inter Regular 11 pt `#F0EDE8`
- Cause: Inter Regular 11 pt `#F0EDE8` at 70%
- Disposition: Inter Medium 11 pt `#27AE60`

---

### ZONE 6 -- Batch Documentation

**Section label:** `BATCH DOCUMENTATION CHECKLIST` -- Y: 28.2". Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

**BLOCK E -- Checklist (Y: 28.8" to 32.3")**

Two columns of checklist items in a rounded rect, fill `#1E2435`.

Left (X: 0.5", W: 11.0"):
```
[ ] Batch number and date
[ ] Substrate material and grade
[ ] Recipe ID and revision
[ ] Thermocouple readings (all zones, log)
[ ] Gas flow rates (MFC log data)
[ ] Deposition time per layer
[ ] Cooling rate and atmosphere
```

Right (X: 12.0", W: 11.5"):
```
[ ] Witness coupon thickness (calotest or XRF)
[ ] Adhesion test results (VDI 3198 class)
[ ] Visual inspection (pass/fail per defect matrix)
[ ] Post-treatment parameters (blast pressure, time)
[ ] Non-conformance report (if applicable)
[ ] Operator signature and date
[ ] Release to packaging
```

JetBrains Mono 12 pt `#F0EDE8`.

Bottom callout:
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `A complete batch record is the only proof that the coating was made correctly. If it is not documented, it did not happen.` Inter Medium 14 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- CVD`. Version `v1.0 -- 2026`.

Disclaimer: `Source: Watson Research Brief (Cluster 2); VDI 3198; ASTM C1624; ISO 20502. Acceptance criteria are application-dependent -- verify against customer specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The four-panel thickness measurement comparison (Zone 3) is the hero because "how thick is the coating" is the single most-asked question in any coating shop. Presenting all four methods with their accuracy, range, and destructive/non-destructive status gives QA inspectors a quick reference for choosing the right tool.

The VDI 3198 Rockwell indent test gets prominent placement because it is the go-to field test -- fast, cheap, and immediately interpretable. The HF1-HF6 classification is something every cutting tool coating operator should know by heart.

The defect matrix closes out the cluster by giving operators a visual dictionary of what can go wrong and what to do about it. This is the poster they will reference most during production troubleshooting.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #418 -- Construction Workup v1.0*
*2026-04-26*
