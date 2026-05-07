---
Project: Plating Posters Inc
Poster Number: 7
Title: "Metallic Contamination — Know Your Thresholds"
Document Type: Content and Layout Draft
Status: v1.0 — Ready for Canva Construction Workup
Created: 2026-04-04T00:00:00
Author: Alaina (poster-designer)
Technical Source: Watson — Metallic Contamination Research Brief v1 (2026-04-03)
Watson Flags: TWO — Cu-in-Ni threshold (3 vs. 5 ppm) + include treatment methods or thresholds only (both Drew, non-blocking)
Process Scope: Cross-process contamination reference — nickel, copper, chrome, zinc, passivation
Editions: Dark + Light
tags:
  - PosterDesign
  - MetallicContamination
  - Troubleshooting
  - ContentDraft
---

# Poster #7 — Content and Layout Draft
## Metallic Contamination — Know Your Thresholds

*Alaina — Plating Posters Inc Creative Lead*
*v1.0 — 2026-04-04*
*Content sourced from Watson's Metallic Contamination Research Brief v1. This poster gives operators and lab technicians a single wall reference for dangerous metal thresholds by bath type.*

---

## Section 1 — Watson Flag Status and Design Decisions

**Status: TWO FLAGS — both Drew, non-blocking.**

**Flag 1 (Drew):** Copper in bright nickel threshold — 3 ppm (very conservative) or 5 ppm (more common)? Watson notes 3 ppm is widely cited but some formulations tolerate higher. Poster currently uses ">3-5 ppm" as a range.

**Flag 2 (Drew):** Include treatment methods or focus purely on thresholds and effects? My recommendation: include both. Treatment adds shop-floor utility and operators will look for "what do I do?" right after "how bad is it?" The poster has room.

**Design decisions:**

- **HERO: the master contamination threshold table.** This is a data-dense poster by nature — the table IS the product. Four bath-type sections (Nickel, Copper, Chrome, Zinc) with contaminant rows showing ppm limits, effects, and treatment. Color-coded by severity.

- **Supporting visual: "How Metals Get In" tank diagram.** A plating tank with arrows pointing to the six contamination sources (dissolving racks, dropped parts, drag-in, corroded equipment, impure anodes, bad water). This makes the concept concrete and engaging.

- **Prevention checklist as the closing action item.** The poster ends with "what can I do right now" — bag anodes, maintain racks, rinse well, test regularly, use pure water, use pure anodes.

- **Severity color coding:** Emerald for safe/below threshold, Amber for warning/approaching, Coral for danger/above threshold. These map naturally to the series semantics.

---

## Section 2 — Layout Zone Map

```
+------------------------------------------------------------------------+
| ZONE 1 — HEADER BAND (~0-8% / 2.9")                                    |
| BLOCK A: Headline + subheading + tagline (left ~55%)                    |
| BLOCK B: "Most Dangerous" callout box (right ~45%)                      |
+------------------------------------------------------------------------+
| ZONE 2 — HOW METALS GET IN (~8-22% / 5.0")                            |
| BLOCK C: Tank diagram with contamination source arrows                   |
+------------------------------------------------------------------------+
| ZONE 3 — CONTAMINATION TABLE (HERO) (~22-72% / 18.0")                 |
| BLOCK D: Four-section master threshold table                             |
| Nickel | Acid Copper | Hard Chrome | Acid Zinc                          |
+------------------------------------------------------------------------+
| ZONE 4 — DETECTION + TREATMENT (~72-86% / 5.0")                       |
| BLOCK E: Detection methods (left 40%)                                    |
| BLOCK F: Treatment quick reference (right 60%)                           |
+------------------------------------------------------------------------+
| ZONE 5 — PREVENTION CHECKLIST (~86-90% / 1.4")                        |
| BLOCK G: Horizontal prevention checklist strip                           |
+------------------------------------------------------------------------+
| ZONE 6 — FOOTER BAND (~90-100% / 3.6")                                 |
| BLOCK H: Disclaimer + Series + Logo + Version                            |
+------------------------------------------------------------------------+
```

**Zone height summary:**
| Zone | Content | % Height | Approx Inches |
|------|---------|----------|---------------|
| 1 — Header | Headline + most dangerous | 8% | 2.9" |
| 2 — Sources | Tank contamination diagram | 14% | 5.0" |
| 3 — Threshold Table | HERO data block | 50% | 18.0" |
| 4 — Detection + Treatment | Methods + quick ref | 14% | 5.0" |
| 5 — Prevention | Checklist strip | 4% | 1.4" |
| 6 — Footer | Disclaimer + metadata | 10% | 3.6" |
| **Total** | | **100%** | **36.0"** |

---

## Section 3 — Content Blocks

---

### BLOCK A — Headline and Subheading

**Headline (Barlow Condensed ExtraBold, 96 pt, `#F0EDE8`):**

> METALLIC CONTAMINATION

**Subheading (Barlow SemiBold, 40 pt, `#E8A020`):**

> Know Your Thresholds

**Tagline (Barlow SemiBold, 22 pt, `#F0EDE8` at 65% opacity):**

> Contamination is always easier to prevent than to remove.

---

### BLOCK B — "Most Dangerous" Callout Box (Header Right)

**Callout box:** fill `#1E2435`, border `#E05C5C` Coral 2 pt, corner radius 8 pt

**Title (Barlow SemiBold, 18 pt, `#E05C5C`):**

> MOST DANGEROUS CONTAMINANT PER BATH

**List (JetBrains Mono Regular, 15 pt, `#F0EDE8`):**

> Nickel:      Cu > 3 ppm
> Acid copper:  Cr⁶⁺ > 2 ppm
> Hard chrome: Cl⁻ > 50 ppm
> Acid zinc:   Cr⁶⁺ > 1 ppm
> Passivation: Fe > 100 ppm

**Closing (Inter Medium, 14 pt, `#E05C5C`):**

> These are the numbers that turn good parts into scrap.

---

### BLOCK C — "How Metals Get In" Tank Diagram (Zone 2)

**Section label (Barlow Condensed ExtraBold, 26 pt, `#F0EDE8`, centered):**

> HOW CONTAMINATION ENTERS YOUR BATH

**Illustration:** A simplified plating tank cross-section (centered, ~16" wide x 3.5" tall) with 6 labeled arrows pointing to contamination sources:

Tank: Rounded rectangle, `#3A4055` outline, `#1E2435` fill. Interior suggests electrolyte with subtle `#2EC4B6` horizontal lines at 20% opacity.

**Arrow labels (positioned around the tank):**

1. **Top left (above tank):** Arrow pointing down into tank
   - Label: `Impure anodes` — Inter Medium, 14 pt, `#E8A020`
   - Sub: `Lead, copper in anode material` — Inter Regular, 11 pt, `#F0EDE8` at 70%

2. **Top right (above tank):** Arrow pointing down
   - Label: `Drag-in from other tanks` — Inter Medium, 14 pt, `#E8A020`
   - Sub: `Chrome, acid, organics carried on parts/racks` — Inter Regular, 11 pt

3. **Left side (pointing right into tank wall):**
   - Label: `Corroding equipment` — Inter Medium, 14 pt, `#E05C5C`
   - Sub: `Heaters, pumps, tank linings` — Inter Regular, 11 pt

4. **Right side (pointing left into tank wall):**
   - Label: `Dissolving racks` — Inter Medium, 14 pt, `#E05C5C`
   - Sub: `Iron, copper from steel/brass fixtures` — Inter Regular, 11 pt

5. **Bottom center (inside tank, arrow pointing to tank floor):**
   - Label: `Dropped parts` — Inter Medium, 14 pt, `#E05C5C`
   - Sub: `Dissolve in bath over time` — Inter Regular, 11 pt

6. **Bottom right (water line into tank):**
   - Label: `Make-up water` — Inter Medium, 14 pt, `#E8A020`
   - Sub: `Iron, copper, calcium from municipal supply` — Inter Regular, 11 pt

---

### BLOCK D — Master Contamination Threshold Table (HERO — Zone 3)

**Section label (Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`, centered):**

> CONTAMINATION THRESHOLDS BY BATH TYPE

**Table structure:** Full width, organized in 4 bath-type sections stacked vertically. Each section has its own section header row, then contaminant data rows.

**Column structure (5 columns):**
1. **Contaminant** (~18%) — Inter Medium, 16 pt
2. **Threshold** (~15%) — JetBrains Mono, 16 pt, severity-colored
3. **Effect** (~30%) — Inter Regular, 15 pt
4. **Treatment** (~25%) — Inter Regular, 14 pt
5. **Severity** (~12%) — left-border accent (4 pt) color-coded

Column header row (top of entire table): `#3A4055` fill, Barlow SemiBold 18 pt.

---

**Section A — NICKEL BATHS** (section header: `#3A4055` fill, `NICKEL BATHS` in Barlow SemiBold 20 pt, `#E8A020`)

| Contaminant | Threshold | Effect | Treatment | Severity |
|-------------|-----------|--------|-----------|----------|
| Copper (Cu) | >3-5 ppm (bright) | Dark LCD deposits; poor adhesion | Dummy at 2-5 ASF | Coral |
| Zinc (Zn) | >20-50 ppm | White/dark LCD; shiny black streaks | Dummy at 2-5 ASF; pH 5.5 | Coral |
| Iron (Fe) | >50-150 ppm | Speckling; roughness; discoloration | pH 5.0-5.5 + H₂O₂ → filter | Amber |
| Lead (Pb) | >1-5 ppm | Dark streaks; brittleness | Carbon + electrolytic | Coral |
| Chromium (Cr⁶⁺) | >5-10 ppm | Brightness loss; pitting | Dummy at 1-2 ASF | Coral |
| Aluminum (Al) | >60 ppm | Reduced limiting CD; rough | Cannot remove — dilute | Amber |
| Cadmium (Cd) | >1-2 ppm | Brittleness; adhesion failure | Dummy; prevent ingress | Coral |

**Section B — ACID COPPER** (section header: `ACID COPPER BATHS` in `#2EC4B6`)

| Contaminant | Threshold | Effect | Treatment | Severity |
|-------------|-----------|--------|-----------|----------|
| Iron (Fe) | >500-1000 ppm | Reduced conductivity; rough | Dilute; prevent ingress | Amber |
| Zinc (Zn) | >25 ppm | Brittle, brassy deposits | Dummy at 2 ASF | Amber |
| Tin (Sn) | >60 ppm | Rough, dark deposits | Dummy plate | Amber |
| Chromium (Cr⁶⁺) | >2-5 ppm | Skip plating; dull deposits | Na₂S₂O₅ → filter | Coral |
| Chloride (Cl⁻) | >50-80 ppm | Pitting; anode corrosion | Prevent drag-in; no removal | Coral |

**Section C — HARD CHROME** (section header: `HARD CHROME BATHS` in `#E05C5C`)

| Contaminant | Threshold | Effect | Treatment | Severity |
|-------------|-----------|--------|-----------|----------|
| Iron (Fe) | >5 g/L | Roughness; reduced coverage | Dummy at low CD (limited) | Amber |
| Copper (Cu) | >2 g/L | Dark deposits; roughness | Dummy at low CD | Amber |
| Trivalent Cr (Cr³⁺) | >2-3% of total Cr | Poor coverage; dull | Porous pot electrolysis | Coral |
| Chloride (Cl⁻) | >50 ppm; target <20 | Severe pitting; etching | Low area/high CD; prevent | Coral |

**Section D — ACID ZINC** (section header: `ACID ZINC BATHS` in `#27AE60`)

| Contaminant | Threshold | Effect | Treatment | Severity |
|-------------|-----------|--------|-----------|----------|
| Iron (Fe) | >25-50 ppm | Dark; roughness; poor brightness | H₂O₂ at pH 5.5-6.0 → filter | Amber |
| Copper (Cu) | >10-20 ppm | Dark/reddish LCD; immersion deposit | Dummy at 2-5 ASF | Coral |
| Lead (Pb) | >2-5 ppm | Dark streaks; brittleness | Dummy; prevent ingress | Coral |
| Chromium (Cr⁶⁺) | >1-2 ppm | Skip plating; poor coverage | Na₂S₂O₅ → filter | Coral |

---

### BLOCK E — Detection Methods (Zone 4 — Left)

**Section label (Barlow Condensed ExtraBold, 20 pt, `#F0EDE8`):**

> HOW TO DETECT

Compact table (2 columns: Method | Use):

| Method | Use |
|--------|-----|
| Atomic Absorption (AA) | Gold standard — sub-ppm sensitivity |
| ICP-OES | Multiple metals simultaneously |
| Hull cell (low CD) | Shop-floor screening — visual |
| Colorimetric kits | Quick field check (5-50 ppm) |
| Dummying response | Diagnostic — "does dummying help?" |

---

### BLOCK F — Treatment Quick Reference (Zone 4 — Right)

**Three stacked callout boxes:**

**Dummy Plating (Emerald accent):**
Title: `DUMMY PLATING`
Body: `Corrugated mild steel cathodes at 2-5 ASF for 4-24 hours. Contaminant metals plate out preferentially at low CD because they are more noble than the bath metal. Monitor by Hull cell.`

**Chemical Precipitation (Amber accent):**
Title: `IRON REMOVAL (NICKEL BATHS)`
Body: `Raise pH to 5.0-5.5. Add H₂O₂ (30%) at 0.1-0.3 mL/L. Iron precipitates as Fe(OH)₃. Filter through 1 um. Lower pH to operating range.`

**Carbon Treatment (Teal accent):**
Title: `CARBON TREATMENT`
Body: `2-5 g/L powdered activated carbon. Mix, settle 2-4 hrs, filter through 1 um. Removes organic breakdown products alongside metallic contamination.`

---

### BLOCK G — Prevention Checklist Strip (Zone 5)

**Full-width strip:** background `#1E2435`, 1.2" tall.

**Title (left):** `PREVENTION IS CHEAPER THAN TREATMENT` — Barlow SemiBold, 16 pt, `#27AE60`

**6 items in a horizontal row, each with a checkmark icon and label:**

- Bag your anodes
- Maintain your racks
- Rinse thoroughly
- Test monthly (Ni) / quarterly (Cu, Zn)
- Use pure water (DI/RO)
- Use pure anodes

Font: Inter Regular, 13 pt, `#F0EDE8`. Checkmark icons: `#27AE60` Emerald.

---

### BLOCK H — Footer Content

Standard footer per series convention.

**Band fill:** `#0D1020` Deep Navy

**Disclaimer:** `This poster presents industry-typical contamination thresholds. Specific limits vary by vendor formulation — always check the product TDS. Analysis by AA or ICP is the authoritative method for confirming contamination levels.`

**Poster title:** `Metallic Contamination — Know Your Thresholds`
**Series name:** `Plating Posters Inc — Metal Finishing Reference Series`
**Version:** `v1.0 — 2026`
**Logo:** `[LOGO]`

---

## Section 4 — Light Edition Notes

Standard remap table applies. The severity color-coded left-border accents (Coral, Amber, Emerald) remap to their darkened Light equivalents. Bath section headers use accent colors as text — these remap normally. No overrides anticipated.

---

## Section 5 — Collaboration Flags

**Watson:** Research complete. No additional research needed.

**Drew (OPEN):** Cu-in-Ni threshold (3 vs. 5 ppm). Include treatment methods? (Recommendation: yes.)

**Tyler (OPEN):** Review iron precipitation method (pH raise + H₂O₂ + filter) — confirm matches actual lab practice.

---

*Alaina — Plating Posters Inc Creative Lead*
*Poster #7 — Metallic Contamination — Content and Layout Draft v1.0*
*2026-04-04*
