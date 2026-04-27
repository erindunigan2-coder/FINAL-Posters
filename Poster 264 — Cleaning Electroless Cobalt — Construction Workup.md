---
Project: Plating Posters Inc
Poster Number: 264
Title: "Cleaning -- Electroless Cobalt"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt, Poster 2)"
Technical Source: Alkaline soak clean and electroclean protocols for electroless cobalt substrates. Same fundamental cleaning chemistry as all electroless processes -- substrate cleanliness is the gatekeeper for autocatalytic initiation. Parameters from Watson domain expertise.
Process Scope: Cleaning stage (Stage 1 of 8) for electroless cobalt plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #264 -- Construction Workup
## Cleaning -- Electroless Cobalt

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for electroless cobalt follows the same universal electroless cleaning protocols -- the substrate must be catalytically active for the autocatalytic reaction to initiate. Any residual oil, oxide, or soil means skip plating. This poster covers alkaline soak clean, optional electrocleaning, and substrate-specific considerations (steel, copper, silicon wafers, plastics).

Hero visual: cleaning tank cross-section showing immersion soak with agitation, temperature probe, and water-break-free test illustration.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank with parts immersed, air agitation bubbles, heater element, and temperature probe. Built with rectangles, lines, and small circles for bubbles.
2. **Cleaning methods comparison (Block D):** Three-column layout -- Soak Clean, Cathodic Electroclean, Anodic Electroclean.
3. **Substrate-specific callouts (Block E):** Four callout boxes for steel, copper/brass, silicon wafers, and plastics.
4. **Critical quality checks (Block F):** Water-break-free test visual + silicate warning.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING METHODS COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- SUBSTRATE-SPECIFIC NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- CRITICAL QUALITY CHECKS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Cobalt -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Every electroless failure starts with a dirty part. The autocatalytic reaction demands a catalytically active surface -- cleaning is non-negotiable.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Incoming substrate (oils, oxides, shop soils)  -->  After: Water-break-free surface ready for activation`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE SOAK CLEAN` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (cleaning solution)
- Border: 3 pt `#C8D0D8`

**Parts on rack (center):**
- 3 vertical rects representing substrates on a rack, X: 9.0"--15.0", Y: 6.5", W: 0.5" each, H: 4.5", fill `#C8D0D8` at 50%, border 1 pt `#3A4055`
- Rack bar across top: horizontal rect, X: 8.5", Y: 6.0", W: 7.0", H: 0.3", fill `#C8D0D8`
- Label above rack: `SUBSTRATE ON RACK` Barlow SemiBold 14 pt `#F0EDE8`

**Air agitation (bottom):**
- Row of small circles (0.15" diameter) across bottom of tank, fill `#2EC4B6` at 30%
- Label: `Air agitation` Inter Regular 12 pt `#2EC4B6`

**Heater element (right side):**
- Zigzag line, X: 19.0", Y: 7.0" to 11.0", stroke 2 pt `#E05C5C`
- Label: `Heater` Inter Regular 11 pt `#E05C5C`

**Bath parameter labels (inside tank):**
Left side (X: 2.5", Y: 7.0"):
- `NaOH: 30--60 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Na2CO3: 15--30 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Surfactant: 1--5 mL/L` JetBrains Mono 14 pt `#2EC4B6`
- `Temp: 140--176 F (60--80 C)` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 3--10 min (soak)` JetBrains Mono 14 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `Alkaline soak cleaning is universal across all electroless processes. The chemistry is identical whether plating Co, Ni, Cu, Pd, or Au.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaning Methods Comparison

**Section label:** `THREE CLEANING METHODS` -- Y: 14.7".

**BLOCK D -- Three-Column Layout (Y: 15.3" to 20.3")**

| Method | X | W | Accent | Title |
|---|---|---|---|---|
| Soak Clean | 0.5" | 7.33" | `#2EC4B6` | SOAK CLEAN |
| Cathodic Electroclean | 8.0" | 7.33" | `#E8A020` | CATHODIC ELECTROCLEAN |
| Anodic Electroclean | 15.5" | 8.0" | `#27AE60` | ANODIC ELECTROCLEAN |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*Soak Clean:*
- `3--10 minutes immersion` JetBrains Mono 16 pt `#2EC4B6`
- `Agitation: air or mechanical`
- `No electrical connection required`
- `Standard for most production`
- `Lowest equipment cost`

*Cathodic Electroclean:*
- `3--6 V, 30--60 seconds` JetBrains Mono 16 pt `#E8A020`
- `H2 generated at part surface`
- `Scrubbing action lifts tenacious soils`
- `CAUTION: H absorption in high-strength steel` (`#E05C5C`)
- `If substrate >1000 MPa UTS: use anodic only`

*Anodic Electroclean:*
- `3--6 V, 15--30 seconds` JetBrains Mono 16 pt `#27AE60`
- `O2 generated at part surface`
- `Removes smut and embedded particles`
- `Use after cathodic to remove absorbed H`
- `Preferred for high-strength substrates`

---

### ZONE 5 -- Substrate-Specific Notes

**Section label:** `SUBSTRATE CONSIDERATIONS` -- Y: 20.7".

**BLOCK E -- 2x2 Grid of Callout Boxes (Y: 21.3" to 26.3")**

| Position | Substrate | Accent | Key Note |
|---|---|---|---|
| R1C1 | Steel / Iron | `#2EC4B6` | Standard alkaline clean; steel is catalytic for Co -- inherent initiation on clean surface |
| R1C2 | Copper / Brass | `#27AE60` | Standard alkaline clean; Cu is catalytic for Co; bright dip if heavily tarnished (dilute HNO3 + H2SO4) |
| R2C1 | Silicon Wafers (MEMS) | `#E8A020` | Solvent pre-clean (acetone/IPA), then dilute alkaline or RCA clean; avoid aggressive alkaline on thin wafers |
| R2C2 | Plastics (ABS, PC) | `#E05C5C` | No alkaline soak -- use proprietary plastic conditioner; etch step follows (chromic/sulfuric or permanganate) |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 6 -- Critical Quality Checks

**Section label:** `QUALITY GATES -- DO NOT SKIP` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Water-Break-Free Test (X: 0.5", W: 11.0"):**
- Visual: simplified part outline with water sheet flowing evenly (no beading)
- `PASS: Water sheets uniformly -- no breaks, no beading` Inter Medium 14 pt `#27AE60`
- `FAIL: Water beads or breaks = residual contamination` Inter Medium 14 pt `#E05C5C`
- `This is the single most important visual QC test in electroless plating prep` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Cleaner Compatibility Warnings (X: 12.0", W: 11.5"):**

| Warning | Detail |
|---|---|
| Silicate residues | Poison catalytic surfaces -- rinse thoroughly if silicate-based cleaner used |
| Foaming agents | Must use non-foaming type if followed by electroclean |
| Aluminum cleaners | Use non-etch (pH <10.5) to prevent surface attack |
| Cobalt-specific | No unique cleaner requirements vs. EN -- same protocols apply |

Warning labels in `#E05C5C`. Detail in `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Electroless Cobalt`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; electroless plating cleaning protocols are universal across all autocatalytic processes.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Electroless Cobalt -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cleaning for electroless cobalt is fundamentally identical to cleaning for any electroless process. The poster's unique value is (1) placing cleaning in the context of the cobalt line specifically, (2) the substrate-specific callouts (especially silicon wafers for MEMS -- unique to cobalt among our poster set), and (3) reinforcing that the water-break-free test is the universal quality gate. Watson's flag #8 recommends visual consistency across "support step" posters -- this cleaning poster should match the layout template of other electroless cleaning posters.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #264 -- Construction Workup v1.0*
*2026-04-26*
