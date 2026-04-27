---
Project: Plating Posters Inc
Poster Number: 624
Title: "Part Prep -- Flame Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 8, Section 8.3)"
Technical Source: Part preparation for flame hardening. Same requirements as induction hardening (clean, decarb-free, adequate carbon) plus additional concerns for large castings (stress relief before hardening) and edge preparation (thin edges overheat first).
Process Scope: Flame hardening -- part preparation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FlameHardening
  - PartPrep
  - ConstructionWorkup
  - ClusterHT08
---

# Poster #624 -- Construction Workup
## Part Prep -- Flame Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep for flame hardening shares fundamentals with induction -- clean surface, adequate carbon, decarb-free -- but adds a concern unique to flame work: large castings and forgings may need stress relief before flame hardening to prevent cracking from thermal shock. The flame delivers intense localized heat, and pre-existing residual stresses from casting or machining can combine with thermal stresses to crack the part.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Material verification panel (Block B -- HERO):** Steel and cast iron grades suitable for flame hardening with expected hardness.
2. **Surface condition checklist (Block D):** Go/no-go items specific to flame hardening.
3. **Stress relief callout (Block E):** When and why to stress relieve before flame hardening.
4. **Edge preparation warning (Block F):** Thin edges and sharp corners in flame hardening.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- MATERIAL VERIFICATION / HERO (4.2"--14.5" / ~10.3")
  Block B: Steel and cast iron grade table
  Block C: "Carbon Content = Maximum Hardness" callout
ZONE 4 -- SURFACE CONDITION CHECKLIST (14.5"--22.0" / ~7.5")
  Block D: Go/no-go surface checklist
ZONE 5 -- STRESS RELIEF + EDGE PREP (22.0"--32.5" / ~10.5")
  Block E: Stress relief panel
  Block F: Edge preparation warning
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flame Hardening -- Stage 2 of 9` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Same metallurgical rules as induction -- but large castings and forgings add the stress relief question. Clean, carbon-verified, decarb-free.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw, as-received material  -->  After: Verified, cleaned, stress-relieved (if needed), ready for setup`

---

### ZONE 3 -- Material Verification (HERO)

**Section label:** `MATERIAL VERIFICATION -- CONFIRM BEFORE YOU LIGHT THE TORCH` -- Y: 4.4".

**BLOCK B -- Grade Table**

Y: 5.0" to 12.0". Full-width table.

Column widths (23.0" total):
- Category (4.0") | Grades (5.5") | Carbon % (3.0") | Surface HRC (3.0") | Notes (7.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Category | Grades | Carbon % | Surface HRC | Notes |
|---|---|---|---|---|
| Medium carbon (workhorse) | 1045, 1050, 1055 | 0.43--0.55 | 58--62 | THE standard flame hardening steels |
| Alloy (medium C) | 4140, 4150, 4340 | 0.38--0.53 | 58--62 | Higher hardenability; less quench-sensitive |
| High carbon | 1060, 1070, 1095 | 0.55--1.00 | 60--65 | Springs, dies, ways |
| Gray cast iron | Class 40+ | 3.0--3.8 (total) | 45--55 | Lathe ways, cylinder liners, brake drums |
| Ductile cast iron | 80-55-06, 100-70-03 | 3.5--3.8 (total) | 50--58 | Gears, sprockets, cams |
| NOT SUITABLE | 1018, 1020, 8620 | < 0.30 | -- | Too low carbon for surface hardening |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.85".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. "NOT SUITABLE" row: `#E05C5C` text.

**BLOCK C -- Carbon = Hardness Callout**

Y: 12.3" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.8", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `CARBON CONTENT = MAXIMUM HARDNESS` -- Barlow SemiBold 16 pt `#E8A020`
- Text: `0.40% C -> 56--58 HRC max | 0.45% C -> 58--60 HRC max | 0.50% C -> 60--62 HRC max | 0.60%+ C -> 62--65 HRC max. No amount of flame intensity will overcome insufficient carbon. Verify carbon BEFORE processing.` -- JetBrains Mono Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Surface Condition Checklist

**Section label:** `SURFACE CONDITION -- GO / NO-GO` -- Y: 14.7".

**BLOCK D -- Checklist**

Y: 15.3" to 21.8". Full-width.

| Item | Status | Detail |
|---|---|---|
| Scale-free surface | GO | Heavy scale insulates and creates hot/cold spots under flame |
| Rust-free | GO | Same as scale -- barrier to uniform heating |
| Oil/grease-free | GO | Burns under flame; creates smoke; uneven heating pattern |
| No stop-off needed | NOTE | Flame is inherently selective -- only areas exposed to flame are hardened |
| Decarburization-free | GO | Check with microhardness or nital etch on sample from same lot |
| Proper prior microstructure | GO | Q&T or normalized preferred; annealed acceptable for flame (slower heating than induction) |
| Deburr thin edges | GO | Thin edges and sharp corners overheat first under flame -- can melt or crack |
| Dimensional check | GO | Parts must be within tolerance BEFORE hardening |

Each row: Rounded rect H: 0.7", fill alternating `#1E2435` / `#252B3D`.
Status badge: GO = `#27AE60`, NOTE = `#E8A020`.
Item: Inter Medium 13 pt. Detail: Inter Regular 12 pt `#F0EDE8` at 75%.

---

### ZONE 5 -- Stress Relief + Edge Prep

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Stress Relief (X: 0.5", W: 11.0"):**

Section label: `STRESS RELIEF BEFORE FLAME HARDENING` Barlow Condensed ExtraBold 24 pt.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
WHEN TO STRESS RELIEVE:

- Large castings (gray iron, ductile iron)
  with complex geometry
- Heavy forgings with residual forging stress
- Parts with extensive prior machining
  (machining creates surface residual stress)
- Parts with abrupt section changes

WHY:
Flame hardening creates intense localized
thermal stress. Combined with pre-existing
residual stress, total stress can exceed the
material's strength --> CRACKING.

STRESS RELIEF PARAMETERS:
  Temperature: 1050--1200 F (565--650 C)
  Time: 1 hour per inch of section thickness
  Cool: Furnace cool to 500 F, then air cool

WHEN TO SKIP:
Simple shapes, uniform sections, small parts,
previously heat-treated (already stress-relieved).
```

Data: JetBrains Mono Regular 13 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Edge Preparation (X: 12.0", W: 11.5"):**

Section label: `EDGES AND CORNERS -- THE OVERHEAT ZONE` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
THE PROBLEM:
Thin edges and sharp corners heat FASTER
than bulk material because:
  - Less mass to absorb heat
  - Greater surface-to-volume ratio
  - Flame wraps around edges (dual-side
    heating)

CONSEQUENCES:
  - Overheating (grain growth, melting)
  - Cracking at corners
  - Distortion of thin sections

PREVENTION:
  - Radius all sharp corners before flame
    hardening (min R = 0.060 in / 1.5 mm)
  - Deburr all machining edges
  - Direct flame AWAY from thin edges when
    possible
  - Reduce torch distance and dwell at edges
  - Consider preheat for thick-to-thin
    transitions

CAST IRON SPECIAL:
Gray iron is notch-sensitive. Flame hardening
a sharp internal corner on a gray iron casting
is a guaranteed crack. Radius first.
```

Bottom highlight: `If you cannot radius the edge, you may not be able to flame harden it safely.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Footer

Standard footer. Title: `Part Prep -- Flame Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; foundry best practices for cast iron flame hardening.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep Flame Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The stress relief panel is the flame-specific content that distinguishes this from the induction part prep poster (#615). Flame hardening is more commonly applied to large castings and forgings than induction, and these parts carry residual stresses from their manufacturing process. The edge preparation warning applies to both flame and induction but is more critical for flame because the operator has less precise control of heat input -- it is easy to dwell too long on an edge.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #624 -- Construction Workup v1.0*
*2026-04-26*
