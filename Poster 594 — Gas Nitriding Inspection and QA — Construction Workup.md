---
Project: Plating Posters Inc
Poster Number: 594
Title: "Gas Nitriding -- Inspection & QA"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.9)"
Technical Source: Inspection and quality assurance for gas nitriding. Covers hardness testing methods (superficial Rockwell, microhardness traverse), white layer measurement on metallographic cross-section, compound zone composition (epsilon vs. gamma-prime), case depth definition, and common defect identification.
Process Scope: Gas nitriding -- inspection and QA (Stage 9 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #594 -- Construction Workup
## Gas Nitriding -- Inspection & QA

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers everything the quality engineer needs after a nitriding cycle: how to test hardness, how to measure the case, how to evaluate the white layer, and how to identify defects. Nitriding inspection is unique because the case is so thin and hard that standard Rockwell testing can punch right through it -- superficial Rockwell and microhardness are the tools.

Design philosophy: hardness testing methods comparison as the hero, white layer measurement and classification panel, case depth definition and measurement, and a defect identification table with causes and remedies.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Hardness testing methods (Block B -- HERO):** Three method cards comparing testing approaches.
2. **White layer measurement panel (Block C).**
3. **Case depth definition and measurement (Block D).**
4. **Defect identification table (Block E).**
5. **Standard formatting: accents, color remap, JetBrains Mono, 24x36".**

---

## Part 2 -- Document Setup Instructions

Standard setup per Poster #586: 24x36", `#1A1F2E` background, four-font stack, series color palette.

### Step 5 -- Set ruler guides
Standard margins. Zone boundaries: 2.9", 12.5", 19.0", 25.5", 32.5".

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- HARDNESS TESTING METHODS / HERO (2.9"--12.5" / ~9.6" tall)
  Block B: Three testing method comparison cards

ZONE 3 -- WHITE LAYER MEASUREMENT (12.5"--19.0" / ~6.5" tall)
  Block C: Metallographic examination and compound zone classification

ZONE 4 -- CASE DEPTH (19.0"--25.5" / ~6.5" tall)
  Block D: ECD definition, measurement methods, traverse procedure

ZONE 5 -- DEFECT IDENTIFICATION TABLE (25.5"--32.5" / ~7.0" tall)
  Block E: Common defects with causes and remedies

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`, letter spacing -4
- Text: `GAS NITRIDING`

**BLOCK A -- Subheading**
- Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Inspection & QA -- Hardness, Case Depth, White Layer & Defect ID`

**BLOCK A -- Tagline**
- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Thin, extremely hard cases demand precise measurement techniques. Standard Rockwell punches through. Use superficial Rockwell or microhardness.`

---

### ZONE 2 -- Hardness Testing Methods (HERO)

**Dimensions:** Y: 2.9" to 12.5" (~9.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `HARDNESS TESTING -- METHOD SELECTION`

---

**BLOCK B -- Three Testing Method Cards**

Y: 3.8" to 12.3". Three cards in a row. Gap: 0.35".

Each card: Rounded rect, W: 7.3", H: 8.3", fill `#1E2435`, radius 8, top accent 4 pt.

*Card 1 -- Superficial Rockwell (X: 0.5"):*
- Top accent: `#27AE60` (Emerald)
- Title: `SUPERFICIAL ROCKWELL` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `PRODUCTION SCREENING` -- Inter Medium, 13 pt, `#27AE60`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
Scales: HR15N, HR30N, HR45N

Light loads (15, 30, or 45 kgf) with
diamond Brale indenter create shallow
impression -- stays within the case.

When to use:
  - Production floor hardness checks
  - Incoming/outgoing verification
  - Quick pass/fail screening

Limitations:
  - Affected by case thickness
  - Not suitable for case < 0.005 in
  - Surface finish affects reading
  - Cannot measure case depth profile

Typical spec:
  Nitralloy 135M: 92+ HR15N
```

*Card 2 -- Microhardness (Vickers/Knoop) (X: 8.2"):*
- Top accent: `#E8A020` (Amber)
- Title: `MICROHARDNESS TRAVERSE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `DEFINITIVE CASE PROFILE` -- Inter Medium, 13 pt, `#E8A020`

Content:
```
Method: Vickers (HV) or Knoop (HK)
Load: 100--500 gf (ASTM E384)

Cross-section polished, indented at
incremental depths from surface inward.

When to use:
  - ECD (effective case depth) measurement
  - Case depth profile (hardness vs. depth)
  - First article / qualification
  - Dispute resolution

Procedure:
  Indent every 0.001--0.002 in from surface
  Plot hardness vs. depth
  ECD = depth to 50 HRC equiv (513 HV)
  OR depth to core + 50 HV (per spec)

Gold standard for nitriding QA.
```

*Card 3 -- Standard Rockwell (X: 15.9"):*
- Top accent: `#E05C5C` (Coral)
- Title: `STANDARD ROCKWELL (HRC)` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `OFTEN INAPPROPRIATE` -- Inter Medium, 13 pt, `#E05C5C`

Content:
```
Scale: HRC (150 kgf, diamond Brale)

Standard HRC uses 150 kgf -- the heavy
load creates a deep impression that
PENETRATES THROUGH thin nitrided cases.

Result: reading reflects BOTH case and
core hardness -- falsely low.

When NOT to use:
  - Case depth < 0.020 in (most nitriding)
  - Thin compound zone evaluation
  - Any precision measurement

When acceptable:
  - VERY deep cases (> 0.020 in)
  - Rough screening only
  - Never for specification compliance
    on standard nitriding
```

Caution note (Inter Medium, 13 pt, `#E05C5C`):
```
Using HRC on a 0.010 in nitrided case
gives a FALSE LOW reading. The indenter
punches into the soft core beneath.
```

---

### ZONE 3 -- White Layer Measurement

**Dimensions:** Y: 12.5" to 19.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 12.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `WHITE LAYER (COMPOUND ZONE) -- MEASUREMENT & CLASSIFICATION`

---

**BLOCK C -- Two Panels**

**Left -- Metallographic Method (X: 0.5", W: 11.0"):**
- Rounded rect, Y: 13.4", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `HOW TO MEASURE WHITE LAYER` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
1. Section the part (destructive test)
2. Mount in metallographic mount
3. Polish to mirror finish (1 um diamond)
4. Examine UNETCHED or lightly etch (2% Nital)
5. White layer appears BRIGHT (non-etching)
   against the darker etched diffusion zone
6. Measure thickness at 400--1000x magnification
7. Report in inches or micrometers

Typical thickness:
  Single-stage: 0.0005--0.001 in (12.7--25 um)
  Two-stage: 0--0.0005 in (0--12.7 um)
  Class 0 (KN-controlled): ZERO
```

**Right -- Compound Zone Composition (X: 12.5", W: 11.0"):**
- Rounded rect, Y: 13.4", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `EPSILON vs. GAMMA-PRIME` -- Barlow SemiBold, 20 pt, `#27AE60`

Content:
```
The white layer contains two phases:

EPSILON (Fe2-3N):
  - Harder (800--1200 HV)
  - More brittle
  - Thicker layers tend to be epsilon-dominant
  - Higher KN produces more epsilon
  - Spalling/flaking risk if too thick

GAMMA-PRIME (Fe4N):
  - Slightly less hard (600--800 HV)
  - Tougher and more ductile
  - Thinner layers or lower KN favors gamma-prime
  - More fatigue-friendly

Identified by: X-ray diffraction (XRD)
or GDOES (glow discharge optical emission)

Ratio controlled by nitriding potential (KN)
and temperature -- higher KN = more epsilon.
```

---

### ZONE 4 -- Case Depth

**Dimensions:** Y: 19.0" to 25.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 19.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `CASE DEPTH -- DEFINITION & MEASUREMENT`

---

**BLOCK D -- Two Panels**

**Left -- ECD Definition (X: 0.5", W: 11.0"):**
- Rounded rect, Y: 19.9", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#27AE60`
- Title: `EFFECTIVE CASE DEPTH (ECD)` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 165%):
```
Two common definitions (check your spec):

DEFINITION 1 (per SAE J423):
  Depth from surface to 50 HRC equivalent
  (approximately 513 HV)

DEFINITION 2 (common in nitriding specs):
  Depth from surface to core hardness + 50 HV
  (accounts for different base steel hardnesses)

Example:
  Core hardness = 350 HV (4140 Q&T)
  ECD = depth to 400 HV (350 + 50)

Typical nitriding ECD:
  0.005--0.030 in (0.13--0.76 mm)
```

**Right -- Measurement Methods (X: 12.5", W: 11.0"):**
- Rounded rect, Y: 19.9", H: 5.4", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `MEASUREMENT METHODS` -- Barlow SemiBold, 20 pt, `#E8A020`

Content:
```
1. MICROHARDNESS TRAVERSE (primary)
   Vickers or Knoop at 0.001--0.002 in steps
   Plot hardness vs. depth
   ECD = depth where hardness drops to target

2. NITROGEN PROFILE (laboratory)
   GDOES or EPMA measures nitrogen concentration
   vs. depth -- correlates to hardness profile
   Used for research / specification development

3. FILE TEST (shop floor, qualitative)
   Hardened file cannot cut properly nitrided case
   Good for quick pass/fail -- not quantitative
   NOT acceptable for specification compliance

4. FRACTURE TEST (qualitative)
   Break a test piece; nitrided case appears
   fine-grained and lighter than core
```

---

### ZONE 5 -- Defect Identification Table

**Dimensions:** Y: 25.5" to 32.5" (~7.0" tall).

---

**Section label:**
- Centered. Y: 25.7". Barlow Condensed ExtraBold, 24 pt, `#E05C5C`
- Text: `COMMON DEFECTS -- IDENTIFICATION, CAUSE & REMEDY`

---

**BLOCK E -- Defect Table**

Y: 26.4" to 32.3". Column widths (23.0" total):
- Defect (4.5") | How to Detect (4.5") | Cause (6.5") | Remedy (7.5")

Header row: `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Defect | Detection | Cause | Remedy |
|---|---|---|---|
| Excessive white layer | Metallography; exceeds class spec | KN too high; single-stage only; too long | Implement 2-stage; reduce KN in Stage 2 |
| No white layer (when required) | Metallography; WL absent | KN too low; poor atmosphere control | Increase KN; verify NH3 flow; check for leaks |
| Spalling / flaking | Visual; fragments lifting from surface | Thick brittle epsilon WL | Control to gamma-prime; reduce WL thickness |
| Soft spots | Superficial Rockwell; low readings | Surface contamination; Cr passive film; part contact | Improve cleaning; activate surface; fix fixturing |
| Core softening | Core hardness below spec | Nitride temp exceeded original temper temp | Verify pre-treat temper > nitride temp + 50 F |
| Uneven case depth | Microhardness traverse varies across part | Poor gas circulation; parts too close | Improve fixturing; increase fan speed; reduce load density |

Data: Inter Regular, 11 pt, `#F0EDE8`. Defect names: Inter Medium, 12 pt, `#E05C5C`.

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Inspection methods and acceptance criteria shown are typical for gas nitriding per AMS 2759/6D, AMS 2759/10A, and ASTM E384. Specific acceptance criteria are defined by the applicable specification for each application. Consult your quality engineer.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"
> Gas Nitriding -- Inspection & QA

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"
> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]`

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"
> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Hardness Testing | Section label, three method comparison cards |
| Zone 3 - White Layer | Section label, measurement method and composition panels |
| Zone 4 - Case Depth | Section label, ECD definition and measurement panels |
| Zone 5 - Defects | Section label, defect identification table |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap per Poster #586.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Inspection QA -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Inspection QA -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Inspection QA -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Inspection QA -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Inspection QA -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Inspection QA -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The "Standard Rockwell is often inappropriate" card in Coral is a critical teaching moment. Many shops default to HRC for everything -- and on a 0.010 in nitrided case, the 150 kgf load drives the indenter clean through the case into the soft core. The reading is meaningless. This is one of the most common inspection errors in nitriding QA.

The epsilon vs. gamma-prime distinction is the white layer's version of "it depends." Both are iron nitride, both are hard, but their mechanical properties and behavior under stress are very different. Quality engineers need to understand this to interpret metallographic results correctly.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #594 -- Construction Workup v1.0*
*2026-04-26*
