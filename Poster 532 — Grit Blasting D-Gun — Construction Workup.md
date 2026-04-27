---
Project: Plating Posters Inc
Poster Number: 532
Title: "Grit Blasting -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun grit blasting parameters. White alumina (99.5%+ purity), 36--60 mesh, 40--60 PSI, Ra 3--6 um, SSPC-SP 5 (White Metal). Profile requirements similar to HVOF -- extremely high particle velocity provides excellent mechanical interlocking even on moderate profiles.
Process Scope: D-Gun -- grit blasting and surface preparation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - GritBlasting
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #532 -- Construction Workup
## Grit Blasting -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Grit blasting poster for D-Gun. Hero message: D-Gun's extreme particle velocity (750--1000 m/s) means the process is less dependent on surface profile than lower-velocity methods. A moderate profile of Ra 3--6 um is sufficient because the detonation impact energy provides its own mechanical interlocking. High-purity white alumina (99.5%+) is mandatory for aerospace substrates.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast parameter table (Block B -- HERO):** Key specifications for D-Gun grit blasting.
2. **"Moderate Profile Sufficient" callout (Block C):** Explaining why D-Gun needs less profile than flame or arc spray.
3. **Media selection guide (Block D):** Why white alumina, why 99.5%+ purity, and what to avoid.
4. **Profile verification methods (Block E):** Testex tape, profilometer, visual standards.
5. **Common blasting defects strip (Block F):** Over-blasting, under-blasting, contamination.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- BLAST PARAMETERS + PROFILE CALLOUT (2.9"--14.0" / ~11.1")
  Block B: Blast parameter table
  Block C: "Moderate Profile Sufficient" callout
ZONE 3 -- MEDIA SELECTION GUIDE (14.0"--22.0" / ~8.0")
  Block D: Media selection table + purity rationale
ZONE 4 -- PROFILE VERIFICATION + DEFECTS (22.0"--32.5" / ~10.5")
  Block E: Verification methods
  Block F: Common blasting defects
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `GRIT BLASTING` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Surface Activation for Detonation-Grade Coatings` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `White alumina. Moderate profile. Extreme velocity does the rest -- D-Gun particles hit so hard that surface texture is a partner, not a crutch.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Blast Parameters + Profile Callout

**Section label:** `GRIT BLAST SPECIFICATION` -- Y: 3.1".

**BLOCK B -- Blast Parameter Table (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 10.0". Full data table.

Header row: `#3A4055`. Columns: Parameter (4.0") | Specification (5.0") | Notes (5.5")

| Parameter | Specification | Notes |
|---|---|---|
| Media | White alumina (Al2O3), 99.5%+ purity | Aerospace standard; no ferrous contamination |
| Grit size | 36--60 mesh | Finer than flame/arc spray; matched to moderate profile target |
| Blast pressure | 40--60 PSI (275--415 kPa) | Moderate; high-velocity D-Gun impact compensates |
| Nozzle distance | 100--200 mm (4--8 inches) | Consistent distance for uniform profile |
| Blast angle | 60--90 degrees to surface | Perpendicular preferred for maximum profile depth |
| Anchor profile (Ra) | 3--6 um (125--250 microinches) | Moderate profile sufficient for D-Gun bonding |
| Surface cleanliness | SSPC-SP 5 (White Metal) / ISO 8501 Sa 3 | No visible contaminants, mill scale, or prior coatings |
| Time to spray | < 4 hours (< 2 hours for some specs) | Blasted surface degrades with time and humidity |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

**BLOCK C -- "Moderate Profile Sufficient" Callout (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 10.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.
Emerald-tinted glass.

Title: `MODERATE PROFILE` Barlow Condensed ExtraBold, 24 pt, `#27AE60`.
Subtitle: `Why D-Gun Needs Less` Barlow SemiBold, 16 pt, `#F0EDE8`.

Profile comparison (JetBrains Mono Regular, 14 pt, line height 180%):
```
D-Gun:        Ra 3--6 um
HVOF:         Ra 3--8 um
Plasma Spray: Ra 3--8 um
Flame Spray:  Ra 4--12 um
Arc Spray:    Ra 4--12 um
```
D-Gun value in `#27AE60`. Flame/Arc values in `#E8A020`. Others in `#F0EDE8` at 60%.

Body (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
Lower-velocity processes (flame, arc)
rely heavily on mechanical interlocking
from rough profiles.

D-Gun particles impact at 750--1000 m/s
with enormous kinetic energy. This energy
drives particles INTO the surface,
creating its own interlocking -- even
on moderate profiles.

Rougher is NOT better for D-Gun.
Over-blasting embeds grit and creates
stress concentrations.
```

**Profile comparison callout (below, Y: 10.5" to 13.5"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Title: `PARTICLE VELOCITY vs. PROFILE DEPENDENCE` Barlow SemiBold, 16 pt, `#E8A020`.

Visual concept -- two-column comparison:

| Process | Velocity | Profile Dependence |
|---|---|---|
| Flame Spray | 40--200 m/s | HIGH -- needs rough profile |
| Arc Spray | 50--200 m/s | HIGH -- needs rough profile |
| Plasma Spray | 200--600 m/s | MODERATE |
| HVOF | 600--900 m/s | LOW--MODERATE |
| D-Gun | 750--1000 m/s | LOW -- moderate profile sufficient |
| Cold Spray | 600--1200 m/s | LOW -- some apps skip blast entirely |

Data: JetBrains Mono, 12 pt. "HIGH" in `#E05C5C`. "MODERATE" in `#E8A020`. "LOW" in `#27AE60`.

---

### ZONE 3 -- Media Selection Guide

**Section label:** `BLAST MEDIA SELECTION -- WHY WHITE ALUMINA` -- Y: 14.2".

**BLOCK D -- Media Selection Table (Full width)**

Y: 14.8" to 19.5".

Header row: `#3A4055`. Columns: Media (4.0") | Hardness (Mohs) (2.5") | Grit Size (2.5") | D-Gun Use? (3.0") | Reason (11.0")

| Media | Hardness | Grit Size | D-Gun Use? | Reason |
|---|---|---|---|---|
| White alumina (Al2O3) 99.5%+ | 9 | 36--60 mesh | YES -- STANDARD | No ferrous contamination; self-sharpening; aerospace approved |
| Brown alumina (Al2O3) | 9 | 36--60 mesh | ACCEPTABLE | Lower purity; OK for non-aerospace; cost advantage |
| Silicon carbide | 9.5 | 36--60 mesh | SPECIALTY | Harder substrates (Ti); more aggressive; higher cost |
| Angular steel grit | 7--8 | G25--G40 | NO | Ferrous contamination risk on Ni/Ti substrates; galvanic corrosion |
| Garnet | 7--8 | 36--80 mesh | NO | Insufficient hardness; inconsistent profile |
| Glass bead | 5--6 | Various | NO | Produces peened (smooth) surface, not angular profile |

"YES" in `#27AE60` bold. "ACCEPTABLE" in `#E8A020`. "NO" in `#E05C5C` bold. "SPECIALTY" in `#2EC4B6`.

**Purity callout (below table, Y: 19.8" to 21.5"):**
Rounded rect, full width, H: 1.5", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

`99.5%+ PURITY REQUIREMENT: Standard brown alumina contains iron oxide impurities (Fe2O3) that can transfer to substrate surfaces. On nickel-alloy and titanium turbine components, iron contamination creates galvanic corrosion initiation sites. White alumina is calcined to remove iron -- this is not a cost preference, it is a corrosion prevention requirement.` Inter Medium, 13 pt, `#E05C5C`, center.

---

### ZONE 4 -- Profile Verification + Defects

**Left -- Profile Verification (X: 0.5", W: 11.5")**

Section label: `PROFILE VERIFICATION METHODS` Y: 22.2".

**BLOCK E -- Verification Cards**

Y: 22.8" to 30.5". Three method cards stacked.

Each card: W: 11.0", H: 2.2", fill `#1E2435`, radius 6, left accent 4 pt.

| Method | Accent | How It Works | When to Use |
|---|---|---|---|
| TESTEX REPLICA TAPE | `#2EC4B6` | Press-o-film tape is pressed into surface profile; measure compressed tape thickness with spring micrometer; subtract tape backing thickness | Field method; quick; widely accepted per ASTM D4417 Method C |
| SURFACE PROFILOMETER | `#E8A020` | Stylus traces across surface; measures Ra (arithmetic average) and Rz (peak-to-valley); digital readout | Lab or shop; most accurate; provides Ra and Rz values for specification |
| VISUAL COMPARATOR | `#C8D0D8` | Compare blasted surface to reference standards (SSPC-VIS 1); trained eye assessment | Quick go/no-go check; supplement with quantitative method |

Method: Barlow SemiBold, 16 pt, accent color.
How It Works: Inter Regular, 12 pt, `#F0EDE8`.
When to Use: Inter Medium, 12 pt, accent color.

**Ra target reminder (below, Y: 30.8" to 32.0"):**
Stat: `Ra 3--6 um` Barlow Condensed ExtraBold, 36 pt, `#E8A020`.
Label: `D-Gun target profile range` Inter Medium, 14 pt, `#F0EDE8`.

**Right -- Common Blasting Defects (X: 12.5", W: 11.0")**

Section label: `COMMON BLASTING DEFECTS` Y: 22.2".

**BLOCK F -- Defect Cards (stacked)**

Y: 22.8" to 32.0". Five defect cards.

| Defect | Color | Cause | Impact on D-Gun Coating |
|---|---|---|---|
| OVER-BLASTING (Ra too high) | `#E05C5C` | Excessive pressure, time, or coarse media | Stress concentrations at profile peaks; embedded grit; coating cracks at peaks |
| UNDER-BLASTING (Ra too low) | `#E8A020` | Insufficient pressure, time, or worn media | Inadequate anchor profile; reduced bond strength |
| EMBEDDED GRIT | `#E05C5C` | Excessive pressure; holding nozzle too close; steel grit on soft substrate | Inclusion at interface; galvanic corrosion site; adhesion failure point |
| NON-UNIFORM PROFILE | `#E8A020` | Inconsistent nozzle distance or angle; worn nozzle | Thickness variation in coating; localized adhesion differences |
| SURFACE OXIDATION AFTER BLAST | `#E05C5C` | Excessive time between blast and spray; high humidity | Oxide film at interface; reduced bond strength |

Each card: H: 1.7", fill `#1E2435`, left accent defect color.
Defect: Barlow SemiBold, 14 pt, defect color.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Impact: Inter Medium, 12 pt, `#E05C5C`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Grit Blasting -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Grit Blasting D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The key insight for this poster is the inverse relationship between particle velocity and profile dependence. Higher velocity processes need less surface roughness because the kinetic energy of impact creates its own interlocking. The velocity-vs-profile comparison table in Zone 2 is the intellectual anchor. The white alumina purity requirement is the critical "do not skip" message -- using the wrong blast media on aerospace components creates corrosion sites that may not be detected until service. The "over-blasting" defect deserves prominent coral treatment because it is counterintuitive: more is not better for D-Gun grit blasting.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #532 -- Construction Workup v1.0*
*2026-04-26*
