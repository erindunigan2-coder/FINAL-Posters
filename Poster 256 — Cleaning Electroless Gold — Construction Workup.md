---
Project: Plating Posters Inc
Poster Number: 256
Title: "Cleaning -- Electroless Gold"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Cleaning for electroless gold (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessGold
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ENIG
---

# Poster #256 -- Construction Workup
## Cleaning -- Electroless Gold

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for electroless gold follows the same principles as all electroless processes. For ENIG/ENEPIG lines, this cleaning stage is shared across the entire process sequence -- the same cleaner services the EN, Pd, and Au baths. The critical distinction for gold: no silicate-containing cleaners. Silicate residues on gold surfaces cause catastrophic wire bond failures in semiconductor packaging. This is a non-negotiable rule.

Hero visual: cleaning tank cross-section with silicate warning prominently featured.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank hero (Block B):** Same construction as Poster #248.
2. **Cleaning parameters (Block D):** Soak clean and PCB-specific cleaning.
3. **Silicate warning callout (Block E):** Prominent safety/quality warning.
4. **Defect grid (Block F):** 4 cleaning-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per Series Design Prompt.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- SILICATE WARNING + PCB DESMEAR (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Gold amplifies every upstream mistake. If it is not clean, it will not bond.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received substrate or EN-coated board  -->  After: Contaminant-free surface ready for gold deposition`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE SOAK CLEAN` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0". Same construction as Poster #248 with these modifications:

**Prominent silicate warning (inside tank, center):**
- Rounded rect, X: 5.0", Y: 9.0", W: 14.0", H: 1.5", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Text: `NO SILICATE CLEANERS -- silicate residues cause wire bond failure on gold surfaces` Barlow SemiBold 16 pt `#E05C5C`

**Solution labels (inside tank):**
- `NaOH: 30--60 g/L` / `Na2CO3: 15--30 g/L` / `Surfactants: 1--5 mL/L (non-silicate)` / `60--80 C (140--176 F)` / `3--10 min`

**Bottom callout (Y: 13.0"):**
- `For ENIG/ENEPIG lines, this cleaner services the entire process. One contaminated bath affects every layer above it.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaning Parameters

**Section label:** `CLEANING METHODS` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- General Alkaline Clean (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `ALKALINE SOAK CLEAN` Barlow SemiBold 20 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| NaOH | 30--60 g/L |
| Na2CO3 | 15--30 g/L |
| Surfactants | 1--5 mL/L (non-silicate, non-foaming) |
| Temperature | 60--80 C (140--176 F) |
| Time | 3--10 minutes (soak) |
| Agitation | Air or mechanical |
| Water-break test | Mandatory after rinse |

**Right -- PCB / ENIG Specific (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `PCB / ENIG CLEANING` Barlow SemiBold 20 pt `#E8A020`
- Content:
  - `Cleaner/conditioner shared with EN process`
  - `Microetch: Na persulfate 100--200 g/L or H2SO4/H2O2`
  - `Purpose: micro-roughen copper for adhesion`
  - `Desmear (multilayer): KMnO4 50--70 g/L in NaOH`
  - `Followed by neutralizer to remove MnO2`
  - `Copper is catalytic for EN -- no Pd needed`

---

### ZONE 5 -- Silicate Warning + PCB Desmear

**Section label:** `CRITICAL NOTES` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Silicate Warning (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, left accent `#E05C5C` 0.06"
- Title: `SILICATE CLEANERS: BANNED` Barlow SemiBold 20 pt `#E05C5C`
- Content:
  - `Silicate residues on gold cause wire bond failures`
  - `Even trace silicate contamination degrades bonding`
  - `Verify cleaner formulation is silicate-free`
  - `Test: boil rinse water sample -- if it clouds, silicate present`
  - `This rule applies to ALL gold surface finishes`
  - `No exceptions. No shortcuts.`

**Right -- Desmear Process (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `PCB DESMEAR (MULTILAYER BOARDS)` Barlow SemiBold 18 pt `#2EC4B6`
- Content:
  - `Drilling creates epoxy smear over inner copper layers`
  - `Permanganate desmear removes smear for reliable interconnects`
  - `KMnO4: 50--70 g/L in NaOH 40--50 g/L`
  - `Temperature: 75--85 C (167--185 F)`
  - `Time: 5--10 minutes`
  - `Followed by neutralizer/reducer to remove MnO2 residues`

---

### ZONE 6 -- Defect Grid

**Section label:** `CLEANING FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | WIRE BOND FAILURE | `#E05C5C` | Silicate contamination on gold surface | Switch to silicate-free cleaner immediately |
| R1C2 | SKIP PLATING | `#E05C5C` | Organic contamination blocking deposition | Improve cleaning; extend soak time |
| R2C1 | POOR Au ADHESION | `#E8A020` | Residual cleaner on EN surface | Thorough rinse between clean and EN |
| R2C2 | ROUGH DEPOSIT | `#E8A020` | Desmear residue (MnO2) not neutralized | Verify neutralizer step; check chemistry |

Each card: W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- Electroless Gold`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Electroless Gold -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The silicate warning is the one thing that makes this cleaning poster different from every other cleaning poster in the series. It needs to be visually loud -- coral border, coral fill tint, impossible to miss at 6 feet. Wire bond failure from silicate contamination is a real, documented, expensive problem in semiconductor packaging. The desmear section is PCB-specific and rounds out the poster for the ENIG audience.

---

*Alaina -- Poster #256 -- Construction Workup v1.0 -- 2026-04-26*
