---
Project: Plating Posters Inc
Poster Number: 388
Title: "Ultrasonic Cleaning Stage"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- the main cleaning step, cavitation mechanism, part loading, and operating procedure
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - MainStage
  - Cavitation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #388 -- Construction Workup
## Ultrasonic Cleaning Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the heart of the cluster -- the actual cleaning step where cavitation does its work. The hero concept is the cavitation mechanism explained visually: compression/rarefaction cycles creating bubbles that implode with micro-jets at 400 km/hr. This poster covers operating procedure, part loading rules, sweep frequency technology, and the aluminum foil test for cavitation verification.

Hero visual: a cavitation bubble sequence showing formation, growth, and implosion with the micro-jet targeting a surface contaminant. The physics made visual.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cavitation mechanism diagram (Block B -- HERO):** Three-phase sequence (rarefaction -> bubble growth -> violent collapse + micro-jet). Built with circles, arrows, and text labels. This is the poster's signature element.
2. **Operating procedure steps (Block D):** Seven-step numbered sequence.
3. **Part loading rules (Block E):** Four rules with visual indicators.
4. **Common failures grid (Block F):** 2x3 grid of failure modes.
5. **Aluminum foil test callout (Block G):** Quick verification method.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Emerald) -- "Ultrasonic Clean"
ZONE 3 -- CAVITATION MECHANISM HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- OPERATING PROCEDURE (15.5"--21.0" / ~5.5")
ZONE 5 -- PART LOADING RULES + FOIL TEST (21.0"--27.5" / ~6.5")
ZONE 6 -- COMMON FAILURES GRID (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ULTRASONIC CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `The Cleaning Stage -- Cavitation, Loading, and Operation` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `5,000 K. 1,000 atm. 400 km/hr micro-jets. Billions of microscopic explosions per second -- cleaning where nothing else can reach.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Contaminated parts loaded in basket --> After: Clean surfaces -- blind holes, threads, and undercuts included`

---

### ZONE 3 -- Cavitation Mechanism Hero

**Section label:** `HOW CAVITATION CLEANS` -- Y: 4.4".
**Sublabel:** `Sound waves do the work -- here's what happens at the microscopic level` -- Y: 4.9". Inter Regular 16 pt `#F0EDE8` at 60%.

**BLOCK B -- Cavitation Sequence Diagram**

Y: 5.5" to 10.5". Three-phase horizontal sequence across full width.

**Phase 1 -- Rarefaction (X: 0.5", W: 7.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, top accent `#2EC4B6`
- Title: `1. RAREFACTION` Barlow Condensed ExtraBold 22 pt `#2EC4B6`
- Visual: Small circle (bubble) ~0.5" diameter, stroke 2 pt `#2EC4B6`, fill `#2EC4B6` at 10%
- Below circle: wavy lines representing sound wave low-pressure phase
- Text: `Low-pressure phase of the sound wave. Microscopic vacuum bubbles form in the liquid.` Inter Regular 14 pt `#F0EDE8`
- Data: `Bubble size: 20--170 micrometers (frequency-dependent)` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Arrow:** Right-pointing, 3 pt `#3A4055`, between Phase 1 and Phase 2.

**Phase 2 -- Growth (X: 8.0", W: 7.0"):**
- Same box style, top accent `#E8A020`
- Title: `2. GROWTH` Barlow Condensed ExtraBold 22 pt `#E8A020`
- Visual: Larger circle ~1.0" diameter, stroke 2 pt `#E8A020`, fill `#E8A020` at 10%
- Text: `Bubble expands through several acoustic cycles, accumulating energy. Near a solid surface, the bubble becomes asymmetric.` Inter Regular 14 pt `#F0EDE8`

**Arrow:** Right-pointing.

**Phase 3 -- Collapse + Micro-Jet (X: 15.5", W: 8.0"):**
- Same box style, top accent `#E05C5C`
- Title: `3. VIOLENT COLLAPSE` Barlow Condensed ExtraBold 22 pt `#E05C5C`
- Visual: Collapsed circle shape with directional arrow (micro-jet) pointing down toward a surface line
- Text: `Bubble implodes asymmetrically. A high-velocity micro-jet of liquid fires at the nearest solid surface.` Inter Regular 14 pt `#F0EDE8`

**Micro-jet data callout (within Phase 3 box):**
Three stat badges:
- `~5,000 K` JetBrains Mono 20 pt `#E05C5C` (Temperature at collapse point)
- `~1,000+ atm` JetBrains Mono 20 pt `#E8A020` (Pressure at collapse point)
- `~400 km/hr` JetBrains Mono 20 pt `#27AE60` (Micro-jet velocity)

Labels beneath each: Inter Regular 11 pt `#F0EDE8` at 60%.

**Key insight strip (Y: 10.8" to 11.4"):**
- Rounded rect, full width, H: 0.5", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `The micro-jet is the primary cleaning mechanism -- it blasts contaminants off the surface, reaching pores, threads, blind holes, and undercuts that spray or immersion cannot access.` Inter Medium 14 pt `#27AE60`

**BLOCK C -- Sweep Frequency + Multi-Frequency (Y: 11.8" to 15.3")**

Two side-by-side callout boxes.

**Left -- Sweep Frequency (X: 0.5", W: 11.0"):**
- Rounded rect, H: 3.3", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SWEEP FREQUENCY` Barlow SemiBold 18 pt `#2EC4B6`
- Body: `Fixed frequency creates standing wave patterns with dead zones (nodes) where cavitation is minimal. Sweep frequency generators vary +/- 1--3 kHz around center frequency, shifting the pattern continuously. Result: uniform cleaning with no dead zones.` Inter Regular 13 pt `#F0EDE8`
- Note: `Modern systems should ALWAYS have sweep capability` Inter Medium 13 pt `#27AE60`

**Right -- Multi-Frequency Systems (X: 12.0", W: 11.5"):**
- Same box style, left accent `#E8A020`
- Title: `MULTI-FREQUENCY SYSTEMS` Barlow SemiBold 18 pt `#E8A020`
- Body: `Advanced tanks offer selectable frequencies (e.g., 25/45/80 kHz). Start low frequency for bulk soil removal, finish high frequency for fine particle removal. Most beneficial for precision cleaning.` Inter Regular 13 pt `#F0EDE8`
- Note: `Combined ultrasonic + electrocleaning exists for high-value plating` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Operating Procedure

**Section label:** `OPERATING PROCEDURE -- 7 STEPS` -- Y: 15.7".

**BLOCK D -- Seven Numbered Steps**

Y: 16.3" to 20.8". Vertical step list.

Each step: Rounded rect, full width (23.0"), H: 0.6", fill alternating `#1E2435` / `#252B3D`.

| Step | Text | Note Color |
|---|---|---|
| 1 | Degas fresh solution: run ultrasonics 10--15 min, no parts | `#E8A020` |
| 2 | Bring solution to operating temperature (120--150 F typical) | `#2EC4B6` |
| 3 | Load parts in wire mesh basket -- orient for full surface exposure | `#2EC4B6` |
| 4 | Immerse basket; activate ultrasonics | `#27AE60` |
| 5 | Clean: 3--10 min general / 1--3 min light / 15--20 min tenacious | `#27AE60` |
| 6 | Remove parts; drain briefly over tank | `#2EC4B6` |
| 7 | Transfer to rinse immediately -- do not air-dry with solution on parts | `#E05C5C` |

Step number: Barlow Condensed ExtraBold 18 pt in note color. Text: Inter Regular 14 pt `#F0EDE8`.

---

### ZONE 5 -- Part Loading Rules + Foil Test

**Two-column layout (Y: 21.2" to 27.3"):**

**Left -- Part Loading Rules (X: 0.5", W: 11.0"):**

Section label: `LOADING RULES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Four rule cards stacked vertically. Each: Rounded rect, W: 11.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Rule | Reason |
|---|---|
| Orient parts so cavitation reaches ALL surfaces | Shielded areas will not clean |
| Do NOT overload basket | Overcrowding blocks sound wave propagation |
| Rotate or reposition for complex geometry | Multi-side exposure improves uniformity |
| NEVER place parts on tank bottom | Blocks transducer energy; may damage transducer |

Rule: Barlow SemiBold 14 pt `#F0EDE8`. Reason: Inter Regular 13 pt `#F0EDE8` at 70%.

**Right -- Aluminum Foil Test (X: 12.0", W: 11.5"):**

Section label: `THE ALUMINUM FOIL TEST` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Rounded rect, W: 11.5", H: 5.5", fill `#1E2435`, left accent `#E8A020`, radius 6.

- Subtitle: `Quick Cavitation Verification -- No Instruments Required` Barlow SemiBold 14 pt `#E8A020`

Steps:
1. `Suspend a sheet of household aluminum foil vertically in operating tank`
2. `Run for 30--60 seconds`
3. `Remove and examine`

Results interpretation:
- `Uniform pitting across foil = GOOD cavitation distribution` `#27AE60`
- `Uneven or no pitting = dead zones, transducer issues, or low power` `#E05C5C`

- `Every shop should do this monthly and after any service` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Common Failures Grid

**Section label:** `WHAT GOES WRONG -- 5 COMMON FAILURES` -- Y: 27.7".

**BLOCK F -- Failure Grid**

Y: 28.3" to 32.3". Five cards in a row (slightly narrower than usual).

Each card: Rounded rect, W: 4.4", H: 3.8", fill `#1E2435`, radius 4, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | UNEVEN CLEANING | Overloaded basket; standing waves | Reduce load; use sweep frequency |
| 2 | 5.2" | SURFACE EROSION | Frequency too low; time too long | Increase frequency; reduce time |
| 3 | 9.9" | NO IMPROVEMENT | Not degassed; temp too high; transducer dead | Degas; check temp; foil test |
| 4 | 14.6" | FOAMING | Surfactant too high or wrong type | Use low-foam ultrasonic cleaner |
| 5 | 19.3" | RE-CONTAMINATION | No filtration; dirty solution; sludge | Filter; clean tank; replace solution |

Interior: Failure name Barlow SemiBold 14 pt `#E05C5C`. Cause Inter Regular 12 pt `#F0EDE8`. Fix Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Ultrasonic Cleaning Stage`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Cavitation physics values are approximate and vary by conditions. Consult your equipment manufacturer for specific operating parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Ultrasonic Cleaning Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the signature poster of the CT-07 cluster. The cavitation mechanism diagram (Zone 3) must be visually compelling -- it explains WHY ultrasonic cleaning works, not just HOW to operate it. The three-phase sequence (rarefaction -> growth -> violent collapse) should feel dynamic. The stat callouts (5,000 K / 1,000 atm / 400 km/hr) are the "wow" numbers that make operators respect the process. The aluminum foil test is the most practical takeaway -- every shop can do this tomorrow.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #388 -- Construction Workup v1.0*
*2026-04-26*
