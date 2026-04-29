---
Project: Plating Posters Inc
Poster Number: 149
Title: "Rinse -- Tin-Lead -- Post-Plate"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 149 -- Rinse -- Tin-Lead Post-Plate -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - TinLeadPlating
  - Rinse
  - PostPlate
  - ClusterEP15
  - v1
---

# Claude Chat Generation Prompt -- Poster #149
## Rinse -- Tin-Lead -- Post-Plate
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone.

---

## Phase 2 -- Header

### Step 1 -- `RINSE` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Tin-Lead Plating -- Post-Plate -- Stage 6 of 8` -- `36` pt `#2EC4B6`. Y: **1.5"**.
### Step 3 -- `Fast rinse to prevent surface oxidation. Segregated waste because the rinse water contains lead. Speed and compliance -- both mandatory.` -- `22` pt at 65%. Y: **2.2"**.

---

## Phase 3 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated solder with acid drag-out  -->  After: Clean solder surface ready for reflow or dry`

---

## Phase 4 -- Fast Rinse Hero

Y: 4.2" to 14.5". Section: `RINSE FAST -- SOLDER OXIDIZES IN AIR`.

Tank: rounded rect X: 2.0", Y: 5.5", W: 20.0", H: 7.0", fill `#252B3D`, border 2 pt `#2EC4B6`.

- **Timer** (upper-right): circle 2.5" diameter, fill `#1E2435`, border 2 pt `#E05C5C`. `< 30 sec` 24pt `#E05C5C` / `transfer time`
- **Arrow** above tank: 4 pt `#E8A020`. `IMMEDIATE TRANSFER`
- **Lead waste warning** (inside tank): rounded rect fill `#E05C5C` at 20%, border 2 pt `#E05C5C`. `LEAD-BEARING RINSE WATER -- SEGREGATE FROM ALL OTHER WASTE STREAMS` / `40 CFR 433: Pb discharge limit 0.43 mg/L daily max`
- **Two-stage rinse** divided by dashed line: `STAGE 1 (drag-out recovery)` `#E8A020` / `STAGE 2 (fresh DI rinse)` `#2EC4B6`
- Params: `Temperature: Ambient` / `Water: DI recommended` / `Flow: Continuous overflow (stage 2)` / `Time: 30--60 sec per stage` / `Stages: Double counterflow`

Bottom: `Double counterflow rinse: first stage captures drag-out for lead-bearing recovery. Second stage provides clean DI rinse for post-treatment.` `#27AE60`

---

## Phase 5 -- Drag-Out Recovery

Y: 14.5" to 20.5". Section: `DRAG-OUT RECOVERY -- SAVE YOUR CHEMISTRY AND YOUR ENVIRONMENT`.

Full-width panel, fill `#1E2435`. Three columns:

| Column | Header Color | Header | Content |
|---|---|---|---|
| Left | `#E8A020` | THE COST | Tin-lead chemistry is expensive. Every rack carries 0.1--0.5 mL/sq ft. Lead compounds are especially costly to dispose of as hazardous waste. |
| Center | `#27AE60` | THE RECOVERY | First rinse stage captures concentrated drag-out. Lead-bearing solution can be returned to bath if clean, reducing both cost and hazardous waste. |
| Right | `#2EC4B6` | THE METHOD | Stagnant recovery rinse --> test Sn/Pb --> verify no Cu or Fe --> add back to bath. Use DI water. Track volume. |

Bottom: `Drag-out recovery on a tin-lead line is not just cost savings -- it is hazardous waste reduction. Two wins in one step.` `#E8A020`

---

## Phase 6 -- Lead Waste Segregation

Y: 20.5" to 26.5". Section: `LEAD WASTE -- REGULATORY NON-NEGOTIABLE`.

Full-width coral-bordered panel: fill `#1E2435`, left accent `#E05C5C`. Title: `LEAD-BEARING RINSE WATER IS REGULATED HAZARDOUS WASTE` 22pt `#E05C5C`.

Three columns inside:

**THE LAW (`#E05C5C`):** Lead discharge limit 0.43 mg/L daily max (40 CFR 433). Lead sludge may be F006 hazardous waste. State limits may be stricter. Manifesting/tracking/disposal docs required.

**WHAT TO DO (`#E8A020`):** Segregate all tin-lead rinse water. Treat by hydroxide precipitation pH 9--10. Lead hydroxide settles as sludge -- filter and contain. Test effluent before discharge. Record all waste manifests.

**MSA HELPS (`#27AE60`):** MSA is biodegradable -- minimal BOD concern. No fluoride treatment required (unlike fluoborate). Simpler waste treatment overall. Lead is still the controlling contaminant regardless of acid.

Bottom: `Lead waste compliance is not optional. The plating line manager and the environmental compliance officer must be aligned.` `#E05C5C`

---

## Phase 7 -- Rinse Metrics and Timing

Y: 26.5" to 32.5". Section: `RINSE METRICS AND TIMING`.

Four cards, W: 5.5", H: 4.5", fill `#1E2435`.

| Card | X | Metric | Target | Notes |
|---|---|---|---|---|
| 1 | 0.5" | TRANSFER TIME | < 30 sec from bath to rinse | Start timing at rack lift |
| 2 | 6.33" | RINSE pH | 5.0--7.0 | Acid residue should wash off quickly |
| 3 | 12.16" | CONDUCTIVITY | < 50 uS/cm (clean stage) | Recovery stage will be higher |
| 4 | 18.0" | LEAD IN EFFLUENT | < 0.43 mg/L | Test before discharge -- always |

Cards 1--3: top accent `#2EC4B6`. Card 4: top accent `#E05C5C` (regulatory).

---

## Phase 8 -- Footer

Standard. Title: `Rinse -- Tin-Lead -- Post-Plate`. Version `v1.0 -- 2026`.

---

## Phase 9 -- Review

- [ ] Headline `RINSE` 88pt
- [ ] Stage 6 highlighted
- [ ] Timer graphic (< 30 sec) in hero
- [ ] Lead waste segregation warning prominent inside tank
- [ ] Two-stage rinse layout (recovery + clean)
- [ ] Three-column drag-out recovery panel
- [ ] Full lead waste regulatory panel
- [ ] Card 4 accent override to coral (regulatory)
- [ ] Footer standard

---

## Phase 10 -- Light Remap & Export

Standard remap. Lead waste panels: verify coral legibility.

Six files: `Rinse Tin-Lead Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
