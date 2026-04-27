---
Project: Plating Posters Inc
Poster Number: 240
Title: "Cleaning -- Electroless Copper"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 2)"
Process Scope: Cleaner/conditioner and permanganate desmear for electroless copper line (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #240 -- Construction Workup
## Cleaning -- Electroless Copper

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of the electroless copper process. Cleaning for E-Cu is fundamentally different from cleaning for EN. In PCB applications, the "cleaner" is actually a cleaner/conditioner: an alkaline surfactant solution that removes drilling smear from through-holes AND conditions the dielectric surface (FR4 epoxy-glass) for subsequent Pd catalyst adsorption. For multilayer PCBs, a permanganate desmear step (KMnO4 in NaOH) follows to remove epoxy smear from inner copper layers exposed during drilling.

For plastics metallization, cleaning removes mold release agents and fingerprints. ABS substrates must not be exposed to solvents that attack the butadiene rubber phase -- that phase IS the etchable component needed for catalyst adhesion downstream.

Hero visual: PCB through-hole cross-section showing drilling smear, desmear action, and conditioned dielectric surface.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Through-hole cross-section hero (Block B):** Rectangular cross-section showing a PCB through-hole with drilling smear, desmear chemistry, and conditioned surface. Standard shape construction.
2. **Orientation strip (Block C):** 8-stage strip with Stage 1 highlighted.
3. **Dual parameter table (Block D):** PCB cleaner/conditioner + permanganate desmear parameters.
4. **Plastics cleaning panel (Block E):** ABS/PC cleaning parameters as secondary application.
5. **Problems table (Block F).**

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Standard locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2" / ~1.3")
  Block C: 8-stage strip with Stage 1 highlighted

ZONE 3 -- THROUGH-HOLE CROSS-SECTION HERO (4.2"--15.0" / ~10.8")
  Block B: PCB through-hole diagram with desmear

ZONE 4 -- FULL PARAMETER TABLE (15.0"--22.0" / ~7.0")
  Block D: Cleaner/conditioner + permanganate desmear

ZONE 5 -- PLASTICS CLEANING + COMMON PROBLEMS (22.0"--28.5" / ~6.5")
  Block E: Plastics cleaning parameters
  Block F: Common problems table

ZONE 6 -- SAFETY CALLOUT (28.5"--32.5" / ~4.0")
  Block G: Chemical hazards (permanganate, NaOH) + PPE

ZONE 7 -- FOOTER BAND (32.5"--36.0" / ~3.5")
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Cleaner/Conditioner & Desmear -- Stage 1 of 8` -- Barlow SemiBold, 30 pt, `#2EC4B6` (Teal). X: 0.5", Y: 1.4".

**Tagline:** `Not just cleaning -- conditioning. The dielectric surface must adsorb Pd catalyst or no copper will deposit. For multilayer PCBs, permanganate desmear exposes inner copper layers.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

**BLOCK C -- 8-Stage Strip**

Y: 3.0" to 4.1". Container: Rounded rect, X: 0.5", Y: 3.0", W: 23.0", H: 1.0", fill `#252B3D`, radius 4.

Eight mini-boxes (each ~2.6" wide, 0.6" tall):

| Box | Label | Fill | Text Color | Opacity |
|---|---|---|---|---|
| 1 | `1 CLEAN` | `#2EC4B6` | `#1A1F2E` | 100% (highlighted) |
| 2 | `2 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 3 | `3 ACTIVATE` | `#3A4055` | `#F0EDE8` | 40% |
| 4 | `4 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 5 | `5 E-Cu BATH` | `#3A4055` | `#F0EDE8` | 40% |
| 6 | `6 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 7 | `7 ANTI-TAR` | `#3A4055` | `#F0EDE8` | 40% |
| 8 | `8 ELEC Cu` | `#3A4055` | `#F0EDE8` | 40% |

Label font: Barlow Condensed ExtraBold, 11 pt. Arrows between boxes.

Below: `Before: Drilled PCB with smeared through-holes  -->  After: Clean, conditioned dielectric surface ready for Pd activation`

---

### ZONE 3 -- Through-Hole Cross-Section Hero

**Section label:** `THE PCB THROUGH-HOLE -- BEFORE AND AFTER CLEANING` -- Y: 4.4".

**BLOCK B -- Through-Hole Diagram**

Y: 5.0" to 14.5" (~9.5" tall).

**Left half -- BEFORE (X: 0.5", W: 11.0"):**

PCB cross-section (simplified):
- Rectangular board outline: X: 1.0", Y: 6.0", W: 10.0", H: 6.0"
- Fill: `#252B3D` (FR4 dielectric)
- Top and bottom copper layers: thin rectangles, H: 0.3", fill `#E8A020` at 60% (copper-colored)
- Inner copper layers (2 layers): thin rectangles at Y: 8.0" and Y: 10.0", fill `#E8A020` at 40%
- Through-hole: vertical rectangle, X: 5.0", W: 1.0", through full board height, fill `#1A1F2E`

Drilling smear indicators:
- Small irregular shapes (circles/ovals) covering inner copper layer edges at through-hole wall
- Fill: `#E05C5C` at 40%
- Label: `DRILLING SMEAR` Barlow SemiBold 14 pt `#E05C5C`
- Arrow pointing to smear: `Epoxy smear covers inner Cu layers -- blocks connection` Inter Regular 12 pt `#E05C5C`

Title: `BEFORE CLEANING` Barlow SemiBold 18 pt `#E05C5C`. Y: 5.2".

**Right half -- AFTER (X: 12.5", W: 11.0"):**

Same PCB cross-section but:
- Drilling smear removed
- Inner copper layers clearly exposed at through-hole wall
- Dielectric surface has subtle texture (conditioned)
- Labels: `SMEAR REMOVED` `#27AE60`, `INNER Cu EXPOSED` `#27AE60`, `DIELECTRIC CONDITIONED` `#2EC4B6`

Title: `AFTER CLEANING + DESMEAR` Barlow SemiBold 18 pt `#27AE60`. Y: 5.2".

**Bottom callout (Y: 13.0"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.2", fill `#1E2435`, border-left 0.06" `#E8A020`
- `Permanganate desmear: KMnO4 oxidizes epoxy smear from inner Cu layers. The conditioner polymer conditions the dielectric for Pd adsorption. Both steps are essential for multilayer PCB reliability.`

---

### ZONE 4 -- Full Parameter Table

**Section label:** `CLEANING PARAMETERS -- DETAILED` -- Y: 15.2".

**Left -- Cleaner/Conditioner (X: 0.5", W: 11.0"):**

Header: `CLEANER/CONDITIONER (PCB)` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Chemistry | Proprietary alkaline cleaner/conditioner |
| pH | 10-12 |
| Temperature | 40-55 C (105-130 F) |
| Time | 3-5 min |
| Agitation | Air or conveyorized |
| Purpose | Remove smear; condition dielectric for Pd |

**Right -- Permanganate Desmear (X: 12.0", W: 11.5"):**

Header: `PERMANGANATE DESMEAR (MULTILAYER PCB)` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Chemistry | KMnO4 50-70 g/L in NaOH 40-50 g/L |
| Temperature | 75-85 C (165-185 F) |
| Time | 5-10 min |
| Followed by | Neutralizer/reducer (hydroxylamine or proprietary) |
| Purpose | Oxidize and remove epoxy smear from inner Cu |
| MnO2 residues | MUST be neutralized -- poisons Pd catalyst |

Data: JetBrains Mono 13 pt. Rows alternate `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Plastics Cleaning + Common Problems

**Left -- Plastics Cleaning (X: 0.5", W: 11.0", Y: 22.2" to 25.5"):**

Title: `PLASTICS CLEANING` Barlow SemiBold 20 pt `#E8A020`. Y: 22.2".

**ABS:**
- `Alkaline soak: NaOH 30-45 g/L + surfactant; 50-60 C; 5-10 min`
- `Remove mold release, fingerprints, surface oils`
- `DO NOT use solvents that attack butadiene rubber phase`

**Polycarbonate:**
- `Mild alkaline soak; lower temp (45-50 C) to avoid surface stress`

**Right -- Common Problems (X: 12.0", W: 11.5", Y: 22.2" to 28.3"):**

Title: `WHAT GOES WRONG AT CLEANING` Barlow SemiBold 20 pt `#E05C5C`. Y: 22.2".

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Incomplete desmear | Inner layer interconnect failure | Permanganate too weak or time too short | Increase KMnO4; extend time |
| MnO2 residue | No Cu deposition in through-hole | Neutralizer exhausted or skipped | Replenish neutralizer; check step |
| Over-conditioning | Excessive catalyst adsorption downstream | Conditioner too concentrated | Reduce concentration; check TDS |
| Smear on vias | Voiding in microvias | Drill parameters too aggressive | Adjust drill speed; improve desmear |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety Callout

**Section label:** `SAFETY -- CLEANING AND DESMEAR CHEMISTRY` -- Barlow Condensed ExtraBold 24 pt `#E8A020`. Y: 28.7".

**Left -- Chemical Hazards (X: 0.5", W: 11.0"):**
- Title: `CHEMICAL HAZARDS` `#E05C5C`
- `KMnO4: strong oxidizer -- fire risk with organics`
- `KMnO4 stains skin and surfaces permanently (purple/brown)`
- `NaOH: severe burns -- pH > 12`
- `Hot desmear solution (165-185 F): thermal burn risk`
- `Hydroxylamine neutralizer: skin sensitizer`

**Right -- PPE Requirements (X: 12.0", W: 11.5"):**
- Title: `REQUIRED PPE` `#E8A020`
- `Chemical splash goggles or face shield`
- `Chemical-resistant gloves (nitrile or neoprene)`
- `Chemical-resistant apron`
- `Eyewash station within 10 seconds`
- `Separate spill kits for oxidizer (KMnO4) and alkali (NaOH)`
- `SDS posted for all chemicals`

---

### ZONE 7 -- Footer Band

Standard footer:
- Disclaimer: `...typical industry values for cleaning and desmear in electroless copper plating for PCB and plastics metallization...`
- Title: `Cleaning -- Electroless Copper`
- Version `v1.0 -- 2026`

---

## Part 5 -- Grouping

| Group | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | 8-stage strip, Stage 1 highlighted |
| Zone 3 - Hero | Through-hole cross-section (before/after) |
| Zone 4 - Parameters | Cleaner/conditioner + permanganate desmear |
| Zone 5 - Plastics + Problems | Plastics cleaning, problem table |
| Zone 6 - Safety | Chemical hazards, PPE |
| Zone 7 - Footer | Standard footer |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap table (same as Poster #239).

---

## Part 7 -- Export Checklist

| File Name | Quality | Bleed |
|---|---|---|
| `Cleaning E-Cu -- Dark -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning E-Cu -- Dark -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning E-Cu -- Dark -- Digital.pdf` | Standard | No |
| `Cleaning E-Cu -- Light -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning E-Cu -- Light -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning E-Cu -- Light -- Digital.pdf` | Standard | No |

---

## Design Notes

The PCB through-hole cross-section is the unique hero for this poster -- nothing like the soak tank diagrams used in EN cleaning posters. The before/after comparison showing drilling smear covering inner copper layers is the visual hook. Every PCB fabricator knows that incomplete desmear causes interconnect failures in the field -- this is a reliability-critical step, not just a cleaning step.

The 8-stage orientation strip (vs. 7 for EN) is the first visual signal that E-Cu has a different process architecture.

---

*Alaina -- Poster #240 -- Construction Workup v1.0 -- 2026-04-26*
