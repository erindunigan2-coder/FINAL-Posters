---
Project: Plating Posters Inc
Poster Number: 654
Title: "Application -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.6"
Technical Source: Industry-standard powder application by electrostatic spray and fluidized bed. Covers gun voltage, current, flow rates, charging methods (corona vs. tribo), Faraday cage effect, reclaim systems, DFT targets, and NFPA 654 combustible dust safety.
Process Scope: Powder application methods (Stage 5 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - Application
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #654 -- Construction Workup
## Application -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of 9. This is where powder meets part. Electrostatic spray is the primary method -- charged powder particles are attracted to grounded parts. The hero visual is a gun-to-part diagram showing the electrostatic field, powder trajectory, and Faraday cage effect. Corona vs. tribo charging is the key operator decision. NFPA 654 combustible dust hazard is real and gets its own safety callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Gun-to-part electrostatic diagram (Block B -- HERO):** Shows corona gun, electric field lines, powder trajectory, and grounded part. Faraday cage effect illustrated on a recessed part.
2. **Application parameter table (Block C):** Gun voltage, current, flow rate, distance, particle size, booth air velocity.
3. **Corona vs. tribo comparison (Block D):** Side-by-side charging method comparison.
4. **DFT target table (Block E):** DFT ranges by application type.
5. **NFPA 654 safety callout (Block F):** Combustible dust warning panel.
6. **Defect grid (Block G):** 6 application-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 19.5" / 25.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Application (Emerald)
ZONE 3 -- ELECTROSTATIC SPRAY HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- APPLICATION PARAMETERS + CORONA vs TRIBO (13.5"--19.5" / ~6.0")
ZONE 5 -- DFT TARGETS + FLUIDIZED BED (19.5"--25.0" / ~5.5")
ZONE 6 -- NFPA 654 SAFETY + RECLAIM (25.0"--28.5" / ~3.5")
ZONE 7 -- DEFECT GRID (28.5"--32.5" / ~4.0")
ZONE 8 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `APPLICATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- Electrostatic Spray and Fluidized Bed` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Charged particles, grounded parts, zero solvent. 95-98% material utilization with overspray reclaim. This is the cleanest application method in industrial finishing.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Application -- fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean, dry, cooled part at < 90 F --> After: Electrostatically deposited powder layer ready for cure`

---

### ZONE 3 -- Electrostatic Spray Hero

**Section label:** `HOW ELECTROSTATIC POWDER SPRAY WORKS` -- Y: 4.4".

**BLOCK B -- Gun-to-Part Diagram**

Y: 5.0" to 13.0". Full-width hero illustration built with rectangles, lines, and labeled callouts.

Left side -- Spray gun:
- Rounded rect representing gun body, fill `#3A4055`, W: 3.0", H: 1.5"
- Label: `CORONA GUN` -- Barlow SemiBold, 16 pt, `#27AE60`
- Electrode tip label: `High-voltage electrode (60--100 kV)`
- Powder feed line entering gun: `Powder from hopper (100--400 g/min)`

Center -- Electric field:
- Curved lines (built with thin rectangles at angles) radiating from gun tip to grounded part
- Dots along field lines representing charged powder particles
- Label: `Charged powder particles follow electric field lines`
- Back-ionization zone label: `Back-ionization risk above 80 kV` (Coral)

Right side -- Grounded part:
- Rectangular workpiece, fill `#3A4055`, border 2 pt `#27AE60`
- Label: `GROUNDED WORKPIECE`
- Ground symbol at bottom
- Deposited powder layer on surface: thin rect `#27AE60` at 40%

Bottom-right -- Faraday cage callout:
- Box section (U-shaped channel) showing field lines wrapping around edges
- Label: `FARADAY CAGE EFFECT` -- Barlow SemiBold, 14 pt, `#E05C5C`
- Annotation: `Field lines cannot penetrate deep recesses -- powder deposits on edges, not in corners`
- Fix note: `Reduce voltage / use tribo / manual touch-up`

Booth environment labels:
- `Booth air velocity: 60--100 fpm (0.3--0.5 m/s)`
- `Transfer efficiency: 60--70% first-pass`
- `Reclaim: Cyclone + cartridge filter -> total 95--98% utilization`

---

### ZONE 4 -- Application Parameters + Corona vs. Tribo

**Section label:** `APPLICATION PARAMETERS AND CHARGING METHODS` -- Y: 13.7".

**Two-column layout (Y: 14.3" to 19.3"):**

**Left -- Parameter Table (X: 0.5", W: 11.0"):**

| Parameter | Typical Range | Notes |
|---|---|---|
| Gun voltage | 60--100 kV | Higher = better wrap; back-ionization > 80 kV |
| Gun current | 10--80 uA | Lower for recoat/touch-up |
| Powder flow rate | 100--400 g/min | Adjust for line speed and target DFT |
| Gun-to-part distance | 6--12 in (150--300 mm) | Closer = thicker; back-ionization risk |
| Particle size (D50) | 30--45 microns | Finer for thin films |
| Booth air velocity | 60--100 fpm | Contain overspray, don't strip powder |
| Transfer efficiency | 60--70% first-pass | 95--98% total with reclaim |

**Right -- Corona vs. Tribo (X: 12.0", W: 11.5"):**

Title: `CORONA vs. TRIBO -- WHICH CHARGING METHOD?` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Two stacked comparison cards:

*Corona Charging:*
- Accent: `#E8A020`
- `High-voltage electrode ionizes air at gun tip`
- `Free ions charge powder particles`
- `PROS: Fast build, high deposition rate, works with all powder types`
- `CONS: Back-ionization on thick films (orange peel, pinholes); poor Faraday cage penetration`
- `BEST FOR: General production, simple geometries`

*Tribo Charging:*
- Accent: `#2EC4B6`
- `Powder gains charge by friction against PTFE gun barrel`
- `No free ions = no back-ionization`
- `PROS: Better Faraday cage penetration; smoother finish on recoat`
- `CONS: Lower charge density, slower build; requires tribo-specific powder formulations`
- `BEST FOR: Complex geometries, recesses, second-coat work`

---

### ZONE 5 -- DFT Targets + Fluidized Bed

**Section label:** `DFT TARGETS AND FLUIDIZED BED APPLICATION` -- Y: 19.7".

**Two-column layout (Y: 20.3" to 24.8"):**

**Left -- DFT Target Table (X: 0.5", W: 11.0"):**

| Application | DFT (mils) | DFT (microns) |
|---|---|---|
| Decorative interior (furniture) | 1.5--3.0 | 38--76 |
| General industrial | 2.0--4.0 | 51--102 |
| Architectural exterior | 2.5--4.0 | 64--102 |
| Automotive (primer + topcoat) | 3.0--5.0 | 76--127 |
| Functional/protective (rebar, pipe) | 7--14 | 178--356 |
| Fluidized bed (thermoplastic) | 8--25+ | 200--635+ |

**Right -- Fluidized Bed (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `FLUIDIZED BED APPLICATION` -- Barlow SemiBold, 18 pt, `#E8A020`

Body:
- `Parts preheated to 400--500 F (204--260 C)`
- `Dipped into bed of fluidized powder`
- `Powder melts on contact with hot metal`
- `Builds 8--25+ mils in a single dip`
- `Primarily thermoplastic: nylon, PE, PVC`

Electrostatic fluidized bed note:
- `Variant: Electrostatic fluidized bed -- charging grid at bottom, no preheat needed. Practical for flat parts at 2--6 mil DFT.`

---

### ZONE 6 -- NFPA 654 Safety + Reclaim

**Two-column layout (Y: 25.2" to 28.3"):**

**Left -- Safety (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#E05C5C`, border 1 pt `#E05C5C` at 30%.
Title: `NFPA 654 -- COMBUSTIBLE DUST HAZARD` -- Barlow SemiBold, 18 pt, `#E05C5C`

Body:
- `Airborne powder in the spray booth is a combustible dust explosion hazard`
- `Maintain booth air velocity to prevent accumulation`
- `Ground all equipment, parts, and operators`
- `Housekeeping: no powder accumulation > 1/32" on surfaces`
- `Reclaim system maintenance: prevent blockages`
- `NO IGNITION SOURCES in or near the booth`

**Right -- Reclaim System (X: 12.0", W: 11.5"):**

Title: `OVERSPRAY RECLAIM` -- Barlow SemiBold, 18 pt, `#27AE60`

Two options:

*Cyclone separator:*
- `Centrifugal separation of powder from air`
- `Best for long-run single colors`
- `Recovery: 90--95% of overspray`

*Cartridge filter:*
- `Filter media captures fine particles`
- `Best for frequent color changes (fast clean-out)`
- `Recovery: 95--98% of overspray`

Bottom note: `With reclaim, total material utilization reaches 95--98%. Nearly zero waste.`

---

### ZONE 7 -- Defect Grid

**Section label:** `WHEN APPLICATION FAILS -- 6 COATING DEFECTS` -- Y: 28.7".

**BLOCK G -- 3x2 Grid (Y: 29.2" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BACK-IONIZATION | `#E05C5C` | Voltage too high or film too thick | Reduce voltage; switch to tribo for recoat |
| R1C2 | ORANGE PEEL | `#E8A020` | Back-ionization or wrong particle size | Lower kV; verify D50 30--45 um |
| R1C3 | THIN IN RECESSES | `#E8A020` | Faraday cage effect | Reduce voltage; tribo gun; manual touch-up |
| R2C1 | UNEVEN DFT | `#E05C5C` | Gun distance variation or hot parts | Standardize gun distance; verify part temp < 90 F |
| R2C2 | POOR WRAP | `#2EC4B6` | Insufficient voltage or poor grounding | Check ground path; increase kV; clean hooks |
| R2C3 | CONTAMINATION / SEEDS | `#E05C5C` | Foreign particles in reclaim powder | Filter reclaim; separate virgin and reclaim hoppers |

Each card: Rounded rect W: 7.33", H: 1.4", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 8 -- Footer

Standard. Title: `Application -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references; NFPA 654 Standard for Prevention of Fire and Dust Explosions from the Manufacturing, Processing, and Handling of Combustible Particulate Solids.`

---

## Parts 5--7

**Grouping:** 8 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Application Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The gun-to-part hero is the visual everyone remembers -- electric field lines curving from gun to grounded workpiece, with the Faraday cage callout showing why recesses are the eternal problem. The NFPA 654 safety panel earns its real estate because combustible dust explosions kill people in powder coating operations. Corona vs. tribo is the "which tool for which job" decision that every powder coat operator needs to understand. The DFT table gives the quality engineer a fast lookup.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #654 -- Construction Workup v1.0*
*2026-04-26*
