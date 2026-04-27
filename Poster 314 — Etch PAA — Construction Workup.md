---
Project: Plating Posters Inc
Poster Number: 314
Title: "Etch -- PAA"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.4)"
Technical Source: Etch / surface preparation stage for PAA. Multiple approaches -- alkaline etch, grit blast, FPL etch (legacy Cr6+), and P2 etch (Cr6+-free replacement). Choice depends on specification and whether Cr6+ is permitted.
Process Scope: Etch -- Stage 3 of PAA sequence
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - Etch
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #314 -- Construction Workup
## Etch -- PAA

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of the PAA sequence. The etch step for PAA is more nuanced than for decorative anodizing because multiple pre-treatment paths exist -- alkaline etch, grit blast, FPL etch (legacy), and P2 etch (modern Cr6+-free). The poster must present all four options clearly and help the operator understand which path their specification calls for.

Hero visual: a four-path decision diagram showing the four etch approaches with parameters for each.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four-path decision hero (Block B):** Four parallel paths from "cleaned surface" to "ready for desmut," each with parameters. Built with rectangles, arrows, and text.
2. **FPL etch detail panel (Block D):** Legacy chromic-sulfuric acid etch -- with prominent Cr6+ warning.
3. **Grit blast detail panel (Block E):** Mechanical prep option.
4. **Alloy behavior table (Block F):** How different alloys respond to each etch method.
5. **Failure modes strip (Block G):** 4 etch failures.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- FOUR-PATH DECISION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- FPL ETCH + P2 ETCH DETAIL (14.5"--20.5" / ~6.0")
ZONE 5 -- ALKALINE ETCH + GRIT BLAST DETAIL (20.5"--26.5" / ~6.0")
ZONE 6 -- ALLOY BEHAVIOR + FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ETCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Surface Preparation -- Stage 3 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Four paths to the same destination -- a uniform surface for PAA oxide growth. Know which one your spec requires.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean aluminum surface  -->  After: Uniform, activated surface ready for desmut`

---

### ZONE 3 -- Four-Path Decision Hero

**Section label:** `FOUR PRE-TREATMENT PATHS` -- Y: 4.4".

**BLOCK B -- Four Parallel Path Cards**

Y: 5.0" to 14.0". Four cards arranged in a 2x2 grid.

Each card: Rounded rect, W: 11.0", H: 4.0", fill `#1E2435`, radius 6.

**Row 1 (Y: 5.0" to 9.2"):**

*Card 1 -- Alkaline Etch (X: 0.5"):*
- Top accent: 4 pt `#E8A020`
- Badge: `OPTION A` Barlow Condensed ExtraBold 14 pt `#1A1F2E` on `#E8A020` pill
- Title: `ALKALINE ETCH (STANDARD)` Barlow SemiBold 20 pt `#E8A020`
- Parameters (JetBrains Mono 13 pt `#F0EDE8`):
```
NaOH 40--60 g/L (5--8 oz/gal)
55--60 C (130--140 F)
1--3 min
```
- When to use: `Standard option when FPL/P2 not specified` Inter Regular 13 pt `#F0EDE8` at 70%
- Pros: `Simple, proven, widely available` Inter Medium 12 pt `#27AE60`
- Cons: `Produces smut on Cu-bearing alloys; requires desmut` Inter Medium 12 pt `#E05C5C`
- Reaction: `2Al + 2NaOH + 2H2O -> 2NaAlO2 + 3H2` JetBrains Mono 11 pt `#F0EDE8` at 60%

*Card 2 -- FPL Etch (X: 12.0"):*
- Top accent: 4 pt `#E05C5C`
- Badge: `OPTION B` + `LEGACY -- Cr6+` Barlow Condensed ExtraBold 14 pt `#1A1F2E` on `#E05C5C` pill
- Title: `FPL ETCH (CHROMIC-SULFURIC)` Barlow SemiBold 20 pt `#E05C5C`
- Parameters:
```
Na2Cr2O7 60 g/L + H2SO4 300 g/L
60--70 C (140--160 F)
10--12 min
```
- When to use: `Legacy aerospace specs; best bond performance data` Inter Regular 13 pt `#F0EDE8` at 70%
- Pros: `Gold standard for bond strength; etch + desmut in one step` Inter Medium 12 pt `#27AE60`
- Cons: `Contains Cr6+ -- being phased out worldwide` Inter Medium 12 pt `#E05C5C`
- Warning: `HEXAVALENT CHROMIUM: OSHA PEL 0.005 mg/m3` Inter Medium 12 pt `#E05C5C`

**Row 2 (Y: 9.8" to 14.0"):**

*Card 3 -- P2 Etch (X: 0.5"):*
- Top accent: 4 pt `#27AE60`
- Badge: `OPTION C` + `Cr6+-FREE` Barlow Condensed ExtraBold 14 pt `#1A1F2E` on `#27AE60` pill
- Title: `P2 ETCH (Cr6+-FREE REPLACEMENT)` Barlow SemiBold 20 pt `#27AE60`
- Parameters:
```
Proprietary (Fe2(SO4)3 + H2SO4-based)
Temperature per TDS
Time per TDS
```
- When to use: `Modern replacement for FPL; Boeing-qualified alternatives exist` Inter Regular 13 pt `#F0EDE8` at 70%
- Pros: `No Cr6+; similar performance to FPL` Inter Medium 12 pt `#27AE60`
- Cons: `Proprietary; must be validated per OEM spec` Inter Medium 12 pt `#E8A020`

*Card 4 -- Grit Blast (X: 12.0"):*
- Top accent: 4 pt `#2EC4B6`
- Badge: `OPTION D` Barlow Condensed ExtraBold 14 pt `#1A1F2E` on `#2EC4B6` pill
- Title: `GRIT BLAST (MECHANICAL)` Barlow SemiBold 20 pt `#2EC4B6`
- Parameters:
```
180--220 grit alumina
30--40 psi
Followed by alkaline clean + light etch
```
- When to use: `When specification permits mechanical prep; often combined with chemical etch` Inter Regular 13 pt `#F0EDE8` at 70%
- Pros: `No chemistry; consistent surface roughness` Inter Medium 12 pt `#27AE60`
- Cons: `Grit embedment risk; requires clean compressed air` Inter Medium 12 pt `#E8A020`

---

### ZONE 4 -- FPL Etch + P2 Etch Detail

**Section label:** `CHEMICAL ETCH DETAIL` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- FPL Etch (Legacy) (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `FPL ETCH -- THE LEGACY GOLD STANDARD` Barlow SemiBold 18 pt `#E05C5C`

| Parameter | Value |
|---|---|
| Na2Cr2O7 | 60 g/L |
| H2SO4 | 300 g/L |
| Temperature | 60--70 C (140--160 F) |
| Time | 10--12 min |
| Etch + Desmut | Combined -- no separate desmut needed |

Safety callout (Coral):
> CONTAINS Cr6+: confirmed human carcinogen. Full engineering controls, respiratory protection, medical surveillance required. EPA hazardous waste (D007).

**Right -- P2 Etch (Modern) (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `P2 ETCH -- THE Cr6+-FREE FUTURE` Barlow SemiBold 18 pt `#27AE60`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> P2-type etches are proprietary formulations designed to match FPL bond performance without hexavalent chromium.
>
> -- Typically ferric sulfate + sulfuric acid based
> -- Boeing and other OEMs have qualified specific products
> -- Must be validated against the applicable bond test specification (ASTM D3762 wedge test)
> -- Separate desmut step may be required (unlike FPL)
>
> The P2 etch is where the industry is heading. If your spec still calls for FPL, ask about qualified P2 alternatives.

---

### ZONE 5 -- Alkaline Etch + Grit Blast Detail

**Section label:** `MECHANICAL + ALKALINE PREP` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Alkaline Etch Detail (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ALKALINE ETCH` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Chemistry | NaOH (sodium hydroxide) |
| Concentration | 40--60 g/L (5--8 oz/gal) |
| Temperature | 55--60 C (130--140 F) |
| Time | 1--3 min (alloy-dependent) |
| Etch rate | ~0.5--1.0 mil/min on 6061 |
| H2 evolution | Vigorous -- ventilation required |

Note: `Produces etch smut on Cu/Zn alloys -- MUST be followed by desmut step` Inter Medium 13 pt `#E8A020`

**Right -- Grit Blast Detail (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `GRIT BLAST` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Media | Alumina (Al2O3), 180--220 grit |
| Pressure | 30--40 psi |
| Angle | 45--90 degrees to surface |
| Distance | 6--12 inches |
| Compressed air | Must be oil-free and dry |
| Post-blast | Alkaline clean + light etch to remove embedded grit |

Note: `Never use steel shot or glass bead -- ferrous/silica contamination ruins PAA oxide` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Alloy Behavior + Failure Modes

**Section label:** `ALLOY RESPONSE + FAILURE MODES` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Alloy Etch Response (X: 0.5", W: 11.0"):**
- Title: `ALLOY BEHAVIOR IN ETCH` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Alloy | Etch Notes |
|---|---|
| 6061 / 6063 | Standard etch; 2--3 min; uniform matte |
| 2024 | Heavy dark Cu smut; shorter etch (1--2 min); aggressive desmut mandatory |
| 7075 | Zn + Cu smut; slightly faster etch; shorter time |
| Cast (high Si) | Caustic does NOT dissolve Si particles; mechanical prep preferred |

4-row table, alternating `#1E2435` / `#252B3D`. Data: Inter Regular 12 pt.

**Right -- Failure Modes (X: 12.0", W: 11.5"):**
- Title: `ETCH FAILURE MODES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Failure | Cause | Bond Impact |
|---|---|---|
| Over-etching | Excessive time/temp | Pitting; H-embrittlement risk; weakened substrate |
| Under-etching | Short time; cold bath | Mill finish variation visible; non-uniform oxide |
| Residual smut | Inadequate desmut follow-up | Smut blocks oxide growth; bond failure |
| Streaking | Cleaner dragover; non-uniform immersion | Non-uniform PAA oxide; weak bond zones |

4-row table with Coral left accent. Data: Inter Regular 12 pt.

---

### ZONE 7 -- Footer

Standard. Title: `Etch -- Phosphoric Acid Anodizing (PAA)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933; Boeing BAC 5555. Etch parameters shown are typical values. FPL and P2 etch formulations are specification-controlled -- consult applicable OEM specifications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch PAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The four-path hero is the centerpiece. Many operators do not realize there are multiple etch options for PAA -- they default to whatever their line runs. This poster helps them understand the landscape and why different specs call for different approaches. The FPL-to-P2 transition is an active industry shift, so giving it prominent space is timely. The Cr6+ warnings on the FPL card must be impossible to miss.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #314 -- Construction Workup v1.0*
*2026-04-26*
