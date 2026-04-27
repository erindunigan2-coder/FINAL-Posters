---
Project: Plating Posters Inc
Poster Number: 228
Title: "Electroless Nickel (Mid Phos) -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 2: EN Mid-P, Poster 6)"
Process Scope: Electroless nickel mid phosphorus main plating tank (Stage 5 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - MidPhosphorus
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEN-MP
---

# Poster #228 -- Construction Workup
## Electroless Nickel (Mid Phos) -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 7. The heart of the Mid-P process -- the industry workhorse. More EN Mid-P is plated globally than all other EN classes combined. It operates at the highest temperature (85-91 C) and delivers the fastest deposition rate (18-25 um/hr) of any EN-P class. The acid pH (4.6-5.2) uses organic acid complexants (lactic, malic, succinic) instead of the ammonium compounds found in alkaline Low-P baths.

The critical insight for this poster: pH controls phosphorus content, and phosphorus controls everything. A bath drifting from pH 4.8 to pH 4.3 crosses into High-P territory, changing all deposit properties. The +/-0.2 pH tolerance is tighter than most platers realize.

Hero visual: an EN tank cross-section showing parts immersed with uniform deposit buildup, pH control as the dominant visual element, and a pH-vs-P% relationship callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **EN tank cross-section hero (Block B):** Tank with parts showing uniform deposit. NO anodes, NO rectifier. H2 evolution on part surfaces. Filter system. pH controller prominent.
2. **Bath composition panel (Block D):** Multi-component breakdown with organic acid complexants.
3. **MTO tracking gauge (Block E):** Visual representation of bath life in metal turnovers.
4. **pH vs. P% relationship chart (Block F):** The master lever -- how pH determines phosphorus content.
5. **NOTE: No Hull cell.** QC section covers plating rate, phosphorus analysis, thickness.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- EN TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- BATH COMPOSITION + MTO TRACKING (14.5"--20.5" / ~6.0")
ZONE 5 -- pH vs P% + DEFECT DIAGNOSIS (20.5"--26.5" / ~6.0")
ZONE 6 -- QC METHODS + BATH STABILITY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROLESS NICKEL` -- Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Mid Phosphorus (5-9% P) -- Main Tank -- Stage 5 of 7` -- Barlow SemiBold, 30 pt, `#27AE60` (Emerald). X: 0.5", Y: 1.4".

**Tagline:** `The industry workhorse. Fastest rate. Highest temperature. pH controls phosphorus -- and phosphorus controls everything.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean, activated surface (catalytic)  -->  After: Uniform Ni-P alloy deposit (5-9% P, 500-600 HV)`

---

### ZONE 3 -- EN Tank Hero

**Section label:** `THE ELECTROLESS NICKEL MID-P BATH` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**NO ANODES -- key visual:**
- Dashed outline rectangles (ghosted), X: 2.5" and X: 20.5", Y: 6.0", W: 1.0", H: 5.5"
- Fill: none. Border: 1 pt `#3A4055` dashed
- Label: `NO ANODES` Barlow SemiBold 14 pt `#E8A020`
- Sub-label: `No external current source` Inter Regular 11 pt `#F0EDE8` at 50%

**NO RECTIFIER -- label at top:**
- Dashed outline rectangle: X: 10.0", Y: 5.0", W: 4.0", H: 0.8"
- Border: 1 pt `#3A4055` dashed
- Text: `NO RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- Sub: `Autocatalytic -- reaction is self-sustaining` Inter Regular 11 pt `#F0EDE8` at 50%

**Parts / Workpieces (center):**
- Three stylized parts of different shapes hanging from rack bar
- Each part has a thin green border showing uniform deposit: 2 pt `#27AE60`
- Label: `UNIFORM DEPOSIT ON ALL SURFACES` Barlow SemiBold 14 pt `#27AE60`
- Sub: `+/- 1-2 um thickness variation` JetBrains Mono 12 pt `#27AE60`

**H2 bubbles on surfaces:**
- Small circles (0.1" dia), fill `#F0EDE8` at 20%, scattered on part surfaces
- Label: `H2 evolution (byproduct)` Inter Regular 11 pt `#F0EDE8` at 50%

**Filter system (right side, outside tank):**
- Small rounded rect, X: 21.0", Y: 8.0", W: 2.0", H: 2.0", fill `#1E2435`, border 1 pt `#2EC4B6`
- Text: `FILTER` Barlow SemiBold 12 pt `#2EC4B6`
- `5-10 um continuous` JetBrains Mono 10 pt `#F0EDE8`

**Bath parameter labels (inside tank):**

Right side (X: 14.0", Y: 7.0"):
- `Ni2+: 4.5-6.5 g/L` JetBrains Mono 14 pt `#27AE60`
- `NaH2PO2: 20-30 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `pH: 4.6-5.2 (ACID)` JetBrains Mono 14 pt `#E8A020`
- `Temp: 85-91 C (185-196 F)` JetBrains Mono 14 pt `#E05C5C`

Left side (X: 4.0", Y: 7.0"):
- `Rate: 18-25 um/hr (FASTEST)` JetBrains Mono 13 pt `#27AE60`
- `Loading: 0.25-0.50 dm2/L` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Stabilizer: 1-5 ppm` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Bath life: 6-8 MTO` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `AUTOCATALYTIC: Ni2+ + 2 H2PO2- + 2 H2O --> Ni0 + 2 H2PO3- + H2 + 2 H+` JetBrains Mono 13 pt `#E8A020`

---

### ZONE 4 -- Bath Composition + MTO Tracking

**Section label:** `BATH CHEMISTRY + BATH LIFE TRACKING` -- Y: 14.7".

**BLOCK D -- Bath Composition Table (X: 0.5", W: 14.0", Y: 15.3" to 18.8")**

| Component | Concentration | Role |
|---|---|---|
| Nickel sulfate (NiSO4 . 6H2O) | 20-30 g/L Ni2+ (4.5-6.5 g/L as Ni) | Metal ion source |
| Sodium hypophosphite (NaH2PO2 . H2O) | 20-30 g/L | Reducing agent |
| Lactic acid (90%) | 20-30 mL/L | Primary complexant |
| Malic acid | 5-15 g/L | Secondary complexant |
| Succinic acid | 5-10 g/L | Buffer + complexant |
| Propionic acid | 2-5 mL/L | pH buffer |
| Stabilizer (Pb, thiourea, thiomalic, IO3-) | 1-5 ppm | Prevents spontaneous decomposition |
| pH adjuster (NaOH or dilute H2SO4) | As needed | Maintain pH 4.6-5.2 |

Header: `#3A4055`. Data: JetBrains Mono 12 pt. Roles: Inter Regular 12 pt at 70%.

**BLOCK E -- MTO Tracking Gauge (X: 15.0", W: 8.5", Y: 15.3" to 20.3")**

Title: `BATH LIFE -- METAL TURNOVERS (MTO)` Barlow SemiBold 18 pt `#F0EDE8`

Definition box:
- `1 MTO = deposited Ni mass equal to initial Ni2+ charge` Inter Medium 13 pt `#F0EDE8`

Vertical bar gauge (H: 3.0", W: 2.0"):
- Green zone (0-4 MTO): fill `#27AE60` at 40%
- Yellow zone (4-6 MTO): fill `#E8A020` at 30%
- Red zone (6-8 MTO): fill `#E05C5C` at 40%
- Hard stop line at 8 MTO: 2 pt `#E05C5C`

Labels beside gauge:
- `0-4 MTO: Fresh bath -- optimal quality` `#27AE60` 12 pt
- `4-6 MTO: Quality degrades -- monitor closely` `#E8A020` 12 pt
- `6-8 MTO: Warning zone -- plan for dump` `#E05C5C` 12 pt
- `> 8 MTO: HARD DISCARD` `#E05C5C` 14 pt bold

Orthophosphite note:
- `Orthophosphite accumulates ~15-20 g/L per MTO` JetBrains Mono 11 pt `#F0EDE8` at 60%
- `Discard at > 120 g/L orthophosphite` JetBrains Mono 11 pt `#E05C5C`
- `Some suppliers claim 8-10 MTO with dump/replenish` JetBrains Mono 11 pt `#F0EDE8` at 50%

---

### ZONE 5 -- pH vs P% + Defect Diagnosis

**Left -- pH vs. P% Relationship (X: 0.5", W: 11.0", Y: 20.7" to 26.3")**

Title: `THE MASTER LEVER -- pH CONTROLS PHOSPHORUS` Barlow Condensed ExtraBold 22 pt `#E8A020`

**Visual: stepped bar chart showing pH ranges mapped to P% territory:**

| pH Range | Expected P% | Territory | Bar Color |
|---|---|---|---|
| 4.2-4.4 | 10-13% | HIGH-P | `#2EC4B6` |
| 4.6-5.0 | 6-9% | MID-P (TARGET) | `#27AE60` |
| 5.0-5.5 | 4-6% | LOW MID-P | `#E8A020` |
| 6.0+ | 2-4% | LOW-P TERRITORY | `#3A4055` |

Callout: `A single bath drifting from pH 4.8 to 4.3 crosses into High-P territory -- all deposit properties change.` Inter Medium 14 pt `#E05C5C`

Key rule: `pH TOLERANCE: +/- 0.2 (NON-NEGOTIABLE)` Barlow SemiBold 16 pt `#E05C5C`

**Right -- Defect Diagnosis Grid (X: 12.0", W: 11.5", Y: 20.7" to 26.3")**

Title: `COMMON DEFECTS` Barlow Condensed ExtraBold 22 pt `#F0EDE8`

| Defect | Color | Cause | Fix |
|---|---|---|---|
| SKIP PLATING | `#E05C5C` | Contamination, poor activation, stabilizer excess | Improve cleaning; reduce stabilizer |
| pH DRIFT | `#E8A020` | Reaction consumes and releases H+ dynamically | Check pH every 2-4 hr; NaOH or H2SO4 |
| WRONG P% | `#E05C5C` | pH outside 4.6-5.2 range | pH < 4.6 = high P; pH > 5.2 = low P |
| PITTING | `#E8A020` | Chloride drag-in, H2 entrapment, particulate | DI rinse; filter 5-10 um |
| BATH DECOMPOSITION | `#E05C5C` | Low stabilizer, overheated, under-loaded | FIRE HAZARD -- dump immediately |

Each row: left accent 0.06" in defect color. Cause: Inter Regular 12 pt. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 6 -- QC Methods + Bath Stability

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- QC Methods (X: 0.5", W: 11.0"):**

Title: `QUALITY CONTROL -- NO HULL CELL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Explanation: `EN baths are not electroplated -- the Hull cell does not apply. Instead:` Inter Regular 13 pt `#F0EDE8` at 70%.

| QC Method | What It Measures | Frequency |
|---|---|---|
| Plating rate coupon | um/hr deposition rate | Every load or every 2-4 hr |
| Phosphorus by ICP | Wt% P in deposit | Weekly or per lot |
| Phosphorus (wet chem) | Wt% P (alternate to ICP) | As needed |
| Thickness (XRF or destructive) | Deposit thickness (um) | Per spec |
| Adhesion (bend/tape test) | Coating adhesion | Per lot |
| Ni2+ titration (EDTA) | Bath nickel concentration | Every 2-4 hr |
| pH measurement | Bath pH | EVERY 2-4 HR (CRITICAL) |
| Temperature check | Bath temperature | Every 2-4 hr |

**Right -- Bath Stability (X: 12.0", W: 11.5"):**

Title: `BATH STABILITY -- PREVENTING DECOMPOSITION` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

- Rounded rect fill `#1E2435`, full border 2 pt `#E05C5C`
- Bullets (Inter Regular 14 pt, line height 155%):
  - `Stabilizer is CRITICAL: too low = spontaneous decomposition (EXOTHERMIC, FIRE HAZARD)`
  - `Too high stabilizer = bath goes inert (no plating)`
  - `Loading ratio: under-loaded baths (< 0.1 dm2/L) are highest risk`
  - `NEVER leave bath at 85-91 C without parts or dummy load`
  - `Hot spots on heater elements (> 5-10 C above bath) nucleate decomposition`
  - `Filter continuously (5-10 um) -- metallic fines are nucleation sites`
  - `If bath begins to decompose: DUMP IMMEDIATELY -- do not attempt to save`

---

### ZONE 7 -- Footer

Standard. Title: `Electroless Nickel (Mid Phos) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM B733 Type IV; AMS 2404/2405; IPC-4552B. EN baths are proprietary formulations -- consult your supplier TDS for specific concentrations and operating windows.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Decomposition warning border (#E05C5C -> #B83E3E).
**Export:** Six files -- `EN Mid-P Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EN Mid-P cluster and the most important after the Process Flow overview (#223). The pH-vs-P% chart is the single most valuable element on the poster -- it answers the most-asked question in EN shops: "what controls phosphorus content?" The answer is pH, and the visual should make this relationship instantly clear. The "FASTEST" callout on deposition rate and the higher operating temperature (85-91 C vs 65-80 C for Low-P) are the primary differentiators from the Low-P Main Tank poster (#220).

The organic acid complexant system (lactic, malic, succinic, propionic) replaces the ammonium-based system used in alkaline Low-P baths. This is a fundamental chemistry difference driven by the acid pH regime.

---

*Alaina -- Poster #228 -- Construction Workup v1.0 -- 2026-04-26*
