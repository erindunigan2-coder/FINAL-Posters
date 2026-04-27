---
Project: Plating Posters Inc
Poster Number: 591
Title: "Gas Nitriding -- Atmosphere / Cycle Control"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.6)"
Technical Source: Atmosphere and cycle control for gas nitriding. Covers single-stage vs. two-stage (Floe) process, nitriding potential (KN) control per AMS 2759/10A, ammonia dissociation monitoring, and white layer class specifications.
Process Scope: Gas nitriding -- atmosphere and cycle control (Stage 6 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - AtmosphereControl
  - NitridingPotential
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #591 -- Construction Workup
## Gas Nitriding -- Atmosphere / Cycle Control

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the two fundamental control methods for gas nitriding: dissociation-based control (AMS 2759/6D) and nitriding potential (KN) control (AMS 2759/10A). The single-stage vs. two-stage (Floe) process comparison is the centerpiece -- understanding when and why to use two stages is the key to white layer control.

Design philosophy: hero panel comparing single-stage vs. two-stage processes side by side, a nitriding potential (KN) reference table with white layer class specifications, ammonia dissociation monitoring methods, and a case depth vs. time reference table.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Single-stage vs. two-stage comparison (Block B -- HERO):** Two large side-by-side panels.
2. **KN and white layer class table (Block C).**
3. **Dissociation monitoring methods (Block D).**
4. **Case depth vs. time table (Block E).**
5. **4 pt left-border accents. Global color remap. JetBrains Mono. Print size 24x36".**

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, and descriptions
- **JetBrains Mono Regular** -- all parameter data, formulas, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette
Same as Poster #586 (series standard).

### Step 5 -- Set ruler guides

**Vertical guides:** 0.5" left, 23.5" right.

**Horizontal guides:**
- 0.5" -- top safe zone
- 2.9" -- Zone 1/Zone 2 boundary
- 15.5" -- Zone 2/Zone 3 boundary
- 22.0" -- Zone 3/Zone 4 boundary
- 27.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SINGLE-STAGE VS. TWO-STAGE / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Side-by-side comparison of control methods

ZONE 3 -- NITRIDING POTENTIAL & WHITE LAYER CLASSES (15.5"--22.0" / ~6.5" tall)
  Block C: KN values and AMS 2759/10 white layer class table

ZONE 4 -- DISSOCIATION MONITORING (22.0"--27.5" / ~5.5" tall)
  Block D: Monitoring methods and instrumentation

ZONE 5 -- CASE DEPTH VS. TIME (27.5"--32.5" / ~5.0" tall)
  Block E: Case depth reference table

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Position: X: 0.5". Y: 0.5". Width: 23.0"
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `GAS NITRIDING`

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5". Width: 23.0"
- Font: Barlow SemiBold, 36 pt, `#27AE60` (Emerald)
- Text: `Atmosphere / Cycle Control -- Dissociation, KN Potential & White Layer`

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2". Width: 23.0"
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Two control philosophies: ammonia dissociation rate (AMS 2759/6D) or nitriding potential KN (AMS 2759/10A). The choice determines your white layer.`

---

### ZONE 2 -- Single-Stage vs. Two-Stage (HERO)

**Dimensions:** Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `SINGLE-STAGE VS. TWO-STAGE (FLOE) PROCESS`

---

**BLOCK B -- Side-by-Side Comparison**

Y: 3.8" to 15.3".

**Left -- Single-Stage Process (X: 0.5", W: 11.0"):**
- Rounded rect, H: 11.3", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `SINGLE-STAGE PROCESS` -- Barlow SemiBold, 24 pt, `#E8A020`
- Subtitle: `One Temperature, One Dissociation Rate` -- Inter Medium, 14 pt, `#E8A020` at 70%

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 165%):

Parameter block (JetBrains Mono, 14 pt, `#F0EDE8`):
```
Temperature:  925--975 F (496--524 C)
NH3 Dissoc:   15--30%
Time:         24--90 hours
White Layer:  0.0005--0.001 in
              (12.7--25 micrometers)
```

Description (Inter Regular, 14 pt):
```
The entire cycle runs at one temperature
and one dissociation rate.

Advantages:
  - Simple to operate
  - No mid-cycle changes
  - Straightforward recipe

Disadvantages:
  - Produces relatively thick white layer
  - Limited compound zone control
  - White layer may be too thick for
    some specifications (Class 0 or 1)

When to use:
  - White layer is acceptable or desired
  - Class 2 per AMS 2759/10
  - Non-aerospace applications
```

**Right -- Two-Stage (Floe) Process (X: 12.5", W: 11.0"):**
- Rounded rect, H: 11.3", fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `TWO-STAGE (FLOE) PROCESS` -- Barlow SemiBold, 24 pt, `#27AE60`
- Subtitle: `White Layer Control by Staged Dissociation` -- Inter Medium, 14 pt, `#27AE60` at 70%

Parameter block -- Stage 1 (JetBrains Mono, 14 pt, `#F0EDE8`):
```
STAGE 1 -- Case Building
Temperature:  925--975 F (496--524 C)
NH3 Dissoc:   15--30%
Time:         15--40 hours
Purpose:      Build case depth
```

Parameter block -- Stage 2 (JetBrains Mono, 14 pt, `#F0EDE8`):
```
STAGE 2 -- White Layer Control
Temperature:  1000--1050 F (538--566 C)
NH3 Dissoc:   75--85%
Time:         10--30 hours
Purpose:      Limit compound zone growth
```

Description:
```
Stage 2 raises temperature and dissociation.
Higher dissociation = lower nitriding potential
at the surface = white layer stops growing
while diffusion zone continues to deepen.

When to use:
  - Aerospace specifications (AMS 2759/6)
  - White layer Class 0 or Class 1 required
  - Spalling/flaking risk must be minimized
```

Highlight box at bottom of right panel:
- Rounded rect, W: 10.0", H: 0.7", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Stage 2 is the key innovation -- it decouples case depth from white layer thickness` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 3 -- Nitriding Potential & White Layer Classes

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `NITRIDING POTENTIAL (KN) & WHITE LAYER CLASSES -- AMS 2759/10`

---

**BLOCK C -- Two Sub-Panels**

**Left -- KN Definition (X: 0.5", W: 11.0"):**
- Rounded rect, Y: 16.4", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `NITRIDING POTENTIAL (KN)` -- Barlow SemiBold, 20 pt, `#27AE60`

Content:
- Formula: `KN = P(NH3) / P(H2)^(3/2)` -- JetBrains Mono Regular, 20 pt, `#E8A020`
- Explanation (Inter Regular, 14 pt, `#F0EDE8`, line height 165%):
```
KN directly controls the nitrogen
activity at the steel surface.

Higher KN = more nitrogen at surface
           = faster compound zone growth

Lower KN  = less nitrogen at surface
           = compound zone reduced or absent

Automated KN control (AMS 2759/10) uses
H2 sensors and NH3 analyzers to calculate
and regulate KN in real time.
```

**Right -- White Layer Class Table (X: 12.5", W: 11.0"):**
- Rounded rect, Y: 16.4", H: 5.4", fill `#1E2435`, radius 8

Title: `WHITE LAYER CLASSES (AMS 2759/10)` -- Barlow SemiBold, 20 pt, `#F0EDE8`

| Class | White Layer Maximum | Stage 1 KN | Stage 2 KN |
|---|---|---|---|
| 0 | NO white layer permitted | 4--15 | 0.2--0.8 |
| 1 | 0.0005 in (12.7 um) max | 4--15 | 0.4--2.6 |
| 2 | 0.001 in (25 um) max | 4--15 | 1.2--5.5 |

Header: Barlow SemiBold, 13 pt, `#F0EDE8` on `#3A4055`.
Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`.

Note below table:
- Inter Medium, 13 pt, `#E8A020`
- Text: `Stage 1 KN is high (4--15) for all classes to build case depth. Stage 2 KN varies dramatically by class -- Class 0 drops to 0.2--0.8 to eliminate white layer entirely.`

---

### ZONE 4 -- Dissociation Monitoring

**Dimensions:** Y: 22.0" to 27.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `MONITORING & CONTROL METHODS`

---

**BLOCK D -- Three Monitoring Method Cards**

Y: 22.9" to 27.3". Three cards in a row. Gap: 0.35".

Each card: Rounded rect, W: 7.3", H: 4.2", fill `#1E2435`, radius 8, top accent 4 pt.

*Card 1 -- Burette (Volumetric) Method (X: 0.5"):*
- Top accent: `#2EC4B6`
- Title: `BURETTE METHOD` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Subtitle: `Traditional / Manual` -- Inter Medium, 12 pt, `#2EC4B6`

Content:
```
Sample exhaust gas over caustic solution
(KOH). NH3 is absorbed; H2 + N2 remain.

Volume reduction = % undissociated NH3
Remainder = % dissociation

Frequency: every 1--4 hours (manual)
Accuracy: +/-2--3% dissociation
Simple, reliable, low cost
Standard method per AMS 2759/6D
```

*Card 2 -- Hydrogen Sensor (X: 8.2"):*
- Top accent: `#E8A020`
- Title: `HYDROGEN SENSOR` -- Barlow SemiBold, 18 pt, `#E8A020`
- Subtitle: `Automated / Continuous` -- Inter Medium, 12 pt, `#E8A020`

Content:
```
Thermal conductivity sensor measures
H2 concentration in exhaust gas.

Combined with NH3 analyzer, calculates
KN = P(NH3) / P(H2)^(3/2) in real time.

Frequency: continuous (every few seconds)
Accuracy: +/-1% H2
Required for AMS 2759/10A (KN control)
Higher cost; calibration required
```

*Card 3 -- Ammonia Analyzer (X: 15.9"):*
- Top accent: `#E8A020`
- Title: `NH3 ANALYZER` -- Barlow SemiBold, 18 pt, `#E8A020`
- Subtitle: `For KN Calculation` -- Inter Medium, 12 pt, `#E8A020`

Content:
```
Infrared or electrochemical sensor
measures NH3 concentration in exhaust.

Paired with H2 sensor to calculate
nitriding potential (KN) per AMS 2759/10.

Frequency: continuous
Required for automated KN control

Modern systems integrate both sensors
with PLC for closed-loop KN regulation.
```

---

### ZONE 5 -- Case Depth vs. Time

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `CASE DEPTH VS. TIME -- REFERENCE TABLE (SINGLE-STAGE, 975 F)`

---

**BLOCK E -- Case Depth Table**

Y: 28.4" to 32.3". Column widths (23.0" total):
- Target Case Depth (in.) (5.0") | Target (mm) (3.5") | Approximate Time (7.5") | Notes (7.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Case Depth (in.) | (mm) | Time | Notes |
|---|---|---|---|
| 0.008--0.010 | 0.20--0.25 | 15--24 hours | Minimum practical gas nitriding case |
| 0.012--0.015 | 0.30--0.38 | 24--40 hours | Standard for many applications |
| 0.018--0.020 | 0.46--0.51 | 40--60 hours | Deep case; multi-day cycle |
| 0.025--0.030 | 0.64--0.76 | 60--90 hours | Maximum practical; 3--4 day cycle |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`.

Note below table:
- Inter Medium, 13 pt, `#F0EDE8` at 60%
- Text: `Times are approximate for single-stage at 975 F (524 C). Two-stage process adds 10--30 hours for Stage 2. Actual times depend on steel grade, nitriding potential, and equipment.`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Nitriding potential values and white layer classes are per AMS 2759/10A. Dissociation targets are per AMS 2759/6D. Actual cycle parameters depend on steel grade, case depth specification, and white layer requirements. Consult your process engineer and applicable standards.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Atmosphere / Cycle Control

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Stage Comparison | Section label, single-stage vs. two-stage panels |
| Zone 3 - KN & White Layer | Section label, KN definition, white layer class table |
| Zone 4 - Monitoring | Section label, three monitoring method cards |
| Zone 5 - Case Depth | Section label, case depth vs. time table |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Panel fills |
| `#252B3D` | `#E8E8F0` | Alternate rows |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Atmosphere Cycle Control -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Atmosphere Cycle Control -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Atmosphere Cycle Control -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Atmosphere Cycle Control -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Atmosphere Cycle Control -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Atmosphere Cycle Control -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The KN formula is the most important equation on this poster. Give it maximum visual prominence -- large type, Amber color, centered in its panel. The white layer class table is the second-most referenced data -- operators check it to verify they are targeting the correct class for their specification.

The single-stage vs. two-stage comparison is the pedagogical core. Most operators understand single-stage but are fuzzy on why Stage 2 works. The key insight: higher dissociation in Stage 2 REDUCES the nitrogen activity at the surface, so the white layer stops thickening while the diffusion zone keeps growing. Make this click.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #591 -- Construction Workup v1.0*
*2026-04-26*
