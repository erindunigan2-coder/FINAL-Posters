---
Project: Plating Posters Inc
Poster Number: 520
Title: "Safety & PPE -- Cold Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 5: Cold Spray)"
Technical Source: Cold spray safety hazards and PPE requirements. Watson research brief sourced from ASM Handbook Vol 5A, OSHA/ACGIH TLV data, and NFPA 652.
Process Scope: Cold spray -- safety and personal protective equipment
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ColdSpray
  - ThermalSpray
  - Safety
  - PPE
  - ConstructionWorkup
  - ClusterTS05
---

# Poster #520 -- Construction Workup
## Safety & PPE -- Cold Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Safety poster for the Cold Spray cluster. Cold spray is the safest thermal spray process from a fume perspective (no melting = minimal fume), but it introduces unique hazards: extremely high gas pressures (20--60 bar), helium asphyxiation risk, pyrophoric metal dust (Ti, Al, Mg), and supersonic ricocheting particles. The poster must communicate both the safety advantages and the unique risks.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard matrix (Block B -- HERO):** 7-row hazard table with severity indicators. Standard table construction with coral-tinted rows for critical hazards.
2. **PPE figure diagram (Block C):** Full-body PPE callout figure. Built with rectangles and text labels (no illustration -- schematic representation).
3. **"Safest Fume Profile" callout (Block D):** Amber-tinted glass callout emphasizing the fume advantage.
4. **TLV/PEL reference strip (Block E):** Compact table of exposure limits for common cold spray feedstock metals.
5. **Emergency response strip (Block F):** 4-card strip for emergency scenarios.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 16.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- HAZARD MATRIX + PPE FIGURE (2.9"--16.5" / ~13.6")
  Block B: 7-row hazard table (left, ~14.0" wide)
  Block C: PPE figure diagram (right, ~8.5" wide)

ZONE 3 -- SAFEST FUME PROFILE CALLOUT (16.5"--21.5" / ~5.0")
  Block D: Callout comparing cold spray fume levels to other thermal spray

ZONE 4 -- TLV/PEL REFERENCE (21.5"--26.5" / ~5.0")
  Block E: Exposure limit table for common metals

ZONE 5 -- EMERGENCY RESPONSE (26.5"--32.5" / ~6.0")
  Block F: 4-card emergency strip

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:**
- `Cold Spray -- Solid-State Process, Unique Hazards` -- 36 pt `#E05C5C` (Coral). Y: 1.5".

**Tagline:**
- `No melting means less fume -- but high-pressure gas, pyrophoric dust, and supersonic particles demand respect.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Hazard Matrix + PPE Figure

**Section label:** `HAZARD IDENTIFICATION` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Hazard Matrix (Left)**

X: 0.5", Y: 3.8", W: 14.0".

Header row: `#3A4055`, H: 0.5". Columns: Hazard (3.5") | Details (5.0") | Controls (5.5")

| Hazard | Details | Controls |
|---|---|---|
| NOISE (110--130 dB) | Supersonic jet -- comparable to HVOF | Double hearing protection; NRR 30+; enclosed booth |
| HIGH-PRESSURE GAS | N2 or He at 20--60 bar (300--870 PSI) | Certified pressure vessels; burst disc protection; no improvised fittings |
| HELIUM ASPHYXIATION | He displaces O2 in enclosed spaces -- odorless | O2 monitoring in booth; forced ventilation; never enter without O2 check |
| PYROPHORIC METAL DUST | Ti, Al, Mg powders are explosive/pyrophoric when airborne | NFPA 652 dust collection; inert atmosphere handling; grounding |
| RICOCHETING PARTICLES | Un-bonded particles rebound at high velocity (hundreds of m/s) | Enclosed spray booth; full face shield; eye protection |
| THERMAL (NOZZLE) | Gas heated to 200--1100 C at nozzle exit area | Heat-resistant PPE near nozzle; insulated fixturing; no bare contact |
| METAL DUST (GENERAL) | Fine particles from rebound and overspray | HEPA filtration; P100 respiratory protection; LEV |

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.5".
Hazard column: Barlow SemiBold, 14 pt, `#E05C5C`.
Details: Inter Regular, 12 pt, `#F0EDE8`.
Controls: Inter Medium, 12 pt, `#27AE60`.

**BLOCK C -- PPE Figure (Right)**

X: 15.0", Y: 3.8", W: 8.5", H: 12.0".
Rounded rect fill `#1E2435`, radius 8.

Schematic body outline (centered in box) with labeled callout lines:

| Body Zone | PPE Item | Color |
|---|---|---|
| Head | Shade 3--5 safety glasses (no welding lens needed -- no arc/flame) | `#2EC4B6` |
| Head | Full face shield (ricochet protection) | `#E05C5C` |
| Ears | Double hearing protection (plugs + muffs, NRR 30+) | `#E05C5C` |
| Respiratory | P100 half-face or PAPR (metal dust) | `#E05C5C` |
| Torso | Leather or flame-resistant jacket | `#E8A020` |
| Hands | Heat-resistant gloves (near nozzle) | `#E8A020` |
| Feet | Steel-toe boots | `#C8D0D8` |

Note at bottom of PPE figure:
- `NO welding helmet required -- cold spray has no arc, no flame, and minimal UV/IR` Inter Medium, 13 pt, `#27AE60`

---

### ZONE 3 -- Safest Fume Profile Callout

**Section label:** `THE COLD SPRAY SAFETY ADVANTAGE` -- Y: 16.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Fume Comparison Callout**

Y: 17.3" to 21.3".
Rounded rect, X: 0.5", W: 23.0", H: 3.8", fill `#1E2435`, radius 8, left accent 4 pt `#27AE60`.

**Header:** `LOWEST FUME OF ANY THERMAL SPRAY` Barlow SemiBold, 22 pt, `#27AE60`. Y: 17.5".

**Comparison bar chart (horizontal bars):**

| Process | Relative Fume | Bar Fill |
|---|---|---|
| Arc Spray | HIGHEST | `#E05C5C` bar, 100% width |
| Plasma Spray | HIGH | `#E05C5C` bar, 75% |
| HVOF | MODERATE | `#E8A020` bar, 50% |
| Flame Spray | MODERATE | `#E8A020` bar, 45% |
| Cold Spray | MINIMAL | `#27AE60` bar, 10% |

Each bar: H: 0.35", rounded ends. Labels left (process name, Inter Medium 13 pt), right (descriptor, JetBrains Mono 12 pt).

**Explanation:** `No melting = minimal fume generation. However, rebounding un-bonded particles create significant DUST. Dust collection (HEPA) and respiratory protection are still mandatory.` Inter Regular, 13 pt, `#F0EDE8` at 70%.

---

### ZONE 4 -- TLV/PEL Reference

**Section label:** `EXPOSURE LIMITS -- COMMON COLD SPRAY METALS` -- Y: 21.7".

**BLOCK E -- TLV Table**

Y: 22.3" to 26.3". Full width.

Header row: `#3A4055`. Columns: Metal (4.0") | OSHA PEL (5.0") | ACGIH TLV (5.0") | Notes (9.0")

| Metal | OSHA PEL (TWA) | ACGIH TLV (TWA) | Notes |
|---|---|---|---|
| Copper (dust) | 1.0 mg/m3 | 1.0 mg/m3 | Most common cold spray material |
| Aluminum (metal dust) | 15 mg/m3 (total) | 1.0 mg/m3 (respirable) | Note large PEL/TLV gap |
| Titanium | 15 mg/m3 (total) | -- (no TLV) | PYROPHORIC as fine powder |
| Nickel (metal) | 1.0 mg/m3 | 1.5 mg/m3 (inhalable) | Carcinogen (IARC Group 1 for compounds) |
| Silver (metal) | 0.01 mg/m3 | 0.1 mg/m3 (metal) | Argyria risk from chronic exposure |
| Zinc (as ZnO fume) | 5 mg/m3 | 2 mg/m3 (respirable) | Zinc fume fever from ZnO fume |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Metal names: Inter Medium, 13 pt. PEL/TLV values in `#E05C5C`.

---

### ZONE 5 -- Emergency Response

**Section label:** `EMERGENCY RESPONSE` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Emergency Cards**

Y: 27.4" to 32.3". Four cards. Gap: 0.33".

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | Scenario | Action |
|---|---|---|
| 1 | GAS LEAK (N2/He) | Evacuate; ventilate; check O2 level before re-entry; He is lighter than air -- accumulates at ceiling |
| 2 | DUST FIRE/EXPLOSION | Extinguish with Class D agent (metal fires); NEVER use water on Ti or Mg dust fires |
| 3 | HIGH-PRESSURE LINE FAILURE | Emergency gas shutoff; evacuate blast radius; inspect all fittings before restart |
| 4 | PARTICLE RICOCHET INJURY | First aid for high-velocity particle embedded in skin; seek medical; report incident |

Scenario: Barlow SemiBold, 15 pt, `#E05C5C`.
Action: Inter Regular, 12 pt, `#F0EDE8`.

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Safety & PPE -- Cold Spray`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Safety requirements vary by jurisdiction, employer policy, and specific application. Consult applicable OSHA, ACGIH, and NFPA standards. Consult your safety officer and equipment manufacturer documentation for site-specific requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE Cold Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cold spray is genuinely the safest thermal spray process for fume exposure, and this poster should celebrate that -- but it must equally emphasize the unique hazards that other thermal spray doesn't share: extreme gas pressures, helium displacement, pyrophoric dust, and high-velocity ricochets. The "no welding helmet needed" note in the PPE figure is a powerful visual differentiator from every other thermal spray safety poster.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #520 -- Construction Workup v1.0*
*2026-04-26*
