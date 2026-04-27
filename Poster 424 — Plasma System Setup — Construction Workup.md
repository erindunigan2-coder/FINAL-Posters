---
Project: Plating Posters Inc
Poster Number: 424
Title: "Plasma System Setup"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Sections 3.1, 3.2)"
Technical Source: PECVD plasma generation systems -- parallel plate (capacitively coupled), ICP, microwave, and pulsed DC. RF at 13.56 MHz is the dominant frequency. System setup includes gas delivery verification, MFC calibration, power supply configuration, and plasma ignition readiness.
Process Scope: PECVD plasma generation hardware, gas delivery, and system preparation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PECVD
  - PlasmaSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #424 -- Construction Workup
## Plasma System Setup

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of the PECVD sequence. This poster covers the hardware side: plasma generation methods, gas delivery infrastructure, and system checks before recipe execution. The distinction between capacitively coupled (parallel plate), inductively coupled (ICP), microwave (ECR), and pulsed DC systems is the core educational content.

Hero visual: four plasma generation types compared side-by-side.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Four plasma types comparison (Block B -- HERO):** Four callout panels showing each plasma generation method with diagram descriptions and key specs.
2. **Gas delivery system (Block C):** Schematic description of MFC-controlled gas delivery from cylinders/bubblers to chamber.
3. **System check protocol (Block D):** Pre-run verification checklist.
4. **RF matching and power delivery (Block E):** Simplified explanation of impedance matching.
5. **Frequency reference (Block F):** Why 13.56 MHz is the standard.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- PLASMA GENERATION TYPES (4.2"--15.5" / ~11.3")
  Block B: Four plasma type comparison panels
ZONE 4 -- GAS DELIVERY + SYSTEM CHECKS (15.5"--24.0" / ~8.5")
  Block C: Gas delivery schematic description
  Block D: Pre-run system check protocol
ZONE 5 -- RF MATCHING + FREQUENCY (24.0"--32.5" / ~8.5")
  Block E: Impedance matching explanation
  Block F: 13.56 MHz reference
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PLASMA SYSTEM SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `PECVD -- Stage 4 of 10 -- Plasma Generation, Gas Delivery, and System Verification` -- 26 pt `#E8A020` (Amber).
**Tagline:** `The plasma is your heat source, your reaction driver, and your film architect. Set it up right or everything downstream fails.` -- 20 pt `#F0EDE8` at 65%.

**Rule Card:**
- Big number: `13.56` -- 60 pt, `#E8A020`
- Label: `MHz` -- JetBrains Mono, 20 pt
- Sub-label: `ISM band RF frequency -- the PECVD standard` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 4 (`Plasma System Setup`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: Chamber at base vacuum  -->  Output: System verified, ready for parameter programming`

---

### ZONE 3 -- Plasma Generation Types

**Section label:** `FOUR WAYS TO MAKE PLASMA` -- Y: 4.4".

**BLOCK B -- Four Plasma Type Panels**

Y: 5.0" to 15.3". Four panels in 2x2 grid.
Each panel: Rounded rect, W: 11.0", H: 4.8", fill `#1E2435`, radius 8, top accent 4 pt.

| Panel | Position | Type | Accent |
|---|---|---|---|
| 1 | X: 0.5", Y: 5.0" | Parallel Plate (CCP) | `#E8A020` |
| 2 | X: 12.0", Y: 5.0" | Inductively Coupled (ICP) | `#2EC4B6` |
| 3 | X: 0.5", Y: 10.3" | Microwave / ECR | `#27AE60` |
| 4 | X: 12.0", Y: 10.3" | Pulsed DC | `#C8D0D8` |

*Panel 1 -- Parallel Plate (CCP):*
- Title: `PARALLEL PLATE (CAPACITIVELY COUPLED)` -- Barlow SemiBold, 18 pt, `#E8A020`
- Badge: `MOST COMMON` -- fill `#E8A020`, text `#1A1F2E`, 12 pt
- Description: `RF power applied between two parallel electrodes. Substrate sits on one electrode. Simple, reliable, proven.`
- Key specs:
```
Frequency: 13.56 MHz
Power: 100--2000 W
Pressure: 50 mTorr -- 5 Torr
Gap: 10--50 mm
Best for: flat substrates, wafers, panels
```
- Limitation: `Limited plasma density; standing wave effects at large electrode sizes`

*Panel 2 -- Inductively Coupled (ICP):*
- Title: `INDUCTIVELY COUPLED PLASMA (ICP)` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Badge: `HIGH DENSITY` -- fill `#2EC4B6`, text `#1A1F2E`
- Description: `RF coil around or above the chamber generates magnetic field that couples energy into plasma. Higher plasma density than CCP.`
- Key specs:
```
Frequency: 13.56 MHz (coil) + bias RF
Power: 200--5000 W
Pressure: 1--50 mTorr
Best for: 3D parts, high-rate deposition
```
- Limitation: `More complex matching; harder to scale for large areas`

*Panel 3 -- Microwave / ECR:*
- Title: `MICROWAVE / ECR (ELECTRON CYCLOTRON RESONANCE)` -- Barlow SemiBold, 16 pt, `#27AE60`
- Badge: `SEMICONDUCTOR FAB` -- fill `#27AE60`, text `#1A1F2E`
- Description: `2.45 GHz microwave energy coupled into chamber, often with magnetic field for ECR condition. Very high ionization efficiency.`
- Key specs:
```
Frequency: 2.45 GHz
Power: 200--3000 W
Pressure: 0.5--10 mTorr
Best for: high-quality films, low damage
```
- Limitation: `Expensive; complex; primarily semiconductor fabs`

*Panel 4 -- Pulsed DC:*
- Title: `PULSED DC` -- Barlow SemiBold, 18 pt, `#C8D0D8`
- Badge: `INDUSTRIAL DLC` -- fill `#C8D0D8`, text `#1A1F2E`
- Description: `DC power pulsed at 50--350 kHz. Compatible with existing PVD vacuum infrastructure. Primary method for industrial DLC coatings on 3D parts.`
- Key specs:
```
Frequency: 50--350 kHz
Voltage: 500--2000 V peak
Pressure: 50--500 mTorr
Best for: DLC on tools, automotive parts
```
- Limitation: `Lower plasma density than RF methods; requires conductive substrates for DC bias`

---

### ZONE 4 -- Gas Delivery + System Checks

**BLOCK C -- Gas Delivery System (Left, X: 0.5", W: 11.0")**

Section label: `GAS DELIVERY INFRASTRUCTURE` -- Y: 15.7".

Flow description (top to bottom):
```
GAS SOURCE
  Cylinders (SiH4, NH3, Ar, N2, C2H2)
  Bubblers (TEOS, HMDSO -- liquid precursors)
       |
  PRESSURE REGULATORS
  (Two-stage; set delivery pressure)
       |
  MASS FLOW CONTROLLERS (MFCs)
  (Electronically controlled; 0--100+ sccm)
  (One MFC per gas line)
       |
  GAS MIXING MANIFOLD
  (Gases combine before entering chamber)
       |
  CHAMBER INLET
  (Showerhead or ring distributor)
```

Key note: `MFC calibration is essential. A 5% drift in SiH4 flow changes film stoichiometry and properties.` -- Inter Medium, 13 pt, `#E8A020`

SiH4 special note: `SiH4 lines: double-contained (coaxial), all-metal VCR fittings, purge manifold at every connection point. No exceptions.` -- Inter Medium, 13 pt, `#E05C5C`

**BLOCK D -- Pre-Run System Check Protocol (Right, X: 12.0", W: 11.5")**

Section label: `PRE-RUN SYSTEM VERIFICATION` -- Y: 15.7".

Checklist (numbered):
```
1. Base vacuum achieved (< 50 mTorr)
2. Leak rate acceptable (< 5 mTorr/min)
3. All MFCs zeroed and responding
4. Gas cylinder pressures verified (not empty)
5. RF generator powered on, reflected power < 5 W
6. Matching network in auto mode
7. Substrate temperature at setpoint (if heated)
8. Exhaust/scrubber/abatement running
9. Safety interlocks green (all doors closed, gas detectors clear)
10. Recipe loaded and parameters confirmed
```

Each item: Inter Regular, 13 pt. Number: Barlow Condensed ExtraBold, 14 pt, `#E8A020`.

---

### ZONE 5 -- RF Matching + Frequency Reference

**BLOCK E -- Impedance Matching (Left, X: 0.5", W: 11.0")**

Section label: `RF IMPEDANCE MATCHING -- DELIVERING POWER TO THE PLASMA` -- Y: 24.2".

Callout panel, fill `#1E2435`, left accent `#E8A020`:

Explanation:
- `The RF generator outputs 50 Ohms. The plasma impedance is complex and variable. A matching network (L-type or pi-type) transforms the plasma impedance to 50 Ohms so power transfers efficiently.`

Key indicators:
```
Forward power: what the generator sends
Reflected power: what bounces back
Target: reflected < 5% of forward
If reflected is high: plasma not igniting,
  or matching network out of range
```

Practical tip: `Most modern systems auto-tune. If reflected power stays high, check: (1) gas is flowing, (2) pressure is in range, (3) matching network capacitors are not at mechanical limit.` -- Inter Medium, 13 pt, `#27AE60`

**BLOCK F -- Why 13.56 MHz (Right, X: 12.0", W: 11.5")**

Section label: `WHY 13.56 MHz?` -- Y: 24.2".

Callout panel, fill `#1E2435`, left accent `#2EC4B6`:

- `13.56 MHz is an ISM (Industrial, Scientific, Medical) band frequency allocated by international radio regulations. Using this frequency means your PECVD system does not interfere with communications and does not require special RF licensing.`

Frequency comparison:

| Frequency | Type | Use |
|---|---|---|
| 50--350 kHz | Pulsed DC | Industrial DLC, hard coatings |
| 13.56 MHz | RF (standard) | Most PECVD systems worldwide |
| 2.45 GHz | Microwave | ECR systems, semiconductor fabs |

Note: `Some advanced PECVD systems use dual-frequency: 13.56 MHz (top electrode) + 400 kHz (bottom electrode) for independent control of plasma density and ion energy.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 6 -- Footer

Standard. Title: `Plasma System Setup`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Plasma System Setup -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The four plasma type panels are the educational core. Most people in plating/finishing know about electrolytic processes but have never seen the inside of a plasma chamber. The 2x2 grid makes the comparison immediate. The RF matching explanation is simplified intentionally -- the audience does not need circuit theory, just "forward vs. reflected power" and what to do when matching fails. The 13.56 MHz callout is a satisfying "why" that sticks with people.

---

*Alaina -- Poster #424 -- Construction Workup v1.0 -- 2026-04-26*
