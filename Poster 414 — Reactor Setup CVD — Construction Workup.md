---
Project: Plating Posters Inc
Poster Number: 414
Title: "Reactor Setup -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.5)"
Technical Source: CVD reactor types (hot-wall, cold-wall, fluidized bed), furnace specifications, multi-zone temperature control, gas delivery systems (bubblers for TiCl4, MFCs for gaseous reactants), exhaust scrubber systems, and seal/purge protocol.
Process Scope: CVD reactor setup including seal and purge (Stage 6 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - ReactorSetup
  - Furnace
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #414 -- Construction Workup
## Reactor Setup -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 10. After loading, the retort is sealed and the reactor is configured for the deposition run. This covers the seal and purge to displace all air (critical -- air + H2 at temperature is an explosion), the multi-zone heating system, gas delivery infrastructure (bubblers for liquid precursors, MFCs for gases), and exhaust scrubbing. This poster also compares the three reactor types used in CVD.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Reactor type comparison (Block B -- HERO):** Three-panel comparison of hot-wall, cold-wall, and fluidized bed CVD reactors. Each panel is a simplified cross-section schematic built from rectangles with labels.
2. **Gas delivery system diagram (Block C):** Schematic showing bubbler for TiCl4, MFCs for gaseous reactants, and carrier gas lines flowing to the reactor.
3. **Temperature control panel (Block D):** Multi-zone heating concept.
4. **Seal and purge protocol (Block E):** Step-by-step sequence.
5. **Exhaust system (Block F):** Scrubber and filter requirements.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber -- equipment)
ZONE 3 -- REACTOR TYPE COMPARISON / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- GAS DELIVERY + TEMPERATURE CONTROL (14.5"--21.0" / ~6.5")
ZONE 5 -- SEAL & PURGE PROTOCOL (21.0"--26.5" / ~5.5")
ZONE 6 -- EXHAUST SYSTEM + COMMON FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `REACTOR SETUP` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 6 of 10 -- Reactor Types, Gas Delivery, Seal & Purge` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Hot-wall for cutting tools, cold-wall for semiconductors, fluidized bed for powders. All share the same fundamentals: controlled gas delivery, multi-zone heating, and airtight sealing. Get this right or the chemistry cannot work.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts loaded in retort (Stage 5) --> After: Retort sealed, purged, heating initiated`

---

### ZONE 3 -- Reactor Type Comparison (HERO)

**Section label:** `THREE CVD REACTOR TYPES` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Three Reactor Panels (Y: 5.0" to 14.3")**

Three columns. Each: Rounded rect W: 7.33", H: 9.0", fill `#1E2435`, radius 6.

| Panel | X | Reactor Type | Accent |
|---|---|---|---|
| 1 | 0.5" | HOT-WALL CVD | `#E8A020` |
| 2 | 8.17" | COLD-WALL CVD | `#2EC4B6` |
| 3 | 15.83" | FLUIDIZED BED CVD | `#27AE60` |

**Interior per panel:**

*Panel 1 -- Hot-Wall CVD:*
- Top accent: 4 pt `#E8A020`
- Title: `HOT-WALL CVD` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `The Industry Standard for Cutting Tools` Inter Regular 13 pt `#F0EDE8` at 50%

Schematic area (simplified cross-section, ~4.0" tall):
- Outer rectangle: Furnace shell, stroke 2 pt `#C8D0D8`, fill `#252B3D`
- Inner rectangle: Retort, stroke 2 pt `#E8A020`, fill `#1E2435`
- Wavy lines between shell and retort: Heating elements, stroke 1 pt `#E05C5C`
- Small rectangles inside retort: Trays with parts
- Labels: `FURNACE`, `RETORT`, `HEATERS`, `PARTS`

Properties (JetBrains Mono 12 pt `#F0EDE8`):
```
Temp: 800-1100 C
Pressure: 50-500 mbar
Capacity: 500-5,000 inserts
Walls coated: YES
Throughput: Batch (12-24 hr cycle)
```

Application: Inter Medium 12 pt `#E8A020`
- `Standard for cemented carbide cutting inserts -- the workhorse of CVD`

*Panel 2 -- Cold-Wall CVD:*
- Top accent: 4 pt `#2EC4B6`
- Title: `COLD-WALL CVD` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Precision for Semiconductors` Inter Regular 13 pt `#F0EDE8` at 50%

Schematic:
- Outer rectangle: Chamber shell (cool), fill `#252B3D`
- Inner element: Heated substrate pedestal (small rectangle at center), fill `#E05C5C`
- Gas showerhead above substrate (rectangle with small circles), fill `#2EC4B6`
- Labels: `COOL WALLS`, `HEATED PEDESTAL`, `GAS SHOWERHEAD`

Properties:
```
Temp: 600-1200 C (substrate only)
Pressure: 0.1-100 mbar
Capacity: 1-25 wafers
Walls coated: NO (stay cool)
Throughput: Single wafer or small batch
```

Application:
- `Semiconductor epitaxy, SiO2, Si3N4 -- walls stay clean, less waste`

*Panel 3 -- Fluidized Bed CVD:*
- Top accent: 4 pt `#27AE60`
- Title: `FLUIDIZED BED CVD` Barlow SemiBold 20 pt `#27AE60`
- Subtitle: `Coating Powders and Small Parts` Inter Regular 13 pt `#F0EDE8` at 50%

Schematic:
- Vertical column (reactor tube), fill `#252B3D`, stroke 2 pt `#C8D0D8`
- Small circles inside column (fluidized particles), fill `#27AE60`
- Upward arrows (gas flow), stroke 2 pt `#27AE60`
- Gas inlet at bottom, exhaust at top
- Labels: `GAS IN (bottom)`, `FLUIDIZED PARTS`, `EXHAUST (top)`

Properties:
```
Temp: 800-1100 C
Pressure: Atmospheric typical
Capacity: kg quantities of powder/small parts
Walls coated: Minimal (particles absorb precursors)
Throughput: Continuous or semi-continuous
```

Application:
- `Coating powders, nuclear fuel particles, small wear components -- excellent uniformity`

---

### ZONE 4 -- Gas Delivery + Temperature Control

**Two-column layout (Y: 14.5" to 20.8"):**

**Left -- Gas Delivery System (X: 0.5", W: 11.0"):**

**Section label:** `GAS DELIVERY` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

- Rounded rect, Y: 15.2", H: 5.4", fill `#1E2435`, left accent `#27AE60`

**Liquid precursor delivery (bubbler system):**
- Title: `BUBBLER SYSTEM (LIQUID PRECURSORS)` Barlow SemiBold 16 pt `#27AE60`
- `TiCl4 (bp 136 C) kept in thermostatted bubbler at 30-40 C`
- `Carrier gas (H2 or Ar) bubbles through liquid, carrying TiCl4 vapor to reactor`
- `Flow rate controlled by bubbler temperature + carrier gas flow`
JetBrains Mono 12 pt `#F0EDE8`

**Gaseous reactants (MFC system):**
- Title: `MFC SYSTEM (GASEOUS REACTANTS)` Barlow SemiBold 16 pt `#2EC4B6`

| Gas | Purpose | Typical Flow |
|---|---|---|
| H2 | Carrier / reducing | Balance (majority of flow) |
| N2 | Nitride formation | 20-40% of total |
| CH4 | Carbide formation (TiC) | 3-6% of total |
| CH3CN | MT-CVD TiCN precursor | 0.5-2% of total |
| CO2 | Al2O3 formation | 3-6% of total |
| AlCl3 | Al2O3 source (sublimed) | 2-5% of total |

Data: JetBrains Mono 11 pt. Header: Barlow SemiBold 11 pt, fill `#3A4055`.

- `MFC accuracy: +/- 1% of full scale` Inter Regular 11 pt `#F0EDE8` at 60%

**Right -- Temperature Control (X: 12.0", W: 11.5"):**

**Section label:** `MULTI-ZONE HEATING` -- Y: 14.7".

- Rounded rect, Y: 15.2", H: 5.4", fill `#1E2435`, left accent `#E8A020`
- Title: `TEMPERATURE UNIFORMITY` Barlow SemiBold 20 pt `#E8A020`

Key points (Inter Medium 14 pt `#F0EDE8`):
- `3-5 independent heating zones (top, center, bottom, + end zones)`
- `Resistance heating elements (Kanthal, MoSi2, or SiC)`
- `Thermocouples: Type K (to 1200 C) or Type S (to 1600 C)`
- `Uniformity requirement: +/- 5 C across work zone`
- `Temperature survey per AMS 2750 or customer spec`
- `Ramp rate: 5-15 C/min (avoid thermal shock)`

Zone diagram (simplified):
- Three stacked horizontal rectangles representing zones
- `TOP ZONE: TC1` / `CENTER ZONE: TC2, TC3` / `BOTTOM ZONE: TC4`
- Each labeled with target temp: `1000 +/- 5 C`

---

### ZONE 5 -- Seal & Purge Protocol

**Section label:** `SEAL AND PURGE -- THE EXPLOSION PREVENTION STEP` -- Y: 21.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Protocol Panel (Y: 21.8" to 26.3")**

Full-width rounded rect, W: 23.0", H: 4.3", fill `#1E2435`, left accent `#E05C5C`.

**Title:** `CRITICAL: REMOVE ALL AIR BEFORE INTRODUCING H2` Barlow SemiBold 22 pt `#E05C5C`

Steps (numbered, two columns):

**Left column (X: 1.0", W: 10.5"):**

| Step | Action | Detail |
|---|---|---|
| 1 | Close and seal retort | Verify all gaskets/seals intact |
| 2 | Begin Ar or N2 purge | Flow: 20-50 L/min |
| 3 | Purge for 15-30 min | Displace all air (O2 < 100 ppm) |
| 4 | Verify O2 level | Sensor at exhaust must read < 100 ppm |

**Right column (X: 12.5", W: 10.5"):**

| Step | Action | Detail |
|---|---|---|
| 5 | Switch to H2 carrier gas | Begin at low flow, ramp up |
| 6 | Initiate heating program | Ramp 5-15 C/min under H2 flow |
| 7 | Monitor H2 detector | Ensure no leaks at seals or fittings |
| 8 | Confirm stable H2 flow | Ready for stabilization stage |

Data: JetBrains Mono 12 pt `#F0EDE8`. Step numbers: Barlow SemiBold 14 pt `#E05C5C`.

Bottom warning:
- `AIR + H2 AT 800-1100 C = CATASTROPHIC EXPLOSION. This step is not optional. Never skip the purge. Never assume residual air is acceptable.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 6 -- Exhaust System + Common Failures

**Two-column layout (Y: 26.5" to 32.3"):**

**Left -- Exhaust System (X: 0.5", W: 11.0"):**

**Section label:** `EXHAUST SCRUBBING` -- Y: 26.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

- Rounded rect, Y: 27.2", H: 4.9", fill `#1E2435`, left accent `#E05C5C`

Exhaust components (Inter Medium 14 pt `#F0EDE8`):
- `Water scrubber: Neutralizes HCl byproduct gas`
- `Particulate filter: Captures unreacted precursor particles and coating debris`
- `Thermal oxidizer (optional): Burns residual H2 and hydrocarbons`
- `Exhaust must comply with 40 CFR Part 63 (HAP emissions)`
- `Scrubber water pH must be monitored and neutralized before discharge`

Warning:
- `Scrubber failure = HCl release to atmosphere. EPA/OSHA violation. Immediate shutdown required.` Inter Medium 12 pt `#E05C5C`

**Right -- Common Failures (X: 12.0", W: 11.5"):**

**Section label:** `REACTOR SETUP FAILURES` -- Y: 26.7".

Four compact failure cards, each W: 11.5", H: 1.1", fill `#1E2435`, left accent `#E05C5C`.

| Card | Y | Failure | Root Cause & Fix |
|---|---|---|---|
| 1 | 27.2" | INCOMPLETE PURGE | Air remaining in retort -> explosion risk on H2 introduction. Verify O2 < 100 ppm before switching to H2. |
| 2 | 28.5" | TEMPERATURE NON-UNIFORMITY | Heater element failure or thermocouple drift. Run temperature survey per AMS 2750. |
| 3 | 29.8" | GAS LEAK | Seal degradation, fitting failure. Leak check with He detector before every run. |
| 4 | 31.1" | BUBBLER TEMP DRIFT | TiCl4 delivery rate changes -> coating composition shift. Verify bubbler thermostat calibration. |

Interior: Failure in Barlow SemiBold 13 pt `#E05C5C`. Fix in Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Reactor Setup -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Reactor Setup CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-reactor comparison is the hero because operators need to understand which reactor type they are working with and why. Hot-wall is dominant for cutting tools, but the poster should be useful across industries. The seal and purge section is highlighted in Coral because an incomplete purge in a CVD system is genuinely life-threatening -- air + H2 at 1000 C is a detonation hazard. The gas delivery section bridges the gap between "turn the valve" operations and understanding what is actually happening with liquid and gaseous precursor delivery.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #414 -- Construction Workup v1.0*
*2026-04-26*
