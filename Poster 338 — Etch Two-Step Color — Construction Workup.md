---
Project: Plating Posters Inc
Poster Number: 338
Title: "Caustic Etch -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color, Section 8.2--8.6)"
  - "Anodizing Clusters -- Watson Research Brief (Process 1: Type II, Section 1.4)"
Technical Source: Standard caustic etch (NaOH) per Type II process. Produces uniform matte texture critical for consistent color in two-step electrolytic coloring. Etch uniformity is THE most important pre-treatment variable for color consistency.
Process Scope: Two-step color anodizing -- Stage 3 of 8 (Caustic Etch)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Etch
  - CausticEtch
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #338 -- Construction Workup
## Caustic Etch -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. The caustic etch dissolves a thin layer of aluminum to produce a uniform matte (satin) texture. In two-step color anodizing, etch uniformity is THE most critical pre-treatment variable because variations in etch depth translate directly to variations in oxide thickness, which translate to variations in pore depth, which translate to uneven metal deposition and color variation. The brief calls for tight controls: +/- 15 sec time, +/- 1 C temperature.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- ETCH PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS + DISSOLVED AL (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- SMUT FORMATION + ETCH CONTROL FOR COLOR (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CAUSTIC ETCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color -- Stage 3 of 8` -- 34 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Etch uniformity IS color uniformity. Every second of etch time and every degree of temperature shows up in the final color.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean aluminum with native oxide --> After: Uniform matte texture, ready for desmut`

---

### ZONE 3 -- Etch Process Hero

**Section label:** `CAUSTIC ETCH -- THE TEXTURE THAT DEFINES THE COLOR` -- Y: 4.4".

**BLOCK B -- Etch Tank + Role Diagram**

Y: 5.0" to 14.0". Full-width panel, fill `#1E2435`.

**Left half -- Tank Cross-Section (X: 1.0", W: 11.0"):**

Tank body: Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`.
Parts on rack: vertical rects, fill `#C8D0D8` at 40%.
Heater: zigzag at bottom.

Bath parameters:
- `NaOH 40--80 g/L (4--8 oz/gal free)` JetBrains Mono 14 pt `#E8A020`
- `130--150 F (55--65 C)` JetBrains Mono 14 pt `#E8A020`
- `1--5 min (CRITICAL: +/- 15 sec for color)` JetBrains Mono 14 pt `#E05C5C`
- `Dissolved Al: control at 25--50 g/L` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Right half -- The Four Roles of Etch:**

Title: `WHAT THE ETCH DOES` Barlow SemiBold 16 pt `#E8A020`

Four vertically stacked mini-cards:

| Role | Description |
|---|---|
| `1. TEXTURE` | Produces uniform matte/satin finish by leveling micro-roughness |
| `2. DEFECT REMOVAL` | Removes scratches, die lines, handling marks |
| `3. ALLOY HOMOGENIZATION` | Dissolves surface-segregated alloying elements |
| `4. OXIDE REMOVAL` | Strips native oxide for fresh aluminum surface |

Each role: Barlow SemiBold 14 pt `#E8A020`, description Inter Regular 13 pt `#F0EDE8`.

**Bottom callout (Y: 13.5"):**
- `FOR COLOR MATCHING: Use the SAME etch time, temperature, and NaOH concentration for every batch. Color consistency requires process consistency -- no shortcuts.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Operating Parameters

**Section label:** `OPERATING WINDOW` -- Y: 14.7".

**Two-column layout:**

**Left -- Parameters (X: 0.5", W: 11.0"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

| Parameter | Value | Two-Step Tolerance |
|---|---|---|
| Chemical | NaOH (caustic soda) | -- |
| Free NaOH | 40--80 g/L (4--8 oz/gal) | +/- 5 g/L |
| Temperature | 130--150 F (55--65 C) | +/- 1 C (2 F) |
| Time | 1--5 min | +/- 15 sec |
| Dissolved Al | 25--50 g/L | Control for stable etch rate |
| Etch rate | ~0.001 in/surface/min at 140 F | Alloy-dependent |

Note: "Two-Step Tolerance" column shows the TIGHT control needed for color matching.

**Right -- Dissolved Aluminum Management:**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".
Title: `DISSOLVED ALUMINUM -- THE HIDDEN VARIABLE` Barlow SemiBold 18 pt `#2EC4B6`

Body:
> As aluminum dissolves in the etch bath, it accumulates as sodium aluminate. This changes the etch rate:
>
> -- Fresh bath (low Al): fast, aggressive etch
> -- Working bath (25--50 g/L Al): stable, predictable etch
> -- Exhausted bath (>60 g/L Al): sluggish, uneven etch
>
> For color consistency, maintain dissolved Al in the 25--50 g/L working range. Decant or replace when etch rate becomes inconsistent.

---

### ZONE 5 -- Failure Modes

**Section label:** `WHAT GOES WRONG` -- Y: 20.7".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | COLOR VARIATION | `#E05C5C` | Etch time/temp inconsistent | Tighten to +/- 15 sec, +/- 1 C |
| R1C2 | HEAVY SMUT | `#E8A020` | Over-etching on high-Cu/Si alloys | Reduce etch time; improve desmut |
| R1C3 | PITTING | `#E05C5C` | Over-etch on sensitive alloys | Reduce time; lower temperature |
| R2C1 | STREAKING | `#E8A020` | Uneven immersion or poor agitation | Consistent racking; improve agitation |
| R2C2 | DIMENSIONAL LOSS | `#2EC4B6` | Excessive etch on thin-wall parts | Reduce etch time; verify tolerance |
| R2C3 | BANDING (COLOR) | `#E05C5C` | Bath stratification (temp layers) | Improve tank agitation |

---

### ZONE 6 -- Smut Formation + Color Control

**Two-column layout:**

**Left -- Smut Formation:**
Title: `SMUT FORMATION BY ALLOY` Barlow SemiBold 18 pt `#E8A020`

| Alloy | Smut Character | Desmut Needed |
|---|---|---|
| 6063 | Light gray -- easy | Standard HNO3 |
| 6061 | Light gray | Standard HNO3 |
| 5052 | Light | Standard HNO3 |
| 2024 | Heavy dark Cu smut | HNO3 + HF |
| 7075 | Moderate Cu/Zn | HNO3 + HF |
| Cast (A356) | Heavy Si smut | HNO3 + HF (extended) |

Note: `6063 is the standard two-step color alloy. Alloy selection is critical for color consistency.` Inter Regular 12 pt `#27AE60`.

**Right -- Etch Control for Color Matching:**
Title: `ETCH CONTROL FOR AAMA 611 COLOR` Barlow SemiBold 18 pt `#27AE60`

Body:
> AAMA 611 requires color match within dE < 1.0 for architectural anodizing. This tight tolerance demands:
>
> -- Same alloy lot (same extrusion heat)
> -- Same etch time (+/- 15 sec)
> -- Same etch temperature (+/- 1 C)
> -- Consistent dissolved Al in etch bath
> -- Same racking position and load density
>
> Two-step color anodizers who achieve consistent color matching are the ones who treat the etch bath like a precision instrument.

---

### ZONE 7 -- Footer

Standard. Title: `Caustic Etch -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; AAMA 611; typical caustic etch parameters for Type II sulfuric acid anodize pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Two-Step Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The central message: etch uniformity IS color uniformity. The tolerance callouts (+/- 15 sec, +/- 1 C) are the most actionable items on the poster. The dissolved aluminum management section educates operators on the hidden variable that most shops overlook. For two-step architectural color, the etch bath is the precision instrument that determines whether the building facade looks uniform or blotchy.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #338 -- Construction Workup v1.0*
*2026-04-26*
