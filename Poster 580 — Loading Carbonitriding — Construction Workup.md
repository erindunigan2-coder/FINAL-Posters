---
Project: Plating Posters Inc
Poster Number: 580
Title: "Loading -- Carbonitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding / Process 1 Section 1.8)"
Technical Source: Loading and fixturing requirements for gas carbonitriding. Fixture materials, part spacing, orientation, weight limits, quench entry orientation.
Process Scope: Carbonitriding loading and fixturing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - Loading
  - Fixturing
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #580 -- Construction Workup
## Loading -- Carbonitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Loading and fixturing determines whether every part in the load gets uniform gas contact and uniform quench cooling. A perfectly controlled atmosphere means nothing if parts are nested together -- the ammonia and endo gas cannot reach blocked surfaces, creating soft spots. This poster covers fixture selection, spacing rules, orientation for gas flow, orientation for quench entry, and load documentation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Furnace cross-section hero (Block B):** Simplified side-view of a sealed quench furnace showing the load on a tray, gas flow arrows around parts, and the quench tank below. Built with rectangles and arrows.
2. **Spacing rules panel (Block D):** Visual showing correct vs. incorrect part spacing.
3. **Fixture material table (Block E):** Comparison of fixture alloys.
4. **Loading do / don't strip (Block F):** 4 cards showing common mistakes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 13.5" / 20.0" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- FURNACE CROSS-SECTION HERO (2.9"--13.5" / ~10.6")
  Block B: Furnace diagram with load, gas flow, quench tank
ZONE 3 -- SPACING RULES (13.5"--20.0" / ~6.5")
  Block D: Correct vs. incorrect spacing visual + rules
ZONE 4 -- FIXTURE MATERIALS (20.0"--26.0" / ~6.0")
  Block E: Fixture alloy comparison table
ZONE 5 -- DO / DON'T STRIP (26.0"--32.5" / ~6.5")
  Block F: 4 loading mistake cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `LOADING & FIXTURING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Carbonitriding -- Every Part Needs Gas Contact and a Clean Quench Path` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Nest it, block it, or crowd it -- and the furnace will give you soft spots. Loading is not stacking.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Furnace Cross-Section (HERO)

**Section label:** `INSIDE THE SEALED QUENCH FURNACE` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Furnace Diagram**

Y: 3.8" to 13.0". Simplified side-view cross-section.

**Furnace body:**
- Rounded rect, X: 1.5", Y: 4.5", W: 21.0", H: 5.5"
- Fill: `#252B3D` (furnace interior)
- Border: 3 pt `#C8D0D8`
- Label above: `SEALED QUENCH FURNACE` Barlow SemiBold 16 pt `#C8D0D8`

**Load tray (inside furnace):**
- Rect, X: 3.0", Y: 7.5", W: 18.0", H: 0.3", fill `#C8D0D8`
- Label: `HT ALLOY TRAY / BASKET` JetBrains Mono 11 pt `#C8D0D8`

**Parts on tray (5 representative parts with spacing):**
- 5 small rounded rects on tray, W: 2.5", H: 2.0", fill `#27AE60` at 30%, border 1 pt `#27AE60`
- Spacing between parts: 0.8" gaps (representing 0.25 in minimum clearance)
- Labels inside parts: `PART` Inter Regular 10 pt `#27AE60`

**Gas flow arrows:**
- 8--10 curved arrows flowing around and between parts
- Stroke: 2 pt `#E8A020`, dashed
- Label: `Endo + NH3 gas flow` Inter Regular 12 pt `#E8A020`

**Quench tank (below furnace):**
- Rect, X: 1.5", Y: 10.5", W: 21.0", H: 2.0"
- Fill: `#E8A020` at 15%
- Border: 2 pt `#E8A020`
- Label: `OIL QUENCH TANK -- 120-180 F` Barlow SemiBold 14 pt `#E8A020`
- Sub-label: `Agitation propellers` Inter Regular 11 pt `#E8A020` at 70%

**Vertical arrow (furnace to quench):**
- Stroke: 3 pt `#3A4055`, arrowhead down
- Label: `Load drops into oil` Inter Medium 12 pt `#F0EDE8` at 60%

**Right-side callout (X: 16.0", Y: 4.8"):**
- Rounded rect, W: 6.5", H: 2.0", fill `#1E2435`, left accent `#27AE60`
- Text: `Minimum 0.25 in clearance between parts` JetBrains Mono 13 pt `#27AE60`
- Sub: `Gas must reach ALL surfaces` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 3 -- Spacing Rules

**Section label:** `SPACING -- THE DIFFERENCE BETWEEN UNIFORM AND REJECTED` -- Y: 13.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Correct vs. Incorrect**

Y: 14.3" to 19.8". Two side-by-side panels.

**Left -- CORRECT (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `CORRECT LOADING` -- Barlow SemiBold, 20 pt, `#27AE60`
- Visual: 4 small rects (parts) with visible gaps, arrows flowing between
- Rules (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
  - `0.25 in minimum clearance between all parts`
  - `Larger parts need more spacing`
  - `Orient for uniform gas flow (no dead zones)`
  - `Thin sections enter quench first when possible`
  - `Load map documented for traceability`

**Right -- INCORRECT (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `INCORRECT LOADING` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Visual: 4 small rects jammed together, no gaps, X marks
- Problems:
  - `Parts touching = soft spots (gas blocked)`
  - `Nesting = uneven case depth`
  - `Overloaded basket = non-uniform quench`
  - `No load map = no traceability`
  - `Random orientation = distortion risk`

---

### ZONE 4 -- Fixture Materials

**Section label:** `FIXTURE ALLOYS -- WHAT SURVIVES THE FURNACE` -- Y: 20.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Fixture Comparison Table**

Y: 20.8" to 25.8". Columns: Alloy (5.0") | Max Temp (3.5") | Pros (7.0") | Cons (7.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt.
Data rows: alternating `#1E2435` / `#252B3D`, H: 1.0".

| Alloy | Max Temp | Pros | Cons |
|---|---|---|---|
| Inconel 600/601 | 2100 F | Excellent oxidation resistance; long life | Expensive; heavy |
| RA330 | 2100 F | Good creep resistance; cost-effective | Carburizes over time at high Cp |
| HH/HK Cast Alloy | 2000 F | Lower cost than wrought alloys | Brittle with age; limited thermal cycling |
| Mild Steel | 1200 F | Cheap; readily available | Carburizes and becomes brittle rapidly; SHORT LIFE |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Mild steel row note in `#E05C5C`: `Not recommended for production carbonitriding fixtures`

Bottom callout: `Weight limit per tray/basket: 500--2000 lb depending on furnace size and fixture alloy creep strength at temperature` -- Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 5 -- Do / Don't Strip

**Section label:** `FOUR LOADING MISTAKES THAT COST LOADS` -- Y: 26.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- 4 Mistake Cards**

Y: 26.9" to 32.3".

| Card | X | Mistake | Consequence | Prevention |
|---|---|---|---|---|
| 1 | 0.5" | PARTS TOUCHING | Soft spots at contact areas | Minimum 0.25 in gap; inspect before closing door |
| 2 | 6.33" | OVERLOADED BASKET | Non-uniform quench; center parts cool slowly | Respect weight limits; test with worst-case load |
| 3 | 12.16" | WRONG QUENCH ORIENTATION | Thin sections warp; keyways crack | Thin section enters oil first; fixture to control entry |
| 4 | 18.0" | NO LOAD MAP | Cannot trace defect to load position | Document every load; photo recommended |

---

### ZONE 6 -- Footer

Standard footer. Title: `Loading -- Carbonitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Loading Carbonitriding -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Loading is the most overlooked stage in heat treatment -- and the most common root cause of non-uniform results. The furnace diagram hero should make the gas flow concept immediately obvious: gas flows AROUND parts, not through them. If parts are touching, gas cannot reach the contact zone, and that zone stays soft.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #580 -- Construction Workup v1.0*
*2026-04-26*
