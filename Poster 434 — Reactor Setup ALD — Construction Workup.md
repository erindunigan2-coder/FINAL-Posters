---
Project: Plating Posters Inc
Poster Number: 434
Title: "Reactor Setup -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.5, 4.6)"
Technical Source: ALD reactor setup -- precursor delivery systems (bubblers, ampoules), carrier gas, precursor line heating, and reactor preparation. Precursor delivery is the heart of ALD hardware -- bubblers must be at precise temperature to control vapor pressure and dose consistency.
Process Scope: ALD precursor delivery infrastructure, carrier gas, reactor hardware preparation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ALD
  - ReactorSetup
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #434 -- Construction Workup
## Reactor Setup -- ALD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of the ALD sequence. This poster covers the hardware side of ALD: how precursors get from their containers into the reactor. ALD precursor delivery is elegant in concept (just pulse vapor into the reactor) but demanding in practice (bubblers must be temperature-controlled to +/- 1 degC, all lines must be heated above precursor condensation temperature, and carrier gas flow rates must be precise).

Hero visual: precursor delivery schematic from bubbler to reactor.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Precursor delivery schematic (Block B -- HERO):** Bubbler -> heated line -> reactor with labeled components.
2. **Common ALD precursor systems (Block C):** Table of precursor/co-reactant pairs for major ALD films.
3. **Bubbler operation (Block D):** How bubblers work and why temperature matters.
4. **Line heating and manifold (Block E):** Preventing condensation in delivery lines.
5. **Pre-run system checks (Block F):** Verification protocol.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- PRECURSOR DELIVERY HERO (4.2"--14.5" / ~10.3")
  Block B: Delivery schematic
ZONE 4 -- PRECURSOR PAIRS + BUBBLER OPERATION (14.5"--23.0" / ~8.5")
  Block C: Precursor systems table
  Block D: Bubbler operation
ZONE 5 -- LINE HEATING + PRE-RUN CHECKS (23.0"--32.5" / ~9.5")
  Block E: Line heating
  Block F: Pre-run verification
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `REACTOR SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `ALD -- Stage 4 of 10 -- Precursor Delivery and System Preparation` -- 28 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The bubbler controls the dose. The heated lines prevent condensation. The carrier gas moves the molecules. Every component must work in concert.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `+/- 1` -- 60 pt, `#E8A020`
- Label: `degC BUBBLER CONTROL` -- JetBrains Mono, 14 pt
- Sub-label: `Temperature precision for consistent dosing` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 4 (`Reactor Setup`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: Reactor at base conditions, substrate at ALD temperature  -->  Output: Precursor delivery verified, system ready for cycling`

---

### ZONE 3 -- Precursor Delivery Hero

**Section label:** `PRECURSOR DELIVERY -- FROM CONTAINER TO REACTOR` -- Y: 4.4".

**BLOCK B -- Delivery Schematic**

Y: 5.0" to 14.3". Full width.
Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Schematic flow (left to right):**

Component 1 -- PRECURSOR SOURCE (X: 1.0"):
- Rounded rect, W: 4.5", H: 3.5", fill `#252B3D`, border 2 pt `#E8A020`
- Title: `PRECURSOR BUBBLER` -- Barlow SemiBold, 16 pt, `#E8A020`
- Labels:
```
Liquid precursor (TMA, TDMAT, etc.)
Temperature bath: +/- 1 degC
Carrier gas (N2/Ar) inlet at bottom
Precursor vapor exits at top
Typical: 20--80 degC depending on precursor
```
- Sub-component: `[AMPOULE ALTERNATIVE]` -- `Some precursors delivered from heated ampoule (vapor pressure sufficient without carrier gas bubbling)`

Component 2 -- HEATED DELIVERY LINE:
- Arrow: 3 pt `#E8A020`, right
- Label: `HEATED LINE` -- JetBrains Mono, 14 pt, `#E8A020`
- Details: `All-metal (VCR fittings). Heated 10--20 degC above precursor condensation point. Insulated.`

Component 3 -- PNEUMATIC VALVE:
- Rounded rect, W: 3.0", H: 2.0", fill `#3A4055`
- Label: `ALD VALVE` -- Barlow SemiBold, 14 pt, `#F0EDE8`
- Details: `High-speed pneumatic valve. Opens 15--200 ms per pulse. Defines dose.`

Component 4 -- REACTOR CHAMBER:
- Large rounded rect, W: 6.0", H: 5.0", fill `#252B3D`, border 2 pt `#27AE60`
- Label: `ALD REACTOR` -- Barlow SemiBold, 18 pt, `#27AE60`
- Inside: `Substrate at ALD temperature. Precursor vapor enters, reacts with surface, self-terminates.`

Component 5 -- EXHAUST:
- Arrow right from reactor
- Label: `TO EXHAUST / PUMP` -- Inter Medium, 12 pt, `#C8D0D8`
- Details: `Byproducts (CH4 from TMA) + excess precursor pumped away during purge`

**CO-REACTANT LINE (parallel path below):**
- Second source: `H2O RESERVOIR or O3 GENERATOR or PLASMA SOURCE`
- Same heated-line -> valve -> reactor path
- Label: `Co-reactant delivers on alternate pulse`

**Carrier Gas Line (top):**
- Arrow feeding into bubbler AND directly into reactor for purge
- Label: `CARRIER / PURGE GAS (N2 or Ar)` -- JetBrains Mono, 13 pt, `#2EC4B6`
- Details: `Same gas serves as carrier (through bubbler) and purge (direct to reactor)`

---

### ZONE 4 -- Precursor Pairs + Bubbler Operation

**BLOCK C -- Common ALD Precursor Systems (Left, X: 0.5", W: 11.0")**

Section label: `PRECURSOR + CO-REACTANT = FILM` -- Y: 14.7".

| Film | Precursor A | Co-Reactant B | Bubbler Temp (A) | ALD Temp |
|---|---|---|---|---|
| Al2O3 | TMA (trimethylaluminum) | H2O | 20--25 degC | 150--300 degC |
| HfO2 | TEMAH or HfCl4 | H2O or O3 | 50--80 degC | 200--350 degC |
| TiO2 | TDMAT or TiCl4 | H2O or O3 | 40--75 degC | 150--350 degC |
| ZrO2 | TEMAZ | H2O | 40--60 degC | 200--350 degC |
| ZnO | DEZ (diethylzinc) | H2O | 0--25 degC | 100--250 degC |
| TiN | TDMAT | NH3 | 40--75 degC | 250--400 degC |
| SiO2 | BDEAS or 3DMAS | O2 plasma | 30--50 degC | 50--400 degC |
| Pt | MeCpPtMe3 | O2 or O3 | 60--80 degC | 250--350 degC |

Data: JetBrains Mono, 11 pt. Film names: Inter Medium, 13 pt.
TMA and DEZ rows: left accent `#E05C5C` (pyrophoric).

**BLOCK D -- Bubbler Operation (Right, X: 12.0", W: 11.5")**

Section label: `HOW THE BUBBLER WORKS` -- Y: 14.7".

Callout panel, fill `#1E2435`, left accent `#E8A020`.

```
PRINCIPLE:
  Carrier gas (N2/Ar) flows through liquid
  precursor, picking up vapor molecules.
  The amount of vapor depends on:

  1. BUBBLER TEMPERATURE
     Higher temp = higher vapor pressure = more precursor per pulse
     Must be controlled to +/- 1 degC for consistent dosing

  2. CARRIER GAS FLOW RATE
     Higher flow = more precursor delivered per unit time
     Typical: 10--200 sccm

  3. BUBBLER PRESSURE
     Some systems use pressure-controlled delivery
     instead of flow-controlled

CRITICAL: If bubbler temp drifts, dose changes.
If dose changes, GPC changes. If GPC changes,
your film thickness drifts from target.
```

Bottom note: `TMA at 20 degC has ~10 Torr vapor pressure -- plenty for ALD. Many metalorganic precursors have much lower vapor pressure and require bubblers at 50--80 degC.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- Line Heating + Pre-Run Checks

**BLOCK E -- Line Heating (Y: 23.2" to 27.5")**

Section label: `LINE HEATING -- PREVENTING PRECURSOR CONDENSATION` -- Y: 23.4".

Callout panel, fill `#1E2435`, left accent `#E05C5C`.

Two columns:

Left -- The Problem:
```
If a delivery line is cooler than the
precursor's condensation point, precursor
vapor condenses inside the line.

CONSEQUENCES:
- Inconsistent dosing (no vapor reaches reactor)
- Clogged lines (TMA residue is sticky)
- For pyrophoric precursors (TMA, DEZ):
  condensate + air on maintenance = FIRE
```

Right -- The Solution:
```
HEAT ALL LINES above precursor condensation
temperature. Typical: 10--20 degC above.

LINE HEATING ZONES:
  Bubbler outlet to valve: heated jacket
  Valve body: heated
  Valve to reactor: heated
  Reactor walls: heated
  Exhaust line: heated (prevent buildup)

VERIFY: All zone thermocouples reading
correctly. One cold spot = one blockage.
```

**BLOCK F -- Pre-Run System Checks (Y: 28.0" to 32.3")**

Section label: `PRE-RUN VERIFICATION CHECKLIST` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 28.2".

Two columns:

Left (X: 0.5", W: 11.0"):
```
[ ] Bubbler A temperature at setpoint (+/- 1 degC)
[ ] Bubbler B (or H2O/O3) ready
[ ] All heated lines at setpoint (verify all zones)
[ ] Carrier gas flow confirmed (MFC responding)
[ ] ALD valves tested (listen for click)
[ ] Base pressure achieved (0.1--1 Torr)
```

Right (X: 12.0", W: 11.5"):
```
[ ] Substrate temperature stable (within ALD window)
[ ] Exhaust/pump running
[ ] Precursor level in bubbler sufficient for run
[ ] Recipe loaded: pulse times, purge times, cycle count
[ ] Safety interlocks green
[ ] If TMA/DEZ: Class D extinguisher at station
```

---

### ZONE 6 -- Footer

Standard. Title: `Reactor Setup -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Reactor Setup ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The precursor delivery schematic is the educational centerpiece. ALD hardware is fundamentally about controlled vapor delivery -- a concept that is completely different from the power supplies and targets of PVD or the gas manifolds of CVD. The bubbler is the heart of the system, and the +/- 1 degC temperature control requirement communicates the precision demanded.

The precursor pairs table (Block C) serves as a quick reference that engineers will actually use -- "I need TiO2, what precursor do I use, what bubbler temperature?" The pyrophoric flags on TMA and DEZ rows maintain the safety thread through the cluster.

---

*Alaina -- Poster #434 -- Construction Workup v1.0 -- 2026-04-26*
