---
Project: Plating Posters Inc
Poster Number: 636
Title: "Salt Bath Temperature Control -- Austempering"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Diffusion Heat Treatment Clusters -- Watson Research Brief (Process 9: Austempering, Section 9.6)"
Process Scope: Salt bath temperature selection and its direct effect on bainite morphology, hardness, and mechanical properties
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - HeatTreatment
  - Austempering
  - TemperatureControl
  - SaltBath
  - ConstructionWorkup
  - ClusterHT09
---

# Poster #636 -- Construction Workup
## Salt Bath Temperature Control -- Austempering

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

In austempering, the salt bath temperature IS the recipe. It determines whether you get lower bainite (hard, strong, low ductility) or upper bainite (softer, tougher, higher elongation). There is no atmosphere to control, no carbon potential to manage -- just temperature, time, and transformation. This poster is the temperature-to-properties lookup that every austempering operator needs on the wall.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temperature-to-properties hero table (Block B):** The central reference -- salt bath temp mapped to bainite type, hardness, ductility, and applications.
2. **Lower vs. upper bainite comparison (Block C):** Visual side-by-side of the two microstructures and their properties.
3. **ADI grade mapping (Block D):** ASTM A897 grades mapped to salt bath temperatures.
4. **Temperature control best practices (Block E):** Practical guidance for maintaining +/-5 F uniformity.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Emerald)
ZONE 3 -- TEMPERATURE-TO-PROPERTIES HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- LOWER VS. UPPER BAINITE (14.5"--21.5" / ~7.0")
ZONE 5 -- ASTM A897 ADI GRADE MAPPING (21.5"--27.5" / ~6.0")
ZONE 6 -- TEMPERATURE CONTROL BEST PRACTICES (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `SALT BATH TEMPERATURE CONTROL` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Austempering -- Temperature Determines Everything` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `No atmosphere. No carbon potential. Just temperature and time. The salt bath temp picks your microstructure.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 of 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `This poster covers the core variable in austempering: salt bath temperature and its effect on final properties`

---

### ZONE 3 -- Temperature-to-Properties Hero

**Section label:** `SALT BATH TEMPERATURE vs. TRANSFORMATION PRODUCT` -- Y: 4.4".

**BLOCK B -- Master Temperature Table**

Y: 5.0" to 14.0". Column widths (23.0" total):
- Salt Temp (4.0") | Bainite Type (4.0") | Hardness (3.5") | Elongation (2.5") | Toughness (3.5") | Best Applications (5.5")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.

Data rows: alternating `#1E2435` / `#252B3D`, H: 1.8" (tall rows for readability).

| Salt Temp | Bainite Type | Hardness | Elong. | Toughness | Best Applications |
|---|---|---|---|---|---|
| 400--500 F (204--260 C) | Lower bainite | 50--55 HRC / 460--550 HB | 1--4% | Moderate | High-strength springs, clips, wear parts |
| 500--600 F (260--316 C) | Mixed bainite | 42--50 HRC / 390--460 HB | 4--7% | Good | Structural components, fasteners |
| 600--700 F (316--371 C) | Upper bainite | 35--42 HRC / 320--390 HB | 7--12% | Very good | Gears (ADI), impact-loaded parts |
| 700--750 F (371--399 C) | Coarse bainite / ausferrite | 30--38 HRC / 280--340 HB | 10--18% | Excellent | High-ductility ADI, shock absorbers |

Data: JetBrains Mono Regular, 13 pt, `#F0EDE8`. Temp ranges: `#E8A020`. Bainite type: Inter Medium, 14 pt.

**Color coding for temperature bands:**
- 400-500 F row: left accent `#E05C5C` (high hardness = demanding)
- 500-600 F row: left accent `#E8A020` (balanced)
- 600-700 F row: left accent `#27AE60` (tough = sweet spot for ADI)
- 700-750 F row: left accent `#2EC4B6` (maximum ductility)

**Key insight callout (Y: 13.5"):**
- Rounded rect, full width, H: 0.6", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Lower temperature = harder but less ductile. Higher temperature = tougher but softer. Choose based on application requirements.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Lower vs. Upper Bainite

**Section label:** `LOWER BAINITE vs. UPPER BAINITE` -- Y: 14.7".

**BLOCK C -- Side-by-Side Comparison**

Y: 15.3" to 21.3".

**Left -- Lower Bainite (X: 0.5", W: 11.0"):**

Rounded rect, fill `#1E2435`, left accent `#E8A020`, radius 6.

Title: `LOWER BAINITE` -- Barlow SemiBold, 20 pt, `#E8A020`
Subtitle: `400--500 F (204--260 C)` -- JetBrains Mono Regular, 14 pt, `#E8A020` at 70%

Properties (Inter Regular 14 pt `#F0EDE8`, line height 155%):

| Property | Value |
|---|---|
| Morphology | Fine acicular ferrite + carbide within plates |
| Hardness | 50--55 HRC |
| Tensile strength | 250--300 ksi |
| Elongation | 1--4% |
| Impact toughness | Better than martensite at same HRC |
| Fatigue strength | Excellent (compressive surface stress) |
| Wear resistance | Very good |
| Comparable to | Tempered martensite at 50--55 HRC -- but tougher |

Labels: Inter Medium 13 pt `#F0EDE8` at 60%. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.

Bottom highlight:
- Rounded rect, W: 10.0", H: 0.5", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Choose lower bainite when hardness and strength are primary requirements` -- Inter Medium, 13 pt, `#E8A020`

**Right -- Upper Bainite (X: 12.0", W: 11.5"):**

Rounded rect, fill `#1E2435`, left accent `#2EC4B6`, radius 6.

Title: `UPPER BAINITE` -- Barlow SemiBold, 20 pt, `#2EC4B6`
Subtitle: `600--750 F (316--399 C)` -- JetBrains Mono Regular, 14 pt, `#2EC4B6` at 70%

| Property | Value |
|---|---|
| Morphology | Coarser ferrite laths + carbide between laths |
| Hardness | 30--42 HRC |
| Tensile strength | 150--200 ksi |
| Elongation | 7--18% |
| Impact toughness | Excellent -- highest of any bainite |
| Fatigue strength | Good |
| Wear resistance | Moderate |
| Comparable to | Normalized + tempered -- but stronger |

Bottom highlight:
- Rounded rect, W: 10.5", H: 0.5", fill `#2EC4B6` at 15%, border 1 pt `#2EC4B6`
- Text: `Choose upper bainite when ductility and impact resistance are primary requirements` -- Inter Medium, 13 pt, `#2EC4B6`

---

### ZONE 5 -- ASTM A897 ADI Grade Mapping

**Section label:** `ASTM A897 ADI GRADES -- SALT BATH TEMPERATURE TARGETS` -- Y: 21.7".

**BLOCK D -- ADI Grade Table**

Y: 22.3" to 27.3". Column widths (23.0" total):
- Grade (2.5") | Tensile (ksi) (3.5") | Yield (ksi) (3.0") | Elong. (%) (2.5") | Hardness (HB) (3.5") | Salt Temp Range (4.0") | Bainite Type (4.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 13 pt, `#F0EDE8`.

| Grade | Tensile | Yield | Elong. | Hardness | Salt Temp | Bainite |
|---|---|---|---|---|---|---|
| 1 | 125 min | 80 min | 10 min | 269--321 | 700--750 F | Upper / ausferrite |
| 2 | 150 min | 100 min | 7 min | 302--363 | 650--700 F | Upper |
| 3 | 175 min | 125 min | 4 min | 341--444 | 575--650 F | Mixed |
| 4 | 200 min | 155 min | 1 min | 388--477 | 500--575 F | Lower |
| 5 | 230 min | 185 min | 0 min | 444--555 | 450--500 F | Lower |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`. Grade numbers: Inter Medium, 14 pt, `#E8A020`.

**Note below table:**
- `ADI = Austempered Ductile Iron. Properties depend on base iron nodularity (min 80%), alloy additions (Cu, Ni, Mo), and austenitizing temperature. Salt temperatures shown are typical starting points -- optimize for your specific casting.` -- Inter Regular, 12 pt, `#F0EDE8` at 70%

---

### ZONE 6 -- Temperature Control Best Practices

**Section label:** `MAINTAINING +/-5 F UNIFORMITY` -- Y: 27.7".

**BLOCK E -- Best Practices Panel**

Y: 28.3" to 32.3". Rounded rect, full width, H: 3.8", fill `#1E2435`, left accent `#27AE60`, radius 8.

Two-column layout:

**Left -- DO (W: 11.0"):**
- Title: `BEST PRACTICES` -- Barlow SemiBold, 16 pt, `#27AE60`
- Items (Inter Medium 13 pt `#F0EDE8`, line height 160%):
```
Run agitation continuously during processing
Calibrate bath thermocouples monthly (AMS 2750)
Use multiple TC zones for baths > 500 gal
Pre-heat loads to reduce thermal shock to bath
Monitor bath temperature recovery after immersion
Size bath volume to load mass (min 5:1 salt-to-part weight ratio)
```

**Right -- DON'T (W: 11.0"):**
- Title: `COMMON MISTAKES` -- Barlow SemiBold, 16 pt, `#E05C5C`
- Items (Inter Medium 13 pt `#F0EDE8`, line height 160%):
```
Overloading bath -- drops temp 20-30 F on immersion
Skipping agitation -- +/-15-25 F stagnant zones
Ignoring recovery time -- parts transforming at wrong temp
Contaminating salt -- water or oil in bath = catastrophic
Single TC on large bath -- measures one spot, not the load
Using salt past its service life -- degraded heat transfer
```

---

### ZONE 7 -- Footer

Standard. Title: `Salt Bath Temperature Control -- Austempering`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 4; ASTM A897/A897M. Exact temperatures and hold times depend on steel grade, section size, and specification requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Salt Bath Temp Control Austempering -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The temperature-to-properties table is THE reference on this poster -- it must be readable at 6 feet with generous row heights. The color-coded left accents on each temperature band create an instant visual gradient from "hot/hard" to "cool/tough." The ADI grade mapping connects ASTM A897 spec requirements directly to salt bath settings -- this is the bridge between the spec and the shop floor. The lower vs. upper bainite comparison answers the metallurgist's question; the ADI table answers the quality engineer's question.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #636 -- Construction Workup v1.0*
*2026-04-26*
