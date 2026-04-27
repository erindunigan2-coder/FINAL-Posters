---
Project: Plating Posters Inc
Poster Number: 495
Title: "Parameter Setup -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 7)"
Technical Source: Complete HVOF parameter ranges for both gas-fuel and liquid-fuel systems. Dual-column parameter table showing differences between architectures. Standoff distance 150-400 mm (much longer than APS). Combustion pressure 60-150 PSI.
Process Scope: HVOF thermal spray -- spray parameter setup and optimization
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Parameters
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #495 -- Construction Workup
## Parameter Setup -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of the HVOF process. This is the data-dense poster -- the operating window for every controllable parameter across BOTH system types (gas-fuel and liquid-fuel). The hero is a dual-column parameter table. The key teaching point: gas-fuel and liquid-fuel HVOF have significantly different parameter ranges, especially for oxygen flow, fuel flow, combustion pressure, and standoff distance. Using gas-fuel parameters on a liquid-fuel system (or vice versa) produces bad coatings.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-column parameter table (Block B -- HERO):** 12-row table with separate columns for gas-fuel and liquid-fuel.
2. **Standoff distance effect (Block C):** Visual showing HVOF standoff (longer than APS).
3. **Fuel:O2 ratio callout (Block D):** The critical ratio that controls combustion temperature.
4. **Deposition efficiency callout (Block E):** 50-70% DE explained.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Slate)
ZONE 3 -- DUAL PARAMETER TABLE HERO (4.2"--15.5" / ~11.3")
  Block B: 12-row dual-column parameter table
ZONE 4 -- STANDOFF DISTANCE EFFECT (15.5"--22.0" / ~6.5")
  Block C: Standoff visual + density relationship
ZONE 5 -- FUEL:O2 RATIO (22.0"--28.5" / ~6.5")
  Block D: Combustion stoichiometry and its effect
ZONE 6 -- DEPOSITION EFFICIENCY (28.5"--32.5" / ~4.0")
  Block E: 50-70% DE explained
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- Gas-Fuel vs. Liquid-Fuel Operating Windows -- Stage 5 of 10` -- 32 pt `#C8D0D8`. Y: 1.4".
**Tagline:** `Two system types. Two parameter sets. Using the wrong recipe for your system type is the fastest way to scrap parts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `12` -- 72 pt `#E8A020`
- Label: `controllable parameters -- matched to your system type` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted. Others dimmed.

---

### ZONE 3 -- Dual Parameter Table (HERO)

**Section label:** `HVOF OPERATING PARAMETERS -- GAS-FUEL VS. LIQUID-FUEL` -- Y: 4.4".

**BLOCK B -- 12-Row Dual-Column Parameter Table**

Y: 5.0" to 15.3". Full width. Columns: Parameter (4.0") | Gas-Fuel (5.5") | Liquid-Fuel (5.5") | Units (2.0") | Notes (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.6". Barlow SemiBold, 13 pt, `#F0EDE8`.
- Gas-Fuel column header in `#2EC4B6`
- Liquid-Fuel column header in `#E8A020`

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Parameter | Gas-Fuel | Liquid-Fuel | Units | Notes |
|---|---|---|---|---|
| Oxygen flow | 200-400 | 800-1000 | SLPM | Liquid-fuel uses 2-4x more O2 |
| Fuel flow | H2: 400-700; C3H6: 60-80 | Kerosene: 18-26 | SLPM / L/hr | Different fuel types and units |
| Combustion pressure | 60-100 | 80-150 | PSI | Higher pressure = higher velocity |
| Particle velocity | 500-750 | 700-900 | m/s | Liquid-fuel achieves highest velocities |
| Gas jet temperature | 2500-3100 | 2600-3200 | degC | Both well above WC-Co melting |
| Powder feed rate | 30-80 | 40-100 | g/min | Liquid-fuel can handle higher throughput |
| Carrier gas (N2 or Ar) | 8-15 | 8-15 | SLPM | Same for both system types |
| Standoff distance | 150-300 | 300-400 | mm | Liquid-fuel sprays at greater distance |
| Spray angle | 75-90 | 75-90 | degrees | Same for both |
| Traverse speed | 300-1000 | 300-1000 | mm/s | Robot-controlled |
| Deposition rate | 2-8 | 3-10 | kg/hr | Liquid-fuel slightly higher |
| Deposition efficiency | 50-70 | 50-70 | % | Comparable between types |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Gas-fuel values tinted `#2EC4B6`. Liquid-fuel values tinted `#E8A020`.

---

### ZONE 4 -- Standoff Distance Effect

**Section label:** `STANDOFF DISTANCE -- LONGER THAN APS, STILL CRITICAL` -- Y: 15.7".

**BLOCK C -- Standoff Visual**

Y: 16.3" to 21.8". Three-panel comparison.

| Standoff | Result | Color |
|---|---|---|
| TOO CLOSE (< 150 mm gas / < 300 mm liquid) | Substrate overheating; coating stress; risk of delamination | `#E05C5C` |
| OPTIMAL (150-300 mm gas / 300-400 mm liquid) | Semi-molten particles at peak velocity; dense, adherent coating | `#27AE60` |
| TOO FAR (> 300 mm gas / > 400 mm liquid) | Particles decelerate and cool; porosity increases; bond weakens | `#E05C5C` |

Each panel: Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, top accent 4 pt in panel color.

Inside each panel:
- Standoff label: Barlow SemiBold 18 pt, panel color
- Distance: JetBrains Mono 22 pt, panel color
- Result description: Inter Regular 13 pt `#F0EDE8`

Key comparison note below panels:
`HVOF standoff is much longer than APS (75-150 mm). This is because the supersonic gas jet maintains particle velocity over a longer flight path. Do not use APS standoff distances on HVOF equipment.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Fuel:O2 Ratio

**Section label:** `THE FUEL:O2 RATIO -- THE MASTER CONTROL` -- Y: 22.2".

**BLOCK D -- Ratio Explanation**

Y: 22.9" to 28.3". Two-column layout.

**Left -- What It Controls (W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `FUEL:O2 RATIO CONTROLS EVERYTHING` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
The fuel-to-oxygen ratio determines:
- Combustion temperature (flame stoichiometry)
- Gas jet velocity (pressure and expansion)
- Particle heating (too hot = decarburization of WC)
- Particle velocity (directly proportional to gas velocity)

STOICHIOMETRIC = maximum temperature
FUEL-RICH = lower temperature, less WC decomposition
  (preferred for WC-Co coatings)
OXYGEN-RICH = oxidizing atmosphere, higher oxide content
  (generally avoided for carbide coatings)
```

**Right -- Practical Guidance (W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `TUNING THE RATIO` Barlow SemiBold 18 pt `#27AE60`

| Condition | Result | Action |
|---|---|---|
| Low hardness | WC decarburizing (too hot) | Go fuel-rich; reduce O2 |
| High oxide content | Oxidizing flame | Reduce O2; verify ratio |
| Low density | Velocity too low | Increase combustion pressure |
| Spitting / unmelted | Particles too cold | Go slightly leaner; increase dwell |

Note: `For WC-Co coatings, a slightly fuel-rich ratio is standard practice to minimize WC decomposition (decarburization). This preserves the carbide phase that provides hardness.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 6 -- Deposition Efficiency

**Section label:** Y: 28.7".

**BLOCK E -- Full-Width Callout**

- Rounded rect, full width, H: 3.0", fill `#1E2435`, border 1 pt `#E8A020`

**Left (40%):** Big number: `50-70%` Barlow Condensed ExtraBold 56 pt `#E8A020`.
Label: `Deposition Efficiency (DE)` Inter Medium 16 pt `#F0EDE8`.

**Right (60%):**
- `50-70% of powder becomes coating. The rest is overspray collected by dust extraction.` Inter Regular 14 pt `#F0EDE8`.
- `HVOF DE is slightly higher than APS (40-70%) due to higher particle velocity and momentum.` Inter Regular 14 pt `#F0EDE8`.
- `Higher DE = lower cost per part. WC-Co powder is expensive -- optimize before scaling.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Parameter Setup -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-column parameter table is the centerpiece and the unique feature of this poster. No other thermal spray process has two fundamentally different system architectures with different parameter ranges. The fuel:O2 ratio section is the advanced teaching content -- understanding stoichiometry is what separates a technician from an operator in HVOF. The WC decarburization problem (fuel-lean = hot = carbide decomposition = low hardness) is the most common quality failure in HVOF WC-Co work.

---

*Alaina -- Poster #495 -- Construction Workup v1.0 -- 2026-04-26*
