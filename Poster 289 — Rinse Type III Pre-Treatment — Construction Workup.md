---
Project: Plating Posters Inc
Poster Number: 289
Title: "Rinse (Pre-Etch) -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2, Section 2.3)"
Process Scope: Pre-etch rinse for hardcoat anodizing -- Stage 2 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Rinse
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #289 -- Construction Workup
## Rinse (Pre-Etch) -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 2 of 8. This is the rinse between alkaline cleaning and the etch/desmut stages. Same rinse as Type II but with a hardcoat-specific warning: alkaline drag-over into the etch bath is worse for hardcoat because the etch step is often short (30--90 sec) or skipped entirely for precision parts -- any cleaner residue that carries through disrupts the desmut chemistry and ultimately contaminates the low-concentration anodize bath.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank hero (Block B):** Cascade rinse tank cross-section with flow arrows, conductivity meter, and drag-out zone.
2. **Drag-out chemistry panel (Block D):** What alkaline cleaner residue does downstream.
3. **Conductivity target callout (Block E):** Visual meter showing pass/fail thresholds.
4. **Rinse efficiency comparison (Block F):** Single immersion vs. cascade vs. spray rinse.

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
  Stage 2 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAG-OUT CHEMISTRY (14.5"--20.5" / ~6.0")
ZONE 5 -- RINSE EFFICIENCY COMPARISON (20.5"--26.5" / ~6.0")
ZONE 6 -- HARDCOAT-SPECIFIC RINSE RULES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stage 2 of 8 -- Pre-Etch` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The bridge between cleaning and etching. Every gram of cleaner you drag over is a gram of contamination in every downstream tank.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Part coated with alkaline cleaner residue  -->  After: Cleaner-free surface ready for etch or desmut`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE PRE-ETCH RINSE STATION` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Tank Cross-Section**

Y: 5.0" to 13.5".

**Tank body (dual cascade):**
- Two rounded rects side by side representing Stage 1 (dirty) and Stage 2 (clean) cascade tanks
- Stage 1: X: 2.0", Y: 5.5", W: 9.5", H: 7.0", fill `#252B3D`, border 2 pt `#C8D0D8`
- Stage 2: X: 12.5", Y: 5.5", W: 9.5", H: 7.0", fill `#252B3D` at 80% (slightly lighter to indicate cleaner water), border 2 pt `#C8D0D8`
- Arrow from Stage 2 overflow to Stage 1: 2 pt `#2EC4B6`, label `Overflow`
- Arrow from Stage 1 to drain: 2 pt `#E05C5C`, label `To waste treatment`

**Parts moving through (center of Stage 1):**
- 2 vertical rects, fill `#C8D0D8` at 40%, border 1 pt `#C8D0D8`
- Label: `PARTS FROM CLEANER` Barlow SemiBold 12 pt `#C8D0D8`

**Fresh water inlet (right side of Stage 2):**
- Arrow from right, 2 pt `#2EC4B6`
- Label: `Fresh water in` Inter Regular 11 pt `#2EC4B6`

**Conductivity meter (above Stage 2):**
- Small rounded rect, W: 2.0", H: 0.6", fill `#1E2435`, border 1 pt `#C8D0D8`
- Text: `COND: <500 uS/cm` JetBrains Mono 12 pt `#27AE60`

**Bath parameter labels (below tanks, Y: 13.0"):**

| Parameter | Value |
|---|---|
| **Type** | Flowing ambient water rinse (city or DI) |
| **Temperature** | Ambient (60--85 F / 15--30 C) |
| **Time** | 30--60 sec immersion; or spray rinse |
| **Conductivity target** | < 200 uS/cm for commercial; < 50 uS/cm for critical |
| **Flow** | Counter-flow dual rinse preferred |

JetBrains Mono 13 pt `#F0EDE8`, labels Inter Medium 13 pt `#F0EDE8` at 60%.

---

### ZONE 4 -- Drag-Out Chemistry

**Section label:** `WHAT CLEANER DRAG-OVER DOES DOWNSTREAM` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

**BLOCK D -- Downstream Contamination Chain**

Y: 15.3" to 20.3".

Four connected callout boxes in a horizontal chain:

Box 1 -- Etch Tank:
- Rounded rect, W: 5.25", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `ETCH TANK` Barlow SemiBold 16 pt `#E8A020`
- Content: `Alkaline drag-over raises pH of etch bath. Depletes free NaOH concentration. Causes uneven etch rate. Hardcoat etch is SHORT (30--90 sec) -- any dilution is proportionally larger.` Inter Regular 12 pt `#F0EDE8`

Box 2 -- Desmut Tank:
- Same dims, left accent `#E8A020`
- Title: `DESMUT TANK` Barlow SemiBold 16 pt `#E8A020`
- Content: `Alkaline contamination neutralizes acid. Raises pH above effective desmut range. Smut residue remains -- trapped under hard coat = delamination.` Inter Regular 12 pt `#F0EDE8`

Box 3 -- Anodize Tank:
- Same dims, left accent `#E05C5C`
- Title: `ANODIZE TANK` Barlow SemiBold 16 pt `#E05C5C`
- Content: `Hardcoat runs at 10--12% H2SO4 (vs. 15--20% Type II). Lower concentration = less tolerance for contamination. Cleaner surfactants cause foaming. Organic contamination raises dissolved carbon.` Inter Regular 12 pt `#F0EDE8`

Box 4 -- Final Coating:
- Same dims, left accent `#E05C5C`
- Title: `FINAL COATING` Barlow SemiBold 16 pt `#E05C5C`
- Content: `Soft spots. Burning. Non-uniform thickness. Delamination. All traceable back to a 30-second rinse that was too short.` Inter Regular 12 pt `#F0EDE8`

Arrows between boxes: 2 pt `#3A4055`, right-pointing.

---

### ZONE 5 -- Rinse Efficiency Comparison

**Section label:** `RINSE METHODS -- EFFICIENCY COMPARISON` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 20.7".

**BLOCK F -- Three-Column Comparison**

Y: 21.3" to 26.3".

Three callout boxes:

**Single Immersion (X: 0.5", W: 7.33"):**
- Fill `#1E2435`, left accent `#E05C5C`
- Title: `SINGLE IMMERSION` Barlow SemiBold 16 pt `#E05C5C`
- Efficiency: `~90% drag-out removal` JetBrains Mono 14 pt `#E05C5C`
- Content: `Minimum acceptable. Water stagnates. Contamination builds quickly. Must be dumped frequently. NOT recommended for hardcoat.` Inter Regular 12 pt `#F0EDE8`

**Dual Cascade (X: 8.33", W: 7.33"):**
- Fill `#1E2435`, left accent `#27AE60`
- Title: `DUAL CASCADE` Barlow SemiBold 16 pt `#27AE60`
- Efficiency: `~99% drag-out removal` JetBrains Mono 14 pt `#27AE60`
- Content: `RECOMMENDED for hardcoat. Counter-flow design: fresh water enters clean tank, overflows to dirty tank, drains to waste. 10x better than single immersion.` Inter Regular 12 pt `#F0EDE8`

**Spray Rinse (X: 16.16", W: 7.33"):**
- Fill `#1E2435`, left accent `#2EC4B6`
- Title: `SPRAY RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Efficiency: `~95--99% drag-out removal` JetBrains Mono 14 pt `#2EC4B6`
- Content: `Excellent for flat parts. Uses less water than immersion. Can supplement cascade. May not reach blind holes or recesses.` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 6 -- Hardcoat-Specific Rinse Rules

**Section label:** `TYPE III RINSE -- KEY RULES` Barlow Condensed ExtraBold 22 pt. Y: 26.7".

Callout box, full width, fill `#1E2435`, left accent `#E8A020`:

- `1. Cascade rinse preferred -- single immersion is NOT adequate for hardcoat` Inter Medium 14 pt `#F0EDE8`
- `2. Dwell 10--15 sec above cleaner tank to drain before entering rinse` Inter Medium 14 pt `#F0EDE8`
- `3. Agitate parts in rinse -- move rack up and down 3--5 times` Inter Regular 13 pt `#F0EDE8` at 80%
- `4. Conductivity monitoring recommended: <200 uS/cm minimum, <50 uS/cm for aerospace` Inter Regular 13 pt `#F0EDE8` at 80%
- `5. If etch step is SKIPPED (precision parts), this rinse feeds directly into desmut -- extra thoroughness required` Inter Regular 13 pt `#E8A020`
- `6. Water temperature: ambient. No heating required.` Inter Regular 13 pt `#F0EDE8` at 80%

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Etch) -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values. Rinse water quality requirements vary by specification. Consult your process supplier and applicable spec for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type III Pre-Treatment -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinse posters are the hardest to make visually engaging because the process is simple. The drag-out chemistry chain (Zone 4) is the hero concept -- it shows why a "simple" rinse has outsized consequences for hardcoat. The rinse efficiency comparison gives actionable shop-floor guidance. The cascade rinse cross-section visual should be clear enough that a maintenance technician can verify their tank is plumbed correctly.

---

*Alaina -- Plating Posters Inc*
*Poster #289 -- Construction Workup v1.0*
*2026-04-26*
