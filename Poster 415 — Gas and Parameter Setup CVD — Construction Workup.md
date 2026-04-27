---
Project: Plating Posters Inc
Poster Number: 415
Title: "Gas & Parameter Setup -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.6)"
Technical Source: CVD parameter setup including precursor gas compositions, flow rates, temperature and pressure setpoints for TiC, TiN, TiCN (MT-CVD), and Al2O3 layers. Multilayer recipe structure and ramp/soak profiles.
Process Scope: CVD gas and parameter setup (Stage 7 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Parameters
  - GasSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #415 -- Construction Workup
## Gas & Parameter Setup -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 10. The furnace is sealed, purged, and at temperature. Now the precursor gas recipe is loaded and verified before deposition begins. This poster covers the parameter tables for each major CVD coating layer (TiC, TiN, MT-CVD TiCN, Al2O3), the multilayer recipe structure for a modern cutting insert, and the critical concept of gas-phase chemistry that drives the whole process.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Multilayer recipe diagram (Block B -- HERO):** Horizontal timeline showing the sequential deposition of layers in a modern CVD cutting insert: TiN base -> MT-CVD TiCN -> Al2O3 -> TiN top. Each layer is a colored horizontal bar with parameters.
2. **Layer parameter table (Block C):** Detailed parameters for each coating layer.
3. **Precursor chemistry cards (Block D):** What each precursor does and why.
4. **Recipe development considerations (Block E):** Hysteresis, substrate limits, multilayer design principles.
5. **Common parameter failures (Block F):** Four failure cards.

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
  Stage 7 highlighted (Amber -- parameters)
ZONE 3 -- MULTILAYER RECIPE DIAGRAM / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- LAYER PARAMETER TABLE (14.5"--21.5" / ~7.0")
ZONE 5 -- PRECURSOR CHEMISTRY + RECIPE NOTES (21.5"--27.0" / ~5.5")
ZONE 6 -- COMMON PARAMETER FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `GAS & PARAMETER SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 7 of 10 -- Precursor Recipes, Multilayer Stacks, and Gas-Phase Chemistry` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `A modern CVD cutting insert has 4+ layers deposited sequentially over 12-24 hours. Each layer has its own gas recipe, temperature, and pressure. The recipe defines the coating -- there is no shortcut.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Furnace at temperature, atmosphere stabilized (Stage 6) --> After: Recipe loaded, gas flows verified, ready for deposition`

---

### ZONE 3 -- Multilayer Recipe Diagram (HERO)

**Section label:** `MODERN CVD MULTILAYER STACK -- LAYER BY LAYER` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Horizontal Timeline Diagram (Y: 5.0" to 14.3")**

**Concept:** A horizontal timeline running left to right showing 5 phases: H2 purge start -> Layer 1 (TiN) -> Purge -> Layer 2 (MT-CVD TiCN) -> Purge -> Layer 3 (Al2O3) -> Purge -> Layer 4 (TiN top) -> Cool-down.

**Timeline base:** Rectangle, X: 0.5", Y: 9.5", W: 23.0", H: 0.08", fill `#C8D0D8`.

**Time labels below timeline:**
- `0 hr`, `2 hr`, `5 hr`, `8 hr`, `12 hr`, `16 hr`, `20 hr`, `24 hr`
- JetBrains Mono 12 pt `#F0EDE8` at 60%

**Layer bars above timeline (stacked vertically like a coating cross-section on the right side):**

Each layer is a horizontal colored bar positioned along the timeline:

| Layer | Color | X Start | Width | Y | Height | Label |
|---|---|---|---|---|---|---|
| Heat-up | `#3A4055` | 0.5" | 2.5" | 8.5" | 0.8" | `HEAT-UP (2 hr)` |
| TiN base (0.5 um) | `#C8A020` (gold) | 3.2" | 2.0" | 7.0" | 1.3" | `TiN BASE` |
| Purge | `#3A4055` | 5.4" | 0.8" | 8.5" | 0.8" | `PURGE` |
| MT-CVD TiCN (8-12 um) | `#5A6A8A` (blue-gray) | 6.4" | 5.5" | 5.5" | 2.8" | `MT-CVD TiCN` |
| Purge | `#3A4055` | 12.1" | 0.8" | 8.5" | 0.8" | `PURGE` |
| Al2O3 (4-8 um) | `#E05C5C` at 60% | 13.1" | 5.0" | 6.2" | 2.1" | `alpha-Al2O3` |
| Purge | `#3A4055` | 18.3" | 0.8" | 8.5" | 0.8" | `PURGE` |
| TiN top (1 um) | `#C8A020` (gold) | 19.3" | 1.5" | 7.5" | 0.8" | `TiN TOP` |
| Cool-down | `#3A4055` | 21.0" | 2.5" | 8.5" | 0.8" | `COOL-DOWN (4+ hr)` |

Layer bar labels: Barlow SemiBold 14 pt, color-matched. Inside each layer bar:
- Thickness: JetBrains Mono 12 pt `#F0EDE8`
- Temperature: JetBrains Mono 11 pt `#E8A020`
- Time: JetBrains Mono 11 pt `#F0EDE8` at 60%

**Right side -- Coating cross-section (Y: 5.5" to 9.5", X: 17.0" to 23.5"):**

Vertical stack showing the final coating cross-section:
- Bottom: `WC-Co SUBSTRATE` rectangle, fill `#3A4055`, H: 1.0"
- Layer 1: `TiN` rectangle, fill `#C8A020`, H: 0.2" -- `0.5 um`
- Layer 2: `TiCN` rectangle, fill `#5A6A8A`, H: 1.5" -- `8-12 um`
- Layer 3: `Al2O3` rectangle, fill `#E05C5C` at 60%, H: 1.0" -- `4-8 um`
- Layer 4: `TiN` rectangle, fill `#C8A020`, H: 0.15" -- `1 um`

Labels to the right of each layer, JetBrains Mono 11 pt `#F0EDE8`.

Title above: `FINAL STACK` Barlow SemiBold 14 pt `#F0EDE8`
Below: `Total: 13-22 um | Cycle: 12-24 hr` JetBrains Mono 12 pt `#E8A020`

**Bottom insight callout (Y: 13.5" to 14.1"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `Each layer requires its own gas recipe. H2 purge between layers prevents cross-contamination. The TiCN layer is the thick wear-resistant core; Al2O3 provides thermal barrier and oxidation resistance.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Layer Parameter Table

**Section label:** `LAYER-BY-LAYER PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK C -- Parameter Table (Y: 15.3" to 21.3")**

| Parameter | TiN (HT) | MT-CVD TiCN | Al2O3 (alpha) | TiC (HT) |
|---|---|---|---|---|
| Temperature | 1000-1050 C | 700-900 C | 1000-1050 C | 1000-1050 C |
| Pressure | 50-200 mbar | 50-200 mbar | 50-100 mbar | 50-200 mbar |
| TiCl4 | 2-5% of total | 2-5% of total | -- | 2-5% of total |
| N2 | 20-40% | -- | -- | -- |
| CH4 | -- | -- | -- | 3-6% |
| CH3CN (acetonitrile) | -- | 0.5-2% | -- | -- |
| AlCl3 | -- | -- | 2-5% | -- |
| CO2 | -- | -- | 3-6% | -- |
| H2 (carrier) | Balance | Balance | Balance | Balance |
| Deposition rate | 0.5-2 um/hr | 2-5 um/hr | 0.5-1.5 um/hr | 1-3 um/hr |
| Typical thickness | 0.5-3 um | 8-12 um | 4-8 um | 3-10 um |
| Layer time | 1-3 hr | 2-4 hr | 4-8 hr | 2-5 hr |
| Hardness | 2000-2400 HV | 2500-3000 HV | 2000-2200 HV | 2800-3200 HV |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

Bottom callout:
- `MT-CVD TiCN at 700-900 C is the modern workhorse -- faster rate, finer grain, and less substrate damage than HT-CVD TiC or TiN.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 5 -- Precursor Chemistry + Recipe Notes

**Two-column layout (Y: 21.5" to 26.8"):**

**Left -- Precursor Chemistry (X: 0.5", W: 11.0"):**

**Section label:** `PRECURSOR CHEMISTRY` -- Y: 21.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

- Rounded rect, Y: 22.2", H: 4.4", fill `#1E2435`, left accent `#27AE60`

Chemical reactions (JetBrains Mono 13 pt `#F0EDE8`):

TiN formation:
- `TiCl4 + 1/2 N2 + 2 H2 -> TiN + 4 HCl`

TiC formation:
- `TiCl4 + CH4 -> TiC + 4 HCl`

MT-CVD TiCN:
- `TiCl4 + CH3CN + H2 -> TiCN + HCl + ...`

Al2O3 formation:
- `2 AlCl3 + 3 CO2 + 3 H2 -> Al2O3 + 3 CO + 6 HCl`

Note: `All reactions produce HCl as byproduct -- drives exhaust scrubber requirement` Inter Medium 12 pt `#E05C5C`

**Right -- Recipe Development Notes (X: 12.0", W: 11.5"):**

**Section label:** `RECIPE CONSIDERATIONS` -- Y: 21.7".

- Rounded rect, Y: 22.2", H: 4.4", fill `#1E2435`, left accent `#E8A020`

Key points (Inter Medium 13 pt `#F0EDE8`):
- `TiCl4 is a liquid (bp 136 C) -- delivery rate depends on bubbler temperature. +/- 1 C bubbler drift = measurable composition change.`
- `AlCl3 is a solid that sublimes -- requires its own heated delivery system (sublimator at 150-180 C).`
- `MT-CVD uses CH3CN (acetonitrile) as combined carbon + nitrogen source -- simpler gas system than separate CH4 + N2.`
- `Alpha-Al2O3 nucleation requires a precise oxidation pulse at the start of the Al2O3 step -- this controls crystal phase.`
- `Pre-hardened steel substrates (HSS) cannot tolerate any CVD temperature above 550 C -- use PVD instead.`

---

### ZONE 6 -- Common Parameter Failures

**Section label:** `PARAMETER FAILURES -- WHAT GOES WRONG` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Failure Cards (Y: 27.8" to 32.3")**

Each card: Rounded rect W: 5.5", H: 4.3", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WRONG Al2O3 PHASE | Nucleation pulse incorrect -- kappa instead of alpha | Verify oxidation pulse protocol; check temperature and timing |
| 2 | 6.33" | COBALT DEPLETION | TiC/TiN layer at HT (1050 C) + HCl attacks cobalt binder | Use MT-CVD TiCN for thick inner layers (700-900 C) |
| 3 | 12.16" | SOOT IN COATING | CH4 flow too high -- thermal cracking produces free carbon | Reduce CH4 ratio; verify MFC calibration; increase H2 flow |
| 4 | 18.0" | LAYER CONTAMINATION | Insufficient H2 purge between layers | Increase purge time to 20-30 min; verify gas switching valves |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Gas & Parameter Setup -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Gas Parameter Setup CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The multilayer recipe timeline is the hero because it communicates the fundamental difference between CVD and PVD recipe design: CVD deposits multiple distinct layers in sequence over a 12-24 hour cycle, each with its own gas chemistry. The coating cross-section on the right gives operators an instant visual of what they are building. The layer parameter table is the reference they will check before every run. The chemical reaction equations are included because CVD operators need to understand why HCl is produced -- it drives both the exhaust scrubber requirement and the cobalt depletion concern.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #415 -- Construction Workup v1.0*
*2026-04-26*
