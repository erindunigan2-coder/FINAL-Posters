---
Project: Plating Posters Inc
Poster Number: 682
Title: "Flash / Leveling -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.7)"
Technical Source: Flash and leveling for dip coating -- drain zone behavior for plastisol, solution dip, and hot-dip thermoplastic. Covers gravity drainage as the leveling mechanism, rotation for uniform thickness, and the trade-off between viscosity and uniformity.
Process Scope: Flash / leveling for dip coating -- Stage 5.5 (between application and cure)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - FlashLeveling
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #682 -- Construction Workup
## Flash / Leveling -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The flash/leveling stage for dip coating is fundamentally different from spray painting: there is no solvent-driven leveling for plastisol (no solvent in plastisol) and no flow period for hot-dip (the coating solidifies as the part cools). The real action is drainage -- gravity pulling excess coating off the part. The hero compares drainage behavior across the three families. Rotation and part orientation are the operator's primary tools for managing uniformity, and they deserve prominent space.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-family drainage comparison (Block B -- HERO):** Plastisol drain, hot-dip cool, solution dip flash -- side-by-side.
2. **Rotation and part orientation (Block C):** How to achieve uniform thickness.
3. **Viscosity-uniformity trade-off (Block D):** The fundamental tension in dip coating leveling.
4. **Defect grid (Block F):** 6 flash/leveling defects.

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
  Stage highlighted (Teal)
ZONE 3 -- THREE-FAMILY DRAINAGE HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- ROTATION AND PART ORIENTATION (15.0"--21.0" / ~6.0")
ZONE 5 -- VISCOSITY-UNIFORMITY TRADE-OFF (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLASH / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Gravity Is Your Leveling Tool` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `No solvent to flash from plastisol. No flow period for hot-dip. Gravity drainage is the only leveling mechanism -- and part orientation is how you control it.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Flash / Leveling -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly dipped part with excess coating --> After: Drained part with controlled thickness ready for cure`

---

### ZONE 3 -- Three-Family Drainage Hero

**Section label:** `THREE FAMILIES -- THREE DRAINAGE BEHAVIORS` -- Y: 4.4".

**BLOCK B -- Three Columns (Y: 5.0" to 14.5")**

*Plastisol Drain (X: 0.5", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#E8A020`
- Title: `PLASTISOL DRAIN` -- Barlow SemiBold, 20 pt, `#E8A020`
- Subtitle: `No Solvent -- Drainage Only`
- Parameters (JetBrains Mono 12 pt):
```
Flash type: None (no solvent)
Drain time: 10--60 sec
Mechanism: Gravity pulls excess
  plastisol off part
Gel behavior: Plastisol is thixotropic
  -- viscosity drops under shear,
  recovers at rest
```
- Leveling tools:
- `Rotate or invert parts during drain`
- `Higher viscosity = less drainage = more uniform`
- `Lower viscosity = more drainage = thinner but uneven`
- Key: `Drainage stops when plastisol viscosity prevents further flow. Thick bottoms and thin tops are the default.`

*Hot-Dip Cool-Down (X: 8.17", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6`
- Title: `HOT-DIP COOL-DOWN` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Subtitle: `Solidification Is the "Leveling"`
- Parameters:
```
Flash type: None (thermoplastic)
Drain time: Brief -- coating solidifies
  as part cools
Mechanism: Molten coating freezes in
  place as part temperature drops
  below material's melt point
```
- Leveling tools:
- `Part temperature uniformity at dip is critical`
- `Hot spots get thicker coating`
- `Cool spots get thinner coating`
- `Rotation during cooling can help`
- Key: `The coating "levels" by freezing in place. No flow after solidification. Thickness uniformity depends entirely on uniform preheat.`

*Solution Dip Flash (X: 15.83", W: 7.67"):*
- Rounded rect, fill `#1E2435`, top accent `#27AE60`
- Title: `SOLUTION DIP FLASH` -- Barlow SemiBold, 20 pt, `#27AE60`
- Subtitle: `Solvent Evaporation + Drainage`
- Parameters:
```
Flash type: Solvent evaporation
Flash time: 5--15 min ambient
  or 5--10 min heated tunnel
  (120--160 F)
Mechanism: Solvent evaporates +
  excess drains simultaneously
```
- Leveling tools:
- `Hang parts at angle to direct drainage`
- `Rotation or tumbling for small parts`
- `Heated tunnel accelerates solvent release`
- `Prevent solvent entrapment before bake`
- Key: `Solution dip is the only dip family with true solvent flash. The drain zone + flash zone overlap -- solvent evaporating while excess drains.`

---

### ZONE 4 -- Rotation and Part Orientation

**Section label:** `ROTATION AND ORIENTATION -- YOUR UNIFORMITY TOOLS` -- Y: 15.2".

**Two-column layout (Y: 15.8" to 20.8"):**

**Left -- Rotation (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#E8A020`.
Title: `ROTATION DURING DRAIN` -- Barlow SemiBold, 20 pt, `#E8A020`

- `Rotate parts slowly during the drain/gel phase`
- `Prevents thick buildup at the lowest point`
- `Equalizes thickness around the circumference`
- `Speed: slow enough to avoid flinging -- typically 5--15 RPM`
- `Not all parts can be rotated -- complex geometries may need fixture redesign`

Applicable to: `Plastisol (most benefit), solution dip (moderate benefit), hot-dip (minimal -- freezes too fast)`

**Right -- Part Orientation (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `FIXTURE ORIENTATION RULES` -- Barlow SemiBold, 18 pt, `#27AE60`

Rules:
1. `Angle parts so excess drains away from critical surfaces`
2. `Drain holes: position at the lowest point of the fixture`
3. `Blind holes face DOWN -- trapped coating pools in upward-facing holes`
4. `Wire hooks: coat the hook too, or mask it to prevent drip transfer`
5. `Document the fixture orientation in the work instruction -- small angle changes produce large thickness differences`

---

### ZONE 5 -- Viscosity-Uniformity Trade-Off

**Section label:** `THE FUNDAMENTAL TRADE-OFF` -- Y: 21.2".

**Single wide callout (Y: 21.8" to 26.3", X: 0.5", W: 23.0"):**

Callout box, fill `#1E2435`, border 2 pt `#2EC4B6`.
Title: `VISCOSITY vs. UNIFORMITY -- THE DIP COATER'S DILEMMA` -- Barlow SemiBold, 20 pt, `#2EC4B6`

Two-column content inside:

**Left sub-column -- High Viscosity:**
- `THICKER coating per dip`
- `LESS drainage (more uniform top-to-bottom)`
- `SLOWER coverage of recesses`
- `BRIDGING risk increases (spans holes/slots)`
- `Fewer dip cycles needed for target thickness`

**Right sub-column -- Low Viscosity:**
- `THINNER coating per dip`
- `MORE drainage (thick bottom, thin top)`
- `BETTER penetration into recesses`
- `LESS bridging`
- `More dip cycles needed for target thickness`

Bottom insight: `There is no perfect viscosity -- only the right compromise for your part geometry and target DFT. Run test panels at 2-3 viscosity levels to find the sweet spot.` -- Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 DRAINAGE/LEVELING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | THICK BOTTOM / THIN TOP | `#E8A020` | Gravity drainage concentrating coating at bottom | Rotate parts; increase viscosity; reduce drain time |
| R1C2 | DRIP EDGE BUILDUP | `#E05C5C` | Excess coating accumulating at the lowest point | Angle part differently; extend drain; wipe drip edge |
| R1C3 | BRIDGING | `#E05C5C` | High viscosity causing coating to span holes/openings | Reduce viscosity; increase drain time; clear bridges before cure |
| R2C1 | SOLVENT ENTRAPMENT | `#E8A020` | Solution dip entering cure oven with trapped solvent | Extend flash time; use heated flash tunnel before bake |
| R2C2 | UNEVEN HOT-DIP (HOT/COLD SPOTS) | `#2EC4B6` | Non-uniform part temperature at dip | Extend preheat soak; verify oven uniformity |
| R2C3 | POOLING IN RECESSES | `#2EC4B6` | Coating collecting in blind holes or cup-shaped features | Orient drain holes down; use vacuum assist or air blow |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Flash / Leveling -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. Drain times and rotation speeds vary by part geometry and coating type. Optimize by test panel evaluation.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Flash Leveling Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-family drainage comparison makes the key point: dip coating "leveling" is fundamentally different for each family. Plastisol drains until viscosity stops it. Hot-dip freezes in place. Solution dip is the only one with true solvent flash. The viscosity-uniformity trade-off panel is the intellectual anchor -- it frames the operator's decision as a deliberate compromise rather than a search for one "correct" viscosity. Rotation and orientation rules are the practical shop-floor takeaway.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #682 -- Construction Workup v1.0*
*2026-04-26*
