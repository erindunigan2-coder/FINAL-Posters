---
Project: Plating Posters Inc
Poster Number: 652
Title: "Rinse / Dry -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.4"
Technical Source: Industry-standard rinse quality and dry-off oven parameters for powder coating. Covers counterflow rinse design, DI water requirements, dry-off oven temperature/time, air knife blow-off, and the critical cooling requirement before powder application.
Process Scope: Rinse and dry-off for powder coating (Stage 3 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - RinseDry
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #652 -- Construction Workup
## Rinse / Dry -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 9. The transition zone between wet chemistry and dry powder application. Rinse quality determines what salts remain on the surface -- and the dry-off oven must remove every molecule of moisture. Residual moisture causes blistering during cure. The critical twist: parts must then cool to below 90 F before entering the powder booth, or the powder deposits unevenly. Hot parts are as bad as wet parts.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse-to-dry flow diagram (Block B -- HERO):** Shows the sequence from final conversion rinse through dry-off oven to cool-down zone. Three main phases with parameters.
2. **Rinse quality table (Block C):** Conductivity targets by rinse position.
3. **Dry-off oven parameters (Block D):** Temperature, time, air knife options.
4. **Cool-down critical callout (Block E):** The 90 F threshold and why it matters.
5. **Defect grid (Block F):** 6 rinse/dry-related failures.

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
  Stage highlighted: Rinse / Dry (Teal)
ZONE 3 -- RINSE-TO-DRY FLOW HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- RINSE QUALITY + COUNTERFLOW DESIGN (14.5"--20.5" / ~6.0")
ZONE 5 -- DRY-OFF OVEN + COOL-DOWN CRITICAL (20.5"--26.5" / ~6.0")
ZONE 6 -- DEFECT GRID -- RINSE/DRY FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- From Wet Chemistry to Dry Application` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Moisture is the enemy of powder coating. Every drop left behind becomes a blister during cure.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Rinse / Dry -- fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Conversion-coated wet surface --> After: Bone-dry, cooled part ready for powder booth`

---

### ZONE 3 -- Rinse-to-Dry Flow Hero

**Section label:** `THE TRANSITION -- RINSE, DRY, COOL` -- Y: 4.4".

**BLOCK B -- Three-Phase Flow Diagram**

Y: 5.0" to 14.0". Three large boxes in a horizontal row connected by right-pointing arrows.

*Phase 1 -- Rinse Stages:*
- X: 0.5", W: 7.0", H: 8.5"
- Fill: `#1E2435`, top accent `#2EC4B6`
- Title: `RINSE STAGES` -- Barlow SemiBold, 22 pt, `#2EC4B6`
- Content (JetBrains Mono 13 pt):
```
Between clean & convert:
  City water, < 500 uS/cm

After conversion coating:
  DI or RO water, < 50 uS/cm

Counterflow design:
  Fresh water enters last tank
  Overflows backward to conserve
```
- Key metric (Inter Medium 14 pt `#E8A020`): `Final rinse conductivity < 50 uS/cm -- non-negotiable`

*Phase 2 -- Dry-Off Oven:*
- X: 8.0", W: 7.0", H: 8.5"
- Fill: `#1E2435`, top accent `#E8A020`
- Title: `DRY-OFF OVEN` -- Barlow SemiBold, 22 pt, `#E8A020`
- Content:
```
Temperature: 250--300 F (121--149 C)
Time: 10--15 min at metal temp
Heavier parts: longer soak needed

Air knife (optional):
  Blow-off before oven entry
  Removes standing water from recesses
  Reduces dry time, prevents spots
```
- Critical (Inter Medium 14 pt `#E05C5C`): `MUST be bone dry. Any residual moisture = blistering in cure oven.`

*Phase 3 -- Cool Down:*
- X: 15.5", W: 7.5", H: 8.5"
- Fill: `#1E2435`, top accent `#27AE60`
- Title: `COOL DOWN` -- Barlow SemiBold, 22 pt, `#27AE60`
- Content:
```
Target: < 90 F (32 C)
Method: Ambient air or forced cooling
Time: Until part temperature verified

WHY THIS MATTERS:
Hot parts attract powder unevenly
  - Thick at edges
  - Thin at centers
  - Poor appearance
```
- Exception note (Inter Regular 13 pt `#F0EDE8` at 70%): `Exception: "Hot flocking" for thermoplastic powders intentionally uses preheated parts (400--500 F).`

---

### ZONE 4 -- Rinse Quality + Counterflow Design

**Section label:** `RINSE WATER QUALITY -- THE HIDDEN VARIABLE` -- Y: 14.7".

**Two-column layout (Y: 15.3" to 20.3"):**

**Left -- Conductivity Table (X: 0.5", W: 11.0"):**

| Rinse Position | Water Source | Max Conductivity | Consequence if Exceeded |
|---|---|---|---|
| After alkaline clean | City water | 500 uS/cm | Cleaner residuals on surface |
| After conversion coating | DI or RO | 50 uS/cm | Salt deposits cause blistering |
| Final rinse before dry | DI water | 50 uS/cm | Osmotic blistering under film |

Header: Barlow SemiBold 14 pt on `#3A4055`. Data: JetBrains Mono 12 pt.

Bottom note: `Conductivity is measured with a handheld meter. Check daily at minimum -- weekly is not enough.` -- Inter Medium 13 pt `#E8A020`.

**Right -- Counterflow Rinse Diagram (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, left accent `#2EC4B6`.
Title: `COUNTERFLOW RINSE DESIGN` -- Barlow SemiBold, 18 pt, `#2EC4B6`

Simplified flow diagram (built with rectangles and arrows):
- Three tanks labeled `RINSE 1`, `RINSE 2`, `RINSE 3`
- Arrow from FRESH DI WATER entering Rinse 3
- Overflow arrow from Rinse 3 to Rinse 2
- Overflow arrow from Rinse 2 to Rinse 1
- Drain arrow from Rinse 1 to WASTE

Benefit note: `Cleanest water contacts cleanest parts. Saves 50--70% water vs. independent rinses.` -- Inter Medium 13 pt `#27AE60`

---

### ZONE 5 -- Dry-Off Oven + Cool-Down Critical

**Section label:** `DRY-OFF OVEN PARAMETERS AND COOLING` -- Y: 20.7".

**Two-column layout (Y: 21.3" to 26.3"):**

**Left -- Oven Parameters (X: 0.5", W: 11.0"):**

| Parameter | Value | Notes |
|---|---|---|
| Temperature | 250--300 F (121--149 C) | Gas-fired or electric convection |
| Time at metal temp | 10--15 min | Heavier parts need longer |
| Air circulation | Recirculating fans | Even heat distribution critical |
| Air knife (pre-oven) | Compressed air blow-off | Removes standing water from recesses |

**Right -- Cool-Down Panel (X: 12.0", W: 11.5"):**

Callout box, fill `#1E2435`, border 1 pt `#E05C5C` at 30%.
Title: `THE 90 F RULE` -- Barlow SemiBold, 22 pt, `#E05C5C`

Body (Inter Regular 14 pt):
```
Parts MUST cool to below 90 F (32 C)
before entering the powder booth.

Hot parts cause:
  - Premature powder melt on contact
  - Thick edges, thin centers
  - Inconsistent DFT
  - Orange peel and poor leveling

Verify with contact thermometer
or IR gun before powder booth entry.
```

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN RINSE OR DRY FAILS -- 6 COATING DEFECTS` -- Y: 26.7".

**BLOCK F -- 3x2 Grid (Y: 27.3" to 32.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | OSMOTIC BLISTERING | `#E05C5C` | High TDS rinse water trapped under film | Improve DI rinse; < 50 uS/cm final |
| R1C2 | WATER SPOT STAINING | `#E8A020` | Standing water evaporating and leaving mineral deposits | Air knife blow-off before oven |
| R1C3 | MOISTURE BLISTERING | `#E05C5C` | Incomplete drying before powder application | Extend dry-off time; check metal temp |
| R2C1 | UNEVEN DFT | `#E8A020` | Hot parts entering powder booth (> 90 F) | Cool parts before application |
| R2C2 | FLASH RUST | `#E05C5C` | Excessive queue time between rinse and dry | Minimize dwell; maintain line speed |
| R2C3 | POOR ADHESION | `#2EC4B6` | Rinse water contamination on conversion coating | Monitor rinse conductivity daily |

Each card: Rounded rect W: 7.33", H: 2.3", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-phase hero is the visual anchor: rinse, dry, cool. The 90 F cool-down rule is the most commonly violated step on powder lines -- operators rush parts from the dry-off oven straight to the booth. The counterflow rinse diagram is a simple but powerful visual that explains water conservation in one glance. Conductivity numbers are the concrete takeaway -- give the operator a number, not a concept.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #652 -- Construction Workup v1.0*
*2026-04-26*
