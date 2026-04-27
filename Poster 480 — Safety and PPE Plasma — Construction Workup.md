---
Project: Plating Posters Inc
Poster Number: 480
Title: "Safety & PPE -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 2)"
Technical Source: APS safety hazards, TLV/PEL values, and PPE requirements per OSHA, ACGIH, and industry best practice. Noise levels 100-130 dB at operator position. UV/IR comparable to welding arc.
Process Scope: Atmospheric plasma spray -- safety hazards and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Safety
  - PPE
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #480 -- Construction Workup
## Safety & PPE -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the safety poster for the APS cluster. It must be immediately readable, impossible to ignore, and designed to save lives. Coral is the dominant accent color. Every hazard gets its own card. The big-number rule card in the header features the plasma temperature -- 15,000 degC -- to convey the severity of the environment.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard grid (Block B -- HERO):** 8 hazard cards in a 4x2 grid. Each card: hazard icon placeholder, hazard name, details, controls. Coral-tinted glass.
2. **TLV/PEL reference table (Block D):** 6-row table with exposure limits for common APS fume constituents.
3. **PPE checklist (Block E):** Visual checklist of required PPE with checkboxes.
4. **"No Compromise" safety callout (Block F):** Full-width amber banner with the core safety message.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + rule card (15,000 degC plasma core)

ZONE 2 -- HAZARD GRID / HERO (2.9"--15.5" / ~12.6")
  Block B: 8 hazard cards (4x2 grid)

ZONE 3 -- TLV/PEL TABLE (15.5"--22.0" / ~6.5")
  Block D: Exposure limit reference table

ZONE 4 -- PPE CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: Required PPE visual checklist

ZONE 5 -- SAFETY CALLOUT (28.5"--32.5" / ~4.0")
  Block F: "No Compromise" banner + booth requirements

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Plasma Spray (APS) -- Know the Hazards, Wear the Gear` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `100-130 dB noise. UV/IR radiation. Metal and ceramic fumes. 40-80 kW DC power. This is not optional safety -- it is survival.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right side of header):**
- Rounded rect, X: 17.0", Y: 0.5", W: 6.5", H: 2.2", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Big number: `15,000` -- Barlow Condensed ExtraBold, 72 pt, `#E05C5C`
- Label: `degC plasma core temperature` -- Inter Medium, 14 pt, `#F0EDE8`

---

### ZONE 2 -- Hazard Grid (HERO)

**Section label:** `8 HAZARDS YOU MUST CONTROL` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt.

**BLOCK B -- 4x2 Hazard Grid**

Y: 3.8" to 15.3". Cards: W: 5.5", H: 5.5", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

Gap between cards: 0.33" horizontal, 0.4" vertical.

| Pos | X | Y | Hazard | Details | Controls |
|---|---|---|---|---|---|
| R1C1 | 0.5" | 3.8" | NOISE (100-130 dB) | Plasma gun exceeds 140 dB at source; causes permanent hearing damage in minutes | Double hearing protection (plugs + muffs); NRR 30+ |
| R1C2 | 6.33" | 3.8" | UV/IR RADIATION | Intense UV from plasma arc; comparable to welding arc; skin and eye burns | Shade 10-14 welding helmet; no exposed skin within line of sight |
| R1C3 | 12.16" | 3.8" | METAL & CERAMIC FUMES | NiCr, Co, Cr2O3, ZrO2 fumes; varies by feedstock; some carcinogenic | Local exhaust ventilation (LEV); HEPA; P100 RPE minimum |
| R1C4 | 18.0" | 3.8" | DUST EXPLOSION | Fine Al, Ti, Mg powders are explosive when airborne | Inert atmosphere powder handling; grounding; no open flames |
| R2C1 | 0.5" | 9.7" | THERMAL BURNS | Hot substrate, fixtures, overspray; plasma jet is lethal | Heat-resistant gloves; leather apron; face shield |
| R2C2 | 6.33" | 9.7" | ELECTRICAL (40-80 kW) | DC power supply; HF arc start; lethal shock potential | Lockout/tagout; insulated gloves; proper grounding |
| R2C3 | 12.16" | 9.7" | COMPRESSED GAS | High-pressure Ar, H2 (flammable), N2; asphyxiation risk | Secured cylinders; H2 leak detection; O2 monitoring |
| R2C4 | 18.0" | 9.7" | OVERSPRAY DUST | Respirable particles in booth; long-term lung damage | Enclosed spray booth; downdraft ventilation; HEPA filtration |

Interior per card:
- Hazard name: Barlow SemiBold, 18 pt, `#E05C5C`
- Details: Inter Regular, 12 pt, `#F0EDE8`
- Controls: Inter Medium, 12 pt, `#27AE60`
- Controls label: `CONTROL:` Barlow SemiBold, 11 pt, `#27AE60`

---

### ZONE 3 -- TLV/PEL Reference Table

**Section label:** `EXPOSURE LIMITS -- KNOW YOUR NUMBERS` -- Y: 15.7".

**BLOCK D -- 6-Row Table**

Y: 16.3" to 21.5". Columns: Substance (5.0") | OSHA PEL (4.5") | ACGIH TLV (4.5") | Notes (9.0")

| Substance | OSHA PEL (TWA) | ACGIH TLV (TWA) | Notes |
|---|---|---|---|
| Chromium (Cr metal) | 1.0 mg/m3 | 0.5 mg/m3 | Cr2O3 feedstock |
| Cr(VI) compounds | 0.005 mg/m3 | 0.0002 mg/m3 | Carcinogenic; avoid Cr(VI)-generating conditions |
| Nickel (metal dust) | 1.0 mg/m3 | 1.5 mg/m3 | NiCr, NiAl feedstocks |
| Cobalt | 0.1 mg/m3 | 0.02 mg/m3 | Hard metal lung disease; bio-monitoring recommended |
| Zirconia (as Zr) | 5 mg/m3 | 5 mg/m3 | YSZ TBC feedstock |
| Alumina (as Al) | 15 mg/m3 (total) | 1 mg/m3 (resp.) | Al2O3 feedstock and grit blast media |

Header: fill `#3A4055`. Data: JetBrains Mono 12 pt. PEL/TLV values in `#E05C5C` for emphasis. Notes: Inter Regular 11 pt.

---

### ZONE 4 -- PPE Checklist

**Section label:** `REQUIRED PPE -- EVERY TIME, NO EXCEPTIONS` -- Y: 22.2".

**BLOCK E -- PPE Visual Checklist**

Y: 22.9" to 28.3". Two columns of PPE items (5 per column).

Each item: Rounded rect, W: 11.0", H: 0.9", fill `#1E2435`, left accent `#27AE60` 0.06".

| PPE Item | Specification |
|---|---|
| Hearing protection | Double protection: plugs + muffs; NRR 30+ |
| Welding helmet | Shade 10-14; auto-darkening recommended |
| Respiratory protection | P100 half-face minimum; PAPR for extended work |
| Heat-resistant gloves | Leather or Kevlar; rated to 250 degC minimum |
| Leather apron | Full-length; protects against spatter and radiant heat |
| Safety boots | Steel toe; metatarsal guard; heat-resistant sole |
| Face shield | Over welding lens for grinding operations |
| Fire-resistant clothing | Long sleeves; no synthetic fabrics (melts to skin) |
| Insulated gloves | For electrical work; lockout/tagout procedures |
| Eye protection | Safety glasses with side shields under helmet |

Item name: Barlow SemiBold, 14 pt, `#F0EDE8`. Spec: JetBrains Mono 12 pt, `#F0EDE8` at 70%.

Checkbox squares: 0.25" x 0.25", border 2 pt `#27AE60`, no fill (empty checkbox visual).

---

### ZONE 5 -- Safety Callout

**Section label:** Y: 28.7".

**BLOCK F -- Full-Width Safety Banner**

- Rounded rect, X: 0.5", Y: 29.2", W: 23.0", H: 3.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8

**Main text:** Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center

> PLASMA SPRAY BOOTHS ARE MANDATORY -- NOT OPTIONAL

**Sub-text:** Inter Medium, 16 pt, `#F0EDE8`, Center

> Enclosed booth with downdraft ventilation. HEPA or cartridge dust collection. Minimum 100 FPM face velocity. No one enters during spray without full PPE. No exceptions.

**Bottom line:** Inter Regular, 13 pt, `#E8A020`

> If your booth ventilation cannot maintain fume levels below TLV at the operator position, STOP spraying and fix the ventilation.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Plasma Spray`. Version `v1.0 -- 2026`.

Disclaimer: `Source: OSHA PELs, ACGIH TLVs, ASM Handbook Vol 5A, ITSA best practices. Consult your facility safety officer and applicable regulations.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster should feel serious. Coral dominates. The 15,000 degC rule card sets the tone immediately. Hearing protection gets the first hazard card because noise damage is the most insidious -- cumulative, irreversible, and often ignored. The cobalt TLV of 0.02 mg/m3 is the number that should make people pause -- that is extremely low and very hard to achieve without proper ventilation.

---

*Alaina -- Poster #480 -- Construction Workup v1.0 -- 2026-04-26*
