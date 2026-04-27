---
Project: Plating Posters Inc
Poster Number: 666
Title: "Inspection & Handling -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.9"
Technical Source: Inspection and handling for liquid spray painting -- DFT measurement (including Tooke gauge for multi-coat systems), gloss (ASTM D523), color (Delta E per ASTM D2244), adhesion, hardness, flexibility, and VOC compliance testing.
Process Scope: Inspection and handling for liquid spray painting (Stage 8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - Inspection
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #666 -- Construction Workup
## Inspection & Handling -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 8. Liquid spray painting adds two inspection dimensions that powder coating does not: gloss measurement and color measurement. The hero is the "six-test battery" that every quality inspector should run on liquid-painted parts -- DFT, adhesion, gloss, color, hardness, and flexibility. The Tooke gauge callout is the unique tool for liquid paint: it cuts a V-groove through the film to measure individual coat thicknesses in a multi-coat system. Gloss and color panels give the inspector specific scales and tolerances.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Six-test battery (Block B -- HERO):** DFT, adhesion, gloss, color, hardness, flexibility -- each with method, instrument, and pass criteria.
2. **Tooke gauge detail (Block C):** Destructive multi-coat thickness measurement.
3. **Gloss scale + color Delta E (Block D):** Visual reference scales.
4. **Defect grid (Block F):** 6 inspection failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Inspection (Amber)
ZONE 3 -- SIX-TEST BATTERY HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- TOOKE GAUGE + MULTI-COAT (15.5"--21.5" / ~6.0")
ZONE 5 -- GLOSS SCALE + COLOR DELTA E (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- The Six-Test Quality Battery` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `DFT tells you the thickness. Adhesion tells you the bond. Gloss and color tell you the appearance. All four must pass -- or the part does not ship.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Inspection -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Fully cured painted part --> After: Quality-verified, packaged, and ready for shipment`

---

### ZONE 3 -- Six-Test Battery Hero

**Section label:** `THE SIX-TEST BATTERY -- EVERY QUALITY INSPECTOR'S CHECKLIST` -- Y: 4.4".

**BLOCK B -- Six Cards in 3x2 Grid (Y: 5.0" to 15.0")**

**Top Row:**

*DFT Measurement (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `1. DFT MEASUREMENT` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters (JetBrains Mono 12 pt):
```
Method: ASTM D7091
Instruments: Magnetic (steel) / Eddy current (Al)
Frequency: 3--5 readings per part, min 5 parts/batch
Tolerance: +/- 0.5 mil from target (general industrial)
```
- Also: `Tooke gauge (ASTM D4138) for multi-coat -- see detail below`

*Adhesion (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `2. ADHESION` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Method B (Cross-Cut): ASTM D3359
  Score lattice, tape pull at 180 deg
  Rate: 0B (complete removal) to 5B (none)
  Pass: 4B or 5B
Method A (X-Cut): ASTM D3359
  Score X, tape pull
  Faster but less quantitative
```

*Gloss (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `3. GLOSS` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Method: ASTM D523, 60-degree glossmeter
Units: Gloss Units (GU)
  High gloss: > 80 GU
  Semi-gloss: 30--80 GU
  Satin: 15--30 GU
  Flat/matte: < 15 GU
```

**Bottom Row:**

*Color (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `4. COLOR (DELTA E)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Method: ASTM D2244, spectrophotometer
Delta E < 1.0: Imperceptible difference
Delta E < 3.0: Most industrial specs
Delta E > 3.0: Visible mismatch -- reject
```
- Note: `Measure against approved color standard panel`

*Hardness (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `5. HARDNESS` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Method: ASTM D3363 Pencil Hardness
Scale: 6B (softest) to 9H (hardest)
Report: Hardest pencil that does NOT cut
Typical liquid paint: F to 3H
```

*Flexibility (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `6. FLEXIBILITY` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Mandrel Bend: ASTM D522
  Smallest mandrel with no cracking
Impact: ASTM D2794
  Drop weighted tup; report in-lb
  Typical: 80--160 in-lb direct impact
```

---

### ZONE 4 -- Tooke Gauge + Multi-Coat

**Section label:** `THE TOOKE GAUGE -- MEASURING INDIVIDUAL COATS` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 21.3"):**

**Left -- Tooke Gauge (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `TOOKE GAUGE (ASTM D4138)` -- Barlow SemiBold, 20 pt, `#27AE60`

Body:
- `DESTRUCTIVE test -- cuts a V-groove through the film`
- `Measures INDIVIDUAL coat thicknesses in multi-coat systems`
- `Essential for: basecoat/clearcoat, primer/topcoat systems`
- `View cut under 50x microscope scaled to groove geometry`
- `Each coating layer visible as a distinct band in the groove`

When to use:
- `When total DFT gauge cannot distinguish primer from topcoat`
- `When customer spec requires per-coat DFT verification`
- `Automotive refinish and multi-coat industrial systems`

**Right -- Multi-Coat System Targets (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `TYPICAL MULTI-COAT DFT TARGETS` -- Barlow SemiBold, 18 pt, `#E8A020`

| Coat | DFT (mils) | Purpose |
|---|---|---|
| Primer | 0.8--2.0 | Adhesion + corrosion barrier |
| Basecoat (color) | 0.5--1.5 | Color, hiding, metallic effect |
| Clearcoat | 1.5--2.5 | Gloss, UV protection, scratch resistance |
| Total system | 2.8--6.0 | Full protection + appearance |

Note: `The Tooke gauge is the ONLY non-destructive alternative to cross-sectioning for per-coat measurement in the field. Magnetic/eddy current gauges read total system DFT only.`

---

### ZONE 5 -- Gloss Scale + Color Delta E

**Section label:** `APPEARANCE QUALITY -- GLOSS AND COLOR` -- Y: 21.7".

**Two-column layout (Y: 22.3" to 26.3"):**

**Left -- Gloss Scale Visual (X: 0.5", W: 11.0"):**

Title: `GLOSS SCALE (ASTM D523, 60-DEGREE)` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Four horizontal bars, stacked vertically, each representing a gloss range:
- Bar 1: `HIGH GLOSS > 80 GU` -- fill gradient bright, accent `#27AE60`
- Bar 2: `SEMI-GLOSS 30--80 GU` -- fill gradient medium, accent `#2EC4B6`
- Bar 3: `SATIN 15--30 GU` -- fill gradient subtle, accent `#E8A020`
- Bar 4: `FLAT / MATTE < 15 GU` -- fill gradient muted, accent `#3A4055`

Note: `Gloss is measured at 60-degree angle for most coatings. Use 20-degree for high-gloss (> 70 GU at 60 deg) and 85-degree for flat (< 10 GU at 60 deg).`

**Right -- Color Delta E (X: 12.0", W: 11.5"):**

Title: `COLOR TOLERANCE (ASTM D2244)` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Delta E Range | Perception | Typical Spec |
|---|---|---|
| < 0.5 | Undetectable | Master standard match |
| 0.5--1.0 | Barely perceptible | Premium automotive |
| 1.0--2.0 | Slight difference | High-quality industrial |
| 2.0--3.0 | Noticeable | General industrial pass |
| > 3.0 | Obvious mismatch | REJECT |

Note: `Always measure against an approved physical color standard. Digital values drift; physical standards are the reference.` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Defect Grid

**Section label:** `INSPECTION FAILURES -- 6 COMMON REJECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DFT OUT OF SPEC | `#E05C5C` | Gun distance, fluid flow, or line speed error | Adjust application parameters; verify with wet film gauge during spray |
| R1C2 | ADHESION FAILURE (< 4B) | `#E05C5C` | Poor surface prep, contamination, or exceeded recoat window | Verify pretreatment; clean before coat; sand if window exceeded |
| R1C3 | GLOSS OUT OF SPEC | `#E8A020` | Orange peel, contamination, or wrong matting agent level | Review flash/leveling; verify coating batch is correct gloss level |
| R2C1 | COLOR MISMATCH (dE > 3.0) | `#E8A020` | Wrong tint batch, metamerism, or substrate color bleed-through | Verify batch; measure under standard illuminant; add hiding coat |
| R2C2 | LOW HARDNESS | `#2EC4B6` | Undercure or wrong mix ratio | Check oven profile; verify A:B ratio; MEK rub test |
| R2C3 | HANDLING DAMAGE | `#E05C5C` | Parts handled before full cure or without protection | Wait for full cure; use clean gloves; interleave with foam/paper |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D7091, D3359, D523, D2244, D3363, D522, D2794, D4138. Acceptance criteria are customer-specific -- verify against purchase order or quality plan.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Liquid spray painting's inspection story adds gloss and color to the DFT-adhesion-hardness-flexibility tests shared with powder coating. The Tooke gauge is the unique tool -- it gives the inspector per-coat thickness in a multi-coat system without sending a panel to the lab for cross-sectioning. The gloss scale and Delta E tolerance table are visual references that a quality inspector can use daily. The six-test battery hero gives every QC technician a checklist: if all six pass, the part ships. If any fails, stop and diagnose.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #666 -- Construction Workup v1.0*
*2026-04-26*
