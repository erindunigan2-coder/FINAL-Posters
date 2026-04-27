---
Project: Plating Posters Inc
Poster Number: 720
Title: "Cure -- Protective Coatings"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster 8 technical reference (Protective Coatings -- Epoxy / Urethane) -- Watson Research Brief (Section 8.8)"
Process Scope: Cure for protective coatings -- Stage 7 of 8
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - ProtectiveCoatings
  - Cure
  - ConstructionWorkup
  - PaintingCoating
  - Cluster8
---

# Poster #720 -- Construction Workup
## Cure -- Protective Coatings

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Stage 7 of 8. Protective coatings cure by ambient chemical reaction, not heat. Epoxy cross-links through amine-epoxy reaction at room temperature. Urethane cross-links through isocyanate-polyol reaction. Full chemical cure takes 7-14 days for epoxy and 5-7 days for urethane -- but immersion service demands you wait the full cure before filling the tank. Temperature is the master variable: below 50 F, most amine-cured epoxies slow dramatically or stop. Above 90 F, pot life collapses. The pot-life rule of thumb -- halves every 18 F -- governs every decision on the job site.

Hero visual: cure parameter matrix showing four coating systems (amine epoxy, polyamide epoxy, aliphatic urethane, solventless tank lining) with ambient cure, force cure, and full chemical cure timelines, plus a temperature effects diagram.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Cure parameter matrix hero (Block B):** Four-row table showing cure conditions, timelines, and verification methods for each system.
2. **Temperature effects diagram (Block D):** Visual showing how temperature affects cure rate, pot life, and the 18 F rule.
3. **Immersion service cure requirements (Block E):** Special requirements for tank lining and immersion coatings.
4. **Defect strip (Block F):** 4 cure-related defects.

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
  Stage 7 highlighted (Emerald)
ZONE 3 -- CURE PARAMETER MATRIX HERO (4.2"--14.5" / ~10.3")
ZONE 4 -- TEMPERATURE EFFECTS (14.5"--20.5" / ~6.0")
ZONE 5 -- IMMERSION SERVICE CURE (20.5"--26.5" / ~6.0")
ZONE 6 -- CURE DEFECTS (26.5"--32.5" / ~6.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `CURE` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Protective Coatings -- Stage 7 of 8` -- 32 pt `#27AE60` (Emerald). Y: 1.4".
**Tagline:** `No oven. No UV lamp. Ambient chemical reaction -- 7 to 14 days to full cure. Temperature is the throttle: below 50 F it stalls, above 90 F it runs away. The 18 F rule governs everything.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Stage 7 highlighted: fill `#27AE60`, text `#1A1F2E`. Others dimmed.
Below: `Before: Applied multi-coat system curing on substrate  -->  After: Fully cured, chemically resistant, ready for service or inspection`

---

### ZONE 3 -- Cure Parameter Matrix Hero

**Section label:** `CURE PARAMETERS -- FOUR COATING SYSTEMS` -- Y: 4.4". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK B -- Matrix Table (Y: 5.0" to 14.0")**

Full-width rounded rect, W: 23.0", H: 8.5", fill `#1E2435`, top accent 4 pt `#27AE60`.

Column widths (23.0" total):
- System (4.5") | Ambient Cure Temp (3.5") | Force Cure (3.5") | Full Chemical Cure (3.5") | Cure Verification (4.0") | Key Note (4.0")

| System | Ambient Cure | Force Cure | Full Cure | Verification | Key Note |
|---|---|---|---|---|---|
| Amine-cured epoxy | 50-100 F, > 40% RH | 140-180 F, 1-4 hr | 7-14 days ambient | MEK rub 50+ | Below 50 F: extremely slow; use cycloaliphatic amine for low-temp |
| Polyamide-cured epoxy | 50-100 F, > 40% RH | 140-180 F, 1-4 hr | 7-14 days ambient | MEK rub 50+ | More flexible than amine; lower chemical resistance |
| Aliphatic urethane | 50-100 F | 140-160 F, 1-2 hr | 5-7 days ambient | Hardness per spec | Moisture sensitivity during cure; avoid dew |
| Solventless epoxy (tank lining) | 60-100 F | 150-200 F, 2-4 hr | 7-14 days ambient; immersion: wait FULL cure | MEK rub 100+; Shore D > 75 | MUST achieve full cure before filling tank with chemical |

Header: Barlow SemiBold 13 pt `#F0EDE8`.
Data: JetBrains Mono 11 pt `#F0EDE8`.
System names: Inter Medium 13 pt, color-coded:
- Amine: `#2EC4B6`
- Polyamide: `#E8A020`
- Urethane: `#27AE60`
- Solventless: `#E05C5C`

**Big Rule Callout (Y: 12.5"):**
- Full-width rounded rect, fill `#252B3D`, border `#E8A020`
- Big stat: `18 F` Barlow Condensed ExtraBold 64 pt `#E8A020`
- Rule text: `POT LIFE HALVES FOR EVERY 18 F (10 C) INCREASE IN TEMPERATURE` Barlow SemiBold 18 pt `#F0EDE8`
- Example: `4-hour pot life at 77 F -> 2 hours at 95 F -> 1 hour at 113 F` JetBrains Mono 14 pt `#E8A020`

---

### ZONE 4 -- Temperature Effects

**Section label:** `TEMPERATURE -- THE MASTER VARIABLE` -- Y: 14.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK D -- Three Temperature Zones (Y: 15.3" to 20.3")**

Three cards. Each: Rounded rect, W: 7.33", H: 4.5", fill `#1E2435`, top accent 4 pt.

**Card 1 -- Cold (< 50 F) (X: 0.5", accent `#2EC4B6`):**
- Title: `BELOW 50 F (10 C)` Barlow SemiBold 18 pt `#2EC4B6`
- Badge: `CAUTION` fill `#E8A020`
- Body (Inter Regular 13 pt `#F0EDE8`):
  - `Most amine-cured epoxies cure extremely slowly or not at all`
  - `Amine blush risk dramatically increases`
  - `Urethane cure slows significantly`
  - `FIX: Use cycloaliphatic amine hardeners designed for low-temp cure (down to 35 F / 2 C)`
  - `FIX: Force cure with heated enclosure (tenting + heaters)`

**Card 2 -- Ideal (50-90 F) (X: 8.16", accent `#27AE60`):**
- Title: `50-90 F (10-32 C)` Barlow SemiBold 18 pt `#27AE60`
- Badge: `OPTIMAL` fill `#27AE60`
- Body:
  - `Standard cure range for all systems`
  - `Pot life and cure rate are in normal range`
  - `Monitor for overnight temperature drops (amine blush)`
  - `Standard ambient cure: 7-14 days to full properties`
  - `Production sweet spot: 65-80 F`

**Card 3 -- Hot (> 90 F) (X: 15.83", accent `#E05C5C`):**
- Title: `ABOVE 90 F (32 C)` Barlow SemiBold 18 pt `#E05C5C`
- Badge: `DANGER` fill `#E05C5C`
- Body:
  - `Pot life collapses (18 F rule)`
  - `Material may gel before application is complete`
  - `FIX: Reduce batch sizes dramatically`
  - `FIX: Keep materials in shade; do not store in sun`
  - `FIX: Apply during cooler parts of the day`
  - `FIX: Use extended-pot-life hardener grades`

---

### ZONE 5 -- Immersion Service Cure

**Section label:** `IMMERSION SERVICE -- THE FULL-CURE REQUIREMENT` -- Y: 20.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`.

**BLOCK E -- Full-Width Panel**

Y: 21.3" to 26.3". Rounded rect, fill `#1E2435`, left accent `#E05C5C` 0.06".

**Two-column layout:**

**Left -- Why Full Cure Matters (X: 1.0", W: 11.0"):**
- Title: `TANK LINING AND IMMERSION COATINGS` Barlow SemiBold 18 pt `#E05C5C`
- Body (Inter Regular 13 pt `#F0EDE8`, line height 155%):
  - `Tank linings and immersion coatings require FULL CHEMICAL CURE before contact with the stored chemical`
  - `Minimum: 7 days ambient cure at 77 F (amine-cured epoxy)`
  - `Accelerated: force cure at 150-200 F for 2-4 hours`
  - `For immersion in strong chemicals or solvents: 14 days ambient or force cure per TDS`
  - `Potable water tanks: must meet NSF/ANSI 61 (Drinking Water System Components)`
  - `Filling before full cure causes softening, blistering, and coating failure within weeks`

**Right -- Cure Verification for Immersion (X: 12.5", W: 10.5"):**
- Title: `VERIFICATION BEFORE FILLING` Barlow SemiBold 18 pt `#27AE60`

| Test | Standard | Requirement |
|---|---|---|
| Solvent rub (MEK or MIBK) | ASTM D4752 | 100+ double rubs, no softening |
| Shore D hardness | ASTM D2240 | > 75D (most tank lining epoxies) |
| Holiday detection (wet sponge) | ASTM D5162 | Zero holidays at 67.5 V DC (< 20 mil) |
| Holiday detection (spark test) | NACE SP0188 / ASTM D4787 | Zero holidays at 100 V/mil (> 20 mil) |
| DFT verification | SSPC-PA 2 / ASTM D7091 | Per spec (+/- 20% from target) |

JetBrains Mono 11 pt `#F0EDE8`.

Warning: `DO NOT fill the tank based on elapsed time alone. VERIFY cure by solvent rub, hardness, AND holiday detection before introducing any chemical. Filling an undercured tank lining is a five- to six-figure rework event.` Inter Medium 13 pt `#E05C5C`.

---

### ZONE 6 -- Cure Defects

**Section label:** `WHAT GOES WRONG -- 4 CURE DEFECTS` -- Y: 26.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`.

**BLOCK F -- Four Problem Cards (Y: 27.3" to 30.3")**

Each card: Rounded rect, W: 5.5", H: 2.7", fill `#1E2435`, radius 6, left accent 0.06" `#E05C5C`.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | INCOMPLETE CURE (SOFT FILM) | Temperature too low; or wrong mix ratio (off-ratio) | Verify mix ratio; increase temperature (tent + heat); use low-temp hardener |
| 2 | 6.33" | AMINE BLUSH ON SURFACE | Cool/humid conditions during cure; dew formation overnight | Wash with water + scrub; solvent wipe; sand if needed; prevent with 5 F dew point rule |
| 3 | 12.16" | POT LIFE EXPIRED (GELLED MATERIAL) | Material applied past pot life; high temperature shortened pot life | Discard gelled material; reduce batch size; track time from mixing |
| 4 | 18.0" | TANK LINING FAILURE (BLISTERING) | Filled tank before full cure; or moisture in substrate | Verify cure (MEK 100+, Shore D 75+) before filling; verify moisture < F1869 limit |

**Key insight callout (Y: 30.6" to 32.3"):**
- Text: `Protective coatings cure by chemical reaction, not by drying. Solvent evaporation is not cure. A film that is "dry to touch" may be only 20-30% of the way to full chemical cure. The only reliable cure verification is the solvent rub test. If you cannot verify it with MEK, you do not know if it is cured.` -- Inter Medium, 14 pt, `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Cure -- Protective Coatings`. Version `v1.0 -- 2026`.

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Cure Protective Coatings -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The 18 F rule big-stat callout is the most important single number on this poster. It governs pot life, cure rate, and every practical decision on a protective coating job site. The three temperature cards make the consequences tangible: cold = stall, ideal = normal, hot = runaway. The immersion service section gets a full zone because the stakes are highest there -- filling an undercured tank lining is a catastrophic, expensive failure. The "dry to touch is not cured" callout in the key insight is the conceptual foundation that separates protective coating professionals from general painters.

---

*Alaina -- Poster #720 -- Construction Workup v1.0 -- 2026-04-26*
