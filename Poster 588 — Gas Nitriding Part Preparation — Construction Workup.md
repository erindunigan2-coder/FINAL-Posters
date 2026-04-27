---
Project: Plating Posters Inc
Poster Number: 588
Title: "Gas Nitriding -- Part Preparation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 4: Gas Nitriding, Section 4.3)"
Technical Source: Part preparation requirements for gas nitriding. Covers critical pre-heat-treatment, surface preparation, and masking for selective nitriding. Key distinction from carburizing: parts MUST be in final Q&T condition before nitriding. Masking uses tin or nickel electroplate (NOT copper).
Process Scope: Gas nitriding -- part preparation (Stage 3 deep-dive)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - GasNitriding
  - PartPreparation
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #588 -- Construction Workup
## Gas Nitriding -- Part Preparation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the most critical preparation step in all of heat treatment: getting parts ready for gas nitriding. The #1 rule is that parts must already be quenched and tempered to their final core hardness BEFORE nitriding. The temper temperature must exceed the nitriding temperature by at least 50 F. Get this wrong and the core softens during the 40-90 hour cycle.

Design philosophy: hero panel explaining the Q&T prerequisite with a temperature relationship diagram, a surface preparation checklist, a masking methods comparison (tin vs. nickel vs. copper -- copper does NOT work for nitriding), and a contaminant effects table.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

- Text boxes with precise font, size, weight, color, and spacing control
- Solid-color rectangles and rounded rectangles for panels, checklist boxes, and accent borders
- Color fills set to exact hex values
- Background page color set to exact hex
- Export at print-quality PDF (300 DPI equivalent via print export)

### Limitations to Flag

1. **Pre-heat-treatment panel (Block B -- HERO):** Large callout explaining the Q&T requirement with a temperature relationship diagram showing temper temp > nitride temp + 50 F.

2. **Surface preparation checklist (Block D):** Vertical list of surface condition requirements with pass/fail indicators.

3. **Masking comparison (Block E):** Three-column comparison of tin, nickel, and copper stop-off methods.

4. **Contaminant effects table (Block C):** Table showing what happens when specific contaminants are present.

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

| Color Name | Hex | Primary Use |
|---|---|---|
| Gunmetal Dark | `#1A1F2E` | Background (Dark edition) |
| Warm White | `#F0EDE8` | All primary text (Dark edition) |
| Amber | `#E8A020` | Temperature references, warning highlights |
| Teal | `#2EC4B6` | Preparation steps, positive actions |
| Emerald | `#27AE60` | Correct procedures, pass indicators |
| Coral | `#E05C5C` | Problems, fail indicators, contaminant effects |
| Mid Slate | `#3A4055` | Table headers, dividers |
| Deep Navy | `#0D1020` | Footer band background |
| Dark Callout | `#1E2435` | Panel fills |
| Alt Row | `#252B3D` | Alternating table rows |
| Bright Silver | `#C8D0D8` | Neutral metallic accents |

### Step 5 -- Set ruler guides

**Vertical guides (from left edge):**
- 0.5" -- left safe zone margin
- 23.5" -- right safe zone margin

**Horizontal guides (from top edge):**
- 0.5" -- top safe zone margin
- 2.9" -- Zone 1/Zone 2 boundary
- 13.0" -- Zone 2/Zone 3 boundary
- 18.5" -- Zone 3/Zone 4 boundary
- 25.0" -- Zone 4/Zone 5 boundary
- 32.5" -- Zone 5/Zone 6 boundary
- 35.5" -- bottom safe zone margin

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PRE-HEAT-TREAT REQUIREMENT / HERO (2.9"--13.0" / ~10.1" tall)
  Block B: Q&T prerequisite panel with temperature relationship

ZONE 3 -- CONTAMINANT EFFECTS TABLE (13.0"--18.5" / ~5.5" tall)
  Block C: What happens when contaminants are present

ZONE 4 -- SURFACE PREPARATION CHECKLIST (18.5"--25.0" / ~6.5" tall)
  Block D: Surface condition requirements

ZONE 5 -- MASKING COMPARISON (25.0"--32.5" / ~7.5" tall)
  Block E: Tin vs. nickel vs. copper stop-off comparison

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

> Part Preparation -- Pre-Treatment, Surface Condition & Masking

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.2"
- Width: 23.0"
- Font: Barlow SemiBold
- Size: 20 pt
- Color: `#F0EDE8` at 65%
- Text:

> Parts must be quenched and tempered BEFORE nitriding. Surface must be chemically clean. Masking uses tin or nickel -- never copper.

---

### ZONE 2 -- Pre-Heat-Treat Requirement (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 13.0" (~10.1" tall).

---

**Section label:**
- Centered horizontally. Y: 3.1"
- Font: Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center
- Text:

> CRITICAL: PRE-HEAT-TREATMENT IS MANDATORY

---

**BLOCK B -- Q&T Prerequisite Panel**

Y: 3.8" to 12.8".

**Main Panel:**
- Rounded rect, X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8
- Left accent: 4 pt `#E05C5C`

Title: `QUENCH & TEMPER BEFORE NITRIDING -- NON-NEGOTIABLE` -- Barlow SemiBold, 24 pt, `#E05C5C`

Content (Inter Regular, 15 pt, `#F0EDE8`, line height 170%):
```
Gas nitriding does not create its own core hardness. The process occurs entirely
below the lower critical temperature (Ac1) -- no austenite forms, no quench happens.
The core retains whatever hardness it had going in.

If the part is in the annealed or normalized condition, the core will be SOFT
after nitriding -- even though the surface is extremely hard. This is usually wrong.
```

**Temperature Rule Box:**
- Rounded rect, X: 0.5", Y: 8.7", W: 23.0", H: 3.8", fill `#252B3D`, radius 8

Title: `THE 50 F RULE` -- Barlow Condensed ExtraBold, 28 pt, `#E8A020`

Content (two columns):

Left column (X: 1.0", W: 10.5"):
- Inter Medium, 16 pt, `#F0EDE8`, line height 170%
```
TEMPER TEMPERATURE must exceed
NITRIDING TEMPERATURE by at least
50 F (28 C).

If this rule is violated, the core
WILL SOFTEN during the 15--90 hour
nitriding cycle.
```

Right column (X: 12.5", W: 10.5"):
- JetBrains Mono Regular, 15 pt, `#F0EDE8`
```
EXAMPLE:
  Nitriding at 975 F (524 C)
  Minimum temper: 1025 F (552 C)

EXAMPLE:
  Nitriding at 1050 F (566 C)
  Minimum temper: 1100 F (593 C)
```

Bottom note:
- Inter Medium, 14 pt, `#E8A020`
- Text: `Stress relief after rough machining is recommended -- prevents distortion during the long nitriding cycle`

---

### ZONE 3 -- Contaminant Effects Table

**Dimensions:** Y: 13.0" to 18.5" (~5.5" tall).

---

**Section label:**
- Centered. Y: 13.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> SURFACE CONTAMINANTS -- WHAT GOES WRONG

---

**BLOCK C -- Contaminant Effects Table**

Y: 13.9" to 18.3". Column widths (23.0" total):
- Contaminant (5.0") | Effect on Nitriding (8.0") | How to Remove (10.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Contaminant | Effect on Nitriding | How to Remove |
|---|---|---|
| Cutting fluid (sulfur-bearing) | Poisons nitriding reaction; soft spots | Solvent wash then alkaline clean |
| Fingerprint oils | Blocks N diffusion; visible soft spot pattern | Wear gloves; vapor degrease |
| Cr2O3 passive film | Blocks nitrogen on high-Cr steels (H13, stainless) | Light abrasive blast or chemical activation |
| Rust / iron oxide | Uneven nitrogen absorption; blotchy case | Pickle or abrasive clean |
| Paint / ink / markers | Complete N blockage at marked area | Solvent strip; verify removal |
| Residual plating chemicals | Contaminate furnace atmosphere | Thorough rinse and dry after plating |

Data: Inter Regular, 12 pt, `#F0EDE8`. Contaminant names: Inter Medium, 13 pt, `#E05C5C`.

---

### ZONE 4 -- Surface Preparation Checklist

**Dimensions:** Y: 18.5" to 25.0" (~6.5" tall).

---

**Section label:**
- Centered. Y: 18.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> SURFACE PREPARATION CHECKLIST

---

**BLOCK D -- Checklist Items**

Y: 19.4" to 24.8". Two columns of checklist items.

Each item: Rounded rect, W: 11.0", H: 2.4", fill `#1E2435`, radius 6, left accent 4 pt.

**Left Column (X: 0.5"):**

*Item 1 (Y: 19.4"):*
- Left accent: `#27AE60`
- Title: `VERIFY Q&T CONDITION` -- Barlow SemiBold, 18 pt, `#27AE60`
- Detail: `Confirm part has been quenched and tempered. Check hardness certificate. Temper temp must be documented and exceed nitriding temp + 50 F.` -- Inter Regular, 13 pt, `#F0EDE8`

*Item 2 (Y: 22.0"):*
- Left accent: `#27AE60`
- Title: `DEGREASE / SOLVENT CLEAN` -- Barlow SemiBold, 18 pt, `#27AE60`
- Detail: `Vapor degrease or solvent wash. Remove all machining oils, cutting fluids, and drawing compounds. Alkaline wash at 140--180 F as secondary clean.` -- Inter Regular, 13 pt, `#F0EDE8`

**Right Column (X: 12.5"):**

*Item 3 (Y: 19.4"):*
- Left accent: `#27AE60`
- Title: `ACTIVATE HIGH-Cr SURFACES` -- Barlow SemiBold, 18 pt, `#27AE60`
- Detail: `H13, 4340, stainless steels: light abrasive blast (glass bead) or chemical activation to break Cr2O3 passive film. Plain carbon steels do not need this step.` -- Inter Regular, 13 pt, `#F0EDE8`

*Item 4 (Y: 22.0"):*
- Left accent: `#E05C5C`
- Title: `HANDLE WITH GLOVES` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Detail: `After cleaning, handle all parts with clean cotton or nitrile gloves ONLY. A single fingerprint creates a visible soft spot after 40+ hours at temperature.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- Masking Comparison

**Dimensions:** Y: 25.0" to 32.5" (~7.5" tall).

---

**Section label:**
- Centered. Y: 25.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`

> MASKING FOR SELECTIVE NITRIDING -- METHOD COMPARISON

---

**BLOCK E -- Three-Column Masking Comparison**

Y: 25.9" to 32.3". Three cards side by side. Gap: 0.33".

*Card 1 -- Tin Electroplate (X: 0.5", W: 7.2"):*
- Rounded rect, H: 6.2", fill `#1E2435`, radius 8
- Top accent: 4 pt `#27AE60`
- Title: `TIN PLATE (Sn)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `MOST COMMON STOP-OFF` -- Inter Medium, 12 pt, `#27AE60`

Content (Inter Regular, 13 pt, `#F0EDE8`, line height 170%):
```
Thickness: 0.0003--0.0005 in
(7.6--12.7 micrometers)

Blocks nitrogen diffusion effectively

Most widely used stop-off for
gas nitriding

Readily available from any
electroplating shop
```

Verdict: `RECOMMENDED` -- Barlow SemiBold, 16 pt, `#27AE60`

*Card 2 -- Nickel Electroplate (X: 8.05", W: 7.2"):*
- Top accent: 4 pt `#2EC4B6`
- Title: `NICKEL PLATE (Ni)` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `EFFECTIVE ALTERNATIVE` -- Inter Medium, 12 pt, `#2EC4B6`

Content:
```
Thickness: 0.001 in (25 micrometers)

Also effective as nitrogen barrier

Thicker deposit required than tin

Higher cost per part than tin plate

Used when tin is not available
or not preferred
```

Verdict: `ACCEPTABLE` -- Barlow SemiBold, 16 pt, `#2EC4B6`

*Card 3 -- Copper Electroplate (X: 15.6", W: 7.2"):*
- Top accent: 4 pt `#E05C5C`
- Title: `COPPER PLATE (Cu)` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Subtitle: `DOES NOT WORK` -- Inter Medium, 12 pt, `#E05C5C`

Content:
```
Copper does NOT block nitrogen
diffusion (unlike carburizing
where Cu is the standard stop-off)

Nitrogen passes through copper
at nitriding temperatures

DO NOT USE copper plate as a
nitriding stop-off
```

Verdict: `NOT EFFECTIVE -- DO NOT USE` -- Barlow SemiBold, 16 pt, `#E05C5C`

---

### ZONE 6 -- Footer Band

**Dimensions:** Y: 32.5" to 36.0" (~3.5" tall).

**Footer background:** Rectangle, X: 0", Y: 32.5", W: 24.0", H: 3.5", fill `#0D1020`

**Disclaimer:** Inter Regular, 11 pt, `#F0EDE8` at 50%, Center. X: 0.5", Y: 32.8", W: 23.0"

> This poster is an educational reference tool. Part preparation requirements shown are typical for gas nitriding per AMS 2759/6D and AMS 2759/10A. Specific steel grades, masking requirements, and surface preparation methods vary by application. Consult your process engineer and applicable specifications.

**Poster title:** Barlow SemiBold, 16 pt, `#F0EDE8`. X: 0.5", Y: 33.5"

> Gas Nitriding -- Part Preparation

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
| Zone 2 - Pre-Heat-Treat | Section label, Q&T prerequisite panel, temperature rule box |
| Zone 3 - Contaminant Table | Section label, contaminant effects table |
| Zone 4 - Surface Checklist | Section label, four checklist items |
| Zone 5 - Masking Comparison | Section label, three masking method cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex | Notes |
|----------|-----------|-------|
| `#1A1F2E` | `#F5F4F0` | Background and all BG-colored elements |
| `#F0EDE8` | `#1A1F2E` | All primary text |
| `#1E2435` | `#ECEEF4` | Panel fills |
| `#252B3D` | `#E8E8F0` | Alternate rows, rule box |
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
| `Gas Nitriding Part Preparation -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Part Preparation -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Part Preparation -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Gas Nitriding Part Preparation -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Part Preparation -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Gas Nitriding Part Preparation -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

The copper-does-not-work-for-nitriding fact is one of the most common mistakes in the industry. People assume copper stop-off is universal because it works perfectly for carburizing. Give the "DO NOT USE" card maximum visual weight -- Coral accent, bold verdict.

The 50 F rule is the single most critical piece of information on this poster. If a shop forgets this, they ruin parts during a 40-90 hour cycle that cannot be interrupted and restarted.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #588 -- Construction Workup v1.0*
*2026-04-26*
