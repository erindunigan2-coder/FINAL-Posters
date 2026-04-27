---
Project: Plating Posters Inc
Poster Number: 614
Title: "Safety & PPE -- Induction Hardening"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 7, Section 7.11)"
Technical Source: Induction hardening safety hazards and PPE requirements. EMF exposure, electrical shock, hot parts, quench splash, and noise hazards. No atmosphere hazards -- a major safety advantage over furnace processes.
Process Scope: Induction hardening -- safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - InductionHardening
  - Safety
  - PPE
  - ConstructionWorkup
  - ClusterHT07
---

# Poster #614 -- Construction Workup
## Safety & PPE -- Induction Hardening

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The safety poster for the induction hardening cluster. Induction is unique among heat treatment processes -- no flammable atmospheres, no toxic gases, no open flames. But it introduces hazards that furnace operators may not expect: strong electromagnetic fields, high-frequency electrical shock risk, and magnetostrictive noise. The EMF warning for pacemaker wearers is the most critical safety callout on this poster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** Six hazard cards in a 3x2 grid. Each card has an SVG icon placeholder, hazard name, details, and mitigation. Standard glass card construction.
2. **PPE checklist (Block D):** Visual checklist of required PPE items with descriptions.
3. **"No Atmosphere Hazards" highlight (Block E):** A positive-safety callout -- induction's major safety advantage over furnace processes.
4. **Emergency procedures strip (Block F):** Quick-reference emergency actions.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- HAZARD GRID / HERO (2.9"--15.5" / ~12.6")
  Block B: 6 hazard cards (3x2 grid)
ZONE 3 -- PPE CHECKLIST (15.5"--22.0" / ~6.5")
  Block D: Required PPE items
ZONE 4 -- SAFETY ADVANTAGE CALLOUT (22.0"--28.5" / ~6.5")
  Block E: "No Atmosphere Hazards" highlight + prohibited items
ZONE 5 -- EMERGENCY PROCEDURES (28.5"--32.5" / ~4.0")
  Block F: Emergency quick-reference strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Induction Hardening -- Know the Hazards Before You Energize` -- 36 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `No flammable atmospheres. No toxic gases. But strong electromagnetic fields and high-voltage AC demand respect.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Hazard Grid (HERO)

**Section label:** `6 HAZARDS YOU MUST KNOW` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- 3x2 Hazard Grid**

Y: 3.8" to 15.3". Each card: Rounded rect, W: 7.33", H: 5.5", fill `#1E2435`, radius 8, left accent 0.06".

| Pos | Hazard | Accent | Icon | Details | Mitigation |
|---|---|---|---|---|---|
| R1C1 | ELECTROMAGNETIC FIELD (EMF) | `#E05C5C` | lightning-bolt | Strong AC magnetic field near inductor; interferes with cardiac pacemakers; heats any ferrous metal in proximity (tools, watches, jewelry, belt buckles) | Warning signs; NO pacemaker wearers near energized equipment; remove ALL ferrous objects from person before approach |
| R1C2 | ELECTRICAL SHOCK | `#E05C5C` | zap | High-frequency AC at significant power levels; water-cooled coils carry voltage | Full guarding and interlocks; NEVER touch coil or part when energized; lockout/tagout for coil changes |
| R1C3 | HOT PARTS | `#E8A020` | flame | Localized heating to 1600+ F; part may be hot in unpredictable locations -- only the heated zone glows, but adjacent areas conduct heat | Tongs for all handling; heat-resistant gloves; no bare-hand contact with recently processed parts; allow cooling time |
| R2C1 | QUENCH SPRAY / STEAM | `#E8A020` | droplets | Hot quenchant splash during spray quench; vigorous steam generation; polymer quenchant can cause skin irritation | Splash guards around quench zone; face shield; chemical-resistant gloves; ventilation for steam extraction |
| R2C2 | NOISE | `#2EC4B6` | ear | Magnetostrictive vibration of parts during heating produces 85--110 dB; varies by part geometry and frequency | Hearing protection required above 85 dB; ear plugs or muffs; monitor with sound level meter |
| R2C3 | PINCH / MECHANICAL | `#2EC4B6` | gear | Rotating parts (60--300 RPM); CNC scanning mechanisms; automated part handling | Machine guarding; interlocks on access doors; never reach into rotation zone during operation |

Grid positions:
- Row 1: Y: 3.8". X: 0.5" / 8.17" / 15.83"
- Row 2: Y: 9.8". X: 0.5" / 8.17" / 15.83"

Card interior layout:
- Hazard name: Barlow SemiBold, 20 pt, accent color
- Details: Inter Regular, 13 pt, `#F0EDE8`, line height 155%
- Mitigation: Inter Medium, 13 pt, `#27AE60`, preceded by `FIX:` label

---

### ZONE 3 -- PPE Checklist

**Section label:** `REQUIRED PERSONAL PROTECTIVE EQUIPMENT` -- Y: 15.7".

**BLOCK D -- PPE Items**

Y: 16.3" to 21.8". Two columns (X: 0.5", W: 11.0" and X: 12.0", W: 11.5").

Each item: Rounded rect H: 1.6", fill `#1E2435`, left accent 0.06" `#27AE60`.

| Col | Item | Description |
|---|---|---|
| L1 | SAFETY GLASSES (ANSI Z87.1) | Standard impact-rated; no shade required for induction (no UV/IR from flame) |
| L2 | HEAT-RESISTANT GLOVES | Rated to 500 F minimum; leather or Kevlar; for part handling only -- remove before approaching energized coil |
| L3 | HEARING PROTECTION | Ear plugs (NRR 25+) or muffs; required when noise exceeds 85 dB during heating cycle |
| R1 | FACE SHIELD | Over safety glasses during quench operations; protects against splash and steam |
| R2 | STEEL-TOE BOOTS | Standard; parts are heavy and hot |
| R3 | NON-FERROUS WATCH / NO JEWELRY | Remove ALL ferrous metal from body before approaching energized induction equipment |

Item name: Barlow SemiBold 16 pt `#F0EDE8`. Description: Inter Regular 13 pt `#F0EDE8` at 80%.

---

### ZONE 4 -- Safety Advantage Callout

**Section label:** `THE INDUCTION SAFETY ADVANTAGE` -- Y: 22.2".

**BLOCK E -- Two-panel layout**

**Left -- No Atmosphere Hazards (X: 0.5", W: 11.0"):**
- Rounded rect H: 5.5", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `NO ATMOSPHERE HAZARDS` -- Barlow SemiBold 20 pt `#27AE60`
- Body (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
Unlike furnace hardening processes:
  - No carbon monoxide (CO)
  - No hydrogen (H2)
  - No ammonia (NH3)
  - No flammable atmosphere
  - No nitrogen purge required
  - No burn-off pilot flames
  - No explosion risk from atmosphere ignition
```
- Bottom note: `This makes induction one of the safest heat treatment processes from an atmosphere standpoint.` Inter Medium 13 pt `#27AE60`

**Right -- Prohibited Items Near Energized Equipment (X: 12.0", W: 11.5"):**
- Rounded rect H: 5.5", fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `PROHIBITED NEAR ENERGIZED COIL` -- Barlow SemiBold 20 pt `#E05C5C`
- Items (Inter Medium 14 pt `#F0EDE8`):
```
- Cardiac pacemakers or implanted defibrillators
- Steel watches, rings, belt buckles
- Steel tools (unless non-magnetic SS)
- Credit cards (magnetic strip damage)
- Cell phones (potential interference)
- Loose clothing near rotating parts
```
- Warning: `EMF can heat ferrous objects on your body without warning -- burns can occur inside gloves or under clothing` Inter Medium 12 pt `#E05C5C`

---

### ZONE 5 -- Emergency Procedures

**Section label:** `EMERGENCY QUICK REFERENCE` -- Y: 28.7".

**BLOCK F -- Four Emergency Cards**

Y: 29.4" to 32.3". Four cards, W: 5.5", H: 2.7", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Emergency | Action |
|---|---|---|---|
| 1 | 0.5" | ELECTRICAL CONTACT | De-energize immediately (E-stop); do NOT touch victim while circuit is live; call 911 |
| 2 | 6.33" | BURN INJURY | Cool with running water 10+ min; do not apply ice directly; seek medical for 2nd/3rd degree |
| 3 | 12.16" | QUENCH SPLASH (EYES) | Flush eyes with water 15 min at eyewash station; remove contacts; seek medical |
| 4 | 18.0" | EQUIPMENT FIRE | E-stop; CO2 or dry chemical extinguisher; do NOT use water on electrical fire |

Emergency label: Barlow SemiBold 16 pt `#E05C5C`. Action: Inter Medium 13 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard footer. Title: `Safety & PPE -- Induction Hardening`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. It does not replace site-specific safety procedures, job hazard analyses, or equipment-specific lockout/tagout programs. Always follow your facility's safety protocols. Source: General industry knowledge; OSHA standards; equipment manufacturer guidelines.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Induction Hardening -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The EMF hazard is the headline safety concern for induction -- it is unique to this process and unfamiliar to operators coming from furnace backgrounds. The pacemaker warning must be visually prominent. The "No Atmosphere Hazards" callout is a deliberate positive-safety message -- operators should understand what induction does NOT expose them to, which builds confidence and contextualizes the hazards that DO exist.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #614 -- Construction Workup v1.0*
*2026-04-26*
