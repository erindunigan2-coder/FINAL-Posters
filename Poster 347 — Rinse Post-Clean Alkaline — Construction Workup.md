---
Project: Plating Posters Inc
Poster Number: 347
Title: "Rinse -- Post-Clean (Alkaline)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-1.5)"
Process Scope: Post-clean rinse requirements, monitoring, and drag-out recovery for alkaline soak cleaning
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - AlkalineCleaning
  - Rinse
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT01
---

# Poster #347 -- Construction Workup
## Rinse -- Post-Clean (Alkaline)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 5 of 7 in the CT-01 cluster. The rinse poster. Rinsing is the most neglected step on every plating line -- operators treat it as dead time between the "real" steps. This poster makes the case that rinsing IS a process step with measurable quality criteria. The hero visual is a counterflow rinse cascade diagram showing how multi-stage rinsing works. The monitoring section gives operators numbers to hit (pH, conductivity). The drag-out recovery section shows how a still rinse before the running rinse saves chemistry and money.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Counterflow cascade diagram (Block B -- HERO):** Three rinse tanks in series with arrows showing water flow direction (counter to part movement). Built with rectangles, arrows, and labels.
2. **Rinse monitoring panel (Block D):** pH and conductivity targets with pass/fail thresholds.
3. **Drag-out recovery callout (Block E):** Still rinse economics.
4. **Rinse quality decision tree (Block F):** Simple yes/no flow for "is my rinse adequate?"

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 5 of 7 highlighted (Teal)
ZONE 3 -- COUNTERFLOW RINSE DIAGRAM / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- RINSE MONITORING (15.0"--21.0" / ~6.0")
ZONE 5 -- DRAG-OUT RECOVERY (21.0"--27.0" / ~6.0")
ZONE 6 -- RINSE QUALITY DECISION TREE (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `THE RINSE STEP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Post-Clean Rinse -- The Step Everyone Ignores Until It Ruins the Job` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `A perfect clean means nothing if you carry the cleaner into the next tank. Rinse quality is process quality.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts coated with alkaline cleaner drag-out --> After: Parts rinsed to near-neutral pH, ready for next step`

---

### ZONE 3 -- Counterflow Rinse Diagram (HERO)

**Section label:** `HOW COUNTERFLOW RINSING WORKS` -- Y: 4.4".

**BLOCK B -- Three-Tank Cascade Diagram**

Y: 5.0" to 14.5".

**Three rinse tanks in a row (left to right):**

| Tank | X | Label | Type | Fill |
|---|---|---|---|---|
| Tank 1 -- Drag-Out (Still) | 1.0" | `DRAG-OUT RINSE` `(Still -- No Overflow)` | Recovery | `#252B3D` fill, `#E8A020` border |
| Tank 2 -- First Running Rinse | 8.5" | `RUNNING RINSE 1` `(Counterflow)` | Active | `#252B3D` fill, `#2EC4B6` border |
| Tank 3 -- Final Rinse | 16.0" | `FINAL RINSE` `(Fresh Water In)` | Final | `#252B3D` fill, `#27AE60` border |

Each tank: Rounded rect W: 6.5", H: 5.5", border 2 pt.

**Part movement arrows (top, left to right):**
- Large arrows above tanks pointing RIGHT: `PARTS MOVE THIS WAY -->` Barlow SemiBold 16 pt `#F0EDE8`
- Arrow color: `#3A4055`, stroke 3 pt, arrowhead right

**Water flow arrows (bottom, right to left):**
- Large arrows below tanks pointing LEFT: `<-- CLEAN WATER FLOWS THIS WAY` Barlow SemiBold 16 pt `#2EC4B6`
- Arrow color: `#2EC4B6`, stroke 3 pt, arrowhead left

**Inside each tank:**

*Tank 1 -- Drag-Out:*
- Concentration label: `HIGH cleaner concentration` JetBrains Mono 13 pt `#E8A020`
- Note: `No overflow -- captures 50-70% of cleaner drag-out` Inter Regular 12 pt `#F0EDE8`
- Action: `Return to cleaner tank periodically` Inter Medium 12 pt `#E8A020`

*Tank 2 -- Running Rinse 1:*
- Concentration: `MODERATE dilution` JetBrains Mono 13 pt `#2EC4B6`
- Note: `Overflow feeds backward (counterflow)` Inter Regular 12 pt `#F0EDE8`
- Target: `pH < 10` JetBrains Mono 14 pt `#F0EDE8`

*Tank 3 -- Final Rinse:*
- Concentration: `LOW -- near clean water` JetBrains Mono 13 pt `#27AE60`
- Note: `Fresh water inlet here` Inter Regular 12 pt `#F0EDE8`
- Target: `pH < 9.0 (target)` JetBrains Mono 14 pt `#27AE60`
- Sub-target: `Conductivity < 200 uS/cm` JetBrains Mono 13 pt `#27AE60`

**Bottom callout (Y: 13.0"):**
- Rounded rect W: 23.0", H: 1.2", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Title: `THE COUNTERFLOW PRINCIPLE` Barlow SemiBold 14 pt `#2EC4B6`
- Text: `Parts move from dirty to clean. Water moves from clean to dirty. Each stage dilutes further. The final rinse sees the least contamination and uses the least water. This is why counterflow rinsing uses 5-10x less water than a single overflow rinse at the same cleanliness level.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Rinse Monitoring

**Section label:** `MEASURING RINSE QUALITY -- NUMBERS, NOT GUESSWORK` -- Y: 15.2".

**BLOCK D -- Two-Column Monitoring Panel (Y: 15.8" to 20.8")**

**Left -- pH Monitoring (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `pH` Barlow Condensed ExtraBold 28 pt `#2EC4B6`

Visual: Horizontal bar showing pH scale 7 to 14.
- Green zone: 7.0-9.0 (fill `#27AE60` at 40%) labeled `GOOD`
- Yellow zone: 9.0-10.0 (fill `#E8A020` at 30%) labeled `MARGINAL`
- Red zone: 10.0-14.0 (fill `#E05C5C` at 30%) labeled `INADEQUATE RINSE`

Key values:
- `Final rinse pH < 9.0 = adequate rinse` JetBrains Mono 14 pt `#27AE60`
- `Persistent pH > 9.5 = increase water flow or add rinse stage` JetBrains Mono 12 pt `#E05C5C`

**Right -- Conductivity Monitoring (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `CONDUCTIVITY` Barlow Condensed ExtraBold 28 pt `#E8A020`

- `Target: < 200 microsiemens/cm` JetBrains Mono 16 pt `#27AE60`
- `200-500 uS/cm: marginal -- increase flow` JetBrains Mono 13 pt `#E8A020`
- `> 500 uS/cm: poor rinse -- investigate` JetBrains Mono 13 pt `#E05C5C`

Note: `Conductivity meters are cheap and give instant feedback. pH strips work but are slower and less precise.` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Drag-Out Recovery

**Section label:** `DRAG-OUT RECOVERY -- SAVE CHEMISTRY, SAVE MONEY` -- Y: 21.2".

**BLOCK E -- Economics Panel (Y: 21.8" to 26.8")**

Rounded rect, full width, H: 4.5", fill `#1E2435`.

**Three-column layout inside:**

| Column | Content |
|---|---|
| Left (W: 7.0") | `WHAT IS DRAG-OUT?` Barlow SemiBold 16 pt `#E8A020`. Body: `Drag-out is the cleaner solution clinging to parts and racks as they leave the tank. Typical: 50-200 mL per m2 of surface area. This is your chemistry leaving the building.` |
| Center (W: 7.0") | `THE STILL RINSE TRICK` Barlow SemiBold 16 pt `#2EC4B6`. Body: `A still (non-flowing) rinse tank immediately after the soak clean captures 50-70% of drag-out. Return this concentrated rinse to the cleaner tank periodically. Cost: one extra tank. Savings: 50-70% chemistry reduction.` |
| Right (W: 7.0") | `DRAG-OUT MATH` Barlow SemiBold 16 pt `#27AE60`. Body: JetBrains Mono 13 pt: `At 100 mL/m2 drag-out:` / `1000 m2/day production =` / `100 L/day cleaner lost` / `x 250 days/year =` / `25,000 L/year` / `Still rinse recovers ~15,000 L` |

---

### ZONE 6 -- Rinse Quality Decision Tree

**Section label:** `IS MY RINSE ADEQUATE? -- A 30-SECOND CHECK` -- Y: 27.2".

**BLOCK F -- Decision Flow (Y: 27.8" to 32.3")**

Simple vertical decision tree:

Step 1: Diamond -- `Final rinse pH < 9.0?`
- YES (right, `#27AE60`): `Rinse is adequate for most processes`
- NO (down, `#E05C5C`): Go to Step 2

Step 2: Diamond -- `Conductivity < 200 uS/cm?`
- YES: `Rinse is acceptable -- pH may be elevated by CO2 absorption (rare)`
- NO: Go to Step 3

Step 3: Action box -- `INCREASE RINSE QUALITY`
- `Add rinse stage`
- `Increase water flow rate`
- `Check for cross-contamination from adjacent tanks`
- `Consider counterflow if using single overflow`

Diamonds: W: 4.0", H: 1.5", fill `#E8A020` at 20%, border 1 pt `#E8A020`.
Action box: Rounded rect W: 10.0", H: 2.5", fill `#1E2435`, left accent `#E05C5C`.
Text: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Post-Clean (Alkaline)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Metal Finishing Guidebook. Rinse ratio and conductivity targets are guidelines -- specific requirements vary by downstream process sensitivity.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Clean Alkaline -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters are deceptively important. Most plating defects trace back to bad rinsing, not bad plating. The counterflow cascade diagram is the hero because it visualizes a concept that most operators misunderstand -- they think rinsing means "dunk in water" when it actually means "dilute to a measurable threshold." The drag-out recovery section gives supervisors a cost argument for adding a still rinse tank. The decision tree gives the lab tech a quick yes/no path for rinse adequacy.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #347 -- Construction Workup v1.0*
*2026-04-26*
