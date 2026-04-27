---
Project: Plating Posters Inc
Poster Number: 375
Title: "Rinse -- Post-Descale"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Post-descale rinse and cleaning protocols for mechanical and chemical descaling. Covers dust removal, permanganate residue removal, and molten salt quench/rinse sequence.
Process Scope: Rinse and cleaning steps following mechanical and chemical descaling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - Rinse
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #375 -- Construction Workup
## Rinse -- Post-Descale

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Post-descale rinsing is fundamentally different depending on whether you just blasted parts (no water rinse -- go straight to alkaline clean) or ran a chemical descaling process (thorough water rinse to remove chemical residue). This poster splits cleanly into those two paths. The molten salt quench is particularly dramatic -- the water quench IS the first "rinse" and it involves violent steam generation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Dual-path layout (Block B -- HERO):** Left path for post-mechanical, right path for post-chemical. Each path shows the sequence of steps from descaling to "ready for next process."

2. **Molten salt quench callout (Block C):** Special emphasis on the water quench procedure with safety warning.

3. **Rinse quality monitoring table (Block D):** pH, conductivity, and visual checks.

4. **Drag-out and waste considerations (Block E):** Permanganate waste, salt residue, blast dust disposal.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- DUAL RINSE PATHS / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Left -- Post-Mechanical path | Right -- Post-Chemical path
  Block C: Molten salt quench callout

ZONE 3 -- RINSE QUALITY MONITORING (16.0"--22.0" / ~6.0" tall)
  Block D: Rinse monitoring table (pH, conductivity, visual)

ZONE 4 -- WASTE & DISPOSAL CONSIDERATIONS (22.0"--28.5" / ~6.5" tall)
  Block E: Waste handling for blast dust, permanganate, salt residue

ZONE 5 -- KEY RULES STRIP (28.5"--32.5" / ~4.0" tall)
  Block F: Four key post-descale rules

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE -- POST-DESCALE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two Paths: After Mechanical vs. After Chemical Descaling` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `No water rinse after blasting -- go straight to cleaning. After chemical descale, rinse thoroughly or contaminate everything downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Dual Rinse Paths (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> POST-DESCALE -- TWO DIFFERENT PATHS

---

**BLOCK B -- Left Path: After Mechanical Descaling**

Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 8.5", fill `#1E2435`, radius 8.
Left accent: 0.06" `#2EC4B6`.
Title: `AFTER MECHANICAL DESCALING` -- Barlow SemiBold, 20 pt, `#2EC4B6`.

Vertical flow inside (4 steps, top to bottom, each in a small rounded rect):

| Step | Text | Detail |
|---|---|---|
| 1 | BLOW OFF / VACUUM | Remove loose media and dust from part surface |
| 2 | ALKALINE CLEAN | Remove residual media dust, oils, and handling contamination |
| 3 | WATER RINSE | Standard flowing rinse after alkaline clean |
| 4 | PROCEED TO ACID PICKLE OR ACTIVATE | No direct water rinse after blasting -- go straight to cleaning |

Each step box: W: 10.0", H: 1.5", fill `#252B3D`, radius 4.
Step number: Barlow Condensed ExtraBold, 16 pt, `#2EC4B6`.
Text: Inter Medium, 14 pt, `#F0EDE8`.
Detail: Inter Regular, 12 pt, `#F0EDE8` at 70%.
Arrows between steps: 2 pt `#3A4055`, down-pointing.

Key callout below steps:
- Inter Medium, 13 pt, `#E8A020`
- `NOTE: No water rinse directly after blasting. Water causes flash rust. Proceed to alkaline clean.`

---

**Right Path: After Chemical Descaling**

Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 8.5", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E8A020`.
Title: `AFTER CHEMICAL DESCALING` -- Barlow SemiBold, 20 pt, `#E8A020`.

Vertical flow inside:

| Step | Text | Detail |
|---|---|---|
| 1 | THOROUGH WATER RINSE | Flowing water; remove all chemical residue |
| 2 | CHECK FOR RESIDUAL STAINING | Permanganate leaves purple stain if rinse is insufficient |
| 3 | ACID PICKLE (if required) | Dissolve conditioned oxide layer; see Clusters 3/4 |
| 4 | FINAL RINSE | pH < 9.0; conductivity < 200 uS/cm |

Same step box styling as left path, with `#E8A020` step number color.

Key callout:
- Inter Medium, 13 pt, `#E8A020`
- `Alkaline permanganate residue is purple -- if you see purple on the part, you have not rinsed enough.`

---

**BLOCK C -- Molten Salt Quench Callout**

Y: 12.8" to 15.8". Full-width callout box.

Rounded rect, X: 0.5", W: 23.0", H: 2.8", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

Title: `MOLTEN SALT: THE QUENCH IS THE FIRST "RINSE"` -- Barlow SemiBold, 18 pt, `#E05C5C`.

Three-column content inside:

| Column | Label | Content |
|---|---|---|
| 1 | QUENCH | Remove from salt bath --> immerse in water. Violent steam generation is normal. Ensure adequate tank volume and ventilation. |
| 2 | ACID DIP | After quench: dilute H2SO4 or HCl to dissolve residual salt film and thin oxide. |
| 3 | FINAL RINSE | Thorough flowing water rinse to remove all acid and salt residue. |

DANGER note (bottom of callout):
- `STAND CLEAR during quench. Steam eruption is violent. Use long-handled tongs. Face shield and heat-resistant gloves mandatory.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 3 -- Rinse Quality Monitoring

**Section label:** Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> RINSE QUALITY -- HOW TO KNOW YOU ARE CLEAN

---

**BLOCK D -- Monitoring Table**

Y: 16.9" to 21.8". Full-width table.

Column widths: Parameter (5.0") | Method (6.0") | Target (5.0") | Applies After (7.0")

Header: `#3A4055` fill. Barlow SemiBold 14 pt.

| Parameter | Method | Target | Applies After |
|---|---|---|---|
| Rinse pH | pH paper or meter | < 9.0 (alkaline) or < 3.0 (acid) depending on prior step | Alkaline perm or acid pickle |
| Conductivity | Conductivity meter | < 200 uS/cm | All chemical descaling rinses |
| Visual -- purple stain | Visual inspection | No purple discoloration | Alkaline permanganate only |
| Visual -- salt residue | Visual + wipe test | No white crystalline residue | Molten salt quench |
| Water break test | After subsequent alk clean | Complete water film, no beading | After blast + alk clean sequence |
| Cellophane tape test | Tape press + peel | No media particles or dust on tape | After mechanical blast + blowoff |

Data: JetBrains Mono Regular 12 pt. Labels: Inter Medium 13 pt.

---

### ZONE 4 -- Waste & Disposal

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WASTE HANDLING -- DESCALING BYPRODUCTS

---

**BLOCK E -- Three Waste Category Cards**

Y: 22.9" to 28.3". Three side-by-side callout boxes.

| Card | X | W | Accent | Title | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `#2EC4B6` | BLAST MEDIA DUST | Spent media + scale dust. May contain heavy metals (Pb, Cr). Characterize per RCRA before disposal. Enclosed dust collection required. |
| 2 | 8.17" | 7.33" | `#E8A020` | PERMANGANATE WASTE | Spent KMnO4 bath + rinse water. Contains dissolved Cr (chromates). Treat as Cr-bearing waste. Reduce Cr(VI) before discharge. |
| 3 | 15.83" | 7.67" | `#E05C5C` | MOLTEN SALT WASTE | Spent salt bath (NaOH/NaH). Strongly alkaline. Neutralize before disposal. Contaminated with dissolved metals. |

Each card: Rounded rect, H: 5.0", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold 16 pt, accent color. Content: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Key Rules Strip

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> FOUR POST-DESCALE RULES

**BLOCK F -- Four Rule Cards**

Y: 29.4" to 32.3".

| Card | X | Rule | Detail |
|---|---|---|---|
| 1 | 0.5" | NO WATER AFTER BLAST | Go to alkaline clean first. Water on freshly blasted steel = flash rust. |
| 2 | 6.33" | RINSE UNTIL CLEAR | Permanganate is purple. If you see purple, keep rinsing. |
| 3 | 12.16" | PROCESS WITHIN 4 HOURS | Freshly descaled steel re-oxidizes fast. Shorter in humid environments. |
| 4 | 18.0" | CLEAN GLOVES ONLY | Bare-hand contact after descaling = fingerprint contamination = adhesion failure. |

Per card: Rounded rect W: 5.5", H: 2.7", fill `#1E2435`, left accent 0.06" `#27AE60`.
Rule: Barlow SemiBold 15 pt `#27AE60`. Detail: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Rinse -- Post-Descale`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Descale -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-path hero is essential because the post-blast and post-chemical paths are fundamentally different -- one does NOT get a water rinse, the other absolutely does. This is a common source of confusion on shop floors where both mechanical and chemical descaling are happening. The molten salt quench callout in coral at the center of the poster draws the eye to the most dangerous rinse step in the entire series.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #375 -- Construction Workup v1.0*
*2026-04-26*
