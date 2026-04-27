---
Project: Plating Posters Inc
Poster Number: 78
Title: "Post Treatment -- Nickel-Cobalt"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-06 technical reference (nickel-cobalt alloy plating)"
Technical Source: Post-treatment stage for nickel-cobalt alloy plating. Three primary post-treatment paths -- (1) chromium topcoat for maximum wear resistance, (2) heat treatment to increase hardness from 400-500 HV to 600-700 HV, and (3) final deposit with no topcoat for magnetic applications. Hydrogen embrittlement bake required for high-strength steel substrates. Stage 7-8 combined (post-treatment + final inspection). Stage 8 of 8.
Process Scope: Post-treatment for nickel-cobalt alloy plating (Stage 8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelCobaltPlating
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEP06
---

# Poster #78 -- Construction Workup
## Post Treatment -- Nickel-Cobalt

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 8 (combines post-treatment and final inspection). NiCo post-treatment is more complex than most plating processes because the deposit serves multiple applications with different post-treatment paths. Aerospace turbine components often receive a chromium topcoat for maximum wear. Tooling and mold applications may use heat treatment to push hardness from 400-500 HV to 600-700 HV. Magnetic applications (historically important, now niche) use the NiCo deposit as-is. And all high-strength steel substrates require a hydrogen embrittlement relief bake within hours of plating.

Hero visual: a three-path decision flowchart -- "What is your application?" branching to chromium topcoat, heat treatment, or as-plated magnetic deposit.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Three-path decision flowchart hero (Block B):** Branching from application to post-treatment path. Same flowchart pattern as Poster #74 (Activation).
2. **Heat treatment detail panel (Block D):** Temperature ramp, hold time, atmosphere, and hardness result.
3. **H-embrittlement bake callout (Block E):** Mandatory for high-strength steel -- time, temperature, and the 4-hour rule.
4. **Final inspection checklist (Block F):** What to verify before shipping.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- POST-TREATMENT DECISION FLOWCHART HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- HEAT TREATMENT DETAIL (14.5"--20.5" / ~6.0")
ZONE 5 -- H-EMBRITTLEMENT BAKE + CHROMIUM TOPCOAT (20.5"--26.5" / ~6.0")
ZONE 6 -- FINAL INSPECTION CHECKLIST (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel-Cobalt Plating -- Stage 8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Three roads out of the plating tank. Chrome topcoat for wear. Heat treat for hardness. Or ship as-plated for magnetics. Know your spec before you start.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Y: 2.9" to 4.2".

Eight mini boxes. Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Rinsed NiCo deposit  -->  After: Post-treated, inspected, and ready for service`

---

### ZONE 3 -- Post-Treatment Decision Flowchart Hero

**Section label:** `WHAT IS YOUR APPLICATION? -- CHOOSE YOUR POST-TREATMENT` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Decision Flowchart**

Y: 5.0" to 14.0".

**Start node (top center):**
- Rounded rect, X: 8.5", Y: 5.0", W: 7.0", H: 1.2", fill `#E8A020`, radius 8
- Text: `APPLICATION?` Barlow Condensed ExtraBold 22 pt `#1A1F2E`

**Three branches below:**

**Branch 1 -- Wear / Turbine (left):**
- Arrow from start node down-left to:
- Rounded rect, X: 0.5", Y: 7.0", W: 7.0", H: 1.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `AEROSPACE / TURBINE / WEAR` Barlow SemiBold 16 pt `#2EC4B6`
- Arrow down to:
- Rounded rect, X: 0.5", Y: 9.0", W: 7.0", H: 3.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Method: `CHROMIUM TOPCOAT` Barlow SemiBold 18 pt `#F0EDE8`
- `Hard chrome over NiCo` JetBrains Mono 14 pt `#2EC4B6`
- `Provides: corrosion + wear combo`
- `The NiCo acts as intermediate hard layer`
- `Chrome provides surface hardness (800+ HV)`
- `Often per AMS 2424 + AMS 2406/2460`
- Arrow down to:
- Result box: fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `MAXIMUM WEAR RESISTANCE` Inter Medium 14 pt `#27AE60`

**Branch 2 -- Hardness / Tooling (center):**
- Arrow from start node straight down to:
- Rounded rect, X: 8.0", Y: 7.0", W: 8.0", H: 1.5", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `TOOLING / MOLDS / HARD FACING` Barlow SemiBold 16 pt `#E8A020`
- Arrow down to:
- Rounded rect, X: 8.0", Y: 9.0", W: 8.0", H: 3.5", fill `#1E2435`, left accent 0.06" `#E8A020`
- Method: `HEAT TREATMENT` Barlow SemiBold 18 pt `#F0EDE8`
- `300 C (572 F) for 1--4 hr` JetBrains Mono 14 pt `#E8A020`
- `As-plated: 400--500 HV`
- `Heat treated: 600--700 HV`
- `Controlled atmosphere (inert or vacuum)`
- `See Zone 4 for full detail`
- Arrow down to:
- Result box: fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `MAXIMUM HARDNESS (600--700 HV)` Inter Medium 14 pt `#E8A020`

**Branch 3 -- Magnetic (right):**
- Arrow from start node down-right to:
- Rounded rect, X: 17.0", Y: 7.0", W: 6.5", H: 1.5", fill `#1E2435`, top accent 4 pt `#C8D0D8`
- Title: `MAGNETIC / RECORDING (LEGACY)` Barlow SemiBold 16 pt `#C8D0D8`
- Arrow down to:
- Rounded rect, X: 17.0", Y: 9.0", W: 6.5", H: 3.5", fill `#1E2435`, left accent 0.06" `#C8D0D8`
- Method: `AS-PLATED (NO TOPCOAT)` Barlow SemiBold 16 pt `#F0EDE8`
- `NiCo deposit is the final surface` JetBrains Mono 13 pt `#C8D0D8`
- `Magnetic permeability tuned via Co%`
- `Higher Co% = higher permeability`
- `Largely historical (tape/disk heads)`
- `Some niche sensor applications remain`
- Arrow down to:
- Result box: fill `#C8D0D8` at 15%, border 1 pt `#C8D0D8`
- `MAGNETIC PROPERTIES` Inter Medium 14 pt `#C8D0D8`

**H-embrittlement warning banner (Y: 13.5"):**
- Full-width rounded rect, X: 0.5", W: 23.0", H: 0.6", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `ALL PATHS: High-strength steel (>=40 HRC) requires H-embrittlement bake 375 F / 4+ hr WITHIN 4 HOURS of plating. No exceptions.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 4 -- Heat Treatment Detail

**Section label:** `HEAT TREATMENT -- HARDNESS UPGRADE` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Heat Treatment Parameter Table (Y: 15.3" to 18.5")**

Column widths (23.0" total):
- Parameter (5.5") | Range (5.5") | Optimal (5.5") | Notes (6.5")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Parameter | Range | Optimal | Notes |
|---|---|---|---|
| Temperature | 250--350 C (482--662 F) | 300 C (572 F) | Higher temp = higher hardness up to limit |
| Time | 1--4 hr at temperature | 2--3 hr | Longer time = more complete transformation |
| Ramp rate | 2--5 C/min | 3 C/min | Too fast causes cracking |
| Atmosphere | Inert (N2, Ar) or vacuum | Vacuum preferred | Prevents oxidation of deposit surface |
| Cooling | Furnace cool or slow air cool | Furnace cool | Do not quench -- thermal shock cracks deposit |
| As-plated hardness | 400--500 HV | -- | Baseline before heat treat |
| Post-heat hardness | 600--700 HV | -- | Verify by Vickers microhardness |
| Co% effect | Higher Co% = higher peak hardness | 20--30% optimal | Below 15% Co: minimal hardening response |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Parameter names: Inter Medium, 13 pt.

**Below-table callout (Y: 18.8"):**

Two side-by-side callouts:

*Left (X: 0.5", W: 11.0"):*
- Rounded rect, fill `#27AE60` at 10%, border 1 pt `#27AE60`
- `THE MECHANISM: Heat treatment causes ordering of the Ni-Co solid solution and precipitation of a hard intermetallic phase. The cobalt content must be sufficient (>15%) for this transformation to produce meaningful hardening.` Inter Regular 12 pt `#F0EDE8`

*Right (X: 12.0", W: 11.5"):*
- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- `WARNING: Excessive cobalt (>35%) or too-rapid heating can cause cracking. Always verify deposit Co% before committing to heat treat. Once cracked, the part is scrap.` Inter Regular 12 pt `#E05C5C`

---

### ZONE 5 -- H-Embrittlement Bake + Chromium Topcoat

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- H-Embrittlement Bake (X: 0.5", W: 11.0"):**

Section label: `HYDROGEN EMBRITTLEMENT RELIEF` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Parameter | Value |
|---|---|
| Temperature | 375 F (190 C) |
| Time | 4 hr minimum (8--24 hr for critical parts) |
| When | Within 4 hr of plating completion |
| Applies to | All steel >= 40 HRC or >= 145 ksi UTS |
| Atmosphere | Air is acceptable |
| Standard | Per ASTM B849, AMS 2759/9 |

- `The 4-hour window is non-negotiable. Hydrogen migrates into grain boundaries during plating. If not baked out promptly, delayed brittle fracture can occur days or weeks later -- catastrophic in aerospace.` Inter Regular 12 pt `#F0EDE8`
- `This bake is NOT the same as the hardness heat treatment. They serve different purposes.` Inter Medium 12 pt `#E8A020`

**Right -- Chromium Topcoat (X: 12.0", W: 11.5"):**

Section label: `CHROMIUM TOPCOAT` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

Callout box: Rounded rect, fill `#1E2435`, left accent 0.06" `#2EC4B6`.

| Parameter | Value |
|---|---|
| Type | Hard chrome (hexavalent) |
| Thickness | 0.5--5 mil typical (per spec) |
| Hardness | 800--1000 HV |
| Applied over | NiCo deposit (after H-bake if required) |
| Purpose | Surface hardness + corrosion barrier |
| Typical spec | AMS 2406 or AMS 2460 over AMS 2424 NiCo |

- `The NiCo layer provides ductile, high-strength foundation. The chrome provides extreme surface hardness. Together they outperform either alone.` Inter Regular 12 pt `#F0EDE8`
- `Activation between NiCo and chrome: reverse etch in chrome bath or mild acid dip. NiCo is easier to activate than stainless or superalloys.` Inter Regular 12 pt `#2EC4B6`

---

### ZONE 6 -- Final Inspection Checklist

**Section label:** `FINAL INSPECTION -- BEFORE IT LEAVES THE SHOP` -- Y: 26.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK F -- Inspection Checklist Table (Y: 27.3" to 32.3")**

Column widths (23.0" total):
- Inspection (5.0") | Method (5.5") | Acceptance Criteria (6.5") | Reference (6.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.7".

| Inspection | Method | Acceptance | Reference |
|---|---|---|---|
| Thickness | XRF or cross-section | Per drawing callout | AMS 2424 |
| Alloy composition | XRF | Co% within spec (typ. 18--25%) | AMS 2424 |
| Hardness | Vickers microhardness | 400--500 HV (as-plated) or 600--700 HV (heat treated) | Per spec |
| Adhesion | Bend test or tape test | No lifting, cracking, or peeling | ASTM B571 |
| Visual | 10x magnification | No pits, nodules, blisters, stains, or skip | Per spec |
| H-bake verification | Time/temp recorder | Bake completed within 4 hr window | ASTM B849 |
| Surface roughness | Profilometer (if specified) | Ra per drawing | Per spec |

Data: JetBrains Mono Regular, 11 pt, `#F0EDE8`. Inspection names: Inter Medium, 13 pt.

**Below-table callout:**
- `AMS 2424 is the primary aerospace specification for nickel-cobalt alloy plating. Always read the current revision and any customer-specific amendments before plating.` Inter Medium 13 pt `#E8A020`

---

### ZONE 7 -- Footer Band

Standard. Title: `Post Treatment -- Nickel-Cobalt`. Version `v1.0 -- 2026`.

**Disclaimer:**

> This poster is an educational reference tool. Post-treatment parameters and inspection criteria shown are typical industry values. Specific heat treatment profiles, H-embrittlement bake requirements, and acceptance criteria are governed by the applicable specification (AMS 2424, ASTM B849, customer PO). Consult your process supplier and quality engineering team for application-specific guidance. Source: General industry knowledge; ASM Handbook Vol. 5; ASTM B849; AMS 2424.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment NiCo -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster combines stages 7 and 8 (post-treatment and final inspection) because NiCo post-treatment is a decision tree, not a single linear step. The three-path flowchart hero mirrors the activation poster's decision flowchart (Poster #74), creating visual consistency within the cluster. The heat treatment detail table is the most technically critical section -- ramp rate and atmosphere are not optional details, they are the difference between a 650 HV deposit and a cracked scrap part.

The H-embrittlement bake gets its own callout because it applies across ALL three post-treatment paths when the substrate is high-strength steel. The 4-hour window is emphasized repeatedly because violation of this requirement is one of the most common and most dangerous failures in aerospace plating.

Watson's brief provided: heat treatment parameters (300 C, 1-4 hr, 600-700 HV), cobalt effect on hardness, chromium topcoat mention, and AMS 2424 reference. I expanded the H-bake detail from standard aerospace practice (ASTM B849) and built the final inspection checklist from typical AMS 2424 acceptance criteria.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #78 -- Construction Workup v1.0*
*2026-04-26*
