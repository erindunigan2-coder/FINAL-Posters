---
Project: Plating Posters Inc
Poster Number: 97
Title: "Rinse -- Copper (Acid) -- Pre-Activation"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Pre-activation rinse for acid copper sulfate plating line (Stage 2 of 8)
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

# Poster #97 -- Construction Workup
## Rinse -- Copper (Acid) -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of the acid copper process. This rinse removes alkaline cleaner residue before the acid activation step. Alkaline drag-in neutralizes the activation acid and can cause surface staining. Same principles as the zinc rinse poster but applied to the copper line context -- with the additional nuance that any cleaner residue dragged into a subsequent acid copper bath can decompose the organic brightener system.

Hero visual: cascade rinse tank diagram showing counter-current water flow.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Two or three connected tanks in cross-section with counter-current flow arrows.
2. **Orientation strip (Block C):** Stage 2 highlighted.
3. **Rinse parameter table (Block D) + Drag-out callout (Block E).**
4. **Problems table and safety/water quality callout.**

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
  Stage 2 highlighted
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5")
ZONE 4 -- RINSE PARAMETER TABLE + DRAG-OUT (14.5"--21.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Acid) -- Pre-Activation -- Stage 2 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".

**Tagline:** `Alkaline cleaner in the activation tank is dead acid. Alkaline cleaner in the copper tank is dead brightener. Rinse it out.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Same structure as Poster #96 strip. **Stage 2 highlighted** (fill `#2EC4B6`, 100%). All others dimmed.

Below strip: `Before: Alkaline-cleaned surface (pH ~12)  -->  After: Neutral surface ready for acid activation`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE CASCADE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 14.0". Three connected tank cross-sections (3-stage counter-current cascade):

**Tank 1 (Dirty Rinse) -- X: 0.5", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior tinted `#E8A020` at 10% (alkaline contamination)
- Label: `STAGE 1 (DIRTY)` -- Barlow SemiBold 16 pt `#E8A020`
- Overflow arrow to DRAIN

**Tank 2 (Middle Rinse) -- X: 8.0", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `STAGE 2 (MIDDLE)` -- Barlow SemiBold 16 pt `#F0EDE8`
- Overflow into Tank 1

**Tank 3 (Clean Rinse) -- X: 15.5", W: 7.0", H: 7.5":**
- Fill `#252B3D` with `#2EC4B6` tint at 10%
- Label: `STAGE 3 (CLEAN)` -- Barlow SemiBold 16 pt `#2EC4B6`
- `FRESH WATER IN` arrow from right

Parts movement arrow (below tanks): `PARTS TRAVEL -->` left to right.
Water flow arrow (above tanks): `<-- WATER FLOW (counter-current)`.

Key metrics callout (Y: 13.0"):
- `A 3-stage cascade uses 90% less water than a single flowing rinse for the same dilution ratio. Target: < 500 uS/cm conductivity at final stage.`

---

### ZONE 4 -- Rinse Parameter Table

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

Header: `PRE-ACTIVATION RINSE` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Water type | DI preferred; city water acceptable |
| Temperature | Ambient (no heating required) |
| Flow rate | 2--5 gal/min per stage (cascade) |
| Stages | 2--3 stage cascade recommended |
| Immersion time | 30--60 sec per stage |
| Agitation | Air or part movement |
| Conductivity target | < 500 uS/cm at final stage |
| Drain time | 10--15 sec between tanks |
| Rinse criterion | No alkaline residue (pH paper check: 6--8) |

**Right -- Drag-Out Callout (X: 15.0", W: 8.5"):**

Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `WHY THIS RINSE MATTERS` -- Barlow SemiBold 18 pt `#E8A020`

Body:
> Alkaline cleaner (pH 12--14) is dragged into the rinse on every rack. If this residue reaches the activation tank, it neutralizes the acid. If it reaches the copper tank, it decomposes organic brighteners -- causing haze, loss of leveling, and accelerated carbon treatment cycles.
>
> Result: wasted chemistry and bad deposits.
>
> The rinse is the barrier between alkaline and acid worlds.

Key metric: `Drag-out rate: ~0.5--2.0 gal per 1000 ft2 of surface` -- JetBrains Mono 12 pt `#2EC4B6`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-ACTIVATION RINSE` -- Y: 21.2".

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Alkaline carry-over | Activation acid neutralized; poor oxide removal | Insufficient rinse stages or time | Add cascade stage; increase flow |
| Brightener decomposition | Hazy copper deposit; accelerated carbon treatment | Alkaline drag-in reaching copper tank | Improve rinse; monitor conductivity |
| Spotting/staining | White mineral spots on surface | Hard water minerals (Ca, Mg) | Switch to DI water; add softener |
| Foam in rinse | Surfactant drag-out from cleaner | High-foam cleaner formulation | Use low-foam cleaner; add defoamer |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

**Section label:** `WATER QUALITY & SAFETY` -- Y: 27.2".

**Left -- Water Quality (X: 0.5", W: 11.0"):**
- Title: `WATER QUALITY MATTERS` -- Barlow SemiBold 18 pt `#2EC4B6`
- `DI water: < 10 uS/cm -- best for critical parts`
- `City water: 200--600 uS/cm -- acceptable for most work`
- `Hard water: > 300 ppm CaCO3 -- risk of mineral spotting`
- `Monitor final rinse conductivity daily`
- `Dump and refill when conductivity exceeds 1000 uS/cm`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` -- Barlow SemiBold 18 pt `#E8A020`
- `Rinse water is mildly alkaline from drag-out`
- `Rinse overflow goes to waste treatment -- not down the drain`
- `Wet floors: slip hazard -- maintain drainage and mats`
- `pH check rinse water periodically -- should be near neutral (6--8)`

---

### ZONE 7 -- Footer Band

Standard footer. Title: `Rinse -- Copper (Acid) -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 standard zones.

**Light Remap:** Standard table.

| Dark | Light |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

**Export:** Six files -- `Rinse Copper Acid Pre-Act -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This rinse poster follows the established cascade rinse visual pattern from Poster #33 (Zinc Alkaline Pre-Act Rinse). The unique angle for the copper line is the brightener decomposition pathway -- alkaline contamination doesn't just waste acid, it actively destroys the organic additive system in acid copper. This is a more expensive failure than in zinc, where there are no organic brighteners at the same concentration sensitivity.

---

*Alaina -- Poster #97 -- Construction Workup v1.0 -- 2026-04-26*
