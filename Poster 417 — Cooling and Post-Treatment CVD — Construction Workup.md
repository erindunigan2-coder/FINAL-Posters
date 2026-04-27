---
Project: Plating Posters Inc
Poster Number: 417
Title: "Cooling & Post-Treatment -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Sections 2.8)"
Technical Source: CVD cooling and post-treatment -- controlled cooling under protective atmosphere, cooling rate limits to avoid thermal stress cracking, eta-phase management during cooldown, and post-coating surface treatments (wet blasting, polishing, edge honing) that transform the as-deposited coating into a usable cutting tool.
Process Scope: CVD cooling and post-deposition treatment (Stage 9 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Cooling
  - PostTreatment
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #417 -- Construction Workup
## Cooling & Post-Treatment -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of 10. Deposition is complete, but the run is not over. The furnace must cool under controlled atmosphere at a controlled rate -- too fast and the coating cracks from thermal stress; too slow and you waste furnace time. The critical temperature zone is 900-700 C where eta-phase can form at the coating-substrate interface in WC-Co substrates. After unloading, most CVD-coated cutting inserts undergo post-treatment: wet blasting, rake face polishing, and edge honing to optimize the coating for cutting performance.

Hero visual: cooling profile curve showing temperature vs. time with critical zones annotated.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cooling profile diagram (Block B -- HERO):** Temperature vs. time curve from deposition temperature to room temperature with annotated zones (eta-phase risk zone, oxidation risk zone, safe handling threshold).
2. **Why cooling rate matters (Block C):** Thermal expansion mismatch concept.
3. **Post-coating treatment sequence (Block D):** Three-step post-treatment flow.
4. **Common cooling/post-treatment failures (Block E):** Failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber -- cooling)
ZONE 3 -- COOLING PROFILE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- THERMAL STRESS + ATMOSPHERE (14.5"--22.0" / ~7.5")
ZONE 5 -- POST-COATING TREATMENT (22.0"--27.5" / ~5.5")
ZONE 6 -- COMMON FAILURES (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `COOLING & POST-TREATMENT` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 9 of 10 -- Controlled Cooldown and Surface Optimization` -- 28 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The coating is deposited. Now cool it without cracking it, and finish it without damaging it. The cooldown is where patience pays off.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `2-10` -- 60 pt, `#E8A020`
- Label: `C/min COOLING RATE` -- JetBrains Mono, 14 pt
- Sub-label: `Too fast = cracking. Too slow = wasted furnace time.` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Deposition complete, furnace at 900-1050 C (Stage 8) --> After: Parts at room temperature, surface-treated, ready for inspection`

---

### ZONE 3 -- Cooling Profile Hero

**Section label:** `COOLING PROFILE -- TEMPERATURE vs. TIME` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Cooling Curve Diagram (Y: 5.0" to 14.0")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Chart area (X: 2.5", Y: 5.5", W: 19.0", H: 7.5"):**

Y-axis: Temperature (C) from 0 to 1100. JetBrains Mono 11 pt `#F0EDE8` at 60%.
X-axis: Time (hr) from 0 to 8. JetBrains Mono 11 pt `#F0EDE8` at 60%.

**Cooling curve:** Smooth descending curve from (0, 1050) to (8, 25). 3 pt stroke `#E8A020`.

**Annotated zones on the curve:**

Zone A -- ETA-PHASE RISK (900-700 C):
- Shaded horizontal band, fill `#E05C5C` at 15%
- Left label: `ETA-PHASE RISK ZONE` Barlow SemiBold 14 pt `#E05C5C`
- Annotation line to callout: `900-700 C: HCl + Co binder interaction can form brittle Co3W3C at interface. Control atmosphere and cooling rate through this range.`
- Inter Regular 12 pt `#F0EDE8`

Zone B -- OXIDATION RISK (above 200 C in air):
- Shaded horizontal band, fill `#E8A020` at 15%
- Left label: `OXIDATION THRESHOLD` Barlow SemiBold 14 pt `#E8A020`
- Annotation: `Do not vent to air above 200 C. Coating surface will oxidize and discolor.`

Zone C -- SAFE HANDLING (below 50 C):
- Shaded horizontal band, fill `#27AE60` at 15%
- Left label: `SAFE TO HANDLE` Barlow SemiBold 14 pt `#27AE60`
- Annotation: `Below 50 C: safe for ungloved handling`

**Cooling rate annotation on curve:**
- `2-10 C/min` JetBrains Mono Bold 16 pt `#E8A020` with an arrow pointing to the slope of the curve

**Atmosphere labels along the curve:**
- `H2 or Ar atmosphere maintained throughout cooling` -- Inter Medium 12 pt `#2EC4B6`, dashed line across the top

---

### ZONE 4 -- Thermal Stress + Atmosphere

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Why Cooling Rate Matters (X: 0.5", W: 11.0")**

**Section label:** `THERMAL EXPANSION MISMATCH` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Thermal Stress Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
The coating and substrate have different
coefficients of thermal expansion (CTE).

As the assembly cools from 1050 C to 25 C,
each material contracts at its own rate.

CTE VALUES:
  WC-Co substrate:  5.5 um/m/C
  TiC coating:      7.4 um/m/C
  TiN coating:      9.4 um/m/C
  Al2O3 coating:    8.0 um/m/C

Since coatings have HIGHER CTE than WC-Co,
they want to shrink MORE than the substrate.
Result: TENSILE STRESS in the coating.

TOO FAST COOLING:
  Stress exceeds coating strength
  = "egg-shell" cracking

CONTROLLED COOLING:
  Stress builds gradually
  = micro-cracking network (normal for CVD)
  that relieves stress without catastrophic failure
```

Bottom callout:
- `CVD coatings on WC-Co always develop a network of micro-cracks upon cooling. This is expected and acceptable -- unlike PVD coatings, which are thin enough to remain crack-free.` Inter Medium 12 pt `#2EC4B6`

**Right -- Atmosphere Control (X: 12.0", W: 11.5")**

**Section label:** `ATMOSPHERE DURING COOLING` -- Y: 14.7".

**BLOCK C2 -- Atmosphere Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Three stacked cards:

Card 1 -- H2 ATMOSPHERE (primary):
- W: 10.5", H: 1.8", fill `#252B3D`, left accent `#27AE60`
- Title: `HYDROGEN (H2)` Barlow SemiBold 14 pt `#27AE60`
- Body: `Reducing atmosphere. Prevents oxidation of coating surface. Maintains clean interface. Standard for most CVD furnaces during cooling.`

Card 2 -- INERT GAS (Ar or N2):
- W: 10.5", H: 1.8", fill `#252B3D`, left accent `#E8A020`
- Title: `ARGON or NITROGEN` Barlow SemiBold 14 pt `#E8A020`
- Body: `Alternative when H2 is not practical. Prevents oxidation but does not reduce surface oxides. Used for some Al2O3-topped stacks.`

Card 3 -- NEVER VENT TO AIR HOT:
- W: 10.5", H: 1.8", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Title: `NEVER VENT TO AIR ABOVE 200 C` Barlow SemiBold 14 pt `#E05C5C`
- Body: `Opening the furnace while parts are hot exposes the fresh coating to atmospheric O2. TiN turns blue-purple. TiCN discolors. Al2O3 is more tolerant but surrounding layers are not.`

---

### ZONE 5 -- Post-Coating Treatment

**Section label:** `POST-COATING SURFACE TREATMENT` -- Y: 22.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Three-Step Treatment Flow (Y: 22.8" to 27.3")**

Three horizontal panels in a flow sequence with arrows:

**Panel 1 -- Wet Blasting (X: 0.5", W: 7.0"):**
- Rounded rect, H: 4.3", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `WET BLASTING` Barlow SemiBold 18 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Fine Al2O3 media (400-800 grit)
suspended in water slurry

PURPOSE:
- Smooth surface nodules
- Remove excess coating buildup
- Introduce beneficial
  compressive stress in
  coating surface layer

Pressure: 2-4 bar
Angle: 45-90 deg
Time: 5-30 sec per surface
```

Arrow: 3 pt `#C8D0D8`, right

**Panel 2 -- Rake Face Polish (X: 8.0", W: 7.0"):**
- Rounded rect, H: 4.3", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `RAKE FACE POLISH` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Polishing the rake face (top surface
of cutting insert) to reduce friction
and improve chip flow.

METHOD:
- Brush polishing or drag finishing
- SiC or diamond abrasive
- Target: Ra < 0.1 um on rake

RESULT:
- Reduced built-up edge
- Lower cutting forces
- Better chip evacuation
```

Arrow: 3 pt `#C8D0D8`, right

**Panel 3 -- Edge Honing (X: 15.5", W: 7.0"):**
- Rounded rect, H: 4.3", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `EDGE HONING` Barlow SemiBold 18 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`):
```
Optimizing the cutting edge radius
after coating.

TARGET: 20-40 um edge radius
(application dependent)

METHOD:
- Brush honing (nylon + SiC)
- Drag finishing
- Wet blasting at edge

WHY: CVD coating thickens at edges;
unhoned edge is too rounded
for some applications
```

---

### ZONE 6 -- Common Failures

**Section label:** `COOLING & POST-TREATMENT FAILURES` -- Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Four Failure Cards (Y: 28.3" to 32.3")**

Each card: Rounded rect W: 5.5", H: 3.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | EGG-SHELL CRACKING | Cooling too fast; thermal stress exceeds coating strength | Reduce cooling rate to 2-5 C/min; multilayer architecture |
| 2 | 6.33" | COATING DISCOLORATION | Vented to air above 200 C; O2 contact with hot TiN/TiCN | Maintain protective atmosphere until < 200 C |
| 3 | 12.16" | COBALT DEPLETION (eta-phase) | Prolonged time at 900-700 C under HCl-containing atmosphere | Faster transition through 900-700 C zone; protective interlayer |
| 4 | 18.0" | OVER-BLASTED SURFACE | Wet blasting pressure too high or time too long | Control blast parameters; use fine media (600+ grit) |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 12 pt `#F0EDE8`
- Fix: Inter Medium 12 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Cooling & Post-Treatment -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cooling Post-Treatment CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cooling profile curve as hero gives operators a visual they can internalize -- a descending line with three color-coded danger zones. The thermal expansion mismatch explanation is the "why" behind the cooling rate rule, and the CTE values table makes it concrete. The post-treatment sequence (wet blast -> polish -> hone) is presented as a linear flow because that is exactly how it happens on the shop floor. Many operators do not realize that most CVD-coated inserts undergo significant post-processing before they reach the end user.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #417 -- Construction Workup v1.0*
*2026-04-26*
