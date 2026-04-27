---
Project: Plating Posters Inc
Poster Number: 431
Title: "Part Prep -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.3, 4.4)"
Technical Source: ALD substrate preparation -- surface functionalization is key. ALD nucleation requires specific functional groups (-OH, -NH2) on the surface. Different substrates (Si, metals, polymers, powders) require different preparation methods to provide these nucleation sites. Carbon contamination blocks nucleation and causes island growth.
Process Scope: ALD substrate inspection, surface functionalization, and preparation for nucleation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ALD
  - PartPrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #431 -- Construction Workup
## Part Prep -- ALD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of the ALD sequence. ALD is fundamentally a surface chemistry process -- the first precursor pulse reacts with functional groups ON the surface. If those groups are not there, the film does not nucleate. This poster covers substrate-specific preparation methods that ensure those nucleation sites exist: RCA clean for silicon, UV-ozone for metals, O2 plasma for polymers.

Hero visual: surface functionalization concept -- bare surface vs. -OH terminated surface.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Surface functionalization concept (Block B -- HERO):** Diagram showing bare vs. functionalized surface with -OH groups.
2. **Substrate-specific prep table (Block C):** 6 substrate types with preparation method and nucleation notes.
3. **Why nucleation matters (Block D):** Island growth vs. continuous film comparison.
4. **Special substrates (Block E):** Powders, nanoparticles, porous materials -- non-traditional ALD substrates.
5. **Pre-process checklist (Block F):** Inspection and qualification steps.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- SURFACE FUNCTIONALIZATION HERO (4.2"--13.5" / ~9.3")
  Block B: Nucleation concept diagram
ZONE 4 -- SUBSTRATE-SPECIFIC PREP (13.5"--21.0" / ~7.5")
  Block C: 6-substrate preparation table
ZONE 5 -- NUCLEATION + SPECIAL SUBSTRATES + CHECKLIST (21.0"--32.5" / ~11.5")
  Block D: Island growth vs. continuous film
  Block E: Special substrates
  Block F: Pre-process checklist
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 1 of 10 -- Surface Functionalization for Nucleation` -- 30 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `ALD does not coat surfaces. It reacts with them. If the surface does not have the right chemistry, the first cycle fails -- and so does the film.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#2EC4B6`
- Big number: `-OH` -- Barlow Condensed ExtraBold, 64 pt, `#2EC4B6`
- Label: `NUCLEATION SITES` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Hydroxyl groups start the ALD reaction` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Orientation Strip

Stage 1 (`Substrate Prep`): fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Input: Raw substrates (wafers, parts, powders)  -->  Output: Functionalized surface ready for ALD nucleation`

---

### ZONE 3 -- Surface Functionalization Hero

**Section label:** `THE SURFACE MUST BE READY -- ALD IS SURFACE CHEMISTRY` -- Y: 4.4".

**BLOCK B -- Nucleation Concept**

Y: 5.0" to 13.3". Full width.

Main panel: Rounded rect, X: 0.5", W: 23.0", fill `#1E2435`, radius 8.

**Left half (X: 1.0", W: 10.5") -- "UNPREPARED SURFACE":**

Title: `UNPREPARED SURFACE` -- Barlow SemiBold, 22 pt, `#E05C5C`

Description block:
```
Surface has:
- Carbon contamination (blocks reaction sites)
- Sparse or absent -OH groups
- Inconsistent oxide layer

RESULT: TMA finds few sites to react with.
Film nucleates as scattered islands.
Coverage is incomplete. Pinholes persist
until islands merge (10-50+ cycles wasted).
```

Text: Inter Regular, 14 pt, `#F0EDE8`. "RESULT" label: `#E05C5C`.

Visual note: `[Describe diagram: flat surface with sparse, scattered dots representing isolated TMA adsorption sites. Gaps between dots labeled "no nucleation here"]`

**Right half (X: 12.5", W: 10.5") -- "PREPARED SURFACE":**

Title: `PREPARED SURFACE` -- Barlow SemiBold, 22 pt, `#27AE60`

Description block:
```
Surface has:
- Dense, uniform -OH groups
- Clean (no carbon, no particles)
- Consistent oxide or native hydroxyl layer

RESULT: TMA reacts with every -OH site.
Complete monolayer coverage from cycle 1.
Film is continuous, pinhole-free, and
uniform from the very first layer.
```

Text: Inter Regular, 14 pt, `#F0EDE8`. "RESULT" label: `#27AE60`.

Visual note: `[Describe diagram: flat surface completely covered with evenly spaced dots. Every site occupied. Label: "complete coverage"]`

**Center divider:** Vertical line, 2 pt `#3A4055`, dashed.

**Bottom callout (full width, Y: 12.0"):**
- Rounded rect, W: 22.0", H: 1.0", fill `#2EC4B6` at 10%, border 1 pt `#2EC4B6`
- Text: `The difference between a good ALD film and a bad one is almost always decided BEFORE the first cycle runs. Surface preparation is the process.` -- Inter Medium, 14 pt, `#2EC4B6`

---

### ZONE 4 -- Substrate-Specific Preparation

**Section label:** `SUBSTRATE-SPECIFIC PREPARATION METHODS` -- Y: 13.7".

**BLOCK C -- 6-Substrate Table**

Y: 14.3" to 20.8".

| Substrate | Prep Method | Surface Chemistry | ALD Temp Range | Key Note |
|---|---|---|---|---|
| Silicon wafers | RCA clean (SC-1 + SC-2); optional HF dip | -OH on native oxide; or H-terminated (HF last) | 100--400 degC | HF-last gives H-terminated surface -- different nucleation behavior |
| Metals (Al, Ti, steel) | Ultrasonic clean + UV-ozone (5--30 min) | UV-ozone creates uniform oxide + -OH groups | 100--300 degC | UV-ozone is the standard for metal surface activation |
| Polymers (PET, PC) | O2 plasma (1--5 min, 50--200 W) | Plasma creates -OH, -COOH groups on polymer | 50--150 degC | WITHOUT plasma: no nucleation on hydrophobic polymers |
| Glass | Solvent clean + UV-ozone or O2 plasma | Native Si-OH groups already present | 100--300 degC | Glass is the "easy" substrate -- good native -OH density |
| Powders / nanoparticles | Thermal desorption in reactor; or plasma | Variable -- depends on particle chemistry | 100--300 degC | Fluidized bed or rotary reactor required |
| Porous materials (AAO, MOF) | Solvent clean + extended baking (vacuum) | Surface -OH groups within pores | 100--250 degC | Longer pulse + purge times needed (diffusion into pores) |

Header: `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`. Accent strip per row varies by substrate.
Substrate names: Barlow SemiBold, 13 pt. Data: Inter Regular, 12 pt. Key notes: Inter Medium, 12 pt, accent color.

---

### ZONE 5 -- Nucleation Insight + Special Substrates + Checklist

**BLOCK D -- Island Growth vs. Continuous Film (Y: 21.2" to 25.0")**

Section label: `WHY NUCLEATION MATTERS -- THE FIRST 10 CYCLES` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 21.4".

Two side-by-side callout panels:

Left -- Poor Nucleation (X: 0.5", W: 11.0"):
- Fill `#1E2435`, left accent `#E05C5C`
- Title: `ISLAND GROWTH (POOR PREP)` -- Barlow SemiBold, 16 pt, `#E05C5C`
- `Cycles 1--10: Isolated islands form at scattered -OH sites`
- `Cycles 10--50: Islands grow laterally and coalesce`
- `Cycles 50+: Film finally becomes continuous`
- `Result: First 5--10 nm is non-uniform, porous, and not conformal`
- `Wasted cycles, poor barrier properties, pinholes`

Right -- Good Nucleation (X: 12.0", W: 11.5"):
- Fill `#1E2435`, left accent `#27AE60`
- Title: `LAYER-BY-LAYER GROWTH (GOOD PREP)` -- Barlow SemiBold, 16 pt, `#27AE60`
- `Cycle 1: Complete monolayer across entire surface`
- `Cycle 2+: Each cycle adds exactly one sub-monolayer`
- `Film is continuous from the start`
- `Result: Pinhole-free at > 5 nm. True ALD behavior.`
- `Every cycle counts. No waste.`

**BLOCK E -- Special Substrates (Y: 25.5" to 29.5")**

Section label: `ALD ON NON-TRADITIONAL SUBSTRATES` -- Barlow Condensed ExtraBold, 22 pt, `#2EC4B6`. Y: 25.7".

Three callout boxes in a row:

| Box | X | Substrate | Notes |
|---|---|---|---|
| 1 | 0.5" | POWDERS & NANOPARTICLES | Fluidized-bed ALD or rotary reactor tumbles particles during cycling. Enables conformal coating of individual particles -- used for battery electrode coatings (1--5 nm Al2O3 on cathode particles improves cycle life). |
| 2 | 8.0" | HIGH-ASPECT-RATIO STRUCTURES | ALD conformality > 95% in 100:1 aspect ratio trenches (semiconductor). Purge times must be extended to allow precursor diffusion into and byproduct diffusion out of deep features. |
| 3 | 15.5" | BIOLOGICAL & CULTURAL | ALD can coat textiles, paper, butterfly wings, cultural artifacts. Ultra-thin Al2O3 (5--50 nm) provides corrosion/oxidation barrier without changing appearance or feel. Temperature must stay below 100 degC. |

Each box: Rounded rect, W: 7.33", H: 3.5", fill `#1E2435`, top accent 3 pt `#2EC4B6`, radius 6.

**BLOCK F -- Pre-Process Checklist (Y: 30.0" to 32.3")**

Section label: `PRE-PROCESS INSPECTION` -- Barlow Condensed ExtraBold, 20 pt, `#E8A020`. Y: 30.2".

Two-column, compact:

Left:
```
[ ] Substrate type documented
[ ] Surface prep method completed
[ ] No visible contamination (fingerprints, particles)
[ ] Outgassing materials absent
```

Right:
```
[ ] Target film and thickness specified
[ ] ALD recipe selected (verified in ALD window)
[ ] Substrate fits reactor/susceptor
[ ] Documentation logged (operator, date, recipe)
```

---

### ZONE 6 -- Footer

Standard. Title: `Part Prep -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

ALD prep is fundamentally different from PVD or PECVD prep. In those processes, you clean the surface to remove contamination. In ALD, you clean AND functionalize -- you actively create the chemical groups that the first precursor needs to react with. The -OH rule card drives this home. The island growth vs. continuous film comparison (Block D) is the visual that makes the concept stick: skip prep and you waste cycles growing islands that eventually merge. Do it right and every cycle counts from the start.

The special substrates callout (Block E) is where ALD's uniqueness shines -- no other coating method can conformally coat individual nanoparticles or the inside of 100:1 aspect ratio trenches.

---

*Alaina -- Poster #431 -- Construction Workup v1.0 -- 2026-04-26*
