---
Project: Plating Posters Inc
Poster Number: 208
Title: "Passivation (Stainless Steel) -- Cleaning"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.2)"
Technical Source: Alkaline cleaning and degreasing for stainless steel passivation lines. Covers cleaner selection (NO chloride), electrocleaning, and descaling/pickling as a pre-step for heavy heat tint. Per ASTM A967, AMS 2700, ASTM A380.
Process Scope: Stainless steel passivation -- Stage 1 cleaning (alkaline degrease)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - Cleaning
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #208 -- Construction Workup
## Passivation (Stainless Steel) -- Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cleaning stage poster for CC-08: Stainless Steel Passivation. Cleaning for passivation has one absolute rule that overrides everything else: NO CHLORIDE. Chloride in the cleaner, in the rinse water, in the shop air, on the operator's gloves -- any chloride that contacts stainless steel can initiate pitting corrosion and undermine the entire purpose of passivation.

Beyond the chloride prohibition, the poster covers standard alkaline cleaning, electrocleaning for precision parts, and the descaling/pickling step that is sometimes needed before passivation when parts have heavy heat tint from welding or heat treatment.

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

1. **Stage detail panel (Block B -- HERO):** Cleaning parameters and the chloride prohibition.
2. **Chloride sources callout (Block C):** Where chloride contamination comes from.
3. **Cleaning method comparison (Block D):** Soak clean vs. electrocleaner vs. descaling pickle.
4. **Heat tint / descaling decision (Block E):** When parts need pickling before passivation.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CLEANING STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (parameters, chloride prohibition)
  Block C: Chloride contamination sources

ZONE 3 -- CLEANING METHOD COMPARISON (15.5"--22.0" / ~6.5" tall)
  Block D: Soak clean vs. electrocleaner vs. descaling pickle

ZONE 4 -- HEAT TINT / DESCALING DECISION (22.0"--28.5" / ~6.5" tall)
  Block E: When pickling is needed before passivation

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Stage 1 -- Cleaning / Degreasing`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Rule number one: NO CHLORIDE. Not in the cleaner. Not in the water. Not on the gloves. Chloride is the enemy of stainless steel.`
- Y: 2.2"

---

### ZONE 2 -- Cleaning Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `ALKALINE CLEANING -- THE FOUNDATION`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 9.0". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 5.0", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge:
- Rounded rect 1.4" x 0.4", fill `#2EC4B6`
- Text: `STAGE 1 -- CLEAN` -- Barlow Condensed ExtraBold, 14 pt, `#1A1F2E`

Parameters (JetBrains Mono 14 pt `#F0EDE8`, left column):
```
Type:            Alkaline cleaner, pH 10--13
Concentration:   4--8 oz/gal (30--60 g/L)
Temperature:     130--180 F (54--82 C)
Time:            5--15 min (immersion)
```

Soil removal targets (Inter Regular 14 pt `#F0EDE8`):
```
- Machining oils and cutting fluids
- Grinding compounds and polishing compounds
- Stamping lubricants and drawing compounds
- Fingerprints and handling residues
- Organic soils and shop contaminants
```

**CHLORIDE PROHIBITION CALLOUT** (right side, prominent):
- Rounded rect W: 10.0", H: 3.0", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 8
- Title: `ABSOLUTE RULE: NO CHLORIDE` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Body (Inter Medium 14 pt `#F0EDE8`):
```
Chloride-containing cleaners MUST NEVER be used
on stainless steel.

Chloride initiates pitting corrosion --
the exact failure that passivation is
designed to prevent.

Check your cleaner's SDS for chloride content.
If in doubt, test with a silver nitrate spot test.
```

---

**BLOCK C -- Chloride Contamination Sources**

Y: 9.5" to 15.0". Six source cards in a 3x2 grid.

Each card: Rounded rect, W: 7.33", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Row 1 (Y: 9.5"):
| Card | X | Source | Risk |
|---|---|---|---|
| 1 | 0.5" | CHLORINATED CLEANERS | Some industrial cleaners contain HCl or chlorinated solvents. Read the SDS. |
| 2 | 8.08" | TAP WATER | Municipal water contains 10--250+ ppm chloride. Use DI for critical rinsing. |
| 3 | 15.67" | SHOP AIR | Shops near salt water or using HCl for other processes contaminate the air. |

Row 2 (Y: 12.5"):
| Card | X | Source | Risk |
|---|---|---|---|
| 4 | 0.5" | HANDLING / GLOVES | PVC gloves release chloride. Sweat contains NaCl. Use nitrile or cotton gloves. |
| 5 | 8.08" | MARKING MATERIALS | Some markers, tapes, and labels contain chloride. Use chloride-free marking. |
| 6 | 15.67" | CARBON STEEL CONTACT | Carbon steel fixtures, racks, and storage shelves transfer iron AND may carry chloride residues. |

Interior per card:
- Source: Barlow SemiBold 14 pt `#E05C5C`
- Risk: Inter Regular 12 pt `#F0EDE8`

---

### ZONE 3 -- Cleaning Method Comparison

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `CLEANING METHODS -- THREE OPTIONS`

**BLOCK D -- Three Method Panels**

Y: 16.3" to 21.8". Three side-by-side panels.

**Soak Clean (Standard):**
- Rounded rect, X: 0.5", Y: 16.3", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SOAK CLEAN` -- Barlow SemiBold, 18 pt, `#2EC4B6`

```
Type:     Alkaline immersion
Conc:     4--8 oz/gal
Temp:     130--180 F
Time:     5--15 min
Best for: General machined parts, moderate soils
Note:     Most common method
```

**Electrocleaner (Precision):**
- Rounded rect, X: 8.08", Y: 16.3", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `ELECTROCLEANER` -- Barlow SemiBold, 18 pt, `#E8A020`

```
Type:     Cathodic electrocleaner preferred
Current:  30--60 ASF
Temp:     130--160 F
Time:     1--3 min after soak clean
Best for: Precision and medical parts
Note:     Cathodic avoids oxygen pitting risk
```

**Descaling Pickle (Pre-Step):**
- Rounded rect, X: 15.67", Y: 16.3", W: 7.83", H: 5.2", fill `#1E2435`, left accent `#E05C5C`
- Title: `DESCALING PICKLE` -- Barlow SemiBold, 18 pt, `#E05C5C`

```
Type:     Nitric-hydrofluoric acid
Conc:     10--15% HNO3 + 1--3% HF
Temp:     120--140 F (49--60 C)
Time:     5--15 min
Best for: Heavy heat tint (welding/heat treat)
WARNING:  This is NOT passivation -- it is
          aggressive surface removal. Passivation
          follows separately after rinsing.
```

---

### ZONE 4 -- Heat Tint / Descaling Decision

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DO YOUR PARTS NEED DESCALING BEFORE PASSIVATION?`

**BLOCK E -- Decision Panel**

Y: 22.9" to 28.3". Two panels.

**Left -- Parts That Need Descaling:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#E05C5C`
- Title: `DESCALE FIRST (HNO3/HF PICKLE)` -- Barlow SemiBold, 18 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
- Heavy heat tint (blue/gold/brown oxide from welding)
- Thick thermal oxide from heat treatment
- Weld discoloration that alkaline clean cannot remove
- Parts with visible scale or heavy oxide
- Cast stainless with surface inclusions

The thick thermal oxide is too tenacious for
passivation acid alone. The pickle removes it.
Then passivation restores the passive film.

SEQUENCE: Clean -> Rinse -> Pickle -> Rinse ->
          Passivate -> Rinse -> Dry
```

**Right -- Parts That Go Directly to Passivation:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `PASSIVATE DIRECTLY (NO PICKLE NEEDED)` -- Barlow SemiBold, 18 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
- Machined parts with light surface contamination
- Parts with embedded free iron from tooling
- Stamped or formed parts (no heat tint)
- Parts that have been polished or ground
- Electropolished parts (already clean surface)

These parts have surface contamination (free iron,
organic soils) but NOT thick thermal oxide.
Passivation acid removes the free iron directly.

SEQUENCE: Clean -> Rinse -> Passivate ->
          Rinse -> Dry
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #207.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PITTING AFTER PASSIVATION | Chloride in cleaner or rinse water | Eliminate ALL chloride sources; use chloride-free cleaner |
| 2 | 6.33" | RESIDUAL OIL (WATER BREAK) | Cleaner too dilute; temp too low; time too short | Increase concentration/temp/time; check surfactant |
| 3 | 12.16" | HEAT TINT WON'T REMOVE | Thermal oxide too heavy for passivation acid alone | Descale with HNO3/HF pickle before passivation |
| 4 | 18.0" | ETCHING DURING PICKLE | HF too concentrated; temp too high; time too long | Reduce HF to 1--2%; lower temp; reduce time |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for cleaning prior to passivation of stainless steel per ASTM A967, AMS 2700, and ASTM A380. Chloride-free cleaning is mandatory. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Cleaning -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chloride prohibition is the emotional center of this poster. It gets a dedicated high-visibility callout in the hero zone AND a full six-card grid of contamination sources. This repetition is intentional -- chloride contamination is the single most common cause of passivation failure, and many shops do not realize how many sources of chloride exist in their environment. The descaling decision tree in Zone 4 addresses the second most common confusion: when passivation alone is sufficient vs. when a pickle is needed first.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #208 -- Construction Workup v1.0*
*2026-04-26*
