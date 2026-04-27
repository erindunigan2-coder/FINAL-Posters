---
Project: Plating Posters Inc
Poster Number: 537
Title: "Post-Treatment -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 6: Detonation Gun)"
Process Scope: Post-treatment for D-Gun coatings -- grinding, finishing, sealing (rare), and final surface quality
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - DGun
  - DetonationGun
  - PostTreatment
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #537 -- Construction Workup
## Post-Treatment -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

D-Gun post-treatment is dominated by one operation: precision grinding. Unlike arc spray or flame spray where sealing is the critical post-treatment step, D-Gun coatings are so dense (porosity < 0.5%) that sealing is almost never required. The coating comes off the gun ready to perform -- it just needs to be ground to final dimension and surface finish. The hero content is the grinding parameter table and the achievable surface finish spectrum from as-sprayed (Ra 2--5 um) through diamond grinding (Ra 0.1--0.4 um) to superfinishing (Ra < 0.1 um). No heat treatment is required. This is a short, focused poster: grind it, measure it, ship it.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Grinding parameter table (Block B -- HERO):** Diamond and CBN grinding specifications for D-Gun WC-Co coatings.
2. **Surface finish spectrum (Block C):** As-sprayed to superfinished -- what each level looks like and where it is used.
3. **Sealing guidance (Block D):** When sealing IS and IS NOT required (rare cases).
4. **D-Gun vs. HVOF post-treatment comparison (Block E):** Side-by-side showing identical post-treatment workflows.
5. **Time-critical warnings (Block F):** 4 warning cards for grinding.

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
ZONE 3 -- GRINDING PARAMETERS / HERO (4.2"--15.5" / ~11.3")
  Block B: Grinding parameter table
  Block C: Surface finish spectrum
ZONE 4 -- SEALING GUIDANCE (15.5"--22.0" / ~6.5")
  Block D: When to seal / when not to seal
  Block E: D-Gun vs. HVOF post-treatment comparison
ZONE 5 -- GRINDING WARNINGS (22.0"--28.5" / ~6.5")
  Block F: 4 warning cards
ZONE 6 -- POST-TREATMENT PROCEDURE STEPS (28.5"--32.5" / ~4.0")
  Block G: 4 sequential step cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST-TREATMENT` -- 88 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Precision Grinding to Final Dimension` -- 36 pt `#E8A020` (Amber).
**Tagline:** `D-Gun coatings are so dense they rarely need sealing. The post-treatment story is grinding -- taking the densest coating in thermal spray from as-sprayed roughness to mirror-finish precision. Diamond wheels. Light passes. No shortcuts.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Coating sprayed to target thickness --> After: Ground to final dimension and surface finish, ready for inspection`

---

### ZONE 3 -- Grinding Parameters (HERO)

**Section label:** `PRECISION GRINDING -- D-GUN WC-Co COATINGS` -- Y: 4.4".

**BLOCK B -- Grinding Parameter Table**

Y: 5.0" to 10.5". Full width within margins (23.0").

Column widths: Parameter (5.0") | Diamond Wheel (6.0") | CBN Wheel (6.0") | Notes (6.0")

| Parameter | Diamond Wheel | CBN Wheel | Notes |
|---|---|---|---|
| Wheel type | Resin-bonded diamond | Vitrified or resin-bonded CBN | Diamond preferred for WC-Co; CBN for metallic coatings |
| Grit size | 100--180 mesh | 100--180 mesh | Finer grit = better finish; coarser = faster stock removal |
| Wheel speed | 20--30 m/s | 20--30 m/s | Standard surface grinding speeds |
| Infeed per pass | 5--15 um (0.0002--0.0006") | 5--15 um | Light cuts prevent coating pullout and thermal damage |
| Coolant | Soluble oil; flood application | Soluble oil; flood application | MANDATORY -- dry grinding causes thermal cracking and delamination |
| Table speed | 10--20 m/min | 10--20 m/min | Consistent traverse for uniform finish |
| Achievable Ra | 0.1--0.4 um | 0.2--0.6 um | Diamond achieves finer finish on WC-Co |
| Stock removal typical | 50--200 um from as-sprayed | 50--200 um | Leave adequate grinding allowance when specifying spray thickness |

Table header: fill `#3A4055`, H: 0.6". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.8".
Parameter: Inter Medium 13 pt. Values: JetBrains Mono 12 pt `#F0EDE8`. Notes: Inter Regular 12 pt `#F0EDE8` at 70%.

**BLOCK C -- Surface Finish Spectrum**

Y: 11.0" to 15.3". Full width.

Section sublabel: `SURFACE FINISH LEVELS -- FROM AS-SPRAYED TO SUPERFINISHED` Barlow SemiBold 18 pt `#2EC4B6`. Y: 11.0".

Four horizontal bands representing finish levels, stacked vertically. Each band: W: 23.0", H: 0.9", radius 4.

| Level | Ra Range | Application | Left Accent | Fill |
|---|---|---|---|---|
| AS-SPRAYED | Ra 2--5 um | Non-critical wear surfaces; will be ground | `#C8D0D8` | `#1E2435` |
| STANDARD GROUND | Ra 0.2--0.4 um | Most aerospace and industrial wear applications; chrome replacement | `#27AE60` | `#1E2435` |
| FINE GROUND | Ra 0.1--0.2 um | Precision bearing surfaces; hydraulic cylinder rods; seal faces | `#E8A020` | `#1E2435` |
| SUPERFINISHED | Ra < 0.1 um | Ultra-precision applications; lapping or honing after grinding | `#2EC4B6` | `#1E2435` |

Level: Barlow SemiBold 14 pt accent color. Ra: JetBrains Mono 14 pt `#F0EDE8`. Application: Inter Regular 13 pt `#F0EDE8` at 80%.

Below spectrum:
- Callout, fill `#E8A020` at 10%, border 1 pt `#E8A020`:
- `D-Gun WC-Co can be ground and finished to the same surface quality as hard chrome plating. For chrome replacement applications, the ground D-Gun coating is dimensionally and functionally interchangeable.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- Sealing Guidance

**Section label:** `SEALING -- WHEN YOU DO AND DON'T NEED IT` -- Y: 15.7".

**Left -- BLOCK D: Sealing Decision Guide (X: 0.5", W: 11.0")**

Two stacked panels:

*Top -- "SEALING NOT REQUIRED" (H: 2.5"):*
Rounded rect fill `#1E2435`, left accent `#27AE60` 0.06".
Title: `SEALING NOT REQUIRED (STANDARD)` Barlow SemiBold 16 pt `#27AE60`.
- `D-Gun porosity is < 0.5% (often < 0.2%)`
- `Interconnected porosity is virtually absent`
- `Coating is a continuous barrier as-sprayed`
- `No heat treatment required -- coating is fully functional`
- `This is the standard condition for D-Gun WC-Co`

*Bottom -- "SEALING MAY BE SPECIFIED" (H: 2.5"):*
Rounded rect fill `#1E2435`, left accent `#E8A020` 0.06".
Title: `SEALING MAY BE SPECIFIED (RARE)` Barlow SemiBold 16 pt `#E8A020`.
- `Salt spray (ASTM B117) requirements exceeding 500 hours`
- `Immersion service in corrosive fluids`
- `Customer specification mandates sealing regardless of porosity`
- `Sealer type: epoxy or phenolic impregnation`
- `Apply AFTER grinding, BEFORE final inspection`

**Right -- BLOCK E: D-Gun vs. HVOF Post-Treatment (X: 12.0", W: 11.5")**

Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#2EC4B6`.

Title: `D-GUN vs. HVOF -- POST-TREATMENT COMPARISON` Barlow SemiBold 18 pt `#2EC4B6`.

| Step | D-Gun | HVOF |
|---|---|---|
| Grinding | Diamond or CBN | Diamond or CBN |
| Achievable Ra | 0.05--0.4 um | 0.1--0.4 um |
| Sealing required? | Rarely | Rarely |
| Heat treatment? | No | No |
| Stock removal | 50--200 um | 50--200 um |
| Superfinishing? | Yes (lapping) | Yes (lapping) |

Data: JetBrains Mono 12 pt. D-Gun values in `#E8A020`. HVOF values in `#2EC4B6`.

Below table:
`Post-treatment workflows are virtually identical for D-Gun and HVOF WC-Co coatings. The difference is in the as-sprayed coating quality -- D-Gun starts denser, harder, and smoother.` Inter Medium 13 pt `#C8D0D8`.

---

### ZONE 5 -- Grinding Warnings

**Section label:** `GRINDING WARNINGS -- PROTECT THE COATING` -- Y: 22.2".

**BLOCK F -- Four Warning Cards**

Y: 22.8" to 28.0". Four cards in a 2x2 grid.

Each card: W: 11.0", H: 2.3", fill `#1E2435`, radius 6, left accent 4 pt `#E05C5C`.

| Card | Position | Warning | Detail |
|---|---|---|---|
| 1 | R1C1 (X: 0.5", Y: 22.8") | NEVER DRY GRIND | Dry grinding generates extreme localized heat. Thermal shock causes micro-cracking, coating delamination, and carbide decomposition. Always flood with coolant. |
| 2 | R1C2 (X: 12.0", Y: 22.8") | LIGHT PASSES ONLY | Aggressive infeed (> 25 um/pass) pulls WC grains from the binder matrix, creating surface pitting and sub-surface damage. Stay at 5--15 um/pass. |
| 3 | R2C1 (X: 0.5", Y: 25.4") | CHECK WHEEL CONDITION | Glazed or loaded diamond wheels generate excess heat and produce poor surface finish. Dress wheels regularly. Monitor for vibration. |
| 4 | R2C2 (X: 12.0", Y: 25.4") | VERIFY GRINDING ALLOWANCE | Spray thickness must include grinding stock. If the as-sprayed coating is at minimum thickness, grinding to finish dimension will leave the coating below specification. Plan ahead. |

Warning: Barlow SemiBold, 16 pt, `#E05C5C`.
Detail: Inter Regular, 13 pt, `#F0EDE8`.

---

### ZONE 6 -- Post-Treatment Procedure Steps

**Section label:** `POST-TREATMENT SEQUENCE` -- Y: 28.7".

Four step cards in a single row, connected by arrows. Gap: 0.33".

Each card: W: 5.5", H: 2.7", fill `#1E2435`, radius 6, top accent 4 pt.

| Card | X | Accent | Step | Detail |
|---|---|---|---|---|
| 1 | 0.5" | `#E8A020` | VISUAL INSPECT AS-SPRAYED | Verify uniform coverage and thickness before committing to grinding. Flag any defects for re-spray. |
| 2 | 6.33" | `#27AE60` | DIAMOND GRIND TO DIMENSION | Flood coolant, 5--15 um infeed/pass, grind to drawing dimension and surface finish specification. |
| 3 | 12.16" | `#2EC4B6` | SEAL (IF SPECIFIED) | Epoxy or phenolic impregnation after grinding. Cure per manufacturer instructions before final inspection. |
| 4 | 18.0" | `#E8A020` | MEASURE AND DOCUMENT | Final thickness, surface roughness (Ra), and visual inspection. Record all results for QA package. |

Step title: Barlow SemiBold 16 pt accent color.
Detail: Inter Regular 13 pt `#F0EDE8`.

Arrows between cards: stroke 2 pt `#3A4055`, filled arrowhead right.

---

### ZONE 7 -- Footer

Standard footer. Title: `Post-Treatment -- D-Gun`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; general industry knowledge; Oerlikon Metco and Praxair Surface Technologies published data. Grinding parameters shown are typical for WC-Co coatings. Consult your grinding wheel manufacturer and coating specification for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

## Design Notes

D-Gun post-treatment is the least complex poster in the cluster because D-Gun coatings need so little done to them after spraying. The grinding parameter table is the hero because that IS the post-treatment for 95% of D-Gun jobs. The surface finish spectrum is the visual anchor -- operators and engineers will look at this to understand what finish level their application requires and whether they need standard grinding, fine grinding, or superfinishing. The sealing section is deliberately minimal -- the message is "you probably do not need to seal D-Gun coatings, and here is why." The grinding warnings in coral are critical because bad grinding technique can destroy a $500+ D-Gun coating in seconds. The comparison with HVOF post-treatment reinforces that these two processes are functionally siblings in the shop.

---

*Alaina -- Poster #537 -- Construction Workup v1.0 -- 2026-04-26*
