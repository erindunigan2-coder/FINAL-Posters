---
Project: Plating Posters Inc
Poster Number: 70
Title: "Post Treatment -- Nickel Sulfamate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-05 technical reference (Sulfamate nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Post-treatment for sulfamate nickel -- grinding/machining for buildup, mandrel separation for electroforming, HE bake if applicable, and final inspection (thickness, stress, hardness). This is the most application-diverse post-treatment in the series.
Process Scope: Post-treatment for sulfamate nickel plating (Stages 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Sulfamate
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP05
---

# Poster #70 -- Construction Workup
## Post Treatment -- Nickel Sulfamate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8. Sulfamate nickel post-treatment is the most application-diverse in the series. Where Watts nickel almost always goes to chrome, and Zn-Ni almost always goes to passivation, sulfamate nickel exits the bath into three fundamentally different paths:

1. **Buildup / Salvage:** Grind or hone to final dimension. The deposit replaces lost material.
2. **Electroforming:** Separate the nickel shell from the mandrel. The deposit IS the part.
3. **Engineering coating:** May be the final surface, or receive a topcoat (chrome, passivate).

All three paths share the same inspection requirements (thickness, stress, hardness) and the same HE bake obligation for high-strength steel substrates.

Hero visual: three-path decision tree showing the post-treatment route by application.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-path decision tree hero (Block B):** Buildup vs. Electroforming vs. Engineering Coating.
2. **Grinding/machining callout (Block C):** Dimensional restoration specs.
3. **Electroforming separation callout (Block D):** Mandrel release methods.
4. **HE bake requirements (Block E):** Same as Watts -- ASTM B850.
5. **Inspection requirements table (Block F):** Thickness, stress, hardness, adhesion.
6. **Applicable specifications (Block G).**
7. **Orientation strip:** Stages 7--8 highlighted (Amber).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.0" / 19.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--8 highlighted (Amber)
ZONE 3 -- THREE-PATH DECISION TREE HERO (4.2"--13.0" / ~8.8")
  Block B: Decision tree -- buildup vs. electroforming vs. engineering
  Block C: Grinding/machining callout
  Block D: Electroforming separation callout
ZONE 4 -- HE BAKE + INSPECTION (13.0"--19.5" / ~6.5")
  Block E: HE bake requirements
  Block F: Inspection requirements table
ZONE 5 -- COMMON FAILURES (19.5"--26.5" / ~7.0")
  Block F2: Common post-treatment failures
ZONE 6 -- SPECIFICATIONS + SAFETY (26.5"--32.5" / ~6.0")
  Block G: Applicable specifications
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 80 pt `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Sulfamate) -- Stages 7--8 of 8 -- Grind, Release, Inspect` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Three applications, three post-treatment paths. Buildup gets ground. Electroforms get released. All get inspected.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stages 7--8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated sulfamate Ni deposit  -->  After: Finished part -- ground, released, or inspected per specification`

---

### ZONE 3 -- Three-Path Decision Tree Hero

**Section label:** `POST-TREATMENT BY APPLICATION` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Three-Path Decision Tree**

Y: 5.0" to 8.0". Three callout boxes side by side.

Path 1 -- `BUILDUP / SALVAGE` (X: 0.5", W: 7.0", H: 2.5"):
- Fill `#1E2435`, left accent `#27AE60`
- Title: `BUILDUP / SALVAGE` Barlow SemiBold 18 pt `#27AE60`
- Body (Inter Regular 13 pt `#F0EDE8`):
  - `Purpose: Dimensional restoration of worn parts`
  - `Post-plate: Grind or hone to final dimension`
  - `Typical build: 5--50 mil (0.13--1.27 mm)`
  - `Examples: Hydraulic rods, shafts, bearing journals`

Path 2 -- `ELECTROFORMING` (X: 8.25", W: 7.0", H: 2.5"):
- Fill `#1E2435`, left accent `#E8A020`
- Title: `ELECTROFORMING` Barlow SemiBold 18 pt `#E8A020`
- Body:
  - `Purpose: Create a free-standing nickel shell`
  - `Post-plate: Separate deposit from mandrel`
  - `Typical build: 10--200+ mil (0.25--5+ mm)`
  - `Examples: Waveguides, mold inserts, CD masters`

Path 3 -- `ENGINEERING COATING` (X: 16.0", W: 7.5", H: 2.5"):
- Fill `#1E2435`, left accent `#2EC4B6`
- Title: `ENGINEERING COATING` Barlow SemiBold 18 pt `#2EC4B6`
- Body:
  - `Purpose: Functional surface layer`
  - `Post-plate: Inspect as-plated or topcoat`
  - `Typical build: 2--50 mil (0.05--1.27 mm)`
  - `Examples: Aerospace fittings, electronic shields`

**BLOCK C -- Grinding/Machining Callout**

Y: 8.5" to 10.5".

Rounded rect, W: 11.0", X: 0.5", fill `#1E2435`, left accent `#27AE60`.
Title: `GRINDING SULFAMATE NICKEL` Barlow SemiBold 16 pt `#27AE60`
Body (JetBrains Mono 13 pt `#F0EDE8`):
```
Deposit hardness: 150--250 HV (as-plated, no brighteners)
Grinding: Conventional Al2O3 or SiC wheels adequate
Surface finish: 8--32 microinch Ra typical
Tolerance: +/- 0.0002" achievable with precision grinding
Note: Sulfamate Ni is softer than hard chrome (800--1000 HV)
      but much more ductile -- no microcracking risk
```

**BLOCK D -- Electroforming Separation Callout**

Y: 8.5" to 10.5" (right side, X: 12.0", W: 11.5").

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `MANDREL SEPARATION` Barlow SemiBold 16 pt `#E8A020`
Body (Inter Regular 13 pt `#F0EDE8`):
- `Chemical release: dissolve or etch mandrel (aluminum mandrels in NaOH)`
- `Mechanical release: precision pull from taper mandrels`
- `Thermal differential: heat or cool to exploit CTE difference`
- `Release agents: applied to mandrel before plating (proprietary)`
- `CRITICAL: Near-zero stress is what makes separation possible without distortion`

Below both callouts (Y: 11.0" to 12.8"):

**Inspection Requirements Teaser:**

Rounded rect, full width, H: 1.5", fill `#27AE60` at 10%, border 1 pt `#27AE60`.
Text: `ALL THREE PATHS converge at inspection. Thickness, stress, and adhesion must be verified regardless of application.` Barlow SemiBold 16 pt `#27AE60`.

---

### ZONE 4 -- HE Bake + Inspection

**Section label:** `HYDROGEN EMBRITTLEMENT BAKE AND INSPECTION` -- Y: 13.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- HE Bake Requirements**

Y: 13.8" to 16.5".

Rounded rect, fill `#1E2435`, border 2 pt `#E05C5C`, W: 23.0".
Title: `HE BAKE -- SAME REQUIREMENTS AS WATTS NICKEL` Barlow SemiBold 18 pt `#E05C5C`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Required for high-strength steel substrates (>= 31 HRC) per ASTM B850.`
- `Temperature: 375 +/- 25 F (190 +/- 14 C)`
- `Timing: Within 4 hours of plating (general); within 1 hour (some aerospace specs)`
- `Duration: 8--24 hours depending on hardness class`
- `Note: Sulfamate Ni generates LESS hydrogen than acid baths (cathode efficiency 95--100%), but the bake requirement is the same for high-strength substrates.`
- `Electroforming on mandrels: HE bake is NOT applicable (mandrels are not structural).`

**BLOCK F -- Inspection Requirements Table**

Y: 17.0" to 19.3".

| Inspection | Method | Frequency | Spec Reference |
|---|---|---|---|
| Thickness | XRF, beta backscatter, or micrometer | Every lot | ASTM B504 |
| Deposit stress | Contractometer or stress strip | Per setup + daily | AMS 2424 |
| Hardness | Vickers or Knoop micro-hardness | Per lot or as required | ASTM E384 |
| Adhesion | Bend test, thermal shock, or tape test | Per lot | ASTM B571 |
| Visual | Magnified inspection (10--30x) for pitting, roughness | Every part | |

Data: JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 5 -- Common Failures

**Section label:** `WHAT GOES WRONG AT POST-TREATMENT` -- Y: 19.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F2 -- Common Post-Treatment Failures**

Y: 20.3" to 26.3".

| Failure | Root Cause | Result |
|---|---|---|
| Cracking during grinding | Excessive tensile stress in deposit | Part scrapped; review stress control in bath |
| Electroform distortion | Stress too high for mandrel separation | Shell warps on release; stress reducer needed |
| HE failure in service | Bake skipped or delayed on high-strength steel | Delayed brittle fracture; catastrophic |
| Under-thickness | Plating time or CD too low; poor current distribution | Part out of spec; re-plate or scrap |
| Over-thickness | Plating time too long | Excessive grinding; dimensional risk |
| Adhesion failure | Inadequate activation or Wood's strike | Deposit lifts during grinding or in service |
| Surface roughness | Particulates in bath; poor filtration | Requires extra grinding; reduces yield |

Cards: fill `#1E2435`, alternating `#252B3D`. Failure: `#E05C5C`. Root Cause: `#F0EDE8`. Result: `#E8A020`.

---

### ZONE 6 -- Specifications + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Applicable Specifications (X: 0.5", W: 14.0"):**

Section label: `APPLICABLE SPECIFICATIONS` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Specification | Coverage |
|---|---|
| AMS 2403 | Nickel plating (general -- Watts and sulfamate) |
| AMS 2424 | Nickel plating, low-stressed-deposit (sulfamate-specific) |
| AMS-QQ-N-290 | Nickel plating (federal) |
| ASTM B689 | Electrodeposited nickel |
| MIL-STD-1501 | Electroforming |
| ASTM B850 | HE relief baking |
| ASTM B504 | Thickness by coulometric method |

Data: JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Grinding nickel: generates nickel dust (respiratory hazard, IARC Group 1 for Ni compounds). Use local exhaust ventilation and P100 respirator.
> - HE bake oven: burn hazard at 375 F. Lockout/tagout for maintenance.
> - Mandrel dissolution (NaOH for Al mandrels): caustic burn hazard.
> - Nickel dust: combustible in fine powder form. Manage accumulation.
> - PPE: respirator for grinding; heat-resistant gloves for oven.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Nickel Sulfamate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Post-treatment parameters shown are typical industry values. Specific inspection requirements and tolerances are determined by the applicable specification and customer drawing. Consult your process supplier and specification for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #63).
**Export:** Six files -- `Post Treatment Nickel Sulfamate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-path decision tree is the unique feature of this poster. No other post-treatment poster in the series has this structure because most plating processes have a single dominant post-treatment path. Sulfamate nickel genuinely serves three different application families, and each has a fundamentally different post-treatment workflow.

The stress connection is threaded throughout: near-zero stress is why electroforming separation works without distortion, why grinding doesn't cause cracking, and why the deposit survives fatigue loading in engineering applications. This poster closes the loop on the stress story that started in Poster #68.

Watson's brief: "Electroforming: Mandrel is separated from deposit (chemical, mechanical, or thermal differential). Engineering coatings: May be used as-plated, or ground/lapped to final dimension. HE baking: Required for high-strength steel per ASTM B850."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #70 -- Construction Workup v1.0*
*2026-04-26*
