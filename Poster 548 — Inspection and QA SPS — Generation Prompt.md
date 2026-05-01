---
Project: Plating Posters Inc
Poster Number: 548
Title: "Inspection & QA -- Suspension Plasma Spray (SPS)"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 548 — Inspection and QA SPS — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ThermalSpray
  - SPS
  - Inspection
  - QualityAssurance
  - ClusterTS07
  - v1
---

# Claude Chat Generation Prompt -- Poster #548
## Inspection & QA -- Suspension Plasma Spray (SPS)
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION & QA` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Suspension Plasma Spray (SPS) -- Confirming Columnar Structure & Performance` -- `32` pt `#2EC4B6`. Y: **1.4"**.
### Step 3 -- `You can measure thickness and bond strength on any coating. SPS demands more -- you must confirm the columnar microstructure actually formed. SEM is your primary tool.` -- `20` pt at 65%. Y: **2.1"**.

Rule card (right): Big number `8` 72pt `#2EC4B6`. Label: `inspection tests to qualify your SPS coating`.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted. Stage 10 highlighted (Teal -- inspection/QA).

---

## Phase 4 -- Test Matrix (HERO)

Y: 3.8" to 15.3". Section label: `SPS INSPECTION TEST MATRIX`.

8-row table. Columns: Test (4.5") | Method/Standard (6.0") | Acceptance Criteria (7.0") | Priority (5.5").

| Test | Method / Standard | Acceptance Criteria | Priority |
|---|---|---|---|
| Microstructure | SEM cross-section (preferred) | Columnar morphology; no lamellar regions | `#E05C5C` CRITICAL |
| Porosity | ASTM E2109 (image analysis) | 10-25% (intentional; within spec) | `#E05C5C` CRITICAL |
| Thickness | Metallographic or eddy current | Per spec; typically 100-400 um | `#E8A020` REQUIRED |
| Bond Strength | Modified ASTM C633 | > 10 MPa (lower than APS due to finer structure) | `#E8A020` REQUIRED |
| Thermal Cycling | Furnace cycling (1100 degC / 1 hr / forced air) | > 1000 cycles to 20% spallation | `#E8A020` REQUIRED |
| Thermal Conductivity | Laser flash (ASTM E1461) | 0.7-1.2 W/mK (lower = better) | `#2EC4B6` RECOMMENDED |
| Phase Stability | XRD | Tetragonal prime ZrO2 -- NO monoclinic | `#E05C5C` CRITICAL |
| Visual | Unaided eye + 10x loupe | Uniform; no spalling, blistering, bare spots | `#E8A020` REQUIRED |

Header fill `#3A4055`. Priority color-coded per table. ASTM numbers in `#E8A020`.

---

## Phase 5 -- Microstructure Evaluation

Y: 15.5" to 22.0". Section label: `MICROSTRUCTURE -- THE PRIMARY QUALITY INDICATOR`.

**Left -- SEM Evaluation Criteria (W: 11.0", accent `#27AE60`):**

Checklist:
- Vertical columns visible from bond coat to surface
- Inter-columnar gaps continuous (not bridged)
- Column width 50-200 um (typical YSZ SPS)
- No lamellar regions indicating parameter drift
- Bond coat/topcoat interface clean and continuous
- No horizontal delamination cracks
- Branching cracks and segmentation ACCEPTABLE (enhance compliance)

Note: `SEM preferred over optical -- SPS features are finer than APS.` `#E8A020`.

**Right -- Good vs. Bad (W: 11.5"):**

*ACCEPTABLE (`#27AE60`):* Clear columnar structure. Inter-columnar porosity 5-15%. No lamellar bands. Consistent column width.

*REJECTABLE (`#E05C5C`):* Lamellar (flat splat) instead of columnar. Bridged inter-columnar gaps. Horizontal delamination cracks. Mixed columnar/lamellar (parameter instability).

---

## Phase 6 -- Phase Analysis + Cycling + Rejection

### XRD Phase Check (Left, Y: 22.0"-28.5", accent `#E05C5C`)

Key requirement: `NO MONOCLINIC ZrO2` JetBrains Mono 18pt `#E05C5C`.

- YSZ must remain tetragonal prime (t') phase
- Monoclinic = phase destabilization
- Monoclinic causes ~4% volume expansion
- Expansion creates stress and spallation
- XRD identifies phase non-destructively

If monoclinic detected: investigate suspension composition, spray temperature, cooling.

### Thermal Cycling Protocol (Right, accent `#E8A020`)

| Step | Condition |
|---|---|
| Heat | Ramp to 1100 degC |
| Hold | 1 hour at 1100 degC |
| Cool | Forced air to ~100 degC |
| Inspect | Visual for spallation each cycle |
| Target | > 1000 cycles to 20% spallation |

`Thermal cycling is the ultimate SPS TBC performance test.` `#E8A020`.

### Rejection Criteria (Y: 28.5"-32.5")

Section label: `REJECTION CRITERIA -- 4 AUTOMATIC FAILURES`. Four cards:

| Failure | Indicator | Action |
|---|---|---|
| LAMELLAR MICROSTRUCTURE | SEM shows flat splats, no columns | Reject; review all parameters; re-qualify |
| MONOCLINIC PHASE | XRD shows monoclinic ZrO2 | Reject; investigate suspension + thermal history |
| BOND STRENGTH < 10 MPa | ASTM C633 failure | Reject; evaluate bond coat + interface |
| PREMATURE SPALLATION | < 500 cycles | Reject; review bond coat oxidation + porosity |

Failure: `#E05C5C`. Action: `#E8A020`.

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.
Disclaimer: `SPS is an emerging technology with evolving quality standards. Acceptance criteria are representative of current YSZ TBC practice. Consult application-specific specifications. Standards may differ for non-TBC SPS applications.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] 8 rule card
- [ ] 8-row test matrix with priority indicators
- [ ] SEM evaluation checklist (7 items)
- [ ] Acceptable vs. rejectable microstructure panels
- [ ] XRD phase stability check with monoclinic warning
- [ ] Thermal cycling protocol table (5 steps)
- [ ] 4 rejection criteria cards
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection QA SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
