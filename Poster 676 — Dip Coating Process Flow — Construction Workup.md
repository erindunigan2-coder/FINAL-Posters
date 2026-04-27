---
Project: Plating Posters Inc
Poster Number: 676
Title: "Dip Coating -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4: Dip Coating)"
Technical Source: Industry-standard dip coating processes covering plastisol, hot-dip thermoplastic, and solution dip. Complete 7-stage sequence from surface preparation through inspection.
Process Scope: Dip coating -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - ProcessFlow
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #676 -- Construction Workup
## Dip Coating -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for Dip Coating. The simplest coating concept imaginable: dip the part in, pull it out, drain the excess, cure. But simplicity hides subtlety -- withdrawal speed controls film thickness, drainage determines uniformity, and the three major dip families (plastisol, hot-dip thermoplastic, and solution dip) each have radically different film-forming mechanisms. This poster is the map for the other 8 posters (#677--#684).

Design philosophy: U-flow diagram of the 7-stage process as the hero, a three-family comparison table, a compact parameter summary, and a troubleshooting quick-hit strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Process flow diagram (Block B -- HERO):** Seven rounded rectangles in a U-flow: top row L-to-R (stages 1--4), vertical connector, bottom row R-to-L (stages 5--7). Each box is color-coded by stage type.
2. **Three-family comparison (Block D):** Plastisol vs. hot-dip thermoplastic vs. solution dip side-by-side.
3. **Parameter summary table (Block E):** 7-row table.
4. **Troubleshooting quick-hit strip (Block F):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--16.0" / ~13.1")
  Block B: Seven-stage U-flow diagram
  Block C: Stage legend strip
ZONE 3 -- THREE-FAMILY COMPARISON (16.0"--22.0" / ~6.0")
  Block D: Plastisol vs. hot-dip vs. solution dip
ZONE 4 -- PARAMETER SUMMARY TABLE (22.0"--28.5" / ~6.5")
  Block E: 7-row parameter table
ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0")
  Block F: 4-problem strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`
- Text: `DIP COATING`
- Position: X: 0.5", Y: 0.5"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Immersion Coating -- Complete Process Flow`
- Position: Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 22 pt, `#F0EDE8` at 65%
- Text: `Dip it in. Pull it out. Let gravity do the work. Three coating families -- plastisol, hot-dip, solution -- one elegantly simple process.`
- Position: Y: 2.2"

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE COMPLETE DIP COATING PROCESS -- STAGE BY STAGE` -- Centered, Y: 3.1". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Seven-Stage U-Flow Diagram**

Y: 3.8" to 14.8". Top row of four boxes, bottom row of three boxes.

Each flow box:
- Rounded rect, W: 5.4", H: 4.5"
- Fill: `#1E2435`
- Corner radius: 8 pt
- Top border accent: 4 pt colored strip

**Top Row (Y: 3.8" to 8.3") -- Stages 1-4, left to right:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Surface Prep | Box 1 | 0.5" | `#2EC4B6` (Teal) | Preparation |
| 2. Preheat (optional) | Box 2 | 6.25" | `#E8A020` (Amber) | Thermal |
| 3. Immerse / Dip | Box 3 | 12.0" | `#E8A020` (Amber) | Application |
| 4. Withdraw | Box 4 | 17.75" | `#E8A020` (Amber) | Application |

**Bottom Row (Y: 10.0" to 14.5") -- Stages 5-7, right to left:**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. Drain / Drip | Box 5 | 16.5" | `#2EC4B6` (Teal) | Leveling |
| 6. Cure | Box 6 | 9.0" | `#E8A020` (Amber) | Cure |
| 7. Inspect | Box 7 | 1.5" | `#C8D0D8` (Silver) | Inspection |

Arrows: 3 pt `#3A4055`, arrowheads.

**Inside each flow box:**

*Box 1 -- Surface Prep:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Surface Preparation`
- Parameters: `Clean + degrease` / `Blast (80--120 grit) for adhesion` / `Primer coat if required`
- Check: `Adhesion promoter for PVC-on-steel, PE-on-steel` (`#2EC4B6`)

*Box 2 -- Preheat:*
- Badge: `STAGE 2`, fill `#E8A020`
- Name: `Preheat` / Subtitle: `(Optional / Hot-Dip Only)`
- Parameters: `400--600 F (204--316 C)` / `Part mass determines soak time` / `Required for nylon, PE hot-dip`
- Check: `Not needed for plastisol or solution dip` (`#E8A020`)

*Box 3 -- Immerse / Dip:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Immerse / Dip`
- Parameters: `Plastisol: 2--30 sec` / `Hot-dip: 2--10 sec` / `Solution: 1--10 sec`
- Check: `Dip time + part temp control thickness` (`#E8A020`)

*Box 4 -- Withdraw:*
- Badge: `STAGE 4`, fill `#E8A020`
- Name: `Withdraw`
- Parameters: `Speed: 1--12 in/sec` / `Slower = thinner (solution dip)` / `Rapid for hot-dip`
- Check: `Withdrawal speed is primary thickness control for solution dip` (`#27AE60`)

*Box 5 -- Drain / Drip:*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Drain / Drip`
- Parameters: `10--60 sec drain time` / `Rotate/invert for uniform thickness` / `Air knives for wire/cable`
- Check: `Thick drip edges at bottom = too fast withdrawal or high viscosity` (`#E05C5C`)

*Box 6 -- Cure:*
- Badge: `STAGE 6`, fill `#E8A020`
- Name: `Cure`
- Parameters: `Plastisol: 350--400 F, 10--20 min` / `Hot-dip: cool to solidify` / `Solution: 300--400 F, 15--30 min`
- Check: `PVC plastisol: must reach fusion temp (350 F) -- below = weak film` (`#E8A020`)

*Box 7 -- Inspect:*
- Badge: `STAGE 7`, fill `#C8D0D8`
- Name: `Inspect`
- Parameters: `DFT: 5--40 mils (thick!)` / `Adhesion: peel/knife test` / `Flexibility: cold bend test`
- Check: `Shore A (soft coatings) or Shore D (hard thermoplastics)` (`#C8D0D8`)

**BLOCK C -- Stage Legend Strip**

Y: 15.0" to 15.8". Same pattern as Poster 668.

| Swatch Color | Label |
|---|---|
| `#2EC4B6` (Teal) | `Preparation & Drain` |
| `#E8A020` (Amber) | `Application & Cure` |
| `#C8D0D8` (Silver) | `Inspection` |
| `#E05C5C` (Coral) | `Caution / Problem` |

---

### ZONE 3 -- Three-Family Comparison

**Section label:** `THREE DIP COATING FAMILIES` -- Centered, Y: 16.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- Three Side-by-Side Callouts (Y: 16.8" to 21.8")**

**Left -- Plastisol (PVC) (X: 0.5", W: 7.33", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `PLASTISOL (PVC)` Barlow SemiBold 20 pt `#E8A020`

Content:
```
Mechanism: PVC particles fused in
  plasticizer at 350--400 F

DFT: 5--40 mils per dip
Preheat: Optional (200--300 F
  for thicker builds)
Cure: 350--400 F, 10--20 min
  (fusion, not cross-linking)

Applications:
  Tool handles, wire racks,
  dishwasher racks, hangers,
  fencing, grips
```

Bottom: `Over-fusion above 420 F releases toxic HCl gas.` Inter Medium 12 pt `#E05C5C`

**Center -- Hot-Dip Thermoplastic (X: 8.17", W: 7.33", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `HOT-DIP THERMOPLASTIC` Barlow SemiBold 20 pt `#2EC4B6`

Content:
```
Mechanism: Preheated part melts
  powder on contact; cools to solidify

DFT: 8--25+ mils per dip
Preheat: 400--600 F (required)
Cure: Cooling (no chemical reaction)

Materials: Nylon 11/12, polyethylene,
  polypropylene, PVC

Applications:
  Chemical resistance, abrasion
  protection, thick protective coatings
```

Bottom: `Part temperature at dip determines film build. Hotter = thicker.` Inter Medium 12 pt `#2EC4B6`

**Right -- Solution / Dispersion Dip (X: 15.83", W: 7.67", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `SOLUTION / DISPERSION DIP` Barlow SemiBold 20 pt `#27AE60`

Content:
```
Mechanism: Part immersed in liquid
  coating; film controlled by withdrawal
  speed, viscosity, and drainage

DFT: 0.5--3 mils per dip
Preheat: None
Cure: 300--400 F, 15--30 min
  (thermoset cross-linking)

Applications:
  Can linings (epoxy phenolic),
  precision thin coatings, multi-dip
  buildup for controlled thickness
```

Bottom: `Withdrawal speed is the primary control: slower = thinner film.` Inter Medium 12 pt `#27AE60`

---

### ZONE 4 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Centered, Y: 22.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK E -- 7-Row Parameter Table (Y: 22.8" to 28.3")**

Column widths (23.0" total):
- Stage (3.0") | Plastisol (6.5") | Hot-Dip (6.5") | Solution Dip (7.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Stage | Plastisol (PVC) | Hot-Dip Thermoplastic | Solution Dip |
|---|---|---|---|
| 1. Surface Prep | Degrease + primer | Blast + epoxy primer (nylon) | Degrease + phosphate |
| 2. Preheat | Optional: 200--300 F | Required: 400--600 F | None |
| 3. Immerse | 2--30 sec, ambient--120 F | 2--10 sec in fluidized bed | 1--10 sec in solution |
| 4. Withdraw | 2--12 in/sec | Rapid | 1--6 in/sec (controls DFT) |
| 5. Drain | 10--60 sec; rotate for uniformity | Brief; cool to solidify | 10--60 sec; angle for drainage |
| 6. Cure | 350--400 F, 10--20 min (fusion) | Cool to ambient | 300--400 F, 15--30 min |
| 7. Inspect | DFT 5--40 mils; Shore A | DFT 8--25 mils; Shore D | DFT 0.5--3 mils; adhesion |

Data: JetBrains Mono 11 pt `#F0EDE8`. Stage names: Inter Medium 13 pt.
Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON DIP COATING PROBLEMS` -- Centered, Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

Each card: Rounded rect W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DRIP MARKS / CURTAINING | Thick edge at bottom from fast withdrawal or high viscosity | Reduce withdrawal speed; lower viscosity; rotate parts during drain |
| 2 | 6.33" | BLISTERING | Trapped moisture or air in substrate | Pre-dry parts completely; pre-bake cast/porous substrates |
| 3 | 12.16" | PINHOLES / OUTGASSING | Gas escaping from substrate during cure | Pre-bake substrate at cure temp before dipping |
| 4 | 18.0" | BRIDGING | Coating spans holes/slots instead of following edges | Reduce viscosity; increase drain time; redesign fixture orientation |

---

### ZONE 6 -- Footer

Standard footer band (Y: 32.5" to 36.0").

**Disclaimer:** `This poster is an educational reference tool. Process parameters shown are typical industry values for dip coating systems. Specific formulations, concentrations, and process limits vary by coating supplier and application. Consult your coating supplier for application-specific guidance.`

**Poster title:** `Dip Coating -- Process Flow`
**Series name:** `Plating Posters Inc -- Metal Finishing Reference Series`
**Version:** `v1.0 -- 2026`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Dip Coating Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Dip coating is the most accessible coating process for a general audience -- everyone has dipped something in paint. The three-family comparison is the key educational element: plastisol, hot-dip, and solution dip look similar from the outside but have fundamentally different film-forming mechanisms. The thick DFT range (5--40+ mils) immediately distinguishes dip coating from spray and e-coat. This poster sets up the remaining 8 deep-dive posters in the cluster.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #676 -- Construction Workup v1.0*
*2026-04-26*
