---
Project: Plating Posters Inc
Poster Number: 422
Title: "Cleaning -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Sections 3.4, 3.9)"
Technical Source: PECVD cleaning encompasses both ex-situ wet cleaning (solvent, alkaline, DI rinse) and in-situ plasma pre-cleaning (Ar or O2 plasma surface activation). Two-stage cleaning is the standard: wet clean outside, plasma clean inside.
Process Scope: PECVD ex-situ and in-situ cleaning procedures
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PECVD
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #422 -- Construction Workup
## Cleaning -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 2 of the PECVD sequence. Cleaning for PECVD is a two-phase operation: ex-situ wet cleaning (outside the chamber) and in-situ plasma pre-cleaning (inside the chamber after pump-down). The in-situ plasma step is especially important for polymer substrates where O2 plasma surface activation is the difference between adhesion and delamination.

Hero visual: two-phase cleaning flow -- wet bench to plasma chamber.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Two-phase cleaning flow (Block B -- HERO):** Left side = ex-situ wet cleaning sequence. Right side = in-situ plasma pre-clean. Arrow connecting them through "Load into chamber."
2. **Solvent/chemical reference (Block C):** Table of cleaning agents with compatibility.
3. **Plasma pre-clean parameters (Block D):** Ar plasma vs. O2 plasma -- when to use each.
4. **Substrate-specific cleaning matrix (Block E):** Quick-reference for which clean applies to which substrate.
5. **Chamber cleaning (Block F):** Separate topic -- cleaning the PECVD chamber itself (maintenance).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal)
ZONE 3 -- TWO-PHASE CLEANING HERO (4.2"--14.5" / ~10.3")
  Block B: Ex-situ + in-situ cleaning flow
ZONE 4 -- CLEANING AGENTS + PLASMA PARAMETERS (14.5"--20.5" / ~6.0")
  Block C: Solvent/chemical table
  Block D: Plasma pre-clean parameters
ZONE 5 -- SUBSTRATE MATRIX + CHAMBER CLEANING (20.5"--32.5" / ~12.0")
  Block E: Substrate-specific cleaning matrix
  Block F: Chamber cleaning (maintenance)
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PECVD -- Stage 2 of 10 -- Ex-Situ Wet Clean + In-Situ Plasma Activation` -- 28 pt `#2EC4B6`. Y: 1.4".
**Tagline:** `Two cleaning stages. The wet bench removes what you can see. The plasma removes what you cannot. Both are non-negotiable.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `2` -- 72 pt, `#2EC4B6`
- Label: `CLEANING PHASES` -- JetBrains Mono, 14 pt
- Sub-label: `Wet (ex-situ) + Plasma (in-situ)` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 2 (`Cleaning`): fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Input: Inspected substrate  -->  Output: Atomically clean surface ready for deposition`

---

### ZONE 3 -- Two-Phase Cleaning Hero

**Section label:** `THE TWO-PHASE CLEAN` -- Y: 4.4".

**BLOCK B -- Cleaning Flow**

Y: 5.0" to 14.3". Full width.

**Left panel -- EX-SITU WET CLEANING (X: 0.5", W: 10.5")**

Large rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `PHASE 1: WET CLEANING (EX-SITU)` -- Barlow SemiBold, 22 pt, `#2EC4B6`

Four sequential steps in vertical flow:

Step 1: `Solvent Clean`
- `Acetone or IPA ultrasonic bath`
- `5--10 min, ambient temperature`
- `Removes organics, fingerprints, light oils`

Step 2: `Alkaline Clean (metals only)`
- `Alkaline detergent, ultrasonic`
- `50--70 degC, 5--15 min`
- `For steel, Al alloys -- heavier contamination`

Step 3: `DI Water Rinse`
- `Multi-stage cascade rinse`
- `18 MOhm-cm DI water (semiconductor grade)`
- `Removes all cleaning chemistry residue`

Step 4: `Drying`
- `Hot air, spin dry, or vacuum dry`
- `No water spots -- they become film defects`
- `N2 blow-off for wafers`

Each step: Rounded rect, W: 10.0", H: 1.8", fill `#252B3D`, left accent 3 pt `#2EC4B6`.
Step number: Barlow Condensed ExtraBold, 16 pt, `#2EC4B6`.
Details: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

Arrows between steps: 2 pt `#3A4055`, down.

**Center connector:**
- Large arrow, X: 11.5", pointing right, `#E8A020`
- Label: `LOAD INTO CHAMBER` -- Barlow SemiBold, 14 pt, `#E8A020`

**Right panel -- IN-SITU PLASMA PRE-CLEAN (X: 12.5", W: 11.0")**

Large rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `PHASE 2: PLASMA CLEAN (IN-SITU)` -- Barlow SemiBold, 22 pt, `#E8A020`

Two options presented:

Option A: `Argon Plasma Clean`
- `Ar+ ion bombardment`
- `Physical sputtering of surface contamination`
- `1--5 min at 100--300 W`
- `Pressure: 50--200 mTorr`
- `Best for: metals, inorganic substrates`
- `Removes: native oxides, residual organics`

Option B: `Oxygen Plasma Clean`
- `O2 reactive plasma`
- `Chemical oxidation of organic contamination`
- `1--5 min at 100--500 W`
- `Pressure: 100--500 mTorr`
- `Best for: polymers (surface activation)`
- `Creates -OH groups for adhesion`

Each option: Rounded rect, W: 10.5", H: 3.5", fill `#252B3D`.
Option A accent: `#C8D0D8`. Option B accent: `#E8A020`.

Bottom callout:
- `For polymer substrates, O2 plasma activation is THE critical step. Skip it and the film peels. Every time.` -- Inter Medium, 14 pt, `#E05C5C`

---

### ZONE 4 -- Cleaning Agents + Plasma Parameters

**Two-column layout. Y: 14.7" to 20.3".**

**BLOCK C -- Cleaning Agent Reference (Left, X: 0.5", W: 11.0")**

Section label: `CLEANING AGENT REFERENCE` -- Barlow Condensed ExtraBold, 22 pt. Y: 14.9".

| Agent | Type | Compatible With | Caution |
|---|---|---|---|
| Acetone | Solvent | All substrates | Flammable; leaves residue if low purity |
| IPA (isopropanol) | Solvent | All substrates | Flammable; final rinse solvent |
| Alkaline detergent | Aqueous | Metals, glass, ceramics | Not for polymers (swelling/attack) |
| DI water (18 MOhm) | Rinse | All substrates | Semiconductor grade for wafer work |
| Piranha (H2SO4:H2O2) | Etch clean | Si wafers, glass | Extremely dangerous -- trained personnel only |
| RCA SC-1 (NH4OH:H2O2:H2O) | Standard clean | Si wafers | Particle removal + organic removal |

**BLOCK D -- Plasma Pre-Clean Parameters (Right, X: 12.0", W: 11.5")**

Section label: `PLASMA PRE-CLEAN PARAMETERS` -- Y: 14.9".

| Parameter | Ar Plasma | O2 Plasma |
|---|---|---|
| Gas | Ar (argon) | O2 (oxygen) |
| Mechanism | Physical sputtering | Chemical oxidation |
| RF Power | 100--300 W | 100--500 W |
| Pressure | 50--200 mTorr | 100--500 mTorr |
| Time | 1--5 min | 1--5 min |
| Bias (if used) | -50 to -200 V | Typically unbiased |
| Best for | Oxide removal on metals | Organic removal; polymer activation |
| Caution | Can damage delicate structures | Can oxidize metal surfaces |

---

### ZONE 5 -- Substrate Matrix + Chamber Cleaning

**BLOCK E -- Substrate-Specific Cleaning Matrix (Y: 20.7" to 26.3")**

Section label: `WHICH CLEAN FOR WHICH SUBSTRATE?` -- Y: 20.9".

| Substrate | Solvent | Alkaline | DI Rinse | Dry | Ar Plasma | O2 Plasma |
|---|---|---|---|---|---|---|
| Si wafers | Yes (or RCA) | No | Yes (18 MOhm) | Spin/N2 | Optional | Yes |
| Glass | Yes | Optional | Yes | Hot air | Optional | Yes |
| Polymers | IPA only | NO | Yes | Air dry | NO (damage) | YES (critical) |
| Al alloys | Yes | Yes | Yes | Vacuum | Yes | Caution (oxidizes) |
| Steel | Yes | Yes | Yes | Vacuum | Yes | Caution (oxidizes) |
| Ceramics | Yes | Optional | Yes | Hot air | Yes | Yes |

Color coding: `YES (critical)` in `#27AE60`. `NO` in `#E05C5C`. `Caution` in `#E8A020`. `Optional` in `#F0EDE8` at 60%.

**BLOCK F -- Chamber Cleaning (Maintenance) (Y: 26.5" to 32.3")**

Section label: `CHAMBER CLEANING -- THE OTHER CLEANING JOB` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 26.7".

Callout panel, fill `#1E2435`, left accent `#E8A020`.

Two columns inside:

Left -- Why:
- `PECVD deposits film on chamber walls, not just substrates`
- `Buildup flakes off -> particles on your next batch`
- `Clean every 5--50 um accumulated wall thickness`
- `Rule of thumb: if you can see color change on the wall, you are overdue`

Right -- How:
- `In-situ plasma etch: NF3, CF4, or SF6 plasma`
- `Or manual wet clean: open chamber, wipe with IPA, inspect`
- `Caution: NF3 and CF4 are potent greenhouse gases -- abatement required`
- `After cleaning: run a "seasoning" coat (5--10 min dummy deposition) to stabilize chamber before production`

Bottom note:
- `Chamber particle counts should be verified after every clean. Run a test wafer and inspect.` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 6 -- Footer

Standard. Title: `Cleaning -- PECVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-phase cleaning concept is the key insight. Many plating professionals understand wet cleaning but are unfamiliar with in-situ plasma pre-cleaning. The side-by-side flow (wet bench -> plasma) should be immediately legible. The polymer substrate callout about O2 plasma activation deserves Coral emphasis -- this is the #1 adhesion failure root cause for PECVD on polymers.

---

*Alaina -- Poster #422 -- Construction Workup v1.0 -- 2026-04-26*
