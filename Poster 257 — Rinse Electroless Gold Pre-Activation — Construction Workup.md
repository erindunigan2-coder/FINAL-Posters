---
Project: Plating Posters Inc
Poster Number: 257
Title: "Rinse -- Electroless Gold -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Pre-activation rinse for electroless gold (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessGold
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ENIG
---

# Poster #257 -- Construction Workup
## Rinse -- Electroless Gold -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of 8. For ENIG/ENEPIG, this is the rinse after EN plating and before the gold bath. It removes EN bath drag-out -- hypophosphite and nickel ions that would contaminate the gold bath if carried in. For standalone autocatalytic gold, this is the standard pre-activation rinse. The unique concern here: hypophosphite drag-in to the gold bath can reduce Au3+ uncontrollably.

Hero visual: counterflow rinse system with contamination pathway indicators specific to the EN-to-Au transition.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Same counterflow construction as previous rinse posters.
2. **EN drag-out contamination table (Block D):** What EN chemistry does to the Au bath.
3. **ENIG vs. autocatalytic rinse considerations (Block E):** Different rinse priorities.
4. **Defect grid (Block F):** 4 rinse-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:** Standard 7-zone layout.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- EN DRAG-OUT CONTAMINATION TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- ENIG vs. AUTOCATALYTIC RINSE NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Pre-Activation -- Electroless Gold -- Stage 2 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Hypophosphite in the gold bath is a recipe for uncontrolled deposition. Rinse it out here.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: EN/cleaner chemistry on surface  -->  After: Clean surface entering gold deposition`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `PRE-GOLD RINSE -- REMOVING EN DRAG-OUT` -- Y: 4.4".

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0". Standard counterflow construction.

**Contamination pathway (left side):**
- Red dashed arrows from left labeled `EN bath drag-out`
- Species labels: `Hypophosphite`, `Orthophosphite`, `Ni2+ ions` in JetBrains Mono 12 pt `#E05C5C`

**Clean exit (right side):**
- Green arrow to right labeled `Clean surface to Au bath`

**Key parameters:**
- `DI counterflow (2-stage minimum)` JetBrains Mono 14 pt `#2EC4B6`
- `Ambient temperature` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 seconds per stage` JetBrains Mono 14 pt `#F0EDE8`
- `Target: < 50 uS/cm` JetBrains Mono 14 pt `#27AE60`

**Warning callout (inside tank):**
- Rounded rect, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- `CRITICAL: Hypophosphite drag-in reduces Au3+ uncontrollably in the gold bath` Barlow SemiBold 14 pt `#E05C5C`

---

### ZONE 4 -- EN Drag-Out Contamination Table

**Section label:** `WHAT EN DRAG-OUT DOES TO THE GOLD BATH` -- Y: 14.7".

**BLOCK D -- Contamination Table (Y: 15.3" to 20.3")**

| Contaminant | Source | Effect on Au Bath | Prevention |
|---|---|---|---|
| Hypophosphite (H2PO2-) | EN bath reducing agent | Reduces Au3+ uncontrollably; deposits gold in bulk solution | DI rinse; verify conductivity |
| Orthophosphite (H2PO3-) | EN bath byproduct | Accumulates; degrades bath stability | Thorough rinse |
| Nickel (Ni2+) | EN bath metal ions | Contamination; co-deposition; deposit quality loss | Multi-stage rinse |
| Complexants (organic acids) | EN bath complexant system | pH disruption; chelation interference | Adequate rinse volume |
| Stabilizer (Pb, thiourea) | EN stabilizer drag-out | Poisons gold bath at ppm levels | Recovery rinse before gold |

Header: fill `#3A4055`. Data: alternating `#1E2435` / `#252B3D`.

---

### ZONE 5 -- ENIG vs. Autocatalytic Rinse Notes

**Section label:** `RINSE PRIORITIES BY PROCESS TYPE` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- ENIG Rinse Priority (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ENIG / ENEPIG RINSE` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `Primary concern: EN drag-out into immersion Au bath`
  - `Hypophosphite is the #1 enemy -- reduces Au uncontrollably`
  - `Nickel ion drag-in accelerates black pad corrosion`
  - `DI water mandatory for ENIG lines`
  - `Conductivity target: <30 uS/cm for critical ENIG work`
  - `Some lines add a dedicated rinse between EN and Au`

**Right -- Autocatalytic Gold Rinse (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `AUTOCATALYTIC Au RINSE` Barlow SemiBold 18 pt `#27AE60`
- Content:
  - `Primary concern: activation chemistry drag-in`
  - `Pd activation residue: controlled -- small amounts acceptable`
  - `Acid drag-in from colloidal catalyst: pH disruption in Au bath`
  - `Standard DI counterflow sufficient`
  - `Less critical than ENIG rinse -- autocatalytic bath is more robust`
  - `Standard conductivity target: <50 uS/cm`

---

### ZONE 6 -- Defect Grid

**Section label:** `RINSE-RELATED Au BATH FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | UNCONTROLLED Au REDUCTION | `#E05C5C` | Hypophosphite drag-in from EN bath | Improve rinse; add dedicated EN rinse stage |
| R1C2 | BLACK PAD ACCELERATION | `#E05C5C` | Ni2+ drag-in accelerates corrosion | Thorough multi-stage rinse; verify conductivity |
| R2C1 | Au BATH pH DRIFT | `#E8A020` | Acid or alkaline chemistry drag-in | DI rinse; verify conductivity target |
| R2C2 | SHORT Au BATH LIFE | `#E8A020` | Cumulative contamination from poor rinsing | Tighten rinse control; consider recovery rinse |

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Electroless Gold -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Gold Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The hypophosphite drag-in warning is the unique hook for this rinse poster. It connects the EN chemistry to the Au chemistry in a way most operators do not think about. The contamination table maps each EN species to its specific effect on the gold bath -- this is immediately actionable diagnostic information. The ENIG vs. autocatalytic comparison in Zone 5 acknowledges that the rinse criticality differs by process type.

---

*Alaina -- Poster #257 -- Construction Workup v1.0 -- 2026-04-26*
