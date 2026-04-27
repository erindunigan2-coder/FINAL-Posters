---
Project: Plating Posters Inc
Poster Number: 381
Title: "Solvent Cleaning Stage -- Dissolution, Contact Time & Diagnostics"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: Industry-standard solvent cleaning mechanisms -- dissolution vs. emulsification, contact time by method, part loading considerations, and common failure diagnostics. Per ASM Handbook Vol. 5 and general industry knowledge.
Process Scope: The main solvent cleaning step -- mechanism of action, contact time, part loading, and failure diagnosis
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - TreatmentStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #381 -- Construction Workup
## Solvent Cleaning Stage -- Dissolution, Contact Time & Diagnostics

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the "main event" poster for the solvent cleaning cluster -- where soil actually gets dissolved. The hero concept is the dissolution mechanism itself: "like dissolves like." Unlike alkaline cleaning which uses chemical reactions (saponification) and physical encapsulation (emulsification), solvent cleaning is pure physical dissolution -- the solvent molecules surround the oil molecules and carry them into solution. No reaction, no byproducts, just solvency. This poster covers mechanism, contact time by method, part loading, and a 4-failure diagnosis grid.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Dissolution mechanism callout (Block B -- HERO):** A large callout explaining the "like dissolves like" principle with a visual comparison to alkaline cleaning mechanisms.

2. **Four-method contact time panel (Block C):** Contact time parameters broken out by cold immersion, vapor degreasing, spray/wipe, and ultrasonic+solvent.

3. **Part loading guidance (Block D):** Fixturing, drainage, blind hole considerations.

4. **Failure diagnosis grid (Block E):** 2x2 grid of common solvent cleaning failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DISSOLUTION MECHANISM + CONTACT TIME (2.9"--15.0" / ~12.1" tall)
  Block B: Dissolution mechanism hero
  Block C: Four-method contact time panels

ZONE 3 -- PART LOADING GUIDANCE (15.0"--21.5" / ~6.5" tall)
  Block D: Loading considerations by method

ZONE 4 -- FAILURE DIAGNOSIS (21.5"--28.5" / ~7.0" tall)
  Block E: 2x2 failure grid

ZONE 5 -- KEY PRINCIPLES (28.5"--32.5" / ~4.0" tall)
  Block F: Quick-reference operating principles

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SOLVENT CLEANING STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dissolution Mechanism, Contact Time & Process Diagnostics` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `No chemical reaction. No emulsion. Just pure dissolution -- the solvent surrounds the soil molecule and carries it away. Elegant simplicity.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Dissolution Mechanism + Contact Time (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> HOW SOLVENT CLEANING WORKS -- DISSOLUTION

---

**BLOCK B -- Dissolution Mechanism Hero**

Y: 3.8" to 8.5". Full width callout.

Rounded rect, X: 0.5", W: 23.0", H: 4.5", fill `#1E2435`, radius 8.
Left accent: 0.06" `#2EC4B6`.

**Two-column interior:**

*Left -- The Mechanism (W: 11.0"):*
- Title: `DISSOLUTION: "LIKE DISSOLVES LIKE"` Barlow SemiBold 18 pt `#2EC4B6`
- Body: Inter Regular 14 pt `#F0EDE8`:
```
Organic solvents dissolve organic contaminants
through molecular similarity. The solvent
surrounds and solvates the oil/grease molecules,
carrying them into solution.

No chemical reaction occurs.
No byproducts are formed.
This is purely a PHYSICAL process.
```
- Emphasis: `No chemical reaction occurs.` in Inter Medium 14 pt `#E8A020`

*Right -- Comparison to Alkaline Cleaning (W: 11.0"):*
- Title: `SOLVENT vs. ALKALINE -- DIFFERENT TOOLS` Barlow SemiBold 16 pt `#E8A020`

Three comparison rows:

| Mechanism | Alkaline | Solvent |
|---|---|---|
| Saponification | Reacts with fats to form soap | Does not apply |
| Emulsification | Surfactants encapsulate oil in micelles | Does not apply |
| Dissolution | Limited (water is a poor organic solvent) | Primary mechanism |

Data: Inter Regular 12 pt. Headers: Barlow SemiBold 13 pt.

---

**BLOCK C -- Four-Method Contact Time Panels**

Y: 9.0" to 14.8". Four callout boxes in a 2x2 grid.

Each box: Rounded rect, W: 11.17", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Position | Method | Contact Time | Endpoint | Accent |
|---|---|---|---|---|
| R1C1 | Cold Immersion | 3-15 min (soil dependent) | Visual: no soil visible; solvent clear around part | `#2EC4B6` |
| R1C2 | Vapor Degreasing | 1-5 min | Condensation stops = part at vapor temp = clean | `#E8A020` |
| R2C1 | Spray / Wipe | Until visually clean | Operator judgment; uneven coverage risk | `#C8D0D8` |
| R2C2 | Ultrasonic + Solvent | 2-10 min | Cavitation + dissolution; superior for complex geometry | `#27AE60` |

Per box:
- Method: Barlow SemiBold 16 pt, accent color
- Contact time: JetBrains Mono 14 pt `#F0EDE8`
- Endpoint: Inter Regular 13 pt `#F0EDE8` at 80%

**Vapor degreasing endpoint callout (below grid, Y: 14.2"):**
- Rounded rect, full width, H: 0.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `In vapor degreasing, when condensation stops, the part is clean. The part has reached vapor temperature -- no more condensation means no more fresh solvent contacting the surface.` Inter Medium 13 pt `#E8A020`

---

### ZONE 3 -- Part Loading Guidance

**Section label:** Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> PART LOADING -- DRAINAGE IS EVERYTHING

---

**BLOCK D -- Loading Guidance Panel**

Y: 15.9" to 21.3". Three callout boxes side by side.

Each box: Rounded rect, W: 7.33", H: 5.0", fill `#1E2435`, radius 6, top accent 3 pt.

| Box | X | Title | Accent | Content |
|---|---|---|---|---|
| 1 | 0.5" | FIXTURING | `#2EC4B6` | Parts must be fixtured for FREE DRAINAGE. Trapped solvent in cups, blind holes, or nested parts = fire/health hazard + dragout contamination. Rack or basket preferred -- barrel processing in solvent is unusual. |
| 2 | 8.16" | BLIND HOLES | `#E8A020` | Orient parts so blind holes drain downward on withdrawal. Air pockets in blind holes prevent solvent contact. In vapor degreasing, blind holes trap vapor that condenses on cooling -- creating a contaminated pool. |
| 3 | 15.83" | LOAD SIZE | `#27AE60` | Do not overload baskets or racks. In vapor degreasing, too many cold parts at once collapse the vapor zone (solvent condenses faster than it can be generated). Introduce parts slowly. |

Per box:
- Title: Barlow SemiBold 16 pt, accent color
- Content: Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Failure Diagnosis

**Section label:** Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> COMMON FAILURES -- DIAGNOSE AND CORRECT

---

**BLOCK E -- 2x2 Failure Grid**

Y: 22.4" to 28.3". Four cards in 2x2 grid. Gap: 0.33".

Each card: Rounded rect, W: 11.17", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Position | Failure | Cause | Fix |
|---|---|---|---|
| R1C1 | Residual soil after clean | Wrong solvent for soil type (polar vs. non-polar mismatch); solvent saturated with soil | Test different solvent; check solvent clarity; replace bath |
| R1C2 | White residue on parts | Moisture contamination in solvent; solvent decomposition products | Check water separator; test acid acceptance; replace if decomposed |
| R2C1 | Spotting / staining | Solvent evaporating unevenly, leaving dissolved soil as residue on surface | Use vapor degreasing (self-rinsing); improve drainage orientation |
| R2C2 | Non-metallic attack | Solvent dissolving seals, gaskets, paint, or plastic components on parts | Verify material compatibility of ALL part components before solvent selection |

Per card:
- Failure: Barlow SemiBold, 15 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 5 -- Key Principles

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> QUICK REFERENCE -- OPERATING PRINCIPLES

---

**BLOCK F -- Four Principle Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Principle | Accent |
|---|---|---|---|
| 1 | 0.5" | Match solvent polarity to soil polarity -- non-polar solvent for non-polar soil | `#2EC4B6` |
| 2 | 6.33" | Vapor degreasing endpoint: condensation stops = clean part | `#E8A020` |
| 3 | 12.16" | Never heat a cold immersion bath -- if you need heat, use a vapor degreaser | `#E8A020` |
| 4 | 18.0" | Solvent cleaning rarely stands alone for plating -- follow with alkaline clean for aqueous transition | `#27AE60` |

Per card:
- Principle: Inter Medium, 14 pt, accent color

---

### ZONE 6 -- Footer

Standard. Title: `Solvent Cleaning Stage -- Dissolution, Contact Time & Diagnostics`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Contact times and cleaning parameters shown are typical values. Specific solvents and process conditions vary by application and soil type. Consult your solvent supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Solvent Cleaning Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dissolution mechanism is what makes solvent cleaning conceptually distinct from every other cleaning method in the series. The "like dissolves like" principle must be front and center -- it is the single sentence that explains why solvents work on greases that alkaline cleaners struggle with. The vapor degreasing endpoint callout ("condensation stops = clean") is the most operationally useful fact on the poster and deserves amber emphasis. Part loading guidance is unusually important here because trapped solvent is both a safety hazard (vapor accumulation) and a quality hazard (contaminated pools).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #381 -- Construction Workup v1.0*
*2026-04-26*
