---
Project: Plating Posters Inc
Poster Number: 332
Title: "Rinse -- Pre-Anodize -- Integral Color"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.6)"
Technical Source: Industry-standard pre-anodize rinse practices for aluminum. The most critical rinse in the sequence -- any contamination dragged into the anodize electrolyte degrades coating quality. Parameters are typical ranges.
Process Scope: Integral color anodizing -- Stage 5 of 8 (Rinse -- Pre-Anodize)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #332 -- Construction Workup
## Rinse -- Pre-Anodize -- Integral Color

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8 (mapped to poster stage "Rinse -- Pre-Anodize"). The most critical rinse in the entire sequence. Any acid, fluoride, or dissolved metals dragged into the integral color anodize tank contaminate the electrolyte -- and in integral color, electrolyte purity directly affects color.

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
  Stage 5 highlighted (Teal)
ZONE 3 -- RINSE PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION THRESHOLDS + MONITORING (14.5"--20.5" / ~6.0")
ZONE 5 -- FAILURE MODES (20.5"--26.5" / ~6.0")
ZONE 6 -- WATER QUALITY + BEST PRACTICES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Pre-Anodize Rinse -- Integral Color -- Stage 5 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The most critical rinse in the line. Everything that enters this rinse exits into the anodize bath. Chloride, fluoride, metals -- all of it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Desmutted aluminum with trace acid residue --> After: Ultra-clean surface ready for integral color anodize`

---

### ZONE 3 -- Rinse Process Hero

**Section label:** `PRE-ANODIZE RINSE -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Parameter Panel**

Y: 5.0" to 14.0". Large rounded rect, fill `#1E2435`.

**Left column (X: 1.0", W: 11.0") -- Parameter Table:**

| Parameter | Value |
|---|---|
| Water quality | DI water strongly preferred |
| Conductivity target | < 100 uS/cm in final rinse stage |
| Temperature | Ambient |
| Time | 60--120 seconds minimum |
| Method | Double cascade rinse recommended |
| Agitation | Air or mechanical |

Values: JetBrains Mono Regular, 15 pt, `#F0EDE8`.

**Right column (X: 12.5", W: 10.5") -- Why This Rinse Matters:**

Three stacked callout boxes:

*Callout 1 (Coral):*
- `CHLORIDE -- THE #1 ENEMY` Barlow SemiBold 16 pt `#E05C5C`
- `Chloride > 25 ppm in the anodize bath causes pitting. Rinse water is the #1 source of chloride contamination.` Inter Regular 13 pt `#F0EDE8`

*Callout 2 (Coral):*
- `FLUORIDE -- SILENT DESTROYER` Barlow SemiBold 16 pt `#E05C5C`
- `Fluoride dragover from HF desmut attacks the growing oxide. Even trace amounts degrade coating quality and color consistency.` Inter Regular 13 pt `#F0EDE8`

*Callout 3 (Amber):*
- `DISSOLVED METALS` Barlow SemiBold 16 pt `#E8A020`
- `Metal ions dragged from desmut into the anodize bath accumulate over time and cause discoloration in the integral color oxide.` Inter Regular 13 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `Monitor this rinse with a conductivity meter every shift. Rising conductivity = rising contamination risk.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Contamination Thresholds + Monitoring

**Section label:** `WHAT CONTAMINANTS DO TO INTEGRAL COLOR` -- Y: 14.7".

**Left (X: 0.5", W: 14.0") -- Contamination Impact Table:**

| Contaminant | Source | Threshold in Anodize Bath | Effect on Integral Color |
|---|---|---|---|
| Chloride (Cl-) | Tap water, cleaner residue | > 25 ppm | Pitting; circular defects in colored oxide |
| Fluoride (F-) | HF desmut dragover | > 5 ppm | Oxide thinning; uneven color |
| Copper (Cu) | Desmut of Cu-bearing alloys | > 10 ppm | Mottling; color shift |
| Iron (Fe) | Water, tank corrosion | > 100 ppm | Brownish discoloration |
| Sulfate (SO4 2-) | Various | Varies | Affects electrolyte balance |

Threshold values in `#E05C5C` JetBrains Mono 13 pt. Effects in Inter Regular 12 pt.

**Right (X: 15.0", W: 8.5") -- Monitoring Checklist:**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `MONITOR EVERY SHIFT` Barlow SemiBold 16 pt `#2EC4B6`.

| Check | Tool | Target |
|---|---|---|
| Conductivity | Handheld meter | < 100 uS/cm |
| pH | pH meter/strips | 6--8 |
| Chloride | Ion test kit | < 10 ppm in rinse |
| Visual | Observation | Clear, no color |

Note: `If conductivity exceeds 100 uS/cm, increase fresh water flow or dump and refill.` Inter Regular 12 pt `#E8A020`.

---

### ZONE 5 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- PRE-ANODIZE RINSE FAILURES` -- Y: 20.7".

**3x2 Grid:**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING IN ANODIZE | `#E05C5C` | Chloride contamination from rinse water | Switch to DI water; check source |
| R1C2 | THIN OXIDE | `#E8A020` | Fluoride dragover from desmut | Extend rinse time; add rinse stage |
| R1C3 | COLOR SHIFT | `#E05C5C` | Metal ions in anodize bath (from dragover) | Improve rinse; consider bath analysis |
| R2C1 | SOFT COATING | `#E8A020` | Acid dragover diluting electrolyte | Better cascade; longer dwell time |
| R2C2 | MOTTLED FINISH | `#E05C5C` | Multiple contaminants combined | Full rinse system evaluation |
| R2C3 | REDUCED COATING LIFE | `#2EC4B6` | Chronic low-level contamination | Install conductivity alarm; regular testing |

---

### ZONE 6 -- Water Quality + Best Practices

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- DI Water Specifications:**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `DI WATER FOR PRE-ANODIZE RINSE` Barlow SemiBold 18 pt `#2EC4B6`.

| Parameter | Target |
|---|---|
| Conductivity | < 10 uS/cm (supply); < 100 uS/cm (rinse tank) |
| Chloride | < 1 ppm |
| Total dissolved solids | < 10 ppm |
| pH | 5.5--7.5 |

Note: `Triple cascade rinsing is common in aerospace integral color lines. For architectural work, double cascade with DI water is the standard.` Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- Best Practices:**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `BEST PRACTICES` Barlow SemiBold 18 pt `#27AE60`.

Bullets:
- `Dwell rack over desmut tank 10--15 sec before entering rinse`
- `Double or triple cascade rinse -- fresh water enters final stage`
- `Install conductivity meter with alarm setpoint at 100 uS/cm`
- `Test chloride monthly in the rinse water supply`
- `Never reuse pre-anodize rinse water for any upstream rinse`
- `This is the last defense before the anodize tank -- treat it that way`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Pre-Anodize -- Integral Color`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; standard pre-anodize rinse parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Pre-Anodize Integral -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "most critical rinse" framing gives this poster urgency. The contamination threshold table is the hero data -- operators need to know what ppm levels of chloride and fluoride destroy their integral color results. The conductivity monitoring emphasis is the most actionable takeaway for a shop floor poster.

---

*Alaina -- Poster #332 -- Construction Workup v1.0 -- 2026-04-26*
