---
Project: Plating Posters Inc
Poster Number: 560
Title: "Safety & PPE -- Carburizing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion & Heat Treatment Clusters -- Watson Research Brief (Process 1: Gas Carburizing, Section 1.11)"
Technical Source: Gas carburizing safety hazards -- CO toxicity, H2 explosion risk, quench oil fire, radiant burns, atmosphere explosion on purge failure. Values from OSHA PELs, NIOSH RELs, and industry best practice.
Process Scope: Gas carburizing safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - GasCarburizing
  - Safety
  - PPE
  - ConstructionWorkup
  - DiffusionHT
---

# Poster #560 -- Construction Workup
## Safety & PPE -- Carburizing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the safety poster for the Gas Carburizing cluster. It goes next to the furnace door. No ambiguity, no fine print -- if you work near a carburizing furnace, this poster tells you what can kill you and how to prevent it. Coral-dominant poster because every section is a warning.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** Six hazard cards in a 3x2 grid -- each card covers one major hazard with details and mitigation. Coral-tinted glass throughout.
2. **PPE requirement strip (Block D):** Horizontal strip showing required PPE items with descriptions.
3. **Emergency procedures panel (Block E):** What to do in CO exposure, oil fire, and burn scenarios.
4. **Exposure limits table (Block F):** OSHA/NIOSH limits for CO and H2.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- HAZARD GRID / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: 3x2 hazard card grid (6 hazards)

ZONE 3 -- PPE REQUIREMENTS (16.0"--22.0" / ~6.0" tall)
  Block D: PPE strip with 6 items

ZONE 4 -- EMERGENCY PROCEDURES (22.0"--28.5" / ~6.5" tall)
  Block E: Three emergency scenario panels

ZONE 5 -- EXPOSURE LIMITS (28.5"--32.5" / ~4.0" tall)
  Block F: CO and H2 exposure limits table + key gas properties

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Gas Carburizing -- Endothermic Atmosphere Furnace Operations` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `20% CO. 40% H2. 1700 F. Quench oil. This is not a forgiving environment. Know the hazards. Wear the gear. Go home safe.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Hazard Grid (HERO)

**Section label:** `SIX HAZARDS THAT CAN KILL YOU` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#E05C5C`.

**BLOCK B -- 3x2 Hazard Grid**

Y: 3.8" to 15.8". Each card: Rounded rect W: 7.33", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Row 1 (Y: 3.8"):

**Card 1 -- Carbon Monoxide (X: 0.5"):**
- Hazard title: `CARBON MONOXIDE (CO)` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `20% of endo gas` JetBrains Mono 28 pt `#E05C5C`
- Details (Inter Regular 13 pt `#F0EDE8`):
```
- Colorless, odorless -- you cannot detect it
- IDLH: 1,200 ppm (immediately dangerous)
- OSHA PEL: 50 ppm (8-hr TWA)
- NIOSH REL: 35 ppm (8-hr TWA)
- Lethal at 12,800 ppm (1.28%) in minutes
```
- Mitigation (Inter Medium 12 pt `#27AE60`):
  `CO monitors at every furnace door. Flame curtains burn off effluent. Never stand in front of an open furnace door.`

**Card 2 -- Hydrogen (X: 8.17"):**
- Hazard title: `HYDROGEN (H2)` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `40% of endo gas` JetBrains Mono 28 pt `#E05C5C`
- Details:
```
- Explosive range: 4--75% in air
- Extremely wide flammability range
- Burns with invisible flame
- Lighter than air -- accumulates at ceiling
```
- Mitigation:
  `Burn-off pilots at furnace doors. Adequate ventilation above furnace. Never extinguish the pilot flame while endo gas is flowing.`

**Card 3 -- Atmosphere Explosion (X: 15.83"):**
- Hazard title: `ATMOSPHERE EXPLOSION` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `PURGE FAILURE = FIREBALL` JetBrains Mono 20 pt `#E05C5C`
- Details:
```
- Endo gas is explosive mixed with air
- Most dangerous moment: furnace startup
- N2 purge before endo gas introduction
- Minimum 5 volume changes required
- Burn-off pilot MUST be lit first
```
- Mitigation:
  `Follow lockout purge procedure exactly. Never skip volume changes. Verify O2 < 1% before introducing endo gas.`

Row 2 (Y: 9.7"):

**Card 4 -- Quench Oil Fire (X: 0.5"):**
- Hazard title: `QUENCH OIL FIRE` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `1500 F parts + oil` JetBrains Mono 28 pt `#E05C5C`
- Details:
```
- Parts enter oil at 1500+ F
- Oil flash point must be monitored
- Loss of agitation = localized overheating
- Degraded oil = lower flash point
```
- Mitigation:
  `Maintain oil below flash point. CO2 or foam suppression over quench tank. Regular oil analysis (flash point, viscosity, water content).`

**Card 5 -- Burns / Radiant Heat (X: 8.17"):**
- Hazard title: `BURNS & RADIANT HEAT` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `1700 F+` JetBrains Mono 28 pt `#E05C5C`
- Details:
```
- Parts and fixtures at 1500+ F
- Radiant heat from open furnace doors
- Contact burns from hot fixtures
- Heat stress in furnace area
```
- Mitigation:
  `Full face shield. Aluminized heat suit components. Heat-resistant gloves. Never reach into furnace. Hydration and rest breaks.`

**Card 6 -- Confined Space (X: 15.83"):**
- Hazard title: `CONFINED SPACE` Barlow SemiBold 18 pt `#E05C5C`
- Stat: `PIT FURNACES + QUENCH TANKS` JetBrains Mono 18 pt `#E05C5C`
- Details:
```
- Pit-type furnaces are confined spaces
- Quench tanks during maintenance
- Residual CO/H2 after shutdown
- O2 displacement by nitrogen
```
- Mitigation:
  `Lockout/tagout. Confined space entry permit. Continuous atmospheric monitoring. Buddy system -- never enter alone.`

---

### ZONE 3 -- PPE Requirements

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 16.2". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK D -- PPE Strip (Y: 16.9" to 21.8")**

Six PPE item cards in a 3x2 layout. Each: Rounded rect W: 7.33", H: 2.2", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

| Position | PPE Item | Details |
|---|---|---|
| R1C1 (X: 0.5") | FACE SHIELD | Full face shield for furnace door operations; protects against radiant heat and flash |
| R1C2 (X: 8.17") | HEAT-RESISTANT GLOVES | High-temp gloves rated for 1500+ F contact; leather or aluminized |
| R1C3 (X: 15.83") | ALUMINIZED HEAT SUIT | Aluminized jacket/apron/leggings for radiant heat protection at furnace front |
| R2C1 (X: 0.5") | SAFETY GLASSES | Under face shield at all times; side shields required |
| R2C2 (X: 8.17") | STEEL-TOE BOOTS | Dropped fixtures and parts; oil-resistant soles for quench area |
| R2C3 (X: 15.83") | CO PERSONAL MONITOR | Clip-on CO detector; alarm at 35 ppm; mandatory in furnace area |

Title per card: Barlow SemiBold 16 pt `#2EC4B6`.
Details: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- Emergency Procedures

**Section label:** `EMERGENCY RESPONSE -- THREE SCENARIOS` -- Y: 22.2". Barlow Condensed ExtraBold 28 pt `#E05C5C`.

**BLOCK E -- Three Emergency Panels (Y: 22.9" to 28.3")**

Three side-by-side callout boxes:

| Panel | X | W | Title | Accent |
|---|---|---|---|---|
| CO Exposure | 0.5" | 7.33" | `CO EXPOSURE` | `#E05C5C` |
| Quench Oil Fire | 8.17" | 7.33" | `QUENCH OIL FIRE` | `#E8A020` |
| Severe Burn | 15.83" | 7.67" | `SEVERE BURN` | `#E05C5C` |

Each: Rounded rect H: 5.2", fill `#1E2435`, left accent 0.06".

*CO Exposure:*
```
1. Remove victim from area IMMEDIATELY
2. Move to fresh air
3. Call 911 -- report CO exposure
4. Administer O2 if available and trained
5. Do NOT re-enter without SCBA
6. Symptoms: headache, dizziness, confusion,
   cherry-red skin color, collapse
```

*Quench Oil Fire:*
```
1. Activate fire suppression (CO2/foam)
2. DO NOT use water on oil fire
3. Close furnace door if safe to do so
4. Evacuate furnace area
5. Call fire department
6. Never attempt to move burning parts
```

*Severe Burn:*
```
1. Remove from heat source
2. Cool burn with clean running water (20 min)
3. Do NOT remove clothing stuck to burn
4. Cover with sterile dressing
5. Call 911 for burns > palm size or
   on face/hands/joints
6. Treat for shock: elevate legs, keep warm
```

Steps: Inter Regular 13 pt `#F0EDE8`. Numbers: JetBrains Mono 13 pt in accent color.

---

### ZONE 5 -- Exposure Limits

**Section label:** `GAS EXPOSURE LIMITS -- KNOW YOUR NUMBERS` -- Y: 28.7". Barlow Condensed ExtraBold 24 pt `#F0EDE8`.

**BLOCK F -- Exposure Table (Y: 29.4" to 32.3")**

Two side-by-side tables:

*Left -- CO Limits (X: 0.5", W: 11.0"):*

| Standard | Limit | Duration |
|---|---|---|
| OSHA PEL | 50 ppm | 8-hr TWA |
| NIOSH REL | 35 ppm | 8-hr TWA |
| NIOSH Ceiling | 200 ppm | Instantaneous |
| IDLH | 1,200 ppm | Immediately dangerous |

*Right -- Flammable Gas Properties (X: 12.0", W: 11.5"):*

| Gas | LEL | UEL | Endo % |
|---|---|---|---|
| CO | 12.5% | 74% | ~20% |
| H2 | 4% | 75% | ~40% |
| CH4 | 5% | 15% | Enrichment gas |

Bottom callout: `Endothermic gas is BOTH toxic (CO) and explosive (CO + H2). Treat every leak as life-threatening.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Gas Carburizing`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. It does not replace your facility's safety program, SOPs, or regulatory requirements. Consult OSHA 29 CFR 1910, NFPA 86 (Industrial Furnaces), and your EHS department.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Carburizing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is a CORAL-DOMINANT poster. The header subheading, section labels, and the majority of content panels use Coral because the entire poster is about hazards. The PPE section uses Teal as a "positive action" color -- these are the things you DO to stay safe. Emergency procedures split between Coral (danger) and Amber (fire). The overall visual impression should be: this environment demands respect.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #560 -- Construction Workup v1.0*
*2026-04-26*
