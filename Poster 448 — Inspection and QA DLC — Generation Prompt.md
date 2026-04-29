---
Project: Plating Posters Inc
Poster Number: 448
Title: "Inspection & QA -- DLC"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 448 — Inspection and QA DLC — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - DLC
  - DiamondLikeCarbon
  - Inspection
  - ThinFilm
  - ClusterTF05
  - v1
---

# Claude Chat Generation Prompt -- Poster #448
## Inspection & QA -- DLC
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `INSPECTION & QA` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Diamond-Like Carbon -- Verifying Coating Quality` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `You cannot see sp3 content with your eyes. You cannot feel 2,000 HV with your fingers. Testing is not optional -- it is the only way to know what you deposited.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 10 of 10 highlighted.

---

## Phase 4 -- Test Methods Reference

Y: 15.3" to 20.3".
Section: `10--30 N |`.

| Test | Standard | What It Measures | Equipment | Typical Values (Good DLC) |
|---|---|---|---|---|
| Rockwell adhesion | VDI 3198 | Adhesion class (HF1--HF6) | Rockwell hardness tester + optical microscope | HF1--HF4 |
| Nanoindentation | ISO 14577 | Hardness (GPa) and elastic modulus | Nanoindenter (Berkovich tip) | a-C:H: 10--20 GPa / ta-C: 40--80 GPa |
| Scratch test | ASTM C1624 | Critical load Lc1 (cohesive) and Lc2 (adhesive) | Scratch tester with Rockwell diamond stylus | Lc2 > 10--30 N |
| Calotest | ISO 26423 | Coating thickness (um) | Ball cratering device + optical measurement | 0.5--5 um per specification |
| Ball-on-disc | ASTM G99 | Friction coefficient and wear rate | Pin-on-disc tribometer | CoF: 0.05--0.15 (dry) |
| Raman spectroscopy | -- | sp3/sp2 content; D and G peak analysis | Raman spectrometer (514 or 532 nm laser) | See Zone 4 |
| Visual inspection | -- | Color, uniformity, defects | Naked eye + 10x magnification | Uniform dark coating, no flaking |
| Profilometry | ISO 4287 | Surface roughness (Ra) | Stylus profilometer or optical | Ra < 0.05 um (bearing applications) |

---

## Phase 5 -- Raman Spectroscopy Interpretation

Y: 21.3" to 26.3".
Section: `150 cm-1) | Highly disordered; typical of good a-C:H |`.

| Observation | Meaning |
|---|---|
| G peak shifts UP (toward 1600 cm-1) | More sp2 clustering; film is more graphitic |
| G peak shifts DOWN (toward 1540 cm-1) | More sp3; film is more diamond-like |
| Broad G peak (FWHM > 150 cm-1) | Highly disordered; typical of good a-C:H |
| Narrow G peak (FWHM < 100 cm-1) | Ordered graphite; film has low sp3 |
| High ID/IG ratio | More disorder; can indicate higher sp3 for a-C:H |
| Photoluminescence background (slope) | High hydrogen content; strong in a-C:H |
| No D peak visible | Very high sp3 content; ta-C signature |

```
Every DLC film produces two broad peaks in
its Raman spectrum:

G PEAK (~1580 cm-1): "Graphite" peak.
  All sp2 carbon. Always present.

D PEAK (~1350 cm-1): "Disorder" peak.
  Activated by sp3 disorder in sp2 clusters.

The ratio ID/IG, the G peak position, and the
G peak width together characterize the DLC type
and quality.
```

---

## Phase 6 -- Accept/Reject Decision

Y: 27.3" to 32.3".
Section: `20% deviation |`.

| Card | X | W | Test | Accept | Reject |
|---|---|---|---|---|---|
| 1 | 0.5" | 4.4" | ADHESION | HF1--HF4 (HF1--HF2 for critical apps) | HF5 or HF6 |
| 2 | 5.1" | 4.4" | HARDNESS | Within spec range (+/- 15%) | Below minimum; > 20% deviation |
| 3 | 9.7" | 4.4" | THICKNESS | Within tolerance (+/- 10% of target) | Outside tolerance; visible thin spots |
| 4 | 14.3" | 4.4" | FRICTION | CoF < 0.15 (dry) per spec | CoF > 0.20; inconsistent values |
| 5 | 18.9" | 4.6" | VISUAL | Uniform dark color; no flaking, blistering, or haze | Flaking, delamination, color variation, haze |

---

## Phase 7 -- Footer

Standard. Title: `Inspection & QA -- DLC`. Version `v1.0 -- 2026`.
Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for Diamond-Like Carbon coating inspection. Adhesion classification per VDI 3198. Specific acceptance criteria vary by customer specification and application. Consult your process supplier and quality requirements for application-specific acceptance limits. Source: General industry knowledge; VDI 3198; VDI 2840; ISO 14577; ASTM C1624; ASTM G99.`

---

## Phase 8 -- Review

- [ ] Headline `INSPECTION & QA` 88pt
- [ ] Orientation strip with poster 10 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Inspection & QA DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
