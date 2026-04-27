---
Project: Plating Posters Inc
Poster Number: 96
Title: "Cleaning -- Copper (Acid)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Cleaning stage for acid copper sulfate plating line (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - CopperPlating
  - AcidCopper
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ClusterEP09
---

# Poster #96 -- Construction Workup
## Cleaning -- Copper (Acid)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of the acid copper process. Cleaning for acid copper is substrate-dependent -- steel requires a strike (cyanide or alkaline non-cyanide copper) before acid copper, while copper/brass/nickel substrates can go directly into the acid bath. PCBs use a completely different cleaning sequence (microetch, no alkaline). This poster covers the standard cleaning approach for metallic substrates, with callouts for the PCB and steel-with-strike pathways.

Hero visual: a tank cross-section showing parts immersed with agitation arrows, temperature indicator, and soil removal dynamics.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Tank cross-section hero (Block B):** Standard cleaning tank diagram with parts, rack, agitation arrows, temperature bar, soil particles.
2. **Orientation strip (Block C):** Stage 1 highlighted.
3. **Two-column parameter table (Block D):** Left = Soak Clean, Right = Electroclean.
4. **Substrate pathway callout (Block E):** Three-path decision diagram (copper/brass direct, steel with strike, PCB microetch).
5. **Problems table + Safety callout.**

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Fonts and colors: same locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Block C: 8-stage strip with Stage 1 highlighted

ZONE 3 -- TANK CROSS-SECTION HERO (4.2"--14.5" / ~10.3" tall)
  Block B: Soak clean tank diagram

ZONE 4 -- PARAMETER TABLES (14.5"--21.0" / ~6.5" tall)
  Block D: Soak clean + Electroclean parameters

ZONE 5 -- SUBSTRATE PATHWAYS + PROBLEMS (21.0"--27.0" / ~6.0" tall)
  Block E: Three substrate pathways
  Block F: Common cleaning problems

ZONE 6 -- SAFETY CALLOUT (27.0"--32.5" / ~5.5" tall)
  Block G: Chemical safety panel

ZONE 7 -- FOOTER BAND (32.5"--36.0")
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `Copper (Acid) -- Stage 1 of 8` -- Barlow SemiBold, 34 pt, `#2EC4B6` (Teal). X: 0.5", Y: 1.4".

**Tagline:** `Acid copper is forgiving. Contamination is not. Every defect in the acid copper tank traces back to cleaning.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

**BLOCK C -- 8-Stage Strip**

Y: 3.0" to 4.1". Horizontal bar with 8 small boxes. Stage 1 fully highlighted; stages 2--8 dimmed.

- Container: Rounded rect, X: 0.5", Y: 3.0", W: 23.0", H: 1.0", fill `#252B3D`, radius 4

| Box | Label | Fill | Text Color | Opacity |
|---|---|---|---|---|
| 1 | `1 CLEAN` | `#2EC4B6` | `#1A1F2E` | 100% (highlighted) |
| 2 | `2 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 3 | `3 ACTIVATE` | `#3A4055` | `#F0EDE8` | 40% |
| 4 | `4 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 5 | `5 PLATE` | `#3A4055` | `#F0EDE8` | 40% |
| 6 | `6 RINSE` | `#3A4055` | `#F0EDE8` | 40% |
| 7 | `7 TREAT` | `#3A4055` | `#F0EDE8` | 40% |
| 8 | `8 DRY` | `#3A4055` | `#F0EDE8` | 40% |

Label font: Barlow Condensed ExtraBold, 12 pt. Small right-pointing arrow between each box (line, 1 pt, `#3A4055`).

Below strip: `Before: Incoming parts (as-received)  -->  After: Oil-free, oxide-free surface ready for activation`

---

### ZONE 3 -- Tank Cross-Section Hero

**Section label:** `THE SOAK CLEAN TANK` -- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center. Y: 4.4".

**BLOCK B -- Tank Diagram**

Y: 5.0" to 14.0".

Tank body:
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.5"
- Fill: `#252B3D` (representing cleaner solution)
- Border: 3 pt, `#C8D0D8`

Temperature indicator (left side):
- Vertical bar, X: 2.5", Y: 6.0", W: 0.6", H: 6.0"
- Fill gradient: bottom 70% `#E05C5C`, top 30% `#3A4055`
- Label: `140--180 F` -- JetBrains Mono 16 pt `#E8A020`
- Sub-label: `(60--82 C)` -- JetBrains Mono 12 pt `#F0EDE8` at 60%

Parts on rack (center):
- Horizontal bar: X: 5.0", Y: 5.0", W: 14.0", H: 0.3", fill `#C8D0D8`
- 4 vertical rectangles: W: 1.5", H: 4.0", fill `#3A4055`, border 2 pt `#C8D0D8`
- Spaced evenly from X: 6.0" to X: 17.0"

Agitation arrows: 6--8 curved upward arrows, stroke 2 pt `#2EC4B6` dashed.

Soil particles: Small circles (0.15") scattered above parts, fill `#E8A020` at 40%.

Labels inside tank:
Right side (X: 18.0", Y: 6.5"):
- `Alkaline Soak Cleaner` -- Barlow SemiBold 16 pt `#F0EDE8`
- `4--8 oz/gal (30--60 g/L)` -- JetBrains Mono 14 pt `#2EC4B6`
- `Time: 3--10 min` -- JetBrains Mono 14 pt `#F0EDE8`
- `pH: 12--14` -- JetBrains Mono 14 pt `#F0EDE8` at 70%

Bottom label:
- `Non-silicated cleaner preferred -- silicate films cause skip plating in acid copper` -- Inter Medium 14 pt `#E8A020`

Left callout (X: 0.5", Y: 10.0"):
- Rounded rect, fill `#1E2435`, border-left 0.06" `#2EC4B6`
- `KEY: Water-break-free surface = clean. Any break in the water film = residual contamination.`

Right callout (X: 20.5", Y: 10.0"):
- Rounded rect, fill `#1E2435`, border-left 0.06" `#E8A020`
- `Electrocleaning: anodic preferred for steel -- cathodic embeds metals and risks H-embrittlement`

---

### ZONE 4 -- Parameter Tables

**Section label:** `CLEANING PARAMETERS -- DETAILED` -- Y: 14.7".

**Left table -- Soak Clean (X: 0.5", W: 11.0"):**

Header: fill `#3A4055`. Label: `SOAK CLEAN (STANDARD)`

| Parameter | Value |
|---|---|
| Cleaner type | Non-silicated alkaline soak (per supplier TDS) |
| Concentration | 4--8 oz/gal (30--60 g/L) |
| Temperature | 140--180 F (60--82 C) |
| Time | 3--10 min (longer for heavy soils) |
| Agitation | Mechanical, air, or ultrasonic |
| pH | 12--14 |
| Replenishment | Per titration or TDS schedule |
| Tank material | Mild steel or polypropylene |

**Right table -- Electroclean (X: 12.0", W: 11.5"):**

Header: fill `#3A4055`. Label: `ELECTROCLEAN (RECOMMENDED)`

| Parameter | Value |
|---|---|
| Type | Anodic preferred for final clean on steel |
| Concentration | 4--8 oz/gal (30--60 g/L) |
| Current density | 20--75 ASF |
| Temperature | 140--180 F (60--82 C) |
| Time | 1--3 min |
| Benefit | O2 scrubbing at anode removes embedded soils |
| Caution | Cathodic phase: H2 generated -- H-embrittlement risk |
| Note | Cathodic first (heavy soil), then anodic (final) |

Data: JetBrains Mono 13 pt `#F0EDE8`. Labels: Inter Medium 13 pt at 60%. Rows alternate `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Substrate Pathways + Problems

**Section label:** `SUBSTRATE-DEPENDENT CLEANING SEQUENCES` -- Y: 21.2".

**BLOCK E -- Three Pathway Cards (Y: 21.8" to 24.5")**

Three side-by-side cards showing different substrate cleaning pathways:

| Card | X | W | Accent | Title | Sequence |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `#27AE60` | `COPPER / BRASS / NICKEL` | Soak clean -> Electroclean -> Rinse -> Acid dip (5--10% H2SO4) -> Rinse -> Acid copper (DIRECT) |
| 2 | 8.17" | 7.33" | `#E8A020` | `STEEL (requires strike)` | Soak clean -> Electroclean -> Rinse -> HCl dip -> Rinse -> CN or alk. copper STRIKE -> Rinse -> Acid copper |
| 3 | 15.83" | 7.67" | `#2EC4B6` | `PCB (PRINTED CIRCUIT)` | No alkaline clean -> Microetch (Na persulfate or H2O2/H2SO4) -> Rinse -> Acid copper (DIRECT) |

Each card: Rounded rect H: 2.5", fill `#1E2435`, left accent 0.06". Title: Barlow SemiBold 16 pt in accent color. Sequence: Inter Regular 12 pt `#F0EDE8`.

Key note below cards: `Steel in acid copper without a strike = immersion deposit = peel. No exceptions.` -- Inter Medium 14 pt `#E05C5C`

**BLOCK F -- Problem Table (Y: 25.0" to 26.8")**

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Water break | Pitting or skip plating in copper tank | Residual oil -- cleaner weak or cold | Increase concentration or temp |
| Silicate film | Skip plating, hazy deposit | Silicated cleaner residue | Switch to non-silicated cleaner |
| Poor adhesion | Copper peels on bending | Oxide not removed (under-cleaning) | Add electroclean; extend soak time |
| Roughness in copper | Particulate embedded in deposit | Shop soil or cleaner breakdown | Filter cleaner; replace if old |

Problem: `#E05C5C`. Symptom: `#E8A020`. Cause: `#F0EDE8`. Fix: `#27AE60`.

---

### ZONE 6 -- Safety Callout

**Section label:** `SAFETY -- ALKALINE CLEANING CHEMISTRY` -- Barlow Condensed ExtraBold 24 pt `#E8A020`. Y: 27.2".

**Left -- Chemical Hazards (X: 0.5", W: 11.0"):**
- Title: `CHEMICAL HAZARDS` -- Barlow SemiBold 18 pt `#E05C5C`
- `NaOH/KOH: severe burns on contact -- pH > 12`
- `Hot solution (140--180 F): thermal burn risk`
- `Mist/vapor: respiratory irritant -- ensure ventilation`
- `Never add water to concentrated cleaner -- add cleaner to water`

**Right -- PPE Requirements (X: 12.0", W: 11.5"):**
- Title: `REQUIRED PPE` -- Barlow SemiBold 18 pt `#E8A020`
- `Chemical splash goggles (minimum) or face shield`
- `Chemical-resistant gloves (nitrile or neoprene)`
- `Chemical-resistant apron`
- `Eyewash station within 10 seconds travel`
- `SDS posted and accessible at all times`

---

### ZONE 7 -- Footer Band

Standard footer. Title: `Cleaning -- Copper (Acid)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for acid copper sulfate pre-treatment. Specific formulations vary by proprietary product. Consult your process supplier.`

---

## Part 5 -- Grouping

| Group | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | 8-stage strip, Stage 1 highlighted |
| Zone 3 - Tank Hero | Tank cross-section, labels, callouts |
| Zone 4 - Parameters | Soak clean table, electroclean table |
| Zone 5 - Pathways/Problems | Three substrate cards, problem table |
| Zone 6 - Safety | Chemical hazards, PPE panels |
| Zone 7 - Footer | Standard footer |

---

## Part 6 -- Light Edition Remap

Standard remap table.

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
| `Cleaning Copper Acid -- Dark -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Copper Acid -- Dark -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Copper Acid -- Dark -- Digital.pdf` | Standard | No |
| `Cleaning Copper Acid -- Light -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Copper Acid -- Light -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Cleaning Copper Acid -- Light -- Digital.pdf` | Standard | No |

---

## Design Notes

The unique feature of this cleaning poster vs. the zinc cleaning poster is the substrate-dependent pathway. Acid copper cleaning is NOT one-size-fits-all. Steel must have a strike. PCBs skip alkaline cleaning entirely. Copper/brass go direct. The three-pathway card layout makes this decision tree visible at a glance.

The non-silicated cleaner note is critical -- silicate films are one of the top causes of skip plating in acid copper, and many shops don't realize their cleaner contains silicates.

---

*Alaina -- Poster #96 -- Construction Workup v1.0 -- 2026-04-26*
