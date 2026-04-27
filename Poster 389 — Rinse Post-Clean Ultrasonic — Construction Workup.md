---
Project: Plating Posters Inc
Poster Number: 389
Title: "Rinse -- Post-Clean (Ultrasonic)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- post-clean rinse stage, cascade rinse for precision, rinse quality
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - Rinse
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #389 -- Construction Workup
## Rinse -- Post-Clean (Ultrasonic)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

The rinse after ultrasonic cleaning removes the cleaning solution and any loosened contaminants from part surfaces. For general plating, a standard running water rinse suffices. For precision applications (electronics, optics, medical), an ultrasonic cascade rinse in DI water takes cleanliness to semiconductor-grade levels. This poster covers both paths.

Hero visual: a cascade rinse flow diagram showing the 4-tank precision configuration (ultrasonic clean -> ultrasonic tap water rinse -> ultrasonic DI rinse -> final DI rinse).

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cascade rinse flow diagram (Block B -- HERO):** Four-tank horizontal sequence with water flow arrows (counter to part direction). Built with rectangles and arrows.
2. **General vs. precision decision tree (Block D):** Two-path callout -- standard rinse vs. cascade ultrasonic rinse.
3. **Rinse quality targets (Block E):** Conductivity and cleanliness targets by application.
4. **Solvent exception callout (Block F):** No water rinse for solvent-based ultrasonic.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.0" / 28.0" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 4 highlighted (Teal) -- "Rinse"
ZONE 3 -- CASCADE RINSE HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- GENERAL VS. PRECISION DECISION (15.0"--21.0" / ~6.0")
ZONE 5 -- RINSE QUALITY TARGETS (21.0"--28.0" / ~7.0")
ZONE 6 -- SOLVENT EXCEPTION + TIPS (28.0"--32.5" / ~4.5")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `RINSE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Post-Clean -- Removing What Cavitation Loosened` -- 36 pt `#2EC4B6` (Teal). Y: 1.5".
**Tagline:** `Ultrasonic cleaning lifts the contamination. The rinse carries it away. Skip the rinse and you've moved the dirt, not removed it.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 4 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Parts with cleaning solution and loosened soil --> After: Clean surfaces ready for drying or next process`

---

### ZONE 3 -- Cascade Rinse Hero

**Section label:** `CASCADE ULTRASONIC RINSE -- PRECISION CONFIGURATION` -- Y: 4.4".
**Sublabel:** `For semiconductor, medical, optical, and electronic applications` -- Y: 4.9". Inter Regular 16 pt `#F0EDE8` at 60%.

**BLOCK B -- Four-Tank Cascade Diagram**

Y: 5.5" to 13.5". Four tanks in a horizontal row with arrows showing part flow (left to right) and water flow (right to left).

Each tank: Rounded rect, W: 5.0", H: 6.5", fill `#252B3D`, border 2 pt `#C8D0D8`, radius 6.

| Tank | X | Label | Contents | Accent |
|---|---|---|---|---|
| 1 | 0.5" | ULTRASONIC CLEAN | Cleaning solution | `#27AE60` |
| 2 | 6.25" | ULTRASONIC RINSE 1 | Tap water + ultrasonics | `#2EC4B6` |
| 3 | 12.0" | ULTRASONIC RINSE 2 | DI water + ultrasonics | `#2EC4B6` |
| 4 | 17.75" | FINAL RINSE | DI water (may be heated) | `#E8A020` |

**Part flow arrows (top, left to right):**
- Large arrows above tanks, stroke 4 pt `#27AE60`, arrowheads right
- Label: `PARTS MOVE THIS WAY -->` Barlow SemiBold 16 pt `#27AE60`

**Water flow arrows (bottom, right to left):**
- Large arrows below tanks, stroke 4 pt `#2EC4B6`, arrowheads left
- Label: `<-- FRESH WATER ENTERS HERE` Barlow SemiBold 16 pt `#2EC4B6`
- Overflow arrows from each tank to the one before it (right to left)

**Inside each tank:**
- Tank number: Barlow Condensed ExtraBold 20 pt, accent color
- Contents: Inter Regular 14 pt `#F0EDE8`
- Key spec: JetBrains Mono 13 pt `#F0EDE8` at 70%

Tank 1: `Cleaner at 30--60 g/L` / `Full ultrasonic power`
Tank 2: `Tap water` / `Ultrasonic assist` / `Removes bulk chemistry`
Tank 3: `DI water (< 5 mg/L TDS)` / `Ultrasonic assist` / `Removes ions`
Tank 4: `Fresh DI water` / `No ultrasonics (or gentle)` / `Final cleanliness`

**Result callout (Y: 13.8" to 14.8"):**
- Rounded rect, full width, H: 0.8", fill `#27AE60` at 12%, border 1 pt `#27AE60`
- Text: `Result: Particle counts and NVR levels suitable for semiconductor, medical, and optical applications (ASTM E1216 / ISO 16232 / IEST-STD-CC1246)` Inter Medium 14 pt `#27AE60`

---

### ZONE 4 -- General vs. Precision Decision

**Section label:** `WHICH RINSE DO YOU NEED?` -- Y: 15.2".

**BLOCK D -- Two-Path Comparison**

Y: 15.8" to 20.8". Two side-by-side callout boxes.

**Left -- General Plating Rinse (X: 0.5", W: 11.0"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent `#2EC4B6`
- Title: `STANDARD RINSE` Barlow SemiBold 20 pt `#2EC4B6`
- Subtitle: `For general metal finishing` Inter Regular 14 pt `#F0EDE8` at 60%
- Content:
  - `Running water rinse (city or softened)`
  - `Single or double immersion`
  - `Ambient temperature`
  - `30--60 seconds`
  - `Adequate for most plating pre-treatment`
- Bottom: `Target: < 200 microsiemens/cm conductivity` JetBrains Mono 14 pt `#2EC4B6`

**Right -- Precision Cascade Rinse (X: 12.0", W: 11.5"):**
- Same box style, left accent `#E8A020`
- Title: `CASCADE ULTRASONIC RINSE` Barlow SemiBold 20 pt `#E8A020`
- Subtitle: `For electronics, medical, optics, semiconductor` Inter Regular 14 pt `#F0EDE8` at 60%
- Content:
  - `3--4 stage ultrasonic cascade (see hero diagram)`
  - `DI water in final stages`
  - `Counter-current flow`
  - `Particle count verification required`
  - `No bare-hand contact after final rinse`
- Bottom: `Target: < 50 microsiemens/cm (electronics) to < 1 microsiemens/cm (semiconductor)` JetBrains Mono 13 pt `#E8A020`

---

### ZONE 5 -- Rinse Quality Targets

**Section label:** `RINSE QUALITY TARGETS BY APPLICATION` -- Y: 21.2".

**BLOCK E -- Target Table**

Y: 21.8" to 27.0". Column widths (23.0" total):
- Application (6.0") | Rinse Type (4.5") | Conductivity Target (5.0") | Verification (7.5")

Header row: fill `#3A4055`, H: 0.5".

| Application | Rinse Type | Conductivity | Verification |
|---|---|---|---|
| General zinc plating | Running water | < 200 microsiemens/cm | Visual water break |
| Decorative nickel/chrome | Running or softened | < 100 microsiemens/cm | Conductivity meter |
| Electronics (gold, tin) | DI cascade | < 50 microsiemens/cm | Conductivity + particle count |
| Medical devices | DI ultrasonic cascade | < 20 microsiemens/cm | Per device validation protocol |
| Semiconductor | 18 megohm-cm ultrapure | < 1 microsiemens/cm | Online particle counter + NVR |

Data: JetBrains Mono 12 pt. Application: Inter Medium 13 pt.

**Key insight (Y: 27.3"):**
- `Lower conductivity = cleaner rinse. A handheld conductivity meter is the cheapest quality tool in the shop.` Inter Medium 14 pt `#E8A020`

---

### ZONE 6 -- Solvent Exception + Tips

**Two-column layout (Y: 28.2" to 32.3"):**

**Left -- Solvent Exception (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `SOLVENT ULTRASONIC -- NO WATER RINSE` Barlow SemiBold 16 pt `#E05C5C`
- Body: `If ultrasonic cleaning used solvent (modified alcohol, HFE, IPA), do NOT follow with a water rinse. Solvent-cleaned parts are air-dried directly. Water would re-contaminate the solvent-clean surface.` Inter Regular 14 pt `#F0EDE8`

**Right -- Rinse Tips (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `PRACTICAL TIPS` Barlow SemiBold 16 pt `#27AE60`
- Bullet list:
  - `Agitate parts gently during rinse to release trapped solution`
  - `Hot DI rinse (final stage) assists faster drying`
  - `Replace rinse water when conductivity rises above target`
  - `Never delay between cleaning and rinsing -- drying = re-contamination`

---

### ZONE 7 -- Footer

Standard. Title: `Rinse -- Post-Clean (Ultrasonic)`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Rinse quality targets vary by application, specification, and customer requirements. Consult your process supplier and applicable standards for site-specific targets.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Rinse Post-Clean Ultrasonic -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The cascade rinse diagram is the hero -- it shows the most sophisticated rinse configuration in ultrasonic cleaning, and the counter-current water flow principle (parts go left-to-right, water goes right-to-left) is fundamental to rinse system design across ALL of metal finishing. The general vs. precision decision tree helps shops quickly determine which path they need. The conductivity target table is the most actionable reference on this poster.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #389 -- Construction Workup v1.0*
*2026-04-26*
