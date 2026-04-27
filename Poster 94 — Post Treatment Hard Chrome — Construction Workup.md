---
Project: Plating Posters Inc
Poster Number: 94
Title: "Post Treatment -- Hard Chrome"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-08 technical reference (hard chrome plating)"
  - "Watson Research Brief -- Electroplating Clusters"
Technical Source: Post-treatment for hard chrome -- HE baking (375-430 F, 8-24 hrs, within 1-4 hrs of plating), grinding/honing to final dimension (diamond/CBN wheels on HV 800-1000 deposit), and final inspection (thickness, hardness, adhesion, micro-crack pattern). Governed by AMS 2406, AMS 2460, ASTM B177, ASTM B850. The finishing steps that turn a raw chrome deposit into a precision engineered surface.
Process Scope: Post-treatment for hard chrome plating (Stage 8 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - HardChrome
  - Hexavalent
  - PostTreatment
  - HydrogenEmbrittlement
  - ConstructionWorkup
  - ClusterEP08
---

# Poster #94 -- Construction Workup
## Post Treatment -- Hard Chrome

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 8 of 8. The final poster in the EP-08 Hard Chrome cluster. This is where a raw chrome deposit becomes a precision engineered surface. Three operations define post-treatment: (1) HE baking -- mandatory for nearly all hard chrome work because substrates are typically high-strength steel; (2) grinding/honing to final dimension -- chrome is too hard (HV 800--1000) for conventional machining; and (3) final inspection against specification requirements.

The HE bake is the most time-critical step in the entire hard chrome process. It must commence within 1--4 hours of plating. Miss that window and hydrogen trapped in the steel lattice causes irreversible embrittlement -- cracks that may not appear until the part is in service under load. For aerospace (AMS 2406, AMS 2460), the bake is typically 23 hours at 375 F. There is no shortcut.

Hero visual: HE bake timeline with the critical "start within 1--4 hours" window prominently called out, grinding/honing parameter panel, and specification compliance checklist.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **HE bake timeline hero (Block B):** Horizontal timeline showing plating end -> transfer -> bake start -> bake duration -> cool.
2. **Grinding/honing parameter panel (Block D):** Diamond/CBN wheel specs, surface finish targets.
3. **Inspection checklist (Block E):** Thickness, hardness, adhesion, micro-crack density, visual.
4. **Specification reference table (Block F):** AMS, ASTM, MIL specs.
5. **Safety banner in Zone 1 (Block A2):** Same Cr(VI) warning as Poster #87.
6. **Orientation strip:** Stage 8 highlighted (Amber).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline
  Block A2: Safety banner
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 8 highlighted (Amber)
ZONE 3 -- HE BAKE TIMELINE HERO (4.2"--14.5" / ~10.3")
  Block B: HE bake timeline
  Block C: HE bake parameter table
ZONE 4 -- GRINDING / HONING (14.5"--20.5" / ~6.0")
  Block D: Grinding/honing parameter panel
  Block D2: Surface finish targets
ZONE 5 -- INSPECTION + SPECIFICATIONS (20.5"--27.0" / ~6.5")
  Block E: Inspection checklist
  Block F: Specification reference table
ZONE 6 -- COMMON FAILURES + SAFETY (27.0"--32.5" / ~5.5")
  Block G: Common post-treatment failures
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline:** `POST TREATMENT` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`, letter spacing -4. X: 0.5", Y: 0.5".

**Subheading:** `Hard Chrome -- Stage 8 of 8 -- Bake, Grind, Inspect` -- Barlow SemiBold, 30 pt, `#E8A020`. X: 0.5", Y: 1.3".

**Tagline:** `Miss the bake window and the part is scrap. Grind too aggressively and the chrome cracks. Post-treatment is where precision meets patience.` -- Barlow SemiBold, 18 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.0", W: 15.0".

**BLOCK A2 -- Safety Banner:** Same as Poster #87 and #92. X: 15.5", Y: 1.3", W: 8.0".

---

### ZONE 2 -- Orientation Strip

Stage 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed chrome deposit  -->  After: Baked, ground, inspected -- ready for service`

---

### ZONE 3 -- HE Bake Timeline Hero

**Section label:** `HYDROGEN EMBRITTLEMENT BAKING -- THE NON-NEGOTIABLE STEP` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- HE Bake Timeline**

Y: 5.0" to 10.5". Full width (W: 23.0").

Horizontal timeline bar, fill `#252B3D`, border 2 pt `#E8A020`. Five labeled segments:

- Segment 1 -- Plating Complete (X: 0.5", W: 3.0"): fill `#27AE60` at 15%, border 1 pt `#27AE60`
  - Title: `PLATING COMPLETE` Barlow SemiBold 13 pt `#27AE60`
  - `Parts exit rinse cascade`

- Segment 2 -- Transfer Window (X: 4.0", W: 5.0"): fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
  - Title: `CRITICAL TRANSFER WINDOW` Barlow SemiBold 15 pt `#E05C5C`
  - `MUST enter bake oven within 1--4 hours`
  - `Aerospace (AMS 2406): 1 hour maximum`
  - `General industrial: 4 hours maximum`
  - Large callout: `THE CLOCK STARTS NOW` JetBrains Mono 14 pt `#E05C5C`

- Segment 3 -- Bake (X: 9.5", W: 7.0"): fill `#E8A020` at 15%, border 2 pt `#E8A020`
  - Title: `HE BAKE` Barlow SemiBold 15 pt `#E8A020`
  - `Temperature: 375 F (191 C) minimum`
  - `Aerospace: 375--430 F (191--221 C)`
  - `Duration: 8--24 hours (see ASTM B850 schedule)`
  - `AMS 2406 / AMS 2460: typically 23 hours at 375 F`

- Segment 4 -- Cool (X: 17.0", W: 3.0"): fill `#2EC4B6` at 10%
  - Title: `COOL` Barlow SemiBold 13 pt `#2EC4B6`
  - `Slow cool in oven or still air`
  - `Do not quench`

- Segment 5 -- To Grinding (X: 20.5", W: 3.0"): fill `#27AE60` at 10%
  - Title: `TO GRINDING` Barlow SemiBold 13 pt `#27AE60`
  - `Proceed to finish grind`

Arrow connectors between all segments. JetBrains Mono 12 pt `#F0EDE8` for all parameter text.

**BLOCK C -- HE Bake Parameters by Hardness**

Y: 11.0" to 14.3".

Rounded rect, full width, H: 3.0", fill `#1E2435`, border 1 pt `#E8A020`, radius 8.
Title: `BAKE TIME BY SUBSTRATE HARDNESS (ASTM B850 / AMS 2759/9)` Barlow Condensed ExtraBold, 20 pt, `#E8A020`

| Substrate Hardness (HRC) | Minimum Bake Time | Temperature |
|---|---|---|
| < 31 HRC | Bake not required (but recommended) | 375 F (191 C) |
| 31--39 HRC | 8 hours minimum | 375 F (191 C) |
| 40--47 HRC | 12 hours minimum | 375 F (191 C) |
| 48--55 HRC | 18 hours minimum | 375 F (191 C) |
| > 55 HRC / aerospace | 23 hours at 375 F (AMS 2406) | 375--430 F |
| Spring steel / landing gear | 24 hours at 375 F | 375 F (191 C) |

JetBrains Mono 12 pt `#F0EDE8`. Headers: Barlow SemiBold 13 pt on `#3A4055`.

Below: `If bake is delayed beyond the allowable transfer window, the part must be stripped and re-plated. There is no recovery.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Grinding / Honing

**Section label:** `GRINDING AND HONING TO FINAL DIMENSION` -- Y: 14.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Grinding Parameter Panel**

Y: 15.3" to 18.5".

Two-column layout:

**Left -- Grinding (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`.
Title: `GRINDING` Barlow SemiBold 18 pt `#2EC4B6`

Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Wheel type: Diamond or CBN (cubic boron nitride). Conventional abrasives cannot cut HV 800--1000 chrome.`
- `Wheel grade: Medium bond; open structure for coolant access.`
- `Speed: 5,000--6,500 SFPM typical.`
- `Infeed: 0.0002"--0.001" per pass. Light passes prevent micro-cracking.`
- `Coolant: Flood coolant required. Chrome generates heat quickly.`
- `Stock removal: Plate 0.002"--0.010" over final dimension, then grind back.`

**Right -- Honing (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`.
Title: `HONING` Barlow SemiBold 18 pt `#E8A020`

Body:
- `For bores (hydraulic cylinders, gun barrels, cylinder liners).`
- `Stone type: Diamond or CBN honing stones.`
- `Speed: 100--200 SFPM.`
- `Pressure: Light -- chrome is hard but brittle.`
- `Finish: 4--16 microinch Ra typical for hydraulic cylinders.`
- `Crosshatch: 15--30 degree crosshatch angle for oil retention.`

**BLOCK D2 -- Surface Finish Targets**

Y: 18.8" to 20.3".

Rounded rect, fill `#252B3D`, W: 23.0".

| Application | Surface Finish Target | Method |
|---|---|---|
| Hydraulic cylinders | 4--16 microinch Ra | Hone |
| Piston rings | 8--20 microinch Ra | Grind + lap |
| Mold surfaces | 2--8 microinch Ra | Grind + polish |
| Industrial tooling | 16--32 microinch Ra | Grind |
| Dimensional restoration | Match original spec | Grind or hone |

JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 5 -- Inspection + Specifications

**Two-column layout (Y: 20.7" to 26.8"):**

**Left -- Inspection Checklist (X: 0.5", W: 14.0"):**

Section label: `FINAL INSPECTION` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:

| Check | Method | Acceptance |
|---|---|---|
| Thickness | Magnetic (Fischerscope), X-ray, or mic before/after | Per drawing (typically 0.2--20 mils) |
| Hardness | Vickers micro-hardness (HV 0.1 or HV 0.3) | 800--1000 HV typical; per spec |
| Adhesion | Bend test (ASTM B571), or qualitative per spec | No peeling, flaking, or blistering |
| Surface finish | Profilometer (Ra) | Per application (see Zone 4) |
| Visual | 10x magnification; uniform color, no pitting | No bare spots, staining, or discoloration |
| Micro-crack pattern | Metallographic cross-section (if specified) | Crack density per spec (some apps require micro-cracking) |
| HE bake verification | Time-temperature recorder or oven chart | Documented bake cycle per ASTM B850 |

Inter Regular 12 pt `#F0EDE8`, line height 140%.

**Right -- Specification Reference (X: 15.5", W: 8.0"):**

Section label: `GOVERNING SPECIFICATIONS` Barlow Condensed ExtraBold 18 pt `#E8A020`.

Rounded rect, fill `#1E2435`, border 1 pt `#E8A020`:

| Specification | Coverage |
|---|---|
| AMS 2406 | Hard chrome plating (aerospace) |
| AMS 2460 | Hard chrome, low HE |
| ASTM B177 | Engineering chromium plating |
| ASTM B850 | HE relief baking |
| ASTM B571 | Adhesion testing |
| QQ-C-320 | Chrome plating (federal, legacy) |
| MIL-STD-1501 | Chromium plating requirements |
| ASTM B578 | Micro-hardness of electrodeposits |

JetBrains Mono 10 pt `#F0EDE8`.

---

### ZONE 6 -- Common Failures + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Common Post-Treatment Failures (X: 0.5", W: 14.0"):**

Section label: `WHAT GOES WRONG AFTER PLATING` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

| Failure | Root Cause | Consequence |
|---|---|---|
| Delayed HE bake | Parts sat too long before entering oven | Irreversible embrittlement; scrap |
| Insufficient bake time | Oven timer error; wrong schedule for hardness | Residual hydrogen; delayed brittle fracture |
| Grinding burn | Excessive infeed or insufficient coolant | Micro-cracking, heat-affected zone, adhesion loss |
| Over-grinding | Removed too much chrome | Undersize; requires strip and re-plate |
| Chrome flaking during grind | Poor adhesion from inadequate reverse etch | Strip, re-etch, re-plate |
| Failed inspection | Multiple root causes | Rework or scrap per spec disposition |

Cards: fill `#1E2435`, alternating `#252B3D`. Failure: `#E05C5C`. Cause: `#F0EDE8`. Consequence: `#E8A020`.

**Right -- Safety (X: 15.5", W: 8.0"):**

Rounded rect, fill `#E05C5C` at 15%, border 2 pt `#E05C5C`, radius 8.
Title: `SAFETY` Barlow Condensed ExtraBold 18 pt `#E05C5C`
Body (Inter Regular 12 pt `#F0EDE8`, line height 150%):

> - HE bake ovens: burn hazard (375--430 F). Heat-resistant gloves required.
> - Grinding chrome: fine chrome dust is a Cr(VI) concern if not properly managed.
> - Wet grinding with flood coolant captures dust -- dry grinding of chrome is NEVER permitted.
> - Chrome grinding swarf/coolant: treat as hazardous waste (Cr content).
> - Coolant mist: local exhaust ventilation over grinders.
> - Inspect PPE: safety glasses, face shield, hearing protection (grinding noise).

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Hard Chrome`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Hard chrome post-treatment involves high-temperature baking and grinding of chromium deposits. HE bake schedules must comply with ASTM B850 and applicable aerospace specifications. Grinding chrome generates hazardous dust -- use wet grinding only. Consult your process supplier and regulatory authority.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #87).
**Export:** Six files -- `Post Treatment Hard Chrome -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the final poster in the EP-08 Hard Chrome cluster, and it carries the weight of closure. The HE bake timeline (Block B) is the emotional and technical centerpiece -- that "critical transfer window" callout in coral must hit like a warning siren. Every hard chrome plater has a story about the time parts sat too long. The ASTM B850 bake schedule table (Block C) gives the specific numbers that operators need on the wall, right next to the oven.

The grinding section (Block D) respects a reality that many poster series would skip: hard chrome is almost never the finished surface. It must be ground or honed to dimension. Diamond/CBN wheels, light passes, flood coolant -- this is precision work on a brutally hard substrate. The surface finish target table (Block D2) connects the grinding to real applications.

Watson's brief: "HE baking: 375 F minimum, 8--24 hours depending on hardness. Must commence within 1--4 hours of plating." "Hard chrome deposits are ground or honed to final dimension. Chrome is too hard (HV 800--1000) for conventional machining."

-> Watson: Confirm ASTM B850 bake schedule breakpoints by HRC range. I have used standard industry values but Watson should verify against published ASTM tables.

-> Tyler: Note -- Tyler is not needed for this poster (no wet chemistry), but if Drew wants lab-side verification of HE bake documentation procedures, Tyler can review.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #94 -- Construction Workup v1.0*
*2026-04-26*
