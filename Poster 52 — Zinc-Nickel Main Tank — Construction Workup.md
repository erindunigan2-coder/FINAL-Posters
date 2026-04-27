---
Project: Plating Posters Inc
Poster Number: 52
Title: "Zinc-Nickel Main Tank"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-03 technical reference (zinc-nickel alloy plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Zinc-nickel alloy plating main tank -- the core electrodeposition stage. Alkaline Zn-Ni (dominant) and acid Zn-Ni (high-speed variant). Target alloy 12--16% Ni by weight per ASTM B841. This is the most chemistry-dense poster in the EP-03 cluster.
Process Scope: Zinc-nickel alloy plating main tank (Stage 5 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ZincNickelPlating
  - MainTank
  - ConstructionWorkup
  - Series2
  - ClusterEP03
---

# Poster #52 -- Construction Workup
## Zinc-Nickel Main Tank

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 5 of 8. This is the heart of the zinc-nickel process -- the electrodeposition tank where the Zn-Ni alloy is co-deposited onto the substrate. The poster covers both alkaline (dominant, 90%+ of installations) and acid (high-speed niche) variants. The critical control variable is alloy composition: 12--16% Ni by weight. Below 10% Ni, corrosion resistance drops dramatically. Above 18% Ni, the coating becomes cathodic to steel and loses sacrificial protection -- the exact opposite of what you want.

This is the most technically dense poster in the EP-03 cluster. Bath chemistry, operating parameters, alloy control, anode management, analytical methods, and a comprehensive defect table.

Hero visual: plating tank cross-section with bath chemistry breakdown and alloy composition control zone.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Plating tank hero (Block B):** Tank cross-section with labeled components -- anodes, cathode (workpiece), solution level, heater, agitation.
2. **Bath chemistry table (Block C):** Alkaline Zn-Ni formulation with component concentrations and purposes.
3. **Operating parameters table (Block D):** Side-by-side alkaline vs. acid.
4. **Alloy composition control zone (Block E):** The 12--16% Ni target zone with high/low consequence callouts.
5. **Defect table (Block F):** 7 common defects with causes and fixes.
6. **Orientation strip:** Stage 5 highlighted (Emerald).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Emerald)
ZONE 3 -- PLATING TANK HERO + BATH CHEMISTRY (4.2"--14.0" / ~9.8")
  Block B: Tank cross-section diagram
  Block C: Bath chemistry table (alkaline Zn-Ni)
ZONE 4 -- OPERATING PARAMETERS + ALLOY CONTROL (14.0"--20.5" / ~6.5")
  Block D: Alkaline vs. acid operating parameters
  Block E: Alloy composition control zone
ZONE 5 -- DEFECTS + ANALYTICAL METHODS (20.5"--27.0" / ~6.5")
  Block F: Common defects table
  Block G: Analytical methods callout
ZONE 6 -- ANODE MANAGEMENT + SAFETY (27.0"--32.5" / ~5.5")
  Block H: Anode management
  Block I: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ZINC-NICKEL MAIN TANK` -- 80 pt `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".
**Subheading:** `Zinc-Nickel -- Stage 5 of 8 -- Alloy Electrodeposition` -- 34 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `12--16% nickel. 1,000+ hours salt spray. The alloy ratio is everything -- monitor it, control it, verify it every shift.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, activated substrate  -->  After: Zn-Ni alloy deposit (12--16% Ni) with sacrificial + barrier protection`

---

### ZONE 3 -- Plating Tank Hero + Bath Chemistry

**Section label:** `THE ZINC-NICKEL PLATING BATH` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section Diagram**

Y: 5.0" to 9.0". Full width.

Rounded rect representing tank (W: 23.0", H: 3.5"), fill `#252B3D`, border 2 pt `#27AE60`.

Inside tank (left to right):
- Zinc anodes (labeled): `Pure Zn anodes (99.99% SHG)` -- in anode bags
- Workpiece (cathode): `Zn-Ni alloy deposits here`
- Solution level line
- Heater element (labeled): `75--95 F (alkaline) / 75--105 F (acid)`
- Agitation: `Mechanical or solution flow; air OK if oil-free`

Labels: JetBrains Mono 12 pt `#F0EDE8`. Component names: Barlow SemiBold 13 pt `#27AE60`.

**BLOCK C -- Alkaline Zn-Ni Bath Chemistry Table**

Y: 9.5" to 13.8".

Section sublabel: `ALKALINE ZINC-NICKEL BATH FORMULATION` Barlow SemiBold 18 pt `#27AE60`.

| Component | Concentration | Purpose |
|---|---|---|
| Zinc (as ZnO or Zn metal) | 6--12 g/L as Zn metal | Zinc ion source |
| Nickel (as NiSO4 or NiCl2) | 1--3 g/L as Ni metal | Nickel ion source |
| Sodium hydroxide (NaOH) | 100--150 g/L | Conductivity, complexation |
| Amine complexing agent | Per supplier TDS (proprietary) | Stabilizes Ni in alkaline solution |
| Brightener / grain refiner | Per supplier TDS | Deposit quality |
| Zn:Ni ratio in bath | 4:1 to 8:1 (metal basis) | Controls alloy composition |

Data: JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt `#F0EDE8` on `#3A4055`.

Below table footnote:
- `Acid Zn-Ni variant: Zn 25--50 g/L, Ni 25--40 g/L as metal, NH4Cl or KCl 100--200 g/L, boric acid 25--35 g/L, pH 5.5--6.5. Higher speed, narrower window.` JetBrains Mono 11 pt `#F0EDE8` at 60%.

---

### ZONE 4 -- Operating Parameters + Alloy Control

**Section label:** `OPERATING PARAMETERS` -- Y: 14.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Side-by-Side Operating Parameters**

Y: 14.8" to 18.0".

| Parameter | Alkaline Zn-Ni | Acid Zn-Ni |
|---|---|---|
| Temperature | 75--95 F (24--35 C) | 75--105 F (24--40 C) |
| pH | >13 (strongly alkaline) | 5.5--6.5 |
| Cathode CD (rack) | 10--40 ASF | 10--50 ASF |
| Cathode CD (barrel) | 5--15 ASF | 5--20 ASF |
| Voltage | 4--12 V | 3--8 V |
| Agitation | Mechanical or solution flow | Air preferred |
| Anode material | Pure zinc (no Ni in anode) | Steel or Ni-plated steel (insoluble) or Zn |
| Cathodic efficiency | 40--70% | 80--95% |
| Plating rate (20 ASF) | ~0.15--0.25 mil/hr | ~0.25--0.4 mil/hr |

**BLOCK E -- Alloy Composition Control Zone**

Y: 18.3" to 20.3".

Three horizontal bars representing alloy ranges:

- Left bar (red zone): `< 10% Ni` -- fill `#E05C5C` at 20%
  - Label: `INSUFFICIENT -- corrosion resistance drops dramatically` Inter Medium 12 pt `#E05C5C`
- Center bar (green zone): `12--16% Ni` -- fill `#27AE60` at 20%, border 2 pt `#27AE60`
  - Label: `TARGET ZONE -- optimal sacrificial + barrier protection` Barlow SemiBold 14 pt `#27AE60`
  - Sub: `ASTM B841 Class 2 | 720--1,000+ hr red rust with passivation` JetBrains Mono 11 pt `#27AE60`
- Right bar (amber zone): `> 18% Ni` -- fill `#E8A020` at 20%
  - Label: `CATHODIC -- coating no longer sacrificial to steel` Inter Medium 12 pt `#E8A020`

---

### ZONE 5 -- Defects + Analytical Methods

**Section label:** `COMMON DEFECTS AND CORRECTIVE ACTIONS` -- Y: 20.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Defect Table**

Y: 21.3" to 25.5".

| Defect | Cause | Corrective Action |
|---|---|---|
| Low Ni in deposit (<10%) | Low bath Ni, high CD, low temperature | Add Ni replenisher; reduce CD; raise temp |
| High Ni in deposit (>18%) | High bath Ni, low CD, high temperature | Reduce Ni; plate at higher CD |
| Burning at HCD | Low Zn metal, high CD | Add Zn; reduce CD |
| Dark deposits | Organic contamination, metallic contamination (Cu, Fe) | Carbon treat; dummy plate; check cleaning |
| Blistering | Poor cleaning, insufficient activation | Review pre-treatment; extend electrocleaning |
| Uneven alloy distribution | Poor agitation, improper racking | Improve agitation; re-rack for uniform CD |
| Poor passivation acceptance | Over-bright deposit, Ni% out of range | Adjust brightener; correct alloy ratio |

Cards: fill `#1E2435`, alternating `#252B3D`. Defect: Barlow SemiBold 13 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

**BLOCK G -- Analytical Methods Callout**

Y: 25.8" to 26.8".

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, W: 23.0", H: 1.0".

Title: `ANALYTICAL METHODS` Barlow SemiBold 14 pt `#2EC4B6`

Body (JetBrains Mono 11 pt `#F0EDE8`):
- `Zinc: EDTA @ pH 10 | Nickel: EDTA + murexide or DMG | NaOH: HCl titration | Alloy (deposit): XRF every shift | Hull cell: 267 mL, 2A, 10 min`

---

### ZONE 6 -- Anode Management + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Anode Management (X: 0.5", W: 14.0"):**

Section label: `ANODE MANAGEMENT` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `Alkaline Zn-Ni: Pure zinc anodes (99.99% SHG). No nickel in the anode -- Ni is added separately as a salt replenisher.`
- `Anode bags: Polypropylene, 1--5 micron. Mandatory. Prevents zinc fines from roughening the deposit.`
- `Anode:cathode ratio: 1:1 to 2:1. Maintain consistent anode area for stable dissolution rate.`
- `Anode passivation: Uncommon in alkaline (NaOH dissolves zinc readily). More common in acid variant if chloride is low.`
- `Monitor: Zinc metal builds in alkaline baths (anode efficiency > cathode efficiency). Adjust by reducing anode area or dilution.`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> - Sodium hydroxide (100--150 g/L): severe chemical burn. pH > 13.
> - Nickel compounds: dermal sensitizer; IARC Group 2B carcinogen (inhalation).
> - PPE: NaOH-resistant gloves (neoprene), face shield, rubber apron.
> - Ventilation: fume suppression recommended; nickel mist must be controlled.
> - Wastewater: Zn precipitates at pH 8.5--9.5; Ni at pH 9.0--10.0. Two-stage precipitation may be needed.

---

### ZONE 7 -- Footer

Standard footer. Title: `Zinc-Nickel Main Tank`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for zinc-nickel alloy plating. Alloy composition, bath formulations, and process limits vary by proprietary product. Consult your process supplier for application-specific guidance. Source: ASTM B841; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #47).
**Export:** Six files -- `Zinc-Nickel Main Tank -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the chemistry powerhouse of the EP-03 cluster. The alloy composition control zone (Block E) must be the visual anchor after the headline -- the three-bar red/green/amber visualization makes the 12--16% Ni target impossible to miss. The defect table is comprehensive (7 entries) because alloy plating has more failure modes than simple zinc.

Key technical decisions:
- Alkaline Zn-Ni is featured as the primary chemistry because it dominates industry (90%+ of installations per Watson's brief). Acid Zn-Ni is footnoted and included in the side-by-side parameter table.
- XRF alloy verification "every shift" is the actionable recommendation -- this is per industry best practice for alloy plating.
- Anode management is unique to Zn-Ni: pure zinc anodes with separate nickel salt replenishment. This surprises shops accustomed to soluble alloy anodes.

-> Watson: Confirm the 4:1 to 8:1 Zn:Ni metal ratio range in bath for alkaline systems. Watson's brief shows Zn 6--12 g/L and Ni 1--3 g/L which gives roughly 2:1 to 12:1 range -- the 4:1 to 8:1 is the practical operating window within that. Verify.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #52 -- Construction Workup v1.0*
*2026-04-26*
