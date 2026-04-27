---
Project: Plating Posters Inc
Poster Number: 261
Title: "Rinse -- Electroless Gold -- Post-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Post-plate rinse for electroless gold (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessGold
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ENIG
---

# Poster #261 -- Construction Workup
## Rinse -- Electroless Gold -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse for electroless gold is unique among all electroless post-plate rinses because of one overriding concern: gold recovery economics. Gold costs $80-100+ per gram. Every milliliter of gold drag-out that goes to waste is real money lost. Production ENIG lines almost universally include a dedicated stagnant "gold recovery" rinse tank before the flowing counterflow rinse. This poster makes gold recovery the hero while covering standard rinse parameters.

Hero visual: gold recovery rinse system schematic showing the stagnant recovery tank, flowing counterflow rinse, and the refining loop.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Gold recovery rinse system hero (Block B):** Schematic of stagnant recovery + counterflow rinse + refining loop.
2. **Rinse parameters table (Block D):** Standard post-plate rinse specs.
3. **Drag-out reduction techniques (Block E):** How to minimize gold loss before the rinse.
4. **Defect grid (Block F):** 4 post-plate rinse-related defects.

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
ZONE 3 -- GOLD RECOVERY RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- DRAG-OUT REDUCTION TECHNIQUES (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 6 of 8 -- Post-Plate` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Gold drag-out is money down the drain -- literally. A recovery rinse captures 60-80% of it before it is lost forever.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Gold-plated surface leaving gold bath  -->  After: Rinsed surface ready for drying / post-treatment`

---

### ZONE 3 -- Gold Recovery Rinse System Hero

**Section label:** `THE GOLD RECOVERY RINSE SYSTEM` -- Y: 4.4".

**BLOCK B -- System Schematic (Y: 5.0" to 14.0")**

Horizontal flow diagram, left to right, showing three tanks plus the refining loop.

**Tank 1 -- Gold Bath (X: 0.5", Y: 6.0", W: 5.0", H: 5.0"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `GOLD BATH` Barlow SemiBold 16 pt `#27AE60`
- Content:
  - `Au 0.5-2.0 g/L` JetBrains Mono 13 pt `#E8A020`
  - `80-90 C` JetBrains Mono 13 pt `#F0EDE8`
  - `Parts exit here with gold drag-out on surfaces` Inter Regular 12 pt `#F0EDE8` at 70%

**Arrow:** 3 pt `#3A4055`, right-pointing. Label above arrow: `Drag-out: 20-50 mL/m2` JetBrains Mono 11 pt `#E8A020`

**Tank 2 -- Recovery Rinse (X: 6.5", Y: 5.5", W: 6.5", H: 6.0"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt, border 2 pt `#E8A020`
- Title: `GOLD RECOVERY RINSE` Barlow SemiBold 18 pt `#E8A020`
- Large callout: `STAGNANT -- NO FLOW` Barlow Condensed ExtraBold 20 pt `#E8A020`
- Content:
  - `DI water -- no flow, no drain` Inter Medium 14 pt `#F0EDE8`
  - `Parts dip for 30-60 sec` JetBrains Mono 13 pt `#F0EDE8`
  - `Gold accumulates over days/weeks` Inter Regular 13 pt `#F0EDE8`
  - `Captures 60-80% of drag-out` Inter Medium 13 pt `#27AE60`
  - `Send to gold refiner when economically viable` Inter Regular 13 pt `#F0EDE8`

**Downward arrow from Tank 2:** `To gold refiner` Inter Medium 12 pt `#E8A020`. Arrow curves down to a refining icon:
- Small rounded rect (X: 7.5", Y: 12.5", W: 4.5", H: 1.2"), fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `GOLD REFINING` Barlow Condensed ExtraBold 14 pt `#E8A020`
- `Recover Au --> return to gold bath or sell` Inter Regular 12 pt `#F0EDE8`

**Arrow from Tank 2 to Tank 3:** 3 pt `#3A4055`, right-pointing.

**Tank 3 -- Counterflow Rinse (X: 14.5", Y: 6.0", W: 8.5", H: 5.0"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `COUNTERFLOW RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Content:
  - `DI counterflow, 2-3 stages` Inter Medium 14 pt `#F0EDE8`
  - `Ambient temperature` JetBrains Mono 13 pt `#F0EDE8`
  - `30-60 sec per stage` JetBrains Mono 13 pt `#F0EDE8`
  - `Removes remaining gold and bath chemicals` Inter Regular 13 pt `#F0EDE8`
  - `Parts must not air-dry before rinse` Inter Medium 12 pt `#E05C5C`

**Arrow from Tank 3:** `To drying / post-treatment` -- right-pointing, 3 pt `#3A4055`.

---

### ZONE 4 -- Rinse Parameters

**Section label:** `POST-PLATE RINSE PARAMETERS` -- Y: 14.7".

**BLOCK D -- Parameters Table (Y: 15.3" to 20.3")**

**Full-width callout (X: 0.5", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"

**Two-column layout inside:**

**Left -- Recovery Rinse (X: 0.8", W: 10.5"):**
- Title: `GOLD RECOVERY RINSE (STAGNANT)` Barlow SemiBold 16 pt `#E8A020`

| Parameter | Value |
|---|---|
| Type | Stagnant DI (no flow) |
| Temperature | Ambient |
| Time | 30-60 seconds |
| Water changes | None -- accumulate gold |
| Monitoring | Track Au concentration by AAS or ICP |
| Trigger for refining | When gold value exceeds refining cost |
| Typical Au buildup | 0.01-0.1 g/L over weeks (volume-dependent) |

**Right -- Counterflow Rinse (X: 12.0", W: 11.0"):**
- Title: `FLOWING COUNTERFLOW RINSE` Barlow SemiBold 16 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Type | DI counterflow, 2-3 stages |
| Temperature | Ambient (cold preferred to stop any residual reaction) |
| Time | 30-60 seconds per stage |
| Conductivity target | <50 uS/cm in final rinse |
| Handling | Do not air-dry between gold bath and rinse |
| Handling | Avoid fingerprint contact on gold surface |
| Handling | Do not stack parts wet (water staining) |

Data: JetBrains Mono 12 pt `#F0EDE8`. Labels: Inter Medium 12 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Drag-Out Reduction Techniques

**Section label:** `REDUCE DRAG-OUT BEFORE IT HAPPENS` -- Y: 20.7".

**BLOCK E -- Techniques Panel (Y: 21.3" to 26.3")**

**Four technique boxes in a 2x2 grid:**

**Box 1 (X: 0.5", Y: 21.3", W: 11.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `WITHDRAWAL SPEED` Barlow SemiBold 16 pt `#27AE60`
- `Slow, controlled withdrawal from gold bath` Inter Regular 14 pt `#F0EDE8`
- `Slower withdrawal = thinner drag-out film = less gold lost` Inter Regular 13 pt `#F0EDE8`
- `10-second dwell time above bath before transfer` JetBrains Mono 13 pt `#F0EDE8`

**Box 2 (X: 12.0", Y: 21.3", W: 11.5", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `AIR KNIFE / DRIP BAR` Barlow SemiBold 16 pt `#27AE60`
- `Air knife above gold bath blows excess solution back into tank` Inter Regular 14 pt `#F0EDE8`
- `Drip bars allow solution to drain back before transfer` Inter Regular 13 pt `#F0EDE8`
- `Reduces drag-out by 30-50%` JetBrains Mono 13 pt `#E8A020`

**Box 3 (X: 0.5", Y: 23.8", W: 11.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `RACK / FIXTURE DESIGN` Barlow SemiBold 16 pt `#E8A020`
- `Minimize cup-shaped features that trap solution` Inter Regular 14 pt `#F0EDE8`
- `Angle parts on rack to promote drainage` Inter Regular 13 pt `#F0EDE8`
- `Design fixtures to minimize gold bath surface area contact` Inter Regular 13 pt `#F0EDE8`

**Box 4 (X: 12.0", Y: 23.8", W: 11.5", H: 2.3"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `WETTING AGENT` Barlow SemiBold 16 pt `#E8A020`
- `Non-ionic wetting agent in gold bath reduces surface tension` Inter Regular 14 pt `#F0EDE8`
- `Lower surface tension = thinner drag-out film` Inter Regular 13 pt `#F0EDE8`
- `Must be gold-bath compatible -- check with supplier` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Defect Grid

**Section label:** `POST-PLATE RINSE DEFECTS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | WATER STAINS ON GOLD | `#E8A020` | Parts air-dried before rinsing; standing water evaporated on surface | Transfer immediately to rinse; do not let parts dry in air |
| R1C2 | FINGERPRINTS ON GOLD | `#E8A020` | Handling freshly plated gold with bare hands | Wear clean nitrile gloves; use fixtures for all handling |
| R2C1 | GOLD SURFACE TARNISH | `#E05C5C` | Contaminated rinse water; sulfide or chloride exposure | Use DI water; check for contamination; rinse quickly |
| R2C2 | EXCESSIVE GOLD LOSS | `#E05C5C` | No recovery rinse; excessive drag-out; wasteful handling | Install recovery rinse; slow withdrawal; air knife; track drag-out |

Card construction: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" (color per defect).

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, defect color
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Electroless Gold -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for electroless gold post-plate rinsing and gold recovery. Gold recovery economics vary by production volume, gold price, and refiner terms. Consult your process supplier and refiner for site-specific guidance. Source: General industry knowledge; IPC-4552B.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Gold Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is all about money. The gold recovery rinse system is the hero because it is the single highest-impact cost-saving measure in any gold plating operation. The schematic in Zone 3 tells the story visually: gold bath -> stagnant recovery rinse (the money saver) -> counterflow rinse -> drying. The refining loop arrow shows the closed-loop economics. The drag-out reduction techniques in Zone 5 are the complementary strategy: reduce what you lose in the first place. Together, recovery + reduction can cut gold chemical costs by 40-60%. This is the poster that pays for itself.

---

*Alaina -- Poster #261 -- Construction Workup v1.0 -- 2026-04-26*
