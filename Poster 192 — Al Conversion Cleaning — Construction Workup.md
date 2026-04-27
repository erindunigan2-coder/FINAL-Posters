---
Project: Plating Posters Inc
Poster Number: 192
Title: "Aluminum Conversion Coating -- Cleaning"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.2)"
Technical Source: Alkaline cleaning for Ti/Zr and non-chromate aluminum conversion coating lines. Covers non-etch and mildly alkaline cleaners suited to multi-metal automotive and aerospace pretreatment. Values are typical ranges for spray and immersion.
Process Scope: Aluminum conversion coating -- Stage 1 cleaning (alkaline degrease)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - Cleaning
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #192 -- Construction Workup
## Aluminum Conversion Coating -- Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cleaning stage poster for CC-06: Chromium-Free Aluminum Conversion Coatings. Cleaning is the foundation -- a Ti/Zr coating deposited at 20--100 nm thickness has zero tolerance for surface contamination. Unlike hex chromate, which is a powerful oxidizer that can "burn through" minor residual soils, Zr coatings deposit by a gentle pH-driven hydrolysis reaction that simply will not happen on a contaminated surface.

The poster must emphasize: (1) non-etch alkaline chemistry is the standard for aluminum, (2) multi-metal cleaners are mandatory for automotive mixed-substrate lines, and (3) the cleaner must work on steel, galvanized, AND aluminum without etching any of them.

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

1. **Stage detail diagram (Block B -- HERO):** A single large callout panel showing the cleaning stage in depth -- parameters for spray and immersion, critical control points, and a substrate compatibility chart.

2. **Spray vs. Immersion comparison (Block C):** Two side-by-side panels comparing spray and immersion cleaning parameters.

3. **Multi-metal compatibility table (Block D):** Table showing cleaner performance across aluminum, steel, galvanized, and mixed-substrate lines.

4. **Critical Points / Failure Modes strip (Block E):** Common cleaning failures and their impact on the downstream conversion coating.

5. **Troubleshooting quick-hit strip (Block F):** 4 common cleaning problems with fixes.

6. **Standard construction: 4 pt accent borders, light remap, JetBrains Mono, 24x36".**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CLEANING STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (large callout with parameters, mechanism, and controls)
  Block C: Spray vs. Immersion comparison (side-by-side)

ZONE 3 -- MULTI-METAL COMPATIBILITY (15.5"--22.0" / ~6.5" tall)
  Block D: Substrate compatibility table + multi-metal callout

ZONE 4 -- CRITICAL CONTROL POINTS (22.0"--28.5" / ~6.5" tall)
  Block E: Failure mode / impact panel (cleaning deficiency -> coating defect chain)

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
- Text: `Stage 1 -- Alkaline Cleaning`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `The thinnest coatings demand the cleanest surfaces. No oxidizer to rescue you -- the Zr reaction simply will not start on a dirty part.`
- Y: 2.2"

---

### ZONE 2 -- Cleaning Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ALKALINE CLEANING -- THE FOUNDATION`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 9.5". Full width within margins.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 5.5", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Inside panel -- left half (X: 1.0" to 12.0"):

Stage badge:
- Rounded rect 1.4" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1 -- CLEAN` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Y: 4.2"

Chemistry overview:
- Barlow SemiBold, 20 pt, `#F0EDE8`
- Text: `Non-Etch Alkaline Cleaner`
- Y: 4.9"

Characteristics list (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
Type: Mildly alkaline, surfactant-based
pH: 9--11
Function: Dissolve oils, soils, shop contaminants
NOT a caustic etch -- must not attack aluminum
Silicate-inhibited cleaners preferred
```

Inside panel -- right half (X: 12.5" to 23.0"):

Key principle callout:
- Rounded rect, W: 10.0", H: 1.5", fill `#252B3D`, radius 6, top accent 4 pt `#27AE60`
- Title: `WHY NON-ETCH?` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body: Inter Regular, 13 pt, `#F0EDE8` at 80%
- Text: `Strongly caustic cleaners (NaOH > 5%) etch aluminum aggressively, producing a heavy smut layer that is harder to remove in the deox stage. For Ti/Zr lines, clean WITHOUT etching -- the deoxidizer handles surface activation.`

Multi-substrate callout:
- Rounded rect, W: 10.0", H: 1.5", fill `#252B3D`, radius 6, top accent 4 pt `#E8A020`
- Title: `MULTI-METAL LINES` -- Barlow SemiBold, 16 pt, `#E8A020`
- Body: `Automotive body-in-white: one cleaner must handle steel + galvanized + aluminum panels in the same line. Low-energy, non-etch formulations are mandatory.`

---

**BLOCK C -- Spray vs. Immersion Comparison**

Y: 10.0" to 15.0". Two side-by-side panels.

**Left -- Spray Cleaning:**
- Rounded rect, X: 0.5", Y: 10.0", W: 11.0", H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SPRAY CLEANING` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Concentration:  2--4 oz/gal (15--30 g/L)
Temperature:    100--140 F (38--60 C)
Time:           1--3 min
Pressure:       10--25 psi (typical)
```

Advantages (Inter Regular 13 pt `#F0EDE8`):
```
- Faster processing, lower chemical cost
- Mechanical action aids soil removal
- Lower energy (lower temp than immersion)
- Standard for automotive multi-stage lines
```

**Right -- Immersion Cleaning:**
- Rounded rect, X: 12.0", Y: 10.0", W: 11.5", H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `IMMERSION CLEANING` -- Barlow SemiBold, 20 pt, `#E8A020`

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Concentration:  4--8 oz/gal (30--60 g/L)
Temperature:    120--160 F (49--71 C)
Time:           3--10 min
Agitation:      Air or mechanical
```

Advantages (Inter Regular 13 pt `#F0EDE8`):
```
- Better soil penetration on complex parts
- Uniform contact in recesses and blind holes
- Higher concentration compensates for no spray action
- Standard for aerospace processing
```

---

### ZONE 3 -- Multi-Metal Compatibility

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `MULTI-METAL SUBSTRATE COMPATIBILITY`

**BLOCK D -- Compatibility Table**

Y: 16.3" to 21.8". Column widths (23.0" total): Substrate (4.0") | Cleaner Type (5.0") | Caution (6.5") | Notes (7.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Substrate | Cleaner Type | Caution | Notes |
|---|---|---|---|
| Wrought Aluminum (6xxx) | Non-etch alkaline, pH 9--11 | Caustic etch dissolves Al; silicate inhibitors OK | Most common automotive alloy family |
| Cast Aluminum (356, A356) | Same; may need stronger surfactancy | High Si content produces tenacious smut | Deox step is critical for cast alloys |
| High-Cu Aluminum (2xxx, 7xxx) | Same cleaner; deox removes Cu smut | Do NOT rely on cleaner alone for smut removal | Aerospace alloys -- cleaner + deox is mandatory |
| Cold-Rolled Steel | Multi-metal alkaline, pH 9--11 | Must not passivate the steel surface | Steel + Al in same automotive line |
| Galvanized Steel | Same multi-metal cleaner | Zinc sensitive to strongly alkaline pH | Avoid pH > 12 on galvanized |

Data: Inter Regular 13 pt. Key terms in Inter Medium.

---

### ZONE 4 -- Critical Control Points

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `CLEANING FAILURES -- DOWNSTREAM CONSEQUENCES`

**BLOCK E -- Failure Chain Panel**

Y: 22.9" to 28.3". Four vertical failure chain cards.

Each card: Rounded rect, W: 5.5", H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt `#E05C5C`.

| Card | X | Cleaning Failure | Downstream Effect | Prevention |
|---|---|---|---|---|
| 1 | 0.5" | RESIDUAL OIL | Zr does not deposit -- bare spots, skip areas; paint peels | Water-break test after clean; no beading = clean |
| 2 | 6.33" | SILICATE RESIDUE | Silicate film blocks Zr deposition; invisible barrier | Use silicate-free or silicate-controlled cleaner |
| 3 | 12.16" | EXCESSIVE ETCH | Heavy smut on aluminum; requires aggressive deox to remove | Use non-etch cleaner; avoid NaOH > 5% |
| 4 | 18.0" | ALKALINE DRAG-OVER | Raises deox pH; reduces acid effectiveness; wastes chemistry | Adequate rinse between clean and deox (Stage 2) |

Interior per card:
- Failure: Barlow SemiBold, 16 pt, `#E05C5C`
- Effect: Inter Regular, 13 pt, `#F0EDE8`
- Prevention: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WATER BREAK (BEADING) | Oil not fully removed; cleaner too dilute or too cold | Increase conc/temp/time; check surfactant level |
| 2 | 6.33" | WHITE SMUT ON AL | Caustic etch of aluminum; cleaner pH too high | Switch to non-etch cleaner; verify pH < 11 |
| 3 | 12.16" | FOAM OVERFLOW | Excess surfactant; drag-in of cutting oils | Reduce cleaner concentration; improve pre-rinse |
| 4 | 18.0" | FLASH RUST ON STEEL | Insufficient inhibitor in multi-metal cleaner; slow transfer | Add rust inhibitor to cleaner; speed up line |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for alkaline cleaning prior to Ti/Zr and related non-chromate conversion coating processes on aluminum. Specific cleaner formulations vary by supplier. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster answers the question every operator asks: "Why does my cleaning matter so much for this thin coating?" The answer is that Zr coatings are deposited at 20--100 nm -- thinner than a wavelength of visible light -- by a gentle hydrolysis reaction that has zero tolerance for surface contamination. Hex chromate could oxidize through minor residual soils. Zr cannot. Cleaning is more important for this process than for any other conversion coating in the series.

The multi-metal compatibility table is critical for automotive shops running mixed-substrate lines. The failure chain panel (Zone 4) visually connects cleaning deficiencies to downstream coating defects -- this is the "why it matters" section that turns a mundane topic into an engaging visual.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #192 -- Construction Workup v1.0*
*2026-04-26*
