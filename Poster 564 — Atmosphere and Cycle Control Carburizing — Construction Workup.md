---
Project: Plating Posters Inc
Poster Number: 564
Title: "Atmosphere & Cycle Control -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.6)"
Technical Source: Carbon potential control methods (O2 probe, dew point, IR CO2 analyzer, shim stock), atmosphere composition targets, enrichment gas management, soot prevention. Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Gas carburizing atmosphere and cycle control (Stage 4 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - AtmosphereControl
  - CarbonPotential
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #564 -- Construction Workup
## Atmosphere & Cycle Control -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the control poster -- the one the furnace operator stares at when the O2 probe reading drifts or the dew point moves. Carbon potential control is the single most important variable in gas carburizing: too low and you get insufficient case, too high and you get carbide networks and scrap. This poster covers all four Cp control methods, atmosphere composition targets, boost/diffuse strategy, and enrichment gas management.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Carbon potential control methods (Block B -- HERO):** Four method cards in a 2x2 grid -- O2 probe, dew point, IR CO2 analyzer, shim stock. Each with principle, accuracy, and when to use.
2. **Atmosphere composition table (Block D):** Target gas composition for methane-based endothermic atmosphere.
3. **Boost/Diffuse cycle panel (Block E):** Visual explanation of the two-phase carbon cycle with Cp targets.
4. **Enrichment and soot strip (Block F):** Enrichment gas management and soot prevention.

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
  Stage 4 highlighted (Amber)
ZONE 3 -- CARBON POTENTIAL CONTROL HERO (4.2"--14.5" / ~10.3")
  Block B: Four Cp control method cards (2x2)
ZONE 4 -- ATMOSPHERE COMPOSITION (14.5"--22.0" / ~7.5")
  Block D: Gas composition targets + Cp vs. dew point/CO2 reference
ZONE 5 -- BOOST/DIFFUSE CYCLE (22.0"--28.5" / ~6.5")
  Block E: Two-phase cycle explanation
ZONE 6 -- ENRICHMENT & SOOT (28.5"--32.5" / ~4.0")
  Block F: Enrichment gas management strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ATMOSPHERE & CYCLE CONTROL` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stage 4 of 9` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Carbon potential is the throttle. Control it precisely and you control the case. Lose control and you're making scrap at 1700 F.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Furnace at temperature, endo atmosphere established  -->  After: Carbon potential verified and controlled throughout the cycle`

---

### ZONE 3 -- Carbon Potential Control Methods (HERO)

**Section label:** `FOUR METHODS TO MEASURE CARBON POTENTIAL` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Four Method Cards (Y: 5.0" to 14.0")**

Four cards in a 2x2 grid:

| Card | X | Y | W | H | Method | Accent |
|---|---|---|---|---|---|---|
| 1 | 0.5" | 5.0" | 11.0" | 4.2" | Oxygen Probe (Zirconia Sensor) | `#27AE60` |
| 2 | 12.0" | 5.0" | 11.5" | 4.2" | Dew Point Analyzer | `#2EC4B6` |
| 3 | 0.5" | 9.5" | 11.0" | 4.2" | Infrared CO2 Analyzer | `#E8A020` |
| 4 | 12.0" | 9.5" | 11.5" | 4.2" | Shim Stock (Foil Test) | `#E8A020` |

Each: Rounded rect, fill `#1E2435`, left accent 0.06".

*Card 1 -- Oxygen Probe:*
- Title: `OXYGEN PROBE (ZIRCONIA)` Barlow SemiBold 18 pt `#27AE60`
- Stat: `PRIMARY CONTROL -- REAL-TIME` JetBrains Mono 14 pt `#27AE60`
- Details (Inter Regular 13 pt `#F0EDE8`):
```
PRINCIPLE:
Zirconia ceramic sensor measures O2
partial pressure; calculates Cp via
Nernst equation

ACCURACY: +/-0.03% C (when calibrated)

RESPONSE TIME: Seconds -- true real-time

ADVANTAGES:
- Continuous feedback for automatic control
- Direct furnace atmosphere measurement
- Industry standard for production

CALIBRATION:
- Requires known reference atmosphere
- Cross-check with shim stock weekly
- Replace sensor per manufacturer schedule
```

*Card 2 -- Dew Point Analyzer:*
- Title: `DEW POINT ANALYZER` Barlow SemiBold 18 pt `#2EC4B6`
- Stat: `BACKUP / CROSS-CHECK` JetBrains Mono 14 pt `#2EC4B6`
- Details:
```
PRINCIPLE:
Measures water vapor (H2O) content in
furnace atmosphere; correlates to Cp
via equilibrium tables

ACCURACY: +/-0.05% C

RESPONSE TIME: Minutes (sample transport)

ADVANTAGES:
- Independent of O2 probe
- Good backup measurement
- Simple principle

LIMITATIONS:
- Slower response than O2 probe
- Affected by sample line condensation
- Requires clean, dry sample line
```

*Card 3 -- Infrared CO2 Analyzer:*
- Title: `INFRARED CO2 ANALYZER` Barlow SemiBold 18 pt `#E8A020`
- Stat: `HIGH-ACCURACY BACKUP` JetBrains Mono 14 pt `#E8A020`
- Details:
```
PRINCIPLE:
Measures CO2 concentration in atmosphere;
derives Cp from CO/CO2 equilibrium ratio

ACCURACY: +/-0.03% C

RESPONSE TIME: Seconds to minutes

ADVANTAGES:
- Very accurate when CO is known
- Independent verification of O2 probe
- Low maintenance

BEST USE:
Cross-check with O2 probe; some facilities
use IR as primary and O2 probe as backup
```

*Card 4 -- Shim Stock (Foil Test):*
- Title: `SHIM STOCK (FOIL TEST)` Barlow SemiBold 18 pt `#E8A020`
- Stat: `DEFINITIVE VERIFICATION` JetBrains Mono 14 pt `#E8A020`
- Details:
```
PRINCIPLE:
Thin steel foil (0.002") weighed before
and after exposure to furnace atmosphere;
weight gain = carbon absorbed (gravimetric)

ACCURACY: Definitive -- direct measurement

RESPONSE TIME: Hours (post-exposure analysis)

USE CASE:
- Weekly calibration check for O2 probe
- Process qualification runs
- Dispute resolution (when probes disagree)
- Not real-time -- cannot control a cycle

THE GOLD STANDARD: when in doubt,
the shim stock result wins.
```

---

### ZONE 4 -- Atmosphere Composition Targets

**Section label:** `TARGET ATMOSPHERE COMPOSITION -- METHANE-BASED ENDO` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Two-column layout (Y: 15.3" to 21.8")**

*Left -- Composition Table (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `ENDOTHERMIC GAS TARGETS` Barlow SemiBold 18 pt `#E8A020`

| Component | Target Range | Notes |
|---|---|---|
| CO | 18.8--20.5% | Primary carbon carrier |
| H2 | 38--42% | Reducing agent; flammable |
| N2 | 38--42% | Balance gas; inert |
| CO2 | 0.10--0.50% | Varies with Cp setpoint |
| CH4 | <0.5% | Generator efficiency indicator |
| Dew Point | -5 to +10 F | At 0.80% Cp; higher for higher Cp |

Data: JetBrains Mono 11 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt.

*Right -- Cp Interpretation Guide (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `READING THE NUMBERS` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
CARBON POTENTIAL (Cp):
The % carbon the atmosphere would produce
at the steel surface at equilibrium.

HOW TO INTERPRET:
- Cp 0.80% = atmosphere wants to put
  0.80% carbon at the surface
- If steel already has 0.20% C, carbon
  will diffuse INTO the surface
- If surface has 1.0% C and Cp is 0.80%,
  carbon diffuses OUT (decarburization)

CRITICAL THRESHOLDS:
- Below 0.70% Cp = insufficient carburizing
- 0.75--0.85% Cp = DIFFUSE phase target
- 0.90--1.10% Cp = BOOST phase target
- Above 1.10% Cp = CARBIDE NETWORK RISK

O2 PROBE mV INCREASES as Cp increases
(higher mV = lower O2 = higher Cp)
```

---

### ZONE 5 -- Boost/Diffuse Cycle

**Section label:** `THE BOOST/DIFFUSE CYCLE -- TWO PHASES, ONE CASE` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- Boost Phase (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `BOOST PHASE` Barlow SemiBold 18 pt `#27AE60`
Subtitle: `Rapid Carbon Absorption` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content (Inter Regular 13 pt `#F0EDE8`):
```
CARBON POTENTIAL: 0.90--1.10% C
PURPOSE: Drive carbon into the surface
  as fast as thermodynamics allow

WHAT HAPPENS:
- High Cp gradient between atmosphere
  and steel surface
- Carbon absorbs rapidly at the surface
- Surface carbon rises toward Cp setpoint
- Enrichment gas (CH4 or C3H8) added
  above base endo level

DURATION: Majority of cycle time
  (roughly 2/3 of total boost+diffuse)

BOOST:DIFFUSE RATIO: ~2:1 (typical)

RISK: Cp above 1.10% = surface carbon
  exceeds solubility limit = carbide
  network along grain boundaries = REJECT
```

*Right -- Diffuse Phase (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `DIFFUSE PHASE` Barlow SemiBold 18 pt `#2EC4B6`
Subtitle: `Carbon Redistribution` JetBrains Mono 12 pt `#F0EDE8` at 60%

Content (Inter Regular 13 pt `#F0EDE8`):
```
CARBON POTENTIAL: 0.75--0.85% C
PURPOSE: Allow carbon to diffuse inward;
  reduce surface carbon concentration

WHAT HAPPENS:
- Lower Cp reduces carbon absorption rate
- Carbon already at the surface migrates
  deeper into the part (Fick's law)
- Surface carbon drops to target range
  (0.75--0.95% C final)
- Any surface carbides dissolve back
  into austenite

DURATION: Roughly 1/3 of total cycle

WHY IT MATTERS:
Without diffuse, you get:
- Excessive surface carbon (>1.0%)
- Carbide networks at grain boundaries
- High retained austenite
- A part that LOOKS carburized but
  fails in service
```

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `Boost puts the carbon in. Diffuse puts the carbon where it belongs. Skip either and the metallurgy will punish you.` Inter Medium 14 pt `#27AE60`, center.

---

### ZONE 6 -- Enrichment & Soot

**Section label:** `ENRICHMENT GAS & SOOT PREVENTION` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four quick-reference cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `NATURAL GAS (CH4)` | Most common enrichment gas. Cracks at furnace temp to deposit carbon. Flow rate controlled by O2 probe feedback loop. |
| 2 | 6.33" | 5.5" | `PROPANE (C3H8)` | Alternative enrichment. Higher carbon content per molecule. Lower flow rate required. More soot-prone than CH4. |
| 3 | 12.16" | 5.5" | `SOOT = TROUBLE` | Soot deposits insulate steel surface from atmosphere. Causes non-uniform case, soft spots, and variable carbon profile. Reduce enrichment flow if soot visible. |
| 4 | 18.0" | 5.5" | `OVER-ENRICHMENT` | Cp reading correct but case still non-uniform? Check for soot. Probe reads atmosphere Cp -- not what the PART sees through a soot layer. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#E8A020`.
Title: Barlow SemiBold 14 pt `#E8A020`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Atmosphere & Cycle Control -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7, general industry practice. Carbon potential control parameters are typical values -- consult your process specification and O2 probe manufacturer for calibration procedures.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Atmosphere Cycle Control Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically dense poster in the DH-01 cluster. Carbon potential control is the core competency of a carburizing operation -- everything flows from Cp. The four control method cards give operators a comprehensive understanding of their instrumentation, and the boost/diffuse explanation makes the cycle logic intuitive. The "shim stock wins" callout is a real-world truth that experienced heat treaters will nod at -- when the instruments disagree, the gravimetric test settles the argument.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #564 -- Construction Workup v1.0*
*2026-04-26*
