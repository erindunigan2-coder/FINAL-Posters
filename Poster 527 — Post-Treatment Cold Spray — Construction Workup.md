---
Project: Plating Posters Inc
Poster Number: 527
Title: "Post-Treatment -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray post-treatment including heat treatment (annealing for ductility recovery), machining of deposits to final dimension, and sealing (rarely needed). Copper, aluminum, and titanium anneal schedules. The unique advantage that cold spray deposits machine like wrought material.
Process Scope: Cold spray -- post-treatment, heat treatment, and machining
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - PostTreatment
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #527 -- Construction Workup
## Post-Treatment -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Post-treatment poster for Cold Spray. Hero concept: cold spray deposits machine like wrought material -- no special tooling, no diamond grinding, conventional turning and milling. This is a massive practical advantage over every other thermal spray process. The secondary story is ductility recovery via annealing -- the severe plastic deformation during impact work-hardens the deposit, and a simple anneal can recover ductility and improve inter-particle bonding through diffusion.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Annealing schedule table (Block B -- HERO):** Material-specific heat treatment temperatures and times for Cu, Al, and Ti.
2. **"Machines Like Wrought" callout (Block C):** Emerald callout emphasizing the machining advantage -- the single biggest practical differentiator for dimensional restoration work.
3. **Post-treatment decision flowchart (Block D):** Simple decision tree: is ductility needed? Is conductivity recovery needed? Is dimensional accuracy needed? Routes to anneal, machine, or both.
4. **Sealing note (Block E):** Brief callout -- sealing is rarely needed because porosity is already below 1%.
5. **Before/after property comparison (Block F):** As-sprayed vs. post-treated properties for copper benchmark.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ANNEALING SCHEDULES + MACHINING CALLOUT (2.9"--14.0" / ~11.1")
  Block B: Material-specific anneal table
  Block C: "Machines Like Wrought" hero callout
ZONE 3 -- DECISION FLOWCHART + SEALING (14.0"--22.0" / ~8.0")
  Block D: Post-treatment decision tree
  Block E: Sealing note
ZONE 4 -- PROPERTY COMPARISON + COMMON ISSUES (22.0"--32.5" / ~10.5")
  Block F: As-sprayed vs. post-treated properties (Cu benchmark)
  Block G: Common post-treatment defects strip
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 80 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Recover Ductility, Achieve Final Dimensions` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Anneal for ductility. Machine like wrought metal. No diamond grinding required -- because the deposit was never molten.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Annealing Schedules + Machining Callout

**Section label:** `HEAT TREATMENT SCHEDULES` -- Y: 3.1".

**BLOCK B -- Annealing Schedule Table (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 10.5". Full data table.

Header row: `#3A4055`. Columns: Material (3.0") | Temperature (3.0") | Time (2.0") | Atmosphere (3.0") | Purpose (3.5")

| Material | Temperature | Time | Atmosphere | Purpose |
|---|---|---|---|---|
| Copper (Cu) | 200--400 C | 1--4 hr | Vacuum or inert (Ar/N2) | Recover ductility; improve conductivity to ~98% IACS |
| Aluminum (Al, 6061) | T6 temper schedule | Per alloy spec | Air or inert | Restore temper properties to cold-sprayed Al alloy |
| Aluminum (Al, 7075) | T7 temper schedule | Per alloy spec | Air or inert | Overaged temper for stress corrosion resistance |
| Titanium (Ti, CP) | 500--700 C | 1--4 hr | Vacuum (mandatory) | Improve ductility; enhance inter-particle bonding |
| Ti-6Al-4V | 500--700 C | 1--4 hr | Vacuum (mandatory) | Diffusion bonding between particles; ductility recovery |
| Nickel (Inconel 625) | 600--800 C | 1--2 hr | Vacuum or inert | Improve inter-particle metallurgical bonding |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Material names in Inter Medium, 13 pt. Temperature values in `#E8A020`.

**Anneal note (below table, Y: 10.8" to 11.8"):**
Rounded rect, W: 14.0", H: 0.8", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

`Heat treatment also improves inter-particle bonding through solid-state diffusion -- atoms migrate across particle-particle interfaces, converting mechanical interlocks into metallurgical bonds.` Inter Medium, 13 pt, `#E8A020`, center.

**Vacuum note (Y: 12.0" to 12.8"):**
Rounded rect, W: 14.0", H: 0.6", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

`TITANIUM: Vacuum atmosphere is MANDATORY above 400 C. Titanium oxidizes aggressively in air at elevated temperatures.` Inter Medium, 13 pt, `#E05C5C`, center.

**BLOCK C -- "Machines Like Wrought" Callout (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 12.8". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.
Emerald-tinted glass.

Title: `MACHINES LIKE WROUGHT` Barlow Condensed ExtraBold, 28 pt, `#27AE60`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
Cold spray is the ONLY thermal spray
process where deposits can be machined
with conventional tools:

  Turning
  Milling
  Drilling
  Tapping
  Grinding (standard wheels)

No diamond grinding required.
No special tooling.
No carbide-specific cutters.
```

Comparison strip (Y: 8.5" to 12.5"):
```
COLD SPRAY:    Conventional machining
HVOF (WC-Co):  Diamond grinding ONLY
Plasma Spray:  Diamond grinding typical
Flame Spray:   Diamond grinding (fused)
```
JetBrains Mono Regular, 13 pt. "Conventional machining" in `#27AE60`, others in `#F0EDE8` at 60%.

Bottom stat: `Ra equivalent to wrought` Barlow SemiBold, 18 pt, `#27AE60`.

---

### ZONE 3 -- Decision Flowchart + Sealing

**Section label:** `POST-TREATMENT DECISION GUIDE` -- Y: 14.2".

**BLOCK D -- Decision Flowchart (Left, X: 0.5", W: 15.0")**

Y: 14.8" to 21.0". Flowchart with decision diamonds and outcome boxes.

Decision flow (top to bottom, branching right):

| Step | Element | Question / Action | Yes Path | No Path |
|---|---|---|---|---|
| 1 | Diamond | Is ductility recovery needed? | Go to Anneal box | Go to Step 2 |
| 2 | Diamond | Is dimensional accuracy required? | Go to Machine box | Go to Step 3 |
| 3 | Diamond | Is electrical/thermal conductivity critical? | Go to Anneal box (Cu: 200--400 C recovers to ~98% IACS) | Go to Step 4 |
| 4 | Diamond | Is porosity > 1%? | Go to Seal box | Go to "Use As-Sprayed" |

Outcome boxes (rounded rect, H: 1.0", fill `#1E2435`, left accent):

| Outcome | Accent | Content |
|---|---|---|
| ANNEAL | `#E8A020` | Heat treat per material schedule. Vacuum for Ti. Inert for Cu/Ni. Air OK for Al. |
| MACHINE | `#27AE60` | Conventional turning/milling/drilling. Achieve final dimension and surface finish. |
| SEAL | `#2EC4B6` | Epoxy impregnation (rare). Only if porosity exceeds 1% or barrier application requires it. |
| USE AS-SPRAYED | `#C8D0D8` | Many cold spray applications require no post-treatment at all. |

Diamond fills: `#252B3D`. Diamond text: Inter Medium, 13 pt, `#F0EDE8`.
Arrows: 2 pt, `#3A4055`, with arrowheads. "YES" and "NO" labels: JetBrains Mono, 11 pt, `#27AE60` and `#E05C5C` respectively.

**BLOCK E -- Sealing Note (Right, X: 16.0", W: 7.5")**

Y: 14.8" to 18.5". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#2EC4B6`.

Title: `SEALING -- RARELY NEEDED` Barlow SemiBold, 18 pt, `#2EC4B6`.

Body (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
Cold spray porosity is typically < 1%:

  Copper:     < 0.5%
  Aluminum:   0.5--2%
  Titanium:   1--3%

Sealing is only considered when:
- Porosity exceeds specification
- Application requires hermetic barrier
- Corrosion environment is severe

Method: epoxy vacuum impregnation
(same as used for cast metal parts)
```

Porosity values in JetBrains Mono, 13 pt, `#2EC4B6`.

**Compressive stress note (below, Y: 19.0" to 21.5"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Title: `WHY NO STRESS RELIEF?` Barlow SemiBold, 16 pt, `#27AE60`.
Body: `Cold spray deposits have COMPRESSIVE residual stress -- the opposite of other thermal spray processes. Compressive stress is beneficial for fatigue life and prevents spontaneous cracking. No stress relief heat treatment is needed for dimensional stability.` Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 4 -- Property Comparison + Common Issues

**Left -- Property Comparison (X: 0.5", W: 14.0")**

Section label: `BEFORE AND AFTER -- COPPER BENCHMARK` Y: 22.2".

**BLOCK F -- As-Sprayed vs. Post-Treated Properties**

Y: 22.8" to 30.5". Full data table.

Header row: `#3A4055`. Columns: Property (4.5") | As-Sprayed (4.5") | After Anneal (300 C / 2 hr) (5.0")

| Property | As-Sprayed | After Anneal (300 C / 2 hr) |
|---|---|---|
| Hardness | 100--150 HV (work-hardened) | 60--90 HV (softened toward bulk) |
| Ductility (elongation) | 1--5% | 10--25% (approaching bulk Cu) |
| Electrical conductivity | 80--95% IACS | 95--98% IACS |
| Thermal conductivity | Near bulk | ~bulk (401 W/mK) |
| Bond strength (ASTM C633) | > 60 MPa | > 60 MPa (no change or slight improvement) |
| Porosity | < 0.5% | < 0.5% (unchanged) |
| Residual stress | Compressive | Relaxed (still beneficial) |
| Machinability | Good (but harder) | Excellent (softened) |

Data: JetBrains Mono Regular, 12 pt. As-Sprayed values in `#E8A020`. Post-Anneal values in `#27AE60`.

Trade-off callout (below table, Y: 30.8" to 31.8"):
Rounded rect, full width 14.0", H: 0.8", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

`TRADE-OFF: Annealing recovers ductility and conductivity but REDUCES hardness. Choose based on application priority -- wear resistance (skip anneal) vs. electrical performance (anneal).` Inter Medium, 13 pt, `#E8A020`, center.

**Right -- Common Post-Treatment Issues (X: 15.0", W: 8.5")**

Section label: `COMMON ISSUES` Y: 22.2".

**BLOCK G -- Issue Cards (stacked)**

Y: 22.8" to 32.0". Four issue cards.

| Issue | Color | Cause | Fix |
|---|---|---|---|
| OVER-ANNEALING | `#E05C5C` | Temperature too high or time too long; excessive grain growth | Reduce temp/time; verify with hardness test |
| OXIDATION DURING ANNEAL | `#E05C5C` | Air atmosphere used for oxygen-sensitive material (Ti, Ni) | Use vacuum or inert atmosphere; verify O2 < 10 ppm |
| CHATTER DURING MACHINING | `#E8A020` | Work-hardened deposit; tool deflection | Anneal before machining; use rigid setup; reduce DOC |
| DIMENSIONAL OVERSHOOT | `#E8A020` | Insufficient stock left for finish machining | Plan spray thickness = final dim + machining allowance (0.25--0.5 mm per side) |

Each card: H: 2.1", fill `#1E2435`, left accent issue color.
Issue: Barlow SemiBold, 15 pt, issue color.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Fix: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Post-Treatment -- Cold Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post-Treatment Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Two stories compete here: (1) the anneal schedule table for ductility/conductivity recovery, and (2) the "machines like wrought" callout. The machining advantage is the more immediately impactful message for a shop audience -- no one wants to hear they need diamond grinding. Lead with the machining callout visually (emerald accent, prominent position) and let the anneal table serve as the reference data. The decision flowchart helps operators quickly determine whether they need post-treatment at all -- many cold spray applications go straight from spray to inspection.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #527 -- Construction Workup v1.0*
*2026-04-26*
