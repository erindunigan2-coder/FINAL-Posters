---
Project: Plating Posters Inc
Poster Number: 348
Title: "Secondary Cleaning -- Alkaline (If Required)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-1.6)"
Process Scope: Secondary cleaning considerations -- two-stage cleaning, silicate residue removal, spray pre-clean, and the soak-to-electroclean handoff
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - AlkalineCleaning
  - SecondaryCleaning
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT01
---

# Poster #348 -- Construction Workup
## Secondary Cleaning -- Alkaline (If Required)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 6 of 7 in the CT-01 cluster. This poster covers the "what comes next" scenarios after the primary soak clean -- two-stage cleaning for heavy soils, silicate residue removal on aluminum, spray cleaning as a pre-soak step, and the critical handoff from soak cleaning to electrocleaning. The hero visual is a decision flowchart: "Does your situation require a secondary step?"

This is the most conditional poster in the cluster -- it covers scenarios that apply to some lines but not others. The operator needs to know when these steps apply and when to skip them.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Decision flowchart (Block B -- HERO):** "Do I need a secondary step?" branching to four scenarios.
2. **Two-stage cleaning panel (Block D):** Heavy-duty vs. maintenance comparison.
3. **Aluminum desmut callout (Block E):** Silicate residue removal.
4. **Spray pre-clean panel (Block F):** Automatic line pre-cleaning.
5. **Electroclean handoff callout (Block G):** The soak-to-electroclean transition.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 19.5" / 25.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 6 of 7 highlighted (Amber)
ZONE 3 -- DECISION FLOWCHART / HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- TWO-STAGE CLEANING (13.5"--19.5" / ~6.0")
ZONE 5 -- ALUMINUM DESMUT + SPRAY PRE-CLEAN (19.5"--25.0" / ~5.5")
ZONE 6 -- THE ELECTROCLEAN HANDOFF (25.0"--32.5" / ~7.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SECONDARY CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `When One Soak Is Not Enough -- Decision Points and Extra Steps` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Not every line needs a secondary step. But when you do, skipping it is the fastest path to adhesion failure.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Conditional step -- applies when primary soak clean alone is insufficient for the soil type or downstream process`

---

### ZONE 3 -- Decision Flowchart (HERO)

**Section label:** `DO YOU NEED A SECONDARY CLEANING STEP?` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 13.0")**

Entry point (top center):
- Rounded rect W: 6.0", H: 1.0", fill `#2EC4B6` at 20%, border 2 pt `#2EC4B6`
- Text: `PARTS CLEANED IN PRIMARY SOAK` Barlow SemiBold 16 pt `#2EC4B6`

Decision 1 (Y: 6.5"):
- Diamond W: 5.0", H: 1.5", fill `#E8A020` at 20%, border 1 pt `#E8A020`
- Text: `HEAVY SOIL?` `(buffing compound, drawing compound, carbonized oil)` Barlow SemiBold 14 pt `#E8A020`
- YES -> Two-Stage Clean (left branch)
- NO -> Decision 2 (right/down)

Decision 2 (Y: 8.5"):
- Diamond same style
- Text: `ALUMINUM SUBSTRATE?` `(after silicated cleaner)`
- YES -> Desmut Step (left branch)
- NO -> Decision 3 (right/down)

Decision 3 (Y: 10.5"):
- Diamond same style
- Text: `CRITICAL PLATING?` `(decorative Ni/Cr, gold, silver)`
- YES -> Electroclean Required (left branch)
- NO -> Proceed Direct (right)

Four destination boxes:

| Destination | Position | Accent | Text |
|---|---|---|---|
| Two-Stage Clean | Left, Y: 6.5" | `#E8A020` | `USE TWO-STAGE CLEANING` / `See Zone 4` |
| Desmut Step | Left, Y: 8.5" | `#E05C5C` | `ADD ACID DESMUT` / `1-5% HNO3 or proprietary` / `See Zone 5` |
| Electroclean | Left, Y: 10.5" | `#2EC4B6` | `ADD ELECTROCLEANING` / `See Poster #350-356` |
| Proceed Direct | Right, Y: 10.5" | `#27AE60` | `PROCEED TO ACID ACTIVATE` / `Single soak sufficient` |

Each destination box: Rounded rect W: 5.0", H: 1.2", fill `#1E2435`, left accent 0.06".

---

### ZONE 4 -- Two-Stage Cleaning

**Section label:** `TWO-STAGE CLEANING -- HEAVY SOIL PROTOCOL` -- Y: 13.7".

**BLOCK D -- Side-by-Side Comparison (Y: 14.3" to 19.3")**

**Left -- Stage 1: Heavy-Duty (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `STAGE 1: HEAVY-DUTY SOAK` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `The Workhorse` Inter Regular 14 pt `#F0EDE8` at 60%
- Parameters: JetBrains Mono 14 pt:
```
Higher concentration
Higher temp: 170-195 F (75-90 C)
Longer time: 5-10 min
Purpose: Strip gross soil
```
- Notes: Inter Regular 13 pt `#F0EDE8`:
```
- Handles heavy buffing compound
- Handles drawing compounds and carbonized oils
- This bath gets dirty fast -- dump more frequently
- May include mechanical agitation or ultrasonics
```

**Right -- Stage 2: Maintenance (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `STAGE 2: MAINTENANCE SOAK` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `The Finisher` Inter Regular 14 pt `#F0EDE8` at 60%
- Parameters:
```
Lower concentration
Standard temp: 150-170 F (65-75 C)
Shorter time: 3-5 min
Purpose: Final soil removal
```
- Notes:
```
- Bath stays clean much longer
- Only sees residual soil the heavy-duty missed
- Dump cycle 3-5x longer than Stage 1
- This is the bath that matters for water break pass
```

**Bottom connector:**
- Arrow from Stage 1 to Stage 2 with label: `RINSE BETWEEN STAGES` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Aluminum Desmut + Spray Pre-Clean

**Two-column layout (Y: 19.7" to 24.8")**

**Left -- Aluminum Desmut (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

Title: `ALUMINUM DESMUT -- NOT OPTIONAL` Barlow SemiBold 18 pt `#E05C5C`

Body: Inter Regular 13 pt `#F0EDE8`:
```
After alkaline cleaning of aluminum, a dilute acid
dip is often REQUIRED to remove:

- Silicate residue from the cleaner
- Light etch smut (aluminum oxide + alloying elements)

Typical: 1-5% HNO3 (nitric acid) or proprietary desmut

This is standard practice in aluminum finishing --
not a failure of the cleaner. The cleaner leaves the
silicate behind intentionally (it was protecting the
aluminum from excessive etch).
```

Highlight: `Every aluminum plating line should have a desmut tank after the alkaline clean` Inter Medium 12 pt `#E8A020`

**Right -- Spray Pre-Clean (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `SPRAY PRE-CLEAN` Barlow SemiBold 18 pt `#2EC4B6`
Subtitle: `Automatic Lines Only` Inter Regular 14 pt `#F0EDE8` at 60%

Body:
```
Used on automatic lines BEFORE soak clean to remove
gross contamination (heavy chips, cutting fluid, bulk oil).

Requirements:
- Low-foam surfactant (HLB 8-12)
- Pressure: 15-30 psi
- Temperature: 130-170 F (55-75 C)
- Reduces soil load on soak cleaner
- Extends soak cleaner bath life significantly
```

Note: `High-foam surfactant in a spray system = overflow disaster` Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- The Electroclean Handoff

**Section label:** `THE SOAK-TO-ELECTROCLEAN HANDOFF` -- Y: 25.2".

**BLOCK G -- Handoff Panel (Y: 25.8" to 32.3")**

Full-width rounded rect H: 6.0", fill `#1E2435`, top accent 4 pt `#2EC4B6`.

**Two-column interior:**

**Left -- Why Electroclean Follows Soak (W: 11.0"):**

Title: `WHY THE COMBINATION?` Barlow SemiBold 18 pt `#2EC4B6`

Body: Inter Regular 14 pt `#F0EDE8`, line height 155%:
```
Soak cleaning removes BULK soil:
  - Oils, greases, fingerprints, compounds

Electrocleaning removes TRACE contamination:
  - Monolayer films, smut, embedded particles

The combination is industry standard for
critical plating applications:
  - Decorative nickel/chrome
  - Gold plating
  - Silver plating
  - Any deposit where adhesion is paramount
```

**Right -- The Rule (W: 11.0"):**

Rounded rect W: 10.0", H: 3.0", fill `#E8A020` at 15%, border 1 pt `#E8A020`, centered in right column.

Title: `THE GOLDEN RULE` Barlow Condensed ExtraBold 22 pt `#E8A020`

Body: Inter Medium 16 pt `#F0EDE8`:
```
Soak clean FIRST, then electroclean.

Never use electrocleaning as
the primary cleaning step.

Electrocleaning is a finishing step,
not a workhorse. Overloading it with
gross soil contaminates the bath and
defeats its purpose.
```

---

### ZONE 7 -- Footer

Standard. Title: `Secondary Cleaning -- Alkaline (If Required)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook. Desmut formulations and spray parameters vary by proprietary product. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Secondary Cleaning Alkaline -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the "conditional logic" poster -- it tells the operator when extra steps are needed and when they can skip them. The decision flowchart hero is the right choice because the content is inherently branching. The two-stage cleaning comparison and aluminum desmut sections will resonate strongly with shops that have struggled with these issues. The electroclean handoff section sets up the transition to the CT-02 cluster (Posters 350-356) -- a natural cross-reference point.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #348 -- Construction Workup v1.0*
*2026-04-26*
