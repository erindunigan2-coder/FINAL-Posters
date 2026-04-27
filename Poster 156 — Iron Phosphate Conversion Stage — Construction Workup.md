---
Project: Plating Posters Inc
Poster Number: 156
Title: "Iron Phosphate -- Conversion Stage"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-01 technical reference (iron phosphate conversion coating)"
Process Scope: Iron phosphate conversion coating main stage -- bath chemistry, operating parameters, coating formation mechanism, and coating weight control
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IronPhosphate
  - ConversionCoating
  - MainStage
  - ConstructionWorkup
  - ClusterCC01
---

# Poster #156 -- Construction Workup
## Iron Phosphate -- Conversion Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The main event. This is where the iron phosphate film actually forms on the steel surface. This poster is the densest in the CC-01 cluster -- it covers the chemical mechanism (acid attack --> pH rise --> precipitation), bath chemistry components, spray vs. immersion parameters, the free acid / total acid ratio, coating weight interpretation, and the accelerator role. Comparable in density to Poster #36 (Zinc Alkaline Main Tank).

Hero visual: a spray/immersion tank cross-section showing the phosphate solution contacting steel, with the coating formation mechanism illustrated at the metal-solution interface.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Coating formation hero (Block B -- HERO):** Tank cross-section showing phosphate solution attacking steel, with a magnified inset of the metal-solution interface showing the 4-step mechanism.
2. **Bath chemistry panel (Block D):** Component table with concentrations and functions.
3. **Free acid / Total acid ratio gauge (Block E):** Visual ratio representation.
4. **Coating weight interpretation chart (Block F):** Range bar showing too light / ideal / too heavy.
5. **Defect grid (Block G):** 5 common coating defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Coating stage highlighted (Amber)
ZONE 3 -- COATING FORMATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH CHEMISTRY + FA/TA RATIO (14.5"--20.5" / ~6.0")
ZONE 5 -- COATING WEIGHT INTERPRETATION (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `IRON PHOSPHATE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Conversion Coating Stage -- Where Paint Adhesion Is Made` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `An amorphous iron phosphate film, 40--60 mg/ft2, invisible to the eye but critical to every paint job. Control the acid. Control the weight. Control the result.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Coating stage highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, active steel surface  -->  After: Amorphous iron phosphate film (iridescent blue to gold)`

---

### ZONE 3 -- Coating Formation Hero

**Section label:** `HOW THE COATING FORMS` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section + Mechanism Inset**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 5.5"
- Fill: `#E8A020` at 8% (phosphate solution tint)
- Border: 2 pt `#E8A020`
- Label: `IRON PHOSPHATE SOLUTION` Barlow SemiBold 16 pt `#E8A020`

**Steel part (inside tank):**
- Rectangle, X: 8.0", Y: 6.5", W: 8.0", H: 3.0", fill `#C8D0D8`, border 2 pt `#3A4055`
- Label above: `STEEL WORKPIECE` Barlow SemiBold 14 pt `#F0EDE8`

**Solution parameters (left side of tank, X: 2.5", Y: 6.5"):**
- `pH: 3.5--5.5` JetBrains Mono 14 pt `#E8A020`
- `Temp: 100--150 F (38--66 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Free acid: 0.5--3.0 pts` JetBrains Mono 13 pt `#F0EDE8`
- `Total acid: 4--15 pts` JetBrains Mono 13 pt `#F0EDE8`
- `FA:TA ratio: 1:4 to 1:8` JetBrains Mono 13 pt `#E8A020`

**Spray nozzles (if spray system -- show both options):**
- Small triangle nozzle shapes above part
- Label: `Spray: 1--3 min | 15--25 psi` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Mechanism inset (right side, X: 12.0", Y: 11.5", W: 11.0", H: 2.3"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`
- Title: `COATING MECHANISM` Barlow SemiBold 14 pt `#E8A020`

Four numbered steps (JetBrains Mono 12 pt `#F0EDE8`):
```
1. ACID ATTACK: H3PO4 dissolves iron --> Fe2+
2. pH RISE: Local pH increases at metal surface
3. PRECIPITATION: FePO4 film deposits (amorphous)
4. ACCELERATOR: Oxidizes Fe2+ to Fe3+ --> FePO4 (strengite)
```

Step numbers: `#E8A020`. Text: `#F0EDE8`.

**Bottom callout (Y: 13.5"):**
- `The coating is AMORPHOUS -- no crystal structure. Film weight, not crystal size, is what you control.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Bath Chemistry + FA/TA Ratio

**Section label:** `BATH CHEMISTRY -- COMPONENTS AND CONTROL` -- Y: 14.7".

**BLOCK D -- Component Table (Y: 15.3" to 18.5")**

Full-width parameter table:

| Component | Concentration | Function |
|---|---|---|
| Phosphoric acid (as H3PO4) | 5--15 g/L (0.7--2.0 oz/gal) | Primary film-forming agent |
| Sodium dihydrogen phosphate | 10--30 g/L | Phosphate source, pH buffer |
| Sodium nitrite (NaNO2) | 0.1--0.5 g/L | Accelerator / oxidant |
| Sodium molybdate (optional) | 0.05--0.2 g/L | Accelerator (non-nitrite systems) |
| Surfactants (nonionic) | 0.5--2.0 g/L | Wetting (cleaner-coater formulations) |
| Fluoride (optional) | 0.5--2.0 g/L as F- | Aluminum / galvanized compatibility |

Header: Barlow SemiBold 14 pt `#F0EDE8`, fill `#3A4055`. Data: JetBrains Mono 12 pt `#F0EDE8`, alternating rows.

**BLOCK E -- Free Acid / Total Acid Ratio Gauge (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `THE CRITICAL RATIO` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `Free Acid : Total Acid` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Red zone left: `< 1:4` fill `#E05C5C` at 40% -- `High free acid = heavy/powdery coating`
- Green zone center: `1:4 to 1:8` fill `#27AE60` at 40% -- `OPTIMAL`
- Red zone right: `> 1:8` fill `#E05C5C` at 40% -- `Low free acid = light/no coating`
- Optimal marker: triangle at `1:6` -- `#27AE60`

Labels: JetBrains Mono 12 pt. Red labels `#E05C5C`, green label `#27AE60` 14 pt bold.

---

### ZONE 5 -- Coating Weight Interpretation

**Section label:** `COATING WEIGHT -- THE NUMBER THAT MATTERS` -- Y: 20.7".

**BLOCK F -- Coating Weight Range Bar (Y: 21.3" to 24.5")**

Full-width rounded rect, fill `#1E2435`.

Horizontal range bar (X: 2.0", W: 20.0", H: 0.8"):
- `< 20 mg/ft2` fill `#E05C5C` at 40% -- `Too light -- poor paint adhesion`
- `20--40 mg/ft2` fill `#E8A020` at 30% -- `Acceptable for non-critical`
- `40--60 mg/ft2` fill `#27AE60` at 50% -- `IDEAL RANGE`
- `60--80 mg/ft2` fill `#E8A020` at 30% -- `Acceptable but approaching heavy`
- `> 80 mg/ft2` fill `#E05C5C` at 40% -- `Too heavy -- powdery, chalking`

Optimal marker: triangle at 50 mg/ft2 -- `#27AE60`.

**Film properties callout (Y: 25.0" to 26.3"):**

Two columns:

| Property | Value |
|---|---|
| Appearance | Iridescent blue to gold to gray-blue |
| Thickness | 0.25--1.0 um (0.01--0.04 mil) |
| Crystal structure | Amorphous to microcrystalline |
| Bare salt spray | 2--24 hours (NOT standalone protection) |
| Primary purpose | PAINT ADHESION -- not bare corrosion resistance |

`PAINT ADHESION` in `#E8A020` bold. `NOT standalone protection` in `#E05C5C`.

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 5 COMMON DEFECTS` -- Y: 26.7".

**BLOCK G -- Defect Cards (Y: 27.3" to 32.3")**

Top row: 3 cards. Bottom row: 2 cards centered.

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BARE SPOTS | `#E05C5C` | Oil contamination, silicate residue, low acid | Improve cleaning; eliminate silicates |
| R1C2 | HEAVY/POWDERY | `#E8A020` | Excess acid, excess time, high temp, dead accelerator | Reduce conc/time/temp; replenish accelerator |
| R1C3 | FLASH RUST | `#E05C5C` | Dwell too long between phosphate and rinse | Speed up transfer; improve line flow |
| R2C1 | YELLOWING | `#E8A020` | Excess nitrite accelerator; iron buildup | Reduce accelerator; partial bath dump |
| R2C2 | POOR PAINT ADHESION | `#E05C5C` | Coating weight outside 40--60 mg/ft2; poor cleaning | Optimize coating weight; improve cleaning |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Iron Phosphate -- Conversion Stage`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; Products Finishing; TT-C-490; ASTM D2092.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Iron Phosphate Conversion Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the CC-01 cluster. The coating formation mechanism (acid attack --> pH rise --> precipitation --> accelerator) must be clearly illustrated -- it is the same fundamental mechanism as zinc phosphate, just simpler. The FA:TA ratio gauge and coating weight range bar are the two most important diagnostic visuals. Every iron phosphate operator should be able to glance at this poster and know whether their bath is in spec.

The "PAINT ADHESION -- not bare corrosion resistance" message must be unmistakable. Too many shops think iron phosphate provides standalone protection. It does not. The paint does the protecting; the phosphate makes the paint stick.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #156 -- Construction Workup v1.0*
*2026-04-26*
