---
Project: Plating Posters Inc
Poster Number: 516
Title: "Spray Application -- Arc Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 4: Arc Spray)"
Process Scope: Arc spray application -- technique, thickness targets per AWS C2.18, coating properties, multi-pass strategy
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - ArcSpray
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS04
---

# Poster #516 -- Construction Workup
## Spray Application -- Arc Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The spraying stage for arc spray. This is where the enormous throughput happens -- up to 30+ kg/hr, the fastest coating application in all of thermal spray. The hero content is the AWS C2.18 thickness specification table for zinc, aluminum, and zinc-aluminum coatings by exposure severity. Key message: first pass at close standoff for maximum bond coat density, then build thickness with subsequent passes. Seal within 4 hours.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Application technique panel (Block B -- HERO):** 6-step spray procedure.
2. **AWS C2.18 thickness table (Block C):** Coating thickness by material and exposure severity.
3. **Coating properties table (Block D):** As-sprayed properties for zinc, aluminum, and stainless.
4. **Seal timing callout (Block E):** Critical 4-hour seal window.
5. **Defect watch strip (Block F):** 4 common application defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- APPLICATION TECHNIQUE / HERO (4.2"--15.5" / ~11.3")
  Block B: 6-step spray procedure
  Block C: AWS C2.18 thickness table
ZONE 4 -- COATING PROPERTIES (15.5"--22.0" / ~6.5")
  Block D: As-sprayed coating properties
ZONE 5 -- SEAL TIMING (22.0"--28.5" / ~6.5")
  Block E: 4-hour seal window + seal coat options
ZONE 6 -- DEFECT WATCH (28.5"--32.5" / ~4.0")
  Block F: 4 defect cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 88 pt `#F0EDE8`.
**Subheading:** `Arc Spray -- Building Corrosion Protection at Production Speed` -- 36 pt `#27AE60` (Emerald).
**Tagline:** `Up to 30+ kg/hr -- the fastest coating rate in thermal spray. One operator, one gun, one shift can protect an entire bridge beam. Speed is the arc spray advantage. Quality comes from discipline.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parameters set, test coupon approved --> After: Coating built to specification, ready for sealing`

---

### ZONE 3 -- Application Technique (HERO)

**Section label:** `SPRAY APPLICATION PROCEDURE` -- Y: 4.4".

**BLOCK B -- 6-Step Application Technique**

Y: 5.0" to 10.5". Six cards in a 3x2 grid. Each card: W: 7.3", H: 2.5", fill `#1E2435`, radius 6, top accent 4 pt `#27AE60`.

| Step | Title | Details |
|---|---|---|
| 1 | PREHEAT TO DEW POINT MARGIN | Substrate must be minimum 10 degC (18 degF) above dew point. For outdoor work, verify with surface thermometer and psychrometer. Cold substrate = condensation = adhesion failure. |
| 2 | FIRST PASS -- BOND LAYER | Spray first pass at close standoff (100--150 mm) for maximum droplet impact and density. This layer anchors the entire coating. Steady traverse speed -- no stopping. |
| 3 | BUILD PASSES | Add thickness with subsequent passes at normal standoff (150--250 mm). Overlap each pass 25--50%. Maintain consistent gun-to-surface distance and angle. |
| 4 | MONITOR THICKNESS | Measure DFT (dry film thickness) with magnetic gauge per SSPC-PA 2. Take readings at multiple locations. Compare to target per AWS C2.18. |
| 5 | CHECK UNIFORMITY | Visual check for uniform coverage, consistent texture, no bare spots. Edge buildup is common -- blend edges with a final light pass. |
| 6 | PROCEED TO SEAL | Seal coat must be applied within 4 hours of spray completion. Do not allow porous coating to absorb moisture. Proceed directly to post-treatment. |

Step numbers: Barlow Condensed ExtraBold 28 pt `#27AE60`. Title: Barlow SemiBold 16 pt `#F0EDE8`. Details: Inter Regular 13 pt `#F0EDE8` at 80%.

**BLOCK C -- AWS C2.18 Thickness Table**

Y: 11.0" to 15.0".

Section sublabel: `COATING THICKNESS BY MATERIAL & EXPOSURE -- AWS C2.18` Barlow SemiBold 18 pt `#E8A020`. Y: 11.0".

| Material | Mild Exposure | Moderate Exposure | Severe / Marine |
|---|---|---|---|
| Zinc (99.9%) | 100--150 um (4--6 mils) | 150--250 um (6--10 mils) | 200--350 um (8--14 mils) |
| Aluminum (99.0%) | 100--150 um (4--6 mils) | 150--250 um (6--10 mils) | 150--350 um (6--14 mils) |
| Zinc-Aluminum 85/15 | 100--150 um (4--6 mils) | 150--250 um (6--10 mils) | 150--300 um (6--12 mils) |

Table header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.
Material: Inter Medium 14 pt `#F0EDE8`. Thickness values: JetBrains Mono 13 pt `#E8A020`.

Below table:
- Callout: `These are MINIMUM thickness requirements. Many specifications call for the upper end of the range to provide additional service life margin.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- Coating Properties

**Section label:** `AS-SPRAYED COATING PROPERTIES` -- Y: 15.7".

**BLOCK D -- Coating Properties Table**

Y: 16.3" to 21.5".

| Property | Zinc | Aluminum | Stainless 316L |
|---|---|---|---|
| Porosity | 5--15% | 5--15% | 5--15% |
| Oxide content | 5--15% | 5--15% | 5--15% |
| Bond strength (ASTM C633) | 10--30 MPa | 10--30 MPa | 15--35 MPa |
| Surface roughness (Ra) | 10--25 um | 10--25 um | 10--25 um |
| Hardness | 40--60 HV | 30--50 HV | 250--350 HV |
| Corrosion mechanism | Sacrificial (cathodic protection) | Barrier + sacrificial in marine | Barrier only |

Table header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.
Property: Inter Medium 13 pt. Values: JetBrains Mono 12 pt.

Below table -- two side-by-side callouts:

**Left:** `Zinc provides CATHODIC (sacrificial) protection -- even if the coating is scratched, zinc preferentially corrodes to protect the steel underneath.` Inter Regular 13 pt `#2EC4B6`. Left accent `#2EC4B6`.

**Right:** `Aluminum provides BARRIER protection in most environments, plus sacrificial protection in marine/salt spray. Preferred for high-temperature service (Al does not form white corrosion products).` Inter Regular 13 pt `#E8A020`. Left accent `#E8A020`.

---

### ZONE 5 -- Seal Timing

**Section label:** `THE 4-HOUR SEAL WINDOW` -- Y: 22.2".

**BLOCK E -- Seal Timing and Options**

Y: 22.8" to 28.0".

**Top -- Warning Banner:**
- Rounded rect, W: 23.0", H: 1.5", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`
- `SEAL WITHIN 4 HOURS OF SPRAY COMPLETION. Porous coatings (5--15% porosity) absorb moisture rapidly. Moisture trapped under the seal coat accelerates corrosion at the coating-substrate interface -- the exact interface you are trying to protect.` Barlow SemiBold 16 pt `#E05C5C`.

**Below -- Seal Coat Options (3 cards):**

| Card | Seal Type | Application | Use Case |
|---|---|---|---|
| 1 | Vinyl wash primer | Brush or spray; thin penetrating sealer | Low-cost; fills surface porosity; often first coat of paint system |
| 2 | Epoxy sealer | Brush or spray; penetrates interconnected porosity | Most common; excellent corrosion barrier; compatible with topcoat paints |
| 3 | Full paint system | Primer + intermediate + topcoat over sealed coating | Maximum service life; many specifications require complete paint system over TSC |

Cards: W: 7.3", H: 2.5", fill `#1E2435`, top accent `#27AE60`.

Below cards:
- `Exception: some cathodic protection specifications deliberately leave zinc UNSEALED so the porous zinc can sacrificially corrode. Verify with your specification before omitting seal.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Defect Watch

**Section label:** `DEFECT WATCH -- WHAT TO LOOK FOR DURING SPRAY` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Defect | Visual Cue | Action |
|---|---|---|---|---|
| 1 | 0.5" | BARE SPOTS | Visible substrate through coating; incomplete coverage | Additional pass at normal standoff; check traverse overlap |
| 2 | 6.33" | EXCESSIVE SPATTER | Large solidified droplets on surface; rough, bumpy texture | Check wire feed balance; verify air pressure is adequate; check contact tips |
| 3 | 12.16" | DELAMINATION | Coating lifting or peeling during spray; visible separation | Stop immediately; strip and re-blast; investigate contamination or dew point |
| 4 | 18.0" | ARC INSTABILITY | Flickering arc; intermittent spray; popping sounds | Check wire feed synchronization; verify power supply voltage; replace worn contact tips |

---

### ZONE 7 -- Footer

Standard footer. Title: `Spray Application -- Arc Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: AWS C2.18; SSPC-CS 23.00; ASM Handbook Vol 5A; general industry knowledge. Thickness requirements are per AWS C2.18 -- always verify against the specific coating specification for each project.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #516 -- Construction Workup v1.0 -- 2026-04-26*
