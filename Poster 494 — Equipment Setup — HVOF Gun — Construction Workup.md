---
Project: Plating Posters Inc
Poster Number: 494
Title: "Equipment Setup -- HVOF Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 6)"
Technical Source: Two main HVOF system types -- gas-fuel (Diamond Jet, Thermach) and liquid-fuel (JP-8000 type, kerosene). Combustion chamber, converging-diverging (de Laval) nozzle, barrel extension, powder feeder, gas/fuel metering, water cooling, robot, booth, control system. Major OEMs: Oerlikon Metco, Praxair/TAFA, Thermach, Kermetico, GTV.
Process Scope: HVOF thermal spray -- equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Equipment
  - HVOFGun
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #494 -- Construction Workup
## Equipment Setup -- HVOF Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of the HVOF process. The "anatomy chart" of an HVOF system. The hero distinguishes the two main system architectures: gas-fuel HVOF and liquid-fuel HVOF. The gun anatomy shows the combustion chamber, de Laval nozzle (the key component that creates supersonic flow), barrel extension, and powder injection point. This is the poster that explains WHY HVOF is supersonic -- it is the nozzle geometry.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-system comparison (Block B -- HERO):** Side-by-side comparison of gas-fuel vs. liquid-fuel HVOF.
2. **Gun anatomy detail (Block C):** Simplified cross-section of HVOF gun internals showing de Laval nozzle.
3. **System component diagram (Block D):** 9 major components and their connections.
4. **Startup sequence checklist (Block E):** Pre-spray equipment verification.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Slate)
ZONE 3 -- TWO-SYSTEM COMPARISON + GUN ANATOMY HERO (4.2"--15.5" / ~11.3")
  Block B: Gas-fuel vs. liquid-fuel comparison
  Block C: Gun anatomy cross-section
ZONE 4 -- SYSTEM COMPONENTS (15.5"--22.0" / ~6.5")
  Block D: 9-component system diagram
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
**Subheading:** `HVOF Gun & System Components -- Stage 4 of 10` -- 32 pt `#C8D0D8`. Y: 1.4".
**Tagline:** `A combustion chamber, a de Laval nozzle, supersonic gas flow. The nozzle geometry is what makes HVOF supersonic.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `Mach 2` -- 64 pt `#E8A020`
- Label: `typical gas jet velocity at nozzle exit` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted (`#C8D0D8` fill, `#1A1F2E` text). Others dimmed.

---

### ZONE 3 -- Two-System Comparison + Gun Anatomy (HERO)

**Section label:** `TWO HVOF ARCHITECTURES -- KNOW YOUR SYSTEM` -- Y: 4.4".

**BLOCK B -- Gas-Fuel vs. Liquid-Fuel Comparison (top half)**

Y: 5.0" to 9.5". Two side-by-side cards.

**Left -- Gas-Fuel HVOF (W: 11.0"):**
- Rounded rect, X: 0.5", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `GAS-FUEL HVOF` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Diamond Jet, Thermach, GTV` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Fuel gases | Hydrogen, propylene, propane, ethylene, natural gas |
| Combustion pressure | 60-100 PSI |
| Particle velocity | 500-750 m/s |
| Advantages | More parameter flexibility; broader feedstock range |
| Preferred for | Diverse applications; R&D; multi-material shops |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono 12 pt `#F0EDE8`.

**Right -- Liquid-Fuel HVOF (W: 11.5"):**
- Rounded rect, X: 12.0", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `LIQUID-FUEL HVOF` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `JP-8000, Praxair/TAFA, Kermetico AK` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Fuel | Kerosene (JP-5 type) atomized with O2 |
| Combustion pressure | 80-150 PSI |
| Particle velocity | 700-900 m/s |
| Advantages | Higher velocity; preferred for densest WC-Co coatings |
| Preferred for | Aerospace WC-Co hardface; chrome replacement |

Bottom note spanning both cards:
`Both architectures produce excellent coatings. Liquid-fuel dominates aerospace WC-Co work because of higher particle velocity. Gas-fuel offers more versatility for mixed-material shops.` Inter Medium 13 pt `#F0EDE8` at 70%.

**BLOCK C -- Gun Anatomy Detail (bottom half)**

Y: 10.5" to 15.3". Centered, W: 22.0".

Simplified cross-section view of HVOF gun:
- Rounded rect representing gun body, W: 22.0", H: 3.5", fill `#252B3D`, border 2 pt `#C8D0D8`
- Internal labels (left to right):
  - `FUEL + O2 INLET` -- arrows entering from left, `#E8A020`
  - `COMBUSTION CHAMBER` -- large zone, `#E05C5C` fill at 20%
  - `DE LAVAL NOZZLE` -- converging-diverging pinch point, `#E8A020` accent, labeled `(converging-diverging -- creates supersonic flow)`
  - `BARREL EXTENSION` -- straight section after nozzle, `#3A4055`
  - `POWDER INJECTION` -- arrow entering barrel, `#27AE60`, labeled `(axial or radial)`
  - `SUPERSONIC JET -->` -- exit right side, gradient `#E8A020` to `#E05C5C`
- `WATER COOLING JACKET` -- annotation along top and bottom of gun body, `#2EC4B6`
- Labels: JetBrains Mono 11 pt with leader lines

Key callout below diagram:
`The de Laval nozzle is the defining component. Gas accelerates through the converging section, reaches Mach 1 at the throat, and expands to supersonic velocity (Mach 1.5-3.0) in the diverging section. This is the same principle used in rocket engines.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- System Components

**Section label:** `HVOF SYSTEM -- 9 MAJOR COMPONENTS` -- Y: 15.7".

**BLOCK D -- System Component Table**

Y: 16.3" to 21.8". Full width. 9 rows.

| Component | Accent | Key Specs |
|---|---|---|
| 1. HVOF GUN | `#E8A020` | Combustion chamber + de Laval nozzle + barrel. Water-cooled. |
| 2. FUEL SUPPLY | `#E8A020` | Gas: cylinders with regulators + MFCs. Liquid: kerosene pump + atomizer. |
| 3. OXYGEN SUPPLY | `#E05C5C` | High-pressure O2. OIL-FREE fittings mandatory. Up to 150 PSI. |
| 4. POWDER FEEDER | `#2EC4B6` | Gravimetric preferred for consistency. Carrier gas: N2 or Ar, 8-15 SLPM. |
| 5. GAS/FUEL METERING | `#2EC4B6` | Mass flow controllers for precise fuel:O2 ratio control. |
| 6. WATER COOLING | `#2EC4B6` | Closed-loop, 15-25 L/min at 15-20 degC. Gun and nozzle cooling. |
| 7. ROBOT | `#27AE60` | 6-axis industrial robot. Controls traverse, standoff, angle. |
| 8. SPRAY BOOTH | `#3A4055` | Enclosed. HEPA dust collection. Critical for cobalt fume capture. |
| 9. CONTROL SYSTEM | `#3A4055` | PLC or proprietary. Data logging for process qualification. |

Each row: alternating `#1E2435` / `#252B3D`, H: 0.55".
Component name: Barlow SemiBold 13 pt, accent color. Specs: JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 5 -- Startup Sequence

**Section label:** `PRE-SPRAY STARTUP SEQUENCE` -- Y: 22.2".

**BLOCK E -- 10-Step Checklist**

Y: 22.9" to 28.3". Two columns of 5 steps.

| Step | Action |
|---|---|
| 1 | Verify cooling water flow and temperature (15-25 L/min, 15-20 degC) |
| 2 | Open oxygen supply -- check cylinder pressure and regulator; verify oil-free fittings |
| 3 | Open fuel supply -- gas: check cylinder/regulator; liquid: prime kerosene pump |
| 4 | Set oxygen and fuel flows on metering console |
| 5 | Power on control system; load recipe/program for target coating |
| 6 | Initiate ignition sequence -- verify stable combustion |
| 7 | Adjust fuel:O2 ratio to target combustion pressure |
| 8 | Start powder feeder; set carrier gas and feed rate |
| 9 | Run test passes on sacrificial coupon -- verify spray pattern and deposition rate |
| 10 | Begin production spray only after coupon verification passes |

Each step: Rounded rect, H: 0.95", fill alternating `#1E2435` / `#252B3D`.
Step number: Barlow Condensed ExtraBold 16 pt `#E8A020`. Action: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Troubleshooting

Four cards:

| Problem | Cause | Fix |
|---|---|---|
| IGNITION FAILURE | Gas flow ratio wrong; igniter fault | Verify fuel:O2 ratio; test ignition system |
| UNSTABLE COMBUSTION | Fuel flow fluctuation; worn nozzle | Check MFCs; inspect nozzle for erosion or buildup |
| POWDER CLOGGING | Moisture in powder; carrier gas too low | Dry powder; increase carrier gas; clean injector |
| GUN OVERHEATING | Cooling water flow insufficient; blockage | Check pump and flow rate; inspect for scale buildup |

---

### ZONE 7 -- Footer

Standard. Title: `Equipment Setup -- HVOF Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Equipment Setup HVOF Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-architecture comparison is what makes this poster unique from the APS equipment poster. Every HVOF shop needs to know which system type they are running because the parameters, fuel handling, and safety considerations differ significantly. The de Laval nozzle is the teaching moment -- it is the single component that makes HVOF supersonic. The rocket engine analogy lands with any audience because everyone understands that rockets are fast.

---

*Alaina -- Poster #494 -- Construction Workup v1.0 -- 2026-04-26*
