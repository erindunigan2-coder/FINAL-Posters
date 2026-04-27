---
Project: Plating Posters Inc
Poster Number: 197
Title: "Aluminum Conversion Coating -- Rinse (Post-Coat)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.7)"
Technical Source: Post-coat rinse stage for Ti/Zr and non-chromate aluminum conversion coatings. Covers DI water requirements for ultra-thin films, gentle handling of the fresh coating, and prevention of water spotting.
Process Scope: Aluminum conversion coating -- Stage 6 rinse (post-coat)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - Rinse
  - PostCoat
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #197 -- Construction Workup
## Aluminum Conversion Coating -- Rinse (Post-Coat)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the post-coat rinse poster for CC-06. The freshly deposited Ti/Zr film is 20--100 nm thick -- thinner than a wavelength of visible light. Any mineral deposit from tap water, any aggressive spray impact, any extended soak will compromise this film. DI water is not optional here. It is the only acceptable rinse medium.

The key teaching point: the post-coat rinse must be gentle, brief, and mineral-free. The coating solution residues must be removed without damaging the ultra-thin film. Think of it as rinsing a soap bubble -- the goal is to clean without breaking.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for flow boxes, callout panels, table rows, and accent borders
- Arrow/line elements connecting flow boxes in sequence
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Stage detail panel (Block B -- HERO):** Parameters, purpose, and film fragility callout.
2. **DI water critical explanation (Block C):** Why minerals visible on 20--100 nm film.
3. **Handling guidelines (Block D):** Do's and don'ts for the fresh coating.
4. **Comparison: this rinse vs. other processes (Block E).**
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- RINSE STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (parameters, purpose, film fragility)
  Block C: Why DI water is critical for post-coat rinsing

ZONE 3 -- HANDLING GUIDELINES (15.5"--22.0" / ~6.5" tall)
  Block D: Do's and Don'ts for the fresh Ti/Zr coating

ZONE 4 -- RINSE COMPARISON ACROSS PROCESSES (22.0"--28.5" / ~6.5" tall)
  Block E: How this rinse differs from post-coat rinses in other conversion coating processes

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 76 pt, `#F0EDE8`, letter spacing -4
- Text: `ALUMINUM CONVERSION COATING`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Stage 6 -- Rinse (Post-Coat)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `20 nanometers of protection. DI water only. Gentle rinse. Brief contact. Every mineral deposit is visible at this scale.`
- Y: 2.2"

---

### ZONE 2 -- Rinse Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE -- POST-COAT (DI WATER CRITICAL)`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 8.5". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge:
- Rounded rect 2.0" x 0.4", fill `#2EC4B6`
- Text: `STAGE 6 -- POST-COAT RINSE` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
```
Water:           DI water -- CRITICAL (no tap water)
Temperature:     Ambient
Conductivity:    < 10 uS/cm
Method:          Gentle immersion or low-pressure spray
Time:            15--60 sec
Agitation:       Minimal -- do not damage fresh film
```

Purpose callout (right side):
- Rounded rect W: 10.0", H: 2.0", fill `#252B3D`, top accent `#27AE60`
- Title: `PURPOSE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body (Inter Regular 14 pt `#F0EDE8`):
- Text: `Remove residual coating solution from the surface without damaging the ultra-thin ZrO2 film. Prevent mineral deposits that interfere with paint adhesion and appearance.`

Film fragility callout (right side, below purpose):
- Rounded rect W: 10.0", H: 1.5", fill `#252B3D`, top accent `#E05C5C`
- Title: `FILM FRAGILITY` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Body (Inter Medium 14 pt `#F0EDE8`):
- Text: `The coating is 20--100 nm. A human hair is ~80,000 nm. Aggressive spray or abrasive contact will strip the film entirely. Handle with care.`

---

**BLOCK C -- Why DI Water Is Critical**

Y: 9.0" to 15.0". Two panels side-by-side.

**Left -- The Scale Problem:**
- Rounded rect, X: 0.5", Y: 9.0", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `THE SCALE PROBLEM` -- Barlow SemiBold, 20 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
A single water drop on a part, dried from tap water
containing 300 ppm TDS, leaves a mineral spot
approximately 50--100 nm thick.

The Zr coating is 20--100 nm thick.

That means the mineral deposit from ONE WATER DROP
can be AS THICK AS THE COATING ITSELF.

On a hex chromate coating (250--1000 nm), this
water spot is invisible.

On a Zr coating, it is 50--100% of the total film.
It WILL show up as poor paint adhesion.
```

**Right -- DI Water Eliminates the Problem:**
- Rounded rect, X: 12.0", Y: 9.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#27AE60`
- Title: `DI WATER -- THE ONLY OPTION` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
DI water at < 10 uS/cm contains essentially
zero dissolved minerals.

A DI water drop leaves NO visible residue when
dried -- even on a 20 nm film.

Requirements for this rinse stage:
  Conductivity:  < 10 uS/cm (target < 5)
  TDS:           < 5 ppm
  Chloride:      < 1 ppm
  pH:            5.5--7.5

Monitor with inline conductivity meter.
Replace DI resin beds before breakthrough.
Alarm set at 20 uS/cm for early warning.
```

---

### ZONE 3 -- Handling Guidelines

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `HANDLING THE FRESH COATING -- DO's AND DON'Ts`

**BLOCK D -- Two-Column Do/Don't Panel**

Y: 16.3" to 21.8". Two panels.

**Left -- DO:**
- Rounded rect, X: 0.5", Y: 16.3", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `DO` -- Barlow Condensed ExtraBold, 28 pt, `#27AE60`

Items (Inter Regular 14 pt `#F0EDE8`, bullet `#27AE60`):
```
- Use DI water for ALL post-coat rinsing
- Keep rinse brief (15--60 sec)
- Use gentle immersion or low-pressure spray
- Transfer promptly to dry/seal stage
- Monitor DI conductivity continuously
- Ensure clean racking -- no metallic contact points
- Allow adequate drain time before oven entry
```

**Right -- DON'T:**
- Rounded rect, X: 12.0", Y: 16.3", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E05C5C`
- Title: `DON'T` -- Barlow Condensed ExtraBold, 28 pt, `#E05C5C`

Items (Inter Regular 14 pt `#F0EDE8`, bullet `#E05C5C`):
```
- Use tap water (mineral deposits on film)
- Use aggressive high-pressure spray (strips film)
- Over-rinse -- extended immersion can dissolve film
- Touch the coating surface (fingerprints = defects)
- Allow parts to air-dry before oven (water spots)
- Stack or contact parts before drying/sealing
- Neglect DI system maintenance
```

---

### ZONE 4 -- Rinse Comparison Across Processes

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `POST-COAT RINSE -- HOW Ti/Zr COMPARES`

**BLOCK E -- Comparison Table**

Y: 22.9" to 28.3". Rounded rect, X: 0.5", W: 23.0", H: 5.0", fill `#1E2435`, radius 8.

| Process | Film Thickness | Rinse Sensitivity | Water Requirement | Special Caution |
|---|---|---|---|---|
| Ti/Zr Conversion | 20--100 nm | VERY HIGH | DI water mandatory | Gentle; brief; mineral-free |
| Hex Chromate (Al) | 250--1000 nm | HIGH | Cold water only | NO hot water; coating still curing |
| Tri Chromate (Al) | 20--100 nm | HIGH | DI preferred | Similar to Ti/Zr sensitivity |
| Zinc Phosphate | 2--25 um | MODERATE | Fresh water | Prompt transfer; no efflorescence |
| Iron Phosphate | 0.25--1.0 um | LOW-MOD | Fresh water | No hot water (thermal shock) |

Data: JetBrains Mono 12 pt. Process names: Inter Medium 13 pt.
Alternating rows: `#1E2435` / `#252B3D`.

Below table:
- Text: `Ti/Zr coatings are the most rinse-sensitive process in the conversion coating family. The film is so thin that contaminants invisible on thicker coatings become significant defects.` -- Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WATER SPOTS | Tap water minerals; DI system breakthrough | Check DI conductivity; replace resin beds |
| 2 | 6.33" | COATING STRIPPED | Aggressive spray pressure; over-rinsing | Reduce pressure; limit rinse to 15--60 sec |
| 3 | 12.16" | FINGERPRINT MARKS | Handling before parts are sealed/dried | Enforce no-touch policy until after drying |
| 4 | 18.0" | POOR PAINT ADHESION | Mineral deposits from hard water rinse; residual coating solution | Switch to DI; verify conductivity daily |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Rinse (Post-Coat)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for post-coat rinse stages in Ti/Zr and non-chromate conversion coating lines. Water quality requirements vary by process supplier and specification. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Rinse Post-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "scale problem" comparison in Zone 2 is the hook -- showing that a tap water mineral deposit can be as thick as the coating itself. That single comparison makes the DI water requirement viscerally obvious. The cross-process rinse comparison in Zone 4 contextualizes Ti/Zr sensitivity against processes the operator may already know -- "your zinc phosphate line could tolerate tap water; your Zr line cannot."

The Do/Don't panel in Zone 3 is designed for wall-at-a-glance use -- an operator walking by should be able to read the green bullets (DO) and red bullets (DON'T) in three seconds.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #197 -- Construction Workup v1.0*
*2026-04-26*
