---
Project: Plating Posters Inc
Poster Number: 655
Title: "Flash / Leveling -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.7"
Technical Source: The gel-flow-cure sequence in powder coating -- the functional equivalent of flash/leveling in liquid paint. No solvent means no flash period, but the melt-flow-crosslink stages determine finish quality. Temperature ramp vs. viscosity curve is the key relationship.
Process Scope: Gel / flow / cure stages -- powder coating leveling (Stage 6 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - FlashLeveling
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #655 -- Construction Workup
## Flash / Leveling -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 6 of 9. Powder coating has no solvent, so there's no "flash" in the liquid paint sense. Instead, the gel-flow-cure sequence inside the oven IS the leveling event. The hero visual is a temperature-vs-viscosity timeline showing the three phases: melt/gel, flow/level, and crosslink/cure. This is where orange peel lives or dies. Insufficient flow time = textured surface. Excessive time = overbake. The operator's job is to hit the sweet spot.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Temperature vs. viscosity timeline (Block B -- HERO):** A horizontal timeline diagram showing the three phases of powder cure with temperature rising and viscosity dipping then rising. Built with rectangles, lines, and labeled zones.
2. **Phase breakdown (Block C):** Three callout cards describing each phase.
3. **Factors affecting leveling (Block D):** Particle size, cure schedule, flow additives, film thickness.
4. **Orange peel vs. smooth finish comparison (Block E):** Side-by-side visual.
5. **Defect grid (Block F):** 6 leveling-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Flash / Leveling (Amber)
ZONE 3 -- GEL-FLOW-CURE TIMELINE HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- THREE-PHASE BREAKDOWN (15.0"--21.0" / ~6.0")
ZONE 5 -- FACTORS + ORANGE PEEL COMPARISON (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID -- LEVELING FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `FLASH / LEVELING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- The Gel-Flow-Cure Sequence` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `No solvent, no flash. But the melt-flow-crosslink sequence in the oven determines everything about surface finish. This is where orange peel lives or dies.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Flash / Leveling -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Dry powder layer on part surface --> After: Molten, flowing, leveling film en route to cross-link`

---

### ZONE 3 -- Gel-Flow-Cure Timeline Hero

**Section label:** `TEMPERATURE vs. VISCOSITY -- THE THREE PHASES` -- Y: 4.4".

**BLOCK B -- Timeline Diagram**

Y: 5.0" to 14.5". Full-width diagram.

Horizontal axis: TIME (minutes in oven) -- 0 to 20 min
Two vertical axes: LEFT = Temperature (F), RIGHT = Viscosity (relative)

The diagram is built with colored rectangles representing three zones along the timeline:

*Phase 1 -- Melt / Gel (0--5 min):*
- Background zone: rect fill `#E8A020` at 10%, X: 1.0" to 7.0"
- Label: `MELT / GEL` -- Barlow Condensed ExtraBold, 22 pt, `#E8A020`
- Temperature line rising from ambient to ~300 F
- Viscosity line: starts infinite (solid), drops rapidly as powder melts
- Annotations (JetBrains Mono 12 pt):
  - `Particles soften and melt`
  - `Begin to flow together`
  - `Viscosity drops sharply`

*Phase 2 -- Flow / Level (5--13 min):*
- Background zone: rect fill `#27AE60` at 10%, X: 7.0" to 15.0"
- Label: `FLOW / LEVEL` -- Barlow Condensed ExtraBold, 22 pt, `#27AE60`
- Temperature steady at 350--400 F
- Viscosity at minimum -- film is most fluid
- Annotations:
  - `Viscosity at MINIMUM`
  - `Molten coating flows and levels`
  - `THIS is when finish quality is determined`
  - `Longer flow = smoother finish`

*Phase 3 -- Crosslink / Cure (13--20 min):*
- Background zone: rect fill `#E05C5C` at 10%, X: 15.0" to 22.0"
- Label: `CROSSLINK / CURE` -- Barlow Condensed ExtraBold, 22 pt, `#E05C5C`
- Temperature maintained at cure temp
- Viscosity line rises steeply (film solidifies)
- Annotations:
  - `Cross-linking begins`
  - `Viscosity rises rapidly`
  - `Film hardens irreversibly`
  - `Point of no return`

Key callout box (bottom of hero, centered):
- Fill `#1E2435`, border 1 pt `#E8A020`
- Text: `The flow/level phase is the ONLY window where surface finish can improve. Once cross-linking starts, the surface is locked in.` -- Inter Medium 14 pt `#E8A020`

---

### ZONE 4 -- Three-Phase Breakdown

**Section label:** `PHASE-BY-PHASE DETAIL` -- Y: 15.2".

**Three cards in a single row (Y: 15.8" to 20.8"):**

*Phase 1 -- Melt/Gel (X: 0.5", W: 7.33"):*
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `MELT / GEL` -- Barlow SemiBold, 18 pt, `#E8A020`
- Duration: `First 2--5 min` -- JetBrains Mono 14 pt
- Body (Inter Regular 13 pt):
  - `Powder particles soften as temperature rises`
  - `Adjacent particles begin to merge`
  - `Film is discontinuous -- not yet a coating`
  - `Benzoin (degassing additive) releases trapped air`

*Phase 2 -- Flow/Level (X: 8.17", W: 7.33"):*
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `FLOW / LEVEL` -- Barlow SemiBold, 18 pt, `#27AE60`
- Duration: `Next 3--8 min` -- JetBrains Mono 14 pt
- Body:
  - `Continuous molten film at minimum viscosity`
  - `Surface tension drives leveling`
  - `Flow additives (acrylate agents) reduce viscosity`
  - `Longer flow time = smoother finish`
  - `THIS PHASE DETERMINES ORANGE PEEL`

*Phase 3 -- Crosslink/Cure (X: 15.83", W: 7.67"):*
- Fill: `#1E2435`, top accent `#E05C5C`
- Title: `CROSSLINK / CURE` -- Barlow SemiBold, 18 pt, `#E05C5C`
- Duration: `Remaining time` -- JetBrains Mono 14 pt
- Body:
  - `Cross-linking reaction accelerates`
  - `Viscosity increases rapidly`
  - `Film hardens irreversibly`
  - `Resin + hardener form 3D polymer network`
  - `CANNOT be remelted after full cure`

---

### ZONE 5 -- Factors + Orange Peel Comparison

**Two-column layout (Y: 21.2" to 26.3"):**

**Left -- Factors Affecting Leveling (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `FACTORS THAT AFFECT LEVELING` -- Barlow SemiBold, 18 pt, `#27AE60`

| Factor | Effect on Leveling | Operator Action |
|---|---|---|
| Particle size (D50) | Finer = smoother | Verify D50 30--45 um |
| Cure schedule | Faster ramp = less flow time | Slower ramp improves finish |
| Flow additives | Reduce melt viscosity | Additive is in the powder formulation |
| Film thickness | Thicker films flow better | Target mid-to-upper DFT range |
| Powder formulation | Varies by chemistry | Consult powder supplier |

**Right -- Orange Peel Comparison (X: 12.0", W: 11.5"):**

Title: `SMOOTH vs. ORANGE PEEL` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Two stacked panels:

*Smooth Finish:*
- Accent: `#27AE60`
- `Adequate flow time (3--8 min in flow phase)`
- `Correct particle size distribution`
- `Proper film thickness (thicker helps)`
- `Result: Uniform, level surface`

*Orange Peel:*
- Accent: `#E05C5C`
- `Insufficient flow time (fast ramp or overcure schedule)`
- `Coarse particle size or narrow distribution`
- `Thin film (< 1.5 mils)`
- `Back-ionization from excessive voltage`
- `Result: Textured, bumpy surface -- not repairable without strip and recoat`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN LEVELING FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | ORANGE PEEL | `#E05C5C` | Insufficient flow time or back-ionization | Slower cure ramp; reduce gun voltage |
| R1C2 | YELLOWING | `#E8A020` | Overbake (excessive time or temperature) | Reduce oven time/temp; profile with datalogger |
| R1C3 | EMBRITTLEMENT | `#E05C5C` | Excessive cross-linking from overbake | Reduce cure schedule; mandrel bend test to verify |
| R2C1 | PINHOLES | `#E8A020` | Trapped air not released during melt/gel phase | Verify benzoin degassing additive in powder |
| R2C2 | SURFACE CRATERING | `#E05C5C` | Contamination on substrate or in powder | Clean reclaim system; verify substrate cleanliness |
| R2C3 | THIN SPOTS WITH TEXTURE | `#2EC4B6` | Film too thin for adequate leveling | Increase DFT to mid-range or above |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Flash / Leveling -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references. Cure schedules and leveling characteristics are powder-formulation-specific -- consult your powder manufacturer.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Flash Leveling Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The timeline hero is the centerpiece -- temperature vs. viscosity over time, with three colored zones. This is the poster that explains WHY orange peel happens, not just WHAT it looks like. The flow/level phase being the only window for surface improvement is the single most important concept on the poster. The orange peel comparison gives operators a mental model: "if the finish is bad, the flow phase was too short."

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #655 -- Construction Workup v1.0*
*2026-04-26*
