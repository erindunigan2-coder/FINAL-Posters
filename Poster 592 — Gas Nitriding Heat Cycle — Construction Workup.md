---
Project: Plating Posters Inc
Poster Number: 592
Title: "Gas Nitriding -- Heat Cycle"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.7)"
Technical Source: Heat cycle parameters for gas nitriding. Slow ramp rates, extended holds at 925-1050 F, and furnace cooling under ammonia. The defining characteristic: no quench, no phase transformation. All hardening occurs during the hold through nitride precipitation.
Process Scope: Gas nitriding -- heat cycle (Stage 7 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - HeatCycle
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #592 -- Construction Workup
## Gas Nitriding -- Heat Cycle

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the heat cycle for gas nitriding -- the longest sustained hold in all of heat treatment. While carburizing holds for 2-50 hours and induction hardening heats in seconds, gas nitriding holds for 15-90 hours at a single temperature below the lower critical. The heat cycle IS the process.

Design philosophy: hero panel showing a stylized time-temperature profile for both single-stage and two-stage processes, a temperature selection guide by steel grade, ramp rate guidelines, and a "what happens at temperature" mechanistic explanation.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Time-temperature profile description (Block B -- HERO):** Text-based description of the cycle profile for both single-stage and two-stage.
2. **Temperature selection by steel grade (Block C).**
3. **Ramp rate and cooling guidelines (Block D).**
4. **Mechanistic explanation panel (Block E).**
5. **Standard formatting: accents, color remap, JetBrains Mono, 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
Standard four-font stack (Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular).

### Step 4 -- Set up color palette
Same as Poster #586 (series standard).

### Step 5 -- Set ruler guides
Standard margins (0.5" all sides). Zone boundaries: 2.9", 14.0", 20.5", 27.0", 32.5".

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- TIME-TEMPERATURE PROFILES / HERO (2.9"--14.0" / ~11.1" tall)
  Block B: Single-stage and two-stage cycle profiles

ZONE 3 -- TEMPERATURE BY STEEL GRADE (14.0"--20.5" / ~6.5" tall)
  Block C: Steel grade vs. nitriding temperature and expected hardness

ZONE 4 -- RAMP RATE & COOLING (20.5"--27.0" / ~6.5" tall)
  Block D: Heating rate, cooling procedure, and cycle timeline

ZONE 5 -- WHAT HAPPENS AT TEMPERATURE (27.0"--32.5" / ~5.5" tall)
  Block E: Mechanistic explanation of nitride precipitation

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `GAS NITRIDING`

**BLOCK A -- Subheading**
- Position: X: 0.5". Y: 1.5". Width: 23.0"
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Heat Cycle -- Time, Temperature & the Longest Hold in Heat Treatment`

**BLOCK A -- Tagline**
- Position: X: 0.5". Y: 2.2". Width: 23.0"
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `15--90 hours at 925--1050 F. Below the critical temperature. No phase transformation. Hardness forms atom by atom through nitride precipitation.`

---

### ZONE 2 -- Time-Temperature Profiles (HERO)

**Dimensions:** Y: 2.9" to 14.0" (~11.1" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `CYCLE PROFILES -- SINGLE-STAGE VS. TWO-STAGE`

---

**BLOCK B -- Two Profile Panels**

**Top -- Single-Stage Profile (X: 0.5", Y: 3.8", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `SINGLE-STAGE CYCLE PROFILE` -- Barlow SemiBold, 22 pt, `#E8A020`

Content (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 160%):
```
Phase 1: RAMP UP      100--200 F/hr to 925--975 F     2--6 hours
Phase 2: HOLD          925--975 F, 15--30% dissociation  24--90 hours
Phase 3: FURNACE COOL  Under NH3 atmosphere to 300 F    4--8 hours
Phase 4: AIR COOL      300 F to ambient                  1--2 hours
```

Total cycle: `30--106 hours (1.3--4.4 days)` -- Inter Medium, 16 pt, `#E8A020`

Description (Inter Regular, 14 pt, `#F0EDE8`):
```
One temperature, one dissociation rate, one long hold. The simplest cycle.
All case building and white layer formation happen simultaneously.
```

**Bottom -- Two-Stage (Floe) Profile (X: 0.5", Y: 9.0", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `TWO-STAGE (FLOE) CYCLE PROFILE` -- Barlow SemiBold, 22 pt, `#27AE60`

Content (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 160%):
```
Phase 1: RAMP UP       100--200 F/hr to 925--975 F     2--6 hours
Phase 2: STAGE 1 HOLD  925--975 F, 15--30% dissociation  15--40 hours
Phase 3: RAMP TO S2    975 F to 1000--1050 F            0.5--1 hour
Phase 4: STAGE 2 HOLD  1000--1050 F, 75--85% dissociation  10--30 hours
Phase 5: FURNACE COOL  Under NH3 to 300 F               4--8 hours
Phase 6: AIR COOL      300 F to ambient                  1--2 hours
```

Total cycle: `33--87 hours (1.4--3.6 days)` -- Inter Medium, 16 pt, `#27AE60`

Description (Inter Regular, 14 pt, `#F0EDE8`):
```
Stage 2 raises temp and dissociation to control white layer. Total time is similar
to single-stage (Stage 2 time offsets shorter Stage 1). Case depth is equivalent.
```

---

### ZONE 3 -- Temperature by Steel Grade

**Dimensions:** Y: 14.0" to 20.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 14.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `NITRIDING TEMPERATURE & HARDNESS BY STEEL GRADE`

---

**BLOCK C -- Steel Grade Table**

Y: 14.9" to 20.3". Column widths (23.0" total):
- Steel Grade (4.0") | Nitriding Temp (4.0") | Surface Hardness (HV) (4.0") | Surface Hardness (HRC eq.) (3.5") | Key Alloying Elements (7.5")

Header row: `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.65".

| Steel | Temp | HV | HRC eq. | Key Elements |
|---|---|---|---|---|
| Nitralloy 135M | 975 F (524 C) | 950--1100 | 68--70 | 1% Al + Cr + Mo (highest response) |
| Nitralloy EZ | 975 F (524 C) | 900--1050 | 67--69 | Free-machining Nitralloy |
| H13 | 975 F (524 C) | 900--1100 | 67--70 | 5% Cr (excellent nitriding response) |
| H11 | 975 F (524 C) | 850--1050 | 66--69 | 5% Cr + Mo + V |
| D2 | 950 F (510 C) | 800--1000 | 64--68 | 12% Cr (activate surface first) |
| 4140 | 975 F (524 C) | 500--650 | 50--57 | Cr + Mo (moderate response) |
| 4340 | 975 F (524 C) | 500--650 | 50--57 | Ni + Cr + Mo |
| D6AC | 950 F (510 C) | 600--800 | 56--64 | Aerospace structural steel |
| 38CrMoAl (EN) | 975 F (524 C) | 950--1100 | 68--70 | European Nitralloy equivalent |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Grade names: Inter Medium, 12 pt.

Note below table:
- Inter Medium, 13 pt, `#E8A020`
- Text: `Plain carbon steels (1018, 1045) develop only iron nitride -- 350--450 HV -- and are NOT normally gas nitrided. Nitriding-grade steels contain Al, Cr, Mo, V, or W for hard alloy nitride formation.`

---

### ZONE 4 -- Ramp Rate & Cooling

**Dimensions:** Y: 20.5" to 27.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 20.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `HEATING, COOLING & CYCLE TIMELINE`

---

**BLOCK D -- Two Panels**

**Left -- Ramp Rate (X: 0.5", W: 11.0"):**
- Rounded rect, Y: 21.4", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `HEATING RATE` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Ramp rate: 100--200 F/hr (56--111 C/hr)

SLOW ramp is deliberate:
  - Ensures uniform part temperature
  - Large parts have significant
    thermal mass -- surface heats
    faster than core
  - Thermal gradients cause distortion
    (defeating nitriding's zero-distortion
    advantage)
  - Heavy loads need slower ramp

Time to reach 975 F from ambient:
  Light load: 2--3 hours
  Heavy load: 4--6 hours

N2 purge BEFORE introducing NH3
```

**Right -- Cooling Procedure (X: 12.5", W: 11.0"):**
- Rounded rect, Y: 21.4", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#2EC4B6`
- Title: `COOLING -- NO QUENCH` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
FURNACE COOL under ammonia atmosphere
from nitriding temperature to 300 F (149 C).

Then open furnace and AIR COOL to ambient.

Why cool under ammonia?
  - Prevents oxidation during cooling
  - Parts remain bright and clean
  - Compound zone is not disturbed

Why NOT quench?
  - No phase transformation to capture
  - Hardness is from nitride precipitates
    (already formed during the hold)
  - Quenching would cause thermal shock
    with zero hardening benefit

Cooling time: 4--8 hours furnace cool
              + 1--2 hours air cool
```

---

### ZONE 5 -- What Happens at Temperature

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `WHAT HAPPENS DURING THE HOLD -- NITRIDE PRECIPITATION`

---

**BLOCK E -- Mechanistic Panel**

Y: 27.9" to 32.3". Full-width panel.

- Rounded rect, X: 0.5", W: 23.0", H: 4.2", fill `#1E2435`, radius 8

Two columns inside:

Left (X: 1.0", W: 10.5"):
- Title: `THE MECHANISM` -- Barlow SemiBold, 20 pt, `#27AE60`
- Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
1. NH3 dissociates on the steel surface:
   2NH3 -> 2N(adsorbed) + 3H2

2. Nascent nitrogen diffuses into the
   ferrite lattice (interstitial diffusion)

3. Nitrogen reacts with alloying elements
   (Al, Cr, Mo, V, W) to form nitrides

4. Fine, coherent nitride precipitates
   create extreme hardness

5. At the very surface: iron nitride
   compound zone (white layer) forms
   -- epsilon (Fe2-3N) and/or
   gamma-prime (Fe4N)
```

Right (X: 12.5", W: 10.5"):
- Title: `WHY IT WORKS WITHOUT A QUENCH` -- Barlow SemiBold, 20 pt, `#E8A020`
- Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
In carburizing, carbon dissolves in austenite
and only becomes hard when quenched to
martensite. Without the quench, it is soft.

In nitriding, nitrogen forms PRECIPITATES
inside the ferrite. The precipitates ARE
the hardening mechanism. They exist at
temperature and remain on cooling.

No transformation needed.
No quench needed.
No distortion from quench.

This is precipitation hardening, not
transformation hardening.

That is the fundamental difference.
```

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Heat cycle parameters shown are typical for gas nitriding per AMS 2759/6D and AMS 2759/10A. Actual cycle times, temperatures, and ramp rates depend on steel grade, part geometry, load size, and specification requirements. Consult your process engineer.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"
> Gas Nitriding -- Heat Cycle

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"
> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"
> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Cycle Profiles | Section label, single-stage and two-stage profile panels |
| Zone 3 - Steel Grade Table | Section label, temperature and hardness by grade |
| Zone 4 - Ramp & Cool | Section label, heating rate and cooling panels |
| Zone 5 - Mechanism | Section label, nitride precipitation explanation |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap per Poster #586.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Heat Cycle -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Heat Cycle -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Heat Cycle -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Heat Cycle -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Heat Cycle -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Heat Cycle -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The mechanistic explanation panel ("Why It Works Without a Quench") is the intellectual core of this poster. Most operators who have worked in carburizing or induction hardening instinctively associate "hard surface" with "quench." Nitriding breaks that mental model. The explanation must be clear, memorable, and technically precise.

The steel grade table will be heavily referenced -- operators checking "what hardness will I get on this steel?" Give it clean typography and enough row height for comfortable reading at 6 feet.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #592 -- Construction Workup v1.0*
*2026-04-26*
