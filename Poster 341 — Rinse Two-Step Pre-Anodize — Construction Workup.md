---
Project: Plating Posters Inc
Poster Number: 341
Title: "Rinse (Pre-Anodize) -- Two-Step Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 8: Two-Step Color)"
  - "Anodizing Clusters -- Watson Research Brief (Process 1: Type II, Section 1.6)"
Technical Source: Pre-anodize rinse after desmut. Removes acid residue. DI water preferred for critical work. Chloride contamination from city water causes pitting. For two-step color, chloride pitting in the anodize creates color defects visible as dark spots in the electrolytic coloring.
Process Scope: Two-step color anodizing -- Stage 6 of 8 (Rinse, Pre-Anodize)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - TwoStepColor
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #341 -- Construction Workup
## Rinse (Pre-Anodize) -- Two-Step Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The final rinse before the anodize tank. DI water is strongly preferred because chloride from city water causes pitting during anodizing, and pits concentrate metal deposition during the coloring step, creating visible dark spots in the finished color. Fluoride drag-in from HF desmut baths is also a concern -- it destroys oxide structure.

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
  Stage 6 highlighted (Teal)
ZONE 3 -- RINSE PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS + CONTAMINATION LIMITS (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- DI WATER + FLUORIDE CONTROL (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Two-Step Color -- Pre-Anodize -- Stage 6 of 8` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last barrier before the anodize tank. Chloride pits. Fluoride destroys. DI water protects.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Desmutted surface with acid residue --> After: Acid-free, DI-rinsed aluminum ready for anodize`

---

### ZONE 3 -- Rinse Process Hero

**Section label:** `THE PRE-ANODIZE RINSE -- LAST LINE OF DEFENSE` -- Y: 4.4".

**BLOCK B -- Full-Width Panel**

Y: 5.0" to 14.0". Rounded rect, X: 0.5", W: 23.0", H: 8.5", fill `#1E2435`.

**Left half -- Tank + Parameters:**
- `DI water preferred` JetBrains Mono 14 pt `#2EC4B6`
- `Conductivity: < 100 uS/cm target` JetBrains Mono 14 pt `#E8A020`
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 60--120 sec` JetBrains Mono 14 pt `#F0EDE8`
- `Counter-flow cascade (2-stage minimum)` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Right half -- Two Critical Contaminants:**

Title: `THE TWO KILLERS: CHLORIDE AND FLUORIDE` Barlow SemiBold 16 pt `#E05C5C`

Body:
> **Chloride (Cl-) from city water:**
> -- > 25 ppm Cl- causes pitting during anodizing
> -- Pits concentrate tin deposition in coloring step
> -- Visible as dark spots in finished color
> -- DI water eliminates this risk
>
> **Fluoride (F-) from HF desmut drag-over:**
> -- Even trace fluoride destroys the pore structure during anodizing
> -- Results in soft, powdery, non-uniform oxide
> -- Coloring step fails completely on fluoride-damaged oxide
> -- If HF desmut is used: extra rinse stages MANDATORY

**Bottom callout (Y: 13.5"):**
- `CRITICAL: Chloride > 25 ppm in the anodize bath causes pitting visible after coloring. Monitor rinse water chloride monthly.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Rinse Parameters + Contamination Limits

**Section label:** `OPERATING PARAMETERS + CONTAMINANT LIMITS` -- Y: 14.7".

**Two-column layout:**

**Left -- Parameters:**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".

| Parameter | Value |
|---|---|
| Water type | DI water (< 100 uS/cm); < 50 for critical |
| Temperature | Ambient (60--85 F) |
| Time | 60--120 sec |
| Flow | Counter-flow cascade |
| Agitation | Mild air |
| Note | DI spray after cascade for best results |

**Right -- Contaminant Limits:**
Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".
Title: `RINSE WATER CONTAMINANT LIMITS` Barlow SemiBold 18 pt `#E05C5C`

| Contaminant | Limit | Source | Effect |
|---|---|---|---|
| Chloride | < 25 ppm | City water | Pitting in anodize |
| Fluoride | < 1 ppm | HF desmut drag-in | Oxide destruction |
| Iron | < 5 ppm | Pipes | Staining |
| Copper | < 1 ppm | Desmut bath | Immersion deposit |

---

### ZONE 5 -- Failure Modes

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING (DARK SPOTS IN COLOR) | `#E05C5C` | Chloride > 25 ppm | DI water; test supply |
| R1C2 | SOFT/POWDERY OXIDE | `#E05C5C` | Fluoride drag-in from HF desmut | Add extra rinse; verify F < 1 ppm |
| R1C3 | COLOR BLOTCHINESS | `#E8A020` | Acid residue on surface | Extend rinse time |
| R2C1 | WATER SPOTS UNDER OXIDE | `#2EC4B6` | Hard water minerals | DI water |
| R2C2 | IRON STAINING | `#E8A020` | Fe in water supply | Plastic plumbing |
| R2C3 | POOR COLOR ADHESION | `#E05C5C` | Contaminated oxide | Improve pre-anodize rinse |

---

### ZONE 6 -- DI Water + Fluoride Control

**Two-column layout:**

**Left -- DI Water System:**
Title: `DI WATER FOR TWO-STEP COLOR` Barlow SemiBold 18 pt `#2EC4B6`
- `Conductivity: < 100 uS/cm (minimum); < 50 preferred`
- `Inline conductivity meter recommended`
- `DI cartridge replacement schedule based on conductivity monitoring`
- `Final DI spray rinse after cascade for best results`
- `Cost of DI << cost of color rework`

**Right -- Fluoride Control:**
Title: `FLUORIDE MANAGEMENT (IF HF DESMUT USED)` Barlow SemiBold 18 pt `#E8A020`
- `Add static drag-out rinse immediately after HF desmut`
- `3-stage cascade minimum after HF-bearing chemistry`
- `Monitor fluoride in pre-anodize rinse with ion-selective electrode`
- `Target: < 1 ppm fluoride in pre-anodize rinse`
- `If fluoride detected: do NOT proceed to anodize -- re-rinse`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Anodize) -- Two-Step Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; typical rinse parameters for aluminum anodize pre-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Two-Step Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "two killers" callout (chloride + fluoride) is the educational anchor. Both contaminants are invisible in the rinse but catastrophic in the anodize. The fluoride management section is especially important for shops that process multiple alloys -- the HF desmut for 2024/7075 can contaminate the entire downstream line if drag-out is not controlled.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #341 -- Construction Workup v1.0*
*2026-04-26*
