---
Project: Plating Posters Inc
Poster Number: 642
Title: "Part Prep -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10: Martempering, Section 10.3)"
Process Scope: Part preparation for martempering -- cleaning, starting conditions, preheat requirements for heavy sections, and steel grade selection with Ms temperatures
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Martempering
  - PartPrep
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #642 -- Construction Workup
## Part Prep -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep for martempering centers on two things austempering does not require: knowing the exact Ms temperature of your steel (because the salt bath sits just above it), and preheating heavy sections (because thermal shock from austenitizing to salt bath cracking risk is real on thick parts). Steel selection is critical -- the steel must have enough hardenability to remain austenitic during the equalization hold. Lean alloys that would transform to pearlite or bainite during the hold are not candidates.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Steel grade + Ms temperature hero table (Block B):** Grades with Ms temps and recommended salt bath temps.
2. **Preheat decision tree (Block C):** When to preheat and when to skip.
3. **Cleaning requirements panel (Block D):** Standard cleaning for salt bath / hot oil.
4. **Hardenability requirement callout (Block E):** Why lean alloys fail in martempering.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal)
ZONE 3 -- STEEL GRADE + Ms TEMPERATURE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- PREHEAT DECISION (14.5"--20.5" / ~6.0")
ZONE 5 -- CLEANING & SURFACE CONDITION (20.5"--27.0" / ~6.5")
ZONE 6 -- HARDENABILITY REQUIREMENT (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Steel Selection, Ms Temperature & Preheat` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Know your Ms. Set your salt bath just above it. If the section is too thick, preheat first.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 of 9 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw or pre-machined part --> After: Clean, dry, steel verified, preheat planned if needed`

---

### ZONE 3 -- Steel Grade + Ms Temperature Hero

**Section label:** `STEEL GRADES FOR MARTEMPERING -- Ms TEMPERATURE REFERENCE` -- Y: 4.4".

**BLOCK B -- Grade Table**

Y: 5.0" to 14.0". Column widths (23.0" total):
- Grade (3.5") | Ms Temp (3.5") | Salt Bath Target (4.0") | Austenitize (3.5") | Applications (8.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Grade | Ms Temp | Salt Bath | Austenitize | Applications |
|---|---|---|---|---|
| 4340 | ~530 F (277 C) | 400--525 F | 1525--1575 F | Gears, shafts, structural components |
| 4140 | ~600 F (316 C) | 450--575 F | 1525--1575 F | General purpose; moderate sections |
| 52100 | ~410 F (210 C) | 300--400 F | 1525--1575 F | Precision bearing races (primary application) |
| D2 | ~375 F (191 C) | 275--365 F | 1825--1875 F | Cold-work die steel; tooling |
| H13 | ~600 F (316 C) | 450--575 F | 1825--1875 F | Hot-work dies, die-casting cores |
| M2 (HSS) | ~375 F (191 C) | 1000--1050 F* | 2175--2225 F | High-speed cutting tools |
| 4150 | ~570 F (299 C) | 425--550 F | 1525--1575 F | Heavy-duty shafts, gears |
| 8640 | ~580 F (304 C) | 435--560 F | 1525--1575 F | Automotive gears, fasteners |

*Note for M2: High-speed steels use a different martempering approach -- salt bath at 1000-1050 F for equalization before air cool. Ms is still ~375 F but the high austenitizing temperature requires intermediate cooling.

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Grade: Inter Medium, 14 pt, `#E8A020`.

**Key rule callout (Y: 13.0"):**
- Rounded rect, full width, H: 0.8", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `RULE: Salt bath temperature must be ABOVE Ms but BELOW the bainite start (Bs). This window is typically 20-50 F above Ms. Set too high = bainite forms (wrong process). Set too low = martensite starts in the salt (defeats the purpose).` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 4 -- Preheat Decision

**Section label:** `PREHEAT -- WHEN AND WHY` -- Y: 14.7".

**BLOCK C -- Decision Flowchart**

Y: 15.3" to 20.3". Horizontal decision flow with three nodes.

**Node 1 (X: 0.5", W: 6.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`, radius 6
- Text: `What is the section thickness?` -- Barlow SemiBold, 16 pt, `#E8A020`

Arrow right, labeled `< 2"` in `#27AE60`:

**Node 2a (X: 7.5", W: 7.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#27AE60`, radius 6
- Text: `NO PREHEAT NEEDED` -- Barlow SemiBold, 18 pt, `#27AE60`
- Detail: `Proceed directly to austenitizing. Thermal shock risk is low for thin-to-moderate sections.` -- Inter Regular, 12 pt, `#F0EDE8`

Arrow from Node 1, labeled `> 2"` in `#E8A020`:

**Node 2b (X: 7.5", W: 7.0", Y offset below 2a):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`, radius 6
- Text: `PREHEAT TO 800--1000 F` -- Barlow SemiBold, 18 pt, `#E8A020`
- Detail: `Hold 30--60 min. Equalizes temp before austenitizing. Reduces thermal shock on both furnace entry and salt quench.` -- Inter Regular, 12 pt, `#F0EDE8`

Arrow right from Node 2b:

**Node 3 (X: 15.5", W: 8.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#2EC4B6`, radius 6
- Title: `WHY PREHEAT?` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Points (Inter Regular, 12 pt, `#F0EDE8`):
```
- Heavy sections develop large temp
  gradients on rapid heating
- Gradient creates thermal stress
  = cracking risk during austenitizing
- Gradient persists into quench
  = non-uniform equalization in salt
- Preheat eliminates the gradient
  before the critical stages
```

---

### ZONE 5 -- Cleaning & Surface Condition

**Section label:** `CLEANING & SURFACE REQUIREMENTS` -- Y: 20.7".

**BLOCK D -- Cleaning Panel**

Y: 21.3" to 26.8". Two-column layout.

**Left -- Cleaning Steps (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Title: `CLEANING PROTOCOL` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Checklist items (Inter Medium 14 pt `#F0EDE8`):
```
[ ] Solvent degrease or alkaline wash -- remove all oil and grease
[ ] Remove scale and rust -- grit blast, wire brush, or pickling
[ ] Verify parts are COMPLETELY DRY -- no moisture
[ ] Inspect for cracks or pre-existing defects
[ ] If hot oil quench: ensure no salt contamination from other baths
[ ] If salt quench: ensure no oil contamination on parts
```

Each checkbox: 0.25" x 0.25" rounded rect, border 1 pt `#2EC4B6`.

**Right -- Why It Matters (X: 12.0", W: 11.5"):**

Three callout boxes stacked:

| Contaminant | Risk for Salt | Risk for Oil |
|---|---|---|
| Moisture on parts | Steam explosion in salt | Violent boil-over in oil |
| Oil / grease | Violent exothermic fire in salt (nitrate is oxidizer) | Accelerates oil degradation; flash point drops |
| Scale / oxide | Insulates surface = non-uniform quench | Same issue; scale trapped in oil contaminates bath |

Each: Rounded rect, H: 1.5", fill `#1E2435`, left accent `#E05C5C`. Risk text: Inter Regular 12 pt `#E05C5C`.

---

### ZONE 6 -- Hardenability Requirement

**Section label:** `WHY HARDENABILITY MATTERS FOR MARTEMPERING` -- Y: 27.2".

**BLOCK E -- Hardenability Panel**

Y: 27.8" to 32.3". Rounded rect, full width, H: 4.3", fill `#1E2435`, left accent `#E8A020`, radius 8.

Two-column layout:

**Left -- The Requirement (W: 12.0"):**

Title: `HIGH HARDENABILITY REQUIRED` -- Barlow SemiBold, 20 pt, `#E8A020`

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
During the 5-15 minute equalization hold in the salt bath,
the steel must remain 100% AUSTENITE. If the steel begins
transforming to bainite or pearlite during the hold, the
result is a mixed microstructure -- not the uniform tempered
martensite that martempering is designed to produce.

This is why low-hardenability steels (1040, 1045, plain carbon)
are NOT candidates for martempering unless in very thin sections.
The TTT diagram for the steel must show sufficient delay at the
hold temperature for the equalization time required.
```

**Right -- Quick Reference (W: 10.0"):**

Title: `SUITABLE vs. NOT SUITABLE` -- Barlow SemiBold, 16 pt, `#F0EDE8`

| Grade | Verdict | Reason |
|---|---|---|
| 4340 | EXCELLENT | High hardenability; large sections viable |
| 4140 | GOOD | Moderate hardenability; up to ~1.5" |
| 52100 | GOOD | Bearing steel; well-characterized for martempering |
| H13 | EXCELLENT | Tool steel; very high hardenability |
| 1045 | POOR | Low hardenability; only thin sections (< 0.5") |
| 1020 | NOT SUITABLE | Transforms during hold -- cannot martemper |

EXCELLENT/GOOD: `#27AE60`. POOR: `#E8A020`. NOT SUITABLE: `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Part Prep -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2759. Ms temperatures are approximate and vary with actual chemistry. Verify with Jominy end-quench or CCT data for your specific heat.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The Ms temperature table is THE reference on this poster -- operators need to look up their steel grade, find the Ms, and set their salt bath accordingly. The preheat decision tree is practical and simple -- section > 2" = preheat; section < 2" = skip. The hardenability panel drives home the fundamental requirement that distinguishes martempering candidates from non-candidates. The "suitable vs. not suitable" quick reference makes it actionable.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #642 -- Construction Workup v1.0*
*2026-04-26*
