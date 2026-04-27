---
Project: Plating Posters Inc
Poster Number: 484
Title: "Equipment Setup -- Plasma Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 6)"
Technical Source: Plasma spray system components including gun architecture (cathode, anode, gas injection), power supply, gas console, powder feeder, robot, cooling, and booth requirements. 40-80 kW DC systems.
Process Scope: Atmospheric plasma spray -- equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Equipment
  - PlasmaGun
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #484 -- Construction Workup
## Equipment Setup -- Plasma Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of the APS process. This poster breaks down every major component of a plasma spray system. The hero is a labeled system component diagram showing how the power supply, gas console, powder feeder, robot, gun, and booth connect. Think of it as the "anatomy chart" of a plasma spray cell.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **System component diagram (Block B -- HERO):** 8 labeled component boxes connected by flow lines showing gas, power, powder, and water paths.
2. **Gun anatomy detail (Block C):** Enlarged cross-section representation of the plasma gun internals.
3. **Gas selection guide (Block D):** Primary and secondary gas options with roles.
4. **Startup sequence checklist (Block E):** Pre-spray equipment verification steps.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Slate)
ZONE 3 -- SYSTEM COMPONENTS HERO (4.2"--15.5" / ~11.3")
  Block B: 8-component system diagram
  Block C: Gun anatomy detail
ZONE 4 -- GAS SELECTION (15.5"--22.0" / ~6.5")
  Block D: Primary/secondary gas guide
ZONE 5 -- STARTUP SEQUENCE (22.0"--28.5" / ~6.5")
  Block E: Pre-spray checklist
ZONE 6 -- TROUBLESHOOTING (28.5"--32.5" / ~4.0")
  Block F: 4 equipment problems
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray Gun & System Components -- Stage 4 of 10` -- 32 pt `#3A4055` lightened to `#C8D0D8`. Y: 1.4".
**Tagline:** `A DC arc, two gases, a powder feeder, a robot, and a lot of cooling water. Here is how it all connects.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `40-80` -- 64 pt `#E8A020`
- Label: `kW DC power -- the engine of the plasma jet` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted (`#C8D0D8` fill, `#1A1F2E` text). Others dimmed.

---

### ZONE 3 -- System Components (HERO)

**Section label:** `PLASMA SPRAY SYSTEM -- 8 MAJOR COMPONENTS` -- Y: 4.4".

**BLOCK B -- System Component Diagram**

Y: 5.0" to 11.5". Full width. Eight labeled component boxes arranged to show connectivity.

Layout: Power supply (top-left) connects to gun (center). Gas console (top-center) connects to gun. Powder feeder (top-right) connects to gun. Robot (center-right) holds gun. Cooling (bottom-left) loops to gun. Booth (bottom-right) contains entire system. Control system (bottom-center) connects to all.

Each component box: Rounded rect, W: 5.0", H: 2.0", fill `#1E2435`, radius 6, top accent 4 pt.

| Component | Accent | Key Specs |
|---|---|---|
| 1. PLASMA GUN | `#E8A020` | Cathode: 2% thoriated tungsten. Anode: O2-free copper. Powder injector port(s). |
| 2. POWER SUPPLY | `#E8A020` | 40-80 kW DC. 400-800 A at 50-80 V. |
| 3. GAS CONSOLE | `#2EC4B6` | Mass flow controllers. Primary: Ar or N2. Secondary: H2, He, or N2. |
| 4. POWDER FEEDER | `#2EC4B6` | Volumetric or gravimetric. Carrier gas: Ar. 20-80 g/min. |
| 5. ROBOT | `#27AE60` | 6-axis industrial. Controls traverse speed, standoff, spray angle. |
| 6. COOLING SYSTEM | `#2EC4B6` | Closed-loop water. 15-25 L/min at 15-20 degC. |
| 7. SPRAY BOOTH | `#3A4055` | Enclosed. Dust collection (HEPA or cartridge). Downdraft preferred. |
| 8. CONTROL SYSTEM | `#3A4055` | PLC or proprietary. Real-time monitoring of all parameters. |

Connection lines: 2 pt dashed lines in `#3A4055` with labels:
- `DC POWER` (red-tinted) from power supply to gun
- `GAS` (teal-tinted) from gas console to gun
- `POWDER + CARRIER` (amber-tinted) from feeder to gun
- `COOLING WATER` (blue-tinted) from cooling to gun and back
- `ROBOT ARM` (green-tinted) from robot to gun

**BLOCK C -- Gun Anatomy (below diagram)**

Y: 12.0" to 15.3". Centered, W: 18.0".

Simplified cross-section view of plasma gun:
- Rounded rect representing gun body, W: 18.0", H: 2.5", fill `#252B3D`, border 2 pt `#C8D0D8`
- Internal labels (left to right):
  - `CATHODE (W-2%Th)` -- pointed shape, `#E05C5C` fill
  - `ARC ZONE` -- between cathode and anode, `#E8A020` glow
  - `ANODE (Cu, OFHC)` -- surrounding ring, `#C8D0D8`
  - `GAS INJECTION` -- arrows entering from top, `#2EC4B6`
  - `POWDER INJECTOR` -- arrow entering downstream, `#27AE60`
  - `PLASMA PLUME -->` -- exit right side, gradient `#E8A020` to `#E05C5C`
- Labels: JetBrains Mono 11 pt with leader lines

---

### ZONE 4 -- Gas Selection Guide

**Section label:** `GAS SELECTION -- PRIMARY AND SECONDARY` -- Y: 15.7".

**BLOCK D -- Gas Guide Table**

Y: 16.3" to 21.5".

| Gas | Role | Typical Flow | Effect on Plasma | When to Use |
|---|---|---|---|---|
| Argon (Ar) | Primary | 35-60 SLPM | Stabilizes arc; low enthalpy per unit | Standard primary for all APS work |
| Nitrogen (N2) | Primary (alt) | 30-50 SLPM | Higher enthalpy than Ar; cheaper | Non-reactive coatings; cost-sensitive |
| Hydrogen (H2) | Secondary | 5-15 SLPM | Dramatically increases enthalpy; hotter plume | Ceramics (YSZ, Al2O3); high-melt-point materials |
| Helium (He) | Secondary | 20-50 SLPM | Moderate enthalpy increase; gentler than H2 | Sensitive substrates; controlled heating |
| Nitrogen (N2) | Secondary | 5-20 SLPM | Lower cost alternative to H2/He | Budget applications; metallic coatings |

Callout below table:
- `CAUTION: Hydrogen is flammable. Leak detection mandatory. Never use H2 without proper flash-back arrestors and ventilation.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 5 -- Startup Sequence

**Section label:** `PRE-SPRAY STARTUP SEQUENCE` -- Y: 22.2".

**BLOCK E -- 10-Step Checklist**

Y: 22.9" to 28.3". Two columns of 5 steps.

| Step | Action |
|---|---|
| 1 | Verify cooling water flow and temperature (15-25 L/min, 15-20 degC) |
| 2 | Open gas supply -- check cylinder pressure and regulator settings |
| 3 | Set primary gas flow (Ar) on mass flow controller |
| 4 | Set secondary gas flow (H2/He) on mass flow controller |
| 5 | Power on control system; load recipe/program |
| 6 | Initiate high-frequency arc start -- verify stable arc |
| 7 | Adjust power to target (verify V and A on readout) |
| 8 | Start powder feeder; set carrier gas and feed rate |
| 9 | Run test passes on sacrificial coupon -- verify spray pattern |
| 10 | Begin production spray only after coupon verification passes |

Each step: Rounded rect, H: 0.95", fill alternating `#1E2435` / `#252B3D`.
Step number: Barlow Condensed ExtraBold 16 pt `#E8A020`. Action: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Troubleshooting

Four cards:

| Problem | Cause | Fix |
|---|---|---|
| ARC WON'T START | Gas flow too low; electrode worn; HF unit fault | Check gas flow; inspect cathode/anode; test HF igniter |
| UNSTABLE ARC | Worn anode or cathode; gas flow fluctuation | Replace consumables; verify mass flow controllers |
| POWDER CLOGGING | Moisture in powder; carrier gas too low; injector buildup | Dry powder; increase carrier gas; clean injector port |
| OVERHEATING GUN | Cooling water flow insufficient; water temp too high | Check pump and flow rate; verify chiller operation |

---

### ZONE 7 -- Footer

Standard. Title: `Equipment Setup -- Plasma Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Equipment Setup Plasma Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the "anatomy chart" poster. The system component diagram should feel like a block diagram an engineer would draw -- clean, logical, with clear flow paths. The gun anatomy detail is the centerpiece: cathode, arc zone, anode, gas injection, powder injection, and the plasma plume exiting. The gas selection guide answers the most common setup question: "which gases and how much?"

---

*Alaina -- Poster #484 -- Construction Workup v1.0 -- 2026-04-26*
