---
Project: Plating Posters Inc
Poster Number: 638
Title: "Isothermal Hold -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Sections 9.7 and 9.8)"
Process Scope: The isothermal salt bath hold -- where bainite transformation actually happens. Hold time, transformation monitoring, and what happens if you pull parts too early or too late.
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - IsothermalHold
  - BainiteTransformation
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #638 -- Construction Workup
## Isothermal Hold -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the poster for the defining step of austempering: the isothermal hold. The part sits in molten salt at a constant temperature while austenite transforms to bainite. Not too short (retained austenite = martensite on cooling = bad), not too long (economics, salt degradation). Conventional quench-and-temper races through the transformation; austempering parks at one temperature and waits for it to finish. This patience is the whole point -- and the reason the results are superior.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Transformation timeline hero (Block B):** Visual showing transformation progress at different hold times.
2. **Hold time guidelines table (Block C):** Recommended hold times by material and section size.
3. **What happens if you pull early (Block D):** Consequences of incomplete transformation -- retained austenite converting to martensite on cooling.
4. **Salt bath management during hold (Block E):** Practical operational guidance.

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
  Stage 8 highlighted (Emerald)
ZONE 3 -- TRANSFORMATION TIMELINE HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- HOLD TIME GUIDELINES (14.0"--21.0" / ~7.0")
ZONE 5 -- EARLY PULL = BAD (21.0"--27.5" / ~6.5")
ZONE 6 -- SALT BATH MANAGEMENT (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ISOTHERMAL HOLD` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Where Bainite Forms` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Hold at temperature. Wait for transformation. No shortcuts. This is where austempering earns its name.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 of 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `The salt bath hold is the core step -- austenite transforms to bainite at constant temperature`

---

### ZONE 3 -- Transformation Timeline Hero

**Section label:** `BAINITE TRANSFORMATION PROGRESS DURING ISOTHERMAL HOLD` -- Y: 4.4".

**BLOCK B -- Transformation Progress Visualization**

Y: 5.0" to 13.5". Horizontal progress bar concept showing transformation completion over time.

Full width (23.0"). A series of five progress states shown as stacked horizontal bars with percentage labels.

**Background rectangle:** fill `#1E2435`, radius 8, full width, H: 8.0".

Five time-stamped states (vertically stacked, equal spacing):

| Time Point | % Transformed | Bar Fill Color | Microstructure State |
|---|---|---|---|
| 0 min (immersion) | 0% | `#E8A020` | 100% austenite -- part equalizing to salt bath temp |
| 15 min | ~25% | `#E8A020` to `#27AE60` gradient | Bainite nucleation beginning at grain boundaries |
| 30 min | ~60% | `#27AE60` dominant | Significant bainite formation -- transformation accelerating |
| 60 min | ~90% | `#27AE60` nearly full | Near-complete transformation -- small austenite islands remain |
| 90--120 min | 100% | `#27AE60` full | Complete bainite -- ready for removal |

Each state: Rounded rect bar, W: proportional to %, H: 0.8", inside a full-width track (fill `#252B3D`).

Left label: JetBrains Mono Regular, 14 pt, `#F0EDE8` -- time value.
Right label: Inter Medium, 13 pt, `#F0EDE8` -- microstructure description.
Percentage: Barlow Condensed ExtraBold, 18 pt, accent color, centered in bar.

**Note below visualization:**
- `Times shown are typical for medium-carbon alloy steel at 500 F salt bath temperature. Actual transformation times depend on steel grade, salt temperature, and section size. ADI may require 60--120 min.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**Key insight callout (Y: 13.2"):**
- Rounded rect, full width, H: 0.5", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Unlike conventional quenching, transformation happens at a CONSTANT temperature. This uniformity is what produces superior toughness.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Hold Time Guidelines

**Section label:** `RECOMMENDED HOLD TIMES BY MATERIAL AND SECTION` -- Y: 14.2".

**BLOCK C -- Hold Time Table**

Y: 14.8" to 20.8". Column widths (23.0" total):
- Material (5.5") | Section (3.5") | Salt Temp (4.0") | Hold Time (3.5") | Notes (6.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Material | Section | Salt Temp | Hold Time | Notes |
|---|---|---|---|---|
| 1075/1095 thin strip | 0.060--0.125" | 500--600 F | 30--45 min | Springs, clips -- fast transformation |
| 5160 spring steel | 0.25--0.50" | 500--600 F | 45--60 min | Coil and leaf springs |
| 4150/4340 structural | 0.5--1.0" | 450--550 F | 60--90 min | Gears, structural components |
| 52100 bearing | 0.25--0.50" | 450--500 F | 45--60 min | Carbide-free bainite target |
| ADI Grade 1 | Up to 1.0" | 700--750 F | 60--90 min | High ductility ausferrite |
| ADI Grade 3 | Up to 2.0" | 575--650 F | 90--120 min | Balanced strength and ductility |
| ADI Grade 5 | Up to 1.5" | 450--500 F | 90--120 min | Maximum hardness |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Material: Inter Medium, 13 pt.

**Rule-of-thumb callout below table:**
- Rounded rect, full width, H: 0.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `Rule of thumb: hold for at least 1.5x the estimated transformation time. Under-holding is far worse than over-holding.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 5 -- Early Pull = Bad

**Section label:** `WHAT HAPPENS IF YOU PULL TOO EARLY` -- Y: 21.2".

**BLOCK D -- Consequences Panel**

Y: 21.8" to 27.3". Three-panel horizontal layout.

**Panel 1 -- Complete Hold (X: 0.5", W: 7.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`, radius 6.

Title: `COMPLETE HOLD` -- Barlow SemiBold, 18 pt, `#27AE60`
Subtitle: `100% bainite` -- JetBrains Mono Regular, 13 pt, `#27AE60`

Body (Inter Regular 13 pt `#F0EDE8`):
```
All austenite transformed to bainite
in the salt bath. Air cooling is
non-critical -- nothing further
transforms.

Result: OPTIMAL
- Target hardness achieved
- Maximum toughness
- Stable microstructure
- No temper required
```

**Panel 2 -- Slightly Early (X: 8.0", W: 7.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `SLIGHTLY EARLY` -- Barlow SemiBold, 18 pt, `#E8A020`
Subtitle: `80--95% bainite + retained austenite` -- JetBrains Mono Regular, 13 pt, `#E8A020`

Body (Inter Regular 13 pt `#F0EDE8`):
```
Some austenite remains untransformed.
On air cooling, this austenite may
transform to MARTENSITE.

Result: MARGINAL
- Mixed bainite + martensite
- Higher hardness than expected
- Lower toughness
- Unpredictable properties
```

**Panel 3 -- Way Too Early (X: 15.5", W: 8.0"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`, radius 6.

Title: `WAY TOO EARLY` -- Barlow SemiBold, 18 pt, `#E05C5C`
Subtitle: `< 60% bainite + significant RA` -- JetBrains Mono Regular, 13 pt, `#E05C5C`

Body (Inter Regular 13 pt `#F0EDE8`):
```
Large volume of retained austenite
transforms to UNTEMPERED MARTENSITE
during air cooling.

Result: FAILURE
- Untempered martensite = brittle
- Cracking risk on further cooling
- Part does not meet any spec
- Scrap or re-process required
```

**Warning banner (Y: 27.0"):**
- Rounded rect, full width, H: 0.5", fill `#E05C5C` at 20%, border 2 pt `#E05C5C`
- Text: `RETAINED AUSTENITE that transforms to UNTEMPERED MARTENSITE on cooling is the #1 failure mode of under-held austempering.` -- Barlow SemiBold, 14 pt, `#E05C5C`, Center

---

### ZONE 6 -- Salt Bath Management During Hold

**Section label:** `OPERATIONAL MANAGEMENT DURING HOLD` -- Y: 27.7".

**BLOCK E -- Management Checklist**

Y: 28.3" to 32.3". Rounded rect, full width, H: 3.8", fill `#1E2435`, left accent `#27AE60`, radius 8.

Two-column layout:

**Left -- Monitor (W: 11.0"):**
- Title: `MONITOR DURING HOLD` -- Barlow SemiBold, 16 pt, `#27AE60`
- Items (Inter Medium 13 pt `#F0EDE8`):
```
Salt bath temperature (continuous readout)
Temperature recovery after load immersion
  -- bath may drop 10-30 F on loading
  -- hold time starts after recovery to setpoint
Agitation -- must run continuously
Salt level -- immersion must be complete
Timer -- start from temperature recovery, not immersion
```

**Right -- Do Not (W: 11.0"):**
- Title: `DO NOT DURING HOLD` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Items (Inter Medium 13 pt `#F0EDE8`):
```
Do NOT add a second load to the bath mid-cycle
  -- drops temperature, disrupts first load
Do NOT turn off agitation to "save energy"
Do NOT start hold timer before bath recovers temp
Do NOT estimate hold time -- use verified data
Do NOT open bath cover unnecessarily (heat loss)
```

---

### ZONE 7 -- Footer

Standard. Title: `Isothermal Hold -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897. Hold times are guidelines -- verify by metallographic examination of transformation completeness for your specific application.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Isothermal Hold Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The transformation progress visualization is the hero -- it makes an invisible process (solid-state phase transformation) visible as a progress bar. The three-panel "early pull" consequence layout uses the green/amber/coral traffic light pattern to drive home why patience matters. The "hold time starts after temperature recovery" point in Zone 6 is a critical operational detail that many shops get wrong -- it deserves prominence.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #638 -- Construction Workup v1.0*
*2026-04-26*
