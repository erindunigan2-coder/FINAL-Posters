---
Project: Plating Posters Inc
Poster Number: 400
Title: "Safety & PPE -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.8)"
Technical Source: PVD safety hazards covering high voltage, vacuum, UV radiation, hot surfaces, process gases, and target material handling. PPE requirements per OSHA general industry standards.
Process Scope: PVD safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #400 -- Construction Workup
## Safety & PPE -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

PVD safety is dominated by high voltage, vacuum implosion risk, UV radiation from arc sources, hot surfaces after deposition cycles, and hazardous process gases. This poster hangs next to the PVD chamber as a constant reminder. Every hazard gets its own card with PPE requirement and emergency response.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** 3x3 grid of hazard cards -- each card has a hazard name, severity indicator, detail, and PPE requirement.
2. **PPE checklist (Block D):** Visual checklist of all required PPE items for PVD operations.
3. **Emergency response strip (Block E):** Four emergency scenarios with immediate actions.
4. **Gas hazard table (Block F):** Specific gas hazards with PEL/LEL values.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 18.0" / 24.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Coral -- safety)
ZONE 3 -- HAZARD GRID / HERO (4.2"--18.0" / ~13.8")
ZONE 4 -- PPE CHECKLIST (18.0"--24.0" / ~6.0")
ZONE 5 -- EMERGENCY RESPONSE STRIP (24.0"--28.5" / ~4.5")
ZONE 6 -- GAS HAZARD TABLE (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PVD SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `High Voltage, Vacuum, UV, Hot Surfaces, Process Gases` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `PVD chambers combine every hazard category in one footprint. Respect the process. Wear the gear. Follow lockout/tagout without exception.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#E05C5C`, text `#1A1F2E` (SAFETY). Others dimmed.
All 10 stages shown: Part Prep | **SAFETY** | Cleaning | Fixturing | Vacuum | Ion Etch | Deposition | Cooling | Unloading | Inspection

Below: `Safety applies to EVERY stage -- this poster covers hazards across the entire PVD cycle`

---

### ZONE 3 -- Hazard Grid (HERO)

**Section label:** `PVD HAZARDS -- KNOW BEFORE YOU APPROACH THE CHAMBER` -- Y: 4.4".

**BLOCK B -- 3x3 Hazard Grid**

Y: 5.0" to 17.8". Nine cards in a 3x3 grid.

Each card: Rounded rect W: 7.33", H: 4.0", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.
Gap between cards: 0.33" horizontal, 0.3" vertical.

| Position | Hazard | Severity | Detail | PPE / Control |
|---|---|---|---|---|
| R1C1 | HIGH VOLTAGE | DANGER | DC supplies up to 1000 V; arc ignition pulses; substrate bias up to -1200 V | Lockout/tagout before any maintenance; interlock verification before cycle start |
| R1C2 | VACUUM IMPLOSION | WARNING | Chamber under high vacuum; glass viewports can implode; O-ring failure | Never use unrated glass viewports; inspect O-rings per schedule; stand clear during pump-down |
| R1C3 | UV / ARC RADIATION | DANGER | Arc sources produce intense UV; retinal damage possible | UV-rated viewport filters mandatory; never look directly at arc; face shield for viewport inspection |
| R2C1 | HOT SURFACES | WARNING | Chamber walls, fixtures 200-500 C after cycle; parts 100-200 C at unload | Heat-resistant gloves (Kevlar or similar); allow cool-down; temperature labels on chamber |
| R2C2 | PROCESS GASES -- Ar, N2 | CAUTION | Asphyxiants in confined spaces; displace oxygen without warning | O2 monitor in PVD area; ventilation; never enter chamber without gas-free verification |
| R2C3 | C2H2 (ACETYLENE) | DANGER | Flammable/explosive; LEL 2.5%; used in DLC and some reactive processes | Gas detection; no ignition sources; purge lines before/after use; check for leaks with sniffer |
| R3C1 | TARGET MATERIALS | WARNING | Cr targets: hexavalent Cr dust during handling; Ti dust pyrophoric in fine form | Respirator for target changes; wet-wipe Cr dust; no compressed air on Ti fines |
| R3C2 | PUMP OILS | CAUTION | Diffusion pump oil (polyphenyl ether) toxic; turbo pump oil conventional hazard | Nitrile gloves; avoid skin contact; ventilate during oil changes |
| R3C3 | NOISE | CAUTION | Roughing pumps 70-85 dB continuous | Hearing protection when operating near roughing pump; dampen with enclosure if possible |

Interior per card:
- Hazard name: Barlow SemiBold, 18 pt, `#E05C5C`
- Severity badge: Rounded rect 1.2" x 0.35"; DANGER = fill `#E05C5C`, WARNING = fill `#E8A020`, CAUTION = fill `#E8A020` at 50%
- Badge text: Barlow Condensed ExtraBold, 12 pt, `#1A1F2E`
- Detail: Inter Regular, 12 pt, `#F0EDE8`
- PPE/Control: Inter Medium, 12 pt, `#2EC4B6`

---

### ZONE 4 -- PPE Checklist

**Section label:** `REQUIRED PPE -- PVD OPERATIONS` -- Y: 18.2".

**BLOCK D -- PPE Items (Y: 18.8" to 23.8")**

Two-column layout. Each item is a rounded rect W: 11.0", H: 1.1", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

| Column | Item | When Required |
|---|---|---|
| Left 1 | Safety glasses | All times in PVD area |
| Left 2 | UV-rated face shield | Arc viewport inspection; chamber opening after arc cycle |
| Left 3 | Heat-resistant gloves (Kevlar) | Unloading parts; any hot-surface contact |
| Left 4 | Nitrile gloves | Part handling (prevents fingerprint contamination); pump oil changes |
| Right 1 | Hearing protection | Near roughing pumps (70-85 dB) |
| Right 2 | Respirator (P100 or higher) | Target changes (especially Cr); cleaning sputtered residue |
| Right 3 | Steel-toe boots | Standard shop floor PPE |
| Right 4 | Acid-resistant apron | Wet chemistry pre-cleaning stages |

Item name: Barlow SemiBold, 16 pt, `#F0EDE8`.
When required: Inter Regular, 13 pt, `#F0EDE8` at 70%.

---

### ZONE 5 -- Emergency Response Strip

**Section label:** `EMERGENCY RESPONSE -- IMMEDIATE ACTIONS` -- Y: 24.2".

**BLOCK E -- Four Emergency Cards (Y: 24.8" to 28.3")**

Four cards in a row. Each card: W: 5.5", H: 3.3", fill `#1E2435`, radius 6, top accent 4 pt `#E05C5C`.

| Card | X | Emergency | Immediate Action |
|---|---|---|---|
| 1 | 0.5" | ELECTRICAL SHOCK | De-energize system (E-stop); do not touch victim until power confirmed off; call emergency services |
| 2 | 6.33" | GAS LEAK (C2H2) | Evacuate area; ventilate; no ignition sources; shut off gas supply remotely if possible |
| 3 | 12.16" | VIEWPORT IMPLOSION | Stay clear of debris; secure area; verify vacuum integrity before restart |
| 4 | 18.0" | BURN (HOT SURFACE) | Cool burn with running water 10+ min; remove from heat source; seek medical attention for 2nd/3rd degree |

Emergency name: Barlow SemiBold, 16 pt, `#E05C5C`
Action: Inter Medium, 13 pt, `#F0EDE8`

---

### ZONE 6 -- Gas Hazard Table

**Section label:** `PROCESS GAS HAZARDS` -- Y: 28.7".

**BLOCK F -- Gas Table (Y: 29.2" to 32.3")**

| Gas | Use in PVD | Hazard | PEL / LEL | Control |
|---|---|---|---|---|
| Argon (Ar) | Sputtering gas, ion etch | Asphyxiant | N/A -- displaces O2 | O2 monitor; ventilation |
| Nitrogen (N2) | Reactive gas (nitrides) | Asphyxiant | N/A -- displaces O2 | Same as Ar |
| Acetylene (C2H2) | DLC, carbonitride coatings | Flammable/explosive | LEL 2.5% | Gas detection; purge protocol |
| Oxygen (O2) | Reactive sputtering (oxides) | Oxidizer | Enrichment > 23.5% | No oil/grease near O2 lines |

Header: Barlow SemiBold 13 pt `#F0EDE8`, fill `#3A4055`.
Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Safety & PPE -- PVD`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. It does not replace site-specific safety training, SDS review, or equipment-specific lockout/tagout procedures. Consult your safety officer and equipment manual.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Safety posters use Coral as the dominant accent instead of the usual Teal/Emerald. The hazard grid is the hero -- it must be readable at 6 feet with clear severity indicators. The PPE checklist serves as a daily pre-shift verification. Every PVD operator should be able to glance at this poster and confirm they have the right gear before approaching the chamber.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #400 -- Construction Workup v1.0*
*2026-04-26*
