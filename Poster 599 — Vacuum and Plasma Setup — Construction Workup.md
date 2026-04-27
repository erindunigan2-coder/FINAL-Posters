---
Project: Plating Posters Inc
Poster Number: 599
Title: "Vacuum & Plasma Setup -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5, Sections 5.2, 5.3)"
Process Scope: Vacuum system operation, gas supply, plasma ignition, and DC power setup for plasma nitriding
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - VacuumSetup
  - PlasmaIgnition
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #599 -- Construction Workup
## Vacuum & Plasma Setup -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the system setup between loading and the nitriding cycle itself -- vacuum pumpdown, gas introduction, DC power supply configuration, and plasma ignition. The visible plasma glow is the signature of this process, and operators need to understand what it tells them.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **System schematic hero (Block B):** Simplified P&ID showing vacuum pump, gas supply (N2/H2), mass flow controllers, DC power supply, vessel, pressure gauge, and thermocouple connections.
2. **Startup sequence checklist (Block D):** Step-by-step from door-closed to plasma-on.
3. **Plasma glow interpretation guide (Block E):** What normal vs. abnormal glow looks like.
4. **Parameter windows table (Block F):** Pressure, voltage, gas ratio ranges.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SYSTEM SCHEMATIC HERO (2.9"--15.5")
ZONE 3 -- STARTUP SEQUENCE (15.5"--22.0")
ZONE 4 -- PLASMA GLOW GUIDE + PARAMETER WINDOWS (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `VACUUM & PLASMA SETUP` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- From Closed Door to Glowing Plasma` -- 32 pt `#E8A020` (Amber).
**Tagline:** `Vacuum integrity is non-negotiable. Gas ratio is your compound layer dial. The glow tells you everything.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `< 0.1` -- 72 pt `#2EC4B6`
- Label: `mbar base vacuum -- verify before every cycle` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- System Schematic (HERO)

**Section label:** `PLASMA NITRIDING SYSTEM -- SIMPLIFIED SCHEMATIC` -- Y: 3.1".

**BLOCK B -- System Diagram (Y: 3.8" to 15.3")**

Simplified P&ID built with rectangles, lines, and labeled connection points:

**Central element -- Vessel:**
- Rounded rect, X: 7.0", Y: 6.0", W: 10.0", H: 7.0", fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `VACUUM VESSEL` Barlow SemiBold 18 pt `#F0EDE8`
- Inner label: `Parts on cathode` Inter Regular 14 pt `#27AE60`

**Left side -- Vacuum system:**
- Rect (mechanical pump): X: 0.5", Y: 9.0", W: 3.5", H: 1.5", fill `#1E2435`, border 2 pt `#2EC4B6`
- Text: `MECH PUMP + ROOTS BLOWER` JetBrains Mono 11 pt `#2EC4B6`
- Line from pump to vessel with valve symbol
- Pressure gauge symbol on line: `PIRANI / CAPACITANCE GAUGE` JetBrains Mono 10 pt `#F0EDE8` at 60%

**Right side -- Gas supply:**
- Two gas bottle symbols (rects):
  - N2: X: 20.0", Y: 4.5", W: 2.0", H: 2.5", fill `#1E2435`, border 2 pt `#2EC4B6`, label `N2 (99.999%)`
  - H2: X: 20.0", Y: 7.5", W: 2.0", H: 2.5", fill `#1E2435`, border 2 pt `#E8A020`, label `H2 (99.999%)`
- Lines from bottles through mass flow controller symbol to vessel
- MFC label: `MASS FLOW CONTROLLERS` JetBrains Mono 11 pt `#E8A020`

**Top -- DC Power Supply:**
- Rect: X: 9.0", Y: 4.0", W: 6.0", H: 1.5", fill `#1E2435`, border 2 pt `#E8A020`
- Text: `DC POWER SUPPLY` Barlow SemiBold 14 pt `#E8A020`
- `400--1000 V | PULSED DC` JetBrains Mono 12 pt `#E8A020`
- Lines down to vessel: `(-)` to cathode plate, `(+)` to vessel wall

**Bottom -- Supplemental heating:**
- Rect: X: 9.0", Y: 13.5", W: 6.0", H: 1.0", fill `#1E2435`, border 1 pt `#C8D0D8`
- Text: `SUPPLEMENTAL RESISTANCE HEATERS` JetBrains Mono 10 pt `#C8D0D8`

**Thermocouple labels:**
- `TC-1, TC-2 (on parts)` JetBrains Mono 10 pt `#27AE60` with lines to parts inside vessel

---

### ZONE 3 -- Startup Sequence

**Section label:** `STARTUP SEQUENCE -- DOOR CLOSED TO PLASMA ON` -- Y: 15.7".

**BLOCK D -- Step Checklist (Y: 16.3" to 21.8")**

8 numbered steps, each a row:

| Step | Action | Parameter | Check |
|---|---|---|---|
| 1 | Close and seal vessel door | Door seal / O-ring integrity | Visual inspection of seal |
| 2 | Start rough pump | Pump down to < 10 mbar | Monitor gauge; listen for pump |
| 3 | Engage Roots blower | Continue to < 0.1 mbar | Leak rate < 1 mbar/min |
| 4 | Leak rate test | Hold vacuum; measure pressure rise | FAIL: > 1 mbar/min rise = find and fix leak |
| 5 | Introduce H2 flush | H2 at low flow; purge moisture | 2--5 min flush |
| 6 | Set gas ratio | N2/H2 per recipe (typical 25/75) | Verify MFC readings |
| 7 | Set pressure | Throttle pump to 1--5 mbar | Verify stable pressure |
| 8 | Energize DC supply | Start at low voltage; ramp up | Observe uniform glow; adjust pulse parameters |

Each row: alternating fills, H: 0.65". Step number: Barlow Condensed ExtraBold 16 pt `#E8A020`. Action: Inter Medium 13 pt. Check: JetBrains Mono 11 pt `#27AE60`.

---

### ZONE 4 -- Plasma Glow Guide + Parameter Windows

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Plasma Glow Interpretation (X: 0.5", W: 11.0")**

Section label: `READING THE GLOW` -- Barlow Condensed ExtraBold 22 pt.

4 stacked indicator cards:

| Glow State | Color Code | Meaning | Action |
|---|---|---|---|
| Uniform violet/purple | `#27AE60` | Normal -- plasma conforming to all part surfaces uniformly | Proceed; temperature ramping correctly |
| Bright spots / concentrated glow | `#E05C5C` | Hollow cathode effect -- arcing at close spacing or small holes | Reduce voltage; check part spacing; may need to abort and re-load |
| Dim / patchy glow | `#E8A020` | Low pressure or low voltage; plasma not fully established | Increase voltage or pressure; check gas flow |
| No glow | `#E05C5C` | Plasma not ignited; possible electrical fault or pressure too high/low | Check DC supply; verify pressure in 1--10 mbar range; check cathode contact |

Each card: H: 2.3", fill `#1E2435`, left accent in color code.

**Right -- BLOCK F: Parameter Windows (X: 12.0", W: 11.5")**

Section label: `OPERATING WINDOWS` -- Barlow Condensed ExtraBold 22 pt.

| Parameter | Typical Range | Notes |
|---|---|---|
| Base vacuum | < 0.1 mbar | Must achieve before gas intro |
| Operating pressure | 1--5 mbar | Throttle valve controls |
| DC voltage | 400--800 V (pulsed) | Pulsed DC preferred for uniformity |
| Pulse frequency | 1--10 kHz | Higher frequency = finer control |
| Duty cycle | 20--80% | Controls effective power and temperature |
| N2 fraction | 5--80% | Standard 25%; low = no white layer; high = thick epsilon |
| H2 fraction | 20--95% | Balance of N2 fraction |
| Current density | 0.5--3.0 mA/cm2 | Measured on cathode area |
| Supplemental heat | As needed | Resistance heaters supplement plasma heating |

Table: Header `#3A4055`, data alternating rows. JetBrains Mono 12 pt.

---

### ZONE 5 -- Footer

Standard footer. Title: `Vacuum & Plasma Setup -- Plasma Nitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. Note: `#9B59B6` violet for plasma visualization -- remap to `#7D3C98` for light. **Export:** Six files.

---

*Alaina -- Poster #599 -- Construction Workup v1.0 -- 2026-04-26*
