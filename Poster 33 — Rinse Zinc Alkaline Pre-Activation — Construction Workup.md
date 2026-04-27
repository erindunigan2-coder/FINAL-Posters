---
Project: Plating Posters Inc
Poster Number: 33
Title: "Rinse -- Zinc (Alkaline) -- Pre-Activation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Pre-activation rinse for alkaline zinc plating line (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - Rinse
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #33 -- Construction Workup
## Rinse -- Zinc (Alkaline) -- Pre-Activation

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stage 2 of the alkaline zinc process. This poster covers the first rinse -- immediately after cleaning, before acid activation. Its job: strip every trace of alkaline cleaner so the acid activation can work. Sounds simple. Gets overlooked. Causes problems.

Hero visual: a cascade rinse tank diagram showing water flow direction, drag-out dilution, and conductivity monitoring.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Two or three connected tanks shown in cross-section, with arrows showing water flow direction (counter-current: clean water enters the final tank, overflows backward). Parts move left-to-right through the cascade.
2. **Orientation strip (Block C):** Stage 2 highlighted.
3. **Rinse parameter table (Block D):** Focused on rinse-specific parameters.
4. **Drag-out/carry-over callout (Block E):** Explains the chemistry of why rinsing matters here.
5. **Problems table and safety callout:** Standard layout.

---

## Part 2 -- Document Setup

Artboard: 24" x 36". Background: `#1A1F2E`. Fonts and colors: same locked palette as all EP-01 posters.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Block C: 8-stage strip with Stage 2 highlighted

ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3" tall)
  Block B: Cascade rinse tank diagram

ZONE 4 -- RINSE PARAMETER TABLE (14.5"--21.0" / ~6.5" tall)
  Block D: Detailed rinse parameters + drag-out callout

ZONE 5 -- COMMON PROBLEMS & FIXES (21.0"--27.0" / ~6.0" tall)
  Block F: Rinse-specific problem table

ZONE 6 -- SAFETY + WATER QUALITY (27.0"--32.5" / ~5.5" tall)
  Block G: Safety and water quality panel

ZONE 7 -- FOOTER BAND (32.5"--36.0")
  Block H: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Zinc (Alkaline) -- Pre-Activation -- Stage 2 of 8` -- Barlow SemiBold, 32 pt, `#2EC4B6`. X: 0.5", Y: 1.5".

**Tagline:** `The bridge between cleaning and activation. Get it wrong and the acid can't do its job.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.2".

---

### ZONE 2 -- Sequence Orientation Strip

Same structure as Poster #32, but **Stage 2 highlighted** (fill `#2EC4B6`, 100%). All others dimmed.

Below strip: `Before: Alkaline-cleaned surface (pH ~12)  -->  After: Neutral surface ready for acid activation`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE CASCADE RINSE` -- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center. Y: 4.4".

**BLOCK B -- Cascade Tank Diagram**

Y: 5.0" to 14.0".

Three connected tank cross-sections side by side, representing a 3-stage counter-current cascade:

**Tank 1 (Dirty Rinse) -- X: 0.5", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior fill slightly tinted with `#E8A020` at 10% (representing alkaline contamination)
- Label above: `STAGE 1 (DIRTY)` -- Barlow SemiBold 16 pt `#E8A020`
- Label inside: `Highest drag-in concentration` -- Inter Regular 13 pt `#F0EDE8` at 60%
- Overflow arrow pointing RIGHT from top edge to Tank 2 (to waste/drain)
  - Actually: overflow goes to DRAIN (counter-current means clean water enters Tank 3)
  - Arrow from top of Tank 1 pointing DOWN to `DRAIN` label

**Tank 2 (Middle Rinse) -- X: 8.0", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Interior slightly cleaner (no tint)
- Label above: `STAGE 2 (MIDDLE)` -- Barlow SemiBold 16 pt `#F0EDE8`
- Overflow arrow from top of Tank 2 pointing LEFT into top of Tank 1

**Tank 3 (Clean Rinse) -- X: 15.5", W: 7.0", H: 7.5":**
- Rounded rect, fill `#252B3D` with slight `#2EC4B6` tint at 10% (fresh water)
- Border 3 pt `#C8D0D8`
- Label above: `STAGE 3 (CLEAN)` -- Barlow SemiBold 16 pt `#2EC4B6`
- Fresh water inlet arrow from RIGHT pointing into Tank 3
- Label: `FRESH WATER IN` -- JetBrains Mono 12 pt `#2EC4B6`
- Overflow arrow from top of Tank 3 pointing LEFT into top of Tank 2

**Parts movement arrow:**
- Large horizontal arrow below all tanks, pointing LEFT to RIGHT
- `PARTS TRAVEL -->` -- Barlow SemiBold 14 pt `#F0EDE8`
- Parts enter Tank 1 (dirtiest) and exit Tank 3 (cleanest) -- counter-current to water flow

**Water flow arrow:**
- Large horizontal arrow above all tanks, pointing RIGHT to LEFT
- `<-- WATER FLOW (counter-current)` -- Barlow SemiBold 14 pt `#2EC4B6`

**Key metrics callout (below tanks, Y: 13.0"):**
- Rounded rect, X: 0.5", W: 23.0", H: 1.0", fill `#1E2435`, border-left 0.06" `#2EC4B6`
- Text: `A 3-stage cascade uses 90% less water than a single flowing rinse for the same dilution ratio. Target: < 500 microsiemens/cm conductivity at final stage.`
- Inter Medium, 14 pt, `#F0EDE8`

---

### ZONE 4 -- Rinse Parameter Table

**Section label:** `RINSE PARAMETERS` -- Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, Center. Y: 14.7".

**BLOCK D -- Parameter Table + Drag-Out Callout**

Y: 15.3" to 20.8".

**Left -- Rinse Parameters (X: 0.5", W: 14.0"):**

Header: `PRE-ACTIVATION RINSE` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Water type | DI preferred; city water acceptable |
| Temperature | Ambient (no heating required) |
| Flow rate | 2--5 gal/min per stage (cascade) |
| Stages | 2--3 stage cascade recommended |
| Immersion time | 30--60 sec per stage |
| Agitation | Air or part movement |
| Conductivity target | < 500 uS/cm at final stage |
| Drain time | 10--15 sec between tanks |
| Rinse criterion | No alkaline residue (pH paper check) |

Data: JetBrains Mono 13 pt. Labels: Inter Medium 13 pt at 60%. Rows alternate.

**Right -- Drag-Out Callout (X: 15.0", W: 8.5"):**

Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `WHY THIS RINSE MATTERS` -- Barlow SemiBold, 18 pt, `#E8A020`

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 150%):

> Alkaline cleaner (pH 11--13) is dragged into the rinse on every rack or barrel. If this residue reaches the acid activation tank, it neutralizes the acid -- raising pH, weakening the activation, and leaving oxide on the parts.
>
> Result: poor adhesion in the zinc tank.
>
> The rinse is not just "water" -- it is a chemical barrier between two incompatible chemistries.

Key metric at bottom:
- `Drag-out rate: ~0.5--2.0 gal per 1000 ft2 of surface` -- JetBrains Mono 12 pt `#2EC4B6`

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT THE PRE-ACTIVATION RINSE` -- Y: 21.2".

**BLOCK F -- 4-Row Problem Table**

| Problem | Symptom Downstream | Root Cause | Fix |
|---|---|---|---|
| Alkaline carry-over | Activation acid neutralized; poor oxide removal | Insufficient rinse time or stages | Add cascade stage; increase flow |
| High conductivity | Parts still alkaline at activation entry | Rinse water exhausted or flow too low | Monitor conductivity; increase water flow |
| Spotting/staining | White residue on parts after rinse | Hard water minerals (Ca, Mg) depositing | Switch to DI water; add water softener |
| Foam in rinse | Surfactant drag-out from cleaner | Cleaner has high-foam surfactants | Use low-foam cleaner; add defoamer to rinse |

Same styling as Poster #32 problem table. Problem: `#E05C5C`, Symptom: `#E8A020`, Cause: `#F0EDE8`, Fix: `#27AE60`.

---

### ZONE 6 -- Safety + Water Quality

**Section label:** `WATER QUALITY & SAFETY` -- Y: 27.2".

**Left -- Water Quality (X: 0.5", W: 11.0"):**
- Title: `WATER QUALITY MATTERS` -- Barlow SemiBold 18 pt `#2EC4B6`
- Bullets:
  - `DI water: < 10 uS/cm -- best for critical parts`
  - `City water: 200--600 uS/cm -- acceptable for most zinc work`
  - `Hard water: > 300 ppm CaCO3 -- risk of spotting`
  - `Monitor final rinse conductivity daily`
  - `Dump and refill when conductivity exceeds 1000 uS/cm`

**Right -- Safety (X: 12.0", W: 11.5"):**
- Title: `SAFETY NOTES` -- Barlow SemiBold 18 pt `#E8A020`
- Bullets:
  - `Rinse water is mildly alkaline from drag-out -- handle accordingly`
  - `Rinse overflow goes to waste treatment -- not down the drain`
  - `Wet floors: slip hazard -- maintain drainage and mats`
  - `pH check rinse water periodically -- should be near neutral (6--8)`

---

### ZONE 7 -- Footer Band

Standard footer. Title: `Rinse -- Zinc (Alkaline) -- Pre-Activation`. Version `v1.0 -- 2026`.

---

## Part 5 -- Grouping

| Group | Contents |
|---|---|
| Zone 1 - Header | Headline, subheading, tagline |
| Zone 2 - Orientation | 8-stage strip, Stage 2 highlighted |
| Zone 3 - Cascade Hero | 3-tank diagram, flow arrows, metrics callout |
| Zone 4 - Parameters | Table + drag-out callout |
| Zone 5 - Problems | 4-row problem table |
| Zone 6 - Water/Safety | Water quality + safety panels |
| Zone 7 - Footer | Standard footer |

---

## Part 6 -- Light Edition Remap

Standard remap table (same as all EP-01 posters). Tank walls `#C8D0D8` unchanged.

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
| `Rinse Zinc Alkaline Pre-Act -- Dark -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Rinse Zinc Alkaline Pre-Act -- Dark -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Rinse Zinc Alkaline Pre-Act -- Dark -- Digital.pdf` | Standard | No |
| `Rinse Zinc Alkaline Pre-Act -- Light -- 24x36 -- Print.pdf` | 300 DPI | Yes |
| `Rinse Zinc Alkaline Pre-Act -- Light -- 18x24 -- Print.pdf` | 300 DPI | Yes |
| `Rinse Zinc Alkaline Pre-Act -- Light -- Digital.pdf` | Standard | No |

---

*Elara -- Poster #33 -- Construction Workup v1.0 -- 2026-04-25*
