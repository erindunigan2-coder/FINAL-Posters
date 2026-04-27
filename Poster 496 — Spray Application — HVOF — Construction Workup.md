---
Project: Plating Posters Inc
Poster Number: 496
Title: "Spray Application -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 8)"
Technical Source: HVOF spray application technique. Preheat to 60-100 degC (less than APS). Build thickness 15-30 um per pass for WC-Co. Chrome replacement target 200-400 um. Substrate temp < 150 degC. Coating properties table comparing HVOF WC-12Co vs. hard chrome.
Process Scope: HVOF thermal spray -- spray application technique and coating buildup
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #496 -- Construction Workup
## Spray Application -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of the HVOF process -- where the WC-Co meets the steel. The hero visual is an HVOF coating cross-section showing the characteristic dense, low-porosity structure with uniformly distributed carbide particles. Supporting content: a head-to-head properties comparison of HVOF WC-12Co vs. hard chrome plating (the benchmark), application sequence, and defect guide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **HVOF coating cross-section (Block B -- HERO):** Dense single-layer cross-section with carbide distribution visible.
2. **HVOF vs. Hard Chrome properties table (Block C):** 10-property comparison -- the definitive reference.
3. **Application sequence (Block D):** 6-step spray application flow.
4. **Defect guide (Block E):** 5 common HVOF-specific defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Emerald)
ZONE 3 -- COATING CROSS-SECTION + PROPERTIES HERO (4.2"--15.5" / ~11.3")
  Block B: HVOF WC-Co cross-section
  Block C: HVOF vs. Hard Chrome properties table
ZONE 4 -- APPLICATION SEQUENCE (15.5"--22.0" / ~6.5")
  Block D: 6-step spray application flow
ZONE 5 -- DEFECT GUIDE (22.0"--28.5" / ~6.5")
  Block E: 5 common HVOF application defects
ZONE 6 -- TEMPERATURE MANAGEMENT (28.5"--32.5" / ~4.0")
  Block F: Substrate temperature callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- Where Carbide Meets Steel -- Stage 7 of 10` -- 32 pt `#27AE60`. Y: 1.4".
**Tagline:** `15-30 microns per pass. Less than 1% porosity. Harder than hard chrome. This is precision coating at supersonic speed.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule card (right):**
- Big number: `15-30` -- 64 pt `#27AE60`
- Label: `microns per pass -- WC-Co, layer by layer` -- 14 pt `#F0EDE8`

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted (Emerald). Others dimmed.

---

### ZONE 3 -- Coating Cross-Section + Properties (HERO)

**Section label:** `HVOF WC-Co -- THE BENCHMARK COATING` -- Y: 4.4".

**BLOCK B -- HVOF Coating Cross-Section (top half)**

Y: 5.0" to 9.0". Centered, W: 22.0".

Horizontal layered cross-section (bottom to top):
- **Substrate** (bottom layer): Rectangle, H: 1.5", fill `#3A4055`, border 1 pt `#C8D0D8`. Label: `SUBSTRATE (e.g., 4340 steel, landing gear)` JetBrains Mono 14 pt `#C8D0D8`.
- **Grit blast profile**: Jagged line between substrate and coating, stroke 2 pt `#E8A020`.
- **HVOF WC-Co coating**: Rectangle, H: 1.5", fill `#E8A020` at 25%, border 1 pt `#E8A020`. Scattered small dots inside representing WC carbide particles in Co matrix. Label: `WC-12Co COATING -- 200-400 um (chrome replacement)` JetBrains Mono 13 pt `#E8A020`.
- **Ground surface**: Top edge, smooth line. Annotation: `Ground to Ra 0.1-0.4 um -- matches hard chrome finish`.

Right side annotations:
- `Porosity: < 1% (typically < 0.5%)`
- `Hardness: 1100-1400 HV300`
- `Bond strength: > 70 MPa`
- `Oxide content: < 0.5%`

Note below cross-section: `HVOF WC-Co is a SINGLE-LAYER coating -- no bond coat required. The high particle velocity creates direct mechanical and metallurgical interlocking with the substrate.` Inter Regular 13 pt `#F0EDE8` at 70%.

**BLOCK C -- HVOF vs. Hard Chrome Properties Table (bottom half)**

Y: 9.5" to 15.3". Full width.

Title: `HEAD-TO-HEAD: HVOF WC-12Co vs. HARD CHROME` Barlow SemiBold 18 pt `#F0EDE8`.

| Property | HVOF WC-12Co | Hard Chrome | Winner |
|---|---|---|---|
| Hardness | 1100-1400 HV300 | 800-1000 HV | HVOF |
| Porosity | < 1% (< 0.5% typical) | < 1% (micro-cracked) | Tie |
| Bond strength (ASTM C633) | > 70 MPa | 40-80 MPa | HVOF |
| Wear rate (ASTM G65) | 1-5 x 10^-7 mm3/Nm | 5-15 x 10^-7 mm3/Nm | HVOF |
| Fatigue life impact | Neutral to beneficial (compressive) | Detrimental (tensile; H2 embrittlement) | HVOF |
| Surface finish (ground) | Ra 0.1-0.4 um | Ra 0.1-0.4 um | Tie |
| Max service temp | 500 degC | 400 degC | HVOF |
| Cr(VI) exposure | ZERO | YES (regulated) | HVOF |
| Cost per part | Higher (equipment + powder) | Lower (simpler process) | Chrome |
| Thickness uniformity | Excellent (robot-controlled) | Good (current distribution dependent) | HVOF |

Header: fill `#3A4055`. Winner column: `HVOF` in `#27AE60`, `Chrome` in `#E05C5C`, `Tie` in `#C8D0D8`.
Data: JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 4 -- Application Sequence

**Section label:** `6-STEP SPRAY APPLICATION` -- Y: 15.7".

**BLOCK D -- 6-Step Application Sequence**

Y: 16.3" to 21.8". Six horizontal step cards.

| Step | Action | Key Detail |
|---|---|---|
| 1. Preheat | Heat substrate with HVOF gun (no powder) | Target: 60-100 degC; less preheat than APS |
| 2. First passes | Begin coating buildup; verify spray pattern | 15-30 um per pass for WC-Co |
| 3. Interpass cooling | Compressed air jets between passes | Keep substrate < 150 degC at all times |
| 4. Thickness check | In-process measurement on sacrificial tabs | Eddy current or contact gauge |
| 5. Build to target | Continue passes to target thickness | Chrome replacement: 200-400 um (over-dimension) |
| 6. Final verification | Confirm thickness, uniformity, and visual quality | Compare deposition rate to qualification data |

Each step: Rounded rect, W: 23.0", H: 0.8", fill alternating `#1E2435` / `#252B3D`, left accent 0.06" `#27AE60`.

---

### ZONE 5 -- Defect Guide

**Section label:** `5 DEFECTS TO WATCH FOR DURING HVOF SPRAY` -- Y: 22.2".

**BLOCK E -- 5 Defect Cards**

Y: 22.9" to 28.3". Five cards in a grid (3 top + 2 bottom).

| Defect | Cause | Fix | Color |
|---|---|---|---|
| DECARBURIZATION (low hardness) | Flame too hot (oxygen-rich); excessive dwell time | Go fuel-rich; reduce standoff; increase traverse | `#E05C5C` |
| SUBSTRATE OVERHEATING | Traverse too slow; insufficient air cooling | Increase traverse; add cooling jets | `#E05C5C` |
| DELAMINATION DURING SPRAY | Contaminated interface; residual chrome | Stop; strip; re-clean; re-blast; re-spray | `#E05C5C` |
| ORANGE PEEL TEXTURE | Powder too coarse; standoff too close | Verify powder 5-45 um; increase standoff | `#E8A020` |
| UNEVEN THICKNESS | Robot program error; inconsistent standoff | Check robot program; verify standoff at all positions | `#E8A020` |

Each card: Rounded rect, fill `#1E2435`, left accent 0.06" in defect color.

---

### ZONE 6 -- Temperature Management

**BLOCK F -- Full-Width Banner**

- Rounded rect, fill `#E8A020` at 12%, border 2 pt `#E8A020`

**Main text:** `SUBSTRATE TEMPERATURE MUST STAY BELOW 150 degC` Barlow Condensed ExtraBold 28 pt `#E8A020`.
**Sub-text:** `Compressed air cooling (dry, oil-free) directed at substrate backside. Monitor with IR pyrometer. HVOF's high kinetic energy bonding means less preheat is needed -- but heat still accumulates during multi-pass buildup.` Inter Medium 16 pt `#F0EDE8`.

Substrate temp limits (inline):
- `Low-carbon steel: 150 degC` | `Tool steel (heat-treated): 150 degC` | `Aluminum: 120-150 degC` | `Titanium: 150-200 degC`

---

### ZONE 7 -- Footer

Standard. Title: `Spray Application -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The HVOF vs. Hard Chrome properties table is the flagship visual of this poster and arguably the entire HVOF cluster. This is the table that aerospace engineers, procurement officers, and shop managers need to see. HVOF wins on 8 of 10 properties. Hard chrome wins only on cost -- and regulatory pressure is eroding that advantage. The decarburization defect is HVOF-specific and critical: it is the most common quality failure, and understanding it requires grasping the fuel:O2 ratio (taught on Poster #495).

---

*Alaina -- Poster #496 -- Construction Workup v1.0 -- 2026-04-26*
