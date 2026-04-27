---
Project: Plating Posters Inc
Poster Number: 662
Title: "Pretreatment -- Liquid Spray Painting"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 2.5"
Technical Source: Pretreatment systems for liquid spray painting -- iron phosphate, zinc phosphate, wash primer (vinyl butyral etch), chromate conversion for aluminum, and self-etching primers. Includes the wash primer as a dual-function system.
Process Scope: Pretreatment for liquid spray painting (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - LiquidSprayPainting
  - Pretreatment
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC02
---

# Poster #662 -- Construction Workup
## Pretreatment -- Liquid Spray Painting

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. Pretreatment for liquid spray painting shares iron phosphate and zinc phosphate with powder coating, but adds two unique options: the wash primer (vinyl butyral etch primer) and self-etching primers. The wash primer is the field hero -- a two-component system that etches bare metal, deposits a conversion layer, and provides primer adhesion in a single 0.3-0.5 mil coat. Self-etching primers serve the same function in one package.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Five pretreatment options comparison (Block B -- HERO):** Iron phosphate, zinc phosphate, wash primer, chromate conversion, self-etching primer.
2. **Wash primer detail (Block C):** Two-component breakdown with military spec reference.
3. **Salt spray performance table (Block D):** Pretreatment + primer combinations.
4. **Defect grid (Block F):** 6 pretreatment failures.

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
ZONE 3 -- FIVE PRETREATMENT OPTIONS HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- WASH PRIMER DETAIL + SELF-ETCH (15.5"--21.5" / ~6.0")
ZONE 5 -- SALT SPRAY TABLE + CHROMATE (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Liquid Spray Painting -- Five Options for Chemical Adhesion` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Iron phosphate for the production line. Wash primer for the field truck. Zinc phosphate for the warranty. Five pretreatment paths -- each with a purpose.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Pretreatment -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean bare metal surface --> After: Conversion-coated or etch-primed surface ready for primer/topcoat`

---

### ZONE 3 -- Five Pretreatment Options Hero

**Section label:** `FIVE PRETREATMENT OPTIONS -- MATCHED TO YOUR APPLICATION` -- Y: 4.4".

**BLOCK B -- Five Cards (Y: 5.0" to 15.0")**

Two rows: top row of 3, bottom row of 2.

**Top Row:**

*Iron Phosphate (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `IRON PHOSPHATE` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters (JetBrains Mono 12 pt):
```
Coating weight: 25--75 mg/ft2
Salt spray (w/ alkyd primer): 250--500 hr B117
Salt spray (w/ epoxy primer): 500--750 hr B117
Standard for general industrial
Same parameters as powder coating
```
- Best for: `Production lines with multi-stage washers`

*Zinc Phosphate (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `ZINC PHOSPHATE` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Coating weight: 150--500 mg/ft2
Salt spray (w/ epoxy primer): 750--1,500 hr B117
Automotive and high-performance
Crystalline structure for maximum adhesion
Higher cost and complexity
```
- Best for: `Automotive, heavy equipment, extended warranty`

*Wash Primer (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `WASH PRIMER (ETCH PRIMER)` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
DFT: 0.3--0.5 mil
Two-component: PVB resin + H3PO4 catalyst
Spec: DOD-P-15328 / TT-P-1757
Etches + converts + primes in ONE coat
Can apply to damp surfaces
Must be topcoated -- not standalone
```
- Best for: `Field touch-up, no-washer situations`

**Bottom Row:**

*Chromate Conversion (X: 0.5", W: 11.0"):*
- Fill: `#1E2435`, top accent `#E05C5C`
- Title: `CHROMATE CONVERSION (ALUMINUM)` -- Barlow SemiBold, 20 pt, `#E05C5C`
- Parameters:
```
MIL-DTL-5541 Type I (hex chrome): 40--150 mg/ft2
MIL-DTL-5541 Type II (trivalent): lower weight
Required by many aerospace paint specs
RoHS/REACH: hex chrome phasing out
Non-chrome alternatives (Ti/Zr) gaining approval
```
- Best for: `Aerospace aluminum per specification`

*Self-Etching Primer (X: 12.0", W: 11.5"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `SELF-ETCHING PRIMER` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
DFT: 0.5--1.0 mil
Acid-functional (H3PO4 component)
Combines adhesion promotion + priming
Single-component (no mixing required)
Common in automotive refinish
Aerospace touch-up
```
- Best for: `Automotive refinish, aerospace field repair`

---

### ZONE 4 -- Wash Primer Detail + Self-Etch

**Section label:** `WASH PRIMER -- THE FIELD APPLICATION HERO` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 21.3"):**

**Left -- Wash Primer Chemistry (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `WASH PRIMER -- HOW IT WORKS` -- Barlow SemiBold, 20 pt, `#27AE60`

Two-component breakdown:
- `COMPONENT A: Polyvinyl butyral (PVB) resin in solvent`
- `COMPONENT B: Phosphoric acid (H3PO4) catalyst in alcohol`
- `Mix ratio: typically 4:1 (A:B) by volume`
- `Pot life: 8--24 hours after mixing`

Three simultaneous actions (Inter Medium 14 pt):
1. `ETCH: Phosphoric acid etches bare metal surface`
2. `CONVERT: Reacts with metal to form thin phosphate layer`
3. `PRIME: PVB resin deposits as thin primer film`

Key rules: `Apply at 0.3--0.5 mil. Do NOT exceed 0.5 mil -- thick wash primer becomes brittle and causes adhesion failure with topcoat.`

**Right -- Self-Etching Primer (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `SELF-ETCHING PRIMER` -- Barlow SemiBold, 18 pt, `#2EC4B6`

- `Single-component acid-functional primer`
- `Phosphoric acid reacts with metal on contact`
- `No mixing required -- ready to spray`
- `DFT: 0.5--1.0 mil`
- `Topcoat within recommended window`

Comparison note: `Simpler than wash primer (no mixing), but less aggressive etch. Wash primer provides deeper chemical bond on bare metal.`

---

### ZONE 5 -- Salt Spray Table + Chromate

**Two-column layout (Y: 21.7" to 26.3"):**

**Left -- Salt Spray Performance (X: 0.5", W: 11.0"):**

Title: `SALT SPRAY PERFORMANCE (ASTM B117)` -- Barlow SemiBold, 16 pt, `#F0EDE8`

| Pretreatment | Primer System | Expected B117 Hours |
|---|---|---|
| Iron phosphate | Alkyd primer | 250--500 hr |
| Iron phosphate | Epoxy primer | 500--750 hr |
| Zinc phosphate | Epoxy primer | 750--1,500 hr |
| Wash primer | Epoxy topcoat | 500--750 hr |
| Chromate (aluminum) | Epoxy primer | Spec-dependent |

**Right -- Chromate Detail (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`.
Title: `CHROMATE CONVERSION -- ALUMINUM` -- Barlow SemiBold, 18 pt, `#E05C5C`

- `Hex chrome (Type I): Maximum corrosion protection`
- `Trivalent (Type II): RoHS-compliant alternative`
- `Non-chrome (Ti/Zr): Growing acceptance`
- `Required before paint on most aerospace aluminum specs`
- `Coating weight verified by test coupon`

RoHS flag: `New installations should default to trivalent or non-chrome unless specification mandates hexavalent.`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN PRETREATMENT FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | EARLY CORROSION | `#E05C5C` | Absent or thin conversion coating | Verify coating weight; increase concentration |
| R1C2 | WASH PRIMER TOO THICK | `#E8A020` | Exceeded 0.5 mil DFT | Apply thinner; single light coat only |
| R1C3 | ADHESION LOSS UNDER TOPCOAT | `#E05C5C` | Poor pretreatment or contamination | Verify conversion coating before priming |
| R2C1 | INTERCOAT DELAMINATION | `#E8A020` | Wash primer too thick or incompatible topcoat | Check DFT; verify topcoat compatibility |
| R2C2 | CHROMATE BLEED-OUT | `#E05C5C` | Excessive chromate coating weight | Reduce immersion time or concentration |
| R2C3 | SELF-ETCH INSUFFICIENT | `#2EC4B6` | Light contamination reducing acid etch effectiveness | Better cleaning before self-etch application |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Liquid Spray Painting`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; DOD-P-15328; MIL-DTL-5541. Wash primer mixing ratios and pot life are product-specific -- consult manufacturer TDS.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Liquid Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The five-option hero gives the quality engineer a decision framework: which pretreatment for which situation. The wash primer detail panel is the unique content for liquid spray -- this dual-function system (etch + convert + prime in one coat) is the field application hero that powder coating can never replicate. The 0.3--0.5 mil DFT limit for wash primer is critical knowledge -- going too thick is a common mistake that causes brittle failure.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #662 -- Construction Workup v1.0*
*2026-04-26*
