---
Project: Plating Posters Inc
Poster Number: 225
Title: "Rinse -- EN (Mid Phos) -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 3)"
Process Scope: Pre-activation rinse for electroless nickel mid phosphorus line (Stage 2 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #225 -- Construction Workup
## Rinse -- EN (Mid Phos) -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of the EN Mid-P process. Identical rinse function to EN Low-P (Poster #217): remove alkaline cleaner drag-out before acid activation. The chemistry does not change between EN-P classes at this stage -- the rinse stands between alkaline cleaning and acid activation regardless of which bath follows downstream. For aluminum substrates headed to zincate, inadequate rinsing causes uncontrolled etching and surface roughness.

Hero visual: cascade rinse tank diagram showing counter-current water flow, drag-out dilution, and conductivity monitoring. Mirrors Poster #217 structure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Two or three connected tanks in cross-section with counter-current water flow arrows.
2. **Orientation strip (Block C):** 7-stage strip, Stage 2 highlighted.
3. **Rinse parameter table (Block D):** Focused on rinse-specific parameters.
4. **Drag-out/carry-over callout (Block E):** Why rinsing matters between alkaline and acid chemistries.
5. **Problems table and safety/water quality callout.**

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Standard locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETER TABLE (14.5"--21.0" / ~6.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0" / ~6.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `EN (Mid Phos) -- Pre-Activation -- Stage 2 of 7` -- Barlow SemiBold, 32 pt, `#2EC4B6`. X: 0.5", Y: 1.5".

**Tagline:** `The bridge between alkaline and acid. Alkaline drag-in neutralizes the activation bath. For aluminum, it causes uncontrolled etching before zincate.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.2".

---

### ZONE 2 -- Sequence Orientation Strip

Same 7-stage strip as Poster #224 but **Stage 2 highlighted** (fill `#2EC4B6`, 100%). All others dimmed.

Below strip: `Before: Alkaline-cleaned surface (pH ~12)  -->  After: Neutral surface ready for acid activation`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE CASCADE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 14.0". Three connected tank cross-sections -- 3-stage counter-current cascade.

**Tank 1 (Dirty Rinse) -- X: 0.5", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior tinted `#E8A020` at 10% (alkaline contamination)
- Label: `STAGE 1 (DIRTY)` -- Barlow SemiBold 16 pt `#E8A020`
- Inside: `Highest drag-in concentration` -- Inter Regular 13 pt at 60%
- Overflow arrow down to `DRAIN`

**Tank 2 (Middle Rinse) -- X: 8.0", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `STAGE 2 (MIDDLE)` -- Barlow SemiBold 16 pt `#F0EDE8`
- Overflow arrow left into Tank 1

**Tank 3 (Clean Rinse) -- X: 15.5", W: 7.0", H: 7.5":**
- Fill `#252B3D` with `#2EC4B6` tint at 10%
- Label: `STAGE 3 (CLEAN)` -- Barlow SemiBold 16 pt `#2EC4B6`
- Fresh water inlet from right: `FRESH WATER IN` JetBrains Mono 12 pt `#2EC4B6`
- Overflow left into Tank 2

**Parts movement:** Arrow below tanks, LEFT to RIGHT. `PARTS TRAVEL -->` Barlow SemiBold 14 pt.
**Water flow:** Arrow above tanks, RIGHT to LEFT. `<-- WATER FLOW (counter-current)` Barlow SemiBold 14 pt `#2EC4B6`.

**Key metrics callout (Y: 13.0"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.0", fill `#1E2435`, border-left 0.06" `#2EC4B6`
- `A 3-stage cascade uses 90% less water than a single flowing rinse for the same dilution ratio. Target: < 50 uS/cm conductivity at final stage.`

---

### ZONE 4 -- Rinse Parameter Table

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

Header: `PRE-ACTIVATION RINSE` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Water type | DI or RO preferred; municipal < 200 ppm TDS |
| Temperature | Ambient (18-30 C / 65-85 F) |
| Flow rate | 2-5 gal/min per stage |
| Stages | 2-3 stage counterflow recommended |
| Immersion time | 30-60 sec per stage |
| Agitation | Air or part movement |
| Conductivity target | < 50 uS/cm in final stage |
| Drain time | 10-15 sec between tanks |

**Right -- Drag-Out Callout (X: 15.0", W: 8.5"):**

- Title: `WHY THIS RINSE MATTERS` -- Barlow SemiBold, 18 pt, `#E8A020`

> Alkaline cleaner (pH 11-13) is dragged into the rinse on every rack or barrel. If this residue reaches the acid activation tank, it neutralizes the acid -- raising pH, weakening activation, leaving oxide on the parts.
>
> For aluminum headed to zincate: residual alkaline causes uncontrolled etching and surface roughness that ruins adhesion.
>
> Result: skip plating in the EN bath.

Key metric: `Drag-out rate: ~0.5-2.0 gal per 1000 ft2 of surface` JetBrains Mono 12 pt `#2EC4B6`.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-ACTIVATION RINSE` -- Y: 21.2".

**4-Row Problem Table:**

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Alkaline carry-over | Acid activation neutralized; poor oxide removal | Insufficient rinse stages or time | Add cascade stage; increase flow |
| High conductivity | Parts still alkaline entering activation | Rinse water exhausted or flow too low | Monitor conductivity; increase water |
| Spotting/staining | White mineral deposits on parts | Hard water (Ca, Mg) | Switch to DI water |
| Aluminum surface roughness | Etched, matte appearance before zincate | Alkaline residue attacking aluminum in rinse | Reduce drain time from cleaner; improve flow |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

**Section label:** `WATER QUALITY & SAFETY` -- Y: 27.2".

**Left -- Water Quality (X: 0.5", W: 11.0"):**
- Title: `WATER QUALITY MATTERS` -- Barlow SemiBold 18 pt `#2EC4B6`
- `DI water: < 10 uS/cm -- best for critical EN work`
- `City water: 200-600 uS/cm -- acceptable for most substrates`
- `Hard water: > 300 ppm CaCO3 -- risk of spotting and contamination drag-in to EN bath`
- `Monitor final rinse conductivity daily`
- `Dump and refill when conductivity exceeds 500 uS/cm`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` -- Barlow SemiBold 18 pt `#E8A020`
- `Rinse water is mildly alkaline from drag-out -- handle accordingly`
- `Rinse overflow goes to waste treatment -- not down the drain`
- `Wet floors: slip hazard -- maintain drainage and mats`
- `pH check rinse water periodically -- should be near neutral (6-8)`

---

### ZONE 7 -- Footer Band

Standard footer. Title: `Rinse -- EN (Mid Phos) -- Pre-Activation`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for pre-activation rinsing in electroless nickel mid phosphorus (5-9% P) plating lines. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones per standard structure.
**Light Remap:** Standard table (same as Poster #215).
**Export:** Six files -- `Rinse EN Mid-P Pre-Act -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #225 -- Construction Workup v1.0 -- 2026-04-26*
