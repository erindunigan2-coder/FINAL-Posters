---
Project: Plating Posters Inc
Poster Number: 281
Title: "Rinse -- Type II -- Pre-Etch"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Anodizing Clusters -- Watson Research Brief (Process 1, Section 1.3)"
Technical Source: Industry-standard rinsing practice between alkaline cleaning and caustic etch for sulfuric acid anodizing (Type II).
Process Scope: Pre-etch rinse stage (Stage 2 of 8) for Type II anodizing
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Anodizing
  - TypeII
  - Rinse
  - ConstructionWorkup
  - ClusterAnodize
---

# Poster #281 -- Construction Workup
## Rinse -- Type II -- Pre-Etch

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 8. The often-overlooked step. This rinse prevents alkaline cleaner chemistry from contaminating the etch tank and accelerating the etch rate uncontrollably. The hero concept: counter-flow cascade rinsing and the "dwell and drain" technique that reduces dragout by 50--80%.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse diagram hero (Block B):** Multi-stage counter-flow rinse schematic showing water flow direction, part travel direction, and dragout reduction.
2. **Operating parameters panel (Block D).**
3. **Dragout reduction techniques (Block E):** Practical tips for reducing chemical carryover.
4. **Failure modes strip (Block F).**

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
  Stage 2 highlighted (Teal)
ZONE 3 -- CASCADE RINSE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OPERATING PARAMETERS + WATER QUALITY (14.5"--20.5" / ~6.0")
ZONE 5 -- DRAGOUT REDUCTION TECHNIQUES (20.5"--26.5" / ~6.0")
ZONE 6 -- FAILURE MODES + RINSE EFFICIENCY (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Type II -- Pre-Etch -- Stage 2 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The cheapest step in the line and the easiest to get wrong. Good rinsing costs pennies. Bad rinsing costs the entire batch.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Part with alkaline cleaner film  -->  After: Clean surface free of cleaner chemistry`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `COUNTER-FLOW CASCADE RINSING` -- Y: 4.4".

**BLOCK B -- Cascade Rinse Schematic**

Y: 5.0" to 14.0".

**Three rinse tanks in sequence (left to right):**

| Tank | X | W | Label | Water Quality |
|---|---|---|---|---|
| Stage 1 (dirtiest) | 1.5" | 6.0" | `RINSE 1` | Highest contamination |
| Stage 2 | 8.5" | 6.0" | `RINSE 2` | Intermediate |
| Stage 3 (cleanest) | 15.5" | 6.0" | `RINSE 3 (FINAL)` | DI or cleanest city water |

Each tank: Rounded rect H: 6.0", fill `#252B3D`, border 2 pt `#C8D0D8`.

**Part travel arrows (above tanks):**
- Left to right, stroke 3 pt `#2EC4B6`, arrowhead filled
- Label: `PART TRAVEL -->` Barlow SemiBold 14 pt `#2EC4B6`

**Water flow arrows (between tanks, below):**
- Right to left (counter to part travel), stroke 3 pt `#E8A020`, arrowhead filled
- Label: `<-- FRESH WATER FLOW (counter-current)` Barlow SemiBold 14 pt `#E8A020`
- Fresh DI water input arrow entering Tank 3 from right
- Overflow from Tank 3 cascading into Tank 2, then Tank 2 into Tank 1
- Drain from Tank 1 (dirtiest) to waste

**Conductivity labels inside each tank:**
- Tank 1: `~2000+ uS/cm` JetBrains Mono 14 pt `#E05C5C`
- Tank 2: `~500--1000 uS/cm` JetBrains Mono 14 pt `#E8A020`
- Tank 3: `<500 uS/cm TARGET` JetBrains Mono 14 pt `#27AE60`

**Dwell-and-drain callout (left of Tank 1):**
- Rounded rect, X: 1.5", Y: 12.0", W: 6.0", H: 1.5", fill `#1E2435`, left accent `#27AE60`
- Text: `DWELL 10--15 sec over cleaner tank before entering rinse. Reduces dragout by 50--80%.` Inter Medium 13 pt `#27AE60`

**Bottom callout:**
- `Counter-flow rinsing is the most water-efficient method. Clean water enters the final tank; contaminated water drains from the first.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Operating Parameters + Water Quality

**Section label:** `RINSE PARAMETERS` -- Y: 14.7".

**Two-column layout:**

**Left -- Operating Parameters (X: 0.5", W: 11.0"):**

| Parameter | Value |
|---|---|
| Water quality | City water acceptable; DI preferred for critical work |
| Temperature | Ambient (room temperature) |
| Time | 30--60 seconds with agitation |
| Rinse method | Double cascade (counter-flow) preferred |
| Conductivity target | <500 uS/cm in final rinse |
| Agitation | Air or part movement |

**Right -- Water Quality Impact (X: 12.0", W: 11.5"):**

Section label: `WATER QUALITY MATTERS` Barlow Condensed ExtraBold 22 pt.

| Water Source | Conductivity | Suitability |
|---|---|---|
| DI water | <10 uS/cm | Ideal for all stages |
| RO water | 10--50 uS/cm | Excellent |
| Softened city | 100--300 uS/cm | Good for early rinses |
| Raw city water | 300--1000+ uS/cm | First rinse only |

Note: `Chloride in water is the #1 source of anodize tank contamination. DI water eliminates this risk.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 5 -- Dragout Reduction Techniques

**Section label:** `REDUCE DRAGOUT -- SAVE CHEMISTRY -- PROTECT DOWNSTREAM TANKS` -- Y: 20.7".

**Four technique cards in a row:**

| Card | Technique | Description | Impact |
|---|---|---|---|
| 1 | DWELL AND DRAIN | Hold rack over process tank 10--15 sec before rinse | 50--80% dragout reduction |
| 2 | SLOW WITHDRAWAL | Pull rack from tank slowly and at an angle | Allows drainage; reduces film thickness |
| 3 | SPRAY RINSE | Spray DI water over parts above the process tank | Recovers chemistry directly into process tank |
| 4 | AIR KNIFE | Blow excess solution off parts before rinse | Best for automated lines |

Each card: W: 5.5", H: 4.5", fill `#1E2435`, radius 6, top accent 4 pt `#2EC4B6`.
Technique: Barlow SemiBold 16 pt `#2EC4B6`. Description: Inter Regular 13 pt `#F0EDE8`. Impact: Inter Medium 13 pt `#27AE60`.

---

### ZONE 6 -- Failure Modes + Rinse Efficiency

**Two-column layout (Y: 26.7" to 32.3"):**

**Left -- Failure Modes (X: 0.5", W: 11.0"):**

| Failure | Cause | Effect |
|---|---|---|
| Streaking in etch | Cleaner not fully rinsed | Surfactant causes uneven etch rate |
| Accelerated etch | Alkaline dragover into etch | NaOH concentration creeps up; etch runs hot |
| Etch contamination | Surfactant buildup in etch bath | Foaming; surface defects on parts |

**Right -- Rinse Efficiency Principles (X: 12.0", W: 11.5"):**

Section label: `RINSE EFFICIENCY` Barlow Condensed ExtraBold 22 pt.

Key principles:
- `Single rinse: ~100:1 dilution ratio`
- `Double cascade: ~10,000:1 dilution ratio`
- `Triple cascade: ~1,000,000:1 dilution ratio`
- `Each additional cascade stage = 100x improvement in rinsing`

JetBrains Mono 14 pt `#27AE60` for ratios.

Bottom note: `Cascade rinsing achieves aerospace-grade cleanliness with minimal water consumption.` Inter Medium 13 pt `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Type II -- Pre-Etch`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; ASM Handbook Vol. 5; standard rinsing practice for anodizing process lines.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Type II Pre-Etch -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Rinsing is the most underappreciated step in any finishing line. This poster makes the case that proper rinsing is cheap insurance. The cascade diagram is the hero -- it should be immediately understandable at arm's length. The dilution ratio comparison (single vs. double vs. triple cascade) is the "aha moment" that justifies multi-stage rinsing. Keep the dwell-and-drain callout visually prominent -- it is the single easiest improvement any shop can make today.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #281 -- Construction Workup v1.0*
*2026-04-26*
