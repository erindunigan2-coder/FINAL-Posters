---
Project: Plating Posters Inc
Poster Number: 58
Title: "Activation -- Nickel (Watts)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster EP-04 technical reference (Watts nickel)"
  - "Watson Research Brief -- Electroplating Clusters EP-02 through EP-15"
Technical Source: Acid activation and Wood's nickel strike for Watts nickel plating. Covers substrate-specific acid selection, Wood's strike composition, and when a strike is mandatory vs. optional.
Process Scope: Activation stage for Watts nickel plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - NickelPlating
  - Watts
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP04
---

# Poster #58 -- Construction Workup
## Activation -- Nickel (Watts)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation removes residual oxides and exposes clean, active metal for nickel adhesion. This poster is more complex than typical activation posters because nickel plating spans many substrates -- steel, copper, brass, zinc die cast, stainless steel -- each requiring different acid chemistry. The Wood's nickel strike is the critical technique for difficult substrates.

Hero visual: substrate decision tree showing which acid and whether a Wood's strike is required.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Substrate decision tree hero (Block B):** Flowchart from substrate type to recommended acid and strike protocol. Built with rounded rectangles and arrows.
2. **Wood's strike parameters panel (Block C):** Detailed callout box with full Wood's strike composition.
3. **Acid selection table (Block D):** Substrate x acid type matrix.
4. **HE caution callout (Block E):** Prominent warning for high-strength steel.
5. **Failure modes strip (Block F):** 4 activation failures.

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
  Block B: Decision tree -- substrate to acid to strike
  Block C: Wood's strike parameters
ZONE 4 -- ACID SELECTION TABLE (15.5"--21.5" / ~6.0")
  Block D: Substrate x acid matrix with parameters
ZONE 5 -- HE CAUTION + TIMING (21.5"--27.0" / ~5.5")
  Block E: Hydrogen embrittlement warning
  Block F: Timing and transfer rules
ZONE 6 -- FAILURE MODES + SAFETY (27.0"--32.5" / ~5.5")
  Block G: 4 activation failure modes
  Block H: Safety callout
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Nickel (Watts) -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Remove the oxide. Expose the metal. If the surface is not active, the nickel will not stick.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean but oxidized surface --> After: Active, oxide-free metal ready for nickel deposition`

---

### ZONE 3 -- Substrate Decision Tree Hero

**Section label:** `WHICH ACID? DO YOU NEED A STRIKE?` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Decision Tree**

Y: 5.0" to 11.5". A flowchart with the substrate as the entry point.

Top node (centered):
- Rounded rect, W: 6.0", H: 1.2", fill `#E8A020`, radius 8
- Text: `WHAT IS YOUR SUBSTRATE?` Barlow SemiBold 18 pt `#1A1F2E`

Five branches descending to substrate nodes:

| Substrate Node | Fill | Acid Path | Strike Required? |
|---|---|---|---|
| STEEL (MILD) | `#1E2435`, accent `#2EC4B6` | HCl 10--30% v/v, 15--60 sec | NO |
| HIGH-STRENGTH STEEL | `#1E2435`, accent `#E05C5C` | HCl 10--30%, 15--30 sec MAX | NO (but minimize time) |
| COPPER / BRASS | `#1E2435`, accent `#E8A020` | H2SO4 5--10% v/v, 15--30 sec | NO |
| ZINC DIE CAST | `#1E2435`, accent `#E8A020` | HF 0.5--1% or proprietary, 5--15 sec | RECOMMENDED |
| STAINLESS / INCONEL / RE-PLATE | `#1E2435`, accent `#E05C5C` | HCl 10--30%, 15--30 sec | MANDATORY -- Wood's strike |

Each node: Rounded rect, W: 4.0", H: 2.5". Arrows from top node to each substrate node: 2 pt `#3A4055`.

Strike-required nodes have a connecting arrow to the Wood's strike panel (Block C).

**BLOCK C -- Wood's Nickel Strike Panel**

Y: 11.8" to 15.3". Full-width prominent callout.
- Rounded rect, fill `#1E2435`, border 2 pt `#E8A020`, radius 8, left accent `#E8A020` 0.08"

Title: `WOOD'S NICKEL STRIKE` Barlow Condensed ExtraBold 24 pt `#E8A020`
Subtitle: `The adhesion insurance policy for difficult substrates` Barlow SemiBold 14 pt `#F0EDE8` at 60%

Two-column layout inside:

*Left -- Composition:*
```
NiCl2 * 6H2O:   240 g/L (32 oz/gal)
HCl (37%):      125 mL/L (16 oz/gal)
Temperature:    Ambient to 90 F (32 C)
Current density: 20--70 ASF
Time:           2--5 min
Anodes:         Nickel (depolarized or carbonized)
```
JetBrains Mono 14 pt `#F0EDE8`

*Right -- When to Use:*
- Inter Medium 14 pt `#F0EDE8`, line height 160%

> - Stainless steel -- ALWAYS (passive oxide reforms in seconds)
> - Inconel, Monel, nickel-based alloys -- ALWAYS
> - Re-plating over old nickel or chrome -- ALWAYS
> - Parts with refractory oxide films -- ALWAYS
> - Clean steel, copper, or brass going directly to Watts -- NOT NEEDED

Bottom note: `The Wood's strike is an aggressive, highly acidic nickel bath. Its job is to etch through passive oxide layers while simultaneously depositing a thin nickel strike that the Watts bath can bond to.` Inter Regular 13 pt `#F0EDE8` at 70%.

---

### ZONE 4 -- Acid Selection Table

**Section label:** `ACID ACTIVATION PARAMETERS BY SUBSTRATE` -- Y: 15.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK D -- Parameter Table**

Y: 16.3" to 21.3". Column widths (23.0" total):
- Substrate (4.0") | Acid (4.0") | Concentration (3.5") | Temp (2.5") | Time (2.5") | Notes (6.5")

| Substrate | Acid | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Steel (mild) | HCl | 10--30% v/v | Ambient | 15--60 sec | Standard activation |
| High-strength steel (>31 HRC) | HCl | 10--30% v/v | Ambient | 15--30 sec MAX | Minimize H-charging; bake after plate |
| Copper / Brass | H2SO4 | 5--10% v/v | Ambient | 15--30 sec | HCl attacks copper alloys |
| Zinc die cast | HF or proprietary | 0.5--1% HF | Ambient | 5--15 sec | Very aggressive -- short immersion critical |
| Stainless steel | HCl | 10--30% v/v | Ambient | 15--30 sec | Then Wood's strike immediately |
| Inconel / Monel | HCl | 10--30% v/v | Ambient | 15--30 sec | Then Wood's strike immediately |

Header: `#3A4055`. Rows: alternating `#1E2435` / `#252B3D`. Data: JetBrains Mono 12 pt. Notes: Inter Regular 12 pt.

---

### ZONE 5 -- HE Caution + Timing

**Two-column layout (Y: 21.7" to 26.8"):**

**Left -- Hydrogen Embrittlement Warning (X: 0.5", W: 14.0"):**

- Rounded rect, fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8
- Title: `HYDROGEN EMBRITTLEMENT WARNING` Barlow Condensed ExtraBold 22 pt `#E05C5C`
- Body (Inter Medium 14 pt `#F0EDE8`, line height 160%):

> High-strength steel (>31 HRC or >1000 MPa UTS) absorbs hydrogen during acid activation. This hydrogen causes delayed brittle fracture if not removed by baking.
>
> RULES:
> - Minimize acid immersion time (15--30 sec max)
> - Do not over-activate -- one dip is enough
> - Track total acid exposure across all steps
> - HE bake required after plating: 375 +/- 25 F for 3--24 hours
> - Bake within 4 hours of plating (ASTM B850)

**Right -- Transfer Timing (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `TIMING MATTERS` Barlow SemiBold 18 pt `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):

> - Activation to rinse: immediate (drain + transfer)
> - Rinse to plating: as fast as possible
> - Do not let activated parts air-dry -- oxides reform immediately
> - Stainless after Wood's strike: into Watts bath within 30 seconds

---

### ZONE 6 -- Failure Modes + Safety

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- 4 Activation Failures (X: 0.5", W: 14.0"):**

| Failure | Root Cause | Downstream Effect |
|---|---|---|
| Under-activation | Time too short or acid too dilute | Nickel peels or blisters |
| Over-activation (etch attack) | Time too long or acid too concentrated | Roughened substrate, pitting |
| Wrong acid for substrate | HCl on copper (attacks it) | Substrate damage, poor adhesion |
| Skipping Wood's strike on stainless | Passive oxide not removed | Nickel peels immediately |

Cards: fill `#1E2435`, left accent `#E05C5C`.

**Right -- Safety (X: 15.5", W: 8.0"):**

- Rounded rect, fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Title: `SAFETY` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Body:

> - HCl fumes: OSHA PEL 5 ppm ceiling. Ventilation mandatory.
> - HF (zinc die cast): extreme burn hazard. Calcium gluconate gel must be on hand.
> - Acid splashes: goggles, face shield, gloves, apron.
> - Never add water to acid. Add acid to water.

---

### ZONE 7 -- Footer

Standard footer. Title: `Activation -- Nickel (Watts)`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Nickel Watts -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The decision tree is the hero -- it answers the question every plater asks when setting up a nickel line: "what acid do I use and do I need a strike?" The Wood's strike panel must be prominent because skipping it on stainless or Inconel is a guaranteed adhesion failure. The HE warning is critical for aerospace and automotive shops.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #58 -- Construction Workup v1.0*
*2026-04-26*
