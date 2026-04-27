---
Project: Plating Posters Inc
Poster Number: 274
Title: "Activation -- EN Boron"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 4)"
Technical Source: Substrate-dependent activation for EN-B deposition. Same protocols as EN-P with EN-B-specific notes. Watson notes EN-B is less sensitive to marginal activation than EN-P. Watson domain expertise.
Process Scope: Activation stage (Stage 3 of 8) for electroless nickel-boron plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #274 -- Construction Workup
## Activation -- EN Boron

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation for EN-B follows the same substrate-dependent protocols as EN-P (steel: acid activation; aluminum: double zincate; stainless: Wood's nickel strike; plastics: Sn/Pd colloidal). Watson notes a key EN-B-specific insight: the EN-B bath is highly active and will initiate on most clean metallic surfaces. Some operators report EN-B is less sensitive to marginal activation than EN-P -- but proper activation is still required for specification-grade adhesion.

Hero visual: substrate activation decision tree (same template as Poster #266).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation decision tree hero (Block B):** Four substrate pathways -- steel, aluminum, stainless, plastics.
2. **Activation parameters by substrate (Block D):** Four detailed callout boxes.
3. **EN-B specific insight panel (Block E):** "Less sensitive to marginal activation" callout.
4. **Safety + troubleshooting (Block F):** H-embrittlement warning for high-strength steel.

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
ZONE 5 -- EN-B SPECIFIC INSIGHTS (20.5"--26.5" / ~6.0")
ZONE 6 -- SAFETY + TROUBLESHOOTING (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Same activation playbook as EN-P. Steel is catalytic. Aluminum needs zincate. Stainless needs a Wood's strike. But EN-B is more forgiving at initiation.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, rinsed substrate  -->  After: Catalytically active surface ready for EN-B deposition`

---

### ZONE 3 -- Activation Decision Tree Hero

**Section label:** `WHICH ACTIVATION FOR YOUR SUBSTRATE?` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Y: 5.0" to 14.0". Same template as Poster #266.

**Four branches:**

| Branch | Substrate | Method | Parameters |
|---|---|---|---|
| 1 | Steel / Iron | Acid activation | HCl 10--20% or H2SO4 10--30%; ambient; 30--120 sec |
| 2 | Aluminum | Double zincate | Desmut -> Zincate -> Strip -> Zincate (NaOH 120--150 g/L + ZnO 15--30 g/L) |
| 3 | Stainless Steel | Wood's nickel strike | 240 g/L NiCl2 + 125 mL/L HCl; 25--35 ASF; 3--5 min |
| 4 | Plastics (ABS, PC) | Sn/Pd colloidal | Etch + catalyze + accelerate (see Poster #266 for full sequence) |

Each branch box includes accent color, substrate name, method, and key parameters per the Poster #266 template.

---

### ZONE 4 -- Activation Parameters by Substrate

**Section label:** `ACTIVATION PARAMETERS -- DETAILED` -- Y: 14.7".

**BLOCK D -- Four Parameter Boxes (Y: 15.3" to 20.3")**

2x2 grid:

**Steel / Iron (X: 0.5", Y: 15.3", W: 11.0", H: 2.3"):**
- Accent: `#2EC4B6`
- `HCl 10--20% v/v or H2SO4 10--30% v/v`
- `Ambient (20--30 C); 30--120 seconds`
- `Dissolves surface oxide; exposes active metal`
- `Steel is inherently catalytic for EN-B -- no Pd required`

**Aluminum (X: 12.0", Y: 15.3", W: 11.5", H: 2.3"):**
- Accent: `#E8A020`
- `Step 1: Acid desmut (50% HNO3; 30--60 sec)`
- `Step 2: Zincate (NaOH 120--150 g/L + ZnO 15--30 g/L; 30--60 sec)`
- `Step 3: Strip (50% HNO3; 15--30 sec)`
- `Step 4: Double zincate (repeat; 15--30 sec)`
- `Double zincate dramatically improves adhesion`

**Stainless Steel (X: 0.5", Y: 17.8", W: 11.0", H: 2.3"):**
- Accent: `#27AE60`
- `Wood's nickel strike: NiCl2 240 g/L + HCl 125 mL/L`
- `25--35 ASF; 3--5 min`
- `Alternative: 20--50% HCl, ambient, 1--2 min (transfer quickly)`

**Plastics (X: 12.0", Y: 17.8", W: 11.5", H: 2.3"):**
- Accent: `#E05C5C`
- `CrO3/H2SO4 etch (or permanganate for RoHS)`
- `Sn/Pd colloidal catalyst + accelerator`
- `EN-B on plastics is uncommon -- primarily for wear-resistant housings`

---

### ZONE 5 -- EN-B Specific Insights

**Section label:** `EN-B ACTIVATION -- WHAT MAKES IT DIFFERENT` -- Y: 20.7".

**BLOCK E -- Two Insight Panels (Y: 21.3" to 26.3")**

**Left -- "More Forgiving" Insight (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `EN-B IS MORE FORGIVING` Barlow SemiBold 18 pt `#27AE60`
- `The EN-B bath is highly active due to the strong reducing power of DMAB`
- `EN-B will initiate on most clean metallic surfaces with less sensitivity to marginal activation`
- `This does NOT mean you can skip activation`
- `Proper activation is still required for specification-grade adhesion per ASTM B841`
- `"Less sensitive" means more tolerant of imperfect activation -- not immune to poor prep` Inter Medium 13 pt `#E8A020`

**Right -- HE Risk for Wear Applications (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `HYDROGEN EMBRITTLEMENT RISK` Barlow SemiBold 18 pt `#E05C5C`
- `EN-B wear applications frequently involve high-strength steel`
- `Acid activation introduces hydrogen into high-strength substrates`
- `ASTM B849 -- Pre-treatment requirements for HE bake`
- `ASTM B850 -- Post-plating HE bake (190--210 C, 2--23 hrs)`
- `HE bake MUST occur within 4 hours of plating for steels >1000 MPa UTS`
- `Cathodic electroclean also introduces hydrogen -- minimize time` Inter Medium 12 pt `#E05C5C`

---

### ZONE 6 -- Safety + Troubleshooting

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Safety (X: 0.5", W: 11.0"):**

| Hazard | Detail |
|---|---|
| HCl / H2SO4 | Corrosive; splash goggles + face shield + nitrile gloves |
| HNO3 (desmut/strip) | Strong oxidizer; fumes; local exhaust ventilation |
| NiCl2 (Wood's strike) | Nickel salts -- IARC Group 1 as aerosol; minimize mist |
| Chromic acid (plastic etch) | Cr6+ -- IARC Group 1 carcinogen; full PPE |

**Right -- Troubleshooting (X: 12.0", W: 11.5"):**

| Problem | Cause | Fix |
|---|---|---|
| Skip plating | Activation too brief or incomplete | Extend time; verify coverage |
| Blistering | Over-activation (excess metal removal) | Reduce activation time |
| Poor adhesion on Al | Single zincate or weak zincate | Always double zincate; verify NaOH/ZnO |
| Uneven deposition | Non-uniform activation | Improve agitation; verify immersion |

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- EN Boron`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; EN-B activation follows established electroless nickel protocols. ASTM B849/B850 for hydrogen embrittlement relief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation EN Boron -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The EN-B activation poster shares the same substrate-dependent framework as all EN activation posters. The two unique EN-B-specific insights are: (1) EN-B is more forgiving at initiation due to DMAB's strong reducing power, and (2) the high-strength steel HE risk is especially relevant because EN-B's primary market is wear applications on hardened steel. The HE bake callout (ASTM B849/B850) is important practical content.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #274 -- Construction Workup v1.0*
*2026-04-26*
