---
Project: Plating Posters Inc
Poster Number: 416
Title: "Deposition -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Sections 2.7)"
Technical Source: CVD deposition stage -- how the coating grows layer by layer via gas-phase chemical reaction at the heated substrate surface. Mass-transport vs. reaction-rate limited regimes, grain structure, in-situ quality indicators, and thickness monitoring. This is where the chemistry happens.
Process Scope: CVD deposition / coating growth (Stage 8 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Deposition
  - CoatingGrowth
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #416 -- Construction Workup
## Deposition -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 10. The gas recipe is flowing, the furnace is at temperature, and the coating is growing. This poster explains what is actually happening at the substrate surface during CVD deposition -- the two growth regimes (mass-transport limited vs. reaction-rate limited), why MT-CVD operates in the reaction-rate regime and what that means for temperature control, how grain structure develops, and the in-situ indicators that tell operators things are going right (or wrong).

Hero visual: cross-section diagram of the CVD boundary layer showing precursor transport and surface reaction.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Boundary layer / growth mechanism diagram (Block B -- HERO):** Cross-section showing gas flow over heated substrate, boundary layer, precursor diffusion, surface reaction, and byproduct desorption.
2. **Growth regime comparison (Block C):** Side-by-side panel contrasting mass-transport limited vs. reaction-rate limited regimes.
3. **Grain structure panel (Block D):** CVD columnar grain growth and texture control.
4. **Thickness monitoring methods (Block E):** Table of monitoring approaches.
5. **In-situ quality indicators (Block F):** What operators watch during a run.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber -- deposition)
ZONE 3 -- BOUNDARY LAYER / GROWTH MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- GROWTH REGIME COMPARISON + GRAIN STRUCTURE (14.5"--21.5" / ~7.0")
ZONE 5 -- THICKNESS MONITORING + IN-SITU INDICATORS (21.5"--27.0" / ~5.5")
ZONE 6 -- DEPOSITION TIMES + COMMON PROBLEMS (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEPOSITION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 8 of 10 -- Gas-Phase Chemistry Builds the Coating` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Precursor molecules arrive at the hot surface, react, and leave behind a solid coating. The byproducts fly away. The chemistry is elegant -- the engineering is demanding.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Gas recipe flowing, temperature stable (Stage 7) --> After: Coating deposited to target thickness, ready for cooldown`

---

### ZONE 3 -- Boundary Layer / Growth Mechanism Hero

**Section label:** `HOW CVD COATING GROWS -- BOUNDARY LAYER CHEMISTRY` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Boundary Layer Diagram (Y: 5.0" to 14.3")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Cross-section schematic (left to right, Y: 5.5" to 12.5"):**

Bottom layer -- SUBSTRATE:
- Rectangle, full width of panel, H: 1.5", fill `#3A4055`, Y: 11.0"
- Label: `HEATED SUBSTRATE (WC-Co INSERT)` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- Temperature label: `900--1050 C` -- JetBrains Mono, 14 pt, `#E8A020`

Layer above substrate -- SURFACE REACTION ZONE:
- Thin rectangle, H: 0.3", fill `#E8A020` at 30%, Y: 10.7"
- Label: `SURFACE REACTIONS` -- JetBrains Mono, 12 pt, `#E8A020`
- Detail labels (right side, stacked):
```
Precursors adsorb on hot surface
Chemical reaction forms solid coating + volatile byproducts
Byproducts desorb and diffuse away
```

Layer above -- BOUNDARY LAYER:
- Gradient rectangle, H: 2.5", fill gradient from `#252B3D` to `#1E2435`, Y: 8.0"
- Label: `BOUNDARY LAYER` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Arrows pointing downward labeled `Precursor diffusion` (Inter Regular 12 pt `#F0EDE8`)
- Arrows pointing upward labeled `Byproduct diffusion` (Inter Regular 12 pt `#F0EDE8` at 60%)

Top -- BULK GAS FLOW:
- Rectangle, H: 2.0", fill `#1E2435`, Y: 5.5"
- Horizontal arrow: `GAS FLOW (H2 carrier + TiCl4, CH4, N2, etc.)` -- Barlow SemiBold, 14 pt, `#F0EDE8`
- Flow direction arrow: 3 pt `#C8D0D8`, left to right

**Step labels on the right side (X: 16.0" to 23.0", vertical stack):**

Five numbered steps in rounded rect cards, each W: 6.5", H: 1.0", fill `#252B3D`:

1. `TRANSPORT` -- `Precursor gases carried to substrate by bulk flow` -- `#2EC4B6`
2. `DIFFUSION` -- `Precursors diffuse through boundary layer to surface` -- `#2EC4B6`
3. `ADSORPTION` -- `Precursor molecules stick to hot surface` -- `#E8A020`
4. `REACTION` -- `Chemical bonds break and reform: TiCl4 + CH4 -> TiC + 4HCl` -- `#E8A020`
5. `DESORPTION` -- `Byproducts (HCl) leave surface, diffuse out through boundary layer` -- `#27AE60`

Step number: JetBrains Mono Bold 16 pt. Title: Barlow SemiBold 13 pt. Description: Inter Regular 11 pt `#F0EDE8`.

**Bottom insight callout (Y: 13.5" to 14.1"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `The boundary layer is the bottleneck. At high temperature, the surface reaction is fast and the coating grows as fast as precursors can diffuse through the boundary layer (mass-transport limited). At lower temperature, the surface reaction is the bottleneck (reaction-rate limited).` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Growth Regime Comparison + Grain Structure

**Two-column layout (Y: 14.5" to 21.3"):**

**Left -- Growth Regime Comparison (X: 0.5", W: 11.5")**

**Section label:** `TWO GROWTH REGIMES` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK C -- Two panels side by side (Y: 15.3" to 21.0"):**

Panel 1 -- Mass-Transport Limited (X: 0.5", W: 5.5"):
- Rounded rect, H: 5.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `MASS-TRANSPORT LIMITED` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
Operates at HIGH temperature
(typically HT-CVD: 1000-1050 C)

Surface reaction is FAST
Diffusion through boundary layer
is the rate-limiting step

ADVANTAGE:
Weak temperature dependence
= uniform coating even with
small temperature variations

Used for: TiC, TiN (HT), Al2O3
```

Panel 2 -- Reaction-Rate Limited (X: 6.25", W: 5.5"):
- Rounded rect, H: 5.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `REACTION-RATE LIMITED` Barlow SemiBold 16 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
Operates at LOWER temperature
(MT-CVD TiCN: 700-900 C)

Surface reaction is SLOW
Chemical kinetics is the
rate-limiting step

CAUTION:
STRONG temperature dependence
(Arrhenius behavior)
+/- 5 C can shift rate by 10-15%
Temperature uniformity is CRITICAL

Used for: MT-CVD TiCN
```

**Right -- Grain Structure (X: 12.5", W: 11.0")**

**Section label:** `GRAIN STRUCTURE` -- Y: 14.7".

**BLOCK D -- Grain Structure Panel (Y: 15.3" to 21.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
CVD coatings are typically COLUMNAR:
grains grow vertically from substrate
surface in columns 0.5--5 um wide.

GRAIN SIZE depends on:
- Temperature (higher = larger grains)
- Deposition rate (faster = finer grains)
- Nucleation density (more nuclei = finer)

Al2O3 TEXTURE CONTROL:
- Alpha-Al2O3: corundum structure;
  thermally stable to 1000+ C; harder;
  preferred for high-speed cutting
- Kappa-Al2O3: metastable; converts to
  alpha above 1000 C with volume change;
  used for interrupted cutting

Phase controlled by nucleation step:
precise oxidation pulse technique
determines alpha vs. kappa growth.
```

Key stat callout at bottom of panel:
- Rounded rect, H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `MT-CVD TiCN: finer grain, more uniform, less substrate damage. This is why MT-CVD replaced HT-CVD TiC as the thick inner layer on modern inserts.` Barlow SemiBold 12 pt `#27AE60`

---

### ZONE 5 -- Thickness Monitoring + In-Situ Indicators

**Two-column layout (Y: 21.5" to 26.8"):**

**Left -- Thickness Monitoring (X: 0.5", W: 11.0")**

**Section label:** `THICKNESS MONITORING` -- Y: 21.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK E -- Monitoring Table (Y: 22.3" to 26.5"):**

| Method | Principle | In-Situ? | Accuracy |
|---|---|---|---|
| Time-based | Calibrated rate x time | Yes (by calc) | +/- 10-20% |
| Weight gain | Weigh before/after | No | +/- 5% average |
| Witness coupons | Flat test piece in batch; measure post-run by calotest or cross-section | No | +/- 2-5% |
| Ellipsometry | Optical; transparent films only | Yes (semiconductor) | +/- 1 nm |
| Reflectometry | Interference fringes | Yes (semiconductor) | +/- 1-5 nm |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows.

Bottom note: `Industrial CVD for cutting tools relies primarily on time-based calculation backed by post-run witness coupon measurement. In-situ monitoring is standard only in semiconductor CVD.` Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- In-Situ Quality Indicators (X: 12.0", W: 11.5")**

**Section label:** `WHAT TO WATCH DURING THE RUN` -- Y: 21.7".

**BLOCK F -- Quality Indicator Cards (Y: 22.3" to 26.5"):**

Four stacked cards, each W: 11.0", H: 0.9", fill `#252B3D`:

Card 1 -- `TEMPERATURE UNIFORMITY`:
- Left accent `#E8A020`
- `All heating zones within +/- 5 C of setpoint. Any zone drift during MT-CVD TiCN = thickness variation.`

Card 2 -- `PRESSURE STABILITY`:
- Left accent `#2EC4B6`
- `Working pressure (50-200 mbar) should be stable. Drift indicates gas leak, MFC malfunction, or exhaust blockage.`

Card 3 -- `GAS FLOW RATES`:
- Left accent `#27AE60`
- `MFC readings should hold at setpoints. TiCl4 bubbler temperature stable to +/- 1 C. AlCl3 sublimator at setpoint.`

Card 4 -- `EXHAUST COLOR/CONDITION`:
- Left accent `#E05C5C`
- `White fume in exhaust = normal (HCl + moisture). Excessive fume = possible gas leak. Dark/sooty exhaust = excess hydrocarbon (carbon problem).`

---

### ZONE 6 -- Deposition Times + Common Problems

**Section label:** `TYPICAL DEPOSITION TIMES & PROBLEMS` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Left -- Deposition Times (X: 0.5", W: 11.0", Y: 27.8" to 30.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

| Layer | Rate | Typical Time |
|---|---|---|
| TiN (0.5-3 um) | 0.5-2 um/hr | 1-3 hr |
| MT-CVD TiCN (8-12 um) | 2-5 um/hr | 2-4 hr |
| Al2O3 (4-8 um) | 0.5-1.5 um/hr | 4-8 hr |
| TiC (3-10 um) | 1-3 um/hr | 2-5 hr |
| H2 purge between layers | -- | 20-30 min each |
| Full multilayer cycle | -- | 12-24 hr total |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Four Problem Cards (X: 12.0", Y: 27.8" to 32.3"):**

Each card: Rounded rect W: 5.5", H: 2.0", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 12.0" | SOOT IN COATING | CH4 or CH3CN flow too high; thermal cracking | Reduce hydrocarbon ratio; increase H2 |
| 2 | 18.0" | NON-UNIFORM THICKNESS | Temperature gradient in furnace | Check zone calibration; rearrange trays |
| 3 | 12.0" | DELAMINATION | Eta-phase at WC-Co interface | Use TiN interlayer; control cooling |
| 4 | 18.0" | WRONG Al2O3 PHASE | Nucleation pulse protocol error | Verify oxidation pulse timing |

Interior per card:
- Problem: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 12 pt `#F0EDE8`
- Fix: Inter Medium 12 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Deposition -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deposition CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The boundary layer diagram is the educational centerpiece because it explains the fundamental mechanism that separates CVD from PVD: in CVD, the coating forms by chemical reaction at the surface, not by physical transfer through vacuum. The five-step sequence (transport -> diffusion -> adsorption -> reaction -> desorption) gives operators a mental model of what is happening inside the sealed furnace they cannot see into.

The two-regime comparison (mass-transport vs. reaction-rate limited) is the key insight for anyone running CVD -- it explains why MT-CVD requires tighter temperature control than HT-CVD, which directly impacts how they set up and monitor their furnace.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #416 -- Construction Workup v1.0*
*2026-04-26*
