---
Project: Plating Posters Inc
Poster Number: 543
Title: "Masking & Fixturing -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS masking follows APS requirements plus additional considerations for liquid overspray (suspension that misses the plasma plume can splash onto masked areas) and ethanol-compatible masking materials. Rotation fixtures 60--200 RPM; cooling air nozzles critical.
Process Scope: Masking and fixturing for SPS
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - Masking
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #543 -- Construction Workup
## Masking & Fixturing -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Masking and fixturing for SPS builds on standard APS practice with two SPS-specific wrinkles: liquid overspray from the suspension feed, and ethanol compatibility of masking materials. Hero visual: a masked part diagram with callouts for each masking material type.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- MASKING MATERIALS INVENTORY / HERO (2.9"--15.5")
  Block B: Masking material table with temp ratings and applications
  Block C: SPS-specific masking callout
ZONE 3 -- FIXTURING REQUIREMENTS (15.5"--22.0")
  Block D: Fixture types and specifications
  Block E: Cooling considerations
ZONE 4 -- BEST PRACTICES + COMMON MISTAKES (22.0"--28.5")
  Block F: Best practices checklist
  Block G: 4 common masking mistakes
ZONE 5 -- SPS-SPECIFIC CONSIDERATIONS (28.5"--32.5")
  Block H: Liquid overspray + ethanol compatibility notes
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `MASKING & FIXTURING` -- 80 pt `#F0EDE8`.
**Subheading:** `Suspension Plasma Spray (SPS) -- Protecting What Shouldn't Be Coated` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Standard APS masking rules apply -- plus liquid overspray protection and ethanol-compatible materials. SPS adds a wet dimension to a traditionally dry process.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Masking Materials Inventory

**Section label:** `MASKING MATERIALS FOR SPS` -- Y: 3.1".

**BLOCK B -- Materials Table**

| Material | Temp Rating | Reusable | Best For |
|---|---|---|---|
| Hi-temp masking tape (silicone adhesive) | 260 degC (500 degF)+ | No | Quick masking; small areas |
| Metal masks (stainless, copper) | >500 degC | Yes | Production runs; repeatable geometry |
| Silicone plugs and caps | 260 degC+ | Yes | Holes, bores, threads |
| Ceramic fiber tape | >1000 degC | No | Extreme temperature zones |
| Liquid maskant (peelable) | Varies | No | Complex geometry; conformal coverage |

**BLOCK C -- SPS-Specific Masking Callout**

Coral-accented callout box:
- `SPS uses liquid suspension -- unmolten spray that misses the plasma plume can SPLASH onto masked areas`
- `Protective splash shields may be needed in addition to standard thermal masking`
- `Ethanol-based suspensions: all masking materials must be ethanol-compatible`
- `Do NOT use masking materials that dissolve or degrade in ethanol vapor atmosphere`

---

### ZONE 3 -- Fixturing Requirements

**Section label:** `FIXTURING FOR SPS` -- Y: 15.7".

**BLOCK D -- Fixture Specifications**

| Fixture Type | Application | Key Specs |
|---|---|---|
| Rotation fixture (lathe-type) | Cylindrical parts | 60--200 RPM; adjustable speed |
| Turntable | Flat/irregular parts | Variable speed; indexing |
| Multi-axis robot mount | Complex geometry | 6-axis; line-of-sight access |
| Custom jig | Part-specific | Design for uniform standoff |

Key rules:
- `Fixture must not shadow spray pattern -- design for full line-of-sight access`
- `Ground fixture to workpiece for electrostatic discharge prevention`
- `Fixture mass affects thermal management -- heavier = more heat sink`

**BLOCK E -- Cooling Considerations**

- `Cooling air nozzles directed at substrate backside -- CRITICAL for SPS`
- `SPS standoff (40--80 mm) is much closer than APS (75--150 mm) -- more heat at substrate`
- `Substrate temperature during SPS: 200--400 degC -- monitor continuously`
- `Compressed air must be dry and oil-free`

---

### ZONE 4 -- Best Practices + Common Mistakes

**Left -- BLOCK F: Best Practices (X: 0.5", W: 11.0"):**

Teal-accented checklist:
- `Mask AFTER cleaning, BEFORE grit blast -- never mask over contamination`
- `Verify mask adhesion after blast -- blast can lift tape edges`
- `Check mask integrity between bond coat and SPS topcoat passes`
- `Remove masks carefully -- avoid chipping coating edges`
- `Label all masks for re-use tracking`

**Right -- BLOCK G: 4 Common Mistakes (X: 12.0", W: 11.5"):**

| Mistake | Consequence |
|---|---|
| Masking over contamination | Trapped contaminants cause delamination |
| Tape not rated for temperature | Burns, melts, or leaves residue |
| Shadow from fixture | Uncoated areas or thin spots |
| No splash shield (SPS) | Liquid overspray contaminates masked surfaces |

---

### ZONE 5 -- SPS-Specific Considerations

**Section label:** `SPS-SPECIFIC MASKING NOTES` -- Y: 28.7".

| Card | Note |
|---|---|
| 1 | Liquid overspray: suspension that misses the plasma plume is still liquid ethanol/water with particles -- it splashes |
| 2 | Ethanol atmosphere: booth has flammable vapor -- masking materials must be non-sparking and ethanol-resistant |
| 3 | Check masks between APS bond coat and SPS topcoat -- bond coat spray may shift mask position |
| 4 | SPS produces finer overspray particles than APS -- masking seals need to be tighter to prevent infiltration |

---

### ZONE 6 -- Footer

Standard. Title: `Masking & Fixturing -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones. **Light Remap:** Standard table. **Export:** Six files.

---

*Alaina -- Poster #543 -- Construction Workup v1.0 -- 2026-04-26*
