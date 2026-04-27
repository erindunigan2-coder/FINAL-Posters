---
Project: Plating Posters Inc
Poster Number: 34
Title: "Activation -- Zinc (Alkaline)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Acid activation for alkaline zinc plating line (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #34 -- Construction Workup
## Activation -- Zinc (Alkaline)

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 3 of the alkaline zinc process. Acid activation removes surface oxides, exposes bare metal, and ensures zinc adhesion. Short immersion, critical results. The hero visual is a magnified cross-section of a steel surface showing oxide layer removal by acid attack.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Surface cross-section hero (Block B):** A magnified schematic cross-section showing the steel substrate with an oxide layer on top, and acid molecules attacking/dissolving the oxide. Left side = before (oxide present), right side = after (clean metal exposed). Built with layered rectangles and small arrow/bubble elements.
2. **HCl vs. H2SO4 comparison (Block E):** Side-by-side callout -- which acid to use and when.
3. **Hydrogen embrittlement warning (Block G):** Prominent safety callout specific to high-strength steel.

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Standard palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- SURFACE CROSS-SECTION HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- ACTIVATION PARAMETERS + HCl vs H2SO4 (14.0"--22.0" / ~8.0")
ZONE 5 -- COMMON PROBLEMS & FIXES (22.0"--28.0" / ~6.0")
ZONE 6 -- H-EMBRITTLEMENT WARNING + SAFETY (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Zinc (Alkaline) -- Stage 3 of 8` -- Barlow SemiBold, 34 pt, `#E8A020` (Amber). X: 0.5", Y: 1.4".

**Tagline:** `Fifteen seconds of acid contact that determines whether your zinc sticks or peels.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. All others dimmed.

Below: `Before: Clean surface with invisible oxide film  -->  After: Bare metal, oxide-free, ready to plate`

---

### ZONE 3 -- Surface Cross-Section Hero

**Section label:** `WHAT ACTIVATION DOES -- THE SURFACE UP CLOSE` -- Y: 4.4".

**BLOCK B -- Magnified Surface Diagram**

Y: 5.0" to 13.5". Two side-by-side cross-section views:

**Left half -- BEFORE (X: 0.5", W: 11.0"):**
- Title: `BEFORE ACTIVATION` -- Barlow SemiBold 20 pt `#E05C5C`
- Steel substrate: thick horizontal rect, X: 1.0", Y: 8.0", W: 10.0", H: 3.0", fill `#C8D0D8` (Bright Silver)
- Oxide layer: thin horizontal rect on top of substrate, H: 0.5", fill `#E05C5C` at 40% (rust-toned)
- Label on oxide: `Iron oxide (Fe2O3)` -- JetBrains Mono 14 pt `#E05C5C`
- Label on substrate: `Steel substrate` -- JetBrains Mono 14 pt `#C8D0D8`
- Small downward arrows above oxide: `Zinc won't adhere to oxide` -- Inter Medium 13 pt `#E05C5C`

**Right half -- AFTER (X: 12.5", W: 11.0"):**
- Title: `AFTER ACTIVATION` -- Barlow SemiBold 20 pt `#27AE60`
- Steel substrate: same dimensions, fill `#C8D0D8`
- NO oxide layer -- clean top surface
- Small star/sparkle markers along the top edge of substrate (4--6 small shapes, fill `#27AE60`)
- Label: `Clean, active metal surface` -- JetBrains Mono 14 pt `#27AE60`
- Upward arrows above surface: `Zinc deposits directly onto metal` -- Inter Medium 13 pt `#27AE60`

**Center divider:**
- Vertical dashed line at X: 12.0", `#3A4055`, 2 pt
- Arrow pointing right across the line: `ACID ACTIVATION` -- Barlow SemiBold 14 pt `#E8A020`

**Acid action detail (below cross-sections, Y: 12.0"):**
- Rounded rect, X: 2.0", W: 20.0", H: 1.5", fill `#1E2435`
- Interior text (Inter Regular 14 pt `#F0EDE8`, line height 150%):
  - `The acid dissolves the oxide layer: Fe2O3 + 6HCl --> 2FeCl3 + 3H2O`
  - `This exposes fresh, chemically active iron -- the ideal surface for zinc adhesion.`
  - Formula in JetBrains Mono 14 pt `#E8A020`.

---

### ZONE 4 -- Parameters + HCl vs H2SO4

**Section label:** `ACTIVATION PARAMETERS` -- Y: 14.2".

**Left -- Parameter Table (X: 0.5", W: 11.0"):**

Header: `ACID ACTIVATION` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Acid type | HCl (hydrochloric) or H2SO4 (sulfuric) |
| HCl concentration | 5--10% v/v (50--100 mL/L) |
| H2SO4 concentration | 5--15% v/v (50--150 mL/L) |
| Temperature | Ambient (no heating) |
| Time | 15--60 sec |
| Agitation | Gentle -- part movement only |
| Substrate | Steel, cast iron, spring steel |
| Rinse after | Immediate -- do not let parts dry |

**Right -- HCl vs H2SO4 Comparison (X: 12.0", W: 11.5"):**

Two stacked callout boxes:

**Top -- HCl (Y: 14.8", H: 3.2"):**
- Rounded rect fill `#1E2435`, left accent `#E8A020`
- Title: `HYDROCHLORIC ACID (HCl)` -- Barlow SemiBold 18 pt `#E8A020`
- Bullets:
  - `Most common choice for steel activation`
  - `Dissolves oxide faster than H2SO4`
  - `Less risk of hydrogen absorption (lower H-embrittlement risk)`
  - `Fumes -- ventilation required`
  - `Attacks copper and brass -- avoid for mixed-metal racks`

**Bottom -- H2SO4 (Y: 18.3", H: 3.2"):**
- Rounded rect fill `#1E2435`, left accent `#2EC4B6`
- Title: `SULFURIC ACID (H2SO4)` -- Barlow SemiBold 18 pt `#2EC4B6`
- Bullets:
  - `Lower fuming than HCl -- better for enclosed areas`
  - `Slower oxide removal -- longer immersion needed`
  - `Higher risk of hydrogen absorption on steel`
  - `Better for copper substrates (does not attack Cu)`
  - `More economical in high-volume operations`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT ACTIVATION` -- Y: 22.2".

**Problem Table (5 rows):**

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Under-activation | Zinc peels, poor adhesion | Time too short or acid too weak | Extend time; check acid concentration |
| Over-activation | Rough zinc, pitting | Time too long or acid too strong | Reduce time; dilute acid |
| H-embrittlement | Delayed fracture (HTS parts) | Hydrogen absorbed during acid contact | Limit to 15--30 sec; bake at 375 F within 4 hr |
| Smut on surface | Dark residue after activation | Carbon smut from high-C steel | Add proprietary de-smutter; light mechanical action |
| Flash rust | Orange tint before reaching zinc tank | Parts dried between activation and rinse | Immediate transfer; never let parts air-dry |

---

### ZONE 6 -- H-Embrittlement Warning + Safety

**Section label:** `CRITICAL SAFETY -- HYDROGEN EMBRITTLEMENT` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`. Y: 28.2".

**Left -- H-Embrittlement Panel (X: 0.5", W: 14.0"):**
- Rounded rect fill `#1E2435`, FULL border 2 pt `#E05C5C` (not just left accent -- full box border for emphasis)
- Title: `HYDROGEN EMBRITTLEMENT WARNING` -- Barlow SemiBold 20 pt `#E05C5C`
- Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `High-strength steel (>= 145 ksi / >= 31 HRC) absorbs hydrogen during acid contact.`
  - `Atomic hydrogen diffuses into the steel lattice and causes delayed brittle fracture.`
  - `REQUIREMENTS FOR HIGH-STRENGTH STEEL:`
  - `* Limit acid activation to 15--30 seconds maximum`
  - `* Bake at 375 F (191 C) within 4 hours of plating`
  - `* Hold bake for 23 hours minimum (per ASTM B850)`
  - `* Never skip the bake -- parts will fail in service`
- Key spec: `Reference: ASTM B850, AMS 2759` -- JetBrains Mono 12 pt `#E05C5C`

**Right -- General Safety (X: 15.0", W: 8.5"):**
- Rounded rect fill `#1E2435`, left accent `#E8A020`
- Title: `ACID HANDLING SAFETY` -- Barlow SemiBold 18 pt `#E8A020`
- Bullets:
  - `HCl fumes: corrosive -- hood ventilation required`
  - `H2SO4: exothermic on dilution -- add acid to water, NEVER reverse`
  - `Chemical splash goggles + face shield`
  - `Acid-resistant gloves and apron`
  - `Eyewash + safety shower within 10 sec`
  - `Neutralize spills with soda ash (Na2CO3)`

---

### ZONE 7 -- Footer Band

Standard footer. Title: `Activation -- Zinc (Alkaline)`. Version `v1.0 -- 2026`.

---

## Part 5 -- Grouping

| Group | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | Strip, Stage 3 highlighted |
| Zone 3 - Surface Hero | Before/after cross-section, acid reaction detail |
| Zone 4 - Parameters | Table + HCl vs H2SO4 comparison |
| Zone 5 - Problems | 5-row problem table |
| Zone 6 - Safety | H-embrittlement warning + acid safety |
| Zone 7 - Footer | Standard footer |

---

## Part 6 -- Light Edition Remap

Standard remap table. H-embrittlement border (`#E05C5C` -> `#B83E3E`) -- verify visibility on light background.

| Dark | Light |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

---

## Part 7 -- Export Checklist

Six files: `Activation Zinc Alkaline -- Dark/Light -- 24x36/18x24/Digital -- Print.pdf`

---

*Elara -- Poster #34 -- Construction Workup v1.0 -- 2026-04-25*
