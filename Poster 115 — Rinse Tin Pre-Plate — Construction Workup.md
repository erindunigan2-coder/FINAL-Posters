---
Project: Plating Posters Inc
Poster Number: 115
Title: "Rinse -- Tin -- Pre-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Pre-plate rinse for acid tin plating (Stage 4 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - Rinse
  - PrePlate
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #115 -- Construction Workup
## Rinse -- Tin -- Pre-Plate

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 4 of 8. The last rinse before parts enter the tin plating bath. This rinse removes residual activation acid. Acid drag-in lowers the bath pH, wastes tin chemistry, and introduces contaminants (dissolved metal from the activation step). For tin, this rinse is also the last chance to prevent chloride contamination if HCl was used for activation on steel substrates.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse tank cross-section hero (Block B):** Same format as Poster #113 but with acid drag-in emphasis instead of alkaline.
2. **Drag-in chemistry panel (Block D):** What acid drag-in does to the tin bath.
3. **Chloride contamination callout (Block E):** Special warning for HCl activation residue.
4. **Rinse quality metrics strip (Block F):** pH, conductivity, and flow checks.

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
  Stage 4 highlighted (Teal)
ZONE 3 -- RINSE TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DRAG-IN TO TIN BATH (14.5"--20.5" / ~6.0")
ZONE 5 -- CHLORIDE WARNING (20.5"--26.5" / ~6.0")
ZONE 6 -- RINSE QUALITY METRICS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin Plating -- Pre-Plate -- Stage 4 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Last stop before the tin bath. Acid carry-over wastes chemistry and introduces contaminants you cannot see.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Activated surface with acid film  -->  After: Acid-free surface entering tin bath`

---

### ZONE 3 -- Rinse Tank Hero

**Section label:** `THE PRE-PLATE RINSE` -- Y: 4.4".

**BLOCK B -- Rinse Tank Cross-Section**

Y: 5.0" to 14.0". Same visual structure as Poster #113 but with acid-specific labeling.

**Tank body:**
- Rounded rect, X: 2.0", Y: 5.5", W: 20.0", H: 7.0"
- Fill: `#252B3D`
- Border: 2 pt `#2EC4B6`

**Parts entering (left side):**
- Border: 2 pt `#E8A020` (acid contamination)
- Label: `PARTS IN` Barlow SemiBold 14 pt `#E8A020`
- Annotation: `Carrying activation acid + dissolved metal` Inter Regular 12 pt `#E8A020`

**Parts exiting (right side):**
- Border: 2 pt `#27AE60`
- Label: `PARTS OUT` Barlow SemiBold 14 pt `#27AE60`
- Annotation: `Acid-free, ready for tin plating` Inter Regular 12 pt `#27AE60`

**Key parameters:**
- `Temperature: Ambient` JetBrains Mono 14 pt `#F0EDE8`
- `Water: City or DI` JetBrains Mono 14 pt `#F0EDE8`
- `Flow: Continuous overflow` JetBrains Mono 14 pt `#2EC4B6`
- `Time: 30--60 sec immersion` JetBrains Mono 14 pt `#F0EDE8`

**Bottom callout:**
- `This rinse prevents acid drag-in from lowering the tin bath pH and contaminating the solution with dissolved metals from the activation step.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Drag-In to Tin Bath

**Section label:** `WHAT ACID DRAG-IN DOES TO YOUR TIN BATH` -- Y: 14.7".

**BLOCK D -- Consequences Panel**

Y: 15.3" to 20.0". Full-width rounded rect, fill `#1E2435`.

Three-column layout:

| Column | Header Color | Header | Content |
|---|---|---|---|
| Left | `#E8A020` | `pH DROP` | Excess acid lowers pH below operating range. Low pH = rough, powdery tin deposit. Acid also accelerates Sn2+ oxidation to Sn4+. |
| Center | `#E05C5C` | `METAL CONTAMINATION` | Dissolved copper, iron, or zinc from activation acid drags into the tin bath. Iron >20 ppm darkens the deposit. Copper causes immersion deposits. |
| Right | `#E05C5C` | `CHEMISTRY WASTE` | Every ounce of acid carried in must be neutralized or compensated. Drag-in is money down the drain -- literally. |

Bottom rule: `Good rinsing extends bath life. Poor rinsing shortens it.` Inter Medium 14 pt `#27AE60`

---

### ZONE 5 -- Chloride Warning

**Section label:** `CHLORIDE CONTAMINATION -- THE HIDDEN THREAT` -- Y: 20.7".

**BLOCK E -- Chloride Warning Panel**

Y: 21.3" to 26.0".

**Full-width coral-tinted panel:**
- Rounded rect, X: 0.5", W: 23.0", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `HCl ACTIVATION + TIN BATH = CHLORIDE RISK` Barlow SemiBold 22 pt `#E05C5C`

**Content (two columns inside panel):**

Left column:
- `If HCl was used for steel activation:`
- `Chloride ions drag into the rinse and then the tin bath`
- `Chloride attacks tin anodes -- promotes uneven dissolution`
- `Chloride causes pitting and hazy deposits`
- `Threshold: < 10 ppm Cl- in acid sulfate tin bath`

Right column:
- `Prevention:`
- `Use H2SO4 activation instead of HCl whenever possible`
- `If HCl is required: add an extra rinse stage`
- `Double-rinse with counterflow cascade`
- `Monitor rinse water conductivity before tin tank`
- `Test tin bath for chloride periodically`

Bottom note: `If you run HCl activation and acid sulfate tin on the same line, this rinse is the firewall. Treat it that way.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Rinse Quality Metrics

**Section label:** `RINSE QUALITY CHECKS` -- Y: 26.7".

**BLOCK F -- Metrics Strip**

Y: 27.3" to 32.0". Four metric cards.

| Card | X | Metric | Target | Method |
|---|---|---|---|---|
| 1 | 0.5" | pH | 5.0--7.0 | pH paper or meter |
| 2 | 6.33" | CONDUCTIVITY | < 50 microS/cm | Conductivity meter |
| 3 | 12.16" | CHLORIDE | < 10 ppm in rinse | Chloride test strips or titration |
| 4 | 18.0" | FLOW RATE | 2--4 gal/min minimum | Flow meter or timed bucket |

Each card: Rounded rect, W: 5.5", H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Tin -- Pre-Plate`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Tin Pre-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chloride contamination warning is the unique value-add for this poster. Most rinse posters cover generic drag-in -- this one addresses the specific cross-contamination risk of HCl activation residue in an acid sulfate tin bath. The chloride threshold (<10 ppm) is a concrete number operators can test against.

---

*Alaina -- Plating Posters Inc*
*Poster #115 -- Construction Workup v1.0*
*2026-04-26*
