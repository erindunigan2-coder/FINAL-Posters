---
Project: Plating Posters Inc
Poster Number: 546
Title: "Spray Application -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS application is a two-step process -- conventional APS bond coat (MCrAlY, 75--150 um) followed by SPS topcoat (YSZ, 100--400 um). The topcoat builds in very thin passes (2--10 um/pass) and forms columnar microstructure naturally via surface shadowing effects. Substrate temperature runs 200--400 degC due to closer standoff -- cooling is critical.
Process Scope: SPS spray application technique, coating buildup, and microstructure formation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #546 -- Construction Workup
## Spray Application -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the core SPS poster -- the actual spraying. Two stages: conventional APS bond coat first, then SPS topcoat. The microstructure story is the hero -- columnar structures forming via surface shadowing at the nanoscale, producing EB-PVD-like TBCs without a vacuum chamber. The three-way comparison table (SPS vs. APS vs. EB-PVD) is the showpiece for anyone evaluating the technology.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- TWO-STEP APPLICATION / HERO (2.9"--15.5")
  Block B: Bond coat (APS) + topcoat (SPS) two-step sequence
  Block C: Coating buildup parameters
ZONE 3 -- MICROSTRUCTURE (15.5"--22.0")
  Block D: Columnar structure explanation and formation mechanism
  Block E: SPS vs. APS vs. EB-PVD comparison table
ZONE 4 -- COATING PROPERTIES (22.0"--28.5")
  Block F: YSZ SPS topcoat property table
  Block G: Application technique notes
ZONE 5 -- COMMON DEFECTS (28.5"--32.5")
  Block H: 4 defect cards with causes and fixes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Suspension Plasma Spray (SPS) -- Bond Coat + Columnar Topcoat` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Two steps. First, a conventional APS bond coat. Then the SPS topcoat -- submicron particles building columns pass by pass. EB-PVD performance without the vacuum chamber.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Two-Step Application (HERO)

**Section label:** `APPLICATION SEQUENCE -- BOND COAT + SPS TOPCOAT` -- Y: 3.1".

**BLOCK B -- Two-Step Sequence**

Y: 3.8" to 11.5". Two large step panels side by side with arrow connector.

*Left panel -- STEP 1: APS Bond Coat (X: 0.5", W: 11.0", H: 7.5"):*

Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt.

Badge: `STEP 1` rounded rect 1.2" x 0.4", fill `#E8A020`, text `#1A1F2E` Barlow Condensed ExtraBold 14 pt.

Title: `APS BOND COAT` -- Barlow SemiBold 24 pt `#F0EDE8`.
Subtitle: `Conventional APS -- Not SPS` -- Inter Medium 14 pt `#E8A020`.

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Material: MCrAlY or NiCrAlY
Thickness: 75--150 um
Method: Standard APS parameters
Purpose: Oxidation barrier + topcoat adhesion
```

Note: `Bond coat is applied by conventional APS powder spray -- NOT by SPS. Standard APS equipment and parameters apply.` Inter Medium 13 pt `#E8A020`.

*Right panel -- STEP 2: SPS Topcoat (X: 12.0", W: 11.5", H: 7.5"):*

Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt.

Badge: `STEP 2` rounded rect 1.2" x 0.4", fill `#27AE60`, text `#1A1F2E`.

Title: `SPS TOPCOAT` -- Barlow SemiBold 24 pt `#F0EDE8`.
Subtitle: `The Core SPS Step -- Columnar TBC` -- Inter Medium 14 pt `#27AE60`.

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Material: YSZ suspension (7--8 wt% Y2O3)
Solids loading: 5--30 wt% in ethanol or water
Thickness per pass: 2--10 um
Total thickness: 100--400 um
Standoff: 40--80 mm
Substrate temp: 200--400 degC
```

Note: `Columnar structure forms naturally via surface shadowing of fine splats. Do NOT attempt to force lamellar deposition.` Inter Medium 13 pt `#27AE60`.

*Arrow connector between panels:*
- Stroke: 3 pt `#3A4055`, arrowhead filled right
- Y: centered (~7.5")

**BLOCK C -- Coating Buildup Summary**

Y: 12.0" to 15.3". Rounded rect, W: 23.0", H: 3.0", fill `#252B3D`.

Three key metrics in a horizontal strip:

| Metric | Value | Color |
|---|---|---|
| Total System Thickness | `Bond coat 75--150 um + SPS topcoat 100--400 um = 175--550 um total` | `#F0EDE8` |
| Passes Required | `SPS topcoat: 10--200 passes at 2--10 um/pass` | `#2EC4B6` |
| Substrate Temperature | `200--400 degC during SPS -- cooling is CRITICAL` | `#E05C5C` |

Each metric: JetBrains Mono 16 pt for value, Inter Medium 13 pt for label.

---

### ZONE 3 -- Microstructure

**Section label:** `COLUMNAR MICROSTRUCTURE -- THE SPS ADVANTAGE` -- Y: 15.7".

**Left -- BLOCK D: Formation Mechanism (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `HOW COLUMNS FORM` -- Barlow SemiBold 20 pt `#27AE60`.

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

```
1. Submicron particles deposit as very fine splats
2. Surface roughness creates shadowing effects
3. Peaks receive more material than valleys
4. Preferential growth builds vertical columns
5. Inter-columnar gaps (porosity) form naturally
6. Columns are 50--200 um wide with 5--15% porosity
```

Bottom callout: `Column gaps provide strain tolerance -- columns flex independently during thermal cycling, preventing catastrophic delamination` Inter Medium 13 pt `#27AE60`.

**Right -- BLOCK E: Three-Way Comparison (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`.

Title: `SPS vs. APS vs. EB-PVD` -- Barlow SemiBold 18 pt `#F0EDE8`.

| Property | SPS | APS | EB-PVD |
|---|---|---|---|
| Microstructure | Columnar | Lamellar | Columnar |
| Porosity | 10--25% | 10--20% | 15--25% |
| Thermal conductivity | 0.7--1.2 W/mK | 0.8--1.2 W/mK | 1.5--2.0 W/mK |
| Strain tolerance | HIGH | LOW | HIGH |
| Bond strength | > 15 MPa | > 10 MPa | > 20 MPa |
| Cost | Medium | Low | Very High |
| Vacuum required | No | No | Yes |

Data: JetBrains Mono 11 pt. SPS column highlighted with `#27AE60` at 10%.

Bottom: `SPS delivers EB-PVD-class performance at APS-class cost` Inter Medium 14 pt `#27AE60`.

---

### ZONE 4 -- Coating Properties

**Section label:** `YSZ SPS TOPCOAT PROPERTIES` -- Y: 22.2".

**Left -- BLOCK F: Property Table (X: 0.5", W: 11.0"):**

| Property | SPS YSZ Topcoat |
|---|---|
| Porosity | 10--25% (intentional) |
| Thermal conductivity | 0.7--1.2 W/mK |
| Microhardness | 600--900 HV |
| Bond strength (on bond coat) | > 15 MPa |
| Column width | 50--200 um |
| Inter-columnar gap | 5--15% porosity |
| Thermal cycling life | > 1000 cycles (1100 degC target) |
| Phase | Tetragonal prime ZrO2 (must verify by XRD) |

Data: JetBrains Mono 12 pt.

**Right -- BLOCK G: Application Notes (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `TECHNIQUE NOTES` -- Barlow SemiBold 20 pt `#E8A020`.

Bullet list (Inter Regular 14 pt):
- `Apply SPS directly over APS bond coat -- no delay needed`
- `Maintain constant standoff (40--80 mm) -- critical for column formation`
- `Cooling air jets on substrate backside -- mandatory`
- `Monitor substrate temp continuously -- max 400 degC`
- `Do NOT preheat for SPS step (bond coat is already warm)`
- `Robot traverse must be consistent -- manual SPS is not practical`
- `Columnar structure is sensitive to standoff variation`

---

### ZONE 5 -- Common Defects

**Section label:** `APPLICATION DEFECTS -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK H -- Four Defect Cards**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | LAMELLAR MICROSTRUCTURE | Standoff too far; particles too large; power too low | Reduce standoff; verify suspension particle size; increase power |
| 2 | 6.33" | DELAMINATION FROM BOND COAT | Contaminated bond coat; excessive time between APS and SPS | Spray SPS promptly after bond coat; minimize handling |
| 3 | 12.16" | SUBSTRATE OVERHEATING | Close standoff + slow traverse; insufficient cooling | Increase traverse speed; increase cooling air; monitor temp |
| 4 | 18.0" | UNEVEN THICKNESS | Inconsistent traverse speed or standoff; robot programming error | Verify robot path; calibrate standoff; run test coupons |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard. Title: `Spray Application -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

Disclaimer: `SPS coating properties and microstructure are highly sensitive to parameter selection. Values shown are representative of YSZ TBC applications. Consult your coating supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #546 -- Construction Workup v1.0 -- 2026-04-26*
