---
Project: Plating Posters Inc
Poster Number: 202
Title: "Activation -- Black Oxide"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Acid pickle / activation stage for hot alkaline black oxide on steel (Stage 3 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - BlackOxide
  - Activation
  - ConstructionWorkup
  - Series2
  - ClusterCC07
---

# Poster #202 -- Construction Workup
## Activation -- Black Oxide

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. The acid pickle removes rust, mill scale, and the passive film that naturally forms on steel. This exposes fresh, active iron -- the substrate the black oxide bath needs to form uniform magnetite. Over-pickling is the main risk: too much metal removal roughens the surface and produces a matte instead of lustrous finish.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Acid pickle tank hero (Block B):** Tank with parts submerged in acid, hydrogen bubble evolution, rust/scale dissolution arrows.
2. **Three-acid comparison (Block D):** HCl vs. H2SO4 vs. H3PO4 side-by-side.
3. **Over-pickle warning (Block E):** Visual showing surface roughening from excessive pickling.
4. **H-embrittlement callout (Block F):** Safety and process note for high-strength steels.

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
ZONE 3 -- ACID PICKLE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- THREE-ACID COMPARISON (14.5"--20.5" / ~6.0")
ZONE 5 -- OVER-PICKLE + SURFACE EFFECTS (20.5"--26.5" / ~6.0")
ZONE 6 -- H-EMBRITTLEMENT + SAFETY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ACTIVATION` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Black Oxide -- Acid Pickle -- Stage 3 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Strip the rust. Remove the scale. Expose fresh iron for uniform magnetite formation. But do not over-pickle.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Clean steel with surface oxide/rust --> After: Active, bare iron ready for blackening`

---

### ZONE 3 -- Acid Pickle Hero

**Section label:** `ACID PICKLE -- ACTIVATING THE STEEL SURFACE` -- Y: 4.4".

**BLOCK B -- Pickle Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.0"
- Fill: `#252B3D` (acid solution)
- Border: 3 pt `#E8A020`

**Parts submerged (center):**
- 3 rectangular parts, fill `#3A4055`, border 1 pt `#C8D0D8`
- Small bubble circles rising from parts (H2 evolution), fill `#F0EDE8` at 20%
- Rust/scale flakes falling from parts (small irregular shapes dissolving), fill `#E05C5C` at 30%

**Labels inside tank:**

Right side (X: 15.0"):
- `Fe + 2HCl --> FeCl2 + H2` JetBrains Mono 14 pt `#E8A020`
- `Iron dissolves, hydrogen evolves` Inter Regular 12 pt `#F0EDE8` at 60%
- `Rust + scale dissolve in acid` Inter Regular 12 pt `#F0EDE8` at 60%

Left side (X: 2.0"):
- `ACID PICKLE` Barlow SemiBold 16 pt `#E8A020`
- `Removes:` Inter Medium 13 pt `#F0EDE8`
- `- Rust (Fe2O3)` Inter Regular 13 pt `#F0EDE8`
- `- Mill scale (Fe3O4)` Inter Regular 13 pt `#F0EDE8`
- `- Passive oxide film` Inter Regular 13 pt `#F0EDE8`
- `- Heat tint / discoloration` Inter Regular 13 pt `#F0EDE8`

**Bottom callout (Y: 13.0"):**
- `HCl is the most common pickle acid for black oxide -- fast, ambient temperature, excellent activation.` Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Three-Acid Comparison

**Section label:** `CHOOSING YOUR PICKLE ACID` -- Y: 14.7".

**Three side-by-side callout boxes (Y: 15.3" to 20.3"):**

| Component | X | W | Accent | Title |
|---|---|---|---|---|
| Hydrochloric Acid | 0.5" | 7.33" | `#27AE60` | HCl (MURIATIC) |
| Sulfuric Acid | 8.0" | 7.33" | `#E8A020` | H2SO4 |
| Phosphoric Acid | 15.5" | 8.0" | `#2EC4B6` | H3PO4 |

Each box: Rounded rect H: 4.8", fill `#1E2435`, left accent 0.06".

*HCl box:*
- `20--50% by volume` JetBrains Mono 16 pt `#27AE60`
- `Temperature: Ambient`
- `Time: 2--10 min`
- `Speed: Fast`
- `Best for: General production; most common for black oxide`
- `Note: Generates HCl fumes -- ventilation required`
- Bottom highlight: `First choice for black oxide pre-pickling` `#27AE60`

*H2SO4 box:*
- `10--25% by volume` JetBrains Mono 16 pt `#E8A020`
- `Temperature: 120--160 F (49--71 C)`
- `Time: 5--15 min`
- `Speed: Moderate (needs heat)`
- `Best for: Heavy scale removal; batch processing`
- `Note: Less fuming than HCl; requires heating`
- Bottom highlight: `Better for heavy scale; slower but more controllable` `#E8A020`

*H3PO4 box:*
- `10--25% by volume` JetBrains Mono 16 pt `#2EC4B6`
- `Temperature: Ambient to 140 F`
- `Time: 5--15 min`
- `Speed: Slowest`
- `Best for: Precision parts; leaves light phosphate film`
- `Note: Mildest acid; least risk of over-pickling`
- Bottom highlight: `Gentlest option -- residual phosphate can aid oil retention` `#2EC4B6`

---

### ZONE 5 -- Over-Pickle + Surface Effects

**Section label:** `THE OVER-PICKLE PROBLEM` -- Y: 20.7".

**Two-panel comparison (Y: 21.3" to 26.3"):**

**Left -- Proper Pickle (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#27AE60`
- Title: `PROPERLY PICKLED` Barlow SemiBold 18 pt `#27AE60`
- Surface illustration: Smooth line representing even surface
- `Surface: smooth, uniformly active`
- `Oxide result: lustrous, deep blue-black`
- `Time in acid: just enough to remove oxide/scale`
- `Dimensional change: minimal`

**Right -- Over-Pickled (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `OVER-PICKLED` Barlow SemiBold 18 pt `#E05C5C`
- Surface illustration: Jagged/rough line representing pitted surface
- `Surface: rough, pitted, etched grain boundaries`
- `Oxide result: matte, non-lustrous, pitted black`
- `Too much time or too strong acid`
- `Dimensional change: measurable metal loss`

Bottom callout spanning full width:
- `The goal is ACTIVATION, not excavation. Remove the oxide film; leave the metal intact.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- H-Embrittlement + Safety

**Section label:** `HYDROGEN EMBRITTLEMENT + SAFETY` -- Y: 26.7".

**Two-column layout (Y: 27.3" to 32.3"):**

**Left -- Hydrogen Embrittlement (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C`
- Title: `H-EMBRITTLEMENT WARNING` Barlow SemiBold 18 pt `#E05C5C`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
Acid pickling generates hydrogen at
the steel surface. Hydrogen atoms can
diffuse into high-strength steel and
cause brittle fracture.

AFFECTED: Steel > 40 HRC (approx.)

BAKE: 375 F (191 C) for 4+ hours
within 4 hours of pickling

REFERENCE: ASTM B633 / ASTM F519

Use inhibited acids to reduce H2
absorption when processing hardened
steel parts.
```

**Right -- Safety (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E8A020`
- Title: `ACID PICKLE SAFETY` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 160%):
```
HCl fumes are corrosive and irritating
-- adequate ventilation is mandatory.

H2SO4 hot baths generate acid mist.

PPE: acid-resistant gloves, face shield,
chemical apron, safety glasses.

Ventilation: slot exhaust or push-pull
at tank lip.

Neutralization: sodium bicarbonate (soda
ash) for spills.

NEVER add water to concentrated acid --
add acid to water.
```

---

### ZONE 7 -- Footer

Standard. Title: `Activation -- Black Oxide`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Activation Black Oxide -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-acid comparison is the analytical core of this poster -- shops often default to whatever acid they have on hand without understanding the tradeoffs. HCl is first choice for a reason (fast, ambient, great activation), but H3PO4 deserves mention for precision work. The over-pickle section is visually impactful: smooth line vs. jagged line tells the story instantly. The H-embrittlement callout is a safety-critical detail that separates this poster from a generic "acid pickle" reference.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #202 -- Construction Workup v1.0*
*2026-04-26*
