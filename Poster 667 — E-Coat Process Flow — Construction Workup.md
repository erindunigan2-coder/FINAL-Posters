---
Project: Plating Posters Inc
Poster Number: 667
Title: "E-Coat (Electrophoretic Deposition) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 3"
Technical Source: Industry-standard e-coat process. Complete 9-stage sequence for automotive cathodic electrodeposition including zinc phosphate pretreatment, UF permeate rinse recovery, and bake cure. Covers cathodic vs. anodic, throwing power, and self-limiting deposition.
Process Scope: E-coat (electrophoretic deposition) -- complete process flow
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ECoat
  - ProcessFlow
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC03
---

# Poster #667 -- Construction Workup
## E-Coat (Electrophoretic Deposition) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cluster overview poster for E-Coat. This is the process that primes virtually every automobile made worldwide. The U-flow shows the complete 9-stage sequence from alkaline cleaning through bake cure. E-coat's superpower is throwing power -- the electric field drives coating into every recess, box section, and weld seam that spray painting cannot reach. The self-limiting deposition mechanism and UF permeate recovery system are the two concepts that make e-coat unique, and both get prominent space.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **9-stage U-flow diagram (Block B -- HERO):** Top row 5, bottom row 4 -- mirrors Poster 658 (Liquid Spray) structure.
2. **Cathodic vs. anodic comparison (Block D):** Why cathodic dominates (>95% of automotive).
3. **Parameter summary table (Block E):** Cathodic epoxy e-coat bath parameters.
4. **Troubleshooting strip (Block F):** 4 common problems.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.5" / ~12.6")
ZONE 3 -- CATHODIC vs. ANODIC + SELF-LIMITING (15.5"--22.0" / ~6.5")
ZONE 4 -- BATH PARAMETER TABLE (22.0"--27.5" / ~5.5")
ZONE 5 -- TROUBLESHOOTING STRIP (27.5"--32.5" / ~5.0")
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline:**
- 88 pt, `#F0EDE8`, Barlow Condensed ExtraBold. X: 0.5", Y: 0.5".
> E-COAT

**Subheading:**
- 36 pt, `#E8A020` (Amber). Y: 1.5".
> Electrophoretic Deposition -- Complete Process Flow

**Tagline:**
- 22 pt, `#F0EDE8` at 65%. Y: 2.2".
> The standard first-coat primer for virtually every automobile made worldwide. Electric fields drive coating where spray guns cannot reach.

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE COMPLETE E-COAT PROCESS -- STAGE BY STAGE` -- Centered, Y: 3.1".

**BLOCK B -- Nine-Stage U-Flow Diagram**

Y: 3.8" to 14.0". Same structure as Poster 658.

**Top Row (Y: 3.8" to 8.1") -- Stages 1-5, left to right:**

| Stage | Box X | Top Accent | Type |
|---|---|---|---|
| 1. Alkaline Clean | 0.5" | `#2EC4B6` (Teal) | Cleaning |
| 2. Rinse | 5.1" | `#2EC4B6` (Teal) | Rinse |
| 3. Surface Condition | 9.7" | `#E8A020` (Amber) | Pretreatment |
| 4. Zinc Phosphate | 14.3" | `#E8A020` (Amber) | Pretreatment |
| 5. Rinse / Seal | 18.9" | `#2EC4B6` (Teal) | Rinse |

Each box: W: 4.3", H: 4.3", fill `#1E2435`, radius 8.

*Box 1 -- Alkaline Clean:*
- Badge: `STAGE 1` on `#2EC4B6`
- Parameters: `2-stage: spray + immersion` / `pH 10--12, 2--5%` / `120--150 F (49--66 C)`
- Purpose: `Remove stamping oils, metal fines, weld flux`
- Check: `Low-foam cleaner; no silicate residues`

*Box 2 -- Rinse:*
- Badge: `STAGE 2` on `#2EC4B6`
- Parameters: `2 spray rinse stages, counterflow` / `Conductivity monitored`
- Purpose: `Remove cleaner residuals`
- Check: `City water acceptable`

*Box 3 -- Surface Condition:*
- Badge: `STAGE 3` on `#E8A020`
- Parameters: `Colloidal TiPO4 (Fixodine type)` / `Ambient--100 F, 30--60 sec` / `0.5--2.0 g/L`
- Purpose: `Provide nucleation sites for fine zinc phosphate crystals`
- Check: `Refines crystal size for better adhesion`

*Box 4 -- Zinc Phosphate:*
- Badge: `STAGE 4` on `#E8A020`
- Parameters: `Immersion, 95--115 F (35--46 C)` / `120--180 sec` / `Total acid 18--25 points`
- Purpose: `Crystalline phosphate layer for adhesion + corrosion resistance`
- Check: `Coating weight 150--400 mg/ft2`

*Box 5 -- Rinse / Seal:*
- Badge: `STAGE 5` on `#2EC4B6`
- Parameters: `2 immersion rinses + seal rinse` / `Non-chrome seal (Zr-based)` / `DI final rinse < 20 uS/cm`
- Purpose: `Remove phosphate residuals; seal crystal porosity`
- Check: `Body enters e-coat tank WET (no dry-off oven)`

**Vertical connector and bottom row:**

**Bottom Row (Y: 9.5" to 13.8") -- Stages 6-9, right to left:**

| Stage | Box X | Top Accent | Type |
|---|---|---|---|
| 6. E-Coat Tank | 18.9" | `#27AE60` (Emerald) | Application |
| 7. UF Permeate Rinse | 14.3" | `#2EC4B6` (Teal) | Recovery |
| 8. Bake Oven | 9.7" | `#E8A020` (Amber) | Cure |
| 9. Inspect | 0.5" | `#3A4055` (Slate) | QC |

*Box 6 -- E-Coat Tank:*
- Badge: `STAGE 6` on `#27AE60`
- Parameters: `200--400 V DC, 120--180 sec` / `Solids 18--22%, pH 5.8--6.2` / `85--95 F (29--35 C)`
- Purpose: `Cathodic electrodeposition of epoxy-amine primer`
- Check: `Self-limiting: film stops building when insulating`

*Box 7 -- UF Permeate Rinse:*
- Badge: `STAGE 7` on `#2EC4B6`
- Parameters: `2--3 stages, counterflow` / `UF permeate from e-coat tank` / `Recovers > 95% of dragout paint`
- Purpose: `Rinse dragout; return paint to tank`
- Check: `Closed-loop: > 99% paint utilization`

*Box 8 -- Bake Oven:*
- Badge: `STAGE 8` on `#E8A020`
- Parameters: `350--375 F (177--191 C) oven air` / `Metal temp 340--360 F` / `20--30 min at metal temp`
- Purpose: `Cross-link blocked isocyanate + epoxy resin`
- Check: `MEK rub: 100+ double rubs = fully cured`

*Box 9 -- Inspect:*
- Badge: `STAGE 9` on `#3A4055`
- Parameters: `DFT: 0.6--1.2 mils (D7091)` / `Adhesion: D3359, 5B required` / `Salt spray: 500--1,000+ hr B117`
- Purpose: `Verify primer quality before topcoat line`
- Check: `Throwing power: DFT ratio interior vs. exterior`

**Stage Legend Strip (Y: 14.3" to 15.3"):**
Same format as Poster 658.

---

### ZONE 3 -- Cathodic vs. Anodic + Self-Limiting

**Two-column layout (Y: 15.7" to 21.8"):**

**Left -- Cathodic vs. Anodic (X: 0.5", W: 11.0"):**

Title: `CATHODIC vs. ANODIC -- WHY CATHODIC WINS` -- Barlow SemiBold, 18 pt, `#F0EDE8`

| Feature | Cathodic (>95% of auto) | Anodic |
|---|---|---|
| Workpiece polarity | Cathode (negative) | Anode (positive) |
| Metal dissolution | None -- metal protected | Metal dissolves during deposition |
| Corrosion protection | Superior | Lower |
| Throwing power | Excellent (8--12" into box sections) | Moderate |
| Chemistry | Epoxy-amine resin, cationic | Acrylic, anionic |
| Voltage | 200--400 V DC | 50--250 V DC |
| Typical DFT | 0.6--1.2 mils | 0.4--0.8 mils |
| Use | Automotive, heavy equipment | Small appliances, general industrial |

Bottom note: `Cathodic e-coat dominates because the workpiece does not dissolve during deposition -- the metal is protected by being the cathode.` -- Inter Medium 12 pt `#27AE60`

**Right -- Self-Limiting Mechanism (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `THE SELF-LIMITING MECHANISM` -- Barlow SemiBold, 20 pt, `#27AE60`

Numbered steps (Inter Medium 14 pt):
1. `Charged resin micelles migrate to cathode surface`
2. `Water electrolysis at cathode: 2H2O + 2e- -> H2 + 2OH-`
3. `Local pH rise neutralizes cationic resin -- it deposits as insulating film`
4. `Deposited film blocks current flow to that area`
5. `Current redirects to uncoated areas -- coating builds there instead`
6. `Result: UNIFORM THICKNESS everywhere the electric field reaches`

Key insight: `This is why e-coat coats the inside of a car door -- the electric field penetrates where spray guns cannot. The self-limiting mechanism ensures uniform thickness on complex geometries.`

---

### ZONE 4 -- Bath Parameter Table

**Section label:** `E-COAT BATH PARAMETERS -- DAILY MONITORING` -- Y: 22.2".

**BLOCK E -- Parameter Table (Y: 22.8" to 27.3")**

| Parameter | Cathodic Epoxy | Control Method | Frequency |
|---|---|---|---|
| Solids content | 18--22% (by weight) | Gravimetric | Daily |
| pH | 5.8--6.2 | pH meter | Daily |
| Conductivity | 1,000--1,800 uS/cm | Conductivity meter | Daily |
| Temperature | 85--95 F (29--35 C) | Thermometer / PLC | Continuous |
| P/B ratio | 0.15--0.25 | Ash test or centrifuge | Daily |
| MEQ (acid equiv) | 30--45 meq/100g solids | Titration | Weekly |
| Solvent content | Per supplier spec | GC or distillation | Weekly |
| Rupture voltage | > 250 V (indicates film quality) | Rupture voltage tester | Weekly |
| UF permeate flow | 5--20 gal/min per 100 ft2 membrane | Flow meter | Continuous |

Header row: fill `#3A4055`, Barlow SemiBold 14 pt `#F0EDE8`.
Data: JetBrains Mono 11 pt. Alternating rows: `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Troubleshooting Strip

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON E-COAT PROBLEMS` -- Y: 27.7".

**BLOCK F -- Four Cards (Y: 29.3" to 32.3")**

| Card | Problem | Cause | Fix |
|---|---|---|---|
| 1 | LOW THROWING POWER | Low voltage, high conductivity, or depleted resin | Increase voltage; check bath solids and MEQ |
| 2 | CRATERS / PINHOLES | Contamination in bath or poor pretreatment | Check cleaner oil loading; verify phosphate coating weight |
| 3 | UNDERCURE (SOFT FILM) | Oven profile insufficient; metal temp too low | Thermocouple profile the oven; verify PMT at 340--360 F |
| 4 | UF MEMBRANE FOULING | Permeate flow declining; pressure differential rising | Flush membranes per schedule; replace if flow < 50% of rated |

Each card: Rounded rect W: 5.5", H: 1.4", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `E-Coat (Electrophoretic Deposition) -- Process Flow`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge. E-coat bath chemistry and process parameters are supplier-specific. Consult your e-coat paint supplier for formulation-specific guidance.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `E-Coat Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

E-coat is the most chemically complex process in the painting clusters -- it sits at the intersection of electrochemistry, coating science, and membrane technology. The self-limiting mechanism callout is the conceptual anchor: it explains in six steps why e-coat can uniformly coat a car body with all its box sections and weld seams. The UF permeate recovery system in Box 7 is the environmental story: >99% paint utilization and minimal wastewater. The cathodic vs. anodic table settles the question definitively -- cathodic wins on every metric that matters for corrosion protection.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #667 -- Construction Workup v1.0*
*2026-04-26*
