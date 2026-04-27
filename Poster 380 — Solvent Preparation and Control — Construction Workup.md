---
Project: Plating Posters Inc
Poster Number: 380
Title: "Solvent Preparation & Control -- Cold Immersion and Vapor Degreasing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-6)"
Technical Source: Industry-standard solvent cleaning bath preparation, vapor degreaser setup, solvent purity monitoring, stabilizer testing, and bath life indicators. Per ASM Handbook Vol. 5, Metal Finishing Guidebook, and solvent manufacturer guidelines.
Process Scope: Solvent bath preparation and control -- cold immersion setup, vapor degreaser commissioning, purity monitoring, stabilizer management, bath life
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - SolventCleaning
  - BathPreparation
  - VaporDegreasing
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT06
---

# Poster #380 -- Construction Workup
## Solvent Preparation & Control -- Cold Immersion and Vapor Degreasing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the "recipe and equipment" poster for the solvent cleaning cluster. Unlike alkaline cleaners with their multi-component formulations, solvents are used as-received -- the challenge is maintaining purity, monitoring stabilizer levels, and knowing when to dump. Vapor degreaser setup is the most equipment-intensive topic here: freeboard ratio, condensing coil positioning, and boiling sump management. The operator who needs to commission or maintain a vapor degreaser starts with this poster.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Cold immersion vs. vapor degreaser comparison (Block B -- HERO):** Two tall callout panels side by side -- left for cold immersion setup, right for vapor degreaser parameters.

2. **Solvent property reference table (Block D):** Key properties for 6 common solvents (boiling point, flash point, Kb value, regulatory status).

3. **Control and monitoring callout (Block E):** Four monitoring methods -- specific gravity, boiling point range, acid acceptance, visual clarity.

4. **Bath life indicators strip (Block F):** When to dump / when to distill.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- COLD IMMERSION vs. VAPOR DEGREASER (2.9"--15.5" / ~12.6" tall)
  Block B: Left -- Cold Immersion Setup
  Block C: Right -- Vapor Degreaser Parameters

ZONE 3 -- SOLVENT PROPERTY REFERENCE (15.5"--22.0" / ~6.5" tall)
  Block D: 6-solvent property table

ZONE 4 -- CONTROL AND MONITORING (22.0"--28.5" / ~6.5" tall)
  Block E: Four monitoring methods

ZONE 5 -- BATH LIFE INDICATORS (28.5"--32.5" / ~4.0" tall)
  Block F: When to dump / distill strip

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SOLVENT PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Cold Immersion Setup and Vapor Degreaser Commissioning` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Solvents are used as-received -- the art is in maintaining purity, monitoring stabilizer health, and knowing when the bath has reached end of life.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cold Immersion vs. Vapor Degreaser (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> TWO METHODS -- TWO EQUIPMENT SETUPS

---

**BLOCK B -- Cold Immersion Setup (Left Panel)**

Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 11.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#2EC4B6`.
Title: `COLD IMMERSION` -- Barlow SemiBold, 22 pt, `#2EC4B6`.

Content rows:

*Setup:*
- Barlow SemiBold 15 pt `#F0EDE8`: `Equipment`
- Inter Regular 13 pt `#F0EDE8`: `Stainless steel or polypropylene tank with lid. Size per part volume. No heating element required.`

*Solvent Fill:*
- JetBrains Mono 13 pt `#F0EDE8`:
```
Solvent: as-received, no dilution
Fill: to cover parts with 2-3 in. margin
Cover when not in use (vapor loss + contamination)
```

*Agitation:*
- Inter Regular 13 pt `#F0EDE8`: `Manual part movement or gentle air agitation. No ultrasonic at this stage (see Cluster 7). Avoid vigorous agitation that increases vapor generation.`

*Temperature:*
- JetBrains Mono 13 pt `#F0EDE8`: `Ambient (room temperature)`
- Inter Regular 13 pt `#F0EDE8`: `Heating cold immersion is NOT standard practice -- if you need heat, you need a vapor degreaser.`

*Maintenance:*
- Inter Medium 13 pt `#27AE60`: `Monitor visual clarity. Replace when solvent is opaque or heavily discolored. Recycle spent solvent via distillation (on-site or off-site service).`

---

**BLOCK C -- Vapor Degreaser Parameters (Right Panel)**

Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 11.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E8A020`.
Title: `VAPOR DEGREASER` -- Barlow SemiBold, 22 pt, `#E8A020`.

Content rows:

*Equipment:*
- Inter Regular 13 pt `#F0EDE8`: `Enclosed or open-top vapor degreasing unit with heating sump, primary and secondary condensing coils, freeboard zone, and water separator.`

*Key Parameters:*
- JetBrains Mono 13 pt `#F0EDE8`:
```
Freeboard ratio: min 1.0 (height:width)
  Preferred: 1.5 for emission control
Boiling point (TCE): 189 deg F (87 C)
Boiling point (PERC): 250 deg F (121 C)
Vapor zone: at solvent boiling point
Condensing coils: maintain vapor line
  below tank lip
```

*Sump Management:*
- Inter Regular 13 pt `#F0EDE8`: `Boiling sump accumulates dissolved soil over time. Some units have a secondary "clean" sump -- parts pass through clean sump last for a purer final rinse. Soil settles or is skimmed periodically.`

*Stabilizer:*
- Inter Medium 13 pt `#E8A020`: `Chlorinated solvents require acid inhibitors / stabilizers to prevent decomposition. Test per manufacturer procedure. Stabilizer depletion -> acid formation -> equipment corrosion + toxic byproducts.`

*Water Separator:*
- Inter Medium 13 pt `#E05C5C`: `Water contamination in chlorinated solvents causes acid formation. Water separator is critical. Check daily. Drain water layer.`

---

### ZONE 3 -- Solvent Property Reference

**Section label:** Centered. Y: 15.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> SOLVENT PROPERTIES AT A GLANCE

---

**BLOCK D -- 6-Solvent Property Table**

Y: 16.3" to 21.8". Column widths (23.0" total):
- Solvent (4.5") | Category (3.0") | Boiling Pt (3.0") | Flash Pt (3.0") | Solvency (3.0") | Regulatory Status (6.5")

Header row: fill `#3A4055`, H: 0.5".

| Solvent | Category | Boiling Pt | Flash Pt | Solvency | Regulatory Status |
|---|---|---|---|---|---|
| TCE (Trichloroethylene) | Halogenated | 189 F (87 C) | None | Excellent | IARC Group 1 carcinogen; NESHAP Subpart T; F001 waste |
| PERC (Perchloroethylene) | Halogenated | 250 F (121 C) | None | Excellent | Probable carcinogen; NESHAP Subpart T; F001 waste |
| trans-DCE | Halogenated | 118 F (48 C) | None | Good | Lower toxicity; newer alternative; still NESHAP regulated |
| Mineral Spirits | Non-Halogenated | 300-400 F (149-204 C) | 105-145 F | Good | VOC; NFPA 30; F003 waste |
| Acetone | Non-Halogenated | 133 F (56 C) | 0 F (-18 C) | Good (polar) | Extremely flammable; exempt from some VOC rules |
| nPB (1-Bromopropane) | Halogenated | 160 F (71 C) | None | Good | Neurotoxic; ACGIH TLV 0.1 ppm; under regulatory review |

Data: Inter Regular 12 pt. Solvent names: Barlow SemiBold 13 pt. Category: `Halogenated` in `#E05C5C`, `Non-Halogenated` in `#E8A020`.

---

### ZONE 4 -- Control and Monitoring

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> MONITORING SOLVENT HEALTH -- FOUR KEY TESTS

---

**BLOCK E -- Four Monitoring Cards**

Y: 22.9" to 28.3". Four cards in a 2x2 grid. Gap: 0.33".

Each card: Rounded rect, W: 11.17", H: 2.5", fill `#1E2435`, radius 6, left accent 0.06".

| Position | Test | What It Measures | Accent |
|---|---|---|---|
| R1C1 | Specific Gravity | Soil loading -- SG rises as dissolved contaminants accumulate | `#2EC4B6` |
| R1C2 | Boiling Point Range | Contamination or stabilizer depletion -- shifts from nominal indicate problems | `#E8A020` |
| R2C1 | Acid Acceptance Test | Stabilizer health in chlorinated solvents -- low AA = decomposition imminent | `#E05C5C` |
| R2C2 | Visual Clarity | Quick field check -- dark discoloration = high soil loading; haze = moisture | `#27AE60` |

Per card:
- Test name: Barlow SemiBold, 16 pt, accent color
- Description: Inter Regular, 13 pt, `#F0EDE8`
- Icon placeholder: 0.4" x 0.4" circle, fill `#3A4055`

---

### ZONE 5 -- Bath Life Indicators

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

> WHEN TO DUMP -- WHEN TO DISTILL

---

**BLOCK F -- Bath Life Strip**

Y: 29.3" to 32.3". Four indicator cards in a row.

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Indicator | Action |
|---|---|---|---|
| 1 | 0.5" | Solvent dark / opaque | Soil saturated -- distill or replace |
| 2 | 6.33" | Boiling point shifted | Contamination or stabilizer failure -- test AA; may need full replacement |
| 3 | 12.16" | Acid acceptance test failure | Stabilizer depleted in chlorinated solvent -- DO NOT continue use; replace immediately |
| 4 | 18.0" | Odor change (sharp / acidic) | Decomposition products forming -- ventilate area; stop use; test and replace |

Per card:
- Indicator: Barlow SemiBold, 15 pt, `#E05C5C`
- Action: Inter Regular, 13 pt, `#F0EDE8`
- Positive action: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 6 -- Footer

Standard. Title: `Solvent Preparation & Control -- Cold Immersion and Vapor Degreasing`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Solvent properties and equipment parameters shown are typical values. Specific solvents, equipment configurations, and stabilizer testing procedures vary by manufacturer. Always follow your solvent supplier's technical data sheet and applicable regulations.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Solvent Preparation Control -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is more equipment-focused than the typical bath preparation poster because solvent cleaning does not involve multi-component formulation. The vapor degreaser panel carries the most technical weight -- freeboard ratio, condensing coils, sump management, and stabilizer testing are concepts most operators have never been formally taught. The acid acceptance test deserves special visual emphasis because stabilizer failure in chlorinated solvents leads to phosgene and HCl generation -- this is not just a quality issue, it is a safety issue.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #380 -- Construction Workup v1.0*
*2026-04-26*
