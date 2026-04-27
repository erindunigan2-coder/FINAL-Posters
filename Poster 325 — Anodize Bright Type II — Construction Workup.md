---
Project: Plating Posters Inc
Poster Number: 325
Title: "Anodize (Type II) -- Bright Anodizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 6: Bright Anodizing, Section 6.5)"
Technical Source: Standard Type II sulfuric acid anodize on a bright-dipped surface. Same chemistry as standard Type II. Critical difference: coating thickness is kept thin (0.2--0.5 mil) for maximum optical clarity over the reflective substrate. Temperature control is especially important -- any softening of oxide clouds the bright finish.
Process Scope: Bright anodizing -- Stage 6 of 8 (Anodize)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - BrightAnodizing
  - TypeII
  - Anodize
  - MainTank
  - ConstructionWorkup
  - AnodizingCluster
---

# Poster #325 -- Construction Workup
## Anodize (Type II) -- Bright Anodizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The anodize step for bright anodizing is IDENTICAL in chemistry to standard Type II sulfuric acid anodize. The critical difference is operational: the coating is kept thin (0.2--0.5 mil) for maximum transparency/clarity, and temperature control is especially tight because any oxide softening scatters light and clouds the mirror finish. Clear anodize over bright dip = "bright clear" -- the classic mirror. Dyed over bright dip = brilliant jewel tones.

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
  Stage 6 highlighted (Emerald)
ZONE 3 -- ANODIZE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS + CLARITY CONTROL (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- THICKNESS VS. CLARITY + FILM GROWTH (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ANODIZE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II on Bright Surface -- Stage 6 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Same sulfuric acid chemistry. Different operating philosophy. Thin, clear, controlled -- every degree matters when you are anodizing a mirror.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Specular bright-dipped aluminum --> After: Transparent anodic oxide over mirror surface (bright clear anodize)`

---

### ZONE 3 -- Anodize Tank Hero

**Section label:** `TYPE II SULFURIC ACID ANODIZE -- BRIGHT SURFACE` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section (Left Half)**

X: 0.5", Y: 5.0", W: 12.0", H: 8.5".

Tank body: Rounded rect, fill `#252B3D` (H2SO4 solution), border 2 pt `#C8D0D8`.

Parts on rack: vertical rects, fill `#C8D0D8` at 40%.
Label: `BRIGHT-DIPPED PARTS (ANODE)` Barlow SemiBold 12 pt `#27AE60`.

Cathode: vertical rects on both sides, fill `#3A4055`.
Label: `LEAD OR 6063 CATHODE` JetBrains Mono 10 pt `#C8D0D8`.

Power supply: rect above tank.
Label: `DC RECTIFIER` Barlow SemiBold 11 pt `#E8A020`.

Bath parameters:
- `H2SO4: 150--200 g/L (15--20%)` JetBrains Mono 14 pt `#27AE60`
- `Temp: 68--72 F (20--22 C) TIGHT CONTROL` JetBrains Mono 14 pt `#E8A020`
- `CD: 12--18 ASF (1.3--2.0 A/dm2)` JetBrains Mono 14 pt `#F0EDE8`
- `Voltage: 15--21V` JetBrains Mono 14 pt `#F0EDE8`
- `Time: 15--25 min (THIN for clarity)` JetBrains Mono 14 pt `#E8A020`

Air agitation indicators at tank bottom, stroke 2 pt `#2EC4B6`.

**BLOCK C -- Clarity Concept (Right Half)**

X: 13.0", Y: 5.0", W: 10.5", H: 8.5".
Rounded rect background, fill `#1E2435`.
Title: `THIN OXIDE = MAXIMUM CLARITY` Barlow Condensed ExtraBold 18 pt `#F0EDE8`

Cross-section diagram (rectangles):
1. `MIRROR SUBSTRATE` -- bright silver rect, fill `#C8D0D8`
2. `THIN OXIDE (0.2--0.5 mil)` -- semi-transparent green overlay, fill `#27AE60` at 20%
3. `Light passes through thin oxide --> reflects off mirror --> exits through oxide`
4. Arrows showing light path: in, reflect, out

Labels:
- `0.2--0.5 mil: transparent to visible light` JetBrains Mono 11 pt `#27AE60`
- `> 0.7 mil: begins to scatter light (haze)` JetBrains Mono 11 pt `#E8A020`
- `> 1.0 mil: visible cloudiness` JetBrains Mono 11 pt `#E05C5C`
- `Clear anodize over bright dip = "BRIGHT CLEAR" finish` Inter Medium 14 pt `#E8A020`

**Bottom callout (Y: 13.5"):**
- `The anodize chemistry is IDENTICAL to standard Type II. The difference: thin coating, tight temperature, and the bright-dipped substrate underneath.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Operating Parameters + Clarity Control

**Section label:** `OPERATING PARAMETERS -- BRIGHT ANODIZE` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Parameters (X: 0.5", W: 11.0"):**
Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `ANODIZE PARAMETERS` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Control Range | Bright-Specific Note |
|---|---|---|
| Electrolyte | H2SO4 150--200 g/L | Same as standard Type II |
| Temperature | 68--72 F (20--22 C) | TIGHTER control than standard (+/- 1 F) |
| Current density | 12--18 ASF | Standard range |
| Voltage | 15--21V | Standard range |
| Time | 15--25 min | SHORTER than standard (thin coating) |
| Target thickness | 0.2--0.5 mil (5--12 um) | Thin for optical clarity |
| Dissolved Al | < 20 g/L | Standard maintenance |

**Right -- Why Thin? (X: 12.0", W: 11.5"):**
Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".
Title: `THE CLARITY-THICKNESS TRADE-OFF` Barlow SemiBold 18 pt `#E8A020`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):
> Anodic oxide is not perfectly transparent. Each micron of oxide scatters a small amount of light. On a matte surface, this is invisible. On a mirror, it is the difference between a sharp reflection and a hazy glow.
>
> -- 0.2 mil (5 um): maximum clarity, minimum corrosion protection
> -- 0.5 mil (12 um): good clarity, reasonable protection
> -- 0.7 mil+ (18 um+): visible haze; not recommended for bright work
>
> The operator must balance reflectivity against corrosion specification.

---

### ZONE 5 -- Defect Diagnosis

**Section label:** `WHAT GOES WRONG -- ANODIZE DEFECTS ON BRIGHT WORK` -- Y: 20.7".

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | HAZE / CLOUDINESS | `#E05C5C` | Oxide too thick; temp too high | Reduce time; tighten temp to 68--72 F |
| R1C2 | BURNING (WHITE EDGES) | `#E05C5C` | CD too high; poor racking | Reduce CD; improve contact points |
| R1C3 | SOFT / POWDERY OXIDE | `#E8A020` | Temperature > 75 F | Lower temperature; check chiller |
| R2C1 | STREAKING | `#E8A020` | Uneven current distribution | Improve racking; add conforming cathode |
| R2C2 | PITTING | `#E05C5C` | Chloride contamination in bath | Check rinse water; maintain bath |
| R2C3 | COLOR VARIATION AFTER DYE | `#2EC4B6` | Uneven oxide thickness | Consistent anodize = consistent color |

---

### ZONE 6 -- Thickness vs. Clarity + Growth

**Section label:** `FILM THICKNESS vs. OPTICAL CLARITY` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Thickness/Clarity Table:**
Rounded rect, fill `#1E2435`, left accent `#27AE60`.
Title: `THICKNESS GUIDE FOR BRIGHT ANODIZE` Barlow SemiBold 18 pt `#27AE60`

| Thickness | Time @ 15 ASF | Clarity | Application |
|---|---|---|---|
| 0.2 mil (5 um) | ~15 min | EXCELLENT | Cosmetic only; minimal protection |
| 0.3 mil (8 um) | ~20 min | VERY GOOD | Balanced for most bright work |
| 0.5 mil (12 um) | ~25 min | GOOD | Best trade-off: clarity + protection |
| 0.7 mil (18 um) | ~35 min | FAIR (slight haze) | Standard Type II; not optimal for bright |
| 1.0 mil (25 um) | ~50 min | POOR (visible cloud) | Not recommended for bright anodize |

"EXCELLENT" in `#27AE60`. "POOR" in `#E05C5C`.

**Right -- Bright Anodize Finishes:**
Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `BRIGHT ANODIZE FINISH OPTIONS` Barlow SemiBold 18 pt `#E8A020`

Body:
> **Bright Clear**: No dye. Maximum reflectivity. Classic mirror finish.
>
> **Bright Dyed**: Dye step after anodize. Brilliant transparent colors over reflective base. Jewel-like appearance -- reds, blues, golds appear vivid and luminous.
>
> **Bright + Clear Topcoat**: Some applications add a clear lacquer or powder coat over sealed bright anodize for additional environmental protection.

---

### ZONE 7 -- Footer

Standard. Title: `Anodize (Type II) -- Bright Anodizing`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; standard Type II sulfuric acid anodize parameters applied to bright-dipped substrates. Consult your process supplier for application-specific thickness and clarity specifications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Anodize Bright Type II -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The clarity cross-section (Block C) is the key educational visual -- it shows light path through thin oxide reflecting off the mirror substrate. This is what makes bright anodize fundamentally different from standard Type II despite identical chemistry. The thickness/clarity table in Zone 6 is the most actionable content for operators: it directly connects anodize time to reflectivity outcome.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #325 -- Construction Workup v1.0*
*2026-04-26*
