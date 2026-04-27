---
Project: Plating Posters Inc
Poster Number: 633
Title: "Part Prep -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering)"
Process Scope: Part preparation for austempering -- cleaning, steel selection, section thickness limits
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - PartPrep
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #633 -- Construction Workup
## Part Prep -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part preparation for austempering is dominated by two questions: (1) is the steel suitable, and (2) is the section thin enough? Unlike conventional quench-and-temper, austempering has a hard section-thickness limit -- the part must cool through the pearlite nose fast enough to avoid pearlite formation. This makes steel selection and hardenability evaluation the most important prep steps.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Steel selection hero (Block B):** Table of suitable grades with hardenability notes and max section thickness.
2. **Section thickness decision tree (Block C):** Visual flowchart -- is the section thin enough for the steel grade?
3. **Cleaning requirements panel (Block D):** Standard cleaning checklist.
4. **TTT diagram concept (Block E):** Simplified TTT sketch showing why section thickness matters.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal)
ZONE 3 -- STEEL SELECTION HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- SECTION THICKNESS LIMITS (14.0"--20.5" / ~6.5")
ZONE 5 -- CLEANING & SURFACE PREP (20.5"--27.0" / ~6.5")
ZONE 6 -- THE TTT CONCEPT (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Steel Selection & Surface Condition` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Austempering only works if the steel can get there. Wrong grade or too-thick section = pearlite instead of bainite.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 of 9 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw part with known steel grade --> After: Clean, verified, ready for furnace loading`

---

### ZONE 3 -- Steel Selection Hero

**Section label:** `SUITABLE STEEL GRADES FOR AUSTEMPERING` -- Y: 4.4".

**BLOCK B -- Steel Grade Table**

Y: 5.0" to 13.5". Column widths (23.0" total):
- Category (4.0") | Grades (5.5") | Max Section (3.5") | Notes (10.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt.

| Category | Grades | Max Section | Notes |
|---|---|---|---|
| Spring steels | 1075, 1095, 5160, 6150 | 0.200" (plain C) / 0.5" (alloy) | Classic austempering candidates -- springs, clips, wire forms |
| Medium-carbon alloy | 4140, 4150, 4340, 8640 | 1.0--1.5" | Excellent hardenability; larger sections possible |
| Ductile cast iron | 80-55-06, 100-70-03, 120-90-02 | Per ADI spec | ADI (austempered ductile iron) -- premium application |
| Thin plain carbon | 1060, 1075, 1095 | ~0.200" max | Thin springs, clips, fasteners only |
| NOT SUITABLE | 1018, 1020 (low carbon) | -- | Insufficient carbon for useful bainite hardness |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`. NOT SUITABLE row: `#E05C5C` accent.

**Rule-of-thumb callout (Y: 13.0"):**
- Rounded rect, full width, H: 0.7", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Rule of thumb: best candidates have 0.40--1.00% carbon and sufficient hardenability to avoid the pearlite nose during quench to the salt bath.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Section Thickness Limits

**Section label:** `SECTION THICKNESS -- THE HARD LIMIT` -- Y: 14.2".

**BLOCK C -- Decision Flowchart**

Y: 14.8" to 20.3". Horizontal flowchart with 4 decision nodes.

Node 1: `What is the steel grade?`
- Plain carbon (1060-1095) --> `Max ~0.200"`
- Alloy steel (4140, 5160, etc.) --> `Max 0.5--1.5"`
- Ductile iron --> `Per ASTM A897 grade`

Node 2: `Can the part cool through the pearlite nose in the TTT diagram before reaching the salt bath temperature?`
- YES --> Proceed to austempering
- NO --> `Consider martempering or conventional Q&T instead`

Each node: Rounded rect, fill `#1E2435`, border 1 pt accent color, radius 6.
Decision arrows: 2 pt `#3A4055`, labeled YES (`#27AE60`) / NO (`#E05C5C`).

**Key insight callout:**
- `The pearlite nose is typically at 1000--1100 F for most steels. The part must cool from austenitizing temperature THROUGH this range fast enough that no pearlite forms. Thicker sections cool slower at the core -- that is why section thickness is the limiting factor.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 5 -- Cleaning & Surface Prep

**Section label:** `CLEANING & SURFACE CONDITION` -- Y: 20.7".

**BLOCK D -- Prep Checklist**

Y: 21.3" to 26.8". Two-column layout.

**Left -- Cleaning Steps (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Checklist items (Inter Medium 14 pt `#F0EDE8`):

```
[ ] Solvent degrease or alkaline wash -- remove all oil and grease
[ ] Remove scale and rust -- wire brush, grit blast, or pickling
[ ] Verify surface is dry -- no moisture permitted near salt bath
[ ] Stress relieve if prior cold work (1100--1200 F, 1 hr)
[ ] Inspect for cracks or defects before processing
```

Each checkbox: 0.25" x 0.25" rounded rect, border 1 pt `#2EC4B6`.

**Right -- Why It Matters (X: 12.0", W: 11.5"):**

Three callout boxes stacked vertically:

| Contaminant | Risk |
|---|---|
| Oil / grease on surface | Nitrate salt + organic = violent exothermic reaction (FIRE) |
| Moisture on parts | Steam explosion on salt bath immersion -- catastrophic |
| Scale / oxide | Uneven heat transfer = non-uniform microstructure |

Each: Rounded rect, H: 1.5", fill `#1E2435`, left accent `#E05C5C`. Risk text: Inter Regular 13 pt `#E05C5C`.

---

### ZONE 6 -- The TTT Concept

**Section label:** `WHY SECTION THICKNESS MATTERS -- THE TTT DIAGRAM` -- Y: 27.2".

**BLOCK E -- Simplified TTT Sketch**

Y: 27.8" to 32.3". Conceptual diagram (built with rectangles and lines, not a rendered chart).

Vertical axis label: `TEMPERATURE` (Barlow SemiBold, 14 pt, vertical)
Horizontal axis label: `TIME (log scale)` (Barlow SemiBold, 14 pt)

Key regions labeled:
- Top: `AUSTENITE (stable above Ac3)` -- `#E8A020`
- Middle-left nose: `PEARLITE NOSE -- AVOID THIS` -- `#E05C5C`, bold
- Lower region: `BAINITE FORMATION ZONE (400--700 F)` -- `#27AE60`
- Bottom: `MARTENSITE START (Ms)` -- `#E8A020`, dashed line

Two cooling curves (dashed lines):
- Fast (thin section): curves steeply left of pearlite nose down to bainite zone -- labeled `THIN SECTION -- clears pearlite nose` in `#27AE60`
- Slow (thick section): curves through pearlite nose -- labeled `THICK SECTION -- hits pearlite nose = FAIL` in `#E05C5C`

Bottom note: `This is why austempering is limited to thin sections of plain carbon steel. Alloy steels shift the pearlite nose to the right (more time), allowing thicker sections.` -- Inter Medium, 13 pt, `#F0EDE8`

---

### ZONE 7 -- Footer

Standard. Title: `Part Prep -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The TTT diagram concept in Zone 6 is the educational centerpiece -- it explains WHY section thickness matters in a visual way that a shop-floor operator can grasp. Keep it schematic, not mathematically precise. The steel selection table is the practical reference -- operators need to know at a glance whether their part is a good candidate.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #633 -- Construction Workup v1.0*
*2026-04-26*
