---
Project: Plating Posters Inc
Poster Number: 187
Title: "Rinse -- Chromate (Tri) -- Pre-Coat Stage"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.5)"
Technical Source: Pre-coat rinse between deoxidize and trivalent chromate bath. Removes acid and dissolved metals. Transit time critical -- aluminum reoxidizes almost instantly. Stage 4 of 7.
Process Scope: Pre-coat rinse -- Stage 4 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Rinse
  - PreCoat
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #187 -- Construction Workup
## Rinse -- Chromate (Tri) -- Pre-Coat Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 7. The rinse between deoxidize and the trivalent chromate coating bath. Purpose: remove all acid, dissolved metals (Cu, Fe, Si), and fluoride before the coating stage. The critical constraint is TIME -- aluminum reoxidizes almost instantly in water, so transit from deox rinse to chromate bath should be under 5 minutes.

Hero visual: a time-pressure diagram showing the reoxidation clock ticking from the moment the part leaves the deox tank.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse + transit time hero (Block B):** Double rinse tanks with a prominent clock/timer element showing the < 5 minute window. Built with rectangles, arrows, and a timer graphic.
2. **Contamination removal panel (Block D):** What this rinse is removing -- dissolved metals and acid -- and why they must not enter the chromate bath.
3. **"The Reoxidation Clock" callout (Block E):** The single most important teaching point on this poster.
4. **Failure mode strip (Block F):** 4 failures specific to this transition.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE + TRANSIT TIME HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION REMOVAL + REOXIDATION CLOCK (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Pre-Coat -- Stage 4 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Remove the acid. Remove the dissolved metals. Get to the chromate bath in under 5 minutes. The clock is ticking.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Deoxidized aluminum with acid residue  -->  After: Neutral, clean surface entering chromate bath`

---

### ZONE 3 -- Rinse + Transit Time Hero

**Section label:** `THE PRE-COAT RINSE -- AND THE CLOCK` -- Y: 4.4".

**BLOCK B -- Rinse System with Timer**

Y: 5.0" to 14.0".

**Left section -- Double Rinse Tanks (X: 1.5" to 14.0"):**

Two tanks side by side (same construction as Poster #185):
- Tank 1 (Drag-Out): X: 1.5", W: 5.5", H: 6.0", fill `#252B3D`, border 2 pt `#C8D0D8`
- Tank 2 (Final): X: 8.0", W: 5.5", H: 6.0", fill `#252B3D` lighter, border 2 pt `#C8D0D8`

Labels inside tanks:
- `Ambient temp` JetBrains Mono 12 pt `#F0EDE8`
- `30--60 sec per stage` JetBrains Mono 12 pt `#F0EDE8`

Flow arrows showing part movement from deox (left) through both tanks to chromate bath (right).

**Right section -- Reoxidation Timer (X: 15.0" to 23.0"):**

Large timer/clock graphic:
- Circle, X: 17.5", Y: 7.5", diameter 5.0", stroke 4 pt `#E8A020`, fill `#1E2435`
- Large number in center: `< 5` Barlow Condensed ExtraBold 72 pt `#E8A020`
- Below number: `MINUTES` Barlow SemiBold 24 pt `#E8A020`
- Below that: `from deox to chromate` Inter Medium 14 pt `#F0EDE8` at 70%

Timer progression labels (around clock):
- `0 min: Fresh surface` `#27AE60` 12 pt (top)
- `2 min: Oxide reforming` `#E8A020` 12 pt (right)
- `5 min: Significant reoxidation` `#E05C5C` 12 pt (bottom)
- `> 10 min: Re-deox may be required` `#E05C5C` 12 pt (left)

**Bottom callout (Y: 13.5"):**
- `Aluminum is not steel. It reoxidizes in SECONDS. The double rinse and transit to the chromate bath is a race against the clock.`
- Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Contamination Removal + Reoxidation Clock

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- What This Rinse Removes (X: 0.5", W: 11.0"):**

Section label: `WHAT THIS RINSE REMOVES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

Table (Y: 15.3" to 19.5"):

| Contaminant | Source | Why It Must Go |
|---|---|---|
| Acid residue (HNO3, HF) | Deoxidize bath drag-out | Accelerates chromate bath consumption |
| Dissolved copper (Cu2+) | 2xxx/7xxx alloy dissolution | Contaminates chromate bath; dark spots |
| Dissolved iron (Fe) | Steel fixtures or alloy | Bath contamination; discoloration |
| Dissolved silicon (Si) | Cast alloys | Interferes with film formation |
| Fluoride (F-) | HF-containing deoxidizers | Excess F- in chromate bath causes over-attack |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt. Alternating rows.

**Right -- The Reoxidation Problem (X: 12.0", W: 11.5"):**

Section label: `THE REOXIDATION PROBLEM` Barlow Condensed ExtraBold 22 pt `#E8A020`. Y: 14.7".

Callout box: Rounded rect, H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Aluminum forms a native oxide (Al2O3) in SECONDS when exposed to air or water`
- `The deoxidize step removes this oxide -- but it starts reforming immediately`
- `A thin, fresh oxide is acceptable and the chromate bath can work through it`
- `A thick, aged oxide (> 5 min) inhibits the chromate reaction and produces thin or absent coating`

Key rule:
- `RULE: < 5 minutes from last rinse to chromate immersion. No exceptions.`
- Inter Medium 14 pt `#E05C5C`

Practical note:
- `If the line stalls, re-deoxidize rather than hope the coating will take.`
- Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Operating Parameters Table

**Section label:** `OPERATING PARAMETERS` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 20.7".

**Parameter table (Y: 21.3" to 26.3"):**

| Parameter | Value | Notes |
|---|---|---|
| Rinse stages | 2 (double rinse standard) | Single rinse acceptable for non-aerospace |
| Water type | DI or RO preferred | Dissolved metals in tap water transfer to chromate |
| Temperature | Ambient | No heating needed |
| Time per stage | 30--60 sec immersion | Brief -- minimize total transit time |
| Agitation | Mild air or part movement | Aids contaminant removal |
| pH after rinse | 5.5--7.5 (neutral) | Confirms acid removed |
| Max transit to chromate | < 5 minutes | THE critical constraint |
| Conductivity | < 500 uS/cm | Monitor; high = contamination |

Data: JetBrains Mono 12 pt. Alternating rows. "Max transit" row highlighted with `#E8A020` left border.

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 4 TRANSITION FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 26.7".

**4-card row (Y: 27.3" to 32.3"):**

| Card | X | Problem | Cause | Downstream Effect |
|---|---|---|---|---|
| 1 | 0.5" | ACID CARRY-OVER | Poor rinse; single stage; low flow | Accelerated chromate bath depletion |
| 2 | 6.33" | METAL CONTAMINATION | Cu/Fe from deox not rinsed off | Dark spots; uneven chromate film |
| 3 | 12.16" | REOXIDATION | > 5 min transit; line stall | Thin or absent chromate coating |
| 4 | 18.0" | EXCESS FLUORIDE | HF deox residue in carry-over | Over-attack of aluminum in chromate bath |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Downstream: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Chromate (Trivalent) -- Pre-Coat Stage`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Chromate Tri Pre-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The timer/clock graphic in Zone 3 is the hero element -- it makes the time constraint visceral. This is a rinse poster, but the teaching point is really about transit time management. The reoxidation problem is unique to aluminum and must be communicated clearly. This differentiates aluminum chromate processing from steel-based processes where time between stages is more forgiving.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #187 -- Construction Workup v1.0*
*2026-04-26*
