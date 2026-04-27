---
Project: Plating Posters Inc
Poster Number: 153
Title: "Rinse -- Iron Phosphate -- Pre-Condition"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-01 technical reference (iron phosphate conversion coating)"
Process Scope: Pre-condition rinse stage for iron phosphate pretreatment (Stage 2)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IronPhosphate
  - Rinse
  - ConstructionWorkup
  - ClusterCC01
---

# Poster #153 -- Construction Workup
## Rinse -- Iron Phosphate -- Pre-Condition

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 6. This rinse removes alkaline cleaner residues before the phosphate stage. In 3-stage systems this rinse does not exist -- the phosphate bath must tolerate some cleaner drag-over. In 1-stage cleaner-coaters, there is no rinse at all. This poster covers water quality, conductivity monitoring, and the impact of hard water on downstream phosphate quality.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse stage diagram (Block B -- HERO):** Cross-section of rinse tank showing water flow, overflow, and drag-out dilution concept.
2. **Water quality panel (Block D):** Conductivity targets, pH targets, hardness impact.
3. **System configuration context (Block E):** Where this rinse fits in 1/3/5-stage systems.
4. **Monitoring table (Block F):** Rinse quality control parameters.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WATER QUALITY REQUIREMENTS (14.5"--20.5" / ~6.0")
ZONE 5 -- SYSTEM CONFIGURATION CONTEXT (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING & TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Iron Phosphate -- Pre-Condition Rinse -- Stage 2 of 6` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Cheap water now or expensive rejects later. The rinse between cleaning and coating sets the floor for everything downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline-wet surface carrying cleaner residues  -->  After: Neutral, residue-free surface ready for phosphate`

---

### ZONE 3 -- Rinse Mechanism Hero

**Section label:** `THE PRE-CONDITION RINSE` -- Y: 4.4".

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 6.0", W: 20.0", H: 6.0", fill `#2EC4B6` at 10%, border 2 pt `#2EC4B6`
- Label: `FRESH WATER RINSE TANK` Barlow SemiBold 16 pt `#2EC4B6`

**Incoming water (top left):**
- Arrow from left, stroke 3 pt `#2EC4B6`
- Label: `Fresh water in` Inter Medium 14 pt `#2EC4B6`
- Sub-label: `1--3 gal/min continuous overflow` JetBrains Mono 13 pt `#F0EDE8`

**Overflow weir (top right):**
- Arrow exiting right, stroke 3 pt `#3A4055`
- Label: `Overflow to drain` Inter Medium 14 pt `#3A4055`
- Sub-label: `Carries away cleaner drag-out` Inter Regular 12 pt `#F0EDE8` at 60%

**Part entering (left side of tank):**
- Rectangle representing part, fill `#C8D0D8` at 50%, border 1 pt `#E05C5C`
- Label above: `Alkaline residue on surface` Inter Regular 13 pt `#E05C5C`
- Small "film" layer: 1 pt line `#E05C5C` on part surface

**Part exiting (right side of tank):**
- Rectangle representing part, fill `#C8D0D8`, border 1 pt `#27AE60`
- Label above: `Clean, neutral surface` Inter Regular 13 pt `#27AE60`

**Key parameters (inside tank, centered):**
- `Temperature: Ambient to 80 F (27 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Overflow: 1--3 gal/min` JetBrains Mono 14 pt `#2EC4B6`
- `Conductivity target: < 500 uS/cm` JetBrains Mono 14 pt `#E8A020`
- `pH after rinse: < 9.0` JetBrains Mono 14 pt `#E8A020`

**Bottom callout (Y: 13.0"):**
- `IF pH STAYS ABOVE 9.0: Cleaner drag-over is excessive. Increase overflow rate, check upstream rinse, or reduce cleaner concentration.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Water Quality Requirements

**Section label:** `WATER QUALITY -- THE HIDDEN VARIABLE` -- Y: 14.7".

**BLOCK D -- Water Quality Panel (Y: 15.3" to 20.3")**

Two side-by-side callout boxes:

**Left -- Conductivity & pH (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `CONDUCTIVITY & pH` Barlow SemiBold 20 pt `#E8A020`

| Metric | Target | Why |
|---|---|---|
| Conductivity | < 500 uS/cm | Below 200 uS/cm is ideal |
| pH | < 9.0 | High pH = cleaner carry-over |
| Rinse ratio | > 10:1 (water:drag-out) | Lower ratio = contaminated rinse |

Note: `Rising conductivity = bath is contaminated. Increase overflow or dump and refill.` Inter Regular 13 pt `#F0EDE8` at 60%.

**Right -- Hard Water Impact (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `HARD WATER WARNING` Barlow SemiBold 20 pt `#E05C5C`

Content:
- `Hardness > 150 ppm (Ca/Mg)` JetBrains Mono 14 pt `#E05C5C`
- `Calcium and magnesium interfere with iron phosphate film formation.` Inter Regular 14 pt `#F0EDE8`
- `Softened or DI water is recommended for rinse stages in hard-water areas.` Inter Medium 14 pt `#F0EDE8`
- `If water spots appear on parts after rinsing, hardness is too high.` Inter Regular 13 pt `#F0EDE8` at 70%

---

### ZONE 5 -- System Configuration Context

**Section label:** `WHERE THIS RINSE FITS` -- Y: 20.7".

**BLOCK E -- Three Configuration Cards (Y: 21.3" to 26.3")**

Three cards in a row:

| Card | X | W | Config | Rinse Status | Detail |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | 1-STAGE (Cleaner-Coater) | NO RINSE | Combined chemistry. No rinse exists. Coating weight lighter (15--40 mg/ft2). |
| 2 | 8.16" | 7.33" | 3-STAGE | NO PRE-COAT RINSE | Clean --> Phosphate --> Seal. Phosphate must tolerate cleaner drag-over. |
| 3 | 15.83" | 7.67" | 5-STAGE | THIS RINSE EXISTS | Clean --> Rinse --> Phosphate --> Rinse --> Seal. Best coating quality. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6.

Card 1 accent: `#3A4055` (dimmed -- no rinse). Card 2 accent: `#E8A020` (caution). Card 3 accent: `#27AE60` (optimal -- this poster applies).

Config label: Barlow SemiBold 18 pt in accent color. Status: Barlow Condensed ExtraBold 14 pt. Detail: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Monitoring & Troubleshooting

**Section label:** `RINSE MONITORING` -- Y: 26.7".

**BLOCK F -- Control Table (Y: 27.3" to 30.5")**

| Parameter | Method | Frequency | Target |
|---|---|---|---|
| Conductivity | Conductivity meter | Every 2 hours | < 500 uS/cm (< 200 ideal) |
| pH | pH meter or strip | Every 2 hours | < 9.0 |
| Overflow rate | Flow meter or visual | Continuous | 1--3 gal/min |
| Temperature | Thermometer | Daily | Ambient to 80 F |

**BLOCK F2 -- Quick Troubleshooting (Y: 31.0" to 32.3")**

Two problem cards side by side:

| Problem | Cause | Fix |
|---|---|---|
| Rinse pH won't drop below 9.0 | Excessive cleaner drag-out, low overflow | Increase overflow; reduce cleaner conc.; add counter-flow |
| Phosphate coating uneven downstream | Contaminated rinse water carrying salts | Dump and refill rinse tank; check water supply |

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Iron Phosphate -- Pre-Condition`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Iron Phosphate Pre-Condition -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters are inherently less visually dramatic than coating or cleaning posters. The hero here is the flow diagram showing the dilution principle -- fresh water in, contaminated water out, part cleaned in between. The hard water warning and configuration context are what give this poster real shop-floor value.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #153 -- Construction Workup v1.0*
*2026-04-26*
