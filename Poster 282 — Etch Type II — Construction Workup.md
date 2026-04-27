---
Project: Plating Posters Inc
Poster Number: 282
Title: "Etch -- Type II"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.4)"
Technical Source: Industry-standard caustic etch (NaOH) for sulfuric acid anodizing (Type II). Covers standard etch, alloy-specific behavior, and the etch reaction chemistry.
Process Scope: Caustic etch stage (Stage 3 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Etch
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #282 -- Construction Workup
## Etch -- Type II

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. The caustic etch produces a uniform matte surface by controlled dissolution of the outer aluminum layer. It removes mill finish variation, minor scratches, and die lines. The hero concept: alloy-specific etch behavior -- different alloys produce dramatically different smut and etch rates. The etch reaction produces hydrogen gas -- ventilation is mandatory.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Etch tank cross-section hero (Block B):** Tank with NaOH solution, parts, H2 gas bubbles rising, and etch smut forming on surface.
2. **Operating parameters panel (Block D).**
3. **Alloy-specific etch behavior table (Block E):** Key comparison showing different alloys and their etch responses.
4. **Etch reaction chemistry callout (Block F).**
5. **Failure mode grid (Block G).**

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
ZONE 3 -- ETCH TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS + DISSOLVED Al MONITOR (14.5"--20.5" / ~6.0")
ZONE 5 -- ALLOY-SPECIFIC ETCH BEHAVIOR (20.5"--26.5" / ~6.0")
ZONE 6 -- ETCH REACTION + FAILURE MODES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CAUSTIC ETCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Controlled dissolution. NaOH strips away the outer aluminum layer to create a uniform matte surface -- but every alloy etches differently.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned aluminum with mill finish variation  -->  After: Uniform matte surface (with smut requiring desmut)`

---

### ZONE 3 -- Etch Tank Hero

**Section label:** `THE CAUSTIC ETCH TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D`
- Border: 3 pt `#C8D0D8`

**Parts on rack (center):**
- Vertical rect, X: 9.5", Y: 6.0", W: 5.0", H: 5.5", fill `#C8D0D8` at 20%, border 2 pt `#E8A020`
- Label: `ALUMINUM WORKPIECE` Barlow SemiBold 14 pt `#E8A020`

**H2 gas bubbles:**
- 8--12 small circles rising from part surface, fill `#F0EDE8` at 20%, various sizes (0.1"--0.3")
- Label: `H2 gas evolution` Inter Regular 12 pt `#F0EDE8` at 60%

**Smut layer on part surface:**
- Thin dark band along part edges, fill `#3A4055`
- Label: `Etch smut (Cu, Si, Fe residues)` Inter Regular 12 pt `#E05C5C`

**Bath parameter labels (right side):**
- `NaOH 40--80 g/L (5.3--10.7 oz/gal)` JetBrains Mono 14 pt `#E8A020`
- `Typical: 50--60 g/L` JetBrains Mono 13 pt `#F0EDE8`
- `130--150 F (55--65 C)` JetBrains Mono 14 pt `#E05C5C`
- `1--5 min (alloy-dependent)` JetBrains Mono 14 pt `#F0EDE8`
- `Etch rate: ~0.5--1.0 mil/min on 6061` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Dissolved aluminum monitor (left side):**
- `Dissolved Al: monitor continuously` JetBrains Mono 13 pt `#F0EDE8`
- `>50 g/L = sluggish etch` JetBrains Mono 13 pt `#E05C5C`
- `Action: partial dump or decant` JetBrains Mono 12 pt `#E8A020`

**Ventilation callout (top of tank):**
- Arrows pointing up from tank surface
- `VENTILATION REQUIRED -- H2 gas is flammable` Barlow SemiBold 14 pt `#E05C5C`

---

### ZONE 4 -- Operating Parameters + Dissolved Al

**Section label:** `OPERATING PARAMETERS` -- Y: 14.7".

**Two-column layout:**

**Left -- Parameter Card (X: 0.5", W: 11.0"):**

| Parameter | Value |
|---|---|
| Chemistry | Sodium hydroxide (NaOH) -- caustic etch |
| Concentration | 40--80 g/L (5.3--10.7 oz/gal); typical 50--60 g/L |
| Temperature | 55--65 C (130--150 F) |
| Time | 1--5 minutes (alloy-dependent) |
| Etch rate | ~0.5--1.0 mil/min (12--25 um/min) on 6061 at 60 C |
| Dissolved aluminum | Monitor; >50 g/L = sluggish; partial dump required |

**Right -- Dissolved Aluminum Gauge (X: 12.0", W: 11.5"):**

Section label: `DISSOLVED ALUMINUM` Barlow Condensed ExtraBold 22 pt.

Horizontal bar gauge:
- Green zone: `0--30 g/L` fill `#27AE60` at 40% -- `Normal`
- Yellow zone: `30--50 g/L` fill `#E8A020` at 30% -- `Aging -- monitor closely`
- Red zone: `>50 g/L` fill `#E05C5C` at 40% -- `Sluggish -- partial dump`

Note: `As dissolved Al rises, etch rate drops and viscosity increases. Parts emerge with incomplete etch and streaking.` Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Alloy-Specific Etch Behavior

**Section label:** `ALLOY BEHAVIOR -- EVERY ALLOY ETCHES DIFFERENTLY` -- Y: 20.7".

**BLOCK E -- Alloy Comparison Table**

| Alloy | Etch Time | Smut Type | Notes |
|---|---|---|---|
| 6061 / 6063 | 2--3 min (standard) | Light, easily removed | Gold standard for anodizing; uniform matte |
| 5052 | 2--3 min | Slight grayish tint | Good etch behavior; Mg content |
| 1100 | 2--3 min | Minimal smut | Soft; etch quickly; watch for over-etch |
| 2024 | 1--2 min (SHORTER) | HEAVY dark copper smut | Cu residue requires aggressive desmut (HNO3/HF) |
| 7075 | 1--2 min (SHORTER) | Zn + Cu smut | Faster etch rate; reduce time to limit smut |
| Cast (high Si) | NOT RECOMMENDED | Gritty, rough surface | Si does NOT dissolve in NaOH; mechanical prep preferred |

Alloy: Inter Medium 14 pt `#F0EDE8`. Time: JetBrains Mono 13 pt. Notes: Inter Regular 12 pt.
2024 and 7075 rows: left accent `#E05C5C`. Cast row: left accent `#E05C5C`, notes in `#E05C5C`.

---

### ZONE 6 -- Etch Reaction + Failure Modes

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- The Etch Reaction (X: 0.5", W: 11.0"):**

Section label: `THE ETCH REACTION` Barlow Condensed ExtraBold 22 pt.

Reaction equation in prominent callout:
- Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`
- `2Al + 2NaOH + 2H2O --> 2NaAlO2 + 3H2` JetBrains Mono 18 pt `#E8A020`

Below:
- `Aluminum dissolves in caustic, forming sodium aluminate` Inter Regular 14 pt `#F0EDE8`
- `Hydrogen gas evolution is vigorous -- adequate ventilation is essential` Inter Medium 14 pt `#E05C5C`
- `Etch produces smut = insoluble alloying element residues that remain on the surface` Inter Regular 13 pt `#F0EDE8` at 70%

**Right -- Failure Modes (X: 12.0", W: 11.5"):**

| Failure | Cause | Fix |
|---|---|---|
| Over-etching | Too long, too hot, or too concentrated | Reduce time; check temp and NaOH |
| Under-etching | Too short, dissolved Al too high | Extend time; partial dump to refresh bath |
| Heavy smut | Cu/Zn alloys (2024, 7075) | Expected -- aggressive desmut in next step |
| Pitting | Grain boundary attack from over-etch | Reduce time; check alloy compatibility |
| Streaking | Mill finish variation not removed | Extend etch or increase concentration |

Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Etch -- Type II`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; typical NaOH caustic etch parameters for aluminum anodizing.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Etch Type II -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The alloy behavior table is the centerpiece of this poster after the tank hero. Every shop that processes mixed alloys needs to understand that 2024 and 7075 behave completely differently from 6061. The etch reaction equation should be visually prominent -- it explains the H2 gas and the sodium aluminate buildup. Cast alloys with high silicon are explicitly called out as problematic because silicon particles do not dissolve in NaOH.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #282 -- Construction Workup v1.0*
*2026-04-26*
