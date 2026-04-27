---
Project: Plating Posters Inc
Poster Number: 540
Title: "Safety & PPE -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS inherits all APS safety hazards (noise 100--130 dB, UV/IR, fumes, electrical, thermal) PLUS ethanol vapor explosion risk, nano-particle respiratory exposure, and pressurized liquid system hazards. Nanomaterial TLVs are not fully established -- precautionary principle applies.
Process Scope: SPS safety, PPE requirements, and hazard controls
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Safety
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #540 -- Construction Workup
## Safety & PPE -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

SPS inherits every hazard from conventional APS -- plus three additional hazards unique to the liquid suspension feedstock: ethanol vapor (flammable), nano-scale particle exposure (enhanced respiratory risk), and pressurized liquid feed systems. This poster covers both inherited APS hazards and SPS-specific additions. The nano-particle callout is the critical differentiator -- TLVs are not fully established, so the precautionary principle applies.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Hazard matrix (Block B -- HERO):** Large table/grid showing hazards, details, and controls. Standard table construction with color-coded severity indicators.
2. **SPS-specific hazard callout (Block C):** Three highlighted callout boxes for ethanol, nano-particles, and pressurized liquid -- the differentiators from standard APS.
3. **TLV/PEL reference strip (Block D):** Compact reference table of exposure limits.
4. **PPE checklist (Block E):** Visual PPE inventory with required/recommended designations.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- HAZARD MATRIX (2.9"--15.5" / ~12.6")
  Block B: Full hazard table (inherited APS + SPS-specific)
ZONE 3 -- SPS-SPECIFIC HAZARD CALLOUTS (15.5"--22.0" / ~6.5")
  Block C: Three callout boxes (ethanol, nano, pressurized liquid)
ZONE 4 -- TLV/PEL REFERENCE + PPE CHECKLIST (22.0"--28.5" / ~6.5")
  Block D: Exposure limits table (left)
  Block E: PPE checklist (right)
ZONE 5 -- EMERGENCY RESPONSE STRIP (28.5"--32.5" / ~4.0")
  Block F: 4 emergency scenario cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SAFETY & PPE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Suspension Plasma Spray (SPS) -- Hazards, Controls & Required Protection` -- 32 pt `#E05C5C` (Coral). Y: 1.4".
**Tagline:** `Every APS hazard, plus ethanol vapor, nano-particles, and pressurized liquid. Know what you're dealing with before you strike the arc.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Hazard Matrix

**Section label:** `HAZARD IDENTIFICATION -- INHERITED APS + SPS-SPECIFIC` -- Y: 3.1".

**BLOCK B -- Hazard Table**

Y: 3.8" to 15.3". Column widths (23.0" total):
- Hazard (4.0") | Details (8.5") | Controls (7.0") | Severity (3.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

| Hazard | Details | Controls | Severity |
|---|---|---|---|
| Noise | 100--130 dB at operator; gun >140 dB | Double hearing protection (plugs + muffs); NRR 30+ | `#E05C5C` HIGH |
| UV/IR Radiation | Intense UV from plasma arc; shade 10--14 equivalent | Shade 10--14 welding helmet; no exposed skin | `#E05C5C` HIGH |
| Metal/Ceramic Fumes | NiCr, Co, ZrO2 fumes vary by feedstock | LEV with HEPA; P100 RPE minimum | `#E05C5C` HIGH |
| Dust Explosion | Fine metal powders (Al, Ti) explosive when airborne | Inert atmosphere handling; grounding; no open flames | `#E05C5C` HIGH |
| Thermal Burns | Substrate/fixture temps; hot overspray | Heat-resistant gloves; leather apron; face shield | `#E8A020` MED |
| Electrical | DC power 40--80 kW; HF arc start | LOTO; insulated gloves; proper grounding | `#E8A020` MED |
| Compressed Gas | High-pressure Ar, H2 (flammable), N2 | Secured cylinders; H2 leak detection; regulators | `#E8A020` MED |
| Overspray Dust | Respirable particles in booth | Enclosed booth with downdraft ventilation | `#E8A020` MED |
| **ETHANOL VAPOR** | Flash point 13 degC / 55 degF; flammable | **Explosion-proof booth; vapor monitoring; grounding** | `#E05C5C` **HIGH** |
| **NANO-PARTICLE EXPOSURE** | Submicron/nano ceramics; enhanced lung penetration | **HEPA 99.97%; nano-specific P100 RPE; exposure monitoring** | `#E05C5C` **HIGH** |
| **PRESSURIZED LIQUID** | Suspension feed at 2--10 bar | **Rated hoses; relief valves; spill containment** | `#E8A020` MED |

Last three rows (SPS-specific) use bold text and `#E05C5C` left accent to distinguish from inherited APS hazards.

Data: Inter Regular, 12 pt. Hazard names: Barlow SemiBold, 13 pt. Severity indicators: JetBrains Mono, 12 pt.

---

### ZONE 3 -- SPS-Specific Hazard Callouts

**Section label:** `SPS-SPECIFIC HAZARDS -- BEYOND STANDARD APS` -- Y: 15.7".

**BLOCK C -- Three Callout Boxes**

Y: 16.3" to 21.8". Three side-by-side boxes.

| Hazard | X | W | Accent | Title |
|---|---|---|---|---|
| Ethanol Vapor | 0.5" | 7.33" | `#E05C5C` | ETHANOL VAPOR |
| Nano-Particles | 8.0" | 7.33" | `#E05C5C` | NANO-PARTICLE EXPOSURE |
| Pressurized Liquid | 15.5" | 8.0" | `#E8A020` | PRESSURIZED LIQUID FEED |

Each box: Rounded rect H: 5.3", fill `#1E2435`, left accent 0.06".

*Ethanol box:*
- `Flash point: 13 degC (55 degF)` JetBrains Mono 16 pt `#E05C5C`
- `Ethanol carrier = flammable atmosphere in spray booth`
- `Explosion-proof electrical in booth -- MANDATORY`
- `Continuous vapor monitoring with alarm`
- `Ground all containers and feed lines`
- `Store per NFPA 30 flammable liquid requirements`

*Nano-particle box:*
- `Particle size: 50 nm -- 5 um` JetBrains Mono 16 pt `#E05C5C`
- `Nano-ceramics penetrate deeper into lungs than micron-scale`
- `TLVs NOT fully established -- precautionary principle`
- `HEPA filtration 99.97% efficiency minimum`
- `P100 RPE with nano-rated filters`
- `Biological monitoring recommended`

*Pressurized liquid box:*
- `Feed pressure: 2--10 bar` JetBrains Mono 16 pt `#E8A020`
- `Suspension feed hoses must be rated for pressure`
- `Relief valves on all pressurized vessels`
- `Spill containment for ethanol-based suspension`
- `Regular hose and fitting inspection`

---

### ZONE 4 -- TLV/PEL Reference + PPE Checklist

**Two-column layout (Y: 22.2" to 28.3"):**

**Left -- TLV/PEL Reference (X: 0.5", W: 11.0"):**

Section label: `EXPOSURE LIMITS` Barlow Condensed ExtraBold 22 pt.

| Substance | OSHA PEL | ACGIH TLV |
|---|---|---|
| Chromium (metal) | 1.0 mg/m3 | 0.5 mg/m3 |
| Nickel (dust) | 1.0 mg/m3 | 1.5 mg/m3 |
| Cobalt | 0.1 mg/m3 | 0.02 mg/m3 |
| Zirconia (as Zr) | 5 mg/m3 | 5 mg/m3 |
| Alumina (as Al) | 15 mg/m3 (total) | 1 mg/m3 (resp) |
| Nano-ceramics | NOT ESTABLISHED | Precautionary |

Data: JetBrains Mono Regular, 12 pt. "NOT ESTABLISHED" row in `#E05C5C`.

**Right -- PPE Checklist (X: 12.0", W: 11.5"):**

Section label: `REQUIRED PPE` Barlow Condensed ExtraBold 22 pt.

| Item | Rating | Status |
|---|---|---|
| Welding helmet | Shade 10--14 | REQUIRED |
| Hearing protection | NRR 30+ (double) | REQUIRED |
| Respirator | P100 (nano-rated) | REQUIRED |
| Heat-resistant gloves | 260 degC+ rated | REQUIRED |
| Leather apron | Full coverage | REQUIRED |
| Safety boots | Steel toe, EH rated | REQUIRED |
| Flame-resistant clothing | FR-rated coverall | REQUIRED (SPS) |

"REQUIRED" in `#E05C5C`. "(SPS)" note in `#E8A020`.

---

### ZONE 5 -- Emergency Response Strip

**Section label:** `EMERGENCY RESPONSE -- 4 SCENARIOS` -- Y: 28.7".

**BLOCK F -- Four Cards**

| Card | Problem | Action |
|---|---|---|
| 1 | ETHANOL FIRE | CO2 or dry chemical extinguisher; evacuate booth; do NOT use water |
| 2 | FUME EXPOSURE | Move to fresh air; administer O2 if available; seek medical attention |
| 3 | ARC FLASH BURN | Cool burn with water; do not remove clothing stuck to skin; call EMS |
| 4 | NANO-DUST RELEASE | Evacuate area; wet-wipe cleanup only (no dry sweep); HEPA vacuum |

---

### ZONE 6 -- Footer

Standard. Title: `Safety & PPE -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol 5A; OSHA/ACGIH exposure limits. Nano-particle TLVs are under development -- apply precautionary principle. Consult your safety officer and applicable regulations.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Safety PPE SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #540 -- Construction Workup v1.0 -- 2026-04-26*
