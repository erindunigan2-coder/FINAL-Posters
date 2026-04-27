---
Project: Plating Posters Inc
Poster Number: 446
Title: "Deposition -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Sections 5.1, 5.3)"
Process Scope: DLC film deposition -- PECVD (a-C:H) and filtered cathodic arc (ta-C) methods
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Deposition
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #446 -- Construction Workup
## Deposition -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the money poster in the DLC cluster -- the actual coating step. It covers the two dominant deposition methods side by side: PECVD (a-C:H) and filtered cathodic arc (ta-C). The hero visual is a split-panel comparison showing the plasma physics of each method. Below that, the real-time process monitoring parameters that operators watch during a run, and a defect gallery for what goes wrong during deposition. The goal: an operator or engineer should be able to look at this poster and understand WHAT is happening inside the chamber while the coating is being deposited.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Split-panel deposition comparison hero (Block B):** Two side-by-side chamber cross-section schematics -- PECVD on left, filtered arc on right. Each shows gas/plasma flow, substrate position, and ion energy pathways. Built with rectangles, arrows, and labels.
2. **Real-time monitoring panel (Block D):** Key parameters operators watch during deposition.
3. **Deposition rate comparison (Block E):** Side-by-side rate data for both methods.
4. **Defect gallery (Block F):** Common deposition-stage defects with visual descriptions and fixes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- DEPOSITION METHOD COMPARISON HERO (2.9"--15.0" / ~12.1")
  Block B: PECVD vs. Filtered Arc split panel
ZONE 3 -- REAL-TIME MONITORING (15.0"--21.0" / ~6.0")
  Block D: What operators watch during deposition
ZONE 4 -- DEPOSITION RATE COMPARISON (21.0"--27.0" / ~6.0")
  Block E: Rate, thickness, and cycle time data
ZONE 5 -- DEPOSITION DEFECT GALLERY (27.0"--32.5" / ~5.5")
  Block F: 6 common defects with causes and fixes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `DEPOSITION` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Growing the Film` -- 36 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Two methods, one goal: pack as much sp3-bonded carbon onto your part as physics will allow. This is where carbon becomes diamond-like.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Deposition Method Comparison Hero

**Section label:** `TWO METHODS -- SAME FAMILY, DIFFERENT PHYSICS` -- Y: 3.1".

**BLOCK B -- Split Panel Comparison**

Y: 3.8" to 14.8". Two side-by-side panels.

**Left Panel -- PECVD / a-C:H (X: 0.5", W: 11.0"):**

Rounded rect container, H: 10.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`.

Title: `PECVD -- a-C:H` -- Barlow SemiBold, 22 pt, `#2EC4B6`. Y: 4.2".
Subtitle: `Hydrogenated Amorphous Carbon` -- Inter Regular, 14 pt, `#F0EDE8` at 60%. Y: 4.7".

Chamber schematic (Y: 5.2" to 10.5"):
- Outer rect representing chamber wall: stroke 2 pt `#3A4055`, fill none
- RF electrode (top): Rect, W: 6.0", H: 0.4", fill `#E8A020` at 40%
- Label: `RF ELECTRODE (13.56 MHz)` JetBrains Mono 10 pt `#E8A020`
- Substrate (bottom): Rect, W: 6.0", H: 0.5", fill `#C8D0D8` at 50%
- Label: `SUBSTRATE (BIASED -200 to -400 V)` JetBrains Mono 10 pt `#C8D0D8`
- Gas inlet arrow (left side): Arrow pointing right into chamber
- Label: `C2H2 + Ar IN` JetBrains Mono 10 pt `#2EC4B6`
- Plasma glow region (center): Rounded rect, fill `#2EC4B6` at 10%, dashed border 1 pt `#2EC4B6`
- Label: `PLASMA GLOW` Inter Medium 11 pt `#2EC4B6`
- Downward arrows from plasma to substrate representing ion bombardment: 3 arrows, stroke 2 pt `#27AE60`
- Label: `C+, CH+, H+ ions` JetBrains Mono 10 pt `#27AE60`
- Pump arrow (bottom right): Arrow pointing out
- Label: `TO PUMP` Inter Regular 10 pt `#F0EDE8` at 50%

Key specs list (Y: 10.8" to 14.5"):
- Inter Regular, 13 pt, `#F0EDE8`, line height 180%

```
Precursor gas: C2H2 (acetylene) or CH4 (methane)
Carrier gas: Ar (argon)
Working pressure: 100--300 mTorr
RF power: 200--800 W at 13.56 MHz
Substrate bias: -200 to -400 V DC
Ion energy arriving at film: 50--200 eV
Substrate temperature: 80--150 C
sp3 content: 30--50%
Hydrogen content: 20--40 at%
Hardness: 10--20 GPa (1,000--2,000 HV)
Deposition rate: 1--3 um/hr
```

Values in JetBrains Mono 13 pt `#2EC4B6`.

**Right Panel -- Filtered Cathodic Arc / ta-C (X: 12.0", W: 11.5"):**

Rounded rect container, H: 10.5", fill `#1E2435`, top accent 4 pt `#E8A020`.

Title: `FILTERED ARC -- ta-C` -- Barlow SemiBold, 22 pt, `#E8A020`. Y: 4.2".
Subtitle: `Tetrahedral Amorphous Carbon` -- Inter Regular, 14 pt, `#F0EDE8` at 60%. Y: 4.7".

Chamber schematic (Y: 5.2" to 10.5"):
- Graphite cathode (left): Rounded rect, W: 1.5", H: 2.0", fill `#3A4055`
- Label: `GRAPHITE CATHODE` JetBrains Mono 10 pt `#E8A020`
- Arc spot indicator: Small circle on cathode face, fill `#E8A020`
- Label: `ARC SPOT (40--100 A)` JetBrains Mono 10 pt `#E8A020`
- Filter bend (center): Curved path with arrow, stroke 2 pt `#E8A020`
- Label: `MAGNETIC FILTER` Inter Medium 11 pt `#E8A020`
- Small dots along outer edge of curve representing macroparticles being filtered
- Label: `Macroparticles removed` Inter Regular 10 pt `#F0EDE8` at 50%
- Substrate (right): Rect, W: 3.0", H: 2.0", fill `#C8D0D8` at 50%
- Label: `SUBSTRATE (BIASED -50 to -2000 V)` JetBrains Mono 10 pt `#C8D0D8`
- Filtered plasma beam: Arrow from filter exit to substrate, stroke 2 pt `#27AE60`
- Label: `C+ ions (>90% ionized)` JetBrains Mono 10 pt `#27AE60`

Key specs list (Y: 10.8" to 14.5"):

```
Source: Solid graphite cathode
Process gas: None required (vacuum arc)
Working pressure: < 1 mTorr
Arc current: 40--100 A
Filter coil current: 5--20 A
Substrate bias: -50 to -2000 V
Optimum ion energy: ~50 eV per C+ ion
Substrate temperature: RT--150 C
sp3 content: 50--80%
Hydrogen content: < 1 at%
Hardness: 40--80 GPa (4,000--8,000 HV)
Deposition rate: 0.1--1 um/hr
```

Values in JetBrains Mono 13 pt `#E8A020`.

---

### ZONE 3 -- Real-Time Monitoring

**Section label:** `WHAT TO WATCH DURING DEPOSITION` -- Y: 15.2".

**BLOCK D -- Monitoring Parameters**

Y: 15.8" to 20.8". Six monitoring cards in a 3x2 grid.

| Position | Parameter | Accent | Normal Range | If Out of Spec |
|---|---|---|---|---|
| R1C1 | Chamber Pressure | `#2EC4B6` | PECVD: 100--300 mTorr / Arc: < 1 mTorr | Pressure rise = leak or outgassing; abort and leak-check |
| R1C2 | Substrate Bias Voltage | `#E8A020` | Per recipe (+/- 5%) | Drift = power supply issue or arcing; check connections |
| R1C3 | Substrate Temperature | `#E05C5C` | < 200 C (hardened steel); < 150 C preferred | Overtemp = risk to substrate hardness; reduce power or extend cooling pauses |
| R2C1 | Gas Flow Rate | `#2EC4B6` | Per MFC setpoint (+/- 2%) | Flow deviation = MFC drift or gas supply issue |
| R2C2 | Deposition Time | `#E8A020` | Per recipe; rate x target thickness | Running long = low deposition rate; check source condition |
| R2C3 | Arc Current (arc only) | `#27AE60` | 40--100 A stable | Fluctuation = cathode erosion or anode contamination |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06".
Parameter: Barlow SemiBold, 16 pt, accent color.
Range: JetBrains Mono Regular, 12 pt, `#F0EDE8`.
If Out of Spec: Inter Regular, 12 pt, `#E05C5C`.

---

### ZONE 4 -- Deposition Rate Comparison

**Section label:** `RATE, THICKNESS & CYCLE TIME` -- Y: 21.2".

**BLOCK E -- Comparison Table**

Y: 21.8" to 26.8".

Two-column layout:

**Left -- a-C:H by PECVD (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `a-C:H (PECVD)` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Value |
|---|---|
| Deposition rate | 1--3 um/hr |
| Typical thickness | 1--5 um |
| Interlayer time | 15--45 min (Cr/CrC gradient) |
| DLC deposition time | 30 min -- 5 hr |
| Total cycle (load to unload) | 2--6 hours |
| Parts per batch | 100--10,000 (depends on chamber) |
| Coating color | Dark gray to black (transparent if thin) |

**Right -- ta-C by Filtered Arc (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ta-C (FILTERED ARC)` -- Barlow SemiBold, 18 pt, `#E8A020`

| Parameter | Value |
|---|---|
| Deposition rate | 0.1--1 um/hr |
| Typical thickness | 0.5--3 um |
| Interlayer time | 15--45 min (Cr or Si) |
| DLC deposition time | 30 min -- 30 hr |
| Total cycle (load to unload) | 3--8 hours typical |
| Parts per batch | Fewer (smaller source area) |
| Coating color | Black, highly reflective |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

---

### ZONE 5 -- Deposition Defect Gallery

**Section label:** `DEPOSITION-STAGE DEFECTS` -- Y: 27.2".

**BLOCK F -- 6 Defect Cards (3x2 grid)**

Y: 27.8" to 32.3".

| Position | Defect | Accent | Cause | Fix |
|---|---|---|---|---|
| R1C1 | Haze / cloudy film | `#E05C5C` | Gas-phase polymerization; PECVD pressure too high | Reduce pressure; increase substrate bias energy |
| R1C2 | Macroparticles | `#E05C5C` | Arc droplets passing filter (arc only) | Check filter magnetic field; reduce arc current; clean filter duct |
| R1C3 | Soft coating | `#E8A020` | Low bias; excessive hydrogen incorporation | Increase bias voltage; reduce hydrocarbon gas fraction |
| R2C1 | Thickness non-uniformity | `#E8A020` | Poor rotation; shadowing; source depletion | Check rotation; verify fixture design; inspect source |
| R2C2 | Arcing on substrate | `#E05C5C` | Sharp edges; contamination; excessive bias | Round edges pre-coat; improve cleaning; reduce bias |
| R2C3 | Color variation batch-to-batch | `#E8A020` | Gas composition drift; source erosion; temperature variation | Calibrate MFCs; replace cathode on schedule; monitor temp |

Each card: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, left accent 0.06".
Defect: Barlow SemiBold, 14 pt, `#E05C5C`.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Fix: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 6 -- Footer

Standard. Title: `Deposition -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deposition DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is where DLC stops being theory and becomes a film on a part. The split-panel hero must land the fundamental difference between PECVD and filtered arc -- one uses gas chemistry (hydrocarbon plasma), the other uses a solid graphite cathode and pure carbon ions. That difference drives everything: sp3 content, hardness, hydrogen content, deposition rate, and cost. The monitoring zone is for operators; the defect gallery is for troubleshooting engineers. Together with Poster 445 (Parameter Setup), this poster gives a complete picture of the DLC deposition process.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #446 -- Construction Workup v1.0*
*2026-04-26*
