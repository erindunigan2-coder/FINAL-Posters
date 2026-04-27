---
Project: Plating Posters Inc
Poster Number: 77
Title: "Rinse -- Nickel-Cobalt -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Post-plate rinse stage for nickel-cobalt alloy plating. Removes NiCo plating solution drag-out before post-treatment (chromium topcoat, heat treat, or final inspection). Drag-out recovery is economically important -- NiCo bath chemistry is expensive. Stage 6 of 8.
Process Scope: Post-plate rinse for nickel-cobalt alloy plating (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #77 -- Construction Workup
## Rinse -- Nickel-Cobalt -- Post-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse removes NiCo plating solution from the freshly plated parts before post-treatment. This rinse stage has two priorities: (1) thorough removal of plating solution to prevent staining or interference with downstream steps, and (2) drag-out recovery -- NiCo bath chemistry includes expensive cobalt sulfate and nickel sulfamate, so recovering drag-out into a return tank makes economic sense.

Hero visual: rinse station with drag-out recovery tank, multi-stage rinse configuration, and cost callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Rinse station hero with drag-out recovery (Block B):** Two-tank configuration -- drag-out recovery tank + clean rinse tank. Standard construction.
2. **Drag-out recovery economics (Block D):** Cost of lost chemistry per gallon of drag-out vs. cost of recovery tank.
3. **Post-plate surface condition (Block E):** What the NiCo deposit looks like coming out, what to check before moving forward.
4. **Common post-plate rinse failures (Block F):** 4-card strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Teal)
ZONE 3 -- RINSE STATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAG-OUT RECOVERY ECONOMICS (14.5"--20.5" / ~6.0")
ZONE 5 -- POST-PLATE SURFACE CHECK (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON POST-PLATE RINSE FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Post-Plate -- Stage 6 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Cobalt sulfate is not cheap. Every drop of drag-out you lose to the drain is money. Recover what you can, rinse what you must.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Freshly plated NiCo surface with drag-out solution  -->  After: Clean NiCo deposit ready for post-treatment`

---

### ZONE 3 -- Rinse Station Hero

**Section label:** `POST-PLATE RINSE WITH DRAG-OUT RECOVERY` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Two-Tank Configuration**

Y: 5.0" to 14.0".

**Tank 1 -- Drag-Out Recovery (left half):**
- Rounded rect, X: 1.5", Y: 5.5", W: 9.5", H: 7.0"
- Fill: `#252B3D` at 80% (concentrated drag-out solution -- slightly tinted)
- Border: 3 pt `#E8A020`
- Label above: `DRAG-OUT RECOVERY TANK` Barlow SemiBold 16 pt `#E8A020`
- Sub-label: `Static or slow-flow; return to plating bath periodically` Inter Regular 12 pt `#F0EDE8` at 60%

**Parts rack in Tank 1:**
- Vertical rect, X: 5.0", Y: 6.0", W: 3.0", H: 5.5", fill `#27AE60` at 20%, border 2 pt `#27AE60`
- Label: `PARTS (FIRST DIP)` Inter Medium 13 pt `#F0EDE8`

**Return arrow (Tank 1 to plating bath):**
- Arrow from Tank 1 left side, curving back left, stroke 2 pt `#E8A020`
- Label: `Return to NiCo bath` Inter Medium 12 pt `#E8A020`
- Sub-label: `When conductivity builds up` Inter Regular 11 pt `#F0EDE8` at 60%

**Tank 2 -- Clean Rinse (right half):**
- Rounded rect, X: 12.5", Y: 5.5", W: 9.5", H: 7.0"
- Fill: `#252B3D` (clean rinse water)
- Border: 3 pt `#2EC4B6`
- Label above: `CLEAN RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Sub-label: `Flowing overflow; DI or city water` Inter Regular 12 pt `#F0EDE8` at 60%

**Parts rack in Tank 2:**
- Vertical rect, X: 16.0", Y: 6.0", W: 3.0", H: 5.5", fill `#27AE60` at 20%, border 2 pt `#27AE60`
- Label: `PARTS (FINAL RINSE)` Inter Medium 13 pt `#F0EDE8`

**Flow arrow (Tank 1 to Tank 2):**
- Arrow from right side of Tank 1 to left side of Tank 2, stroke 3 pt `#3A4055`
- Label: `Parts transfer` Inter Regular 12 pt `#3A4055`

**Water inlet (Tank 2, bottom):**
- Arrow, stroke 2 pt `#2EC4B6`
- Label: `Fresh water inlet` Inter Medium 12 pt `#2EC4B6`

**Overflow (Tank 2, top-right):**
- Arrow exiting, stroke 2 pt `#2EC4B6`
- Label: `Overflow to drain (or wastewater)` Inter Medium 12 pt `#2EC4B6`

**Bath parameters (inside each tank):**

Tank 1:
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Flow: Static (no overflow)` JetBrains Mono 13 pt `#E8A020`
- `Time: 30--60 sec` JetBrains Mono 13 pt `#F0EDE8`

Tank 2:
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Flow: Continuous overflow` JetBrains Mono 13 pt `#2EC4B6`
- `Time: 30--60 sec` JetBrains Mono 13 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `A single drag-out recovery tank can return 50--70% of drag-out chemistry to the plating bath. For cobalt sulfate at current pricing, this pays for itself in weeks.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Drag-Out Recovery Economics

**Section label:** `THE ECONOMICS OF DRAG-OUT RECOVERY` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- What You Lose (X: 0.5", W: 11.0"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`.

- Title: `WITHOUT RECOVERY` Barlow SemiBold 18 pt `#E05C5C`
- `Drag-out rate: 1--4 gal / 1000 ft2` JetBrains Mono 14 pt `#F0EDE8`
- `Each gallon contains:`
- `  Ni sulfamate: ~350 g/L` JetBrains Mono 12 pt `#2EC4B6`
- `  CoSO4: ~30 g/L` JetBrains Mono 12 pt `#E8A020`
- `  Boric acid: ~40 g/L` JetBrains Mono 12 pt `#F0EDE8`
- `All of it goes to wastewater treatment`
- `You pay for the chemistry AND the treatment`
- Bottom: `Double cost: buy it, then pay to dispose it.` Inter Medium 13 pt `#E05C5C`

**Right -- What You Save (X: 12.0", W: 11.5"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`.

- Title: `WITH RECOVERY` Barlow SemiBold 18 pt `#27AE60`
- `Recovery tank captures 50--70% of drag-out`
- `Periodic return to plating bath via pump or manual transfer`
- `Monitor recovery tank for contamination buildup`
- `When specific gravity approaches 50% of bath, return it`
- `Reduces chemical consumption by 30--50%`
- `Reduces wastewater treatment load and costs`
- Bottom: `The recovery tank is the cheapest piece of equipment on the line with the fastest ROI.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Post-Plate Surface Check

**Section label:** `WHAT TO CHECK BEFORE MOVING FORWARD` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Surface Condition Table (Y: 21.3" to 26.3")**

Column widths (23.0" total):
- Check (5.0") | Good Result (6.0") | Bad Result (6.0") | Action if Bad (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.9".

| Check | Good | Bad | Action |
|---|---|---|---|
| Visual appearance | Uniform semi-bright metallic | Dull, dark, or streaky | Hold -- investigate bath chemistry |
| Adhesion (tape test) | No lifting on cross-hatch tape pull | Deposit lifts or blisters | Activation or strike failure -- strip and replicate |
| Thickness (XRF spot) | Within spec tolerance | Out of tolerance | Adjust CD or plating time |
| Co% (XRF) | Within spec (typically 18--25%) | Out of range | Adjust bath metals, temp, or CD |
| Surface roughness | Smooth to touch, no nodules | Gritty, rough, or nodular | Filter bath; inspect anode bags |
| Staining after rinse | No discoloration, no water spots | Stains or spots visible | Improve rinse quality; use DI water |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.
Good column: `#27AE60`. Bad column: `#E05C5C`. Action column: `#E8A020`.

---

### ZONE 6 -- Common Post-Plate Rinse Failures

**Section label:** `WHAT GOES WRONG` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | STAINING ON DEPOSIT | Plating solution drying on surface before rinse | Move parts to rinse immediately; do not air-dry |
| 2 | 6.33" | CHEMISTRY LOSS | No drag-out recovery; high drag-out rate | Install recovery tank; optimize rack orientation for drainage |
| 3 | 12.16" | CONTAMINATED RECOVERY TANK | Iron, organics, or particulate buildup in return | Monitor recovery tank; filter before return; dump if contaminated |
| 4 | 18.0" | POST-TREATMENT INTERFERENCE | Residual NiCo solution under chromium topcoat | Improve final rinse; add second overflow stage |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

Standard. Title: `Rinse -- Nickel-Cobalt -- Post-Plate`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Rinse configurations and drag-out recovery practices shown are typical industry values. Specific wastewater treatment requirements vary by local regulation. Consult your process supplier for application-specific guidance. Source: General industry knowledge; Metal Finishing Guidebook.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse NiCo Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The post-plate rinse poster differentiates itself from the two upstream rinse posters by focusing on drag-out recovery economics and post-plate quality verification. NiCo chemistry is significantly more expensive than standard nickel or zinc -- the cobalt sulfate alone justifies a recovery system. The surface condition table in Zone 5 bridges the rinse stage to the post-treatment stage, giving operators a checklist before they commit to the next (often irreversible) process step.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #77 -- Construction Workup v1.0*
*2026-04-26*
