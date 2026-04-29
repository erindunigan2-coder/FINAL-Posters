---
Project: Plating Posters Inc
Poster Number: 290
Title: "Etch / Desmut -- Hardcoat Anodizing (Type III)"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 290 -- Etch Desmut Type III -- Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - Anodizing
  - TypeIII
  - Hardcoat
  - Etch
  - Desmut
  - ClusterAnodize02
  - v1
---

# Claude Chat Generation Prompt -- Poster #290
## Etch / Desmut -- Hardcoat Anodizing (Type III)
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone.

---

## Phase 2 -- Header

### Step 1 -- `ETCH / DESMUT` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Hardcoat Anodizing (Type III) -- Stages 3 & 4 of 8` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Etch is optional for precision parts. Desmut is NEVER optional. Trapped smut under 50 um of hard oxide means delamination.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Stages 3 and 4 both highlighted (fill `#E8A020`). Others dimmed.
Below: `Before: Clean surface (may have native oxide and mill finish)  -->  After: Smut-free, activated aluminum ready for anodize`

---

## Phase 4 -- Etch + Desmut Dual-Tank Hero

Y: 4.2" to 15.5". Section: `TWO TANKS, ONE GOAL: A SMUT-FREE ACTIVATED SURFACE`.

**Left -- Etch Tank:** `CAUSTIC ETCH (LIGHT OR SKIP)`. NaOH 30--45 g/L / 130--150 F / 30--90 sec (SHORTER than Type II). Etch rate ~0.5--1.0 mil/min.

Decision callout: `ETCH OR SKIP?`
- Precision parts (tight tolerance): SKIP etch -- go directly to desmut
- General parts: LIGHT etch 30--90 sec
- Some specs PROHIBIT caustic etch for hardcoat `#E05C5C`

**Right -- Desmut Tank:** `DESMUT / DEOXIDIZE (ALWAYS REQUIRED)`. Standard: HNO3 25--50% / Cu alloys: HNO3 + HF 1--3% / Ambient / 15--60 sec (HNO3) or 2--10 min (ferric sulfate).

Critical callout: `DESMUT IS NON-NEGOTIABLE. Trapped smut under hard coat = delamination under mechanical stress.` `#E05C5C`. `HF handling: calcium gluconate gel at station` `#E05C5C`

---

## Phase 5 -- Dimensional Impact + Etch Decision Tree

Y: 15.5" to 22.0".

**Left -- Dimensional Math:**
```
ETCH REMOVES: 60 sec at 140 F = ~0.5--1.0 mil/surface
ANODIZE ADDS: 2.0 mil coating = ~1.0 mil outward/surface
NET: Etched part = 0 to +0.5 mil | Non-etched = +1.0 mil
FOR PRECISION: Skip etch. Final = Original + (coating/2)
```

**Right -- Etch Decision Tree:**
Diamond 1: `Tolerance +/- 0.5 mil or tighter?` YES --> SKIP ETCH | NO --> Diamond 2
Diamond 2: `Cosmetic required?` YES --> LIGHT ETCH 30--60 sec | NO --> LIGHT ETCH or SKIP.
`Customer spec overrides this guide.`

---

## Phase 6 -- Smut Character by Alloy

Y: 22.0" to 28.5". Section: `ALLOY SMUT TABLE`.

| Alloy | Smut | Recommended Desmut | Notes |
|---|---|---|---|
| 6061 | Light gray | Straight HNO3 50% | Best hardcoat alloy |
| 6063 | Light gray | Straight HNO3 50% | Excellent hardcoat |
| 5052 | Light gray | Straight HNO3 50% | Slightly softer oxide |
| 2024 | Heavy dark copper | HNO3 + HF 1--3% | Max ~50 um before cracking |
| 7075 | Moderate copper/zinc | HNO3 + HF preferred | Slow current ramp required |
| Cast (A356, 380) | Very heavy black silicon | HNO3 + HF, extended | NOT RECOMMENDED for hardcoat |

Smut severity color-coded: Light=`#27AE60`, Moderate=`#E8A020`, Heavy/Very heavy=`#E05C5C`.

---

## Phase 7 -- Defect Strip

Y: 28.5" to 32.5". Section: `WHAT GOES WRONG -- 4 ETCH/DESMUT FAILURES`.

| # | Problem | Cause | Fix |
|---|---|---|---|
| 1 | DELAMINATION | Smut trapped under oxide | Verify desmut; use HF for Cu/Si alloys |
| 2 | OVER-ETCH (dimensional) | Etch too long on precision parts | Reduce time to 30 sec or skip |
| 3 | NON-UNIFORM COATING | Uneven etch = uneven oxide | Improve agitation; verify concentration |
| 4 | BURNING AT THIN SPOTS | Etch removed too much at edges | Mask edges; reduce etch time; skip etch |

---

## Phase 8 -- Footer

Standard. Title: `Etch / Desmut -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.
Disclaimer: `Parameters vary by alloy and specification. HF is extremely hazardous -- follow all OSHA requirements. Consult your process supplier.`

---

## Phase 9 -- Review

- [ ] Headline `ETCH / DESMUT` 88pt
- [ ] Dual-tank hero with etch (left) and desmut (right)
- [ ] `ETCH OR SKIP?` decision callout
- [ ] `DESMUT IS NON-NEGOTIABLE` coral callout
- [ ] Dimensional math calculation
- [ ] Etch decision tree (2 diamonds)
- [ ] 6-alloy smut table with severity colors
- [ ] 4 defect cards
- [ ] All text within 0.5" safe zone

---

## Phase 10 -- Light Remap & Export

Standard remap. Six files: `Etch Desmut Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
