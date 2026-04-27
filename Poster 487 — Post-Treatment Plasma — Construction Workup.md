---
Project: Plating Posters Inc
Poster Number: 487
Title: "Post-Treatment -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 9)"
Technical Source: APS post-treatment including sealing (epoxy, silicone, phenolic, aluminum phosphate), grinding/machining (diamond for ceramics, CBN for metals), and diffusion heat treatment for MCrAlY bond coats.
Process Scope: Atmospheric plasma spray -- post-spray sealing, grinding, and heat treatment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - PostTreatment
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #487 -- Construction Workup
## Post-Treatment -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of the APS process. Once the coating is on, what happens next? Sealing fills porosity, grinding achieves final dimensions, and heat treatment (when specified) creates diffusion bonds. Three distinct post-treatment paths depending on the application.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-path decision tree (Block B -- HERO):** Seal, Grind, or Heat Treat -- with decision logic.
2. **Sealer selection table (Block C):** 5 sealer types with temperature ratings and applications.
3. **Grinding specification table (Block D):** Wheel types, speeds, and achievable finishes.
4. **Heat treatment callout (Block E):** MCrAlY diffusion treatment details.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber)
ZONE 3 -- THREE-PATH DECISION HERO (4.2"--14.5" / ~10.3")
  Block B: Decision tree -- Seal / Grind / Heat Treat
ZONE 4 -- SEALER SELECTION (14.5"--20.5" / ~6.0")
  Block C: 5-row sealer table
ZONE 5 -- GRINDING SPEC (20.5"--26.5" / ~6.0")
  Block D: Grinding parameters and achievable finishes
ZONE 6 -- HEAT TREATMENT (26.5"--32.5" / ~6.0")
  Block E: MCrAlY diffusion heat treatment
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- Seal, Grind, Heat Treat -- Stage 9 of 10` -- 32 pt `#E8A020`. Y: 1.4".
**Tagline:** `The coating is on. Now make it perform. Seal the porosity. Grind to dimension. Heat treat to bond.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted (Amber). Others dimmed.

---

### ZONE 3 -- Three-Path Decision Tree (HERO)

**Section label:** `POST-TREATMENT PATHS -- CHOOSE BY APPLICATION` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Y: 5.0" to 14.3". Three large vertical path cards side by side.

Each path card: Rounded rect, W: 7.33", H: 9.0", fill `#1E2435`, radius 6, top accent 4 pt.

**Path 1 -- SEAL (X: 0.5")**
- Accent: `#2EC4B6`
- Title: `SEAL` Barlow Condensed ExtraBold 28 pt `#2EC4B6`
- When: `Porous coatings that need corrosion or wear protection`
- Method: `Vacuum impregnation (epoxy, silicone, phenolic, AlPO4)`
- Key detail: `Fills interconnected porosity; does not change dimensions`
- Applications: `Wear coatings in corrosive environments; hydraulic seals`
- Caution: `Epoxy max: ~200 degC. AlPO4 for high-temp (800+ degC)`

**Path 2 -- GRIND (X: 8.0")**
- Accent: `#E8A020`
- Title: `GRIND` Barlow Condensed ExtraBold 28 pt `#E8A020`
- When: `Final dimensions or surface finish required by drawing`
- Method: `Diamond grinding (ceramics); CBN or SiC (metals)`
- Key detail: `Coolant required -- thermal shock cracks coatings`
- Applications: `All dimensional parts; bearing surfaces; seal surfaces`
- Achievable: `Ra 0.2-1.6 um; stock removal 50-200 um typical`

**Path 3 -- HEAT TREAT (X: 15.5")**
- Accent: `#E05C5C`
- Title: `HEAT TREAT` Barlow Condensed ExtraBold 28 pt `#E05C5C`
- When: `MCrAlY bond coats requiring diffusion bond to substrate`
- Method: `Vacuum furnace, 1050-1080 degC, 2-4 hours`
- Key detail: `Creates metallurgical bond; not standard for ceramic topcoats`
- Applications: `Turbine components with TBC systems`
- Caution: `High temp exceeds capability of many substrates; verify compatibility`

Interior per card:
- Title: top, centered
- "When:" label: Inter Medium 14 pt `#F0EDE8` at 60%. Value: Inter Regular 14 pt `#F0EDE8`.
- "Method:" same styling
- Key detail: Inter Medium 14 pt, accent color
- Applications: Inter Regular 13 pt `#F0EDE8`
- Caution line: Inter Medium 12 pt `#E05C5C`

---

### ZONE 4 -- Sealer Selection Table

**Section label:** `SEALER SELECTION GUIDE` -- Y: 14.7".

**BLOCK C -- 5-Row Sealer Table**

| Sealer Type | Max Temp | Method | Best For | Limitations |
|---|---|---|---|---|
| Epoxy | ~200 degC | Vacuum impregnation | General wear/corrosion; standard industrial | Temperature limited |
| Silicone | ~250 degC | Brush or spray | Higher temp service | Less chemical resistance than epoxy |
| Phenolic | ~250 degC | Vacuum impregnation | Chemical resistance applications | Brittle; limited thermal cycling |
| Aluminum phosphate | ~800 degC | Inorganic ceramic sealer | High-temperature service (turbine parts) | Expensive; specialized process |
| Laser glazing | Surface densification | Laser beam | Research/specialty; maximum density | Not widely available; cost |

---

### ZONE 5 -- Grinding Specification

**Section label:** `GRINDING APS COATINGS -- DO NOT THERMAL SHOCK` -- Y: 20.7".

**BLOCK D -- Grinding Parameters**

| Coating Type | Wheel | Surface Speed | Infeed | Coolant | Achievable Ra |
|---|---|---|---|---|---|
| Alumina (Al2O3) | Diamond (resin bond) | 20-30 m/s | 5-15 um/pass | Required | 0.2-0.8 um |
| Chrome oxide (Cr2O3) | Diamond (resin bond) | 20-30 m/s | 5-10 um/pass | Required | 0.2-0.8 um |
| Zirconia (YSZ) | Diamond (resin bond) | 20-30 m/s | 5-15 um/pass | Required | 0.4-1.6 um |
| Metallic (NiCr, MCrAlY) | CBN or SiC | 25-35 m/s | 10-20 um/pass | Required | 0.2-1.0 um |

Callout: `COOLANT IS MANDATORY. Dry grinding generates thermal shock that cracks ceramic coatings and creates subsurface damage invisible to the eye but fatal in service.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 6 -- Heat Treatment

**Section label:** `DIFFUSION HEAT TREATMENT -- MCrAlY BOND COATS` -- Y: 26.7".

**BLOCK E -- Heat Treatment Callout**

Two-column layout:

**Left -- Specification:**
- `Atmosphere: Vacuum (< 10^-4 torr)` JetBrains Mono 14 pt
- `Temperature: 1050-1080 degC` JetBrains Mono 14 pt `#E05C5C`
- `Time: 2-4 hours at temperature` JetBrains Mono 14 pt
- `Cooling: Furnace cool or controlled gas quench` JetBrains Mono 14 pt

**Right -- Purpose and Notes:**
- `Creates interdiffusion zone between bond coat and substrate`
- `Improves oxidation resistance of TBC system`
- `Not required for single-layer metallic or ceramic coatings`
- `Verify substrate can tolerate 1050+ degC without property degradation`

---

### ZONE 7 -- Footer

Standard. Title: `Post-Treatment -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post-Treatment Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-path decision tree is the unique teaching tool here. Not every coating gets all three treatments -- the operator needs to know which path applies to their specific job. The "coolant is mandatory" callout for grinding is critical: thermal shock failure of ceramic coatings is a real and expensive problem that many shops learn the hard way.

---

*Alaina -- Poster #487 -- Construction Workup v1.0 -- 2026-04-26*
