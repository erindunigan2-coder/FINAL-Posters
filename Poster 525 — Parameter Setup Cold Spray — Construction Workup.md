---
Project: Plating Posters Inc
Poster Number: 525
Title: "Parameter Setup -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray operating parameters for HPCS and LPCS systems. Critical velocity concept. Gas pressure, temperature, powder feed rate, standoff, and traverse speed.
Process Scope: Cold spray -- parameter setup and operating windows
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - Parameters
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #525 -- Construction Workup
## Parameter Setup -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Parameter poster for Cold Spray. The hero concept is "critical velocity" -- the material-specific minimum particle velocity required for bonding. Below critical velocity, particles bounce off. Above it, they bond via adiabatic shear instability. Everything in cold spray parameter setup is about achieving and exceeding this threshold.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **HPCS vs. LPCS parameter table (Block B -- HERO):** Side-by-side operating windows.
2. **Critical velocity concept (Block C):** Visual showing the velocity threshold -- below = bounce, above = bond.
3. **Material-specific velocity requirements (Block D):** Table showing critical velocities for common cold spray materials.
4. **Parameter interaction diagram (Block E):** How gas pressure, gas temperature, and powder size interact to determine particle velocity.
5. **Deposition efficiency by material (Block F):** Quick reference for DE expectations.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PARAMETER TABLE HERO (2.9"--14.0" / ~11.1")
  Block B: HPCS vs. LPCS parameter comparison
  Block C: Critical velocity concept callout
ZONE 3 -- MATERIAL VELOCITY REQUIREMENTS (14.0"--22.0" / ~8.0")
  Block D: Material-specific critical velocities
ZONE 4 -- PARAMETER INTERACTIONS + DE (22.0"--32.5" / ~10.5")
  Block E: Parameter interaction diagram
  Block F: Deposition efficiency by material
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Achieving Critical Velocity` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Every parameter serves one goal: accelerate particles past the critical velocity threshold. Below it, they bounce. Above it, they bond.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Parameter Table Hero

**Section label:** `OPERATING PARAMETERS -- HPCS VS. LPCS` -- Y: 3.1".

**BLOCK B -- Dual Parameter Table**

Y: 3.8" to 10.5". Full width.

Header row: `#3A4055`. Columns: Parameter (4.5") | HPCS (5.5") | LPCS (5.5") | Notes (7.5")

| Parameter | High-Pressure CS | Low-Pressure CS | Notes |
|---|---|---|---|
| Gas type | N2 or He | Air or N2 | He for hard metals only (cost) |
| Gas pressure | 20--60 bar (300--870 PSI) | 5--10 bar (70--150 PSI) | Primary velocity driver |
| Gas temperature | 300--1100 C | 200--600 C | Heats GAS, not particles |
| Particle velocity | 600--1200 m/s | 300--600 m/s | Must exceed critical velocity |
| Powder feed rate | 2--10 kg/hr | 1--5 kg/hr | Higher = faster buildup |
| Powder size | 5--50 um | 5--50 um | Finer powder = higher velocity |
| Standoff distance | 10--50 mm | 10--30 mm | VERY close vs. other TS |
| Spray angle | 75--90 deg | 75--90 deg | Perpendicular preferred |
| Traverse speed | 100--500 mm/s | 100--500 mm/s | Robot-controlled |
| Nozzle type | WC-Co or SiC | Polymer or steel | Wear-resistant for HPCS |
| Deposition efficiency | 50--95% | 30--70% | Material-dependent |
| Deposition rate | 1--8 kg/hr | 0.5--3 kg/hr | Lower than HVOF |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.
"Primary velocity driver" and similar notes: `#E8A020`.

**BLOCK C -- Critical Velocity Concept (below table)**

Y: 11.0" to 13.8". Rounded rect, full width, H: 2.6", fill `#1E2435`, radius 8, left accent 4 pt `#E05C5C`.

Title: `THE CRITICAL VELOCITY THRESHOLD` Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**Horizontal velocity gauge:**
- Bar, X: 2.0", W: 20.0", H: 0.6"
- Red zone left (0--400 m/s): `#E05C5C` at 40%, label `BOUNCE` Barlow SemiBold 14 pt `#E05C5C`
- Transition zone (400--600 m/s): gradient `#E05C5C` to `#E8A020`
- Green zone right (600--1200 m/s): `#27AE60` at 40%, label `BOND` Barlow SemiBold 14 pt `#27AE60`
- Critical velocity marker: triangle at ~500--600 m/s zone, label `Vc (critical)` JetBrains Mono 12 pt `#E8A020`

Explanation: `Below Vc: particles rebound elastically -- no deposition. Above Vc: adiabatic shear instability breaks oxide films, creates metallurgical bond via solid-state welding. Every cold spray parameter is tuned to exceed Vc for the specific feedstock material.` Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Material Velocity Requirements

**Section label:** `CRITICAL VELOCITY BY MATERIAL` -- Y: 14.2".

**BLOCK D -- Material Table**

Y: 14.8" to 21.8". Full width.

Header row: `#3A4055`. Columns: Material (4.0") | Critical Velocity (4.0") | Typical Spray Velocity (4.5") | System Required (4.0") | Deposition Efficiency (6.5")

| Material | Critical Velocity (approx.) | Typical Spray Velocity | System | DE |
|---|---|---|---|---|
| Copper (Cu) | 300--400 m/s | 500--800 m/s | HPCS (N2) or LPCS | 80--95% (highest) |
| Aluminum (Al) | 350--450 m/s | 500--900 m/s | HPCS (N2) or LPCS | 70--90% |
| Zinc (Zn) | 250--350 m/s | 400--600 m/s | LPCS adequate | 70--85% |
| Tin (Sn) | 200--300 m/s | 300--500 m/s | LPCS adequate | 75--90% |
| Nickel (Ni) | 500--600 m/s | 700--1000 m/s | HPCS (N2 or He) | 50--70% |
| Titanium (Ti-6Al-4V) | 600--750 m/s | 800--1200 m/s | HPCS (He preferred) | 50--70% |
| Stainless steel (316L) | 550--700 m/s | 700--1000 m/s | HPCS (N2 or He) | 40--60% |
| Silver (Ag) | 300--400 m/s | 500--700 m/s | HPCS (N2) or LPCS | 75--90% |
| Inconel 625 | 600--800 m/s | 800--1200 m/s | HPCS (He recommended) | 40--60% |
| Tantalum (Ta) | 600--800 m/s | 900--1200 m/s | HPCS (He required) | 30--50% |

Critical velocity column: JetBrains Mono 13 pt, `#E05C5C`.
Spray velocity column: JetBrains Mono 13 pt, `#27AE60`.
"He preferred" / "He required" annotations: `#E8A020`.

Callout: `Softer, more ductile metals have lower critical velocities -- easier to cold spray. Hard metals (Ti, steel, Inconel) require HPCS with helium.` Inter Medium, 14 pt, `#2EC4B6`.

---

### ZONE 4 -- Parameter Interactions + Deposition Efficiency

**Left -- Parameter Interaction Diagram (X: 0.5", W: 11.0")**

Section label: `PARAMETER INTERACTIONS` Y: 22.2".

Y: 22.8" to 30.0". Rounded rect, fill `#1E2435`, radius 8.

**Three primary levers (vertical stack with arrows showing "increase" effect):**

| Lever | Increase Effect | Symbol |
|---|---|---|
| GAS PRESSURE | Higher particle velocity; higher DE | Up arrow `#27AE60` |
| GAS TEMPERATURE | Higher gas velocity (expansion); higher particle velocity | Up arrow `#27AE60` |
| POWDER SIZE (smaller) | Higher particle velocity (less mass to accelerate) | Up arrow `#27AE60` |

**Three secondary effects:**

| Factor | Effect |
|---|---|
| Standoff too close (< 10 mm) | Bow shock decelerates particles; REDUCED velocity at impact |
| Standoff too far (> 50 mm) | Particles decelerate in ambient air |
| Spray angle < 75 deg | Reduced normal component of velocity; porosity increases |

Warning callout: `There is a "bow shock" effect at very close standoff -- the gas decelerates before the substrate surface. Optimal standoff is 15--30 mm for most HPCS applications.` Inter Medium, 13 pt, `#E8A020`.

**Right -- Deposition Efficiency Summary (X: 12.0", W: 11.5")**

Section label: `DEPOSITION EFFICIENCY` Y: 22.2".

Y: 22.8" to 30.0". Rounded rect, fill `#1E2435`, radius 8.

**Horizontal bar chart:**

| Material | DE Range | Bar Color |
|---|---|---|
| Cu | 80--95% | `#27AE60` (nearly full) |
| Al | 70--90% | `#27AE60` |
| Zn, Sn, Ag | 70--90% | `#27AE60` |
| Ni | 50--70% | `#E8A020` |
| Ti | 50--70% | `#E8A020` |
| Steel | 40--60% | `#E8A020` |
| Inconel | 40--60% | `#E8A020` |
| Ta | 30--50% | `#E05C5C` |

Note: `DE is highly dependent on particle velocity relative to critical velocity. The further above Vc, the higher the DE. Copper achieves the highest DE because its critical velocity is low and it is highly ductile.` Inter Regular, 13 pt, `#F0EDE8` at 70%.

**Verdic banner (spanning full width, Y: 30.5" to 32.0"):**
Rounded rect, X: 0.5", W: 23.0", H: 1.3", fill `#E8A020` at 15%, border 1 pt `#E8A020`, radius 999.

`Copper is the benchmark cold spray material -- highest deposition efficiency, lowest critical velocity, near-bulk properties in the deposit.` Inter Medium, 14 pt, `#E8A020`, center.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Parameter Setup -- Cold Spray`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Critical velocity values are approximate and depend on powder morphology, size distribution, and oxide content. Actual parameters must be validated for each material-substrate combination. Consult your equipment manufacturer and application specification.`

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The critical velocity concept is the single most important idea in cold spray parameter setup. The horizontal velocity gauge (Zone 2) should be the most visually memorable element -- BOUNCE on the left in coral, BOND on the right in emerald, with the critical velocity threshold clearly marked. The material table (Zone 3) gives every operator the answer to "can I cold spray this material?" at a glance.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #525 -- Construction Workup v1.0*
*2026-04-26*
