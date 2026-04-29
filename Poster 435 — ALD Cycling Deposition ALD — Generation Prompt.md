---
Project: Plating Posters Inc
Poster Number: 435
Title: "ALD Cycling (Deposition) -- ALD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 435 — ALD Cycling Deposition ALD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - MainStage
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #435
## ALD Cycling (Deposition) -- ALD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `ALD CYCLING` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 7 of 10 -- One Atomic Layer at a Time` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `Pulse. Purge. Pulse. Purge. Repeat 100 times and you have 11 nm of Al2O3 -- pinhole-free, perfectly conformal, and digitally controlled by cycle count.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 7 of 10 highlighted.

---

## Phase 4 -- ALD Cycle Hero

Y: 5.0" to 14.0".
Section: `-O-Al(CH3)2 + CH4`.

```
-OH + Al(CH3)3 -->
-O-Al(CH3)2 + CH4

TMA reacts with surface -OH groups.
When all -OH sites consumed,
reaction STOPS (self-limiting).
```

```
Purge removes:
- Unreacted TMA
- CH4 byproduct
- Any physisorbed molecules

CRITICAL: Incomplete purge leads to
CVD-like growth (non-self-limiting)
```

```
-Al(CH3)2 + H2O -->
-Al-OH + CH4

H2O reacts with surface -CH3 groups.
Regenerates -OH surface.
Self-limiting when all -CH3 consumed.
```

```
Surface is now identical to the
starting surface -- but one
sub-monolayer of Al2O3 has been added.

RESULT: +0.11 nm of Al2O3
READY FOR: Next cycle
```

---

## Phase 5 -- Self-Limiting Behavior + GPC Table

Y: 14.5" to 21.8".

| Film | Precursors | GPC (nm/cycle) | Cycles for 10 nm | Cycles for 50 nm |
|---|---|---|---|---|
| Al2O3 | TMA + H2O | 0.11 | ~91 | ~455 |
| HfO2 | TEMAH + H2O | 0.10 | ~100 | ~500 |
| TiO2 | TDMAT + H2O | 0.06 | ~167 | ~833 |
| ZrO2 | TEMAZ + H2O | 0.10 | ~100 | ~500 |
| ZnO | DEZ + H2O | 0.18 | ~56 | ~278 |
| TiN | TDMAT + NH3 | 0.05 | ~200 | ~1000 |
| SiO2 | BDEAS + O2 plasma | 0.12 | ~83 | ~417 |
| Pt | MeCpPtMe3 + O2 | 0.05 | ~200 | ~1000 |

```
SELF-LIMITING means:
Once all available surface sites react,
NO MORE deposition occurs -- even if
you continue pulsing precursor.

THIS ENABLES:
1. DIGITAL THICKNESS CONTROL
   100 cycles = 11.0 nm. Period.

2. 100% CONFORMALITY
   High-aspect-ratio trenches, vias, and
   pores get the same thickness on bottom
   as on top (given sufficient exposure)

3. PINHOLE-FREE FILMS
   Self-limiting nature fills every gap
   above ~5-10 nm thickness

4. REACTOR GEOMETRY INDEPENDENCE
   Film thickness does not depend on
   gas flow pattern or substrate position
   (unlike PVD and most CVD)

VERIFICATION:
Saturation curve: plot GPC vs. pulse time.
GPC should plateau. If GPC keeps increasing
with longer pulse, the process is NOT
self-limiting (it is CVD).
```

---

## Phase 6 -- ALD Temperature Window + Cycle Timing

Y: 22.0" to 28.3".
Section: `true value. Not self-limiting.``.

| Parameter | Typical Value |
|---|---|
| TMA pulse time | 0.015-0.2 sec |
| TMA dose | 0.1-1 Torr pulse |
| Purge after TMA | 5-30 sec |
| H2O pulse time | 0.015-0.2 sec |
| Purge after H2O | 5-30 sec |
| Total cycle time | 15-60 sec |
| Cycles for 10 nm Al2O3 | ~91 |
| Total time for 10 nm | 25-100 min |

---

## Phase 7 -- Common Deposition Problems

Y: 29.3" to 32.0".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NON-SELF-LIMITING GROWTH | Insufficient purge; precursor overlap = CVD mode | Increase purge time; verify with saturation curve |
| 2 | 6.33" | ISLAND GROWTH | Surface lacks functional groups; contamination blocking nucleation | Surface functionalization (O2 plasma); proper cleaning |
| 3 | 12.16" | THICKNESS DRIFT | Temperature outside ALD window; bubbler temp unstable | Verify temperature calibration; check bubbler +/- 1 C |
| 4 | 18.0" | HIGH CARBON IN FILM | Low deposition temp (< 150 C); short purges | Increase temp; use plasma-ALD; extend purge |

---

## Phase 8 -- Footer

Standard. Title: `ALD Cycling (Deposition) -- ALD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 9 -- Review

- [ ] Headline `ALD CYCLING` 88pt
- [ ] Orientation strip with poster 7 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `ALD Cycling Deposition ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
