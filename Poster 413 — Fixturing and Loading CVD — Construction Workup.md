---
Project: Plating Posters Inc
Poster Number: 413
Title: "Fixturing & Loading -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Sections 2.3, 2.5)"
Technical Source: CVD fixturing covering graphite and ceramic tray systems, retort loading patterns, gas flow path considerations, batch density optimization, and key differences from PVD fixturing (no rotation required -- CVD is not line-of-sight).
Process Scope: CVD fixturing and loading (Stage 5 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Fixturing
  - Loading
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #413 -- Construction Workup
## Fixturing & Loading -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 10. CVD fixturing is fundamentally different from PVD: no rotation is required because CVD is a chemical process, not a line-of-sight process. Gas flows around and between parts, reacting at every exposed surface. The challenge is ensuring uniform gas distribution throughout a densely packed load of 500-5,000 cutting inserts. Tray design, stacking pattern, and gas flow paths determine whether the center of the load gets the same coating as the edges.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Retort cross-section diagram (Block B -- HERO):** Side-view cross-section of a CVD hot-wall furnace retort showing stacked trays, gas inlet/outlet, and flow paths. Built from rectangles and arrows.
2. **CVD vs. PVD fixturing comparison (Block C):** Key differences -- no rotation, chemical vs. physical, gas flow vs. line-of-sight.
3. **Tray materials and design (Block D):** Graphite and ceramic tray specifications.
4. **Loading best practices (Block E):** Rules for optimizing batch density and uniformity.
5. **Common loading failures (Block F):** Four failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 20.0" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Teal -- loading)
ZONE 3 -- RETORT CROSS-SECTION / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- CVD VS. PVD FIXTURING (15.0"--20.0" / ~5.0")
ZONE 5 -- TRAY MATERIALS + LOADING RULES (20.0"--26.0" / ~6.0")
ZONE 6 -- COMMON LOADING FAILURES (26.0"--32.5" / ~6.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FIXTURING & LOADING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 5 of 10 -- Graphite Trays, Retort Loading, and Gas Flow Paths` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `CVD is not line-of-sight -- no rotation needed. But gas must reach every part uniformly. Tray design, stacking pattern, and load density control coating uniformity across 500-5,000 inserts per batch.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts cleaned and dried (Stage 4) --> After: Parts loaded in retort, ready for seal and purge`

---

### ZONE 3 -- Retort Cross-Section (HERO)

**Section label:** `INSIDE THE CVD RETORT -- GAS FLOW IS EVERYTHING` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Retort Diagram (Y: 5.0" to 14.8")**

Centered cross-section view of a cylindrical retort shown as a rounded rectangle (side view).

**Retort shell:**
- Rounded rect, X: 3.0", Y: 5.5", W: 18.0", H: 8.5", fill `#252B3D`, stroke 3 pt `#C8D0D8`
- Label: `RETORT (Inconel 600 or Graphite)` Barlow SemiBold 14 pt `#C8D0D8`, above shell

**Tray stack (inside retort):**
- 5 horizontal rectangles (trays) stacked vertically inside the retort
- Each tray: W: 14.0", H: 0.15", fill `#E8A020`, centered in retort
- Vertical spacing between trays: 1.2"
- Small rectangles (parts) sitting on each tray: 8-10 small squares (W: 0.5", H: 0.3") per tray, fill `#2EC4B6`
- Label on first tray: `GRAPHITE TRAY` Inter Medium 11 pt `#E8A020`
- Label on parts: `INSERTS` Inter Regular 10 pt `#2EC4B6`

**Gas flow arrows:**
- Left side: Large arrow pointing RIGHT into retort, fill `#27AE60`
- Label: `GAS IN (H2 + TiCl4 + reactive gases)` JetBrains Mono 12 pt `#27AE60`
- Right side: Large arrow pointing RIGHT out of retort, fill `#E05C5C`
- Label: `EXHAUST (H2 + HCl + byproducts)` JetBrains Mono 12 pt `#E05C5C`
- Between trays: Small horizontal arrows showing gas flowing between tray layers, stroke 2 pt `#27AE60`
- Label: `Gas flows between trays -- must reach center of load` Inter Regular 11 pt `#F0EDE8` at 60%

**Temperature zones (right side of retort):**
- Three horizontal bands labeled:
- `TOP ZONE` at top, `CENTER ZONE` at middle, `BOTTOM ZONE` at bottom
- Small thermometer icons or "TC" labels
- `All zones: 1000 +/- 5 C` JetBrains Mono 12 pt `#E8A020`

**Key metrics callout (below retort):**
- Rounded rect, X: 3.0", Y: 13.5", W: 18.0", H: 1.1", fill `#1E2435`, left accent `#E8A020`
- `Typical load: 500-5,000 inserts | Retort material: Inconel 600/601, graphite, or SiC | Tray material: Graphite (most common) or alumina ceramic` JetBrains Mono 12 pt `#F0EDE8`

---

### ZONE 4 -- CVD vs. PVD Fixturing

**Section label:** `CVD VS. PVD -- WHY FIXTURING IS DIFFERENT` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK C -- Comparison Table (Y: 15.8" to 19.8")**

| Property | PVD | CVD |
|---|---|---|
| Process type | Physical (line-of-sight) | Chemical (gas-phase reaction) |
| Rotation required? | YES -- planetary rotation mandatory | NO -- gas reaches all surfaces |
| Fixture complexity | High (planetary spindles, satellite fixtures) | Low (flat trays, stacking) |
| Batch size | 50-500 parts | 500-5,000 inserts |
| Key uniformity driver | Rotation speed + part-to-target distance | Gas flow distribution + temperature uniformity |
| Fixture material | Stainless steel, Ti, Mo | Graphite, alumina ceramic |
| Coating on fixtures? | Yes (must bead-blast to remove) | Yes (furnace etch cleans periodically) |
| Load time | 30-60 min (precise positioning) | 15-30 min (stack trays) |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`. Alternating rows.

Bottom callout:
- `CVD loading is simpler because it does not require precise part orientation relative to a target. But gas flow uniformity across a dense load of thousands of inserts is the equivalent challenge.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Tray Materials + Loading Rules

**Two-column layout (Y: 20.0" to 25.8"):**

**Left -- Tray Materials (X: 0.5", W: 11.0"):**
- Rounded rect H: 5.6", fill `#1E2435`, left accent `#E8A020`
- Title: `TRAY MATERIALS` Barlow SemiBold 20 pt `#E8A020`

| Material | Max Temp | Pros | Cons |
|---|---|---|---|
| Graphite | 2500 C | Light, inexpensive, easy to machine | Friable (particulate risk); reacts with O2 |
| Alumina ceramic | 1700 C | Chemical inert; no particulate | Heavy; brittle; expensive |
| SiC | 1600 C | Strong; chemical resistant | Expensive; specialty |

Data: JetBrains Mono 11 pt `#F0EDE8`.

Tray design notes:
- `Perforated trays improve gas flow between layers`
- `Tray edges must not block gas inlet/outlet`
- `BN spray on trays prevents insert adhesion to tray surface`
Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- Loading Rules (X: 12.0", W: 11.5"):**
- Rounded rect H: 5.6", fill `#1E2435`, left accent `#27AE60`
- Title: `LOADING BEST PRACTICES` Barlow SemiBold 20 pt `#27AE60`

Rules (Inter Medium 14 pt `#F0EDE8`):
- `Space inserts on trays -- do not stack or overlap`
- `Leave gaps between inserts for gas circulation (min 2-3 mm)`
- `Orient inserts consistently for reproducible results`
- `Do not overload -- center of load gets less gas if packed too tight`
- `Place witness coupons at top, center, and bottom of load`
- `Track tray usage -- replace cracked or eroded trays`
- `Record load map for traceability and troubleshooting`
- `Handle trays with cotton or Kevlar gloves -- not bare hands`

---

### ZONE 6 -- Common Loading Failures

**Section label:** `LOADING FAILURES -- WHAT GOES WRONG` -- Y: 26.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Failure Cards (Y: 26.8" to 32.3")**

Each card: Rounded rect W: 5.5", H: 5.3", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | THIN COATING AT CENTER | Gas depletion in densely packed center of load | Reduce load density; use perforated trays; increase gas flow rate |
| 2 | 6.33" | INSERTS STUCK TO TRAY | No BN release coating; graphite tray surface too rough | Apply BN spray before loading; use smooth-surface trays |
| 3 | 12.16" | PARTICULATE CONTAMINATION | Graphite tray crumbling; friable material from worn trays | Inspect trays before use; replace cracked/eroded trays |
| 4 | 18.0" | TEMPERATURE GRADIENT | Overloaded furnace; trays blocking thermocouple zones | Reduce load; verify multi-zone temp uniformity per AMS 2750 |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Fixturing & Loading -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Fixturing Loading CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The retort cross-section is the hero because it shows the fundamental CVD fixturing concept: gas flows horizontally between stacked trays of inserts, and the coating quality at the center of the load depends on gas reaching those parts. The CVD vs. PVD comparison table reinforces the key conceptual shift -- from line-of-sight (PVD) to gas-phase chemistry (CVD). The much larger batch size (500-5,000 vs. 50-500) makes CVD economically dominant for cutting inserts.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #413 -- Construction Workup v1.0*
*2026-04-26*
