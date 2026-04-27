---
Project: Plating Posters Inc
Poster Number: 294
Title: "Inspection & Final -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2)"
  - "MIL-A-8625F Type III inspection requirements"
Process Scope: Final inspection, quality testing, and acceptance criteria for hardcoat anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Inspection
  - QualityControl
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #294 -- Construction Workup
## Inspection & Final -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 8 of 8 (the final gate). Hardcoat inspection is more rigorous than Type II because the coatings are thicker, the applications are more demanding (aerospace, hydraulic, wear), and the specifications are tighter. MIL-A-8625F Type III requires minimum hardness (Rockwell C 60--70 depending on alloy), minimum thickness, and salt spray hours. This poster covers thickness measurement (eddy current, cross-section), hardness testing, seal quality, visual inspection, and dimensional verification. The concept hook: "You can't see hardness. You can't see porosity. You can't see adhesion. Every critical property of hardcoat is invisible to the naked eye."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection test matrix hero (Block B):** Grid of all required tests with method, tool, and accept/reject criteria.
2. **Thickness measurement methods (Block D):** Eddy current vs. cross-section comparison.
3. **Hardness testing callout (Block E):** MIL-A-8625F minimum hardness by alloy.
4. **Seal quality test (Block F):** Dye spot test and acid dissolution test.
5. **Dimensional verification (Block G):** How to calculate expected dimensions after hardcoat.
6. **Accept/Reject decision flow (Block H).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 20.0" / 25.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- INSPECTION TEST MATRIX HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- THICKNESS + HARDNESS (15.0"--20.0" / ~5.0")
ZONE 5 -- SEAL QUALITY + DIMENSIONAL VERIFICATION (20.0"--25.0" / ~5.0")
ZONE 6 -- ACCEPT/REJECT DECISION FLOW (25.0"--28.5" / ~3.5")
ZONE 7 -- SPECIFICATION QUICK REFERENCE (28.5"--32.5" / ~4.0")
ZONE 8 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & FINAL` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stage 8 of 8 -- The Final Gate` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `You cannot see hardness. You cannot see porosity. Every critical property of hardcoat is invisible to the naked eye. Test it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Sealed hard-coated part  -->  After: Inspected, measured, documented, released`

---

### ZONE 3 -- Inspection Test Matrix Hero

**Section label:** `THE COMPLETE INSPECTION CHECKLIST` -- Y: 4.4".

**BLOCK B -- Test Matrix Table**

Y: 5.0" to 14.5". Full-width table.

| Test | Method | Tool / Equipment | Accept Criterion | Frequency | Spec Reference |
|---|---|---|---|---|---|
| **Thickness** | Eddy current (non-destructive) | Fischer or DeFelsko gauge | Min per spec (default 2.0 mil / 50 um) | Every part or per sampling plan | MIL-A-8625F 4.5.1 |
| **Thickness (destructive)** | Metallographic cross-section | Cut, mount, polish, measure | Verify eddy current accuracy | Per lot or qualification | ASTM B487 |
| **Hardness** | Microhardness tester (Vickers or Knoop) | Microhardness tester on cross-section | Min Rc 60 (2xxx), Rc 65 (7xxx), Rc 70 (others) | Per lot or qualification | MIL-A-8625F 4.5.3 |
| **Seal quality** | Dye spot test | Dye solution + blotting paper | No dye absorption = sealed | Per lot (if sealed) | ASTM B680 |
| **Seal quality** | Acid dissolution test | Weight loss measurement | Per spec limits | Qualification or dispute | ASTM B680 |
| **Corrosion resistance** | Salt spray (fog) test | Salt spray cabinet | Min hours per spec and alloy | Qualification or periodic | ASTM B117 |
| **Visual** | Unaided eye, 24" distance | Good lighting, no magnification | Uniform color; no burns, pits, bare spots, cracks | Every part | MIL-A-8625F 4.5.4 |
| **Adhesion** | Tape test (if specified) | Cross-hatch + tape pull | No delamination | Per spec requirement | ASTM D3359 |
| **Dimensions** | Precision measurement | Micrometer, CMM | Within print tolerance after coating | Per drawing/spec | Customer spec |

Header: Barlow SemiBold 11 pt `#F0EDE8` on `#3A4055`.
Data: Inter Regular 11 pt, alternating `#1E2435` / `#252B3D`.
Test names: Inter Medium 12 pt `#F0EDE8`.

---

### ZONE 4 -- Thickness + Hardness

**Two-column layout (Y: 15.2" to 19.8"):**

**Left -- Thickness Measurement (X: 0.5", W: 11.0"):**

Section label: `THICKNESS MEASUREMENT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Two stacked callout boxes:

Eddy Current (top):
- Fill `#1E2435`, left accent `#27AE60`
- Title: `EDDY CURRENT (NON-DESTRUCTIVE)` Barlow SemiBold 16 pt `#27AE60`
- `Standard production method` Inter Medium 13 pt `#F0EDE8`
- `Probe placed on coating surface` Inter Regular 12 pt `#F0EDE8`
- `Reads in seconds; no part damage` Inter Regular 12 pt `#F0EDE8`
- `Calibrate with foil standards on same alloy` Inter Regular 12 pt `#E8A020`
- `Accuracy: +/- 5% typical` JetBrains Mono 12 pt `#F0EDE8`

Cross-Section (bottom):
- Fill `#1E2435`, left accent `#E8A020`
- Title: `CROSS-SECTION (DESTRUCTIVE)` Barlow SemiBold 16 pt `#E8A020`
- `Gold standard for accuracy` Inter Medium 13 pt `#F0EDE8`
- `Cut part, mount in epoxy, polish, measure under microscope` Inter Regular 12 pt `#F0EDE8`
- `Destroys the test piece -- use coupons or sacrificial parts` Inter Regular 12 pt `#E05C5C`
- `Used for: qualification, dispute resolution, eddy current verification` Inter Regular 12 pt `#F0EDE8`

**Right -- Hardness Testing (X: 12.0", W: 11.5"):**

Section label: `HARDNESS TESTING` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `MIL-A-8625F MINIMUM HARDNESS` Barlow SemiBold 16 pt `#E8A020`

| Alloy Series | Minimum Hardness | Rockwell C Equivalent |
|---|---|---|
| **2xxx (Al-Cu)** | ~550 HV (Vickers) | Rc 60 minimum |
| **7xxx (Al-Zn)** | ~600 HV (Vickers) | Rc 65 minimum |
| **All other alloys** | ~650 HV (Vickers) | Rc 70 minimum |

JetBrains Mono 12 pt `#F0EDE8`. Header: Barlow SemiBold 11 pt on `#3A4055`.

Below table:
- `Method: Vickers or Knoop microhardness on polished cross-section` Inter Regular 12 pt `#F0EDE8`
- `Load: 25--100 gf (microhardness); indent must be within coating` Inter Regular 12 pt `#F0EDE8`
- `NOTE: Hardness varies through coating depth -- measure at mid-thickness` Inter Medium 12 pt `#E8A020`

---

### ZONE 5 -- Seal Quality + Dimensional Verification

**Two-column layout (Y: 20.2" to 24.8"):**

**Left -- Seal Quality Testing (X: 0.5", W: 11.0"):**

Section label: `SEAL QUALITY TESTING` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

Title: `DYE SPOT TEST (ASTM B680)` Barlow SemiBold 16 pt `#2EC4B6`

Content:
- `1. Apply dye solution to sealed surface (acid violet dye, 5 min)` Inter Regular 12 pt `#F0EDE8`
- `2. Rinse and blot dry` Inter Regular 12 pt `#F0EDE8`
- `3. Compare stain intensity to reference standards` Inter Regular 12 pt `#F0EDE8`
- ``
- `PASS: No stain or very faint stain (pores closed)` Inter Medium 13 pt `#27AE60`
- `FAIL: Dark stain (pores open -- reseal or investigate)` Inter Medium 13 pt `#E05C5C`
- ``
- `NOTE: PTFE-sealed parts -- dye spot test not applicable (PTFE fills pores differently than hydration seal)` Inter Regular 12 pt `#E8A020`

**Right -- Dimensional Verification (X: 12.0", W: 11.5"):**

Section label: `DIMENSIONAL VERIFICATION` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `CALCULATING FINAL DIMENSIONS` Barlow SemiBold 16 pt `#E8A020`

Content (JetBrains Mono 12 pt `#F0EDE8`):
```
Hard coat builds ~50% outward, ~50% inward.

For a 2.0 mil (50 um) total coating:
  Outward growth: +1.0 mil per surface
  Inward growth: -1.0 mil per surface (consumed Al)

FINAL DIMENSION per surface:
  = Original + (coating thickness / 2) - etch removal

EXAMPLE (shaft, 1.000" diameter, 2.0 mil coat, no etch):
  Each surface adds: +1.0 mil = +0.001"
  Total diameter: 1.000 + 0.002 = 1.002"

EXAMPLE (bore, 1.000" ID, 2.0 mil coat, no etch):
  Each surface grows inward: -0.001" per side
  Total ID: 1.000 - 0.002 = 0.998"
```

Below: `Always verify with actual measurement. Growth ratio varies by alloy and process conditions.` Inter Regular 11 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Accept/Reject Decision Flow

**Section label:** `ACCEPT / REJECT DECISION FLOW` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 25.2".

**BLOCK H -- Horizontal Decision Flow**

Y: 25.8" to 28.3".

Four decision boxes in a left-to-right flow:

Box 1: `VISUAL OK?` -- If NO --> `REJECT: Burns, pits, cracks, bare spots` (Coral)
If YES --> Box 2

Box 2: `THICKNESS OK?` -- If NO --> `STRIP & REPROCESS (if within alloy limits)` (Amber)
If YES --> Box 3

Box 3: `HARDNESS OK?` -- If NO --> `REJECT: Process investigation required` (Coral)
If YES --> Box 4

Box 4: `SEAL OK + DIMENSIONS OK?` -- If NO --> `RESEAL or REJECT per spec` (Amber)
If YES --> `ACCEPT -- SHIP` (Emerald `#27AE60`, prominent)

Decision boxes: Rounded rect, W: 5.5", H: 2.0", fill `#252B3D`, border 1 pt `#C8D0D8`.
Accept box: fill `#27AE60` at 15%, border 2 pt `#27AE60`, text `ACCEPT` Barlow SemiBold 18 pt `#27AE60`.

---

### ZONE 7 -- Specification Quick Reference

**Section label:** `SPECIFICATION QUICK REFERENCE` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 28.7".

Four quick-reference cards:

| Card | X | Spec | Coverage |
|---|---|---|---|
| 1 | 0.5" | MIL-A-8625F Type III | Military/aerospace hardcoat anodize -- thickness, hardness, corrosion, visual |
| 2 | 6.33" | AMS 2469 | Hard coat anodize -- aerospace material specification |
| 3 | 12.16" | ASTM B580 | Standard spec for anodic oxide coatings on aluminum |
| 4 | 18.0" | ASTM B117 | Salt spray (fog) testing procedure |

Each card: Rounded rect, W: 5.5", H: 3.5", fill `#1E2435`, radius 6, left accent 0.06" `#C8D0D8`.
Spec: Barlow SemiBold 14 pt `#E8A020`. Coverage: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 8 -- Footer

Standard. Title: `Inspection & Final -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Inspection requirements are specification-specific. MIL-A-8625F, AMS 2469, and customer specifications govern actual acceptance criteria. Hardness conversion values are approximate. Consult your quality engineer and applicable spec.`

---

## Parts 5--7

**Grouping:** 8 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Final Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the quality gate poster -- it hangs in the inspection area, not on the process line. The test matrix is the hero: an inspector needs to see every required test, method, tool, and accept criterion in one scan. The dimensional verification calculation is critical for shops doing precision hardcoat -- miscalculating growth direction on a bore vs. a shaft is a classic error. The accept/reject decision flow provides a clear, repeatable inspection sequence. The hardness minimum table by alloy series is one of the most commonly referenced MIL-A-8625F requirements.

---

*Alaina -- Plating Posters Inc*
*Poster #294 -- Construction Workup v1.0*
*2026-04-26*
