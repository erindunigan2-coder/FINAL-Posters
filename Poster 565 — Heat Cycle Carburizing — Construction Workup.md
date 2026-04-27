---
Project: Plating Posters Inc
Poster Number: 565
Title: "Heat Cycle -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.7)"
Technical Source: Gas carburizing heat cycle -- temperatures, case depth vs. time (sqrt relationship), ECD vs. TCD, cycle structure (boost/diffuse example at 1700 F for 0.040" ECD). Per ASM Handbook Vol. 4, AMS 2759/7.
Process Scope: Gas carburizing heat cycle (Stage 5 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - HeatCycle
  - CaseDepth
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #565 -- Construction Workup
## Heat Cycle -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the numbers poster -- the one the process engineer reaches for when planning a new carburizing recipe. Case depth vs. time at 1700 F, the sqrt(t) relationship, boost/diffuse cycle structure, and the critical temperature decisions that determine grain size, diffusion rate, and cycle time. If the Process Flow poster (#559) is the map, this poster is the GPS coordinates.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Case depth vs. time table (Block B -- HERO):** Large reference table -- ECD at 1700 F with total cycle times. The single most consulted data point in carburizing operations.
2. **Temperature decision panel (Block D):** Why 1650, 1700, or 1750 F -- the tradeoffs.
3. **Cycle structure example (Block E):** Worked example of a 0.040" ECD cycle at 1700 F showing boost and diffuse phases with timing.
4. **ECD vs. TCD and sqrt law strip (Block F):** Quick-reference callouts on the key metallurgical relationships.

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
  Stage 5 highlighted (Emerald)
ZONE 3 -- CASE DEPTH VS. TIME HERO (4.2"--14.5" / ~10.3")
  Block B: ECD reference table + sqrt(t) explanation
ZONE 4 -- TEMPERATURE DECISIONS (14.5"--22.0" / ~7.5")
  Block D: Three temperature cards (1650 / 1700 / 1750 F)
ZONE 5 -- CYCLE STRUCTURE EXAMPLE (22.0"--28.5" / ~6.5")
  Block E: Worked example -- 0.040" ECD at 1700 F
ZONE 6 -- KEY RELATIONSHIPS (28.5"--32.5" / ~4.0")
  Block F: ECD vs. TCD, sqrt law, temperature effect
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEAT CYCLE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Stage 5 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Temperature is the throttle. Time is the dial. Case depth follows the square root of time -- double the depth costs four times the hours. Plan accordingly.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Furnace at carburizing temperature, atmosphere controlled  -->  After: Target case depth achieved, ready for quench`

---

### ZONE 3 -- Case Depth vs. Time (HERO)

**Section label:** `CASE DEPTH VS. TIME AT 1700 F (927 C) -- THE CARBURIZER'S REFERENCE TABLE` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Left: ECD Table (X: 0.5", W: 14.0")**

Y: 5.0" to 13.0". Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `EFFECTIVE CASE DEPTH (ECD) AT 1700 F` Barlow SemiBold 20 pt `#27AE60`
Subtitle: `ECD measured to 50 HRC (513 HV, ~0.40% C) per SAE J423` JetBrains Mono 12 pt `#F0EDE8` at 60%

| Target ECD (in.) | Target ECD (mm) | Approx. Time at Temp | TCD (approx.) | Typical Application |
|---|---|---|---|---|
| 0.020 | 0.51 | 1.0--1.5 hr | 0.030--0.035" | Light-duty pins, bushings |
| 0.030 | 0.76 | 2.0--3.0 hr | 0.045--0.055" | Small gears, shafts |
| 0.040 | 1.02 | 3.0--5.0 hr | 0.060--0.070" | Medium gears, splines |
| 0.060 | 1.52 | 6.0--9.0 hr | 0.085--0.100" | Automotive transmission gears |
| 0.080 | 2.03 | 10--14 hr | 0.110--0.130" | Heavy-duty gears, bearings |
| 0.100 | 2.54 | 16--22 hr | 0.140--0.160" | Large industrial gears |
| 0.150 | 3.81 | 36--50 hr | 0.210--0.240" | Mining/off-highway gears |

Data: JetBrains Mono 12 pt `#F0EDE8`. Header: Barlow SemiBold 12 pt. Alternating rows: `#1E2435` / `#252B3D`.

**BLOCK B -- Right: Sqrt Law Explanation (X: 15.0", W: 8.5")**

Y: 5.0" to 13.0". Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `THE SQUARE ROOT RULE` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
THE FUNDAMENTAL LAW:
ECD = K x sqrt(t)

WHERE:
K = carburizing constant
    (temperature-dependent)
    ~0.018--0.025 in./sqrt(hr) at 1700 F
t = time at temperature (hours)

WHAT THIS MEANS:
- Double the ECD = 4x the time
- Triple the ECD = 9x the time
- This is Fick's Second Law in action

EXAMPLE:
0.040" ECD takes ~4 hours
0.080" ECD takes ~12 hours (not 8)
0.160" ECD takes ~48 hours (not 16)

THE IMPLICATION:
Deep cases are EXPENSIVE in furnace time.
Every additional 0.010" of case depth
costs progressively more hours.

TEMPERATURE EFFECT:
A 100 F increase in carburizing temp
roughly DOUBLES the diffusion coefficient.
1800 F processes ~2x faster than 1700 F.
```

---

### ZONE 4 -- Temperature Decisions

**Section label:** `CHOOSING YOUR CARBURIZING TEMPERATURE` -- Y: 14.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Three Temperature Cards (Y: 15.3" to 21.8")**

Three side-by-side callout boxes:

| Card | X | W | Temp | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | 1650 F (899 C) | `#2EC4B6` |
| 2 | 8.17" | 7.33" | 1700 F (927 C) | `#27AE60` |
| 3 | 15.83" | 7.67" | 1750 F (954 C) | `#E8A020` |

Each: Rounded rect H: 6.2", fill `#1E2435`, left accent 0.06".

*Card 1 -- 1650 F:*
- Title: `1650 F (899 C)` Barlow SemiBold 20 pt `#2EC4B6`
- Stat: `CONSERVATIVE` JetBrains Mono 14 pt `#2EC4B6`
- Content (Inter Regular 13 pt `#F0EDE8`):
```
WHEN TO USE:
- Fine-pitch gears where grain size
  is critical (AGMA Grade 7+)
- Thin cases (0.010--0.030" ECD)
- Parts sensitive to distortion

ADVANTAGES:
- Finer grain size (ASTM 6-8)
- Less distortion
- Better fatigue life per unit case depth

TRADEOFF:
- Slower diffusion = longer cycles
- ~30% longer than 1700 F for
  equivalent case depth
```

*Card 2 -- 1700 F:*
- Title: `1700 F (927 C)` Barlow SemiBold 20 pt `#27AE60`
- Stat: `INDUSTRY STANDARD` JetBrains Mono 14 pt `#27AE60`
- Content:
```
WHEN TO USE:
- General production carburizing
- Most gear and bearing applications
- Balanced cycle time vs. quality

ADVANTAGES:
- Good balance: speed vs. grain size
- Well-characterized in industry
- All ECD tables reference this temp
- Grain size: ASTM 5-7 (acceptable)

THIS IS YOUR DEFAULT:
Unless the specification or part design
demands otherwise, 1700 F is where
most carburizing happens.
```

*Card 3 -- 1750 F:*
- Title: `1750 F (954 C)` Barlow SemiBold 20 pt `#E8A020`
- Stat: `HIGH PRODUCTIVITY` JetBrains Mono 14 pt `#E8A020`
- Content:
```
WHEN TO USE:
- Deep cases (>0.060" ECD) where
  cycle time reduction is critical
- Large gears, mining equipment
- When grain size is less critical

ADVANTAGES:
- ~25% faster than 1700 F
- Significant cost savings on deep cases
- Wider temperature window for continuous
  furnace operations

RISK:
- Grain growth (ASTM 4-5 or coarser)
- Not suitable for fine-pitch gears
- Higher IGO tendency
- Requires fine-grain steel (Al-killed)
```

---

### ZONE 5 -- Cycle Structure Example

**Section label:** `WORKED EXAMPLE -- 0.040" ECD AT 1700 F` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Horizontal timeline (Y: 22.9" to 28.3")**

Rounded rect full width, fill `#1E2435`.

Title: `TYPICAL CYCLE STRUCTURE FOR 0.040" ECD AT 1700 F (927 C)` Barlow SemiBold 16 pt `#27AE60`. Y: 23.1".

Four phase boxes in a horizontal sequence with arrows:

| Phase | X | W | Duration | Cp | Color |
|---|---|---|---|---|---|
| HEAT | 0.8" | 4.5" | 1--2 hr | -- | `#E8A020` |
| BOOST | 5.8" | 7.0" | 2.5 hr | 1.0% C | `#27AE60` |
| DIFFUSE | 13.3" | 5.0" | 1.5 hr | 0.80% C | `#2EC4B6` |
| TO QUENCH | 18.8" | 4.5" | -- | -- | `#E05C5C` |

Each phase box: Rounded rect H: 2.5", fill `#252B3D`, top accent 4 pt in phase color.

Phase label: Barlow SemiBold 16 pt in accent color.
Duration: JetBrains Mono 14 pt `#F0EDE8`.
Cp value: JetBrains Mono 12 pt `#F0EDE8` at 70%.

Below timeline (Y: 26.5"):

Content (Inter Regular 13 pt `#F0EDE8`):
```
TOTAL CYCLE: ~5--6.5 hours (heat + boost + diffuse)
BOOST:DIFFUSE RATIO: 2.5 : 1.5 = ~1.7:1 (close to the 2:1 rule of thumb)
RESULT: 0.040" ECD, surface carbon 0.80--0.85%, surface hardness 60--62 HRC after quench and temper
NOTE: This is a TYPICAL example. Your specification, steel grade, and furnace characteristics will require recipe optimization.
```

---

### ZONE 6 -- Key Relationships

**Section label:** `KEY METALLURGICAL RELATIONSHIPS` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Three quick-reference cards (Y: 29.4" to 32.3")**

| Card | X | W | Title | Content |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `ECD vs. TCD` | ECD = depth to 50 HRC (~0.40% C). TCD = depth to core carbon level. TCD = 1.5--2.0x ECD. Specify which one your drawing calls out -- they are NOT interchangeable. |
| 2 | 8.17" | 7.33" | `SQRT(TIME) RULE` | Case depth proportional to sqrt(time). Double the depth = 4x the hours. The most important number in carburizing economics. Plan cycle time BEFORE committing the furnace. |
| 3 | 15.83" | 7.67" | `TEMPERATURE EFFECT` | +100 F = ~2x diffusion coefficient. Going from 1700 to 1800 F cuts cycle time roughly in half -- but watch grain size. This is why vacuum carburizing at 1800+ F is gaining ground. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#27AE60`.
Title: Barlow SemiBold 14 pt `#27AE60`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Heat Cycle -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7, SAE J423. Case depth vs. time values are typical ranges at 1700 F (927 C) for standard production carburizing. Actual results depend on steel grade, furnace type, atmosphere composition, and quench severity.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heat Cycle Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the engineer's poster. The case depth vs. time table is the single most referenced piece of data in any carburizing operation -- it should dominate the hero zone and be readable from 8 feet. The sqrt(t) explanation turns an abstract equation into practical cycle planning. The temperature decision cards give operators and engineers a framework for choosing their carburizing temperature instead of just defaulting to "whatever we always do." The worked example makes the boost/diffuse concept concrete.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #565 -- Construction Workup v1.0*
*2026-04-26*
