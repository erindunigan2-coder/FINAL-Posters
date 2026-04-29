---
Project: Plating Posters Inc
Poster Number: 433
Title: "Loading -- ALD System"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-28T00:00:00
Source: Poster 433 — Loading ALD System — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - ALD
  - AtomicLayerDeposition
  - Loading
  - ThinFilm
  - ClusterTF04
  - v1
---

# Claude Chat Generation Prompt -- Poster #433
## Loading -- ALD System
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-28).*

---

> **IMPORTANT:** Generate as SVG or HTML visual artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `LOADING` -- `88` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `ALD -- Stage 3 of 10 -- Reactor Loading and Thermal Stabilization` -- `32` pt `#C8D0D8`. Y: **1.4"**.
### Step 3 -- `ALD reactors come in six distinct flavors -- from single-wafer R&D tools to continuous roll-to-roll production lines. Temperature stability in the ALD window is universal to all of them.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 5 of 10 highlighted.

---

## Phase 4 -- Reactor Types Hero

Y: 5.0" to 15.3".

| Panel | Position | Reactor Type | Accent | Throughput |
|---|---|---|---|---|
| 1 | R1C1 (X: 0.5", Y: 5.0") | Cross-Flow (Viscous Flow) | `#2EC4B6` | Low-Medium |
| 2 | R1C2 (X: 8.17", Y: 5.0") | Showerhead | `#E8A020` | Medium |
| 3 | R1C3 (X: 15.83", Y: 5.0") | Batch Vertical Furnace | `#27AE60` | High |
| 4 | R2C1 (X: 0.5", Y: 10.3") | Spatial ALD | `#27AE60` | Very High |
| 5 | R2C2 (X: 8.17", Y: 10.3") | Rotary / Fluidized Bed | `#C8D0D8` | Batch (kg-scale) |
| 6 | R2C3 (X: 15.83", Y: 10.3") | Roll-to-Roll | `#E8A020` | Continuous |

---

## Phase 5 -- Loading Procedure + ALD Window

Section: `350 degC`.

```
1. Open reactor (verify no precursor flow, heater at setpoint)
2. Place substrate on heated susceptor / chuck
3. Verify substrate centered and seated flat
4. Close reactor -- check seal (O-ring or face seal)
5. Begin pump-down to base pressure
6. Wait for thermal stabilization (5--15 min at setpoint)
```

```
The ALD window is the temperature range where:
- Growth per cycle (GPC) is CONSTANT
- Reactions are truly self-limiting
- Film quality is optimal

BELOW WINDOW:
  Precursor condenses on surface (too cold)
  OR reaction is too slow (incomplete)
  GPC is variable and unreliable

WITHIN WINDOW:
  GPC = constant (~0.11 nm/cycle for Al2O3)
  Self-limiting behavior confirmed
  This is where you operate

ABOVE WINDOW:
  Precursor decomposes in gas phase (CVD mode)
  OR precursor desorbs before reacting
  GPC becomes erratic or zero
```

```
TMA / H2O (Al2O3):
  Below window: < 150 degC
  ALD window:   150--350 degC
  Above window: > 350 degC
  Target:       200 degC (standard)
```

---

## Phase 6 -- Pump-Down + Common Mistakes

Y: 24.2" to 28.5".
Section: `1 Torr | 1--5 min | Mechanical pump |`.

| Phase | Pressure | Time | Action |
|---|---|---|---|
| Roughing | Atm -> 1 Torr | 1--5 min | Mechanical pump |
| Base vacuum | 1 Torr -> 0.1--1 Torr | 5--15 min | Continue pumping; verify leak rate |
| Thermal stabilization | At base pressure | 5--15 min | Heater at setpoint; substrate equilibrating |
| Carrier gas flow | Base pressure + carrier | 2--5 min | Start N2/Ar carrier; pressure stabilizes at working level |

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CYCLING TOO SOON | Substrate not thermally stabilized | Wait 5--15 min after heater reaches setpoint; verify with thermocouple |
| 2 | 6.33" | TEMPERATURE OUTSIDE WINDOW | Heater setpoint incorrect or gradient | Calibrate; verify with thermocouple survey; check reactor uniformity spec |
| 3 | 12.16" | CONTAMINATION ON SUSCEPTOR | Precursor residue from previous runs | Clean susceptor regularly; run ALD clean cycles (O3 or plasma) |
| 4 | 18.0" | SUBSTRATE MISALIGNMENT | Part not centered on heated zone | Verify alignment; use mechanical stops or vacuum chuck |

---

## Phase 7 -- Footer

Standard. Title: `Loading -- ALD System`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge. Consult your process supplier for application-specific guidance.`

---

## Phase 8 -- Review

- [ ] Headline `LOADING` 88pt
- [ ] Orientation strip with poster 5 highlighted
- [ ] Footer with disclaimer and version

---

## Phase 9 -- Light Remap & Export

Standard remap. Verify accent legibility on light background.

Six files: `Loading ALD System -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-28 | Initial. |
