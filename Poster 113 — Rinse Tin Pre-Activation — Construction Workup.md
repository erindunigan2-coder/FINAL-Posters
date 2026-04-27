---
Project: Plating Posters Inc
Poster Number: 113
Title: "Rinse -- Tin -- Pre-Activation"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Pre-activation rinse for acid tin plating (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #113 -- Construction Workup
## Rinse -- Tin -- Pre-Activation

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The rinse between cleaning and activation. Its job is simple: remove every trace of alkaline cleaner before the part enters the acid activation dip. Alkaline drag-in neutralizes the acid, wastes activation chemistry, and leaves a buffered film that prevents proper oxide removal. This poster covers rinse types, contamination thresholds, and the metrics that prove a rinse is working.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Flowing water rinse tank showing parts entering with alkaline film and exiting clean. Built with rectangles, flow arrows, and labeled zones.
2. **Rinse type comparison (Block D):** Single overflow vs. counterflow cascade vs. spray -- three options with pros/cons.
3. **Contamination drag-in diagram (Block E):** Visual showing what happens when alkaline cleaner reaches the acid activation tank.
4. **Rinse quality metrics strip (Block F):** Conductivity, pH, and visual checks.

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
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE TYPE COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- DRAG-IN CONSEQUENCES (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE QUALITY METRICS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin Plating -- Pre-Activation -- Stage 2 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The alkaline cleaner did its job. Now get it off the part -- completely -- before the acid sees it.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean part with alkaline film  -->  After: Neutral surface ready for acid activation`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE PRE-ACTIVATION RINSE` -- Y: 4.4".

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.0"
- Fill: `#252B3D` (rinse water)
- Border: 2 pt `#2EC4B6`

**Water flow indicators:**
- Horizontal wavy arrows across the tank, stroke 2 pt `#2EC4B6` at 50%
- Label: `Fresh water in (bottom)` at bottom-left, `Overflow out (top)` at top-right

**Parts entering (left side):**
- Vertical rect representing rack/barrel, X: 4.0", Y: 6.0", H: 5.0"
- Border: 2 pt `#E8A020` (indicating alkaline contamination)
- Label above: `PARTS IN` Barlow SemiBold 14 pt `#E8A020`
- Annotation: `Carrying alkaline cleaner film` Inter Regular 12 pt `#E8A020`

**Parts exiting (right side):**
- Vertical rect, X: 18.0", Y: 6.0", H: 5.0"
- Border: 2 pt `#27AE60` (clean)
- Label above: `PARTS OUT` Barlow SemiBold 14 pt `#27AE60`
- Annotation: `Alkaline-free, ready for acid` Inter Regular 12 pt `#27AE60`

**Key parameter labels (inside tank):**
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Water: City or DI` JetBrains Mono 14 pt `#F0EDE8`
- `Flow: Continuous overflow` JetBrains Mono 14 pt `#2EC4B6`
- `Time: 30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`

**Bottom callout:**
- `The rinse removes alkaline cleaner. If alkaline drag-in reaches the acid activation, it neutralizes the acid and the activation fails.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Rinse Type Comparison

**Section label:** `THREE RINSE CONFIGURATIONS` -- Y: 14.7".

**BLOCK D -- Three-Column Comparison**

Y: 15.3" to 20.0". Three side-by-side callout boxes.

| Config | X | W | Accent | Title |
|---|---|---|---|---|
| Single Overflow | 0.5" | 7.33" | `#3A4055` | SINGLE OVERFLOW |
| Counterflow Cascade | 8.0" | 7.33" | `#2EC4B6` | COUNTERFLOW CASCADE |
| Spray Rinse | 15.5" | 8.0" | `#27AE60` | SPRAY RINSE |

Each box: Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06".

*Single Overflow:*
- `One tank, continuous fill and drain`
- `Simple, low cost`
- `Higher water usage per part`
- `Adequate for light carry-over`
- Verdict: `Minimum standard` Inter Medium 13 pt `#3A4055`

*Counterflow Cascade:*
- `Two or three tanks in series`
- `Fresh water enters last tank, overflows backward`
- `Lowest water consumption per part`
- `Best rinse quality`
- Verdict: `RECOMMENDED for tin lines` Inter Medium 13 pt `#2EC4B6`

*Spray Rinse:*
- `High-pressure nozzles above tank`
- `Excellent for rack lines`
- `Fast cycle time`
- `May miss recessed areas on complex parts`
- Verdict: `Good supplement to immersion` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Drag-In Consequences

**Section label:** `WHAT HAPPENS WHEN ALKALINE REACHES THE ACID` -- Y: 20.7".

**BLOCK E -- Contamination Consequence Panel**

Y: 21.3" to 26.0". Full-width rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Three-column layout inside the panel:

| Column | Header | Content |
|---|---|---|
| Left | `THE DRAG-IN` | Alkaline cleaner carried on parts and rack. Typical drag-in: 0.1--0.5 mL per sq ft of surface area. |
| Center | `THE REACTION` | NaOH + H2SO4 -> Na2SO4 + H2O. Neutralizes acid. Raises pH. Reduces activation effectiveness. |
| Right | `THE RESULT` | Oxide film remains on surface. Tin adhesion fails. Blistering, peeling, skip plating. |

Each column: accent color header bar. Left: `#E8A020`. Center: `#E05C5C`. Right: `#E05C5C`.

Bottom rule: `One good rinse prevents one bad plating lot. The math is simple.` Inter Medium 14 pt `#27AE60`

---

### ZONE 6 -- Rinse Quality Metrics

**Section label:** `HOW TO KNOW YOUR RINSE IS WORKING` -- Y: 26.7".

**BLOCK F -- Metrics Strip**

Y: 27.3" to 32.0". Four metric cards in a row.

| Card | X | Metric | Target | Method |
|---|---|---|---|---|
| 1 | 0.5" | pH | 6.0--8.0 (neutral) | pH paper or meter in rinse overflow |
| 2 | 6.33" | CONDUCTIVITY | < 50 microS/cm | Conductivity meter |
| 3 | 12.16" | WATER BREAK | Complete sheeting | Visual -- no beading or pulling back |
| 4 | 18.0" | FLOW RATE | 2--4 gal/min minimum | Flow meter or timed bucket test |

Each card: Rounded rect, W: 5.5", H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt in `#2EC4B6`.
Metric name: Barlow SemiBold 16 pt `#2EC4B6`.
Target: JetBrains Mono 14 pt `#27AE60`.
Method: Inter Regular 12 pt `#F0EDE8` at 70%.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Tin -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Tin Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters are the "boring" ones -- and that is exactly why they matter. Operators skip rinses, cut immersion time, and let water flow rates drop. This poster exists to make the consequence of bad rinsing viscerally obvious. The drag-in consequence panel is the centerpiece argument: one chemical equation, one failed lot.

---

*Alaina -- Plating Posters Inc*
*Poster #113 -- Construction Workup v1.0*
*2026-04-26*
