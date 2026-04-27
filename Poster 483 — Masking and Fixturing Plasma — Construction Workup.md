---
Project: Plating Posters Inc
Poster Number: 483
Title: "Masking & Fixturing -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 5)"
Technical Source: Masking materials rated for APS temperatures (260 degC+), fixturing for rotation and cooling, and design rules for line-of-sight access.
Process Scope: Atmospheric plasma spray -- masking materials and part fixturing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Masking
  - Fixturing
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #483 -- Construction Workup
## Masking & Fixturing -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of the APS process. Masking protects areas that must not be coated. Fixturing ensures uniform standoff distance and spray angle. Both are engineering decisions, not afterthoughts. Hero visual: a masking materials comparison table paired with fixturing design rules.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Masking materials table (Block B):** 5-row comparison of masking types with temperature ratings and use cases.
2. **Fixturing design rules (Block C):** 6 rules as numbered cards.
3. **Temperature rating callout (Block D):** Visual showing APS temperature exposure on masking surfaces.
4. **Common mistakes grid (Block E):** 4 cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- MASKING MATERIALS HERO (4.2"--14.5" / ~10.3")
  Block B: Masking materials comparison table
  Block C: Fixturing design rules
ZONE 4 -- TEMPERATURE EXPOSURE (14.5"--20.5" / ~6.0")
  Block D: Temperature rating vs. APS exposure callout
ZONE 5 -- COMMON MISTAKES (20.5"--26.5" / ~6.0")
  Block E: 4 mistake cards
ZONE 6 -- DESIGN CHECKLIST (26.5"--32.5" / ~6.0")
  Block F: Pre-spray fixture verification checklist
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MASKING & FIXTURING` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- Protect What Must Not Be Coated -- Stage 3 of 10` -- 32 pt `#E8A020`. Y: 1.4".
**Tagline:** `Good masking is invisible in the finished part. Bad masking shows up as rework, scrap, or a customer complaint.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted (Amber). Others dimmed.

---

### ZONE 3 -- Masking Materials + Fixturing (HERO)

**Section label:** `MASKING MATERIALS FOR APS` -- Y: 4.4".

**BLOCK B -- Masking Materials Table (left, W: 13.0")**

Y: 5.0" to 10.5".

| Material | Temp Rating | Reusable? | Best For | Limitations |
|---|---|---|---|---|
| Hi-temp silicone tape | 260 degC (500 degF) | No | Quick masking of flat surfaces, edges | Adhesive residue risk; single use |
| Metal masks (steel, SS, Cu) | > 500 degC | Yes | Production runs; repeatable geometry | Requires machining; cost for custom shapes |
| Silicone plugs & caps | 260 degC (500 degF) | Yes (limited) | Holes, bores, threaded features | Must fit snugly; check for heat deformation |
| Ceramic fiber tape | > 1000 degC | No | Extreme temperature zones near plasma plume | Fragile; limited adhesion |
| Liquid maskant (peelable) | 200-300 degC (varies) | No | Complex shapes; spray-applied masking | Requires curing time; thickness control |

**BLOCK C -- Fixturing Design Rules (right, W: 9.5")**

Y: 5.0" to 10.5". Six numbered rule cards stacked vertically.

| Rule | Text |
|---|---|
| 1 | Rotation speed: 60-200 RPM for cylindrical parts (lathe-type setup) |
| 2 | Maintain uniform standoff distance -- fixture must hold part rigidly |
| 3 | Cooling air nozzles directed at substrate backside -- critical for temp control |
| 4 | Fixture must not shadow spray pattern -- design for line-of-sight access |
| 5 | Ground fixture to workpiece -- prevent electrostatic discharge |
| 6 | Use sacrificial test tabs attached to same fixture for in-process QC |

Each rule: Rounded rect, H: 0.85", fill `#1E2435`, left accent `#2EC4B6`.
Rule number: Barlow Condensed ExtraBold 16 pt `#2EC4B6`. Text: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 4 -- Temperature Exposure Callout

**Section label:** `MASKING MUST SURVIVE THE HEAT` -- Y: 14.7".

**BLOCK D -- Temperature Rating Visual**

Y: 15.3" to 20.3". Full width.

Horizontal bar showing temperature zones:
- `0-200 degC`: `Standard tape zone` -- fill `#27AE60` at 30%
- `200-300 degC`: `Silicone tape / liquid maskant zone` -- fill `#E8A020` at 30%
- `300-500 degC`: `Metal mask required` -- fill `#E05C5C` at 30%
- `500+ degC`: `Ceramic fiber or bare (no mask survives indefinitely)` -- fill `#E05C5C` at 50%

Marker arrow: `APS substrate temp during spray: 80-200 degC typical` at ~150 degC mark.
Marker arrow: `Direct plasma plume exposure: > 1000 degC` at right edge.

Note below: `The substrate temperature is survivable for silicone tape. Direct plume exposure is not. Position masks so they are never in the direct spray path.` Inter Medium 14 pt `#E8A020`.

---

### ZONE 5 -- Common Mistakes

**Section label:** `4 MASKING & FIXTURING MISTAKES` -- Y: 20.7".

Four cards in a row:

| Problem | Cause | Fix |
|---|---|---|
| COATING UNDER MASK | Mask not sealed to surface; gap at edge | Press firmly; use metal masks for tight tolerance |
| FIXTURE SHADOW | Fixture blocks spray path | Redesign fixture for full line-of-sight access |
| THERMAL DISTORTION | Part overheats; warps on fixture | Add cooling air; reduce pass dwell time |
| ADHESIVE RESIDUE | Tape removed after spray; residue contaminates surface | Use silicone-adhesive tapes; remove cleanly before any post-treatment |

---

### ZONE 6 -- Pre-Spray Checklist

**Section label:** `PRE-SPRAY FIXTURE VERIFICATION` -- Y: 26.7".

**BLOCK F -- Checklist (10 items)**

Two columns of 5 items. Each: checkbox + text.

| Item |
|---|
| Part securely fixtured -- no wobble or play |
| Masking complete and inspected |
| No masking tape in direct spray path |
| Cooling air nozzles positioned and tested |
| Fixture does not shadow any coated area |
| Sacrificial test tabs installed |
| Rotation speed set and verified |
| Part grounded to fixture |
| All non-coated features masked (holes, threads, bearing surfaces) |
| Operator has verified standoff distance at all positions |

---

### ZONE 7 -- Footer

Standard. Title: `Masking & Fixturing -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Masking Fixturing Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster bridges the gap between cleaning (Stage 1) and equipment setup (Stage 4). Metal masks for production, tape for prototyping -- that's the decision tree. The temperature exposure visual is the unique element here: operators need to understand that masking materials have thermal limits and direct plume exposure destroys everything except ceramic fiber.

---

*Alaina -- Poster #483 -- Construction Workup v1.0 -- 2026-04-26*
