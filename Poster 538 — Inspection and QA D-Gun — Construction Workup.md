---
Project: Plating Posters Inc
Poster Number: 538
Title: "Inspection & QA -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 6: Detonation Gun)"
Process Scope: Inspection and quality assurance for D-Gun coatings -- test methods, acceptance criteria, metallographic evaluation, and the premium-tier QA standards that match D-Gun's premium coating quality
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - DGun
  - DetonationGun
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #538 -- Construction Workup
## Inspection & QA -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the D-Gun cluster. D-Gun inspection is aerospace-grade QA at its most demanding. The acceptance criteria reflect the premium quality of the process: porosity < 0.5%, bond strength exceeding the epoxy used in ASTM C633 testing, hardness 1200--1500 HV300, thickness tolerances of +/- 25 um (tighter than HVOF). The hero content is the inspection test matrix with these criteria. The metallographic cross-section evaluation is the showpiece -- D-Gun cross-sections display the finest carbide distribution and lowest decarburization of any thermal spray process. Every D-Gun job runs with destructive test coupons sprayed alongside production parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection test matrix (Block B -- HERO):** 7-row table with ASTM methods and D-Gun-specific acceptance criteria.
2. **Metallographic cross-section guide (Block C):** What good and bad D-Gun microstructure looks like.
3. **D-Gun vs. HVOF QA comparison (Block D):** Side-by-side acceptance criteria highlighting where D-Gun is tighter.
4. **Test coupon requirements (Block E):** Destructive testing protocol using companion coupons.
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
ZONE 3 -- INSPECTION TEST MATRIX / HERO (4.2"--15.5" / ~11.3")
  Block B: 7-row test matrix with acceptance criteria
  Block C: Metallographic cross-section guide
ZONE 4 -- D-GUN vs. HVOF QA COMPARISON (15.5"--22.0" / ~6.5")
  Block D: Side-by-side acceptance criteria table
ZONE 5 -- TEST COUPON REQUIREMENTS (22.0"--28.5" / ~6.5")
  Block E: Companion coupon protocol
ZONE 6 -- REJECT CRITERIA (28.5"--32.5" / ~4.0")
  Block F: 4 rejection condition cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Premium Coatings Demand Premium QA` -- 36 pt `#2EC4B6` (Teal).
**Tagline:** `D-Gun produces the densest, hardest, best-bonded coatings in thermal spray. The inspection criteria reflect that -- tighter tolerances, lower porosity limits, and metallographic evaluation that reveals the finest carbide structure in the industry.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating ground to final dimension and surface finish --> After: Coating verified, documented, and released for service`

---

### ZONE 3 -- Inspection Test Matrix (HERO)

**Section label:** `INSPECTION TEST MATRIX -- D-GUN WC-Co` -- Y: 4.4".

**BLOCK B -- 7-Row Test Matrix**

Y: 5.0" to 12.0". Full width within margins (23.0").

Column widths: Test (3.5") | Method / Standard (5.0") | Acceptance Criteria (7.0") | Notes (7.5")

| Test | Method / Standard | Acceptance Criteria | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 (tensile adhesion) | > 80 MPa (reports as "> epoxy strength") | Bond routinely exceeds the 70--80 MPa strength of the FM1000 epoxy adhesive used in ASTM C633 |
| Porosity | ASTM E2109 (image analysis on cross-section) | < 1.0% (typically < 0.5%; often < 0.2%) | Lowest porosity of any thermal spray process |
| Thickness | Eddy current (non-ferrous substrate); mag-gauge (ferrous); ASTM B487 (cross-section) | Per drawing +/- 25 um | Tighter tolerance than HVOF (+/- 50 um) |
| Hardness | ASTM E384 (Vickers microhardness, HV300) | 1200--1500 HV300 (WC-12Co) | Minimum 5 indentations across coating thickness on polished cross-section |
| Surface roughness | Profilometer (Ra) | As-ground: Ra < 0.4 um; superfinished: Ra < 0.1 um | Measured after grinding; as-sprayed Ra 2--5 um is for reference only |
| Microstructure | Metallographic cross-section (unetched + etched) | Uniform carbide distribution; no continuous oxide stringers; no delamination; minimal decarburization | SEM recommended for detailed carbide evaluation |
| Visual | Unaided eye + 10x loupe | No spalling, blistering, orange peel, bare spots, or grinding damage | Performed before and after grinding |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.85".
Test names: Inter Medium 13 pt `#F0EDE8`. Methods: JetBrains Mono 12 pt `#E8A020`. Criteria: Inter Regular 13 pt. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

**BLOCK C -- Metallographic Cross-Section Guide**

Y: 12.5" to 15.3". Two side-by-side panels.

**Left -- Good Microstructure (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `ACCEPTABLE D-GUN MICROSTRUCTURE` Barlow SemiBold 16 pt `#27AE60`
- `Uniform WC carbide distribution throughout binder matrix`
- `No continuous oxide stringers between splats`
- `Porosity < 0.5% -- isolated, round pores only`
- `Minimal decarburization (WC grains retain angular morphology)`
- `Clean substrate-coating interface with no voids`
- `Carbides retain their original size -- no excessive dissolution`

**Right -- Rejectable Microstructure (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `REJECTABLE MICROSTRUCTURE` Barlow SemiBold 16 pt `#E05C5C`
- `Oxide stringers visible as dark continuous lines between splats`
- `Decarburized zones -- rounded or dissolved WC grains (eta-phase W2C or W)`
- `Porosity > 1% or interconnected porosity channels`
- `Interface voids or evidence of contamination at substrate boundary`
- `Banded structure indicating inconsistent detonation parameters`
- `Hardness below 1200 HV indicates decarburization problem`

---

### ZONE 4 -- D-Gun vs. HVOF QA Comparison

**Section label:** `ACCEPTANCE CRITERIA -- D-GUN vs. HVOF (WC-12Co)` -- Y: 15.7".

**BLOCK D -- Side-by-Side Comparison Table**

Y: 16.3" to 21.5". Full width.

Column widths: Property (5.0") | D-Gun Criteria (6.5") | HVOF Criteria (6.5") | Advantage (5.0")

| Property | D-Gun Criteria | HVOF Criteria | Advantage |
|---|---|---|---|
| Porosity | < 0.5% (< 0.2% typical) | < 1% (< 0.5% typical) | D-Gun |
| Bond strength | > 80 MPa (exceeds epoxy) | > 70 MPa (often exceeds epoxy) | D-Gun |
| Hardness (HV300) | 1200--1500 | 1100--1400 | D-Gun |
| Thickness tolerance | +/- 25 um | +/- 50 um | D-Gun |
| Surface roughness (ground) | Ra < 0.4 um | Ra < 0.4 um | Equal |
| Oxide content | < 0.3% | < 0.5% | D-Gun |
| Wear rate (ASTM G65) | 0.5--3 x 10^-7 mm3/Nm | 1--5 x 10^-7 mm3/Nm | D-Gun |

Data: JetBrains Mono Regular, 12 pt. D-Gun values in `#E8A020`. HVOF values in `#2EC4B6`.
"Advantage" column: Inter Medium, 12 pt. D-Gun advantages in `#E8A020`. Equal in `#C8D0D8`.

**Summary callout (below table, Y: 21.0" to 21.5"):**
Rounded rect, full width, H: 0.4", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

`D-Gun wins every quality metric. HVOF wins on throughput and cost. Both exceed hard chrome plating on every measure except deposition cost.` Inter Medium, 13 pt, `#E8A020`, center.

---

### ZONE 5 -- Test Coupon Requirements

**Section label:** `DESTRUCTIVE TEST COUPONS -- SPRAY WITH EVERY BATCH` -- Y: 22.2".

**BLOCK E -- Companion Coupon Protocol**

Y: 22.8" to 28.0".

**Left -- Coupon Procedure (X: 0.5", W: 14.0"):**

Six step cards, vertically stacked.

Each card: W: 13.5", H: 0.75", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Action | Detail |
|---|---|---|---|
| 1 | `#E8A020` | PREPARE TEST COUPONS | Same substrate material as production part; grit-blasted identically; minimum 2 coupons per batch |
| 2 | `#2EC4B6` | MOUNT IN SPRAY BOOTH | Position coupons adjacent to production parts; same standoff distance and spray angle |
| 3 | `#27AE60` | SPRAY SIMULTANEOUSLY | Coupons receive identical coating as production parts -- same parameters, same operator, same session |
| 4 | `#E8A020` | GRIND COUPONS IDENTICALLY | Grind test coupons using same wheel, coolant, and infeed as production parts |
| 5 | `#2EC4B6` | DESTRUCTIVE TESTING | Section for metallography and microhardness; bond test per ASTM C633; porosity per ASTM E2109 |
| 6 | `#27AE60` | CORRELATE TO PRODUCTION | Coupon results represent the production coating. If coupons fail, production parts are suspect. |

Step numbers: Barlow Condensed ExtraBold 18 pt accent color. Action: Inter Medium 13 pt `#F0EDE8`. Detail: Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- Why Coupons (X: 15.0", W: 8.5"):**

Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.

Title: `WHY COMPANION COUPONS?` Barlow SemiBold 18 pt `#27AE60`.

Body (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
D-Gun parts are typically high-value
aerospace components that cannot be
destructively tested.

Companion coupons sprayed alongside
production parts provide the destructive
test data without sacrificing the part.

This is standard aerospace QA practice
and is required by most D-Gun coating
specifications.

The coupon IS the quality record
for the production part.
```

Callout: `1 coupon = 1 ASTM C633 pull + 1 cross-section (porosity + hardness + microstructure). Minimum 2 coupons per batch.` JetBrains Mono 12 pt `#E8A020`.

---

### ZONE 6 -- Reject Criteria

**Section label:** `REJECT CONDITIONS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Condition | Action |
|---|---|---|---|
| 1 | 0.5" | POROSITY > 1% | Strip by grit blast; investigate gas ratios (O2/C2H2), powder charge, and barrel condition; re-spray after root cause corrected |
| 2 | 6.33" | HARDNESS < 1200 HV300 | Indicates decarburization -- O2/C2H2 ratio likely too fuel-rich; verify gas metering calibration; strip and re-spray with corrected parameters |
| 3 | 12.16" | BOND STRENGTH BELOW SPEC | Strip by grit blast; investigate surface preparation (contamination, stale blast, profile); re-blast and re-spray |
| 4 | 18.0" | THICKNESS OUTSIDE TOLERANCE | If below minimum after grinding, strip and re-spray with adequate grinding allowance. If above maximum, additional grinding may be possible if minimum thickness is maintained. |

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- D-Gun`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; ASTM C633, E2109, B487, E384; general industry knowledge; Oerlikon Metco and Praxair Surface Technologies published data. Acceptance criteria shown are typical for WC-12Co D-Gun coatings. Specific aerospace and OEM specifications may impose additional or different requirements.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

## Design Notes

This is the capstone poster for the D-Gun cluster -- and it should feel like it. The test matrix hero table needs to communicate "this is the tightest QA in thermal spray" through the numbers alone. The D-Gun vs. HVOF comparison table is the data anchor that engineers will study -- every row says "D-Gun is better" except throughput. The metallographic cross-section guide is critical because D-Gun microstructure evaluation is how you catch decarburization (the number one way to ruin a D-Gun WC-Co coating). The companion coupon protocol section tells the full story of aerospace QA: you cannot cut up a $10,000 turbine blade, so you prove the coating quality through companion coupons sprayed alongside it. The +/- 25 um thickness tolerance (tighter than HVOF's +/- 50 um) reflects the precision nature of D-Gun work.

---

*Alaina -- Poster #538 -- Construction Workup v1.0 -- 2026-04-26*
