---
Project: Plating Posters Inc
Poster Number: 482
Title: "Grit Blasting -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 4)"
Technical Source: Grit blast specifications for APS including media selection, blast parameters, profile verification methods, and SSPC cleanliness standards. White alumina preferred for aerospace to avoid ferrous contamination.
Process Scope: Atmospheric plasma spray -- grit blasting and surface profile preparation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - GritBlasting
  - SurfacePrep
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #482 -- Construction Workup
## Grit Blasting -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of the APS process. Grit blasting creates the anchor profile that the coating mechanically interlocks with. Wrong media, wrong pressure, wrong profile -- and the coating peels off the wall. The hero is a blast parameter specification table paired with a media selection guide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast parameter spec table (Block B -- HERO):** Large specification table with ranges and notes.
2. **Media selection guide (Block C):** 6-row comparison of blast media types.
3. **Profile verification methods (Block D):** Three methods with visual descriptions.
4. **"Why Alumina?" callout (Block E):** Comparison of alumina vs. steel grit for aerospace.
5. **Cleanliness standards reference (Block F):** SSPC/ISO equivalency strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Amber)
ZONE 3 -- BLAST PARAMETERS + MEDIA HERO (4.2"--14.0" / ~9.8")
  Block B: Blast parameter table
  Block C: Media selection guide (side by side)
ZONE 4 -- PROFILE VERIFICATION (14.0"--20.5" / ~6.5")
  Block D: Three verification methods
ZONE 5 -- WHY ALUMINA + CLEANLINESS (20.5"--26.5" / ~6.0")
  Block E: Alumina vs. steel grit callout
  Block F: SSPC cleanliness standards
ZONE 6 -- TROUBLESHOOTING (26.5"--32.5" / ~6.0")
  Block G: 4 common grit blast problems
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `GRIT BLASTING` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- Surface Profile Preparation -- Stage 2 of 10` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The coating does not bond to the metal. It bonds to the profile. No profile, no coating.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `Ra 3-8` -- 64 pt `#E8A020`
- Label: `microns target anchor profile` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted (Amber). Others dimmed.
Below: `Before: Clean, dry surface --> After: Uniformly roughened profile, SSPC-SP 5 or SP 10`

---

### ZONE 3 -- Blast Parameters + Media (HERO)

**Section label:** `BLAST SPECIFICATION FOR APS` -- Y: 4.4".

**BLOCK B -- Blast Parameter Table (left, W: 11.0")**

Y: 5.0" to 10.0".

| Parameter | Typical Range | Notes |
|---|---|---|
| Media | White or brown alumina (Al2O3) | Aerospace: white alumina only (99%+ purity) |
| Grit size | 24-36 mesh (coarse); 60 mesh (thin substrates) | Coarser = deeper profile |
| Blast pressure | 40-80 PSI (275-550 kPa) | Higher pressure for harder substrates |
| Nozzle distance | 100-200 mm (4-8 inches) | Closer = more aggressive cut |
| Blast angle | 60-90 degrees to surface | 90 deg for max depth; 60-75 for wider pattern |
| Anchor profile (Ra) | 3-8 microns (125-325 microinches) | Specification dependent |
| Cleanliness | SSPC-SP 5 / NACE No.1 (White Metal) or SA 3 (ISO 8501) | Most APS specs require SP-5 |

**BLOCK C -- Media Selection Guide (right, W: 11.5")**

Y: 5.0" to 10.0". Six rows.

| Media | Grit Size | Hardness | Best For |
|---|---|---|---|
| White alumina | 24-60 mesh | Mohs 9 | Aerospace; no ferrous contamination |
| Brown alumina | 24-60 mesh | Mohs 9 | General purpose; lower cost |
| Angular steel grit | G25-G40 | Mohs 7-8 | Infrastructure; bridge work |
| Silicon carbide | 24-60 mesh | Mohs 9.5 | Hard substrates; titanium prep |
| Garnet | 36-80 mesh | Mohs 7-8 | Non-ferrous; less aggressive |
| Chilled iron grit | G25-G40 | Mohs 7-8 | Heavy structural steel |

---

### ZONE 4 -- Profile Verification

**Section label:** `HOW TO VERIFY YOUR PROFILE` -- Y: 14.2".

**BLOCK D -- Three Verification Methods**

Y: 14.9" to 20.3". Three side-by-side cards.

| Method | X | W | Description | When to Use |
|---|---|---|---|---|
| Testex Replica Tape | 0.5" | 7.33" | Press-o-film tape pressed into surface, measured with micrometer. Reads peak-to-valley directly. Field standard. | Field verification; quick QC checks |
| Surface Profilometer | 8.0" | 7.33" | Stylus traces surface; outputs Ra, Rz values digitally. Most precise method. | Lab verification; specification compliance |
| Visual Comparator | 15.5" | 8.0" | SSPC-VIS 1 standard photos. Compare blasted surface to reference images. Qualitative but fast. | First-pass field assessment |

Each card: Rounded rect, H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt in `#2EC4B6`.

---

### ZONE 5 -- Why Alumina + Cleanliness Standards

**Two-column layout.**

**Left -- Why Alumina (Block E):**
- Rounded rect, X: 0.5", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#E8A020`
- Title: `WHY ALUMINA OVER STEEL GRIT?` Barlow Condensed ExtraBold 20 pt `#E8A020`
- Three reasons (Inter Medium 14 pt):
  1. `No ferrous contamination risk on Ni or Ti substrates` `#27AE60`
  2. `Alumina fractures to expose fresh cutting edges (self-sharpening)` `#F0EDE8`
  3. `Steel grit can embed and cause galvanic corrosion sites` `#E05C5C`

**Right -- SSPC Cleanliness Reference (Block F):**
- Rounded rect, X: 12.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `CLEANLINESS STANDARDS` Barlow Condensed ExtraBold 20 pt `#2EC4B6`

| SSPC | ISO 8501 | NACE | Description |
|---|---|---|---|
| SP 5 | Sa 3 | No. 1 | White Metal Blast -- all visible contamination removed |
| SP 10 | Sa 2.5 | No. 2 | Near-White Blast -- 95% of surface cleaned |
| SP 6 | Sa 2 | No. 3 | Commercial Blast -- 67% cleaned |

Note: `Most APS specifications require SP-5 (White Metal). Accept nothing less.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Troubleshooting

**Section label:** `GRIT BLAST PROBLEMS -- QUICK FIXES` -- Y: 26.7".

Four cards in a row (same format as Poster #479 Block F):

| Problem | Cause | Fix |
|---|---|---|
| EMBEDDED GRIT | Excessive pressure or too close | Reduce pressure; increase nozzle distance |
| INSUFFICIENT PROFILE | Low pressure or worn media | Increase pressure; replace media |
| NON-UNIFORM PROFILE | Inconsistent angle or distance | Maintain 60-90 deg; steady hand/robot |
| FERROUS CONTAMINATION | Steel grit on Ni/Ti substrate | Switch to alumina; NEVER use steel on aerospace parts |

---

### ZONE 7 -- Footer

Standard. Title: `Grit Blasting -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Grit Blasting Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The big insight: the coating bonds to the profile, not the metal. Ra 3-8 microns is the target window and it should be the most prominent number on the poster. The media selection guide is critical for shops that work on mixed substrates -- choosing the wrong media on an aerospace part is a scrapping event.

---

*Alaina -- Poster #482 -- Construction Workup v1.0 -- 2026-04-26*
