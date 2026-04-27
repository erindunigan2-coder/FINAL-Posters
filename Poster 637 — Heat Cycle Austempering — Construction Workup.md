---
Project: Plating Posters Inc
Poster Number: 637
Title: "Heat Cycle -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Section 9.7)"
Process Scope: Austenitizing cycle parameters, hold times, section size limitations, and the critical relationship between hardenability and process feasibility
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - HeatCycle
  - Austenitizing
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #637 -- Construction Workup
## Heat Cycle -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The heat cycle in austempering has two phases: austenitizing (getting the steel fully into the austenite phase) and isothermal holding (transforming that austenite to bainite in the salt bath). This poster focuses on the austenitizing side -- temperature selection, hold times by material type, and the section-size limitation that defines whether austempering is even possible for a given part. The isothermal hold gets its own poster (#638).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Austenitizing parameter hero (Block B):** Steel vs. ADI austenitizing requirements side by side.
2. **Section size limitation table (Block C):** Max section by steel grade -- the hard limit.
3. **TTT timing diagram concept (Block D):** Why the cooling rate through the pearlite nose determines feasibility.
4. **Cycle sequence timeline (Block E):** Visual timeline of the complete thermal cycle.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 20.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- AUSTENITIZING PARAMETERS HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- SECTION SIZE LIMITATIONS (13.5"--20.5" / ~7.0")
ZONE 5 -- TTT TIMING CONCEPT (20.5"--27.5" / ~7.0")
ZONE 6 -- COMPLETE CYCLE TIMELINE (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HEAT CYCLE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Austenitizing Parameters & Section Limits` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Full austenitization is non-negotiable. Incomplete = mixed structures = unpredictable properties.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 of 9 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Austenitizing cycle: temperature, hold time, and the section-size question that gates the entire process`

---

### ZONE 3 -- Austenitizing Parameters Hero

**Section label:** `AUSTENITIZING PARAMETERS -- STEEL vs. ADI` -- Y: 4.4".

**BLOCK B -- Side-by-Side Parameter Panels**

Y: 5.0" to 13.0".

**Left -- Steel Austempering (X: 0.5", W: 11.0"):**

Rounded rect, H: 7.5", fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `STEEL` -- Barlow Condensed ExtraBold, 24 pt, `#E8A020`
Subtitle: `Carbon and Alloy Steels` -- Inter Regular, 14 pt, `#F0EDE8` at 50%

Parameters (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Austenitizing temp:  1525--1600 F (829--871 C)
Hold time:           30--90 minutes
                     (depends on section size)
Atmosphere:          Endothermic gas or N2
                     (protect from decarburization)
Ac3 reference:       Must exceed Ac3 by 50--100 F
                     for complete austenitization
```

Property callout box (fill `#E8A020` at 10%, border 1 pt `#E8A020`):
```
Common grades:
  1065-1095  -- 1475-1550 F
  4150/4340  -- 1525-1575 F
  5160/6150  -- 1500-1575 F
  52100      -- 1525-1575 F
```
JetBrains Mono Regular, 12 pt, `#F0EDE8`.

**Right -- ADI (Austempered Ductile Iron) (X: 12.0", W: 11.5"):**

Rounded rect, H: 7.5", fill `#1E2435`, left accent `#27AE60`, radius 6.

Title: `DUCTILE IRON (ADI)` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
Subtitle: `Austempered Ductile Iron per ASTM A897` -- Inter Regular, 14 pt, `#F0EDE8` at 50%

Parameters (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Austenitizing temp:  1550--1650 F (843--899 C)
Hold time:           60--120 minutes
                     (longer -- carbon must dissolve
                      from graphite nodules)
Atmosphere:          Not critical (iron is in
                     a salt bath or controlled
                     atmosphere)
Nodularity:          Min 80% per ASTM A897
```

Property callout box (fill `#27AE60` at 10%, border 1 pt `#27AE60`):
```
ADI austenitize temp affects:
  Higher temp = more carbon in austenite
              = more retained austenite in ADI
              = higher ductility, lower hardness
  Lower temp  = less carbon in austenite
              = more complete transformation
              = higher hardness
```
JetBrains Mono Regular, 12 pt, `#F0EDE8`.

**Key insight callout (Y: 12.8"):**
- Rounded rect, full width, H: 0.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `ADI holds longer because carbon must dissolve from graphite nodules into the austenite matrix. Steel dissolves carbon from carbides faster.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 4 -- Section Size Limitations

**Section label:** `SECTION SIZE -- THE HARD LIMIT OF AUSTEMPERING` -- Y: 13.7".

**BLOCK C -- Max Section Table**

Y: 14.3" to 20.3". Column widths (23.0" total):
- Steel Type (5.5") | Representative Grades (5.5") | Max Section (4.0") | Limiting Factor (8.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Steel Type | Grades | Max Section | Limiting Factor |
|---|---|---|---|
| Plain carbon (high C) | 1065, 1075, 1095 | ~0.200" (5 mm) | Low hardenability -- core hits pearlite nose on TTT |
| Alloy spring steels | 5160, 6150 | 0.5" (12.7 mm) | Moderate hardenability; good for wire and strip |
| Medium-carbon alloy | 4150, 4340, 8640 | 1.0--1.5" (25--38 mm) | High hardenability; larger sections viable |
| High-alloy bearing | 52100 | 0.5--0.75" (12--19 mm) | Hardenability limits; carbide-free bainite target |
| Ductile iron (ADI) | Per ASTM A897 | 3--4" (76--102 mm) | With Cu, Ni, Mo additions for hardenability |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Steel type: Inter Medium, 13 pt.

**Warning callout below table:**
- Rounded rect, full width, H: 0.7", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `If the part core cannot cool fast enough to avoid the pearlite nose, austempering WILL NOT WORK. No amount of salt bath optimization can fix insufficient hardenability. Select a higher-alloy steel or use conventional Q&T.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 5 -- TTT Timing Concept

**Section label:** `THE TTT DIAGRAM -- WHY SECTION SIZE MATTERS` -- Y: 20.7".

**BLOCK D -- TTT Concept Diagram**

Y: 21.3" to 27.3". Conceptual diagram built with rectangles and lines.

Vertical axis: `TEMPERATURE` (Barlow SemiBold, 14 pt, vertical)
Horizontal axis: `TIME (log scale)` (Barlow SemiBold, 14 pt)

Key regions:
- Top zone: `AUSTENITE REGION (above Ac3)` -- `#E8A020`, dashed boundary
- C-curve nose: `PEARLITE NOSE -- DO NOT ENTER` -- `#E05C5C`, bold, filled region indicator
- Middle zone: `BAINITE BAY (400--750 F)` -- `#27AE60`, shaded region
- Bottom line: `Ms (Martensite Start)` -- `#E8A020`, dashed horizontal

Three cooling curves (dashed):
- **Curve 1 -- Thin section / high alloy:** Steep curve from austenite region, passes LEFT of pearlite nose, enters bainite bay. Label: `THIN / HIGH HARDENABILITY -- clears pearlite nose` -- `#27AE60`
- **Curve 2 -- Marginal section:** Curve grazes the pearlite nose. Label: `BORDERLINE -- mixed pearlite + bainite` -- `#E8A020`
- **Curve 3 -- Thick section / low alloy:** Curve passes through pearlite nose. Label: `TOO THICK / LOW HARDENABILITY -- pearlite = FAIL` -- `#E05C5C`

Annotation in bainite bay:
- `Isothermal hold at salt bath temperature. Transformation to bainite occurs here over 30--120 min.` -- Inter Regular, 12 pt, `#27AE60`

Bottom note:
- `Alloy additions (Mn, Cr, Mo, Ni) shift the pearlite nose to the RIGHT (longer time), giving thicker sections a larger window to clear the nose.` -- Inter Medium, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Complete Cycle Timeline

**Section label:** `COMPLETE AUSTEMPERING THERMAL CYCLE` -- Y: 27.7".

**BLOCK E -- Timeline Strip**

Y: 28.3" to 32.3". Horizontal timeline built with colored segments.

Full width (23.0"). Each segment is a rounded rectangle, H: 1.5", with time duration and temperature.

| Segment | Width | Color | Label | Parameters |
|---|---|---|---|---|
| 1. Heat to austenitize | 4.5" | `#E8A020` | HEAT-UP | Ramp to 1525--1600 F; 30--60 min |
| 2. Austenitize hold | 5.0" | `#E8A020` | AUSTENITIZE | Hold 30--90 min at temp |
| 3. Transfer | 1.0" | `#E05C5C` | TRANSFER | < 15 sec -- CRITICAL |
| 4. Isothermal hold | 7.0" | `#27AE60` | SALT BATH HOLD | 400--750 F; 30--120 min |
| 5. Air cool + wash | 5.5" | `#2EC4B6` | AIR COOL / WASH | To room temp; wash salt |

Arrows between segments: 2 pt `#3A4055`, right-pointing.

Segment labels: Barlow SemiBold, 14 pt, `#1A1F2E` on colored fill.
Parameters: JetBrains Mono Regular, 11 pt, below each segment.

Below timeline:
- `Total cycle: 2--5 hours (depending on section size and austenitizing time). NO TEMPER STEP -- bainite is the final structure.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Heat Cycle -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897. Austenitizing temperatures and hold times vary by steel grade and section size. Consult TTT diagrams for your specific material.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Heat Cycle Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The section-size table is the practical gatekeeper -- operators need to know at a glance whether their part is even a candidate. The TTT concept diagram returns from Poster 633 but with more detail and three cooling curves instead of two, reinforcing the hardenability lesson. The timeline strip at the bottom puts the complete thermal journey on one visual line -- austenitize (amber), transfer (coral flash), isothermal hold (emerald), cool (teal). The "no temper" callout at the end is the punchline that makes austempering special.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #637 -- Construction Workup v1.0*
*2026-04-26*
