---
Project: Plating Posters Inc
Poster Number: 477
Title: "Post-Processing -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.7-8.8)"
Technical Source: Electroforming post-processing -- trimming flash, machining to final dimensions, stress-relief annealing, exterior plating, and any secondary operations that transform the raw electroform into a finished part. The electroform as removed from the mandrel has a precision interior but a rough exterior and excess material at edges.
Process Scope: Electroforming post-processing (Stage 9 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - PostProcessing
  - Machining
  - Annealing
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #477 -- Construction Workup
## Post-Processing -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of 10. The raw electroform has a mirror-quality interior (replicated from the mandrel) and a rough, as-deposited exterior with flash at the edges. Post-processing transforms it into a finished part: flash trimmed, exterior machined to dimension, stress relieved by annealing, and optionally plated on the outside for corrosion protection or appearance. The key constraint throughout: protect the precision interior surface.

Hero visual: post-processing flow diagram showing the five main operations.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Post-processing flow diagram (Block B -- HERO):** Five-step horizontal flow from raw electroform to finished part.
2. **Flash trimming (Block C):** Methods and cautions.
3. **Machining to final dimensions (Block D):** Turning, milling, grinding, EDM options.
4. **Stress-relief annealing (Block E):** Temperature, atmosphere, and property changes.
5. **Exterior plating (Block F):** Options for corrosion/decorative finish.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Post-processing stage highlighted (Teal)
ZONE 3 -- POST-PROCESSING FLOW HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- FLASH TRIM + MACHINING (14.5"--22.0" / ~7.5")
ZONE 5 -- ANNEALING + EXTERIOR PLATING (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON POST-PROCESSING PROBLEMS (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-PROCESSING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- From Raw Electroform to Finished Part` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The interior is precision. The exterior is rough. Post-processing brings the outside up to spec while leaving the inside untouched.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Post-processing stage highlighted (Teal). Others dimmed.
Below: `Before: Mandrel separated, raw electroform (Stage 8) --> After: Trimmed, machined, annealed, plated -- ready for QA`

---

### ZONE 3 -- Post-Processing Flow Hero

**Section label:** `POST-PROCESSING SEQUENCE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Five-Step Flow (Y: 5.0" to 14.0")**

Five panels in horizontal flow with arrows between:

**Panel 1 -- TRIM FLASH (X: 0.5", W: 4.3", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `TRIM FLASH` Barlow SemiBold 16 pt `#E05C5C`
- Icon area: scissors/cut symbol
- Body (Inter Regular 12 pt `#F0EDE8`):
```
Remove excess deposit
at edges and contact points.

Methods:
- Grinding wheel
- Rotary tool (Dremel)
- Laser cutting
- Wire EDM (precision)

CAUTION:
Do not let grinding heat
or vibration damage the
interior surface.
```

Arrow: `->` 3 pt `#C8D0D8`

**Panel 2 -- MACHINE EXTERIOR (X: 5.1", W: 4.3", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `MACHINE` Barlow SemiBold 16 pt `#E8A020`
- Body:
```
Machine exterior to final
dimensions and tolerances.

Options:
- CNC turning (cylindrical)
- CNC milling (complex shapes)
- Surface grinding (flat)
- EDM (complex, precise)

Fixture on interior surface
ONLY with soft jaws or
custom fixtures that do
not mar the precision surface.
```

Arrow: `->` 3 pt `#C8D0D8`

**Panel 3 -- ANNEAL (X: 9.7", W: 4.3", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `ANNEAL` Barlow SemiBold 16 pt `#27AE60`
- Body:
```
Stress-relief anneal
(if required by application).

400-600 C for 1-2 hours
in inert atmosphere
(Ar, N2, or vacuum).

EFFECTS:
- Reduces internal stress
- Increases ductility
- REDUCES hardness
  (300 HV -> 150-180 HV)
- May cause slight
  dimensional change

NOT FOR ALL APPLICATIONS.
Skip if hardness is critical.
```

Arrow: `->` 3 pt `#C8D0D8`

**Panel 4 -- PLATE EXTERIOR (X: 14.3", W: 4.3", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `PLATE EXTERIOR` Barlow SemiBold 16 pt `#2EC4B6`
- Body:
```
Optional exterior plating
for protection or appearance.

Options:
- Chrome: corrosion + wear
- Gold: corrosion + appearance
- Tin: solderability
- Nickel: corrosion + buildup

Mask the precision interior
surface before any exterior
plating operation.

Standard electroplating
process applies.
```

Arrow: `->` 3 pt `#C8D0D8`

**Panel 5 -- FINAL CLEAN (X: 18.9", W: 4.3", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#F0EDE8`
- Title: `FINAL CLEAN` Barlow SemiBold 16 pt `#F0EDE8`
- Body:
```
Remove all machining oils,
coolant residue, handling marks.

Ultrasonic clean in mild alkaline
DI water rinse
IPA wipe on critical surfaces
Dry with filtered air

PACKAGE:
Wrap interior surface in
lint-free protective material.
Package in clean container.
Label completely.
```

**Bottom insight (Y: 13.2" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#2EC4B6`
- `Not every electroform needs all five steps. A thin screen mesh may only need flash trimming. A precision waveguide needs all five. Match the post-processing to the application.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Flash Trim + Machining Details

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Flash Trimming (X: 0.5", W: 11.0")**

**Section label:** `FLASH TRIMMING` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Trimming Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
WHAT IS FLASH?
  Excess electroformed metal that extends
  beyond the intended part boundary.
  Caused by:
  - Current wrapping around mandrel edges
  - Deposit growing past mandrel boundary
  - Cathode contact point deposits

REMOVAL METHODS:

| Method | Precision | Speed |
|--------|-----------|-------|
| Hand grinding (rotary tool) | Low | Fast |
| Band saw | Low | Fast |
| Wire EDM | Very high | Slow |
| Laser cutting | High | Moderate |
| CNC milling | High | Moderate |

CRITICAL RULE:
Clamp the electroform securely but
DO NOT compress or deform it.
Use soft fixtures. Avoid vise jaws
that contact the interior surface.

EDGE FINISH:
Deburr after trimming. Sharp edges
on thin electroforms are hazardous
(cut risk) and stress concentrators.
```

**Right -- Machining (X: 12.0", W: 11.5")**

**Section label:** `MACHINING TO FINAL DIMENSIONS` -- Y: 14.7".

**BLOCK D -- Machining Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
EXTERIOR MACHINING:
The as-deposited exterior surface of an
electroform is rough (Ra 1-10 um depending
on bath conditions and deposit thickness).
Machining brings it to final dimensions
and surface finish.

FIXTURING CHALLENGE:
The interior surface is precision -- you
cannot clamp on it with hard fixtures.
Solutions:
- Expanding mandrel (internal)
- Soft jaw chucks
- Wax or low-melt alloy fill (temporary
  internal support for machining)
- Vacuum fixtures

DIMENSIONAL NOTES:
- Account for material removed by machining
  when calculating required deposit thickness
- Typical machining allowance: 0.1-0.5 mm
  per side above final dimension
- For tight tolerances (+/- 0.01 mm):
  measure frequently during machining

CUTTING PARAMETERS:
Ni electroforms machine like wrought Ni.
Use carbide or ceramic inserts.
Moderate cutting speed (50-100 m/min).
Coolant recommended.
```

---

### ZONE 5 -- Annealing + Exterior Plating

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Stress-Relief Annealing (X: 0.5", W: 11.0")**

**Section label:** `STRESS-RELIEF ANNEAL` -- Y: 22.2".

**BLOCK E -- Annealing Panel (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

| Parameter | Value |
|---|---|
| Temperature | 400-600 C (typical: 500 C) |
| Time | 1-2 hours at temperature |
| Atmosphere | Inert (Ar, N2) or vacuum -- prevents oxidation |
| Ramp rate | 3-5 C/min (avoid thermal shock) |
| Cooling | Furnace cool or controlled (2-5 C/min) |

Effects table:

| Property | Before Anneal | After Anneal |
|---|---|---|
| Internal stress | 20-50 MPa tensile | < 10 MPa |
| Hardness | 250-350 HV | 150-180 HV |
| Ductility (elongation) | 5-15% | 20-30% |
| Dimensional stability | May creep over time | Stable |

Bottom note:
- `SULFUR WARNING: Ni sulfamate deposits contain 0.01-0.1% sulfur. Above 600 C, sulfur migrates to grain boundaries causing embrittlement. NEVER exceed 600 C for sulfamate deposits. For applications requiring brazing (> 800 C), sulfur must be < 0.03% -- verify by combustion analysis.` Inter Medium 12 pt `#E05C5C`

**Right -- Exterior Plating (X: 12.0", W: 11.5")**

**Section label:** `EXTERIOR PLATING (OPTIONAL)` -- Y: 22.2".

**BLOCK F -- Plating Options (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
WHEN NEEDED:
- Corrosion protection for service
  environment (marine, chemical)
- Decorative appearance
- Solderability (tin plate)
- Wear resistance (hard chrome)
- Electrical conductivity (gold, silver)

PROCESS:
Standard electroplating on the EXTERIOR
surface of the electroform.
Mask the precision interior surface
completely before immersion.

COMMON EXTERIOR FINISHES:
- Decorative chrome (0.25-0.5 um)
- Hard chrome (25-250 um)
- Gold (0.5-5 um, electronics)
- Tin (5-25 um, solderability)
- Passivation (chemical, not electroplated)

PREPARATION:
Activate exterior surface (mild acid dip)
before plating. Electroformed Ni activates
easily -- no special pretreatment needed.
```

---

### ZONE 6 -- Common Post-Processing Problems

**Section label:** `POST-PROCESSING PROBLEMS` -- Y: 28.7".

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | INTERIOR SURFACE DAMAGED | Hard fixturing during machining; careless handling | Soft fixtures; training; protective wrapping |
| 2 | 6.33" | DISTORTION AFTER ANNEAL | Stress release causes dimensional change | Anneal on fixture (constrained anneal); measure before/after |
| 3 | 12.16" | EMBRITTLEMENT AT HIGH TEMP | Sulfur at grain boundaries above 600 C | Never exceed 600 C for sulfamate deposits; verify S content |
| 4 | 18.0" | EXTERIOR PLATING PEELED | Poor activation of as-machined exterior surface | Acid activate before plating; verify cleanliness |

---

### ZONE 7 -- Footer

Standard. Title: `Post-Processing -- Electroforming`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post-Processing Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The five-step flow hero is deliberately broad because post-processing varies enormously by application. The "not every electroform needs all five steps" callout manages expectations. The sulfur warning in the annealing section is critical safety/technical content -- sulfur-induced embrittlement has caused real-world failures in aerospace electroformed components, and the 600 C ceiling is a hard rule that every operator must know.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #477 -- Construction Workup v1.0*
*2026-04-26*
