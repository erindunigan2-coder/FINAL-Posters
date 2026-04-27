---
Project: Plating Posters Inc
Poster Number: 32
Title: "Cleaning -- Zinc (Alkaline)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Alkaline soak cleaning for zinc plating line (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #32 -- Construction Workup
## Cleaning -- Zinc (Alkaline)

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 1 of the alkaline zinc process. This poster covers the soak cleaning tank -- the first and arguably most important step. "If the cleaning is wrong, everything downstream is wrong." The hero visual is a tank cross-section showing parts immersed with agitation arrows, temperature indicator, and soil removal dynamics.

---

## Part 1 -- Workflow Orientation

### Design Capabilities
- Text boxes, rounded rectangles, line elements, color fills -- all standard
- Tank cross-section diagram: a large rounded rectangle (tank body) with internal elements representing parts on a rack, agitation arrows (curved lines), temperature indicator bar, and soil particles lifting off parts

### Limitations to Flag
1. **Tank cross-section hero (Block B):** A rectangular "tank" shape with rounded corners, filled with a lighter shade to represent liquid. Internal elements: stylized parts hanging from a rack bar, wavy upward arrows for agitation/soil lift, a thermometer icon or temperature bar on the side. All buildable with basic shapes and lines.
2. **"Before/After" orientation strip (Block C):** A thin horizontal bar showing where this stage sits in the 8-stage sequence. Current stage highlighted, others dimmed.
3. **Full parameter table (Block D):** Single-stage deep dive -- more columns and rows than the summary in Poster #31.
4. **Common problems table (Block F):** 4--5 rows of cleaning-specific defects.
5. **Safety callout (Block G):** Specific to alkaline chemistry -- NaOH/KOH splash, temperature burns.

---

## Part 2 -- Document Setup Instructions

### Step 1 -- Artboard: 24" x 36"
### Step 2 -- Background: `#1A1F2E`
### Step 3 -- Fonts: Barlow Condensed ExtraBold, Barlow SemiBold, Inter Regular/Medium, JetBrains Mono Regular
### Step 4 -- Colors: Same locked palette as all EP-01 posters (see Poster #31)
### Step 5 -- Guides

**Horizontal guides:**
- 0.5" -- top safe zone
- 2.9" -- Zone 1/Zone 2 boundary
- 4.2" -- Zone 2/Zone 3 boundary (orientation strip)
- 15.0" -- Zone 3/Zone 4 boundary
- 22.0" -- Zone 4/Zone 5 boundary
- 28.5" -- Zone 5/Zone 6 boundary
- 32.5" -- Zone 6/Zone 7 boundary
- 35.5" -- bottom safe zone

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2" / ~1.3" tall)
  Block C: 8-stage strip with Stage 1 highlighted

ZONE 3 -- TANK CROSS-SECTION HERO (4.2"--15.0" / ~10.8" tall)
  Block B: Soak clean tank diagram

ZONE 4 -- FULL PARAMETER TABLE (15.0"--22.0" / ~7.0" tall)
  Block D: Detailed cleaning parameters

ZONE 5 -- COMMON PROBLEMS & FIXES (22.0"--28.5" / ~6.5" tall)
  Block F: Cleaning-specific problem table

ZONE 6 -- SAFETY CALLOUT (28.5"--32.5" / ~4.0" tall)
  Block G: Alkaline cleaning safety panel

ZONE 7 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5"
- Text: `CLEANING`

**BLOCK A -- Subheading**
- Barlow SemiBold, 34 pt, `#2EC4B6` (Teal). X: 0.5", Y: 1.4"
- Text: `Zinc (Alkaline) -- Stage 1 of 8`

**BLOCK A -- Tagline**
- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1"
- Text: `If the cleaning is wrong, everything downstream is wrong. This is where quality starts.`

---

### ZONE 2 -- Sequence Orientation Strip

**BLOCK C -- 8-Stage Strip**

Y: 3.0" to 4.1". A horizontal bar with 8 small boxes representing all stages. Stage 1 is fully opaque and highlighted; stages 2--8 are dimmed.

- Container: Rounded rect, X: 0.5", Y: 3.0", W: 23.0", H: 1.0", fill `#252B3D`, radius 4
- Eight mini-boxes evenly spaced inside (each ~2.5" wide, 0.6" tall):

| Box | Label | Fill | Text Color | Opacity |
|---|---|---|---|---|
| 1 | `1 CLEAN` | `#2EC4B6` | `#1A1F2E` | 100% (highlighted) |
| 2 | `2 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 3 | `3 ACTIVATE` | `#3A4055` | `#F0EDE8` | 40% |
| 4 | `4 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 5 | `5 PLATE` | `#3A4055` | `#F0EDE8` | 40% |
| 6 | `6 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 7 | `7 PASSIVATE` | `#3A4055` | `#F0EDE8` | 40% |
| 8 | `8 DRY` | `#3A4055` | `#F0EDE8` | 40% |

Label font: Barlow Condensed ExtraBold, 12 pt. A small right-pointing arrow between each box (line, 1 pt, `#3A4055`).

Below strip: `Before: Incoming parts (as-received)` and `After: Oil-free, water-break-free surface` -- Inter Regular, 12 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Tank Cross-Section Hero

**Dimensions:** Y: 4.2" to 15.0" (~10.8" tall).

**Section label:**
- Centered. Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `THE SOAK CLEAN TANK`

**BLOCK B -- Tank Diagram**

Y: 5.0" to 14.5" (~9.5" tall).

Tank body:
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 8.0"
- Fill: `#252B3D` (representing cleaner solution)
- Border: 3 pt, `#C8D0D8` (Bright Silver -- tank walls)
- Corner radius: 4 pt (bottom corners only if possible, else all)

Inside the tank (left to right):

**Temperature indicator (left side):**
- Vertical bar, X: 2.5", Y: 6.0", W: 0.6", H: 6.5"
- Fill gradient effect: bottom 70% fill `#E05C5C` (hot), top 30% fill `#3A4055` (empty)
- Label beside: `140--160 F` -- JetBrains Mono Regular, 16 pt, `#E8A020`
- Sub-label: `(60--71 C)` -- JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%

**Parts on rack (center):**
- Horizontal bar (rack bar): Rectangle, X: 5.0", Y: 5.0", W: 14.0", H: 0.3", fill `#C8D0D8`
- 4--5 vertical rectangles hanging from the bar (representing parts):
  - Each: W: 1.5", H: 4.0", fill `#3A4055`, border 2 pt `#C8D0D8`
  - Spaced evenly from X: 6.0" to X: 17.0"
  - Y: 5.3" (hanging from rack bar)

**Agitation arrows (around parts):**
- 6--8 curved upward arrows around and between the parts
- Stroke: 2 pt, `#2EC4B6` (Teal), dashed
- Arrowheads pointing upward
- Represent convective cleaning action and soil lifting

**Soil particles lifting (above parts):**
- Small circles (0.15" diameter) scattered above parts, rising
- Fill: `#E8A020` at 40% (representing oils/soils)
- 8--10 scattered between Y: 5.5" and Y: 7.0"

**Labels inside/around tank:**

Right side label group (X: 18.0", Y: 6.0"):
- `Alkaline Soak Cleaner` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- `4--8 oz/gal` -- JetBrains Mono Regular, 14 pt, `#2EC4B6`
- `Time: 3--10 min` -- JetBrains Mono Regular, 14 pt, `#F0EDE8`

Bottom label:
- Centered. Y: 13.8"
- `Agitation: Mechanical or air -- keeps cleaner in contact with soil` -- Inter Medium, 14 pt, `#F0EDE8`

**Callout boxes flanking the tank (optional, if space):**

Left callout (X: 0.5", Y: 10.0", W: 3.0"):
- Small rounded rect, fill `#1E2435`, border-left 0.06" `#2EC4B6`
- Text: `KEY: Parts must be fully submerged. Air pockets trap soil.`
- Inter Regular, 12 pt, `#F0EDE8`

Right callout (X: 20.5", Y: 10.0", W: 3.0"):
- Small rounded rect, fill `#1E2435`, border-left 0.06" `#E8A020`
- Text: `Electrocleaning option: cathodic then anodic, 5--10 ASF, 30--60 sec each`
- Inter Regular, 12 pt, `#F0EDE8`

---

### ZONE 4 -- Full Parameter Table

**Dimensions:** Y: 15.0" to 22.0" (~7.0" tall).

**Section label:**
- Centered. Y: 15.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `CLEANING PARAMETERS -- DETAILED`

**BLOCK D -- Parameter Table**

Y: 15.9" to 21.8". Two-column layout: left = Soak Clean, right = Electroclean (optional).

**Left table -- Soak Clean (X: 0.5", W: 11.0"):**

Header: fill `#3A4055`, Barlow SemiBold 14 pt `#F0EDE8`. Label: `SOAK CLEAN (STANDARD)`

| Parameter | Value |
|---|---|
| Cleaner type | Alkaline soak (per supplier TDS) |
| Concentration | 4--8 oz/gal (30--60 g/L) |
| Temperature | 140--160 F (60--71 C) |
| Time | 3--10 min (longer for heavy soils) |
| Agitation | Mechanical, air, or ultrasonic |
| pH | 11--13 (highly alkaline) |
| Replenishment | Per titration or TDS schedule |
| Tank material | Mild steel or polypropylene |

**Right table -- Electroclean (X: 12.0", W: 11.5"):**

Header: fill `#3A4055`. Label: `ELECTROCLEAN (OPTIONAL)`

| Parameter | Value |
|---|---|
| Type | Cathodic then anodic (reverse) |
| Current density | 5--10 ASF |
| Time | 30--60 sec each direction |
| Temperature | 140--180 F (60--82 C) |
| Concentration | 4--8 oz/gal |
| Benefit | Removes embedded soils, better adhesion |
| Caution | Cathodic phase generates H2 -- embrittlement risk |
| Note | Anodic-last preferred for steel |

Data: JetBrains Mono Regular 13 pt `#F0EDE8`. Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Rows alternate `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Common Problems & Fixes

**Dimensions:** Y: 22.0" to 28.5" (~6.5" tall).

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `WHAT GOES WRONG AT THE CLEANING STAGE`

**BLOCK F -- Problem Table**

Y: 22.9" to 28.3". Five problem rows.

Each row: rounded rect full width, H: 1.0", alternating `#1E2435` / `#252B3D`, left accent 0.06" `#E05C5C`.

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Water break | Fish-eyes or skip plating in zinc tank | Residual oil -- cleaner too weak or too cold | Increase concentration or temp; extend time |
| Poor adhesion | Zinc peels or flakes on bending | Oxide layer not removed (under-cleaning) | Add electroclean step; check cleaner age |
| Pitting in zinc | Small pits scattered across deposit | Oil micro-droplets carried into plate tank | Carbon treat zinc bath; improve cleaner agitation |
| Staining after rinse | Discolored surface before activation | Cleaner residue -- inadequate rinse | Add rinse stage; check rinse water flow |
| Hydrogen embrittlement | Delayed brittle fracture | Excessive cathodic electrocleaning on high-strength steel | Limit cathodic time; use anodic-only for >150 ksi |

Column widths: Problem (3.5") | Symptom (5.0") | Cause (7.0") | Fix (7.5").

- Problem: Barlow SemiBold, 14 pt, `#E05C5C`
- Symptom: Inter Regular, 13 pt, `#E8A020`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Safety Callout

**Dimensions:** Y: 28.5" to 32.5" (~4.0" tall).

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#E8A020`
- Text: `SAFETY -- ALKALINE CLEANING CHEMISTRY`

**BLOCK G -- Safety Panel**

Y: 29.3" to 32.3". Two side-by-side panels.

**Left -- Chemical Hazards (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `CHEMICAL HAZARDS` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Bullet list (Inter Regular, 14 pt, `#F0EDE8`, line height 155%):
  - `NaOH/KOH: severe burns on contact -- pH > 12`
  - `Hot solution (140--160 F): thermal burn risk`
  - `Mist/vapor: respiratory irritant -- ensure ventilation`
  - `Never add water to concentrated cleaner -- add cleaner to water`

**Right -- PPE Requirements (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `REQUIRED PPE` -- Barlow SemiBold, 18 pt, `#E8A020`
- Bullet list:
  - `Chemical splash goggles (minimum) or face shield`
  - `Chemical-resistant gloves (nitrile or neoprene)`
  - `Chemical-resistant apron`
  - `Eyewash station within 10 seconds travel`
  - `SDS posted and accessible at all times`

---

### ZONE 7 -- Footer Band

Standard footer (identical structure to Poster #31):
- Footer background: `#0D1020`, Y: 32.5", H: 3.5"
- Disclaimer: `This poster is an educational reference tool...` (standard text)
- Title: `Cleaning -- Zinc (Alkaline)`
- Series: `Plating Posters Inc -- Metal Finishing Reference Series`
- Logo placeholder, version `v1.0 -- 2026`

---

## Part 5 -- Grouping and Naming

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | 8-stage strip with Stage 1 highlighted |
| Zone 3 - Tank Hero | Section label, tank cross-section, labels, callouts |
| Zone 4 - Parameters | Section label, soak clean table, electroclean table |
| Zone 5 - Problems | Section label, 5-row problem table |
| Zone 6 - Safety | Section label, chemical hazards panel, PPE panel |
| Zone 7 - Footer | Standard footer elements |

---

## Part 6 -- Light Edition Color Remap Table

| Dark Hex | Light Hex |
|----------|-----------|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

Tank walls (`#C8D0D8`) unchanged. Tank liquid fill (`#252B3D` -> `#E8E8F0`).

---

## Part 7 -- Export Checklist

| File Name | Quality | Bleed |
|---|---|---|
| `Cleaning Zinc Alkaline -- Dark -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Zinc Alkaline -- Dark -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Zinc Alkaline -- Dark -- Digital.pdf` | Standard | No |
| `Cleaning Zinc Alkaline -- Light -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Zinc Alkaline -- Light -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Zinc Alkaline -- Light -- Digital.pdf` | Standard | No |

---

*Elara -- Poster #32 -- Construction Workup v1.0 -- 2026-04-25*
