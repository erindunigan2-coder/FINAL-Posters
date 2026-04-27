---
Project: Plating Posters Inc
Poster Number: 373
Title: "Chemical Prep -- Descaling Baths"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Industry-standard chemical descaling bath formulations -- alkaline permanganate conditioning and molten salt descaling. Mechanical media selection and blast parameter setup.
Process Scope: Bath preparation and equipment setup for descaling -- alkaline permanganate, molten salt, and blast media/parameters
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - BathPreparation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #373 -- Construction Workup
## Chemical Prep -- Descaling Baths

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This poster covers the preparation and control of the two major chemical descaling systems (alkaline permanganate and molten salt) plus mechanical blast setup parameters. It is the "recipe and equipment" poster -- the operator who needs to make up a bath or set up a blast cabinet starts here.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Alkaline permanganate composition panel (Block B):** Four-row composition table with concentration, function, and operating parameters.

2. **Molten salt descaling panel (Block C):** Parameter table for the aggressive high-temperature process.

3. **Blast parameter setup (Block D):** Pressure, distance, angle, and coverage requirements.

4. **Analytical control callout (Block E):** How to monitor chemical descaling baths.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- CHEMICAL DESCALING BATHS / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Alkaline permanganate composition + operating parameters
  Block C: Molten salt descaling parameters

ZONE 3 -- MECHANICAL BLAST PARAMETERS (14.5"--22.0" / ~7.5" tall)
  Block D: Blast setup table + coverage requirements

ZONE 4 -- ANALYTICAL CONTROL (22.0"--28.5" / ~6.5" tall)
  Block E: Bath monitoring procedures and action levels

ZONE 5 -- KEY WARNINGS (28.5"--32.5" / ~4.0" tall)
  Block F: Four critical prep warnings

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block G: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CHEMICAL PREP` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Descaling Bath Preparation, Media Setup & Control` -- 32 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Alkaline permanganate, molten salt, and blast media -- set up right or tear down early. This poster covers every descaling prep method.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Chemical Descaling Baths (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> CHEMICAL DESCALING -- TWO METHODS

---

**BLOCK B -- Alkaline Permanganate Descale Bath (Left Panel)**

Rounded rect, X: 0.5", Y: 3.8", W: 11.0", H: 10.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E8A020`.
Title: `ALKALINE PERMANGANATE CONDITIONING` -- Barlow SemiBold, 20 pt, `#E8A020`.
Subtitle: `For Cr-containing oxides, alloy steel scale, and stainless conditioning` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

**Composition table inside panel:**

Header: `#3A4055` fill. Barlow SemiBold 13 pt `#F0EDE8`.

| Component | Concentration | Function |
|---|---|---|
| Sodium hydroxide (NaOH) | 50--100 g/L (6.7--13.4 oz/gal) | Alkalinity; aids oxide dissolution |
| Potassium permanganate (KMnO4) | 30--50 g/L (4--6.7 oz/gal) | Oxidizer; converts Cr-oxides to soluble chromates |

Data: JetBrains Mono Regular 12 pt `#F0EDE8`. Component names: Inter Medium 12 pt.

**Operating parameters below table:**

| Parameter | Value |
|---|---|
| Temperature | 80--95 C (175--205 F) |
| Immersion time | 15--60 min (depends on scale severity) |
| Agitation | Air or mechanical; gentle |
| Follow-up | Rinse --> Acid pickle to remove conditioned oxide |

Params: JetBrains Mono Regular, 14 pt, `#E8A020` for values. Inter Medium, 13 pt, `#F0EDE8` for labels.

**Bottom note:**
- Inter Medium, 12 pt, `#E8A020`
- `Permanganate does not remove scale directly -- it conditions refractory Cr-oxides so subsequent acid pickle can dissolve them`

---

**BLOCK C -- Molten Salt Descaling (Right Panel)**

Rounded rect, X: 12.0", Y: 3.8", W: 11.5", H: 10.2", fill `#1E2435`, radius 8.
Left accent: 0.06" `#E05C5C`.
Title: `MOLTEN SALT DESCALING` -- Barlow SemiBold, 20 pt, `#E05C5C`.
Subtitle: `The most aggressive chemical descaling method -- for the worst scale conditions` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

**Parameter rows:**

| Parameter | Detail |
|---|---|
| Salt composition | NaOH base + NaH (reducing) or NaNO3 (oxidizing) |
| Operating temperature | 400--500 C (750--930 F) |
| Immersion time | 5--20 minutes |
| Mechanism | Molten caustic chemically reduces/dissolves oxide; NaH reduces refractory oxides |
| Follow-up | Water quench (violent steam!) --> Acid pickle (dilute H2SO4 or HCl) --> Rinse |

Params: JetBrains Mono Regular, 14 pt, `#E05C5C` for values.

**DANGER callout (inside panel, bottom):**
- Rounded rect, fill `#E05C5C` at 15%, border 1 pt `#E05C5C`, radius 4
- Text: `DANGER: 400--500 C molten salt. Wet parts cause violent steam explosions. Parts must be bone-dry before immersion. No exceptions.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 3 -- Mechanical Blast Parameters

**Section label:** Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> BLAST SETUP PARAMETERS

---

**BLOCK D -- Blast Parameter Table**

Y: 15.4" to 19.5". Full-width table.

Column widths (23.0" total):
- Parameter (5.0") | Suction Blast (5.5") | Pressure Blast (5.5") | Notes (7.0")

Header row: `#3A4055` fill. Barlow SemiBold 14 pt.

| Parameter | Suction Blast | Pressure Blast | Notes |
|---|---|---|---|
| Air Pressure | 40--80 psi (275--550 kPa) | 60--100 psi (410--690 kPa) | Higher pressure = more aggressive removal |
| Nozzle Distance | 6--12 in (150--300 mm) | 6--12 in (150--300 mm) | Closer = more aggressive; farther = wider pattern |
| Angle of Impingement | 60--90 deg (max scale removal) | 60--90 deg | 45 deg for profile generation |
| Coverage | 100% visual min | 100% visual min | 200% for critical coatings (SSPC-SP 5 / NACE No. 1) |
| Media Flow Rate | Per nozzle size | Per nozzle size | Monitor consumption; worn media loses cutting power |

Data: JetBrains Mono Regular 12 pt. Notes: Inter Regular 12 pt at 70%.

**Coverage callout below table:**
- Rounded rect, X: 0.5", Y: 19.8", W: 23.0", H: 1.5", fill `#27AE60` at 12%, border 1 pt `#27AE60`, radius 4
- Text: `What does 200% coverage mean? Every square inch of the surface is hit by the blast stream twice. This is the standard for White Metal (SP-5) preparation for plating.` -- Inter Medium, 14 pt, `#27AE60`

---

### ZONE 4 -- Analytical Control

**Section label:** Centered. Y: 22.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> BATH MONITORING -- CHEMICAL DESCALING

---

**BLOCK E -- Monitoring Table + Notes**

Y: 22.9" to 28.3". Two-column layout.

**Left column (X: 0.5", W: 14.0") -- Permanganate Bath Monitoring:**

Rounded rect, fill `#1E2435`, radius 6.
Title: `ALKALINE PERMANGANATE MONITORING` -- Barlow SemiBold, 16 pt, `#E8A020`.

| Parameter | Method | Frequency |
|---|---|---|
| NaOH concentration | Titrate with H2SO4 to phenolphthalein endpoint | Weekly |
| KMnO4 concentration | Visual (purple intensity) + titrate with oxalic acid | Weekly |
| Dissolved metals (Cr, Fe) | When bath performance degrades | As needed |
| Temperature | Thermometer | Every run |

**Right column (X: 15.0", W: 8.5") -- Molten Salt Monitoring:**

Rounded rect, fill `#1E2435`, radius 6.
Title: `MOLTEN SALT MONITORING` -- Barlow SemiBold, 16 pt, `#E05C5C`.

| Parameter | Method |
|---|---|
| Salt level | Visual -- maintain above parts |
| Temperature | Pyrometer or thermocouple |
| Salt contamination | When descaling time increases significantly, salt is contaminated; partial or full replacement |
| NaH content (reducing bath) | Supplier-specific titration |

---

### ZONE 5 -- Key Warnings

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#E05C5C`.

> CRITICAL PREP WARNINGS

**BLOCK F -- Four Warning Cards**

Y: 29.4" to 32.3". Four cards, same construction as Poster #371 troubleshooting strip.

| Card | X | Warning | Detail |
|---|---|---|---|
| 1 | 0.5" | WET PARTS IN MOLTEN SALT | Causes violent steam explosion. Parts must be completely dry. Pre-heat parts at 200 C (400 F) before immersion. |
| 2 | 6.33" | PERMANGANATE ON SKIN | Causes deep brown/black staining. Wear gloves. Stains persist for days -- no quick removal. |
| 3 | 12.16" | SILICA SAND MEDIA | Prohibited in many jurisdictions. Causes silicosis (irreversible lung disease). Substitute steel, garnet, or aluminum oxide. |
| 4 | 18.0" | BLAST MEDIA CROSS-CONTAMINATION | Never use media from ferrous blasting on aluminum or stainless. Iron particles embed and cause corrosion. Dedicate media to substrate type. |

Per card: left accent `#E05C5C`. Warning: Barlow SemiBold 15 pt `#E05C5C`. Detail: Inter Regular 12 pt `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Chemical Prep -- Descaling Baths`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; SSPC/NACE standards. Consult your process supplier for application-specific formulations and equipment settings.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Chemical Prep Descaling -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster serves two distinct audiences: the chemical descaling operator making up alkaline permanganate or running a molten salt line, and the blast operator setting up media and pressure. The molten salt section must convey extreme severity -- this is the most dangerous single process in the entire Chemical Treatment cluster series. The permanganate-conditioning concept (it does not remove scale directly -- it conditions it for subsequent acid pickle) is counterintuitive and must be stated clearly.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #373 -- Construction Workup v1.0*
*2026-04-26*
