---
Project: Plating Posters Inc
Poster Number: 435
Title: "ALD Cycling (Deposition) -- ALD"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters -- Watson Research Brief (Cluster 4: ALD, Sections 4.7-4.8)"
Technical Source: ALD deposition -- the pulse/purge/pulse/purge cycle that builds film one atomic layer at a time. Self-limiting surface reactions, growth per cycle (GPC), the ALD temperature window, and how cycle count digitally controls thickness. The defining feature of ALD and what makes it unique among all deposition methods.
Process Scope: ALD cycling / deposition (Stage 7 of 10)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ALD
  - Deposition
  - Cycling
  - SelfLimiting
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #435 -- Construction Workup
## ALD Cycling (Deposition) -- ALD

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 10. This is the heart of ALD -- the self-limiting pulse/purge/pulse/purge cycle that deposits exactly one sub-monolayer of material per cycle. This poster illustrates one complete ALD cycle for the canonical Al2O3 from TMA + H2O system, explains self-limiting behavior, defines Growth Per Cycle (GPC), and shows how cycle count directly controls film thickness with atomic precision.

Hero visual: a four-panel sequence showing one complete ALD cycle (Pulse A -> Purge -> Pulse B -> Purge) with surface chemistry illustrations.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Four-panel ALD cycle diagram (Block B -- HERO):** Four panels showing surface chemistry at each step of one ALD cycle.
2. **Self-limiting behavior explanation (Block C):** Why the reaction stops and what that means.
3. **GPC and thickness control table (Block D):** Cycle count -> thickness lookup for common films.
4. **ALD temperature window diagram (Block E):** Temperature vs. GPC showing the window.
5. **Cycle timing parameters (Block F):** Pulse and purge times for Al2O3.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- ALD CYCLE HERO (4.2"--14.5" / ~10.3")
  Block B: Four-panel cycle diagram
ZONE 4 -- SELF-LIMITING BEHAVIOR + GPC TABLE (14.5"--22.0" / ~7.5")
  Block C: Self-limiting explanation
  Block D: GPC and thickness lookup
ZONE 5 -- ALD TEMPERATURE WINDOW + CYCLE TIMING (22.0"--28.5" / ~6.5")
  Block E: Temperature window
  Block F: Timing parameters
ZONE 6 -- COMMON DEPOSITION PROBLEMS (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `ALD CYCLING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `ALD -- Stage 7 of 10 -- One Atomic Layer at a Time` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Pulse. Purge. Pulse. Purge. Repeat 100 times and you have 11 nm of Al2O3 -- pinhole-free, perfectly conformal, and digitally controlled by cycle count.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

**Rule Card:**
- Big number: `0.11` -- 60 pt, `#E8A020`
- Label: `nm PER CYCLE` -- JetBrains Mono, 14 pt
- Sub-label: `Al2O3 from TMA + H2O at 200 C` -- Inter Regular, 12 pt

---

### ZONE 2 -- Orientation Strip

Stage 7 (`ALD Cycling`): fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Input: Reactor at ALD temperature, precursors ready (Stage 6) --> Output: Film deposited to target thickness, ready for final purge`

---

### ZONE 3 -- ALD Cycle Hero

**Section label:** `ONE COMPLETE ALD CYCLE -- Al2O3 FROM TMA + H2O` -- Y: 4.4". Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`.

**BLOCK B -- Four-Panel Cycle Diagram (Y: 5.0" to 14.0")**

Four equal panels arranged left to right, each W: 5.5", H: 8.5". Rounded rect, fill `#1E2435`, radius 6.

**Panel 1 -- PULSE A: TMA (X: 0.5"):**
- Top accent 4 pt `#E8A020`
- Title: `STEP 1: TMA PULSE` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `15-200 ms`

Surface diagram area (center of panel):
- Bottom: substrate bar, fill `#3A4055`, H: 0.6"
- Surface: row of `-OH` groups, JetBrains Mono 12 pt `#27AE60`
- Arrows from above: `TMA vapor` molecules arriving
- Reaction annotation:
```
-OH + Al(CH3)3 -->
-O-Al(CH3)2 + CH4

TMA reacts with surface -OH groups.
When all -OH sites consumed,
reaction STOPS (self-limiting).
```
Inter Regular 12 pt `#F0EDE8`.

**Panel 2 -- PURGE 1 (X: 6.33"):**
- Top accent 4 pt `#2EC4B6`
- Title: `STEP 2: PURGE` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `5-30 sec`

Surface diagram:
- Substrate with `-O-Al(CH3)2` groups on surface (new surface)
- Arrows pointing away: `Excess TMA + CH4 removed`
- Horizontal flow arrow: `N2 or Ar purge gas`

```
Purge removes:
- Unreacted TMA
- CH4 byproduct
- Any physisorbed molecules

CRITICAL: Incomplete purge leads to
CVD-like growth (non-self-limiting)
```

**Panel 3 -- PULSE B: H2O (X: 12.16"):**
- Top accent 4 pt `#E8A020`
- Title: `STEP 3: H2O PULSE` Barlow SemiBold 18 pt `#E8A020`
- Subtitle: `15-200 ms`

Surface diagram:
- Surface with `-O-Al(CH3)2` groups
- Arrows from above: `H2O vapor` arriving
- Reaction annotation:
```
-Al(CH3)2 + H2O -->
-Al-OH + CH4

H2O reacts with surface -CH3 groups.
Regenerates -OH surface.
Self-limiting when all -CH3 consumed.
```

**Panel 4 -- PURGE 2 (X: 18.0"):**
- Top accent 4 pt `#2EC4B6`
- Title: `STEP 4: PURGE` Barlow SemiBold 18 pt `#2EC4B6`
- Subtitle: `5-30 sec`

Surface diagram:
- Substrate now has new `-OH` surface (same as starting surface!)
- Arrows pointing away: `Excess H2O + CH4 removed`

```
Surface is now identical to the
starting surface -- but one
sub-monolayer of Al2O3 has been added.

RESULT: +0.11 nm of Al2O3
READY FOR: Next cycle
```

**Cycle arrow at bottom connecting Panel 4 back to Panel 1:**
- Curved arrow, 3 pt `#E8A020`, with label `REPEAT N CYCLES`

**Bottom insight (Y: 13.3" to 14.0"):**
- Full-width rounded rect, fill `#252B3D`, left accent `#E8A020`
- `Each cycle adds exactly one sub-monolayer because the surface chemistry self-terminates. This is what gives ALD its atomic-level precision -- thickness is controlled by counting cycles, not by time, flux, or rate.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Self-Limiting Behavior + GPC Table

**Two-column layout (Y: 14.5" to 21.8"):**

**Left -- Self-Limiting Behavior (X: 0.5", W: 11.0")**

**Section label:** `WHY SELF-LIMITING MATTERS` -- Y: 14.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK C -- Self-Limiting Panel (Y: 15.3" to 21.5"):**

Rounded rect, fill `#1E2435`, left accent `#27AE60`.

Body (Inter Regular 13 pt `#F0EDE8`, line height 160%):
```
SELF-LIMITING means:
Once all available surface sites react,
NO MORE deposition occurs -- even if
you continue pulsing precursor.

THIS ENABLES:
1. DIGITAL THICKNESS CONTROL
   100 cycles = 11.0 nm. Period.

2. 100% CONFORMALITY
   High-aspect-ratio trenches, vias, and
   pores get the same thickness on bottom
   as on top (given sufficient exposure)

3. PINHOLE-FREE FILMS
   Self-limiting nature fills every gap
   above ~5-10 nm thickness

4. REACTOR GEOMETRY INDEPENDENCE
   Film thickness does not depend on
   gas flow pattern or substrate position
   (unlike PVD and most CVD)

VERIFICATION:
Saturation curve: plot GPC vs. pulse time.
GPC should plateau. If GPC keeps increasing
with longer pulse, the process is NOT
self-limiting (it is CVD).
```

**Right -- GPC and Thickness Lookup (X: 12.0", W: 11.5")**

**Section label:** `GROWTH PER CYCLE (GPC) REFERENCE` -- Y: 14.7".

**BLOCK D -- GPC Table (Y: 15.3" to 21.5"):**

| Film | Precursors | GPC (nm/cycle) | Cycles for 10 nm | Cycles for 50 nm |
|---|---|---|---|---|
| Al2O3 | TMA + H2O | 0.11 | ~91 | ~455 |
| HfO2 | TEMAH + H2O | 0.10 | ~100 | ~500 |
| TiO2 | TDMAT + H2O | 0.06 | ~167 | ~833 |
| ZrO2 | TEMAZ + H2O | 0.10 | ~100 | ~500 |
| ZnO | DEZ + H2O | 0.18 | ~56 | ~278 |
| TiN | TDMAT + NH3 | 0.05 | ~200 | ~1000 |
| SiO2 | BDEAS + O2 plasma | 0.12 | ~83 | ~417 |
| Pt | MeCpPtMe3 + O2 | 0.05 | ~200 | ~1000 |

Header: Barlow SemiBold 12 pt, fill `#3A4055`. Data: JetBrains Mono 11 pt `#F0EDE8`. Alternating rows.

Bottom callout:
- `These GPC values are typical at mid-range ALD window temperature. GPC is constant within the ALD window but drops or rises outside it (see Temperature Window below).` Inter Medium 12 pt `#2EC4B6`

---

### ZONE 5 -- ALD Temperature Window + Cycle Timing

**Two-column layout (Y: 22.0" to 28.3"):**

**Left -- ALD Temperature Window (X: 0.5", W: 11.0")**

**Section label:** `THE ALD TEMPERATURE WINDOW` -- Y: 22.2". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**BLOCK E -- Temperature Window Diagram (Y: 22.8" to 28.0"):**

Main panel: Rounded rect, fill `#1E2435`, left accent `#E8A020`.

**Conceptual chart (center):**

X-axis: `Temperature (C)` -- 50 to 450
Y-axis: `GPC (nm/cycle)`

Four labeled regions on the curve:

Region 1 (far left, GPC rising):
- Label: `CONDENSATION` -- `#E05C5C`
- `Precursor condenses on cold surface. GPC > true value. Not self-limiting.`

Region 2 (left, GPC flat but low):
- Label: `INCOMPLETE REACTION` -- `#E8A020`
- `Surface reaction too slow. GPC below saturation value.`

Region 3 (center, GPC flat -- plateau):
- Label: `ALD WINDOW` -- `#27AE60`
- Highlighted band, fill `#27AE60` at 15%
- `GPC is constant. Self-limiting confirmed. OPERATE HERE.`
- `TMA/H2O: ~150-350 C`

Region 4 (right, GPC rising or falling):
- Label: `DECOMPOSITION` -- `#E05C5C`
- `Precursor decomposes in gas phase (CVD mode) or desorbs before reacting.`

**Right -- Cycle Timing Parameters (X: 12.0", W: 11.5")**

**Section label:** `CYCLE TIMING -- Al2O3 REFERENCE` -- Y: 22.2".

**BLOCK F -- Timing Table (Y: 22.8" to 26.0"):**

| Parameter | Typical Value |
|---|---|
| TMA pulse time | 0.015-0.2 sec |
| TMA dose | 0.1-1 Torr pulse |
| Purge after TMA | 5-30 sec |
| H2O pulse time | 0.015-0.2 sec |
| Purge after H2O | 5-30 sec |
| Total cycle time | 15-60 sec |
| Cycles for 10 nm Al2O3 | ~91 |
| Total time for 10 nm | 25-100 min |

JetBrains Mono 12 pt `#F0EDE8`. Header: `#3A4055`.

Below table -- Critical note:
- Rounded rect, fill `#E8A020` at 15%, border 1 pt `#E8A020`
- `Purge time dominates the cycle. For high-aspect-ratio structures (semiconductor vias), purge times increase to 30-60 sec to ensure complete removal from deep features. This is why ALD is slow.` Barlow SemiBold 12 pt `#E8A020`

---

### ZONE 6 -- Common Deposition Problems

**Section label:** `DEPOSITION PROBLEMS` -- Y: 28.7". Barlow Condensed ExtraBold, 22 pt, `#F0EDE8`.

**Four Problem Cards (Y: 29.3" to 32.0")**

Each card: Rounded rect W: 5.5", H: 2.5", fill `#1E2435`, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | NON-SELF-LIMITING GROWTH | Insufficient purge; precursor overlap = CVD mode | Increase purge time; verify with saturation curve |
| 2 | 6.33" | ISLAND GROWTH | Surface lacks functional groups; contamination blocking nucleation | Surface functionalization (O2 plasma); proper cleaning |
| 3 | 12.16" | THICKNESS DRIFT | Temperature outside ALD window; bubbler temp unstable | Verify temperature calibration; check bubbler +/- 1 C |
| 4 | 18.0" | HIGH CARBON IN FILM | Low deposition temp (< 150 C); short purges | Increase temp; use plasma-ALD; extend purge |

Interior per card:
- Problem: Barlow SemiBold 14 pt `#E05C5C`
- Cause: Inter Regular 12 pt `#F0EDE8`
- Fix: Inter Medium 12 pt `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `ALD Cycling (Deposition) -- ALD`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `ALD Cycling Deposition ALD -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The four-panel ALD cycle is the money shot for this entire cluster. Watson flagged that the self-limiting pulse/purge mechanism is ideal for visual representation, and he is right -- the four panels show the surface chemistry evolving through one complete cycle, ending with a surface identical to the start (but with one more sub-monolayer). The cycle arrow connecting Panel 4 back to Panel 1 reinforces the repetitive nature.

The GPC table is the quick-reference that ALD engineers will use daily -- "how many cycles for 20 nm HfO2?" The ALD temperature window diagram is essential context for anyone setting up a process: operate inside the window or your self-limiting behavior breaks down.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #435 -- Construction Workup v1.0*
*2026-04-26*
