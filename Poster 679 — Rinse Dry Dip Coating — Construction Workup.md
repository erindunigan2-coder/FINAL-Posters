---
Project: Plating Posters Inc
Poster Number: 679
Title: "Rinse / Dry -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.4)"
Technical Source: Rinse and dry procedures for dip coating. Covers complete drying requirement, oven dry parameters, and the preheat path for hot-dip thermoplastic where drying is inherent.
Process Scope: Rinse and dry for dip coating -- Stage 3 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - RinseDry
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #679 -- Construction Workup
## Rinse / Dry -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 7. Dip coating is unforgiving about moisture: water trapped under a 20-mil plastisol coat has nowhere to go during a 400 F cure, and it will blister violently. The hero contrasts two drying paths -- the standard oven dry for plastisol and solution dip, and the preheat path for hot-dip thermoplastic where the 400-600 F preheat inherently eliminates all moisture. No ambiguity, no shortcuts: the part must be bone dry before it touches the dip tank.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Standard dry vs. preheat path (Block B -- HERO):** Side-by-side comparison of oven dry path and hot-dip preheat path.
2. **Rinse quality requirements (Block C):** DI water and conductivity targets.
3. **Moisture verification (Block D):** How to confirm parts are dry.
4. **Defect grid (Block F):** 6 rinse/dry defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal)
ZONE 3 -- STANDARD DRY vs. PREHEAT HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- RINSE QUALITY + WATER MANAGEMENT (15.0"--21.0" / ~6.0")
ZONE 5 -- MOISTURE VERIFICATION + BLOW-OFF (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Bone Dry or Blistered -- Stage 3 of 7` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Water trapped under a thick dip coat has nowhere to go during cure. The moisture turns to steam, and the coating bubbles off the part. Dry it completely or do not dip it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned parts with rinse water residue --> After: Completely dry parts ready for priming or dipping`

---

### ZONE 3 -- Standard Dry vs. Preheat Hero

**Section label:** `TWO DRYING PATHS -- STANDARD AND PREHEAT` -- Y: 4.4".

**BLOCK B -- Two-Panel Comparison (Y: 5.0" to 14.5")**

**Left -- Standard Oven Dry Path (X: 0.5", W: 11.0", H: 9.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`
- Title: `STANDARD OVEN DRY` -- Barlow Condensed ExtraBold, 24 pt, `#E8A020`
- Subtitle: `For plastisol and solution dip applications`

Flow (vertical sequence of 4 boxes with down arrows):

Box 1: `Rinse: DI water final rinse to remove chemical residuals`
Box 2: `Air blow-off: Compressed air removes standing water from recesses`
Box 3: `Oven dry: 200--250 F (93--121 C), 10--15 min`
Box 4: `Cool to ambient before dipping`

Key rules (Inter Medium 14 pt):
- `Parts must be COMPLETELY DRY before entering dip tank`
- `Standing water in recesses = blistering during cure`
- `Heavier parts need longer soak time in dry oven`
- `Oil-free compressed air only for blow-off`

Warning (Coral): `Plastisol cure at 350--400 F will violently blister any trapped moisture. There is no tolerance for residual water.`

**Right -- Hot-Dip Preheat Path (X: 12.0", W: 11.5", H: 9.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#27AE60`
- Title: `HOT-DIP PREHEAT PATH` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
- Subtitle: `For nylon, polyethylene, PVC hot-dip applications`

Flow (vertical sequence):

Box 1: `Rinse: Remove chemical residuals`
Box 2: `Preheat oven: 400--600 F (204--316 C)`
Box 3: `Preheat inherently eliminates ALL moisture`
Box 4: `Transfer directly to fluidized bed or dip tank`

Key rules:
- `Preheat temperature far exceeds boiling point -- moisture is driven off completely`
- `No separate dry step needed`
- `Part temperature at dip determines film build`
- `Hotter part = thicker coating`

Note (Emerald): `The preheat step does double duty: it dries the part AND sets the dip temperature that controls film thickness. Efficiency built into the process.`

---

### ZONE 4 -- Rinse Quality + Water Management

**Section label:** `RINSE WATER QUALITY` -- Y: 15.2".

**Two-column layout (Y: 15.8" to 20.8"):**

**Left -- Rinse Quality Table (X: 0.5", W: 11.0"):**

Title: `RINSE WATER TARGETS` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Rinse Stage | Source | Max Conductivity | Notes |
|---|---|---|---|
| After alkaline clean | City water | 500 uS/cm | Remove cleaner residuals |
| Final rinse | DI or RO | 50 uS/cm | Prevent salt deposits under coating |

Note: `Salt deposits from hard water rinse become trapped under thick dip coatings and cause osmotic blistering in service -- especially in humid or wet environments.`

**Right -- Water Management (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `COUNTERFLOW RINSE` -- Barlow SemiBold, 18 pt, `#2EC4B6`

- `Fresh DI water enters the final rinse stage`
- `Overflows backward to earlier stages`
- `Conserves water while maintaining quality`
- `Monitor conductivity at each stage`
- `Replace DI when conductivity exceeds target`

---

### ZONE 5 -- Moisture Verification + Blow-Off

**Section label:** `VERIFYING DRYNESS BEFORE DIP` -- Y: 21.2".

**Two-column layout (Y: 21.8" to 26.3"):**

**Left -- Moisture Verification (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `HOW TO VERIFY DRY` -- Barlow SemiBold, 18 pt, `#E8A020`

Methods:
1. `Visual: No visible water droplets, beading, or wet spots`
2. `Touch: Surface feels completely dry to clean gloved hand`
3. `Compressed air probe: Direct air into recesses -- no water spray-out`
4. `IR thermometer: Surface temp above 150 F after oven confirms moisture driven off`

Warning: `Recesses, blind holes, and weld seams trap water that is invisible from the outside. Blow-off BEFORE oven, and verify AFTER oven.`

**Right -- Blow-Off Best Practices (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `COMPRESSED AIR BLOW-OFF` -- Barlow SemiBold, 18 pt, `#27AE60`

- `Blow off BEFORE oven entry to reduce dry time`
- `Focus on recesses, blind holes, overlapping joints`
- `Use oil-free, filtered compressed air`
- `Moisture separator on air line is mandatory`
- `Contaminated air = fish-eye defects in the dip coat`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 RINSE/DRY DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BLISTERING (CURE) | `#E05C5C` | Trapped moisture boiling during 350--400 F cure | Complete drying; blow-off recesses; extend oven time |
| R1C2 | OSMOTIC BLISTERING (SERVICE) | `#E8A020` | Salt deposits from hard water under coating | DI final rinse; conductivity < 50 uS/cm |
| R1C3 | FISH-EYE (AIR LINE) | `#E05C5C` | Oil from compressed air contaminating surface | Oil/water separator; filter maintenance |
| R2C1 | WATER SPOTS | `#E8A020` | Hard water drying on surface before oven | DI rinse; blow-off standing water before dry oven |
| R2C2 | ADHESION LOSS (PREHEAT) | `#2EC4B6` | Oxidation scale from excessive preheat temperature | Control preheat temp per spec; verify surface condition |
| R2C3 | UNEVEN PREHEAT | `#2EC4B6` | Thick/thin sections at different temperatures at dip | Extend preheat soak; uniform part geometry in batch |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Drying temperatures and times vary by part mass and geometry. Hot-dip preheat temperatures are coating-specific -- consult supplier TDS.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-path hero makes the drying story crystal clear: standard oven dry for plastisol/solution dip, and preheat (which inherently dries) for hot-dip thermoplastic. The moisture verification section is practical and important -- recesses trap water that is invisible from outside, and a single trapped droplet creates a blister the size of a quarter during cure. The preheat doing double duty (drying + thickness control) is an elegant process design worth highlighting.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #679 -- Construction Workup v1.0*
*2026-04-26*
