---
Project: Plating Posters Inc
Poster Number: 530
Title: "Safety and PPE -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun safety hazards including extreme noise (130--150 dB, loudest thermal spray process), blast/overpressure risk, combustible gas handling (O2/C2H2), cobalt and chromium fumes, thermal hazards, and mandatory remote operation from sound-isolated booth.
Process Scope: D-Gun -- safety hazards and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - Safety
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #530 -- Construction Workup
## Safety and PPE -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Safety poster for D-Gun. The dominant hazard is NOISE -- 130--150 dB from detonation pulses makes D-Gun the loudest thermal spray process by a wide margin. The hero message is mandatory remote operation: no human should be inside the spray booth during D-Gun operation. This poster leads with the noise hazard and the "REMOTE OPERATION MANDATORY" callout, then covers the full hazard matrix.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard matrix table (Block B -- HERO):** 7-row hazard table with controls -- the reference anchor.
2. **"Remote Operation Mandatory" callout (Block C):** Coral callout -- the single most important safety message.
3. **Noise comparison chart (Block D):** D-Gun noise level compared to other thermal spray processes and common reference points.
4. **TLV/PEL reference (Block E):** Exposure limits for cobalt, chromium, and nickel fumes.
5. **PPE checklist strip (Block F):** Visual PPE requirements for booth setup and monitoring roles.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- HAZARD MATRIX + REMOTE OP CALLOUT (2.9"--14.0" / ~11.1")
  Block B: 7-row hazard table
  Block C: "Remote Operation Mandatory" callout
ZONE 3 -- NOISE COMPARISON + TLV/PEL (14.0"--22.0" / ~8.0")
  Block D: Noise level comparison
  Block E: TLV/PEL table
ZONE 4 -- PPE CHECKLIST + EMERGENCY PROCEDURES (22.0"--32.5" / ~10.5")
  Block F: PPE checklist
  Block G: Emergency response strip
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- The Loudest Process in Thermal Spray` -- 32 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `130--150 dB detonation pulses. Mandatory remote operation. No human in the spray booth during firing.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Hazard Matrix + Remote Operation Callout

**Section label:** `HAZARD IDENTIFICATION MATRIX` -- Y: 3.1".

**BLOCK B -- Hazard Table (Left, X: 0.5", W: 15.5")**

Y: 3.8" to 13.0". Full data table.

Header row: `#3A4055`. Columns: Hazard (3.0") | Details (5.0") | Controls (4.5") | Severity (3.0")

| Hazard | Details | Controls | Severity |
|---|---|---|---|
| NOISE | 130--150 dB (detonation pulses); loudest thermal spray process | Mandatory double hearing protection (NRR 30+); sound-isolated spray booth; remote operation | EXTREME |
| BLAST / OVERPRESSURE | Repeated detonation waves; risk of barrel failure | Barrel inspection schedule; burst disc protection; never operate with damaged barrel | HIGH |
| COMBUSTIBLE GAS | Oxygen + acetylene in detonable mixtures | Gas handling per NFPA/OSHA; flashback arrestors; leak detection; proper storage | HIGH |
| METAL FUMES | Cobalt, nickel, chromium from WC-Co and alloy powders | Local exhaust ventilation (LEV); HEPA filtration; RPE with P100 minimum | HIGH |
| THERMAL | Hot barrel (water-cooled but still hot); hot substrate and fixtures | Heat-resistant PPE; never touch barrel during or after operation; cooling verification | MODERATE |
| UV/IR RADIATION | Moderate detonation flash | Shade 5--8 eye protection; no exposed skin near booth windows | MODERATE |
| VIBRATION | Pulsed operation transmits vibration to fixtures and surrounding structure | Vibration-isolating mounts; structural assessment of booth mounting | MODERATE |

Data: Inter Regular, 12 pt, `#F0EDE8`. Hazard names: Barlow SemiBold, 13 pt. Severity badges:
- EXTREME: fill `#E05C5C`, text `#1A1F2E`
- HIGH: fill `#E8A020`, text `#1A1F2E`
- MODERATE: fill `#C8D0D8`, text `#1A1F2E`

Badges: rounded rect, W: 2.5", H: 0.3", Barlow Condensed ExtraBold, 11 pt.

**BLOCK C -- "Remote Operation Mandatory" Callout (Right, X: 16.5", W: 7.0")**

Y: 3.8" to 10.0". Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8.

Title: `REMOTE OPERATION` Barlow Condensed ExtraBold, 32 pt, `#E05C5C`.
Subtitle: `MANDATORY` Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
NO human should be inside the
spray booth during D-Gun operation.

The operator controls the gun via:
  - Robotic manipulator (6-axis)
  - Remote control console
  - Camera monitoring system

The booth provides:
  - Acoustic isolation (130--150 dB)
  - Blast containment
  - Fume extraction
  - Overspray containment
```

Bottom stat: `150 dB` Barlow Condensed ExtraBold, 48 pt, `#E05C5C`.
Label: `= threshold of eardrum rupture` Inter Medium, 14 pt, `#F0EDE8`.

**Gas safety note (below, Y: 10.5" to 13.0"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Title: `ACETYLENE SAFETY` Barlow SemiBold, 16 pt, `#E8A020`.
Body: `Acetylene is unstable above 15 PSI gauge pressure. D-Gun systems use acetylene at controlled low pressure in precisely metered volumes. Flashback arrestors are mandatory on all gas lines. Never operate D-Gun systems with gas leaks -- acetylene-oxygen mixtures are detonable across a wide concentration range.` Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Noise Comparison + TLV/PEL

**Left -- Noise Comparison (X: 0.5", W: 12.0")**

Section label: `NOISE LEVEL COMPARISON` Y: 14.2".

**BLOCK D -- Noise Chart**

Y: 14.8" to 21.0". Horizontal bar chart format using rectangles.

| Source | dB Level | Bar Width (proportional) | Color |
|---|---|---|---|
| D-Gun | 130--150 dB | Full width | `#E05C5C` |
| Plasma Spray | 100--130 dB | ~85% | `#E8A020` |
| HVOF | 110--130 dB | ~85% | `#E8A020` |
| Cold Spray | 110--130 dB | ~85% | `#E8A020` |
| Arc Spray | 95--115 dB | ~72% | `#2EC4B6` |
| Flame Spray | 85--105 dB | ~63% | `#27AE60` |
| Conversation | 60 dB | ~40% | `#C8D0D8` |
| Pain threshold | 125 dB | Reference line | `#E05C5C` dashed |
| Eardrum rupture | 150 dB | Reference line | `#E05C5C` solid |

Each bar: H: 0.55", fill at stated color, radius 4. Label left-aligned inside bar: Inter Medium, 12 pt. dB value right-aligned: JetBrains Mono, 13 pt.

Reference lines: dashed/solid horizontal lines with labels on right.

`OSHA permissible exposure: 90 dB (8-hr TWA). At 130 dB, exposure limit is < 1 second.` Inter Medium, 12 pt, `#E05C5C`.

**Right -- TLV/PEL Reference (X: 13.0", W: 10.5")**

Section label: `EXPOSURE LIMITS -- KEY FUME HAZARDS` Y: 14.2".

**BLOCK E -- TLV/PEL Table**

Y: 14.8" to 21.0".

Header row: `#3A4055`. Columns: Substance (3.0") | OSHA PEL (3.5") | ACGIH TLV (4.0")

| Substance | OSHA PEL (TWA) | ACGIH TLV (TWA) |
|---|---|---|
| Cobalt (as Co) | 0.1 mg/m3 | 0.02 mg/m3 |
| Chromium (as Cr metal) | 1.0 mg/m3 | 0.5 mg/m3 |
| Nickel (metal dust) | 1.0 mg/m3 | 1.5 mg/m3 |
| Tungsten (as W) | -- | 5 mg/m3 (insoluble) |
| Tungsten carbide (WC) | 15 mg/m3 (total dust) | 5 mg/m3 (inhalable) |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Substance names: Inter Medium, 13 pt.

Cobalt warning callout (below table):
Rounded rect, H: 0.8", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

`COBALT is the primary inhalation hazard when spraying WC-Co. ACGIH TLV of 0.02 mg/m3 is extremely low. Continuous air monitoring is recommended during D-Gun WC-Co spraying.` Inter Medium, 13 pt, `#E05C5C`, center.

---

### ZONE 4 -- PPE Checklist + Emergency Procedures

**Left -- PPE Checklist (X: 0.5", W: 12.0")**

Section label: `PPE REQUIREMENTS BY ROLE` Y: 22.2".

**BLOCK F -- PPE Cards (2 cards side by side)**

Y: 22.8" to 31.5".

**Card 1 -- Booth Setup / Maintenance (X: 0.5", W: 5.7")**
Rounded rect, fill `#1E2435`, radius 6, top accent 4 pt `#E8A020`.

Title: `BOOTH SETUP / MAINTENANCE` Barlow SemiBold, 16 pt, `#E8A020`.

Checklist (Inter Regular, 13 pt, `#F0EDE8`, line height 170%):
```
[x] Double hearing protection (NRR 30+)
[x] Shade 5--8 safety glasses
[x] Heat-resistant gloves
[x] Leather apron or flame-resistant coat
[x] Steel-toed boots
[x] P100 half-mask respirator (fume residue)
[x] Face shield (barrel inspection)
```

Note: `Equipment is OFF during booth entry. LOTO required.` Inter Medium, 12 pt, `#E05C5C`.

**Card 2 -- Remote Operator (X: 6.5", W: 5.7")**
Rounded rect, fill `#1E2435`, radius 6, top accent 4 pt `#2EC4B6`.

Title: `REMOTE OPERATOR` Barlow SemiBold, 16 pt, `#2EC4B6`.

Checklist:
```
[x] Hearing protection (booth may transmit noise)
[x] Safety glasses
[x] Standard work clothing
[x] Access to emergency stop
[x] Camera monitoring active
[x] Communication system with booth area
```

Note: `Operator remains OUTSIDE booth at all times during firing.` Inter Medium, 12 pt, `#2EC4B6`.

**Right -- Emergency Procedures (X: 13.0", W: 10.5")**

Section label: `EMERGENCY RESPONSE` Y: 22.2".

**BLOCK G -- Emergency Cards (stacked)**

Y: 22.8" to 32.0". Four emergency cards.

| Emergency | Color | Response |
|---|---|---|
| GAS LEAK (O2 or C2H2) | `#E05C5C` | Emergency stop. Evacuate. Ventilate. No ignition sources. Do not re-enter until gas-free verified. |
| BARREL FAILURE | `#E05C5C` | Emergency stop. Do not enter booth. Allow cooling. Inspect for structural damage before clearing. |
| FIRE IN BOOTH | `#E8A020` | Emergency stop. Activate fire suppression. Do not open booth doors (oxygen feed). Call fire response. |
| FUME OVEREXPOSURE | `#E8A020` | Remove to fresh air. Seek medical attention. Report cobalt symptoms: cough, wheeze, difficulty breathing. |

Each card: H: 2.1", fill `#1E2435`, left accent emergency color, radius 6.
Emergency: Barlow SemiBold, 16 pt, emergency color.
Response: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Safety and PPE -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety and PPE D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most safety-critical poster in the thermal spray series. The noise hazard is genuinely exceptional -- 150 dB can rupture eardrums. The "Remote Operation Mandatory" callout must be the first thing a viewer reads after the headline. The coral color treatment on the callout and the 150 dB stat number should be viscerally attention-grabbing. The noise comparison chart provides immediate context by stacking D-Gun against all other thermal spray processes and common reference points. The cobalt TLV callout is the secondary critical message -- 0.02 mg/m3 is an exceptionally low exposure limit.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #530 -- Construction Workup v1.0*
*2026-04-26*
