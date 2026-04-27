---
Project: Plating Posters Inc
Poster Number: 463
Title: "Electropolishing Stage"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7, Sections 7.1--7.5)"
Technical Source: Electropolishing main tank -- the core process stage. Phosphoric/sulfuric acid electrolyte for stainless steel. Covers polarity (part = anode), electrolyte composition, polishing plateau, current density, voltage control, and the viscous film mechanism. Most content-dense poster in the EP cluster.
Process Scope: Electropolishing -- main electropolishing tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Electropolishing
  - MainTank
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #463 -- Construction Workup
## Electropolishing Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the heart of the electropolishing cluster -- the main tank where anodic dissolution occurs. Comparable to Poster #36 (Zinc Alkaline Main Tank) in information density. The hero visual is a tank cross-section showing the reversed polarity (part = anode, not cathode), the viscous film layer, current flow, and electrolyte composition. The polishing plateau voltage-current relationship is the single most important control concept.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **EP tank cross-section hero (Block B):** Tank with workpiece as ANODE on both sides, cathode (Cu or Pb) in center or opposite, current flow reversed from plating posters, viscous film layer on workpiece surface.
2. **Electrolyte composition panel (Block D):** Two-component breakdown (H3PO4 + H2SO4) plus substrate-specific variants.
3. **Polishing plateau diagram (Block E):** Voltage-current curve showing the three regimes (etching, polishing, gas evolution).
4. **Defect grid (Block F):** 6 common EP failures.
5. **Surface finish results panel (Block G):** Ra values before and after.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- EP TANK HERO (4.2"--14.5" / ~10.3")
  Block B: Tank cross-section with reversed polarity
ZONE 4 -- ELECTROLYTE + POLISHING PLATEAU (14.5"--20.5" / ~6.0")
  Block D: Electrolyte composition
  Block E: Polishing plateau voltage-current explanation
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
  Block F: 6 common EP failures
ZONE 6 -- SURFACE FINISH RESULTS (26.5"--32.5" / ~6.0")
  Block G: Ra improvement data + Cr/Fe ratio enrichment
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROPOLISHING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `The Electropolishing Tank -- Stage 5 of 8 -- PART IS ANODE (+)` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Controlled anodic dissolution in phosphoric-sulfuric acid. Smoothing, brightening, and passive layer enrichment in one operation.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, oxide-free surface --> After: Smooth, bright, Cr-enriched passive surface`

---

### ZONE 3 -- EP Tank Hero

**Section label:** `THE ELECTROPOLISHING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (electrolyte solution)
- Border: 3 pt `#C8D0D8`

**Workpiece / ANODE (left and right sides):**
- Left workpiece: Vertical rect, X: 3.0", Y: 6.0", W: 1.5", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Right workpiece: Same, X: 19.5"
- Label above each: `ANODE (+) WORKPIECE` Barlow SemiBold 14 pt `#27AE60`
- Small label on surface: `Viscous film layer` Inter Regular 11 pt `#E8A020`

**Cathode (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#C8D0D8` at 30%, border 2 pt `#C8D0D8`
- Label above: `CATHODE (-) Cu or Pb` Barlow SemiBold 14 pt `#C8D0D8`
- Sub-label: `H2 gas evolved here` Inter Regular 11 pt `#F0EDE8` at 60%

**Current flow lines:**
- Curved arrows from workpiece (anode) OUTWARD toward cathode
- Stroke: 2 pt `#E8A020`, dashed
- Label: `Metal ions dissolve from anode surface` Inter Regular 12 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` labels on wires running to left and right workpieces (ANODE)
- `(-)` label on wire running to center cathode

**POLARITY REVERSAL CALLOUT (prominent):**
- Rounded rect, X: 5.0", Y: 12.5", W: 14.0", H: 1.0", fill `#E05C5C` at 20%, border 2 pt `#E05C5C`
- Text: `REVERSED POLARITY: The workpiece is the ANODE (+). Metal dissolves FROM the part. This is the opposite of electroplating.` Barlow SemiBold 14 pt `#E05C5C`

**Bath parameter labels (inside tank):**
Right side (X: 14.5", Y: 7.0"):
- `H3PO4: ~50% by vol` JetBrains Mono 14 pt `#27AE60`
- `H2SO4: ~30% by vol` JetBrains Mono 14 pt `#2EC4B6`
- `Temp: 65--80 C (150--175 F)` JetBrains Mono 14 pt `#F0EDE8`
- `CD: 10--20 A/dm2 (100--200 A/ft2)` JetBrains Mono 14 pt `#E8A020`
- `Voltage: 8--14 V` JetBrains Mono 14 pt `#E8A020`

Left side (X: 5.0", Y: 7.0"):
- `Time: 5--45 min` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Agitation: mild (do not disrupt film)` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Ripple: < 5%` JetBrains Mono 12 pt `#F0EDE8` at 70%
- `Cathode:anode ratio: 1:2 to 1:1` JetBrains Mono 12 pt `#F0EDE8` at 70%

---

### ZONE 4 -- Electrolyte + Polishing Plateau

**Section label:** `ELECTROLYTE CHEMISTRY + THE POLISHING PLATEAU` -- Y: 14.7".

**BLOCK D -- Electrolyte by Substrate (Y: 15.3" to 17.8")**

Table -- columns: Substrate (4.0") | Electrolyte (6.0") | Temp (3.0") | CD (3.5") | Voltage (3.0") | Notes (3.5")

| Substrate | Electrolyte | Temp | CD | Voltage | Notes |
|---|---|---|---|---|---|
| 300-series SS (304, 316) | H3PO4 50% + H2SO4 30% | 65--80 C | 10--20 A/dm2 | 8--14 V | Standard industrial EP |
| 400-series SS (410, 430) | H3PO4 + H2SO4 + glycerol | 50--80 C | 5--20 A/dm2 | 6--15 V | More sensitive to etching |
| Carbon steel | H3PO4 + H2SO4 | 50--80 C | 10--30 A/dm2 | 8--18 V | Higher CD needed |
| Copper alloys | H3PO4 60--85% (alone) | 20--50 C | 5--30 A/dm2 | 1--6 V | Lower temp, lower voltage |
| Nickel alloys | H2SO4 + citric/glycolic | 50--80 C | 5--15 A/dm2 | 8--18 V | Proprietary blends |

**BLOCK E -- Polishing Plateau Explanation (Y: 18.2" to 20.3")**

Full-width rounded rect, H: 2.0", fill `#1E2435`, left accent `#E8A020`.

Title: `THE THREE VOLTAGE REGIMES` Barlow SemiBold 18 pt `#E8A020`

Three-segment horizontal bar (X: 1.0", W: 22.0", H: 0.5"):
- Segment 1 (left ~25%): fill `#E05C5C` at 40%, label `ETCHING` above, `Low voltage: active dissolution, matte surface -- NOT polishing` below
- Segment 2 (center ~50%): fill `#27AE60` at 50%, label `POLISHING PLATEAU` above, `Current constant despite voltage increase -- operate HERE` below
- Segment 3 (right ~25%): fill `#E05C5C` at 40%, label `GAS EVOLUTION` above, `O2 bubbles: pitting, streaks, gas marks` below

Bottom note: `Always run a test coupon to locate the polishing plateau for your specific electrolyte and substrate combination.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON EP DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid (Y: 21.3" to 26.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | PITTING | `#E05C5C` | Above polishing plateau (O2); Cl- contamination; MnS inclusions (303 SS) | Verify voltage on plateau; test for Cl-; avoid 303 SS |
| R1C2 | ORANGE PEEL | `#E8A020` | Below polishing plateau; insufficient time; grain boundary etching | Increase voltage to plateau; extend time |
| R1C3 | STREAKING | `#E8A020` | Non-uniform current; gas entrapment on surface | Reposition parts; tilt for gas escape; improve cathode placement |
| R2C1 | STAINING | `#E05C5C` | Slow removal; iron contamination in electrolyte; poor rinse | Immediate rinse; maintain electrolyte purity; quick transfer |
| R2C2 | UNEVEN FINISH | `#2EC4B6` | Poor electrical contact; fixture shielding; part spacing | Check contacts; redesign fixture; increase spacing |
| R2C3 | ETCHING (MATTE) | `#E05C5C` | Solution too hot; too concentrated; excessive current | Check temperature; analyze solution; verify on plateau |

Each card: W: 7.33", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 6 -- Surface Finish Results

**Section label:** `SURFACE FINISH RESULTS` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.0"):**

**Left -- Ra Improvement (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `SURFACE ROUGHNESS IMPROVEMENT` Barlow SemiBold 18 pt `#27AE60`

| Starting Ra | After EP Ra | Improvement |
|---|---|---|
| 0.8 um (32 uin) | 0.2--0.4 um (8--16 uin) | 50--75% |
| 0.4 um (16 uin) | 0.1--0.2 um (4--8 uin) | 50--75% |
| 0.2 um (8 uin) | 0.05--0.1 um (2--4 uin) | ~50% |

Bottom: `Best achievable: Ra 0.05 um (2 uin) with excellent starting surface` JetBrains Mono 12 pt `#27AE60`

**Right -- Cr/Fe Ratio Enrichment (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `PASSIVE LAYER ENRICHMENT` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
Cr/Fe surface ratio:
  Mechanically polished: ~0.4
  After electropolishing: 1.0--1.5

EP preferentially dissolves iron, enriching
chromium in the passive oxide layer.

This is why pharma and semiconductor specify EP:
  - Enhanced corrosion resistance
  - Reduced particle shedding
  - Smoother surface = easier to clean
```

Standards: `ASTM B912 | ASME BPE SF4 | SEMI F19` JetBrains Mono 12 pt `#F0EDE8` at 60%

---

### ZONE 7 -- Footer

Standard. Title: `Electropolishing Stage`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM B912; ASME BPE; typical H3PO4/H2SO4 electrolyte parameters for stainless steel. Proprietary electrolyte formulations vary.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Electropolishing Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP cluster -- comparable to Poster #36 (Zinc Main Tank). The polarity reversal callout in the tank hero must be impossible to miss. The polishing plateau (Block E) is the most critical operational concept -- if the operator does not understand the three voltage regimes, everything else is irrelevant. The Cr/Fe enrichment data (Zone 6) is what elevates EP from "just polishing" to a passivation-enhancing surface treatment. No perchloric acid anywhere.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #463 -- Construction Workup v1.0*
*2026-04-26*
