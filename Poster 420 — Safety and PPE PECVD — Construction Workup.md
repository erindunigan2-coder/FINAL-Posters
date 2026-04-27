---
Project: Plating Posters Inc
Poster Number: 420
Title: "Safety & PPE -- PECVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 3: PECVD, Section 3.8)"
Technical Source: PECVD safety hazards including pyrophoric silane (SiH4), RF radiation, toxic/flammable process gases, vacuum implosion, and ozone generation. SiH4 is the #1 hazard -- spontaneous ignition in air.
Process Scope: PECVD safety protocols, PPE requirements, gas hazard management
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PECVD
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #420 -- Construction Workup
## Safety & PPE -- PECVD

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

This is the safety poster for the PECVD cluster. Silane (SiH4) is pyrophoric -- it ignites spontaneously on contact with air. That fact dominates this poster. Every other hazard (RF radiation, vacuum implosion, NH3 toxicity, C2H2 flammability, ozone) is real but secondary. The rule card stat is the silane IDLH: 50 ppm.

Design philosophy: Coral-dominant poster. Large pyrophoric hazard callout as hero. PPE grid. Gas hazard table. Emergency response strip. This poster should make someone stop and think before they open a gas cabinet.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Pyrophoric gas hero callout (Block B -- HERO):** Large coral-tinted glass panel with silane warning. Triangle-warning icon. Bold imperatives.
2. **PPE grid (Block C):** 6 PPE items in a 3x2 grid with icon placeholders and descriptions.
3. **Gas hazard table (Block D):** 7-row table listing each PECVD gas with hazard type, PEL/LEL, and controls.
4. **Emergency response strip (Block E):** 4-card strip -- silane leak, fire, vacuum failure, chemical exposure.
5. **Interlock checklist (Block F):** Required safety interlocks before system operation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 10.5" / 16.0" / 22.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + rule card (IDLH 50 ppm)

ZONE 2 -- PYROPHORIC GAS HERO (2.9"--10.5" / ~7.6")
  Block B: Silane (SiH4) pyrophoric hazard callout -- THE dominant visual

ZONE 3 -- PPE REQUIREMENTS (10.5"--16.0" / ~5.5")
  Block C: 3x2 PPE grid

ZONE 4 -- GAS HAZARD TABLE (16.0"--22.5" / ~6.5")
  Block D: 7-row gas hazard reference table

ZONE 5 -- EMERGENCY RESPONSE + INTERLOCKS (22.5"--32.5" / ~10.0")
  Block E: 4-card emergency response strip
  Block F: Interlock checklist

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Plasma-Enhanced CVD (PECVD) -- Hazard Awareness` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `Silane ignites in air. That sentence should change how you approach every gas connection in this facility.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card (top right):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#1E2435`, border 1 pt `#E05C5C`
- Coral tint glass
- Big number: `50 ppm` -- Barlow Condensed ExtraBold, 64 pt, `#E05C5C`
- Label: `SiH4 IDLH` -- JetBrains Mono Regular, 14 pt, `#F0EDE8` at 70%
- Sub-label: `Immediately Dangerous to Life or Health` -- Inter Regular, 12 pt, `#F0EDE8` at 50%

---

### ZONE 2 -- Pyrophoric Gas Hero

**Section label:** `THE #1 HAZARD: PYROPHORIC SILANE` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#E05C5C`.

**BLOCK B -- Silane Warning Panel**

Y: 3.8" to 10.3". Full width within margins.

Main panel: Rounded rect, X: 0.5", Y: 3.8", W: 23.0", H: 6.0", fill `#1E2435`, left accent 0.08" `#E05C5C`.

**Left column (X: 1.5", W: 10.0"):**

Warning header:
- Barlow Condensed ExtraBold, 36 pt, `#E05C5C`
- Text: `SILANE (SiH4) -- PYROPHORIC`

Definition:
- Inter Medium, 16 pt, `#F0EDE8`
- Text: `Pyrophoric = ignites spontaneously on contact with air. No spark needed. No ignition source needed. Just air.`

Key facts (JetBrains Mono Regular, 14 pt, `#F0EDE8`, line height 180%):
```
Auto-ignition: SPONTANEOUS IN AIR
IDLH: 50 ppm
LEL: 1.4% in air
Odor: repulsive (like silicone)
Density: heavier than air (pools in low areas)
```

Imperative (Inter Medium, 14 pt, `#E05C5C`):
> Never open a silane cylinder or gas cabinet without verifying N2 purge, leak detection, and fire suppression are active.

**Right column (X: 12.5", W: 10.5"):**

Required controls (Barlow SemiBold, 18 pt, `#F0EDE8`):
`MANDATORY CONTROLS`

Checklist (Inter Regular, 14 pt, `#F0EDE8`, line height 170%):
```
[x] Gas cabinet with automatic sprinkler
[x] Double-contained gas lines (coaxial tubing)
[x] Continuous LEL monitoring at gas cabinet
[x] Continuous LEL monitoring in chamber area
[x] N2 purge manifold for all connections
[x] Automatic gas shutoff on LEL alarm
[x] Dedicated exhaust ventilation for gas cabinet
[x] Emergency shutoff accessible from 2 locations
```

Bottom bar (Y: 9.3"):
- Rounded rect, W: 22.0", H: 0.6", fill `#E05C5C` at 20%, border 1 pt `#E05C5C`
- Text: `SILANE LEAKS CAN PRODUCE DELAYED IGNITION -- a cloud of SiH4 can accumulate and then detonate. Treat every leak as an emergency.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 3 -- PPE Requirements

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 10.7".

**BLOCK C -- 3x2 PPE Grid**

Y: 11.3" to 15.8". Six cards in two rows of three.

Each card: Rounded rect, W: 7.33", H: 2.0", fill `#1E2435`, radius 6, top accent 3 pt.

| Position | PPE Item | Accent | Icon Desc | When Required |
|---|---|---|---|---|
| R1C1 | Safety Glasses | `#2EC4B6` | Eye icon | All PECVD operations |
| R1C2 | Nitrile Gloves | `#2EC4B6` | Hand icon | Part handling (prevents fingerprint contamination) |
| R1C3 | Hearing Protection | `#E8A020` | Ear icon | Near roughing pumps (70--85 dB) |
| R2C1 | Face Shield | `#E05C5C` | Shield icon | Gas cabinet operations, viewport inspection |
| R2C2 | Chemical Splash Goggles | `#E05C5C` | Goggle icon | NH3 or liquid precursor handling |
| R2C3 | SCBA (Standby) | `#E05C5C` | Mask icon | Emergency response -- SiH4 or NH3 release |

Card interior:
- Icon placeholder: Rounded rect, 0.5" x 0.5", fill accent at 30%
- PPE name: Barlow SemiBold, 16 pt, `#F0EDE8`
- When required: Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 4 -- Gas Hazard Table

**Section label:** `PECVD PROCESS GAS HAZARD REFERENCE` -- Y: 16.2".

**BLOCK D -- 7-Row Table**

Y: 16.8" to 22.3". Column widths:
- Gas (3.0") | Formula (2.0") | Hazard Type (4.0") | PEL / LEL (3.0") | Key Control (11.0")

| Gas | Formula | Hazard Type | PEL / LEL | Key Control |
|---|---|---|---|---|
| Silane | SiH4 | PYROPHORIC + toxic | IDLH 50 ppm | Double-contained lines; LEL detector; gas cabinet sprinkler |
| Ammonia | NH3 | Toxic + corrosive | PEL 50 ppm; IDLH 300 ppm | Local exhaust; gas detector; emergency shower |
| Nitrous oxide | N2O | Oxidizer | No PEL established | Never mix with fuel gases; supports combustion |
| Acetylene | C2H2 | Flammable/explosive | LEL 2.5% | Never compress > 15 psig; flash arrestors on lines |
| HMDSO | C6H18OSi2 | Flammable liquid | Flash point -1 degC | Vapor heavier than air; ground all containers |
| Argon | Ar | Asphyxiant | -- | O2 monitor in enclosed areas; ventilation |
| Ozone (byproduct) | O3 | Toxic oxidizer | PEL 0.1 ppm; IDLH 5 ppm | Forms in some plasma configs; exhaust ventilation |

Header row: `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.
Hazard type for SiH4: `#E05C5C` (Coral, bold). Other hazard types: Inter Medium `#F0EDE8`.
PEL/LEL values: JetBrains Mono Regular, 12 pt.

---

### ZONE 5 -- Emergency Response + Interlocks

**Section label:** `EMERGENCY RESPONSE` -- Y: 22.7".

**BLOCK E -- 4-Card Emergency Strip**

Y: 23.3" to 27.5". Four cards, equal width with 0.33" gap.

Each card: Rounded rect, W: 5.5", H: 4.0", fill `#1E2435`, radius 6, top accent 4 pt `#E05C5C`.

| Card | X | Emergency | Response |
|---|---|---|---|
| 1 | 0.5" | SILANE LEAK | Evacuate area. Do NOT attempt to find leak. Activate gas shutoff from remote location. Do NOT create ignition sources. Call emergency response. |
| 2 | 6.33" | FIRE | Activate suppression. Shut off all gas supply at source. Evacuate. If cylinder involved, evacuate 100 ft minimum. |
| 3 | 12.16" | VACUUM FAILURE | Chamber may implode if viewport cracked. Stand clear. Vent slowly through valve -- never rapid vent. |
| 4 | 18.0" | CHEMICAL EXPOSURE | NH3 splash: emergency shower 15 min. SiH4 burn: treat as chemical + thermal burn. Seek immediate medical attention. |

Card interior:
- Emergency type: Barlow Condensed ExtraBold, 18 pt, `#E05C5C`
- Response steps: Inter Regular, 12 pt, `#F0EDE8`, line height 155%

**BLOCK F -- Interlock Checklist**

Y: 28.0" to 32.3".

Section label: `PRE-OPERATION SAFETY INTERLOCK CHECKLIST` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`. Y: 28.2".

Two-column layout:

Left column (X: 0.5", W: 11.0"):
```
[ ] Gas cabinet exhaust flow confirmed
[ ] LEL detector calibrated and reading zero
[ ] N2 purge manifold operational
[ ] Chamber door interlock functional
[ ] RF power interlock tested
[ ] Emergency shutoff buttons tested (both locations)
```

Right column (X: 12.0", W: 11.5"):
```
[ ] Fire suppression system armed
[ ] Exhaust scrubber/abatement running
[ ] O2 monitor in room reading 20.9%
[ ] Communication system operational
[ ] MSDS/SDS sheets accessible at station
[ ] Operator trained on SiH4 emergency procedures
```

Each item: Inter Regular, 14 pt, `#F0EDE8`. Checkbox: rounded rect 0.25" x 0.25", border 1 pt `#3A4055`.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- PECVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Safety protocols shown are representative of PECVD operations. Your facility safety plan, equipment manuals, and local regulations take precedence. Consult your EHS department.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE PECVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most critical poster in the PECVD cluster. Silane is not just another flammable gas -- it is pyrophoric, meaning it requires zero ignition energy. A pinhole leak will catch fire. A large leak can accumulate a cloud that detonates. The poster must communicate this viscerally. Coral dominates. The rule card (50 ppm IDLH) should be the first thing someone reads from 10 feet away.

---

*Alaina -- Poster #420 -- Construction Workup v1.0 -- 2026-04-26*
