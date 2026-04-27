---
Project: Plating Posters Inc
Poster Number: 254
Title: "Post Treatment -- Electroless Palladium"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Process Scope: Post-treatment for electroless palladium (Stage 7-8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessPalladium
  - PostTreatment
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #254 -- Construction Workup
## Post Treatment -- Electroless Palladium

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7-8 of 8. Post-treatment for electroless palladium varies entirely by application. In ENEPIG, there is no post-treatment between Pd and Au -- the parts proceed directly to immersion gold, then to drying and storage. For hydrogen permeation membranes, a high-temperature anneal (400-600 C) in inert atmosphere optimizes grain structure and hydrogen selectivity. For electronics connectors, an optional thin gold flash enhances contact resistance and oxidation protection.

Hero visual: three application-specific post-treatment pathways shown as branching routes from the Pd rinse step.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-pathway hero (Block B):** Branching diagram from Pd rinse to three application endpoints: ENEPIG, membrane, connector.
2. **ENEPIG final sequence (Block D):** Au -> rinse -> dry -> storage.
3. **Membrane anneal parameters (Block E):** Temperature, atmosphere, time.
4. **Quality checklist (Block F):** Final inspection points.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per Series Design Prompt.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stages 7--8 highlighted (Amber)
ZONE 3 -- THREE-PATHWAY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- ENEPIG FINAL SEQUENCE (14.5"--20.5" / ~6.0")
ZONE 5 -- MEMBRANE + CONNECTOR POST-TREATMENT (20.5"--26.5" / ~6.0")
ZONE 6 -- FINAL QUALITY CHECKLIST (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `POST TREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Palladium -- Stages 7--8 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Three applications, three endpoints. The finish line depends on where the palladium is going.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stages 7-8 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly rinsed Pd surface  -->  After: Application-ready part -- soldered, bonded, or permeating`

---

### ZONE 3 -- Three-Pathway Hero

**Section label:** `POST-TREATMENT BY APPLICATION` -- Y: 4.4".

**BLOCK B -- Three-Pathway Diagram**

Y: 5.0" to 14.0".

**Entry node (left center):**
- Rounded rect, X: 0.5", Y: 8.0", W: 5.0", H: 2.0", fill `#27AE60` at 20%, border 2 pt `#27AE60`
- Text: `FROM Pd RINSE` Barlow SemiBold 16 pt `#27AE60`

**Three branching paths to the right:**

**Path 1 -- ENEPIG (top, Y: 5.5"):**
- Rounded rect, X: 7.0", Y: 5.0", W: 16.5", H: 2.5", fill `#1E2435`, top accent `#E8A020` 4 pt
- Title: `ENEPIG -- PROCEED TO IMMERSION GOLD` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `No heat treatment between Pd and Au`
  - `Immersion gold: 0.03--0.1 um (displacement reaction)`
  - `Then: rinse --> air knife dry --> oven 60--80 C --> N2 storage`
  - `IPC-4556 compliant stack complete`

**Path 2 -- Hydrogen Membrane (middle, Y: 8.5"):**
- Rounded rect, X: 7.0", Y: 8.0", W: 16.5", H: 2.5", fill `#1E2435`, top accent `#2EC4B6` 4 pt
- Title: `MEMBRANE -- HIGH-TEMPERATURE ANNEAL` Barlow SemiBold 18 pt `#2EC4B6`
- Content:
  - `Anneal: 400--600 C in N2 or Ar atmosphere`
  - `Time: 1--4 hours`
  - `Improves grain structure, H2 selectivity, mechanical integrity`
  - `Some membranes use Pd-Ag alloy (23--25% Ag) to resist H2 embrittlement at <300 C`

**Path 3 -- Electronics Connector (bottom, Y: 11.5"):**
- Rounded rect, X: 7.0", Y: 11.0", W: 16.5", H: 2.5", fill `#1E2435`, top accent `#C8D0D8` 4 pt
- Title: `CONNECTOR -- OPTIONAL GOLD FLASH` Barlow SemiBold 18 pt `#C8D0D8`
- Content:
  - `Thin immersion or electrolytic gold over Pd`
  - `Enhances contact resistance and oxidation protection`
  - `Pd alone provides excellent solderability and wire bondability`
  - `Gold flash is optional -- application-dependent`

---

### ZONE 4 -- ENEPIG Final Sequence

**Section label:** `ENEPIG -- THE COMPLETE STACK` -- Y: 14.7".

**BLOCK D -- Horizontal Stack Diagram (Y: 15.3" to 20.3")**

Visual: layered bar showing the ENEPIG stack from substrate up:

| Layer | Material | Thickness | Purpose |
|---|---|---|---|
| Substrate | Copper (PCB pad) | -- | Base metal |
| EN | Ni-P alloy (Mid-P 6--9%) | 3--6 um | Barrier + solderable layer |
| E-Pd | Pd or Pd-P | 0.05--0.3 um | Diffusion barrier (prevents Ni migration) |
| IG | Pure Au (immersion) | 0.03--0.1 um | Oxidation protection + solderability |

Stack visualization: four horizontal bars of increasing layer prominence, color-coded:
- Copper: `#E8A020` at 40%
- EN: `#2EC4B6`
- Pd: `#27AE60`
- Au: `#E8A020`

**Key callout below stack:**
- `The Pd layer is the black pad killer. Without it, Ni migrates into Au during immersion gold, creating a phosphorus-enriched "black pad" that causes solder joint failure. With it, ENEPIG achieves superior reliability over ENIG.` Inter Medium 14 pt `#27AE60`

---

### ZONE 5 -- Membrane + Connector Post-Treatment

**Section label:** `SPECIALIZED POST-TREATMENT PARAMETERS` -- Y: 20.7".

**Two callout boxes (Y: 21.3" to 26.3"):**

**Left -- Membrane Anneal (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `MEMBRANE ANNEAL PARAMETERS` Barlow SemiBold 18 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| Temperature | 400--600 C |
| Atmosphere | N2 or Ar (inert) |
| Time | 1--4 hours |
| Purpose | Optimize grain structure, H2 selectivity |
| Pd-Ag option | 23--25 wt% Ag resists H2 embrittlement <300 C |
| Substrate | Porous ceramic (Al2O3, ZrO2) |

**Right -- Storage and Handling (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `STORAGE AND HANDLING` Barlow SemiBold 18 pt `#E8A020`
- Content:
  - `ENEPIG boards: N2 atmosphere or vacuum-sealed bags`
  - `Shelf life before assembly: typically 6--12 months (spec-dependent)`
  - `Avoid contamination: clean nitrile gloves only`
  - `No bare-hand contact -- fingerprints degrade solderability`
  - `Store away from sulfur-containing compounds (tarnish risk)`
  - `Inspect per IPC-4556 before assembly`

---

### ZONE 6 -- Final Quality Checklist

**Section label:** `FINAL INSPECTION POINTS` -- Y: 26.7".

**BLOCK F -- Checklist Grid (Y: 27.3" to 32.3")**

| Position | Check | Color | What to Verify | Spec |
|---|---|---|---|---|
| R1C1 | Pd THICKNESS | `#27AE60` | XRF measurement | 0.05--0.3 um per IPC-4556 |
| R1C2 | SURFACE APPEARANCE | `#2EC4B6` | Visual: uniform, no staining or spots | Bright to semi-bright, no discoloration |
| R2C1 | SOLDERABILITY | `#E8A020` | Wetting balance or dip-and-look test | Per IPC J-STD-003 |
| R2C2 | WIRE BONDABILITY | `#E8A020` | Pull test / shear test on bonded wire | Per IPC-4556 requirements |

Each card: W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06".

---

### ZONE 7 -- Footer

Standard footer. Title: `Post Treatment -- Electroless Palladium`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; IPC-4556; ASTM standards. Consult your process supplier and applicable specifications.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Post Treatment Electroless Palladium -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster's unique feature is the three-pathway hero, which honestly represents the reality: electroless palladium has three very different endpoints, and the post-treatment is entirely application-dependent. The ENEPIG stack diagram in Zone 4 is the money shot -- it visually shows all four layers of the stack with their thicknesses, and the "black pad killer" callout is the punchline that justifies the entire poster cluster. The membrane and connector paths are secondary but technically complete for reference.

---

*Alaina -- Poster #254 -- Construction Workup v1.0 -- 2026-04-26*
