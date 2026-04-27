---
Project: Plating Posters Inc
Poster Number: 53
Title: "Rinse -- Zinc-Nickel -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-03 technical reference (zinc-nickel alloy plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Post-plate rinse for zinc-nickel alloy plating. Triple rinse recommended (drag-out recovery + double counterflow). NaOH drag-in from alkaline Zn-Ni bath destroys the subsequent passivation chemistry. Watson brief: "Triple rinse recommended -- drag-out recovery + double counterflow. ZnNi baths are expensive; drag-out recovery is economically justified."
Process Scope: Post-plate rinse for zinc-nickel plating (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincNickelPlating
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP03
---

# Poster #53 -- Construction Workup
## Rinse -- Zinc-Nickel -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse for zinc-nickel is the bridge between plating and passivation. It has two jobs: (1) remove NaOH and Zn-Ni chemistry drag-out before the acidic passivation step, and (2) recover expensive Zn-Ni chemistry via a drag-out recovery tank. Watson's brief is emphatic: "NaOH drag-in destroys passivate."

If alkaline drag-out reaches the trivalent passivation bath (pH 1.5--3.0), it neutralizes the acid, raises pH, and destroys the passivation film quality. The result: poor salt spray, flaking passivate, customer rejections.

Hero visual: triple rinse cascade with drag-out recovery economics and passivation impact callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Triple rinse cascade hero (Block B):** Three tanks -- drag-out recovery + double counterflow.
2. **Passivation impact callout (Block C):** What NaOH drag-in does to the trivalent passivation bath.
3. **Nitric acid bright dip step (Block D):** Optional de-smut between rinse and passivation.
4. **Drag-out recovery economics (Block G):** Cost justification.
5. **Orientation strip:** Stage 6 highlighted (Teal).

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
  Stage 6 highlighted (Teal)
ZONE 3 -- TRIPLE RINSE CASCADE HERO (4.2"--15.0" / ~10.8")
  Block B: Triple rinse cascade diagram
  Block C: Passivation impact callout
ZONE 4 -- RINSE PARAMETERS + BRIGHT DIP (15.0"--21.0" / ~6.0")
  Block D: Rinse parameter table
  Block E: Nitric acid bright dip (optional step)
ZONE 5 -- COMMON FAILURES + HE BAKE TIMING (21.0"--27.0" / ~6.0")
  Block F: Common rinse failures
  Block F2: HE bake timing note
ZONE 6 -- DRAG-OUT ECONOMICS + SAFETY (27.0"--32.5" / ~5.5")
  Block G: Drag-out recovery economics
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Zinc-Nickel -- Stage 6 of 8 -- Post-Plate` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `NaOH into trivalent passivate is a salt spray death sentence. Triple rinse. Recover drag-out. Protect the passivation step.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated Zn-Ni alloy with alkaline drag-out  -->  After: Clean Zn-Ni surface ready for passivation`

---

### ZONE 3 -- Triple Rinse Cascade Hero

**Section label:** `THE TRIPLE RINSE -- PROTECTING THE PASSIVATION` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Triple Rinse Cascade Diagram**

Y: 5.0" to 11.5". Three tank rectangles in sequence.

- Tank 1 -- Drag-Out Recovery (X: 0.5", W: 7.0", H: 5.5"): fill `#252B3D`, border 2 pt `#E8A020`
  - Title: `DRAG-OUT RECOVERY` Barlow SemiBold 16 pt `#E8A020`
  - Parameters (JetBrains Mono 13 pt `#F0EDE8`):
    ```
    Type: Static (no fresh water in)
    Purpose: Capture concentrated Zn-Ni drag-out
    Return: Periodically to plating bath
    Temp: Ambient
    ```
  - Tag: `SAVES CHEMISTRY + REDUCES WASTE` Inter Medium 12 pt `#27AE60`

- Tank 2 -- Rinse 1 (X: 8.25", W: 7.0", H: 5.5"): fill `#252B3D`, border 2 pt `#2EC4B6`
  - Title: `RINSE 1 (OVERFLOW)` Barlow SemiBold 16 pt `#2EC4B6`
  - Parameters:
    ```
    Type: Overflow (cascade to drain)
    Temp: Ambient
    Receives overflow from Tank 3
    ```

- Tank 3 -- Rinse 2 (X: 16.0", W: 7.5", H: 5.5"): fill `#252B3D`, border 2 pt `#27AE60`
  - Title: `RINSE 2 (FINAL)` Barlow SemiBold 16 pt `#27AE60`
  - Parameters:
    ```
    Type: Overflow (fresh water in)
    Temp: Ambient
    Water: DI recommended for appearance parts
    Target: < 100 uS/cm conductivity
    ```
  - Tag: `PARTS EXIT HERE --> TO PASSIVATION` Inter Medium 12 pt `#27AE60`

Arrows: Parts flow left to right. Water flows right to left (counterflow).

**BLOCK C -- Passivation Impact Callout**

Y: 12.0" to 14.8".

- Rounded rect, full width, H: 2.5", fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 8
- Title: `WHAT NaOH DRAG-IN DOES TO TRIVALENT PASSIVATION` Barlow Condensed ExtraBold, 20 pt, `#E05C5C`
- Three-column impact chain:

| NaOH enters passivate | pH rises | Passivation fails |
|---|---|---|
| Alkaline Zn-Ni drag-out (NaOH 100--150 g/L) | Passivate pH rises from 1.5--3.0 to >4.0 locally | Thin, patchy, non-adherent conversion coating |

- Bottom: `Result: Passivate flakes during handling. Salt spray fails at 50% of target. Customer rejection.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Rinse Parameters + Bright Dip

**Section label:** `RINSE PARAMETERS AND OPTIONAL BRIGHT DIP` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Rinse Parameter Table**

Y: 15.8" to 18.5".

| Parameter | Value |
|---|---|
| Rinse configuration | Triple: drag-out recovery + double counterflow |
| Water temperature | Ambient (65--85 F) |
| Water quality (final tank) | DI preferred; municipal < 500 uS/cm acceptable |
| Target conductivity (final tank) | < 100 uS/cm |
| Immersion time per tank | 30--60 sec |
| Agitation | Parts dip or mild air sparging |
| Key risk | NaOH drag-in to passivation bath |

**BLOCK E -- Nitric Acid Bright Dip (Optional)**

Y: 19.0" to 20.8".

Rounded rect, fill `#1E2435`, left accent `#E8A020`, W: 23.0", H: 1.5".
Title: `OPTIONAL: NITRIC ACID BRIGHT DIP / DE-SMUT` Barlow SemiBold 16 pt `#E8A020`
Body (JetBrains Mono 13 pt `#F0EDE8`):
```
0.5--1% v/v HNO3 | Ambient | 10--30 sec
Purpose: Remove surface smut, brighten Zn-Ni deposit before passivation
Note: Not required on all lines -- depends on deposit appearance and passivation type
Rinse immediately after -- do NOT carry HNO3 into passivation
```

---

### ZONE 5 -- Common Failures + HE Bake Timing

**Section label:** `WHAT GOES WRONG` -- Y: 21.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Common Rinse Failures**

Y: 21.8" to 25.5".

| Failure | Root Cause | Result |
|---|---|---|
| NaOH drag-in to passivate | Insufficient rinsing; single rinse | Passivate flakes; fails salt spray |
| No drag-out recovery | Skipped recovery tank | Chemistry wasted to drain; cost increase 15--25% |
| Water staining | DI not used on appearance parts | Staining visible under passivation |
| Parts dry between rinse and passivate | Slow transfer or rack backup | Surface oxidizes; passivation adhesion drops |
| Excess NaOH in rinse water | Rinse water not flowing | Rinse becomes alkaline sump |

Cards: fill `#1E2435`, alternating `#252B3D`. Failure: `#E05C5C`. Root Cause: `#F0EDE8`. Result: `#E8A020`.

**BLOCK F2 -- HE Bake Timing Note**

Y: 25.8" to 26.8".

Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, W: 23.0", H: 0.8".
Text: `HE BAKE NOTE: For high-strength steel (>= 31 HRC), bake BEFORE passivation per ASTM B850. The post-plate rinse must be fast -- parts need to reach the oven within 1--4 hours of plating. Clock is ticking.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Drag-Out Economics + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Drag-Out Recovery Economics (X: 0.5", W: 14.0"):**

Section label: `DRAG-OUT RECOVERY -- THE NUMBERS` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:
- `Zn-Ni baths cost significantly more than plain zinc per gallon.`
- `A barrel line drags out 0.5--2.0 gallons per 1,000 lbs of parts (typical).`
- `A drag-out recovery tank captures 50--80% of this chemistry.`
- `Return the concentrated drag-out to the plating bath weekly or as conductivity indicates.`
- `Payback: 3--6 months on a production line.`
- `Bonus: Reduces waste treatment load and nickel discharge to sewer.`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Rinse water contains NaOH and nickel compounds.
> - Nickel: dermal sensitizer. Avoid prolonged skin contact.
> - Drain rinse water to waste treatment -- never to sanitary sewer.
> - If bright dip (HNO3) is used: nitric acid is a strong oxidizer. Fumes are toxic.
> - PPE: gloves, goggles, apron for all rinse/bright dip work.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Zinc-Nickel -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #47).
**Export:** Six files -- `Rinse Zinc-Nickel Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The passivation impact callout (Block C) is the emotional anchor of this poster. Shops that cut rinse stages to save floor space or water cost pay for it in salt spray failures and customer rejections. The message must be blunt: NaOH drag-in destroys passivation. Period.

The HE bake timing note is included here (not just on the post-treatment poster) because the clock starts at the end of plating -- the rinse stage is where operators first need to be aware that time is running.

Watson's brief: "Triple rinse recommended -- drag-out recovery + double counterflow. ZnNi baths are expensive; drag-out recovery is economically justified."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #53 -- Construction Workup v1.0*
*2026-04-26*
