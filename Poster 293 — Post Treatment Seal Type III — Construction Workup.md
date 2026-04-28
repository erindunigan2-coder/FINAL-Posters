---
Project: Plating Posters Inc
Poster Number: 293
Title: "Post Treatment / Seal -- Hardcoat Anodizing (Type III)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 2, Section 2.6)"
Process Scope: Post-anodize rinse, sealing, and PTFE impregnation for hardcoat -- Stages 7--8 of 8 (combined)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeIII
  - Hardcoat
  - Seal
  - PostTreatment
  - PTFE
  - ConstructionWorkup
  - ClusterAnodize02
---

# Poster #293 -- Construction Workup
## Post Treatment / Seal -- Hardcoat Anodizing (Type III)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stages 7--8 of 8 (combined: post-anodize rinse + seal). Hardcoat sealing is different from Type II because the application drives the seal choice. Corrosion protection? Hot water or nickel acetate. Sliding surfaces? PTFE impregnation -- drops coefficient of friction from 0.4--0.6 to 0.08--0.15. Some wear applications benefit from NO seal at all -- open pores retain lubricant. The concept hook: "The seal you choose defines whether this is a corrosion barrier, a bearing surface, or a self-lubricating wear part."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Seal method comparison hero (Block B):** Four seal options side by side with properties and applications.
2. **PTFE impregnation detail panel (Block D):** The unique hardcoat seal that doesn't exist in Type II.
3. **Dyeing limitations callout (Block E):** Why hardcoat limits dye to dark colors only.
4. **Application decision tree (Block F):** Which seal for which application.
5. **Effect on properties table (Block G):** How each seal changes hardness, friction, corrosion resistance.

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
  Stages 7 and 8 highlighted
ZONE 3 -- SEAL METHOD COMPARISON HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- PTFE DETAIL + DYEING LIMITATIONS (15.5"--22.0" / ~6.5")
ZONE 5 -- APPLICATION DECISION TREE (22.0"--28.5" / ~6.5")
ZONE 6 -- EFFECT ON PROPERTIES TABLE (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT / SEAL` -- 72 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Hardcoat Anodizing (Type III) -- Stages 7--8 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The seal defines the application. Corrosion barrier? Bearing surface? Self-lubricating wear part? Choose your seal, choose your performance.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stages 7 and 8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: As-anodized hard oxide (open pores, 400--600+ HV)  -->  After: Sealed, application-ready surface`

---

### ZONE 3 -- Seal Method Comparison Hero

**Section label:** `FOUR SEAL OPTIONS -- CHOOSE BY APPLICATION` -- Y: 4.4".

**BLOCK B -- Four Seal Cards**

Y: 5.0" to 14.5". Four tall cards in a single row.

**Card 1 -- Hot DI Water (X: 0.5", W: 5.5", H: 9.0"):**
- Fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `HOT DI WATER` Barlow SemiBold 18 pt `#2EC4B6`
- Chemistry: `Deionized water, pH 5.5--6.5` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `200--212 F (93--100 C)` JetBrains Mono 13 pt `#E8A020`
- Time: `2--3 min/um thickness (min 30 min for thick coats)` JetBrains Mono 12 pt `#F0EDE8`
- Mechanism: `Pores hydrate to boehmite (AlOOH), swelling shut` Inter Regular 12 pt `#F0EDE8` at 70%
- Best for: `General corrosion protection` Inter Medium 13 pt `#2EC4B6`
- Salt spray: `336--750 hr (ASTM B117)` JetBrains Mono 12 pt `#F0EDE8`

**Card 2 -- Nickel Acetate (X: 6.33", W: 5.5", H: 9.0"):**
- Fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `NICKEL ACETATE` Barlow SemiBold 18 pt `#27AE60`
- Chemistry: `5--8 g/L Ni(CH3COO)2, pH 5.5--6.0` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `180--200 F (82--93 C)` JetBrains Mono 13 pt `#E8A020`
- Time: `15--30 min` JetBrains Mono 12 pt `#F0EDE8`
- Mechanism: `Nickel precipitates in pores + boehmite formation` Inter Regular 12 pt `#F0EDE8` at 70%
- Best for: `Aerospace; maximum corrosion resistance` Inter Medium 13 pt `#27AE60`
- Salt spray: `750--1500+ hr (ASTM B117)` JetBrains Mono 12 pt `#F0EDE8`

**Card 3 -- PTFE Impregnation (X: 12.16", W: 5.5", H: 9.0"):**
- Fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `PTFE IMPREGNATION` Barlow SemiBold 18 pt `#E8A020`
- Chemistry: `PTFE dispersion, vendor-specific` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `Per vendor TDS` JetBrains Mono 13 pt `#F0EDE8`
- Time: `Per vendor TDS` JetBrains Mono 12 pt `#F0EDE8`
- Mechanism: `PTFE particles fill pores; cured at elevated temperature` Inter Regular 12 pt `#F0EDE8` at 70%
- Best for: `Sliding surfaces; low friction; wear resistance` Inter Medium 13 pt `#E8A020`
- CoF: `0.08--0.15 (vs. 0.4--0.6 unsealed)` JetBrains Mono 13 pt `#E8A020`

**Card 4 -- No Seal (X: 18.0", W: 5.5", H: 9.0"):**
- Fill `#1E2435`, top accent 4 pt `#C8D0D8`
- Title: `NO SEAL` Barlow SemiBold 18 pt `#C8D0D8`
- Chemistry: `N/A -- as-anodized` JetBrains Mono 12 pt `#F0EDE8`
- Temperature: `N/A` JetBrains Mono 13 pt `#F0EDE8`
- Time: `N/A` JetBrains Mono 12 pt `#F0EDE8`
- Mechanism: `Open pores retained intentionally` Inter Regular 12 pt `#F0EDE8` at 70%
- Best for: `Wear applications where pores retain oil/lubricant` Inter Medium 13 pt `#C8D0D8`
- Note: `Poor corrosion resistance; acceptable only for lubricated assemblies` Inter Regular 12 pt `#E05C5C`

---

### ZONE 4 -- PTFE Detail + Dyeing Limitations

**Two-column layout (Y: 15.7" to 21.8"):**

**Left -- PTFE Impregnation Detail (X: 0.5", W: 13.0"):**

Section label: `PTFE IMPREGNATION -- THE HARDCOAT SPECIALTY SEAL` Barlow Condensed ExtraBold 22 pt `#E8A020`.

Callout box, fill `#1E2435`, left accent `#E8A020`:

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `PTFE (polytetrafluoroethylene) -- the industry-standard low-friction polymer.`
- `Applied as an aqueous dispersion that is drawn into the open pores of the hard coat by immersion or vacuum.`
- `After impregnation, parts are typically heat-cured at 400--500 F to fuse PTFE particles.`
- ``
- `RESULT:` Inter Medium 13 pt `#E8A020`
- `-- Coefficient of friction drops from 0.4--0.6 to 0.08--0.15`
- `-- Self-lubricating surface; no external lubricant needed`
- `-- Excellent for hydraulic cylinders, pistons, valve bodies, guide rails`
- `-- NOT a corrosion seal -- PTFE fills pores but does not hydrate them`
- ``
- `IMPORTANT: PTFE seal is NOT reversible. Once cured, it cannot be stripped without destroying the oxide.` Inter Medium 12 pt `#E05C5C`

**Right -- Dyeing Limitations (X: 14.0", W: 9.5"):**

Section label: `DYEING -- LIMITED FOR HARDCOAT` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#C8D0D8`:

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Type III hardcoat has a dense, tightly packed pore structure that severely limits dye absorption.`
- ``
- `ACHIEVABLE COLORS:` Inter Medium 13 pt `#F0EDE8`
- `-- Black` Inter Regular 13 pt `#F0EDE8`
- `-- Dark blue` Inter Regular 13 pt `#F0EDE8`
- `-- Dark green` Inter Regular 13 pt `#F0EDE8`
- ``
- `NOT ACHIEVABLE:` Inter Medium 13 pt `#E05C5C`
- `-- Light colors (red, yellow, pink, gold)` Inter Regular 13 pt `#E05C5C`
- `-- Bright or pastel shades` Inter Regular 13 pt `#E05C5C`
- ``
- `Natural hardcoat color: dark bronze to near-black (thicker = darker). Most hardcoat is left in its natural color.`

Below: `If the customer requires bright colors, they need Type II -- not Type III.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Application Decision Tree

**Section label:** `WHICH SEAL FOR WHICH APPLICATION?` Barlow Condensed ExtraBold 24 pt `#F0EDE8`. Y: 22.2".

**BLOCK F -- Decision Flow**

Y: 22.8" to 28.3".

Vertical decision tree using rounded rects and arrows:

Diamond 1: `Is the part a sliding/bearing surface?`
- YES --> `PTFE IMPREGNATION` (Amber card) --> `Hydraulic cylinders, pistons, valve bodies, guide rails`
- NO --> Diamond 2

Diamond 2: `Does the part need corrosion resistance?`
- YES --> Diamond 3
- NO --> `NO SEAL -- open pores retain lubricant` (Silver card) --> `Oil-lubricated assemblies only`

Diamond 3: `Aerospace or military spec?`
- YES --> `NICKEL ACETATE` (Emerald card) --> `AMS 2469; maximum salt spray hours`
- NO --> `HOT DI WATER` (Teal card) --> `Standard corrosion protection; lowest cost`

Diamonds: Rotated square, fill `#252B3D`, border 1 pt `#C8D0D8`, text Inter Medium 13 pt `#F0EDE8`.
Answer cards: Rounded rect, fill `#1E2435`, top accent in method color.

---

### ZONE 6 -- Effect on Properties Table

**Section label:** `HOW SEALING CHANGES COATING PROPERTIES` Barlow Condensed ExtraBold 22 pt `#F0EDE8`. Y: 28.7".

**BLOCK G -- Properties Table**

Y: 29.3" to 32.3".

| Property | Unsealed | Hot Water | Ni Acetate | PTFE |
|---|---|---|---|---|
| **Hardness** | Maximum (500--700 HV) | Slight reduction | Slight reduction | Slight reduction |
| **Friction (CoF)** | 0.4--0.6 | 0.4--0.6 | 0.4--0.6 | 0.08--0.15 |
| **Corrosion (B117)** | Poor (< 168 hr) | Good (336--750 hr) | Excellent (750--1500+ hr) | Poor (not a corrosion seal) |
| **Lubricant retention** | Excellent (open pores) | None (pores closed) | None (pores closed) | Self-lubricating |
| **Abrasion resistance** | Maximum | Good | Good | Good + low friction |

Header: Barlow SemiBold 11 pt `#F0EDE8` on `#3A4055`. Data: Inter Regular 11 pt, alternating rows.

Best-in-class values highlighted: Hardness unsealed = `#27AE60`. Friction PTFE = `#27AE60`. Corrosion Ni Acetate = `#27AE60`. Lubricant retention unsealed = `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment / Seal -- Hardcoat Anodizing (Type III)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Seal selection depends on application requirements and customer specification. PTFE vendor products vary -- consult vendor TDS for specific procedures. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Seal Type III -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is unique in the series because the seal choice IS the engineering decision. Type II sealing is mostly "hot water or nickel acetate" with an occasional dichromate. Type III adds PTFE impregnation and the "no seal" option, both of which are valid engineering choices. The decision tree is the hero element -- an engineer or shop manager can trace from application to seal method in 15 seconds. The CoF numbers for PTFE (0.08--0.15) are the most dramatic performance improvement on the poster and should be visually prominent. The dyeing limitations callout prevents customer expectations from getting ahead of physics.

---

*Alaina -- Plating Posters Inc*
*Poster #293 -- Construction Workup v1.0*
*2026-04-26*
