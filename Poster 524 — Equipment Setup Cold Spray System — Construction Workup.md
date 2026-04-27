---
Project: Plating Posters Inc
Poster Number: 524
Title: "Equipment Setup -- Cold Spray System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray system components, HPCS vs. LPCS classification, de Laval nozzle design, gas heating and powder feeding. Zero brand names.
Process Scope: Cold spray -- equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - Equipment
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #524 -- Construction Workup
## Equipment Setup -- Cold Spray System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Equipment poster for Cold Spray. The hero element is the system schematic showing the key components: high-pressure gas supply, gas heater, de Laval nozzle, powder feeder, robot, and spray booth. The critical HPCS vs. LPCS distinction defines the entire equipment class and must be clearly presented.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **System schematic (Block B -- HERO):** Block diagram showing gas flow from supply through heater, through nozzle, to substrate. Powder injection point. Built with rectangles, arrows, and labels.
2. **HPCS vs. LPCS comparison (Block C):** Two-column comparison -- the fundamental equipment classification.
3. **Component detail cards (Block D):** Individual cards for de Laval nozzle, gas heater, powder feeder, and robot.
4. **De Laval nozzle detail (Block E):** Schematic of converging-diverging nozzle geometry.
5. **Helium vs. Nitrogen trade-off (Block F):** Decision guide for carrier gas selection.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SYSTEM SCHEMATIC HERO (2.9"--14.5" / ~11.6")
  Block B: System block diagram
ZONE 3 -- HPCS VS. LPCS (14.5"--21.5" / ~7.0")
  Block C: Two-column comparison
ZONE 4 -- COMPONENT DETAILS + NOZZLE (21.5"--32.5" / ~11.0")
  Block D: Component cards (2x2 grid)
  Block E: De Laval nozzle schematic
  Block F: Helium vs. Nitrogen callout
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `Cold Spray System -- High-Pressure Gas, De Laval Nozzle, Solid-State Deposition` -- 30 pt `#3A4055` adjusted to `#E8A020` (Amber). Y: 1.5".
**Tagline:** `No arc. No flame. No plasma. Just gas pressure, heat, and a converging-diverging nozzle that turns powder into a supersonic stream.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- System Schematic Hero

**Section label:** `COLD SPRAY SYSTEM -- COMPONENT LAYOUT` -- Y: 3.1".

**BLOCK B -- System Block Diagram**

Y: 3.8" to 14.0". Full width within margins.

**Flow diagram (left to right):**

Seven component blocks connected by directional arrows:

| Block | X | W | H | Fill | Label | Sub-label |
|---|---|---|---|---|---|---|
| Gas Supply | 0.5" | 3.0" | 3.0" | `#1E2435` | `GAS SUPPLY` | `N2 (bulk liquid) or He (cylinders)` / `20--60 bar (300--870 PSI)` |
| Gas Heater | 4.0" | 3.0" | 3.0" | `#1E2435` | `GAS HEATER` | `Electric resistance` / `200--1100 C` / `Heats GAS, not particles` |
| De Laval Nozzle | 7.5" | 3.5" | 3.0" | `#1E2435` border `#E8A020` | `DE LAVAL NOZZLE` | `Converging-diverging` / `Throat: 2--3 mm` / `Exit: 5--8 mm` |
| Powder Feeder | 7.5" (below nozzle) | 3.5" | 2.0" | `#1E2435` | `POWDER FEEDER` | `High-pressure type` / `Injects against system pressure` |
| Robot | 11.5" | 3.0" | 3.0" | `#1E2435` | `6-AXIS ROBOT` | `Precise standoff control` / `100--500 mm/s traverse` |
| Spray Booth | 15.0" | 4.0" | 3.0" | `#1E2435` | `SPRAY BOOTH` | `Enclosed + HEPA dust collection` |
| Control System | 19.5" | 4.0" | 3.0" | `#1E2435` | `CONTROL SYSTEM` | `Gas pressure + temp` / `Powder feed rate` / `Robot path` |

Block labels: Barlow SemiBold, 16 pt, `#E8A020`.
Sub-labels: JetBrains Mono Regular, 11 pt, `#F0EDE8`.
Arrows: 3 pt `#3A4055` with filled arrowheads.

**Gas flow annotation (above arrow chain):**
- `GAS FLOW: Supply -> Heater -> Nozzle -> Supersonic jet -> Substrate` Inter Medium, 14 pt, `#2EC4B6`

**Powder flow annotation (from feeder to nozzle):**
- `POWDER: Injected into gas stream upstream of or at nozzle` Inter Medium, 13 pt, `#E8A020`

**Key callout below diagram:**
Rounded rect, H: 1.2", fill `#252B3D`, full width.
`The gas heater raises gas VELOCITY (via gas expansion), not particle temperature. Particles enter the nozzle at powder feeder temperature and exit still solid.` Inter Medium, 14 pt, `#E8A020`.

---

### ZONE 3 -- HPCS vs. LPCS

**Section label:** `TWO SYSTEM CLASSES -- HPCS VS. LPCS` -- Y: 14.7".

**BLOCK C -- Two-Column Comparison**

Y: 15.3" to 21.3".

**Left -- High-Pressure Cold Spray (HPCS):**
Rounded rect, X: 0.5", W: 11.0", H: 5.8", fill `#1E2435`, left accent `#2EC4B6`.

Title: `HIGH-PRESSURE COLD SPRAY (HPCS)` Barlow SemiBold, 18 pt, `#2EC4B6`.

| Property | Value |
|---|---|
| Gas pressure | 20--60 bar (300--870 PSI) |
| Gas type | N2 or He |
| Particle velocity | 600--1200 m/s |
| Materials | Cu, Al, Ti, Ni, steel, Inconel, Ta |
| Nozzle material | WC-Co or SiC (wear-resistant) |
| Deposition efficiency | 50--95% (material-dependent) |
| Deposition rate | 1--8 kg/hr |
| Cost class | High (equipment + gas) |

Bottom: `The production workhorse -- handles hard metals that LPCS cannot spray.` Inter Medium, 13 pt, `#2EC4B6`.

**Right -- Low-Pressure Cold Spray (LPCS):**
Rounded rect, X: 12.0", W: 11.5", H: 5.8", fill `#1E2435`, left accent `#E8A020`.

Title: `LOW-PRESSURE COLD SPRAY (LPCS)` Barlow SemiBold, 18 pt, `#E8A020`.

| Property | Value |
|---|---|
| Gas pressure | 5--10 bar (70--150 PSI) |
| Gas type | Air or N2 |
| Particle velocity | 300--600 m/s |
| Materials | Cu, Zn, Sn, Al (soft metals only) |
| Nozzle material | Polymer or steel |
| Deposition efficiency | 30--70% |
| Deposition rate | 0.5--3 kg/hr |
| Cost class | Moderate (simpler equipment) |

Bottom: `Lower cost entry point -- limited to ductile, soft metals. Cannot spray Ti, steel, or Ni.` Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 4 -- Component Details + Nozzle + Gas Selection

**BLOCK D -- Component Detail Cards (2x2 Grid, left side)**

Y: 21.7" to 28.5". X: 0.5", W: 11.0".

| Card | Component | Key Details |
|---|---|---|
| 1 (R1C1) | DE LAVAL NOZZLE | Converging-diverging geometry. Throat diameter 2--3 mm, exit diameter 5--8 mm. Creates supersonic gas flow (Mach 2--4). WC-Co or SiC throat for HPCS (wear from particle erosion). Polymer nozzle acceptable for LPCS. |
| 2 (R1C2) | GAS HEATER | Electric resistance heater. Temperature range 200--1100 C. Purpose: increase gas velocity by thermal expansion -- NOT to melt powder. Higher gas temp = higher gas velocity = higher particle velocity. |
| 3 (R2C1) | POWDER FEEDER | High-pressure type required (must inject AGAINST system pressure of 20--60 bar). Gravimetric preferred for consistency. Feed rate: 2--10 kg/hr (HPCS). |
| 4 (R2C2) | ROBOT / MANIPULATOR | 6-axis industrial robot. Precise standoff control (10--50 mm). Traverse speed 100--500 mm/s. Essential -- no manual cold spray. |

Each card: W: 5.25", H: 3.2", fill `#1E2435`, radius 6, top accent 4 pt `#E8A020`.

**BLOCK F -- Helium vs. Nitrogen (Right side)**

X: 12.0", W: 11.5", Y: 21.7" to 28.5".
Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.

Title: `CARRIER GAS: He VS. N2` Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

| Property | Helium | Nitrogen |
|---|---|---|
| Speed of sound | 1007 m/s | 349 m/s |
| Relative velocity | ~2.6x faster | Baseline |
| Cost | HIGH (10--50x N2) | Low |
| Availability | Cylinders (limited volume) | Bulk liquid (unlimited) |
| Best for | Ti, steel, hard metals | Cu, Al, soft metals |
| Recycling | Systems exist (add complexity) | Not needed (cost negligible) |

Decision rule:
- `Use N2 unless the material DEMANDS helium velocity.` Inter Medium, 14 pt, `#27AE60`
- `Most production applications use N2.` Inter Regular, 13 pt, `#F0EDE8` at 70%
- `He required for: titanium, high-strength steels, refractory metals.` Inter Medium, 13 pt, `#E8A020`

**Stat callout at bottom:**
- `2.6x` Barlow Condensed ExtraBold, 48 pt, `#E8A020`
- `Velocity advantage of He over N2` Inter Medium, 14 pt, `#F0EDE8` at 60%

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Equipment Setup -- Cold Spray System`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Equipment specifications vary by manufacturer and model. Parameter ranges shown are representative of current commercial systems. Consult your equipment manufacturer for system-specific setup procedures.`

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Equipment Setup Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The system schematic (Zone 2) is the hero -- it must clearly show the gas flow path from supply through heater and nozzle to substrate. The de Laval nozzle is the heart of cold spray (it converts pressure to supersonic velocity) and should be visually emphasized. The HPCS vs. LPCS comparison is the key decision framework for anyone evaluating cold spray equipment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #524 -- Construction Workup v1.0*
*2026-04-26*
