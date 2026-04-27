---
Project: Plating Posters Inc
Poster Number: 648
Title: "Inspection & QA -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10, Section 10.8)"
Technical Source: Martempering inspection -- hardness (same targets as conventional Q&T), distortion measurement (the key metric that justifies martempering), microstructure verification (100% tempered martensite, no pearlite, no bainite), and crack detection. Distortion comparison data: 0.0001--0.0005 in OD change vs. conventional quench.
Process Scope: Martempering -- inspection and quality assurance
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Martempering
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #648 -- Construction Workup
## Inspection & QA -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Martempering inspection has a unique priority: distortion measurement. The entire reason this process exists is to produce martensite with less distortion than conventional quenching. If the parts come out with the same distortion as a conventional oil quench, the process failed -- even if the hardness is perfect. This poster puts distortion front and center alongside the standard inspection points (hardness, microstructure, cracks) and provides the common defect table that ties back to process parameters.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four-point inspection sequence (Block B -- HERO):** Hardness, distortion, microstructure, crack detection.
2. **Distortion comparison data (Block C):** Martempering vs. conventional Q&T dimensional change data.
3. **Common defects table (Block D):** Full defect-cause-remedy table from Watson's research.
4. **Acceptance criteria summary (Block E):** Pass/fail for martempered parts.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Teal)
ZONE 3 -- INSPECTION SEQUENCE / HERO (4.2"--14.5" / ~10.3")
  Block B: Four-point inspection
  Block C: Distortion comparison
ZONE 4 -- DEFECT REFERENCE TABLE (14.5"--22.0" / ~7.5")
  Block D: Defect-cause-remedy table
ZONE 5 -- ACCEPTANCE CRITERIA (22.0"--28.5" / ~6.5")
  Block E: Pass/fail summary
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Stage 9 of 9` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Hardness confirms the metallurgy. Distortion confirms the process. Both must pass. If distortion equals conventional Q&T, the martempering failed.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Tempered martensite, process complete  -->  After: Verified, measured, documented, released or rejected`

---

### ZONE 3 -- Inspection Sequence (HERO)

**Section label:** `FOUR-POINT INSPECTION` -- Y: 4.4".

**BLOCK B -- Four Inspection Points**

Y: 5.0" to 10.0". Four cards in a single row.

Each card: Rounded rect W: 5.5", H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt `#2EC4B6`.

| Point | X | Title | Method | Standard | What to Check |
|---|---|---|---|---|---|
| 1 | 0.5" | HARDNESS | Rockwell C (HRC) | ASTM E18 | Same hardness targets as conventional Q&T for the grade. Measure at specified locations per drawing. |
| 2 | 6.25" | DISTORTION | Dimensional measurement (before/after) | Per drawing | THE KEY METRIC. Compare pre- and post-process dimensions. OD change, roundness, flatness, runout. |
| 3 | 12.0" | MICROSTRUCTURE | Metallography (mount, polish, etch) | ASTM E3 / E407 | 100% tempered martensite. No pearlite (too-slow transfer). No bainite (salt too hot or hold too long). |
| 4 | 17.75" | CRACK DETECTION | MPI (preferred) or dye penetrant | ASTM E1444 / E165 | Surface and near-surface cracks. Lower risk than conventional Q&T but not zero. Focus on section changes. |

Card interior:
- Point badge: Rounded rect 0.8" x 0.35", fill `#2EC4B6`, text `POINT [N]` Barlow Condensed ExtraBold 13 pt `#1A1F2E`
- Title: Barlow SemiBold, 18 pt, `#F0EDE8`
- Method: JetBrains Mono Regular, 12 pt, `#2EC4B6`
- Standard: JetBrains Mono Regular, 11 pt, `#F0EDE8` at 60%
- What to check: Inter Regular, 12 pt, `#F0EDE8`, line height 150%

**BLOCK C -- Distortion Comparison Data**

Y: 10.5" to 14.3". Full-width panel.

Section label: `DISTORTION -- MARTEMPERING vs. CONVENTIONAL Q&T` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 10.5".

Two-column layout within rounded rect (W: 23.0", H: 3.3", fill `#1E2435`, radius 6):

**Left -- Dimensional Change Data (X: 1.0", W: 10.5"):**

Title: `TYPICAL DIMENSIONAL CHANGE` Barlow SemiBold 16 pt `#27AE60`

Table:

| Measurement | Martempering | Conventional Q&T |
|---|---|---|
| OD change | 0.0001--0.0005 in (0.003--0.013 mm) | 0.001--0.005 in (0.025--0.127 mm) |
| Roundness variation | 0.0002--0.0010 in (0.005--0.025 mm) | 0.002--0.010 in (0.05--0.25 mm) |
| Distortion reduction | 50--80% less | Baseline (100%) |

Header: fill `#3A4055`. Data: JetBrains Mono Regular 12 pt `#F0EDE8`.
Martempering column values: `#27AE60`. Conventional column values: `#E05C5C`.

**Right -- Why Less Distortion (X: 12.5", W: 10.0"):**

Title: `WHY MARTEMPERING DISTORTS LESS` Barlow SemiBold 16 pt `#F0EDE8`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
```
Conventional quench:
  Surface transforms to martensite FIRST
  (expands). Core transforms LATER
  (expands against already-rigid surface).
  Result: internal stress = distortion.

Martempering:
  Equalization hold ensures surface and
  core are at the SAME temperature when
  martensite starts forming. Both transform
  together. Minimal thermal gradient =
  minimal internal stress = minimal
  distortion.
```

Key terms: `#27AE60` for martempering advantages, `#E05C5C` for conventional disadvantages.

---

### ZONE 4 -- Defect Reference Table

**Section label:** `COMMON DEFECTS -- CAUSE AND REMEDY` -- Y: 14.7".

**BLOCK D -- Defect Table**

Y: 15.3" to 21.8". Column widths (23.0" total):
- Defect (4.5") | Cause (8.5") | Remedy (10.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Defect | Cause | Remedy |
|---|---|---|
| Bainite in microstructure | Salt bath temperature in bainite range (too high); hold time too long | Reduce salt temp to just above Ms; reduce hold to equalization only |
| Pearlite (soft spots) | Transfer too slow (> 15 sec); steel hardenability insufficient for section size | Faster transfer (automate); select higher-hardenability grade |
| Retained austenite | High alloy content; as-quenched only (temper skipped or insufficient) | Sub-zero treatment; double temper |
| Cracking | Section size variation; sharp stress risers; contaminated quench salt | Preheat heavy sections; radius sharp corners; maintain salt purity |
| Distortion (still excessive) | Salt bath temp too far below Ms; non-uniform agitation | Verify Ms temperature; optimize salt temp; improve agitation uniformity |

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".
Defect: Barlow SemiBold 13 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Remedy: Inter Medium 12 pt `#27AE60`.

---

### ZONE 5 -- Acceptance Criteria

**Section label:** `ACCEPTANCE CRITERIA` -- Y: 22.2".

**BLOCK E -- Pass/Fail Summary**

Y: 22.9" to 28.3". Two-column layout.

**Left -- Acceptance Requirements (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`, radius 6.

Title: `PASS` -- Barlow Condensed ExtraBold 24 pt `#27AE60`

Items (Inter Medium 13 pt `#F0EDE8`):
```
Hardness within specification for the grade
  (same targets as conventional Q&T)
Distortion within drawing tolerance
  (verify: < conventional Q&T distortion)
Microstructure: 100% tempered martensite
No cracks detected by MPI or dye penetrant
Dimensional measurements within print tolerance
Salt residue fully removed (visual + spot check)
Surface condition acceptable (no pitting
  from salt corrosion)
```

Data values: JetBrains Mono Regular 12 pt `#27AE60`.

**Right -- Rejection Criteria (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#E05C5C`, radius 6.

Title: `REJECT / REWORK` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`

Items (Inter Medium 13 pt `#F0EDE8`):
```
Hardness below minimum specification
Pearlite in microstructure (process failure:
  transfer too slow or hardenability too low)
Bainite in microstructure (process failure:
  salt too hot or hold too long)
Cracks detected (zero tolerance)
Distortion exceeds drawing tolerance
  (investigate: salt temp, agitation, transfer)
Retained austenite > specification limit
  (rework: additional temper cycles or sub-zero)
Salt residue corrosion on part surface
```

Data values: JetBrains Mono Regular 12 pt `#E05C5C`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Inspection & QA -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Acceptance criteria are typical industry values. Actual requirements are defined by the part drawing, customer specification, and applicable standards (ASTM E18, AMS 2759). Distortion data shown are representative ranges for medium-section steel parts. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Distortion is the star of this poster. The dimensional change data in Block C -- showing 0.0001--0.0005 in OD change vs. 0.001--0.005 in for conventional quench -- is the hard evidence that justifies the entire martempering process. The "why less distortion" explanation next to the data connects the numbers to the metallurgy: uniform transformation start temperature = uniform expansion = less stress = less distortion. The defect table maps directly to Watson's research brief, and the acceptance/rejection split gives QA a clean wall reference.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #648 -- Construction Workup v1.0*
*2026-04-26*
