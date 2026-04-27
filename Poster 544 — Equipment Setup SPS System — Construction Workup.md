---
Project: Plating Posters Inc
Poster Number: 544
Title: "Equipment Setup -- SPS System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS system = modified APS system with specialized suspension feed. Same plasma guns (F4-MB, SinplexPro), power supply, gas console, robot, booth, cooling. Adds pressurized suspension vessel or peristaltic pump (20--100 mL/min), suspension injector (mechanical stream or atomizing), and suspension preparation equipment (ball/bead milling).
Process Scope: SPS equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Equipment
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #544 -- Construction Workup
## Equipment Setup -- SPS System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

SPS is a modified APS system -- the plasma gun, power supply, gas console, robot, and booth are the same. The key addition is the suspension feed system: pressurized vessel or peristaltic pump, specialized injector, and suspension preparation equipment. This poster should clearly show "what's the same as APS" and "what's new for SPS." Hero visual: system component diagram with SPS-specific additions highlighted.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SYSTEM COMPONENTS / HERO (2.9"--15.5")
  Block B: Numbered component list with APS-inherited vs. SPS-specific tagging
ZONE 3 -- SUSPENSION FEED SYSTEM DETAIL (15.5"--22.0")
  Block C: Feed system types (pressurized vs. peristaltic)
  Block D: Suspension preparation requirements
ZONE 4 -- PLASMA GUN + GAS CONSOLE (22.0"--28.5")
  Block E: Gun specifications (shared with APS)
  Block F: Gas console parameters
ZONE 5 -- OEM SYSTEMS + INFRASTRUCTURE (28.5"--32.5")
  Block G: Major OEM systems with SPS capability
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `SPS System -- Modified APS with Specialized Suspension Feed` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Same plasma gun. Same robot. Same booth. The difference is what you feed it -- liquid suspension instead of dry powder. That one change transforms the microstructure.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- System Components

**Section label:** `SPS SYSTEM COMPONENTS` -- Y: 3.1".

**BLOCK B -- Component List**

8 components in two columns. Each component card: rounded rect, W: 11.0", H: 2.5", fill `#1E2435`.

Tag system: `APS STANDARD` badge in `#3A4055` for inherited components; `SPS-SPECIFIC` badge in `#27AE60` for new additions.

| # | Component | Tag | Key Specs |
|---|---|---|---|
| 1 | Plasma Gun | APS STANDARD | Cathode (thoriated W), anode (OFC Cu), gas ring, injector port |
| 2 | Power Supply | APS STANDARD | 40--80 kW DC; 400--800 A at 50--80 V |
| 3 | Gas Console | APS STANDARD | Mass flow controllers: primary Ar/N2, secondary H2/He/N2 |
| 4 | Suspension Feed System | SPS-SPECIFIC | Pressurized vessel or peristaltic pump; 20--100 mL/min |
| 5 | Suspension Injector | SPS-SPECIFIC | Mechanical (stream) or atomizing (spray); radial injection into plume |
| 6 | Robot / Manipulator | APS STANDARD | 6-axis industrial robot; precise standoff control |
| 7 | Cooling System | APS STANDARD | Closed-loop water cooling; 15--25 L/min at 15--20 degC |
| 8 | Spray Booth | APS STANDARD* | Enclosed with HEPA dust collection; *must be explosion-proof for ethanol SPS |

Note: Item 8 has asterisk -- `*Booth must be rated for flammable vapor if using ethanol-based suspension` in `#E05C5C`.

---

### ZONE 3 -- Suspension Feed System Detail

**Section label:** `THE SPS DIFFERENCE -- SUSPENSION FEED SYSTEM` -- Y: 15.7".

**Left -- BLOCK C: Feed System Types (X: 0.5", W: 11.0"):**

Two sub-panels:

*Pressurized Vessel:*
- `Sealed vessel pressurized to 2--10 bar`
- `Consistent flow rate under pressure`
- `Requires agitation to prevent sedimentation`
- `Simpler; preferred for production`

*Peristaltic Pump:*
- `Positive displacement pump`
- `Pulsed flow (may need dampener)`
- `Easier to vary flow rate`
- `Better for R&D / small batches`

**Right -- BLOCK D: Suspension Preparation (X: 12.0", W: 11.5"):**

- `Particle size in suspension: 50 nm -- 5 um` JetBrains Mono 16 pt `#27AE60`
- `Solids loading: 5--30 wt%`
- `Carrier: ethanol (better atomization) or water (safer)`
- `Preparation: ball milling or bead milling for homogeneous dispersion`
- `Shelf life: LIMITED -- sedimentation occurs; agitate before use`
- `Ethanol suspensions require explosion-proof handling and storage`

---

### ZONE 4 -- Plasma Gun + Gas Console

**Section label:** `PLASMA GUN & GAS CONSOLE (SHARED WITH APS)` -- Y: 22.2".

**Left -- BLOCK E: Gun Specs (X: 0.5", W: 11.0"):**

| Component | Specification |
|---|---|
| Cathode | 2% thoriated tungsten |
| Anode | Oxygen-free copper |
| Arc current | 400--700 A |
| Arc voltage | 50--80 V |
| Power | 30--60 kW (slightly higher than APS to evaporate solvent) |
| Cooling | 15--25 L/min water at 15--20 degC |

Note: `SPS may use modified nozzle optimized for suspension injection` Inter Medium 13 pt `#E8A020`.

**Right -- BLOCK F: Gas Console (X: 12.0", W: 11.5"):**

| Gas | Role | Flow Rate |
|---|---|---|
| Primary (Ar) | Stabilizes arc; plasma forming | 40--60 SLPM |
| Secondary (H2) | Increases enthalpy for solvent evaporation | 6--14 SLPM |
| Secondary (He) | Alternative to H2; less aggressive | 20--50 SLPM |
| Carrier (Ar) | N/A for SPS (liquid feed replaces carrier gas) | -- |

Note: `SPS eliminates the powder carrier gas -- suspension is injected as liquid` `#27AE60`.

---

### ZONE 5 -- OEM Systems + Infrastructure

**Section label:** `SYSTEMS WITH SPS CAPABILITY` -- Y: 28.7".

| OEM | System | Notes |
|---|---|---|
| Oerlikon Metco | SinplexPro with SPS option | Cascaded arc; high stability |
| Progressive Surface | Custom SPS integration | North American |
| Northwest Mettech | Axial III with suspension feed | Axial injection -- unique |

Infrastructure note: `SPS capability is typically added to an existing APS installation -- not a standalone purchase. Budget for suspension feed system, explosion-proof booth upgrades (if ethanol), and suspension preparation equipment.` Inter Medium 14 pt `#E8A020`.

---

### ZONE 6 -- Footer

Standard. Title: `Equipment Setup -- SPS System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #544 -- Construction Workup v1.0 -- 2026-04-26*
