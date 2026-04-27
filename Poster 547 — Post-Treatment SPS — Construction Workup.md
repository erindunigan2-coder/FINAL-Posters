---
Project: Plating Posters Inc
Poster Number: 547
Title: "Post-Treatment -- Suspension Plasma Spray (SPS)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 7: SPS)"
Technical Source: SPS TBCs typically receive NO post-treatment. The columnar microstructure and intentional porosity are functional -- grinding destroys columns, sealing defeats thermal insulation. Bond coat diffusion heat treatment is done BEFORE SPS topcoat, not after. Non-TBC SPS applications (wear, biomedical) may receive light polish or biocompatible sealing.
Process Scope: SPS post-spray treatment (or deliberate lack thereof)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - SPS
  - PostTreatment
  - ConstructionWorkup
  - ClusterTS07
---

# Poster #547 -- Construction Workup
## Post-Treatment -- Suspension Plasma Spray (SPS)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the poster that says "DON'T." For TBC applications -- which are the primary SPS use case -- the answer to "what post-treatment?" is almost always "none." The columnar structure IS the product. Grinding it flat destroys the columns. Sealing the porosity defeats the thermal insulation. The hero message is a big, bold "DO NOT" panel for TBCs, balanced against a smaller section covering the exceptions (non-TBC SPS applications).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- "DO NOT" HERO FOR TBCs (2.9"--15.5")
  Block B: Three large "DO NOT" panels -- grinding, sealing, quenching
  Block C: Why the as-sprayed state is functional
ZONE 3 -- BOND COAT HEAT TREATMENT (15.5"--22.0")
  Block D: Diffusion heat treatment details (done BEFORE SPS topcoat)
  Block E: Heat treatment sequencing timeline
ZONE 4 -- NON-TBC SPS EXCEPTIONS (22.0"--28.5")
  Block F: Wear coating post-treatment
  Block G: Biomedical coating post-treatment
ZONE 5 -- DECISION FLOWCHART (28.5"--32.5")
  Block H: "Is it a TBC?" decision strip
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Suspension Plasma Spray (SPS) -- When "Do Nothing" Is the Right Answer` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `For thermal barrier coatings, the as-sprayed columnar structure IS the product. Grinding destroys it. Sealing defeats it. Know when to leave it alone.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- "DO NOT" Hero for TBCs

**Section label:** `TBC APPLICATIONS -- PRESERVE THE COLUMNAR STRUCTURE` -- Y: 3.1".

**BLOCK B -- Three "DO NOT" Panels**

Y: 3.8" to 11.5". Three large cards in a single row.

Each card: Rounded rect, W: 7.33", H: 7.5", fill `#1E2435`, left accent `#E05C5C` 0.06", radius 6.

| Card | X | Title | Body |
|---|---|---|---|
| 1 | 0.5" | DO NOT GRIND | Grinding removes column tips and destroys the columnar architecture. The strain tolerance that makes SPS superior to APS comes from independent columns -- flatten them and you have an expensive lamellar coating. |
| 2 | 8.0" | DO NOT SEAL | SPS TBC porosity is FUNCTIONAL. Inter-columnar gaps reduce thermal conductivity (0.7--1.2 W/mK). Sealing fills these gaps and increases heat transfer to the substrate -- defeating the coating's purpose. |
| 3 | 15.5" | DO NOT QUENCH | Rapid cooling after spraying induces thermal shock in the columnar structure. Controlled cool-down preserves column integrity. Allow the coated part to cool slowly in ambient air. |

Title: Barlow Condensed ExtraBold 28 pt `#E05C5C`.
Body: Inter Regular 14 pt `#F0EDE8`, line height 155%.

**BLOCK C -- Why As-Sprayed Is Functional**

Y: 12.0" to 15.3". Rounded rect, W: 23.0", H: 3.0", fill `#252B3D`, radius 6.

Title: `THE AS-SPRAYED STATE IS THE PRODUCT` -- Barlow SemiBold 22 pt `#27AE60`. Centered.

Three-column metric strip:

| Metric | Value | Note |
|---|---|---|
| Porosity | 10--25% | Reduces thermal conductivity |
| Column structure | 50--200 um wide | Each column flexes independently |
| Surface finish | As-sprayed (Ra 5--15 um) | Acceptable for TBC function |

`Unlike conventional coatings, SPS TBCs do not need finishing. The microstructure you sprayed is the microstructure you want.` Inter Medium 14 pt `#27AE60`.

---

### ZONE 3 -- Bond Coat Heat Treatment

**Section label:** `BOND COAT DIFFUSION HEAT TREATMENT` -- Y: 15.7".

**Left -- BLOCK D: Heat Treatment Details (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06".

Title: `MCrAlY BOND COAT -- DIFFUSION TREATMENT` -- Barlow SemiBold 18 pt `#E8A020`.

| Parameter | Value |
|---|---|
| Temperature | 1050--1080 degC |
| Atmosphere | Vacuum or inert (argon) |
| Duration | 2--4 hours |
| Purpose | Interdiffusion between bond coat and substrate; improves adhesion and oxidation resistance |
| Timing | BEFORE SPS topcoat application |

Data: JetBrains Mono 12 pt.

Note: `This is a bond coat treatment, not a topcoat treatment. It is done after APS bond coat and before SPS topcoat.` Inter Medium 13 pt `#E8A020`.

**Right -- BLOCK E: Sequencing Timeline (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`.

Title: `PROCESS SEQUENCE` -- Barlow SemiBold 18 pt `#F0EDE8`.

Vertical sequence (5 steps with downward arrows):

1. `APS Bond Coat (MCrAlY)` -- badge `#E8A020`
2. `Diffusion Heat Treatment (vacuum, 1050--1080 degC, 2--4 hr)` -- badge `#E8A020`
3. `Cool to Room Temperature` -- badge `#2EC4B6`
4. `SPS Topcoat (YSZ)` -- badge `#27AE60`
5. `Controlled Cool-Down -- DONE` -- badge `#2EC4B6`

Each step: Rounded rect W: 10.5", H: 0.8", fill `#252B3D`. Text: Inter Medium 13 pt.

Arrow between step 2 and 3: `Critical sequence -- do NOT apply SPS before heat treatment` `#E05C5C` 12 pt.

---

### ZONE 4 -- Non-TBC Exceptions

**Section label:** `NON-TBC SPS APPLICATIONS -- EXCEPTIONS` -- Y: 22.2".

**Left -- BLOCK F: Wear Coatings (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".

Title: `WEAR-RESISTANT SPS COATINGS` -- Barlow SemiBold 18 pt `#2EC4B6`.

- `Light polishing may be applied for dimensional control`
- `Avoid aggressive grinding -- finer microstructure is more sensitive`
- `Diamond lapping preferred over wheel grinding`
- `Sealing with epoxy acceptable for non-thermal applications`
- `These applications are less common -- SPS is primarily a TBC process`

**Right -- BLOCK G: Biomedical Coatings (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06".

Title: `BIOMEDICAL SPS COATINGS` -- Barlow SemiBold 18 pt `#2EC4B6`.

- `Hydroxyapatite (HA) coatings on orthopedic implants`
- `Sealing with biocompatible polymers may be specified`
- `Surface roughness may be controlled for cell adhesion`
- `Porosity may be intentional (bone ingrowth) or minimized`
- `Follow FDA/ISO 13485 requirements for implant coatings`

---

### ZONE 5 -- Decision Flowchart

**Section label:** `POST-TREATMENT DECISION` -- Y: 28.7".

**BLOCK H -- Decision Strip**

Three-box horizontal decision flow:

Box 1 (X: 0.5", W: 7.0"): `IS IT A TBC?` -- Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Fill `#3A4055`.

Arrow right to Box 2 (X: 8.0", W: 7.0"):
- Top path: `YES` in `#27AE60` -> `NO POST-TREATMENT. Controlled cool-down only. Leave the columnar structure intact.` Fill `#1E2435`, left accent `#27AE60`.
- Bottom path: `NO` in `#E8A020` -> Box 3 (X: 15.5", W: 8.0"): `Light polish or seal per specification. Consult application-specific requirements.` Fill `#1E2435`, left accent `#E8A020`.

---

### ZONE 6 -- Footer

Standard. Title: `Post-Treatment -- Suspension Plasma Spray (SPS)`. Version `v1.0 -- 2026`.

Disclaimer: `SPS TBCs are an emerging technology. Post-treatment practices are evolving. The "no post-treatment" guidance applies to thermal barrier coatings -- other SPS applications may require finishing. Consult your coating supplier.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post-Treatment SPS -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

*Alaina -- Poster #547 -- Construction Workup v1.0 -- 2026-04-26*
