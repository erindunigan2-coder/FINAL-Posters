---
Project: Plating Posters Inc
Poster Number: 250
Title: "Activation -- Electroless Palladium"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Process Scope: Catalytic activation for electroless palladium (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessPalladium
  - Activation
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #250 -- Construction Workup
## Activation -- Electroless Palladium

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation creates a catalytically active surface that initiates electroless palladium deposition. The activation method varies dramatically by substrate. The most important thing to understand: in ENEPIG, the freshly deposited EN layer IS the catalytic surface for Pd -- no separate activation is needed. For non-catalytic substrates (ceramics, polymers), Sn/Pd colloidal or direct Pd activation is required. For hydrogen permeation membranes, multiple sensitization/activation cycles on porous ceramic may be needed.

Hero visual: a three-path activation decision tree showing ENEPIG (no activation needed), metallic substrates, and non-conductive substrates.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation decision tree hero (Block B):** Three-path diagram showing activation routes by substrate type. Rounded rectangles with connectors.
2. **Activation parameters table (Block D):** Multi-row table for each activation type.
3. **Membrane activation callout (Block E):** Multi-cycle sensitization/activation for porous ceramics.
4. **Defect grid (Block F):** 4 activation-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per Series Design Prompt.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- ACTIVATION DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACTIVATION PARAMETERS BY SUBSTRATE (14.5"--20.5" / ~6.0")
ZONE 5 -- MEMBRANE ACTIVATION + ENEPIG NOTE (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Palladium -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `No catalytic surface, no deposition. Activation method depends entirely on what you are plating onto.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, rinsed substrate  -->  After: Catalytically active surface ready for Pd deposition`

---

### ZONE 3 -- Activation Decision Tree Hero

**Section label:** `ACTIVATION DEPENDS ON YOUR SUBSTRATE` -- Y: 4.4".

**BLOCK B -- Three-Path Decision Tree**

Y: 5.0" to 14.0".

**Root node (top center):**
- Rounded rect, X: 7.5", Y: 5.0", W: 9.0", H: 1.5", fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Text: `WHAT IS YOUR SUBSTRATE?` Barlow Condensed ExtraBold 22 pt `#E8A020`

**Three connector arrows down to three paths:**

**Path 1 -- ENEPIG (Left, X: 0.5"):**
- Rounded rect, W: 7.0", H: 5.5", fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `ENEPIG / EN SURFACE` Barlow SemiBold 18 pt `#27AE60`
- Content:
  - `NO SEPARATE ACTIVATION NEEDED` Barlow Condensed ExtraBold 16 pt `#27AE60`
  - `The EN layer IS the catalytic surface`
  - `Pd deposits directly onto freshly plated EN`
  - `Proceed from EN rinse to Pd bath`
  - `Do not allow EN surface to dry or oxidize`

**Path 2 -- Non-Conductive (Center, X: 8.0"):**
- Rounded rect, W: 7.5", H: 5.5", fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `NON-CONDUCTIVE SUBSTRATES` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `Ceramics, polymers, glass` Inter Regular 13 pt `#F0EDE8` at 60%
- Content:
  - `Sn/Pd colloidal catalyst` Barlow SemiBold 14 pt `#E8A020`
  - `PdCl2: 100--250 mg/L Pd`
  - `SnCl2: 15--40 g/L Sn`
  - `HCl: 150--250 mL/L`
  - `35--45 C, 3--7 min`
  - `Followed by accelerator (HCl rinse)`

**Path 3 -- Direct Pd Activation (Right, X: 16.0"):**
- Rounded rect, W: 7.5", H: 5.5", fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `DIRECT Pd ACTIVATION` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `Simple metallic surfaces` Inter Regular 13 pt `#F0EDE8` at 60%
- Content:
  - `PdCl2 / HCl solution`
  - `0.1--0.5 g/L Pd`
  - `20--40 C, 30--60 sec`
  - `Deposits Pd nuclei as catalyst seeds`
  - `Used when substrate is not self-catalytic`

**Bottom callout spanning full width (Y: 13.0"):**
- `ENEPIG is the dominant application. If you are running ENEPIG, your EN surface is your activation. No extra chemistry needed.` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- Activation Parameters by Substrate

**Section label:** `ACTIVATION PARAMETERS BY METHOD` -- Y: 14.7".

**BLOCK D -- Parameter Table (Y: 15.3" to 20.3")**

| Method | Chemistry | Temp | Time | pH | Key Control |
|---|---|---|---|---|---|
| ENEPIG (EN surface) | None required | -- | -- | -- | EN surface must be fresh, not oxidized |
| Sn/Pd colloidal | PdCl2 + SnCl2 in HCl | 35--45 C | 3--7 min | Acid | Accelerator after to expose Pd nuclei |
| Direct Pd activation | PdCl2 0.1--0.5 g/L in HCl | 20--40 C | 30--60 sec | Acid | Light Pd flash on surface |
| Membrane (multi-cycle) | SnCl2 sensitize + PdCl2 activate | Ambient | 3--5 min each | Acid | Up to 10 cycles for porous ceramic |

Header: fill `#3A4055`. Data: alternating `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Membrane Activation + ENEPIG Note

**Section label:** `SPECIAL APPLICATIONS` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Hydrogen Membrane Activation (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `MEMBRANE ACTIVATION (MULTI-CYCLE)` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `Step 1: SnCl2 sensitize (1 g/L in 1 mL/L HCl; ambient; 3--5 min)`
  - `Step 2: PdCl2 activate (0.1 g/L in 1 mL/L HCl; ambient; 3--5 min)`
  - `Repeat steps 1--2 up to 10 cycles`
  - `Each cycle deposits more Pd nuclei on porous ceramic`
  - `Uniform coverage required for gas-tight Pd film`

**Right -- ENEPIG Fast Track (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `ENEPIG -- THE FAST TRACK` Barlow SemiBold 18 pt `#27AE60`
- Content:
  - `EN surface is inherently catalytic for Pd`
  - `Transfer from EN rinse to Pd bath immediately`
  - `Do not allow parts to air-dry between EN and Pd`
  - `Oxidized EN surface = poor Pd initiation`
  - `IPC-4556 does not require separate activation`

---

### ZONE 6 -- Defect Grid

**Section label:** `ACTIVATION FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP PLATING | `#E05C5C` | No catalytic surface; poor activation | Verify activation method for substrate type |
| R1C2 | INCOMPLETE COVERAGE | `#E05C5C` | Too few sensitize/activate cycles (membranes) | Increase number of cycles; check Pd concentration |
| R2C1 | DELAYED INITIATION | `#E8A020` | EN surface oxidized before Pd bath | Reduce transfer time; keep parts wet |
| R2C2 | DARK SPOTS | `#E8A020` | Excess Sn residue from colloidal catalyst | Extend accelerator step to expose Pd nuclei |

Each card: W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Electroless Palladium`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Electroless Palladium -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-path decision tree is the most important visual on this poster. Most users running ENEPIG need to understand that they skip activation entirely -- the EN layer does the work. The membrane multi-cycle activation is niche but technically fascinating and worth featuring for completeness. The decision tree format makes this poster unique in the cluster -- it reads more like a routing diagram than a process detail, which matches the actual decision the operator faces.

---

*Alaina -- Poster #250 -- Construction Workup v1.0 -- 2026-04-26*
