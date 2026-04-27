---
Project: Plating Posters Inc
Poster Number: 334
Title: "Seal / Post Treatment -- Integral Color"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.8)"
Technical Source: Industry-standard sealing options for integral color anodizing. Nickel acetate is preferred for best color retention. No dye step -- color is integral to the oxide. Parameters are typical ranges.
Process Scope: Integral color anodizing -- Stage 7 of 8 (Seal / Post Treatment)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - Seal
  - PostTreatment
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #334 -- Construction Workup
## Seal / Post Treatment -- Integral Color

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 8 (mapped to poster stage "Seal / Post Treatment"). Sealing closes the pores of the anodic oxide, locking in the integral color and providing corrosion resistance. Nickel acetate seal is preferred because it provides the best color retention -- hot water seal can slightly shift the color lighter.

Key distinction: NO DYE STEP. The color was formed during anodizing. Seal is the final functional step.

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
ZONE 3 -- SEAL PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SEAL METHODS COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- QUALITY TESTING + NO DYE CALLOUT (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SEAL` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Integral Color -- Post Treatment -- Stage 7 of 8` -- 34 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The color is already in the oxide. Sealing locks it in, closes the pores, and delivers 30+ years of outdoor durability.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Colored anodic oxide with open pores --> After: Sealed, corrosion-resistant integral color finish`

---

### ZONE 3 -- Seal Process Hero

**Section label:** `SEALING -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Primary Seal Method (Nickel Acetate)**

Y: 5.0" to 10.0". Large rounded rect, fill `#1E2435`, left accent `#27AE60`.

Title: `NICKEL ACETATE SEAL -- PREFERRED FOR INTEGRAL COLOR` Barlow SemiBold 20 pt `#27AE60`.

| Parameter | Value |
|---|---|
| Chemistry | Nickel acetate, Ni(OAc)2 |
| Concentration | 5--8 g/L |
| Temperature | 158--185 F (70--85 C) |
| pH | 5.5--7.0 |
| Time | 20--30 minutes |
| Water quality | DI water (< 50 uS/cm) |

Values: JetBrains Mono Regular, 16 pt, `#F0EDE8`.

Key note: `Nickel acetate provides the BEST color retention during seal. The lower temperature (vs. hot water) minimizes thermal attack on the colored oxide.` Inter Medium 14 pt `#27AE60`.

**BLOCK B2 -- Alternative: Hot DI Water Seal**

Y: 10.5" to 14.0". Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Title: `HOT DI WATER SEAL -- ACCEPTABLE ALTERNATIVE` Barlow SemiBold 18 pt `#2EC4B6`.

| Parameter | Value |
|---|---|
| Chemistry | DI water (< 50 uS/cm conductivity) |
| Temperature | 205--212 F (96--100 C) |
| pH | 5.5--7.5 |
| Time | 20--30 minutes |

Note: `Hot water seal may slightly SHIFT color lighter. Acceptable for many applications but nickel acetate is preferred for premium architectural color match.` Inter Regular 13 pt `#F0EDE8` at 70%.

**Bottom callout (Y: 13.5"):**
- `NO DYE STEP EXISTS IN INTEGRAL COLOR. The color was formed in the anodize tank. Seal is the final process step before dry and pack.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Seal Methods Comparison

**Section label:** `SEAL METHOD COMPARISON` -- Y: 14.7".

**Full-width comparison table (Y: 15.3" to 20.3"):**

| Seal Method | Temp | Chemistry | Time | Color Retention | Corrosion (ASTM B117) | Best For |
|---|---|---|---|---|---|---|
| Nickel acetate | 158--185 F | 5--8 g/L Ni(OAc)2 | 20--30 min | EXCELLENT | 500+ hrs | Architectural (preferred) |
| Hot DI water | 205--212 F | DI water < 50 uS | 20--30 min | Good (slight shift) | 336+ hrs | General purpose |
| Cold nickel fluoride | 77--86 F | Proprietary NiF2 | 15--20 min | Good | Good | High-volume, energy savings |

"EXCELLENT" in `#27AE60`. Column headers in Barlow SemiBold 13 pt `#F0EDE8`.

**Below table -- Important exclusions:**

Coral-accented callout:
- `DO NOT USE DICHROMATE SEAL on integral color -- yellow tint degrades the color appearance.` `#E05C5C`
- `DO NOT DYE integral color parts -- organic dye on top of integral color produces inconsistent results.` `#E05C5C`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- SEAL FAILURES` -- Y: 20.7".

**3x2 Grid:**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SEAL BLOOM (WHITE HAZE) | `#E05C5C` | Tap water minerals (Ca, Mg); pH too high | Use DI water; adjust pH 5.5--7.0 |
| R1C2 | COLOR SHIFT DURING SEAL | `#E8A020` | Hot water seal temperature too high | Switch to nickel acetate (lower temp) |
| R1C3 | CRAZING (FINE CRACKS) | `#E05C5C` | Thermal shock (cold part into hot seal) | Pre-warm parts in warm rinse |
| R2C1 | POOR SEAL QUALITY | `#E8A020` | Temperature too low or time too short | Verify temperature; extend time |
| R2C2 | INCONSISTENT SEAL | `#2EC4B6` | Inadequate agitation in seal tank | Improve air agitation |
| R2C3 | SALT FOG FAILURE | `#E05C5C` | Incomplete seal; contaminated seal bath | Dye spot test; replace seal bath |

---

### ZONE 6 -- Quality Testing + No Dye Callout

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Seal Quality Testing:**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `SEAL QUALITY TESTING` Barlow SemiBold 18 pt `#2EC4B6`.

| Test | Standard | Method |
|---|---|---|
| Dye spot test | ASTM B680 | Sealed surface resists dye; unsealed absorbs |
| Admittance test | ISO 2931 | Impedance measurement; lower = better seal |
| Salt fog | ASTM B117 | 336--1000+ hrs depending on specification |
| Color measurement | ASTM D2244 | CIE L*a*b*; dE < 1.0 for architectural |

JetBrains Mono 12 pt for standard codes.

Note: `Color measurement per ASTM D2244 is mandatory for architectural integral color. Parts must match within dE < 1.0 within a batch.` Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- "No Dye" Emphasis Callout:**

Large Amber-accented panel:
- Title: `INTEGRAL COLOR = NO DYE` Barlow SemiBold 22 pt `#E8A020`
- Body (Inter Regular 14 pt `#F0EDE8`):
  - `The color was formed DURING anodizing`
  - `Organic acid decomposition products are embedded in the oxide`
  - `Adding organic dye on top produces inconsistent results`
  - `This is NOT standard practice`
  - `UV stability is EXCELLENT because the color is inorganic/embedded`
  - `30+ year outdoor durability for architectural applications`

Highlight: `This is what makes integral color special -- the color cannot fade from UV because it is not a dye.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Seal / Post Treatment -- Integral Color`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; typical sealing parameters for integral color anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Seal Post Treatment Integral Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Key messages: (1) Nickel acetate is preferred because it minimizes color shift during seal. (2) NO DYE STEP -- this differentiates integral color from every other anodize process with post-color sealing. (3) The UV stability / 30+ year durability is the selling point of integral color for architectural applications. The "No Dye" callout panel should be visually prominent.

---

*Alaina -- Poster #334 -- Construction Workup v1.0 -- 2026-04-26*
