---
Project: Plating Posters Inc
Poster Number: 677
Title: "Surface Preparation -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.2)"
Technical Source: Surface preparation methods for dip coating applications including steel parts, wire/cable, and consumer products. Covers blast profiles, adhesion promoters, and primer requirements.
Process Scope: Surface preparation for dip coating -- Stage 1 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - SurfacePreparation
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #677 -- Construction Workup
## Surface Preparation -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 7. Dip coating may be forgiving on thickness uniformity, but it is unforgiving on adhesion. A thick PVC or nylon coating that peels off the substrate is worse than no coating at all -- it creates a hidden failure. Surface prep for dip coating is a three-part system: clean, roughen, and prime. Each dip family has different primer requirements, and getting them wrong is the number one cause of field failures.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-substrate prep comparison (Block B -- HERO):** Three large callout boxes showing prep for steel parts, wire/cable, and consumer products (tool handles).
2. **Primer requirements by coating family (Block C):** Table showing which primer systems are required for each dip family on each substrate.
3. **Blast profile panel (Block D):** Steel blast specifications.
4. **Defect grid (Block F):** 6 surface prep defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- THREE-SUBSTRATE PREP HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- PRIMER REQUIREMENTS TABLE (14.5"--21.0" / ~6.5")
ZONE 5 -- BLAST PROFILE + ADHESION PROMOTERS (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT DIAGNOSIS GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Clean, Roughen, Prime -- Stage 1 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `A thick coating that peels is worse than no coating. Surface prep is the difference between a 10-year life and a warranty claim.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw steel, wire, or fabricated part with oils and mill scale  -->  After: Clean, profiled, primed surface ready for dip coating`

---

### ZONE 3 -- Three-Substrate Prep Hero

**Section label:** `SURFACE PREP BY SUBSTRATE TYPE` -- Y: 4.4".

**BLOCK B -- Three Callout Boxes (Y: 5.0" to 14.0")**

**Left -- Steel Parts (X: 0.5", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `STEEL PARTS` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Racking, Fixtures, Industrial Components` 14 pt `#F0EDE8` at 50%

Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
```
1. Alkaline clean
   120--160 F, 5--15 min soak
   Remove oils, greases, drawing compounds

2. Rinse
   City water, ambient

3. Abrasive blast
   80--120 grit aluminum oxide or steel grit
   SSPC-SP6 minimum (commercial blast)
   Profile: 1.5--3.0 mils (38--76 um)

4. Phosphate conversion (optional)
   Iron phosphate, 25--75 mg/ft2
   Improves under-film corrosion resistance

5. Primer coat
   Specific to coating family (see table)
   DFT: 0.3--1.0 mil, baked or air-dried
```

Key callout: `Blast-to-prime within 4 hours in humid conditions to prevent flash rust.` Inter Medium 13 pt `#E05C5C`

**Center -- Wire & Cable (X: 8.17", W: 7.33", H: 8.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `WIRE & CABLE` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Continuous Line Processing` 14 pt `#F0EDE8` at 50%

Content:
```
1. In-line alkaline spray clean
   With ultrasonic assist
   Removes drawing lubricant residues

2. Rinse
   DI water spray

3. Dry
   Hot air or IR dryer

No blasting -- wire gauge is too small.
Adhesion relies on chemical bonding
between primer and clean copper/steel
surface.

Line speeds: 100--1,000+ ft/min
  (prep must keep up with coating speed)
```

Key callout: `Drawing lubricant residue is the #1 adhesion killer on wire. Clean it completely.` Inter Medium 13 pt `#2EC4B6`

**Right -- Tool Handles / Consumer (X: 15.83", W: 7.67", H: 8.5"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `TOOL HANDLES & CONSUMER` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `Grips, Racks, Household Items` 14 pt `#F0EDE8` at 50%

Content:
```
1. Degrease
   Solvent wipe or alkaline wash

2. Mechanical roughening
   80--120 grit blast or Scotch-Brite
   Creates mechanical anchor pattern

3. Adhesion promoter / primer
   PVC on steel: phenolic or polyester
   PE on steel: chlorinated polyolefin
     or flame treatment
   Nylon on steel: epoxy primer

Critical: primer selection must match
the dip coating material. Wrong primer
= delamination in service.
```

Key callout: `Flame treatment activates PE/PP surfaces for adhesion without primer.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Primer Requirements Table

**Section label:** `PRIMER REQUIREMENTS BY COATING FAMILY` -- Y: 14.7".

**BLOCK C -- Primer Matrix Table (Y: 15.3" to 20.8")**

Column widths (23.0" total):
- Coating Family (5.0") | On Steel (6.0") | On Aluminum (6.0") | On Wire/Cable (6.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt `#F0EDE8`.

| Coating Family | On Steel | On Aluminum | On Wire/Cable |
|---|---|---|---|
| PVC Plastisol | Phenolic or polyester primer | Chromate conversion + primer | Not typical |
| Nylon 11/12 | Epoxy primer (baked) | Epoxy primer | Epoxy primer |
| Polyethylene (PE) | Chlorinated polyolefin or flame | Flame or plasma treatment | Direct (with clean surface) |
| Polypropylene (PP) | Flame or plasma treatment | Flame or plasma treatment | Not typical |
| Epoxy solution dip | Iron/zinc phosphate (no primer) | Chromate or Zr conversion | Alkaline clean only |
| Rubber/latex dip | Adhesive primer (proprietary) | Not typical | Not typical |

Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Blast Profile + Adhesion Promoters

**Two-column layout (Y: 21.2" to 26.3"):**

**Left -- Blast Profile (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `BLAST PROFILE FOR DIP COATING` Barlow SemiBold 20 pt `#E8A020`

Content:
```
Target profile: 1.5--3.0 mils (38--76 um)
Standard: ASTM D4417

Media options:
  Aluminum oxide (aggressive, sharp profile)
  Steel grit (consistent, recyclable)
  Garnet (moderate, low dust)

Blast grade:
  SSPC-SP6 (Commercial) -- minimum
  SSPC-SP10 (Near-White) -- heavy duty

Measurement:
  Testex replica tape + micrometer
  Or surface profile gauge

Blast-to-prime window: 4 hours max
  in >60% RH environments
```

**Right -- Adhesion Promoters (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `ADHESION PROMOTERS & PRIMERS` Barlow SemiBold 20 pt `#27AE60`

Content:
```
Adhesion promoters create a chemical
bridge between the metal substrate
and the dip coating material.

Phenolic primer (PVC on steel):
  Heat-resistant, bonds PVC plasticizer
  DFT: 0.3--0.5 mil, bake at 350 F

Epoxy primer (nylon on steel):
  Excellent adhesion to both metal
  and nylon; DFT 0.5--1.0 mil

Chlorinated polyolefin (PE on steel):
  Chemical bond to polyethylene
  Spray or dip applied

Flame treatment (PE/PP):
  Oxidizes surface, creates polar
  groups for adhesion -- no primer
  needed but equipment-intensive
```

---

### ZONE 6 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 SURFACE PREP DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | COATING PEELING | `#E05C5C` | Wrong primer for coating-substrate combination | Match primer to coating family (see table above) |
| R1C2 | BLISTERING AT INTERFACE | `#E05C5C` | Trapped moisture under primer or coating | Complete drying before priming; pre-bake porous substrates |
| R1C3 | RUST UNDER COATING | `#E8A020` | Insufficient blast grade or skipped phosphate | Blast to SSPC-SP6 minimum; add phosphate conversion |
| R2C1 | FLASH RUST BEFORE PRIME | `#E8A020` | Excessive delay between blast and primer | Prime within 4 hours; control humidity in blast area |
| R2C2 | THIN SPOTS / POOR WETTING | `#2EC4B6` | Oil contamination or insufficient surface energy | Re-clean; verify water-break-free before priming |
| R2C3 | PRIMER ADHESION FAILURE | `#E05C5C` | Primer applied over contaminated or wet surface | Clean surface, dry completely, re-prime |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Surface Preparation -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge. Primer requirements vary by coating supplier formulation. Always verify primer compatibility with your specific dip coating material.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Preparation Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The primer matrix table is the most valuable reference element on this poster -- it answers the question that causes 80% of dip coating adhesion failures: "which primer do I use?" The three-substrate breakdown grounds the prep requirements in real applications. The blast profile section connects dip coating to the broader SSPC standards that industrial coating professionals already know.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #677 -- Construction Workup v1.0*
*2026-04-26*
