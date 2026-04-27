---
Project: Plating Posters Inc
Poster Number: 246
Title: "Post Treatment -- Electroless Copper"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 8)"
Technical Source: Post-treatment options for electroless copper deposits. Covers the two primary pathways: (1) PCB through-hole -- no standalone post-treatment; proceed directly to electrolytic acid copper buildup; (2) EMI shielding / plastics metallization -- anti-tarnish dip and optional annealing. Includes annealing parameters with glass transition temperature (Tg) limits for plastic substrates.
Process Scope: Electroless copper -- Stage 8 of 8 (post-treatment / final)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #246 -- Construction Workup
## Post Treatment -- Electroless Copper

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 8 of the electroless copper process -- the final poster in the EL-04 Electroless Copper cluster. Post-treatment for E-Cu splits cleanly into two paths based on application:

**Path 1 -- PCB Through-Hole:** There is no standalone post-treatment. The E-Cu seed layer (0.5-2.5 um) proceeds directly to electrolytic acid copper buildup (25-50 um). The electroless copper deposit is purely a conductive bridge -- it exists only to make the non-conductive through-hole walls electrically conductive for electrolytic deposition. Once the electrolytic copper is on, the E-Cu layer is buried and its job is done.

**Path 2 -- EMI Shielding / Plastics Metallization:** The E-Cu deposit IS the functional coating. Post-treatment includes anti-tarnish passivation (benzotriazole or trivalent chromate) and optional annealing to improve ductility and adhesion. Annealing on plastic substrates requires strict temperature limits based on the glass transition temperature (Tg) of the substrate.

The Tg limitation is the critical educational element here. Annealing above Tg causes the plastic to soften and deform, destroying adhesion and part geometry. Each common substrate material has a different Tg, and operators need this information on the wall.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Application decision tree hero (Block B):** PCB vs. EMI shielding vs. plastics metallization.
2. **Orientation strip (Block C):** 8-stage strip, Stage 8 highlighted.
3. **Annealing parameters with Tg limits (Block D).**
4. **Anti-tarnish / passivation options (Block E).**
5. **Troubleshooting strip (Block F).**

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
  Stage 8 highlighted (Amber)
ZONE 3 -- APPLICATION DECISION TREE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ANNEALING & Tg LIMITS (14.5"--22.0" / ~7.5")
ZONE 5 -- ANTI-TARNISH & PASSIVATION (22.0"--28.0" / ~6.0")
ZONE 6 -- TROUBLESHOOTING (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Stage 8 of 8` -- Barlow SemiBold, 32 pt, `#E8A020` (Amber). X: 0.5", Y: 1.4".

**Tagline:** `The application defines the path. PCB through-hole? No post-treatment -- proceed to electrolytic copper. EMI shielding or plastics? Anti-tarnish and optional anneal.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Rinsed E-Cu deposit (0.5-2.5 um seed or 25-50 um functional)  -->  After: Application-ready surface`

---

### ZONE 3 -- Application Decision Tree Hero

**Section label:** `WHAT IS YOUR APPLICATION? -- THE PATH SPLITS HERE` -- Y: 4.4".

**BLOCK B -- Decision Tree (Y: 5.0" to 14.0")**

**Root node (top center):**
- Rounded rect, X: 7.0", Y: 5.0", W: 10.0", H: 1.2", fill `#E8A020` at 30%, border 2 pt `#E8A020`
- Text: `WHAT IS THE E-Cu DEPOSIT FOR?` Barlow Condensed ExtraBold 20 pt `#E8A020`

**Three branch nodes (Y: 7.0"):**

| Branch | X | W | Accent | Application | Post-Treatment |
|---|---|---|---|---|---|
| Left | 0.5" | 7.33" | `#27AE60` | PCB THROUGH-HOLE | No post-treatment. Proceed directly to electrolytic acid copper (25-50 um). E-Cu is a seed layer only. |
| Center | 8.17" | 7.33" | `#2EC4B6` | EMI SHIELDING | Anti-tarnish dip (BTA or trivalent chromate). Optional anneal: 150-200 C, 1-2 hr. Functional copper coating. |
| Right | 15.83" | 7.67" | `#E8A020` | PLASTICS METALLIZATION | Anti-tarnish + anneal for adhesion. Temperature MUST stay below substrate Tg. Decorative or functional copper. |

Each branch: Rounded rect, H: 6.5", fill `#1E2435`, left accent 0.06".

**Inside each branch:**

*PCB Through-Hole:*
- Badge: `NO POST-TREATMENT` fill `#27AE60`
- `Proceed directly to electrolytic copper` Barlow SemiBold 18 pt `#27AE60`
- `The E-Cu deposit is a conductive bridge:` Inter Regular 13 pt `#F0EDE8`
- `  - 0.5-2.5 um seed layer on through-hole walls` Inter Regular 13 pt `#F0EDE8`
- `  - Makes non-conductive FR4 electrically conductive` Inter Regular 13 pt `#F0EDE8`
- `  - Electrolytic acid Cu builds to 25-50 um` Inter Regular 13 pt `#F0EDE8`
- `  - E-Cu layer is permanently buried` Inter Regular 13 pt `#F0EDE8`
- `DO NOT allow air exposure delay` Inter Medium 13 pt `#E05C5C`
- `Transfer to electrolytic Cu within minutes` Inter Medium 12 pt `#E8A020`

*EMI Shielding:*
- Badge: `ANTI-TARNISH + OPTIONAL ANNEAL` fill `#2EC4B6`
- `E-Cu is the FUNCTIONAL coating` Barlow SemiBold 16 pt `#2EC4B6`
- `Thickness: 25-50 um (heavy-build E-Cu)` JetBrains Mono 14 pt `#2EC4B6`
- `Conductivity: 90-95% IACS` JetBrains Mono 13 pt `#F0EDE8`
- `Anti-tarnish: BTA or trivalent chromate dip` Inter Regular 13 pt `#F0EDE8`
- `Anneal: 150-200 C, 1-2 hr` JetBrains Mono 13 pt `#F0EDE8`
- `Improves ductility and adhesion` Inter Regular 12 pt `#F0EDE8`
- `Common substrates: injection-molded plastic housings, enclosures` Inter Regular 11 pt `#F0EDE8` at 70%

*Plastics Metallization:*
- Badge: `ANNEAL WITH Tg LIMIT` fill `#E8A020`
- `E-Cu is the DECORATIVE or FUNCTIONAL coating` Barlow SemiBold 16 pt `#E8A020`
- `Anti-tarnish: BTA or trivalent chromate` Inter Regular 13 pt `#F0EDE8`
- `Anneal: 150-200 C, 1-2 hr` JetBrains Mono 13 pt `#F0EDE8`
- `CRITICAL: anneal temperature MUST be` Inter Medium 13 pt `#E05C5C`
- `BELOW the substrate Tg` Inter Medium 14 pt `#E05C5C`
- `Above Tg: plastic softens, deforms,` Inter Regular 13 pt `#E05C5C`
- `adhesion destroyed, part geometry lost` Inter Regular 13 pt `#E05C5C`
- `See Tg table below (Zone 4)` Inter Medium 12 pt `#E8A020`

---

### ZONE 4 -- Annealing & Tg Limits

**Section label:** `ANNEALING -- GLASS TRANSITION TEMPERATURE LIMITS` -- Y: 14.7".

**BLOCK D -- Annealing Parameters + Tg Table (Y: 15.3" to 21.5")**

**Left -- Annealing Parameters (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ANNEALING PARAMETERS` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`):
```
Purpose:
  Improve ductility of E-Cu deposit
  Improve adhesion to plastic substrate
  Relieve internal stress in deposit

Parameters:
  Temperature: 150-200 C (300-390 F)
  Time: 1-2 hours
  Atmosphere: Air (standard)
  Ramp rate: Slow (2-5 C/min) to avoid
    thermal shock to plastic substrate

Key rules:
  1. NEVER exceed substrate Tg
  2. Ramp slowly -- thermal shock cracks
     the E-Cu deposit on rigid plastics
  3. Cool slowly -- same reason
  4. For multi-layer parts, use the LOWEST
     Tg of any material in the assembly
```

**Right -- Substrate Tg Table (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `SUBSTRATE GLASS TRANSITION TEMPERATURES` Barlow SemiBold 16 pt `#E05C5C`

| Substrate | Tg | Max Anneal Temp | Notes |
|---|---|---|---|
| ABS | ~105 C (221 F) | 90-95 C | Most common E-Cu substrate for decorative |
| Polycarbonate (PC) | ~147 C (297 F) | 130-140 C | EMI shielding housings |
| FR4 (standard) | ~130-140 C (266-284 F) | 120-130 C | PCB laminate (if annealing PCB) |
| FR4 (high Tg) | ~170 C (338 F) | 155-165 C | High-reliability PCB |
| Polyetherimide (PEI/Ultem) | ~217 C (423 F) | 200 C | Aerospace / medical |
| LCP (liquid crystal polymer) | ~280 C (536 F) | 250 C | High-performance connectors |

Data: JetBrains Mono 11 pt. Substrate column: Inter Medium 12 pt `#F0EDE8`.
Alternating rows: `#1E2435` / `#252B3D`.

**Warning bar below table:**
- Rounded rect, X: 0.5", W: 23.0", H: 0.8", fill `#E05C5C` at 15%
- `ABS is the most common E-Cu plastic substrate and has the LOWEST Tg. Standard anneal at 150-200 C EXCEEDS ABS Tg. For ABS parts, anneal at 90-95 C maximum or skip anneal entirely.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Anti-Tarnish & Passivation

**Section label:** `ANTI-TARNISH & SURFACE PROTECTION` -- Y: 22.2".

**BLOCK E -- Two Panels (Y: 22.8" to 27.8")**

**Left -- Anti-Tarnish Methods (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.6", fill `#1E2435`, left accent `#27AE60`
- Title: `ANTI-TARNISH OPTIONS` Barlow SemiBold 18 pt `#27AE60`

| Method | Chemistry | Time | Mechanism |
|---|---|---|---|
| BTA (benzotriazole) | 0.1-1% BTA in water or IPA | 15-30 sec dip | Forms Cu-BTA molecular film; blocks O2 access |
| Trivalent chromate | Proprietary Cr3+ solution | 15-30 sec dip | Thin conversion coating; RoHS-compliant |
| OSP (organic solderability preservative) | Imidazole or BTA derivative | 15-60 sec dip | PCB-specific; preserves solderability |

Data: JetBrains Mono 11 pt.

Note: `All anti-tarnish treatments must be REMOVED before subsequent plating (if any). BTA and OSP are removed by mild acid or alkaline cleaning.` Inter Medium 12 pt `#E8A020`

**Right -- When No Protection Is Needed (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.6", fill `#1E2435`, left accent `#2EC4B6`
- Title: `WHEN TO SKIP ANTI-TARNISH` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`):
```
PCB through-hole:
  Parts go directly to electrolytic Cu
  No air exposure = no oxidation
  Anti-tarnish is unnecessary and would
  contaminate the electrolytic bath

Immediate electrolytic buildup:
  If the next step is electrolytic plating
  within minutes, skip anti-tarnish
  Fresh Cu surface is ideal for adhesion

Parts going to solder:
  OSP may be applied if boards are stored
  before wave or reflow soldering
  OSP protects Cu pads for solderability
```

---

### ZONE 6 -- Troubleshooting

**Section label:** `WHAT GOES WRONG AT POST-TREATMENT` -- Y: 28.2".

**Five problem cards (Y: 28.8" to 32.3"):**

| Card | X | W | Problem | Cause | Fix |
|---|---|---|---|---|---|
| 1 | 0.5" | 4.4" | DELAMINATION AFTER ANNEAL | Anneal temp exceeded substrate Tg; thermal shock | Reduce temp below Tg; slow ramp rate (2-5 C/min) |
| 2 | 5.2" | 4.4" | COPPER TARNISH (BROWN/BLACK) | Inadequate anti-tarnish; delay before application | Apply anti-tarnish immediately after rinse; check BTA concentration |
| 3 | 9.9" | 4.4" | CRACKED DEPOSIT AFTER ANNEAL | Thermal shock; ramp too fast; Cu deposit too thin | Slow ramp/cool rate; increase E-Cu thickness if possible |
| 4 | 14.6" | 4.4" | POOR SOLDERABILITY (PCB) | Oxidized Cu pads; no OSP applied; old boards | Apply OSP; store in N2 or vacuum; reduce storage time |
| 5 | 19.3" | 4.2" | WARPED PLASTIC SUBSTRATE | Anneal temp at or above Tg; non-uniform heating | Reduce anneal temp; check oven uniformity; verify Tg of actual resin |

Card construction: Rounded rect, H: 3.2", fill `#1E2435`, left accent 0.04" `#E05C5C`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Electroless Copper`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Post-treatment parameters and glass transition temperatures shown are typical values. Tg values vary by resin grade, filler content, and manufacturer. Always verify Tg from substrate supplier datasheet. Anneal parameters vary by E-Cu deposit thickness and substrate. Consult your process supplier TDS.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment E-Cu -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster mirrors the structure of Poster 238 (Post Treatment -- EN High Phos) with its application decision tree hero. The parallel is deliberate -- operators familiar with the EN post-treatment poster will immediately recognize the layout pattern and know how to read it. The difference is content: EN post-treatment is about the 260 C crystallization threshold and hydrogen embrittlement. E-Cu post-treatment is about substrate Tg limits and the PCB vs. non-PCB split.

The Tg table in Zone 4 is the most operationally critical content on this poster. The ABS warning bar is essential -- ABS is the most common plastic substrate for E-Cu, and the standard anneal range (150-200 C) exceeds its Tg (~105 C). This is a real production mistake that happens regularly, and it needs to be called out prominently.

This poster completes the EL-04 Electroless Copper cluster (Posters 239-246, 8 stages).

---

*Alaina -- Poster #246 -- Construction Workup v1.0 -- 2026-04-26*
