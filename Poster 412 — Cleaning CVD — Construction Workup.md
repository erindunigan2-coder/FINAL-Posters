---
Project: Plating Posters Inc
Poster Number: 412
Title: "Cleaning -- CVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 2: CVD, Section 2.4)"
Technical Source: CVD cleaning covering pre-cleaning (ultrasonic alkaline wash), in-furnace hydrogen reduction for oxide removal, furnace cleaning (HCl/Cl2 etch runs), and why contamination tolerance is higher than PVD but still matters.
Process Scope: CVD cleaning (Stage 4 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CVD
  - Cleaning
  - SurfacePrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #412 -- Construction Workup
## Cleaning -- CVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 10. Cleaning for CVD is simpler than PVD because the high-temperature hydrogen atmosphere performs in-situ oxide removal that PVD cannot match. But "simpler" does not mean "optional." Organic contamination produces carbon inclusions in the coating. Particulates create local coating defects. And the furnace itself needs periodic cleaning to prevent buildup from degrading coating quality.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **CVD vs. PVD cleaning comparison (Block B -- HERO):** Side-by-side showing why CVD cleaning is less demanding than PVD, with the in-furnace H2 reduction step as the key differentiator.
2. **Cleaning sequence (Block C):** Step-by-step cleaning protocol for CVD substrates.
3. **Furnace cleaning (Block D):** Periodic HCl/Cl2 etch run protocol for retort maintenance.
4. **Contamination effects (Block E):** What each type of contamination does to the coating.
5. **Common cleaning failures (Block F):** Four failure cards.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.0" / 20.0" / 25.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal -- cleaning)
ZONE 3 -- CVD VS. PVD CLEANING COMPARISON / HERO (4.2"--14.0" / ~9.8")
ZONE 4 -- CLEANING SEQUENCE + FURNACE CLEANING (14.0"--20.0" / ~6.0")
ZONE 5 -- CONTAMINATION EFFECTS (20.0"--25.5" / ~5.5")
ZONE 6 -- COMMON CLEANING FAILURES (25.5"--32.5" / ~7.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `CVD -- Stage 4 of 10 -- Pre-Clean, H2 Reduction, and Furnace Maintenance` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `CVD's high-temperature hydrogen atmosphere cleans what your ultrasonic bath cannot -- surface oxides are reduced in situ. But organic contamination still becomes carbon inclusions. Clean the parts AND clean the furnace.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts prepped, edges treated (Stage 3) --> After: Parts cleaned, ready for loading into furnace`

---

### ZONE 3 -- CVD vs. PVD Cleaning Comparison (HERO)

**Section label:** `WHY CVD CLEANING IS DIFFERENT FROM PVD` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Side-by-Side Comparison (Y: 5.0" to 13.8")**

**Left -- PVD Cleaning (for reference) (X: 0.5", W: 11.0"):**
- Rounded rect H: 8.5", fill `#1E2435`, left accent `#3A4055` (dimmed -- for context only)
- Title: `PVD CLEANING (FOR COMPARISON)` Barlow SemiBold 20 pt `#C8D0D8`
- Subtitle: `Extremely demanding -- a monolayer of contamination reduces adhesion by > 50%` Inter Regular 13 pt `#F0EDE8` at 50%

Key points (Inter Regular 14 pt `#F0EDE8` at 60%):
- `8-step cleaning sequence required`
- `Multi-stage ultrasonic (alkaline + solvent + DI)`
- `Water-break test validation`
- `UV fluorescence inspection`
- `In-chamber Ar+ ion etch for final oxide removal`
- `Cleanliness is the #1 cause of PVD adhesion failure`
- `No in-situ chemical cleaning at PVD temps (200-500 C)`

Verdict box: `#3A4055` fill, border 1 pt `#C8D0D8`
- `PVD: Surface cleanliness is EVERYTHING` Inter Medium 14 pt `#C8D0D8`

**Right -- CVD Cleaning (X: 12.0", W: 11.5"):**
- Rounded rect H: 8.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `CVD CLEANING` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `Less demanding -- but still required` Inter Regular 13 pt `#2EC4B6`

Key points (Inter Medium 14 pt `#F0EDE8`):
- `3-4 step pre-cleaning (alkaline wash + DI rinse + dry)`
- `H2 reduction at 900-1050 C removes surface oxides IN SITU`
- `Chemical reaction provides inherent surface activation`
- `Contamination tolerance is higher because:`
- `  -- Thicker coatings (3-20 um) can accommodate minor defects`
- `  -- Chemical bonding (not physical) at substrate/coating interface`
- `  -- High-temp H2 thermally decomposes most organics`
- `BUT: Organic contamination still causes carbon inclusions`
- `AND: Particulates still create local coating defects`

Verdict box: `#2EC4B6` at 15% fill, border 1 pt `#2EC4B6`
- `CVD: Simpler cleaning, but organic contamination = carbon defects` Inter Medium 14 pt `#2EC4B6`

**Center insight (spanning both columns, Y: 13.3" to 13.8"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `The key difference: PVD has no in-situ cleaning mechanism. CVD's H2 atmosphere at 900+ C reduces oxides and decomposes many contaminants -- it's a built-in cleaning step.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Cleaning Sequence + Furnace Cleaning

**Two-column layout (Y: 14.0" to 19.8"):**

**Left -- Substrate Cleaning Sequence (X: 0.5", W: 11.0"):**
- Rounded rect H: 5.6", fill `#1E2435`, left accent `#2EC4B6`
- Title: `PRE-COATING CLEANING PROTOCOL` Barlow SemiBold 20 pt `#2EC4B6`

Steps (Inter Medium 14 pt `#F0EDE8`, numbered with JetBrains Mono step numbers in `#2EC4B6`):

| Step | Description | Details |
|---|---|---|
| 1 | Ultrasonic alkaline wash | pH 10-12, 50-60 C, 5-10 min, 40 kHz |
| 2 | DI water rinse | Cascade rinse, > 10 Mohm-cm water |
| 3 | Hot air dry | Filtered hot air, 80-100 C |
| 4 | In-furnace H2 reduction | 900-1050 C, H2 flow, 15-30 min soak |

Data: JetBrains Mono 12 pt `#F0EDE8`. Labels: Inter Medium 12 pt.

Note: `Step 4 happens automatically during the heat-up and stabilization stages (Stages 5-6). No separate cleaning station required.` Inter Regular 12 pt `#F0EDE8` at 70%

**Right -- Furnace Cleaning (X: 12.0", W: 11.5"):**
- Rounded rect H: 5.6", fill `#1E2435`, left accent `#E8A020`
- Title: `FURNACE MAINTENANCE CLEANING` Barlow SemiBold 20 pt `#E8A020`

Key points (Inter Medium 14 pt `#F0EDE8`):
- `Frequency: Every 20-50 production runs`
- `Method: HCl or Cl2 gas etch at process temperature`
- `Purpose: Remove coating buildup from retort walls, gas inlet tubes, and fixtures`
- `Duration: 2-4 hours at 1000 C`
- `Exhaust: ALL etch gases through scrubber`

Warning:
- `HCl/Cl2 etch runs generate large volumes of corrosive gas -- ensure scrubber capacity is adequate before running` Inter Medium 12 pt `#E05C5C`

Buildup consequences:
- `Coating buildup on retort walls changes gas flow patterns -> non-uniform coatings`
- `Flaking from walls can contaminate parts`
- `Excessive buildup reduces effective chamber volume`
Inter Regular 12 pt `#F0EDE8` at 70%

---

### ZONE 5 -- Contamination Effects

**Section label:** `WHAT CONTAMINATION DOES TO CVD COATINGS` -- Y: 20.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK E -- Contamination Table (Y: 20.8" to 25.3")**

| Contaminant | Source | Effect on Coating | Severity |
|---|---|---|---|
| Organic residue (oil, fingerprints) | Handling without gloves; cutting fluid residue | Carbon inclusions in coating; local porosity | Medium |
| Surface oxides (native oxide) | Normal atmospheric exposure | Removed by H2 reduction -- no issue if furnace protocol followed | Low |
| Particulate (grinding dust, lint) | Grinding, shop air, dirty storage | Local coating defects; thickness variation | Medium |
| Water / moisture | Inadequate drying | Increased H2 consumption; possible oxide formation during heat-up | Low-Medium |
| Metallic contamination (Fe, Cu) | Cross-contamination from other processes | Diffusion into coating at CVD temperatures; composition change | High |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`. Severity: color-coded (Low `#27AE60`, Medium `#E8A020`, High `#E05C5C`). Alternating rows.

Bottom callout:
- `Surface oxides are the one contamination type CVD handles automatically. Everything else requires pre-cleaning.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 6 -- Common Cleaning Failures

**Section label:** `CLEANING FAILURES -- WHAT GOES WRONG` -- Y: 25.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Failure Cards (Y: 26.3" to 32.3")**

Each card: Rounded rect W: 5.5", H: 5.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Failure | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CARBON INCLUSIONS | Organic contamination not removed by pre-cleaning | Ultrasonic alkaline wash; verify oil-free handling |
| 2 | 6.33" | COATING BUILDUP ON RETORT | Furnace cleaning schedule skipped | Maintain 20-50 run etch schedule; track run count |
| 3 | 12.16" | NON-UNIFORM COATING | Particulate on parts created local defects; retort buildup | Clean parts + clean furnace; inspect retort condition |
| 4 | 18.0" | METALLIC CROSS-CONTAMINATION | Parts stored or handled with other materials | Dedicated storage for CVD parts; clean handling trays |

Interior per card:
- Failure: Barlow SemiBold 15 pt `#E05C5C`
- Cause: Inter Regular 13 pt `#F0EDE8`
- Fix: Inter Medium 13 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- CVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning CVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The CVD vs. PVD cleaning comparison is the hero because it establishes the most important conceptual difference: CVD has a built-in cleaning mechanism (H2 reduction) that PVD lacks. This is why PVD requires eight cleaning steps while CVD needs three to four. The furnace cleaning section is included because retort maintenance is chronically neglected in real production environments -- operators focus on part cleaning but forget the furnace, and coating quality degrades gradually.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #412 -- Construction Workup v1.0*
*2026-04-26*
