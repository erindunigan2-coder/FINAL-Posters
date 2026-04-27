---
Project: Plating Posters Inc
Poster Number: 650
Title: "Surface Preparation -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.2"
Technical Source: Industry-standard surface preparation for powder coating. Covers substrate requirements, blast profiles, outgassing mitigation, and incoming material condition for steel, aluminum, and galvanized substrates.
Process Scope: Surface preparation for powder coating -- substrate conditioning before cleaning
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - SurfacePreparation
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #650 -- Construction Workup
## Surface Preparation -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage-level deep dive into surface preparation for powder coating. This is the "foundation of the foundation" poster -- powder magnifies every surface defect because the 2--4 mil film cannot fill imperfections the way a thick liquid primer might. The hero visual is a substrate cross-section showing what happens when prep is right vs. wrong.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate cross-section hero (Block B):** Two side-by-side cross-sections -- properly prepared (clean, profiled, uniform) vs. poorly prepared (mill scale, oil, flash rust). Built with layered rectangles and labeled callouts.
2. **Blast profile table (Block D):** Media types, profiles, and SSPC grades.
3. **Outgassing risk callout (Block E):** Coral-tinted warning panel for cast aluminum, hot-rolled steel, and galvanized substrates.
4. **Multi-substrate reference (Block F):** Steel vs. aluminum vs. galvanized requirements grid.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Surface Preparation (Teal)
ZONE 3 -- SUBSTRATE CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BLAST PROFILE + SSPC GRADES (14.5"--20.5" / ~6.0")
ZONE 5 -- OUTGASSING RISK + MULTI-SUBSTRATE GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID -- PREP FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- The Foundation of Every Finish` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Powder magnifies defects. A 2-mil film hides nothing. Get the surface right or the coating fails -- every time.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Surface Preparation -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw incoming material (mill scale, oils, oxides)  -->  After: Clean, profiled substrate ready for pretreatment wash`

---

### ZONE 3 -- Substrate Cross-Section Hero

**Section label:** `WHAT GOOD PREP LOOKS LIKE -- AND WHAT BAD PREP COSTS YOU` -- Y: 4.4".

**BLOCK B -- Side-by-Side Cross-Sections**

Y: 5.0" to 14.0".

**Left panel -- GOOD PREP (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#27AE60`
- Title: `PROPERLY PREPARED` -- Barlow SemiBold, 18 pt, `#27AE60`
- Cross-section illustration (layered rectangles):
  - Bottom layer: `SUBSTRATE (STEEL)` -- rect fill `#3A4055`, H: 2.0"
  - Surface texture: wavy line indicating 1.0--2.5 mil blast profile
  - Label: `Blast profile 1.0--2.5 mils (ASTM D4417)` JetBrains Mono 12 pt
  - Conversion coating layer: thin line `#2EC4B6`, label: `Iron phosphate 25--75 mg/ft2`
  - Powder layer: rect fill `#27AE60` at 40%, H: 0.5", label: `Powder 2--4 mils`
- Callouts (Inter Medium 13 pt `#27AE60`):
  - `Clean metal surface -- no oils, no oxides`
  - `Uniform anchor profile for mechanical adhesion`
  - `Conversion coating bonds chemically to substrate`
  - `Result: 500--1,500 hr salt spray (B117)`

**Right panel -- BAD PREP (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, border 1 pt `#E05C5C`
- Title: `POORLY PREPARED` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Cross-section illustration:
  - Bottom layer: `SUBSTRATE` -- rect fill `#3A4055`, H: 2.0"
  - Mill scale patches: dark rectangles `#252B3D` on surface
  - Oil contamination: wavy blob label `Oil / soil residue`
  - Flash rust spots: orange spots `#E8A020` at 40%
  - Powder layer: rect fill `#E05C5C` at 30%, with gap/lift indicators
- Callouts (Inter Medium 13 pt `#E05C5C`):
  - `Mill scale creates adhesion barrier`
  - `Oil contamination causes fish-eye and cratering`
  - `Flash rust develops in 4 hours (humid conditions)`
  - `Result: Adhesion failure, blistering, field callbacks`

---

### ZONE 4 -- Blast Profile + SSPC Grades

**Section label:** `BLAST STANDARDS AND PROFILE TARGETS` -- Y: 14.7".

**BLOCK D -- Two-Column Layout (Y: 15.3" to 20.3")**

**Left -- Blast Media Table (X: 0.5", W: 11.0"):**

| Media | Profile (mils) | Aggressiveness | Best For |
|---|---|---|---|
| Aluminum Oxide | 1.5--3.0 | Aggressive | Heavy scale, fast cut |
| Steel Grit | 1.0--2.5 | Consistent | Production lines |
| Garnet | 1.0--2.0 | Moderate | General prep |
| Glass Bead | 0.5--1.0 | Light | Cleaning without heavy profile |

Header: Barlow SemiBold 14 pt `#F0EDE8` on `#3A4055`. Data: JetBrains Mono 12 pt.

**Right -- SSPC Grade Reference (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.

| Grade | Name | Description | Use Case |
|---|---|---|---|
| SP-1 | Solvent Clean | Remove visible oil/grease | Minimum first step |
| SP-6 | Commercial Blast | Remove mill scale, rust (66%) | Standard powder coat |
| SP-10 | Near-White Blast | 95% removal of all residues | High-performance coatings |
| SP-5 | White Metal Blast | 100% removal | Immersion service |

Bottom note: `Target profile for powder coating on steel: 1.0--2.5 mils (25--63 microns) per ASTM D4417` -- JetBrains Mono 13 pt `#E8A020`.

Critical timing note (Coral):
- `Blast-to-coat window: 4 hours maximum in humid environments. Flash rust kills adhesion.` -- Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Outgassing Risk + Multi-Substrate Grid

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Outgassing Warning (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`, border 1 pt `#E05C5C` at 30%.

- Title: `OUTGASSING -- THE HIDDEN KILLER` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):
  - `Cast aluminum, hot-rolled steel, and galvanized steel trap gases in the substrate pores.`
  - `During cure at 350--400 F, these gases escape through the molten powder film.`
  - `Result: Pinholes, craters, and "outgassing" defects that cannot be repaired without stripping.`
- Mitigation (Inter Medium 14 pt `#27AE60`):
  - `PRE-BAKE: Heat substrate to cure temperature for 10--20 min BEFORE powder application`
  - `ALTERNATIVE: Use outgassing-resistant powder formulations`
  - `TESTING: Run test panel from each lot -- outgassing is batch-dependent`

**Right -- Multi-Substrate Requirements (X: 12.0", W: 11.5"):**

Title: `SUBSTRATE-SPECIFIC PREP` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Three stacked callout cards:

*Steel:*
- Accent: `#C8D0D8`
- `Blast to SSPC-SP6 minimum`
- `Profile: 1.0--2.5 mils`
- `Iron phosphate or zinc phosphate conversion`

*Aluminum:*
- Accent: `#2EC4B6`
- `Alkaline etch or non-etch clean`
- `Chromate or non-chrome conversion (MIL-DTL-5541)`
- `Outgassing risk on castings -- pre-bake required`

*Galvanized:*
- Accent: `#E8A020`
- `Light abrasion (sweep blast or scotch-brite)`
- `Adhesion promoter or etch primer may be needed`
- `SEVERE outgassing risk -- always pre-bake`

---

### ZONE 6 -- Defect Grid -- Prep Failures

**Section label:** `WHEN PREP FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | ADHESION LOSS | `#E05C5C` | Oil/soil on surface | Re-clean; water-break test |
| R1C2 | FISH-EYE / CRATERING | `#E05C5C` | Silicone contamination | Identify source; isolate silicone |
| R1C3 | OUTGASSING PINHOLES | `#E8A020` | Trapped substrate gas | Pre-bake before coating |
| R2C1 | FLASH RUST BLISTERS | `#E05C5C` | Blast-to-coat time exceeded | Coat within 4 hours; control humidity |
| R2C2 | POOR PROFILE ADHESION | `#E8A020` | Insufficient blast profile | Re-blast; verify 1.0--2.5 mils |
| R2C3 | MILL SCALE LIFTING | `#2EC4B6` | Incomplete scale removal | Blast to SP-6 minimum |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Surface Preparation -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; SSPC/NACE standards; Powder Coating Institute references.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Preparation Powder -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster hammers one message: surface prep is everything. The side-by-side cross-section hero must be immediately readable -- good prep on the left (green accents, clean lines), bad prep on the right (coral accents, chaos). The outgassing panel is the one thing that surprises newcomers to powder coating. The blast-to-coat 4-hour window is critical knowledge that saves jobs.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #650 -- Construction Workup v1.0*
*2026-04-26*
