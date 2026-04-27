---
Project: Plating Posters Inc
Poster Number: 213
Title: "Passivation (Stainless Steel) -- Rinse (Post-Acid)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.7)"
Technical Source: Post-acid rinse stage for stainless steel passivation. Covers removal of nitric or citric acid residues, trapped acid in crevices (the #1 cause of post-passivation staining), DI water for critical parts, and multi-stage rinsing.
Process Scope: Stainless steel passivation -- Stage 6 rinse (post-acid)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - Rinse
  - PostAcid
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #213 -- Construction Workup
## Passivation (Stainless Steel) -- Rinse (Post-Acid)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the post-acid rinse poster for CC-08. The single most common cause of post-passivation staining is trapped acid in crevices, blind holes, and threaded areas. This poster makes that message impossible to miss.

Nitric acid residue causes brown/orange staining. Citric acid residue promotes microbial growth. Both must be completely removed. For aerospace and medical parts, DI water and multi-stage rinsing are standard. For general industrial, thorough overflow rinsing with attention to geometry is sufficient.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set.

### Limitations to Flag

1. **Stage detail panel (Block B -- HERO):** Parameters and the trapped acid problem.
2. **Trapped acid locations (Block C):** Visual guide to where acid hides on parts.
3. **Rinse protocol by application (Block D):** General vs. aerospace vs. medical.
4. **Nitric vs. citric rinse considerations (Block E).**
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- RINSE STAGE DETAIL / HERO (2.9"--15.5" / ~12.6" tall)
  Block B: Stage detail panel (parameters, trapped acid problem)
  Block C: Where acid hides -- part geometry guide

ZONE 3 -- RINSE PROTOCOL BY APPLICATION (15.5"--22.0" / ~6.5" tall)
  Block D: General / aerospace / medical rinse specs

ZONE 4 -- NITRIC vs. CITRIC RINSE CONSIDERATIONS (22.0"--28.5" / ~6.5" tall)
  Block E: Different residue risks for each acid type

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#2EC4B6` (Teal)
- Text: `Stage 6 -- Rinse (Post-Acid)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Trapped acid in crevices is the #1 cause of post-passivation staining. Rinse thoroughly. Rotate parts. Check blind holes.`
- Y: 2.2"

---

### ZONE 2 -- Rinse Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE -- POST-ACID`

---

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 8.5". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge: `STAGE 6 -- POST-ACID RINSE` fill `#2EC4B6`

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
```
Water:           Fresh water; DI for aerospace/medical
Temperature:     Ambient to warm
Method:          Overflow immersion; multiple stages for critical parts
Time:            1--3 min per stage
Chloride:        < 25 ppm general; < 5 ppm aerospace
```

Purpose callout (right side):
- Rounded rect, fill `#252B3D`, top accent `#27AE60`
- Title: `PURPOSE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Text: `Remove ALL acid residues from the passivation bath. Nitric acid residue causes staining and continued etching. Citric acid residue promotes microbial growth. Both must be completely removed.`

Trapped acid callout (right side, below):
- Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `#1 FAILURE MODE` -- Barlow Condensed ExtraBold, 18 pt, `#E05C5C`
- Text: `Trapped acid in crevices, blind holes, threads, and lap joints. The acid continues to etch the stainless in a concentrated, localized area -- causing brown staining that appears hours or days after passivation.` -- Inter Medium 14 pt `#F0EDE8`

---

**BLOCK C -- Where Acid Hides**

Y: 9.0" to 15.0". Six location cards in a 3x2 grid.

Each card: Rounded rect, W: 7.33", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Row 1 (Y: 9.0"):
| Card | X | Location | Prevention |
|---|---|---|---|
| 1 | 0.5" | BLIND HOLES | Acid fills the hole but does not drain. Rotate parts 180 degrees during rinse to drain. Air blow if needed. |
| 2 | 8.08" | THREADED HOLES | Acid wicks into threads by capillary action. Requires extended soak rinse + air blow to displace. |
| 3 | 15.67" | LAP JOINTS / SEAMS | Acid enters the overlap and will not drain without mechanical assistance. Separate or open if possible. |

Row 2 (Y: 12.2"):
| Card | X | Location | Prevention |
|---|---|---|---|
| 4 | 0.5" | INSIDE TUBES | Acid fills the tube interior; horizontal tubes trap acid at low points. Flush with rinse water. |
| 5 | 8.08" | UNDER RUBBER FIXTURES | Masking materials, plugs, and rubber pads trap acid underneath. Remove fixtures before rinsing. |
| 6 | 15.67" | WELD ROOTS / CREVICES | Weld root gaps and crevice geometries trap acid indefinitely. Multi-stage rinse + extended soak. |

Interior per card:
- Location: Barlow SemiBold 14 pt `#E05C5C`
- Prevention: Inter Regular 12 pt `#F0EDE8`

---

### ZONE 3 -- Rinse Protocol by Application

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE PROTOCOL -- BY APPLICATION`

**BLOCK D -- Three Application Panels**

Y: 16.3" to 21.8". Three panels.

**General Industrial:**
- Rounded rect, X: 0.5", Y: 16.3", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `GENERAL INDUSTRIAL` -- Barlow SemiBold, 18 pt, `#2EC4B6`

```
Rinse stages:  1--2 (overflow immersion)
Water:         Low-chloride tap or softened
Conductivity:  < 500 uS/cm
Time:          1--2 min per stage
Drain check:   Rotate parts to drain blind holes
Verification:  pH strip on surface (neutral)
```

**Aerospace (AMS 2700):**
- Rounded rect, X: 8.08", Y: 16.3", W: 7.33", H: 5.2", fill `#1E2435`, left accent `#E8A020`
- Title: `AEROSPACE (AMS 2700)` -- Barlow SemiBold, 18 pt, `#E8A020`

```
Rinse stages:  2--3 (counter-flow + DI final)
Water:         DI or RO (Cl- < 5 ppm)
Conductivity:  < 50 uS/cm final rinse
Time:          2--3 min per stage
Drain check:   Rotate + air blow blind holes
Verification:  pH + conductivity at surface
Additional:    Parts may require ultrasonic rinse
               for complex geometries
```

**Medical / Pharmaceutical:**
- Rounded rect, X: 15.67", Y: 16.3", W: 7.83", H: 5.2", fill `#1E2435`, left accent `#27AE60`
- Title: `MEDICAL / PHARMA` -- Barlow SemiBold, 18 pt, `#27AE60`

```
Rinse stages:  3+ (DI water all stages)
Water:         High-purity DI (Cl- < 1 ppm)
Conductivity:  < 10 uS/cm
Time:          2--5 min per stage
Drain check:   Mandatory rotation + air blow
Verification:  pH, conductivity, residual ion test
Standards:     ASTM F86 (surgical implants)
Additional:    Cleanroom-compatible handling
```

---

### ZONE 4 -- Nitric vs. Citric Rinse Considerations

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE DIFFERENCES -- NITRIC vs. CITRIC RESIDUES`

**BLOCK E -- Two Panels**

Y: 22.9" to 28.3".

**Left -- Nitric Acid Residues:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `AFTER NITRIC ACID` -- Barlow SemiBold, 20 pt, `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`):
```
Residue risk:
  Brown/orange staining from trapped HNO3
  continuing to etch stainless in crevices

Rinse urgency: HIGH
  Nitric acid continues etching until removed
  Concentrated residue attacks even resistant alloys

If dichromate was used (Nitric 1):
  Cr6+ residue is hazardous
  Rinse water must be treated as hazardous waste
  Thorough multi-stage rinsing is mandatory

Smell test: If you can smell HNO3 on parts
after rinsing, they are not rinsed enough
```

**Right -- Citric Acid Residues:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `AFTER CITRIC ACID` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`):
```
Residue risk:
  Microbial growth -- citric acid is an organic
  compound; bacteria thrive in citric residue
  Possible light staining from iron-citrate complex

Rinse urgency: MODERATE
  Citric acid is much milder than nitric
  Residue is less aggressive but still needs removal

Special consideration:
  Citric acid residue is biodegradable but can
  promote biofilm formation on medical/pharma parts
  if not completely removed

  For biomedical applications, multi-stage DI rinse
  is mandatory to eliminate organic residue
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | BROWN STAINING (DELAYED) | Trapped acid in crevices; appears hours/days later | Improve rinse technique; rotate parts; air blow blind holes |
| 2 | 6.33" | CHLORIDE PITTING | Chloride in rinse water contacting freshly passivated surface | Switch to DI/RO; test rinse water for chloride |
| 3 | 12.16" | STREAKING / TIDE MARKS | Uneven rinse; parts partially submerged; slow withdrawal | Full immersion; smooth withdrawal; adequate overflow |
| 4 | 18.0" | ACID SMELL ON PARTS | Insufficient rinsing; no second rinse stage | Add second rinse; increase rinse time; check overflow |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Rinse (Post-Acid)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse parameters shown are typical for post-passivation rinsing of stainless steel per ASTM A967 and AMS 2700. Water quality and rinsing requirements vary by specification and application. Consult your process supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Rinse Post-Acid -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "where acid hides" grid in Zone 2 is the most operationally valuable section on this poster. Every passivation technician has seen the delayed brown stain that appears 24 hours after "successful" passivation -- and the cause is almost always trapped acid in a blind hole or thread. This poster makes those geometry traps visible and provides actionable prevention (rotate, air blow, extended soak).

The nitric vs. citric rinse comparison in Zone 4 highlights a rarely discussed difference: citric acid's microbial growth risk. This is important for medical/pharma shops.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #213 -- Construction Workup v1.0*
*2026-04-26*
