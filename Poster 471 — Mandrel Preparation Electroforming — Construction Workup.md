---
Project: Plating Posters Inc
Poster Number: 471
Title: "Mandrel Preparation -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 8, Sections 8.3--8.4)"
Technical Source: Mandrel types (permanent, expendable, semi-expendable), surface finishing, release agents (chromate passivation, proprietary compounds), making non-conductive mandrels conductive (electroless Ni, Ag paint, graphite, vacuum metallization). The mandrel IS the mold -- its surface becomes the part's exterior.
Process Scope: Electroforming -- mandrel preparation (Stages 1--3 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Electroforming
  - MandrelPreparation
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #471 -- Construction Workup
## Mandrel Preparation -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Mandrel preparation is the foundation of electroforming -- equivalent in importance to surface preparation in plating. The mandrel's surface finish is replicated exactly on the part's exterior. The mandrel's dimensional accuracy IS the part's dimensional accuracy. The choice of mandrel type (permanent, expendable, semi-expendable) and release agent determines whether separation will work or destroy the part. This poster covers all three preparation stages.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Mandrel types comparison (Block B -- HERO):** Three-panel comparison of permanent, expendable, and semi-expendable mandrels.
2. **Release agents table (Block D):** Methods for enabling separation on permanent mandrels.
3. **Making non-conductive mandrels conductive (Block E):** Techniques for wax, plastic, glass mandrels.
4. **Surface finish requirements (Block F):** Ra targets by application.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stages 1--3 highlighted (Amber)
ZONE 3 -- MANDREL TYPES HERO (4.2"--14.5" / ~10.3")
  Block B: Three mandrel type panels
  Block C: Key principle callout
ZONE 4 -- RELEASE AGENTS (14.5"--22.0" / ~7.5")
  Block D: Release agent methods table
  Block E: Making non-conductive mandrels conductive
ZONE 5 -- SURFACE FINISH REQUIREMENTS (22.0"--28.5" / ~6.5")
  Block F: Ra targets by application
  Block G: Draft angle guidance
ZONE 6 -- COMMON MANDREL PROBLEMS (28.5"--32.5" / ~4.0")
  Block H: Troubleshooting strip
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MANDREL PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Stages 1--3 of 10 -- The Mold That Makes the Part` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The mandrel's surface becomes the part's surface. The mandrel's dimensions become the part's dimensions. Get the mandrel right or nothing else matters.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Stages 1--3 highlighted (Amber). Others dimmed.

Below: `Before: Design drawing --> After: Finished, conductive mandrel ready for the electroforming tank` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Mandrel Types Hero

**Section label:** `MANDREL TYPES` -- Y: 4.4".

---

**BLOCK B -- Three Mandrel Type Panels (Y: 5.0" to 12.5")**

Three tall panels side by side:

**Panel 1 -- Permanent Mandrel (X: 0.5", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `PERMANENT` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `Reusable -- hundreds of cycles` Inter Medium 13 pt `#F0EDE8` at 60%

Materials (JetBrains Mono 13 pt `#F0EDE8`):
```
Stainless steel
Nickel
Chrome-plated steel
Glass (for optical mandrels)
```

Separation (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
Release agent required (applied each cycle):
  - Chromate passivation dip
  - Proprietary parting compound
  - Electrolytic oxidation

Separation method:
  - Mechanical (pry, flex)
  - Thermal differential
```

Best for (Inter Medium 12 pt `#27AE60`):
```
Production runs with consistent geometry.
Highest dimensional repeatability.
Lowest per-part cost at volume.
```

**Panel 2 -- Expendable Mandrel (X: 8.33", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `EXPENDABLE` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Single use -- dissolved or destroyed` Inter Medium 13 pt `#F0EDE8` at 60%

Materials (JetBrains Mono 13 pt `#F0EDE8`):
```
Aluminum (dissolve in NaOH)
Zinc (dissolve in HCl)
Wax (melt out)
ABS plastic (dissolve in acetone)
3D-printed polymer
```

Separation (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
No release agent needed -- mandrel is destroyed.

Dissolution:
  - Al: 10--20% NaOH at 60--80 C
  - Zn: 10--20% HCl at ambient
  - Wax: heat or solvent
  - Plastic: solvent bath
```

Best for (Inter Medium 12 pt `#E8A020`):
```
Complex internal geometry (no draft).
Undercuts impossible to separate mechanically.
Prototype and low-volume runs.
```

**Panel 3 -- Semi-Expendable Mandrel (X: 16.16", W: 7.33"):**
- Rounded rect, H: 7.0", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `SEMI-EXPENDABLE` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Re-meltable -- dozens of cycles` Inter Medium 13 pt `#F0EDE8` at 60%

Materials (JetBrains Mono 13 pt `#F0EDE8`):
```
Cerrolow (mp 47 C)
Cerrobend (mp 70 C)
Wood's metal (mp 70 C)
Custom low-melting alloys
```

Separation (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
Melt out at low temperature:
  - Heat assembly above mp
  - Mandrel material flows out
  - Collect, re-melt, re-cast

No chemical dissolution needed.
```

Best for (Inter Medium 12 pt `#2EC4B6`):
```
Complex geometry with moderate volume.
When chemical dissolution is undesirable.
NOTE: Some contain lead, cadmium, or
  bismuth -- check toxicity / RoHS.
```

---

**BLOCK C -- Key Principle Callout (Y: 12.8" to 14.0")**

Full-width rounded rect, H: 1.0", fill `#E8A020` at 15%, border 1 pt `#E8A020`.
Text centered: `The mandrel is a negative of the final part. The mandrel's EXTERIOR surface becomes the electroformed part's INTERIOR surface -- which is the precision surface. Polish the mandrel to the spec the part must meet.` Barlow SemiBold 14 pt `#E8A020`.

---

### ZONE 4 -- Release Agents

**Section label:** `RELEASE AGENTS & CONDUCTIVE COATINGS` -- Y: 14.7".

---

**BLOCK D -- Release Agent Table (Y: 15.3" to 18.5")**

Table -- columns: Agent (5.0") | Application (5.0") | Mandrel Type (3.5") | Pros (5.0") | Limitations (4.5")

| Agent | Application | Mandrel Type | Pros | Limitations |
|---|---|---|---|---|
| Chromate passivation (K2Cr2O7 2--5%) | Dip 30--60 sec at 20--50 C | Permanent (SS, Ni) | Proven, reliable, inexpensive | Cr(VI) -- RoHS/REACH concern |
| Trivalent Cr passivation | Alternative to hexavalent chromate | Permanent | RoHS compliant | Less proven; may be less reliable |
| Proprietary parting compounds | Brush or spray on mandrel | Permanent | No Cr(VI); easy to apply | Cost; supplier-dependent |
| Electrolytic oxidation | Anodic in NaOH to form thin oxide | Permanent (Ni mandrels) | No chemicals to dispose | Setup required |
| None required | -- | Expendable / semi-expendable | Simplest | N/A |

Header: `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

---

**BLOCK E -- Making Non-Conductive Mandrels Conductive (Y: 19.0" to 21.8")**

Table -- columns: Method (5.0") | Thickness (3.0") | Application (5.5") | Pros (5.0") | Limitations (4.5")

| Method | Thickness | Application | Pros | Limitations |
|---|---|---|---|---|
| Electroless nickel | 0.5--2 um | Universal; wax, plastic, glass | Excellent adhesion; uniform; preferred | Requires activation chemistry |
| Silver paint (conductive) | 5--25 um | Art, jewelry, prototypes | Quick, easy, brush or spray | Less uniform; may have voids |
| Graphite spray/suspension | 1--5 um | Non-critical; quick prototyping | Fast, cheap | Some porosity; rough surface |
| Vacuum metallization (sputter/evaporate) | 50--200 nm | Precision: LIGA, optical | Excellent for fine detail | Requires vacuum equipment |
| Conductive lacquer (Cu or Ag filled) | 5--50 um | Commercial products | Readily available | Thickness variation |

Header: `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Surface Finish Requirements

**Section label:** `MANDREL SURFACE FINISH REQUIREMENTS` -- Y: 22.2".

---

**BLOCK F -- Ra Targets Table (Y: 22.9" to 26.0")**

Table -- columns: Application (6.0") | Mandrel Ra (um) (3.5") | Mandrel Ra (uin) (3.0") | Mandrel Finish (5.0") | Notes (5.5")

| Application | Ra (um) | Ra (uin) | Finish | Notes |
|---|---|---|---|---|
| Optical reflectors | < 0.01 | < 0.4 | Optical polish | Mandrel = optical quality mirror |
| Precision waveguides | < 0.05 | < 2 | Mirror polish | Surface roughness affects signal loss |
| CD/DVD stampers | < 0.02 | < 0.8 | Optical polish | Nanoscale feature replication |
| Mold inserts | 0.05--0.4 | 2--16 | Fine grind to polish | Texture may be intentional |
| General industrial | < 0.2 | < 8 | Fine grind | Good-quality engineering finish |
| Prototyping | 0.4--1.6 | 16--63 | Machine finish | Acceptable for form/fit |

Header: `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`.

Bottom note: `Remember: the mandrel surface becomes the INTERIOR of the electroform -- this is usually the functional/precision surface.` Inter Medium 12 pt `#E8A020`

---

**BLOCK G -- Draft Angle Guidance (Y: 26.5" to 28.0")**

Rounded rect, X: 0.5", W: 23.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `DRAFT ANGLES FOR PERMANENT MANDRELS` Barlow SemiBold 16 pt `#2EC4B6`

Text (Inter Regular 13 pt `#F0EDE8`):

> Include 1--3 degrees of draft on all permanent mandrel surfaces to enable mechanical separation. Without draft, the deposit mechanically locks onto the mandrel. For expendable mandrels, draft is not required -- the mandrel is destroyed during separation. For complex geometry with zero draft, expendable or semi-expendable mandrels are the only option.

---

### ZONE 6 -- Common Mandrel Problems

**Section label:** `MANDREL TROUBLESHOOTING` -- Y: 28.7".

---

**BLOCK H -- Four Problem Cards (Y: 29.4" to 32.0")**

Four cards in a row:

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CANNOT SEPARATE | No release agent; deposit grew into undercuts; no draft | Fresh release agent; add draft; switch to expendable mandrel |
| 2 | 6.33" | POOR INTERIOR FINISH | Mandrel too rough; scratches in mandrel surface | Re-polish mandrel to spec; handle with gloves |
| 3 | 12.16" | NON-UNIFORM DEPOSITION | Non-conductive mandrel has patchy conductive layer | Verify full coverage of electroless Ni or Ag paint; inspect before plating |
| 4 | 18.0" | MANDREL DAMAGE | Mandrel deformed during separation or re-use | Inspect mandrel after each cycle; replace when worn |

Each card: Rounded rect, W: 5.5", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Interior per card:
- Problem: Barlow SemiBold, 14 pt, `#E05C5C`
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Mandrel Preparation -- Electroforming`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM B832; ASM Handbook Vol. 5. Mandrel materials, release agents, and surface finish requirements vary by application. Chromate release agents may contain Cr(VI) -- verify RoHS/REACH compliance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Mandrel Preparation Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The mandrel is half the story in electroforming -- three of the ten process stages are mandrel preparation. The three-panel comparison (Block B) is the decision matrix that determines the entire downstream process. The "mandrel surface = part surface" principle (Block C) must be impossible to miss. The RoHS note on chromate release agents and low-melting alloys containing lead/cadmium is a real-world compliance flag.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #471 -- Construction Workup v1.0*
*2026-04-26*
