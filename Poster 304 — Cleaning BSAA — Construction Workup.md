---
Project: Plating Posters Inc
Poster Number: 304
Title: "Cleaning -- Boric-Sulfuric Acid Anodizing (BSAA)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 4, Sections 4.2--4.4)"
Process Scope: Alkaline cleaning for BSAA anodizing -- Stage 1 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - BSAA
  - TypeIC
  - Cleaning
  - ConstructionWorkup
  - ClusterAnodize04
---

# Poster #304 -- Construction Workup
## Cleaning -- Boric-Sulfuric Acid Anodizing (BSAA)

*Alaina -- Plating Posters Inc*
*v1.0 -- 2026-04-26*

Stage 1 of 8. Cleaning for BSAA follows the same requirements as Type I and Type II -- non-etch alkaline soak cleaner, water-break-free surface. No special pre-treatment requirements unique to BSAA. The key differentiator for this poster vs. the Type I cleaning poster (#296): no Cr(VI) safety warnings. The cleaning line is identical; the downstream hazard is absent. The concept hook: "Same clean. Same standard. But this time, no one needs a respirator in the next room."

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Same visual language as Posters 296 and 288.
2. **Contaminant impact panel (Block D):** How contamination affects the thin BSAA oxide.
3. **Water-break test callout (Block E):** Standard visual.
4. **Defect grid (Block F):** 6 cleaning-related failure modes.
5. **Chromate-free reminder strip (Block G):** Positive framing -- "Cr(VI)-free from this stage forward."

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
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CONTAMINANT IMPACT + WATER BREAK TEST (14.5"--20.5" / ~6.0")
ZONE 5 -- DEFECT DIAGNOSIS GRID (20.5"--26.5" / ~6.0")
ZONE 6 -- BSAA CLEANING RULES + Cr-FREE REMINDER (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Boric-Sulfuric Acid Anodizing (BSAA) -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Standard alkaline cleaning. Same water-break-free target. No special BSAA requirements -- but BSAA produces a thin oxide, so contamination tolerance is low.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Eight-stage strip. Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Stages labeled: `1. Clean` | `2. Rinse` | `3. Etch` | `4. Desmut` | `5. Rinse` | `6. BSAA Anodize` | `7. Rinse` | `8. Seal`

Below: `Before: As-received part with oils, soils, shop contamination  -->  After: Clean, water-break-free surface ready for etch`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE CLEANING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Same construction as Poster 296 (Type I Cleaning) and Poster 288 (Type III Cleaning).

Tank body, parts on rack, air agitation, heater, parameter labels:
- `Non-etch alkaline soak cleaner` JetBrains Mono 14 pt `#2EC4B6`
- `4--8 oz/gal (30--60 g/L)` JetBrains Mono 14 pt `#F0EDE8`
- `130--160 F (55--70 C)` JetBrains Mono 14 pt `#E8A020`
- `Soak: 3--10 min` JetBrains Mono 13 pt `#F0EDE8`
- `pH: 9--11` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Key restriction callout (bottom, Y: 13.0"):**
- Rounded rect, W: 20.0", H: 0.8", fill `#E05C5C` at 12%, border 1 pt `#E05C5C`
- Text: `NEVER use silicated cleaners before anodizing -- silicate deposits block oxide growth in ALL anodize types` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Contaminant Impact + Water Break Test

**Two-column layout (Y: 14.7" to 20.3"):**

**Left -- Contaminant Impact (X: 0.5", W: 13.0"):**

Section label: `WHY CLEANING MATTERS FOR BSAA` Barlow Condensed ExtraBold 22 pt `#F0EDE8`.

| Contaminant | Source | Effect on BSAA Coating |
|---|---|---|
| Silicates | Silicated cleaners | Bare spots -- no oxide growth at deposit sites |
| Oils/grease | Machining, fingerprints | Thin areas, poor paint adhesion (defeats BSAA purpose) |
| Chlorides | Tap water, cleaner residue | Pitting potential in acidic anodize bath |
| Buffing compound | Mechanical polishing | Embedded particles, non-uniform oxide |
| Drawing lubricant | Forming operations | Heavy organic load, requires solvent pre-clean |

Header: Barlow SemiBold 12 pt `#F0EDE8` on `#3A4055`. Data: Inter Regular 12 pt, alternating rows.

Below: `BSAA produces a THIN oxide (comparable to Type I). Contamination that Type II tolerates may cause BSAA failure.` Inter Medium 13 pt `#E8A020`.

**Right -- Water Break Test (X: 14.0", W: 9.5"):**

Standard water-break test visual (PASS/FAIL panels) per Poster 296.

---

### ZONE 5 -- Defect Diagnosis Grid

**Section label:** `WHAT GOES WRONG -- 6 CLEANING FAILURES` -- Y: 20.7".

**BLOCK F -- 3x2 Grid**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | BARE SPOTS | `#E05C5C` | Organic residue or silicate deposit | Re-clean; verify non-silicated cleaner |
| R1C2 | POOR PAINT ADHESION | `#E05C5C` | Residual contamination under thin oxide | Extend soak time; improve rinsing |
| R1C3 | STREAKING | `#E8A020` | Inadequate rinsing after clean | Improve cascade rinse; check water quality |
| R2C1 | THIN OXIDE AREAS | `#E8A020` | Partial organic film inhibiting oxide growth | Re-clean; water-break test before proceeding |
| R2C2 | UNEVEN APPEARANCE | `#2EC4B6` | Non-uniform soil removal | Improve agitation; verify cleaner concentration |
| R2C3 | BLISTERING AFTER PAINT | `#E05C5C` | Trapped moisture/contamination under oxide and primer | Thorough drying; verify cleaning effectiveness |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 6 -- BSAA Cleaning Rules + Cr-Free Reminder

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- BSAA Cleaning Rules (X: 0.5", W: 11.0"):**

Section label: `BSAA CLEANING -- THE RULES` Barlow Condensed ExtraBold 22 pt.

Callout box, fill `#1E2435`, left accent `#E8A020`:
- `1. Same non-etch alkaline cleaner as Type I and Type II` Inter Medium 14 pt `#F0EDE8`
- `2. No silicated cleaners -- ever` Inter Medium 14 pt `#F0EDE8`
- `3. No special BSAA-specific cleaning requirements` Inter Medium 14 pt `#F0EDE8`
- `4. Water-break-free test is MANDATORY` Inter Regular 13 pt `#F0EDE8` at 80%
- `5. Thin oxide = low tolerance for residual contamination` Inter Regular 13 pt `#E8A020`
- `6. If parts were machined with heavy coolant: solvent pre-clean recommended` Inter Regular 13 pt `#F0EDE8` at 80%

**Right -- Cr(VI)-Free Reminder (X: 12.0", W: 11.5"):**

Callout box, fill `#27AE60` at 10%, border 1 pt `#27AE60`:

Title: `Cr(VI)-FREE FROM START TO FINISH` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `BSAA is a fully chromate-free process.`
- `No Cr(VI) in the cleaning stage.`
- `No Cr(VI) in the desmut stage.`
- `No Cr(VI) in the anodize bath.`
- `No Cr(VI) in the seal.`
- ``
- `This means:` Inter Medium 13 pt `#27AE60`
- `-- No hexavalent chromium PPE requirements`
- `-- No Cr(VI) air monitoring`
- `-- No D007 hazardous waste sludge`
- `-- No medical surveillance program (for Cr(VI))`
- ``
- `Standard acid-handling PPE still required for all stages.` Inter Regular 12 pt `#F0EDE8` at 60%

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Boric-Sulfuric Acid Anodizing (BSAA)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Parameters shown are typical industry values. Cleaning procedures are the same as for conventional anodizing. Consult your process supplier and applicable spec.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning BSAA -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is intentionally similar to the Type I cleaning poster (#296) in structure, but the tone is fundamentally different. The Type I poster carries a Cr(VI) safety warning. This poster carries a Cr(VI)-FREE celebration. Same cleaning chemistry, different downstream context. The Emerald-tinted Cr(VI)-free callout in Zone 6 is the visual counterpart to the Coral-tinted Cr(VI) warning on Poster 296. When hung side by side, the contrast tells the story of the industry transition from chromic acid to BSAA.

---

*Alaina -- Plating Posters Inc*
*Poster #304 -- Construction Workup v1.0*
*2026-04-26*
