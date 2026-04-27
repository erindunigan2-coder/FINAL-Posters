---
Project: Plating Posters Inc
Poster Number: 87
Title: "Hard Chrome Plating -- Process Flow"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
Technical Source: Industry-standard hard chrome (industrial/functional chrome) plating process. Complete 8-stage sequence from cleaning through post-treatment. Hard chrome is STILL predominantly hexavalent CrO3 -- this is functional plating for wear resistance, not cosmetic. Trivalent alternatives exist but are thickness-limited (~10-15 um max). OSHA PEL 5 ug/m3 Cr(VI) -- known carcinogen.
Process Scope: Hard chrome plating -- complete process flow (8 stages)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HardChrome
  - Hexavalent
  - ProcessFlow
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #87 -- Construction Workup
## Hard Chrome Plating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EP-08: Hard Chrome Plating. It shows the complete 8-stage process sequence at a glance. Hard chrome is fundamentally different from decorative chrome: thick deposits (2.5-500+ microns) plated directly to the basis metal (no nickel undercoat), for functional purposes -- wear resistance, low friction, dimensional restoration. The chemistry is still predominantly hexavalent CrO3, making this the most hazardous process in the poster series. Every poster in this cluster carries a prominent regulatory/safety warning.

Key technical fact for this poster: the CrO3:SO4 ratio (100:1) is THE most critical bath parameter. Cathode efficiency is only 10-25% -- most of the current goes to hydrogen evolution. Activation is done by reverse etch (anodic) in the chrome bath itself. Post-treatment is grinding/honing to dimension, not chemical conversion.

Design philosophy: clean U-flow diagram as the hero, parameter summary table, a "hard chrome vs. decorative chrome" comparison, troubleshooting strip, and a prominent safety banner that is impossible to ignore.

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

2. **Parameter summary table (Block D):** 8-row table.

3. **"Hard vs. Decorative" comparison callout (Block E):** Side-by-side comparison.

4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

5. **Safety banner (Block A2):** Prominent coral banner in Zone 1 -- Cr(VI) carcinogen warning.

6. **Print size -- 24x36".**

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

Standard locked palette (see Poster #79).

### Step 5 -- Set ruler guides

Standard vertical and horizontal guides (see Poster #79).

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
  Block A2: Safety banner (Cr VI carcinogen warning)

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Eight-stage U-flow diagram (2 rows of 4)
  Block C: Stage legend strip

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5" tall)
  Block D: 8-row parameter table

ZONE 4 -- HARD VS. DECORATIVE COMPARISON (22.0"--28.5" / ~6.5" tall)
  Block E: Hard Chrome vs. Decorative Chrome side-by-side

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + poster title + series name + logo placeholder + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Dimensions:** Full page width. Y: 0" to 2.9".

**BLOCK A -- Headline**

- Position: X: 0.5". Y: 0.5"
- Width: 23.0"
- Font: Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`
- Letter spacing: -4
- Text (all caps):

> HARD CHROME PLATING

**BLOCK A -- Subheading**

- Position: X: 0.5". Y: 1.4"
- Font: Barlow SemiBold, 32 pt, `#27AE60` (Emerald)
- Text:

> Complete Process Flow -- 8 Stages from Cleaning to Finish Grind

**BLOCK A -- Tagline**

- Position: X: 0.5". Y: 2.0"
- Width: 15.0"
- Font: Barlow SemiBold, 18 pt, `#F0EDE8` at 65%
- Text:

> Functional chrome for wear, hardness, and dimensional restoration. 800--1000 HV as-plated. Still hexavalent. Still hazardous. Still essential.

**BLOCK A2 -- Safety Banner**

- Position: X: 15.5". Y: 1.4"
- Width: 8.0". Height: 1.3"
- Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 6
- Line 1: `HEXAVALENT CHROMIUM (Cr VI)` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Line 2: `KNOWN HUMAN CARCINOGEN` -- Barlow Condensed ExtraBold, 14 pt, `#E05C5C`
- Line 3: `OSHA PEL: 5 ug/m3 | EPA NESHAP 40 CFR 63 Subpart N` -- JetBrains Mono Regular, 10 pt, `#E05C5C` at 80%

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Dimensions:** Full page width within margins. Y: 2.9" to 15.5" (~12.6" tall).

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`

> THE COMPLETE PROCESS -- STAGE BY STAGE

**BLOCK B -- Eight-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Two rows of four boxes. Same construction as Poster #79.

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Activation) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Reverse Etch (Activation) | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. (Polarity Reversal) | Box 4 | 17.0" | `#E8A020` (Amber) | Transition |

**Bottom Row (Y: 9.5" to 14.0") -- Stages 5-8, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Hard Chrome Plate | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Chrome) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Hydrogen Embrittlement Relief | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |
| 8. Finish Grind / Hone | Box 8 | 0.5" | `#E8A020` (Amber) | Post-Treatment |

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `6--10 oz/gal (45--75 g/L)` / `150--190 F (66--88 C)` / `5--15 min`
- Purpose: `Remove machining oils, grinding coolant, lapping compound`
- Check: `Heavy-duty cleaner -- these parts are dirty`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Double overflow, ambient`
- Purpose: `Remove alkaline cleaner residue`
- Check: `Must be thorough -- alkaline into chrome bath = problems`

*Box 3 -- Reverse Etch (Activation):*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Reverse Etch`
- Parameters: `Anodic in chrome bath` / `100--200 ASF (anodic)` / `30 sec to 3 min`
- Purpose: `Dissolve oxide, roughen surface, heat part`
- Check: `Part is the ANODE -- current reversed from plating`

*Box 4 -- Polarity Reversal:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Polarity Reversal` / Subtitle: `Transition`
- Parameters: `Switch from anodic to cathodic` / `In same chrome bath` / `Immediate`
- Purpose: `Begin plating -- part becomes cathode`
- Check: `No delay between etch and plate -- same tank`

*Box 5 -- Hard Chrome Plate:*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `Hard Chrome Plate` / Subtitle: `Main Tank`
- Parameters: `CrO3: 200--300 g/L` / `CrO3:SO4 = 100:1` / `120--140 F` / `100--400 ASF`
- Purpose: `Electrodeposit thick, hard chrome`
- Check: `CrO3:SO4 ratio is THE critical parameter`

*Box 6 -- Rinse (Post-Chrome):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Chrome`
- Parameters: `Multi-stage cascade` / `Drag-out recovery first`
- Purpose: `Remove Cr(VI) drag-out`
- Check: `HAZARDOUS WASTE -- recover or reduce Cr(VI)` (`#E05C5C`)

*Box 7 -- H-Embrittlement Relief:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `H-Embrittlement Relief`
- Parameters: `Bake: 375 F (191 C)` / `Within 4 hours of plating` / `3--24 hr (per spec)`
- Purpose: `Drive out absorbed hydrogen`
- Check: `MANDATORY for high-strength steel (>= 40 HRC)` (`#E05C5C`)

*Box 8 -- Finish Grind / Hone:*
- Badge: `STAGE 8`, fill `#E8A020`
- Name: `Finish Grind / Hone`
- Parameters: `Grind to final dimension` / `Surface finish per spec` / `Measure with micrometer`
- Purpose: `Achieve dimensional tolerance`
- Check: `Hard chrome is almost always ground after plating`

---

**BLOCK C -- Stage Legend Strip**

Y: 14.3" to 15.0". Standard construction.

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Cleaning & Rinse` |
| `#E8A020` (Amber) | `Activation & Post-Treatment` |
| `#27AE60` (Emerald) | `Plating (Main Tank)` |
| `#E05C5C` (Coral) | `Safety Hazard / Caution` |

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

**BLOCK D -- 8-Row Parameter Table**

Y: 16.3" to 21.8". Standard column widths.

| Stage | Chemistry | Temp | Time | CD | Key Control |
|---|---|---|---|---|---|
| 1. Alk Clean | 6--10 oz/gal | 150--190 F | 5--15 min | -- | Remove all machining soils |
| 2. Rinse | DI or city water | Ambient | 30--60 sec | -- | Double overflow |
| 3. Reverse Etch | In chrome bath (anodic) | Bath temp | 30 sec--3 min | 100--200 ASF (anodic) | Part is ANODE |
| 4. Polarity Reversal | Same bath | Bath temp | Immediate | Switch to cathodic | No delay |
| 5. Hard Chrome | CrO3 200--300, SO4 2--3 g/L | 120--140 F | Per thickness spec | 100--400 ASF | CrO3:SO4 = 100:1 |
| 6. Rinse | Cascade + recovery | Ambient | 30--60 sec | -- | Cr(VI) recovery |
| 7. H-Embrit Relief | Bake in oven | 375 F | 3--24 hr | -- | Within 4 hr of plating |
| 8. Finish Grind | Mechanical | N/A | Per dimension | -- | Grind to final spec |

---

### ZONE 4 -- Hard vs. Decorative Comparison

**Section label:** `HARD CHROME VS. DECORATIVE CHROME` -- Y: 22.2".

**BLOCK E -- Side-by-Side Comparison (Y: 22.9" to 28.3")**

**Left -- Hard Chrome:**
- Rounded rect, X: 0.5", W: 11.0", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `HARD CHROME` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Functional / Industrial` -- 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Purpose | Wear resistance, low friction, dimensional restoration |
| Thickness | 2.5--500+ microns (0.1--20+ mil) |
| Hardness | 800--1000 HV |
| Undercoat | Usually NONE -- direct to basis metal |
| Chemistry | Hexavalent CrO3 (predominantly) |
| Temperature | 120--140 F |
| CD | 100--400 ASF |
| Efficiency | 12--25% |
| Anodes | Conforming lead alloy |
| Post-treatment | Grind/hone to dimension |

Bottom: `The workhorse of industrial plating. Hydraulic cylinders, piston rings, mold cavities, landing gear.` -- `#27AE60`

**Right -- Decorative Chrome:**
- Rounded rect, X: 12.0", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `DECORATIVE CHROME` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Cosmetic / Aesthetic` -- 14 pt, `#F0EDE8` at 50%

| Property | Value |
|---|---|
| Purpose | Bright, tarnish-resistant appearance |
| Thickness | 0.15--0.75 microns |
| Hardness | Same (but irrelevant at this thickness) |
| Undercoat | ALWAYS over nickel (+ optional copper) |
| Chemistry | Increasingly trivalent Cr(III) |
| Temperature | 80--120 F (tri) / 95--120 F (hex) |
| CD | 50--200 ASF |
| Efficiency | 10--30% |
| Anodes | Lead (hex) or graphite/MMO (tri) |
| Post-treatment | Dry and inspect |

Bottom: `The finish you see. Faucets, automotive trim, furniture hardware. Moving to trivalent.` -- `#2EC4B6`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | MILKY / FROSTED | Temp too low, CrO3 too low, Cr3+ too high | Raise temp; check CrO3:SO4 ratio; reduce Cr3+ |
| 2 | 6.33" | BURNING (ROUGH, DARK) | CD too high for temp, poor anode geometry | Reduce CD; reshape conforming anodes |
| 3 | 12.16" | POOR ADHESION / PEELING | Inadequate reverse etch, surface contamination | Extend reverse etch; improve cleaning |
| 4 | 18.0" | NON-UNIFORM THICKNESS | Anode geometry mismatch, no shields/thieves | Reshape anodes; add shields; adjust racking |

Standard card construction with `#E05C5C` left accents.

---

### ZONE 6 -- Footer Band

Standard. Title: `Hard Chrome Plating -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Hard chrome plating uses hexavalent chromium -- a known human carcinogen. Comply with all OSHA (29 CFR 1910.1026), EPA NESHAP (40 CFR 63 Subpart N), and state/local regulations. Process parameters shown are typical industry values. Consult your process supplier for application-specific guidance.`

---

## Part 5 -- Grouping and Naming Convention

| Group Name | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline, safety banner |
| Zone 2 - Process Flow | Section label, eight flow boxes, arrows, legend strip |
| Zone 3 - Parameter Table | Section label, 8-row table |
| Zone 4 - Hard vs Deco | Section label, two comparison callouts |
| Zone 5 - Troubleshooting | Section label, four problem cards |
| Zone 6 - Footer | Footer band, disclaimer, title, series, logo, version |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap table (see Poster #79).

---

## Part 7 -- Export Checklist

| File Name | Mode | Quality | Bleed |
|---|---|---|---|
| `Hard Chrome Process Flow -- Dark -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hard Chrome Process Flow -- Dark -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hard Chrome Process Flow -- Dark -- Digital.pdf` | RGB | Standard | No |
| `Hard Chrome Process Flow -- Light -- 24x36 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hard Chrome Process Flow -- Light -- 18x24 -- Print.pdf` | RGB | 300 DPI | Yes |
| `Hard Chrome Process Flow -- Light -- Digital.pdf` | RGB | Standard | No |

---

## Design Notes

This is the "map" poster for the most hazardous plating process in the entire series. The safety banner in Zone 1 is not decorative -- it is a legal and moral obligation. The process flow differs from decorative chrome in critical ways: (1) activation is done by reverse etch in the chrome bath itself (no separate tank), (2) stages 3 and 4 happen in the same tank (etch then plate), (3) post-treatment is mechanical grinding, not chemical. The hard vs. decorative comparison answers the most common question from people outside the industry: "isn't hard chrome the same as regular chrome?" No. It is not. The comparison makes that unmistakably clear.

The Stage 4 "Polarity Reversal" box is unusual -- it is a process step that happens in the same tank as Stage 3. The flow diagram should make it visually clear that Stages 3-5 all occur in the same tank with the arrow from Box 3 to Box 4 being very short or overlapping, with a note: "Stages 3-5: same tank."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #87 -- Construction Workup v1.0*
*2026-04-26*
