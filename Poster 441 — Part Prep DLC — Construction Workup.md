---
Project: Plating Posters Inc
Poster Number: 441
Title: "Part Prep -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Section 5.4)"
Process Scope: Substrate preparation and surface requirements for DLC coating
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - PartPrep
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #441 -- Construction Workup
## Part Prep -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

DLC does not smooth rough surfaces -- it replicates substrate topography with atomic fidelity. This poster hammers that single message home. Surface finish, dimensional verification, and masking must all be completed BEFORE the part enters the coating chamber. The poster also covers substrate compatibility (steel, aluminum, titanium, carbide, ceramics) and the temperature constraint that makes DLC attractive for hardened steels.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Surface replication hero (Block B):** A side-by-side visual concept showing rough substrate = rough DLC vs. polished substrate = smooth DLC. Built with rectangles and text -- conceptual, not photographic.
2. **Substrate compatibility matrix (Block D):** Table of common substrates with DLC compatibility notes.
3. **Surface finish targets (Block E):** Ra targets by application type.
4. **Pre-coating checklist (Block F):** Step-by-step checklist for the operator.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SURFACE REPLICATION HERO (2.9"--14.5" / ~11.6")
  Block B: Surface replication concept + key message
  Block C: Temperature advantage callout
ZONE 3 -- SUBSTRATE COMPATIBILITY (14.5"--20.5" / ~6.0")
  Block D: Substrate matrix
ZONE 4 -- SURFACE FINISH TARGETS (20.5"--26.5" / ~6.0")
  Block E: Ra targets by application
ZONE 5 -- PRE-COATING CHECKLIST (26.5"--32.5" / ~6.0")
  Block F: Operator checklist
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `PART PREP` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Substrate Requirements` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `DLC replicates your surface with atomic fidelity. A rough substrate gives you a rough coating. Polish first -- or live with the result.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Surface Replication Hero

**Section label:** `DLC COPIES YOUR SURFACE -- NO EXCEPTIONS` -- Y: 3.1".

**BLOCK B -- Replication Concept**

Y: 3.8" to 12.0".

**Two side-by-side panels:**

*Left panel -- "BAD: Rough Substrate" (X: 0.5", W: 11.0", H: 7.5"):*
- Rounded rect, fill `#1E2435`, left accent 0.06" `#E05C5C`
- Title: `ROUGH SUBSTRATE` -- Barlow SemiBold, 22 pt, `#E05C5C`
- Conceptual representation: Jagged horizontal line (irregular zigzag stroke, 3 pt `#C8D0D8`) labeled `Substrate surface Ra > 0.2 um`
- Below: Parallel jagged line offset upward, 2 pt `#E05C5C`, labeled `DLC coating follows every peak and valley`
- Result callout: `RESULT: High friction defeats the purpose of DLC` -- Inter Medium, 16 pt, `#E05C5C`
- Parameter: `Friction: 0.15--0.25 (negates DLC benefit)` -- JetBrains Mono 14 pt `#E05C5C`

*Right panel -- "GOOD: Polished Substrate" (X: 12.0", W: 11.5", H: 7.5"):*
- Rounded rect, fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `POLISHED SUBSTRATE` -- Barlow SemiBold, 22 pt, `#27AE60`
- Conceptual representation: Smooth horizontal line (straight stroke, 3 pt `#C8D0D8`) labeled `Substrate surface Ra < 0.05 um`
- Below: Parallel smooth line offset upward, 2 pt `#27AE60`, labeled `DLC coating: smooth, uniform`
- Result callout: `RESULT: Ultra-low friction as intended` -- Inter Medium, 16 pt, `#27AE60`
- Parameter: `Friction: 0.05--0.10 (DLC at its best)` -- JetBrains Mono 14 pt `#27AE60`

**BLOCK C -- Temperature Advantage Callout**

Y: 12.3" to 14.3". Full width.

- Rounded rect, X: 0.5", W: 23.0", H: 1.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Title: `TEMPERATURE ADVANTAGE` -- Barlow SemiBold, 18 pt, `#27AE60`
- Text: `DLC deposits at < 200 C -- hardened tool steels retain their temper. PVD nitrides (TiN, CrN) require 300--500 C and risk softening heat-treated substrates. DLC coats what PVD cannot.` -- Inter Regular, 14 pt, `#F0EDE8`

---

### ZONE 3 -- Substrate Compatibility

**Section label:** `SUBSTRATE COMPATIBILITY` -- Y: 14.7".

**BLOCK D -- Compatibility Matrix**

Y: 15.3" to 20.3". Full width table.

| Substrate | Compatible? | DLC Method | Notes |
|---|---|---|---|
| Tool steel (HSS, D2, M2, H13) | YES | PECVD or arc | Largest DLC market. < 200 C preserves hardness. |
| Bearing steel (52100, 440C) | YES | PECVD or arc | Bearings, gears, seals. Cr interlayer standard. |
| Stainless steel (304, 316, 17-4PH) | YES | PECVD or arc | Medical, food processing. Si interlayer preferred. |
| Aluminum alloys | YES | PECVD | Automotive pistons, engine components. |
| Titanium alloys (Ti-6Al-4V) | YES | PECVD or arc | Biomedical implants. Ti interlayer natural match. |
| Cemented carbide (WC-Co) | YES | PECVD or arc | Cutting tools, forming dies. |
| Polymers | LIMITED | PECVD only | Very thin films only. Plasma pre-treatment required. |
| Ceramics (SiC, Al2O3) | YES | PECVD or arc | Specialty applications. |

Header: Barlow SemiBold, 14 pt, `#F0EDE8`. Fill `#3A4055`.
Data: Inter Regular, 12 pt, `#F0EDE8`. Alternating `#1E2435` / `#252B3D`.
"YES" in `#27AE60`. "LIMITED" in `#E8A020`.

---

### ZONE 4 -- Surface Finish Targets

**Section label:** `SURFACE FINISH TARGETS BY APPLICATION` -- Y: 20.7".

**BLOCK E -- Ra Targets**

Y: 21.3" to 26.3". Full width table.

| Application | Target Ra (um) | Why | Example Parts |
|---|---|---|---|
| Bearing surfaces | < 0.05 | Ultra-low friction required | Piston pins, cam followers, bearings |
| Cutting tools (molds) | < 0.10 | Part release; prevent sticking | Al die-cast molds, injection molds |
| Engine components | < 0.10 | Fuel efficiency, wear life | Tappets, fuel injectors, gears |
| Medical implants | < 0.05 | Biocompatibility; low wear debris | Orthopedic joint surfaces, surgical tools |
| General industrial | < 0.20 | Wear protection; moderate friction | Hydraulic components, textile guides |
| Decorative | < 0.10 | Visual appearance; smooth black finish | Watch components, jewelry |

Header: Barlow SemiBold, 14 pt. Fill `#3A4055`.
Ra values: JetBrains Mono 14 pt `#E8A020`.

**Bottom note:** `Measure Ra BEFORE coating. If Ra does not meet target, send back to polishing. DLC does not fix surface problems.` -- Inter Medium, 14 pt, `#E05C5C`.

---

### ZONE 5 -- Pre-Coating Checklist

**Section label:** `OPERATOR CHECKLIST -- BEFORE LOADING` -- Y: 26.7".

**BLOCK F -- Checklist**

Y: 27.3" to 32.3". Two columns of checklist items.

**Left column:**
1. `Dimensional inspection complete -- parts within tolerance`
2. `Surface finish verified -- Ra meets application target`
3. `No burrs, sharp edges, or machining damage`
4. `Non-coat areas masked (metal masks or approved tape)`

**Right column:**
5. `Parts cleaned per procedure (alkaline + solvent)`
6. `No fingerprints, oils, or visible contamination`
7. `Fixtures assigned -- contact points in non-critical areas`
8. `Paperwork: batch number, substrate material, DLC type specified`

Each item: Rounded rect row, H: 1.1", fill `#1E2435`, left accent 0.06" `#2EC4B6`.
Number: Barlow Condensed ExtraBold, 18 pt, `#2EC4B6`. Text: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Part Prep -- DLC`. Version `v1.0 -- 2026`.
Disclaimer: `Source: General industry knowledge; VDI 2840. Surface finish targets are typical values -- consult your coating supplier for application-specific requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Part Prep DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The single most important message on this poster is: DLC replicates your surface. The side-by-side hero visual must make this instantly obvious at 6 feet. Secondary message: DLC's low temperature (< 200 C) means it can coat hardened steels that PVD cannot -- this is a major commercial advantage and should be prominently displayed.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #441 -- Construction Workup v1.0*
*2026-04-26*
