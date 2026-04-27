---
Project: Plating Posters Inc
Poster Number: 73
Title: "Rinse -- Nickel-Cobalt -- Pre-Activation"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Pre-activation rinse stage for nickel-cobalt alloy plating. Standard rinse practice -- ambient temperature, flowing water, purpose is to remove alkaline cleaner carry-over before the acid activation step. Stage 2 of 8.
Process Scope: Pre-activation rinse for nickel-cobalt alloy plating (Stage 2 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - Rinse
  - PreActivation
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #73 -- Construction Workup
## Rinse -- Nickel-Cobalt -- Pre-Activation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The pre-activation rinse removes alkaline cleaner carry-over before the acid activation step. This is standard rinse practice -- nothing unique to NiCo versus any other nickel process. But rinse posters earn their place by teaching rinse fundamentals that apply across every plating line: flow rate, conductivity monitoring, drag-out economics, and the cascade vs. counterflow decision.

Hero visual: a rinse station cross-section showing water flow, conductivity monitoring point, and drag-out/drag-in arrows.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Rinse station cross-section hero (Block B):** Tank with overflow weir, parts rack, water flow arrows, conductivity probe. Built with rectangles, lines, and text.
2. **Rinse types comparison (Block D):** Three-column layout -- single overflow, counterflow cascade, spray rinse.
3. **Conductivity and contamination callout (Block E):** When to dump, when to monitor, drag-out economics.
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
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE STATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE TYPES COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- CONDUCTIVITY + DRAG-OUT (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON RINSE FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Pre-Activation -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The cheapest tank on the line and the easiest one to ignore. That is exactly why it causes so many problems.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Cleaner-wet surface with alkaline residue  -->  After: Neutral, residue-free surface ready for acid activation`

---

### ZONE 3 -- Rinse Station Hero

**Section label:** `THE PRE-ACTIVATION RINSE STATION` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.0"
- Fill: `#252B3D` (rinse water)
- Border: 3 pt `#2EC4B6`

**Parts rack (center):**
- Vertical rect, X: 10.0", Y: 6.0", W: 4.0", H: 5.5", fill `#C8D0D8` at 30%, border 2 pt `#C8D0D8`
- Label above: `PARTS FROM CLEANER` Barlow SemiBold 14 pt `#F0EDE8`

**Water inlet (bottom-left):**
- Arrow entering tank from left side, stroke 2 pt `#2EC4B6`
- Label: `Fresh water inlet` Inter Medium 13 pt `#2EC4B6`

**Overflow weir (top-right):**
- Arrow exiting over right wall, stroke 2 pt `#2EC4B6`
- Label: `Overflow to drain` Inter Medium 13 pt `#2EC4B6`

**Drag-in arrow (left, above tank):**
- Downward arrow from left, stroke 2 pt `#E8A020`, dashed
- Label: `Alkaline drag-in` Inter Medium 13 pt `#E8A020`
- Sub-label: `Cleaner solution on part surface` Inter Regular 11 pt `#F0EDE8` at 60%

**Drag-out arrow (right, above tank):**
- Upward arrow to right, stroke 2 pt `#E8A020`, dashed
- Label: `Drag-out to activation` Inter Medium 13 pt `#E8A020`
- Sub-label: `Must be near-neutral` Inter Regular 11 pt `#F0EDE8` at 60%

**Conductivity probe (right side of tank):**
- Small rectangle, X: 19.0", Y: 8.0", W: 1.5", H: 2.0", fill `#1E2435`, border 1 pt `#E8A020`
- Label: `Conductivity probe` Inter Medium 12 pt `#E8A020`
- Reading: `Target: < 50 uS/cm` JetBrains Mono 13 pt `#27AE60`

**Bath parameter labels (center-right, X: 15.0", Y: 10.0"):**
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Flow: Continuous overflow` JetBrains Mono 14 pt `#2EC4B6`
- `Time: 30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`
- `Water: DI or city` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `Alkaline carry-over into the acid activation neutralizes the acid, shortens its life, and weakens the etch. A good rinse here saves acid downstream.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Rinse Types Comparison

**Section label:** `THREE RINSE CONFIGURATIONS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three-Column Comparison (Y: 15.3" to 20.3")**

| Type | X | W | Accent | Title |
|---|---|---|---|---|
| Single Overflow | 0.5" | 7.33" | `#2EC4B6` | SINGLE OVERFLOW |
| Counterflow Cascade | 8.0" | 7.33" | `#27AE60` | COUNTERFLOW CASCADE |
| Spray Rinse | 15.5" | 8.0" | `#E8A020` | SPRAY RINSE |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*Single Overflow:*
- `1 tank, continuous flow`
- `Simplest setup -- one inlet, one overflow`
- `Water use: highest per unit of rinse quality`
- `Best for: low-volume rack lines`
- `Limitation: poor rinse ratio vs. water consumption`

*Counterflow Cascade:*
- `2--3 tanks in series`
- `Fresh water enters last tank, overflows backward`
- `Water use: 90% less than single overflow for same rinse ratio`
- `Best for: high-volume production, barrel lines`
- `The industry standard for water efficiency`

*Spray Rinse:*
- `Nozzle array over tank or separate station`
- `Lowest water consumption`
- `Best for: flat parts, wire, strip`
- `Limitation: poor coverage on complex geometry (recesses, blind holes)`
- `Often combined with immersion as a pre-spray`

---

### ZONE 5 -- Conductivity and Drag-Out Economics

**Section label:** `MONITORING + DRAG-OUT ECONOMICS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Conductivity Monitoring (X: 0.5", W: 11.0"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`.

- Title: `CONDUCTIVITY IS YOUR RINSE GAUGE` Barlow SemiBold 18 pt `#27AE60`
- `Fresh DI water: < 5 uS/cm` JetBrains Mono 14 pt `#27AE60`
- `Good rinse: < 50 uS/cm` JetBrains Mono 14 pt `#27AE60`
- `Marginal: 50--200 uS/cm` JetBrains Mono 14 pt `#E8A020`
- `Dump and refill: > 200 uS/cm` JetBrains Mono 14 pt `#E05C5C`
- Body: `A handheld conductivity meter costs under $100. It tells you more about your rinse quality than any visual inspection. If you only buy one instrument for rinse monitoring, buy this.` Inter Regular 13 pt `#F0EDE8`

**Right -- Drag-Out Economics (X: 12.0", W: 11.5"):**

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`.

- Title: `DRAG-OUT = MONEY LEAVING THE TANK` Barlow SemiBold 18 pt `#E8A020`
- `Typical drag-out: 1--4 gal per 1000 ft2` JetBrains Mono 13 pt `#F0EDE8`
- `Rack orientation matters -- tilt parts to drain`
- `Dwell time over tank: 5--10 sec minimum`
- `Fog spray over process tank saves chemistry`
- Body: `Every drop of process solution on the part that ends up in the rinse tank is chemistry you paid for. Drain time is free. Use it.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 6 -- Common Rinse Failures

**Section label:** `WHAT GOES WRONG` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ALKALINE CARRY-OVER | Insufficient rinse time or stagnant water | Increase flow rate; extend immersion to 30+ sec |
| 2 | 6.33" | ACTIVATION NEUTRALIZED | High pH rinse water reaching acid tank | Monitor conductivity; dump and refill rinse |
| 3 | 12.16" | WATER SPOTTING | Minerals in city water drying on parts | Switch to DI water or add final spray rinse |
| 4 | 18.0" | CROSS-CONTAMINATION | Metals or organics from upstream dragged forward | Dedicated rinse per stage; never share rinse tanks |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer Band

Standard. Title: `Rinse -- Nickel-Cobalt -- Pre-Activation`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Rinse parameters shown are typical industry values. Specific conductivity limits and water quality requirements may vary by process specification. Consult your process supplier for application-specific guidance. Source: General industry knowledge; Metal Finishing Guidebook.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse NiCo Pre-Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters are universal -- the fundamentals do not change between zinc, nickel, or NiCo. The value of a dedicated rinse poster is teaching operators why rinsing matters and how to monitor it. The conductivity callout and drag-out economics section are the unique content that separates this from a "just a rinse tank" poster. Watson's brief says "Standard" for this stage, which is correct -- I expanded from general rinse engineering knowledge.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #73 -- Construction Workup v1.0*
*2026-04-26*
