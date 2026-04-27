---
Project: Plating Posters Inc
Poster Number: 291
Title: "Rinse (Pre-Anodize) -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2)"
Process Scope: Pre-anodize rinse for hardcoat anodizing -- Stage 5 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #291 -- Construction Workup
## Rinse (Pre-Anodize) -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The critical rinse. This is the last step before parts enter the near-freezing hardcoat anodize tank. Any acid drag-in from desmut raises dissolved aluminum and sulfate levels. Any fluoride drag-in from HF desmut causes catastrophic pitting at the extreme current densities used in hardcoat. The concept hook: "The anodize bath runs at 10--12% acid -- half the concentration of Type II. Every contaminant you drag in hits twice as hard."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Triple cascade rinse hero (Block B):** Three-tank cascade cross-section with conductivity monitoring at each stage.
2. **Contaminant impact panel (Block D):** What specific contaminants (acid, fluoride, chloride, organics) do to the hardcoat bath.
3. **Conductivity target visual (Block E):** Gauge-style visual showing pass/caution/fail thresholds.
4. **DI vs. city water comparison (Block F):** When DI water is required.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Teal)
ZONE 3 -- TRIPLE CASCADE RINSE HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- CONTAMINANT IMPACT ON HARDCOAT BATH (15.5"--22.0" / ~6.5")
ZONE 5 -- CONDUCTIVITY TARGETS + DI vs. CITY WATER (22.0"--28.5" / ~6.5")
ZONE 6 -- HARDCOAT-SPECIFIC RINSE RULES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stage 5 of 8 -- Pre-Anodize (CRITICAL)` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last line of defense before the anodize tank. Hardcoat runs at half the acid concentration of Type II -- every contaminant hits twice as hard.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Part carrying desmut acid residue  -->  After: Acid-free, contaminant-free surface entering anodize tank`

---

### ZONE 3 -- Triple Cascade Rinse Hero

**Section label:** `THE PRE-ANODIZE RINSE -- TRIPLE CASCADE FOR HARDCOAT` -- Y: 4.4".

**BLOCK B -- Three-Tank Cascade Cross-Section**

Y: 5.0" to 14.5".

Three rounded rects representing Stage 1 (dirty), Stage 2 (intermediate), Stage 3 (clean):
- Stage 1: X: 0.5", Y: 5.5", W: 7.0", H: 7.5", fill `#252B3D`, border 2 pt `#C8D0D8`
- Stage 2: X: 8.25", Y: 5.5", W: 7.0", H: 7.5", fill `#252B3D` at 85%, border 2 pt `#C8D0D8`
- Stage 3: X: 16.0", Y: 5.5", W: 7.5", H: 7.5", fill `#252B3D` at 70%, border 2 pt `#C8D0D8`

Labels above each tank:
- `STAGE 1 (DIRTY)` Barlow SemiBold 14 pt `#E05C5C`
- `STAGE 2 (INTERMEDIATE)` Barlow SemiBold 14 pt `#E8A020`
- `STAGE 3 (CLEAN)` Barlow SemiBold 14 pt `#27AE60`

Overflow arrows between tanks: 2 pt `#2EC4B6`
Fresh water arrow into Stage 3: 2 pt `#27AE60`, label `Fresh DI water in`
Drain arrow from Stage 1: 2 pt `#E05C5C`, label `To waste treatment`

Conductivity meters above each tank:
- Stage 1: `COND: variable` JetBrains Mono 11 pt `#E05C5C`
- Stage 2: `COND: <200 uS/cm` JetBrains Mono 11 pt `#E8A020`
- Stage 3: `COND: <50 uS/cm` JetBrains Mono 11 pt `#27AE60`

Parts (in Stage 2): 2 vertical rects, fill `#C8D0D8` at 40%

**Parameter summary (below tanks, Y: 13.5"):**

| Parameter | Value |
|---|---|
| **Type** | Triple cascade, counter-flow, DI water feed |
| **Temperature** | Ambient |
| **Time** | 60--120 sec total (move through all 3 stages) |
| **Final stage conductivity** | < 50 uS/cm for aerospace; < 100 uS/cm minimum |
| **Agitation** | Rack agitation in each tank |

JetBrains Mono 13 pt `#F0EDE8`.

---

### ZONE 4 -- Contaminant Impact on Hardcoat Bath

**Section label:** `WHAT DRAG-IN DOES TO THE HARDCOAT BATH` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 15.7".

**BLOCK D -- Four Contaminant Cards**

Y: 16.3" to 21.8". Four cards in 2x2 grid.

| Position | Contaminant | Color | Effect | Threshold |
|---|---|---|---|---|
| R1C1 | FLUORIDE (F-) | `#E05C5C` | Catastrophic pitting at high CD. Attacks barrier layer. Coating dissolves locally. | < 5 ppm |
| R1C2 | CHLORIDE (Cl-) | `#E05C5C` | Pitting corrosion of aluminum under oxide. Accelerated at near-freezing temp. | < 25 ppm |
| R2C1 | SULFATE / ACID | `#E8A020` | Raises acid concentration. Shifts dissolution/formation balance. Softens coating. | Monitor SG |
| R2C2 | ORGANICS | `#E8A020` | Causes foaming. Disrupts current distribution. Burning at foam contact points. | No visible foam |

Each card: Rounded rect W: 11.0", H: 2.5", fill `#1E2435`, radius 4, left accent 0.06" in contaminant color.

Interior: Contaminant name Barlow SemiBold 16 pt in color. Effect Inter Regular 12 pt `#F0EDE8`. Threshold JetBrains Mono 13 pt in color.

---

### ZONE 5 -- Conductivity Targets + DI vs. City Water

**Two-column layout (Y: 22.2" to 28.3"):**

**Left -- Conductivity Target Visual (X: 0.5", W: 11.0"):**

Section label: `CONDUCTIVITY TARGETS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Vertical gauge visual (tall rounded rect representing a conductivity scale):
- 0--50 uS/cm zone: fill `#27AE60` at 15%, label `AEROSPACE / CRITICAL` `#27AE60`
- 50--100 uS/cm zone: fill `#2EC4B6` at 15%, label `COMMERCIAL HARDCOAT` `#2EC4B6`
- 100--200 uS/cm zone: fill `#E8A020` at 15%, label `CAUTION -- MARGINAL` `#E8A020`
- >200 uS/cm zone: fill `#E05C5C` at 15%, label `FAIL -- DO NOT PROCEED` `#E05C5C`

Scale labels: JetBrains Mono 13 pt `#F0EDE8`.

**Right -- DI vs. City Water (X: 12.0", W: 11.5"):**

Section label: `DI WATER vs. CITY WATER` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Two stacked callout boxes:

DI Water (top):
- Fill `#1E2435`, left accent `#27AE60`
- Title: `DI WATER -- REQUIRED FOR HARDCOAT` Barlow SemiBold 16 pt `#27AE60`
- `Conductivity: 0.1--5 uS/cm` JetBrains Mono 13 pt `#F0EDE8`
- `Zero chlorides, zero fluorides, zero dissolved solids` Inter Regular 12 pt `#F0EDE8`
- `MANDATORY for final rinse stage` Inter Medium 13 pt `#27AE60`

City Water (bottom):
- Fill `#1E2435`, left accent `#E05C5C`
- Title: `CITY WATER -- RISK FOR HARDCOAT` Barlow SemiBold 16 pt `#E05C5C`
- `Conductivity: 100--500+ uS/cm` JetBrains Mono 13 pt `#F0EDE8`
- `Contains Cl- (10--50 ppm typical), dissolved solids, possible F-` Inter Regular 12 pt `#F0EDE8`
- `Acceptable for Stage 1 only; NEVER for final stage` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Hardcoat-Specific Rinse Rules

**Section label:** `TYPE III PRE-ANODIZE RINSE -- KEY RULES` Barlow Condensed ExtraBold 22 pt. Y: 28.7".

Four quick-hit cards in single row:

| Card | X | Rule | Detail |
|---|---|---|---|
| 1 | 0.5" | TRIPLE CASCADE | Three tanks minimum for hardcoat. Two is marginal. One is unacceptable. |
| 2 | 6.33" | DI WATER FINAL STAGE | Final rinse tank must be fed with DI water. City water = chloride contamination. |
| 3 | 12.16" | CONDUCTIVITY MONITOR | Check final stage conductivity every load. Log it. < 50 uS/cm for aerospace. |
| 4 | 18.0" | HF RINSE-OUT | If HF desmut was used, add an extra rinse. Fluoride is the #1 pitting contaminant for hardcoat. |

Each card: Rounded rect, W: 5.5", H: 3.5", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.

Rule: Barlow SemiBold 14 pt `#2EC4B6`. Detail: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Anodize) -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse water quality requirements vary by specification and facility. DI water system sizing and maintenance is facility-specific. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type III Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the more critical of the two rinse posters in the Type III cluster. The triple cascade hero and conductivity gauge are the visual anchors. The fluoride warning needs to be impossible to miss -- F- at high current density is the single most common cause of catastrophic pitting in hardcoat, and it comes from the previous step's HF desmut. The DI vs. city water comparison is practical shop-floor guidance that many smaller shops overlook.

---

*Alaina -- Plating Posters Inc*
*Poster #291 -- Construction Workup v1.0*
*2026-04-26*
