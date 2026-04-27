---
Project: Plating Posters Inc
Poster Number: 340
Title: "Desmut -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color)"
  - "Anodizing Clusters -- Watson Research Brief (Process 1: Type II, Section 1.5)"
Technical Source: Standard deoxidize/desmut step. Removes insoluble smut (Cu, Fe, Si residues) left by caustic etch. HNO3-based for 6063; HNO3+HF for high-Cu/Si alloys. Complete smut removal is essential for uniform oxide growth and consistent electrolytic color.
Process Scope: Two-step color anodizing -- Stage 5 of 8 (Desmut / Deoxidize)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Desmut
  - Deoxidize
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #340 -- Construction Workup
## Desmut -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The desmut step removes the dark residue (smut) left by caustic etching. Smut consists of insoluble alloying elements (Cu, Fe, Si, Mn, Zn) that were not dissolved by the NaOH etch. For two-step color, residual smut is a color killer -- it creates non-uniform oxide thickness and uneven metal deposition in the coloring bath. On 6063 (the standard architectural alloy), standard HNO3 desmut works well.

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
  Stage 5 highlighted (Amber)
ZONE 3 -- DESMUT PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DESMUT OPTIONS + ALLOY GUIDE (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- SAFETY + BATH CONTROL (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DESMUT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color -- Deoxidize -- Stage 5 of 8` -- 34 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Smut under the oxide is a color defect waiting to happen. What you cannot see after desmut, you will see after coloring.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Etched surface with dark smut residue --> After: Clean, bright, smut-free aluminum ready for anodize`

---

### ZONE 3 -- Desmut Process Hero

**Section label:** `DESMUT -- REMOVING THE ETCH RESIDUE` -- Y: 4.4".

**BLOCK B -- Full-Width Panel**

Y: 5.0" to 14.0". Rounded rect, X: 0.5", W: 23.0", H: 8.5", fill `#1E2435`.

**Left half -- Tank + Parameters (X: 1.0", W: 11.0"):**

Tank body: Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`.
Parts: fill `#C8D0D8` at 40%.

Bath parameters:
- `HNO3 25--50% v/v` JetBrains Mono 14 pt `#E8A020`
- `Ambient (60--85 F)` JetBrains Mono 14 pt `#F0EDE8`
- `30--120 sec` JetBrains Mono 14 pt `#F0EDE8`
- `Agitation: mild` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Right half -- What Smut Is:**

Title: `WHAT IS SMUT?` Barlow SemiBold 18 pt `#E8A020`

Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):
> When aluminum dissolves in caustic etch, the insoluble alloying elements remain on the surface:
>
> -- **Copper** (from 2xxx, 7xxx alloys): dark, tenacious smut
> -- **Silicon** (from cast, 4xxx alloys): gray-black gritty smut
> -- **Iron**: dark spots and inclusions
> -- **Manganese, Zinc**: contribute to overall smut film
>
> On 6063 (the workhorse two-step alloy), smut is light gray and easily removed with standard HNO3. On high-Cu or cast alloys, smut requires HNO3 + HF.

**Bottom callout (Y: 13.5"):**
- `A properly desmutted surface is bright, clean, and uniformly reflective (or uniformly matte if etched). Run your gloved finger across it -- it should feel smooth with no gritty residue.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Desmut Options + Alloy Guide

**Section label:** `DESMUT OPTIONS BY ALLOY` -- Y: 14.7".

**Two-column layout:**

**Left -- Desmut Chemistry Options (X: 0.5", W: 11.0"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

| Desmut Type | Composition | Temp | Time | Best For |
|---|---|---|---|---|
| Nitric acid | HNO3 25--50% v/v | Ambient | 15--60 sec | 6063, 5052, 6061 |
| Ferric sulfate + H2SO4 | 3--6 oz/gal Fe2(SO4)3 + 10--15% H2SO4 | 80--100 F | 2--10 min | Multi-alloy shops |
| Nitric + HF | HNO3 50% + HF 1--3% (48%) | Ambient | 15--60 sec | 2024, 7075, cast |
| Proprietary Cr-free | Per vendor TDS | Per TDS | Per TDS | Environmental compliance |

**Right -- Alloy-Specific Guidance (X: 12.0", W: 11.5"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `ALLOY-SPECIFIC RECOMMENDATIONS` Barlow SemiBold 18 pt `#27AE60`

| Alloy | Smut | Recommended | Notes |
|---|---|---|---|
| 6063 | Light gray | HNO3 50% | Standard -- gold standard alloy |
| 6061 | Light gray | HNO3 50% | Slightly more smut than 6063 |
| 5052 | Light | HNO3 50% | Easy desmut |
| 2024 | Heavy Cu smut | HNO3 + HF 1--3% | Straight HNO3 struggles |
| 7075 | Moderate Cu/Zn | HNO3 + HF | Preferred |
| Cast (A356) | Heavy Si | HNO3 + HF, extended | May need 2--3 min |

"Standard" in `#27AE60`. "HNO3 + HF" entries in `#E8A020`.

---

### ZONE 5 -- Failure Modes

**Section label:** `WHAT GOES WRONG` -- Y: 20.7".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SMUT UNDER OXIDE | `#E05C5C` | Incomplete desmut | Extend time; use stronger chemistry |
| R1C2 | COLOR VARIATION | `#E05C5C` | Residual smut disrupts oxide growth | Verify complete smut removal |
| R1C3 | PITTING | `#E05C5C` | Excessive HF concentration | Reduce HF to 1%; shorten time |
| R2C1 | OVER-ETCHING IN DESMUT | `#E8A020` | Too long in acid | Reduce time; monitor surface |
| R2C2 | STAINING | `#E8A020` | Copper re-deposition from desmut bath | Replace exhausted desmut bath |
| R2C3 | UNEVEN DESMUT | `#2EC4B6` | Poor agitation or racking | Improve agitation; consistent racking |

---

### ZONE 6 -- Safety + Bath Control

**Two-column layout:**

**Left -- Safety:**
Rounded rect, fill `#1E2435`, left accent `#E05C5C`.
Title: `SAFETY` Barlow SemiBold 18 pt `#E05C5C`

Body:
- `HNO3: strong oxidizing acid -- violent reaction with organic materials`
- `HF (if used): EXTREMELY DANGEROUS -- penetrating burns`
- `HF exposure: apply calcium gluconate gel IMMEDIATELY`
- `PPE: face shield, nitrile gloves (double-glove for HF), acid apron`
- `HF baths: calcium gluconate gel and eyewash MUST be within arm's reach`
- `Never mix HNO3 with organic solvents or reducing agents`

**Right -- Bath Maintenance:**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `BATH MAINTENANCE` Barlow SemiBold 18 pt `#2EC4B6`

Body:
- `Monitor HNO3 concentration by specific gravity or titration`
- `Dissolved metals accumulate -- replace when desmut slows`
- `Copper buildup causes staining on subsequent parts`
- `For two-step color: fresh desmut bath = consistent results`
- `Decant schedule: depends on production volume and alloy mix`

---

### ZONE 7 -- Footer

Standard. Title: `Desmut -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; typical desmut parameters. HF-bearing desmuts present serious safety hazards. Follow your facility SDS and EHS requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Desmut Two-Step Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "what is smut?" explanation is the key educational content -- many operators know to desmut but do not understand what smut actually is. The alloy-specific guidance table is the most actionable content. For two-step color, the connection between residual smut and color variation must be made explicit.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #340 -- Construction Workup v1.0*
*2026-04-26*
