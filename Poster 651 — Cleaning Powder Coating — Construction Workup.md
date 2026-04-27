---
Project: Plating Posters Inc
Poster Number: 651
Title: "Cleaning -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.3"
Technical Source: Industry-standard multi-stage spray washer cleaning for powder coating. Covers alkaline cleaning chemistry, 5-stage wash systems, conductivity monitoring, and water-break verification. Values are typical ranges for industrial spray tunnel systems on steel and aluminum substrates.
Process Scope: Cleaning for powder coating -- multi-stage spray washer (Stage 2 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - Cleaning
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #651 -- Construction Workup
## Cleaning -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 2 of 9. The multi-stage spray washer is the workhorse of powder coat pretreatment -- five stages that take incoming parts from contaminated to conversion-coated in under 10 minutes. The hero visual is the 5-stage tunnel diagram showing each stage with its chemistry, temperature, and time. Cleaner oil loading and silicate residues are the two most common failure modes that destroy downstream adhesion.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Five-stage tunnel diagram (Block B -- HERO):** Five sequential boxes representing each washer stage, with flow arrows and chemistry parameters inside each. Top-down flow or left-to-right horizontal layout.
2. **Cleaner chemistry breakdown (Block C):** Callout panel showing alkaline cleaner components and their roles.
3. **Critical control points (Block D):** Oil breakthrough, silicate residues, conductivity monitoring.
4. **Rinse water quality table (Block E):** Conductivity targets for each rinse stage.
5. **Defect grid (Block F):** 6 cleaning-related coating failures.

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
  Stage highlighted: Cleaning (Teal)
ZONE 3 -- 5-STAGE WASHER HERO DIAGRAM (4.2"--15.0" / ~10.8")
ZONE 4 -- CLEANER CHEMISTRY + CRITICAL CONTROLS (15.0"--21.0" / ~6.0")
ZONE 5 -- RINSE WATER QUALITY + VERIFICATION (21.0"--26.5" / ~5.5")
ZONE 6 -- DEFECT GRID -- CLEANING FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- The 5-Stage Spray Washer` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Every contamination molecule left on the surface is a future adhesion failure. Clean it now or strip it later.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Cleaning -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Oily, soiled parts from racking --> After: Clean, conversion-coated surface ready for dry-off`

---

### ZONE 3 -- 5-Stage Washer Hero Diagram

**Section label:** `THE FIVE-STAGE SPRAY TUNNEL -- STAGE BY STAGE` -- Y: 4.4".

**BLOCK B -- Five-Stage Tunnel Diagram**

Y: 5.0" to 14.5". Five large boxes in a single horizontal row, connected by right-pointing arrows.

Each stage box:
- Rounded rectangle, W: 4.3", H: 8.5"
- Fill: `#1E2435`
- Corner radius: 8 pt
- Top accent: 4 pt colored strip

**Stage boxes left to right:**

*Stage 1 -- Alkaline Clean:*
- X: 0.5". Top accent: `#2EC4B6` (Teal)
- Badge: `STAGE 1` on `#2EC4B6`
- Name: `Alkaline Clean`
- Parameters (JetBrains Mono 13 pt):
```
pH 10--12
Concentration: 2--5%
Temp: 120--150 F (49--66 C)
Time: 60--120 sec
```
- Purpose (Inter Regular 13 pt at 70%): `Remove oils, soils, drawing compounds`
- Chemistry note (Inter Medium 12 pt `#2EC4B6`): `NaOH + metasilicate + surfactants + chelants (EDTA, GLDA, citrate)`

*Stage 2 -- Fresh Water Rinse 1:*
- X: 5.1". Top accent: `#C8D0D8` (Silver)
- Badge: `STAGE 2` on `#3A4055`
- Name: `Fresh Water Rinse`
- Parameters:
```
DI or city water
Temp: Ambient
Time: 30--60 sec
```
- Purpose: `Remove cleaner residuals before conversion`
- Control: `Conductivity < 500 uS/cm`

*Stage 3 -- Conversion Coating:*
- X: 9.7". Top accent: `#E8A020` (Amber)
- Badge: `STAGE 3` on `#E8A020`
- Name: `Conversion Coating`
- Parameters:
```
Iron phosphate or zirconium
Temp: 100--140 F (38--60 C)
Time: 60--120 sec
```
- Purpose: `Promote adhesion and corrosion resistance`
- Control: `Coating weight 25--75 mg/ft2 (iron phos)`

*Stage 4 -- Fresh Water Rinse 2:*
- X: 14.3". Top accent: `#C8D0D8` (Silver)
- Badge: `STAGE 4` on `#3A4055`
- Name: `Fresh Water Rinse`
- Parameters:
```
DI or RO water
Temp: Ambient
Time: 30--60 sec
```
- Purpose: `Remove conversion coating residuals`
- Control: `Conductivity < 50 uS/cm (DI preferred)`

*Stage 5 -- Seal Rinse:*
- X: 18.9". Top accent: `#27AE60` (Emerald)
- Badge: `STAGE 5` on `#27AE60`
- Name: `Seal Rinse`
- Parameters:
```
Non-chrome seal (Zr/Ti based)
or DI final rinse
Temp: Ambient
Time: 15--30 sec
```
- Purpose: `Enhance corrosion resistance`
- Control: `Seals porosity in conversion coating`

**Arrows between boxes:**
- Stroke: 3 pt, `#3A4055`. Arrowhead: filled, right.
- Y: centered vertically within boxes.

---

### ZONE 4 -- Cleaner Chemistry + Critical Controls

**Section label:** `ALKALINE CLEANER CHEMISTRY AND CRITICAL CONTROLS` -- Y: 15.2".

**Two-column layout (Y: 15.8" to 20.8"):**

**Left -- Cleaner Components (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `CLEANER COMPONENTS` -- Barlow SemiBold, 18 pt, `#2EC4B6`

| Component | Role |
|---|---|
| Sodium hydroxide (NaOH) | Primary alkalinity source |
| Sodium metasilicate | Detergency + corrosion inhibition |
| Surfactants (nonionic) | Wetting, emulsification of oils |
| EDTA / GLDA / Citrate | Chelate hard water ions (Ca, Mg) |
| Phosphate builders | Buffering + soil suspension |

Table: Header on `#3A4055`, data alternating `#1E2435` / `#252B3D`. JetBrains Mono 12 pt.

Bottom warning (Coral): `Silicate residues from cleaner can cause adhesion failure. Use low-silicate or silicate-free formulations for powder coat pretreatment.`

**Right -- Critical Controls (X: 12.0", W: 11.5"):**

Title: `CRITICAL CONTROL POINTS` -- Barlow SemiBold, 18 pt, `#E8A020`

Three stacked callout cards:

*Oil Breakthrough:*
- Accent: `#E05C5C`
- `Alkaline cleaner oil-loading capacity is finite`
- `Monitor by water-break test (ASTM F22)`
- `Unbroken water film = clean surface`

*Silicate Residues:*
- Accent: `#E05C5C`
- `Insoluble silicate deposits block conversion coating`
- `Cause adhesion failure under powder film`
- `Use silicate-free formulations when possible`

*Conductivity Monitoring:*
- Accent: `#2EC4B6`
- `Rinse water < 200 uS/cm (between stages)`
- `Final DI rinse < 50 uS/cm`
- `High TDS = osmotic blistering under film`

---

### ZONE 5 -- Rinse Water Quality + Verification

**Section label:** `RINSE WATER QUALITY TARGETS` -- Y: 21.2".

**Two-column layout (Y: 21.8" to 26.3"):**

**Left -- Conductivity Table (X: 0.5", W: 11.0"):**

| Rinse Stage | Water Source | Conductivity Target | Risk if Exceeded |
|---|---|---|---|
| After cleaner | City water | < 500 uS/cm | Cleaner carryover |
| After conversion | DI or RO | < 50 uS/cm | Salt deposits, blistering |
| Final seal rinse | DI water | < 50 uS/cm | Osmotic blistering |

Header: Barlow SemiBold 14 pt on `#3A4055`. Data: JetBrains Mono 12 pt.

**Right -- Water-Break Test Panel (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `WATER-BREAK TEST (ASTM F22)` -- Barlow SemiBold, 18 pt, `#27AE60`

Body (Inter Regular 14 pt):
- `Spray clean water onto the part surface`
- `Observe the water film for 30 seconds`
- `PASS: Continuous unbroken water sheet -- surface is clean`
- `FAIL: Water beads up or breaks -- oil/contamination present`

Bottom note: `This is the single most reliable go/no-go test for surface cleanliness. No instrument required.` -- Inter Medium 13 pt `#27AE60`

Counterflow rinse design note:
- `Counterflow Design: Fresh water enters the last rinse tank and overflows backward. Conserves water while maintaining quality at the critical final rinse.` -- Inter Regular 13 pt `#F0EDE8` at 70%

---

### ZONE 6 -- Defect Grid -- Cleaning Failures

**Section label:** `WHEN CLEANING FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | OIL FISH-EYE | `#E05C5C` | Residual oils from inadequate cleaning | Increase cleaner concentration; extend wash time |
| R1C2 | SILICATE HAZE | `#E8A020` | Insoluble silicate deposits from cleaner | Switch to silicate-free formulation |
| R1C3 | OSMOTIC BLISTERING | `#E05C5C` | High TDS rinse water under powder film | Improve DI rinse quality; < 50 uS/cm |
| R2C1 | POOR CONVERSION COATING | `#E8A020` | Cleaner carryover interfering with phosphate | Improve rinse between clean and convert |
| R2C2 | ADHESION LOSS | `#E05C5C` | Contamination passing through wash system | Water-break test after clean stage |
| R2C3 | FLASH RUST | `#2EC4B6` | Excessive dwell time between wash and dry | Minimize queue time; blow off standing water |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

Interior per card:
- Defect: Barlow SemiBold, 14 pt, defect color
- Cause: Inter Regular, 12 pt, `#F0EDE8`
- Fix: Inter Medium, 12 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard. Title: `Cleaning -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references. Specific cleaner formulations and operating parameters vary by supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is all about the 5-stage spray tunnel -- the visual must read as a clear left-to-right flow that a washer operator can follow. The water-break test callout is the single most actionable piece of knowledge on the poster. Silicate residues are the sleeper failure mode -- most operators don't know their cleaner is leaving behind adhesion-killing deposits. The conductivity targets give rinse operators concrete numbers to hit.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #651 -- Construction Workup v1.0*
*2026-04-26*
