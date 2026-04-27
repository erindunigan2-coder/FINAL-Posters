---
Project: Plating Posters Inc
Poster Number: 114
Title: "Activation -- Tin"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid activation for tin plating (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - TinPlating
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterEP11
---

# Poster #114 -- Construction Workup
## Activation -- Tin

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 3 of 8. Activation removes surface oxides and exposes clean, active metal for tin deposition. Unlike nickel or zinc plating where HCl is standard, tin activation favors sulfuric acid -- especially for copper and brass substrates. This poster covers substrate-specific activation, the chemistry behind oxide removal, and the consequences of getting it wrong.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Activation mechanism diagram (Block B -- HERO):** Cross-section of a substrate surface showing oxide layer dissolving in acid, exposing clean metal beneath. Built with layered rectangles and annotation arrows.
2. **Substrate-specific activation table (Block D):** Parameters by substrate (copper/brass, steel, nickel-plated).
3. **Over-activation vs. under-activation callout (Block E):** Side-by-side showing what both look like.
4. **Safety strip (Block F):** Acid handling safety for sulfuric and hydrochloric.

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
  Stage 3 highlighted (Amber)
ZONE 3 -- ACTIVATION MECHANISM HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- SUBSTRATE ACTIVATION TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- OVER VS. UNDER ACTIVATION (20.5"--26.5" / ~6.0")
ZONE 6 -- SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Tin Plating -- Stage 3 of 8` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `Strip the oxide. Expose the metal. Give the tin something to grab onto.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean surface with oxide film  -->  After: Oxide-free metal ready for tin deposition`

---

### ZONE 3 -- Activation Mechanism Hero

**Section label:** `HOW ACID ACTIVATION WORKS` -- Y: 4.4".

**BLOCK B -- Surface Cross-Section Diagram**

Y: 5.0" to 14.0".

**Diagram concept:** Three-panel sequence showing:

Panel 1 (left third) -- `BEFORE`:
- Substrate layer (bottom): rounded rect, fill `#C8D0D8`, labeled `BASE METAL`
- Oxide layer (top): rounded rect, fill `#E05C5C` at 40%, labeled `OXIDE FILM`
- Annotation: `Surface oxides block adhesion` Inter Regular 13 pt `#E05C5C`

Panel 2 (center third) -- `DURING`:
- Substrate layer: same
- Oxide layer: partially dissolved, gaps showing
- Acid arrows pointing down at oxide: `H2SO4` labels, stroke 2 pt `#E8A020`
- Chemical equation: `Metal oxide + H2SO4 -> Metal sulfate + H2O` JetBrains Mono 13 pt `#E8A020`
- Annotation: `Acid dissolves oxide layer` Inter Regular 13 pt `#E8A020`

Panel 3 (right third) -- `AFTER`:
- Substrate layer: exposed, bright
- No oxide layer
- Fill `#27AE60` at 20% glow on surface
- Annotation: `Clean, active metal surface` Inter Regular 13 pt `#27AE60`
- `Ready for tin deposition` Inter Medium 13 pt `#27AE60`

Each panel: Rounded rect frame, W: 7.0", H: 8.0", fill `#1E2435`, radius 6.
Panel labels: Barlow Condensed ExtraBold 22 pt, centered.
Arrow connectors between panels: 3 pt `#3A4055`, right-pointing.

**Key parameters below diagram (Y: 13.0"):**
- `Typical: 5--10% H2SO4 | Ambient | 15--30 sec` JetBrains Mono 16 pt `#E8A020`

---

### ZONE 4 -- Substrate Activation Table

**Section label:** `ACTIVATION BY SUBSTRATE` -- Y: 14.7".

**BLOCK D -- Substrate Table**

Y: 15.3" to 20.0".

| Substrate | Acid | Concentration | Temp | Time | Notes |
|---|---|---|---|---|---|
| Copper / Brass | H2SO4 | 5--10% v/v | Ambient | 15--30 sec | Most common for tin |
| Steel | HCl or H2SO4 | HCl 10--20% or H2SO4 5--15% | Ambient | 15--60 sec | HCl preferred for heavy oxide |
| Nickel-plated | H2SO4 | 5% v/v | Ambient | 10--15 sec | Light touch -- protect Ni layer |
| Pre-tinned (rework) | H2SO4 | 5--10% | Ambient | 10--20 sec | Remove tarnish, not the tin |

Header: `#3A4055`. Alternating rows: `#1E2435` / `#252B3D`.

**Note below table:**
- `H2SO4 is the default activation acid for tin plating. HCl is acceptable for steel but introduces chloride -- keep it out of the tin bath.` Inter Medium 13 pt `#E8A020`

---

### ZONE 5 -- Over vs. Under Activation

**Section label:** `GET IT RIGHT -- OVER VS. UNDER` -- Y: 20.7".

**BLOCK E -- Two-Panel Comparison**

Y: 21.3" to 26.0".

**Left -- Under-Activation:**
- Rounded rect, X: 0.5", W: 11.0", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `UNDER-ACTIVATED` Barlow SemiBold 18 pt `#E05C5C`

Symptoms:
- `Oxide film remains on surface`
- `Tin plates over oxide -- poor adhesion`
- `Blistering on thermal cycling`
- `Solderability fails after aging`
- `Peel test failure`

Visual cue: `Looks OK wet -- fails in test` Inter Medium 13 pt `#E05C5C`

**Right -- Over-Activation:**
- Rounded rect, X: 12.0", W: 11.5", H: 4.5", fill `#1E2435`, left accent `#E8A020`
- Title: `OVER-ACTIVATED` Barlow SemiBold 18 pt `#E8A020`

Symptoms:
- `Base metal attacked -- surface roughened`
- `Copper/brass turns pink or matte`
- `Grainy, rough tin deposit`
- `Dimensional loss on precision parts`
- `Increased drag-in of dissolved metal`

Visual cue: `Visible etch on copper = too long or too strong` Inter Medium 13 pt `#E8A020`

**Center divider verdict:**
- `The window is narrow: 15--30 seconds in 5--10% sulfuric. Set a timer. Every time.` Inter Medium 14 pt `#27AE60`

---

### ZONE 6 -- Safety

**Section label:** `ACID SAFETY -- NON-NEGOTIABLE` -- Y: 26.7".

**BLOCK F -- Safety Cards**

Y: 27.3" to 32.0". Two large safety cards.

**Left -- Sulfuric Acid:**
- Rounded rect, X: 0.5", W: 11.0", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `SULFURIC ACID (H2SO4)` Barlow SemiBold 18 pt `#E05C5C`
- `Corrosive -- severe burns on contact`
- `Add acid to water, NEVER water to acid`
- `Exothermic reaction on dilution -- heats rapidly`
- `PPE: face shield, chemical gloves, acid apron`
- `Spill: neutralize with soda ash, flush with water`

**Right -- Hydrochloric Acid:**
- Rounded rect, X: 12.0", W: 11.5", H: 4.5", fill `#1E2435`, left accent `#E05C5C`
- Title: `HYDROCHLORIC ACID (HCl)` Barlow SemiBold 18 pt `#E05C5C`
- `Corrosive -- severe burns, strong fumes`
- `Fuming at room temperature -- ventilation mandatory`
- `PPE: face shield, chemical gloves, acid apron, respirator if unventilated`
- `Chloride contamination risk to tin bath`
- `Rinse thoroughly after HCl activation`

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Tin`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Tin -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-panel before/during/after hero is the most effective way to explain activation to a shop floor audience. Operators understand pictures of surfaces. The over vs. under comparison is critical because copper and brass etch fast -- the activation window is narrow and unforgiving. The chloride contamination warning (HCl in a tin bath) is an important cross-process note.

---

*Alaina -- Plating Posters Inc*
*Poster #114 -- Construction Workup v1.0*
*2026-04-26*
