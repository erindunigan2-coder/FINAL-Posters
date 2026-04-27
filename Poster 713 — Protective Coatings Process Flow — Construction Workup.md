---
Project: Plating Posters Inc
Poster Number: 713
Title: "Protective Coatings -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief"
Technical Source: Industry-standard protective coating systems for severe service -- marine, tank lining, concrete, pipeline, infrastructure. Multi-coat 2K reactive systems (epoxy + urethane) totaling 6--20+ mils DFT. Complete process from surface preparation through inspection.
Process Scope: Protective coatings (epoxy/urethane) -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ProtectiveCoatings
  - EpoxyUrethane
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #713 -- Construction Workup
## Protective Coatings -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Cluster 8: Protective Coatings (Epoxy / Urethane). These are the heavy-duty multi-coat systems that protect bridges, ships, offshore platforms, tank linings, and concrete floors. The hero is a U-flow diagram showing the 8-stage process. The system architecture callout shows the three-coat build: zinc-rich primer + high-build epoxy intermediate + aliphatic polyurethane topcoat.

Design philosophy: U-flow diagram as the hero (matching Cluster 7 overview), a system architecture diagram showing the three-coat stack, a service environment callout, and a troubleshooting quick-hit strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Process flow diagram (Block B -- HERO):** Eight rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--8). Same pattern as Poster #704.
2. **System architecture diagram (Block D):** Cross-section showing the three-coat stack with DFT for each layer.
3. **Service environment callout (Block E):** Where these systems are used and why.
4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6")
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip
ZONE 3 -- SYSTEM ARCHITECTURE DIAGRAM (15.5"--22.0" / ~6.5")
  Block D: Three-coat cross-section stack
ZONE 4 -- SERVICE ENVIRONMENTS (22.0"--28.5" / ~6.5")
  Block E: Where and why these systems are specified
ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0")
  Block F: 4 common problems
ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Disclaimer, title, series, logo, version
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

---

**BLOCK A -- Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> PROTECTIVE COATINGS

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Complete Process Flow -- Epoxy & Urethane Systems for Severe Service

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 22 pt
- Color: `#F0EDE8` at 65%
- Text:

> Multi-coat, two-component reactive systems -- 6 to 20+ mils of barrier and UV protection for the most demanding environments.

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

Y: 3.8" to 14.0" (~10.2" tall). Two rows of four boxes in a U-flow pattern.

Each flow box:
- Element type: Rounded rectangle
- Width: 5.0". Height: 4.5"
- Fill: `#1E2435` (Dark Callout)
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip at the top of each box

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Surface Prep (Blast) | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Cleaning (SP1 + Salt Removal) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Cleaning |
| 3. Rinse / Dry | Box 3 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 4. Pretreatment (Primer) | Box 4 | 17.0" | `#E8A020` (Amber) | Pretreatment |

**Arrows between top-row boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered within boxes (~6.1")

**Vertical connector (Stage 4 to Stage 5):**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, down.

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Application (Multi-Coat) | Box 5 | 17.0" | `#E8A020` (Amber) | Application |
| 6. Flash / Recoat Windows | Box 6 | 11.5" | `#27AE60` (Emerald) | Flash |
| 7. Cure | Box 7 | 6.0" | `#27AE60` (Emerald) | Cure |
| 8. Inspection & Testing | Box 8 | 0.5" | `#C8D0D8` (Silver) | Inspection |

**Inside each flow box (top to bottom):**

*Box 1 -- Surface Prep:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Surface Prep`
- Parameters:
```
Steel: SSPC-SP10 (new) / SP5 (immersion)
Concrete: ICRI CSP 2--5
Profile: 2.0--4.0 mils (steel)
```
- Purpose: `Clean, profiled substrate for multi-coat adhesion`
- Check: `Soluble salts: Cl- < 3 ug/cm2, SO4 < 10 ug/cm2`

*Box 2 -- Cleaning:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Cleaning`
- Parameters:
```
SSPC-SP1 (solvent clean before blast)
Salt removal: pressurized fresh water
Concrete: alkaline degrease + power wash
```
- Purpose: `Remove oils, salts, and surface contaminants`
- Check: `ASTM D4285 blotter test for oil-free air`

*Box 3 -- Rinse / Dry:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Rinse / Dry`
- Parameters:
```
Steel: no rinse after blast -- keep dry
Concrete: 24 hr minimum dry after wash
Dew point: surface temp > 5 deg F above dew point
```
- Purpose: `Ensure dry substrate before coating`
- Check: `ASTM E337 dew point; ASTM F2170 concrete RH`

*Box 4 -- Pretreatment (Primer):*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Pretreatment / Primer`
- Parameters:
```
Steel: zinc-rich or epoxy primer (2--4 mils)
Concrete: epoxy penetrating sealer (optional)
No conversion coating required
```
- Purpose: `Corrosion protection + adhesion foundation`
- Check: `Blast profile provides mechanical adhesion`

*Box 5 -- Application (Multi-Coat):*
- Badge: `STAGE 5`, fill `#E8A020`
- Name: `Application`
- Parameters:
```
Epoxy intermediate: 4--8 mils per coat
PU topcoat: 2--3 mils
Total system: 6--20+ mils
```
- Purpose: `Build barrier thickness + UV protection`
- Check: `Mix ratio, pot life, stripe coat edges first` (Coral `#E05C5C`)

*Box 6 -- Flash / Recoat Windows:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Flash / Recoat`
- Parameters:
```
Epoxy over epoxy: min 6--16 hr, max 3--7 days
PU over epoxy: min 6--16 hr, max 3--7 days
Stripe coat before each full coat
```
- Purpose: `Intercoat adhesion and film integrity`
- Check: `CRITICAL: Amine blush removal before recoat` (Coral `#E05C5C`)

*Box 7 -- Cure:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Cure`
- Parameters:
```
Epoxy: 7--14 days ambient; force cure 140--180 deg F
Urethane: 5--7 days ambient
Tank lining: full cure before filling
```
- Purpose: `Develop full chemical and mechanical resistance`
- Check: `MEK rub (50+ double rubs) + Shore D hardness`

*Box 8 -- Inspection & Testing:*
- Badge: `STAGE 8`, fill `#C8D0D8`
- Name: `Inspection`
- Parameters:
```
DFT: ASTM D7091 / SSPC-PA 2
Holiday detection: ASTM D5162 / D4787
Adhesion: ASTM D4541 (> 200 psi)
```
- Purpose: `Verify system meets specification before service`
- Check: `Holiday test mandatory for tank lining and pipeline`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3"

- Rounded rectangle, X: 0.5", Y: 14.3", W: 23.0", H: 0.8", fill `#252B3D`, radius 4

Four legend items evenly spaced:

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Prep & Cleaning` |
| `#E8A020` (Amber) | `Primer & Application` |
| `#27AE60` (Emerald) | `Flash & Cure` |
| `#C8D0D8` (Silver) | `Inspection` |

Each swatch: 0.3" x 0.3" rounded rect. Label: Inter Medium, 14 pt, `#F0EDE8`.

---

### ZONE 3 -- System Architecture Diagram

**Dimensions:** Y: 15.5" to 22.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THREE-COAT SYSTEM ARCHITECTURE

---

**BLOCK D -- Cross-Section Stack (Y: 16.3" to 21.8")**

Large cross-section diagram showing three coating layers on a steel substrate:

**Substrate base:**
- Rectangle, X: 2.0", Y: 19.5", W: 20.0", H: 1.5", fill `#3A4055`, border 2 pt `#C8D0D8`
- Label: `STEEL SUBSTRATE (blast profile 2.0--4.0 mils)` Barlow SemiBold 14 pt `#C8D0D8`

**Layer 1 -- Primer (bottom coat):**
- Rectangle above substrate, H: 0.8", fill `#27AE60` at 40%
- Label (left): `PRIMER` Barlow SemiBold 14 pt `#27AE60`
- Label (right): `Zinc-rich or epoxy -- 2--4 mils` JetBrains Mono 12 pt `#F0EDE8`
- Purpose: `Corrosion protection, galvanic (zinc) or barrier (epoxy)`

**Layer 2 -- Intermediate (middle coat):**
- Rectangle above primer, H: 1.5", fill `#2EC4B6` at 30%
- Label (left): `INTERMEDIATE` Barlow SemiBold 14 pt `#2EC4B6`
- Label (right): `High-build epoxy -- 4--8 mils per coat` JetBrains Mono 12 pt `#F0EDE8`
- Purpose: `Barrier protection, chemical resistance, build thickness`

**Layer 3 -- Topcoat (top coat):**
- Rectangle above intermediate, H: 0.6", fill `#E8A020` at 40%
- Label (left): `TOPCOAT` Barlow SemiBold 14 pt `#E8A020`
- Label (right): `Aliphatic polyurethane -- 2--3 mils` JetBrains Mono 12 pt `#F0EDE8`
- Purpose: `UV resistance, color retention, gloss, weathering`

**Total DFT callout (right side):**
- Vertical bracket spanning all three layers
- `TOTAL: 6--20+ mils` Barlow Condensed ExtraBold 20 pt `#E8A020`

**Why 2K callout (below diagram, Y: 20.5"):**
- Rounded rect, W: 20.0", H: 1.0", fill `#1E2435`, left accent `#E8A020`
- `Why two-component? Epoxy (resin + amine) and urethane (polyol + isocyanate) cross-link into thermoset films that cannot be achieved with single-component coatings. The chemistry requires mixing immediately before application.`
- Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Service Environments

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

---

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> WHERE THESE SYSTEMS ARE SPECIFIED

---

**BLOCK E -- Six Environment Cards (Y: 22.9" to 28.3")**

3x2 grid of service environment cards:

| Position | Environment | Accent | System | DFT |
|---|---|---|---|---|
| R1C1 | Marine / Offshore | `#2EC4B6` | IOZ + epoxy + PU | 10--16 mils |
| R1C2 | Tank Lining | `#E8A020` | Solventless epoxy (NSF 61 for potable) | 12--20+ mils |
| R1C3 | Concrete Floors | `#27AE60` | Epoxy primer + epoxy topcoat | 10--15 mils |
| R2C1 | Pipeline (External) | `#2EC4B6` | Fusion-bonded epoxy or liquid epoxy | 12--25 mils |
| R2C2 | Bridge / Infrastructure | `#E8A020` | IOZ + epoxy + PU (per ISO 12944 C5/CX) | 10--14 mils |
| R2C3 | Chemical Processing | `#E05C5C` | Novolac epoxy (max chemical resistance) | 15--25 mils |

Each card: Rounded rect, W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in environment color.

Interior: Environment name: Barlow SemiBold 16 pt in accent color. System and DFT: JetBrains Mono 12 pt `#F0EDE8`.

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
| 1 | 0.5" | INTERCOAT DELAMINATION | Amine blush not removed; exceeded max recoat | Wash blush with water; scuff sand if recoat window exceeded |
| 2 | 6.33" | SOLVENT ENTRAPMENT (BUBBLING) | Applied too thick; solvent trapped in film | Reduce DFT per coat; allow adequate flash |
| 3 | 12.16" | HOLIDAYS (PINHOLES) | Thin spots at edges, welds, bolt heads | Stripe coat all edges first; holiday test entire surface |
| 4 | 18.0" | PREMATURE TOPCOAT FAILURE | Aromatic urethane used for exterior exposure | Specify ALIPHATIC polyurethane for UV exposure |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Process parameters shown are typical industry values for epoxy and urethane protective coating systems. Specific formulations, DFT requirements, and cure conditions vary by product. Consult your coating supplier and applicable specification for application-specific guidance. Source: General industry knowledge; SSPC standards; Watson Research Brief.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Protective Coatings -- Process Flow

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
| Zone 3 - System Architecture | Section label, three-coat cross-section, 2K callout |
| Zone 4 - Service Environments | Section label, six environment cards |
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

Stage badges: Verify text legibility on darkened fills -- may need `#F5F4F0` text.

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Protective Coatings Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Protective Coatings Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Protective Coatings Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Protective Coatings Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Protective Coatings Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Protective Coatings Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This overview poster mirrors the structure of Poster #704 (Industrial Priming Process Flow) to maintain visual consistency across the painting clusters. The system architecture cross-section is the unique element -- it shows physically how the three coats stack up and why each layer serves a different purpose. The service environment grid makes it immediately clear where these systems are used: this is not decorative painting, this is industrial protection for extreme environments.

---

*Alaina -- Poster #713 -- Construction Workup v1.0 -- 2026-04-26*
