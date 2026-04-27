---
Project: Plating Posters Inc
Poster Number: 627
Title: "Heating Cycle -- Flame Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8, Section 8.6)"
Technical Source: Flame hardening heating cycle parameters -- surface temperature targets, flame-to-part distance, traverse speed, rotation speed, case depth control methods, and the operator-skill component. Case depth is controlled by time/distance/intensity rather than frequency (as in induction).
Process Scope: Flame hardening -- heating cycle
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FlameHardening
  - HeatingCycle
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #627 -- Construction Workup
## Heating Cycle -- Flame Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The heating cycle in flame hardening is controlled by three variables: flame intensity, distance, and speed. There is no frequency dial (like induction), no carbon potential probe (like carburizing), and no digital temperature readout on most setups. The operator reads cherry red -- color temperature judgment honed by experience. This poster quantifies what experienced operators do by feel, making it teachable.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Case depth control triangle (Block B -- HERO):** Visual showing the three control variables (intensity, distance, speed) and their effects.
2. **Heating method comparison (Block D):** Spot, progressive, spin, and combination methods.
3. **Color temperature guide (Block E):** What cherry red, bright orange, and yellow mean in degrees.
4. **Case depth tolerance callout (Block F):** Realistic expectations for flame vs. induction.

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
  Stage 6 highlighted (Amber)
ZONE 3 -- CASE DEPTH CONTROL / HERO (4.2"--14.5" / ~10.3")
  Block B: Three-variable control diagram
  Block C: Parameter table
ZONE 4 -- HEATING METHODS (14.5"--22.0" / ~7.5")
  Block D: Four methods with parameters
ZONE 5 -- COLOR TEMPERATURE + TOLERANCE (22.0"--32.5" / ~10.5")
  Block E: Color temperature guide
  Block F: Case depth tolerance callout
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEATING CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flame Hardening -- Stage 6 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `No frequency dial. No digital readout. Three variables: flame intensity, distance, and speed. The operator reads cherry red.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Equipment set, flame adjusted  -->  After: Surface at 1500--1650 F, austenitized, ready for quench`

---

### ZONE 3 -- Case Depth Control (HERO)

**Section label:** `THREE VARIABLES CONTROL CASE DEPTH` -- Y: 4.4".

**BLOCK B -- Three-Variable Control Diagram**

Y: 5.0" to 10.5". Full-width panel.

- Rounded rect W: 23.0", H: 5.0", fill `#1E2435`, radius 8

Three side-by-side variable panels:

| Variable | X | W | Accent | Effect |
|---|---|---|---|---|
| FLAME INTENSITY | 0.8" | 7.0" | `#E8A020` | Controlled by tip size and gas pressure. Higher intensity = more BTU/hr = faster surface heating = shallower case (less time for heat to conduct inward). |
| DISTANCE | 8.3" | 7.0" | `#2EC4B6` | Flame-to-part gap: 0.25--0.75 in. Closer = more intense, narrower heating. Farther = gentler, wider zone. |
| SPEED | 15.8" | 7.0" | `#27AE60` | Traverse rate: 2--12 in/min (progressive). Rotation: 30--120 RPM (spin). Slower = deeper case. Faster = shallower case. |

Each panel: Rounded rect, fill `#252B3D`, top accent 3 pt.
Variable name: Barlow SemiBold 18 pt, accent color.
Effect: Inter Regular 13 pt `#F0EDE8`.

Below panels -- key insight:
- Rounded rect W: 21.5", H: 1.0", fill `#1E2435`, left accent 0.06" `#E8A020`
- Text: `Unlike induction (where frequency is the primary depth control), flame hardening has NO frequency variable. Case depth is controlled entirely by how much heat reaches the surface and how long it stays before quench.` Inter Medium 14 pt `#E8A020`

**BLOCK C -- Parameter Table**

Y: 11.0" to 14.3".

| Parameter | Value | Effect on Case Depth |
|---|---|---|
| Surface temp target | 1500--1650 F (816--899 C) | Must exceed Ac3 of the steel |
| Flame-to-part distance | 0.25--0.75 in (6--19 mm) | Closer = more intense |
| Traverse speed (progressive) | 2--12 in/min (50--300 mm/min) | Slower = deeper case |
| Rotation speed (spin) | 30--120 RPM | Slower = deeper (more dwell per revolution) |
| Heat time (spot) | 10--60 seconds per area | Longer = deeper |
| Typical case depth | 0.050--0.250 in (1.3--6.4 mm) | Deeper than typical induction |
| Case depth tolerance | +/- 0.030 in (0.76 mm) | Less precise than induction (+/- 0.010 in) |

Header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 0.4".
Data: JetBrains Mono Regular 11 pt `#F0EDE8`.

---

### ZONE 4 -- Heating Methods

**Section label:** `FOUR HEATING METHODS` -- Y: 14.7".

**BLOCK D -- Four Method Cards**

Y: 15.3" to 21.8". Four cards, two rows of two.

Each card: Rounded rect W: 11.0", H: 3.0", fill `#1E2435`, radius 6, left accent 0.06".

| Pos | Method | Accent | Parameters | Best For |
|---|---|---|---|---|
| TL | SPOT (STATIONARY) | `#E8A020` | Flame and part both stationary; dwell 10--60 sec; small area per application | Localized hardening; small wear pads; bearing seats; repair |
| TR | PROGRESSIVE (SCANNING) | `#2EC4B6` | Flame traverses along part at 2--12 in/min; quench spray follows; most common production method | Long surfaces: ways, rails, shafts; most repeatable |
| BL | SPIN | `#27AE60` | Part rotates 30--120 RPM under stationary flame head; for cylindrical parts | Journals, bushings, rolls; good circumferential uniformity |
| BR | COMBINATION | `#E8A020` | Part rotates AND flame traverses simultaneously | Long cylindrical parts requiring both circumferential and axial coverage |

Card interior:
- Method: Barlow SemiBold 18 pt, accent color
- Parameters: JetBrains Mono Regular 12 pt `#F0EDE8`
- Best for: Inter Medium 13 pt, accent color

---

### ZONE 5 -- Color Temperature + Tolerance

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Color Temperature Guide (X: 0.5", W: 11.0"):**

Section label: `COLOR TEMPERATURE -- READING THE HEAT` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`

Content:
```
STEEL COLOR vs. TEMPERATURE:

  Black heat          below 900 F (480 C)
  Faint red           900--1000 F (480--540 C)
  Dark red            1000--1200 F (540--650 C)
  Cherry red          1200--1400 F (650--760 C)
  Bright cherry       1400--1500 F (760--816 C)
  Dark orange         1500--1600 F (816--871 C)
  Bright orange       1600--1700 F (871--927 C)
  Yellow              1700--1900 F (927--1038 C)
  Light yellow/white  1900+ F (1038+ C)

TARGET FOR FLAME HARDENING:
  Cherry red to bright orange
  = 1400--1700 F (760--927 C)

  For medium-carbon steels:
  Ac3 is approximately 1400--1500 F
  (depends on carbon content and alloy)

CAUTION: Color judgment requires consistent
lighting. Ambient light washes out low colors.
Shade the work area or use IR pyrometer
for verification.
```

Data: JetBrains Mono Regular 12 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Case Depth Tolerance (X: 12.0", W: 11.5"):**

Section label: `REALISTIC EXPECTATIONS` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`

Content:
```
FLAME HARDENING CASE DEPTH TOLERANCE:

  Manual:    +/- 0.030--0.060 in (0.8--1.5 mm)
  Automated: +/- 0.020--0.030 in (0.5--0.8 mm)

  vs. INDUCTION:
  +/- 0.005--0.010 in (0.13--0.25 mm)

WHAT THIS MEANS:
If the print calls for 0.100 in case depth:
  Flame (manual): expect 0.040--0.160 in
  Flame (auto):   expect 0.070--0.130 in
  Induction:      expect 0.090--0.110 in

WHY THE WIDER TOLERANCE?
  - No skin effect (like induction) to limit
    depth intrinsically
  - Flame is broader and less focused
  - Operator variation in manual work
  - Traverse speed variation

IF TOLERANCE IS TIGHT:
  - Use automated traverse (CNC)
  - Verify with pyrometer
  - Run test coupons before production
  - Consider induction if tolerance
    is < +/- 0.020 in
```

Data: JetBrains Mono Regular 13 pt `#2EC4B6`. Body: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Heating Cycle -- Flame Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Heating parameters are application-specific. Color temperature is an approximate visual guide only -- use pyrometry for critical work. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heating Cycle Flame Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The color temperature guide is the most operator-relevant content on this poster. Experienced flame hardening operators work by color -- they know what cherry red looks like and how to maintain it. But this knowledge is rarely documented and difficult to transfer. Putting actual temperatures next to color descriptions makes the skill teachable. The tolerance comparison with induction is honest and practical: flame hardening is less precise, and the poster says so without apology.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #627 -- Construction Workup v1.0*
*2026-04-26*
