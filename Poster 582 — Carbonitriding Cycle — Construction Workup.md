---
Project: Plating Posters Inc
Poster Number: 582
Title: "Carbonitriding Cycle"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding, Sections 3.1, 3.4, 3.5)"
Technical Source: The carbonitriding diffusion cycle itself -- temperature, carbon potential, ammonia addition, time-at-temperature, case depth expectations. This is the "main tank" equivalent for heat treatment.
Process Scope: Carbonitriding cycle -- time, temperature, atmosphere control, case depth
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - CarbonitrideProcess
  - Diffusion
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #582 -- Construction Workup
## Carbonitriding Cycle

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the "main tank" poster for carbonitriding -- the core process cycle where carbon and nitrogen simultaneously diffuse into the steel surface. The hero visual is a time-temperature profile showing the hold at 1400--1600 F with ammonia overlay. The case depth table is the most referenced data on this poster -- operators and engineers need to know how long to run for a given case depth.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Time-temperature profile hero (Block B):** A horizontal chart showing temp on Y-axis, time on X-axis. Heat-up ramp, hold at carbonitriding temperature, direct quench drop. Ammonia flow shown as a colored band overlay.
2. **Case depth vs. time table (Block D):** 4-row table showing ECD targets and cycle times.
3. **Suitable steels panel (Block E):** Steel grade table showing ideal carbonitriding candidates.
4. **Metallurgical mechanism callout (Block F):** Simplified description of what happens at the atomic level.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- TIME-TEMPERATURE PROFILE / HERO (2.9"--14.5" / ~11.6")
  Block B: T-T profile chart with ammonia overlay
  Block C: Key parameter callouts alongside chart
ZONE 3 -- CASE DEPTH TABLE (14.5"--20.5" / ~6.0")
  Block D: ECD vs. time at 1550 F
ZONE 4 -- SUITABLE STEELS (20.5"--26.5" / ~6.0")
  Block E: Steel grade table
ZONE 5 -- METALLURGICAL MECHANISM (26.5"--32.5" / ~6.0")
  Block F: What happens at the atomic level
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CARBONITRIDING CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Time, Temperature, and Atmosphere -- Where Carbon Meets Nitrogen` -- 32 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Lower temperature than carburizing. Thinner case. But nitrogen makes the impossible possible -- martensite in 1018.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Time-Temperature Profile (HERO)

**Section label:** `THE CARBONITRIDING CYCLE PROFILE` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- T-T Profile Chart**

Y: 3.8" to 13.0". Chart area: X: 2.0" to 22.0", Y: 4.5" to 12.5".

**Axes:**
- Y-axis (left): Temperature, 0--1800 F. Labels at 0, 300, 600, 900, 1200, 1400, 1600 F. JetBrains Mono 11 pt `#F0EDE8` at 60%.
- X-axis (bottom): Time. Labels: `0`, `Heat-Up`, `Soak`, `Hold (1--6 hr)`, `Quench`. JetBrains Mono 11 pt `#F0EDE8` at 60%.
- Axis lines: 1 pt `#3A4055`.
- Grid lines: 0.5 pt `#3A4055` at 30%.

**Temperature profile line:**
- Stroke: 3 pt `#E8A020`
- Shape: ramp up from ambient (~75 F) to 1400--1600 F, flat hold for the cycle duration, then vertical drop to ~180 F (oil quench temperature)
- The ramp takes approximately 15% of the chart width
- The hold is approximately 60% of the chart width
- The quench drop is approximately 5% of the chart width (nearly vertical)

**Ammonia overlay band:**
- Semi-transparent band (`#2EC4B6` at 20%) overlaid on the hold phase
- Label inside band: `NH3: 2--10% by volume` Barlow SemiBold 14 pt `#2EC4B6`

**Carbon potential overlay:**
- Dashed line within hold phase at ~70% of chart height
- Label: `Cp: 0.5--0.8% C` JetBrains Mono 13 pt `#E8A020`

**Key annotations on chart:**
- At start of hold: `Austenitization complete` Inter Regular 11 pt `#F0EDE8` at 60%
- At quench drop: `Direct oil quench` Inter Medium 12 pt `#E8A020`
- At post-quench: `Oil temp: 120--180 F` JetBrains Mono 11 pt `#E8A020` at 70%

**BLOCK C -- Parameter Callouts (right side, X: 16.0")**

Three small callout boxes stacked vertically:

| Callout | Accent | Content |
|---|---|---|
| Temperature | `#E8A020` | `1400--1600 F (760--870 C)` / `Typical: 1500--1550 F` |
| Atmosphere | `#2EC4B6` | `Endo gas + 2--10% NH3` / `Cp: 0.5--0.8% C` / `Surface N: 0.2--0.4 wt%` |
| Time | `#27AE60` | `1--6 hours` / `Case depth dependent` / `Max practical: 0.030 in ECD` |

Each: Rounded rect, W: 6.5", H: 2.0", fill `#1E2435`, left accent 0.06".

---

### ZONE 3 -- Case Depth Table

**Section label:** `CASE DEPTH VS. TIME (at 1550 F / 845 C)` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Case Depth Table**

Y: 15.3" to 20.3". Columns: ECD Target (5.0") | Time at 1550 F (5.0") | Application (6.0") | Notes (7.0")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 1.0".

| ECD (at 50 HRC) | Time at 1550 F | Application | Notes |
|---|---|---|---|
| 0.005 in (0.13 mm) | 1--1.5 hours | Thin wear case; light-duty | Minimum practical |
| 0.010 in (0.25 mm) | 2--3 hours | Standard automotive; fasteners | Most common target |
| 0.020 in (0.50 mm) | 3--4 hours | Heavy-duty wear surfaces | Approaching maximum |
| 0.030 in (0.75 mm) | 5--6 hours | Maximum practical for CN | Above this: switch to carburizing |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Notes column: Inter Regular 12 pt.

Bottom callout: `Above 0.030 in ECD, switch to carburizing. Carbonitriding at depth = excessive retained austenite from high nitrogen content.` -- Inter Medium, 14 pt, `#E8A020`.

---

### ZONE 4 -- Suitable Steels

**Section label:** `IDEAL STEELS FOR CARBONITRIDING` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Steel Grade Table**

Y: 21.3" to 26.3". Columns: Category (4.5") | Grades (6.0") | Why Carbonitriding? (12.5")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 1.0".

| Category | Grades | Why Carbonitriding? |
|---|---|---|
| Plain carbon | 1018, 1020, 1022 | Low hardenability -- NEED the nitrogen boost to form martensite |
| Free machining | 12L14, 1117, 1215, 1144 | Classic CN candidates; sulfur inclusions tolerable in thin cases |
| Sintered (PM) | Iron-based powder metal | Porosity limits case depth; CN's thin case is ideal |
| Low alloy (optional) | 8620 | Works but often overkill -- carburizing is usually better for these |

Data: JetBrains Mono Regular, 12 pt. Category: Inter Medium 13 pt.

Bottom callout: `The whole point of carbonitriding: nitrogen lowers the critical cooling rate so that even 1018 can form hard martensite under oil quench.` -- Inter Medium, 14 pt, `#27AE60`.

---

### ZONE 5 -- Metallurgical Mechanism

**Section label:** `WHAT HAPPENS IN THE FURNACE` -- Y: 26.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK F -- Mechanism Callout**

Y: 27.3" to 32.3". Full-width callout box.

Rounded rect, X: 0.5", Y: 27.3", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06".

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):

**Three-step mechanism:**

1. `CARBON TRANSFER: 2CO -> C(dissolved) + CO2 at the steel surface`
   - `Carbon from endo gas dissolves into austenite` -- `#E8A020`

2. `NITROGEN TRANSFER: NH3 -> N(atomic) + 3/2 H2 at the steel surface`
   - `Atomic nitrogen from ammonia dissolves into austenite alongside carbon` -- `#2EC4B6`

3. `DIFFUSION: C and N atoms migrate inward following Fick's law`
   - `Combined C+N = 0.8--1.0% equivalent hardening effect` -- `#27AE60`
   - `Surface nitrogen: 0.2--0.4 wt% N typical`

**Key insight box (bottom, Amber border):**
- `Nitrogen lowers Ms temperature and retards pearlite/bainite transformation. Translation: steels that would form soft pearlite if merely carburized can now be quenched to hard martensite. That is the entire value proposition.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 6 -- Footer

Standard footer. Title: `Carbonitriding Cycle`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Carbonitriding Cycle -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the carbonitriding cluster. The time-temperature profile chart is the hero -- it should be readable at 6 feet, with the ammonia band visually distinct from the temperature line. The case depth table is the most-referenced data. The metallurgical mechanism section bridges the gap between "what to set" and "why it works."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #582 -- Construction Workup v1.0*
*2026-04-26*
