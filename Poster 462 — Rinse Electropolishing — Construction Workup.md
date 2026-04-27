---
Project: Plating Posters Inc
Poster Number: 462
Title: "Rinse -- Electropolishing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7)"
Technical Source: Pre-electropolishing rinse stages. Covers rinse principles specific to EP -- preventing acid/cleaner drag-in to the electrolyte tank. Ambient temperature, flowing water, conductivity monitoring.
Process Scope: Electropolishing -- pre-polish rinse stages (Stages 2 and 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Electropolishing
  - Rinse
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #462 -- Construction Workup
## Rinse -- Electropolishing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Rinse poster covering the pre-polish rinse stages (Stages 2 and 4). In electropolishing, drag-in contamination is a real concern -- alkaline cleaner or acid dip residue in the EP electrolyte changes the chemistry and can cause defects. This poster covers rinse water quality, cascade vs. single-stage, conductivity monitoring, and the economics of drag-out control.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse flow diagram (Block B -- HERO):** Visual showing cascade rinse tanks, flow direction, and conductivity check points.
2. **Rinse parameter table (Block D):** Compact table for both pre-polish rinse stages.
3. **Drag-in contamination callout (Block E):** What happens when rinse fails.
4. **Water quality panel (Block F):** DI vs. city water guidance.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stages 2 and 4 highlighted (Teal)
ZONE 3 -- RINSE SYSTEM HERO (4.2"--14.5" / ~10.3")
  Block B: Cascade rinse diagram with flow direction
  Block C: Rinse stage comparison (Stage 2 vs Stage 4)
ZONE 4 -- DRAG-IN CONTAMINATION (14.5"--22.0" / ~7.5")
  Block D: What drag-in does to the EP electrolyte
  Block E: Contamination threshold guidance
ZONE 5 -- WATER QUALITY & MONITORING (22.0"--28.5" / ~6.5")
  Block F: DI vs city water, conductivity targets
ZONE 6 -- RINSE ECONOMICS (28.5"--32.5" / ~4.0")
  Block G: Drag-out recovery, water conservation
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electropolishing -- Pre-Polish Rinse Stages 2 & 4` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `The rinse between cleaning and polishing protects the electrolyte. Drag-in contamination changes chemistry and causes defects.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Stages 2 and 4 highlighted (Teal). Others dimmed.
Below: `Before: Cleaned or acid-dipped surface --> After: Residue-free surface entering next stage`

---

### ZONE 3 -- Rinse System Hero

**Section label:** `RINSE CONFIGURATION` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Diagram (Y: 5.0" to 10.5")**

Visual showing two-stage cascade rinse with flow arrows:
- Tank 1 (drag-out recovery): Rounded rect, X: 2.0", W: 9.0", H: 4.0", fill `#252B3D`, border 2 pt `#2EC4B6`
- Tank 2 (clean rinse): Rounded rect, X: 13.0", W: 9.0", H: 4.0", fill `#252B3D`, border 2 pt `#27AE60`
- Flow arrow from Tank 2 overflow to Tank 1
- Fresh water input arrow to Tank 2
- Labels: `DRAG-OUT RECOVERY` and `CLEAN RINSE` Barlow SemiBold 16 pt

Parameters inside each tank:
- Tank 1: `Captures concentrated drag-out` / `Return to process tank when concentration builds` JetBrains Mono 12 pt `#2EC4B6`
- Tank 2: `Fresh flowing water` / `Conductivity < 50 uS/cm target` JetBrains Mono 12 pt `#27AE60`

**BLOCK C -- Stage-by-Stage Rinse Comparison (Y: 11.0" to 14.0")**

Two side-by-side cards:

**Stage 2 -- Post-Clean Rinse (X: 0.5", W: 11.0"):**
- Rounded rect, H: 2.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `STAGE 2: POST-CLEAN RINSE`
- Parameters: `Ambient temp | Flowing or cascade | 30--60 sec`
- Purpose: `Remove alkaline cleaner. Prevents neutralizing the acid dip (Stage 3).`
- Check: `Alkaline residue + acid = heat + reaction products in tank`

**Stage 4 -- Pre-Polish Rinse (X: 12.0", W: 11.5"):**
- Rounded rect, H: 2.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `STAGE 4: PRE-POLISH RINSE`
- Parameters: `Ambient temp | Flowing or cascade | 30--60 sec`
- Purpose: `Remove acid dip residue. Prevents chloride drag-in to EP electrolyte.`
- Check: `HCl drag-in introduces chloride -- causes pitting during EP` (Coral `#E05C5C`)

---

### ZONE 4 -- Drag-In Contamination

**Section label:** `WHAT DRAG-IN DOES TO THE ELECTROLYTE` -- Y: 14.7".

**BLOCK D -- Contamination Effects Table (Y: 15.3" to 19.5")**

| Contaminant | Source | Effect on EP | Prevention |
|---|---|---|---|
| Alkaline cleaner | Stage 1 drag-through | Neutralizes acid; changes viscosity; poor polishing | Thorough Stage 2 rinse |
| Chloride (Cl-) | HCl acid dip drag-through | Pitting -- breaks down passive layer on SS | Use HNO3 instead of HCl; thorough Stage 4 rinse |
| Iron salts | Acid dip on carbon steel | Contaminates electrolyte; staining | Separate EP lines for CS vs SS |
| Organic residue | Incomplete cleaning | Streaking, uneven polishing film | Verify water-break-free before EP |
| Mineral deposits | Hard water rinse | Surface staining after EP | Use DI water for final pre-EP rinse |

**BLOCK E -- Key Warning Callout (Y: 20.0" to 21.0")**

Full-width, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`.
Text: `Chloride is the #1 drag-in concern for stainless steel EP. Even 50 ppm Cl- in the electrolyte can cause pitting. If using HCl for acid dip, rinse aggressively or switch to HNO3.` Barlow SemiBold 14 pt `#E05C5C`.

---

### ZONE 5 -- Water Quality & Monitoring

**Section label:** `WATER QUALITY` -- Y: 22.2".

**BLOCK F -- Two-Panel Water Guide (Y: 22.9" to 28.0")**

**Left -- Water Type Selection (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `WATER TYPE BY APPLICATION`

| Application | Water Type | Rationale |
|---|---|---|
| General industrial EP | City water acceptable | Cost-effective for non-critical work |
| Pharmaceutical/biotech | DI water required | ASME BPE requires DI final rinse > 1 MOhm-cm |
| Semiconductor | UPW (ultrapure water) | SEMI F19 specifications |
| Drag-out recovery tank | City water OK | Will be contaminated by drag-out anyway |

**Right -- Monitoring (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `RINSE MONITORING`

```
Conductivity meter: < 50 uS/cm for clean rinse
pH paper: verify neutral (6--8) after alkaline clean rinse
Visual: no foaming, no discoloration
Flow rate: sufficient to dilute drag-out
Temperature: ambient (no heating required)
```

---

### ZONE 6 -- Rinse Economics

**Section label:** `WATER CONSERVATION` -- Y: 28.7".

Two-card strip:

**Card 1 -- Drag-Out Recovery (X: 0.5", W: 11.0"):**
- Title: `DRAG-OUT RECOVERY` Barlow SemiBold 16 pt `#27AE60`
- Body: `First rinse tank captures concentrated drag-out. Return to EP tank when concentration builds. Reduces chemical consumption and wastewater volume.`

**Card 2 -- Cascade Rinse Benefit (X: 12.5", W: 11.0"):**
- Title: `CASCADE RINSE` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Counter-current cascade: fresh water enters the cleanest tank and overflows backward to the dirtiest. Uses 80--90% less water than single-tank overflow rinse.`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Electropolishing`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Electropolishing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chloride drag-in warning (Block E) is the single most actionable item on this poster. Many shops use HCl for their acid dip out of habit, not realizing that chloride drag-in to the EP tank is a direct cause of pitting on stainless. The cascade rinse diagram should be visually clear enough that a new operator can trace the water flow path.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #462 -- Construction Workup v1.0*
*2026-04-26*
