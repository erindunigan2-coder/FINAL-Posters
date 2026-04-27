---
Project: Plating Posters Inc
Poster Number: 597
Title: "Part Preparation -- Plasma Nitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 5, Sections 5.4, 5.1)"
  - "Process 4 (Gas Nitriding), Section 4.7 -- Part Preparation"
Process Scope: Part preparation requirements for plasma nitriding -- cleaning, prior heat treatment, masking, surface condition
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PlasmaNitriding
  - PartPrep
  - ConstructionWorkup
  - DiffusionHeatTreatment
---

# Poster #597 -- Construction Workup
## Part Preparation -- Plasma Nitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Part prep is the foundation -- skip it, ruin the case. This poster covers everything that must happen before a part enters the plasma nitriding vessel: prior heat treatment requirements (Q&T with temper > nitriding temp + 50 F), surface cleaning, masking options (mechanical masking is unique to plasma), and material selection (which steels respond well to nitriding).

Hero visual: a decision-tree flow showing the prep sequence from incoming material through ready-to-load.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Prep sequence decision tree (Block B -- HERO):** Vertical flowchart with decision diamonds and action boxes.
2. **Steel grade suitability table (Block D):** Which steels nitride well and which do not.
3. **Prior heat treatment callout (Block E):** The critical "temper > nitride temp + 50 F" rule.
4. **Masking comparison (Block F):** Plasma vs. gas masking methods -- mechanical vs. electroplate stop-off.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PREP SEQUENCE HERO (2.9"--14.5")
  Block B: Vertical decision-tree flowchart
ZONE 3 -- STEEL GRADE TABLE (14.5"--22.0")
  Block D: Suitability table by steel category
ZONE 4 -- PRIOR HEAT TREATMENT + MASKING (22.0"--32.5")
  Block E: Q&T rule callout (left)
  Block F: Masking comparison (right)
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 88 pt `#F0EDE8`.
**Subheading:** `Plasma Nitriding -- Everything Before the Chamber Door Closes` -- 32 pt `#2EC4B6` (Teal).
**Tagline:** `Good surface prep is to nitriding what a great foundation is to a skyscraper. Get it wrong and nothing above it matters.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `+50 F` -- 72 pt `#E8A020`
- Label: `Prior temper must exceed nitriding temp by at least 50 F` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Prep Sequence (HERO)

**Section label:** `PREPARATION SEQUENCE -- FROM INCOMING TO READY-TO-LOAD` -- Y: 3.1".

**BLOCK B -- Decision-Tree Flowchart (Y: 3.8" to 14.3")**

Vertical flow, 6 action steps with 2 decision diamonds:

| Step | Type | Text | Detail | Accent |
|---|---|---|---|---|
| 1 | Action | VERIFY MATERIAL | Confirm steel grade contains nitride-forming elements (Cr, Mo, Al, V, Ti). Plain carbon steel will NOT nitride effectively. | `#2EC4B6` |
| D1 | Decision | NITRIDING STEEL? | YES -> proceed. NO -> STOP: select appropriate alloy or consider alternative process. | `#E8A020` |
| 2 | Action | VERIFY PRIOR Q&T | Part must be in quenched-and-tempered condition. Temper temperature must be >= nitriding temp + 50 F. Example: nitriding at 975 F requires prior temper >= 1025 F. | `#2EC4B6` |
| 3 | Action | STRESS RELIEVE | Stress relieve at 1050--1100 F after rough machining, before finish machining. Prevents distortion during long nitriding cycles. | `#2EC4B6` |
| 4 | Action | FINISH MACHINE | Nitriding does not change surface finish significantly. Parts CAN be finish-machined and ground before nitriding. Major advantage for precision components. | `#27AE60` |
| 5 | Action | DEGREASE / CLEAN | Chemically clean surface required. Solvent degreasing or alkaline wash. Any oil, grease, or oxide film blocks nitrogen absorption. | `#E05C5C` |
| D2 | Decision | SELECTIVE NITRIDING NEEDED? | YES -> apply mechanical mask. NO -> proceed to loading. | `#E8A020` |
| 6 | Action | APPLY MASK (IF NEEDED) | Plasma nitriding uses close-fitting steel masks (unique advantage). No electroplated stop-off required. Masked areas shielded from plasma. | `#E8A020` |

Action boxes: Rounded rect, W: 16.0", H: 1.2", fill `#1E2435`, left accent 0.06" in step color.
Decision diamonds: Rotated square, W: 2.5", fill `#252B3D`, border 2 pt `#E8A020`.
Arrows: 3 pt `#3A4055`, arrowhead filled.

---

### ZONE 3 -- Steel Grade Suitability

**Section label:** `WHICH STEELS RESPOND TO PLASMA NITRIDING?` -- Y: 14.7".

**BLOCK D -- Suitability Table (Y: 15.3" to 21.8")**

| Category | Grades | Surface Hardness (HV) | Response | Notes |
|---|---|---|---|---|
| Nitralloy | 135M (AMS 6471), N (AMS 6470) | 900--1100 | EXCELLENT | Purpose-designed; ~1% Al |
| Chrome-Moly | 4140, 4340, 4150 | 500--700 | GOOD | Cr + Mo nitrides |
| Hot Work Tool | H11, H13 | 900--1100 | EXCELLENT | High Cr + Mo + V |
| Precipitation Hardening | 17-4PH, 15-5PH | 1000--1200 | EXCELLENT | |
| Austenitic Stainless | 304, 316, 316L | 900--1200 | EXCELLENT (plasma only) | Low-temp < 800 F; "S-phase" -- unique to plasma |
| Tool Steels | M2, M42, D2, A2 | 1000--1200 | EXCELLENT | V + Cr form hard nitrides |
| Plain Carbon | 1018, 1045 | < 400 | DO NOT USE | No nitride-forming elements |

"EXCELLENT" in `#27AE60`. "DO NOT USE" in `#E05C5C`.
Header: `#3A4055` fill. Data: alternating rows. JetBrains Mono 12 pt.

---

### ZONE 4 -- Prior Heat Treatment + Masking

**Two-column layout (Y: 22.2" to 32.3")**

**Left -- BLOCK E: The Q&T Rule (X: 0.5", W: 11.0")**

Section label: `THE CRITICAL RULE` -- Barlow Condensed ExtraBold 22 pt `#E8A020`.

Callout box: Rounded rect, H: 9.5", fill `#1E2435`, left accent `#E8A020`.

Content:
- Rule: `Prior temper must be >= nitriding temperature + 50 F` -- Barlow SemiBold 18 pt `#E8A020`
- Why: `If nitriding temperature exceeds the prior temper, the CORE softens during the long nitriding cycle. The core properties collapse.` -- Inter Regular 14 pt `#F0EDE8`
- Example box (inner callout, fill `#252B3D`):
  - `Nitriding at 975 F -> Prior temper >= 1025 F` JetBrains Mono 14 pt `#27AE60`
  - `Nitriding at 1050 F -> Prior temper >= 1100 F` JetBrains Mono 14 pt `#27AE60`
- Additional: `Stress relieve at 1050--1100 F after rough machining. Finish machine AFTER stress relief, BEFORE nitriding.` Inter Medium 13 pt `#F0EDE8`
- Surface finish note: `Nitriding growth is only 0.0001--0.0005 inch per surface. Parts can be finish-ground before nitriding.` Inter Regular 13 pt `#2EC4B6`

**Right -- BLOCK F: Masking Comparison (X: 12.0", W: 11.5")**

Section label: `SELECTIVE NITRIDING -- MASKING OPTIONS` -- Barlow Condensed ExtraBold 22 pt.

Two stacked callout boxes:

*Top -- Plasma Masking (Emerald):*
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `PLASMA: MECHANICAL MASKING` -- Barlow SemiBold 18 pt `#27AE60`
- `Close-fitting steel masks shield areas from plasma`
- `No electroplating required`
- `Reusable masks -- lower per-part cost`
- `Mask must make close contact -- gaps allow plasma penetration`
- `UNIQUE TO PLASMA -- not possible in gas nitriding`

*Bottom -- Gas Nitriding Masking (Amber):*
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `GAS: ELECTROPLATE STOP-OFF` -- Barlow SemiBold 18 pt `#E8A020`
- `Tin plate 0.0003--0.0005 inch`
- `Copper plate 0.0005--0.001 inch`
- `Commercial stop-off paints available`
- `Must be stripped after nitriding`
- `Per-part cost for plating`

---

### ZONE 5 -- Footer

Standard footer. Title: `Part Preparation -- Plasma Nitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #597 -- Construction Workup v1.0 -- 2026-04-26*
