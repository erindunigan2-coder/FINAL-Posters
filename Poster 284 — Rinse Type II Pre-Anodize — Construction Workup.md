---
Project: Plating Posters Inc
Poster Number: 284
Title: "Rinse -- Type II -- Pre-Anodize"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.6)"
Technical Source: Industry-standard pre-anodize rinsing practice for sulfuric acid anodizing (Type II). The most critical rinse in the entire sequence.
Process Scope: Pre-anodize rinse stage (Stage 5 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #284 -- Construction Workup
## Rinse -- Type II -- Pre-Anodize

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is THE most critical rinse in the entire anodizing sequence. Any acid, fluoride, or dissolved metals dragged into the anodize tank contaminate the electrolyte. The hero concept: chloride is the #1 enemy -- >25 ppm causes pitting. Fluoride from HF desmut attacks the growing oxide. This rinse is the last line of defense before the main tank.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Critical rinse diagram hero (Block B):** Double or triple cascade rinse with conductivity monitoring at each stage. Visual emphasis on "this is the gatekeeper."
2. **Contamination thresholds panel (Block D):** What happens when each contaminant reaches the anodize tank.
3. **Conductivity monitoring guide (Block E).**
4. **Failure modes strip (Block F).**

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
ZONE 3 -- CRITICAL RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION THRESHOLDS (14.5"--20.5" / ~6.0")
ZONE 5 -- CONDUCTIVITY MONITORING + WATER QUALITY (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES + AEROSPACE REQUIREMENTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Pre-Anodize (CRITICAL) -- Stage 5 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last line of defense. Everything that gets past this rinse ends up in your anodize tank -- and chloride, fluoride, and metals do not forgive.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Desmutted surface with acid residue  -->  After: Pristine surface with no chemical carryover`

---

### ZONE 3 -- Critical Rinse Hero

**Section label:** `THE MOST CRITICAL RINSE IN THE SEQUENCE` -- Y: 4.4".

**BLOCK B -- Double Cascade Rinse Schematic**

Y: 5.0" to 14.0".

**Two rinse tanks + conductivity meter:**

| Tank | X | W | Label | Target |
|---|---|---|---|---|
| Rinse 1 (cascade) | 2.0" | 9.0" | `RINSE 1` | Remove bulk acid/chemistry |
| Rinse 2 (final) | 13.0" | 9.0" | `FINAL RINSE` | DI water; <100 uS/cm |

Each tank: Rounded rect H: 6.0", fill `#252B3D`, border 2 pt `#C8D0D8`.

**Conductivity meter symbol (between tanks):**
- Small panel, X: 11.5", Y: 7.0", W: 1.5", H: 2.0", fill `#1E2435`, border 1 pt `#27AE60`
- Display: `<100 uS/cm` JetBrains Mono 14 pt `#27AE60`
- Label: `CONDUCTIVITY METER` Inter Medium 11 pt `#F0EDE8`

**Water quality label (entering final rinse):**
- Arrow from right entering Tank 2: `DI WATER IN (<50 uS/cm)` JetBrains Mono 12 pt `#2EC4B6`

**Contamination warnings (floating callouts inside Tank 1):**
- `Cl- from water` Inter Regular 12 pt `#E05C5C`
- `F- from HF desmut` Inter Regular 12 pt `#E05C5C`
- `Dissolved metals` Inter Regular 12 pt `#E05C5C`
- `Acid residue` Inter Regular 12 pt `#E8A020`

**"Gatekeeper" callout (bottom of zone):**
- Rounded rect, full width, H: 1.0", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `THIS RINSE IS THE GATEKEEPER. Chloride >25 ppm in the anodize bath causes pitting. Fluoride attacks the growing oxide. There is no "close enough" -- monitor and maintain.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Contamination Thresholds

**Section label:** `WHAT HAPPENS WHEN CONTAMINANTS REACH THE ANODIZE TANK` -- Y: 14.7".

**BLOCK D -- Contamination Table**

| Contaminant | Source | Threshold in Anodize Bath | Effect |
|---|---|---|---|
| Chloride (Cl-) | Rinse water; city water | >25 ppm | PITTING -- most damaging contaminant |
| Fluoride (F-) | HF desmut dragover | Trace amounts | Attacks growing oxide; degrades coating |
| Copper (Cu) | Dissolved from 2024/7075 | >10 ppm | Mottling and discoloration |
| Iron (Fe) | Water; tank; racking | >100 ppm | Brownish discoloration |
| Acid residue | Desmut dragover | pH shift | Localized acid concentration changes |

Contaminant: Inter Medium 14 pt `#F0EDE8`. Threshold: JetBrains Mono 13 pt `#E05C5C`. Effect: Inter Regular 13 pt `#E8A020`.

Bottom highlight: `Chloride is the #1 rinse-water contaminant. DI water eliminates the risk entirely.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 5 -- Conductivity Monitoring + Water Quality

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Conductivity Monitoring (X: 0.5", W: 11.0"):**

| Parameter | Value |
|---|---|
| Water quality | DI water strongly preferred; <50 uS/cm |
| Temperature | Ambient |
| Time | 60--120 seconds minimum |
| Method | Double cascade rinse recommended; triple for aerospace |
| Conductivity target | <100 uS/cm in final rinse stage |
| Monitoring | Inline conductivity meter or periodic grab sample |

**Right -- Rinse Quality by Application (X: 12.0", W: 11.5"):**

| Application | Rinse Standard | Cascade Stages |
|---|---|---|
| Commercial / decorative | <500 uS/cm | Double cascade |
| MIL-A-8625F (standard) | <100 uS/cm | Double cascade |
| Aerospace (BAC spec) | <50 uS/cm | Triple cascade |
| Critical optical/medical | <20 uS/cm | Triple + final spray |

Note: `More cascade stages = lower contamination risk. Each stage adds ~100x dilution.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 6 -- Failure Modes + Aerospace Requirements

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Failure Modes:**

| Failure | Cause | Fix |
|---|---|---|
| Pitting in anodize | Chloride dragover >25 ppm | Switch to DI water; add cascade stage |
| Soft/thin coating | Fluoride from HF desmut | Improve rinsing; extend time; add spray rinse |
| Mottled coating | Dissolved Cu/Fe carryover | Monitor metal levels; dummy plate desmut |
| Bath chemistry drift | Acid dragover shifts pH | Thorough rinsing; dwell and drain |

**Right -- Aerospace Note:**

Section label: `AEROSPACE RINSING REQUIREMENTS` Barlow Condensed ExtraBold 22 pt.

Callout:
- `For aerospace work (Boeing, Lockheed, Airbus programs):`
- `Triple cascade rinsing is standard practice`
- `DI water required at all stages`
- `Conductivity monitoring is continuous, not periodic`
- `Fluoride monitoring mandatory after HF desmut`

Inter Medium 14 pt `#2EC4B6`. Aerospace label: `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Type II -- Pre-Anodize`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; MIL-A-8625F guidelines for anodize bath contamination control.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type II Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster must convey urgency. Unlike the pre-etch rinse (#281), this rinse has direct, measurable consequences if done poorly. The contamination thresholds table is the core reference value -- a plater can check chloride/fluoride limits at a glance. The "gatekeeper" callout should be unmissable. Conductivity monitoring is the practical tool that makes this actionable -- emphasize it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #284 -- Construction Workup v1.0*
*2026-04-26*
