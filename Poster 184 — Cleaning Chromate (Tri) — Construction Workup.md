---
Project: Plating Posters Inc
Poster Number: 184
Title: "Cleaning -- Chromate (Tri)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.2)"
Technical Source: Alkaline cleaning for trivalent chromate conversion coating on aluminum. Identical requirements to hex chromate cleaning (CC-04 Section 4.2). Non-etch or mildly alkaline, silicate-inhibited. Stage 1 of 7.
Process Scope: Alkaline cleaning -- Stage 1 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Cleaning
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #184 -- Construction Workup
## Cleaning -- Chromate (Tri)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 7. Cleaning for trivalent chromate on aluminum. The critical message: aluminum is reactive -- you cannot use the same aggressive cleaners you would on steel. Silicate-inhibited, non-etch alkaline cleaners are the standard. The tri chromate bath downstream is LESS forgiving of contamination than hex, so cleaning must be thorough.

Hero visual: a cleaning tank cross-section showing immersion of an aluminum workpiece with labeled chemistry zones and contaminant removal action.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank with aluminum workpiece submerged, contaminant particles lifting off surface, chemistry labels inside tank. Built with rectangles, lines, and small circles/arrows.
2. **Cleaner selection decision panel (Block D):** What cleaner type for which situation -- non-etch vs. inhibited alkaline vs. fluoride-bearing.
3. **"Aluminum Is Different" callout (Block E):** Why you cannot use steel-line cleaners on aluminum -- single most important teaching point.
4. **Defect grid (Block F):** 4 common cleaning failures and their downstream effects on the tri chromate coat.

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
ZONE 4 -- CLEANER SELECTION + ALUMINUM RULES (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Stage 1 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Aluminum is not steel. Use the wrong cleaner and you will etch, smut, and ruin everything downstream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2". Seven-stage strip with Stage 1 highlighted.

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed: fill `#252B3D`, text `#F0EDE8` at 40%.

Stages: `1. Clean` | `2. Rinse` | `3. Deox` | `4. Rinse` | `5. Tri Coat` | `6. Rinse` | `7. Dry`

Below strip: `Before: Aluminum with oils, oxide, shop soils  -->  After: Clean, water-break-free aluminum surface`
Inter Medium 14 pt `#F0EDE8` at 60%.

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE CLEANING STAGE` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (cleaning solution)
- Border: 3 pt `#C8D0D8`

**Aluminum workpiece (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.5", fill `#C8D0D8` at 30%, border 2 pt `#C8D0D8`
- Label above: `ALUMINUM WORKPIECE` Barlow SemiBold 14 pt `#C8D0D8`

**Contaminant particles lifting off (both sides of workpiece):**
- 6--8 small circles (0.15" diameter) in `#E05C5C` at 50%, positioned near workpiece surface, with small upward arrows showing removal action
- Label: `Oils, soils, fingerprints, shop contaminants lifting off` Inter Regular 12 pt `#F0EDE8` at 60%

**Solution chemistry labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `Non-etch alkaline cleaner` Barlow SemiBold 14 pt `#2EC4B6`
- `pH 9--11` JetBrains Mono 14 pt `#2EC4B6`
- `120--160 F (49--71 C)` JetBrains Mono 14 pt `#F0EDE8`
- `3--10 min immersion` JetBrains Mono 14 pt `#F0EDE8`

Left side (X: 2.5", Y: 7.0"):
- `Surfactants emulsify oils` Inter Regular 13 pt `#F0EDE8` at 70%
- `Alkalinity saponifies greases` Inter Regular 13 pt `#F0EDE8` at 70%
- `Silicate inhibitors protect Al` Inter Regular 13 pt `#27AE60`

**Spray alternative note (below tank, Y: 13.2"):**
- `Spray alternative: 2--4 oz/gal, 100--140 F, 1--3 min. Lower concentration, lower temp, shorter time.`
- JetBrains Mono 12 pt `#F0EDE8` at 60%

**Bottom callout (Y: 13.8"):**
- `The goal: water-break-free surface. If water beads on the part after rinse, the surface is still contaminated.`
- Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaner Selection + Aluminum Rules

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Cleaner Selection Guide (X: 0.5", W: 11.0"):**

Section label: `CLEANER SELECTION` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

Three stacked callout boxes (Y: 15.3" to 20.0"):

| Cleaner Type | Accent | Use Case | Notes |
|---|---|---|---|
| Non-Etch Alkaline (pH 9--11) | `#27AE60` | Standard for most aluminum alloys | Preferred default for tri chromate lines |
| Inhibited Alkaline (silicate) | `#2EC4B6` | Heavy soils on wrought alloys | Silicate inhibits aluminum attack |
| Fluoride-Bearing | `#E8A020` | Cast alloys with heavy oxide | Carefully controlled -- excess F- pits aluminum |

Each box: Rounded rect, H: 1.4", fill `#1E2435`, left accent 0.06".
Cleaner type: Barlow SemiBold 16 pt in accent color. Use case: Inter Regular 13 pt `#F0EDE8`. Notes: Inter Medium 12 pt `#F0EDE8` at 70%.

**Right -- "Aluminum Is Different" Warning (X: 12.0", W: 11.5"):**

Section label: `ALUMINUM IS DIFFERENT` Barlow Condensed ExtraBold 22 pt `#E05C5C`. Y: 14.7".

Warning callout box: Rounded rect, Y: 15.3", H: 4.8", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Strongly caustic cleaners (NaOH > 5%) aggressively etch aluminum -- producing a dark smut layer that is difficult to remove`
- `Steel-line cleaners are NOT compatible -- they will dissolve the aluminum surface`
- `Silicate-containing cleaners are preferred -- but silicate residues must be fully rinsed before phosphate or chromate stages`
- `Fluoride cleaners: effective but risky. Excess fluoride pits aluminum alloys, especially 2xxx and 7xxx series`

Bottom rule:
- `RULE: If you would not put your hand in it, do not put aluminum in it without checking the TDS.` Inter Medium 14 pt `#E8A020`

---

### ZONE 5 -- Operating Parameters Table

**Section label:** `OPERATING PARAMETERS` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 20.7".

**Parameter table (Y: 21.3" to 26.3"):**

Column widths (23.0" total):
- Parameter (4.0") | Immersion (5.0") | Spray (5.0") | Control Method (9.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Parameter | Immersion | Spray | Control Method |
|---|---|---|---|
| Concentration | 4--8 oz/gal (30--60 g/L) | 2--4 oz/gal (15--30 g/L) | Titration (free alkalinity) |
| Temperature | 120--160 F (49--71 C) | 100--140 F (38--60 C) | Thermocouple; heater interlock |
| Time | 3--10 min | 1--3 min | Timer; watch for over-etch |
| pH | 9--11 | 9--11 | pH meter; adjust with cleaner adds |
| Water break test | Must pass after rinse | Must pass after rinse | Visual; water sheets uniformly = pass |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Row height: 0.8". Alternating `#1E2435` / `#252B3D`.

---

### ZONE 6 -- Defect Diagnosis

**Section label:** `WHAT GOES WRONG -- 4 CLEANING FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 26.7".

**4-card row (Y: 27.3" to 32.3"):**

Each card: Rounded rect, W: 5.5", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Downstream Effect |
|---|---|---|---|---|
| 1 | 0.5" | OIL RESIDUE | Insufficient concentration or time | Skip areas in chromate coat |
| 2 | 6.33" | ALUMINUM ETCH | Cleaner too caustic or too hot | Heavy smut; poor deox; patchy coating |
| 3 | 12.16" | SILICATE RESIDUE | Over-concentration; poor rinse | Inhibits chromate film deposition |
| 4 | 18.0" | WATER BREAK FAIL | Contaminated part or contaminated rinse | Entire downstream process compromised |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Downstream: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- Chromate (Trivalent)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for alkaline cleaning of aluminum prior to trivalent chromate conversion coating. Consult your process supplier for product-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Chromate Tri -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "Aluminum Is Different" warning is the teaching centerpiece. Many shops transitioning from steel plating lines make the mistake of using their existing cleaners on aluminum. This poster should make the consequences viscerally clear. The downstream effect column in the defect cards reinforces that cleaning failures cascade through every subsequent stage.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #184 -- Construction Workup v1.0*
*2026-04-26*
