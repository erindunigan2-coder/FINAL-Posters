---
Project: Plating Posters Inc
Poster Number: 308
Title: "BSAA Anodizing Main Tank -- Boric-Sulfuric Acid Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4, Section 4.5)"
Process Scope: BSAA anodize main tank -- Stage 6 of 8 (the core process)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - MainTank
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #308 -- Construction Workup
## BSAA Anodizing Main Tank -- Boric-Sulfuric Acid Anodizing

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 6 of 8. This is the heart of the BSAA cluster. The electrolyte is dilute H2SO4 (30--50 g/L) plus boric acid (5--10 g/L). Operating voltage ramps to ~15V -- lower than Type I's 40V and much lower than Type II's 15--21V at higher acid concentration. The boric acid acts as a buffering agent that moderates the aggressiveness of sulfuric acid dissolution, allowing a thin, dense oxide to form without the Cr(VI). The concept hook: "Boric acid doesn't become part of the oxide. It controls how the oxide forms. The buffer that replaces the carcinogen."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Anodize tank cross-section hero (Block B):** Tank with cathodes, power supply, temperature control.
2. **Role of boric acid panel (Block D):** How H3BO3 buffers the electrolyte and why it works.
3. **Coating weight vs. time (Block E):** Growth rate at standard conditions.
4. **BSAA vs. Type I chemistry comparison (Block F):** Side-by-side electrolyte differences.
5. **Dissolved aluminum monitoring (Block G):** Tighter control needed.
6. **Defect diagnosis grid (Block H).**

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
  Stage 6 highlighted (Emerald)
ZONE 3 -- ANODIZE TANK HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- ROLE OF BORIC ACID (14.0"--18.5" / ~4.5")
ZONE 5 -- COATING WEIGHT + CHEMISTRY COMPARISON (18.5"--22.5" / ~4.0")
ZONE 6 -- DISSOLVED Al MONITORING + ALLOY NOTES (22.5"--27.0" / ~4.5")
ZONE 7 -- DEFECT DIAGNOSIS GRID (27.0"--32.5" / ~5.5")
ZONE 8 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `BSAA ANODIZING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing -- Stage 6 of 8 -- The Main Tank` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Dilute sulfuric. A pinch of boric acid. 15 volts maximum. A thin oxide that replaces chromic acid -- without the carcinogen.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.

Below: `Before: Smut-free, rinsed aluminum  -->  After: Thin, dense oxide (200--700 mg/ft2) -- paint adhesion base`

---

### ZONE 3 -- Anodize Tank Hero

**Section label:** `THE BSAA ANODIZE TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 13.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 6.5"
- Fill: `#252B3D`
- Border: 3 pt `#C8D0D8`
- Label inside top: `H2SO4 + H3BO3 ELECTROLYTE` Barlow SemiBold 14 pt `#F0EDE8` at 40%

**Parts on rack (center):**
- 3 vertical rects, X: 9.0"--15.0", Y: 6.5", H: 4.0"
- Fill: `#27AE60` at 20% (oxide growing), border 2 pt `#27AE60`
- Label: `ANODE (+)` Barlow SemiBold 14 pt `#27AE60`

**Cathodes (left and right):**
- Vertical rects, X: 3.0" and 19.0"
- Fill: `#3A4055`, border 1 pt `#C8D0D8`
- Label: `CATHODE (-)` Barlow SemiBold 11 pt `#C8D0D8`

**Air agitation (bottom):**
- Dashed line with bubbles
- Label: `Air agitation (mild)` Inter Regular 11 pt `#F0EDE8` at 60%

**Temperature indicator (left side):**
- Rounded rect, W: 2.5", H: 0.8", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `70--90 F` JetBrains Mono 16 pt `#2EC4B6`
- Sublabel: `(21--32 C)` JetBrains Mono 11 pt `#F0EDE8` at 60%

**Power supply indicator (right side):**
- Rounded rect, W: 3.0", H: 1.2", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `RECTIFIER` Barlow SemiBold 12 pt `#27AE60`
- `Ramp to ~15 V` JetBrains Mono 14 pt `#F0EDE8`
- `Max ~10 ASF avg` JetBrains Mono 13 pt `#F0EDE8`

**Bath parameter labels (below tank, Y: 12.5"):**

Centered parameter strip:
- `H2SO4: 30--50 g/L (3--5% w/v)` JetBrains Mono 13 pt `#F0EDE8`
- `H3BO3: 5--10 g/L (0.5--1% w/v)` JetBrains Mono 13 pt `#E8A020`
- `Temp: 70--90 F (21--32 C) | Voltage: ramp from ~5V to 15V`
- `CD: max ~10 ASF average (voltage-controlled)`
- `Time: 20--30 min | Coating weight: 200--700 mg/ft2`

---

### ZONE 4 -- Role of Boric Acid

**Section label:** `THE ROLE OF BORIC ACID -- THE KEY INGREDIENT` Barlow Condensed ExtraBold 24 pt `#E8A020`. Y: 14.2".

**BLOCK D -- Two-Column Explanation**

Y: 14.8" to 18.3".

**Left -- What Boric Acid Does (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `H3BO3 -- THE BUFFER` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Boric acid acts as a pH buffer in the electrolyte.`
- `It reduces the aggressiveness of sulfuric acid's attack on the growing oxide.`
- `Without boric acid, 3--5% H2SO4 alone would produce a thin, aggressive dissolution front.`
- `WITH boric acid, the dissolution/formation balance shifts -- more formation, less dissolution.`
- `Result: a thin, dense oxide similar to chromic acid anodize.`
- ``
- `CRITICAL POINT:` Inter Medium 13 pt `#E8A020`
- `Boric acid does NOT incorporate into the oxide film.`
- `It modifies the electrolyte behavior only.`
- `The oxide is still pure aluminum oxide (Al2O3).`

**Right -- What Happens Without It (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`:

Title: `WITHOUT H3BO3` Barlow SemiBold 18 pt `#E05C5C`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `3--5% H2SO4 alone at room temperature:`
- `-- Too aggressive dissolution for thin oxide target`
- `-- Inconsistent coating weight`
- `-- Poor paint adhesion`
- `-- Essentially a very dilute Type II bath that can't build a useful oxide`
- ``
- `The boric acid is what makes BSAA a different process from dilute sulfuric acid anodizing. Remove it and you lose the performance equivalence to Type I.`

---

### ZONE 5 -- Coating Weight + Chemistry Comparison

**Two-column layout (Y: 18.7" to 22.3"):**

**Left -- Coating Weight (X: 0.5", W: 11.0"):**

Section label: `COATING WEIGHT -- THE METRIC FOR BSAA` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:

Content:
- `BSAA coating is measured by WEIGHT (mg/ft2), not thickness.` Inter Medium 13 pt `#E8A020`
- `This is because the coating is so thin that eddy current thickness gauges may lack resolution.`
- ``
- `MIL-A-8625F Type IC:` Inter Medium 13 pt `#27AE60`
- `Minimum: 200 mg/ft2` JetBrains Mono 14 pt `#F0EDE8`
- `Maximum: 700 mg/ft2` JetBrains Mono 14 pt `#F0EDE8`
- `Typical: 300--500 mg/ft2` JetBrains Mono 14 pt `#E8A020`
- ``
- `Measurement: Weigh part before and after anodize (coupon method) or use calibrated thickness gauge with thin-film capability.`
- ``
- `Approximate thickness equivalent: 200--700 mg/ft2 ~ 0.2--2.0 um` Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- Chemistry Comparison (X: 12.0", W: 11.5"):**

Section label: `BSAA vs. TYPE I CHEMISTRY` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Parameter | Type I (Chromic) | BSAA (Type IC) |
|---|---|---|
| Electrolyte | CrO3 50 g/L | H2SO4 30--50 g/L + H3BO3 5--10 g/L |
| Temperature | 90--100 F | 70--90 F |
| Voltage | 40V (ramp cycle) | ~15V (ramp) |
| CD | 5--10 ASF | Max ~10 ASF |
| Coating weight | ~200--700 mg/ft2 | 200--700 mg/ft2 |
| Cr(VI) | YES | NO |
| Cost (chemicals) | HIGH (CrO3 + waste) | LOW (H2SO4 + H3BO3) |
| Waste category | D007 hazardous | Standard acid waste |

Header: Barlow SemiBold 11 pt. Data: JetBrains Mono 11 pt.
Cr(VI) row: YES in `#E05C5C`, NO in `#27AE60`.

---

### ZONE 6 -- Dissolved Al Monitoring + Alloy Notes

**Two-column layout (Y: 22.7" to 26.8"):**

**Left -- Dissolved Aluminum (X: 0.5", W: 11.0"):**

Section label: `DISSOLVED ALUMINUM -- MONITOR CLOSELY` Barlow Condensed ExtraBold 20 pt `#E8A020`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Content:
- `As parts are anodized, aluminum dissolves into the electrolyte.` Inter Regular 13 pt `#F0EDE8`
- `In Type II (15--20% acid), the bath absorbs 20+ g/L dissolved Al before performance degrades.`
- `In BSAA (3--5% acid), the tolerance is LOWER -- the dilute bath saturates faster.`
- ``
- `MONITORING:` Inter Medium 13 pt `#E8A020`
- `-- Analyze dissolved Al by titration or ICP` JetBrains Mono 12 pt `#F0EDE8`
- `-- Track specific gravity as a daily proxy` JetBrains Mono 12 pt `#F0EDE8`
- `-- Establish shop-specific limits (no universal standard)` JetBrains Mono 12 pt `#F0EDE8`
- `-- Decant/replenish when Al exceeds internal limit` Inter Regular 12 pt `#F0EDE8`

**Right -- Alloy Compatibility (X: 12.0", W: 11.5"):**

Section label: `ALLOY COMPATIBILITY` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Alloy | BSAA Rating | Notes |
|---|---|---|
| **2024** | GOOD | BSAA preferred over Type II for 2xxx (same advantage as Type I) |
| **7075** | GOOD | Works well; thin oxide minimizes alloy sensitivity |
| **6061** | GOOD | Standard substrate |
| **5052** | GOOD | No issues |
| **1100** | GOOD | Excellent |
| **Cast** | VARIABLE | Same limitations as any anodize process on high-Si alloys |

Header: Barlow SemiBold 11 pt. Data: Inter Regular 12 pt.
GOOD highlighted in `#27AE60`.

Below: `BSAA works well on 2xxx and 7xxx alloys -- the same alloys that make Type I the preferred process over Type II. This is not a coincidence; BSAA was designed to match Type I's alloy compatibility.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 7 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 MAIN TANK DEFECTS` -- Y: 27.2".

**BLOCK H -- 3x2 Grid**

Y: 27.8" to 32.3".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | THIN / NO COATING | `#E05C5C` | H2SO4 or H3BO3 low; dissolved Al too high | Analyze bath; replenish acids; decant if needed |
| R1C2 | POOR PAINT ADHESION | `#E05C5C` | Oxide too thin; pre-treatment contamination | Increase time; improve cleaning/desmut |
| R1C3 | NON-UNIFORM COATING WEIGHT | `#E8A020` | Poor racking; non-uniform current distribution | Improve racking; verify voltage profile |
| R2C1 | LOW CORROSION RESISTANCE | `#E8A020` | Incomplete seal; thin oxide | Verify seal quality (dye spot); increase coating weight |
| R2C2 | DISCOLORATION | `#2EC4B6` | Alloy variation; dissolved Al too high | Verify alloy; check bath chemistry |
| R2C3 | COATING FLAKING | `#E05C5C` | Poor adhesion from contamination or excessive oxide | Improve pre-treatment; reduce anodize time |

Each card: Rounded rect W: 7.33", H: 2.0", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 8 -- Footer

Standard. Title: `BSAA Anodizing Main Tank -- Boric-Sulfuric Acid Anodizing`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for MIL-A-8625F Type IC per Boeing BAC 5632. Bath chemistry, voltage profiles, and coating weight specifications vary by facility. BSAA is a newer process with less established operating history than Type I or Type II -- maintain detailed records. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 8 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `BSAA Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the flagship poster of the BSAA cluster -- and possibly the most educational single poster in the anodizing series. Most platers have never run BSAA. They understand sulfuric acid anodizing. They understand (or fear) chromic acid anodizing. BSAA is the new thing, and this poster needs to demystify it. The boric acid explanation (Zone 4) is the conceptual core: "It doesn't become part of the oxide. It controls how the oxide forms." That single insight makes the entire process click. The chemistry comparison table (Zone 5) closes the sale: same performance, lower voltage, lower temperature, zero Cr(VI), standard waste.

---

*Alaina -- Plating Posters Inc*
*Poster #308 -- Construction Workup v1.0*
*2026-04-26*
