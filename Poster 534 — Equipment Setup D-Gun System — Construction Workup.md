---
Project: Plating Posters Inc
Poster Number: 534
Title: "Equipment Setup -- D-Gun System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun system components including water-cooled detonation barrel (25--50 mm bore, 1--2 m length), gas metering system (O2 + C2H2), powder injection, spark ignition, nitrogen purge, water cooling, 6-axis robot, sound-isolated booth, and remote control system. Originally proprietary to Union Carbide / Praxair Surface Technologies. Major providers: Oerlikon Metco (LCNTEC), Praxair.
Process Scope: D-Gun -- equipment setup and system components
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - EquipmentSetup
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #534 -- Construction Workup
## Equipment Setup -- D-Gun System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Equipment setup poster for D-Gun. Hero element: the detonation barrel system diagram showing the cycle sequence -- gas fill, powder inject, ignite, detonate, purge, repeat. The D-Gun barrel is the heart of the system: a water-cooled steel tube where precisely metered charges of acetylene and oxygen are detonated 1--15 times per second. This poster also highlights the proprietary nature of D-Gun technology -- this is NOT off-the-shelf equipment.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **System component diagram (Block B -- HERO):** 9-component breakdown of the D-Gun system.
2. **Detonation cycle sequence (Block C):** 5-step cycle: Gas Fill -> Powder Inject -> Ignite -> Detonate -> N2 Purge -> Repeat.
3. **Barrel specifications callout (Block D):** Dimensions, cooling, bore size, and barrel maintenance.
4. **"Proprietary Technology" callout (Block E):** Amber callout on the Union Carbide / Praxair history and limited availability.
5. **System pre-checks strip (Block F):** Pre-operation verification checklist.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SYSTEM COMPONENTS + DETONATION CYCLE (2.9"--14.0" / ~11.1")
  Block B: 9-component system breakdown
  Block C: Detonation cycle sequence
ZONE 3 -- BARREL SPECS + PROPRIETARY CALLOUT (14.0"--22.0" / ~8.0")
  Block D: Barrel specifications
  Block E: "Proprietary Technology" callout
ZONE 4 -- PRE-OPERATION CHECKLIST + OEM REFERENCE (22.0"--32.5" / ~10.5")
  Block F: System pre-checks
  Block G: OEM providers
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `EQUIPMENT SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun System -- Controlled Detonation in a Water-Cooled Barrel` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Acetylene-oxygen detonation. Spark ignition. Nitrogen purge. A precisely engineered explosion -- repeated up to 15 times per second.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- System Components + Detonation Cycle

**Section label:** `D-GUN SYSTEM COMPONENTS` -- Y: 3.1".

**BLOCK B -- 9-Component Breakdown (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 13.0". Nine component cards vertically stacked.

Each card: W: 14.0", H: 0.95", fill `#1E2435`, radius 6, left accent 4 pt.

| # | Component | Accent | Details |
|---|---|---|---|
| 1 | DETONATION BARREL | `#E8A020` | Water-cooled steel tube; 25--50 mm bore; 1--2 m length; the heart of the system |
| 2 | GAS METERING SYSTEM | `#E8A020` | Precise volumetric metering of O2 and C2H2 for each detonation cycle |
| 3 | POWDER INJECTION | `#2EC4B6` | Metered charge of powder (0.5--3 g) injected after gas fill, before ignition |
| 4 | IGNITION SYSTEM | `#E05C5C` | Spark plug or pilot flame; initiates detonation wave |
| 5 | NITROGEN PURGE | `#2EC4B6` | Clears barrel between cycles; prevents premature detonation of next charge; 1--3x barrel volume |
| 6 | WATER COOLING | `#27AE60` | Barrel cooling system; high flow rate; barrel must remain below distortion temperature |
| 7 | ROBOT / MANIPULATOR | `#C8D0D8` | Precision 6-axis; critical for consistent standoff and traverse; programmed path |
| 8 | SOUND-ISOLATED BOOTH | `#E05C5C` | Mandatory; 130--150 dB noise requires massive acoustic isolation panels and sealed doors |
| 9 | REMOTE CONTROL SYSTEM | `#C8D0D8` | Full parameter monitoring and control from outside booth; camera feeds; emergency stop |

Component number badge: Rounded rect, W: 0.5", H: 0.35", fill accent color. Text: `1` etc., Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`.
Component name: Barlow SemiBold, 15 pt, `#F0EDE8`.
Details: Inter Regular, 12 pt, `#F0EDE8` at 80%.

**BLOCK C -- Detonation Cycle Sequence (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 13.0". Vertical flow showing one complete detonation cycle.

Title: `ONE DETONATION CYCLE` Barlow Condensed ExtraBold, 22 pt, `#E8A020`.
Subtitle: `Repeats 1--15 times per second` Inter Medium, 14 pt, `#F0EDE8`.

Five cycle step cards connected by downward arrows, with a return arrow from Step 5 back to Step 1.

Each step card: W: 7.5", H: 1.3", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Title | Duration |
|---|---|---|---|
| 1 | `#2EC4B6` | GAS FILL | O2 + C2H2 metered into barrel (~milliseconds) |
| 2 | `#E8A020` | POWDER INJECT | 0.5--3 g powder charge injected after gas |
| 3 | `#E05C5C` | IGNITE | Spark plug fires; detonation wave initiates |
| 4 | `#E05C5C` | DETONATE | Wave travels ~3500 m/s down barrel; particles accelerate to 750--1000 m/s; 25 mm spot deposited |
| 5 | `#27AE60` | N2 PURGE | Nitrogen flushes barrel (1--3x volume); clears combustion products; prevents premature next-cycle ignition |

Arrows: 2 pt, `#3A4055`, downward. Return arrow (Step 5 to Step 1): dashed, `#E8A020`, with label `REPEAT` JetBrains Mono, 12 pt, `#E8A020`.

Stat below cycle: `67--1000 ms per cycle` JetBrains Mono Bold, 18 pt, `#E8A020`.

---

### ZONE 3 -- Barrel Specs + Proprietary Callout

**Left -- Barrel Specifications (X: 0.5", W: 12.0")**

Section label: `DETONATION BARREL SPECIFICATIONS` Y: 14.2".

**BLOCK D -- Barrel Spec Table**

Y: 14.8" to 19.5".

Header row: `#3A4055`. Columns: Parameter (4.0") | Specification (4.0") | Notes (4.0")

| Parameter | Specification | Notes |
|---|---|---|
| Barrel material | High-strength steel | Must withstand repeated detonation pressures |
| Bore diameter | 25--50 mm | Determines spot size and gas volume |
| Barrel length | 1--2 m | Longer barrel = higher particle velocity |
| Cooling | Water-cooled jacket | High flow rate; continuous during operation |
| Bore condition | Polished, no scoring | Scoring causes turbulence; degrades coating quality |
| Service life | Manufacturer-specified | Barrel is a wear item; inspect per maintenance schedule |
| Burst disc | Installed on barrel | Safety relief; prevents catastrophic over-pressure |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`.

**Barrel maintenance callout (below, Y: 19.8" to 21.5"):**
Rounded rect, W: 11.5", H: 1.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

`BARREL INSPECTION IS CRITICAL. A scored, worn, or damaged barrel produces inconsistent coatings and poses a safety risk. Inspect bore condition per manufacturer schedule. Replace immediately if scoring, pitting, or dimensional wear exceeds tolerance.` Inter Medium, 13 pt, `#E05C5C`, center.

**Right -- "Proprietary Technology" Callout (X: 13.0", W: 10.5")**

Section label: `TECHNOLOGY HISTORY` Y: 14.2".

**BLOCK E -- Proprietary Technology Callout**

Y: 14.8" to 21.5". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.

Title: `PROPRIETARY ORIGINS` Barlow Condensed ExtraBold, 24 pt, `#E8A020`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
D-Gun technology was developed and
patented by Union Carbide Corporation
in the 1950s.

The technology remained proprietary
for decades -- only Union Carbide
(later Praxair Surface Technologies)
operated D-Gun systems commercially.

Today, generic D-Gun and "super D-Gun"
systems exist, but the technology
remains semi-proprietary:

  - NOT off-the-shelf equipment
  - Limited number of manufacturers
  - Significant capital investment
  - Specialized operator training required
  - Process know-how is closely held
```

Major providers:
```
Oerlikon Metco    LCNTEC Detonation Spray
Praxair / Linde   Original D-Gun licensee
```
JetBrains Mono Regular, 13 pt. Company names in `#E8A020`.

`This is premium technology for premium applications. D-Gun shops are specialists, not general-purpose coaters.` Inter Medium, 12 pt, `#E8A020`.

---

### ZONE 4 -- Pre-Operation Checklist + OEM Reference

**Left -- Pre-Operation Checklist (X: 0.5", W: 14.0")**

Section label: `PRE-OPERATION VERIFICATION CHECKLIST` Y: 22.2".

**BLOCK F -- Checklist Cards**

Y: 22.8" to 32.0". Ten checklist items in two columns.

Each item: W: 6.7", H: 0.85", fill `#1E2435`, radius 4, left accent 3 pt.

| # | Check Item | Accent |
|---|---|---|
| 1 | Water cooling flow confirmed; barrel temperature stable | `#27AE60` |
| 2 | O2 and C2H2 supply pressures verified; regulators set | `#E8A020` |
| 3 | N2 purge supply confirmed; purge volume verified | `#2EC4B6` |
| 4 | Barrel bore inspected; no scoring or damage | `#E05C5C` |
| 5 | Powder feeder loaded; charge weight calibrated (0.5--3 g) | `#E8A020` |
| 6 | Spark plug / ignition system tested | `#E05C5C` |
| 7 | Robot program loaded and verified; standoff confirmed (100--200 mm) | `#C8D0D8` |
| 8 | Sound booth sealed; doors locked; no personnel inside | `#E05C5C` |
| 9 | Camera monitoring active; remote control console powered | `#C8D0D8` |
| 10 | Emergency stop accessible and tested | `#E05C5C` |

Column 1 (items 1--5): X: 0.5". Column 2 (items 6--10): X: 7.5".
Check number: Barlow Condensed ExtraBold, 14 pt, accent color.
Check item: Inter Regular, 12 pt, `#F0EDE8`.

**Right -- System Comparison (X: 15.0", W: 8.5")**

Section label: `D-GUN vs. OTHER THERMAL SPRAY SYSTEMS` Y: 22.2".

**BLOCK G -- Quick Comparison**

Y: 22.8" to 32.0". Comparison table.

| Attribute | D-Gun | HVOF | Plasma |
|---|---|---|---|
| Energy source | Detonation | Combustion | Electric arc |
| Operation | Pulsed | Continuous | Continuous |
| Noise | 130--150 dB | 110--130 dB | 100--130 dB |
| Remote operation | Mandatory | Optional | Optional |
| Capital cost | Very high | High | High |
| Off-the-shelf | No | Yes | Yes |
| Throughput | Low (1--5 kg/hr) | Med (2--10 kg/hr) | Med (2--10 kg/hr) |
| Coating density | Highest | Very high | High |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. D-Gun column values in `#E8A020`. "Mandatory" and "No" in `#E05C5C`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Equipment Setup -- D-Gun System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Equipment Setup D-Gun System -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The detonation cycle sequence is the intellectual centerpiece of this poster. The 5-step cycle (fill, inject, ignite, detonate, purge) with the return arrow creates a visual loop that communicates the repetitive nature of D-Gun operation. The barrel specification table grounds the abstract detonation concept in physical hardware. The proprietary technology callout is important context -- operators encountering D-Gun for the first time need to understand this is specialized, premium equipment with a specific industrial pedigree.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #534 -- Construction Workup v1.0*
*2026-04-26*
