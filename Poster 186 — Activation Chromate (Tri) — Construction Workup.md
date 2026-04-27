---
Project: Plating Posters Inc
Poster Number: 186
Title: "Activation -- Chromate (Tri)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.4)"
Technical Source: Deoxidize/desmut step for trivalent chromate conversion on aluminum. Removes oxide layer and alloying element smut. More critical for tri than hex because tri baths cannot "burn through" surface contamination. Stage 3 of 7.
Process Scope: Deoxidize/desmut (activation) -- Stage 3 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Activation
  - Deoxidize
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #186 -- Construction Workup
## Activation -- Chromate (Tri)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 7. The deoxidize/desmut step is surface conditioning for aluminum. It removes the natural oxide layer (which reforms in seconds) and any smut from alloying elements (Cu, Si, Mn, Fe) left by cleaning. This step is MORE critical for trivalent chromate than for hexavalent -- hex chrome is a powerful oxidizer that can "burn through" minor contamination, but tri chrome cannot.

Hero visual: microscopic cross-section of aluminum surface showing oxide removal and smut dissolution, with alloy-specific deoxidizer selection guide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Surface conditioning hero (Block B):** Schematic cross-section showing aluminum substrate, native oxide layer being dissolved, smut particles being removed. Built with layered rectangles and arrows.
2. **Alloy-specific deoxidizer guide (Block D):** Which deoxidizer for which alloy family -- the most actionable content on this poster.
3. **"Tri Is Less Forgiving" callout (Block E):** Why thorough deox matters more for trivalent than hexavalent.
4. **Defect grid (Block F):** 4 deoxidize failures and consequences.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- SURFACE CONDITIONING HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ALLOY GUIDE + "TRI IS LESS FORGIVING" (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE / DESMUT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Activation -- Stage 3 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Aluminum reoxidizes in seconds. Remove the oxide, remove the smut, expose fresh metal. Tri chromate demands a perfect surface.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned aluminum with native oxide and alloying smut  -->  After: Fresh, active aluminum surface ready for chromate`

---

### ZONE 3 -- Surface Conditioning Hero

**Section label:** `DEOXIDIZE AND DESMUT -- WHAT HAPPENS AT THE SURFACE` -- Y: 4.4".

**BLOCK B -- Aluminum Surface Cross-Section**

Y: 5.0" to 14.0". Schematic showing layered structure.

**Substrate layer (bottom):**
- Rectangle, X: 2.0", Y: 10.5", W: 20.0", H: 3.0", fill `#C8D0D8` at 40%
- Label: `ALUMINUM SUBSTRATE` Barlow SemiBold 16 pt `#C8D0D8`
- Sublabel: `(2024, 6061, 7075, cast, etc.)` Inter Regular 12 pt `#F0EDE8` at 60%

**Native oxide layer (middle -- being removed):**
- Rectangle, X: 2.0", Y: 9.5", W: 20.0", H: 1.0", fill `#3A4055`
- Label: `Al2O3 NATIVE OXIDE (5--50 nm)` JetBrains Mono 12 pt `#F0EDE8`
- Dashed border or "dissolving" visual: small gaps in the rectangle with arrows pointing up showing dissolution
- Dissolution label: `Acid dissolves oxide layer` Inter Regular 12 pt `#E8A020`

**Smut particles (on surface):**
- 6--8 small irregular shapes in `#E05C5C` at 60% scattered on top of oxide layer
- Label: `Alloying element smut: Cu, Si, Mn, Fe residues` Inter Regular 12 pt `#E05C5C`
- Arrow showing removal: `Smut dissolves in acid (HF needed for Si, Cu)` Inter Regular 12 pt `#E8A020`

**Deoxidizer solution (above surface):**
- Large area, Y: 5.5" to 9.5", fill `#252B3D` at 30%
- Chemistry labels:
  - `HNO3 30--50%` JetBrains Mono 16 pt `#E8A020`
  - `+ HF 1--3% (high-Cu/Si alloys)` JetBrains Mono 14 pt `#E8A020`
  - `Ambient temperature` JetBrains Mono 13 pt `#F0EDE8`
  - `1--5 min immersion` JetBrains Mono 13 pt `#F0EDE8`

**"After" state (right side callout):**
- Arrow pointing down to clean substrate
- `RESULT: Fresh, active aluminum surface` Barlow SemiBold 14 pt `#27AE60`
- `Ready for chromate deposition within 5 minutes` Inter Medium 12 pt `#27AE60`

**Bottom callout (Y: 13.5"):**
- `The deoxidize step is surface conditioning for aluminum. It is analogous to acid activation on steel -- but with alloy-specific chemistry.`
- Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Alloy Guide + "Tri Is Less Forgiving"

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Alloy-Specific Deoxidizer Guide (X: 0.5", W: 12.0"):**

Section label: `DEOXIDIZER BY ALLOY FAMILY` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

Table (Y: 15.3" to 20.0"):

| Alloy Family | Examples | Deoxidizer | Notes |
|---|---|---|---|
| 2xxx (high Cu) | 2024, 2014 | HNO3/HF or Cr-sulfuric | Cu-rich smut is tenacious; HF required |
| 6xxx (low alloy) | 6061, 6063 | Mild HNO3 or non-chrome | Easiest to deox; most forgiving |
| 7xxx (Zn-Cu) | 7075, 7050 | HNO3/HF | Cu smut similar to 2xxx; aggressive deox needed |
| Cast (high Si) | 356, A356 | HNO3/HF (extra HF) | Silicon particles require fluoride to dissolve |

Data: JetBrains Mono 12 pt `#F0EDE8`. Alloy labels: Inter Medium 13 pt in `#E8A020`. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- "Tri Is Less Forgiving" Warning (X: 13.0", W: 10.5"):**

Section label: `WHY THIS MATTERS MORE FOR TRI` Barlow Condensed ExtraBold 22 pt `#E05C5C`. Y: 14.7".

Callout box: Rounded rect, H: 4.8", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Hex chromate (Cr6+) is a powerful oxidizer that can "burn through" minor surface contamination during coating`
- `Tri chromate (Cr3+) CANNOT do this -- it relies entirely on a clean, active surface`
- `Incomplete deox = patchy or absent tri coating`
- `This is the #1 reason tri chromate processes fail when converting from hex`

Bottom rule:
- `RULE: If you could get away with a lazy deox on hex, you cannot on tri.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Operating Parameters Table

**Section label:** `OPERATING PARAMETERS` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 20.7".

**Parameter table (Y: 21.3" to 26.3"):**

| Deoxidizer Type | Concentration | Temp | Time | Best For |
|---|---|---|---|---|
| Nitric acid (HNO3) | 30--50% by volume | Ambient | 1--5 min | 6xxx alloys; general use |
| Nitric + HF | 30% HNO3 + 1--3% HF | Ambient | 30 sec--3 min | 2xxx, 7xxx, cast (high Cu/Si) |
| Chromic-sulfuric (legacy) | 10--15 oz/gal CrO3 + 30--40 oz/gal H2SO4 | 140--160 F | 5--10 min | Legacy lines; being phased out |
| Non-chrome (ferric sulfate) | Per supplier | Amb--120 F | 1--5 min | RoHS-compliant alternative |
| Ammonium bifluoride | 4--8 oz/gal | Ambient | 1--3 min | Cast alloys; heavy oxide |

Data: JetBrains Mono 12 pt. Alternating rows. "Legacy" row in `#E05C5C` at 20% tint to flag regulatory concern.

---

### ZONE 6 -- Defect Diagnosis

**Section label:** `WHAT GOES WRONG -- 4 DEOX FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 26.7".

**4-card row (Y: 27.3" to 32.3"):**

| Card | X | Problem | Cause | Downstream Effect |
|---|---|---|---|---|
| 1 | 0.5" | RESIDUAL SMUT | Wrong deox for alloy; no HF on 2xxx/7xxx | No chromate adhesion; coating wipes off |
| 2 | 6.33" | OVER-ETCH | Excess HF or too long immersion | Roughened surface; pitting visible through coating |
| 3 | 12.16" | REOXIDATION | > 5 min between deox rinse and chromate | Fresh oxide blocks chromate deposition |
| 4 | 18.0" | PITTING | Chloride in deox bath or rinse water | Permanent surface damage; coating failure at pits |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Downstream: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Chromate (Trivalent)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Chromate Tri -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The alloy-specific deoxidizer table is the most actionable content. A shop running 7075 needs to know that mild nitric alone will leave copper smut that ruins the tri chromate coat. The "Tri Is Less Forgiving" callout is the key educational differentiator -- shops converting from hex to tri need to upgrade their deox discipline.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #186 -- Construction Workup v1.0*
*2026-04-26*
