---
Project: Plating Posters Inc
Poster Number: 717
Title: "Pretreatment -- Protective Coatings"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief (Section 8.5)"
Process Scope: Pretreatment for protective coatings -- Stage 4 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ProtectiveCoatings
  - Pretreatment
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #717 -- Construction Workup
## Pretreatment -- Protective Coatings

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 4 of 8. Pretreatment in protective coatings is not what most painters expect -- for the most demanding applications, there is no conversion coating. On steel, the blast profile IS the pretreatment. A zinc-rich primer applied directly to bare, profiled steel provides galvanic protection; adding a phosphate conversion coating would insulate the zinc from the steel and defeat the purpose. On concrete, the mechanical profile from grinding or blasting is the adhesion mechanism. This poster maps the fundamentally different pretreatment strategies for steel vs. concrete.

Hero visual: dual-track pretreatment decision tree -- steel (left) vs. concrete (right) -- showing what goes on the surface before primer.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Dual pretreatment decision tree hero (Block B):** Steel path and concrete path shown side by side with decision points.
2. **Steel pretreatment by application tier (Block D):** General industrial vs. immersion service vs. marine.
3. **Concrete pretreatment detail (Block E):** Moisture testing, pH, profile, and no-sealer rules.
4. **Defect strip (Block F):** 4 pretreatment failures.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 20.5" / 26.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Amber)
ZONE 3 -- DUAL PRETREATMENT DECISION HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- STEEL PRETREATMENT BY TIER (14.5"--20.5" / ~6.0")
ZONE 5 -- CONCRETE PRETREATMENT DETAIL (20.5"--26.5" / ~6.0")
ZONE 6 -- PRETREATMENT FAILURES (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `PRETREATMENT` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Protective Coatings -- Stage 4 of 8` -- 32 pt `#E8A020` (Amber). Y: 1.4".
**Tagline:** `On steel, the blast profile IS the pretreatment. On concrete, the grind profile IS the pretreatment. No conversion coating. No phosphate. Just clean, profiled substrate and primer.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Cleaned substrate (steel or concrete)  -->  After: Profiled surface ready for primer application`

---

### ZONE 3 -- Dual Pretreatment Decision Hero

**Section label:** `STEEL vs. CONCRETE -- TWO DIFFERENT APPROACHES` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Dual Decision Tree (Y: 5.0" to 14.0")**

**Left -- Steel Path (X: 0.5", W: 11.0", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `STEEL` Barlow SemiBold 22 pt `#2EC4B6`

Decision tree (top to bottom):

Step 1: `ABRASIVE BLAST TO SPEC`
- `SP10 (general) or SP5 (immersion)` JetBrains Mono 12 pt `#F0EDE8`

Step 2: `VERIFY PROFILE`
- `2.0-4.0 mils per ASTM D4417` JetBrains Mono 12 pt

Step 3: Decision diamond: `ZINC-RICH PRIMER?`
- YES arrow (left): `NO conversion coating` Inter Medium 13 pt `#E8A020`
  - `Profile = pretreatment. Zinc must contact steel directly.`
- NO arrow (right): `Optional: iron phosphate or wash primer` Inter Regular 13 pt `#2EC4B6`
  - `Epoxy primer directly on profiled steel is acceptable for most applications`

Step 4: `APPLY PRIMER WITHIN BLAST-TO-COAT WINDOW`
- `4-8 hr (< 80% RH) or 1-2 hr (> 80% RH)` JetBrains Mono 12 pt `#E05C5C`

Big callout: `DO NOT ADD CONVERSION COATING UNDER ZINC-RICH PRIMER` Inter Medium 16 pt `#E05C5C`

**Right -- Concrete Path (X: 12.0", W: 11.5", H: 8.5"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `CONCRETE` Barlow SemiBold 22 pt `#E8A020`

Decision tree:

Step 1: `MECHANICAL PROFILE`
- `ICRI CSP 2-5 (shot blast, grind, or scarify)` JetBrains Mono 12 pt

Step 2: `VERIFY MOISTURE`
- `ASTM F2170: < 75% RH` JetBrains Mono 12 pt
- `ASTM F1869: < 3 lb/1,000 ft2/24 hr`

Step 3: `CHECK pH`
- `Surface pH 7-10 (pH paper or phenolphthalein)` JetBrains Mono 12 pt

Step 4: `VERIFY NO SEALERS OR CURING COMPOUNDS`
- `Water droplet test -- must absorb, not bead` Inter Regular 13 pt

Step 5: `APPLY EPOXY PRIMER OR PENETRATING SEALER`
- `No zinc-rich on concrete -- galvanic protection is not applicable`

Big callout: `NO CURING COMPOUNDS OR SEALERS ON THE SURFACE -- GRIND OFF IF PRESENT` Inter Medium 14 pt `#E05C5C`

---

### ZONE 4 -- Steel Pretreatment by Tier

**Section label:** `STEEL -- PRETREATMENT BY SERVICE TIER` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three-Tier Table**

Y: 15.3" to 20.3". Column widths (23.0" total):
- Service Tier (4.5") | Blast Spec (4.0") | Profile (3.0") | Primer (5.0") | Salt Limits (6.5")

| Service Tier | Blast Spec | Profile | Primer | Salt Limits |
|---|---|---|---|---|
| General industrial (atmospheric) | SSPC-SP6 or SP10 | 1.5-3.0 mils | Epoxy or organic zinc | Cl < 7 ug/cm2 (per SSPC Guide 15) |
| Marine / offshore | SSPC-SP10 or SP5 | 2.0-4.0 mils | IOZ (mandatory by most marine specs) | Cl < 3 ug/cm2, SO4 < 10 ug/cm2 |
| Immersion (tank lining) | SSPC-SP5 (White Metal) | 2.0-4.0 mils | Solventless epoxy | Cl < 3 ug/cm2, SO4 < 10 ug/cm2 |
| Maintenance / spot repair | SSPC-SP11 (Power Tool to Bare) | Feather edges | Epoxy or OZ | Test at repair area |

Data: JetBrains Mono 11 pt `#F0EDE8`.

Footnote: `Soluble salt testing per SSPC Guide 15 / ISO 8502 is mandatory for marine, offshore, and immersion service. Chloride contamination causes osmotic blistering under the coating.` Inter Medium 12 pt `#E8A020`.

---

### ZONE 5 -- Concrete Pretreatment Detail

**Section label:** `CONCRETE -- THE SUBSTRATE THAT FIGHTS BACK` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Two-Column Detail**

Y: 21.3" to 26.3".

**Left -- Profile and Surface Requirements (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020` 0.06"
- Title: `SURFACE REQUIREMENTS` Barlow SemiBold 18 pt `#E8A020`

| Requirement | Specification | Method |
|---|---|---|
| Surface profile | ICRI CSP 2-5 | Shot blast, grind, or scarify |
| Moisture (RH probe) | < 75% RH | ASTM F2170 |
| Moisture (calcium chloride) | < 3 lb/1,000 ft2/24 hr | ASTM F1869 |
| Surface pH | 7-10 | pH paper on wet surface |
| Curing compounds | NONE (grind off if present) | Water droplet absorption test |
| Laitance | Removed | Visible weak layer on surface |
| Contamination (oil/grease) | None | Alkaline clean or solvent wipe |

JetBrains Mono 11 pt `#F0EDE8`.

**Right -- Why Concrete Is Difficult (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06"
- Title: `CONCRETE CHALLENGES` Barlow SemiBold 18 pt `#E05C5C`

Bullet list (Inter Regular 13 pt `#F0EDE8`, line height 155%):
- `Porous -- absorbs coating unevenly (pin-dot pattern)`
- `Contains moisture -- even "dry" concrete transmits vapor`
- `Alkaline (pH 12-13 fresh) -- attacks acid-catalyzed coatings`
- `Weak surface layer (laitance) must be removed`
- `Curing compounds seal the surface and prevent adhesion`
- `No electrical connection for galvanic primers -- zinc-rich does not protect concrete`
- `Epoxy penetrating sealer is the standard concrete primer`

---

### ZONE 6 -- Pretreatment Failures

**Section label:** `WHAT GOES WRONG -- 4 PRETREATMENT FAILURES` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | ZINC-RICH PRIMER FAILS ON STEEL | Conversion coating under zinc-rich insulates zinc from steel | Blast to bare steel; apply zinc-rich directly; no intermediate layer |
| 2 | 6.33" | BLISTERING ON CONCRETE | Moisture vapor transmission through slab exceeds F1869 limit | Test MVER; install vapor barrier; dehumidify; do not coat until < 3 lb |
| 3 | 12.16" | COATING PEELING OFF CONCRETE | Curing compound or sealer on the surface preventing adhesion | Grind off curing compound; re-profile; verify absorption with water droplet test |
| 4 | 18.0" | OSMOTIC BLISTERING ON STEEL | Soluble salts (chloride, sulfate) trapped under coating | Test with Bresle patch; wash with fresh water; re-blast; verify < 3 ug/cm2 Cl |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `Protective coating pretreatment is the opposite of what most painters learn: no conversion coating, no phosphate, no chemical treatment on the surface. The blast profile on steel and the grind profile on concrete ARE the pretreatment. Adding anything between the metal and the zinc defeats the galvanic protection that is the entire point of the system.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Pretreatment -- Protective Coatings`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Pretreatment Protective Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The dual decision tree is the hero because the steel-vs-concrete divergence is the most important concept in this poster. Steel people coming from Cluster 7 (priming) understand "no conversion coating under zinc-rich." Concrete people need a completely different set of checks: moisture, pH, curing compounds, profile. The big red callout on each side hammers the one rule each audience must not violate. The service tier table in Zone 4 gives the specifier a quick lookup for how aggressive the surface prep needs to be based on the service environment.

---

*Alaina -- Poster #717 -- Construction Workup v1.0 -- 2026-04-26*
