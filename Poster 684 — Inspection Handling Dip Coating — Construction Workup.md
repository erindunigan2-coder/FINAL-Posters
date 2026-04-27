---
Project: Plating Posters Inc
Poster Number: 684
Title: "Inspection & Handling -- Dip Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters -- Watson Research Brief (Cluster 4, Section 4.9)"
Technical Source: Inspection and handling for dip coating -- thick-film DFT measurement (micrometer, ultrasonic), adhesion (peel/knife test for thick coats), flexibility (cold-temperature bend), hardness (Shore A and Shore D durometer), and five dip-coating-specific defects.
Process Scope: Inspection and handling for dip coating -- Stage 7 of 7
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - DipCoating
  - Inspection
  - ConstructionWorkup
  - PaintingCoating
  - ClusterPC04
---

# Poster #684 -- Construction Workup
## Inspection & Handling -- Dip Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 7. Dip coating inspection differs from thin-film processes in every dimension: thickness is measured in tens of mils (not tenths), adhesion is tested by manual peel (not cross-hatch tape pull), hardness is Shore durometer (not pencil), and flexibility is cold-temperature bend (not mandrel at room temp). The hero is a five-test battery adapted for thick coatings. The five dip-coating-specific defects panel highlights the failures unique to immersion processes: drip marks, bridging, pinholes, blistering, and thin spots.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Five-test battery (Block B -- HERO):** DFT, adhesion, hardness, flexibility, visual -- each adapted for thick dip coatings.
2. **Shore durometer detail (Block C):** Shore A vs. Shore D with material mapping.
3. **Cold-temperature flexibility (Block D):** The critical test for outdoor/dishwasher-rack applications.
4. **Defect grid (Block F):** 6 inspection defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- FIVE-TEST BATTERY HERO (4.2"--15.5" / ~11.3")
ZONE 4 -- SHORE DUROMETER DETAIL (15.5"--21.5" / ~6.0")
ZONE 5 -- COLD-TEMP FLEXIBILITY + CHEMICAL RESISTANCE (21.5"--26.5" / ~5.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Dip Coating -- Thick-Film Testing: Shore Hardness, Peel Adhesion, Cold Bend -- Stage 7 of 7` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Forget pencil hardness and cross-hatch tape pull. At 20 mils thick, you test with a durometer and you test adhesion by trying to peel it off with a knife.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Fully cured dip-coated part --> After: Quality-verified, inspected part ready for packaging`

---

### ZONE 3 -- Five-Test Battery Hero

**Section label:** `THE FIVE-TEST BATTERY -- ADAPTED FOR THICK COATINGS` -- Y: 4.4".

**BLOCK B -- Five Cards (Y: 5.0" to 15.0")**

Top row of 3, bottom row of 2.

**Top Row:**

*DFT Measurement (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `1. DFT MEASUREMENT` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters (JetBrains Mono 12 pt):
```
Thin films (< 10 mils):
  Magnetic/eddy current gauge (D7091)
Thick films (> 10 mils):
  Micrometer (cut cross-section)
  Ultrasonic thickness gauge
Typical range: 5--40+ mils
Measure at multiple locations
  (top, middle, bottom of part)
```
- Key: `Specify MINIMUM DFT, not target. Dip coating has inherent top-to-bottom variation.`

*Adhesion (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `2. ADHESION` -- Barlow SemiBold, 20 pt, `#2EC4B6`
- Parameters:
```
Thin films (< 5 mils):
  ASTM D3359 cross-hatch tape pull
  Pass: 4B--5B
Thick films (> 5 mils):
  Knife adhesion test
  Score and attempt to peel by hand
  Pass: cannot peel; cohesive failure
  Manual peel test (pull tab)
```
- Key: `Cross-hatch tape pull does not work on thick coatings -- the tape cannot overcome the bulk strength of a 20-mil film.`

*Hardness (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `3. HARDNESS (DUROMETER)` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
ASTM D2240
Shore A: Soft/flexible coatings
  (plastisol, rubber)
  Scale: 0--100 (higher = harder)
Shore D: Hard thermoplastics
  (nylon, rigid PE)
  Scale: 0--100 (higher = harder)
NOT pencil hardness -- that is
  for thin paint films
```
- Key: `Shore A for PVC/rubber. Shore D for nylon. Never mix the scales.`

**Bottom Row:**

*Flexibility (X: 0.5", W: 11.0"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `4. FLEXIBILITY` -- Barlow SemiBold, 20 pt, `#27AE60`
- Parameters:
```
Thin films: ASTM D522 mandrel bend (room temp)
Thick films: Cold-temperature bend test
  Bend at -20 F (-29 C) for outdoor/freezer apps
  Critical for dishwasher racks, outdoor furniture
  PVC: Must remain flexible at service temperature
  Nylon: Excellent cold flexibility
```
- Key: `Cold bend is the real-world test. A coating that passes at room temp but cracks at -20 F fails in winter service.`

*Visual Inspection (X: 12.0", W: 11.5"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `5. VISUAL INSPECTION` -- Barlow SemiBold, 20 pt, `#E8A020`
- Parameters:
```
Check for:
  Drip marks / curtaining at bottom
  Bare spots / thin areas
  Bridging across holes or slots
  Pinholes / blisters
  Color uniformity
  Surface texture (smooth, no lumps)
Lighting: Bright, even, no shadows
```

---

### ZONE 4 -- Shore Durometer Detail

**Section label:** `SHORE HARDNESS -- TWO SCALES, TWO WORLDS` -- Y: 15.7".

**Two-column layout (Y: 16.3" to 21.3"):**

**Left -- Shore A (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `SHORE A -- SOFT/FLEXIBLE COATINGS` -- Barlow SemiBold, 20 pt, `#2EC4B6`

| Material | Typical Shore A | Application |
|---|---|---|
| Soft PVC plastisol | 40--60 A | Tool grips, soft-touch handles |
| Standard PVC plastisol | 60--80 A | Dishwasher racks, wire goods |
| Hard PVC plastisol | 80--95 A | Fencing, rigid grips |
| Rubber (latex dip) | 30--70 A | Gloves, gaskets, flexible coatings |
| Silicone | 20--80 A | Medical, high-temp flexible coatings |

Note: `Shore A readings above 95 overlap with Shore D. Switch to Shore D for very hard materials.`

**Right -- Shore D (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `SHORE D -- HARD THERMOPLASTICS` -- Barlow SemiBold, 20 pt, `#E8A020`

| Material | Typical Shore D | Application |
|---|---|---|
| Nylon 11 (PA11) | 70--80 D | Chemical/abrasion resistance |
| Nylon 12 (PA12) | 70--80 D | Similar to PA11, lower moisture |
| Polyethylene (PE) | 55--70 D | Wire goods, tool handles |
| Polypropylene (PP) | 70--80 D | Chemical tanks, lab equipment |
| Rigid PVC | 75--85 D | Structural, non-flexible |

---

### ZONE 5 -- Cold-Temp Flexibility + Chemical Resistance

**Section label:** `SERVICE ENVIRONMENT TESTS` -- Y: 21.7".

**Two-column layout (Y: 22.3" to 26.3"):**

**Left -- Cold-Temperature Flexibility (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#27AE60`.
Title: `COLD-TEMPERATURE BEND TEST` -- Barlow SemiBold, 20 pt, `#27AE60`

- `Test coated sample by bending at low temperature`
- `Standard test temperatures:`
- `  -20 F (-29 C): Outdoor winter service`
- `  0 F (-18 C): Freezer/refrigeration`
- `  32 F (0 C): Mild cold service`
- `Pass: No cracking, crazing, or delamination at test temp`
- `Fail: Visible cracks or coating separation`

Applications requiring cold bend:
- `Dishwasher racks (hot wash + cold rinse cycles)`
- `Outdoor furniture and playground equipment`
- `Automotive underbody (winter road conditions)`

**Right -- Chemical Resistance (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#E8A020`.
Title: `CHEMICAL SPOT TEST` -- Barlow SemiBold, 18 pt, `#E8A020`

- `Apply reagent drops to cured coating surface`
- `Cover and expose for specified time (1--24 hr)`
- `Evaluate: staining, softening, blistering, dissolution`
- `Common reagents:`
- `  10% NaOH (alkali resistance)`
- `  10% H2SO4 (acid resistance)`
- `  Detergent solution (dishwasher simulation)`
- `  Mineral oil, gasoline (hydrocarbon resistance)`

Note: `PVC plastisol has good chemical resistance but poor solvent resistance. Nylon resists solvents but absorbs moisture. Know the service environment before selecting the coating.`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- 6 INSPECTION REJECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | DFT BELOW MINIMUM | `#E05C5C` | Insufficient dip time, low viscosity, or excessive drainage | Increase dip time; raise viscosity; reduce drain angle |
| R1C2 | ADHESION FAILURE (PEEL) | `#E05C5C` | Missing or wrong adhesion promoter primer | Verify primer type per matrix (Poster #680); cure primer fully |
| R1C3 | DRIP MARKS AT BOTTOM | `#E8A020` | Gravity drainage creating thick edge | Rotate parts during drain; extend drain time |
| R2C1 | PINHOLES / BLISTERS | `#E8A020` | Outgassing from substrate or trapped moisture | Pre-bake substrates; complete drying before dip |
| R2C2 | BRIDGING (HOLES/SLOTS) | `#2EC4B6` | High viscosity; coating spanning openings | Lower viscosity; increase drain time; clear bridges manually |
| R2C3 | COLD BEND FAILURE | `#2EC4B6` | Wrong plasticizer level or coating selection for temp | Increase plasticizer ratio; select nylon over PVC for cold service |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Inspection & Handling -- Dip Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D2240, D3359, D7091. Acceptance criteria are application-specific. Consult your dip coating supplier for recommended test methods and targets.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Dip Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The thick-film adaptation of every test method is the poster's core message: dip coating operates in a different dimensional universe from spray painting, and the inspection tools must match. Shore durometer replaces pencil hardness. Knife peel replaces cross-hatch tape pull. Cold bend replaces room-temperature mandrel. The two durometer scales (A and D) with material mapping give the inspector an immediate reference for which scale to use on which material. The cross-reference to Poster #680 (adhesion promoter matrix) in the defect grid reinforces the cluster's internal linkage.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #684 -- Construction Workup v1.0*
*2026-04-26*
