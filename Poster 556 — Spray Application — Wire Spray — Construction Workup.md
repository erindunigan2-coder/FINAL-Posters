---
Project: Plating Posters Inc
Poster Number: 556
Title: "Spray Application -- Wire Combustion Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 8: Wire Combustion Spray)"
Technical Source: Wire combustion spray application for corrosion protection per AWS C2.18. Zinc 100--350 um, aluminum 150--350 um, Zn-Al 85/15 150--300 um depending on exposure severity. Porosity 5--15%, oxide content 5--15%, bond strength 7--25 MPa. Comparison with arc spray: lower density but more portable. Coating is cathodic (sacrificial) protection on steel.
Process Scope: Wire combustion spray application technique and coating buildup
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - WireCombustionSpray
  - SprayApplication
  - ConstructionWorkup
  - ClusterTS08
---

# Poster #556 -- Construction Workup
## Spray Application -- Wire Combustion Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is where the zinc or aluminum goes onto the steel. Multiple crossing passes at consistent standoff, building to AWS C2.18 thickness targets. The coating provides cathodic (sacrificial) protection -- zinc or aluminum corrodes preferentially, protecting the steel underneath even at holidays and cut edges. The thickness table per exposure severity is the key reference. Coating properties comparison with arc spray is the decision-support element.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- APPLICATION TECHNIQUE / HERO (2.9"--15.5")
  Block B: Step-by-step spray technique
  Block C: AWS C2.18 thickness requirements table
ZONE 3 -- COATING PROPERTIES (15.5"--22.0")
  Block D: Zinc wire spray coating property table
  Block E: How cathodic protection works callout
ZONE 4 -- WIRE MATERIAL COMPARISON (22.0"--28.5")
  Block F: Zinc vs. aluminum vs. Zn-Al 85/15 comparison
ZONE 5 -- COMMON DEFECTS (28.5"--32.5")
  Block G: 4 application defect cards
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SPRAY APPLICATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Wire Combustion Spray -- Cathodic Protection for Steel Infrastructure` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Zinc or aluminum, melted in flame, atomized by air, deposited on steel. The coating sacrifices itself so the structure doesn't. That's cathodic protection -- and it works for decades.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Application Technique (HERO)

**Section label:** `SPRAY APPLICATION TECHNIQUE` -- Y: 3.1".

**BLOCK B -- Step-by-Step Technique**

Y: 3.8" to 10.5". Six step cards in two rows of three.

Each card: Rounded rect, W: 7.33", H: 3.0", fill `#1E2435`, radius 6.

| Step | Title | Detail |
|---|---|---|
| 1 | PREHEAT | Flame gun (no wire) to 80--120 degC. Drives off moisture; improves first-pass adhesion. Verify with temp crayon or IR gun. |
| 2 | FIRST PASS | Spray at 150--250 mm standoff, 75--90 deg angle. Consistent traverse speed. Cover entire surface in one direction. |
| 3 | CROSSING PASS | Second pass at 60--90 deg to first. This builds uniform thickness and fills gaps from first pass. |
| 4 | BUILD THICKNESS | Continue crossing passes until target thickness reached. Check with DFT gauge between pass sets. |
| 5 | EDGE & CORNER WORK | Extra attention to edges, corners, welds, bolts. These areas are hardest to coat and first to fail. Reduce standoff slightly. |
| 6 | FINAL DFT CHECK | Verify thickness at multiple points per SSPC-PA 2. Record readings. Flag any thin areas for touch-up. |

Step 1-2: top accent `#E8A020`. Step 3-4: top accent `#27AE60`. Step 5-6: top accent `#2EC4B6`.

**BLOCK C -- AWS C2.18 Thickness Table**

Y: 11.0" to 15.3". Full-width table.

Title: `MINIMUM COATING THICKNESS PER AWS C2.18` Barlow SemiBold 20 pt `#F0EDE8`.

| Wire Material | Mild Exposure (um) | Moderate Exposure (um) | Severe Exposure (um) |
|---|---|---|---|
| Zinc | 100 | 200 | 300--350 |
| Aluminum | 150 | 200 | 250--350 |
| Zinc-Aluminum 85/15 | 150 | 200 | 250--300 |

Data: JetBrains Mono 14 pt.

Note below table: `Exposure severity defined by AWS C2.18: Mild = indoor/dry; Moderate = industrial/urban; Severe = marine/immersion/chemical.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 3 -- Coating Properties

**Section label:** `WIRE SPRAY COATING PROPERTIES` -- Y: 15.7".

**Left -- BLOCK D: Zinc Coating Properties (X: 0.5", W: 11.0"):**

Title: `ZINC WIRE COMBUSTION SPRAY COATING` Barlow SemiBold 18 pt `#F0EDE8`.

| Property | Typical Range |
|---|---|
| Porosity | 5--15% |
| Oxide content | 5--15% |
| Bond strength (ASTM C633) | 7--25 MPa |
| Surface roughness (Ra) | 10--25 um |
| Hardness | 40--60 HV |
| Density | 85--95% of wire density |
| Protection mechanism | Cathodic (sacrificial) |

Data: JetBrains Mono 12 pt.

Note: `Porosity is sealed by the seal coat (post-treatment). The interconnected porosity allows the sealer to penetrate and lock the coating system together.` Inter Medium 13 pt `#2EC4B6`.

**Right -- BLOCK E: Cathodic Protection Explanation (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06".

Title: `HOW CATHODIC PROTECTION WORKS` Barlow SemiBold 18 pt `#27AE60`.

Body (Inter Regular 14 pt, line height 155%):
```
Zinc and aluminum are MORE ANODIC than steel
in the galvanic series.

When moisture bridges the coating and steel,
the zinc/aluminum corrodes INSTEAD of the steel.

This is "sacrificial" protection:
- Works even at holidays, scratches, and cut edges
- The coating corrodes preferentially
- Steel remains protected as long as zinc/aluminum remains
- White rust (zinc) or white powder (aluminum) = protection working

Expected service life:
- Zinc: 20--40+ years depending on thickness and environment
- Aluminum: 20--40+ years (better in marine environments)
```

---

### ZONE 4 -- Wire Material Comparison

**Section label:** `ZINC vs. ALUMINUM vs. ZINC-ALUMINUM` -- Y: 22.2".

**BLOCK F -- Three-Column Comparison**

| Property | Zinc | Aluminum | Zn-Al 85/15 |
|---|---|---|---|
| Melting point | 420 degC | 660 degC | ~450 degC |
| Protection type | Cathodic (sacrificial) | Cathodic (sacrificial) + barrier | Cathodic + barrier |
| Best for | Atmospheric; mild to moderate | Marine; high-temp; immersion | Best all-around; combines benefits |
| White corrosion product | Yes (zinc carbonate) | Yes (aluminum oxide) | Yes (mixed) |
| Max service temp | ~250 degC | ~500 degC | ~300 degC |
| Sealer adhesion | Good | Good | Excellent (85/15 standard) |
| Relative cost | Lowest | Moderate | Moderate |
| Spray difficulty | Easiest | Slightly harder (higher melt point) | Easy |

Data: JetBrains Mono 11 pt.

Three column headers with accent colors:
- Zinc: `#2EC4B6`
- Aluminum: `#E8A020`
- Zn-Al 85/15: `#27AE60` with badge: `RECOMMENDED ALL-AROUND`

Bottom note: `Zn-Al 85/15 is increasingly specified as the default choice -- it combines the cathodic protection of zinc with the barrier protection and sealer adhesion of aluminum.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 5 -- Common Defects

**Section label:** `APPLICATION DEFECTS -- 4 COMMON PROBLEMS` -- Y: 28.7".

**BLOCK G -- Four Defect Cards**

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | THIN SPOTS | Inconsistent traverse speed; missing areas | DFT check between passes; mark thin areas; touch up |
| 2 | 6.33" | POOR ADHESION | Contaminated surface; exceeded blast-to-spray window | Re-blast and re-spray; respect time windows |
| 3 | 12.16" | BLISTERING | Moisture on substrate; insufficient preheat | Preheat to 80--120 degC; verify dew point compliance |
| 4 | 18.0" | EDGE/CORNER FAILURES | Insufficient coverage at edges (common) | Extra passes at edges; reduce standoff; consider rounding sharp edges before blast |

---

### ZONE 6 -- Footer

Standard. Title: `Spray Application -- Wire Combustion Spray`. Version `v1.0 -- 2026`.

Disclaimer: `Coating thickness requirements per AWS C2.18. Exposure severity classification and minimum thicknesses are specification-dependent. Consult applicable standards for binding requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Spray Application Wire Spray -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #556 -- Construction Workup v1.0 -- 2026-04-26*
