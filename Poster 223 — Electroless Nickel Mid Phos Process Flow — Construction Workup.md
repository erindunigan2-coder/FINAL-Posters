---
Project: Plating Posters Inc
Poster Number: 223
Title: "Electroless Nickel (Mid Phos) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P)"
Technical Source: Industry-standard electroless nickel mid phosphorus (5-9% P) plating process. Covers the complete 7-stage autocatalytic sequence. Values are typical ranges for acid-pH EN Mid-P baths per ASTM B733 Type IV.
Process Scope: Electroless nickel mid phosphorus (5-9% P) -- complete process flow (7 stages)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - ProcessFlow
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #223 -- Construction Workup
## Electroless Nickel (Mid Phos) -- Process Flow

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for EN Mid-P: Electroless Nickel Mid Phosphorus (5-9% P) -- the industry workhorse. More EN Mid-P is plated globally than all other EN classes combined. It is the standard ENIG base layer per IPC-4552B, the go-to for aerospace hydraulics (AMS 2404), and the default choice for general engineering. Fastest deposition rate of any EN-P class at 18-25 um/hr. Highest operating temperature at 85-91 C.

Design philosophy mirrors Poster #215 (EN Low-P Process Flow) with adapted chemistry, parameters, and emphasis on the "workhorse" positioning.

---

## Part 1 -- Workflow Orientation

### Design Capabilities and Limitations

Same as Poster #215. Seven-stage U-flow, parameter table, three-class comparison (with Mid-P highlighted), troubleshooting strip.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series standard.

**Ruler guides:** Same as Poster #215.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6")
  Block B: Seven-stage U-flow diagram
  Block C: Stage legend strip

ZONE 3 -- PARAMETER SUMMARY TABLE (15.5"--22.0" / ~6.5")
  Block D: 7-row parameter table

ZONE 4 -- WHY MID-P? COMPARISON (22.0"--28.5" / ~6.5")
  Block E: Low-P vs. Mid-P vs. High-P (Mid-P highlighted)

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0")
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROLESS NICKEL` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Mid Phosphorus (5-9% P) -- Complete Process Flow -- 7 Stages` -- 34 pt `#E8A020` (Amber -- used here to distinguish from Low-P's Emerald). X: 0.5", Y: 1.4".

**Tagline:** `The industry workhorse. Fastest deposition rate. ENIG standard. More Mid-P is plated worldwide than all other EN classes combined.` -- 20 pt at 65%. Y: 2.2".

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE COMPLETE PROCESS -- STAGE BY STAGE` -- Y: 3.1".

**BLOCK B -- Seven-Stage U-Flow**

Same layout geometry as Poster #215. Content differs:

**Top Row (Stages 1-4):**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 1. Alkaline Clean | Box 1 | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse (Pre-Act) | Box 2 | 6.0" | `#2EC4B6` (Teal) | Rinse |
| 3. Activation | Box 3 | 11.5" | `#E8A020` (Amber) | Activation |
| 4. Rinse (Pre-Plate) | Box 4 | 17.0" | `#2EC4B6` (Teal) | Rinse |

**Bottom Row (Stages 5-7):**

| Stage | Box | X | Top Accent | Type |
|---|---|---|---|---|
| 5. EN Mid-P Bath | Box 5 | 17.0" | `#27AE60` (Emerald) | Plating |
| 6. Rinse (Post-Plate) | Box 6 | 11.5" | `#2EC4B6` (Teal) | Rinse |
| 7. Post Treatment | Box 7 | 6.0" | `#E8A020` (Amber) | Post-Treatment |

**Inside each flow box:**

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters: `60-80 C (140-176 F)` / `NaOH 30-60 g/L` / `3-10 min soak`
- Purpose: `Remove oils, oxides, soils`
- Check: `CHECK: Water-break-free surface`

*Box 2 -- Rinse (Pre-Activation):*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Activation`
- Parameters: `Ambient temp` / `Counterflow 2-stage min`
- Purpose: `Remove alkaline cleaner drag-out`
- Check: `Target: < 50 uS/cm conductivity`

*Box 3 -- Activation:*
- Badge: `STAGE 3`, fill `#E8A020`
- Name: `Activation`
- Parameters: `HCl 10-20% (steel)` / `Na2S2O8 microetch (PCB/ENIG)` / `Zincate (aluminum)`
- Purpose: `Create catalytic surface for EN initiation`
- Check: `Copper (PCB) is self-catalytic -- no Pd needed` (`#27AE60`)

*Box 4 -- Rinse (Pre-Plate):*
- Badge: `STAGE 4`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Pre-Plate`
- Parameters: `DI preferred` / `Ambient, 30-60 sec`
- Purpose: `Remove acid/persulfate drag-in`
- Check: `CRITICAL: Persulfate drag-in degrades EN stabilizers` (Coral `#E05C5C`)

*Box 5 -- EN Mid-P Bath (Main Tank):*
- Badge: `STAGE 5`, fill `#27AE60`
- Name: `EN Mid-P Bath` / Subtitle: `Main Tank`
- Parameters: `Ni2+: 4.5-6.5 g/L` / `NaH2PO2: 20-30 g/L` / `pH 4.6-5.2 (ACID)` / `85-91 C (185-196 F)`
- Purpose: `Autocatalytic Ni-P deposition (5-9% P)`
- Check: `Rate: 18-25 um/hr | Bath life: 6-8 MTO`

*Box 6 -- Rinse (Post-Plate):*
- Badge: `STAGE 6`, fill `#2EC4B6`
- Name: `Rinse` / Subtitle: `Post-Plate`
- Parameters: `Cold water preferred` / `Double counterflow or spray`
- Purpose: `Stop EN reaction; remove drag-out`
- Check: `CRITICAL: Do not air-dry` (Coral `#E05C5C`)

*Box 7 -- Post Treatment:*
- Badge: `STAGE 7`, fill `#E8A020`
- Name: `Post Treatment`
- Parameters: `HE bake: 190-210 C, 2-23 hr` / `Hardness HT: 350-400 C, 1 hr` / `ENIG: no HT -- proceed to Au`
- Purpose: `Relieve hydrogen; develop hardness (850-1000 HV)`
- Check: `ENIG: skip HT -- go directly to immersion gold` (`#E8A020`)

**BLOCK C -- Stage Legend Strip:** Same as Poster #215.

---

### ZONE 3 -- Parameter Summary Table

**Section label:** `AT-A-GLANCE PARAMETERS` -- Y: 15.7".

| Stage | Chemistry | Temp | Time | Key Control |
|---|---|---|---|---|
| 1. Alkaline Clean | NaOH 30-60 g/L + surfactant | 60-80 C | 3-10 min | Water-break-free |
| 2. Rinse | DI or city water | Ambient | 30-60 sec | < 50 uS/cm conductivity |
| 3. Activation | HCl 10-20% (steel) / Persulfate (PCB) | Ambient | 30-120 sec | Substrate-dependent |
| 4. Rinse | DI preferred | Ambient | 30-60 sec | No persulfate/chloride drag-in |
| 5. EN Mid-P Bath | Ni2+ 4.5-6.5 g/L, pH 4.6-5.2 | 85-91 C | Per spec | 18-25 um/hr, +/-0.2 pH |
| 6. Rinse | DI or city water | Ambient (cold) | 30-60 sec | No air-dry |
| 7. Post Treatment | Oven / furnace (or Au for ENIG) | 190-400 C | 1-23 hr | HE bake within 4 hr |

---

### ZONE 4 -- Why Mid-P? Comparison

**Section label:** `THE THREE EN-P CLASSES -- LOW VS. MID VS. HIGH` -- Y: 22.2".

Same three-column comparison as Poster #215, but **Mid-P is highlighted** (full 2 pt border `#E8A020`).

**Left -- Low-P (2-4% P):**
- Left accent `#27AE60`. No full border.
- Properties same as Poster #215.
- Bottom: `Highest hardness. Ferromagnetic. Electronics specialist.`

**Center -- Mid-P (5-9% P) -- THIS POSTER:**
- Full border 2 pt `#E8A020` (highlighted)
- Title: `MID-P (5-9% P)` -- `#E8A020`
- Subtitle: `This Poster -- Industry Workhorse`

| Property | Value |
|---|---|
| pH | Acid (4.6-5.2) |
| Structure | Mixed crystalline/amorphous |
| Magnetic | Weakly magnetic at 5-6% P; non-magnetic at 8-9% P |
| Hardness (as-plated) | 500-600 HV |
| Hardness (HT) | 850-1000 HV |
| Corrosion (SST 25 um) | 240-500 hr |
| Solderability | Moderate (adequate for ENIG + Au) |
| Deposition rate | 18-25 um/hr (FASTEST) |

Bottom: `Most widely used. Fastest rate. ENIG standard (IPC-4552B). Balanced properties.`

**Right -- High-P (10-13% P):**
- Left accent `#2EC4B6`.
- Properties same as Poster #215 High-P column.
- Bottom: `Maximum corrosion. Amorphous. Oil/gas, chemical processing.`

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | SKIP PLATING | Contamination or poor activation | Improve cleaning; check activation |
| 2 | 6.33" | pH DRIFT | Reaction consumes H+ and releases H+ -- dynamic equilibrium | Check pH every 2-4 hr; adjust with NaOH or H2SO4 |
| 3 | 12.16" | WRONG P% | pH drifted out of 4.6-5.2 range | pH < 4.6 = high P; pH > 5.2 = low P; tighten control |
| 4 | 18.0" | BATH DECOMPOSITION | Low stabilizer, overheated, or under-loaded | Check stabilizer ppm; never idle at 85-91 C |

---

### ZONE 6 -- Footer

Standard footer.

**Disclaimer:** `Source: General industry knowledge; ASTM B733 Type IV; AMS 2404/2405; IPC-4552B. EN baths are proprietary -- consult your supplier TDS.`

**Title:** `Electroless Nickel (Mid Phos) -- Process Flow`

**Version:** `v1.0 -- 2026`

---

## Part 5 -- Grouping

Same structure as Poster #215.

---

## Part 6 -- Light Edition Remap

Standard table (same as all cluster posters).

---

## Part 7 -- Export Checklist

Six files: `EN Mid-P Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Mid-P is the workhorse -- the poster should convey "default choice, broadest application." The pH control message is the single most important technical insight: pH controls phosphorus content, and phosphorus controls everything. A Mid-P bath drifting from pH 4.8 to 4.3 crosses into High-P territory, changing all deposit properties. The +/-0.2 pH tolerance is tighter than most platers realize.

The ENIG callout in the post-treatment box is important: for PCB applications, the EN deposit goes directly to immersion gold without any heat treatment. Heat treatment would oxidize the EN surface and prevent gold deposition.

---

*Alaina -- Poster #223 -- Construction Workup v1.0 -- 2026-04-26*
