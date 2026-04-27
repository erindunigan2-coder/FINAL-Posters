---
Project: Plating Posters Inc
Poster Number: 216
Title: "Cleaning -- EN (Low Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 1: EN Low-P, Poster 2)"
Process Scope: Alkaline soak cleaning for electroless nickel low phosphorus line (Stage 1 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - LowPhosphorus
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEN-LP
---

# Poster #216 -- Construction Workup
## Cleaning -- EN (Low Phos)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of the EN Low-P process. Cleaning for electroless nickel is arguably more critical than for electrolytic processes. EN is autocatalytic -- the freshly deposited surface must catalyze the next layer. Any contamination that poisons the catalytic surface causes skip plating, and unlike electroplating you cannot force deposition with more current. If the cleaning is wrong, the EN bath simply refuses to plate.

Hero visual: a tank cross-section showing parts immersed in alkaline soak cleaner with agitation arrows and soil removal dynamics.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Tank cross-section hero (Block B):** Rectangular tank with parts on a rack, agitation arrows, temperature indicator, soil particles lifting off surfaces. Standard shape construction.
2. **Orientation strip (Block C):** 7-stage strip with Stage 1 highlighted.
3. **Full parameter table (Block D):** Deep-dive cleaning parameters including electrocleaning option.
4. **Common problems table (Block F):** 5 rows of cleaning-specific defects mapped to EN consequences.
5. **Safety callout (Block G):** Alkaline chemistry hazards + substrate-specific cautions.

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Standard locked palette and fonts per Poster #215.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2" / ~1.3" tall)
  Block C: 7-stage strip with Stage 1 highlighted

ZONE 3 -- TANK CROSS-SECTION HERO (4.2"--15.0" / ~10.8" tall)
  Block B: Soak clean tank diagram

ZONE 4 -- FULL PARAMETER TABLE (15.0"--22.0" / ~7.0" tall)
  Block D: Detailed cleaning parameters

ZONE 5 -- COMMON PROBLEMS & FIXES (22.0"--28.5" / ~6.5" tall)
  Block F: Cleaning-specific problem table

ZONE 6 -- SAFETY CALLOUT (28.5"--32.5" / ~4.0" tall)
  Block G: Alkaline cleaning safety + substrate cautions

ZONE 7 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `EN (Low Phos) -- Stage 1 of 7` -- Barlow SemiBold, 34 pt, `#2EC4B6` (Teal). X: 0.5", Y: 1.4".

**Tagline:** `EN is autocatalytic -- it plates itself. But only on a truly clean surface. Contamination does not reduce quality. It stops deposition entirely.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

**BLOCK C -- 7-Stage Strip**

Y: 3.0" to 4.1". Horizontal bar with 7 small boxes. Stage 1 fully opaque and highlighted; stages 2--7 dimmed.

- Container: Rounded rect, X: 0.5", Y: 3.0", W: 23.0", H: 1.0", fill `#252B3D`, radius 4
- Seven mini-boxes evenly spaced inside (each ~2.9" wide, 0.6" tall):

| Box | Label | Fill | Text Color | Opacity |
|---|---|---|---|---|
| 1 | `1 CLEAN` | `#2EC4B6` | `#1A1F2E` | 100% (highlighted) |
| 2 | `2 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 3 | `3 ACTIVATE` | `#3A4055` | `#F0EDE8` | 40% |
| 4 | `4 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 5 | `5 EN BATH` | `#3A4055` | `#F0EDE8` | 40% |
| 6 | `6 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 7 | `7 POST-TX` | `#3A4055` | `#F0EDE8` | 40% |

Label font: Barlow Condensed ExtraBold, 12 pt. Small right-pointing arrow between each box (1 pt, `#3A4055`).

Below strip: `Before: Incoming parts (as-received)` and `After: Oil-free, water-break-free surface ready for activation` -- Inter Regular, 12 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Tank Cross-Section Hero

**Section label:** `THE SOAK CLEAN TANK` -- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center. Y: 4.4".

**BLOCK B -- Tank Diagram**

Y: 5.0" to 14.5" (~9.5" tall).

Tank body:
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 8.0"
- Fill: `#252B3D` (representing cleaner solution)
- Border: 3 pt, `#C8D0D8` (tank walls)
- Corner radius: 4 pt

**Temperature indicator (left side):**
- Vertical bar, X: 2.5", Y: 6.0", W: 0.6", H: 6.5"
- Fill gradient: bottom 70% `#E05C5C` (hot), top 30% `#3A4055` (empty)
- Label: `60-80 C` -- JetBrains Mono Regular, 16 pt, `#E8A020`
- Sub-label: `(140-176 F)` -- JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%

**Parts on rack (center):**
- Horizontal bar (rack bar): X: 5.0", Y: 5.0", W: 14.0", H: 0.3", fill `#C8D0D8`
- 4-5 vertical rectangles (parts): W: 1.5", H: 4.0", fill `#3A4055`, border 2 pt `#C8D0D8`
- Spaced from X: 6.0" to X: 17.0"

**Agitation arrows:**
- 6-8 curved upward arrows around parts
- Stroke: 2 pt, `#2EC4B6`, dashed
- Represent convective cleaning action

**Soil particles lifting:**
- Small circles (0.15" dia) scattered above parts
- Fill: `#E8A020` at 40%
- 8-10 scattered between Y: 5.5" and Y: 7.0"

**Labels inside/around tank:**

Right side (X: 18.0", Y: 6.0"):
- `Alkaline Soak Cleaner` -- Barlow SemiBold 16 pt `#F0EDE8`
- `NaOH 30-60 g/L` -- JetBrains Mono 14 pt `#2EC4B6`
- `Na2CO3 15-30 g/L` -- JetBrains Mono 14 pt `#2EC4B6`
- `Surfactants 1-5 mL/L` -- JetBrains Mono 14 pt `#F0EDE8`
- `Time: 3-10 min` -- JetBrains Mono 14 pt `#F0EDE8`

Bottom label:
- `Agitation: Mechanical or air -- keeps cleaner in contact with soil` -- Inter Medium, 14 pt, `#F0EDE8`. Centered, Y: 13.8".

**Left callout (X: 0.5", Y: 10.0", W: 3.0"):**
- Rounded rect, fill `#1E2435`, border-left 0.06" `#2EC4B6`
- `KEY: Parts must be fully submerged. Air pockets trap soil and cause skip plating.`

**Right callout (X: 20.5", Y: 10.0", W: 3.0"):**
- Rounded rect, fill `#1E2435`, border-left 0.06" `#E8A020`
- `Electrocleaning option: cathodic then anodic, 3-6 V, 30-60 sec each`

---

### ZONE 4 -- Full Parameter Table

**Section label:** `CLEANING PARAMETERS -- DETAILED` -- Y: 15.2".

**Two-column layout:**

**Left -- Soak Clean (X: 0.5", W: 11.0"):**

Header: `SOAK CLEAN (STANDARD)` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Cleaner type | Alkaline soak (per supplier TDS) |
| NaOH | 30-60 g/L |
| Na2CO3 | 15-30 g/L |
| Surfactants | 1-5 mL/L (proprietary, non-foaming) |
| Temperature | 60-80 C (140-176 F) |
| Time | 3-10 min (soak); 1-3 min (electroclean) |
| Agitation | Air or mechanical |
| pH | 11-13 |

**Right -- Electroclean + Substrate Notes (X: 12.0", W: 11.5"):**

Header: `ELECTROCLEAN (OPTIONAL) + SUBSTRATE NOTES` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Cathodic clean | 3-6 V, 30-60 sec (H2 scrubbing) |
| Anodic clean | 3-6 V, 15-30 sec (smut removal) |
| Caution (HTS) | Cathodic = H absorption risk on >1000 MPa steel |
| Aluminum substrates | Non-etch cleaner (pH < 10.5) to avoid attack |
| Silicate cleaners | Must rinse thoroughly -- residue poisons EN catalysis |
| Water-break test | Visual: continuous film = clean; beading = contaminated |

Data: JetBrains Mono 13 pt. Labels: Inter Medium 13 pt at 60%. Rows alternate `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE CLEANING STAGE` -- Y: 22.2".

**5-row problem table (Y: 22.9" to 28.3"):**

Each row: rounded rect full width, H: 1.0", alternating fills, left accent 0.06" `#E05C5C`.

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Water break | Skip plating -- EN will not initiate | Residual oil; cleaner too weak or cold | Increase concentration or temp; extend time |
| Skip plating | Bare spots; no deposit on portions of part | Silicate residue from cleaner poisoning surface | Switch to silicate-free cleaner; improve rinse |
| Pitting in EN | Small pits in deposit | Oil micro-droplets carried through to EN bath | Carbon treat EN bath; improve agitation in cleaner |
| Poor adhesion | EN peels on bending or thermal shock | Oxide layer not removed; under-cleaning | Add electroclean step; check cleaner age |
| Rough deposit | Grainy or nodular EN surface | Particulate from dirty cleaner carried forward | Filter cleaner bath; replace if heavily loaded |

Column widths: Problem (3.5") | Symptom (5.0") | Cause (7.0") | Fix (7.5").

- Problem: Barlow SemiBold, 14 pt, `#E05C5C`
- Symptom: Inter Regular, 13 pt, `#E8A020`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Safety Callout

**Section label:** `SAFETY -- ALKALINE CLEANING CHEMISTRY` -- Barlow Condensed ExtraBold 24 pt `#E8A020`. Y: 28.7".

**Left -- Chemical Hazards (X: 0.5", W: 11.0"):**
- Rounded rect fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `CHEMICAL HAZARDS` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Bullets:
  - `NaOH: severe burns on contact -- pH > 12`
  - `Hot solution (140-176 F): thermal burn risk`
  - `Mist/vapor: respiratory irritant -- ensure ventilation`
  - `Never add water to concentrated cleaner -- add cleaner to water`
  - `Electrocleaning generates H2 gas -- explosion risk if unventilated`

**Right -- PPE Requirements (X: 12.0", W: 11.5"):**
- Rounded rect fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `REQUIRED PPE` -- Barlow SemiBold, 18 pt, `#E8A020`
- Bullets:
  - `Chemical splash goggles (minimum) or face shield`
  - `Chemical-resistant gloves (nitrile or neoprene)`
  - `Chemical-resistant apron`
  - `Eyewash station within 10 seconds travel`
  - `SDS posted and accessible at all times`

---

### ZONE 7 -- Footer Band

Standard footer:
- Footer background: `#0D1020`, Y: 32.5", H: 3.5"
- Disclaimer: `This poster is an educational reference tool...` (standard text referencing EN Low-P cleaning)
- Title: `Cleaning -- EN (Low Phos)`
- Series: `Plating Posters Inc -- Metal Finishing Reference Series`
- Logo placeholder, version `v1.0 -- 2026`

---

## Part 5 -- Grouping

| Group | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | 7-stage strip, Stage 1 highlighted |
| Zone 3 - Tank Hero | Section label, tank cross-section, labels, callouts |
| Zone 4 - Parameters | Section label, soak clean table, electroclean table |
| Zone 5 - Problems | Section label, 5-row problem table |
| Zone 6 - Safety | Section label, chemical hazards, PPE |
| Zone 7 - Footer | Standard footer |

---

## Part 6 -- Light Edition Color Remap Table

Standard remap (same as Poster #215). Tank walls `#C8D0D8` unchanged.

| Dark | Light |
|---|---|
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

---

## Part 7 -- Export Checklist

| File Name | Quality | Bleed |
|---|---|---|
| `Cleaning EN Low-P -- Dark -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning EN Low-P -- Dark -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning EN Low-P -- Dark -- Digital.pdf` | Standard | No |
| `Cleaning EN Low-P -- Light -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning EN Low-P -- Light -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning EN Low-P -- Light -- Digital.pdf` | Standard | No |

---

*Alaina -- Poster #216 -- Construction Workup v1.0 -- 2026-04-26*
