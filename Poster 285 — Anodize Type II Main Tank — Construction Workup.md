---
Project: Plating Posters Inc
Poster Number: 285
Title: "Anodize -- Type II (Main Tank)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.7)"
Technical Source: Industry-standard sulfuric acid anodizing main tank per MIL-A-8625F Type II. Covers electrolyte, temperature control, current density, alloy effects, thickness targets, and contamination thresholds.
Process Scope: Sulfuric acid anodize main tank (Stage 6 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - MainTank
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #285 -- Construction Workup
## Anodize -- Type II (Main Tank)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. This is the heart of the process -- where the anodic oxide film grows. The most content-dense poster in the Type II cluster, comparable to Poster #36 (Zinc Alkaline Main Tank) and Poster #23 (Watts Nickel). Hero concept: temperature is the single most critical parameter. +/- 1 C control is recommended. The temperature effects table is the key visual -- showing how even a few degrees changes the coating from hard and dense to soft and powdery.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Anodize tank cross-section hero (Block B):** Tank with sulfuric acid electrolyte, aluminum workpiece as anode, lead-antimony cathodes, rectifier, air agitation, and cooling system.
2. **Temperature effects table (Block D):** The hero data visualization -- temperature vs. coating quality.
3. **Alloy effects panel (Block E).**
4. **Contamination thresholds + defect grid (Block F).**
5. **Thickness by application table (Block G).**

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
  Stage 6 highlighted (Emerald)
ZONE 3 -- ANODIZE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TEMPERATURE EFFECTS + THICKNESS BY APPLICATION (14.5"--20.5" / ~6.0")
ZONE 5 -- ALLOY EFFECTS + CONTAMINATION THRESHOLDS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ANODIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Main Tank -- Stage 6 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where the oxide grows. H2SO4 electrolyte, room temperature, moderate current -- and the most critical variable is the one you can feel: temperature.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, desmutted aluminum surface  -->  After: Porous anodic oxide film (5--25 um) ready for dye and seal`

---

### ZONE 3 -- Anodize Tank Hero

**Section label:** `THE TYPE II ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (electrolyte)
- Border: 3 pt `#C8D0D8`
- Label inside tank: `H2SO4 ELECTROLYTE` Barlow SemiBold 12 pt `#E8A020` at 50%

**Cathodes (left and right sides):**
- Left: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right: same, X: 20.5"
- Label: `CATHODE (Pb-6% Sb alloy)` JetBrains Mono 12 pt `#C8D0D8`

**Anode / Workpiece (center):**
- Vertical rect, X: 10.5", Y: 6.0", W: 3.0", H: 5.5", fill `#27AE60` at 25%, border 2 pt `#27AE60`
- Label above: `ANODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Thin oxide layer on surface: thin band `#E8A020` at 40%
- Label: `Oxide growing on surface` Inter Regular 11 pt `#E8A020`

**Rectifier (above tank):**
- Rect, X: 9.5", Y: 5.0", W: 5.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER (filtered, <5% ripple)` Barlow SemiBold 12 pt `#E8A020`
- `(+)` on wire to workpiece (anode); `(-)` on wires to cathodes

**Cooling system indicator (bottom of tank):**
- Coil symbol at tank bottom
- Label: `COOLING COIL -- maintain 18--22 C` JetBrains Mono 12 pt `#2EC4B6`

**Air agitation (bottom):**
- Upward arrows from agitation bar
- Label: `Oil-free air agitation` Inter Regular 12 pt `#2EC4B6`

**Bath parameter labels (right side, inside tank):**
- `H2SO4: 150--200 g/L (20--27 oz/gal)` JetBrains Mono 14 pt `#27AE60`
- `Temp: 64--72 F (18--22 C)` JetBrains Mono 14 pt `#E8A020`
- `CD: 12--18 ASF (1.2--1.8 A/dm2)` JetBrains Mono 14 pt `#E8A020`
- `Voltage: 12--24 V (rises as coating grows)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 20--60 min` JetBrains Mono 13 pt `#F0EDE8`

**Left side labels:**
- `Dissolved Al: <15 g/L` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Cl-: <25 ppm` JetBrains Mono 13 pt `#E05C5C`
- `Sp. gravity: 1.10--1.14` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Growth rate: ~0.4--0.5 um/min (6061)` JetBrains Mono 12 pt `#F0EDE8` at 70%

**Tank material note (below tank):**
- `Tank: Polypropylene, PVDF, or PVC-lined steel. Never bare steel or stainless in contact with bath.` Inter Regular 12 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Temperature Effects + Thickness by Application

**Section label:** `TEMPERATURE -- THE #1 VARIABLE` -- Y: 14.7".

**Two-column layout:**

**Left -- Temperature Effects Table (X: 0.5", W: 11.5"):**

Title: `TEMPERATURE VS. COATING QUALITY` Barlow Condensed ExtraBold 22 pt `#E8A020`.

| Bath Temperature | Coating Result | Color Code |
|---|---|---|
| <59 F (<15 C) | Hard, dense, brittle; poor dye absorption -- Type III territory | `#2EC4B6` |
| 64--72 F (18--22 C) | OPTIMUM -- good pore structure; balanced growth/dissolution; excellent dye | `#27AE60` |
| 73--77 F (23--25 C) | Softer; increased pore size; acceptable for some applications | `#E8A020` |
| >77 F (>25 C) | POWDERING RISK -- rapid dissolution; unacceptable quality | `#E05C5C` |

Each row: left accent colored per code. Optimum row highlighted with fill `#27AE60` at 10%.
Note: `+/- 1 C control is recommended. A few degrees changes everything.` Inter Medium 13 pt `#E8A020`.

**Right -- Thickness by Application (X: 12.5", W: 11.0"):**

Title: `THICKNESS TARGETS` Barlow Condensed ExtraBold 22 pt.

| Application | Typical Thickness |
|---|---|
| Architectural (exterior) | 18--25 um (0.7--1.0 mil) per AA-M45 |
| Decorative (interior) | 8--15 um (0.3--0.6 mil) |
| MIL-A-8625F Class 1 minimum | 10 um (0.4 mil) |
| Electronics / consumer | 10--15 um (0.4--0.6 mil) |

Note: `Dimensional change: ~50% inward, ~50% outward. Net dimensional gain = ~50% of total thickness per surface.` Inter Regular 13 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Alloy Effects + Contamination Thresholds

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Alloy Effects (X: 0.5", W: 11.0"):**

Section label: `ALLOY EFFECTS IN THE ANODIZE TANK` Barlow Condensed ExtraBold 22 pt.

| Alloy | Oxide Appearance | Dye Response | Notes |
|---|---|---|---|
| 6061 / 6063 | Clear, uniform | Excellent | Gold standard for Type II |
| 5052 | Slightly grayish | Good | Mg content causes tint |
| 1100 | Clear, bright | Excellent | Soft oxide |
| 2024 | Tan/brown (Cu) | Poor for bright colors | Lower efficiency; less corrosion-resistant |
| 7075 | Yellow-bronze | Moderate | Zinc dissolves preferentially |
| Cast (high Si) | Salt and pepper | Mottled | Si does not convert to oxide |

**Right -- Contamination Thresholds (X: 12.0", W: 11.5"):**

| Contaminant | Threshold | Effect |
|---|---|---|
| Dissolved Al | >15 g/L | Gray coatings; reduced efficiency |
| Chloride (Cl-) | >25 ppm | PITTING -- most damaging |
| Copper (Cu) | >10 ppm | Mottling, discoloration |
| Iron (Fe) | >100 ppm | Brownish discoloration |
| Rectifier ripple | >5% | Soft, powdery coatings |

Threshold values: JetBrains Mono 13 pt `#E05C5C`.

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 26.7".

**3x2 Grid:**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BURNING | `#E05C5C` | Excessive CD, high temp, low acid, or high dissolved Al | Reduce CD; check temp; analyze bath |
| R1C2 | POWDERING | `#E8A020` | Temp >77 F (>25 C) or time too long | Cool bath immediately; reduce time |
| R1C3 | PITTING | `#E05C5C` | Chloride >25 ppm or substrate defects | Analyze for Cl-; check rinse water |
| R2C1 | UNEVEN THICKNESS | `#2EC4B6` | Poor racking, temp gradients, inadequate agitation | Improve agitation; check rack contacts |
| R2C2 | GRAY COATING | `#E8A020` | High dissolved Al (>15 g/L), high temp | Partial dump; cool bath |
| R2C3 | POOR DYE COLOR | `#2EC4B6` | Coating too thin or pores too small (temp too low) | Increase time; verify temp in range |

Each card: W: 7.33", H: 2.5", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Anodize -- Type II (Main Tank)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; MIL-A-8625F; ASM Handbook Vol. 5; typical parameters for conventional sulfuric acid anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize Type II Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the Type II cluster. The temperature effects table is the single most important visualization -- it explains why Type II lives in a narrow temperature band and what happens when you drift. The anodize tank diagram should show the workpiece as the ANODE (positive terminal) -- this is the fundamental difference from electroplating where the workpiece is the cathode. Lead-antimony cathodes, cooling coils, and oil-free air agitation are the key hardware elements. The alloy effects table reinforces that 6061/6063 are the gold standard and copper-bearing alloys are challenging.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #285 -- Construction Workup v1.0*
*2026-04-26*
