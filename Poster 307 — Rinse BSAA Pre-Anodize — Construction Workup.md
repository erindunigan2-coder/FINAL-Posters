---
Project: Plating Posters Inc
Poster Number: 307
Title: "Rinse (Pre-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4)"
Process Scope: Pre-anodize rinse for BSAA -- Stage 5 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #307 -- Construction Workup
## Rinse (Pre-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The critical rinse before the BSAA anodize tank. BSAA is the most contamination-sensitive anodize bath in common use: 3--5% H2SO4 + 0.5--1% H3BO3. Any acid drag-in from desmut shifts the sulfuric/boric acid ratio. Any alkaline drag-through neutralizes the dilute acid. The dissolved aluminum tolerance is tighter than Type II because the lower acid concentration provides less buffer capacity. The concept hook: "The thinnest margin in anodizing. 3% acid. 1% boric. Every drop of drag-in changes the balance."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse hero (Block B):** Dual or triple cascade.
2. **Bath sensitivity panel (Block D):** Why BSAA is more sensitive to drag-in than any other anodize bath.
3. **Conductivity targets (Block E).**
4. **DI water requirement (Block F).**

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
ZONE 3 -- CASCADE RINSE HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- BATH SENSITIVITY (15.5"--22.0" / ~6.5")
ZONE 5 -- CONDUCTIVITY TARGETS + DI WATER (22.0"--28.5" / ~6.5")
ZONE 6 -- KEY RULES STRIP (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing (BSAA) -- Stage 5 of 8 -- Pre-Anodize (CRITICAL)` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The thinnest margin in anodizing. 3% acid, 1% boric. Every drop of contamination changes the H2SO4/H3BO3 balance.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Part carrying desmut acid residue  -->  After: Clean, contaminant-free surface entering BSAA tank`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `THE PRE-ANODIZE RINSE -- CRITICAL FOR BSAA` -- Y: 4.4".

**BLOCK B -- Dual/Triple Cascade Cross-Section**

Same construction as Poster 291 (Type III pre-anodize rinse), adapted:
- Dual cascade minimum; triple recommended for aerospace
- Conductivity meters above each stage
- DI water feed on final stage

**Parameter summary:**

| Parameter | Value |
|---|---|
| **Type** | Counter-flow cascade, DI water feed |
| **Temperature** | Ambient |
| **Time** | 60--120 sec total |
| **Final stage conductivity** | < 50 uS/cm for aerospace; < 100 uS/cm minimum |
| **Agitation** | Rack agitation in each tank |

---

### ZONE 4 -- Bath Sensitivity

**Section label:** `WHY BSAA IS THE MOST SENSITIVE ANODIZE BATH` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 15.7".

**BLOCK D -- Sensitivity Comparison Table**

Y: 16.3" to 21.8".

| Factor | Type II (Sulfuric) | Type III (Hardcoat) | BSAA |
|---|---|---|---|
| **H2SO4 concentration** | 165--225 g/L | 110--135 g/L | 30--50 g/L |
| **Additional acid** | None | Oxalic (optional) | H3BO3 5--10 g/L |
| **Buffer capacity** | HIGH | MODERATE | LOW |
| **Drag-in tolerance** | Moderate | Low | VERY LOW |
| **Dissolved Al limit** | < 20 g/L | < 15 g/L | Monitor closely |
| **Effect of 10 mL cleaner drag-in per liter** | Negligible | Minor | Measurable pH/SG shift |

Header: Barlow SemiBold 11 pt `#F0EDE8` on `#3A4055`. Data: JetBrains Mono 12 pt, alternating rows.
BSAA column: `#E8A020` for emphasis values.

Below table, full-width callout:
- Rounded rect, fill `#E8A020` at 12%, border 1 pt `#E8A020`
- Text: `The boric acid (H3BO3) in BSAA is present at 5--10 g/L -- a TINY amount. Drag-in contamination can shift the H2SO4/H3BO3 ratio enough to change the oxide formation/dissolution balance.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Conductivity Targets + DI Water

**Two-column layout (Y: 22.2" to 28.3"):**

**Left -- Conductivity Targets (X: 0.5", W: 11.0"):**

Section label: `CONDUCTIVITY TARGETS FOR BSAA` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Vertical gauge visual (same format as Poster 291):
- 0--50 uS/cm: `AEROSPACE -- REQUIRED` `#27AE60`
- 50--100 uS/cm: `COMMERCIAL -- ACCEPTABLE` `#2EC4B6`
- 100--200 uS/cm: `CAUTION -- MARGINAL FOR BSAA` `#E8A020`
- >200 uS/cm: `FAIL -- DO NOT PROCEED` `#E05C5C`

Note below gauge: `BSAA is less tolerant than Type II. Target the same conductivity as hardcoat (< 50 uS/cm) even for commercial work.` Inter Medium 12 pt `#E8A020`.

**Right -- DI Water Requirement (X: 12.0", W: 11.5"):**

Section label: `DI WATER -- STRONGLY RECOMMENDED` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Two stacked callout boxes:

DI Water:
- Fill `#1E2435`, left accent `#27AE60`
- Title: `DI WATER -- RECOMMENDED FOR ALL BSAA RINSE STAGES` Barlow SemiBold 14 pt `#27AE60`
- `Conductivity: 0.1--5 uS/cm` JetBrains Mono 13 pt `#F0EDE8`
- `Zero dissolved solids, zero chlorides` Inter Regular 12 pt `#F0EDE8`
- `Required for final stage; recommended for all stages` Inter Medium 12 pt `#27AE60`

City Water:
- Fill `#1E2435`, left accent `#E05C5C`
- Title: `CITY WATER -- RISK FOR BSAA` Barlow SemiBold 14 pt `#E05C5C`
- `Conductivity: 100--500+ uS/cm` JetBrains Mono 13 pt `#F0EDE8`
- `Dissolved solids, Cl-, possible F- all accumulate in BSAA bath via drag-in` Inter Regular 12 pt `#F0EDE8`
- `Acceptable ONLY for first cascade stage` Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- Key Rules Strip

**Section label:** `BSAA PRE-ANODIZE RINSE -- KEY RULES` Barlow Condensed ExtraBold 22 pt. Y: 28.7".

Four quick-hit cards:

| Card | X | Rule | Detail |
|---|---|---|---|
| 1 | 0.5" | DI WATER FINAL STAGE | BSAA's low concentration makes it the most sensitive bath to city water contaminants |
| 2 | 6.33" | DUAL CASCADE MINIMUM | Triple recommended for aerospace; single immersion is inadequate |
| 3 | 12.16" | CONDUCTIVITY CHECK | < 50 uS/cm target; log every load; trend analysis catches DI system degradation |
| 4 | 18.0" | DWELL OVER DESMUT | 10--15 sec drain above desmut before entering rinse; minimizes acid drag-in volume |

Each card: Rounded rect, W: 5.5", H: 3.5", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Anodize) -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse water quality requirements are more stringent for BSAA than for conventional sulfuric acid anodizing due to the bath's lower acid concentration and narrow chemistry window. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse BSAA Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster makes the strongest case for why rinse quality matters more for BSAA than any other anodize process. The sensitivity comparison table (Zone 4) is the hero -- side-by-side with Type II and Type III, it becomes obvious that BSAA has the least buffer capacity and lowest contamination tolerance. This is not theoretical: shops transitioning from Type I to BSAA frequently underestimate the rinse quality needed because Type I's chromic acid bath was relatively tolerant of contamination (the chromic acid itself is a strong oxidizer that breaks down organics).

---

*Alaina -- Plating Posters Inc*
*Poster #307 -- Construction Workup v1.0*
*2026-04-26*
