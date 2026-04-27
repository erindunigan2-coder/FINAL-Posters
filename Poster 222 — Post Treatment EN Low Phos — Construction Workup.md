---
Project: Plating Posters Inc
Poster Number: 222
Title: "Post Treatment -- EN (Low Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 1: EN Low-P, Poster 8)"
Process Scope: Post-treatment (heat treatment, passivation) for EN low phosphorus line (Stage 7 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - LowPhosphorus
  - PostTreatment
  - HeatTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEN-LP
---

# Poster #222 -- Construction Workup
## Post Treatment -- EN (Low Phos)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7 of 7. The final step -- where EN Low-P transforms from a good coating into a great one. Heat treatment at 350-400 C for 1 hour precipitates the Ni3P phase and drives hardness from 650-750 HV to 1000-1100 HV -- harder than hard chrome. For high-strength steel, hydrogen embrittlement relief at 190-210 C is not optional; it is a safety-critical requirement that must happen within 4 hours of plating.

Hero visual: a hardness-vs-temperature curve showing the dramatic hardness increase from heat treatment, with ASTM B733 class zones marked.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hardness curve hero (Block B):** A visual graph (built with rectangles and lines) showing hardness (HV) on Y-axis vs. heat treatment temperature on X-axis. Key inflection point at 350-400 C where hardness peaks.
2. **ASTM B733 class table (Block D):** Heat treatment classes from the standard.
3. **HE relief timing diagram (Block E):** Visual timeline showing the 4-hour window.
4. **Substrate-specific notes (Block F):** Different rules for steel, aluminum, titanium.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted
ZONE 3 -- HARDNESS CURVE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ASTM B733 HEAT TREATMENT CLASSES (14.5"--21.0" / ~6.5")
ZONE 5 -- HE RELIEF TIMING + SUBSTRATE NOTES (21.0"--27.5" / ~6.5")
ZONE 6 -- COMMON PROBLEMS + SAFETY (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`. Y: 0.5".

**Subheading:** `EN (Low Phos) -- Heat Treatment & Passivation -- Stage 7 of 7` -- 30 pt `#E8A020` (Amber). Y: 1.4".

**Tagline:** `650 HV out of the bath. 1100 HV out of the oven. Heat treatment transforms EN Low-P into one of the hardest coatings in metal finishing.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: As-plated Ni-P (650-750 HV, tensile stress)  -->  After: Heat-treated Ni-P (up to 1100 HV, stress-relieved)`

---

### ZONE 3 -- Hardness Curve Hero

**Section label:** `HARDNESS VS. HEAT TREATMENT TEMPERATURE` -- Y: 4.4".

**BLOCK B -- Hardness Curve Diagram (Y: 5.0" to 14.0")**

A stylized bar chart / step graph showing hardness at different heat treatment conditions:

**Y-axis (left side):** Hardness scale from 0 to 1200 HV
- Marked at: 200, 400, 600, 800, 1000, 1200
- Label: `HARDNESS (HV)` JetBrains Mono 14 pt, rotated 90 deg

**X-axis (bottom):** Treatment conditions (not continuous temperature -- discrete conditions)

| Condition | Temp | Time | Hardness (HV) | Bar Color |
|---|---|---|---|---|
| As-Plated | -- | -- | 650-750 | `#2EC4B6` |
| HE Relief | 190-210 C | 2-23 hr | 600-700 | `#E8A020` |
| Adhesion Bake (Al) | 120-150 C | 1-2 hr | 600-700 | `#E8A020` |
| Medium HT | 260-300 C | 1 hr | 800-900 | `#E8A020` |
| Maximum Hardness | 350-400 C | 1 hr | 1000-1100 | `#27AE60` |
| Hard Chrome (reference) | -- | -- | 850-1000 | `#3A4055` dashed outline |

Each bar: Rounded rect, W: 3.0", appropriate height proportional to HV value.

**Peak hardness callout (above the 350-400 C bar):**
- Rounded rect fill `#27AE60` at 20%, border 1 pt `#27AE60`
- `1000-1100 HV` Barlow Condensed ExtraBold 28 pt `#27AE60`
- `Ni3P precipitation hardening` Inter Regular 13 pt `#F0EDE8`
- `Exceeds hard chrome` Inter Medium 13 pt `#27AE60`

**Hard chrome reference line:**
- Horizontal dashed line at ~950 HV across full width
- Label: `Hard chrome reference (850-1000 HV)` JetBrains Mono 12 pt `#3A4055`

---

### ZONE 4 -- ASTM B733 Heat Treatment Classes

**Section label:** `ASTM B733 HEAT TREATMENT CLASSES` -- Y: 14.7".

**Full-width table:**

| Class | Treatment | Temperature | Time | Purpose | Substrate |
|---|---|---|---|---|---|
| Class 1 | As-plated | None | -- | No heat treatment required | General |
| Class 2 | Maximum hardness | 350-400 C (660-750 F) | 1 hr | Precipitate Ni3P; achieve 1000-1100 HV | Steel, iron |
| Class 3 | HE relief | 190-210 C (375-410 F) | 2-23 hr | Drive out absorbed hydrogen | High-strength steel |
| Class 4 | Adhesion (Al, non-HT) | 120-150 C (250-300 F) | 1-2 hr | Improve adhesion on non-heat-treatable Al | Aluminum |
| Class 5 | Adhesion (Al, age-hard) | 120-150 C (250-300 F) | 1-2 hr | Improve adhesion on age-hardened Al | Aluminum |
| Class 6 | Adhesion (Ti) | 300-320 C (570-610 F) | 1-4 hr | Adhesion on titanium alloys | Titanium |

Header: `#3A4055`. Data: JetBrains Mono 12 pt. Class column: Inter Medium 13 pt.

Note below table: `Classes can be combined -- e.g., HE relief (Class 3) followed by hardness treatment (Class 2). Always perform HE relief FIRST.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- HE Relief Timing + Substrate Notes

**Left -- HE Relief Timing (X: 0.5", W: 14.0"):**

Title: `HYDROGEN EMBRITTLEMENT RELIEF -- THE 4-HOUR WINDOW` Barlow SemiBold 20 pt `#E05C5C`

- Rounded rect fill `#1E2435`, FULL border 2 pt `#E05C5C`

**Visual timeline (horizontal bar):**
- Bar divided into segments: `PLATING COMPLETE` -> `0-4 hr: BAKE WINDOW` -> `> 4 hr: RISK ZONE`
- Bake window: fill `#27AE60` at 30%
- Risk zone: fill `#E05C5C` at 40%

Key rules:
- `High-strength steel (> 1000 MPa UTS or > 40 HRC):`
- `Bake at 190-210 C (375-410 F) within 4 hours of plating completion`
- `Minimum hold: 4 hours (per ASTM B849)`
- `Extended hold: up to 23 hours for critical aerospace parts (per ASTM B850)`
- `FAILURE TO BAKE = RISK OF CATASTROPHIC DELAYED BRITTLE FRACTURE`

Spec references: `ASTM B849 / ASTM B850 / AMS 2759/9` JetBrains Mono 12 pt `#E05C5C`

**Right -- Substrate-Specific Notes (X: 15.0", W: 8.5"):**

Title: `SUBSTRATE NOTES` Barlow SemiBold 18 pt `#E8A020`

**Aluminum:**
- `Do not exceed 290 C (554 F) -- differential thermal expansion causes delamination`
- `Adhesion bake at 120-150 C is safe for all Al alloys`

**Steel:**
- `Hardness HT at 350-400 C is standard`
- `Combine with HE relief: bake at 190 C first, then ramp to 350-400 C`

**Passivation (optional):**
- `Trivalent chromate passivation provides additional corrosion resistance`
- `Less common on Low-P than on Mid/High-P`

---

### ZONE 6 -- Common Problems + Safety

**Left -- Problems (X: 0.5", W: 14.0"):**

| Problem | Cause | Fix |
|---|---|---|
| Hardness not reached | Temp too low or time too short | Verify furnace calibration; hold full 1 hr at 350-400 C |
| Deposit cracking | Over-temperature or ramp too fast | Ramp gradually; do not exceed 400 C |
| Adhesion loss on Al | Exceeded 290 C | Reduce temperature; use adhesion bake only |
| Delayed fracture (HTS) | HE bake skipped or delayed past 4 hr | Always bake within 4 hr -- no exceptions |
| Discoloration | Oxidation during heat treatment | Use inert atmosphere (N2 or Ar) for critical parts |

**Right -- Safety (X: 15.0", W: 8.5"):**
- Title: `FURNACE SAFETY` `#E8A020`
- `Furnace operates at 190-400 C -- severe burn hazard`
- `Use heat-resistant gloves for part handling`
- `Ensure furnace ventilation -- hydrogen gas released during bake`
- `Do not open furnace door rapidly -- thermal shock risk to parts`
- `Inert atmosphere furnaces: asphyxiation hazard -- ventilate`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- EN (Low Phos)`. Version `v1.0 -- 2026`.

Disclaimer addition: `Heat treatment specifications per ASTM B733, ASTM B849, ASTM B850, AMS 2404/2405. Always verify requirements against the applicable drawing or purchase order specification.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. HE border (#E05C5C -> #B83E3E).
**Export:** Six files -- `Post Treatment EN Low-P -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the final poster in the EN Low-P cluster and arguably the most important after #220 (Main Tank). The hardness curve is the visual centerpiece -- it should be immediately striking that EN Low-P at 1000-1100 HV exceeds hard chrome. The HE relief timing diagram is a safety-critical element: delayed baking has caused real-world catastrophic failures in aerospace and automotive applications.

---

*Alaina -- Poster #222 -- Construction Workup v1.0 -- 2026-04-26*
