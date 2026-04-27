---
Project: Plating Posters Inc
Poster Number: 374
Title: "Descaling Stage -- Mechanical & Chemical Treatment"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Industry-standard mechanical and chemical descaling treatment stages. SSPC surface preparation grades. Combined blast + pickle approach.
Process Scope: The main descaling treatment step -- mechanical blasting, alkaline permanganate conditioning, molten salt descaling, and their common failure modes
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - TreatmentStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #374 -- Construction Workup
## Descaling Stage -- Mechanical & Chemical Treatment

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the "main event" poster for the descaling cluster -- where scale actually gets removed. It covers the three primary descaling methods in detail (blast cleaning, alkaline permanganate conditioning, molten salt), the combined blast-then-pickle sequence that handles 80% of real-world jobs, and a 6-defect diagnosis grid for what goes wrong.

Hero visual: a blast nozzle cross-section showing media impinging on scaled steel, with the scale layer breaking away. Simple geometric construction.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Three-method comparison panel (Block B -- HERO):** Three tall callout boxes side-by-side -- Mechanical Blast, Alkaline Permanganate, Molten Salt. Each with operating parameters, mechanism description, and best-for note.

2. **Combined sequence callout (Block C):** The standard blast --> clean --> pickle --> activate flow, emphasizing the 4-hour window.

3. **Defect diagnosis grid (Block D):** 3x2 grid of common descaling failures.

4. **Surface profile hero callout (Block E):** Anchor profile measurement guidance.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 21.5" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- THREE-METHOD COMPARISON / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Blast | Permanganate | Molten Salt -- three columns

ZONE 3 -- COMBINED SEQUENCE + 4-HOUR RULE (15.5"--21.5" / ~6.0" tall)
  Block C: Blast-then-pickle flow + timing callout

ZONE 4 -- DEFECT DIAGNOSIS GRID (21.5"--28.0" / ~6.5" tall)
  Block D: 3x2 defect grid (5 common failures)
  Block E: Surface profile measurement callout

ZONE 5 -- PROCESS FLOW STANDARDS (28.0"--32.5" / ~4.5" tall)
  Block F: SSPC grade reminders in horizontal strip

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DESCALING STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Mechanical & Chemical Treatment -- Where Scale Gets Removed` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Three methods, one goal: expose clean metal for the next step. Blast it, condition it, or melt it off -- but get it all.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Three-Method Comparison (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> THREE DESCALING METHODS -- SIDE BY SIDE

---

**BLOCK B -- Three Columns**

Y: 3.8" to 15.0". Three side-by-side callout boxes.

| Column | X | W | Accent | Title | Title Color |
|---|---|---|---|---|---|
| Mechanical Blast | 0.5" | 7.33" | `#2EC4B6` | MECHANICAL BLAST | `#2EC4B6` |
| Alkaline Permanganate | 8.17" | 7.33" | `#E8A020` | ALKALINE PERMANGANATE | `#E8A020` |
| Molten Salt | 15.83" | 7.67" | `#E05C5C` | MOLTEN SALT | `#E05C5C` |

Each box: Rounded rect, H: 11.0", fill `#1E2435`, radius 8, left accent 0.06".

---

*Column 1 -- Mechanical Blast:*

Title: Barlow SemiBold, 20 pt, `#2EC4B6`.
Subtitle: `The Workhorse` -- Barlow Condensed ExtraBold, 14 pt, `#F0EDE8` at 50%.

Parameters (JetBrains Mono 13 pt, `#2EC4B6`):
```
Pressure: 40--100 psi
Distance: 6--12 in
Angle: 60--90 deg
Coverage: 100--200%
Media: steel shot, grit, garnet, Al2O3, glass bead
```

Mechanism (Inter Regular 13 pt `#F0EDE8`):
`High-velocity media impacts scale, fracturing and removing it. No chemical reaction -- purely mechanical energy transfer.`

Best for (Inter Medium 13 pt `#27AE60`):
`Heavy forge scale, casting scale, mill scale on carbon steel. Line-of-sight surfaces.`

Limitation (Inter Regular 12 pt `#E05C5C`):
`Cannot reach recesses, blind holes, or internal passages. Follow with acid pickle for complete cleaning.`

---

*Column 2 -- Alkaline Permanganate:*

Title: Barlow SemiBold, 20 pt, `#E8A020`.
Subtitle: `The Conditioner` -- 14 pt `#F0EDE8` at 50%.

Parameters:
```
NaOH: 50--100 g/L
KMnO4: 30--50 g/L
Temp: 80--95 C (175--205 F)
Time: 15--60 min
```

Mechanism:
`KMnO4 oxidizes tight Cr-containing oxides (on stainless and alloy steels) to soluble chromates. Does NOT remove scale directly -- conditions it for subsequent acid pickle.`

Best for:
`Alloy steel with Cr-bearing oxides. Stainless steel conditioning. Complex geometry where blast cannot reach.`

Limitation:
`Slow. Requires acid pickle follow-up. Permanganate stains everything it touches.`

---

*Column 3 -- Molten Salt:*

Title: Barlow SemiBold, 20 pt, `#E05C5C`.
Subtitle: `The Nuclear Option` -- 14 pt `#F0EDE8` at 50%.

Parameters:
```
Salt: NaOH + NaH or NaNO3
Temp: 400--500 C (750--930 F)
Time: 5--20 min
Follow-up: water quench + acid pickle
```

Mechanism:
`Molten caustic chemically reduces and dissolves oxide at extreme temperature. NaH reduces refractory oxides that resist all other methods.`

Best for:
`The worst scale conditions: heavy heat-treat scale on alloy steel, refractory oxides, titanium descaling.`

Limitation:
`Extremely hazardous (extreme temperature, steam explosion risk). Requires specialized equipment. Not for thin or delicate parts.`

DANGER badge (bottom of column): Rounded rect, fill `#E05C5C` at 20%, border 1 pt `#E05C5C`.
Text: `DANGER: 400--500 C` Barlow SemiBold 14 pt `#E05C5C`.

---

### ZONE 3 -- Combined Sequence + 4-Hour Rule

**Section label:** Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> THE STANDARD COMBO -- BLAST + PICKLE

---

**BLOCK C -- Flow + Timing**

Y: 16.4" to 19.5".

Six small boxes in a horizontal flow (same pattern as Poster #371 Block C but more compact):

`Blast (SP-10 min)` --> `Alk Clean` --> `Rinse` --> `Acid Pickle` --> `Rinse` --> `Activate + Plate`

Below flow, full-width callout:
- Rounded rect, X: 0.5", Y: 19.8", W: 23.0", H: 1.5", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`, radius 4
- Text: `THE 4-HOUR RULE: Steel begins oxidizing immediately after blast cleaning. Process within 4 hours. In humid environments (>60% RH), process faster. If delay is unavoidable, apply temporary rust preventive.` -- Inter Medium, 14 pt, `#E05C5C`

---

### ZONE 4 -- Defect Diagnosis Grid + Profile

**Section label:** Centered. Y: 21.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> WHAT GOES WRONG -- 5 COMMON FAILURES

---

**BLOCK D -- Defect Grid (3x2, 5 cells used)**

Y: 22.3" to 26.3". Same construction as Poster #36.

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | EMBEDDED MEDIA | `#E05C5C` | Wrong media on soft substrate; excessive pressure | Softer media; reduce pressure; increase distance |
| R1C2 | RESIDUAL SCALE IN RECESSES | `#E8A020` | Blast is line-of-sight; cannot reach pits/holes | Follow with acid pickle; vibratory finish for complex geometry |
| R1C3 | PROFILE TOO DEEP | `#E8A020` | Over-blast with aggressive angular grit | Reduce pressure; increase distance; switch to finer grit or shot |
| R2C1 | PROFILE TOO SHALLOW | `#2EC4B6` | Under-blast; media worn round | Replace media; increase pressure or dwell time |
| R2C2 | FLASH RUST | `#E05C5C` | Humidity > 60% RH; delay > 4 hours | Blast with dry air; process immediately; apply flash-rust inhibitor |

Each card: Rounded rect W: 7.33", H: 1.8", fill `#1E2435`, left accent 0.06" in defect color.

---

**BLOCK E -- Surface Profile Callout**

Y: 26.6" to 27.8". Full-width callout.

Rounded rect, X: 0.5", W: 23.0", H: 1.2", fill `#1E2435`, left accent 0.06" `#27AE60`.
Title: `ANCHOR PROFILE TARGET` -- Barlow SemiBold, 16 pt, `#27AE60`.
Text: `For plating adhesion: 25--75 micrometers (1--3 mils). Measure with replica tape (ASTM D4417-C) or digital profilometer (ASTM D4417-B). Report as Rz (peak-to-valley) or Ra (arithmetic average).` -- Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 5 -- SSPC Grade Reminders

**Section label:** Centered. Y: 28.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> SURFACE PREP GRADES -- QUICK REFERENCE

Four horizontal strip cards (same as Poster #371 Zone 4 but compact horizontal format):

Y: 28.9" to 32.3".

| Card | Grade | Standard | Requirement |
|---|---|---|---|
| 1 | SP-5 | White Metal | 100% free of all visible residues |
| 2 | SP-10 | Near-White | 95% free of visible residues |
| 3 | SP-6 | Commercial | 67% free of visible residues |
| 4 | SP-7 | Brush-Off | Loose scale removed; tight scale may remain |

Each: Rounded rect, W: 5.5", H: 1.5", fill `#1E2435`, top accent 3 pt in grade color.
- SP-5: `#27AE60` | SP-10: `#2EC4B6` | SP-6: `#E8A020` | SP-7: `#3A4055`

Grade: JetBrains Mono 14 pt, accent color. Requirement: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Descaling Stage -- Mechanical & Chemical Treatment`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Descaling Stage -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-column hero comparison is the core decision-support visual. A shop supervisor looking at this poster can immediately see: "We have medium mill scale on carbon steel -- mechanical blast is our method. We have Cr-bearing scale on alloy steel -- permanganate conditioning then pickle." The 4-hour rule callout in coral is one of the most practically important pieces of information on any poster in this cluster -- steel will flash-rust faster than most people expect, especially in the South.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #374 -- Construction Workup v1.0*
*2026-04-26*
