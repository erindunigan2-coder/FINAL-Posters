---
Project: Plating Posters Inc
Poster Number: 271
Title: "Electroless Nickel-Boron -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: Electroless Nickel-Boron)"
Technical Source: Industry-standard electroless nickel-boron (EN-B) plating process. DMAB and borohydride reducing agents. ASTM B841. Values from Watson domain expertise and published literature. Watson flagged deposition rates for Tyler spot-check.
Process Scope: Electroless nickel-boron plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #271 -- Construction Workup
## Electroless Nickel-Boron -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EL-08: Electroless Nickel-Boron (EN-B). It shows the complete 8-stage process sequence at a glance. EN-B is the hardest electroless nickel variant -- 700-850 HV as-plated, 1000-1200+ HV heat-treated -- and a legitimate competitor to hard chrome for wear applications, without the hexavalent chromium. The tradeoff: DMAB reducing agent is 5-10x more expensive than hypophosphite, and corrosion resistance is lower than EN High-P. ASTM B841 governs.

Design philosophy: clean U-flow diagram as the hero, a compact parameter summary table, a "EN-B vs. EN-P vs. Hard Chrome" comparison (the headline comparison for this process), and a troubleshooting quick-hit strip.

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

1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8).

2. **Parameter summary table (Block D):** Compact 8-row table.

3. **"EN-B vs. EN-P vs. Hard Chrome" comparison callout (Block E):** Three-column comparison -- the killer comparison that sells this process.

4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **JetBrains Mono font.** Fallback: Courier Prime.

8. **Print size -- 24x36".**

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
| Amber | `#E8A020` | Activation & post-treatment stages, warning headers |
| Teal | `#2EC4B6` | Cleaning & rinse stages, structural positives |
| Emerald | `#27AE60` | Plating stage, optimal reference |
| Coral | `#E05C5C` | Problems, defects, contamination callouts |
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
- 15.5" -- Zone 2/Zone 3 boundary
- 22.0" -- Zone 3/Zone 4 boundary
- 28.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table (one row per stage)

ZONE 4 -- EN-B VS. EN-P VS. HARD CHROME (22.0"--28.5" / ~6.5" tall)
  Block E: Three-column comparison

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Element type: Text box
- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> ELECTROLESS NICKEL-BORON

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Heat Treatment

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> The hardest electroless nickel. 700--850 HV as-plated. 1000--1200+ HV heat-treated. Hard chrome's autocatalytic rival. ASTM B841.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Two rows of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. EN-B Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Heat Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Passivation / Inspect | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Arrows between bottom-row boxes:**
- Same style, pointing LEFT.

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `140--176 F (60--80 C)` / `NaOH 30--60 g/L` / `3--10 min soak`
- Purpose: `Remove oils, soils, oxides`
- Check: `CHECK: Water-break-free after rinse`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Ambient temp` / `DI counterflow (2-stage min)`
- Purpose: `Remove alkaline cleaner before acid activation`
- Check: `Conductivity <50 uS/cm`

*Box 3 -- Acid Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Activation`
- Parameters: `Steel: HCl 10--20% or H2SO4 10--30%` / `Al: double zincate` / `SS: Wood's Ni strike` / `Ambient, 30--120 sec`
- Purpose: `Create catalytic surface for EN-B initiation`
- Check: `EN-B is less sensitive to marginal activation than EN-P -- but proper activation still required`

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `Ambient` / `DI preferred` / `<20 uS/cm critical`
- Purpose: `Remove acid / activation chemistry`
- Check: `Chloride drag-in causes pitting in EN-B bath`

*Box 5 -- EN-B Plate (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `EN-B Plate` / Subtitle: `Main Tank`
- Parameters: `Ni2+: 20--30 g/L` / `DMAB: 2--5 g/L` / `pH 6--8 (DMAB) or 12--14 (NaBH4)` / `140--203 F (60--95 C)`
- Purpose: `Autocatalytic Ni-B alloy deposition`
- Check: `Rate: 10--20 um/hr (DMAB); 20--30 um/hr (NaBH4)`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Cold DI preferred` / `30--60 sec`
- Purpose: `Stop autocatalytic reaction; remove bath chemistry`
- Check: `Do not air-dry before rinsing; no fingerprints`

*Box 7 -- Heat Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Heat Treatment`
- Parameters: `HE relief: 190--210 C, 2--23 hr` / `Max hardness: 350--400 C, 1 hr` / `Result: 1000--1200+ HV`
- Purpose: `Ni3B precipitation hardening`
- Check: `HE relief within 4 hours of plating for high-strength steel`

*Box 8 -- Passivation / Inspect:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Passivation / Inspect`
- Parameters: `Tri-Cr conversion (optional)` / `Thickness: XRF` / `Hardness: Vickers HV`
- Purpose: `Improve corrosion protection; verify deposit quality`
- Check: `EN-B corrosion resistance < EN High-P -- passivation often essential`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
| `#E05C5C` (Coral) | `Caution / Problem` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- Parameter Summary Table

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> AT-A-GLANCE PARAMETERS

---

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | pH (2.0") | Key Control (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.6".

| Stage | Chemistry | Temp | Time | pH | Key Control |
|---|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30--60 g/L + surfactant | 140--176 F | 3--10 min | >12 | Water-break-free |
| 2. Rinse | DI counterflow | Ambient | 30--60 sec | -- | <50 uS/cm |
| 3. Activation | HCl / H2SO4 / zincate (substrate) | Ambient | 30--120 sec | -- | Substrate-dependent |
| 4. Rinse | DI counterflow | Ambient | 30--60 sec | -- | <20 uS/cm; no Cl- drag-in |
| 5. EN-B Plate | NiCl2 + DMAB or NaBH4 + EDA | 140--203 F | Per spec | 6--14 | DMAB or NaBH4 replenish |
| 6. Rinse | DI (cold preferred) | Ambient | 30--60 sec | -- | Do not air-dry |
| 7. Heat Treatment | Air or inert atmosphere | 350--400 C | 1 hr (max HV) | -- | HE relief first if >1000 MPa |
| 8. Passivate/Inspect | Tri-Cr conversion (optional) | -- | Per spec | -- | ASTM B841 compliance |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Stage names: Inter Medium, 13 pt.

---

### ZONE 4 -- EN-B vs. EN-P vs. Hard Chrome

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE HARD CHROME QUESTION -- EN-B VS. EN-P VS. HARD CHROME

---

**BLOCK E -- Three-Column Comparison**

Y: 22.9" to 28.3".

**Column 1 -- EN-B (Heat-Treated):**
- Rounded rect, X: 0.5", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `EN-B (HEAT-TREATED)` Barlow SemiBold 18 pt `#27AE60`
- Subtitle: `The Hardness Champion` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Hardness | 1000--1200 HV |
| Friction | 0.05--0.12 |
| Corrosion (NSS) | 200--500 hrs |
| Cr6+ chemistry | NONE |
| Cost | HIGH (DMAB) |

**Column 2 -- EN High-P (Heat-Treated):**
- Rounded rect, X: 8.33", Y: 22.9", W: 7.33", H: 5.2", fill `#1E2435`
- Left accent: `#2EC4B6`, 0.06"
- Title: `EN HIGH-P (HEAT-TREATED)` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `The Corrosion King` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Hardness | 800--900 HV |
| Friction | 0.10--0.15 |
| Corrosion (NSS) | 1,000+ hrs |
| Cr6+ chemistry | NONE |
| Cost | MODERATE |

**Column 3 -- Hard Chrome:**
- Rounded rect, X: 16.16", Y: 22.9", W: 7.34", H: 5.2", fill `#1E2435`
- Left accent: `#E05C5C`, 0.06"
- Title: `HARD CHROME` Barlow SemiBold 18 pt `#E05C5C`
- Subtitle: `The Regulated Incumbent` Barlow Condensed ExtraBold 13 pt `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Hardness | 900--1100 HV |
| Friction | 0.12--0.16 |
| Corrosion (NSS) | 24--100 hrs |
| Cr6+ chemistry | YES -- regulated |
| Cost | LOW--MODERATE |

Bottom spanning callout:
- Rounded rect, X: 0.5", W: 23.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Text: `EN-B matches or exceeds hard chrome hardness with zero hexavalent chromium. The tradeoff: higher cost and lower corrosion resistance.` Inter Medium, 14 pt, `#27AE60`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

---

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS

---

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SKIP PLATING | Poor activation or stabilizer poisoning | Verify activation; check stabilizer; try Pd flash |
| 2 | 6.33" | BATH DECOMPOSITION | Under-loaded at temp; Fe/Cu contamination; DMAB idle decomposition | Never idle at temp; filter; load parts before heating |
| 3 | 12.16" | PITTING | Chloride drag-in; H2 bubbles; poor agitation | Improve pre-plate rinse; increase agitation |
| 4 | 18.0" | LOW HARDNESS | Insufficient heat treatment; incorrect B% | Verify HT temp/time; check bath chemistry for B content |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for electroless nickel-boron plating per ASTM B841. Specific formulations, concentrations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Deposition rates from published literature -- verify against supplier data.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Electroless Nickel-Boron -- Process Flow

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
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - EN-B vs EN-P vs Chrome | Section label, three comparison columns |
| Zone 5 - Troubleshooting | Section label, four problem cards |
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

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Electroless Nickel-Boron Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Nickel-Boron Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Nickel-Boron Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Electroless Nickel-Boron Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Nickel-Boron Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Electroless Nickel-Boron Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

EN-B is the hardness story. The three-column comparison (EN-B vs. EN-P vs. Hard Chrome) is the centerpiece of this poster -- it answers the question every surface engineer asks: "Can EN-B replace hard chrome?" The answer is yes for hardness and wear, no for corrosion resistance, and the cost is higher. Watson flagged deposition rates for Tyler spot-check -- DMAB: 8-15 um/hr, borohydride: 15-25 um/hr. Watson also flagged ASTM B841 status verification. The headline font size is 80 pt (not 88) because "ELECTROLESS NICKEL-BORON" is a longer title than most.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #271 -- Construction Workup v1.0*
*2026-04-26*
