---
Project: Plating Posters Inc
Poster Number: 60
Title: "Nickel Plating (Watts) -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Watts nickel plating main tank -- NiSO4 + NiCl2 + H3BO3 bath. The most widely used nickel plating formulation worldwide since 1916. Covers bath composition, operating parameters, anode setup, brightener system, and contamination thresholds.
Process Scope: Watts nickel plating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #60 -- Construction Workup
## Nickel Plating (Watts) -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the process -- the main plating tank where nickel is electrodeposited onto the substrate. This poster is the most content-dense in the EP-04 cluster. It covers bath composition, operating parameters, anode setup, the brightener system (Class I carriers + Class II brighteners + wetting agent), and a Hull cell diagnostic strip. pH is the master control variable.

Hero visual: a plating tank cross-section showing nickel anodes, cathode (workpiece), current flow lines, and nickel deposition.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Large tank with nickel anodes on both sides, cathode in center, current flow lines, and labeled components.
2. **Bath composition panel (Block D):** Three-component breakdown (NiSO4, NiCl2, H3BO3).
3. **pH control gauge (Block E):** Visual representation of the critical pH range.
4. **Hull cell strip (Block G):** Watts nickel diagnostic patterns.
5. **Defect grid (Block F):** 6 common problems.
6. **Contamination thresholds (Block H):** Metal contaminant limits.

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
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH COMPOSITION + pH CONTROL (14.5"--20.5" / ~6.0")
  Block D: Three-component breakdown
  Block E: pH gauge
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
  Block F: 6 common defects
ZONE 6 -- HULL CELL STRIP + CONTAMINATION (26.5"--32.5" / ~6.0")
  Block G: Hull cell strip
  Block H: Contamination thresholds
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NICKEL PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Watts Bath -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where the nickel goes on. pH is the master variable. Control the pH and everything else follows.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated substrate --> After: Nickel-plated surface ready for chrome, gold, or topcoat`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE WATTS NICKEL PLATING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right anodes: same, X: 20.5"
- Label beneath each: `Ni ANODES (S-ROUNDS)` JetBrains Mono 12 pt `#C8D0D8`
- Sub-label: `99.9%+ Ni in Ti baskets, double-bagged` Inter Regular 11 pt `#F0EDE8` at 60%

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small arrow labels on cathode surface: `Ni depositing` Inter Regular 11 pt `#27AE60`

**Current flow lines:**
- Curved arrows from anodes to cathode (6--8 lines)
- Stroke: 2 pt `#E8A020`, dashed
- Arrowheads pointing toward cathode
- Label: `Current flow (Ni2+ migration)` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` to anodes; `(-)` to cathode

**Bath parameter labels (inside tank):**

Right side (X: 15.0", Y: 7.0"):
- `NiSO4: 270--330 g/L (36--44 oz/gal)` JetBrains Mono 14 pt `#27AE60`
- `NiCl2: 37--55 g/L (5--7 oz/gal)` JetBrains Mono 14 pt `#2EC4B6`
- `H3BO3: 37--45 g/L (5--6 oz/gal)` JetBrains Mono 14 pt `#E8A020`
- `Ni metal: 60--90 g/L total` JetBrains Mono 13 pt `#F0EDE8`

Left side (X: 4.0", Y: 7.0"):
- `pH: 3.8--4.2` JetBrains Mono 16 pt `#27AE60` (prominent)
- `Temp: 130--150 F (54--66 C)` JetBrains Mono 14 pt `#F0EDE8`
- `CD: 30--50 ASF (rack)` JetBrains Mono 14 pt `#E8A020`
- `CD: 8--15 ASF (barrel)` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Cathode eff: 92--98%` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `A:C ratio: 1:1 to 2:1` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Heated bath (130--150 F). Below 115 F: poor brightness, high stress. Above 160 F: brightener destruction, soft deposit.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Bath Composition + pH Control

**Section label:** `BATH CHEMISTRY -- THE THREE ESSENTIALS` -- Y: 14.7".

**BLOCK D -- Three-Component Breakdown (Y: 15.3" to 18.5")**

Three side-by-side callout boxes:

| Component | X | W | Accent | Title |
|---|---|---|---|---|
| Nickel Sulfate | 0.5" | 7.33" | `#27AE60` | NICKEL SULFATE |
| Nickel Chloride | 8.0" | 7.33" | `#2EC4B6` | NICKEL CHLORIDE |
| Boric Acid | 15.5" | 8.0" | `#E8A020` | BORIC ACID |

Each box: Rounded rect H: 3.0", fill `#1E2435`, left accent 0.06".

*Nickel Sulfate box:*
- `270--330 g/L (36--44 oz/gal)` JetBrains Mono 16 pt `#27AE60`
- `Source: NiSO4 * 6H2O`
- `Role: Primary Ni2+ source (~22% Ni by weight)`
- `Low: thin deposit, poor coverage`
- `High: no significant penalty (bath is forgiving)`

*Nickel Chloride box:*
- `37--55 g/L (5--7 oz/gal)` JetBrains Mono 16 pt `#2EC4B6`
- `Source: NiCl2 * 6H2O (~25% Ni by weight)`
- `Role: Anode depolarization + conductivity`
- `Low: anode passivation --> metal depletion, pH rise, voltage spike`
- `High: increased internal stress`

*Boric Acid box:*
- `37--45 g/L (5--6 oz/gal)` JetBrains Mono 16 pt `#E8A020`
- `Source: H3BO3`
- `Role: Cathode film pH buffer (prevents Ni(OH)2 co-deposition)`
- `Low: pitting, burning, poor LCD coverage`
- `High: precipitation risk below operating temperature`
- Solubility note: `Solubility: 39 g/L at 68 F, 54 g/L at 140 F. Maintain near saturation for operating temp.` Inter Regular 11 pt `#F0EDE8` at 60%

**BLOCK E -- pH Control Gauge (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `THE MASTER VARIABLE` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `Bath pH` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge:
- Red zone left: `< 3.5` fill `#E05C5C` at 40%
- Green zone center: `3.8 -- 4.2` fill `#27AE60` at 40%
- Yellow zone: `4.2 -- 4.5` fill `#E8A020` at 30%
- Red zone right: `> 4.5` fill `#E05C5C` at 40%
- Optimal marker: triangle at `4.0` -- `#27AE60`

Labels:
- `< 3.5: low efficiency, brittle, poor LCD` `#E05C5C` 12 pt
- `3.8--4.2: OPTIMAL` `#27AE60` 14 pt (bold)
- `> 4.5: dark deposit, Ni(OH)2, stress, peeling` `#E05C5C` 12 pt

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING | `#E05C5C` | Low wetting agent, oil contamination, poor agitation | Add anti-pit; carbon treat; improve filtration |
| R1C2 | BURNING (HCD) | `#E8A020` | CD too high, low metal, high pH, low H3BO3 | Reduce CD; add NiSO4; check boric acid |
| R1C3 | DULL / MILKY | `#2EC4B6` | Organic contamination, metallic impurities | Carbon treat; low-pH dummy (pH 3.0, 2--5 ASF) |
| R2C1 | PEELING | `#E05C5C` | Poor cleaning, inadequate activation, no strike on stainless | Improve clean; check water-break test |
| R2C2 | DARK LCD | `#E8A020` | Cu, Cr contamination; high pH; low brightener | Dummy plate; adjust pH; Hull cell check |
| R2C3 | HIGH STRESS / CRACKING | `#2EC4B6` | Low primary brightener, excess secondary, organic breakdown | Adjust brightener balance; carbon treat |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Hull Cell Strip + Contamination

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Hull Cell Strip (X: 0.5", W: 11.0"):**

Section label: `THE HULL CELL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.
Test conditions: `267 mL | 2 A | 10 min | 140 F` JetBrains Mono 12 pt at 60%.

Panel strip: 5 segments, X: 0.5", Y: 27.5", W: 11.0", H: 1.5".

| Segment | Fill | Label | Diagnosis |
|---|---|---|---|
| HCD edge | `#E8A020` at 40% | `HCD` | `Burned = high CD or low H3BO3` |
| Upper mid | `#27AE60` at 50% | | `Bright + level = good brightener balance` |
| Center | `#27AE60` at 70% | `OPTIMAL` | `Full brightness = balanced bath` |
| Lower mid | `#27AE60` at 40% | | `Semi-bright = acceptable; check primary brightener` |
| LCD edge | `#3A4055` at 60% | `LCD` | `Dull/dark = metallic contamination or low brightener` |

Good panel note: `Good Watts panel: bright across 70--80% of width. LCD slightly dull is acceptable. Full-panel brightness indicates well-maintained bath with good brightener balance.` Inter Medium 13 pt `#27AE60`.

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

Section label: `CONTAMINATION THRESHOLDS` Barlow Condensed ExtraBold 22 pt.

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 5 ppm | Dark/black LCD, tree growths at HCD |
| Zinc | > 10 ppm | Dull, streaky deposits, peeling |
| Iron | > 25 ppm | Roughness, dark LCD, co-deposited iron |
| Chromium (Cr6+) | > 1 ppm | Skip plating, then dark at all CDs |
| Lead | > 1 ppm | Dark streaks, embrittlement |
| Organic (decomposed) | Variable | Pitting, haze, brittleness, peeling |

Threshold values in `#E05C5C`.

Remediation note: `Low-pH dummying (pH 3.0, 2--5 ASF, 4--8 hr) removes Cu, Zn, and other metals. Carbon treatment (2--5 g/L, stir 2--4 hr, filter through pre-coat) removes organics. H2O2 (0.5--1 mL/L of 30%) oxidizes Fe2+ for filtration.` Inter Regular 12 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Nickel Plating (Watts) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Modern Electroplating; ASM Handbook Vol. 5; Nickel Institute publications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Nickel Watts Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-04 cluster -- comparable to Poster #36 (Alkaline Zinc Main Tank) in information density. The pH gauge is the most important single visual on the poster. Every Watts nickel plater needs to internalize pH 3.8--4.2 as the target. The Hull cell strip is specific to Watts nickel -- brighter across a wider range than alkaline zinc, with different diagnostic patterns. The contamination threshold table is a daily reference for troubleshooting -- many platers will use this more than any other section. Note the minimum temperature callout: 115 F is the floor for acceptable Watts nickel performance. Below that, you are fighting the bath.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #60 -- Construction Workup v1.0*
*2026-04-26*
