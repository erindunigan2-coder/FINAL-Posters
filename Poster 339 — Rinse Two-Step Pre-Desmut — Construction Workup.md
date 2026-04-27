---
Project: Plating Posters Inc
Poster Number: 339
Title: "Rinse (Pre-Desmut) -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color)"
Technical Source: Standard post-etch rinse. Removes caustic (NaOH) before desmut. Prevents alkaline contamination of the acid desmut bath.
Process Scope: Two-step color anodizing -- Stage 4 of 8 (Rinse, Pre-Desmut)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Rinse
  - PreDesmut
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #339 -- Construction Workup
## Rinse (Pre-Desmut) -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This rinse removes caustic etch residue (NaOH + dissolved aluminum) before the acid desmut tank. NaOH drag-in neutralizes the desmut acid, reducing its effectiveness and allowing smut to remain on the surface. Residual smut under the anodic oxide causes non-uniform thickness and color variation in the electrolytic coloring step.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- CAUSTIC DRAG-OUT + CONTROL (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color -- Pre-Desmut -- Stage 4 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Caustic drag-in kills the desmut. Dead desmut leaves smut. Smut under the oxide means blotchy color.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Etched parts with caustic residue --> After: Caustic-free surface ready for acid desmut`

---

### ZONE 3 -- Rinse Process Hero

**Section label:** `THE POST-ETCH RINSE` -- Y: 4.4".

**BLOCK B -- Full-Width Panel**

Y: 5.0" to 14.0". Rounded rect, X: 0.5", W: 23.0", H: 8.5", fill `#1E2435`.

**Left half -- Tank + Parameters:**
- `Flowing ambient water` JetBrains Mono 14 pt `#2EC4B6`
- `60--85 F (15--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`
- `Counter-flow cascade preferred` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Right half -- Contamination Chain:**

Title: `NaOH DRAG-IN TO DESMUT -- THE PROBLEM` Barlow SemiBold 16 pt `#E05C5C`

Body:
> Caustic etch residue carried into the desmut bath:
>
> -- Neutralizes the HNO3 acid (NaOH + HNO3 -> NaNO3 + H2O)
> -- Raises desmut pH -- reduced smut removal effectiveness
> -- Leaves residual smut on the surface
> -- Smut under the anodic oxide disrupts uniform growth
> -- Non-uniform oxide = non-uniform pore depth = color variation
>
> This rinse is cheap insurance against expensive color defects.

**Bottom callout (Y: 13.5"):**
- `The etch bath is alkaline (pH 13+). The desmut bath is acid (pH <1). This rinse prevents a violent neutralization reaction at the bath boundary.` Inter Medium 14 pt `#E8A020`

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
| Conductivity | < 200 uS/cm commercial |

**Right -- Verification:**
- `pH paper: verify rinse water is pH 6--8 (not alkaline)`
- `No slimy/slippery feel on parts (indicates residual NaOH)`
- `Visual: etched matte surface visible; no gloss from residual caustic film`
- `Conductivity should approach supply water quality`

---

### ZONE 5 -- Failure Modes

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SMUT UNDER OXIDE | `#E05C5C` | NaOH neutralized the desmut | Improve rinse; add cascade |
| R1C2 | COLOR VARIATION | `#E05C5C` | Residual smut under oxide | Better rinse + desmut |
| R1C3 | DESMUT BATH DEPLETION | `#E8A020` | Excessive caustic drag-in | Longer drain time; cascade |
| R2C1 | ALKALINE STREAKS | `#E8A020` | Uneven rinsing | Improve agitation |
| R2C2 | WATER SPOTS | `#2EC4B6` | Hard water minerals | DI water |
| R2C3 | FOAMING IN DESMUT | `#2EC4B6` | Surfactant drag-in from upstream | Better rinsing at every stage |

---

### ZONE 6 -- Caustic Drag-Out Control

**Two-column layout:**

**Left -- Drag-Out Reduction:**
Title: `MINIMIZE CAUSTIC DRAG-OUT` Barlow SemiBold 18 pt `#E8A020`
- `Dwell over etch tank 10--15 sec -- caustic is viscous when hot`
- `Orient parts for drainage -- channels, recesses drain slowly`
- `The etch bath is hot (130--150 F) -- viscosity is lower than room temp, but still clings`
- `Every mL of caustic in the rinse = desmut contamination`

**Right -- Cascade Design:**
Title: `CASCADE RINSE DESIGN` Barlow SemiBold 18 pt `#2EC4B6`
- `Counter-flow: fresh water enters final tank`
- `2-stage minimum for post-etch rinse`
- `First stage captures bulk caustic; second delivers final rinse quality`
- `Monitor pH at cascade overflow point`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Desmut) -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; typical rinse parameters for aluminum anodize pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Two-Step Pre-Desmut -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The contamination chain panel connects this seemingly simple rinse to the final color outcome -- three stages downstream. The acid/base neutralization note at the bottom of Zone 3 adds a chemistry lesson that resonates with shop floor operators who can visualize the reaction.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #339 -- Construction Workup v1.0*
*2026-04-26*
