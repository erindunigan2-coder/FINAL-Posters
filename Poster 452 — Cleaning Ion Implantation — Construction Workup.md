---
Project: Plating Posters Inc
Poster Number: 452
Title: "Cleaning -- Ion Implantation"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 6: Ion Implantation, Sections 6.3, 6.4)"
Process Scope: Pre-implantation cleaning for semiconductor wafers and industrial parts
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IonImplantation
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #452 -- Construction Workup
## Cleaning -- Ion Implantation

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning for ion implantation is critical but for different reasons than coating processes. There is no adhesion concern -- the ions are embedded in the lattice regardless. The issue is that surface contamination absorbs implant energy and scatters ions before they reach the substrate, wasting dose and degrading depth profile uniformity. For semiconductor, the RCA clean is the gold standard and is a well-defined multi-step chemical process. For industrial, standard ultrasonic cleaning applies. The hero visual is the RCA clean sequence for semiconductor -- it is iconic in the semiconductor industry.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **RCA clean sequence hero (Block B):** Step-by-step RCA cleaning process for semiconductor wafers.
2. **Industrial cleaning protocol (Block D):** Simpler cleaning for metal parts.
3. **Why contamination matters (Block E):** How surface contamination affects implant quality.
4. **Cleaning validation (Block F):** Methods to verify cleanliness.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- RCA CLEAN SEQUENCE HERO (2.9"--14.5" / ~11.6")
  Block B: Semiconductor RCA clean step-by-step
ZONE 3 -- INDUSTRIAL CLEANING PROTOCOL (14.5"--20.5" / ~6.0")
  Block D: Ultrasonic cleaning for metal parts
ZONE 4 -- WHY CONTAMINATION MATTERS (20.5"--26.5" / ~6.0")
  Block E: How surface contamination degrades implant quality
ZONE 5 -- CLEANING VALIDATION (26.5"--32.5" / ~6.0")
  Block F: Methods to confirm cleanliness
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`.
**Subheading:** `Ion Implantation -- Pre-Implant Surface Preparation` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Surface contamination scatters and absorbs your ion beam. Every atom of contamination between the beam and the substrate is a wasted ion.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- RCA Clean Sequence Hero

**Section label:** `THE RCA CLEAN -- SEMICONDUCTOR INDUSTRY STANDARD` -- Y: 3.1".

**BLOCK B -- RCA Clean Steps**

Y: 3.8" to 14.3".

**Introduction (Y: 3.8" to 4.8"):**
- Inter Regular, 14 pt, `#F0EDE8`
- Text: `The RCA clean was developed at the RCA Corporation in 1965 by Werner Kern. It remains the foundation of semiconductor wafer cleaning worldwide. It consists of two chemical steps (SC-1 and SC-2) with DI water rinses between them, targeting organic contamination, particles, and metal ions respectively.`

**Five sequential step cards (Y: 5.2" to 14.0"):**

Vertical sequence with downward arrows between cards.

| Step | Title | Accent | Chemistry | Temp | Time | Target |
|---|---|---|---|---|---|---|
| SC-1 | Standard Clean 1 | `#2EC4B6` | NH4OH : H2O2 : H2O (1:1:5 to 1:2:7) | 70--80 C | 10--15 min | Removes organic contamination and particles. H2O2 oxidizes organics; NH4OH dissolves oxide to undercut particles. |
| Rinse 1 | DI Water Rinse | `#C8D0D8` | > 18 Mohm-cm ultrapure DI water | Ambient | 5 min (cascade or dump-rinse) | Remove SC-1 chemistry and dissolved contaminants. |
| SC-2 | Standard Clean 2 | `#E8A020` | HCl : H2O2 : H2O (1:1:6 to 1:2:8) | 70--80 C | 10--15 min | Removes metal ion contamination (Fe, Cu, Ni, Cr, Co). HCl forms soluble metal chloride complexes. |
| Rinse 2 | DI Water Rinse | `#C8D0D8` | > 18 Mohm-cm ultrapure DI water | Ambient | 5 min | Remove SC-2 chemistry. |
| Dry | Spin-Rinse Dry or Marangoni Dry | `#27AE60` | IPA vapor assist (Marangoni) or spin dry | Ambient | 2--5 min | Zero water spots; zero particles added during drying. |

Each card: Rounded rect, X: 2.0", W: 20.0", H: 1.5", fill `#1E2435`, left accent 0.06".
Title: Barlow SemiBold, 16 pt, accent color.
Chemistry: JetBrains Mono 12 pt `#F0EDE8`.
Temp/Time: JetBrains Mono 12 pt `#E8A020`.
Target: Inter Regular, 12 pt, `#F0EDE8` at 70%.

Downward arrows between cards: stroke 2 pt `#3A4055`, arrowhead filled.

**Note (Y: 13.5"):**
- `Some fabs add an HF dip (dilute HF, 1:100, 30 sec) before SC-1 to remove native oxide. This exposes a hydrogen-terminated Si surface and improves SC-1 particle removal.` -- Inter Regular, 12 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Industrial Cleaning Protocol

**Section label:** `INDUSTRIAL CLEANING -- SIMPLER BUT STILL CRITICAL` -- Y: 14.7".

**BLOCK D -- Industrial Clean Steps**

Y: 15.3" to 20.3".

| Step | Method | Temperature | Time | Purpose |
|---|---|---|---|---|
| 1 | Alkaline ultrasonic soak | 50--70 C | 10--20 min | Remove oils, grease, machining fluids, fingerprints |
| 2 | DI water rinse | Ambient | 5 min | Remove alkaline residue |
| 3 | IPA or acetone wipe (optional) | Ambient | As needed | Spot clean any remaining contamination |
| 4 | Hot air dry or vacuum dry | 80--100 C | 5--10 min | Zero moisture on surface |
| 5 | Visual inspection | -- | -- | Verify clean, dry, particle-free surface |

Header: Barlow SemiBold, 13 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Inter Regular 13 pt `#F0EDE8`.

**Key difference callout (Y: 19.5"):**
- `Industrial parts are polycrystalline -- channeling is less of a concern. But contamination still absorbs and scatters the beam, reducing the effective dose reaching the substrate surface.` -- Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 4 -- Why Contamination Matters

**Section label:** `HOW CONTAMINATION DEGRADES YOUR IMPLANT` -- Y: 20.7".

**BLOCK E -- Four Impact Cards**

Y: 21.3" to 26.3". Four cards in a row.

| Card | X | W | Impact | Accent | Explanation |
|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | DOSE LOSS | `#E05C5C` | Ions hitting contamination atoms instead of substrate atoms are wasted. A 10 nm hydrocarbon layer absorbs measurable dose that never reaches the metal surface. |
| 2 | 6.33" | 5.5" | DEPTH PROFILE SHIFT | `#E8A020` | Contamination acts as an additional stopping layer, shifting the implant depth profile shallower than intended. The peak concentration (Rp) moves toward the surface. |
| 3 | 12.16" | 5.5" | SPUTTERING OF CONTAMINANTS | `#E05C5C` | High-energy ions can sputter contamination atoms INTO the substrate -- implanting the wrong species. Carbon and oxygen from organics are common contaminants. |
| 4 | 18.0" | 5.5" | NON-UNIFORM PROPERTIES | `#E8A020` | Patchy contamination causes patchy implantation. Some areas receive full dose; others receive reduced dose through the contamination layer. |

Each card: Rounded rect, H: 4.8", fill `#1E2435`, radius 6, left accent 0.06".
Impact: Barlow SemiBold, 16 pt, accent color.
Explanation: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 5 -- Cleaning Validation

**Section label:** `VERIFYING CLEANLINESS` -- Y: 26.7".

**BLOCK F -- Validation Methods Table**

Y: 27.3" to 32.3".

| Method | What It Detects | Sensitivity | Application |
|---|---|---|---|
| Water-break test | Hydrocarbon contamination | Qualitative (monolayer-level) | Quick shop-floor check; water should sheet uniformly |
| Particle counter (laser) | Surface particles > 0.1 um | Quantitative; particles/cm2 | Semiconductor -- post-clean wafer inspection |
| TXRF (Total Reflection XRF) | Metal contamination on Si surface | 10^9 atoms/cm2 | Semiconductor -- verifies SC-2 effectiveness |
| Contact angle measurement | Surface energy / organic contamination | Quantitative; < 5 deg = clean | Research and QC labs |
| UV fluorescence | Residual oils and organic contamination | Qualitative | Industrial -- black light inspection |
| TOC (Total Organic Carbon) | Organic contamination in rinse water | ppb-level | Semiconductor -- rinse water quality monitoring |

Header: Barlow SemiBold, 12 pt, `#F0EDE8`, fill `#3A4055`.
Data: alternating `#1E2435` / `#252B3D`. Method: Inter Medium, 13 pt, `#F0EDE8`. Sensitivity: JetBrains Mono 12 pt `#2EC4B6`.

---

### ZONE 6 -- Footer

Standard. Title: `Cleaning -- Ion Implantation`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Ion Implantation -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The RCA clean hero (Zone 2) is a piece of semiconductor history. Werner Kern's 1965 procedure is still in use 60+ years later -- that makes it one of the most enduring chemical processes in all of manufacturing. The vertical step sequence with downward arrows visually communicates the sequential nature of the clean. The industrial section (Zone 3) is deliberately simpler because industrial cleaning for ion implantation IS simpler. The contamination impact cards (Zone 4) bridge both audiences by explaining the physics of why cleaning matters regardless of application.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #452 -- Construction Workup v1.0*
*2026-04-26*
