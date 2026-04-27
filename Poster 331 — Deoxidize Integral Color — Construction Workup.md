---
Project: Plating Posters Inc
Poster Number: 331
Title: "Deoxidize -- Integral Color Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 7, Section 7.5)"
Technical Source: Industry-standard desmut/deoxidize step for aluminum anodizing. HNO3 is the standard chemistry for 6xxx alloys used in integral color. Parameters are typical ranges.
Process Scope: Integral color anodizing -- Stage 4 of 8 (Deoxidize/Desmut)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - IntegralColor
  - Deoxidize
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #331 -- Construction Workup
## Deoxidize -- Integral Color Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8 (mapped to poster stage "Deoxidize"). Removes the smut left by the caustic etch -- insoluble alloying element residues (copper, silicon, iron, manganese). For integral color on 6063, standard HNO3 desmut is sufficient. The poster covers standard and aggressive options.

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
  Stage 4 highlighted (Amber)
ZONE 3 -- DESMUT PROCESS HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CHEMISTRY BY ALLOY + ALTERNATIVES (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- HF SAFETY + STANDARDS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DEOXIDIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Integral Color Anodizing -- Stage 4 of 8` -- 34 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Smut is what the etch leaves behind -- insoluble residues from alloying elements. Remove it all, or it carries into the anodize tank and ruins the color.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Etched surface with smut residue --> After: Clean, bright aluminum ready for rinse and anodize`

---

### ZONE 3 -- Desmut Process Hero

**Section label:** `DESMUT / DEOXIDIZE -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Parameter Panel**

Y: 5.0" to 14.0". Large rounded rect, fill `#1E2435`.

**Left column (X: 1.0", W: 11.0") -- Standard Desmut (6xxx alloys):**

Title: `STANDARD DESMUT -- 6063 / 6061` Barlow SemiBold 18 pt `#27AE60`.

| Parameter | Value |
|---|---|
| Chemistry | Nitric acid (HNO3) |
| Concentration | 25--50% by volume (conc. HNO3 = 67--70%) |
| Temperature | Ambient (room temperature) |
| Time | 30--120 seconds |
| HF required? | NO -- not needed for 6xxx alloys |

Values: JetBrains Mono Regular, 15 pt, `#F0EDE8`.

Note below table: `For integral color on 6063 (the standard architectural alloy), simple HNO3 desmut is all that is needed. The smut from 6063 etch is light and dissolves readily in nitric acid.` Inter Regular 13 pt `#F0EDE8` at 70%.

**Right column (X: 12.5", W: 10.5") -- Aggressive Desmut (Cu-bearing alloys):**

Title: `AGGRESSIVE DESMUT -- 2xxx / 7xxx` Barlow SemiBold 18 pt `#E05C5C`.

| Parameter | Value |
|---|---|
| Chemistry | HNO3 + HF (mixed acid) |
| HNO3 | 25--50% by volume |
| HF | 1--3% by volume (40% HF) |
| Temperature | Ambient |
| Time | 60--180 seconds |
| Why HF? | Dissolves metallic copper and silicon particles |

Note: `HF is RARELY needed for integral color work because integral color is almost exclusively run on 6063 and 5005 -- not copper-bearing alloys.` Inter Medium 13 pt `#2EC4B6`.

**Key Callout (Y: 11.5"):**

Coral-accented callout:
- `WHY DESMUT MATTERS FOR INTEGRAL COLOR` Barlow SemiBold 16 pt `#E05C5C`
- `Smut carried into the integral color anodize bath contaminates the electrolyte with metal particles. These metals co-deposit into the oxide and cause mottled, inconsistent color.` Inter Regular 13 pt `#F0EDE8`

**Bottom callout (Y: 13.5"):**
- `Standard HNO3 desmut for 6063. Save the aggressive chemistry for copper alloys -- which should not be in integral color work anyway.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Chemistry by Alloy + Alternatives

**Section label:** `DESMUT CHEMISTRY -- MATCH TO YOUR ALLOY` -- Y: 14.7".

**Left (X: 0.5", W: 14.0") -- Alloy-Desmut Matrix:**

| Alloy | Desmut Chemistry | Time | Notes |
|---|---|---|---|
| 6063 | HNO3 25--50% | 30--120 sec | Standard for integral color |
| 6061 | HNO3 25--50% | 30--120 sec | Same as 6063 |
| 5005 | HNO3 25--50% | 30--90 sec | Light smut; fast desmut |
| 2024 | HNO3 + HF | 60--180 sec | Heavy copper smut; not typical for integral |
| 7075 | HNO3 + HF | 60--180 sec | Zinc + copper smut; not typical for integral |
| Cast (high Si) | HNO3 + HF (or mechanical) | 120--300 sec | Not recommended for integral color |

**Right (X: 15.0", W: 8.5") -- Proprietary Alternatives:**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `NON-HF ALTERNATIVES` Barlow SemiBold 16 pt `#2EC4B6`.

- `Ferric sulfate + sulfuric acid desmuts`
- `Gaining market share due to HF safety concerns`
- `Work well on 6xxx alloys`
- `May be insufficient for heavy copper smut (2024)`
- `Check supplier TDS for alloy compatibility`

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- DESMUT FAILURES` -- Y: 20.7".

**3x2 Grid:**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | MOTTLED COLOR | `#E05C5C` | Smut carried into anodize bath | Extend desmut time; verify complete removal |
| R1C2 | POOR DYE ABSORPTION | `#E8A020` | Residual smut blocks pore structure | N/A for integral (no dye) -- but affects pore quality |
| R1C3 | SURFACE PITTING | `#E05C5C` | HF too concentrated or too long | Reduce HF %; reduce time |
| R2C1 | DARK SPOTS | `#E05C5C` | Metallic residue (Cu, Fe) not removed | Switch to HNO3/HF; increase time |
| R2C2 | GRAIN BOUNDARY ATTACK | `#E8A020` | Aggressive desmut on thin-wall parts | Reduce time; lower HF concentration |
| R2C3 | INCONSISTENT FINISH | `#2EC4B6` | Uneven desmut agitation | Improve air agitation; rotate rack |

---

### ZONE 6 -- HF Safety + Standards

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- HF Safety (PROMINENT Coral panel):**

Large coral-tinted panel:
- Title: `HF SAFETY -- IF USED` Barlow SemiBold 22 pt `#E05C5C`
- Subtitle: `Hydrofluoric acid is extremely hazardous` Inter Medium 14 pt `#F0EDE8`

Bullets (Inter Regular 14 pt `#F0EDE8`):
- `Skin absorption causes systemic fluoride poisoning`
- `Bone damage and cardiac arrest possible from small exposures`
- `Calcium gluconate gel MUST be available at the station`
- `HF-specific training is MANDATORY`
- `Buddy system -- never work with HF alone`
- `HF burns may not be immediately painful -- delayed onset`

Amber closer: `For integral color on 6063, HF is not needed. Reserve HF for copper-bearing alloys only.` Inter Medium 14 pt `#E8A020`

**Right -- Standards:**

| Standard | Description |
|---|---|
| MIL-A-8625F | References desmut as mandatory pre-treatment |
| ASTM B580 | Anodic oxide coatings -- includes pre-treatment |
| OSHA 29 CFR 1910.1000 | HF exposure limits (PEL: 3 ppm TWA) |

---

### ZONE 7 -- Footer

Standard. Title: `Deoxidize -- Integral Color Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; typical desmut parameters for aluminum anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Deoxidize Integral Color -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Key message: for integral color on 6063, standard HNO3 desmut is sufficient. The HF section is included for completeness (and because some shops process mixed alloys) but should be clearly framed as "if needed -- and for integral color it usually is not." The HF safety callout is mandatory per Watson's Flag 4.

---

*Alaina -- Poster #331 -- Construction Workup v1.0 -- 2026-04-26*
