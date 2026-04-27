---
Project: Plating Posters Inc
Poster Number: 316
Title: "Rinse -- PAA -- Pre-Anodize"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 5: PAA, Section 5.6)"
Technical Source: Pre-anodize rinse for PAA. DI water required. Fluoride dragover from HF desmut is especially damaging to PAA oxide growth. Chloride contamination causes pitting.
Process Scope: Rinse -- Pre-Anodize (Stage 5 of PAA sequence)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - Anodizing
  - PAA
  - Rinse
  - PreAnodize
  - ConstructionWorkup
  - ClusterAnodPAA
---

# Poster #316 -- Construction Workup
## Rinse -- PAA -- Pre-Anodize

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 5 of the PAA sequence. The most critical rinse in the entire PAA line. Any acid, fluoride, or dissolved metals dragged into the PAA anodize tank contaminate the electrolyte. Fluoride dragover from HF desmut is particularly destructive because even trace amounts attack the growing PAA oxide -- and the PAA oxide is only 0.5--1.5 um thick.

Hero visual: a DI rinse cascade with contamination threshold indicators.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **DI cascade rinse hero (Block B):** Triple-cascade rinse with DI water, conductivity indicators at each stage. Built with rectangles, lines, arrows.
2. **Contamination thresholds panel (Block D):** What contaminants damage the PAA bath and at what levels.
3. **Fluoride dragover callout (Block E):** Why fluoride is the #1 threat.
4. **Conductivity monitoring guide (Block F):** How to verify rinse quality.
5. **Downstream consequences (Block G):** What happens if contaminants reach the PAA tank.

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
  Stage 5 highlighted (Teal)
ZONE 3 -- DI CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINATION THRESHOLDS + FLUORIDE (14.5"--20.5" / ~6.0")
ZONE 5 -- CONDUCTIVITY MONITORING (20.5"--26.5" / ~6.0")
ZONE 6 -- DOWNSTREAM CONSEQUENCES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PAA Pre-Anodize -- Stage 5 of 7 -- THE CRITICAL RINSE` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The last line of defense before the PAA tank. DI water only. Fluoride and chloride are the enemies.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Desmutted surface with acid residue  -->  After: Contaminant-free surface ready for phosphoric acid anodize`

---

### ZONE 3 -- DI Cascade Rinse Hero

**Section label:** `THE CRITICAL PRE-ANODIZE RINSE` -- Y: 4.4".

**BLOCK B -- Triple-Cascade DI Rinse Diagram**

Y: 5.0" to 13.5".

**Three rinse tanks in sequence:**

*Tank 1 (first rinse -- most contaminated):*
- Rounded rect, X: 0.5", Y: 5.5", W: 7.0", H: 6.0"
- Fill: `#252B3D` at 80%
- Border: 2 pt `#C8D0D8`
- Label: `RINSE 1` Barlow SemiBold 14 pt `#F0EDE8` at 60%
- Conductivity indicator: `~300 uS/cm` JetBrains Mono 14 pt `#E8A020`

*Tank 2 (middle rinse):*
- Rounded rect, X: 8.5", Y: 5.5", W: 7.0", H: 6.0"
- Fill: `#252B3D` at 50%
- Border: 2 pt `#C8D0D8`
- Label: `RINSE 2` Barlow SemiBold 14 pt `#F0EDE8` at 60%
- Conductivity indicator: `~100 uS/cm` JetBrains Mono 14 pt `#2EC4B6`

*Tank 3 (final rinse -- cleanest):*
- Rounded rect, X: 16.5", Y: 5.5", W: 7.0", H: 6.0"
- Fill: `#252B3D` at 25%
- Border: 2 pt `#27AE60`
- Label: `RINSE 3 (FINAL)` Barlow SemiBold 14 pt `#27AE60`
- Conductivity indicator: `< 100 uS/cm TARGET` JetBrains Mono 14 pt `#27AE60`

**Counter-flow arrows:**
- Arrow from Tank 3 overflow to Tank 2: 3 pt `#2EC4B6`
- Arrow from Tank 2 overflow to Tank 1: 3 pt `#2EC4B6`
- Label: `COUNTER-FLOW: DI water enters Tank 3, cascades backward` Inter Regular 12 pt `#2EC4B6`

**DI water inlet:**
- Arrow into Tank 3 right side
- Label: `DI WATER IN (< 50 uS/cm)` JetBrains Mono 12 pt `#27AE60`

**Part movement arrows:**
- Arrows showing parts moving left-to-right through tanks
- Label: `PARTS MOVE: Desmut -> Rinse 1 -> Rinse 2 -> Rinse 3 -> PAA Tank` Inter Regular 12 pt `#E8A020`

**Bath parameter labels (below tanks, Y: 12.0"):**
- `Water quality: DI water REQUIRED (< 50 uS/cm input)` JetBrains Mono 14 pt `#27AE60`
- `Temperature: Ambient` JetBrains Mono 13 pt `#F0EDE8`
- `Time: 60--120 seconds minimum per stage` JetBrains Mono 13 pt `#F0EDE8`
- `Final rinse target: < 100 uS/cm` JetBrains Mono 14 pt `#E8A020`

**Bottom callout (Y: 13.0"):**
- `For aerospace PAA: triple cascade is standard practice. Double cascade is minimum.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Contamination Thresholds + Fluoride

**Section label:** `CONTAMINATION LIMITS IN THE PAA BATH` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Contamination Thresholds (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `WHAT MUST NOT REACH THE PAA TANK` Barlow SemiBold 18 pt `#E05C5C`

| Contaminant | Source | Effect on PAA |
|---|---|---|
| Fluoride (F-) | HF desmut dragover | Attacks growing oxide; destroys whisker structure |
| Chloride (Cl-) | Process water; cleaner residue | Pitting attack; > 25 ppm is damaging |
| Organic residue | Cleaning carryover | Blocks oxide growth; reduces bond strength |
| Dissolved metals | Desmut bath carryover | Contaminates PAA electrolyte; discoloration |
| Sulfate (SO4 2-) | Cross-contamination from Type II line | Changes pore morphology |

Data: Inter Regular 13 pt. Contaminant names: `#E05C5C`. Effects: `#F0EDE8`.

**Right -- Fluoride: The #1 Threat (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `FLUORIDE DRAGOVER` Barlow SemiBold 22 pt `#E05C5C`

Body (Inter Regular 14 pt `#F0EDE8`, line height 155%):

> If HNO3/HF desmut was used in Stage 4, fluoride residue on parts is the most dangerous contaminant for the PAA bath.
>
> Even trace fluoride:
> -- Attacks the growing aluminum oxide
> -- Dissolves the whisker/dendrite pore tips
> -- Reduces oxide thickness below spec minimum
> -- Degrades adhesive interlocking = bond failure
>
> The PAA oxide is only 0.5--1.5 um thick. There is no margin for fluoride damage.
>
> Triple cascade rinse with DI water is the only reliable defense.

Stat callout: `0 ppm fluoride tolerance in PAA bath` JetBrains Mono 18 pt `#E05C5C`

---

### ZONE 5 -- Conductivity Monitoring

**Section label:** `RINSE VERIFICATION BY CONDUCTIVITY` -- Y: 20.7".

**Full-width panel (Y: 21.3" to 26.3"):**
- Rounded rect, X: 0.5", W: 23.0", H: 4.8", fill `#1E2435`

**Three-column conductivity guide:**

*Column 1 -- Why Conductivity (X: 1.0", W: 7.0"):*
- Title: `WHY MEASURE?` Barlow SemiBold 16 pt `#2EC4B6`
- Body: `Conductivity is the fastest, cheapest way to verify rinse quality. High conductivity = dissolved ions = contamination risk. A $50 meter prevents a $5,000 rework.` Inter Regular 13 pt `#F0EDE8`

*Column 2 -- How to Read (X: 8.5", W: 7.0"):*
- Title: `HOW TO READ IT` Barlow SemiBold 16 pt `#E8A020`
- Body:
```
< 50 uS/cm: Excellent -- DI quality
50--100 uS/cm: Good -- acceptable for PAA
100--500 uS/cm: Marginal -- increase flow
> 500 uS/cm: FAIL -- do not proceed
```
JetBrains Mono 13 pt `#F0EDE8`.
- Thresholds color-coded: `#27AE60` / `#2EC4B6` / `#E8A020` / `#E05C5C`

*Column 3 -- When to Act (X: 16.0", W: 7.0"):*
- Title: `WHEN TO ACT` Barlow SemiBold 16 pt `#E05C5C`
- Body: `If final rinse conductivity won't come below 100 uS/cm:` Inter Regular 13 pt `#F0EDE8`
- Action items:
  - `Increase DI flow rate`
  - `Add a rinse stage`
  - `Check DI system output quality`
  - `Inspect for cross-contamination`
  Inter Regular 13 pt `#F0EDE8`

---

### ZONE 6 -- Downstream Consequences

**Section label:** `IF THIS RINSE FAILS` -- Y: 26.7".

**Three-card cascade (Y: 27.3" to 32.3"):**

| Step | Title | Detail | Color |
|---|---|---|---|
| 1 | CONTAMINANT ENTERS PAA BATH | Fluoride, chloride, or organics reach the phosphoric acid electrolyte. Bath chemistry shifts. | `#E8A020` |
| 2 | OXIDE STRUCTURE COMPROMISED | Whisker morphology damaged or absent. Pore structure non-uniform. Coating thickness below spec. | `#E05C5C` |
| 3 | BOND FAILURE | Adhesive cannot interlock with damaged oxide. Bond strength drops below 40 MPa. Structural joint fails in service. | `#E05C5C` |

Each card: Rounded rect W: 7.33", H: 4.0", fill `#1E2435`, top accent 4 pt in card color.
Arrows between cards: 3 pt `#3A4055`, pointing right.

Bottom summary:
- `This rinse is not optional. It is not "just water." It is the firewall between your desmut chemistry and your bonding surface.` Inter Medium 14 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- PAA -- Pre-Anodize`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM D3933; Boeing BAC 5555. Rinse parameters shown are typical values. DI water quality and cascade configuration vary by facility. Consult your process specification.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse PAA Pre-Anodize -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the most important rinse poster in the PAA cluster. The fluoride dragover callout is the centerpiece -- it is the non-obvious hazard that experienced operators may not fully appreciate. The conductivity guide gives them a concrete, measurable target (< 100 uS/cm) that they can act on immediately. The downstream consequences cascade connects this rinse to bond failure in three clear steps.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #316 -- Construction Workup v1.0*
*2026-04-26*
