---
Project: Plating Posters Inc
Poster Number: 621
Title: "Inspection & QA -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.8)"
Technical Source: Inspection and quality assurance for induction-hardened parts -- hardness testing, case depth measurement (acid etch and microhardness traverse), pattern verification, magnetic particle inspection (MPI), and dimensional check. Pattern verification by acid etch is unique to induction and the single most important QA step.
Process Scope: Induction hardening -- inspection and quality assurance
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - InductionHardening
  - Inspection
  - QualityAssurance
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #621 -- Construction Workup
## Inspection & QA -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Inspection of induction-hardened parts has one element that furnace-hardened parts do not: pattern verification. In furnace hardening, the entire surface is treated uniformly. In induction, only the area exposed to the coil is hardened -- and the boundary between hardened and unhardened zones must be verified. A hardness test tells you how hard. A pattern check tells you where. Both are non-negotiable.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Inspection methods grid (Block B -- HERO):** Five inspection methods with descriptions, standards, and when each is required.
2. **Pattern verification deep-dive (Block D):** Acid etch process, what to look for, common pattern defects.
3. **Common defects table (Block E):** Defect-cause-remedy reference.
4. **First-article inspection callout (Block F):** Why first-article is critical for induction.

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
  Stage 9 highlighted (Emerald)
ZONE 3 -- INSPECTION METHODS / HERO (4.2"--14.5" / ~10.3")
  Block B: Five inspection method cards
  Block C: "Pattern + Hardness + Depth" triad callout
ZONE 4 -- PATTERN VERIFICATION (14.5"--22.0" / ~7.5")
  Block D: Acid etch deep-dive + pattern defect examples
ZONE 5 -- DEFECTS TABLE + FIRST-ARTICLE (22.0"--32.5" / ~10.5")
  Block E: Common defects table
  Block F: First-article inspection callout
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & QA` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Stage 9 of 9` -- 36 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Hardness tells you how hard. Pattern tells you where. Case depth tells you how deep. All three are mandatory.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Tempered part  -->  After: Verified conforming part released to next operation`

---

### ZONE 3 -- Inspection Methods (HERO)

**Section label:** `FIVE INSPECTION METHODS -- ALL MAY BE REQUIRED` -- Y: 4.4".

**BLOCK B -- Five Inspection Cards**

Y: 5.0" to 12.5". Two rows: Row 1 = three cards, Row 2 = two cards centered.

Each card: Rounded rect W: 7.33", H: 3.5", fill `#1E2435`, radius 8, left accent 0.06".

| Pos | Method | Accent | Standard | What It Measures | When Required |
|---|---|---|---|---|---|
| R1C1 | SURFACE HARDNESS | `#27AE60` | ASTM E18 (Rockwell) | Surface HRC at specified locations; minimum typically 55--58 HRC depending on carbon content | Every part (production) or per sampling plan |
| R1C2 | CASE DEPTH | `#E8A020` | ASTM E384 / SAE J423 | Depth from surface to 50 HRC equivalent; measured by microhardness traverse on cross-section | First article + periodic per spec |
| R1C3 | PATTERN VERIFICATION | `#2EC4B6` | AMS 2759/12 | Location and extent of hardened zone; verified by acid etch on cross-section (10% ammonium persulfate or 5% nital) | First article mandatory; periodic thereafter |
| R2C1 | CRACK DETECTION (MPI) | `#E05C5C` | ASTM E1444 | Surface and near-surface cracks; magnetic particle inspection with UV light | 100% on safety-critical parts; per spec otherwise |
| R2C2 | DIMENSIONAL CHECK | `#C8D0D8` | Per drawing | OD growth (0.0002--0.001 in typical due to martensite expansion); runout; straightness | Per sampling plan; 100% for precision parts |

Grid positions:
- Row 1: Y: 5.0". X: 0.5" / 8.17" / 15.83"
- Row 2: Y: 9.0". X: 4.33" / 12.0"

Card interior:
- Method name: Barlow SemiBold 16 pt, accent color
- Standard: JetBrains Mono Regular 11 pt `#F0EDE8` at 60%
- What it measures: Inter Regular 13 pt `#F0EDE8`
- When required: Inter Medium 12 pt, accent color

**BLOCK C -- Triad Callout**

Y: 12.8" to 14.3". Full-width callout.
- Rounded rect W: 23.0", H: 1.3", fill `#1E2435`, left accent 0.06" `#27AE60`
- Text: `THE INDUCTION QA TRIAD: Pattern (WHERE is it hard?) + Hardness (HOW hard?) + Case Depth (HOW deep?). All three must be verified. A part can pass hardness but fail pattern. A part can pass pattern but have insufficient depth. Test all three.` -- Inter Medium 14 pt `#F0EDE8`

---

### ZONE 4 -- Pattern Verification

**Section label:** `PATTERN VERIFICATION -- THE INDUCTION-SPECIFIC INSPECTION` -- Y: 14.7".

**BLOCK D -- Two-panel layout**

**Left -- Acid Etch Process (X: 0.5", W: 11.0"):**

- Rounded rect H: 6.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `ACID ETCH PATTERN CHECK` -- Barlow SemiBold 18 pt `#2EC4B6`

Steps (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
1. Section part through the hardened zone
   (destructive test -- use test coupon
   or sacrificial part from same setup)

2. Mount and polish cross-section
   (standard metallographic preparation)

3. Etch with:
   - 10% ammonium persulfate (room temp), OR
   - 5% nital (2--5% nitric acid in ethanol)

4. Hardened zone appears DARK against the
   lighter unhardened core

5. Measure:
   - Pattern location (matches drawing?)
   - Pattern depth (matches case depth spec?)
   - Transition zone width and shape
   - Symmetry (uniform around circumference?)
```

Data: JetBrains Mono Regular 13 pt `#2EC4B6`. Body: Inter Regular 13 pt `#F0EDE8`.

**Right -- Pattern Defect Examples (X: 12.0", W: 11.5"):**

- Rounded rect H: 6.5", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `PATTERN DEFECTS -- WHAT TO LOOK FOR` -- Barlow SemiBold 18 pt `#E05C5C`

| Defect | What You See | Likely Cause |
|---|---|---|
| Asymmetric pattern | One side deeper than the other | Part off-center in coil; coupling gap uneven |
| Pattern too shallow | Dark zone thinner than spec | Frequency too high; power too low; time too short |
| Pattern too deep | Dark zone exceeds spec | Frequency too low; time too long; through-hardened |
| Sharp transition | Abrupt boundary; stress riser | Quench too severe at boundary; may crack in service |
| Unintended hardening | Dark zone extends beyond target area | Stray flux heating adjacent zones; coil design issue |
| No pattern visible | Uniform etch across section | Through-hardened (entire section austenitized) or not hardened at all |

Header: Barlow SemiBold 12 pt `#F0EDE8`. Data: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 5 -- Defects Table + First-Article

**Two-column layout (Y: 22.2" to 32.3"):**

**Left -- Common Defects (X: 0.5", W: 11.0"):**

Section label: `COMMON DEFECTS -- CAUSE AND REMEDY` Barlow Condensed ExtraBold 24 pt.

Table (Y: 23.0" to 31.0"):

| Defect | Cause | Remedy |
|---|---|---|
| Soft spots | Part off-center; decarburized surface; scale | Center part; verify stock; remove scale |
| Through-hardening | Freq too low; power too high; time too long | Increase frequency; reduce power/time |
| Cracking | Too-rapid quench; too-deep case; sharp corners | Reduce quench severity; radius transitions |
| Non-uniform pattern | Coil design; coupling gap variation; geometry | Redesign coil; verify fixturing |
| Overheating (grain growth) | Power too high; dwell too long | Reduce power; verify control system |
| OD growth out of spec | Excessive martensite volume | Reduce case depth if possible; adjust tolerance |

Header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`, H: 0.85".
Defect: Barlow SemiBold 12 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Remedy: Inter Medium 12 pt `#27AE60`.

**Right -- First-Article Inspection (X: 12.0", W: 11.5"):**

Section label: `FIRST-ARTICLE INSPECTION -- NON-NEGOTIABLE` Barlow Condensed ExtraBold 24 pt `#27AE60`.

- Rounded rect H: 9.0", fill `#1E2435`, left accent 0.06" `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
WHY FIRST-ARTICLE IS CRITICAL:

Induction hardening is process-dependent --
the result depends on exact coil position,
coupling gap, power, time, and quench.

UNLIKE furnace hardening (where the entire
load sees the same conditions), induction
parameters can drift from part to part:
  - Coil wear changes the gap
  - Fixture wear changes positioning
  - Power supply drift affects temperature
  - Quench concentration changes daily

FIRST-ARTICLE PROTOCOL:
1. Run first part with production parameters
2. Section and acid etch for pattern
3. Microhardness traverse for case depth
4. Surface hardness at 3+ locations
5. MPI for cracks
6. Dimensional check
7. APPROVE before releasing production

FREQUENCY:
First article on every new setup, coil
change, power supply maintenance, or
new material lot.
```

Data: JetBrains Mono Regular 13 pt `#27AE60`. Body: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Inspection & QA -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Inspection requirements are governed by the applicable specification and customer requirements. Always follow your quality management system and customer-specific inspection plans. Source: General industry knowledge; ASM Handbook Vol. 4; AMS 2759/12; ASTM E18, E384, E1444.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection QA Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Pattern verification is the unique inspection content for induction hardening. Furnace processes do not have this concept because the entire part is uniformly treated. The acid etch process is simple but the interpretation requires training -- this poster provides the vocabulary for what to look for. The first-article callout is critical because induction is a setup-sensitive process. Small changes in the setup produce measurable changes in the result, and the only way to catch drift is rigorous first-article verification.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #621 -- Construction Workup v1.0*
*2026-04-26*
