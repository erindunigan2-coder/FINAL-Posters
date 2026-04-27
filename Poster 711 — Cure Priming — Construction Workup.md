---
Project: Plating Posters Inc
Poster Number: 711
Title: "Cure -- Priming"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 7 technical reference (Industrial Priming Systems) -- Watson Research Brief"
Technical Source: Cure mechanisms and parameters for zinc-rich (IOZ and OZ), epoxy, and aerospace primers. IOZ cures by hydrolysis + condensation of ethyl silicate requiring atmospheric moisture. OZ and epoxy cure by binder chemistry (amine cross-linking, moisture-cure PU). Critical topcoating rules -- mist coat over IOZ, recoat windows, and the 30-day maximum.
Process Scope: Cure for industrial priming -- Stage 7 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - IndustrialPriming
  - Cure
  - ConstructionWorkup
  - PaintingCoating
  - Cluster7
---

# Poster #711 -- Construction Workup
## Cure -- Priming

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 8. This poster explains how each primer type develops its final properties. The hero is a cure mechanism comparison showing three fundamentally different chemistries side by side. The critical practical content: topcoating over zinc-rich primer requires a mist coat, and the recoat window for IOZ is 24 hours minimum to 30 days maximum. After 30 days, white zinc corrosion products form and the surface must be sweep-blasted before topcoating.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three cure mechanism panels (Block B):** IOZ hydrolysis, epoxy amine cross-linking, moisture-cure PU -- each with a simplified reaction description. Built with rounded rectangles and text.
2. **Cure parameters table (Block D):** Full comparison of all primer types with times and conditions.
3. **Topcoating over IOZ callout (Block E):** Mist coat requirement, recoat window, and the 30-day rule.
4. **Temperature effects panel (Block F):** How temperature affects cure speed and what to do about it.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 21.5" / 27.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 7 highlighted (Emerald)
ZONE 3 -- CURE MECHANISM HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- CURE PARAMETERS TABLE (15.0"--21.5" / ~6.5")
ZONE 5 -- TOPCOATING OVER IOZ (21.5"--27.5" / ~6.0")
ZONE 6 -- TEMPERATURE EFFECTS + CURE VERIFICATION (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Industrial Priming -- Stage 7 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `IOZ needs moisture to cure. Epoxy needs time. Patience here saves you from stripping the topcoat later.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Flash-off complete, film setting  -->  After: Fully cured primer, ready for inspection and topcoat`

---

### ZONE 3 -- Cure Mechanism Hero

**Section label:** `THREE CURE CHEMISTRIES -- THREE DIFFERENT RULES` -- Y: 4.4".

**BLOCK B -- Three Mechanism Panels (Y: 5.0" to 14.5")**

Three tall panels:

**Panel 1 -- IOZ Hydrolysis (X: 0.5", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `IOZ -- HYDROLYSIS` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `Moisture-Driven Cure` Inter Regular 14 pt `#F0EDE8` at 50%

Mechanism description (Inter Regular 14 pt `#F0EDE8`, line height 165%):
- `Step 1: Ethyl silicate binder reacts with atmospheric moisture (H2O)`
- `Step 2: Hydrolysis breaks Si-OEt bonds, releasing ethanol`
- `Step 3: Silanol groups (Si-OH) condense to form Si-O-Si network`
- `Step 4: Inorganic silicate matrix binds zinc particles together`
- `Result: Ceramic-like film with zinc particles in galvanic contact with steel`

Key requirements:
- `RH > 40% required for cure` JetBrains Mono 13 pt `#27AE60`
- `Full cure: 24--72 hours` JetBrains Mono 13 pt `#27AE60`
- `In dry air (< 30% RH): mist with water` JetBrains Mono 13 pt `#E8A020`

Bottom badge: `UNIQUE: Needs moisture, not heat` Barlow SemiBold 13 pt `#27AE60` on `#27AE60` at 15% fill

**Panel 2 -- Epoxy Cross-Linking (X: 8.33", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#2EC4B6`
- Title: `EPOXY -- CROSS-LINKING` Barlow SemiBold 22 pt `#2EC4B6`
- Subtitle: `Amine or Polyamide Cure` Inter Regular 14 pt `#F0EDE8` at 50%

Mechanism:
- `Step 1: Mix Component A (epoxy resin) + Component B (amine hardener)`
- `Step 2: Amine N-H reacts with epoxide ring (ring-opening addition)`
- `Step 3: Cross-links form 3D thermoset network`
- `Step 4: Film hardens irreversibly -- cannot be remelted`
- `Result: Dense, chemically resistant barrier film`

Key parameters:
- `Ambient cure: 50--100 deg F, > 40% RH` JetBrains Mono 13 pt `#2EC4B6`
- `Force cure: 140--180 deg F, 1--4 hours` JetBrains Mono 13 pt `#2EC4B6`
- `Full cure: 7--14 days ambient` JetBrains Mono 13 pt `#2EC4B6`

Bottom badge: `Time + temperature dependent` Barlow SemiBold 13 pt `#2EC4B6` on `#2EC4B6` at 15% fill

**Panel 3 -- Moisture-Cure PU (X: 16.17", W: 7.33", H: 9.0"):**
- Rounded rect, fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `MOISTURE-CURE PU` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `Single-Component Convenience` Inter Regular 14 pt `#F0EDE8` at 50%

Mechanism:
- `Step 1: Isocyanate groups (-NCO) react with atmospheric moisture`
- `Step 2: Carbamic acid intermediate forms, then decomposes to amine + CO2`
- `Step 3: Amine reacts with additional isocyanate to form urea linkages`
- `Step 4: Film cross-links into polyurethane/polyurea network`
- `Result: Tough, flexible film with good chemical resistance`

Key parameters:
- `RH > 30% required` JetBrains Mono 13 pt `#E8A020`
- `Full cure: 24--72 hours` JetBrains Mono 13 pt `#E8A020`
- `Single component -- no mixing errors` JetBrains Mono 13 pt `#27AE60`

Bottom badge: `One component, moisture does the work` Barlow SemiBold 13 pt `#E8A020` on `#E8A020` at 15% fill

---

### ZONE 4 -- Cure Parameters Table

**Section label:** `CURE PARAMETERS -- ALL PRIMER TYPES` -- Y: 15.2".

**BLOCK D -- Table (Y: 15.8" to 21.3")**

| Primer Type | Cure Mechanism | Conditions | Full Cure Time | Recoat Window |
|---|---|---|---|---|
| IOZ (ethyl silicate) | Hydrolysis + condensation | Ambient, 40--80% RH | 24--72 hr | 24 hr--30 days |
| IOZ (alkali silicate) | Water evaporation + silicate hardening | Ambient | 24--48 hr | 24 hr--30 days |
| OZ (2K epoxy-zinc) | Amine-epoxy cross-linking | Ambient to 120 deg F | 7--14 days | 4--24 hr (recoat); 3--7 days max |
| OZ (moisture-cure PU) | Isocyanate + moisture | Ambient, > 30% RH | 24--72 hr | Per TDS |
| Epoxy primer (2K) | Amine cross-linking | Ambient to 120 deg F | 7--14 days | 4--24 hr (recoat); 3--7 days max |
| Chromated epoxy (aero) | Amine cross-linking | 77 deg F air dry or 250 deg F force | 7 days air dry; 1 hr force cure | Per spec |

Header: `#3A4055`. Alternating rows `#1E2435` / `#252B3D`. Data: JetBrains Mono 12 pt.

---

### ZONE 5 -- Topcoating Over IOZ

**Section label:** `TOPCOATING OVER ZINC-RICH PRIMER -- THE RULES` -- Y: 21.7".

**BLOCK E -- Full-Width Panel (Y: 22.3" to 27.3")**

Three-part layout:

**Left -- Mist Coat Requirement (X: 0.5", W: 7.5"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `THE MIST COAT` Barlow SemiBold 20 pt `#E8A020`

Content (Inter Regular 14 pt `#F0EDE8`, line height 165%):
- `IOZ primer is POROUS -- the film is 75--85% zinc particles with air voids`
- `If a full-thickness topcoat is applied directly, solvent penetrates the porous IOZ`
- `Trapped solvent escapes during cure = bubbling and pinholing in the topcoat`
- `SOLUTION: Apply a thin "mist coat" (0.5--1.0 mil) of the intermediate (epoxy)`
- `The mist coat seals the porous IOZ surface`
- `After mist coat flash (1--4 hours), apply full intermediate coat`

Warning: `Skip the mist coat and the topcoat bubbles. Every time.` Inter Medium 14 pt `#E05C5C`

**Center -- The 30-Day Rule (X: 8.5", W: 7.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E05C5C`
- Title: `THE 30-DAY WINDOW` Barlow SemiBold 20 pt `#E05C5C`

Big stat: `30` Barlow Condensed ExtraBold 72 pt `#E05C5C`
Subtitle: `days maximum before topcoating IOZ` Barlow SemiBold 16 pt `#F0EDE8`

Content:
- `Wait minimum 24 hours (IOZ must be fully cured)`
- `If > 30 days elapse, white zinc corrosion products form on the surface`
- `These products = weak boundary layer = adhesion failure of topcoat`
- `Fix: Sweep blast (SSPC-SP7) to remove white zinc salts`
- `Then topcoat immediately`
- Inter Regular 13 pt `#F0EDE8`

**Right -- OZ Exception (X: 16.0", W: 7.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `OZ -- EASIER` Barlow SemiBold 20 pt `#27AE60`

Content:
- `Organic zinc primers are NOT porous like IOZ`
- `No mist coat required`
- `Standard recoat per binder TDS`
- `Recoat window same as the base binder (epoxy, PU)`
- `If max recoat exceeded: scuff sand and recoat`
- Inter Regular 13 pt `#F0EDE8`

Bottom: `OZ is more forgiving for multi-coat systems -- one of its key advantages over IOZ` Inter Medium 13 pt `#27AE60`

---

### ZONE 6 -- Temperature Effects + Cure Verification

**Two-column layout (Y: 27.7" to 32.3"):**

**Left -- Temperature Effects (X: 0.5", W: 11.0"):**

Section label: `TEMPERATURE AND CURE SPEED` Barlow Condensed ExtraBold 22 pt `#E8A020`.

| Temperature | IOZ Effect | Epoxy Effect |
|---|---|---|
| < 40 deg F (4 deg C) | Cure slows dramatically | Most epoxies STOP curing |
| 40--60 deg F (4--16 deg C) | Slow but functional | Slow; use cycloaliphatic amine hardener |
| 60--80 deg F (16--27 deg C) | Optimal cure range | Standard cure |
| 80--100 deg F (27--38 deg C) | Fast cure | Fast cure; pot life shortened |
| > 100 deg F (38 deg C) | Very fast; watch for dry spray | Pot life very short; reduce batch size |

Data: JetBrains Mono 12 pt. Temperature column: Inter Medium 13 pt.

Rule: `Pot life halves for every 18 deg F (10 deg C) increase in temperature.` Inter Medium 13 pt `#E05C5C`.

**Right -- Cure Verification (X: 12.0", W: 11.5"):**

Section label: `HOW TO VERIFY CURE` Barlow Condensed ExtraBold 22 pt `#27AE60`.

| Test | Method | Pass Criterion |
|---|---|---|
| IOZ thumb test | Press thumb firmly into IOZ surface | No zinc transfer to thumb = cured |
| Epoxy MEK rub | ASTM D4752, 50 double rubs | No softening, no color transfer |
| Epoxy Shore D | ASTM D2240 | > 70 Shore D (typical epoxy primer) |
| Pencil hardness | ASTM D3363 | Per specification (typically F to 2H) |

Data: JetBrains Mono 12 pt. Test names: Inter Medium 13 pt `#27AE60`.

Note: `The thumb test for IOZ is crude but effective field verification. If zinc dust transfers to your thumb, the primer is not cured -- do not topcoat.` Inter Regular 12 pt `#F0EDE8` at 60%.

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Priming`. Version `v1.0 -- 2026`.
Disclaimer note: `Source: General industry knowledge; SSPC-PS 12.01; ASTM D4752; Watson Research Brief.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Priming -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster is the chemistry deep-dive of the cluster. Three fundamentally different cure mechanisms -- hydrolysis, amine cross-linking, and moisture-cure PU -- all happen at ambient temperature but by completely different chemical pathways. The topcoating section is the most practically critical content: the mist coat requirement, the 30-day window, and the sweep-blast remedy for aged IOZ. The temperature table and cure verification methods close the loop -- the coating foreman needs to know when the primer is ready and what to do when conditions are not ideal.

---

*Alaina -- Poster #711 -- Construction Workup v1.0 -- 2026-04-26*
