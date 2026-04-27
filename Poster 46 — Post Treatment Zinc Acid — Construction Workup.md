---
Project: Plating Posters Inc
Poster Number: 46
Title: "Post Treatment -- Zinc (Acid)"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Process Scope: Post-treatment (passivation, sealer, dry/cure, HE bake) for acid chloride zinc line (Stages 7--8 of 8)
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ZincPlating
  - AcidChloride
  - PostTreatment
  - Passivation
  - Chromate
  - ConstructionWorkup
  - Series2
  - ClusterEP02
---

# Poster #46 -- Construction Workup
## Post Treatment -- Zinc (Acid)

*Alaina -- Plating Posters Inc Creative Lead*
*v1.0 -- 2026-04-26*

Stages 7--8 of the acid chloride zinc process. Passivation, optional sealer, dry/cure, and hydrogen embrittlement bake. Structurally parallel to Poster #38 (Post Treatment -- Alkaline) with identical passivate chemistry (the passivation step is the same regardless of whether the zinc was deposited from acid or alkaline bath). The hero visual is the same tri vs. hex comparison with salt spray bar chart.

Key difference from Poster #38: expanded passivation type table (Watson's brief provides 8 distinct passivate variants with salt spray data), and the HE bake section references ASTM B850 timing specific to acid zinc plating (within 4 hours of plating, 4--24 hours hold).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Trivalent vs. Hexavalent hero (Block B):** Same concept as Poster #38.
2. **Salt spray bar chart (Block C):** Horizontal bars with hours to white rust.
3. **Passivate parameter table (Block D):** Full-width, expanded.
4. **Sealer + Dry/Cure (Block E):** Combined panel.
5. **Orientation strip:** Stages 7+8 highlighted.

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
ZONE 5 -- SEALER + DRY/CURE + HE BAKE (22.0"--27.0")
ZONE 6 -- COMMON PROBLEMS + SAFETY (27.0"--32.5")
ZONE 7 -- FOOTER (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header

**Headline:** `POST TREATMENT` -- 76 pt `#F0EDE8`. Y: 0.5".
**Subheading:** `Zinc (Acid) -- Passivate, Seal, Cure -- Stages 7 & 8` -- 30 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `The zinc is on. Now protect it. The difference between 24-hour and 500-hour salt spray is right here.` -- 20 pt at 65%. Y: 2.1".

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
- Title: `TRIVALENT CHROMATE (Cr3+)` Barlow SemiBold 22 pt `#27AE60`
- RoHS badge: fill `#27AE60`, text `RoHS COMPLIANT` Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Subtitle: `The Modern Standard` Inter Medium 14 pt `#F0EDE8` at 60%

Parameters (JetBrains Mono 14 pt):
```
pH:           1.5--2.5
Temperature:  70--90 F (21--32 C)
Time:         30--90 sec immersion
Chemistry:    Cr3+ salts (proprietary)
```

Color chips (4 small rectangles):
- Clear/Blue: fill `#87CEEB` at 50%, label `Clear / Blue` -- most common
- Yellow iridescent: fill `#DAA520` at 60%, label `Yellow Iridescent`
- Black: fill `#1A1F2E`, border 1 pt `#F0EDE8`, label `Black`
- Olive drab: fill `#6B8E23` at 60%, label `Olive Drab`

Performance: `SST: 24--72 hr white rust (no sealer) | 96--200+ hr (with sealer)` JetBrains Mono 13 pt `#27AE60`

**Right -- Hexavalent Chromate (X: 12.0", W: 11.5", H: 7.5"):**
- Rounded rect fill `#1E2435`, border 2 pt `#E8A020`
- Title: `HEXAVALENT CHROMATE (Cr6+)` Barlow SemiBold 22 pt `#E8A020`
- RoHS badge: fill `#E05C5C`, text `RoHS RESTRICTED` Barlow Condensed ExtraBold 12 pt `#1A1F2E`
- Subtitle: `Legacy -- Performance and Risk` Inter Medium 14 pt `#F0EDE8` at 60%

Parameters:
```
pH:           1.0--2.5
Temperature:  Ambient to 100 F
Time:         5--30 sec immersion
Chemistry:    Cr6+ (chromic acid based)
```

Color chips:
- Clear/Blue: fill `#87CEEB` at 40%
- Yellow: fill `#FFD700` at 70%, label `Yellow (classic iridescent)`
- Black: fill `#1A1F2E`, border 1 pt `#F0EDE8`
- Olive drab: fill `#556B2F` at 70%, label `Olive Drab (military)`

Performance: `SST: 96--500+ hr white rust | Self-healing property unique to hex` JetBrains Mono 13 pt `#E8A020`
Disadvantage: `CARCINOGENIC Cr6+ -- restricted under RoHS, REACH, ELV` Inter Medium 13 pt `#E05C5C`

---

**BLOCK C -- Salt Spray Comparison Bar Chart (Y: 13.3" to 15.8")**

Title: `SALT SPRAY PERFORMANCE (hours to white rust, ASTM B117)` Barlow Condensed ExtraBold 20 pt. Y: 13.3".

| Type | Hours | Bar Color |
|---|---|---|
| Bare zinc (no passivate) | 12--24 hr | `#E05C5C` |
| Tri clear (no sealer) | 24--72 hr | `#2EC4B6` |
| Tri clear + sealer | 96--200 hr | `#27AE60` |
| Tri black + sealer | 120--240 hr | `#27AE60` |
| Hex yellow | 96--200 hr | `#E8A020` |
| Hex yellow + sealer | 200--500 hr | `#E8A020` |

Each bar: Rounded rect, H: 0.3", fill at 70%. Label left (Inter Medium 12 pt), hours right (JetBrains Mono 12 pt).

---

### ZONE 4 -- Passivate Parameters Table

**Section label:** `PASSIVATION PARAMETERS -- DETAILED` -- Y: 16.2".

Full-width table:

| Parameter | Trivalent | Hexavalent | Notes |
|---|---|---|---|
| pH | 1.5--2.5 | 1.0--2.5 | Check 2x/shift minimum |
| Temperature | 70--90 F (21--32 C) | Ambient--100 F | Hex may need mild heat |
| Immersion time | 30--90 sec | 5--30 sec | Longer =/= better |
| Agitation | Gentle | Gentle | Excessive strips coating |
| Rinse before | Clean, < 100 uS/cm | Clean, < 100 uS/cm | Chloride is the enemy here |
| Rinse after | Immediate, gentle | Immediate, gentle | Aggressive rinse strips fresh film |
| Drain time | 10--15 sec | 10--15 sec | Allow excess to drip back |
| Replenishment | Per titration / TDS | Per titration / TDS | Cr3+ consumed by use |
| Tank material | PP or PVC (no metal) | PP or PVC (no metal) | Metal contamination kills bath |

---

### ZONE 5 -- Sealer + Dry/Cure + HE Bake

**Section label:** `SEALER, DRY/CURE & HYDROGEN BAKE` -- Y: 22.2".

Three panels side by side:

**Left -- Sealer (X: 0.5", W: 7.33"):**
- Rounded rect fill `#1E2435`, accent `#2EC4B6`
- Title: `TOPCOAT SEALER` Barlow SemiBold 18 pt `#2EC4B6`
- `Type: Organic or silicate-based`
- `Temp: 150--180 F (66--82 C)`
- `Time: 30--60 sec immersion`
- `Benefit: 2--3x salt spray increase`
- `Note: affects coefficient of friction -- check torque specs`

**Center -- Dry/Cure (X: 8.08", W: 7.33"):**
- Rounded rect fill `#1E2435`, accent `#E8A020`
- Title: `DRY / CURE` Barlow SemiBold 18 pt `#E8A020`
- `Method: Forced air, oven, or IR lamps`
- `Temp: 150--170 F (66--77 C)`
- `Time: 15--20 min minimum`
- `Under-curing: soft film, poor performance`
- `Over-curing (> 200 F): film degradation`

**Right -- HE Bake (X: 15.66", W: 7.84"):**
- Rounded rect fill `#1E2435`, FULL border 2 pt `#E05C5C`
- Title: `H-EMBRITTLEMENT BAKE` Barlow SemiBold 18 pt `#E05C5C`
- `Applies to: >= 145 ksi / >= 31 HRC steel`
- `Temp: 375 +/- 25 F (190 +/- 14 C)`
- `Time: 4--24 hours (per spec and hardness)`
- `To oven: within 4 hours of plating`
- `BAKE BEFORE PASSIVATION -- not after`
- Spec: `ASTM B850, AMS 2759/9` JetBrains Mono 11 pt `#E05C5C`

---

### ZONE 6 -- Problems + Safety

**Left -- Problems (X: 0.5", W: 14.0"):**

| Problem | Cause | Fix |
|---|---|---|
| No passivate color | pH too high or too low; contaminated bath | Check pH; dump and remake if contaminated |
| Patchy/uneven color | Chloride drag-in or poor rinse | Improve post-plate rinse; check Cl- |
| Passivate peeling | Over-immersion or over-agitation | Reduce time; gentle dip only |
| Poor salt spray | Under-curing or no sealer | Add sealer; ensure full cure time |
| Blistering after bake | HE bake done after passivation (not before) | ALWAYS bake before passivation |
| Short passivate bath life | Chloride accumulation from drag-in | Improve rinse; drag-out recovery tank |

**Right -- Safety (X: 15.0", W: 8.5"):**
- `Passivate baths are ACIDIC (pH 1.0--2.5) -- acid burns`
- `Hexavalent chromate: CARCINOGENIC -- full PPE + ventilation`
- `OSHA PEL for Cr6+: 5 ug/m3 -- medical surveillance required`
- `Trivalent: lower hazard but still acidic`
- `Sealer baths: hot (150--180 F) -- thermal burn risk`
- `All Cr6+ waste: REGULATED -- special treatment required`
- `Boric acid (EU): classified reproductive toxin (SVHC under REACH)`

---

### ZONE 7 -- Footer

Standard. Title: `Post Treatment -- Zinc (Acid)`. Version `v1.0 -- 2026`.

Disclaimer addition: `Hexavalent chromium processes are subject to regulatory restrictions (RoHS, REACH, ELV, OSHA PEL). Boric acid is classified as SVHC under EU REACH. Verify compliance with applicable regulations.`

---

## Parts 5--7

**Grouping:** 7 standard zones.
**Light Remap:** Standard table. RoHS badges and HE bake border: verify legibility on light background.

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

**Export:** Six files -- `Post Treatment Zinc Acid -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The passivation chemistry is identical whether the zinc came from an acid or alkaline bath -- the passivate reacts with the zinc deposit, not the bath chemistry underneath. The structural parallel to Poster #38 is intentional. Key differences: (1) the chloride drag-in issue is called out more prominently because acid zinc drag-out contains KCl; (2) the boric acid REACH/SVHC note is added to safety because it's relevant to the entire acid zinc process; (3) the HE bake panel is elevated to equal status with sealer and dry/cure because acid zinc is widely used on fasteners -- exactly the parts most likely to require HE baking.

---

*Alaina -- Plating Posters Inc Creative Lead*
*Poster #46 -- Construction Workup v1.0*
*2026-04-26*
