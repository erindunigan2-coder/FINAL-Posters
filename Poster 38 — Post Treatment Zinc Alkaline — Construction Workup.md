---
Project: Plating Posters Inc
Poster Number: 38
Title: "Post Treatment -- Zinc (Alkaline)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-25T00:00:00
Author: Elara (prompt-architect)
Process Scope: Post-treatment (passivation, sealer, dry/cure) for alkaline zinc line (Stage 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - Alkaline
  - PostTreatment
  - Passivation
  - Chromate
  - ConstructionWorkup
  - Series2
  - ClusterEP01
---

# Poster #38 -- Construction Workup
## Post Treatment -- Zinc (Alkaline)

*Elara -- Plating Posters Inc Prompt Architect*
*v1.0 -- 2026-04-25*

Stages 7--8 of the alkaline zinc process. This poster combines passivation (chromate conversion), optional sealer, and dry/cure into a single poster because these steps form an inseparable unit -- the post-treatment sequence that determines the final corrosion protection performance. Passivation is where the zinc deposit transforms from a bare metal layer into a corrosion-resistant system.

Hero visual: a side-by-side comparison of trivalent vs. hexavalent chromate conversion coatings, with color chips showing the visual appearance of each (clear, blue, yellow, black) and a salt spray performance bar chart.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Trivalent vs. Hexavalent hero (Block B):** Two large panels side by side showing the two chromate families. Each panel includes color appearance chips (small colored rectangles), pH ranges, immersion times, and RoHS status. Visual comparison format.
2. **Salt spray bar chart (Block C):** A horizontal bar chart showing hours to white rust for each passivate type. Built with rectangles of varying widths.
3. **Color chip samples (inside Block B):** Small rectangles with text labels showing: Clear/Blue, Yellow, Black. Colors approximated using hex fills.
4. **Sealer + Dry/Cure section (Block E):** Combined panel covering the final steps.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette.

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- ORIENTATION STRIP (2.9"--4.2")
  Stages 7+8 highlighted
ZONE 3 -- TRI VS HEX HERO + SALT SPRAY CHART (4.2"--16.0")
ZONE 4 -- PASSIVATE PARAMETERS TABLE (16.0"--22.0")
ZONE 5 -- SEALER + DRY/CURE (22.0"--27.0")
ZONE 6 -- COMMON PROBLEMS + SAFETY (27.0"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header

**Headline:** `POST TREATMENT` -- 76 pt `#F0EDE8`. Y: 0.5".
**Subheading:** `Zinc (Alkaline) -- Passivate, Seal, Cure -- Stages 7 & 8` -- 30 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The zinc is on. Now protect it. Passivation determines whether your parts last 48 hours or 480 hours in salt spray.` -- 20 pt at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

**Stages 7 AND 8 both highlighted:** fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Bare zinc deposit (no corrosion protection)  -->  After: Passivated, sealed, cured -- spec-ready`

---

### ZONE 3 -- Trivalent vs. Hexavalent Hero + Salt Spray

**Section label:** `PASSIVATION -- TRIVALENT VS. HEXAVALENT CHROMATE` -- Y: 4.4".

**BLOCK B -- Two Panels (Y: 5.0" to 13.0")**

**Left -- Trivalent Chromate (X: 0.5", W: 11.0", H: 7.5"):**
- Rounded rect fill `#1E2435`, border 2 pt `#27AE60`
- Title: `TRIVALENT CHROMATE (Cr3+)` -- Barlow SemiBold 22 pt `#27AE60`
- RoHS badge: small rounded rect fill `#27AE60`, text `RoHS COMPLIANT` Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Subtitle: `The Modern Standard` Inter Medium 14 pt `#F0EDE8` at 60%

Parameters (JetBrains Mono 14 pt):
```
pH:           1.8--4.5
Temperature:  Ambient (65--85 F)
Time:         30--90 sec immersion
Chemistry:    Cr3+ salts (proprietary)
```

**Color chips** (4 small colored rectangles, each W: 2.0", H: 0.8", with label):
- Clear/Blue: fill `#87CEEB` at 50%, label `Clear / Blue` -- most common
- Yellow iridescent: fill `#DAA520` at 60%, label `Yellow Iridescent`
- Black: fill `#1A1F2E`, border 1 pt `#F0EDE8`, label `Black`
- Olive drab: fill `#6B8E23` at 60%, label `Olive Drab`

Performance note: `Typical SST: 72--200+ hr to white rust (with sealer)` JetBrains Mono 13 pt `#27AE60`

Key advantage: `No hexavalent chromium -- safe, compliant, increasing market share` Inter Medium 13 pt `#27AE60`

**Right -- Hexavalent Chromate (X: 12.0", W: 11.5", H: 7.5"):**
- Rounded rect fill `#1E2435`, border 2 pt `#E8A020`
- Title: `HEXAVALENT CHROMATE (Cr6+)` -- Barlow SemiBold 22 pt `#E8A020`
- RoHS badge: fill `#E05C5C`, text `RoHS RESTRICTED` Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Subtitle: `Legacy -- Still Used for Performance` Inter Medium 14 pt `#F0EDE8` at 60%

Parameters:
```
pH:           1.5--2.5
Temperature:  Ambient to 100 F
Time:         15--30 sec immersion
Chemistry:    Cr6+ (chromic acid based)
```

**Color chips:**
- Clear/Blue: fill `#87CEEB` at 40%, label `Clear / Blue`
- Yellow: fill `#FFD700` at 70%, label `Yellow (classic iridescent)`
- Black: fill `#1A1F2E`, border 1 pt `#F0EDE8`, label `Black`
- Olive drab: fill `#556B2F` at 70%, label `Olive Drab (military)`

Performance note: `Typical SST: 96--500+ hr to white rust` JetBrains Mono 13 pt `#E8A020`

Key disadvantage: `Contains carcinogenic Cr6+ -- restricted under RoHS, REACH, ELV. Self-healing property unique to hex.` Inter Medium 13 pt `#E05C5C`

---

**BLOCK C -- Salt Spray Comparison Bar Chart (Y: 13.3" to 15.8")**

Horizontal bar chart comparing hours to white rust:

Title: `SALT SPRAY PERFORMANCE (hours to white rust)` Barlow Condensed ExtraBold 20 pt. Y: 13.3".

| Type | Hours | Bar Width (proportional) | Bar Color |
|---|---|---|---|
| Bare zinc (no passivate) | 12--24 hr | Short | `#E05C5C` |
| Tri clear (no sealer) | 48--72 hr | Medium | `#2EC4B6` |
| Tri clear + sealer | 96--200 hr | Long | `#27AE60` |
| Tri black + sealer | 120--240 hr | Longer | `#27AE60` |
| Hex yellow | 96--200 hr | Long | `#E8A020` |
| Hex yellow + sealer | 200--500 hr | Longest | `#E8A020` |

Each bar: Rounded rect, H: 0.3", fill at 70% of bar color. Label on left (Inter Medium 12 pt), hours on right (JetBrains Mono 12 pt).

Scale line at bottom: `0` to `500+ hours`.

---

### ZONE 4 -- Passivate Parameters Table

**Section label:** `PASSIVATION PARAMETERS -- DETAILED` -- Y: 16.2".

**Full-width table (X: 0.5", W: 23.0"):**

| Parameter | Trivalent | Hexavalent | Notes |
|---|---|---|---|
| pH | 1.8--4.5 | 1.5--2.5 | Check 2x/shift minimum |
| Temperature | Ambient (65--85 F) | Ambient--100 F | Hex may need mild heat |
| Immersion time | 30--90 sec | 15--30 sec | Longer =/= better (over-immersion dulls) |
| Agitation | Gentle | Gentle | Excessive agitation strips coating |
| Rinse before | Must be neutral (pH 6--8) | Must be neutral | Alkaline residue destroys both |
| Rinse after | Immediate, gentle | Immediate, gentle | Aggressive rinse strips fresh coating |
| Drain time | 10--15 sec | 10--15 sec | Allow excess to drip back |
| Replenishment | Per titration / TDS | Per titration / TDS | Cr3+ consumed by use; Cr6+ by drag-out |
| Tank material | PP or PVC (no metal) | PP or PVC (no metal) | Metal tanks contaminate bath |

Header: `#3A4055`. Data: JetBrains Mono 12 pt. Notes: Inter Regular 11 pt at 70%.

---

### ZONE 5 -- Sealer + Dry/Cure

**Section label:** `SEALER & DRY/CURE -- THE FINAL STEPS` -- Y: 22.2".

**Two side-by-side panels:**

**Left -- Sealer (X: 0.5", W: 11.0"):**
- Rounded rect fill `#1E2435`, accent `#2EC4B6`
- Title: `TOPCOAT SEALER (OPTIONAL)` Barlow SemiBold 20 pt `#2EC4B6`
- Parameters:
  - `Type: Organic or silicate-based sealant`
  - `Temperature: 150--180 F (66--82 C)`
  - `Time: 30--60 sec immersion`
  - `Purpose: Fills micro-pores in passivate layer`
  - `Benefit: 2--3x increase in salt spray performance`
  - `Application: Dip or spray`
  - `Note: Sealer changes the coefficient of friction -- check torque specs on fasteners`

**Right -- Dry/Cure (X: 12.0", W: 11.5"):**
- Rounded rect fill `#1E2435`, accent `#E8A020`
- Title: `DRY / CURE` Barlow SemiBold 20 pt `#E8A020`
- Parameters:
  - `Method: Forced air, oven, or IR lamps`
  - `Temperature: 150--170 F (66--77 C)`
  - `Time: 15--20 minutes minimum`
  - `Purpose: Cure passivate film + remove moisture`
  - `Critical: Under-curing = soft film = poor performance`
  - `Over-curing (> 200 F / 93 C): film degradation -- avoid`
  - `Hydrogen bake (if required): 375 F for 23 hr BEFORE passivation`

H-embrittlement note at bottom:
- `High-strength steel (>= 145 ksi / >= 31 HRC): bake at 375 F BEFORE passivation -- per ASTM B850` -- Inter Medium 13 pt `#E05C5C`

---

### ZONE 6 -- Problems + Safety

**Left -- Problems (X: 0.5", W: 14.0"):**

**Section label:** `WHAT GOES WRONG AT POST-TREATMENT` -- Y: 27.2".

| Problem | Cause | Fix |
|---|---|---|
| No passivate color | pH too high (alkaline drag-in) | Improve post-plate rinse; check pH |
| Patchy/uneven color | Contaminated passivate or poor rinse | Dump and remake; improve rinse |
| Passivate peeling | Over-immersion or over-agitation | Reduce time; gentle immersion only |
| Poor salt spray | Under-curing or no sealer | Add sealer; ensure full cure time |
| Iridescent shift (tri) | Bath aging or Cr3+ depletion | Replenish per TDS; check drag-out |
| Blistering after bake | H-embrittlement bake after passivate | Bake BEFORE passivation, not after |

Problem: `#E05C5C`. Fix: `#27AE60`.

**Right -- Safety (X: 15.0", W: 8.5"):**
- Title: `SAFETY -- POST-TREATMENT CHEMISTRY` `#E8A020`
- `Passivate baths are ACIDIC (pH 1.5--4.5) -- acid burns`
- `Hexavalent chromate: CARCINOGENIC -- full PPE + ventilation`
- `Trivalent: lower hazard but still acidic`
- `Sealer baths: hot (150--180 F) -- thermal burn risk`
- `Dry oven: burn hazard -- gloves for part handling`
- `Cr6+ waste: REGULATED -- special waste treatment required`
- `All Cr6+ operations require medical surveillance program`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Zinc (Alkaline)`. Version `v1.0 -- 2026`.

Disclaimer addition: `Hexavalent chromium processes are subject to regulatory restrictions (RoHS, REACH, ELV, OSHA PEL). Verify compliance with applicable regulations before use.`

---

## Parts 5--7

**Grouping:** 7 standard zones.

**Light Remap:** Standard table. Color chip fills need testing on light background -- some may need opacity adjustment. RoHS badges: verify green/red text legibility on light fills.

| Dark | Light |
|---|---|
| `#1A1F2E` | `#F5F4F0` |
| `#F0EDE8` | `#1A1F2E` |
| `#1E2435` | `#ECEEF4` |
| `#252B3D` | `#E8E8F0` |
| `#0D1020` | `#1A1F2E` |
| `#E8A020` | `#C8860A` |
| `#2EC4B6` | `#1A8C82` |
| `#27AE60` | `#1E7A47` |
| `#E05C5C` | `#B83E3E` |
| `#3A4055` | `#D0D4DE` |
| `#C8D0D8` | `#C8D0D8` |

**Export:** Six files -- `Post Treatment Zinc Alkaline -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This is the final poster in the EP-01 cluster and arguably the second most important after #36 (Main Tank). Passivation is where corrosion protection is either made or broken. The trivalent vs. hexavalent comparison is one of the most commonly asked questions in zinc plating, and the salt spray bar chart makes the performance difference visceral and immediate.

The RoHS compliance badges are intentionally prominent -- in 2026, most new zinc plating specs require trivalent, but many legacy military and aerospace specs still call out hexavalent. The poster helps operators and quality engineers understand both systems.

---

*Elara -- Poster #38 -- Construction Workup v1.0 -- 2026-04-25*
