---
Project: Plating Posters Inc
Poster Number: 716
Title: "Rinse / Dry -- Protective Coatings"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief"
Technical Source: Rinse and dry requirements for steel and concrete before protective coating. Steel follows the same no-rinse-after-blast rule as Cluster 7. Concrete requires 24+ hours drying after water wash or acid etch. Dew point monitoring (5 deg F rule) applies to both substrates.
Process Scope: Rinse / dry for protective coatings -- Stage 3 of 8
Editions: Dark (flagship) + Light (accessible print)
tags:
  - PosterDesign
  - ProtectiveCoatings
  - RinseDry
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #716 -- Construction Workup
## Rinse / Dry -- Protective Coatings

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 3 of 8. This poster covers the rinse/dry requirements for both steel and concrete. For steel, the rule is identical to Cluster 7: no rinse after blast, prime before flash rust. For concrete, the situation is fundamentally different -- concrete must dry for 24+ hours after water wash or acid etch, and moisture must be verified by ASTM F1869 or F2170 before coating. The hero is a dual-track drying timeline showing steel (hours) vs. concrete (days/weeks).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual-track drying timeline hero (Block B):** Steel timeline (hours) and concrete timeline (days/weeks) shown in parallel. Horizontal timelines with markers.
2. **Dew point monitoring panel (Block D):** 5 deg F rule, ASTM E337, digital dew point meters.
3. **Concrete drying deep-dive (Block E):** New concrete curing time, slab thickness effects, vapor barriers.
4. **Steel blast-to-coat window (Block F):** Cross-reference to Cluster 7 with humidity-dependent windows.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 21.0" / 27.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 3 highlighted (Teal)
ZONE 3 -- DUAL-TRACK DRYING HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- DEW POINT MONITORING (14.5"--21.0" / ~6.5")
ZONE 5 -- CONCRETE DRYING DEEP DIVE (21.0"--27.0" / ~6.0")
ZONE 6 -- STEEL BLAST-TO-COAT + COMMON MISTAKES (27.0"--32.5" / ~5.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE / DRY` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Protective Coatings -- Stage 3 of 8` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `Steel dries in hours. Concrete dries in weeks. Know your substrate's timeline -- or trap moisture under the coating.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned/washed substrate  -->  After: Dry, verified surface at correct temperature for coating`

---

### ZONE 3 -- Dual-Track Drying Hero

**Section label:** `DRYING TIMELINES -- STEEL VS. CONCRETE` -- Y: 4.4".

**BLOCK B -- Dual Timeline (Y: 5.0" to 14.0")**

**Top -- Steel Timeline (Y: 5.0" to 9.0"):**
- Large rounded rect, X: 0.5", W: 23.0", H: 3.5", fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `STEEL -- HOURS` Barlow SemiBold 22 pt `#2EC4B6`

Horizontal timeline bar (X: 2.0", Y: 7.0", W: 21.0", H: 1.0"):
- Three segments:
  - `0--4 hr` fill `#27AE60` at 50% -- `PRIME NOW` JetBrains Mono 14 pt `#27AE60`
  - `4--8 hr` fill `#E8A020` at 40% -- `CAUTION` JetBrains Mono 14 pt `#E8A020`
  - `8+ hr` fill `#E05C5C` at 40% -- `RE-BLAST` JetBrains Mono 14 pt `#E05C5C`

Key rules (below bar):
- `If salt wash was used: allow full drying BEFORE blasting`
- `After blast: NO RINSE. Apply primer before flash rust.`
- Inter Regular 13 pt `#F0EDE8`

**Bottom -- Concrete Timeline (Y: 9.5" to 14.0"):**
- Large rounded rect, X: 0.5", W: 23.0", H: 4.0", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `CONCRETE -- DAYS TO WEEKS` Barlow SemiBold 22 pt `#E8A020`

Horizontal timeline bar (X: 2.0", Y: 11.5", W: 21.0", H: 1.0"):
- Three segments:
  - `0--24 hr` fill `#E05C5C` at 50% -- `TOO WET` JetBrains Mono 14 pt `#E05C5C`
  - `1--7 days` fill `#E8A020` at 40% -- `TEST MOISTURE` JetBrains Mono 14 pt `#E8A020`
  - `7+ days (new pour: 28+ days)` fill `#27AE60` at 40% -- `LIKELY READY -- VERIFY` JetBrains Mono 14 pt `#27AE60`

Key rules (below bar):
- `After water wash or acid etch: minimum 24 hours drying`
- `New concrete: minimum 28 days curing before coating`
- `ALWAYS test with ASTM F2170 (< 75% RH) or F1869 (< 3 lb/1,000 ft2/24 hr)`
- Inter Regular 13 pt `#F0EDE8`

Contrast callout (Y: 13.5"):
- Pill-shaped, fill `#E8A020` at 15%, border 1 pt `#E8A020`, W: 23.0", H: 0.4"
- Text: `Steel is measured in hours. Concrete is measured in days. Never apply the steel timeline to concrete.` Inter Medium 13 pt `#E8A020`

---

### ZONE 4 -- Dew Point Monitoring

**Section label:** `DEW POINT -- THE 5 DEG F RULE (BOTH SUBSTRATES)` -- Y: 14.7".

**Full-width callout (Y: 15.3" to 20.8"):**

Big stat: `5 deg F` Barlow Condensed ExtraBold 72 pt `#E8A020` (centered)
Subtitle: `Minimum surface temperature above dew point` Barlow SemiBold 22 pt `#F0EDE8`

Two-column detail below stat:

**Left -- Why It Matters (X: 0.5", W: 11.0"):**
- `Surface temperature must exceed dew point by at least 5 deg F (3 deg C)`
- `If surface temp drops to dew point: invisible moisture condenses on the surface`
- `On steel: causes flash rust or adhesion failure under coating`
- `On concrete: adds moisture to an already moisture-sensitive substrate`
- `On uncured epoxy: causes amine blush (carbamate formation)`
- Inter Regular 14 pt `#F0EDE8`

**Right -- Measurement Methods (X: 12.0", W: 11.5"):**

| Method | Tool | Standard |
|---|---|---|
| Sling psychrometer + surface thermometer | Manual calculation | ASTM E337 |
| Digital dew point meter | Direct reading | Faster, more convenient |
| Infrared surface thermometer | Non-contact surface temp | Verify calibration |

Data: JetBrains Mono 12 pt.

Monitoring rule: `Check and record at start of each shift and whenever ambient conditions change. Log in coating inspection report. If conditions deteriorate mid-shift, STOP application.` Inter Medium 13 pt `#E8A020`.

---

### ZONE 5 -- Concrete Drying Deep Dive

**Section label:** `CONCRETE DRYING -- WHY IT TAKES SO LONG` -- Y: 21.2".

**Two-column layout (Y: 21.8" to 26.8"):**

**Left -- Drying Variables (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`

| Variable | Effect on Drying |
|---|---|
| Slab thickness | Thicker = much longer (Rule of thumb: 1 month per inch of thickness for new concrete) |
| Ambient RH | High humidity slows drying dramatically |
| Vapor barrier below slab | Without barrier: ground moisture migrates up continuously |
| Concrete mix design | Higher water-cement ratio = more moisture to remove |
| Temperature | Warmer = faster drying |
| Air circulation | Good ventilation accelerates surface drying |

Data: Inter Regular 13 pt `#F0EDE8`. Variables: Inter Medium 13 pt `#E8A020`.

**Right -- Moisture Migration (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `MOISTURE VAPOR TRANSMISSION` Barlow SemiBold 16 pt `#E05C5C`

Content:
- `Even "dry" concrete transmits moisture vapor from the ground through the slab`
- `Without a vapor barrier below the slab, this is a continuous process`
- `The coating must either:`
- `  1. Block the moisture (dense epoxy barrier) -- risk of blistering`
- `  2. Breathe (moisture-tolerant primer) -- limited chemical resistance`
- `No coating can permanently seal a slab with active moisture migration above F1869 limits`
- Inter Regular 13 pt `#F0EDE8`

Warning: `If MVER exceeds 3 lb/1,000 ft2/24 hr: DO NOT coat. Address the moisture source first (install vapor barrier, dehumidify, or wait).` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Steel Blast-to-Coat + Common Mistakes

**Two-column layout (Y: 27.2" to 32.3"):**

**Left -- Steel Blast-to-Coat Window (X: 0.5", W: 11.0"):**

Section label: `STEEL -- BLAST-TO-COAT WINDOW` Barlow Condensed ExtraBold 22 pt `#2EC4B6`.

| RH Range | Window | Action |
|---|---|---|
| < 50% | 8 hours max | Standard workflow |
| 50--80% | 4 hours | Plan blast and coat together |
| > 80% | 1--2 hours | Blast small areas, coat immediately |
| Rain / dew | Zero | Do not blast |

Data: JetBrains Mono 12 pt.

Cross-reference: `See Poster #707 (Rinse -- Priming) for full blast-to-prime window detail.` Inter Regular 12 pt `#F0EDE8` at 50%.

**Right -- Common Mistakes (X: 12.0", W: 11.5"):**

Section label: `DRYING MISTAKES` Barlow Condensed ExtraBold 22 pt `#E05C5C`.

| Mistake | Consequence |
|---|---|
| Coat concrete without moisture test | Blistering, delamination within weeks |
| Allow blasted steel to sit overnight | Flash rust = re-blast required |
| Ignore dew point mid-shift | Invisible condensation under coating |
| Assume new concrete is "dry enough" at 14 days | Likely still above 75% RH |
| Coat over standing water in recesses | Immediate adhesion failure |

Each: small card, fill `#1E2435`, left accent `#E05C5C`.

---

### ZONE 7 -- Footer

Standard. Title: `Rinse / Dry -- Protective Coatings`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; ASTM E337; ASTM F1869; ASTM F2170; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Dry Protective Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual-track timeline hero is the money shot -- it makes the steel-vs-concrete time difference viscerally obvious. Steel is hours, concrete is weeks. Anyone who applies the steel timeline to concrete is going to trap moisture and destroy the coating. The dew point big-stat section echoes Poster #707, reinforcing this critical environmental check. The concrete drying deep-dive addresses the fundamental physics of moisture vapor transmission -- even "dry" concrete without a vapor barrier transmits moisture continuously.

---

*Alaina -- Poster #716 -- Construction Workup v1.0 -- 2026-04-26*
