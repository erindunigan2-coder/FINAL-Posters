---
Project: Plating Posters Inc
Poster Number: 453
Title: "Loading -- Ion System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.1, 6.5)"
Process Scope: Loading substrates into ion implantation systems -- wafer handling and industrial part fixturing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - Loading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #453 -- Construction Workup
## Loading -- Ion System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading for ion implantation serves two critical functions: positioning the substrate for uniform beam exposure, and ensuring thermal contact so the substrate does not overheat during implantation. Semiconductor systems use automated wafer handlers with electrostatic chucks and backside gas cooling. Industrial systems use simpler fixtures on cooled or heated platens. The hero visual compares semiconductor and industrial loading side by side, emphasizing the thermal contact challenge.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Loading comparison hero (Block B):** Semiconductor wafer handler vs. industrial fixture schematic.
2. **Thermal contact management (Block D):** Why thermal contact matters and how it is achieved.
3. **Wafer handling specifics (Block E):** Electrostatic chuck, backside gas cooling, tilt stage.
4. **Industrial fixturing specifics (Block F):** Platen mounting, mask clamping, batch considerations.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.0" / 20.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- LOADING COMPARISON HERO (2.9"--14.0" / ~11.1")
  Block B: Semiconductor vs. industrial loading side by side
ZONE 3 -- THERMAL CONTACT MANAGEMENT (14.0"--20.0" / ~6.0")
  Block D: Why and how to manage substrate temperature during implant
ZONE 4 -- SEMICONDUCTOR WAFER HANDLING (20.0"--26.5" / ~6.5")
  Block E: Electrostatic chuck, gas cooling, tilt
ZONE 5 -- INDUSTRIAL FIXTURING (26.5"--32.5" / ~6.0")
  Block F: Platen mounting, mask clamping, batch
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Substrate Mounting & Thermal Management` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The ion beam deposits energy into your substrate. Without thermal contact, that energy has nowhere to go. Overheating damages masks, shifts profiles, and ruins parts.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Loading Comparison Hero

**Section label:** `TWO LOADING WORLDS -- SAME THERMAL CHALLENGE` -- Y: 3.1".

**BLOCK B -- Side-by-Side Loading Schematics**

Y: 3.8" to 13.8". Two panels.

**Left Panel -- Semiconductor (X: 0.5", W: 11.0"):**
- Rounded rect container, H: 9.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `SEMICONDUCTOR WAFER LOADING` -- Barlow SemiBold, 20 pt, `#2EC4B6`. Y: 4.2".

Schematic (Y: 5.0" to 11.5"):
- Wafer (thin horizontal line): stroke 2 pt `#C8D0D8`, W: 6.0"
- Label: `Si WAFER (150--300 mm)` JetBrains Mono 10 pt `#C8D0D8`
- Electrostatic chuck below wafer: Rect, W: 7.0", H: 1.0", fill `#3A4055`
- Label: `ELECTROSTATIC CHUCK (ESC)` JetBrains Mono 10 pt `#E8A020`
- Backside gas arrows (between wafer and chuck): Small arrows pointing outward
- Label: `He BACKSIDE GAS (5--15 Torr)` JetBrains Mono 10 pt `#2EC4B6`
- Cooling channels inside chuck: Wavy lines, stroke 1 pt `#2EC4B6`
- Label: `WATER COOLING` Inter Regular 10 pt `#2EC4B6`
- Tilt indicator: Angled line showing 7-deg tilt
- Label: `7 deg TILT (channeling prevention)` JetBrains Mono 10 pt `#E8A020`
- Ion beam arrows from above: 3 downward arrows, stroke 2 pt `#27AE60`
- Label: `ION BEAM` Barlow SemiBold 12 pt `#27AE60`

Key specs below schematic:
```
Wafer size: 150, 200, or 300 mm diameter
Handling: Robotic (FOUP to chuck, automated)
Thermal: ESC + He backside gas + water-cooled chuck
Tilt: Motorized, 0--10 deg adjustable
Throughput: 100--1000+ wafers/hour
```
JetBrains Mono 11 pt `#F0EDE8`.

**Right Panel -- Industrial (X: 12.0", W: 11.5"):**
- Rounded rect container, H: 9.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `INDUSTRIAL PART LOADING` -- Barlow SemiBold, 20 pt, `#E8A020`. Y: 4.2".

Schematic (Y: 5.0" to 11.5"):
- Parts (3 irregular shapes): fill `#C8D0D8` at 40%
- Label: `PARTS (various geometry)` JetBrains Mono 10 pt `#C8D0D8`
- Metal mask over parts (partial): fill `#E8A020` at 30%
- Label: `METAL MASK (clamped)` JetBrains Mono 10 pt `#E8A020`
- Platen below parts: Rect, W: 8.0", H: 1.5", fill `#3A4055`
- Label: `COOLED / HEATED PLATEN` JetBrains Mono 10 pt `#E8A020`
- Thermal paste indicator between parts and platen
- Label: `THERMAL CONTACT (paste or clamping pressure)` Inter Regular 10 pt `#2EC4B6`
- Ion beam arrows from above: 3 downward arrows, stroke 2 pt `#27AE60`
- Label: `ION BEAM` Barlow SemiBold 12 pt `#27AE60`

Key specs below schematic:
```
Part size: Varies (mm to meters)
Handling: Manual or semi-automated
Thermal: Clamped to cooled platen; thermal paste
Tilt: Fixed or adjustable stage
Throughput: Parts/hour to parts/day
```
JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 3 -- Thermal Contact Management

**Section label:** `THERMAL MANAGEMENT -- THE HIDDEN CRITICAL FACTOR` -- Y: 14.2".

**BLOCK D -- Thermal Explanation**

Y: 14.8" to 19.8". Three cards in a row.

| Card | X | W | Title | Accent | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | ENERGY INPUT | `#E05C5C` | The ion beam deposits energy into the substrate. At 100 keV and 10 mA beam current, that is 1,000 watts of power hitting the substrate surface. Without cooling, temperature rises rapidly -- 100s of degrees in minutes for small parts. |
| 2 | 8.16" | 7.33" | WHY OVERHEATING HURTS | `#E05C5C` | Semiconductor: photoresist melts above 120 C, destroying the mask pattern. Industrial: hardened steel tempers above 200 C, losing the substrate hardness you are trying to improve. Both: high temp promotes diffusion, broadening the implant profile. |
| 3 | 15.83" | 7.33" | HOW TO MANAGE IT | `#27AE60` | Semiconductor: electrostatic chuck with He backside gas provides ~1 kW/m2-K thermal conductance. Industrial: clamp to water-cooled platen; use thermal paste for irregular surfaces. Both: monitor temperature continuously; reduce beam current if temp rises. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold, 18 pt, accent color.
Content: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 4 -- Semiconductor Wafer Handling

**Section label:** `SEMICONDUCTOR -- WAFER HANDLING DETAILS` -- Y: 20.2".

**BLOCK E -- Wafer Handling Table**

Y: 20.8" to 26.3".

| Component | Function | Specification | Critical Note |
|---|---|---|---|
| FOUP (Front Opening Unified Pod) | Wafer cassette transport | 25 wafers per FOUP; N2 purge | Wafers never exposed to fab air during transport |
| Robotic handler | Transfers wafer from FOUP to process chamber | Vacuum-compatible end effector | Edge-grip or backside-contact only; no front surface contact |
| Electrostatic chuck (ESC) | Clamps wafer without mechanical contact | Coulombic or Johnsen-Rahbek type | Provides clamping force for backside gas seal |
| He backside gas | Thermal coupling between wafer and chuck | 5--15 Torr He; conductance ~500--2000 W/m2-K | He is used because it is inert and has high thermal conductivity |
| Tilt stage | Prevents channeling | 0--10 deg motorized tilt; typically 7 deg | Tilt angle set in recipe; must be reproducible |
| Dose Faraday cage | Measures dose during implant | Surrounds wafer; measures current to determine dose | Accuracy: +/- 1--2% uniformity; +/- 1--3% wafer-to-wafer |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 12 pt `#F0EDE8`. Specification: JetBrains Mono 11 pt `#2EC4B6`.

---

### ZONE 5 -- Industrial Fixturing

**Section label:** `INDUSTRIAL -- FIXTURING FOR METAL PARTS` -- Y: 26.7".

**BLOCK F -- Industrial Fixturing Guidelines**

Y: 27.3" to 32.3".

| Consideration | Guideline | Why |
|---|---|---|
| Thermal contact | Clamp parts firmly to water-cooled platen; apply thermal paste to irregular surfaces | Poor contact = hot spots = non-uniform treatment |
| Metal masks | Clamp stainless steel or Mo masks over non-implant areas; verify mask thickness vs. Rp | Mask must stop ALL ions at the implant energy |
| Part orientation | Orient flat surfaces perpendicular to beam; tilt complex parts for coverage | Ion implantation is a line-of-sight process |
| Batch loading | Multiple parts per run; all must see uniform beam scan | Verify scan coverage for each part position |
| Electrical isolation | Parts may charge if electrically isolated from platen | Ground parts or use electron flood gun for charge neutralization |
| Documentation | Record part position, mask ID, and fixture configuration for each run | Traceability for quality and repeatability |

Header: Barlow SemiBold, 13 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Guideline: Inter Regular, 13 pt, `#F0EDE8`. Why: Inter Regular, 12 pt, `#F0EDE8` at 70%.

---

### ZONE 6 -- Footer

Standard. Title: `Loading -- Ion System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Ion System -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The loading poster bridges two very different realities: the highly automated, cleanroom-grade semiconductor world and the manual, fixture-based industrial world. The side-by-side hero (Zone 2) makes this contrast visual and immediate. The thermal management section (Zone 3) is the technical core -- it explains WHY loading matters, which is not obvious to someone who thinks of loading as "just putting parts in the machine." The energy calculation (1,000 watts from a 100 keV / 10 mA beam) is a concrete number that makes the thermal challenge tangible.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #453 -- Construction Workup v1.0*
*2026-04-26*
