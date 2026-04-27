---
Project: Plating Posters Inc
Poster Number: 515
Title: "Parameter Setup -- Arc Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 4: Arc Spray)"
Process Scope: Arc spray parameter setup -- voltage, current, wire feed speed, air pressure, standoff, spray angle
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - ArcSpray
  - Parameters
  - ConstructionWorkup
  - ClusterTS04
---

# Poster #515 -- Construction Workup
## Parameter Setup -- Arc Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Parameter setup for arc spray. The hero is a comprehensive parameter table. Arc spray parameters are fewer than plasma but each one has a direct, visible effect on the spray pattern. Voltage controls spray pattern width; wire feed speed controls deposition rate; atomizing air pressure controls droplet size and coating density. The key relationship: higher air pressure = finer atomization = denser coating.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Parameter table (Block B -- HERO):** Full parameter reference with ranges, notes, and effect descriptions.
2. **Parameter interaction guide (Block C):** How voltage, wire speed, and air pressure interact.
3. **Standoff and angle guide (Block D):** Effect of distance and angle on coating quality.
4. **Test coupon checklist (Block E):** Pre-production validation sequence.
5. **Common parameter errors strip (Block F):** 4 error cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- PARAMETER TABLE / HERO (4.2"--15.5" / ~11.3")
  Block B: Full parameter table
  Block C: Parameter interaction guide
ZONE 4 -- STANDOFF AND ANGLE (15.5"--22.0" / ~6.5")
  Block D: Distance and angle effects
ZONE 5 -- TEST COUPON CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: 6-step pre-production validation
ZONE 6 -- COMMON ERRORS (28.5"--32.5" / ~4.0")
  Block F: 4 error cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Arc Spray -- Voltage, Wire Speed, and Air Pressure` -- 36 pt `#E8A020` (Amber).
**Tagline:** `Three dials that control everything: voltage sets the arc character, wire speed sets the deposition rate, air pressure sets the coating density. Master these three and you master arc spray.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Equipment powered, wire loaded, air verified --> After: Spray pattern verified on test coupon, ready for production`

---

### ZONE 3 -- Parameter Table (HERO)

**Section label:** `ARC SPRAY OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Full Parameter Table**

Y: 5.0" to 12.0". Full width.

| Parameter | Typical Range | Effect | Notes |
|---|---|---|---|
| Arc voltage | 24--35 V | Higher voltage = wider spray pattern, coarser droplets | Primary arc characteristic control |
| Arc current | 100--300 A | Determined by wire feed speed at given voltage | Not directly set -- result of voltage and wire speed |
| Wire feed speed | 2--15 m/min (each wire) | Higher = higher deposition rate, higher current draw | Both wires must be synchronized |
| Atomizing air pressure | 40--80 PSI (275--550 kPa) | Higher pressure = finer atomization, denser coating | Most critical parameter for coating quality |
| Air volume | 40--80 CFM | Must maintain adequate flow at working pressure | Undersized compressor = air pressure drop during spray |
| Standoff distance | 100--250 mm (4--10 in) | Closer = denser; farther = more porosity | Optimal typically 150--200 mm |
| Spray angle | 60--90 degrees | Below 45 degrees = severe porosity and poor adhesion | 90 degrees (perpendicular) is ideal |
| Traverse speed | Manual: operator-controlled; Robot: 200--800 mm/s | Faster = thinner passes; slower = thicker but risk overheating | Consistency determines uniformity |
| Deposition rate | 5--30+ kg/hr | Highest of all thermal spray processes | Material and parameter dependent |
| Deposition efficiency | 60--80% | Higher than flame spray (50--70%) | Remainder is overspray |
| Particle velocity | 50--200 m/s | Atomizing gas pressure is primary velocity driver | Air velocity at nozzle exit |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 13 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".
Parameter names: Inter Medium 13 pt `#F0EDE8`. Ranges: JetBrains Mono 12 pt `#E8A020`. Effect/Notes: Inter Regular 12 pt.

**BLOCK C -- Parameter Interaction Guide**

Y: 12.5" to 15.0". Three connected panels.

**Panel 1 -- Voltage (X: 0.5", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020`
- Title: `VOLTAGE (24--35 V)` Barlow SemiBold 16 pt `#E8A020`
- `Low voltage (24--28 V): narrow, focused spray pattern; finer droplets`
- `High voltage (30--35 V): wider, more diffuse pattern; coarser droplets`
- `Start low and increase until pattern width matches application`

**Panel 2 -- Wire Speed (X: 8.15", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6`
- Title: `WIRE SPEED (2--15 m/min)` Barlow SemiBold 16 pt `#2EC4B6`
- `Controls deposition rate directly`
- `Higher speed = more material = higher current draw`
- `Both wires must feed at equal speed -- asymmetry causes arc instability`

**Panel 3 -- Air Pressure (X: 15.85", W: 7.3"):**
- Rounded rect, fill `#1E2435`, top accent `#27AE60`
- Title: `AIR PRESSURE (40--80 PSI)` Barlow SemiBold 16 pt `#27AE60`
- `The single most important parameter for coating density`
- `Higher pressure = finer atomization = denser, smoother coating`
- `Lower pressure = coarser droplets = more porosity`
- `Balance: too high = excessive overspray and material waste`

---

### ZONE 4 -- Standoff and Angle

**Section label:** `STANDOFF DISTANCE & SPRAY ANGLE` -- Y: 15.7".

**BLOCK D -- Distance and Angle Effects**

Y: 16.3" to 21.5". Two panels.

**Left -- Standoff Distance (X: 0.5", W: 11.0"):**

| Range | Effect | Color |
|---|---|---|
| Too close (<100 mm) | Substrate overheating; coating stress; spatter buildup on gun | `#E05C5C` at 20% |
| Optimal (100--250 mm) | Best density, adhesion, and surface finish | `#27AE60` at 20% |
| Too far (>300 mm) | High porosity; poor adhesion; cold, solidified particles | `#E05C5C` at 20% |

**Right -- Spray Angle (X: 12.0", W: 11.5"):**

| Angle | Effect | Color |
|---|---|---|
| 90 degrees | Maximum density and bond strength | `#27AE60` at 20% |
| 60--75 degrees | Acceptable; slight porosity increase | `#E8A020` at 15% |
| <45 degrees | Severe porosity; shadowing; poor adhesion -- avoid | `#E05C5C` at 20% |

---

### ZONE 5 -- Test Coupon Checklist

**Section label:** `PRE-PRODUCTION TEST COUPON SEQUENCE` -- Y: 22.2".

**BLOCK E -- 6-Step Checklist**

Y: 22.8" to 28.3". Two columns of 3 steps each.

| Step | Action | Verify |
|---|---|---|
| 1 | Select test coupon -- same substrate as production | Match material, thickness, and surface condition |
| 2 | Grit blast coupon to same profile spec | Ra 4--12 um; SSPC-SP 5 |
| 3 | Spray one pass at production parameters | Observe spray pattern; uniform fan; stable arc |
| 4 | Measure thickness per pass | Record microns per pass for production planning |
| 5 | Build to target thickness on second coupon | Verify total thickness and visual quality |
| 6 | Bend test or adhesion check per specification | Document results before production spray |

Step numbers: Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Action: Inter Regular 14 pt. Verify: JetBrains Mono 12 pt `#27AE60`.

---

### ZONE 6 -- Common Errors

**Section label:** `COMMON PARAMETER ERRORS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Error | Result | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WIRE FEED IMBALANCE | Asymmetric arc; uneven spray pattern; one wire consumed faster | Synchronize both wire feed speeds; check for drag in conduit |
| 2 | 6.33" | AIR PRESSURE TOO LOW | Coarse droplets; excessive porosity; rough surface | Increase atomizing air to 60--80 PSI; verify compressor capacity |
| 3 | 12.16" | VOLTAGE TOO HIGH | Excessively wide spray pattern; high overspray; material waste | Reduce voltage in 2 V increments until pattern tightens to workpiece width |
| 4 | 18.0" | WORN CONTACT TIPS | Arc wanders; inconsistent spray pattern; spitting | Replace contact tips every shift or per OEM wear schedule |

---

### ZONE 7 -- Footer

Standard footer. Title: `Parameter Setup -- Arc Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; general industry knowledge. Parameters shown are typical ranges -- always verify against your equipment OEM documentation and coating specification.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #515 -- Construction Workup v1.0 -- 2026-04-26*
