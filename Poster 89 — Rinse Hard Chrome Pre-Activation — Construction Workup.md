---
Project: Plating Posters Inc
Poster Number: 89
Title: "Rinse -- Hard Chrome -- Pre-Activation"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
Technical Source: Pre-activation rinse for hard chrome -- double overflow at ambient to remove alkaline cleaner before parts enter the chrome bath for reverse etch. Thorough rinsing is critical because alkaline contamination in the chrome bath is detrimental.
Process Scope: Pre-activation rinse -- Stage 2 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HardChrome
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #89 -- Construction Workup
## Rinse -- Hard Chrome -- Pre-Activation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. This rinse removes alkaline cleaner drag-out before parts enter the chrome bath for reverse etch (activation). Unlike decorative chrome (where speed trumps thoroughness), hard chrome rinsing demands thoroughness. Alkaline contamination in the chrome bath raises pH, disrupts the CrO3:SO4 ratio, and can cause dull or rough deposits. A double overflow rinse is standard.

Hero visual: a double-overflow rinse system with flow indicators, showing alkaline contamination being diluted before parts proceed to the chrome bath.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Double overflow rinse hero (Block B):** Two-stage rinse system with flow arrows and contamination dilution indicators.
2. **Why thorough rinsing matters (Block D):** What alkaline contamination does to the chrome bath.
3. **Operating parameters (Block E):** Straightforward rinse parameters.
4. **Common issues cards (Block F):** 4 problems.

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
ZONE 3 -- DOUBLE OVERFLOW RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ALKALINE CONTAMINATION IN CHROME BATH (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON ISSUES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hard Chrome -- Pre-Activation -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Alkaline cleaner into the chrome bath is a recipe for dull, rough deposits. Double rinse. Do it right.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

**Safety note (right side):**
- Rounded rect, X: 18.0", Y: 0.6", W: 5.5", H: 0.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Text: `Cr(VI) CARCINOGEN -- see Main Tank poster` JetBrains Mono 10 pt `#E05C5C`

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean parts with alkaline cleaner drag-out  -->  After: Alkaline-free surface ready for reverse etch in chrome bath`

---

### ZONE 3 -- Double Overflow Rinse Hero

**Section label:** `DOUBLE OVERFLOW RINSE` -- Y: 4.4".

**BLOCK B -- Two-Tank Rinse Diagram (Y: 5.0" to 14.0")**

Two tanks side by side:

**Tank 1 -- First Rinse (Dirty):**
- Rounded rect, X: 1.0", Y: 6.0", W: 10.0", H: 6.0", fill `#2EC4B6` at 8%, border 2 pt `#2EC4B6`
- Label: `RINSE 1 (ROUGH)` Barlow SemiBold 16 pt `#2EC4B6`
- Overflow weir on right side
- Parameters inside: `Ambient` / `Continuous overflow` / `Catches bulk of alkaline drag-out`
- Contamination indicator: lighter tint showing dissolved alkaline

**Tank 2 -- Second Rinse (Clean):**
- Rounded rect, X: 13.0", Y: 6.0", W: 10.0", H: 6.0", fill `#27AE60` at 8%, border 2 pt `#27AE60`
- Label: `RINSE 2 (FINAL)` Barlow SemiBold 16 pt `#27AE60`
- Fresh water inlet on left side
- Parameters inside: `Ambient` / `Fresh water in` / `Conductivity < 200 uS/cm`

**Parts movement arrow:** 3 pt `#3A4055`, right-pointing, above tanks.
**Water counter-flow:** 3 pt `#2EC4B6`, left-pointing arrows below tanks.

**Key parameter callout (centered, Y: 13.0"):**
- Rounded rect, W: 20.0", H: 1.0", fill `#E8A020` at 10%, border 1 pt `#E8A020`
- Text: `Unlike decorative chrome rinsing, thoroughness matters here. The chrome bath is expensive and sensitive to contamination. Take the time.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 4 -- Alkaline Contamination in Chrome Bath

**Section label:** `WHAT ALKALINE DRAG-IN DOES TO YOUR CHROME BATH` -- Y: 14.7".

**BLOCK D -- Contamination Panel (Y: 15.3" to 20.3")**

Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#E05C5C`.

| Contaminant | Effect on Chrome Bath | Severity |
|---|---|---|
| NaOH (caustic) | Raises pH; precipitates Cr(OH)3 sludge; reduces CrO3 concentration | HIGH |
| Surfactant (from cleaner) | Organic contamination -- reduces efficiency, causes pitting | HIGH |
| Silicate (from cleaner) | Insoluble silica deposits -- causes rough chrome | MODERATE |
| Hard water minerals | Calcium/magnesium buildup over time | LOW |

Each row: alternating `#1E2435` / `#252B3D`.

**Key insight:**
- `Chrome baths are long-lived (months to years). Every contamination event is cumulative. Good rinsing protects the bath's lifespan and performance.` -- Inter Medium, 14 pt, `#E8A020`

**Cleaner selection note:**
- `Use silicate-free cleaners when possible. Silicate residue is nearly impossible to remove from a chrome bath once introduced.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 5 -- Operating Parameters

**Section label:** `OPERATING PARAMETERS` -- Y: 20.7".

**BLOCK E -- Parameter Table (Y: 21.3" to 26.3")**

| Parameter | Rinse 1 (Rough) | Rinse 2 (Final) |
|---|---|---|
| Water source | City water | DI preferred |
| Temperature | Ambient | Ambient |
| Type | Continuous overflow | Continuous overflow |
| Dwell time | 30--60 sec | 30--60 sec |
| Flow rate | Moderate-high | Moderate |
| Agitation | Part movement (2--3 dips) | Part movement (2--3 dips) |
| Conductivity target | Not critical | < 200 uS/cm |
| Maintenance | Dump and refill when contaminated | Monitor conductivity |

Data: JetBrains Mono 14 pt. Headers: Barlow SemiBold 14 pt.

**Bottom note:**
- `Total rinse time: 1--2 min. Longer than decorative chrome rinsing (15--30 sec) because alkaline contamination in the chrome bath is cumulative and expensive to correct.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 6 -- Common Issues

**Section label:** `COMMON RINSE PROBLEMS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Problem | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DULL CHROME DEPOSIT | `#E8A020` | Alkaline drag-in raising pH, precipitating Cr(OH)3 | Improve rinsing; check conductivity of final rinse |
| R1C2 | ROUGH CHROME | `#E05C5C` | Silicate from cleaner contaminating chrome bath | Switch to silicate-free cleaner; improve rinse |
| R2C1 | REDUCED BATH LIFE | `#E8A020` | Cumulative contamination from inadequate rinsing | Install conductivity alarm on final rinse; double overflow |
| R2C2 | CLEANER FOAM IN CHROME | `#E05C5C` | Surfactant drag-in from cleaner | Use low-foam cleaner; extend rinse stages |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Hard Chrome -- Pre-Activation`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; hard chrome process engineering practice. Hard chrome uses hexavalent chromium -- comply with all applicable OSHA and EPA regulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Hard Chrome Rinse Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The contrast with Poster #81 (decorative chrome pre-activation rinse) is deliberate and important. Decorative chrome rinsing is about speed (nickel passivates). Hard chrome rinsing is about thoroughness (protect the chrome bath). The double overflow system is the visual anchor. The alkaline contamination panel in Zone 4 gives the process engineer the ammunition to justify proper rinsing to management -- every bit of alkaline drag-in shortens the chrome bath's lifespan. The silicate warning is a practical tip that experienced hard chrome platers will immediately recognize and appreciate.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #89 -- Construction Workup v1.0*
*2026-04-26*
