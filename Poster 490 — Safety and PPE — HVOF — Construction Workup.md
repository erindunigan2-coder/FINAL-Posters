---
Project: Plating Posters Inc
Poster Number: 490
Title: "Safety & PPE -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 2)"
Technical Source: HVOF safety hazards including supersonic jet noise (110-130 dB), combustible fuel gases (hydrogen, propylene, propane, kerosene), cobalt fume exposure (ACGIH TLV 0.02 mg/m3), and high-pressure oxygen handling. PPE requirements per OSHA, ACGIH, and industry best practice.
Process Scope: HVOF thermal spray -- safety hazards and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Safety
  - PPE
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #490 -- Construction Workup
## Safety & PPE -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the safety poster for the HVOF cluster. HVOF has two unique hazards that demand special emphasis: (1) combustible fuel gases (hydrogen, propylene, kerosene) and (2) cobalt dust from WC-Co feedstock. Cobalt's TLV of 0.02 mg/m3 is one of the lowest in all of industrial hygiene. Coral dominates. The rule card features the cobalt TLV to set the tone.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** 8 hazard cards in a 4x2 grid. Each card: hazard name, details, controls. Coral-tinted.
2. **Cobalt exposure special emphasis (Block D):** Dedicated callout for WC-Co fume hazards.
3. **PPE checklist (Block E):** Visual checklist of required PPE.
4. **"Fuel Gas Safety" callout (Block F):** Full-width banner on combustible gas controls.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + rule card (0.02 mg/m3 cobalt TLV)

ZONE 2 -- HAZARD GRID / HERO (2.9"--15.5" / ~12.6")
  Block B: 8 hazard cards (4x2 grid)

ZONE 3 -- COBALT EXPOSURE (15.5"--22.0" / ~6.5")
  Block D: Cobalt hazard deep-dive + biological monitoring

ZONE 4 -- PPE CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: Required PPE visual checklist

ZONE 5 -- FUEL GAS SAFETY (28.5"--32.5" / ~4.0")
  Block F: Combustible gas safety banner

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `HVOF -- Supersonic Combustion, Cobalt Fumes, and Fuel Gas Hazards` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `110-130 dB supersonic jet. Combustible fuel gases. Cobalt fume at 0.02 mg/m3 TLV. Respect every hazard or pay the price.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right side of header):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Big number: `0.02` -- Barlow Condensed ExtraBold, 72 pt, `#E05C5C`
- Label: `mg/m3 -- cobalt TLV (ACGIH)` -- Inter Medium, 14 pt, `#F0EDE8`

---

### ZONE 2 -- Hazard Grid (HERO)

**Section label:** `8 HAZARDS YOU MUST CONTROL` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt.

**BLOCK B -- 4x2 Hazard Grid**

Y: 3.8" to 15.3". Cards: W: 5.5", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Gap between cards: 0.33" horizontal, 0.4" vertical.

| Pos | X | Y | Hazard | Details | Controls |
|---|---|---|---|---|---|
| R1C1 | 0.5" | 3.8" | NOISE (110-130 dB) | Supersonic jet; causes permanent hearing damage in minutes of unprotected exposure | Double hearing protection (plugs + muffs); NRR 30+ |
| R1C2 | 6.33" | 3.8" | COMBUSTIBLE GASES | H2, propylene, propane, kerosene vapor -- all explosive/flammable | Gas detection systems; flash-back arrestors on ALL lines; no ignition sources |
| R1C3 | 12.16" | 3.8" | COBALT FUMES | WC-Co is the #1 HVOF feedstock; cobalt causes hard metal lung disease and asthma | LEV with HEPA; P100 RPE minimum; biological monitoring (urine Co < 15 ug/L) |
| R1C4 | 18.0" | 3.8" | HIGH-PRESSURE O2 | Oxygen up to 150 PSI; violently accelerates combustion of oils/grease | Oil-free fittings ONLY; no grease on O2 components; proper regulators |
| R2C1 | 0.5" | 9.7" | THERMAL RADIATION | Intense IR from combustion jet; burns at distance | Heat-reflective PPE; IR-filter face shield |
| R2C2 | 6.33" | 9.7" | KEROSENE HANDLING | Liquid-fuel HVOF systems; flammable liquid | Proper fuel storage; spill containment; fire suppression system |
| R2C3 | 12.16" | 9.7" | UV RADIATION | Less intense than plasma but still significant skin/eye hazard | Safety glasses shade 5-8 minimum; long sleeves |
| R2C4 | 18.0" | 9.7" | DUST EXPLOSION | Fine WC-Co and metal powders are explosive when airborne | Inert atmosphere powder handling; grounding; no open flames near powder |

Interior per card:
- Hazard name: Barlow SemiBold, 18 pt, `#E05C5C`
- Details: Inter Regular, 12 pt, `#F0EDE8`
- Controls: Inter Medium, 12 pt, `#27AE60`
- Controls label: `CONTROL:` Barlow SemiBold, 11 pt, `#27AE60`

---

### ZONE 3 -- Cobalt Exposure Deep-Dive

**Section label:** `COBALT -- THE SILENT HAZARD IN EVERY WC-Co SPRAY` -- Y: 15.7".

**BLOCK D -- Two-Column Cobalt Callout**

Y: 16.3" to 21.8".

**Left -- Exposure Limits and Health Effects (W: 11.5"):**

- Rounded rect, X: 0.5", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#E05C5C` 0.06"

| Metric | Value |
|---|---|
| OSHA PEL (TWA) | 0.1 mg/m3 |
| ACGIH TLV (TWA) | 0.02 mg/m3 |
| Biological Exposure Index | Urine cobalt < 15 ug/L |
| Health effects | Hard metal lung disease (cobalt pneumoconiosis); occupational asthma |
| Onset | Can develop after months to years of exposure; often irreversible |
| Carcinogenicity | IARC Group 2B (possibly carcinogenic -- cobalt with WC) |

Labels: Inter Medium 12 pt `#F0EDE8` at 60%. Values: JetBrains Mono 12 pt `#E05C5C`.

**Right -- Required Controls (W: 11.0"):**

- Rounded rect, X: 12.0", W: 11.5", H: 5.2", fill `#1E2435`, left accent `#27AE60` 0.06"

Title: `MANDATORY CONTROLS FOR WC-Co SPRAYING` -- Barlow SemiBold 16 pt `#27AE60`

Controls (Inter Regular 13 pt, line height 170%):
```
1. Enclosed spray booth with LEV and HEPA filtration
2. Respiratory protection: P100 half-face minimum; PAPR for extended work
3. Medical surveillance program (annual PFTs + urine cobalt)
4. Air monitoring: personal breathing zone samples per OSHA method
5. Housekeeping: wet wipe or HEPA vacuum -- NEVER dry sweep
6. Shower and change facilities -- no contaminated clothing leaves the spray area
```

Bottom note: `The 0.02 mg/m3 TLV is EXTREMELY LOW. For context, that is 50x stricter than the nickel TLV. Achieving compliance requires engineering controls, not just RPE.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 4 -- PPE Checklist

**Section label:** `REQUIRED PPE -- EVERY TIME, NO EXCEPTIONS` -- Y: 22.2".

**BLOCK E -- PPE Visual Checklist**

Y: 22.9" to 28.3". Two columns of PPE items (5 per column).

Each item: Rounded rect, W: 11.0", H: 0.9", fill `#1E2435`, left accent `#27AE60` 0.06".

| PPE Item | Specification |
|---|---|
| Hearing protection | Double protection: plugs + muffs; NRR 30+ |
| Respiratory protection | P100 half-face minimum; PAPR for cobalt work |
| Face shield | IR filter for combustion jet; shade 5-8 minimum |
| Heat-reflective gloves | Rated for radiant heat; leather or aluminized |
| Leather apron | Full-length; protects against spatter and radiant heat |
| Safety boots | Steel toe; metatarsal guard; heat-resistant sole |
| Fire-resistant clothing | Long sleeves; no synthetic fabrics (melts to skin) |
| Safety glasses | With side shields; under face shield |
| Insulated gloves | For electrical work and gas cylinder handling |
| Eye wash station | Within 10 seconds of work area -- OSHA requirement |

Item name: Barlow SemiBold, 14 pt, `#F0EDE8`. Spec: JetBrains Mono 12 pt, `#F0EDE8` at 70%.

Checkbox squares: 0.25" x 0.25", border 2 pt `#27AE60`, no fill.

---

### ZONE 5 -- Fuel Gas Safety Callout

**Section label:** Y: 28.7".

**BLOCK F -- Full-Width Safety Banner**

- Rounded rect, X: 0.5", Y: 29.2", W: 23.0", H: 3.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

**Main text:** Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center

> HVOF USES COMBUSTIBLE FUEL GASES -- TREAT EVERY CONNECTION AS A POTENTIAL LEAK

**Sub-text:** Inter Medium, 16 pt, `#F0EDE8`, Center

> Flash-back arrestors on EVERY fuel and oxygen line. Gas detection system active before, during, and after spray. Hydrogen leak-check with soapy water or electronic sniffer before every shift.

**Bottom line:** Inter Regular, 13 pt, `#E8A020`

> Kerosene-fuel systems: maintain spill containment, proper fuel storage per NFPA 30, and automatic fire suppression in the spray booth.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- HVOF`. Version `v1.0 -- 2026`.

Disclaimer: `Source: OSHA PELs, ACGIH TLVs, ASM Handbook Vol 5A, ITSA best practices. Consult your facility safety officer and applicable regulations.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster must feel urgent. Cobalt is the star hazard -- it is the reason HVOF spray booths need better ventilation than most thermal spray operations. The 0.02 mg/m3 TLV in the rule card should make anyone pause. The combustible gas banner addresses the other unique HVOF risk: you are burning fuel at supersonic velocities in an enclosed booth. Flash-back arrestors are not optional equipment -- they are life-safety devices.

---

*Alaina -- Poster #490 -- Construction Workup v1.0 -- 2026-04-26*
