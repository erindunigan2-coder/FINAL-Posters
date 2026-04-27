---
Project: Plating Posters Inc
Poster Number: 176
Title: "Cleaning -- Chromate Conversion (Hex)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-04 technical reference (hexavalent chromate conversion coating on aluminum)"
Process Scope: Alkaline cleaning stage for hexavalent chromate conversion coating on aluminum (Stage 1 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ChromateConversion
  - Hexavalent
  - Aluminum
  - Cleaning
  - ConstructionWorkup
  - ClusterCC04
---

# Poster #176 -- Construction Workup
## Cleaning -- Chromate Conversion (Hex)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 7. Cleaning aluminum for hex chromate is fundamentally different from cleaning steel for phosphate. The overriding rule: DO NOT ETCH THE ALUMINUM. Strongly caustic cleaners (NaOH-based) attack aluminum aggressively, producing a smut layer that is difficult to remove in the deoxidize step. Non-etch or mildly alkaline cleaners (pH 9--11) with silicate or other etch inhibitors are preferred.

This poster covers the cleaning chemistry for aluminum, the critical distinction between etching and non-etching cleaners, and the alloy-specific considerations that make aluminum cleaning more complex than steel cleaning.

EVERY poster in the CC-04 cluster carries the Cr(VI) carcinogen/regulatory warning in the footer.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning mechanism hero (Block B -- HERO):** Cross-section showing non-etch alkaline cleaner on aluminum, contrasting with what happens when caustic cleaners etch the surface.
2. **Spray vs. immersion comparison (Block D):** Two-column parameter breakdown.
3. **Etch vs. non-etch cleaner warning (Block E):** Critical distinction for aluminum processing.
4. **Alloy-specific notes (Block F):** How 2024, 7075, 6061, and cast alloys differ in cleaning sensitivity.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SPRAY vs. IMMERSION (14.5"--20.5" / ~6.0")
ZONE 5 -- ETCH vs. NON-ETCH + ALLOY NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- MONITORING & DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromate Conversion (Hex) on Aluminum -- Stage 1 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Aluminum is not steel. Caustic cleaners that work on steel will destroy an aluminum surface. Clean without etching -- or spend twice as long fixing the damage downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Shop soils, oils, fingerprints on aluminum  -->  After: Clean, un-etched aluminum surface ready for deoxidize`

**Cr(VI) warning badge (right side of strip):**
- Small rounded rect, fill `#E05C5C` at 20%, border 1 pt `#E05C5C`
- Text: `Cr(VI) PROCESS -- SEE SAFETY NOTE` Inter Medium 11 pt `#E05C5C`

---

### ZONE 3 -- Cleaning Mechanism Hero

**Section label:** `THE ALKALINE CLEANING STAGE -- FOR ALUMINUM` -- Y: 4.4".

**BLOCK B -- Cleaning Cross-Section (Y: 5.0" to 14.0")**

Two side-by-side panels showing correct vs. incorrect cleaning:

**Left -- Non-Etch Cleaning (CORRECT) (X: 0.5", W: 11.0"):**
- Large rounded rect, H: 8.5", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `NON-ETCH ALKALINE CLEANER` Barlow Condensed ExtraBold 22 pt `#27AE60`
- Badge: `CORRECT FOR ALUMINUM` Barlow Condensed ExtraBold 12 pt, fill `#27AE60`, text `#1A1F2E`

Visual: aluminum substrate (bright silver) with cleaner solution above, no damage
- `ALUMINUM SUBSTRATE` on base -- fill `#C8D0D8`
- `Mild alkaline cleaner (pH 9--11)` Barlow SemiBold 14 pt `#2EC4B6`
- Cleaner zone: fill `#2EC4B6` at 10%

Parameters:
- `pH 9--11 (inhibited)` JetBrains Mono 14 pt `#27AE60`
- `Silicate or other etch inhibitor present` Inter Regular 13 pt `#F0EDE8`
- `Surfactants remove oils without attacking base metal` Inter Regular 13 pt `#F0EDE8`
- `Surface remains bright and smooth` Inter Medium 14 pt `#27AE60`

**Right -- Caustic Etching (WRONG) (X: 12.0", W: 11.5"):**
- Large rounded rect, H: 8.5", fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `CAUSTIC CLEANER (NaOH-BASED)` Barlow Condensed ExtraBold 22 pt `#E05C5C`
- Badge: `DANGEROUS FOR ALUMINUM` Barlow Condensed ExtraBold 12 pt, fill `#E05C5C`, text `#1A1F2E`

Visual: aluminum substrate with damaged/rough surface, dark smut layer
- `ALUMINUM SUBSTRATE` with roughened surface texture
- `Strong caustic (pH 12--14)` Barlow SemiBold 14 pt `#E05C5C`
- `SMUT LAYER` on surface -- dark patches

Consequences:
- `Al dissolves aggressively in caustic:` JetBrains Mono 12 pt `#E05C5C`
- `2Al + 2NaOH + 2H2O --> 2NaAlO2 + 3H2` JetBrains Mono 11 pt `#F0EDE8`
- `Alloy elements (Cu, Si, Fe, Mn) precipitate as smut` Inter Regular 13 pt `#E05C5C`
- `Smut is hard to remove -- requires aggressive deox` Inter Regular 13 pt `#F0EDE8`
- `Over-etched surface = poor, uneven chromate coating` Inter Medium 13 pt `#E05C5C`

---

### ZONE 4 -- Spray vs. Immersion

**Section label:** `SPRAY vs. IMMERSION -- PARAMETER COMPARISON` -- Y: 14.7".

**BLOCK D -- Two-Column Layout (Y: 15.3" to 20.3")**

**Left -- Immersion Cleaning (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `IMMERSION CLEANING` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Value |
|---|---|
| Concentration | 4--8 oz/gal (30--60 g/L) |
| Temperature | 120--160 F (49--71 C) |
| Time | 3--10 min |
| pH | 9--11 |
| Method | Soak with mild agitation |

**Right -- Spray Cleaning (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `SPRAY CLEANING` Barlow SemiBold 20 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Concentration | 2--4 oz/gal (15--30 g/L) |
| Temperature | 100--140 F (38--60 C) |
| Time | 1--3 min |
| pH | 9--11 |
| Method | Spray at 15--25 psi |

Bottom note: `Lower concentration and temperature for spray -- mechanical action of spray compensates.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Etch vs. Non-Etch + Alloy Notes

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Cleaner Selection Guide (X: 0.5", W: 11.0"):**

Section label: `CLEANER SELECTION FOR ALUMINUM` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E8A020` 0.06".

| Cleaner Type | pH | Aluminum Safe? | Notes |
|---|---|---|---|
| Non-etch alkaline | 9--11 | YES | Standard for chromate prep |
| Silicate-inhibited alkaline | 10--12 | YES | Silicate protects aluminum |
| Fluoride-bearing | 9--11 | YES (controlled) | Effective but must control F- |
| Mild caustic (NaOH < 5%) | 12--13 | CAUTION | Light etch; requires thorough deox |
| Strong caustic (NaOH > 5%) | 13--14 | NO | Aggressive etch; creates heavy smut |

Safe cleaners: `#27AE60`. Caution: `#E8A020`. Unsafe: `#E05C5C`.

**Right -- Alloy-Specific Notes (X: 12.0", W: 11.5"):**

Section label: `ALLOY SENSITIVITY` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

Rounded rect, H: 5.0", fill `#1E2435`, left accent `#2EC4B6` 0.06".

| Alloy Family | Cleaning Notes |
|---|---|
| 2024, 2014 (high Cu) | Copper-rich; smuts easily; avoid caustic; mild cleaner + aggressive deox |
| 7075, 7050 (Zn-Cu) | Similar to 2xxx; tenacious copper smut if etched |
| 6061, 6063 (low alloy) | Less sensitive; mild alkaline is sufficient |
| 356, A356 (cast, high Si) | Silicon particles resist cleaning; may need longer soak time |

Note: `The alloy determines the downstream deoxidize formula. Clean gently here -- let the deoxidizer do the heavy lifting.` Inter Medium 13 pt `#E8A020`

---

### ZONE 6 -- Monitoring & Defects

**Section label:** `BATH MONITORING & CLEANING FAILURES` -- Y: 26.7".

**BLOCK F -- Two-Column (Y: 27.3" to 32.3")**

**Left -- Monitoring Table:**

| Parameter | Method | Frequency |
|---|---|---|
| pH | pH meter | Every 4 hours |
| Concentration (alkalinity) | Titration | Every 4 hours |
| Temperature | Thermocouple | Continuous |
| Oil content | Visual / skimmer | Continuous |
| Water-break test | Visual | Every load |

**Right -- Cleaning Defects:**

| Defect | Cause | Fix |
|---|---|---|
| Smut on surface after clean | Caustic etching aluminum; wrong cleaner | Switch to non-etch cleaner; reduce pH |
| Residual oil after clean | Low concentration, low temp, short time | Increase conc/temp/time; check surfactant level |
| Uneven chromate downstream | Mixed cleaning quality across parts | Improve loading; ensure all surfaces contacted |
| Pitting on aluminum | Chloride in cleaner or rinse water | Use DI/RO water; check cleaner composition |

---

### ZONE 7 -- Footer

Standard footer with Cr(VI) disclaimer.

**Footer background:** Rectangle, fill `#0D1020`

**Disclaimer:**
> This poster is an educational reference tool. Hexavalent chromium (Cr6+) is a known human carcinogen. Process parameters shown are typical industry values for cleaning aluminum prior to hex chromate conversion coating per MIL-DTL-5541 Type I. Specific formulations and limits vary by proprietary product. Consult your process supplier and safety data sheets. Follow all applicable OSHA, EPA, and local regulations.

**Poster title:** `Cleaning -- Chromate Conversion (Hex)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Chromate Conversion Hex -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The etch vs. non-etch comparison in the hero zone is the centerpiece. For operators who come from steel phosphate backgrounds, the instinct is to use aggressive cleaners -- this poster stops that instinct with a clear visual of what happens when you etch aluminum. The alloy-specific notes give aerospace operators the nuance they need: 2024 and 7075 smut more easily than 6061, which affects everything downstream.

The Cr(VI) footer disclaimer appears on every CC-04 poster -- this is the first in the series, and the pattern is set here.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #176 -- Construction Workup v1.0*
*2026-04-26*
