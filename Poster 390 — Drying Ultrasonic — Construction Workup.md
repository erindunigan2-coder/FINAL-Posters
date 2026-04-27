---
Project: Plating Posters Inc
Poster Number: 390
Title: "Drying -- Ultrasonic Cleaning"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Cluster CT-7 technical reference (ultrasonic cleaning)"
  - "Chemical Treatment Clusters — Watson Research Brief"
Process Scope: Ultrasonic cleaning -- drying methods, water spot prevention, and transition to next process
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - UltrasonicCleaning
  - Drying
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT07
---

# Poster #390 -- Construction Workup
## Drying -- Ultrasonic Cleaning

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Drying is the step most people think is trivial -- until water spots ruin the finish, trapped moisture causes adhesion failures, or parts sit in a queue and oxidize. This poster covers drying methods (forced air, oven, vacuum, hot DI assist), water spot prevention, and the transition window to the next process step.

Hero visual: a comparison of drying methods showing forced air, oven, and vacuum configurations with their temperature/time ranges and best applications.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Drying methods comparison (Block B -- HERO):** Three drying methods side by side with parameters and application guidance.
2. **Water spot prevention panel (Block D):** Root causes and solutions for water spots.
3. **Transition timing callout (Block E):** How long parts can sit after drying before re-contamination risk increases.
4. **Solvent drying exception (Block F):** Air-dry only for solvent-cleaned parts.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts per series design system.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 15.0" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE ORIENTATION STRIP (2.9"--4.2")
  Stage 5 highlighted (Amber) -- "Dry"
ZONE 3 -- DRYING METHODS HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- WATER SPOT PREVENTION (15.0"--22.0" / ~7.0")
ZONE 5 -- TRANSITION TIMING + HANDLING (22.0"--28.5" / ~6.5")
ZONE 6 -- SPECIAL CASES (28.5"--32.5" / ~4.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `DRYING` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Ultrasonic Cleaning -- The Step Between Clean and Ready` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `A perfectly cleaned part with water spots is a rejected part. Drying is not an afterthought -- it is the final quality gate before the next process.` -- 22 pt `#F0EDE8` at 65%. Y: 2.2".

---

### ZONE 2 -- Orientation Strip

Stage 5 highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.
Below: `Before: Wet, rinsed parts --> After: Dry, spot-free surfaces ready for next process step`

---

### ZONE 3 -- Drying Methods Hero

**Section label:** `DRYING METHODS -- CHOOSE BY APPLICATION` -- Y: 4.4".

**BLOCK B -- Three Method Comparison**

Y: 5.0" to 14.8". Three large callout boxes side by side.

| Method | X | W | Accent |
|---|---|---|---|
| Forced Air | 0.5" | 7.33" | `#2EC4B6` |
| Oven / Recirculating Hot Air | 8.0" | 7.33" | `#E8A020` |
| Vacuum Drying | 15.5" | 8.0" | `#27AE60` |

Each box: Rounded rect, H: 9.5", fill `#1E2435`, left accent 0.06", radius 6.

*Forced Air box:*
- Title: `FORCED AIR` Barlow Condensed ExtraBold 24 pt `#2EC4B6`
- Parameters:
  - `Ambient to warm (filtered, oil-free)`
  - `Air knife or blow-off nozzle`
  - `30 sec -- 5 min depending on geometry`
- Best for: `General parts, simple geometry, high throughput`
- Limitations: `Blind holes may retain moisture; not suitable for precision`
- Cost: `LOW` JetBrains Mono 14 pt `#27AE60`
- Key rule: `Air must be clean and dry -- compressed shop air often contains oil` Inter Medium 13 pt `#E05C5C`

*Oven box:*
- Title: `OVEN DRY` Barlow Condensed ExtraBold 24 pt `#E8A020`
- Parameters:
  - `150--250 F (65--120 C)`
  - `Recirculating hot air`
  - `5--20 min depending on mass`
- Best for: `Thorough drying, complex geometry, batch processing`
- Limitations: `Heat-sensitive substrates or coatings may not tolerate`
- Cost: `MODERATE` JetBrains Mono 14 pt `#E8A020`
- Key rule: `Do not exceed temperature limits for substrate or any applied coating` Inter Medium 13 pt `#E05C5C`

*Vacuum Drying box:*
- Title: `VACUUM DRY` Barlow Condensed ExtraBold 24 pt `#27AE60`
- Parameters:
  - `Low pressure reduces boiling point of water`
  - `Moisture evaporates at lower temperature`
  - `2--10 min typical`
- Best for: `Precision, heat-sensitive parts, blind holes, complex internal geometry`
- Limitations: `Higher equipment cost; batch process`
- Cost: `HIGH` JetBrains Mono 14 pt `#E05C5C`
- Key rule: `Best method for parts with features that trap water` Inter Medium 13 pt `#27AE60`

---

### ZONE 4 -- Water Spot Prevention

**Section label:** `WATER SPOTS -- CAUSES AND PREVENTION` -- Y: 15.2".

**BLOCK D -- Water Spot Root Causes**

Y: 15.8" to 21.8". Table format.

Column widths (23.0" total):
- Cause (5.0") | Mechanism (8.0") | Prevention (10.0")

| Cause | Mechanism | Prevention |
|---|---|---|
| Hard water | Ca/Mg salts deposit as water evaporates | Use DI or softened water for final rinse |
| Contaminated rinse | Dissolved chemicals in rinse leave residue | Monitor conductivity; replace rinse when target exceeded |
| Slow drying | Extended evaporation allows residue concentration | Prompt transfer to drying; use hot DI final rinse |
| Dirty compressed air | Oil/moisture in air re-contaminates surface | Use dedicated filtered, oil-free air supply |
| Part geometry | Water pools in recesses, dries last with concentrated residue | Orient parts for drainage; vacuum dry complex parts |

Data: Inter Regular 13 pt. Cause names: Barlow SemiBold 14 pt.

**Key insight (Y: 21.3"):**
- `Hot DI rinse as the final step before drying dramatically reduces water spots -- the heat assists evaporation and the DI water leaves zero mineral residue.` Inter Medium 14 pt `#27AE60`

---

### ZONE 5 -- Transition Timing + Handling

**Section label:** `TIME IS THE ENEMY -- TRANSITION RULES` -- Y: 22.2".

**BLOCK E -- Timing Guidance**

Y: 22.8" to 28.3". Two-column layout.

**Left -- Timing Rules (X: 0.5", W: 11.0"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#E05C5C`
- Title: `PROCESS WITHOUT DELAY` Barlow SemiBold 18 pt `#E05C5C`
- Rules:
  - `Rinse to dry: IMMEDIATELY -- never air-dry with solution on parts`
  - `Dry to next process: as soon as possible`
  - `Maximum hold time (dry parts): depends on substrate and environment`
  - `Steel in humid shop: oxidation visible within 30--60 minutes`
  - `Aluminum: less sensitive but still process same shift`
  - `Precision/electronic: process within minutes of drying`

**Right -- Handling Rules (X: 12.0", W: 11.5"):**
- Rounded rect, H: 5.3", fill `#1E2435`, left accent `#2EC4B6`
- Title: `HANDLING AFTER DRYING` Barlow SemiBold 18 pt `#2EC4B6`
- Rules:
  - `Clean gloves ONLY -- fingerprints are contamination`
  - `Handle by edges or fixtures, not plating surfaces`
  - `Store in clean, covered containers if hold time > 30 min`
  - `Never blow on parts (breath moisture + oils)`
  - `Re-clean if parts are dropped or contacted`

---

### ZONE 6 -- Special Cases

**Two-column layout (Y: 28.7" to 32.3"):**

**Left -- Solvent Drying (X: 0.5", W: 11.0"):**
- Rounded rect, fill `#1E2435`, left accent `#E8A020`
- Title: `SOLVENT-CLEANED PARTS` Barlow SemiBold 16 pt `#E8A020`
- Body: `Parts cleaned in solvent ultrasonic (modified alcohol, HFE, IPA) are air-dried directly. No water rinse, no oven. The solvent evaporates cleanly. Ensure adequate ventilation during evaporation.`

**Right -- Hot DI Assist (X: 12.0", W: 11.5"):**
- Rounded rect, fill `#1E2435`, left accent `#27AE60`
- Title: `HOT DI RINSE ASSIST` Barlow SemiBold 16 pt `#27AE60`
- Body: `Heating the final DI rinse to 140--160 F serves double duty: it improves rinse efficiency AND accelerates drying. Parts come out of the rinse already hot -- evaporation begins immediately. This is the single best upgrade for drying quality in most shops.`

---

### ZONE 7 -- Footer

Standard. Title: `Drying -- Ultrasonic Cleaning`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Drying temperatures and times vary by substrate, geometry, and application. Consult your process specification for drying requirements.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Drying Ultrasonic -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

Drying is often the forgotten step, but it is where water spots, oxidation, and handling contamination ruin otherwise perfect work. The hot DI rinse assist tip is the highest-value practical takeaway. The transition timing guidance (Zone 5) is what shops need most -- "how long can cleaned parts sit?" The answer depends on substrate and environment, and this poster gives them the framework to make that judgment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #390 -- Construction Workup v1.0*
*2026-04-26*
