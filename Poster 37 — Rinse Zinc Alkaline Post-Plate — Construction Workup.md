---
Project: Plating Posters Inc
Poster Number: 37
Title: "Rinse -- Zinc (Alkaline) -- Post-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Post-plate rinse for alkaline zinc plating line (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #37 -- Construction Workup
## Rinse -- Zinc (Alkaline) -- Post-Plate

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 6 of 8. The most critical rinse in the entire line. This rinse removes caustic drag-out from the zinc bath before the parts enter the passivate tank. If any NaOH residue reaches the passivate (pH 3.5--4.5), it neutralizes the acid, kills the conversion coating, and ruins the corrosion protection.

Hero visual: a "consequences chain" -- what happens at the passivate when this rinse fails, shown as a visual damage cascade.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Consequences chain hero (Block B):** A top-to-bottom cascade diagram: good rinse (green path) vs. bad rinse (red path), ending at the passivate tank. Shows pH values at each point.
2. **Drag-out volume callout (Block E):** How much caustic is carried out per rack/barrel.
3. **Orientation strip:** Stage 6 highlighted.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted
ZONE 3 -- CONSEQUENCES CHAIN HERO (4.2"--14.5")
ZONE 4 -- RINSE PARAMETERS + DRAG-OUT (14.5"--21.5")
ZONE 5 -- COMMON PROBLEMS (21.5"--27.5")
ZONE 6 -- MONITORING + SAFETY (27.5"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. Y: 0.5".
**Subheading:** `Zinc (Alkaline) -- Post-Plate -- Stage 6 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".
**Tagline:** `The most critical rinse on the line. Caustic on parts will kill the passivate. Every second counts.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`. Others dimmed.
Below: `Before: Freshly zinc-plated surface (alkaline, pH > 12)  -->  After: Neutral zinc surface ready for passivate`

---

### ZONE 3 -- Consequences Chain Hero

**Section label:** `WHY THIS IS THE MOST CRITICAL RINSE` -- Y: 4.4".

**BLOCK B -- Two-Path Consequences Diagram**

Y: 5.0" to 14.0". Two vertical paths (good and bad), ending at the passivate stage.

**Left path -- GOOD RINSE (X: 0.5", W: 11.0"):**
- Title: `PROPER POST-PLATE RINSE` Barlow SemiBold 18 pt `#27AE60`
- 4 stacked boxes connected by downward arrows (`#27AE60`):

| Step | Content | pH Label |
|---|---|---|
| 1 | Parts exit zinc bath | pH > 12.5 |
| 2 | Multi-stage cascade rinse, 30--60 sec/stage | pH dropping |
| 3 | Final rinse: neutral, clean surface | pH 6--8 |
| 4 | Parts enter passivate | pH 3.5--4.5 MAINTAINED |

Box 4 has Emerald border to emphasize success.

**Right path -- BAD RINSE (X: 12.5", W: 11.0"):**
- Title: `INADEQUATE POST-PLATE RINSE` Barlow SemiBold 18 pt `#E05C5C`
- 4 stacked boxes with `#E05C5C` arrows:

| Step | Content | pH Label |
|---|---|---|
| 1 | Parts exit zinc bath | pH > 12.5 |
| 2 | Quick single rinse, parts still alkaline | pH 10+ on surface |
| 3 | Alkaline surface enters passivate | NaOH neutralizes acid |
| 4 | Passivate FAILS: pH rises, no conversion coating | CORROSION FAILURE |

Box 4 has Coral border + `#E05C5C` fill at 15% for danger emphasis.

**Center annotation (between the two paths):**
- Vertical text or centered label: `THE CRITICAL VARIABLE: RINSE THOROUGHNESS` Barlow Condensed ExtraBold 16 pt `#E8A020`

**Bottom impact line (Y: 13.5"):**
- `A passivate bath that rises from pH 4.0 to pH 5.5 due to NaOH drag-in produces ZERO corrosion protection. The parts fail salt spray.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Parameters + Drag-Out

**Section label:** `POST-PLATE RINSE PARAMETERS` -- Y: 14.7".

**Left -- Parameter Table (X: 0.5", W: 14.0"):**

| Parameter | Value |
|---|---|
| Water type | DI strongly recommended |
| Temperature | Ambient |
| Stages | 3-stage cascade MINIMUM |
| Flow rate | 3--5 gal/min per stage |
| Immersion time | 30--60 sec per stage |
| Agitation | Air + part movement (both) |
| Conductivity target | < 100 uS/cm (tightest in the line) |
| pH target | 6--8 at final stage |
| Drain time | 15--20 sec (longer than other rinses) |

**Right -- Drag-Out Callout (X: 15.0", W: 8.5"):**
- Title: `DRAG-OUT ECONOMICS` Barlow SemiBold 18 pt `#E8A020`
- Body:
  - `Drag-out from the zinc bath: ~1--3 gal per 1000 ft2`
  - `Zinc bath concentration: ~140 g/L NaOH`
  - `Each rack carries ~50--150 mL of bath solution`
  - `That's 7--21 grams of NaOH per rack going into the rinse`
  - `Multiply by 50 racks/shift = 350--1050 g NaOH in rinse water`
- Conclusion: `If rinse is inadequate, this NaOH accumulation enters the passivate and destroys it.` Inter Medium 13 pt `#E05C5C`
- Tip: `Spray rinse nozzles at the exit of the zinc tank dramatically reduce drag-out volume.` Inter Medium 12 pt `#27AE60`

---

### ZONE 5 -- Problems

**Section label:** `WHAT GOES WRONG AT THE POST-PLATE RINSE` -- Y: 21.7".

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Passivate failure | No chromate color; parts fail salt spray | NaOH carry-over neutralizing passivate | Add rinse stages; spray rinse at zinc exit |
| White haze on zinc | Cloudy appearance before passivate | Zinc hydroxide forming in alkaline rinse | Ensure rinse water is neutral; change water |
| Passivate pH rising | Must add acid constantly to passivate | Drag-out overwhelming the rinse | Improve rinse efficiency; longer drain time |
| Staining/streaks | Uneven passivate color | Localized alkaline residue (recesses, blind holes) | Air agitation; extend rinse time; spray nozzles |
| Water spots | Marks after drying | Hard water in rinse | Use DI for final stage |

---

### ZONE 6 -- Monitoring + Safety

**Left -- Monitoring (X: 0.5", W: 11.0"):**
- Title: `CRITICAL MONITORING` `#2EC4B6`
- `Conductivity: check EVERY HOUR -- this rinse degrades fastest`
- `pH paper: dip test at final stage -- must read 6--8`
- `Passivate bath pH: if it's drifting up, the rinse is failing`
- `Dump schedule: when conductivity > 300 uS/cm or pH > 9`
- `Track rinse water consumption vs. passivate acid additions -- they correlate`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY -- ALKALINE RINSE WATER` `#E8A020`
- `Rinse water contains NaOH from drag-out -- pH may be 9--11`
- `Burns are possible from concentrated drag-out splashes`
- `All overflow to waste treatment -- pH adjustment required before discharge`
- `Standard PPE: goggles, gloves, apron`
- `Posted SDS for all zinc bath chemicals`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Zinc (Alkaline) -- Post-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 standard zones.
**Light Remap:** Standard table. Danger emphasis fill (`#E05C5C` at 15% -> `#B83E3E` at 10%).
**Export:** Six files -- `Rinse Zinc Alkaline Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Elara -- Poster #37 -- Construction Workup v1.0 -- 2026-04-25*
