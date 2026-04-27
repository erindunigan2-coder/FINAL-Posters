---
Project: Plating Posters Inc
Poster Number: 268
Title: "Electroless Cobalt -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 7: Electroless Cobalt, Poster 6)"
Technical Source: Electroless cobalt plating bath -- Co-P (hypophosphite) and Co-W-P (ternary) formulations. Operating parameters, deposit properties, and bath stability management. Watson domain expertise; deposition rates from published literature.
Process Scope: Main electroless cobalt plating tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessCobalt
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEL07
---

# Poster #268 -- Construction Workup
## Electroless Cobalt -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. The heart of the process -- the main plating tank where cobalt alloy is autocatalytically deposited. This poster is the most content-dense in the cluster. It covers both Co-P (binary) and Co-W-P (ternary) bath formulations, operating parameters, deposit properties including magnetic characteristics, and the critical bath stability challenge. Cobalt baths are notably less stable than EN baths -- shorter bath life and higher decomposition risk.

Hero visual: plating tank cross-section showing autocatalytic deposition (no anodes, no rectifier), chemical reduction arrows on the substrate surface, and bath chemistry labels.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank cross-section hero (Block B):** Electroless tank -- no anodes, no rectifier. Parts immersed in heated solution. Chemical reduction arrows at substrate surface. Heater, agitation, filtration shown.
2. **Dual bath composition panels (Block D):** Side-by-side Co-P and Co-W-P formulations.
3. **Deposit properties comparison (Block E):** Property table comparing low-P, high-P, and Co-W-P deposits.
4. **Bath stability management (Block F):** Decomposition prevention rules and MTO tracking.
5. **Defect grid (Block G):** 6 common problems.

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
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH COMPOSITION -- DUAL FORMULATION (14.5"--20.5" / ~6.0")
ZONE 5 -- DEPOSIT PROPERTIES + MAGNETIC DATA (20.5"--26.5" / ~6.0")
ZONE 6 -- BATH STABILITY + DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROLESS COBALT` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Autocatalytic deposition -- no rectifier, no anodes. Chemical reduction deposits ferromagnetic Co-P or Co-W-P alloy with tunable properties.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated substrate  -->  After: Cobalt alloy deposit (uniform thickness on all surfaces)`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE ELECTROLESS COBALT BATH` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**NO anodes, NO rectifier** (key visual difference from electroplating):
- Prominent label at top center: `NO RECTIFIER -- AUTOCATALYTIC` Barlow Condensed ExtraBold 18 pt `#27AE60`

**Parts on rack (center):**
- 3 vertical rects, X: 9.5"--14.5", Y: 6.5", W: 0.5" each, H: 4.5"
- Fill: `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `SUBSTRATE (CATHODE SURFACE)` Barlow SemiBold 14 pt `#27AE60`

**Chemical reduction arrows (at substrate surface):**
- Small curved arrows pointing toward substrate surfaces from surrounding solution
- Label: `Co2+ + H2PO2- + H2O → Co0 + H2PO3- + 2H+` JetBrains Mono 13 pt `#27AE60`
- Subtitle: `Autocatalytic: freshly deposited Co catalyzes further reaction` Inter Regular 12 pt `#F0EDE8` at 70%

**Heater element (right side):**
- Zigzag line, X: 19.5", Y: 7.0" to 11.0", stroke 2 pt `#E05C5C`
- Label: `Heater (158--194 F)` Inter Regular 11 pt `#E05C5C`

**Filter loop (left side):**
- Rectangle with "FILTER" label, X: 2.0", Y: 9.0"
- Arrows showing recirculation: bath -> filter -> back to bath
- Label: `Continuous filtration 1--5 um` Inter Regular 11 pt `#2EC4B6`

**Bath parameter labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `Co2+: 5--15 g/L` JetBrains Mono 14 pt `#27AE60`
- `NaH2PO2: 15--30 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Citrate: 30--60 g/L` JetBrains Mono 14 pt `#F0EDE8`
- `pH: 8.0--10.0` JetBrains Mono 14 pt `#E8A020`
- `Temp: 158--194 F (70--90 C)` JetBrains Mono 14 pt `#E8A020`

Left side (X: 3.0", Y: 7.0"):
- `Rate: 3--8 um/hr` JetBrains Mono 14 pt `#F0EDE8`
- `Bath life: 2--4 MTO` JetBrains Mono 13 pt `#E8A020`
- `Stabilizer: 0.5--5 ppm` JetBrains Mono 13 pt `#E05C5C`

**Bottom callout (Y: 13.5"):**
- `Cobalt baths are less stable than EN baths. Never leave at temperature without parts loaded. Bath life is short -- plan accordingly.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Bath Composition -- Dual Formulation

**Section label:** `BATH CHEMISTRY -- TWO FORMULATIONS` -- Y: 14.7".

**BLOCK D -- Side-by-Side (Y: 15.3" to 20.3")**

**Left -- Co-P (Hypophosphite-Based):**
- Rounded rect, X: 0.5", Y: 15.3", W: 11.0", H: 4.8", fill `#1E2435`
- Left accent: `#27AE60`, 0.06"
- Title: `CO-P ALLOY BATH` Barlow SemiBold 20 pt `#27AE60`

| Component | Concentration | Role |
|---|---|---|
| Cobalt sulfate (CoSO4 . 7H2O) | 5--15 g/L Co2+ | Metal source |
| Sodium hypophosphite | 15--30 g/L | Reducing agent |
| Sodium citrate | 30--60 g/L | Primary complexant |
| Ammonium sulfate | 20--40 g/L | Buffer + complexant |
| Boric acid | 10--20 g/L | Buffer |
| Stabilizer (thiourea or MBT) | 0.5--5 ppm | Prevents decomposition |

JetBrains Mono 12 pt for concentrations. Inter Regular 12 pt for roles.

**Right -- Co-W-P (Ternary Alloy):**
- Rounded rect, X: 12.0", Y: 15.3", W: 11.5", H: 4.8", fill `#1E2435`
- Left accent: `#E8A020`, 0.06"
- Title: `CO-W-P TERNARY BATH` Barlow SemiBold 20 pt `#E8A020`

| Component | Concentration | Role |
|---|---|---|
| Cobalt sulfate | 10--20 g/L Co2+ | Metal source |
| Sodium tungstate (Na2WO4) | 10--40 g/L | Tungsten source |
| Sodium hypophosphite | 15--25 g/L | Reducing agent |
| Sodium citrate | 40--80 g/L | Complexant (critical for W) |
| Boric acid | 15--25 g/L | Buffer |

Note below: `Citrate concentration controls tungsten incorporation -- higher citrate = more W in deposit` Inter Medium 12 pt `#E8A020`

---

### ZONE 5 -- Deposit Properties + Magnetic Data

**Section label:** `DEPOSIT PROPERTIES -- THE MAGNETIC STORY` -- Y: 20.7".

**BLOCK E -- Property Table (Y: 21.3" to 26.3")**

| Property | Co-P (low P, 2--5%) | Co-P (high P, 8--12%) | Co-W-P |
|---|---|---|---|
| Hardness (as-plated) | 400--550 HV | 500--700 HV | 500--800 HV |
| Structure | Crystalline | Amorphous | Amorphous |
| Magnetic coercivity | >500 Oe (HARD) | <100 Oe (SOFT) | Medium |
| Saturation magnetization | HIGH | LOW | Medium |
| Corrosion resistance | Moderate | Good | Very good |
| Thermal stability | Moderate | Moderate | EXCELLENT |
| Primary application | Magnetic recording media | Soft magnetic layers | Diffusion barrier |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`.
Magnetic data highlighted: coercivity values in `#E8A020`.

Below table:
- `KEY INSIGHT: Phosphorus content controls magnetic behavior. Low P = hard magnetic (high coercivity). High P = soft magnetic (low coercivity). This is the fundamental tuning lever.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Bath Stability + Defects

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Bath Stability Rules (X: 0.5", W: 11.0"):**

Section label: `STABILITY MANAGEMENT` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Rule | Detail |
|---|---|
| Never idle at temp without load | Under-loaded bath at temperature = decomposition risk |
| Cool to <40 C when not in use | Reduces reaction kinetics to negligible |
| Filter continuously (1--5 um) | Remove metallic particles that serve as nucleation sites |
| Monitor stabilizer | Stabilizer consumed during plating; replenish per protocol |
| Loading ratio | 0.2--0.5 dm2/L optimal; <0.1 dm2/L is danger zone |
| MTO tracking | 2--4 MTO typical; discard when orthophosphite limits reached |

Rules: Inter Medium 13 pt `#F0EDE8`. "Never" and "danger" in `#E05C5C`.

**Right -- Common Defects (X: 12.0", W: 11.5"):**

3x2 mini-grid:

| Defect | Cause | Fix |
|---|---|---|
| SKIP PLATING | Poor activation or stabilizer poisoning | Verify activation; check stabilizer |
| BATH CRASH | Under-loaded at temp; Fe/Cu contamination | Never idle hot; filter; inspect heater |
| PITTING | H2 bubbles adhering; poor agitation | Increase agitation; add wetting agent |
| ROUGHNESS | Particulate; high MTO; metallic contamination | Filter; check MTO; dummy plate |
| POOR ADHESION | Inadequate activation; transfer delay | Review activation; minimize transfer time |
| LOW RATE | Low temperature; depleted reducing agent | Check temp; replenish hypophosphite |

Each cell: small card, fill `#1E2435`, left accent `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Electroless Cobalt -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer note: `Source: General industry knowledge; electroless cobalt bath parameters from published literature and domain expertise. Specific formulations vary by supplier. No governing ASTM standard for electroless cobalt.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Electroless Cobalt Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EL-07 cluster. The "no rectifier -- autocatalytic" callout must be visually prominent. The dual bath formulation (Co-P vs. Co-W-P) is the unique feature of this poster. The magnetic properties section is what makes electroless cobalt interesting -- phosphorus content controls coercivity, which is the entire reason this process exists. Bath stability is the practical challenge -- cobalt baths are less forgiving than EN. Watson notes that bath life is only 2-4 MTO, making stability management paramount.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #268 -- Construction Workup v1.0*
*2026-04-26*
