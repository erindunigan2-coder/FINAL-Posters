---
Project: Plating Posters Inc
Poster Number: 345
Title: "Bath Preparation & Control -- Alkaline Cleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-1.3)"
Process Scope: Bath makeup, composition, analytical control, and dump criteria for alkaline soak cleaners
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - AlkalineCleaning
  - BathPreparation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT01
---

# Poster #345 -- Construction Workup
## Bath Preparation & Control -- Alkaline Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 3 of 7 in the CT-01 cluster. This is the chemistry poster -- how to build the tank, what goes in it, how to keep it running, and when to dump it. The hero visual is a bath composition breakdown showing six components and their functions. The analytical control section covers titration and bath life monitoring. The makeup procedure is a numbered step-by-step that an operator can follow directly.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Bath composition breakdown (Block B -- HERO):** Six-component visual showing NaOH, silicate, carbonate, surfactant, phosphate, and chelator with functions and concentration ranges.
2. **Makeup procedure (Block D):** Numbered step-by-step sequence (6 steps).
3. **Analytical control panel (Block E):** Titration methods and frequency.
4. **Bath life / dump criteria table (Block F):** Four-parameter action-level table.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 3 of 7 highlighted (Teal)
ZONE 3 -- BATH COMPOSITION BREAKDOWN / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- MAKEUP PROCEDURE (15.0"--21.0" / ~6.0")
ZONE 5 -- ANALYTICAL CONTROL (21.0"--27.0" / ~6.0")
ZONE 6 -- BATH LIFE & DUMP CRITERIA (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `BATH PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Alkaline Cleaning -- Building and Controlling the Soak Tank` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Six components, one goal: dissolve every trace of soil without attacking the substrate. Here is what goes in the tank and why.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Empty tank --> After: Fully charged cleaner at operating concentration and temperature`

---

### ZONE 3 -- Bath Composition Breakdown (HERO)

**Section label:** `WHAT IS IN YOUR SOAK CLEANER -- 6 COMPONENTS` -- Y: 4.4".

**BLOCK B -- Six-Component Visual**

Y: 5.0" to 14.5". Six callout boxes in a 3x2 grid.

| Component | Position | Accent | Concentration (Steel) | Function |
|---|---|---|---|---|
| Sodium Hydroxide (NaOH) | R1C1 (X: 0.5") | `#2EC4B6` | 45-90 g/L (6-12 oz/gal) | Primary alkalinity; saponification agent -- reacts with fats to form water-soluble soaps |
| Sodium Metasilicate (Na2SiO3) | R1C2 (X: 8.0") | `#E8A020` | 15-45 g/L (2-6 oz/gal) | Builder; etch inhibitor (critical for aluminum); aids soil suspension in solution |
| Sodium Carbonate (Na2CO3) | R1C3 (X: 15.5") | `#27AE60` | 15-30 g/L (2-4 oz/gal) | Alkalinity buffer; softens water hardness (precipitates Ca/Mg) |
| Surfactant (Nonionic) | R2C1 (X: 0.5") | `#2EC4B6` | 0.5-3 g/L | Wetting, emulsification, foam control -- the key to removing non-saponifiable oils |
| Sodium Tripolyphosphate (STPP) | R2C2 (X: 8.0") | `#E8A020` | 7-22 g/L (1-3 oz/gal) | Chelation of Ca/Mg hardness; soil dispersant; prevents redeposition |
| Chelating Agent (EDTA or Gluconate) | R2C3 (X: 15.5") | `#27AE60` | 2-10 g/L | Sequestration of dissolved metals (Fe, Zn, Cu) that interfere with cleaning |

Each box: Rounded rect W: 7.0", H: 4.5", fill `#1E2435`, left accent 0.06".

Interior per box:
- Component name: Barlow SemiBold 16 pt, accent color
- Formula: JetBrains Mono 14 pt, `#F0EDE8` at 70%
- Concentration: JetBrains Mono 16 pt, accent color
- Function: Inter Regular 13 pt `#F0EDE8`, line height 150%

**Aluminum modification callout (Y: 14.0"):**
- Rounded rect, W: 23.0", H: 0.8", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `FOR ALUMINUM: Reduce NaOH to 10-30 g/L. Increase silicate to 30-60 g/L. Reduce temp to 120-150 F. Reduce time to 1-3 min.` -- Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Makeup Procedure

**Section label:** `TANK MAKEUP -- STEP BY STEP` -- Y: 15.2".

**BLOCK D -- Numbered Procedure (Y: 15.8" to 20.8")**

Six numbered steps in a vertical sequence. Each step is a rounded rect, full width (23.0"), H: 0.75", fill alternating `#1E2435` / `#252B3D`.

| Step | Instruction | Caution |
|---|---|---|
| 1 | Fill tank to 2/3 volume with warm water (40-50 C / 105-120 F) | Use warm water to aid dissolution |
| 2 | Add NaOH slowly with agitation | EXOTHERMIC -- temperature will rise significantly. Add gradually. |
| 3 | Add silicate, carbonate, and phosphate builders | Dissolve each component before adding next |
| 4 | Add surfactant LAST | Adding surfactant early causes excessive foaming during mixing |
| 5 | Bring to operating volume and temperature | Target: 140-195 F (60-90 C) for steel; lower for aluminum |
| 6 | Titrate to confirm concentration before use | Do NOT plate from a new tank without analytical verification |

Step number: Barlow Condensed ExtraBold 20 pt, `#2EC4B6`, in a 0.6" circle fill `#2EC4B6` at 20%.
Instruction: Inter Medium 14 pt `#F0EDE8`.
Caution: Inter Regular 12 pt `#E8A020` (or `#E05C5C` for step 2).

---

### ZONE 5 -- Analytical Control

**Section label:** `KEEPING IT RIGHT -- ANALYTICAL CONTROL` -- Y: 21.2".

**BLOCK E -- Control Panel (Y: 21.8" to 26.8")**

Two-column layout.

**Left -- Titration Methods (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `TITRATION` Barlow SemiBold 18 pt `#2EC4B6`

| Test | Method | Endpoint |
|---|---|---|
| Total Alkalinity | Titrate with standardized HCl or H2SO4 | Phenolphthalein and/or methyl orange |
| Free Alkalinity (NaOH) | BaCl2 precipitation + titrate to phenolphthalein | Isolates NaOH from carbonate |

- JetBrains Mono 13 pt for method details
- Frequency: `Daily on heavy-use lines; 2-3x per week on moderate lines` Inter Medium 13 pt `#E8A020`

**Right -- What to Watch (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `WHAT TO WATCH` Barlow SemiBold 18 pt `#E8A020`

Bullet items, Inter Regular 13 pt `#F0EDE8`:
- `NaOH concentration drops with use -- replenish based on titration`
- `Surfactant decomposes over time -- add to restore wetting action`
- `Oil loading visible as floating oil or soil on surface`
- `Dissolved metals accumulate -- Fe, Zn, Cu from substrates`
- `Carbonate builds from CO2 absorption and organic decomposition`

---

### ZONE 6 -- Bath Life & Dump Criteria

**Section label:** `WHEN TO DUMP -- BATH LIFE INDICATORS` -- Y: 27.2".

**BLOCK F -- Dump Criteria Table (Y: 27.8" to 32.3")**

Column widths: Parameter (5.0") | Action Level (5.0") | Symptom (6.5") | Response (6.5")

Header row: fill `#E05C5C` at 25%, H: 0.5".

| Parameter | Action Level | Symptom | Response |
|---|---|---|---|
| Oil Loading | > 5-10 g/L total oil | Bath losing cleaning efficiency; parts not passing water break | Partial dump + rebuild; improve pre-cleaning |
| Soil Redeposition | Visible on parts | Cleaned parts show residual soil or haze after rinse | Dump or partial dump + rebuild |
| Dissolved Metals (Fe + Zn + Cu) | > 5-10 g/L total | Interferes with surfactant; cleaning quality degrades | Partial dump; add chelating agent |
| Water Break Failure Rate | > 10% of parts | Systematic cleaning failure | Investigate root cause; rebuild if chemistry cannot be corrected |

Data: Inter Regular 13 pt. Action levels: JetBrains Mono 14 pt `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Bath Preparation & Control -- Alkaline Cleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook. Specific product concentrations vary by supplier formulation. Consult your process supplier TDS for exact makeup instructions.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Bath Preparation Control Alkaline Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster lives next to the soak tank. The operator uses it during makeup and the lab tech uses it for analytical control. The six-component hero is the most important visual -- it answers "why is each ingredient here?" which most operators never learn. The makeup procedure must be followable step-by-step during an actual tank build. The dump criteria table gives the supervisor objective thresholds for a decision that is otherwise guesswork.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #345 -- Construction Workup v1.0*
*2026-04-26*
