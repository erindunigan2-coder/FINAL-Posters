---
Project: Plating Posters Inc
Poster Number: 277
Title: "Rinse -- EN Boron -- Post-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 7)"
Technical Source: Standard post-plate rinse for EN-B. Same handling precautions as EN-P. Cold rinse preferred to stop reaction. Watson domain expertise.
Process Scope: Post-plate rinse (Stage 6 of 8) for electroless nickel-boron plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #277 -- Construction Workup
## Rinse -- EN Boron -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse for EN-B stops the plating reaction, removes drag-out chemicals, and prepares the surface for post-treatment (typically heat treatment for maximum hardness). The rinse parameters are identical to EN-P post-plate rinsing: cold DI counterflow, do not air-dry before rinsing, avoid fingerprint contact. The unique EN-B concern is dimethylamine ((CH3)2NH) -- a volatile, flammable, fish-odor byproduct of DMAB reduction that is present in the drag-out. Ventilation at the rinse station is important for operator comfort and safety.

Hero visual: post-plate rinse sequence diagram showing the transition from EN-B bath to rinse to drying, with handling callouts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-plate rinse sequence hero (Block B):** EN-B bath -> cold rinse -> handling -> drying path.
2. **Rinse parameters table (Block D):** Standard DI counterflow specs with EN-B-specific notes.
3. **Handling and dimethylamine safety (Block E):** Volatile byproduct handling; surface handling rules.
4. **Defect grid (Block F):** 4 post-plate rinse-related defects.

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
  Stage 6 highlighted (Teal)
ZONE 3 -- POST-PLATE RINSE SEQUENCE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- HANDLING + DIMETHYLAMINE SAFETY (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 6 of 8 -- Post-Plate` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Stop the reaction. Remove drag-out. Protect the deposit. And ventilate -- DMAB byproducts have a smell you will not forget.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: EN-B coated surface leaving plating bath  -->  After: Rinsed surface ready for post-treatment / heat treatment`

---

### ZONE 3 -- Post-Plate Rinse Sequence Hero

**Section label:** `FROM EN-B BATH TO RINSE TO DRYING` -- Y: 4.4".

**BLOCK B -- Sequence Diagram (Y: 5.0" to 14.0")**

Horizontal flow diagram, left to right, showing four steps.

**Step 1 -- EN-B Bath Exit (X: 0.5", Y: 6.0", W: 5.0", H: 5.5"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `EN-B BATH EXIT` Barlow SemiBold 16 pt `#27AE60`
- Content:
  - `Parts exit EN-B bath with:` Inter Medium 14 pt `#F0EDE8`
  - `EN-B drag-out on surfaces` Inter Regular 13 pt `#F0EDE8`
  - `Contains: Ni2+, DMAB, borate, complexant, dimethylamine` JetBrains Mono 12 pt `#F0EDE8`
  - `Bath pH: 6.0-8.0 (DMAB) or 12.0-14.0 (NaBH4)` JetBrains Mono 12 pt `#F0EDE8`
- Warning: `Do NOT air-dry before rinse` Inter Medium 13 pt `#E05C5C`

**Arrow:** 3 pt `#3A4055`, right-pointing.

**Step 2 -- Cold Rinse (X: 6.5", Y: 5.5", W: 6.0", H: 6.5"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` 4 pt, border 2 pt `#2EC4B6`
- Title: `COLD DI RINSE` Barlow SemiBold 18 pt `#2EC4B6`
- Large callout: `COLD WATER PREFERRED` Barlow Condensed ExtraBold 18 pt `#2EC4B6`
- Content:
  - `DI counterflow -- 2-3 stages` Inter Medium 14 pt `#F0EDE8`
  - `Ambient or cold (15-25 C)` JetBrains Mono 13 pt `#F0EDE8`
  - `Cold rinse stops reaction faster` Inter Regular 13 pt `#F0EDE8`
  - `30-60 seconds per stage` JetBrains Mono 13 pt `#F0EDE8`
  - `Target: <50 uS/cm` JetBrains Mono 13 pt `#2EC4B6`
- Note: `Dimethylamine volatilizes at rinse -- ventilate` Inter Medium 12 pt `#E8A020`

**Arrow:** 3 pt `#3A4055`, right-pointing.

**Step 3 -- Handling (X: 13.5", Y: 6.0", W: 4.5", H: 5.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `HANDLING` Barlow SemiBold 16 pt `#E8A020`
- Content:
  - `Wear clean nitrile gloves` Inter Medium 13 pt `#F0EDE8`
  - `No fingerprints on deposit` Inter Medium 13 pt `#E05C5C`
  - `Do not stack parts wet` Inter Medium 13 pt `#E05C5C`
  - `Handle by edges or fixtures only` Inter Regular 13 pt `#F0EDE8`
  - `Inspect for coverage before drying` Inter Regular 13 pt `#F0EDE8`

**Arrow:** 3 pt `#3A4055`, right-pointing.

**Step 4 -- Drying (X: 19.0", Y: 6.0", W: 4.5", H: 5.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `DRYING` Barlow SemiBold 16 pt `#E8A020`
- Content:
  - `Air knife or forced air` Inter Regular 13 pt `#F0EDE8`
  - `Low-temperature oven: 60-80 C` JetBrains Mono 13 pt `#F0EDE8`
  - `Remove all moisture before post-treatment` Inter Regular 13 pt `#F0EDE8`
  - `Dry parts can proceed to heat treatment` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Rinse Parameters

**Section label:** `POST-PLATE RINSE PARAMETERS` -- Y: 14.7".

**BLOCK D -- Parameters Table (Y: 15.3" to 20.3")**

**Full-width callout (X: 0.5", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `EN-B POST-PLATE RINSE SPECIFICATIONS` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Type | DI counterflow, 2-3 stages |
| Temperature | Ambient or cold (15-25 C) -- cold preferred to stop reaction |
| Time | 30-60 seconds per stage |
| Water quality | DI or RO preferred |
| Conductivity target | <50 uS/cm in final rinse |
| Transfer | Immediate -- do not air-dry between bath and rinse |
| Handling | No bare-hand contact; no stacking wet parts |
| Ventilation | Local exhaust at rinse station -- dimethylamine is volatile |
| After rinse | Air knife dry -> low-temp oven (60-80 C) -> post-treatment |

Data: JetBrains Mono 13 pt `#F0EDE8`. Labels: Inter Medium 13 pt `#F0EDE8` at 60%.

**Bottom callout:**
- Rounded rect, W: 22.0", H: 0.5", fill `#2EC4B6` at 10%, border 1 pt `#2EC4B6`
- `Same rinse discipline as EN-P. No shortcuts. No air-drying. No fingerprints.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 5 -- Handling + Dimethylamine Safety

**Section label:** `HANDLING AND SAFETY -- WHAT IS DIFFERENT ABOUT EN-B` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Surface Handling (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `SURFACE HANDLING RULES` Barlow SemiBold 18 pt `#E8A020`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `1. NEVER touch freshly plated EN-B with bare hands` Inter Medium 14 pt `#E05C5C`
  - `Fingerprint oils etch into the deposit and cause adhesion failures`
  - `2. Do not stack parts wet -- galvanic attack at contact points`
  - `3. Do not let parts air-dry before rinsing -- watermarks from dried EN-B solution`
  - `4. Transfer parts from rinse to drying immediately`
  - `5. Inspect for skip plating, roughness, or color variation BEFORE drying`
  - `6. If proceeding to heat treatment: parts must be completely dry`

**Right -- Dimethylamine Safety (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `DIMETHYLAMINE BYPRODUCT` Barlow SemiBold 18 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `DMAB reduction produces dimethylamine ((CH3)2NH)` JetBrains Mono 13 pt `#F0EDE8`
  - `Dimethylamine is:`
  - `Volatile (boils at 7 C -- evaporates readily at room temp)` JetBrains Mono 12 pt `#F0EDE8`
  - `Flammable (flash point -17 C in pure form)` JetBrains Mono 12 pt `#F0EDE8`
  - `Has a strong, fishy/ammonia-like odor` Inter Regular 14 pt `#F0EDE8`
  - `Low hazard in dilute rinse solution but:` Inter Regular 14 pt `#F0EDE8`
  - `Local exhaust ventilation required at rinse station` Inter Medium 14 pt `#E05C5C`
  - `Especially important in enclosed or poorly ventilated areas` Inter Regular 13 pt `#F0EDE8`
  - `OSHA PEL for dimethylamine: 10 ppm TWA` JetBrains Mono 13 pt `#E8A020`

---

### ZONE 6 -- Defect Grid

**Section label:** `POST-PLATE RINSE DEFECTS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | WATER STAINS | `#E8A020` | Parts air-dried before rinsing; standing water evaporated on surface | Transfer immediately to rinse; do not let parts air-dry |
| R1C2 | FINGERPRINT ETCH | `#E05C5C` | Bare-hand handling of freshly plated EN-B | Wear clean nitrile gloves; use fixtures; train operators |
| R2C1 | SURFACE DISCOLORATION | `#E8A020` | Contaminated rinse water or prolonged air exposure before rinse | Use DI water; minimize transfer time; check rinse quality |
| R2C2 | GALVANIC STAINING | `#E05C5C` | Wet parts stacked or touching dissimilar metals | Do not stack wet; separate parts; use non-metallic fixtures |

Card construction: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" (color per defect).

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, defect color
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- EN Boron -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for EN-B post-plate rinsing. Specific requirements vary by EN-B bath chemistry and application. Consult your process supplier for guidance. Source: General industry knowledge; ASTM B841.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse EN Boron Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The EN-B post-plate rinse poster follows the same handling-focused approach as all electroless post-plate rinse posters. The unique EN-B angle is the dimethylamine byproduct: it is volatile, flammable in pure form, and has a distinctive fish/ammonia odor that operators will notice immediately. The safety callout in Zone 5 addresses this without alarm -- dimethylamine in dilute rinse solution is low-hazard, but ventilation is important for comfort and OSHA compliance. The sequence diagram in Zone 3 tells the full story from bath exit to drying, reinforcing the "no air-dry, no fingerprints, no stacking" discipline that applies to all electroless post-plate handling.

---

*Alaina -- Poster #277 -- Construction Workup v1.0 -- 2026-04-26*
