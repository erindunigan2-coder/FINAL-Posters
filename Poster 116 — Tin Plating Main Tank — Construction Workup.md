---
Project: Plating Posters Inc
Poster Number: 116
Title: "Tin Plating -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid tin electroplating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #116 -- Construction Workup
## Tin Plating -- Main Tank

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the process -- the main plating tank where tin is electrodeposited onto the substrate. This poster is the densest in the EP-11 cluster. It covers both acid sulfate and MSA bath compositions, operating parameters, anode setup, the critical Sn2+/Sn4+ oxidation challenge, and a Hull cell diagnostic strip. The single most important message: keep stannous alive or the bath dies.

Hero visual: a plating tank cross-section showing pure tin anodes, cathode (workpiece), current flow lines, and tin deposition -- with emphasis on oxygen exclusion (no air agitation).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Large tank with tin anodes on both sides, cathode in center, current flow, and a prominent "NO AIR" symbol to emphasize no air agitation.
2. **Bath composition panels (Block D):** Side-by-side acid sulfate and MSA bath chemistry.
3. **Sn2+/Sn4+ oxidation gauge (Block E):** Visual showing the balance between good stannous and bad stannic tin.
4. **Defect grid (Block F):** 6 common tin plating defects.
5. **Hull cell strip + contamination thresholds (Block G).**

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
ZONE 4 -- BATH COMPOSITION + Sn2+/Sn4+ (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- HULL CELL + CONTAMINATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TIN PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Acid Tin -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where the tin goes on. Keep the stannous alive, keep the air out, and keep the temperature down -- or watch the bath turn to sludge.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated surface  -->  After: Tin-coated substrate ready for post-treatment`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE ACID TIN PLATING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right anodes: same, X: 20.5"
- Label beneath each: `PURE TIN ANODES` JetBrains Mono 12 pt `#C8D0D8`
- Sub-label: `99.9%+ Sn bars or balls in Ti baskets` Inter Regular 11 pt `#F0EDE8` at 60%

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small annotation: `Sn2+ depositing as metallic Sn` Inter Regular 11 pt `#27AE60`

**Current flow lines:**
- Curved arrows from anodes to cathode (6--8 lines)
- Stroke: 2 pt `#E8A020`, dashed
- Label: `Current flow (Sn2+ migration)` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` to anodes, `(-)` to cathode

**"NO AIR AGITATION" warning (prominent, inside tank):**
- Rounded rect, X: 7.0", Y: 10.0", W: 10.0", H: 1.2", fill `#E05C5C` at 20%, border 2 pt `#E05C5C`
- Text: `NO AIR AGITATION -- use mechanical or cathode rod agitation only` Barlow SemiBold 14 pt `#E05C5C`
- Sub-text: `Air dissolves oxygen into bath, oxidizing Sn2+ to Sn4+` Inter Regular 12 pt `#E05C5C`

**Bath parameter labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `Sn2+: 20--30 g/L (sulfate) / 30--40 g/L (MSA)` JetBrains Mono 13 pt `#27AE60`
- `Acid: 130--170 g/L H2SO4 / 150--200 g/L MSA` JetBrains Mono 13 pt `#2EC4B6`
- `Temp: 60--85 F (16--29 C)` JetBrains Mono 14 pt `#F0EDE8`
- `CD: 10--30 ASF rack (sulfate)` JetBrains Mono 13 pt `#E8A020`
- `CD: 10--100 ASF rack (MSA)` JetBrains Mono 13 pt `#E8A020`

Left side (X: 4.0", Y: 7.0"):
- `Cathode eff: 85--95% (sulfate) / 90--99% (MSA)` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `A:C ratio: 1:1 to 2:1` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Anode bags: Required (polypropylene)` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Filtration: Continuous` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Low temperature operation is critical. Above 90 F, Sn2+ oxidation accelerates and grain structure coarsens.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Bath Composition + Sn2+/Sn4+ Balance

**Section label:** `BATH CHEMISTRY -- TWO SYSTEMS` -- Y: 14.7".

**BLOCK D -- Side-by-Side Bath Composition (Y: 15.3" to 18.5")**

Two callout boxes:

**Left -- Acid Sulfate Bath:**
- Rounded rect, X: 0.5", W: 11.0", H: 3.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `ACID SULFATE TIN` Barlow SemiBold 18 pt `#2EC4B6`

| Component | Range | Optimal |
|---|---|---|
| Stannous sulfate (SnSO4) | 30--80 g/L | 40--60 g/L |
| Tin metal (Sn2+) | 15--45 g/L | 20--30 g/L |
| Sulfuric acid (H2SO4) | 100--200 g/L | 130--170 g/L |
| Antioxidant | Per supplier | Per supplier |
| Wetting agent | Per supplier | Per supplier |

**Right -- MSA Bath:**
- Rounded rect, X: 12.0", W: 11.5", H: 3.0", fill `#1E2435`, left accent `#27AE60`
- Title: `MSA TIN` Barlow SemiBold 18 pt `#27AE60`

| Component | Range | Optimal |
|---|---|---|
| Stannous methane sulfonate | 40--100 g/L | 60--80 g/L |
| Tin metal (Sn2+) | 20--55 g/L | 30--40 g/L |
| Free MSA | 100--250 g/L | 150--200 g/L |
| Antioxidant | Per supplier | Per supplier |
| Grain refiner | Per supplier | Per supplier |

**BLOCK E -- Sn2+/Sn4+ Oxidation Gauge (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `THE CRITICAL BALANCE` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `Stannous (Sn2+) vs. Stannic (Sn4+)` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Green zone (large, left): `Sn2+ DOMINANT` fill `#27AE60` at 40%
- Yellow zone (narrow): `Sn4+ rising` fill `#E8A020` at 30%
- Red zone (right): `Sn4+ PRECIPITATING` fill `#E05C5C` at 40%

Labels beneath gauge:
- `Sn2+ > 90% of total Sn: GOOD` `#27AE60` 14 pt
- `Sn4+ visible as white sludge: TREAT IMMEDIATELY` `#E05C5C` 12 pt

Bottom note: `Minimize air contact. Use antioxidants. Keep temperature below 85 F. These three rules control Sn4+.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DULL DEPOSIT | `#2EC4B6` | Sn4+ buildup, organic contamination, low brightener | Carbon treat; add antioxidant; Hull cell |
| R1C2 | ROUGH / GRITTY | `#E8A020` | Stannic sludge, anode sludge, poor filtration | Increase filtration; inspect anode bags |
| R1C3 | DARK DEPOSIT | `#E05C5C` | Iron contamination >20 ppm, organic breakdown | Dummy plate; identify Fe source |
| R2C1 | PITTING | `#E05C5C` | Low wetting agent, dissolved gases | Add wetting agent; reduce air exposure |
| R2C2 | WHITE HAZE | `#E8A020` | Stannic oxide on surface during slow rinse | Fast rinse after plating; check Sn4+ |
| R2C3 | TIN WHISKERS | `#E05C5C` | Pure tin on copper without barrier | Ni underplate; reflow; or alloy with Bi |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Hull Cell + Contamination

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Hull Cell Strip (X: 0.5", W: 11.0"):**

Section label: `THE HULL CELL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.
Test conditions: `267 mL | 1--2 A | 5--10 min | 70 F` JetBrains Mono 12 pt at 60%.

Panel strip: 5 segments, X: 0.5", Y: 27.5", W: 11.0", H: 1.5".

| Segment | Fill | Label | Diagnosis |
|---|---|---|---|
| HCD edge | `#E8A020` at 40% | `HCD` | `Burned/rough = CD too high or acid too low` |
| Upper mid | `#27AE60` at 50% | | `Smooth = good` |
| Center | `#27AE60` at 70% | `OPTIMAL` | `Bright/matte per additive level` |
| Lower mid | `#27AE60` at 40% | | `Semi-bright = acceptable` |
| LCD edge | `#3A4055` at 60% | `LCD` | `Dull = low Sn2+ or low brightener` |

Good panel note: `Good acid tin panel: uniform matte-to-bright across 50--70% width. LCD dullness acceptable.` Inter Medium 13 pt `#27AE60`.

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

Section label: `CONTAMINATION THRESHOLDS` Barlow Condensed ExtraBold 22 pt.

| Contaminant | Threshold | Effect |
|---|---|---|
| Iron | > 20 ppm | Dark deposit, catalyzes Sn2+ oxidation |
| Copper | > 5 ppm | Immersion deposit, dark spots |
| Lead | > 2 ppm | Dark LCD, stress |
| Chloride | > 10 ppm (sulfate bath) | Pitting, anode attack |
| Organic (oil) | visible | Pitting, dull deposit |
| Sn4+ (stannic) | > 10% of total Sn | Sludge, rough deposit |

Threshold values in `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Tin Plating -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; typical acid tin bath parameters for sulfate and MSA systems.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Tin Plating Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-11 cluster. The "NO AIR AGITATION" warning must be visually prominent -- it is the single most violated rule in acid tin plating and the primary cause of Sn4+ buildup. The Sn2+/Sn4+ gauge replaces the ratio gauge used in zinc posters and serves the same purpose: one visual that captures the critical control parameter. Tin whiskers appear in the defect grid as a cross-reference to the post-treatment poster (#118) where mitigation is covered in depth.

---

*Alaina -- Plating Posters Inc*
*Poster #116 -- Construction Workup v1.0*
*2026-04-26*
