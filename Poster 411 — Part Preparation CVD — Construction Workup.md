---
Project: Plating Posters Inc
Poster Number: 411
Title: "Part Preparation -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.3)"
Technical Source: CVD part preparation covering WC-Co substrate verification, surface finish requirements, edge preparation, cobalt enrichment concerns, masking with refractory pastes, and dimensional tolerance considerations for CVD coating buildup.
Process Scope: CVD part preparation (Stage 3 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - PartPreparation
  - SubstratePrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #411 -- Construction Workup
## Part Preparation -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 10. CVD part preparation is fundamentally different from PVD because the substrate pool is narrower (primarily WC-Co cemented carbide) and the high process temperature creates unique concerns: cobalt migration, eta-phase formation, and grinding burn. The surface finish requirements are less demanding than PVD because CVD coatings are thicker and the chemical process has better throwing power -- but substrate integrity is paramount.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate compatibility chart (Block B -- HERO):** Large comparison showing which substrates can and cannot tolerate CVD temperatures, with the WC-Co sweet spot highlighted.
2. **Surface finish requirements (Block C):** Comparison of CVD vs. PVD surface finish needs.
3. **Edge preparation guide (Block D):** K-land and chamfer illustrations for cutting insert edges.
4. **Cobalt concerns callout (Block E):** Warning panel on cobalt depletion and eta-phase.
5. **Masking materials (Block F):** Table of CVD-compatible masking materials.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 19.5" / 24.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal -- preparation)
ZONE 3 -- SUBSTRATE COMPATIBILITY / HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SURFACE FINISH + EDGE PREP (14.5"--19.5" / ~5.0")
ZONE 5 -- COBALT CONCERNS (19.5"--24.5" / ~5.0")
ZONE 6 -- MASKING + DIMENSIONAL NOTES (24.5"--32.5" / ~8.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 3 of 10 -- Substrate Verification, Edge Prep, and Cobalt Concerns` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `CVD operates at 800-1100 C. Your substrate must survive that temperature without distortion, phase change, or cobalt depletion. WC-Co cemented carbide is the sweet spot. Verify before you load.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts received, documentation verified (Stage 1) --> After: Parts prepped for cleaning -- edges prepared, masking applied if needed`

---

### ZONE 3 -- Substrate Compatibility (HERO)

**Section label:** `SUBSTRATE COMPATIBILITY -- CAN IT SURVIVE CVD TEMPERATURES?` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Substrate Chart (Y: 5.0" to 14.3")**

Table format with visual "traffic light" indicators.

Column widths (23.0" total): Substrate (5.0") | Max Temp (3.0") | CVD Compatible? (3.0") | Notes (6.0") | Risk Level (3.0") | Verdict (3.0")

| Substrate | Max Temp | CVD OK? | Notes | Risk | Verdict |
|---|---|---|---|---|---|
| WC-Co cemented carbide | 1200+ C | YES | Primary CVD substrate; tolerate process temp | LOW | `#27AE60` COAT IT |
| Ceramics (Si3N4, Al2O3, SiC) | 1500+ C | YES | Excellent thermal stability; common for CVD | LOW | `#27AE60` COAT IT |
| Graphite | 2500+ C | YES | Common substrate for SiC CVD; friable | LOW | `#27AE60` COAT IT |
| Silicon wafers | 1414 C (mp) | YES | Semiconductor CVD; epitaxial growth | LOW | `#27AE60` COAT IT |
| High-speed steel (HSS) | 550 C (temper) | NO | CVD temp exceeds tempering temp -- softens steel | HIGH | `#E05C5C` DO NOT COAT |
| Pre-hardened tool steel | 500-600 C | NO | Loses hardness above tempering temperature | HIGH | `#E05C5C` DO NOT COAT |
| Aluminum alloys | 400-550 C | NO | Melts or distorts at CVD temperatures | HIGH | `#E05C5C` DO NOT COAT |
| Stainless steel | 800+ C | CAUTION | Sensitization risk (carbide precipitation in 304/316) | MEDIUM | `#E8A020` SPECIAL CARE |
| Titanium alloys | 880+ C | CAUTION | Alpha-beta transition at 880 C; grain growth | MEDIUM | `#E8A020` SPECIAL CARE |

Header: Barlow SemiBold 13 pt, fill `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`. Verdict: Barlow SemiBold 12 pt, color per verdict. Alternating rows `#1E2435` / `#252B3D`.

Risk indicators: Small rounded rect (0.6" x 0.3") color-coded:
- LOW = `#27AE60` fill
- MEDIUM = `#E8A020` fill
- HIGH = `#E05C5C` fill

Bottom callout:
- `CVD was built for cemented carbide. If your substrate can't handle 800-1100 C, use PVD instead (200-500 C).` Inter Medium 15 pt `#E8A020`

---

### ZONE 4 -- Surface Finish + Edge Preparation

**Two-column layout (Y: 14.5" to 19.3"):**

**Left -- Surface Finish (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.6", fill `#1E2435`, left accent `#2EC4B6`
- Title: `SURFACE FINISH REQUIREMENTS` Barlow SemiBold 20 pt `#2EC4B6`

| Application | Ra Requirement | Notes |
|---|---|---|
| Cutting inserts | < 0.4 um (16 uin) | After grinding; standard production finish |
| Precision molds | < 0.2 um (8 uin) | Fine grinding or lapping |
| General wear parts | < 0.8 um (32 uin) | Less critical than PVD |

Data: JetBrains Mono 12 pt `#F0EDE8`.

Key difference callout:
- `CVD coatings are thicker (3-20+ um) and have chemical "throwing power" -- surface finish requirements are less demanding than PVD (which needs Ra < 0.05-0.2 um).` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Edge Preparation (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.6", fill `#1E2435`, left accent `#E8A020`
- Title: `EDGE PREPARATION` Barlow SemiBold 20 pt `#E8A020`

Edge types (Inter Medium 14 pt `#F0EDE8`):
- `K-land: Flat chamfer at cutting edge (0.05-0.2 mm x 15-25 deg)`
- `Honed radius: Rounded edge (20-50 um radius)`
- `Sharp edge: < 10 um radius -- AVOID for CVD (stress concentration, coating buildup at edge)`

Bottom note:
- `CVD gas-phase reactions can cause excess coating buildup at sharp edges and corners. Edge prep before coating prevents this.` Inter Regular 12 pt `#E8A020`

Inspection callout:
- `CHECK FOR: Grinding burn (discoloration), sub-surface damage (micro-cracks), cobalt depletion zone from previous heat treatment` Inter Medium 12 pt `#E05C5C`

---

### ZONE 5 -- Cobalt Concerns

**Section label:** `COBALT -- THE CVD SUBSTRATE CHALLENGE` -- Y: 19.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Cobalt Warning Panel (Y: 20.3" to 24.3")**

Full-width rounded rect, W: 23.0", H: 3.8", fill `#1E2435`, left accent `#E05C5C`, 0.06".

**Title:** `WHY COBALT MATTERS IN CVD` Barlow SemiBold 22 pt `#E05C5C`

Two-column interior:

**Left column -- The Problem (X: 1.0", W: 10.5"):**
- Inter Medium 14 pt `#F0EDE8`
- `HCl gas (CVD byproduct) attacks cobalt binder in WC-Co at high temperature`
- `Cobalt migrates to surface or is etched away -- creating a cobalt-depleted zone`
- `Depleted zone is brittle -- reduces substrate toughness and coating adhesion`
- `Eta-phase (Co3W3C) forms at interface if cooling is not controlled -- brittle intermetallic`

**Right column -- The Solutions (X: 12.5", W: 10.5"):**
- Inter Medium 14 pt `#27AE60`
- `Use TiN as first interlayer -- protects WC-Co surface during subsequent high-temp layers`
- `MT-CVD (700-900 C) for inner layers reduces cobalt attack vs. HT-CVD (1000-1050 C)`
- `Control cooling rate through 900-700 C range to minimize eta-phase`
- `Select WC-Co grades with higher cobalt content (10-12% Co) for CVD compatibility`
- `Modern "CVD-grade" substrates are specifically designed to resist cobalt depletion`

Bottom callout:
- `Cobalt depletion is the #1 substrate-related failure mode in CVD-coated cutting inserts. It does not occur in PVD because PVD operates below the temperature where HCl attacks cobalt.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Masking + Dimensional Notes

**Two-column layout (Y: 24.5" to 32.3"):**

**Left -- Masking Materials (X: 0.5", W: 11.0"):**

**Section label:** `CVD MASKING` -- Y: 24.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

- Rounded rect, Y: 25.2", H: 3.5", fill `#1E2435`, left accent `#2EC4B6`

| Material | Max Temp | Application Method |
|---|---|---|
| Al2O3 paste (refractory) | 1200+ C | Brush or screen print |
| ZrO2 paste (refractory) | 1500+ C | Brush or screen print |
| BN spray (boron nitride) | 1000+ C | Spray on fixtures |
| Graphite fixtures | 2500+ C | Inherent masking by contact |

Data: JetBrains Mono 12 pt `#F0EDE8`.

Note: `Masking is less common in CVD than PVD -- most cutting inserts are coated on all surfaces. Masking mainly used on mounting holes or specific non-coated areas.` Inter Regular 12 pt `#F0EDE8` at 70%.

**Right -- Dimensional Tolerances (X: 12.0", W: 11.5"):**

**Section label:** `COATING ADDS THICKNESS` -- Y: 24.7".

- Rounded rect, Y: 25.2", H: 3.5", fill `#1E2435`, left accent `#E8A020`
- Title: `DIMENSIONAL IMPACT` Barlow SemiBold 18 pt `#E8A020`

Key points (Inter Medium 14 pt `#F0EDE8`):
- `CVD adds 3-20+ um per side (much thicker than PVD's 1-5 um)`
- `For precision inserts: account for coating thickness in pre-grind dimensions`
- `Typical tolerance: specify +/- 10% thickness uniformity`
- `Post-coat grinding or honing may be required for tight-tolerance applications`
- `Multilayer stacks (TiN + TiCN + Al2O3 + TiN) can total 15-25 um`

Bottom callout:
- `CVD coatings are 3-5x thicker than PVD. Dimensional impact is real -- always account for coating buildup in the pre-coating dimensions.` Inter Medium 13 pt `#E8A020`

**Common failures strip (Y: 29.0" to 32.3"):**

Four compact failure cards, each W: 5.5", H: 3.1", fill `#1E2435`, left accent `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SUBSTRATE SOFTENED | HSS or pre-hardened steel loaded -- exceeds temper temp | Verify material grade; CVD is for carbide/ceramics only |
| 2 | 6.33" | GRINDING BURN | Aggressive grinding created heat-affected zone | Inspect for discoloration; re-grind or reject |
| 3 | 12.16" | EDGE BUILDUP | Sharp edges not prepped; CVD gas nucleation at edges | K-land or hone edges before coating |
| 4 | 18.0" | WRONG GRADE LOADED | WC-Co grade not rated for CVD temperature | Check material cert; use CVD-grade substrates |

---

### ZONE 7 -- Footer

Standard footer. Title: `Part Preparation -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Preparation CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The substrate compatibility chart is the hero because it answers the most fundamental CVD question: "can my part handle 800-1100 C?" The traffic-light verdict system makes the answer instantly clear. The cobalt depletion panel is critical technical content unique to CVD that has no parallel in PVD -- operators and engineers need to understand this failure mode. The comparison to PVD surface requirements helps operators who work both processes understand why CVD is more forgiving on surface finish but more demanding on substrate material.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #411 -- Construction Workup v1.0*
*2026-04-26*
