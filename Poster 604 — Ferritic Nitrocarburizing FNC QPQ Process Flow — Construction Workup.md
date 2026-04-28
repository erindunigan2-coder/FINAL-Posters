---
Project: Plating Posters Inc
Poster Number: 604
Title: "Ferritic Nitrocarburizing (FNC / Q-P-Q) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: Ferritic Nitrocarburizing / FNC / Q-P-Q)"
Technical Source: Industry-standard ferritic nitrocarburizing and Q-P-Q (Quench-Polish-Quench) process. Salt bath FNC at 1050-1125 F, oxidizing quench at 700-800 F, mechanical polish, second oxidizing quench. Q-P-Q corrosion resistance: 200-500 hours neutral salt spray on low-carbon steel. Per AMS 2753, AMS 2755, and ASTM B117.
Process Scope: Ferritic nitrocarburizing (FNC/Q-P-Q) -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - Q-P-Q
  - SaltBathFNC
  - GasFNC
  - ProcessFlow
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #604 -- Construction Workup
## Ferritic Nitrocarburizing (FNC / Q-P-Q) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Ferritic Nitrocarburizing -- the process that gun owners, hydraulic engineers, and automotive engineers rely on for wear and corrosion resistance as a hard chrome replacement and crankshaft treatment. FNC operates below Ac1 (ferritic range), produces a hard epsilon iron nitride compound zone, and when the full Q-P-Q (Quench-Polish-Quench) cycle is applied, delivers corrosion resistance that exceeds hard chrome in salt spray testing at 200-500 hours. Minimal distortion, matte black appearance, no hexavalent chromium.

Design philosophy: same U-flow hero layout for cluster consistency. The Q-P-Q variant is the star, so the 9-step sequence follows the full Q-P-Q path. Amber and Coral get prominent play -- this is a hot process with molten salt, and the hazard profile demands respect.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1-5), vertical connector, bottom row R-to-L (stages 6-9).
2. **Parameter summary table (Block D):** Compact 9-row table (one per stage).
3. **Process variants callout (Block E):** Salt bath FNC, gas FNC, and Q-P-Q variants -- what distinguishes each.
4. **Troubleshooting quick-hit strip (Block F):** Four common FNC/Q-P-Q failures.

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
- **JetBrains Mono Regular** -- all parameter data, chemical formulas, temperature ranges, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Heat/salt bath stages, warning headers |
| Teal | `#2EC4B6` | Preparation stages, structural positives |
| Emerald | `#27AE60` | Core process (nitrocarburize), optimal reference |
| Coral | `#E05C5C` | Safety hazards, failures, molten salt warnings |
| Mid Slate | `#3A4055` | Table headers, dividers, flow arrows |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Callout box fills, flow box fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides:** 0.5" / 23.5"
**Horizontal guides:** 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Nine-stage U-flow diagram (top row 5, bottom row 4)
  Block C: Stage legend strip (color key)

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 9-row parameter table (one row per stage)

ZONE 4 -- PROCESS VARIANTS (22.0"--28.5" / ~6.5" tall)
  Block E: Salt bath FNC, gas FNC, and Q-P-Q variants

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip with one-line fixes

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

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold
- Size: 72 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> FERRITIC NITROCARBURIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 32 pt
- Color: `#27AE60` (Emerald)
- Text:

> FNC / Q-P-Q (Quench-Polish-Quench) -- Complete Process Flow

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Nitrogen + carbon below Ac1. Epsilon compound zone for wear. Oxidizing salt quench for corrosion. The process that replaces hard chrome without hexavalent chromium.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE COMPLETE Q-P-Q PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same geometry as other DH cluster Process Flow posters.

Each flow box: Rounded rect W: 4.2", H: 4.3", fill `#1E2435`, radius 8, top accent 4 pt.

**Top Row (Y: 3.8" to 8.1") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Pre-Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Preheat | Box 2 | 5.0" | `#E8A020` (Amber) | Heat |
| 3. Nitrocarburize | Box 3 | 9.5" | `#27AE60` (Emerald) | Core Process |
| 4. Oxidizing Quench (Q1) | Box 4 | 14.0" | `#E8A020` (Amber) | Q-P-Q |
| 5. Rinse | Box 5 | 18.5" | `#2EC4B6` (Teal) | Prep |

**Arrows:** 3 pt `#3A4055`, filled arrowheads.

**Vertical connector** from Box 5 bottom to Box 6 top.

**Bottom Row (Y: 9.7" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Polish (P) | Box 6 | 17.5" | `#2EC4B6` (Teal) | Mechanical |
| 7. Second Oxidizing Quench (Q2) | Box 7 | 12.0" | `#E8A020` (Amber) | Q-P-Q |
| 8. Final Rinse | Box 8 | 6.5" | `#2EC4B6` (Teal) | Prep |
| 9. Inspection & QA | Box 9 | 1.0" | `#27AE60` (Emerald) | Quality |

**Inside each flow box:**

*Box 1 -- Pre-Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Pre-Clean`
- Parameters:
```
Alkaline wash, rinse, dry
Surface must be free of ALL moisture
Moisture + molten salt = EXPLOSION
```
- Purpose: `Remove oils, chips, and -- critically -- all moisture before any salt bath contact`
- Check: `Parts must be completely dry before preheat`

*Box 2 -- Preheat:*
- Badge: `STAGE 2`, fill `#E8A020`
- Name: `Preheat`
- Parameters:
```
600--700 F (316--371 C)
Air or protective atmosphere
Drives off ALL residual moisture
```
- Purpose: `Mandatory moisture removal before molten salt immersion -- safety-critical step`
- Check: `No visible moisture or condensation on ANY part surface`

*Box 3 -- Nitrocarburize:*
- Badge: `STAGE 3`, fill `#27AE60`
- Name: `Nitrocarburize`
- Parameters:
```
Salt bath: 1050--1075 F (566--580 C)
Cyanate-based (NaCNO/KCNO)
60--120 minutes (standard)
```
- Purpose: `Simultaneous nitrogen + carbon diffusion into ferrite; forms epsilon Fe2-3N compound zone`
- Check: `Bath temperature and cyanate concentration verified` (Emerald `#27AE60`)

*Box 4 -- Oxidizing Quench (Q1):*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Oxidizing Salt Quench (Q1)`
- Parameters:
```
Oxidizing salt: 700--800 F (371--427 C)
NaNO3/NaNO2 bath
15--30 minutes
```
- Purpose: `Creates black magnetite (Fe3O4) layer that seals compound zone pores -- dramatic corrosion boost`
- Check: `Transfer time from FNC bath to oxidizing bath minimized`

*Box 5 -- Rinse:*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Hot Water Rinse`
- Parameters:
```
Hot water rinse
Remove all salt residue
Inspect for complete coverage
```
- Purpose: `Remove residual salt before mechanical polishing step`
- Check: `No visible salt deposits remaining`

*Box 6 -- Polish (P):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Polish (P)`
- Parameters:
```
Mechanical: buffing, lapping, or
centerless grinding
Target: Ra 8--16 micro-inch
```
- Purpose: `Smooth the surface and expose fresh compound zone for second oxidizing quench`
- Check: `Surface roughness verified to specification`

*Box 7 -- Second Oxidizing Quench (Q2):*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Second Oxidizing Quench (Q2)`
- Parameters:
```
Same oxidizing salt bath
700--800 F (371--427 C)
15--30 minutes
```
- Purpose: `Second oxide layer on freshly polished surface -- completes the corrosion protection system`
- Check: `Uniform matte black appearance after Q2`

*Box 8 -- Final Rinse:*
- Badge: `STAGE 8`, fill `#2EC4B6`
- Name: `Final Rinse`
- Parameters:
```
Hot water rinse
Rust preventative if required
Dry thoroughly
```
- Purpose: `Remove all residual salt; apply corrosion inhibitor if parts will be stored`
- Check: `Clean, dry, uniform matte black finish`

*Box 9 -- Inspection & QA:*
- Badge: `STAGE 9`, fill `#27AE60`
- Name: `Inspection & QA`
- Parameters:
```
Compound zone: 10--25 um (0.0004--0.001")
Surface hardness: 600--1000 HV
Salt spray: 200--500 hr (Q-P-Q on 1018)
```
- Purpose: `Verify compound zone thickness, hardness, corrosion resistance, and appearance`
- Check: `Dimensional change typically <0.0002" (5 um)`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3". Same format as other DH clusters.

| Swatch | Label |
|---|---|
| `#2EC4B6` | `Preparation & Mechanical` |
| `#E8A020` | `Heat / Salt Bath` |
| `#27AE60` | `Core Process & QA` |
| `#E05C5C` | `Critical / Hazard` |
| `#C8D0D8` | `Equipment Reference` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Key Action (5.0") | Temperature (3.5") | Time (3.0") | Medium (4.5") | Key Control (4.0")

| Stage | Key Action | Temp | Time | Medium | Key Control |
|---|---|---|---|---|---|
| 1. Pre-Clean | Alkaline wash, dry | Ambient | 10--15 min | Alkaline solution | Zero moisture |
| 2. Preheat | Moisture removal | 600--700 F | 15--30 min | Air | Completely dry |
| 3. Nitrocarburize | Salt bath immersion | 1050--1075 F | 60--120 min | NaCNO/KCNO salt | Cyanate 35--40% |
| 4. Q1 | Oxidizing salt quench | 700--800 F | 15--30 min | NaNO3/NaNO2 salt | Transfer time |
| 5. Rinse | Salt removal | Hot water | 5--10 min | Water | No residual salt |
| 6. Polish | Mechanical smoothing | Ambient | Per part | Buffing/lapping | Ra 8--16 micro-inch |
| 7. Q2 | Second oxidizing quench | 700--800 F | 15--30 min | NaNO3/NaNO2 salt | Uniform black |
| 8. Final Rinse | Salt removal + protect | Hot water | 5--10 min | Water + RP | Clean and dry |
| 9. Inspect | Hardness, zone, corrosion | Ambient | -- | -- | Per AMS 2753/2755 |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- Process Variants

**Section label:** `FNC PROCESS VARIANTS -- SAME METALLURGY, DIFFERENT METHODS` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Four variant cards in a row (Y: 22.9" to 28.3")**

| Card | X | W | Name | Description | Accent |
|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | `SALT BATH FNC` | The original method. Parts immersed in molten cyanate salt at 1050--1075 F. Uniform case depth. Excellent for complex geometries. Requires cyanide waste management. | `#E8A020` |
| 2 | 6.33" | 5.5" | `GAS FNC` | NH3 + CO2 atmosphere in a sealed retort. No molten salt handling. Cleaner process. Lower corrosion resistance unless supplemented with oxidizing post-treatment. | `#27AE60` |
| 3 | 12.16" | 5.5" | `Q-P-Q (QUENCH-POLISH-QUENCH)` | Full oxidizing quench, mechanical polish, second oxidizing quench cycle. Maximum corrosion protection -- 200--500 hr salt spray on low-carbon steel. The gold standard for wear + corrosion in one treatment. | `#2EC4B6` |
| 4 | 18.0" | 5.5" | `PLASMA FNC` | Ion bombardment in vacuum. Precise case control. Can selectively treat surfaces. Most expensive method. Used in aerospace and precision tooling. | `#C8D0D8` |

Each: Rounded rect H: 5.0", fill `#1E2435`, top accent 4 pt.
Name: Barlow SemiBold 20 pt in accent color.
Details: Inter Regular 12 pt `#F0EDE8`.

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- `Different methods, same metallurgy. Every FNC variant produces an epsilon iron nitride compound zone on a ferritic substrate. The Q-P-Q variant adds the oxidizing quench and polish that makes corrosion resistance exceptional.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON FNC/Q-P-Q FAILURES` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | POOR CORROSION | Insufficient oxidizing quench time; poor polish quality | Extend Q1/Q2 time; improve polish to specified Ra |
| 2 | 6.33" | THIN COMPOUND ZONE | Low bath temperature; depleted cyanate content | Verify bath temp; analyze and replenish salts to 35--40% CNO |
| 3 | 12.16" | STAINING/DISCOLORATION | Salt residue not fully rinsed; contaminated oxidizing bath | Improve rinse thoroughness; maintain bath purity |
| 4 | 18.0" | PITTING | Moisture on parts before immersion (steam explosion micro-pits) | Improve preheat drying; extend preheat time |

Each card: Rounded rect W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.
Problem: Barlow SemiBold 16 pt `#E05C5C`.
Cause: Inter Regular 12 pt `#F0EDE8`.
Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center.

> This poster is an educational reference tool. Process parameters shown are typical industry values for ferritic nitrocarburizing with the Q-P-Q (Quench-Polish-Quench) variant. Specific bath compositions, cycle times, and acceptance criteria vary by specification, equipment, and part design. Consult AMS 2753, AMS 2755, and your salt bath equipment supplier.

**Poster title:** `Ferritic Nitrocarburizing (FNC / Q-P-Q) -- Process Flow`
**Series name:** `Plating Posters Inc -- Metal Finishing Reference Series`
**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, nine flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 9-row table |
| Zone 4 - Trademarked Names | Section label, five name cards, callout bar |
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
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Ferritic Nitrocarburizing FNC Q-P-Q Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

FNC/Q-P-Q is one of the most commercially relevant processes in this entire series -- it's the hard chrome replacement that the industry has been looking for, the gun barrel treatment that every firearms enthusiast has heard of, and the crankshaft treatment that automotive engineers specify daily. The process variants section (Zone 4) is essential because operators encounter FNC under multiple methods (salt bath, gas, plasma) and need to understand they're all variations of the same metallurgy. The Q-P-Q corrosion resistance figure (200-500 hours salt spray) is the headline stat that makes this process commercially compelling -- it exceeds hard chrome (24-96 hours typical) by an order of magnitude.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #604 -- Construction Workup v1.0*
*2026-04-26*
