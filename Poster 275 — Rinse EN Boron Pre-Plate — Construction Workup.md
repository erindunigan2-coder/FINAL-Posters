---
Project: Plating Posters Inc
Poster Number: 275
Title: "Rinse -- EN Boron -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 5)"
Technical Source: Standard pre-plate rinse for EN-B. Same contamination concerns as EN-P: chloride drag-in causes pitting, chromate drag-in poisons stabilizer. Watson domain expertise.
Process Scope: Pre-plate rinse (Stage 4 of 8) for electroless nickel-boron plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #275 -- Construction Workup
## Rinse -- EN Boron -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The pre-plate rinse for EN-B follows the same principles as all electroless nickel pre-plate rinses. Its purpose is to remove acid activation chemistry, zincate residues, or colloidal activation chemicals before parts enter the EN-B bath. The unique EN-B concern: the DMAB reducing agent is 5-10x more expensive than hypophosphite, and the EN-B bath is less tolerant of metallic contamination (Fe, Cu) than EN-P. Contamination shortens an already expensive bath's life even further. This rinse is the last line of defense before the most costly bath on the line.

Hero visual: rinse tank cross-section with contamination pathway diagram emphasizing the economic impact of drag-in on an expensive DMAB bath.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Contamination pathway -- what activation drag-in does to the EN-B bath.
2. **EN-B-specific contamination concerns (Block D):** Why EN-B is less tolerant than EN-P.
3. **Substrate-specific rinse notes (Block E):** Zincated aluminum requires fast transfer; chloride from HCl is the universal threat.
4. **Defect grid (Block F):** 4 rinse-related EN-B defects.

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
ZONE 3 -- CONTAMINATION PATHWAY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- EN-B-SPECIFIC CONTAMINATION CONCERNS (14.5"--20.5" / ~6.0")
ZONE 5 -- SUBSTRATE-SPECIFIC RINSE NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 4 of 8 -- Pre-Plate` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The EN-B bath is the most expensive electroless nickel on the line. Every contaminant you drag in shortens its life and wastes DMAB.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated surface (acid, zincate, or colloidal)  -->  After: Clean surface ready for EN-B deposition`

---

### ZONE 3 -- Contamination Pathway Hero

**Section label:** `WHAT DRAG-IN DOES TO YOUR EN-B BATH` -- Y: 4.4".

**BLOCK B -- Three-Panel Contamination Pathway (Y: 5.0" to 14.0")**

Same three-panel horizontal layout as Poster #259.

**Panel 1 -- Source (X: 0.5", Y: 5.0", W: 7.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `DRAG-OUT SOURCES` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `From acid activation (steel):` Inter Medium 14 pt `#F0EDE8`
  - `HCl or H2SO4 residues` JetBrains Mono 13 pt `#F0EDE8`
  - `Chloride ions (Cl-)` JetBrains Mono 13 pt `#E05C5C`
  - `Dissolved iron (Fe2+/Fe3+)` JetBrains Mono 13 pt `#F0EDE8`
  - `From zincate (aluminum):` Inter Medium 14 pt `#F0EDE8`
  - `NaOH / ZnO residues` JetBrains Mono 13 pt `#F0EDE8`
  - `Excess zinc ions` JetBrains Mono 13 pt `#F0EDE8`
  - `From Sn/Pd colloidal (plastics):` Inter Medium 14 pt `#F0EDE8`
  - `Tin, palladium, HCl residues` JetBrains Mono 13 pt `#F0EDE8`
  - `Chromate from etch (Cr6+ -- poison!)` JetBrains Mono 13 pt `#E05C5C`

**Panel 2 -- Rinse (X: 8.0", Y: 5.0", W: 7.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `THE RINSE` Barlow SemiBold 18 pt `#2EC4B6`
- Visual: simplified cross-section of counterflow rinse tank
- Parameters:
  - `DI counterflow -- 2 stage minimum` Inter Medium 14 pt `#F0EDE8`
  - `Ambient temperature (18-30 C)` JetBrains Mono 13 pt `#F0EDE8`
  - `30-60 seconds per stage` JetBrains Mono 13 pt `#F0EDE8`
  - `Target: <20 uS/cm final rinse` JetBrains Mono 13 pt `#2EC4B6`
  - `DI or RO water preferred` Inter Regular 13 pt `#F0EDE8`

**Panel 3 -- Consequence (X: 16.0", Y: 5.0", W: 7.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E05C5C` 4 pt
- Title: `IF DRAG-IN REACHES THE EN-B BATH` Barlow SemiBold 18 pt `#E05C5C`
- Content:
  - `Chloride drag-in:` Inter Medium 14 pt `#F0EDE8`
  - `Causes pitting in EN-B deposit` Inter Regular 13 pt `#E05C5C`
  - `Accelerates bath aging` Inter Regular 13 pt `#E05C5C`
  - `Fe/Cu contamination:` Inter Medium 14 pt `#F0EDE8`
  - `EN-B is MORE sensitive to metallic contamination than EN-P` Inter Medium 13 pt `#E05C5C`
  - `Fe and Cu act as decomposition nucleation sites` Inter Regular 13 pt `#E05C5C`
  - `Chromate drag-in:` Inter Medium 14 pt `#F0EDE8`
  - `Poisons stabilizer system at ppm levels` Inter Regular 13 pt `#E05C5C`
  - `Bath goes inert -- no deposition` Inter Regular 13 pt `#E05C5C`
  - `DMAB cost: 5-10x hypophosphite` Inter Medium 14 pt `#E8A020`
  - `Every MTO lost to contamination is expensive` Inter Medium 13 pt `#E8A020`

**Arrows between panels:** 3 pt `#3A4055`, right-pointing.

---

### ZONE 4 -- EN-B-Specific Contamination Concerns

**Section label:** `WHY EN-B IS LESS TOLERANT THAN EN-P` -- Y: 14.7".

**BLOCK D -- Two Callout Panels (Y: 15.3" to 20.3")**

**Left -- Metal Contamination Sensitivity (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `METALLIC CONTAMINATION -- MORE DANGEROUS IN EN-B` Barlow SemiBold 16 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `DMAB is a stronger reducing agent than hypophosphite`
  - `Stronger reducing power = lower energy barrier for spontaneous reduction`
  - `Metal ions (Fe2+, Cu2+) in bath are reduced to metallic particles MORE easily`
  - `These particles act as nucleation sites for uncontrolled decomposition`
  - `EN-P tolerates low-level Fe/Cu; EN-B may crash at the same levels`
  - `Continuous filtration (1-5 um) is essential -- not optional` Inter Medium 13 pt `#E8A020`

**Right -- Cost Impact (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `THE COST OF CONTAMINATION` Barlow SemiBold 16 pt `#E8A020`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `DMAB cost: 5-10x more per unit reducing power than NaH2PO2` JetBrains Mono 13 pt `#E8A020`
  - `EN-B bath life: 3-5 MTO (DMAB) or 2-4 MTO (borohydride)`
  - `EN-P bath life: 6-8 MTO`
  - `Contamination shortens an already short bath life`
  - `Every premature bath dump wastes hundreds of dollars in DMAB`
  - `ROI calculation: a $50 DI rinse system saves thousands in DMAB`
- Bottom highlight:
  - Rounded rect, W: 10.5", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
  - `The cheapest step on the line protects the most expensive bath. Rinse well.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Substrate-Specific Rinse Notes

**Section label:** `RINSE NOTES BY SUBSTRATE` -- Y: 20.7".

**BLOCK E -- Four Substrate Boxes (Y: 21.3" to 26.3")**

2x2 grid:

**Steel (X: 0.5", Y: 21.3", W: 11.0", H: 2.3"):**
- Accent: `#2EC4B6`
- Title: `STEEL -- AFTER ACID ACTIVATION` Barlow SemiBold 14 pt `#2EC4B6`
- `Rinse removes HCl or H2SO4 residues` Inter Regular 13 pt `#F0EDE8`
- `Chloride is the primary threat -- DI rinse is essential` Inter Medium 13 pt `#E05C5C`
- `Transfer quickly -- clean steel re-oxidizes in seconds` Inter Regular 13 pt `#F0EDE8`

**Aluminum (X: 12.0", Y: 21.3", W: 11.5", H: 2.3"):**
- Accent: `#E8A020`
- Title: `ALUMINUM -- AFTER DOUBLE ZINCATE` Barlow SemiBold 14 pt `#E8A020`
- `Minimize rinse time -- zinc layer oxidizes in air` Inter Medium 13 pt `#E05C5C`
- `Transfer to EN-B bath within 30 seconds of rinsing` JetBrains Mono 13 pt `#E8A020`
- `Brief rinse (15-30 sec) -- just enough to remove excess zincate` Inter Regular 13 pt `#F0EDE8`

**Stainless Steel (X: 0.5", Y: 23.8", W: 11.0", H: 2.3"):**
- Accent: `#27AE60`
- Title: `STAINLESS -- AFTER WOOD'S STRIKE` Barlow SemiBold 14 pt `#27AE60`
- `Rinse removes NiCl2 + HCl residues from Wood's strike` Inter Regular 13 pt `#F0EDE8`
- `Chloride drag-in from Wood's strike is significant` Inter Medium 13 pt `#E05C5C`
- `Double counterflow rinse recommended` Inter Regular 13 pt `#F0EDE8`

**Plastics (X: 12.0", Y: 23.8", W: 11.5", H: 2.3"):**
- Accent: `#E05C5C`
- Title: `PLASTICS -- AFTER Sn/Pd COLLOIDAL` Barlow SemiBold 14 pt `#E05C5C`
- `Chromate drag-in from CrO3 etch is the greatest risk` Inter Medium 13 pt `#E05C5C`
- `Even trace Cr6+ poisons EN-B stabilizer -- bath goes inert` Inter Regular 13 pt `#E05C5C`
- `Extended rinse (3+ stages) after chromic acid etch` Inter Regular 13 pt `#F0EDE8`
- `Consider permanganate etch (RoHS) to eliminate Cr6+ entirely` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 6 -- Defect Grid

**Section label:** `RINSE-RELATED EN-B DEFECTS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING | `#E05C5C` | Chloride drag-in from HCl activation or Wood's strike | Improve rinse; use DI; verify <20 uS/cm; add rinse stage |
| R1C2 | BATH DECOMPOSITION | `#E05C5C` | Fe/Cu metallic contamination from activation drag-in | Extended rinse; continuous filtration; verify activation bath purity |
| R2C1 | SKIP PLATING | `#E8A020` | Oxidized activation surface from slow transfer or poor rinse | Minimize transfer time; keep parts wet; verify catalytic surface |
| R2C2 | STABILIZER POISONING | `#E05C5C` | Chromate (Cr6+) drag-in from plastic etch | Extended rinse after chromic etch; switch to permanganate etch |

Card construction: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" (color per defect).

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, defect color
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- EN Boron -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for EN-B pre-plate rinsing. Specific rinse requirements vary by EN-B bath chemistry and substrate. Consult your process supplier for guidance. Source: General industry knowledge; ASTM B841.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse EN Boron Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster follows the same contamination-pathway structure as Poster #259 (Electroless Gold pre-plate rinse) but with an EN-B-specific economic argument. The core message: EN-B is the most expensive electroless nickel bath, and it is more sensitive to metallic contamination than EN-P. A good rinse is the cheapest insurance policy on the line. The substrate-specific rinse notes in Zone 5 are the practical reference -- operators need to know that zincated aluminum requires speed, that Wood's strike brings chloride, and that chromic acid etch brings Cr6+ poison. The cost callout in Zone 4 puts real dollars behind the discipline.

---

*Alaina -- Poster #275 -- Construction Workup v1.0 -- 2026-04-26*
