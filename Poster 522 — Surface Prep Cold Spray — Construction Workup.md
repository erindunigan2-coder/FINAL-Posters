---
Project: Plating Posters Inc
Poster Number: 522
Title: "Surface Prep -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Grit blasting and surface preparation for cold spray. Unique aspect: some cold spray applications skip grit blasting entirely because the first particles self-activate the surface.
Process Scope: Cold spray -- grit blasting and surface preparation
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - SurfacePrep
  - GritBlast
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #522 -- Construction Workup
## Surface Prep -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Surface preparation poster for Cold Spray. The unique story here is that cold spray uses LESS aggressive grit blasting than other thermal spray processes, and some applications skip grit blasting entirely. The supersonic particle impact itself activates the surface -- the first layer acts as an in-situ grit blast. This is a live research area.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Grit blast parameter table (Block B -- HERO):** Standard parameter table with cold spray-specific ranges.
2. **"Self-Activating Surface" callout (Block C):** Key differentiator -- some CS applications skip blasting.
3. **Media selection guide (Block D):** Comparison of blast media options for cold spray substrates.
4. **Profile verification methods (Block E):** Testex tape, profilometer, visual standards.
5. **Substrate warnings strip (Block F):** Substrate-specific grit blast precautions.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- GRIT BLAST PARAMETERS + SELF-ACTIVATION (2.9"--14.5" / ~11.6")
  Block B: Parameter table (left)
  Block C: Self-activating surface callout (right)
ZONE 3 -- MEDIA SELECTION GUIDE (14.5"--21.5" / ~7.0")
  Block D: Media comparison table
ZONE 4 -- PROFILE VERIFICATION + SUBSTRATE WARNINGS (21.5"--32.5" / ~11.0")
  Block E: Verification methods
  Block F: Substrate precaution cards
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SURFACE PREP` -- 88 pt `#F0EDE8`.
**Subheading:** `Cold Spray -- Grit Blasting & Surface Activation` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Less aggressive than any other thermal spray -- because supersonic particles do half the work themselves.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Grit Blast Parameters + Self-Activation

**Section label:** `GRIT BLAST SPECIFICATION` -- Y: 3.1".

**BLOCK B -- Parameter Table (Left, X: 0.5", W: 14.0")**

Y: 3.8" to 10.0".

Header row: `#3A4055`. Columns: Parameter (4.0") | Typical Range (5.0") | Notes (5.0")

| Parameter | Typical Range | Notes |
|---|---|---|
| Media | Alumina (Al2O3), 99%+ purity | No steel grit on Al or Ti substrates |
| Grit size | 36--80 mesh | FINER than other thermal spray |
| Blast pressure | 30--60 PSI (200--415 kPa) | LESS aggressive than plasma/HVOF |
| Anchor profile (Ra) | 3--8 um (125--325 uin) | Moderate profile sufficient |
| Surface cleanliness | SSPC-SP 5 (White Metal) | Or equivalent specification |
| Blast angle | 60--90 degrees | Perpendicular preferred |
| Nozzle distance | 100--200 mm | Standard technique |

Data: JetBrains Mono Regular, 14 pt, `#F0EDE8`.
"FINER" and "LESS aggressive" annotations: `#E8A020` bold.

**Comparison callout below table:**
Rounded rect, H: 1.5", fill `#252B3D`, left accent `#E8A020`.
Title: `WHY LESS AGGRESSIVE?` Barlow SemiBold, 16 pt, `#E8A020`.
Body: `Cold spray particles impact at 600--1200 m/s -- they provide their own mechanical interlocking. A moderate profile is sufficient. Over-aggressive blasting wastes substrate material without improving adhesion.` Inter Regular, 13 pt, `#F0EDE8`.

**BLOCK C -- Self-Activating Surface Callout (Right, X: 15.0", W: 8.5")**

Y: 3.8" to 14.0". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.

Title: `SELF-ACTIVATING` Barlow Condensed ExtraBold, 28 pt, `#27AE60`.
Subtitle: `The First Particles ARE the Grit Blast` Barlow SemiBold, 16 pt, `#F0EDE8`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 165%):

```
Some cold spray applications do NOT
require grit blasting at all.

The first layer of high-velocity
particles impacts the surface with
enough energy to:

  1. Break through oxide films
  2. Plastically deform the substrate
  3. Create fresh metal contact
  4. Establish metallurgical bond

This "in-situ activation" is an
active area of research and is
application-specific.
```

Warning: `ALWAYS consult the specific cold spray specification before omitting grit blast. This is NOT universal.` Inter Medium, 13 pt, `#E05C5C`.

Bottom box:
- `Research frontier` JetBrains Mono Regular, 12 pt, `#27AE60` at 70%
- `Application-specific validation required` Inter Regular, 12 pt, `#F0EDE8` at 60%

---

### ZONE 3 -- Media Selection Guide

**Section label:** `BLAST MEDIA SELECTION` -- Y: 14.7".

**BLOCK D -- Media Comparison Table**

Y: 15.3" to 21.3". Full width.

Header row: `#3A4055`. Columns: Media (4.5") | Grit Size (3.0") | Hardness (2.5") | Best For (5.0") | Avoid On (4.0") | Cost (4.0")

| Media | Grit Size | Hardness | Best For | Avoid On | Cost |
|---|---|---|---|---|---|
| White alumina (Al2O3) | 36--80 mesh | 9 Mohs | Aerospace (Al, Ti, Ni) -- preferred | -- | Moderate |
| Brown alumina (Al2O3) | 36--60 mesh | 9 Mohs | General purpose | Aerospace (purity concern) | Low |
| Silicon carbide | 36--80 mesh | 9.5 Mohs | Hard substrates; Ti prep | Soft metals (embedding) | High |
| Garnet | 36--80 mesh | 7--8 Mohs | Non-ferrous substrates | -- | Moderate |
| Steel grit | -- | 7--8 Mohs | STRUCTURAL STEEL ONLY | Al, Ti, Ni (ferrous contamination) | Low |

"Avoid On" column: `#E05C5C` text.
"Best For" column: `#27AE60` text.

Callout below table:
`White alumina at 99%+ purity is the default for cold spray aerospace applications. Steel grit causes galvanic corrosion sites on non-ferrous substrates.` Inter Medium, 14 pt, `#2EC4B6`.

---

### ZONE 4 -- Profile Verification + Substrate Warnings

**Two-column layout (Y: 21.7" to 32.3"):**

**Left -- Profile Verification (X: 0.5", W: 11.0"):**

Section label: `PROFILE VERIFICATION` Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

Three method cards stacked:

| Method | Details | Use Case |
|---|---|---|
| Testex replica tape | Press-o-film + micrometer | Field method; quick; ASTM D4417 |
| Surface profilometer | Ra, Rz measurement (digital) | Precision; lab or in-line |
| Visual standards | SSPC-VIS 1 comparator | Quick pass/fail reference |

Each card: H: 2.0", fill `#1E2435`, left accent `#2EC4B6`.
Target: `Ra 3--8 um` JetBrains Mono 18 pt `#E8A020`.

**Right -- Substrate Warnings (X: 12.0", W: 11.5"):**

Section label: `SUBSTRATE PRECAUTIONS` Barlow Condensed ExtraBold, 22 pt, `#E05C5C`.

Four warning cards stacked:

| Substrate | Warning |
|---|---|
| Aluminum alloys | Limit pressure to 40 PSI max; annealing risk from excessive work hardening |
| Titanium alloys | Alumina ONLY (no ferrous contamination); oxidizes rapidly -- spray within 2 hr |
| Magnesium alloys | Extremely gentle blast (30 PSI); substrate easily damaged; cold spray preferred specifically because of low thermal load |
| Polymers/composites | NO grit blast -- mechanical abrasion (light sanding) or direct cold spray onto as-received surface |

Each card: H: 2.0", fill `#1E2435`, left accent `#E05C5C`.
Substrate: Barlow SemiBold, 15 pt, `#E05C5C`.
Warning: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Surface Prep -- Cold Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Surface Prep Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The "self-activating surface" concept is the hero story for this poster. No other thermal spray process can claim that the first particles replace grit blasting. This is genuinely unique to cold spray and should be visually prominent. The "less aggressive" theme throughout is a deliberate contrast with every other thermal spray surface prep poster, where the message is typically "blast harder."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #522 -- Construction Workup v1.0*
*2026-04-26*
