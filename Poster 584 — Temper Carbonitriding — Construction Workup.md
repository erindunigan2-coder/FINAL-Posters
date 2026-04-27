---
Project: Plating Posters Inc
Poster Number: 584
Title: "Temper -- Carbonitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding, Section 3.4)"
Technical Source: Post-quench tempering for carbonitriding. Temperature, time, atmosphere, and the balance between stress relief and hardness retention. Also covers sub-zero treatment for retained austenite.
Process Scope: Carbonitriding temper and post-quench treatment
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - Temper
  - PostQuench
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #584 -- Construction Workup
## Temper -- Carbonitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Tempering is the final heat step after quench -- it relieves the massive internal stresses created during the austenite-to-martensite transformation without significantly reducing surface hardness. Skip the temper and you get a part that is hard but dangerously brittle. This poster also covers sub-zero treatment, which is particularly important for carbonitriding because nitrogen increases retained austenite.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temper cycle profile (Block B -- HERO):** Time-temperature chart showing heat to temper temperature, hold, cool.
2. **Temper parameter table (Block D):** Temperature, time, atmosphere targets.
3. **Sub-zero treatment panel (Block E):** When and how to treat retained austenite.
4. **Temper rules callout (Block F):** Critical rules -- temper immediately, never skip, never over-temper.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 13.0" / 19.0" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- TEMPER CYCLE PROFILE / HERO (2.9"--13.0" / ~10.1")
  Block B: T-T chart for temper cycle
ZONE 3 -- TEMPER PARAMETERS (13.0"--19.0" / ~6.0")
  Block D: Parameter table + hardness retention data
ZONE 4 -- SUB-ZERO TREATMENT (19.0"--26.0" / ~7.0")
  Block E: Retained austenite treatment
ZONE 5 -- TEMPER RULES (26.0"--32.5" / ~6.5")
  Block F: Non-negotiable rules
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Carbonitriding -- Stress Relief Without Softening the Case` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `A quenched part is hard but brittle. Tempering is the difference between a part that works and a part that cracks in service.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Temper Cycle Profile (HERO)

**Section label:** `THE TEMPER CYCLE` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- T-T Profile Chart**

Y: 3.8" to 12.5". Chart area: X: 2.0" to 22.0", Y: 4.5" to 12.0".

**Axes:**
- Y-axis: Temperature, 0--500 F. Labels at 0, 100, 200, 300, 400, 500 F.
- X-axis: Time. Labels: `Load`, `Heat-Up`, `Hold (1--2 hr)`, `Cool`.
- Axis lines: 1 pt `#3A4055`. Grid: 0.5 pt `#3A4055` at 30%.

**Temperature profile line:**
- Stroke: 3 pt `#E8A020`
- Shape: ramp from ambient to 300--400 F, flat hold for 1--2 hours, gradual cool to ambient

**Optimal range band:**
- Semi-transparent band (`#27AE60` at 15%) from 300 F to 400 F across the hold phase
- Label: `OPTIMAL: 300--400 F (150--205 C)` Barlow SemiBold 14 pt `#27AE60`

**Warning zones:**
- Below 250 F: label `Insufficient stress relief` Inter Regular 11 pt `#E05C5C`
- Above 500 F: label `Excessive softening -- hardness drops` Inter Regular 11 pt `#E05C5C`

**Annotations:**
- At hold start: `Minimum 1 hour at temperature` Inter Medium 12 pt `#E8A020`
- At cool: `Air cool to ambient` Inter Regular 11 pt `#F0EDE8` at 60%

**Right-side callout (X: 16.0", Y: 5.0"):**
- Rounded rect, W: 6.5", H: 3.5", fill `#1E2435`, left accent `#E8A020`
- `Temper temp: 300--400 F` JetBrains Mono 14 pt `#E8A020`
- `Time: 1--2 hours minimum` JetBrains Mono 13 pt `#F0EDE8`
- `Atmosphere: Air or N2 blanket` Inter Regular 12 pt `#F0EDE8` at 70%
- `Surface hardness after temper: 58--62 HRC` JetBrains Mono 13 pt `#27AE60`

---

### ZONE 3 -- Temper Parameters

**Section label:** `TEMPER PARAMETERS` -- Y: 13.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Parameter Table**

Y: 13.8" to 18.8". Two panels side by side.

**Left -- Parameters (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `STANDARD TEMPER` -- Barlow SemiBold, 18 pt, `#E8A020`
- Content (JetBrains Mono 13 pt, line height 170%):
  - `Temperature: 300--400 F (150--205 C)`
  - `Time at temp: 1--2 hours minimum`
  - `Atmosphere: Air or nitrogen blanket`
  - `Heating rate: No restriction (temper furnace)`
  - `Cooling: Air cool to ambient`
  - `Per AMS 2759/7: 300--375 F, 2 hr min`

**Right -- Hardness Retention (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60`
- Title: `HARDNESS AFTER TEMPER` -- Barlow SemiBold, 18 pt, `#27AE60`
- Content:
  - `As-quenched: 60--65 HRC`
  - `After 300 F temper: 59--63 HRC (minimal loss)`
  - `After 400 F temper: 57--61 HRC`
  - `After 500 F temper: 52--56 HRC (excessive)`
  - Highlight: `Stay below 400 F to preserve case hardness` -- `#27AE60`
  - `Higher temper temps are used only for specific toughness requirements`

---

### ZONE 4 -- Sub-Zero Treatment

**Section label:** `SUB-ZERO TREATMENT -- RETAINED AUSTENITE CONVERSION` -- Y: 19.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Sub-Zero Treatment Panel**

Y: 19.8" to 25.8". Full-width panel.

Rounded rect, X: 0.5", W: 23.0", H: 5.8", fill `#1E2435`, left accent `#2EC4B6` 0.06".

**Two-column interior:**

**Left -- Why Sub-Zero? (W: 11.0"):**
- Title: `THE RETAINED AUSTENITE PROBLEM` -- Barlow SemiBold, 18 pt, `#E05C5C`
- `Carbonitriding has HIGHER retained austenite risk than carburizing`
- `Nitrogen stabilizes austenite -- more NH3 = more RA`
- `Retained austenite is soft (compared to martensite)`
- `RA can transform in service -> dimensional instability`
- `Spec limit: typically max 15--20% RA`
- `If RA exceeds limit: sub-zero treatment required`

**Right -- Sub-Zero Procedure (W: 11.0"):**
- Title: `SUB-ZERO TREATMENT PROCEDURE` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- `Temperature: -100 to -120 F (-73 to -84 C)` JetBrains Mono 14 pt `#2EC4B6`
- `Method: dry ice + alcohol bath or mechanical cryo`
- `Time: 1--2 hours at temperature`
- `Perform BEFORE tempering (quench -> sub-zero -> temper)`
- `Converts retained austenite to martensite`
- `Re-temper after sub-zero treatment`

**Bottom callout:** `Sequence: Quench -> Sub-Zero (if needed) -> Temper -> Final inspection. Never temper before sub-zero -- tempering stabilizes austenite.` -- Inter Medium, 14 pt, `#E8A020`.

---

### ZONE 5 -- Temper Rules

**Section label:** `NON-NEGOTIABLE TEMPER RULES` -- Y: 26.2". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

**BLOCK F -- 4 Rule Cards**

Y: 26.9" to 32.3". Four cards in a row.

| Card | X | Rule | Explanation |
|---|---|---|---|
| 1 | 0.5" | TEMPER WITHIN 1 HOUR OF QUENCH | Delayed temper increases cracking risk; residual stress is maximum immediately after quench |
| 2 | 6.33" | NEVER SKIP THE TEMPER | Untempered martensite is extremely brittle; parts will crack in service |
| 3 | 12.16" | NEVER EXCEED 400 F WITHOUT CAUSE | Over-tempering softens the case; spec limits exist for a reason |
| 4 | 18.0" | SUB-ZERO BEFORE TEMPER | Tempering stabilizes retained austenite; sub-zero after temper is less effective |

Card format: Rounded rect, W: 5.5", H: 5.2", fill `#1E2435`, radius 6, left accent `#E05C5C` 0.06".
- Rule: Barlow SemiBold, 16 pt, `#E05C5C`
- Explanation: Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Footer

Standard footer. Title: `Temper -- Carbonitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Carbonitriding -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The sub-zero treatment section is uniquely important for carbonitriding (more so than carburizing) because nitrogen significantly increases retained austenite. The temper rules strip uses Coral accents throughout because every one of these rules, if violated, leads to cracked or dimensionally unstable parts.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #584 -- Construction Workup v1.0*
*2026-04-26*
