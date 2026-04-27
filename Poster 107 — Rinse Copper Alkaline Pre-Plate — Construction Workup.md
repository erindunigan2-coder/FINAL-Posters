---
Project: Plating Posters Inc
Poster Number: 107
Title: "Rinse -- Copper (Alkaline) -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Pre-plate rinse for alkaline non-cyanide copper plating line (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CopperPlating
  - AlkalineCopper
  - NonCyanide
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP10
---

# Poster #107 -- Construction Workup
## Rinse -- Copper (Alkaline) -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of the alkaline non-cyanide copper process. This rinse sits between acid activation and the alkaline copper strike bath -- and its job is more critical than it looks. Acid drag-in to the alkaline copper bath lowers pH, decomposes the complexant (HEDP, citrate, or pyrophosphate), and can cause immersion copper deposition on active metals like steel and zinc die castings. That immersion layer is non-adherent garbage -- it destroys the entire purpose of the alkaline strike.

The rinse must be fast (especially for zinc die castings -- every second of exposure to air after activation risks re-oxidation) and thorough (no acid carry-over into a pH 8--13 bath).

Hero visual: cascade rinse tank diagram with acid drag-in consequence callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Standard 2-tank cascade with drag-in consequence callout.
2. **Orientation strip:** Stage 4 highlighted.
3. **Rinse parameter table + acid drag-in callout.**
4. **Problems and safety/water quality panels.**

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
ZONE 4 -- RINSE PARAMETERS + ACID DRAG-IN (14.5"--21.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Alkaline) -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".

**Tagline:** `Acid drag-in destroys the complexant and drops the pH. One contaminated load can immersion-plate every part in the strike tank.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted (fill `#2EC4B6`). Others dimmed.

Below strip: `Before: Acid-activated surface  -->  After: Acid-free, ready for alkaline copper strike`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE PRE-PLATE RINSE -- PROTECTING THE ALKALINE BATH` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 10.5". Two-tank counter-current cascade. Same visual pattern as Poster #105.

Tank 1 (Acid-contaminated): tinted `#E05C5C` at 10%. Tank 2 (Clean): tinted `#2EC4B6` at 10%.

Parts travel left to right. Water flows right to left.

Key labels:
- Tank 1: `Captures acid drag-out from activation`
- Tank 2: `Clean rinse -- parts exit near-neutral pH`
- Exit arrow: `TO ALKALINE COPPER STRIKE -- FAST` `#27AE60`

Key metrics (Y: 11.0"):
- `Target: pH 6--8 on rinse water at exit. No acid carry-over to the alkaline bath.`
- `For zinc die castings: minimize air exposure after rinse. Enter strike within 30 sec.`

**BLOCK B2 -- Acid Drag-In Consequence Callout**

Y: 11.5" to 14.0".

Rounded rect, full width, H: 2.2", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8.
Title: `WHAT HAPPENS WHEN ACID REACHES THE ALKALINE COPPER BATH` Barlow Condensed ExtraBold, 20 pt, `#E05C5C`

Three-column interior:

**Column 1 -- pH Drop:**
- `Acid lowers bath pH below operating range`
- `At pH < 8: copper complexant breaks down`
- `Free copper ions appear in solution`
JetBrains Mono 11 pt `#F0EDE8`

**Column 2 -- Immersion Copper:**
- `Free Cu2+ plates immersion copper on steel/zinc`
- `Immersion deposit = non-adherent`
- `Entire load fails adhesion test`
JetBrains Mono 11 pt `#E05C5C`

**Column 3 -- Bath Damage:**
- `Complexant decomposition is NOT reversible`
- `Bath may need partial dump and rebuild`
- `Expensive -- and production stops`
JetBrains Mono 11 pt `#E8A020`

---

### ZONE 4 -- Rinse Parameters + Acid Drag-In

**Section label:** `RINSE PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

| Parameter | Value |
|---|---|
| Water type | DI preferred; city water acceptable |
| Temperature | Ambient |
| Flow rate | 2--5 gal/min per stage |
| Stages | 2 cascade minimum |
| Immersion time | 15--30 sec (all substrates) |
| Agitation | Air or part movement |
| Conductivity target | < 500 uS/cm at exit tank |
| Drain time | 10--15 sec |
| Rinse criterion | pH 6--8 (paper check) |

**Right -- Transfer Speed Callout (X: 15.0", W: 8.5"):**

Title: `SPEED MATTERS` -- Barlow SemiBold 18 pt `#E8A020`

Rounded rect, fill `#1E2435`, left accent `#E8A020`:

Body:
> After acid activation and rinsing, the activated surface begins to re-oxidize immediately on contact with air. For zinc die castings, the window is extremely tight:
>
> - Rinse: 15--30 sec
> - Drain: 10 sec
> - Into the copper strike: within 30 sec of exiting rinse
>
> Total activation-to-strike time: under 90 seconds.

Inter Regular 13 pt `#F0EDE8`. Timing values: JetBrains Mono 14 pt `#E8A020`.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-PLATE RINSE` -- Y: 21.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Acid drag-in to copper bath | pH drops; immersion copper on parts | Insufficient rinsing or skipped stage | Add rinse stage; increase flow rate |
| Re-oxidation on zinc DC | White haze; poor copper adhesion | Slow transfer after rinse | Enter copper strike within 30 sec |
| Spotting/mineral deposits | White spots under copper deposit | Hard water minerals | Switch to DI water |
| Contaminated rinse water | Copper residue on parts before strike | Rinse tank not dumped; copper drag-back from strike | Dump/refresh rinse; check tank flow direction |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

Same two-panel layout as Poster #105.

**Left -- Water Quality:** DI vs. city water, conductivity monitoring, pH spot-check, dump criteria.
**Right -- Safety:** Mildly acidic rinse water (residual HCl/H2SO4), copper compounds in drag-back, wet floor hazard, waste treatment routing.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Copper (Alkaline) -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table (see Poster #103). **Export:** Six files -- `Rinse Copper Alkaline Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster's unique angle is the acid drag-in consequence callout (Block B2). Acid contamination of an alkaline copper bath is catastrophic in a way that acid contamination of, say, an acid zinc bath is not -- because the alkaline complexant system is pH-dependent and breaks down irreversibly. The three-column "what happens" layout makes the cascade of consequences visually clear: pH drops -> immersion copper forms -> bath needs rebuilding.

The transfer speed callout mirrors Poster #106's urgency for zinc die castings -- under 90 seconds from activation to strike. This isn't paranoia; it's physics. Clean zinc re-oxidizes fast.

Watson's brief: "Pre-plate: Single overflow minimum. Must remove all acid from activation before entering alkaline copper bath."

---

*Alaina -- Poster #107 -- Construction Workup v1.0 -- 2026-04-26*
