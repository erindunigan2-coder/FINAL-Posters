---
Project: Plating Posters Inc
Poster Number: 226
Title: "Activation -- EN (Mid Phos)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 4)"
Process Scope: Activation for electroless nickel mid phosphorus line (Stage 3 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #226 -- Construction Workup
## Activation -- EN (Mid Phos)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of the EN Mid-P process. The substrate-dependent activation decision tree is identical to EN Low-P (Poster #218): steel is self-catalytic, aluminum needs zincate, copper is catalytic, non-conductors need colloidal Pd/Sn, and stainless steel may need a Wood's nickel strike. The activation chemistry does not change between EN-P classes -- the activation creates a catalytic surface for whichever EN bath follows.

The key Mid-P differentiator at this stage is the ENIG pathway: for PCB applications, the substrate is copper-clad laminate. Activation is via sodium persulfate microetch (not HCl acid dip), which creates a micro-roughened copper surface. No Pd catalyst is needed because copper is inherently catalytic for EN.

Hero visual: substrate decision tree showing the activation path for each material type, with the ENIG/copper path called out prominently.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate decision tree hero (Block B):** A branching flowchart: substrate type at top, branches to specific activation protocols. Built with rectangles and connecting lines. ENIG/copper path highlighted.
2. **Orientation strip (Block C):** Stage 3 highlighted.
3. **Zincate detail panel (Block E):** The double-zincate process for aluminum.
4. **ENIG microetch callout (Block F):** Sodium persulfate activation for PCB copper.
5. **H-embrittlement warning (Block G):** Prominent safety callout for high-strength steel.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted
ZONE 3 -- SUBSTRATE DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ACTIVATION PARAMETERS BY SUBSTRATE (14.5"--22.0" / ~7.5")
ZONE 5 -- COMMON PROBLEMS & FIXES (22.0"--28.0" / ~6.0")
ZONE 6 -- H-EMBRITTLEMENT WARNING + SAFETY (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `EN (Mid Phos) -- Stage 3 of 7` -- Barlow SemiBold, 34 pt, `#E8A020` (Amber). X: 0.5", Y: 1.4".

**Tagline:** `The substrate decides the activation. Steel is easy. Aluminum needs zincate. Copper (ENIG) needs microetch. Know your material, know your path.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean surface with invisible oxide film  -->  After: Catalytically active surface ready for EN deposition`

---

### ZONE 3 -- Substrate Decision Tree Hero

**Section label:** `ACTIVATION BY SUBSTRATE -- THE DECISION TREE` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 14.0")**

Central question box at top center:
- Rounded rect, X: 7.0", W: 10.0", H: 1.2", fill `#E8A020`, radius 8
- Text: `WHAT IS YOUR SUBSTRATE?` Barlow Condensed ExtraBold 22 pt `#1A1F2E`

Six branch boxes below, connected by vertical lines from question box:

**Branch 1 -- Steel / Iron (X: 0.5", Y: 7.0", W: 3.5", H: 5.5"):**
- Rounded rect fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `STEEL / IRON` Barlow SemiBold 16 pt `#2EC4B6`
- `HCl 10-20% v/v or H2SO4 10-30% v/v`
- `Ambient, 30-120 sec`
- `Steel is self-catalytic -- no Pd needed`
- Badge: `SIMPLEST PATH` fill `#27AE60`, 10 pt `#1A1F2E`

**Branch 2 -- Aluminum (X: 4.4", Y: 7.0", W: 3.5", H: 5.5"):**
- Top accent `#E8A020`
- Title: `ALUMINUM` Barlow SemiBold 16 pt `#E8A020`
- `1. Acid desmut (HNO3 50% v/v, 30-60 sec)`
- `2. Zincate (NaOH 120-150 g/L + ZnO 15-30 g/L, 30-60 sec)`
- `3. Strip (HNO3 50%, 15-30 sec)`
- `4. Double zincate (repeat step 2, 15-30 sec)`
- Badge: `MOST COMPLEX` fill `#E8A020`, 10 pt `#1A1F2E`

**Branch 3 -- Copper / Brass (X: 8.3", Y: 7.0", W: 3.5", H: 5.5"):**
- Top accent `#2EC4B6`
- Title: `COPPER / BRASS` Barlow SemiBold 16 pt `#2EC4B6`
- `H2SO4 10-20%, ambient, 30-60 sec`
- `Copper is catalytic -- no Pd needed`
- `Tarnished Cu: bright dip in HNO3 + H2SO4 first`

**Branch 4 -- ENIG / PCB Copper (X: 12.2", Y: 7.0", W: 3.5", H: 5.5"):**
- Top accent `#27AE60`
- Full border 2 pt `#27AE60` (highlighted -- the Mid-P signature application)
- Title: `ENIG / PCB COPPER` Barlow SemiBold 16 pt `#27AE60`
- `Na2S2O8 microetch: 100-200 g/L`
- `or H2SO4/H2O2: 50 mL/L + 20-40 mL/L`
- `Ambient, 30-60 sec`
- `Micro-roughens Cu for adhesion`
- Badge: `MID-P SIGNATURE` fill `#27AE60`, 10 pt `#1A1F2E`

**Branch 5 -- Stainless Steel (X: 16.1", Y: 7.0", W: 3.5", H: 5.5"):**
- Top accent `#E8A020`
- Title: `STAINLESS STEEL` Barlow SemiBold 16 pt `#E8A020`
- `Wood's nickel strike recommended:`
- `NiCl2 240 g/L + HCl 125 mL/L`
- `25-35 ASF, 3-5 min`
- `Or: HCl 20-50%, 1-2 min, quick transfer`

**Branch 6 -- Plastics / Non-Conductors (X: 20.0", Y: 7.0", W: 3.5", H: 5.5"):**
- Top accent `#E05C5C`
- Title: `PLASTICS / CERAMICS` Barlow SemiBold 16 pt `#E05C5C`
- `1. Etch (CrO3/H2SO4 or permanganate)`
- `2. Neutralize`
- `3. Colloidal Sn/Pd catalyst (35-45 C, 3-5 min)`
- `4. Accelerator (removes excess Sn)`
- Badge: `Cr6+ ETCH -- RoHS FLAG` fill `#E05C5C`, 10 pt `#1A1F2E`

---

### ZONE 4 -- Activation Parameters by Substrate

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.7".

**Full-width table (X: 0.5", W: 23.0"):**

| Substrate | Chemistry | Temp | Time | Catalytic? | Key Note |
|---|---|---|---|---|---|
| Carbon steel | HCl 10-20% v/v | Ambient | 30-120 sec | Self-catalytic | Simplest -- just remove oxide |
| High-strength steel | HCl 10-20% v/v | Ambient | 15-30 sec MAX | Self-catalytic | H-embrittlement risk -- minimize time |
| Aluminum (wrought) | Double zincate | 20-25 C | 30-60 sec per step | Via Zn layer | Double zincate for best adhesion |
| Aluminum (cast) | Desmut + zincate | 20-25 C | 30-60 sec each | Via Zn layer | Cast alloys need aggressive desmut |
| Copper / brass | H2SO4 10-20% | Ambient | 30-60 sec | Self-catalytic | No Pd needed |
| PCB copper (ENIG) | Na2S2O8 100-200 g/L | Ambient | 30-60 sec | Self-catalytic | Microetch for adhesion; no Pd |
| Stainless steel | Wood's Ni strike | 25-35 C | 3-5 min at 25-35 ASF | Via Ni strike | Passive oxide must be penetrated |
| ABS plastic | Sn/Pd colloidal | 35-45 C | 3-5 min | Via Pd catalyst | Requires etch + accelerator steps |

Header: `#3A4055`. Data: JetBrains Mono 12 pt. Notes: Inter Regular 11 pt at 70%.

---

### ZONE 5 -- Common Problems & Fixes

**Section label:** `WHAT GOES WRONG AT ACTIVATION` -- Y: 22.2".

**5-row problem table:**

| Problem | Symptom | Cause | Fix |
|---|---|---|---|
| Skip plating | EN does not initiate on portions of part | Under-activation; oxide still present | Extend time; check acid concentration |
| Poor adhesion | EN peels on tape test or bend | Zincate too thick (single zincate on Al) | Use double zincate; strip and re-zincate |
| Rough EN deposit | Grainy or nodular surface from start | Over-activation; excessive micro-etch | Reduce time; dilute acid |
| H-embrittlement | Delayed fracture on high-strength steel | Hydrogen absorbed during acid contact | Limit to 15-30 sec; bake within 4 hr |
| Persulfate drag-in (ENIG) | EN stabilizer degradation | Sodium persulfate carried to EN bath | Thorough DI rinse; monitor rinse conductivity |

---

### ZONE 6 -- H-Embrittlement Warning + Safety

**Section label:** `CRITICAL SAFETY -- HYDROGEN EMBRITTLEMENT` -- Barlow Condensed ExtraBold 24 pt `#E05C5C`. Y: 28.2".

**Left -- H-Embrittlement Panel (X: 0.5", W: 14.0"):**
- Rounded rect fill `#1E2435`, FULL border 2 pt `#E05C5C`
- Title: `HYDROGEN EMBRITTLEMENT WARNING` -- Barlow SemiBold 20 pt `#E05C5C`
- Body:
  - `High-strength steel (>= 1000 MPa UTS / >= 40 HRC) absorbs hydrogen during acid contact.`
  - `REQUIREMENTS:`
  - `* Limit acid activation to 15-30 seconds maximum`
  - `* Use anodic electroclean only (no cathodic) for these substrates`
  - `* Bake at 190-210 C within 4 hours of plating completion`
  - `* Hold for minimum 4 hours (per ASTM B849 / B850)`
- Spec: `Reference: ASTM B849, ASTM B850, AMS 2759/9` JetBrains Mono 12 pt `#E05C5C`

**Right -- Acid Handling Safety (X: 15.0", W: 8.5"):**
- Title: `ACID HANDLING SAFETY` -- `#E8A020`
- `HCl fumes: corrosive -- hood ventilation required`
- `H2SO4: exothermic on dilution -- add acid to water, NEVER reverse`
- `HNO3 (desmut/zincate strip): oxidizer + toxic NOx fumes`
- `Na2S2O8 (persulfate): strong oxidizer -- store away from organics`
- `Chemical splash goggles + face shield`
- `Acid-resistant gloves and apron`
- `Eyewash + safety shower within 10 sec`

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- EN (Mid Phos)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Activation parameters shown are typical industry values for substrates entering electroless nickel mid phosphorus (5-9% P) baths. Consult your process supplier for application-specific guidance. Source: General industry knowledge; ASTM B733.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. H-embrittlement border `#E05C5C` -> `#B83E3E`. ENIG highlight border `#27AE60` -> `#1E7A47`.
**Export:** Six files -- `Activation EN Mid-P -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The decision tree gains a sixth branch compared to the Low-P version (Poster #218): the ENIG/PCB copper path. This is the Mid-P signature application and deserves prominent visual treatment. The persulfate microetch is chemically distinct from HCl acid activation -- it is an oxidative etch that creates mechanical adhesion, not just oxide removal. The ENIG branch should be visually highlighted with a full Emerald border to signal "this is why Mid-P exists."

---

*Alaina -- Poster #226 -- Construction Workup v1.0 -- 2026-04-26*
