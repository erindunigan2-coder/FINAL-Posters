---
Project: Plating Posters Inc
Poster Number: 497
Title: "Post-Treatment -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 9)"
Technical Source: HVOF post-treatment. Grinding is the PRIMARY post-treatment (diamond or CBN wheels, wet grinding mandatory, 5-15 um infeed per pass, achievable Ra 0.1-0.4 um). Sealing generally NOT required for WC-Co (<1% porosity). No diffusion heat treatment needed -- coatings are functional as-sprayed and ground.
Process Scope: HVOF thermal spray -- post-spray grinding, sealing, and finishing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - PostTreatment
  - Grinding
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #497 -- Construction Workup
## Post-Treatment -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 9 of the HVOF process. Unlike APS (which has three post-treatment paths: seal, grind, heat treat), HVOF is overwhelmingly about GRINDING. The coating is so dense that sealing is rarely needed, and no diffusion heat treatment is required. The hero is a grinding specification table -- this is where HVOF coatings are brought to final dimension and surface finish. The key message: wet grinding is mandatory, light cuts only, and the achievable finish matches ground hard chrome.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Grinding specification table (Block B -- HERO):** Complete grinding parameters with wheel types, speeds, infeed, and achievable finishes.
2. **HVOF vs. APS post-treatment comparison (Block C):** Shows how much simpler HVOF post-treatment is.
3. **Superfinishing and lapping callout (Block D):** For Ra < 0.1 um applications.
4. **Sealing decision tree (Block E):** When sealing IS needed (rare cases).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 9 highlighted (Amber)
ZONE 3 -- GRINDING SPECIFICATION HERO (4.2"--15.5" / ~11.3")
  Block B: Grinding parameter table
  Block C: HVOF vs. APS post-treatment comparison
ZONE 4 -- SUPERFINISHING (15.5"--22.0" / ~6.5")
  Block D: Lapping and superfinishing for ultra-smooth surfaces
ZONE 5 -- SEALING DECISION (22.0"--28.5" / ~6.5")
  Block E: When to seal (and when NOT to)
ZONE 6 -- WET GRINDING CALLOUT (28.5"--32.5" / ~4.0")
  Block F: Mandatory wet grinding banner
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 80 pt `#F0EDE8`.
**Subheading:** `HVOF -- Grind to Dimension, Finish to Spec -- Stage 9 of 10` -- 32 pt `#E8A020`. Y: 1.4".
**Tagline:** `HVOF coatings are so dense that sealing is rarely needed. Grinding IS the post-treatment. Light cuts, wet grinding, and a finish that matches ground hard chrome.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 9 highlighted (Amber). Others dimmed.

---

### ZONE 3 -- Grinding Specification (HERO)

**Section label:** `GRINDING HVOF COATINGS -- THE PRIMARY POST-TREATMENT` -- Y: 4.4".

**BLOCK B -- Grinding Parameter Table (top half)**

Y: 5.0" to 10.0". Full width.

| Parameter | Value | Notes |
|---|---|---|
| Wheel type (WC-Co) | Diamond (resin or vitrified bond) | Diamond is the only effective abrasive for WC |
| Wheel type (metallic) | CBN or SiC | For NiCrBSi, Stellite, Inconel coatings |
| Surface speed | 20-30 m/s | Standard production grinding speeds |
| Infeed | 5-15 um per pass | Light cuts ONLY -- heavy cuts cause pullout and microcracking |
| Coolant | Soluble oil, wet grinding | MANDATORY -- dry grinding causes thermal damage |
| Achievable finish (Ra) | 0.1-0.4 um | Matches ground hard chrome |
| Stock removal | 50-200 um from as-sprayed | Spray over-dimension to allow grinding to final size |
| Superfinishing | Ra < 0.1 um possible with lapping | For seal surfaces, hydraulic cylinder rods |
| As-sprayed Ra | 3-6 um | Always requires grinding for functional surfaces |

Header: fill `#3A4055`, Barlow SemiBold 13 pt. Data: JetBrains Mono 12 pt `#F0EDE8`. Infeed and coolant values in `#E05C5C` for emphasis.

**BLOCK C -- HVOF vs. APS Post-Treatment (bottom half)**

Y: 10.5" to 15.3". Two side-by-side comparison cards.

**Left -- HVOF Post-Treatment (W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `HVOF -- SIMPLE` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
1. Grind to dimension (diamond wheels)
2. Verify surface finish (Ra 0.1-0.4 um)
3. Done.

No sealing required (porosity < 1%)
No heat treatment required
Coating is fully functional as-ground
```

Accent: `HVOF post-treatment is grinding. That is it.` Inter Medium 14 pt `#E8A020`.

**Right -- APS Post-Treatment (Reference) (W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `APS -- THREE PATHS` Barlow SemiBold 18 pt `#2EC4B6`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
1. SEAL -- epoxy/silicone/AlPO4 (porous coatings)
2. GRIND -- diamond for ceramics, CBN for metals
3. HEAT TREAT -- vacuum 1050 degC for MCrAlY

Multiple paths depending on coating type
Sealing often mandatory (5-15% porosity)
Heat treatment for TBC bond coats
More complex post-processing workflow
```

---

### ZONE 4 -- Superfinishing

**Section label:** `SUPERFINISHING AND LAPPING -- FOR ULTRA-SMOOTH SURFACES` -- Y: 15.7".

**BLOCK D -- Superfinishing Callout**

Y: 16.3" to 21.8". Two-column layout.

**Left -- When Superfinishing Is Required (W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `APPLICATIONS REQUIRING Ra < 0.1 um` Barlow SemiBold 16 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
- Hydraulic cylinder rods (seal surfaces)
- Pump shafts (mechanical seal contact)
- Valve stems (high-pressure sealing)
- Precision bearing journals

Standard diamond grinding achieves Ra 0.1-0.4 um.
For Ra < 0.1 um, use diamond lapping or
superfinishing (honing) after grinding.
```

**Right -- Superfinishing Methods (W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `METHODS` Barlow SemiBold 16 pt `#E8A020`

| Method | Achievable Ra | Notes |
|---|---|---|
| Diamond lapping | 0.02-0.1 um | Manual or machine; diamond paste abrasive |
| Superfinishing (honing) | 0.05-0.1 um | Oscillating stone or tape on rotating part |
| Polishing | 0.01-0.05 um | Diamond compound on lap; mirror finish |

Note: `Superfinished HVOF WC-Co surfaces are visually indistinguishable from polished hard chrome. The surface finish is NOT the limitation -- HVOF matches or exceeds chrome at every roughness level.` Inter Medium 12 pt `#F0EDE8` at 70%.

---

### ZONE 5 -- Sealing Decision

**Section label:** `TO SEAL OR NOT TO SEAL` -- Y: 22.2".

**BLOCK E -- Sealing Decision Tree**

Y: 22.9" to 28.3". Three cards side by side.

**Card 1 -- DO NOT SEAL (most HVOF) (W: 7.33"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `NO SEAL NEEDED` Barlow SemiBold 16 pt `#27AE60`
- Content:
```
Standard WC-Co, WC-CoCr, CrC-NiCr coatings
Porosity < 1% -- no interconnected pore network
Coating is inherently dense and corrosion-resistant
This is the default for most HVOF applications
```

**Card 2 -- SEAL FOR CORROSION (rare) (W: 7.33"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `SEAL IF SPECIFIED` Barlow SemiBold 16 pt `#E8A020`
- Content:
```
Salt spray environments (ASTM B117 > 500 hrs)
Marine and offshore applications
Chemical exposure environments
Use: epoxy or phenolic vacuum impregnation
```

**Card 3 -- SEAL FOR HIGH TEMP (specialty) (W: 7.33"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E05C5C`
- Title: `HIGH-TEMP SEAL` Barlow SemiBold 16 pt `#E05C5C`
- Content:
```
Elevated temperature service (> 300 degC)
Use: aluminum phosphate inorganic sealer
Note: WC decomposes above ~540 degC
Consult application engineer for temp limits
```

---

### ZONE 6 -- Wet Grinding Callout

**BLOCK F -- Full-Width Banner**

- Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`

**Main text:** `WET GRINDING IS MANDATORY -- NEVER DRY GRIND HVOF COATINGS` Barlow Condensed ExtraBold 28 pt `#E05C5C`.
**Sub-text:** `Dry grinding generates thermal shock that causes microcracking and subsurface damage. Use soluble oil coolant. Infeed 5-15 um per pass only. Heavy cuts cause carbide pullout and surface pitting that no amount of polishing can fix.` Inter Medium 16 pt `#F0EDE8`.

---

### ZONE 7 -- Footer

Standard. Title: `Post-Treatment -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post-Treatment HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The simplicity of HVOF post-treatment compared to APS is the story here. APS has three paths (seal, grind, heat treat). HVOF has one: grind. The side-by-side comparison makes this visually obvious. The wet grinding callout is non-negotiable safety/quality content -- dry grinding HVOF coatings is one of the most common and expensive mistakes in the industry. The superfinishing section addresses the "can HVOF match chrome finish?" question with a definitive yes.

---

*Alaina -- Poster #497 -- Construction Workup v1.0 -- 2026-04-26*
