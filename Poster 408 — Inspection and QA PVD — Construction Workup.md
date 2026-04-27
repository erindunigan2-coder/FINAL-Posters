---
Project: Plating Posters Inc
Poster Number: 408
Title: "Inspection & QA -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.8)"
Technical Source: PVD post-deposition inspection including adhesion testing (VDI 3198 Rockwell, scratch test, tape test), thickness measurement (calotest, XRF, profilometry, SEM), common defect identification, documentation and release criteria.
Process Scope: PVD inspection and quality assurance (Stage 10 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PVD
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #408 -- Construction Workup
## Inspection & QA -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 10 of 10 -- the final gate. Everything before this was process. This is where you prove it worked. Adhesion testing (VDI 3198), thickness measurement (calotest, XRF), visual inspection, and documentation. If the coating passes here, it ships. If it fails, the root cause traces back to one of the previous nine stages.

Design philosophy: the VDI 3198 Rockwell adhesion classification (HF1-HF6) is the hero -- this is the single most widely used adhesion test in PVD, and operators need to visually identify pass vs. fail. Flanked by a thickness measurement method comparison, a defect identification guide, and a release checklist.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **VDI 3198 adhesion classification (Block B -- HERO):** Six panels showing schematic crack patterns around a Rockwell indentation for HF1 through HF6. Each panel is a simplified illustration -- a circle (indentation) with radiating lines and delamination areas. Achievable with circles, lines, and shaded areas.
2. **Thickness measurement comparison (Block C):** Table comparing calotest, XRF, profilometry, SEM.
3. **Defect identification guide (Block D):** Visual defect cards with cause and rejection criteria.
4. **Release checklist (Block E):** Documentation and sign-off requirements.
5. **Common QA failures (Block F):** Four failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 16.0" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 10 highlighted (Emerald -- quality)
ZONE 3 -- VDI 3198 ADHESION CLASSIFICATION / HERO (4.2"--16.0" / ~11.8")
ZONE 4 -- THICKNESS MEASUREMENT COMPARISON (16.0"--21.5" / ~5.5")
ZONE 5 -- DEFECT IDENTIFICATION GUIDE (21.5"--27.0" / ~5.5")
ZONE 6 -- RELEASE CHECKLIST + COMMON QA FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 10 of 10 -- Adhesion, Thickness, Defect ID, and Release` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The coating is only as good as the test that proves it. VDI 3198 for adhesion, calotest for thickness, and your eyes for everything else. Pass here or trace back through the other nine stages.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 10 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts cooled and unloaded (Stage 9) --> After: Inspection complete, parts released or rejected`

---

### ZONE 3 -- VDI 3198 Adhesion Classification (HERO)

**Section label:** `VDI 3198 ROCKWELL ADHESION TEST -- THE INDUSTRY STANDARD` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Six HF Classification Panels (Y: 5.0" to 14.0")**

Two rows of three panels each. Each panel: Rounded rect W: 7.33", H: 4.2", fill `#1E2435`, radius 6.

**Top Row (Y: 5.0" to 9.2") -- HF1, HF2, HF3:**

| Panel | X | Class | Verdict | Accent |
|---|---|---|---|---|
| 1 | 0.5" | HF1 | PASS (excellent) | `#27AE60` |
| 2 | 8.17" | HF2 | PASS (good) | `#27AE60` |
| 3 | 15.83" | HF3 | PASS (acceptable) | `#E8A020` |

**Bottom Row (Y: 9.8" to 14.0") -- HF4, HF5, HF6:**

| Panel | X | Class | Verdict | Accent |
|---|---|---|---|---|
| 4 | 0.5" | HF4 | MARGINAL | `#E8A020` |
| 5 | 8.17" | HF5 | FAIL | `#E05C5C` |
| 6 | 15.83" | HF6 | FAIL (severe) | `#E05C5C` |

**Inside each panel (top to bottom):**

*HF1 -- Excellent Adhesion:*
- Top border accent: 4 pt `#27AE60`
- Class badge: Rounded rect 1.2" x 0.4", fill `#27AE60`
- Text: `HF1` Barlow Condensed ExtraBold 16 pt `#1A1F2E`
- Illustration area (centered, 3.0" x 3.0"): Large circle (Rockwell indent, ~1.5" diameter, stroke 2 pt `#C8D0D8`) with very fine radial cracks (4-6 thin lines, stroke 1 pt `#C8D0D8`) extending ~0.3" beyond indent. No delamination.
- Description: Inter Regular 12 pt `#F0EDE8`
- `Fine radial cracks only. No delamination at indent edge.`
- Verdict: Barlow SemiBold 14 pt `#27AE60`
- `ACCEPTABLE`

*HF2 -- Good Adhesion:*
- Badge fill: `#27AE60`
- Illustration: Circle with more radial cracks (6-8 lines) and slight chipping at indent edge (small triangular areas in `#3A4055` around 10-20% of circumference).
- `Radial cracks with slight chipping at indent edge. < 20% circumference affected.`
- `ACCEPTABLE`

*HF3 -- Acceptable Adhesion:*
- Badge fill: `#E8A020`
- Illustration: Circle with more cracks, chipping around 20-40% of circumference, small delamination areas.
- `More chipping at indent edge. 20-40% circumference. Minor delamination.`
- Verdict: `#E8A020`
- `ACCEPTABLE (borderline)`

*HF4 -- Marginal:*
- Badge fill: `#E8A020`
- Illustration: Circle with significant chipping (40-60% circumference), visible delamination areas (larger `#3A4055` patches).
- `Significant chipping and delamination at indent edge. 40-60% circumference.`
- Verdict: `#E8A020`
- `MARGINAL -- consult spec`

*HF5 -- Failure:*
- Badge fill: `#E05C5C`
- Illustration: Circle with extensive delamination (60-80% circumference), large areas of coating removed.
- `Extensive delamination around indent. Coating lifting in large areas.`
- Verdict: `#E05C5C`
- `REJECT`

*HF6 -- Severe Failure:*
- Badge fill: `#E05C5C`
- Illustration: Circle with near-complete delamination, coating removed well beyond indent area.
- `Complete delamination around and beyond indent. Coating has no adhesion.`
- Verdict: `#E05C5C`
- `REJECT`

**Below the six panels -- Test procedure callout (Y: 14.2" to 14.8"):**
- Full-width rounded rect, H: 0.6", fill `#252B3D`, left accent `#27AE60`
- Text: `Procedure: Rockwell C indent at 150 kgf on coated surface. Examine crack pattern at 100-200x magnification. Classify HF1-HF6. Most specifications require HF1-HF4 maximum.` Inter Medium 13 pt `#27AE60`

**Additional test methods (right callout, Y: 14.2" to 15.8"):**
- Rounded rect, X: 12.0", Y: 14.2", W: 11.5", H: 1.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `OTHER ADHESION TESTS` Barlow SemiBold 14 pt `#2EC4B6`
- `Scratch test (ASTM C1624): Lc > 30 N = good adhesion` JetBrains Mono 11 pt `#F0EDE8`
- `Tape test (ASTM D3359): 4B-5B = acceptable; 0B-3B = failure` JetBrains Mono 11 pt `#F0EDE8`

---

### ZONE 4 -- Thickness Measurement Comparison

**Section label:** `THICKNESS MEASUREMENT -- POST-DEPOSITION` -- Y: 16.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK C -- Comparison Table (Y: 16.8" to 21.3")**

| Method | Principle | Range | Accuracy | Destructive? | Speed |
|---|---|---|---|---|---|
| Calotest (ball crater) | Grinding a crater through coating; measure ring diameters | 0.1-50 um | +/- 2-5% | Yes (small crater) | 2-5 min |
| XRF (X-ray fluorescence) | X-ray excitation; element-specific fluorescence | 0.01-50 um | +/- 3-10% | No | 30-60 sec |
| Profilometry (step height) | Stylus measures step at coating edge on witness coupon | 0.01-100 um | +/- 1-5% | Requires coupon | 1-3 min |
| SEM cross-section | Cut, polish, and image coating cross-section | 0.01-100 um | +/- 2% | Yes (destructive) | 30-60 min |
| Ellipsometry | Polarized light reflection on transparent films | 1 nm-10 um | +/- 0.5 nm | No | 1 min |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

Bottom callout:
- `Calotest + XRF is the standard QC combination for industrial PVD. Calotest for accurate absolute thickness; XRF for fast, non-destructive screening.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 5 -- Defect Identification Guide

**Section label:** `COMMON DEFECTS -- VISUAL IDENTIFICATION` -- Y: 21.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Six Defect Cards (Y: 22.3" to 26.8")**

Six cards in two rows of three. Each: Rounded rect W: 7.33", H: 2.1", fill `#1E2435`, radius 4, left accent `#E05C5C`.

**Top Row (Y: 22.3" to 24.4"):**

| Card | X | Defect | Visual Cue | Root Cause |
|---|---|---|---|---|
| 1 | 0.5" | Macroparticles | Raised bumps/droplets on surface | Arc process; high current; cathode contamination |
| 2 | 8.17" | Delamination | Coating peeling or flaking at edges | Poor adhesion; contamination; inadequate ion etch |
| 3 | 15.83" | Pinholes | Small uncoated spots; visible substrate | Particulate on surface; shadowing; geometry |

**Bottom Row (Y: 24.7" to 26.8"):**

| Card | X | Defect | Visual Cue | Root Cause |
|---|---|---|---|---|
| 4 | 0.5" | Wrong Color | Color shift from specification | Reactive gas ratio off; contamination |
| 5 | 8.17" | Non-Uniform | Thickness variation visible as color bands | Rotation failure; fixture shadowing; target erosion |
| 6 | 15.83" | Stress Cracking | Network of fine cracks in coating | Excessive stress; bias too high; coating too thick |

Interior per card:
- Defect name: Barlow SemiBold 14 pt `#E05C5C`
- Visual cue: Inter Regular 11 pt `#F0EDE8`
- Root cause: Inter Regular 11 pt `#E8A020`

---

### ZONE 6 -- Release Checklist + Common QA Failures

**Two-column layout (Y: 27.0" to 32.3"):**

**Left -- Release Checklist (X: 0.5", W: 11.0"):**

**Section label:** `RELEASE CHECKLIST` -- Y: 27.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

- Rounded rect, Y: 27.7", H: 4.4", fill `#1E2435`, left accent `#27AE60`
- Title: `BEFORE RELEASE -- VERIFY ALL` Barlow SemiBold 18 pt `#27AE60`

Checklist items (Inter Medium 14 pt `#F0EDE8`, each with a checkbox square):
- `Visual inspection -- correct color, no visible defects`
- `Adhesion test -- VDI 3198 HF1-HF4 (or per customer spec)`
- `Thickness -- within specification (+/- 10% typical)`
- `Documentation -- lot number, recipe, batch ID recorded`
- `Certificate of conformance generated`
- `Parts packaged in soft wrap or tray -- no metal-to-metal contact`
- `Witness coupons retained per batch`

**Right -- Common QA Failures (X: 12.0", W: 11.5"):**

**Section label:** `QA FAILURES -- ROOT CAUSE TRACEABILITY` -- Y: 27.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Three Failure Cards (Y: 27.7" to 32.3")**

Each card: Rounded rect W: 11.5", H: 1.4", fill `#1E2435`, left accent `#E05C5C`.

| Card | Y | Failure | Trace Back To |
|---|---|---|---|
| 1 | 27.7" | Adhesion failure (HF5-HF6) | Cleaning (Stage 4) or Ion Etch (Stage 7) -- contamination or insufficient surface activation |
| 2 | 29.3" | Thickness out of spec | Parameter Setup (Stage 7) -- deposition rate, time, or gas flow incorrect |
| 3 | 30.9" | Color/composition wrong | Deposition (Stage 8) -- reactive gas ratio, MFC calibration, or target condition |

Interior per card:
- Failure: Barlow SemiBold 14 pt `#E05C5C`
- Trace: Inter Medium 13 pt `#E8A020`

Bottom callout:
- `Every QA failure traces back to a specific upstream stage. The 10-stage process flow (Poster #399) is your root-cause map.` Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Inspection & QA -- PVD`. Version `v1.0 -- 2026`.

**Disclaimer:** `This poster is an educational reference tool. Inspection methods and acceptance criteria shown are typical for PVD hard coatings. Specific requirements vary by customer specification, industry standard, and coating application. Consult applicable specifications (VDI 3198, ASTM C1624, customer drawing) for binding acceptance criteria.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The VDI 3198 classification is the hero because it is the single most commonly performed adhesion test in PVD coating shops worldwide, and operators need to visually distinguish HF1 (pass) from HF5 (fail). The six-panel illustration makes this a wall reference that operators can compare to what they see under the microscope. The traceability section at the bottom ties this final stage back to the entire 10-stage process -- every failure here originated somewhere upstream.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #408 -- Construction Workup v1.0*
*2026-04-26*
