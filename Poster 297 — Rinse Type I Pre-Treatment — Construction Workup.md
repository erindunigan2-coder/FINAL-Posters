---
Project: Plating Posters Inc
Poster Number: 297
Title: "Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Treatment"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 3, Section 3.3)"
Process Scope: Pre-etch rinse for chromic acid anodizing -- Stage 2 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - ChromicAcid
  - TypeI
  - Rinse
  - ConstructionWorkup
  - ClusterAnodize03
---

# Poster #297 -- Construction Workup
## Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Treatment

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The pre-etch rinse removes alkaline cleaner before the etch tank. For Type I, any contamination that survives this rinse eventually reaches the chromic acid bath -- and the chromic acid bath has the tightest contamination limits of any anodize electrolyte.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse diagram (Block B -- HERO):** Two or three cascade rinse tanks showing counter-flow water direction, overflow weirs, and dragout concept.
2. **Dragout reduction callout (Block D):** Visual showing dwell/drain time over the previous tank.
3. **Water quality table (Block E):** Conductivity targets, chloride limits, water source comparison.
4. **Defect grid (Block F):** 4 rinse-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAGOUT + WATER QUALITY (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT GRID + RINSE MONITORING (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE EFFICIENCY PRINCIPLES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromic Acid Anodizing (Type I) -- Pre-Treatment -- Stage 2 of 8` -- 30 pt `#2EC4B6`. Y: 1.4".
**Tagline:** `The bridge between cleaning and etching. Inadequate rinsing here means streaking in the etch and contamination all the way to the chromic acid bath.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Cr(VI) flag:** Same coral badge as cluster standard.

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted. Before/After: `Before: Clean part carrying alkaline cleaner residue  -->  After: Residue-free surface ready for etch or desmut`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `COUNTER-FLOW CASCADE RINSING` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Diagram**

Y: 5.0" to 13.5".

**Two-tank cascade (preferred) or three-tank cascade (aerospace):**

Tank 1 (dirty rinse, left): Rounded rect, X: 2.0", W: 9.0", H: 6.5", fill `#252B3D`, border 2 pt `#C8D0D8`
Tank 2 (clean rinse, right): Rounded rect, X: 13.0", W: 9.0", H: 6.5", fill `#252B3D` at lighter tint, border 2 pt `#C8D0D8`

Fresh water arrow: enters Tank 2 from right side. Label: `Fresh DI or city water in` JetBrains Mono 12 pt `#2EC4B6`
Overflow arrow: from Tank 2 to Tank 1. Label: `Overflow (counter-flow)` Inter Regular 12 pt `#F0EDE8`
Drain arrow: exits Tank 1 to left. Label: `To drain` Inter Regular 12 pt `#F0EDE8` at 60%
Part movement arrow: large arrow from Tank 1 to Tank 2 above tanks. Label: `Part travel direction -->` Barlow SemiBold 14 pt `#E8A020`

**Inside Tank 1:**
- Label: `RINSE 1 (DRAG-OUT)` Barlow SemiBold 16 pt `#F0EDE8`
- `Higher contamination` Inter Regular 12 pt `#F0EDE8` at 60%
- `Captures bulk cleaner residue` Inter Regular 12 pt `#F0EDE8` at 60%

**Inside Tank 2:**
- Label: `RINSE 2 (FINAL)` Barlow SemiBold 16 pt `#2EC4B6`
- `Low contamination` Inter Regular 12 pt `#2EC4B6`
- `Target: < 500 uS/cm` JetBrains Mono 13 pt `#27AE60`

**Operating parameters (right side callout):**
- Rounded rect, X: 15.0", Y: 12.5", W: 8.0", H: 2.5", fill `#1E2435`
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 30--60 sec with agitation` JetBrains Mono 13 pt `#F0EDE8`
- `Method: Double cascade preferred` JetBrains Mono 13 pt `#2EC4B6`
- `Aerospace: Triple cascade common` JetBrains Mono 12 pt `#E8A020`

---

### ZONE 4 -- Dragout + Water Quality

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Dragout Reduction (X: 0.5", W: 11.0"):**

Section label: `REDUCE DRAGOUT -- SAVE YOUR DOWNSTREAM TANKS` Barlow Condensed ExtraBold 20 pt.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `Dwell the rack over the cleaner tank for 10--15 seconds before entering rinse` Inter Medium 14 pt `#E8A020`
- `This single practice reduces dragout by 50--80%` Inter Medium 14 pt `#27AE60`
- `Less dragout = cleaner rinse water = less contamination reaching the etch and anodize tanks` Inter Regular 13 pt `#F0EDE8` at 80%
- `For barrel work: slow extraction speed; allow 15--20 sec drain` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Water Quality Table (X: 12.0", W: 11.5"):**

Section label: `WATER QUALITY TARGETS` Barlow Condensed ExtraBold 20 pt.

| Parameter | Target | Notes |
|---|---|---|
| Conductivity | < 500 uS/cm (final rinse) | Monitor with inline meter |
| Chloride | Minimize | Cl- carries into chromic acid bath (limit < 10 ppm in bath) |
| Temperature | Ambient | No heating needed |
| pH | Near neutral after rinsing | Confirms cleaner removal |
| Water source | City water acceptable; DI preferred | DI strongly preferred for Type I |

Header: Barlow SemiBold 13 pt on `#3A4055`. Data: Inter Regular 12 pt, JetBrains Mono for values.

---

### ZONE 5 -- Defect Grid + Rinse Monitoring

**Left -- Defect Grid (X: 0.5", W: 14.0", 2x2):**

Section label: `WHAT GOES WRONG -- 4 RINSE FAILURES`

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | STREAKING IN ETCH | `#E8A020` | Cleaner residue carried into etch | Improve cascade; extend dwell time |
| R1C2 | ETCH BATH CONTAMINATION | `#E05C5C` | Surfactants from cleaner drag-over | Add drain dwell; improve rinse |
| R2C1 | ACCELERATED ETCH RATE | `#E8A020` | Alkaline cleaner raising etch NaOH | Better rinse; monitor etch concentration |
| R2C2 | CHROMIC ACID CONTAMINATION | `#E05C5C` | Contaminants surviving rinse + etch + desmut | Entire pre-treatment chain must work together |

**Right -- Conductivity Monitoring (X: 15.0", W: 8.5"):**

Callout box, fill `#1E2435`:
- Title: `MONITOR YOUR RINSE` Barlow SemiBold 18 pt `#2EC4B6`
- `Inline conductivity meter is the single best investment for rinse quality control` Inter Regular 13 pt `#F0EDE8`
- `High reading = poor rinsing = contamination moving downstream` Inter Medium 13 pt `#E05C5C`
- `Track daily. Trend weekly. React before problems reach the anodize tank.` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Rinse Efficiency Principles

**Section label:** `THE PHYSICS OF RINSING` -- Y: 26.7".

Full-width callout, fill `#1E2435`, Y: 27.3" to 32.3":

Three key principles in a row:

| Principle | Icon Concept | Text |
|---|---|---|
| Dilution | Water drop | `Each cascade stage dilutes contaminants by 10--100x. Two stages = 100--10,000x reduction.` |
| Agitation | Wavy lines | `Moving water rinses faster than still water. Air sparging or part movement accelerates mixing.` |
| Time | Clock | `Minimum 30 sec per stage. Longer is better. The rinse is not a pass-through -- it is a chemical step.` |

Each: Rounded rect W: 7.33", H: 4.0", fill `#252B3D`, left accent `#2EC4B6`.
Principle name: Barlow SemiBold 18 pt `#2EC4B6`.
Body: Inter Regular 13 pt `#F0EDE8`, line height 155%.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Chromic Acid Anodizing (Type I) -- Pre-Treatment`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type I Pre-Treatment -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being "boring" -- but this one earns its wall space by connecting the humble rinse tank to the extremely contamination-sensitive chromic acid bath downstream. The cascade rinse diagram is the hero visual that makes the physics intuitive. The dragout reduction tip (10--15 sec dwell) is the single most actionable takeaway on this poster.

---

*Alaina -- Plating Posters Inc*
*Poster #297 -- Construction Workup v1.0*
*2026-04-26*
