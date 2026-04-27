---
Project: Plating Posters Inc
Poster Number: 364
Title: "Acid Pickling (Stainless Steel) -- Process Flow"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4)"
Technical Source: Industry-standard acid pickling of stainless steel. Covers the complete 7-poster sequence for the CT-04 cluster. HNO3/HF mixed acid as primary chemistry with HNO3-only and citric acid alternatives. Values are typical ranges for austenitic, ferritic, martensitic, and duplex stainless steels.
Process Scope: Acid pickling of stainless steel -- complete process flow (cluster overview)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - ProcessFlow
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #364 -- Construction Workup
## Acid Pickling (Stainless Steel) -- Process Flow

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the cluster overview poster for CT-04: Acid Pickling (Stainless Steel). This cluster is fundamentally different from CT-03 (carbon steel pickling) in three ways: the acids are more dangerous (HNO3/HF vs. HCl/H2SO4), the safety stakes are dramatically higher (HF can kill), and the process terminates with passivation rather than direct plating. The hero is a U-flow diagram showing the 7-stage process from alloy verification through passivation. A compact HNO3/HF vs. HNO3-only vs. citric acid comparison answers the chemistry selection question. An alloy routing table covers the five major stainless families.

Design philosophy: same U-flow hero as CT-03 (Poster 357) to maintain structural consistency across pickling clusters, but with the HF hazard prominently flagged throughout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **U-flow diagram (Block B -- HERO):** Seven stages in a U-flow (top L-to-R, vertical, bottom R-to-L).
2. **Chemistry comparison table (Block D):** HNO3/HF vs. HNO3-only vs. citric acid.
3. **Alloy routing table (Block E):** Five stainless families with recommended pickle chemistry.
4. **Troubleshooting quick-hit strip (Block F):** 4 common failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.0" / 21.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")

ZONE 2 -- PROCESS FLOW DIAGRAM / HERO (2.9"--15.0" / ~12.1")
  Block B: Seven-stage U-flow diagram
  Block C: Stage legend strip

ZONE 3 -- CHEMISTRY COMPARISON TABLE (15.0"--21.5" / ~6.5")
  Block D: HNO3/HF vs. HNO3 vs. Citric

ZONE 4 -- ALLOY ROUTING (21.5"--28.5" / ~7.0")
  Block E: Five stainless families with chemistry and cautions

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0")
  Block F: 4 common failures

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Position: X: 0.5". Y: 0.5". W: 23.0"
- Font: Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4
- Text: `ACID PICKLING (STAINLESS STEEL)`

**BLOCK A -- Subheading**
- Y: 1.5". Barlow SemiBold, 34 pt, `#E05C5C` (Coral)
- Text: `Complete Process Flow -- HF Changes Everything`

**BLOCK A -- Tagline**
- Y: 2.2". Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `This is not carbon steel pickling with different acid. The chemistry is more aggressive, the hazards are more dangerous, and the process ends with passivation, not plating.`

---

### ZONE 2 -- Process Flow Diagram (HERO)

**Section label:** `THE STAINLESS STEEL PICKLE -- STAGE BY STAGE` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- Seven-Stage U-Flow Diagram (Y: 3.8" to 13.5")**

**Top Row (Y: 3.8" to 7.8") -- Stages 1-4, left to right:**

| Stage | Box | X | W | Top Accent | Type |
|---|---|---|---|---|---|
| 1. Verify Alloy | Box 1 | 0.5" | 5.0" | `#3A4055` (Slate) | Entry |
| 2. Alkaline Clean | Box 2 | 6.0" | 5.0" | `#2EC4B6` (Teal) | Prior Step |
| 3. Rinse | Box 3 | 11.5" | 4.5" | `#2EC4B6` (Teal) | Rinse |
| 4. Acid Pickle | Box 4 | 16.5" | 7.0" | `#E05C5C` (Coral) | Main Step |

**Vertical connector (Y: 8.0" to 9.5"):** Arrow from Box 4 down to bottom row.

**Bottom Row (Y: 9.5" to 13.5") -- Stages 5-7, right to left:**

| Stage | Box | X | W | Top Accent | Type |
|---|---|---|---|---|---|
| 5. Triple Rinse | Box 5 | 16.5" | 5.5" | `#2EC4B6` (Teal) | Rinse |
| 6. Passivation | Box 6 | 8.5" | 7.0" | `#27AE60` (Emerald) | Treatment |
| 7. Final Rinse + Inspect | Box 7 | 0.5" | 7.0" | `#27AE60` (Emerald) | Inspection |

Each flow box: Rounded rect H: 3.5", fill `#1E2435`, radius 8, top accent 4 pt.

**Inside each box:**

*Box 1 -- Verify Alloy:*
- Badge: `STAGE 1`, fill `#3A4055`
- Name: `Verify Alloy Type`
- Info: `Determines acid mixture` / `304, 316, 430, 410, 17-4 PH, duplex`
- Check: `WRONG ACID + WRONG ALLOY = DISASTER` Inter Medium 12 pt `#E05C5C`

*Box 2 -- Alkaline Clean:*
- Badge: `STAGE 2`, fill `#2EC4B6`
- Name: `Alkaline Clean`
- Info: `Remove oil, grease, contaminants` / `Before acid contact`
- Check: `See Posters #343-349`

*Box 3 -- Rinse:*
- Badge: `STAGE 3`, fill `#2EC4B6`
- Name: `Rinse`
- Info: `Ambient | 30-60 sec` / `Remove alkaline residue`

*Box 4 -- Acid Pickle:*
- Badge: `MAIN STEP`, fill `#E05C5C`
- Name: `Acid Pickle`
- Parameters: JetBrains Mono 13 pt:
```
HNO3: 10-25% v/v (70-175 g/L)
HF: 1-8% v/v (5-40 g/L)
Temp: 70-130 F (21-54 C)
Time: 5-60 min (scale dependent)
```
- Check: `HF IS LETHAL -- see Safety Poster #365` Inter Medium 12 pt `#E05C5C`

*Box 5 -- Triple Rinse:*
- Badge: `STAGE 5`, fill `#2EC4B6`
- Name: `Triple Rinse (Minimum)`
- Info: `Drag-out capture -> counterflow -> final` / `Fluoride removal critical`
- Check: `Test final rinse for residual fluoride` Inter Medium 12 pt `#E8A020`

*Box 6 -- Passivation:*
- Badge: `STAGE 6`, fill `#27AE60`
- Name: `Passivation`
- Parameters:
```
HNO3 20-50% or Citric 4-10%
70-160 F (21-71 C)
20-30 min
Per ASTM A967 / AMS 2700
```
- Check: `Restores protective chromium oxide film`

*Box 7 -- Final Rinse + Inspect:*
- Badge: `STAGE 7`, fill `#27AE60`
- Name: `Final Rinse & Inspection`
- Info: `DI rinse | Visual + copper sulfate test` / `Verify passivation per ASTM A967`

**BLOCK C -- Stage Legend Strip (Y: 13.8" to 14.5")**

Rounded rect, W: 23.0", H: 0.6", fill `#252B3D`.

| Swatch | Label |
|---|---|
| `#3A4055` | `Entry / Verification` |
| `#2EC4B6` | `Cleaning & Rinse` |
| `#E05C5C` | `Acid Pickle (HF Hazard)` |
| `#27AE60` | `Passivation & Inspection` |

---

### ZONE 3 -- Chemistry Comparison Table

**Section label:** `THREE PICKLE CHEMISTRIES -- CHOOSE BY SCALE AND RISK` -- Y: 15.2".

**BLOCK D -- Three-Column Comparison (Y: 15.8" to 21.3")**

Column widths (23.0" total):
- Property (4.0") | HNO3 + HF (6.5") | HNO3 Only (6.0") | Citric Acid (6.5")

Header row: fill `#3A4055`, H: 0.5".

| Property | HNO3 + HF | HNO3 Only | Citric Acid |
|---|---|---|---|
| Concentration | 10-25% HNO3 + 1-8% HF | 15-30% HNO3 | 4-10% citric by weight |
| Temperature | 70-130 F (21-54 C) | 70-140 F (21-60 C) | 70-160 F (21-71 C) |
| Scale Removal | Excellent -- heavy anneal and weld scale | Moderate -- light heat tint only | Light -- primarily for passivation |
| HF Hazard | YES -- LETHAL | None | None |
| NOx Fumes | YES -- toxic brown gas | YES -- toxic brown gas | Minimal |
| Environmental | HF waste requires special treatment | Standard acid waste | ENVIRONMENTALLY PREFERRED |
| ASTM A967 | Not a standard method (pickle, not passivation) | Method 1 (passivation) | Method 5 (passivation) |
| Best For | Heavy scale, weld scale, production shops | Light oxide, passivation, HF-avoidance | Passivation; increasing adoption |

Data: JetBrains Mono 12 pt. "YES -- LETHAL" in `#E05C5C` bold. "ENVIRONMENTALLY PREFERRED" in `#27AE60`.

---

### ZONE 4 -- Alloy Routing

**Section label:** `ALLOY ROUTING -- MATCH CHEMISTRY TO GRADE` -- Y: 21.7".

**BLOCK E -- Five-Alloy Comparison (Y: 22.3" to 28.3")**

Five callout boxes in a single row.

| Family | X | W | Accent | Grades | Pickle | Caution |
|---|---|---|---|---|---|---|
| Austenitic | 0.5" | 4.3" | `#2EC4B6` | 304, 316, 321, 347 | 15-20% HNO3 + 2-5% HF standard | Most common; standard parameters |
| Ferritic | 5.1" | 4.3" | `#E8A020` | 430, 409 | H2SO4/HF blend or HNO3/HF; may require heat | More sensitive to HF concentration |
| Martensitic | 9.7" | 4.3" | `#E05C5C` | 410, 420 | HNO3/HF at lower HF%; shorter time | Susceptible to hydrogen embrittlement |
| Duplex | 14.3" | 4.3" | `#27AE60` | 2205, 2507 | HNO3/HF standard; control time carefully | Resist over-pickling -- dual-phase microstructure |
| PH Grades | 18.9" | 4.6" | `#C8D0D8` | 17-4 PH, 15-5 PH | HNO3/HF at reduced concentration; shorter time | High strength -- HE risk from pickle; document time |

Each box: Rounded rect H: 5.5", fill `#1E2435`, left accent 0.06".
Family name: Barlow SemiBold 16 pt, accent color.
Grades: JetBrains Mono 13 pt `#F0EDE8`.
Pickle: Inter Regular 12 pt `#F0EDE8`.
Caution: Inter Medium 11 pt, `#E05C5C` or `#E8A020`.

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:** `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK F -- Four Problem Cards (Y: 29.4" to 32.3")**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | OVER-PICKLE | HF too high; time too long; temperature too high | Reduce HF; reduce time; check temperature; inspect for grain boundary attack |
| 2 | 6.33" | INCOMPLETE SCALE | Acid depleted; metal content too high; time too short | Check free acid; replace solution if metals >40 g/L; extend time |
| 3 | 12.16" | WELD ATTACK | Heat-affected zone metallurgy; acid imbalance | Pre-grind weld scale; adjust HNO3:HF ratio; reduce time on welds |
| 4 | 18.0" | TEA STAINING | Free iron contamination; handling with carbon steel tools | Re-pickle; re-passivate; eliminate carbon steel contact; use SS-only tooling |

Interior per card:
- Problem: Barlow SemiBold, 16 pt, `#E05C5C`
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer Band

Standard. Title: `Acid Pickling (Stainless Steel) -- Process Flow`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A380 (cleaning/descaling/passivation of stainless); ASTM A967 / AMS 2700 (passivation); general industry knowledge. HF is an extremely hazardous chemical -- dedicated safety training is MANDATORY before handling. Consult your process supplier for alloy-specific parameters.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Acid Pickling Stainless Steel Process Flow -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This overview poster sets the tone for the CT-04 cluster: stainless steel pickling is a more dangerous, more nuanced process than carbon steel pickling. The Coral accent dominates the acid pickle box in the flow diagram -- a deliberate visual signal that HF demands respect. The chemistry comparison table is the key reference for shops deciding whether they need HF or can use an alternative. The alloy routing section answers the question "does my grade need HF?" which is the first decision point for any fabricator. The passivation stage in the flow diagram signals that this cluster does not end at rinse -- it ends at a verified passive surface.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #364 -- Construction Workup v1.0*
*2026-04-26*
