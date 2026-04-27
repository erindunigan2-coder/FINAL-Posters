---
Project: Plating Posters Inc
Poster Number: 83
Title: "Rinse -- Chrome (Decorative) -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-07 technical reference (decorative chrome plating)"
Technical Source: Pre-plate rinse in decorative chrome -- single rinse between activation and chrome bath. Often skipped entirely when using in-tank activation. When present, must be fast to prevent re-passivation.
Process Scope: Pre-plate rinse -- Stage 4 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ChromePlating
  - Decorative
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - ClusterEP07
---

# Poster #83 -- Construction Workup
## Rinse -- Chrome (Decorative) -- Pre-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This rinse sits between the activation acid dip and the chrome plating bath. Its purpose: remove acid drag-out so it does not contaminate the chrome bath. The catch: this rinse is often skipped entirely when shops use in-tank activation (no separate acid dip = no acid to rinse off). When it does exist, it must be fast -- the activated nickel surface is re-passivating.

Hero visual: a decision tree showing when this rinse is needed vs. when it is skipped, with a rinse tank cross-section for the "needed" path.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Decision tree hero (Block B):** "Do you have a separate activation tank?" Yes -> rinse needed. No (in-tank activation) -> skip this stage.
2. **Rinse tank cross-section (Block C):** Standard tank for the "yes" path.
3. **Contamination risk panel (Block D):** What acid drag-in does to the chrome bath.
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
  Stage 4 highlighted (Teal)
ZONE 3 -- DECISION TREE + RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION RISK (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON ISSUES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chrome (Decorative) -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Only needed if you run a separate activation tank. If you activate in the chrome bath, skip this stage.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated nickel surface with acid residue  -->  After: Acid-free surface ready for chrome immersion`

---

### ZONE 3 -- Decision Tree + Rinse Tank Hero

**Section label:** `DO YOU NEED THIS RINSE?` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 9.0")**

Central question box:
- Rounded rect, X: 6.0", Y: 5.0", W: 12.0", H: 1.5", fill `#E8A020` at 15%, border 2 pt `#E8A020`, radius 8
- Text: `DO YOU HAVE A SEPARATE ACTIVATION TANK?` -- Barlow SemiBold, 20 pt, `#E8A020`

Two answer branches:

**Left -- YES:**
- Arrow down-left from question box
- Rounded rect, X: 1.0", Y: 7.5", W: 9.0", H: 1.5", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `YES -- Separate acid dip` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Sub: `RINSE IS NEEDED -- remove acid before chrome bath` -- Inter Medium, 13 pt, `#F0EDE8`

**Right -- NO:**
- Arrow down-right from question box
- Rounded rect, X: 14.0", Y: 7.5", W: 9.0", H: 1.5", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `NO -- In-tank activation` -- Barlow SemiBold, 18 pt, `#27AE60`
- Sub: `SKIP THIS STAGE -- go directly to chrome bath` -- Inter Medium, 13 pt, `#F0EDE8`

**BLOCK C -- Rinse Tank (for "YES" path, Y: 9.5" to 14.0")**

- Standard rinse tank cross-section, X: 1.0", W: 22.0", H: 4.0"
- Fill `#252B3D`, border 2 pt `#C8D0D8`
- Parts on rack, overflow weir, flow arrows
- Key labels inside:
  - `Single stage, ambient` JetBrains Mono 14 pt
  - `Dwell: 15--30 sec` JetBrains Mono 14 pt `#E8A020`
  - `Purpose: remove acid drag-out` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Contamination Risk

**Section label:** `WHAT ACID DRAG-IN DOES TO YOUR CHROME BATH` -- Y: 14.7".

**BLOCK D -- Risk Panel (Y: 15.3" to 20.3")**

Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#E05C5C`.

**Three contamination scenarios:**

| Contaminant | Effect on Chrome Bath | Severity |
|---|---|---|
| HCl drag-in | Introduces chloride -- attacks lead anodes (hex), disrupts bath chemistry | HIGH (`#E05C5C`) |
| H2SO4 drag-in | Increases sulfate -- shifts CrO3:SO4 ratio (hex), alters catalyst balance | MODERATE (`#E8A020`) |
| Nickel salts | Builds up as metallic contamination over time | LOW (`#2EC4B6`) |

Each row: alternating `#1E2435` / `#252B3D`.

Bottom callout:
- `Chloride is the biggest risk. Even small amounts attack lead anodes and create bath instability. If you use HCl activation, this rinse is non-negotiable.` -- Inter Medium, 14 pt, `#E05C5C`

---

### ZONE 5 -- Operating Parameters

**Section label:** `OPERATING PARAMETERS (WHEN RINSE IS PRESENT)` -- Y: 20.7".

**BLOCK E -- Parameters (Y: 21.3" to 26.3")**

| Parameter | Value | Notes |
|---|---|---|
| Water source | City water or DI | DI reduces mineral contamination risk |
| Temperature | Ambient | No heating |
| Rinse type | Single overflow | Speed is still the priority |
| Dwell time | 15--30 sec | Minimize to prevent re-passivation |
| Flow rate | Moderate continuous | Enough to dilute acid |
| Agitation | 2--3 dips | Quick immersions |
| pH check | Optional (> 5.0) | Ensures acid is adequately rinsed |

Data: JetBrains Mono 14 pt. Notes: Inter Regular 13 pt `#F0EDE8` at 70%.

---

### ZONE 6 -- Common Issues

**Section label:** `COMMON PROBLEMS AT THIS STAGE` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Problem | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | CHROME BATH RATIO DRIFT | `#E05C5C` | Acid drag-in shifting sulfate levels | Improve rinse; monitor CrO3:SO4 ratio |
| R1C2 | RE-PASSIVATION | `#E05C5C` | Parts sat too long in rinse after activation | Shorten dwell; move parts immediately |
| R2C1 | CHLORIDE CONTAMINATION | `#E8A020` | HCl activation without adequate rinse | Switch to H2SO4 activation or add rinse stage |
| R2C2 | WATER SPOTS | `#E8A020` | Hard water deposits on parts before chrome | Use DI water for final rinse stage |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Chrome (Decorative) -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; decorative chrome process engineering practice.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Chrome Decorative Rinse Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The decision tree in Zone 3 is the most important element on this poster. Half of decorative chrome lines do not even have this tank -- the poster needs to acknowledge that reality immediately rather than pretending every line runs this stage. The contamination risk panel in Zone 4 gives the "why" for shops that do run a separate activation -- chloride drag-in from HCl activation is the killer. The operating parameters are deliberately spare; this is a simple rinse when it exists.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #83 -- Construction Workup v1.0*
*2026-04-26*
