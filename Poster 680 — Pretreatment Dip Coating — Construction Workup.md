---
Project: Plating Posters Inc
Poster Number: 680
Title: "Pretreatment -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.5)"
Technical Source: Pretreatment systems for dip coating -- iron phosphate for steel, and adhesion promoter primers specific to each dip coating family (PVC on steel, nylon on steel, polyethylene on steel). Primer is the critical pretreatment for dip coating because many thick dip coats require a chemical bridge to the substrate.
Process Scope: Pretreatment for dip coating -- Stage 4 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - Pretreatment
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #680 -- Construction Workup
## Pretreatment -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 7. Dip coating pretreatment tells a different story than spray or powder: the thick coatings (5-40 mils) do not need the fine-tuned conversion coatings of thin-film processes, but they absolutely need adhesion promoter primers matched to the specific coating-substrate combination. PVC on steel needs a phenolic primer. Nylon on steel needs epoxy. Polyethylene on steel needs chlorinated polyolefin or flame treatment. The hero is a primer matching matrix that tells the operator exactly which primer to use for which coating-substrate pair.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Primer matching matrix (Block B -- HERO):** Coating type x substrate --> required primer.
2. **Iron phosphate baseline (Block C):** Standard conversion coating for steel parts.
3. **Primer application parameters (Block D):** DFT, cure, and method for each primer type.
4. **Defect grid (Block F):** 6 pretreatment defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- PRIMER MATCHING MATRIX HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- IRON PHOSPHATE BASELINE (15.0"--21.0" / ~6.0")
ZONE 5 -- PRIMER APPLICATION PARAMETERS (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Adhesion Promoters Matched to Coating and Substrate -- Stage 4 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `PVC will not stick to bare steel. Nylon will not stick without epoxy primer. Polyethylene needs chlorinated polyolefin. The primer is the bridge -- get the chemistry right.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry surface --> After: Primed surface with adhesion promoter ready for dip coating`

---

### ZONE 3 -- Primer Matching Matrix Hero

**Section label:** `PRIMER MATCHING MATRIX -- WHICH PRIMER FOR WHICH SYSTEM` -- Y: 4.4".

**BLOCK B -- Matrix Table (Y: 5.0" to 14.5")**

Large table spanning full width (23.0"):

| Dip Coating Type | Substrate | Required Primer | Primer Chemistry | DFT (mils) | Cure |
|---|---|---|---|---|---|
| PVC Plastisol | Steel | Phenolic-based primer | Phenolic resin, solvent-borne | 0.3--1.0 | Bake 300--350 F, 10--15 min |
| PVC Plastisol | Steel | Polyester primer (alternative) | Polyester resin | 0.3--1.0 | Bake 300--350 F, 10--15 min |
| Nylon 11/12 | Steel | Epoxy primer | 2K epoxy or heat-cure epoxy | 0.5--1.0 | Bake 350--400 F, 10--15 min |
| Polyethylene | Steel | Chlorinated polyolefin (CPO) | CPO adhesion promoter | 0.3--0.5 | Air dry or bake |
| Polyethylene | Steel | Flame treatment (alternative) | No primer -- flame oxidizes PE surface | N/A | In-line flame treatment |
| Solution dip (epoxy) | Steel | Iron phosphate conversion | Phosphoric acid conversion | 25--75 mg/ft2 | Immersion 60--120 sec |
| Solution dip (epoxy) | Steel | None (direct to blast) | Blast profile provides adhesion | 1.5--3.0 mil profile | N/A |

Header row: fill `#3A4055`, Barlow SemiBold 13 pt `#F0EDE8`.
Data: JetBrains Mono 11 pt. Alternating rows: `#1E2435` / `#252B3D`.

Below table -- callout (Inter Medium 14 pt `#E8A020`):
`The primer is NOT optional for PVC, nylon, and PE on steel. Without the correct adhesion promoter, thick dip coats peel off in sheets. This is not a gradual failure -- it is catastrophic.`

---

### ZONE 4 -- Iron Phosphate Baseline

**Section label:** `IRON PHOSPHATE -- THE STANDARD CONVERSION COATING` -- Y: 15.2".

**Two-column layout (Y: 15.8" to 20.8"):**

**Left -- Iron Phosphate Parameters (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `IRON PHOSPHATE FOR DIP COATING` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Parameters (JetBrains Mono 13 pt):
```
Coating weight: 25--75 mg/ft2
Chemistry: Acidic phosphate, pH 3.5--5.5
Temperature: 100--140 F (38--60 C)
Time: 60--120 sec immersion
Color: Iridescent blue-to-gold on steel
```

Purpose:
- `Provides adhesion and under-film corrosion resistance`
- `Standard for general dip coating on steel`
- `Applied BEFORE adhesion promoter primer (if used)`

**Right -- When Iron Phosphate Is Enough (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `WHEN CONVERSION COATING ALONE WORKS` -- Barlow SemiBold, 18 pt, `#27AE60`

- `Solution dip (epoxy, rubber) on steel: iron phosphate + direct dip`
- `Thin solution dip coatings (0.5--3 mils) can adhere directly to phosphate-coated steel`
- `Thick plastisol/thermoplastic coats STILL need adhesion promoter primer over phosphate`

Decision rule: `If the DFT is > 5 mils AND the coating is thermoplastic (PVC, nylon, PE), you need an adhesion promoter primer. If the DFT is < 3 mils and thermoset (epoxy, rubber), iron phosphate alone may be sufficient.`

---

### ZONE 5 -- Primer Application Parameters

**Section label:** `ADHESION PROMOTER PRIMER APPLICATION` -- Y: 21.2".

**Single wide table (Y: 21.8" to 26.3", X: 0.5", W: 23.0"):**

Title: `PRIMER APPLICATION GUIDE` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Primer Type | Application Method | DFT | Cure Before Dip | Pot Life | Notes |
|---|---|---|---|---|---|
| Phenolic (for PVC) | Spray or dip | 0.3--1.0 mil | Bake 300--350 F, 10--15 min | N/A (1K) | Must be fully cured before plastisol dip |
| Epoxy (for nylon) | Spray or dip | 0.5--1.0 mil | Bake 350--400 F, 10--15 min | 2--4 hr (if 2K) | Cured primer withstands 400--600 F preheat |
| CPO (for PE) | Spray, wipe, or dip | 0.3--0.5 mil | Air dry 10--30 min or bake | N/A (1K) | Thin is better -- thick CPO reduces adhesion |
| Iron phosphate | Immersion or spray | 25--75 mg/ft2 | Rinse and dry | N/A | Applied before primer, not after |

Data: JetBrains Mono 11 pt. Alternating rows.

Bottom note: `Always cure the adhesion promoter primer FULLY before dipping. Uncured primer dissolves into the dip coating and provides zero adhesion benefit.` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 PRETREATMENT DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | CATASTROPHIC PEEL | `#E05C5C` | No adhesion promoter primer on PVC/nylon/PE | Apply correct primer per matrix; fully cure before dip |
| R1C2 | PRIMER UNDERCURE | `#E8A020` | Primer not fully baked before dipping | Verify oven profile; extend cure time |
| R1C3 | WRONG PRIMER TYPE | `#E05C5C` | Epoxy primer used for PVC (wrong chemistry) | Match primer to coating type per matrix |
| R2C1 | THIN PHOSPHATE | `#E8A020` | Low concentration or short immersion time | Titrate phosphate bath; increase time or temp |
| R2C2 | CPO TOO THICK | `#2EC4B6` | Excessive chlorinated polyolefin primer DFT | Apply thinner; 0.3--0.5 mil maximum |
| R2C3 | FLASH RUST UNDER PRIMER | `#E05C5C` | Delay between phosphate and primer application | Prime within 4 hours of conversion coating |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Adhesion promoter primer selection and cure parameters are supplier-specific. Consult your dip coating supplier for recommended primer systems.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The primer matching matrix is the poster's defining contribution -- it is the decision tool that prevents the most common dip coating failure: no primer or wrong primer. The "catastrophic peel" language is deliberate: thick dip coats without adhesion promoter do not gradually lose adhesion, they come off in sheets. The CPO "too thick" defect is counterintuitive and worth highlighting -- more primer is not better when the primer itself becomes a weak boundary layer. Iron phosphate gets its own section because it is the baseline for all steel dip coating, applied before the adhesion promoter.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #680 -- Construction Workup v1.0*
*2026-04-26*
