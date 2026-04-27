---
Project: Plating Posters Inc
Poster Number: 323
Title: "Desmut -- Bright Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 6: Bright Anodizing, Section 6.4)"
Technical Source: Desmut after bright dip -- often unnecessary for bright anodize alloys (1xxx, 5xxx) because the bright dip itself removes smut-forming elements. On alloys with copper or silicon, a brief nitric acid desmut may follow the bright dip.
Process Scope: Bright anodizing -- Stage 4 of 8 (Desmut)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - BrightAnodizing
  - Desmut
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #323 -- Construction Workup
## Desmut -- Bright Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. Unlike standard anodize pre-treatment where desmut is always required after caustic etch, the bright dip process often makes desmut unnecessary. On most bright alloys (1xxx, 5xxx), the phosphoric/nitric acid bright dip dissolves smut-forming elements. Desmut is only needed when processing copper- or silicon-bearing alloys. This poster explains when desmut is needed, when it can be skipped, and how to do it without damaging the bright-dipped surface.

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
  Stage 4 highlighted (Amber)
ZONE 3 -- DESMUT DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- ALLOY-SPECIFIC GUIDANCE (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DESMUT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Bright Anodizing -- Stage 4 of 8 (Conditional)` -- 34 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Most bright alloys skip this step. The bright dip already does the work. But on copper or silicon alloys, desmut protects the mirror.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Bright-dipped surface (may have light smut on Cu/Si alloys) --> After: Smut-free, specular surface ready for anodize`

---

### ZONE 3 -- Desmut Decision Tree Hero

**Section label:** `DO YOU NEED TO DESMUT?` -- Y: 4.4".

**BLOCK B -- Decision Flowchart**

Y: 5.0" to 14.0". Full-width panel.

Rounded rect, X: 0.5", Y: 5.0", W: 23.0", H: 8.5", fill `#1E2435`, radius 8.

**Decision tree (built with rectangles and arrows):**

*Start box (top center):*
- `WHAT ALLOY?` Barlow SemiBold 20 pt `#F0EDE8`
- Rounded rect, fill `#3A4055`, W: 8.0", H: 1.2"

*Branch Left -- Pure/Low-Alloy (X: 2.0"):*
- Arrow down from start
- `1xxx, 5xxx, 6xxx (low Cu)` JetBrains Mono 14 pt `#27AE60`
- `SKIP DESMUT` Barlow SemiBold 22 pt `#27AE60`
- `Bright dip removes smut-forming elements` Inter Regular 13 pt `#F0EDE8`
- `Proceed directly to rinse` Inter Medium 13 pt `#27AE60`
- Green-accented result box, fill `#27AE60` at 10%, border 1 pt `#27AE60`

*Branch Right -- Cu/Si Alloys (X: 14.0"):*
- Arrow down from start
- `2xxx, 7xxx, Cast (high Cu/Si)` JetBrains Mono 14 pt `#E05C5C`
- `DESMUT REQUIRED` Barlow SemiBold 22 pt `#E05C5C`
- `Cu/Si smut remains after bright dip` Inter Regular 13 pt `#F0EDE8`
- `Brief HNO3 desmut: 30--60 sec` Inter Medium 13 pt `#E8A020`
- Coral-accented result box, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`

**Bottom callout (Y: 13.0"):**
- `NOTE: Even when desmut is needed, keep it brief (30--60 sec). Extended desmut can attack the bright-dipped surface and reduce reflectivity.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Operating Parameters

**Section label:** `DESMUT PARAMETERS (WHEN REQUIRED)` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Parameters (X: 0.5", W: 11.0"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".
Title: `DESMUT OPERATING WINDOW` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Chemistry | Nitric acid (HNO3) |
| Concentration | 25--50% v/v |
| Temperature | Ambient (60--85 F / 15--30 C) |
| Time | 30--60 sec (BRIEF) |
| Agitation | Mild |

Note: `Do NOT use HF-bearing desmuts on bright-dipped surfaces -- HF attacks the polished surface and destroys reflectivity.` Inter Medium 13 pt `#E05C5C`.

**Right -- Why Brief? (X: 12.0", W: 11.5"):**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".
Title: `PROTECTING THE MIRROR` Barlow SemiBold 18 pt `#2EC4B6`

Body:
> The bright-dipped surface is chemically polished to nanometer-scale smoothness. Extended acid exposure (even mild HNO3) begins to micro-etch the surface, reducing specular reflectivity.
>
> Rule: minimum effective time. Get the smut off and get out.
>
> If the alloy requires aggressive desmut (HNO3 + HF for cast), bright anodizing is probably not the right process for that alloy.

---

### ZONE 5 -- Failure Modes

**Section label:** `WHAT GOES WRONG` -- Y: 20.7".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SMUT UNDER OXIDE | `#E05C5C` | Skipped desmut on Cu/Si alloy | Add desmut step for that alloy |
| R1C2 | REDUCED REFLECTIVITY | `#E8A020` | Desmut too long or too aggressive | Reduce time; eliminate HF |
| R1C3 | UNEVEN COLOR AFTER DYE | `#E05C5C` | Residual smut under oxide | Desmut before anodize |
| R2C1 | PITTING | `#E05C5C` | Chloride in desmut acid | Use reagent-grade HNO3 |
| R2C2 | STAINING | `#E8A020` | Cu enrichment on surface from desmut | Shorter desmut; immediate rinse |
| R2C3 | NO DEFECT (MOST ALLOYS) | `#27AE60` | Bright alloys don't need desmut | Correct -- skip for 1xxx/5xxx |

---

### ZONE 6 -- Alloy-Specific Guidance

**Section label:** `ALLOY DECISION GUIDE` -- Y: 26.7".

**Full-width table (Y: 27.3" to 32.3"):**

| Alloy | Smut After Bright Dip | Desmut Needed? | Recommended Desmut | Notes |
|---|---|---|---|---|
| 1100 | None | NO | Skip | Pure Al -- no smut-forming elements |
| 5657 | None | NO | Skip | Dedicated bright alloy |
| 5252 | Trace | NO | Skip | Negligible smut |
| 6463 | Trace | NO | Skip | Bright architectural alloy |
| 6061 | Light | SOMETIMES | HNO3 30 sec | Minor Mg/Si smut possible |
| 2024 | Heavy Cu smut | YES | HNO3 50%, 60 sec | But 2024 is a poor bright dip alloy |
| 7075 | Moderate Cu/Zn | YES | HNO3 50%, 60 sec | Poor bright dip alloy |
| Cast (A356) | Heavy Si smut | YES | HNO3 + HF (NOT recommended for bright) | Cast alloys are unsuitable for bright anodize |

"NO" in `#27AE60`. "YES" in `#E05C5C`. "SOMETIMES" in `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Desmut -- Bright Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; typical desmut parameters for bright anodize pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Desmut Bright Anodizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The decision tree hero is unique to this poster -- no other desmut poster in the series has a "skip this step" path. This reflects the reality that most bright anodize work uses pure or low-alloy aluminum that doesn't generate smut. The alloy compatibility table in Zone 6 reinforces which alloys should and should not be bright-dipped in the first place.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #323 -- Construction Workup v1.0*
*2026-04-26*
