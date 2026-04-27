---
Project: Plating Posters Inc
Poster Number: 428
Title: "Inspection & QA -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Sections 3.7, 3.8)"
Technical Source: PECVD post-deposition characterization -- ellipsometry (thickness + refractive index), FTIR (composition and hydrogen content), stress measurement (wafer bow / Stoney equation), BOE etch rate, adhesion testing, and particle counting. Refractive index is the primary in-line quality metric.
Process Scope: PECVD film characterization, quality verification, and acceptance criteria
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - InspectionQA
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #428 -- Construction Workup
## Inspection & QA -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 9 of the PECVD sequence -- the final quality gate. Did the film meet spec? This poster covers every measurement tool in the PECVD QA arsenal: ellipsometry for thickness and refractive index, FTIR for composition, wafer bow for stress, BOE etch rate as a film quality proxy, and adhesion testing. The hero visual is a film property dashboard showing target values for the five most common PECVD films.

Amber dominates -- this is a quality/verification stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Film property dashboard (Block B -- HERO):** Target values for 5 PECVD films across 5 metrics.
2. **Measurement techniques (Block C):** Five characterization methods with what they measure, how they work, and accuracy.
3. **FTIR reference (Block D):** Key absorption peaks for PECVD films -- the "fingerprints" of film composition.
4. **Acceptance criteria flowchart (Block E):** Pass/fail decision tree.
5. **Optional post-deposition anneal (Block F):** When and why to anneal PECVD films.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 20.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber)
ZONE 3 -- FILM PROPERTY DASHBOARD HERO (4.2"--13.5" / ~9.3")
  Block B: Five-film property target matrix
ZONE 4 -- MEASUREMENT TECHNIQUES (13.5"--20.5" / ~7.0")
  Block C: Five characterization methods
ZONE 5 -- FTIR + ACCEPTANCE + ANNEAL (20.5"--32.5" / ~12.0")
  Block D: FTIR reference peaks
  Block E: Pass/fail acceptance criteria
  Block F: Post-deposition anneal
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stage 9 of 10 -- Film Characterization and Acceptance` -- 28 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Refractive index tells you if the stoichiometry is right. Thickness tells you if the rate was stable. Stress tells you if the film will survive. Measure all three.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#E8A020`
- Big number: `1.46` -- Barlow Condensed ExtraBold, 64 pt, `#E8A020`
- Label: `SiO2 TARGET n` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Refractive index = primary QA metric` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Stage 9 (`Inspection & QA`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: Cooled, unloaded substrate with deposited film  -->  Output: Measured, documented, accepted or rejected`

---

### ZONE 3 -- Film Property Dashboard Hero

**Section label:** `FILM PROPERTY TARGETS -- DO YOUR NUMBERS MATCH?` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Five-Film Property Matrix**

Y: 5.0" to 13.3". Full width.

Large table with 5 film rows x 6 property columns:

| Film | Refractive Index (n) | Dielectric Constant (k) | Hardness | Film Stress | BOE Etch Rate |
|---|---|---|---|---|---|
| SiO2 | 1.46--1.47 | 4.0--4.5 | 6--8 GPa | < 200 MPa (comp.) | 200--400 nm/min |
| Si3N4 | 1.85--2.05 | 6.0--7.5 | 15--25 GPa | < 300 MPa (comp.) | Very slow (< 5 nm/min) |
| SiNx:H (solar) | 2.0--2.1 (tunable) | 5--7 | 12--18 GPa | < 200 MPa | Slow |
| a-Si:H | 3.5--4.5 | 11--12 | -- | Variable | -- |
| DLC (a-C:H) | 1.8--2.4 | 3--5 | 10--30 GPa | < 1 GPa (comp.) | -- |

Header row: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 1.2" each.

Film names: Barlow SemiBold, 16 pt, left-aligned. Each film row gets a left accent strip:
- SiO2: `#2EC4B6`
- Si3N4: `#E8A020`
- SiNx:H: `#27AE60`
- a-Si:H: `#C8D0D8`
- DLC: `#E05C5C`

Property values: JetBrains Mono Regular, 13 pt, `#F0EDE8`.
Column headers: Barlow SemiBold, 13 pt, `#F0EDE8`.

Bottom callout:
- Rounded rect, W: 22.0", H: 0.8", fill `#E8A020` at 10%, border 1 pt `#E8A020`
- Text: `REFRACTIVE INDEX is the single most informative QA metric for PECVD films. If n matches the target, stoichiometry is correct. If n drifts, the gas ratio has shifted.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 4 -- Measurement Techniques

**Section label:** `MEASUREMENT TECHNIQUES -- YOUR QA TOOLKIT` -- Y: 13.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK C -- Five Technique Cards**

Y: 14.3" to 20.3". Five cards in a vertical stack.

Each card: Rounded rect, W: 23.0", H: 1.1", fill `#1E2435`, left accent 3 pt, radius 6.

| Card | Technique | What It Measures | Accuracy | Destructive? | Accent |
|---|---|---|---|---|---|
| 1 | ELLIPSOMETRY | Thickness + refractive index | +/- 0.5 nm thickness; +/- 0.01 n | No | `#E8A020` |
| 2 | FTIR SPECTROSCOPY | Film composition -- Si-O, Si-N, Si-H, N-H bond peaks | Qualitative to semi-quantitative | No | `#2EC4B6` |
| 3 | WAFER BOW (STONEY EQUATION) | Film stress (tensile vs. compressive) | +/- 10 MPa | No | `#27AE60` |
| 4 | BOE ETCH RATE | Film density proxy -- lower etch rate = denser film | +/- 5% | Yes (partial etch) | `#C8D0D8` |
| 5 | TAPE / SCRATCH ADHESION | Film adhesion to substrate | Qualitative (pass/fail) | Yes (localized) | `#E05C5C` |

Card interior:
- Technique: Barlow SemiBold, 16 pt, accent color
- Measures: Inter Regular, 12 pt, `#F0EDE8`
- Accuracy: JetBrains Mono, 11 pt, `#F0EDE8` at 70%
- Destructive flag: Inter Medium, 11 pt, `#27AE60` for No, `#E05C5C` for Yes

Reference note: `Ellipsometry is the workhorse. FTIR confirms composition. Stress catches problems before they cause yield loss. BOE etch rate is the quick-and-dirty film quality check.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- FTIR Reference + Acceptance Criteria + Anneal

**BLOCK D -- FTIR Reference Peaks (Left, X: 0.5", W: 11.0")**

Section label: `FTIR FINGERPRINTS -- WHAT THE PEAKS TELL YOU` -- Y: 20.7". Barlow Condensed ExtraBold, 20 pt, `#2EC4B6`.

Y: 21.3" to 25.5".

| Peak Position (cm-1) | Bond | Interpretation |
|---|---|---|
| ~1060 | Si-O stretch | Primary SiO2 peak -- shift indicates off-stoichiometry |
| ~810 | Si-O bend | Secondary SiO2 confirmation |
| ~880 | Si-N stretch | Primary Si3N4 peak |
| ~2100 | Si-H stretch | Hydrogen in film -- higher = more H, less dense |
| ~3340 | N-H stretch | Hydrogen bonded to nitrogen -- indicates Si3N4 quality |
| ~2350 | CO2 (atmospheric) | Ignore -- background artifact from spectrometer |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Bond column: Inter Medium, 12 pt, `#2EC4B6`.

Callout: `Track the Si-H peak at 2100 cm-1 over time. Rising Si-H content means your film is getting more hydrogen-rich -- chamber condition is degrading or temperature has drifted.` -- Inter Medium, 12 pt, `#E8A020`

**BLOCK E -- Acceptance Criteria (Right, X: 12.0", W: 11.5")**

Section label: `ACCEPT / REJECT DECISION` -- Y: 20.7". Barlow Condensed ExtraBold, 20 pt, `#E8A020`.

Y: 21.3" to 25.5".

Decision flow (top to bottom):

Step 1: `Measure thickness by ellipsometry`
- PASS: `Within +/- 5% of target` -> continue
- FAIL: `Outside tolerance` -> `REJECT -- investigate rate drift`

Step 2: `Measure refractive index`
- PASS: `Within +/- 0.02 of target` -> continue
- FAIL: `Outside tolerance` -> `REJECT -- gas ratio shifted`

Step 3: `Measure stress (wafer bow)`
- PASS: `< specified limit (typically 200--300 MPa)` -> continue
- FAIL: `Excessive stress` -> `HOLD -- may need anneal or recipe adjustment`

Step 4: `Visual inspection`
- PASS: `No haze, particles, discoloration, peeling` -> `ACCEPT`
- FAIL: `Visible defects` -> `REJECT -- investigate contamination or process drift`

PASS: Green fill `#27AE60` at 15%, text `#27AE60`. FAIL: Red fill `#E05C5C` at 15%, text `#E05C5C`.

Flow: Barlow SemiBold for step labels, Inter Regular for criteria, arrows 2 pt `#3A4055`.

**BLOCK F -- Post-Deposition Anneal (Full width, Y: 26.0" to 32.3")**

Section label: `OPTIONAL: POST-DEPOSITION ANNEAL` -- Barlow Condensed ExtraBold, 22 pt, `#27AE60`. Y: 26.2".

Callout panel: Rounded rect, X: 0.5", Y: 26.8", W: 23.0", H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`.

Two columns:

Left -- When to Anneal (X: 1.5", W: 10.0"):
- `PECVD SiO2 for interlayer dielectric:` -- Barlow SemiBold, 16 pt, `#27AE60`
- `Anneal at 400--450 degC in N2 for 30--60 min` -- Inter Regular, 14 pt, `#F0EDE8`
- Benefits:
```
Drives out hydrogen -> densifies film
Reduces BOE etch rate (closer to thermal SiO2)
Lowers dielectric leakage current
Improves long-term stability
```

Right -- When NOT to Anneal (X: 12.5", W: 10.5"):
- `DO NOT anneal if:` -- Barlow SemiBold, 16 pt, `#E05C5C`
```
Substrate cannot survive 400 degC (polymers, assembled devices)
Film is intentionally H-rich (solar SiNx:H -- H provides passivation)
Application does not require densification (barrier coatings)
```

Bottom note:
- `For solar SiNx:H, the hydrogen IS the product. Annealing drives out hydrogen and destroys passivation. Know your application before you anneal.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & QA -- PECVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Film property targets and measurement techniques shown are representative of PECVD operations. Specific acceptance criteria depend on your application, customer specification, and equipment capabilities.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the "did we nail it?" poster. The film property dashboard (Block B) should be the first thing an engineer looks at -- five films, five metrics, all in one table. Refractive index gets special emphasis because it is the single most informative measurement: if n is on target, the film composition is correct. The FTIR reference is a deep-cut detail that process engineers will genuinely appreciate -- knowing that Si-H at 2100 cm-1 tracks hydrogen content is the kind of insight that separates routine operators from skilled technicians.

The anneal guidance (Block F) is deliberately placed last and marked "optional" because annealing is not universal -- solar applications specifically NEED the hydrogen that annealing removes. This nuance prevents well-meaning operators from ruining passivation films.

---

*Alaina -- Poster #428 -- Construction Workup v1.0 -- 2026-04-26*
