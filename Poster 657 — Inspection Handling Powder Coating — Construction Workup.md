---
Project: Plating Posters Inc
Poster Number: 657
Title: "Inspection & Handling -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.9"
Technical Source: Industry-standard inspection tests for powder coating -- DFT measurement, adhesion (cross-cut), pencil hardness, mandrel bend, impact resistance, MEK rub, chemical spot tests, and salt spray. Plus handling/packaging requirements.
Process Scope: Inspection and handling for powder coating (Stage 8 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - Inspection
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #657 -- Construction Workup
## Inspection & Handling -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 9. The final quality gate before parts leave the line. The hero is a test method matrix: DFT, adhesion, hardness, flexibility, cure verification (MEK), chemical resistance, and salt spray -- with ASTM standards, procedures, and pass/fail criteria. This is the QC technician's wall reference. Handling rules round out the poster: cool before handling, clean gloves, no surface-to-surface contact.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Test method matrix (Block B -- HERO):** 7-row table with test name, ASTM standard, procedure summary, and pass criteria.
2. **Salt spray performance table (Block C):** Pretreatment + powder chemistry combinations with expected B117 hours.
3. **DFT measurement callout (Block D):** Magnetic vs. eddy current, measurement frequency.
4. **Handling rules panel (Block E):** Temperature, gloves, packaging.
5. **Defect grid (Block F):** 6 inspection failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Inspection (Amber)
ZONE 3 -- TEST METHOD MATRIX HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- SALT SPRAY TABLE + DFT MEASUREMENT (15.5"--21.0" / ~5.5")
ZONE 5 -- HANDLING RULES + PACKAGING (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID -- INSPECTION FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- The Quality Gate` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Seven tests. Seven answers. If the coating passes these, it is ready for the customer. If it fails even one, find the root cause before the next rack enters the oven.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Inspection -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cured powder-coated part --> After: Verified, documented, packaged for shipment`

---

### ZONE 3 -- Test Method Matrix Hero

**Section label:** `THE SEVEN TESTS -- YOUR QUALITY CHECKLIST` -- Y: 4.4".

**BLOCK B -- Test Matrix Table**

Y: 5.0" to 15.0". Full-width table.

| Test | ASTM Standard | Method | Pass Criteria | Frequency |
|---|---|---|---|---|
| Film Thickness (DFT) | D7091 | Magnetic gauge (steel) or eddy current (Al) -- 3--5 readings per part | Per customer spec; general +/- 0.5 mil from target | Min 5 parts per rack/batch |
| Adhesion (Cross-Cut) | D3359 Method B | Score lattice (6 or 11 cuts), apply tape, pull at 180 deg | 4B--5B (no removal or trace removal) | Per batch or shift change |
| Adhesion (X-Cut) | D3359 Method A | Score X, apply tape, pull | No removal at intersection | Quick field check |
| Pencil Hardness | D3363 | Push calibrated pencils (6B to 9H) across film | Hardest pencil that does NOT cut through; typical F to 3H | Per batch |
| Flexibility (Mandrel Bend) | D522 | Bend coated panel over cylindrical mandrel (1/8" to 1" dia) | No cracking at specified mandrel; typical 1/8" pass | Per batch or chemistry change |
| Impact Resistance | D2794 | Drop weighted tup onto panel; report inch-pounds | Typical 80--160 in-lb direct impact | Per batch |
| Cure Verification (MEK Rub) | D4752 | MEK-soaked cloth, 50 double rubs, 2 lb pressure | 50+ rubs with no softening or color transfer | Per oven load or shift |

Header: Barlow SemiBold 14 pt on `#3A4055`. Data: JetBrains Mono 11 pt, `#F0EDE8`. ASTM standards: `#E8A020`.

Highlight row for MEK Rub with subtle `#E8A020` at 8% fill -- this is the most critical single test.

---

### ZONE 4 -- Salt Spray Table + DFT Measurement

**Section label:** `SALT SPRAY PERFORMANCE AND DFT FUNDAMENTALS` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 20.8"):**

**Left -- Salt Spray Table (X: 0.5", W: 11.0"):**

Title: `EXPECTED SALT SPRAY PERFORMANCE (ASTM B117)` -- Barlow SemiBold, 16 pt, `#F0EDE8`

| Pretreatment + Powder | Expected B117 Hours |
|---|---|
| Iron phosphate + polyester | 500--750 hr |
| Zinc phosphate + polyester | 1,000--1,500 hr |
| Iron phosphate + epoxy (interior) | 1,000+ hr |
| Nanoceramic + polyester | 500--750 hr |

Bottom note: `Scribed panels per ASTM D1654. Results depend on substrate, pretreatment quality, and film thickness.` -- Inter Regular 12 pt at 70%.

**Right -- DFT Measurement (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `DFT MEASUREMENT BASICS` -- Barlow SemiBold, 18 pt, `#E8A020`

Body:
- `STEEL substrate: Magnetic gauge (Type 1 per D7091)`
- `ALUMINUM substrate: Eddy current gauge (Type 2 per D7091)`
- `Take 3--5 readings per part, minimum 5 parts per batch`
- `General tolerance: +/- 0.5 mil from target`
- `Calibrate gauge on uncoated substrate or certified shims`
- `Avoid edges and corners -- DFT varies at geometric transitions`

---

### ZONE 5 -- Handling Rules + Packaging

**Section label:** `HANDLING AND PACKAGING -- PROTECT THE FINISH` -- Y: 21.2".

**Two-column layout (Y: 21.8" to 26.3"):**

**Left -- Handling Rules (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`.
Title: `HANDLING RULES` -- Barlow SemiBold, 18 pt, `#E05C5C`

Rules (Inter Medium 14 pt):
1. `Cool to below 120 F (49 C) before ANY handling`
2. `Fingerprints embed permanently in warm powder film`
3. `Clean cotton or nitrile gloves ONLY`
4. `Silicone-contaminated gloves cause fish-eye defects on the NEXT batch`
5. `No bare-hand contact with coated surfaces`
6. `Inspect BEFORE removing from rack`

**Right -- Packaging (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `PACKAGING FOR SHIPMENT` -- Barlow SemiBold, 18 pt, `#27AE60`

Rules:
- `No surface-to-surface contact between coated parts`
- `Foam dividers between layers`
- `Kraft paper interleaving for flat panels`
- `Bubble wrap for complex shapes`
- `Cardboard edge protectors for long parts`
- `Mark packaging: COATED PARTS -- HANDLE WITH CARE`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN INSPECTION FINDS PROBLEMS -- 6 COMMON FAILURES` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | LOW DFT | `#E8A020` | Insufficient powder deposition | Increase flow rate, reduce gun distance, check hooks |
| R1C2 | ADHESION FAIL (0B--3B) | `#E05C5C` | Pretreatment failure or contamination | Investigate upstream: clean, convert, dry |
| R1C3 | MEK FAIL (< 50 RUBS) | `#E05C5C` | Undercure -- insufficient metal temp or time | Profile oven with data logger; increase cure |
| R2C1 | MANDREL BEND CRACK | `#E8A020` | Overcure (brittle film) or wrong chemistry | Reduce cure; check powder supplier TDS |
| R2C2 | LOW IMPACT RESISTANCE | `#E05C5C` | Overcure or undercure (both reduce impact) | Profile oven; test with MEK rub to distinguish |
| R2C3 | HANDLING DAMAGE | `#2EC4B6` | Parts handled while warm or with contaminated gloves | Enforce cool-down rule; clean glove protocol |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM test method standards; Powder Coating Institute references. Specific pass/fail criteria depend on customer specification and application requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The test matrix hero is the beating heart of this poster -- seven rows, seven tests, every QC technician's wall reference. The MEK rub row gets a subtle highlight because it's the single most important cure verification test. The salt spray table gives the quality engineer expected performance numbers to quote to customers. The handling section is deceptively critical: more powder coat jobs are ruined by warm handling and silicone contamination than by any process failure.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #657 -- Construction Workup v1.0*
*2026-04-26*
