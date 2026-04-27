---
Project: Plating Posters Inc
Poster Number: 387
Title: "Bath Setup -- Ultrasonic Cleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- bath preparation, solution selection, and equipment setup
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - BathSetup
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #387 -- Construction Workup
## Bath Setup -- Ultrasonic Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Before a single part goes in the tank, the bath must be right. Solution selection, concentration, temperature, degassing, solution level, and filtration -- get any of these wrong and the most expensive ultrasonic system in the world will clean no better than a soak tank. This poster is the setup checklist.

Hero visual: a tank cross-section showing solution level, transducers, filtration loop, and heater -- with parameter callouts for every critical variable.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Tank cross-section hero (Block B):** Tank showing transducers (bottom-mounted), solution level line, heater, filtration loop, and basket position. Built with rectangles and lines.
2. **Solution selection table (Block D):** Five-row application-to-solution matrix.
3. **Critical bath parameters panel (Block E):** Four parameters with "if wrong" consequences.
4. **Maintenance schedule (Block F):** Frequency-based task list.

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
  Stage 2 highlighted (Teal) -- "Bath Prep"
ZONE 3 -- TANK CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SOLUTION SELECTION TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- CRITICAL PARAMETERS + CONSEQUENCES (20.5"--26.5" / ~6.0")
ZONE 6 -- MAINTENANCE SCHEDULE (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `BATH SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ultrasonic Cleaning -- Solution, Temperature, and Equipment` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The ultrasonic generator creates the cavitation. The bath chemistry does the cleaning. Get both right or get neither.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Empty/spent tank --> After: Degassed, heated, filtered bath ready for production`

---

### ZONE 3 -- Tank Cross-Section Hero

**Section label:** `THE ULTRASONIC CLEANING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.0"
- Fill: `#252B3D` (solution)
- Border: 3 pt `#C8D0D8`

**Transducers (bottom-mounted):**
- 4 rectangles across bottom interior, W: 3.5", H: 0.4", fill `#E8A020` at 60%, border 1 pt `#E8A020`
- Label: `TRANSDUCERS` JetBrains Mono 12 pt `#E8A020`
- Sub-label: `Piezoelectric elements convert electrical energy to ultrasonic waves` Inter Regular 11 pt `#F0EDE8` at 60%

**Solution level line:**
- Dashed line across tank at Y: 6.0", stroke 2 pt `#2EC4B6`
- Label right: `SOLUTION LEVEL` JetBrains Mono 12 pt `#2EC4B6`
- Sub-label: `Covers transducers + 2--4" minimum` Inter Regular 11 pt `#F0EDE8` at 60%

**Heater element (side-mounted):**
- Vertical rect, X: 3.0", Y: 6.5", W: 0.5", H: 4.0", fill `#E05C5C` at 40%, border 1 pt `#E05C5C`
- Label: `HEATER` JetBrains Mono 12 pt `#E05C5C`

**Filtration loop (external):**
- Rectangle on right side of tank (pump + filter symbol), X: 22.5", Y: 8.0"
- Arrow from tank bottom-right out to filter, arrow returning to tank top-right
- Label: `FILTRATION` JetBrains Mono 12 pt `#27AE60`
- Sub-label: `5--25 micrometer continuous` Inter Regular 11 pt `#F0EDE8` at 60%

**Basket position (inside tank):**
- Dashed-outline rect centered in tank, W: 10.0", H: 3.5", stroke 2 pt `#C8D0D8` dashed
- Label above: `BASKET ZONE` Barlow SemiBold 14 pt `#F0EDE8`
- Note below: `Wire mesh basket ONLY -- solid bottoms block cavitation` Inter Medium 12 pt `#E05C5C`

**Parameter callouts (inside tank):**
Right side:
- `Temp: 120--150 F (50--65 C)` JetBrains Mono 14 pt `#2EC4B6`
- `Concentration: 30--60 g/L` JetBrains Mono 14 pt `#27AE60`
- `Power density: 5--10 W/L` JetBrains Mono 14 pt `#E8A020`

Left side:
- `pH: 9--12 (alkaline)` JetBrains Mono 14 pt `#F0EDE8` at 70%
- `Filtration: 5--25 um` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.0"):**
- `DEGAS FIRST: Run ultrasonics 10--15 minutes with no parts. Dissolved gas cushions bubble collapse -- degassed solution cleans dramatically better.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Solution Selection Table

**Section label:** `SOLUTION SELECTION BY APPLICATION` -- Y: 14.7".

**BLOCK D -- Five-Row Application Matrix**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Application (5.0") | Solution (5.5") | Concentration (4.0") | Temperature (4.0") | Notes (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Application | Solution | Concentration | Temperature | Notes |
|---|---|---|---|---|
| General metals (steel, SS, brass) | Alkaline cleaner (mild, non-silicated) | 30--60 g/L (4--8 oz/gal) | 120--150 F (50--65 C) | Most common setup |
| Aluminum parts | Mildly alkaline or neutral pH | 20--40 g/L; pH 8--10 | 115--130 F (45--55 C) | Avoid high caustic |
| Precision / electronics | Neutral enzymatic or DI water | Per manufacturer | 105--120 F (40--50 C) | Particle removal focus |
| Heavy oil removal | Alkaline + enhanced surfactant | Per manufacturer | 130--150 F (55--65 C) | May need pre-clean |
| Solvent ultrasonic | Modified alcohol, HFE, or IPA | Neat (100%) | Ambient--105 F | No water rinse after |

Data: JetBrains Mono Regular, 12 pt. Application names: Inter Medium 13 pt.

---

### ZONE 5 -- Critical Parameters + Consequences

**Section label:** `FOUR PARAMETERS THAT MAKE OR BREAK CLEANING` -- Y: 20.7".

**BLOCK E -- Four Parameter Cards**

Y: 21.3" to 26.3". 2x2 grid.

Each card: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06", radius 6.

| Card | Position | Parameter | Optimal | Too Low | Too High |
|---|---|---|---|---|---|
| 1 | R1C1 (X: 0.5") | TEMPERATURE | 120--150 F aqueous | Reduced cavitation and chemical activity | Vapor cushions collapse -- LESS cleaning, not more |
| 2 | R1C2 (X: 12.0") | DEGASSING | 10--15 min before loading | Dissolved gas cushions collapse; poor cleaning | N/A -- cannot over-degas |
| 3 | R2C1 (X: 0.5") | SOLUTION LEVEL | Covers transducers + 2--4" | Poor cavitation; uneven cleaning; transducer damage | Reduced surface cavitation |
| 4 | R2C2 (X: 12.0") | FILTRATION | 5--25 micrometer continuous | Removed particles re-deposit on parts | N/A -- finer is better |

Interior per card:
- Parameter: Barlow SemiBold, 18 pt, `#2EC4B6`
- Optimal: JetBrains Mono 14 pt `#27AE60`
- Too Low / Too High: Inter Regular, 13 pt, `#E05C5C`

**Key insight callout (Y: 25.8"):**
- Rounded rect, full width, H: 0.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `Temperature has an OPTIMUM -- not "hotter is better." Above ~160 F, vapor formation cushions cavitation collapse and cleaning power drops.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Maintenance Schedule

**Section label:** `MAINTENANCE SCHEDULE` -- Y: 26.7".

**BLOCK F -- Maintenance Table**

Y: 27.3" to 32.3". Column widths (23.0" total):
- Task (8.0") | Frequency (5.0") | Why (10.0")

| Task | Frequency | Why |
|---|---|---|
| Titrate cleaner concentration | Daily (production lines) | Concentration drops as soil load accumulates |
| Check/replace solution | Weekly to monthly | Depends on soil loading; dirty solution re-contaminates |
| Clean tank interior (drain + wipe) | Monthly | Remove sludge buildup from bottom and walls |
| Inspect transducers | Monthly | Check for delamination, cracking, hot spots |
| Replace transducers | Per manufacturer (5,000--10,000 hrs typical) | Performance degrades gradually -- monitor output |
| Aluminum foil test | Monthly or after service | Quick cavitation distribution check |

Data: Inter Regular 13 pt. Task names: Inter Medium 14 pt.

---

### ZONE 7 -- Footer

Standard. Title: `Bath Setup -- Ultrasonic Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Solution types, concentrations, and equipment specifications vary by manufacturer. Consult your equipment manual and chemical supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Bath Setup Ultrasonic -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The temperature-has-an-optimum insight is the single most valuable piece of information on this poster. Most operators assume hotter is always better -- wrong for ultrasonic. The degassing step is the second most commonly skipped step. The tank cross-section hero should make the spatial relationships clear: transducers on bottom, basket elevated on a rack (never touching bottom), filtration loop external, heater on the side.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #387 -- Construction Workup v1.0*
*2026-04-26*
