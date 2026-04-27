---
Project: Plating Posters Inc
Poster Number: 305
Title: "Rinse (Pre-Etch) -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4)"
Process Scope: Pre-etch rinse for BSAA anodizing -- Stage 2 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Rinse
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #305 -- Construction Workup
## Rinse (Pre-Etch) -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 2 of 8. Standard pre-etch rinse -- same as Type I and Type II. Remove alkaline cleaner residue before the etch step. No BSAA-specific rinse requirements. The concept for this poster borrows from the Type III rinse (#289) -- the downstream contamination chain -- but adapted for BSAA's thin-oxide sensitivity and lower acid concentration.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse tank hero (Block B):** Dual cascade cross-section.
2. **Drag-out chain panel (Block D):** What cleaner drag-over does to BSAA's low-concentration bath.
3. **Rinse efficiency comparison (Block E):** Single vs. cascade vs. spray.
4. **BSAA-specific rinse notes (Block F).**

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
ZONE 4 -- DRAG-OUT CHAIN (14.5"--20.5" / ~6.0")
ZONE 5 -- RINSE EFFICIENCY COMPARISON (20.5"--26.5" / ~6.0")
ZONE 6 -- BSAA RINSE NOTES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing (BSAA) -- Stage 2 of 8 -- Pre-Etch` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Standard rinse. But BSAA runs at 3--5% acid -- half the concentration of Type II. Cleaner drag-over has proportionally more impact.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Part coated with alkaline cleaner residue  -->  After: Cleaner-free surface ready for etch`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE PRE-ETCH RINSE STATION` -- Y: 4.4".

**BLOCK B -- Dual Cascade Rinse Tank Cross-Section**

Same construction as Poster 289, adapted:
- Dual cascade tanks (Stage 1 dirty, Stage 2 clean)
- Overflow arrows, fresh water inlet, conductivity meter
- Parts moving from cleaner through rinse

**Parameter summary:**

| Parameter | Value |
|---|---|
| **Type** | Flowing ambient water rinse (city or DI) |
| **Temperature** | Ambient (60--85 F / 15--30 C) |
| **Time** | 30--60 sec immersion; or spray rinse |
| **Conductivity target** | < 200 uS/cm for commercial; < 50 uS/cm for aerospace |
| **Flow** | Counter-flow dual rinse preferred |

---

### ZONE 4 -- Drag-Out Chain

**Section label:** `WHAT CLEANER DRAG-OVER DOES TO BSAA` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 14.7".

**BLOCK D -- Downstream Contamination Chain**

Three connected callout boxes:

Box 1 -- Etch Tank:
- Left accent `#E8A020`
- Title: `ETCH TANK`
- Content: `Alkaline drag-over raises pH. Dilutes NaOH. Etch time for BSAA is already short (30--60 sec) -- any dilution changes the etch rate significantly.`

Box 2 -- BSAA Anodize Tank:
- Left accent `#E05C5C`
- Title: `BSAA ANODIZE TANK`
- Content: `BSAA runs at 3--5% H2SO4 (30--50 g/L) -- MUCH lower than Type II (15--20%). Cleaner surfactants cause foaming. Alkaline contamination neutralizes acid and shifts the H2SO4/H3BO3 balance. Dissolved aluminum accumulates faster in dilute baths.`

Box 3 -- Final Coating:
- Left accent `#E05C5C`
- Title: `FINAL COATING`
- Content: `Thin oxide, poor paint adhesion, corrosion failure. For a process designed to replace Type I in aerospace, this means rejected parts and potential NADCAP findings.`

Arrows between boxes: 2 pt `#3A4055`, right-pointing.

---

### ZONE 5 -- Rinse Efficiency Comparison

**Section label:** `RINSE METHODS -- EFFICIENCY COMPARISON` Barlow Condensed ExtraBold 22 pt. Y: 20.7".

Same three-column comparison as Poster 289:
- Single Immersion (90%, not recommended)
- Dual Cascade (99%, recommended)
- Spray Rinse (95--99%, supplemental)

---

### ZONE 6 -- BSAA Rinse Notes

**Section label:** `BSAA PRE-ETCH RINSE -- KEY NOTES` Barlow Condensed ExtraBold 22 pt. Y: 26.7".

**Two-column layout:**

**Left -- Rinse Rules (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`:
- `1. No special BSAA-specific rinse requirements` Inter Medium 14 pt `#F0EDE8`
- `2. Cascade rinse preferred over single immersion` Inter Medium 14 pt `#F0EDE8`
- `3. Dwell 10--15 sec above cleaner tank to drain` Inter Regular 13 pt `#F0EDE8` at 80%
- `4. Agitate parts in rinse -- move rack 3--5 times` Inter Regular 13 pt `#F0EDE8` at 80%
- `5. Conductivity monitoring recommended` Inter Regular 13 pt `#F0EDE8` at 80%
- `6. BSAA's low acid concentration means the anodize bath is less tolerant of contamination` Inter Regular 13 pt `#E8A020`

**Right -- BSAA vs. Type II Sensitivity (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`:

Title: `WHY BSAA IS MORE SENSITIVE` Barlow SemiBold 16 pt `#E8A020`

| Factor | Type II | BSAA |
|---|---|---|
| H2SO4 concentration | 15--20% (165--225 g/L) | 3--5% (30--50 g/L) |
| Buffer capacity | High -- tolerates some contamination | Low -- small changes shift bath chemistry |
| Dissolved Al tolerance | < 20 g/L | Lower -- tighter control needed |
| Effect of drag-in | Diluted by large acid volume | Amplified by small acid volume |

Header: Barlow SemiBold 11 pt. Data: JetBrains Mono 12 pt.

Below: `BSAA baths are smaller-volume and lower-concentration. The same drag-in that Type II shrugs off can shift BSAA chemistry enough to affect coating weight.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse (Pre-Etch) -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse water quality requirements vary by specification and facility. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse BSAA Pre-Treatment -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The BSAA rinse poster differentiates itself from the Type II and Type III rinse posters through the sensitivity comparison in Zone 6. BSAA's low acid concentration makes it the most contamination-sensitive anodize bath in the series. The drag-out chain (Zone 4) emphasizes this: the same cleaner residue that Type II absorbs without blinking can destabilize a BSAA bath. This is practical, non-obvious guidance that a shop transitioning from Type I to BSAA needs to hear.

---

*Alaina -- Plating Posters Inc*
*Poster #305 -- Construction Workup v1.0*
*2026-04-26*
