---
Project: Plating Posters Inc
Poster Number: 518
Title: "Inspection & QA -- Arc Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 4: Arc Spray)"
Process Scope: Inspection and quality assurance for arc spray coatings -- field and lab test methods, AWS C2.18 acceptance criteria, holiday detection for sealed systems
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - ArcSpray
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS04
---

# Poster #518 -- Construction Workup
## Inspection & QA -- Arc Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Arc Spray cluster. Arc spray inspection is simpler than HVOF or plasma -- you are dealing with corrosion protection coatings on structural steel, not aerospace turbine parts. The hero content is the test methods table with AWS C2.18 acceptance criteria. The unique element here is holiday detection on sealed coatings -- a low-voltage wet sponge test that verifies the seal coat is continuous and the corrosion barrier is intact. The 180-degree bend test (qualification only) is the mechanical adhesion proof. Field-portable testing dominates -- mag-gauge thickness, portable pull-off adhesion, and visual inspection are what inspectors actually use on bridges and structures.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test methods table (Block B -- HERO):** 6-row table with ASTM/SSPC methods and AWS C2.18 acceptance criteria.
2. **Field vs. lab testing callout (Block C):** Side-by-side showing what is done in the field vs. the lab.
3. **Holiday detection guide (Block D):** How low-voltage wet sponge testing works on sealed arc spray coatings.
4. **Documentation checklist (Block E):** QA record-keeping requirements per AWS C2.18.
5. **Reject criteria strip (Block F):** 4 conditions that require stripping and re-spraying.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Teal)
ZONE 3 -- TEST METHODS TABLE / HERO (4.2"--15.5" / ~11.3")
  Block B: 6-row test methods and acceptance criteria
  Block C: Field vs. lab testing callout
ZONE 4 -- HOLIDAY DETECTION GUIDE (15.5"--22.0" / ~6.5")
  Block D: Low-voltage wet sponge procedure
ZONE 5 -- DOCUMENTATION CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: QA documentation requirements
ZONE 6 -- REJECT CRITERIA (28.5"--32.5" / ~4.0")
  Block F: 4 reject condition cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Arc Spray -- Verifying Corrosion Protection from Field to Lab` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `Arc spray coatings protect structural steel for decades -- but only if the thickness, bond, and seal are verified. Most arc spray inspection happens on-site with portable instruments. Know your tools. Know your acceptance criteria.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating sealed and paint system applied --> After: Coating verified, documented, and released for service`

---

### ZONE 3 -- Test Methods Table (HERO)

**Section label:** `INSPECTION TEST METHODS & ACCEPTANCE CRITERIA` -- Y: 4.4".

**BLOCK B -- 6-Row Test Methods Table**

Y: 5.0" to 12.0". Full width within margins (23.0").

Column widths: Test (3.5") | Method / Standard (5.0") | Acceptance Criteria (6.0") | Notes (4.0") | Field/Lab (4.5")

| Test | Method / Standard | Acceptance Criteria | Notes | Field/Lab |
|---|---|---|---|---|
| Bond strength | ASTM C633 (lab) or portable pull-off adhesion tester (field) | > 7 MPa (AWS C2.18 minimum); typical 10--30 MPa | Portable adhesion tester most common in field; ASTM C633 for qualification | Both |
| Thickness | Magnetic gauge (DFT) per SSPC-PA 2 | Per specification: Zn mild 100--150 um; Zn severe 200--350 um; Al 150--350 um | Multiple readings per area; average must meet minimum; no single reading below 80% of specified minimum | Field |
| Visual | Unaided eye | Uniform coverage; no bare spots, blistering, delamination, or excessive orange peel | First inspection performed; before any instrument testing | Field |
| Bend test | 180-degree bend around mandrel (qualification test) | No cracking or spalling | Qualification test only -- not production; per AWS C2.18 | Lab |
| Holiday detection | Low-voltage wet sponge (for sealed coatings) | Zero holidays in sealed system | Verifies seal coat continuity; detects pinholes in seal | Field |
| Surface profile (pre-spray) | Testex replica tape or profilometer | Ra 4--12 um (per AWS C2.18) | Verified BEFORE spray; documented as part of QA record | Field |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".
Test names: Inter Medium 13 pt `#F0EDE8`. Methods: JetBrains Mono 12 pt `#E8A020`. Criteria: Inter Regular 13 pt. Notes: Inter Regular 12 pt `#F0EDE8` at 70%. Field/Lab: JetBrains Mono 12 pt `#2EC4B6`.

**BLOCK C -- Field vs. Lab Testing**

Y: 12.5" to 15.3". Two side-by-side panels.

**Left -- Field Testing (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `FIELD TESTING` Barlow SemiBold 16 pt `#27AE60`
- `Mag-gauge thickness (SSPC-PA 2)`
- `Portable pull-off adhesion tester`
- `Visual inspection -- unaided eye`
- `Holiday detection -- wet sponge`
- `Surface profile -- Testex tape`
- Bottom: `90% of arc spray QA is performed on-site with portable instruments.` Inter Medium 13 pt `#27AE60`.

**Right -- Lab Testing (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `LABORATORY TESTING` Barlow SemiBold 16 pt `#E8A020`
- `ASTM C633 tensile adhesion (epoxy-bonded dollies)`
- `180-degree mandrel bend test (qualification)`
- `Metallographic cross-section (rare for arc spray)`
- `Salt spray testing (ASTM B117, if specified)`
- Bottom: `Lab testing is primarily for process qualification, not production QA.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- Holiday Detection Guide

**Section label:** `HOLIDAY DETECTION -- VERIFYING SEAL COAT INTEGRITY` -- Y: 15.7".

**BLOCK D -- Low-Voltage Wet Sponge Procedure**

Y: 16.3" to 21.5". Full width. Two elements side by side.

**Left -- Procedure Steps (X: 0.5", W: 14.0"):**

Six step cards, vertically stacked.

Each card: W: 13.5", H: 0.75", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Action | Detail |
|---|---|---|---|
| 1 | `#2EC4B6` | VERIFY SEAL COAT IS FULLY CURED | Testing uncured seal gives false positives |
| 2 | `#E8A020` | WET SPONGE WITH TAP WATER | Saturate sponge; squeeze out excess; sponge must be uniformly damp |
| 3 | `#2EC4B6` | SET DETECTOR VOLTAGE | Low-voltage setting (typically 9--90 V DC); per NACE SP0188 or ASTM D5162 |
| 4 | `#E8A020` | GROUND CLIP TO BARE METAL | Electrical ground connection to substrate; must be clean metal contact |
| 5 | `#27AE60` | SLOWLY TRAVERSE SEALED SURFACE | Move sponge at 150--300 mm/s; maintain full contact; overlapping passes |
| 6 | `#E05C5C` | MARK ALL HOLIDAYS | Audible alarm indicates pinhole in seal; mark with chalk; repair and re-test |

Step numbers: Barlow Condensed ExtraBold 18 pt accent color. Action: Inter Medium 13 pt `#F0EDE8`. Detail: Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- Why It Matters (X: 15.0", W: 8.5"):**

Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E05C5C`.

Title: `WHY HOLIDAYS MATTER` Barlow SemiBold 18 pt `#E05C5C`.

Body (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
A "holiday" is a pinhole or gap in the
seal coat where moisture can reach the
porous thermal spray coating beneath.

Even one holiday allows water to travel
through interconnected porosity and
reach the steel substrate.

At that point, the zinc provides
cathodic protection -- but the seal
system has failed and service life
is reduced.

Holiday detection is the quality gate
between "sealed" and "properly sealed."
```

Stat: `ZERO HOLIDAYS` JetBrains Mono Bold, 20 pt, `#E05C5C`.
Label: `Acceptance criterion for all sealed systems` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Documentation Checklist

**Section label:** `QA DOCUMENTATION -- AWS C2.18 REQUIREMENTS` -- Y: 22.2".

**BLOCK E -- Documentation Checklist**

Y: 22.8" to 28.0". Two columns of checklist items.

| Item | Record |
|---|---|
| Surface preparation | Blast media, grit size, profile (Ra), cleanliness standard (SSPC-SP 5 or SP 10), ambient conditions |
| Time between blast and spray | Documented with humidity and temperature at time of spray |
| Wire feedstock | Material, wire diameter, lot number, certificate of conformance |
| Spray parameters | Voltage, amperage, wire feed speed, air pressure, standoff distance |
| Coating thickness | DFT readings per SSPC-PA 2; multiple readings per area; average and minimum reported |
| Seal coat application | Sealer type, manufacturer, application method, time between spray and seal, cure time |
| Holiday detection results | Test method, voltage setting, results (pass/fail), any repairs performed |
| Bond strength (if tested) | Test method, number of tests, individual and average results |
| Visual inspection | Inspector name, date, acceptance/rejection, any observations |
| Weather conditions (field work) | Temperature, relative humidity, dew point, wind speed (per AWS C2.18 limits) |

Checklist items: Inter Medium 13 pt `#F0EDE8`. Records: Inter Regular 13 pt `#F0EDE8` at 70%.
Each row has a checkbox indicator: rounded rect 0.3" x 0.3", border 1 pt `#2EC4B6`, fill transparent.

Below checklist:
- Callout: `AWS C2.18 requires full documentation of every process step. If the inspector cannot verify it from the records, it was not done.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 6 -- Reject Criteria

**Section label:** `REJECT CONDITIONS -- STRIP AND RE-SPRAY` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Condition | Action |
|---|---|---|---|
| 1 | 0.5" | THICKNESS BELOW MINIMUM | If average DFT is below specified minimum or any single reading is below 80% of minimum, add additional spray to deficient areas and re-measure. If bond is compromised, strip and re-spray. |
| 2 | 6.33" | BOND STRENGTH BELOW 7 MPa | Strip coating completely by grit blasting; investigate root cause (contamination, stale blast, moisture); re-blast and re-spray. |
| 3 | 12.16" | HOLIDAYS IN SEALED SYSTEM | Re-apply seal coat to deficient areas; re-test. If holidays persist, strip seal, investigate coating porosity and seal application, re-seal. |
| 4 | 18.0" | BARE SPOTS OR DELAMINATION | Strip affected area by grit blast; re-blast to profile; re-spray. Investigate cause -- likely contamination, insufficient profile, or excessive time between blast and spray. |

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- Arc Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: AWS C2.18; SSPC-CS 23.00; SSPC-PA 2; NACE SP0188; ASM Handbook Vol 5A; general industry knowledge. Acceptance criteria shown are typical values per AWS C2.18. Specific project specifications may impose additional or different requirements.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

## Design Notes

This is the "prove it" poster -- the final station in the arc spray workflow. Unlike HVOF or plasma where you are chasing sub-micron porosity and 1400 HV hardness numbers, arc spray QA is practical and field-oriented. The mag-gauge and the wet sponge are the two instruments an inspector carries onto a bridge. The holiday detection guide is the unique content for this poster -- it is the quality gate that separates a porous zinc coating from a corrosion protection system. The documentation checklist reinforces that AWS C2.18 demands traceability of every step, especially weather conditions for outdoor field work. The bond strength minimum of 7 MPa (AWS C2.18) is notably lower than HVOF (70 MPa) or D-Gun (80 MPa) -- this reflects the different application: corrosion protection, not wear resistance.

---

*Alaina -- Poster #518 -- Construction Workup v1.0 -- 2026-04-26*
