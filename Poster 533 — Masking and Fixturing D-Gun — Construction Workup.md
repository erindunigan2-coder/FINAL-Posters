---
Project: Plating Posters Inc
Poster Number: 533
Title: "Masking and Fixturing -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun masking requires metal masks mandatory (detonation impact is extremely energetic). Custom-machined stainless steel or Inconel masks. Precision-balanced rotation fixtures. Full robotic gun manipulation -- no manual D-Gun spraying. Parts are typically small to medium (turbine blades, vanes, seals, bushings). Cooling air between detonation cycles.
Process Scope: D-Gun -- masking, fixturing, and part handling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - Masking
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #533 -- Construction Workup
## Masking and Fixturing -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Masking and fixturing poster for D-Gun. Hero message: metal masks are mandatory -- the detonation impact is so energetic that tape, silicone, and soft masking materials are destroyed instantly. Custom-machined stainless steel or Inconel masks designed for each specific part geometry. Secondary story: precision-balanced rotation fixtures are critical because the pulsed detonation loading creates vibration that can shift poorly balanced parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Masking material requirements (Block B -- HERO):** Why metal masks are mandatory -- the detonation energy rationale.
2. **"No Manual Spraying" callout (Block C):** Coral callout -- full robotic operation for all D-Gun work.
3. **Fixture design guide (Block D):** Requirements for D-Gun fixtures -- balance, vibration isolation, cooling.
4. **Typical part gallery (Block E):** 4 cards showing typical D-Gun parts and their masking/fixturing challenges.
5. **Common masking failures strip (Block F):** Defects from inadequate masking.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- MASKING REQUIREMENTS + ROBOTIC CALLOUT (2.9"--14.0" / ~11.1")
  Block B: Masking material comparison
  Block C: "No Manual Spraying" callout
ZONE 3 -- FIXTURE DESIGN GUIDE (14.0"--22.0" / ~8.0")
  Block D: Fixture requirements for D-Gun
ZONE 4 -- TYPICAL PARTS + COMMON FAILURES (22.0"--32.5" / ~10.5")
  Block E: 4 part cards
  Block F: Common masking failures
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `MASKING & FIXTURING` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Metal Masks Mandatory, Robotic Operation Only` -- 32 pt `#C8D0D8` (Silver). Y: 1.5".
**Tagline:** `Controlled detonation demands engineered masking. No tape. No silicone. Custom-machined metal masks for every part geometry.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Masking Requirements + Robotic Callout

**Section label:** `MASKING MATERIAL REQUIREMENTS` -- Y: 3.1".

**BLOCK B -- Masking Comparison Table (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 11.0". Full data table.

Header row: `#3A4055`. Columns: Masking Type (3.5") | D-Gun Compatible? (3.0") | Reason (8.0")

| Masking Type | D-Gun Compatible? | Reason |
|---|---|---|
| Custom-machined stainless steel | YES -- STANDARD | Withstands detonation impact; reusable; precision-cut to part geometry |
| Custom-machined Inconel | YES -- PREMIUM | Superior heat and impact resistance; for highest-energy configurations |
| Mild steel masks | ACCEPTABLE | Lower cost; shorter service life; may deform after repeated impacts |
| High-temperature masking tape | NO | Destroyed by detonation impact; tape debris contaminates coating |
| Silicone plugs / caps | NO | Shattered or displaced by detonation energy; debris contamination |
| Ceramic fiber tape | NO | Fragments under impact; fiber contamination risk |
| Liquid peelable maskant | NO | Cannot withstand detonation forces; peels away exposing substrate |

"YES" in `#27AE60` bold. "ACCEPTABLE" in `#E8A020`. "NO" in `#E05C5C` bold.
Data: Inter Regular, 13 pt, `#F0EDE8`. Masking type: Inter Medium, 13 pt.

**Energy rationale callout (below table, Y: 11.3" to 13.5"):**
Rounded rect, W: 14.0", H: 2.0", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

Title: `WHY METAL MASKS?` Barlow SemiBold, 18 pt, `#E8A020`.
Body: `D-Gun particles impact at 750--1000 m/s with detonation-level kinetic energy. Soft masking materials (tape, silicone, peelable coatings) cannot absorb this energy -- they are physically destroyed, and their debris becomes contaminant inclusions in the coating. Metal masks absorb impact energy through elastic deformation and can be reused hundreds of times.` Inter Regular, 13 pt, `#F0EDE8`.

**BLOCK C -- "No Manual Spraying" Callout (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 10.0". Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8.

Title: `ROBOTIC OPERATION` Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.
Subtitle: `MANDATORY` Barlow Condensed ExtraBold, 24 pt, `#E05C5C`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
D-Gun is NEVER operated manually.

Reasons:
1. Noise: 130--150 dB (eardrum rupture)
2. Blast overpressure risk
3. Precision: 25 mm spot requires
   exact standoff and traverse
4. Speed: 1--15 Hz cycle rate demands
   programmed robotic path

All D-Gun spraying is performed by:
  - 6-axis industrial robot
  - Programmed traverse pattern
  - Remote operator outside booth
  - Camera monitoring
```

`Manual D-Gun spraying does not exist in any specification.` Inter Medium, 13 pt, `#E05C5C`.

**Cooling note (below, Y: 10.5" to 13.5"):**
Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Title: `COOLING BETWEEN CYCLES` Barlow SemiBold, 16 pt, `#2EC4B6`.
Body: `Cooling air nozzles must be directed at the substrate between detonation cycles. Although D-Gun heat input is intermittent (pulsed), cumulative thermal buildup can exceed substrate temperature limits at high cycle frequencies. Monitor substrate temperature with IR pyrometer. Cool fixture and backside of part.` Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Fixture Design Guide

**Section label:** `FIXTURE DESIGN REQUIREMENTS` -- Y: 14.2".

**BLOCK D -- Fixture Requirements (Full width)**

Y: 14.8" to 21.5". Six requirement cards in 2 columns x 3 rows.

Each card: W: 11.0", H: 2.0", fill `#1E2435`, radius 6, left accent 4 pt.

| Requirement | Accent | Details |
|---|---|---|
| PRECISION BALANCE | `#E8A020` | Rotation fixtures must be dynamically balanced. Pulsed detonation loading at 1--15 Hz creates cyclical forces. Imbalance causes vibration, part shift, and inconsistent standoff. |
| VIBRATION ISOLATION | `#E05C5C` | Mount fixtures on vibration-isolating pads or spring mounts. Detonation pulses transmit through fixture into booth structure. Isolate to prevent resonance. |
| LINE-OF-SIGHT ACCESS | `#27AE60` | Fixture must not shadow any spray zone. D-Gun spot is only 25 mm diameter -- even small obstructions block coverage. Design fixtures with clear access for robotic arm travel. |
| ROTATION SPEED CONTROL | `#2EC4B6` | Variable speed rotation for cylindrical parts. Synchronize rotation speed with detonation frequency and robot traverse to achieve uniform overlapping spot coverage. |
| SUBSTRATE TEMPERATURE MONITORING | `#E8A020` | IR pyrometer aimed at substrate. Thermocouple backup for critical parts. Interlock to pause spray if temperature exceeds substrate limit. |
| ELECTRICAL GROUNDING | `#C8D0D8` | Ground fixture to workpiece for electrostatic discharge prevention. Metal mask must be electrically bonded to fixture ground. |

Column 1: X: 0.5". Column 2: X: 12.0". Gap: 0.5" vertical between rows.
Requirement: Barlow SemiBold, 16 pt, accent color.
Details: Inter Regular, 12 pt, `#F0EDE8`.

---

### ZONE 4 -- Typical Parts + Common Failures

**Left -- Typical D-Gun Parts (X: 0.5", W: 11.5")**

Section label: `TYPICAL D-GUN PARTS` Y: 22.2".

**BLOCK E -- 4 Part Cards (2x2)**

Y: 22.8" to 31.0". Each card: W: 5.5", H: 3.8", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | Part Type | Accent | Masking Challenge | Typical Coating |
|---|---|---|---|---|
| 1 (R1C1) | TURBINE BLADES | `#E8A020` | Complex airfoil geometry; mask root and tip; leave blade platform exposed for coating | WC-Co or CrC-NiCr; 150--300 um |
| 2 (R1C2) | COMPRESSOR SEALS | `#2EC4B6` | Annular geometry; mask ID and edges; coat OD wear surface only | Al2O3-TiO2 or Cr2O3; 100--250 um |
| 3 (R2C1) | PUMP SHAFTS | `#27AE60` | Cylindrical; mask keyways, threads, and bearing journals; coat wear zones | WC-CoCr; 150--400 um |
| 4 (R2C2) | VALVE SEATS | `#C8D0D8` | Small contact area; mask surrounding surfaces; coat only seating surface | Stellite or WC-Co; 75--200 um |

Part Type: Barlow SemiBold, 16 pt, accent color.
Masking Challenge: Inter Regular, 12 pt, `#F0EDE8`.
Typical Coating: JetBrains Mono Regular, 12 pt, accent color.

**Right -- Common Masking Failures (X: 12.5", W: 11.0")**

Section label: `COMMON MASKING FAILURES` Y: 22.2".

**BLOCK F -- Failure Cards (stacked)**

Y: 22.8" to 32.0". Five failure cards.

| Failure | Color | Cause | Result |
|---|---|---|---|
| MASK EROSION / BREAKTHROUGH | `#E05C5C` | Mask too thin or wrong material; exceeded service life | Coating on non-spray areas; requires stripping and recoating |
| MASK SHIFT DURING SPRAY | `#E05C5C` | Poor clamping; vibration from detonation pulses | Edge definition lost; coating overlap onto masked areas |
| OVERSPRAY BENEATH MASK | `#E8A020` | Gap between mask and substrate surface | Thin, poorly bonded coating under mask edge; requires rework |
| THERMAL DISTORTION OF MASK | `#E8A020` | Cumulative heat from detonation cycles; insufficient cooling | Mask warps, changing gap and coverage; replace mask |
| DEBRIS CONTAMINATION | `#E05C5C` | Soft masking material used (tape, silicone); mask fragments in coating | Coating rejection; inclusions visible in cross-section |

Each card: H: 1.7", fill `#1E2435`, left accent failure color.
Failure: Barlow SemiBold, 14 pt, failure color.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Result: Inter Medium, 12 pt, `#E05C5C`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Masking and Fixturing -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Masking and Fixturing D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The masking story for D-Gun is uniquely extreme: the detonation energy literally destroys soft masking. This makes the "NO" column in the masking comparison table dramatic and memorable. The "No Manual Spraying" callout in coral reinforces the safety poster's remote operation message and is equally relevant here -- you cannot fixture and mask for manual D-Gun because it does not exist. The typical parts gallery grounds the abstract fixturing requirements in real components that operators will recognize.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #533 -- Construction Workup v1.0*
*2026-04-26*
