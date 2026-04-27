---
Project: Plating Posters Inc
Poster Number: 377
Title: "Inspection & Handling -- Post-Descale"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-5 technical reference (descaling / heavy oxide removal)"
Technical Source: Surface profile measurement (ASTM D4417), surface cleanliness verification (SSPC-VIS 1), handling protocols post-descale. Replica tape, profilometer, tape test, water break test.
Process Scope: Post-descale inspection methods, surface profile measurement, cleanliness verification, and handling protocols
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (SVG/HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Descaling
  - Inspection
  - Handling
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT05
---

# Poster #377 -- Construction Workup
## Inspection & Handling -- Post-Descale

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

After descaling, two questions must be answered: "Is the surface clean enough?" and "Is the profile right?" This poster covers every inspection method for both cleanliness and surface profile, plus the handling rules that prevent recontamination between descaling and the next process step. The 4-hour window and clean-glove handling are the two most common points of failure.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Surface profile measurement panel (Block B -- HERO):** Two side-by-side panels -- replica tape method and digital profilometer. Each with procedure, ASTM reference, and target values.

2. **Cleanliness verification grid (Block C):** Four methods -- SSPC-VIS 1 visual comparison, water break test, cellophane tape test, UV inspection.

3. **Handling rules callout (Block D):** Time limits, glove requirements, storage guidance.

4. **Profile target reference (Block E):** Table of target profiles by downstream coating type.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 14.5" / 22.5" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- SURFACE PROFILE MEASUREMENT / HERO (2.9"--14.5" / ~11.6" tall)
  Block B: Replica tape vs. digital profilometer (two panels)
  Block B2: Profile target table by coating type

ZONE 3 -- CLEANLINESS VERIFICATION (14.5"--22.5" / ~8.0" tall)
  Block C: Four verification methods (2x2 grid)

ZONE 4 -- HANDLING RULES (22.5"--28.5" / ~6.0" tall)
  Block D: Time limits, glove handling, storage

ZONE 5 -- THE 4-HOUR RULE (28.5"--32.5" / ~4.0" tall)
  Block E: Prominent 4-hour rule callout with environmental modifiers

ZONE 6 -- FOOTER BAND (32.5"--36.0")
  Block F: Standard footer
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `INSPECTION & HANDLING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Post-Descale -- Profile Measurement, Cleanliness Checks & Handling Rules` -- 30 pt `#27AE60` (Emerald). Y: 1.5".
**Tagline:** `Two questions after descaling: Is it clean? Is the profile right? This poster answers both -- and tells you how not to ruin the surface before the next step.` -- 20 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Surface Profile Measurement (HERO)

**Section label:** Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> SURFACE PROFILE -- MEASURING THE ANCHOR PATTERN

---

**BLOCK B -- Two-Panel Profile Methods**

Y: 3.8" to 11.0".

**Left -- Replica Tape Method (X: 0.5", W: 11.0"):**

Rounded rect, H: 7.0", fill `#1E2435`, radius 8. Left accent 0.06" `#2EC4B6`.

Title: `REPLICA TAPE (TESTEX PRESS-O-FILM)` -- Barlow SemiBold, 18 pt, `#2EC4B6`.
Reference: `ASTM D4417 Method C` -- JetBrains Mono 13 pt `#2EC4B6`.

Procedure steps (Inter Regular 13 pt `#F0EDE8`, numbered):
1. `Place tape (foam side down) on blasted surface`
2. `Burnish with swivel burnishing tool (10--15 circular strokes)`
3. `Remove tape -- foam compresses to replicate profile`
4. `Measure with spring micrometer`
5. `Subtract film thickness (50 um / 2 mils) from reading`
6. `Report as peak-to-valley profile depth`

Advantages (Inter Medium 12 pt `#27AE60`):
`Field-portable. No batteries. Accepted worldwide. Low cost per test.`

Limitation (Inter Regular 12 pt `#E8A020`):
`Measures only peak-to-valley. Single-point measurement -- take 3+ readings and average.`

**Right -- Digital Profilometer (X: 12.0", W: 11.5"):**

Rounded rect, H: 7.0", fill `#1E2435`, radius 8. Left accent 0.06" `#E8A020`.

Title: `DIGITAL PROFILOMETER` -- Barlow SemiBold, 18 pt, `#E8A020`.
Reference: `ASTM D4417 Method B` -- JetBrains Mono 13 pt `#E8A020`.

Procedure steps:
1. `Calibrate instrument per manufacturer`
2. `Place stylus on blasted surface`
3. `Instrument traverses surface, recording peaks and valleys`
4. `Reports Ra (arithmetic average) and/or Rz (10-point average)`
5. `Multiple traverses for statistical confidence`

Advantages:
`More precise than replica tape. Reports Ra and Rz. Digital record for quality documentation.`

Limitation:
`More expensive. Requires calibration. Not as fast in the field.`

---

**BLOCK B2 -- Profile Target Table**

Y: 11.3" to 14.3". Full-width table.

Column widths: Downstream Coating (7.0") | Target Profile (5.0") | Unit (4.0") | Notes (7.0")

Header: `#3A4055` fill.

| Downstream Coating | Target Profile | Unit | Notes |
|---|---|---|---|
| Electroplating (general) | 25--75 um (1--3 mils) | Rz | Anchor for adhesion; too deep traps solution |
| Hot-dip galvanizing | 50--100 um (2--4 mils) | Rz | Heavier profile for thicker coating |
| Organic coating / paint | 25--75 um (1--3 mils) | Rz | Match to paint system spec |
| Thermal spray | 50--125 um (2--5 mils) | Rz | Higher profile for mechanical bond |
| Powder coating | 25--50 um (1--2 mils) | Rz | Moderate profile; too deep causes orange peel |

Data: JetBrains Mono 12 pt. Labels: Inter Medium 12 pt.

---

### ZONE 3 -- Cleanliness Verification

**Section label:** Centered. Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> CLEANLINESS CHECKS -- FOUR METHODS

---

**BLOCK C -- 2x2 Grid**

Y: 15.4" to 22.3". Four cards in a 2x2 grid.

Each card: Rounded rect, W: 11.0", H: 3.2", fill `#1E2435`, radius 6, left accent 0.06".

| Position | Method | Accent | Standard | Procedure | Result |
|---|---|---|---|---|---|
| R1C1 (X: 0.5", Y: 15.4") | SSPC-VIS 1 Visual Comparison | `#2EC4B6` | SSPC-VIS 1 photo standards | Hold reference photos next to blasted surface; compare under adequate lighting | Match to SP-5, SP-10, SP-6, or SP-7 grade |
| R1C2 (X: 12.0", Y: 15.4") | Water Break Test | `#27AE60` | After subsequent alk clean | Rinse surface with clean water; observe drainage pattern | Complete film = clean; beading = contamination |
| R2C1 (X: 0.5", Y: 19.0") | Cellophane Tape Test | `#E8A020` | After blast + blowoff | Press clear tape firmly on surface; peel; examine tape | Particles on tape = residual media/dust |
| R2C2 (X: 12.0", Y: 19.0") | UV / Black Light Inspection | `#E8A020` | 365 nm UV lamp | Illuminate surface in darkened area | Fluorescence = residual oil (many oils fluoresce under UV) |

Per card:
- Method: Barlow SemiBold 16 pt, accent color
- Standard: JetBrains Mono 12 pt `#F0EDE8` at 60%
- Procedure: Inter Regular 13 pt `#F0EDE8`
- Result: Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Handling Rules

**Section label:** Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

> HANDLING AFTER DESCALING -- DON'T RUIN YOUR WORK

---

**BLOCK D -- Three Handling Rule Cards**

Y: 23.4" to 28.3". Three side-by-side callout boxes.

| Card | X | W | Accent | Title | Content |
|---|---|---|---|---|---|
| 1 | 0.5" | 7.33" | `#E05C5C` | TIME LIMITS | Steel oxidizes immediately after blast. Max 4 hours before next step. Less in humid environments (> 60% RH). If delay unavoidable: apply temporary rust preventive (soluble oil or flash-rust inhibitor). |
| 2 | 8.17" | 7.33" | `#E8A020` | GLOVE HANDLING | Handle with clean, dry gloves ONLY. No bare-hand contact. Fingerprints = organic contamination = adhesion failure at that spot. Cotton or nitrile gloves acceptable. |
| 3 | 15.83" | 7.67" | `#2EC4B6` | STORAGE (IF REQUIRED) | Wrap in clean, lint-free paper or VCI paper (vapor corrosion inhibitor). Store in dry, climate-controlled area. Minimize storage time -- process as soon as possible. |

Each card: Rounded rect, H: 4.5", fill `#1E2435`, radius 6, left accent 0.06".
Title: Barlow SemiBold 16 pt, accent color. Content: Inter Regular 13 pt `#F0EDE8`.

---

### ZONE 5 -- The 4-Hour Rule

**Section label:** Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#E05C5C`.

> THE 4-HOUR RULE

**BLOCK E -- Full-Width Prominent Callout**

Y: 29.4" to 32.3".

Rounded rect, X: 0.5", W: 23.0", H: 2.7", fill `#E05C5C` at 12%, border 2 pt `#E05C5C`, radius 8.

Big number (left side): `4 HR` -- Barlow Condensed ExtraBold, 72 pt, `#E05C5C`.

Three columns to the right:

| Column | Environment | Modified Limit |
|---|---|---|
| 1 | Dry shop (< 40% RH) | Up to 4 hours acceptable |
| 2 | Moderate (40--60% RH) | 2--4 hours -- monitor for flash rust |
| 3 | Humid (> 60% RH) | Process ASAP -- flash rust in under 1 hour possible |

Per column:
- Environment: Inter Medium 14 pt `#F0EDE8`
- Limit: JetBrains Mono 14 pt, `#27AE60` (dry), `#E8A020` (moderate), `#E05C5C` (humid)

Bottom note: `If you see orange or brown discoloration before the next step, you have flash rust. Re-blast or re-pickle before proceeding.` -- Inter Medium, 13 pt, `#E05C5C`

---

### ZONE 6 -- Footer

Standard. Title: `Inspection & Handling -- Post-Descale`. Version `v1.0 -- 2026`.

Disclaimer: `Source: ASTM D4417; SSPC-VIS 1; general industry knowledge. Consult applicable specifications for site-specific profile and cleanliness requirements.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Inspection Handling Descaling -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The profile target table by downstream coating type is one of the most practically useful references in the entire cluster. Shops constantly ask "what profile do I need?" and the answer depends entirely on what comes next. The 4-hour rule gets its own zone (Zone 5) with the big "4 HR" number because this is the single most time-critical rule in descaling -- and the one most commonly violated. The humidity modifier table adds real-world nuance that generic references often miss.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #377 -- Construction Workup v1.0*
*2026-04-26*
