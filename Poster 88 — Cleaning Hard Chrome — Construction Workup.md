---
Project: Plating Posters Inc
Poster Number: 88
Title: "Cleaning -- Hard Chrome"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
Technical Source: Cleaning for hard chrome plating -- heavy-duty alkaline soak clean to remove machining oils, grinding coolant, lapping compound, and other industrial soils. Parts are typically machined steel, hardened steel, or cast iron. Optional vapor degrease for precision/aerospace parts (legacy, being phased out).
Process Scope: Cleaning -- Stage 1 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HardChrome
  - Cleaning
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #88 -- Construction Workup
## Cleaning -- Hard Chrome

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Hard chrome cleaning is serious industrial cleaning -- not the gentle surface prep of decorative work. These parts come from the machine shop covered in cutting oil, grinding coolant, lapping compound, rust preventative, and shop grime. The cleaner has to get it ALL off, because anything left on the surface will cause peeling, pitting, or poor adhesion under the high-stress hard chrome deposit.

Hero visual: a cleaning tank cross-section with parts on a rack, showing the types of soils being removed, with callouts for the cleaning parameters.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank hero (Block B):** Large soak clean tank cross-section with parts, heating coils, and soil removal indicators.
2. **Soil identification panel (Block D):** What you are cleaning off -- machining oils, coolant, lapping compound, rust preventative.
3. **Vapor degrease callout (Block E):** Legacy method, still used in some aerospace shops.
4. **Failure mode cards (Block F):** 4 cleaning-related failures.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SOIL IDENTIFICATION (14.5"--20.5" / ~6.0")
ZONE 5 -- VAPOR DEGREASE + ELECTROCLEAN OPTION (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hard Chrome -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Machine shop parts come in dirty. Cutting oil, grinding coolant, lapping compound. Get it ALL off -- or the chrome will peel.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

**Safety note (right side):**
- Rounded rect, X: 18.0", Y: 0.6", W: 5.5", H: 0.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `Cr(VI) CARCINOGEN -- see Main Tank poster` JetBrains Mono 10 pt `#E05C5C`

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Machined parts with oils, coolant, and shop soils  -->  After: Clean, oil-free surface ready for rinse and activation`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `ALKALINE SOAK CLEAN -- HEAVY DUTY` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.0"
- Fill: `#252B3D` (cleaner solution)
- Border: 3 pt `#C8D0D8`

**Heating elements (bottom of tank):**
- 2 horizontal rects, X: 3.0", Y: 12.0", W: 18.0", H: 0.3", fill `#E05C5C` at 50%
- Label: `HEATERS -- 150-190 F required` JetBrains Mono 11 pt `#E05C5C`

**Parts on rack (center):**
- Large irregular shapes representing industrial parts (cylinders, shafts, rings)
- Fill: `#3A4055`, border 2 pt `#C8D0D8`
- Label: `MACHINED STEEL PARTS` Barlow SemiBold 14 pt `#F0EDE8`

**Soil removal indicators:**
- Wavy lines rising from parts representing oil lifting off
- Stroke: 1 pt `#E8A020`, wavy/dashed
- Label: `Oils and soils dissolving` Inter Regular 11 pt `#E8A020`

**Key parameters (right side of tank):**
- `Concentration: 6--10 oz/gal (45--75 g/L)` JetBrains Mono 14 pt `#F0EDE8`
- `Temperature: 150--190 F (66--88 C)` JetBrains Mono 14 pt `#E05C5C`
- `Time: 5--15 min` JetBrains Mono 14 pt `#E8A020`
- `Type: Heavy-duty alkaline cleaner` JetBrains Mono 13 pt `#F0EDE8`

**Left side notes:**
- `Agitation: air or mechanical` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Water-break test after rinse` Inter Medium 13 pt `#2EC4B6`
- `Free alkalinity: monitor and replenish` Inter Regular 12 pt `#F0EDE8` at 60%

**Bottom callout:**
- `Hard chrome cleaning runs hotter and longer than most plating prep. These parts carry heavy industrial soils -- not fingerprints.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 4 -- Soil Identification

**Section label:** `WHAT YOU ARE CLEANING OFF` -- Y: 14.7".

**BLOCK D -- Soil Cards (Y: 15.3" to 20.3")**

Six cards in a 3x2 grid:

| Pos | Soil Type | Color | Source | Removal Difficulty |
|---|---|---|---|---|
| R1C1 | CUTTING OIL | `#E8A020` | Machining, turning, milling | Moderate -- alkaline soak |
| R1C2 | GRINDING COOLANT | `#E8A020` | Surface grinding, cylindrical grinding | Moderate -- may be water-soluble |
| R1C3 | LAPPING COMPOUND | `#E05C5C` | Precision finishing, honing | HIGH -- abrasive paste embedded in surface |
| R2C1 | RUST PREVENTATIVE | `#E8A020` | Storage, shipping between operations | Moderate -- petroleum-based film |
| R2C2 | SHOP GRIME | `#2EC4B6` | Handling, floor debris, mixed contamination | Low -- general alkaline cleaning |
| R2C3 | DRAWING COMPOUND | `#E05C5C` | Stamping, deep drawing | HIGH -- heavy film, may need pre-wipe |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

Bottom note: `Lapping compound and drawing compound are the hardest soils to remove. If water-break test fails after cleaning, these are the usual suspects. Extend soak time or add a pre-wipe step.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 5 -- Vapor Degrease + Electroclean Option

**Section label:** `ALTERNATIVE CLEANING METHODS` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Vapor Degrease (Legacy):**
- Rounded rect, X: 0.5", W: 11.0", H: 4.8", fill `#1E2435`, left accent `#3A4055`
- Title: `VAPOR DEGREASE (LEGACY)` -- Barlow SemiBold, 18 pt, `#C8D0D8`

| Parameter | Value |
|---|---|
| Solvent | Trichloroethylene or perchloroethylene |
| Method | Vapor condensation on cold parts |
| Time | Until parts reach solvent vapor temp |
| Status | Being phased out -- EPA NESHAP regulated |
| Still used | Some aerospace shops under permit |

Note: `Effective but environmentally problematic. Aqueous alkaline cleaning has largely replaced vapor degrease in modern hard chrome shops.` -- Inter Regular, 13 pt, `#F0EDE8` at 70%

**Right -- Electrocleaning (Optional Second Step):**
- Rounded rect, X: 12.0", W: 11.5", H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `ELECTROCLEAN (OPTIONAL)` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Value |
|---|---|
| Type | Anodic electrocleaning |
| Concentration | 4--8 oz/gal |
| CD | 30--50 ASF |
| Temperature | 140--180 F |
| Time | 1--3 min |
| Purpose | Scrubbing action from gas evolution at surface |

Note: `Used as a second cleaning step for critical parts. The gas evolution (anodic = oxygen) mechanically dislodges soils that soak cleaning alone cannot reach.` -- Inter Regular, 13 pt, `#F0EDE8` at 70%

Caution: `ANODIC only for steel going to hard chrome. Cathodic cleaning risks hydrogen absorption.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 4 CLEANING FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | CHROME PEELING | `#E05C5C` | Oil or soil residue under chrome deposit | Extend soak time; increase temperature; verify water-break |
| R1C2 | PITTING IN CHROME | `#E05C5C` | Embedded contaminant (lapping compound) outgassing | Pre-wipe parts; extend cleaning; ultrasonic if available |
| R2C1 | ROUGH DEPOSIT | `#E8A020` | Particulate from inadequate cleaning | Increase agitation; filter cleaner tank |
| R2C2 | WATER-BREAK FAILURE | `#E8A020` | Cleaner exhausted or temp too low | Replenish cleaner; check heater function |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Hard Chrome`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; hard chrome process engineering practice. Hard chrome plating uses hexavalent chromium -- a known human carcinogen. Comply with all applicable regulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Hard Chrome Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The contrast between this cleaning poster and Poster #80 (decorative chrome cleaning) is stark. Decorative chrome "cleaning" is about speed and timing on a nickel surface. Hard chrome cleaning is industrial grunt work -- heavy soils, hot solutions, long soak times. The soil identification panel in Zone 4 is unique to this cluster -- no other cleaning poster in the series needs to explain lapping compound or drawing compound. The vapor degrease callout in Zone 5 gives context for shops still running legacy equipment, while making it clear that aqueous cleaning is the modern standard.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #88 -- Construction Workup v1.0*
*2026-04-26*
