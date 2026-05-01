---
Project: Plating Posters Inc
Poster Number: 524
Title: "Equipment Setup -- Cold Spray System"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 524 — Equipment Setup Cold Spray System — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ColdSpray
  - ThermalSpray
  - Equipment
  - ClusterTS05
  - v1
---

# Claude Chat Generation Prompt -- Poster #524
## Equipment Setup -- Cold Spray System
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `EQUIPMENT SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Cold Spray System -- High-Pressure Gas, De Laval Nozzle, Solid-State Deposition` -- `30` pt `#E8A020`. Y: **1.5"**.
### Step 3 -- `No arc. No flame. No plasma. Just gas pressure, heat, and a converging-diverging nozzle that turns powder into a supersonic stream.` -- `22` pt at 65%. Y: **2.2"**.

Rule card (right): Big number `7` 72pt `#E8A020`. Label: `core system components`.

---

## Phase 3 -- System Schematic (HERO)

Y: 2.9" to 14.5". Section label: `COLD SPRAY SYSTEM -- COMPONENT LAYOUT`.

Seven component blocks connected by directional arrows (left to right flow):

| Component | Label | Sub-labels |
|---|---|---|
| GAS SUPPLY | `GAS SUPPLY` | N2 (bulk liquid) or He (cylinders); 20--60 bar (300--870 PSI) |
| GAS HEATER | `GAS HEATER` | Electric resistance; 200--1100 C; Heats GAS, not particles |
| DE LAVAL NOZZLE | `DE LAVAL NOZZLE` | Converging-diverging; Throat: 2--3 mm; Exit: 5--8 mm |
| POWDER FEEDER | `POWDER FEEDER` | High-pressure type; injects against system pressure |
| 6-AXIS ROBOT | `6-AXIS ROBOT` | Precise standoff control; 100--500 mm/s traverse |
| SPRAY BOOTH | `SPRAY BOOTH` | Enclosed + HEPA dust collection |
| CONTROL SYSTEM | `CONTROL SYSTEM` | Gas pressure + temp; powder feed rate; robot path |

Block labels: Barlow 600, 16pt, `#E8A020`. Sub-labels: JetBrains Mono 400, 11pt. Nozzle block highlighted with `#E8A020` border. Arrows: 3pt `#3A4055`.

**Gas flow annotation:** `GAS FLOW: Supply -> Heater -> Nozzle -> Supersonic jet -> Substrate` in `#2EC4B6`.
**Powder annotation:** `POWDER: Injected into gas stream upstream of or at nozzle` in `#E8A020`.

**Key callout:** `The gas heater raises gas VELOCITY (via expansion), not particle temperature. Particles enter at powder feeder temperature and exit still solid.` in `#E8A020`.

---

## Phase 4 -- HPCS vs. LPCS

Y: 14.5" to 21.5". Section label: `TWO SYSTEM CLASSES -- HPCS VS. LPCS`.

**Left -- High-Pressure Cold Spray (W: 11.0", accent `#2EC4B6`):**

| Property | Value |
|---|---|
| Gas pressure | 20--60 bar (300--870 PSI) |
| Gas type | N2 or He |
| Particle velocity | 600--1200 m/s |
| Materials | Cu, Al, Ti, Ni, steel, Inconel, Ta |
| Nozzle material | WC-Co or SiC |
| Deposition efficiency | 50--95% |
| Deposition rate | 1--8 kg/hr |
| Cost class | High |

Bottom: `The production workhorse -- handles hard metals that LPCS cannot spray.`

**Right -- Low-Pressure Cold Spray (W: 11.5", accent `#E8A020`):**

| Property | Value |
|---|---|
| Gas pressure | 5--10 bar (70--150 PSI) |
| Gas type | Air or N2 |
| Particle velocity | 300--600 m/s |
| Materials | Cu, Zn, Sn, Al (soft metals only) |
| Nozzle material | Polymer or steel |
| Deposition efficiency | 30--70% |
| Deposition rate | 0.5--3 kg/hr |
| Cost class | Moderate |

Bottom: `Lower cost -- limited to ductile, soft metals. Cannot spray Ti, steel, or Ni.`

---

## Phase 5 -- Component Details + Gas Selection

Y: 21.5" to 32.5".

**Left -- Component Detail Cards (2x2, W: 11.0"):**

| Component | Key Details |
|---|---|
| DE LAVAL NOZZLE | Converging-diverging. Throat 2--3 mm, exit 5--8 mm. Mach 2--4. WC-Co or SiC for HPCS. |
| GAS HEATER | Electric resistance, 200--1100 C. Increases gas velocity by expansion -- NOT to melt powder. |
| POWDER FEEDER | High-pressure type (inject against 20--60 bar). Gravimetric preferred. 2--10 kg/hr (HPCS). |
| ROBOT / MANIPULATOR | 6-axis. Standoff 10--50 mm. Traverse 100--500 mm/s. Essential -- no manual CS. |

Each card: top accent 4pt `#E8A020`.

**Right -- He vs. N2 (W: 11.5", accent `#E8A020`):**

Title: `CARRIER GAS: He VS. N2`.

| Property | Helium | Nitrogen |
|---|---|---|
| Speed of sound | 1007 m/s | 349 m/s |
| Relative velocity | ~2.6x faster | Baseline |
| Cost | HIGH (10--50x N2) | Low |
| Availability | Cylinders (limited) | Bulk liquid (unlimited) |
| Best for | Ti, steel, hard metals | Cu, Al, soft metals |
| Recycling | Systems exist | Not needed |

Decision: `Use N2 unless the material DEMANDS helium velocity.` in `#27AE60`.
`He required for: titanium, high-strength steels, refractory metals.` in `#E8A020`.

Stat: `2.6x` Barlow Condensed 800, 48pt, `#E8A020`. Label: `Velocity advantage of He over N2`.

---

## Phase 6 -- Footer

Standard. Title: `Equipment Setup -- Cold Spray System`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Equipment specifications vary by manufacturer and model. Parameter ranges are representative of current commercial systems. Consult your equipment manufacturer for system-specific setup procedures.`

---

## Phase 7 -- Review

- [ ] Headline `EQUIPMENT SETUP` 80pt
- [ ] 7 rule card
- [ ] 7-block system schematic with gas/powder flow annotations
- [ ] Key callout (heater raises velocity, not particle temp)
- [ ] HPCS vs. LPCS comparison (2 cards, 8 properties each)
- [ ] 4 component detail cards (nozzle, heater, feeder, robot)
- [ ] He vs. N2 comparison table with 2.6x stat
- [ ] Footer with disclaimer and version

---

## Phase 8 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Equipment Setup Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
