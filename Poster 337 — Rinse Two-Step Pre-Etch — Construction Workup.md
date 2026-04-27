---
Project: Plating Posters Inc
Poster Number: 337
Title: "Rinse (Pre-Etch) -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color, Section 8.2)"
Technical Source: Standard pre-etch rinse. Removes alkaline cleaner before caustic etch. Prevents contamination of etch tank. Same parameters as all anodizing pre-etch rinses.
Process Scope: Two-step color anodizing -- Stage 2 of 8 (Rinse, Pre-Etch)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Rinse
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #337 -- Construction Workup
## Rinse (Pre-Etch) -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. Standard pre-etch rinse -- removes alkaline cleaner residue before the caustic etch tank. Cleaner drag-in raises etch bath pH and depletes free caustic, leading to uneven etch rates. In two-step color anodizing, uneven etch translates directly to uneven color.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + WATER QUALITY (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- DRAG-OUT + WATER CONSERVATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color -- Pre-Etch -- Stage 2 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Alkaline drag-in depletes the etch bath. Depleted etch means uneven texture. Uneven texture means uneven color.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts with alkaline cleaner residue --> After: pH-neutral surface ready for caustic etch`

---

### ZONE 3 -- Rinse Process Hero

**Section label:** `THE PRE-ETCH RINSE` -- Y: 4.4".

**BLOCK B -- Full-Width Panel**

Y: 5.0" to 14.0". Rounded rect, X: 0.5", W: 23.0", H: 8.5", fill `#1E2435`, radius 8.

**Left half -- Tank + Parameters:**

Tank cross-section with parts, cascade flow indicators.
- `Flowing ambient water` JetBrains Mono 14 pt `#2EC4B6`
- `60--85 F (15--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`
- `Counter-flow cascade preferred` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Right half -- Why This Matters for Color:**

Title: `THE COLOR CONNECTION` Barlow SemiBold 16 pt `#E8A020`

Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):
> Alkaline cleaner carried into the etch tank:
>
> -- Raises etch bath pH -- reduces etch rate
> -- Creates localized pH variations -- uneven etch
> -- Uneven etch = non-uniform matte texture
> -- Non-uniform texture = inconsistent oxide growth in anodize
> -- Inconsistent oxide = uneven pore depth
> -- Uneven pore depth = patchy color in the electrolytic coloring step
>
> This rinse breaks the contamination chain.

**Bottom callout (Y: 13.5"):**
- `Conductivity target: < 200 uS/cm for commercial; < 50 uS/cm for critical architectural color match.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Rinse Parameters

**Section label:** `OPERATING PARAMETERS` -- Y: 14.7".

**Two-column layout:**

**Left -- Parameters:**
| Parameter | Value |
|---|---|
| Water type | City or DI water |
| Temperature | Ambient (60--85 F) |
| Time | 30--60 sec |
| Flow | Counter-flow cascade preferred |
| Conductivity | < 200 uS/cm commercial; < 50 uS/cm critical |

**Right -- Verification:**
- `pH paper: rinse water should match supply (6--8)`
- `No foam or soap residue on surface`
- `No slippery feel on parts`
- `Conductivity meter for quantitative check`

---

### ZONE 5 -- Failure Modes

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | UNEVEN ETCH | `#E05C5C` | Alkaline drag-in to etch | Improve rinse; add cascade |
| R1C2 | COLOR BANDING | `#E05C5C` | Etch variation from contamination | Trace back to rinse quality |
| R1C3 | ETCH BATH DEPLETION | `#E8A020` | Excessive cleaner drag-in | Better drain time; cascade |
| R2C1 | STREAKING | `#E8A020` | Uneven rinsing | Increase agitation |
| R2C2 | FOAM IN ETCH | `#2EC4B6` | Surfactant drag-in | Longer drain over cleaner |
| R2C3 | WATER SPOTS | `#2EC4B6` | Hard water minerals | DI water for final rinse |

---

### ZONE 6 -- Drag-Out + Conservation

**Two-column layout:**

**Left -- Drag-Out Reduction:**
- `Dwell 10--15 sec over cleaner tank to drain`
- `Orient parts for maximum drainage`
- `Slower withdrawal = less drag-out`

**Right -- Cascade Design:**
- `Counter-flow: fresh water enters last tank, overflows backward`
- `2-stage cascade: 80--90% water savings`
- `Monitor conductivity at each stage`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Etch) -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; typical rinse parameters for aluminum anodize pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Two-Step Pre-Etch -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "color connection" panel in Zone 3 is the key differentiator from standard rinse posters. It traces the full contamination chain from cleaner drag-in through six cause-effect steps to patchy color in the final product. This multi-step consequence chain is uniquely visible in two-step color anodizing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #337 -- Construction Workup v1.0*
*2026-04-26*
