---
Project: Plating Posters Inc
Poster Number: 191
Title: "Aluminum Conversion Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-06 Aluminum Conversion)"
Technical Source: Industry-standard aluminum conversion coating processes -- Ti/Zr, Zr-only, rare earth, and sol-gel alternatives. Completely chromium-free technologies. Complete 7-stage sequence from cleaning through dry/seal. Values are typical ranges.
Process Scope: Chromium-free aluminum conversion coating -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - AluminumConversion
  - ChemFilm
  - ProcessFlow
  - ConstructionWorkup
  - ClusterCC06
---

# Poster #191 -- Construction Workup
## Aluminum Conversion Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CC-06: Chromium-Free Aluminum Conversion Coatings. It covers the BROADER category of entirely Cr-free technologies -- Ti/Zr conversion coatings (the dominant commercial alternative), Zr-only systems (dominant in automotive), rare earth (cerium) coatings (emerging), and sol-gel hybrids.

Key framing: these are NOT chromate coatings. They contain zero chromium of any valence. They are the "post-chromium" future, especially for automotive multi-metal pretreatment where one bath must work on steel, galvanized, AND aluminum in the same body.

Design philosophy: clean U-flow diagram as the hero, a technology comparison panel (Zr vs. Ti/Zr vs. Cerium vs. Sol-Gel), a compact parameter summary, and a troubleshooting strip.

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

1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Same geometry as Poster #183.

2. **Parameter summary table (Block D):** 7-row table.

3. **Technology comparison panel (Block E):** Four technology columns (Zr-only, Ti/Zr, Cerium, Sol-Gel) comparing key properties.

4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

5. **Standard accent borders, light remap, JetBrains Mono.**

6. **Print size -- 24x36".**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Seven-stage U-flow diagram
  Block C: Stage legend strip

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 7-row parameter table

ZONE 4 -- TECHNOLOGY COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Four-technology comparison panel

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
- Font: Barlow SemiBold, 32 pt, `#27AE60` (Emerald)
- Text: `Complete Process Flow -- 7 Stages from Cleaning to Seal`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Zero chromium. Ti/Zr conversion technology for aluminum pretreatment. One bath, multiple substrates, no heavy metal waste.`
- Y: 2.2"

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE COMPLETE PROCESS -- STAGE BY STAGE`

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same geometry as Poster #183.

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Deox) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Acid Etch / Deoxidize | Box 3 | 11.5" | `#E8A020` (Amber) | Surface Conditioning |
| 4. Rinse (Pre-Coat) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-7:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Ti/Zr Conversion Coat | Box 5 | 17.0" | `#27AE60` (Emerald) | Conversion Coating |
| 6. Rinse (Post-Coat) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Dry / Seal | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |

Empty space at X: 0.5" on bottom row can hold callout: `Multi-metal capable: steel + galvanized + aluminum in one bath. The automotive OEM standard.` Inter Medium 14 pt `#27AE60`.

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `Non-etch, pH 9--11` / `100--160 F (38--71 C)` / `1--10 min`
- Purpose: `Remove oils, soils, shop contaminants`
- Check: `Multi-metal cleaner for mixed-substrate lines`

*Box 2 -- Rinse (Pre-Deox):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Deoxidize`
- Parameters: `Ambient temp` / `Overflow or spray`
- Purpose: `Remove cleaner before acid stage`
- Check: `DI/RO preferred; minerals compete with coating`

*Box 3 -- Acid Etch / Deoxidize:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Acid Etch / Deoxidize`
- Parameters: `HNO3 or acidic ZrF/TiF rinse` / `pH 2.5--4.5` / `Ambient--120 F, 30 sec--5 min`
- Purpose: `Remove oxide and smut; activate surface`
- Check: `Alloy-matched chemistry (same as chromate lines)`

*Box 4 -- Rinse (Pre-Coat):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Coat`
- Parameters: `DI or RO preferred` / `Ambient`
- Purpose: `Remove acid; prevent mineral competition`
- Check: `Dissolved minerals compete with Zr deposition`

*Box 5 -- Ti/Zr Conversion Coat (Main Stage):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Ti/Zr Conversion Coat` / Subtitle: `Main Stage`
- Parameters: `50--200 ppm Zr` / `pH 3.8--5.0` / `70--120 F, 60--180 sec`
- Purpose: `Deposit ZrO2/TiO2 amorphous barrier film`
- Check: `Film is nearly INVISIBLE -- verify with XRF`

*Box 6 -- Rinse (Post-Coat):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Coat`
- Parameters: `DI water (critical)` / `Ambient` / `15--60 sec`
- Purpose: `Remove residual coating solution`
- Check: `Tap water minerals visible on ultra-thin film`

*Box 7 -- Dry / Seal:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Dry / Seal`
- Parameters: `Air dry or 180--250 F oven` / `Some hybrids need thermal cure` / `5--15 min`
- Purpose: `Dry film; crosslink if hybrid chemistry`
- Check: `Over-cure degrades film -- follow supplier TDS`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3". Same construction as Poster #183.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

**BLOCK D -- 7-Row Parameter Table**

Y: 16.3" to 21.8". Column widths: Stage (3.5") | Chemistry (5.5") | Temperature (3.0") | Time (2.5") | pH (2.0") | Key Control (6.5")

| Stage | Chemistry | Temp | Time | pH | Key Control |
|---|---|---|---|---|---|
| 1. Clean | Non-etch alkaline, pH 9--11 | 100--160 F | 1--10 min | 9--11 | Multi-metal compatible |
| 2. Rinse | DI or RO water | Ambient | 30--60 sec | -- | Low conductivity |
| 3. Deoxidize | HNO3 or acidic ZrF/TiF | Amb--120 F | 30 sec--5 min | 2.5--4.5 | Alloy-matched |
| 4. Rinse | DI or RO water | Ambient | 30--60 sec | -- | Minimize dissolved minerals |
| 5. Ti/Zr Coat | H2ZrF6 50--200 ppm Zr | 70--120 F | 60--180 sec | 3.8--5.0 | XRF verification |
| 6. Rinse | DI water | Ambient | 15--60 sec | -- | DI critical for appearance |
| 7. Dry/Seal | -- | Air or 180--250 F | 5--15 min | -- | Check if thermal cure needed |

Data: JetBrains Mono 12 pt. Alternating rows.

---

### ZONE 4 -- Technology Comparison

**Section label:** `FOUR TECHNOLOGIES -- ONE GOAL: ZERO CHROMIUM` -- Y: 22.2".

**BLOCK E -- Four-Column Technology Panel**

Y: 22.9" to 28.3". Four vertical callout boxes:

| Technology | X | W | Accent | Key Data |
|---|---|---|---|---|
| Zr-Only | 0.5" | 5.5" | `#27AE60` | Dominant automotive; H2ZrF6; 50--200 ppm Zr; 20--100 nm film; nearly invisible; minimal sludge; multi-metal |
| Ti/Zr Hybrid | 6.25" | 5.5" | `#2EC4B6` | Combined Ti/Zr fluorocomplexes; broader operating window; some aerospace approvals |
| Cerium (Rare Earth) | 12.0" | 5.5" | `#E8A020` | Emerging; CeO2/Ce(OH)3 on cathodic sites; promising for 2xxx/7xxx Cu-alloys; still primarily R&D |
| Sol-Gel Hybrid | 17.75" | 5.75" | `#C8D0D8` | Organic-inorganic hybrid; silane + metal oxide; may require thermal cure; excellent paint base |

Each box: Rounded rect, H: 5.0", fill `#1E2435`, top accent 4 pt.
Title: Barlow SemiBold 18 pt in accent color. Status tag: small rounded rect below title.

Content per box (Inter Regular 13 pt `#F0EDE8`):
- Active component and concentration
- Film thickness
- Multi-metal compatibility
- Bare salt spray range
- Key advantage
- Key limitation

Status tags:
- Zr-Only: `COMMERCIAL STANDARD` in `#27AE60`
- Ti/Zr: `ESTABLISHED` in `#2EC4B6`
- Cerium: `EMERGING` in `#E8A020`
- Sol-Gel: `SPECIALIZED` in `#C8D0D8`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #183.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NO VISIBLE COATING | Normal for Zr -- film is nearly invisible | Verify by XRF (5--30 mg/m2 Zr); do NOT judge by eye |
| 2 | 6.33" | POOR PAINT ADHESION | Coating too thin; contamination; wrong pH | Increase immersion time; improve cleaning; check pH |
| 3 | 12.16" | WATER SPOTS | Hard water rinse; poor drainage; DI failure | Check DI conductivity; improve racking/drainage |
| 4 | 18.0" | INCONSISTENT XRF | Uneven coating; mixed substrates in same load | Optimize per substrate; separate alloy families if possible |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Aluminum Conversion Coating -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for Ti/Zr and related non-chromate conversion coating systems on aluminum. No dedicated MIL-SPEC exists for Zr conversion coatings as of this printing. Automotive OEM specifications are proprietary. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Aluminum Conversion Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster marks the transition from chromate-based chemistry to the "post-chromium" future. The technology comparison panel is the educational centerpiece -- most shops know about hex and tri chromate but are less familiar with Zr/Ti alternatives. The "NO VISIBLE COATING" troubleshooting card addresses the single most common misunderstanding: operators expect to SEE the coating (like gold chem film), but Zr coatings are nearly invisible. XRF is the only reliable verification.

Watson flag: Confirm no MIL-SPEC has been issued for Zr conversion coatings as of 2026. SAE ARP 5903 is for evaluation, not specification.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #191 -- Construction Workup v1.0*
*2026-04-26*
