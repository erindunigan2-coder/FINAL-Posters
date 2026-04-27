---
Project: Plating Posters Inc
Poster Number: 485
Title: "Parameter Setup -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 7)"
Technical Source: Complete APS parameter ranges including arc current, voltage, gas flows, powder feed rate, standoff distance, traverse speed, step increment, deposition rate, and efficiency. Values from ASM Handbook Vol 5A.
Process Scope: Atmospheric plasma spray -- spray parameter setup and optimization
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Parameters
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #485 -- Construction Workup
## Parameter Setup -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of the APS process. This is the data-dense poster -- the operating window for every controllable parameter. The hero is a comprehensive parameter table. Supporting content: a standoff distance effect visual, a "what each parameter controls" guide, and a parameter interaction map.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Master parameter table (Block B -- HERO):** 14-row table with parameter, range, and notes.
2. **Standoff distance effect (Block C):** Visual showing how standoff affects coating density.
3. **Parameter-to-property map (Block D):** Shows which parameters control which coating properties.
4. **Deposition efficiency callout (Block E):** 40-70% DE explained.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Slate)
ZONE 3 -- MASTER PARAMETER TABLE HERO (4.2"--15.5" / ~11.3")
  Block B: 14-row parameter table
ZONE 4 -- STANDOFF DISTANCE EFFECT (15.5"--22.0" / ~6.5")
  Block C: Standoff visual + density relationship
ZONE 5 -- PARAMETER-TO-PROPERTY MAP (22.0"--28.5" / ~6.5")
  Block D: Which knob controls which outcome
ZONE 6 -- DEPOSITION EFFICIENCY (28.5"--32.5" / ~4.0")
  Block E: 40-70% DE explained
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- The Operating Window -- Stage 5 of 10` -- 32 pt `#C8D0D8`. Y: 1.4".
**Tagline:** `Every parameter is a lever. Pull the right ones and the coating performs. Pull the wrong ones and you are grinding off scrap.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `14` -- 72 pt `#E8A020`
- Label: `controllable parameters define your coating` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted. Others dimmed.

---

### ZONE 3 -- Master Parameter Table (HERO)

**Section label:** `APS OPERATING PARAMETERS -- COMPLETE REFERENCE` -- Y: 4.4".

**BLOCK B -- 14-Row Parameter Table**

Y: 5.0" to 15.3". Full width. Columns: Parameter (4.5") | Typical Range (5.0") | Units (2.5") | Notes (11.0")

| Parameter | Typical Range | Units | Notes |
|---|---|---|---|
| Arc current | 400-800 | A | Higher current = higher enthalpy; heavier electrode wear |
| Arc voltage | 50-80 | V | Determined by gas composition and flow rates |
| Power | 25-60 (up to 80) | kW | Power = V x A; defines total energy input |
| Primary gas (Ar) | 35-60 | SLPM | Stabilizes arc; carries plasma |
| Secondary gas (H2) | 5-15 | SLPM | Increases enthalpy dramatically; hotter plume |
| Secondary gas (He) | 20-50 | SLPM | Alternative to H2; gentler heating |
| Secondary gas (N2) | 5-20 | SLPM | Lower cost alternative |
| Carrier gas (Ar) | 3-8 | SLPM | Delivers powder to plasma plume |
| Powder feed rate | 20-80 | g/min | Material and application dependent |
| Standoff distance | 75-150 | mm | Closer = denser; farther = more porous |
| Spray angle | 75-90 | degrees | Below 45 deg causes shadowing and porosity |
| Traverse speed | 200-1000 | mm/s | Robot-controlled for uniformity |
| Step increment | 3-6 | mm | Overlap between passes (25-50% of footprint) |
| Deposition rate | 2-10 | kg/hr | Material and parameter dependent |

Header: fill `#3A4055`, Barlow SemiBold 13 pt. Data: JetBrains Mono 12 pt `#F0EDE8`. Range values in `#E8A020` for emphasis.

Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 4 -- Standoff Distance Effect

**Section label:** `STANDOFF DISTANCE -- THE MOST SENSITIVE PARAMETER` -- Y: 15.7".

**BLOCK C -- Standoff Visual**

Y: 16.3" to 21.8". Three-panel comparison.

| Standoff | Result | Color |
|---|---|---|
| TOO CLOSE (< 75 mm) | Dense but overheated substrate; risk of delamination from thermal stress | `#E05C5C` |
| OPTIMAL (75-150 mm) | Well-melted particles; good splat formation; dense, adherent coating | `#27AE60` |
| TOO FAR (> 150 mm) | Particles cool and solidify in flight; porous, weakly bonded coating | `#E05C5C` |

Each panel: Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, top accent 4 pt in panel color.

Inside each panel:
- Standoff label: Barlow SemiBold 18 pt, panel color
- Distance: JetBrains Mono 22 pt, panel color
- Result description: Inter Regular 13 pt `#F0EDE8`
- Arrow from "gun" rectangle to "substrate" line showing distance

---

### ZONE 5 -- Parameter-to-Property Map

**Section label:** `WHICH KNOB CONTROLS WHICH OUTCOME` -- Y: 22.2".

**BLOCK D -- Parameter Map**

Y: 22.9" to 28.3". Grid of parameter-property relationships.

| To Increase... | Adjust... |
|---|---|
| Coating density | Decrease standoff; increase power; use H2 secondary |
| Bond strength | Preheat substrate; optimize profile Ra; increase particle velocity |
| Deposition rate | Increase powder feed rate; increase power |
| Surface smoothness | Finer powder; increase particle velocity; closer standoff |
| Porosity (intentional, e.g., TBC) | Increase standoff; reduce power; coarser powder |
| Coating hardness | Optimize melting (fully molten splats); minimize oxide content |

Two-column layout. Left column: "To Increase..." (Barlow SemiBold 16 pt `#E8A020`). Right column: "Adjust..." (Inter Regular 14 pt `#F0EDE8`). Each row in rounded rect with left accent in `#E8A020`.

---

### ZONE 6 -- Deposition Efficiency

**Section label:** Y: 28.7".

**BLOCK E -- Full-Width Callout**

- Rounded rect, full width, H: 3.0", fill `#1E2435`, border 1 pt `#E8A020`

**Left (40%):** Big number: `40-70%` Barlow Condensed ExtraBold 56 pt `#E8A020`.
Label: `Deposition Efficiency (DE)` Inter Medium 16 pt `#F0EDE8`.

**Right (60%):**
- `Only 40-70% of powder actually becomes coating. The rest is overspray.` Inter Regular 14 pt `#F0EDE8`.
- `DE depends on: standoff, power, powder size, and spray angle.` Inter Regular 14 pt `#F0EDE8`.
- `Higher DE = lower cost per part. Optimize before scaling production.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Parameter Setup -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most data-dense poster in the APS cluster. The 14-row parameter table is the core reference -- an operator should be able to glance at the wall and find any parameter range. The standoff distance visual is the teaching moment: this is the single most common source of variation in APS, and understanding its effect is what separates a technician from an operator.

---

*Alaina -- Poster #485 -- Construction Workup v1.0 -- 2026-04-26*
