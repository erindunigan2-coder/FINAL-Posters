---
Project: Plating Posters Inc
Poster Number: 590
Title: "Gas Nitriding -- Furnace / System Setup"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.5)"
Technical Source: Furnace types and atmosphere system setup for gas nitriding. Covers pit (vertical retort), bell, and horizontal retort furnaces. Anhydrous ammonia supply, flow control, and exhaust systems. AMS 2750 compliance for temperature uniformity.
Process Scope: Gas nitriding -- furnace and system setup (Stage 5 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - FurnaceSetup
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #590 -- Construction Workup
## Gas Nitriding -- Furnace / System Setup

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers furnace types and atmosphere system configuration for gas nitriding. Pit furnaces (vertical retorts) are the most common -- parts hang vertically for uniform gas flow. The atmosphere is pure anhydrous ammonia from cylinders or bulk tank. No endothermic gas generator, no enrichment gas, no carbon potential probe. Simpler atmosphere than carburizing, but the ammonia supply, flow control, and exhaust handling need proper setup.

Design philosophy: furnace type comparison as the hero (pit vs. bell vs. horizontal retort), an ammonia supply system schematic described in text, AMS 2750 temperature uniformity requirements, and an atmosphere system component checklist.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Furnace type comparison (Block B -- HERO):** Three large cards comparing pit, bell, and horizontal retort furnaces.

2. **AMS 2750 requirements table (Block C):** Temperature uniformity class requirements for nitriding.

3. **Atmosphere system components (Block D):** Component-by-component breakdown of the ammonia supply and exhaust system.

4. **Key setup checks strip (Block E):** Four pre-cycle verification points.

5. **4 pt left-border accents on callout boxes.**

6. **Global Colors / swatch remap for Light edition.**

7. **Print size -- 24x36".**

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
- **JetBrains Mono Regular** -- all parameter data, version number

If JetBrains Mono upload fails, substitute **Courier Prime**.

### Step 4 -- Set up color palette

Same as Poster #586 (series standard).

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 14.5" -- Zone 2/Zone 3 boundary
- 19.5" -- Zone 3/Zone 4 boundary
- 27.5" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- FURNACE TYPE COMPARISON / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Three furnace type cards

ZONE 3 -- AMS 2750 REQUIREMENTS (14.5"--19.5" / ~5.0" tall)
  Block C: Temperature uniformity class table + instrumentation notes

ZONE 4 -- ATMOSPHERE SYSTEM COMPONENTS (19.5"--27.5" / ~8.0" tall)
  Block D: NH3 supply system component breakdown

ZONE 5 -- PRE-CYCLE SETUP CHECKS (27.5"--32.5" / ~5.0" tall)
  Block E: Four verification cards

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block F: Disclaimer + poster title + series name + logo placeholder + version
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
- Size: 88 pt
- Color: `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> GAS NITRIDING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.5"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 36 pt
- Color: `#E8A020` (Amber)
- Text:

> Furnace / System Setup -- Furnace Types, Atmosphere & Pyrometry

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Pit retorts dominate. Ammonia is the only process gas. No endo generator, no enrichment gas -- just NH3, a good fan, and a burn-off pilot.

---

### ZONE 2 -- Furnace Type Comparison (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 14.5" (~11.6" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> FURNACE TYPES FOR GAS NITRIDING

---

**BLOCK B -- Three Furnace Type Cards**

Y: 3.8" to 14.3". Three cards in a row. Gap: 0.35".

Each card: Rounded rect, W: 7.3", H: 10.3", fill `#1E2435`, radius 8, top accent 4 pt.

*Card 1 -- Pit Furnace / Vertical Retort (X: 0.5"):*
- Top accent: `#27AE60` (Emerald)
- Title: `PIT FURNACE (VERTICAL RETORT)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `MOST COMMON` -- Inter Medium, 14 pt, `#27AE60`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 170%):
```
Configuration:
  Vertical retort sunk into floor
  Parts hang from top of retort
  Retort sealed with lid and gasket
  Internal fan circulates ammonia

Advantages:
  - Parts hang vertically (best orientation)
  - Gravity assists uniform gas flow
  - Easy to load from overhead crane
  - Natural convection supplements fan

Load size:
  Diameter 24--72 in (600--1800 mm)
  Height 36--120 in (900--3000 mm)

Best for:
  Shafts, gears, dies, landing gear
```

*Card 2 -- Bell Furnace (X: 8.2"):*
- Top accent: `#E8A020` (Amber)
- Title: `BELL FURNACE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `INVERTED PIT DESIGN` -- Inter Medium, 14 pt, `#E8A020`

Content:
```
Configuration:
  Parts loaded on base plate
  Bell (dome) lowered over parts
  Sealed at base with sand seal or gasket
  Atmosphere circulated by internal fan

Advantages:
  - Easy floor-level loading
  - Good for heavy/large components
  - Multiple bases allow load/unload
    while another base is processing

Load size:
  Similar to pit furnaces
  Width limited by bell diameter

Best for:
  Large dies, mold components,
  heavy industrial parts
```

*Card 3 -- Horizontal Retort (X: 15.9"):*
- Top accent: `#2EC4B6` (Teal)
- Title: `HORIZONTAL BATCH RETORT` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `TRAY-LOADED` -- Inter Medium, 14 pt, `#2EC4B6`

Content:
```
Configuration:
  Horizontal tube or box retort
  Parts loaded on trays/baskets
  Pushed into retort on rails
  Door sealed; atmosphere introduced

Advantages:
  - Familiar loading (like batch Q&T)
  - Good for mixed small parts
  - Multiple retorts can share
    one control system

Limitations:
  - Parts lay flat (contact risk)
  - Gas circulation less uniform
    than vertical retort

Best for:
  Small to medium parts,
  job shop environments
```

Note below cards:
- Inter Medium, 14 pt, `#F0EDE8` at 60%
- Text: `Continuous furnaces are rare for gas nitriding due to extremely long cycle times (15--90+ hours). Batch processing dominates.`

---

### ZONE 3 -- AMS 2750 Requirements

**Dimensions:** Y: 14.5" to 19.5" (~5.0" tall).

---

**Section label:**
- Centered. Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> AMS 2750 PYROMETRY -- TEMPERATURE UNIFORMITY FOR NITRIDING

---

**BLOCK C -- Temperature Uniformity Table + Notes**

Y: 15.4" to 19.3".

**Left -- Class Table (X: 0.5", W: 11.0"):**
- Rounded rect, H: 3.7", fill `#1E2435`, radius 8

Table inside panel:

| Class | Tolerance | Typical Use |
|---|---|---|
| 2 | +/-6 C (+/-10 F) | Precision nitriding (aerospace) |
| 3 | +/-8 C (+/-15 F) | Standard nitriding (most applications) |
| 4 | +/-10 C (+/-20 F) | General nitriding (non-critical) |

Header: Barlow SemiBold, 13 pt, `#F0EDE8` on `#3A4055`.
Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

Note: `Nitriding furnaces are typically Class 2 or Class 3` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Instrumentation Notes (X: 12.5", W: 11.0"):**
- Rounded rect, H: 3.7", fill `#1E2435`, radius 8
- Left accent: 4 pt `#2EC4B6`
- Title: `INSTRUMENTATION REQUIREMENTS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 170%):
```
- Type A or B instrumentation per AMS 2750
- Recording instrument mandatory (full cycle)
- SAT (System Accuracy Test): per schedule
- TUS (Temp Uniformity Survey): quarterly or
  semiannual depending on class and history
- Load TC required per specification
- Base metal TCs (Type J, K, N) standard
  for nitriding temperature range
```

---

### ZONE 4 -- Atmosphere System Components

**Dimensions:** Y: 19.5" to 27.5" (~8.0" tall).

---

**Section label:**
- Centered. Y: 19.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> ATMOSPHERE SYSTEM -- AMMONIA SUPPLY & EXHAUST

---

**BLOCK D -- Component Breakdown**

Y: 20.4" to 27.3". Six component cards in a 3x2 grid. Gap: 0.3".

Each card: Rounded rect, W: 7.3", H: 3.1", fill `#1E2435`, radius 6, left accent 4 pt `#E8A020`.

**Row 1 (Y: 20.4" to 23.5"):**

*Card 1 -- NH3 Supply (X: 0.5"):*
- Title: `AMMONIA SUPPLY` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Anhydrous NH3 from cylinders (150 lb) or bulk tank. Regulator reduces to line pressure. Store upright, chained, away from heat. No copper fittings.` -- Inter Regular, 12 pt, `#F0EDE8`

*Card 2 -- Flow Control (X: 8.15"):*
- Title: `FLOW CONTROL` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Rotameter or mass flow controller. Flow rate set to maintain target dissociation rate (15--85% depending on stage). Adjusted based on furnace volume and load size.` -- Inter Regular, 12 pt, `#F0EDE8`

*Card 3 -- Dissociator (X: 15.8"):*
- Title: `DISSOCIATOR (OPTIONAL)` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Pre-dissociates a portion of NH3 before it enters the furnace. Used to fine-tune nitriding potential (KN) in controlled-potential systems per AMS 2759/10.` -- Inter Regular, 12 pt, `#F0EDE8`

**Row 2 (Y: 23.9" to 27.0"):**

*Card 4 -- Circulation Fan (X: 0.5"):*
- Title: `INTERNAL FAN` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Circulates ammonia throughout the retort. Critical for uniform case depth. Fan failure = gas starvation at load center = uneven case. Verify operation before every cycle.` -- Inter Regular, 12 pt, `#F0EDE8`

*Card 5 -- Exhaust System (X: 8.15"):*
- Title: `EXHAUST / BURN-OFF` -- Barlow SemiBold, 17 pt, `#E05C5C`
- Content: `Dissociated ammonia exits as H2 + N2 + unreacted NH3. BURN-OFF PILOT at exhaust is MANDATORY. Combusts H2 and remaining NH3 to prevent accumulation. Pilot failure = explosion risk.` -- Inter Regular, 12 pt, `#F0EDE8`
- Left accent color: `#E05C5C` (Coral -- safety emphasis)

*Card 6 -- Dissociation Monitoring (X: 15.8"):*
- Title: `DISSOCIATION MEASUREMENT` -- Barlow SemiBold, 17 pt, `#E8A020`
- Content: `Burette (volumetric) method measures % NH3 dissociation at exhaust. Automated systems use hydrogen sensors + NH3 analyzers to calculate KN in real time.` -- Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 5 -- Pre-Cycle Setup Checks

**Dimensions:** Y: 27.5" to 32.5" (~5.0" tall).

---

**Section label:**
- Centered. Y: 27.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> PRE-CYCLE SETUP VERIFICATION -- CHECK BEFORE EVERY RUN

---

**BLOCK E -- Four Verification Cards**

Y: 28.4" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 3.7", fill `#1E2435`, radius 6, left accent 0.06" `#27AE60`.

| Card | X | Check | Detail |
|---|---|---|---|
| 1 | 0.5" | BURN-OFF PILOT | Verify lit and functioning. Check flame sensor interlock. NEVER introduce NH3 with pilot out. |
| 2 | 6.33" | SEAL INTEGRITY | Retort lid/door gasket sealed. Leak check complete. Air infiltration during 40+ hr cycle oxidizes parts and dilutes atmosphere. |
| 3 | 12.16" | FAN OPERATION | Internal circulation fan running. Verify amperage. Fan failure mid-cycle causes uneven case and may not be detected for hours. |
| 4 | 18.0" | NH3 SUPPLY | Sufficient ammonia for full cycle (calculate total flow x hours). Running out mid-cycle means starting over. Verify cylinder manifold or bulk level. |

Interior per card:
- Check title: Barlow SemiBold, 16 pt, `#27AE60`
- Detail: Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Furnace configurations and atmosphere system designs vary by manufacturer and application. AMS 2750 requirements apply to aerospace heat treatment; other industries may follow different pyrometry standards. Consult your equipment supplier and applicable specifications.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Furnace / System Setup

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
| Zone 2 - Furnace Types | Section label, three furnace type cards |
| Zone 3 - AMS 2750 | Section label, class table, instrumentation notes |
| Zone 4 - Atmosphere System | Section label, six component cards |
| Zone 5 - Setup Checks | Section label, four verification cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Panel fills |
| `#252B3D` | `#E8E8F0` | Alternate rows |
| `#0D1020` | `#1A1F2E` | Footer background |
| `#E8A020` | `#C8860A` | Amber accents |
| `#2EC4B6` | `#1A8C82` | Teal accents |
| `#27AE60` | `#1E7A47` | Emerald accents |
| `#E05C5C` | `#B83E3E` | Coral accents |
| `#3A4055` | `#D0D4DE` | Table headers, dividers |
| `#C8D0D8` | `#C8D0D8` | Bright Silver -- **unchanged** |

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Gas Nitriding Furnace System Setup -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Furnace System Setup -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Furnace System Setup -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Furnace System Setup -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Furnace System Setup -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Furnace System Setup -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

Gas nitriding has the simplest atmosphere of any diffusion heat treatment: pure ammonia, nothing else. No endothermic generator, no carbon potential control, no oxygen probe. The simplicity is deceptive -- the process control is in the dissociation rate, and the exhaust handling (burn-off pilot) is a genuine safety requirement.

The pit furnace's dominance is directly tied to the vertical hanging preference. When you need uniform nitrogen access to every surface for 40-90 hours, gravity-assisted vertical hanging in a retort is the natural solution.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #590 -- Construction Workup v1.0*
*2026-04-26*
