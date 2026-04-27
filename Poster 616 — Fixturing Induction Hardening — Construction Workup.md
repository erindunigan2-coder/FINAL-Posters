---
Project: Plating Posters Inc
Poster Number: 616
Title: "Fixturing -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.8)"
Technical Source: Induction hardening fixturing -- part holding, rotation, scanning mechanisms, and the critical requirement for non-magnetic fixture materials. Coil-to-part coupling distance is the single most important fixturing parameter.
Process Scope: Induction hardening -- loading and fixturing
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - InductionHardening
  - Fixturing
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #616 -- Construction Workup
## Fixturing -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Fixturing for induction is fundamentally different from furnace fixturing. The fixture is not just holding the part in a hot environment -- it is positioning the part precisely inside an electromagnetic field. Every millimeter of coil-to-part gap matters. And the fixture material itself must be non-magnetic, or it will heat up instead of the part.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Fixturing methods diagram (Block B -- HERO):** Three panels showing between-centers, chuck, and scanning setups.
2. **Coupling distance gauge (Block D):** Visual representation of coil-to-part gap and its effect on heating efficiency.
3. **Rotation requirements (Block E):** Table of rotation speeds and their purposes.
4. **Material selection callout (Block F):** Non-magnetic materials only -- why and what to use.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- FIXTURING METHODS / HERO (4.2"--14.5" / ~10.3")
  Block B: Three fixturing method panels
  Block C: Scanning vs. single-shot comparison
ZONE 4 -- COUPLING DISTANCE (14.5"--22.0" / ~7.5")
  Block D: Gap gauge + efficiency relationship
ZONE 5 -- ROTATION + MATERIAL SELECTION (22.0"--32.5" / ~10.5")
  Block E: Rotation speed table
  Block F: Fixture material requirements
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FIXTURING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 2 of 7` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Position the part precisely in the electromagnetic field. Non-magnetic fixtures only. Every thousandth of gap matters.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, verified part  -->  After: Part positioned and rotating in the inductor`

---

### ZONE 3 -- Fixturing Methods (HERO)

**Section label:** `THREE FIXTURING APPROACHES` -- Y: 4.4".

**BLOCK B -- Three Method Panels**

Y: 5.0" to 12.0". Three panels side by side.

Each panel: Rounded rect W: 7.33", H: 6.5", fill `#1E2435`, radius 8, top accent 4 pt.

| Panel | X | Method | Accent | Description |
|---|---|---|---|---|
| 1 | 0.5" | BETWEEN CENTERS | `#2EC4B6` | Part held between tailstock and headstock centers (like a lathe). Part rotates. Best for shafts, axles, pins. Centers must be non-magnetic. Most common method for cylindrical parts. |
| 2 | 8.17" | CHUCK / COLLET | `#E8A020` | Part gripped in chuck or collet. Good for short parts, gears, flanges. Chuck jaw material: brass or non-magnetic stainless. Part can rotate or remain stationary for single-shot. |
| 3 | 15.83" | CNC SCANNING | `#27AE60` | Part held stationary (or rotating); inductor coil travels along the part length on a CNC carriage. Trailing spray quench follows the coil. Best for long shafts, rolls, and bars. Scan speed: 0.1--2.0 in/sec. |

Panel interior:
- Method name: Barlow SemiBold 20 pt, accent color
- Diagram placeholder: Rounded rect 6.0" x 2.5", fill `#252B3D`, center text `[Diagram placeholder]`
- Description: Inter Regular 13 pt `#F0EDE8`
- Best for: Inter Medium 12 pt, accent color

**BLOCK C -- Scanning vs. Single-Shot**

Y: 12.3" to 14.3". Full-width comparison strip.

Two side-by-side boxes:

| Method | X | W | Accent | Key Points |
|---|---|---|---|---|
| SINGLE-SHOT | 0.5" | 11.0" | `#E8A020` | Entire area heated simultaneously; no coil movement; fastest cycle; best for localized areas (gear teeth, bearing seats); requires high power |
| PROGRESSIVE SCAN | 12.0" | 11.5" | `#2EC4B6` | Coil moves along part with trailing quench; lower instantaneous power; best for long surfaces (shafts); creates uniform case along length |

Each: Rounded rect H: 1.8", fill `#1E2435`, left accent 0.06".

---

### ZONE 4 -- Coupling Distance

**Section label:** `COIL-TO-PART GAP -- THE CRITICAL DIMENSION` -- Y: 14.7".

**BLOCK D -- Gap Gauge**

Y: 15.3" to 21.8".

**Left -- Visual gauge (X: 0.5", W: 11.0"):**

Horizontal bar gauge showing coupling distance ranges:

| Range | Fill | Label | Effect |
|---|---|---|---|
| < 0.030 in | `#E05C5C` at 40% | TOO CLOSE | Risk of arcing; coil damage; uneven heating |
| 0.040--0.060 in | `#27AE60` at 40% | OPTIMAL (small parts) | Maximum efficiency; uniform heating |
| 0.060--0.125 in | `#27AE60` at 30% | OPTIMAL (large parts) | Standard production range |
| 0.125--0.250 in | `#E8A020` at 30% | ACCEPTABLE | Reduced efficiency; may need higher power |
| > 0.250 in | `#E05C5C` at 40% | TOO FAR | Severe efficiency loss; non-uniform heating |

Gauge: Rounded rect W: 10.0", H: 3.0". Segments stacked vertically.

**Right -- Efficiency relationship (X: 12.0", W: 11.5"):**

Callout box, H: 6.0", fill `#1E2435`, left accent 0.06" `#E8A020`.

Key facts (Inter Regular 14 pt, `#F0EDE8`, line height 160%):
```
Heating efficiency vs. coupling gap:

  0.040" gap --> ~90% efficiency
  0.080" gap --> ~75% efficiency
  0.125" gap --> ~60% efficiency
  0.250" gap --> ~35% efficiency

Efficiency drops as the SQUARE of the distance.
Doubling the gap = roughly 1/4 the efficiency.

PRACTICAL IMPLICATION:
A 0.010" change in gap causes a measurable
change in heating pattern. Fixture wear,
thermal expansion, and part dimensional
variation all affect the gap.

VERIFY GAP WITH FEELER GAUGES ON SETUP.
```

Data values: JetBrains Mono Regular 14 pt `#E8A020`. Body: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Rotation + Material Selection

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Rotation Requirements (X: 0.5", W: 11.0"):**

Section label: `PART ROTATION` Barlow Condensed ExtraBold 24 pt.

Table (Y: 23.0" to 28.0"):

| Application | Speed (RPM) | Reason |
|---|---|---|
| Shafts (general) | 60--120 | Circumferential uniformity |
| Shafts (precision) | 120--200 | Tighter pattern control |
| Gears (encircling coil) | 0 (stationary) | Coil surrounds entire tooth profile |
| Gears (tooth-by-tooth) | Indexed | Gear indexes one tooth at a time |
| Large cylinders | 30--60 | Slower for mass; uniform heat |

Bottom note: `Parts that do NOT rotate will have a "hot side" facing the coil and a "cold side" away from it. This creates non-uniform case depth -- sometimes acceptable, usually not.` Inter Medium 13 pt `#E8A020`

**Right -- Fixture Materials (X: 12.0", W: 11.5"):**

Section label: `NON-MAGNETIC MATERIALS ONLY` Barlow Condensed ExtraBold 24 pt `#E05C5C`.

- Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#E05C5C`

| Material | Use | Notes |
|---|---|---|
| 300-series stainless (304, 316) | Centers, chucks, fixtures | Austenitic = non-magnetic; standard choice |
| Brass / bronze | Centers, bushings | Excellent; non-magnetic; good wear |
| Ceramic | Insulating pads | For electrical isolation |
| UHMW / nylon | Guides, supports | Low-temp zones only (away from heat) |

Warning box: `NEVER use carbon steel, tool steel, or 400-series stainless for fixtures. They are ferromagnetic and WILL heat up in the induction field -- damaging the fixture and stealing power from the workpiece.` Inter Medium 13 pt `#E05C5C`

Additional note: `Wear check: Fixture wear changes the coupling gap. Inspect centers and chucks on a regular schedule. A worn center = inconsistent case depth.` Inter Regular 12 pt `#2EC4B6`

---

### ZONE 6 -- Footer

Standard footer. Title: `Fixturing -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; induction equipment manufacturer guidelines.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Fixturing Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The coupling distance gauge is the single most important visual on this poster. Operators need to internalize that the gap between coil and part is not "close enough" -- it is a precision dimension that directly controls heating efficiency. The inverse-square relationship is the key insight that makes this click. The non-magnetic materials callout is a common mistake that experienced operators know but new hires don't.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #616 -- Construction Workup v1.0*
*2026-04-26*
