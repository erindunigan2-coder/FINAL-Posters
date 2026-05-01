---
Project: Plating Posters Inc
Poster Number: 573
Title: "Atmosphere & Cycle Control -- Vacuum Carburizing"
Document Type: Claude Chat Generation Prompt
Version: v1.0
Status: Active
Created: 2026-04-30T00:00:00
Source: Poster 573 — Atmosphere and Cycle Control Vacuum Carburizing — Construction Workup.md
Editions: Dark (primary) + Light (remap)
tags:
  - ClaudeChatPrompt
  - VacuumCarburizing
  - LPC
  - AtmosphereControl
  - CycleControl
  - ClusterDH02
  - v1
---

# Claude Chat Generation Prompt -- Poster #573
## Atmosphere & Cycle Control -- Vacuum Carburizing
### Version 1.0 | Dark + Light

*Elara from CW v1.0 (2026-04-30).*

---

> **IMPORTANT:** Generate as HTML artifact. 24 x 36" portrait. Dark edition first.

---

## Phase 1 -- Foundation

Standard: 24x36", `#1A1F2E`, locked palette, 0.5" safe zone. iOS Liquid Glass aesthetic. Fonts: Barlow Condensed 800 (headlines), Barlow 600 (subheads), Inter 400/500 (body), JetBrains Mono 400 (data/params).

---

## Phase 2 -- Header

### Step 1 -- `ATMOSPHERE & CYCLE CONTROL` -- `80` pt `#F0EDE8`. Y: **0.5"**.
### Step 2 -- `Vacuum Carburizing (LPC) -- Stage 4 of 9` -- `32` pt `#27AE60`. Y: **1.4"**.
### Step 3 -- `No oxygen probe. No dew point analyzer. In vacuum carburizing, the recipe IS the control. Computer-simulated boost/diffuse pulses replace real-time atmosphere measurement.` -- `20` pt at 65%. Y: **2.1"**.

---

## Phase 3 -- Orientation Strip

Poster 6 of 9. Stage 4 highlighted (Emerald). Before/After: `Furnace at carburizing temperature under vacuum --> Target carbon profile achieved via pulsed recipe`.

---

## Phase 4 -- Boost/Diffuse Pulse Diagram (HERO)

Y: 4.2" to 15.5". Section label: `THE BOOST/DIFFUSE CYCLE -- HOW LPC BUILDS A CARBON PROFILE`.

Large diagram area (H: 9.0", fill `#1E2435`) showing alternating pressure pulse timeline:

Boost pulses (Emerald tinted rectangles at 5--15 mbar height) alternating with diffuse phases (baseline at <1 mbar). Diffuse phases get progressively LONGER as recipe advances.

| Phase | Duration | Pressure | Label |
|---|---|---|---|
| Boost 1 | 2 min | 5--15 mbar | C2H2 ON |
| Diffuse 1 | 5 min | <1 mbar | VACUUM |
| Boost 2 | 2 min | 5--15 mbar | C2H2 ON |
| Diffuse 2 | 8 min | <1 mbar | VACUUM |
| Boost 3 | 1.5 min | 5--15 mbar | C2H2 ON |
| Diffuse 3 | 12 min | <1 mbar | VACUUM |
| ... | ... | ... | REPEAT 5--30+ CYCLES |

Key annotations: BOOST = acetylene decomposes on hot surface, depositing atomic carbon. DIFFUSE = no gas, carbon diffuses inward via Fick's Law. Diffuse phases get longer (early: surface not saturated; late: driving carbon deeper).

Parameters below: Boost 30 sec to 5 min; Diffuse 2--30 min; 5--30+ cycles; Boost pressure 5--15 mbar via mass flow controllers.

---

## Phase 5 -- Carbon Source Gas Comparison

Y: 15.5" to 22.0". Section label: `CARBON SOURCE GASES -- ACETYLENE WINS`.

Three cards:

| Card | Gas | Accent | Stat | Key Points |
|---|---|---|---|---|
| 1 | Acetylene (C2H2) | `#27AE60` | PREFERRED FOR MODERN LPC | Clean decomposition; minimal soot at 5--15 mbar; excellent blind hole uniformity; industry standard; explosive (LEL 2.5%, 15 psig max) |
| 2 | Propane (C3H8) | `#E8A020` | OLDER SYSTEMS -- HIGHER SOOT RISK | Higher soot tendency; more complex decomposition; requires higher pressures; being phased out |
| 3 | Ethylene (C2H4) | `#C8D0D8` | ALTERNATIVE -- LESS COMMON | Intermediate soot; niche applications; limited simulation support; limited published data |

---

## Phase 6 -- Process Simulation + Key Difference

**Simulation (Y: 22.0"--28.5"):** Section label: `RECIPE-DRIVEN CONTROL -- SIMULATION SOFTWARE`.

*Left -- Software Tools (Emerald accent):* SimVac (dedicated LPC recipe simulator), CarbTool (general-purpose with LPC mode), DANTE (distortion + residual stress), DEFORM (FEA heat treatment module).

*Right -- Recipe Workflow (Teal accent):* 1. INPUT: steel, geometry, target ECD, surface C, furnace params. 2. SIMULATE: calculate optimal pulse sequence. 3. OUTPUT: recipe file for furnace controller. 4. VERIFY: test load, measure vs. simulation. 5. LOCK: approved recipe frozen for production. THIS IS NOT REAL-TIME CONTROL -- recipe is pre-calculated; furnace follows instructions.

**Key Difference (Y: 28.5"--32.5"):** Section label: `THE FUNDAMENTAL DIFFERENCE`. Full-width callout, Amber accent, two columns:

*Gas:* O2 probe reads Cp in REAL TIME. Operator adjusts. Control = FEEDBACK LOOP.
*LPC:* No probe. Recipe pre-calculated by simulation. Furnace executes blindly. Control = PRE-PROGRAMMED RECIPE.

Bottom line in Teal: `Both produce the same result. Gas carburizing is like driving with a speedometer. LPC is like programming a self-driving car.`

---

## Phase 7 -- Footer

Standard. Title: `Atmosphere & Cycle Control -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol. 4, AMS 2759/7E. Boost/diffuse recipes are specific to furnace, steel grade, part geometry, and target profile. Always validate with test loads.`

---

## Phase 8 -- Review

- [ ] Headline `ATMOSPHERE & CYCLE CONTROL` 80pt
- [ ] Stage 4 highlighted (Emerald)
- [ ] Boost/diffuse pulse timeline diagram (hero)
- [ ] Progressively longer diffuse phases visible
- [ ] 3 carbon source gas cards (C2H2 preferred)
- [ ] 4 simulation software packages
- [ ] Recipe workflow (5 steps)
- [ ] Gas vs. LPC fundamental difference callout
- [ ] Footer

---

## Phase 9 -- Light Remap & Export

Standard remap. Six files: `Atmosphere Cycle Control Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

| v1.0 | 2026-04-30 | Initial. |
