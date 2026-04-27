---
Project: Plating Posters Inc
Poster Number: 598
Title: "Loading -- Plasma Nitriding System"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5, Sections 5.2, 5.6)"
Process Scope: Loading, fixturing, and part arrangement for plasma nitriding systems
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - Loading
  - Fixturing
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #598 -- Construction Workup
## Loading -- Plasma Nitriding System

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading a plasma nitriding vessel is fundamentally different from loading a gas nitriding retort. Every part is electrically connected to the cathode. Part spacing governs plasma uniformity. The hollow cathode effect lurks anywhere geometry creates concentrated glow discharge. This poster is about getting parts into the chamber correctly.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Chamber cross-section hero (Block B):** Schematic showing vessel wall (anode), parts on cathode, plasma sheath visualization, spacing callouts.
2. **Hollow cathode effect diagram (Block D):** Visual showing what happens when parts are too close or have small holes.
3. **Loading rules checklist (Block E):** Critical spacing and orientation rules.
4. **Active screen vs. conventional comparison (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- CHAMBER CROSS-SECTION HERO (2.9"--15.5")
ZONE 3 -- HOLLOW CATHODE EFFECT (15.5"--22.0")
ZONE 4 -- LOADING RULES + ACTIVE SCREEN (22.0"--32.5")
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding System -- Every Part is an Electrode` -- 32 pt `#2EC4B6`.
**Tagline:** `In gas nitriding, you load a furnace. In plasma nitriding, you build a circuit. Spacing and contact are everything.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `10 mm` -- 72 pt `#E8A020`
- Label: `Minimum part spacing to prevent hollow cathode effect` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Chamber Cross-Section (HERO)

**Section label:** `INSIDE THE PLASMA NITRIDING VESSEL` -- Y: 3.1".

**BLOCK B -- Chamber Schematic (Y: 3.8" to 15.3")**

Large cross-section diagram:

**Vessel wall (anode):**
- Rounded rect, X: 1.0", Y: 4.5", W: 22.0", H: 10.0"
- Fill: `#252B3D`, border 3 pt `#C8D0D8`
- Label at top: `VESSEL WALL (ANODE +)` -- Barlow SemiBold 16 pt `#C8D0D8`

**Cathode plate (bottom):**
- Rect, X: 3.0", Y: 13.0", W: 18.0", H: 0.5"
- Fill: `#3A4055`, border 2 pt `#E8A020`
- Label: `CATHODE PLATE (-)` -- Barlow SemiBold 14 pt `#E8A020`

**Parts on cathode (3 representative shapes):**
- Left part: Tall rect (shaft), X: 5.0", Y: 7.0", W: 1.5", H: 6.0", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Center part: Wide rect (plate), X: 9.5", Y: 10.0", W: 4.0", H: 3.0", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Right part: Tall rect (gear), X: 17.0", Y: 7.5", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`

**Plasma sheath (glow):**
- Dashed border around each part, 0.15" offset, stroke 2 pt `#9B59B6` (violet), dashed
- Label: `Plasma sheath (visible violet glow)` -- Inter Medium 12 pt `#9B59B6`

**Spacing callouts:**
- Double-headed arrows between parts: `>= 10 mm` JetBrains Mono 14 pt `#E8A020`
- Arrow from part to vessel wall: `Gap ensures uniform plasma density` Inter Regular 12 pt `#F0EDE8` at 70%

**DC power supply symbol (top center):**
- Rect, X: 10.0", Y: 4.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC POWER SUPPLY (400--1000 V)` JetBrains Mono 11 pt `#E8A020`
- Lines to vessel wall (+) and cathode plate (-)

**Gas inlet / outlet labels:**
- Left: `N2/H2 IN` with arrow, JetBrains Mono 12 pt `#2EC4B6`
- Right: `TO VACUUM PUMP` with arrow, JetBrains Mono 12 pt `#F0EDE8` at 60%

---

### ZONE 3 -- Hollow Cathode Effect

**Section label:** `THE HOLLOW CATHODE EFFECT -- KNOW THE ENEMY` -- Y: 15.7". `#E05C5C`.

**BLOCK D -- Two-Panel Comparison (Y: 16.3" to 21.8")**

**Left -- PROBLEM (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `HOLLOW CATHODE = ARCING` -- Barlow SemiBold 20 pt `#E05C5C`
- Diagram: Two closely spaced parts with concentrated glow between them
- Text:
  - `When parts are too close, plasma concentrates in the narrow gap`
  - `Local temperature spikes; surface damage; melting possible`
  - `Also occurs inside blind holes and small bores`
  - `RULE: Minimum hole diameter = 3x hole depth`
  - `RULE: Minimum part spacing = 10 mm`

**Right -- SOLUTION (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#27AE60`
- Title: `PREVENTION` -- Barlow SemiBold 20 pt `#27AE60`
- Text:
  - `Maintain 10 mm minimum between all parts`
  - `Plug blind holes that violate 3x rule`
  - `Use pulsed DC (duty cycle control) to moderate plasma intensity`
  - `Active Screen Plasma Nitriding (ASPN) eliminates the problem entirely`
  - `ASPN: Screen is the cathode, parts at floating potential -- no arcing on parts`

---

### ZONE 4 -- Loading Rules + Active Screen

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: Loading Rules Checklist (X: 0.5", W: 11.0")**

Section label: `LOADING RULES` -- Barlow Condensed ExtraBold 22 pt.

| # | Rule | Why |
|---|---|---|
| 1 | Every part must have electrical contact to cathode | No contact = no plasma = no nitriding |
| 2 | Minimum 10 mm spacing between all parts | Prevent hollow cathode arcing |
| 3 | Blind holes: min diameter = 3x depth | Same reason -- concentrated plasma |
| 4 | Use non-magnetic fixtures where possible | Magnetic fixtures can distort plasma field |
| 5 | Thermocouple placement on representative parts | Pulsed DC adjusts duty cycle based on TC feedback |
| 6 | Parts should not shadow each other | Shadowed areas receive less ion bombardment |
| 7 | Flat parts: set vertical or spaced on pins | Contact surfaces will not nitride |

Each row: alternating `#1E2435` / `#252B3D`, H: 1.2".

**Right -- BLOCK F: Active Screen vs. Conventional (X: 12.0", W: 11.5")**

Section label: `ACTIVE SCREEN PLASMA NITRIDING (ASPN)` -- Barlow Condensed ExtraBold 22 pt.

Two stacked callout boxes:

*Top -- Conventional DC Plasma:*
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E8A020`
- `Parts = cathode (-)` / `Vessel wall = anode (+)` / `Plasma forms directly on part surfaces`
- `PRO: Direct ion bombardment -- sputters passive films on stainless`
- `CON: Arcing on complex geometries; edge effect; hollow cathode`

*Bottom -- Active Screen (ASPN):*
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- `Metal screen = cathode (-)` / `Parts at floating or low bias potential`
- `Plasma forms on the screen, not the parts`
- `Nitrogen species diffuse from screen to parts`
- `PRO: No arcing; uniform treatment; handles complex geometry`
- `CON: Higher equipment cost; slightly different compound layer characteristics`
- Badge: `INCREASINGLY COMMON IN PRODUCTION` JetBrains Mono 12 pt `#27AE60`

---

### ZONE 5 -- Footer

Standard footer. Title: `Loading -- Plasma Nitriding System`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

Note: `#9B59B6` (violet) used for plasma sheath visualization is NOT in the locked palette. For Light edition, remap to `#7D3C98` (darker violet). This is a one-off accent specific to this poster's plasma visualization -- document it in the generation prompt.

---

*Alaina -- Poster #598 -- Construction Workup v1.0 -- 2026-04-26*
