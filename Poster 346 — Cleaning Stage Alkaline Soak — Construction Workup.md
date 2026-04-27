---
Project: Plating Posters Inc
Poster Number: 346
Title: "Cleaning Stage -- Alkaline Soak"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters — Watson Research Brief (CT-1.4)"
Process Scope: Main cleaning step -- operating parameters, mechanism details, and common failures
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - AlkalineCleaning
  - CleaningStage
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT01
---

# Poster #346 -- Construction Workup
## Cleaning Stage -- Alkaline Soak

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 4 of 7 in the CT-01 cluster. This is the "main tank" poster -- the cleaning operation itself. The hero visual is a dual-mechanism diagram showing saponification on one side and emulsification on the other, because these are the two fundamentally different ways alkaline cleaners remove soil. The operating parameter table is substrate-specific (steel vs. aluminum vs. zinc die cast). The failure/fix table covers the five most common cleaning problems.

This is the densest poster in the CT-01 cluster. An operator staring at parts that are not coming clean should be able to look at this poster and diagnose the problem.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-mechanism diagram (Block B -- HERO):** Split visual -- left side shows saponification (fat + NaOH = soap + glycerol), right side shows emulsification (surfactant micelle encapsulating oil droplet). Both are text-based diagrams using rectangles, arrows, and labels.
2. **Operating parameter table (Block D):** Three-substrate table (steel, aluminum, zinc die cast) with temperature, time, NaOH concentration, and agitation.
3. **Surfactant science callout (Block E):** CMC and cloud point explanation.
4. **Failure/fix table (Block F):** Five common failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Poster 4 of 7 highlighted (Teal)
ZONE 3 -- DUAL-MECHANISM DIAGRAM / HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- OPERATING PARAMETERS BY SUBSTRATE (15.5"--22.0" / ~6.5")
ZONE 5 -- SURFACTANT SCIENCE (22.0"--27.5" / ~5.5")
ZONE 6 -- COMMON FAILURES (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `THE CLEANING STAGE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Alkaline Soak -- Where Saponification Meets Emulsification` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Two mechanisms, one tank, one goal: a water-break-free surface. Understand how your cleaner works and you will know why it fails.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Soiled substrate in rack or barrel --> After: Clean surface ready for rinse and water break test`

---

### ZONE 3 -- Dual-Mechanism Diagram (HERO)

**Section label:** `HOW YOUR CLEANER ACTUALLY WORKS -- TWO MECHANISMS` -- Y: 4.4".

**Two-column hero (Y: 5.0" to 15.0"):**

**Left -- Saponification (X: 0.5", W: 11.0"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `SAPONIFICATION` Barlow Condensed ExtraBold 24 pt `#27AE60`.
Subtitle: `For Animal & Vegetable Fats (Polar Oils)` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Reaction diagram (Y: 6.0" to 8.5"):**

Three boxes in a row connected by arrows:

| Box | Content | Color |
|---|---|---|
| Reactant 1 | `Fat / Oil` `(RCOOH)` | `#E8A020` |
| + | `NaOH` `(Alkali)` | `#2EC4B6` |
| Product | `RCOONa (Soap)` `+ Glycerol` | `#27AE60` |

Arrows: `+` between boxes 1 and 2, `-->` between box 2 and 3.
Each box: Rounded rect W: 3.0", H: 2.0", fill `#252B3D`.
Text: JetBrains Mono 14 pt.

**Key points below diagram:**
- Inter Regular 13 pt `#F0EDE8`, line height 155%:
```
- Requires elevated temperature (> 60 C / 140 F)
- Only works on fats containing fatty acid esters
- Products are fully water-soluble
- Higher NaOH = faster saponification
- This is why temperature matters so much
```

**Right -- Emulsification (X: 12.0", W: 11.5"):**

Rounded rect H: 9.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `EMULSIFICATION` Barlow Condensed ExtraBold 24 pt `#2EC4B6`.
Subtitle: `For Mineral Oils & Synthetic Lubricants (Non-Polar)` Barlow SemiBold 16 pt `#F0EDE8` at 60%.

**Micelle diagram (Y: 6.0" to 8.5"):**

Central circle representing oil droplet (fill `#E8A020` at 30%, border 2 pt `#E8A020`, W: 2.5", H: 2.5") with small lines radiating outward (surfactant tails pointing in, heads pointing out).

Labels around circle:
- Inside: `OIL DROPLET` JetBrains Mono 12 pt `#E8A020`
- Outward-pointing heads: `Hydrophilic head (water-loving)` Inter Regular 11 pt `#2EC4B6`
- Inward-pointing tails: `Hydrophobic tail (oil-loving)` Inter Regular 11 pt `#E8A020`
- Label beneath: `MICELLE` Barlow SemiBold 16 pt `#2EC4B6`

**Key points:**
```
- Surfactant molecules trap oil in micelles
- Micelles suspend oil in water phase
- CMC (critical micelle concentration): 0.1-1 g/L
- Above CMC, more surfactant does NOT help
- Temperature must stay BELOW cloud point
```

**Bottom callout spanning both columns (Y: 14.5"):**
- Rounded rect W: 23.0", H: 0.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- `Saponifiable soils are the easy ones -- just add heat and caustic. Non-saponifiable soils need surfactant. If you have both, you need both mechanisms working together.` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Operating Parameters by Substrate

**Section label:** `OPERATING PARAMETERS -- BY SUBSTRATE` -- Y: 15.7".

**BLOCK D -- Three-Substrate Table (Y: 16.3" to 21.8")**

Column widths (23.0" total):
- Parameter (4.0") | Steel / Iron (5.5") | Aluminum (6.5") | Zinc Die Cast (7.0")

Header row: fill `#3A4055`, H: 0.5". Barlow SemiBold 14 pt.

| Parameter | Steel / Iron | Aluminum | Zinc Die Cast |
|---|---|---|---|
| Temperature | 150-195 F (65-90 C) | 120-150 F (50-65 C) | 130-160 F (55-70 C) |
| Immersion Time | 3-10 min | 1-3 min | 2-5 min |
| NaOH Concentration | 45-90 g/L (6-12 oz/gal) | 10-30 g/L (1.3-4 oz/gal) | 30-60 g/L (4-8 oz/gal) |
| Agitation | Air agitation or solution movement preferred | Gentle -- avoid excessive turbulence | Moderate |
| Special Notes | No special restrictions; most forgiving | Silicate inhibitor required; etches above 30 g/L | Dissolves in strong caustic; limit exposure time |

Data: JetBrains Mono 13 pt `#F0EDE8`. Parameter labels: Inter Medium 14 pt.
Special Notes row: Inter Regular 12 pt; aluminum and zinc die cast in `#E8A020`.

---

### ZONE 5 -- Surfactant Science

**Section label:** `SURFACTANT SCIENCE -- THE 60-SECOND VERSION` -- Y: 22.2".

**BLOCK E -- Two Key Concepts (Y: 22.8" to 27.3")**

Two side-by-side callout boxes.

**Left -- CMC (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.0", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `CRITICAL MICELLE CONCENTRATION (CMC)` Barlow SemiBold 16 pt `#2EC4B6`
- Body: Inter Regular 13 pt `#F0EDE8`:
```
The minimum surfactant concentration needed to
form micelles and clean effectively.

Typical CMC: 0.1-1 g/L for nonionic surfactants

Below CMC: poor cleaning -- surfactant not forming micelles
At CMC: cleaning efficiency activates
Above CMC: cleaning efficiency plateaus -- more does not help
```
- Highlight: `Adding more surfactant above CMC wastes money and can cause foam problems` Inter Medium 12 pt `#E8A020`

**Right -- Cloud Point (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.0", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `CLOUD POINT` Barlow SemiBold 16 pt `#E8A020`
- Body:
```
The temperature at which nonionic surfactant
becomes insoluble and the solution turns cloudy.

Typical cloud point: 140-175 F (60-80 C)

ABOVE cloud point: emulsion breaks down
Oil re-deposits onto parts
Cleaning efficiency collapses

Match your surfactant cloud point to your
operating temperature -- or you will clean
parts and then un-clean them.
```

---

### ZONE 6 -- Common Failures

**Section label:** `WHAT GOES WRONG -- 5 COMMON FAILURES` -- Y: 27.7".

**BLOCK F -- Failure Table (Y: 28.3" to 32.3")**

| Failure | Cause | Fix |
|---|---|---|
| Water break (oil film after rinse) | Insufficient time/temp; bath exhausted; surfactant depleted | Increase time/temp; rebuild bath; add surfactant |
| White silicate residue on aluminum | Silicate too high, temp too high, or rinse inadequate | Reduce silicate; lower temp; improve rinse; add acid desmut after clean |
| Etching of aluminum | NaOH too high for substrate; temperature too high | Reduce NaOH; increase silicate inhibitor; lower temperature |
| Etching of zinc die cast | Excessive immersion time in strong caustic | Shorten time to < 3 min; reduce NaOH |
| Foam overflow | Surfactant overdose; drag-in of incompatible chemistry | Check surfactant concentration; use low-foam grade for spray |

Each row: Rounded rect H: 0.7", alternating fills.
Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning Stage -- Alkaline Soak`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASTM B322; Metal Finishing Guidebook. Surfactant CMC and cloud point values are generic ranges -- consult your supplier TDS for product-specific data.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Stage Alkaline Soak -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-mechanism hero is the unique feature of this poster. Most operators have no idea that their cleaner removes oil through two completely different chemical pathways depending on whether the oil is animal/vegetable or petroleum-based. The saponification reaction diagram and micelle diagram make this visible. The surfactant science callouts (CMC and cloud point) are the kind of "insider knowledge" that separates a competent operator from one who just dumps chemicals in a tank.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #346 -- Construction Workup v1.0*
*2026-04-26*
