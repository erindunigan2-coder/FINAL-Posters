---
Project: Plating Posters Inc
Poster Number: 495
Title: "Parameter Setup -- HVOF"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 495 — Parameter Setup — HVOF — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - HVOF
  - Parameters
  - ClusterTS02
  - v1
---

# Claude Chat Generation Prompt -- Poster #495
## Parameter Setup -- HVOF
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PARAMETER SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `HVOF -- Gas-Fuel vs. Liquid-Fuel Operating Windows -- Stage 5 of 10` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `Two system types. Two parameter sets. Using the wrong recipe for your system type is the fastest way to scrap parts.` -- `20` pt at 65%. Y: **2.1"**.

**Rule card** (right side):
- Big number: `12` -- 72 pt `#E8A020`
- Label: `controllable parameters -- matched to your system type` -- 14 pt `#F0EDE8`

---

## Phase 3 -- Orientation Strip

Stage 5 highlighted. Others dimmed.

---

## Phase 4 -- Dual Parameter Table (HERO)

Y: 4.2" to 15.5". Section label: `HVOF OPERATING PARAMETERS -- GAS-FUEL VS. LIQUID-FUEL` centered, 28 pt.

12-row dual-column table. Header fill `#3A4055`. Gas-Fuel header in `#2EC4B6`, Liquid-Fuel header in `#E8A020`. Alternating rows `#1E2435` / `#252B3D`.

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

Gas-fuel values tinted `#2EC4B6`. Liquid-fuel values tinted `#E8A020`.

---

## Phase 5 -- Standoff Distance + Fuel:O2 Ratio

### Standoff Distance (Y: 15.5"-22.0")

Section label: `STANDOFF DISTANCE -- LONGER THAN APS, STILL CRITICAL` centered, 28 pt.

Three panels side by side, top accent 4pt in panel color:

| Standoff | Result | Color |
|---|---|---|
| TOO CLOSE (< 150 mm gas / < 300 mm liquid) | Substrate overheating; coating stress; risk of delamination | `#E05C5C` |
| OPTIMAL (150-300 mm gas / 300-400 mm liquid) | Semi-molten particles at peak velocity; dense, adherent coating | `#27AE60` |
| TOO FAR (> 300 mm gas / > 400 mm liquid) | Particles decelerate and cool; porosity increases; bond weakens | `#E05C5C` |

Standoff label: Barlow SemiBold 18pt. Distance: JetBrains Mono 22pt.

Key note: `HVOF standoff is much longer than APS (75-150 mm). This is because the supersonic gas jet maintains particle velocity over a longer flight path. Do not use APS standoff distances on HVOF equipment.` 13pt `#E8A020`.

### Fuel:O2 Ratio (Y: 22.0"-28.5")

Section label: `THE FUEL:O2 RATIO -- THE MASTER CONTROL` centered, 28 pt.

**Left -- What It Controls (W: 11.5", accent `#E8A020`):**
Title: `FUEL:O2 RATIO CONTROLS EVERYTHING`. Controls: combustion temperature (flame stoichiometry); gas jet velocity; particle heating (too hot = decarburization of WC); particle velocity. STOICHIOMETRIC = max temp. FUEL-RICH = lower temp, less WC decomposition (preferred for WC-Co). OXYGEN-RICH = oxidizing atmosphere, higher oxide content (generally avoided).

**Right -- Practical Guidance (W: 11.0", accent `#27AE60`):**
Title: `TUNING THE RATIO`.

| Condition | Result | Action |
|---|---|---|
| Low hardness | WC decarburizing (too hot) | Go fuel-rich; reduce O2 |
| High oxide content | Oxidizing flame | Reduce O2; verify ratio |
| Low density | Velocity too low | Increase combustion pressure |
| Spitting / unmelted | Particles too cold | Go slightly leaner; increase dwell |

Note: `For WC-Co coatings, a slightly fuel-rich ratio is standard practice to minimize WC decomposition (decarburization). This preserves the carbide phase that provides hardness.` 12pt `#E8A020`.

---

## Phase 6 -- Deposition Efficiency

Y: 28.5" to 32.5". Full-width callout, fill `#1E2435`, border 1pt `#E8A020`.

**Left (40%):** Big number: `50-70%` Barlow Condensed ExtraBold 56pt `#E8A020`. Label: `Deposition Efficiency (DE)` 16pt.

**Right (60%):**
- `50-70% of powder becomes coating. The rest is overspray collected by dust extraction.`
- `HVOF DE is slightly higher than APS (40-70%) due to higher particle velocity and momentum.`
- `Higher DE = lower cost per part. WC-Co powder is expensive -- optimize before scaling.` in `#27AE60`.

---

## Phase 7 -- Footer

Standard. Title: `Parameter Setup -- HVOF`. Version `v1.0 -- 2026`.

---

## Phase 8 -- Review

- [ ] Headline `PARAMETER SETUP` 80pt
- [ ] Rule card with 12 controllable parameters
- [ ] Orientation strip with stage 5 highlighted
- [ ] 12-row dual-column parameter table with color-coded values
- [ ] Three standoff distance panels (too close / optimal / too far)
- [ ] Fuel:O2 ratio two-column explanation
- [ ] Deposition efficiency callout with 50-70%
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Parameter Setup HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
