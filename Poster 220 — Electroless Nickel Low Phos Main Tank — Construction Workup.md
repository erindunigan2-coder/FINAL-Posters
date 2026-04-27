---
Project: Plating Posters Inc
Poster Number: 220
Title: "Electroless Nickel (Low Phos) -- Main Tank"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 1: EN Low-P, Poster 6)"
Process Scope: Electroless nickel low phosphorus main plating tank (Stage 5 of 7)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessNickel
  - LowPhosphorus
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEN-LP
---

# Poster #220 -- Construction Workup
## Electroless Nickel (Low Phos) -- Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 7. The heart of the process -- the autocatalytic EN bath. Unlike electroplating, there is no rectifier, no anodes, no external current. The deposit grows by chemical reduction: hypophosphite reduces nickel ions on the catalytic surface, generating a Ni-P alloy. The freshly deposited alloy is itself catalytic, perpetuating the reaction.

This poster is the densest in the cluster. It covers bath composition, operating parameters, MTO (metal turnover) tracking, deposit properties, and bath stability management. No Hull cell for EN -- instead, QC is plating rate coupon testing, phosphorus analysis (ICP or wet chemistry), and thickness verification.

Hero visual: an EN tank cross-section showing parts immersed with uniform deposit buildup on all surfaces including blind holes -- the defining advantage of EN over electrolytic processes.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **EN tank cross-section hero (Block B):** Tank with parts showing uniform deposit on all surfaces. NO anodes, NO rectifier -- this is the visual key difference from electroplating. Show bubbling (H2 evolution from the reaction) on part surfaces. Filter system shown.
2. **Bath composition panel (Block D):** Multi-component breakdown (nickel sulfate, hypophosphite, complexants, stabilizer, pH adjuster).
3. **MTO tracking gauge (Block E):** Visual representation of bath life in metal turnovers.
4. **Deposit properties panel (Block F):** As-plated and heat-treated properties.
5. **NOTE: No Hull cell.** EN does not use a Hull cell. QC section covers plating rate test, phosphorus analysis by ICP or wet chemistry, and thickness measurement.

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
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- QC METHODS + BATH STABILITY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ELECTROLESS NICKEL` -- Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Low Phosphorus (1-4% P) -- Main Tank -- Stage 5 of 7` -- Barlow SemiBold, 30 pt, `#27AE60` (Emerald). X: 0.5", Y: 1.4".

**Tagline:** `No rectifier. No anodes. Uniform deposit on every surface. The autocatalytic reaction that plates itself -- if you keep the chemistry right.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.

Below: `Before: Clean, activated surface (catalytic)  -->  After: Uniform Ni-P alloy deposit (1-4% P, 650-750 HV)`

---

### ZONE 3 -- EN Tank Hero

**Section label:** `THE ELECTROLESS NICKEL LOW-P BATH` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**NO ANODES -- this is the key visual difference.** Label where anodes would be in an electrolytic tank:
- Dashed outline rectangles (ghosted), X: 2.5" and X: 20.5", Y: 6.0", W: 1.0", H: 5.5"
- Fill: none. Border: 1 pt `#3A4055` dashed
- Label: `NO ANODES` Barlow SemiBold 14 pt `#E8A020`
- Sub-label: `No external current source` Inter Regular 11 pt `#F0EDE8` at 50%

**NO RECTIFIER -- label at top:**
- Dashed outline rectangle where rectifier would sit: X: 10.0", Y: 5.0", W: 4.0", H: 0.8"
- Border: 1 pt `#3A4055` dashed
- Text: `NO RECTIFIER` Barlow SemiBold 12 pt `#E8A020`
- Sub: `Autocatalytic -- reaction is self-sustaining` Inter Regular 11 pt `#F0EDE8` at 50%

**Parts / Workpieces (center):**
- Three stylized parts of different shapes (rect, cylinder, L-bracket) hanging from rack bar
- Each part has a thin green border showing uniform deposit: 2 pt `#27AE60`
- The deposit follows all contours uniformly -- including inside surfaces and blind holes
- Label: `UNIFORM DEPOSIT ON ALL SURFACES` Barlow SemiBold 14 pt `#27AE60`
- Sub: `+/- 1-2 um thickness variation` JetBrains Mono 12 pt `#27AE60`

**H2 bubbles on surfaces:**
- Small circles (0.1" dia), fill `#F0EDE8` at 20%, scattered on part surfaces
- Label: `H2 evolution (byproduct)` Inter Regular 11 pt `#F0EDE8` at 50%

**Filter system (right side, outside tank):**
- Small rounded rect, X: 21.0", Y: 8.0", W: 2.0", H: 2.0", fill `#1E2435`, border 1 pt `#2EC4B6`
- Text: `FILTER` Barlow SemiBold 12 pt `#2EC4B6`
- `5-10 um continuous` JetBrains Mono 10 pt `#F0EDE8`
- Circulation arrows from tank through filter and back

**Bath parameter labels (inside tank):**

Right side (X: 14.0", Y: 7.0"):
- `Ni2+: 4.5-6.0 g/L` JetBrains Mono 14 pt `#27AE60`
- `NaH2PO2: 20-35 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `pH: 8.5-9.5 (ALKALINE)` JetBrains Mono 14 pt `#E8A020`
- `Temp: 80-92 C (176-198 F)` JetBrains Mono 14 pt `#F0EDE8`

Left side (X: 4.0", Y: 7.0"):
- `Rate: 10-15 um/hr` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Loading: 0.25-0.50 dm2/L` JetBrains Mono 13 pt `#F0EDE8` at 70%
- `Stabilizer: 1-5 ppm` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Bottom callout (Y: 13.5"):**
- `AUTOCATALYTIC: Ni2+ + 2 H2PO2- + 2 H2O --> Ni0 + 2 H2PO3- + H2 + 2 H+` JetBrains Mono 13 pt `#E8A020`

---

### ZONE 4 -- Bath Composition + MTO Tracking

**Section label:** `BATH CHEMISTRY + BATH LIFE TRACKING` -- Y: 14.7".

**BLOCK D -- Bath Composition Table (X: 0.5", W: 14.0", Y: 15.3" to 18.5")**

| Component | Concentration | Role |
|---|---|---|
| Nickel sulfate (NiSO4 . 6H2O) | 15-25 g/L Ni2+ | Metal ion source |
| Sodium hypophosphite | 20-35 g/L | Reducing agent |
| Ammonium sulfate | 30-65 g/L | Complexant + buffer |
| Sodium citrate | 10-20 g/L | Complexant (prevents Ni(OH)2 ppt) |
| Sodium acetate | 5-15 g/L | pH buffer |
| Stabilizer (Pb, thiourea, IO3-) | 1-5 ppm | Prevents spontaneous decomposition |
| pH adjuster (NaOH or NH4OH) | As needed | Maintain pH 8.5-9.5 |

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

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 COMMON DEFECTS` -- Y: 20.7".

**BLOCK F -- 3x2 Grid (Y: 21.3" to 26.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP PLATING | `#E05C5C` | Contamination, poor activation, or stabilizer excess | Improve cleaning; reduce stabilizer; check activation |
| R1C2 | PITTING | `#E05C5C` | Chloride drag-in, H2 entrapment, or particulate | DI pre-plate rinse; filter 5-10 um; reduce loading |
| R1C3 | LOW RATE | `#E8A020` | pH too low, temp too low, or reducer depleted | Check pH; raise temp; replenish hypophosphite |
| R2C1 | ROUGH DEPOSIT | `#E8A020` | Particulate in bath or metallic fines | Filter continuously; check for decomposition seeds |
| R2C2 | DARK DEPOSIT | `#2EC4B6` | Metallic contamination (Cu, Zn, Fe) | Dummy plate at low temp; carbon treat |
| R2C3 | BATH DECOMPOSITION | `#E05C5C` | Low stabilizer, overheated, or under-loaded | FIRE HAZARD -- dump immediately; check stabilizer ppm |

Each card: W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- QC Methods + Bath Stability

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- QC Methods (X: 0.5", W: 11.0"):**

Title: `QUALITY CONTROL -- NO HULL CELL` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Explanation: `EN baths are not electroplated -- there is no current to vary across a panel. The Hull cell does not apply. Instead:` Inter Regular 13 pt `#F0EDE8` at 70%.

| QC Method | What It Measures | Frequency |
|---|---|---|
| Plating rate coupon | um/hr deposition rate | Every load or every 2-4 hr |
| Phosphorus by ICP | Wt% P in deposit | Weekly or per lot |
| Phosphorus (wet chem) | Wt% P (alternate to ICP) | As needed |
| Thickness (XRF or destructive) | Deposit thickness (um) | Per spec |
| Adhesion (bend/tape test) | Coating adhesion | Per lot |
| Ni2+ titration (EDTA) | Bath nickel concentration | Every 2-4 hr |
| pH measurement | Bath pH | Every 2-4 hr |
| Temperature check | Bath temperature | Every 2-4 hr |

**Right -- Bath Stability (X: 12.0", W: 11.5"):**

Title: `BATH STABILITY -- PREVENTING DECOMPOSITION` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

- Rounded rect fill `#1E2435`, full border 2 pt `#E05C5C`
- Bullets (Inter Regular 14 pt, line height 155%):
  - `Stabilizer is CRITICAL: too low = spontaneous decomposition (EXOTHERMIC, FIRE HAZARD)`
  - `Too high stabilizer = bath goes inert (no plating)`
  - `Loading ratio: under-loaded baths (< 0.1 dm2/L) are highest risk`
  - `NEVER leave bath at operating temp without parts or dummy load`
  - `Hot spots on heater elements (> 5-10 C above bath) nucleate decomposition`
  - `Filter continuously (5-10 um) -- metallic fines are nucleation sites`
  - `If bath begins to decompose: DUMP IMMEDIATELY -- do not attempt to save`

---

### ZONE 7 -- Footer

Standard. Title: `Electroless Nickel (Low Phos) -- Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM B733 Type II/III; AMS 2404/2405. EN baths are proprietary formulations -- consult your supplier TDS for specific concentrations and operating windows.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table. Decomposition warning border (#E05C5C -> #B83E3E).
**Export:** Six files -- `EN Low-P Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the densest poster in the EN Low-P cluster. The visual absence of anodes and rectifier is the single most important design choice -- it communicates "this is not electroplating" instantly. The MTO gauge replaces the Hull cell strip from electroplating posters. The bath stability/decomposition warning is an EN-specific safety concern with no parallel in electroplating: a decomposing EN bath is exothermic and can cause fires.

---

*Alaina -- Poster #220 -- Construction Workup v1.0 -- 2026-04-26*
