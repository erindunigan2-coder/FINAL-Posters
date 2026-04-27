---
Project: Plating Posters Inc
Poster Number: 35
Title: "Rinse -- Zinc (Alkaline) -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Pre-plate rinse for alkaline zinc plating line (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #35 -- Construction Workup
## Rinse -- Zinc (Alkaline) -- Pre-Plate

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 4 of 8. The second rinse in the line -- between acid activation and the zinc plating tank. Its job: remove every trace of acid so the alkaline zinc bath stays healthy. Acid drag-in is the most common source of zinc bath contamination from the pre-treatment side.

Hero visual: a "contamination pathway" diagram showing how acid carry-over affects the zinc bath -- a visual cause-and-effect chain.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Contamination pathway hero (Block B):** A horizontal cause-and-effect chain: acid on parts -> enters rinse -> if rinse fails -> acid enters zinc bath -> pH drop -> zinc metal precipitation -> rough/dull deposit. Built as connected rounded rectangles with arrows, color-coded green (good path) vs. red (contamination path).
2. **Orientation strip (Block C):** Stage 4 highlighted.
3. **Parameter table (Block D):** Rinse-specific parameters (similar structure to Poster #33 but focused on the acid-to-alkaline transition).
4. **Acid-Alkaline interface callout (Block E):** Explains the chemistry of why this rinse is particularly critical.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted
ZONE 3 -- CONTAMINATION PATHWAY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + INTERFACE CALLOUT (14.5"--21.5" / ~7.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.5"--27.5" / ~6.0")
ZONE 6 -- MONITORING + SAFETY (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Zinc (Alkaline) -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".
**Tagline:** `The last line of defense before the plating tank. Acid drag-in is the #1 contamination source.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Acid-activated surface (pH ~1)  -->  After: Neutral surface ready for alkaline zinc bath`

---

### ZONE 3 -- Contamination Pathway Hero

**Section label:** `WHAT HAPPENS IF THIS RINSE FAILS` -- Y: 4.4".

**BLOCK B -- Two-Path Diagram**

Y: 5.0" to 14.0". Two parallel horizontal pathways:

**Top path -- GOOD (Y: 5.0" to 8.5"):**
- Label: `GOOD RINSE PATH` -- Barlow SemiBold 18 pt `#27AE60`
- 4 connected boxes (rounded rect, W: 5.0", H: 2.5", fill `#1E2435`, top accent `#27AE60`):

| Box | Text |
|---|---|
| 1 | `Parts exit activation` / `pH ~1 on surface` |
| 2 | `Thorough rinse` / `30--60 sec, flowing water` |
| 3 | `Clean neutral surface` / `pH 6--8, no acid residue` |
| 4 | `Zinc bath stays healthy` / `Consistent deposit quality` |

Arrows between boxes: 3 pt `#27AE60`, right-pointing.

**Bottom path -- BAD (Y: 9.5" to 13.0"):**
- Label: `CONTAMINATION PATH` -- Barlow SemiBold 18 pt `#E05C5C`
- 4 connected boxes (fill `#1E2435`, top accent `#E05C5C`):

| Box | Text |
|---|---|
| 1 | `Parts exit activation` / `pH ~1 on surface` |
| 2 | `Inadequate rinse` / `Too fast, stagnant water` |
| 3 | `Acid enters zinc bath` / `pH drops, NaOH consumed` |
| 4 | `Bath problems` / `Dull, rough, poor throwing power` |

Arrows: 3 pt `#E05C5C`, right-pointing.

**Divider between paths:**
- Dashed horizontal line, `#3A4055`, 1 pt
- Center label: `THE DIFFERENCE: 30 SECONDS OF PROPER RINSING` -- Barlow Condensed ExtraBold 16 pt `#E8A020`

**Impact callout (below paths, Y: 13.5"):**
- Rounded rect, full width, H: 0.8", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `Every 1 mL of concentrated HCl dragged into a 100-gal zinc bath consumes ~0.4 g NaOH. Cumulative drag-in can drop caustic concentration measurably over a shift.` -- Inter Medium 13 pt `#F0EDE8`

---

### ZONE 4 -- Parameters + Interface Callout

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Parameter Table (X: 0.5", W: 14.0"):**

| Parameter | Value |
|---|---|
| Water type | DI preferred; city acceptable |
| Temperature | Ambient |
| Flow rate | 2--5 gal/min per stage |
| Stages | 2--3 cascade (same as pre-activation rinse) |
| Immersion time | 30--60 sec per stage |
| Agitation | Air or part movement |
| Conductivity target | < 200 uS/cm (tighter than pre-activation) |
| pH target | 6--8 at final stage |
| Drain time | 10--15 sec |

**Right -- Acid-Alkaline Interface Callout (X: 15.0", W: 8.5"):**
- Rounded rect fill `#1E2435`, left accent `#E8A020`
- Title: `THE ACID-TO-ALKALINE TRANSITION` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 14 pt, line height 150%):

> This is the most chemically aggressive transition in the zinc line.
>
> Acid activation: pH ~1
> Zinc bath: pH > 12.5
>
> That is a 100-billion-fold difference in hydrogen ion concentration. Any acid residue on parts will react violently with the caustic in the zinc bath, generating heat and consuming NaOH.
>
> The rinse must bridge this gap completely.

Key metric: `Tighter conductivity target here (< 200 uS/cm) vs. pre-activation (< 500)` -- JetBrains Mono 12 pt `#E8A020`.

---

### ZONE 5 -- Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-PLATE RINSE` -- Y: 21.7".

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Acid carry-over | Low caustic in zinc bath; poor throwing power | Rinse too brief or stagnant | Extend rinse; add cascade stage |
| Rough zinc deposit | Roughness in LCD areas | Iron dissolved in acid carried into bath | Improve rinse; dump/replace activation acid periodically |
| Chloride contamination | Pitting in zinc deposit | HCl residue entering the bath | Cascade rinse to < 200 uS/cm; use H2SO4 activation instead |
| Flash rust | Orange tint on parts at zinc tank entry | Delay between rinse and plating | Immediate transfer; keep parts wet |

---

### ZONE 6 -- Monitoring + Safety

**Left -- Monitoring (X: 0.5", W: 11.0"):**
- Title: `DAILY MONITORING` Barlow SemiBold 18 pt `#2EC4B6`
- Bullets:
  - `Conductivity meter: check final rinse every 2 hours`
  - `pH paper: quick check -- should read 6--8`
  - `Visual: rinse water should be clear, not yellow (iron)`
  - `Dump schedule: when conductivity > 500 uS/cm or pH < 5`
  - `Log readings: trend tracking catches slow degradation`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` Barlow SemiBold 18 pt `#E8A020`
- Bullets:
  - `Rinse water is acidic from drag-out -- handle accordingly`
  - `Rinse overflow to waste treatment -- never to storm drain`
  - `Wet floors: slip hazard`
  - `If rinse water turns yellow: iron content high -- change water`
  - `Standard PPE: goggles, gloves, apron`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Zinc (Alkaline) -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** Standard 7-zone groups.

**Light Remap:** Standard table (same as all EP-01).

**Export:** Six files -- `Rinse Zinc Alkaline Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Elara -- Poster #35 -- Construction Workup v1.0 -- 2026-04-25*
