---
Project: Plating Posters Inc
Poster Number: 692
Title: "Drain / Leveling -- Flow Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating, Section 5.7)"
Process Scope: Drain and leveling for flow coating -- Stage 6 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - DrainLeveling
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #692 -- Construction Workup
## Drain / Leveling -- Flow Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 7. After the flood, gravity takes over. Excess coating drains off and returns to the reservoir. How you hang the part, how long you drain, and how you manage that flash period determines whether you get a uniform film or a mess of runs and sags. This is the stage where flow coating's biggest weakness shows -- thickness variation. +/- 30-50% is the reality. Part orientation is the primary lever you have.

Hero visual: part orientation diagram showing how hanging angle affects drainage pattern and film thickness distribution (thick at bottom, thin at top).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Part orientation / drainage hero (Block B):** Three versions of the same part hung at different angles, with film thickness gradient indicated by color intensity. Simple geometry with overlaid color zones.
2. **Drain parameters table (Block D):** Drain time, flash time, temperature, and their effects on film.
3. **Thickness variation reality panel (Block E):** What +/- 30-50% actually means on a real part.
4. **Defect strip (Block F):** 4 common drain/leveling failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber)
ZONE 3 -- PART ORIENTATION / DRAINAGE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAIN PARAMETERS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- THICKNESS VARIATION REALITY (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON DRAIN/LEVELING FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DRAIN / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flow Coating -- Stage 6 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Gravity is your leveling tool. How you hang the part determines where the coating ends up -- thick at the bottom, thin at the top, holidays in the shadows.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet-flooded part with excess coating  -->  After: Drained part with leveled wet film ready for cure`

---

### ZONE 3 -- Part Orientation / Drainage Hero

**Section label:** `PART ORIENTATION CONTROLS FILM DISTRIBUTION` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Three Orientation Panels**

Y: 5.0" to 14.0". Three panels side by side showing the same rectangular part (with a flange and a pocket) at three different hanging angles.

**Panel 1 -- Vertical Hang (X: 0.5", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `VERTICAL (0 deg tilt)` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- Badge: `POOR` -- fill `#E05C5C`, text `#F0EDE8`
- Part diagram: Rectangle hung vertically, with graduated color fill:
  - Top 1/3: `#E8A020` at 10% (very thin film)
  - Middle 1/3: `#E8A020` at 25% (target thickness)
  - Bottom 1/3: `#E8A020` at 50% (heavy buildup)
  - Bottom edge: thick drip line `#E8A020` at 70%
- Labels: `Thin` at top, `Target` at middle, `Heavy + drip edge` at bottom
- DFT callout: `Top: 0.3 mil / Bottom: 2.5 mils` -- JetBrains Mono, 12 pt, `#E05C5C`
- Note: `Maximum variation. Drip edge at bottom.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**Panel 2 -- Angled Hang (X: 8.16", W: 7.33", H: 8.5"):**
- Top accent 4 pt `#27AE60`
- Title: `ANGLED (15-30 deg tilt)` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- Badge: `BEST` -- fill `#27AE60`, text `#1A1F2E`
- Part diagram: Same rectangle tilted, more uniform color distribution:
  - Upper area: `#E8A020` at 20%
  - Lower area: `#E8A020` at 35%
  - Corner drainage paths indicated with small arrows
- DFT callout: `High: 1.8 mils / Low: 0.8 mils` -- JetBrains Mono, 12 pt, `#27AE60`
- Note: `Balanced drainage. Minimal drip edge. Orient pocket to drain.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**Panel 3 -- Rotated During Drain (X: 15.83", W: 7.33", H: 8.5"):**
- Top accent 4 pt `#2EC4B6`
- Title: `ROTATED (tumble drain)` -- Barlow SemiBold, 16 pt, `#F0EDE8`
- Badge: `SPECIALTY` -- fill `#2EC4B6`, text `#1A1F2E`
- Part diagram: Small parts on a rotating fixture, with even color distribution `#E8A020` at 25%
- DFT callout: `Uniform: +/- 15-20%` -- JetBrains Mono, 12 pt, `#2EC4B6`
- Note: `Best uniformity. Only practical for small parts that can be fixtured for rotation.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Drain Parameters Table

**Section label:** `DRAIN AND FLASH PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Parameters Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Parameter (4.5") | Range (4.0") | Effect of Increase (5.0") | Effect of Decrease (5.0") | Control Method (4.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.9".

| Parameter | Range | Increase Effect | Decrease Effect | Control |
|---|---|---|---|---|
| Drain time | 30-120 sec | Thinner film, more uniform | Thicker film, more runs | Timer / conveyor speed |
| Flash time (pre-oven) | 5-15 min ambient | Smoother surface, less solvent pop | Faster throughput, risk of solvent entrapment | Ambient temp + conveyor |
| Flash tunnel temp | 120-160 F | Faster solvent release, less sag risk | Longer drain, more leveling | Heated tunnel thermostat |
| Coating viscosity | 15-40 sec Zahn #2 | Less drainage, thicker film, more runs | More drainage, thinner film | Solvent addition per TDS |
| Part tilt angle | 15-30 deg | More drainage from one area | Less directional drainage | Fixture design |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

---

### ZONE 5 -- Thickness Variation Reality

**Section label:** `WHAT +/- 30-50% VARIATION REALLY MEANS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Real-World Example Panel**

Y: 21.3" to 26.3".

**Large callout box (X: 0.5", W: 23.0", H: 4.8"):**
- Fill `#1E2435`, left accent 0.06" `#E8A020`

**Left section (X: 1.0", W: 10.5"):**
- Title: `EXAMPLE: 2.0 mil TARGET DFT` -- Barlow SemiBold, 18 pt, `#E8A020`

Horizontal bar gauge showing DFT distribution:
- Red zone left: `< 1.0 mil` fill `#E05C5C` at 30%
- Yellow zone: `1.0-1.4 mils` fill `#E8A020` at 25%
- Green zone: `1.4-2.6 mils` fill `#27AE60` at 40%
- Yellow zone: `2.6-3.0 mils` fill `#E8A020` at 25%
- Red zone right: `> 3.0 mils (runs/sags)` fill `#E05C5C` at 30%

Labels below bar:
- `Thin spots (holidays)` under left red
- `Spec range` under green
- `Heavy (runs)` under right red

**Right section (X: 12.5", W: 10.5"):**
- Title: `SPECIFICATION STRATEGY` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Specify MINIMUM DFT, not target`
- `Measure at top, middle, and bottom of each part`
- `Accept that bottom edges will be thicker`
- `If tight tolerance is required: flow coat is the wrong method -- switch to spray`
- `ASTM D7091 gauge: 3+ readings per zone, 3 zones per part`

Bottom strip:
- Rounded rect, fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Flow coating trades precision for efficiency. You get 90-95% material utilization but +/- 30-50% thickness variation. For industrial primers, that trade-off is almost always worth it.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 6 -- Common Drain/Leveling Failures

**Section label:** `WHAT GOES WRONG -- 4 DRAIN / LEVELING FAILURES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CURTAINING / SAGS | Viscosity too low, drain time too short, or poor part angle | Increase viscosity; extend drain; tilt part for drainage |
| 2 | 6.33" | DRIP EDGE BUILDUP | Gravity pooling at lowest point | Rotate part during drain; design fixtures with drain points |
| 3 | 12.16" | HOLIDAYS ON UPWARD FACES | Horizontal surfaces facing up shed coating during drain | Tilt to eliminate horizontal surfaces; touch-up spray |
| 4 | 18.0" | SOLVENT POP IN OVEN | Insufficient flash time -- solvent trapped under skinned surface | Extend flash time; reduce flash tunnel temperature; reduce film build |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `The best fixture designer in a flow coat shop is worth their weight in gold. Part orientation is the single most effective control for film distribution, and it is entirely determined by how the fixture holds the part. Invest in fixture design before blaming the coating.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Drain / Leveling -- Flow Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Drain Leveling Flow Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster confronts flow coating's honest limitation: you cannot precisely control where the coating ends up. The three-orientation hero makes the point visually -- same part, different angle, dramatically different film distribution. The thickness variation panel is the reality check: +/- 30-50% means your 2 mil target could be anywhere from 1 to 3 mils. For industrial primers, that is acceptable. For appearance-critical work, it is not. Know your method's limits.

---

*Alaina -- Poster #692 -- Construction Workup v1.0 -- 2026-04-26*
