---
Project: Plating Posters Inc
Poster Number: 433
Title: "Loading -- ALD System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.5, 4.6)"
Technical Source: ALD reactor types (cross-flow, showerhead, batch vertical furnace, spatial, rotary/fluidized bed, roll-to-roll) and loading procedures. Temperature stabilization within the ALD window is critical before cycling begins. Base pressure 0.1--10 Torr depending on system type.
Process Scope: ALD substrate loading, reactor closure, pump-down, and thermal stabilization
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ALD
  - Loading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #433 -- Construction Workup
## Loading -- ALD System

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the ALD sequence. Loading an ALD reactor is straightforward mechanically but temperature stabilization is the critical step -- the substrate must be at a stable temperature within the ALD window before cycling begins. This poster covers reactor types (the variety is remarkable), loading procedures, and the concept of the ALD temperature window.

Hero visual: six ALD reactor types compared -- from single-wafer to spatial ALD.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Six reactor types comparison (Block B -- HERO):** 3x2 grid of ALD reactor configurations.
2. **Loading procedure (Block C):** Step-by-step loading protocol.
3. **ALD temperature window (Block D):** THE key concept -- the temperature range where GPC is constant.
4. **Pump-down and thermal stabilization (Block E):** Getting to base conditions.
5. **Common loading mistakes (Block F):** 4-card strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Silver)
ZONE 3 -- REACTOR TYPES HERO (4.2"--15.5" / ~11.3")
  Block B: Six reactor type panels
ZONE 4 -- LOADING + ALD WINDOW (15.5"--24.0" / ~8.5")
  Block C: Loading procedure
  Block D: ALD temperature window concept
ZONE 5 -- PUMP-DOWN + MISTAKES (24.0"--32.5" / ~8.5")
  Block E: Pump-down and stabilization
  Block F: Common loading mistakes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING` -- 88 pt `#F0EDE8`.
**Subheading:** `ALD -- Stage 3 of 10 -- Reactor Loading and Thermal Stabilization` -- 28 pt `#C8D0D8` (Silver). Y: 1.4".
**Tagline:** `ALD reactors come in six distinct flavors -- from single-wafer R&D tools to continuous roll-to-roll production lines. Temperature stability in the ALD window is universal to all of them.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `150-300` -- 52 pt, `#E8A020`
- Label: `degC ALD WINDOW` -- JetBrains Mono, 14 pt
- Sub-label: `Typical TMA/H2O temperature range` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 3 (`Loading`): fill `#C8D0D8`, text `#1A1F2E`. Others dimmed.
Below: `Input: Clean, functionalized substrate  -->  Output: Substrate in reactor at stable ALD temperature`

---

### ZONE 3 -- Reactor Types Hero

**Section label:** `SIX WAYS TO BUILD AN ALD REACTOR` -- Y: 4.4".

**BLOCK B -- Six Reactor Panels**

Y: 5.0" to 15.3". Six panels in 3x2 grid.
Each panel: Rounded rect, W: 7.33", H: 4.8", fill `#1E2435`, radius 8, top accent 4 pt.

| Panel | Position | Reactor Type | Accent | Throughput |
|---|---|---|---|---|
| 1 | R1C1 (X: 0.5", Y: 5.0") | Cross-Flow (Viscous Flow) | `#2EC4B6` | Low-Medium |
| 2 | R1C2 (X: 8.17", Y: 5.0") | Showerhead | `#E8A020` | Medium |
| 3 | R1C3 (X: 15.83", Y: 5.0") | Batch Vertical Furnace | `#27AE60` | High |
| 4 | R2C1 (X: 0.5", Y: 10.3") | Spatial ALD | `#27AE60` | Very High |
| 5 | R2C2 (X: 8.17", Y: 10.3") | Rotary / Fluidized Bed | `#C8D0D8` | Batch (kg-scale) |
| 6 | R2C3 (X: 15.83", Y: 10.3") | Roll-to-Roll | `#E8A020` | Continuous |

*Panel 1 -- Cross-Flow:*
- Title: `CROSS-FLOW (VISCOUS FLOW)` -- Barlow SemiBold, 16 pt, accent
- Badge: `R&D STANDARD` -- fill accent, text `#1A1F2E`, 12 pt
- Description: `Precursor flows across substrate surface horizontally. Single wafer or small batch. Simple design, well-characterized.`
- Specs: `Substrates: 1--6 wafers. Pressure: 0.1--10 Torr. Application: Research, process development.`

*Panel 2 -- Showerhead:*
- Title: `SHOWERHEAD` -- Barlow SemiBold, 16 pt
- Badge: `PRODUCTION` -- fill accent
- Description: `Gas distributed through perforated plate above substrate. Better uniformity than cross-flow. Standard in semiconductor production.`
- Specs: `Substrates: single 200--300 mm wafer. Pressure: 0.1--5 Torr. Application: Semiconductor manufacturing.`

*Panel 3 -- Batch Vertical Furnace:*
- Title: `BATCH VERTICAL FURNACE` -- Barlow SemiBold, 16 pt
- Badge: `HIGH THROUGHPUT` -- fill accent
- Description: `50--150 wafers stacked vertically. Precursors flow between wafers. Excellent for high-volume production.`
- Specs: `Substrates: 50--150 wafers. Application: Solar cell Al2O3 passivation.`

*Panel 4 -- Spatial ALD:*
- Title: `SPATIAL ALD` -- Barlow SemiBold, 16 pt
- Badge: `INLINE PRODUCTION` -- fill accent
- Description: `Substrate moves through spatially separated precursor zones (instead of time-separated pulses). No purge wait time -- cycle time drops from 30 sec to < 1 sec.`
- Specs: `Throughput: 1000+ wafers/hr. Application: Solar, display, flexible electronics.`

*Panel 5 -- Rotary / Fluidized Bed:*
- Title: `ROTARY / FLUIDIZED BED` -- Barlow SemiBold, 16 pt
- Badge: `PARTICLES & POWDERS` -- fill accent
- Description: `Particles tumbled in rotating drum or fluidized in gas stream during ALD cycling. Enables conformal coating of individual particles.`
- Specs: `Batch size: grams to kilograms. Application: Battery materials, catalysts, pharmaceuticals.`

*Panel 6 -- Roll-to-Roll:*
- Title: `ROLL-TO-ROLL` -- Barlow SemiBold, 16 pt
- Badge: `FLEXIBLE SUBSTRATES` -- fill accent
- Description: `Continuous web of polymer film moves through spatial ALD zones. Inline production of barrier-coated flexible materials.`
- Specs: `Web speed: 0.1--10 m/min. Application: Flexible OLED encapsulation, food packaging barrier.`

---

### ZONE 4 -- Loading Procedure + ALD Window

**BLOCK C -- Loading Procedure (Left, X: 0.5", W: 11.0")**

Section label: `LOADING PROCEDURE` -- Y: 15.7".

Six steps:
```
1. Open reactor (verify no precursor flow, heater at setpoint)
2. Place substrate on heated susceptor / chuck
3. Verify substrate centered and seated flat
4. Close reactor -- check seal (O-ring or face seal)
5. Begin pump-down to base pressure
6. Wait for thermal stabilization (5--15 min at setpoint)
```

Each step: numbered badge + text row.

Bottom note: `Do NOT begin ALD cycling until substrate temperature has stabilized. Temperature affects GPC -- an unstabilized substrate produces non-uniform film thickness.` -- Inter Medium, 12 pt, `#E05C5C`

**BLOCK D -- ALD Temperature Window (Right, X: 12.0", W: 11.5")**

Section label: `THE ALD TEMPERATURE WINDOW` -- Y: 15.7".

Callout panel, fill `#1E2435`, left accent `#27AE60`.

Concept description:
```
The ALD window is the temperature range where:
- Growth per cycle (GPC) is CONSTANT
- Reactions are truly self-limiting
- Film quality is optimal

BELOW WINDOW:
  Precursor condenses on surface (too cold)
  OR reaction is too slow (incomplete)
  GPC is variable and unreliable

WITHIN WINDOW:
  GPC = constant (~0.11 nm/cycle for Al2O3)
  Self-limiting behavior confirmed
  This is where you operate

ABOVE WINDOW:
  Precursor decomposes in gas phase (CVD mode)
  OR precursor desorbs before reacting
  GPC becomes erratic or zero
```

Example (JetBrains Mono, 13 pt, `#27AE60`):
```
TMA / H2O (Al2O3):
  Below window: < 150 degC
  ALD window:   150--350 degC
  Above window: > 350 degC
  Target:       200 degC (standard)
```

---

### ZONE 5 -- Pump-Down + Common Mistakes

**BLOCK E -- Pump-Down and Thermal Stabilization (Y: 24.2" to 28.5")**

Section label: `FROM ATMOSPHERE TO ALD READY` -- Y: 24.4".

Timeline table:

| Phase | Pressure | Time | Action |
|---|---|---|---|
| Roughing | Atm -> 1 Torr | 1--5 min | Mechanical pump |
| Base vacuum | 1 Torr -> 0.1--1 Torr | 5--15 min | Continue pumping; verify leak rate |
| Thermal stabilization | At base pressure | 5--15 min | Heater at setpoint; substrate equilibrating |
| Carrier gas flow | Base pressure + carrier | 2--5 min | Start N2/Ar carrier; pressure stabilizes at working level |

Note: `Some ALD systems operate at near-atmospheric pressure (spatial ALD). For these, pumpdown is minimal -- temperature stabilization is still required.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**BLOCK F -- Common Loading Mistakes (Y: 29.0" to 32.3")**

Section label: `LOADING MISTAKES THAT AFFECT ALD QUALITY` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`. Y: 29.2".

Four cards:

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CYCLING TOO SOON | Substrate not thermally stabilized | Wait 5--15 min after heater reaches setpoint; verify with thermocouple |
| 2 | 6.33" | TEMPERATURE OUTSIDE WINDOW | Heater setpoint incorrect or gradient | Calibrate; verify with thermocouple survey; check reactor uniformity spec |
| 3 | 12.16" | CONTAMINATION ON SUSCEPTOR | Precursor residue from previous runs | Clean susceptor regularly; run ALD clean cycles (O3 or plasma) |
| 4 | 18.0" | SUBSTRATE MISALIGNMENT | Part not centered on heated zone | Verify alignment; use mechanical stops or vacuum chuck |

Card format: standard 4-card strip.

---

### ZONE 6 -- Footer

Standard. Title: `Loading -- ALD System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading ALD System -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The six-reactor-type grid is the educational showpiece. ALD reactor diversity is remarkable -- from a benchtop cross-flow tube to a continuous roll-to-roll production line coating flexible OLED encapsulation films. The spatial ALD panel deserves special attention because it represents the technology leap that made ALD viable for high-throughput manufacturing (solar, display).

The ALD temperature window concept (Block D) is THE foundational ALD principle and should be the one thing someone remembers from this poster. Below the window: condensation. Above: decomposition. Inside: magic.

---

*Alaina -- Poster #433 -- Construction Workup v1.0 -- 2026-04-26*
