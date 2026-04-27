---
Project: Plating Posters Inc
Poster Number: 193
Title: "Aluminum Conversion Coating -- Rinse (Pre-Deoxidize)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.3)"
Technical Source: Rinse stage between alkaline cleaning and acid etch/deoxidize in Ti/Zr aluminum conversion coating lines. Covers water quality, conductivity targets, and the critical role of preventing alkaline drag-over into the acid deoxidizer.
Process Scope: Aluminum conversion coating -- Stage 2 rinse (pre-deoxidize)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - Rinse
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #193 -- Construction Workup
## Aluminum Conversion Coating -- Rinse (Pre-Deoxidize)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the first rinse poster for CC-06. In conversion coating, rinse stages are where most process failures originate -- not because rinsing is complicated, but because it is neglected. This poster makes the case that water quality and rinse discipline are make-or-break for ultra-thin Zr coatings.

The key message: every dissolved mineral, every microSiemen of conductivity, every pH point of alkaline drag-over is a contaminant that competes with the deoxidizer and the downstream Zr deposition. DI or RO water is not a luxury -- it is the standard.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Stage detail panel (Block B -- HERO):** Large callout showing rinse parameters, water quality targets, and drag-over prevention.
2. **Water quality comparison table (Block D):** Tap vs. softened vs. DI vs. RO water.
3. **Drag-over impact diagram (Block E):** Visual showing how alkaline drag-over neutralizes the deoxidizer.
4. **Troubleshooting strip (Block F).**
5. **Standard construction.**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- RINSE STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (parameters, water quality, rinse methods)
  Block C: Rinse method comparison (overflow vs. spray vs. counter-flow)

ZONE 3 -- WATER QUALITY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: Water quality comparison (tap / softened / DI / RO)

ZONE 4 -- DRAG-OVER IMPACT (22.0"--28.5" / ~6.5" tall)
  Block E: Alkaline drag-over consequences + prevention

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`, letter spacing -4
- Text: `ALUMINUM CONVERSION COATING`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Stage 2 -- Rinse (Pre-Deoxidize)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `The bridge between cleaning and activation. Every microSiemen of conductivity is a contaminant competing with your coating.`
- Y: 2.2"

---

### ZONE 2 -- Rinse Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE -- PRE-DEOXIDIZE`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 9.0". Full width within margins.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 5.0", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge:
- Rounded rect 1.6" x 0.4", fill `#2EC4B6`
- Text: `STAGE 2 -- RINSE` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Y: 4.2"

Parameters (JetBrains Mono 14 pt `#F0EDE8`, left column):
```
Water:           Fresh water, DI or RO preferred
Temperature:     Ambient to 80 F (27 C)
Method:          Overflow, spray, or counter-flow
Conductivity:    < 500 uS/cm (< 200 uS/cm ideal)
pH after rinse:  < 9.0 (confirms cleaner removal)
Time:            30--60 sec (immersion); continuous (spray)
```

Purpose callout (right side, rounded rect W: 10.0", H: 2.0", fill `#252B3D`, top accent `#2EC4B6`):
- Title: `PURPOSE` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Body: Inter Regular 14 pt `#F0EDE8`
- Text: `Remove ALL alkaline cleaner residues before the acid deoxidize stage. Alkaline carryover neutralizes the deoxidizer, wastes chemistry, and produces incomplete deoxidation that leads to coating failures.`

Critical check callout (right side, below purpose, rounded rect W: 10.0", H: 1.5", fill `#252B3D`, top accent `#E05C5C`):
- Title: `CRITICAL CHECK` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Body: Inter Medium 14 pt `#F0EDE8`
- Text: `If rinse pH stays above 9.0, cleaner drag-over is excessive. Increase overflow rate, add a second rinse stage, or reduce cleaner concentration.`

---

**BLOCK C -- Rinse Method Comparison**

Y: 9.5" to 15.0". Three panels side-by-side.

| Method | X | W | Accent |
|---|---|---|---|
| Overflow Immersion | 0.5" | 7.33" | `#2EC4B6` |
| Spray Rinse | 8.08" | 7.33" | `#E8A020` |
| Counter-Flow (2-Stage) | 15.67" | 7.83" | `#27AE60` |

Each panel: Rounded rect, H: 5.3", fill `#1E2435`, radius 6, top accent 4 pt.

**Overflow Immersion:**
- Title: Barlow SemiBold, 18 pt, `#2EC4B6`
- Parameters: `1--3 gal/min overflow` / `Parts fully submerged` / `Simple, reliable`
- Best for: `Rack lines, small batch operations`
- Limitation: `Higher water consumption than counter-flow`

**Spray Rinse:**
- Title: Barlow SemiBold, 18 pt, `#E8A020`
- Parameters: `15--25 psi, ambient` / `Fan nozzles for coverage` / `Low water consumption`
- Best for: `Conveyor lines, high-throughput spray systems`
- Limitation: `Recesses and blind holes may not rinse completely`

**Counter-Flow (2-Stage):**
- Title: Barlow SemiBold, 18 pt, `#27AE60`
- Parameters: `Fresh DI enters Stage 2, overflows to Stage 1` / `Parts travel Stage 1 -> Stage 2` / `Lowest water use, best quality`
- Best for: `Automotive OEM lines, high-volume operations`
- Limitation: `More tankage; higher capital cost`

---

### ZONE 3 -- Water Quality Table

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WATER QUALITY -- THE HIDDEN VARIABLE`

**BLOCK D -- Water Quality Comparison Table**

Y: 16.3" to 21.8". Column widths (23.0" total): Water Type (3.5") | Conductivity (3.0") | Minerals (4.5") | Chloride (3.0") | Suitability (9.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Water Type | Conductivity | Minerals | Chloride | Suitability for Ti/Zr Lines |
|---|---|---|---|---|
| City Tap Water | 200--1000+ uS/cm | Ca, Mg, Fe present | Variable (0--250+ ppm) | Intermediate rinses only; NOT for final rinse |
| Softened Water | 200--500 uS/cm | Ca/Mg removed; Na remains | Same as source | Better; acceptable for intermediate rinses |
| DI Water | < 10 uS/cm (typ. < 5) | Negligible | < 1 ppm | Preferred for all rinse stages |
| RO Water | < 50 uS/cm (typ. 10--30) | Very low | Very low | Excellent; cost-effective alternative to full DI |

Data: JetBrains Mono 12 pt. Stage names: Inter Medium 13 pt.

Below table -- highlight callout:
- Rounded rect, W: 23.0", H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `For Ti/Zr coatings, dissolved minerals in rinse water COMPETE with Zr deposition. DI or RO water is the standard for automotive and aerospace lines.` -- Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Drag-Over Impact

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ALKALINE DRAG-OVER -- THE INVISIBLE KILLER`

**BLOCK E -- Drag-Over Consequences Panel**

Y: 22.9" to 28.3". Two panels.

**Left -- The Problem:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#E05C5C`
- Title: `WHAT HAPPENS` -- Barlow SemiBold, 20 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
1. Alkaline cleaner clings to parts and rack
2. Drag-over enters the deox tank
3. Alkaline chemistry raises deox pH
4. Acid is neutralized -- less effective deox
5. Oxide and smut remain on aluminum surface
6. Ti/Zr coating deposits unevenly or not at all
7. Paint adhesion fails in service
```

**Right -- The Prevention:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `HOW TO PREVENT IT` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
- Adequate drain time over cleaner (10--15 sec)
- Fresh water overflow at 1--3 gal/min
- Counter-flow rinse for high-volume lines
- Monitor rinse conductivity daily
- Monitor rinse pH -- must drop below 9.0
- Double rinse stages for aerospace processing
- Periodic dump-and-refill if conductivity climbs
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HIGH CONDUCTIVITY | Inadequate overflow; cleaner drag-over accumulating | Increase overflow rate; consider counter-flow |
| 2 | 6.33" | RINSE pH > 9.0 | Excessive alkaline carryover; cleaner too concentrated | Improve drain time; reduce cleaner concentration |
| 3 | 12.16" | WATER SPOTS ON PARTS | Hard water minerals drying on surface | Switch to DI/RO water; improve air knife drainage |
| 4 | 18.0" | POOR DEOX DOWNSTREAM | Contaminated rinse neutralizing acid; insufficient rinsing | Double rinse; dump-and-fill; monitor daily |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Rinse (Pre-Deoxidize)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for rinse stages in Ti/Zr and non-chromate conversion coating lines. Water quality requirements vary by process supplier and specification. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Rinse Pre-Deox -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being "boring" -- this one counters that by making water quality the star. The conductivity comparison table and the drag-over impact chain give operators concrete reasons to care about their rinse water. The counter-flow rinse method comparison educates shops that may be running single-stage overflow and wondering why their coating is inconsistent.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #193 -- Construction Workup v1.0*
*2026-04-26*
