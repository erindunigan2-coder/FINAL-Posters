---
Project: Plating Posters Inc
Poster Number: 661
Title: "Rinse / Dry -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.4"
Technical Source: Rinse and dry procedures for liquid spray painting. Covers DI rinse after conversion coating, air blow-off, force dry, tack cloth usage, and the key difference from powder coating -- some liquid primers are moisture-tolerant (wash primers/etch primers can be applied to damp surfaces).
Process Scope: Rinse and dry for liquid spray painting (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - RinseDry
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #661 -- Construction Workup
## Rinse / Dry -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. The rinse/dry stage for liquid spray painting shares principles with powder coating but has one critical difference: some liquid primers (wash primers, etch primers) can be applied to damp surfaces. This opens up field application options that powder coating can never match. The hero compares the standard dry path vs. the moisture-tolerant primer path side by side.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Standard dry path vs. moisture-tolerant path (Block B -- HERO):** Side-by-side comparison showing when full drying is required vs. when damp application is acceptable.
2. **Rinse quality table (Block C):** Conductivity targets.
3. **Tack cloth callout (Block D):** Between-coat dust removal.
4. **Defect grid (Block F):** 6 rinse/dry failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Rinse / Dry (Teal)
ZONE 3 -- STANDARD vs MOISTURE-TOLERANT HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- RINSE QUALITY + BLOW-OFF (15.0"--21.0" / ~6.0")
ZONE 5 -- TACK CLOTH + BETWEEN-COAT PREP (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- The Flexibility Advantage` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Unlike powder coating, some liquid primers can go on damp. That is the field application advantage that makes liquid paint irreplaceable.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Rinse / Dry -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned/conversion-coated wet surface --> After: Dry (or acceptably damp) surface ready for primer`

---

### ZONE 3 -- Standard vs. Moisture-Tolerant Hero

**Section label:** `TWO PATHS -- STANDARD DRY vs. MOISTURE-TOLERANT PRIMER` -- Y: 4.4".

**BLOCK B -- Side-by-Side (Y: 5.0" to 14.5")**

**Left -- Standard Dry Path (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`
- Title: `STANDARD DRY PATH` -- Barlow Condensed ExtraBold, 24 pt, `#E8A020`
- Subtitle: `Required for most primers and topcoats`

Flow (vertical sequence of 4 boxes with down arrows):

Box 1: `Rinse (DI water, < 50 uS/cm after conversion)`
Box 2: `Air blow-off (compressed air removes standing water from recesses)`
Box 3: `Force dry or air dry (remove ALL moisture)`
Box 4: `Apply primer to completely dry surface`

Key rules (Inter Medium 14 pt):
- `Standard epoxy primers: surface must be bone dry`
- `Standard alkyd primers: surface must be bone dry`
- `2K urethane primers: surface must be bone dry`
- `ALL topcoats: surface must be completely dry`

Warning (Coral): `Moisture trapped under standard primer = blistering, adhesion loss, premature corrosion`

**Right -- Moisture-Tolerant Path (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#27AE60`
- Title: `MOISTURE-TOLERANT PRIMER PATH` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
- Subtitle: `Field application advantage`

Flow (vertical sequence):

Box 1: `Rinse (remove chemical residuals)`
Box 2: `Blow off excess water (puddles, not film)`
Box 3: `Apply wash primer or etch primer to damp surface`
Box 4: `Flash dry, then topcoat per normal schedule`

Compatible primers (JetBrains Mono 13 pt `#27AE60`):
- `Wash primer (vinyl butyral etch): DOD-P-15328`
- `  Two-component: PVB resin + H3PO4 catalyst`
- `  DFT: 0.3--0.5 mil`
- `  Etches metal + converts + primes in one coat`
- `Self-etching primers: H3PO4-functional`
- `  DFT: 0.5--1.0 mil`
- `  Common in automotive refinish, aerospace touch-up`

Note: `Must be topcoated -- not a standalone primer. Excellent for field touch-up where multi-stage washer is unavailable.`

---

### ZONE 4 -- Rinse Quality + Blow-Off

**Section label:** `RINSE WATER QUALITY AND BLOW-OFF` -- Y: 15.2".

**Two-column layout (Y: 15.8" to 20.8"):**

**Left -- Rinse Quality (X: 0.5", W: 11.0"):**

| Rinse Position | Source | Max Conductivity | Notes |
|---|---|---|---|
| After alkaline clean | City water | 500 uS/cm | Remove cleaner residuals |
| After conversion coating | DI or RO | 50 uS/cm | Salt deposits cause blistering |
| Final rinse | DI water | 50 uS/cm | Critical for long-term adhesion |

Same principles as powder coating rinse quality.

**Right -- Blow-Off and Drying (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `BLOW-OFF AND DRYING` -- Barlow SemiBold, 18 pt, `#E8A020`

Methods:
- `Compressed air blow-off: Remove standing water from recesses, edges, and welds`
- `Air dry: Ambient, 15--30 min (weather/humidity dependent)`
- `Force dry: 140--180 F (60--82 C), 10--15 min`
- `Oven dry: 200--250 F (93--121 C), 5--10 min`

Note: `Oil-free compressed air ONLY. Compressor oil contamination causes fish-eye defects.` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Tack Cloth + Between-Coat Prep

**Section label:** `BETWEEN-COAT SURFACE PREP` -- Y: 21.2".

**Two-column layout (Y: 21.8" to 26.3"):**

**Left -- Tack Cloth (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `TACK CLOTH PROTOCOL` -- Barlow SemiBold, 18 pt, `#E8A020`

Steps:
1. `Sand between coats with 320--400 grit (if required by spec or if recoat window exceeded)`
2. `Blow off sanding dust with clean, dry compressed air`
3. `Wipe with LOW-TACK, SILICONE-FREE tack cloth`
4. `Light pressure -- do not press resin into the surface`
5. `Spray topcoat within 30 min of tack wipe`

**Right -- Intercoat Sanding (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `WHEN TO SAND BETWEEN COATS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Decision guide:
- `Within recoat window? NO sanding needed (chemical adhesion)`
- `Recoat window exceeded? SCUFF SAND required (mechanical adhesion)`
- `Typical recoat windows:`
- `  Alkyd: 24--72 hr`
- `  2K epoxy: 4--24 hr (CRITICAL -- epoxy hardens fast)`
- `  2K urethane: 1--24 hr`
- `Scuff sand with 320--400 grit, then tack wipe`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN RINSE OR DRY FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BLISTERING | `#E05C5C` | Moisture trapped under standard primer | Full drying before primer application |
| R1C2 | SALT DEPOSITS | `#E8A020` | High-TDS rinse water evaporating on surface | DI rinse; < 50 uS/cm final |
| R1C3 | FISH-EYE (COMPRESSED AIR) | `#E05C5C` | Oil-contaminated compressed air | Oil/water separator on air line |
| R2C1 | INTERCOAT ADHESION LOSS | `#E8A020` | Recoat window exceeded without scuff sand | Scuff with 320--400 grit before recoat |
| R2C2 | DUST NIBS | `#E05C5C` | Sanding dust not removed by tack cloth | Tack wipe after every sand step |
| R2C3 | TACK CLOTH FISH-EYE | `#2EC4B6` | Silicone-containing tack cloth | Use silicone-free, low-tack cloths only |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Wash primer compatibility and recoat windows are product-specific -- consult your coating manufacturer's TDS.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The side-by-side hero -- standard dry vs. moisture-tolerant primer -- is the unique story for liquid paint's rinse/dry stage. This is the feature that powder coating literally cannot replicate: the ability to prime a damp surface in the field using a wash primer. The intercoat recoat window table is sneaky-critical: missing that 4-24 hour epoxy window is one of the most common liquid paint failures. The tack cloth / silicone contamination warning rounds out the between-coat knowledge.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #661 -- Construction Workup v1.0*
*2026-04-26*
