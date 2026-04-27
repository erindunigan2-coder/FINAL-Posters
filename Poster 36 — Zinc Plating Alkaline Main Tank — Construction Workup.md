---
Project: Plating Posters Inc
Poster Number: 36
Title: "Zinc Plating (Alkaline) -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Alkaline non-cyanide zinc electroplating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #36 -- Construction Workup
## Zinc Plating (Alkaline) -- Main Tank

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 5 of 8. This is the heart of the process -- the main plating tank where zinc is electrodeposited onto the substrate. This poster is the most content-dense in the cluster, comparable to Poster #23 (Watts Nickel). It covers bath composition, operating parameters, anode setup, the NaOH:Zn ratio (the single most important control parameter), and a Hull cell diagnostic strip.

Hero visual: a plating tank cross-section showing anodes, cathode (workpiece), current flow lines, and zinc deposition.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Large tank with zinc anodes on both sides, cathode (workpiece) in the center, current flow lines (curved arrows from anode to cathode), zinc ion migration arrows, and labeled components. Built with rectangles, lines, and arrows.
2. **Bath composition panel (Block D):** Three-component breakdown (ZnO, NaOH, brightener) similar to Poster #23's pillar approach but adapted for zinc.
3. **Zn:NaOH ratio gauge (Block E):** A visual representation of the critical ratio -- bar gauge or slider showing the optimal range.
4. **Hull cell strip (Block G):** Similar to Poster #23 but for alkaline zinc -- different diagnostic patterns.
5. **Defect grid (Block F):** 6 common problems.

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
ZONE 4 -- BATH COMPOSITION + NaOH:Zn RATIO (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- HULL CELL STRIP + CONTAMINATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ZINC PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Alkaline Non-Cyanide -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where the zinc goes on. Bath chemistry, current density, and the critical NaOH:Zn ratio -- all on one wall.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated steel surface  -->  After: Zinc-coated substrate ready for passivation`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE ALKALINE ZINC PLATING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right anodes: same, X: 20.5"
- Label beneath each: `STEEL ANODES` JetBrains Mono 12 pt `#C8D0D8`
- Sub-label: `Insoluble mild steel (Zn replenished by ZnO addition)` Inter Regular 11 pt `#F0EDE8` at 60%

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small arrow labels on cathode surface: `Zn depositing` Inter Regular 11 pt `#27AE60`

**Current flow lines:**
- Curved arrows from anodes to cathode (6--8 lines)
- Stroke: 2 pt `#E8A020`, dashed
- Arrowheads pointing toward cathode
- Label: `Current flow (Zn2+ migration)` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` labels on wires running outward to left and right anode banks; `(-)` label on wire running down to center cathode

**Bath parameter labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `Zn: 10--14 g/L (1.3--1.9 oz/gal)` JetBrains Mono 14 pt `#27AE60`
- `NaOH: 100--140 g/L (13--19 oz/gal)` JetBrains Mono 14 pt `#2EC4B6`
- `Temp: 65--85 F (18--29 C)` JetBrains Mono 14 pt `#F0EDE8`
- `CD: 5--40 ASF (rack)` JetBrains Mono 14 pt `#E8A020`

Left side (X: 4.0", Y: 7.0"):
- `pH: > 12.5` JetBrains Mono 14 pt `#F0EDE8` at 70%
- `Cathode efficiency: 70--85%` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Anode CD: 5--20 ASF` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Ambient temperature -- no heating required. The alkaline zinc bath is one of the most energy-efficient plating processes.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Bath Composition + Zn:NaOH Ratio

**Section label:** `BATH CHEMISTRY -- THE THREE ESSENTIALS` -- Y: 14.7".

**ZONE 4 label (gauge):** `BATH CHEMISTRY + NaOH:Zn RATIO`

**BLOCK D -- Three-Component Breakdown (Y: 15.3" to 18.5")**

Three side-by-side callout boxes (similar to Poster #23 pillars but shorter):

| Component | X | W | Accent | Title |
|---|---|---|---|---|
| Zinc (as ZnO) | 0.5" | 7.33" | `#27AE60` | ZINC METAL |
| Sodium Hydroxide | 8.0" | 7.33" | `#2EC4B6` | CAUSTIC (NaOH) |
| Brightener System | 15.5" | 8.0" | `#E8A020` | BRIGHTENER |

Each box: Rounded rect H: 3.0", fill `#1E2435`, left accent 0.06".

*Zinc box:*
- `10--14 g/L (1.3--1.9 oz/gal)` JetBrains Mono 16 pt `#27AE60`
- `Source: ZnO dissolved in NaOH`
- `Role: provides Zn2+ ions for deposition`
- `Low Zn: dull, poor LCD coverage`
- `High Zn: rough, burning at HCD`

*Caustic box:*
- `100--140 g/L (13--19 oz/gal)` JetBrains Mono 16 pt `#2EC4B6`
- `Source: NaOH (sodium hydroxide)`
- `Role: dissolves ZnO, provides conductivity`
- `Low NaOH: poor throwing power, low efficiency`
- `High NaOH: excess H2 evolution, pitting`

*Brightener box:*
- `Per supplier TDS` JetBrains Mono 16 pt `#E8A020`
- `Source: Proprietary organic complexant`
- `Role: brightness, leveling, grain refinement`
- `Low: dull deposit, poor leveling`
- `High: stress, hazy deposit`

**BLOCK E -- Zn:NaOH Ratio Gauge (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `THE CRITICAL RATIO` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `NaOH:Zn Ratio (g/L to g/L)` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Red zone left: `< 8:1` fill `#E05C5C` at 40%
- Green zone center: `8:1 to 12:1` fill `#27AE60` at 40%
- Yellow zone: `12:1 to 14:1` fill `#E8A020` at 30%
- Red zone right: `> 14:1` fill `#E05C5C` at 40%
- Optimal marker: triangle at `10:1` -- `#27AE60`

Labels beneath gauge:
- `< 8:1: rough, burning` `#E05C5C` 12 pt
- `8:1 -- 12:1: OPTIMAL` `#27AE60` 14 pt (bold)
- `> 14:1: dull, poor coverage` `#E05C5C` 12 pt

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3". Same construction as Poster #23 defect grid.

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DULL DEPOSIT | `#2EC4B6` | Low zinc or low brightener | Add ZnO; Hull cell brightener check |
| R1C2 | BURNING (HCD) | `#E8A020` | High zinc, high CD, or low NaOH | Reduce CD; adjust NaOH:Zn ratio |
| R1C3 | PITTING | `#E05C5C` | Organic contamination or H2 gas | Carbon treat; check brightener level |
| R2C1 | DARK LCD | `#E05C5C` | Metallic contamination (Cu, Pb) | Dummy plate 2--5 ASF |
| R2C2 | ROUGH/GRAINY | `#E8A020` | Particulate, torn anode bags | Inspect bags; increase filtration |
| R2C3 | POOR THROWING | `#2EC4B6` | Low NaOH or low NaOH:Zn ratio | Increase caustic; check ratio |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Hull Cell + Contamination

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Hull Cell Strip (X: 0.5", W: 11.0"):**

Section label: `THE HULL CELL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.
Test conditions: `267 mL | 2 A | 5 min | 75 F` JetBrains Mono 12 pt at 60%.

Panel strip: 5 segments, X: 0.5", Y: 27.5", W: 11.0", H: 1.5".

| Segment | Fill | Label | Diagnosis |
|---|---|---|---|
| HCD edge | `#E8A020` at 40% | `HCD` | `Burned = low NaOH or high Zn` |
| Upper mid | `#27AE60` at 50% | | `Smooth/bright = good` |
| Center | `#27AE60` at 70% | `OPTIMAL` | `Bright + level = balanced` |
| Lower mid | `#27AE60` at 40% | | `Semi-bright = acceptable` |
| LCD edge | `#3A4055` at 60% | `LCD` | `Dull/dark = low Zn or contamination` |

Good panel note: `Good ANC zinc panel: bright across 60--70% of width. LCD slightly dull is normal.` Inter Medium 13 pt `#27AE60`.

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

Section label: `CONTAMINATION THRESHOLDS` Barlow Condensed ExtraBold 22 pt.

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 5 ppm | Dark LCD, black spots |
| Lead | > 2 ppm | Dark LCD, brittle deposit |
| Iron | > 50 ppm | Rough, dull deposit |
| Chromium | > 1 ppm | Dull, poor coverage |
| Organic (oil) | visible | Pitting, poor adhesion |
| Carbonate | > 30 g/L | Reduced conductivity, rough |

Threshold values in `#E05C5C`. Carbonate row note: `Freeze-out at < 35 F (2 C) to remove excess carbonate` Inter Regular 11 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Zinc Plating (Alkaline) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; Metal Finishing Guidebook; typical ANC zinc bath parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Zinc Plating Alkaline Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-01 cluster -- comparable to Poster #23 in information density. The Zn:NaOH ratio gauge is the most important single visual on the poster. Every alkaline zinc plater needs to understand this ratio. The Hull cell strip is specific to ANC zinc (different pattern than Watts nickel -- LCD dullness is more normal in zinc, and the bright range is narrower).

---

*Elara -- Poster #36 -- Construction Workup v1.0 -- 2026-04-25*
