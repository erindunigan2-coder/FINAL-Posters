---
Project: Plating Posters Inc
Poster Number: 467
Title: "Inspection -- Surface Finish -- Electropolishing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7, Sections 7.6--7.8)"
Technical Source: Post-electropolishing inspection and surface finish measurement. Covers Ra/Rz profilometry, visual inspection, glossmeter readings, passivation verification, and documentation requirements per ASTM B912, ASME BPE, and SEMI F19.
Process Scope: Electropolishing -- inspection and surface finish verification (Stage 8b of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electropolishing
  - Inspection
  - SurfaceFinish
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #467 -- Construction Workup
## Inspection -- Surface Finish -- Electropolishing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Inspection is where all the work comes together -- or falls apart. Electropolished surfaces are measured to tighter specifications than almost any other metal finish. Ra values in the sub-micrometer range, Cr:Fe ratio verification by XPS, ferroxyl testing for free iron -- the QC toolkit for EP is extensive. This poster gives the quality engineer and inspector a complete field reference for what to measure, how to measure it, and what specs to reference.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Measurement methods matrix (Block B -- HERO):** Comprehensive table of measurement techniques with application, accuracy, and standard references.
2. **Ra/Rz specification table (Block D):** Target values by industry/application.
3. **Visual inspection guide (Block E):** What to look for under different lighting conditions.
4. **Passivation verification (Block F):** Ferroxyl, copper sulfate, and ESCA/XPS summary.
5. **Documentation checklist (Block G):** What records to keep.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber) -- Inspect portion
ZONE 3 -- MEASUREMENT METHODS HERO (4.2"--15.0" / ~10.8")
  Block B: Measurement methods matrix
  Block C: Profilometer parameter definitions
ZONE 4 -- SPECIFICATION TARGETS (15.0"--21.5" / ~6.5")
  Block D: Ra/Rz targets by industry
  Block E: Visual inspection guide
ZONE 5 -- PASSIVATION VERIFICATION + DOCUMENTATION (21.5"--27.5" / ~6.0")
  Block F: Passivation test summary
  Block G: Documentation checklist
ZONE 6 -- ACCEPTANCE / REJECTION (27.5"--32.5" / ~5.0")
  Block H: Accept/reject decision tree
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electropolishing -- Surface Finish Verification & Quality Control` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Ra, Rz, Cr:Fe ratio, ferroxyl, visual -- the complete QC toolkit for electropolished surfaces. Measure what matters. Document everything.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Label: `Dry / Inspect`. Others dimmed.

Below: `Before: Dried, passivated electropolished surface --> After: Measured, documented, accepted/rejected per specification` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Measurement Methods Hero

**Section label:** `SURFACE FINISH MEASUREMENT METHODS` -- Y: 4.4".

---

**BLOCK B -- Measurement Methods Matrix (Y: 5.0" to 12.0")**

Table -- columns: Method (4.5") | What It Measures (4.5") | Range (3.0") | Accuracy (2.5") | Destructive? (2.0") | Standard (3.0") | Notes (3.5")

Header row: Rectangle fill `#3A4055`, H: 0.6". Barlow SemiBold, 13 pt, `#F0EDE8`.

| Method | What It Measures | Range | Accuracy | Destr.? | Standard | Notes |
|---|---|---|---|---|---|---|
| Stylus profilometer | Ra, Rz, Rq, Rmax surface roughness | 0.005--50 um | +/- 5--10% | No (minor trace) | ISO 4287, ASME B46.1 | Primary QC tool; most widely specified |
| Optical profilometer | Ra, Rz, 3D topography | 0.001--50 um | +/- 2--5% | No | ISO 25178 | Non-contact; ideal for soft metals |
| Glossmeter | Surface reflectivity / gloss | 0--1000 GU | +/- 2 GU | No | ASTM D523 | Correlates to visual appearance |
| ESCA / XPS | Surface composition (Cr:Fe ratio, oxide thickness) | Top 1--10 nm | Quantitative | No | -- | Passive layer analysis; pharma/research |
| Ferroxyl test | Free iron on surface | Pass/fail | Qualitative | No | ASTM A380 | Passivation verification |
| Copper sulfate test | Free iron on surface | Pass/fail | Qualitative | No | ASTM A967, A380 | Passivation verification |
| Water-break test | Surface cleanliness | Pass/fail | Qualitative | No | Visual | Contamination screening |
| Weight loss | Average material removal | mg/cm2 | +/- 1% | No | Gravimetric | Calculates avg removal depth |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Alternating rows: `#1E2435` / `#252B3D`.

---

**BLOCK C -- Profilometer Parameter Definitions (Y: 12.5" to 14.5")**

Rounded rect, X: 0.5", W: 23.0", H: 1.8", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `KEY SURFACE ROUGHNESS PARAMETERS` Barlow SemiBold 18 pt `#2EC4B6`

Four definitions in a row (JetBrains Mono 13 pt `#F0EDE8`):

| Parameter | Definition |
|---|---|
| **Ra** | Arithmetic average of surface deviations from the mean line. Most commonly specified. |
| **Rz** | Average of the five highest peaks to five deepest valleys. More sensitive to extreme features. |
| **Rq** | Root mean square of surface deviations. Statistically more rigorous than Ra. |
| **Rmax** | Maximum peak-to-valley height in the evaluation length. Catches worst-case defects. |

Inter Regular 12 pt `#F0EDE8` at 80% for definitions.

---

### ZONE 4 -- Specification Targets

**Section label:** `TARGET VALUES BY APPLICATION` -- Y: 15.2".

---

**BLOCK D -- Ra/Rz Target Table (Y: 15.8" to 19.5")**

Table -- columns: Application (5.0") | Ra Target (um) (3.5") | Ra Target (uin) (3.0") | Rz Typical (um) (3.0") | Spec / Standard (5.0") | Notes (3.5")

| Application | Ra (um) | Ra (uin) | Rz (um) | Spec | Notes |
|---|---|---|---|---|---|
| General industrial | < 0.8 | < 32 | < 3.2 | Customer spec | Visible brightness improvement |
| Food/beverage (3A) | < 0.8 | < 32 | < 3.2 | 3-A 605-04 | Sanitary finish requirement |
| Pharma (ASME BPE SF4) | < 0.5 | < 20 | < 2.5 | ASME BPE | Standard EP finish |
| Pharma high-purity | < 0.25 | < 10 | < 1.5 | ASME BPE SF6 | Premium EP finish; multi-step process |
| Semiconductor | < 0.25 | < 10 | < 1.0 | SEMI F19 | Ultra-clean surface |
| Medical implants | < 0.4 | < 16 | < 2.0 | ASTM F86 | Biocompatible finish |
| Decorative (mirror) | < 0.1 | < 4 | < 0.5 | Visual | Requires excellent starting surface |

Header: `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`.

Bottom note: `Ra conversion: 1 um = 39.37 uin. Rz is typically 4--6x Ra for electropolished surfaces.` Inter Medium 12 pt `#F0EDE8` at 60%

---

**BLOCK E -- Visual Inspection Guide (Y: 20.0" to 21.3")**

Rounded rect, X: 0.5", W: 23.0", H: 1.1", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `VISUAL INSPECTION` Barlow SemiBold 16 pt `#E8A020`

Text (Inter Regular 13 pt `#F0EDE8`):

> Inspect under diffuse white light (fluorescent or LED) at 18--24 inches. Rotate part to catch reflections at multiple angles. Look for: orange peel texture, pitting, streaking, staining, uneven brightness, contact marks from fixturing, and water spots. For critical applications, inspect under both direct and diffuse lighting. Document any deviations with photographs.

---

### ZONE 5 -- Passivation Verification + Documentation

**Section label:** `PASSIVATION VERIFICATION & DOCUMENTATION` -- Y: 21.7".

---

**BLOCK F -- Passivation Test Summary (Y: 22.3" to 25.5")**

Three compact cards in a row:

**Card 1 -- Ferroxyl (X: 0.5", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `FERROXYL` Barlow SemiBold 14 pt `#2EC4B6`
- Body (Inter Regular 12 pt `#F0EDE8`):
```
K3Fe(CN)6 solution applied to surface
PASS = no blue spots in 15 min
Tests for free iron (surface contamination)
Most common passivation QC test
Per ASTM A380
```

**Card 2 -- Copper Sulfate (X: 8.33", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#E8A020`
- Title: `COPPER SULFATE` Barlow SemiBold 14 pt `#E8A020`
- Body (Inter Regular 12 pt `#F0EDE8`):
```
CuSO4 solution swabbed on surface
PASS = no copper (pink) deposit in 6 min
Tests for active iron (passive layer integrity)
Per ASTM A967 / A380
300 and 400 series SS
```

**Card 3 -- ESCA/XPS (X: 16.16", W: 7.33"):**
- Rounded rect, H: 2.8", fill `#1E2435`, left accent `#27AE60`
- Title: `ESCA / XPS` Barlow SemiBold 14 pt `#27AE60`
- Body (Inter Regular 12 pt `#F0EDE8`):
```
X-ray photoelectron spectroscopy
Quantifies Cr:Fe ratio at surface
Target: Cr:Fe > 1.5:1 (EP typically 3:1+)
Measures passive oxide layer thickness
Research / high-spec QC only (expensive)
```

---

**BLOCK G -- Documentation Checklist (Y: 26.0" to 27.3")**

Rounded rect, X: 0.5", W: 23.0", H: 1.1", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `EP INSPECTION DOCUMENTATION CHECKLIST` Barlow SemiBold 16 pt `#27AE60`

Checklist (two columns, Inter Regular 13 pt `#F0EDE8`):

Left:
```
[ ] Part ID / serial number
[ ] Alloy grade (e.g., 316L)
[ ] EP process parameters (CD, time, temp)
[ ] Pre-EP surface condition (starting Ra)
[ ] Post-EP Ra measurement (locations noted)
```

Right:
```
[ ] Post-EP Rz measurement (if required)
[ ] Passivation method (citric/nitric, time, temp)
[ ] Ferroxyl test result (pass/fail)
[ ] Visual inspection result (accept/reject)
[ ] Inspector signature / date
```

---

### ZONE 6 -- Acceptance / Rejection

**Section label:** `ACCEPT / REJECT DECISION` -- Y: 27.7".

---

**BLOCK H -- Decision Guide (Y: 28.3" to 32.0")**

Two side-by-side panels:

**Left -- Accept Criteria (X: 0.5", W: 11.0"):**
- Rounded rect, H: 3.5", fill `#27AE60` at 10%, border 1 pt `#27AE60`
- Title: `ACCEPT WHEN:` Barlow SemiBold 18 pt `#27AE60`
- List (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
- Ra meets or exceeds specification target
- Visual: uniform brightness, no defects visible
- Ferroxyl test: PASS (no blue spots)
- Copper sulfate test: PASS (if required)
- No water spots, staining, or contact marks
- Dimensional tolerance still within spec
  (EP removes 5--25 um per side)
- Documentation complete
```

**Right -- Reject / Rework Criteria (X: 12.0", W: 11.5"):**
- Rounded rect, H: 3.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Title: `REJECT / REWORK WHEN:` Barlow SemiBold 18 pt `#E05C5C`
- List (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
- Ra exceeds specification limit
- Visible pitting, orange peel, streaking
- Ferroxyl test: FAIL (free iron present)
  --> Re-passivate and re-test
- Staining or discoloration
  --> Light re-polish may recover
- Contact marks in critical areas
  --> Re-process with repositioned fixtures
- Out of dimensional tolerance
  --> SCRAP (cannot add material back)
```

---

### ZONE 7 -- Footer

Standard. Title: `Inspection -- Surface Finish -- Electropolishing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ISO 4287; ASME B46.1; ASTM B912; ASME BPE; ASTM A967; ASTM A380. Specific acceptance criteria vary by customer specification and application. Consult your quality engineer.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Surface Finish Electropolishing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the quality engineer's poster -- the one that hangs in the QC lab, not on the shop floor. The measurement methods matrix (Block B) is the most reference-dense element: seven rows of instrumentation with accuracy, range, and standard references. The Ra/Rz target table (Block D) is what the inspector reaches for when a PO comes in. The accept/reject panels (Zone 6) give immediate actionable guidance. The dimensional tolerance warning in the reject panel is critical -- EP removes material, and unlike plating, you cannot add it back.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #467 -- Construction Workup v1.0*
*2026-04-26*
