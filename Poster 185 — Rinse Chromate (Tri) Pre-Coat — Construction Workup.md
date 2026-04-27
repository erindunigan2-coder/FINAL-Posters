---
Project: Plating Posters Inc
Poster Number: 185
Title: "Rinse -- Chromate (Tri) -- Pre-Coat"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-05 Section 5.3)"
Technical Source: Pre-deoxidize rinse for trivalent chromate conversion coating on aluminum. Double rinse standard. DI/RO water preferred for aerospace. Stage 2 of 7.
Process Scope: Pre-deoxidize rinse -- Stage 2 of trivalent chromate conversion on aluminum
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ConversionCoating
  - TrivalentChromate
  - Rinse
  - ConstructionWorkup
  - ClusterCC05
---

# Poster #185 -- Construction Workup
## Rinse -- Chromate (Tri) -- Pre-Coat

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 7. This is the rinse between alkaline cleaning and deoxidize/desmut. On aluminum lines, this rinse is critical -- alkaline carryover into the acid deoxidizer neutralizes the acid and reduces effectiveness. For aerospace processing, double rinse with DI/RO water is standard.

Hero visual: a two-stage counter-flow rinse system with conductivity monitoring and water quality targets.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse system hero (Block B):** Two rinse tanks in series showing counter-flow water direction, conductivity probes, and overflow. Built with rectangles and flow arrows.
2. **Water quality targets panel (Block D):** Conductivity, pH, and contaminant thresholds in a compact table.
3. **"Why Double Rinse?" callout (Block E):** Economics and quality rationale for counter-flow rinsing.
4. **Failure mode strip (Block F):** 4 rinse failures and their downstream consequences.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- WATER QUALITY + WHY DOUBLE RINSE (14.5"--20.5" / ~6.0")
ZONE 5 -- OPERATING PARAMETERS TABLE (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Trivalent Chromate on Aluminum -- Pre-Deoxidize -- Stage 2 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The rinse between clean and deox. Alkaline carryover neutralizes your acid. Double rinse is the standard.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned aluminum with alkaline residue  -->  After: Neutral, residue-free surface ready for deoxidize`

---

### ZONE 3 -- Rinse System Hero

**Section label:** `THE PRE-DEOXIDIZE RINSE` -- Y: 4.4".

**BLOCK B -- Two-Stage Counter-Flow Rinse**

Y: 5.0" to 14.0".

**Tank 1 (First Rinse -- Drag-Out):**
- Rounded rect, X: 1.5", Y: 5.5", W: 9.5", H: 7.0"
- Fill: `#252B3D` (rinse water)
- Border: 2 pt `#C8D0D8`
- Label above: `RINSE 1 (DRAG-OUT)` Barlow SemiBold 16 pt `#2EC4B6`

**Tank 2 (Final Rinse -- Clean):**
- Rounded rect, X: 13.0", Y: 5.5", W: 9.5", H: 7.0"
- Fill: `#252B3D` at lighter opacity (cleaner water)
- Border: 2 pt `#C8D0D8`
- Label above: `RINSE 2 (FINAL)` Barlow SemiBold 16 pt `#27AE60`

**Counter-flow arrow (from Tank 2 to Tank 1):**
- Large horizontal arrow, Y: 13.0", from X: 13.0" to X: 11.0"
- Stroke: 3 pt `#2EC4B6`, dashed
- Label: `Fresh water IN --> Overflow OUT` Inter Medium 12 pt `#2EC4B6`

**Conductivity probe symbols (inside each tank):**
- Tank 1: `Conductivity: < 1000 uS/cm` JetBrains Mono 13 pt `#E8A020`
- Tank 2: `Conductivity: < 500 uS/cm target` JetBrains Mono 13 pt `#27AE60`
- `< 200 uS/cm ideal (aerospace)` JetBrains Mono 12 pt `#27AE60`

**pH targets (inside tanks):**
- Tank 1: `pH dropping from > 9 to < 9` JetBrains Mono 12 pt `#F0EDE8`
- Tank 2: `pH: 6.5--8.0 (neutral)` JetBrains Mono 12 pt `#27AE60`

**Water source label (top right):**
- `DI or RO water preferred` Barlow SemiBold 14 pt `#27AE60`
- `Chloride and sulfate in tap water cause pitting on aluminum` Inter Regular 12 pt `#E05C5C`

**Part movement arrows:**
- Arrow from left edge to Tank 1: `From cleaner`
- Arrow from Tank 1 to Tank 2: `Part transfer`
- Arrow from Tank 2 to right edge: `To deoxidize`

**Bottom callout (Y: 13.5"):**
- `Counter-flow saves water: fresh water enters Tank 2, overflows into Tank 1, exits to drain from Tank 1.`
- Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Water Quality + Why Double Rinse

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Water Quality Targets (X: 0.5", W: 11.0"):**

Section label: `WATER QUALITY TARGETS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

Table (Y: 15.3" to 18.5"):

| Parameter | Target | Why It Matters |
|---|---|---|
| Conductivity | < 500 uS/cm (< 200 aerospace) | High conductivity = high dissolved solids = contamination |
| pH (after rinse) | < 9.0 (ideally 7--8) | High pH = alkaline carryover into deox |
| Chloride | < 25 ppm | Chloride causes pitting corrosion on aluminum |
| Sulfate | < 50 ppm | Sulfate residues interfere with chromate deposition |
| Temperature | Ambient to 80 F (27 C) | No heating needed; warm water wastes energy |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt `#F0EDE8`. Alternating rows.

**Right -- Why Double Rinse? (X: 12.0", W: 11.5"):**

Section label: `WHY DOUBLE RINSE?` Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Y: 14.7".

Callout box: Rounded rect, H: 4.8", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):

- `Single rinse: removes ~90% of drag-out`
- `Double rinse (counter-flow): removes ~99% of drag-out`
- `That extra 9% is the difference between a clean deox step and a neutralized one`
- `Aerospace standard: double rinse is NOT optional -- it is specified in most Nadcap-accredited process lines`

Bottom stat:
- `10x` Barlow Condensed ExtraBold 48 pt `#2EC4B6`
- `improvement in rinse efficiency with counter-flow vs. single immersion` Inter Medium 14 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Operating Parameters Table

**Section label:** `OPERATING PARAMETERS` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 20.7".

**Parameter table (Y: 21.3" to 26.3"):**

| Parameter | Standard | Aerospace | Notes |
|---|---|---|---|
| Rinse stages | 1 (minimum) | 2 (counter-flow) | Double rinse is best practice for all |
| Water type | City water acceptable | DI or RO required | Aerospace specs mandate low-TDS water |
| Temperature | Ambient | Ambient | No heating needed |
| Overflow rate | 1--3 gal/min | 2--5 gal/min | Higher flow = better rinse |
| Conductivity limit | < 1000 uS/cm | < 500 uS/cm (< 200 ideal) | Monitor continuously |
| pH after rinse | < 9.0 | < 8.0 | Indicator of alkaline carryover |
| Agitation | Mild air or part movement | Air agitation preferred | Improves rinse efficiency |

Data: JetBrains Mono 12 pt. Alternating rows.

---

### ZONE 6 -- Failure Modes

**Section label:** `WHAT GOES WRONG -- 4 RINSE FAILURES` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 26.7".

**4-card row (Y: 27.3" to 32.3"):**

| Card | X | Problem | Cause | Downstream Effect |
|---|---|---|---|---|
| 1 | 0.5" | ALKALINE CARRYOVER | Single rinse; low overflow; high drag-out | Neutralizes deox acid; incomplete desmut |
| 2 | 6.33" | CHLORIDE CONTAMINATION | Tap water in aerospace line | Pitting on aluminum; coating failure |
| 3 | 12.16" | HIGH CONDUCTIVITY | Stale rinse water; no overflow | Dissolved contaminants transfer to deox |
| 4 | 18.0" | WATER SPOTS | Hard water; poor drainage; no DI | Visible marks through thin tri chromate film |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Downstream: Inter Medium, 13 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Chromate (Trivalent) -- Pre-Deoxidize`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Chromate Tri Pre-Deox -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters risk being "boring" -- but rinse quality is the #1 predictor of downstream coating quality on aluminum. The counter-flow diagram and the 10x stat are the hooks. The water quality table gives the operator something concrete to monitor.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #185 -- Construction Workup v1.0*
*2026-04-26*
