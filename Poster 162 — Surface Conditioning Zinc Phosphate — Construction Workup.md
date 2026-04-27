---
Project: Plating Posters Inc
Poster Number: 162
Title: "Surface Conditioning -- Zinc Phosphate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-02 technical reference (zinc phosphate conversion coating)"
Process Scope: Surface conditioning with titanium colloid activator for zinc phosphate pretreatment (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPhosphate
  - SurfaceConditioning
  - ConstructionWorkup
  - ClusterCC02
---

# Poster #162 -- Construction Workup
## Surface Conditioning -- Zinc Phosphate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. THIS IS THE MOST CRITICAL STEP IN ZINC PHOSPHATE PROCESSING. The titanium colloid activator creates millions of nucleation sites per cm2 on the steel surface, determining whether the zinc phosphate crystals will be fine and dense (2--10 um, excellent coating) or coarse and porous (50--100+ um, failure). This poster must make two things unmistakable: (1) conditioning controls everything downstream, and (2) DO NOT RINSE between this stage and the phosphate bath.

The contrast with iron phosphate (Poster #154, where no conditioner is needed) should be referenced but not dominate -- this poster is about HOW conditioning works, not whether it is needed.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Nucleation site hero (Block B -- HERO):** Large visual showing Ti colloid particles adsorbing onto the steel surface and creating nucleation sites, with a conditioned vs. unconditioned crystal comparison.
2. **Chemistry and parameters panel (Block D):** Ti colloid bath chemistry, operating parameters, and control variables.
3. **"NO RINSE" callout (Block E):** The critical transition from conditioner to phosphate bath.
4. **Conditioner failure diagnosis (Block F):** Common problems and fixes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- NUCLEATION SITE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CHEMISTRY & PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- NO RINSE RULE + CONDITIONER HEALTH (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE DIAGNOSIS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE CONDITIONING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Zinc Phosphate -- The Most Critical Step -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `A few grams per liter of titanium colloid, 30 seconds of contact, and the entire zinc phosphate coating is decided. Fine crystals or coarse crystals. There is no middle ground.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, rinsed steel surface  -->  After: Millions of Ti nucleation sites per cm2 -- ready for phosphate`

---

### ZONE 3 -- Nucleation Site Hero

**Section label:** `HOW CONDITIONING CONTROLS CRYSTAL SIZE` -- Y: 4.4".

**BLOCK B -- Conditioned vs. Unconditioned Comparison (Y: 5.0" to 14.0")**

Two large panels:

**Left -- WITH Conditioning (X: 0.5", W: 11.0"):**
- Large rounded rect, H: 8.5", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `WITH Ti CONDITIONING` Barlow Condensed ExtraBold 24 pt `#27AE60`
- Badge: `CORRECT` Barlow Condensed ExtraBold 14 pt, fill `#27AE60`, text `#1A1F2E`

Visual element -- steel surface cross-section:
- Rectangle representing steel surface
- Dense layer of small dots across surface: `Ti colloid particles (1--5 g/L)` Inter Regular 12 pt `#E8A020`
- Many small crystal shapes growing from each dot
- Label: `Fine, dense crystals: 2--10 um` Inter Medium 16 pt `#27AE60`

Key metrics (JetBrains Mono 14 pt):
- `Millions of nucleation sites / cm2` `#27AE60`
- `Crystal size: 2--10 um` `#F0EDE8`
- `Coating: dense, compact, adherent` `#F0EDE8`
- `Paint adhesion: EXCELLENT` `#27AE60`
- `SST (painted): 500--1500+ hours` `#F0EDE8`

Big stat callout:
- `2--10` Barlow Condensed ExtraBold 64 pt `#27AE60`
- `um crystal size` Inter Medium 16 pt `#27AE60`

**Right -- WITHOUT Conditioning (X: 12.0", W: 11.5"):**
- Large rounded rect, H: 8.5", fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `WITHOUT CONDITIONING` Barlow Condensed ExtraBold 24 pt `#E05C5C`
- Badge: `FAILURE` Barlow Condensed ExtraBold 14 pt, fill `#E05C5C`, text `#1A1F2E`

Visual element:
- Rectangle representing steel surface
- Only a few scattered nucleation points (grain boundaries, defects)
- Large, coarse crystal shapes growing from sparse points
- Label: `Coarse, porous crystals: 50--100+ um` Inter Medium 16 pt `#E05C5C`

Key metrics:
- `Nucleation only at grain boundaries` `#E05C5C`
- `Crystal size: 50--100+ um` `#F0EDE8`
- `Coating: porous, poorly adherent` `#F0EDE8`
- `Paint adhesion: POOR` `#E05C5C`
- `SST (painted): dramatically reduced` `#F0EDE8`

Big stat callout:
- `50--100+` Barlow Condensed ExtraBold 64 pt `#E05C5C`
- `um crystal size` Inter Medium 16 pt `#E05C5C`

---

### ZONE 4 -- Chemistry & Parameters

**Section label:** `Ti COLLOID BATH -- CHEMISTRY AND CONTROL` -- Y: 14.7".

**BLOCK D -- Two-Column Layout (Y: 15.3" to 20.3")**

**Left -- Bath Chemistry (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `BATH CHEMISTRY` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Value |
|---|---|
| Active chemistry | Colloidal titanium phosphate -- Ti(HPO4)2 |
| Concentration | 0.1--0.5% by weight (1--5 g/L) |
| pH | 7.5--9.5 (mildly alkaline) |
| Temperature | Ambient to 100 F (16--38 C) |
| Time | 30 sec to 2 min |
| Method | Immersion or spray |

Data: JetBrains Mono 12 pt `#F0EDE8`. Labels: Inter Medium 13 pt.

Bottom note: `The colloid is a DISPERSION, not a dissolved solution. It is particles in suspension. Particle viability is everything.` Inter Regular 12 pt `#F0EDE8` at 60%.

**Right -- Critical Control Rules (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `NON-NEGOTIABLE RULES` Barlow SemiBold 20 pt `#E05C5C`

Five rules, each with icon-style number:

1. `NEVER HEAT this bath` -- `Heat destabilizes the colloid` Inter Regular 13 pt `#F0EDE8`
2. `pH 7.5--9.5 ONLY` -- `Below 7: colloid dissolves. Above 10: colloid flocculates` Inter Regular 13 pt `#F0EDE8`
3. `NO ACID carryover from upstream` -- `Acid destroys colloid instantly` Inter Regular 13 pt `#F0EDE8`
4. `NO ALKALINE carryover` -- `Raises pH, kills colloid viability` Inter Regular 13 pt `#F0EDE8`
5. `Dump and remake when contaminated` -- `Conductivity > 1500--2000 uS/cm = contaminated` Inter Regular 13 pt `#F0EDE8`

Rule numbers: Barlow Condensed ExtraBold 16 pt `#E05C5C`. Rule text: Barlow SemiBold 13 pt `#F0EDE8`.

---

### ZONE 5 -- No Rinse Rule + Conditioner Health

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- NO RINSE BETWEEN CONDITIONER AND PHOSPHATE (X: 0.5", W: 11.0"):**

Section label: `DO NOT RINSE AFTER CONDITIONING` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Rounded rect, H: 5.0", fill `#E05C5C` at 8%, border 2 pt `#E05C5C`, left accent `#E05C5C` 0.06".

Content:
- `THE TITANIUM COLLOID MUST REMAIN ON THE SURFACE` Barlow SemiBold 18 pt `#E05C5C`
- `When the part enters the zinc phosphate bath, the Ti particles must still be adsorbed on the steel surface. They are the nucleation sites.` Inter Regular 14 pt `#F0EDE8`
- `A rinse between conditioning and phosphating washes away the nucleation sites.` Inter Medium 14 pt `#E05C5C`
- `Result: coarse crystals, porous coating, failed adhesion.` Inter Regular 13 pt `#F0EDE8`
- `This is the most common setup error in zinc phosphate lines.` Inter Medium 14 pt `#E8A020`
- `Parts go DIRECTLY from conditioner to phosphate bath. No exceptions.` Barlow SemiBold 14 pt `#E05C5C`

**Right -- Conditioner Health Assessment (X: 12.0", W: 11.5"):**

Section label: `IS YOUR CONDITIONER ALIVE?` Barlow Condensed ExtraBold 22 pt `#27AE60`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#27AE60` 0.06".

| Check | Healthy | Dead/Dying |
|---|---|---|
| pH | 7.5--9.5 | Below 7 or above 10 |
| Conductivity | < 1500 uS/cm | > 2000 uS/cm |
| Appearance | Slightly milky/opalescent | Clear (settled) or chunky |
| Settling test | Stays suspended 30+ min | Settles rapidly |
| Downstream crystals | Fine (2--10 um) | Coarse (50+ um) |

Header: Barlow SemiBold 13 pt `#F0EDE8`. Healthy column: JetBrains Mono 12 pt `#27AE60`. Dead column: JetBrains Mono 12 pt `#E05C5C`.

Bottom: `When in doubt, dump and remake. Fresh conditioner costs less than one rejected load.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Failure Diagnosis

**Section label:** `CONDITIONER PROBLEMS -- DIAGNOSIS & FIX` -- Y: 26.7".

**BLOCK F -- Problem Cards (Y: 27.3" to 32.3")**

Four problem cards, 2x2 grid:

| Position | Problem | Cause | Fix |
|---|---|---|---|
| R1C1 | COARSE CRYSTALS | pH wrong; conditioner dead; contaminated; overheated; too dilute | Check pH 7.5--9.5; replace if needed; verify concentration |
| R1C2 | CONDITIONER DEAD | Excess alkaline or acid carryover; bacterial growth; aged past shelf life | Dump and remake; improve upstream rinsing |
| R2C1 | pH RISING | Alkaline cleaner drag-over from upstream | Improve pre-condition rinse; increase overflow rate |
| R2C2 | pH DROPPING | Acid drag-over from phosphate bath (rare -- reverse drag) or contamination | Check for splash-back; isolate stages; dump and remake |

Each card: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06" `#E05C5C`.
Problem: Barlow SemiBold 16 pt `#E05C5C`. Cause: Inter Regular 13 pt `#F0EDE8`. Fix: Inter Medium 13 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Surface Conditioning -- Zinc Phosphate`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Products Finishing; typical zinc phosphate pretreatment parameters. Titanium colloid activators are proprietary -- consult your supplier for product-specific control ranges.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Conditioning Zinc Phosphate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the CC-02 cluster. The conditioned vs. unconditioned crystal comparison is the most important single visual in the entire zinc phosphate series -- it makes the abstract concept of "nucleation sites" tangible. The big stat callouts (2--10 um vs. 50--100+ um) should be readable from 10+ feet. The NO RINSE callout in Zone 5 must be visually impossible to miss -- coral background tint, coral border, coral text. This rule is counterintuitive and the most common setup error.

The "Is Your Conditioner Alive?" health assessment table gives operators an immediate diagnostic tool. If the conditioner is clear instead of milky, it is dead. That one visual cue saves more coatings than any analytical test.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #162 -- Construction Workup v1.0*
*2026-04-26*
