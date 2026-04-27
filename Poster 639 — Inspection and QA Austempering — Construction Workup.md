---
Project: Plating Posters Inc
Poster Number: 639
Title: "Inspection & QA -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Section 9.9)"
Process Scope: Post-process inspection, hardness testing, metallographic verification of bainite, mechanical testing per ASTM A897, common defects and corrective actions
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #639 -- Construction Workup
## Inspection & QA -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Austempering cluster. No temper step to worry about -- bainite IS the final structure. Inspection confirms you got bainite and not something else. Pearlite in the micro means slow transfer. Retained austenite means short hold. Martensite means the salt bath was too cold or the part was pulled early. The metallurgist's eye is the final quality gate, backed by hardness testing and mechanical testing per ASTM A897 for ADI.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection sequence hero (Block B):** Step-by-step QA flow from salt removal through final acceptance.
2. **Hardness targets table (Block C):** Expected ranges by material and salt bath temperature.
3. **Metallographic acceptance criteria (Block D):** What good bainite looks like vs. reject microstructures.
4. **Common defects table (Block E):** Defect, cause, remedy -- the troubleshooting reference.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 20.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber)
ZONE 3 -- INSPECTION SEQUENCE HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- HARDNESS TARGETS (13.5"--20.0" / ~6.5")
ZONE 5 -- METALLOGRAPHIC CRITERIA (20.0"--27.0" / ~7.0")
ZONE 6 -- COMMON DEFECTS TABLE (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Confirming Bainite, Verifying Properties` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `No temper to check. The microstructure IS the answer. Bainite confirmed = process success.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 of 9 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Final step: confirm bainite microstructure, verify hardness, check dimensions, release or reject`

---

### ZONE 3 -- Inspection Sequence Hero

**Section label:** `AUSTEMPERING INSPECTION SEQUENCE` -- Y: 4.4".

**BLOCK B -- 6-Step QA Flow**

Y: 5.0" to 13.0". Six rounded rectangles in a 3x2 grid (top row L-R, bottom row L-R).

Each box: W: 7.0", H: 3.5", fill `#1E2435`, radius 6, top accent 4 pt.

**Top Row (Y: 5.0"):**

| Step | Box X | Accent | Title | Content |
|---|---|---|---|---|
| 1. Salt Removal | 0.5" | `#2EC4B6` | `WASH & CLEAN` | Hot water rinse to remove all salt residue. Inspect for salt entrapment in blind holes or recesses. Salt left on parts = corrosion. |
| 2. Visual Inspection | 8.0" | `#2EC4B6` | `VISUAL CHECK` | Inspect for cracks, distortion, surface discoloration. Austempered parts should appear dark grey to black (salt quench oxide). No bright spots (indicates missed areas). |
| 3. Hardness Testing | 15.5" | `#E8A020` | `HARDNESS TEST` | Rockwell C (steel) or Brinell (ADI) at specified locations. Minimum 3 readings per part or per lot sample. Compare to spec requirement. |

**Bottom Row (Y: 9.0"):**

| Step | Box X | Accent | Title | Content |
|---|---|---|---|---|
| 4. Metallography | 0.5" | `#E8A020` | `MICROSTRUCTURE` | Mount, polish, etch with 2% nital. Confirm: bainite present, no pearlite, minimal retained austenite. This is the definitive test. |
| 5. Mechanical Testing | 8.0" | `#27AE60` | `MECHANICAL TESTS` | Per ASTM A897 for ADI: tensile, yield, elongation, impact (Charpy/Izod). For steel: per customer spec. Test coupons processed with the load. |
| 6. Dimensional Check | 15.5" | `#27AE60` | `DIMENSIONAL` | Check critical dimensions for distortion. Austempering produces 60-90% less distortion than conventional Q&T -- but verify. Compare to pre-process measurements. |

Arrows between boxes: 2 pt `#3A4055`, right-pointing (top row) and right-pointing (bottom row), with vertical connector from step 3 to step 4.

Inside each box:
- Step badge: Rounded rect, 1.0" x 0.35", fill = accent color, text `STEP N` in Barlow Condensed ExtraBold, 13 pt, `#1A1F2E`
- Title: Barlow SemiBold, 18 pt, `#F0EDE8`
- Content: Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 4 -- Hardness Targets

**Section label:** `HARDNESS TARGETS BY MATERIAL AND SALT TEMPERATURE` -- Y: 13.7".

**BLOCK C -- Hardness Table**

Y: 14.3" to 19.8". Column widths (23.0" total):
- Material (5.0") | Salt Temp (4.0") | Bainite Type (3.5") | HRC (3.0") | HB (3.0") | Tensile (ksi) (4.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

| Material | Salt Temp | Bainite | HRC | HB | Tensile |
|---|---|---|---|---|---|
| 1075-1095 | 500 F | Lower | 50--55 | -- | 250--300 |
| 5160 spring | 550 F | Lower/mixed | 45--52 | -- | 220--270 |
| 4340 structural | 500 F | Lower | 48--55 | -- | 240--290 |
| 4340 structural | 650 F | Upper | 35--42 | -- | 160--200 |
| ADI Grade 1 | 700 F | Ausferrite | -- | 269--321 | 125 min |
| ADI Grade 3 | 600 F | Ausferrite | -- | 341--444 | 175 min |
| ADI Grade 5 | 475 F | Ausferrite | -- | 444--555 | 230 min |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Material: Inter Medium, 13 pt.

**Note below table:**
- `HRC used for steel; HB (Brinell) used for ADI per ASTM A897. Do not convert between scales for specification compliance -- use the scale specified.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 5 -- Metallographic Acceptance Criteria

**Section label:** `METALLOGRAPHIC ACCEPTANCE -- WHAT TO LOOK FOR` -- Y: 20.2".

**BLOCK D -- Accept vs. Reject Panels**

Y: 20.8" to 26.8". Two-column layout.

**Left -- ACCEPT (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`, radius 6.

Title: `ACCEPTABLE MICROSTRUCTURES` -- Barlow SemiBold, 20 pt, `#27AE60`

Items (Inter Regular 14 pt `#F0EDE8`, line height 170%):

| Feature | Accept Criterion |
|---|---|
| Primary phase | 100% bainite (lower, upper, or mixed per spec) |
| Retained austenite | < 10% for steel; up to 25% acceptable for some ADI grades |
| Pearlite | ZERO -- any pearlite = reject |
| Martensite | ZERO (unless negligible trace at surface) |
| Carbide morphology | Fine, well-dispersed within bainite plates |
| Etch appearance | Acicular (needle-like) ferrite laths with fine carbide; dark etching |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Criteria: Inter Regular 13 pt `#F0EDE8`.

**Etch method note:**
- `Etchant: 2% nital (2% nitric acid in ethanol), 5-10 sec immersion. Bainite appears as dark acicular structure. Pearlite appears as lamellar (layered) structure -- distinctly different.` -- Inter Regular, 12 pt, `#2EC4B6`

**Right -- REJECT (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6.

Title: `REJECT INDICATORS` -- Barlow SemiBold, 20 pt, `#E05C5C`

Items (Inter Regular 14 pt `#F0EDE8`, line height 170%):

| Feature | Reject Reason | Root Cause |
|---|---|---|
| Pearlite present | Transfer too slow OR section too thick | Improve transfer speed; reduce section; re-evaluate hardenability |
| Untempered martensite | Pulled from salt too early; retained austenite transformed on cooling | Extend isothermal hold time |
| Excessive retained austenite (> spec) | Incomplete transformation | Extend hold; verify salt bath temp; check austenitizing temp (ADI) |
| Mixed bainite + pearlite | Marginal hardenability for section | Higher-alloy steel needed; or reduce section size |

Each reject item: Inter Regular 13 pt `#F0EDE8`. Root cause: Inter Medium 12 pt `#E05C5C`.

---

### ZONE 6 -- Common Defects Table

**Section label:** `COMMON DEFECTS -- CAUSE & CORRECTIVE ACTION` -- Y: 27.2".

**BLOCK E -- Defect Table**

Y: 27.8" to 32.3". Column widths (23.0" total):
- Defect (4.5") | Cause (7.5") | Corrective Action (11.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Defect | Cause | Corrective Action |
|---|---|---|
| Pearlite (soft spots) | Transfer > 15 sec; section too thick; insufficient hardenability | Reduce transfer time; alloy for hardenability; reduce section size |
| Incomplete transformation | Isothermal hold too short | Extend hold; verify with metallography on test coupon before full production |
| Retained austenite (ADI) | Austenitizing temp too high; hold time insufficient | Reduce austenitize temp; extend isothermal hold |
| Excessive distortion | Non-uniform salt bath temp; asymmetric quench entry | Improve agitation; optimize part orientation; verify bath uniformity |
| Salt contamination defects | Oil carryover from cleaning; water in salt | Improve pre-cleaning protocol; preheat parts and fixtures to 250+ F |

Data: Inter Regular, 12 pt, `#F0EDE8`. Defect names: Barlow SemiBold, 13 pt, `#E05C5C`.
Corrective actions: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & QA -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897/A897M; ASTM E18; ASTM E384. Specific acceptance criteria per customer specification and applicable standards.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the quality gate poster. The 6-step QA flow in Zone 3 gives the quality engineer a visual checklist. The accept/reject panels in Zone 5 are the metallurgist's quick reference -- "does my micro look like this?" The defect table at the bottom is the troubleshooting bridge back to process control. The "no temper to check" tagline reinforces what makes austempering unique -- the microstructure is the final answer, no further heat treatment steps to verify.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #639 -- Construction Workup v1.0*
*2026-04-26*
