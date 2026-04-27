---
Project: Plating Posters Inc
Poster Number: 404
Title: "Vacuum System Setup -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.2)"
Technical Source: PVD vacuum system including roughing pumps, turbomolecular/cryogenic pumps, base vacuum requirements, leak checking, and pump-down procedures.
Process Scope: PVD vacuum system setup (Stage 4 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - Vacuum
  - PumpDown
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #404 -- Construction Workup
## Vacuum System Setup -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 10. The vacuum system is the heart of PVD infrastructure. Without achieving base vacuum below 5 x 10^-5 Torr, coatings will contain oxides, have poor adhesion, and show contamination. This poster covers the pump-down sequence, vacuum measurement, leak detection, and the relationship between vacuum quality and coating quality.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Vacuum system schematic (Block B -- HERO):** Simplified diagram showing roughing pump -> turbo/cryo pump -> chamber, with valves, gauges, and gas inlet.
2. **Pump-down curve chart (Block D):** Pressure vs. time showing rough pump region, crossover, and high-vacuum region.
3. **Vacuum quality table (Block E):** Pressure ranges and what they mean for coating quality.
4. **Leak detection checklist (Block F):** Systematic leak-checking procedure.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 16.0" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber -- equipment)
ZONE 3 -- VACUUM SYSTEM SCHEMATIC / HERO (4.2"--16.0" / ~11.8")
ZONE 4 -- PUMP-DOWN CURVE + VACUUM RANGES (16.0"--22.0" / ~6.0")
ZONE 5 -- LEAK DETECTION (22.0"--28.0" / ~6.0")
ZONE 6 -- MAINTENANCE + COMMON PROBLEMS (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `VACUUM SYSTEM SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 4 of 10 -- Pump-Down, Leak Check, Base Vacuum` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `No vacuum, no PVD. Base pressure below 5 x 10^-5 Torr is the minimum for quality hard coatings. Leak rate, outgassing, and pump condition determine everything.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts fixtured in chamber (Stage 3) --> After: Chamber at base vacuum, ready for ion etching`

---

### ZONE 3 -- Vacuum System Schematic (HERO)

**Section label:** `THE PVD VACUUM SYSTEM -- FROM ATMOSPHERE TO HIGH VACUUM` -- Y: 4.4".

**BLOCK B -- System Schematic (Y: 5.0" to 15.8")**

Horizontal schematic flowing left to right:

**Chamber (center-right):**
- Large rounded rect, X: 12.0", Y: 6.0", W: 10.0", H: 6.0", fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `PVD CHAMBER` Barlow SemiBold 18 pt `#F0EDE8`
- Inside: small fixture/part indicators, target indicators on walls
- Gauge symbol (circle): `IG` (ion gauge) on chamber, `TC` (thermocouple) on foreline

**Turbo/Cryo Pump (below chamber):**
- Rounded rect, X: 14.0", Y: 12.5", W: 4.0", H: 2.0", fill `#1E2435`, border 2 pt `#2EC4B6`
- Label: `TURBO / CRYO PUMP` Barlow SemiBold 14 pt `#2EC4B6`
- Gate valve between pump and chamber: small rect `#E8A020`
- Label: `GATE VALVE` Inter Regular 11 pt `#E8A020`

**Roughing Pump (far left):**
- Rounded rect, X: 1.0", Y: 8.0", W: 4.0", H: 2.0", fill `#1E2435`, border 2 pt `#E8A020`
- Label: `ROUGHING PUMP` Barlow SemiBold 14 pt `#E8A020`
- Sub-label: `Rotary vane or scroll` Inter Regular 12 pt `#F0EDE8` at 60%

**Foreline (connecting roughing to turbo):**
- Line from roughing pump output to turbo pump inlet
- Stroke: 3 pt `#3A4055`
- Foreline valve: small rect `#E8A020`

**Gas Inlet (top of chamber):**
- Small rectangles representing MFCs, connected to chamber top
- Labels: `Ar`, `N2`, `O2`, `C2H2` -- JetBrains Mono 12 pt `#F0EDE8`
- Label: `MASS FLOW CONTROLLERS` Inter Regular 12 pt `#2EC4B6`

**Pressure readout callouts:**
- `Atmosphere: 760 Torr` JetBrains Mono 13 pt `#F0EDE8` at 50%
- `Rough vacuum: < 50 mTorr (crossover)` JetBrains Mono 13 pt `#E8A020`
- `Base vacuum: < 5 x 10^-5 Torr` JetBrains Mono 14 pt `#27AE60`
- `Working pressure: 1-10 mTorr` JetBrains Mono 13 pt `#2EC4B6`

**Rule card (top-right):**
- Rounded rect, X: 17.0", Y: 5.0", W: 6.5", H: 2.5", fill `#1E2435`, border 1 pt `#27AE60`
- Big number: `< 5 x 10^-5` Barlow Condensed ExtraBold 36 pt `#27AE60`
- Label: `Torr -- BASE VACUUM TARGET` Inter Medium 14 pt `#F0EDE8`
- Sublabel: `< 1 x 10^-5 preferred for high-quality films` Inter Regular 12 pt `#27AE60`

---

### ZONE 4 -- Pump-Down Curve + Vacuum Ranges

**Section label:** `PUMP-DOWN SEQUENCE AND VACUUM QUALITY` -- Y: 16.2".

**BLOCK D -- Two-Column Layout (Y: 16.8" to 21.8")**

**Left -- Pump-Down Curve Description (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `TYPICAL PUMP-DOWN CURVE` Barlow SemiBold 18 pt `#E8A020`

Simplified curve description (text-based since we cannot render true charts):
```
Phase 1: Roughing (0-10 min)
  760 Torr -> ~50 mTorr
  Rotary vane pump only

Phase 2: Crossover (~50 mTorr)
  Open gate valve to turbo/cryo
  Close roughing valve to chamber

Phase 3: High vacuum (10-90 min)
  50 mTorr -> < 5 x 10^-5 Torr
  Turbo/cryo pump + foreline backing

Total: 30-90 min (chamber dependent)
```

JetBrains Mono 13 pt `#F0EDE8`. Phase labels: Barlow SemiBold 14 pt `#E8A020`.

**Right -- Vacuum Quality Table (X: 12.0", W: 11.5"):**

| Pressure Range | Classification | Coating Impact |
|---|---|---|
| > 1 x 10^-3 Torr | Poor vacuum | Excessive O2/H2O; coating will fail |
| 1 x 10^-4 Torr | Marginal | Possible oxide inclusions; reduced adhesion |
| < 5 x 10^-5 Torr | Acceptable | Standard quality hard coatings |
| < 1 x 10^-5 Torr | Excellent | Highest quality; lowest contamination |
| < 1 x 10^-6 Torr | Research grade | Not required for industrial PVD |

Color coding: Poor = `#E05C5C`, Marginal = `#E8A020`, Acceptable = `#27AE60`, Excellent = `#27AE60` bold.

---

### ZONE 5 -- Leak Detection

**Section label:** `LEAK DETECTION -- FINDING AND FIXING VACUUM LEAKS` -- Y: 22.2".

**BLOCK E -- Leak Check Procedure (Y: 22.8" to 27.8")**

**Left -- Systematic Leak Check (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `LEAK CHECK PROCEDURE` Barlow SemiBold 18 pt `#2EC4B6`

Steps (Inter Regular 14 pt `#F0EDE8`):
1. `Pump to base vacuum and monitor pressure rise`
2. `Acceptable leak rate: < 2 mTorr/min`
3. `If leak rate high: spray He at suspected joints (He leak detector)`
4. `Check O-rings first -- #1 leak source`
5. `Check feedthroughs, viewport seals, gas fittings`
6. `Virtual leaks: outgassing from trapped volumes, dirty chamber walls`

**Right -- Common Leak Sources (X: 12.0", W: 11.5"):**

| Source | Likelihood | Fix |
|---|---|---|
| O-ring seals (door, viewport) | HIGHEST | Replace O-ring; clean groove; check for nicks |
| Gas line fittings | HIGH | Retighten VCR/Swagelok; replace gasket |
| Feedthroughs (electrical, water) | MODERATE | Tighten; replace if corroded |
| Chamber wall (weld crack) | LOW | He leak detect to locate; weld repair |
| Virtual leak (trapped gas) | COMMON | Bake-out at 100-200 C; redesign fixture |

Likelihood: color-coded -- HIGHEST/HIGH `#E05C5C`, MODERATE `#E8A020`, LOW/COMMON `#2EC4B6`.

---

### ZONE 6 -- Maintenance + Common Problems

**Section label:** `VACUUM SYSTEM MAINTENANCE` -- Y: 28.2".

**BLOCK F -- Four Problem Cards (Y: 28.7" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SLOW PUMP-DOWN | Contaminated chamber, water vapor, O-ring degradation | Bake-out; replace O-rings; check pump oil |
| 2 | 6.33" | CAN'T REACH BASE VACUUM | Leak or outgassing; pump degradation | Leak check; service pump; check foreline trap |
| 3 | 12.16" | PUMP OIL BACKSTREAMING | Cold trap missing or saturated; turbo bearing wear | Install/regenerate cold trap; service turbo |
| 4 | 18.0" | GAUGE READING UNSTABLE | Contaminated gauge filament; gas burst | Clean or replace gauge; check for intermittent leak |

Standard failure card format.

---

### ZONE 7 -- Footer

Standard footer. Title: `Vacuum System Setup -- PVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Vacuum System Setup PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The vacuum system schematic is the hero because operators need to understand the relationship between roughing pump, high-vacuum pump, and chamber. The pump-down curve description (text-based due to rendering limitations) walks through the three phases every PVD operator experiences. The leak detection section is heavily practical -- O-rings are always the first suspect, and virtual leaks are the most confusing for new operators.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #404 -- Construction Workup v1.0*
*2026-04-26*
