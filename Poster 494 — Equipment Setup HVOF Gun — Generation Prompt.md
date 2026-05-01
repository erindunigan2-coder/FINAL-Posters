---
Project: Plating Posters Inc
Poster Number: 494
Title: "Equipment Setup -- HVOF Gun"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 494 — Equipment Setup — HVOF Gun — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - HVOF
  - Equipment
  - HVOFGun
  - ClusterTS02
  - v1
---

# Claude Chat Generation Prompt -- Poster #494
## Equipment Setup -- HVOF Gun
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `EQUIPMENT SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `HVOF Gun & System Components -- Stage 4 of 10` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `A combustion chamber, a de Laval nozzle, supersonic gas flow. The nozzle geometry is what makes HVOF supersonic.` -- `20` pt at 65%. Y: **2.1"**.

**Rule card** (right side):
- Big number: `Mach 2` -- 64 pt `#E8A020`
- Label: `typical gas jet velocity at nozzle exit` -- 14 pt `#F0EDE8`

---

## Phase 3 -- Orientation Strip

Stage 4 highlighted (`#C8D0D8` fill, `#1A1F2E` text). Others dimmed.

---

## Phase 4 -- Two-System Comparison + Gun Anatomy (HERO)

Y: 4.2" to 15.5". Section label: `TWO HVOF ARCHITECTURES -- KNOW YOUR SYSTEM` centered, 28 pt.

### Gas-Fuel vs. Liquid-Fuel (Y: 5.0"-9.5")

**Left -- Gas-Fuel HVOF (W: 11.0", accent `#2EC4B6`):**
Title: `GAS-FUEL HVOF`. Subtitle: `Diamond Jet, Thermach, GTV`.

| Property | Value |
|---|---|
| Fuel gases | Hydrogen, propylene, propane, ethylene, natural gas |
| Combustion pressure | 60-100 PSI |
| Particle velocity | 500-750 m/s |
| Advantages | More parameter flexibility; broader feedstock range |
| Preferred for | Diverse applications; R&D; multi-material shops |

**Right -- Liquid-Fuel HVOF (W: 11.5", accent `#E8A020`):**
Title: `LIQUID-FUEL HVOF`. Subtitle: `JP-8000, Praxair/TAFA, Kermetico AK`.

| Property | Value |
|---|---|
| Fuel | Kerosene (JP-5 type) atomized with O2 |
| Combustion pressure | 80-150 PSI |
| Particle velocity | 700-900 m/s |
| Advantages | Higher velocity; preferred for densest WC-Co coatings |
| Preferred for | Aerospace WC-Co hardface; chrome replacement |

Bottom note: `Both architectures produce excellent coatings. Liquid-fuel dominates aerospace WC-Co work because of higher particle velocity. Gas-fuel offers more versatility for mixed-material shops.`

### Gun Anatomy Cross-Section (Y: 10.5"-15.3")

Simplified horizontal cross-section of HVOF gun, W: 22.0", fill `#252B3D`, border 2pt `#C8D0D8`. Internal labels left to right:
- `FUEL + O2 INLET` (arrows from left, `#E8A020`)
- `COMBUSTION CHAMBER` (large zone, `#E05C5C` fill at 20%)
- `DE LAVAL NOZZLE` (converging-diverging pinch, `#E8A020`, label: `converging-diverging -- creates supersonic flow`)
- `BARREL EXTENSION` (straight section, `#3A4055`)
- `POWDER INJECTION` (arrow entering barrel, `#27AE60`, label: `axial or radial`)
- `SUPERSONIC JET -->` (exit right, gradient `#E8A020` to `#E05C5C`)
- `WATER COOLING JACKET` (annotation top/bottom, `#2EC4B6`)

Key callout: `The de Laval nozzle is the defining component. Gas accelerates through the converging section, reaches Mach 1 at the throat, and expands to supersonic velocity (Mach 1.5-3.0) in the diverging section. This is the same principle used in rocket engines.` 13pt `#E8A020`.

---

## Phase 5 -- System Components + Startup Sequence

### 9 System Components (Y: 15.5"-22.0")

Section label: `HVOF SYSTEM -- 9 MAJOR COMPONENTS` centered, 28 pt.

9-row table, alternating `#1E2435` / `#252B3D`:

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

Component name in accent color. Specs: JetBrains Mono 11pt.

### Startup Sequence (Y: 22.0"-28.5")

Section label: `PRE-SPRAY STARTUP SEQUENCE` centered, 28 pt.

10-step checklist, two columns of 5. Alternating fills.

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

Step number: Barlow Condensed ExtraBold 16pt `#E8A020`.

---

## Phase 6 -- Troubleshooting

Y: 28.5" to 32.5". Four cards in a row, left accent `#E05C5C`:

| Problem | Cause | Fix |
|---|---|---|
| IGNITION FAILURE | Gas flow ratio wrong; igniter fault | Verify fuel:O2 ratio; test ignition system |
| UNSTABLE COMBUSTION | Fuel flow fluctuation; worn nozzle | Check MFCs; inspect nozzle for erosion or buildup |
| POWDER CLOGGING | Moisture in powder; carrier gas too low | Dry powder; increase carrier gas; clean injector |
| GUN OVERHEATING | Cooling water flow insufficient; blockage | Check pump and flow rate; inspect for scale buildup |

---

## Phase 7 -- Footer

Standard. Title: `Equipment Setup -- HVOF Gun`. Version `v1.0 -- 2026`.

---

## Phase 8 -- Review

- [ ] Headline `EQUIPMENT SETUP` 80pt
- [ ] Rule card with Mach 2
- [ ] Orientation strip with stage 4 highlighted
- [ ] Gas-fuel vs. liquid-fuel side-by-side comparison
- [ ] Gun anatomy cross-section with de Laval nozzle labeled
- [ ] 9-component system table
- [ ] 10-step startup checklist
- [ ] Four troubleshooting cards
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Equipment Setup HVOF Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
