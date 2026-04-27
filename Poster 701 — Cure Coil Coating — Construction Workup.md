---
Project: Plating Posters Inc
Poster Number: 701
Title: "Cure -- Coil Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting Coating Clusters -- Watson Research Brief (Cluster 6: Coil Coating, Section 6.8)"
Process Scope: Cure (oven + quench) for coil coating -- Stages 7 and 9 of 9
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - CoilCoating
  - Cure
  - ConstructionWorkup
  - PaintingCoating
  - ClusterCC
---

# Poster #701 -- Construction Workup
## Cure -- Coil Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stages 7 and 9 of 9 -- prime oven and finish oven. The fastest cure in all of industrial painting: 15-60 seconds at PMT. The strip is thin gauge (0.015-0.060 inch), so it heats fast. The cure window is defined by Peak Metal Temperature, not oven air temperature -- and at 200-700 ft/min, every degree and every second matters. Water quench immediately after the oven locks in film properties and prevents overcure. Afterburners on the oven exhaust destroy the solvent vapors.

Hero visual: oven profile diagram showing oven temperature zones, PMT ramp curve, and quench, with the primer oven and finish oven shown as paired units.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual oven profile hero (Block B):** Primer oven and finish oven shown side by side with PMT curves and quench zones.
2. **Oven parameters table (Block D):** Primer vs. finish oven specifications.
3. **PMT measurement and VOC emissions panel (Block E):** IR pyrometer monitoring and afterburner requirements.
4. **Defect strip (Block F):** 4 cure-related defects.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stages 7 + 9 highlighted (Emerald)
ZONE 3 -- DUAL OVEN PROFILE HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- OVEN PARAMETERS TABLE (14.5"--20.5" / ~6.0")
ZONE 5 -- PMT MONITORING + VOC EMISSIONS (20.5"--26.5" / ~6.0")
ZONE 6 -- CURE DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Coil Coating -- Stages 7 + 9: Prime Oven & Finish Oven` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `Fifteen to sixty seconds. PMT 400-480 F. Water quench. The fastest cure cycle in the painting world -- and the strip never stops moving.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stages 7 and 9 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet-coated strip from roll coater  -->  After: Fully cured, quenched strip ready for recoil`

---

### ZONE 3 -- Dual Oven Profile Hero

**Section label:** `TWO OVENS, TWO QUENCHES -- PRIMER AND FINISH` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Dual Oven Diagram (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#27AE60`.

**Strip path (horizontal, Y: 6.5"):** `#C8D0D8` 3 pt line, arrow `STRIP -->`.

**Left half -- Primer Oven (X: 0.5", W: 11.0"):**

Oven box (Y: 5.5" to 10.0"):
- Rounded rect, fill `#27AE60` at 10%, border `#27AE60` dashed
- Label: `PRIMER OVEN` Barlow SemiBold 18 pt `#27AE60`
- Heat wave icons inside

PMT curve overlay (inside oven box):
- Rising line from left to right, `#E8A020` 2 pt
- Start: `AMBIENT` label
- Peak: `PMT 400-450 F` JetBrains Mono 14 pt `#E8A020`
- Duration: `15-40 sec` JetBrains Mono 12 pt `#F0EDE8`

Quench zone (immediately after oven, X: 8.5"):
- Blue zone, fill `#2EC4B6` at 15%, border `#2EC4B6`
- Label: `WATER QUENCH` Barlow SemiBold 12 pt `#2EC4B6`
- `Cool to ambient` JetBrains Mono 11 pt

**Right half -- Finish Oven (X: 12.0", W: 11.0"):**

Same structure:
- Label: `FINISH OVEN` Barlow SemiBold 18 pt `#27AE60`
- PMT: `PMT 430-480 F` JetBrains Mono 14 pt `#E8A020`
- Duration: `20-60 sec`
- Quench: same as primer oven
- After quench: `TO RECOILER` label

**Oven length annotations:**
- Primer: `80-150 ft oven length` JetBrains Mono 11 pt `#F0EDE8` at 60%
- Finish: `100-200 ft oven length`

Bottom callout (Y: 12.5"):
- `The strip passes through two complete oven-quench cycles: once after prime coat, once after finish coat. Total time from wet primer to cured finish coat: 90-180 seconds at line speed.` Inter Regular 13 pt `#F0EDE8`

---

### ZONE 4 -- Oven Parameters Table

**Section label:** `PRIMER OVEN vs. FINISH OVEN` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Comparison Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Parameter (5.0") | Primer Oven (Stage 7) (9.0") | Finish Oven (Stage 9) (9.0")

| Parameter | Primer Oven (Stage 7) | Finish Oven (Stage 9) |
|---|---|---|
| Peak Metal Temperature (PMT) | 400-450 F (204-232 C) | 430-480 F (221-249 C) |
| Oven length | 80-150 ft | 100-200 ft |
| Residence time in oven | 15-40 sec | 20-60 sec |
| Oven type | Gas-fired convection | Gas-fired convection |
| Afterburner | Thermal or catalytic oxidizer | Thermal or catalytic oxidizer |
| Quench | Water quench to ambient | Water quench to ambient |
| Cure verification | MEK rub 100+ double rubs | MEK rub 100+ double rubs |
| PMT measurement | In-line IR pyrometer (continuous) | In-line IR pyrometer (continuous) |

Data: JetBrains Mono Regular, 12 pt, `#F0EDE8`.

**Critical distinction callout (Y: 19.5"):**
- Fill `#252B3D`, left accent `#E05C5C` 0.06"
- Text: `PMT = PEAK METAL TEMPERATURE, not oven air temperature. The oven air may be 50-100 F hotter than the strip. PMT is always the specification parameter. Measure by in-line IR pyrometer or thermocouple data logger on test strips.` Inter Medium 13 pt `#E05C5C`

---

### ZONE 5 -- PMT Monitoring + VOC Emissions

**Section label:** `MONITORING AND EMISSIONS` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Panel**

Y: 21.3" to 26.3".

**Left -- PMT Monitoring (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `PMT MEASUREMENT` -- Barlow SemiBold, 18 pt, `#E8A020`

| Method | Use | Notes |
|---|---|---|
| In-line IR pyrometer | Continuous production monitoring | Non-contact; measures strip temp at oven exit |
| Thermocouple data logger | Periodic oven profiling | Attached to test strips; maps temp vs. time through oven |
| Contact thermocouple | Spot checks | Slower but verifies IR pyrometer accuracy |

JetBrains Mono 11 pt `#F0EDE8`.

Note: `Profile the oven whenever line speed, gauge, or coating changes. A speed reduction of 50 ft/min can increase PMT by 20-40 F and overcure the coating.` Inter Regular 12 pt `#E8A020`.

**Right -- VOC Emissions (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `SOLVENT EMISSIONS AND AFTERBURNERS` -- Barlow SemiBold, 18 pt, `#E05C5C`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Coil coatings are typically 50-70% volume solids -- significant solvent content`
- `Solvent vapors released during cure must be captured and destroyed`
- `Thermal oxidizer: 1,400-1,600 F, > 95% VOC destruction`
- `Catalytic oxidizer: 600-800 F, > 95% VOC destruction`
- `EPA 40 CFR Part 63, Subpart SSSS governs metal coil coating emissions`
- `The oven acts as the emission enclosure -- total capture + destruction > 95%`

Regulation callout: `NESHAP Subpart SSSS: Surface Coating of Metal Coil` JetBrains Mono 11 pt `#E05C5C`.

---

### ZONE 6 -- Cure Defects

**Section label:** `WHAT GOES WRONG -- 4 CURE DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | UNDERCURE (MEK RUB FAILS) | PMT too low or residence time too short | Increase oven zone temps; reduce line speed; verify IR pyrometer calibration |
| 2 | 6.33" | OVERCURE (BRITTLE / YELLOWING) | PMT too high -- often from line speed reduction without oven adjustment | Interlock oven temp to line speed; profile after every speed change |
| 3 | 12.16" | FORMING CRACK AFTER CURE | Over-crosslinked film lost flexibility (overcure) or wrong chemistry | Verify T-bend per spec; check PMT history; switch to higher-flexibility chemistry |
| 4 | 18.0" | BLISTERING AFTER QUENCH | Residual moisture under coating or solvent entrapment | Verify pre-dry stage; check for upstream rinse water carryover |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `The most dangerous moment on a coil coating line is a speed reduction. When the line slows down, the strip spends more time in the oven, and PMT rises. Without an automatic oven-to-speed interlock, a 50% speed reduction can overcure the coating and embrittle it -- and you will not know until the fabricator tries to bend it.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Coil Coating`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Coil Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-oven hero makes it clear that coil coating runs two complete cure cycles -- primer and finish -- in rapid succession. The PMT distinction callout is repeated from other cure posters because it is the single most common source of cure errors across all painting processes. The speed-reduction danger callout is the real-world wisdom: every coil coater has learned this lesson the hard way. Overcure from a line slowdown is invisible until the forming failure happens downstream at the fabricator's plant.

---

*Alaina -- Poster #701 -- Construction Workup v1.0 -- 2026-04-26*
