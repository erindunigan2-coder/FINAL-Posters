---
Project: Plating Posters Inc
Poster Number: 572
Title: "Furnace & System Setup -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.5)"
Technical Source: Vacuum carburizing furnace types (single-chamber, multi-chamber, continuous), vacuum system design (roughing pump + roots blower), temperature capability (1700-1900 F), base pressure and leak rate. Per ASM Handbook Vol. 4 and AMS 2750.
Process Scope: Vacuum carburizing furnace and system setup (Stage 3 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - FurnaceSetup
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #572 -- Construction Workup
## Furnace & System Setup -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The furnace poster for the LPC cluster. Vacuum carburizing furnaces are a different breed from atmosphere furnaces -- sealed pressure vessels with vacuum pumps, gas quench blowers, and modular transfer systems. This poster covers the three major furnace configurations (single-chamber, multi-chamber, continuous), the vacuum system itself, and the temperature capability advantage that makes LPC faster than gas carburizing.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three furnace type cards (Block B -- HERO):** Single-chamber, multi-chamber, and continuous -- each with a description, pros/cons, and typical application.
2. **Vacuum system schematic panel (Block D):** Roughing pump + roots blower + diffusion pump chain with performance specs.
3. **Temperature capability comparison (Block E):** LPC vs. gas -- the higher temperature advantage quantified.
4. **Specification strip (Block F):** AMS 2750 requirements for vacuum furnaces.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal)
ZONE 3 -- FURNACE TYPES HERO (4.2"--14.5" / ~10.3")
  Block B: Three furnace type cards
ZONE 4 -- VACUUM SYSTEM (14.5"--22.0" / ~7.5")
  Block D: Pump chain and performance specs
ZONE 5 -- TEMPERATURE CAPABILITY (22.0"--28.5" / ~6.5")
  Block E: LPC vs. gas temperature comparison
ZONE 6 -- SPEC STRIP (28.5"--32.5" / ~4.0")
  Block F: AMS 2750 requirements
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FURNACE & SYSTEM SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 3 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Sealed pressure vessels with vacuum pumps, gas quench blowers, and computer-controlled recipe execution. These are not your grandfather's atmosphere furnaces.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts fixtured in CFC trays  -->  After: Furnace sealed, vacuum verified, ready for heating`

---

### ZONE 3 -- Furnace Types (HERO)

**Section label:** `FURNACE CONFIGURATIONS -- THREE APPROACHES TO VACUUM CARBURIZING` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Three Furnace Type Cards (Y: 5.0" to 14.0")**

| Card | X | Y | W | H | Type | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 23.0" | 2.8" | Single-Chamber Vacuum Furnace | `#2EC4B6` |
| 2 | 0.5" | 8.1" | 23.0" | 2.8" | Multi-Chamber (Modular) | `#27AE60` |
| 3 | 0.5" | 11.2" | 23.0" | 2.8" | Continuous Multi-Chamber | `#E8A020` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Single-Chamber:*
- Title: `SINGLE-CHAMBER VACUUM FURNACE` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `MOST VERSATILE -- LOAD, HEAT, CARBURIZE, QUENCH IN ONE VESSEL` JetBrains Mono 13 pt `#2EC4B6`
- Details (Inter Regular 13 pt `#F0EDE8`, two columns):

Left:
```
HOW IT WORKS:
- One sealed chamber handles all steps
- Evacuate, heat, boost/diffuse, HPGQ
- Integrated gas quench blower and
  nozzle system inside chamber
- Computer controls entire recipe
```

Right:
```
PROS / CONS:
+ Maximum flexibility (any recipe)
+ Lower capital than multi-chamber
+ Good for job shop / low-medium volume
- Entire cycle in one chamber = lower
  throughput (furnace idle during heat-up)
- Load size limited by single chamber
```

*Card 2 -- Multi-Chamber:*
- Title: `MULTI-CHAMBER (MODULAR)` Barlow SemiBold 18 pt `#27AE60`
- Stat: `ECM ICBP / SECO WARWICK CASEMASTER EVOLUTION` JetBrains Mono 13 pt `#27AE60`
- Details:

Left:
```
HOW IT WORKS:
- Separate preheat, carburize, and
  quench chambers
- Internal transfer mechanism moves
  parts between chambers under vacuum
- One carburizing chamber feeds
  multiple quench chambers
```

Right:
```
PROS / CONS:
+ Higher throughput (parallel processing)
+ Dedicated chambers optimized per step
+ Continuous production flow
- Higher capital cost
- More complex maintenance
- Requires reliable transfer mechanism
```

*Card 3 -- Continuous:*
- Title: `CONTINUOUS MULTI-CHAMBER` Barlow SemiBold 18 pt `#E8A020`
- Stat: `AUTOMOTIVE HIGH-VOLUME PRODUCTION` JetBrains Mono 13 pt `#E8A020`
- Details:

Left:
```
HOW IT WORKS:
- Parts move on pallets through
  sequential chambers
- Preheat -> Carburize -> Diffuse ->
  Quench in continuous flow
- Highest throughput of any LPC design
```

Right:
```
PROS / CONS:
+ Maximum throughput for mass production
+ Consistent, repeatable results
+ Minimum operator intervention
- Highest capital investment
- Less flexible (optimized for one recipe)
- Requires steady production volume
  to justify investment
```

---

### ZONE 4 -- Vacuum System

**Section label:** `THE VACUUM SYSTEM -- PUMPS, PRESSURE, AND LEAK INTEGRITY` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- Pump Chain (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `VACUUM PUMP CHAIN` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`):
```
ROUGHING PUMP (mechanical rotary vane)
  Reduces pressure from atmosphere
  to ~1 mbar in minutes
        |
ROOTS BLOWER (booster)
  Increases pumping speed in the
  0.1--10 mbar range
  Provides the volume needed for
  acetylene pulse evacuation
        |
DIFFUSION PUMP or TURBO PUMP (optional)
  For harder vacuum (<0.01 mbar)
  Used in some high-specification systems

BASE PRESSURE REQUIREMENT:
< 0.1 mbar (< 0.075 torr) before heating
```

*Right -- Performance Specs (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `KEY PERFORMANCE SPECIFICATIONS` Barlow SemiBold 18 pt `#E8A020`

Content:
```
LEAK RATE:
< 5 microns/hour for most specifications
Verified by pump-down and hold test
Lower leak rate = cleaner parts, better
carbon control

PUMP-DOWN TIME:
Atmosphere to <0.1 mbar: 15--45 minutes
(depends on chamber volume and pump capacity)

O-RING / SEAL MAINTENANCE:
- Door seals, feedthrough seals, viewport seals
- Inspect before every run
- Replace on schedule (thermal cycling
  degrades elastomers)
- A single bad seal = contaminated run

VACUUM GAUGE TYPES:
- Pirani gauge (rough vacuum)
- Capacitance manometer (process pressure)
- Ionization gauge (high vacuum, if equipped)
```

---

### ZONE 5 -- Temperature Capability

**Section label:** `TEMPERATURE ADVANTAGE -- WHY LPC RUNS HOTTER` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Comparison table + callout (Y: 22.9" to 28.3")**

*Temperature comparison table (Y: 23.0" to 25.5"):*

| Parameter | Gas Carburizing | Vacuum Carburizing (LPC) |
|---|---|---|
| Standard range | 1650--1750 F (899--954 C) | 1700--1850 F (927--1010 C) |
| Maximum practical | 1750 F (954 C) | 1900 F (1038 C) |
| Upper limit | Grain growth + severe IGO | Grain growth (but no IGO) |
| Cycle time for 0.040" ECD | 4--5 hours at 1700 F | 1.5--2.5 hours at 1800 F |
| Time savings | -- | 30--50% shorter cycle |

Table: Header `#3A4055`, alternating rows `#252B3D` / `#1E2435`. JetBrains Mono 12 pt.

*Why higher temps work in vacuum (Y: 26.0" to 28.3"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Content (Inter Regular 13 pt `#F0EDE8`):
```
WHY CAN VACUUM GO HIGHER?
- No oxygen in vacuum = no intergranular oxidation (IGO)
- IGO is the temperature-limiting factor in gas carburizing
- Without IGO risk, temperature can be pushed to 1850--1900 F
- Every 100 F increase roughly doubles the diffusion coefficient
- Result: same case depth in 30--50% less time
- Trade-off: grain growth at highest temperatures
  (use vacuum-grade fine-grain steels above 1850 F)
```

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- `Higher temperature = faster diffusion = shorter cycles = more parts per day. That is the business case for LPC in three equations.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 6 -- Specification Strip

**Section label:** `AMS 2750 REQUIREMENTS FOR VACUUM FURNACES` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four spec cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `FURNACE CLASS` | Class 2 (+/-10 F) for aerospace per AMS 2759/7. Class 3 (+/-15 F) for general production. Verify TUS quarterly. |
| 2 | 6.33" | 5.5" | `INSTRUMENTATION` | Type A or B per AMS 2750. Recording + control + over-temperature instruments. All calibrated per schedule. |
| 3 | 12.16" | 5.5" | `THERMOCOUPLES` | Types K or N (base metal). Sheathed to protect vacuum integrity. Optical pyrometry as supplement. |
| 4 | 18.0" | 5.5" | `TUS FREQUENCY` | Temperature Uniformity Survey quarterly. SAT weekly or monthly per furnace class. 9+ TCs for large work zones. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Title: Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Furnace & System Setup -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2750H, AMS 2759/7E. Furnace specifications vary by manufacturer and model. Consult your vacuum furnace OEM for pump capacity, chamber dimensions, and HPGQ performance data.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Furnace System Setup Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three furnace type cards are full-width to give each configuration enough room for a fair comparison. The vacuum system panel is the technical heart -- operators transitioning from atmosphere furnaces need to understand leak rates and pump-down procedures, which are entirely new concepts for them. The temperature comparison table is the business case for LPC: same case depth, 30-50% less time.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #572 -- Construction Workup v1.0*
*2026-04-26*
