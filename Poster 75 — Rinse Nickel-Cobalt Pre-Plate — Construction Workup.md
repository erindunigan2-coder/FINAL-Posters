---
Project: Plating Posters Inc
Poster Number: 75
Title: "Rinse -- Nickel-Cobalt -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Pre-plate rinse stage for nickel-cobalt alloy plating. Removes residual activation acid before the NiCo plating bath. Critical for preventing acid drag-in that lowers bath pH and introduces chloride contamination. Stage 4 of 8.
Process Scope: Pre-plate rinse for nickel-cobalt alloy plating (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #75 -- Construction Workup
## Rinse -- Nickel-Cobalt -- Pre-Plate

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The pre-plate rinse removes residual activation acid (HCl from acid dip or Wood's strike) before parts enter the NiCo plating bath. Acid drag-in is the enemy here -- it drops bath pH, introduces chloride, and can cause pitting. For parts coming out of a Wood's strike, this rinse must be fast -- the thin nickel strike layer can start to passivate if parts sit too long in stagnant water.

Hero visual: rinse station with emphasis on the acid-to-alkaline transition and the time-sensitivity callout for Wood's strike parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Rinse station hero (Block B):** Tank cross-section with acid drag-in and time-sensitivity callouts. Same construction pattern as Poster #73.
2. **Acid drag-in impact panel (Block D):** What happens to the NiCo bath when acid is carried in -- pH, chloride, and pitting consequences.
3. **Transfer timing callout (Block E):** Time-critical transfer for Wood's strike parts vs. standard acid-dipped parts.
4. **Common rinse failures (Block F):** 4-card strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE STATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACID DRAG-IN IMPACT (14.5"--20.5" / ~6.0")
ZONE 5 -- TRANSFER TIMING (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON RINSE FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Pre-Plate -- Stage 4 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Last stop before the plating bath. Acid drag-in drops your pH and introduces chloride. Rinse it clean or pay for it in the tank.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Activated surface with residual acid  -->  After: Acid-free surface ready for NiCo plating`

---

### ZONE 3 -- Rinse Station Hero

**Section label:** `THE PRE-PLATE RINSE STATION` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.0"
- Fill: `#252B3D` (rinse water)
- Border: 3 pt `#2EC4B6`

**Parts rack (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.5", fill `#C8D0D8` at 30%, border 2 pt `#C8D0D8`
- Label above: `PARTS FROM ACTIVATION` Barlow SemiBold 14 pt `#F0EDE8`

**Water inlet (bottom-left):**
- Arrow entering tank, stroke 2 pt `#2EC4B6`
- Label: `Fresh water inlet` Inter Medium 13 pt `#2EC4B6`

**Overflow weir (top-right):**
- Arrow exiting, stroke 2 pt `#2EC4B6`
- Label: `Overflow to drain` Inter Medium 13 pt `#2EC4B6`

**Acid drag-in arrow (left, above tank):**
- Downward arrow, stroke 2 pt `#E05C5C`, dashed
- Label: `HCl drag-in from activation` Inter Medium 13 pt `#E05C5C`
- Sub-label: `Drops bath pH, introduces Cl-` Inter Regular 11 pt `#E05C5C`

**Clean drag-out arrow (right, above tank):**
- Upward arrow, stroke 2 pt `#27AE60`, dashed
- Label: `Clean surface to NiCo bath` Inter Medium 13 pt `#27AE60`
- Sub-label: `Must be acid-free and still active` Inter Regular 11 pt `#27AE60`

**Bath parameter labels (right side, X: 15.0", Y: 9.0"):**
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Flow: Continuous overflow` JetBrains Mono 14 pt `#2EC4B6`
- `Time: 30--60 sec` JetBrains Mono 14 pt `#F0EDE8`
- `Water: DI preferred` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `pH target: 6--8 (neutral)` JetBrains Mono 13 pt `#27AE60`

**Time-sensitive callout (left side, X: 2.5", Y: 9.0"):**
- Rounded rect, W: 6.0", H: 2.5", fill `#E8A020` at 10%, border 1 pt `#E8A020`
- Title: `TIME-SENSITIVE` Barlow SemiBold 14 pt `#E8A020`
- Text: `Wood's strike parts: Do not hold in rinse longer than 60 sec. The thin Ni strike can passivate, compromising adhesion to the NiCo deposit.` Inter Regular 12 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `This rinse bridges acid activation and the NiCo plating bath. Too much acid carry-over wrecks your bath pH. Too much delay re-passivates your strike. Move with purpose.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Acid Drag-In Impact

**Section label:** `WHAT ACID DRAG-IN DOES TO YOUR NiCo BATH` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Impact Panel (Y: 15.3" to 20.3")**

**Three side-by-side callout boxes:**

| Impact | X | W | Accent | Title |
|---|---|---|---|---|
| pH Drop | 0.5" | 7.33" | `#E05C5C` | pH DROP |
| Chloride Buildup | 8.0" | 7.33" | `#E8A020` | CHLORIDE BUILDUP |
| Pitting | 15.5" | 8.0" | `#E05C5C` | PITTING |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*pH Drop box:*
- `HCl drag-in lowers bath pH` JetBrains Mono 14 pt `#E05C5C`
- `NiCo bath target: pH 3.5--4.5`
- `Below 3.5: poor throwing power, burning at HCD`
- `Above 4.5: hydroxide precipitation, rough deposit`
- `Corrective: NaOH or NiCO3 to raise; H2SO4 to lower`
- `Prevention > correction -- rinse properly`

*Chloride Buildup box:*
- `HCl introduces free Cl- ions` JetBrains Mono 14 pt `#E8A020`
- `Small amount of NiCl2 is normal in NiCo baths (5--15 g/L)`
- `Excess Cl- from drag-in: increases anode corrosion`
- `Can shift alloy composition (higher stress)`
- `Not easily removed -- prevention is the only practical control`

*Pitting box:*
- `Acid-contaminated bath pits` JetBrains Mono 14 pt `#E05C5C`
- `Low pH + excess Cl- = gas evolution + pin-hole pits`
- `NiCo aerospace parts cannot tolerate pitting`
- `Rework on turbine components is expensive`
- `One bad rinse can contaminate a bath for days`

---

### ZONE 5 -- Transfer Timing

**Section label:** `TRANSFER TIMING -- HOW FAST IS FAST ENOUGH?` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Standard Acid Dip Parts (X: 0.5", W: 11.0"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`.

- Title: `STEEL / STANDARD ACID DIP` Barlow SemiBold 18 pt `#2EC4B6`
- `Rinse: 30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`
- `No strict time limit between rinse and plate`
- `Parts can sit briefly if still wet`
- `Do not allow parts to dry -- re-oxidation starts immediately`
- `Comfortable pace -- focus on thorough rinsing`

**Right -- Wood's Strike Parts (X: 12.0", W: 11.5"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`.

- Title: `SUPERALLOY / WOOD'S STRIKE` Barlow SemiBold 18 pt `#E8A020`
- `Rinse: 15--30 sec MAX` JetBrains Mono 14 pt `#E8A020`
- `Transfer to NiCo bath within 60 sec of exiting rinse`
- `Thin Ni strike re-passivates in air`
- `Some shops transfer LIVE (current on) from Wood's to NiCo`
- `Speed is everything -- have the plating bath ready before you start the strike` Inter Medium 13 pt `#E05C5C`

**Full-width verdict banner (Y: 25.8"):**
- Rounded rect, W: 23.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`, radius 999
- Text: `The Wood's strike exists because these alloys fight adhesion. Do not give them time to win.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Common Rinse Failures

**Section label:** `WHAT GOES WRONG` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BATH pH DRIFT | Acid carry-over from insufficient rinsing | Increase rinse flow; monitor bath pH every shift |
| 2 | 6.33" | PITTING IN NiCo DEPOSIT | Chloride contamination from drag-in | Improve rinse; consider double rinse |
| 3 | 12.16" | ADHESION LOSS (SUPERALLOYS) | Strike passivated during extended rinse hold | Reduce transfer time; consider live transfer |
| 4 | 18.0" | ROUGH DEPOSIT | Particulate from dirty rinse water | Filter rinse tank; use DI water |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

Standard. Title: `Rinse -- Nickel-Cobalt -- Pre-Plate`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Rinse parameters and transfer timing shown are typical industry values. Specific transfer protocols for Wood's strike parts vary by OEM specification (AMS 2424, PWA, GE). Consult your process supplier and governing specification for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse NiCo Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This pre-plate rinse poster differentiates itself from the pre-activation rinse (Poster #73) by focusing on acid drag-in consequences and the time-sensitive transfer for Wood's strike parts. The three-panel acid drag-in impact section is the unique value-add -- operators need to understand that a sloppy rinse here has quantifiable consequences in the plating bath. The transfer timing comparison (standard vs. Wood's strike) is practical and immediately actionable.

Watson's brief says "Standard" for this stage, which is technically true -- but the context of NiCo (superalloy substrates requiring Wood's strike) makes this rinse more operationally critical than a typical pre-plate rinse.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #75 -- Construction Workup v1.0*
*2026-04-26*
