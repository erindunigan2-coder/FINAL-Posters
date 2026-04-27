---
Project: Plating Posters Inc
Poster Number: 492
Title: "Grit Blasting -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 4)"
Technical Source: Grit blast specifications for HVOF including media selection (white alumina 99%+ for aerospace), blast parameters, profile verification. HVOF-specific note: profile need not be as aggressive as APS because high particle velocity provides excellent mechanical interlocking even on moderate profiles.
Process Scope: HVOF thermal spray -- grit blasting and surface profile preparation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - GritBlasting
  - SurfacePrep
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #492 -- Construction Workup
## Grit Blasting -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of the HVOF process. The key HVOF-specific insight: HVOF's high particle velocity (600-900 m/s) provides such excellent mechanical interlocking that a moderate profile is sufficient. Over-blasting is counterproductive -- it can damage thin-walled substrates and embed grit. Finer grit (36-60 mesh) and lower pressure (40-60 PSI) compared to APS.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Blast parameter spec table (Block B -- HERO):** Large specification table.
2. **HVOF vs. APS profile comparison (Block C):** Why HVOF needs less aggressive prep.
3. **Profile verification methods (Block D):** Three methods.
4. **Chrome replacement dimensional callout (Block E):** Grind-back requirements before blasting.
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
ZONE 3 -- BLAST PARAMETERS + COMPARISON HERO (4.2"--14.0" / ~9.8")
  Block B: Blast parameter table
  Block C: HVOF vs. APS profile comparison
ZONE 4 -- PROFILE VERIFICATION (14.0"--20.5" / ~6.5")
  Block D: Three verification methods
ZONE 5 -- CHROME REPLACEMENT + CLEANLINESS (20.5"--26.5" / ~6.0")
  Block E: Chrome replacement dimensional prep
  Block F: SSPC cleanliness standards
ZONE 6 -- TROUBLESHOOTING (26.5"--32.5" / ~6.0")
  Block G: 4 common grit blast problems
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `GRIT BLASTING` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- Surface Profile Preparation -- Stage 2 of 10` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `HVOF particles hit at 600-900 m/s. They interlock mechanically even on moderate profiles. Do not over-blast.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `Ra 3-6` -- 64 pt `#E8A020`
- Label: `microns -- moderate profile is sufficient for HVOF` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted (Amber). Others dimmed.
Below: `Before: Clean, dry surface --> After: Uniformly roughened profile, SSPC-SP 5 or SP 10`

---

### ZONE 3 -- Blast Parameters + Comparison (HERO)

**Section label:** `BLAST SPECIFICATION FOR HVOF` -- Y: 4.4".

**BLOCK B -- Blast Parameter Table (left, W: 11.0")**

Y: 5.0" to 10.0".

| Parameter | Typical Range | Notes |
|---|---|---|
| Media | White alumina (Al2O3); 99%+ purity for aerospace | No ferrous contamination |
| Grit size | 36-60 mesh | Finer than APS (24-36 mesh) |
| Blast pressure | 40-60 PSI (275-415 kPa) | Lower than APS (40-80 PSI) |
| Nozzle distance | 100-150 mm | Controlled distance for uniformity |
| Blast angle | 75-90 degrees to surface | 90 deg for max depth |
| Anchor profile (Ra) | 3-6 microns (125-250 microinches) | Moderate profile sufficient |
| Cleanliness | SSPC-SP 5 (White Metal) or SP 10 (Near-White) | Most HVOF specs require SP-5 |

**BLOCK C -- HVOF vs. APS Profile Comparison (right, W: 11.5")**

Y: 5.0" to 10.0".

- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `WHY HVOF NEEDS LESS AGGRESSIVE PREP` Barlow Condensed ExtraBold 18 pt `#E8A020`

Two-row comparison:

| Process | Particle Velocity | Profile (Ra) | Why |
|---|---|---|---|
| APS | 200-600 m/s | 3-8 um | Lower velocity -- needs rougher profile for mechanical interlock |
| HVOF | 600-900 m/s | 3-6 um | Supersonic impact provides excellent bonding even on moderate profile |

Key insight callout:
- `HVOF's high kinetic energy means particles "hammer" into the surface. The impact energy alone creates superior mechanical interlocking. Over-blasting can damage thin substrates without improving bond strength.` Inter Medium 13 pt `#F0EDE8`

Note:
- `Alumina from blasting gets incorporated into the first coating layer -- this is generally acceptable and does not compromise HVOF coating integrity.` Inter Regular 12 pt `#F0EDE8` at 70%

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

### ZONE 5 -- Chrome Replacement + Cleanliness Standards

**Two-column layout.**

**Left -- Chrome Replacement Dimensional Prep (Block E):**
- Rounded rect, X: 0.5", W: 11.0", H: 5.5", fill `#1E2435`, left accent `#E8A020`
- Title: `CHROME REPLACEMENT: GRIND BACK BEFORE BLAST` Barlow Condensed ExtraBold 18 pt `#E8A020`

Content (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
For hard chrome replacement applications:

1. Strip all remaining chrome (chemical or mechanical)
2. Grind substrate to achieve correct dimensional
   tolerance BEFORE blasting
3. Verify: no residual chrome remains on surface
4. Grit blast to SSPC-SP 5
5. HVOF spray to 200-400 um over-dimension
6. Final grind to drawing dimension

The substrate must be at the correct under-dimension
before HVOF coating to allow for finish grinding.
```

**Right -- SSPC Cleanliness Reference (Block F):**
- Rounded rect, X: 12.0", W: 11.5", H: 5.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `CLEANLINESS STANDARDS` Barlow Condensed ExtraBold 18 pt `#2EC4B6`

| SSPC | ISO 8501 | NACE | Description |
|---|---|---|---|
| SP 5 | Sa 3 | No. 1 | White Metal Blast -- all visible contamination removed |
| SP 10 | Sa 2.5 | No. 2 | Near-White Blast -- 95% of surface cleaned |
| SP 6 | Sa 2 | No. 3 | Commercial Blast -- 67% cleaned |

Note: `Most HVOF specifications require SP-5 (White Metal). For AMS 2448 compliance, SP-5 is the minimum.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 6 -- Troubleshooting

**Section label:** `GRIT BLAST PROBLEMS -- QUICK FIXES` -- Y: 26.7".

Four cards in a row:

| Problem | Cause | Fix |
|---|---|---|
| EMBEDDED GRIT | Excessive pressure or too close | Reduce pressure to 40-60 PSI; increase distance |
| INSUFFICIENT PROFILE | Worn media or pressure too low | Replace media; verify blast pressure |
| SUBSTRATE DAMAGE | Over-blasting thin walls or edges | Reduce pressure; use finer grit; mask edges |
| RESIDUAL CHROME | Blasting over unstripped chrome | Stop -- return to stripping; never blast over chrome |

Each card: Rounded rect, W: 5.5", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Grit Blasting -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Grit Blasting HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The big insight on this poster is "less is more" for HVOF grit blasting. APS operators who transition to HVOF often over-blast because they are trained on coarser profiles. HVOF's supersonic particle velocity compensates. The chrome replacement dimensional prep block is critical for the hard chrome replacement workflow -- this is the most common HVOF application and getting the pre-blast dimensions right is essential.

---

*Alaina -- Poster #492 -- Construction Workup v1.0 -- 2026-04-26*
