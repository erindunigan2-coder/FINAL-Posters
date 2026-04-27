---
Project: Plating Posters Inc
Poster Number: 432
Title: "Cleaning -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.3, 4.4)"
Technical Source: ALD cleaning requirements -- surface cleanliness AND surface chemistry must be correct. Carbon contamination blocks nucleation sites. RCA clean for semiconductor, UV-ozone for metals, O2 plasma for polymers. ALD is more forgiving of particles than PVD (conformal coating around particles) but less forgiving of chemical contamination.
Process Scope: ALD ex-situ cleaning, surface activation, and contamination management
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ALD
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #432 -- Construction Workup
## Cleaning -- ALD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of the ALD sequence. ALD cleaning has a dual purpose that distinguishes it from cleaning for any other deposition method: (1) remove contamination, and (2) activate the surface chemistry. A "clean" surface for ALD is not just free of particles and organics -- it must present the correct functional groups for the first precursor to react with. This poster covers both objectives.

Hero visual: the dual-purpose cleaning concept -- contaminant removal AND surface activation.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Dual-purpose cleaning concept (Block B -- HERO):** Two objectives illustrated side by side.
2. **Cleaning method matrix (Block C):** Substrate vs. cleaning method with activation technique.
3. **RCA clean detail (Block D):** The gold standard for semiconductor ALD -- both steps explained.
4. **UV-ozone and O2 plasma detail (Block E):** The activation techniques for non-semiconductor substrates.
5. **Contamination effects on ALD (Block F):** How different contaminants affect nucleation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- DUAL-PURPOSE CLEANING HERO (4.2"--13.0" / ~8.8")
  Block B: Remove contaminants + Activate surface
ZONE 4 -- CLEANING METHODS + RCA DETAIL (13.0"--22.0" / ~9.0")
  Block C: Substrate cleaning matrix
  Block D: RCA clean detail
ZONE 5 -- ACTIVATION TECHNIQUES + CONTAMINATION EFFECTS (22.0"--32.5" / ~10.5")
  Block E: UV-ozone and O2 plasma
  Block F: Contamination effects table
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 2 of 10 -- Contaminant Removal + Surface Activation` -- 28 pt `#2EC4B6`. Y: 1.4".
**Tagline:** `For ALD, "clean" means two things: no contamination AND correct surface chemistry. Remove the dirt, then set the stage for the first precursor pulse.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `2` -- 72 pt, `#2EC4B6`
- Label: `OBJECTIVES` -- JetBrains Mono, 14 pt
- Sub-label: `Remove + Activate` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 2 (`Cleaning`): fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Input: Inspected substrate  -->  Output: Clean surface with -OH nucleation sites ready for ALD`

---

### ZONE 3 -- Dual-Purpose Cleaning Hero

**Section label:** `CLEANING FOR ALD HAS TWO JOBS` -- Y: 4.4".

**BLOCK B -- Two-Objective Panel**

Y: 5.0" to 12.8". Full width.

**Left panel -- OBJECTIVE 1: REMOVE (X: 0.5", W: 11.0")**

Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`.
Title: `REMOVE CONTAMINATION` -- Barlow SemiBold, 24 pt, `#E05C5C`

Contaminant list (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
ORGANIC CONTAMINATION
- Fingerprints, oils, grease
- Photoresist residue
- Adventitious carbon from air exposure
EFFECT: Carbon blocks -OH sites -> island growth

PARTICULATE CONTAMINATION
- Dust, fibers, packaging debris
- Less critical than for PVD (ALD coats around particles)
- BUT particles still create bump defects

METALLIC CONTAMINATION
- Metal ions from previous processing steps
- Fe, Cu, Na from handling or chemicals
EFFECT: Metals can act as unwanted catalysts or dopants
```

**Right panel -- OBJECTIVE 2: ACTIVATE (X: 12.0", W: 11.5")**

Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`.
Title: `ACTIVATE SURFACE CHEMISTRY` -- Barlow SemiBold, 24 pt, `#27AE60`

Activation concept (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
CREATE NUCLEATION SITES
- -OH (hydroxyl) groups for oxide ALD
- -NH2 (amine) groups for nitride ALD
- Uniform density across entire surface

METHODS:
- Native oxide provides -OH on Si, Al, glass
- UV-ozone CREATES -OH on bare metals
- O2 plasma CREATES -OH/-COOH on polymers
- HF dip REMOVES oxide (H-terminated Si)

GOAL: Every surface site has a functional
group ready to react with Precursor A.
```

**Center connector arrow:** Large horizontal double arrow, `#E8A020`, with label: `Both objectives must be met` -- Barlow SemiBold, 14 pt.

**Bottom callout:**
- `ALD tolerates particles better than PVD because it is not line-of-sight. But ALD is LESS tolerant of chemical contamination because carbon blocks the self-limiting surface reactions.` -- Inter Medium, 13 pt, `#E8A020`

---

### ZONE 4 -- Cleaning Methods + RCA Detail

**BLOCK C -- Cleaning Method Matrix (Y: 13.2" to 18.0")**

Section label: `WHICH CLEAN FOR WHICH SUBSTRATE?` -- Y: 13.4".

| Substrate | Wet Clean | Activation | Final Surface | Cleanroom Class |
|---|---|---|---|---|
| Si wafers | RCA SC-1 + SC-2 | Optional HF dip | -OH (oxide) or -H (HF last) | ISO 5 (Class 100) |
| Metals | Ultrasonic alkaline + IPA | UV-ozone 5--30 min | -OH on oxide layer | ISO 6--7 |
| Polymers | IPA wipe (gentle) | O2 plasma 1--5 min | -OH / -COOH | ISO 6--7 |
| Glass | Solvent + DI rinse | UV-ozone (optional) | Native Si-OH | ISO 6 |
| Powders | None (no wet clean) | Thermal bake in reactor | Variable | N/A |
| Porous | Solvent rinse + vacuum bake | UV-ozone or thermal | -OH in pores | ISO 7 |

Header: `#3A4055`. Data: alternating fills.

**BLOCK D -- RCA Clean Detail (Y: 18.5" to 21.8")**

Section label: `THE RCA CLEAN -- GOLD STANDARD FOR SEMICONDUCTOR ALD` -- Y: 18.7".

Two side-by-side callout panels:

Left -- SC-1 (X: 0.5", W: 11.0"):
- Title: `SC-1 (Standard Clean 1)` -- Barlow SemiBold, 18 pt, `#2EC4B6`
- Chemistry: `NH4OH : H2O2 : H2O = 1:1:5`
- Temperature: `75--80 degC`
- Time: `10 min`
- Purpose: `Removes organic contamination and particles`
- Mechanism: `H2O2 oxidizes organics; NH4OH etches + lifts particles`

Right -- SC-2 (X: 12.0", W: 11.5"):
- Title: `SC-2 (Standard Clean 2)` -- Barlow SemiBold, 18 pt, `#E8A020`
- Chemistry: `HCl : H2O2 : H2O = 1:1:6`
- Temperature: `75--80 degC`
- Time: `10 min`
- Purpose: `Removes metallic (ionic) contamination`
- Mechanism: `HCl dissolves metal ions; H2O2 oxidizes surface`

Bottom note: `After RCA clean: surface is covered with a thin chemical oxide (~1 nm) rich in -OH groups -- ideal for TMA nucleation.` -- Inter Medium, 12 pt, `#27AE60`

---

### ZONE 5 -- Activation Techniques + Contamination Effects

**BLOCK E -- UV-Ozone and O2 Plasma (Y: 22.2" to 27.5")**

Section label: `SURFACE ACTIVATION TECHNIQUES` -- Y: 22.4".

Two technique panels side by side:

Left -- UV-Ozone (X: 0.5", W: 11.0"):
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `UV-OZONE TREATMENT` -- Barlow SemiBold, 18 pt, `#E8A020`
```
Mechanism: 185 + 254 nm UV light generates
O3 and atomic oxygen from air O2
These species oxidize organics and create
-OH groups on metal/oxide surfaces

Parameters:
  Time: 5--30 min
  Distance: sample 5--20 mm from UV lamp
  Atmosphere: air (ambient)
  Equipment: UV-ozone cleaner (benchtop)

Best for: metals, inorganics
Not suitable for: polymers (UV damages)
```

Right -- O2 Plasma (X: 12.0", W: 11.5"):
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `O2 PLASMA ACTIVATION` -- Barlow SemiBold, 18 pt, `#27AE60`
```
Mechanism: RF plasma generates reactive
oxygen species that functionalize surfaces
Creates -OH and -COOH groups on polymers
Also removes ~1 nm/min of organic material

Parameters:
  Power: 50--200 W
  Time: 1--5 min
  Pressure: 100--500 mTorr
  Gas: O2 or O2/Ar mixture

Best for: polymers, assembled devices
CRITICAL for: PET, PC, PTFE substrates
```

Note: `Both methods serve the same purpose: create a dense, uniform layer of -OH groups. UV-ozone is simpler (benchtop tool, ambient atmosphere). O2 plasma is faster and works on polymers.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

**BLOCK F -- Contamination Effects on ALD (Y: 28.0" to 32.3")**

Section label: `HOW CONTAMINATION AFFECTS ALD NUCLEATION` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`. Y: 28.2".

| Contaminant | Effect on Nucleation | Detection | Impact |
|---|---|---|---|
| Carbon (organics) | Blocks -OH sites; causes island growth | XPS (C 1s peak); contact angle | Pinholes; non-uniform film; poor barrier |
| Water residue | Premature reaction with TMA in gas phase | RGA; extended pump-down | Particles; CVD-like growth; rough film |
| Metal ions (Na, Fe, Cu) | Act as dopants; alter film electrical properties | TXRF; SIMS | Shift dielectric constant; leakage current |
| Particulates | ALD coats around them; bump defects | Optical inspection; particle counter | Localized defects; acceptable in non-critical apps |
| Native oxide (too thick) | Adds uncontrolled thickness to total stack | Ellipsometry | May exceed spec; strip with HF if needed |

Header: `#3A4055`. Data: alternating fills. Contaminant names: `#E05C5C`. Effects: Inter Regular.

---

### ZONE 6 -- Footer

Standard. Title: `Cleaning -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-purpose cleaning concept is what distinguishes ALD cleaning from every other process. In electroplating, you clean to remove contamination. In PVD, you clean to remove contamination. In ALD, you clean to remove contamination AND to create the chemistry the process needs. The two-panel hero (Remove + Activate) must communicate this duality immediately.

The RCA clean detail is essential for the semiconductor audience. The UV-ozone / O2 plasma comparison serves the industrial and research audience who work with non-semiconductor substrates.

---

*Alaina -- Poster #432 -- Construction Workup v1.0 -- 2026-04-26*
