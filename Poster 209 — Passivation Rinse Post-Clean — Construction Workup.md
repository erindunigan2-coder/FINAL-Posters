---
Project: Plating Posters Inc
Poster Number: 209
Title: "Passivation (Stainless Steel) -- Rinse (Post-Clean)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.3)"
Technical Source: Rinse stage after alkaline cleaning (and after descaling pickle, if used) in stainless steel passivation lines. Covers water quality, chloride-free water requirements, and rinse verification.
Process Scope: Stainless steel passivation -- Stage 2 rinse (post-clean)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - Rinse
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #209 -- Construction Workup
## Passivation (Stainless Steel) -- Rinse (Post-Clean)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the post-clean rinse poster for CC-08. In passivation, the rinse stages carry an additional burden: they must be chloride-free. Chloride in rinse water is just as dangerous as chloride in the cleaner -- it contacts the stainless steel surface and can initiate pitting during the subsequent passivation step when the protective oxide is being actively dissolved and reformed.

For aerospace and medical parts, DI or RO water is mandatory. For general industrial passivation, low-chloride water (< 25 ppm Cl-) is the minimum standard.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set (text boxes, rounded rectangles, arrows, exact hex fills, print-quality export).

### Limitations to Flag

1. **Stage detail panel (Block B -- HERO):** Parameters, chloride-free water requirement.
2. **Water quality for passivation rinsing (Block C):** Chloride limits and testing.
3. **Double rinse protocol (Block D):** Why two rinse stages are standard for critical parts.
4. **Pickle rinse addendum (Block E):** Special requirements when descaling pickle was used.
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
  Block B: Stage detail panel
  Block C: Water quality requirements (chloride focus)

ZONE 3 -- DOUBLE RINSE PROTOCOL (15.5"--22.0" / ~6.5" tall)
  Block D: Why and when to use double rinse stages

ZONE 4 -- PICKLE RINSE ADDENDUM (22.0"--28.5" / ~6.5" tall)
  Block E: Special rinse requirements after descaling pickle (HNO3/HF)

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
- Text: `Stage 2 -- Rinse (Post-Clean)`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Chloride-free water. Every rinse. Every time. The same ion that causes pitting hides in your water supply.`
- Y: 2.2"

---

### ZONE 2 -- Rinse Stage Detail (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `RINSE -- POST-CLEAN`

**BLOCK B -- Stage Detail Panel**

Y: 3.8" to 8.5". Full width.

Large rounded rectangle: X: 0.5", Y: 3.8", W: 23.0", H: 4.5", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge: `STAGE 2 -- RINSE` fill `#2EC4B6`

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
```
Water:           Fresh water; DI or RO for aerospace/medical
Temperature:     Ambient to warm
Conductivity:    < 500 uS/cm (< 50 uS/cm for DI)
Chloride:        < 25 ppm general; < 5 ppm aerospace/medical
Method:          Overflow immersion or spray
Time:            1--2 min
```

Purpose callout (right side):
- Rounded rect, fill `#252B3D`, top accent `#27AE60`
- Title: `PURPOSE` -- Barlow SemiBold, 16 pt, `#27AE60`
- Text: `Remove ALL cleaner residues (and pickle acid, if used) before passivation. Prevent chemical carryover into the passivation bath that wastes acid and contaminates the bath.`

Chloride callout (right side, below purpose):
- Rounded rect, fill `#252B3D`, top accent `#E05C5C`
- Title: `CHLORIDE IN WATER` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Text: `Municipal water contains 10--250+ ppm chloride. This is enough to pit stainless steel during passivation. Test your water supply. Use DI or RO for critical parts.`

---

**BLOCK C -- Water Quality Requirements**

Y: 9.0" to 15.0". Two panels.

**Left -- Water Quality Specs:**
- Rounded rect, X: 0.5", Y: 9.0", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#27AE60`
- Title: `WATER QUALITY SPECIFICATIONS` -- Barlow SemiBold, 18 pt, `#27AE60`

Table:
| Parameter | General Industrial | Aerospace / Medical |
|---|---|---|
| Chloride (Cl-) | < 25 ppm | < 5 ppm |
| Conductivity | < 500 uS/cm | < 50 uS/cm |
| Sulfate (SO4 2-) | < 100 ppm | < 25 ppm |
| pH | 5.5--8.0 | 6.0--7.5 |
| Water type | Low-Cl tap or softened | DI or RO |

Data: JetBrains Mono 12 pt. Headers: Barlow SemiBold 13 pt.

**Right -- How to Test for Chloride:**
- Rounded rect, X: 12.0", Y: 9.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#E8A020`
- Title: `TESTING FOR CHLORIDE` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`):
```
Silver Nitrate Spot Test (Quick):
  - Add drops of 0.1N AgNO3 to water sample
  - White precipitate (AgCl) = chloride present
  - Heavier precipitate = higher chloride

Chloride Test Strips (Semi-Quantitative):
  - Dip strip in water; compare color to chart
  - Range: 0--500 ppm; sufficient for screening
  - Available from water testing suppliers

Ion Chromatography (Lab Method):
  - Most accurate; quantitative to < 1 ppm
  - Used for aerospace/medical qualification
  - Send sample to analytical lab
```

---

### ZONE 3 -- Double Rinse Protocol

**Section label:**
- Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DOUBLE RINSE -- WHEN AND WHY`

**BLOCK D -- Double Rinse Explanation**

Y: 16.3" to 21.8". Single wide panel with two sub-sections.

Rounded rect, X: 0.5", Y: 16.3", W: 23.0", H: 5.2", fill `#1E2435`, radius 8.

Left sub-section (X: 1.0" to 11.5"):
- Title: `WHEN TO DOUBLE RINSE` -- Barlow SemiBold, 18 pt, `#E8A020`
- Content (Inter Regular 14 pt `#F0EDE8`, bullets):
```
- Aerospace and medical parts (per AMS 2700)
- After descaling pickle (HNO3/HF residues)
- High-value components where rework cost exceeds
  water cost
- When single rinse conductivity exceeds target
- When processing mixed loads with heavy drag-out
```

Right sub-section (X: 12.0" to 23.0"):
- Title: `HOW IT WORKS` -- Barlow SemiBold, 18 pt, `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Stage 1 Rinse: Captures bulk drag-out.
  Higher conductivity; carries most contaminants.
  Periodically dump and refill.

Stage 2 Rinse: Final quality rinse.
  Low conductivity; chloride-free.
  DI or RO water feed.
  This is what the parts carry into passivation.

Counter-flow: Fresh DI enters Stage 2 and
overflows into Stage 1 for maximum efficiency.
```

---

### ZONE 4 -- Pickle Rinse Addendum

**Section label:**
- Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `SPECIAL RINSE AFTER DESCALING PICKLE`

**BLOCK E -- Pickle Rinse Requirements**

Y: 22.9" to 28.3". Two panels.

**Left -- Why Extra Rinsing:**
- Rounded rect, X: 0.5", Y: 22.9", W: 11.0", H: 5.0", fill `#1E2435`, left accent `#E05C5C`
- Title: `THE HF RISK` -- Barlow SemiBold, 20 pt, `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`):
```
If parts were descaled with HNO3/HF pickle,
the rinse MUST remove all HF residues.

HF trapped in crevices, blind holes, or
threaded areas will:
  1. Continue etching the stainless surface
  2. Cause localized pitting
  3. Contaminate the passivation bath
  4. Create operator safety hazards

Double rinse is MANDATORY after HF pickling.
Monitor rinse water for fluoride if possible.
```

**Right -- Rinse Protocol After Pickle:**
- Rounded rect, X: 12.0", Y: 22.9", W: 11.5", H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `RECOMMENDED PROTOCOL` -- Barlow SemiBold, 20 pt, `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`):
```
1. First rinse: Flowing water, 1--2 min
   - Removes bulk acid
   - May use tap water

2. Second rinse: DI or RO water, 1--2 min
   - Final quality rinse
   - Chloride-free
   - Conductivity < 50 uS/cm for critical parts

3. Verify: pH strip on part surface
   - Must read neutral (6.0--7.5)
   - If acidic, rinse again

4. Check crevices: Rotate parts to drain
   trapped acid from blind holes and threads
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as Poster #207.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | PITTING AFTER PASSIVATION | Chloride in rinse water (> 25 ppm) | Test water; switch to DI/RO; eliminate Cl sources |
| 2 | 6.33" | STAINING AFTER DRY | Alkaline residue carried into passivation; poor rinse | Double rinse; verify conductivity; check drain time |
| 3 | 12.16" | PASSIVATION BATH pH RISING | Excessive alkaline drag-over from cleaner | Improve rinse; reduce cleaner concentration |
| 4 | 18.0" | ETCHING FROM RESIDUAL HF | Pickle acid trapped in crevices; insufficient rinsing | Double rinse; rotate parts to drain; pH verify |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Rinse (Post-Clean)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical for rinse stages in stainless steel passivation lines per ASTM A967 and AMS 2700. Chloride-free rinsing is critical for stainless steel. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Rinse Post-Clean -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster reinforces the chloride message from Poster 208 but applies it specifically to water quality. The chloride testing section gives operators actionable methods -- from quick spot tests to lab IC analysis. The pickle rinse addendum addresses a real gap: many shops that pickle stainless before passivation do not rinse thoroughly enough, and the residual HF causes more damage than the heat tint it was supposed to remove.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #209 -- Construction Workup v1.0*
*2026-04-26*
