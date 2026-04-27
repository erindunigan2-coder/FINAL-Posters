---
Project: Plating Posters Inc
Poster Number: 456
Title: "Implantation Process"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.5, 6.8)"
Process Scope: The active implantation step -- beam scanning, dose delivery, and real-time monitoring
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - ImplantationProcess
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #456 -- Construction Workup
## Implantation Process

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the active treatment poster -- what happens while ions are being driven into the substrate. The beam scans across the surface, the Faraday system integrates dose in real time, and the substrate temperature is monitored. The hero visual shows the beam scanning pattern across a wafer (or part). Below that, real-time monitoring parameters that operators watch, and the physics of what happens inside the substrate lattice when an energetic ion arrives (collision cascade, lattice damage, final resting position). This is where the atomic-level modification happens.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Beam scanning pattern hero (Block B):** Top-down view of beam scanning across substrate surface.
2. **Collision cascade visualization (Block D):** What happens inside the lattice when an ion arrives.
3. **Real-time monitoring panel (Block E):** Parameters operators watch during implantation.
4. **Process timing reference (Block F):** How long different implant types take.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- BEAM SCANNING HERO (2.9"--14.5" / ~11.6")
  Block B: Top-down scan pattern + dose integration concept
ZONE 3 -- COLLISION CASCADE (14.5"--20.5" / ~6.0")
  Block D: What happens at the atomic level
ZONE 4 -- REAL-TIME MONITORING (20.5"--26.5" / ~6.0")
  Block E: What operators watch during implantation
ZONE 5 -- PROCESS TIMING REFERENCE (26.5"--32.5" / ~6.0")
  Block F: Implant duration by application type
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `IMPLANTATION` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Active Beam Delivery & Dose Integration` -- 36 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Right now, 10^15 ions per second are slamming into this surface at 100 km/s. Each one buries itself in the lattice, displacing substrate atoms along the way. This is precision violence at the atomic scale.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Beam Scanning Hero

**Section label:** `BEAM SCANNING -- UNIFORM DOSE DELIVERY` -- Y: 3.1".

**BLOCK B -- Scan Pattern Visualization**

Y: 3.8" to 14.3".

**Left -- Scan Pattern Top View (X: 0.5", W: 12.0"):**
- Rounded rect container, H: 10.0", fill `#1E2435`
- Title: `TOP VIEW -- BEAM SCAN ACROSS WAFER` Barlow SemiBold 18 pt `#27AE60`. Y: 4.2".

Wafer/substrate representation (Y: 5.0" to 12.0"):
- Large circle (wafer) or rounded rect (industrial part): stroke 2 pt `#C8D0D8`, fill none, radius ~3.0"
- Label: `300 mm WAFER` or `SUBSTRATE SURFACE` JetBrains Mono 12 pt `#C8D0D8`
- Horizontal scan lines (raster pattern): 10--15 parallel horizontal lines, stroke 1 pt `#27AE60` at 40%
- Beam spot: Small filled circle, 0.2" radius, fill `#27AE60`, at one position on a scan line
- Label: `BEAM SPOT (~1--30 mm diameter)` JetBrains Mono 10 pt `#27AE60`
- Arrow showing X-scan direction: Horizontal, stroke 2 pt `#E8A020`
- Label: `X-SCAN (electrostatic, 100--1000 Hz)` JetBrains Mono 10 pt `#E8A020`
- Arrow showing Y-scan direction: Vertical, stroke 2 pt `#2EC4B6`
- Label: `Y-SCAN (mechanical translation or electrostatic)` JetBrains Mono 10 pt `#2EC4B6`

**Right -- Dose Integration Concept (X: 13.0", W: 10.5"):**
- Rounded rect container, H: 10.0", fill `#1E2435`
- Title: `FARADAY DOSE INTEGRATION` Barlow SemiBold 18 pt `#E8A020`. Y: 4.2".

Dose equation and explanation (Y: 5.0" to 8.5"):

```
DOSE EQUATION:

Dose (ions/cm2) = Q / (q x A)

Where:
  Q = Total charge collected by Faraday (Coulombs)
  q = Charge per ion (1.6 x 10^-19 C for singly charged)
  A = Implanted area (cm2)

In practice:
  Q = Beam current (A) x Time (s)
  Dose integrator counts in real time
  Implant stops automatically when target dose reached
```

JetBrains Mono 13 pt `#F0EDE8`. Key terms: `#E8A020`.

Accuracy callout (Y: 9.0" to 10.5"):
- Rounded rect, fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Semiconductor dose accuracy: +/- 1--2% across wafer. +/- 1--3% wafer-to-wafer. This is one of the most precisely controlled parameters in all of manufacturing.` -- Inter Medium, 13 pt, `#E8A020`.

Scan uniformity note (Y: 11.0" to 12.5"):
- Text: `The scan system overlaps beam passes to ensure every point on the surface receives the same total dose. Think of it like mowing a lawn -- overlap each pass, and the grass height (dose) is uniform.` -- Inter Regular, 13 pt, `#F0EDE8` at 70%.

---

### ZONE 3 -- Collision Cascade

**Section label:** `INSIDE THE LATTICE -- THE COLLISION CASCADE` -- Y: 14.7".

**BLOCK D -- Atomic-Level Explanation**

Y: 15.3" to 20.3". Three cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | THE INCOMING ION | `#27AE60` | A single N+ ion at 100 keV enters the substrate surface at ~600 km/s. It collides with substrate atoms (nuclear stopping) and with electrons (electronic stopping). Each nuclear collision displaces a substrate atom from its lattice site, creating a vacancy-interstitial pair (Frenkel pair). |
| 2 | 8.16" | 7.33" | THE CASCADE | `#E8A020` | Each displaced substrate atom may have enough energy to displace additional atoms -- creating a cascade of collisions. A single 100 keV N+ ion in steel produces ~1,000 displaced atoms along its path before coming to rest at depth Rp. The damage zone extends ~2x wider than Rp. |
| 3 | 15.83" | 7.33" | THE FINAL STATE | `#2EC4B6` | The implanted ion comes to rest as an interstitial or substitutional atom in the lattice. The surrounding damage (vacancies, interstitials, amorphous zones) can be partially repaired by annealing. In semiconductors, annealing is essential to activate dopants. In metals, the damage itself may be beneficial (contributes to hardening). |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 4 -- Real-Time Monitoring

**Section label:** `WHAT TO WATCH DURING IMPLANTATION` -- Y: 20.7".

**BLOCK E -- Monitoring Parameters**

Y: 21.3" to 26.3". Six monitoring cards in 3x2 grid.

| Position | Parameter | Accent | Normal | If Out of Spec |
|---|---|---|---|---|
| R1C1 | Beam Current | `#E8A020` | Stable at setpoint (+/- 5%) | Current drop = source depletion or extraction issue; check source |
| R1C2 | Integrated Dose | `#27AE60` | Counting toward target; uniform scan | Dose rate anomaly = beam instability; pause and investigate |
| R1C3 | Substrate Temperature | `#E05C5C` | Below limit (120 C for resist; 200 C for steel) | Overtemp = reduce beam current; check thermal contact |
| R2C1 | Scan Uniformity | `#2EC4B6` | Multi-point Faraday reads within +/- 1--2% | Non-uniform = scan waveform drift; recalibrate |
| R2C2 | Chamber Pressure | `#E8A020` | < 10^-5 Torr; stable | Pressure rise = leak or outgassing; may need to abort |
| R2C3 | Charge Neutralization | `#2EC4B6` | Flood gun current stable (if active) | Charging artifacts on insulating substrates; check flood gun |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06".
Parameter: Barlow SemiBold, 14 pt, accent color.
Normal: JetBrains Mono 11 pt `#F0EDE8`.
If Out of Spec: Inter Regular, 11 pt, `#E05C5C`.

---

### ZONE 5 -- Process Timing Reference

**Section label:** `HOW LONG DOES IMPLANTATION TAKE?` -- Y: 26.7".

**BLOCK F -- Timing Table**

Y: 27.3" to 32.3".

| Application | Typical Dose | Beam Current | Implant Time | Total Cycle (incl. overhead) |
|---|---|---|---|---|
| Threshold adjust (semiconductor) | 10^12 ions/cm2 | 1 mA | < 1 second | 30--60 sec (wafer handling dominated) |
| Source/drain (semiconductor) | 10^15 ions/cm2 | 10--25 mA | 5--30 seconds | 1--2 min per wafer |
| High-dose amorphization | 10^15 ions/cm2 | 10--25 mA | 5--30 seconds | 1--2 min per wafer |
| N+ into tool steel (industrial) | 10^17 ions/cm2 | 10--50 mA | 10--60 minutes | 1--2 hours per batch |
| N+ into Ti implant (medical) | 5x10^17 ions/cm2 | 10--30 mA | 30--120 minutes | 2--4 hours per batch |
| High-dose C+ research | 10^18 ions/cm2 | 1--10 mA | Hours to days | Research time scale |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Time: JetBrains Mono 12 pt `#E8A020`.

**Key insight (Y: 31.5"):**
- `Semiconductor implants are fast (seconds per wafer) because doses are low. Industrial implants are slow (minutes to hours) because doses are 100x--10,000x higher. Time = dose / beam current.` -- Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 6 -- Footer

Standard. Title: `Implantation Process`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Implantation Process -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The beam scanning hero (Zone 2) makes an invisible process visible -- you literally cannot see an ion beam (it is in vacuum), so the poster must use diagrams to show what is happening. The collision cascade explanation (Zone 3) is the intellectual heart of the entire Ion Implantation cluster -- it explains the physics of what happens when an energetic ion hits a solid surface. The "precision violence" tagline captures the essence perfectly. The timing table (Zone 5) answers the most common practical question: "How long does this take?"

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #456 -- Construction Workup v1.0*
*2026-04-26*
