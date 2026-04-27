---
Project: Plating Posters Inc
Poster Number: 566
Title: "Quench -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.8)"
Technical Source: Gas carburizing quench stage -- quench media comparison (oil, polymer, gas, water), H-factor table, oil quench parameters, distortion control strategies (press quench, plug quench, marquench). Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Gas carburizing quench (Stage 6 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - Quench
  - Distortion
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #566 -- Construction Workup
## Quench -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The quench is the most violent moment in the carburizing process. A 1500 F part hits oil at 150 F -- the temperature differential drives the martensitic transformation that creates hardness, but it also creates distortion, residual stress, and (if you get it wrong) cracking. This poster covers quench media options with H-factors, oil quench parameters, and the distortion control strategies that separate precision heat treating from throwing parts in oil and hoping.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Quench media comparison (Block B -- HERO):** Six-row reference table with H-factors -- the definitive quench severity reference for carburizing operations.
2. **Oil quench parameters panel (Block D):** Temperature, agitation, maintenance, and the critical water-in-oil hazard.
3. **Distortion control strategies (Block E):** Press quench, plug quench, marquench, and orientation strategies.
4. **Quick-reference strip (Block F):** Four critical quench rules.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Coral)
ZONE 3 -- QUENCH MEDIA COMPARISON HERO (4.2"--14.5" / ~10.3")
  Block B: H-factor table + media descriptions
ZONE 4 -- OIL QUENCH PARAMETERS (14.5"--22.0" / ~7.5")
  Block D: Oil temp, agitation, maintenance, water hazard
ZONE 5 -- DISTORTION CONTROL (22.0"--28.5" / ~6.5")
  Block E: Press quench, plug quench, marquench, orientation
ZONE 6 -- CRITICAL QUENCH RULES (28.5"--32.5" / ~4.0")
  Block F: Four-rule strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stage 6 of 9` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `1500 F steel meets 150 F oil. The temperature shock that creates martensite also creates distortion. Master the quench or the quench masters you.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E05C5C`, text `#F0EDE8`. Others dimmed.
Below: `Before: Parts at carburizing temperature, carbon profile complete  -->  After: Austenite transformed to martensite, 58--63 HRC surface`

---

### ZONE 3 -- Quench Media Comparison (HERO)

**Section label:** `QUENCH MEDIA -- SEVERITY, SPEED, AND SELECTION` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Left: H-Factor Table (X: 0.5", W: 14.0")**

Y: 5.0" to 13.0". Rounded rect fill `#1E2435`, left accent `#E05C5C`.

Title: `GROSSMANN H-FACTOR REFERENCE` Barlow SemiBold 20 pt `#E05C5C`
Subtitle: `H = quench severity coefficient -- higher H = faster cooling = harder part (but more distortion)` JetBrains Mono 11 pt `#F0EDE8` at 60%

| Medium | H-Factor | Cooling Rate | Typical Use |
|---|---|---|---|
| Still oil | 0.25--0.30 | Slow | Low distortion, good hardenability steels |
| Agitated oil (moderate) | 0.35--0.50 | Standard | General production carburizing |
| Agitated oil (vigorous) | 0.50--0.80 | Fast | Higher hardenability demand |
| Marquench (hot oil) 250--400 F | 0.20--0.35 | Controlled | Reduced distortion; held above Ms |
| Polymer (10--20% PAG) | 0.30--0.80 | Adjustable | Cleaner than oil; variable severity |
| Agitated water | 1.0--1.5 | Severe | Rarely for carburized parts -- cracking risk |
| HPGQ N2 (10 bar) | 0.10--0.20 | Slow-moderate | Vacuum furnace quenching |
| HPGQ He (20 bar) | 0.20--0.35 | Moderate-fast | Aerospace vacuum carburizing |

Data: JetBrains Mono 11 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt. Alternating rows: `#1E2435` / `#252B3D`.

**BLOCK B -- Right: Media Selection Guide (X: 15.0", W: 8.5")**

Y: 5.0" to 13.0". Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `CHOOSING YOUR QUENCH` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
THE TRADEOFF:
Harder quench = more martensite = higher
hardness BUT more distortion and cracking
risk.

SELECTION LOGIC:
1. What H-factor does the steel NEED?
   (hardenability via Jominy data)
2. What distortion can the part TOLERATE?
3. What does the SPECIFICATION require?

MOST CARBURIZED GEARS:
Agitated oil, H = 0.35--0.70
(the sweet spot for 8620, 4320, 9310)

PRECISION GEARS:
Press quench or marquench for
distortion-critical geometries

PLAIN CARBON STEELS:
Need higher H-factor (water or vigorous
oil) -- low hardenability demands
severe quench

ALLOY STEELS (9310, 4820):
Can use milder quench due to high
hardenability -- less distortion risk
```

---

### ZONE 4 -- Oil Quench Parameters

**Section label:** `OIL QUENCH -- PARAMETERS AND HAZARDS` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Three-column layout (Y: 15.3" to 21.8")**

*Left -- Operating Parameters (X: 0.5", W: 7.33"):*
- Accent: `#E8A020`
- Title: `OPERATING PARAMETERS`

Content (Inter Regular 13 pt `#F0EDE8`):
```
OIL TEMPERATURE:
Standard: 100--160 F (38--71 C)
Hot (marquench): 250--400 F (121--204 C)

AGITATION:
Propeller or pump driven
50--200 ft/min flow velocity across load
UNIFORM agitation is critical -- dead
zones = non-uniform hardness

TRANSFER TIME:
Parts must reach oil within seconds
of leaving the furnace hot zone.
Slow transfer = pearlite/bainite = soft

QUENCH DURATION:
Until core reaches below 300 F
(varies by section size: seconds
for thin parts, minutes for thick)
```

*Center -- Oil Maintenance (X: 8.17", W: 7.33"):*
- Accent: `#27AE60`
- Title: `OIL MAINTENANCE`

Content:
```
MONITOR REGULARLY:
- Viscosity (thickens with oxidation)
- Flash point (drops as oil degrades)
- Water content (MUST be <0.05%)
- Cooling curve (ASTM D6200)
- Oxidation number

REPLACEMENT CRITERIA:
- Flash point drops below minimum
- Viscosity increases >20% from new
- Cooling curve degrades significantly
- Quench results become inconsistent

OIL LIFE:
Properly maintained quench oil can
last years. Neglected oil becomes
a fire hazard and produces
inconsistent hardness.
```

*Right -- Water-in-Oil Hazard (X: 15.83", W: 7.67"):*
- Accent: `#E05C5C`
- Title: `WATER-IN-OIL HAZARD`

Content:
```
THE MOST DANGEROUS CONDITION
IN A QUENCH TANK:

Water content as low as 0.1% in
quench oil can cause VIOLENT BOIL-OVER
when hot parts are submerged.

MECHANISM:
1500 F parts flash water to steam
Steam expands 1,700x in volume
Oil erupts from tank = FIRE + BURNS

SOURCES OF WATER:
- Roof leaks into quench tank
- Condensation from humid air
- Parts not dried after wash
- Cooler heat exchanger leak

PREVENTION:
- Test oil for water content weekly
- Cover tank when not in use
- Fix roof leaks IMMEDIATELY
- Verify parts are dry before quench
```

---

### ZONE 5 -- Distortion Control

**Section label:** `DISTORTION CONTROL STRATEGIES` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Four strategy cards (Y: 22.9" to 28.3")**

2x2 grid:

| Card | X | Y | W | H | Strategy | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 22.9" | 11.0" | 2.5" | Press Quench | `#27AE60` |
| 2 | 12.0" | 22.9" | 11.5" | 2.5" | Plug Quench | `#2EC4B6` |
| 3 | 0.5" | 25.7" | 11.0" | 2.5" | Marquench (Hot Oil) | `#E8A020` |
| 4 | 12.0" | 25.7" | 11.5" | 2.5" | Part Orientation | `#E8A020` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Press Quench:*
- Title: `PRESS QUENCH` Barlow SemiBold 16 pt `#27AE60`
- Content: `Part held in a die during oil quench. Die constrains distortion in critical dimensions. Used for flat gears, discs, and ring gears. Requires dedicated press and dies per part number. The gold standard for distortion-critical gears.`

*Card 2 -- Plug Quench:*
- Title: `PLUG QUENCH` Barlow SemiBold 16 pt `#2EC4B6`
- Content: `Expandable plug inserted into bore during quench. Controls bore roundness and taper. Used for splined parts, ring gears, and bearing races. Plug expands to constrain ID while oil quenches the OD.`

*Card 3 -- Marquench (Hot Oil):*
- Title: `MARQUENCH (HOT OIL)` Barlow SemiBold 16 pt `#E8A020`
- Content: `Oil held at 250--400 F -- above Ms temperature. Parts held briefly to equalize temperature between surface and core. Then air cooled through transformation. Reduces thermal gradient = reduced distortion. Requires sufficient hardenability.`

*Card 4 -- Part Orientation:*
- Title: `PART ORIENTATION IN QUENCH` Barlow SemiBold 16 pt `#E8A020`
- Content: `Thin sections enter oil first. Bore vertical for ring gears. Agitation direction matters -- uniform oil flow across all surfaces. Dense center of load cools slower. Controlled orientation is free distortion control.`

---

### ZONE 6 -- Critical Quench Rules

**Section label:** `FOUR RULES FOR EVERY QUENCH` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four rule cards (Y: 29.4" to 32.3")**

| Card | X | W | Rule |
|---|---|---|---|
| 1 | 0.5" | 5.5" | `SPEED MATTERS: Parts must reach oil within seconds. Every second of delay = pearlite/bainite at the surface = soft spots that no temper can fix.` |
| 2 | 6.33" | 5.5" | `UNIFORMITY: Non-uniform quench = non-uniform hardness = non-uniform distortion. Agitation must reach every surface of every part in the load.` |
| 3 | 12.16" | 5.5" | `OIL HEALTH: Degraded oil = inconsistent quench = inconsistent parts. Test cooling curves regularly. Oil is cheap; scrap is expensive.` |
| 4 | 18.0" | 5.5" | `FIRE AWARENESS: 1500 F parts + oil + potential water contamination = the recipe for a quench fire. Know where the suppression system is. Every shift.` |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#E05C5C`.
Title (first phrase before colon): Barlow SemiBold 14 pt `#E05C5C`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Quench -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7, general industry practice. H-factor values are typical ranges from Grossmann's original work and subsequent refinements. Actual quench severity depends on oil condition, agitation, and load geometry.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is a Coral-accented poster because the quench is dangerous (fire, burns, boil-over) and critical (wrong quench = wrong part). The H-factor table is the hero -- this is the reference that metallurgists and process engineers actually use when specifying quench severity. The water-in-oil hazard panel is intentionally dramatic because water contamination is genuinely one of the most dangerous conditions in a heat treat shop. The distortion control section elevates the poster from "how to quench" to "how to quench intelligently."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #566 -- Construction Workup v1.0*
*2026-04-26*
