---
Project: Plating Posters Inc
Poster Number: 486
Title: "Spray Application -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 8)"
Technical Source: APS spray application technique including preheat, bond coat, multi-pass buildup, interpass cooling, thickness monitoring, and common application defects. TBC layup structure (MCrAlY + 7YSZ).
Process Scope: Atmospheric plasma spray -- spray application technique and coating buildup
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #486 -- Construction Workup
## Spray Application -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of the APS process (the main event -- where coating meets substrate). This poster covers the actual spraying: preheat, bond coat, multi-pass topcoat buildup, interpass cooling, and in-process thickness monitoring. The hero visual is a TBC layup cross-section showing bond coat + ceramic topcoat.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **TBC layup cross-section (Block B -- HERO):** Horizontal cross-section showing substrate, bond coat (MCrAlY), and ceramic topcoat (YSZ) with labeled thicknesses.
2. **Application sequence (Block C):** 6-step spray application flow.
3. **Defect guide (Block D):** 5 common defects during application with causes and fixes.
4. **Thickness reference (Block E):** Typical thickness ranges by application type.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Emerald)
ZONE 3 -- TBC LAYUP + APPLICATION SEQUENCE HERO (4.2"--15.5" / ~11.3")
  Block B: TBC cross-section
  Block C: 6-step application sequence
ZONE 4 -- DEFECT GUIDE (15.5"--22.0" / ~6.5")
  Block D: 5 common application defects
ZONE 5 -- THICKNESS REFERENCE (22.0"--28.5" / ~6.5")
  Block E: Thickness by application type + pass-per-layer data
ZONE 6 -- INTERPASS COOLING CALLOUT (28.5"--32.5" / ~4.0")
  Block F: Temperature management rules
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 80 pt `#F0EDE8`.
**Subheading:** `Plasma Spray (APS) -- Where Coating Meets Substrate -- Stage 7 of 10` -- 32 pt `#27AE60`. Y: 1.4".
**Tagline:** `Build it layer by layer. 20-50 microns per pass. Every splat counts.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `20-50` -- 64 pt `#27AE60`
- Label: `microns per pass -- patience builds quality` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted (Emerald). Others dimmed.

---

### ZONE 3 -- TBC Layup + Application Sequence (HERO)

**Section label:** `COATING ARCHITECTURE -- BUILD FROM THE BOTTOM UP` -- Y: 4.4".

**BLOCK B -- TBC Cross-Section (top half)**

Y: 5.0" to 9.5". Centered, W: 22.0".

Horizontal layered cross-section (bottom to top):
- **Substrate** (bottom layer): Rectangle, H: 1.5", fill `#3A4055`, border 1 pt `#C8D0D8`. Label: `SUBSTRATE (e.g., Ni superalloy)` JetBrains Mono 14 pt `#C8D0D8`.
- **Grit blast profile**: Jagged line between substrate and bond coat, stroke 2 pt `#E8A020`.
- **Bond coat**: Rectangle, H: 0.8", fill `#E8A020` at 30%, border 1 pt `#E8A020`. Label: `BOND COAT -- MCrAlY or NiAl` JetBrains Mono 13 pt `#E8A020`. Thickness: `50-150 um`.
- **Ceramic topcoat**: Rectangle, H: 1.5", fill `#2EC4B6` at 20%, border 1 pt `#2EC4B6`. Label: `TOPCOAT -- 7YSZ (yttria-stabilized zirconia)` JetBrains Mono 13 pt `#2EC4B6`. Thickness: `250-500 um`.
- **Surface**: Top edge with annotation `As-sprayed Ra: 5-15 um`.

Right side annotations:
- Total TBC system: `300-650 um total`
- Arrow spanning both layers: `Thermal gradient: 1000+ degC across this stack in service`

Note below cross-section: `Not all APS coatings require a bond coat. Single-layer ceramic and metallic coatings are common. The TBC layup shown here is the flagship APS application.` Inter Regular 13 pt `#F0EDE8` at 70%.

**BLOCK C -- 6-Step Application Sequence (bottom half)**

Y: 10.0" to 15.3". Six horizontal step cards.

| Step | Action | Key Detail |
|---|---|---|
| 1. Preheat | Heat substrate with plasma gun (no powder) | Target: 80-120 degC; improves adhesion |
| 2. Bond coat | Spray metallic bond coat (MCrAlY, NiAl) | 50-150 um; required for ceramic topcoats |
| 3. Topcoat passes | Build ceramic topcoat in multiple passes | 20-50 um per pass; robot-controlled |
| 4. Interpass cooling | Air jets between passes as needed | Keep substrate below temp limit |
| 5. Thickness check | In-process measurement on sacrificial tabs | Eddy current or contact gauge |
| 6. Final passes | Complete to target thickness | Verify uniformity across part |

Each step: Rounded rect, W: 23.0", H: 0.8", fill alternating `#1E2435` / `#252B3D`, left accent 0.06" `#27AE60`.

---

### ZONE 4 -- Defect Guide

**Section label:** `5 DEFECTS TO WATCH FOR DURING SPRAY` -- Y: 15.7".

**BLOCK D -- 5 Defect Cards**

Y: 16.3" to 21.8". Five cards in a grid (3 top + 2 bottom, or 5 in a row with smaller width).

| Defect | Cause | Fix | Color |
|---|---|---|---|
| UNMELTED PARTICLES ("spitting") | Power too low or standoff too far | Increase power; reduce standoff | `#E05C5C` |
| SUBSTRATE OVERHEATING | Traverse too slow; insufficient cooling | Increase traverse; add air cooling | `#E05C5C` |
| DELAMINATION DURING SPRAY | Contaminated surface or insufficient profile | Stop; strip; re-blast; re-spray | `#E05C5C` |
| UNEVEN THICKNESS | Inconsistent traverse speed or standoff variation | Check robot program; verify standoff at all positions | `#E8A020` |
| VERTICAL CRACKING (ceramics) | Thermal stress during cooling | May be beneficial (strain tolerance) or detrimental -- consult spec | `#E8A020` |

Each card: Rounded rect, fill `#1E2435`, left accent 0.06" in defect color.

---

### ZONE 5 -- Thickness Reference

**Section label:** `TYPICAL COATING THICKNESS BY APPLICATION` -- Y: 22.2".

**BLOCK E -- Thickness Table**

| Application | Bond Coat | Topcoat | Total | Passes (approx) |
|---|---|---|---|---|
| TBC (gas turbine) | MCrAlY 75-150 um | 7YSZ 250-500 um | 325-650 um | 15-30 |
| Ceramic wear (Al2O3) | NiAl 50-125 um | Al2O3 200-400 um | 250-525 um | 12-25 |
| Chrome oxide wear | NiAl 50-100 um | Cr2O3 150-300 um | 200-400 um | 10-20 |
| Metallic wear (NiCr) | None (direct) | NiCr 200-500 um | 200-500 um | 10-25 |
| Abradable (clearance) | Optional | Al-polyester 500-2000 um | 500-2000 um | 25-100 |

Data: JetBrains Mono 12 pt. Thickness values in `#27AE60`.

---

### ZONE 6 -- Interpass Cooling Callout

**BLOCK F -- Full-Width Banner**

- Rounded rect, fill `#E8A020` at 12%, border 2 pt `#E8A020`

**Main text:** `INTERPASS COOLING IS NOT OPTIONAL` Barlow Condensed ExtraBold 28 pt `#E8A020`.
**Sub-text:** `Monitor substrate temperature with IR pyrometer. Never exceed substrate limit. Air jets (dry, oil-free) directed at backside.` Inter Medium 16 pt `#F0EDE8`.

Substrate temp limits (inline):
- `Low-carbon steel: 150-200 degC` | `Aluminum: 120-150 degC` | `Titanium: 150-200 degC` | `Mg alloys: 100-120 degC`

---

### ZONE 7 -- Footer

Standard. Title: `Spray Application -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The TBC cross-section is the signature visual of this poster. Gas turbine TBCs are the most famous APS application -- a plating shop audience will immediately understand the parallels to layered plating (like nickel/chrome or zinc/passivate). The "20-50 microns per pass" discipline is the key takeaway: you cannot rush thermal spray. Layer by layer, pass by pass.

---

*Alaina -- Poster #486 -- Construction Workup v1.0 -- 2026-04-26*
