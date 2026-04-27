---
Project: Plating Posters Inc
Poster Number: 548
Title: "Inspection & QA -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS QA focuses on confirming columnar microstructure (SEM cross-section), porosity within 10--25% (ASTM E2109), thickness 100--400 um, bond strength > 10 MPa (modified ASTM C633), thermal cycling life > 1000 cycles, thermal conductivity 0.7--1.2 W/mK (laser flash ASTM E1461), and tetragonal prime ZrO2 phase stability (XRD). SEM is preferred over optical for SPS microstructure evaluation due to finer features.
Process Scope: SPS coating inspection, quality assurance, and acceptance testing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Inspection
  - QA
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #548 -- Construction Workup
## Inspection & QA -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

SPS inspection is more demanding than conventional APS because the microstructure features are finer and the acceptance criteria are different. You are not just checking thickness and bond strength -- you are confirming that the columnar structure actually formed. SEM cross-section is the gold standard. XRD phase analysis confirms no monoclinic zirconia (which would mean the coating is destabilized). Thermal cycling is the ultimate performance test. Hero visual: the test matrix with methods and acceptance criteria.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- TEST MATRIX / HERO (2.9"--15.5")
  Block B: Full inspection test table with methods and acceptance criteria
ZONE 3 -- MICROSTRUCTURE EVALUATION (15.5"--22.0")
  Block C: SEM cross-section evaluation criteria
  Block D: "What Good Looks Like" vs. "What Bad Looks Like" callout
ZONE 4 -- PHASE STABILITY + THERMAL CYCLING (22.0"--28.5")
  Block E: XRD phase analysis (tetragonal prime vs. monoclinic)
  Block F: Thermal cycling test protocol
ZONE 5 -- ACCEPTANCE / REJECTION STRIP (28.5"--32.5")
  Block G: 4 rejection criteria cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Suspension Plasma Spray (SPS) -- Confirming Columnar Structure & Performance` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `You can measure thickness and bond strength on any coating. SPS demands more -- you must confirm the columnar microstructure actually formed. SEM is your primary tool.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Test Matrix (HERO)

**Section label:** `SPS INSPECTION TEST MATRIX` -- Y: 3.1".

**BLOCK B -- Full Test Table**

Y: 3.8" to 15.3". Column widths (23.0" total):
- Test (4.5") | Method / Standard (6.0") | Acceptance Criteria (7.0") | Priority (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Test | Method / Standard | Acceptance Criteria | Priority |
|---|---|---|---|
| Microstructure | Metallographic cross-section (SEM preferred) | Columnar morphology confirmed; no lamellar regions; inter-columnar gap spacing visible | `#E05C5C` CRITICAL |
| Porosity | ASTM E2109 (image analysis on cross-section) | 10--25% (intentional; within spec range) | `#E05C5C` CRITICAL |
| Thickness | Metallographic or eddy current | Per spec; typically 100--400 um (SPS topcoat) | `#E8A020` REQUIRED |
| Bond Strength | Modified ASTM C633 (small-area test) | > 10 MPa (lower than APS due to finer structure) | `#E8A020` REQUIRED |
| Thermal Cycling | Furnace cycling (1100 degC / 1 hr hold / forced air cool) | > 1000 cycles to 20% spallation (target) | `#E8A020` REQUIRED |
| Thermal Conductivity | Laser flash analysis (ASTM E1461) | 0.7--1.2 W/mK (lower = better insulation) | `#2EC4B6` RECOMMENDED |
| Phase Stability | XRD (X-ray diffraction) | Tetragonal prime ZrO2 -- NO monoclinic phase | `#E05C5C` CRITICAL |
| Visual | Unaided eye + 10x loupe | Uniform coverage; no spalling, blistering, bare spots | `#E8A020` REQUIRED |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Test names: Inter Medium, 13 pt.

Priority indicators: JetBrains Mono 11 pt, color-coded per table.

---

### ZONE 3 -- Microstructure Evaluation

**Section label:** `MICROSTRUCTURE -- THE PRIMARY QUALITY INDICATOR` -- Y: 15.7".

**Left -- BLOCK C: SEM Evaluation Criteria (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `SEM CROSS-SECTION EVALUATION` -- Barlow SemiBold 20 pt `#27AE60`.

Checklist (Inter Regular 14 pt `#F0EDE8`, line height 155%):
- `Vertical columns clearly visible from bond coat to surface`
- `Inter-columnar gaps continuous (not bridged)`
- `Column width: 50--200 um (typical for YSZ SPS)`
- `No lamellar regions indicating parameter drift`
- `Bond coat / topcoat interface clean and continuous`
- `No horizontal delamination cracks`
- `Branching cracks and segmentation are ACCEPTABLE (enhance compliance)`

Note: `SEM is preferred over optical microscopy -- SPS features are finer than conventional APS and may not resolve well at optical magnification.` Inter Medium 13 pt `#E8A020`.

**Right -- BLOCK D: Good vs. Bad (X: 12.0", W: 11.5"):**

Two stacked panels:

*Top -- "ACCEPTABLE" (H: 2.5"):*
Rounded rect fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `ACCEPTABLE MICROSTRUCTURE` Barlow SemiBold 16 pt `#27AE60`.
- `Clear columnar structure with vertical alignment`
- `Inter-columnar porosity 5--15%`
- `No lamellar bands or horizontal crack planes`
- `Consistent column width across cross-section`

*Bottom -- "REJECTABLE" (H: 2.5"):*
Rounded rect fill `#1E2435`, left accent `#E05C5C` 0.06".
Title: `REJECTABLE MICROSTRUCTURE` Barlow SemiBold 16 pt `#E05C5C`.
- `Lamellar (flat splat) structure instead of columnar`
- `Bridged inter-columnar gaps (columns fused together)`
- `Horizontal delamination cracks at bond coat interface`
- `Mixed columnar/lamellar (indicates parameter instability)`

---

### ZONE 4 -- Phase Stability + Thermal Cycling

**Section label:** `PHASE ANALYSIS & THERMAL CYCLING` -- Y: 22.2".

**Left -- BLOCK E: XRD Phase Analysis (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".

Title: `XRD PHASE STABILITY CHECK` -- Barlow SemiBold 20 pt `#E05C5C`.

Key requirement (JetBrains Mono 18 pt `#E05C5C`):
`NO MONOCLINIC ZrO2`

Body (Inter Regular 14 pt):
- `YSZ must remain in tetragonal prime (t') phase`
- `Monoclinic ZrO2 = phase destabilization`
- `Monoclinic transformation causes ~4% volume expansion`
- `Volume expansion creates internal stress and spallation`
- `XRD scan identifies phase composition non-destructively`

Bottom callout: `If monoclinic phase is detected, the coating has failed phase stability. Investigate suspension composition, spray temperature, and cooling conditions.` Inter Medium 13 pt `#E05C5C`.

**Right -- BLOCK F: Thermal Cycling Test (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `THERMAL CYCLING PROTOCOL` -- Barlow SemiBold 20 pt `#E8A020`.

| Step | Condition |
|---|---|
| Heat | Ramp to 1100 degC in furnace |
| Hold | 1 hour at 1100 degC |
| Cool | Forced air cool to ~100 degC |
| Inspect | Visual for spallation after each cycle |
| Target | > 1000 cycles to 20% spallation area |

Data: JetBrains Mono 12 pt.

Note: `Thermal cycling is the ultimate SPS TBC performance test. It validates both columnar structure integrity and bond coat oxidation resistance under real-world thermal loading.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Acceptance / Rejection Strip

**Section label:** `REJECTION CRITERIA -- 4 AUTOMATIC FAILURES` -- Y: 28.7".

**BLOCK G -- Four Rejection Cards**

| Card | X | Failure | Indicator | Action |
|---|---|---|---|---|
| 1 | 0.5" | LAMELLAR MICROSTRUCTURE | SEM shows flat splats, no columns | Reject; review all spray parameters; re-qualify |
| 2 | 6.33" | MONOCLINIC PHASE DETECTED | XRD shows monoclinic ZrO2 peaks | Reject; investigate suspension and thermal history |
| 3 | 12.16" | BOND STRENGTH < 10 MPa | ASTM C633 failure | Reject; evaluate bond coat quality and interface cleanliness |
| 4 | 18.0" | PREMATURE SPALLATION | < 500 cycles in thermal cycling test | Reject; review bond coat oxidation and topcoat porosity |

Interior per card:
- Failure: Barlow SemiBold, 16 pt, `#E05C5C`
- Indicator: Inter Regular, 13 pt, `#F0EDE8`
- Action: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & QA -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

Disclaimer: `SPS is an emerging coating technology with evolving quality standards. Acceptance criteria shown are representative of current research practice for YSZ TBCs. Consult application-specific specifications for binding requirements. Standards may differ for non-TBC SPS applications.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #548 -- Construction Workup v1.0 -- 2026-04-26*
