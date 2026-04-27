---
Project: Plating Posters Inc
Poster Number: 554
Title: "Equipment Setup -- Wire Spray System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 8: Wire Combustion Spray)"
Technical Source: Wire combustion spray system = oxy-fuel nozzle, wire feed mechanism (air-turbine or electric motor), compressed air cap (atomizer), wire guide tube, gas supply (O2 + C2H2 or propane), and compressed air supply. The entire setup fits in a pickup truck. Major OEMs: Oerlikon Metco (14E), Metallisation Ltd (Mark 73), Saint-Gobain, Thermach, Flame Spray Technologies.
Process Scope: Wire combustion spray equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - WireCombustionSpray
  - Equipment
  - ConstructionWorkup
  - ClusterTS08
---

# Poster #554 -- Construction Workup
## Equipment Setup -- Wire Spray System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The wire combustion spray system is beautifully simple compared to plasma or HVOF. Four main gun components, two gas bottles, an air compressor, and a wire spool. The entire rig fits in a pickup truck -- that portability is the process's killer advantage. Hero visual: numbered component list showing the complete system. The gas supply section needs special attention because of acetylene safety rules.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SYSTEM COMPONENTS / HERO (2.9"--15.5")
  Block B: Numbered component list with descriptions
ZONE 3 -- GAS & AIR SUPPLY (15.5"--22.0")
  Block C: Gas supply specifications (O2, C2H2, propane)
  Block D: Compressed air requirements
ZONE 4 -- GUN ANATOMY + WIRE FEED (22.0"--28.5")
  Block E: Gun component breakdown
  Block F: Wire feed mechanism types
ZONE 5 -- OEM SYSTEMS + PORTABILITY (28.5"--32.5")
  Block G: Major OEM guns and portability advantage
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Wire Spray System -- The Most Portable Thermal Spray Setup` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Gun, gas bottles, air compressor, wire spool. Fits in a pickup truck. No power supply, no robot, no spray booth required. This is thermal spray at its most accessible.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- System Components (HERO)

**Section label:** `WIRE COMBUSTION SPRAY SYSTEM COMPONENTS` -- Y: 3.1".

**BLOCK B -- Component List**

Y: 3.8" to 15.3". 8 components in two columns. Each component card: rounded rect, W: 11.0", H: 2.5", fill `#1E2435`.

| # | Component | Key Specs |
|---|---|---|
| 1 | Wire Spray Gun | Hand-held; oxy-fuel nozzle, wire feed, air cap, guide tube |
| 2 | Oxygen Supply | Cylinder or manifold; regulated 20--40 PSI |
| 3 | Fuel Gas Supply | Acetylene (10--15 PSI; NEVER > 15) or propane (10--20 PSI) |
| 4 | Compressed Air Supply | Compressor or plant air; 40--80 PSI at 20--40 CFM |
| 5 | Wire Spool | 1.6--4.8 mm (1/16--3/16") diameter; on gun-mounted or stand reel |
| 6 | Gas Hoses & Regulators | Twin hose (O2/fuel); flashback arrestors on both lines |
| 7 | Air Hose | 3/8" or 1/2" ID; rated for working pressure |
| 8 | Control Valves (on gun) | O2, fuel, air, and wire feed controls at operator's hand |

Each card has a number badge (Barlow Condensed ExtraBold 14 pt, white on `#3A4055` rounded rect).

Note at bottom: `That's it. No power supply, no robot, no powder feeder, no cooling system, no PLC. The simplest thermal spray equipment in existence.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 3 -- Gas & Air Supply

**Section label:** `GAS & AIR SUPPLY SPECIFICATIONS` -- Y: 15.7".

**Left -- BLOCK C: Gas Supply (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".

Title: `FUEL & OXYGEN` Barlow SemiBold 20 pt `#E05C5C`.

| Gas | Pressure | Flow Rate | Notes |
|---|---|---|---|
| Oxygen | 20--40 PSI (regulated) | 30--60 SCFH | Adjust for neutral or slightly oxidizing flame |
| Acetylene | 10--15 PSI (regulated) | 15--40 SCFH | NEVER exceed 15 PSI -- decomposition risk |
| Propane (alternative) | 10--20 PSI | 20--50 SCFH | Safer; lower flame temp (~2800 degC vs. ~3100 degC) |

Safety callout (JetBrains Mono 16 pt `#E05C5C`):
`ACETYLENE: NEVER EXCEED 15 PSI GAUGE`

Additional notes (Inter Regular 13 pt):
- `Flashback arrestors on BOTH O2 and fuel lines -- mandatory`
- `Secure cylinders upright; chain to cart or wall`
- `Test connections with soapy water -- never open flame`
- `Purge each line separately before lighting`

**Right -- BLOCK D: Compressed Air (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".

Title: `ATOMIZING AIR` Barlow SemiBold 20 pt `#2EC4B6`.

| Parameter | Specification |
|---|---|
| Pressure | 40--80 PSI |
| Flow rate | 20--40 CFM |
| Quality | Dry, oil-free |
| Source | Portable compressor or plant air |
| Function | Atomizes molten wire tip into droplets; propels toward substrate |

Note: `Higher air pressure = finer atomization = denser coating. But also more overspray. Balance for your application.` Inter Medium 13 pt `#E8A020`.

Portability note: `A portable compressor rated at 40+ CFM and 80+ PSI is sufficient. Gas-powered compressors for field work where electrical power is unavailable.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- Gun Anatomy + Wire Feed

**Section label:** `GUN COMPONENTS & WIRE FEED` -- Y: 22.2".

**Left -- BLOCK E: Gun Component Breakdown (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `GUN ANATOMY` Barlow SemiBold 20 pt `#E8A020`.

| Component | Function |
|---|---|
| Oxy-fuel nozzle | Concentric flame cone; mixes fuel and oxygen |
| Wire guide tube | Centers wire in flame; feeds through nozzle center |
| Compressed air cap | Surrounds flame; atomizes molten wire tip |
| Wire feed drive | Pulls wire from spool through guide tube |
| Trigger / controls | Start/stop wire feed; some guns have air and gas valves on-gun |

Note: `The gun is self-contained and hand-held. Operator controls wire feed, flame, and air from the gun. Total weight: typically 1--3 kg (2--7 lb).` Inter Medium 13 pt `#2EC4B6`.

**Right -- BLOCK F: Wire Feed Mechanisms (X: 12.0", W: 11.5"):**

Two sub-panels:

*Air-Turbine Feed:*
Rounded rect, fill `#252B3D`, left accent `#27AE60` 0.06".
- `Atomizing air drives a small turbine that powers wire feed rollers`
- `Self-powered -- no electrical connection needed`
- `Wire speed varies with air pressure (linked)`
- `Simpler; standard on most portable guns`

*Electric Motor Feed:*
Rounded rect, fill `#252B3D`, left accent `#E8A020` 0.06".
- `Electric motor drives wire feed independently of air pressure`
- `Wire speed adjustable independently`
- `Requires electrical power (battery or mains)`
- `More precise; preferred for shop and automated setups`

---

### ZONE 5 -- OEM Systems + Portability

**Section label:** `EQUIPMENT MANUFACTURERS & PORTABILITY` -- Y: 28.7".

**Left -- OEM Table (X: 0.5", W: 11.0"):**

| OEM | Gun Model | Notes |
|---|---|---|
| Oerlikon Metco | 14E | Industry standard; widely available |
| Metallisation Ltd | Mark 73 | UK manufacturer; popular worldwide |
| Saint-Gobain | Various | Integrated systems |
| Thermach | Various | North American |
| Flame Spray Technologies | Various | European |

**Right -- Portability Callout (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `THE PORTABILITY ADVANTAGE` Barlow SemiBold 20 pt `#27AE60`.

```
Complete wire spray rig:
- Gun (1--3 kg)
- O2 cylinder
- Fuel gas cylinder
- Air compressor (portable, gas-powered)
- Wire spool(s)
- Hoses, regulators, accessories

Total: fits in a pickup truck bed or small trailer.
No electrical power required for the gun itself.
Ready to spray in 15--30 minutes on arrival.
```

`This is why wire combustion spray dominates field corrosion protection. You go to the structure -- the structure doesn't come to you.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 6 -- Footer

Standard. Title: `Equipment Setup -- Wire Spray System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Equipment Setup Wire Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #554 -- Construction Workup v1.0 -- 2026-04-26*
