---
Project: Plating Posters Inc
Poster Number: 695
Title: "Surface Preparation -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.2)"
Process Scope: Surface preparation for coil coating -- Stage 1 (Uncoil / incoming condition)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - SurfacePreparation
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #695 -- Construction Workup
## Surface Preparation -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 -- Uncoil and incoming material condition. Coil coating has no abrasive blast step -- the substrate arrives from the steel or aluminum mill with mill oil and a known surface condition. Surface prep IS the incoming coil itself: its alloy, its coating (galvanized, Galvalume, bare CRS, aluminum), and the oil it carries. The coil coater's job starts with knowing what they are unwinding.

Hero visual: four coil cross-sections showing the substrate types (HDG, Galvalume, CRS, aluminum) with their surface characteristics.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate cross-section hero (Block B):** Four coil profile diagrams showing substrate layers and surface characteristics for each material type.
2. **Incoming coil specification table (Block D):** What the coil coater receives and what they check.
3. **Accumulator explanation panel (Block E):** How continuous operation is maintained during coil changes.
4. **Defect strip (Block F):** 4 incoming material defects.

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
  Stage 1 highlighted (Teal)
ZONE 3 -- SUBSTRATE TYPES HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- INCOMING COIL SPEC TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- ACCUMULATOR AND LINE THREADING (20.5"--26.5" / ~6.0")
ZONE 6 -- INCOMING MATERIAL DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stage 1: Incoming Material` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No blast. No grind. The substrate is the mill's product. Know what you are unwinding -- because every defect from the mill runs the full length of the coil.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw coil from steel or aluminum mill with mill oil  -->  After: Coil threaded through line, accumulator charged, ready for cleaning`

---

### ZONE 3 -- Substrate Types Hero

**Section label:** `FOUR SUBSTRATE TYPES -- WHAT YOU ARE COATING` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Four Substrate Panels**

Y: 5.0" to 14.0". Four equal panels.

Each panel: Rounded rect, W: 5.5", H: 8.5", fill `#1E2435`, top accent 4 pt.

**Panel 1 -- Hot-Dip Galvanized (HDG) (X: 0.5", accent `#E8A020`):**
- Badge: `HDG` fill `#E8A020`, text `#1A1F2E`
- Title: `Hot-Dip Galvanized Steel` -- Barlow SemiBold, 16 pt, `#E8A020`
- Cross-section diagram (stacked layers):
  - Bottom: `Steel substrate (0.015-0.060")` `#3A4055`
  - Middle: `Zinc coating (G60-G90)` `#C8D0D8`
  - Top: `Mill oil film` `#E8A020` at 15%
- Properties (JetBrains Mono 11 pt `#F0EDE8`):
  - `Zinc weight: 0.60-0.90 oz/ft2`
  - `Spangle: regular, minimized, or zero`
  - `Mill oil: 50-200 mg/m2`
- Note: `Most common substrate for building panels and gutters` -- Inter Regular, 11 pt, `#F0EDE8` at 70%

**Panel 2 -- Galvalume (X: 6.33", accent `#2EC4B6`):**
- Badge: `GL` fill `#2EC4B6`, text `#1A1F2E`
- Title: `Galvalume (55% Al-Zn)` -- Barlow SemiBold, 16 pt, `#2EC4B6`
- Cross-section:
  - `Steel substrate` `#3A4055`
  - `55% Al / 43.5% Zn / 1.5% Si coating` `#C8D0D8` with subtle speckle
  - `Mill oil film` `#E8A020` at 15%
- Properties:
  - `AZ50-AZ55 typical`
  - `Superior corrosion resistance to HDG`
  - `Mill oil: 50-200 mg/m2`
- Note: `Premium roofing and wall panels; better cut-edge corrosion than HDG`

**Panel 3 -- Cold-Rolled Steel (CRS) (X: 12.16", accent `#E05C5C`):**
- Badge: `CRS` fill `#E05C5C`, text `#F0EDE8`
- Title: `Cold-Rolled Steel (Bare)` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Cross-section:
  - `Steel substrate (bare)` `#3A4055`
  - `Drawing oil / anti-rust oil film` `#E8A020` at 15%
- Properties:
  - `No metallic coating -- bare steel`
  - `Must be coated immediately after cleaning`
  - `Flash rust risk if exposed`
- Note: `Appliance interiors, hidden structural panels; requires primer for corrosion protection`

**Panel 4 -- Aluminum (X: 18.0", accent `#27AE60`):**
- Badge: `AL` fill `#27AE60`, text `#1A1F2E`
- Title: `Aluminum Coil` -- Barlow SemiBold, 16 pt, `#27AE60`
- Cross-section:
  - `Aluminum substrate (3xxx or 5xxx)` lighter `#3A4055`
  - `Native oxide layer (thin)` `#C8D0D8` thin line
  - `Mill oil film` `#E8A020` at 15%
- Properties:
  - `3003, 3105, 5005, 5052 alloys typical`
  - `Naturally corrosion resistant`
  - `Lighter gauge (0.015-0.040")`
- Note: `Gutters, downspouts, composite panels, beverage cans`

---

### ZONE 4 -- Incoming Coil Specification Table

**Section label:** `WHAT THE COIL COATER CHECKS ON ARRIVAL` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Incoming Inspection Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Parameter (5.0") | Specification (5.5") | Method (5.0") | Why It Matters (7.5")

| Parameter | Specification | Method | Why It Matters |
|---|---|---|---|
| Gauge (thickness) | 0.015-0.060" (per order) | Micrometer | Wrong gauge = forming failure, structural underspec |
| Width | Per order +/- 0.010" | Steel rule / width gauge | Width out of spec = trim waste or edge defects |
| Coil weight | Per order (5,000-25,000 lb typical) | Scale | Affects accumulator run time |
| Surface condition | No rust, scale, or mechanical damage | Visual | Surface defects telegraph through coating |
| Oil weight | 50-200 mg/m2 typical | Gravimetric or solvent extraction | Excessive oil overloads cleaner |
| Zinc weight (HDG/GL) | Per spec (G60, G90, AZ50, etc.) | XRF or strip weight | Determines corrosion performance |
| Spangle (HDG) | Regular, minimized, or zero per spec | Visual | Large spangle can telegraph through thin coatings |

---

### ZONE 5 -- Accumulator and Line Threading

**Section label:** `THE ACCUMULATOR -- KEEPING THE LINE RUNNING` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Accumulator Panel**

Y: 21.3" to 26.3". Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

**Two-column layout:**

**Left (X: 1.0", W: 10.5"):**
- Title: `HOW IT WORKS` -- Barlow SemiBold, 18 pt, `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - `The accumulator is a looping tower that stores 200-600 ft of strip.`
  - `When one coil ends and the next is being stitched (welded), the accumulator pays out stored strip to keep the coating line running at full speed.`
  - `Without the accumulator, the line would stop for every coil change -- killing productivity on a 200-700 ft/min process.`
  - `Coil changes take 2-5 minutes. The accumulator must hold enough strip for that duration at line speed.`

**Right (X: 12.5", W: 10.5"):**
- Title: `KEY PARAMETERS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Parameter | Typical |
|---|---|
| Storage capacity | 200-600 ft of strip |
| Coil change time | 2-5 min |
| Stitcher type | Resistance weld or rivet |
| Line speed during change | Full speed (from accumulator) |
| Tension control | Dancer roll / load cell |

JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 6 -- Incoming Material Defects

**Section label:** `WHAT GOES WRONG -- 4 INCOMING MATERIAL DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SPANGLE SHOW-THROUGH | Large zinc crystals visible through thin topcoat | Specify minimized or zero-spangle HDG for coated product |
| 2 | 6.33" | EXCESSIVE MILL OIL | Oil weight above 200 mg/m2 overloads cleaner | Reject coil or increase cleaner concentration and brush stages |
| 3 | 12.16" | EDGE DAMAGE / BURRS | Shipping or handling damage to coil edges | Trim edges in-line; reject if damage extends beyond trim zone |
| 4 | 18.0" | RUST / STAINING | Moisture exposure during storage (coil sweating) | Store indoors, dry, temperature-controlled; inspect before threading |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `In coil coating, surface preparation is not something you do -- it is something you specify and verify. The substrate arrives from the mill. Your job is to confirm it meets spec before threading it into a line that runs at 400 ft/min with no way to stop for a bad coil.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Surface Preparation -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Preparation Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Coil coating's "surface prep" is fundamentally different from every other process in the painting series: there is no blast, no grind, no manual cleaning. The substrate is a mill product. This poster reframes surface prep as incoming material management -- what are you unwinding, and does it meet spec? The four substrate panels are the hero because every coil coater runs multiple substrates and needs to know the differences at a glance.

---

*Alaina -- Poster #695 -- Construction Workup v1.0 -- 2026-04-26*
