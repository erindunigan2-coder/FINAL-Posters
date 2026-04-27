---
Project: Plating Posters Inc
Poster Number: 449
Title: "Ion Implantation -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Section 6.1)"
Technical Source: Industry-standard ion implantation process covering both semiconductor doping and industrial surface modification. Parameters from ASM Handbook Vol. 5, semiconductor process literature, and ASTM standards.
Process Scope: Ion Implantation -- complete process flow (10 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IonImplantation
  - ProcessFlow
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #449 -- Construction Workup
## Ion Implantation -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Ion Implantation. Ion implantation is fundamentally different from every other process in the poster series -- it does NOT add a coating. It modifies the existing surface by shooting energetic ions INTO the substrate lattice. No thickness is added. No adhesion concerns. The surface composition changes at the atomic level. The poster must hammer this distinction home. The hero is a 10-stage U-flow diagram. A comparison table shows semiconductor vs. industrial applications side by side, and a property improvement summary shows what implantation actually does to a surface.

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

1. **Process flow diagram (Block B -- HERO):** Ten rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--10). Each box is color-coded by stage type.
2. **Semiconductor vs. Industrial comparison (Block E):** Two-column table showing how the same technology serves both worlds.
3. **Property improvement summary (Block D):** Before/after table for N+ implantation into steel.
4. **Key distinction callout (Block F):** "Not a coating" message.

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Create the document
- Width: **24 inches**. Height: **36 inches**.

### Step 2 -- Set the background color
- **`#1A1F2E`** (Gunmetal Dark)

### Step 3 -- Upload fonts
- **Barlow Condensed ExtraBold** -- all headlines and section labels
- **Barlow SemiBold** -- all subheadings, callout titles
- **Inter Regular** and **Inter Medium** -- all body text, table data, and descriptions
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, concentration ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Equipment/system stages, energy parameters |
| Teal | `#2EC4B6` | Cleaning & prep stages, structural positives |
| Emerald | `#27AE60` | Implantation stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, safety callouts |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 16.0" -- Zone 2/Zone 3 boundary
- 22.0" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Ten-stage U-flow diagram (2 rows of 5)
  Block C: Stage legend strip (color key)

ZONE 3 -- PROPERTY IMPROVEMENT SUMMARY (16.0"--22.0" / ~6.0" tall)
  Block D: Before/after implantation table

ZONE 4 -- SEMICONDUCTOR vs. INDUSTRIAL (22.0"--28.5" / ~6.5" tall)
  Block E: Two-world comparison

ZONE 5 -- KEY DISTINCTION (28.5"--32.5" / ~4.0" tall)
  Block F: "Not a coating" callout + common issues strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".
**Background:** Same as page (`#1A1F2E`).

---

**BLOCK A -- Headline**

- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. Letter spacing: -4.
- Position: X: 0.5". Y: 0.5". Width: 23.0".
- Text:

> ION IMPLANTATION

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5". Width: 23.0".
- Font: Barlow SemiBold, 36 pt, `#27AE60` (Emerald).
- Text:

> Complete Process Flow -- 10 Stages from Inspection to Characterization

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2". Width: 23.0".
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%.
- Text:

> Not a coating. Not a surface treatment. Ion implantation shoots energetic ions INTO the substrate lattice, modifying surface composition at the atomic level without adding measurable thickness.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 16.0" (~13.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1".
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center.
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Ten-Stage U-Flow Diagram**

Y: 3.8" to 14.5" (~10.7" tall). Two rows of five boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 4.2". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Substrate Inspection | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Cleaning | Box 2 | 5.1" | `#2EC4B6` (Teal) | Cleaning |
| 3. Masking | Box 3 | 9.7" | `#2EC4B6` (Teal) | Prep |
| 4. Loading | Box 4 | 14.3" | `#2EC4B6` (Teal) | Loading |
| 5. Pumpdown | Box 5 | 18.9" | `#E8A020` (Amber) | Equipment |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 5 to Stage 6):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.
- From: X: 21.0", Y: 8.3" (bottom center Box 5)
- To: X: 21.0", Y: 9.5" (top center Box 6)

**Bottom Row (Y: 9.5" to 14.0") -- Stages 6-10, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Ion Source Startup | Box 6 | 18.9" | `#E8A020` (Amber) | Equipment |
| 7. Beam Tuning | Box 7 | 14.3" | `#E8A020` (Amber) | Parameters |
| 8. Implantation | Box 8 | 9.7" | `#27AE60` (Emerald) | Process |
| 9. Anneal (Semiconductor) | Box 9 | 5.1" | `#E8A020` (Amber) | Post-Process |
| 10. Characterize | Box 10 | 0.5" | `#E8A020` (Amber) | Quality |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box (top to bottom):**

*Box 1 -- Substrate Inspection:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Substrate Inspection`
- Parameters: `Verify material ID and grade` / `Check dimensions and tolerances` / `Document surface condition`
- Purpose: `Confirm substrate before committing to implantation`
- Check: `Material verification is critical -- wrong alloy = wrong stopping range`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters: `Semiconductor: RCA clean` / `Industrial: ultrasonic alkaline + rinse` / `Surface must be free of all contamination`
- Purpose: `Remove contaminants that scatter or absorb ions`
- Check: `Surface contamination wastes implant dose on non-substrate atoms`

*Box 3 -- Masking:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Masking`
- Parameters: `Semiconductor: photoresist 0.5--5 um` / `Industrial: metal masks (steel, Mo)` / `Mask must stop ions at implant energy`
- Purpose: `Define implant area; protect non-implant regions`
- Check: `Mask thickness must exceed ion projected range (Rp)`

*Box 4 -- Loading:*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Loading`
- Parameters: `Mount on cooled/heated platen` / `Ensure thermal contact` / `Semiconductor: wafer handler (automated)`
- Purpose: `Position substrate for uniform beam exposure`
- Check: `Poor thermal contact = localized overheating = resist damage`

*Box 5 -- Pumpdown:*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Pumpdown`
- Parameters: `Base pressure: 10^-5 to 10^-6 Torr` / `Cryopump or turbopump` / `Residual gas analyzer check (optional)`
- Purpose: `Establish vacuum for beam transport`
- Check: `Beam scatters in residual gas -- pressure must be low` (Coral `#E05C5C`)

*Box 6 -- Ion Source Startup:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Ion Source Startup`
- Parameters: `Ignite source plasma` / `Tune mass analyzer to select species` / `Verify beam purity (no contaminants)`
- Purpose: `Generate and isolate the correct ion species`
- Check: `Mass separation is essential -- wrong ion = wrong implant`

*Box 7 -- Beam Tuning:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Beam Tuning`
- Parameters: `Set energy: 10 keV -- 10 MeV` / `Set beam current: 0.1--30 mA` / `Verify dose uniformity via Faraday cup`
- Purpose: `Calibrate beam for correct energy, current, and scan pattern`
- Check: `Faraday cup = dose accuracy. No Faraday = no dose control.`

*Box 8 -- Implantation:*
- Badge: `STAGE 8`, fill `#27AE60`
- Name: `Implantation`
- Parameters: `Beam scans across substrate` / `Dose integrator counts total ions` / `Typical dose: 10^14 to 10^18 ions/cm2`
- Purpose: `Embed ions in substrate near-surface region`
- Check: `Substrate temp monitored -- overheating damages masks and substrates`

*Box 9 -- Anneal:*
- Badge: `STAGE 9`, fill `#E8A020`
- Name: `Anneal` / Subtitle: `(Semiconductor)`
- Parameters: `RTA: 900--1100 C, 5--60 sec` / `Repairs lattice damage` / `Activates dopant electrically`
- Purpose: `Restore crystal structure; activate implanted species`
- Check: `Industrial implants often skip anneal -- damage may be beneficial`

*Box 10 -- Characterize:*
- Badge: `STAGE 10`, fill `#E8A020`
- Name: `Characterize`
- Parameters: `SIMS: depth profile` / `4-point probe: sheet resistance` / `Nanoindentation: hardness (industrial)`
- Purpose: `Verify dose, depth, and property improvement`
- Check: `SIMS is gold standard for implant verification`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep & Cleaning` |
| `#E8A020` (Amber) | `Equipment & Parameters` |
| `#27AE60` (Emerald) | `Implantation` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Property Improvement Summary

**Dimensions:** Y: 16.0" to 22.0" (~6.0" tall).

---

**Section label:**
- Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHAT ION IMPLANTATION DOES TO A SURFACE

---

**BLOCK D -- Before/After Table**

Y: 16.8" to 21.8".

Rounded rect container, X: 0.5", Y: 16.8", W: 23.0", H: 4.8", fill `#1E2435`.

Header row: fill `#3A4055`, H: 0.5".
Columns: Property (5.0") | Before Implantation (6.0") | After N+ Implantation (Steel) (6.0") | Improvement (6.0")

| Property | Before | After N+ (Steel) | Improvement |
|---|---|---|---|
| Surface hardness | 800--1,000 HV (tool steel) | 1,200--1,800 HV | 50--100% increase |
| Wear rate | Baseline | 2x--10x reduction | Dramatic |
| Friction coefficient (dry) | 0.5--0.7 (steel-on-steel) | 0.2--0.4 | 40--70% reduction |
| Corrosion resistance | Baseline | Improved (N stabilizes passive film) | Measurable |
| Fatigue life | Baseline | 2x--5x improvement | Compressive residual stress |
| Modified zone depth | -- | 50--500 nm | Near-surface only |
| Dimensional change | -- | ZERO (< 1 nm) | No measurable addition |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Improvement: Inter Medium, 12 pt, `#27AE60`.

---

### ZONE 4 -- Semiconductor vs. Industrial

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> TWO WORLDS -- SAME PHYSICS

---

**BLOCK E -- Comparison Table**

Y: 22.9" to 28.3".

Two-column layout:

**Left -- Semiconductor (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SEMICONDUCTOR DOPING` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Aspect | Detail |
|---|---|
| Purpose | Create p-type or n-type regions in Si |
| Ion species | B+ (p-type), P+ / As+ (n-type), BF2+ |
| Energy | 0.2--200 keV |
| Dose | 10^11 to 10^16 ions/cm2 |
| Beam current | 0.1--30 mA |
| Anneal | Required (RTA 900--1100 C) |
| Characterization | 4-point probe, SIMS, SRP |
| Volume | Billions of implants/year worldwide |

**Right -- Industrial Surface Modification (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `INDUSTRIAL SURFACE MODIFICATION` -- Barlow SemiBold, 18 pt, `#E8A020`

| Aspect | Detail |
|---|---|
| Purpose | Improve hardness, wear, corrosion, fatigue |
| Ion species | N+, C+, B+, Ti+, Cr+ |
| Energy | 10--500 keV |
| Dose | 10^14 to 10^18 ions/cm2 (much higher) |
| Beam current | 1--100 mA |
| Anneal | Usually not needed |
| Characterization | Nanoindentation, wear test, SIMS |
| Volume | Specialty / high-value parts only |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

---

### ZONE 5 -- Key Distinction

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> REMEMBER -- THIS IS NOT A COATING

---

**BLOCK F -- Distinction Callout + Common Issues**

Y: 29.4" to 32.3".

**Main callout (Y: 29.4" to 30.6"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.0", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `Ion implantation embeds foreign atoms INTO the existing substrate lattice. No material is added on top. No thickness change. No adhesion concern. The surface IS the substrate -- modified at the atomic level.` -- Inter Medium, 14 pt, `#27AE60`

**Four common issues cards (Y: 31.0" to 32.3"):**

| Card | X | W | Issue | Fix |
|---|---|---|---|---|
| 1 | 0.5" | 5.5" | CHANNELING | Tilt wafer 7 deg off crystal axis; use screen oxide |
| 2 | 6.33" | 5.5" | DOSE NON-UNIFORMITY | Calibrate beam scan; verify Faraday cup |
| 3 | 12.16" | 5.5" | SPUTTERING AT HIGH DOSE | Accept surface erosion; reduce energy if critical |
| 4 | 18.0" | 5.5" | CHARGING (INSULATORS) | Use electron flood gun for charge neutralization |

Each card: Rounded rect, H: 1.1", fill `#1E2435`, left accent 0.06" `#E05C5C`.
Issue: Barlow SemiBold, 13 pt, `#E05C5C`. Fix: Inter Regular, 11 pt, `#F0EDE8`.

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for ion implantation. Semiconductor parameters reflect beam-line implanter technology. Industrial parameters reflect nitrogen and carbon implantation into metals. Specific process recipes vary by implanter manufacturer and application. Source: General industry knowledge; ASM Handbook Vol. 5; semiconductor process literature.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Ion Implantation -- Process Flow

**Series name:** Inter Regular, 14 pt, `#F0EDE8` at 70%, Center. Y: 34.2"

> Plating Posters Inc -- Metal Finishing Reference Series

**Logo placeholder:** Rectangle, X: 22.5", Y: 33.3", W: 0.83", H: 0.42", fill `#3A4055`. Text: `[LOGO]` -- Inter Regular, 10 pt, `#F0EDE8` at 50%

**Version:** JetBrains Mono Regular, 11 pt, `#F0EDE8` at 50%. X: 0.5", Y: 35.0"

> v1.0 -- 2026

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, ten flow boxes, arrows, legend strip |
| Zone 3 - Property Table | Section label, before/after improvement table |
| Zone 4 - Comparison | Section label, semiconductor vs. industrial panels |
| Zone 5 - Key Distinction | Callout, four common issues cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Callout/flow box fills |
| `#252B3D` | `#E8E8F0` | Alternate rows, legend strip |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers, arrows |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

Stage badges: Verify text legibility on darkened fills -- may need `#F5F4F0` text.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Ion Implantation Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ion Implantation Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ion Implantation Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Ion Implantation Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ion Implantation Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ion Implantation Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Ion implantation is the most "physics-heavy" process in the entire poster library. The key challenge is making it accessible to a metal finishing audience that thinks in terms of tanks, amps, and plating thickness. The "not a coating" distinction must be prominent and repeated. The semiconductor vs. industrial comparison (Zone 4) bridges two very different audiences. For the plating shop wall, the industrial column is the anchor; for educational and academic customers, the semiconductor column adds completeness. The property improvement table (Zone 3) is the sell -- it shows exactly what implantation does in terms plating people understand (hardness, wear, friction).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #449 -- Construction Workup v1.0*
*2026-04-26*
