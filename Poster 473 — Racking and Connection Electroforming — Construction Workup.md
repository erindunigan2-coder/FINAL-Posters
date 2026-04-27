---
Project: Plating Posters Inc
Poster Number: 473
Title: "Racking & Connection -- Electroforming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 8: Electroforming, Sections 8.5-8.6)"
Technical Source: Electroforming racking and electrical connection -- mounting the mandrel in the plating tank, cathode connection, anode arrangement (conforming anodes, Ti baskets with Ni or Cu fills), and the critical role of current distribution in electroforming. Unlike decorative plating, electroforming requires thick, uniform deposits -- so current distribution management is not optional, it is the defining engineering challenge.
Process Scope: Electroforming racking, cathode connection, and anode setup (Stage 5 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electroforming
  - Racking
  - CurrentDistribution
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #473 -- Construction Workup
## Racking & Connection -- Electroforming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 10. The mandrel is clean, activated, and ready for the tank. Now it must be mounted securely, connected electrically, and positioned relative to the anodes for uniform current distribution. In electroforming, thickness uniformity is everything -- a waveguide wall that is 2 mm on one side and 0.5 mm on the other is scrap. Conforming anodes, auxiliary cathodes (thieves), and shields are the tools that make uniformity possible.

Hero visual: tank cross-section showing mandrel, conforming anodes, shields, thieves, and current distribution lines.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Tank cross-section diagram (Block B -- HERO):** Mandrel centered in tank with conforming anodes, shields, and thieves annotated.
2. **Current distribution concept (Block C):** Why edges get more deposit and how to fix it.
3. **Anode setup table (Block D):** Anode types and materials for Ni and Cu EF.
4. **Electrical connection details (Block E):** Cathode bar, contact points, bus bar sizing.
5. **Pre-immersion checklist (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Racking stage highlighted (Teal)
ZONE 3 -- TANK CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CURRENT DISTRIBUTION + ANODE SETUP (14.5"--22.0" / ~7.5")
ZONE 5 -- ELECTRICAL CONNECTIONS + CHECKLIST (22.0"--28.5" / ~6.5")
ZONE 6 -- COMMON RACKING PROBLEMS (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RACKING & CONNECTION` -- 76 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroforming -- Mandrel Mounting, Anode Setup, and Current Distribution` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The mandrel is the cathode. The anodes must follow its contour. The current must reach every surface uniformly. Rack it wrong and you build scrap for three days.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Racking stage highlighted (Teal). Others dimmed.
Below: `Before: Clean, activated mandrel with release agent/conductive coating (Stage 4) --> After: Mandrel mounted in tank, connected as cathode, anodes positioned, ready for strike`

---

### ZONE 3 -- Tank Cross-Section Hero

**Section label:** `TANK SETUP -- MANDREL, ANODES, AND CURRENT DISTRIBUTION` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Cross-Section Diagram (Y: 5.0" to 14.0")**

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Tank outline:** Large rectangle, X: 2.0", Y: 6.0", W: 19.0", H: 6.5", fill `#252B3D`, border 2 pt `#3A4055`.
- Label above: `ELECTROFORMING TANK (PP or PVC lined)` Barlow SemiBold 14 pt `#F0EDE8` at 60%

**Solution fill:** Rectangle inside tank, fill `#2EC4B6` at 10%.
- Label: `Ni SULFAMATE SOLUTION` JetBrains Mono 12 pt `#2EC4B6` at 60%

**Mandrel (center):** Irregular shape representing a mandrel, fill `#3A4055`, border 2 pt `#E8A020`.
- Label: `MANDREL (CATHODE)` Barlow SemiBold 16 pt `#E8A020`
- Cathode lead wire going up to cathode bar

**Conforming anodes (flanking mandrel):**
Two curved shapes following mandrel contour, fill `#27AE60` at 30%, border 2 pt `#27AE60`.
- Label: `CONFORMING ANODES` Barlow SemiBold 14 pt `#27AE60`
- Detail: `Shaped to follow mandrel profile. Maintain uniform anode-to-cathode distance.`

**Ti basket anode (one side):**
- Rectangle, fill `#27AE60` at 20%, border 1 pt `#27AE60`
- Label: `Ti BASKET with Ni ROUNDS` JetBrains Mono 11 pt `#27AE60`
- Detail: `Anode bag (PP) over basket to contain particles`

**Shields (two, placed at mandrel edges):**
- Vertical rectangles, fill `#E05C5C` at 30%
- Label: `SHIELDS` Barlow SemiBold 12 pt `#E05C5C`
- Detail: `Block excess current at edges/corners`

**Thieves / Auxiliary cathodes (at tank edges):**
- Small rectangles, fill `#E8A020` at 30%
- Label: `THIEVES (AUX. CATHODES)` Barlow SemiBold 12 pt `#E8A020`
- Detail: `Draw current away from high-CD areas. Sacrificial -- deposit on thief is discarded.`

**Current distribution lines:**
- Curved arrows from anodes to mandrel, 1 pt `#C8D0D8` at 40%
- Denser at edges (showing current concentration problem)
- Annotation: `Current concentrates at edges and protrusions -- shields and thieves redistribute it`

**Cathode bar at top:**
- Horizontal rectangle, fill `#E8A020`
- Label: `CATHODE BAR` JetBrains Mono 12 pt `#1A1F2E`

**Bottom insight (Y: 13.2" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#2EC4B6`
- `Conforming anodes are the single most important tool for thickness uniformity. The anode must follow the mandrel contour so that the anode-to-cathode distance is constant across the entire surface.` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 4 -- Current Distribution + Anode Setup

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Current Distribution (X: 0.5", W: 11.0")**

**Section label:** `CURRENT DISTRIBUTION -- THE CORE CHALLENGE` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Distribution Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
PROBLEM:
Current follows the path of least resistance.
Edges, corners, and protrusions on the mandrel
are closest to the anodes = highest current
density = thickest deposit.

Recesses, flat areas far from anodes =
lowest current density = thinnest deposit.

FOR ELECTROFORMING THIS IS CATASTROPHIC:
A 5 mm target wall thickness can vary from
8 mm at edges to 2 mm in recesses without
proper current distribution management.

SOLUTIONS:

1. CONFORMING ANODES
   Shape anodes to follow mandrel contour.
   Constant A-C distance = uniform current.

2. SHIELDS (non-conductive)
   Block current at high-CD areas.
   Placed between anode and mandrel edge.

3. AUXILIARY CATHODES (THIEVES)
   Conductive elements placed at high-CD
   areas. Draw current away from mandrel
   edges. Connected to cathode bar.

4. ANODE-TO-CATHODE DISTANCE
   General rule: 100-200 mm.
   Closer = higher CD but less uniform.
   Farther = lower CD but more uniform.
```

**Right -- Anode Setup (X: 12.0", W: 11.5")**

**Section label:** `ANODE TYPES AND MATERIALS` -- Y: 14.7".

**BLOCK D -- Anode Table (Y: 15.3" to 21.5"):**

| Anode Type | Material | Application | Notes |
|---|---|---|---|
| S-depolarized Ni rounds | Electrolytic Ni, S-activated | Ni sulfamate EF | Standard; maintains bath chemistry; 99.5%+ purity |
| Ni crowns / bars | Cast or rolled Ni | Ni Watts EF | Less common; may need anode bags |
| OFHC copper | Oxygen-free high-conductivity Cu | Acid Cu EF | Phosphorized Cu for long-term bath stability |
| Ti baskets | Titanium mesh baskets | All EF baths | Fill with Ni rounds or Cu chips; anode bags required |
| Insoluble (Pt/Ti or MMO) | Platinum-clad Ti or mixed metal oxide | Special applications | Bath chemistry must be replenished by metal salt addition |

Header: Barlow SemiBold 11 pt, fill `#3A4055`. Data: Inter Regular 11 pt `#F0EDE8`.

Below table:
- `ANODE-TO-CATHODE RATIO: 1:1 to 2:1 surface area. Higher ratio = more uniform dissolution and better current distribution. Always use anode bags to contain particulate.` Inter Medium 12 pt `#E8A020`

---

### ZONE 5 -- Electrical Connections + Checklist

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- Electrical Connection Details (X: 0.5", W: 11.0")**

**Section label:** `ELECTRICAL CONNECTIONS` -- Y: 22.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK E -- Connection Panel (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
CATHODE CONNECTION (mandrel):
- Copper or titanium lead wire
- Soldered, bolted, or clamped to mandrel
  at a non-critical area (contact mark
  will not be coated properly)
- Multiple contact points for large mandrels
  to avoid voltage drop
- Wire gauge: sized for full operating current
  without excessive heating (< 5 V drop)

CATHODE BAR:
- Copper bus bar across tank top
- Clean contact surfaces (no oxide)
- Bolt mandrel hangers to bar securely

ANODE CONNECTION:
- Separate anode bus bar (copper)
- Anodes hung from anode bar by
  titanium hooks
- Each anode independently connected
  for balance adjustment

RECTIFIER:
- DC, < 5% ripple at full load
- Current range: sized for max A/dm2 x
  total cathode area + 20% headroom
- Pulse capability optional (improves
  deposit quality for thick builds)
```

**Right -- Pre-Immersion Checklist (X: 12.0", W: 11.5")**

**Section label:** `PRE-IMMERSION CHECKLIST` -- Y: 22.2".

**BLOCK F -- Checklist (Y: 22.8" to 28.0"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

```
[ ] Mandrel clean and activated (per Stage 4)
[ ] Release agent fresh (permanent mandrels)
[ ] Conductive coating intact (non-conductive
    mandrels -- check continuity)
[ ] Cathode lead wire connected securely
[ ] Conforming anodes positioned at correct
    distance from mandrel (100-200 mm)
[ ] Shields in place at high-CD areas
[ ] Thieves in place and connected to cathode
[ ] Anode bags installed on all anodes
[ ] Anode fill level sufficient for full run
[ ] Bath chemistry verified (pH, Ni conc,
    temperature, stress reducer level)
[ ] Filtration running (1-5 um filter)
[ ] Agitation set (air or cathode rod)
[ ] Rectifier set to STRIKE current (50-75%
    of full CD) -- DO NOT start at full CD
```

JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 6 -- Common Racking Problems

**Section label:** `RACKING PROBLEMS` -- Y: 28.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | THICK EDGES / THIN CENTER | No conforming anodes or shields | Install conforming anodes; add shields at edges |
| 2 | 6.33" | NO DEPOSIT IN RECESSES | Recessed area too far from anode; current cannot reach | Auxiliary anode inside recess; or increase overall CD |
| 3 | 12.16" | CONTACT MARK DEFECT | Cathode lead wire blocks deposition at contact point | Relocate contact to non-critical area; use multiple contacts |
| 4 | 18.0" | POOR ELECTRICAL CONNECTION | Loose contact; oxide on bus bar; voltage drop | Clean contacts; torque bolts; measure voltage at mandrel |

---

### ZONE 7 -- Footer

Standard. Title: `Racking & Connection -- Electroforming`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Racking Connection Electroforming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The tank cross-section hero is the poster that electroforming operators will study most carefully. Every current distribution tool (conforming anodes, shields, thieves) is shown in spatial context relative to the mandrel. The curved current lines showing edge concentration are the visual "aha" -- operators see immediately why edges build thick and centers build thin, and then see the three solutions in place.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #473 -- Construction Workup v1.0*
*2026-04-26*
