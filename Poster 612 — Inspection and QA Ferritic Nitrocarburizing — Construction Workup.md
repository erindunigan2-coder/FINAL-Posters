---
Project: Plating Posters Inc
Poster Number: 612
Title: "Inspection & QA -- Ferritic Nitrocarburizing (FNC / QPQ)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / QPQ, Section 6.7)"
Technical Source: FNC/QPQ inspection -- compound zone thickness (metallographic), surface hardness (Vickers micro/superficial Rockwell), salt spray testing (ASTM B117, 200-500 hr), appearance (matte black), surface roughness (Ra), dimensional change (<0.0002 inch). Common defects and remedies. Per AMS 2753, AMS 2755.
Process Scope: Ferritic nitrocarburizing inspection and quality assurance (Stage 9 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - QPQ
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #612 -- Construction Workup
## Inspection & QA -- Ferritic Nitrocarburizing (FNC / QPQ)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The closing poster for the FNC/QPQ cluster. Inspection for QPQ is distinctive because it includes corrosion testing as a routine quality measure -- unlike most heat treatment processes where corrosion is not part of the inspection protocol. The five key inspection parameters are: compound zone thickness, surface hardness, salt spray resistance, appearance, and dimensional change. The defect table covers the five most common QPQ failures and links each to a root cause and remedy.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Five inspection parameters (Block B -- HERO):** Five parameter cards with target values and measurement methods.
2. **Common defects table (Block D):** Five defects with causes and remedies.
3. **Salt spray testing panel (Block E):** How ASTM B117 testing works and what QPQ results mean.
4. **Acceptance criteria summary strip (Block F):** Quick-reference pass/fail targets.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Emerald)
ZONE 3 -- FIVE INSPECTION PARAMETERS HERO (4.2"--15.5" / ~11.3")
  Block B: Five parameter cards
ZONE 4 -- COMMON DEFECTS TABLE (15.5"--22.0" / ~6.5")
  Block D: Five defects
ZONE 5 -- SALT SPRAY TESTING (22.0"--28.5" / ~6.5")
  Block E: ASTM B117 explained
ZONE 6 -- ACCEPTANCE CRITERIA STRIP (28.5"--32.5" / ~4.0")
  Block F: Pass/fail summary
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ferritic Nitrocarburizing (FNC / QPQ) -- Stage 9 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Five parameters define a good QPQ treatment: compound zone thickness, hardness, salt spray resistance, appearance, and dimensional stability. Corrosion testing is part of routine QA -- that is unique to QPQ among heat treatment processes.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: QPQ-treated, rinsed parts  -->  After: Inspected, documented, released to customer`

---

### ZONE 3 -- Five Inspection Parameters (HERO)

**Section label:** `FIVE INSPECTION PARAMETERS -- THE COMPLETE QPQ QUALITY CHECK` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Five Parameter Cards (Y: 5.0" to 14.5")**

Row 1 (Y: 5.0", three cards):

*Card 1 -- Compound Zone (X: 0.5", W: 7.33", H: 4.5"):*
- Title: `COMPOUND ZONE THICKNESS` Barlow SemiBold 16 pt `#E8A020`
- Accent: left `#E8A020`
- Target: `10--25 micrometers (0.0004--0.001 inch)` JetBrains Mono 14 pt `#E8A020`
- Method:
```
Metallographic cross-section:
- Mount, polish, and etch specimen
- Measure white layer thickness
  at 400--1000x magnification
- Nital or Picral etch reveals
  compound zone clearly

Frequency: Per lot or per specification
Destructive test (sacrifice sample)
```

*Card 2 -- Surface Hardness (X: 8.17", W: 7.33", H: 4.5"):*
- Title: `SURFACE HARDNESS` Barlow SemiBold 16 pt `#27AE60`
- Accent: left `#27AE60`
- Target: `600--1000 HV (substrate-dependent)` JetBrains Mono 14 pt `#27AE60`
- Method:
```
Vickers microhardness:
- On metallographic cross-section
- Load: HV 0.1 to HV 0.5
- Traverse from surface to core

Superficial Rockwell:
- Direct surface measurement
- HR15N or HR30N scale
- Non-destructive screening test

Frequency: Per lot minimum
```

*Card 3 -- Appearance (X: 15.83", W: 7.67", H: 4.5"):*
- Title: `APPEARANCE` Barlow SemiBold 16 pt `#2EC4B6`
- Accent: left `#2EC4B6`
- Target: `Uniform matte black (QPQ)` JetBrains Mono 14 pt `#2EC4B6`
- Method:
```
Visual inspection:
- Uniform matte black finish
- No staining, discoloration,
  or salt residue
- No bare spots or uncoated areas
- Consistent color across all parts

Gray = gas FNC without oxidizing quench
(not QPQ -- lower corrosion performance)

Frequency: 100% visual inspection
Non-destructive
```

Row 2 (Y: 9.8", two cards centered):

*Card 4 -- Salt Spray (X: 0.5", W: 11.0", H: 4.5"):*
- Title: `SALT SPRAY RESISTANCE (ASTM B117)` Barlow SemiBold 16 pt `#27AE60`
- Accent: left `#27AE60`
- Target: `200--500 hours to first red rust (QPQ on 1018)` JetBrains Mono 14 pt `#27AE60`
- Method:
```
ASTM B117 Neutral Salt Spray:
- 5% NaCl solution at 95 F (35 C)
- Parts placed in salt fog chamber
- Inspect at intervals (24, 48, 96,
  200, 336, 500 hours)
- Record time to first red rust

QPQ on 1018 steel: 200--500+ hours
(compare: hard chrome = 24--96 hours)

Frequency: Per qualification lot or
per customer specification
Destructive test (salt spray panels
or sacrificial parts)
```

*Card 5 -- Dimensional Change (X: 12.0", W: 11.5", H: 4.5"):*
- Title: `DIMENSIONAL CHANGE` Barlow SemiBold 16 pt `#C8D0D8`
- Accent: left `#C8D0D8`
- Target: `<0.0002 inch (5 micrometers) typical` JetBrains Mono 14 pt `#C8D0D8`
- Method:
```
Before/after measurement:
- Measure critical dimensions
  before FNC treatment
- Measure same dimensions after
  complete QPQ cycle
- Record growth per surface

Expected: negligible (<0.0002")
If growth exceeds tolerance:
check bath temperature (too high
= more growth) and immersion time

Frequency: Per qualification;
spot-check per lot for critical
tolerance parts
```

---

### ZONE 4 -- Common Defects Table

**Section label:** `COMMON DEFECTS -- QPQ FAILURE MODES` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#E05C5C`.

**BLOCK D -- Defect Table (Y: 16.3" to 21.8")**

| Defect | Cause | Remedy |
|---|---|---|
| Poor corrosion resistance (salt spray fails early) | Insufficient oxidizing quench time; poor polish quality (Ra too high) | Extend Q1/Q2 time to full 30 min; improve polish to Ra 8--16 micro-inch specification |
| Thin or absent compound zone | Low bath temperature (below 1050 F); depleted cyanate (CNO below 35%) | Verify bath temperature; analyze salt composition and replenish to 35--40% CNO |
| Staining or discoloration | Salt residue not fully rinsed; contaminated oxidizing bath; cross-contamination | Improve rinse thoroughness; maintain bath purity; extend rinse time |
| Distortion | Part previously hardened by another method; FNC temperature exceeded prior temper temperature | Verify thermal history compatibility before processing; FNC temp must not exceed prior temper temp |
| Pitting (surface micro-pits) | Moisture on parts before salt bath immersion (steam explosion at micro-scale) | Improve preheat drying step; extend preheat time; verify no condensation during transfer |

Table: Header `#3A4055`, alternating rows. Defect column: Inter Medium 13 pt `#E05C5C`. Cause/Remedy: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Salt Spray Testing

**Section label:** `SALT SPRAY TESTING -- ASTM B117 EXPLAINED` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- How It Works (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `THE TEST` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
ASTM B117 NEUTRAL SALT SPRAY:

1. Prepare test panels or parts
2. Place in salt fog cabinet
3. Cabinet atomizes 5% NaCl solution
   at 95 F (35 C) continuously
4. Humid, corrosive salt fog surrounds
   the parts 24/7
5. Inspect at specified intervals
6. Record time to FIRST RED RUST
   (base metal corrosion visible)

THE TEST IS ACCELERATED:
Salt spray hours do NOT equal
real-world exposure hours.
Salt spray is a comparative test --
it ranks treatments against each
other, not against calendar time.

INDUSTRY STANDARD:
Most QPQ specifications require
minimum 200 hours to first red
rust on a low-carbon steel panel.
```

*Right -- What Results Mean (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `INTERPRETING QPQ RESULTS` Barlow SemiBold 18 pt `#27AE60`

Content:
```
200--500 HOURS ON 1018 STEEL:
This is the Watson-verified range for
QPQ on low-carbon steel. Actual hours
depend on polish quality, bath
condition, and oxidizing quench time.

FACTORS THAT IMPROVE HOURS:
- Better polish (lower Ra)
- Longer oxidizing quench (30 min > 15 min)
- Fresh, well-maintained salt baths
- Good rinse (no residual salt)

FACTORS THAT REDUCE HOURS:
- Poor polish (high Ra = pits exposed)
- Short oxidizing quench
- Depleted or contaminated baths
- Salt residue on finished parts

COMPARISON CONTEXT:
Hard chrome plate: 24--96 hours
(QPQ is 2--10x better)

Black oxide: 1--4 hours
(QPQ is 50--500x better)
```

---

### ZONE 6 -- Acceptance Criteria Strip

**Section label:** `QUICK-REFERENCE ACCEPTANCE CRITERIA` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Five criteria cards (Y: 29.4" to 32.3")**

| Card | X | W | Parameter | Pass Criteria |
|---|---|---|---|---|
| 1 | 0.5" | 4.4" | `COMPOUND ZONE` | 10--25 um minimum. Continuous, uniform. No gaps. |
| 2 | 5.2" | 4.4" | `HARDNESS` | 600--1000 HV (substrate-dependent). Meets specified minimum. |
| 3 | 9.9" | 4.4" | `SALT SPRAY` | Minimum 200 hr (ASTM B117) to first red rust on 1018 test panel. |
| 4 | 14.6" | 4.4" | `APPEARANCE` | Uniform matte black. No staining, salt residue, or bare spots. |
| 5 | 19.3" | 4.2" | `DIMENSIONS` | Within tolerance. Growth typically <0.0002 inch per surface. |

Each: Rounded rect H: 2.7", fill `#1E2435`, top accent 4 pt `#27AE60`.
Title: Barlow SemiBold 14 pt `#27AE60`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & QA -- Ferritic Nitrocarburizing (FNC / QPQ)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755, ASTM B117, ASTM E384. Acceptance criteria are specification-dependent. Salt spray results of 200-500 hours reflect the Watson-verified range for QPQ on low-carbon steel. Actual results vary by substrate, bath condition, and process execution.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table. **Export:** Six files.

---

## Design Notes

This poster closes the FNC/QPQ cluster with the quality engineer's reference. The five-parameter hero is organized by importance: compound zone and hardness (the metallurgical requirements), salt spray (the corrosion requirement), appearance (the visual requirement), and dimensional change (the precision requirement). The salt spray testing panel deserves extra space because ASTM B117 is unfamiliar to many heat treaters -- they know hardness testing cold but may never have run a salt spray cabinet. The acceptance criteria strip at the bottom is the one-line-per-parameter summary for the production floor.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #612 -- Construction Workup v1.0*
*2026-04-26*
