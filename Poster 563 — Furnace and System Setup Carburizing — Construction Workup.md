---
Project: Plating Posters Inc
Poster Number: 563
Title: "Furnace & System Setup -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.5)"
Technical Source: Gas carburizing furnace types (batch integral quench, continuous pusher/roller hearth, rotary retort, pit), temperature uniformity per AMS 2750, endothermic generator systems, nitrogen-methanol alternative. Per ASM Handbook Vol. 4 and AMS 2750H.
Process Scope: Gas carburizing furnace and system setup (Stage 3 of 9 -- Furnace/System Setup)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - FurnaceSetup
  - EndothermicGenerator
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #563 -- Construction Workup
## Furnace & System Setup -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the hardware side of gas carburizing -- furnace types, temperature uniformity requirements per AMS 2750, and the atmosphere generation systems (endothermic generator and nitrogen-methanol alternative). The endothermic generator is the beating heart of every atmosphere carburizing line; understanding the air-to-gas ratio, target composition, and generator retort temperature is what separates an operator from a button-pusher.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Furnace type comparison (Block B -- HERO):** Four furnace type cards in a 2x2 grid -- batch integral quench, continuous pusher/roller hearth, rotary retort, pit furnace. Each card with application notes and capacity.
2. **AMS 2750 uniformity panel (Block D):** Temperature uniformity class table and instrumentation types.
3. **Endothermic generator detail (Block E):** Two-column deep dive -- generator chemistry and the N2-methanol alternative.
4. **System checklist strip (Block F):** Pre-cycle furnace readiness checklist.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- FURNACE TYPES HERO (4.2"--14.5" / ~10.3")
  Block B: Four furnace type cards (2x2)
ZONE 4 -- AMS 2750 UNIFORMITY (14.5"--22.0" / ~7.5")
  Block D: Temperature class table + instrumentation types
ZONE 5 -- ATMOSPHERE GENERATION (22.0"--28.5" / ~6.5")
  Block E: Endothermic generator vs. N2-methanol
ZONE 6 -- SYSTEM READINESS CHECKLIST (28.5"--32.5" / ~4.0")
  Block F: Pre-cycle checklist strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FURNACE & SYSTEM SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stage 3 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The furnace is the vessel. The atmosphere is the chemistry. Get the system right and the metallurgy follows. Get it wrong and nothing downstream can save the load.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts loaded in fixtures  -->  After: Furnace sealed, purged, atmosphere established, ready to heat`

---

### ZONE 3 -- Furnace Types (HERO)

**Section label:** `FURNACE TYPES -- MATCHING THE MACHINE TO THE MISSION` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Four Furnace Type Cards (Y: 5.0" to 14.0")**

Four cards in a 2x2 grid:

| Card | X | Y | W | H | Furnace Type | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 11.0" | 4.2" | Batch Integral Quench | `#27AE60` |
| 2 | 12.0" | 5.0" | 11.5" | 4.2" | Continuous Pusher/Roller Hearth | `#2EC4B6` |
| 3 | 0.5" | 9.5" | 11.0" | 4.2" | Rotary Retort | `#E8A020` |
| 4 | 12.0" | 9.5" | 11.5" | 4.2" | Pit Furnace | `#E8A020` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Batch Integral Quench:*
- Title: `BATCH INTEGRAL QUENCH` Barlow SemiBold 18 pt `#27AE60`
- Stat: `MOST COMMON -- JOB SHOP STANDARD` JetBrains Mono 14 pt `#27AE60`
- Details (Inter Regular 13 pt `#F0EDE8`):
```
- Sealed quench furnace with internal oil quench
- Load enters from front; quench elevator drops
  load directly into oil within the sealed vestibule
- One load at a time -- full process control
- Capacity: 500--2,000 lb per load (typical)
- Best for: job shops, mixed part sizes,
  aerospace, low-to-medium volume
```

*Card 2 -- Continuous Pusher/Roller Hearth:*
- Title: `CONTINUOUS PUSHER / ROLLER HEARTH` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `HIGH-VOLUME AUTOMOTIVE` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
- Parts on trays pushed through sequential zones:
  preheat -> carburize -> diffuse -> quench
- Continuous throughput -- 24/7 operation
- Atmosphere curtains separate zones
- Multiple trays in process simultaneously
- Best for: automotive gears, bearings,
  high-volume production runs
```

*Card 3 -- Rotary Retort:*
- Title: `ROTARY RETORT` Barlow SemiBold 18 pt `#E8A020`
- Stat: `SMALL PARTS SPECIALIST` JetBrains Mono 14 pt `#E8A020`
- Details:
```
- Rotating drum inside heated retort
- Parts tumble during processing -- ensures
  uniform gas contact on all surfaces
- Ideal for small loose parts (pins, rollers,
  bushings, fasteners)
- Batch process with good uniformity
- Best for: small parts that can tumble
  without damage
```

*Card 4 -- Pit Furnace:*
- Title: `PIT FURNACE` Barlow SemiBold 18 pt `#E8A020`
- Stat: `LONG PARTS & LARGE GEARS` JetBrains Mono 14 pt `#E8A020`
- Details:
```
- Vertical loading -- parts hang or stand
  on fixtures
- Excellent for long shafts, tall gears,
  and heavy assemblies
- Gravity assists uniform atmosphere
  distribution
- Fan-circulated atmosphere
- Best for: long shafts, large ring gears,
  components that cannot lay flat
```

---

### ZONE 4 -- AMS 2750 Temperature Uniformity

**Section label:** `AMS 2750 -- TEMPERATURE UNIFORMITY AND INSTRUMENTATION` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- Furnace Class Table (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `FURNACE CLASSES` Barlow SemiBold 18 pt `#E8A020`
Subtitle: `Temperature Uniformity Tolerance per AMS 2750H` JetBrains Mono 12 pt `#F0EDE8` at 60%

| Class | Tolerance | Typical Use |
|---|---|---|
| 1 | +/-3 C (+/-5 F) | Precision aerospace (rare for carburizing) |
| 2 | +/-6 C (+/-10 F) | Aerospace gears per AMS 2759/7 |
| 3 | +/-8 C (+/-15 F) | Standard carburizing (most common) |
| 4 | +/-10 C (+/-20 F) | Commercial carburizing |
| 5 | +/-14 C (+/-25 F) | Non-critical applications |

Data: JetBrains Mono 11 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt.

Bottom note: `Most carburizing furnaces operate at Class 3 or Class 4. Aerospace gears (9310, AMS 2759/7) typically require Class 2.` Inter Medium 12 pt `#E8A020`.

*Right -- Instrumentation Types (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `INSTRUMENTATION TYPES` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
TYPE A: Recording + separate control +
  over-temperature instrument (most stringent)

TYPE B: Recording combined with control +
  over-temperature instrument

TYPE C: Recording + separate control
  (no over-temp required)

TYPE D: Recording combined with control
  (no over-temp required)

TYPE E: Load thermocouple with recording
  instrument

THERMOCOUPLE TYPES:
- Noble metal (B, R, S): above 1800 F
- Base metal (J, K, N): standard carburizing
- Expendable: one-time load verification

SYSTEM ACCURACY TEST (SAT):
Weekly or monthly -- compares process TC
against independent reference TC

TEMPERATURE UNIFORMITY SURVEY (TUS):
Quarterly -- verifies work zone uniformity
Minimum 9 thermocouples for large zones
```

---

### ZONE 5 -- Atmosphere Generation

**Section label:** `ATMOSPHERE GENERATION -- THE CHEMISTRY BEHIND THE GAS` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- Endothermic Generator (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `ENDOTHERMIC GENERATOR` Barlow SemiBold 18 pt `#E8A020`
Subtitle: `The Workhorse Atmosphere Source` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content (Inter Regular 13 pt `#F0EDE8`):
```
REACTION:
Natural gas (CH4) + air --> catalytic reaction
in heated retort at 1900--2050 F

AIR-TO-GAS RATIOS:
- Methane (CH4):    2.77 : 1
- Propane (C3H8):   7.16 : 1

OUTPUT COMPOSITION (methane feed):
- CO:  ~20%
- H2:  ~40%
- N2:  ~40% (balance)
- CH4: <0.5% (generator efficiency check)

ENRICHMENT:
- Natural gas or propane added to furnace
  to raise carbon potential above base endo
- Flow controlled by O2 probe feedback
- Over-enrichment = soot = non-uniform case

GENERATOR HEALTH CHECK:
- Residual CH4 < 0.5% = good cracking
- CH4 > 1.0% = retort catalyst degraded
- Dew point at generator outlet: -40 to 0 F
```

*Right -- Nitrogen-Methanol Alternative (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `N2-METHANOL SYSTEM` Barlow SemiBold 18 pt `#2EC4B6`
Subtitle: `The Generator-Free Alternative` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content (Inter Regular 13 pt `#F0EDE8`):
```
PRINCIPLE:
N2 + methanol (CH3OH) injected directly
into the hot furnace; methanol cracks
in situ to produce CO + H2

RATIO:
~40% N2 + ~60% methanol by volume

ADVANTAGES:
- No endothermic generator to maintain
- Faster atmosphere changeover
- Consistent composition
- Lower capital cost for small operations

DISADVANTAGES:
- Methanol storage and handling (flammable,
  toxic -- OSHA PEL 200 ppm)
- Higher operating cost per cubic foot
  of atmosphere vs. endo generator
- Less precise carbon potential control
  in some configurations

BEST FOR:
Small batch furnaces, backup systems,
facilities without room for a generator
```

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `The endothermic generator is to carburizing what the rectifier is to electroplating -- the invisible engine that makes everything possible.` Inter Medium 14 pt `#E8A020`, center.

---

### ZONE 6 -- System Readiness Checklist

**Section label:** `PRE-CYCLE SYSTEM READINESS CHECKLIST` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Checklist strip (Y: 29.4" to 32.3")**

Rounded rect full width, fill `#1E2435`. Eight checklist items in two columns:

Left column:
```
[ ] Furnace sealed -- door gaskets inspected
[ ] Endothermic generator at operating temp (1900+ F)
[ ] Burn-off pilots lit at all furnace openings
[ ] N2 purge complete -- O2 below 1% verified
```

Right column:
```
[ ] Endo gas introduced -- composition verified
[ ] O2 probe calibrated and reading correctly
[ ] Quench oil at operating temperature (120--180 F)
[ ] Load thermocouples placed and recording
```

Checkbox: Rounded rect 0.25" x 0.25", border 1 pt `#E8A020`, no fill.
Text: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Furnace & System Setup -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2750H, AMS 2759/7, ASM Handbook Vol. 4, general industry practice. Consult your furnace OEM manual and process engineer for equipment-specific parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Furnace System Setup Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The endothermic generator section is the technical heart of this poster. Most heat treat operators interact with the generator daily but few understand the underlying chemistry (air-to-gas ratio, cracking efficiency, residual methane as a health indicator). The AMS 2750 section is pure reference -- operators will look this up when setting up TUS surveys or preparing for Nadcap audits. The N2-methanol panel is a genuine alternative that smaller shops use, and comparing the two side by side gives operators a real understanding of their options.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #563 -- Construction Workup v1.0*
*2026-04-26*
