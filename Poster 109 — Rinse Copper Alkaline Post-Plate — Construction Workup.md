---
Project: Plating Posters Inc
Poster Number: 109
Title: "Rinse -- Copper (Alkaline) -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-plate rinse for alkaline non-cyanide copper plating line (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CopperPlating
  - AlkalineCopper
  - NonCyanide
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP10
---

# Poster #109 -- Construction Workup
## Rinse -- Copper (Alkaline) -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of the alkaline non-cyanide copper process. The post-plate rinse removes alkaline copper bath chemistry from the freshly plated surface before the part moves to its next destination -- which is almost always another plating bath (acid copper, nickel, or chromium). Copper drag-out is a contamination concern for every downstream process: copper in a nickel bath causes dark deposits; copper in a chrome bath is devastating.

The alkaline nature of the drag-out also matters. If the next step is an acid dip or acid copper bath, the alkaline film must be fully removed to prevent localized pH spikes that cause staining or adhesion problems at the copper/next-layer interface.

Double counterflow rinse is the minimum. DI water is preferred if proceeding to sensitive downstream chemistry.

Hero visual: cascade rinse diagram with downstream contamination consequence callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Standard 2--3 tank cascade.
2. **Downstream contamination callout (Block C):** What copper drag-out does to next baths.
3. **Orientation strip:** Stage 6 highlighted (Teal).
4. **Rinse parameters + problems + safety panels.**

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
  Stage 6 highlighted
ZONE 3 -- CASCADE RINSE HERO + CONTAMINATION CALLOUT (4.2"--14.5")
ZONE 4 -- RINSE PARAMETERS + DRAG-OUT (14.5"--21.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Alkaline) -- Post-Plate -- Stage 6 of 8` -- 32 pt `#2EC4B6`. Y: 1.5".

**Tagline:** `Copper drag-out is a contaminant in every downstream bath. Rinse it off here or deal with it in the nickel, the chrome, or the waste treatment -- your choice.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted (fill `#2EC4B6`). Others dimmed.

Below strip: `Before: Freshly plated copper surface with alkaline bath drag-out  -->  After: Clean copper surface ready for next step`

---

### ZONE 3 -- Cascade Rinse Hero + Contamination Callout

**Section label:** `THE POST-PLATE RINSE -- REMOVING COPPER DRAG-OUT` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 10.0". Two- or three-tank counter-current cascade. Same visual pattern as Poster #105.

Tank 1 (Copper-contaminated): tinted `#E8A020` at 10%. Tank 2 (Middle): neutral. Tank 3 (Clean): tinted `#2EC4B6` at 10%.

Parts travel left to right. Water flows right to left.

Key labels:
- Tank 1: `Captures alkaline copper drag-out`
- Tank 2: `Intermediate rinse`
- Tank 3: `Clean rinse -- parts exit copper-free`
- Exit arrow: `TO NEXT STEP (acid dip, acid Cu, Ni, or anti-tarnish)` `#27AE60`

Key metrics (Y: 10.5"):
- `Target: < 200 uS/cm at final stage. No visible copper residue in rinse water.`

**BLOCK C -- Downstream Contamination Callout**

Y: 11.0" to 14.0".

Rounded rect, full width, H: 2.8", fill `#E8A020` at 10%, border 2 pt `#E8A020`, radius 8.
Title: `WHERE COPPER DRAG-OUT CAUSES PROBLEMS DOWNSTREAM` Barlow Condensed ExtraBold, 20 pt, `#E8A020`

Four-column interior (each a mini-card):

**Col 1 -- Acid Copper Bath:**
- `Alkaline carry-over raises pH locally`
- `Minimal concern -- Cu is native`
- Risk: `LOW` `#27AE60`

**Col 2 -- Nickel Bath:**
- `Cu contamination > 50 ppm: dark deposits, pitting`
- `Copper plates out on anodes and re-dissolves unpredictably`
- Risk: `HIGH` `#E05C5C`

**Col 3 -- Chrome Bath:**
- `Cu > 200 ppm: discoloration, dark spots`
- `Removal: dummy plate or porous pot`
- Risk: `HIGH` `#E05C5C`

**Col 4 -- Waste Treatment:**
- `Chelant carry-over (HEDP, pyrophosphate) keeps Cu in solution through hydroxide precip`
- `May need sulfide precip or IX`
- Risk: `MODERATE` `#E8A020`

JetBrains Mono 10 pt `#F0EDE8` for body. Risk labels: Inter Medium 12 pt.

---

### ZONE 4 -- Rinse Parameters + Drag-Out

**Section label:** `RINSE PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

| Parameter | Value |
|---|---|
| Water type | DI preferred (especially before nickel or chrome) |
| Temperature | Ambient |
| Flow rate | 2--5 gal/min per stage |
| Stages | 2--3 cascade (double counterflow minimum) |
| Immersion time | 30--60 sec per stage |
| Agitation | Air or part movement |
| Conductivity target | < 200 uS/cm at final stage |
| Drain time | 10--15 sec |
| Rinse criterion | No visible blue-green tint in final tank |

**Right -- Drag-Out Recovery Callout (X: 15.0", W: 8.5"):**

Title: `DRAG-OUT RECOVERY` -- Barlow SemiBold 18 pt `#E8A020`

Rounded rect, fill `#1E2435`, left accent `#E8A020`:

Body:
> Alkaline copper baths are expensive -- the complexant chemistry costs more than simple salt baths. A static drag-out recovery tank before the rinse cascade can return concentrated chemistry to the plating bath, reducing chemical consumption and waste treatment load.
>
> Recovery tank: static, no overflow. Return solution to plating bath periodically. Monitor for contamination buildup.

Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE POST-PLATE RINSE` -- Y: 21.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Copper carry-over to nickel | Dark nickel deposits, pitting | Insufficient rinsing; skipped stages | Add rinse stage; check flow rate |
| Chelant carry-over to waste treatment | Copper not precipitating in waste treatment | HEDP/pyro in rinse water complexes Cu | Segregate copper rinse water; sulfide precip |
| Alkaline carry-over to acid dip | Localized pH spike at copper surface | Insufficient rinsing | Extend rinse time or add stage |
| Copper tarnishing in rinse | Orange/brown discoloration on copper surface | Hot rinse water + air exposure; long soak | Use ambient water; minimize rinse time |
| Rinse tank turning blue-green | Heavy copper drag-out | Bath viscosity high; poor drain time | Increase drain time; check bath concentration |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

Same two-panel layout as Poster #105.

**Left -- Water Quality:** DI vs. city water, conductivity monitoring, copper spot-check (visual or colorimetric), dump criteria.

**Right -- Safety:**
- Alkaline rinse water (pH 8--10 initially): mild irritant
- Copper compounds in rinse water: aquatic toxicity -- route to waste treatment
- Wet floor hazard
- Chelant-containing water must not bypass waste treatment -- chelants prevent copper precipitation

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Copper (Alkaline) -- Post-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table (see Poster #103). **Export:** Six files -- `Rinse Copper Alkaline Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The downstream contamination callout (Block C) is this poster's unique value. Most rinse posters focus on the rinse itself -- this one looks forward to what happens if the rinse fails. The four-column risk assessment (acid copper = low, nickel = high, chrome = high, waste treatment = moderate) gives operators an immediate reason to care about rinse quality. It's not abstract; it's "copper in your nickel bath means dark deposits."

The chelant carry-over to waste treatment is a subtlety that many shops miss. HEDP and pyrophosphate are chelants -- they hold copper in solution through standard hydroxide precipitation. If rinse water containing these chelants goes to the waste treatment system, the copper won't precipitate. This is a compliance issue.

Watson's brief: "Post-plate: Double counterflow. If proceeding to acid copper, an acid dip (5--10% H2SO4) follows the post-copper rinse to neutralize alkaline film." "HEDP and pyrophosphate are chelants -- they keep copper in solution through standard hydroxide precipitation."

---

*Alaina -- Poster #109 -- Construction Workup v1.0 -- 2026-04-26*
