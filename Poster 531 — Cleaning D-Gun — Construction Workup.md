---
Project: Plating Posters Inc
Poster Number: 531
Title: "Cleaning -- D-Gun"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (alaina-poster-designer)
Source Documents:
  - "Thermal Spray Clusters — Watson Research Brief (Cluster 6: Detonation Gun)"
Technical Source: D-Gun pre-spray cleaning follows premium aerospace protocol identical to HVOF. Aqueous alkaline cleaning at 50--70 C, DI water rinse, water-break-free verification, forced air dry, grit blast within specified time window. Emphasis on aerospace-grade cleanliness for turbine components.
Process Scope: D-Gun -- pre-spray cleaning sequence
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document.
tags:
  - PosterDesign
  - DGun
  - DetonationGun
  - ThermalSpray
  - Cleaning
  - ConstructionWorkup
  - ClusterTS06
---

# Poster #531 -- Construction Workup
## Cleaning -- D-Gun

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Cleaning poster for D-Gun. The hero message is "premium aerospace standard" -- D-Gun cleaning protocol is identical to HVOF because both processes serve the same high-value aerospace market. The cleaning sequence must be flawless because the parts being coated (turbine blades, seals, shafts) are extremely expensive and reject rates must be near zero. The water-break-free test is the gatekeeper.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cleaning sequence steps (Block B -- HERO):** 4-step vertical flow showing the premium aerospace cleaning protocol.
2. **"Premium Aerospace Standard" callout (Block C):** Amber callout emphasizing that D-Gun cleaning equals HVOF protocol.
3. **Contamination types table (Block D):** What contaminants are present and how each cleaning step addresses them.
4. **Time windows callout (Block E):** Critical time limits between cleaning, blasting, and spraying.
5. **Common cleaning failures strip (Block F):** Defects caused by inadequate cleaning.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- CLEANING SEQUENCE + AEROSPACE CALLOUT (2.9"--14.0" / ~11.1")
  Block B: 4-step cleaning flow
  Block C: "Premium Aerospace Standard" callout
ZONE 3 -- CONTAMINATION TYPES TABLE (14.0"--22.0" / ~8.0")
  Block D: Contamination identification and removal
ZONE 4 -- TIME WINDOWS + COMMON FAILURES (22.0"--32.5" / ~10.5")
  Block E: Critical time limits
  Block F: Common cleaning failures
ZONE 5 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**Headline:** `CLEANING` -- 80 pt `#F0EDE8`.
**Subheading:** `D-Gun -- Premium Aerospace Cleaning Protocol` -- 32 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Zero-defect parts demand zero-contamination surfaces. Every D-Gun coating starts with immaculate substrate preparation.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Cleaning Sequence + Aerospace Callout

**Section label:** `PRE-SPRAY CLEANING SEQUENCE` -- Y: 3.1".

**BLOCK B -- 4-Step Cleaning Flow (Left, X: 0.5", W: 14.5")**

Y: 3.8" to 13.0". Four step cards, vertically stacked, connected by arrows.

Each card: W: 14.0", H: 2.0", fill `#1E2435`, radius 6, left accent 4 pt.

| Step | Accent | Title | Parameters | Critical Check |
|---|---|---|---|---|
| 1 | `#2EC4B6` | AQUEOUS ALKALINE CLEAN | 50--70 C (120--160 F); pH 10--12; 5--15 min immersion or spray wash | Remove all oils, greases, machining fluids, fingerprints |
| 2 | `#2EC4B6` | DI WATER RINSE | Deionized water; multiple stages; final rinse resistivity > 1 MOhm-cm | Aerospace requirement: DI rinse prevents mineral deposit residue |
| 3 | `#E8A020` | WATER-BREAK-FREE VERIFICATION | ASTM F22 equivalent; surface must sheet water uniformly with no beading | GATEKEEPER TEST: if water beads, return to Step 1 and re-clean |
| 4 | `#27AE60` | FORCED AIR DRY | Clean, filtered, oil-free compressed air or oven dry | No moisture at time of grit blast; no cloth or paper towel contact |

Step number badges: Rounded rect, W: 1.0", H: 0.35", fill accent color. Text: `STEP 1` etc., Barlow Condensed ExtraBold, 13 pt, `#1A1F2E`.

Title: Barlow SemiBold, 18 pt, `#F0EDE8`.
Parameters: JetBrains Mono Regular, 12 pt, `#F0EDE8`.
Critical Check: Inter Medium, 12 pt, accent color.

Arrows between cards: 2 pt, `#3A4055`, with downward arrowhead.

**"Return to Step 1" feedback arrow (from Step 3 right side back to Step 1 right side):**
Dashed line, 2 pt, `#E05C5C`, with arrowhead. Label: `FAIL: Re-clean` JetBrains Mono, 11 pt, `#E05C5C`.

**BLOCK C -- "Premium Aerospace Standard" Callout (Right, X: 15.5", W: 8.0")**

Y: 3.8" to 8.5". Rounded rect, fill `#1E2435`, radius 8, left accent 4 pt `#E8A020`.
Amber-tinted glass.

Title: `PREMIUM STANDARD` Barlow Condensed ExtraBold, 24 pt, `#E8A020`.

Body (Inter Regular, 14 pt, `#F0EDE8`, line height 160%):
```
D-Gun cleaning protocol is IDENTICAL
to HVOF aerospace cleaning.

Both processes coat high-value parts:
  - Gas turbine blades and vanes
  - Compressor seals
  - Landing gear components
  - Hydraulic actuator rods
  - Industrial pump shafts

Part values: $1,000 -- $50,000+ each.
A rejected coating due to contamination
is an expensive failure.
```

`Cleaning is not optional. It is not "good practice." It is a SPECIFICATION REQUIREMENT.` Inter Medium, 12 pt, `#E8A020`.

**Glove handling note (below, Y: 9.0" to 12.5"):**
Rounded rect, fill `#1E2435`, left accent `#E05C5C`.

Title: `HANDLING AFTER CLEANING` Barlow SemiBold, 16 pt, `#E05C5C`.

Rules (Inter Regular, 13 pt, `#F0EDE8`, line height 160%):
```
1. NEVER touch cleaned surface with bare hands
   (fingerprint oils contaminate immediately)

2. Wear clean, lint-free gloves (nitrile or cotton)

3. Store cleaned parts in clean, covered containers

4. Minimize time between cleaning and grit blast
   (ideally same shift)

5. If part is dropped or contacts any surface,
   RE-CLEAN from Step 1
```

Rules 1 and 5: Inter Medium, `#E05C5C`.

---

### ZONE 3 -- Contamination Types Table

**Section label:** `CONTAMINATION IDENTIFICATION AND REMOVAL` -- Y: 14.2".

**BLOCK D -- Contamination Table (Full width)**

Y: 14.8" to 21.5".

Header row: `#3A4055`. Columns: Contaminant (4.0") | Source (5.0") | Removal Method (5.5") | If Not Removed (8.5")

| Contaminant | Source | Removal Method | If Not Removed |
|---|---|---|---|
| Machining oils / coolants | CNC machining, grinding | Alkaline clean (Step 1) | Adhesion failure; coating delamination |
| Fingerprints (sebaceous oils) | Bare-hand contact | Alkaline clean; then glove protocol | Localized adhesion failure (fingerprint pattern visible in coating) |
| Shop dust / particulates | Ambient contamination | Alkaline clean + DI rinse | Inclusions at interface; porosity |
| Mineral deposits (hard water) | Tap water rinse | DI water final rinse (Step 2) | White residue at interface; adhesion reduction |
| Rust / oxide scale | Storage corrosion | Grit blast removes (Step 3 is next) | Must be removed by blasting, not cleaning |
| Residual cleaning agent | Incomplete rinsing | Extended DI rinse; verify rinse water quality | Chemical contamination at interface |

Data: Inter Regular, 12 pt, `#F0EDE8`. "If Not Removed" column: Inter Medium, 12 pt, `#E05C5C`.
Contaminant names: Inter Medium, 13 pt, `#E8A020`.

---

### ZONE 4 -- Time Windows + Common Failures

**Left -- Time Windows (X: 0.5", W: 11.5")**

Section label: `CRITICAL TIME WINDOWS` Y: 22.2".

**BLOCK E -- Time Limit Cards**

Y: 22.8" to 30.5". Three time-window cards stacked.

Each card: W: 11.0", H: 2.2", fill `#1E2435`, radius 6, left accent 4 pt.

| Window | Accent | Time Limit | Notes |
|---|---|---|---|
| CLEAN TO BLAST | `#E8A020` | < 4 hours (same shift preferred) | Cleaned surface re-contaminates with shop dust and humidity over time |
| BLAST TO SPRAY | `#E05C5C` | < 4 hours (some specs require < 2 hours) | Blasted surface oxidizes and loses activation; humidity accelerates degradation |
| RINSE TO DRY | `#2EC4B6` | Immediately | Standing water leaves mineral deposits; promotes flash rust on ferrous substrates |

Window: Barlow SemiBold, 16 pt, accent color.
Time Limit: Barlow Condensed ExtraBold, 24 pt, accent color.
Notes: Inter Regular, 13 pt, `#F0EDE8`.

**Humidity note (below, Y: 30.8" to 32.0"):**
Rounded rect, W: 11.0", H: 1.0", fill `#E8A020` at 10%, border 1 pt `#E8A020`, radius 8.

`In high-humidity environments (> 60% RH), reduce all time windows by 50%. Monitor with hygrometer.` Inter Medium, 13 pt, `#E8A020`, center.

**Right -- Common Cleaning Failures (X: 12.5", W: 11.0")**

Section label: `COMMON CLEANING FAILURES` Y: 22.2".

**BLOCK F -- Failure Cards (stacked)**

Y: 22.8" to 32.0". Five failure cards.

| Failure | Color | Cause | Result in Coating |
|---|---|---|---|
| WATER BREAK ON SURFACE | `#E05C5C` | Incomplete oil removal; contaminated rinse water | Adhesion failure at contaminated spots |
| FINGERPRINT PATTERN IN COATING | `#E05C5C` | Bare-hand contact after cleaning | Localized delamination matching finger pattern |
| WHITE RESIDUE AT INTERFACE | `#E8A020` | Tap water used instead of DI for final rinse | Mineral inclusions; reduced bond strength |
| FLASH RUST BEFORE BLAST | `#E8A020` | Excessive time between rinse and blast; high humidity | Oxide layer at interface reduces adhesion |
| CLEANING AGENT RESIDUE | `#2EC4B6` | Insufficient rinsing; concentrated alkaline left on surface | Chemical contamination; gas evolution during spray |

Each card: H: 1.7", fill `#1E2435`, left accent failure color.
Failure: Barlow SemiBold, 14 pt, failure color.
Cause: Inter Regular, 12 pt, `#F0EDE8`.
Result: Inter Medium, 12 pt, `#E05C5C`.

---

### ZONE 5 -- Footer Band

Standard footer. Title: `Cleaning -- D-Gun`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 5 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cleaning D-Gun -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cleaning protocol for D-Gun is identical to HVOF, but the stakes are even higher because D-Gun is typically applied to the most expensive aerospace components. The poster emphasizes the cost of failure -- these are $1K--$50K parts. The water-break-free test as a "gatekeeper" is the critical visual concept: if water beads, you go back to Step 1. The feedback arrow in the cleaning flow reinforces this loop. The fingerprint pattern failure is a particularly visceral example -- operators can literally see the pattern of their fingertip in a failed coating.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #531 -- Construction Workup v1.0*
*2026-04-26*
