---
Project: Plating Posters Inc
Poster Number: 653
Title: "Pretreatment -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.5"
Technical Source: Industry-standard pretreatment systems for powder coating -- iron phosphate, zinc phosphate, zirconium nanoceramic, and chromate conversion. Covers coating weights, salt spray performance, and the emerging shift toward nanoceramic multi-metal systems.
Process Scope: Pretreatment / conversion coating for powder coating (Stage 4 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - Pretreatment
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #653 -- Construction Workup
## Pretreatment -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 9. Pretreatment is the chemical bridge between the cleaned substrate and the powder coat. Iron phosphate is the workhorse, zinc phosphate is the premium, and zirconium nanoceramic is the rising star. The hero visual is a three-column comparison of these technologies with their coating weights, salt spray performance, and cost/complexity trade-offs. Chromate conversion for aluminum gets its own callout with the RoHS flag.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-column pretreatment comparison (Block B -- HERO):** Iron phosphate vs. zinc phosphate vs. zirconium nanoceramic -- side-by-side with key metrics.
2. **Coating weight and salt spray table (Block C):** Quantitative comparison.
3. **Chromate conversion callout (Block D):** Aluminum-specific with RoHS/REACH flag.
4. **When-to-specify decision matrix (Block E):** Which pretreatment for which application.
5. **Defect grid (Block F):** 6 pretreatment-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Pretreatment (Amber)
ZONE 3 -- THREE-COLUMN PRETREATMENT COMPARISON HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- COATING WEIGHT + SALT SPRAY TABLE (15.5"--21.5" / ~6.0")
ZONE 5 -- CHROMATE CALLOUT + DECISION MATRIX (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID -- PRETREATMENT FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- The Conversion Coating That Makes Adhesion Possible` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Without pretreatment, powder coating is just colored dust sitting on bare metal. The conversion coating is the chemical handshake between substrate and film.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Pretreatment -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, profiled substrate --> After: Conversion-coated surface with chemical adhesion layer`

---

### ZONE 3 -- Three-Column Pretreatment Comparison Hero

**Section label:** `THREE TECHNOLOGIES -- ONE GOAL: ADHESION + CORROSION PROTECTION` -- Y: 4.4".

**BLOCK B -- Three-Column Comparison**

Y: 5.0" to 15.0". Three large columns side by side.

*Column 1 -- Iron Phosphate (X: 0.5", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `IRON PHOSPHATE` -- Barlow Condensed ExtraBold, 24 pt, `#2EC4B6`
- Subtitle: `The Workhorse` -- Barlow SemiBold, 14 pt, `#F0EDE8` at 50%
- Parameters (JetBrains Mono 13 pt):
```
Chemistry: Acidic phosphate, pH 3.5--5.5
Accelerators: Hydroxylamine, nitrite,
  or molybdate
Coating weight: 25--75 mg/ft2
  (270--810 mg/m2)
Crystal structure: Amorphous
Color: Iridescent blue-to-gold on steel
Temp: 100--140 F (38--60 C)
Time: 60--120 sec
```
- Salt spray (Inter Medium 14 pt `#27AE60`): `500--750 hr B117 on CRS with powder`
- Cost note (Inter Regular 13 pt at 70%): `Lowest chemical and waste treatment cost. Standard for general industrial.`

*Column 2 -- Zinc Phosphate (X: 8.17", W: 7.33"):*
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `ZINC PHOSPHATE` -- Barlow Condensed ExtraBold, 24 pt, `#E8A020`
- Subtitle: `The Premium` -- Barlow SemiBold, 14 pt, `#F0EDE8` at 50%
- Parameters:
```
Chemistry: Zinc/manganese/nickel modified
Coating weight: 150--500 mg/ft2
  (1,600--5,400 mg/m2)
Crystal structure: Crystalline
  Hopeite + Phosphophyllite
Surface conditioning: TiPO4 colloidal
  (refines crystal size)
Temp: 95--130 F (35--54 C)
Time: 120--180 sec
More stages, higher complexity
```
- Salt spray: `750--1,500+ hr B117 on CRS with powder`
- Cost note: `3--5x chemical and waste cost vs. iron phosphate. Sludge management required.`

*Column 3 -- Zirconium Nanoceramic (X: 15.83", W: 7.67"):*
- Rounded rect, fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `ZIRCONIUM NANOCERAMIC` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
- Subtitle: `The Rising Star` -- Barlow SemiBold, 14 pt, `#F0EDE8` at 50%
- Parameters:
```
Chemistry: Fluorozirconic acid (H2ZrF6)
  or fluorotitanic acid
pH: 3.5--5.0
Coating weight: 5--30 mg/ft2
  (nanoscale oxide film)
Temp: Ambient to 110 F
Time: 60--120 sec
Chrome-free, low sludge
Multi-metal capable (steel + Al + galv)
```
- Salt spray: `500--750 hr B117 (approaches zinc phos with optimized seal rinse)`
- Cost note: `Lower waste treatment burden than iron phos. Growing adoption -- replacing iron phos in many shops.`

---

### ZONE 4 -- Coating Weight + Salt Spray Table

**Section label:** `PERFORMANCE COMPARISON AT A GLANCE` -- Y: 15.7".

**BLOCK C -- Comparison Table (Y: 16.3" to 21.3")**

| Technology | Coating Weight | Crystal Type | B117 Salt Spray (w/ powder) | Complexity | Cost Index |
|---|---|---|---|---|---|
| Iron Phosphate | 25--75 mg/ft2 | Amorphous | 500--750 hr | Low (5-stage washer) | 1x |
| Zinc Phosphate | 150--500 mg/ft2 | Crystalline | 750--1,500+ hr | High (7-10 stages + sludge) | 3--5x |
| Zirconium Nanoceramic | 5--30 mg/ft2 | Nanoscale oxide | 500--750 hr | Low-Medium | 1--2x |
| Chromate (Aluminum) | 40--150 mg/ft2 | Amorphous Cr(III)/Cr(VI) | Application-specific | Medium | 2--3x |

Header: Barlow SemiBold 14 pt on `#3A4055`. Data: JetBrains Mono 12 pt.

---

### ZONE 5 -- Chromate Callout + Decision Matrix

**Two-column layout (Y: 21.7" to 26.3"):**

**Left -- Chromate Conversion (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`, border 1 pt `#E05C5C` at 30%.
Title: `CHROMATE CONVERSION (ALUMINUM)` -- Barlow SemiBold, 18 pt, `#E05C5C`

Body (Inter Regular 14 pt):
- `Hexavalent chromate (MIL-DTL-5541 Type I): Still required by many aerospace specs. Coating weight 40--150 mg/ft2.`
- `Trivalent chromate (Type II): Chrome-III alternative. Lower coating weight. Gaining approval.`
- `Non-chrome alternatives (Ti/Zr): Growing traction but not universally accepted for aerospace.`

RoHS/REACH flag (Coral):
- `Hex chrome is being phased out under RoHS/REACH. New installations should default to trivalent or non-chrome unless aerospace spec mandates otherwise.`

**Right -- Decision Matrix (X: 12.0", W: 11.5"):**

Title: `WHICH PRETREATMENT FOR YOUR APPLICATION?` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Application | Recommended | Why |
|---|---|---|
| General industrial (furniture, shelving) | Iron phosphate | Cost-effective, adequate performance |
| Automotive, heavy equipment | Zinc phosphate | Maximum corrosion protection |
| Multi-metal line (steel + Al + galv) | Zirconium nanoceramic | One chemistry fits all substrates |
| Aerospace aluminum | Chromate (per spec) | Spec-driven; trivalent preferred |
| Extended warranty (10+ yr outdoor) | Zinc phosphate | Highest B117 performance |

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN PRETREATMENT FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | LOW COATING WEIGHT | `#E8A020` | Bath chemistry out of range or temperature low | Check total acid, free acid, accelerator, temperature |
| R1C2 | HEAVY SLUDGE (ZINC PHOS) | `#E05C5C` | Iron contamination from substrate dissolving | Filtration, centrifuge, sludge management |
| R1C3 | COARSE CRYSTALS | `#E8A020` | Missing or depleted surface conditioner (TiPO4) | Replenish surface conditioning rinse |
| R2C1 | ADHESION FAILURE | `#E05C5C` | Incomplete or absent conversion coating | Verify coating weight by gravimetric strip |
| R2C2 | EARLY CORROSION | `#E05C5C` | Coating weight below minimum specification | Increase concentration, time, or temperature |
| R2C3 | STAINING / DISCOLORATION | `#2EC4B6` | Over-etching or excessive dwell in phosphate | Reduce immersion time; check pH |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references. Pretreatment chemistry is supplier-specific -- consult your chemical supplier for operating parameters and control limits.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-column hero comparison is the visual anchor -- iron phosphate (reliable blue-collar), zinc phosphate (premium performance), zirconium nanoceramic (the future). The decision matrix gives the quality engineer a fast answer to "which one should we run?" The chromate callout with the RoHS flag is essential context for anyone on an aluminum line. Coating weight numbers are the actionable data -- everything else is explanation.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #653 -- Construction Workup v1.0*
*2026-04-26*
