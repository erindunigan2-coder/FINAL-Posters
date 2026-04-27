---
Project: Plating Posters Inc
Poster Number: 681
Title: "Application -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.6)"
Technical Source: Dip coating application methods -- plastisol, hot-dip thermoplastic, and solution dip. Covers bath parameters, film thickness control (withdrawal speed, dip time, part temperature), the Landau-Levich equation for solution dip, and drip/drainage control including wire/cable air knives.
Process Scope: Application for dip coating -- Stage 5 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - Application
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #681 -- Construction Workup
## Application -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 7. The application stage is where dip coating's elegant simplicity reveals its hidden complexity. Three coating families, three completely different thickness control mechanisms: plastisol builds by dip time and viscosity, hot-dip thermoplastic builds by part temperature and dip time, and solution dip builds by withdrawal speed governed by the Landau-Levich equation. The hero is a three-family parameter comparison. The drainage and drip control section covers the transition from dip to cure -- including wire/cable air knives running at 1,000+ ft/min.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-family parameter comparison (Block B -- HERO):** Plastisol vs. hot-dip vs. solution dip application parameters side-by-side.
2. **Thickness control mechanisms (Block C):** What controls film build in each family.
3. **Drainage and drip control (Block D):** Post-withdrawal excess removal.
4. **Defect grid (Block F):** 6 application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- THREE-FAMILY PARAMETERS HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- THICKNESS CONTROL MECHANISMS (15.5"--21.5" / ~6.0")
ZONE 5 -- DRAINAGE AND DRIP CONTROL (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Three Families, Three Thickness Control Mechanisms -- Stage 5 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Plastisol builds by time. Hot-dip builds by temperature. Solution dip builds by withdrawal speed. Know your control variable or your thickness is a guess.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Primed, dry part ready for immersion --> After: Wet-coated part with target film build`

---

### ZONE 3 -- Three-Family Parameters Hero

**Section label:** `THREE COATING FAMILIES -- APPLICATION PARAMETERS` -- Y: 4.4".

**BLOCK B -- Three Columns (Y: 5.0" to 15.0")**

*Plastisol (PVC) (X: 0.5", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#E8A020`
- Title: `PLASTISOL (PVC)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters (JetBrains Mono 12 pt):
```
Bath temp: Ambient to 120 F
Part preheat: None, or 200--300 F
  for thicker builds
Immersion time: 2--30 sec
Withdrawal speed: 2--12 in/sec
Film build per dip: 5--40 mils
Multiple dips: Yes (very thick coats)
```
- Primary control: `DIP TIME + VISCOSITY`
- Key: `Longer immersion = thicker coat. Preheat accelerates gel-on-contact for even thicker builds.`

*Hot-Dip Thermoplastic (X: 8.17", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6`
- Title: `HOT-DIP THERMOPLASTIC` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Bath: Fluidized bed at ambient
Part preheat: 400--600 F (204--316 C)
Immersion time: 2--10 sec
Withdrawal: Rapid
Film build per dip: 8--25+ mils
Multiple dips: Rarely needed
```
- Primary control: `PART TEMPERATURE + DIP TIME`
- Key: `Hotter part = thicker coating. Powder melts on contact with hot metal and builds continuously until part cools below melt point.`

*Solution / Dispersion Dip (X: 15.83", W: 7.67"):*
- Rounded rect, fill `#1E2435`, top accent `#27AE60`
- Title: `SOLUTION DIP` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Bath temp: Ambient to 100 F
Part preheat: None
Immersion time: 1--10 sec
Withdrawal speed: 1--6 in/sec
  (SLOWER = THINNER)
Film build per dip: 0.5--3 mils
Multiple dips: Common (build gradually)
```
- Primary control: `WITHDRAWAL SPEED + VISCOSITY`
- Key: `The Landau-Levich equation governs: film thickness proportional to (speed)^2/3 x (viscosity)^2/3.`

---

### ZONE 4 -- Thickness Control Mechanisms

**Section label:** `WHAT CONTROLS YOUR FILM THICKNESS` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 21.3"):**

**Left -- Control Variable Summary (X: 0.5", W: 11.0"):**

Title: `PRIMARY AND SECONDARY CONTROLS` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Family | Primary Control | Secondary Control | Measure With |
|---|---|---|---|
| Plastisol | Dip time | Viscosity, preheat temp | Micrometer or DFT gauge |
| Hot-dip | Part temperature | Dip time | IR thermometer + micrometer |
| Solution | Withdrawal speed | Viscosity, solids content | DFT gauge or micrometer |

Note: `For plastisol and hot-dip, INCREASE the primary control to build thicker. For solution dip, DECREASE withdrawal speed to build thinner (counterintuitive).`

**Right -- Viscosity Management (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `VISCOSITY -- THE UNIVERSAL SECONDARY CONTROL` -- Barlow SemiBold, 18 pt, `#E8A020`

Plastisol viscosity:
- `Controlled by PVC particle size, plasticizer ratio, diluent`
- `Higher viscosity = thicker coat per dip`

Solution dip viscosity:
- `Controlled by solids content and solvent additions`
- `Monitor with Zahn cup or Brookfield viscometer`
- `Solvent evaporation from open tank raises viscosity over time`
- `Regular viscosity checks and solvent additions required`

---

### ZONE 5 -- Drainage and Drip Control

**Section label:** `DRAINAGE -- FROM DIP TANK TO CURE` -- Y: 21.7".

**Two-column layout (Y: 22.3" to 26.3"):**

**Left -- Batch Parts (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `BATCH PARTS -- DRAIN AND ROTATE` -- Barlow SemiBold, 18 pt, `#2EC4B6`

- `After withdrawal, excess coating drains by gravity`
- `Drain time: 10--60 sec before entering cure oven`
- `Rotate or invert parts to prevent thick drip edges at bottom`
- `Part orientation on rack matters: angle to direct drainage away from critical surfaces`
- `Higher viscosity = less drainage = more uniform but thicker`

**Right -- Wire / Cable (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `CONTINUOUS WIRE/CABLE -- AIR KNIVES` -- Barlow SemiBold, 18 pt, `#27AE60`

- `Line speed: 100--1,000+ ft/min`
- `Air knives or die strippers control final film thickness`
- `Precise, uniform coating at production speed`
- `Die strippers: wire passes through calibrated orifice`
- `Air knives: compressed air removes excess before cure`
- `Film uniformity is critical for electrical insulation properties`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 APPLICATION DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DRIP MARKS / CURTAINING | `#E05C5C` | Too-fast withdrawal or high viscosity; insufficient drain | Reduce withdrawal speed; lower viscosity; extend drain time |
| R1C2 | THIN SPOTS / BARE AREAS | `#E8A020` | Air pockets preventing wetting; low viscosity | Slower immersion; adjust part angle; raise viscosity |
| R1C3 | BRIDGING (HOLES/SLOTS) | `#E05C5C` | Coating spans across openings instead of coating edges | Reduce viscosity; increase drain time; redesign fixture |
| R2C1 | UNEVEN HOT-DIP THICKNESS | `#E8A020` | Thick/thin sections at different temperatures during dip | Extend preheat soak; uniform part mass distribution |
| R2C2 | PLASTISOL TOO THICK | `#2EC4B6` | Excessive dip time or high viscosity | Reduce dip time; lower viscosity; no preheat if not needed |
| R2C3 | WIRE COATING ECCENTRICITY | `#2EC4B6` | Wire off-center through die or air knife | Align guide rollers; center die orifice; check wire tension |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Application -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Dip coating parameters vary by coating formulation and part geometry. Consult your coating supplier for application-specific recommendations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-family comparison is the poster's anchor -- each family uses a completely different primary control variable for thickness. The counterintuitive solution dip behavior (slower withdrawal = thinner film) catches people, so it gets explicit emphasis. The Landau-Levich equation reference gives the technically curious reader a framework for understanding why withdrawal speed has that 2/3 power relationship to thickness. The wire/cable section is important because continuous dip coating of wire is one of the highest-volume coating operations in industry.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #681 -- Construction Workup v1.0*
*2026-04-26*
