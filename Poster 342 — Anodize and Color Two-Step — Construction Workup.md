---
Project: Plating Posters Inc
Poster Number: 342
Title: "Anodize + Electrolytic Color -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color, Sections 8.5--8.8)"
  - "Anodizing Clusters -- Watson Research Brief (Process 1: Type II, Section 1.7)"
Technical Source: Two electrochemical steps combined in one poster. Step 1: Standard Type II sulfuric acid anodize creates the porous oxide. Step 2: AC electrolytic coloring deposits metallic tin into the pore bases. Color is controlled by time in the coloring bath. Stannous sulfate is the most common coloring chemistry. Parameters from Watson brief Cluster 8, Sections 8.5--8.7.
Process Scope: Two-step color anodizing -- Stages 7a+7b of 8 (Anodize + Electrolytic Color)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Anodize
  - ElectrolyticColor
  - MainTank
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #342 -- Construction Workup
## Anodize + Electrolytic Color -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stages 7a + 7b combined -- the heart of the two-step process. This poster covers BOTH electrochemical steps: (1) the sulfuric acid anodize that creates the porous oxide, and (2) the AC electrolytic coloring that deposits metallic tin into the pore bases. These are two separate tanks with two different power sources (DC for anodize, AC for color), but they form one continuous process stage.

This is the most technically complex poster in the entire anodizing series. Two tanks, two chemistries, two power supplies, one seamless operation. The hero visual must show both tanks and the transition between them.

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
  Stage 7 highlighted (Emerald)
ZONE 3 -- TWO-TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS (BOTH STEPS) (14.5"--20.5" / ~6.0")
ZONE 5 -- HOW ELECTROLYTIC COLORING WORKS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS + COLOR BY TIME (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ANODIZE + COLOR` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Electrolytic -- Stages 7a + 7b of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Two tanks, two power supplies. DC creates the pores. AC fills them with metal. Time controls the color -- from champagne to black.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, desmutted aluminum surface --> After: Colored anodic oxide with tin particles deposited in pore bases`

---

### ZONE 3 -- Two-Tank Hero

**Section label:** `TWO TANKS, TWO STEPS, ONE FINISH` -- Y: 4.4".

**BLOCK B -- Dual Tank Diagram**

Y: 5.0" to 14.0". Full-width panel, fill `#1E2435`.

**Left Tank -- Anodize (Step 1) (X: 0.5", W: 11.0"):**

Rounded rect, fill `#252B3D`, border 2 pt `#27AE60`.
Label above: `STEP 1: SULFURIC ACID ANODIZE` Barlow SemiBold 16 pt `#27AE60`
Sub-label: `Standard Type II -- DC Power` Inter Medium 12 pt `#F0EDE8` at 60%

Tank cross-section with:
- Parts (anode): vertical rects, fill `#C8D0D8` at 40%, label `ANODE (+)`
- Cathode: vertical rects on sides, fill `#3A4055`, label `Pb OR 6063 CATHODE (-)`
- Power: `DC RECTIFIER` above, rect fill `#1E2435`, border `#27AE60`

Bath parameters inside tank:
- `H2SO4: 150--200 g/L (15--20%)` JetBrains Mono 13 pt `#27AE60`
- `Temp: 64--72 F (18--22 C)` JetBrains Mono 13 pt `#E8A020`
- `CD: 12--18 ASF` JetBrains Mono 13 pt `#F0EDE8`
- `Voltage: 15--18V DC` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 20--60 min` JetBrains Mono 13 pt `#F0EDE8`
- `Target: 0.5--1.0 mil (12--25 um)` JetBrains Mono 12 pt `#E8A020`

**Transfer Arrow (Center):**
- Large horizontal arrow, X: 11.5" to 12.5", Y: 9.0"
- Stroke: 4 pt `#E8A020`, arrowhead filled
- Label above: `RINSE` Inter Medium 14 pt `#2EC4B6`
- Label below: `Transfer immediately` Inter Regular 11 pt `#F0EDE8` at 60%

**Right Tank -- Electrolytic Color (Step 2) (X: 12.5", W: 11.0"):**

Rounded rect, fill `#252B3D`, border 2 pt `#2EC4B6`.
Label above: `STEP 2: ELECTROLYTIC COLORING` Barlow SemiBold 16 pt `#2EC4B6`
Sub-label: `Tin Deposition -- AC Power` Inter Medium 12 pt `#F0EDE8` at 60%

Tank cross-section with:
- Parts: vertical rects, fill `#C8D0D8` at 40% (now with color gradient at base -- conceptual)
- Counter-electrode: `316 SS, Sn, or GRAPHITE` JetBrains Mono 10 pt `#C8D0D8`
- Power: `AC POWER SUPPLY (60 Hz)` above, rect fill `#1E2435`, border `#2EC4B6`

Bath parameters:
- `SnSO4: 10--25 g/L` JetBrains Mono 13 pt `#2EC4B6`
- `H2SO4: 10--20 g/L` JetBrains Mono 13 pt `#F0EDE8`
- `Organic additives: per vendor` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Temp: 65--75 F (18--24 C)` JetBrains Mono 13 pt `#E8A020`
- `Voltage: 10--18V AC` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 30 sec -- 15 min` JetBrains Mono 13 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `STEP 1 creates the pores. STEP 2 fills them with metal. The anodize must be PERFECT before coloring begins -- every pore-depth variation becomes a color variation.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Operating Parameters (Both Steps)

**Section label:** `OPERATING PARAMETERS -- BOTH STEPS` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Step 1: Anodize (X: 0.5", W: 11.0"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `STEP 1: SULFURIC ACID ANODIZE` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Value | Note |
|---|---|---|
| Electrolyte | H2SO4 150--200 g/L | Standard Type II |
| Temperature | 64--72 F (18--22 C) | Tighter than standard: +/- 1 F |
| Current density | 12--18 ASF (1.3--2.0 A/dm2) | Current-controlled |
| Voltage | 15--18V DC | Rises as oxide grows |
| Time | 20--60 min | Longer = thicker = darker color potential |
| Oxide thickness | 0.5--1.0 mil (12--25 um) | Thicker for darker architectural colors |
| Dissolved Al | < 20 g/L | Maintain for consistency |
| Cathode | Lead, Pb-Sn alloy, or 6063 Al | 1:1 to 2:1 cathode:anode ratio |

**Right -- Step 2: Electrolytic Color (X: 12.0", W: 11.5"):**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".
Title: `STEP 2: ELECTROLYTIC COLORING` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value | Note |
|---|---|---|
| Metal salt | SnSO4 (stannous sulfate) | Most common in N. America |
| Concentration | 10--25 g/L SnSO4 | With Sn counter-electrode: ~12 g/L |
| H2SO4 | 10--20 g/L | Conductivity |
| Organic additives | ~1 lb per 3 lb SnSO4 | Vendor-specified; mandatory |
| Temperature | 65--75 F (18--24 C) | Room temperature range |
| Power | AC (60 Hz single phase) | NOT DC |
| Voltage | 10--18V AC (typical 14--16V) | Matched to pore structure from Step 1 |
| Current | 5 ASF average / 10 ASF peak | Self-regulating |
| Counter-electrode | 316 SS, tin, or graphite | Tin replenishes the bath |

---

### ZONE 5 -- How Electrolytic Coloring Works

**Section label:** `THE MECHANISM -- HOW METAL BECOMES COLOR` -- Y: 20.7".

**Full-width mechanism panel (Y: 21.3" to 26.3"):**
Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`.

**Three-column mechanism:**

*Column 1 -- The AC Cycle (X: 1.0", W: 7.0"):*
Title: `THE AC CYCLE` Barlow SemiBold 16 pt `#2EC4B6`
Body:
> During the cathodic half-cycle (60 Hz):
> -- Sn2+ ions migrate into the pores
> -- Tin deposits at the pore bottoms (barrier layer)
>
> During the anodic half-cycle:
> -- Partial dissolution/redistribution of deposited tin
>
> Net result: metallic tin particles accumulate at the base of every pore.

*Column 2 -- How Color Forms (X: 8.5", W: 7.0"):*
Title: `HOW COLOR FORMS` Barlow SemiBold 16 pt `#E8A020`
Body:
> Color comes from two optical effects:
>
> 1. **Light absorption** by metallic tin particles
> 2. **Interference effects** from pore depth and particle spacing
>
> Deeper pores = more tin deposited = darker color
> Longer time in coloring bath = more tin = darker shade
>
> Color is controlled by TIME -- the simplest control variable in anodizing.

*Column 3 -- Color by Time (X: 16.0", W: 7.0"):*
Title: `COLOR BY TIME` Barlow SemiBold 16 pt `#27AE60`

| Color | Time |
|---|---|
| Light champagne | 30 sec -- 1 min |
| Medium bronze | 2--5 min |
| Dark bronze | 5--8 min |
| Black | ~10 min |

Note: `These times are approximate and depend on oxide thickness, SnSO4 concentration, and voltage. Calibrate for your specific line.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Defect Diagnosis + Color Control

**Section label:** `WHAT GOES WRONG + COLOR CONTROL TIPS` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Defect Diagnosis (X: 0.5", W: 11.0"):**
Title: `TWO-STEP COLOR DEFECTS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Defect | Cause | Fix |
|---|---|---|
| Color variation (batch) | Inconsistent anodize thickness | Tighten anodize temp +/- 1 F |
| Metallic sheen/surface deposit | Metal ON surface, not in pores | Reduce coloring voltage |
| Blotchy appearance | Uneven rinse between anodize and color | Improve rinse; check for drag-over |
| Fading (should not occur) | Organic dye contamination or incomplete color | Verify process is inorganic |
| Dark spots | Pitting from chloride | Monitor Cl- in anodize bath |
| Color non-uniformity (rack) | Uneven current in coloring bath | Improve racking; uniform spacing |

Coral left accent. Data: Inter Regular 12 pt `#F0EDE8`.

**Right -- Color Control Tips (X: 12.0", W: 11.5"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `COLOR MATCHING BEST PRACTICES` Barlow SemiBold 18 pt `#27AE60`

Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):
> **Consistent anodize is the prerequisite:**
> -- Same oxide thickness = same pore depth = same color depth
> -- Temperature +/- 1 F; time +/- 30 sec; CD +/- 1 ASF
>
> **Coloring bath control:**
> -- Monitor SnSO4 by titration or AA
> -- Replenish organic additives per schedule
> -- Replace bath when performance degrades
>
> **Process control:**
> -- Calibrate coloring time to desired shade with test panels
> -- Match parts by alloy lot (same extrusion heat)
> -- Consistent racking position for uniform current distribution
>
> **AAMA 611 requirement:** dE < 1.0 between production panels and master standard.

---

### ZONE 7 -- Footer

Standard. Title: `Anodize + Electrolytic Color -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; AAMA 611. Specific coloring formulations (Duranodic, Anolok, Colinal) are proprietary. Parameters shown are representative. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize and Color Two-Step -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the Two-Step cluster -- the one that explains the core innovation. The dual-tank hero (Block B) is the most important visual in the entire two-step series. The transfer arrow between tanks must be visually prominent -- it represents the critical moment where DC anodize becomes AC coloring. The "color by time" table is the single most valuable piece of data for an operator: it tells them exactly how long to hold parts in the coloring bath for each shade. Simple, actionable, directly useful on the shop floor.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #342 -- Construction Workup v1.0*
*2026-04-26*
