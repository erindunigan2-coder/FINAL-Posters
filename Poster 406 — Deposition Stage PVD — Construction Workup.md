---
Project: Plating Posters Inc
Poster Number: 406
Title: "Deposition Stage -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.7)"
Technical Source: PVD deposition covering sputtering and arc evaporation mechanics, film growth (Thornton Structure Zone Model), reactive gas control, in-situ quality indicators, thickness monitoring, and typical deposition times for TiN, TiAlN, CrN, and DLC.
Process Scope: PVD deposition stage (Stage 8 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PVD
  - Deposition
  - ThinFilm
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #406 -- Construction Workup
## Deposition Stage -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 10. This is the main event -- the coating is deposited. Whether by magnetron sputtering or cathodic arc evaporation, the physics of film growth determine every property the end user cares about: hardness, adhesion, color, friction coefficient, and oxidation resistance. This poster covers the deposition mechanism, the Thornton Structure Zone Model, reactive gas control, in-situ quality indicators, and coating-specific deposition parameters.

Design philosophy: the Thornton Zone Model diagram is the hero -- it is the single most important concept in understanding how PVD film structure relates to process parameters. Flanked by a deposition comparison table, in-situ quality indicators, and a coating property quick-reference strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Thornton Structure Zone Model (Block B -- HERO):** Four-column visual showing Zone 1, Zone T, Zone 2, and Zone 3 columnar structures. Each zone is a vertical column of simplified grain illustrations (rectangles/pillars) with progressively different morphologies. Achievable with stacked rectangles and labels.
2. **Deposition comparison table (Block C):** Sputtering vs. arc parameters side-by-side.
3. **In-situ quality indicators (Block D):** Color-coded diagnostic cards for plasma color, pressure stability, bias current, and arc stability.
4. **Coating properties quick-reference (Block E):** Compact table of 6 coatings with hardness, friction, max temp, and color.
5. **Common deposition failures (Block F):** Four failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Emerald -- deposition)
ZONE 3 -- THORNTON ZONE MODEL / HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- DEPOSITION COMPARISON TABLE (15.5"--21.5" / ~6.0")
ZONE 5 -- IN-SITU QUALITY INDICATORS (21.5"--27.0" / ~5.5")
ZONE 6 -- COMMON DEPOSITION FAILURES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEPOSITION STAGE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 8 of 10 -- Sputtering, Arc, Film Growth, and Reactive Gas Control` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The coating grows atom by atom. Sputtering delivers precision; arc delivers density. The Thornton Zone Model explains the rest. Every parameter shapes the film you get.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Ion etch complete, recipe parameters loaded (Stage 7) --> After: Coating deposited, ready for cooling`

---

### ZONE 3 -- Thornton Structure Zone Model (HERO)

**Section label:** `HOW PVD FILMS GROW -- THE THORNTON STRUCTURE ZONE MODEL` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Zone Model Diagram (Y: 5.0" to 13.0")**

Four columns representing the four Thornton zones, each containing a stylized grain structure illustration built from rectangles.

Full width within margins (23.0"). Each column: W: 5.25", H: 7.5", separated by 0.33" gaps.

**Column layout (left to right):**

| Zone | X | Fill | Top Accent | Grain Style |
|---|---|---|---|---|
| Zone 1 | 0.5" | `#1E2435` | `#E05C5C` (Coral) | Tall, narrow, separated columns with visible gaps (voided boundaries) |
| Zone T | 6.08" | `#1E2435` | `#E8A020` (Amber) | Dense fibrous columns, no gaps, slight taper |
| Zone 2 | 11.66" | `#1E2435` | `#2EC4B6` (Teal) | Wider columnar with fully dense boundaries |
| Zone 3 | 17.24" | `#1E2435` | `#27AE60` (Emerald) | Equiaxed recrystallized grains (rounded shapes) |

**Inside each column (top to bottom):**

*Zone 1 -- Porous Columnar:*
- Zone badge: Rounded rect 1.4" x 0.4", fill `#E05C5C`
- Text: `ZONE 1` Barlow Condensed ExtraBold 14 pt `#1A1F2E`
- Title: `Porous Columnar` Barlow SemiBold 18 pt `#E05C5C`
- Grain illustration area: ~3.5" tall. 5-6 narrow vertical rectangles (W: 0.4", H: 3.0") in `#3A4055` with visible gaps (0.15") filled with background color, representing voided grain boundaries.
- Parameters: JetBrains Mono 12 pt `#F0EDE8`
```
T/Tm < 0.3
Low ion energy
Low substrate temp
```
- Properties: Inter Regular 12 pt `#F0EDE8` at 70%
```
Porous, rough surface
Voided grain boundaries
Low hardness, high friction
Columnar voids trap moisture
```
- Verdict: Inter Medium 12 pt `#E05C5C`
- `AVOID: Poor coating quality`

*Zone T -- Dense Fibrous:*
- Badge fill: `#E8A020`. Title color: `#E8A020`.
- Grain illustration: 6-7 tightly packed columns (no gaps), slight width variation, fill `#3A4055` with `#E8A020` borders 1 pt.
- Parameters:
```
T/Tm 0.3-0.5
Moderate ion energy
Bias -50 to -150 V
```
- Properties:
```
Dense fibrous structure
Competitive grain growth
Good hardness, smooth surface
Most PVD tool coatings here
```
- Verdict: Inter Medium 12 pt `#E8A020`
- `TARGET: Ideal for most industrial PVD`

*Zone 2 -- Columnar Dense:*
- Badge fill: `#2EC4B6`. Title color: `#2EC4B6`.
- Grain illustration: Wider columns, fully packed, fill `#3A4055` with `#2EC4B6` borders.
- Parameters:
```
T/Tm 0.5-0.7
Higher substrate temp
Good crystallinity
```
- Properties:
```
Fully dense grain boundaries
Larger columnar grains
Higher adhesion, lower stress
Decorative and optical coatings
```
- Verdict: Inter Medium 12 pt `#2EC4B6`
- `GOOD: Dense, well-adhered films`

*Zone 3 -- Recrystallized:*
- Badge fill: `#27AE60`. Title color: `#27AE60`.
- Grain illustration: Rounded/equiaxed shapes (rounded rectangles, W: 0.8", H: 0.6") packed together, representing recrystallized grains.
- Parameters:
```
T/Tm > 0.7
High substrate temp
Recrystallized grains
```
- Properties:
```
Equiaxed grain structure
Smooth, dense, isotropic
Highest ductility
Rarely achieved in PVD (temp too high for most substrates)
```
- Verdict: Inter Medium 12 pt `#27AE60`
- `RARE: Requires very high T -- limited substrates`

**Below the four columns -- Key insight callout (Y: 13.2" to 13.8"):**
- Full-width rounded rect, W: 23.0", H: 0.6", fill `#252B3D`, border-left 4 pt `#E8A020`
- Text: `T/Tm = substrate temperature / coating melting point (in Kelvin). Increase T/Tm by raising substrate temp or increasing ion bombardment energy (bias voltage). Zone T is your target for hard coatings.` Inter Medium 14 pt `#E8A020`

**X-axis label below diagram:**
- `LOW T/Tm -----------------------> HIGH T/Tm` JetBrains Mono 14 pt `#C8D0D8`, centered

**Y-axis label (left edge, rotated):**
- `ION ENERGY` JetBrains Mono 14 pt `#C8D0D8`, rotated 90 degrees CCW

---

### ZONE 4 -- Deposition Comparison Table

**Section label:** `SPUTTERING VS. ARC -- DEPOSITION PARAMETERS` -- Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK C -- Comparison Table (Y: 16.3" to 21.3")**

| Parameter | Magnetron Sputtering | Cathodic Arc |
|---|---|---|
| Power | DC 1-20 kW / cathode | 20-40 V, 50-200 A / cathode |
| Ionization of flux | ~5% | 50-100% |
| Substrate bias (dep) | -50 to -300 V | -20 to -200 V |
| Working pressure | 1-10 mTorr (0.1-1.0 Pa) | 5-50 mTorr (0.7-6.7 Pa) |
| Deposition rate | 0.5-5 um/hr | 2-10 um/hr |
| Film density | Good (Zone T typical) | Excellent (high ion energy) |
| Surface finish | Very smooth | Macroparticles (droplets) present |
| Adhesion energy | Lower (less ionization) | Higher (metal ion bombardment) |
| Insulating targets? | Yes (RF sputtering 13.56 MHz) | No (DC only) |
| Best application | Decorative, optical, precision | Cutting tools, wear parts, industrial |

Header: Barlow SemiBold 13 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

Bottom callout:
- `Arc = faster + denser but with droplets. Sputtering = smoother + more controllable but slower. Choose based on your application.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- In-Situ Quality Indicators

**Section label:** `WHAT TO WATCH DURING DEPOSITION` -- Y: 21.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Four Diagnostic Cards (Y: 22.3" to 26.8")**

Four cards in a single row. Each: Rounded rect W: 5.5", H: 4.3", fill `#1E2435`, radius 6.

| Card | X | Accent Color | Title | Indicators |
|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | PLASMA COLOR | TiN: golden-pink = correct / Blue = N2 excess / Bright white = N2 deficient (metallic Ti) |
| 2 | 6.33" | `#2EC4B6` | PRESSURE STABILITY | Stable = good / Drifting up = gas leak or outgassing / Drifting down = MFC malfunction or gas supply low |
| 3 | 12.16" | `#27AE60` | BIAS CURRENT | Stable = uniform ion flux / Sudden spike = arcing on substrate / Gradual drop = target erosion |
| 4 | 18.0" | `#E05C5C` | ARC STABILITY (Arc Systems) | Stable arc spots = normal / Flickering/extinguishing = target contamination or magnetic field issue / Loud snapping = high macroparticle generation |

Interior per card:
- Title: Barlow SemiBold 16 pt, card accent color
- "Normal" indicator: Inter Medium 13 pt `#27AE60`
- "Warning" indicators: Inter Medium 12 pt `#E8A020`
- "Problem" indicator: Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- Common Deposition Failures

**Section label:** `DEPOSITION FAILURES -- WHAT GOES WRONG` -- Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Failure Cards (Y: 27.8" to 32.3")**

Each card: Rounded rect W: 5.5", H: 4.3", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WRONG COLOR / COMPOSITION | Reactive gas ratio off -- target poisoning or N2 deficiency | Verify MFC calibration; use OES feedback control; check gas supply pressure |
| 2 | 6.33" | LOW ADHESION | Inadequate ion etch; contamination survived cleaning | Increase etch time/bias; review cleaning protocol; verify base vacuum before etch |
| 3 | 12.16" | HIGH STRESS / FLAKING | Bias too high; coating too thick in single layer | Reduce bias to -100 V range; use multilayer architecture; limit single layer < 5 um |
| 4 | 18.0" | MACROPARTICLES (ARC) | Arc current too high; cathode surface contaminated | Reduce arc current; polish cathode surface; consider filtered arc |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 12 pt `#F0EDE8`
- Fix: Inter Medium 12 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Deposition Stage -- PVD`. Version `v1.0 -- 2026`.

**Disclaimer:** `This poster is an educational reference tool. Deposition parameters shown are typical industry ranges for PVD hard coatings. Specific recipes vary by equipment manufacturer, target material, and coating specification. Consult your equipment supplier for application-specific settings.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deposition Stage PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The Thornton Structure Zone Model is the single most important concept in PVD film growth. Every PVD operator should understand that substrate temperature and ion bombardment energy determine whether they get a porous, useless film (Zone 1) or a dense, hard coating (Zone T). The four-column visual makes this immediately intuitive. The in-situ quality indicators are the "dashboard" section -- plasma color and pressure stability are the two most accessible real-time diagnostics on any PVD system.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #406 -- Construction Workup v1.0*
*2026-04-26*
