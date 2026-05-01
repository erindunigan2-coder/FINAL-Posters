---
Project: Plating Posters Inc
Poster Number: 498
Title: "Inspection & QA -- HVOF"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 498 — Inspection and QA — HVOF — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - HVOF
  - Inspection
  - QualityAssurance
  - ClusterTS02
  - v1
---

# Claude Chat Generation Prompt -- Poster #498
## Inspection & QA -- HVOF
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION & QA` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `HVOF -- The Final Gate -- Stage 10 of 10` -- `32` pt `#27AE60`. Y: **1.4"**.
### Step 3 -- `Bond strength so high the test adhesive fails before the coating does. Porosity below 1%. Hardness exceeding hard chrome. Verify every property.` -- `20` pt at 65%. Y: **2.1"**.

**Rule card** (right side):
- Big number: `8` -- 72 pt `#27AE60`
- Label: `standard tests to qualify your HVOF coating` -- 14 pt `#F0EDE8`

---

## Phase 3 -- Orientation Strip

Stage 10 highlighted (Emerald). Others dimmed.

---

## Phase 4 -- Test Method Table (HERO)

Y: 4.2" to 15.5". Section label: `HVOF QUALITY TESTS -- COMPLETE REFERENCE` centered, 28 pt.

8-row table. Header fill `#3A4055`. ASTM numbers in `#E8A020`.

| Test | Method | Acceptance Criteria (WC-12Co) | Notes |
|---|---|---|---|
| Bond strength | ASTM C633 | > 70 MPa (often exceeds epoxy -- report as "> epoxy") | Tensile adhesion; epoxy FM-1000 rated ~75-80 MPa |
| Porosity | ASTM E2109 | < 1.0% (typically < 0.5%) | Image analysis on metallographic cross-section |
| Thickness | Eddy current; mag-gauge; ASTM B487 | Per drawing +/- 50 um | Cross-section is definitive; others are screening |
| Hardness | ASTM E384 (HV300) | 1100-1400 HV300 | Vickers microhardness on cross-section; load 300 gf |
| Surface roughness | Profilometer (Ra) | As-ground: Ra < 0.4 um typical | Specification dependent; verify per drawing |
| Microstructure | Metallographic cross-section (unetched + etched) | Uniform carbide distribution; no delamination; no oxide stringers | Evaluate at 200-500x; check for decarburization |
| Visual | Unaided eye + 10x loupe | No spalling, blistering, orange peel, or bare spots | First-pass screen before destructive testing |
| Corrosion | ASTM B117 (salt spray) | Per spec; typically > 500 hrs (sealed) | Only if specified; most WC-Co applications are wear, not corrosion |

---

## Phase 5 -- AMS 2448 Compliance + Microstructure Guide

### AMS 2448 Compliance (Y: 15.5"-22.0")

Section label: `AMS 2448 -- AEROSPACE QUALIFICATION FOR HVOF WC COATINGS` centered, 28 pt.

**Left -- AMS 2448 Requirements (W: 11.5", accent `#E8A020`):**
Title: `AMS 2448 REQUIREMENTS`. Key requirements: process qualification with destructive test coupons sprayed alongside production; equipment calibration records; powder lot traceability and certification; parameter recording and data logging; operator qualification per AMS 2448; periodic re-qualification (annual or per spec).

**Right -- Destructive Test Coupon Protocol (W: 11.0", accent `#27AE60`):**
Title: `TEST COUPON PROTOCOL`. Coupons must be: same substrate material as production part; sprayed simultaneously in same setup; subjected to same post-treatment (grinding). From each set: bond strength (ASTM C633); hardness (ASTM E384, HV300); porosity (ASTM E2109, cross-section); microstructure (metallographic evaluation). If ANY coupon fails: entire production lot is suspect.

Bottom note: `AMS 2448 is the aerospace industry's assurance that HVOF WC-Co can reliably replace hard chrome on flight-critical components. Compliance is non-negotiable for aerospace work.` 13pt `#E8A020`.

### Microstructure Interpretation Guide (Y: 22.0"-28.5")

Section label: `READING THE WC-Co CROSS-SECTION -- WHAT TO LOOK FOR` centered, 28 pt.

Six cards in 3x2 grid, W: 7.33", H: 2.5", fill `#1E2435`:

| Feature | Good Sign | Bad Sign |
|---|---|---|
| Carbide distribution | Uniform WC particles throughout Co matrix | Clusters, voids, or depleted zones |
| Decarburization | Sharp, angular WC particles (original morphology) | Rounded WC particles; W2C or eta-phase halos visible |
| Interface quality | Clean bond line; grit blast profile visible | Gaps, contamination, or disbond at interface |
| Porosity | Minimal pores; no interconnected voids | Large voids or interconnected pore network |
| Oxide content | Minimal dark stringers between splats | Heavy oxide layers between lamellae |
| Lamellar structure | Well-deformed splats with good cohesion | Poorly bonded splats; visible inter-lamellar gaps |

Good: Inter Medium 12pt `#27AE60`. Bad: Inter Medium 12pt `#E05C5C`.

Key note: `DECARBURIZATION is the #1 microstructure defect in HVOF WC-Co. Look for rounded (instead of angular) WC particles and gray halos around carbides. Decarburization means the flame was too hot -- the WC decomposed to W2C or free tungsten, and hardness drops dramatically.` 13pt `#E05C5C`.

---

## Phase 6 -- Accept/Reject Decision

Y: 28.5" to 32.5". Two side-by-side boxes:

**Left -- ACCEPT** (fill `#27AE60` at 12%, border 1pt `#27AE60`):
All tests meet AMS 2448 or customer specification. Visual inspection passes. Test coupons within limits. Documentation complete (parameter logs, coupon certs, powder lot records).

**Right -- REJECT / REWORK** (fill `#E05C5C` at 12%, border 1pt `#E05C5C`):
Any test below specification. Strip and re-spray (grind off coating; re-blast; re-spray). Root cause analysis REQUIRED before re-spray. If decarburization: check fuel:O2 ratio and standoff distance. `The cost of stripping and re-spraying is always less than the cost of a failed component in service.`

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- HVOF`. Version `v1.0 -- 2026`.

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 80pt
- [ ] Rule card with 8 standard tests
- [ ] Orientation strip with stage 10 highlighted
- [ ] 8-row test method table with ASTM references
- [ ] AMS 2448 two-column compliance layout
- [ ] 6-card microstructure interpretation guide
- [ ] Accept/reject decision boxes
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection QA HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
