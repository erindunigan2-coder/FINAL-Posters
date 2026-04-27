---
Project: Plating Posters Inc
Poster Number: 397
Title: "Secondary Treatment -- Acid & Alkaline Neutralization"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-8)"
Technical Source: Industry-standard neutralization practices for transitions between alkaline and acid processes on plating lines. Acid neutralization, alkaline neutralization, inhibited acid dip, and passivation rinse for stainless steel after pickle. Per Metal Finishing Guidebook and general industry knowledge.
Process Scope: Secondary treatment -- acid neutralization after alkaline cleaning, alkaline neutralization after acid pickle, inhibited acid dip, and passivation rinse for stainless
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Neutralization
  - AcidDip
  - Passivation
  - SecondaryTreatment
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT08
---

# Poster #397 -- Construction Workup
## Secondary Treatment -- Acid & Alkaline Neutralization

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Neutralization tanks are the transition zones between alkaline and acid worlds on the plating line. Most operators know they exist but few understand exactly what each does and when one is needed vs. when thorough rinsing alone is sufficient. This poster covers the four major neutralization scenarios: acid neutralization after alkaline clean, alkaline neutralization after acid pickle, the inhibited acid dip (combination activation/neutralization), and the passivation rinse for stainless after pickle.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Four neutralization scenarios (Block B -- HERO):** Four tall callout panels showing when and how each neutralization type is used.

2. **"When is neutralization needed?" decision table (Block D):** Process transition -> neutralization required? -> why or why not.

3. **Inhibited acid dip detail (Block E):** The most common combined activation/neutralization step.

4. **Passivation rinse for stainless (Block F):** Cross-reference to Cluster 4 with key points.

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

ZONE 2 -- FOUR NEUTRALIZATION SCENARIOS (2.9"--15.0" / ~12.1" tall)
  Block B: Four scenario panels (HERO)
  Block C: pH transition diagram

ZONE 3 -- DECISION TABLE (15.0"--22.0" / ~7.0" tall)
  Block D: "When is neutralization needed?" table

ZONE 4 -- INHIBITED ACID DIP + PASSIVATION (22.0"--28.5" / ~6.5" tall)
  Block E: Inhibited acid dip detail
  Block F: Passivation rinse for stainless

ZONE 5 -- KEY PRINCIPLES (28.5"--32.5" / ~4.0" tall)
  Block G: Quick-reference neutralization rules

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NEUTRALIZATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Acid & Alkaline Neutralization -- Bridging the pH Gap` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Every transition from alkaline to acid (or acid to alkaline) needs a bridge. Sometimes that bridge is a dedicated neutralization tank. Sometimes a good rinse is enough. Know the difference.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Four Neutralization Scenarios (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> FOUR NEUTRALIZATION SCENARIOS

---

**BLOCK B -- Four Scenario Panels**

Y: 3.8" to 12.5". Four callout boxes in a 2x2 grid. Gap: 0.33".

Each box: Rounded rect, W: 11.17", H: 4.1", fill `#1E2435`, radius 6, left accent 0.06".

**Panel 1 (R1C1, X: 0.5") -- Acid Neutralization After Alkaline Clean:**
- Accent: `#E8A020`
- Title: `ALKALINE -> ACID TRANSITION` Barlow SemiBold 18 pt `#E8A020`
- Transition arrow: `pH 12-14 --> pH 2-3` JetBrains Mono 16 pt `#F0EDE8`
- Solution: `Dilute H2SO4 or HCl: 1-5% (10-50 g/L)` JetBrains Mono 13 pt `#F0EDE8`
- Temperature: `Ambient` JetBrains Mono 13 pt `#F0EDE8`
- Time: `15-30 seconds` JetBrains Mono 13 pt `#F0EDE8`
- Purpose: Inter Regular 13 pt: `Remove alkaline film from part surface before acid activation. Prevents alkaline dragout from neutralizing the acid bath.`
- Note: Inter Medium 12 pt `#2EC4B6`: `Most common neutralization step on a plating line.`

**Panel 2 (R1C2, X: 12.0") -- Alkaline Neutralization After Acid Pickle:**
- Accent: `#2EC4B6`
- Title: `ACID -> ALKALINE TRANSITION` Barlow SemiBold 18 pt `#2EC4B6`
- Transition arrow: `pH 1-3 --> pH 9-11` JetBrains Mono 16 pt `#F0EDE8`
- Solution: `Dilute NaOH or Na2CO3: 1-3% (10-30 g/L)` JetBrains Mono 13 pt `#F0EDE8`
- Temperature: `Ambient` JetBrains Mono 13 pt `#F0EDE8`
- Time: `15-30 seconds` JetBrains Mono 13 pt `#F0EDE8`
- Purpose: Inter Regular 13 pt: `Remove acid residue before alkaline plating bath (e.g., alkaline zinc). Prevents acid dragout from attacking alkaline bath chemistry.`
- Note: Inter Medium 12 pt `#E8A020`: `Less common -- only needed when acid precedes alkaline plating.`

**Panel 3 (R2C1, X: 0.5") -- No Neutralization Needed:**
- Accent: `#27AE60`
- Title: `ACID -> ACID PLATING (NO NEUTRALIZATION)` Barlow SemiBold 18 pt `#27AE60`
- Transition: `pH 1-3 --> pH 1-5 (acid plating bath)` JetBrains Mono 16 pt `#F0EDE8`
- Solution: `None -- direct rinse only` JetBrains Mono 13 pt `#F0EDE8`
- Purpose: Inter Regular 13 pt: `Mild acid residue on the part surface is COMPATIBLE with acid plating baths (acid copper, acid zinc, nickel). No neutralization step needed -- a thorough rinse is sufficient.`
- Note: Inter Medium 12 pt `#27AE60`: `Most common situation -- acid activate -> rinse -> acid plate.`

**Panel 4 (R2C2, X: 12.0") -- Inhibited Acid Dip:**
- Accent: `#E8A020`
- Title: `INHIBITED ACID DIP (COMBINED STEP)` Barlow SemiBold 18 pt `#E8A020`
- Solution: `Dilute H2SO4 or HCl: 3-10% + wetting agent + inhibitor` JetBrains Mono 13 pt `#F0EDE8`
- Temperature: `Ambient` JetBrains Mono 13 pt `#F0EDE8`
- Time: `15-60 seconds` JetBrains Mono 13 pt `#F0EDE8`
- Purpose: Inter Regular 13 pt: `Combines neutralization + surface activation in one step. Removes alkaline film, activates the surface, and minimizes base metal attack via inhibitor.`
- Note: Inter Medium 12 pt `#E8A020`: `Very common in practice -- often replaces separate neutralization + acid activate.`

---

**BLOCK C -- pH Transition Diagram**

Y: 12.8" to 14.8". Full width.

Horizontal pH scale from 0 to 14:
- Rounded rect, X: 0.5", W: 23.0", H: 0.6", fill gradient:
  - pH 0-3: `#E05C5C` at 20%
  - pH 4-6: `#E8A020` at 15%
  - pH 7 (neutral): `#27AE60` at 20%
  - pH 8-10: `#E8A020` at 15%
  - pH 11-14: `#2EC4B6` at 20%

Labels: JetBrains Mono 12 pt.
- pH 1-3: `ACID PICKLE / ACTIVATE`
- pH 7: `NEUTRAL`
- pH 12-14: `ALKALINE CLEAN`

Arrows showing transitions:
- Alkaline->Acid: arrow from pH 13 to pH 2, `#E8A020`, label `ACID NEUTRALIZATION`
- Acid->Alkaline: arrow from pH 2 to pH 10, `#2EC4B6`, label `ALKALINE NEUTRALIZATION`

---

### ZONE 3 -- Decision Table

**Section label:** Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHEN IS NEUTRALIZATION NEEDED?

---

**BLOCK D -- Decision Table**

Y: 15.9" to 21.8". Column widths (23.0" total):
- Previous Step (5.0") | Next Step (5.0") | Neutralization? (4.0") | Reason (9.0")

Header row: fill `#3A4055`, H: 0.5".

| Previous Step | Next Step | Neutralization? | Reason |
|---|---|---|---|
| Alkaline soak clean | Electroclean (alkaline) | NO | Both are alkaline -- compatible chemistry |
| Alkaline soak clean | Acid activate | OPTIONAL | Rinse usually sufficient; acid activate handles residual alkali |
| Electroclean | Acid activate | OPTIONAL | Most common: rinse between is adequate for standard work |
| Acid pickle (HCl/H2SO4) | Alkaline zinc plating | YES | Acid carryover attacks alkaline bath; dedicated neutralization or thorough rinsing required |
| Acid pickle (stainless) | Next process | PASSIVATION | Nitric acid passivation restores Cr2O3 film; this IS the neutralization for stainless |
| Any process | Same-chemistry process | NO | No pH transition = no neutralization |

Data: Inter Regular 12 pt. "YES" in `#E8A020`. "NO" in `#27AE60`. "OPTIONAL" in `#2EC4B6`. "PASSIVATION" in `#E05C5C`.

---

### ZONE 4 -- Inhibited Acid Dip + Passivation

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

**Two-column layout:**

**Left -- Inhibited Acid Dip Detail (X: 0.5", W: 11.0"):**

**BLOCK E:**

Rounded rect, H: 6.0", fill `#1E2435`, radius 6, left accent `#E8A020`.

Title: `INHIBITED ACID DIP -- IN DETAIL` Barlow SemiBold 18 pt `#E8A020`

Body:
```
Chemistry:
  Acid: 3-10% H2SO4 or HCl by volume
  Wetting agent: promotes uniform contact
  Inhibitor: reduces base metal attack

Function (3-in-1):
  1. Neutralizes alkaline residue
  2. Activates the surface (light etch)
  3. Inhibitor prevents over-etching

Immersion time: 15-60 seconds
Temperature: Ambient (room temp)

Common use: between electroclean and plating
  when a single-step activation is preferred
```

JetBrains Mono 13 pt for chemistry and parameters. Inter Regular 13 pt for descriptive text.

**Right -- Passivation Rinse for Stainless (X: 12.0", W: 11.5"):**

**BLOCK F:**

Rounded rect, H: 6.0", fill `#1E2435`, radius 6, left accent `#E05C5C`.

Title: `PASSIVATION RINSE -- STAINLESS STEEL` Barlow SemiBold 18 pt `#E05C5C`

Body:
```
After pickling stainless steel, a passivation
step serves as BOTH neutralization and surface
restoration:

  - Removes residual pickle acid
  - Restores the Cr2O3 passive film
  - Creates the corrosion-resistant surface

Common passivation solutions:
  20-50% HNO3 (nitric acid)
  or citric acid formulation (ASTM A967)

Immersion: 20-60 min depending on grade
Temperature: Ambient to 150 F (66 C)

See Cluster CT-04 posters for full
passivation detail.
```

Cross-reference note: Inter Medium 12 pt `#2EC4B6`: `Full passivation coverage in CT-04: Acid Pickling (Stainless Steel) cluster.`

---

### ZONE 5 -- Key Principles

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> NEUTRALIZATION RULES -- QUICK REFERENCE

---

**BLOCK G -- Four Principle Cards**

Y: 29.3" to 32.3". Four cards in a single row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Principle | Accent |
|---|---|---|---|
| 1 | 0.5" | If both steps are the same pH range (alkaline->alkaline or acid->acid), no neutralization needed | `#27AE60` |
| 2 | 6.33" | Alkaline residue carried into acid baths neutralizes the acid and increases chemical consumption | `#E8A020` |
| 3 | 12.16" | The inhibited acid dip combines neutralization + activation in one tank -- the most practical solution | `#2EC4B6` |
| 4 | 18.0" | For stainless steel, passivation IS the neutralization -- it restores the protective Cr2O3 film | `#E05C5C` |

---

### ZONE 6 -- Footer

Standard. Title: `Secondary Treatment -- Acid & Alkaline Neutralization`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Neutralization procedures and concentrations shown are typical industry values. Specific formulations and procedures vary by application and process specification. Consult your process supplier for site-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Secondary Treatment Neutralization -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The four-panel hero layout makes it immediately clear that there are four distinct neutralization scenarios -- and that the most common scenario (acid->acid plating) requires NO neutralization at all. This is the most valuable insight on the poster because many junior operators assume every transition needs a neutralization tank. The decision table in Zone 3 provides the definitive "do I need it?" reference. The inhibited acid dip panel (Zone 4) deserves detailed treatment because this single step replaces two separate tanks in many practical line configurations. The passivation callout provides a bridge to the Stainless Steel Pickling cluster (CT-04).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #397 -- Construction Workup v1.0*
*2026-04-26*
