---
Project: Plating Posters Inc
Poster Number: 478
Title: "Inspection & QA -- Electroforming"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 478 — Inspection and QA Electroforming — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Electroforming
  - Inspection
  - QualityAssurance
  - SpecialtyAdvanced
  - ClusterSA08
  - v1
---

# Claude Chat Generation Prompt -- Poster #478
## Inspection & QA -- Electroforming
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION & QA` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Electroforming -- Testing the Deposit That IS the Part` -- `32` pt `#2EC4B6`. Y: **1.5"**.
### Step 3 -- `In electroplating, you test whether the coating protects the part. In electroforming, you test whether the deposit IS a good part. Every deposit property is a product property.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted. Inspection stage highlighted (Teal).

---

## Phase 4 -- Inspection Method Matrix Hero

Y: 4.2" to 14.5". Section label: `QUALITY INSPECTION METHODS`.

Eight panels in 2x4 grid:

**Row 1:**

| Panel | Title | Accent | Methods | Target |
|---|---|---|---|---|
| THICKNESS | `THICKNESS` | `#E8A020` | Micrometer, ultrasonic, cross-section microscopy | +/- 10-15% nominal; check edges vs. center |
| STRESS | `STRESS` | `#E05C5C` | Spiral contractometer, strip deflection, X-ray diffraction | < 35 MPa tensile (ASTM B832); ideal near-zero |
| HARDNESS | `HARDNESS` | `#27AE60` | Vickers microhardness (100-500 gf) | No additives: 150-250 HV; with reducers: 300-500 HV; after anneal: 150-180 HV |
| DUCTILITY | `DUCTILITY` | `#2EC4B6` | Tensile test on companion coupon | Elongation > 10% (as-dep), > 20% (annealed); UTS 400-700 MPa |

**Row 2:**

| Panel | Title | Accent | Methods | Target |
|---|---|---|---|---|
| INTERIOR SURFACE | `INTERIOR SURFACE` | `#E8A020` | Profilometer (stylus/optical); visual under oblique light | Optical: Ra < 0.01 um; general: Ra < 0.2 um; should match mandrel Ra |
| POROSITY | `POROSITY` | `#E05C5C` | Ferroxyl test (K3Fe(CN)6 + NaCl); bend test; pressurized leak test | No through-porosity above min wall (usually > 50 um) |
| DIMENSIONS | `DIMENSIONS` | `#27AE60` | CMM; fixture gauges | ID: +/- 0.005-0.025 mm (mandrel precision); OD: per machining tolerance |
| SULFUR | `SULFUR` | `#2EC4B6` | Combustion analysis (LECO) on companion coupon | General: < 0.1%; elevated temp: < 0.03%; aerospace: < 0.02% |

---

## Phase 5 -- Common Defects Table

Y: 14.5" to 22.0". Section label: `COMMON ELECTROFORMING DEFECTS`.

| Defect | Appearance | Cause | Prevention |
|---|---|---|---|
| Pitting | Pits on interior | H2 bubbles; contamination; low pH | Wetting agent; agitation; pH > 3.5; carbon treat |
| Burning | Dark, rough at edges | CD too high; Ni low; pH high | Reduce CD; maintain Ni; shields |
| High stress / cracking | Cracks; curling | Contamination; saccharin depleted; CD high | Carbon treat; saccharin; reduce CD; increase temp |
| Poor separation | Stuck to mandrel | Release agent failed | Fresh release every cycle |
| Non-uniform thickness | Thick edges, thin center | Poor current distribution | Conforming anodes; shields; thieves |
| Lamination | Visible layers in cross-section | Power interruption; chemistry excursion | UPS; automated monitoring |
| Rough deposit (nodules) | Bumpy exterior | Particles; anode sludge | Filtration; anode bags; carbon treat |
| Brittle deposit | Fails bend/tensile | Metallic contamination; organic decomposition | Hull cell; dummy plate + carbon treat |

---

## Phase 6 -- Dimensional Verification + Application Criteria + Documentation

Y: 22.0" to 32.5".

**Left -- DIMENSIONAL VERIFICATION (`#27AE60`):**

```
CMM inspection against engineering drawing.
KEY DIMENSIONS:
- ID (interior): mandrel precision. Multiple cross-sections.
- OD (exterior): machining tolerance. 8+ points.
- Features: holes, slots, mounting surfaces.

TOLERANCE STACK:
  Mandrel accuracy + deposit variation + machining tolerance + anneal change = total.

DOCUMENTATION: CMM report with 3D deviation map. FAI for new mandrels/recipes.
```

**Right -- ACCEPTANCE BY APPLICATION:**

| Application | Critical Tests | Key Spec |
|---|---|---|
| Waveguides (aerospace) | Thickness, interior Ra, dimensions, S | MIL/ASTM B832; S < 0.02% |
| Printing dies/holograms | Interior detail; hardness | Visual + optical comparison |
| Screens/meshes | Hole size/pitch; porosity | Optical; leak test |
| Mold inserts | Hardness (Ni-Co); interior finish | > 300 HV; Ra per spec |
| Reflectors/optics | Interior Ra < 0.01 um; no pits | Profilometry + interferometry |
| General industrial | Thickness, stress, hardness, dimensions | ASTM B832 |

**Batch Documentation Checklist (Y: 28.5" to 32.5"):** Section label in `#E8A020`.

```
Left column:                              Right column:
[ ] Batch/job number and date             [ ] Thickness measurements (multiple points)
[ ] Mandrel ID and type                   [ ] Stress measurement
[ ] Bath chemistry records                [ ] Hardness test results
[ ] CD, temperature, pH log               [ ] Ductility (if required)
[ ] Total amp-hours + calculated thickness [ ] Interior surface (Ra + visual)
[ ] Separation method and observations     [ ] Dimensional inspection (CMM)
[ ] Post-processing records               [ ] Sulfur analysis (if elevated temp)
                                          [ ] Final disposition: ACCEPT/REJECT/MRB
                                          [ ] Operator and QA signatures
```

**Bottom callout:** `Electroformed parts for aerospace and defense require full traceability from mandrel fabrication through final inspection. Every parameter, every measurement, every decision -- documented.`

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- Electroforming`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B832 -- Standard Guide for Electroforming with Nickel; ASM Handbook Vol. 5. Acceptance criteria are application-specific. Consult your quality engineer for site-specific requirements.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] Eight-method inspection grid (2x4)
- [ ] Common defects table with 8 entries
- [ ] Application-specific acceptance criteria
- [ ] Batch documentation checklist
- [ ] Traceability callout
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection QA Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
