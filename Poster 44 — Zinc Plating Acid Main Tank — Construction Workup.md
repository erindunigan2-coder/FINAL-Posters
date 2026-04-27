---
Project: Plating Posters Inc
Poster Number: 44
Title: "Zinc Plating (Acid) -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid chloride zinc electroplating main tank -- potassium chloride type (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - AcidChloride
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP02
---

# Poster #44 -- Construction Workup
## Zinc Plating (Acid) -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The heart of the acid chloride zinc process. This poster is the most content-dense in the EP-02 cluster -- comparable to Poster #36 (Alkaline Main Tank) and Poster #23 (Watts Nickel). It covers bath composition (KCl type as the modern standard, NH4Cl type as legacy reference), operating parameters, anode setup with SHG zinc, the pH control system (the #1 parameter), brightener management, and a Hull cell diagnostic strip.

Hero visual: plating tank cross-section showing zinc anodes in titanium baskets, cathode (workpiece), current flow lines, and zinc ion migration.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Large tank with zinc anode baskets on both sides, cathode in center, current flow lines, rectifier symbol. Similar construction to Poster #36 but with zinc balls in baskets instead of steel anodes.
2. **Bath composition panel (Block D):** Four-component breakdown (ZnCl2, KCl, boric acid, brightener) -- one more pillar than the alkaline version.
3. **pH control gauge (Block E):** Visual representation of the critical pH range (4.8--5.8).
4. **Hull cell strip (Block G):** Acid zinc patterns are different from alkaline -- brighter across a wider range but more sensitive to contamination at LCD.
5. **Defect grid (Block F):** 6 common problems.
6. **KCl vs NH4Cl callout:** Comparison of the two acid zinc sub-types.

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
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- HULL CELL STRIP + CONTAMINATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ZINC PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Acid Chloride -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `95--98% cathode efficiency. Bright as-plated. pH is everything -- lose it and the bath tells you immediately.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated steel surface  -->  After: Bright zinc deposit ready for passivation`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE ACID CHLORIDE ZINC PLATING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5", fill `#252B3D`, border 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical "basket" shapes (rounded rects), X: 2.5", Y: 6.0", W: 1.5", H: 5.5", fill `#C8D0D8` at 60%, border 2 pt `#C8D0D8`
- Small circles inside baskets representing zinc balls (4--5 per basket, fill `#C8D0D8`)
- Right anodes: same, X: 19.5"
- Label beneath each: `SHG ZINC BALLS IN Ti BASKETS` JetBrains Mono 11 pt `#C8D0D8`
- Sub-label: `99.99% purity | 1-2 um PP anode bags` Inter Regular 11 pt `#F0EDE8` at 60%

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small arrow labels: `Zn2+ depositing` Inter Regular 11 pt `#27AE60`

**Current flow lines:**
- Curved arrows from anodes to cathode (6--8 lines), stroke 2 pt `#E8A020` dashed
- Label: `Current flow (Zn2+ migration)` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` labels to anode wires; `(-)` label to cathode wire

**Bath parameter labels (inside tank):**

Right side (X: 15.0", Y: 7.0"):
- `Zn: 25--35 g/L (3.3--4.7 oz/gal)` JetBrains Mono 14 pt `#27AE60`
- `KCl: 180--200 g/L (24--27 oz/gal)` JetBrains Mono 14 pt `#2EC4B6`
- `H3BO3: 25--30 g/L (3.3--4.0 oz/gal)` JetBrains Mono 14 pt `#E8A020`
- `Temp: 70--85 F (21--29 C)` JetBrains Mono 14 pt `#F0EDE8`

Left side (X: 4.0", Y: 7.0"):
- `pH: 5.0--5.4` JetBrains Mono 16 pt `#E8A020`
- `Cathode efficiency: 95--98%` JetBrains Mono 13 pt `#27AE60`
- `CD (rack): 20--40 ASF` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `CD (barrel): 5--12 ASF` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `A:C ratio: 1:1 to 2:1` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Potassium chloride type: the modern standard. No ammonia wastewater issues. NH4Cl type is legacy -- brighter but creates ammonia compliance problems.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Bath Composition + pH Control

**Section label:** `BATH CHEMISTRY -- THE FOUR ESSENTIALS` -- Y: 14.7".

**BLOCK D -- Four-Component Breakdown (Y: 15.3" to 18.3")**

Four side-by-side callout boxes:

| Component | X | W | Accent | Title |
|---|---|---|---|---|
| Zinc Chloride | 0.5" | 5.5" | `#27AE60` | ZINC METAL |
| Potassium Chloride | 6.25" | 5.5" | `#2EC4B6` | CONDUCTIVITY |
| Boric Acid | 12.0" | 5.5" | `#E8A020` | pH BUFFER |
| Brightener | 17.75" | 5.75" | `#C8D0D8` | BRIGHTENER |

Each box: Rounded rect H: 2.8", fill `#1E2435`, left accent 0.06".

*Zinc Chloride box:*
- `25--35 g/L (3.3--4.7 oz/gal)` JetBrains Mono 15 pt `#27AE60`
- `Source: ZnCl2 dissolved in chloride solution`
- `Role: provides Zn2+ ions for deposition`
- `Low Zn: dull deposit, poor LCD coverage`
- `High Zn: burning at HCD, rough deposit`

*Potassium Chloride box:*
- `180--200 g/L (24--27 oz/gal)` JetBrains Mono 15 pt `#2EC4B6`
- `Source: KCl (replaces NH4Cl in modern baths)`
- `Role: conductivity, anode dissolution`
- `Low KCl: poor conductivity, high voltage`
- `High KCl: minimal negative effect`

*Boric Acid box:*
- `25--30 g/L (3.3--4.0 oz/gal)` JetBrains Mono 15 pt `#E8A020`
- `Source: H3BO3 (granular, dissolved hot)`
- `Role: buffers cathode film pH`
- `Low H3BO3: pH excursion at cathode, dark LCD`
- `Precipitated H3BO3: rough/gritty deposit`

*Brightener box:*
- `Per supplier TDS` JetBrains Mono 15 pt `#C8D0D8`
- `3-component system: carrier + brightener + wetter`
- `Carrier: grain refinement, semi-bright base`
- `Brightener: reflectivity, leveling`
- `Wetter: pit prevention, surface tension`

**BLOCK E -- pH Control Gauge (Y: 18.6" to 20.3")**

- Rounded rect, full width, H: 1.5", fill `#1E2435`
- Title left: `THE CRITICAL PARAMETER: pH` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `pH Controls Everything in Acid Zinc` JetBrains Mono 14 pt `#E8A020`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Red zone left: `< 4.8` fill `#E05C5C` at 40%
- Green zone center: `4.8 -- 5.8` fill `#27AE60` at 40%
- Narrow optimal: `5.0 -- 5.4` fill `#27AE60` at 70% (brighter band within green)
- Red zone right: `> 5.8` fill `#E05C5C` at 40%
- Optimal marker: triangle at `5.2` -- `#27AE60`

Labels beneath gauge:
- `< 4.8: boric acid precipitation, dark LCD, rough` `#E05C5C` 12 pt
- `5.0 -- 5.4: OPTIMAL` `#27AE60` 14 pt (bold)
- `> 5.8: zinc hydroxide haze, reduced brightness` `#E05C5C` 12 pt

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DULL/HAZY DEPOSIT | `#2EC4B6` | Low brightener, high iron, organic contamination | Hull cell; H2O2 for iron; carbon treat |
| R1C2 | BURNING AT HCD | `#E8A020` | CD too high, low zinc, high temperature (> 95 F) | Reduce CD; add ZnCl2; cool bath |
| R1C3 | PITTING | `#E05C5C` | Low wetting agent, oil drag-in, poor agitation | Add wetter; carbon treat; increase air |
| R2C1 | DARK LCD AREAS | `#E05C5C` | Iron > 50 ppm, high pH, low primary brightener | H2O2 + filter; adjust pH; Hull cell |
| R2C2 | ROUGH/GRITTY | `#E8A020` | Boric acid precipitation, anode sludge, particulate | Filter; check boric acid solubility; inspect anode bags |
| R2C3 | WHITE HAZE POST-PLATE | `#2EC4B6` | Poor rinsing before passivate, zinc hydroxide on surface | Improve post-plate rinse; check passivate pH |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 6 -- Hull Cell + Contamination

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Hull Cell Strip (X: 0.5", W: 11.0"):**

Section label: `THE HULL CELL` Barlow Condensed ExtraBold 22 pt.
Test conditions: `267 mL | 2 A | 10 min | 75 F` JetBrains Mono 12 pt at 60%.

Panel strip: 5 segments, Y: 27.5", W: 11.0", H: 1.5".

| Segment | Fill | Label | Diagnosis |
|---|---|---|---|
| HCD edge | `#E8A020` at 40% | `HCD` | `Burned = low zinc or high temp` |
| Upper mid | `#27AE60` at 50% | | `Bright = good` |
| Center | `#27AE60` at 70% | `OPTIMAL` | `Bright + level = balanced brightener` |
| Lower mid | `#27AE60` at 40% | | `Semi-bright = acceptable` |
| LCD edge | `#3A4055` at 60% | `LCD` | `Dull/dark = iron contamination or low brightener` |

Good panel note: `Good acid zinc panel: bright across 70--80% of width. LCD dullness beyond 5 ASF equivalent is normal but narrowing bright range = brightener imbalance.` Inter Medium 13 pt `#27AE60`.

KCl vs NH4Cl note:
- `NH4Cl baths produce brighter panels at LCD but create ammonia in wastewater (POTW limit typically < 10 mg/L).` Inter Regular 12 pt `#F0EDE8` at 60%

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

Section label: `CONTAMINATION THRESHOLDS` Barlow Condensed ExtraBold 22 pt.

| Contaminant | Threshold | Effect |
|---|---|---|
| Iron | > 50 ppm | Dull, dark deposit (especially LCD) |
| Copper | > 5 ppm | Dark LCD, black spots, immersion deposit |
| Lead | > 2 ppm | Dark LCD, brittle deposit |
| Chromium | > 1 ppm | Dull, poor coverage at all CDs |
| Organic (oil) | Visible | Pitting, haze, poor ductility |
| Carbonate | N/A (acid bath) | Not a concern -- acid pH dissolves carbonates |

Threshold values in `#E05C5C`.

Iron treatment note: `Iron removal: add 0.5--1 mL/L H2O2 (30%), raise pH to 5.5 briefly, filter Fe(OH)3 precipitate, readjust pH.` Inter Regular 11 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Zinc Plating (Acid) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; Metal Finishing Guidebook; typical KCl-type acid chloride zinc bath parameters.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.

| Dark | Light |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

**Export:** Six files -- `Zinc Plating Acid Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-02 cluster. The pH gauge is the most important single visual -- equivalent to the NaOH:Zn ratio gauge on Poster #36 (Alkaline). The four-component breakdown (vs. three for alkaline) reflects the more complex chemistry of acid zinc: ZnCl2 + KCl + boric acid + brightener system.

The carbonate row in the contamination table deliberately shows "N/A" -- in alkaline zinc, carbonate buildup is a major problem requiring freeze-out treatment. In acid zinc, the acidic pH keeps carbonates dissolved. This contrast is worth calling out for operators familiar with alkaline zinc who are transitioning to acid.

The KCl vs. NH4Cl note is placed at the Hull cell section because the visual difference between the two bath types is most apparent on Hull cell panels.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #44 -- Construction Workup v1.0*
*2026-04-26*
