---
Project: Plating Posters Inc
Poster Number: 402
Title: "Cleaning -- PVD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 1: PVD, Section 1.4)"
Technical Source: PVD pre-cleaning sequence -- the number one cause of coating failure is inadequate cleaning. Covers ultrasonic alkaline, solvent rinse, DI water, and drying.
Process Scope: PVD cleaning (Stage 2 of 10)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - PVD
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #402 -- Construction Workup
## Cleaning -- PVD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 10. The single most important stage in the entire PVD process. Watson's research brief states it directly: "#1 cause of PVD coating failure is poor cleaning." This poster drives that message home with a multi-step cleaning sequence, contamination sources, and a pass/fail visual inspection guide.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning sequence flowchart (Block B -- HERO):** Vertical 5-step flowchart showing the complete cleaning sequence with parameters at each step.
2. **Contamination source matrix (Block D):** What contaminants come from where and what they do to the coating.
3. **Pass/fail inspection panel (Block E):** Visual criteria for clean vs. contaminated parts.
4. **Rule card callout (Block C):** Big stat -- "#1 cause of PVD failure: CONTAMINATION."

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 17.0" / 23.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 2 highlighted (Teal -- cleaning)
ZONE 3 -- CLEANING SEQUENCE / HERO (4.2"--17.0" / ~12.8")
ZONE 4 -- CONTAMINATION SOURCES (17.0"--23.0" / ~6.0")
ZONE 5 -- PASS/FAIL INSPECTION (23.0"--28.5" / ~5.5")
ZONE 6 -- CLEANING TIPS + COMMON MISTAKES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `PVD -- Stage 2 of 10 -- The Foundation of Every Good Coating` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Skip the cleaning. Ruin the batch. One fingerprint can delaminate a $50,000 load of coated tooling.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 2 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts verified and approved (Stage 1) --> After: Spotless, dry, ready for fixturing`

---

### ZONE 3 -- Cleaning Sequence (HERO)

**Section label:** `THE 5-STEP PVD CLEANING SEQUENCE` -- Y: 4.4".

**Rule card (top-right corner of zone):**
- Rounded rect, X: 17.0", Y: 4.8", W: 6.5", H: 2.5", fill `#1E2435`, border 1 pt `#E05C5C`
- Big number: `#1` Barlow Condensed ExtraBold 78 pt `#E05C5C`
- Label: `CAUSE OF PVD FAILURE:` Inter Medium 14 pt `#F0EDE8`
- Sublabel: `CONTAMINATION` Barlow SemiBold 22 pt `#E05C5C`

**BLOCK B -- Vertical Flowchart (Y: 5.2" to 16.8")**

Five step cards stacked vertically with arrows between them. Each card spans X: 0.5" to 15.5" (W: 15.0"), H: 2.0".

| Step | Fill | Accent | Name | Parameters | Key Note |
|---|---|---|---|---|---|
| 1 | `#1E2435` | `#2EC4B6` left 0.06" | ULTRASONIC ALKALINE DEGREASE | 50-70 C, 5-15 min, alkaline detergent, ultrasonic agitation | Removes cutting oils, coolant residue, shop soils |
| 2 | `#1E2435` | `#2EC4B6` left 0.06" | DI WATER RINSE (MULTI-STAGE) | Ambient, flowing DI water, 2-3 stages, 1-2 min each | Removes alkaline residue; conductivity check on final rinse |
| 3 | `#1E2435` | `#E8A020` left 0.06" | SOLVENT CLEAN (ACETONE / IPA) | Ultrasonic, 5-10 min, fresh solvent | Removes residual organics that alkaline missed |
| 4 | `#1E2435` | `#2EC4B6` left 0.06" | FINAL DI RINSE | Spot-free grade DI, brief immersion | Last chance to remove particulate |
| 5 | `#1E2435` | `#E8A020` left 0.06" | DRYING | Hot air 60-80 C or vacuum dry; no water spots | Water spots = mineral deposits = coating defects |

Step number badge: Rounded rect 0.8" x 0.8", fill accent color. Number: Barlow Condensed ExtraBold 24 pt `#1A1F2E`.
Step name: Barlow SemiBold 20 pt `#F0EDE8`.
Parameters: JetBrains Mono Regular 13 pt `#F0EDE8`.
Key note: Inter Regular 13 pt accent color.

Arrows between steps: 3 pt `#3A4055`, filled arrowhead, downward.

---

### ZONE 4 -- Contamination Sources

**Section label:** `WHERE CONTAMINATION COMES FROM` -- Y: 17.2".

**BLOCK D -- Source Table (Y: 17.8" to 22.8")**

| Source | Contaminant | Effect on Coating | Prevention |
|---|---|---|---|
| Operator hands | Fingerprint oils | Delamination in fingerprint pattern | Nitrile gloves -- always |
| Machining | Cutting oil, coolant | Fish-eye defects, poor adhesion | Thorough alkaline clean |
| Storage | Rust, surface oxide | Weak adhesion, discoloration | Process promptly; no long storage after cleaning |
| Rinse water | Minerals, chlorides | Spot defects, corrosion under coating | DI water only; check conductivity |
| Shop air | Dust, oil mist | Particulate inclusions, haze | Clean parts in controlled area |
| Prior process | Grinding compound, EDM recast | Coating over contaminated layer | Verify surface condition at incoming |

Header: Barlow SemiBold 13 pt `#F0EDE8`, fill `#3A4055`.
Source: Inter Medium 13 pt `#F0EDE8`. Contaminant: JetBrains Mono 12 pt `#E8A020`. Effect: Inter Regular 12 pt `#E05C5C`. Prevention: Inter Medium 12 pt `#27AE60`.
Alternating rows `#1E2435` / `#252B3D`.

---

### ZONE 5 -- Pass/Fail Inspection

**Section label:** `VISUAL INSPECTION -- CLEAN ENOUGH FOR PVD?` -- Y: 23.2".

**BLOCK E -- Two-Panel Comparison (Y: 23.8" to 28.3")**

**Left -- PASS (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.3", fill `#1E2435`, left accent `#27AE60`
- Title: `PASS -- READY FOR FIXTURING` Barlow SemiBold 20 pt `#27AE60`

Criteria list (Inter Regular 14 pt `#F0EDE8`):
- `Water-break-free surface (water sheets off uniformly)`
- `No visible spots, stains, or residue under bright light`
- `No fingerprints (inspect under UV light if available)`
- `Completely dry -- no water droplets or damp areas`
- `No particulate visible at 10x magnification`

**Right -- FAIL (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `FAIL -- RETURN TO CLEANING` Barlow SemiBold 20 pt `#E05C5C`

Criteria list:
- `Water beads up on surface (indicates oil contamination)`
- `Visible stains, water marks, or rainbow discoloration`
- `Any fingerprints or smudges`
- `Residual moisture -- even a single droplet`
- `Dust or lint particles visible`

Bottom callout (full width):
- `When in doubt, re-clean. A 15-minute re-clean is cheaper than scrapping a failed batch.` Inter Medium 15 pt `#E8A020`

---

### ZONE 6 -- Cleaning Tips + Common Mistakes

**Section label:** `COMMON CLEANING MISTAKES` -- Y: 28.7".

**BLOCK F -- Four Mistake Cards (Y: 29.2" to 32.3")**

Four cards in a row. Each: W: 5.5", H: 2.8", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Mistake | Consequence | Fix |
|---|---|---|---|---|
| 1 | 0.5" | REUSING DIRTY SOLVENT | Redeposits contamination onto parts | Fresh solvent every batch; track solvent life |
| 2 | 6.33" | TOUCHING CLEANED PARTS | Fingerprint = delamination | Nitrile gloves from cleaning through loading |
| 3 | 12.16" | LONG DELAY AFTER CLEANING | Surface recontamination and oxide regrowth | Load into chamber within 2-4 hours of cleaning |
| 4 | 18.0" | COMPRESSED AIR DRYING | Oil from compressor deposits on surface | Use hot air or vacuum drying only; no shop air |

Mistake: Barlow SemiBold 15 pt `#E05C5C`. Consequence: Inter Regular 12 pt `#F0EDE8`. Fix: Inter Medium 12 pt `#27AE60`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- PVD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning PVD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is arguably the most important poster in the PVD cluster. The hero cleaning sequence must be crystal clear -- operators should be able to follow it step by step. The rule card with "#1 cause of failure: contamination" anchors the message. The pass/fail inspection panel gives concrete visual criteria. The common mistakes section targets the specific shortcuts that cause real-world failures.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #402 -- Construction Workup v1.0*
*2026-04-26*
