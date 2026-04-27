---
Project: Plating Posters Inc
Poster Number: 600
Title: "Nitriding Cycle -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5, Sections 5.1, 5.3)"
Process Scope: The active nitriding cycle -- gas ratio control, compound layer management, case depth vs. time, and the metallurgical mechanism
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - NitridingCycle
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #600 -- Construction Workup
## Nitriding Cycle -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the core process poster -- the main event. During the nitriding cycle, nitrogen ions bombard the cathode (workpiece), penetrate the surface, and form nitride precipitates that create extreme hardness without any quench. The gas ratio (N2/H2) is the master control for compound layer composition. This poster is the densest in the plasma cluster.

Hero visual: a cross-section diagram of the nitrided surface showing compound layer (white layer) and diffusion zone, with the gas ratio as a "control dial" that determines what you get.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Surface cross-section hero (Block B):** Metallographic-style diagram showing compound layer (epsilon/gamma-prime) over diffusion zone over core.
2. **Gas ratio = compound layer dial (Block D):** Visual slider/dial showing N2% vs. compound layer outcome.
3. **Case depth vs. time table (Block E).**
4. **Metallurgical mechanism callout (Block F):** The physics of ion bombardment and nitrogen diffusion.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SURFACE CROSS-SECTION HERO (2.9"--15.5")
ZONE 3 -- GAS RATIO CONTROL (15.5"--22.0")
ZONE 4 -- CASE DEPTH TABLE + MECHANISM (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NITRIDING CYCLE` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- The Core Process: Ion Bombardment and Nitrogen Diffusion` -- 30 pt `#27AE60` (Emerald).
**Tagline:** `No carbon added. No quench needed. Hardness by precipitation -- the elegant physics of nitriding.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `1100+` -- 72 pt `#27AE60`
- Label: `HV surface hardness achievable on Nitralloy steels` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Surface Cross-Section (HERO)

**Section label:** `THE NITRIDED SURFACE -- WHAT YOU'RE BUILDING` -- Y: 3.1".

**BLOCK B -- Cross-Section Diagram (Y: 3.8" to 15.3")**

Large vertical cross-section showing three distinct zones from surface to core:

**Overall frame:**
- Rounded rect, X: 2.0", Y: 4.5", W: 20.0", H: 10.0", fill `#252B3D`, border 2 pt `#C8D0D8`

**Layer 1 -- Compound Layer (White Layer) -- top:**
- Rect, X: 2.0", Y: 4.5", W: 20.0", H: 1.5"
- Fill: `#F0EDE8` at 25% (appears "white" against dark background)
- Border bottom: 2 pt dashed `#E8A020`
- Labels (left side):
  - `COMPOUND LAYER` Barlow SemiBold 18 pt `#E8A020`
  - `("White Layer")` Inter Regular 14 pt `#F0EDE8` at 60%
  - `0--25 microns (0--0.001 inch)` JetBrains Mono 13 pt `#E8A020`
- Labels (right side, inside):
  - `Gamma-prime (Fe4N) -- ductile, preferred` Inter Medium 13 pt `#27AE60`
  - `Epsilon (Fe2-3N) -- harder, more wear-resistant` Inter Medium 13 pt `#2EC4B6`
  - `Or NONE -- achievable only in plasma nitriding` Inter Medium 13 pt `#E05C5C`

**Layer 2 -- Diffusion Zone -- middle:**
- Rect, X: 2.0", Y: 6.0", W: 20.0", H: 5.0"
- Fill: gradient from `#27AE60` at 20% (top) to `#1A1F2E` at 10% (bottom) -- represents decreasing nitrogen concentration
- Border bottom: 2 pt dashed `#2EC4B6`
- Labels (left side):
  - `DIFFUSION ZONE` Barlow SemiBold 18 pt `#27AE60`
  - `0.003--0.024 inch (at 970 F)` JetBrains Mono 13 pt `#27AE60`
- Labels (right side, inside):
  - `Nitrogen in solid solution with ferrite` Inter Regular 13 pt `#F0EDE8`
  - `Fine alloy nitride precipitates (CrN, AlN, MoN, VN)` Inter Regular 13 pt `#F0EDE8`
  - `THESE PRECIPITATES = THE HARDNESS` Inter Medium 14 pt `#27AE60`
  - `No phase transformation -- steel stays ferritic` Inter Regular 13 pt `#F0EDE8` at 70%

**Layer 3 -- Core (unaffected) -- bottom:**
- Rect, X: 2.0", Y: 11.0", W: 20.0", H: 3.5"
- Fill: `#1A1F2E` (same as background -- visually "core")
- Labels:
  - `CORE (UNAFFECTED)` Barlow SemiBold 18 pt `#C8D0D8`
  - `Original Q&T microstructure preserved` Inter Regular 13 pt `#F0EDE8` at 60%
  - `Core hardness unchanged -- temper was above nitriding temp` Inter Regular 13 pt `#F0EDE8` at 60%

**Dimension callout arrows (right edge):**
- Vertical arrows with dimension labels showing relative thickness of each zone

---

### ZONE 3 -- Gas Ratio Control

**Section label:** `GAS RATIO = COMPOUND LAYER CONTROL` -- Y: 15.7".

**BLOCK D -- Gas Ratio Slider (Y: 16.3" to 21.8")**

**Horizontal bar gauge (X: 0.5", W: 23.0", H: 1.0", Y: 16.8"):**

Five zones left to right:

| N2 % | H2 % | Fill | Result |
|---|---|---|---|
| 5% N2 | 95% H2 | `#2EC4B6` at 30% | Diffusion zone ONLY -- NO compound layer |
| 15% N2 | 85% H2 | `#27AE60` at 30% | Thin gamma-prime (Fe4N) layer |
| 25% N2 | 75% H2 | `#27AE60` at 50% | STANDARD -- mixed compound layer |
| 50% N2 | 50% H2 | `#E8A020` at 40% | Thicker compound layer |
| 80% N2 | 20% H2 | `#E8A020` at 60% | Thick epsilon (Fe2-3N) layer |

Labels above gauge: N2 percentage. Labels below: result description.
Optimal marker at 25%: triangle `#27AE60`.
"NO WHITE LAYER" callout at 5% end: badge `#E05C5C` text `THIS IS UNIQUE TO PLASMA`.

**Below gauge -- Three key callout boxes (Y: 18.5" to 21.5"):**

| Callout | Title | Content | Accent |
|---|---|---|---|
| Left | GAMMA-PRIME (Fe4N) | More ductile; better fatigue resistance; preferred for most applications; lower N2 ratios favor gamma-prime | `#27AE60` |
| Center | EPSILON (Fe2-3N) | Harder; better wear resistance; higher N2 ratios and lower temperatures favor epsilon | `#2EC4B6` |
| Right | NO COMPOUND LAYER | Diffusion zone only; maximum fatigue life; no brittle surface layer; only achievable in plasma nitriding; requires very low N2 (< 10%) | `#E8A020` |

Each: Rounded rect, W: 7.33", H: 2.8", fill `#1E2435`, left accent 0.06".

---

### ZONE 4 -- Case Depth Table + Mechanism

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Case Depth vs. Time (X: 0.5", W: 11.0")**

Section label: `CASE DEPTH VS. TIME (at 970 F / 520 C)` -- Barlow Condensed ExtraBold 22 pt.

| Time | ECD | Compound Layer |
|---|---|---|
| 4 hours | 0.003--0.005 inch | 0.0001--0.0002 inch |
| 10 hours | 0.006--0.010 inch | 0.0002--0.0004 inch |
| 20 hours | 0.010--0.016 inch | 0.0003--0.0006 inch |
| 40 hours | 0.016--0.024 inch | 0.0004--0.0008 inch |

Table: Header `#3A4055`, alternating rows. JetBrains Mono 13 pt.

Below table:
- `Plasma nitriding is 20--30% faster than gas nitriding for equivalent case depth` -- Inter Medium 14 pt `#27AE60`
- `Ion bombardment enhances surface nitrogen uptake rate` -- Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- BLOCK F: Metallurgical Mechanism (X: 12.0", W: 11.5")**

Section label: `HOW IT WORKS -- THE PHYSICS` -- Barlow Condensed ExtraBold 22 pt.

Callout box, H: 9.5", fill `#1E2435`, left accent `#2EC4B6`:

Numbered steps:
1. `DC voltage ionizes N2/H2 gas mixture at low pressure (1--5 mbar)`
2. `Nitrogen ions (N+, N2+) accelerate toward negatively charged workpiece (cathode)`
3. `Ion bombardment SPUTTERS the surface -- removes oxides, passive films`
4. `This is why plasma nitriding works on stainless steel -- sputtering breaks the Cr2O3 passive film`
5. `Atomic nitrogen implants into surface and diffuses inward`
6. `Nitrogen combines with alloying elements (Cr, Al, Mo, V) to form nitride precipitates`
7. `These coherent precipitates strain the iron lattice = extreme hardness`
8. `NO PHASE TRANSFORMATION -- steel remains ferritic throughout`
9. `NO QUENCH -- hardness is from precipitation, not martensite`

Each step: Inter Regular 13 pt. Key phrases in `#2EC4B6` or `#27AE60`.

Bottom callout:
- `Dimensional change: only 0.0001--0.0005 inch per surface` JetBrains Mono 13 pt `#27AE60`
- `Parts can be finish-machined BEFORE nitriding` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Footer

Standard footer. Title: `Nitriding Cycle -- Plasma Nitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

## Design Notes

This is the most technically dense poster in the plasma cluster. The surface cross-section diagram is the hero -- it must communicate the three-zone structure (compound layer / diffusion zone / core) clearly at 6 feet. The gas ratio slider is the second most important visual -- it's the "knob" that the operator turns to get different results. The "no white layer" capability is plasma nitriding's unique selling point and should be visually prominent.

---

*Alaina -- Poster #600 -- Construction Workup v1.0 -- 2026-04-26*
