---
Project: Plating Posters Inc
Poster Number: 233
Title: "Rinse -- EN (High Phos) -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 3: EN High-P)"
Technical Source: Pre-activation rinse between alkaline cleaning and acid activation for EN High-P process. Stage 2 of 8. No brand names.
Process Scope: Pre-activation rinse stage for electroless nickel high-phosphorus process
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - HighPhosphorus
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ClusterEN03
---

# Poster #233 -- Construction Workup
## Rinse -- EN (High Phos) -- Pre-Activation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The bridge between alkaline cleaning and acid activation. Rinse posters are deceptively simple -- the science is in what you are preventing. Alkaline drag-in to the acid activation bath neutralizes the acid, raises pH, and produces poor activation. For aluminum substrates heading to a zincate step, residual alkaline cleaner causes uncontrolled etching and surface roughness. This rinse is the gatekeeper.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Counterflow rinse system with two stages, flow direction arrows, conductivity probe placement.
2. **Drag-in/drag-out contamination diagram (Block D):** Visual showing what contaminants are being removed and why.
3. **Conductivity monitoring panel (Block E):** Target values with gauge visual.
4. **Rinse efficiency callout (Block F):** Tips for improving rinse quality.

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
ZONE 3 -- RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAG-IN CONTAMINATION (14.5"--20.5" / ~6.0")
ZONE 5 -- CONDUCTIVITY MONITORING (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE EFFICIENCY TIPS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN (High Phos) -- Pre-Activation -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The bridge between cleaning and activation. What you drag in, you pay for downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline cleaner on surface  -->  After: Neutral, contaminant-free surface ready for acid activation`

---

### ZONE 3 -- Rinse System Hero

**Section label:** `COUNTERFLOW RINSE -- 2-STAGE MINIMUM` -- Y: 4.4".

**BLOCK B -- Counterflow Rinse Diagram**

Y: 5.0" to 14.0".

**Two tanks side by side:**

*Tank 1 (First Rinse -- Dirty Side):*
- Rounded rect, X: 1.0", Y: 5.5", W: 10.0", H: 7.0"
- Fill: `#252B3D`, border 2 pt `#C8D0D8`
- Label: `STAGE 1 (DIRTY)` Barlow SemiBold 16 pt `#F0EDE8`
- Water flow arrow entering from Tank 2 (clean water cascades backward)

*Tank 2 (Final Rinse -- Clean Side):*
- Rounded rect, X: 13.0", Y: 5.5", W: 10.0", H: 7.0"
- Fill: `#252B3D` at lighter tint, border 2 pt `#C8D0D8`
- Label: `STAGE 2 (CLEAN)` Barlow SemiBold 16 pt `#27AE60`
- Fresh DI water inlet arrow at top

**Flow direction arrows:**
- Large arrow from Tank 2 overflow to Tank 1 inlet
- Tank 1 overflow to drain
- Label: `COUNTERFLOW: Fresh water enters clean side, cascades to dirty side` Inter Medium 13 pt `#2EC4B6`

**Parts movement arrow:**
- Arrow from left (from cleaning) through Tank 1 to Tank 2 to right (to activation)
- Label: `Parts flow: Clean tank --> Dirty rinse --> Clean rinse --> Activation` Inter Regular 13 pt `#F0EDE8`

**Parameter labels inside tanks:**

Right side of Tank 2 (X: 15.0", Y: 7.0"):
- `Water: DI or RO preferred` JetBrains Mono 14 pt `#2EC4B6`
- `Municipal OK if <200 ppm TDS` JetBrains Mono 13 pt `#F0EDE8`
- `Temp: Ambient (18--30 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 30--60 sec per stage` JetBrains Mono 14 pt `#F0EDE8`
- `Target: <50 uS/cm final rinse` JetBrains Mono 14 pt `#27AE60`

**Conductivity probe icon (in Tank 2):**
- Small rect with probe symbol, labeled `CONDUCTIVITY PROBE` JetBrains Mono 11 pt `#E8A020`

**Bottom callout (Y: 13.3"):**
- `Spray rinse header bars above the rinse tank improve efficiency -- consider adding them to both stages.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Drag-In Contamination

**Section label:** `WHAT YOU ARE REMOVING -- AND WHY IT MATTERS` -- Y: 14.7".

**BLOCK D -- Contamination Flow Diagram (Y: 15.3" to 20.3")**

Three-column layout showing contaminant, consequence if not removed, and downstream effect:

| Contaminant | Source | If Not Removed |
|---|---|---|
| NaOH / alkaline cleaner | Cleaning tank drag-out | Neutralizes acid activation; raises pH; poor activation |
| Na2CO3 (carbonate) | Cleaner component | Precipitates in acid; surface deposits |
| Surfactant residue | Cleaner wetting agents | Foaming in activation; passivates surface |
| Silicate (if present) | Some cleaners contain silicate | Poisons EN catalytic surface -- causes skip plating |

Each row: Rounded rect, full width, H: 1.1", fill alternating `#1E2435` / `#252B3D`, left accent `#E05C5C`.
Contaminant: Barlow SemiBold 14 pt `#E05C5C`. Source: Inter Regular 12 pt `#F0EDE8`. Consequence: Inter Medium 13 pt `#E8A020`.

**Bottom warning (Y: 19.8"):**
- Rounded rect, full width, H: 0.4", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `For aluminum substrates: residual alkaline cleaner causes uncontrolled etching and surface roughness before zincate` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Conductivity Monitoring

**Section label:** `CONDUCTIVITY -- YOUR RINSE QUALITY NUMBER` -- Y: 20.7".

**BLOCK E -- Conductivity Gauge (Y: 21.3" to 26.3")**

**Horizontal bar gauge (centered, W: 20.0", H: 0.8"):**
- Red zone: `>200 uS/cm` fill `#E05C5C` at 40% -- `Unacceptable`
- Yellow zone: `50--200 uS/cm` fill `#E8A020` at 30% -- `Marginal`
- Green zone: `<50 uS/cm` fill `#27AE60` at 40% -- `Target for pre-activation rinse`

**Callout boxes below gauge:**

Left (X: 0.5", W: 7.33"):
- `WHAT IS CONDUCTIVITY?` Barlow SemiBold 16 pt `#F0EDE8`
- `Measures dissolved ions in the rinse water. Higher conductivity = more drag-in contamination remaining. A conductivity meter is the simplest, cheapest rinse quality tool.` Inter Regular 13 pt `#F0EDE8`

Center (X: 8.17", W: 7.33"):
- `HOW TO MEASURE` Barlow SemiBold 16 pt `#2EC4B6`
- `Inline conductivity probe in final rinse stage. Read continuously or spot-check with handheld meter. Target: <50 uS/cm. Alarm at >100 uS/cm.` Inter Regular 13 pt `#F0EDE8`

Right (X: 15.83", W: 7.67"):
- `WHEN IT IS TOO HIGH` Barlow SemiBold 16 pt `#E05C5C`
- `Increase water flow. Check counterflow direction. Verify no cross-contamination from adjacent tanks. Replace water if stagnant.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 6 -- Rinse Efficiency Tips

**Section label:** `IMPROVING RINSE QUALITY` -- Y: 26.7".

**BLOCK F -- 4-Tip Strip (Y: 27.3" to 32.3")**

Four callout cards in a row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 4.8", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.

| Card | X | Title | Detail |
|---|---|---|---|
| 1 | 0.5" | DRAIN TIME | Allow 8-10 sec drain time over cleaning tank before entering rinse. Reduces drag-out volume by 50%+. |
| 2 | 6.33" | SPRAY BARS | Overhead spray rinse headers above the first rinse tank. Dilutes drag-out before immersion. |
| 3 | 12.16" | AGITATION | Air agitation or part movement in rinse. Breaks boundary layer; improves mass transfer. |
| 4 | 18.0" | WATER QUALITY | DI or RO water in final stage. Municipal water in first stage is acceptable. Save good water for the clean side. |

Interior per card:
- Title: Barlow SemiBold, 16 pt, `#2EC4B6`
- Detail: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- EN (High Phos) -- Pre-Activation`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse parameters shown are typical industry values for pre-activation rinsing in electroless nickel processes. Consult your process supplier for application-specific guidance.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse EN High-P Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being boring. The counterflow diagram and conductivity gauge give this poster visual anchors. The contamination table is the real teaching tool -- operators need to understand that rinsing is not just "getting wet" but specifically removing named contaminants that cause named problems. The silicate warning is particularly important for EN shops.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #233 -- Construction Workup v1.0*
*2026-04-26*
