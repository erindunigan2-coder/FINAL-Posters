---
Project: Plating Posters Inc
Poster Number: 68
Title: "Nickel Sulfamate Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-05 technical reference (Sulfamate nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Nickel sulfamate main plating tank -- the electrodeposition stage for low-stress engineering nickel. Ni(SO3NH2)2 + H3BO3. Operates 130--145 F, pH 3.8--4.2, 20--75+ ASF. Cathode efficiency 95--100%. The defining feature: near-zero internal stress, controllable from tensile to compressive. CRITICAL: sulfamate hydrolyzes irreversibly above 160 F or below pH 3.0.
Process Scope: Sulfamate nickel plating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Sulfamate
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP05
---

# Poster #68 -- Construction Workup
## Nickel Sulfamate Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the centerpiece of the EP-05 cluster -- the sulfamate nickel plating bath. Unlike Watts nickel (Poster #60), sulfamate is engineered for low stress. It is the only nickel process that can achieve near-zero internal stress, making it indispensable for electroforming, aerospace components, waveguides, and any application where the deposit must survive mechanical loading without cracking.

The chemistry is elegant: nickel sulfamate as the sole nickel salt (no NiSO4), optional low NiCl2 for anode dissolution, and boric acid for pH buffering. The simplicity is the point -- fewer additives means fewer stress-inducing variables. But this simplicity comes with a critical vulnerability: sulfamate hydrolyzes irreversibly above 160 F or below pH 3.0. Once hydrolyzed, the bath cannot be recovered. Temperature and pH are life-or-death parameters.

Hero visual: plating tank cross-section with stress control as the central theme.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank hero (Block B):** Tank cross-section with bath chemistry breakdown.
2. **Bath chemistry table (Block C):** Sulfamate formulation for electroforming and general engineering.
3. **Stress control panel (Block E):** The factors that shift stress from tensile to compressive -- the unique value proposition of sulfamate.
4. **Hydrolysis warning (Block D):** Prominent coral callout -- this is the #1 catastrophic failure mode.
5. **Defect table (Block F):** 6 common defects.
6. **Orientation strip:** Stage 5 highlighted (Emerald).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO + BATH CHEMISTRY (4.2"--14.0" / ~9.8")
  Block B: Tank cross-section diagram
  Block C: Bath chemistry table (electroforming + engineering)
  Block D: Hydrolysis warning callout
ZONE 4 -- OPERATING PARAMETERS + STRESS CONTROL (14.0"--20.0" / ~6.0")
  Block D2: Operating parameters (electroforming vs. engineering)
  Block E: Stress control factor table
ZONE 5 -- DEFECTS + ANODE MANAGEMENT (20.0"--27.0" / ~7.0")
  Block F: Common defects table
  Block G: Anode management
ZONE 6 -- ANALYTICAL METHODS + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Analytical methods
  Block I: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NICKEL SULFAMATE MAIN TANK` -- 72 pt `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Sulfamate) -- Stage 5 of 8 -- Low-Stress Electrodeposition` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Near-zero internal stress. The only nickel process for electroforming, fatigue-critical parts, and deposits that must never crack.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated substrate  -->  After: Low-stress sulfamate nickel deposit (50--500+ microinch per spec)`

---

### ZONE 3 -- Plating Tank Hero + Bath Chemistry

**Section label:** `THE SULFAMATE NICKEL BATH` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section Diagram**

Y: 5.0" to 8.5". Full width.

Rounded rect representing tank (W: 23.0", H: 3.0"), fill `#252B3D`, border 2 pt `#27AE60`.

Inside tank (labeled):
- Nickel S-Rounds in Ti baskets with anode bags (left): `S-Rounds (sulfur-depolarized) in Ti baskets + PP bags`
- Workpiece (cathode, center): `Low-stress Ni deposits here`
- Heater element: `130--145 F (54--63 C) -- NEVER exceed 160 F`
- Agitation: `Cathode rod oscillation or solution flow; air agitation AVOIDED`
- Filtration: `Continuous, 1--5 micron + activated carbon`

Labels: JetBrains Mono 12 pt `#F0EDE8`. Component names: Barlow SemiBold 13 pt `#27AE60`.

**BLOCK C -- Bath Chemistry Table**

Y: 9.0" to 12.0".

Section sublabel: `SULFAMATE NICKEL BATH FORMULATION` Barlow SemiBold 18 pt `#27AE60`.

| Component | Electroforming | General Engineering | Purpose |
|---|---|---|---|
| Nickel sulfamate [Ni(SO3NH2)2] | 300--450 g/L | 450--650 g/L | Primary Ni source (high solubility) |
| Nickel chloride (NiCl2.6H2O) | 0 g/L (chloride-free) | 5--30 g/L | Anode dissolution; adds stress |
| Boric acid (H3BO3) | 30--45 g/L | 37--45 g/L | Cathode film pH buffer |
| Nickel metal content | 60--80 g/L | 80--110 g/L | |
| Stress reducer (saccharin) | 50--200 mg/L (if needed) | Per TDS | Shifts stress from tensile to compressive |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt on `#3A4055`.

**BLOCK D -- Hydrolysis Warning**

Y: 12.3" to 13.8".

- Rounded rect, full width, H: 1.3", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 6
- Title: `CRITICAL: SULFAMATE HYDROLYSIS` Barlow Condensed ExtraBold, 18 pt, `#E05C5C`
- Body: `Nickel sulfamate hydrolyzes to nickel ammonium sulfate IRREVERSIBLY at temperatures > 160 F (71 C) or pH < 3.0. Hydrolysis increases stress permanently. The bath cannot be recovered -- partial or full replacement required. NEVER allow temperature or pH to exceed limits.` Inter Medium 13 pt `#F0EDE8`.

---

### ZONE 4 -- Operating Parameters + Stress Control

**Section label:** `OPERATING PARAMETERS AND STRESS CONTROL` -- Y: 14.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D2 -- Operating Parameters (Side-by-Side)**

Y: 14.8" to 17.5".

| Parameter | Low-Stress Electroforming | General Engineering |
|---|---|---|
| Temperature | 90--110 F (32--43 C) | 100--140 F (38--60 C) |
| pH | 3.8--4.2 | 3.5--4.5 |
| Cathode CD | 10--40 ASF | 20--100 ASF |
| Voltage | 4--12 V | 6--15 V |
| Agitation | Cathode oscillation or solution flow; NO air | Air OK for engineering if quality permits |
| Filtration | Continuous, 1--5 micron + carbon | Same |
| Anode material | S-Rounds in Ti baskets + bags | Same |
| Cathodic efficiency | 95--100% | 95--100% |
| Plating rate (40 ASF) | ~0.9--1.0 mil/hr | ~0.9--1.0 mil/hr |
| Plating rate (100 ASF) | -- | ~2.2--2.5 mil/hr |

**BLOCK E -- Stress Control Factor Table**

Y: 17.8" to 19.8".

Section sublabel: `WHAT CONTROLS DEPOSIT STRESS` Barlow SemiBold 16 pt `#E8A020`.

| Factor | Effect on Stress |
|---|---|
| Higher chloride (NiCl2) | Increases tensile stress |
| Higher temperature (> 140 F) | Risk of hydrolysis; stress erratic |
| Lower pH (< 3.5) | Hydrolysis risk; tensile stress increases |
| Organic contamination | Increases tensile stress dramatically |
| Saccharin (stress reducer) | Shifts tensile to compressive; 50--200 mg/L |
| Higher current density | Slightly increases tensile stress |
| Metallic impurities (Cu, Fe, Zn) | Increase stress and embrittlement |

Data: JetBrains Mono 12 pt `#F0EDE8`. Factor column: Inter Medium 13 pt `#F0EDE8`.

---

### ZONE 5 -- Defects + Anode Management

**Section label:** `COMMON DEFECTS AND ANODE MANAGEMENT` -- Y: 20.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Common Defects Table**

Y: 20.8" to 24.5".

| Defect | Cause | Corrective Action |
|---|---|---|
| High tensile stress | Chloride too high, organics, hydrolysis | Reduce NiCl2; carbon treat; check for hydrolysis |
| Cracking | Extreme tensile stress + low ductility | Add stress reducer (saccharin); purify bath |
| Pitting | Low wetting agent, particles, poor filtration | Add anti-pit (use sparingly -- organics affect stress) |
| Rough deposits | Particulates, anode dissolution products | Filter continuously; anode bags; maintain Ti baskets |
| Peeling | Inadequate activation or strike on passivating alloy | Review Wood's strike procedure |
| Sulfamate hydrolysis | Temperature > 160 F or pH < 3.0 | IRREVERSIBLE -- partial or full bath replacement |

Cards: fill `#1E2435`, alternating `#252B3D`. Defect: `#E05C5C`. Cause: `#F0EDE8`. Fix: `#27AE60`.

**BLOCK G -- Anode Management**

Y: 24.8" to 26.8".

Rounded rect, fill `#1E2435`, left accent `#E8A020`, W: 23.0", H: 1.8".
Title: `ANODE MANAGEMENT` Barlow SemiBold 16 pt `#E8A020`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `S-Rounds (sulfur-depolarized): Standard. Dissolve evenly. Preferred for all applications.`
- `R-Rounds (electrolytic, no sulfur): Used when zero sulfur deposit is specified.`
- `Anode bags: MANDATORY -- polypropylene, 1--5 micron. Prevent roughness.`
- `Ti baskets: Clean regularly. Inspect for damage.`
- `Anode:cathode ratio: 1:1 to 2:1. Maintain consistent area.`
- `Air agitation AVOIDED near anodes: introduces CO2 and organics, increases stress.`

---

### ZONE 6 -- Analytical Methods + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Analytical Methods (X: 0.5", W: 14.0"):**

Section label: `ANALYTICAL METHODS` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#2EC4B6`:

| Analysis | Method |
|---|---|
| Nickel metal | EDTA titration @ pH 10, murexide indicator |
| Chloride | Mohr titration (AgNO3 / K2CrO4) |
| Boric acid | Mannitol + NaOH titration |
| pH | Calibrated pH meter (check daily) |
| Deposit stress | Contractometer or deposit stress strip |
| Deposit thickness | XRF, beta backscatter, or micrometer (thick builds) |
| Hull cell | 267 mL, 2A, 10 min at bath temperature |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Nickel compounds: #1 industrial allergen (dermal sensitizer). IARC Group 1 (inhalation), Group 2B (metallic Ni).
> - Sulfamate solutions: moderately acidic (pH 3.5--4.5). Skin and eye irritant.
> - PPE: nitrile gloves (minimum), neoprene for extended contact, safety goggles.
> - Ventilation: mandatory. Fume suppression or local exhaust.
> - Biological monitoring: urinary nickel recommended for chronic exposure.
> - Wastewater: Ni precipitates at pH 9.5--10.5. Discharge limits: 0.5--3.4 mg/L.

---

### ZONE 7 -- Footer

Standard footer. Title: `Nickel Sulfamate Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for sulfamate nickel plating. Specific formulations and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: ASM Handbook Vol. 5; Modern Electroplating; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #63).
**Export:** Six files -- `Nickel Sulfamate Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most technically distinct main tank poster in the nickel series. Every element contrasts with the Watts Main Tank (Poster #60): no brighteners (usually), chloride optional (not required), air agitation avoided (not preferred), stress is THE control variable (not pH or brightness).

The hydrolysis warning (Block D) is the poster's safety-critical moment. It needs to hit like a stop sign. The stress control table (Block E) is the intellectual centerpiece -- it answers "how do I control stress?" with a clear, factor-by-factor breakdown.

Watson's brief: "CRITICAL NOTE: Nickel sulfamate hydrolyzes to nickel ammonium sulfate at temperatures above 160 deg F (71 deg C) or pH below 3.0. Hydrolysis is irreversible and increases stress."

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #68 -- Construction Workup v1.0*
*2026-04-26*
