---
Project: Plating Posters Inc
Poster Number: 576
Title: "Temper & Inspection -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.9)"
Technical Source: Tempering (300-375 F, 2+ hours, sub-zero treatment), inspection advantages (no IGO), common LPC-specific defects (soot, non-uniform case, free carbides, grain growth). Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Vacuum carburizing temper and inspection (Stages 8-9 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - Temper
  - Inspection
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #576 -- Construction Workup
## Temper & Inspection -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the LPC cluster. Tempering is identical to gas carburizing (300-375 F, 2+ hours), but inspection is where LPC shines -- no IGO to measure, no surface oxidation to evaluate. One entire inspection step is eliminated. This poster covers the tempering parameters, the inspection advantage, the common LPC-specific defects, and the hardness targets. The defect table is the most critical content for the quality engineer.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Tempering parameters panel (Block B -- HERO):** Temperature, time, sub-zero treatment, double temper for aerospace.
2. **Inspection advantage callout (Block C):** What LPC eliminates from the inspection protocol.
3. **Hardness targets table (Block D):** Surface and core hardness ranges.
4. **Common defects table (Block E):** LPC-specific defects with causes and remedies.
5. **Inspection methods strip (Block F):** Microhardness traverse, metallography, retained austenite.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 12.5" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 8 and 9 highlighted
ZONE 3 -- TEMPERING PARAMETERS HERO (4.2"--12.5" / ~8.3")
  Block B: Temperature, time, sub-zero, double temper
ZONE 4 -- INSPECTION ADVANTAGE (12.5"--15.0" / ~2.5")
  Block C: What LPC eliminates
ZONE 5 -- HARDNESS + DEFECTS (15.0"--28.5" / ~13.5")
  Block D: Hardness targets (left)
  Block E: Common defects table (right, extending below)
ZONE 6 -- INSPECTION METHODS (28.5"--32.5" / ~4.0")
  Block F: Methods strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER & INSPECTION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stages 8 and 9 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Tempering is the same as gas carburizing. Inspection is where LPC pays dividends -- no IGO to measure, no surface oxidation to evaluate. One major rejection cause eliminated before you even pick up the microscope.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 8 and 9 highlighted: Stage 8 fill `#E8A020` (Temper), Stage 9 fill `#27AE60` (Inspection). Others dimmed.
Below: `Before: Quenched parts (martensite + retained austenite)  -->  After: Tempered, inspected, approved for service`

---

### ZONE 3 -- Tempering Parameters (HERO)

**Section label:** `TEMPERING -- STRESS RELIEF WITHOUT HARDNESS LOSS` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Four parameter cards (Y: 5.0" to 12.0")**

Two rows of two cards:

Row 1:

*Card 1 -- Standard Temper (X: 0.5", W: 11.0", H: 3.2"):*
- Title: `STANDARD TEMPER` Barlow SemiBold 18 pt `#E8A020`
- Accent: left `#E8A020`
- Content:
```
Temperature: 300--375 F (149--191 C)
Time: 2 hours minimum at temperature
Atmosphere: Air or nitrogen
Per AMS 2759/7

Low-temperature temper: relieves quench
stress and improves toughness without
significant hardness reduction

Same parameters as gas carburizing --
the tempering step is process-agnostic
```

*Card 2 -- Double Temper (X: 12.0", W: 11.5", H: 3.2"):*
- Title: `DOUBLE TEMPER (AEROSPACE)` Barlow SemiBold 18 pt `#2EC4B6`
- Accent: left `#2EC4B6`
- Content:
```
Required for: 9310 steel and some
aerospace specifications

Cycle: Temper -> Cool to RT -> Temper again
Each temper: 300--375 F for 2+ hours

Purpose: Ensures all fresh martensite
(formed from retained austenite during
first cool) is tempered in second cycle

Not optional -- specification-driven
```

Row 2:

*Card 3 -- Sub-Zero Treatment (X: 0.5", W: 11.0", H: 3.2"):*
- Title: `SUB-ZERO TREATMENT` Barlow SemiBold 18 pt `#2EC4B6`
- Accent: left `#2EC4B6`
- Content:
```
Temperature: -100 to -120 F (-73 to -84 C)
Applied BETWEEN temper cycles

Purpose: Transforms retained austenite
to martensite (RA specification often
requires <10% in outer case)

When required: Specification-driven;
mandatory when RA must be minimized

Method: Dry ice/alcohol bath (-109 F)
or mechanical refrigeration
```

*Card 4 -- Process Sequence (X: 12.0", W: 11.5", H: 3.2"):*
- Title: `FULL SEQUENCE (AEROSPACE)` Barlow SemiBold 18 pt `#27AE60`
- Accent: left `#27AE60`
- Content:
```
1. QUENCH (HPGQ or oil)
2. TEMPER 1: 300--375 F, 2+ hours
3. SUB-ZERO: -100 to -120 F (if required)
4. TEMPER 2: 300--375 F, 2+ hours
5. INSPECT

Total post-quench time: 8--12 hours
for the full aerospace sequence

For non-aerospace: Steps 3 and 4
may be omitted per specification
```

---

### ZONE 4 -- Inspection Advantage

**BLOCK C -- Full-width callout (Y: 12.7" to 14.8")**

Rounded rect fill `#1E2435`, left accent `#27AE60`, H: 1.8".

Title: `WHAT LPC ELIMINATES FROM INSPECTION` Barlow SemiBold 18 pt `#27AE60`

Two-column:

*Left -- ELIMINATED (Emerald):*
```
- IGO measurement (intergranular oxidation)
  Gas carburizing: measure and grind off IGO layer
  LPC: NO IGO EXISTS -- step eliminated entirely

- Surface oxidation evaluation
  Gas carburizing: check for decarburization from
  atmosphere leaks
  LPC: No atmosphere = no surface oxidation
```

*Right -- STILL REQUIRED (Amber):*
```
- Hardness traverse (ECD to 50 HRC)
- Surface hardness (58--63 HRC)
- Core hardness verification
- Retained austenite measurement
- Microstructure evaluation
- Carbide morphology check
- Soot deposit inspection (LPC-specific)
```

---

### ZONE 5 -- Hardness Targets + Defects

**BLOCK D -- Hardness Targets (X: 0.5", W: 11.0", Y: 15.2" to 19.0")**

Section label: `HARDNESS TARGETS` Barlow Condensed ExtraBold 22 pt.

| Location | Range |
|---|---|
| Surface (case) | 58--63 HRC |
| Core (8620) | 30--40 HRC |
| Core (9310) | 35--44 HRC |
| Core (M50NiL) | 38--45 HRC |

Below table:
- `ECD measured to 50 HRC (513 HV) per SAE J423` Inter Medium 13 pt `#27AE60`
- `Total case depth: 1.5--2.0x ECD` Inter Regular 12 pt `#F0EDE8` at 70%

**BLOCK E -- Common Defects Table (X: 0.5", W: 23.0", Y: 19.5" to 28.3")**

Section label: `COMMON DEFECTS -- LPC-SPECIFIC FAILURES` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Defect | Cause | Remedy |
|---|---|---|
| Soot / carbon black deposits | Excessive boost pressure or time; propane vs. acetylene | Reduce boost pressure; switch to C2H2; verify mass flow calibration |
| Non-uniform case (variation across load) | Gas flow pattern in chamber; load density too high | Optimize loading pattern; increase diffuse time between boosts |
| Excessive retained austenite | High surface carbon; high alloy content; insufficient quench | Sub-zero treatment; verify surface carbon via simulation |
| Free carbides at surface | Too many boost cycles without sufficient diffuse | Extend diffuse phases; re-run simulation |
| Grain growth | Temperature too high (above 1900 F without microalloy control) | Reduce temperature; use vacuum-grade fine-grain steel |

Table: Header `#3A4055`, alternating rows. Defect column: Inter Medium 13 pt `#E05C5C`. Cause/Remedy: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Inspection Methods

**Section label:** `INSPECTION METHODS` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four method cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `MICROHARDNESS TRAVERSE` | Knoop or Vickers at incremental depths. ECD = depth to 50 HRC equivalent. Per ASTM E384 / SAE J423. |
| 2 | 6.33" | 5.5" | `METALLOGRAPHY` | Mount, polish, etch (2% Nital). Evaluate martensite quality, carbide morphology, check for soot deposits in case. |
| 3 | 12.16" | 5.5" | `RETAINED AUSTENITE` | Point count or XRD. Must not exceed 20% in outer 10% of case per AMS 2759/7. Sub-zero treat if over limit. |
| 4 | 18.0" | 5.5" | `SURFACE CARBON` | Verified by simulation (not measured in real time). Validate on test coupons by combustion analysis or GDOES. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#27AE60`.
Title: Barlow SemiBold 14 pt `#27AE60`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Temper & Inspection -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7E, SAE J423, ASTM E384. Hardness targets and acceptance criteria are specification-dependent. Tempering parameters must comply with the governing customer or aerospace specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Inspection Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the LPC cluster on a high note -- the inspection advantage is the quality engineer's reward for investing in vacuum carburizing. No IGO measurement means one fewer rejection cause, one fewer grinding operation, and one fewer line item on the inspection report. The defect table is the most critical content for daily reference -- soot deposits and non-uniform case are the two most common LPC-specific failures that operators need to diagnose quickly.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #576 -- Construction Workup v1.0*
*2026-04-26*
