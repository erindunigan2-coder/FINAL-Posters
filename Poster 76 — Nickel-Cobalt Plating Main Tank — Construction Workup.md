---
Project: Plating Posters Inc
Poster Number: 76
Title: "Nickel-Cobalt Plating -- Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Nickel-cobalt alloy electroplating main tank. Sulfamate-based NiCo bath with cobalt sulfate addition. Deposits 15-35% cobalt by weight. Anomalous co-deposition -- cobalt deposits preferentially despite lower concentration. Hardness 400-500 HV as-plated, 600-700 HV heat-treated. Applications: aerospace turbine components, high-wear tooling, molds. Stage 5 of 8.
Process Scope: Nickel-cobalt alloy plating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #76 -- Construction Workup
## Nickel-Cobalt Plating -- Main Tank

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the NiCo process -- the main plating tank where the nickel-cobalt alloy is electrodeposited. This poster is the most content-dense in the cluster. It covers bath composition (sulfamate-based), operating parameters, anode configuration, the cobalt co-deposition mechanism, alloy control, and a defect diagnosis grid.

The defining characteristic of NiCo plating is anomalous co-deposition: cobalt deposits at a higher percentage than its bath concentration would predict. This means small changes in bath chemistry, temperature, or current density can swing the alloy composition significantly. Controlling Co% is the central challenge.

Hero visual: a plating tank cross-section showing Ni anodes, cathode workpiece, current flow, and Co2+ / Ni2+ migration with labeled codeposition mechanism.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Plating tank cross-section hero (Block B):** Large tank with nickel S-round anodes in Ti baskets, cathode workpiece, current flow lines, and dual-ion migration arrows (Ni2+ and Co2+). Rectangles, lines, arrows, text labels.
2. **Bath composition panel (Block D):** Four-component breakdown: nickel sulfamate, cobalt sulfate, boric acid, nickel chloride.
3. **Alloy control gauge (Block E):** Visual showing how CD and temperature affect Co% in the deposit.
4. **Defect diagnosis grid (Block F):** 6 common defects in 3x2 grid.
5. **Hull cell strip or XRF verification callout (Block G):** Analytical verification methods for Co%.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH COMPOSITION + ALLOY CONTROL (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- ANALYTICAL VERIFICATION + SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NICKEL-COBALT PLATING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Sulfamate NiCo -- Main Tank -- Stage 5 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Harder than pure nickel. Tunable alloy composition. But cobalt does not behave -- anomalous codeposition means small bath changes swing your alloy. Control is everything.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.

Below: `Before: Activated (or Wood's strike) surface  -->  After: Ni-Co alloy deposit (15--35% Co) ready for post-treatment`

---

### ZONE 3 -- Plating Tank Hero

**Section label:** `THE NICKEL-COBALT PLATING TANK` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (plating solution -- greenish tint implied by label)
- Border: 3 pt `#C8D0D8`

**Anodes (left and right sides):**
- Left anodes: 2 vertical rects, X: 2.5", Y: 6.0", W: 1.0", H: 5.5", fill `#C8D0D8`, border 1 pt `#3A4055`
- Right anodes: same, X: 20.5"
- Label beneath each: `Ni S-ROUNDS IN Ti BASKETS` JetBrains Mono 12 pt `#C8D0D8`
- Sub-label: `Soluble nickel anodes only -- NO cobalt anodes` Inter Regular 11 pt `#E8A020`

**Cathode / Workpiece (center):**
- Vertical rect, X: 11.0", Y: 6.0", W: 2.0", H: 5.5", fill `#27AE60` at 30%, border 2 pt `#27AE60`
- Label above: `CATHODE (WORKPIECE)` Barlow SemiBold 14 pt `#27AE60`
- Small labels on cathode surface: `Ni + Co co-depositing` Inter Regular 11 pt `#27AE60`

**Dual-ion migration arrows:**
- Set of arrows from anodes to cathode (4 lines):
  - Ni2+ arrows: stroke 2 pt `#2EC4B6`, dashed. Label: `Ni2+ (from anode dissolution)` Inter Regular 12 pt `#2EC4B6`
  - Co2+ arrows: stroke 2 pt `#E8A020`, dashed. Label: `Co2+ (from CoSO4 addition)` Inter Regular 12 pt `#E8A020`

**Current flow lines:**
- Curved arrows (dashed) from anode to cathode, stroke 2 pt `#3A4055`
- Label: `Current flow` Inter Regular 11 pt `#3A4055`

**Rectifier symbol (above tank):**
- Small rectangle, X: 10.0", Y: 5.0", W: 4.0", H: 0.8", fill `#1E2435`, border 1 pt `#E8A020`
- Text: `DC RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- `(+)` on anode wires; `(-)` on cathode wire

**Bath parameter labels (right side, X: 15.0", Y: 7.0"):**
- `Ni sulfamate: 300--400 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `CoSO4 * 7H2O: 10--60 g/L` JetBrains Mono 14 pt `#E8A020`
- `Boric acid: 30--45 g/L` JetBrains Mono 14 pt `#F0EDE8`
- `NiCl2: 5--15 g/L` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `pH: 3.5--4.5` JetBrains Mono 14 pt `#27AE60`
- `Temp: 120--140 F (49--60 C)` JetBrains Mono 14 pt `#F0EDE8`
- `CD: 20--60 ASF (rack)` JetBrains Mono 14 pt `#E8A020`

**Left side labels (X: 4.0", Y: 7.0"):**
- `Cathode efficiency: 90--98%` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Deposit Co: 15--35% by wt` JetBrains Mono 14 pt `#E8A020`
- `Hardness: 400--500 HV (as-plated)` JetBrains Mono 13 pt `#F0EDE8`
- `A:C ratio: 1:1 to 2:1` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Anomalous codeposition callout (bottom of tank, Y: 12.5"):**
- Rounded rect, X: 3.0", W: 18.0", H: 1.2", fill `#E8A020` at 10%, border 1 pt `#E8A020`
- Title: `ANOMALOUS CODEPOSITION` Barlow SemiBold 14 pt `#E8A020`
- Text: `Cobalt deposits at a HIGHER percentage than its bath concentration predicts. A bath with 10% Co (by metal weight) can produce a deposit with 20--30% Co. Higher CD and lower temperature both increase Co%.` Inter Regular 12 pt `#F0EDE8`

---

### ZONE 4 -- Bath Composition + Alloy Control

**Section label:** `BATH CHEMISTRY + ALLOY CONTROL` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Four-Component Breakdown (Y: 15.3" to 18.0")**

Four callout boxes in a row:

| Component | X | W | Accent | Title |
|---|---|---|---|---|
| Nickel Sulfamate | 0.5" | 5.5" | `#2EC4B6` | NICKEL SULFAMATE |
| Cobalt Sulfate | 6.25" | 5.5" | `#E8A020` | COBALT SULFATE |
| Boric Acid | 12.0" | 5.5" | `#C8D0D8` | BORIC ACID |
| Nickel Chloride | 17.75" | 5.75" | `#3A4055` | NICKEL CHLORIDE |

Each box: Rounded rect H: 2.5", fill `#1E2435`, left accent 0.06".

*Nickel Sulfamate:*
- `300--400 g/L (as salt)` JetBrains Mono 14 pt `#2EC4B6`
- `Optimal: 350 g/L`
- `Primary Ni source; low stress`

*Cobalt Sulfate:*
- `10--60 g/L (CoSO4 * 7H2O)` JetBrains Mono 14 pt `#E8A020`
- `Optimal: 15--40 g/L`
- `Sole Co source; added chemically`

*Boric Acid:*
- `30--45 g/L` JetBrains Mono 14 pt `#C8D0D8`
- `Optimal: 37--40 g/L`
- `pH buffer at cathode film`

*Nickel Chloride:*
- `0--15 g/L` JetBrains Mono 13 pt `#F0EDE8`
- `Optimal: 5--10 g/L`
- `Promotes anode dissolution`

**BLOCK E -- Alloy Control Gauge (Y: 18.3" to 20.3")**

- Rounded rect, full width, H: 1.8", fill `#1E2435`
- Title: `CONTROLLING COBALT % IN THE DEPOSIT` Barlow Condensed ExtraBold 18 pt `#F0EDE8`

**Two-factor control display:**

Left half -- Current Density Effect:
- Horizontal bar, W: 10.0", H: 0.5"
- Left end: `Low CD (20 ASF)` -- `Lower Co%` JetBrains Mono 12 pt `#2EC4B6`
- Right end: `High CD (60 ASF)` -- `Higher Co%` JetBrains Mono 12 pt `#E8A020`
- Gradient fill from `#2EC4B6` at 30% to `#E8A020` at 30%
- Label: `Higher current density = more cobalt in deposit` Inter Medium 12 pt `#F0EDE8`

Right half -- Temperature Effect:
- Horizontal bar, W: 10.0", H: 0.5"
- Left end: `Low T (100 F)` -- `Higher Co%` JetBrains Mono 12 pt `#E8A020`
- Right end: `High T (150 F)` -- `Lower Co%` JetBrains Mono 12 pt `#2EC4B6`
- Gradient fill from `#E8A020` at 30% to `#2EC4B6` at 30%
- Label: `Higher temperature = less cobalt in deposit` Inter Medium 12 pt `#F0EDE8`

**Below bars:**
- `Typical target: 18--25% Co by weight. Verify by XRF or wet chemistry (EDTA total metals minus DMG nickel = cobalt).` Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK F -- 3x2 Grid (Y: 21.3" to 26.3")**

Same construction as Poster #36 defect grid.

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | CO% OUT OF SPEC | `#E8A020` | Bath ratio drift, temp shift, CD mismatch | Analyze metals; adjust CoSO4; verify CD + temp |
| R1C2 | CRACKING (HEAT TREAT) | `#E05C5C` | Too rapid ramp, excess Co, H2 damage | Slow ramp to 300 C; verify Co% < 30%; pre-bake for H2 |
| R1C3 | ROUGH / NODULAR | `#E8A020` | Particulate, anode sludge, torn bags | Inspect/replace anode bags; continuous filtration |
| R2C1 | LOW HARDNESS | `#2EC4B6` | Cobalt too low; organic contamination | Add CoSO4; carbon treat; analyze by XRF |
| R2C2 | PITTING | `#E05C5C` | Wetting agent depleted, H2 gas, low pH | Add wetting agent; check pH; increase agitation |
| R2C3 | POOR THROWING POWER | `#2EC4B6` | Low NiCl2, low boric acid, high CD | Add NiCl2; replenish H3BO3; reduce CD |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- Analytical Verification + Safety

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Analytical Verification (X: 0.5", W: 11.0"):**

Section label: `VERIFYING YOUR DEPOSIT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`.

| Method | What It Tells You | Notes |
|---|---|---|
| XRF (X-ray fluorescence) | Co% and Ni% in deposit | Fast, non-destructive, most common in production |
| Wet chemistry (EDTA + DMG) | Total metals; Ni by DMG; Co by difference | Lab method -- slower but more precise |
| Hull cell | Visual check of deposit quality across CD range | Run at bath conditions (120--140 F) |
| Vickers hardness | Deposit hardness (HV) | Cross-section required; 400--500 HV as-plated target |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Method names: Inter Medium, 13 pt.

**Right -- Safety (X: 12.0", W: 11.5"):**

Section label: `SAFETY` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`.

- Title: `COBALT COMPOUNDS -- HEALTH HAZARD` Barlow SemiBold 16 pt `#E05C5C`
- `IARC Group 2B: Possibly carcinogenic to humans` JetBrains Mono 13 pt `#E05C5C`
- `Respiratory protection required for mist/dust exposure`
- `Same nickel dermatitis concerns as Watts/sulfamate`
- `Ventilation: Local exhaust at tank level mandatory`
- `PPE: Gloves, splash apron, eye protection, respiratory as needed`
- `Monitor airborne cobalt: ACGIH TLV 0.02 mg/m3 TWA | OSHA PEL 0.1 mg/m3 TWA` JetBrains Mono 12 pt `#E05C5C`

---

### ZONE 7 -- Footer Band

Standard. Title: `Nickel-Cobalt Plating -- Main Tank`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Bath parameters shown are typical industry values for sulfamate-based nickel-cobalt alloy plating. Specific formulations, alloy targets, and process limits are frequently OEM-specific (Pratt & Whitney, GE, Honeywell). Consult your process supplier and governing specification (e.g., AMS 2424) for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5; Modern Electroplating.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `NiCo Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EP-06 cluster -- comparable to Poster #36 (Zinc Alkaline Main Tank) and Poster #23 (Watts Nickel) in information density. The anomalous codeposition callout is the single most important concept on the poster -- it explains why controlling Co% is harder than controlling a single-metal bath. The alloy control gauge (CD and temperature effects on Co%) is the key decision-making visual. The safety section is mandatory -- cobalt's IARC 2B classification is not well known on shop floors.

Watson's brief provided the sulfamate bath composition, anode spec (no cobalt anodes), failure modes, safety notes, and key specifications. I expanded the alloy control mechanism and analytical verification from standard electroplating practice.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #76 -- Construction Workup v1.0*
*2026-04-26*
