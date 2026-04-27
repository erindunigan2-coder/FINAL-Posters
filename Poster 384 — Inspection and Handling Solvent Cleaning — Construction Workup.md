---
Project: Plating Posters Inc
Poster Number: 384
Title: "Inspection & Handling -- Solvent Cleaning Quality Verification"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: Industry-standard inspection methods for solvent-cleaned parts -- UV fluorescence, visual inspection, and handling protocols. Water break test applicability and limitations after solvent cleaning. Per ASM Handbook Vol. 5 and general industry knowledge.
Process Scope: Inspection and handling after solvent cleaning -- UV fluorescence, visual criteria, clean handling, and common surface defects from improper cleaning
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - Inspection
  - Handling
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #384 -- Construction Workup
## Inspection & Handling -- Solvent Cleaning Quality Verification

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Inspection after solvent cleaning has a unique twist: the water break test does not directly apply. Parts exiting a solvent clean may not be wetted with water at this stage (they are transitioning to aqueous processing via alkaline soak clean). The primary inspection tool is UV fluorescence -- many oils and greases fluoresce under UV/blacklight, so absence of fluorescence is a strong indicator of cleanliness. This poster covers UV inspection, visual criteria, clean handling, and the defect consequences of improper solvent cleaning.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **UV fluorescence hero (Block B -- HERO):** A large callout explaining UV inspection as the primary cleanliness verification after solvent cleaning.

2. **Visual inspection criteria panel (Block C):** What to look for -- no visible oil, no solvent residue, no haze or staining.

3. **Clean handling requirements (Block D):** Glove type, ventilation, stacking prohibition.

4. **Defect consequences table (Block E):** What happens downstream when solvent cleaning fails.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- UV FLUORESCENCE HERO + VISUAL CRITERIA (2.9"--14.5" / ~11.6" tall)
  Block B: UV fluorescence inspection callout
  Block C: Visual inspection criteria

ZONE 3 -- CLEAN HANDLING (14.5"--21.5" / ~7.0" tall)
  Block D: Handling requirements (4 rules)

ZONE 4 -- DEFECT CONSEQUENCES (21.5"--28.5" / ~7.0" tall)
  Block E: What goes wrong when solvent cleaning fails

ZONE 5 -- WATER BREAK TEST NOTE (28.5"--32.5" / ~4.0" tall)
  Block F: Water break test applicability after solvent clean

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Quality Verification After Solvent Cleaning` -- 32 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `The water break test does not apply here. Your primary tool is UV fluorescence -- if it glows, it is not clean. If the surface is haze-free and residue-free, you are ready for the alkaline handoff.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- UV Fluorescence Hero + Visual Criteria

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> VERIFYING CLEANLINESS -- UV FLUORESCENCE AND VISUAL

---

**BLOCK B -- UV Fluorescence Inspection Hero**

Y: 3.8" to 9.0". Full width.

Rounded rect, X: 0.5", W: 23.0", H: 5.0", fill `#1E2435`, radius 8.
Left accent: 0.06" `#27AE60`.

**Two-column interior:**

*Left -- The Method (W: 11.0"):*
- Title: `UV FLUORESCENCE INSPECTION` Barlow SemiBold 22 pt `#27AE60`
- Body: Inter Regular 14 pt `#F0EDE8`:

```
Many oils and greases fluoresce under
ultraviolet / blacklight illumination.
Fluorescence = organic contamination present.

Method:
  1. Darken the inspection area
  2. Illuminate part with UV lamp (365 nm)
  3. Inspect all surfaces
  4. PASS: no fluorescence visible
  5. FAIL: any fluorescent glow = soil remains

This is the FASTEST and MOST SENSITIVE
quick-check for residual organic contamination.
```

*Right -- Limitations (W: 11.0"):*
- Title: `LIMITATIONS TO KNOW` Barlow SemiBold 18 pt `#E8A020`
- Body: Inter Regular 14 pt `#F0EDE8`:

```
Not all oils fluoresce:
  - Synthetic coolants: some do not
  - Silicone: often non-fluorescent
  - Mineral spirits residue: may not fluoresce

UV fluorescence confirms contamination is
PRESENT -- absence of fluorescence does not
guarantee the surface is perfectly clean.

Use UV as a screening tool, not a final
certification. Final certification occurs
after the aqueous water break test.
```

**Callout strip (Y: 9.2"):**
- Rounded rect, full width, H: 0.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `UV fluorescence is a SCREENING tool. The definitive cleanliness test (water break per ASTM F22) is performed after the aqueous cleaning step, not after solvent cleaning.` Inter Medium 13 pt `#E8A020`

---

**BLOCK C -- Visual Inspection Criteria**

Y: 10.0" to 14.3". Full width.

Section sublabel: `VISUAL CRITERIA -- WHAT TO LOOK FOR` Barlow SemiBold 18 pt `#F0EDE8`. Y: 10.0".

Four criteria cards in a row. Each: Rounded rect, W: 5.5", H: 3.5", fill `#1E2435`, radius 6, top accent 3 pt.

| Card | X | Criterion | Pass Condition | Fail Condition | Accent |
|---|---|---|---|---|---|
| 1 | 0.5" | Oil / Grease | No visible oil sheen, no iridescence | Oil film visible, rainbow sheen | `#27AE60` |
| 2 | 6.33" | Solvent Residue | Clean, dry surface; no white haze | White haze or staining (decomposition products or moisture) | `#E8A020` |
| 3 | 12.16" | Particulate | No embedded particles or fibers | Visible lint, metal fines, or debris | `#2EC4B6` |
| 4 | 18.0" | Surface Condition | No etching, discoloration, or attack | Discoloration or material attack from wrong solvent | `#E05C5C` |

Per card:
- Criterion: Barlow SemiBold 15 pt, accent color
- Pass: Inter Regular 12 pt `#27AE60`
- Fail: Inter Regular 12 pt `#E05C5C`

---

### ZONE 3 -- Clean Handling

**Section label:** Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> CLEAN HANDLING -- FOUR RULES

---

**BLOCK D -- Four Handling Rules**

Y: 15.4" to 21.3". Four tall cards in a row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06".

| Card | X | Rule | Detail | Accent |
|---|---|---|---|---|
| 1 | 0.5" | WEAR CLEAN GLOVES | Nitrile preferred (lint-free). Cotton gloves absorb solvent vapor. Never touch solvent-cleaned parts with bare hands -- fingerprints = immediate recontamination. | `#27AE60` |
| 2 | 6.33" | VENTILATED AREA | Handle in well-ventilated space. Residual solvent vapor continues to off-gas from part surfaces and from gloves. Do not work in enclosed area without ventilation. | `#E8A020` |
| 3 | 12.16" | DO NOT STACK | Do not stack or nest parts after solvent cleaning. Stacking traps solvent vapor between surfaces, creating contaminated pools. Use drying racks with separation. | `#E05C5C` |
| 4 | 18.0" | MINIMIZE DWELL TIME | Transfer to alkaline soak clean promptly. Cleaned parts begin to oxidize and attract airborne contaminants. Target: transfer within 30 minutes. | `#2EC4B6` |

Per card:
- Rule: Barlow SemiBold 16 pt, accent color
- Detail: Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Defect Consequences

**Section label:** Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHEN SOLVENT CLEANING FAILS -- DOWNSTREAM DEFECTS

---

**BLOCK E -- Defect Table**

Y: 22.4" to 28.3". Column widths (23.0" total):
- Defect (5.0") | Cause (7.0") | Where It Shows Up (6.0") | Prevention (5.0")

Header row: fill `#3A4055`, H: 0.5".

| Defect | Cause | Where It Shows Up | Prevention |
|---|---|---|---|
| Blistering after plating | Residual grease or wax trapped under plating deposit | After plating -- adhesion failure | Complete soil dissolution; adequate contact time |
| Skip plating (bare spots) | Organic film preventing proper acid activation and plating | At the plating tank -- non-wetting areas | UV inspection; adequate alkaline clean after solvent |
| Rough deposit | Embedded particles (abrasive, metal fines) not removed | After plating -- gritty texture | Proper fixturing; clean solvent; filter bath |
| Staining / discoloration | Solvent decomposition products redepositing on surface | After solvent clean -- visible before plating | Monitor solvent health (AA test); replace when decomposed |
| White haze | Moisture in chlorinated solvent; incomplete evaporation | After solvent clean -- visible before plating | Maintain water separator; adequate evaporation time |

Data: Inter Regular 12 pt. Defect names: Barlow SemiBold 13 pt `#E05C5C`.

---

### ZONE 5 -- Water Break Test Note

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> ABOUT THE WATER BREAK TEST

---

**BLOCK F -- Water Break Test Applicability**

Y: 29.3" to 32.3". Full width callout.

Rounded rect, X: 0.5", W: 23.0", H: 2.7", fill `#1E2435`, radius 6.
Left accent: 0.06" `#E8A020`.
Border: 1 pt `#E8A020` at 30%.

**Two-column interior:**

*Left -- After Solvent Clean (W: 11.0"):*
- Title: `AFTER SOLVENT CLEAN` Barlow SemiBold 16 pt `#E8A020`
- Body: Inter Regular 13 pt `#F0EDE8`:

```
NOT directly applicable.
Parts are not wetted with water at this stage.
Use UV fluorescence and visual inspection.
```

*Right -- After Alkaline Clean (W: 11.0"):*
- Title: `AFTER ALKALINE CLEAN (DOWNSTREAM)` Barlow SemiBold 16 pt `#27AE60`
- Body: Inter Regular 13 pt `#F0EDE8`:

```
The water break test (ASTM F22) IS performed
after the alkaline soak clean and rinse --
this is the definitive cleanliness gate.
Water must sheet uniformly for 30 seconds.
Any break = organic contamination remains.
```

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & Handling -- Solvent Cleaning Quality Verification`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Inspection methods and handling practices shown are typical for solvent-cleaned parts. Specific cleanliness verification requirements vary by application and downstream process specification. UV fluorescence is a screening tool -- final certification should follow applicable standards (e.g., ASTM F22 after aqueous cleaning). Consult your process specification for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Solvent Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The UV fluorescence hero is the visual centerpiece -- it is both the most useful inspection technique after solvent cleaning AND the most visually interesting concept (parts glowing under blacklight). The honest limitation callout ("not all oils fluoresce") earns credibility with experienced operators who would immediately question a blanket claim. The water break test note in Zone 5 is deliberately placed as a bridge to the downstream aqueous process -- it reinforces that solvent cleaning is a step in a sequence, not a standalone endpoint for plating applications.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #384 -- Construction Workup v1.0*
*2026-04-26*
