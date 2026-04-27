---
Project: Plating Posters Inc
Poster Number: 266
Title: "Activation -- Electroless Cobalt"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt, Poster 4)"
Technical Source: Substrate-dependent activation for electroless cobalt deposition. Copper and nickel substrates are catalytic for cobalt, but Pd flash activation improves reliability. Silicon wafer activation (HF + Pd) is unique to MEMS applications. Watson domain expertise.
Process Scope: Activation stage (Stage 3 of 8) for electroless cobalt plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #266 -- Construction Workup
## Activation -- Electroless Cobalt

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation creates a catalytically active surface that initiates the autocatalytic cobalt deposition reaction. Without proper activation, deposition will not start -- skip plating. Electroless cobalt has an interesting activation profile: copper and nickel are inherently catalytic for cobalt reduction (though initiation may be slow), while non-conductive substrates and silicon wafers require Sn/Pd colloidal or Pd seed activation.

Hero visual: substrate activation decision tree showing the four pathways (copper/nickel, non-conductive, silicon, stainless steel).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation decision tree hero (Block B):** Central decision diamond ("What is your substrate?") branching to four pathways. Built with rectangles, diamonds, and connecting arrows.
2. **Activation parameters by substrate (Block D):** Four detailed callout boxes, one per substrate type.
3. **Sn/Pd colloidal process detail (Block E):** Step sequence for non-conductive substrates.
4. **Safety callout (Block F):** HF hazard warning for silicon wafer activation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

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
ZONE 5 -- SN/PD COLLOIDAL PROCESS (20.5"--26.5" / ~6.0")
ZONE 6 -- SAFETY + TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Cobalt -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The substrate determines the activation method. Copper and nickel are catalytic for cobalt -- everything else needs help.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, rinsed substrate  -->  After: Catalytically active surface ready for cobalt deposition`

---

### ZONE 3 -- Activation Decision Tree Hero

**Section label:** `WHICH ACTIVATION FOR YOUR SUBSTRATE?` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Y: 5.0" to 14.0".

**Central decision diamond:**
- Diamond shape (rotated square), X: center, Y: 6.0", W: 5.0", H: 3.0", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Text: `WHAT IS YOUR SUBSTRATE?` Barlow SemiBold 18 pt `#E8A020`

**Four branches radiating outward:**

| Branch | Direction | Target Box | Fill | Accent | Substrate | Method |
|---|---|---|---|---|---|---|
| 1 | Upper-left | X: 0.5", Y: 5.0" | `#1E2435` | `#27AE60` | Copper / Nickel | Direct immersion (catalytic) |
| 2 | Upper-right | X: 16.0", Y: 5.0" | `#1E2435` | `#2EC4B6` | Non-Conductive (ABS, PC) | Sn/Pd colloidal + accelerator |
| 3 | Lower-left | X: 0.5", Y: 10.5" | `#1E2435` | `#E8A020` | Silicon Wafers (MEMS) | HF dip + Pd activation |
| 4 | Lower-right | X: 16.0", Y: 10.5" | `#1E2435` | `#2EC4B6` | Stainless Steel | HCl activation or Pd flash |

Each branch box: Rounded rect W: 7.0", H: 3.0", left accent 0.06".
- Substrate name: Barlow SemiBold 18 pt, accent color
- Method: Inter Regular 14 pt `#F0EDE8`
- Key note: Inter Regular 12 pt `#F0EDE8` at 70%

Connecting arrows from diamond to each box: 3 pt `#3A4055`.

---

### ZONE 4 -- Activation Parameters by Substrate

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.7".

**BLOCK D -- Four Parameter Boxes (Y: 15.3" to 20.3")**

2x2 grid:

**Copper / Nickel (X: 0.5", Y: 15.3", W: 11.0", H: 2.3"):**
- Accent: `#27AE60`
- `Direct immersion -- Cu and Ni are catalytic for Co deposition`
- `Brief Pd flash activation (0.1--0.5 g/L PdCl2 in HCl, 30 sec) improves reliability`
- `Initiation may be slow without Pd -- allow 2--5 min for visible deposition`

**Non-Conductive Substrates (X: 12.0", Y: 15.3", W: 11.5", H: 2.3"):**
- Accent: `#2EC4B6`
- `Etch: CrO3 400 g/L + H2SO4 400 g/L, 65--70 C, 5--15 min (or permanganate for RoHS)`
- `Activate: Sn/Pd colloidal catalyst, 35--45 C, 3--5 min`
- `Accelerate: dilute HCl, remove excess Sn`

**Silicon Wafers -- MEMS (X: 0.5", Y: 17.8", W: 11.0", H: 2.3"):**
- Accent: `#E8A020`
- `HF dip: 10--50% HF, 30--60 sec (removes native SiO2)`
- `Pd activation: PdCl2 0.1--0.5 g/L in HCl, 30--60 sec`
- `Alternative: sputtered Pd seed layer (vacuum-deposited)`

**Stainless Steel (X: 12.0", Y: 17.8", W: 11.5", H: 2.3"):**
- Accent: `#2EC4B6`
- `HCl activation: 20--50% HCl, ambient, 1--2 min`
- `Transfer quickly to Co bath after activation`
- `Pd flash (0.1--0.5 g/L PdCl2) optional but improves initiation`

---

### ZONE 5 -- Sn/Pd Colloidal Process

**Section label:** `SN/PD COLLOIDAL ACTIVATION -- STEP BY STEP` -- Y: 20.7".

**BLOCK E -- Process Flow Strip (Y: 21.3" to 26.3")**

Horizontal flow of 5 steps:

| Step | Box | Chemistry | Time | Temp |
|---|---|---|---|---|
| 1 | Etch | CrO3/H2SO4 (or KMnO4) | 5--15 min | 65--70 C |
| 2 | Neutralize | Dilute acid rinse | 30--60 sec | Ambient |
| 3 | Catalyze | SnCl2 + PdCl2 in HCl | 3--5 min | 35--45 C |
| 4 | Accelerate | Dilute HCl | 1--3 min | Ambient |
| 5 | Rinse | DI water | 30--60 sec | Ambient |

Each step box: Rounded rect W: 4.2", H: 3.5", fill `#1E2435`, top accent 4 pt `#E8A020`.
Arrows between: 3 pt `#3A4055`.

Below strip:
- `NOTE: Chromic acid etch uses hexavalent chromium -- RoHS compliance requires permanganate alternative` Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Safety + Troubleshooting

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Safety Callouts (X: 0.5", W: 11.0"):**

Section label: `SAFETY ALERTS` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Hazard | Detail |
|---|---|
| HF (silicon activation) | EXTREMELY corrosive; penetrates skin causing deep tissue damage; calcium gluconate gel must be on-site; immediate medical attention required for any exposure |
| Chromic acid (plastic etch) | Hexavalent chromium -- IARC Group 1 carcinogen; full PPE required; local exhaust ventilation mandatory |
| PdCl2 / HCl | Corrosive; Pd salts are sensitizers; nitrile gloves + splash goggles minimum |

Each row: left accent `#E05C5C`, text `#F0EDE8`.

**Right -- Activation Troubleshooting (X: 12.0", W: 11.5"):**

Section label: `IF ACTIVATION FAILS` Barlow Condensed ExtraBold 22 pt `#E8A020`.

| Problem | Cause | Fix |
|---|---|---|
| Skip plating | Inadequate activation or surface re-oxidation | Extend activation time; minimize transfer time to Co bath |
| Blistering | Over-activation or contaminated activator | Reduce activation time; replace exhausted Pd solution |
| Uneven initiation | Non-uniform activation coverage | Improve agitation during activation; verify complete immersion |

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Electroless Cobalt`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; activation protocols for electroless cobalt follow established electroless plating practice with substrate-specific modifications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Electroless Cobalt -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The activation poster for electroless cobalt is more varied than for EN because cobalt is used on a wider range of substrates -- notably silicon wafers for MEMS applications. The decision tree hero is the key differentiator. The HF safety callout for silicon wafer activation must be visually prominent -- HF is uniquely dangerous among plating chemicals. Watson notes that Cu/Ni are catalytic for Co but initiation may be slow; the Pd flash recommendation is a practical tip.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #266 -- Construction Workup v1.0*
*2026-04-26*
