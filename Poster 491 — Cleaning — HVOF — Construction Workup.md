---
Project: Plating Posters Inc
Poster Number: 491
Title: "Cleaning -- HVOF"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 2: HVOF, Poster 3)"
Technical Source: Pre-spray cleaning sequence for HVOF. Surface cleanliness is even more critical than APS because HVOF coatings are so dense that contaminants at the interface have no porosity to hide in. Chrome-stripped part handling for hard chrome replacement applications.
Process Scope: HVOF thermal spray -- pre-spray cleaning and contamination removal
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ThermalSpray
  - HVOF
  - Cleaning
  - ConstructionWorkup
  - ClusterTS02
---

# Poster #491 -- Construction Workup
## Cleaning -- HVOF

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 1 of the HVOF process. Same 4-step cleaning sequence as APS, but with a critical HVOF-specific twist: because HVOF coatings are so dense (< 1% porosity), there is absolutely nowhere for interface contaminants to hide. Every molecule of contamination directly compromises bond strength. The additional content block covers chrome-stripped part handling -- the most common incoming condition for HVOF hard chrome replacement jobs.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **4-step cleaning sequence (Block B -- HERO):** Four large numbered step cards in a vertical flow.
2. **Chrome-strip handling callout (Block D):** Special procedures for parts arriving from chrome stripping.
3. **Time-between-steps strip (Block E):** Critical time windows.
4. **"Dense Coatings Demand Clean Surfaces" callout (Block F):** Warning banner.

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
ZONE 4 -- CHROME-STRIP HANDLING (15.5"--22.0" / ~6.5")
  Block D: Incoming part condition for chrome replacement jobs
ZONE 5 -- TIME-BETWEEN-STEPS (22.0"--28.5" / ~6.5")
  Block E: Critical time windows
ZONE 6 -- DENSE COATING CALLOUT (28.5"--32.5" / ~4.0")
  Block F: Warning banner
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `HVOF -- Pre-Spray Surface Preparation -- Stage 1 of 10` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `HVOF coatings are dense. Less than 1% porosity. That means contaminants have nowhere to hide -- they sit at the interface and destroy your bond.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 1 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: As-received part (oils, chrome residue, contamination) --> After: Chemically clean, dry surface ready for grit blast`

---

### ZONE 3 -- Cleaning Sequence (HERO)

**Section label:** `THE 4-STEP CLEANING SEQUENCE` -- Y: 4.4".

**BLOCK B -- Four Step Cards (vertical flow)**

Y: 5.0" to 15.3". Four cards stacked vertically with downward arrows between them.

Each card: Rounded rect, X: 1.0", W: 22.0", H: 2.2", fill `#1E2435`, radius 6, left accent 0.06".

| Step | Y | Accent | Name | Method | Pass/Fail |
|---|---|---|---|---|---|
| 1 | 5.0" | `#2EC4B6` | SOLVENT DEGREASE | Aqueous alkaline clean (preferred) or vapor degrease (legacy). Remove all oils, greases, machining fluids, fingerprints. | Visible contamination = fail |
| 2 | 7.8" | `#2EC4B6` | ALKALINE WASH | Immersion or spray wash. 50-70 degC, pH 10-12, 5-15 min. Rinse thoroughly. DI water final rinse for aerospace components. | Residual alkaline = fail |
| 3 | 10.6" | `#27AE60` | WATER-BREAK-FREE TEST | ASTM F22 equivalent. Surface must sheet water uniformly with no beading. Any beading = residual contamination. | Any water break = FAIL -- repeat Steps 1-2 |
| 4 | 13.4" | `#E8A020` | DRY | Forced air or oven dry. No moisture at time of grit blast. Moisture causes flash rust on steel substrates. | Surface must be bone dry |

Interior per card:
- Step number badge: Rounded rect 1.0" x 0.4", fill accent color, text `STEP [N]` Barlow Condensed ExtraBold 14 pt `#1A1F2E`
- Name: Barlow SemiBold 22 pt `#F0EDE8`
- Method: Inter Regular 14 pt `#F0EDE8` (left 60% of card width)
- Pass/Fail: Inter Medium 14 pt, accent color (right 35% of card width), bordered box

Arrows between cards: 3 pt `#3A4055`, down-pointing, centered.

---

### ZONE 4 -- Chrome-Strip Handling

**Section label:** `CHROME REPLACEMENT JOBS -- INCOMING PART HANDLING` -- Y: 15.7".

**BLOCK D -- Chrome-Strip Callout**

Y: 16.3" to 21.8". Two-column layout.

**Left -- The Problem (W: 11.0"):**
- Rounded rect, X: 0.5", fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `PARTS ARRIVING FROM CHROME STRIP` Barlow SemiBold 18 pt `#E05C5C`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
Most HVOF chrome replacement parts arrive
after chemical or mechanical chrome strip.

Common incoming conditions:
- Residual chrome not fully removed
- Etch products from acid strip (pitting)
- Hydrogen embrittlement from stripping acid
- Dimensional undersize from strip + grinding

Every one of these conditions affects bond strength.
```

**Right -- The Solution (W: 11.5"):**
- Rounded rect, X: 12.0", fill `#1E2435`, left accent `#27AE60` 0.06"
- Title: `VERIFICATION STEPS` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 13 pt `#F0EDE8`, line height 165%):
```
1. Visual inspect for residual chrome (shiny patches)
2. Spot-check with dilute copper sulfate solution
   (copper deposits on steel, not on chrome)
3. Verify dimensions -- measure before cleaning
4. If acid-stripped: bake 375 degF / 4 hrs for
   hydrogen embrittlement relief (per ASTM B849)
5. Full alkaline clean sequence AFTER bake
6. Proceed to grit blast only when clean and verified
```

Bottom note spanning full width:
`If residual chrome is found, DO NOT proceed to grit blast -- return to stripping. Blasting over chrome creates a weak interface that will delaminate in service.` Inter Medium 14 pt `#E05C5C`.

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

### ZONE 6 -- Dense Coating Callout

**BLOCK F -- Warning Banner**

- Rounded rect, X: 0.5", Y: 29.2", W: 23.0", H: 3.0", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`

**Main text:** Barlow Condensed ExtraBold, 28 pt, `#E05C5C`, Center

> DENSE COATINGS DEMAND CLEAN SURFACES -- THERE IS NO POROSITY TO FORGIVE CONTAMINATION

**Sub-text:** Inter Medium, 16 pt, `#F0EDE8`, Center

> APS coatings with 5-15% porosity can sometimes tolerate minor interface contamination. HVOF at <1% porosity cannot. Every fingerprint, every oil droplet, every residual chrome flake is a delamination site waiting to fail.

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- HVOF`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning HVOF -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The chrome-strip handling block is what makes this poster unique from the APS cleaning poster. The vast majority of HVOF work is chrome replacement -- and the parts arrive in various states of "stripped." Teaching operators how to verify incoming condition before proceeding is critical. The dense-coating callout drives home the central theme: HVOF's greatest strength (density) is also what makes contamination unforgivable.

---

*Alaina -- Poster #491 -- Construction Workup v1.0 -- 2026-04-26*
