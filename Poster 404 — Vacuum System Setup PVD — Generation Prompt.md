---
Project: Plating Posters Inc
Poster Number: 404
Title: "Vacuum System Setup -- PVD"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 404 — Vacuum System Setup PVD — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - PVD
  - PhysicalVaporDeposition
  - BathPreparation
  - ThinFilm
  - ClusterTF01
  - v1
---

# Claude Chat Generation Prompt -- Poster #404
## Vacuum System Setup -- PVD
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `VACUUM SYSTEM SETUP` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `PVD -- Stage 4 of 10 -- Pump-Down, Leak Check, Base Vacuum` -- `32` pt `#E8A020`. Y: **1.4"**.
### Step 3 -- `No vacuum, no PVD. Base pressure below 5 x 10^-5 Torr is the minimum for quality hard coatings. Leak rate, outgassing, and pump condition determine everything.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 6 of 10 highlighted.

---

## Phase 4 -- Vacuum System Schematic (HERO)

Y: 5.0" to 15.8".

- Large rounded rect, X: 12.0", Y: 6.0", W: 10.0", H: 6.0", fill `#252B3D`, border 3 pt `#C8D0D8`
- Label: `PVD CHAMBER` Barlow SemiBold 18 pt `#F0EDE8`
- Inside: small fixture/part indicators, target indicators on walls
- Gauge symbol (circle): `IG` (ion gauge) on chamber, `TC` (thermocouple) on foreline
- Label: `TURBO / CRYO PUMP` Barlow SemiBold 14 pt `#2EC4B6`
- Gate valve between pump and chamber: small rect `#E8A020`
- Label: `GATE VALVE` Inter Regular 11 pt `#E8A020`
- Label: `ROUGHING PUMP` Barlow SemiBold 14 pt `#E8A020`
- Sub-label: `Rotary vane or scroll` Inter Regular 12 pt `#F0EDE8` at 60%
- Line from roughing pump output to turbo pump inlet
- Stroke: 3 pt `#3A4055`
- Foreline valve: small rect `#E8A020`
- Small rectangles representing MFCs, connected to chamber top

---

## Phase 5 -- Pump-Down Curve + Vacuum Ranges

Y: 16.8" to 21.8".
Section: `~50 mTorr`.

| Pressure Range | Classification | Coating Impact |
|---|---|---|
| > 1 x 10^-3 Torr | Poor vacuum | Excessive O2/H2O; coating will fail |
| 1 x 10^-4 Torr | Marginal | Possible oxide inclusions; reduced adhesion |
| < 5 x 10^-5 Torr | Acceptable | Standard quality hard coatings |
| < 1 x 10^-5 Torr | Excellent | Highest quality; lowest contamination |
| < 1 x 10^-6 Torr | Research grade | Not required for industrial PVD |

```
Phase 1: Roughing (0-10 min)
  760 Torr -> ~50 mTorr
  Rotary vane pump only

Phase 2: Crossover (~50 mTorr)
  Open gate valve to turbo/cryo
  Close roughing valve to chamber

Phase 3: High vacuum (10-90 min)
  50 mTorr -> < 5 x 10^-5 Torr
  Turbo/cryo pump + foreline backing

Total: 30-90 min (chamber dependent)
```

---

## Phase 6 -- Leak Detection

Y: 22.8" to 27.8".

| Source | Likelihood | Fix |
|---|---|---|
| O-ring seals (door, viewport) | HIGHEST | Replace O-ring; clean groove; check for nicks |
| Gas line fittings | HIGH | Retighten VCR/Swagelok; replace gasket |
| Feedthroughs (electrical, water) | MODERATE | Tighten; replace if corroded |
| Chamber wall (weld crack) | LOW | He leak detect to locate; weld repair |
| Virtual leak (trapped gas) | COMMON | Bake-out at 100-200 C; redesign fixture |

---

## Phase 7 -- Maintenance + Common Problems

Y: 28.7" to 32.3".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SLOW PUMP-DOWN | Contaminated chamber, water vapor, O-ring degradation | Bake-out; replace O-rings; check pump oil |
| 2 | 6.33" | CAN'T REACH BASE VACUUM | Leak or outgassing; pump degradation | Leak check; service pump; check foreline trap |
| 3 | 12.16" | PUMP OIL BACKSTREAMING | Cold trap missing or saturated; turbo bearing wear | Install/regenerate cold trap; service turbo |
| 4 | 18.0" | GAUGE READING UNSTABLE | Contaminated gauge filament; gas burst | Clean or replace gauge; check for intermittent leak |

---

## Phase 8 -- Footer

Standard. Title: `Vacuum System Setup -- PVD`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 9 -- Review

- [ ] Headline `VACUUM SYSTEM SETUP` 80pt
- [ ] Orientation strip with poster 6 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 10 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Vacuum System Setup PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
