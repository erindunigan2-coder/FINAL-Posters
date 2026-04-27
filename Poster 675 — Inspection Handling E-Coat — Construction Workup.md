---
Project: Plating Posters Inc
Poster Number: 675
Title: "Inspection & Handling -- E-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 3, Section 3.9)"
Technical Source: E-coat inspection methods, bath monitoring parameters, throwing power measurement, and salt spray testing. Values are typical for automotive cathodic epoxy e-coat systems.
Process Scope: E-coat inspection, testing, and bath monitoring -- Stage 9 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoating
  - Inspection
  - QualityControl
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC03
---

# Poster #675 -- Construction Workup
## Inspection & Handling -- E-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of 9 -- the final poster in the E-Coating cluster. Inspection for e-coat goes beyond simple DFT and adhesion. Throwing power measurement (DFT inside vs. outside a test box) is the unique QC tool that validates e-coat's core advantage. Bath monitoring is a daily discipline: pH, conductivity, solids, P/B ratio, MEQ, and UF membrane performance all feed into process control. The full automotive corrosion test suite -- B117 salt spray plus cyclic corrosion (SAE J2334, GMW14872) -- validates the total system.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection test grid (Block B -- HERO):** 3x2 grid of the six primary inspection tests with methods, targets, and pass/fail criteria.
2. **Bath monitoring schedule (Block C):** Two-column daily/weekly monitoring table.
3. **Throwing power concept (Block D):** Callout explaining the test box measurement and DFT ratio.
4. **Salt spray performance table (Block E):** Comparison of e-coat system performance levels.
5. **Troubleshooting strip (Block F):** 4 inspection-related problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Silver)
ZONE 3 -- INSPECTION TEST GRID HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH MONITORING SCHEDULE (14.5"--20.5" / ~6.0")
ZONE 5 -- THROWING POWER + SALT SPRAY (20.5"--26.0" / ~5.5")
ZONE 6 -- TROUBLESHOOTING STRIP (26.0"--32.5" / ~6.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `E-Coat Line -- Testing, Bath Monitoring & Quality Control -- Stage 9 of 9` -- 32 pt `#C8D0D8` (Bright Silver). Y: 1.4".
**Tagline:** `DFT, adhesion, and MEK rub are the basics. Throwing power measurement is the e-coat-specific test that validates the process's core advantage.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#C8D0D8`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cured e-coat primer, fresh from bake oven  -->  After: Validated primer ready for topcoat line (surfacer, basecoat, clearcoat)`

---

### ZONE 3 -- Inspection Test Grid Hero

**Section label:** `THE SIX ESSENTIAL E-COAT TESTS` -- Y: 4.4".

**BLOCK B -- 3x2 Test Grid**

Y: 5.0" to 14.0". Six large test cards.

Each card: Rounded rect W: 7.33", H: 4.2", fill `#1E2435`, radius 6.

| Position | X | Y | Test | Accent | Method | Target | Frequency |
|---|---|---|---|---|---|---|---|
| R1C1 | 0.5" | 5.0" | FILM THICKNESS (DFT) | `#27AE60` | ASTM D7091 magnetic/eddy current | 0.6--1.2 mils (15--30 um); automotive: 0.7--1.0 mil | 3--5 readings/part, min 5 parts/rack |
| R1C2 | 8.17" | 5.0" | ADHESION | `#27AE60` | ASTM D3359 Method B (cross-cut tape pull) | 5B (no removal) | Per lot or per quality plan |
| R1C3 | 15.83" | 5.0" | MEK DOUBLE RUB | `#E8A020` | ASTM D4752 -- MEK-soaked cloth, 2 lb pressure | 100+ double rubs, no softening | Every oven zone change; every shift |
| R2C1 | 0.5" | 9.5" | WET ADHESION | `#E8A020` | Soak panel in DI water 104 F (40 C) for 240 hr; cross-cut within 30 min | 4B--5B after soak | Periodic qualification |
| R2C2 | 8.17" | 9.5" | THROWING POWER | `#2EC4B6` | DFT measurement inside standardized test box (2" x 4" x 12" deep) | Interior/exterior DFT ratio | Per voltage or chemistry change |
| R2C3 | 15.83" | 9.5" | RUPTURE VOLTAGE | `#2EC4B6` | Ramp voltage on wet film until rupture (electrical breakdown) | Indicates film insulation quality | Weekly or per bath change |

Interior per card:
- Top accent strip: 4 pt in accent color
- Test name: Barlow SemiBold 18 pt in accent color
- Method: Inter Regular 13 pt `#F0EDE8` at 70%
- Target: JetBrains Mono 13 pt `#F0EDE8`
- Frequency: Inter Medium 12 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Bath Monitoring Schedule

**Section label:** `BATH MONITORING -- DAILY AND WEEKLY DISCIPLINE` -- Y: 14.7".

**BLOCK C -- Two-Column Monitoring Table (Y: 15.3" to 20.3")**

**Left -- Daily Monitoring (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `DAILY MONITORING` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Method | Target |
|---|---|---|
| pH | pH meter | 5.8--6.2 |
| Conductivity | Conductivity meter | 1,000--1,800 uS/cm |
| Temperature | Thermometer | 85--95 F (29--35 C) |
| Solids (% weight) | Gravimetric (oven dry) | 18--22% |
| P/B ratio | Ash test or centrifuge | 0.15--0.25 |

JetBrains Mono 12 pt for values. Inter Medium 12 pt for labels.

**Right -- Weekly Monitoring (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `WEEKLY MONITORING` Barlow SemiBold 20 pt `#2EC4B6`

| Parameter | Method | Target |
|---|---|---|
| MEQ (acid/100g solids) | Titration | 30--45 |
| Solvent content | GC or distillation | Per supplier spec |
| Rupture voltage | Voltage ramp on wet film | Per supplier spec |
| UF permeate flow rate | Flow meter | >70% of baseline |
| UF permeate conductivity | Conductivity meter | 500--2,000 uS/cm |
| UF pressure differential | Pressure gauge | < 40 psi |

Bottom callout spanning both columns:
- `Bath monitoring is not optional. E-coat chemistry drifts slowly -- by the time you see defects, the bath has been off-spec for days.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Throwing Power + Salt Spray

**Two-column layout (Y: 20.7" to 25.8"):**

**Left -- Throwing Power (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `THROWING POWER MEASUREMENT` Barlow SemiBold 20 pt `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
The e-coat-specific test.

Test box: 2" x 4" x 12" deep
  (standardized steel box, open on one end)

Measure DFT at:
  Outside surface (full exposure)
  2" depth
  6" depth
  12" depth (back of box)

Throwing power index:
  DFT at 12" / DFT at outside

Cathodic e-coat: 8--12" penetration
  into box sections is typical.

Higher voltage = deeper penetration
  (but risk of rupture at edges)
```

Key highlight:
- `This test validates e-coat's core advantage: coating where spray cannot reach.` Inter Medium 13 pt `#2EC4B6`

**Right -- Salt Spray Performance (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `CORROSION PERFORMANCE` Barlow SemiBold 20 pt `#27AE60`

**BLOCK E -- Performance Table**

| System | B117 Salt Spray Hours |
|---|---|
| E-coat alone (no topcoat) on CRS + ZnPO4 | 500--1,000+ |
| Full automotive (e-coat + surfacer + BC/CC) | 1,500--4,000+ |
| E-coat alone on galvanized steel | 1,000--2,000+ |

JetBrains Mono 14 pt for values. Inter Medium 13 pt for labels.

Additional notes:
- `Cyclic corrosion testing (SAE J2334, GMW14872) is more representative of real-world automotive corrosion than B117.` Inter Regular 13 pt `#F0EDE8` at 70%.
- `Most OEMs now specify cyclic testing as the primary corrosion qualification method.` Inter Medium 12 pt `#27AE60`.

---

### ZONE 6 -- Troubleshooting Strip

**Section label:** `INSPECTION FAILURES -- 4 COMMON ISSUES` -- Y: 26.2".

**BLOCK F -- Four Problem Cards (Y: 26.8" to 32.3")**

Four cards in a single row. Gap: 0.33".

Each card: Rounded rect W: 5.5", H: 5.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | LOW DFT IN CAVITIES | Voltage too low, bath conductivity off, or poor throwing power | Increase voltage; check conductivity; profile test box |
| 2 | 6.33" | MEK RUB FAILURE | Undercure -- metal temp below 340 F or time below 20 min | Oven profile with data loggers; adjust zone temps or conveyor speed |
| 3 | 12.16" | ADHESION FAILURE (WET) | Phosphate coating compromised or seal rinse depleted | Check phosphate coating weight; replenish seal rinse |
| 4 | 18.0" | DECLINING THROWING POWER | Bath chemistry drift (MEQ, solids, P/B) or anode degradation | Full bath analysis; check anode box membranes; adjust MEQ |

Interior per card:
- Problem: Barlow SemiBold 16 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- E-Coat`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; automotive e-coat and OEM specifications. Salt spray hours are typical ranges -- actual performance depends on substrate, pretreatment, and formulation.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling E-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the E-Coating cluster. The six-test grid is the hero -- it covers everything from basic DFT to e-coat-specific throwing power and rupture voltage tests. The bath monitoring schedule reinforces that e-coat is not a "set and forget" process. The throwing power callout is the unique differentiator -- no other coating test measures penetration into enclosed cavities. Salt spray performance grounds everything in a number that customers and engineers understand.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #675 -- Construction Workup v1.0*
*2026-04-26*
