---
Project: Plating Posters Inc
Poster Number: 195
Title: "Aluminum Conversion Coating -- Rinse (Pre-Coat)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.5)"
Technical Source: Rinse stage between acid etch/deoxidize and Ti/Zr conversion coating bath. Covers DI/RO water requirements, mineral competition with Zr deposition, and the critical transit time window.
Process Scope: Aluminum conversion coating -- Stage 4 rinse (pre-coat)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - Rinse
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #195 -- Construction Workup
## Aluminum Conversion Coating -- Rinse (Pre-Coat)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the pre-coat rinse poster for CC-06. It occupies the most critical position in the sequence -- the last wet stage before the ultra-thin Ti/Zr coating is deposited. Everything that enters this rinse water can end up competing with the Zr deposition reaction. Dissolved minerals from tap water, acid residues from the deoxidizer, dissolved metals from the etch -- all of it must be removed.

The central message: DI or RO water is not optional for this rinse stage. Dissolved calcium, magnesium, and iron from tap water directly compete with Zr for deposition sites on the aluminum surface. This is the rinse where water quality makes or breaks the coating.

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

1. **Stage detail panel (Block B -- HERO):** Parameters, purpose, and the mineral competition mechanism.
2. **The "competition" diagram (Block C):** Visual showing dissolved minerals vs. Zr competing for surface sites.
3. **Transit time callout (Block D):** The < 5 minute window before aluminum re-oxidizes.
4. **Water quality requirements table (Block E).**
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
  Block B: Stage detail panel (parameters, purpose, critical role)
  Block C: Mineral competition diagram (why DI/RO matters)

ZONE 3 -- TRANSIT TIME WINDOW (15.5"--22.0" / ~6.5" tall)
  Block D: The re-oxidation clock -- what happens at 1 min, 5 min, 15 min

ZONE 4 -- WATER QUALITY REQUIREMENTS (22.0"--28.5" / ~6.5" tall)
  Block E: Detailed water quality specs for this rinse stage

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
- Text: `Stage 4 -- Rinse (Pre-Coat)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `The last rinse before coating. Every dissolved mineral here is a competitor. DI water is the standard -- not the upgrade.`
- Y: 2.2"

---

### ZONE 2 -- Rinse Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE -- PRE-COAT (THE CRITICAL RINSE)`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 8.5". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge:
- Rounded rect 2.0" x 0.4", fill `#2EC4B6`
- Text: `STAGE 4 -- PRE-COAT RINSE` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`
- Y: 4.2"

Parameters (JetBrains Mono 14 pt `#F0EDE8`, left column):
```
Water:           DI or RO water STRONGLY preferred
Temperature:     Ambient
Conductivity:    < 50 uS/cm (DI); < 200 uS/cm (RO acceptable)
Method:          Overflow immersion or gentle spray
Time:            30--60 sec
```

Purpose callout (right side):
- Rounded rect W: 10.0", H: 2.5", fill `#252B3D`, top accent `#27AE60`
- Title: `THREE JOBS, ONE RINSE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body (Inter Regular 14 pt `#F0EDE8`):

```
1. Remove all acid and dissolved metals from deoxidize
2. Provide a mineral-free surface for Zr deposition
3. Minimize the transit window before re-oxidation
```

---

**BLOCK C -- Mineral Competition Diagram**

Y: 9.0" to 15.0". Two panels side-by-side.

**Left -- The Problem: Mineral Competition**
- Rounded rect, X: 0.5", Y: 9.0", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `WHY TAP WATER FAILS` -- Barlow SemiBold, 20 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
The Ti/Zr conversion reaction deposits a 20--100 nm
film by a pH-driven hydrolysis at the metal surface.

Dissolved minerals in tap water compete for the same
deposition sites:

  Ca2+ and Mg2+ --> CaCO3 / MgO deposits
  Fe2+ and Fe3+ --> iron oxide inclusions
  SO4 2- and Cl- --> interfere with film uniformity

These minerals are INVISIBLE on the part but show up
as poor paint adhesion, inconsistent XRF readings,
and premature corrosion.
```

**Right -- The Solution: DI/RO Water**
- Rounded rect, X: 12.0", Y: 9.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#27AE60`
- Title: `DI / RO WATER -- THE STANDARD` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
DI (Deionized) Water:
  Conductivity: < 10 uS/cm (typically < 5)
  Ion content: negligible
  Best for: all applications; aerospace mandatory

RO (Reverse Osmosis) Water:
  Conductivity: 10--50 uS/cm
  Ion content: very low
  Best for: cost-effective alternative to full DI

Either is acceptable for most Ti/Zr lines.
Aerospace specifications typically require full DI.
Automotive lines commonly use RO.
```

Cost perspective callout at bottom:
- Rounded rect, W: 23.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `A DI system costs pennies per gallon. A coating failure costs thousands in rework. The math is simple.` -- Inter Medium 13 pt `#E8A020`

---

### ZONE 3 -- Transit Time Window

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE RE-OXIDATION CLOCK`

**BLOCK D -- Transit Time Impact Panel**

Y: 16.3" to 21.8". Four time-step cards in a row.

Each card: Rounded rect, W: 5.5", H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | X | Time | Status | Accent | Description |
|---|---|---|---|---|---|
| 1 | 0.5" | < 1 MINUTE | IDEAL | `#27AE60` | Fresh, active aluminum surface. Oxide layer just beginning to reform. Best coating adhesion. |
| 2 | 6.33" | 1--5 MINUTES | ACCEPTABLE | `#E8A020` | Thin oxide reforming. Zr deposition still effective on most alloys. Aerospace target: < 5 min. |
| 3 | 12.16" | 5--15 MINUTES | MARGINAL | `#E05C5C` | Significant oxide regrowth. Coating may be thinner, less uniform. Adhesion compromised. |
| 4 | 18.0" | > 15 MINUTES | RE-DEOX NEEDED | `#E05C5C` | Oxide layer fully reformed. Parts must return to deoxidize stage. Coating will not adhere properly. |

Interior per card:
- Time: Barlow Condensed ExtraBold, 22 pt, in accent color
- Status tag: small rounded rect fill accent color, text Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Description: Inter Regular 13 pt `#F0EDE8`

Below cards -- key principle:
- Rounded rect, W: 23.0", H: 0.8", fill `#252B3D`
- Text: `Aluminum re-oxidizes in SECONDS in air or water. The deoxidize-to-coat transit is the tightest window in the entire line. Design your rack flow to minimize this gap.` -- Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Water Quality Requirements

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WATER QUALITY SPECIFICATIONS -- PRE-COAT RINSE`

**BLOCK E -- Water Quality Specs Table**

Y: 22.9" to 28.3".

Rounded rect, X: 0.5", Y: 22.9", W: 23.0", H: 5.0", fill `#1E2435`, radius 8.

Table inside:

| Parameter | Target | Maximum | Test Method |
|---|---|---|---|
| Conductivity | < 10 uS/cm (DI) | < 50 uS/cm | Inline conductivity meter |
| Total Dissolved Solids | < 5 ppm | < 25 ppm | TDS meter |
| Chloride (Cl-) | < 1 ppm | < 5 ppm | Ion chromatography or test strip |
| pH | 5.5--7.5 | -- | pH meter |
| Iron (Fe) | < 0.1 ppm | < 0.5 ppm | Colorimetric test kit |
| Silica (SiO2) | < 1 ppm | < 5 ppm | Colorimetric test kit |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 14 pt.
Alternating rows: `#1E2435` / `#252B3D`.

Below table -- monitoring callout:
- Text: `Monitor conductivity CONTINUOUSLY with an inline meter. A conductivity alarm at 50 uS/cm prevents the most common rinse-related coating failures.` -- Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | INCONSISTENT XRF | Mineral deposits competing with Zr coating | Check DI quality; replace resin beds; verify conductivity |
| 2 | 6.33" | WATER SPOTS | Hard water minerals; parts drying before coating | Switch to DI/RO; improve transfer speed |
| 3 | 12.16" | THIN COATING | Re-oxidation from slow transfer (> 5 min gap) | Speed up line; minimize deox-to-coat transit |
| 4 | 18.0" | ACID CARRY-OVER | Deox acid dragged into pre-coat rinse; low overflow | Increase overflow rate; improve drain time over deox |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Rinse (Pre-Coat)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for pre-coat rinse stages in Ti/Zr conversion coating lines. Water quality requirements vary by process supplier and specification. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Rinse Pre-Coat -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster transforms a "boring" rinse stage into a compelling visual by introducing two strong conceptual hooks: the mineral competition mechanism and the re-oxidation clock. The four time-step cards in Zone 3 give operators an immediate, visceral understanding of why speed matters between deox and coating. The water quality specs table in Zone 4 gives them actionable numbers to put on their control charts.

The cost callout ("pennies per gallon vs. thousands in rework") speaks directly to shop managers who see DI systems as an expense rather than an investment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #195 -- Construction Workup v1.0*
*2026-04-26*
