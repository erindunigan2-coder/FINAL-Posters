---
Project: Plating Posters Inc
Poster Number: 450
Title: "Safety & PPE -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Section 6.2)"
Process Scope: Safety hazards, PPE requirements, and emergency procedures for ion implantation
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #450 -- Construction Workup
## Safety & PPE -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Ion implantation is among the most dangerous equipment in a semiconductor fab. This poster does not mince words. Accelerating voltages up to 10 MV. Arsine gas with an IDLH of 3 ppm. X-ray radiation from bremsstrahlung. Potential neutron activation at MeV energies. This is a poster that could save a life. The hero is a hazard severity matrix, followed by PPE requirements, toxic gas monitoring protocols, and the arsine emergency response procedure. Every element is designed for maximum visibility and clarity.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Hazard severity matrix hero (Block B):** Five hazard rows ranked by severity with color-coded indicators.
2. **PPE and controls panel (Block D):** Required safety equipment and engineering controls.
3. **Toxic gas monitoring (Block E):** AsH3, PH3, BF3 alarm setpoints and response.
4. **Arsine emergency protocol (Block F):** Step-by-step emergency response -- the most critical panel.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 13.5" / 19.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- HAZARD SEVERITY MATRIX HERO (2.9"--13.5" / ~10.6")
  Block B: 5 hazard categories with severity and source detail
ZONE 3 -- PPE & ENGINEERING CONTROLS (13.5"--19.5" / ~6.0")
  Block D: Required equipment and systems
ZONE 4 -- TOXIC GAS MONITORING (19.5"--26.0" / ~6.5")
  Block E: Gas species, alarm levels, and response actions
ZONE 5 -- ARSINE EMERGENCY PROTOCOL (26.0"--32.5" / ~6.5")
  Block F: Step-by-step AsH3 response
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Lethal Hazards Require Absolute Discipline` -- 36 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Ion implanters combine extreme high voltage, toxic source gases, ionizing radiation, and vacuum -- all in one machine. There is no room for shortcuts.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Hazard Severity Matrix Hero

**Section label:** `HAZARD IDENTIFICATION -- KNOW WHAT CAN KILL YOU` -- Y: 3.1".

**BLOCK B -- Hazard Matrix**

Y: 3.8" to 13.3". Five hazard rows, full width.

Each row: Rounded rect, X: 0.5", W: 23.0", H: 1.7", fill `#1E2435`, left accent 0.08".

| Row | Hazard | Accent | Source | Severity | OSHA Reference |
|---|---|---|---|---|---|
| 1 | EXTREME HIGH VOLTAGE | `#E05C5C` | Accelerating voltages 10 kV to 10 MV. Stored energy in terminal capacitance. Multiple lethal energy sources in a single machine. | LETHAL -- electrocution. One of the most dangerous machines in a semiconductor fab. | 29 CFR 1910.147 (LOTO); NFPA 70E |
| 2 | TOXIC SOURCE GASES | `#E05C5C` | AsH3 (arsine): PEL 0.05 ppm, IDLH 3 ppm. PH3 (phosphine): PEL 0.3 ppm, IDLH 50 ppm. BF3: PEL 1 ppm ceiling. | LETHAL -- AsH3 causes massive hemolysis. Colorless. May be fatal before symptoms appear. | 29 CFR 1910.1018; 29 CFR 1910.134 |
| 3 | X-RAY RADIATION | `#E8A020` | Bremsstrahlung generated when energetic ions/electrons strike metal surfaces inside the implanter. | Radiation exposure -- chronic or acute. Systems require lead shielding and interlocked access. | 10 CFR 20; state radiation regulations |
| 4 | ACTIVATED MATERIALS | `#E8A020` | At MeV energies, neutron activation of chamber components is possible. Residual radioactivity. | Radiation survey required after high-energy implants. Monitor exposure with TLD badges. | 10 CFR 20; facility radiation safety program |
| 5 | VACUUM / MECHANICAL | `#2EC4B6` | Large vacuum chambers under atmospheric pressure differential. Heavy wafer handling stages. Cryopumps at 10--20 K. | Standard vacuum hazards: implosion, pinch points, cryogenic burns. | 29 CFR 1910.147; general machine guarding |

Layout per row:
- Hazard: Barlow SemiBold, 18 pt, accent color. Left side, X: 1.0".
- Source: Inter Regular, 13 pt, `#F0EDE8`. Center block.
- Severity: Inter Medium, 13 pt, accent color. Right side.
- OSHA Ref: JetBrains Mono, 10 pt, `#F0EDE8` at 50%. Bottom-right.

---

### ZONE 3 -- PPE & Engineering Controls

**Section label:** `REQUIRED PROTECTION -- NO EXCEPTIONS` -- Y: 13.7".

**BLOCK D -- PPE and Controls**

Y: 14.3" to 19.3". Two-column layout.

**Left -- Personal Protective Equipment (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `PERSONAL PROTECTION` -- Barlow SemiBold, 18 pt, `#E05C5C`

| Item | Specification |
|---|---|
| TLD badge | Thermoluminescent dosimeter; worn at all times in implant bay |
| Toxic gas monitor (personal) | Continuous AsH3/PH3 detector clipped to collar |
| Safety glasses | Side shields; required in implant bay at all times |
| ESD wrist strap | Grounded; semiconductor wafer handling |
| Cleanroom garments | Bunny suit, gloves, booties (fab environment) |
| Emergency SCBA | Self-contained breathing apparatus available within 30 seconds |

**Right -- Engineering Controls (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ENGINEERING CONTROLS` -- Barlow SemiBold, 18 pt, `#E8A020`

| Control | Function |
|---|---|
| Multi-level interlocks | Personnel access doors interlock beam-off and HV discharge |
| High-voltage discharge verification | Grounding hooks confirmed before any maintenance entry |
| Gas cabinets | All toxic gases in exhausted, alarmed, auto-shutoff cabinets |
| Area radiation monitors | Continuous monitoring; alarm if X-ray levels exceed limits |
| Continuous toxic gas monitors | AsH3 alarm at 0.005 ppm (10% of PEL); PH3 alarm at 0.03 ppm |
| Emergency ventilation | Push-button or automatic high-volume exhaust activation |

Data: Inter Regular, 13 pt, `#F0EDE8`. Specification: JetBrains Mono 12 pt `#F0EDE8`.

---

### ZONE 4 -- Toxic Gas Monitoring

**Section label:** `TOXIC GAS MONITORING -- ALARM SETPOINTS` -- Y: 19.7".

**BLOCK E -- Gas Monitoring Table**

Y: 20.3" to 25.8".

Rounded rect container, X: 0.5", W: 23.0", H: 5.3", fill `#1E2435`.

| Gas | Formula | OSHA PEL | IDLH | Alarm Level 1 | Alarm Level 2 | Emergency Response |
|---|---|---|---|---|---|---|
| Arsine | AsH3 | 0.05 ppm TWA | 3 ppm | 0.005 ppm (investigate) | 0.05 ppm (evacuate) | Evacuate; SCBA; ventilate; medical eval for ANY exposure |
| Phosphine | PH3 | 0.3 ppm TWA | 50 ppm | 0.03 ppm (investigate) | 0.3 ppm (evacuate) | Evacuate; SCBA; ventilate; medical eval |
| Boron trifluoride | BF3 | 1 ppm ceiling | 25 ppm | 0.1 ppm (investigate) | 1 ppm (evacuate) | Evacuate; ventilate; respiratory protection |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Gas name: Inter Medium, 14 pt, `#F0EDE8`.
PEL/IDLH: JetBrains Mono 13 pt `#E05C5C`.
Alarm levels: JetBrains Mono 12 pt. Level 1: `#E8A020`. Level 2: `#E05C5C`.

**Critical note (Y: 25.0"):**
- `Arsine is colorless and nearly odorless. You CANNOT detect a lethal exposure with your senses. Continuous electronic monitoring is the only protection.` -- Inter Medium, 14 pt, `#E05C5C`.

---

### ZONE 5 -- Arsine Emergency Protocol

**Section label:** `ARSINE EXPOSURE -- EMERGENCY RESPONSE` -- Y: 26.2". Color: `#E05C5C`.

**BLOCK F -- Step-by-Step Protocol**

Y: 26.8" to 32.3".

Full-width panel, fill `#E05C5C` at 10%, border 2 pt `#E05C5C`, radius 6.

**Six numbered steps in vertical sequence:**

| Step | Action | Detail |
|---|---|---|
| 1 | EVACUATE IMMEDIATELY | Leave the implant bay. Activate emergency alarm. Do NOT re-enter. |
| 2 | DON SCBA | If rescue is needed, only SCBA-equipped personnel may enter. NO air-purifying respirators for arsine. |
| 3 | SHUT DOWN SOURCE | Remote E-stop if available. Gas cabinet auto-shutoff should activate on alarm. |
| 4 | VENTILATE | Emergency exhaust system engaged. Do not re-enter until gas monitors read ZERO. |
| 5 | ADMINISTER OXYGEN | Exposed personnel: 100% O2 via mask. Arsine causes hemolysis -- O2 supports remaining RBCs. |
| 6 | HOSPITAL TRANSPORT | ANY suspected arsine exposure warrants immediate hospital transport. Symptoms may be delayed 2--24 hours. Blood work: haptoglobin, free hemoglobin, urinalysis for hemoglobinuria. |

Step number: Barlow Condensed ExtraBold, 24 pt, `#E05C5C`, in circle badge (radius 0.3", fill `#1E2435`, border 2 pt `#E05C5C`).
Action: Barlow SemiBold, 16 pt, `#E05C5C`.
Detail: Inter Regular, 13 pt, `#F0EDE8`.

**Bottom warning:**
- `Arsine causes massive destruction of red blood cells (hemolysis). Symptoms (dark urine, jaundice, abdominal pain) may not appear for 2--24 hours after exposure. The threshold for medical evaluation is ANY detectable exposure above 0.01 ppm.` -- Inter Medium, 13 pt, `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Ion Implantation`. Version `v1.0 -- 2026`.

Footer disclaimer:

> This poster is an educational reference tool and does NOT replace your facility's safety program, standard operating procedures, or emergency response plan. Ion implantation safety requirements vary by implanter type, facility, and jurisdiction. Consult your EHS department, implanter manufacturer documentation, and applicable OSHA/state/local regulations.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety and PPE Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is a life-safety poster. Design choices must prioritize instant readability and severity communication. The Coral red is used more heavily here than in any other poster in the series -- because the hazards warrant it. The arsine emergency protocol (Zone 5) is the single most important panel. It should be visually distinct from everything else -- the `#E05C5C` at 10% background tint with a 2 pt border makes it impossible to miss. The toxic gas monitoring table gives operators the exact alarm setpoints they need to memorize. This poster should hang within line of sight of every ion implanter.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #450 -- Construction Workup v1.0*
*2026-04-26*
