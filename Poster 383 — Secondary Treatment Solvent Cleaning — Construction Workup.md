---
Project: Plating Posters Inc
Poster Number: 383
Title: "Secondary Treatment -- Solvent to Alkaline Transition"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: Industry-standard practices for the solvent-to-alkaline handoff. Covers when solvent cleaning precedes alkaline cleaning (most plating applications) vs. when solvent cleaning is the final step (electronics, optics). The "belt and suspenders" philosophy and its limits.
Process Scope: Secondary treatment after solvent cleaning -- the alkaline soak clean handoff, solvent-only final clean applications, and process sequencing decisions
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - SecondaryTreatment
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #383 -- Construction Workup
## Secondary Treatment -- Solvent to Alkaline Transition

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

After solvent cleaning, what comes next? For plating applications, the answer is almost always "alkaline soak clean." The solvent handles the heavy organic burden; the alkaline cleaner handles residual films, water-soluble contaminants, and the transition to aqueous processing. This poster covers the handoff between solvent and alkaline cleaning, the decision logic for when solvent cleaning is or is not needed, and the rare cases where solvent cleaning stands alone as the final step.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Decision tree (Block B -- HERO):** "Is solvent cleaning needed?" decision flow based on soil type and severity.

2. **Handoff sequence diagram (Block C):** The solvent -> evaporate -> alkaline clean sequence with what each step removes.

3. **Solvent-only final clean panel (Block D):** When solvent cleaning is the endpoint (electronics, optics, aerospace assembly).

4. **Process sequencing table (Block E):** Five common soil scenarios with recommended cleaning sequence.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DECISION TREE + HANDOFF SEQUENCE (2.9"--15.0" / ~12.1" tall)
  Block B: Decision tree hero
  Block C: Handoff sequence diagram

ZONE 3 -- SOLVENT-ONLY APPLICATIONS (15.0"--22.0" / ~7.0" tall)
  Block D: When solvent cleaning is the final step

ZONE 4 -- PROCESS SEQUENCING TABLE (22.0"--28.5" / ~6.5" tall)
  Block E: Five soil scenario sequences

ZONE 5 -- KEY PRINCIPLES (28.5"--32.5" / ~4.0" tall)
  Block F: Quick-reference principles

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SECONDARY TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `The Solvent-to-Alkaline Handoff -- Belt and Suspenders Cleaning` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Solvent dissolves the heavy stuff. Alkaline emulsifies the residual film. Together, they handle what neither can do alone.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Decision Tree + Handoff Sequence (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> DO YOU NEED SOLVENT CLEANING?

---

**BLOCK B -- Decision Tree**

Y: 3.8" to 9.0". Full width.

Decision flow using rounded rects and diamond decision points:

**Start box (X: 9.0", Y: 3.8", W: 6.0", H: 1.2"):**
- Fill `#3A4055`, radius 6
- Text: `WHAT IS THE SOIL?` Barlow SemiBold 18 pt `#F0EDE8`

**Decision diamond 1 (X: 10.5", Y: 5.5", W: 3.0", H: 1.5"):**
- Fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Text: `Heavy grease, wax, tar, silicone, adhesive?` Inter Medium 12 pt `#E8A020`

**YES path (left, X: 2.0", Y: 5.5"):**
- Arrow left, label `YES` Barlow SemiBold 14 pt `#27AE60`
- Box: `SOLVENT CLEAN FIRST` fill `#1E2435`, accent `#E8A020`
- Sub-text: `Then proceed to alkaline soak clean` Inter Regular 12 pt `#F0EDE8`

**NO path (right, X: 17.0", Y: 5.5"):**
- Arrow right, label `NO` Barlow SemiBold 14 pt `#2EC4B6`
- Box: `SKIP SOLVENT -- GO DIRECT TO ALKALINE` fill `#1E2435`, accent `#2EC4B6`
- Sub-text: `Light oils, fingerprints, water-soluble soils` Inter Regular 12 pt `#F0EDE8`

**Decision diamond 2 (below YES, X: 1.5", Y: 7.5", W: 3.0", H: 1.2"):**
- Text: `Plating application?` Inter Medium 12 pt `#E8A020`

**YES -> `Solvent -> Alkaline -> Electroclean -> Acid Activate -> Plate`**
**NO -> `Solvent may be final clean (see Zone 3)`**

---

**BLOCK C -- Handoff Sequence Diagram**

Y: 9.5" to 14.8". Full width.

Section sublabel: `THE "BELT AND SUSPENDERS" SEQUENCE` Barlow SemiBold 18 pt `#2EC4B6`. Y: 9.5".

Three-stage horizontal diagram:

| Stage | X | W | Accent | Title | What It Removes |
|---|---|---|---|---|---|
| 1. Solvent Clean | 0.5" | 7.0" | `#E8A020` | SOLVENT DISSOLVES | Heavy grease, wax, tar, adhesive, silicone, heavy mineral oil |
| 2. Evaporate | 8.0" | 3.0" | `#3A4055` | FLASH OFF | Solvent evaporates; residual film remains |
| 3. Alkaline Soak | 11.5" | 7.0" | `#2EC4B6` | ALKALINE EMULSIFIES | Residual solvent film, water-soluble soils, light oils, fingerprints |

Each stage box: Rounded rect, H: 4.0", fill `#1E2435`, radius 6, top accent 4 pt.

Arrows: 3 pt `#3A4055` between stages.

**Result arrow from Stage 3 (right):**
- Arrow to small box at X: 19.0": `CLEAN -- Ready for electroclean or acid activate` fill `#27AE60` at 15%, border 1 pt `#27AE60`, Barlow SemiBold 14 pt `#27AE60`.

---

### ZONE 3 -- Solvent-Only Applications

**Section label:** Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHEN SOLVENT CLEANING IS THE FINAL STEP

---

**BLOCK D -- Solvent-Only Panel**

Y: 15.9" to 21.8". Two-column layout.

**Left -- Applications (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.5", fill `#1E2435`, radius 6, left accent `#2EC4B6`.

Title: `SOLVENT-ONLY FINAL CLEAN` Barlow SemiBold 18 pt `#2EC4B6`

Four application rows:

| Application | Reason |
|---|---|
| Electronics / PCB assembly | No aqueous residue; rapid drying; non-conductive solvent |
| Optics / precision lenses | Spot-free finish; no water marks |
| Aerospace assembly (non-plating) | Critical cleanliness per MIL-STD; controlled environment |
| Medical device (non-plating) | Residue-free surface per ISO 19227 or manufacturer spec |

Per row:
- Application: Barlow SemiBold 14 pt `#F0EDE8`
- Reason: Inter Regular 12 pt `#F0EDE8` at 80%

**Right -- Requirements (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.5", fill `#1E2435`, radius 6, left accent `#E8A020`.

Title: `WHEN SOLVENT IS FINAL, PURITY IS CRITICAL` Barlow SemiBold 18 pt `#E8A020`

Body: Inter Regular 14 pt `#F0EDE8`:
```
If no alkaline clean follows:
  - Use high-purity grade solvent
  - Multi-stage rinsing (dirty -> clean -> vapor)
  - Final exposure must be to freshly distilled
    solvent (vapor zone only)
  - Any soil redeposition is a defect --
    there is no downstream process to save you
```

Caution callout at bottom:
- Inter Medium 13 pt `#E05C5C`: `For plating applications, solvent-only cleaning is almost NEVER sufficient. Residual solvent film on the surface will cause plating adhesion failure.`

---

### ZONE 4 -- Process Sequencing Table

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> FIVE SOIL SCENARIOS -- RECOMMENDED SEQUENCES

---

**BLOCK E -- Scenario Table**

Y: 22.9" to 28.3". Column widths (23.0" total):
- Scenario (5.0") | Soil Type (5.0") | Recommended Sequence (9.0") | Notes (4.0")

Header row: fill `#3A4055`, H: 0.5".

| Scenario | Soil Type | Recommended Sequence | Notes |
|---|---|---|---|
| Light shop soil | Fingerprints, light cutting oil | Alkaline Soak -> Rinse -> Electroclean | No solvent needed |
| Medium industrial | Mineral oil, synthetic coolant | Alkaline Soak -> Rinse -> Electroclean | Soak clean handles this |
| Heavy grease / wax | Drawing compound, buffing compound, wax | Solvent Clean -> Alkaline Soak -> Rinse -> Electroclean | Solvent dissolves bulk soil first |
| Silicone contamination | Silicone mold release, silicone sealant | Solvent Clean -> Alkaline Soak (2x cycle) -> Rinse -> Electroclean | Silicone is extremely persistent |
| Tar / adhesive | Hot-melt adhesive, tar, asphalt | Solvent Clean -> Alkaline Soak -> Rinse -> Electroclean | May need repeat solvent cycle |

Data: Inter Regular 12 pt. Scenario names: Barlow SemiBold 13 pt. "No solvent needed" rows in `#2EC4B6`. Solvent-required rows in `#E8A020`.

---

### ZONE 5 -- Key Principles

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> TRANSITION PRINCIPLES -- QUICK REFERENCE

---

**BLOCK F -- Four Principle Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Principle | Accent |
|---|---|---|---|
| 1 | 0.5" | Solvent first, alkaline second -- dissolve the bulk, then emulsify the residual | `#2EC4B6` |
| 2 | 6.33" | Light soils skip solvent entirely -- alkaline soak clean handles fingerprints and cutting oil | `#27AE60` |
| 3 | 12.16" | Silicone is the worst -- it requires solvent AND aggressive alkaline cleaning, often multiple cycles | `#E05C5C` |
| 4 | 18.0" | For plating, solvent alone is NEVER the final clean -- always follow with aqueous processing | `#E8A020` |

---

### ZONE 6 -- Footer

Standard. Title: `Secondary Treatment -- Solvent to Alkaline Transition`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cleaning sequences shown are typical recommendations for common soil types. Specific cleaning requirements vary by substrate, soil, and downstream process specification. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Secondary Treatment Solvent Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The decision tree hero is the most operationally useful element -- it answers the question every process engineer asks: "Do I need a solvent pre-clean or can I go straight to alkaline?" The five-scenario table in Zone 4 provides concrete guidance for the most common soil situations. The solvent-only final clean panel (Zone 3) is included for completeness but carries a prominent warning that it is NOT appropriate for plating applications. The silicone contamination callout deserves extra visual weight because silicone is the single most persistent contaminant in metal finishing -- shops that encounter it for the first time are often shocked at how difficult it is to remove.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #383 -- Construction Workup v1.0*
*2026-04-26*
