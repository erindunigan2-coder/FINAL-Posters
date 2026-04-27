---
Project: Plating Posters Inc
Poster Number: 618
Title: "Heating Cycle -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.6)"
Technical Source: Induction hardening heating cycle parameters -- power density, heating time, surface temperature, scan rate, and the relationship between these variables and the resulting case depth. Single-shot vs. progressive scan heating patterns.
Process Scope: Induction hardening -- heating cycle
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - HeatingCycle
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #618 -- Construction Workup
## Heating Cycle -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The heating cycle is where seconds count -- literally. Unlike furnace processes where parts soak for hours, induction heating happens in 1 to 30 seconds. Power density, not time, is the primary variable. This poster makes that paradigm shift visual: a furnace operator thinks in hours; an induction operator thinks in kilowatts per square inch and fractions of a second.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Power density vs. case depth diagram (Block B -- HERO):** Visual showing the inverse relationship between power density and case depth for a given frequency.
2. **Heating parameter table (Block D):** Key cycle parameters for single-shot and progressive scan methods.
3. **Temperature monitoring callout (Block E):** Pyrometry methods and importance of real-time temperature feedback.
4. **Overheating warning strip (Block F):** Consequences of exceeding critical temperature thresholds.

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
ZONE 3 -- POWER DENSITY & HEATING / HERO (4.2"--14.5" / ~10.3")
  Block B: Power density vs. case depth relationship
  Block C: Single-shot vs. progressive scan comparison
ZONE 4 -- HEATING PARAMETER TABLE (14.5"--22.0" / ~7.5")
  Block D: Comprehensive parameter reference
ZONE 5 -- TEMPERATURE MONITORING + OVERHEATING WARNING (22.0"--32.5" / ~10.5")
  Block E: Pyrometry and temperature feedback
  Block F: Overheating consequences strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEATING CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 6 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Seconds, not hours. Power density is your primary control variable -- the part surface reaches austenitizing temperature in the blink of an eye.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coil positioned, recipe loaded  -->  After: Surface austenitized, ready for quench`

---

### ZONE 3 -- Power Density & Heating (HERO)

**Section label:** `POWER DENSITY -- THE PRIMARY CONTROL VARIABLE` -- Y: 4.4".

**BLOCK B -- Power Density vs. Case Depth**

Y: 5.0" to 11.0". Full-width panel.

- Rounded rect W: 23.0", H: 5.5", fill `#1E2435`, radius 8

**Left side (X: 0.8", W: 11.0") -- Visual relationship:**

Four horizontal bars showing the inverse relationship:

| Power Density | Case Depth | Heating Time | Fill |
|---|---|---|---|
| 50 kW/in2 (very high) | 0.015--0.030 in (shallow) | 0.5--2 sec | `#E8A020` at 80% |
| 20 kW/in2 (high) | 0.030--0.060 in (medium) | 2--5 sec | `#E8A020` at 60% |
| 10 kW/in2 (moderate) | 0.060--0.120 in (deep) | 5--15 sec | `#E8A020` at 40% |
| 1--5 kW/in2 (low) | 0.120--0.300 in (very deep) | 15--30 sec | `#E8A020` at 20% |

Each bar: Rounded rect H: 1.0", fill as specified. Labels: JetBrains Mono Regular 13 pt `#F0EDE8`.

**Right side (X: 12.5", W: 10.0") -- Key principles:**

Callout box, fill `#1E2435`, left accent 0.06" `#E8A020`.

```
THE POWER-DEPTH TRADEOFF:

High power density + short time
= SHALLOW case (surface only)

Low power density + longer time
= DEEPER case (heat soaks inward)

At any given frequency, you control
case depth by adjusting the ratio
of power to time.

SURFACE TEMPERATURE TARGET:
1500--1700 F (816--927 C)
Must exceed Ac3 of the steel.
```

Data: JetBrains Mono Regular 14 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

**BLOCK C -- Single-Shot vs. Progressive Scan**

Y: 11.3" to 14.3". Two side-by-side comparison panels.

| Method | X | W | Accent | Parameters | Best For |
|---|---|---|---|---|---|
| SINGLE-SHOT (STATIC) | 0.5" | 11.0" | `#E8A020` | Power: high (entire area simultaneously); Time: 1--10 sec; No coil or part movement during heating; Quench follows immediately | Localized hardening: gear teeth, bearing seats, cam lobes, splined sections; Highest production rate |
| PROGRESSIVE SCAN | 12.0" | 11.5" | `#2EC4B6` | Scan rate: 0.1--2.0 in/sec; Power: lower (only heating narrow band); Trailing spray quench follows coil; Part may rotate simultaneously | Long uniform surfaces: shafts, rods, rolls, bars; Lower instantaneous power requirement |

Each: Rounded rect H: 2.8", fill `#1E2435`, left accent 0.06".

Method name: Barlow SemiBold 18 pt, accent color. Parameters: JetBrains Mono Regular 12 pt `#F0EDE8`. Best for: Inter Medium 13 pt, accent color.

---

### ZONE 4 -- Heating Parameter Table

**Section label:** `HEATING CYCLE PARAMETERS -- QUICK REFERENCE` -- Y: 14.7".

**BLOCK D -- Parameter Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Parameter (5.0") | Single-Shot Value (5.5") | Progressive Scan Value (5.5") | Key Control (7.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Parameter | Single-Shot | Progressive Scan | Key Control |
|---|---|---|---|
| Surface temperature | 1500--1700 F (816--927 C) | 1500--1700 F (816--927 C) | Must exceed Ac3 of the steel |
| Power density | 1--50 kW/in2 | 5--20 kW/in2 | Higher = shallower; lower = deeper |
| Heating time | 1--30 sec | N/A (continuous) | Shorter = shallower case |
| Scan rate | N/A | 0.1--2.0 in/sec | Slower = deeper case |
| Quench delay | 0.1--2.0 sec | 0 (trailing spray) | Minimize -- heat soak to core |
| Part rotation | 60--300 RPM (if applicable) | 60--300 RPM (typical) | Uniformity around circumference |
| Coil coupling gap | 0.060--0.125 in | 0.060--0.125 in | Tighter = more efficient |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Parameter names: Inter Medium 13 pt.

---

### ZONE 5 -- Temperature Monitoring + Overheating Warning

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Temperature Monitoring (X: 0.5", W: 11.0"):**

Section label: `TEMPERATURE MONITORING` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
METHODS:

Infrared pyrometer (non-contact)
  - Aimed at part surface during heating
  - Emissivity setting critical (0.85--0.95
    for oxidized steel)
  - Response time: < 10 ms required

Dual-color (ratio) pyrometer
  - Less sensitive to emissivity variation
  - Preferred for induction applications

Thermocouple (contact)
  - Not practical during induction heating
    (EMF interference)
  - Used for first-article setup only

WHY IT MATTERS:
Temperature variation of +/- 50 F directly
affects case depth and hardness. Real-time
pyrometry enables closed-loop power control
on modern systems.
```

Data: JetBrains Mono Regular 13 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Overheating Warning (X: 12.0", W: 11.5"):**

Section label: `OVERHEATING -- CONSEQUENCES` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`

Warning content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
GRAIN GROWTH
Excessive temperature or time causes austenite
grain coarsening. Coarse-grained martensite is
BRITTLE and crack-prone.

INCIPIENT MELTING
Surface temperatures above 2500 F (1370 C) can
cause localized melting at grain boundaries --
especially at sharp corners and thin edges where
current concentrates.

THROUGH-HARDENING
If heat soaks too deep (time too long, power
too low, frequency too low for the section),
the entire cross-section austenitizes. Result:
martensite throughout = no tough core = brittle
part that shatters under load.

DISTORTION
Overheating causes excessive thermal expansion
followed by severe contraction during quench.
Result: OD growth, bowing, or cracking.
```

Bottom highlight: `Monitor surface temperature with pyrometry on EVERY production run. A 100 F overshoot can mean the difference between a good part and scrap.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Footer

Standard footer. Title: `Heating Cycle -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Heating cycle parameters are highly application-specific. Values shown are typical industry ranges for medium-carbon steels. Consult your equipment manufacturer and process engineer for specific recipes. Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2759/12.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heating Cycle Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The power density relationship is the conceptual shift this poster needs to communicate. Furnace operators think in time and temperature. Induction operators think in kilowatts per square inch and seconds. The four-bar visual makes this intuitive: high power = shallow and fast; low power = deep and slower. The temperature monitoring section is increasingly important as modern systems add closed-loop pyrometry -- this is where induction is heading.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #618 -- Construction Workup v1.0*
*2026-04-26*
