---
Project: Plating Posters Inc
Poster Number: 536
Title: "Spray Application -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun spray application technique. Each detonation cycle deposits a circular spot ~25 mm diameter. Coating built by overlapping spots via robotic traverse. 5--20 um per spot. Total thickness 75--500 um. Substrate temperature controlled by air cooling between cycles. WC-12Co benchmark coating properties: porosity < 0.5%, bond strength > 80 MPa, hardness 1200--1500 HV300.
Process Scope: D-Gun -- spray application technique and coating characteristics
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #536 -- Construction Workup
## Spray Application -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Spray application poster for D-Gun. Hero elements: the spot-overlap deposition concept (each detonation deposits a single 25 mm spot, and coating is built by precisely overlapping these spots), and the WC-12Co benchmark table comparing D-Gun to HVOF coatings. The pulsed nature of D-Gun deposition is fundamentally different from all continuous thermal spray processes -- this is the unique visual story.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Application technique steps (Block B -- HERO):** How spot-overlap deposition works.
2. **WC-12Co benchmark table (Block C):** D-Gun vs. HVOF side-by-side coating properties.
3. **Spot overlap concept (Block D):** Visual showing how individual spots build up a continuous coating.
4. **Key D-Gun applications gallery (Block E):** 4 cards showing primary applications.
5. **Common defects strip (Block F):** Defects during spray application.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- APPLICATION TECHNIQUE (2.9"--14.0" / ~11.1")
  Block B: Application steps
  Block D: Spot overlap concept
ZONE 3 -- COATING PROPERTIES BENCHMARK (14.0"--22.0" / ~8.0")
  Block C: WC-12Co D-Gun vs. HVOF table
ZONE 4 -- KEY APPLICATIONS + DEFECTS (22.0"--32.5" / ~10.5")
  Block E: 4 application cards
  Block F: Common defects strip
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Building Coatings One Detonation at a Time` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Each explosion deposits a single 25 mm spot. Overlap them precisely and you get the densest, hardest coatings in thermal spray.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Application Technique

**Section label:** `APPLICATION TECHNIQUE` -- Y: 3.1".

**BLOCK B -- Application Steps (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 13.5". Six step cards, vertically stacked, connected by arrows.

Each card: W: 14.0", H: 1.4", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Title | Detail |
|---|---|---|---|
| 1 | `#E8A020` | VERIFY SUBSTRATE PREP | Confirm grit-blasted surface is clean, dry, within time window. Verify masking secure. |
| 2 | `#2EC4B6` | CONFIRM PARAMETERS | O2/C2H2 ratio set; frequency selected; powder charge calibrated; standoff programmed |
| 3 | `#27AE60` | INITIATE DETONATION CYCLE | Start remotely from outside booth. First spots establish bond to substrate surface. |
| 4 | `#E8A020` | BUILD COATING BY SPOT OVERLAP | Robot traverses part; each detonation deposits 25 mm spot at 5--20 um thick. Overlapping spots build continuous coating. |
| 5 | `#2EC4B6` | MONITOR SUBSTRATE TEMPERATURE | IR pyrometer monitors substrate temp. Pause and cool if approaching limit. Pulsed heat input allows recovery between cycles. |
| 6 | `#27AE60` | COMPLETE TO TARGET THICKNESS | Total thickness: 75--500 um. Verify against specification using reference coupons or in-process measurement. |

**BLOCK D -- Spot Overlap Concept (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 9.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.

Title: `SPOT OVERLAP DEPOSITION` Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

Concept description (Inter Regular, 13 pt, `#F0EDE8`, line height 155%):
```
Unlike continuous spray processes,
D-Gun builds coating spot by spot:

  Single spot:  ~25 mm diameter
  Spot thickness: 5--20 um
  Frequency:    1--15 spots/second

The robot traverses so each new spot
overlaps 50--75% of the previous one.
Multiple traverse passes build up
the total coating thickness.

This pulsed deposition gives D-Gun
two unique advantages:
1. Intermittent heat -- substrate
   cools between cycles
2. Each spot is independently
   dense -- no continuous splat
   cascade porosity
```

Stat: `5--20 um/spot` JetBrains Mono Bold, 20 pt, `#E8A020`.
vs. `25--75 um/pass` JetBrains Mono Regular, 14 pt, `#F0EDE8` at 60%. Label: `(HVOF continuous)`.

**Pulsed heat advantage (below, Y: 9.5" to 13.5"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Title: `PULSED HEAT ADVANTAGE` Barlow SemiBold, 18 pt, `#27AE60`.
Body (Inter Regular, 13 pt, `#F0EDE8`):
```
Continuous processes (plasma, HVOF) deliver
a constant heat stream to the substrate.

D-Gun delivers heat in discrete pulses.
Between pulses, the substrate conducts
heat away. This intermittent loading means:

  - Lower peak substrate temperature
  - Less thermal distortion of thin parts
  - Better coating adhesion on heat-sensitive
    substrates
  - No need for aggressive substrate cooling
    (air cooling between cycles sufficient)
```

---

### ZONE 3 -- Coating Properties Benchmark

**Section label:** `COATING PROPERTIES -- WC-12Co BENCHMARK` -- Y: 14.2".

**BLOCK C -- D-Gun vs. HVOF Comparison Table**

Y: 14.8" to 21.5". Full width.

Header row: `#3A4055`. Columns: Property (5.0") | D-Gun WC-12Co (5.5") | HVOF WC-12Co (5.5") | Advantage (7.0")

| Property | D-Gun WC-12Co | HVOF WC-12Co | Advantage |
|---|---|---|---|
| Porosity | < 0.5% (often < 0.2%) | < 1% (typically < 0.5%) | D-Gun: denser |
| Oxide content | < 0.3% | < 0.5% | D-Gun: less oxidation |
| Bond strength (ASTM C633) | > 80 MPa (exceeds epoxy) | > 70 MPa | D-Gun: stronger bond |
| Hardness (HV300) | 1200--1500 | 1100--1400 | D-Gun: harder |
| Surface roughness (as-sprayed, Ra) | 2--5 um | 3--6 um | D-Gun: smoother |
| Wear rate (ASTM G65) | 0.5--3 x 10^-7 mm3/Nm | 1--5 x 10^-7 mm3/Nm | D-Gun: more wear-resistant |
| Deposition rate | 1--5 kg/hr | 2--10 kg/hr | HVOF: faster throughput |
| Coating thickness range | 75--500 um | 75--750 um | HVOF: broader range |

Data: JetBrains Mono Regular, 12 pt. D-Gun values in `#E8A020`. HVOF values in `#2EC4B6`.
"Advantage" column: Inter Medium, 12 pt. D-Gun advantages in `#E8A020`. HVOF advantages in `#2EC4B6`.

**Summary callout (below table, Y: 21.0" to 21.8"):**
Rounded rect, full width, H: 0.6", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

`D-Gun wins on coating quality (density, hardness, wear resistance). HVOF wins on throughput and versatility. Both are hard-chrome replacements.` Inter Medium, 13 pt, `#E8A020`, center.

---

### ZONE 4 -- Key Applications + Defects

**Left -- Key Applications (X: 0.5", W: 11.5")**

Section label: `KEY D-GUN APPLICATIONS` Y: 22.2".

**BLOCK E -- 4 Application Cards (2x2)**

Y: 22.8" to 30.0". Each card: W: 5.5", H: 3.3", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | Application | Accent | Details |
|---|---|---|---|
| 1 (R1C1) | GAS TURBINE COMPONENTS | `#E8A020` | Blades, vanes, seals, shrouds. WC-Co and CrC-NiCr for erosion and high-temperature wear. The original and primary D-Gun market. |
| 2 (R1C2) | PUMP AND VALVE COMPONENTS | `#2EC4B6` | Pump plungers, valve seats, sleeve bearings. WC-CoCr for chemical and abrasive wear resistance in harsh fluid environments. |
| 3 (R2C1) | HARD CHROME REPLACEMENT | `#27AE60` | WC-Co D-Gun coatings as a premium replacement for hard chromium plating. Superior wear life, no hexavalent chromium. |
| 4 (R2C2) | CERAMIC WEAR SURFACES | `#C8D0D8` | Cr2O3 and Al2O3-TiO2 for high-temperature wear, chemical inertness, and electrical insulation. D-Gun densities exceed plasma spray ceramics. |

Application: Barlow SemiBold, 16 pt, accent color.
Details: Inter Regular, 12 pt, `#F0EDE8`.

**Right -- Common Defects (X: 12.5", W: 11.0")**

Section label: `COMMON DEFECTS` Y: 22.2".

**BLOCK F -- Defect Cards (stacked)**

Y: 22.8" to 32.0". Five defect cards.

| Defect | Color | Cause | Fix |
|---|---|---|---|
| POROSITY (spots not dense) | `#E05C5C` | Insufficient velocity; poor gas ratios; excessive standoff | Verify O2/C2H2 ratio; reduce standoff; check barrel condition |
| DECARBURIZATION (low hardness) | `#E05C5C` | O2/C2H2 ratio too rich; excessive particle temperature | Use lean ratio (1.1--1.5); verify gas metering calibration |
| UNEVEN THICKNESS | `#E8A020` | Inconsistent spot overlap; robot path error; varying standoff | Reprogram traverse; verify robot calibration; check fixture |
| SUBSTRATE OVERHEATING | `#E8A020` | Frequency too high; insufficient cooling; too many passes | Reduce frequency; increase cooling air; add pause between passes |
| POOR ADHESION | `#E05C5C` | Surface contamination; stale grit blast; excessive time to spray | Re-blast; verify cleanliness; reduce clean-to-spray time |

Each card: H: 1.7", fill `#1E2435`, left accent defect color.
Defect: Barlow SemiBold, 14 pt, defect color.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Fix: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Spray Application -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The spot-overlap concept is the unique visual story for D-Gun spray application. Every other thermal spray process deposits a continuous stream of particles; D-Gun deposits discrete spots that overlap like tiles. This pulsed deposition creates the "intermittent heat advantage" that allows D-Gun to coat heat-sensitive parts with minimal thermal distortion. The WC-12Co benchmark table is the data anchor -- operators and engineers will compare D-Gun to HVOF and see that D-Gun wins on every quality metric but loses on throughput. The decarburization defect (O2/C2H2 ratio too rich destroying WC grains) deserves coral treatment because it is the most common way to ruin an expensive D-Gun WC-Co coating.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #536 -- Construction Workup v1.0*
*2026-04-26*
