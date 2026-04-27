---
Project: Plating Posters Inc
Poster Number: 481
Title: "Cleaning -- Plasma Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 1: APS, Poster 3)"
Technical Source: Pre-spray cleaning sequence for APS including solvent degrease, alkaline wash, water-break-free inspection, and drying. Time-between-steps requirements per industry best practice.
Process Scope: Atmospheric plasma spray -- pre-spray cleaning and contamination removal
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - PlasmaSpray
  - APS
  - Cleaning
  - ConstructionWorkup
  - ClusterTS01
---

# Poster #481 -- Construction Workup
## Cleaning -- Plasma Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of the APS process. Surface contamination is the number-one cause of coating failure in thermal spray. This poster drives that point home with a 4-step cleaning sequence as the hero, a contamination source table, and a time-between-steps critical path strip.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **4-step cleaning sequence (Block B -- HERO):** Four large numbered step cards in a vertical flow. Each card shows the step, method, and pass/fail criteria.
2. **Contamination source table (Block D):** 6-row table showing contaminant types, sources, and consequences.
3. **Time-between-steps strip (Block E):** Horizontal timeline showing critical time windows.
4. **"Clean Before Mask" callout (Block F):** Warning banner.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 1 highlighted (Teal)
ZONE 3 -- CLEANING SEQUENCE HERO (4.2"--15.5" / ~11.3")
  Block B: 4-step vertical flow
ZONE 4 -- CONTAMINATION TABLE (15.5"--22.0" / ~6.5")
  Block D: Contaminant source and consequence table
ZONE 5 -- TIME-BETWEEN-STEPS (22.0"--28.5" / ~6.5")
  Block E: Critical time windows
ZONE 6 -- CLEAN BEFORE MASK CALLOUT (28.5"--32.5" / ~4.0")
  Block F: Warning banner + glove handling rules
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Plasma Spray (APS) -- Pre-Spray Surface Preparation -- Stage 1 of 10` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Skip the prep. Ruin the coating. Every delamination investigation starts here.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received part (oils, oxides, contamination) --> After: Chemically clean, dry surface ready for grit blast`

---

### ZONE 3 -- Cleaning Sequence (HERO)

**Section label:** `THE 4-STEP CLEANING SEQUENCE` -- Y: 4.4".

**BLOCK B -- Four Step Cards (vertical flow)**

Y: 5.0" to 15.3". Four cards stacked vertically with downward arrows between them.

Each card: Rounded rect, X: 1.0", W: 22.0", H: 2.2", fill `#1E2435`, radius 6, left accent 0.06".

| Step | Y | Accent | Name | Method | Pass/Fail |
|---|---|---|---|---|---|
| 1 | 5.0" | `#2EC4B6` | SOLVENT DEGREASE | Vapor degrease (legacy) or aqueous alkaline clean (preferred). Remove all oils, greases, machining fluids, fingerprints. | Visible contamination = fail |
| 2 | 7.8" | `#2EC4B6` | ALKALINE WASH | Immersion or spray wash. 50-70 degC, pH 10-12, 5-15 min. Rinse thoroughly with clean water. | Residual alkaline = fail |
| 3 | 10.6" | `#27AE60` | WATER-BREAK-FREE TEST | ASTM F22 equivalent. Surface must sheet water uniformly with no beading. Any beading indicates residual contamination. | Any water break = FAIL -- repeat Steps 1-2 |
| 4 | 13.4" | `#E8A020` | DRY | Forced air or oven dry. No moisture at time of grit blast. Moisture causes flash rust on steel substrates. | Surface must be bone dry |

Interior per card:
- Step number badge: Rounded rect 1.0" x 0.4", fill accent color, text `STEP [N]` Barlow Condensed ExtraBold 14 pt `#1A1F2E`
- Name: Barlow SemiBold 22 pt `#F0EDE8`
- Method: Inter Regular 14 pt `#F0EDE8` (left 60% of card width)
- Pass/Fail: Inter Medium 14 pt, accent color (right 35% of card width), bordered box

Arrows between cards: 3 pt `#3A4055`, down-pointing, centered.

---

### ZONE 4 -- Contamination Table

**Section label:** `WHAT CONTAMINANTS DO TO YOUR COATING` -- Y: 15.7".

**BLOCK D -- Contamination Table**

Y: 16.3" to 21.8". Columns: Contaminant (4.0") | Common Source (6.0") | Consequence (6.5") | Detection (6.5")

| Contaminant | Source | Consequence | Detection |
|---|---|---|---|
| Oil / grease | Machining fluids, fingerprints | Delamination, poor bond strength | Water-break-free test |
| Rust / mill scale | Storage, ambient exposure | Weak interface, porosity at bond line | Visual; SSPC-SP 5 verification |
| Moisture | Humidity, incomplete drying | Flash rust; hydrogen porosity in coating | Dew point check; forced air dry |
| Cutting fluid residue | Prior machining operations | Outgassing during spray; porosity | Solvent wipe + UV inspection |
| Oxide films | Prior heat treatment, welding | Reduced mechanical interlocking | Grit blast removes (Stage 2) |
| Masking adhesive | Premature masking over dirty surface | Contamination trapped under mask | NEVER mask before cleaning |

Header: fill `#3A4055`. Data: Inter Regular 12 pt. Consequence column in `#E05C5C`.

---

### ZONE 5 -- Time-Between-Steps

**Section label:** `CRITICAL TIME WINDOWS -- DO NOT EXCEED` -- Y: 22.2".

**BLOCK E -- Horizontal Timeline**

Y: 23.0" to 28.0". Full width.

Three time-window bars (horizontal):

| Window | From | To | Max Time | Color |
|---|---|---|---|---|
| 1 | Cleaning complete | Grit blast start | Same shift (ideally < 4 hrs) | `#2EC4B6` |
| 2 | Grit blast complete | Spray start | < 4 hours (some specs: < 2 hrs) | `#E8A020` |
| 3 | Spray start | Part handling | Allow full cool-down | `#27AE60` |

Each bar: Rounded rect, full width, H: 1.2", fill accent at 15%, border 1 pt accent.
- Left label: `FROM:` + step name. Right label: `TO:` + step name. Center: big time value in Barlow Condensed ExtraBold 36 pt, accent color.

Below bars: `Humidity matters: in high-humidity environments (>60% RH), reduce all time windows by half. Freshly blasted steel rusts FAST.` Inter Medium 14 pt `#E05C5C`.

---

### ZONE 6 -- Clean Before Mask Callout

**BLOCK F -- Warning Banner**

- Rounded rect, X: 0.5", Y: 29.2", W: 23.0", H: 3.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`

**Main text:** Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center

> CLEAN BEFORE MASKING -- NEVER MASK OVER CONTAMINATION

**Sub-text:** Inter Medium, 16 pt, `#F0EDE8`, Center

> Wear clean lint-free gloves after cleaning. No bare-hand contact with blasted surfaces. Every fingerprint is a potential delamination site.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Plasma Spray`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Plasma -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is about discipline. The 4-step sequence is simple -- but the consequences of skipping any step are catastrophic. The time-between-steps strip is the unique visual on this poster -- operators need to internalize that freshly blasted surfaces have a shelf life. The "Clean Before Mask" callout is a direct response to the most common mistake in thermal spray shops.

---

*Alaina -- Poster #481 -- Construction Workup v1.0 -- 2026-04-26*
