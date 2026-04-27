---
Project: Plating Posters Inc
Poster Number: 99
Title: "Rinse -- Copper (Acid) -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Pre-plate rinse for acid copper sulfate plating line (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CopperPlating
  - AcidCopper
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEP09
---

# Poster #99 -- Construction Workup
## Rinse -- Copper (Acid) -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of the acid copper process. This rinse removes activation acid residue before the copper plating tank. The critical concern here is not pH neutralization (the copper bath is strongly acidic anyway) but preventing drag-in of contaminants -- dissolved metals from the acid dip, iron from steel etching in HCl, and chloride concentration spikes that could upset the tightly controlled Cl- window in the acid copper bath.

Hero visual: cascade rinse tank diagram with contamination flow callouts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Standard 2--3 tank cascade.
2. **Orientation strip (Block C):** Stage 4 highlighted.
3. **Rinse parameter table + Chloride drag-in callout.**
4. **Problems table and safety/water quality panel.**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5")
ZONE 4 -- RINSE PARAMETERS + CHLORIDE CALLOUT (14.5"--21.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Acid) -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".

**Tagline:** `The acid copper bath controls chloride to the ppm. Drag contamination in from the acid dip and you shift the entire additive balance.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted (fill `#2EC4B6`, 100%). Others dimmed.

Below strip: `Before: Acid-activated surface  -->  After: Clean, neutral surface entering copper tank`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE PRE-PLATE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 14.0". Two connected tank cross-sections (2-stage cascade -- simpler rinse than pre-activation since both sides are acidic):

**Tank 1 (Dirty Rinse) -- X: 1.5", W: 10.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `STAGE 1 (DIRTY)` -- Barlow SemiBold 16 pt `#E8A020`
- Inside label: `Contains dissolved metals, acid residue, Cl- from HCl dip` -- Inter Regular 12 pt `#F0EDE8` at 60%
- Overflow to drain

**Tank 2 (Clean Rinse) -- X: 12.5", W: 10.0", H: 7.5":**
- Fill `#252B3D` with `#2EC4B6` tint at 10%
- Label: `STAGE 2 (CLEAN)` -- Barlow SemiBold 16 pt `#2EC4B6`
- `FRESH WATER IN` arrow from right
- Overflow into Tank 1

Parts movement: `PARTS TRAVEL -->` left to right.
Water flow: `<-- WATER FLOW (counter-current)`.

**Contamination callout boxes flanking the diagram:**

Left callout (Y: 11.0"):
- Accent `#E05C5C`
- `IRON DRAG-IN: Fe dissolved during HCl activation accumulates in rinse. Keep rinse fresh to prevent Fe carry-over into copper bath.`

Right callout (Y: 11.0"):
- Accent `#E8A020`
- `CHLORIDE DRAG-IN: HCl acid dip is a major source of Cl- contamination. Acid copper Cl- window is only 30--80 ppm. Even small drag-in matters.`

Key metrics (Y: 13.0"):
- `Target: < 200 uS/cm conductivity at final stage. Single overflow minimum; cascade preferred.`

---

### ZONE 4 -- Rinse Parameters + Chloride Callout

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

| Parameter | Value |
|---|---|
| Water type | DI preferred; city water acceptable |
| Temperature | Ambient |
| Flow rate | 2--5 gal/min per stage |
| Stages | 1--2 (single overflow minimum) |
| Immersion time | 30--60 sec |
| Agitation | Air or part movement |
| Conductivity target | < 200 uS/cm |
| Drain time | 10--15 sec |
| Rinse criterion | No acid residue; near-neutral pH |

**Right -- Chloride Control Callout (X: 15.0", W: 8.5"):**

Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `THE CHLORIDE WINDOW` -- Barlow SemiBold 18 pt `#E8A020`

Body:
> Acid copper sulfate controls Cl- within a narrow band: 30--80 ppm. Below 30 ppm, the brightener system fails -- hazy, milky deposits. Above 100 ppm, deposits go dull and streaky.
>
> HCl from the activation acid dip is the #1 source of uncontrolled Cl- addition. One poorly rinsed rack can spike Cl- by 5--10 ppm in a small tank.
>
> This rinse is your firewall.

Key metric: `Monitor copper bath Cl- weekly by AgNO3 titration or ISE` -- JetBrains Mono 12 pt `#E8A020`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-PLATE RINSE` -- Y: 21.2".

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Chloride spike in Cu bath | Dull, streaky deposit at LCD | HCl drag-in from activation | Improve rinse; switch activation to H2SO4 |
| Iron contamination | Roughness, dark spots | Fe from HCl on steel | Fresh rinse water; consider drag-out rinse |
| Insufficient rinsing | General haze, brightener consumption up | Rinse flow too low or no cascade | Add cascade; increase flow rate |
| Dry spots on parts | Skip plating or uneven thickness | Parts left too long between rinse and plate | Minimize transfer time; keep parts wet |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

**Left -- Water Quality (X: 0.5", W: 11.0"):**
- Title: `WATER QUALITY` -- `#2EC4B6`
- `DI water: < 10 uS/cm -- best for acid copper lines`
- `City water: acceptable but adds minerals and Cl-`
- `Note: city water Cl- adds to copper bath Cl- budget`
- `Monitor rinse conductivity -- flag any sudden rise`
- `Copper in rinse overflow: treat before discharge (EPA limit ~1.0 mg/L)`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` -- `#E8A020`
- `Rinse water is mildly acidic from drag-out`
- `Copper sulfate in drag-out: toxic to aquatic life`
- `Route all rinse overflow to waste treatment`
- `Wet floors: slip hazard -- maintain drainage`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Copper (Acid) -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table. **Export:** Six files -- `Rinse Copper Acid Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The unique angle for this rinse poster is the chloride window. In zinc plating, the pre-plate rinse story is about pH and drag-in of incompatible chemistry. In acid copper, the story is about chloride -- a few ppm too much or too little and the entire brightener system shifts. The chloride callout panel makes this the teaching moment of the poster. If a shop is chasing hazy deposits in acid copper, this poster should make them look at their rinse first.

---

*Alaina -- Poster #99 -- Construction Workup v1.0 -- 2026-04-26*
