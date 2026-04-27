---
Project: Plating Posters Inc
Poster Number: 251
Title: "Rinse -- Electroless Palladium -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Process Scope: Pre-plate rinse for electroless palladium (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessPalladium
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #251 -- Construction Workup
## Rinse -- Electroless Palladium -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This is the most critical rinse in the electroless palladium process line. It removes acid, activation chemistry, or EN bath drag-out before entering the Pd bath. Contamination drag-in to the Pd bath can cause pitting, stabilizer poisoning, or uncontrolled deposition. For ENEPIG, the main concern is removing EN bath drag-out (hypophosphite, orthophosphite, nickel) before the Pd bath.

Hero visual: counterflow rinse system with contamination pathway indicators.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Counterflow rinse with contamination callouts. Same construction approach as Poster #249.
2. **Critical contamination table (Block D):** What contaminants do what in the Pd bath.
3. **Transfer time callout (Block E):** Speed matters -- surface oxidation.
4. **Defect grid (Block F):** 4 rinse-related defects.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION CONCERNS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- TRANSFER TIME + SURFACE OXIDATION (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Pre-Plate -- Electroless Palladium -- Stage 4 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last line of defense before the Pd bath. What you drag in, you deposit around.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activation chemistry residue on surface  -->  After: Clean, ready surface entering Pd bath`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE CRITICAL PRE-PLATE RINSE` -- Y: 4.4".

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0".

Same counterflow tank construction as Poster #249 with these modifications:

**Contamination pathway indicators:**
- Red dashed arrows from left (activation/EN bath) carrying contaminants into rinse
- Labels on arrows: `Acid drag-in`, `EN drag-out`, `Activation residue`
- Green check on clean exit path (right side toward Pd bath)

**Key parameters displayed in tank:**
- `DI preferred` JetBrains Mono 14 pt `#2EC4B6`
- `Ambient (18--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 seconds per stage` JetBrains Mono 14 pt `#F0EDE8`
- `Target: < 20 uS/cm for critical work` JetBrains Mono 14 pt `#27AE60`

**Transfer time warning (top right):**
- Rounded rect, W: 6.0", H: 1.2", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `MINIMIZE TRANSFER TIME -- Pd surface oxidizes in air` Barlow SemiBold 13 pt `#E05C5C`

**Bottom callout (Y: 13.0"):**
- `For ENEPIG: this rinse removes EN bath drag-out. Hypophosphite drag-in to Pd bath can cause uncontrolled deposition.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Contamination Concerns Table

**Section label:** `WHAT DRAG-IN DOES TO THE Pd BATH` -- Y: 14.7".

**BLOCK D -- Contamination Table (Y: 15.3" to 20.3")**

| Contaminant Source | Drag-In Species | Effect on Pd Bath | Prevention |
|---|---|---|---|
| EN bath | Hypophosphite, orthophosphite | Uncontrolled reduction; excess deposition | DI rinse; <20 uS/cm |
| EN bath | Ni2+ ions | Bath contamination; deposit quality loss | Thorough multi-stage rinse |
| HCl activation | Chloride (Cl-) | Pitting; accelerated bath aging | DI rinse essential |
| Sn/Pd colloidal | Excess Sn residue | Deposit roughness; initiation problems | Adequate accelerator step |
| Chromate etch (plastics) | Cr6+ traces | Stabilizer poisoning at ppm levels | Dedicated rinse before activation |

Header: fill `#3A4055`. Data: alternating `#1E2435` / `#252B3D`.
Contaminant column: Inter Medium 13 pt `#E05C5C`. Effect: JetBrains Mono 12 pt `#F0EDE8`. Prevention: Inter Medium 12 pt `#27AE60`.

---

### ZONE 5 -- Transfer Time + Surface Oxidation

**Section label:** `SPEED IS QUALITY` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Transfer Time Rules (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `TRANSFER TIME MATTERS` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `EN surface: begin oxidizing within seconds of air exposure`
  - `Pd catalytic surface: less sensitive than Ni but still degrades`
  - `ENEPIG: minimize time from EN rinse to Pd bath`
  - `Zincated aluminum: transfer within 30 seconds`
  - `Keep parts wet during transfer -- never let surfaces dry`

**Right -- Conductivity Monitoring (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `CONDUCTIVITY AS YOUR SENTINEL` Barlow SemiBold 18 pt `#27AE60`
- Content:
  - `< 20 uS/cm: excellent (critical ENEPIG work)`
  - `20--50 uS/cm: acceptable (general applications)`
  - `> 50 uS/cm: marginal -- increase rinse flow or replace water`
  - `> 100 uS/cm: unacceptable -- troubleshoot immediately`
  - `Trend the numbers daily -- rising conductivity warns before defects appear`

---

### ZONE 6 -- Defect Grid

**Section label:** `RINSE-RELATED Pd BATH FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING | `#E05C5C` | Chloride drag-in from HCl activation | Switch to DI rinse; extend rinse time |
| R1C2 | UNCONTROLLED DEPOSITION | `#E05C5C` | Hypophosphite drag-in from EN bath | Improve rinse quality; verify conductivity |
| R2C1 | DELAYED INITIATION | `#E8A020` | Surface oxidation from slow transfer | Reduce transfer time; keep parts wet |
| R2C2 | BATH INSTABILITY | `#E8A020` | Cumulative contamination from poor rinsing | Tighten conductivity limits; DI water |

Each card: W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Electroless Palladium -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Palladium Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the more critical of the two rinse posters in the cluster. The contamination table is the centerpiece -- it maps specific drag-in species to specific Pd bath failures, which makes it immediately actionable. The conductivity monitoring callout transforms a passive rinse step into an active quality control point. The <20 uS/cm target for critical ENEPIG work is tighter than the pre-activation rinse, reflecting the Pd bath's sensitivity.

---

*Alaina -- Poster #251 -- Construction Workup v1.0 -- 2026-04-26*
