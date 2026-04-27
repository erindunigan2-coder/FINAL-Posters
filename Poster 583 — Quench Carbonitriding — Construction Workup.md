---
Project: Plating Posters Inc
Poster Number: 583
Title: "Quench -- Carbonitriding"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 3: Carbonitriding, Section 3.6 / Process 1 Sections 1.6)"
Technical Source: Oil quench for carbonitriding. Quench media selection, H-values, oil temperature, agitation, and the critical advantage of nitrogen in lowering the critical cooling rate.
Process Scope: Carbonitriding quench -- oil quench, polymer quench, quench severity
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Carbonitriding
  - Quench
  - OilQuench
  - HeatTreatment
  - ConstructionWorkup
---

# Poster #583 -- Construction Workup
## Quench -- Carbonitriding

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The quench transforms the carbon-nitrogen enriched austenite into hard martensite. What makes carbonitriding special: nitrogen lowers the critical cooling rate so dramatically that even a moderate oil quench fully hardens the case on low-hardenability steels like 1018. This poster covers quench media, severity (H-values), oil maintenance, and the nitrogen advantage.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Quench tank cross-section hero (Block B):** Tank showing parts entering oil, agitation system, temperature zones. Built with rectangles and arrows.
2. **Quench media comparison table (Block D):** Oil vs. polymer with H-values.
3. **The nitrogen advantage callout (Block E):** Visual explanation of why nitrogen lowers critical cooling rate.
4. **Oil maintenance checklist (Block F):** Testing schedule and parameters.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 13.5" / 19.5" / 26.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- QUENCH TANK HERO (2.9"--13.5" / ~10.6")
  Block B: Tank cross-section with parts, agitation, temperature
ZONE 3 -- QUENCH MEDIA TABLE (13.5"--19.5" / ~6.0")
  Block D: Media comparison with H-values
ZONE 4 -- THE NITROGEN ADVANTAGE (19.5"--26.0" / ~6.5")
  Block E: Why carbonitriding quench is different
ZONE 5 -- OIL MAINTENANCE (26.0"--32.5" / ~6.5")
  Block F: Oil testing schedule
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `QUENCH` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Carbonitriding -- Nitrogen Makes the Quench Work on Steels That Shouldn't Harden` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Direct oil quench from process temperature. Nitrogen buys you the hardenability that the steel alloy doesn't have.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Quench Tank (HERO)

**Section label:** `THE OIL QUENCH TANK` -- Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Tank Cross-Section**

Y: 3.8" to 13.0".

**Tank body:**
- Rounded rect, X: 2.0", Y: 4.5", W: 20.0", H: 7.5"
- Fill: `#E8A020` at 12% (oil)
- Border: 3 pt `#C8D0D8`
- Label: `QUENCH OIL` Barlow SemiBold 16 pt `#E8A020`

**Parts entering oil (top center):**
- 3 rounded rects (parts) at top of tank, partially submerged
- Fill: `#E05C5C` at 30% (hot), border 2 pt `#E05C5C`
- Label above: `PARTS AT 1400--1600 F` Barlow SemiBold 14 pt `#E05C5C`
- Arrow pointing down: `Direct drop from furnace` Inter Regular 12 pt

**Oil temperature zones:**
- Upper zone label: `Vapor blanket (initial)` Inter Regular 11 pt `#E8A020` at 60%
- Middle zone label: `Nucleate boiling (max cooling)` Inter Regular 11 pt `#E8A020`
- Lower zone label: `Convection (final)` Inter Regular 11 pt `#E8A020` at 60%

**Agitation system:**
- 2 propeller icons (circles with blades) at bottom of tank
- Label: `AGITATION PROPELLERS` JetBrains Mono 12 pt `#C8D0D8`
- `Agitation increases H-value by 50--100%` Inter Regular 11 pt `#F0EDE8` at 70%

**Oil parameters (right side callout, X: 15.0", Y: 5.0"):**
- Rounded rect, W: 6.5", H: 3.0", fill `#1E2435`, left accent `#E8A020`
- `Oil temp: 120--180 F (50--80 C)` JetBrains Mono 14 pt `#E8A020`
- `Flash point: monitor weekly` Inter Regular 12 pt `#F0EDE8`
- `Water content: < 0.1%` JetBrains Mono 12 pt `#F0EDE8`
- `Viscosity: per supplier spec` Inter Regular 12 pt `#F0EDE8` at 70%

**Transformation callout (bottom of tank area, Y: 11.5"):**
- `Austenite (FCC, soft) -> Martensite (BCT, hard) -- the quench is the transformation` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 3 -- Quench Media Table

**Section label:** `QUENCH MEDIA -- SELECTING SEVERITY` -- Y: 13.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Media Comparison**

Y: 14.3" to 19.3". Columns: Medium (5.5") | H-Value (3.0") | Temperature (3.5") | Best For (5.5") | Notes (5.5")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 1.0".

| Medium | H-Value | Temp | Best For | Notes |
|---|---|---|---|---|
| Fast quench oil (agitated) | 0.50--0.70 | 120--180 F | Standard production | Most common for CN |
| Fast quench oil (still) | 0.25--0.35 | 120--180 F | Distortion-sensitive parts | Lower severity |
| Polymer quench (PAG) | 0.20--0.60 | 75--120 F | Thin sections; clean process | Adjustable by concentration (5--25% PAG) |

Data: JetBrains Mono Regular, 12 pt. Notes: Inter Regular 12 pt.

Bottom callout: `Because nitrogen lowers the critical cooling rate, even a moderate oil quench (H = 0.35) can fully harden the case on 1018 steel. This is NOT possible with carburizing alone.` -- Inter Medium, 14 pt, `#27AE60`.

---

### ZONE 4 -- The Nitrogen Advantage

**Section label:** `THE NITROGEN ADVANTAGE -- WHY CARBONITRIDING WORKS` -- Y: 19.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Nitrogen Advantage Callout**

Y: 20.3" to 25.8". Full-width panel.

Rounded rect, X: 0.5", W: 23.0", H: 5.3", fill `#1E2435`, left accent `#27AE60` 0.06".

**Two-column interior:**

**Left column (X: 1.0", W: 10.5") -- Without Nitrogen (Carburizing Only):**
- Title: `CARBURIZING 1018 STEEL` -- Barlow SemiBold, 18 pt, `#E8A020`
- `Surface carbon: 0.80% C after carburizing`
- `Oil quench (H = 0.50)`
- `Result: pearlite + bainite (SOFT)` -- `#E05C5C`
- `1018 lacks Cr, Mo, Ni for hardenability`
- `The alloy cannot be quenched fast enough`
- `Case hardness: 30--40 HRC (FAIL)` JetBrains Mono 14 pt `#E05C5C`

**Right column (X: 12.5", W: 10.5") -- With Nitrogen (Carbonitriding):**
- Title: `CARBONITRIDING 1018 STEEL` -- Barlow SemiBold, 18 pt, `#27AE60`
- `Surface: 0.70% C + 0.30% N after CN`
- `Same oil quench (H = 0.50)`
- `Result: MARTENSITE (HARD)` -- `#27AE60`
- `Nitrogen lowers the critical cooling rate`
- `Even moderate quench achieves full transformation`
- `Case hardness: 58--63 HRC (PASS)` JetBrains Mono 14 pt `#27AE60`

**Center divider:** Vertical line, 2 pt `#3A4055`, with arrow pointing right. Label: `+ NITROGEN` Barlow SemiBold 16 pt `#2EC4B6`.

---

### ZONE 5 -- Oil Maintenance

**Section label:** `QUENCH OIL MAINTENANCE -- KEEP THE OIL WORKING` -- Y: 26.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Oil Testing Schedule**

Y: 26.8" to 32.3". 5-row table.

Columns: Test (5.5") | Frequency (3.5") | Target (5.0") | Why (9.0")

Header row: fill `#3A4055`. Barlow SemiBold, 14 pt.
Data rows: alternating fills, H: 0.9".

| Test | Frequency | Target | Why |
|---|---|---|---|
| Flash point | Weekly | > 300 F (per oil spec) | Below flash point = fire risk |
| Viscosity | Monthly | Per supplier spec | Degraded oil quenches inconsistently |
| Water content | Weekly | < 0.1% | Water in oil = steam explosion risk |
| Cooling curve | Quarterly | Per ASTM D6200 | Verifies actual quench severity |
| Particulate / sludge | Monthly | Clear, no sediment | Sludge insulates parts; uneven quench |

Data: JetBrains Mono Regular, 12 pt. Why: Inter Regular 12 pt.

---

### ZONE 6 -- Footer

Standard footer. Title: `Quench -- Carbonitriding`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Quench Carbonitriding -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The nitrogen advantage panel (Zone 4) is the single most important visual on this poster. It answers the question every metallurgist asks: "Why not just carburize?" The side-by-side comparison of 1018 with and without nitrogen makes the value proposition undeniable. The quench tank hero should show the three cooling stages (vapor blanket, nucleate boiling, convection) as labeled zones within the oil.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #583 -- Construction Workup v1.0*
*2026-04-26*
