---
Project: Plating Posters Inc
Poster Number: 411
Title: "Part Preparation -- CVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 411 — Part Preparation CVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - CVD
  - ChemicalVaporDeposition
  - BathPreparation
  - ThinFilm
  - ClusterTF02
  - v1
---

# Claude Chat Generation Prompt -- Poster #411
## Part Preparation -- CVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `PART PREPARATION` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `CVD -- Stage 3 of 10 -- Substrate Verification, Edge Prep, and Cobalt Concerns` -- `32` pt `#2EC4B6`. Y: **1.4"**.
### Step 3 -- `CVD operates at 800-1100 C. Your substrate must survive that temperature without distortion, phase change, or cobalt depletion. WC-Co cemented carbide is the sweet spot. Verify before you load.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 3 of 10 highlighted.

---

## Phase 4 -- Substrate Compatibility (HERO)

Y: 5.0" to 14.3".

| Substrate | Max Temp | CVD OK? | Notes | Risk | Verdict |
|---|---|---|---|---|---|
| WC-Co cemented carbide | 1200+ C | YES | Primary CVD substrate; tolerate process temp | LOW | `#27AE60` COAT IT |
| Ceramics (Si3N4, Al2O3, SiC) | 1500+ C | YES | Excellent thermal stability; common for CVD | LOW | `#27AE60` COAT IT |
| Graphite | 2500+ C | YES | Common substrate for SiC CVD; friable | LOW | `#27AE60` COAT IT |
| Silicon wafers | 1414 C (mp) | YES | Semiconductor CVD; epitaxial growth | LOW | `#27AE60` COAT IT |
| High-speed steel (HSS) | 550 C (temper) | NO | CVD temp exceeds tempering temp -- softens steel | HIGH | `#E05C5C` DO NOT COAT |
| Pre-hardened tool steel | 500-600 C | NO | Loses hardness above tempering temperature | HIGH | `#E05C5C` DO NOT COAT |
| Aluminum alloys | 400-550 C | NO | Melts or distorts at CVD temperatures | HIGH | `#E05C5C` DO NOT COAT |
| Stainless steel | 800+ C | CAUTION | Sensitization risk (carbide precipitation in 304/316) | MEDIUM | `#E8A020` SPECIAL CARE |
| Titanium alloys | 880+ C | CAUTION | Alpha-beta transition at 880 C; grain growth | MEDIUM | `#E8A020` SPECIAL CARE |

---

## Phase 5 -- Surface Finish + Edge Preparation

Y: 14.5" to 19.3".

| Application | Ra Requirement | Notes |
|---|---|---|
| Cutting inserts | < 0.4 um (16 uin) | After grinding; standard production finish |
| Precision molds | < 0.2 um (8 uin) | Fine grinding or lapping |
| General wear parts | < 0.8 um (32 uin) | Less critical than PVD |

---

## Phase 6 -- Cobalt Concerns

Y: 20.3" to 24.3".

- Inter Medium 14 pt `#F0EDE8`
- `HCl gas (CVD byproduct) attacks cobalt binder in WC-Co at high temperature`
- `Cobalt migrates to surface or is etched away -- creating a cobalt-depleted zone`
- `Depleted zone is brittle -- reduces substrate toughness and coating adhesion`
- `Eta-phase (Co3W3C) forms at interface if cooling is not controlled -- brittle intermetallic`
- Inter Medium 14 pt `#27AE60`
- `Use TiN as first interlayer -- protects WC-Co surface during subsequent high-temp layers`
- `MT-CVD (700-900 C) for inner layers reduces cobalt attack vs. HT-CVD (1000-1050 C)`
- `Control cooling rate through 900-700 C range to minimize eta-phase`
- `Select WC-Co grades with higher cobalt content (10-12% Co) for CVD compatibility`
- `Modern "CVD-grade" substrates are specifically designed to resist cobalt depletion`
- `Cobalt depletion is the #1 substrate-related failure mode in CVD-coated cutting inserts. It does not occur in PVD because PVD operates below the temperature where HCl attacks cobalt.` Inter Medium 14 pt `#E8A020`

---

## Phase 7 -- Masking + Dimensional Notes

Y: 24.5" to 32.3".

| Material | Max Temp | Application Method |
|---|---|---|
| Al2O3 paste (refractory) | 1200+ C | Brush or screen print |
| ZrO2 paste (refractory) | 1500+ C | Brush or screen print |
| BN spray (boron nitride) | 1000+ C | Spray on fixtures |
| Graphite fixtures | 2500+ C | Inherent masking by contact |

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SUBSTRATE SOFTENED | HSS or pre-hardened steel loaded -- exceeds temper temp | Verify material grade; CVD is for carbide/ceramics only |
| 2 | 6.33" | GRINDING BURN | Aggressive grinding created heat-affected zone | Inspect for discoloration; re-grind or reject |
| 3 | 12.16" | EDGE BUILDUP | Sharp edges not prepped; CVD gas nucleation at edges | K-land or hone edges before coating |
| 4 | 18.0" | WRONG GRADE LOADED | WC-Co grade not rated for CVD temperature | Check material cert; use CVD-grade substrates |

---

## Phase 8 -- Footer

Standard. Title: `Part Preparation -- CVD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 9 -- Review

- [ ] Headline `PART PREPARATION` 80pt
- [ ] Orientation strip with poster 3 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Part Preparation CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
