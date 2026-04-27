---
Project: Plating Posters Inc
Poster Number: 696
Title: "Cleaning -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.3)"
Process Scope: Cleaning for coil coating -- Stage 2 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - Cleaning
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #696 -- Construction Workup
## Cleaning -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 9. Cleaning at line speed. The coil coating cleaner section is 20-40 feet long and the strip is moving at 200-700 ft/min -- contact time is measured in seconds, not minutes. High pressure alkaline spray plus counter-rotating brush scrubbers do in seconds what a soak tank does in minutes. Oil must drop below 5 mg/m2 or the conversion coating fails, and every downstream coating with it.

Hero visual: cutaway diagram of a multi-stage brush scrubber section showing spray nozzles, rotating brushes, and the strip path, with parameter callouts at each stage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Brush scrubber cutaway hero (Block B):** Simplified side-view showing 2-4 brush stages with spray headers and the strip path through the section.
2. **Cleaning parameters table (Block D):** Complete operational parameters for coil line cleaning.
3. **Cleanliness verification panel (Block E):** Methods for confirming oil removal at line speed.
4. **Defect strip (Block F):** 4 cleaning-related defects.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- BRUSH SCRUBBER HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING PARAMETERS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- CLEANLINESS VERIFICATION (20.5"--26.5" / ~6.0")
ZONE 6 -- CLEANING DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stage 2 of 9` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Seconds, not minutes. The strip is moving at 400 ft/min -- spray pressure and brush scrubbers replace soak time. Get the oil below 5 mg/m2 or nothing downstream will stick.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Mill-oiled coil strip from uncoiler  -->  After: Oil-free surface ready for conversion coating`

---

### ZONE 3 -- Brush Scrubber Hero

**Section label:** `ALKALINE SPRAY + BRUSH SCRUB -- AT LINE SPEED` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Scrubber Section Diagram (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`.

Side-view cutaway showing the strip (horizontal line, `#C8D0D8`) passing through four stages left-to-right:

**Stage A -- Pre-Spray (X: 1.5", W: 4.5"):**
- Spray nozzle icons (above and below strip), fill `#2EC4B6`
- Label: `PRE-SPRAY` Barlow SemiBold 14 pt `#2EC4B6`
- Parameters (JetBrains Mono 11 pt `#F0EDE8`):
  - `Alkaline, pH 10-12`
  - `130-160 F (54-71 C)`
  - `15-30 psi spray`
  - `1-3% concentration`

**Stage B -- Brush 1 (X: 6.5", W: 4.5"):**
- Two counter-rotating brush circles (above and below strip), fill `#E8A020` at 30%
- Rotation arrows showing counter-rotation
- Label: `BRUSH SCRUB 1` Barlow SemiBold 14 pt `#E8A020`
- Parameters:
  - `Nylon bristle`
  - `Counter-rotating`
  - `Mechanical oil removal`

**Stage C -- Brush 2 (X: 11.5", W: 4.5"):**
- Same brush diagram
- Label: `BRUSH SCRUB 2` Barlow SemiBold 14 pt `#E8A020`
- Parameters:
  - `2-4 brush stages total`
  - `Fresh alkaline spray at each`
  - `Progressive cleaning`

**Stage D -- Rinse Spray (X: 16.5", W: 5.5"):**
- Spray nozzle icons, fill `#27AE60`
- Label: `DI RINSE SPRAY` Barlow SemiBold 14 pt `#27AE60`
- Parameters:
  - `DI water, 2 stages`
  - `Counterflow design`
  - `Conductivity < 30 uS/cm`

Strip path: continuous horizontal line with directional arrow showing travel direction (left to right), labeled `STRIP TRAVEL: 200-700 ft/min` in JetBrains Mono 12 pt `#F0EDE8`.

Bottom callout (Y: 12.5"):
- Fill `#252B3D`, left accent `#E8A020` 0.06", W: 21.0", H: 1.0"
- Text: `The entire cleaning section is only 20-40 feet long. At 400 ft/min, a point on the strip passes through the entire cleaner in 3-6 seconds. Brush scrubbers provide the mechanical action that compensates for zero soak time.` -- Inter Regular, 13 pt, `#F0EDE8`

---

### ZONE 4 -- Cleaning Parameters Table

**Section label:** `OPERATIONAL PARAMETERS` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Parameter Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Parameter (5.0") | Specification (6.0") | Control Method (5.5") | Notes (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Parameter | Specification | Control Method | Notes |
|---|---|---|---|
| Cleaner type | Low-foam alkaline, pH 10-12 | pH meter / titration | Must be low-foam for spray application |
| Concentration | 1-3% by volume | Titration (free alkalinity) | Higher concentration for heavier oil loads |
| Temperature | 130-160 F (54-71 C) | Thermocouple | Higher temp improves oil removal |
| Spray pressure | 15-30 psi | Pressure gauge | Consistent across width |
| Brush stages | 2-4 stages, nylon bristle | Visual inspection | Counter-rotating; replace worn brushes |
| Rinse water | DI spray, 2 stages counterflow | Conductivity meter | < 30 uS/cm final rinse |
| Oil removal target | < 5 mg/m2 residual | Gravimetric or solvent extraction | Critical -- trace oil causes adhesion failure |
| Surface carbon | < 2 mg/m2 | Surface carbon analyzer | Premium QC for high-performance lines |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

---

### ZONE 5 -- Cleanliness Verification

**Section label:** `PROVING THE SURFACE IS CLEAN` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Verification Panel**

Y: 21.3" to 26.3".

**Left -- Test Methods (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `VERIFICATION METHODS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Method | How It Works | Frequency |
|---|---|---|
| Water break test | Pull strip sample, rinse -- unbroken water film = clean | Per coil or per shift |
| Surface carbon analysis | Quantitative measurement < 2 mg/m2 | Premium lines / qualification |
| Gravimetric oil measurement | Solvent extraction, weigh residue | Troubleshooting or qualification |
| Rinse water conductivity | Monitor final rinse conductivity < 30 uS/cm | Continuous (in-line meter) |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Why 5 mg/m2 Matters (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `THE 5 mg/m2 THRESHOLD` -- Barlow SemiBold, 18 pt, `#E8A020`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Coil coating primer is only 0.15-0.30 mil thick`
- `At this thickness, even trace oil prevents adhesion`
- `5 mg/m2 is the industry consensus maximum for reliable performance`
- `< 2 mg/m2 surface carbon is the premium target`
- `Conversion coating chemistry will not react on an oily surface`
- `Every downstream step -- primer, topcoat, forming -- depends on this cleaning stage`

Big stat callout (Y: 25.5"):
- `< 5 mg/m2` Barlow Condensed ExtraBold 48 pt `#E8A020` centered
- `Maximum residual oil for coil coating` Inter Medium 14 pt `#F0EDE8`

---

### ZONE 6 -- Cleaning Defects

**Section label:** `WHAT GOES WRONG -- 4 CLEANING DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | OIL SKIP (ADHESION FAILURE) | Insufficient brush contact or worn bristles | Replace brushes; verify nip pressure against strip |
| 2 | 6.33" | CLEANER RESIDUE ON STRIP | Inadequate rinse or high cleaner concentration | Verify rinse conductivity; check spray nozzle coverage |
| 3 | 12.16" | UNEVEN CLEANING (STREAKS) | Clogged spray nozzles or misaligned brushes | Clean nozzles; realign brush pressure across width |
| 4 | 18.0" | FOAM IN CLEANER SECTION | Wrong cleaner type (high-foam in spray system) | Switch to low-foam formulation designed for spray |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `The coil coating cleaner is the shortest-contact-time cleaning step in all of industrial painting. It compensates with mechanical action (brushes) and chemistry (hot alkaline spray). If the cleaner fails, the failure mode is adhesion loss -- and you will not see it until the formed product is in service.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The hero diagram sells the speed. A 20-40 foot section at 200-700 ft/min means the strip sees the entire cleaner in seconds. The brush scrubber cutaway makes this tangible -- you can see the counter-rotating brushes physically scrubbing oil off a moving strip. The 5 mg/m2 big-stat callout anchors the cleaning target in memory. Everything about coil coating cleaning is about compensating for zero soak time with mechanical force and chemistry.

---

*Alaina -- Poster #696 -- Construction Workup v1.0 -- 2026-04-26*
