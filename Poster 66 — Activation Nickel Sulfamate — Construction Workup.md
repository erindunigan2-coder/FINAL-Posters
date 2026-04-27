---
Project: Plating Posters Inc
Poster Number: 66
Title: "Activation -- Nickel (Sulfamate)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-05 technical reference (Sulfamate nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Acid activation and Wood's nickel strike for sulfamate nickel plating. Same activation protocols as Watts nickel. Wood's strike required for same substrates.
Process Scope: Activation stage for sulfamate nickel plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Sulfamate
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP05
---

# Poster #66 -- Construction Workup
## Activation -- Nickel (Sulfamate)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Same activation protocols as Watts nickel (Poster #58). The substrate decision tree, acid selection, and Wood's strike requirements are identical. The sulfamate-specific angle: many sulfamate applications involve aerospace substrates (Inconel, Waspaloy, titanium, stainless) that require Wood's strike as standard practice -- not the exception. Also, electroforming mandrels may require specialized activation or release layers instead of conventional acid activation.

Hero visual: same substrate decision tree as Poster #58 but with aerospace and electroforming substrates highlighted.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
Same construction as Poster #58. Decision tree, Wood's strike panel, acid selection table, HE caution. Additional unique elements: aerospace substrate emphasis and electroforming mandrel activation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Amber)
ZONE 3 -- SUBSTRATE DECISION TREE HERO (4.2"--15.5" / ~11.3")
  Block B: Decision tree with aerospace emphasis
  Block C: Wood's strike parameters
ZONE 4 -- ACID SELECTION + ELECTROFORMING MANDRELS (15.5"--21.5" / ~6.0")
  Block D: Acid selection table
  Block E: Mandrel activation/release methods
ZONE 5 -- HE CAUTION + AEROSPACE NOTES (21.5"--27.0" / ~5.5")
  Block F: Hydrogen embrittlement warning
  Block G: Aerospace substrate notes
ZONE 6 -- FAILURE MODES + SAFETY (27.0"--32.5" / ~5.5")
  Block H: 4 activation failure modes
  Block I: Safety
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Sulfamate) -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Aerospace alloys, electroforming mandrels, stainless steel -- sulfamate substrates demand precision activation.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean but oxidized surface --> After: Active metal or prepared mandrel ready for sulfamate deposition`

---

### ZONE 3 -- Substrate Decision Tree Hero

**Section label:** `WHICH ACID? DO YOU NEED A STRIKE? -- SULFAMATE SUBSTRATES` -- Y: 4.4".

**BLOCK B -- Decision Tree**

Same flowchart structure as Poster #58 but with sulfamate-relevant substrates emphasized. The aerospace substrates (stainless, Inconel) are more prominent because they represent a larger share of sulfamate work.

Top node: `WHAT IS YOUR SUBSTRATE?`

Branches:

| Substrate Node | Fill | Acid Path | Strike Required? |
|---|---|---|---|
| STEEL (MILD/ALLOY) | `#1E2435`, accent `#2EC4B6` | HCl 10--30% v/v, 15--60 sec | NO |
| HIGH-STRENGTH STEEL | `#1E2435`, accent `#E05C5C` | HCl 10--30%, 15--30 sec MAX | NO (minimize time) |
| COPPER / BRASS | `#1E2435`, accent `#E8A020` | H2SO4 5--10% v/v, 15--30 sec | NO |
| STAINLESS / INCONEL / WASPALOY | `#1E2435`, accent `#E05C5C` | HCl 10--30%, 15--30 sec | MANDATORY -- Wood's strike |
| ELECTROFORMING MANDREL | `#1E2435`, accent `#E8A020` | See mandrel section | RELEASE LAYER instead |

**BLOCK C -- Wood's Nickel Strike Panel**

Same content as Poster #58. Identical Wood's strike composition:
```
NiCl2 * 6H2O:   240 g/L (32 oz/gal)
HCl (37%):      125 mL/L (16 oz/gal)
Temperature:    Ambient to 90 F (32 C)
Current density: 20--70 ASF
Time:           2--5 min
Anodes:         Nickel (depolarized or carbonized)
```

Additional note for sulfamate context: `For sulfamate applications, Wood's strike is standard operating procedure on most substrates -- not the exception. Aerospace specs (AMS 2403, AMS 2424) typically mandate it for Inconel, stainless, and re-plate work.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 4 -- Acid Selection + Electroforming Mandrels

**Two-column layout (Y: 15.7" to 21.3"):**

**Left -- Acid Selection Table (X: 0.5", W: 11.0"):**

Same table as Poster #58 but with sulfamate-relevant substrates:

| Substrate | Acid | Concentration | Time | Notes |
|---|---|---|---|---|
| Steel (mild/alloy) | HCl | 10--30% v/v | 15--60 sec | Standard |
| High-strength steel | HCl | 10--30% v/v | 15--30 sec MAX | HE risk |
| Copper / Brass | H2SO4 | 5--10% v/v | 15--30 sec | Standard |
| Stainless steel | HCl | 10--30% | 15--30 sec | Then Wood's strike |
| Inconel / Waspaloy | HCl | 10--30% | 15--30 sec | Then Wood's strike |
| Titanium | HF/HNO3 | Per AMS spec | Per spec | Special etch + Wood's |

**Right -- Electroforming Mandrel Activation (X: 12.5", W: 11.0"):**

- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `MANDREL PREPARATION -- NOT ACID ACTIVATION` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):

> Electroforming mandrels do not receive conventional acid activation. Instead, they require a release layer that allows the sulfamate deposit to separate cleanly after plating.
>
> **Common mandrel preparation methods:**
> - Aluminum: chromate or anodize release layer
> - Steel: thin chrome flash (0.1--0.3 microns) or proprietary release agent
> - Wax/epoxy: no chemical treatment; surface finish is critical
> - Glass: conductive coating (sputtered metal or conductive paint)
>
> The mandrel surface directly determines the surface quality of the electroform. Polish and prepare mandrels as carefully as you would a mold tool.

---

### ZONE 5 -- HE Caution + Aerospace Notes

**Two-column layout (Y: 21.7" to 26.8"):**

**Left -- HE Warning (X: 0.5", W: 14.0"):**

Same content as Poster #58 HE warning. Additionally:

> Sulfamate nickel is frequently applied to high-strength aerospace components. HE baking is almost always required. Aerospace specifications (AMS 2424) may require baking within 1 hour of plating -- stricter than the standard 4-hour ASTM B850 window. Verify the governing specification before starting production.

**Right -- Aerospace Substrate Notes (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#1E2435`, left accent `#2EC4B6`
- Title: `AEROSPACE SUBSTRATES` Barlow SemiBold 16 pt `#2EC4B6`
- Body (Inter Regular 13 pt `#F0EDE8`):

> - Inconel 718: Wood's strike mandatory. HCl activation, short immersion.
> - Waspaloy: Same as Inconel. Heat treat history affects activation.
> - Titanium: HF/HNO3 etch per specification. Extremely hazardous -- dedicated equipment.
> - 4340 / 300M steel: HCl activation, 15 sec max. HE bake mandatory (23 hr minimum per some specs).

---

### ZONE 6 -- Failure Modes + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- 4 Activation Failures (X: 0.5", W: 14.0"):**

| Failure | Root Cause | Effect in Sulfamate Bath |
|---|---|---|
| Under-activation | Time too short, acid too dilute | Adhesion failure -- deposit peels under stress |
| Over-activation | Time too long on aerospace alloys | Intergranular attack, weakened substrate |
| Skipping Wood's strike | Assumed unnecessary on stainless/Inconel | Deposit peels immediately -- catastrophic |
| Mandrel release failure | Improper or absent release layer | Electroform cannot be separated from mandrel |

**Right -- Safety (X: 15.5", W: 8.0"):**

Same as Poster #58 plus:
> - Titanium activation uses HF/HNO3 -- extreme burn hazard. Calcium gluconate gel must be immediately available.
> - Aerospace shops: follow facility-specific safety protocols for each substrate.

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Nickel (Sulfamate)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Nickel Sulfamate -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is 75% identical to Poster #58 (Watts Activation). The 25% difference: aerospace substrate emphasis (Inconel, Waspaloy, titanium), electroforming mandrel preparation replacing conventional acid activation for that application, and stricter HE baking windows per aerospace specs. The mandrel preparation callout is the unique content that makes this poster indispensable for electroforming shops. The decision tree should visually emphasize that for sulfamate work, Wood's strike is the norm, not the exception.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #66 -- Construction Workup v1.0*
*2026-04-26*
