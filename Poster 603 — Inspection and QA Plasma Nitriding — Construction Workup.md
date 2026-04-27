---
Project: Plating Posters Inc
Poster Number: 603
Title: "Inspection & QA -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5, Process 4 Sections 4.9, 4.10)"
Process Scope: Quality testing, inspection methods, acceptance criteria, and applicable standards for plasma nitrided parts
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #603 -- Construction Workup
## Inspection & QA -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The final poster in the Plasma Nitriding cluster. Everything converges here: did the process deliver what was specified? Surface hardness, case depth, compound layer thickness and phase, dimensional change, and microstructure -- all verified by specific test methods. This poster is the quality engineer's reference.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection matrix hero (Block B):** Large table mapping each test to method, equipment, acceptance criteria, and applicable standard.
2. **Hardness testing callout (Block D):** Why HRC does not work for nitrided cases and what to use instead.
3. **Standards reference (Block E):** AMS 2759/10, AMS 2759/6, ASTM E384.
4. **Common rejection reasons (Block F):** 4 cards with fail conditions.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- INSPECTION MATRIX HERO (2.9"--15.5")
ZONE 3 -- HARDNESS TESTING (15.5"--22.0")
ZONE 4 -- STANDARDS + REJECTIONS (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- Verify the Case, Verify the Layer, Ship with Confidence` -- 30 pt `#E8A020` (Amber).
**Tagline:** `Microhardness is your truth. Metallography is your proof. The specification is your contract.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `HV` -- 72 pt `#27AE60`
- Label: `Vickers / Knoop -- the ONLY appropriate hardness scale for nitrided cases` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Inspection Matrix (HERO)

**Section label:** `INSPECTION MATRIX -- TEST BY TEST` -- Y: 3.1".

**BLOCK B -- Full-Width Table (Y: 3.8" to 15.3")**

| Test | Method | Equipment | Acceptance Criteria | Standard |
|---|---|---|---|---|
| Surface hardness | Vickers or Knoop microhardness | Microhardness tester; 300--500 gf load | Per spec: 500--1200 HV depending on alloy | ASTM E384 |
| Production screening | Rockwell 15N (superficial) | Rockwell tester; 15N scale | Correlate to HV; use for rapid go/no-go | ASTM E18 |
| Case depth (ECD) | Microhardness traverse | Step measurements from surface inward | Depth to core + 50 HV or specified minimum (e.g., 500 HV) | ASTM E384 |
| White layer thickness | Metallographic cross-section | Optical microscope 500--1000x; nital etch | Per spec: 0--25 microns; some specs require zero | AMS 2759/10 |
| White layer phase | X-ray diffraction (XRD) | XRD instrument | Gamma-prime (Fe4N) vs. epsilon (Fe2-3N); gamma-prime preferred for most | -- |
| Microstructure | Metallographic section; nital etch | Optical microscope 200--500x | No grain boundary nitride network (overnitriding); no anomalous structures | AMS 2759/10 |
| Dimensional check | CMM or gauge measurement | CMM, micrometers, bore gauges | Growth 0.0001--0.0005 inch/surface; within drawing tolerance | Per drawing |

Header row: `#3A4055` fill, Barlow SemiBold 13 pt. Data rows: alternating `#1E2435` / `#252B3D`, H: 1.4". Data: JetBrains Mono 12 pt. Standard column: `#E8A020`.

---

### ZONE 3 -- Hardness Testing

**Section label:** `HARDNESS TESTING -- GET IT RIGHT` -- Y: 15.7".

**BLOCK D -- Two-Panel (Y: 16.3" to 21.8")**

**Left -- THE PROBLEM (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `WHY HRC DOES NOT WORK` Barlow SemiBold 20 pt `#E05C5C`
- `Rockwell C (HRC) uses a 150 kgf major load`
- `The Brale diamond indenter penetrates 0.003--0.005 inch into the surface`
- `A typical nitrided case is only 0.005--0.025 inch deep`
- `HRC READS THROUGH THE CASE INTO THE SOFTER CORE`
- `Result: falsely low hardness reading`
- `NEVER use HRC for nitriding acceptance testing`

**Right -- THE SOLUTION (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#27AE60`
- Title: `USE MICROHARDNESS (HV / HK)` Barlow SemiBold 20 pt `#27AE60`
- `Vickers (HV) or Knoop (HK) at 300--500 gf load`
- `Indentation depth: < 0.0005 inch -- stays within the case`
- `Measures actual case hardness without core influence`
- `For traverse: step inward at 0.001--0.002 inch intervals`
- `Plot HV vs. depth -- the hardness profile`
- `ECD = depth where HV drops to core + 50 HV`
- `Rockwell 15N (superficial) acceptable for production screening -- correlate to HV`

---

### ZONE 4 -- Standards + Rejections

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Applicable Standards (X: 0.5", W: 11.0")**

Section label: `APPLICABLE STANDARDS` -- Barlow Condensed ExtraBold 22 pt.

| Standard | Coverage |
|---|---|
| AMS 2759/10 | Gas and plasma nitriding of steel parts -- THE primary aerospace nitriding spec |
| AMS 2759/6 | Nitriding of corrosion-resistant and maraging steels |
| AMS 2750 | Pyrometry -- furnace temperature uniformity requirements |
| ASTM E384 | Microhardness testing (Vickers and Knoop) |
| ASTM E18 | Rockwell hardness testing (for screening only) |
| CQI-9 | AIAG special process audit for heat treatment (automotive) |
| Nadcap AC7102 | Aerospace heat treating accreditation |

Each row: H: 1.2", alternating fills. Standard code: JetBrains Mono 13 pt `#E8A020`. Coverage: Inter Regular 13 pt `#F0EDE8`.

**Right -- BLOCK F: Common Rejection Reasons (X: 12.0", W: 11.5")**

Section label: `COMMON REJECTION REASONS` -- Barlow Condensed ExtraBold 22 pt `#E05C5C`.

4 stacked cards:

| Rejection | Cause | Prevention |
|---|---|---|
| SHALLOW CASE | Wrong steel (no nitride formers); temp too low; time too short | Verify alloy; check process parameters |
| EXCESSIVE WHITE LAYER | Gas ratio too N2-rich; temperature too low | Reduce N2 %; increase temp; or use two-phase cycle |
| NON-UNIFORM HARDNESS | Poor loading (shadowing, hollow cathode); temp non-uniformity | Fix spacing; add TCs; use pulsed DC or ASPN |
| CORE SOFTENING | Nitriding temp exceeded prior temper temp | Verify heat treatment history; temper must be > nitride temp + 50 F |

Each card: H: 2.2", fill `#1E2435`, left accent `#E05C5C`.
Rejection: Barlow SemiBold 16 pt `#E05C5C`.
Cause: Inter Regular 13 pt `#F0EDE8`.
Prevention: Inter Medium 13 pt `#27AE60`.

---

### ZONE 5 -- Footer

Standard footer. Title: `Inspection & QA -- Plasma Nitriding`. Version `v1.0 -- 2026`.
Disclaimer: `Process parameters and acceptance criteria shown are typical industry values. Specific requirements are governed by the applicable specification (AMS 2759/10, customer drawing, or purchase order). Consult your quality engineering department.`

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #603 -- Construction Workup v1.0 -- 2026-04-26*
