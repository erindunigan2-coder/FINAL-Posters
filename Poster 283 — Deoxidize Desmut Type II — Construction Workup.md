---
Project: Plating Posters Inc
Poster Number: 283
Title: "Deoxidize / Desmut -- Type II"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.5)"
Technical Source: Industry-standard deoxidize/desmut chemistry for sulfuric acid anodizing (Type II). Covers HNO3, HNO3/HF, and proprietary non-HF alternatives.
Process Scope: Deoxidize/desmut stage (Stage 4 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Desmut
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #283 -- Construction Workup
## Deoxidize / Desmut -- Type II

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. After caustic etch, the aluminum surface is coated in smut -- insoluble residues of copper, silicon, iron, and manganese that did not dissolve in NaOH. The desmut step removes this smut and leaves a clean, oxide-free surface ready for anodizing. The hero concept: why HF is needed for copper alloys (2024, 7075) and the safety imperative that comes with it.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Desmut process visual (Block B):** Before/after surface comparison showing smut layer being dissolved.
2. **Alloy-specific desmut table (Block D):** Two columns -- standard (6xxx) vs. high-Cu (2xxx/7xxx).
3. **HF safety callout (Block E):** Prominent safety panel -- calcium gluconate, training requirements.
4. **Non-HF alternatives panel (Block F).**
5. **Failure mode strip (Block G).**

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
  Stage 4 highlighted (Amber)
ZONE 3 -- DESMUT PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ALLOY-SPECIFIC CHEMISTRY (14.5"--20.5" / ~6.0")
ZONE 5 -- HF SAFETY + NON-HF ALTERNATIVES (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES + WHY DESMUT MATTERS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE / DESMUT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Stage 4 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The caustic etch removed the aluminum. Now remove what it left behind. Smut is the etch's garbage -- and it must go before you anodize.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Etched surface with smut layer (Cu, Si, Fe residues)  -->  After: Clean, oxide-free aluminum ready for anodizing`

---

### ZONE 3 -- Desmut Process Hero

**Section label:** `THE DESMUT TANK` -- Y: 4.4".

**BLOCK B -- Before/After Surface + Tank**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 6.0", W: 21.0", H: 6.0"
- Fill: `#252B3D`
- Border: 3 pt `#C8D0D8`

**Parts on rack (center):**
- Vertical rect, X: 9.5", Y: 6.5", W: 5.0", H: 4.5", fill `#C8D0D8` at 20%, border 2 pt `#E8A020`

**Bath parameter labels (right side, inside tank):**
- `HNO3 25--50% by volume` JetBrains Mono 14 pt `#E8A020`
- `Ambient temperature` JetBrains Mono 14 pt `#F0EDE8`
- `30--120 sec (standard alloys)` JetBrains Mono 14 pt `#F0EDE8`
- `60--180 sec (Cu alloys)` JetBrains Mono 13 pt `#E05C5C`

**Smut dissolution arrows (from part surface outward):**
- Small arrows showing smut dissolving into solution
- Labels: `Cu particles` / `Si particles` / `Fe residue` / `Mn residue`
- Each: Inter Regular 11 pt `#E05C5C`

**Before/After comparison strip (above tank, Y: 5.0" to 5.8"):**

Two panels side by side:
- LEFT: `BEFORE` Barlow SemiBold 14 pt `#E05C5C` -- `Dark smut layer covering etched surface`
- RIGHT: `AFTER` Barlow SemiBold 14 pt `#27AE60` -- `Clean, bright aluminum -- ready for anodize`

**Why HNO3 callout (bottom of zone):**
- `Nitric acid dissolves the aluminum matrix of the smut layer, releasing the insoluble particles. For copper alloys, HF is needed to attack the metallic copper directly.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Alloy-Specific Chemistry

**Section label:** `ALLOY-SPECIFIC DESMUT CHEMISTRY` -- Y: 14.7".

**Two-column layout:**

**Left -- Standard Alloys: 6xxx, 5xxx, 1xxx (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.5", fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `STANDARD DESMUT (6061, 6063, 5052, 1100)` Barlow SemiBold 18 pt `#27AE60`.

| Parameter | Value |
|---|---|
| Chemistry | Nitric acid (HNO3) |
| Concentration | 25--50% by volume (from concentrated 67--70% HNO3) |
| HF | NOT required |
| Temperature | Ambient (room temperature) |
| Time | 30--120 seconds |
| Alternative | Proprietary non-HF desmut (ferric sulfate-based) |

Note: `Light smut from 6xxx alloys dissolves readily in HNO3 alone. No HF needed.` Inter Medium 13 pt `#27AE60`.

**Right -- High-Cu Alloys: 2xxx, 7xxx (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.5", fill `#1E2435`, left accent `#E05C5C` 0.06".
Title: `AGGRESSIVE DESMUT (2024, 7075)` Barlow SemiBold 18 pt `#E05C5C`.

| Parameter | Value |
|---|---|
| Chemistry | HNO3 + HF (mixed acid) |
| HNO3 | 25--50% by volume |
| HF | 1--3% by volume (from 40% HF) |
| Temperature | Ambient |
| Time | 60--180 seconds |
| Alternative | Chromic-sulfuric deox (legacy -- Cr6+ being phased out) |

Note: `HNO3 alone cannot dissolve metallic copper particles. HF attacks copper directly and dissolves silicon from cast alloys.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 5 -- HF Safety + Non-HF Alternatives

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- HF SAFETY (X: 0.5", W: 11.0"):**

Rounded rect, fill `#E05C5C` at 10%, border 2 pt `#E05C5C`.
Title: `HF SAFETY -- NON-NEGOTIABLE` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- `Hydrofluoric acid (HF) is EXTREMELY hazardous`
- `Skin absorption causes systemic fluoride poisoning and bone damage`
- `Burns may not be immediately painful -- delayed onset is common`
- `Calcium gluconate gel MUST be available at the station`
- `HF-specific training is MANDATORY before personnel work with this chemistry`
- `Buddy system: never work alone with HF`

Each bullet: Inter Medium 14 pt `#F0EDE8`. Bold keywords in `#E05C5C`.

Bottom highlight: `If you see HF -- you need training, calcium gluconate, and a buddy. No exceptions.` Barlow SemiBold 14 pt `#E05C5C`.

**Right -- Non-HF Alternatives (X: 12.0", W: 11.5"):**

Section label: `NON-HF ALTERNATIVES` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Alternative | Chemistry | Pros | Cons |
|---|---|---|---|
| Ferric sulfate desmut | Fe2(SO4)3 + H2SO4 | No HF; safer; growing market share | May not remove heavy Cu smut on 2024 |
| Proprietary deoxidizer | Per supplier TDS | Formulated for specific alloys | Must validate for each alloy |
| Chromic-sulfuric (legacy) | Na2Cr2O7 + H2SO4 | Excellent on all alloys | Contains Cr6+ -- regulatory phase-out |

Note: `Non-HF alternatives work well on 6xxx alloys but must be validated for heavy copper smut on 2024.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Failure Modes + Why Desmut Matters

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Failure Modes:**

| Failure | Cause | Downstream Effect |
|---|---|---|
| Mottled anodize | Smut carried into anodize tank | Uneven oxide thickness; poor dye absorption |
| Poor dye uptake | Residual smut blocks pores | Discolored or spotty dyed coating |
| Reduced corrosion resistance | Smut under oxide film | Corrosion initiates at smut inclusions |
| Surface pitting | Over-aggressive desmut (HF too long) | Grain boundary attack, especially on thin walls |

**Right -- Why Desmut Matters:**

Section label: `WHY THIS STEP MATTERS` Barlow Condensed ExtraBold 22 pt.

Prominent callout:
- `Smut is invisible to a casual glance but devastating to anodize quality.`
- `A part that looks clean after etch is NOT clean -- it is covered in a microscopic layer of insoluble alloy residues.`
- `The desmut step is where "looks good enough" gets you rejected.`

Inter Medium 14 pt `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Deoxidize / Desmut -- Type II`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5. HF safety information is general guidance -- always follow site-specific safety protocols and OSHA requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deoxidize Desmut Type II -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The HF safety callout should be the most visually prominent coral element on the poster. This is a life-safety topic -- HF burns can be fatal. The alloy-specific split (standard vs. high-Cu) is the core technical content. The non-HF alternatives section reflects the real industry trend away from HF where possible. The "why desmut matters" section drives home that this seemingly simple step has outsized impact on final coating quality.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #283 -- Construction Workup v1.0*
*2026-04-26*
