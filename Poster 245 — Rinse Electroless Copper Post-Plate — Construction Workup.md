---
Project: Plating Posters Inc
Poster Number: 245
Title: "Rinse (Post-Plate) -- Electroless Copper"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Electroless Clusters -- Watson Research Brief (Process 4: Electroless Copper, Poster 7)"
Technical Source: Post-plate rinse for electroless copper. Covers removal of alkaline E-Cu bath chemistry, rapid oxidation risk of freshly plated copper, anti-tarnish options, and the urgency of proceeding immediately to the next process step (electrolytic copper or anti-tarnish). Double counterflow rinse at ambient temperature.
Process Scope: Electroless copper -- Stage 7 of 8 (rinse post-plate)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ElectrolessCopper
  - Rinse
  - PostPlate
  - ConstructionWorkup
  - Series2
  - ClusterEL-Cu
---

# Poster #245 -- Construction Workup
## Rinse (Post-Plate) -- Electroless Copper

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stage 7 of the electroless copper process. This rinse removes the alkaline E-Cu bath chemistry from the freshly plated parts. The defining characteristic of this stage is URGENCY: freshly deposited electroless copper oxidizes rapidly in air. The thin seed layer (0.5-2.5 um) is particularly vulnerable because even a thin oxide layer represents a significant percentage of total film thickness and can compromise adhesion of the subsequent electrolytic copper deposit.

Parts should proceed immediately from the E-Cu bath through this rinse and into either anti-tarnish treatment or electrolytic copper buildup. Delays at this stage are measured in minutes, not hours.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Rinse stage detail panel (Block B -- HERO):** Parameters and the oxidation urgency.
2. **Orientation strip (Block C):** 8-stage strip, Stage 7 highlighted.
3. **Oxidation timeline (Block D):** What happens to fresh E-Cu in air over time.
4. **Anti-tarnish options (Block E):** Quick protection before electrolytic buildup.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted
ZONE 3 -- RINSE DETAIL + OXIDATION URGENCY HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- COPPER OXIDATION TIMELINE (14.5"--22.0" / ~7.5")
ZONE 5 -- ANTI-TARNISH OPTIONS + NEXT STEP (22.0"--28.0" / ~6.0")
ZONE 6 -- TROUBLESHOOTING (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE (POST-PLATE)` -- Barlow Condensed ExtraBold, 80 pt, `#F0EDE8`. X: 0.5", Y: 0.5".

**Subheading:** `Electroless Copper -- Remove Bath Chemistry, Protect the Deposit -- Stage 7 of 8` -- Barlow SemiBold, 28 pt, `#2EC4B6` (Teal). X: 0.5", Y: 1.4".

**Tagline:** `Fresh electroless copper oxidizes in minutes. This rinse removes bath chemistry and starts the clock. Proceed to anti-tarnish or electrolytic copper immediately.` -- Barlow SemiBold, 20 pt, `#F0EDE8` at 65%. X: 0.5", Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.

Below: `Before: Parts with fresh E-Cu deposit in alkaline bath chemistry  -->  After: Rinsed parts ready for anti-tarnish or electrolytic copper (TIME SENSITIVE)`

---

### ZONE 3 -- Rinse Detail + Oxidation Urgency Hero

**Section label:** `RINSE -- POST-PLATE (TIME IS THE ENEMY)` -- Y: 4.4".

**BLOCK B -- Stage Detail Panel (Y: 5.0" to 9.0")**

Large rounded rectangle: X: 0.5", Y: 5.0", W: 23.0", H: 3.8", fill `#1E2435`, radius 8, left accent 0.06" `#2EC4B6`.

Stage badge: `STAGE 7 -- POST-PLATE RINSE` fill `#2EC4B6`, text `#1A1F2E`

Parameters (JetBrains Mono 14 pt `#F0EDE8`):
```
Type:            Double counterflow
Temperature:     Ambient
Time:            1-2 minutes
Water:           DI preferred; low-chloride tap acceptable
Agitation:       Gentle immersion
```

**Urgency callout (right side):**
- Rounded rect, fill `#E8A020` at 20%, border 2 pt `#E8A020`
- Title: `TIME CRITICAL` -- Barlow Condensed ExtraBold, 18 pt, `#E8A020`
- Text: `Freshly deposited electroless copper begins to oxidize IMMEDIATELY upon air exposure. The E-Cu seed layer is only 0.5-2.5 um thick -- even a thin oxide represents a significant fraction of total deposit. Proceed to the next step within MINUTES, not hours.` -- Inter Medium 13 pt `#F0EDE8`

---

**BLOCK C -- What You Are Removing (Y: 9.5" to 14.0")**

Two-panel layout.

**Left -- Bath Chemistry Removal (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.2", fill `#1E2435`, left accent `#2EC4B6`
- Title: `WHAT THIS RINSE REMOVES` Barlow SemiBold 18 pt `#2EC4B6`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Drag-out from the E-Cu bath:
  - NaOH (pH 12+)
  - EDTA complexant
  - Dissolved Cu2+ ions
  - Formaldehyde (volatile -- off-gasses)
  - Formate byproduct (HCOO-)
  - Stabilizer residues

Why removal matters:
  Alkaline residue causes staining
  EDTA residue interferes with acid copper
  Formaldehyde residue is a health hazard
  Cu2+ drag-out contaminates the next bath
```

**Right -- The Oxidation Problem (X: 12.0", W: 11.5"):**
- Rounded rect, H: 4.2", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `THE OXIDATION PROBLEM` Barlow SemiBold 18 pt `#E05C5C`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Fresh copper + oxygen + moisture:
  2 Cu + O2 --> 2 CuO (black oxide)
  4 Cu + O2 --> 2 Cu2O (red/brown oxide)

A 0.5 um E-Cu seed layer is THIN:
  Even 10 nm of oxide = 2% of total deposit
  Oxide layer prevents adhesion of
  subsequent electrolytic copper
  Result: delamination, blistering, opens

This is why every PCB shop runs the
E-Cu line as a CONTINUOUS sequence --
parts do not stop between the E-Cu
bath and the electrolytic copper bath.
```

---

### ZONE 4 -- Copper Oxidation Timeline

**Section label:** `OXIDATION TIMELINE -- WHAT HAPPENS WHEN YOU WAIT` -- Y: 14.7".

**BLOCK D -- Timeline Visual (Y: 15.3" to 21.5")**

Horizontal timeline bar: X: 0.5", W: 23.0", H: 1.0".

Five time markers with condition cards below:

**0-5 min (X: 0.5", W: 4.2"):**
- Marker: `#27AE60`
- Badge: `0-5 MIN` fill `#27AE60`
- Card fill `#1E2435`, left accent `#27AE60`
- `Bright pink-copper appearance` Inter Regular 13 pt `#F0EDE8`
- `No visible oxide` Inter Regular 13 pt `#F0EDE8`
- `OPTIMAL: proceed immediately` Inter Medium 13 pt `#27AE60`

**5-15 min (X: 5.0", W: 4.2"):**
- Marker: `#E8A020`
- Badge: `5-15 MIN` fill `#E8A020`
- Card fill `#1E2435`, left accent `#E8A020`
- `Slight dulling of copper luster` Inter Regular 13 pt `#F0EDE8`
- `Thin oxide forming` Inter Regular 13 pt `#F0EDE8`
- `ACCEPTABLE: anti-tarnish recommended` Inter Medium 13 pt `#E8A020`

**15-60 min (X: 9.5", W: 4.2"):**
- Marker: `#E8A020`
- Badge: `15-60 MIN` fill `#E8A020`
- Card fill `#1E2435`, left accent `#E8A020`
- `Visible tarnish (brown/dark)` Inter Regular 13 pt `#F0EDE8`
- `Oxide layer growing` Inter Regular 13 pt `#F0EDE8`
- `RISKY: adhesion may be compromised` Inter Medium 13 pt `#E8A020`

**1-4 hr (X: 14.0", W: 4.2"):**
- Marker: `#E05C5C`
- Badge: `1-4 HR` fill `#E05C5C`
- Card fill `#1E2435`, left accent `#E05C5C`
- `Dark brown to black oxide` Inter Regular 13 pt `#F0EDE8`
- `Significant oxide thickness` Inter Regular 13 pt `#F0EDE8`
- `PROBLEM: micro-etch required before electrolytic Cu` Inter Medium 12 pt `#E05C5C`

**>4 hr / overnight (X: 18.5", W: 5.0"):**
- Marker: `#E05C5C`
- Badge: `> 4 HR` fill `#E05C5C`
- Card fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- `Heavy oxide or tarnish film` Inter Regular 13 pt `#F0EDE8`
- `Possible adhesion failure` Inter Regular 13 pt `#F0EDE8`
- `Strip and re-plate may be necessary` Inter Medium 12 pt `#E05C5C`
- `DO NOT send oxidized E-Cu to electrolytic copper without surface preparation` Inter Medium 11 pt `#E05C5C`

---

### ZONE 5 -- Anti-Tarnish Options + Next Step

**Section label:** `ANTI-TARNISH PROTECTION & NEXT STEP` -- Y: 22.2".

**Left -- Anti-Tarnish Options (X: 0.5", W: 11.0", Y: 22.8" to 27.8"):**
- Rounded rect, H: 4.6", fill `#1E2435`, left accent `#E8A020`
- Title: `ANTI-TARNISH OPTIONS` Barlow SemiBold 18 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`):
```
IF parts cannot proceed immediately
to electrolytic copper:

1. ORGANIC TARNISH INHIBITOR
   Benzotriazole (BTA) or proprietary
   Dip: 15-30 seconds
   Forms molecular-thin barrier on Cu
   Must be removed before plating

2. DILUTE CHROMATE DIP
   Trivalent chromate preferred (RoHS)
   Dip: 15-30 seconds
   Provides temporary oxidation barrier

3. MICRO-ETCH BEFORE ELECTROLYTIC Cu
   If delay was unavoidable and oxide formed
   Sodium persulfate or peroxide/sulfuric
   Removes oxide; refreshes surface
   Re-activates for electrolytic deposition
```

**Right -- The Standard Path (X: 12.0", W: 11.5", Y: 22.8" to 27.8"):**
- Rounded rect, H: 4.6", fill `#1E2435`, left accent `#27AE60`
- Title: `THE STANDARD PATH (PCB)` Barlow SemiBold 18 pt `#27AE60`

Content (Inter Regular 14 pt `#F0EDE8`):
```
In PCB manufacturing, the standard
sequence is CONTINUOUS:

  E-Cu bath --> Rinse --> Electrolytic
  acid copper (25-50 um buildup)

No anti-tarnish needed because:
  - Parts move through in minutes
  - No air exposure delay
  - Wet copper surface stays reactive

The anti-tarnish options above are for:
  - End-of-shift holds
  - Equipment malfunctions
  - Plastics metallization (E-Cu is final)
  - EMI shielding (E-Cu is functional coat)
```

Callout below: `For plastics metallization and EMI shielding, the E-Cu deposit IS the functional coating. Anti-tarnish or passivation is the final step.` Inter Medium 12 pt `#E8A020`

---

### ZONE 6 -- Troubleshooting

**Section label:** `WHAT GOES WRONG AT POST-PLATE RINSE` -- Y: 28.2".

**Four problem cards (Y: 28.8" to 32.3"):**

| Card | X | W | Problem | Cause | Fix |
|---|---|---|---|---|---|
| 1 | 0.5" | 5.5" | DARK TARNISH ON FRESH Cu | Air exposure delay; rinse water too warm (accelerates oxidation) | Reduce transfer time; use ambient temp rinse; apply anti-tarnish |
| 2 | 6.3" | 5.5" | DELAMINATION AT ELECTROLYTIC Cu | Oxide on E-Cu surface from delay; contaminated rinse | Eliminate delays; micro-etch if delay occurred; check rinse water |
| 3 | 12.1" | 5.5" | WHITE RESIDUE ON SURFACE | NaOH/EDTA drag-out not fully rinsed; hard water minerals | Improve rinsing; use DI water; increase rinse time |
| 4 | 17.9" | 5.6" | FORMALDEHYDE ODOR AT RINSE | HCHO off-gassing from drag-out | Normal but ventilate; slot exhaust at rinse tank; monitor air |

Card construction: Rounded rect, H: 3.2", fill `#1E2435`, left accent 0.04" `#E05C5C`.

---

### ZONE 7 -- Footer

Standard footer. Title: `Rinse (Post-Plate) -- Electroless Copper`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse parameters and oxidation timeline shown are typical for formaldehyde-based electroless copper plating for PCB and plastics metallization. Oxidation rates vary with humidity, temperature, and deposit characteristics. Consult your process supplier TDS.`

---

## Parts 5-7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Plate E-Cu -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The oxidation timeline in Zone 4 is the signature visual for this poster. The five time markers -- from "bright pink-copper at 0-5 min" to "strip and re-plate at >4 hr" -- communicate the urgency in a way that no amount of text can match. The color progression from Emerald (safe) through Amber (warning) to Coral (problem) follows the series convention and reads instantly from across a room.

The "standard path" callout in Zone 5 provides important context: in a well-run PCB line, this poster's warnings are largely academic because parts move continuously through the sequence. The anti-tarnish options are for the exception cases -- end-of-shift holds, equipment problems, or applications where E-Cu is the final deposit (plastics metallization, EMI shielding).

The formaldehyde odor card in troubleshooting is a practical touch -- operators at the post-plate rinse will smell HCHO off-gassing from the drag-out, and it is important to normalize this while still requiring ventilation.

---

*Alaina -- Poster #245 -- Construction Workup v1.0 -- 2026-04-26*
