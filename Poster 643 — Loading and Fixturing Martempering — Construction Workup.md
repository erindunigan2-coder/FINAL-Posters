---
Project: Plating Posters Inc
Poster Number: 643
Title: "Loading & Fixturing -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10: Martempering, Section 10.4)"
Process Scope: Loading, fixturing, drainage orientation, and transfer mechanisms for martempering -- salt bath and hot oil configurations
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Martempering
  - Loading
  - Fixturing
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #643 -- Construction Workup
## Loading & Fixturing -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading for martempering follows the same principles as austempering -- drainage orientation, rapid transfer, no part contact -- but the equalization hold is only 5-15 minutes (vs. 30-120 min for austempering), so the transfer speed tolerance is slightly more forgiving if the steel has high hardenability. Still, the same 15-second rule applies: slow transfer risks pearlite formation. This poster also covers the difference between fixturing for salt bath quench vs. hot oil quench.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Fixture comparison hero (Block B):** Salt bath fixturing vs. hot oil fixturing side by side.
2. **Transfer speed and mechanism (Block C):** Same 15-second rule with consequence table.
3. **Load configuration for equalization (Block D):** Why part spacing matters for uniform temperature equalization.
4. **Pre-immersion checklist (Block E):** Practical checklist before loading.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 21.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal)
ZONE 3 -- FIXTURE COMPARISON HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- TRANSFER SPEED (14.0"--21.0" / ~7.0")
ZONE 5 -- LOAD CONFIGURATION (21.0"--27.5" / ~6.5")
ZONE 6 -- PRE-IMMERSION CHECKLIST (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Salt Bath & Hot Oil Configurations` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Fixture for the quench medium. Orient for drainage. Transfer in under 15 seconds.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 of 9 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry, verified parts --> After: Fixtured, oriented, transfer path clear, ready for austenitize`

---

### ZONE 3 -- Fixture Comparison Hero

**Section label:** `FIXTURING FOR TWO QUENCH MEDIA` -- Y: 4.4".

**BLOCK B -- Side-by-Side Fixture Panels**

Y: 5.0" to 13.5".

**Left -- Salt Bath Fixturing (X: 0.5", W: 11.0"):**

Rounded rect, H: 8.0", fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `SALT BATH FIXTURING` -- Barlow SemiBold, 20 pt, `#E8A020`
Subtitle: `Nitrate/Nitrite Salt at 350--600 F` -- JetBrains Mono Regular, 13 pt, `#F0EDE8` at 60%

Items (Inter Regular 14 pt `#F0EDE8`, line height 165%):

| Requirement | Detail |
|---|---|
| Material | RA 330, Inconel 601, or equivalent salt-rated alloy |
| Drainage | Parts oriented open-end DOWN; bores vertical |
| Spacing | Min 0.25" between parts for salt circulation |
| Salt compatibility | No carbon steel in salt > 500 F -- degrades rapidly |
| Pre-heat | Fixtures pre-heated to 250+ F before salt immersion |
| Extraction | Allow salt to drain 10-15 sec before moving to wash |

Bottom note: `Salt fixturing must survive BOTH austenitizing temp (1500+ F) and salt bath temp (350-600 F) without distortion.` -- Inter Medium, 12 pt, `#E8A020`

**Right -- Hot Oil Fixturing (X: 12.0", W: 11.5"):**

Rounded rect, H: 8.0", fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Title: `HOT OIL FIXTURING` -- Barlow SemiBold, 20 pt, `#2EC4B6`
Subtitle: `Marquench Oil at 250--400 F` -- JetBrains Mono Regular, 13 pt, `#F0EDE8` at 60%

| Requirement | Detail |
|---|---|
| Material | Standard HT alloy steel fixtures; less demanding than salt |
| Drainage | Parts oriented for oil drainage; avoid oil pooling in recesses |
| Spacing | Min 0.5" for adequate oil flow (oil is more viscous than salt) |
| Oil compatibility | Fixture materials must not contaminate oil (no copper, no zinc) |
| Agitation access | Load must allow agitation flow through entire load |
| Fire safety | No fixture features that could trap and concentrate oil vapor |

Bottom note: `Hot oil is less corrosive to fixtures than salt, but higher viscosity requires wider spacing for equivalent quench uniformity.` -- Inter Medium, 12 pt, `#2EC4B6`

---

### ZONE 4 -- Transfer Speed

**Section label:** `TRANSFER FROM FURNACE TO QUENCH -- THE 15-SECOND RULE` -- Y: 14.2".

**BLOCK C -- Transfer Panel**

Y: 14.8" to 20.8". Two-panel layout.

**Left -- The Rule (X: 0.5", W: 13.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6.

Title: `MAXIMUM 15 SECONDS` -- Barlow Condensed ExtraBold, 26 pt, `#E05C5C`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
Same rule as austempering. From furnace door opening to complete
immersion in salt or oil -- 15 seconds maximum.

The pearlite nose on the TTT diagram is the enemy. If any part
of the cross-section cools into the pearlite region during
transfer, that volume transforms to pearlite irreversibly.

DIFFERENCE FROM AUSTEMPERING: In martempering, the equalization
hold is only 5-15 min. If you have a high-hardenability steel
(4340, H13), the TTT diagram gives you more time before pearlite
-- but never assume it. Measure your transfer time.
```

**Right -- Transfer Methods (X: 14.0", W: 9.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Title: `TRANSFER METHODS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Method | Typical Time | Best For |
|---|---|---|
| Robot arm | 3--6 sec | Precision, repeatability |
| Automated conveyor | 5--8 sec | High-volume production |
| Overhead crane | 8--12 sec | Heavy loads, large parts |
| Manual (tongs) | 10--20 sec | Small shop; RISKY for time |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

Warning: `Manual transfer regularly exceeds 15 sec -- automate if possible.` -- Inter Medium, 12 pt, `#E05C5C`

---

### ZONE 5 -- Load Configuration for Equalization

**Section label:** `LOAD CONFIGURATION -- WHY SPACING MATTERS FOR EQUALIZATION` -- Y: 21.2".

**BLOCK D -- Equalization Panel**

Y: 21.8" to 27.3". Rounded rect, full width, H: 5.3", fill `#1E2435`, left accent `#27AE60`, radius 8.

Three-column layout:

**Column 1 -- The Problem (W: 7.5"):**
- Title: `DENSE LOAD` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Body (Inter Regular, 13 pt, `#F0EDE8`):
```
Parts packed tight. Salt/oil cannot
circulate. Parts at center of load
equalize slowly -- core may still be
100+ F hotter than bath temp when
surface parts are equalized.

Result: surface transforms to martensite
before core equalizes. Non-uniform
transformation. Distortion.
```

**Column 2 -- The Solution (W: 7.5"):**
- Title: `PROPERLY SPACED LOAD` -- Barlow SemiBold, 16 pt, `#27AE60`
- Body (Inter Regular, 13 pt, `#F0EDE8`):
```
Min 0.25" spacing (salt) or 0.5" (oil)
between all parts. Quench medium flows
freely around every surface. All parts
equalize at the same rate.

Result: Surface AND core of every part
reach bath temperature before removal.
Uniform martensite transformation on
air cool. Minimal distortion.
```

**Column 3 -- Key Numbers (W: 7.0"):**
- Title: `EQUALIZATION TIMES` -- Barlow SemiBold, 16 pt, `#E8A020`
- Body (JetBrains Mono Regular, 12 pt, `#F0EDE8`):
```
0.5" section:   3--5 min
1.0" section:   5--8 min
1.5" section:   8--12 min
2.0" section:  12--15 min

Above 2": preheat recommended
to reduce equalization time

Hold = equalization time +
       2 min safety margin
```

---

### ZONE 6 -- Pre-Immersion Checklist

**Section label:** `PRE-IMMERSION CHECKLIST` -- Y: 27.7".

**BLOCK E -- Checklist**

Y: 28.3" to 32.3". Rounded rect, full width, H: 3.8", fill `#1E2435`, left accent `#2EC4B6`, radius 8.

Checklist items (Inter Medium 14 pt `#F0EDE8`):
```
[ ] All parts clean, dry, and free of organic contamination
[ ] Parts fixtured with drainage orientation for quench medium
[ ] Spacing verified -- no contact between parts
[ ] Fixture rated for austenitizing temperature
[ ] Fixture pre-heated (salt bath operations)
[ ] Transfer path clear -- no obstacles between furnace and quench
[ ] Quench bath at target temperature (+/-5 F) and agitation running
[ ] Transfer mechanism tested -- confirmed < 15 sec cycle time
```

Each checkbox: 0.25" x 0.25" rounded rect, border 1 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Loading & Fixturing -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4. Specific fixture materials and load configurations per equipment manufacturer recommendations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Fixturing Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-media fixture comparison in Zone 3 is the distinguishing feature -- operators running salt lines see different requirements than those running hot oil. The equalization panel in Zone 5 connects load configuration directly to the quality outcome -- wider spacing = better equalization = more uniform martensite = less distortion. The equalization time table gives practical numbers to target.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #643 -- Construction Workup v1.0*
*2026-04-26*
