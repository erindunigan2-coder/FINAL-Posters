---
Project: Plating Posters Inc
Poster Number: 265
Title: "Rinse -- Electroless Cobalt -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt, Poster 3)"
Technical Source: Standard DI counterflow rinse between alkaline cleaning and acid activation. Parameters identical to all electroless pre-activation rinses. Watson domain expertise.
Process Scope: Pre-activation rinse (Stage 2 of 8) for electroless cobalt plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #265 -- Construction Workup
## Rinse -- Electroless Cobalt -- Pre-Activation

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The pre-activation rinse removes alkaline cleaning chemistry before the part enters the acid activation bath. Alkaline drag-in causes pH spikes in the activation bath, leading to poor oxide removal and subsequent skip plating. This is a simple but critical step -- the bridge between cleaning and activation.

Hero visual: counterflow rinse tank system showing two-stage cascade, conductivity meter, and drag-out/drag-in flow arrows.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Two-stage counterflow tank with water flow arrows, conductivity probe, and parts transferring from clean to rinse.
2. **Rinse parameters panel (Block D):** Single comprehensive parameter box.
3. **Why this rinse matters (Block E):** Cause-and-effect chain -- alkaline drag-in -> pH spike -> poor activation -> skip plating.
4. **Rinse efficiency techniques (Block F):** Spray headers, air agitation, counterflow design.

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
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- WHY THIS RINSE MATTERS (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE EFFICIENCY TECHNIQUES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Cobalt -- Pre-Activation -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The bridge between cleaning and activation. Alkaline drag-in to the acid bath is the fastest way to ruin your activation step.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline-wetted surface from cleaning  -->  After: Neutral, clean surface ready for acid activation`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `COUNTERFLOW RINSE SYSTEM` -- Y: 4.4".

**BLOCK B -- Two-Stage Counterflow Tank**

Y: 5.0" to 14.0".

**Two tanks side by side:**
- Tank 1 (first rinse): Rounded rect, X: 1.5", Y: 5.5", W: 9.5", H: 7.5", fill `#252B3D`, border 3 pt `#C8D0D8`
- Tank 2 (final rinse): Rounded rect, X: 12.5", Y: 5.5", W: 9.5", H: 7.5", fill `#252B3D` at lighter tint, border 3 pt `#C8D0D8`
- Label Tank 1: `STAGE 1 RINSE (dirtiest)` Barlow SemiBold 14 pt `#F0EDE8`
- Label Tank 2: `STAGE 2 RINSE (cleanest)` Barlow SemiBold 14 pt `#2EC4B6`

**Water flow arrows:**
- Fresh DI water enters Tank 2 (right), overflows to Tank 1 (left), then to drain
- Curved arrow from Tank 2 to Tank 1: stroke 3 pt `#2EC4B6`, dashed
- Arrow from Tank 1 to drain: stroke 2 pt `#3A4055`
- Label: `Fresh DI in -->` at Tank 2 inlet; `--> Drain` at Tank 1 outlet
- `Counterflow: cleanest water meets cleanest parts` Inter Medium 13 pt `#2EC4B6`

**Parts transfer arrow:**
- Large arrow from left (cleaning tank, off-frame) into Tank 1: `FROM ALKALINE CLEAN` Inter Regular 12 pt `#E8A020`
- Arrow from Tank 2 to right (activation, off-frame): `TO ACTIVATION` Inter Regular 12 pt `#E8A020`

**Conductivity probe (Tank 2):**
- Small rectangle with probe line, X: 20.0", Y: 8.0"
- Label: `Conductivity meter` Inter Regular 11 pt `#F0EDE8`
- Value: `Target: <50 uS/cm` JetBrains Mono 14 pt `#27AE60`

**Bath parameters (inside tanks):**
- `DI or RO water` JetBrains Mono 14 pt `#2EC4B6`
- `Ambient (65--85 F / 18--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `30--60 sec per stage` JetBrains Mono 14 pt `#E8A020`

---

### ZONE 4 -- Rinse Parameters

**Section label:** `RINSE SPECIFICATIONS` -- Y: 14.7".

**BLOCK D -- Parameter Panel (Y: 15.3" to 20.3")**

Single large callout box: Rounded rect, X: 0.5", Y: 15.3", W: 23.0", H: 4.8", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

| Parameter | Specification |
|---|---|
| Rinse type | Counterflow (2-stage minimum); spray rinse acceptable for rack work |
| Water quality | DI or RO preferred; municipal acceptable if <200 ppm TDS |
| Temperature | Ambient (18--30 C / 65--85 F) |
| Immersion time | 30--60 seconds per stage |
| Agitation | Overflow + optional air sparger |
| Conductivity target | <50 uS/cm in final rinse stage |
| Flow rate | Sufficient to maintain conductivity target under production load |

Parameters: JetBrains Mono Regular 14 pt `#F0EDE8`. Labels: Inter Medium 14 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Why This Rinse Matters

**Section label:** `THE FAILURE CHAIN -- WHAT HAPPENS WHEN YOU SKIP OR RUSH` -- Y: 20.7".

**BLOCK E -- Cause-Effect Chain (Y: 21.3" to 26.3")**

Horizontal chain of 4 linked boxes with arrows:

| Step | Box Fill | Accent | Text |
|---|---|---|---|
| 1 | `#1E2435` | `#E8A020` | `Alkaline drag-in to activation bath` |
| 2 | `#1E2435` | `#E05C5C` | `pH spike in acid bath -- acid neutralized` |
| 3 | `#1E2435` | `#E05C5C` | `Poor oxide removal -- surface not activated` |
| 4 | `#1E2435` | `#E05C5C` | `SKIP PLATING -- no cobalt deposition` |

Each box: W: 5.25", H: 2.5", rounded rect, left accent 0.06".
Arrows between boxes: 3 pt `#3A4055`, right-pointing.

Below chain:
- `For aluminum substrates: residual alkaline on aluminum causes uncontrolled etching and surface roughness before zincate` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Rinse Efficiency Techniques

**Section label:** `IMPROVING RINSE EFFICIENCY` -- Y: 26.7".

**BLOCK F -- Three Technique Cards (Y: 27.3" to 32.3")**

Three cards in a row, gap 0.5":

| Card | X | W | Technique | Detail |
|---|---|---|---|---|
| 1 | 0.5" | 7.0" | SPRAY HEADERS | Mount spray bars above rinse tanks; pre-rinse parts during transfer; reduces drag-in by 50--70% |
| 2 | 8.0" | 7.0" | AIR AGITATION | Gentle air sparger at tank bottom improves rinse contact; avoid violent agitation that causes splashing |
| 3 | 15.5" | 8.0" | CONDUCTIVITY MONITORING | Continuous conductivity meter in final stage; alarm at >50 uS/cm; automatic DI makeup on demand |

Each card: Rounded rect H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt in `#2EC4B6`.
Title: Barlow SemiBold 18 pt `#2EC4B6`. Detail: Inter Regular 14 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Electroless Cobalt -- Pre-Activation`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; counterflow rinse parameters are standard across all electroless plating processes.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Cobalt Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Pre-activation rinse is one of the "support step" posters that shares chemistry across all electroless clusters. The unique value here is placing it in the cobalt context and emphasizing the failure chain. The conductivity target (<50 uS/cm) is the measurable quality gate. Layout should match the rinse poster template across all electroless clusters for visual consistency per Watson flag #8.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #265 -- Construction Workup v1.0*
*2026-04-26*
