---
Project: Plating Posters Inc
Poster Number: 589
Title: "Gas Nitriding -- Loading & Fixturing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.4)"
Technical Source: Loading and fixturing requirements for gas nitriding. Key considerations include long cycle times (40-90+ hours), fixture creep resistance, vertical hanging preference, and thermocouple placement for extended holds.
Process Scope: Gas nitriding -- loading and fixturing (Stage 4 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - Loading
  - Fixturing
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #589 -- Construction Workup
## Gas Nitriding -- Loading & Fixturing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers loading and fixturing for gas nitriding. The defining challenge is TIME -- gas nitriding cycles run 15-90+ hours. Fixtures must support parts without creep or deformation for days at temperature. Vertical hanging is preferred to prevent contact marks and ensure uniform gas flow.

Design philosophy: hero diagram showing proper vs. improper loading arrangements, a fixture material comparison table, thermocouple placement guidelines, and a spacing/orientation reference panel.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, table rows, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Loading best practices panel (Block B -- HERO):** Four callout cards showing proper loading principles.

2. **Fixture material table (Block C):** Comparison of alloy fixture materials for long-duration nitriding.

3. **Thermocouple placement panel (Block D):** Guidelines for TC positioning during extended cycles.

4. **Common loading errors strip (Block E):** Four common mistakes with corrections.

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
- 15.0" -- Zone 2/Zone 3 boundary
- 21.0" -- Zone 3/Zone 4 boundary
- 27.0" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- LOADING BEST PRACTICES / HERO (2.9"--15.0" / ~12.1" tall)
  Block B: Four loading principle cards (2x2 grid)

ZONE 3 -- FIXTURE MATERIALS (15.0"--21.0" / ~6.0" tall)
  Block C: Fixture material comparison table

ZONE 4 -- THERMOCOUPLE PLACEMENT (21.0"--27.0" / ~6.0" tall)
  Block D: TC placement guidelines for extended cycles

ZONE 5 -- COMMON LOADING ERRORS (27.0"--32.5" / ~5.5" tall)
  Block E: Four common mistakes with corrections

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
- Color: `#2EC4B6` (Teal)
- Text:

> Loading & Fixturing -- Orientation, Spacing & Fixture Selection

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Fixtures must survive 40--90 hours at temperature without creep. Hang parts vertically. Space for gas flow. Plan for the long haul.

---

### ZONE 2 -- Loading Best Practices (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.0" (~12.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center
- Text:

> LOADING PRINCIPLES -- THE LONG-CYCLE CHALLENGE

---

**BLOCK B -- Four Loading Principle Cards (2x2 Grid)**

Y: 3.8" to 14.8". Two columns, two rows. Gap: 0.4".

Each card: Rounded rect, W: 11.1", H: 5.1", fill `#1E2435`, radius 8, top accent 4 pt.

**Row 1 (Y: 3.8" to 8.9"):**

*Card 1 -- Vertical Hanging (X: 0.5"):*
- Top accent: `#27AE60` (Emerald)
- Title: `HANG PARTS VERTICALLY` -- Barlow SemiBold, 22 pt, `#27AE60`
- Subtitle: `PREFERRED ORIENTATION` -- Inter Medium, 12 pt, `#27AE60`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Hang parts from hooks, wires, or fixtures
whenever possible. Vertical orientation:

- Prevents contact marks (soft spots)
- Maximizes gas flow over all surfaces
- Eliminates gravity-induced flat spots
- Allows uniform ammonia access to 360 degrees

For shafts: hang from one end
For rings/discs: hang from internal supports
```

*Card 2 -- Spacing Requirements (X: 11.9"):*
- Top accent: `#E8A020` (Amber)
- Title: `MAINTAIN ADEQUATE SPACING` -- Barlow SemiBold, 22 pt, `#E8A020`

Content:
```
Minimum spacing between parts:
0.5--1.0 in (12.7--25.4 mm)

Gas nitriding relies on NH3 flowing over
every surface. Inadequate spacing causes:

- Gas starvation at contact points
- Uneven case depth
- Soft spots where parts touch

Dense loads require LONGER cycles
(same case depth needs more time)
```

Key data (JetBrains Mono, 13 pt, `#E8A020`):
```
0.5 in MINIMUM -- 1.0 in PREFERRED
```

**Row 2 (Y: 9.5" to 14.6"):**

*Card 3 -- Fixture Creep Resistance (X: 0.5"):*
- Top accent: `#E05C5C` (Coral)
- Title: `FIXTURE CREEP -- THE HIDDEN RISK` -- Barlow SemiBold, 22 pt, `#E05C5C`

Content:
```
Gas nitriding cycles run 15--90+ HOURS
at 925--1050 F. This is orders of magnitude
longer than carburizing (2--8 hours).

Fixture creep (slow deformation under load
at elevated temperature) is a real risk:

- Parts sag or shift during the cycle
- Fixture trays bow under sustained load
- Contact points develop where none existed

Use creep-resistant alloys and conservative
load weights. Inspect fixtures regularly.
```

*Card 4 -- Load Thermocouples (X: 11.9"):*
- Top accent: `#2EC4B6` (Teal)
- Title: `THERMOCOUPLE PLACEMENT` -- Barlow SemiBold, 22 pt, `#2EC4B6`

Content:
```
Load TC at center of heaviest section
or densest part of the load.

For large loads, use MULTIPLE TCs
to verify temperature uniformity.

Long cycle = long time for gradients
to develop if circulation is poor.

Per AMS 2750: load TC must be within
the qualified work zone and representative
of actual part temperature.
```

---

### ZONE 3 -- Fixture Materials

**Dimensions:** Y: 15.0" to 21.0" (~6.0" tall).

---

**Section label:**
- Centered. Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> FIXTURE MATERIAL SELECTION -- CREEP RESISTANCE IS KEY

---

**BLOCK C -- Fixture Material Table**

Y: 15.9" to 20.8". Column widths (23.0" total):
- Material (4.5") | Max Service Temp (3.5") | Creep Resistance (4.0") | Notes (5.5") | Suitability (5.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Material | Max Temp | Creep Resistance | Notes | Suitability |
|---|---|---|---|---|
| RA 330 (HT alloy) | 2100 F | Excellent | Standard heat treat fixture alloy | Excellent |
| Inconel 601 | 2150 F | Excellent | Ni-Cr-Al alloy; oxidation resistant | Excellent |
| HU (309) cast | 2000 F | Good | Common casting alloy for trays | Good |
| HK-40 cast | 2050 F | Good | Higher strength than HU | Good |
| Low-carbon steel | 1200 F | Poor | Adequate for short cycles only | Marginal for nitriding |
| Stainless 304/316 | 1600 F | Moderate | Will nitride at surface over time | Acceptable (short term) |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Material names: Inter Medium, 12 pt.

Note below table:
- Inter Medium, 13 pt, `#E8A020`
- Text: `Fixtures absorb nitrogen slowly at nitriding temperatures -- less aggressively than carbon absorption during carburizing, but replace periodically`

---

### ZONE 4 -- Thermocouple Placement Guidelines

**Dimensions:** Y: 21.0" to 27.0" (~6.0" tall).

---

**Section label:**
- Centered. Y: 21.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> THERMOCOUPLE PLACEMENT -- ACCURACY OVER 40--90 HOURS

---

**BLOCK D -- TC Placement Panel**

Y: 21.9" to 26.8". Two side-by-side panels.

**Left -- Placement Rules (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.7", fill `#1E2435`, radius 8
- Left accent: 4 pt `#2EC4B6`
- Title: `WHERE TO PLACE THERMOCOUPLES` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
1. At the COLDEST point in the load
   (center of densest section)

2. At the HEAVIEST part (largest
   thermal mass = slowest to heat)

3. Multiple TCs for loads > 500 lbs
   to verify uniformity across the load

4. Per AMS 2750: TC must be in the
   qualified work zone

5. Record temperature continuously
   for the FULL cycle (15--90 hours)
```

**Right -- Extended Cycle Considerations (X: 12.5", W: 11.0"):**
- Rounded rect, H: 4.7", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E8A020`
- Title: `LONG-CYCLE CONCERNS` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
Gas nitriding has the LONGEST cycles
in heat treatment. This amplifies
every small error:

- A 2 F temperature error sustained
  for 90 hours affects case depth

- TC drift over multi-day cycles must
  be accounted for in SAT intervals

- Chart recorder must have sufficient
  paper/memory for full cycle duration

- Power interruptions during a 3-day
  cycle: document and evaluate impact
```

---

### ZONE 5 -- Common Loading Errors

**Dimensions:** Y: 27.0" to 32.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 27.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> COMMON LOADING ERRORS -- AVOID THESE

---

**BLOCK E -- Four Error Cards**

Y: 27.9" to 32.3". Four cards in a single row. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 4.2", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Error | Consequence | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PARTS TOUCHING | Soft spots at every contact point after 40+ hours | Minimum 0.5 in spacing; hang vertically |
| 2 | 6.33" | OVERLOADED TRAYS | Fixture creep; parts sag mid-cycle; new contact points form | Reduce load weight; use creep-resistant alloys |
| 3 | 12.16" | POOR GAS CIRCULATION | Uneven case depth across the load | Space parts uniformly; verify fan operation |
| 4 | 18.0" | TC IN WRONG LOCATION | Temperature reading not representative; case depth errors | Place at coldest/heaviest point; use multiple TCs |

Interior per card:
- Error: Barlow SemiBold, 15 pt, `#E05C5C`
- Consequence: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Loading and fixturing requirements shown are typical for gas nitriding per AMS 2759/6D and AMS 2750. Specific fixture designs, load configurations, and thermocouple requirements vary by furnace type and specification. Consult your process engineer.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Loading & Fixturing

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
| Zone 2 - Loading Principles | Section label, four principle cards |
| Zone 3 - Fixture Materials | Section label, material comparison table |
| Zone 4 - TC Placement | Section label, two TC guideline panels |
| Zone 5 - Common Errors | Section label, four error cards |
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
| `Gas Nitriding Loading Fixturing -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Loading Fixturing -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Loading Fixturing -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Loading Fixturing -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Loading Fixturing -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Loading Fixturing -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The long cycle time is the recurring theme. Every loading and fixturing decision in gas nitriding is shaped by the fact that parts sit at 925-1050 F for 15-90 HOURS. A small error that would be inconsequential in a 4-hour carburizing cycle becomes catastrophic over 3+ days. Emphasize this throughout.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #589 -- Construction Workup v1.0*
*2026-04-26*
