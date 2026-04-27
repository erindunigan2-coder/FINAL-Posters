---
Project: Plating Posters Inc
Poster Number: 523
Title: "Masking & Fixturing -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Masking and fixturing requirements for cold spray. High particle velocity erodes soft masking -- metal masks mandatory. Focused spray footprint (5--15 mm) demands precise masking.
Process Scope: Cold spray -- masking and fixturing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - Masking
  - Fixturing
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #523 -- Construction Workup
## Masking & Fixturing -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Masking and fixturing poster for Cold Spray. Key differentiators: adhesive tape is NOT reliable (particles erode it), metal masks are mandatory, the spray footprint is extremely focused (5--15 mm), and substrate cooling is generally NOT needed (major advantage over all other thermal spray).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Masking materials comparison (Block B -- HERO):** Table comparing masking options with pass/fail indicators for cold spray compatibility.
2. **"Tape Won't Work" warning callout (Block C):** Coral-tinted callout -- the single most important masking message.
3. **Fixturing requirements (Block D):** Robot manipulation, precision standoff, no cooling needed.
4. **Spray footprint diagram (Block E):** Visual showing the 5--15 mm focused spray pattern.
5. **Application-specific masking cards (Block F):** Cards for repair, additive buildup, and coating applications.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- MASKING MATERIALS + WARNING (2.9"--15.0" / ~12.1")
  Block B: Masking materials table
  Block C: "Tape Won't Work" warning callout
ZONE 3 -- FIXTURING + SPRAY FOOTPRINT (15.0"--25.0" / ~10.0")
  Block D: Fixturing requirements
  Block E: Spray footprint diagram
ZONE 4 -- APPLICATION-SPECIFIC MASKING (25.0"--32.5" / ~7.5")
  Block F: 3 application cards
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `MASKING & FIXTURING` -- 80 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Precision Masking for Supersonic Particles` -- 32 pt `#C8D0D8` (Silver). Y: 1.5".
**Tagline:** `Adhesive tape cannot survive 600+ m/s particle impact. Metal masks are not optional -- they are the only option.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Masking Materials + Warning

**Section label:** `MASKING MATERIAL SELECTION` -- Y: 3.1".

**BLOCK B -- Masking Materials Table (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 12.0".

Header row: `#3A4055`. Columns: Material (3.5") | Suitability (2.0") | Reason (4.5") | Applications (4.5")

| Material | Suitability | Reason | Applications |
|---|---|---|---|
| Aluminum sheet masks | RECOMMENDED | Lightweight; easy to machine; good for Al-on-Al spray | Aerospace repair; Al coating |
| Stainless steel masks | RECOMMENDED | Durable; reusable; withstands high particle energy | Production runs; all materials |
| Custom-machined Inconel | BEST (for production) | Maximum durability; withstands thousands of cycles | High-volume coating |
| Silicone plugs/caps | ACCEPTABLE (sheltered) | OK for holes/bores where not in direct spray path | Thread protection; bore masking |
| Adhesive tape (any type) | NOT RELIABLE | Particles erode and penetrate tape at cold spray velocities | DO NOT USE in spray path |
| High-temp masking tape | NOT RELIABLE | Same erosion problem -- velocity, not temperature, is the issue | DO NOT USE in spray path |

Suitability column: `RECOMMENDED` in `#27AE60`; `BEST` in `#2EC4B6`; `ACCEPTABLE` in `#E8A020`; `NOT RELIABLE` in `#E05C5C`.

**BLOCK C -- "Tape Won't Work" Warning (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 9.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E05C5C`.
Coral-tinted glass treatment.

Title: `TAPE WILL FAIL` Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

Body (Inter Regular, 15 pt, `#F0EDE8`, line height 165%):
```
In every other thermal spray
process, adhesive tape is a
standard masking material.

NOT in cold spray.

Particles at 600--1200 m/s erode
and penetrate adhesive tape --
regardless of type, temperature
rating, or thickness.

Metal masks are MANDATORY for
any surface in the direct spray
path.
```

Bottom callout: `This is a velocity problem, not a temperature problem.` Inter Medium, 14 pt, `#E05C5C`.

**No-Cooling Advantage callout (below warning, Y: 9.5" to 12.0"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Title: `NO COOLING NEEDED` Barlow SemiBold, 18 pt, `#27AE60`.
Body: `Unlike plasma, HVOF, and flame spray, cold spray does not require cooling air directed at the substrate or fixture. Substrate temperature stays well below damage thresholds. This simplifies fixturing dramatically.` Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 3 -- Fixturing + Spray Footprint

**Two-column layout:**

**Left -- Fixturing Requirements (X: 0.5", W: 11.0"):**

Section label: `FIXTURING REQUIREMENTS` Y: 15.2".

Five requirement cards stacked:

| Requirement | Detail |
|---|---|
| Robot manipulation | 6-axis robot ESSENTIAL -- precise standoff and traverse control |
| Standoff distance | 10--50 mm (MUCH closer than other thermal spray) |
| Traverse speed | 100--500 mm/s -- robot-controlled for uniformity |
| Part rotation | For cylindrical parts; robot coordinates with rotation |
| No cooling air | Substrate stays cool -- NO cooling fixtures needed |

Each card: H: 1.5", fill `#1E2435`, left accent `#2EC4B6`.
Requirement: Barlow SemiBold, 14 pt, `#2EC4B6`.
Detail: Inter Regular, 13 pt, `#F0EDE8`.

**Right -- Spray Footprint Diagram (X: 12.0", W: 11.5"):**

Section label: `SPRAY FOOTPRINT` Y: 15.2".

**BLOCK E -- Footprint Visual**

Y: 16.0" to 24.5". Rounded rect, fill `#1E2435`, radius 8.

Central diagram:
- Circle representing spray spot: 5--15 mm diameter
- Label: `5--15 mm` JetBrains Mono, 24 pt, `#E8A020`
- Subtitle: `Spray footprint diameter (nozzle-dependent)` Inter Regular, 13 pt, `#F0EDE8` at 60%

Comparison callout:
- `Cold Spray: 5--15 mm (focused)` `#2EC4B6`
- `Plasma Spray: 15--40 mm (broad)` `#3A4055`
- `HVOF: 10--25 mm (moderate)` `#3A4055`
- `Arc Spray: 25--75 mm (wide)` `#3A4055`

Note: `The focused footprint enables precise repair and additive buildup -- but demands precise masking to define spray boundaries.` Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 4 -- Application-Specific Masking

**Section label:** `MASKING BY APPLICATION` -- Y: 25.2".

**BLOCK F -- 3 Application Cards**

Y: 25.8" to 32.3". Three cards in a row. W: 7.33" each, H: 4.0".

| Card | Application | Masking Approach | Key Note |
|---|---|---|---|
| 1 | DIMENSIONAL REPAIR (Aerospace) | Custom aluminum mask defining repair zone precisely; build up flush with surrounding surface | Mask defines the boundary between new deposit and original material |
| 2 | ADDITIVE BUILDUP (Manufacturing) | Stainless steel fixture with cutout exposing deposition area only | Part must be fixtured to maintain exact standoff during multi-mm buildup |
| 3 | FULL-SURFACE COATING | Masks protect threads, holes, bearing surfaces, and mating faces only | Simpler masking than repair -- fewer boundaries to define |

Application: Barlow SemiBold, 16 pt, `#E8A020`.
Approach: Inter Regular, 13 pt, `#F0EDE8`.
Key Note: Inter Medium, 12 pt, `#2EC4B6`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Masking & Fixturing -- Cold Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Masking Fixturing Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Two hero messages: (1) tape fails at cold spray velocities, and (2) no substrate cooling is needed. The focused footprint diagram provides an excellent visual differentiator from other thermal spray processes. The "velocity problem, not temperature problem" line is the key insight that experienced thermal spray operators need to internalize.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #523 -- Construction Workup v1.0*
*2026-04-26*
