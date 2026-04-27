---
Project: Plating Posters Inc
Poster Number: 610
Title: "Nitrocarburizing Cycle -- FNC / QPQ"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 6: FNC / QPQ, Sections 6.1, 6.6)"
Technical Source: The active nitrocarburizing step -- cyanate decomposition mechanism, epsilon compound zone formation, diffusion zone development, ferritic transformation (no phase change). Per AMS 2753.
Process Scope: The active nitrocarburizing cycle (Stage 3 of 9 -- the core process)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - FerriticNitrocarburizing
  - FNC
  - QPQ
  - NitrocarburizingCycle
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #610 -- Construction Workup
## Nitrocarburizing Cycle -- FNC / QPQ

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the core process poster -- Stage 3 of 9 -- where the actual metallurgy happens. Parts sit in molten cyanate salt at 1050-1075 F and nitrogen plus carbon diffuse into the ferrite surface. The result: an epsilon iron nitride (Fe2-3N) compound zone that provides extreme surface hardness and wear resistance, formed entirely below Ac1 with no phase transformation and no quench. The cross-section diagram showing the compound zone over the diffusion zone over the unaffected core is the hero visual.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Surface cross-section hero (Block B):** Metallographic-style diagram showing compound zone, diffusion zone, and core.
2. **Mechanism of action panel (Block D):** How cyanate decomposes and N+C diffuse.
3. **Steel response comparison (Block E):** Different steels, different hardness responses.
4. **Dimensional change callout (Block F):** The precision advantage -- negligible growth.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SURFACE CROSS-SECTION HERO (2.9"--15.5")
  Block B: Compound zone / diffusion zone / core diagram
ZONE 3 -- MECHANISM OF ACTION (15.5"--22.0")
  Block D: Cyanate decomposition and diffusion
ZONE 4 -- STEEL RESPONSE + DIMENSIONAL CHANGE (22.0"--32.5")
  Block E: Steel comparison table (left)
  Block F: Dimensional change callout (right)
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NITROCARBURIZING CYCLE` -- 80 pt `#F0EDE8`.
**Subheading:** `FNC / QPQ -- The Core Process: Cyanate Salt at 1050-1075 F` -- 30 pt `#27AE60` (Emerald).
**Tagline:** `Below Ac1. No phase transformation. No quench distortion. Nitrogen and carbon diffuse into ferrite, forming an epsilon iron nitride compound zone of extraordinary hardness -- all without changing the core microstructure.` -- 20 pt `#F0EDE8` at 65%.

**Rule card (right):**
- Big number: `1000` -- 72 pt `#27AE60`
- Label: `HV surface hardness on H13 tool steel after FNC treatment` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Surface Cross-Section (HERO)

**Section label:** `THE FNC-TREATED SURFACE -- WHAT YOU'RE BUILDING` -- Y: 3.1".

**BLOCK B -- Cross-Section Diagram (Y: 3.8" to 15.3")**

Large vertical cross-section showing three distinct zones from surface to core:

**Overall frame:**
- Rounded rect, X: 2.0", Y: 4.5", W: 20.0", H: 10.0", fill `#252B3D`, border 2 pt `#C8D0D8`

**Layer 1 -- Compound Zone (top):**
- Rect, X: 2.0", Y: 4.5", W: 20.0", H: 1.5"
- Fill: `#F0EDE8` at 25%
- Border bottom: 2 pt dashed `#E8A020`
- Labels (left side):
  - `COMPOUND ZONE` Barlow SemiBold 18 pt `#E8A020`
  - `("White Layer")` Inter Regular 14 pt `#F0EDE8` at 60%
  - `10--25 microns (0.0004--0.001 inch)` JetBrains Mono 13 pt `#E8A020`
- Labels (right side, inside):
  - `Primarily EPSILON (Fe2-3N) iron nitride` Inter Medium 13 pt `#27AE60`
  - `Extremely hard: 600--1000+ HV` Inter Medium 13 pt `#27AE60`
  - `Wear-resistant and corrosion-resistant` Inter Medium 13 pt `#2EC4B6`
  - `Porous -- sealed by QPQ oxidizing quench` Inter Medium 13 pt `#E8A020`

**Layer 2 -- Diffusion Zone (middle):**
- Rect, X: 2.0", Y: 6.0", W: 20.0", H: 5.0"
- Fill: gradient from `#27AE60` at 20% (top) to `#1A1F2E` at 10% (bottom)
- Border bottom: 2 pt dashed `#2EC4B6`
- Labels (left side):
  - `DIFFUSION ZONE` Barlow SemiBold 18 pt `#27AE60`
  - `0.005--0.025 inch (0.13--0.64 mm)` JetBrains Mono 13 pt `#27AE60`
- Labels (right side, inside):
  - `Nitrogen in solid solution with ferrite` Inter Regular 13 pt `#F0EDE8`
  - `Fine nitride precipitates (Fe4N, CrN, etc.)` Inter Regular 13 pt `#F0EDE8`
  - `Provides fatigue resistance and load support` Inter Medium 13 pt `#27AE60`
  - `Hardness gradient: high at top, fading to core` Inter Regular 13 pt `#F0EDE8` at 70%

**Layer 3 -- Core (unaffected):**
- Rect, X: 2.0", Y: 11.0", W: 20.0", H: 3.5"
- Fill: `#1A1F2E`
- Labels:
  - `CORE (UNAFFECTED)` Barlow SemiBold 18 pt `#C8D0D8`
  - `Original microstructure preserved` Inter Regular 13 pt `#F0EDE8` at 60%
  - `No Q&T required before FNC (unlike gas nitriding)` Inter Regular 13 pt `#F0EDE8` at 60%
  - `As-machined, normalized, or annealed -- all work` Inter Medium 13 pt `#2EC4B6`

---

### ZONE 3 -- Mechanism of Action

**Section label:** `HOW IT WORKS -- CYANATE DECOMPOSITION AND DIFFUSION` -- Y: 15.7".

**BLOCK D -- Two-column layout (Y: 16.3" to 21.8")**

*Left -- Chemistry (X: 0.5", W: 11.0"):*

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `THE CHEMISTRY` Barlow SemiBold 18 pt `#27AE60`

Content:
```
CYANATE DECOMPOSITION:

The alkali cyanate (NaCNO/KCNO) in
the salt bath decomposes at the
steel surface:

4NaCNO -> Na2CO3 + 2NaCN + CO + 2N

The released NITROGEN and CARBON
atoms are absorbed into the ferrite
surface and diffuse inward.

CARBON SOURCE:
CO from cyanate decomposition provides
the carbon that co-diffuses with
nitrogen into the steel.

CYANIDE BYPRODUCT:
Note that NaCN (cyanide) is a
decomposition product. This is why
cyanide monitoring is required.

BATH REPLENISHMENT:
As cyanate is consumed, fresh salt
must be added to maintain the
35--40% CNO target.
```

*Right -- What Happens in the Steel (X: 12.0", W: 11.5"):*

Rounded rect fill `#1E2435`, left accent `#2EC4B6`.

Title: `WHAT HAPPENS IN THE STEEL` Barlow SemiBold 18 pt `#2EC4B6`

Content:
```
1. Nitrogen atoms diffuse into ferrite
   lattice (interstitial diffusion)

2. At the surface: nitrogen concentration
   exceeds the solubility limit in ferrite

3. Epsilon iron nitride (Fe2-3N) COMPOUND
   ZONE precipitates at the surface

4. Below the compound zone: nitrogen
   remains in solid solution and forms
   fine alloy nitride precipitates
   (CrN, MoN on alloy steels)

5. Carbon co-diffuses with nitrogen,
   contributing to compound zone formation

6. ALL OF THIS HAPPENS BELOW Ac1:
   The steel STAYS FERRITIC throughout
   No austenite, no martensite, no quench

7. Result: hard surface, tough core,
   minimal distortion, no warping

8. The compound zone is POROUS --
   this is actually an advantage:
   the QPQ oxidizing quench fills
   the pores with magnetite (Fe3O4),
   creating the corrosion barrier
```

---

### ZONE 4 -- Steel Response + Dimensional Change

**BLOCK E -- Steel Response Table (X: 0.5", W: 14.0", Y: 22.2" to 30.0")**

Section label: `STEEL RESPONSE TO FNC -- NOT ALL STEELS ARE EQUAL` Barlow Condensed ExtraBold 22 pt.

| Steel Grade | Surface Hardness (HV) | Application | Response |
|---|---|---|---|
| 1018 / 1020 | 350--550 | General engineering | Moderate -- dramatic improvement over untreated |
| 1045 | 400--600 | Shafts, pins | Good -- medium carbon adds some response |
| 4140 / 4340 | 500--700 | Hydraulic cylinders, gun barrels | Good -- Cr and Mo form hard nitrides |
| H13 | 900--1100 | Die casting cores, pins | Excellent -- 5% Cr produces very hard case |
| 410 / 420 stainless | 800--1000 | Corrosion + wear parts | Good but slower initial uptake (passive film) |
| Ductile iron | 400--600 | Crankshafts, camshafts | Good -- widely used in automotive |
| Cast iron | 350--500 | Cylinder liners, brake rotors | Moderate -- improves wear significantly |

Table: Header `#3A4055`, alternating rows. JetBrains Mono 13 pt for data.

Below table:
- `KEY PRINCIPLE: Steels with nitride-forming elements (Cr, Mo, Al, V) produce the hardest FNC cases. Plain carbon steels form only iron nitride -- still beneficial but lower hardness.` Inter Medium 13 pt `#27AE60`

**BLOCK F -- Dimensional Change Callout (X: 15.0", W: 8.5", Y: 22.2" to 30.0")**

Rounded rect fill `#1E2435`, left accent `#27AE60`.

Title: `DIMENSIONAL CHANGE` Barlow SemiBold 20 pt `#27AE60`

Big number: `<0.0002"` -- 48 pt `#27AE60`
Label: `(< 5 micrometers) typical growth` -- 16 pt `#F0EDE8`

Content:
```
NEGLIGIBLE GROWTH:
FNC produces minimal dimensional
change -- typically less than
0.0002 inch (5 micrometers)
per surface.

WHY?
- No phase transformation
  (no austenite -> martensite
  volume change)
- No quench (no thermal shock
  distortion)
- Compound zone is thin
  (10--25 micrometers)

WHAT THIS MEANS:
Parts can be finish-machined to
final dimensions BEFORE FNC
treatment. No post-treatment
grinding required for most
applications.

This is a major cost and lead
time advantage over carburizing,
which requires grinding stock.
```

Below both blocks -- bottom callout (Y: 30.5" to 32.3"):
- Pill bar, full width, fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- `FNC is to surface hardening what a clear coat is to automotive paint -- it changes the surface without changing the part.` Inter Medium 14 pt `#2EC4B6`, center.

---

### ZONE 5 -- Footer

Standard. Title: `Nitrocarburizing Cycle -- FNC / QPQ`. Version `v1.0 -- 2026`.

Disclaimer: `Source: AMS 2753, AMS 2755, ASM Handbook Vol. 4. Hardness values are typical for standard salt bath FNC at 1075 F. Actual results depend on steel grade, bath composition, and immersion time.`

---

## Parts 5--7

**Grouping:** 5 zones. **Light Remap:** Standard table. **Export:** Six files.

---

## Design Notes

The surface cross-section diagram mirrors the plasma nitriding cycle poster (#600) for series consistency -- operators familiar with one will immediately recognize the structure of the other. The key differentiator here is the "porous compound zone sealed by QPQ" annotation, which links this poster conceptually to the QPQ quench poster (#611). The steel response table is the reference that metallurgists will consult most often.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #610 -- Construction Workup v1.0*
*2026-04-26*
