---
Project: Plating Posters Inc
Poster Number: 568
Title: "Vacuum Carburizing (LPC) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC)"
Technical Source: Industry-standard vacuum (low pressure) carburizing process. Acetylene pulsed at 5--15 mbar, boost/diffuse cycles, HPGQ or oil quench. Values are typical production ranges per ASM Handbook Vol. 4 and AMS 2759/7.
Process Scope: Vacuum carburizing (LPC) -- complete process flow (9 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - HeatTreatment
  - Diffusion
  - ProcessFlow
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #568 -- Construction Workup
## Vacuum Carburizing (LPC) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Vacuum Carburizing (Low Pressure Carburizing / LPC). The modern, clean alternative to gas carburizing -- no endothermic atmosphere, no IGO, no CO exposure risk. Acetylene pulses at millibar pressures, computer-controlled recipes, and high-pressure gas quench. This poster shows the complete 9-stage process at a glance and highlights the key advantages over conventional gas carburizing.

Design philosophy: same U-flow hero as DH-01 (consistency across clusters), but with a distinctly "high-tech" feel -- the Teal accent color gets more play here because vacuum carburizing is the precision/aerospace method.

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

1. **Process flow diagram (Block B -- HERO):** Nine rounded rectangles in a U-flow: top row L-to-R (stages 1--5), vertical connector, bottom row R-to-L (stages 6--9). Same geometry as Poster #559 for cluster consistency.
2. **Parameter summary table (Block D):** Compact 9-row table (one per stage).
3. **LPC vs. Gas Carburizing comparison (Block E):** Side-by-side advantage/disadvantage comparison -- the key selling point for this process.
4. **Troubleshooting quick-hit strip (Block F):** Four common LPC-specific failures.

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
| Amber | `#E8A020` | Heat/temperature stages, warning headers |
| Teal | `#2EC4B6` | Vacuum/precision stages, structural positives |
| Emerald | `#27AE60` | Core process (boost/diffuse), optimal reference |
| Coral | `#E05C5C` | Safety hazards, failures |
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

ZONE 4 -- LPC VS. GAS CARBURIZING (22.0"--28.5" / ~6.5" tall)
  Block E: Side-by-side comparison

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
- Size: 80 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> VACUUM CARBURIZING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Font: Barlow SemiBold, 34 pt
- Color: `#2EC4B6` (Teal)
- Text:

> Low Pressure Carburizing (LPC) -- Complete Process Flow

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Font: Barlow SemiBold, 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Acetylene at millibar pressures. Computer-controlled recipes. Zero IGO. The precision carburizing process for aerospace and high-volume automotive.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

---

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE COMPLETE PROCESS -- STAGE BY STAGE

---

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same geometry as Poster #559.

Each flow box: Rounded rect W: 4.2", H: 4.3", fill `#1E2435`, radius 8, top accent 4 pt.

**Top Row (Y: 3.8" to 8.1") -- Stages 1-5, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Pre-Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Prep |
| 2. Load | Box 2 | 5.0" | `#2EC4B6` (Teal) | Prep |
| 3. Evacuate | Box 3 | 9.5" | `#2EC4B6` (Teal) | Vacuum |
| 4. Heat Under Vacuum | Box 4 | 14.0" | `#E8A020` (Amber) | Heat |
| 5. Boost/Diffuse Cycles | Box 5 | 18.5" | `#27AE60` (Emerald) | Core Process |

**Arrows:** 3 pt `#3A4055`, filled arrowheads.

**Vertical connector** from Box 5 bottom to Box 6 top.

**Bottom Row (Y: 9.7" to 14.0") -- Stages 6-9, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 6. Quench (HPGQ) | Box 6 | 17.5" | `#E05C5C` (Coral) | Critical |
| 7. Wash (if oil quench) | Box 7 | 12.0" | `#2EC4B6` (Teal) | Prep |
| 8. Temper | Box 8 | 6.5" | `#E8A020` (Amber) | Heat |
| 9. Inspection & QA | Box 9 | 1.0" | `#27AE60` (Emerald) | Quality |

**Inside each flow box:**

*Box 1 -- Pre-Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Pre-Clean`
- Parameters:
```
Solvent wash -- completely dry
No moisture (contaminates vacuum)
No chlorinated solvents
```
- Purpose: `Remove all contaminants; moisture degrades vacuum quality and pump oil`
- Check: `Parts must be bone-dry before loading`

*Box 2 -- Load:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Load`
- Parameters:
```
CFC (carbon fiber composite) fixtures
Ceramic (SiC, alumina) supports
NO alloy steel fixtures
```
- Purpose: `Steel fixtures absorb carbon from acetylene -- graphite/CFC does not`
- Check: `No metallic fixtures in the vacuum chamber`

*Box 3 -- Evacuate:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Evacuate`
- Parameters:
```
Pump to <0.1 mbar (hard vacuum)
Leak rate: <5 microns/hr
Roughing pump + roots blower
```
- Purpose: `Remove all oxygen and moisture before heating -- prevents oxidation`
- Check: `Base pressure reached before heating begins`

*Box 4 -- Heat Under Vacuum:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Heat Under Vacuum`
- Parameters:
```
1700--1850 F (927--1010 C)
Under vacuum -- no atmosphere
No oxidation, no IGO formation
```
- Purpose: `Austenitize steel in oxygen-free environment; higher temps possible (no IGO risk)`
- Check: `Verify temperature uniformity across load`

*Box 5 -- Boost/Diffuse Cycles:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Boost/Diffuse Cycles`
- Parameters:
```
Boost: C2H2 at 5--15 mbar
Diffuse: vacuum (<1 mbar)
5--30+ cycles per recipe
```
- Purpose: `Pulse acetylene for carbon absorption; evacuate for inward diffusion. Computer-controlled recipe.`
- Check: `Mass flow controller calibration verified` (Teal `#2EC4B6`)

*Box 6 -- Quench (HPGQ):*
- Badge: `STAGE 6`, fill `#E05C5C`
- Name: `Quench` / Subtitle: `High-Pressure Gas Quench`
- Parameters:
```
N2 at 10--20 bar or He at 15--20 bar
H = 0.10--0.40 (gas dependent)
Or: transfer to integrated oil quench
```
- Purpose: `Transform austenite to martensite; HPGQ = less distortion than oil`
- Check: `Verify interlock systems before initiating HPGQ` (Coral `#E05C5C`)

*Box 7 -- Wash:*
- Badge: `STAGE 7`, fill `#2EC4B6`
- Name: `Wash (If Oil Quench)`
- Parameters:
```
Required only for oil quench option
HPGQ parts are clean -- no wash needed
Alkaline wash if oil quench used
```
- Purpose: `Remove quench oil residue before tempering (oil quench path only)`
- Check: `HPGQ path: skip to temper`

*Box 8 -- Temper:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Temper`
- Parameters:
```
300--375 F (149--191 C)
2 hours minimum
Sub-zero -100 to -120 F if RA spec
```
- Purpose: `Relieve quench stress; improve toughness; sub-zero converts retained austenite`
- Check: `Double temper for aerospace 9310 applications`

*Box 9 -- Inspection & QA:*
- Badge: `STAGE 9`, fill `#27AE60`
- Name: `Inspection & QA`
- Parameters:
```
ECD to 50 HRC (ASTM E384)
Surface: 58--63 HRC
No IGO (key LPC advantage)
```
- Purpose: `Verify case depth, hardness, and microstructure; IGO inspection step eliminated`
- Check: `Check for soot deposits, free carbides, RA`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.3". Same format as Poster #559.

| Swatch | Label |
|---|---|
| `#2EC4B6` | `Preparation & Vacuum` |
| `#E8A020` | `Heat` |
| `#27AE60` | `Core Process & QA` |
| `#E05C5C` | `Critical / Hazard` |
| `#C8D0D8` | `Equipment Reference` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- 9-Row Parameter Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Stage (3.0") | Key Action (5.0") | Temperature (3.5") | Time (3.0") | Atmosphere/Media (4.5") | Key Control (4.0")

| Stage | Key Action | Temp | Time | Atmosphere/Media | Key Control |
|---|---|---|---|---|---|
| 1. Pre-Clean | Solvent wash, dry completely | Ambient | -- | -- | Zero moisture |
| 2. Load | CFC/ceramic fixtures | Ambient | -- | -- | No steel fixtures |
| 3. Evacuate | Pump to hard vacuum | Ambient | 15--45 min | Vacuum (<0.1 mbar) | Leak rate <5 microns/hr |
| 4. Heat | Ramp under vacuum | 1700--1850 F | 1--3 hr | Vacuum | Uniformity per AMS 2750 |
| 5. Boost/Diffuse | Acetylene pulse cycles | 1700--1850 F | 1--8 hr (per ECD) | C2H2 at 5--15 mbar | Recipe simulation |
| 6. Quench | HPGQ or oil | N2/He: ambient->150 F | Minutes | N2 10--20 bar / He 15--20 bar | Interlock verified |
| 7. Wash | Oil removal (oil path only) | Ambient--160 F | 5--15 min | Alkaline wash | HPGQ: skip this step |
| 8. Temper | Stress relief | 300--375 F | 2 hr min | Air or N2 | Per AMS 2759/7 |
| 9. Inspect | ECD, hardness, micro | Ambient | -- | -- | No IGO to check |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Stage names: Inter Medium, 12 pt.

---

### ZONE 4 -- LPC vs. Gas Carburizing

**Section label:** `VACUUM VS. GAS CARBURIZING -- WHY CHOOSE LPC?` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- Two-column comparison (Y: 22.9" to 28.3")**

*Left -- LPC Advantages (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `LPC ADVANTAGES` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`):
```
- ZERO IGO -- eliminates a major rejection cause
  and reduces grinding stock requirement
- Clean, bright surface finish -- no oxidation
- Higher temperature possible (1800--1900 F)
  = 30--50% shorter cycle times
- HPGQ reduces distortion 30--50% vs. oil
- No CO exposure -- major safety advantage
- No endothermic generator to maintain
- Excellent for blind holes and deep bores
  (low-pressure gas penetrates better)
- Computer-controlled recipes (SimVac, DANTE)
  = precise, repeatable carbon profiles
- Handles high-Cr steels (M50NiL) better
  than gas (no Cr-oxide passivation)
```

*Right -- LPC Limitations (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#E8A020`.

Title: `LPC LIMITATIONS` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`):
```
- Higher capital cost (vacuum furnace
  vs. atmosphere furnace)
- HPGQ may not quench thick sections
  in lean-alloy steels (>1.5" / 38 mm)
- No real-time carbon potential measurement
  (controlled by recipe, not O2 probe)
- Soot management -- acetylene can deposit
  carbon black if boost parameters are wrong
- Smaller load sizes in single-chamber systems
  (multi-chamber helps but adds cost)
- CFC fixtures are expensive (but lighter
  and longer-lived than alloy steel)
- Acetylene handling requirements (explosive
  gas; 15 psig max line pressure)
- Requires process simulation software
  expertise to develop recipes
```

Bottom callout (Y: 27.8" to 28.3"):
- Pill bar, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- `LPC is to gas carburizing what CNC is to manual machining -- higher precision, higher investment, higher capability.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON LPC FAILURES` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Four cards in a single row. Gap: 0.33".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SOOT DEPOSITS | Excessive boost pressure/time; propane instead of acetylene | Reduce boost pressure; switch to C2H2; verify mass flow cal |
| 2 | 6.33" | NON-UNIFORM CASE | Gas flow pattern in chamber; load too dense | Optimize loading pattern; increase diffuse time between boosts |
| 3 | 12.16" | FREE CARBIDES | Too many boosts without sufficient diffuse | Extend diffuse phases; re-run simulation |
| 4 | 18.0" | GRAIN GROWTH | Temperature above 1900 F without microalloy control | Reduce temp; use vacuum-grade fine-grain steel |

Each card: Rounded rect W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.
Problem: Barlow SemiBold 16 pt `#E05C5C`.
Cause: Inter Regular 12 pt `#F0EDE8`.
Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 6 -- Footer Band

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center.

> This poster is an educational reference tool. Process parameters shown are typical industry values for vacuum (low pressure) carburizing with acetylene. Specific equipment settings, recipe parameters, and acceptance criteria vary by specification and part design. Consult AMS 2759/7, your furnace OEM, and process simulation software documentation.

**Poster title:** `Vacuum Carburizing (LPC) -- Process Flow`
**Series name:** `Plating Posters Inc -- Metal Finishing Reference Series`
**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Process Flow | Section label, nine flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 9-row table |
| Zone 4 - LPC vs Gas | Section label, advantages/limitations panels, callout bar |
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
| `Vacuum Carburizing LPC Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Vacuum Carburizing LPC Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Vacuum Carburizing LPC Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Vacuum Carburizing LPC Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Vacuum Carburizing LPC Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Vacuum Carburizing LPC Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This poster mirrors the structure of DH-01's Process Flow (#559) for series consistency, but the content and feel are distinctly "high-tech." Teal gets more prominence because vacuum carburizing is the precision/aerospace method. The LPC vs. Gas comparison panel is the unique Zone 4 content for this cluster -- it's the question every heat treater asks ("why would I buy a vacuum furnace?") and deserves a clear, honest answer that covers both sides.

The acetylene pulsing concept is unfamiliar to many gas carburizing operators, so the flow boxes need to make the boost/diffuse cycle logic crystal clear. The "recipe simulation" concept (SimVac, DANTE) is a genuine differentiator that separates LPC from the empirical art of gas carburizing.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #568 -- Construction Workup v1.0*
*2026-04-26*
