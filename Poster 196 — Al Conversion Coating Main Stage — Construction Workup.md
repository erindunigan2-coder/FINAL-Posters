---
Project: Plating Posters Inc
Poster Number: 196
Title: "Aluminum Conversion Coating -- Ti/Zr Conversion Coat (Main Stage)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Section 6.6)"
Technical Source: Zirconium-based and Ti/Zr hybrid conversion coatings on aluminum -- the main deposition stage. Covers H2ZrF6-based chemistry, the pH-driven hydrolysis mechanism, spray and immersion parameters, film characteristics, and multi-metal capability. Also covers cerium-based emerging technology.
Process Scope: Aluminum conversion coating -- Stage 5 Ti/Zr conversion coat (main stage)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - MainStage
  - TiZr
  - Zirconium
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #196 -- Construction Workup
## Aluminum Conversion Coating -- Ti/Zr Conversion Coat (Main Stage)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the main event -- the heart of the CC-06 cluster. The Ti/Zr conversion coating stage is where the ultra-thin ZrO2/TiO2 barrier film deposits on the aluminum (and steel, and galvanized) surface. This is the poster that explains HOW the coating forms, WHAT controls it, and WHY it is nearly invisible.

The coating mechanism is elegant: the acid dissolves substrate metal, local pH rises at the surface, and the zirconium fluoro-complex hydrolyzes and precipitates as an amorphous ZrO2 film. No external current. No heat required. The substrate drives its own coating. This mechanism must be the visual centerpiece.

Design philosophy: the chemical mechanism as a clear 4-step diagram, a comprehensive parameter table, bath chemistry composition, film characteristics, and the multi-metal capability story.

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

1. **Chemical mechanism diagram (Block B -- HERO):** 4-step reaction sequence in a vertical flow.
2. **Bath chemistry composition table (Block C).**
3. **Operating parameter table (Block D):** Spray vs. immersion.
4. **Film characteristics panel (Block E):** Properties of the deposited film.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CHEMICAL MECHANISM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: 4-step mechanism diagram
  Block C: Bath chemistry composition table

ZONE 3 -- OPERATING PARAMETERS (15.5"--22.0" / ~6.5" tall)
  Block D: Spray vs. immersion parameter table

ZONE 4 -- FILM CHARACTERISTICS (22.0"--28.5" / ~6.5" tall)
  Block E: Film properties + multi-metal capability

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
- Font: Barlow SemiBold, 36 pt, `#27AE60` (Emerald)
- Text: `Stage 5 -- Ti/Zr Conversion Coat (Main Stage)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `The substrate drives its own coating. Acid dissolves metal, pH rises, ZrO2 precipitates. 20--100 nm of invisible protection.`
- Y: 2.2"

---

### ZONE 2 -- Chemical Mechanism (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DEPOSITION MECHANISM -- HOW THE COATING FORMS`

---

**BLOCK B -- 4-Step Mechanism Diagram**

Y: 3.8" to 12.0". Four large rounded rectangles in a vertical flow (top to bottom), connected by arrows.

Each step box: W: 22.0", H: 1.8", fill `#1E2435`, radius 8, left accent 0.06".

| Step | Y | Accent | Title | Content |
|---|---|---|---|---|
| 1 | 3.8" | `#E8A020` | `ACID ATTACK ON SUBSTRATE` | `The mildly acidic Zr bath (pH 3.8--5.0) dissolves substrate metal:` / `Al --> Al3+ + 3e- (aluminum)` / `Fe --> Fe2+ + 2e- (steel)` / `Zn --> Zn2+ + 2e- (galvanized)` |
| 2 | 6.0" | `#2EC4B6` | `LOCAL pH RISE` | `As metal dissolves and H+ is consumed at the surface (2H+ + 2e- --> H2), the pH at the metal-solution interface RISES. Bulk pH is 3.8--5.0, but the interface pH climbs to 5.5+.` |
| 3 | 8.2" | `#27AE60` | `ZIRCONIUM HYDROLYSIS` | `The rising pH drives the hydrolysis of the zirconium fluoro-complex:` / `ZrF6 2- + 2H2O --> ZrO2 + 6F- + 4H+ (simplified)` / `Amorphous ZrO2 precipitates directly on the metal surface.` |
| 4 | 10.4" | `#27AE60` | `FILM FORMATION` | `Result: a thin, adherent, amorphous ZrO2 film, 20--100 nm thick. Nearly invisible. Multi-metal compatible. No sludge. No heavy metals in waste.` |

Arrows between boxes: Stroke 3 pt `#3A4055`, arrowhead filled, pointing down.

Step titles: Barlow SemiBold, 18 pt, in accent color.
Chemical formulas: JetBrains Mono 13 pt `#F0EDE8`.
Descriptions: Inter Regular 13 pt `#F0EDE8`.

---

**BLOCK C -- Bath Chemistry Composition Table**

Y: 12.5" to 15.3". Column widths: Component (6.0") | Concentration (5.0") | Function (12.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Component | Concentration | Function |
|---|---|---|
| H2ZrF6 (hexafluorozirconic acid) | 50--200 ppm as Zr | Film-forming species -- source of ZrO2 |
| Free fluoride (F-) | 10--50 ppm | Activator -- dissolves native Al2O3 oxide barrier |
| Cu2+ (optional) | 5--30 ppm | Accelerator -- Cu deposits cathodically, accelerates Zr deposition |
| Organic polymer (some formulations) | 100--500 ppm | Co-deposited organic sealer in hybrid systems |
| pH (controlled by H2ZrF6 + alkali) | 3.8--5.0 | Critical operating range |

Data: JetBrains Mono 12 pt. Component names: Inter Medium 13 pt.

---

### ZONE 3 -- Operating Parameters

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `OPERATING PARAMETERS -- SPRAY vs. IMMERSION`

**BLOCK D -- Parameter Comparison Table**

Y: 16.3" to 21.8". Two side-by-side panels.

**Left -- Spray Application:**
- Rounded rect, X: 0.5", Y: 16.3", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SPRAY` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Temperature:    70--110 F (21--43 C)
Time:           60--120 sec
pH:             3.8--5.0
Free fluoride:  10--50 ppm
Zr content:     50--200 ppm (by XRF or titration)
Pressure:       10--20 psi
```

Notes (Inter Regular 13 pt `#F0EDE8` at 70%):
```
Standard for automotive conveyor lines.
Faster processing, lower chemical consumption.
Ensure full spray coverage -- recesses may be thin.
```

**Right -- Immersion Application:**
- Rounded rect, X: 12.0", Y: 16.3", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `IMMERSION` -- Barlow SemiBold, 20 pt, `#E8A020`

Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
Temperature:    70--120 F (21--49 C)
Time:           60--180 sec
pH:             3.8--5.0
Free fluoride:  10--50 ppm
Zr content:     50--200 ppm (by XRF or titration)
Agitation:      Air or mechanical (mild)
```

Notes (Inter Regular 13 pt `#F0EDE8` at 70%):
```
Standard for rack lines and aerospace.
Better coverage in recesses and blind holes.
Higher chemical consumption per part.
```

---

### ZONE 4 -- Film Characteristics

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `FILM CHARACTERISTICS -- WHAT YOU GET`

**BLOCK E -- Film Properties Panel**

Y: 22.9" to 28.3". Two panels.

**Left -- Film Properties Table:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `FILM PROPERTIES` -- Barlow SemiBold, 20 pt, `#27AE60`

| Property | Value |
|---|---|
| Appearance | Clear to pale iridescent (nearly invisible) |
| Thickness | 20--100 nm (0.02--0.10 um) -- ultra-thin |
| Coating weight | 5--30 mg/m2 as Zr (measured by XRF) |
| Structure | Amorphous ZrO2 / TiO2 |
| Salt spray -- bare | 24--72 hours |
| Salt spray -- with e-coat | 500--1500+ hours |
| Sludge generation | Negligible |
| Wastewater | No Cr, Ni, Mn -- simple treatment |

Data: JetBrains Mono 12 pt. Properties: Inter Medium 13 pt.

**Right -- Multi-Metal Capability:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `MULTI-METAL CAPABILITY` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
One bath. Three substrates. Same reaction.

The pH-driven hydrolysis mechanism works on ANY
metal that dissolves in the mildly acidic bath:

  ALUMINUM  --> Al3+ --> local pH rise --> ZrO2
  STEEL     --> Fe2+ --> local pH rise --> ZrO2
  GALVANIZED --> Zn2+ --> local pH rise --> ZrO2

This is why Zr conversion replaced zinc phosphate
in automotive: one pretreatment bath for the
entire mixed-metal body-in-white.

COMPARED TO ZINC PHOSPHATE:
  - No sludge (vs. tons/year for Zn phos)
  - No heavy metals in waste
  - Lower energy (ambient temp vs. 130+ F)
  - Fewer stages (7 vs. 10+ for Zn phos)
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #191.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NO VISIBLE COATING | Normal for Zr -- the film IS nearly invisible | Verify by XRF (target 5--30 mg/m2 Zr); do NOT judge by eye |
| 2 | 6.33" | LOW XRF READINGS | pH too high (> 5.0); fluoride depleted; contamination | Adjust pH to 3.8--5.0; replenish fluoride; check bath |
| 3 | 12.16" | POOR PAINT ADHESION | Coating too thin; surface contamination; wrong pH | Increase time; improve cleaning; verify pH |
| 4 | 18.0" | INCONSISTENT READINGS | Mixed substrates; variable deox quality; bath aging | Optimize per substrate; standardize deox; monitor bath age |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Ti/Zr Conversion Coat (Main Stage)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for Zr-based and Ti/Zr hybrid conversion coating systems. No dedicated MIL-SPEC exists for Zr conversion coatings as of this printing. Automotive OEM specifications are proprietary. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Al Conversion Main Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the CC-06 cluster -- the mechanism diagram in Zone 2 is the educational heart. The 4-step vertical flow (acid attack -> pH rise -> Zr hydrolysis -> film formation) must be immediately readable at 6 feet. Each step should feel like a logical consequence of the one before it.

The multi-metal capability panel answers the question automotive engineers ask first: "Why did we replace zinc phosphate?" The answer is compelling: one bath, three substrates, no sludge, no heavy metals, lower energy. That is the business case in four lines.

Watson flag confirmed from Poster 191: no MIL-SPEC for Zr conversion coatings as of 2026. SAE ARP 5903 is for evaluation only.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #196 -- Construction Workup v1.0*
*2026-04-26*
