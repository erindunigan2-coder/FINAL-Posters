---
Project: Plating Posters Inc
Poster Number: 290
Title: "Etch / Desmut -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2, Sections 2.3--2.4)"
Process Scope: Caustic etch and acid desmut for hardcoat anodizing -- Stages 3--4 of 8 (combined)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Etch
  - Desmut
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #290 -- Construction Workup
## Etch / Desmut -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stages 3--4 of 8 (combined). This poster covers both etch and desmut because hardcoat etching is fundamentally different from Type II: it is short (30--90 sec), light, and often SKIPPED entirely for precision parts. The desmut step, however, is always performed and is even more critical than for Type II because trapped smut under a 50--100 um hard oxide causes delamination under stress. The concept hook: "Etch is optional. Desmut is never optional."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-tank hero (Block B):** Side-by-side etch tank and desmut tank cross-sections with a decision diamond between them showing the "etch or skip?" decision tree.
2. **Dimensional impact callout (Block D):** Shows material removal vs. oxide buildup math.
3. **Smut character by alloy table (Block E):** Alloy-specific smut composition and recommended desmut chemistry.
4. **Defect grid (Block F):** 4 etch/desmut failure modes.

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
  Stages 3 and 4 highlighted (Amber)
ZONE 3 -- ETCH + DESMUT DUAL-TANK HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- DIMENSIONAL IMPACT + DECISION TREE (15.5"--22.0" / ~6.5")
ZONE 5 -- SMUT CHARACTER BY ALLOY (22.0"--28.5" / ~6.5")
ZONE 6 -- DEFECT GRID (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ETCH / DESMUT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stages 3 & 4 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Etch is optional for precision parts. Desmut is NEVER optional. Trapped smut under 50 um of hard oxide means delamination.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stages 3 and 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean surface (may have native oxide and mill finish)  -->  After: Smut-free, activated aluminum ready for anodize`

---

### ZONE 3 -- Etch + Desmut Dual-Tank Hero

**Section label:** `TWO TANKS, ONE GOAL: A SMUT-FREE ACTIVATED SURFACE` -- Y: 4.4".

**Left -- Etch Tank (X: 0.5", Y: 5.0", W: 10.5", H: 9.5"):**

Tank body:
- Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`
- Title above: `CAUSTIC ETCH` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `(LIGHT OR SKIP)` Barlow SemiBold 14 pt `#E8A020` at 60%

Parameter labels inside/adjacent:
- `NaOH 30--45 g/L (4--6 oz/gal)` JetBrains Mono 14 pt `#F0EDE8`
- `130--150 F (55--66 C)` JetBrains Mono 14 pt `#E8A020`
- `30--90 sec (SHORTER than Type II)` JetBrains Mono 13 pt `#F0EDE8`
- `Etch rate: ~0.5--1.0 mil/min per surface` JetBrains Mono 12 pt `#F0EDE8` at 70%

Decision callout (bottom of etch tank area, Y: 12.5"):
- Rounded rect, W: 10.0", H: 1.5", fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Title: `ETCH OR SKIP?` Barlow SemiBold 14 pt `#E8A020`
- `Precision parts (tight tolerance): SKIP etch -- go directly to desmut` Inter Medium 12 pt `#F0EDE8`
- `General parts (cosmetic or non-critical): LIGHT etch 30--90 sec` Inter Medium 12 pt `#F0EDE8`
- `Some specs PROHIBIT caustic etch for hardcoat` Inter Medium 12 pt `#E05C5C`

**Right -- Desmut Tank (X: 12.0", Y: 5.0", W: 11.5", H: 9.5"):**

Tank body:
- Rounded rect, fill `#252B3D`, border 2 pt `#C8D0D8`
- Title above: `DESMUT / DEOXIDIZE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `(ALWAYS REQUIRED)` Barlow SemiBold 14 pt `#27AE60`

Parameter labels:
- `Standard: HNO3 25--50% v/v` JetBrains Mono 14 pt `#F0EDE8`
- `Cu alloys: HNO3 + HF 1--3%` JetBrains Mono 14 pt `#E8A020`
- `Ambient temp (60--85 F)` JetBrains Mono 13 pt `#F0EDE8`
- `15--60 sec (straight HNO3)` JetBrains Mono 13 pt `#F0EDE8`
- `2--10 min (ferric sulfate type)` JetBrains Mono 12 pt `#F0EDE8` at 70%

Critical callout (bottom of desmut area, Y: 12.5"):
- Rounded rect, W: 11.0", H: 1.5", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Title: `DESMUT IS NON-NEGOTIABLE` Barlow SemiBold 14 pt `#E05C5C`
- `Trapped smut under hard coat = delamination under mechanical stress` Inter Medium 12 pt `#F0EDE8`
- `HF handling: calcium gluconate gel at station -- HF burns are medical emergencies` Inter Medium 12 pt `#E05C5C`

---

### ZONE 4 -- Dimensional Impact + Etch Decision Tree

**Two-column layout (Y: 15.7" to 21.8"):**

**Left -- Dimensional Impact (X: 0.5", W: 11.0"):**

Section label: `DIMENSIONAL MATH -- ETCH vs. ANODIZE` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Content (Inter Regular 13 pt `#F0EDE8`, line height 160%):

```
ETCH REMOVES aluminum:
  60 sec at 140 F = ~0.5--1.0 mil removed per surface

ANODIZE ADDS oxide:
  2.0 mil coating = ~1.0 mil outward growth per surface
  (50% inward into aluminum, 50% outward above surface)

NET DIMENSIONAL CHANGE per surface:
  Etched part: -0.5 to -1.0 mil (etch) + 1.0 mil (anodize outward) = 0 to +0.5 mil
  Non-etched part: +1.0 mil (anodize outward only)

FOR PRECISION PARTS:
  Skip etch. Calculate final dimension as:
  Original + (coating thickness / 2)
```

JetBrains Mono 12 pt `#F0EDE8` for calculations. Labels in Inter Medium 13 pt `#E8A020`.

**Right -- Etch Decision Tree (X: 12.0", W: 11.5"):**

Section label: `WHEN TO ETCH -- DECISION GUIDE` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Decision flow (vertical, using rounded rects with connecting arrows):

Diamond 1: `Dimensional tolerance +/- 0.5 mil or tighter?`
- YES --> `SKIP ETCH -- desmut only` (Emerald `#27AE60`)
- NO --> Diamond 2

Diamond 2: `Cosmetic appearance required?`
- YES --> `LIGHT ETCH -- 30--60 sec` (Amber `#E8A020`)
- NO --> `LIGHT ETCH -- 30--90 sec or SKIP` (Teal `#2EC4B6`)

Below: `Customer spec overrides this guide. Some aerospace primes prohibit caustic etch for hardcoat entirely.` Inter Medium 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Smut Character by Alloy

**Section label:** `ALLOY SMUT TABLE -- WHAT CAUSTIC ETCH LEAVES BEHIND` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 22.2".

**BLOCK E -- Smut Table**

Y: 22.8" to 28.3".

| Alloy | Smut Character | Color | Recommended Desmut | Notes |
|---|---|---|---|---|
| **6061** | Light gray, easy to remove | Light | Straight HNO3 50% | Best hardcoat alloy -- minimal smut issues |
| **6063** | Light gray, easy to remove | Light | Straight HNO3 50% | Excellent hardcoat response |
| **5052** | Light gray | Light | Straight HNO3 50% | Good hardcoat; slightly softer oxide |
| **2024** | Heavy dark copper-rich | Heavy | HNO3 + HF 1--3% | Difficult to hardcoat -- max ~50 um before cracking |
| **7075** | Moderate copper/zinc | Moderate | HNO3 + HF preferred | Fair hardcoat -- requires slow current ramp |
| **Cast (A356, 380)** | Heavy black silicon-rich | Very heavy | HNO3 + HF, extended time | NOT RECOMMENDED for hardcoat |

Header: Barlow SemiBold 12 pt `#F0EDE8` on `#3A4055`. Data: Inter Regular 12 pt, alternating `#1E2435` / `#252B3D`.

Smut character column: color-coded text -- Light = `#27AE60`, Moderate = `#E8A020`, Heavy = `#E05C5C`, Very heavy = `#E05C5C`.

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 4 ETCH/DESMUT FAILURES` -- Y: 28.7".

**BLOCK F -- 4-Card Strip**

Y: 29.3" to 32.3".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | DELAMINATION | Smut trapped under oxide | Verify desmut completeness; use HF for Cu/Si alloys |
| 2 | 6.33" | OVER-ETCH (dimensional) | Etch too long on precision parts | Reduce time to 30 sec or skip entirely |
| 3 | 12.16" | NON-UNIFORM COATING | Uneven etch = uneven oxide growth | Improve agitation; verify etch concentration |
| 4 | 18.0" | BURNING AT THIN SPOTS | Etch removed too much material at edges | Mask edges; reduce etch time; skip etch |

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Interior: Problem in Barlow SemiBold 16 pt `#E05C5C`. Cause in Inter Regular 13 pt `#F0EDE8`. Fix in Inter Medium 13 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Etch / Desmut -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values. Etch and desmut procedures vary by alloy, specification, and dimensional requirements. HF is extremely hazardous -- follow all OSHA requirements. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Desmut Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Combining etch and desmut into one poster is unique to the hardcoat cluster because the etch step is so often abbreviated or skipped. The etch decision tree is the most actionable element -- a shop operator can follow the two-diamond flow to determine whether to etch their part in 10 seconds. The dimensional math callout is critical for shops doing precision hardcoat -- they need to calculate net dimensional change accounting for both material removal (etch) and material addition (oxide growth). The smut table is carried over from the Type II cluster but with hardcoat-specific alloy notes emphasizing thickness limits.

---

*Alaina -- Plating Posters Inc*
*Poster #290 -- Construction Workup v1.0*
*2026-04-26*
