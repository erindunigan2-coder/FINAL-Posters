---
Project: Plating Posters Inc
Poster Number: 567
Title: "Temper & Inspection -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.9)"
Technical Source: Gas carburizing temper and inspection -- tempering parameters, sub-zero treatment, hardness targets, case depth measurement (SAE J423), metallographic examination, common defects table. Per ASM Handbook Vol. 4, AMS 2759/7, ASTM E384.
Process Scope: Gas carburizing temper and inspection (Stages 7--9 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - Temper
  - Inspection
  - Metallography
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #567 -- Construction Workup
## Temper & Inspection -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Gas Carburizing cluster. Tempering relieves quench stress and improves toughness; inspection verifies that everything upstream worked. This poster covers tempering parameters, sub-zero treatment for retained austenite, hardness targets, all four case depth measurement methods (per SAE J423), metallographic examination criteria, and the common defect table that ties the entire cluster together. If a part fails inspection, this poster tells you what went wrong and which upstream poster to revisit.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temper parameters panel (Block B -- left HERO):** Temperature, time, double temper, sub-zero treatment.
2. **Case depth measurement methods (Block B -- right HERO):** Four methods per SAE J423 with descriptions.
3. **Hardness targets table (Block D):** Surface and core hardness for common steel grades.
4. **Metallographic criteria panel (Block E):** What to look for under the microscope -- retained austenite, IGO, carbide network, NMTP.
5. **Common defects table (Block F):** Six defects with causes and remedies -- the cluster's troubleshooting capstone.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--9 highlighted (Amber + Emerald)
ZONE 3 -- TEMPER & CASE DEPTH HERO (4.2"--15.0" / ~10.8")
  Block B Left: Temper parameters + sub-zero treatment
  Block B Right: Case depth measurement methods (SAE J423)
ZONE 4 -- HARDNESS TARGETS (15.0"--22.0" / ~7.0")
  Block D: Surface and core hardness by steel grade
ZONE 5 -- METALLOGRAPHIC CRITERIA (22.0"--28.5" / ~6.5")
  Block E: Retained austenite, IGO, carbide network, NMTP
ZONE 6 -- COMMON DEFECTS TABLE (28.5"--32.5" / ~4.0")
  Block F: Six-defect reference table
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER & INSPECTION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stages 7-9 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The temper relieves stress. The inspection reveals truth. Every defect found here traces back to a decision made upstream. This poster closes the loop.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7, 8, 9 highlighted: Stage 7 (Wash) `#2EC4B6`, Stage 8 (Temper) `#E8A020`, Stage 9 (Inspect) `#27AE60`. Others dimmed.
Below: `Before: As-quenched parts -- hard, stressed, brittle  -->  After: Tempered, inspected, accepted -- ready for service`

---

### ZONE 3 -- Temper & Case Depth Measurement (HERO)

**Section label:** `TEMPERING AND CASE DEPTH VERIFICATION` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Left: Temper Parameters (X: 0.5", W: 11.0")**

Y: 5.0" to 14.5". Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `TEMPERING PARAMETERS` Barlow SemiBold 20 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
TEMPERATURE:
300--375 F (149--191 C)
Low-temperature temper -- relieves quench
stress without significant hardness loss

TIME:
2 hours minimum at temperature per AMS 2759/7
Many shops: 2--4 hours for consistency

ATMOSPHERE:
Air or nitrogen (N2 preferred for
clean parts; air acceptable)

DOUBLE TEMPER:
Required for some aerospace applications
(especially 9310 steel). Two full temper
cycles with cooling to room temp between.

SUB-ZERO TREATMENT (CRYOGENIC):
-100 to -120 F (-73 to -84 C)
- Applied BETWEEN first and second temper
- Transforms retained austenite to martensite
- Required when RA must be below 10%
- Typical hold: 1--2 hours at temperature
- Parts must be tempered AFTER sub-zero
  (fresh martensite is untempered)

WHY TEMPER?
As-quenched martensite is hard but brittle.
Tempering trades a few points of hardness
for significant improvement in toughness
and dimensional stability.
```

**BLOCK B -- Right: Case Depth Measurement (X: 12.0", W: 11.5")**

Y: 5.0" to 14.5". Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `CASE DEPTH MEASUREMENT (SAE J423)` Barlow SemiBold 20 pt `#27AE60`

Four method sub-panels stacked vertically:

*Method 1 -- Microhardness Traverse:*
- Subtitle: `MICROHARDNESS TRAVERSE` Barlow SemiBold 14 pt `#27AE60`
```
THE PRIMARY METHOD
Knoop or Vickers indentations at incremental
depths on polished cross-section
ECD = depth where hardness equals 50 HRC
(or 513 HV equivalent)
Per ASTM E384 for test procedure
Most accurate and most commonly specified
```

*Method 2 -- Chemical (Step Machining):*
- Subtitle: `CHEMICAL METHOD` Barlow SemiBold 14 pt `#2EC4B6`
```
Step-machine layers from surface; analyze
carbon content at each depth by combustion
analysis. Laboratory method -- slow but
gives actual carbon profile (not just
hardness approximation).
```

*Method 3 -- File Test:*
- Subtitle: `FILE TEST` Barlow SemiBold 14 pt `#E8A020`
```
QUALITATIVE SHOP-FLOOR CHECK
Hardened file will not cut properly
hardened case (58+ HRC). Quick go/no-go
but cannot measure depth. Not acceptable
for specification compliance.
```

*Method 4 -- Fracture Test:*
- Subtitle: `FRACTURE TEST` Barlow SemiBold 14 pt `#E8A020`
```
Break test piece and examine fracture
surface. Case appears fine-grained and
lighter than core. Gives visual ECD
estimate. Used for quick lot verification.
```

---

### ZONE 4 -- Hardness Targets

**Section label:** `HARDNESS TARGETS BY STEEL GRADE` -- Y: 15.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Hardness Table (Y: 15.9" to 21.8")**

Full-width rounded rect fill `#1E2435`.

| Steel Grade | Surface (HRC) | Core (HRC) | Typical Application |
|---|---|---|---|
| 8620 | 58--62 | 30--40 | General purpose gears, pinions |
| 4320 | 58--63 | 33--43 | Heavy-duty gears, high core toughness |
| 9310 | 59--63 | 35--44 | Aerospace gears (AMS 6265) |
| 3310 | 58--63 | 30--40 | High hardenability gears |
| 4620 | 58--62 | 28--38 | Worm gears, shafts |
| 4820 | 59--63 | 35--44 | Heavy sections, high core strength |
| 1018/1020 | 55--60 | 15--25 | Light-duty pins, bushings |

Data: JetBrains Mono 11 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt. Alternating rows.

Bottom note: `Surface hardness depends on surface carbon content and quench severity. Core hardness depends on alloy content and section size. Both are measured per ASTM E18 (Rockwell).` Inter Medium 12 pt `#E8A020`.

---

### ZONE 5 -- Metallographic Criteria

**Section label:** `METALLOGRAPHIC EXAMINATION -- WHAT TO LOOK FOR` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Four criteria cards (Y: 22.9" to 28.3")**

2x2 grid:

| Card | X | Y | W | H | Criterion | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 22.9" | 11.0" | 2.5" | Retained Austenite | `#E8A020` |
| 2 | 12.0" | 22.9" | 11.5" | 2.5" | Intergranular Oxidation (IGO) | `#E05C5C` |
| 3 | 0.5" | 25.7" | 11.0" | 2.5" | Carbide Network | `#E05C5C` |
| 4 | 12.0" | 25.7" | 11.5" | 2.5" | NMTP (Non-Martensitic) | `#E8A020` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Retained Austenite:*
- Title: `RETAINED AUSTENITE (RA)` Barlow SemiBold 16 pt `#E8A020`
- Content: `Austenite that did not transform to martensite during quench. Must not exceed 20% per AMS 2759/7 in outer 10% of case. Measured by point count on metallographic section or by XRD. Excessive RA: sub-zero treatment at -100 to -120 F.`

*Card 2 -- Intergranular Oxidation (IGO):*
- Title: `INTERGRANULAR OXIDATION (IGO)` Barlow SemiBold 16 pt `#E05C5C`
- Content: `Dark-etching network along prior austenite grain boundaries in outer 0.0005--0.001". Caused by oxidation of Cr, Mn, Si by CO2/H2O in endo atmosphere. MUST be removed by grinding (min 0.002--0.003" stock removal). Eliminated entirely by vacuum carburizing.`

*Card 3 -- Carbide Network:*
- Title: `CARBIDE NETWORK` Barlow SemiBold 16 pt `#E05C5C`
- Content: `Continuous or semi-continuous network of iron carbides (Fe3C) at prior austenite grain boundaries. Caused by surface carbon exceeding ~1.0%. Makes case brittle -- cracks initiate at carbide network. Remedy: reduce Cp during boost; extend diffuse cycle to dissolve carbides.`

*Card 4 -- NMTP:*
- Title: `NON-MARTENSITIC TRANSFORMATION PRODUCTS` Barlow SemiBold 16 pt `#E8A020`
- Content: `Bainite or pearlite in the case -- indicates insufficient quench severity. Part did not cool fast enough to form martensite. Remedy: increase agitation, use faster oil, increase H-factor, or switch to higher-hardenability steel.`

---

### ZONE 6 -- Common Defects Table

**Section label:** `COMMON DEFECTS -- CAUSE AND REMEDY` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Defect Table (Y: 29.4" to 32.3")**

Rounded rect full width, fill `#1E2435`.

| Defect | Cause | Remedy |
|---|---|---|
| Excess retained austenite | High surface C, high alloy, insufficient quench | Reduce Cp; sub-zero treat; verify quench |
| IGO | CO2 and H2O at grain boundaries | Vacuum carburize; or grind 0.002--0.003" |
| Decarburization | Air leaks, low Cp, improper purge | Fix seals; verify atmosphere composition |
| Soft spots | Part contact, gas starvation, oil residue | Improve fixturing; increase agitation; clean oil |
| Carbide network | Surface C >1.0%, insufficient diffuse | Lower Cp; extend diffuse cycle |
| Grain growth | Temp too high, time too long | Reduce temp; use fine-grain steels |

Data: JetBrains Mono 10 pt `#F0EDE8`. Defect: Inter Medium 11 pt `#E05C5C`. Alternating rows.

---

### ZONE 7 -- Footer

Standard. Title: `Temper & Inspection -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7, SAE J423, ASTM E384, ASTM E18. Hardness targets and metallographic criteria are typical values -- consult your part-specific specification for acceptance criteria.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Inspection Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Gas Carburizing cluster. It ties the entire 9-poster series together by connecting inspection findings back to upstream causes. The common defects table is the capstone -- when a part fails, the operator can trace the defect to a root cause and flip to the relevant poster for the corrective action. The metallographic criteria cards are written for a QA engineer who knows what they're looking at under a microscope but wants a quick reference for acceptance limits. The sub-zero treatment section addresses the most common post-quench intervention in carburizing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #567 -- Construction Workup v1.0*
*2026-04-26*
