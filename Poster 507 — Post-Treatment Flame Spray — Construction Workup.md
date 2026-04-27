---
Project: Plating Posters Inc
Poster Number: 507
Title: "Post-Treatment -- Flame Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Process Scope: Post-treatment for flame spray -- sealing, fusing self-fluxing alloys, machining, grinding
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - PostTreatment
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #507 -- Construction Workup
## Post-Treatment -- Flame Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Post-treatment is where flame spray gets interesting. This is the only thermal spray process with a widely used fusing step -- self-fluxing NiCrBSi alloys can be torch-fused or furnace-fused to near-zero porosity with a true metallurgical bond. That fusing capability is flame spray's unique superpower. The hero content is a three-path decision tree: Seal, Fuse, or Machine. The critical safety message: fusing temperatures (1000--1100 degC) exceed most substrate limits.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-path decision tree (Block B -- HERO):** Seal / Fuse / Machine -- which path applies to which coating type.
2. **Fusing deep-dive panel (Block C):** Torch fusing vs. furnace fusing comparison with property improvements.
3. **Sealing options table (Block D):** Epoxy, phenolic, wax, and their applications.
4. **Machining guide (Block E):** Grinding and turning options for flame spray coatings.
5. **Safety warning strip (Block F):** Fusing temperature warnings.

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
  Stage 7 highlighted (Amber)
ZONE 3 -- THREE-PATH DECISION TREE / HERO (4.2"--15.5" / ~11.3")
  Block B: Seal / Fuse / Machine decision paths
  Block C: Fusing deep-dive (torch vs. furnace)
ZONE 4 -- SEALING OPTIONS (15.5"--22.0" / ~6.5")
  Block D: Sealer types and applications
ZONE 5 -- MACHINING GUIDE (22.0"--28.5" / ~6.5")
  Block E: Grinding and turning reference
ZONE 6 -- SAFETY WARNINGS (28.5"--32.5" / ~4.0")
  Block F: Fusing temperature and substrate warnings
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 88 pt `#F0EDE8`.
**Subheading:** `Flame Spray -- Seal, Fuse, or Machine to Specification` -- 36 pt `#E8A020` (Amber).
**Tagline:** `Flame spray's secret weapon: self-fluxing alloys that can be fused to near-zero porosity. No other thermal spray process does this routinely at shop-floor level.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating sprayed to target thickness --> After: Coating sealed, fused, or machined to final specification`

---

### ZONE 3 -- Three-Path Decision Tree (HERO)

**Section label:** `POST-TREATMENT PATHS -- CHOOSE BASED ON COATING TYPE` -- Y: 4.4".

**BLOCK B -- Three Decision Paths**

Y: 5.0" to 10.5". Three tall cards side by side.

Each card: W: 7.3", H: 5.3", fill `#1E2435`, radius 6.

**Card 1 -- SEAL (X: 0.5"):**
- Top accent: 4 pt `#2EC4B6` (Teal)
- Title: `PATH 1: SEAL` Barlow SemiBold 22 pt `#2EC4B6`
- When: `Zinc/aluminum corrosion coatings, general metallic coatings where porosity must be blocked`
- Method: `Epoxy, phenolic, wax, or silicone sealer applied by brush, spray, or vacuum impregnation`
- Result: `Fills interconnected porosity; prevents moisture ingress; extends service life`
- Key fact: `Essential for Zn/Al corrosion coatings per AWS C2.18 -- seal within 4 hours of spray`

**Card 2 -- FUSE (X: 8.15"):**
- Top accent: 4 pt `#E8A020` (Amber)
- Title: `PATH 2: FUSE` Barlow SemiBold 22 pt `#E8A020`
- When: `Self-fluxing alloys only (NiCrBSi, NiBSi, CoCrWC blends)`
- Method: `Oxy-acetylene torch fusing or furnace fusing at 1000--1100 degC`
- Result: `Porosity drops from 5--15% to <1%; bond becomes metallurgical (>70 MPa); hardness increases to 700--900 HV`
- Key fact: `CRITICAL: Fusing temperature exceeds capability of most substrates. Verify part can withstand 1000+ degC.` -- this line in `#E05C5C`

**Card 3 -- MACHINE (X: 15.85"):**
- Top accent: 4 pt `#27AE60` (Emerald)
- Title: `PATH 3: MACHINE` Barlow SemiBold 22 pt `#27AE60`
- When: `Dimensional repair, bearing surfaces, any coating requiring a finished dimension`
- Method: `Conventional turning/milling (soft metals) or diamond grinding (hard/fused coatings)`
- Result: `Achievable finish: Ra 0.2--1.6 microns depending on coating material`
- Key fact: `Stock removal: typically 50--200 microns from as-sprayed surface. Spray oversize to allow for grinding.`

Card interior formatting:
- When: Inter Regular 13 pt `#F0EDE8` at 70%. Label `WHEN:` Inter Medium 12 pt accent color.
- Method: Inter Regular 14 pt `#F0EDE8`. Label `METHOD:` Inter Medium 12 pt accent color.
- Result: Inter Regular 14 pt `#F0EDE8`. Label `RESULT:` Inter Medium 12 pt accent color.
- Key fact: Inter Medium 13 pt accent color (or `#E05C5C` where flagged).

**BLOCK C -- Fusing Deep-Dive**

Y: 11.0" to 15.0".

Section sublabel: `SELF-FLUXING ALLOY FUSING -- FLAME SPRAY'S UNIQUE ADVANTAGE` Barlow SemiBold 18 pt `#E8A020`. Y: 11.0".

Two panels side by side:

**Left -- Torch Fusing (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `TORCH FUSING (OXY-ACETYLENE)` Barlow SemiBold 16 pt `#E8A020`
- `Operator heats coating surface with neutral flame until it "sweats" -- a glossy, wet appearance indicating the alloy has remelted`
- `Temperature: 1000--1100 degC at coating surface`
- `Operator skill-dependent; visual endpoint (sweat test)`
- `Best for: field work, small areas, repair jobs`
- `Risk: uneven heating can cause localized overheating or incomplete fusion`

**Right -- Furnace Fusing (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `FURNACE FUSING` Barlow SemiBold 16 pt `#2EC4B6`
- `Vacuum or controlled atmosphere furnace at 1000--1100 degC`
- `Uniform heating -- entire coating fuses simultaneously`
- `More consistent results than torch fusing`
- `Best for: production work, critical components, tight tolerances`
- `Higher capital cost but superior repeatability`

Below panels -- property improvement summary:
- Rounded rect, fill `#252B3D`, W: 23.0", H: 1.2"

| Property | As-Sprayed | After Fusing |
|---|---|---|
| Porosity | 5--15% | <1% |
| Bond strength | 10--30 MPa (mechanical) | >70 MPa (metallurgical) |
| Hardness (NiCrBSi) | 300--500 HV | 700--900 HV |

Values: JetBrains Mono 13 pt. As-sprayed values `#F0EDE8` at 60%. After-fusing values `#E8A020`.

---

### ZONE 4 -- Sealing Options

**Section label:** `SEALING OPTIONS FOR POROUS FLAME SPRAY COATINGS` -- Y: 15.7".

**BLOCK D -- Sealer Comparison Table**

Y: 16.3" to 21.5".

| Sealer Type | Application Method | Max Service Temp | Best For |
|---|---|---|---|
| Epoxy | Brush, spray, or vacuum impregnation | 120 degC (250 degF) | General corrosion protection; Zn/Al coatings on steel |
| Phenolic | Brush or spray | 150 degC (300 degF) | Chemical resistance applications |
| Silicone | Brush or spray | 250 degC (480 degF) | Higher-temperature service; Al coatings on exhaust systems |
| Wax | Dip or brush | 60 degC (140 degF) | Low-cost applications; temporary protection |
| Aluminum phosphate | Spray or brush | 800 degC (1470 degF) | High-temperature inorganic sealer; specialty applications |

Table header: fill `#3A4055`. Data rows: alternating `#1E2435` / `#252B3D`.
Sealer type: Inter Medium 14 pt `#2EC4B6`. Values: Inter Regular 13 pt. Temp: JetBrains Mono 13 pt `#E8A020`.

Below table:
- Callout, left accent `#2EC4B6`: `For zinc/aluminum corrosion coatings per AWS C2.18: apply seal coat within 4 hours of spray completion. Do not allow moisture to enter the porous coating before sealing.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 5 -- Machining Guide

**Section label:** `MACHINING FLAME SPRAY COATINGS` -- Y: 22.2".

**BLOCK E -- Machining Reference**

Y: 22.8" to 28.0".

Two panels side by side:

**Left -- Conventional Machining (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `TURNING & MILLING` Barlow SemiBold 18 pt `#27AE60`
- `Suitable for: soft metallic coatings (zinc, aluminum, bronze, babbitt, un-fused NiCrBSi)`
- `Use carbide tooling; avoid high-speed steel (wears too fast on sprayed coatings)`
- `Light cuts: 0.1--0.3 mm depth of cut`
- `Use coolant to avoid thermal shock and coating pullout`
- `Achievable finish: Ra 1.6--6.3 microns`

**Right -- Diamond Grinding (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `DIAMOND GRINDING` Barlow SemiBold 18 pt `#E8A020`
- `Required for: hard coatings (fused NiCrBSi, stellite, WC blends, ceramics)`
- `Diamond or CBN wheels (resin or vitrified bond)`
- `Wet grinding mandatory -- coolant prevents thermal damage`
- `Infeed: 5--15 microns per pass`
- `Achievable finish: Ra 0.2--1.6 microns`
- `Superfinishing/lapping possible for Ra < 0.1 microns`

Below panels:
- `Stock removal allowance: spray 50--200 microns oversize to allow for machining to final dimension. Account for this in your spray thickness target.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Safety Warnings

**Section label:** `CRITICAL POST-TREATMENT WARNINGS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Warning | Detail |
|---|---|---|---|
| 1 | 0.5" | FUSING EXCEEDS SUBSTRATE LIMITS | Most steels, all aluminum alloys, and heat-treated parts cannot survive 1000--1100 degC fusing. Verify substrate compatibility BEFORE spraying self-fluxing alloy. |
| 2 | 6.33" | TORCH FUSING FIRE HAZARD | Open oxy-acetylene flame at 1000+ degC. Full fire watch; clear all combustibles within 10 m; fire extinguisher at hand. |
| 3 | 12.16" | SEAL BEFORE MOISTURE | Porous coatings absorb moisture within hours. Seal Zn/Al coatings within 4 hours of spray or the seal will trap moisture at the interface. |
| 4 | 18.0" | GRINDING DUST HAZARD | NiCrBSi, stellite, and WC grinding dust is hazardous. Wet grinding + local exhaust ventilation mandatory. RPE if dry grinding unavoidable. |

---

### ZONE 7 -- Footer

Standard footer. Title: `Post-Treatment -- Flame Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; AWS C2.18; general industry knowledge. Fusing temperatures and sealer properties are typical ranges. Consult your coating specification and substrate material data before post-treatment.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #507 -- Construction Workup v1.0 -- 2026-04-26*
