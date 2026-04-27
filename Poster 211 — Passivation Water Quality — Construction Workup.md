---
Project: Plating Posters Inc
Poster Number: 211
Title: "Passivation (Stainless Steel) -- Water Quality"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.5)"
Technical Source: Water quality requirements for the pre-passivation rinse and all rinse stages in stainless steel passivation. Covers chloride limits, DI/RO requirements, temperature considerations, and the critical importance of chloride-free water in contact with actively dissolving stainless.
Process Scope: Stainless steel passivation -- Stage 4 water quality / pre-passivation rinse
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - WaterQuality
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #211 -- Construction Workup
## Passivation (Stainless Steel) -- Water Quality

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the water quality poster for CC-08. In the Process Flow (Poster 207), this stage was labeled "Water Quality / Pre-Passivation" -- it occupies the conceptual space between cleaning and passivation, focused on the water that contacts parts at every stage.

For passivation, water quality is not a general best practice -- it is a specification requirement. ASTM A967 and AMS 2700 reference water quality explicitly. Chloride in water is the most common and most dangerous contaminant because stainless steel is uniquely susceptible to chloride-induced pitting -- and during passivation, the surface is actively dissolving, making it even MORE vulnerable.

This poster consolidates all water quality guidance for the entire passivation sequence into one reference.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set.

### Limitations to Flag

1. **Water quality overview (Block B -- HERO):** Comprehensive water specs for each stage.
2. **Chloride pitting mechanism (Block C):** Why chloride is uniquely dangerous during passivation.
3. **DI/RO system basics (Block D):** What these systems do and how to maintain them.
4. **Water quality monitoring schedule (Block E).**
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- WATER QUALITY BY STAGE / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Water quality requirements by process stage
  Block C: Chloride pitting mechanism during passivation

ZONE 3 -- DI / RO SYSTEM BASICS (15.5"--22.0" / ~6.5" tall)
  Block D: What DI and RO systems do; maintenance essentials

ZONE 4 -- MONITORING SCHEDULE (22.0"--28.5" / ~6.5" tall)
  Block E: Water quality monitoring frequency and methods

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Stage 4 -- Water Quality`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Chloride-free. Every rinse. Every stage. The water that touches your parts is as important as the acid that passivates them.`
- Y: 2.2"

---

### ZONE 2 -- Water Quality by Stage (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WATER QUALITY REQUIREMENTS -- BY PROCESS STAGE`

---

**BLOCK B -- Stage-by-Stage Water Quality Table**

Y: 3.8" to 9.5". Full width.

Rounded rect, X: 0.5", Y: 3.8", W: 23.0", H: 5.5", fill `#1E2435`, radius 8.

Column widths: Stage (4.5") | Water Type (4.0") | Conductivity (3.0") | Chloride Max (3.0") | Notes (8.5")

| Stage | Water Type | Conductivity | Cl- Max | Notes |
|---|---|---|---|---|
| Post-Clean Rinse | DI/RO (aerospace); low-Cl tap (general) | < 500 uS/cm | < 25 ppm | Remove cleaner; no Cl carryover into acid |
| Post-Pickle Rinse | DI/RO preferred | < 200 uS/cm | < 10 ppm | Remove HF/HNO3 residues completely |
| Pre-Passivation Rinse | DI or RO | < 50 uS/cm | < 5 ppm | Last wet stage before acid; chloride-free critical |
| Passivation Bath Makeup | DI water | < 10 uS/cm | < 1 ppm | Chloride in the acid bath causes pitting during passivation |
| Post-Acid Rinse | DI/RO (aerospace/medical); low-Cl (general) | < 200 uS/cm | < 10 ppm | Remove all acid; prevent staining |
| Final Rinse (if used) | DI water | < 10 uS/cm | < 1 ppm | Spot-free drying for appearance-sensitive parts |

Data: JetBrains Mono 12 pt. Stage names: Inter Medium 13 pt.
Header: Barlow SemiBold 13 pt. Alternating rows: `#1E2435` / `#252B3D`.

---

**BLOCK C -- Chloride Pitting Mechanism**

Y: 10.0" to 15.0". Two panels.

**Left -- Why Chloride Is Uniquely Dangerous:**
- Rounded rect, X: 0.5", Y: 10.0", W: 11.0", H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `WHY CHLORIDE PITS STAINLESS` -- Barlow SemiBold, 20 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Chloride ions (Cl-) penetrate the Cr2O3
passive film at defect sites, inclusions,
or grain boundaries.

Once through, Cl- creates a local acidic
environment (autocatalytic pit):
  Metal dissolves -> M+ + Cl- -> MCl2
  MCl2 + H2O -> M(OH)2 + 2HCl
  HCl lowers pH locally -> MORE dissolution

The pit feeds itself. Once initiated, it
accelerates unless the chloride is removed.

During passivation, the surface is ACTIVELY
being dissolved by acid. Chloride accelerates
this dissolution in an uncontrolled, localized
manner -- causing pitting instead of uniform
passive film formation.
```

**Right -- Chloride Limits by Application:**
- Rounded rect, X: 12.0", Y: 10.0", W: 11.5", H: 4.8", fill `#1E2435`, left accent `#27AE60`
- Title: `CHLORIDE LIMITS` -- Barlow SemiBold, 20 pt, `#27AE60`

Table:
| Application | Max Chloride (ppm) | Water Type |
|---|---|---|
| General industrial | < 25 | Low-Cl tap or softened |
| Food / pharmaceutical | < 10 | RO or DI |
| Aerospace (AMS 2700) | < 5 | DI |
| Medical / implant | < 1 | High-purity DI |
| Semiconductor (SEMI F42) | < 0.1 | Ultra-pure DI |

Data: JetBrains Mono 12 pt.

Below table: `Lower alloy grades (410, 420) are MORE susceptible to chloride pitting than high-alloy grades (316, 317). If processing low-Cr martensitic grades, use the tightest chloride limit you can achieve.` -- Inter Medium 12 pt `#E8A020`

---

### ZONE 3 -- DI / RO System Basics

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DI AND RO WATER SYSTEMS -- THE ESSENTIALS`

**BLOCK D -- Two System Panels**

Y: 16.3" to 21.8".

**Left -- DI (Deionized) Water:**
- Rounded rect, X: 0.5", Y: 16.3", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `DEIONIZED (DI) WATER` -- Barlow SemiBold, 18 pt, `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`):
```
How it works:
  Ion exchange resins remove dissolved ions
  (Ca2+, Mg2+, Na+, Cl-, SO42-, etc.)
  Produces water at < 5 uS/cm typically

Output quality:
  Conductivity: < 10 uS/cm (often < 1)
  Chloride: < 1 ppm
  TDS: < 5 ppm

Maintenance:
  - Monitor outlet conductivity continuously
  - Regenerate or replace resin beds when
    conductivity rises above setpoint
  - Typical resin life: weeks to months
    (depends on feed water quality)
  - Alarm at 20 uS/cm for early warning
```

**Right -- RO (Reverse Osmosis) Water:**
- Rounded rect, X: 12.0", Y: 16.3", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `REVERSE OSMOSIS (RO) WATER` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`):
```
How it works:
  Semi-permeable membrane rejects 95--99%
  of dissolved ions under pressure

Output quality:
  Conductivity: 10--50 uS/cm
  Chloride: typically < 5 ppm
  TDS: 5--25 ppm

Maintenance:
  - Replace pre-filters per schedule
  - Monitor membrane performance (rejection %)
  - Replace membranes every 2--5 years
  - Watch for biofouling in warm environments

RO + DI polisher = best of both worlds
  (RO removes bulk; DI polishes to < 1 uS/cm)
```

---

### ZONE 4 -- Monitoring Schedule

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WATER QUALITY MONITORING SCHEDULE`

**BLOCK E -- Monitoring Table**

Y: 22.9" to 28.3". Rounded rect, X: 0.5", W: 23.0", H: 5.0", fill `#1E2435`, radius 8.

| Parameter | Method | Frequency | Target | Action if Out of Spec |
|---|---|---|---|---|
| Conductivity | Inline meter (continuous) | Continuous | < 50 uS/cm (DI rinses) | Regenerate/replace DI resin |
| Chloride | AgNO3 spot test or test strip | Daily | < 25 ppm (general); < 5 ppm (aerospace) | Switch to DI; investigate source |
| pH | pH meter or strip | Daily | 5.5--7.5 | Investigate acid or alkaline contamination |
| TDS | TDS meter | Weekly | < 25 ppm | Indicates DI/RO system degradation |
| Iron (Fe) | Colorimetric test kit | Weekly | < 0.5 ppm | Possible upstream corrosion or contamination |

Data: JetBrains Mono 11 pt. Headers: Barlow SemiBold 13 pt.
Alternating rows.

Below table:
- Text: `Continuous conductivity monitoring with an alarm is the single most cost-effective water quality investment. It catches DI system failures before they reach your parts.` -- Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PITTING IN PASSIVATION BATH | Chloride in makeup water or drag-in from rinse | Test bath for chloride; use DI for makeup; improve rinse |
| 2 | 6.33" | DI CONDUCTIVITY RISING | Resin exhaustion; RO membrane fouling | Regenerate resin; replace RO membrane; check pre-filters |
| 3 | 12.16" | WATER SPOTS AFTER DRYING | Mineral deposits from tap water in final rinse | Use DI for final rinse; improve air knife drainage |
| 4 | 18.0" | STAINING BETWEEN STAGES | Contaminated rinse water; long dwell between stages | Improve rinse quality; speed up transfers |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Water Quality`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Water quality parameters shown are typical for stainless steel passivation per ASTM A967 and AMS 2700. Specific chloride limits vary by alloy, application, and specification. Consult your process supplier and applicable specification for application-specific requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Water Quality -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster consolidates water quality guidance that was scattered across Posters 209 (rinse) and the research brief into a single comprehensive reference. The stage-by-stage water quality table (Zone 2) is the most actionable element -- an operator can look at which stage they are running and immediately see the conductivity and chloride targets. The chloride pitting mechanism panel gives the "why" that makes the specifications stick.

The DI/RO system basics in Zone 3 acknowledge that many shops do not understand their water treatment systems well enough to maintain them. This poster teaches the minimum: what the system does, what to monitor, and when to act.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #211 -- Construction Workup v1.0*
*2026-04-26*
