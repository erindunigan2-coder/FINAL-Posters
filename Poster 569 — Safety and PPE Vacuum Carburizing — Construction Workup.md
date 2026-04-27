---
Project: Plating Posters Inc
Poster Number: 569
Title: "Safety & PPE -- Vacuum Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 2: Vacuum Carburizing / LPC, Section 2.2)"
Technical Source: Vacuum carburizing safety -- acetylene explosion risk, vacuum chamber implosion, HPGQ pressure release, burn hazards, N2 asphyxiation during maintenance. No CO exposure risk (major safety advantage vs. gas carburizing).
Process Scope: Vacuum carburizing safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - VacuumCarburizing
  - LPC
  - Safety
  - PPE
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #569 -- Construction Workup
## Safety & PPE -- Vacuum Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Safety poster for the Vacuum Carburizing cluster. The hazard profile is fundamentally different from gas carburizing -- no CO exposure, no endothermic atmosphere explosion risk. Instead, the hazards are acetylene handling, vacuum vessel integrity, high-pressure gas quench release, and the ever-present N2 asphyxiation risk during maintenance. This poster makes the distinction clear: LPC is safer in some ways, but introduces its own unique risks.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** Five hazard cards (3+2 layout) -- acetylene, HPGQ pressure, burns, N2 asphyxiation, vacuum vessel.
2. **LPC vs. Gas Safety Comparison (Block C):** Quick callout -- what LPC eliminates vs. what it adds.
3. **PPE requirement strip (Block D):** Six PPE items with descriptions.
4. **Emergency procedures panel (Block E):** Acetylene leak, N2 asphyxiation, burn response.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.0" / 18.5" / 24.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
ZONE 2 -- HAZARD GRID / HERO (2.9"--16.0" / ~13.1")
  Block B: Five hazard cards
ZONE 3 -- SAFETY COMPARISON (16.0"--18.5" / ~2.5")
  Block C: LPC eliminates vs. adds callout
ZONE 4 -- PPE REQUIREMENTS (18.5"--24.0" / ~5.5")
  Block D: Six PPE items
ZONE 5 -- EMERGENCY PROCEDURES (24.0"--32.5" / ~8.5")
  Block E: Three emergency scenario panels
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Vacuum Carburizing (LPC) -- No CO, No Endo -- Different Risks` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `No endothermic gas means no CO poisoning risk -- a genuine safety advantage. But acetylene is explosive, HPGQ vessels are pressurized, and nitrogen displaces oxygen silently. Know what changed and what didn't.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Hazard Grid (HERO)

**Section label:** `FIVE HAZARDS IN VACUUM CARBURIZING` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#E05C5C`.

**BLOCK B -- Hazard Cards**

Row 1 (Y: 3.8", three cards):

**Card 1 -- Acetylene (X: 0.5", W: 7.33", H: 5.5"):**
- Title: `ACETYLENE (C2H2)` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `EXPLOSIVE: LEL 2.5%` JetBrains Mono 24 pt `#E05C5C`
- Details (Inter Regular 13 pt `#F0EDE8`):
```
- Extremely wide flammable range: 2.5--100%
  (can burn in pure acetylene -- no air needed)
- Stored in cylinders with acetone solvent
- NEVER exceed 15 psig line pressure
  (risk of decomposition explosion)
- Heavier than air in cold state
- Acetylene detectors required at floor level
```
- Mitigation (Inter Medium 12 pt `#27AE60`):
  `Dedicated acetylene storage area. Leak detection at all connections. Flash arrestors on supply lines. Never use copper fittings (acetylide formation).`

**Card 2 -- HPGQ Pressure (X: 8.17", W: 7.33", H: 5.5"):**
- Title: `HIGH-PRESSURE GAS QUENCH` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `10--20 BAR RELEASE` JetBrains Mono 24 pt `#E05C5C`
- Details:
```
- HPGQ introduces 10--20 bar (150--300 psi)
  of N2 or He into the vessel
- Blower noise can exceed 90 dB
- Vessel is a pressure vessel during quench
- All interlocks must be verified before
  initiating gas quench cycle
```
- Mitigation:
  `Verify all interlocks before HPGQ. Hearing protection mandatory during quench. Pressure relief valves tested per schedule. Never override safety interlocks.`

**Card 3 -- Burns (X: 15.83", W: 7.67", H: 5.5"):**
- Title: `BURNS & HOT PARTS` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `150--300 F EXIT TEMP` JetBrains Mono 24 pt `#E05C5C`
- Details:
```
- Parts exit at 150--300 F after HPGQ
  (cooler than gas carburizing but still hot)
- Fixtures and chamber walls are hot
- Loading/unloading burns are common
- Hot CFC fixtures can be deceptive
  (dark surfaces radiate less visibly)
```
- Mitigation:
  `Heat-resistant gloves for all loading/unloading. Allow cooling time before handling. Verify part temperature before bare-hand contact.`

Row 2 (Y: 9.7", two cards centered):

**Card 4 -- N2 Asphyxiation (X: 0.5", W: 11.0", H: 5.5"):**
- Title: `NITROGEN ASPHYXIATION` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `SILENT KILLER -- NO WARNING` JetBrains Mono 20 pt `#E05C5C`
- Details:
```
- N2 used for HPGQ and backfill is an
  asphyxiant -- displaces oxygen silently
- No odor, no color, no irritation
- O2 below 19.5% = oxygen-deficient
- O2 below 16% = loss of consciousness
- O2 below 10% = death within minutes
- Vacuum chamber maintenance is CONFINED
  SPACE entry -- residual N2 fills the vessel
```
- Mitigation:
  `Continuous O2 monitoring in furnace area. Confined space entry permit for ALL chamber maintenance. Never enter a vacuum vessel without verified O2 > 20.9%. Buddy system mandatory.`

**Card 5 -- Vacuum Vessel Integrity (X: 12.0", W: 11.5", H: 5.5"):**
- Title: `VACUUM VESSEL INTEGRITY` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `IMPLOSION / PRESSURE RISK` JetBrains Mono 18 pt `#E05C5C`
- Details:
```
- Thick-walled vessel designed for
  external atmospheric pressure (vacuum)
  AND internal HPGQ pressure (10--20 bar)
- Viewports and seals are potential
  failure points
- Thermal cycling fatigues vessel walls
- Regular inspection per ASME pressure
  vessel code
```
- Mitigation:
  `Inspect viewports and door seals at every maintenance interval. Hydrostatic testing per code. Replace O-rings and gaskets on schedule. Log thermal cycles for fatigue tracking.`

---

### ZONE 3 -- Safety Comparison

**BLOCK C -- Full-width callout (Y: 16.0" to 18.3")**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, H: 2.1".

Title: `WHAT LPC ELIMINATES vs. WHAT LPC ADDS` Barlow SemiBold 16 pt `#2EC4B6`

Two-column layout inside:

*Left -- ELIMINATED (Emerald `#27AE60`):*
```
- CO exposure (OSHA PEL 50 ppm)
- H2 explosion from endo gas
- Atmosphere explosion on purge failure
- Quench oil fire (if HPGQ path used)
- Continuous CO monitoring requirement
```

*Right -- ADDED (Amber `#E8A020`):*
```
- Acetylene handling and storage
- HPGQ high-pressure vessel operation
- N2 asphyxiation risk (backfill/quench)
- Vacuum vessel inspection requirements
- Hearing protection during HPGQ cycle
```

---

### ZONE 4 -- PPE Requirements

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 18.7". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- PPE Strip (Y: 19.3" to 23.8")**

Six PPE item cards in a 3x2 layout. Each: Rounded rect W: 7.33", H: 2.0", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

| Position | PPE Item | Details |
|---|---|---|
| R1C1 | HEAT-RESISTANT GLOVES | For loading/unloading; parts at 150--300 F after HPGQ |
| R1C2 | HEARING PROTECTION | Mandatory during HPGQ cycle; blower noise >90 dB |
| R1C3 | SAFETY GLASSES | Standard requirement for all furnace area operations |
| R2C1 | STEEL-TOE BOOTS | Dropped fixtures, heavy CFC trays |
| R2C2 | O2 PERSONAL MONITOR | Clip-on O2 detector; alarm at 19.5%; mandatory in furnace area |
| R2C3 | SCBA (MAINTENANCE) | Self-contained breathing apparatus for confined space entry in vacuum vessel |

Title per card: Barlow SemiBold 16 pt `#2EC4B6`.
Details: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Emergency Procedures

**Section label:** `EMERGENCY RESPONSE -- THREE SCENARIOS` -- Y: 24.2". Barlow Condensed ExtraBold 28 pt `#E05C5C`.

**BLOCK E -- Three Emergency Panels (Y: 24.9" to 32.3")**

Three side-by-side callout boxes:

| Panel | X | W | Title | Accent |
|---|---|---|---|---|
| Acetylene Leak | 0.5" | 7.33" | `ACETYLENE LEAK` | `#E05C5C` |
| N2 Asphyxiation | 8.17" | 7.33" | `N2 ASPHYXIATION` | `#E05C5C` |
| Burn Injury | 15.83" | 7.67" | `BURN INJURY` | `#E8A020` |

Each: Rounded rect H: 7.2", fill `#1E2435`, left accent 0.06".

*Acetylene Leak:*
```
1. EVACUATE the area immediately
2. Eliminate all ignition sources
3. DO NOT operate electrical switches
   (sparking risk)
4. Close acetylene supply valve at cylinder
   (if safe to approach)
5. Ventilate the area -- open doors/louvers
6. Call fire department
7. Do NOT re-enter until area tested
   and declared safe
```

*N2 Asphyxiation:*
```
1. DO NOT enter the area to rescue
   (you will also collapse)
2. Call 911 immediately
3. Ventilate the area from outside
   (open doors, activate fans)
4. Rescue ONLY with SCBA or supplied air
5. Move victim to fresh air
6. Begin CPR if not breathing
7. Administer O2 if available and trained
8. N2 asphyxiation can cause brain damage
   in minutes -- TIME IS CRITICAL
```

*Burn Injury:*
```
1. Remove from heat source
2. Cool burn with clean running water (20 min)
3. Do NOT remove clothing stuck to burn
4. Cover with sterile dressing
5. Call 911 for burns > palm size or on
   face/hands/joints
6. CFC fixture burns may appear minor
   but can be deep due to sustained contact
   -- seek medical evaluation
```

Steps: Inter Regular 13 pt `#F0EDE8`. Numbers: JetBrains Mono 13 pt in accent color.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Vacuum Carburizing (LPC)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. It does not replace your facility's safety program, SOPs, or regulatory requirements. Consult OSHA 29 CFR 1910, NFPA 86 (Industrial Furnaces), ASME pressure vessel code, and your EHS department.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Vacuum Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster deliberately contrasts with the gas carburizing safety poster (#560). The CO and endo explosion hazards are gone -- and that elimination deserves celebration (Zone 3 callout). But the replacement hazards (acetylene, N2 asphyxiation, HPGQ pressure) are equally serious and less familiar to operators transitioning from atmosphere furnaces. The N2 asphyxiation card is the most critical content -- nitrogen is a silent killer and the "do not enter to rescue" rule saves lives.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #569 -- Construction Workup v1.0*
*2026-04-26*
