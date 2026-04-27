---
Project: Plating Posters Inc
Poster Number: 280
Title: "Cleaning -- Type II"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.2)"
Technical Source: Industry-standard alkaline cleaning for sulfuric acid anodizing (Type II). Non-silicated inhibited alkaline cleaners for aluminum substrates.
Process Scope: Alkaline cleaning stage (Stage 1 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Cleaning
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #280 -- Construction Workup
## Cleaning -- Type II

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of 8. The cleaning stage sets the foundation for everything downstream. Residual organics cause skip anodizing -- bare spots where the oxide refuses to grow. The hero concept: silicate-free is non-negotiable. Silicated cleaners are invisible saboteurs that block oxide growth.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank schematic showing immersion soak cleaning with part rack, heater, agitation, and labeled contaminant types being removed.
2. **Operating parameters panel (Block D):** Detailed parameter card with ranges.
3. **Water-break test visual (Block E):** Two-panel visual -- pass (continuous film) vs. fail (beading water).
4. **Contaminant identification strip (Block F):** 4 cards showing common contaminant types and their downstream effects.
5. **Standard construction patterns throughout.**

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
ZONE 4 -- OPERATING PARAMETERS + CLEANER TYPES (14.5"--20.5" / ~6.0")
ZONE 5 -- WATER-BREAK TEST + FAILURE MODES (20.5"--26.5" / ~6.0")
ZONE 6 -- CONTAMINANT IDENTIFICATION (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Sulfuric Acid Anodizing (Type II) -- Stage 1 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Skip the prep. Ruin the finish. Every bare spot on an anodized part starts with a dirty surface.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received aluminum with oils, compounds, fingerprints  -->  After: Water-break-free surface ready for etch`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE CLEANING TANK` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (bath solution)
- Border: 3 pt `#C8D0D8`

**Part rack (center):**
- Vertical rect representing rack with parts, X: 9.0", Y: 6.0", W: 6.0", H: 5.5", fill `#C8D0D8` at 20%, border 2 pt `#2EC4B6`
- Label above: `ALUMINUM WORKPIECE` Barlow SemiBold 14 pt `#2EC4B6`

**Heater element (bottom of tank):**
- Horizontal line, X: 3.0", Y: 12.5", W: 18.0", stroke 3 pt `#E05C5C`
- Label: `IMMERSION HEATER -- 130--160 F (55--70 C)` JetBrains Mono 12 pt `#E05C5C`

**Agitation arrows (air or mechanical):**
- 4--6 upward arrows from bottom, stroke 2 pt `#2EC4B6`, dashed
- Label: `Air agitation (mild)` Inter Regular 12 pt `#2EC4B6`

**Bath parameter labels (inside tank, right side):**
- `Non-silicated alkaline cleaner` JetBrains Mono 14 pt `#2EC4B6`
- `30--60 g/L (4--8 oz/gal)` JetBrains Mono 14 pt `#F0EDE8`
- `pH 9--12` JetBrains Mono 14 pt `#F0EDE8`
- `130--160 F (55--70 C)` JetBrains Mono 14 pt `#E8A020`
- `2--10 min soak | 1--3 min spray` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Contaminant labels (floating off part surface, left side):**
- Small callout arrows pointing away from part surface:
- `Oils` / `Buffing compounds` / `Fingerprints` / `Drawing lubricants`
- Each: Inter Regular 12 pt `#E05C5C`

**Critical callout (bottom of zone):**
- Rounded rect, X: 0.5", Y: 13.3", W: 23.0", H: 0.8", fill `#E05C5C` at 15%, border 1 pt `#E05C5C`
- Text: `NEVER use silicated cleaners before anodizing. Silicate deposits are invisible but block oxide growth -- causing skip anodizing and poor adhesion.` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Operating Parameters + Cleaner Types

**Section label:** `OPERATING PARAMETERS` -- Y: 14.7".

**Two-column layout:**

**Left -- Parameter Card (X: 0.5", W: 11.0"):**

Rounded rect, H: 5.5", fill `#1E2435`, left accent `#2EC4B6` 0.06".

| Parameter | Value |
|---|---|
| Chemistry | Non-silicated alkaline cleaner (inhibited for Al) |
| Concentration | 30--60 g/L (4--8 oz/gal) |
| Temperature | 55--70 C (130--160 F) |
| Time (soak) | 2--10 minutes |
| Time (spray) | 1--3 minutes |
| Agitation | Mild air or mechanical |
| pH | 9--12 |

JetBrains Mono 13 pt for values, Inter Medium 13 pt for labels.

**Right -- Cleaner Type Guide (X: 12.0", W: 11.5"):**

Section label: `CLEANER SELECTION` Barlow Condensed ExtraBold 22 pt.

Three stacked cards (H: 1.5" each):

| Card | Title | Details |
|---|---|---|
| 1 | `ALKALINE SOAK (STANDARD)` | Most common for rack work. Non-silicated, inhibited. Works on all alloys. |
| 2 | `SPRAY CLEAN` | Faster cycle (1--3 min). Better for automated lines. Requires spray-compatible formulation. |
| 3 | `SOLVENT PRE-CLEAN` | For heavy buffing compound or grease. Solvent wipe or vapor degrease BEFORE alkaline soak. |

Each: fill `#1E2435`, left accent `#E8A020`, title Barlow SemiBold 16 pt `#E8A020`, details Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- Water-Break Test + Failure Modes

**Two-column layout (Y: 20.7" to 26.3"):**

**Left -- Water-Break Test (X: 0.5", W: 11.0"):**

Section label: `THE WATER-BREAK TEST` Barlow Condensed ExtraBold 22 pt.
Subtitle: `The simplest and most important QC check in the cleaning stage` Inter Regular 14 pt `#F0EDE8` at 60%.

Two side-by-side panels:

*PASS panel (X: 0.5", W: 5.0", H: 3.5"):*
- Fill `#27AE60` at 10%, border 1 pt `#27AE60`
- Header: `PASS` Barlow SemiBold 18 pt `#27AE60`
- Description: `Continuous water film covers entire surface -- no beading, no break-up for 30+ seconds`
- Label: `Clean surface -- proceed to etch` Inter Medium 13 pt `#27AE60`

*FAIL panel (X: 6.0", W: 5.0", H: 3.5"):*
- Fill `#E05C5C` at 10%, border 1 pt `#E05C5C`
- Header: `FAIL` Barlow SemiBold 18 pt `#E05C5C`
- Description: `Water beads, breaks up, or recedes from areas -- organic residue still present`
- Label: `Re-clean or extend soak time` Inter Medium 13 pt `#E05C5C`

**Right -- Failure Modes (X: 12.0", W: 11.5"):**

Section label: `WHAT GOES WRONG` Barlow Condensed ExtraBold 22 pt.

| Failure | Cause | Downstream Effect |
|---|---|---|
| Skip anodizing | Organic residue on surface | Bare spots -- no oxide growth at contaminated areas |
| Thin/uneven oxide | Partial organic film | Light/discolored patches visible after dyeing |
| Poor dye uptake | Silicate deposit from wrong cleaner | Invisible blockage -- most frustrating to diagnose |
| Streaking in etch | Cleaner not fully rinsed | Surfactant carryover accelerates etch unevenly |

Failure: Barlow SemiBold 14 pt `#E05C5C`. Cause: Inter Regular 12 pt `#F0EDE8`. Effect: Inter Regular 12 pt `#E8A020`.

---

### ZONE 6 -- Contaminant Identification

**Section label:** `KNOW YOUR CONTAMINANTS` -- Y: 26.7".

**BLOCK F -- Four Contaminant Cards**

Y: 27.3" to 32.3". Four cards in a row.

| Card | X | Contaminant | Source | Cleaning Approach |
|---|---|---|---|---|
| 1 | 0.5" | MACHINING OILS | CNC, lathe, mill operations | Standard alkaline soak -- 5+ min at 140+ F |
| 2 | 6.33" | BUFFING COMPOUND | Polishing/buffing wheels | Solvent pre-clean required before alkaline soak |
| 3 | 12.16" | FINGERPRINTS | Bare-hand handling | Standard alkaline soak; prevent with glove handling |
| 4 | 18.0" | DRAWING LUBRICANT | Stamping, deep draw forming | Extended soak (8--10 min) or emulsion pre-soak |

Each card: W: 5.5", H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt in `#E8A020`.
Contaminant: Barlow SemiBold 16 pt `#E8A020`. Source: Inter Regular 13 pt `#F0EDE8`. Approach: Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Type II`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; typical parameters for non-silicated alkaline cleaners on aluminum.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Type II -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The water-break test is the single most practical thing on this poster -- it costs nothing, requires no equipment, and catches 90% of cleaning failures. Make it visually prominent. The silicate warning should hit hard -- it is the #1 "silent killer" in anodizing cleaning. For aerospace context, BAC 5763 is the Boeing cleaning spec; include as a reference note only, not a full callout.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #280 -- Construction Workup v1.0*
*2026-04-26*
