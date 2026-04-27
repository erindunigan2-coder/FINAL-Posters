---
Project: Plating Posters Inc
Poster Number: 242
Title: "Activation -- Electroless Copper"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 4)"
Process Scope: Sn/Pd colloidal activation for electroless copper line (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #242 -- Construction Workup
## Activation -- Electroless Copper

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the electroless copper process. This is the most complex and expensive activation in all of electroless plating. Unlike EN on steel (where the metal substrate is self-catalytic), E-Cu deposits on non-conductive surfaces that have zero catalytic activity. The solution: colloidal Sn/Pd catalyst -- a three-step sequence of pre-dip, catalyst immersion, and accelerator. The colloidal Sn/Pd system deposits palladium nuclei on the conditioned dielectric surface. These Pd nuclei are the catalytic sites where copper reduction begins.

The Pd catalyst solution is the most expensive consumable in the E-Cu line ($50-200+ per liter). Proper control maximizes bath life and minimizes waste.

Hero visual: a three-step activation sequence diagram showing pre-dip, Sn/Pd catalyst immersion, and accelerator with the mechanism at each step.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-step activation sequence hero (Block B):** Three connected tank cross-sections showing pre-dip, catalyst, and accelerator. Mechanism annotations at each step.
2. **Orientation strip (Block C):** 8-stage strip, Stage 3 highlighted.
3. **Catalyst mechanism diagram (Block D):** Simplified colloidal Sn/Pd mechanism.
4. **Parameter tables (Block E):** Pre-dip, catalyst, and accelerator parameters.
5. **Direct metallization callout (Block F):** Emerging alternative to Sn/Pd.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- THREE-STEP ACTIVATION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACTIVATION PARAMETERS (14.5"--22.0" / ~7.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (22.0"--28.0" / ~6.0")
ZONE 6 -- DIRECT METALLIZATION + SAFETY (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Sn/Pd Colloidal Catalyst -- Stage 3 of 8` -- Barlow SemiBold, 30 pt, `#E8A020` (Amber). X: 0.5", Y: 1.4".

**Tagline:** `Non-conductive surfaces cannot catalyze copper deposition. Palladium can. Three steps deposit Pd nuclei on the dielectric: pre-dip, catalyst, accelerator.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean, conditioned dielectric surface (non-catalytic)  -->  After: Surface coated with Pd nuclei ready to catalyze Cu deposition`

---

### ZONE 3 -- Three-Step Activation Hero

**Section label:** `THE THREE-STEP ACTIVATION SEQUENCE` -- Y: 4.4".

**BLOCK B -- Three Tanks (Y: 5.0" to 12.5")**

Three tank cross-sections in a horizontal row, connected by arrows.

**Tank 1 -- Pre-Dip (X: 0.5", W: 7.0", H: 6.5"):**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Title: `STEP 1: PRE-DIP` Barlow SemiBold 18 pt `#E8A020`
- Inside labels:
  - `HCl 150-250 mL/L` JetBrains Mono 14 pt `#E8A020`
  - `Ambient temp` JetBrains Mono 13 pt `#F0EDE8`
  - `1-2 min` JetBrains Mono 13 pt `#F0EDE8`
- Mechanism: `Acidifies the surface. Prevents alkaline drag-in from contaminating the expensive Pd catalyst bath.` Inter Regular 12 pt `#F0EDE8` at 70%

**Arrow: Step 1 to Step 2**

**Tank 2 -- Sn/Pd Catalyst (X: 8.0", W: 7.5", H: 6.5"):**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- FULL border overlay: 2 pt `#E8A020` (highlighted -- most critical step)
- Title: `STEP 2: Sn/Pd CATALYST` Barlow SemiBold 18 pt `#E8A020`
- Inside labels:
  - `Pd: 100-250 mg/L` JetBrains Mono 14 pt `#E8A020`
  - `Sn: 15-40 g/L` JetBrains Mono 14 pt `#2EC4B6`
  - `HCl: 150-250 mL/L` JetBrains Mono 13 pt `#F0EDE8`
  - `35-45 C (95-113 F)` JetBrains Mono 13 pt `#F0EDE8`
  - `3-7 min` JetBrains Mono 13 pt `#F0EDE8`
- Mechanism: `Colloidal Sn/Pd particles adsorb onto conditioned dielectric. Sn2+ reduces Pd2+ to metallic Pd0 nuclei on the surface.` Inter Regular 12 pt `#F0EDE8` at 70%
- Cost callout: `$50-200+ per liter -- MOST EXPENSIVE STEP` Barlow SemiBold 12 pt `#E05C5C`

**Arrow: Step 2 to Step 3**

**Tank 3 -- Accelerator (X: 16.0", W: 7.5", H: 6.5"):**
- Rounded rect, fill `#252B3D`, border 3 pt `#C8D0D8`
- Title: `STEP 3: ACCELERATOR` Barlow SemiBold 18 pt `#2EC4B6`
- Inside labels:
  - `HCl 50-100 mL/L (or fluoboric acid)` JetBrains Mono 13 pt `#2EC4B6`
  - `25-45 C` JetBrains Mono 13 pt `#F0EDE8`
  - `2-5 min` JetBrains Mono 13 pt `#F0EDE8`
- Mechanism: `Removes excess Sn from the colloidal shell, exposing bare Pd0 nuclei that are catalytically active for Cu2+ reduction.` Inter Regular 12 pt `#F0EDE8` at 70%

**Bottom summary callout (Y: 12.8" to 14.3"):**
- Rounded rect, fill `#1E2435`, border-left 0.06" `#E8A020`
- `Result: bare Pd nuclei on the dielectric surface. When this surface enters the E-Cu bath, Cu2+ ions are reduced to metallic copper at each Pd site. Once the first Cu layer deposits, the copper itself becomes catalytic -- the reaction is now autocatalytic and self-sustaining.`

---

### ZONE 4 -- Activation Parameters

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.7".

**Three-column parameter table:**

**Left -- Pre-Dip (X: 0.5", W: 7.0"):**
Header: `PRE-DIP` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Chemistry | HCl 150-250 mL/L |
| Temperature | Ambient |
| Time | 1-2 min |
| Purpose | Acidify surface; protect catalyst |
| Rinse after? | NO -- go directly to catalyst |

**Center -- Sn/Pd Catalyst (X: 7.83", W: 8.0"):**
Header: `Sn/Pd COLLOIDAL CATALYST` fill `#E8A020`.

| Parameter | Value |
|---|---|
| Pd concentration | 100-250 mg/L Pd |
| Sn concentration | 15-40 g/L Sn |
| HCl concentration | 150-250 mL/L |
| Temperature | 35-45 C (95-113 F) |
| Time | 3-7 min |
| Mechanism | Colloidal particles adsorb onto surface |
| Bath life | Monitor Pd by titration or ICP |

**Right -- Accelerator (X: 16.17", W: 7.33"):**
Header: `ACCELERATOR` fill `#3A4055`.

| Parameter | Value |
|---|---|
| Chemistry | HCl 50-100 mL/L, or fluoboric acid, or proprietary |
| Temperature | 25-45 C |
| Time | 2-5 min |
| Purpose | Strip Sn shell, expose Pd nuclei |
| Over-acceleration | Strips Pd too -- reduces Cu coverage |

Data: JetBrains Mono 12 pt. Headers: Barlow SemiBold 14 pt.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT ACTIVATION` -- Y: 22.2".

**5-row problem table:**

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| No Cu deposition | Open through-holes; bare dielectric | Pd catalyst exhausted or poisoned | Replenish Pd; check for oxidizer drag-in |
| Patchy Cu coverage | Cu deposits on some areas, not others | Poor conditioning; uneven Pd adsorption | Check conditioner; increase catalyst time |
| Over-acceleration | Thin or patchy Cu; Pd stripped off | Accelerator too concentrated or too long | Reduce time; dilute accelerator |
| Catalyst drag-out | High Pd consumption; expensive waste | Poor drainage between tanks | Improve drain time (10-15 sec); add drag-out tank |
| Void in micro-via | No Cu in blind via | Air trapped in via prevents Pd contact | Improve agitation; vacuum degas; ultrasonic |

---

### ZONE 6 -- Direct Metallization + Safety

**Left -- Direct Metallization Alternative (X: 0.5", W: 11.0"):**

Title: `EMERGING: DIRECT METALLIZATION (NO Pd)` Barlow SemiBold 18 pt `#2EC4B6`

- Rounded rect fill `#1E2435`, left accent 0.06" `#2EC4B6`
- `Conductive polymer (PEDOT:PSS or polyaniline) deposited on dielectric`
- `Or: carbon/graphite-based direct metallization`
- `Eliminates expensive Pd catalyst entirely`
- `Simplifies waste treatment (no Sn, no Pd)`
- `Not universally adopted; some reliability concerns in high-layer-count boards`
- `Watch: gaining market share for cost and environmental reasons`

**Right -- Safety (X: 12.0", W: 11.5"):**

Title: `SAFETY -- ACTIVATION CHEMISTRY` `#E8A020`

- `HCl: corrosive vapor -- hood ventilation required`
- `Sn/Pd catalyst: contains concentrated HCl`
- `PdCl2: skin sensitizer; Pd compounds are toxic`
- `SnCl2: irritant; stains`
- `Chemical splash goggles + face shield`
- `Acid-resistant gloves and apron`
- `Eyewash + safety shower within 10 sec`
- `Pd waste: precious metal -- recover for recycling, not drain`

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Electroless Copper`. Version `v1.0 -- 2026`.

Disclaimer: `...typical industry values for Sn/Pd colloidal activation in electroless copper plating for PCB and plastics metallization. Catalyst formulations are proprietary -- consult your supplier TDS...`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Catalyst border `#E8A020` -> `#C8860A`.
**Export:** Six files -- `Activation E-Cu -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-tank hero is the signature visual for this poster. Unlike EN activation (which is a simple acid dip or zincate), E-Cu activation is a three-step chemical sequence involving colloidal chemistry. The cost callout on the Pd catalyst tank is important practical context -- in PCB shops, the catalyst is the single most expensive consumable after the copper plating solution itself.

The direct metallization callout positions the poster as forward-looking. PEDOT:PSS and carbon-based alternatives are real technologies gaining market share, and any PCB shop poster should acknowledge them.

---

*Alaina -- Poster #242 -- Construction Workup v1.0 -- 2026-04-26*
