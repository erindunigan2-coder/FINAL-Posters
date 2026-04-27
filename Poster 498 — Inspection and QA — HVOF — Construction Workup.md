---
Project: Plating Posters Inc
Poster Number: 498
Title: "Inspection & QA -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 10)"
Technical Source: HVOF quality assurance testing including ASTM C633 bond strength (>70 MPa), ASTM E2109 porosity (<1%), ASTM E384 hardness (1100-1400 HV300 for WC-12Co), ASTM B117 salt spray, metallographic cross-section, and AMS 2448 compliance requirements.
Process Scope: HVOF thermal spray -- inspection methods and quality acceptance criteria
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #498 -- Construction Workup
## Inspection & QA -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of the HVOF process -- the final gate. This poster is the comprehensive QA reference for HVOF coatings, with the 8-row test method table as the hero. The unique HVOF QA elements: bond strength so high it often exceeds the epoxy adhesive used in ASTM C633 testing (report as "> epoxy strength"), AMS 2448 compliance with destructive test coupons alongside production parts, and a microstructure interpretation guide focused on WC-Co-specific features (carbide distribution, decarburization indicators).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test method table (Block B -- HERO):** 8-row table with HVOF-specific acceptance criteria.
2. **AMS 2448 compliance callout (Block C):** Process qualification requirements for aerospace.
3. **Microstructure interpretation guide (Block D):** WC-Co-specific cross-section features.
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
  Block B: 8-row QA test table
ZONE 4 -- AMS 2448 COMPLIANCE (15.5"--22.0" / ~6.5")
  Block C: Aerospace qualification requirements
ZONE 5 -- MICROSTRUCTURE GUIDE (22.0"--28.5" / ~6.5")
  Block D: WC-Co cross-section interpretation
ZONE 6 -- ACCEPT/REJECT (28.5"--32.5" / ~4.0")
  Block E: Decision framework
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- The Final Gate -- Stage 10 of 10` -- 32 pt `#27AE60`. Y: 1.4".
**Tagline:** `Bond strength so high the test adhesive fails before the coating does. Porosity below 1%. Hardness exceeding hard chrome. Verify every property.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `8` -- 72 pt `#27AE60`
- Label: `standard tests to qualify your HVOF coating` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 10 highlighted (Emerald). Others dimmed.

---

### ZONE 3 -- Test Method Table (HERO)

**Section label:** `HVOF QUALITY TESTS -- COMPLETE REFERENCE` -- Y: 4.4".

**BLOCK B -- 8-Row Test Table**

Y: 5.0" to 15.3". Full width. Columns: Test (4.0") | ASTM Method (3.5") | Acceptance Criteria (8.0") | Notes (7.5")

| Test | Method | Acceptance Criteria (WC-12Co) | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 | > 70 MPa (often exceeds epoxy -- report as "> epoxy") | Tensile adhesion; epoxy FM-1000 rated ~75-80 MPa |
| Porosity | ASTM E2109 | < 1.0% (typically < 0.5%) | Image analysis on metallographic cross-section |
| Thickness | Eddy current; mag-gauge; ASTM B487 | Per drawing +/- 50 um | Cross-section is definitive; others are screening |
| Hardness | ASTM E384 (HV300) | 1100-1400 HV300 | Vickers microhardness on cross-section; load 300 gf |
| Surface roughness | Profilometer (Ra) | As-ground: Ra < 0.4 um typical | Specification dependent; verify per drawing |
| Microstructure | Metallographic cross-section (unetched + etched) | Uniform carbide distribution; no delamination; no oxide stringers | Evaluate at 200-500x; check for decarburization |
| Visual | Unaided eye + 10x loupe | No spalling, blistering, orange peel, or bare spots | First-pass screen before destructive testing |
| Corrosion | ASTM B117 (salt spray) | Per spec; typically > 500 hrs (sealed) | Only if specified; most WC-Co applications are wear, not corrosion |

Header: fill `#3A4055`, Barlow SemiBold 13 pt. Data: JetBrains Mono 11 pt `#F0EDE8`. ASTM numbers in `#E8A020`.

---

### ZONE 4 -- AMS 2448 Compliance

**Section label:** `AMS 2448 -- AEROSPACE QUALIFICATION FOR HVOF WC COATINGS` -- Y: 15.7".

**BLOCK C -- Two-Column AMS 2448 Layout**

Y: 16.3" to 21.8".

**Left -- What AMS 2448 Requires (W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `AMS 2448 REQUIREMENTS` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
AMS 2448 governs HVOF application of
tungsten carbide coatings for aerospace.

Key requirements:
1. Process qualification (PQ) with destructive
   test coupons sprayed alongside production
2. Equipment calibration records
3. Powder lot traceability and certification
4. Parameter recording and data logging
5. Operator qualification per AMS 2448
6. Periodic re-qualification (annual or per spec)
```

**Right -- Destructive Test Coupon Protocol (W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `TEST COUPON PROTOCOL` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
Test coupons must be:
- Same substrate material as production part
- Sprayed simultaneously in same setup
- Subjected to same post-treatment (grinding)

From each coupon set, perform:
- Bond strength (ASTM C633)
- Hardness (ASTM E384, HV300)
- Porosity (ASTM E2109, cross-section)
- Microstructure (metallographic evaluation)

If ANY coupon fails: entire production lot is suspect.
Investigate root cause before re-spraying.
```

Bottom note spanning full width:
`AMS 2448 is the aerospace industry's assurance that HVOF WC-Co can reliably replace hard chrome on flight-critical components. Compliance is non-negotiable for aerospace work.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Microstructure Guide

**Section label:** `READING THE WC-Co CROSS-SECTION -- WHAT TO LOOK FOR` -- Y: 22.2".

**BLOCK D -- 6 Microstructure Features**

Y: 22.9" to 28.3". Six cards in a 3x2 grid.

| Feature | Good Sign | Bad Sign | Color |
|---|---|---|---|
| Carbide distribution | Uniform WC particles throughout Co matrix | Clusters, voids, or depleted zones | `#27AE60` / `#E05C5C` |
| Decarburization | Sharp, angular WC particles (original morphology) | Rounded WC particles; W2C or eta-phase halos visible | `#27AE60` / `#E05C5C` |
| Interface quality | Clean bond line; grit blast profile visible | Gaps, contamination, or disbond at interface | `#27AE60` / `#E05C5C` |
| Porosity | Minimal pores; no interconnected voids | Large voids or interconnected pore network | `#27AE60` / `#E05C5C` |
| Oxide content | Minimal dark stringers between splats | Heavy oxide layers between lamellae | `#E8A020` / `#E05C5C` |
| Lamellar structure | Well-deformed splats with good cohesion | Poorly bonded splats; visible inter-lamellar gaps | `#27AE60` / `#E05C5C` |

Each card: Rounded rect, W: 7.33", H: 2.5", fill `#1E2435`.
Feature name: Barlow SemiBold 14 pt `#F0EDE8`.
Good: Inter Medium 12 pt `#27AE60`. Bad: Inter Medium 12 pt `#E05C5C`.

Key note below grid:
`DECARBURIZATION is the #1 microstructure defect in HVOF WC-Co. Look for rounded (instead of angular) WC particles and gray halos around carbides. Decarburization means the flame was too hot -- the WC decomposed to W2C or free tungsten, and hardness drops dramatically.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Accept/Reject Decision

**BLOCK E -- Decision Callout**

Two side-by-side boxes:

**Left -- ACCEPT (Emerald):**
- Fill `#27AE60` at 12%, border 1 pt `#27AE60`
- All tests meet AMS 2448 or customer specification
- Visual inspection passes
- Test coupons within limits
- Documentation complete (parameter logs, coupon certs, powder lot records)

**Right -- REJECT / REWORK (Coral):**
- Fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Any test below specification
- Strip and re-spray (grind off coating; re-blast; re-spray)
- Root cause analysis REQUIRED before re-spray
- If decarburization: check fuel:O2 ratio and standoff distance
- `The cost of stripping and re-spraying is always less than the cost of a failed component in service`

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & QA -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the HVOF cluster. The bond strength exceeding epoxy adhesive is a genuinely impressive data point that makes HVOF quality tangible -- the test literally cannot measure how strong the bond is because the adhesive fails first. The AMS 2448 section is critical for aerospace shops -- it is the specification that enables HVOF as a hard chrome replacement on flight hardware. The decarburization emphasis in the microstructure guide connects back to the fuel:O2 ratio teaching from Poster #495 -- the cluster tells a complete story.

---

*Alaina -- Poster #498 -- Construction Workup v1.0 -- 2026-04-26*
