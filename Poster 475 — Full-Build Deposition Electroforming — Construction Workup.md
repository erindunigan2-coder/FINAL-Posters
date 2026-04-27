---
Project: Plating Posters Inc
Poster Number: 475
Title: "Full-Build Deposition -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.5-8.7)"
Technical Source: Electroforming full-build deposition at production current density. Covers Ni sulfamate parameters, Faraday's law thickness calculation, build time estimates, stress control, bath maintenance during long runs, and the monitoring that keeps a multi-day deposition on track. This is where electroforming becomes an endurance event.
Process Scope: Electroforming full-build deposition (Stage 7 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - Deposition
  - FullBuild
  - FaradaysLaw
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #475 -- Construction Workup
## Full-Build Deposition -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 10. Strike is complete, nucleation is uniform, and now the mandrel builds to target thickness at full current density. For thin electroforms (100 um screen mesh), this takes 2 hours. For thick ones (5 mm waveguide shell), it takes 3-4 days. For massive mold inserts (10 mm), it can run for a week or more. Bath maintenance, stress monitoring, and thickness checks become ongoing tasks during the build.

Hero visual: Faraday's law thickness chart + build time table.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Faraday's law + build time chart (Block B -- HERO):** Thickness vs. time at various current densities.
2. **Deposition parameters table (Block C):** Ni sulfamate operating parameters.
3. **Stress control (Block D):** Saccharin, temperature, and current density effects on stress.
4. **Bath maintenance during long runs (Block E):** What to monitor and when.
5. **Periodic inspection protocol (Block F):** When to pull and measure.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Deposition stage highlighted (Teal)
ZONE 3 -- BUILD TIME CHART HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- PARAMETERS + STRESS CONTROL (14.5"--22.0" / ~7.5")
ZONE 5 -- BATH MAINTENANCE + INSPECTION (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON BUILD PROBLEMS (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FULL-BUILD DEPOSITION` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Building to Target Thickness at Production Current` -- 28 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Electroforming is a marathon, not a sprint. A 5 mm nickel shell takes 83 hours at 5 A/dm2. Bath chemistry, stress, and patience are all required in equal measure.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `~12` -- 60 pt, `#E8A020`
- Label: `um/hr AT 1 A/dm2` -- JetBrains Mono, 14 pt
- Sub-label: `Nickel deposition rate (Faraday's law)` -- Inter Regular, 12 pt

---

### ZONE 2 -- Sequence Orientation Strip

Deposition stage highlighted (Teal). Others dimmed.
Below: `Before: Uniform initial strike established (Stage 6) --> After: Target thickness reached, ready for removal from bath`

---

### ZONE 3 -- Build Time Chart Hero

**Section label:** `BUILD TIME -- FARADAY'S LAW IN ACTION` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Build Time Chart + Table (Y: 5.0" to 14.0")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Left -- Chart (X: 1.5", Y: 5.5", W: 12.0", H: 7.0"):**

X-axis: `Time (hours)` from 0 to 120.
Y-axis: `Thickness (mm)` from 0 to 8.

Three lines at different current densities:

| Line | CD | Rate | Color | Stroke |
|---|---|---|---|---|
| 1 | 1 A/dm2 | 12 um/hr | `#2EC4B6` | 3 pt solid |
| 2 | 3 A/dm2 | 36 um/hr | `#E8A020` | 3 pt solid |
| 3 | 5 A/dm2 | 60 um/hr | `#27AE60` | 3 pt solid |

Each line is straight (linear -- Faraday's law). Labels at line endpoints.

**Faraday's law equation callout (below chart):**
- `Thickness (um) = (CD x t x M) / (n x F x rho x 10^-4)` JetBrains Mono 13 pt `#E8A020`
- `For Ni: ~12 um/hr per A/dm2 at 97% cathode efficiency` Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- Build Time Reference Table (X: 14.5", Y: 5.5", W: 8.0", H: 7.0"):**

| Target Thickness | At 3 A/dm2 | At 5 A/dm2 |
|---|---|---|
| 100 um (0.004") | ~3 hr | ~2 hr |
| 250 um (0.010") | ~7 hr | ~4 hr |
| 500 um (0.020") | ~14 hr | ~8 hr |
| 1 mm (0.040") | ~28 hr | ~17 hr |
| 2 mm (0.080") | ~56 hr (2.3 days) | ~33 hr (1.4 days) |
| 5 mm (0.200") | ~139 hr (5.8 days) | ~83 hr (3.5 days) |
| 10 mm (0.400") | ~278 hr (11.6 days) | ~167 hr (7 days) |

JetBrains Mono 11 pt `#F0EDE8`. Header: Barlow SemiBold 11 pt `#3A4055`.

**Bottom insight (Y: 13.2" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `Higher current density = faster build, but also higher stress, rougher deposit, and more risk of burning. Most Ni sulfamate electroforming runs at 3-5 A/dm2 as the best compromise between speed and quality.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Parameters + Stress Control

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Deposition Parameters (X: 0.5", W: 11.0")**

**Section label:** `Ni SULFAMATE PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Parameter Table (Y: 15.3" to 21.5"):**

| Parameter | Range | Optimal |
|---|---|---|
| Current density | 1-10 A/dm2 | 3-5 A/dm2 |
| Temperature | 40-55 C | 50-54 C |
| pH | 3.5-4.5 | 3.8-4.2 |
| Ni(NH2SO3)2 | 300-450 g/L | 400 g/L |
| NiCl2 | 5-30 g/L | 15 g/L |
| H3BO3 | 30-45 g/L | 40 g/L |
| Saccharin | 0.5-3 g/L | Per Hull cell |
| Wetting agent | 0.01-0.05 g/L | Per Hull cell |
| Agitation | Air or cathode rod | Moderate |
| Filtration | Continuous, 1-5 um | Always running |
| Cathode efficiency | 95-99% | ~97% |
| Deposit hardness | 150-250 HV (no additives) | Application-dependent |

JetBrains Mono 11 pt `#F0EDE8`. Header: `#3A4055`.

**Right -- Stress Control (X: 12.0", W: 11.5")**

**Section label:** `INTERNAL STRESS CONTROL` -- Y: 14.7".

**BLOCK D -- Stress Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
TARGET: < 35 MPa (5000 psi) tensile
IDEAL: Near-zero or slightly compressive

STRESS MATTERS because thick electroforms
under high stress will:
- Crack during or after deposition
- Curl away from mandrel prematurely
- Distort dimensionally after separation
- Fail mechanically in service

STRESS CONTROL TOOLS:

1. SACCHARIN (stress reducer)
   0.5-3 g/L. Reduces tensile stress.
   Too much = brittle, high-S deposit.
   Monitor by Hull cell or spiral
   contractometer.

2. TEMPERATURE
   Higher temp (50-55 C) = lower stress.
   Below 45 C: stress increases sharply.

3. CURRENT DENSITY
   Higher CD = higher stress.
   Keep at 3-5 A/dm2 for thick builds.

4. BATH PURITY
   Organic contamination increases stress.
   Carbon-treat bath regularly (every
   2-4 weeks for heavy use).

5. PULSE PLATING (optional)
   On/off pulsing reduces average stress.
   Typical: 8 ms on / 2 ms off.
```

---

### ZONE 5 -- Bath Maintenance + Inspection

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Bath Maintenance During Long Runs (X: 0.5", W: 11.0")**

**Section label:** `BATH MAINTENANCE -- MULTI-DAY RUNS` -- Y: 22.2".

**BLOCK E -- Maintenance Schedule (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

| Frequency | Action |
|---|---|
| Every shift (8-12 hr) | Check temperature, pH; record amp-hours |
| Daily | Check Ni concentration (specific gravity or titration); adjust pH with H2SO4 or NiCO3; replenish wetting agent |
| Every 48-72 hr | Hull cell test (2 A, 10 min); check for stress, pitting, brightness changes |
| Weekly | Full bath analysis; check boric acid; evaluate filtration (replace if flow drops) |
| As needed | Carbon treatment (if Hull cell shows organic contamination); dummy plate at 0.2-0.5 A/dm2 overnight for metallic contamination |
| Anode maintenance | Check Ni round fill level; replace anode bags when particulate visible |

JetBrains Mono 11 pt `#F0EDE8`. Left column: Barlow SemiBold 11 pt `#E8A020`.

**Right -- Periodic Inspection (X: 12.0", W: 11.5")**

**Section label:** `THICKNESS CHECK PROTOCOL` -- Y: 22.2".

**BLOCK F -- Inspection Protocol (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
FOR THICK ELECTROFORMS (> 1 mm target):

1. CALCULATE expected thickness from
   amp-hours using Faraday's law

2. MEASURE at accessible points using
   micrometer (mandrel + deposit)
   Subtract known mandrel dimension

3. COMPARE calculated vs. measured
   If measured < calculated: check for
   current leakage or low efficiency

4. INSPECT visually for:
   - Roughness (nodules forming?)
   - Discoloration (burning at high-CD areas?)
   - Pitting (H2 bubbles?)
   - Edge buildup (shields working?)

5. ADJUST if needed:
   - Reposition shields
   - Reduce CD if burning evident
   - Carbon-treat if roughness increasing

FOR VERY LONG RUNS (> 5 days):
Consider removing mandrel at midpoint for
full dimensional measurement and
intermediate surface inspection.
```

---

### ZONE 6 -- Common Build Problems

**Section label:** `BUILD PROBLEMS` -- Y: 28.7".

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | HIGH STRESS / CRACKING | Bath contamination; saccharin depleted; CD too high | Carbon treat; replenish saccharin; reduce CD |
| 2 | 6.33" | PITTING | Low wetting agent; pH too low (< 3.5); H2 bubbles | Add wetting agent; adjust pH; increase air agitation |
| 3 | 12.16" | BURNING (ROUGH/DARK) | CD too high for Ni concentration; temp low | Reduce CD or increase Ni; raise temp to 50-54 C |
| 4 | 18.0" | ROUGH DEPOSIT (NODULES) | Particulate in bath; anode sludge | Check filtration; replace anode bags; carbon treat |

---

### ZONE 7 -- Footer

Standard. Title: `Full-Build Deposition -- Electroforming`. Version `v1.0 -- 2026`.

Disclaimer: `Source: Watson Research Brief (Cluster 8); ASTM B832; ASM Handbook Vol. 5. Saccharin dosing must be verified by Hull cell testing -- do not dose by calculation alone.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Full-Build Deposition Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The build time chart is the hero because it answers the first question every electroforming operator asks: "how long is this going to take?" The three current-density lines give an immediate visual of the speed/quality tradeoff. The build time table provides the exact lookup values they will reference before every job. The stress control panel is the most operationally critical content -- uncontrolled stress is the number one failure mode in thick electroforming, and the five tools (saccharin, temperature, CD, bath purity, pulse) give operators a complete strategy.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #475 -- Construction Workup v1.0*
*2026-04-26*
