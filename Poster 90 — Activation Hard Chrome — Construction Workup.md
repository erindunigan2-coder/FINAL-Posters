---
Project: Plating Posters Inc
Poster Number: 90
Title: "Activation -- Hard Chrome"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
Technical Source: Activation for hard chrome -- reverse etch (anodic etching) in the chrome bath itself. The part is made the ANODE for 30 sec to 3 min at 100-200 ASF, dissolving surface oxide and roughening the surface for adhesion. Then polarity is reversed and plating begins in the same tank. This is THE standard activation for hard chrome. External acid etch is used only when reverse etch is insufficient.
Process Scope: Activation (reverse etch) -- Stage 3 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HardChrome
  - Activation
  - ReverseEtch
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #90 -- Construction Workup
## Activation -- Hard Chrome

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. This is the most distinctive activation step in the entire poster series: reverse etch. The part is immersed in the chrome bath and made the ANODE (polarity reversed). Chromium dissolves from the surface, oxide is removed, and the surface is roughened for adhesion. After 30 sec to 3 min, polarity is reversed and plating begins. It all happens in one tank. No separate activation chemical. No transfer between tanks. Just a flip of the rectifier.

For parts with heavy oxide or hardened steel that resists reverse etch, an external acid etch (20-50% HCl or 10-30% H2SO4) can be used before the chrome bath.

Hero visual: a chrome plating tank showing the reverse etch process -- part connected as anode, with arrows showing material dissolving from the surface, then a transition showing polarity reversal to cathodic plating.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Reverse etch hero (Block B):** Chrome bath with part as anode, material dissolution arrows, rectifier showing + on workpiece. Then a transition arrow showing polarity flip.
2. **Reverse etch parameters (Block D):** Current density, time, what the etch accomplishes.
3. **External acid etch alternative (Block E):** When and why the external method is used.
4. **Failure mode cards (Block F):** 4 activation problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- REVERSE ETCH HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- REVERSE ETCH PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- EXTERNAL ACID ETCH ALTERNATIVE (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hard Chrome -- Reverse Etch -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Make the part the anode. Dissolve the oxide. Roughen the surface. Then flip the switch and plate.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

**Safety banner (right side):**
- Rounded rect, X: 17.0", Y: 1.4", W: 6.5", H: 1.0", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `Cr(VI) CARCINOGEN` -- Barlow SemiBold, 14 pt, `#E05C5C`
- Sub: `OSHA PEL 5 ug/m3 | Full PPE required` -- JetBrains Mono 10 pt `#E05C5C` at 80%

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean steel with surface oxide  -->  After: Oxide-free, roughened surface ready for chrome deposition`

---

### ZONE 3 -- Reverse Etch Hero

**Section label:** `REVERSE ETCH -- ACTIVATION IN THE CHROME BATH` -- Y: 4.4".

**BLOCK B -- Two-Phase Diagram (Y: 5.0" to 14.0")**

Two side-by-side panels representing the same tank in two states:

**Left -- Phase 1: Reverse Etch (Anodic):**
- Rounded rect, X: 0.5", Y: 5.5", W: 11.0", H: 7.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Tank interior: fill `#252B3D` (chrome bath)
- Part (center): rect labeled `WORKPIECE (+) ANODE` in `#E8A020`
- Anodes (sides): rects labeled `LEAD ANODES (-) CATHODE` in `#C8D0D8`
- Arrows from workpiece outward: `Metal dissolving from surface` -- `#E8A020` dashed
- Rectifier above: `(+)` on workpiece wire, `(-)` on anode wire

Overlay text:
- `PHASE 1: REVERSE ETCH` -- Barlow Condensed ExtraBold, 24 pt, `#E8A020`
- `Part is ANODE` JetBrains Mono 16 pt `#E8A020`
- `100--200 ASF (anodic)` JetBrains Mono 14 pt
- `30 sec to 3 min` JetBrains Mono 14 pt
- `Oxide dissolves, surface roughens` Inter Medium 13 pt

**Right -- Phase 2: Polarity Reversal (Begin Plating):**
- Rounded rect, X: 12.5", Y: 5.5", W: 11.0", H: 7.5", fill `#1E2435`, top accent 4 pt `#27AE60`
- Same tank interior
- Part: rect labeled `WORKPIECE (-) CATHODE` in `#27AE60`
- Anodes: labeled `LEAD ANODES (+) ANODE` in `#C8D0D8`
- Arrows from bath toward workpiece: `Chrome depositing on surface` -- `#27AE60` dashed
- Rectifier: `(-)` on workpiece, `(+)` on anodes

Overlay text:
- `PHASE 2: PLATE` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
- `Part is CATHODE` JetBrains Mono 16 pt `#27AE60`
- `100--400 ASF (cathodic)` JetBrains Mono 14 pt
- `Polarity reversed -- plating begins` Inter Medium 13 pt

**Transition arrow between panels:**
- Large right-pointing arrow, stroke 4 pt `#F0EDE8`
- Label: `FLIP POLARITY` -- Barlow Condensed ExtraBold, 18 pt, `#F0EDE8`
- Sub: `No delay -- same tank, same solution` -- Inter Medium, 12 pt, `#E8A020`

---

### ZONE 4 -- Reverse Etch Parameters

**Section label:** `REVERSE ETCH PARAMETERS` -- Y: 14.7".

**BLOCK D -- Parameter Panel (Y: 15.3" to 20.3")**

| Parameter | Value | Notes |
|---|---|---|
| Bath | Chrome plating bath (CrO3 + sulfate) | Same bath used for plating |
| Workpiece polarity | ANODIC (+) | Part is the anode |
| Current density | 100--200 ASF (anodic) | Higher CD = more aggressive etch |
| Time | 30 sec to 3 min | Depends on substrate and oxide condition |
| Temperature | Bath operating temp (120--140 F) | Part heats during etch -- reduces thermal shock |
| What it does | Dissolves surface oxide and thin metal layer | Creates micro-rough surface for chrome adhesion |
| Iron buildup | Dissolved iron enters chrome bath | Monitor; >8--10 g/L causes rough deposits |
| Transition | Reverse polarity immediately to begin plating | No delay -- same bath, no transfer |

Data: JetBrains Mono 14 pt. Notes: Inter Regular 13 pt `#F0EDE8` at 70%.

**Key insight callout:**
- `The reverse etch serves THREE purposes: (1) removes oxide, (2) roughens surface for adhesion, (3) pre-heats the part to reduce thermal shock when plating begins. Genius in its simplicity.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 5 -- External Acid Etch Alternative

**Section label:** `ALTERNATIVE: EXTERNAL ACID ETCH` -- Y: 20.7".

**BLOCK E -- External Etch Panel (Y: 21.3" to 26.3")**

Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`, left accent `#3A4055`.

Title: `WHEN REVERSE ETCH IS NOT ENOUGH` -- Barlow SemiBold, 18 pt, `#C8D0D8`

| Parameter | Value |
|---|---|
| Solution | 20--50% v/v HCl or 10--30% v/v H2SO4 |
| Temperature | Ambient to 120 F |
| Time | 1--5 min |
| Use case | Heavy oxide, hardened steel, case-hardened surfaces |
| Rinse after | Single rinse before chrome bath |
| Caution | H-embrittlement risk on high-strength steel (>= 40 HRC) |

**When to use external acid etch:**
- `Reverse etch alone leaves visible oxide after 3 min at 200 ASF`
- `Hardened tool steel or case-hardened surfaces`
- `Parts with heavy scale from heat treatment`
- `Parts that have been stored with significant corrosion`

Bottom note:
- `Most hard chrome shops use reverse etch 95%+ of the time. External acid etch is the exception, not the rule.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 4 ACTIVATION FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | CHROME PEELING | `#E05C5C` | Reverse etch too short; oxide not fully removed | Extend etch time; increase anodic CD |
| R1C2 | OVER-ETCHED SURFACE | `#E8A020` | Etch too long or CD too high; excessive metal removal | Reduce time; validate with test panels |
| R2C1 | HIGH IRON IN BATH | `#E05C5C` | Excessive reverse etch dissolves steel into bath | Shorten etch; dummy plate to remove iron; dilute |
| R2C2 | POOR ADHESION ON HARDENED STEEL | `#E8A020` | Reverse etch insufficient for hardened substrate | Use external acid etch first; extend reverse etch |

Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06".

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Hard Chrome`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; hard chrome process engineering practice. Hard chrome uses hexavalent chromium -- comply with all OSHA and EPA regulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Hard Chrome Activation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-phase hero diagram is the star of this poster. Showing the same tank in two states (anodic etch, then cathodic plate) communicates the elegance of the reverse etch process better than any text could. The polarity reversal arrow between the two panels should be bold and impossible to miss -- it is the "aha moment" for anyone new to hard chrome. The three-purpose callout in Zone 4 (oxide removal + surface roughening + pre-heating) is the kind of insight that makes a poster worth hanging on the wall. The iron buildup warning is a practical detail that experienced hard chrome platers will immediately appreciate -- it is the hidden cost of reverse etching that nobody talks about until the bath goes rough.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #90 -- Construction Workup v1.0*
*2026-04-26*
