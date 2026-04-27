---
Project: Plating Posters Inc
Poster Number: 545
Title: "Parameter Setup -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS parameters overlap with conventional APS but with critical differences -- shorter standoff (40--80 mm vs. 75--150 mm APS), liquid suspension feed replacing carrier gas, higher power to evaporate solvent, faster traverse, and finer step increments. Parameter windows are narrower and less standardized than APS.
Process Scope: SPS parameter setup and process variable control
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Parameters
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #545 -- Construction Workup
## Parameter Setup -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

SPS shares the same plasma gun and gas console as APS, so many parameters are familiar -- but the critical differences are what make or break the coating. Standoff is MUCH closer (40--80 mm vs. 75--150 mm), there is no carrier gas (liquid feed replaces it), power may be bumped to evaporate solvent, and traverse speed is faster because each pass deposits only 2--10 um. This poster is the "what knobs to turn" reference. Hero visual: parameter table with APS comparison column so operators can see exactly where SPS diverges.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PARAMETER TABLE / HERO (2.9"--15.5")
  Block B: Full SPS parameter table with APS comparison column
ZONE 3 -- SUSPENSION FEED PARAMETERS (15.5"--22.0")
  Block C: Suspension-specific variables (solids loading, carrier, flow rate)
  Block D: Injection geometry callout
ZONE 4 -- GAS CONSOLE SETTINGS (22.0"--28.5")
  Block E: Primary/secondary gas flow table
  Block F: "No Carrier Gas" callout (the key SPS difference)
ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5")
  Block G: 4 parameter-related problems with fixes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Suspension Plasma Spray (SPS) -- Process Variables & Control` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Same plasma gun. Different rules. Closer standoff, liquid feed instead of carrier gas, and narrower process windows. Get the parameters right or the columnar structure never forms.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Parameter Table (HERO)

**Section label:** `SPS OPERATING PARAMETERS -- WITH APS COMPARISON` -- Y: 3.1".

**BLOCK B -- Parameter Table**

Y: 3.8" to 15.3". Column widths (23.0" total):
- Parameter (5.5") | SPS Range (5.5") | APS Range (5.0") | Notes (7.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Parameter | SPS Range | APS Range | Notes |
|---|---|---|---|
| Arc current | 400--700 A | 400--800 A | Similar range |
| Arc voltage | 50--80 V | 50--80 V | Gas-dependent |
| Power | 30--60 kW | 25--60 kW | Slightly higher for SPS to evaporate solvent |
| Primary gas (Ar) | 40--60 SLPM | 35--60 SLPM | Similar |
| Secondary gas (H2) | 6--14 SLPM | 5--15 SLPM | Higher H2 increases enthalpy for solvent evaporation |
| Secondary gas (He) | 20--50 SLPM | 20--50 SLPM | Alternative to H2 |
| Suspension flow rate | 20--100 mL/min | N/A (powder) | LIQUID FEED -- no carrier gas |
| Solids loading | 5--30 wt% | N/A | Higher = faster deposition but clogging risk |
| Standoff distance | 40--80 mm | 75--150 mm | MUCH CLOSER -- fine particles decelerate fast |
| Traverse speed | 500--2000 mm/s | 200--1000 mm/s | Faster; thin layers per pass |
| Step increment | 2--4 mm | 3--6 mm | Finer spray footprint |
| Deposition rate | 0.5--3 kg/hr | 2--10 kg/hr | Lower than APS |
| Deposition efficiency | 20--50% | 40--70% | Lower due to overspray and unmolten fines |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

Rows where SPS diverges significantly from APS (standoff, traverse, suspension flow, deposition rate/efficiency): highlight SPS cell background with `#27AE60` at 10%.

---

### ZONE 3 -- Suspension Feed Parameters

**Section label:** `SUSPENSION FEED -- THE CORE SPS VARIABLE` -- Y: 15.7".

**Left -- BLOCK C: Suspension Variables (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `SUSPENSION CHARACTERISTICS` -- Barlow SemiBold 20 pt `#27AE60`.

| Variable | Range | Impact |
|---|---|---|
| Particle size | 50 nm -- 5 um | Finer = more columnar; coarser = denser/lamellar |
| Solids loading | 5--30 wt% | Higher = faster deposition; risk of clogging |
| Carrier liquid | Ethanol or water | Ethanol: better atomization; water: safer handling |
| Flow rate | 20--100 mL/min | Must match plasma enthalpy for full evaporation |
| Shelf life | LIMITED | Sedimentation occurs; agitate before use |

Data: JetBrains Mono 12 pt.

Bottom note: `Ethanol-based suspensions require explosion-proof handling and storage` Inter Medium 13 pt `#E05C5C`.

**Right -- BLOCK D: Injection Geometry (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `INJECTION CONFIGURATION` -- Barlow SemiBold 20 pt `#E8A020`.

Two sub-panels:

*Mechanical Stream Injection:*
- `Continuous liquid stream into plume`
- `Simpler; more common in production`
- `Fragmentation depends on plasma momentum`
- `Radial injection external to nozzle`

*Atomizing Injection:*
- `Pre-atomized spray into plume`
- `Better control of droplet size`
- `More complex; higher gas consumption`
- `Used in R&D and optimization studies`

Note: `Injection point is typically radial (external) -- not through the gun like APS powder` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 4 -- Gas Console Settings

**Section label:** `GAS CONSOLE -- SAME HARDWARE, DIFFERENT LOGIC` -- Y: 22.2".

**Left -- BLOCK E: Gas Flow Settings (X: 0.5", W: 11.0"):**

| Gas | Role in SPS | Flow Rate |
|---|---|---|
| Primary (Ar) | Stabilizes arc; plasma forming | 40--60 SLPM |
| Secondary (H2) | Increases enthalpy for solvent evaporation | 6--14 SLPM |
| Secondary (He) | Alternative to H2; gentler heating | 20--50 SLPM |
| Carrier (Ar) | NOT USED IN SPS | -- |

Data: JetBrains Mono Regular 12 pt.

"NOT USED IN SPS" row highlighted in `#E8A020` background at 15%.

**Right -- BLOCK F: No Carrier Gas Callout (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06", H: 5.0".

Title: `THE KEY DIFFERENCE` -- Barlow SemiBold 22 pt `#27AE60`.

Body (Inter Regular 16 pt `#F0EDE8`, line height 160%):

```
In conventional APS, carrier gas (Ar) delivers
dry powder to the plasma plume.

In SPS, the LIQUID SUSPENSION replaces the
carrier gas entirely. The suspension is
injected as a stream or spray -- the plasma
evaporates the solvent and melts the particles.

This eliminates the powder feeder and carrier
gas line. The suspension feed system is the
replacement.
```

`No powder feeder. No carrier gas. Liquid in, coating out.` JetBrains Mono 14 pt `#27AE60`.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `PARAMETER PROBLEMS -- 4 COMMON ISSUES` -- Y: 28.7".

**BLOCK G -- Four Problem Cards**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | LAMELLAR INSTEAD OF COLUMNAR | Standoff too far; particles too large | Reduce standoff to 40--60 mm; verify particle size < 5 um |
| 2 | 6.33" | LOW DEPOSITION RATE | Solids loading too low; flow rate insufficient | Increase solids loading (target 15--25 wt%); increase flow rate |
| 3 | 12.16" | INJECTOR CLOGGING | Sedimentation; high solids loading; aged suspension | Agitate before use; reduce loading; check shelf life |
| 4 | 18.0" | SUBSTRATE OVERHEATING | Standoff too close; insufficient cooling; traverse too slow | Increase cooling air; increase traverse speed; monitor temp < 400 degC |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard. Title: `Parameter Setup -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

Disclaimer: `SPS parameters are less standardized than conventional APS. Ranges shown are representative of current research and early-production practice. Consult your coating supplier and equipment OEM for application-specific settings.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Parameter Setup SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #545 -- Construction Workup v1.0 -- 2026-04-26*
