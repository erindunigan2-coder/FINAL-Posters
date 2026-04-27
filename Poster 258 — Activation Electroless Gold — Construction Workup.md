---
Project: Plating Posters Inc
Poster Number: 258
Title: "Activation -- Electroless Gold"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Activation for electroless gold (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessGold
  - Activation
  - ConstructionWorkup
  - Series2
  - ENIG
---

# Poster #258 -- Construction Workup
## Activation -- Electroless Gold

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation for electroless gold depends entirely on which gold process you are running. For immersion gold (ENIG), there is NO activation step -- the EN surface itself is the driving force for the galvanic displacement reaction. Gold deposits by stealing electrons from nickel. For autocatalytic gold on non-catalytic substrates, Pd activation or Sn/Pd colloidal activation is required, identical to the procedures used for other electroless processes.

This is the simplest poster in the cluster for ENIG users and the most detailed for autocatalytic gold users.

Hero visual: two-path decision diagram -- ENIG (no activation) vs. autocatalytic (Pd activation required).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Two-path decision hero (Block B):** ENIG path (no activation) vs. autocatalytic path (Pd activation).
2. **Displacement mechanism explanation (Block D):** How immersion gold works without activation.
3. **Autocatalytic activation parameters (Block E):** Pd activation details.
4. **Defect grid (Block F):** 4 activation-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:** Standard 7-zone layout.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- TWO-PATH DECISION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DISPLACEMENT MECHANISM (14.5"--20.5" / ~6.0")
ZONE 5 -- AUTOCATALYTIC ACTIVATION PARAMETERS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Immersion gold needs no activation -- the nickel IS the driving force. Autocatalytic gold needs a catalytic surface.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed EN surface or clean substrate  -->  After: Surface ready for gold deposition`

---

### ZONE 3 -- Two-Path Decision Hero

**Section label:** `WHICH GOLD PROCESS ARE YOU RUNNING?` -- Y: 4.4".

**BLOCK B -- Two-Path Decision Diagram**

Y: 5.0" to 14.0".

**Root node (top center):**
- Rounded rect, X: 5.0", Y: 5.0", W: 14.0", H: 1.5", fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Text: `IMMERSION GOLD OR AUTOCATALYTIC GOLD?` Barlow Condensed ExtraBold 22 pt `#E8A020`

**Two paths:**

**Left -- Immersion Gold / ENIG (X: 0.5", Y: 7.5"):**
- Rounded rect, W: 11.0", H: 5.5", fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `IMMERSION GOLD (ENIG / ENEPIG)` Barlow SemiBold 20 pt `#E8A020`
- Large centered text: `NO ACTIVATION REQUIRED` Barlow Condensed ExtraBold 28 pt `#27AE60`
- Content below:
  - `Immersion gold is a displacement reaction`
  - `The EN surface provides electrons for Au3+ reduction`
  - `No external activation, no Pd catalyst, no colloidal treatment`
  - `Parts go directly from EN rinse to gold bath`
  - `3 Ni0 + 2 Au3+ --> 3 Ni2+ + 2 Au0` JetBrains Mono 14 pt `#E8A020`
  - `The nickel dissolves. The gold deposits. Self-limiting.`

**Right -- Autocatalytic Gold (X: 12.5", Y: 7.5"):**
- Rounded rect, W: 11.0", H: 5.5", fill `#1E2435`, top accent `#27AE60` 4 pt
- Title: `AUTOCATALYTIC GOLD` Barlow SemiBold 20 pt `#27AE60`
- Content:
  - `Requires catalytic surface for initiation`
  - `Option 1: Pd activation from PdCl2/HCl`
  - `0.1--0.5 g/L Pd; 20--40 C; 30--60 sec`
  - `Option 2: Sn/Pd colloidal + accelerator`
  - `Same as E-Cu process activation`
  - `On metallic substrates: Pd flash or direct immersion`
  - `Once initiated, autocatalytic reaction sustains itself`

**Bottom callout (Y: 13.5"):**
- Full width, fill `#E8A020` at 10%, border 1 pt `#E8A020`
- `If you are running ENIG, skip this step. Proceed from EN rinse directly to the immersion gold bath.` Inter Medium 16 pt `#E8A020`

---

### ZONE 4 -- Displacement Mechanism

**Section label:** `HOW IMMERSION GOLD WORKS WITHOUT ACTIVATION` -- Y: 14.7".

**BLOCK D -- Mechanism Explanation (Y: 15.3" to 20.3")**

Full-width callout, rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

**Visual: simplified three-step diagram (horizontal):**

Step 1: `EN Surface (Ni-P)` -- Emerald box showing nickel atoms
Arrow: `Au3+ arrives from solution`
Step 2: `Ni dissolves, releases electrons` -- Arrow showing Ni --> Ni2+ + 2e-
Step 3: `Au3+ + 3e- --> Au0 deposits` -- Amber box showing gold atoms replacing nickel

**Key principles (below diagram):**
- `Nickel is less noble than gold (Ni: -0.26V vs Au: +1.50V in EMF series)` JetBrains Mono 13 pt `#F0EDE8`
- `The potential difference drives spontaneous displacement` Inter Regular 14 pt `#F0EDE8`
- `Reaction is SELF-LIMITING: once gold covers all nickel, no more nickel can dissolve` Inter Medium 14 pt `#E8A020`
- `Result: ultra-thin gold layer (0.03--0.1 um) -- no thicker, ever`
- `If gold bath is too aggressive: excessive Ni corrosion = BLACK PAD` Inter Medium 14 pt `#E05C5C`

---

### ZONE 5 -- Autocatalytic Activation Parameters

**Section label:** `AUTOCATALYTIC GOLD -- ACTIVATION DETAILS` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Pd Activation (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `Pd ACTIVATION (DIRECT)` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Value |
|---|---|
| Chemistry | PdCl2 in HCl |
| Pd concentration | 0.1--0.5 g/L |
| Temperature | 20--40 C |
| Time | 30--60 seconds |
| Purpose | Deposit Pd nuclei as catalytic initiation sites |
| Substrates | Metallic and non-metallic |

**Right -- Sn/Pd Colloidal (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `Sn/Pd COLLOIDAL ACTIVATION` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Chemistry | SnCl2/PdCl2 colloidal in HCl |
| Temperature | 35--45 C |
| Time | 3--7 minutes |
| Accelerator | Dilute HCl, 2--5 min (removes excess Sn) |
| Purpose | Deposit Pd nuclei on non-conductive substrates |
| Substrates | Ceramics, polymers, glass |

---

### ZONE 6 -- Defect Grid

**Section label:** `ACTIVATION-RELATED GOLD DEFECTS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP PLATING (AUTO) | `#E05C5C` | Poor Pd activation on substrate | Verify activation; increase Pd concentration |
| R1C2 | DELAYED INITIATION (AUTO) | `#E8A020` | Oxidized substrate or weak Pd activation | Reduce transfer time; refresh activation bath |
| R2C1 | NO GOLD (ENIG) | `#E05C5C` | EN surface passivated or contaminated | Verify EN quality; rinse properly; check bath activity |
| R2C2 | EXCESS Ni CORROSION (ENIG) | `#E05C5C` | Immersion gold bath too aggressive (high Au, high temp) | Reduce Au concentration or temperature; check pH |

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Electroless Gold`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard table.
**Export:** Six files -- `Activation Electroless Gold -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The two-path decision diagram is simpler than Poster #250's three-path tree because there are only two choices here. The "NO ACTIVATION REQUIRED" text for immersion gold should be large and bold -- most ENIG operators need this reinforcement. The displacement mechanism explanation in Zone 4 is the educational core -- it connects the EMF series to the self-limiting nature of immersion gold and introduces the black pad risk in a single visual sequence. This is the poster that builds the foundation for understanding the Main Tank poster (#260).

---

*Alaina -- Poster #258 -- Construction Workup v1.0 -- 2026-04-26*
