---
Project: Plating Posters Inc
Poster Number: 69
Title: "Rinse -- Nickel Sulfamate -- Post-Plate"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-05 technical reference (Sulfamate nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Post-plate rinse for sulfamate nickel plating. Removes sulfamate drag-out from parts before post-treatment. Key economic consideration: sulfamate concentrate is significantly more expensive than Watts chemistry -- drag-out recovery is strongly recommended.
Process Scope: Post-plate rinse for sulfamate nickel plating (Stage 6 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Sulfamate
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEP05
---

# Poster #69 -- Construction Workup
## Rinse -- Nickel Sulfamate -- Post-Plate

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 6 of 8. The post-plate rinse for sulfamate nickel has the same fundamental purpose as the Watts post-plate rinse (Poster #61): remove nickel chemistry from the part surface before post-treatment. But the economic stakes are higher -- sulfamate concentrate costs significantly more than Watts chemistry per gallon. Drag-out recovery is not just recommended; it is an economic necessity.

The post-treatment downstream varies: grinding for buildup/salvage, mandrel separation for electroforming, or topcoating. In all cases, the rinse must remove sulfamate residues cleanly.

Hero visual: double counterflow rinse with drag-out recovery and cost comparison callout.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse cascade hero (Block B):** Drag-out recovery + double counterflow.
2. **Cost comparison callout (Block C):** Sulfamate vs. Watts drag-out cost impact.
3. **Rinse parameter table (Block D).**
4. **Common failures (Block F).**
5. **Orientation strip:** Stage 6 highlighted (Teal).

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 6 highlighted (Teal)
ZONE 3 -- RINSE CASCADE HERO + COST CALLOUT (4.2"--15.0" / ~10.8")
  Block B: Drag-out recovery + double counterflow diagram
  Block C: Sulfamate vs. Watts drag-out cost comparison
ZONE 4 -- RINSE PARAMETERS (15.0"--21.0" / ~6.0")
  Block D: Parameter table
  Block E: DI water recommendation
ZONE 5 -- COMMON FAILURES (21.0"--27.0" / ~6.0")
  Block F: Common rinse failures
ZONE 6 -- DRAG-OUT RECOVERY BEST PRACTICES + SAFETY (27.0"--32.5" / ~5.5")
  Block G: Recovery best practices
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Sulfamate) -- Stage 6 of 8 -- Post-Plate` -- 34 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Sulfamate concentrate is expensive. Every gallon of drag-out you recover goes straight back to the bath -- and straight to the bottom line.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 6 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Freshly plated sulfamate Ni with bath drag-out  -->  After: Clean Ni surface ready for post-treatment`

---

### ZONE 3 -- Rinse Cascade Hero + Cost Callout

**Section label:** `THE POST-PLATE RINSE -- RECOVER AND PROTECT` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Rinse Cascade Diagram**

Y: 5.0" to 10.5". Three tank rectangles.

- Tank 1 -- Drag-Out Recovery (X: 0.5", W: 7.0", H: 5.0"): fill `#252B3D`, border 2 pt `#E8A020`
  - Title: `DRAG-OUT RECOVERY` Barlow SemiBold 16 pt `#E8A020`
  - Parameters (JetBrains Mono 13 pt `#F0EDE8`):
    ```
    Type: Static (no fresh water)
    Purpose: Capture concentrated sulfamate Ni
    Return: Periodically to plating bath
    Temp: Ambient
    ```
  - Tag: `ECONOMICALLY CRITICAL -- sulfamate is 2--3x Watts cost` Inter Medium 12 pt `#E8A020`

- Tank 2 -- Rinse 1 (X: 8.25", W: 7.0", H: 5.0"): fill `#252B3D`, border 2 pt `#2EC4B6`
  - Title: `RINSE 1 (OVERFLOW)` Barlow SemiBold 16 pt `#2EC4B6`

- Tank 3 -- Rinse 2 (X: 16.0", W: 7.5", H: 5.0"): fill `#252B3D`, border 2 pt `#27AE60`
  - Title: `RINSE 2 (FINAL)` Barlow SemiBold 16 pt `#27AE60`
  - Tag: `Parts exit --> to grind, topcoat, or inspection` Inter Medium 12 pt `#27AE60`

**BLOCK C -- Cost Comparison Callout**

Y: 11.0" to 14.8".

Two side-by-side callouts:

Left -- `SULFAMATE Ni DRAG-OUT` (W: 11.0", fill `#1E2435`, left accent `#E8A020`):
- `Sulfamate salt: premium-priced (2--3x Watts chemistry per kg Ni metal)`
- `Drag-out per barrel cycle: 0.5--2.0 gal/1,000 lbs`
- `Without recovery: $$ lost per shift`
- `With recovery: 50--80% chemistry returned to bath`

Right -- `WATTS Ni DRAG-OUT (for comparison)` (W: 11.5", fill `#1E2435`, left accent `#2EC4B6`):
- `Watts chemistry: lower cost per kg Ni`
- `Drag-out recovery still recommended but less economically urgent`
- `Sulfamate drag-out recovery pays back FASTER due to higher chemistry cost`

Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 4 -- Rinse Parameters

**Section label:** `RINSE PARAMETERS` -- Y: 15.2". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Parameter Table**

Y: 15.8" to 18.5".

| Parameter | Value |
|---|---|
| Rinse configuration | Drag-out recovery + double counterflow |
| Water temperature | Ambient |
| Water quality (final tank) | DI recommended (prevents water spotting on precision parts) |
| Target conductivity (final tank) | < 100 uS/cm |
| Immersion time per tank | 30--60 sec |
| Agitation | Parts dip or mild sparging |
| Key concern | Chemistry cost recovery; nickel discharge limits |

**BLOCK E -- DI Water Note**

Y: 18.8" to 19.8".

Rounded rect, fill `#27AE60` at 15%, border 1 pt `#27AE60`, W: 23.0", H: 0.8".
Text: `DI water in the final rinse is recommended for precision electroforming and aerospace parts. Mineral deposits from municipal water can interfere with dimensional inspection and downstream machining.` Inter Medium 13 pt `#27AE60`.

---

### ZONE 5 -- Common Failures

**Section label:** `WHAT GOES WRONG` -- Y: 21.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK F -- Common Rinse Failures**

Y: 21.8" to 26.8".

| Failure | Root Cause | Result |
|---|---|---|
| No drag-out recovery | Skipped or not maintained | Expensive sulfamate chemistry lost to drain |
| Nickel staining on parts | Inadequate rinsing; parts sat in contaminated rinse | Visible stains under inspection light |
| Water spots on precision parts | Municipal water used in final rinse | Interferes with dimensional measurement |
| Nickel contamination downstream | Drag-out carried to chrome or other bath | Haze, adhesion loss in subsequent plating |
| Rinse water exceeds Ni discharge | No drag-out recovery; heavy production | Wastewater Ni > permit limit (0.5--3.4 mg/L) |

Cards: fill `#1E2435`, alternating `#252B3D`. Failure: `#E05C5C`. Root Cause: `#F0EDE8`. Result: `#E8A020`.

---

### ZONE 6 -- Recovery Best Practices + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Drag-Out Recovery Best Practices (X: 0.5", W: 14.0"):**

Section label: `DRAG-OUT RECOVERY BEST PRACTICES` Barlow Condensed ExtraBold 20 pt `#F0EDE8`.

Callout box, fill `#1E2435`, left accent `#27AE60`:
- `Allow parts to drip for 10--15 sec over the plating tank before entering drag-out.`
- `Longer drain time = less drag-out = less recovery needed.`
- `Monitor drag-out tank Ni concentration -- return to bath when it reaches 50--70% of bath concentration.`
- `Check drag-out tank for contamination before returning to bath (pH, organics).`
- `Keep drag-out tank covered when not in use to prevent contamination.`
- `For electroforming mandrels: extra drip time reduces chemistry loss on large surfaces.`

Inter Regular 13 pt `#F0EDE8`, line height 155%.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`, radius 8
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - Rinse water contains nickel compounds -- dermal sensitizer.
> - Sulfamate drag-out adds ammonia to wastewater (from hydrolysis products). Monitor.
> - Nickel discharge limits: 0.5--3.4 mg/L (40 CFR 433).
> - Drain all rinse water to waste treatment -- not sanitary sewer.
> - PPE: nitrile gloves, goggles for rinse handling.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse -- Nickel Sulfamate -- Post-Plate`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table (see Poster #63).
**Export:** Six files -- `Rinse Nickel Sulfamate Post-Plate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The economic angle is the differentiator for this poster. Every other post-plate rinse poster in the series focuses on chemistry protection downstream. This one adds a strong economic dimension: sulfamate concentrate is expensive, and every gallon of drag-out you don't recover is money down the drain -- literally.

Watson's brief: "Sulfamate concentrate is expensive -- recover drag-out."

The nickel discharge limits callout is also important for regulatory awareness. Nickel is one of the more tightly regulated metals in wastewater.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #69 -- Construction Workup v1.0*
*2026-04-26*
