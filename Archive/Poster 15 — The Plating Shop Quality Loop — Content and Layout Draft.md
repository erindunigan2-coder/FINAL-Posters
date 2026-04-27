---
Project: Plating Posters Inc
Poster Number: 15
Title: "The Plating Shop Quality Loop: From Incoming Part to Final Inspection"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Plating Shop Quality Loop Research Brief v1 (2026-04-04)
Watson Flags: THREE — ZendoLIMS reference (Drew), AS9100D prominence (Drew), Nadcap naming (Drew) — all non-blocking
Process Scope: Cross-process quality control — applicable to all plating operations
Editions: Dark + Light
tags:
  - PosterDesign
  - QualityControl
  - ISO9001
  - ContentDraft
---

# Poster #15 — Content and Layout Draft
## The Plating Shop Quality Loop: From Incoming Part to Final Inspection

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Plating Shop Quality Loop Research Brief v1. This poster maps the seven-station quality control cycle that every plating shop must run — and shows what breaks when any station is skipped.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: THREE FLAGS — all Drew, non-blocking.**

**Flag 1 (Drew):** ZendoLIMS reference — should the poster include a subtle nod to digital quality management / LIMS? Recommendation: no. Keep the poster universally applicable. ZendoLIMS is a separate product conversation, not poster content.

**Flag 2 (Drew):** AS9100D vs. ISO 9001 prominence — the poster uses ISO 9001 as the primary framing (universal) with AS9100D mentioned where it adds specificity (aerospace). Confirm this balance.

**Flag 3 (Drew):** Nadcap naming — is referencing Nadcap AC7108 appropriate, or does it narrow the audience? Recommendation: include it in the specifications strip but not in the main body. The aerospace audience will recognize it; the commercial audience can ignore it.

**Design decisions:**

- **HERO: the circular quality wheel.** Seven stations arranged as segments of a wheel, connected by directional arrows. This is the poster's visual anchor — it communicates the continuous loop concept instantly from across the room. The feedback path from Station 7 back to Station 1 runs through the center as a bold return arrow.

- **Color assignment for stations:** Each station gets a color from the series palette based on its function:
  - Stations 1-2 (incoming + pre-treat): `#2EC4B6` Teal — "Plan" phase
  - Stations 3-5 (bath control + in-process + post-treat): `#E8A020` Amber — "Do" phase
  - Stations 6-7 (measurement + final inspection): `#27AE60` Emerald — "Check" phase
  - Feedback loop: `#E05C5C` Coral — "Act" phase

- **"What breaks if you skip this" consequence labels.** These are the poster's most attention-grabbing content. Each station gets a red-text consequence on the outer ring of the wheel. This transforms the poster from informational to motivational — it gives operators a reason to care about every station.

- **Hydrogen embrittlement warning panel.** Given standalone prominence. This is the most serious quality failure in the plating industry and Watson's brief flags it as deserving special treatment. I agree completely.

- **Special Process designation callout.** The ISO 9001 "special process" concept is the poster's philosophical core: you cannot inspect quality into a plated part — you must build it in during the process. This callout goes in the header area, not buried in the body.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "Special Process" callout (right ~45%)                         |
+------------------------------------------------------------------------+
| ZONE 2 — QUALITY WHEEL (HERO) (~8-52% / 15.8")                        |
| BLOCK C: Seven-station circular quality wheel with consequence labels    |
+------------------------------------------------------------------------+
| ZONE 3 — STATION DETAILS (~52-72% / 7.2")                             |
| BLOCK D: Station detail cards — 7 compact cards in two rows             |
+------------------------------------------------------------------------+
| ZONE 4 — H2 EMBRITTLEMENT + CALIBRATION (~72-85% / 4.7")              |
| BLOCK E: Hydrogen embrittlement warning panel (left 55%)                |
| BLOCK F: Calibration checklist + PDCA overlay (right 45%)               |
+------------------------------------------------------------------------+
| ZONE 5 — SPECIFICATIONS (~85-90% / 1.8")                              |
| BLOCK G: Specification reference strip                                   |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK H: Disclaimer + Series + Logo + Version                           |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + special process | 8% | 2.9" |
| 2 — Quality Wheel | HERO circular diagram | 44% | 15.8" |
| 3 — Station Details | Compact detail cards | 20% | 7.2" |
| 4 — Warnings + Tools | H₂ embrittlement + calibration | 13% | 4.7" |
| 5 — Specifications | Standards strip | 5% | 1.8" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 88 pt, `#F0EDE8`):**

> THE QUALITY LOOP

**Subheading (Barlow SemiBold, 36 pt, `#E8A020`):**

> From Incoming Part to Final Inspection

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> Quality isn't the final step. It's every step.

---

### BLOCK B — "Special Process" Callout (Header Right)

**Callout box:** fill `#1E2435`, border `#E05C5C` Coral 2 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#E05C5C`):**

> PLATING IS A SPECIAL PROCESS

**Body (Inter Regular, 15 pt, `#F0EDE8`):**

> You cannot look at a plated part and know if it will pass salt spray. You cannot see hydrogen trapped in steel. Quality must be built in during the process — it cannot be inspected in afterward.

**Standard reference (JetBrains Mono Regular, 12 pt, `#F0EDE8` at 70%):**

> ISO 9001:2015 Section 8.5.1

---

### BLOCK C — Quality Wheel (HERO — Zone 2)

**Section label (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):**

> THE SEVEN STATIONS OF PLATING QUALITY

**Wheel construction:** A circular diagram, approximately 14" in diameter, centered in the zone.

The wheel consists of:
1. **Seven arc segments** arranged clockwise, each representing one station
2. **Directional arrows** between segments showing process flow
3. **Station icons** inside each segment (Canva built-in icons or simple shapes)
4. **Station labels** (name + one-line description) radiating outward
5. **Consequence labels** in Coral on the outer ring
6. **Center text** inside the wheel
7. **Feedback arrow** from Station 7 back to Station 1 through the center

**Building the wheel in Canva:**
- The wheel is built as 7 pie-slice-shaped elements. In Canva, approximate this with 7 slightly overlapping curved/arc shapes, OR build as 7 rectangular cards arranged in a circular pattern around a central circle. **Recommended approach:** Use a large circle (`#1E2435` fill, `#3A4055` border, 2 pt) as the wheel background. Place 7 station label groups around the perimeter, evenly spaced at ~51-degree intervals. Connect with arrow lines (`#3A4055`, 2 pt). The visual metaphor is a clock face with stations instead of hours.

**Station positions (clockwise from top):**

| Station | Clock Position | Color | Label | Consequence |
|---------|---------------|-------|-------|-------------|
| 1 — Incoming | 12 o'clock | `#2EC4B6` | Incoming Part Inspection | Wrong alloy = contaminated bath |
| 2 — Pre-Treatment | ~2 o'clock | `#2EC4B6` | Pre-Treatment Verification | Skip = adhesion failure |
| 3 — Bath Control | ~3:30 | `#E8A020` | Bath Chemistry Control | Drift = invisible degradation |
| 4 — In-Process | ~5 o'clock | `#E8A020` | In-Process Monitoring | Bad contacts = non-uniform deposit |
| 5 — Post-Treatment | ~6:30 | `#E8A020` | Post-Treatment Verification | Missed bake = catastrophic failure |
| 6 — Measurement | ~8 o'clock | `#27AE60` | Thickness and Property Testing | Under-thickness = field failure |
| 7 — Final | ~10 o'clock | `#27AE60` | Final Inspection and Documentation | No traceability = audit failure |

**Station icon suggestions (Canva search terms):**
1. Magnifying glass (search: "inspect")
2. Water droplet (search: "water drop")
3. Flask / beaker (search: "chemistry")
4. Gauge / meter (search: "gauge")
5. Thermometer (search: "temperature")
6. Ruler / measurement (search: "measure")
7. Clipboard with checkmark (search: "checklist")

Icon size: ~0.8" x 0.8", colored per station accent.

**Center of wheel:**

Large circle, `#1A1F2E` fill (matches background), bordered by `#3A4055`, 3 pt.

Center text (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`):
> CERTIFIED.
> EVERY TIME.

Below center text (Inter Regular, 14 pt, `#F0EDE8` at 60%):
> Plan - Do - Check - Act

**Feedback arrow:**
- A bold curved arrow from Station 7 position back to Station 1 position, passing through or near the center
- Color: `#E05C5C` Coral, 3 pt stroke, arrow head at Station 1 end
- Label along arrow: `CORRECTIVE ACTION` — Barlow SemiBold, 14 pt, `#E05C5C`

**PDCA quadrant shading (subtle):**
- Behind Stations 1-2: very faint `#2EC4B6` at 5% opacity — "PLAN"
- Behind Stations 3-5: very faint `#E8A020` at 5% opacity — "DO"
- Behind Stations 6-7: very faint `#27AE60` at 5% opacity — "CHECK"
- Feedback arrow area: very faint `#E05C5C` at 5% opacity — "ACT"

Quadrant labels (Barlow SemiBold, 16 pt, respective accent color at 40% opacity):
> PLAN  |  DO  |  CHECK  |  ACT

---

### BLOCK D — Station Detail Cards (Zone 3)

**Layout:** Two rows of cards. Row 1: Stations 1-4. Row 2: Stations 5-7 + one summary card.

Each card is approximately 5.5" wide x 3.3" tall. Row of 4 cards = 23.0" across (with 0.33" gaps).

**Card construction:**
- Fill: `#1E2435` Dark Callout
- Left-border accent: 4 pt, station color
- Corner radius: 6 pt
- Internal padding: 12 pt

**Card content template:**

Station number + name (Barlow SemiBold, 14 pt, station color):
> STATION 1: INCOMING INSPECTION

Key checks (Inter Regular, 12 pt, `#F0EDE8`, bullet list):
> - Surface condition
> - Material identification
> - Drawing / spec review
> - Quantity verification

Quality gate (Inter Medium, 11 pt, `#27AE60`):
> GATE: Reject before plating line entry.

---

**Card data:**

**Station 1 — Incoming Inspection** (Teal)
- Surface condition, material ID, dimensional check, documentation review
- Gate: Parts failing inspection are quarantined — do not enter plating line.

**Station 2 — Pre-Treatment** (Teal)
- Cleaner concentration, electrocleaner V/A, acid activation, rinse conductivity
- Gate: Water break test — continuous film, no beading.

**Station 3 — Bath Chemistry** (Amber)
- pH, metal concentration (titration), buffer level, Hull cell, temperature
- Gate: Out-of-spec chemistry corrected before production resumes.

**Station 4 — In-Process Monitoring** (Amber)
- Rectifier V/A, current density, temperature, agitation, rack/barrel condition
- Gate: Deviation from parameters requires intervention or hold.

**Station 5 — Post-Treatment** (Amber)
- Passivation pH/temp/time, sealer application, H₂ embrittlement bake, drying
- Gate: Bake oven calibrated with recording chart or data logger.

**Station 6 — Thickness + Properties** (Emerald)
- XRF (ASTM B568), magnetic induction (B499), salt spray (B117), adhesion (B571)
- Gate: Parts failing measurement are quarantined and dispositioned.

**Station 7 — Final Inspection + Docs** (Emerald)
- Visual inspection, thickness records, salt spray results, bake cert, CoC, lot traceability
- Gate: Release authority signs off. No shipment without signed CoC.

**Summary card — FEEDBACK LOOP** (Coral)
- Salt spray failures trace to Stations 3 + 5
- Adhesion failures trace to Stations 1 + 2
- Customer complaints trigger 8D/CAPA
- Internal audits verify all stations functioning
- Gate: Management review per ISO 9001 Section 9.3.

---

### BLOCK E — Hydrogen Embrittlement Warning (Zone 4 — Left)

**Callout box:** fill `#1E2435`, border `#E05C5C` Coral 2 pt, corner radius 8 pt

**Warning icon:** Canva "alert triangle" or "warning" icon, `#E05C5C`, 1.0" x 1.0", positioned top-left inside box

**Title (Barlow Condensed ExtraBold, 22 pt, `#E05C5C`):**

> HYDROGEN EMBRITTLEMENT — THE CRITICAL WINDOW

**Body (Inter Regular, 15 pt, `#F0EDE8`):**

> High-strength steel parts (>40 HRC / >1000 MPa) must be baked within 4 hours of plating completion. Some specs require 1 hour. Delayed or omitted baking risks catastrophic brittle fracture — the most dangerous failure mode in the plating industry.

**Key data (JetBrains Mono Regular, 16 pt, `#F0EDE8`):**

> Bake temp:  190 C (375 F)
> Duration:   4-24 hours (per spec)
> Deadline:   Within 4 hrs of plating
> Threshold:  >40 HRC or >1000 MPa

**Standards (JetBrains Mono Regular, 12 pt, `#F0EDE8` at 60%):**

> ASTM B850 | AMS 2759/9 | ASTM B633

---

### BLOCK F — Calibration Checklist (Zone 4 — Right)

**Callout box:** fill `#1E2435`, border `#27AE60` Emerald 1.5 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#27AE60`):**

> IF IT MEASURES, IT MUST BE CALIBRATED

**Checklist (Inter Regular, 14 pt, `#F0EDE8`):**

- pH meter (2-point calibration before each use)
- Thermometer / RTD probe
- XRF thickness gauge
- Microhardness tester
- Bake oven temperature controller
- Rectifier ammeter and voltmeter
- Ampere-hour meter

**Standard reference (JetBrains Mono, 12 pt, `#F0EDE8` at 60%):**

> ISO 9001:2015 Section 7.1.5 — Monitoring and measuring resources

---

### BLOCK G — Specification Reference Strip (Zone 5)

**Full-width strip:** background `#1E2435`, 1.5" tall.

**Title (left):** `GOVERNING STANDARDS` — Barlow SemiBold, 16 pt, `#F0EDE8`

**Standards in a horizontal row (JetBrains Mono Regular, 13 pt, `#F0EDE8` at 80%, separated by vertical `#3A4055` dividers):**

> ASTM B633  |  B117  |  B571  |  B568  |  B487  |  B499  |  ISO 9001  |  AS9100D  |  Nadcap AC7108

---

### BLOCK H — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents a generalized plating shop quality loop applicable to most electroplating operations. Specific quality requirements vary by customer specification, industry sector, and regulatory environment. Consult your quality management system documentation for site-specific procedures.`

**Poster title:** `The Plating Shop Quality Loop`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The quality wheel uses multiple accent colors (Teal, Amber, Emerald, Coral) — all remap to their darkened Light equivalents per standard table.

The PDCA quadrant shading (5% opacity tints) may be imperceptible on the Light background. Either increase to 8-10% opacity in Light edition, or remove entirely — the PDCA labels alone are sufficient. Verify at build time.

Station detail card left-border accents remap normally. No overrides anticipated.

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Drew (OPEN):** ZendoLIMS reference (recommendation: omit), AS9100D prominence, Nadcap naming.

**Tyler (OPEN):** Confirm titration methods at Station 3 align with A Brite Generic Methods library (GM-001 through GM-006).

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #15 — The Plating Shop Quality Loop — Content and Layout Draft v1.0*
*2026-04-04*
