---
Project: Plating Posters Inc
Poster Number: 558
Title: "Inspection & QA -- Wire Combustion Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 8: Wire Combustion Spray)"
Process Scope: Inspection and quality assurance for wire combustion spray coatings -- field test methods, AWS C2.18 acceptance criteria, holiday detection, and documentation requirements identical to arc spray QA
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - WireCombustionSpray
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS08
---

# Poster #558 -- Construction Workup
## Inspection & QA -- Wire Combustion Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Wire Combustion Spray cluster. Wire combustion spray inspection is functionally identical to arc spray QA -- both processes serve the same corrosion protection market, both follow AWS C2.18, and both use the same field-portable test instruments. The hero is the test methods table with AWS C2.18 acceptance criteria. The unique angle for this poster is the field inspection emphasis -- wire combustion spray is the most portable thermal spray process, so the QA often happens on bridges, tanks, and offshore platforms where lab instruments are not available. The comparison with arc spray QA criteria reinforces that these two processes produce comparable coatings requiring comparable quality verification.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test methods table (Block B -- HERO):** 5-row table with ASTM/SSPC methods and AWS C2.18 acceptance criteria.
2. **Field inspection toolkit (Block C):** The portable instruments an inspector carries to a jobsite.
3. **Holiday detection procedure (Block D):** Low-voltage wet sponge test for sealed coatings.
4. **Wire combustion vs. arc spray QA comparison (Block E):** Side-by-side showing identical acceptance criteria.
5. **Reject criteria strip (Block F):** 4 rejection conditions.

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
  Block B: 5-row test methods and acceptance criteria
  Block C: Field inspection toolkit
ZONE 4 -- HOLIDAY DETECTION + COMPARISON (15.5"--22.0" / ~6.5")
  Block D: Holiday detection procedure
  Block E: Wire combustion vs. arc spray QA comparison
ZONE 5 -- DOCUMENTATION REQUIREMENTS (22.0"--28.5" / ~6.5")
  Block G: QA documentation checklist for field work
ZONE 6 -- REJECT CRITERIA (28.5"--32.5" / ~4.0")
  Block F: 4 reject condition cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Wire Combustion Spray -- Field-Ready Quality Verification` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `Wire combustion spray goes where other processes cannot -- bridges, offshore platforms, remote infrastructure. The inspection goes with it. Mag-gauge, wet sponge, visual. Portable, proven, and per AWS C2.18.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating sealed and paint system applied --> After: Coating verified, documented, and released for service`

---

### ZONE 3 -- Test Methods Table (HERO)

**Section label:** `INSPECTION TEST METHODS & ACCEPTANCE CRITERIA` -- Y: 4.4".

**BLOCK B -- 5-Row Test Methods Table**

Y: 5.0" to 11.0". Full width within margins (23.0").

Column widths: Test (3.5") | Method / Standard (5.5") | Acceptance Criteria (6.5") | Notes (7.5")

| Test | Method / Standard | Acceptance Criteria | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 (lab) or portable adhesion tester (field) | > 7 MPa (AWS C2.18 minimum); typical 7--25 MPa | Portable pull-off tester is the field standard; ASTM C633 for qualification only |
| Thickness | Magnetic gauge (DFT) per SSPC-PA 2 | Per specification: Zn 100--350 um; Al 150--350 um; ZnAl 150--300 um | Minimum 5 readings per defined area; average and individual minimums per SSPC-PA 2 |
| Visual | Unaided eye | Uniform coverage; no bare spots, blistering, or delamination | First inspection performed at every stage; no instruments required |
| Bend test | 180-degree mandrel bend (qualification) | No cracking or spalling | Qualification test only; not repeated in production; per AWS C2.18 |
| Holiday detection | Low-voltage wet sponge (sealed coatings) | Zero holidays | Verifies seal coat continuity; performed after seal coat cure |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".
Test names: Inter Medium 13 pt `#F0EDE8`. Methods: JetBrains Mono 12 pt `#E8A020`. Criteria: Inter Regular 13 pt. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

**BLOCK C -- Field Inspection Toolkit**

Y: 11.5" to 15.3". Full width.

Section sublabel: `THE FIELD INSPECTOR'S TOOLKIT` Barlow SemiBold 18 pt `#27AE60`. Y: 11.5".

Five tool cards in a single row. Each card: W: 4.4", H: 3.0", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | X | Accent | Tool | What It Measures |
|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | MAG-GAUGE | Dry film thickness (DFT) on ferrous substrates. Non-destructive. Per SSPC-PA 2. Multiple readings per area. |
| 2 | 5.2" | `#2EC4B6` | PORTABLE ADHESION TESTER | Pull-off bond strength. Epoxy-bonded dolly glued to coating surface. Portable hydraulic or pneumatic pull. |
| 3 | 9.9" | `#27AE60` | WET SPONGE DETECTOR | Holiday (pinhole) detection in seal coat. Low-voltage DC through damp sponge. Audible alarm at holidays. |
| 4 | 14.6" | `#E8A020` | TESTEX REPLICA TAPE | Surface profile (Ra) measurement. Press tape onto blasted surface; measure with micrometer. Pre-spray verification. |
| 5 | 19.3" | `#C8D0D8` | INSPECTION MIRROR + 10x LOUPE | Visual inspection of hard-to-see areas. Loupe for close-up surface evaluation. |

Tool name: Barlow SemiBold 14 pt accent color.
What It Measures: Inter Regular 12 pt `#F0EDE8`.

Below toolkit:
- Callout: `Every instrument in this toolkit is battery-powered or mechanical, truck-portable, and usable in field conditions. No lab required.` Inter Medium 13 pt `#27AE60`.

---

### ZONE 4 -- Holiday Detection + Comparison

**Left -- BLOCK D: Holiday Detection Procedure (X: 0.5", W: 11.0")**

Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".

Title: `HOLIDAY DETECTION -- SEAL COAT VERIFICATION` Barlow SemiBold 20 pt `#E05C5C`.

| Step | Action |
|---|---|
| 1 | Confirm seal coat is fully cured (per manufacturer spec) |
| 2 | Wet sponge with clean tap water; squeeze to damp (not dripping) |
| 3 | Set detector to low-voltage DC (9--90 V per NACE SP0188 / ASTM D5162) |
| 4 | Attach ground clip to exposed bare metal on substrate |
| 5 | Traverse sponge across sealed surface at 150--300 mm/s; overlapping passes |
| 6 | Audible alarm = holiday found. Mark location with chalk or paint pen. |
| 7 | Repair holidays by re-applying seal coat to marked areas; re-test after cure |

Step numbers: Barlow Condensed ExtraBold 16 pt `#E05C5C`. Action: Inter Regular 13 pt `#F0EDE8`.

Acceptance: `ZERO HOLIDAYS. Any holiday means the seal coat barrier is compromised at that point.` JetBrains Mono 14 pt `#E05C5C`.

**Right -- BLOCK E: Wire Combustion vs. Arc Spray QA (X: 12.0", W: 11.5")**

Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#2EC4B6`.

Title: `WIRE COMBUSTION vs. ARC SPRAY -- QA COMPARISON` Barlow SemiBold 18 pt `#2EC4B6`.

| Test | Wire Combustion | Arc Spray |
|---|---|---|
| Bond strength minimum | > 7 MPa | > 7 MPa |
| Thickness standard | SSPC-PA 2 | SSPC-PA 2 |
| Visual | Same criteria | Same criteria |
| Bend test | 180-degree mandrel | 180-degree mandrel |
| Holiday detection | Wet sponge; zero holidays | Wet sponge; zero holidays |
| Governing standard | AWS C2.18 | AWS C2.18 |

Data: JetBrains Mono 12 pt. Wire combustion values in `#E8A020`. Arc spray values in `#2EC4B6`.

Below table:
`QA criteria are identical because both processes serve the same corrosion protection function per the same standard (AWS C2.18). The coating quality is comparable -- wire combustion runs slightly lower bond strength (7--25 MPa vs. 10--30 MPa) but meets the same minimum.` Inter Medium 12 pt `#C8D0D8`.

---

### ZONE 5 -- Documentation Requirements

**Section label:** `FIELD QA DOCUMENTATION -- AWS C2.18` -- Y: 22.2".

**BLOCK G -- Field Documentation Checklist**

Y: 22.8" to 28.0". Two columns of checklist items.

| Item | Record |
|---|---|
| Surface preparation | Blast media, grit size, profile achieved (Ra), cleanliness standard (SSPC-SP 5 or SP 10) |
| Ambient conditions | Temperature, relative humidity, dew point, wind speed; verify surface temp > 3 degC above dew point |
| Time from blast to spray | Documented with timestamp; must comply with AWS C2.18 humidity-based limits |
| Wire feedstock | Material, wire diameter, lot number, supplier certificate of conformance |
| Spray parameters | O2 pressure, fuel pressure, air pressure, wire feed speed, standoff distance |
| Coating thickness | DFT per SSPC-PA 2; spot readings documented by location; average and minimum reported |
| Seal coat application | Sealer type, manufacturer, lot, application method, time from spray to seal, cure conditions |
| Holiday detection | Test method, voltage, results (pass/fail), any repairs and re-tests |
| Visual inspection | Inspector name/certification, date, time, acceptance/rejection |
| Photographs | Before blast, after blast, during spray (if practical), after seal, final coating |

Checklist items: Inter Medium 13 pt `#F0EDE8`. Records: Inter Regular 13 pt `#F0EDE8` at 70%.
Each row has a checkbox indicator: rounded rect 0.3" x 0.3", border 1 pt `#2EC4B6`, fill transparent.

Below checklist:
- Callout: `Field work demands MORE documentation, not less. Weather conditions change, access is limited, and re-work costs are high. Record everything. Photograph everything.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 6 -- Reject Criteria

**Section label:** `REJECT CONDITIONS -- STRIP AND RE-SPRAY` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Condition | Action |
|---|---|---|---|
| 1 | 0.5" | THICKNESS BELOW MINIMUM | Add spray to deficient areas if bond is still sound. If coating has been sealed, re-spraying over seal is not acceptable -- strip seal, add spray, re-seal. |
| 2 | 6.33" | BOND STRENGTH BELOW 7 MPa | Strip coating by grit blast; investigate surface prep quality (contamination, profile, dew point compliance); re-blast and re-spray. |
| 3 | 12.16" | PERSISTENT HOLIDAYS | Re-seal and re-test. If holidays persist after second seal application, strip seal coat, investigate coating porosity and seal technique, and re-seal with corrected method. |
| 4 | 18.0" | BARE SPOTS OR DELAMINATION | Strip affected area by grit blast to clean profile; re-spray. Common causes: contamination, insufficient profile, surface moisture (dew point violation), or excessive time between blast and spray. |

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- Wire Combustion Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: AWS C2.18; SSPC-CS 23.00; SSPC-PA 2; NACE SP0188; ASTM D5162; ASM Handbook Vol 5A; general industry knowledge. Acceptance criteria shown are typical values per AWS C2.18 for cathodic corrosion protection coatings. Specific project specifications may impose additional requirements.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

## Design Notes

This poster closes out the Wire Combustion Spray cluster with the same QA rigor as Poster 518 (Arc Spray Inspection & QA). The two posters are deliberately parallel in structure because the two processes share the same governing standard (AWS C2.18) and the same acceptance criteria. The differentiator for this poster is the field inspection toolkit -- wire combustion spray is the most portable thermal spray setup, so the inspection has to be equally portable. The five-tool toolkit (mag-gauge, portable adhesion tester, wet sponge, Testex tape, mirror + loupe) is the visual centerpiece of Zone 3 -- an inspector could photograph this poster on their phone and use it as a packing checklist. The documentation section emphasizes field-specific records (weather conditions, photographs, timestamps) because field work on bridges and infrastructure is where documentation gaps most commonly occur.

---

*Alaina -- Poster #558 -- Construction Workup v1.0 -- 2026-04-26*
