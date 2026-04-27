---
Project: Plating Posters Inc
Poster Number: 693
Title: "Cure and Inspection -- Flow Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 5: Flow Coating, Sections 5.8 and 5.9)"
Process Scope: Cure and inspection for flow coating -- Stage 7 of 7 + Final Inspection
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - FlowCoating
  - Cure
  - Inspection
  - ConstructionWorkup
  - PaintingCoating
  - ClusterFC
---

# Poster #693 -- Construction Workup
## Cure and Inspection -- Flow Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 7 + Final Inspection. The coating is on the part -- now it has to become a film. Most flow-coated products are alkyd or modified alkyd (air dry or force dry) or baking enamel. The cure method follows the coating chemistry, not the application method. Inspection closes the loop: DFT at multiple locations (because flow coat variation is real), adhesion, and visual. This poster combines cure and inspection because flow coating's cure stage is identical to liquid spray painting -- the unique part is the inspection strategy for high-variation films.

Hero visual: cure methods diagram (air dry / force dry / bake) with temperature-time profiles, paired with a multi-point DFT measurement map on a flow-coated part.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cure methods diagram (Block B -- left):** Three horizontal bars showing temperature vs. time for air dry, force dry, and bake cure. Simple bar chart construction.
2. **DFT measurement map (Block B -- right):** A schematic part with numbered measurement locations and example readings showing thickness variation.
3. **Coating chemistry and cure table (Block D):** Cross-reference table matching coating type to cure method.
4. **Inspection checklist panel (Block E):** Complete QC checklist for flow-coated parts.
5. **Defect strip (Block F):** 4 common cure/inspection issues.

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
  Stage 7 highlighted (Emerald) + Inspect badge
ZONE 3 -- CURE METHODS + DFT MAP HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- COATING CHEMISTRY / CURE TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- INSPECTION CHECKLIST (20.5"--26.5" / ~6.0")
ZONE 6 -- COMMON CURE / INSPECTION ISSUES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE AND INSPECTION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Flow Coating -- Stage 7 of 7 + Final QC` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `The coating is on. Now make it a film. Then prove it meets spec -- at the top, the middle, AND the bottom, because flow coat variation is the reality you inspect around.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Inspect callout also highlighted with `#27AE60` border. Others dimmed.
Below: `Before: Drained wet film ready for cure  -->  After: Fully cured, inspected, ready for service or topcoat`

---

### ZONE 3 -- Cure Methods + DFT Map Hero

**Section label:** `CURE THE FILM -- THEN PROVE IT` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Split Hero (Two Panels)**

Y: 5.0" to 14.0".

**Left panel -- Cure Methods (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `CURE METHODS` -- Barlow SemiBold, 20 pt, `#27AE60`

Three horizontal cure bars (stacked vertically):

Bar 1 -- Air Dry (Y: 6.0"):
- Rect W: 10.0", H: 1.5", fill `#252B3D`
- Left label: `AIR DRY` Barlow SemiBold 14 pt `#2EC4B6`
- Parameters (JetBrains Mono 12 pt `#F0EDE8`):
  - `65-85 F (18-29 C)`
  - `1-7 days full cure`
- Right label: `Alkyds, latex` Inter Regular 12 pt `#F0EDE8` at 60%
- Temperature bar: thin rect fill `#2EC4B6` at 30%, representing low temp range

Bar 2 -- Force Dry (Y: 8.0"):
- Same structure
- Left label: `FORCE DRY` `#E8A020`
- Parameters:
  - `140-180 F (60-82 C)`
  - `30-60 min`
- Right label: `Modified alkyds, acrylics`
- Temperature bar: `#E8A020` at 40%, medium length

Bar 3 -- Bake (Y: 10.0"):
- Same structure
- Left label: `BAKE` `#E05C5C`
- Parameters:
  - `250-350 F (121-177 C)`
  - `15-30 min`
- Right label: `Baking enamels, thermosets`
- Temperature bar: `#E05C5C` at 40%, full length

Callout below bars (Y: 12.0"):
- Fill `#252B3D`, left accent `#E8A020` 0.06", W: 10.0", H: 1.5"
- Text: `Most flow-coated industrial primers are alkyd or modified alkyd. Force dry (140-180 F) is the production standard. Air dry for field applications. Bake for high-performance baking enamels.` -- Inter Regular, 13 pt, `#F0EDE8`

**Right panel -- DFT Measurement Map (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `MULTI-POINT DFT MAP` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `Flow coat variation requires measurement everywhere` -- Inter Regular, 12 pt, `#F0EDE8` at 60%

Part schematic (centered, Y: 6.5"):
- Simplified rectangular part shape with flange, fill `#3A4055`, border `#C8D0D8`
- 6 numbered measurement points with DFT readings:

| Point | Location | Reading | Status |
|---|---|---|---|
| 1 | Top edge | 0.6 mil | `#E05C5C` (below min) |
| 2 | Upper face | 1.1 mils | `#E8A020` (marginal) |
| 3 | Center face | 1.8 mils | `#27AE60` (target) |
| 4 | Lower face | 2.4 mils | `#27AE60` (in spec) |
| 5 | Bottom edge | 3.1 mils | `#E8A020` (heavy) |
| 6 | Drip point | 4.2 mils | `#E05C5C` (excessive) |

Each point: small circle with number, connected to a mini label showing the DFT reading in the status color. JetBrains Mono 12 pt.

Bottom note: `ASTM D7091 -- Minimum 3 readings per zone, 3 zones per part` -- JetBrains Mono, 11 pt, `#2EC4B6`

Key: `Spec: 1.0 mil minimum DFT` -- Inter Medium, 13 pt, `#27AE60`

---

### ZONE 4 -- Coating Chemistry / Cure Table

**Section label:** `COATING TYPE vs. CURE METHOD` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Cross-Reference Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Coating Type (5.0") | Cure Method (4.0") | Temperature (3.5") | Time (3.0") | Key Check (7.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Coating Type | Cure Method | Temperature | Time | Key Check |
|---|---|---|---|---|
| Alkyd enamel | Air dry or force dry | Ambient or 140-180 F | 1-7 days (air) / 30-60 min (force) | Tack-free to hard dry per TDS |
| Modified alkyd | Force dry | 140-180 F | 30-60 min | Through-dry; no soft spots |
| Baking enamel | Bake | 250-350 F | 15-30 min at PMT | Pencil hardness per spec |
| 2K epoxy primer | Chemical cure (ambient) | 50-100 F | 7-14 days full cure | MEK rub 50+ double rubs; recoat window 4-24 hr |
| 2K urethane | Chemical cure (ambient) | 50-100 F | 5-7 days full cure | Recoat window per TDS; hardness check |
| Latex / waterborne | Air dry + coalescence | 50-85 F, 40-70% RH | 1-7 days | Film formation temp must exceed 50 F |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Coating type names: Inter Medium, 13 pt.

Footnote:
- `PMT = Peak Metal Temperature. Always confirm cure by metal temp, not oven air temp. Use thermocouple data loggers for oven profiling.` -- Inter Regular, 12 pt, `#E8A020`

---

### ZONE 5 -- Inspection Checklist

**Section label:** `FLOW COATING INSPECTION CHECKLIST` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Checklist**

Y: 21.3" to 26.3".

**Left -- Film Property Tests (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `FILM PROPERTY TESTS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Test | Standard | Acceptance |
|---|---|---|
| DFT | ASTM D7091 | Minimum DFT per spec; measure top, middle, bottom |
| Adhesion | ASTM D3359 Method B | 4B-5B (crosshatch tape pull) |
| Hardness | ASTM D3363 | Per spec (F to 2H typical) |
| Flexibility | ASTM D522 mandrel bend | Per spec (1/8" to 1/2" mandrel) |
| Cure verification | MEK rub (ASTM D4752) | 50+ double rubs (thermoset only) |

Table: JetBrains Mono 11 pt `#F0EDE8` for standards; Inter Regular 12 pt for descriptions.

**Right -- Visual and Defect Checks (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `VISUAL AND DEFECT CHECKS` -- Barlow SemiBold, 18 pt, `#E8A020`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Runs and sags -- check bottom edges and drainage points`
- `Holidays -- check inner corners, upward-facing surfaces, shielded areas`
- `Orange peel -- check flow-coated surface under raking light`
- `Drip marks -- check lowest points of each part`
- `Color uniformity -- spot-check Delta E if multi-batch reservoir`
- `Blistering -- check recesses (trapped moisture indicator)`

Bottom note:
- `Flow coating inspection requires MORE measurement points than spray painting because of the inherent +/- 30-50% thickness variation. Minimum: 3 zones per part, 3 readings per zone.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 6 -- Common Cure / Inspection Issues

**Section label:** `WHAT GOES WRONG -- 4 CURE / INSPECTION ISSUES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | UNDERCURE (SOFT FILM) | Oven too cool, insufficient time at PMT, or low ambient temp (air dry) | Profile oven with thermocouple; extend cure time; increase temp |
| 2 | 6.33" | DFT BELOW MINIMUM (TOP) | Natural flow-coat drainage -- top of part always thinnest | Increase viscosity; reduce drain time; specify minimum DFT not target |
| 3 | 12.16" | SOLVENT POP / PINHOLES | Insufficient flash before bake; solvent trapped under surface skin | Extend flash time; reduce oven ramp rate for first 5 min |
| 4 | 18.0" | ADHESION FAILURE | Pretreatment failure, contamination, or undercure | Verify phosphate coating weight; check cleanliness; confirm cure (MEK rub) |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

**Key insight callout (Y: 30.6" to 32.3"):**
- Full-width rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Text: `The single most common inspection failure on flow-coated parts is DFT below minimum at the top of the part. The fix is almost never "coat heavier" -- it is to adjust part orientation, viscosity, and drain time to redistribute the existing film more evenly.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Cure and Inspection -- Flow Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Inspection Flow Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the Flow Coating cluster by combining cure and inspection. The cure side is intentionally compact because flow coating uses the same cure methods as liquid spray painting -- there is nothing flow-coat-specific about the chemistry. The inspection side is where the unique value lives: the DFT measurement map with color-coded readings makes the thickness variation tangible. Point 1 at 0.6 mil and Point 6 at 4.2 mil on the same part -- that is flow coating. The spec strategy callout ("specify minimum DFT, not target") is the practical wisdom that makes this poster worth hanging on the wall.

---

*Alaina -- Poster #693 -- Construction Workup v1.0 -- 2026-04-26*
