---
Project: Plating Posters Inc
Poster Number: 161
Title: "Rinse -- Zinc Phosphate -- Pre-Condition"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-02 technical reference (zinc phosphate conversion coating)"
Process Scope: Pre-condition rinse stage for zinc phosphate pretreatment (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPhosphate
  - Rinse
  - ConstructionWorkup
  - ClusterCC02
---

# Poster #161 -- Construction Workup
## Rinse -- Zinc Phosphate -- Pre-Condition

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. This rinse removes alkaline cleaner residues before the surface conditioner. Zinc phosphate rinse quality requirements are significantly tighter than iron phosphate -- alkaline carryover into the conditioner raises pH and deactivates the titanium colloid, which is the single most damaging upstream failure mode in zinc phosphate processing. Counter-flow (2-stage) rinse systems are common on automotive lines.

The hero message: contaminated rinses are the #1 cause of poor zinc phosphate coating. This is not a "just add water" stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse stage diagram (Block B -- HERO):** Cross-section of a two-stage counter-flow rinse showing water flow, overflow, and drag-out dilution.
2. **Water quality panel (Block D):** Conductivity targets, pH targets, counter-flow concept.
3. **Downstream impact callout (Block E):** What happens when this rinse fails -- conditioner death and coarse crystals.
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
ZONE 5 -- DOWNSTREAM IMPACT + COUNTER-FLOW (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING & TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Zinc Phosphate -- Pre-Condition Rinse -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Contaminated rinses are the number-one cause of poor zinc phosphate coating. This stage protects the conditioner -- and the conditioner protects everything downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Alkaline-wet surface carrying cleaner residues  -->  After: Neutral, residue-free surface ready for Ti colloid conditioning`

---

### ZONE 3 -- Rinse Mechanism Hero

**Section label:** `THE PRE-CONDITION RINSE` -- Y: 4.4".

**BLOCK B -- Two-Stage Counter-Flow Rinse Diagram**

Y: 5.0" to 14.0".

**Two tanks side by side (counter-flow concept):**

*Tank 1 -- First Rinse (X: 1.0", Y: 6.0", W: 10.0", H: 5.5"):*
- Rounded rect, fill `#2EC4B6` at 8%, border 2 pt `#2EC4B6`
- Label: `RINSE 1 (FIRST CONTACT)` Barlow SemiBold 14 pt `#2EC4B6`
- Part entering from left with alkaline residue layer (1 pt `#E05C5C`)
- Label: `Heaviest drag-out lands here` Inter Regular 12 pt `#F0EDE8` at 60%
- Parameters inside: `Most contaminated water` JetBrains Mono 12 pt `#E05C5C`

*Tank 2 -- Second Rinse (X: 13.0", Y: 6.0", W: 10.0", H: 5.5"):*
- Rounded rect, fill `#2EC4B6` at 15%, border 2 pt `#2EC4B6`
- Label: `RINSE 2 (FINAL RINSE)` Barlow SemiBold 14 pt `#2EC4B6`
- Part exiting right, clean (border 1 pt `#27AE60`)
- Label: `Cleanest water contacts part last` Inter Regular 12 pt `#27AE60`
- Parameters inside: `Freshest water` JetBrains Mono 12 pt `#27AE60`

**Counter-flow arrows:**
- Arrow from Tank 2 to Tank 1: `Fresh water IN (to Tank 2)` at right side
- Arrow from Tank 1 to drain: `Overflow to drain (from Tank 1)` at left side
- Both arrows: stroke 3 pt `#2EC4B6`, labels Inter Medium 13 pt

**Key parameters (centered below tanks, Y: 12.0"):**
- `Temperature: Ambient to 80 F (27 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Conductivity target: < 300 uS/cm` JetBrains Mono 14 pt `#E8A020`
- `pH after rinse: < 8.0 (must drop below 9.0 minimum)` JetBrains Mono 14 pt `#E8A020`

**Bottom callout (Y: 13.0"):**
- `ALKALINE CARRYOVER RAISES CONDITIONER pH AND DEACTIVATES THE TITANIUM COLLOID. This rinse protects the most critical stage in the entire line.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Water Quality Requirements

**Section label:** `WATER QUALITY -- TIGHTER THAN IRON PHOSPHATE` -- Y: 14.7".

**BLOCK D -- Water Quality Panel (Y: 15.3" to 20.3")**

Two side-by-side callout boxes:

**Left -- Conductivity & pH (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `CONDUCTIVITY & pH` Barlow SemiBold 20 pt `#E8A020`

| Metric | Target | Why |
|---|---|---|
| Conductivity | < 300 uS/cm | Tighter than Fe phosphate (< 500) |
| pH | < 8.0 | Alkaline carryover kills conditioner |
| Rinse ratio | > 15:1 (water:drag-out) | Counter-flow achieves this efficiently |

Note: `Conductivity rising above 500 uS/cm = the conditioner is at risk. Increase overflow or dump and refill.` Inter Regular 13 pt `#F0EDE8` at 60%.

**Right -- Zinc Phosphate vs. Iron Phosphate Rinse Standards (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `WHY TIGHTER SPECS?` Barlow SemiBold 20 pt `#E05C5C`

| Parameter | Fe Phosphate Rinse | Zn Phosphate Rinse |
|---|---|---|
| Conductivity | < 500 uS/cm | < 300 uS/cm |
| pH | < 9.0 | < 8.0 |
| Rinse stages | 1 (or none) | 2 (counter-flow) |
| Consequence of failure | Uneven coating | Dead conditioner + coarse crystals |

Bottom note: `Zinc phosphate is less forgiving at every stage. The rinse quality reflects this.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Downstream Impact + Counter-Flow

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- What Happens When This Rinse Fails (X: 0.5", W: 11.0"):**

Section label: `DOWNSTREAM FAILURE CASCADE` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E05C5C` 0.06".

Content (vertical cascade with arrows):
- `1. Alkaline drag-over enters conditioner` Inter Medium 14 pt `#F0EDE8`
- Arrow down, `#E05C5C`
- `2. Conditioner pH rises above 9.5` Inter Medium 14 pt `#E05C5C`
- Arrow down
- `3. Ti colloid destabilizes and dies` Inter Medium 14 pt `#E05C5C`
- Arrow down
- `4. Fewer nucleation sites on steel surface` Inter Medium 14 pt `#E05C5C`
- Arrow down
- `5. COARSE CRYSTALS (50--100+ um)` Barlow SemiBold 16 pt `#E05C5C`
- `Porous, weak coating. Paint adhesion failure.` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Counter-Flow Rinse System (X: 12.0", W: 11.5"):**

Section label: `COUNTER-FLOW DESIGN` Barlow Condensed ExtraBold 22 pt `#27AE60`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#27AE60` 0.06".

Content:
- `Counter-flow means fresh water enters the LAST tank and overflows backward to the FIRST.` Inter Regular 14 pt `#F0EDE8`
- `Benefits:` Barlow SemiBold 14 pt `#27AE60`
- `Cleanest water contacts the cleanest surface` Inter Regular 13 pt `#F0EDE8`
- `Dirtiest water handles the dirtiest surface` Inter Regular 13 pt `#F0EDE8`
- `Reduces fresh water consumption by 50--70%` Inter Regular 13 pt `#F0EDE8`
- `Standard on automotive OEM lines` Inter Regular 13 pt `#E8A020`
- `Even small shops benefit from a two-tank counter-flow setup.` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Monitoring & Troubleshooting

**Section label:** `RINSE MONITORING` -- Y: 26.7".

**BLOCK F -- Control Table (Y: 27.3" to 30.5")**

| Parameter | Method | Frequency | Target |
|---|---|---|---|
| Conductivity | Conductivity meter | Every 2 hours | < 300 uS/cm |
| pH | pH meter or strip | Every 2 hours | < 8.0 |
| Overflow rate | Flow meter or visual | Continuous | Per system design |
| Temperature | Thermometer | Daily | Ambient to 80 F |

**BLOCK F2 -- Quick Troubleshooting (Y: 31.0" to 32.3")**

Two problem cards side by side:

| Problem | Cause | Fix |
|---|---|---|
| Rinse pH won't drop below 9.0 | Excessive cleaner drag-out, low overflow | Increase overflow; reduce cleaner conc.; add counter-flow |
| Coarse zinc phosphate crystals downstream | Contaminated rinse killing conditioner | Dump and refill rinse tanks; verify conductivity < 300 |

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Zinc Phosphate -- Pre-Condition`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Products Finishing; typical zinc phosphate pretreatment parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Zinc Phosphate Pre-Condition -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This rinse poster carries more weight than its iron phosphate counterpart (Poster #153) because the downstream consequences are far more severe. The failure cascade visualization in Zone 5 is the key differentiator -- showing the chain reaction from alkaline drag-over to dead conditioner to coarse crystals makes the abstract rinse quality requirement concrete and visceral. The counter-flow diagram in the hero zone is unique to this poster and gives operators a clear mental model of how a properly designed rinse system works.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #161 -- Construction Workup v1.0*
*2026-04-26*
