---
Project: Plating Posters Inc
Poster Number: 178
Title: "Deoxidize / Desmut -- Chromate Conversion (Hex)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CC-04 technical reference (hexavalent chromate conversion coating on aluminum)"
Process Scope: Deoxidize/desmut (acid activation) stage for hexavalent chromate conversion coating on aluminum (Stage 3 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ChromateConversion
  - Hexavalent
  - Aluminum
  - Deoxidize
  - Desmut
  - ConstructionWorkup
  - ClusterCC04
---

# Poster #178 -- Construction Workup
## Deoxidize / Desmut -- Chromate Conversion (Hex)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 7. This is the "surface conditioning" equivalent for aluminum -- but instead of a Ti colloid activator (zinc phosphate), aluminum uses an acid deoxidizer to remove the natural oxide layer and alloy smut. The oxide layer on aluminum reforms in seconds, so the deoxidize step must expose fresh, active aluminum immediately before the chromate coating step.

The critical content: alloy-specific deoxidize formulas. 2024 and 7075 (high copper) require HNO3 + HF to remove tenacious copper smut. 6061 and 6063 need only mild HNO3. Cast alloys (356, A356) with high silicon require HF to dissolve silicon particles. Getting this wrong means incomplete smut removal, patchy chromate coating, and spec failure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Deoxidize mechanism hero (Block B -- HERO):** Cross-section showing acid removing oxide and smut layers from aluminum, exposing fresh Al.
2. **Deoxidizer chemistry options (Block D):** Table of HNO3, HNO3+HF, chromic-sulfuric, non-chrome, and ammonium bifluoride formulas.
3. **Alloy-specific guide (Block E):** Which deoxidizer for which alloy family.
4. **Common defects (Block F):** Over-deox, under-deox, pitting from HF excess.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- DEOXIDIZE MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DEOXIDIZER CHEMISTRY OPTIONS (14.5"--20.5" / ~6.0")
ZONE 5 -- ALLOY-SPECIFIC GUIDE (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECTS & MONITORING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE / DESMUT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Chromate Conversion (Hex) on Aluminum -- Stage 3 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Strip the oxide. Remove the smut. Expose fresh aluminum. The chromate reaction needs a clean, active surface -- and aluminum re-oxidizes in seconds. This step is time-critical.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Oxidized aluminum with alloy smut  -->  After: Fresh, active aluminum surface ready for chromate`

Cr(VI) warning badge (right): `Cr(VI) PROCESS -- SEE SAFETY NOTE` `#E05C5C`

---

### ZONE 3 -- Deoxidize Mechanism Hero

**Section label:** `REMOVING THE OXIDE AND SMUT` -- Y: 4.4".

**BLOCK B -- Deoxidize Cross-Section (Y: 5.0" to 14.0")**

**Layered cross-section showing aluminum with oxide and smut:**

**Base layer -- Aluminum substrate:**
- Rectangle, fill `#C8D0D8`, border 2 pt `#3A4055`
- Label: `ALUMINUM SUBSTRATE (base metal)` Barlow SemiBold 14 pt `#F0EDE8`

**Oxide layer (on aluminum):**
- Thin layer (2 pt), fill `#3A4055` at 50%
- Label: `Al2O3 oxide layer (reforms in seconds in air)` Inter Regular 12 pt `#F0EDE8`

**Smut layer (on oxide):**
- Patchy dark layer, fill `#E05C5C` at 25%
- Label: `Alloy smut: Cu, Si, Fe, Mn precipitates from cleaning` Inter Regular 12 pt `#E05C5C`

**Acid deoxidizer solution (above):**
- Large rectangle, fill `#E8A020` at 8%, border 2 pt `#E8A020`
- Label: `ACID DEOXIDIZER` Barlow SemiBold 16 pt `#E8A020`

**Mechanism arrows showing acid dissolving oxide and smut:**
- Arrows pointing down from acid to oxide/smut layers
- `HNO3 dissolves Al2O3 oxide` Inter Medium 13 pt `#E8A020`
- `HF (when present) attacks Si particles and Cu-rich smut` Inter Medium 13 pt `#E8A020`
- `Result: fresh Al surface exposed` Inter Medium 14 pt `#27AE60`

**Parameters (left side):**
- `HNO3 30--50% by volume` JetBrains Mono 14 pt `#E8A020`
- `HF 1--3% (for high-Cu/Si alloys)` JetBrains Mono 14 pt `#E8A020`
- `Ambient temperature` JetBrains Mono 14 pt `#F0EDE8`
- `1--5 min (alloy dependent)` JetBrains Mono 14 pt `#F0EDE8`

**Bottom callout (Y: 13.0"):**
- `ALUMINUM RE-OXIDIZES IN SECONDS. Minimize time between deoxidize and chromate coating -- ideally less than 5 minutes.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Deoxidizer Chemistry Options

**Section label:** `DEOXIDIZER FORMULAS -- CHOOSE BY ALLOY` -- Y: 14.7".

**BLOCK D -- Chemistry Options Table (Y: 15.3" to 20.3")**

Full-width table:

| Deoxidizer Type | Concentration | Temperature | Time | Best For |
|---|---|---|---|---|
| Nitric acid (HNO3) | 30--50% by volume | Ambient | 1--5 min | General Al; 6xxx alloys |
| Nitric + HF | 30% HNO3 + 1--3% HF | Ambient | 30 sec--3 min | 2xxx, 7xxx (high Cu); cast Al (high Si) |
| Chromic-sulfuric (legacy) | 10--15 oz/gal CrO3 + 30--40 oz/gal H2SO4 | 140--160 F | 5--10 min | Heavy oxide/scale removal |
| Non-chrome deoxidizers | Ferric sulfate, persulfate (per supplier) | Ambient--120 F | 1--5 min | RoHS/REACH-compliant lines |
| Ammonium bifluoride | 4--8 oz/gal | Ambient | 1--3 min | Cast alloys with heavy Si |

Header: Barlow SemiBold 13 pt `#F0EDE8`, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`, alternating rows.

Bottom note: `Chromic-sulfuric deox adds ANOTHER Cr(VI) source to the process. Non-chrome alternatives are available and increasingly specified.` Inter Regular 12 pt `#E05C5C` at 80%.

---

### ZONE 5 -- Alloy-Specific Guide

**Section label:** `ALLOY-SPECIFIC DEOXIDIZE GUIDE` -- Y: 20.7".

**BLOCK E -- Four Alloy Family Cards (Y: 21.3" to 26.3")**

Four cards in a 2x2 grid:

**Card 1 -- 2024, 2014 (High Copper) (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `2xxx SERIES (HIGH COPPER)` Barlow SemiBold 16 pt `#E8A020`
- `Copper-rich alloys produce tenacious dark copper smut` Inter Regular 13 pt `#F0EDE8`
- `Requires HNO3 + HF to dissolve copper` JetBrains Mono 12 pt `#E8A020`
- `Mild HNO3 alone will NOT remove copper smut` Inter Medium 12 pt `#E05C5C`

**Card 2 -- 7075, 7050 (Zinc-Copper) (X: 12.0", W: 11.5"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `7xxx SERIES (ZINC-COPPER)` Barlow SemiBold 16 pt `#E8A020`
- `Same as 2xxx -- copper smut is tenacious` Inter Regular 13 pt `#F0EDE8`
- `HNO3 + HF required` JetBrains Mono 12 pt `#E8A020`
- `Zinc dissolves readily; copper does not` Inter Regular 12 pt `#F0EDE8` at 70%

**Card 3 -- 6061, 6063 (Low Alloy) (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `6xxx SERIES (LOW ALLOY)` Barlow SemiBold 16 pt `#27AE60`
- `Low copper content -- mild deoxidizer is sufficient` Inter Regular 13 pt `#F0EDE8`
- `HNO3 30--50% alone, or non-chrome deoxidizer` JetBrains Mono 12 pt `#27AE60`
- `Easiest alloys to process` Inter Regular 12 pt `#F0EDE8` at 70%

**Card 4 -- 356, A356 (Cast, High Silicon) (X: 12.0", W: 11.5"):**
- Rounded rect, H: 2.3", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `CAST Al (HIGH SILICON)` Barlow SemiBold 16 pt `#E05C5C`
- `Silicon particles resist acid dissolution` Inter Regular 13 pt `#F0EDE8`
- `MUST use HF-containing deoxidizer or ammonium bifluoride` JetBrains Mono 12 pt `#E05C5C`
- `Longer soak time may be needed (3--5 min)` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 6 -- Defects & Monitoring

**Section label:** `DEOXIDIZE DEFECTS & MONITORING` -- Y: 26.7".

**BLOCK F -- Two-Column (Y: 27.3" to 32.3")**

**Left -- Monitoring Table:**

| Parameter | Method | Frequency |
|---|---|---|
| Acid concentration | Titration (HNO3) | Every 4 hours |
| Fluoride (if HF used) | Specific ion electrode | Daily |
| Dissolved metals | Lab analysis | Weekly |
| Temperature | Thermocouple | Continuous |
| Visual check | Surface brightness | Every load |

**Right -- Deoxidize Defects:**

| Defect | Cause | Fix |
|---|---|---|
| Residual smut (dark surface) | Wrong deoxidizer for alloy; acid depleted | Match deox to alloy; replenish acid |
| Over-etched / rough surface | Excess HF; too long; too hot | Reduce HF; shorten time; maintain ambient |
| Pitting | Excess HF; chloride contamination | Reduce HF; check acid purity |
| Uneven deox | Mixed alloys in load; uneven cleaning upstream | Separate alloys; improve cleaning |
| Bare spots in chromate downstream | Incomplete deox; re-oxidized before coating | Improve deox; minimize transit time |

---

### ZONE 7 -- Footer

Standard Cr(VI) footer.

**Disclaimer:**
> This poster is an educational reference tool. Hexavalent chromium (Cr6+) is a known human carcinogen. Process parameters shown are typical industry values for deoxidizing aluminum prior to hex chromate conversion coating per MIL-DTL-5541 Type I. Specific formulations vary by product. Consult your process supplier and safety data sheets. Follow all applicable OSHA, EPA, and local regulations. HF (hydrofluoric acid) is extremely hazardous -- follow all HF safety protocols.

Title: `Deoxidize / Desmut -- Chromate Conversion (Hex)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deoxidize Desmut Chromate Conversion Hex -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The alloy-specific guide in Zone 5 is the unique value of this poster. Every aerospace shop processes multiple alloy families, and the deoxidize formula must match the alloy. The 4-card grid makes this decision tree visual and immediate -- green for easy (6xxx), amber for needs HF (2xxx, 7xxx), coral for difficult (cast Si). The HF safety note in the footer is mandatory -- hydrofluoric acid is one of the most dangerous chemicals in a finishing shop.

The re-oxidation time callout ("aluminum re-oxidizes in seconds") is the operational urgency that makes this stage time-critical. The poster should convey a sense of "act fast" once the deoxidize is complete.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #178 -- Construction Workup v1.0*
*2026-04-26*
