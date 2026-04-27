---
Project: Plating Posters Inc
Poster Number: 697
Title: "Rinse / Dry -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.4)"
Process Scope: Rinse and dry for coil coating -- Stage 3 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - RinseDry
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #697 -- Construction Workup
## Rinse / Dry -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 9. Rinse the cleaner off, dry the strip, and preheat it for conversion coating. Two-stage counterflow DI rinse brings conductivity below 30 uS/cm. IR or convection dryer takes the strip to 100-120 F -- bone dry and slightly warm. Any water droplets left on the strip cause uneven conversion coating, which means uneven adhesion, which means warranty claims on a million square feet of building panels.

Hero visual: counterflow rinse diagram showing water flow direction opposite to strip travel, paired with a dryer section showing the strip entering the conversion coating stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Counterflow rinse diagram (Block B -- left):** Two-stage rinse with water flow arrows showing counterflow direction vs. strip travel.
2. **Dryer section diagram (Block B -- right):** IR or convection dryer with strip exiting dry and warm.
3. **Rinse water quality table (Block D):** Conductivity targets and monitoring frequency.
4. **Defect strip (Block F):** 4 rinse/dry defects.

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
  Stage 3 highlighted (Teal)
ZONE 3 -- COUNTERFLOW RINSE + DRYER HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE WATER QUALITY TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- DRYING AND PREHEAT DETAIL (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE / DRY DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stage 3 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Two rinse stages. One dryer. Zero tolerance for water droplets. The strip must enter conversion coating bone-dry and warm -- or the treatment will be uneven across the entire coil.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned strip with cleaner residuals  -->  After: Dry, warm strip at 100-120 F ready for conversion coating`

---

### ZONE 3 -- Counterflow Rinse + Dryer Hero

**Section label:** `COUNTERFLOW RINSE + PREHEAT DRY` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Split Hero (Two Panels)**

Y: 5.0" to 14.0".

**Left panel -- Counterflow Rinse (X: 0.5", W: 12.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `TWO-STAGE COUNTERFLOW RINSE` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Diagram (Y: 6.0" to 11.0"):
- Horizontal strip line (left to right), `#C8D0D8`, labeled `STRIP TRAVEL -->`
- Two rinse zones stacked along the strip:

Rinse Zone 1 (first contact):
- Spray nozzles above and below, fill `#2EC4B6` at 30%
- Label: `RINSE 1 (USED WATER)` JetBrains Mono 12 pt `#F0EDE8`
- Arrow showing water flowing LEFT (opposite to strip) from Zone 2

Rinse Zone 2 (final contact):
- Spray nozzles above and below, fill `#27AE60` at 30%
- Label: `RINSE 2 (FRESH DI)` JetBrains Mono 12 pt `#27AE60`
- Arrow: `FRESH DI IN` pointing into Zone 2

Water flow arrow below: `<-- WATER FLOW (COUNTERFLOW)` `#E8A020`
Strip flow arrow above: `STRIP TRAVEL -->` `#C8D0D8`

Callout below diagram:
- `Counterflow = fresh water enters the LAST rinse stage, overflows backward to the first. The strip always meets the cleanest water last.` -- Inter Regular 13 pt `#F0EDE8`

**Right panel -- Dryer Section (X: 13.0", W: 10.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `DRYER / PREHEAT` -- Barlow SemiBold, 20 pt, `#E8A020`

Diagram (Y: 6.0" to 10.0"):
- Strip passing through a simplified oven box
- Heat waves/arrows from IR elements or convection blowers
- Temperature callout: `100-120 F strip temp` JetBrains Mono 14 pt `#E8A020`

Parameters below diagram:
- `IR pre-heater or convection dryer` -- Inter Regular 13 pt
- `Removes ALL surface moisture` -- Inter Medium 13 pt `#E8A020`
- `Slight preheat improves conversion coating reactivity` -- Inter Regular 13 pt
- `Water droplets = uneven treatment = adhesion failure` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 4 -- Rinse Water Quality Table

**Section label:** `RINSE WATER TARGETS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Quality Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Parameter (5.0") | Stage 1 (5.5") | Stage 2 (Final) (5.5") | Why (7.0")

| Parameter | Stage 1 | Stage 2 (Final) | Why |
|---|---|---|---|
| Water source | Overflow from Stage 2 | Fresh DI water | Counterflow conserves water |
| Conductivity target | < 200 uS/cm | < 30 uS/cm | High TDS deposits salts that cause adhesion failure |
| pH | 7-9 (carryover from cleaner) | 6.5-7.5 (neutral DI) | Alkaline carryover interferes with conversion coating |
| Flow rate | Overflow from Stage 2 | Per line speed and strip width | Must maintain conductivity target |
| Monitoring | Conductivity meter (continuous) | Conductivity meter (continuous) | Alarm if target exceeded |
| Temperature | Ambient | Ambient | No heating needed for rinse |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

Footnote: `Counterflow rinse design reduces DI water consumption by 40-60% compared to single-pass rinse at equivalent conductivity targets.` -- Inter Regular, 12 pt, `#2EC4B6`

---

### ZONE 5 -- Drying and Preheat Detail

**Section label:** `DRYING -- WHY BONE-DRY MATTERS AT LINE SPEED` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Detail Panel**

Y: 21.3" to 26.3".

**Left -- Dryer Types (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `DRYER OPTIONS` -- Barlow SemiBold, 18 pt, `#E8A020`

| Type | Mechanism | Advantages |
|---|---|---|
| IR pre-heater | Infrared radiant heat directly on strip | Fast response; compact; efficient for thin gauge |
| Convection dryer | Hot air blown across strip surface | Even drying; good for heavier gauge |
| Combination (IR + convection) | IR for rapid surface dry, convection for through-heat | Best of both; most modern lines |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Preheat Benefits (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `WHY PREHEAT TO 100-120 F` -- Barlow SemiBold, 18 pt, `#27AE60`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Removes all surface moisture -- eliminates water spotting`
- `Warm surface improves conversion coating chemical reactivity`
- `Ti/Zr nanoceramic chemistry works better on warm metal`
- `Prevents condensation if ambient humidity is high`
- `Strip must be completely dry BEFORE conversion coating contact`
- `Undried spots produce visible adhesion failures in the finished coil`

---

### ZONE 6 -- Rinse / Dry Defects

**Section label:** `WHAT GOES WRONG -- 4 RINSE / DRY DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | UNEVEN CONVERSION COATING | Water droplets on strip entering treatment | Verify dryer temperature; check for blocked IR elements or air nozzles |
| 2 | 6.33" | SALT DEPOSITS ON STRIP | High-TDS rinse water (conductivity above target) | Check DI system; verify counterflow is functioning; replace DI resin |
| 3 | 12.16" | ALKALINE CARRYOVER | Insufficient rinse removing cleaner residuals | Increase rinse flow rate; verify spray nozzle coverage across full width |
| 4 | 18.0" | STRIP TOO HOT (> 150 F) | Dryer overheating at reduced line speed | Interlock dryer output to line speed; reduce heat during slowdowns |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `At 400 ft/min, a water droplet that survives the dryer becomes a 400-foot streak of uneven conversion coating. The dryer is not optional -- it is the gatekeeper for every quality attribute downstream.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The counterflow diagram is the visual anchor -- the arrows showing water flowing opposite to strip travel make the concept click instantly. Counterflow is one of those engineering solutions that seems obvious once you see it but is poorly understood by many operators. The dryer panel drives home that "bone dry" is not aspirational, it is mandatory. The callout about a single surviving water droplet becoming a 400-foot streak at line speed is the kind of practical wisdom that makes someone nod and remember.

---

*Alaina -- Poster #697 -- Construction Workup v1.0 -- 2026-04-26*
