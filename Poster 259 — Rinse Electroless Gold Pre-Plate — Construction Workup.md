---
Project: Plating Posters Inc
Poster Number: 259
Title: "Rinse -- Electroless Gold -- Pre-Plate"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 6: Electroless Gold)"
Process Scope: Pre-plate rinse for electroless gold (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessGold
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ENIG
---

# Poster #259 -- Construction Workup
## Rinse -- Electroless Gold -- Pre-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This is the rinse between activation (or EN plating for ENIG) and the gold bath. For ENIG and ENEPIG lines, this rinse removes EN bath drag-out -- hypophosphite and nickel ions -- that would contaminate the gold bath. This is the single most economically critical rinse in the entire gold process: gold chemistry is expensive ($80-100+ per gram of gold), and contamination from drag-in shortens bath life, degrades deposit quality, and wastes precious metal. For autocatalytic gold, this rinse removes activation chemistry (PdCl2/HCl) that would destabilize the reducing agent system.

Hero visual: rinse tank cross-section with drag-in contamination pathway diagram showing exactly what gets carried into the gold bath if rinsing is inadequate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Contamination pathway diagram -- what EN drag-out does to the gold bath.
2. **ENIG vs. autocatalytic rinse parameters (Block D):** Two-path comparison -- different contamination concerns.
3. **Gold recovery economics callout (Block E):** Why a dedicated gold recovery rinse before the main rinse pays for itself.
4. **Defect grid (Block F):** 4 rinse-related gold plating defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE TANK CROSS-SECTION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ENIG vs. AUTOCATALYTIC RINSE PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- GOLD RECOVERY ECONOMICS (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Gold -- Stage 4 of 8 -- Pre-Plate` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The most expensive bath on the line deserves the cleanest rinse. Every contaminant you carry in costs gold.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated or EN-plated surface  -->  After: Clean surface ready for gold deposition`

---

### ZONE 3 -- Rinse Tank Cross-Section Hero

**Section label:** `WHAT HAPPENS WHEN DRAG-IN REACHES THE GOLD BATH` -- Y: 4.4".

**BLOCK B -- Contamination Pathway Diagram**

Y: 5.0" to 14.0".

**Three-panel horizontal layout:**

**Panel 1 -- Source (X: 0.5", Y: 5.0", W: 7.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `DRAG-OUT SOURCES` Barlow SemiBold 18 pt `#E8A020`
- ENIG path content:
  - `EN bath drag-out contains:` Inter Medium 14 pt `#F0EDE8`
  - `Ni2+ ions (4-6 g/L in bath)` JetBrains Mono 13 pt `#F0EDE8`
  - `Hypophosphite (NaH2PO2)` JetBrains Mono 13 pt `#F0EDE8`
  - `Orthophosphite (aging byproduct)` JetBrains Mono 13 pt `#F0EDE8`
  - `Complexants (citric/lactic acid)` JetBrains Mono 13 pt `#F0EDE8`
  - `pH 4.6-5.2 acid solution` JetBrains Mono 13 pt `#F0EDE8`
- Autocatalytic path:
  - `Activation drag-out contains:` Inter Medium 14 pt `#F0EDE8`
  - `PdCl2 / HCl residues` JetBrains Mono 13 pt `#F0EDE8`
  - `Chloride ions` JetBrains Mono 13 pt `#F0EDE8`

**Panel 2 -- Rinse (X: 8.0", Y: 5.0", W: 7.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `THE RINSE` Barlow SemiBold 18 pt `#2EC4B6`
- Visual: simplified cross-section of counterflow rinse tank
  - Two cascading chambers with arrows showing water flow direction
  - Parts rack in first chamber
  - DI water inlet arrow at clean end
  - Overflow drain at dirty end
- Parameters inside visual:
  - `DI counterflow -- 2 stage minimum` Inter Medium 14 pt `#F0EDE8`
  - `Ambient temperature` JetBrains Mono 13 pt `#F0EDE8`
  - `30-60 seconds per stage` JetBrains Mono 13 pt `#F0EDE8`
  - `Target: <20 uS/cm final rinse` JetBrains Mono 13 pt `#2EC4B6`

**Panel 3 -- Consequence (X: 16.0", Y: 5.0", W: 7.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent `#E05C5C` 4 pt
- Title: `IF DRAG-IN IS NOT REMOVED` Barlow SemiBold 18 pt `#E05C5C`
- Content:
  - `Hypophosphite in gold bath:` Inter Medium 14 pt `#F0EDE8`
  - `Reduces Au3+ uncontrollably` Inter Regular 13 pt `#E05C5C`
  - `Causes spontaneous gold precipitation` Inter Regular 13 pt `#E05C5C`
  - `Wastes gold at $80-100+/gram` Inter Regular 13 pt `#E05C5C`
  - `Nickel in gold bath:` Inter Medium 14 pt `#F0EDE8`
  - `Contaminates gold deposit` Inter Regular 13 pt `#E05C5C`
  - `Chloride in gold bath:` Inter Medium 14 pt `#F0EDE8`
  - `Attacks gold complexant system` Inter Regular 13 pt `#E05C5C`

**Arrows between panels:** 3 pt `#3A4055`, right-pointing.

---

### ZONE 4 -- ENIG vs. Autocatalytic Rinse Parameters

**Section label:** `RINSE REQUIREMENTS BY GOLD PROCESS TYPE` -- Y: 14.7".

**Two callout boxes (Y: 15.3" to 20.3"):**

**Left -- ENIG/ENEPIG Rinse (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ENIG / ENEPIG PRE-GOLD RINSE` Barlow SemiBold 18 pt `#E8A020`

| Parameter | Value |
|---|---|
| Type | DI counterflow, 2-3 stages |
| Temperature | Ambient (18-30 C) |
| Time | 30-60 seconds per stage |
| Conductivity target | <20 uS/cm in final rinse |
| Water quality | DI or RO -- municipal water adds chloride |
| Critical concern | Hypophosphite drag-in causes uncontrolled Au reduction |
| Transfer note | Minimize air exposure -- EN surface oxidizes rapidly |

Data: JetBrains Mono 13 pt `#F0EDE8`. Labels: Inter Medium 13 pt `#F0EDE8` at 60%.

**Right -- Autocatalytic Gold Rinse (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `AUTOCATALYTIC GOLD PRE-PLATE RINSE` Barlow SemiBold 18 pt `#27AE60`

| Parameter | Value |
|---|---|
| Type | DI counterflow, 2 stages minimum |
| Temperature | Ambient |
| Time | 30-60 seconds per stage |
| Conductivity target | <20 uS/cm |
| Critical concern | PdCl2/HCl activation residues destabilize reducing agent |
| Chloride concern | Chloride attacks gold sulfite complexant |
| Transfer note | Transfer quickly -- activated surface must remain catalytic |

---

### ZONE 5 -- Gold Recovery Economics

**Section label:** `GOLD RECOVERY -- WHY A DEDICATED RECOVERY RINSE PAYS FOR ITSELF` -- Y: 20.7".

**BLOCK E -- Economics Panel (Y: 21.3" to 26.3")**

**Full-width callout (X: 0.5", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `THE GOLD RECOVERY RINSE` Barlow SemiBold 20 pt `#E8A020`

**Left half (X: 0.8", W: 10.5"):**
- Subtitle: `HOW IT WORKS` Barlow Condensed ExtraBold 16 pt `#F0EDE8` at 50%
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `A stagnant (non-flowing) DI rinse tank placed immediately after the gold bath`
  - `Parts dip into this tank FIRST before the flowing counterflow rinse`
  - `Gold drag-out accumulates in this stagnant rinse over days/weeks`
  - `When gold concentration reaches economically recoverable levels, solution is sent to gold refining`
  - `This is NOT the pre-plate rinse -- this is the post-plate recovery rinse (Stage 6)`

**Right half (X: 12.0", W: 11.0"):**
- Subtitle: `THE ECONOMICS` Barlow Condensed ExtraBold 16 pt `#F0EDE8` at 50%
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `Gold cost: $80-100+ per gram` JetBrains Mono 14 pt `#E8A020`
  - `Typical ENIG drag-out: 20-50 mL per m2 of board area` JetBrains Mono 13 pt `#F0EDE8`
  - `At 1 g/L Au in bath: 0.02-0.05 g gold lost per m2 without recovery`
  - `Recovery rinse captures 60-80% of drag-out gold`
  - `ROI: recovery rinse pays for itself within weeks on a production ENIG line`

- Bottom highlight:
  - Rounded rect, W: 22.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
  - `Every drop of gold solution that goes down the drain is money gone. Capture it.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Defect Grid

**Section label:** `RINSE-RELATED GOLD DEFECTS` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | HAZY / DULL GOLD | `#E05C5C` | Nickel or hypophosphite contamination from EN drag-in | Improve rinse; verify <20 uS/cm; add rinse stage |
| R1C2 | SPONTANEOUS PRECIPITATION | `#E05C5C` | Hypophosphite drag-in reduces Au3+ in bulk solution | Extend rinse time; use DI only; monitor conductivity |
| R2C1 | THIN / INCOMPLETE GOLD | `#E8A020` | Oxidized EN surface from slow transfer or air-dried rinse | Minimize transfer time; keep parts wet throughout |
| R2C2 | GOLD BATH RAPID AGING | `#E8A020` | Cumulative drag-in contamination shortening bath life | Improve rinse discipline; track MTO; consider drag-out reduction |

Card construction: Rounded rect, W: 11.0", H: 2.3", fill `#1E2435`, radius 6, left accent 0.06" (color per defect).

Interior per card:
- Defect name: Barlow SemiBold, 16 pt, defect color
- Cause: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Electroless Gold -- Pre-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for electroless gold pre-plate rinsing. Specific rinse requirements vary by gold bath chemistry and application specification. Consult your process supplier for guidance. Source: General industry knowledge; IPC-4552B; IPC-4556.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electroless Gold Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster serves double duty: it teaches rinse discipline AND introduces the gold recovery economics concept that will be expanded in the post-plate rinse poster (#261). The contamination pathway diagram in Zone 3 is the hero -- it tells a visual story from source (EN drag-out) through the rinse to the consequence (wasted gold, degraded deposits). The economics callout in Zone 5 is a preview; the full recovery rinse gets its own treatment in Poster #261. The distinction between ENIG rinse concerns (hypophosphite, nickel) and autocatalytic rinse concerns (PdCl2, chloride) reinforces the two-process framework established in Poster #258.

---

*Alaina -- Poster #259 -- Construction Workup v1.0 -- 2026-04-26*
