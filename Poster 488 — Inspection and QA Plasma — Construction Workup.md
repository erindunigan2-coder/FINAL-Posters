---
Project: Plating Posters Inc
Poster Number: 488
Title: "Inspection & QA -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 10)"
Technical Source: APS quality assurance testing including ASTM C633 bond strength, ASTM E2109 porosity, ASTM B487 thickness, ASTM E384 microhardness, profilometry, metallographic cross-section, and visual inspection. Acceptance criteria by coating type.
Process Scope: Atmospheric plasma spray -- inspection methods and quality acceptance criteria
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #488 -- Construction Workup
## Inspection & QA -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of the APS process -- the final gate. This poster is a comprehensive QA reference showing every test method, the ASTM standard that governs it, and typical acceptance criteria by coating material. The hero is a 9-row test method table. Supporting content: hardness values by coating type and a microstructure interpretation guide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test method table (Block B -- HERO):** 9-row table with test, ASTM method, and acceptance criteria.
2. **Hardness by coating type (Block C):** 5 common APS coatings with expected HV values.
3. **Microstructure interpretation guide (Block D):** What to look for in a cross-section.
4. **Accept/reject decision callout (Block E):** Binary decision framework.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 10 highlighted (Emerald)
ZONE 3 -- TEST METHOD TABLE HERO (4.2"--15.5" / ~11.3")
  Block B: 9-row QA test table
ZONE 4 -- HARDNESS BY COATING (15.5"--22.0" / ~6.5")
  Block C: Hardness reference + porosity targets
ZONE 5 -- MICROSTRUCTURE GUIDE (22.0"--28.5" / ~6.5")
  Block D: What to look for in cross-section
ZONE 6 -- ACCEPT/REJECT (28.5"--32.5" / ~4.0")
  Block E: Decision framework
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- The Final Gate -- Stage 10 of 10` -- 32 pt `#27AE60`. Y: 1.4".
**Tagline:** `Trust your process, but verify your coating. Every test method here exists because someone shipped a bad part without it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `9` -- 72 pt `#27AE60`
- Label: `standard tests to qualify your APS coating` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 10 highlighted (Emerald). Others dimmed.

---

### ZONE 3 -- Test Method Table (HERO)

**Section label:** `APS QUALITY TESTS -- COMPLETE REFERENCE` -- Y: 4.4".

**BLOCK B -- 9-Row Test Table**

Y: 5.0" to 15.3". Full width. Columns: Test (4.0") | ASTM Method (3.5") | Acceptance Criteria (8.0") | Notes (7.5")

| Test | Method | Acceptance Criteria | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 | > 10 MPa (ceramics); > 30 MPa (metals) | Tensile adhesion pull-off; spec-dependent |
| Porosity | ASTM E2109 | TBCs: 10-20% (intentional); wear: < 5% | Image analysis on metallographic section |
| Thickness | ASTM B487; eddy current; mag-gauge | Per drawing tolerance; typically +/- 50 um | Cross-section is definitive; others are screening |
| Hardness | ASTM E384 (HV300) | Material-dependent (see Zone 4) | Vickers microhardness on cross-section |
| Surface roughness | Profilometer (Ra) | As-sprayed: 5-15 um; ground: 0.2-1.6 um | Specification dependent |
| Microstructure | Metallographic cross-section | No delamination, cracks, oxide stringers | Evaluate at 100-500x magnification |
| Visual | Unaided eye + 10x loupe | No blistering, spalling, discoloration, bare spots | First-pass screen before destructive tests |
| Bend test | Mandrel bend (qualitative) | No cracking or spalling at specified radius | Qualification test; not routine production |
| Macrohardness | Rockwell HR15N (thin coatings) | Process-specific | Surface hardness; less precise than HV300 |

Header: fill `#3A4055`, Barlow SemiBold 13 pt. Data: JetBrains Mono 11 pt `#F0EDE8`. ASTM numbers in `#E8A020`.

---

### ZONE 4 -- Hardness by Coating Type

**Section label:** `EXPECTED HARDNESS BY COATING MATERIAL` -- Y: 15.7".

**BLOCK C -- Hardness Reference Table + Porosity Targets**

Two side-by-side panels.

**Left -- Hardness (W: 11.0"):**

| Coating | Hardness (HV300) | Notes |
|---|---|---|
| Alumina (Al2O3) | 800-1,200 | General ceramic wear coating |
| Chrome oxide (Cr2O3) | 1,000-1,800 | Hardest APS ceramic coating |
| YSZ (7-8% Y2O3) | 600-900 | TBC topcoat |
| NiCr (80/20) | 250-400 | Metallic wear/corrosion coating |
| MCrAlY | 300-500 | TBC bond coat |

**Right -- Porosity Targets (W: 11.5"):**

| Application | Target Porosity | Why |
|---|---|---|
| TBC (thermal barrier) | 10-20% | Intentional -- provides strain tolerance and thermal insulation |
| Wear coating (Al2O3, Cr2O3) | < 5% | Low porosity = wear resistance |
| Abradable coating | 30-60% | Intentional -- must wear away on contact |
| Metallic corrosion coating | < 5% (+ seal) | Seal interconnected porosity for corrosion barrier |

---

### ZONE 5 -- Microstructure Guide

**Section label:** `READING THE CROSS-SECTION -- WHAT TO LOOK FOR` -- Y: 22.2".

**BLOCK D -- 6 Microstructure Features**

Y: 22.9" to 28.3". Six cards in a 3x2 grid.

| Feature | Good Sign | Bad Sign | Color |
|---|---|---|---|
| Splat structure | Flat, well-deformed lamellae | Round, unmelted particles | `#27AE60` / `#E05C5C` |
| Interface | Clean bond line; profile visible | Gaps, contamination at interface | `#27AE60` / `#E05C5C` |
| Porosity distribution | Uniform, fine pores (if expected) | Large interconnected voids | `#27AE60` / `#E05C5C` |
| Oxide content | Minimal dark stringers between splats | Heavy oxide layers between every splat | `#E8A020` / `#E05C5C` |
| Cracks | None (or controlled vertical segmentation in TBCs) | Horizontal cracks parallel to interface | `#E8A020` / `#E05C5C` |
| Thickness uniformity | Consistent across cross-section | Thinning at edges or high points | `#27AE60` / `#E05C5C` |

Each card: Rounded rect, W: 7.33", H: 2.5", fill `#1E2435`.
Feature name: Barlow SemiBold 14 pt `#F0EDE8`.
Good: Inter Medium 12 pt `#27AE60`. Bad: Inter Medium 12 pt `#E05C5C`.

---

### ZONE 6 -- Accept/Reject Decision

**BLOCK E -- Decision Callout**

Two side-by-side boxes:

**Left -- ACCEPT (Emerald):**
- Fill `#27AE60` at 12%, border 1 pt `#27AE60`
- All tests meet specification
- Visual inspection passes
- Documentation complete (test coupons, parameter logs, certificates)

**Right -- REJECT / REWORK (Coral):**
- Fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Any test below specification
- Strip and re-spray (most common rework path)
- Root cause analysis required before re-spray
- `Never ship a marginal coating -- the failure will be more expensive than the rework`

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & QA -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the APS cluster. The 9-test table is the core reference -- a QA engineer should be able to look at the wall and know which ASTM standard applies to each test. The microstructure guide is the teaching tool: reading a cross-section is a skill, and this poster gives operators a framework for interpreting what they see under the microscope. The porosity targets table makes the critical distinction that porosity is sometimes intentional (TBCs, abradables) and sometimes a defect.

---

*Alaina -- Poster #488 -- Construction Workup v1.0 -- 2026-04-26*
