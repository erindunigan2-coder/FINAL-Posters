---
Project: Plating Posters Inc
Poster Number: 436
Title: "In-Situ Monitoring -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.7-4.8)"
Technical Source: ALD in-situ monitoring -- spectroscopic ellipsometry, quartz crystal microbalance (QCM), and the quality metrics that confirm self-limiting behavior during deposition. Unlike CVD or PVD where operators may rely on time-based estimates, ALD monitoring can track film growth cycle by cycle.
Process Scope: ALD in-situ monitoring and process verification (Stage 8 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ALD
  - Monitoring
  - Ellipsometry
  - QCM
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #436 -- Construction Workup
## In-Situ Monitoring -- ALD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 10. ALD's self-limiting nature means that if the process is working correctly, the film grows at a perfectly predictable rate. In-situ monitoring confirms this cycle by cycle. This poster covers the two primary real-time monitoring methods (spectroscopic ellipsometry and QCM), the quality metrics that ALD engineers track, and how deviations from expected GPC diagnose specific problems.

Hero visual: GPC staircase chart showing perfectly linear film growth vs. cycle count, with annotated deviation scenarios.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **GPC staircase chart (Block B -- HERO):** Thickness vs. cycle number showing ideal linear growth and deviation scenarios.
2. **Ellipsometry panel (Block C):** How spectroscopic ellipsometry works for ALD.
3. **QCM panel (Block D):** Quartz crystal microbalance for mass-based monitoring.
4. **Quality metrics reference (Block E):** GPC, uniformity, conformality, impurity targets.
5. **Deviation diagnostics (Block F):** What GPC deviations tell you.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- GPC STAIRCASE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- MONITORING METHODS (14.5"--22.0" / ~7.5")
  Block C: Ellipsometry
  Block D: QCM
ZONE 5 -- QUALITY METRICS + DEVIATION DIAGNOSTICS (22.0"--28.5" / ~6.5")
  Block E: Quality targets
  Block F: Diagnostic table
ZONE 6 -- PROCESS VERIFICATION CHECKLIST (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `IN-SITU MONITORING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 8 of 10 -- Tracking Film Growth Cycle by Cycle` -- 28 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `ALD is the only deposition method where you can count the atoms going down. In-situ monitoring confirms the count is correct.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `< 1%` -- 60 pt, `#27AE60`
- Label: `UNIFORMITY TARGET` -- JetBrains Mono, 14 pt
- Sub-label: `Across-wafer non-uniformity for semiconductor ALD` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 8 (`In-Situ Monitoring`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: ALD cycling in progress (Stage 7) --> Output: Film growth confirmed on-target, process validated`

---

### ZONE 3 -- GPC Staircase Hero

**Section label:** `FILM GROWTH vs. CYCLE COUNT -- THE ALD STAIRCASE` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Staircase Chart (Y: 5.0" to 14.0")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Chart area (X: 2.5", Y: 5.5", W: 18.0", H: 7.0"):**

X-axis: `Cycle Number` from 0 to 100. JetBrains Mono 11 pt `#F0EDE8` at 60%.
Y-axis: `Film Thickness (nm)` from 0 to 12. JetBrains Mono 11 pt `#F0EDE8` at 60%.

**Ideal growth line:** Staircase stepping up from (0, 0) to (100, 11.0). 3 pt stroke `#27AE60`.
- Each step = one cycle = +0.11 nm
- Label on line: `IDEAL: GPC = 0.11 nm/cycle (Al2O3)` Barlow SemiBold 13 pt `#27AE60`

**Deviation scenario 1 (above ideal):**
- Dashed line, steeper slope, 2 pt `#E05C5C`
- Label: `HIGH GPC: Precursor overlap (CVD mode) or condensation` Inter Medium 12 pt `#E05C5C`

**Deviation scenario 2 (below ideal):**
- Dashed line, shallower slope, 2 pt `#E8A020`
- Label: `LOW GPC: Incomplete reaction, surface blocked, or temp too high (desorption)` Inter Medium 12 pt `#E8A020`

**Deviation scenario 3 (initial delay then catching up):**
- Dotted line showing flat first ~10 cycles then normal slope, 2 pt `#2EC4B6`
- Label: `NUCLEATION DELAY: Substrate surface lacks initial -OH groups` Inter Medium 12 pt `#2EC4B6`

**Right-side annotation (X: 17.0" to 23.0"):**

Key stat card:
- Rounded rect, W: 5.5", H: 2.5", fill `#252B3D`, border 1 pt `#27AE60`
```
100 cycles x 0.11 nm/cycle
= 11.0 +/- 0.5 nm Al2O3

This result is INDEPENDENT of:
- Reactor geometry
- Gas flow pattern
- Substrate position
- Substrate shape/topology
```
JetBrains Mono 12 pt `#F0EDE8`.

**Bottom insight (Y: 13.3" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#27AE60`
- `The linear staircase is the signature of true ALD. Any deviation from linearity tells you the process is not fully self-limiting -- diagnose using the deviation table below.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Monitoring Methods

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Spectroscopic Ellipsometry (X: 0.5", W: 11.0")**

**Section label:** `SPECTROSCOPIC ELLIPSOMETRY` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Ellipsometry Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
PRINCIPLE:
Polarized light reflects off the film surface.
The change in polarization (psi and delta)
depends on film thickness and optical constants.

MEASURES:
- Thickness: +/- 0.1 nm accuracy
- Refractive index (n) and extinction
  coefficient (k)
- Can track growth EVERY CYCLE

IN-SITU SETUP:
Optical windows on ALD reactor allow
light beam to reach substrate surface.
Software fits measured data to optical model
in real time.

GOLD STANDARD for ALD monitoring
in semiconductor fabrication.

LIMITATION:
Requires optical access to substrate.
Works best on flat, reflective substrates.
Not practical for batch/rotary ALD.
```

**Right -- QCM (X: 12.0", W: 11.5")**

**Section label:** `QUARTZ CRYSTAL MICROBALANCE (QCM)` -- Y: 14.7".

**BLOCK D -- QCM Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
PRINCIPLE:
Piezoelectric quartz crystal oscillates
at a resonant frequency. As mass deposits
on the crystal surface, frequency decreases.

MEASURES:
- Mass gain per cycle
  (converts to thickness via density)
- Sub-nanogram sensitivity

IN-SITU SETUP:
QCM sensor crystal mounted inside
ALD reactor, exposed to same precursor
environment as substrate.

ADVANTAGE:
Works regardless of substrate type.
Can monitor inside batch reactors.
Shows mass gain for EACH half-cycle
(Pulse A mass gain vs. Pulse B mass gain).

LIMITATION:
Sensor crystal coats over time --
must be replaced periodically.
Temperature sensitivity -- requires
thermal stabilization of crystal.
```

---

### ZONE 5 -- Quality Metrics + Deviation Diagnostics

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Quality Metrics (X: 0.5", W: 11.0")**

**Section label:** `QUALITY METRICS -- WHAT TO MEASURE` -- Y: 22.2".

**BLOCK E -- Metrics Table (Y: 22.8" to 27.0"):**

| Metric | Target | Method |
|---|---|---|
| GPC | Match literature value for precursor/temp | In-situ ellipsometry or QCM |
| Non-uniformity | < 1% across wafer (semiconductor) | 49-point ellipsometry map |
| Conformality (step coverage) | > 95% (bottom/top thickness ratio) | TEM or SEM cross-section of test structures |
| Carbon impurity | < 2 at% (Al2O3 at > 200 C) | XPS or SIMS |
| Refractive index | 1.62-1.65 for Al2O3 | Ellipsometry |
| Film density | > 3.0 g/cm3 for Al2O3 | XRR (X-ray reflectivity) |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Deviation Diagnostics (X: 12.0", W: 11.5")**

**Section label:** `GPC DEVIATION DIAGNOSTICS` -- Y: 22.2".

**BLOCK F -- Diagnostic Cards (Y: 22.8" to 28.0"):**

Four stacked cards, each W: 11.0", H: 1.2", fill `#252B3D`:

Card 1 -- `GPC HIGHER THAN EXPECTED`:
- Left accent `#E05C5C`
- `Precursors overlapping (CVD mode). Increase purge time. Or: temperature below ALD window (condensation).`

Card 2 -- `GPC LOWER THAN EXPECTED`:
- Left accent `#E8A020`
- `Insufficient precursor dose (bubbler temp low, pulse too short). Or: temperature above ALD window (desorption).`

Card 3 -- `GPC DRIFTING OVER RUN`:
- Left accent `#2EC4B6`
- `Bubbler precursor level dropping (less vapor per pulse). Or: reactor wall buildup affecting gas dynamics.`

Card 4 -- `NUCLEATION DELAY (first 5-20 cycles)`:
- Left accent `#27AE60`
- `Substrate surface lacks functional groups. Pre-treat with O2 plasma, UV-ozone, or H2O soak. Normal on hydrophobic surfaces.`

---

### ZONE 6 -- Process Verification Checklist

**Section label:** `MID-RUN VERIFICATION` -- Y: 28.7". Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

Rounded rect, fill `#1E2435`, Y: 29.2" to 32.3".

Two columns:

Left:
```
[ ] GPC matches expected value (+/- 5%)
[ ] No drift in GPC over cycle count
[ ] Reactor pressure stable between pulses
[ ] Bubbler temperature at setpoint
[ ] Purge baseline (pressure return to base
    between pulses)
```

Right:
```
[ ] Ellipsometry or QCM data tracking normally
[ ] No abnormal pressure spikes
    (indicates precursor decomposition or leak)
[ ] Carrier gas flow steady
[ ] Cycle count on schedule for target thickness
[ ] No error flags from ALD controller
```

JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `In-Situ Monitoring -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `In-Situ Monitoring ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The GPC staircase chart is the hero because it communicates ALD's defining property visually: perfectly linear growth. The three deviation lines (too steep, too shallow, nucleation delay) turn the chart into a diagnostic tool -- operators can compare their own data to the poster and immediately identify the category of problem. The ellipsometry vs. QCM comparison gives engineers a clear basis for choosing their monitoring strategy.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #436 -- Construction Workup v1.0*
*2026-04-26*
