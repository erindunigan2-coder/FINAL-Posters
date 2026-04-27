---
Project: Plating Posters Inc
Poster Number: 148
Title: "Tin-Lead Plating -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Tin-lead (solder) electroplating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinLeadPlating
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP15
---

# Poster #148 -- Construction Workup
## Tin-Lead Plating -- Main Tank

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the process -- the main plating tank where the tin-lead solder alloy is co-deposited onto the substrate. This poster is the densest in the EP-15 cluster. It covers both MSA bath compositions (60Sn/40Pb and 90Sn/10Pb), operating parameters, anode configuration, the critical alloy composition control challenge, and a defect diagnosis grid. The single most important message: alloy ratio is everything. If the Sn:Pb ratio drifts, solderability fails and the deposit does not meet specification.

Hero visual: a plating tank cross-section showing tin-lead alloy anodes (or separate Sn and Pb anodes), cathode (workpiece), current flow lines, and solder alloy deposition.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Large tank with tin-lead alloy anodes on both sides, cathode in center, current flow, and prominent alloy composition callout.
2. **Bath composition panels (Block D):** Side-by-side 60/40 and 90/10 alloy bath chemistry.
3. **Alloy composition control gauge (Block E):** Visual showing the target Sn:Pb ratio and what shifts it.
4. **Defect grid (Block F):** 6 common tin-lead plating defects.
5. **Contamination thresholds (Block G).**

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
ZONE 4 -- BATH COMPOSITION + ALLOY CONTROL (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- CONTAMINATION THRESHOLDS + XRF (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TIN-LEAD PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Solder Plate -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where solder meets substrate. Control the alloy ratio or the specification controls you. 60/40 or 90/10 -- hit your target or strip and start over.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated surface  -->  After: Solder-coated substrate ready for post-treatment`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE TIN-LEAD PLATING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right anodes: same, X: 20.5"
- Label beneath each: `Sn-Pb ALLOY ANODES` JetBrains Mono 12 pt `#C8D0D8`
- Sub-label: `60/40 or 90/10 matching deposit composition` Inter Regular 11 pt `#F0EDE8` at 60%
- Alternative label: `Or: separate Sn + Pb anodes in Ti baskets` Inter Regular 10 pt `#F0EDE8` at 50%

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small annotation: `Sn2+ and Pb2+ co-depositing as solder alloy` Inter Regular 11 pt `#27AE60`

**Current flow lines:**
- Curved arrows from anodes to cathode (6--8 lines)
- Stroke: 2 pt `#E8A020`, dashed
- Label: `Current flow (Sn2+ and Pb2+ migration)` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` to anodes, `(-)` to cathode

**Alloy composition callout (prominent, inside tank):**
- Rounded rect, X: 7.0", Y: 10.0", W: 10.0", H: 1.2", fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Text: `ALLOY RATIO IS THE #1 CONTROL PARAMETER` Barlow SemiBold 14 pt `#E8A020`
- Sub-text: `Verify Sn:Pb by XRF -- non-destructive, fast, on every lot` Inter Regular 12 pt `#E8A020`

**Bath parameter labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `Sn2+: 35--55 g/L (60/40) / 50--70 g/L (90/10)` JetBrains Mono 13 pt `#27AE60`
- `Pb2+: 15--25 g/L (60/40) / 5--10 g/L (90/10)` JetBrains Mono 13 pt `#E05C5C`
- `Free MSA: 100--200 g/L` JetBrains Mono 13 pt `#2EC4B6`
- `Temp: 60--100 F (16--38 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Voltage: 1--6 V` JetBrains Mono 13 pt `#F0EDE8`
- `CD: 10--40 ASF rack / 5--15 ASF barrel` JetBrains Mono 13 pt `#E8A020`

Left side (X: 4.0", Y: 7.0"):
- `Cathode eff: 90--98%` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `A:C ratio: 1:1 to 2:1` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Anode bags: Required (polypropylene)` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Filtration: Continuous, 5--10 micron` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Agitation: Air (oil-free) or mechanical` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Higher CD slightly favors tin deposition. Temperature has minimal effect on alloy ratio. Brightener concentration can shift the ratio -- monitor carefully.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Bath Composition + Alloy Control

**Section label:** `BATH CHEMISTRY -- TWO STANDARD ALLOYS` -- Y: 14.7".

**BLOCK D -- Side-by-Side Bath Composition (Y: 15.3" to 18.5")**

Two callout boxes:

**Left -- 60Sn/40Pb Bath:**
- Rounded rect, X: 0.5", W: 11.0", H: 3.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `60/40 SOLDER (EUTECTIC)` Barlow SemiBold 18 pt `#2EC4B6`

| Component | Range | Optimal |
|---|---|---|
| Stannous methanesulfonate (Sn2+) | 35--55 g/L | 40--50 g/L |
| Lead methanesulfonate (Pb2+) | 15--25 g/L | 18--22 g/L |
| Free MSA | 100--200 g/L | 130--170 g/L |
| Antioxidant (hydroquinone) | 1--2 g/L | 1.5 g/L |
| Grain refiner / brightener | Per supplier | Per supplier |
| Wetting agent | Per supplier | Per supplier |

**Right -- 90Sn/10Pb Bath:**
- Rounded rect, X: 12.0", W: 11.5", H: 3.0", fill `#1E2435`, left accent `#27AE60`
- Title: `90/10 SOLDER (HIGH-TIN)` Barlow SemiBold 18 pt `#27AE60`

| Component | Range | Optimal |
|---|---|---|
| Stannous methanesulfonate (Sn2+) | 50--70 g/L | 55--65 g/L |
| Lead methanesulfonate (Pb2+) | 5--10 g/L | 6--8 g/L |
| Free MSA | 100--200 g/L | 130--170 g/L |
| Antioxidant (hydroquinone) | 1--2 g/L | 1.5 g/L |
| Grain refiner / brightener | Per supplier | Per supplier |
| Wetting agent | Per supplier | Per supplier |

**BLOCK E -- Alloy Composition Control Panel (Y: 18.8" to 20.3")**

- Rounded rect, full width, H: 1.3", fill `#1E2435`
- Title left: `ALLOY RATIO CONTROL` Barlow Condensed ExtraBold 18 pt `#F0EDE8`
- Subtitle: `What Shifts the Sn:Pb Ratio in the Deposit` JetBrains Mono 14 pt `#F0EDE8`

Horizontal bar gauge (X: 6.0", W: 17.0", H: 0.5"):
- Left zone: `MORE TIN in deposit` fill `#27AE60` at 40%
- Center zone (target): `ON SPEC` fill `#2EC4B6` at 50%
- Right zone: `MORE LEAD in deposit` fill `#E05C5C` at 40%

Labels beneath gauge:
- `Higher CD, higher Sn2+ conc, certain brighteners -> more Sn` `#27AE60` 12 pt
- `Lower CD, higher Pb2+ conc -> more Pb` `#E05C5C` 12 pt

Bottom note: `Verify alloy composition by XRF on every lot. Non-destructive. Takes 30 seconds. No excuses.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

Y: 21.3" to 26.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | WRONG ALLOY COMPOSITION | `#E05C5C` | Sn:Pb ratio out of balance in solution | Analyze bath, adjust metal concentrations |
| R1C2 | ROUGH / GRITTY | `#E8A020` | Stannic acid (Sn4+), particulates, anode sludge | Add antioxidant, filter, carbon treat |
| R1C3 | DULL DEPOSIT | `#2EC4B6` | Low brightener, low temperature | Add brightener, raise temp slightly |
| R2C1 | PITTING | `#E05C5C` | Low wetting agent, particles, dissolved gases | Add wetting agent, improve filtration |
| R2C2 | POOR SOLDERABILITY | `#E05C5C` | Oxide film, contamination, wrong alloy ratio | Reflow, improve rinsing, check alloy |
| R2C3 | TIN PEST (ALPHA TIN) | `#E8A020` | Storage below 56 F (13 C) -- gray tin conversion | Maintain storage temp; alloy >3% Pb prevents tin pest |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Contamination Thresholds + XRF

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Contamination Thresholds (X: 0.5", W: 11.0"):**

Section label: `CONTAMINATION THRESHOLDS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

| Contaminant | Threshold | Effect |
|---|---|---|
| Copper | > 5 ppm | Immersion deposit, dark spots, alloy shift |
| Iron | > 20 ppm | Dark deposit, catalyzes Sn2+ oxidation |
| Chloride | > 10 ppm | Pitting, anode attack (sulfate/MSA baths) |
| Organic (oil) | Visible | Pitting, dull deposit |
| Sn4+ (stannic) | > 10% of total Sn | Sludge, rough deposit |

Threshold values in `#E05C5C`.

**Right -- XRF Alloy Verification (X: 12.0", W: 11.5"):**

Section label: `ALLOY VERIFICATION BY XRF` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- `X-Ray Fluorescence (XRF) -- the standard method`
- `Non-destructive: no sample preparation`
- `Measures Sn and Pb content in deposit directly`
- `Accuracy: +/- 1--2% on well-calibrated instruments`
- `Frequency: every lot, every rack, every reel`
- `Alternative: dissolve in acid + AA/ICP (destructive)`
- `Specification: ASTM B579 -- electrodeposited tin-lead alloy`
- `Military: SAE AS5272 (aerospace), MIL-P-81728 (superseded)`

Bottom note: `If you are not running XRF on every lot, you are shipping unverified alloy. Stop guessing.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 7 -- Footer

Standard. Title: `Tin-Lead Plating -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; typical MSA-based tin-lead bath parameters for 60/40 and 90/10 alloys. Lead is a restricted substance under EU RoHS and a regulated occupational hazard under OSHA.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Tin-Lead Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-15 cluster. The alloy ratio callout inside the tank replaces the "NO AIR" warning from the tin cluster -- because alloy composition control is the defining challenge of tin-lead plating, just as Sn4+ control is for pure tin. Air agitation is actually permitted in tin-lead (unlike pure tin), which is worth noting in the tank parameters. The XRF section in Zone 6 is unique to this cluster -- alloy verification is not optional for solder plate, and XRF is the industry-standard method. Tin pest in the defect grid is an unusual defect specific to high-tin alloys stored below 56 F -- a piece of metallurgical trivia that could save someone a lot of grief.

---

*Alaina -- Plating Posters Inc*
*Poster #148 -- Construction Workup v1.0*
*2026-04-26*
