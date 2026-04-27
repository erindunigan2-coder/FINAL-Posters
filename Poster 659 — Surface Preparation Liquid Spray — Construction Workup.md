---
Project: Plating Posters Inc
Poster Number: 659
Title: "Surface Preparation -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.2"
Technical Source: Industry-standard surface preparation for liquid spray painting on steel, aluminum, and plastic substrates. Covers SSPC blast grades, profile targets, aluminum etch/anodize, and plastic adhesion promotion (flame/plasma treatment, CPO primers).
Process Scope: Surface preparation for liquid spray painting (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - SurfacePreparation
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #659 -- Construction Workup
## Surface Preparation -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Surface prep for liquid spray painting spans three substrate families: steel (blast grades and profiles), aluminum (etch, conversion, anodize), and plastics (adhesion promotion is the wild card). The hero is a three-substrate comparison showing the prep path for each. Liquid paint's thicker multi-coat system is more forgiving of minor profile variations than powder, but contamination tolerance is zero -- the same as any coating.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-substrate prep comparison (Block B -- HERO):** Steel vs. aluminum vs. plastic -- side-by-side prep paths.
2. **SSPC blast grade table (Block C):** Grades SP-1 through SP-5 with use cases.
3. **Aluminum prep detail (Block D):** Etch, conversion, anodize options.
4. **Plastic prep callout (Block E):** Adhesion promotion methods.
5. **Defect grid (Block F):** 6 prep-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Surface Preparation (Teal)
ZONE 3 -- THREE-SUBSTRATE HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- SSPC GRADES + PROFILE (15.0"--21.0" / ~6.0")
ZONE 5 -- ALUMINUM + PLASTIC DETAIL (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREPARATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- Three Substrates, Three Prep Paths` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Steel, aluminum, or plastic -- each substrate has its own prep recipe. The paint doesn't care what you think the surface looks like. It cares what the surface IS.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Surface Preparation -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Raw incoming material --> After: Clean, profiled, conversion-coated substrate ready for primer`

---

### ZONE 3 -- Three-Substrate Hero

**Section label:** `PREP PATH BY SUBSTRATE` -- Y: 4.4".

**BLOCK B -- Three Columns (Y: 5.0" to 14.5")**

*Column 1 -- Steel (X: 0.5", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#C8D0D8` (Silver)
- Title: `STEEL` -- Barlow Condensed ExtraBold, 28 pt, `#C8D0D8`
- Prep sequence (numbered list, Inter Medium 14 pt):
  1. `SSPC-SP1: Solvent clean (remove oils)`
  2. `SSPC-SP2/SP3: Hand or power tool (loose rust, scale)`
  3. `SSPC-SP6 to SP-10: Blast to spec`
  4. `Profile: 1.5--3.0 mils (38--76 um)`
  5. `Phosphate conversion coating`
  6. `Prime within 4 hours (humid environments)`
- Key metric (JetBrains Mono 14 pt `#E8A020`): `SP-6 Commercial Blast = standard for liquid paint`

*Column 2 -- Aluminum (X: 8.17", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` (Teal)
- Title: `ALUMINUM` -- Barlow Condensed ExtraBold, 28 pt, `#2EC4B6`
- Prep sequence:
  1. `Alkaline etch or non-etch clean`
  2. `Chromate conversion (MIL-DTL-5541) or non-chrome`
  3. `Scuff sand: 180--320 grit Scotch-Brite`
  4. `Anodize (sulfuric or chromic) for aerospace`
  5. `Apply primer within spec window`
- Key metric: `Chromate conversion = aerospace standard (Type I or II)`
- RoHS note (Inter Regular 12 pt `#E05C5C`): `Hex chrome phasing out -- trivalent or non-chrome alternatives gaining spec approval`

*Column 3 -- Plastic (X: 15.83", W: 7.67"):*
- Rounded rect, fill `#1E2435`, top accent `#E8A020` (Amber)
- Title: `PLASTIC` -- Barlow Condensed ExtraBold, 28 pt, `#E8A020`
- Prep sequence:
  1. `Solvent wipe (IPA) -- remove mold release`
  2. `Adhesion promoter application:`
  3. `  - CPO primer for PP/PE`
  4. `  - Flame treatment (3--5 sec exposure)`
  5. `  - Plasma treatment (industrial)`
  6. `Static dissipation for electrostatic spray`
  7. `Apply primer per adhesion promoter window`
- Key metric: `Adhesion promotion is MANDATORY for polyolefins (PP, PE). Without it: zero adhesion.`

---

### ZONE 4 -- SSPC Grades + Profile

**Section label:** `BLAST GRADES AND PROFILE TARGETS` -- Y: 15.2".

**BLOCK C -- SSPC Grade Table (Y: 15.8" to 20.8")**

Full-width table:

| Grade | Name | Removal Level | Profile (mils) | Use Case |
|---|---|---|---|---|
| SP-1 | Solvent Clean | Visible oil/grease | N/A | Minimum first step for all substrates |
| SP-2 | Hand Tool | Loose rust, scale, paint | Variable | Field touch-up, minor repair |
| SP-3 | Power Tool | Loose rust, scale, paint | Variable | Better than SP-2; still manual |
| SP-6 | Commercial Blast | 66% removal of all residues | 1.5--3.0 | Standard for liquid paint on steel |
| SP-10 | Near-White Blast | 95% removal | 1.5--3.0 | High-performance coatings |
| SP-5 | White Metal Blast | 100% removal | 2.0--3.5 | Immersion service, tank lining |

Header: Barlow SemiBold 14 pt on `#3A4055`. Data: JetBrains Mono 12 pt.

Bottom note: `Profile measured per ASTM D4417. Liquid primers generally tolerate slightly coarser profiles than powder coatings.` -- Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Aluminum + Plastic Detail

**Two-column layout (Y: 21.2" to 26.3"):**

**Left -- Aluminum Detail (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `ALUMINUM PREP -- THREE OPTIONS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

*Chemical conversion:*
- `Chromate (MIL-DTL-5541): 40--150 mg/ft2`
- `Non-chrome (Ti/Zr nanoceramic): growing adoption`

*Mechanical:*
- `Scuff sand with 180--320 grit Scotch-Brite`
- `Creates mechanical anchor for primer`

*Anodize:*
- `Sulfuric or chromic anodize`
- `Creates porous oxide layer for paint adhesion`
- `Required by many aerospace paint specs`

**Right -- Plastic Detail (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `PLASTIC PREP -- ADHESION IS EVERYTHING` -- Barlow SemiBold, 18 pt, `#E8A020`

Methods:
- `Chlorinated polyolefin (CPO) primer: For PP and PE`
- `Flame treatment: 3--5 sec propane/natural gas exposure`
- `  Raises surface energy from ~30 to ~50+ dyne/cm`
- `Plasma treatment: atmospheric or vacuum`
- `  Industrial-scale surface activation`
- `Static dissipation: prevents dust attraction and`
- `  enables electrostatic spray on non-conductive parts`

Test note: `Dyne pen test to verify surface energy > 38 dyne/cm before painting.` -- Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN PREP FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | ADHESION LOSS (STEEL) | `#E05C5C` | Mill scale, oil, insufficient profile | Blast to SP-6; solvent clean first |
| R1C2 | ADHESION LOSS (ALUMINUM) | `#E05C5C` | Missing conversion coating or anodize | Apply chromate or non-chrome conversion |
| R1C3 | ADHESION LOSS (PLASTIC) | `#E8A020` | No adhesion promoter on polyolefin | CPO primer or flame/plasma treatment |
| R2C1 | FLASH RUST | `#E05C5C` | Blast-to-prime time exceeded | Prime within 4 hr; control humidity |
| R2C2 | FISH-EYE | `#E8A020` | Silicone contamination or mold release | IPA wipe; identify contamination source |
| R2C3 | PROFILE TOO COARSE | `#2EC4B6` | Aggressive media or excessive blast | Verify 1.5--3.0 mils; change media |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Surface Preparation -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; SSPC/NACE standards; MIL-DTL-5541 for aluminum.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Preparation Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Three-substrate comparison is the visual hook -- steel, aluminum, and plastic each get their own column with a clear prep path. The plastic column is the surprise: most metal finishers don't think about painting plastics, but automotive bumpers, interior trim, and consumer electronics are all painted plastic. The CPO primer / flame treatment requirement for polyolefins is knowledge that saves adhesion failures. SSPC grades table is the evergreen reference.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #659 -- Construction Workup v1.0*
*2026-04-26*
