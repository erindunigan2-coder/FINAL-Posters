---
Project: Plating Posters Inc
Poster Number: 573
Title: "Atmosphere & Cycle Control -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.6)"
Technical Source: Acetylene vs. propane vs. ethylene carbon source gases, boost/diffuse pulse parameters, process simulation software (SimVac, CarbTool, DANTE, DEFORM), mass flow control. Per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Vacuum carburizing atmosphere and cycle control (Stage 4 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - AtmosphereControl
  - CycleControl
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #573 -- Construction Workup
## Atmosphere & Cycle Control -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the brain of the LPC process. Unlike gas carburizing where an oxygen probe measures carbon potential in real time, vacuum carburizing is recipe-driven -- the carbon profile is controlled by the timing of boost and diffuse pulses, not by a sensor. Process simulation software pre-calculates the entire recipe. This poster covers the carbon source gas options, the boost/diffuse pulse mechanics, and the simulation-driven approach that makes LPC fundamentally different from atmosphere carburizing.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Boost/diffuse pulse diagram (Block B -- HERO):** Visual timeline showing alternating boost and diffuse phases with pressure levels and carbon absorption.
2. **Carbon source gas comparison (Block D):** Acetylene vs. propane vs. ethylene table.
3. **Process simulation panel (Block E):** SimVac, CarbTool, DANTE -- what they do and why they matter.
4. **No real-time measurement callout (Block F):** The key philosophical difference from gas carburizing.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Emerald)
ZONE 3 -- BOOST/DIFFUSE PULSE HERO (4.2"--15.5" / ~11.3")
  Block B: Pulse timeline diagram
ZONE 4 -- CARBON SOURCE GAS COMPARISON (15.5"--22.0" / ~6.5")
  Block D: Three gas options
ZONE 5 -- PROCESS SIMULATION (22.0"--28.5" / ~6.5")
  Block E: Simulation software and recipe-driven control
ZONE 6 -- KEY DIFFERENCE CALLOUT (28.5"--32.5" / ~4.0")
  Block F: No O2 probe -- recipe is king
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ATMOSPHERE & CYCLE CONTROL` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- Stage 4 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `No oxygen probe. No dew point analyzer. In vacuum carburizing, the recipe IS the control. Computer-simulated boost/diffuse pulses replace real-time atmosphere measurement.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Furnace at carburizing temperature under vacuum  -->  After: Target carbon profile achieved via pulsed recipe`

---

### ZONE 3 -- Boost/Diffuse Pulse Diagram (HERO)

**Section label:** `THE BOOST/DIFFUSE CYCLE -- HOW LPC BUILDS A CARBON PROFILE` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Pulse Timeline (Y: 5.0" to 14.5")**

*Main diagram area:* Rounded rect X: 0.5", Y: 5.0", W: 23.0", H: 9.0", fill `#1E2435`, border 1 pt `#3A4055`.

*Horizontal timeline (Y: 7.5" to 12.0"):*

Visual representation of alternating pressure pulses:

| Phase | Duration | Pressure | Fill Color | Label |
|---|---|---|---|---|
| Boost 1 | 2 min | 5--15 mbar | `#27AE60` at 40% | C2H2 ON |
| Diffuse 1 | 5 min | <1 mbar | `#1A1F2E` | VACUUM |
| Boost 2 | 2 min | 5--15 mbar | `#27AE60` at 40% | C2H2 ON |
| Diffuse 2 | 8 min | <1 mbar | `#1A1F2E` | VACUUM |
| Boost 3 | 1.5 min | 5--15 mbar | `#27AE60` at 40% | C2H2 ON |
| Diffuse 3 | 12 min | <1 mbar | `#1A1F2E` | VACUUM |
| ... | ... | ... | ... | REPEAT 5--30+ CYCLES |

Pulse blocks shown as rectangles at two height levels -- boost pulses raised (representing 5-15 mbar), diffuse phases at baseline (<1 mbar). Arrows between each phase.

*Above timeline -- labels:*
- `BOOST: Acetylene pulsed at 5--15 mbar` Inter Medium 14 pt `#27AE60`
- `Acetylene decomposes on hot steel surface, depositing atomic carbon` Inter Regular 12 pt `#F0EDE8`

- `DIFFUSE: Chamber re-evacuated to <1 mbar` Inter Medium 14 pt `#E8A020`
- `No gas present -- carbon diffuses inward via Fick's Law` Inter Regular 12 pt `#F0EDE8`

*Below timeline -- key parameters:*
```
Boost pulse duration: 30 seconds to 5 minutes
Diffuse duration: 2--30 minutes (longer as recipe progresses)
Number of cycles: 5--30+ per recipe
Boost pressure: 5--15 mbar (controlled by mass flow controllers)
```
JetBrains Mono 12 pt `#F0EDE8`.

*Right side annotation:*
- `DIFFUSE PHASES GET LONGER` Inter Medium 16 pt `#E8A020`
- `Early in the cycle: short diffuse (surface not yet saturated)` Inter Regular 12 pt `#F0EDE8`
- `Late in the cycle: long diffuse (driving carbon deeper into core)` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 4 -- Carbon Source Gas Comparison

**Section label:** `CARBON SOURCE GASES -- ACETYLENE WINS` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Three-column gas comparison (Y: 16.3" to 21.8")**

| Card | X | W | Gas | Accent |
|---|---|---|---|---|
| 1 | 0.5" | 7.33" | Acetylene (C2H2) | `#27AE60` |
| 2 | 8.17" | 7.33" | Propane (C3H8) | `#E8A020` |
| 3 | 15.83" | 7.67" | Ethylene (C2H4) | `#C8D0D8` |

Each: Rounded rect H: 5.2", fill `#1E2435`, left accent 0.06".

*Card 1 -- Acetylene:*
- Title: `ACETYLENE (C2H2)` Barlow SemiBold 18 pt `#27AE60`
- Stat: `PREFERRED FOR MODERN LPC` JetBrains Mono 14 pt `#27AE60`
- Details:
```
- Clean thermal decomposition on steel
- Minimal soot at 5--15 mbar pressure
- Excellent uniformity in blind holes
- Most predictable carbon delivery
- Industry standard for new LPC systems
- Explosive (LEL 2.5%) -- 15 psig max
  line pressure (safety trade-off)
```

*Card 2 -- Propane:*
- Title: `PROPANE (C3H8)` Barlow SemiBold 18 pt `#E8A020`
- Stat: `OLDER SYSTEMS -- HIGHER SOOT RISK` JetBrains Mono 14 pt `#E8A020`
- Details:
```
- Used in some older LPC furnaces
- Higher soot tendency than acetylene
- More complex decomposition products
- Requires higher boost pressures
- Soot deposits cause non-uniform case
- Being phased out in favor of C2H2
```

*Card 3 -- Ethylene:*
- Title: `ETHYLENE (C2H4)` Barlow SemiBold 18 pt `#C8D0D8`
- Stat: `ALTERNATIVE -- LESS COMMON` JetBrains Mono 14 pt `#C8D0D8`
- Details:
```
- Less common than C2H2 or C3H8
- Intermediate soot behavior
- Some niche applications
- Not widely supported by simulation
  software libraries
- Limited published recipe data
```

---

### ZONE 5 -- Process Simulation

**Section label:** `RECIPE-DRIVEN CONTROL -- SIMULATION SOFTWARE` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- Software Tools (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `SIMULATION PACKAGES` Barlow SemiBold 18 pt `#27AE60`

Content:
```
SimVac -- Dedicated LPC recipe simulator
  Predicts carbon profiles for boost/diffuse
  cycles. Widely used by furnace OEMs.

CarbTool -- Carburizing simulation
  General-purpose; includes LPC mode.
  Calculates diffusion using Fick's Law.

DANTE -- Distortion and residual stress
  Full thermo-metallurgical-mechanical sim.
  Predicts distortion during quench.

DEFORM -- Finite element simulation
  Heat treatment module for complex geometry.
  Used for aerospace qualification.
```

*Right -- How It Works (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `THE RECIPE WORKFLOW` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
1. INPUT: Steel grade, part geometry,
   target ECD, surface carbon, furnace
   parameters

2. SIMULATE: Software calculates optimal
   boost/diffuse sequence -- pulse count,
   duration, pressure per pulse

3. OUTPUT: Complete recipe file that the
   furnace controller executes automatically

4. VERIFY: Run test load; measure actual
   carbon profile; compare to simulation

5. LOCK: Approved recipe is frozen and
   run identically for every production load

THIS IS NOT REAL-TIME CONTROL.
The recipe is pre-calculated.
The furnace follows instructions.
```

---

### ZONE 6 -- Key Difference Callout

**Section label:** `THE FUNDAMENTAL DIFFERENCE` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Full-width callout (Y: 29.4" to 32.3")**

Rounded rect W: 23.0", H: 2.7", fill `#1E2435`, left accent `#E8A020`.

Two-column inside:

*Left:*
```
GAS CARBURIZING:
Oxygen probe reads carbon potential
in REAL TIME. Operator adjusts gas
flow based on sensor feedback.
Control = FEEDBACK LOOP.
```

*Right:*
```
VACUUM CARBURIZING (LPC):
No oxygen probe. No dew point.
Recipe is pre-calculated by simulation.
Furnace executes the recipe blindly.
Control = PRE-PROGRAMMED RECIPE.
```

Bottom line: `Both approaches produce the same result. Gas carburizing is like driving with a speedometer. LPC is like programming a self-driving car.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 7 -- Footer

Standard. Title: `Atmosphere & Cycle Control -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7E. Boost/diffuse recipes are specific to the furnace, steel grade, part geometry, and target case profile. Always validate simulated recipes with test loads before production.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Atmosphere Cycle Control Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The pulse timeline diagram is the hero -- it needs to clearly show the alternating boost/diffuse phases at different pressure levels, with the diffuse phases visibly getting longer as the recipe progresses. This is the "aha" moment for operators who understand gas carburizing but not LPC. The "no oxygen probe" callout at the bottom is intentionally provocative -- it challenges the gas carburizing operator's assumption that you always need real-time atmosphere measurement.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #573 -- Construction Workup v1.0*
*2026-04-26*
