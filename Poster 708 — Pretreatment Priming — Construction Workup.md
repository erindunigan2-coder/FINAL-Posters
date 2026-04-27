---
Project: Plating Posters Inc
Poster Number: 708
Title: "Pretreatment -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Pretreatment requirements for industrial primers. The key insight: for zinc-rich primers on steel, the blast profile IS the pretreatment -- adding a conversion coating defeats the galvanic mechanism. Epoxy primers optionally benefit from iron phosphate. Aerospace primers REQUIRE conversion coating or anodize on aluminum.
Process Scope: Pretreatment for industrial priming -- Stage 4 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - IndustrialPriming
  - Pretreatment
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #708 -- Construction Workup
## Pretreatment -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. This poster teaches the most counterintuitive lesson in the priming cluster: for zinc-rich primers, the best pretreatment is NO pretreatment. A phosphate conversion coating under IOZ insulates the zinc from the steel and defeats the galvanic protection mechanism. The blast profile alone provides both adhesion and electrical contact.

Hero visual: a three-pathway decision diagram showing which pretreatment to use (or not use) based on primer type and substrate.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-pathway decision hero (Block B):** Three vertical paths from "Primer Type?" branch point: IOZ/OZ on Steel -> No pretreatment; Epoxy on Steel -> Optional; Aerospace on Aluminum -> Required. Built with rectangles and branching arrows.
2. **"Why NO pretreatment for IOZ" deep-dive (Block D):** Galvanic circuit explanation.
3. **Aerospace pretreatment table (Block E):** Conversion coating and anodize options.
4. **Common mistake callout (Block F):** Phosphate under IOZ = failure.

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
  Stage 4 highlighted (Amber)
ZONE 3 -- THREE-PATHWAY DECISION HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- WHY NO PRETREATMENT FOR IOZ (15.0"--21.0" / ~6.0")
ZONE 5 -- AEROSPACE PRETREATMENT TABLE (21.0"--27.0" / ~6.0")
ZONE 6 -- COMMON MISTAKES + STANDARDS (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 4 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Sometimes the best pretreatment is no pretreatment at all. Know your primer, know your substrate -- the answer changes.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Blast-cleaned substrate  -->  After: Surface ready for primer application`

---

### ZONE 3 -- Three-Pathway Decision Hero

**Section label:** `PRETREATMENT DEPENDS ON PRIMER TYPE AND SUBSTRATE` -- Y: 4.4".

**BLOCK B -- Decision Flowchart (Y: 5.0" to 14.5")**

**Decision node (top center):**
- Rounded rect, X: 7.5", Y: 5.0", W: 9.0", H: 1.2", fill `#E8A020` at 25%, border 2 pt `#E8A020`
- Text: `WHAT PRIMER AND SUBSTRATE?` Barlow SemiBold 20 pt `#E8A020`

Three arrows branch down to three pathway columns:

**Path 1 -- IOZ/OZ on Steel (X: 0.5", Y: 7.0", W: 7.0", H: 7.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `ZINC-RICH ON STEEL` Barlow SemiBold 20 pt `#27AE60`
- Big text: `NO PRETREATMENT` Barlow Condensed ExtraBold 28 pt `#27AE60`
- Content:
  - `The blast profile IS the pretreatment`
  - `Zinc must contact steel directly for galvanic protection`
  - `Adding phosphate = adding an insulator = defeating the primer`
  - `SSPC-SP10 or SP5 blast provides:`
  - `  -- Anchor profile for adhesion`
  - `  -- Clean metal for galvanic circuit`
  - `  -- Surface energy for wetting`
- Inter Regular 13 pt `#F0EDE8`
- Bottom badge: `BLAST PROFILE = PRETREATMENT` Barlow SemiBold 14 pt `#27AE60` on `#27AE60` at 15% fill

**Path 2 -- Epoxy on Steel (X: 8.5", Y: 7.0", W: 7.0", H: 7.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `EPOXY ON STEEL` Barlow SemiBold 20 pt `#E8A020`
- Big text: `OPTIONAL` Barlow Condensed ExtraBold 28 pt `#E8A020`
- Content:
  - `Blast-cleaned steel is acceptable for most epoxy primers`
  - `Optional: iron phosphate wash primer for additional adhesion`
  - `Optional: wash primer (vinyl butyral + phosphoric acid) for spot repair`
  - `SSPC-SP6 minimum for new steel`
  - `SSPC-SP3 for maintenance/repair`
- Inter Regular 13 pt `#F0EDE8`
- Bottom badge: `BLAST ALONE IS USUALLY SUFFICIENT` Barlow SemiBold 14 pt `#E8A020` on `#E8A020` at 15% fill

**Path 3 -- Aerospace on Aluminum (X: 16.5", Y: 7.0", W: 7.0", H: 7.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `AEROSPACE ON ALUMINUM` Barlow SemiBold 20 pt `#2EC4B6`
- Big text: `REQUIRED` Barlow Condensed ExtraBold 28 pt `#2EC4B6`
- Content:
  - `Conversion coating or anodize is MANDATORY`
  - `Chromate: MIL-DTL-5541 (Type I hex, Type II tri)`
  - `Anodize: MIL-PRF-8625 Type I (chromic) or IIB (thin sulfuric)`
  - `Non-chrome: Ti/Zr sol-gel or TCP`
  - `Prime within 24 hr of conversion coating`
- Inter Regular 13 pt `#F0EDE8`
- Bottom badge: `CONVERSION COATING = MANDATORY` Barlow SemiBold 14 pt `#2EC4B6` on `#2EC4B6` at 15% fill

---

### ZONE 4 -- Why No Pretreatment for IOZ

**Section label:** `THE GALVANIC CIRCUIT -- WHY PHOSPHATE DEFEATS IOZ` -- Y: 15.2".

**Full-width deep-dive panel (Y: 15.8" to 20.8"):**

Two side-by-side comparison panels:

**Left -- CORRECT (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `CORRECT: Zinc on Bare Steel` Barlow SemiBold 18 pt `#27AE60`
- Diagram description: Layered rectangles showing Steel -> Zinc Particles (direct contact) -> Primer Film
- `Zinc particles touch steel directly`
- `Galvanic circuit complete`
- `When scratched: zinc corrodes sacrificially`
- `Steel is cathodically protected`
- Inter Regular 13 pt `#F0EDE8`

**Right -- WRONG (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `WRONG: Zinc on Phosphate on Steel` Barlow SemiBold 18 pt `#E05C5C`
- Diagram description: Layered rectangles showing Steel -> Phosphate Layer (insulator) -> Zinc Particles -> Primer Film
- `Phosphate layer insulates zinc from steel`
- `Galvanic circuit BROKEN`
- `When scratched: zinc cannot protect steel`
- `Expensive primer providing zero galvanic benefit`
- Inter Regular 13 pt `#F0EDE8`

Verdict banner (full width, Y: 20.3"):
- Pill-shaped, fill `#E8A020` at 20%, border 1 pt `#E8A020`, radius 999
- Text: `Phosphate under IOZ = paying for galvanic protection you are not getting` Inter Medium 15 pt `#E8A020`

---

### ZONE 5 -- Aerospace Pretreatment Table

**Section label:** `AEROSPACE PRETREATMENT OPTIONS` -- Y: 21.2".

**BLOCK E -- Table (Y: 21.8" to 26.8")**

| Pretreatment | Substrate | Specification | Coating Weight | Status |
|---|---|---|---|---|
| Hex chromate conversion | Aluminum | MIL-DTL-5541 Type I | 40--150 mg/ft2 | Legacy -- RoHS restricted |
| Tri chromate conversion (TCP) | Aluminum | MIL-DTL-5541 Type II | Lower than hex | Gaining approval |
| Chromic acid anodize | Aluminum | MIL-PRF-8625 Type I | 0.05--0.15 mils | Declining -- Cr6+ phase-out |
| Thin sulfuric anodize | Aluminum | MIL-PRF-8625 Type IIB | 0.05--0.15 mils | Replacing Type I |
| Ti/Zr sol-gel | Aluminum | Boeing spec (AC-131) | Nanoscale | Approved on select programs |
| Zn-Ni plate + chromate | Steel (aero) | Per OEM spec | 0.3--0.8 mils | Replacing cadmium plate |

Header: `#3A4055`. Alternating rows. Data: Inter Regular 12 pt. Status column uses color coding: Legacy `#E05C5C`, Gaining `#E8A020`, Approved `#27AE60`.

Note: `Aerospace pretreatment is always specification-driven. The OEM or prime contractor dictates the process. Verify current revision before starting.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 6 -- Common Mistakes + Standards

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Common Mistakes (X: 0.5", W: 11.0"):**

Section label: `PRETREATMENT MISTAKES` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Mistake | Consequence |
|---|---|
| Phosphate under zinc-rich primer | Insulates zinc; defeats galvanic protection |
| Skip conversion coating on aerospace Al | Primer adhesion failure; spec non-compliance |
| Use expired conversion coating bath | Inadequate coating weight; corrosion failure |
| Apply IOZ to oxidized (unblasted) steel | No galvanic circuit; primer is just expensive paint |

Each: small card, fill `#1E2435`, left accent `#E05C5C`.

**Right -- Key Standards (X: 12.0", W: 11.5"):**

Section label: `STANDARDS REFERENCE` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| Standard | Description |
|---|---|
| SSPC-PS 12.01 | Guide for Selecting Zinc-Rich Primers |
| SSPC-SP10 / SP5 | Near-White / White Metal Blast |
| MIL-DTL-5541 | Chemical Conversion on Aluminum |
| MIL-PRF-8625 | Anodic Coatings on Aluminum |
| ASTM D4417 | Blast Profile Measurement |
| ISO 12944 | Corrosion Protection by Paint Systems |

Data: JetBrains Mono 12 pt `#F0EDE8`. Standard codes: `#2EC4B6`.

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC-PS 12.01; MIL specs; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster delivers the single most counterintuitive lesson in industrial priming: the best pretreatment for zinc-rich primers is no pretreatment. The three-pathway decision diagram makes the logic unavoidable -- you cannot miss that zinc-rich on steel = no conversion coating. The galvanic circuit comparison (correct vs. wrong) is the money shot. The aerospace section ensures the poster does not mislead people who prime aluminum -- for them, conversion coating is mandatory.

---

*Alaina -- Poster #708 -- Construction Workup v1.0 -- 2026-04-26*
