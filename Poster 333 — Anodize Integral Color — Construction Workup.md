---
Project: Plating Posters Inc
Poster Number: 333
Title: "Anodize -- Integral Color"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.7)"
Technical Source: Industry-standard integral color anodizing main tank. Mixed acid electrolyte (sulfuric + organic acids) at high voltage. Color forms in the oxide from organic acid decomposition products. Formulations are largely proprietary -- poster focuses on mechanism and general parameter ranges.
Process Scope: Integral color anodizing -- Stage 6 of 8 (Anodize -- Main Tank)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - MainTank
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #333 -- Construction Workup
## Anodize -- Integral Color

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8 (mapped to poster stage "Anodize -- Main Tank"). This is the heart of integral color -- where the magic happens. The electrolyte is a mixture of sulfuric acid and organic acids (oxalic, sulfosalicylic, sulfophthalic). At high voltage (50--80 V), the organic acids decompose and their byproducts incorporate into the growing oxide, producing color. This is the most content-dense poster in the cluster.

Hero visual: anodize tank cross-section showing the mixed acid electrolyte, the high-voltage power supply, and a color gradient strip showing how alloy + time + voltage = color depth.

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
  Stage 6 highlighted (Emerald)
ZONE 3 -- ANODIZE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- COLOR MECHANISM + ELECTROLYTE CHEMISTRY (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- COLOR CONTROL CHALLENGES + ALLOY EFFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INTEGRAL COLOR ANODIZE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Main Tank -- Stage 6 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Where color is born. High voltage drives organic acid decomposition into the growing oxide -- no dye, no second step. The color IS the coating.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, desmutted aluminum --> After: Colored anodic oxide, 15--30 um thick, bronze to black`

---

### ZONE 3 -- Anodize Tank Hero

**Section label:** `THE INTEGRAL COLOR ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (electrolyte)
- Border: 3 pt `#C8D0D8`

**Cathode material labels:**
- Left and right: `CATHODE (Al or Pb-Sb)` Barlow SemiBold 12 pt `#C8D0D8`
- Vertical rects representing cathode plates

**Anode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#E8A020` at 25%, border 2 pt `#E8A020`
- Label above: `ANODE (WORKPIECE)` Barlow SemiBold 14 pt `#E8A020`
- Small annotation: `Color developing in oxide` Inter Regular 11 pt `#E8A020`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER  50--80 V` Barlow SemiBold 12 pt `#E8A020`
- Note: In anodizing the workpiece is the ANODE (positive terminal)

**Bath parameter labels (inside tank):**

Right side (X: 15.0", Y: 7.0"):
- `H2SO4: 100--180 g/L` JetBrains Mono 14 pt `#F0EDE8`
- `Oxalic acid: 5--20 g/L` JetBrains Mono 14 pt `#E8A020`
- `Sulfosalicylic: 10--40 g/L` JetBrains Mono 14 pt `#E8A020`
- `Temp: 59--77 F (15--25 C)` JetBrains Mono 14 pt `#2EC4B6`

Left side (X: 4.0", Y: 7.0"):
- `Voltage: 50--80 V` JetBrains Mono 16 pt `#E8A020` (larger -- hero metric)
- `CD: 10--20 ASF (1.0--2.0 A/dm2)` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 20--45 min` JetBrains Mono 13 pt `#F0EDE8`
- `Thickness: 15--30 um (0.6--1.2 mil)` JetBrains Mono 13 pt `#27AE60`

**Color Gradient Strip (Y: 12.0"):**
- Horizontal strip, X: 2.0", W: 20.0", H: 0.8"
- Gradient from light bronze (`#C4A35A`) through medium bronze (`#8B6914`) to dark brown/black (`#3D2B1F` to `#1A1008`)
- Labels below: `20 min / Light Bronze` ... `30 min / Medium Bronze` ... `45 min / Dark Brown-Black`
- JetBrains Mono 11 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `50--80 V is 3--5x higher than standard Type II (15--18 V). This high voltage drives the organic acid decomposition that creates color.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Color Mechanism + Electrolyte Chemistry

**Section label:** `HOW COLOR FORMS -- THE MECHANISM` -- Y: 14.7".

**Left (X: 0.5", W: 11.0") -- Color Development Mechanism:**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `COLOR DEVELOPMENT -- STEP BY STEP` Barlow SemiBold 18 pt `#E8A020`.

Numbered steps (Inter Regular 14 pt `#F0EDE8`, line height 170%):

1. `Organic acids (oxalic, sulfosalicylic) present in the electrolyte`
2. `High voltage (50--80 V) causes decomposition at the pore base`
3. `Carbon-containing decomposition products incorporate into the growing oxide`
4. `These incorporated species create light-absorbing centers throughout the oxide`
5. `Color darkens with increasing thickness, higher voltage, and longer time`
6. `Alloy elements (Mn, Cu, Fe) contribute additional color effects`

Key insight (Amber box):
- `The color is EMBEDDED in the oxide structure. It cannot fade from UV exposure the way organic dyes do. 30+ year outdoor durability.` Inter Medium 13 pt `#E8A020`

**Right (X: 12.0", W: 11.5") -- Electrolyte Components:**

Three stacked callout boxes:

*Component 1 -- Sulfuric Acid (base):*
- Left accent `#F0EDE8`
- `H2SO4: 100--180 g/L (13--24 oz/gal)` JetBrains Mono 14 pt
- `Base electrolyte -- same acid used in standard Type II`
- `Provides conductivity and drives oxide growth`

*Component 2 -- Oxalic Acid (color agent):*
- Left accent `#E8A020`
- `C2H2O4: 5--20 g/L` JetBrains Mono 14 pt
- `Most common additive for integral color`
- `Decomposes at high voltage; byproducts create color`

*Component 3 -- Sulfosalicylic Acid (color agent):*
- Left accent `#E8A020`
- `10--40 g/L` JetBrains Mono 14 pt
- `Used in Kalcolor-type proprietary processes`
- `Alternative or combined with oxalic acid`

Note: `Formulations are PROPRIETARY. Specific ratios, additives, and operating windows vary by supplier. These ranges are representative.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**3x2 Grid:**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | COLOR VARIATION (PART-TO-PART) | `#E05C5C` | Alloy chemistry variation (heat-to-heat) | Match alloy lots; tag racks by heat |
| R1C2 | COLOR VARIATION (BATCH) | `#E05C5C` | Temperature drift; dissolved Al drift | Tighten temp +/- 1 C; test dissolved Al |
| R1C3 | PITTING | `#E05C5C` | Chloride > 25 ppm in electrolyte | Monitor rinse water; test bath chloride |
| R2C1 | BURNING | `#E8A020` | Excessive CD at edges/protrusions | Reduce CD; check voltage; improve racking |
| R2C2 | CHALKING | `#2EC4B6` | Surface degradation (typically 20+ years) | Normal aging; not a process defect |
| R2C3 | FADING (RARE) | `#E8A020` | May not be true integral color | Verify process; true integral does not fade |

---

### ZONE 6 -- Color Control Challenges + Alloy Effects

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Color Control Challenges:**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.
Title: `THE #1 QUALITY CHALLENGE` Barlow SemiBold 18 pt `#E05C5C`.
Subtitle: `Alloy-Driven Color Variation` Inter Medium 14 pt `#F0EDE8`.

Bullets (Inter Regular 14 pt `#F0EDE8`):
- `Heat-to-heat alloy chemistry variation causes color shifts`
- `Different extrusion dies produce different grain structures`
- `Different grain structures = different integral colors on the same rack`
- `Temperature +/- 1 C produces visible color difference`
- `Dissolved Al affects shade: fresh bath vs. aged bath differs`
- `Color matching: CIE L*a*b* per ASTM D2244; dE < 1.0 for architectural`

**Right -- Alloy Color Chart:**

| Alloy | Typical Integral Color Range | Notes |
|---|---|---|
| 6063 | Light bronze to dark bronze | Architectural standard; best color uniformity |
| 5005 | Light bronze to medium bronze | Good match with 6063 |
| 6061 | Medium bronze to dark brown | Slightly different shade than 6063 |
| 3003 | Tan to yellowish-brown | Manganese affects color |
| 2024 | Dark brown to black | Copper darkens oxide; not typical for integral |

JetBrains Mono 12 pt for colors. "Architectural standard" in `#27AE60`.

Note: `6063 and 5005 are the only alloys routinely specified for architectural integral color. All other alloys produce unpredictable colors.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Anodize -- Integral Color`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5. Specific integral color formulations (Kalcolor, Duranodic, Permalux) are proprietary. Parameters shown are representative ranges. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize Integral Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the integral color cluster. The voltage (50--80 V) is the hero metric -- visually emphasize that this is 3--5x higher than standard Type II. The color gradient strip is a key visual showing the time-to-color relationship. The alloy color chart directly addresses the #1 quality challenge in architectural integral color work.

---

*Alaina -- Poster #333 -- Construction Workup v1.0 -- 2026-04-26*
