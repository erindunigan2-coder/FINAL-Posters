---
Project: Plating Posters Inc
Poster Number: 227
Title: "Rinse -- EN (Mid Phos) -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 5)"
Process Scope: Pre-plate rinse for electroless nickel mid phosphorus line (Stage 4 of 7)
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

# Poster #227 -- Construction Workup
## Rinse -- EN (Mid Phos) -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of the EN Mid-P process. The most critical rinse in the EN line -- the last barrier between activation chemistry and the EN bath. Chloride drag-in from HCl activation causes pitting. Chromate drag-in from plastic activation etching poisons the bath at ppm levels. For ENIG lines, persulfate or peroxide drag-in degrades EN stabilizers -- and the EN Mid-P bath operates at acid pH (4.6-5.2), so while there is less pH differential concern from acidic activation chemistry, the specific contaminants are uniquely damaging. For zincated aluminum, the rinse must be fast -- the zinc layer oxidizes immediately.

Hero visual: cascade rinse with contamination callout icons showing the three critical drag-in threats, with ENIG persulfate threat added.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero with contamination icons (Block B):** Similar to Poster #219 but with persulfate drag-in threat callout for ENIG added.
2. **Orientation strip (Block C):** Stage 4 highlighted.
3. **Contamination threat panel (Block E):** Four specific drag-in threats and their consequences in the EN bath.
4. **Zincated aluminum timing callout (Block F):** Time-critical transfer requirement.

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
  Stage 4 highlighted
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + CONTAMINATION THREATS (14.5"--21.0" / ~6.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0" / ~6.0")
ZONE 6 -- ZINCATE TIMING + SAFETY (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `EN (Mid Phos) -- Pre-Plate -- Stage 4 of 7` -- Barlow SemiBold, 32 pt, `#2EC4B6`. X: 0.5", Y: 1.5".

**Tagline:** `The most critical rinse in the EN line. Chloride pits the deposit. Persulfate degrades stabilizers. Chromate kills the bath. Speed saves the zincate.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Activated surface (catalytic, acidic residue)  -->  After: Clean, neutral surface ready for EN bath entry`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE PRE-PLATE CASCADE RINSE` -- Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 11.5". Two connected tank cross-sections -- 2-stage counter-current cascade (DI preferred).

**Tank 1 (Dirty Rinse) -- X: 1.5", W: 9.5", H: 5.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior tinted `#E8A020` at 10%
- Label: `STAGE 1 (DIRTY)` Barlow SemiBold 16 pt `#E8A020`
- Overflow arrow down to `DRAIN`

**Tank 2 (Clean Rinse) -- X: 12.0", W: 9.5", H: 5.5":**
- Fill `#252B3D` with `#2EC4B6` tint at 10%
- Label: `STAGE 2 (CLEAN)` Barlow SemiBold 16 pt `#2EC4B6`
- Fresh water inlet: `DI WATER IN` JetBrains Mono 12 pt `#2EC4B6`
- Overflow left into Tank 1

Parts and water flow arrows per standard cascade pattern.

**Four contamination threat callout boxes (Y: 11.8" to 14.3"):**

Four boxes in a single row, each W: 5.5", H: 2.3", fill `#1E2435`, left accent 0.06":

| Box | X | Threat | Accent | Consequence |
|---|---|---|---|---|
| 1 | 0.5" | `CHLORIDE (from HCl)` | `#E05C5C` | Pitting in EN deposit; accelerates bath aging |
| 2 | 6.33" | `CHROMATE (from plastic etch)` | `#E05C5C` | Poisons EN catalysis at ppm levels; kills bath |
| 3 | 12.16" | `PERSULFATE (from ENIG microetch)` | `#E8A020` | Degrades EN stabilizer system; reduces bath life |
| 4 | 18.0" | `ZINC OXIDE (from zincated Al)` | `#E8A020` | Oxidized Zn layer prevents EN initiation |

Threat title: Barlow SemiBold 14 pt in accent color. Consequence: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 4 -- Rinse Parameters + Contamination Threats

**Section label:** `RINSE PARAMETERS -- DETAILED` -- Y: 14.7".

**Left -- Rinse Parameters (X: 0.5", W: 11.0"):**

Header: `PRE-PLATE RINSE` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Water type | DI preferred (critical for ENIG and high-spec) |
| Temperature | Ambient (18-30 C) |
| Stages | 2-3 stage counterflow |
| Immersion time | 30-60 sec per stage |
| Conductivity target | < 20 uS/cm for critical work; < 50 uS/cm minimum |
| Agitation | Air or part movement |
| Drain time | 10-15 sec between tanks |

**Right -- Contamination Impact Table (X: 12.0", W: 11.5"):**

Header: `DRAG-IN CONTAMINANT IMPACT ON EN MID-P BATH` fill `#3A4055`.

| Contaminant | Source | Damage Mechanism | Threshold |
|---|---|---|---|
| Chloride (Cl-) | HCl activation | Pitting; bath instability | < 5 ppm in bath |
| Chromate (Cr6+) | Plastic etch | Stabilizer poisoning; bath death | < 1 ppm fatal |
| Persulfate (S2O8 2-) | ENIG microetch | Stabilizer oxidation | Rinse to < 30 uS/cm |
| Zinc | Excess zincate drag | Metal contamination | Acceptable in traces |

Data: JetBrains Mono 11 pt. Damage: Inter Regular 11 pt `#E05C5C`.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-PLATE RINSE` -- Y: 21.2".

**5-Row Problem Table:**

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Chloride pitting | Small pits in EN deposit | HCl drag-in from activation | DI rinse; add cascade stage |
| Bath decomposition | Spontaneous decomposition after parts enter | Cr6+ drag-in from plastic etch | Dedicated rinse between etch and EN; monitor Cr |
| Stabilizer crash | Plating rate drops; deposit goes rough | Persulfate drag-in (ENIG lines) | Thorough DI rinse; monitor conductivity |
| Skip on aluminum | EN does not initiate on zincated parts | Zinc layer oxidized -- rinse too long | Reduce rinse time; transfer to EN within 30 sec |
| High reject rate | General quality issues across all substrates | Rinse water conductivity too high | Monitor daily; dump and refill at > 500 uS/cm |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Zincate Timing + Safety

**Section label:** `CRITICAL TIMING & SAFETY` -- Y: 27.2".

**Left -- Zincate Transfer Timing (X: 0.5", W: 11.0"):**
- Rounded rect fill `#1E2435`, FULL border 2 pt `#E8A020`
- Title: `ZINCATED ALUMINUM -- TRANSFER TIMING` Barlow SemiBold 18 pt `#E8A020`
- `Zinc layer begins to oxidize IMMEDIATELY on exposure to air`
- `Oxidized zinc will not initiate EN deposition`
- `RULE: Rinse quickly and transfer to EN bath within 30 seconds`
- `Do not allow parts to sit in rinse or dry between rinse and EN`
- Visual: horizontal timeline bar -- `ZINCATE` -> `RINSE (30 sec max)` -> `EN BATH` with urgency arrow

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` Barlow SemiBold 18 pt `#E8A020`
- `Rinse water is mildly acidic from activation drag-out`
- `ENIG rinse may contain trace persulfate -- oxidizer; handle accordingly`
- `Rinse overflow goes to waste treatment`
- `Wet floors: slip hazard`
- `DI water system: check resistivity daily`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- EN (Mid Phos) -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for pre-plate rinsing in electroless nickel mid phosphorus (5-9% P) plating lines. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Zincate timing border `#E8A020` -> `#C8860A`.
**Export:** Six files -- `Rinse EN Mid-P Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The persulfate drag-in threat is the unique Mid-P element at this stage. In ENIG lines, sodium persulfate microetch (or sulfuric/peroxide) is used instead of HCl to activate the copper substrate. Persulfate is an oxidizer that attacks EN stabilizer chemistry -- a contamination pathway that does not exist in Low-P lines processing steel or aluminum. This deserves visual emphasis: four threat boxes instead of three.

---

*Alaina -- Poster #227 -- Construction Workup v1.0 -- 2026-04-26*
