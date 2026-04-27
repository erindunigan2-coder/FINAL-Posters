---
Project: Plating Posters Inc
Poster Number: 474
Title: "Initial Strike -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.5-8.6)"
Technical Source: Electroforming initial strike -- low-current-density start period (50-75% of full CD for 10-30 min) to ensure uniform initial nucleation across the mandrel surface. The strike establishes the foundation layer that determines the quality of the entire electroform. Rushing this step causes adhesion problems, rough starts, and non-uniform initial coverage.
Process Scope: Electroforming initial strike / low-CD start (Stage 6 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - Strike
  - Nucleation
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #474 -- Construction Workup
## Initial Strike -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 10. The mandrel is in the tank. Before ramping to full production current, a low-current-density strike period (10-30 minutes at 50-75% of full CD) ensures that the initial metal nucleation is uniform across the entire mandrel surface. This is especially critical for electroforming because the first few micrometers of deposit become the precision interior surface of the finished part -- any roughness, pitting, or non-uniformity at this stage is permanent.

Hero visual: nucleation comparison -- uniform initial coverage vs. poor coverage with visible defects.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Nucleation comparison diagram (Block B -- HERO):** Side-by-side showing good vs. poor initial nucleation on mandrel surface.
2. **Strike protocol parameters (Block C):** Current density ramp, timing, and verification.
3. **Why the strike matters (Block D):** Connection to interior surface quality.
4. **Bath condition verification (Block E):** Pre-strike chemistry checks.
5. **Common strike failures (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Strike stage highlighted (Teal)
ZONE 3 -- NUCLEATION COMPARISON HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- STRIKE PROTOCOL + WHY IT MATTERS (14.5"--22.0" / ~7.5")
ZONE 5 -- BATH CONDITION + IMMERSION TECHNIQUE (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON STRIKE FAILURES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INITIAL STRIKE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Low-Current Start for Uniform Nucleation` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The first few micrometers of deposit become the precision interior surface. Start slow. Start uniform. There are no second chances at nucleation.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `50-75%` -- 60 pt, `#E8A020`
- Label: `OF FULL CURRENT DENSITY` -- JetBrains Mono, 14 pt
- Sub-label: `For the first 10-30 minutes` -- Inter Regular, 12 pt

---

### ZONE 2 -- Sequence Orientation Strip

Strike stage highlighted (Teal). Others dimmed.
Below: `Before: Mandrel racked, anodes positioned, bath verified (Stage 5) --> After: Uniform initial deposit established, ready for full-CD build`

---

### ZONE 3 -- Nucleation Comparison Hero

**Section label:** `INITIAL NUCLEATION -- GOOD vs. POOR` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Side-by-Side Comparison (Y: 5.0" to 14.0")**

Two large panels side by side:

**Panel 1 -- GOOD NUCLEATION (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `GOOD: UNIFORM INITIAL COVERAGE` Barlow SemiBold 20 pt `#27AE60`

Surface diagram (center):
- Mandrel surface bar, fill `#3A4055`
- Uniform layer of fine metal nuclei covering entire surface, fill `#27AE60` at 40%
- Label: `Fine, uniform nucleation at 50-75% CD`

Characteristics (Inter Regular 13 pt `#F0EDE8`):
```
STRIKE AT 50-75% OF FULL CD:
- Fine-grained initial deposit
- Complete surface coverage
- Smooth interior surface
- No pitting or skip areas
- Deposit adheres uniformly to
  release agent layer
- Foundation for a quality electroform

RESULT:
Interior surface replicates mandrel
finish exactly. Ra matches mandrel Ra.
```

**Panel 2 -- POOR NUCLEATION (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `POOR: UNEVEN INITIAL COVERAGE` Barlow SemiBold 20 pt `#E05C5C`

Surface diagram (center):
- Mandrel surface bar, fill `#3A4055`
- Patchy, irregular nuclei clusters with gaps, `#E05C5C` at 40%
- Gap labels: `No deposit here` with arrows
- Rough spots: `Coarse grains from high CD`

Characteristics (Inter Regular 13 pt `#F0EDE8`):
```
STARTED AT FULL CD (NO STRIKE):
- Coarse initial grains
- Incomplete coverage in recesses
- Rough interior surface
- Hydrogen pitting trapped at interface
- Adhesion problems in thin areas
- Potential for lamination

RESULT:
Interior surface is rough, pitted,
and does not replicate mandrel finish.
SCRAP.
```

**Bottom insight (Y: 13.2" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#27AE60`
- `The strike is the foundation of the electroform -- like surface prep for plating. You cannot fix a bad start by plating over it. The interior surface quality is locked in during the first 10-30 minutes.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Strike Protocol + Why It Matters

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Strike Protocol (X: 0.5", W: 11.0")**

**Section label:** `STRIKE PROTOCOL` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Protocol Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
STEP 1: IMMERSE MANDREL (LIVE)
  Apply current BEFORE or AS mandrel
  enters solution to prevent chemical
  etching or passive layer formation.
  "Hot entry" -- rectifier on, then immerse.

STEP 2: STRIKE AT REDUCED CD
  Ni sulfamate: 1.5-2.5 A/dm2
  (50-75% of target 3-5 A/dm2)
  Duration: 10-30 min

STEP 3: RAMP TO FULL CD
  Increase current gradually over
  5-10 min to full operating CD
  (3-5 A/dm2 for Ni sulfamate)

STEP 4: VERIFY COVERAGE
  After 30-60 min, visually inspect
  if possible (some tanks allow viewing).
  Full matte coverage = good nucleation.
  Bright spots or bare areas = problem.
```

**Right -- Why It Matters (X: 12.0", W: 11.5")**

**Section label:** `WHY THE STRIKE IS CRITICAL` -- Y: 14.7".

**BLOCK D -- Importance Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Three key-point cards:

Card 1:
- Title: `INTERIOR SURFACE QUALITY` Barlow SemiBold 14 pt `#2EC4B6`
- Body: `The mandrel surface is replicated during the first few micrometers of deposition. Coarse grains, pits, or gaps at this stage become permanent features of the electroform's interior surface. For waveguides, reflectors, and molds, this surface IS the product.`

Card 2:
- Title: `ADHESION TO RELEASE LAYER` Barlow SemiBold 14 pt `#2EC4B6`
- Body: `The initial deposit must adhere uniformly to the release agent without bonding permanently. Too much initial current can chemically break through the release layer, locking the deposit to the mandrel. Too little leaves gaps.`

Card 3:
- Title: `STRESS DISTRIBUTION` Barlow SemiBold 14 pt `#2EC4B6`
- Body: `Initial deposit stress affects the entire electroform. High current density at start = high tensile stress in the base layer = curling and premature separation risk. Controlled strike = controlled stress.`

---

### ZONE 5 -- Bath Condition + Immersion Technique

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Bath Condition Verification (X: 0.5", W: 11.0")**

**Section label:** `PRE-STRIKE BATH CHECK` -- Y: 22.2".

**BLOCK E -- Bath Check Table (Y: 22.8" to 28.0"):**

| Parameter | Ni Sulfamate Target | Check Method |
|---|---|---|
| Ni concentration | 300-450 g/L (as Ni sulfamate) | Titration or specific gravity |
| NiCl2 | 5-30 g/L | Titration |
| H3BO3 | 30-45 g/L | Titration |
| pH | 3.8-4.2 | pH meter (calibrate daily) |
| Temperature | 50-54 C | Thermometer / controller |
| Stress reducer (saccharin) | 0.5-3 g/L (per Hull cell) | Hull cell test |
| Wetting agent | Per supplier recommendation | Visual (foaming test) |
| Filtration | Running, 1-5 um filter | Visual flow check |
| Contamination | Hull cell panel clean | Hull cell at 2 A, 10 min |

JetBrains Mono 11 pt `#F0EDE8`. Header: `#3A4055`.

**Right -- Immersion Technique (X: 12.0", W: 11.5")**

**Section label:** `HOT ENTRY TECHNIQUE` -- Y: 22.2".

**BLOCK E2 -- Technique Panel (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
"HOT ENTRY" (RECOMMENDED):
1. Turn rectifier ON at strike CD
2. Lower mandrel into solution
   smoothly and steadily
3. Ensure mandrel is fully submerged
   before stopping motion
4. Do not pause with mandrel
   partially submerged
   (causes waterline mark)

WHY HOT ENTRY:
- Prevents chemical attack on
  mandrel surface or release agent
  by acidic bath solution before
  current is flowing
- Ensures immediate cathodic
  protection of mandrel surface
- Avoids passive layer formation
  that blocks initial nucleation

CAUTION:
- Immerse smoothly to avoid
  trapping air bubbles under mandrel
- Air bubbles = pits in deposit
- Tilt mandrel slightly if geometry
  tends to trap air
```

---

### ZONE 6 -- Common Strike Failures

**Section label:** `STRIKE FAILURES` -- Y: 28.7".

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ROUGH INTERIOR SURFACE | Started at full CD; coarse initial grains | Strike at 50-75% CD for 10-30 min before ramping |
| 2 | 6.33" | PITTING AT INTERFACE | Air bubbles trapped during immersion; H2 evolution at high CD | Tilt during immersion; add wetting agent; reduce strike CD |
| 3 | 12.16" | ADHESION TO MANDREL | Strike CD too high; broke through release layer | Reduce strike CD; verify fresh release agent application |
| 4 | 18.0" | SKIP PLATING (BARE SPOTS) | Release agent too thick; or mandrel not conductive | Thinner release layer; verify conductivity on non-metal mandrels |

---

### ZONE 7 -- Footer

Standard. Title: `Initial Strike -- Electroforming`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Initial Strike Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The side-by-side nucleation comparison is deliberately dramatic -- the "good" panel shows a smooth, complete initial layer while the "poor" panel shows patchy, coarse coverage. This visual contrast drives home why the strike is not just a warm-up period but a quality-defining step. The hot entry technique section addresses a practical question that every electroforming operator faces: how do you get the mandrel into the bath without creating defects?

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #474 -- Construction Workup v1.0*
*2026-04-26*
