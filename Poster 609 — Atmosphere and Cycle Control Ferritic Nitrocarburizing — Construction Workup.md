---
Project: Plating Posters Inc
Poster Number: 609
Title: "Atmosphere & Cycle Control -- Ferritic Nitrocarburizing (FNC / Q-P-Q)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / Q-P-Q, Section 6.6)"
Technical Source: FNC cycle parameters -- nitrocarburizing temperature (1050-1125 F), immersion times (60-240 min), oxidizing quench parameters (700-800 F, 15-30 min), total Q-P-Q cycle time (2.5-5 hours). Per AMS 2753 and AMS 2755.
Process Scope: Ferritic nitrocarburizing atmosphere and cycle control (Stages 3-4 of 9)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - Q-P-Q
  - CycleControl
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #609 -- Construction Workup
## Atmosphere & Cycle Control -- Ferritic Nitrocarburizing (FNC / Q-P-Q)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The cycle control poster for FNC. Unlike gas carburizing (where carbon potential is measured in real time) or vacuum carburizing (where recipes are simulation-driven), salt bath FNC is controlled by three straightforward variables: bath temperature, immersion time, and bath composition. The simplicity is part of the appeal -- but the bath chemistry must be monitored and maintained. This poster covers all the cycle timing parameters and connects each Q-P-Q stage to its purpose.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Q-P-Q cycle timeline (Block B -- HERO):** Full timeline showing each Q-P-Q stage with duration, temperature, and purpose.
2. **Parameter table (Block D):** All cycle control parameters in one reference table.
3. **Compound zone growth vs. time (Block E):** How immersion time affects the compound zone.
4. **Total cycle time callout (Block F):** 2.5-5 hours from preheat to final rinse.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 3 and 4 highlighted
ZONE 3 -- Q-P-Q CYCLE TIMELINE HERO (4.2"--15.5" / ~11.3")
  Block B: Horizontal timeline with all Q-P-Q stages
ZONE 4 -- PARAMETER TABLE (15.5"--22.0" / ~6.5")
  Block D: All cycle parameters
ZONE 5 -- COMPOUND ZONE GROWTH (22.0"--28.5" / ~6.5")
  Block E: Time vs. compound zone thickness
ZONE 6 -- TOTAL CYCLE TIME (28.5"--32.5" / ~4.0")
  Block F: Cycle time callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ATMOSPHERE & CYCLE CONTROL` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ferritic Nitrocarburizing (FNC / Q-P-Q) -- Stages 3 and 4 of 9` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Three variables: bath temperature, immersion time, bath composition. Salt bath FNC is simpler to control than gas-phase processes -- but the chemistry must be maintained. Cyanate content is your process control knob.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 3 and 4 highlighted: Stage 3 fill `#27AE60` (Nitrocarburize), Stage 4 fill `#E8A020` (Oxidizing Quench). Others dimmed.
Below: `Before: Parts preheated and fixtured  -->  After: Compound zone formed, oxide sealed`

---

### ZONE 3 -- Q-P-Q Cycle Timeline (HERO)

**Section label:** `THE COMPLETE Q-P-Q CYCLE -- TIME AND TEMPERATURE` -- Y: 4.4". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Horizontal Timeline (Y: 5.0" to 14.5")**

Full-width rounded rect fill `#1E2435`, border 1 pt `#3A4055`.

Horizontal timeline with time scale along the bottom (minutes). Seven blocks representing the Q-P-Q stages:

| Stage | Start (min) | Duration (min) | Temperature | Fill | Label |
|---|---|---|---|---|---|
| Preheat | 0 | 15--30 | 600--700 F | `#E8A020` at 20% | PREHEAT |
| FNC Bath | 30 | 60--120 | 1050--1075 F | `#27AE60` at 30% | NITROCARBURIZE |
| Q1 (Oxidizing) | 150 | 15--30 | 700--800 F | `#E8A020` at 30% | Q1 |
| Rinse | 180 | 5--10 | Hot water | `#2EC4B6` at 20% | RINSE |
| Polish | 190 | 10--30 | Ambient | `#C8D0D8` at 20% | POLISH |
| Q2 (Oxidizing) | 220 | 15--30 | 700--800 F | `#E8A020` at 30% | Q2 |
| Final Rinse | 250 | 5--10 | Hot water | `#2EC4B6` at 20% | FINAL RINSE |

Each block: Rounded rect at proportional width on timeline, height 3.5", with stage label inside.

*Above each block -- purpose annotation:*
- Preheat: `Drives off moisture (safety)`
- FNC Bath: `N + C diffuse into ferrite; epsilon compound zone forms`
- Q1: `Magnetite oxide seals compound zone pores`
- Rinse: `Removes residual salt before polish`
- Polish: `Smooth to Ra 8--16 micro-inch; expose fresh surface`
- Q2: `Second oxide layer on polished surface`
- Final Rinse: `Remove all salt; apply rust preventative`

Inter Regular 12 pt `#F0EDE8`.

*Below timeline -- total time bar:*
- `TOTAL Q-P-Q CYCLE: 2.5--5 HOURS (preheat to final rinse)` Barlow SemiBold 20 pt `#E8A020`
- `Compare to gas nitriding: 24--90 hours. Q-P-Q is dramatically faster for equivalent wear and corrosion performance.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Parameter Table

**Section label:** `CYCLE CONTROL PARAMETERS -- COMPLETE REFERENCE` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Parameter Table (Y: 16.3" to 21.8")**

| Parameter | Value | Control Method | Frequency |
|---|---|---|---|
| FNC bath temperature | 1050--1125 F (566--607 C); target 1075 F | Thermocouple + controller | Continuous |
| FNC immersion time | 60--120 min (standard); up to 240 min | Timer | Per load |
| Cyanate content (CNO) | 35--40% | Titration | Every shift |
| Cyanide content (CN) | Below regulatory limit | Analysis | Per schedule |
| Oxidizing bath temperature | 700--800 F (371--427 C) | Thermocouple + controller | Continuous |
| Oxidizing immersion time | 15--30 min (Q1 and Q2 each) | Timer | Per load |
| Polish surface finish | Ra 8--16 micro-inch | Profilometer | Per lot |
| Bath sludge level | Minimal (remove regularly) | Visual + ladle | Weekly |

Table: Header `#3A4055`, alternating rows `#252B3D` / `#1E2435`. JetBrains Mono 12 pt.

---

### ZONE 5 -- Compound Zone Growth

**Section label:** `COMPOUND ZONE THICKNESS VS. IMMERSION TIME` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column layout (Y: 22.9" to 28.3")**

*Left -- Growth Table (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `AT 1075 F (580 C) IN STANDARD SALT BATH` Barlow SemiBold 16 pt `#27AE60`

| Immersion Time | Compound Zone | Diffusion Zone |
|---|---|---|
| 60 minutes | 0.0004--0.0006" (10--15 um) | 0.005--0.010" |
| 90 minutes | 0.0005--0.0008" (13--20 um) | 0.008--0.015" |
| 120 minutes | 0.0006--0.001" (15--25 um) | 0.010--0.020" |
| 240 minutes | 0.001--0.0015" (25--38 um) | 0.015--0.025" |

JetBrains Mono 13 pt.

Below: `Compound zone growth follows a parabolic (square root of time) relationship -- doubling the time does NOT double the thickness.` Inter Regular 12 pt `#F0EDE8` at 70%.

*Right -- What Controls Thickness (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `FACTORS AFFECTING COMPOUND ZONE` Barlow SemiBold 16 pt `#E8A020`

Content:
```
TEMPERATURE:
Higher bath temp = faster growth
But stay below Ac1 (ferritic range)
1125 F is the practical maximum

TIME:
Longer immersion = thicker zone
Diminishing returns past 120 min
(parabolic growth)

BATH COMPOSITION:
Higher cyanate = more active nitrogen
and carbon source = faster growth
Target 35--40% CNO for standard results

SUBSTRATE:
Different steels absorb N and C at
different rates. 1018 and 4140 are
standard references. Stainless steels
(410, 420) respond more slowly.

SURFACE CONDITION:
Clean, oxide-free surface absorbs
faster. Passive films (Cr2O3 on
stainless) slow initial absorption.
```

---

### ZONE 6 -- Total Cycle Time

**Section label:** `CYCLE TIME COMPARISON` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four comparison cards (Y: 29.4" to 32.3")**

| Card | X | W | Process | Typical Cycle Time |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `FNC/Q-P-Q (SALT BATH)` | 2.5--5 hours total. Preheat to final rinse. Wear + corrosion in one cycle. |
| 2 | 6.33" | 5.5" | `GAS NITRIDING` | 24--90 hours. Deeper case possible but dramatically longer. No built-in corrosion treatment. |
| 3 | 12.16" | 5.5" | `HARD CHROME PLATE` | 2--8 hours (plating time). But hexavalent chromium. Q-P-Q is the replacement candidate. |
| 4 | 18.0" | 5.5" | `GAS FNC (ATMOSPHERE)` | 2--4 hours (FNC step only). No oxidizing quench = lower corrosion unless supplemented. |

Each: Rounded rect H: 2.7", fill `#1E2435`, left accent `#2EC4B6`.
Title: Barlow SemiBold 14 pt `#2EC4B6`.
Details: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Atmosphere & Cycle Control -- Ferritic Nitrocarburizing (FNC / Q-P-Q)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755. Cycle times and compound zone growth rates are typical values for standard salt bath FNC. Actual results depend on bath composition, steel grade, and equipment. Consult your salt bath supplier for application-specific cycle recommendations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Atmosphere Cycle Control Ferritic Nitrocarburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The Q-P-Q cycle timeline is the hero -- it shows production managers that the entire Q-P-Q process fits into half a shift, which is dramatically faster than gas nitriding (days). The compound zone growth table is the metallurgist's reference. The cycle time comparison strip at the bottom positions Q-P-Q against its competitors -- gas nitriding for case depth, hard chrome for corrosion -- and makes a compelling case for FNC/Q-P-Q as the process that delivers both in one short cycle.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #609 -- Construction Workup v1.0*
*2026-04-26*
