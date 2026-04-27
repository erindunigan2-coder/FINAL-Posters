---
Project: Plating Posters Inc
Poster Number: 647
Title: "Temper -- Martempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 10, Section 10.8)"
Technical Source: Martempering temper -- same temper parameters as conventional Q&T for the specific steel grade. Temperature range 300--1100 F depending on grade and target hardness. Double temper recommended for tool steels and retained austenite reduction. The temper is MANDATORY (unlike austempering where no temper is needed).
Process Scope: Martempering -- temper stage
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Martempering
  - Temper
  - ConstructionWorkup
  - ClusterHT10
---

# Poster #647 -- Construction Workup
## Temper -- Martempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The martempering temper is identical to any conventional Q&T temper -- same temperatures, same times, same metallurgy. The martensite formed during air cooling is the same martensite formed during a conventional oil quench. It just got there with less thermal gradient and therefore less distortion. The temper parameters come from the steel grade, not from the martempering process. This poster provides grade-specific temper data and makes the mandatory nature of the temper unmistakable -- because the one thing that distinguishes martempering from austempering at this stage is that martempering REQUIRES a temper.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **"Temper is mandatory" hero callout (Block B -- HERO):** Large, unmissable callout establishing that martensite must be tempered.
2. **Grade-specific temper table (Block C):** Common steels with their temper parameters and expected hardness.
3. **Double temper guidance (Block D):** When and why to double (or triple) temper.
4. **Temper vs. austempering comparison (Block E):** Why martempering needs temper and austempering doesn't.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- TEMPER MANDATORY + GRADE TABLE / HERO (4.2"--14.5" / ~10.3")
  Block B: Mandatory temper callout
  Block C: Grade-specific temper table
ZONE 4 -- DOUBLE TEMPER GUIDANCE (14.5"--22.0" / ~7.5")
  Block D: When to double temper
ZONE 5 -- TEMPER COMPARISON (22.0"--28.5" / ~6.5")
  Block E: Martempering vs. austempering temper requirements
ZONE 6 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `TEMPER` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Martempering -- Stage 8 of 9` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Martensite is martensite -- whether it formed by conventional quench or martempering. It MUST be tempered. Same steel, same temper parameters.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-quenched martensite from air cool -- maximum hardness, maximum brittleness  -->  After: Tempered martensite -- target hardness, improved toughness`

---

### ZONE 3 -- Temper Mandatory + Grade Table (HERO)

**BLOCK B -- Mandatory Temper Callout**

Y: 4.4" to 6.5". Full-width panel.

- Rounded rect W: 23.0", H: 1.8", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

Content (centered):
- Title: `TEMPER IS MANDATORY` -- Barlow Condensed ExtraBold 36 pt `#E05C5C`
- Text: `Unlike austempering (where bainite is the final structure and no temper is needed), martempering produces martensite -- which MUST be tempered to achieve the required toughness and relieve internal stress. Skipping temper = brittle parts = service failures.` -- Inter Medium, 15 pt, `#F0EDE8`

**BLOCK C -- Grade-Specific Temper Table**

Y: 7.0" to 14.3".

Section label: `TEMPER PARAMETERS BY STEEL GRADE` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 7.0".

Column widths (23.0" total):
- Grade (3.0") | Temper Temp F (C) (5.0") | Time (2.5") | Expected HRC (3.0") | Application (5.0") | Notes (4.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 13 pt `#F0EDE8`.

| Grade | Temper Temp | Time | HRC | Application | Notes |
|---|---|---|---|---|---|
| 1045 | 300--600 F (149--316 C) | 1--2 hr | 50--62 | Gears, shafts, pins | Single temper standard |
| 4140 | 400--1100 F (204--593 C) | 1--2 hr | 28--58 | General structural | Wide range per target |
| 4340 | 400--1100 F (204--593 C) | 1--2 hr | 30--56 | Aircraft, high-strength | Double temper for critical |
| 52100 | 300--350 F (149--177 C) | 2 hr | 60--62 | Bearings | Low temper to retain hardness |
| H13 | 1000--1050 F (538--566 C) | 2 hr x2 or x3 | 44--48 | Die casting dies | Double or triple temper |
| M2 (HSS) | 1025--1050 F (552--566 C) | 2 hr x2 or x3 | 63--65 | Cutting tools | Triple temper standard |
| D2 | 400--950 F (204--510 C) | 2 hr x2 | 56--62 | Blanking, stamping dies | Double temper minimum |

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.75".
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Grade: Inter Medium 13 pt. Notes: Inter Regular 11 pt `#E8A020`.

Note below table:
- `Temper parameters are identical to conventional Q&T for the same grade. The martempering process does not change the temper requirements -- only the as-quenched distortion level.` -- Inter Regular 12 pt `#F0EDE8` at 60%

---

### ZONE 4 -- Double Temper Guidance

**Section label:** `WHEN TO DOUBLE (OR TRIPLE) TEMPER` -- Y: 14.7".

**BLOCK D -- Double Temper Panel**

Y: 15.3" to 21.8". Two-column layout.

**Left -- When to Double Temper (X: 0.5", W: 11.0"):**

Rounded rect, H: 6.0", fill `#1E2435`, left accent 0.06" `#E8A020`, radius 6.

Title: `DOUBLE TEMPER` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`

Content (Inter Medium 13 pt `#F0EDE8`, line height 165%):
```
WHEN:
  Tool steels (H13, D2, A2, S7)
  High-speed steels (M2, M42, T15)
  Any grade with > 5% retained austenite
  Critical aerospace/bearing applications
  When specification requires it (AMS 2759)

WHY:
  First temper: relieves stress, tempers
  primary martensite, conditions retained
  austenite to transform on cooling

  Second temper: tempers the fresh martensite
  that formed from retained austenite during
  cooling from first temper
```

Key terms in JetBrains Mono Regular 13 pt `#E8A020`.

**Right -- Retained Austenite Explanation (X: 12.0", W: 11.5"):**

Rounded rect, H: 6.0", fill `#1E2435`, left accent 0.06" `#2EC4B6`, radius 6.

Title: `RETAINED AUSTENITE` -- Barlow Condensed ExtraBold, 22 pt, `#2EC4B6`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
WHAT IT IS:
  Austenite that did not transform to
  martensite during air cooling. Trapped
  in the microstructure.

WHY IT MATTERS:
  - Softer than martensite (reduces hardness)
  - Dimensionally unstable (transforms in
    service = dimensional changes)
  - Can transform under load = unexpected
    property changes

HOW TO REDUCE IT:
  1. Double or triple temper
  2. Sub-zero treatment (-100 to -320 F)
     between temper cycles
  3. Both (for maximum conversion)

TYPICAL RETAINED AUSTENITE:
  52100 as-quenched: 6--12%
  M2 as-quenched:    20--30%
  After double temper: < 5% (target)
```

Data values: JetBrains Mono Regular 12 pt `#2EC4B6`.

---

### ZONE 5 -- Temper Comparison

**Section label:** `WHY MARTEMPERING NEEDS TEMPER AND AUSTEMPERING DOESN'T` -- Y: 22.2".

**BLOCK E -- Comparison Panel**

Y: 22.9" to 28.3". Two side-by-side panels.

**Left -- Martempering (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#27AE60`, radius 6.

Title: `MARTEMPERING -- TEMPER REQUIRED` -- Barlow SemiBold, 18 pt, `#27AE60`

Content (Inter Medium 13 pt `#F0EDE8`):
```
Final structure: MARTENSITE
  - Body-centered tetragonal (BCT)
  - Supersaturated with carbon
  - Hard (60--65 HRC) but BRITTLE
  - Under extreme internal stress
  - Dimensionally unstable

Temper converts BCT martensite to
TEMPERED MARTENSITE:
  - Carbon precipitates as fine carbides
  - Stress relieved
  - Toughness dramatically improved
  - Hardness reduced (controllable)
  - Dimensionally stable
```

**Right -- Austempering (X: 12.0", W: 11.5"):**

Rounded rect, H: 5.0", fill `#1E2435`, left accent 0.06" `#E8A020`, radius 6.

Title: `AUSTEMPERING -- NO TEMPER NEEDED` -- Barlow SemiBold, 18 pt, `#E8A020`

Content (Inter Medium 13 pt `#F0EDE8`):
```
Final structure: BAINITE
  - Ferrite + carbide aggregate
  - NOT supersaturated -- carbon already
    precipitated during transformation
  - Tough at formation (no temper needed)
  - Lower internal stress than martensite
  - Dimensionally stable as-transformed

No temper needed because:
  - Bainite is already a STABLE structure
  - Carbon is already distributed in carbides
  - No BCT lattice strain to relieve
  - Tempering bainite has minimal effect
    (may even reduce toughness)
```

---

### ZONE 6 -- Footer

Standard footer. Title: `Temper -- Martempering`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Temper temperatures and times are grade-specific. Retained austenite percentages are typical ranges. Consult steel supplier data, AMS 2759, and your metallurgist for specification-compliant temper parameters. Source: General industry knowledge; ASM Handbook Vol. 4.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Temper Martempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "TEMPER IS MANDATORY" callout is deliberately oversized and in Coral because this is the most common conceptual error: operators who have worked with austempering assume martempering is the same and skip the temper. The grade-specific table gives actionable data -- an operator can look up their steel and get the temper parameters directly. The retained austenite explanation in Zone 4 answers the "why double temper?" question at the metallurgical level without requiring a materials science degree.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #647 -- Construction Workup v1.0*
*2026-04-26*
