---
Project: Plating Posters Inc
Poster Number: 188
Title: "Chromate Conversion (Tri) -- Main Stage"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.6)"
Technical Source: Trivalent chromium conversion coating main bath. Cr3+/Zr/Ti mixed oxide gel deposition on aluminum. MIL-DTL-5541 Type II. pH 3.5--4.2 (narrow window). Stage 5 of 7.
Process Scope: Trivalent chromate conversion coating -- main stage -- Stage 5 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - MainStage
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #188 -- Construction Workup
## Chromate Conversion (Tri) -- Main Stage

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 7. This is the heart of the trivalent chromate process -- where the Cr3+/Zr/Ti mixed oxide barrier film forms on the aluminum substrate. This is the densest poster in the CC-05 cluster. It covers bath chemistry, the reaction mechanism, the critical narrow pH window (3.5--4.2), film characteristics, and the fundamental difference from hex chromate: NO self-healing.

Hero visual: a reaction mechanism diagram showing aluminum dissolution, Zr/Ti fluorocomplex hydrolysis, and Cr3+ co-deposition as a mixed oxide gel on the surface.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Reaction mechanism hero (Block B):** Layered diagram showing aluminum surface, solution interface, and film formation. Arrows show Al dissolution (downward), local pH rise, and Zr/Cr oxide precipitation. Built with rectangles, layers, and labeled arrows.
2. **Bath chemistry panel (Block D):** Three-component breakdown (Cr3+, Zr4+/Ti4+, Fluoride activator).
3. **pH window gauge (Block E):** Visual bar showing the narrow 3.5--4.2 operating window vs. hex chrome's wider 1.3--1.8 range.
4. **Film characteristics comparison (Block F):** Tri vs. hex film properties side by side.
5. **Defect grid (Block G):** 5 common coating failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 19.5" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- REACTION MECHANISM HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- BATH CHEMISTRY + pH WINDOW (13.5"--19.5" / ~6.0")
ZONE 5 -- FILM CHARACTERISTICS (19.5"--25.5" / ~6.0")
ZONE 6 -- DEFECT DIAGNOSIS (25.5"--32.5" / ~7.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TRIVALENT CHROMATE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Conversion Coating on Aluminum -- Main Stage -- Stage 5 of 7` -- 30 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `No Cr6+. No self-healing. A Cr3+/Zr/Ti barrier film that meets MIL-DTL-5541 Type II -- if you hold the pH.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, deoxidized aluminum surface  -->  After: Cr3+/Zr/Ti mixed oxide barrier film`

---

### ZONE 3 -- Reaction Mechanism Hero

**Section label:** `HOW THE TRIVALENT COATING FORMS` -- Y: 4.4".

**BLOCK B -- Reaction Mechanism Diagram**

Y: 5.0" to 13.0".

**Three-layer schematic (bottom to top):**

**Layer 1 -- Aluminum Substrate (bottom):**
- Rectangle, X: 2.0", Y: 11.0", W: 20.0", H: 1.5", fill `#C8D0D8` at 40%
- Label: `ALUMINUM SUBSTRATE` Barlow SemiBold 14 pt `#C8D0D8`
- Reaction: `Al --> Al3+ + 3e-` JetBrains Mono 14 pt `#E8A020`
- Arrow pointing upward from surface labeled `Al3+ dissolves into solution`

**Layer 2 -- Interface Zone (middle):**
- Rectangle, X: 2.0", Y: 9.0", W: 20.0", H: 2.0", fill `#27AE60` at 15%
- Label: `REACTION INTERFACE -- pH RISES HERE` Barlow SemiBold 13 pt `#27AE60`
- Left side reactions:
  - `ZrF62- + 2H2O --> ZrO2 + 6F- + 4H+` JetBrains Mono 12 pt `#2EC4B6`
  - `(pH rise drives hydrolysis)` Inter Regular 11 pt `#F0EDE8` at 60%
- Right side:
  - `Cr3+ co-deposits with ZrO2` JetBrains Mono 12 pt `#27AE60`
  - `Al2O3 from substrate dissolution` JetBrains Mono 12 pt `#C8D0D8`
  - `F- bridges in film structure` JetBrains Mono 12 pt `#E8A020`

**Layer 3 -- Bulk Solution (top):**
- Rectangle, X: 2.0", Y: 5.5", W: 20.0", H: 3.5", fill `#252B3D` at 30%
- Chemistry labels:
  - `Cr3+: 0.5--2.0 g/L` JetBrains Mono 14 pt `#27AE60`
  - `Zr4+: 0.5--3.0 g/L (as H2ZrF6)` JetBrains Mono 14 pt `#2EC4B6`
  - `Free F-: 0.5--2.0 g/L` JetBrains Mono 14 pt `#E8A020`
  - `pH: 3.5--4.2` JetBrains Mono 16 pt `#E05C5C` (emphasized -- this is the critical control)
  - `65--95 F (18--35 C)` JetBrains Mono 13 pt `#F0EDE8`
  - `2--5 min immersion` JetBrains Mono 13 pt `#F0EDE8`

**Film Result Arrow (right side, pointing to interface layer):**
- `RESULT: ZrO2/Cr2O3/Al2O3 mixed oxide gel` Barlow SemiBold 14 pt `#27AE60`
- `0.02--0.10 um thick (1--4 uin)` JetBrains Mono 12 pt `#F0EDE8`
- `NO Cr6+ in the film` Inter Medium 13 pt `#E05C5C`

**Key insight callout (bottom of zone):**
- `Unlike hex chromate, there is NO Cr6+ reduction step. The chromium is already Cr3+ in solution. The film forms by co-deposition of Cr3+ with Zr/Ti oxides as local pH rises at the aluminum surface.`
- Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Bath Chemistry + pH Window

**Two-column layout (Y: 13.7" to 19.3"):**

**Left -- Bath Chemistry (X: 0.5", W: 12.0"):**

Section label: `BATH CHEMISTRY` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 13.7".

Three-component callout boxes (Y: 14.3" to 17.5"):

| Component | Accent | Concentration | Role |
|---|---|---|---|
| Cr3+ (chromium III) | `#27AE60` | 0.5--2.0 g/L | Film-forming element; barrier protection |
| Zr4+ / Ti4+ (fluorocomplexes) | `#2EC4B6` | 0.5--3.0 g/L | Primary barrier-forming; hydrolyzes at surface |
| Fluoride (F-) | `#E8A020` | 0.5--2.0 g/L free | Activator -- dissolves Al2O3 barrier |

Each box: Rounded rect H: 1.0", fill `#1E2435`, left accent 0.06".

**Operating parameters mini-table (Y: 17.8" to 19.3"):**

| Parameter | Immersion | Spray |
|---|---|---|
| Temperature | 65--95 F (18--35 C) | 70--90 F (21--32 C) |
| Time | 2--5 min (typ. 3--4 min) | 1--3 min |
| pH | 3.5--4.2 | 3.5--4.2 |
| Agitation | Mild air or mechanical | N/A |

Data: JetBrains Mono 12 pt.

**Right -- pH Window Gauge (X: 13.0", W: 10.5"):**

Section label: `THE CRITICAL pH WINDOW` Barlow Condensed ExtraBold 22 pt `#E05C5C`. Y: 13.7".

**Tri chromate pH gauge (Y: 14.5"):**
Horizontal bar, W: 10.0", H: 0.6":
- Red zone left: `< 3.0` fill `#E05C5C` at 40% -- `White haze / powdery`
- Yellow zone: `3.0--3.5` fill `#E8A020` at 30% -- `Thin but usable`
- Green zone: `3.5--4.2` fill `#27AE60` at 40% -- `OPTIMAL`
- Yellow zone: `4.2--4.5` fill `#E8A020` at 30% -- `Coating thinning`
- Red zone right: `> 4.5` fill `#E05C5C` at 40% -- `No coating`
Labels: JetBrains Mono 11 pt. Optimal marker: triangle at `3.8`.

**Hex chromate pH gauge (for comparison, Y: 16.0"):**
Label: `For comparison: Hex Chromate (Type I)` Inter Medium 13 pt `#F0EDE8` at 60%.
Horizontal bar, W: 10.0", H: 0.4":
- Green zone: `1.3--1.8` fill `#27AE60` at 30% -- much wider relative to scale

Contrast callout box (Y: 17.0"):
- Rounded rect, H: 2.0", fill `#1E2435`, left accent 0.06" `#E05C5C`
- `Tri pH window: 0.7 units wide (3.5--4.2)` JetBrains Mono 14 pt `#E05C5C`
- `Hex pH window: 0.5 units wide (1.3--1.8)` JetBrains Mono 13 pt `#F0EDE8` at 60%
- `But hex is far more forgiving of drift -- the oxidizing power compensates for pH excursions. Tri has no such safety net.` Inter Regular 13 pt `#F0EDE8`
- `MONITOR pH CONTINUOUSLY.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Film Characteristics

**Section label:** `FILM CHARACTERISTICS -- TRI VS. HEX AT A GLANCE` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 19.7".

**Comparison table (Y: 20.3" to 25.3"):**

| Property | Trivalent (Type II) | Hexavalent (Type I) |
|---|---|---|
| Film composition | ZrO2/Cr2O3/Al2O3 mixed oxide | Cr2O3/CrO4 2-/Al2O3 gel |
| Cr6+ in film | ZERO | 10--30% of total Cr |
| Self-healing | NO | YES (Cr6+ migrates to damage) |
| Appearance | Clear to pale blue/iridescent | Gold to golden-brown |
| Thickness | 0.02--0.10 um (1--4 uin) | 0.25--1.0 um (10--40 uin) |
| Coating weight | 2--15 mg/ft2 | 10--40 mg/ft2 |
| Salt spray bare (ASTM B117) | 168 hr min (Class 1A) | 168--336 hr (Class 1A) |
| Electrical resistance | Very low (< 0.1 milliohm/in2) | Low (0.001--5 milliohm/in2) |
| Thermal stability | More stable (no Cr6+ to lose) | Degrades > 140 F (60 C) |
| Regulatory | RoHS + REACH compliant | Restricted / phasing out |

Column headers: Barlow SemiBold 14 pt. Tri column: `#27AE60`. Hex column: `#E05C5C`.
Data: JetBrains Mono 12 pt `#F0EDE8`. Alternating rows.

Spec callout (below table):
- `MIL-DTL-5541F Type II -- Class 1A (corrosion protection) and Class 3 (low resistance)` JetBrains Mono 12 pt `#2EC4B6`
- `Also: AMS 2487 | ASTM B921 | SAE ARP 6584 | NADCAP AC7108` JetBrains Mono 11 pt `#F0EDE8` at 60%

---

### ZONE 6 -- Defect Diagnosis

**Section label:** `WHAT GOES WRONG -- 5 COATING FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 25.7".

**5-card layout (Y: 26.3" to 32.3"):**

Top row: 3 cards. Bottom row: 2 cards centered.

| Position | Problem | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | NO COATING | `#E05C5C` | pH > 4.5; fluoride depleted; surface not activated | Adjust pH; add fluoride; check deox step |
| R1C2 | WHITE HAZE | `#E8A020` | Over-immersion; pH < 3.0; excess fluoride | Reduce time; adjust pH upward; check F- |
| R1C3 | RAINBOW FILM | `#2EC4B6` | Normal variation on some alloys | Usually acceptable -- verify coating weight and SST |
| R2C1 | FAILED 168 HR SST | `#E05C5C` | Coating too thin; contamination; no sealer | Increase time; improve cleaning; add sealer |
| R2C2 | BLUE/PURPLE SPOTS | `#E8A020` | Zr precipitation; bath contamination | Check bath chemistry; filter; verify pH |

Top row cards: W: 7.33", H: 2.5". Bottom row cards: W: 7.33", centered. Fill `#1E2435`, radius 6, left accent 0.06".

---

### ZONE 7 -- Footer

Standard footer. Title: `Chromate Conversion (Trivalent) -- Main Stage`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for trivalent chromium conversion coating on aluminum per MIL-DTL-5541 Type II. Specific formulations and process limits vary by proprietary product. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Chromate Tri Main Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the CC-05 cluster. The reaction mechanism diagram must be clear at wall distance -- use large arrows and bold labels. The pH window gauge is THE single most important visual -- it makes the narrow operating range visceral. The Tri vs. Hex film characteristics table is the reference payoff -- a shop engineer should be able to answer "what exactly is different about tri?" by reading this table.

Watson flag: Confirm current MIL-DTL-5541F revision still requires 168 hr SST minimum for Type II Class 1A.
Tyler flag: Validate that pH 3.5--4.2 is the consensus range across major TCP suppliers (Surtec 650, Alodine 5700, TCP-HF).

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #188 -- Construction Workup v1.0*
*2026-04-26*
