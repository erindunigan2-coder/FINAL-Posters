---
Project: Plating Posters Inc
Poster Number: 656
Title: "Cure -- Powder Coating"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Painting & Organic Coating Clusters — Watson Research Brief, Cluster 1.8"
Technical Source: Industry-standard cure parameters for thermoset powder coating. Covers cure temperatures and times for all major powder chemistries, oven types, the critical distinction between oven air temperature and metal temperature, MEK rub cure verification, and undercure vs. overcure failure modes.
Process Scope: Cure oven operation for powder coating (Stage 7 of 9)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - PowderCoating
  - Cure
  - ConstructionWorkup
  - PaintingClusters
  - ClusterPC01
---

# Poster #656 -- Construction Workup
## Cure -- Powder Coating

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 9. The cure oven is where chemistry becomes coating. The hero table is a cure schedule matrix for all six major powder chemistries. The single most important concept: the cure window is defined by METAL temperature, not oven air temperature. A heavy steel part at 375 F oven air is not at 375 F metal temp until the thermal mass catches up. Oven profiling with data loggers is the only way to verify.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cure schedule matrix (Block B -- HERO):** Table showing cure temp and time for all 6 major powder chemistries plus low-temp formulations.
2. **Metal temp vs. oven temp callout (Block C):** The critical distinction with data logger illustration.
3. **Oven types comparison (Block D):** Convection, IR, combination.
4. **MEK rub test panel (Block E):** Cure verification procedure.
5. **Undercure vs. overcure comparison (Block F):** Side-by-side failure modes.
6. **Defect grid (Block G):** 6 cure-related failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 13.5" / 19.5" / 25.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage highlighted: Cure (Amber)
ZONE 3 -- CURE SCHEDULE MATRIX HERO (4.2"--13.5" / ~9.3")
ZONE 4 -- METAL TEMP vs OVEN TEMP + OVEN TYPES (13.5"--19.5" / ~6.0")
ZONE 5 -- MEK RUB TEST + UNDERCURE vs OVERCURE (19.5"--25.0" / ~5.5")
ZONE 6 -- DEFECT GRID (25.0"--28.5" / ~3.5")
ZONE 7 -- FOOTER BAND (28.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 80 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Powder Coating -- Where Chemistry Becomes Coating` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `Metal temperature, not oven air temperature. That distinction has saved more jobs than any other single piece of knowledge in powder coating.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage highlighted: Cure -- fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Dry powder layer on pretreated surface --> After: Fully cross-linked thermoset film`

---

### ZONE 3 -- Cure Schedule Matrix Hero

**Section label:** `CURE SCHEDULES BY POWDER CHEMISTRY` -- Y: 4.4".

**BLOCK B -- Cure Matrix Table**

Y: 5.0" to 13.0". Full-width table.

| Chemistry | Cure Temp (Metal) | Cure Time at Temp | Cross-Linker | Notes |
|---|---|---|---|---|
| Epoxy | 350--400 F (177--204 C) | 10--20 min | Dicyandiamide (DICY) or phenolic | Standard cure; interior only (chalks in UV) |
| Hybrid (Epoxy-Polyester) | 350--375 F (177--191 C) | 10--15 min | Epoxy resin cross-links polyester | Indoor/mild outdoor; general industrial |
| Polyester-TGIC | 375--400 F (191--204 C) | 10--15 min | Triglycidyl isocyanurate | Excellent UV durability; architectural |
| Polyester-HAA | 375--400 F (191--204 C) | 10--15 min | Hydroxyalkylamide (Primid) | TGIC-free; emits water during cure |
| Polyurethane | 350--400 F (177--204 C) | 15--25 min | Blocked isocyanate (caprolactam/IPDI) | Unblocks at ~320 F; high-appearance |
| Acrylic | 325--375 F (163--191 C) | 15--20 min | GMA-functional acrylic + diacid | Lower cure temp; auto clearcoat |
| Low-Temp Formulations | 250--300 F (121--149 C) | 15--30 min | Various | Heat-sensitive substrates (MDF, plastics) |

Header: Barlow SemiBold 14 pt `#F0EDE8` on `#3A4055`. Data: JetBrains Mono 12 pt. Chemistry names: Inter Medium 13 pt in accent colors.

Color-code chemistry names:
- Epoxy: `#E05C5C` (interior-only flag)
- Hybrid: `#E8A020`
- TGIC/HAA: `#27AE60` (outdoor-rated)
- Urethane/Acrylic: `#2EC4B6`
- Low-temp: `#C8D0D8`

---

### ZONE 4 -- Metal Temp vs. Oven Temp + Oven Types

**Section label:** `THE MOST IMPORTANT DISTINCTION IN POWDER CURE` -- Y: 13.7".

**Two-column layout (Y: 14.3" to 19.3"):**

**Left -- Metal vs. Oven Temp (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, border 2 pt `#E05C5C`.
Title: `METAL TEMPERATURE -- NOT OVEN AIR TEMPERATURE` -- Barlow SemiBold, 18 pt, `#E05C5C`

Body (Inter Regular 14 pt):
- `The cure window is ALWAYS defined by metal temperature.`
- `A large steel part may require 30+ minutes of oven time to reach 375 F metal temperature, even when oven air is at 400 F.`
- `Thin parts reach metal temp quickly; heavy parts lag significantly.`

Data logger callout (JetBrains Mono 13 pt `#E8A020`):
- `OVEN PROFILING:`
- `Attach thermocouple data loggers (Datapaq, ECD)`
- `Map actual metal temp vs. time through oven`
- `Cure window = integral of time at or above minimum cure temp`

Bottom warning: `Running cure schedule by oven air temp alone guarantees undercure on heavy parts and overcure on thin parts -- simultaneously, in the same oven load.` -- Inter Medium 13 pt `#E05C5C`

**Right -- Oven Types (X: 12.0", W: 11.5"):**

Title: `OVEN TYPES` -- Barlow SemiBold, 18 pt, `#F0EDE8`

Three stacked cards:

*Convection (Most Common):*
- Accent: `#E8A020`
- `Gas-fired or electric with recirculating fans`
- `Even heat distribution critical`
- `Handles mixed part sizes`
- `Most forgiving for complex loads`

*Infrared (IR):*
- Accent: `#2EC4B6`
- `Rapid heat-up; high energy density`
- `Good for thin, uniform parts (panels, sheet)`
- `Poor penetration into recesses or heavy parts`
- `Line-of-sight heating only`

*IR + Convection Combination:*
- Accent: `#27AE60`
- `IR zone for fast gel/melt (first phase)`
- `Convection zone for complete cure (final phase)`
- `Best of both: speed + uniformity`

---

### ZONE 5 -- MEK Rub Test + Undercure vs. Overcure

**Section label:** `CURE VERIFICATION AND FAILURE MODES` -- Y: 19.7".

**Two-column layout (Y: 20.3" to 24.8"):**

**Left -- MEK Rub Test (X: 0.5", W: 11.0"):**

Callout box, fill `#1E2435`, left accent `#27AE60`.
Title: `MEK DOUBLE RUB TEST (ASTM D4752)` -- Barlow SemiBold, 18 pt, `#27AE60`

Procedure (Inter Regular 14 pt):
1. `Soak cloth pad with methyl ethyl ketone (MEK)`
2. `Rub surface with 2 lb pressure`
3. `Count double rubs (back-and-forth = 1 double rub)`
4. `Evaluate: softening, color transfer, film breakthrough`

Pass criteria (JetBrains Mono 14 pt `#27AE60`):
- `50+ double rubs with no softening = FULLY CURED`
- `< 50 double rubs = UNDERCURED -- investigate oven profile`

**Right -- Undercure vs. Overcure (X: 12.0", W: 11.5"):**

Title: `TWO WAYS TO FAIL` -- Barlow SemiBold, 18 pt, `#F0EDE8`

*Undercure:*
- Accent: `#E05C5C`
- `Film remains soft`
- `Poor chemical resistance`
- `Poor adhesion`
- `Low hardness (fails pencil test)`
- `MEK rub: dissolves in < 50 rubs`
- `FIX: Increase metal temp or time`

*Overcure:*
- Accent: `#E8A020`
- `Film yellows (especially epoxy)`
- `Becomes brittle`
- `Loses flexibility and impact resistance`
- `Wastes energy`
- `MEK rub: passes, but mandrel bend fails`
- `FIX: Reduce temp or time; oven profile`

---

### ZONE 6 -- Defect Grid

**Section label:** `WHEN CURE FAILS -- 6 COATING DEFECTS` -- Y: 25.2".

**BLOCK G -- 3x2 Grid (Y: 25.7" to 28.3")**

| Position | Defect | Color | Cause | Fix |
|---|---|---|---|---|
| R1C1 | SOFT FILM / MEK FAIL | `#E05C5C` | Undercure (insufficient metal temp or time) | Oven profile; increase cure schedule |
| R1C2 | YELLOWING | `#E8A020` | Overcure or wrong chemistry for bake schedule | Reduce time/temp; verify powder chemistry |
| R1C3 | POOR ADHESION | `#E05C5C` | Undercure or overbake embrittlement | MEK rub to diagnose; adjust cure |
| R2C1 | BRITTLENESS / CRACKING | `#E8A020` | Overcure destroying film flexibility | Mandrel bend test; reduce cure schedule |
| R2C2 | OUTGASSING (LATE) | `#E05C5C` | Substrate gases escaping during cure | Pre-bake substrate before powder application |
| R2C3 | UNEVEN GLOSS | `#2EC4B6` | Temperature variation across oven load | Improve oven air circulation; profile uniformity |

Each card: Rounded rect W: 7.33", H: 1.2", fill `#1E2435`, radius 4, left accent 0.06" in defect color.

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Powder Coating`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; Powder Coating Institute references; ASTM D4752. Cure schedules are powder-formulation-specific -- always verify with your powder manufacturer's Technical Data Sheet.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Powder Coating -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cure schedule matrix is the wall reference -- an operator glances up and sees the exact temp and time for their powder chemistry. The metal-temp-vs-oven-temp callout box with its red border is the visual alarm: this is the #1 mistake in powder coating. The MEK rub test panel gives every quality tech a concrete pass/fail procedure. Undercure vs. overcure side-by-side is the diagnostic tool -- "is my film soft or brittle?" determines which direction to adjust.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #656 -- Construction Workup v1.0*
*2026-04-26*
