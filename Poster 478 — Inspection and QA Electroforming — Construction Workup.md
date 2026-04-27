---
Project: Plating Posters Inc
Poster Number: 478
Title: "Inspection & QA -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.7-8.8)"
Technical Source: Electroforming inspection and quality assurance -- thickness uniformity, internal stress measurement, hardness, ductility, surface roughness (interior), porosity testing, dimensional accuracy (CMM), sulfur content, and visual inspection. Electroforming QA is unique because the part IS the deposit -- every property of the electrodeposit is a property of the final product.
Process Scope: Electroforming inspection and quality assurance (Stage 10 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #478 -- Construction Workup
## Inspection & QA -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of 10. The final gate for the electroforming cluster. Unlike electroplating QA (where you test whether the coating is adequate on a substrate), electroforming QA tests whether the deposit itself is a satisfactory structural part. Thickness, stress, hardness, ductility, porosity, dimensional accuracy, and sulfur content all matter. The interior surface -- replicated from the mandrel -- gets special attention because it is often the functional surface (reflector, waveguide, mold cavity).

Hero visual: comprehensive quality inspection matrix with eight test methods.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection method matrix (Block B -- HERO):** Eight-method grid covering all key QA tests.
2. **Common defects table (Block C):** Eight defects with cause, appearance, and disposition.
3. **Dimensional verification (Block D):** CMM and fixture gauging.
4. **Acceptance criteria by application (Block E):** Different standards for different industries.
5. **Batch documentation checklist (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Inspection stage highlighted (Teal)
ZONE 3 -- INSPECTION METHOD MATRIX HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- COMMON DEFECTS (14.5"--22.0" / ~7.5")
ZONE 5 -- DIMENSIONAL + APPLICATION CRITERIA (22.0"--28.5" / ~6.5")
ZONE 6 -- BATCH DOCUMENTATION (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Testing the Deposit That IS the Part` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `In electroplating, you test whether the coating protects the part. In electroforming, you test whether the deposit IS a good part. Every deposit property is a product property.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Inspection stage highlighted (Teal). Others dimmed.
Below: `Before: Post-processing complete (Stage 9) --> After: Part accepted or rejected, documented, packaged for delivery`

---

### ZONE 3 -- Inspection Method Matrix Hero

**Section label:** `QUALITY INSPECTION METHODS` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Eight-Method Grid (Y: 5.0" to 14.0")**

Two rows of four panels. Each panel: Rounded rect W: 5.5", H: 4.2", fill `#1E2435`, radius 6.

**Row 1 (Y: 5.0"):**

Panel 1 -- THICKNESS UNIFORMITY (X: 0.5"):
- Top accent 4 pt `#E8A020`
- Title: `THICKNESS` Barlow SemiBold 16 pt `#E8A020`
- Body (Inter Regular 11 pt `#F0EDE8`):
```
METHODS:
- Micrometer (mandrel dim subtracted)
- Ultrasonic thickness gauge (non-magnetic)
- Cross-section microscopy (destructive)

MEASURE AT: Multiple points across part
TARGET: +/- 10-15% of nominal (application)
CHECK: Edges vs. center (current distribution)
```

Panel 2 -- INTERNAL STRESS (X: 6.33"):
- Top accent 4 pt `#E05C5C`
- Title: `STRESS` Barlow SemiBold 16 pt `#E05C5C`
- Body:
```
METHODS:
- Spiral contractometer (during deposition)
- Strip deflection test (companion coupon)
- X-ray diffraction (post-deposition)

TARGET: < 35 MPa tensile (ASTM B832)
IDEAL: Near-zero or slightly compressive

High stress = cracking, distortion, failure
```

Panel 3 -- HARDNESS (X: 12.16"):
- Top accent 4 pt `#27AE60`
- Title: `HARDNESS` Barlow SemiBold 16 pt `#27AE60`
- Body:
```
METHOD:
Vickers microhardness (HV) on cross-section
or surface (100-500 gf load)

TYPICAL VALUES:
- Ni sulfamate (no additives): 150-250 HV
- Ni sulfamate (with stress reducers): 300-500 HV
- After anneal: 150-180 HV
- Cu electroform: 50-100 HV

Test companion coupon (non-destructive to part)
```

Panel 4 -- DUCTILITY (X: 18.0"):
- Top accent 4 pt `#2EC4B6`
- Title: `DUCTILITY` Barlow SemiBold 16 pt `#2EC4B6`
- Body:
```
METHOD:
Tensile test on companion coupon
(flat strip plated alongside part)

MEASURES:
- Elongation at break (%)
- Ultimate tensile strength (MPa)

TARGET (Ni sulfamate):
- Elongation: > 10% (as-deposited)
- Elongation: > 20% (after anneal)
- UTS: 400-700 MPa
```

**Row 2 (Y: 9.5"):**

Panel 5 -- SURFACE ROUGHNESS (X: 0.5"):
- Top accent 4 pt `#E8A020`
- Title: `INTERIOR SURFACE` Barlow SemiBold 16 pt `#E8A020`
- Body:
```
METHOD:
Profilometer (stylus or optical)
on interior (mandrel-replica) surface

TARGET: Should match mandrel Ra
- Optical quality: Ra < 0.01 um
- General industrial: Ra < 0.2 um
- Mold inserts: per mold spec

ALSO CHECK:
Visual inspection under oblique light
for pits, scratches, inclusions
```

Panel 6 -- POROSITY (X: 6.33"):
- Top accent 4 pt `#E05C5C`
- Title: `POROSITY` Barlow SemiBold 16 pt `#E05C5C`
- Body:
```
METHODS:
- Ferroxyl test (Ni): filter paper
  soaked in K3Fe(CN)6 + NaCl solution;
  blue spots = pinholes (Fe substrate
  showing through, or bare areas)
- Bend test: flex thin section; cracks
  at pinholes become visible
- Pressurized leak test: for vessels,
  waveguides, sealed parts

TYPICAL REQUIREMENT:
No through-porosity above minimum
wall thickness (usually > 50 um)
```

Panel 7 -- DIMENSIONAL ACCURACY (X: 12.16"):
- Top accent 4 pt `#27AE60`
- Title: `DIMENSIONS` Barlow SemiBold 16 pt `#27AE60`
- Body:
```
METHOD:
CMM (coordinate measuring machine)
or fixture gauges

MEASURES:
- Overall dimensions vs. drawing
- Wall thickness uniformity
- ID dimensions (replicated from mandrel)
- OD dimensions (machined)
- Concentricity, flatness, runout

TOLERANCE:
ID: typically +/- 0.005-0.025 mm
  (mandrel precision + deposit factors)
OD: per machining tolerance
```

Panel 8 -- SULFUR CONTENT (X: 18.0"):
- Top accent 4 pt `#2EC4B6`
- Title: `SULFUR` Barlow SemiBold 16 pt `#2EC4B6`
- Body:
```
METHOD:
Combustion analysis (LECO instrument)
on companion coupon

TARGET:
- General: < 0.1%
- Elevated temp applications
  (brazing, soldering): < 0.03%
- Aerospace: per spec (often < 0.02%)

WHY:
Sulfur migrates to grain boundaries
above 600 C causing catastrophic
embrittlement. If the part will see
heat, sulfur MUST be tested.
```

---

### ZONE 4 -- Common Defects

**Section label:** `COMMON ELECTROFORMING DEFECTS` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK C -- Eight-Defect Table (Y: 15.3" to 21.5")**

| Defect | Appearance | Cause | Prevention |
|---|---|---|---|
| Pitting | Visible pits on interior surface | H2 bubbles; contamination; low pH | Wetting agent; air agitation; maintain pH > 3.5; carbon treat |
| Burning | Dark, rough deposit at edges/protrusions | CD too high; Ni too low; pH too high | Reduce CD; maintain Ni; control pH; use shields |
| High stress / cracking | Cracks in deposit; curling | Contamination; saccharin depleted; CD too high; temp low | Carbon treat; replenish saccharin; reduce CD; increase temp |
| Poor separation | Deposit stuck to mandrel | Release agent failed or was skipped | Fresh release agent every cycle; verify before plating |
| Non-uniform thickness | Thick edges, thin center | Poor current distribution | Conforming anodes; shields; thieves; see Stage 5 |
| Lamination | Visible layers in cross-section | Power interruption; bath chemistry excursion | UPS for power; automated bath monitoring |
| Rough deposit (nodules) | Bumpy exterior surface | Particles in bath; anode sludge; organics | Continuous filtration; anode bags; carbon treatment |
| Brittle deposit | Fails bend or tensile test | Metallic contamination (Cu, Zn, Pb); organic decomposition | Hull cell testing; dummy plate + carbon treatment |

Header: Barlow SemiBold 10 pt, fill `#3A4055`. Data: Inter Regular 11 pt `#F0EDE8`. Alternating rows.

---

### ZONE 5 -- Dimensional + Application Criteria

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Dimensional Verification (X: 0.5", W: 11.0")**

**Section label:** `DIMENSIONAL VERIFICATION` -- Y: 22.2".

**BLOCK D -- CMM Panel (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
CMM INSPECTION:
The electroform is measured against
the engineering drawing using CMM.

KEY DIMENSIONS:
- ID (interior): controlled by mandrel
  precision. Measure at multiple cross-
  sections for roundness and taper.
- OD (exterior): controlled by machining.
  Measure wall thickness at 8+ points.
- Features: holes, slots, mounting
  surfaces machined post-separation.

TOLERANCE STACK:
  Mandrel dimensional accuracy
  + Deposit thickness variation
  + Post-machining tolerance
  + Dimensional change from anneal
  = Total part tolerance

DOCUMENTATION:
  CMM report with 3D deviation map
  attached to batch record.
  First article inspection (FAI) for
  new mandrels or new recipes.
```

**Right -- Application-Specific Criteria (X: 12.0", W: 11.5")**

**Section label:** `ACCEPTANCE BY APPLICATION` -- Y: 22.2".

**BLOCK E -- Application Table (Y: 22.8" to 28.0"):**

| Application | Critical Tests | Key Spec |
|---|---|---|
| Waveguides (aerospace) | Thickness uniformity, interior Ra, dimensions, S content | Per MIL or ASTM B832; S < 0.02% |
| Printing dies / holograms | Interior surface detail replication; hardness | Visual + optical comparison to master |
| Screens / meshes | Hole size/pitch accuracy; thickness; porosity | Optical measurement; leak test |
| Mold inserts | Hardness (may need Ni-Co); interior finish; dimensions | Hardness > 300 HV; Ra per mold spec |
| Reflectors / optics | Interior Ra (< 0.01 um); no pits, no distortion | Profilometry + interferometry |
| General industrial | Thickness, stress, hardness, dimensions | ASTM B832 |

JetBrains Mono 10 pt `#F0EDE8`. Header: Barlow SemiBold 10 pt `#3A4055`.

---

### ZONE 6 -- Batch Documentation

**Section label:** `BATCH DOCUMENTATION CHECKLIST` -- Y: 28.7". Barlow Condensed ExtraBold, 22 pt, `#E8A020`.

**BLOCK F -- Checklist (Y: 29.2" to 32.3")**

Two columns in a rounded rect, fill `#1E2435`.

Left:
```
[ ] Batch/job number and date
[ ] Mandrel ID and type
[ ] Bath chemistry records (all analyses)
[ ] Current density, temperature, pH log
[ ] Total amp-hours and calculated thickness
[ ] Separation method and observations
[ ] Post-processing records (machining, anneal)
```

Right:
```
[ ] Thickness measurements (multiple points)
[ ] Stress measurement (contractometer or strip)
[ ] Hardness test results
[ ] Ductility test results (if required)
[ ] Interior surface inspection (Ra + visual)
[ ] Dimensional inspection (CMM report)
[ ] Sulfur analysis (if elevated temp application)
[ ] Final disposition: ACCEPT / REJECT / MRB
[ ] Operator and QA signatures
```

JetBrains Mono 11 pt `#F0EDE8`.

Bottom callout:
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `Electroformed parts for aerospace and defense applications require full traceability from mandrel fabrication through final inspection. Every parameter, every measurement, every decision -- documented.` Inter Medium 13 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & QA -- Electroforming`. Version `v1.0 -- 2026`.

Disclaimer: `Source: Watson Research Brief (Cluster 8); ASTM B832 -- Standard Guide for Electroforming with Nickel; ASM Handbook Vol. 5. Acceptance criteria are application-specific. Tyler spot-check recommended for bath chemistry testing methods.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The eight-method inspection matrix as hero communicates the breadth of QA required for electroforming. Unlike decorative plating (where visual inspection and adhesion testing may suffice), electroforming demands structural testing because the deposit IS the part. The application-specific criteria table (Zone 5) acknowledges that a hologram die has completely different acceptance criteria than a waveguide shell, and operators need to know which tests matter for their specific product.

This poster closes out the Electroforming cluster. Together, Posters 469-478 cover the complete electroforming process from concept through final QA -- a body of knowledge that is remarkably under-documented in poster format despite being critical to aerospace, printing, and precision manufacturing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #478 -- Construction Workup v1.0*
*2026-04-26*
