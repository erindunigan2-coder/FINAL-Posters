---
Project: Plating Posters Inc
Poster Number: 352
Title: "Bath Preparation & Control -- Electrocleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-2.3)"
Technical Source: Industry-standard bath makeup and analytical control for electrolytic cleaners. NaOH-based formulations with surfactant, phosphate, and chelator components. Chloride contamination monitoring per Drew's field notes.
Process Scope: Bath preparation, composition, analytical control, and dump criteria for electrocleaners
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electrocleaning
  - BathPreparation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT02
---

# Poster #352 -- Construction Workup
## Bath Preparation & Control -- Electrocleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 3 of 7 in the CT-02 cluster. The electrocleaner bath is simpler than the soak cleaner -- fewer components because the electrical action does the heavy lifting. The hero visual is a five-component breakdown (NaOH, carbonate, phosphate, surfactant, chelator). The analytical control section introduces chloride monitoring, which is the unique control parameter for electrocleaners -- Drew's field experience confirms that 10 g/L chloride causes substrate corrosion and salt spray failure. The rectifier setup callout covers the electrical side of "bath preparation" that soak cleaners do not have.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Bath composition breakdown (Block B -- HERO):** Five-component visual with functions and concentration ranges.
2. **Makeup procedure (Block D):** Numbered step-by-step (6 steps, including rectifier setup).
3. **Analytical control panel (Block E):** Titration methods, chloride monitoring, and frequency.
4. **Bath life / dump criteria table (Block F):** Five-parameter action-level table.

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
**Subheading:** `Electrocleaning -- Simpler Chemistry, Smarter Control` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Fewer ingredients than a soak cleaner because the electricity does the heavy lifting. But the analytical control is tighter -- especially chlorides.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Empty tank + rectifier offline --> After: Fully charged electrocleaner at operating concentration, temperature, and rectifier set`

---

### ZONE 3 -- Bath Composition Breakdown (HERO)

**Section label:** `WHAT IS IN YOUR ELECTROCLEANER -- 5 COMPONENTS` -- Y: 4.4".

**BLOCK B -- Five-Component Visual**

Y: 5.0" to 14.5". Five callout boxes in a layout: 3 top row, 2 bottom row centered.

| Component | Position | Accent | Concentration | Function |
|---|---|---|---|---|
| Sodium Hydroxide (NaOH) | R1C1 (X: 0.5") | `#2EC4B6` | 22-60 g/L (3-8 oz/gal) | Primary alkalinity; solution conductivity; saponification agent |
| Sodium Carbonate (Na2CO3) | R1C2 (X: 8.0") | `#E8A020` | 15-45 g/L (2-6 oz/gal) | Alkalinity buffer; maintains consistent pH during use |
| Trisodium Phosphate (TSP) | R1C3 (X: 15.5") | `#27AE60` | 7.5-30 g/L (1-4 oz/gal) | Emulsifier; soil dispersant; softens water hardness |
| Surfactant (Low-Foam) | R2C1 (X: 3.0") | `#2EC4B6` | 0.05-0.3% by volume | Residual oil emulsification; foam control critical (gas evolution creates turbulence) |
| Chelating Agent (Gluconate or EDTA) | R2C2 (X: 12.0") | `#E8A020` | 0-7.5 g/L (0-1 oz/gal) | Complexes dissolved metals (Fe, Zn, Cu) to prevent cathodic smut deposition |

Each box: Rounded rect W: 7.0", H: 4.2", fill `#1E2435`, left accent 0.06".

Interior per box:
- Component name: Barlow SemiBold 16 pt, accent color
- Formula: JetBrains Mono 14 pt, `#F0EDE8` at 70%
- Concentration: JetBrains Mono 16 pt, accent color
- Function: Inter Regular 13 pt `#F0EDE8`, line height 150%

**"Simpler than soak clean" callout (Y: 14.0"):**
- Rounded rect, W: 23.0", H: 0.8", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Electrocleaner formulations are deliberately simpler than soak cleaners. The gas evolution and electrical action do the mechanical work -- the chemistry provides the environment.` -- Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Makeup Procedure

**Section label:** `TANK MAKEUP -- STEP BY STEP` -- Y: 15.2".

**BLOCK D -- Numbered Procedure (Y: 15.8" to 20.8")**

Six numbered steps in a vertical sequence. Each step: rounded rect, full width (23.0"), H: 0.75", fill alternating `#1E2435` / `#252B3D`.

| Step | Instruction | Caution |
|---|---|---|
| 1 | Fill tank to 2/3 volume with warm water (40-50 C / 105-120 F) | Use warm water to aid dissolution |
| 2 | Add NaOH slowly with agitation | EXOTHERMIC -- same caution as soak cleaner makeup |
| 3 | Add carbonate and phosphate builders; dissolve completely | Stir thoroughly between additions |
| 4 | Add surfactant LAST -- low-foam grade required | Gas evolution during operation creates aggressive agitation; high-foam surfactant = overflow |
| 5 | Bring to operating volume and temperature (150-160 F target) | Connect heater; verify thermostat |
| 6 | Set up rectifier: verify polarity, set voltage (6-12 V), confirm bus bar connections | TEST with dummy load before first production use; check all contact points |

Step number: Barlow Condensed ExtraBold 20 pt, `#2EC4B6`, in a 0.6" circle fill `#2EC4B6` at 20%.
Instruction: Inter Medium 14 pt `#F0EDE8`.
Caution: Inter Regular 12 pt `#E8A020` (or `#E05C5C` for step 6).

---

### ZONE 5 -- Analytical Control

**Section label:** `KEEPING IT RIGHT -- ANALYTICAL CONTROL` -- Y: 21.2".

**BLOCK E -- Control Panel (Y: 21.8" to 26.8")**

Two-column layout.

**Left -- Titration Methods (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `TITRATION` Barlow SemiBold 18 pt `#2EC4B6`

| Test | Method | Target |
|---|---|---|
| Free Alkalinity | Titrate 10 mL sample with N/10 HCl to phenolphthalein | 5-10 points |
| Total Alkalinity | Titrate to methyl orange endpoint | 8-15 points |

- JetBrains Mono 13 pt for method details
- Frequency: `Daily on production lines; 2-3x per week on intermittent use` Inter Medium 13 pt `#E8A020`

**Right -- Chloride Monitoring (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, left accent 0.06" `#E05C5C`.

Title: `CHLORIDE CONTAMINATION -- CRITICAL` Barlow SemiBold 18 pt `#E05C5C`

Body: Inter Regular 13 pt `#F0EDE8`:
```
Chlorides cause substrate corrosion during electrocleaning
that leads to salt spray failure after plating.

Method: Mohr titration (AgNO3 / K2CrO4)
Action level: > 10 g/L = PROBLEM

Source: HCl drag-in from acid pickle,
contaminated water, chlorinated solvents

Fix: Partial dump and rebuild;
investigate drag-in source
```

Highlight: JetBrains Mono 14 pt `#E05C5C`: `> 10 g/L Cl- = DUMP TRIGGER`

---

### ZONE 6 -- Bath Life & Dump Criteria

**Section label:** `WHEN TO DUMP -- BATH LIFE INDICATORS` -- Y: 27.2".

**BLOCK F -- Dump Criteria Table (Y: 27.8" to 32.3")**

Column widths: Parameter (4.5") | Action Level (4.5") | Symptom (7.0") | Response (7.0")

Header row: fill `#E05C5C` at 25%, H: 0.5".

| Parameter | Action Level | Symptom | Response |
|---|---|---|---|
| Chloride Content | > 10 g/L | Etching, pitting, salt spray failure after plating | Partial dump + rebuild; identify drag-in source |
| Dissolved Metals | > 5 g/L total Fe + Zn + Cu | Cathodic smut on parts; discoloration | Partial dump; increase chelator; switch to anodic mode |
| Alkalinity Drop | Cannot maintain free alk > 5 pts | Rapid consumption; poor conductivity | Rebuild bath; check for acid drag-in |
| Surfactant Depletion | Parts still oily after normal cycle | Oil film on parts; water break failure | Add surfactant; if persistent, dump |
| Age / Throughput | 6-12 months (production line) | General degradation | Scheduled rebuild; electrocleaner baths last longer than soak cleaners |

Data: Inter Regular 13 pt. Action levels: JetBrains Mono 14 pt `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Bath Preparation & Control -- Electrocleaning`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook. Chloride action level per field experience -- 10 g/L confirmed as corrosion threshold. Specific product concentrations vary by supplier. Consult your process supplier TDS for exact makeup instructions.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Bath Preparation Control Electrocleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chloride monitoring callout is the signature feature of this poster. Most operators have no idea that chloride drag-in from acid pickle can silently destroy the electrocleaner's ability to produce parts that pass salt spray. Drew's field data confirms 10 g/L as the action threshold -- this is real-world knowledge that elevates the poster beyond textbook content. The five-component hero is deliberately simpler than the soak cleaner's six-component version (345) to reinforce the message that electrocleaner chemistry is leaner. The rectifier setup step in the makeup procedure is new for this series and bridges the gap between chemistry and electrical setup.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #352 -- Construction Workup v1.0*
*2026-04-26*
