---
Project: Plating Posters Inc
Poster Number: 440
Title: "Safety & PPE -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Section 5.8)"
Process Scope: Safety and PPE requirements for Diamond-Like Carbon coating operations
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Safety
  - PPE
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #440 -- Construction Workup
## Safety & PPE -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

DLC safety centers on three pillars: flammable/explosive precursor gases (acetylene is the big one -- LEL 2.5% and can decompose explosively above 15 psig), high-voltage bias supplies (up to 2,000 V on filtered arc systems), and UV radiation from arc sources. This poster is the "hang it by the chamber door" reference.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Hazard matrix (Block B -- HERO):** A 2x4 grid of hazard cards, each with an icon placeholder, hazard name, detail, and mitigation. Coral-tinted glass cards for highest-risk items.
2. **PPE checklist (Block D):** Visual PPE layout -- head-to-toe gear list.
3. **Emergency procedures strip (Block E):** Quick-action steps for gas leak, electrical contact, UV exposure.
4. **Gas properties reference (Block F):** Compact table of precursor gases with LEL/PEL/key hazard.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 21.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- HAZARD MATRIX / HERO (2.9"--15.5" / ~12.6")
  Block B: Eight hazard cards (2x4 grid)

ZONE 3 -- PPE CHECKLIST (15.5"--21.5" / ~6.0")
  Block D: Head-to-toe PPE requirements

ZONE 4 -- EMERGENCY PROCEDURES (21.5"--27.5" / ~6.0")
  Block E: Three emergency scenarios with response steps

ZONE 5 -- GAS PROPERTIES REFERENCE (27.5"--32.5" / ~5.0")
  Block F: Precursor gas safety data table

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Disclaimer + poster title + series + version
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Diamond-Like Carbon Coating Operations` -- 36 pt `#E05C5C` (Coral). Y: 1.5".
**Tagline:** `Acetylene is explosive. Bias voltage is lethal. Arc light causes eye damage. Know the hazards before you open the chamber.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Hazard Matrix (HERO)

**Section label:** `HAZARD IDENTIFICATION -- 8 KEY RISKS` -- Y: 3.1". Barlow Condensed ExtraBold 28 pt `#F0EDE8`.

**BLOCK B -- 2x4 Hazard Grid**

Y: 3.8" to 15.3". Cards in 2 rows of 4. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 5.3", fill `#1E2435`, radius 6.

| Card | Row | X | Hazard | Accent | Detail | Mitigation |
|---|---|---|---|---|---|---|
| 1 | R1 | 0.5" | ACETYLENE (C2H2) | `#E05C5C` | Flammable/explosive. LEL 2.5%. Decomposes explosively > 15 psig. | Flash arrestors on all lines. Never compress above 15 psig. LEL monitors mandatory. |
| 2 | R1 | 6.33" | METHANE (CH4) | `#E05C5C` | Flammable. LEL 5%. | Ventilation + LEL detection. No ignition sources. |
| 3 | R1 | 12.16" | HIGH VOLTAGE BIAS | `#E05C5C` | Up to 2,000 V on filtered arc. Lethal. | Lockout/tagout. Interlock on chamber door. Never bypass. |
| 4 | R1 | 18.0" | UV RADIATION | `#E8A020` | Arc sources produce intense UV. Eye damage in seconds. | UV-rated viewport filters. Never look directly at arc. |
| 5 | R2 | 0.5" | HOT SURFACES | `#E8A020` | Chamber walls and fixtures 50--200 C after cycle. | Heat-resistant gloves for unloading. Wait for cool-down. |
| 6 | R2 | 6.33" | CHROMIUM DUST | `#E05C5C` | Cr target handling -- Cr(VI) formation possible at high O2. PEL 5 ug/m3. | Respiratory protection during target changes. Wet wipe cleanup. |
| 7 | R2 | 12.16" | TMS (TETRAMETHYLSILANE) | `#E8A020` | Flammable liquid. Flash point -27 C. Vapor heavier than air. | Store in approved cabinets. Ventilate at floor level. |
| 8 | R2 | 18.0" | VACUUM HAZARD | `#2EC4B6` | Implosion risk. Viewport failure. | Never use non-rated glass. Inspect O-rings on schedule. |

Interior per card:
- Hazard name: Barlow SemiBold, 18 pt, accent color
- Detail: Inter Regular, 13 pt, `#F0EDE8`
- Mitigation: Inter Medium, 12 pt, `#27AE60`
- Left accent: 0.06" in accent color

---

### ZONE 3 -- PPE Checklist

**Section label:** `REQUIRED PPE -- HEAD TO TOE` -- Y: 15.7".

**BLOCK D -- PPE Items**

Y: 16.3" to 21.3". Two columns.

**Left column (X: 0.5", W: 11.0"):**

| PPE Item | When | Color |
|---|---|---|
| Safety glasses (standard) | All chamber operations | `#2EC4B6` |
| UV-rated viewport filter | Arc system observation | `#E05C5C` |
| Face shield | Arc viewport close inspection | `#E05C5C` |
| Hearing protection | Near roughing pumps (70--85 dB) | `#E8A020` |

**Right column (X: 12.0", W: 11.5"):**

| PPE Item | When | Color |
|---|---|---|
| Nitrile gloves | Part handling (fingerprint prevention) | `#2EC4B6` |
| Heat-resistant gloves | Unloading after cycle | `#E05C5C` |
| Respiratory protection | Cr target handling; TMS spill | `#E05C5C` |
| Steel-toe boots | Standard shop floor | `#2EC4B6` |

Each item: Rounded rect row, H: 1.1", fill `#1E2435`, left accent 0.06" in designated color.
Item name: Barlow SemiBold, 16 pt, `#F0EDE8`. When: Inter Regular, 13 pt, `#F0EDE8` at 70%.

---

### ZONE 4 -- Emergency Procedures

**Section label:** `EMERGENCY RESPONSE -- THREE SCENARIOS` -- Y: 21.7".

**BLOCK E -- Three Emergency Cards**

Y: 22.3" to 27.3". Three equal-width cards in a row. Gap: 0.33".

Each card: Rounded rect, W: 7.33", H: 4.8", fill `#1E2435`, radius 6.

| Card | X | Scenario | Accent | Steps |
|---|---|---|---|---|
| 1 | 0.5" | GAS LEAK | `#E05C5C` | 1. Evacuate area. 2. Do NOT use electrical switches. 3. Shut off gas supply at cylinder (if safe). 4. Ventilate. 5. Call emergency services. |
| 2 | 8.16" | ELECTRICAL CONTACT | `#E05C5C` | 1. Cut power at breaker -- do NOT touch victim while energized. 2. Call emergency services. 3. Administer CPR if trained. 4. Lockout/tagout before any investigation. |
| 3 | 15.83" | UV EXPOSURE | `#E8A020` | 1. Move away from arc source. 2. Flush eyes with clean water 15 min. 3. Seek medical attention. 4. Report incident. |

Scenario title: Barlow SemiBold, 20 pt, accent color.
Steps: Inter Regular, 13 pt, `#F0EDE8`, numbered list.

---

### ZONE 5 -- Gas Properties Reference

**Section label:** `PRECURSOR GAS REFERENCE` -- Y: 27.7".

**BLOCK F -- Gas Table**

Y: 28.3" to 32.3". Full width.

| Gas | Formula | LEL | PEL/TLV | Key Hazard | Flash Point |
|---|---|---|---|---|---|
| Acetylene | C2H2 | 2.5% | -- | Explosive decomposition > 15 psig | Gas |
| Methane | CH4 | 5.0% | -- | Flammable; asphyxiant in confined space | Gas |
| Argon | Ar | -- | -- | Simple asphyxiant | -- |
| TMS | Si(CH3)4 | -- | -- | Flammable liquid; flash -27 C | -27 C |

Header: Barlow SemiBold, 14 pt, `#F0EDE8`. Fill `#3A4055`.
Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Alternating rows `#1E2435` / `#252B3D`.
LEL values in `#E05C5C`.

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- DLC`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool and does not replace site-specific safety training, OSHA requirements, or equipment manufacturer safety manuals. Always follow your facility's safety program and SDS documentation.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster lives next to the DLC chamber door. Coral dominates -- this is a safety poster. The acetylene hazard is the most critical single item: it can decompose explosively even without an ignition source if compressed above 15 psig. The high-voltage hazard (up to 2,000 V) is equally lethal. UV from arc sources causes acute photokeratitis ("welder's flash") in seconds of direct exposure. Every card must be readable at arm's length.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #440 -- Construction Workup v1.0*
*2026-04-26*
