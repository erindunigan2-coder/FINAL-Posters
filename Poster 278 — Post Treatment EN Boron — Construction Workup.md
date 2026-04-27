---
Project: Plating Posters Inc
Poster Number: 278
Title: "Post Treatment -- EN Boron"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief v1.1 (Process 8: EN-B, Poster 8)"
Technical Source: EN-B heat treatment for maximum hardness (Ni3B precipitation hardening). HE relief per ASTM B849/B850. Passivation options. EN-B + PTFE/MoS2 composite coatings. Watson domain expertise.
Process Scope: Post treatment (Stage 7 of 8) for electroless nickel-boron plating
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ElectrolessNickelBoron
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ClusterEL08
---

# Poster #278 -- Construction Workup
## Post Treatment -- EN Boron

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7 of 8. Post treatment for EN-B is where the deposit reaches its full potential. As-plated EN-B is already the hardest electroless nickel (700-850 HV), but heat treatment precipitates Ni3B intermetallic phase, pushing hardness to 1000-1300 HV -- exceeding hard chrome. This poster covers three heat treatment tiers (HE relief, intermediate hardening, maximum hardness), the Ni3B precipitation hardening mechanism, passivation options for improved corrosion resistance, and the advanced topic of EN-B composite coatings with PTFE or MoS2 for ultra-low friction.

Hero visual: heat treatment temperature-hardness curve showing the three tiers as distinct zones on the curve.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temperature-hardness curve hero (Block B):** Three-tier HT zones plotted on a hardness curve.
2. **Heat treatment parameters table (Block D):** HE relief, intermediate, and maximum hardness specs.
3. **Ni3B hardening mechanism callout (Block E):** Why heat treatment works -- the metallurgical explanation.
4. **Passivation + composites strip (Block F):** Corrosion improvement and ultra-low friction options.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- TEMPERATURE-HARDNESS CURVE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- HEAT TREATMENT PARAMETERS (14.5"--20.5" / ~6.0")
ZONE 5 -- Ni3B HARDENING MECHANISM (20.5"--26.5" / ~6.0")
ZONE 6 -- PASSIVATION + COMPOSITES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `EN Boron -- Stage 7 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Heat treatment transforms EN-B from excellent to extraordinary. 1000-1300 HV. Harder than hard chrome. The Ni3B phase does the work.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Rinsed, dried EN-B deposit  -->  After: Heat-treated, passivated surface ready for service`

---

### ZONE 3 -- Temperature-Hardness Curve Hero

**Section label:** `HEAT TREATMENT -- THREE TIERS` -- Y: 4.4".

**BLOCK B -- Temperature-Hardness Curve (Y: 5.0" to 14.0")**

**Conceptual chart area (X: 0.5", Y: 5.0", W: 23.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`
- X-axis: `TEMPERATURE (C)` -- 0 to 500 C, labeled at 100, 200, 300, 400, 500
- Y-axis: `HARDNESS (HV)` -- 400 to 1400 HV, labeled at 400, 600, 800, 1000, 1200, 1400
- Axis lines: 2 pt `#3A4055`
- Axis labels: JetBrains Mono 12 pt `#F0EDE8` at 60%

**Curve:** Simplified stepped/rising curve showing hardness increase with temperature.

**Three shaded zones on the curve:**

**Zone A -- HE Relief (190-210 C):**
- Shaded vertical band, fill `#2EC4B6` at 15%, border dashed 1 pt `#2EC4B6`
- Label: `HE RELIEF` Barlow Condensed ExtraBold 16 pt `#2EC4B6`
- Hardness annotation: `~700-800 HV (unchanged)` JetBrains Mono 12 pt `#2EC4B6`
- Note below zone: `Drives out absorbed hydrogen` Inter Regular 12 pt `#F0EDE8` at 70%
- Note: `MANDATORY for high-strength steel` Inter Medium 12 pt `#E05C5C`

**Zone B -- Intermediate Hardening (280-320 C):**
- Shaded vertical band, fill `#E8A020` at 15%, border dashed 1 pt `#E8A020`
- Label: `INTERMEDIATE` Barlow Condensed ExtraBold 16 pt `#E8A020`
- Hardness annotation: `900-1000 HV` JetBrains Mono 12 pt `#E8A020`
- Note: `Retains some ductility` Inter Regular 12 pt `#F0EDE8` at 70%

**Zone C -- Maximum Hardness (350-400 C):**
- Shaded vertical band, fill `#27AE60` at 15%, border dashed 1 pt `#27AE60`
- Label: `MAXIMUM` Barlow Condensed ExtraBold 16 pt `#27AE60`
- Hardness annotation: `1000-1300 HV` JetBrains Mono 14 pt `#27AE60`
- Note: `Ni3B precipitation hardening` Inter Regular 12 pt `#F0EDE8` at 70%
- Note: `Exceeds hard chrome (900-1100 HV)` Inter Medium 12 pt `#27AE60`

**Reference line:** Horizontal dashed line at ~1000 HV, label: `Hard Chrome Reference: 900-1100 HV` JetBrains Mono 11 pt `#E05C5C` at 60%

**Legend (bottom of chart):**
- Three swatches: Teal = HE Relief, Amber = Intermediate, Emerald = Maximum

---

### ZONE 4 -- Heat Treatment Parameters

**Section label:** `HEAT TREATMENT SPECIFICATIONS` -- Y: 14.7".

**BLOCK D -- Parameters Table (Y: 15.3" to 20.3")**

Full-width table. Column widths (23.0" total):
- Treatment (4.0") | Temperature (4.0") | Time (3.0") | Atmosphere (3.0") | Result (5.0") | Notes (4.0")

Header row: Rectangle fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".

| Treatment | Temperature | Time | Atmosphere | Result | Notes |
|---|---|---|---|---|---|
| HE Relief | 190-210 C (375-410 F) | 2-23 hours | Air acceptable | ~700-800 HV (unchanged) | MANDATORY within 4 hrs of plating for steel >1000 MPa UTS. Per ASTM B849/B850 |
| Intermediate | 280-320 C (535-610 F) | 1-2 hours | Air or N2 | 900-1000 HV | Retains ductility; good for applications requiring some flexibility |
| Maximum Hardness | 350-400 C (660-750 F) | 1 hour | N2 or vacuum preferred | 1000-1200 HV (DMAB) / 1100-1300 HV (NaBH4) | Ni3B precipitation hardening. Maximum wear resistance |

Data: JetBrains Mono 12 pt `#F0EDE8`. Treatment names: Inter Medium 13 pt `#F0EDE8`.

**Bottom callout -- HE Relief Rule:**
- Full width, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- `HIGH-STRENGTH STEEL (>1000 MPa UTS or >40 HRC): HE bake at 190-210 C for minimum 4 hours, within 4 hours of plating. Failure to bake = risk of catastrophic delayed brittle fracture. ASTM B849 / ASTM B850 / AMS 2759/9.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- Ni3B Hardening Mechanism

**Section label:** `WHY HEAT TREATMENT WORKS -- THE Ni3B MECHANISM` -- Y: 20.7".

**BLOCK E -- Mechanism Panel (Y: 21.3" to 26.3")**

**Full-width callout (X: 0.5", W: 23.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"

**Left half (X: 0.8", W: 10.5"):**
- Title: `AS-PLATED: AMORPHOUS Ni-B` Barlow SemiBold 18 pt `#F0EDE8`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `EN-B deposit is amorphous (metallic glass) at >3% B`
  - `Boron atoms are randomly distributed in nickel matrix`
  - `No crystalline grain structure`
  - `Hardness: 700-850 HV (already excellent)`
  - `This is analogous to EN-P (amorphous Ni-P at >10% P)`

**Visual: simplified arrow diagram (center):**
- Left box: `Amorphous Ni-B` with random dot pattern
- Arrow: `Heat at 350-400 C` with flame icon (stylized)
- Right box: `Nanocrystalline Ni + Ni3B precipitates` with organized dot pattern

**Right half (X: 12.0", W: 11.0"):**
- Title: `HEAT-TREATED: NANOCRYSTALLINE Ni + Ni3B` Barlow SemiBold 18 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `Heat treatment crystallizes the amorphous matrix`
  - `Boron segregates and forms Ni3B intermetallic precipitates`
  - `Ni3B particles PIN dislocations -- dramatically increasing hardness`
  - `Result: nanocrystalline nickel matrix reinforced by Ni3B`
  - `Hardness: 1000-1300 HV`
  - `This is the SAME mechanism as EN-P (Ni3P precipitation)` Inter Medium 13 pt `#E8A020`

**Bottom highlight:**
- Rounded rect, W: 22.0", H: 0.6", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `Ni3B is to EN-B what Ni3P is to EN-P. The mechanism is the same -- only the intermetallic phase changes. And Ni3B is harder.` Inter Medium 14 pt `#27AE60`

---

### ZONE 6 -- Passivation + Composites

**Section label:** `BEYOND HEAT TREATMENT -- PASSIVATION AND COMPOSITES` -- Y: 26.7".

**Two callout boxes (Y: 27.3" to 32.3"):**

**Left -- Passivation (X: 0.5", W: 11.0", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `PASSIVATION -- IMPROVING CORROSION RESISTANCE` Barlow SemiBold 16 pt `#E8A020`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `EN-B corrosion resistance: 200-600 hrs NSS at 25 um`
  - `Lower than EN High-P (1,000+ hrs) -- this is EN-B's weakness`
  - `Trivalent chromate conversion coating improves corrosion:`
  - `Adds 100-300 hrs additional NSS protection` JetBrains Mono 13 pt `#27AE60`
  - `No hexavalent chromium -- RoHS compliant`
  - `Apply after heat treatment, not before`
  - `Alternative: organic sealers (proprietary topcoats)`
- Bottom note: `If corrosion resistance is the primary requirement, EN High-P is the better choice. EN-B is for WEAR.` Inter Medium 12 pt `#E8A020`

**Right -- Composite Coatings (X: 12.0", W: 11.5", H: 4.8"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `EN-B COMPOSITES -- ULTRA-LOW FRICTION` Barlow SemiBold 16 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`, line height 155%):
  - `EN-B with co-deposited particles for extreme performance:`

| Composite | CoF (dry) | Application |
|---|---|---|
| EN-B + PTFE | 0.02-0.05 | Mold release, anti-galling, food processing |
| EN-B + MoS2 | 0.03-0.06 | Aerospace, vacuum environments |
| EN-B (no composite) | 0.05-0.12 | Reference baseline |

  - `PTFE particles (0.1-1 um) or MoS2 particles co-deposit during EN-B plating`
  - `Combined hardness of EN-B + lubricity of solid lubricant`
  - `Specialist process -- not all EN-B suppliers offer composites` Inter Medium 12 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- EN Boron`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Process parameters shown are typical industry values for EN-B post-treatment. Specific heat treatment temperatures, times, and atmospheres vary by application specification and EN-B bath chemistry. Consult your process supplier and applicable ASTM/AMS standards. Source: General industry knowledge; ASTM B841; ASTM B849/B850.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment EN Boron -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster closes the EN-B cluster with the payoff: heat treatment transforms an already excellent deposit into something extraordinary. The temperature-hardness curve hero in Zone 3 is the visual anchor -- it shows the three treatment tiers as distinct zones, with the hard chrome reference line providing the benchmark that EN-B exceeds. The Ni3B mechanism in Zone 5 is the educational core -- it explains WHY heat treatment works and explicitly connects it to the analogous Ni3P mechanism in EN-P, which most operators already understand. The composite coatings callout in Zone 6 opens the door to advanced applications (EN-B + PTFE at 0.02-0.05 CoF is genuinely remarkable). The HE relief callout is flagged in Coral because it is a safety-critical requirement -- failure to bake high-strength steel causes delayed brittle fracture, which is catastrophic.

---

*Alaina -- Poster #278 -- Construction Workup v1.0 -- 2026-04-26*
