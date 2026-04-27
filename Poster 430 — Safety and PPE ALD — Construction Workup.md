---
Project: Plating Posters Inc
Poster Number: 430
Title: "Safety & PPE -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Section 4.2)"
Technical Source: ALD safety hazards including pyrophoric TMA (trimethylaluminum), flammable/toxic metalorganic precursors (TDMAT, TEMAH, DEZ), ozone as oxidant, and standard vacuum/electrical hazards. TMA is the #1 hazard -- ignites spontaneously in air and reacts violently with water.
Process Scope: ALD safety protocols, PPE requirements, precursor hazard management
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ALD
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #430 -- Construction Workup
## Safety & PPE -- ALD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the safety poster for the ALD cluster. TMA (trimethylaluminum) -- the most common ALD precursor -- is pyrophoric. It ignites spontaneously in air AND reacts violently with water. That dual hazard dominates this poster. Other metalorganic precursors (TDMAT, TEMAH, DEZ) range from flammable to pyrophoric. The rule card stat: TMA has no safe exposure at ambient atmosphere.

Design philosophy: Coral-dominant. Large TMA pyrophoric hazard callout as hero. PPE grid. Precursor hazard table. Emergency response strip. This poster should make someone think twice before opening a bubbler.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **TMA pyrophoric hero callout (Block B -- HERO):** Large coral-tinted panel with TMA warning.
2. **PPE grid (Block C):** 6 PPE items in 3x2 grid.
3. **Precursor hazard table (Block D):** 6-row table of ALD precursors with hazard types and controls.
4. **Emergency response strip (Block E):** 4-card strip -- TMA release, fire, ozone exposure, vacuum failure.
5. **Interlock/handling checklist (Block F):** Required safety controls.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + rule card
ZONE 2 -- TMA PYROPHORIC HERO (2.9"--10.5" / ~7.6")
  Block B: TMA hazard callout -- THE dominant visual
ZONE 3 -- PPE REQUIREMENTS (10.5"--16.0" / ~5.5")
  Block C: 3x2 PPE grid
ZONE 4 -- PRECURSOR HAZARD TABLE (16.0"--22.5" / ~6.5")
  Block D: 6-row precursor hazard reference
ZONE 5 -- EMERGENCY RESPONSE + HANDLING (22.5"--32.5" / ~10.0")
  Block E: 4-card emergency response strip
  Block F: Safe handling checklist
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Atomic Layer Deposition (ALD) -- Hazard Awareness` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `TMA ignites in air and reacts violently with water. Every precursor change is a potential ignition event. Respect the chemistry.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#E05C5C`
- Big number: `PYRO` -- Barlow Condensed ExtraBold, 56 pt, `#E05C5C`
- Label: `TMA CLASSIFICATION` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Pyrophoric -- ignites in air, no spark needed` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- TMA Pyrophoric Hero

**Section label:** `THE #1 HAZARD: PYROPHORIC TMA` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

**BLOCK B -- TMA Warning Panel**

Y: 3.8" to 10.3". Full width.
Main panel: Rounded rect, X: 0.5", Y: 3.8", W: 23.0", H: 6.0", fill `#1E2435`, left accent 0.08" `#E05C5C`.

**Left column (X: 1.5", W: 10.0"):**

Warning header: Barlow Condensed ExtraBold, 36 pt, `#E05C5C`
> TRIMETHYLALUMINUM (TMA) -- PYROPHORIC

Definition: Inter Medium, 16 pt, `#F0EDE8`
> Pyrophoric = ignites spontaneously on contact with air. Water-reactive = reacts violently with moisture, producing heat and flammable methane gas. TWO ways to catch fire.

Key facts (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 180%):
```
Formula: Al(CH3)3
Auto-ignition: SPONTANEOUS IN AIR
Water reactivity: VIOLENT (produces CH4 + heat)
Flash point: 17 degC (liquid)
OSHA PEL: 2 mg/m3 (as Al)
State: liquid at room temperature
Vapor pressure: ~10 Torr at 20 degC
```

Imperative (Inter Medium, 14 pt, `#E05C5C`):
> Never open a TMA bubbler or cylinder outside an inert atmosphere glove box. Never use water to fight a TMA fire.

**Right column (X: 12.5", W: 10.5"):**

Required controls: Barlow SemiBold, 18 pt, `#F0EDE8`
> MANDATORY CONTROLS

Checklist (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
[x] Inert atmosphere glove box for cylinder changes
[x] All-metal gas lines (VCR fittings, no polymers)
[x] N2 purge manifold on all connections
[x] Bubbler temperature controlled (+/- 1 degC)
[x] Carrier gas (N2/Ar) flowing whenever bubbler is open
[x] Exhaust ventilation on precursor cabinet
[x] Class D fire extinguisher at station
[x] SCBA available for emergency response
```

Bottom bar (Y: 9.3"):
- Rounded rect, W: 22.0", H: 0.6", fill `#E05C5C` at 20%, border 1 pt `#E05C5C`
- Text: `TMA + AIR = INSTANT FIRE. TMA + WATER = VIOLENT REACTION + METHANE IGNITION. Carry Class D extinguisher and dry sand -- NEVER water.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 3 -- PPE Requirements

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 10.7".

**BLOCK C -- 3x2 PPE Grid**

Y: 11.3" to 15.8". Six cards in two rows of three.
Each card: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, radius 6, top accent 3 pt.

| Position | PPE Item | Accent | When Required |
|---|---|---|---|
| R1C1 | Safety Glasses | `#2EC4B6` | All ALD operations |
| R1C2 | Nitrile Gloves (clean) | `#2EC4B6` | Substrate handling -- prevents contamination |
| R1C3 | Lab Coat | `#2EC4B6` | Standard cleanroom/lab attire |
| R2C1 | Full Face Shield | `#E05C5C` | Precursor cylinder/bubbler changes |
| R2C2 | Flame-Resistant Clothing | `#E05C5C` | TMA or DEZ handling -- pyrophoric precursors |
| R2C3 | SCBA (Standby) | `#E05C5C` | Emergency response -- precursor release |

Card interior:
- PPE name: Barlow SemiBold, 16 pt, `#F0EDE8`
- When required: Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Precursor Hazard Table

**Section label:** `ALD PRECURSOR HAZARD REFERENCE` -- Y: 16.2".

**BLOCK D -- 6-Row Table**

Y: 16.8" to 22.3".
Column widths: Precursor (4.0") | Formula (3.0") | Hazard Type (4.0") | Key Control (12.0")

| Precursor | Formula | Hazard Type | Key Control |
|---|---|---|---|
| TMA (trimethylaluminum) | Al(CH3)3 | PYROPHORIC + water-reactive | Inert glove box; Class D extinguisher; NEVER water |
| TDMAT (tetrakis(dimethylamino)titanium) | Ti(N(CH3)2)4 | Flammable liquid; air-sensitive | N2 blanket; avoid air exposure; standard flammable handling |
| TEMAH (tetrakis(ethylmethylamino)hafnium) | Hf(NEtMe)4 | Flammable; pyrophoric in some conditions | Same as TMA handling; inert atmosphere |
| DEZ (diethylzinc) | Zn(C2H5)2 | PYROPHORIC | Same class as TMA; extremely air-sensitive |
| Water (H2O) | H2O | Non-hazardous alone | KEEP AWAY from TMA/DEZ -- violent reaction |
| Ozone (O3) | O3 | Toxic oxidizer; PEL 0.1 ppm | Ozone generator off when not in use; exhaust ventilation; O3 detector |

Header row: `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.
TMA and DEZ hazard types: `#E05C5C` (Coral, bold).
Data: Inter Regular, 12 pt. Formulas: JetBrains Mono, 12 pt.

---

### ZONE 5 -- Emergency Response + Handling

**Section label:** `EMERGENCY RESPONSE` -- Y: 22.7".

**BLOCK E -- 4-Card Emergency Strip**

Y: 23.3" to 27.5". Four cards, equal width, 0.33" gap.
Each card: Rounded rect, W: 5.5", H: 4.0", fill `#1E2435`, radius 6, top accent 4 pt `#E05C5C`.

| Card | X | Emergency | Response |
|---|---|---|---|
| 1 | 0.5" | TMA / DEZ RELEASE | Evacuate immediately. Dense white Al2O3 (or ZnO) smoke = precursor reacting with air moisture. Do NOT use water. Smother with dry sand or Class D extinguisher. Call HAZMAT. |
| 2 | 6.33" | PRECURSOR FIRE | Class D extinguisher ONLY. Dry sand or vermiculite for small fires. Shut off precursor supply from remote valve. Evacuate 50 ft minimum if cylinder involved. |
| 3 | 12.16" | OZONE EXPOSURE | Move to fresh air immediately. O3 irritates lungs at < 1 ppm. Provide supplemental O2 if breathing difficulty. Seek medical attention. |
| 4 | 18.0" | VACUUM FAILURE | Stand clear of chamber. Vent slowly. If precursor was flowing when vacuum was lost, treat as potential fire/release. Ventilate room. |

Card interior:
- Emergency type: Barlow Condensed ExtraBold, 18 pt, `#E05C5C`
- Response: Inter Regular, 12 pt, `#F0EDE8`, line height 155%

**BLOCK F -- Safe Handling Checklist**

Y: 28.0" to 32.3".
Section label: `PRECURSOR HANDLING -- NON-NEGOTIABLE RULES` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 28.2".

Two-column layout:

Left (X: 0.5", W: 11.0"):
```
[ ] ALL precursor changes done in N2/Ar glove box
[ ] Bubbler connections: VCR metal-to-metal only
[ ] Purge all lines with inert gas before disconnecting
[ ] Carrier gas flowing before opening bubbler valve
[ ] Class D extinguisher within arm's reach
[ ] Waste TMA containers: purge with N2, seal, label PYROPHORIC
```

Right (X: 12.0", W: 11.5"):
```
[ ] O3 generator OFF when not depositing
[ ] O3 detector calibrated and reading zero at rest
[ ] Exhaust ventilation verified on precursor cabinet
[ ] SDS/MSDS for all precursors posted at station
[ ] Spill kit (dry sand, vermiculite) accessible
[ ] Emergency shower and eyewash within 10 seconds
```

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- ALD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Safety protocols shown are representative of ALD operations. Your facility safety plan, equipment manuals, and local regulations take precedence. Consult your EHS department.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

TMA is to ALD what silane is to PECVD -- the dominant safety concern. But TMA adds a twist: it is BOTH pyrophoric AND water-reactive. Water -- the standard co-reactant in ALD -- becomes a fire accelerant if it contacts TMA outside the reactor. This dual hazard must be communicated viscerally. The "NEVER water" message on TMA fires is the single most important safety takeaway.

DEZ (diethylzinc) is equally pyrophoric and deserves the same Coral treatment. The poster groups TMA and DEZ together visually to communicate: "these are the dangerous ones."

---

*Alaina -- Poster #430 -- Construction Workup v1.0 -- 2026-04-26*
