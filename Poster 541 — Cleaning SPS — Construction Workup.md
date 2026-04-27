---
Project: Plating Posters Inc
Poster Number: 541
Title: "Cleaning -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS cleaning follows the standard APS pre-spray cleaning sequence. SPS coatings are applied over a conventionally sprayed APS bond coat, so cleaning applies to initial substrate preparation. Identical to APS cleaning protocol.
Process Scope: Pre-spray substrate cleaning for SPS
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Cleaning
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #541 -- Construction Workup
## Cleaning -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning for SPS follows the standard APS pre-spray protocol -- this is substrate preparation before any spraying happens. The SPS topcoat goes over a conventional APS bond coat, so cleanliness at the initial substrate level determines the entire system's integrity. Hero visual: a 4-step cleaning sequence with time-window callouts between steps.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- CLEANING SEQUENCE HERO (2.9"--15.5" / ~12.6")
  Block B: 4-step vertical cleaning sequence with time windows
ZONE 3 -- CLEANING METHODS DETAIL (15.5"--22.0" / ~6.5")
  Block C: Solvent degrease vs. alkaline wash comparison
  Block D: Water-break-free test panel
ZONE 4 -- CRITICAL TIMING + CONTAMINATION (22.0"--28.5" / ~6.5")
  Block E: Time-window rules (clean-to-blast, blast-to-spray)
  Block F: Common contaminants and their effects
ZONE 5 -- SPS-SPECIFIC NOTES (28.5"--32.5" / ~4.0")
  Block G: 4 SPS-specific cleaning considerations
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`.
**Subheading:** `Suspension Plasma Spray (SPS) -- Pre-Spray Substrate Preparation` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Skip the prep. Ruin the coating. Every SPS system starts with a clean substrate -- the bond coat has no chance on a contaminated surface.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Cleaning Sequence Hero

**Section label:** `PRE-SPRAY CLEANING SEQUENCE` -- Y: 3.1".

**BLOCK B -- 4-Step Vertical Sequence**

Y: 3.8" to 15.0". Four large step cards stacked vertically with arrow connectors and time-window callouts between steps.

Each step card: Rounded rect, W: 23.0", H: 2.3", fill `#1E2435`, radius 6.

| Step | Top Accent | Title | Parameters | Check |
|---|---|---|---|---|
| 1 | `#2EC4B6` | SOLVENT DEGREASE | Vapor degrease (legacy) or aqueous alkaline clean (preferred). Remove all oils, greases, machining fluids, fingerprints. | No visible residue |
| 2 | `#2EC4B6` | ALKALINE WASH | Immersion or spray wash. 50--70 degC, pH 10--12, 5--15 min. Rinse thoroughly with clean water. | Thorough rinse -- no alkaline residue |
| 3 | `#27AE60` | WATER-BREAK-FREE TEST | ASTM F22 equivalent. Surface must sheet water uniformly with no beading. Any break = contamination remains. | PASS = uniform water sheet |
| 4 | `#E8A020` | DRY | Forced air or oven dry. No moisture at time of grit blast. Moisture = flash rust on steel substrates. | Bone dry before blast |

Time-window callouts between steps (Inter Medium 14 pt `#E8A020`):
- Between Step 2 and 3: `Rinse immediately -- do not allow cleaner to dry on surface`
- Between Step 4 and grit blast: `Minimize time to grit blast -- ideally same shift`

---

### ZONE 3 -- Cleaning Methods Detail

**Section label:** `CLEANING METHODS -- TWO APPROACHES` -- Y: 15.7".

**Two-column layout:**

**Left -- BLOCK C: Solvent vs. Alkaline Comparison (X: 0.5", W: 11.0"):**

| Property | Solvent Degrease | Alkaline Wash |
|---|---|---|
| Method | Vapor or wipe | Immersion or spray |
| Temperature | Per solvent | 50--70 degC |
| Effectiveness | Oils and greases | Oils, particulate, shop soils |
| Environmental | VOC concerns; legacy solvents restricted | Preferred; water-based |
| Rinse required | No (vapor); yes (wipe) | Yes -- thorough |
| Best for | Light contamination | General purpose |

**Right -- BLOCK D: Water-Break-Free Test (X: 12.0", W: 11.5"):**

Visual: Rounded rect with two sub-panels:
- `PASS` panel (`#27AE60` accent): `Water sheets uniformly. No beading. No breaks. Surface is clean.`
- `FAIL` panel (`#E05C5C` accent): `Water beads or breaks. Contamination present. Re-clean and re-test.`

`This is the go/no-go gate. If the surface fails water-break-free, do NOT proceed to grit blast.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 4 -- Critical Timing + Contamination

**Section label:** `TIME WINDOWS & CONTAMINATION` -- Y: 22.2".

**Left -- BLOCK E: Time-Window Rules (X: 0.5", W: 11.0"):**

| Window | Rule | Why |
|---|---|---|
| Clean to blast | Same shift; minimize delay | Recontamination from handling, airborne |
| Blast to spray | < 4 hours (spec-dependent; some < 2 hr) | Oxide regrowth; moisture absorption |
| After blast | Wear clean lint-free gloves | Fingerprints = instant contamination |

**Right -- BLOCK F: Common Contaminants (X: 12.0", W: 11.5"):**

| Contaminant | Source | Effect on Coating |
|---|---|---|
| Machining oil | Prior operations | Delamination; poor bond |
| Fingerprints | Bare-hand contact | Localized adhesion failure |
| Moisture | Humidity, incomplete dry | Flash rust; porosity at interface |
| Shop dust | Airborne particulate | Inclusions at interface |
| Old coatings | Incomplete strip | Non-uniform bonding |

---

### ZONE 5 -- SPS-Specific Notes

**Section label:** `SPS-SPECIFIC CLEANING NOTES` -- Y: 28.7".

**BLOCK G -- Four Note Cards**

| Card | Note |
|---|---|
| 1 | SPS goes over an APS bond coat -- cleaning is for the initial substrate, not the bond coat surface |
| 2 | Bond coat surface should be sprayed promptly after APS application -- no additional cleaning between bond coat and SPS topcoat |
| 3 | Cleaning protocol is identical to standard APS -- no SPS-specific deviations at this stage |
| 4 | For aerospace substrates: final rinse with DI water; avoid any residual mineral deposits from tap water |

---

### ZONE 6 -- Footer

Standard. Title: `Cleaning -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #541 -- Construction Workup v1.0 -- 2026-04-26*
