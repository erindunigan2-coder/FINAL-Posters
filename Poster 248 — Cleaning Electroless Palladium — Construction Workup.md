---
Project: Plating Posters Inc
Poster Number: 248
Title: "Cleaning -- Electroless Palladium"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters — Watson Research Brief (Process 5: Electroless Palladium)"
Process Scope: Alkaline soak clean / electroclean for electroless palladium (Stage 1 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessPalladium
  - Cleaning
  - ConstructionWorkup
  - Series2
  - ENEPIG
---

# Poster #248 -- Construction Workup
## Cleaning -- Electroless Palladium

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 1 of 8. The cleaning step for electroless palladium is identical in principle to all electroless processes -- remove oils, greases, oxides, and organic contaminants that would inhibit catalytic deposition. Skip plating from contamination is the number one defect in electroless operations. For ENEPIG lines, the cleaning is typically shared across the entire ENIG/ENEPIG sequence.

Hero visual: a cleaning tank cross-section showing the soak clean and optional electroclean stages.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning tank cross-section hero (Block B):** Tank with immersed workpiece, alkaline solution indicators, optional electroclean electrodes. Built with rectangles, lines, and labels.
2. **Cleaning parameters panel (Block D):** Soak clean and electroclean side-by-side.
3. **Substrate-specific notes callout (Block E):** Different substrates require different cleaning approaches.
4. **Defect grid (Block F):** 4 cleaning-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per Series Design Prompt.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING TANK HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- CLEANING PARAMETERS + ELECTROCLEAN (14.5"--20.5" / ~6.0")
ZONE 5 -- SUBSTRATE-SPECIFIC NOTES (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electroless Palladium -- Stage 1 of 8` -- 36 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Every electroless defect traces back to the clean. Skip the prep, skip the plate.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received substrate with oils, oxides, soils  -->  After: Water-break-free, catalytically active surface`

---

### ZONE 3 -- Cleaning Tank Hero

**Section label:** `THE ALKALINE SOAK CLEAN` -- Y: 4.4".

**BLOCK B -- Tank Cross-Section**

Y: 5.0" to 14.0".

**Tank body:**
- Rounded rect, X: 1.5", Y: 5.5", W: 21.0", H: 7.5"
- Fill: `#252B3D` (cleaning solution)
- Border: 3 pt `#C8D0D8`

**Workpiece (center):**
- Vertical rect, X: 10.5", Y: 6.5", W: 3.0", H: 5.0", fill `#2EC4B6` at 20%, border 2 pt `#2EC4B6`
- Label above: `WORKPIECE` Barlow SemiBold 14 pt `#2EC4B6`

**Solution labels (inside tank):**
Right side (X: 15.0", Y: 7.0"):
- `NaOH: 30--60 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Na2CO3: 15--30 g/L` JetBrains Mono 14 pt `#2EC4B6`
- `Surfactants: 1--5 mL/L` JetBrains Mono 14 pt `#F0EDE8`
- `Temp: 60--80 C (140--176 F)` JetBrains Mono 14 pt `#E8A020`

Left side (X: 2.5", Y: 7.0"):
- `Soak time: 3--10 min` JetBrains Mono 14 pt `#F0EDE8`
- `Agitation: Air or mechanical` JetBrains Mono 13 pt `#F0EDE8` at 70%

**Optional electroclean electrodes (dimmed overlay):**
- Two vertical rects flanking workpiece (X: 8.0" and 16.0"), H: 4.5", fill `#C8D0D8` at 30%, dashed border 1 pt `#C8D0D8`
- Label: `ELECTROCLEAN (OPTIONAL)` Inter Medium 12 pt `#C8D0D8`
- Sub-label: `Cathodic: 3--6 V, 30--60 sec (H2 scrub)` / `Anodic: 3--6 V, 15--30 sec (smut removal)` JetBrains Mono 11 pt `#F0EDE8` at 60%

**Bottom callout (Y: 13.0"):**
- `Water-break-free test: After rinsing, water should sheet uniformly across the entire surface with no beading or dry spots.` Inter Medium 14 pt `#2EC4B6`

---

### ZONE 4 -- Cleaning Parameters + Electroclean

**Section label:** `CLEANING METHODS -- SOAK vs. ELECTROCLEAN` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Alkaline Soak Clean (X: 0.5", W: 11.0"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#2EC4B6` 0.06"
- Title: `ALKALINE SOAK CLEAN` Barlow SemiBold 20 pt `#2EC4B6`

| Parameter | Value |
|---|---|
| NaOH | 30--60 g/L |
| Na2CO3 | 15--30 g/L |
| Surfactants | 1--5 mL/L (proprietary blends) |
| Temperature | 60--80 C (140--176 F) |
| Time | 3--10 minutes |
| Agitation | Air or mechanical |

**Right -- Electroclean (X: 12.0", W: 11.5"):**
- Rounded rect H: 4.8", fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `ELECTROCLEAN (OPTIONAL)` Barlow SemiBold 20 pt `#E8A020`

| Parameter | Cathodic | Anodic |
|---|---|---|
| Voltage | 3--6 V | 3--6 V |
| Time | 30--60 sec | 15--30 sec |
| Action | H2 gas scrubs surface | O2 removes smut |
| Caution | H absorption in high-strength steel | Preferred for >1000 MPa UTS |

Bottom note: `For critical work, cathodic followed by anodic electroclean provides the most thorough surface preparation.` Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Substrate-Specific Notes

**Section label:** `SUBSTRATE-SPECIFIC CLEANING NOTES` -- Y: 20.7".

**BLOCK E -- Four Substrate Cards (Y: 21.3" to 26.3")**

2x2 grid. Each card: Rounded rect W: 11.0", H: 2.3", fill `#1E2435`, radius 4.

| Position | Substrate | Accent | Notes |
|---|---|---|---|
| R1C1 | COPPER / PCB (ENEPIG) | `#27AE60` | Shared cleaner/conditioner for entire ENIG/ENEPIG line; removes drilling smear on PCB |
| R1C2 | STEEL / IRON | `#2EC4B6` | Standard alkaline soak; electroclean recommended for critical adhesion |
| R2C1 | ALUMINUM | `#E8A020` | Non-etch alkaline cleaner (pH <10.5); avoid surface attack; followed by zincate in EN step |
| R2C2 | CERAMICS / POLYMERS | `#E05C5C` | Chromic/sulfuric etch for ABS; permanganate desmear for PCB; silicate-free cleaners mandatory |

Interior: Substrate name in Barlow SemiBold 16 pt (accent color). Notes in Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 6 -- Defect Grid

**Section label:** `WHAT GOES WRONG -- CLEANING FAILURES` -- Y: 26.7".

**BLOCK F -- 2x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SKIP PLATING | `#E05C5C` | Residual oils or organic films | Extend soak time; increase temperature; check surfactant level |
| R1C2 | POOR ADHESION | `#E05C5C` | Surface oxides not fully removed | Add electroclean step; verify water-break-free |
| R2C1 | SILICATE POISONING | `#E8A020` | Silicate-containing cleaner residue | Switch to silicate-free cleaner; improve rinse |
| R2C2 | SURFACE ROUGHENING | `#E8A020` | Aggressive etch on aluminum | Use non-etch cleaner (pH <10.5) for Al substrates |

Each card: W: 11.0", H: 2.3", fill `#1E2435`, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard footer. Title: `Cleaning -- Electroless Palladium`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM standards; IPC-4556. Consult your process supplier for application-specific guidance.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Electroless Palladium -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Cleaning is the same story across all electroless processes: if you don't get this right, nothing else matters. The hero tank visual should be simpler than a plating tank -- no anodes, no rectifier. The electroclean electrodes are shown as an optional overlay (dimmed) since not all shops use electrocleaning for electroless palladium. The substrate-specific cards are important because electroless Pd is applied to wildly different substrates -- from PCB copper to porous ceramics -- and each requires different cleaning protocols.

---

*Alaina -- Poster #248 -- Construction Workup v1.0 -- 2026-04-26*
