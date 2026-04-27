---
Project: Plating Posters Inc
Poster Number: 505
Title: "Parameter Setup -- Flame Spray"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Thermal Spray Clusters -- Watson Research Brief (Cluster 3: Flame Spray)"
Process Scope: Flame spray parameter setup -- wire vs. powder settings, gas pressures, standoff, spray angle
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ThermalSpray
  - FlameSpray
  - Parameters
  - ConstructionWorkup
  - ClusterTS03
---

# Poster #505 -- Construction Workup
## Parameter Setup -- Flame Spray

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Parameter setup for flame spray -- the poster that turns a lit gun into a dialed-in spray system. The hero is a side-by-side parameter table comparing wire and powder variants. Key message: flame spray parameters are simpler than plasma or HVOF, but getting the standoff, angle, and feed rate wrong still ruins coatings. Test on a coupon before you touch the part.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Parameter comparison table (Block B -- HERO):** Large two-column table -- wire flame spray vs. powder flame spray -- with all key settings.
2. **Flame type visual (Block C):** Simplified diagram showing neutral flame profile with labeled zones (inner cone, outer envelope).
3. **Standoff and angle guide (Block D):** Visual showing effect of distance and angle on coating quality.
4. **Test coupon checklist (Block E):** Pre-production validation sequence.
5. **Common parameter errors strip (Block F):** 4 cards -- wrong setting, what happens, how to fix.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber)
ZONE 3 -- PARAMETER TABLE / HERO (4.2"--15.5" / ~11.3")
  Block B: Wire vs. Powder parameter comparison table
  Block C: Neutral flame diagram
ZONE 4 -- STANDOFF AND ANGLE GUIDE (15.5"--22.0" / ~6.5")
  Block D: Distance and angle effect diagrams
ZONE 5 -- TEST COUPON CHECKLIST (22.0"--28.5" / ~6.5")
  Block E: 6-step pre-production validation
ZONE 6 -- COMMON PARAMETER ERRORS (28.5"--32.5" / ~4.0")
  Block F: 4 error cards
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PARAMETER SETUP` -- 88 pt `#F0EDE8`.
**Subheading:** `Flame Spray -- Wire & Powder Operating Parameters` -- 36 pt `#E8A020` (Amber).
**Tagline:** `Same gun, two feedstock paths, different dial-in points. Get the parameters right on a test coupon before you commit to the part.` -- 22 pt `#F0EDE8` at 65%.

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Gun lit and stable, feedstock loaded --> After: Spray pattern verified on test coupon, ready for production`

---

### ZONE 3 -- Parameter Table (HERO)

**Section label:** `WIRE VS. POWDER -- OPERATING PARAMETERS` -- Y: 4.4".

**BLOCK B -- Side-by-Side Parameter Table**

Y: 5.0" to 13.5". Full width within margins (23.0").

Two-column comparison format. Left column header: `WIRE FLAME SPRAY` in Barlow SemiBold 20 pt `#27AE60`. Right column header: `POWDER FLAME SPRAY` in Barlow SemiBold 20 pt `#E8A020`.

| Parameter | Wire Flame Spray | Powder Flame Spray |
|---|---|---|
| Oxygen pressure | 20--40 PSI | 15--30 PSI |
| Fuel (acetylene) pressure | 10--15 PSI | 10--15 PSI |
| Compressed air pressure | 40--80 PSI (atomizing) | 20--40 PSI (carrier gas) |
| Wire feed rate | 1--8 m/min | N/A |
| Powder feed rate | N/A | 20--60 g/min |
| Flame temperature | ~3,100 degC (oxy-acetylene) | ~3,100 degC (oxy-acetylene) |
| Particle velocity | 80--200 m/s | 40--100 m/s |
| Standoff distance | 150--250 mm (6--10 in) | 150--300 mm (6--12 in) |
| Spray angle | 60--90 degrees | 60--90 degrees |
| Deposition rate | 2--8 kg/hr | 1--4 kg/hr |
| Deposition efficiency | 50--70% | 30--50% |

Table header row: fill `#3A4055`, H: 0.5". Barlow SemiBold, 14 pt, `#F0EDE8`.
Data rows: alternating `#1E2435` / `#252B3D`, H: 0.55".
Parameter names: Inter Medium 13 pt `#F0EDE8`. Values: JetBrains Mono Regular 13 pt `#F0EDE8`.
Acetylene row: full row highlighted with `#E05C5C` at 15% fill.

Below table -- acetylene warning:
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- `REMINDER: Acetylene NEVER exceeds 15 PSI. This is a hard ceiling -- not a suggestion.` Inter Medium 14 pt `#E05C5C`.

**BLOCK C -- Neutral Flame Diagram**

Y: 13.8" to 15.3". Centered, W: 16.0".

Simplified flame profile built from overlapping rounded rectangles:
- Outer envelope: W: 12.0", H: 1.2", fill `#E8A020` at 20%, border 1 pt `#E8A020`
- Inner cone: W: 3.5", H: 0.8", fill `#E8A020` at 40%, border 1 pt `#E8A020`
- Labels with callout lines:
  - `Inner cone (hottest zone)` -- Inter Medium 12 pt `#E8A020`
  - `Outer envelope (reducing)` -- Inter Medium 12 pt `#F0EDE8` at 70%
  - `Feedstock injection point` -- Inter Medium 12 pt `#2EC4B6`
- Caption: `Neutral flame: equal inner cones, no acetylene feather. This is your target.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 4 -- Standoff and Angle Guide

**Section label:** `STANDOFF DISTANCE & SPRAY ANGLE` -- Y: 15.7".

**BLOCK D -- Distance and Angle Effects**

Y: 16.3" to 21.5". Two panels side by side.

**Left Panel -- Standoff Distance (X: 0.5", W: 11.0"):**

Title: `STANDOFF DISTANCE` Barlow SemiBold 18 pt `#2EC4B6`.

Three horizontal bars representing standoff ranges:

| Range | Label | Effect |
|---|---|---|
| Too close (<150 mm) | `#E05C5C` fill at 20% | Substrate overheating; coating stress; spatter buildup |
| Optimal (150--250 mm wire / 150--300 mm powder) | `#27AE60` fill at 20% | Best density and adhesion; smooth deposit |
| Too far (>300 mm) | `#E05C5C` fill at 20% | High porosity; poor adhesion; cold particles |

Labels: Inter Medium 13 pt. Effects: Inter Regular 12 pt `#F0EDE8` at 70%.

**Right Panel -- Spray Angle (X: 12.0", W: 11.5"):**

Title: `SPRAY ANGLE` Barlow SemiBold 18 pt `#E8A020`.

| Angle | Label | Effect |
|---|---|---|
| 90 degrees (perpendicular) | `#27AE60` fill at 20% | Maximum density and bond strength |
| 60--75 degrees | `#E8A020` fill at 15% | Acceptable; slight porosity increase |
| <45 degrees | `#E05C5C` fill at 20% | Shadowing; severe porosity; poor adhesion -- avoid |

Below both panels:
- Callout: `Flame spray is more sensitive to standoff and angle than HVOF because particle velocity is lower -- there is less kinetic energy to overcome poor geometry.` Inter Regular 13 pt `#F0EDE8` at 60%.

---

### ZONE 5 -- Test Coupon Checklist

**Section label:** `PRE-PRODUCTION TEST COUPON SEQUENCE` -- Y: 22.2".

**BLOCK E -- 6-Step Checklist**

Y: 22.8" to 28.3". Two columns of 3 steps each.

| Step | Action | Verify |
|---|---|---|
| 1 | Select test coupon -- same substrate material and thickness as production part | Match alloy and heat-treat condition |
| 2 | Grit blast coupon to same profile spec as production | Ra 4--12 um; SSPC-SP 5 or SP 10 |
| 3 | Spray one pass at production parameters | Observe spray pattern, adhesion, no spitting |
| 4 | Measure thickness per pass with mag gauge or eddy current | Record microns per pass for planning |
| 5 | Build to target thickness on second coupon | Verify total thickness and visual quality |
| 6 | Bend test or adhesion spot-check if specification requires | Document results before production spray |

Step numbers: Barlow Condensed ExtraBold 22 pt `#2EC4B6`. Action: Inter Regular 14 pt. Verify: JetBrains Mono 12 pt `#27AE60`.

---

### ZONE 6 -- Common Parameter Errors

**Section label:** `COMMON PARAMETER ERRORS` -- Y: 28.7".

Four cards, W: 5.5", H: 2.5", left accent `#E05C5C`.

| Card | X | Error | Result | Fix |
|---|---|---|---|---|
| 1 | 0.5" | WIRE FEED TOO FAST | Spitting, unmelted particles in coating | Reduce feed rate until spray pattern is smooth and uniform |
| 2 | 6.33" | STANDOFF TOO FAR | Porous, poorly bonded coating; powdery texture | Move closer -- 150--250 mm for wire, 150--300 mm for powder |
| 3 | 12.16" | OXIDIZING FLAME | Excessive oxide content; brittle deposit | Adjust to neutral flame -- equal inner cones, no excess O2 |
| 4 | 18.0" | AIR PRESSURE TOO LOW (WIRE) | Coarse droplets; rough, porous coating | Increase atomizing air to 40--80 PSI; verify air supply CFM |

Interior per card:
- Error: Barlow SemiBold, 16 pt, `#E05C5C`
- Result: Inter Regular, 13 pt, `#F0EDE8`
- Fix: Inter Medium, 13 pt, `#27AE60`

---

### ZONE 7 -- Footer

Standard footer. Title: `Parameter Setup -- Flame Spray`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASM Handbook Vol 5A; general industry knowledge. Parameters shown are typical ranges -- always verify against your equipment OEM documentation and coating specification.`

---

## Parts 5--7

**Grouping:** 7 zones. **Light Remap:** Standard. **Export:** Six files.

---

*Alaina -- Poster #505 -- Construction Workup v1.0 -- 2026-04-26*
