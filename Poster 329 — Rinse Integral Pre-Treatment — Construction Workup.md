---
Project: Plating Posters Inc
Poster Number: 329
Title: "Rinse -- Integral Color -- Pre-Treatment"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.3)"
Technical Source: Industry-standard rinse practices between alkaline clean and caustic etch for aluminum anodizing. Parameters are typical ranges for cascade and immersion rinsing.
Process Scope: Integral color anodizing -- Stage 2 of 8 (Rinse -- Pre-Etch)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - Rinse
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #329 -- Construction Workup
## Rinse -- Integral Color -- Pre-Treatment

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. This rinse removes alkaline cleaner chemistry before the etch tank. Inadequate rinsing here means cleaner surfactants contaminate the etch bath, causing streaking. For integral color, streaking in the etch step translates directly to color variation in the finished part.

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
ZONE 3 -- RINSE PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE METHODS COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- DRAGOUT REDUCTION + MONITORING (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES + WATER QUALITY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Integral Color -- Pre-Treatment Rinse -- Stage 2 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The bridge between cleaning and etching. Cleaner residue in the etch bath means streaky etching -- and streaky etching means streaky color.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly cleaned surface with alkaline residue --> After: Residue-free surface ready for etch`

---

### ZONE 3 -- Rinse Process Hero

**Section label:** `PRE-ETCH RINSE -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Parameter Panel + Rinse Tank Diagram**

Y: 5.0" to 14.0".

**Left (X: 0.5", W: 11.0") -- Parameter Table:**

Rounded rect, H: 8.5", fill `#1E2435`, radius 8.

| Parameter | Value |
|---|---|
| Water quality | City water acceptable; DI preferred for quality-critical work |
| Temperature | Ambient (room temperature) |
| Time | 30--60 seconds with agitation |
| Method | Double rinse (cascade) preferred |
| Conductivity target | < 500 uS/cm in final rinse |
| Agitation | Air or mechanical |

Parameter labels: Inter Medium, 14 pt, `#F0EDE8` at 60%. Values: JetBrains Mono Regular, 15 pt, `#F0EDE8`.

**Right (X: 12.0", W: 11.5") -- Cascade Rinse Diagram:**

Rounded rect, fill `#1E2435`, radius 8.

Two tank rectangles side by side representing cascade rinse:
- Tank 1 (dirty): rect fill `#252B3D`, border `#3A4055`, label `STAGE 1 (DIRTY)`
- Tank 2 (clean): rect fill `#252B3D`, border `#2EC4B6`, label `STAGE 2 (CLEAN)`
- Arrow showing water flow from clean to dirty (counter-flow)
- Arrow showing parts movement from dirty to clean
- Fresh water input arrow into Tank 2: `FRESH WATER IN` in Teal
- Overflow drain from Tank 1: `DRAIN` in `#F0EDE8` at 50%

Labels: Inter Medium 12 pt. Flow arrows: 2 pt `#2EC4B6`.

**Bottom callout (Y: 13.5"):**
- `Counter-flow cascade rinsing is the most water-efficient method. Fresh water enters the final (cleanest) stage and flows backward to the first (dirtiest) stage.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Rinse Methods Comparison

**Section label:** `RINSE METHODS -- CHOOSE YOUR APPROACH` -- Y: 14.7".

**Three-column comparison (Y: 15.3" to 20.3"):**

| Method | X | W | Accent | Title |
|---|---|---|---|---|
| Single Immersion | 0.5" | 7.33" | `#3A4055` | SINGLE DIP |
| Double Cascade | 8.0" | 7.33" | `#2EC4B6` | CASCADE (PREFERRED) |
| Spray Rinse | 15.5" | 8.0" | `#E8A020` | SPRAY |

Each box: Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06".

*Single Dip:*
- `One tank, still or agitated`
- `Water efficiency: Low`
- `Rinse quality: Moderate`
- `Best for: Low-volume, non-critical`
- Highlight: `Simplest but least effective` Inter Medium 12 pt `#3A4055`

*Cascade:*
- `Two or three tanks in series`
- `Water efficiency: HIGH`
- `Rinse quality: Excellent`
- `Best for: Production lines, quality-critical`
- Highlight: `RECOMMENDED for integral color` Inter Medium 12 pt `#2EC4B6`

*Spray:*
- `Fresh water spray over parts`
- `Water efficiency: High`
- `Rinse quality: Good`
- `Best for: Large parts, automated lines`
- Highlight: `Effective but equipment-dependent` Inter Medium 12 pt `#E8A020`

---

### ZONE 5 -- Dragout Reduction + Monitoring

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Dragout Reduction Tips:**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `REDUCE DRAGOUT -- SAVE CHEMISTRY` Barlow SemiBold 18 pt `#27AE60`.

Bullets (Inter Regular 14 pt `#F0EDE8`):
- `Dwell rack over cleaner tank 10--15 sec before entering rinse`
- `Reduces dragout by 50--80%`
- `Slower withdrawal speed = thinner drag-out film`
- `Orient parts to drain freely (no cupping)`
- `Dragout reduction saves cleaner AND reduces rinse contamination`

**Right -- Monitoring:**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `MONITOR YOUR RINSE` Barlow SemiBold 18 pt `#E8A020`.

| Check | Method | Target |
|---|---|---|
| Conductivity | Handheld meter | < 500 uS/cm |
| pH | pH strip or meter | 6--8 (neutral) |
| Visual | Observe rinse water | Clear, no foam |
| Frequency | Every shift | Continuous for cascade |

JetBrains Mono 13 pt for values. Inter Regular 13 pt for labels.

Note: `Rising conductivity = rising contamination. Act before it reaches the etch tank.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Failure Modes + Water Quality

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Failure Modes (4 cards, 2x2 grid):**

| Position | Defect | Cause | Fix |
|---|---|---|---|
| R1C1 | STREAKY ETCH | Cleaner surfactant in etch bath | Improve rinse; check conductivity |
| R1C2 | COLOR VARIATION | Uneven cleaner removal | Extend rinse time; add agitation |
| R2C1 | ETCH RATE DRIFT | Alkaline drag-in accelerates etch | Better dragout control |
| R2C2 | FOAM IN ETCH | Surfactant carry-over | Replace rinse water; dwell longer |

Each card: Rounded rect W: 5.25", H: 2.5", fill `#1E2435`, left accent `#E05C5C`.

**Right -- Water Quality Reference:**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `WATER QUALITY MATTERS` Barlow SemiBold 18 pt `#2EC4B6`.

| Parameter | City Water | DI Water |
|---|---|---|
| Conductivity | 200--800 uS/cm | < 10 uS/cm |
| Chloride | 10--100 ppm | < 1 ppm |
| Hardness | 50--300 ppm CaCO3 | < 1 ppm |
| Cost | Low | Higher |
| Suitability | Pre-etch rinse OK | Pre-anodize rinse required |

Note: `DI water is preferred for all rinse stages in integral color work. City water is acceptable here (pre-etch) but DI is mandatory at Stage 6 (pre-anodize).` Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Integral Color -- Pre-Treatment`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; standard rinse practices for aluminum anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Integral Pre-Treatment -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being "boring" -- lean into the cascade rinse diagram as the hero visual. The key insight for the operator: this rinse protects the etch bath from contamination, and etch uniformity directly controls integral color consistency. The dragout reduction tips are immediately actionable on the shop floor.

---

*Alaina -- Poster #329 -- Construction Workup v1.0 -- 2026-04-26*
