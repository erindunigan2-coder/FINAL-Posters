---
Project: Plating Posters Inc
Poster Number: 442
Title: "Cleaning -- DLC"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 5: DLC, Section 5.4)"
Process Scope: Pre-coating cleaning sequence for DLC substrates
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - DLC
  - Cleaning
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #442 -- Construction Workup
## Cleaning -- DLC

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning for DLC is a multi-step sequence from alkaline ultrasonic through solvent final clean to vacuum drying. The standard is absolute: zero contamination, zero water spots, zero fingerprints. Any organic residue on the substrate becomes a delamination site. This poster covers the full external cleaning sequence (the in-chamber ion etch is covered in Poster 444).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Cleaning sequence flow (Block B -- HERO):** Vertical flow of 5 cleaning steps with time, temperature, and chemistry for each.
2. **Contamination vs. consequence table (Block D):** What contaminant causes what DLC failure.
3. **Water-break test callout (Block E):** How to verify cleanliness.
4. **Do / Don't comparison (Block F):** Common cleaning mistakes.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 15.5" / 21.5" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- CLEANING SEQUENCE HERO (2.9"--15.5" / ~12.6")
  Block B: Five-step vertical cleaning flow
ZONE 3 -- CONTAMINATION CONSEQUENCES (15.5"--21.5" / ~6.0")
  Block D: Contaminant -> failure table
ZONE 4 -- WATER-BREAK TEST + HANDLING (21.5"--27.0" / ~5.5")
  Block E: Verification method + glove handling rules
ZONE 5 -- DO / DON'T (27.0"--32.5" / ~5.5")
  Block F: Side-by-side comparison
ZONE 6 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 88 pt `#F0EDE8`.
**Subheading:** `Diamond-Like Carbon -- Pre-Coating Cleaning Sequence` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Contamination equals delamination. The cleaning sequence is not optional, not flexible, and not negotiable.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cleaning Sequence Hero

**Section label:** `FIVE-STEP CLEANING SEQUENCE` -- Y: 3.1".

**BLOCK B -- Vertical Flow (5 Steps)**

Y: 3.8" to 15.3". Five stacked cards with downward arrows between them.

Each card: Rounded rect, X: 0.5", W: 23.0", H: 2.0", fill `#1E2435`, radius 6, left accent 0.06" `#2EC4B6`.

| Step | Name | Chemistry | Temperature | Time | Key Detail |
|---|---|---|---|---|---|
| 1 | Alkaline Ultrasonic Clean | Alkaline detergent solution | 50--70 C (120--160 F) | 10--20 min | Removes oils, greases, machining fluids. Ultrasonic agitation essential. |
| 2 | Multi-Stage Rinse | DI or high-purity water | Ambient | 2--5 min per stage | Minimum 2 rinse stages. Remove all alkaline residue. |
| 3 | Solvent Clean | IPA (isopropanol) or acetone | Ambient | 5--10 min | Ultrasonic recommended. Removes residual organics not caught by alkaline. |
| 4 | Final Rinse | IPA or acetone (fresh) | Ambient | 1--3 min | Fresh solvent -- never re-use contaminated solvent for final rinse. |
| 5 | Vacuum Drying | -- | 50--80 C (if heated) | Until dry | Zero water spots. No compressed air (oil contamination risk). Vacuum oven preferred. |

Step number: Barlow Condensed ExtraBold, 24 pt, `#2EC4B6`.
Name: Barlow SemiBold, 20 pt, `#F0EDE8`.
Chemistry/Temp/Time: JetBrains Mono Regular, 13 pt, `#F0EDE8`.
Key Detail: Inter Regular, 13 pt, `#F0EDE8` at 70%.

Arrows between cards: 3 pt `#3A4055`, arrowhead filled, down. Centered horizontally.

---

### ZONE 3 -- Contamination Consequences

**Section label:** `WHAT CONTAMINATION DOES TO DLC` -- Y: 15.7".

**BLOCK D -- Contamination Table**

Y: 16.3" to 21.3". Full width.

| Contaminant | Source | DLC Failure Mode | How Bad? |
|---|---|---|---|
| Fingerprint oils | Bare-hand contact | Delamination at contact site | Critical |
| Machining oil residue | Incomplete alkaline clean | Widespread pitting and adhesion loss | Critical |
| Water spots | Air drying, compressed air | Localized delamination, pinhole defects | Serious |
| Particulate (dust, grit) | Poor cleanroom practice | Coating defects, pinhole sites | Serious |
| Solvent residue | Contaminated final rinse | Thin-film contamination, haze | Moderate |
| Alkaline residue | Insufficient rinsing | Chemical interference with interlayer | Serious |

"Critical" in `#E05C5C`. "Serious" in `#E8A020`. "Moderate" in `#F0EDE8`.
Header: Barlow SemiBold, 14 pt, `#F0EDE8`. Fill `#3A4055`.
Data: Inter Regular, 12 pt, `#F0EDE8`. Alternating rows.

---

### ZONE 4 -- Water-Break Test + Handling

**Section label:** `VERIFICATION + HANDLING RULES` -- Y: 21.7".

**Two-column layout:**

**Left -- Water-Break Test (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `WATER-BREAK TEST` -- Barlow SemiBold, 20 pt, `#27AE60`
- Steps:
  1. `Rinse part with clean DI water`
  2. `Observe water film behavior`
  3. `PASS: Water sheets uniformly -- no beading, no breaks`
  4. `FAIL: Water beads or breaks = organic contamination present`
  5. `If FAIL: return to Step 1 (alkaline clean)`
- Steps: Inter Regular, 14 pt, `#F0EDE8`. PASS in `#27AE60`. FAIL in `#E05C5C`.

**Right -- Handling Rules (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `HANDLING AFTER CLEANING` -- Barlow SemiBold, 20 pt, `#E8A020`
- Rules:
  - `Nitrile gloves ONLY -- never bare hands`
  - `Never touch cleaned surfaces -- handle by edges or fixtures`
  - `Load into chamber within 1 hour of cleaning`
  - `If delay > 1 hour: store in sealed clean container, re-clean if > 4 hours`
  - `No shop air on cleaned parts -- contamination risk`
- Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 5 -- Do / Don't

**Section label:** `DO vs. DON'T` -- Y: 27.2".

**BLOCK F -- Side-by-Side**

Y: 27.8" to 32.3".

**Left -- DO (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `DO` -- Barlow Condensed ExtraBold, 24 pt, `#27AE60`
- Items:
  - `Use fresh solvent for final rinse`
  - `Vacuum dry or clean oven dry`
  - `Wear nitrile gloves at all times`
  - `Inspect under bright light before loading`
  - `Log cleaning batch and time`

**Right -- DON'T (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `DON'T` -- Barlow Condensed ExtraBold, 24 pt, `#E05C5C`
- Items:
  - `Don't use shop compressed air (oil mist)`
  - `Don't air dry -- water spots = delamination`
  - `Don't re-use dirty solvent`
  - `Don't stack cleaned parts -- contact contamination`
  - `Don't delay loading -- contamination builds with time`

Items: Inter Regular, 14 pt, `#F0EDE8`.

---

### ZONE 6 -- Footer

Standard. Title: `Cleaning -- DLC`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning DLC -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster hammers one message: cleaning quality determines coating quality. The vertical flow is intentionally simple -- five steps, each clearly delineated. The contamination consequences table provides the "why" behind the obsessive cleaning. The water-break test is the oldest and simplest cleanliness verification in the finishing industry, and it works just as well for DLC substrates as for electroplating.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #442 -- Construction Workup v1.0*
*2026-04-26*
