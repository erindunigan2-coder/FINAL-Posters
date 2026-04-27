---
Project: Plating Posters Inc
Poster Number: 410
Title: "Safety & PPE -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.2)"
Technical Source: CVD safety hazards covering toxic/corrosive precursor gases (TiCl4, SiH4, WF6), hydrogen explosion risk, HCl byproducts, CO generation, high-temperature furnace operations, and exhaust scrubber requirements.
Process Scope: CVD safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #410 -- Construction Workup
## Safety & PPE -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

CVD safety is dominated by chemical hazards that PVD operators never face: hydrogen gas in large volumes (explosive), toxic chloride precursors that fume on contact with air, HCl byproduct gas, CO generation during Al2O3 deposition, and pyrophoric silane (SiH4). Add furnace temperatures of 800-1100 C and you have one of the most hazard-dense coating processes in the industry. This poster is the wall-mounted safety bible.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard cards (Block B -- HERO):** Seven hazard cards (one per major hazard) in a two-row layout. Each card with hazard, source, severity, and PPE requirement.
2. **Gas monitoring requirements (Block C):** Table of gas monitors with alarm setpoints.
3. **Emergency procedures (Block D):** Four emergency scenario cards with immediate actions.
4. **PPE summary strip (Block E):** Visual strip of required PPE items.
5. **Regulatory reference strip (Block F):** OSHA standards applicable to CVD.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 16.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Coral -- safety)
ZONE 3 -- HAZARD CARDS / HERO (4.2"--16.0" / ~11.8")
ZONE 4 -- GAS MONITORING + PPE (16.0"--21.0" / ~5.0")
ZONE 5 -- EMERGENCY PROCEDURES (21.0"--27.0" / ~6.0")
ZONE 6 -- REGULATORY REFERENCES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Toxic Gases, Hydrogen Explosion Risk, HCl Byproducts, High Temperature` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `CVD uses hydrogen at 800-1100 C alongside toxic chloride precursors. Every gas is either explosive, corrosive, toxic, or all three. Know the hazards. Wear the PPE. Monitor continuously.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Safety poster -- all 10 stages shown dimmed with "SAFETY APPLIES TO ALL STAGES" banner. Fill `#E05C5C`, text `#1A1F2E`.
Below: `This poster covers hazards present throughout the entire CVD process. Post at the furnace control station.`

---

### ZONE 3 -- Hazard Cards (HERO)

**Section label:** `CVD HAZARDS -- KNOW EVERY ONE` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Seven Hazard Cards (Y: 5.0" to 15.8")**

Two rows. Top row: 4 cards. Bottom row: 3 cards.

Each card: Rounded rect W: 5.5", H: 5.0", fill `#1E2435`, radius 6, top accent 4 pt `#E05C5C`.

**Top Row (Y: 5.0" to 10.0"):**

| Card | X | Hazard Title |
|---|---|---|
| 1 | 0.5" | HYDROGEN (H2) EXPLOSION |
| 2 | 6.33" | TOXIC PRECURSORS (TiCl4, AlCl3) |
| 3 | 12.16" | PYROPHORIC SILANE (SiH4) |
| 4 | 18.0" | HCl BYPRODUCT GAS |

**Bottom Row (Y: 10.5" to 15.5"):**

| Card | X | Hazard Title |
|---|---|---|
| 5 | 0.5" | CARBON MONOXIDE (CO) |
| 6 | 6.33" | HIGH TEMPERATURE (800-1100 C) |
| 7 | 12.16" | COMPRESSED GAS CYLINDERS |

**Interior per card:**

*Card 1 -- Hydrogen Explosion:*
- Hazard: Barlow SemiBold 16 pt `#E05C5C`
- `HYDROGEN (H2) EXPLOSION`
- Source: Inter Regular 13 pt `#F0EDE8`
- `Carrier/reducing gas used at 10-100 L/min. LEL 4%, UEL 75%. Invisible flame.`
- Severity: Inter Medium 13 pt `#E8A020`
- `Explosion or detonation in confined space. Burns with invisible flame.`
- PPE/Control: Inter Medium 13 pt `#2EC4B6`
- `H2 detector alarm at 10% LEL (0.4% H2). No ignition sources. Auto-shutoff valves. Never open furnace without purging H2 first.`

*Card 2 -- Toxic Precursors:*
- `TOXIC PRECURSORS (TiCl4, AlCl3)`
- `TiCl4 fumes in moist air producing TiO2 + HCl. AlCl3 sublimes and reacts similarly. WF6 produces HF.`
- `Inhalation: pulmonary edema. Contact: severe chemical burns. WF6/HF: bone-seeking fluoride toxicity.`
- `Full-face respirator with acid gas cartridge or supplied air. Chemical-resistant gloves (butyl rubber or Viton). Eye protection.`

*Card 3 -- Pyrophoric Silane:*
- `PYROPHORIC SILANE (SiH4)`
- `SiH4 ignites spontaneously in air. Used in SiC and Si3N4 CVD.`
- `Spontaneous fire. Explosion if accumulated in enclosed space.`
- `Gas cabinet with auto-shutoff. If leaking: evacuate, do NOT attempt to extinguish -- let burn if isolated. Shut off supply remotely.`

*Card 4 -- HCl Byproduct:*
- `HCl BYPRODUCT GAS`
- `Product of all TiCl4 and AlCl3 reactions. Continuous generation during deposition.`
- `Corrosive to lungs and eyes. OSHA PEL: 5 ppm ceiling. Corrodes equipment.`
- `Exhaust scrubber (water) mandatory. HCl monitor alarm at 2 ppm. Acid-gas respirator for maintenance.`

*Card 5 -- Carbon Monoxide:*
- `CARBON MONOXIDE (CO)`
- `Byproduct of Al2O3 deposition: CO2 + H2 -> CO + H2O at process temp.`
- `Toxic: OSHA PEL 50 ppm TWA. Odorless, colorless.`
- `CO monitor alarm at 35 ppm. Ensure adequate ventilation. Supplied air for furnace maintenance.`

*Card 6 -- High Temperature:*
- `HIGH TEMPERATURE (800-1100 C)`
- `Furnace interior and external surfaces. Retort, trays, fixtures.`
- `Severe burns. Ignition of flammable materials near furnace.`
- `Fire-resistant clothing (Nomex). Heat-resistant gloves (rated > 250 C). Face shield. IR thermometer before handling.`

*Card 7 -- Compressed Gas:*
- `COMPRESSED GAS CYLINDERS`
- `Multiple gas types (H2, Ar, N2, CO2, CH4) at 2000-2500 psi.`
- `Cylinder projectile. Asphyxiation (inert gases). Fire (H2, CH4).`
- `Secure cylinders upright. Segregate oxidizers from flammables. Use flash arrestors on H2 lines. Gas cabinets for toxic gases.`

---

### ZONE 4 -- Gas Monitoring + PPE

**Two-column layout (Y: 16.0" to 20.8"):**

**Left -- Gas Monitoring Table (X: 0.5", W: 11.0"):**

**Section label:** `CONTINUOUS GAS MONITORING` -- Y: 16.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

| Gas | Sensor Type | Alarm Setpoint | OSHA Limit |
|---|---|---|---|
| H2 | Catalytic bead / electrochemical | 10% LEL (0.4% v/v) | N/A (fire/explosion) |
| HCl | Electrochemical | 2 ppm | 5 ppm ceiling |
| CO | Electrochemical | 35 ppm | 50 ppm TWA |
| O2 (deficiency) | Electrochemical | < 19.5% | 19.5% min |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 12 pt `#F0EDE8`.

**Right -- PPE Summary (X: 12.0", W: 11.5"):**

**Section label:** `REQUIRED PPE -- CVD OPERATIONS` -- Y: 16.2".

- Rounded rect H: 4.6", fill `#1E2435`, left accent `#E05C5C`

PPE items (Inter Medium 14 pt `#F0EDE8`, with accent-colored bullet indicators):
- `Chemical-resistant apron + gloves (butyl rubber or Viton)` -- `#E05C5C`
- `Full-face respirator w/ acid gas cartridge (or supplied air)` -- `#E05C5C`
- `Fire-resistant clothing (Nomex) near furnace` -- `#E8A020`
- `Safety glasses + face shield for furnace ops` -- `#E8A020`
- `Heat-resistant gloves (Kevlar/silicone, > 250 C)` -- `#E8A020`
- `Steel-toe boots` -- `#2EC4B6`

---

### ZONE 5 -- Emergency Procedures

**Section label:** `EMERGENCY RESPONSE -- 4 SCENARIOS` -- Y: 21.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Four Emergency Cards (Y: 21.8" to 26.8")**

Each card: Rounded rect W: 5.5", H: 4.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Scenario | Immediate Actions |
|---|---|---|---|
| 1 | 0.5" | SiH4 LEAK / FIRE | Evacuate area. SiH4 ignites spontaneously -- do NOT extinguish unless gas can be shut off. Shut off supply remotely. Let burn if isolated. Call fire department. |
| 2 | 6.33" | H2 FIRE | Shut off H2 supply. H2 flame is invisible -- use broom straw or thermal camera to locate. CO2 or dry chemical extinguisher. Never open furnace door during H2 fire. |
| 3 | 12.16" | TiCl4 RELEASE | Dense white fumes (TiO2 + HCl). Evacuate. Use supplied air. Neutralize spill with soda ash or lime. Ventilate. |
| 4 | 18.0" | FURNACE THERMAL RUNAWAY | E-stop. Close all precursor gas valves. Maintain H2 or inert purge -- DO NOT allow air to enter (air + H2 at temperature = explosion). |

Interior per card:
- Scenario: Barlow SemiBold 16 pt `#E05C5C`
- Actions: Inter Medium 13 pt `#F0EDE8`, numbered steps

---

### ZONE 6 -- Regulatory References

**Section label:** `APPLICABLE REGULATIONS` -- Y: 27.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Regulation Table (Y: 27.8" to 32.3")**

| Regulation | Applies To |
|---|---|
| OSHA 29 CFR 1910.147 | Lockout/Tagout -- all furnace maintenance |
| OSHA 29 CFR 1910.134 | Respiratory protection -- HCl, CO, precursor gas exposure |
| OSHA 29 CFR 1910.101 | Compressed gas storage and handling |
| NFPA 70E | Electrical safety (furnace power systems) |
| NFPA 55 | Compressed gases and cryogenic fluids |
| 40 CFR Part 63 | HAP emissions (HCl) -- scrubber requirements |
| CGA P-1 | Safe handling of compressed gases |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`. Alternating rows.

Bottom callout:
- `All CVD exhaust must be scrubbed. Water scrubbers neutralize HCl. Particulate filters capture unreacted precursors. Non-compliance is an EPA/OSHA violation.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 7 -- Footer

Standard footer. Title: `Safety & PPE -- CVD`. Version `v1.0 -- 2026`.

**Disclaimer:** `This poster is an educational reference tool. Safety requirements and PPE specifications shown are general industry guidance. Consult your facility safety officer, equipment SDS/MSDS, and applicable OSHA/EPA regulations for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

CVD safety is significantly more complex than PVD due to the chemical hazards. The seven hazard cards are the hero because every operator must internalize each hazard before working near the furnace. Hydrogen explosion risk is the #1 concern -- it's used in massive volumes and is explosive across nearly its entire concentration range (4-75%). The emergency procedures section is critical because CVD emergencies (SiH4 fire, TiCl4 release, furnace runaway) require very specific responses that differ from standard fire/chemical protocols.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #410 -- Construction Workup v1.0*
*2026-04-26*
