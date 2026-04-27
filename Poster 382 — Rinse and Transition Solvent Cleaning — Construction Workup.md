---
Project: Plating Posters Inc
Poster Number: 382
Title: "Rinse & Transition -- Solvent to Aqueous Process"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: Industry-standard practices for transitioning from solvent cleaning to aqueous processes. Covers why water rinse is NOT used after solvent cleaning, solvent evaporation/drainage, the alkaline soak clean as the aqueous bridge, and multi-stage solvent rinse systems for non-plating applications.
Process Scope: Rinse and transition after solvent cleaning -- evaporation, drainage, dragout capture, and transition to alkaline cleaning
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - Rinse
  - Transition
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #382 -- Construction Workup
## Rinse & Transition -- Solvent to Aqueous Process

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the most unusual "rinse" in the entire series -- because there is no water rinse. Solvents and water do not mix. The "rinse" after solvent cleaning is evaporation and drainage, followed by transition to an aqueous process (typically alkaline soak clean). In vapor degreasing, the process is self-rinsing -- the final condensing solvent IS the rinse. This poster also covers dragout management for solvents (which evaporate rather than drip like aqueous solutions) and the multi-stage approach for non-plating final-clean applications.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **"No water rinse" hero callout (Block B -- HERO):** A large, visually prominent callout that immediately communicates the key difference from every other cluster's rinse poster.

2. **Transition pathway diagram (Block C):** The solvent-to-aqueous transition showing evaporation -> alkaline soak clean -> standard aqueous rinse.

3. **Vapor degreasing self-rinse explanation (Block D):** How the cascading condensate system serves as the rinse.

4. **Dragout and environmental callout (Block E):** Solvent vapor capture, evaporative loss, and enclosure requirements.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- "NO WATER RINSE" HERO + TRANSITION PATH (2.9"--14.0" / ~11.1" tall)
  Block B: No-water-rinse callout
  Block C: Transition pathway diagram

ZONE 3 -- VAPOR DEGREASING SELF-RINSE (14.0"--21.5" / ~7.5" tall)
  Block D: Cascading condensate system
  Block D2: Multi-stage solvent systems

ZONE 4 -- DRAGOUT AND ENVIRONMENTAL (21.5"--28.5" / ~7.0" tall)
  Block E: Solvent dragout management
  Block F: Environmental capture requirements

ZONE 5 -- KEY PRINCIPLES (28.5"--32.5" / ~4.0" tall)
  Block G: Quick-reference transition rules

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE & TRANSITION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `From Solvent Clean to Aqueous Process -- No Water Rinse Required` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The only cleaning process where the "rinse" is evaporation. Solvents and water do not mix -- the transition to aqueous happens at the alkaline soak tank.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- "No Water Rinse" Hero + Transition Pathway

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> THE SOLVENT-TO-AQUEOUS TRANSITION

---

**BLOCK B -- No-Water-Rinse Hero Callout**

Y: 3.8" to 6.8". Full width.

Rounded rect, X: 0.5", W: 23.0", H: 2.8", fill `#E8A020` at 10%, radius 8.
Border: 2 pt `#E8A020`.
Left accent: 0.08" `#E8A020`.

- Title: `WATER RINSE IS NOT USED AFTER SOLVENT CLEANING` Barlow Condensed ExtraBold 28 pt `#E8A020`
- Body: Inter Regular 16 pt `#F0EDE8`:

```
Solvents and water do not mix. Running parts under water after solvent
cleaning does not remove solvent residue -- it traps it under a water
film. The correct post-solvent sequence is:

  1. Drain and allow solvent to evaporate (in ventilated area)
  2. Transfer directly to alkaline soak cleaner

The alkaline cleaner's surfactants emulsify any residual solvent film,
completing the transition from organic solvent to aqueous process.
```

---

**BLOCK C -- Transition Pathway Diagram**

Y: 7.3" to 13.8". Full width.

**Five-box linear flow (left to right):**

Each box: Rounded rect, W: 4.2", H: 3.0", fill `#1E2435`, top accent 4 pt, radius 6.

| Stage | X | Accent | Name | Detail |
|---|---|---|---|---|
| 1. Solvent Clean | 0.5" | `#2EC4B6` | Solvent Cleaning Complete | Parts cleaned by immersion, vapor, or spray |
| 2. Drain | 5.2" | `#E8A020` | Drain & Evaporate | Allow solvent to flash off; ventilated area; 1-5 min |
| 3. Transfer | 9.9" | `#3A4055` | Transfer to Aqueous Line | Move parts to alkaline soak cleaner |
| 4. Alkaline Soak | 14.6" | `#2EC4B6` | Alkaline Soak Clean | Surfactants emulsify residual solvent film; standard clean cycle |
| 5. Standard Rinse | 19.3" | `#27AE60` | Aqueous Rinse | Normal rinse protocol resumes from this point forward |

Arrows: 3 pt `#3A4055`, arrowhead right.

Inside each box:
- Stage badge: Barlow Condensed ExtraBold 13 pt on accent-colored rounded rect
- Name: Barlow SemiBold 15 pt `#F0EDE8`
- Detail: Inter Regular 12 pt `#F0EDE8` at 70%

**Belt-and-suspenders callout (Y: 13.2"):**
- Rounded rect, full width, H: 0.5", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Solvent cleaning + alkaline cleaning is the "belt and suspenders" approach -- solvents dissolve the heavy organic soil; alkaline cleaners handle residual films and water-soluble contamination.` Inter Medium 13 pt `#27AE60`

---

### ZONE 3 -- Vapor Degreasing Self-Rinse

**Section label:** Centered. Y: 14.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> VAPOR DEGREASING IS SELF-RINSING

---

**BLOCK D -- Self-Rinse Explanation**

Y: 14.9" to 18.5". Left panel, W: 11.0".

Rounded rect, X: 0.5", W: 11.0", H: 3.4", fill `#1E2435`, radius 6, left accent `#E8A020`.

- Title: `THE CASCADING CONDENSATE` Barlow SemiBold 18 pt `#E8A020`
- Body: Inter Regular 14 pt `#F0EDE8`:

```
In vapor degreasing, the final solvent that touches
the part is freshly distilled condensate -- pure
solvent with zero dissolved soil.

This is why vapor degreasing is self-rinsing:
  - Soil dissolves into condensate
  - Condensate drips back to boiling sump
  - Soil accumulates in sump, NOT on parts
  - Each condensation cycle is a fresh rinse

No separate rinse step is needed.
```

**BLOCK D2 -- Multi-Stage Solvent Systems**

Y: 14.9" to 18.5". Right panel, W: 11.5".

Rounded rect, X: 12.0", W: 11.5", H: 3.4", fill `#1E2435`, radius 6, left accent `#2EC4B6`.

- Title: `MULTI-STAGE SYSTEMS (NON-PLATING)` Barlow SemiBold 18 pt `#2EC4B6`
- Body: Inter Regular 14 pt `#F0EDE8`:

```
When solvent cleaning IS the final clean (electronics,
optics, aerospace assembly):

  1. Dirty sump (bulk soil removal)
  2. Clean sump (reduced soil load)
  3. Vapor zone (pure distilled rinse)

Solvent purity is critical -- use high-grade solvent
and cascading stages (analogous to counterflow
aqueous rinsing).
```

**Callout strip (Y: 19.0"):**
- Rounded rect, full width, H: 0.5", fill `#2EC4B6` at 12%, border 1 pt `#2EC4B6`
- Text: `For plating applications, solvent cleaning is almost never the final clean -- always follow with alkaline soak to transition to aqueous processing.` Inter Medium 13 pt `#2EC4B6`

---

**Dragout comparison panel (Y: 19.8" to 21.3"):**

Rounded rect, X: 0.5", W: 23.0", H: 1.3", fill `#252B3D`, radius 6.

Two-column:
- Left: `AQUEOUS DRAGOUT: drips from parts; measured in mL/m2; captured in rinse tank` Inter Regular 13 pt `#2EC4B6`
- Right: `SOLVENT DRAGOUT: evaporates from parts; escapes as vapor; must be CAPTURED (fume hood, enclosure)` Inter Regular 13 pt `#E8A020`

---

### ZONE 4 -- Dragout and Environmental

**Section label:** Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> DRAGOUT MANAGEMENT -- SOLVENT VAPOR IS THE ENEMY

---

**BLOCK E -- Dragout Methods**

Y: 22.4" to 25.5". Three callout cards.

Each card: Rounded rect, W: 7.33", H: 2.8", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Method | Detail | Accent |
|---|---|---|---|---|
| 1 | 0.5" | Slow Withdrawal | Drain parts above tank for 10-15 sec; use drain rails. Reduces liquid solvent carry-out. | `#2EC4B6` |
| 2 | 8.16" | Enclosure | Vapor degreaser must be enclosed or hooded. NESHAP Subpart T requires freeboard controls and idling emission limits. | `#E8A020` |
| 3 | 15.83" | Multi-Stage | Dirty sump -> clean sump -> vapor zone minimizes contaminated dragout. Recovers dissolved soil before it reaches the vapor zone. | `#27AE60` |

**BLOCK F -- Environmental Capture**

Y: 26.0" to 28.3". Full-width callout.

Rounded rect, X: 0.5", W: 23.0", H: 2.1", fill `#E05C5C` at 8%, radius 6, border 1 pt `#E05C5C`.

- Title: `ENVIRONMENTAL CAPTURE IS NOT OPTIONAL` Barlow SemiBold 18 pt `#E05C5C`
- Body: Inter Regular 13 pt `#F0EDE8`:

```
Halogenated solvent vapor: NESHAP 40 CFR Part 63 Subpart T requires enclosed equipment,
freeboard chillers, and emission monitoring. Violations carry serious penalties.

Non-halogenated solvent vapor: VOC emissions regulated under Clean Air Act. May require
carbon adsorption or thermal oxidation. NFPA 30 flammable liquids code applies.

Evaporating solvent is not "gone" -- it is in the air your workers breathe and the
atmosphere. Capture it.
```

---

### ZONE 5 -- Key Principles

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> TRANSITION RULES -- QUICK REFERENCE

---

**BLOCK G -- Four Principle Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Principle | Accent |
|---|---|---|---|
| 1 | 0.5" | NO water rinse after solvent clean -- solvents and water do not mix | `#E8A020` |
| 2 | 6.33" | Drain and evaporate FIRST, then transfer to alkaline soak clean | `#2EC4B6` |
| 3 | 12.16" | Vapor degreasing is self-rinsing -- no separate rinse step needed | `#27AE60` |
| 4 | 18.0" | Solvent vapor is dragout you cannot see -- capture it or lose it to the air | `#E05C5C` |

---

### ZONE 6 -- Footer

Standard. Title: `Rinse & Transition -- Solvent to Aqueous Process`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Solvent handling and transition procedures shown are typical practices. Equipment configurations and regulatory requirements vary by jurisdiction and application. Consult your solvent supplier, equipment manufacturer, and applicable EPA/OSHA/NESHAP regulations.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Transition Solvent Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most conceptually distinctive rinse poster in the entire Chemical Treatment series because the answer is "there is no water rinse." That message must be visually dominant -- the amber-bordered hero callout in Zone 2 makes it impossible to miss. The transition pathway diagram grounds the concept in a practical sequence the operator can follow. The environmental capture callout in Zone 4 carries regulatory weight -- NESHAP Subpart T violations are not theoretical; they happen when shops treat solvent vapor as "it just evaporates."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #382 -- Construction Workup v1.0*
*2026-04-26*
