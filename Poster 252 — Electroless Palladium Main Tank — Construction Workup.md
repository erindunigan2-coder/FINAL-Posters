---
Project: Plating Posters Inc
Poster Number: 252
Title: "Electroless Palladium -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Process Scope: Electroless palladium main plating tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessPalladium
  - MainTank
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #252 -- Construction Workup
## Electroless Palladium -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The heart of the process -- where palladium deposits autocatalytically onto the substrate. This poster is the most content-dense in the cluster. It covers both major bath types (hypophosphite for Pd-P alloy, hydrazine for pure Pd), operating parameters, deposit properties, and bath stability management. No rectifier, no anode, no external current -- this is pure chemistry driving the deposition.

Hero visual: a plating tank cross-section showing the autocatalytic process -- workpiece immersed, chemical reactions indicated, no electrodes or rectifier.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Autocatalytic tank hero (Block B):** Tank with workpiece, solution labels, deposition indicators -- NO rectifier, NO anodes. This is electroless.
2. **Dual bath composition panel (Block D):** Hypophosphite vs. hydrazine bath compositions side by side.
3. **Deposit properties comparison (Block E):** Pd-P alloy vs. pure Pd deposit properties.
4. **Defect grid (Block F):** 6 common defects.

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
  Stage 5 highlighted (Emerald)
ZONE 3 -- AUTOCATALYTIC TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DUAL BATH COMPOSITION (14.5"--20.5" / ~6.0")
ZONE 5 -- DEPOSIT PROPERTIES + BATH LIFE (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROLESS PALLADIUM` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Main Tank -- Autocatalytic Deposition -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `No rectifier. No anode. Pure chemistry deposits palladium atom by atom onto any catalytic surface.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated or EN-coated surface  -->  After: Pd or Pd-P barrier layer (0.05--0.3 um ENEPIG; 5--25 um membranes)`

---

### ZONE 3 -- Autocatalytic Tank Hero

**Section label:** `THE ELECTROLESS PALLADIUM BATH` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**NO anodes, NO rectifier** -- this is electroless. Instead:

**Workpiece (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.5", fill `#27AE60` at 20%, border 2 pt `#27AE60`
- Label above: `WORKPIECE (CATHODE-FREE)` Barlow SemiBold 14 pt `#27AE60`
- Small deposition arrows pointing inward toward workpiece surface from all directions
- Label: `Pd depositing uniformly` Inter Regular 11 pt `#27AE60`

**Autocatalytic label (above tank):**
- Rounded rect, X: 7.0", Y: 5.0", W: 10.0", H: 0.8", fill `#1E2435`, border 1 pt `#27AE60`
- Text: `AUTOCATALYTIC -- NO EXTERNAL CURRENT` Barlow SemiBold 14 pt `#27AE60`

**Reaction equation (inside tank, top):**
- `Pd2+ + H2PO2- + H2O --> Pd0 + H2PO3- + 2H+` JetBrains Mono 13 pt `#E8A020`
- Sub-label: `(Hypophosphite reducing agent -- produces Pd-P alloy)` Inter Regular 11 pt `#F0EDE8` at 60%

**Bath parameter labels (inside tank):**
Right side (X: 15.5", Y: 7.5"):
- `Pd: 0.5--3.0 g/L Pd2+` JetBrains Mono 14 pt `#27AE60`
- `Hypo: 5--15 g/L (hypo bath)` JetBrains Mono 14 pt `#2EC4B6`
- `pH: 5.0--7.0 (hypo) / 9.0--11.0 (hydrazine)` JetBrains Mono 13 pt `#F0EDE8`
- `Temp: 40--70 C (105--158 F)` JetBrains Mono 14 pt `#E8A020`

Left side (X: 2.5", Y: 7.5"):
- `Rate: 1--5 um/hr (hypo)` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Rate: 1--3 um/hr (hydrazine)` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `ENEPIG target: 0.05--0.3 um` JetBrains Mono 14 pt `#27AE60`
- `Membrane target: 5--25 um` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Heater element (bottom of tank):**
- Horizontal rect, X: 3.0", Y: 12.0", W: 18.0", H: 0.3", fill `#E8A020` at 30%
- Label: `Temperature control: +/- 2 C` Inter Regular 11 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `Uniform deposition on ALL surfaces including recesses, blind holes, and internal geometries -- the fundamental advantage of electroless.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Dual Bath Composition

**Section label:** `TWO BATH TYPES -- TWO DEPOSIT TYPES` -- Y: 14.7".

**BLOCK D -- Side-by-Side Composition (Y: 15.3" to 20.3")**

**Left -- Hypophosphite Bath (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `HYPOPHOSPHITE BATH (Pd-P)` Barlow SemiBold 18 pt `#27AE60`
- Subtitle: `Most common commercial formulation` Inter Regular 12 pt `#F0EDE8` at 50%

| Component | Concentration | Role |
|---|---|---|
| PdCl2 or Pd(NH3)4Cl2 | 0.5--3.0 g/L Pd2+ | Metal source |
| NaH2PO2 | 5--15 g/L | Reducing agent |
| EDTA or ethylenediamine | 10--30 g/L | Complexant |
| NH4OH / ammonia | As needed | pH adjuster + complexant |
| Stabilizer | 1--10 mg/L | Prevents decomposition |

Operating: `pH 5.0--7.0 | 40--70 C | 1--5 um/hr | 3--5 MTO`

**Right -- Hydrazine Bath (Pure Pd) (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `HYDRAZINE BATH (PURE Pd)` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `Phosphorus-free deposit` Inter Regular 12 pt `#F0EDE8` at 50%

| Component | Concentration | Role |
|---|---|---|
| PdCl2 | 1--3 g/L Pd2+ | Metal source |
| Hydrazine hydrate | 0.5--3 mL/L | Reducing agent |
| EDTA | 20--40 g/L | Complexant |
| NH4OH | As needed | pH adjuster |

Operating: `pH 9.0--11.0 | 50--70 C | 1--3 um/hr | 2--4 MTO`

Safety warning: `HYDRAZINE: Toxic, suspected carcinogen. Requires engineering controls and PPE.` Inter Medium 12 pt `#E05C5C`

---

### ZONE 5 -- Deposit Properties + Bath Life

**Section label:** `DEPOSIT PROPERTIES AND BATH MANAGEMENT` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Deposit Properties Table (X: 0.5", W: 11.0"):**

| Property | Pd-P Alloy | Pure Pd |
|---|---|---|
| Composition | Pd + 1--7% P | >99% Pd |
| Structure | Amorphous | Crystalline |
| Hardness | 400--600 HV | 200--300 HV |
| Corrosion resistance | Excellent | Excellent |
| Solderability | Excellent | Excellent |
| Wire bondability | Excellent | Excellent |
| H2 permeability | Moderate | Excellent |
| Magnetic | Non-magnetic | Non-magnetic |

**Right -- Bath Life Management (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `BATH LIFE MANAGEMENT` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `Hypophosphite bath: 3--5 MTO` JetBrains Mono 14 pt `#27AE60`
  - `Hydrazine bath: 2--4 MTO` JetBrains Mono 14 pt `#E8A020`
  - `Pd is expensive -- bath economics matter`
  - `Stabilizer: too low = decomposition risk; too high = bath goes inert`
  - `Filter continuously (5 um); remove metallic fines`
  - `Never leave bath at temp without parts or dummy load`
  - `Monitor Pd concentration by titration or ICP`

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP PLATING | `#E05C5C` | Poor activation; contaminated surface | Verify catalytic surface; improve cleaning |
| R1C2 | BATH DECOMPOSITION | `#E05C5C` | Low stabilizer; overheating; under-loaded | Check stabilizer ppm; reduce temperature |
| R1C3 | PITTING | `#E8A020` | Chloride contamination; H2 entrapment | Improve pre-plate rinse; add agitation |
| R2C1 | THICKNESS VARIATION | `#2EC4B6` | Temperature gradient across bath | Improve heating uniformity; add agitation |
| R2C2 | DARK DEPOSIT | `#E8A020` | Organic contamination or excess stabilizer | Carbon treat; reduce stabilizer |
| R2C3 | ROUGH DEPOSIT | `#2EC4B6` | Particulate in bath; metallic fines | Increase filtration; check filter integrity |

Each card: W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard footer. Title: `Electroless Palladium -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; IPC-4556; ASTM standards. Specific formulations vary by proprietary product.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Electroless Palladium Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the Electroless Palladium cluster. The hero visual must clearly communicate "no rectifier, no anode" -- this is what makes electroless fundamentally different from electrolytic plating. The dual bath composition is the central design challenge: two different chemistries producing two different deposits. The deposition equation displayed inside the tank connects the visual to the underlying science. The "ENEPIG target: 0.05-0.3 um" callout is the number most users are looking for -- make it prominent.

---

*Alaina -- Poster #252 -- Construction Workup v1.0 -- 2026-04-26*
