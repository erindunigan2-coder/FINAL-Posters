---
Project: Plating Posters Inc
Poster Number: 336
Title: "Cleaning -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color, Section 8.2)"
Technical Source: Alkaline soak cleaning for two-step electrolytic color anodizing. Standard non-silicated inhibited cleaner. Same as Type II pre-treatment. Etch uniformity is critical because it drives color uniformity in the electrolytic coloring step.
Process Scope: Two-step color anodizing -- Stage 1 of 8 (Cleaning)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Cleaning
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #336 -- Construction Workup
## Cleaning -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for two-step electrolytic color anodizing is identical to standard Type II cleaning. The critical emphasis for two-step: cleaning quality ultimately drives COLOR uniformity because uneven cleaning leads to uneven etch, which leads to uneven oxide thickness, which leads to uneven metal deposition in the coloring bath. The chain of consequences is longer in two-step than in any other anodizing process.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANER CHEMISTRY + WATER BREAK TEST (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- THE CHAIN OF CONSEQUENCES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color Anodizing -- Stage 1 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Clean surface, clean etch, uniform oxide, uniform color. The chain starts here. Break a link and the color pays the price.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight small stage boxes. Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Shop-soiled aluminum extrusion --> After: Oil-free, water-break-free surface ready for etch`

---

### ZONE 3 -- Cleaning Process Hero

**Section label:** `ALKALINE SOAK CLEANING` -- Y: 4.4".

**BLOCK B -- Operating Parameters Panel**

Y: 5.0" to 14.0". Rounded rect, X: 0.5", W: 23.0", H: 8.5", fill `#1E2435`, radius 8.

**Left column (X: 1.0", W: 11.0") -- Parameter Table:**

| Parameter | Value |
|---|---|
| Chemistry | Non-silicated alkaline cleaner (inhibited for Al) |
| Concentration | 30--60 g/L (4--8 oz/gal) |
| Temperature | 130--160 F (55--70 C) |
| Time (soak) | 2--10 minutes |
| Time (spray) | 1--3 minutes |
| Agitation | Mild air or mechanical |
| pH | 9--12 |

**Right column (X: 12.5", W: 10.5") -- Key Rules:**

*Rule 1 (Coral):*
- `NEVER USE SILICATED CLEANERS` Barlow SemiBold 16 pt `#E05C5C`
- `Silicate deposits block oxide growth. Bare spots = color gaps.` Inter Regular 13 pt `#F0EDE8`

*Rule 2 (Teal):*
- `WATER-BREAK TEST MANDATORY` Barlow SemiBold 16 pt `#2EC4B6`
- `Continuous water film = clean. Any beading = organic residue. Re-clean.` Inter Regular 13 pt `#F0EDE8`

*Rule 3 (Amber):*
- `UNIFORM CLEANING = UNIFORM COLOR` Barlow SemiBold 16 pt `#E8A020`
- `Two-step color amplifies every pre-treatment defect. Clean poorly and the color will tell the story.` Inter Regular 13 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `Architectural color matching (dE < 1.0 per AAMA 611) starts with consistent cleaning. Batch-to-batch color variation is often traced back to cleaning inconsistency.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Cleaner Chemistry + Water Break Test

**Section label:** `CLEANER SELECTION + VERIFICATION` -- Y: 14.7".

**Two-column layout:**

**Left -- Cleaner Types:**

| Cleaner Type | Suitability | Notes |
|---|---|---|
| Non-silicated alkaline (inhibited) | PREFERRED | Standard for all anodizing |
| Silicated alkaline | NEVER | Silicate blocks oxide growth |
| Solvent / emulsion | PRE-CLEAN ONLY | For heavy oils, machining fluids |
| Acid cleaner | NOT TYPICAL | May be used for light oxide removal |

**Right -- Best Practices:**
Title: `BEST PRACTICES FOR TWO-STEP COLOR` Barlow SemiBold 18 pt `#27AE60`
- `Monitor cleaner concentration weekly by titration`
- `Replace bath when contamination exceeds cleaning ability`
- `Consistent dwell time (soak) for consistent etch response`
- `Rinse immediately after cleaning -- do not allow parts to air dry`
- `For rack work: same rack position consistency for color matching`

---

### ZONE 5 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- CLEANING FAILURES` -- Y: 20.7".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP ANODIZING | `#E05C5C` | Organic residue | Extend soak; check cleaner strength |
| R1C2 | STREAKING IN ETCH | `#E8A020` | Incomplete rinse after clean | Improve rinse; add cascade |
| R1C3 | COLOR VARIATION (TWO-STEP) | `#E05C5C` | Uneven cleaning -> uneven etch -> uneven oxide | Tighten cleaning consistency |
| R2C1 | FINGERPRINTS IN COLOR | `#E8A020` | Bare-hand handling | Clean gloves only |
| R2C2 | SILICATE STAINING | `#E05C5C` | Silicated cleaner used | Replace with non-silicated |
| R2C3 | ETCHING IN CLEANER | `#2EC4B6` | pH too high / inhibitor depleted | Replace bath; verify pH |

---

### ZONE 6 -- The Chain of Consequences

**Section label:** `THE CHAIN OF CONSEQUENCES -- WHY CLEANING MATTERS FOR COLOR` -- Y: 26.7".

**Full-width chain diagram (Y: 27.3" to 32.3"):**
Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`.

Title: `CLEANING -> ETCH -> OXIDE -> COLOR` Barlow SemiBold 22 pt `#E8A020`

**Horizontal chain (four linked boxes with arrows):**

| Box | Label | Good Result | Bad Result |
|---|---|---|---|
| 1 | CLEAN | Uniform soil removal | Residual contamination |
| 2 | ETCH | Even matte texture | Uneven etch (streaks, patches) |
| 3 | ANODIZE | Consistent pore depth | Variable thickness |
| 4 | COLOR | Uniform tin deposition | Blotchy, streaked, or banded color |

Good results: `#27AE60`. Bad results: `#E05C5C`.

Bottom note: `In two-step color, every upstream inconsistency is AMPLIFIED by the electrolytic coloring step. Color darkness depends on pore depth. Pore depth depends on oxide thickness. Oxide thickness depends on etch uniformity. Etch uniformity depends on cleanliness.` Inter Medium 14 pt `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; AAMA 611; typical alkaline cleaning parameters for aluminum anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Two-Step Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "chain of consequences" diagram in Zone 6 is unique to the two-step cluster. It visually demonstrates how cleaning quality propagates through four stages to ultimately affect color uniformity. This is the poster's educational signature -- a concept that applies to all anodizing but is most dramatically visible in two-step color where color variation is the most obvious quality defect.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #336 -- Construction Workup v1.0*
*2026-04-26*
