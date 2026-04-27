---
Project: Plating Posters Inc
Poster Number: 526
Title: "Spray Application -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray application technique, coating buildup, material properties, and common applications. Copper as benchmark material.
Process Scope: Cold spray -- spray application technique and coating characteristics
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #526 -- Construction Workup
## Spray Application -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Spray application poster for Cold Spray. Hero elements: no substrate preheating required, virtually unlimited thickness buildup (additive manufacturing capability), and coating properties that approach bulk material. The copper benchmark table is the centerpiece data element.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Application technique sequence (Block B -- HERO):** Step-by-step spray application procedure.
2. **Coating properties table (Block C):** Cold spray copper vs. bulk copper -- the benchmark comparison.
3. **Key applications gallery (Block D):** 4 cards showing primary cold spray applications.
4. **"No Preheat" advantage callout (Block E):** Emerald callout emphasizing the substrate temperature advantage.
5. **Common defects strip (Block F):** Defects during spray application.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- APPLICATION TECHNIQUE (2.9"--14.0" / ~11.1")
  Block B: Application steps + "No Preheat" callout
ZONE 3 -- COATING PROPERTIES (14.0"--22.0" / ~8.0")
  Block C: Copper benchmark table + material limitation note
ZONE 4 -- KEY APPLICATIONS + DEFECTS (22.0"--32.5" / ~10.5")
  Block D: 4 application cards
  Block F: Common defects strip
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 80 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Build Coatings Without Melting a Single Particle` -- 32 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `No preheat. No bond coat. No thickness limit. Deposit material that machines like wrought metal -- because it never melted.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Application Technique

**Section label:** `APPLICATION TECHNIQUE` -- Y: 3.1".

**BLOCK B -- Application Steps (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 13.5". Six step cards, vertically stacked, connected by arrows.

Each card: W: 14.0", H: 1.4", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Title | Detail |
|---|---|---|---|
| 1 | `#27AE60` | NO SUBSTRATE PREHEAT | Proceed directly to spray -- no warming passes required (unlike plasma, HVOF, flame) |
| 2 | `#2EC4B6` | VERIFY PARAMETERS | Confirm gas pressure, gas temperature, powder feed rate, standoff, traverse speed all at setpoint |
| 3 | `#E8A020` | FIRST PASS -- INTERFACE LAYER | Critical pass -- establishes bonding to substrate. Particles impact virgin surface; adiabatic shear creates metallurgical bond |
| 4 | `#27AE60` | BUILD THICKNESS | 50--500 um per pass. Continue robotic traverse pattern. Virtually unlimited total thickness -- cold spray enables multi-mm additive buildup |
| 5 | `#2EC4B6` | MONITOR DEPOSITION | Track thickness on sacrificial tabs or reference coupons. Compare deposition rate to qualification data |
| 6 | `#E8A020` | COMPLETE SPRAY | Verify total thickness meets specification. Allow natural cooling (no quenching needed) |

**BLOCK E -- "No Preheat" Advantage (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 8.5". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.
Emerald-tinted glass.

Stat: `0 C` Barlow Condensed ExtraBold, 60 pt, `#27AE60`.
Label: `Substrate preheat required` Barlow SemiBold, 18 pt, `#F0EDE8`.

Comparison:
```
Plasma Spray:    80--120 C preheat
HVOF:            60--100 C preheat
Flame Spray:     80--120 C preheat
Cold Spray:      NONE
```
JetBrains Mono Regular, 14 pt. "NONE" in `#27AE60`, others in `#F0EDE8` at 60%.

`The substrate stays cool because particles are solid -- no latent heat of fusion transferred at impact.` Inter Regular, 13 pt, `#F0EDE8` at 70%.

**Thickness callout (below, Y: 9.0" to 13.5"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Title: `UNLIMITED THICKNESS` Barlow SemiBold, 20 pt, `#E8A020`.
Body: `Cold spray deposits build compressive residual stress, not tensile. This means coatings do not delaminate as thickness increases -- enabling multi-millimeter buildups for dimensional restoration and additive manufacturing. Other thermal spray processes are limited to ~2 mm before tensile stress causes failure.` Inter Regular, 13 pt, `#F0EDE8`.

Stat: `50--500 um/pass` JetBrains Mono, 18 pt, `#E8A020`.

---

### ZONE 3 -- Coating Properties

**Section label:** `COATING PROPERTIES -- COPPER BENCHMARK` -- Y: 14.2".

**BLOCK C -- Copper Comparison Table**

Y: 14.8" to 20.0". Full width.

Header row: `#3A4055`. Columns: Property (5.0") | Cold Spray Cu (6.0") | Bulk Cu (reference) (6.0") | Notes (6.0")

| Property | Cold Spray Cu | Bulk Cu | Notes |
|---|---|---|---|
| Porosity | < 0.5% | 0% | Near-fully-dense deposit |
| Oxide content | < 0.1% | 0% | No thermal oxidation |
| Bond strength (ASTM C633) | > 60 MPa | N/A | Often exceeds epoxy strength |
| Hardness | 100--150 HV | 50--80 HV (annealed) | Work-hardened by impact |
| Electrical conductivity | 80--95% IACS | 100% IACS | Recoverable to ~98% with anneal |
| Thermal conductivity | Near bulk | 401 W/mK | Excellent heat transfer |
| Residual stress | Compressive | N/A | Beneficial for fatigue life |

Data: JetBrains Mono Regular, 13 pt. Cold Spray values in `#27AE60`. Bulk values in `#F0EDE8` at 60%.

**Material limitation callout (below table, Y: 20.3" to 21.8"):**
Rounded rect, full width, H: 1.3", fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8.

`LIMITATION: Cold spray can only deposit DUCTILE metals. Ceramics (Al2O3, Cr2O3, YSZ) and brittle materials CANNOT be cold sprayed -- they shatter on impact instead of plastically deforming.` Inter Medium, 14 pt, `#E05C5C`, center.

---

### ZONE 4 -- Key Applications + Defects

**Left -- Key Applications (X: 0.5", W: 11.5")**

Section label: `KEY APPLICATIONS` Y: 22.2".

**BLOCK D -- 4 Application Cards (2x2)**

Y: 22.8" to 30.0". Each card: W: 5.5", H: 3.3", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | Application | Accent | Details |
|---|---|---|---|
| 1 (R1C1) | DIMENSIONAL RESTORATION | `#2EC4B6` | Rebuild corroded or worn aerospace components (Al gearbox housings, structural parts). Deposit directly into machined-out damage, machine flush. |
| 2 (R1C2) | CONDUCTIVITY COATINGS | `#E8A020` | Copper cold spray for electrical and thermal conductivity applications. 80--95% IACS as-sprayed, recoverable with anneal. |
| 3 (R2C1) | ADDITIVE MANUFACTURING | `#27AE60` | Build near-net-shape preforms. Multi-mm deposits. Machine to final dimension. Compressive stress enables unlimited buildup. |
| 4 (R2C2) | CORROSION PROTECTION | `#C8D0D8` | Zinc or aluminum coatings on steel. Dense, low-porosity alternative to arc spray or flame spray for critical applications. |

Application: Barlow SemiBold, 16 pt, accent color.
Details: Inter Regular, 12 pt, `#F0EDE8`.

**Right -- Common Defects (X: 12.5", W: 11.0")**

Section label: `COMMON DEFECTS` Y: 22.2".

**BLOCK F -- Defect Cards (stacked)**

Y: 22.8" to 32.0". Five defect cards.

| Defect | Color | Cause | Fix |
|---|---|---|---|
| LOW DE (particles bouncing) | `#E05C5C` | Velocity below critical threshold | Increase gas pressure / temperature; switch to He |
| POROSITY | `#E8A020` | Insufficient velocity; wrong powder morphology | Increase pressure; use gas-atomized spherical powder |
| POOR ADHESION | `#E05C5C` | Surface contamination; oxide film on substrate | Reclean; reduce clean-to-spray time |
| NOZZLE CLOGGING | `#E8A020` | Powder buildup on nozzle throat | Clean; reduce gas temp; use WC-Co nozzle |
| SURFACE ROUGHNESS | `#2EC4B6` | Large particles or low velocity (partially bonded particles) | Reduce powder size; increase velocity |

Each card: H: 1.7", fill `#1E2435`, left accent defect color.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Spray Application -- Cold Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Three hero stories compete for attention: (1) no preheat, (2) unlimited thickness, and (3) near-bulk material properties. The copper benchmark table is the most data-dense element and should be the reference anchor. The "ductile metals only" limitation callout in coral must be impossible to miss -- it is the single most important constraint in cold spray material selection.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #526 -- Construction Workup v1.0*
*2026-04-26*
