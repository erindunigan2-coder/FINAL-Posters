---
Project: Plating Posters Inc
Poster Number: 292
Title: "Hard Anodizing Main Tank -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2, Section 2.5)"
Process Scope: Hard anodize main tank -- Stage 6 of 8 (the core process)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - MainTank
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #292 -- Construction Workup
## Hard Anodizing Main Tank -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 6 of 8. This is the heart of the cluster -- the poster that every hardcoat operator will reference daily. Near-freezing H2SO4, current ramp protocol, voltage rise as oxide grows, chiller capacity, mixed-acid variant, alloy-specific thickness limits, and the defect table. Temperature control is THE variable. The concept hook: "Same electrolyte as the decorative anodize tank next door. Drop the temperature 40 degrees and double the current -- and you get a coating harder than mild steel."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Anodize tank cross-section hero (Block B):** Tank with chiller coils, cathodes, air agitation, power supply ramp indicator, temperature monitoring.
2. **Current ramp protocol visual (Block D):** Time vs. current/voltage chart showing ramp-up sequence.
3. **Film thickness vs. time table (Block E):** Growth rate at standard conditions.
4. **Mixed acid variant callout (Block F):** Alumilite 225/226 oxalic acid addition.
5. **Alloy thickness limits strip (Block G):** Critical -- alloy-specific maximum thickness before cracking.
6. **Defect diagnosis grid (Block H):** 6 main tank defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 18.5" / 22.5" / 27.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Amber -- anodize emphasis)
ZONE 3 -- ANODIZE TANK HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- CURRENT RAMP PROTOCOL (14.0"--18.5" / ~4.5")
ZONE 5 -- FILM THICKNESS TABLE + MIXED ACID (18.5"--22.5" / ~4.0")
ZONE 6 -- ALLOY THICKNESS LIMITS (22.5"--27.0" / ~4.5")
ZONE 7 -- DEFECT DIAGNOSIS GRID (27.0"--32.5" / ~5.5")
ZONE 8 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `HARD ANODIZING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stage 6 of 8 -- The Main Tank` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Near-freezing sulfuric acid. Double the current. A coating harder than mild steel. Temperature is EVERYTHING.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 6 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Smut-free, rinsed aluminum  -->  After: 25--100+ um dense aluminum oxide (400--600+ HV)`

---

### ZONE 3 -- Anodize Tank Hero

**Section label:** `THE HARDCOAT ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 13.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 6.5"
- Fill: `#252B3D` (electrolyte)
- Border: 3 pt `#C8D0D8`
- Label inside top: `H2SO4 ELECTROLYTE` Barlow SemiBold 14 pt `#F0EDE8` at 40%

**Parts on rack (center):**
- 3 vertical rects, X: 9.0"--15.0", Y: 6.5", H: 4.0"
- Fill: `#E8A020` at 20% (oxide growing), border 2 pt `#E8A020`
- Label: `ANODE (+)` Barlow SemiBold 14 pt `#E8A020`
- `PARTS` Inter Medium 12 pt `#F0EDE8`

**Cathodes (left and right of parts):**
- Vertical rects, X: 3.0" and 19.0", Y: 6.5", W: 0.5", H: 4.0"
- Fill: `#3A4055`, border 1 pt `#C8D0D8`
- Label: `CATHODE (-)` Barlow SemiBold 11 pt `#C8D0D8`
- Sublabel: `Lead or aluminum` Inter Regular 10 pt `#F0EDE8` at 60%

**Chiller coils (bottom of tank):**
- Zigzag/coil line, Y: 10.5", full tank width
- Stroke: 2 pt `#2EC4B6`
- Label: `Titanium cooling coils -- chiller 5--20 ton` Inter Regular 11 pt `#2EC4B6`

**Air agitation (very bottom):**
- Dashed horizontal line at Y: 11.5"
- Small circles (bubbles) rising
- Label: `Vigorous air agitation (heat removal)` Inter Regular 11 pt `#F0EDE8` at 60%

**Temperature indicator (left side, outside tank):**
- Rounded rect, W: 2.5", H: 1.0", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `28--36 F` JetBrains Mono 18 pt `#E05C5C`
- Sublabel: `(-2 to +2 C)` JetBrains Mono 12 pt `#F0EDE8` at 60%
- Below: `+/- 2 F tolerance` Inter Medium 11 pt `#E05C5C`

**Power supply indicator (right side, outside tank):**
- Rounded rect, W: 3.0", H: 1.5", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `24--36 ASF` JetBrains Mono 14 pt `#F0EDE8`
- `40--75+ V` JetBrains Mono 14 pt `#F0EDE8`
- `CURRENT RAMP` Inter Medium 11 pt `#E8A020`

**Bath parameter labels (below tank, Y: 12.5"):**

Centered parameter strip:
- `H2SO4: 110--135 g/L (10--12% w/v; 15--18 oz/gal)` JetBrains Mono 13 pt `#F0EDE8`
- `Temp: 28--36 F (-2 to +2 C) | CD: 24--36 ASF (ramp!) | V: 40--75+ V`
- `Time: 60--120 min for 2.0 mil | Dissolved Al: < 15 g/L`
- `Cathode: Pb or Al | Cathode:Anode ratio 1:1 to 2:1`

---

### ZONE 4 -- Current Ramp Protocol

**Section label:** `CURRENT RAMP PROTOCOL -- PREVENTS BURNING` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 14.2".

**BLOCK D -- Ramp Visual**

Y: 14.8" to 18.3".

**Two-column layout:**

**Left -- Ramp Sequence (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `STANDARD CURRENT RAMP` Barlow SemiBold 18 pt `#E8A020`

Step table:
| Time | Current Density | Voltage (typical) | Action |
|---|---|---|---|
| 0--2 min | 6--12 ASF | 15--25 V | Initial ramp -- gentle start |
| 2--5 min | 12--18 ASF | 25--35 V | Intermediate ramp |
| 5--15 min | 18--36 ASF | 35--50 V | Ramp to full CD |
| 15 min--end | 24--36 ASF (hold) | 50--75+ V (rising) | Hold at full CD; voltage rises as oxide thickens |

Header: Barlow SemiBold 11 pt `#F0EDE8` on `#3A4055`. Data: JetBrains Mono 12 pt.

Below: `Voltage rises continuously as oxide grows (increasing electrical resistance). Final voltage of 75--100+ V is normal for thick coatings.` Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- Why Ramp? (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`:

Title: `WHY RAMP? BECAUSE BURNING.` Barlow SemiBold 18 pt `#E05C5C`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `At process start, the aluminum surface has zero oxide.`
- `Full current (24--36 ASF) on bare aluminum = instant heat generation at the surface.`
- `Heat cannot dissipate fast enough through the thin initial oxide.`
- `Result: BURNING -- white powdery dissolved areas, especially at edges and high-current-density points.`
- ``
- `The ramp allows a thin oxide to form at low CD first.`
- `This initial oxide layer distributes current more evenly.`
- `Then current is gradually increased to full operating CD.`

Below content:
- `ALTERNATIVE: Some shops use VOLTAGE CONTROL instead of current control.` Inter Medium 12 pt `#E8A020`
- `Start at low voltage, ramp to operating voltage, let current find its level.` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Film Thickness Table + Mixed Acid Variant

**Two-column layout (Y: 18.7" to 22.3"):**

**Left -- Film Thickness vs. Time (X: 0.5", W: 11.0"):**

Section label: `FILM THICKNESS vs. TIME` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Target Thickness | um | Time at 30 ASF | Notes |
|---|---|---|---|
| 1.0 mil | 25 um | 30--45 min | Minimum per MIL-A-8625F |
| 2.0 mil | 50 um | 60--90 min | Default per spec if unspecified |
| 3.0 mil | 75 um | 90--135 min | Near alloy limits for 2024, 7075 |
| 4.0 mil | 100 um | 120--180 min | Maximum practical; 6061 only |

Header: Barlow SemiBold 11 pt. Data: JetBrains Mono 12 pt.
Below: `Growth rate slows as coating thickens (increasing resistance). Times are approximate.` Inter Regular 11 pt `#F0EDE8` at 60%.

**Right -- Mixed Acid Variant (X: 12.0", W: 11.5"):**

Section label: `MIXED ACID VARIANT` Barlow Condensed ExtraBold 20 pt `#E8A020`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `ALUMILITE 225/226 (OXALIC ACID ADDITION)` Barlow SemiBold 14 pt `#E8A020`

| Parameter | Value |
|---|---|
| H2SO4 | 12% (132 g/L) |
| Oxalic acid | 1% (40--45 g/L) |
| Temperature | 28--36 F (-2 to +2 C) |

JetBrains Mono 12 pt `#F0EDE8`.

Benefits:
- `Improved throwing power (more uniform in recesses)` Inter Regular 12 pt `#F0EDE8`
- `Reduced burning tendency` Inter Regular 12 pt `#27AE60`
- `Harder, more crack-resistant coating` Inter Regular 12 pt `#27AE60`
- `Originally developed by Alcoa` Inter Regular 11 pt `#F0EDE8` at 60%

---

### ZONE 6 -- Alloy Thickness Limits

**Section label:** `CRITICAL: ALLOY-SPECIFIC THICKNESS LIMITS` Barlow Condensed ExtraBold 24 pt `#E05C5C`. Y: 22.7".

**BLOCK G -- Alloy Limit Table**

Y: 23.3" to 26.8".

Full-width table with alloy color-coding:

| Alloy | Max Practical Thickness | Hardness (HV) | Hardcoat Rating | Notes |
|---|---|---|---|---|
| **6061** | 75--100+ um (3.0--4.0+ mil) | 500--600+ | EXCELLENT | Best alloy for hardcoat; uniform, predictable |
| **6063** | 75--100+ um (3.0--4.0+ mil) | 500--600+ | EXCELLENT | Same family; slightly softer substrate |
| **5052** | 50--75 um (2.0--3.0 mil) | 450--550 | GOOD | Slightly softer coating; good uniformity |
| **7075** | ~50 um (~2.0 mil) | 400--500 | FAIR | Zinc/copper cause brittleness; slow ramp required |
| **2024** | ~50 um (~2.0 mil) | 350--450 | DIFFICULT | High Cu = burning, soft spots; low CD and slow ramp |
| **Cast (A356, 380)** | NOT RECOMMENDED | -- | NOT RECOMMENDED | Silicon disrupts oxide growth catastrophically |

Header: Barlow SemiBold 11 pt `#F0EDE8` on `#3A4055`.
Data: Inter Regular 12 pt, alternating rows.
Rating column color-coded: EXCELLENT = `#27AE60`, GOOD = `#2EC4B6`, FAIR = `#E8A020`, DIFFICULT = `#E05C5C`, NOT RECOMMENDED = `#E05C5C`.

Below table:
- Rounded rect, full width, H: 0.8", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `EXCEEDING ALLOY LIMITS = CRACKING, SPALLING, DELAMINATION. These are not cosmetic defects -- they are structural failures.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 7 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 MAIN TANK DEFECTS` -- Y: 27.2".

**BLOCK H -- 3x2 Grid**

Y: 27.8" to 32.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BURNING (white/dissolved edges) | `#E05C5C` | CD too high; no ramp; sharp geometry; poor contact | Use ramp protocol; radius edges; check racking |
| R1C2 | CRACKING / SPALLING | `#E05C5C` | Thickness exceeds alloy limit; thermal stress | Stay within alloy limits; slow post-process cooling |
| R1C3 | POWDERY / SOFT COATING | `#E05C5C` | Temperature > 40 F; acid too concentrated | STOP -- check chiller; lower acid concentration |
| R2C1 | NON-UNIFORM THICKNESS | `#E8A020` | Poor agitation; heat buildup zones; racking | Increase agitation; add conforming cathodes |
| R2C2 | DELAMINATION | `#E8A020` | Poor adhesion (smut, contamination) | Improve cleaning/desmut; verify surface prep |
| R2C3 | PITTING | `#E05C5C` | Fluoride or chloride contamination | Analyze bath; improve pre-anodize rinse; check DI |

Each card: Rounded rect W: 7.33", H: 2.0", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 8 -- Footer

Standard. Title: `Hard Anodizing Main Tank -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values for MIL-A-8625F Type III hardcoat anodizing. Alloy-specific limits, mixed-acid variants, and ramp protocols vary by facility. Consult your process supplier, metallurgist, and applicable specification. Source: MIL-A-8625F; AMS 2469; ASM Handbook Vol. 5.`

---

## Parts 5--7

**Grouping:** 8 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Hard Anodizing Main Tank Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the hardcoat cluster -- the one that will hang next to the anodize tank. Every parameter must be readable at 6 feet. The current ramp protocol is the most actionable element: operators need to see the step table at a glance during setup. The alloy thickness limits strip must be impossible to miss -- cracking a $5,000 aerospace part because someone ran 2024 to 75 um is not a theoretical risk, it is a Tuesday. The temperature callout should be the largest single number on the poster. The mixed-acid variant is a secondary callout for shops using the Alumilite process.

---

*Alaina -- Plating Posters Inc*
*Poster #292 -- Construction Workup v1.0*
*2026-04-26*
