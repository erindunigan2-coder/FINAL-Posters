---
Project: Plating Posters Inc
Poster Number: 396
Title: "DI Water Systems -- Ion Exchange, RO & Water Quality for Plating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-8)"
Technical Source: Industry-standard deionized water systems for metal finishing -- mixed-bed ion exchange, reverse osmosis, RO+mixed-bed combinations, resistivity monitoring, and the impact of water impurities on plating quality. Per Metal Finishing Guidebook and general industry knowledge.
Process Scope: DI water systems -- why DI matters for plating, system types, quality monitoring, and the consequences of poor water quality
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DIWater
  - IonExchange
  - ReverseOsmosis
  - WaterQuality
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT08
---

# Poster #396 -- Construction Workup
## DI Water Systems -- Ion Exchange, RO & Water Quality for Plating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster is the deep dive into deionized water -- the unsung hero of plating quality. Many shops treat the DI system as "just a water filter" and neglect it until plating defects appear. This poster explains why every impurity in city water causes a specific plating defect, how the three major DI system types work, and what resistivity numbers to target. The hero concept: the city-to-DI transformation table showing what gets removed and why it matters.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **City vs. DI comparison (Block B -- HERO):** Side-by-side showing what city water contains and what DI removes, with the plating defect each impurity causes.

2. **Three DI system types (Block C):** Mixed-bed ion exchange, reverse osmosis, and RO+mixed-bed compared.

3. **Resistivity monitoring panel (Block D):** Target values, inline monitoring, and resin exhaustion indicators.

4. **Plating defect consequences (Block E):** What happens when water quality fails.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CITY vs. DI HERO + SYSTEM TYPES (2.9"--15.0" / ~12.1" tall)
  Block B: City vs. DI transformation table (HERO)
  Block C: Three DI system types compared

ZONE 3 -- RESISTIVITY MONITORING (15.0"--22.0" / ~7.0" tall)
  Block D: Target values, monitoring, and resin life

ZONE 4 -- DEFECT CONSEQUENCES (22.0"--28.5" / ~6.5" tall)
  Block E: Water impurity -> plating defect map

ZONE 5 -- KEY RULES (28.5"--32.5" / ~4.0" tall)
  Block F: Quick-reference DI water rules

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DI WATER SYSTEMS` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ion Exchange, Reverse Osmosis & Why Water Quality Drives Plating Quality` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `City water contains hardness, chlorides, and silica that cause pitting, haze, and adhesion failure. DI water removes them all -- but only if the system is maintained.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- City vs. DI Hero + System Types

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHAT DI WATER REMOVES -- AND WHY IT MATTERS

---

**BLOCK B -- City vs. DI Transformation Table**

Y: 3.8" to 8.5". Full width.

Column widths (23.0" total):
- Parameter (4.0") | City Water (4.5") | DI Water (4.5") | Plating Impact (10.0")

Header row: fill `#3A4055`, H: 0.5".

| Parameter | City Water | DI Water | Plating Impact |
|---|---|---|---|
| Conductivity | 200-1000 uS/cm | 0.055-1.0 uS/cm | High conductivity = high dissolved solids = bath contamination |
| Hardness (Ca/Mg) | 50-500 ppm CaCO3 | < 1 ppm | Insoluble soaps in alkaline baths; interferes with brightener systems |
| Chloride | 10-250 ppm | < 0.1 ppm | PITTING in nickel, chrome, and most plating baths |
| Silica | 5-50 ppm | < 0.01 ppm | Haze on decorative surfaces; adhesion failure; interferes with activation |
| Iron | 0.1-5 ppm | < 0.01 ppm | Roughness; co-deposition of iron in plating baths |
| Copper (from piping) | 0.01-1 ppm | < 0.001 ppm | Immersion copper deposit on active surfaces; adhesion failure |

Data: Inter Regular 12 pt. Parameter names: Barlow SemiBold 13 pt. City water values: `#E05C5C`. DI water values: `#27AE60`. Impact text: `#F0EDE8`.

**Key insight (Y: 8.0"):**
- Rounded rect, full width, H: 0.4", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Rule of thumb: any rinse that feeds directly into a plating tank should use DI water.` Inter Medium 14 pt `#27AE60`

---

**BLOCK C -- Three DI System Types**

Y: 8.8" to 14.8". Three callout boxes side by side.

Each box: Rounded rect, W: 7.33", H: 5.7", fill `#1E2435`, radius 6, top accent 4 pt.

| Box | X | System | Accent |
|---|---|---|---|
| 1 | 0.5" | MIXED-BED ION EXCHANGE | `#2EC4B6` |
| 2 | 8.16" | REVERSE OSMOSIS (RO) | `#E8A020` |
| 3 | 15.83" | RO + MIXED-BED | `#27AE60` |

**Box 1 -- Mixed-Bed Ion Exchange:**
- Title: Barlow SemiBold 18 pt `#2EC4B6`
- Body: Inter Regular 13 pt `#F0EDE8`:
```
How it works:
  Cation resin (H+) removes Ca, Mg, Na, Fe
  Anion resin (OH-) removes Cl, SO4, CO3, SiO2
  H+ and OH- combine to form pure H2O

Output: 1-18 megohm-cm (standard)
Regeneration: acid (H2SO4) + caustic (NaOH)
Best for: Standard plating shop DI
Limitation: High TDS feed shortens resin life
```

**Box 2 -- Reverse Osmosis:**
- Title: Barlow SemiBold 18 pt `#E8A020`
- Body:
```
How it works:
  Semipermeable membrane rejects 90-99%
  of dissolved solids under pressure

Output: 90-99% TDS reduction
Regeneration: None (membrane replacement)
Best for: Pre-treatment before ion exchange;
  high-TDS feed water areas
Limitation: Does not produce 18 megohm water
  alone -- still has 1-10% pass-through
```

**Box 3 -- RO + Mixed-Bed:**
- Title: Barlow SemiBold 18 pt `#27AE60`
- Body:
```
How it works:
  RO removes bulk dissolved solids
  Mixed-bed polishes to ultra-pure

Output: 18 megohm-cm achievable
Regeneration: RO membrane + resin regen
Best for: High-quality plating (electronics,
  aerospace, decorative chrome)
Advantage: RO extends resin life dramatically
  (less work for the ion exchange bed)
```

---

### ZONE 3 -- Resistivity Monitoring

**Section label:** Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> MONITORING DI QUALITY -- RESISTIVITY IS YOUR SIGNAL

---

**BLOCK D -- Monitoring Panel**

Y: 15.9" to 21.8". Two-column layout.

**Left -- Resistivity Targets (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.5", fill `#1E2435`, radius 6, left accent `#27AE60`.

Title: `RESISTIVITY TARGETS` Barlow SemiBold 18 pt `#27AE60`

| Quality Level | Resistivity | Conductivity | Application |
|---|---|---|---|
| Minimum acceptable | 0.2 megohm-cm | 5 uS/cm | General rinsing |
| Standard plating | 1-5 megohm-cm | 0.2-1 uS/cm | Most plating shops |
| High-quality | 10-18 megohm-cm | 0.055-0.1 uS/cm | Electronics, aerospace |
| Theoretical max | 18.2 megohm-cm | 0.055 uS/cm | Ultra-pure (rarely needed in plating) |

Data: JetBrains Mono 12 pt for numbers. Inter Regular 12 pt for text.

**Right -- Resin Life and Maintenance (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.5", fill `#1E2435`, radius 6, left accent `#E8A020`.

Title: `MAINTENANCE AND RESIN LIFE` Barlow SemiBold 18 pt `#E8A020`

Body: Inter Regular 13 pt `#F0EDE8`:
```
Inline resistivity meter at DI output:
  - Alarm when resistivity drops below setpoint
  - Indicates resin exhaustion or membrane failure

Resin regeneration frequency:
  - Depends on feed water TDS and usage rate
  - Typical: every 1-4 weeks (service exchange)
  - Monitor resistivity trend -- gradual decline =
    resin approaching exhaustion

RO membrane life:
  - 2-5 years typical
  - Pre-filter (sediment + carbon) extends life
  - Monitor permeate TDS -- rising = membrane aging
```

Caution callout at bottom:
- Inter Medium 13 pt `#E05C5C`: `Exhausted resin actually RELEASES previously captured ions back into the water -- running past resin exhaustion is WORSE than using city water.`

---

### ZONE 4 -- Defect Consequences

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHEN WATER QUALITY FAILS -- PLATING DEFECTS

---

**BLOCK E -- Defect Map**

Y: 22.9" to 28.3". Column widths (23.0" total):
- Impurity (4.5") | Source (4.5") | Plating Defect (6.0") | Prevention (8.0")

Header row: fill `#3A4055`, H: 0.5".

| Impurity | Source | Plating Defect | Prevention |
|---|---|---|---|
| Calcium / Magnesium | City water hardness | Insoluble soaps; interferes with wetting; dull deposits | DI water for final rinse; water softener as minimum |
| Chloride | City water; HCl carry-over | Pitting in nickel, chrome, and most plating baths | DI water removes to < 0.1 ppm; verify rinse conductivity |
| Silica | City water; silicate cleaners | Haze on decorative surfaces; poor adhesion | DI with anion resin (removes silica); avoid silicate carryover |
| Iron | City water piping; process carryover | Roughness; dark deposits; co-deposition | DI water; use PVC or CPVC piping for DI distribution |
| Organic contamination | Water source; biofilm in DI system | Pitting; reduced throwing power; brightener interference | Activated carbon pre-filter; periodic DI system sanitization |

Data: Inter Regular 12 pt. Impurity names: Barlow SemiBold 13 pt `#E05C5C`. Prevention: Inter Medium 12 pt `#27AE60`.

---

### ZONE 5 -- Key Rules

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> DI WATER RULES -- QUICK REFERENCE

---

**BLOCK F -- Four Rule Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Rule | Accent |
|---|---|---|---|
| 1 | 0.5" | Any rinse feeding directly into a plating tank = DI water | `#27AE60` |
| 2 | 6.33" | Monitor resistivity at the DI output CONTINUOUSLY -- alarm on drop | `#E8A020` |
| 3 | 12.16" | Exhausted resin releases captured ions BACK into the water -- worse than city | `#E05C5C` |
| 4 | 18.0" | RO before ion exchange extends resin life 3-5x and saves regeneration chemicals | `#2EC4B6` |

---

### ZONE 6 -- Footer

Standard. Title: `DI Water Systems -- Ion Exchange, RO & Water Quality for Plating`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. DI water system specifications and resistivity targets shown are typical values for metal finishing. Specific requirements vary by plating process, customer specification, and feed water quality. Consult your water treatment supplier for system sizing and maintenance schedules.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `DI Water Systems -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster gives DI water the attention it deserves -- most plating shops treat their DI system as an afterthought until chloride pitting or hardness haze shows up. The city-vs-DI table is the visual hook: seeing "Chloride: 10-250 ppm -> < 0.1 ppm" next to "PITTING" makes the case instantly. The three system types demystify equipment that many operators have never been taught about. The exhausted-resin warning is a practical gem -- operators who do not know about ion dump-back will run a dead DI bed for weeks, making their water quality worse than city tap.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #396 -- Construction Workup v1.0*
*2026-04-26*
