---
Project: Plating Posters Inc
Poster Number: 241
Title: "Rinse -- Electroless Copper -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 3)"
Process Scope: Pre-activation rinse for electroless copper line (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #241 -- Construction Workup
## Rinse -- Electroless Copper -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of the electroless copper process. This rinse sits between the cleaner/conditioner (and permanganate desmear for multilayer PCBs) and the Sn/Pd activation sequence. The critical concern is unique to E-Cu: residual permanganate or other oxidizer poisons the expensive Pd catalyst downstream. MnO2 residues from incomplete neutralization are equally fatal -- they create a barrier layer that prevents Pd adsorption on the dielectric surface.

Hero visual: cascade rinse diagram with oxidizer contamination threat callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** DI counterflow with oxidizer threat callout.
2. **Orientation strip (Block C):** 8-stage strip, Stage 2 highlighted.
3. **Rinse parameter table (Block D).**
4. **Oxidizer contamination panel (Block E):** Why permanganate/MnO2 residue is fatal to Pd catalyst.
5. **Problems table + safety.**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + OXIDIZER THREAT (14.5"--21.0" / ~6.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0" / ~6.0")
ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Pre-Activation -- Stage 2 of 8` -- Barlow SemiBold, 32 pt, `#2EC4B6`. X: 0.5", Y: 1.5".

**Tagline:** `Residual oxidizer poisons the Pd catalyst. MnO2 residue blocks catalyst adsorption. This rinse protects the most expensive step in the line.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.2".

---

### ZONE 2 -- Orientation Strip

8-stage strip. Stage 2 highlighted (fill `#2EC4B6`, 100%). All others dimmed. Labels match Poster #240 strip.

Below: `Before: Cleaned/desmeared surface with alkaline/oxidizer residue  -->  After: Neutral surface ready for acid pre-dip and Pd catalyst`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE PRE-ACTIVATION CASCADE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 12.0". Three connected tank cross-sections per standard cascade pattern.

**Tank 1 (Dirty) -- X: 0.5", W: 7.0", H: 6.0":**
- Interior tinted `#E05C5C` at 8% (oxidizer contamination)
- Label: `STAGE 1 (DIRTY)` `#E05C5C`
- Inside: `Highest KMnO4/MnO2 drag-in` Inter Regular 12 pt

**Tank 2 (Middle) -- X: 8.0", W: 7.0", H: 6.0":**
- Label: `STAGE 2 (MIDDLE)` `#F0EDE8`

**Tank 3 (Clean) -- X: 15.5", W: 7.0", H: 6.0":**
- Tint `#2EC4B6` at 10%
- Label: `STAGE 3 (CLEAN)` `#2EC4B6`
- `DI WATER IN` JetBrains Mono 12 pt `#2EC4B6`

Standard parts movement and water flow arrows.

**Oxidizer threat callout (Y: 12.5" to 14.3"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.6", fill `#1E2435`, FULL border 2 pt `#E05C5C`
- `CRITICAL: Residual oxidizer (KMnO4) or MnO2 residue POISONS the Pd catalyst in Stage 3. The catalyst costs $50-200+ per liter -- one batch of contaminated catalyst is an expensive mistake.`
- Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Rinse Parameters + Oxidizer Threat

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 11.0"):**

| Parameter | Value |
|---|---|
| Type | Double or triple counterflow, DI water |
| Temperature | Ambient |
| Time | 1-3 min per stage |
| Conductivity target | < 50 uS/cm in final stage |
| Agitation | Air or part movement |
| Water quality | DI preferred -- oxidizer residues dissolve better |

**Right -- Oxidizer Contamination (X: 12.0", W: 11.5"):**

Title: `WHY OXIDIZER RESIDUE IS FATAL` Barlow SemiBold 18 pt `#E05C5C`

- `KMnO4 is a strong oxidizer that remains on surfaces`
- `MnO2 (brown residue) forms during permanganate desmear`
- `If not removed by neutralizer/reducer, MnO2 coats dielectric`
- `Pd catalyst cannot adsorb onto MnO2-coated surface`
- `Result: no Pd nuclei --> no copper deposition --> open through-holes`

Solution: `Verify neutralizer step is effective. Check for brown residue visually. Thorough DI rinse after neutralizer.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-ACTIVATION RINSE` -- Y: 21.2".

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| KMnO4 carry-over | Pd catalyst poisoned; no Cu deposition | Insufficient rinse after desmear | Add rinse stage; increase flow |
| MnO2 residue | Patchy Cu deposition on dielectric | Neutralizer exhausted or skipped | Replenish neutralizer; verify step |
| Alkaline carry-over | Acid pre-dip neutralized; weak Pd adsorption | Cleaner residue not rinsed | More rinse stages; check conductivity |
| Particulate in rinse | Nodular Cu deposit downstream | Dirty rinse water or tank | Filter rinse water; clean tanks |

---

### ZONE 6 -- Safety + Water Quality

**Left -- Water Quality (X: 0.5", W: 11.0"):**
- Title: `WATER QUALITY` `#2EC4B6`
- `DI water preferred for all E-Cu rinses`
- `Monitor conductivity at final stage: < 50 uS/cm`
- `Dump and refill when contaminated`
- `Rinse water color: purple/brown tint = permanganate carryover`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY` `#E8A020`
- `Rinse water may contain dissolved KMnO4 (oxidizer)`
- `MnO2 stains skin and surfaces permanently`
- `Rinse overflow: waste treatment (may contain Mn)`
- `Wet floors: slip hazard`
- `Gloves at all times`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Electroless Copper -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Oxidizer threat border `#E05C5C` -> `#B83E3E`.
**Export:** Six files -- `Rinse E-Cu Pre-Act -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The permanganate/MnO2 contamination threat is unique to E-Cu processing and has no parallel in EN rinse posters. The visual should emphasize the cost of catalyst contamination -- Pd catalyst solutions are the single most expensive consumable in the E-Cu line. The brown MnO2 residue is visually detectable (unlike most rinse contaminants), which makes the "check for brown residue" callout practical advice.

---

*Alaina -- Poster #241 -- Construction Workup v1.0 -- 2026-04-26*
