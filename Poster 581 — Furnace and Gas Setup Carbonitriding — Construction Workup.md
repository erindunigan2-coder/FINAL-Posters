---
Project: Plating Posters Inc
Poster Number: 581
Title: "Furnace & Gas Setup -- Carbonitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding, Sections 3.2--3.3)"
Technical Source: Equipment and atmosphere setup for gas carbonitriding. Endothermic gas generation, ammonia supply and control, carbon potential measurement, residual ammonia monitoring.
Process Scope: Carbonitriding furnace and atmosphere setup
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - Furnace
  - Atmosphere
  - GasSetup
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #581 -- Construction Workup
## Furnace & Gas Setup -- Carbonitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the equipment and atmosphere that make carbonitriding work. The atmosphere is what distinguishes carbonitriding from carburizing: same endothermic base gas, but with 2--10% ammonia added. The ammonia provides atomic nitrogen that lowers the critical cooling rate and forms carbonitride compounds. This poster details the endo gas generator, ammonia supply, carbon potential control (oxygen probe), and residual ammonia monitoring.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Atmosphere system schematic (Block B -- HERO):** Flow diagram showing endo gas generator -> furnace, with ammonia injection point, oxygen probe, and exhaust burn-off. Built with rectangles, lines, arrows.
2. **Gas composition table (Block D):** Atmosphere component breakdown.
3. **Carbon potential control panel (Block E):** Cp measurement methods and target ranges.
4. **Ammonia control panel (Block F):** Ammonia addition rates, residual ammonia targets, dissociation monitoring.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 19.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ATMOSPHERE SYSTEM SCHEMATIC / HERO (2.9"--14.0" / ~11.1")
  Block B: Gas system flow diagram
ZONE 3 -- GAS COMPOSITION TABLE (14.0"--19.5" / ~5.5")
  Block D: Component breakdown
ZONE 4 -- CARBON POTENTIAL CONTROL (19.5"--26.0" / ~6.5")
  Block E: Cp measurement and targets
  Block F: Ammonia control and monitoring
ZONE 5 -- STARTUP SEQUENCE CHECKLIST (26.0"--32.5" / ~6.5")
  Block G: Step-by-step furnace startup
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FURNACE & GAS SETUP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Carbonitriding Atmosphere -- Endo Gas + Ammonia = Carbon + Nitrogen` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `The atmosphere does the chemistry. Get the gas right, get the case right.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Atmosphere System Schematic (HERO)

**Section label:** `THE CARBONITRIDING ATMOSPHERE SYSTEM` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- System Flow Diagram**

Y: 3.8" to 13.5". Left-to-right flow showing gas generation and delivery.

**Component boxes (rounded rects, fill `#1E2435`, border 1 pt `#3A4055`):**

| Component | X | Y | W | H | Accent | Label |
|---|---|---|---|---|---|---|
| Natural Gas Supply | 0.5" | 5.0" | 4.0" | 2.0" | `#E8A020` top | `CH4 SUPPLY` |
| Endo Gas Generator | 5.5" | 4.0" | 5.0" | 3.5" | `#E8A020` top | `ENDOTHERMIC GENERATOR` |
| Ammonia Supply | 5.5" | 9.0" | 4.0" | 2.0" | `#2EC4B6` top | `NH3 SUPPLY` |
| Furnace Chamber | 12.0" | 3.5" | 7.0" | 5.0" | `#27AE60` top | `FURNACE CHAMBER` |
| Oxygen Probe | 12.0" | 9.5" | 4.0" | 2.0" | `#E8A020` top | `O2 PROBE (Cp)` |
| Exhaust / Burn-Off | 20.0" | 4.5" | 3.5" | 2.0" | `#E05C5C` top | `EXHAUST BURN-OFF` |

**Flow arrows between components:**
- Natural Gas -> Endo Generator: 3 pt `#E8A020`, right arrow
- Endo Generator -> Furnace: 3 pt `#E8A020`, right arrow. Label: `40% N2 + 20% CO + 40% H2`
- NH3 Supply -> Furnace: 3 pt `#2EC4B6`, up-right arrow. Label: `2--10% NH3 by volume`
- Furnace -> Exhaust: 3 pt `#3A4055`, right arrow. Label: `Effluent to burn-off pilot`
- Furnace -> O2 Probe: 3 pt `#E8A020`, down arrow. Label: `Cp feedback`

**Inside Endo Generator box:**
- `Air:Gas ratio ~2.5:1` JetBrains Mono 12 pt `#E8A020`
- `Nickel catalyst at ~1900 F` Inter Regular 11 pt `#F0EDE8` at 70%

**Inside Furnace box:**
- `1400--1600 F` JetBrains Mono 16 pt `#27AE60`
- `Endo + NH3 atmosphere` Inter Medium 13 pt `#F0EDE8`
- Parts schematic: 3 small rects representing workload

**Inside NH3 Supply box:**
- `Anhydrous ammonia` JetBrains Mono 12 pt `#2EC4B6`
- `Rotameter or MFC controlled` Inter Regular 11 pt `#F0EDE8` at 70%

**Callout below diagram (Y: 12.5"):**
- `CRITICAL: Burn-off pilot at exhaust MUST be lit before introducing endo gas. Endo gas is explosive (20% CO + 40% H2).` -- Inter Medium, 14 pt, `#E05C5C`

---

### ZONE 3 -- Gas Composition Table

**Section label:** `ATMOSPHERE COMPOSITION` -- Y: 14.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Gas Component Table**

Y: 14.8" to 19.3". Columns: Component (5.0") | Source (5.0") | Concentration (4.0") | Role (9.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Component | Source | Concentration | Role |
|---|---|---|---|
| Nitrogen (N2) | Endo gas | ~40% by volume | Carrier; inert diluent |
| Carbon monoxide (CO) | Endo gas | ~20% by volume | Primary carbon source: 2CO -> C + CO2 |
| Hydrogen (H2) | Endo gas + NH3 | ~40%+ by volume | Reducing agent; prevents oxidation |
| Methane (CH4) | Enrichment gas | Added to raise Cp | Secondary carbon source |
| Ammonia (NH3) | Anhydrous cylinder | 2--10% by volume | Nitrogen source: NH3 -> N(atomic) + 3/2 H2 |
| CO2 | Reaction product | < 0.5% (controlled) | Cp indicator (inverse relationship) |

Data: JetBrains Mono Regular, 12 pt. Role column: Inter Regular 12 pt.

---

### ZONE 4 -- Carbon Potential + Ammonia Control

**Two-column layout (Y: 19.7" to 25.8").**

**Left -- Carbon Potential Control (X: 0.5", W: 11.0"):**

Section label: `CARBON POTENTIAL (Cp)` Barlow Condensed ExtraBold 22 pt `#E8A020`. Y: 19.7".

Callout box, Y: 20.3", H: 5.3", fill `#1E2435`, left accent `#E8A020`.

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
- `Target Cp: 0.5--0.8% C`
- `Lower than carburizing (0.9--1.1% C) because nitrogen supplements hardening`
- **Measurement methods:**
  - `Zirconia oxygen probe (primary)` -- `#E8A020`
  - `IR CO2 analyzer (cross-check)` -- `#F0EDE8` at 70%
  - `Shim stock (AISI 1095, gold standard)` -- `#F0EDE8` at 70%
- `Cp too high + NH3 = excessive retained austenite`
- `Cp too low = inadequate case hardness`

**Right -- Ammonia Control (X: 12.0", W: 11.5"):**

Section label: `AMMONIA CONTROL (NH3)` Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Y: 19.7".

Callout box, Y: 20.3", H: 5.3", fill `#1E2435`, left accent `#2EC4B6`.

Content:
- `Addition rate: 2--10% by volume of total flow`
- `Typical production: 3--5%`
- `Residual ammonia in exhaust: 0.5--5% undissociated`
- `At 1500 F: 95--98% of NH3 dissociates`
- `The small residual provides atomic nitrogen`
- **Monitoring:** `Orsat analysis or IR analyzer for residual NH3` -- `#2EC4B6`
- `Too much NH3: retained austenite + porosity`
- `Too little NH3: no nitrogen benefit (just carburizing)`

---

### ZONE 5 -- Startup Sequence Checklist

**Section label:** `FURNACE STARTUP -- THE SAFE SEQUENCE` -- Y: 26.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK G -- 6-Step Startup Checklist**

Y: 26.9" to 32.3". Six numbered steps in a vertical list.

Each step: Rounded rect, full width (23.0"), H: 0.8", fill alternating `#1E2435` / `#252B3D`, left accent color-coded.

| Step | Accent | Text |
|---|---|---|
| 1 | `#2EC4B6` | `Close and seal furnace -- verify door seal integrity` |
| 2 | `#E8A020` | `Nitrogen purge -- 5 volume changes minimum to displace all air` |
| 3 | `#E05C5C` | `Light burn-off pilot at exhaust -- MUST be confirmed before gas flow` |
| 4 | `#E8A020` | `Introduce endothermic gas -- verify positive furnace pressure` |
| 5 | `#E8A020` | `Heat to target temperature -- 1400--1600 F per recipe` |
| 6 | `#2EC4B6` | `Introduce ammonia -- 2--10% by volume; verify flow rate on rotameter/MFC` |

Step number: Barlow Condensed ExtraBold 16 pt, accent color. Text: Inter Medium 14 pt `#F0EDE8`.

Bottom callout: `Never introduce endo gas into a furnace that has not been nitrogen-purged. Air + endo gas = explosion.` -- Inter Medium, 14 pt, `#E05C5C`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Furnace & Gas Setup -- Carbonitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Furnace Gas Setup Carbonitriding -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The atmosphere schematic is the hero -- it must make the gas flow path immediately obvious to an operator who may not think in terms of chemistry. The ammonia injection point should be visually distinct (Teal vs. Amber for endo gas) so the unique carbonitriding element stands out. The startup checklist is a life-safety sequence -- step 3 (burn-off pilot) in Coral because skipping it can kill someone.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #581 -- Construction Workup v1.0*
*2026-04-26*
