---
Project: Plating Posters Inc
Poster Number: 366
Title: "Bath Preparation & Control -- Acid Pickling (Stainless Steel)"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Chemical Treatment Clusters -- Watson Research Brief (CT-4.3)"
Technical Source: Industry-standard bath makeup and analytical control for HNO3/HF stainless steel pickle baths. Includes HNO3-only and citric acid alternatives, titration methods, dissolved metal monitoring, and dump criteria.
Process Scope: Bath preparation, composition, analytical control, and dump criteria for stainless steel pickling
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - AcidPickling
  - StainlessSteel
  - BathPreparation
  - ConstructionWorkup
  - ChemicalTreatment
  - ClusterCT04
---

# Poster #366 -- Construction Workup
## Bath Preparation & Control -- Acid Pickling (Stainless Steel)

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Poster 3 of 7 in the CT-04 cluster. This is the chemistry poster for the stainless pickle. The hero visual is a three-bath comparison showing HNO3/HF (standard), HNO3-only (light scale), and citric acid (passivation/light pickle). The makeup procedure is critical safety content -- adding HF to water requires absolute discipline. The analytical control section introduces dual-acid titration (separate HNO3 and HF analysis) and dissolved metal monitoring by solution color. Bath life is shorter than carbon steel pickle due to chromium and nickel dissolution.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag
1. **Three-bath composition comparison (Block B -- HERO):** HNO3/HF, HNO3-only, and citric acid side by side.
2. **Makeup procedure (Block D):** Numbered step-by-step with HF safety callouts.
3. **Analytical control panel (Block E):** Dual-acid titration and dissolved metal monitoring.
4. **Bath life / dump criteria table (Block F):** Four-parameter action-level table.

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
  Poster 3 of 7 highlighted (Teal)
ZONE 3 -- THREE-BATH COMPOSITION / HERO (4.2"--15.0" / ~10.8")
ZONE 4 -- MAKEUP PROCEDURE (15.0"--21.5" / ~6.5")
ZONE 5 -- ANALYTICAL CONTROL (21.5"--27.5" / ~6.0")
ZONE 6 -- BATH LIFE & DUMP CRITERIA (27.5"--32.5" / ~5.0")
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `BATH PREPARATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Stainless Steel Pickling -- Three Chemistries, Three Risk Levels` -- 32 pt `#2EC4B6` (Teal). Y: 1.4".
**Tagline:** `The standard mixed-acid pickle is the workhorse. The citric alternative is the future. Know all three and match to your scale type.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Orientation Strip

Poster 3 highlighted: fill `#2EC4B6`, text `#1A1F2E`. Others dimmed.
Below: `Before: Empty pickle tank --> After: Charged, titrated, and temperature-verified pickle bath ready for production`

---

### ZONE 3 -- Three-Bath Composition (HERO)

**Section label:** `THREE PICKLE CHEMISTRIES -- COMPOSITION AND FUNCTION` -- Y: 4.4".

**BLOCK B -- Three Side-by-Side Bath Cards (Y: 5.0" to 14.5")**

**Left -- HNO3 + HF Standard (X: 0.5", W: 7.3"):**

Rounded rect H: 9.0", fill `#1E2435`, left accent 0.06" `#E05C5C`.

Title: `HNO3 + HF (MIXED ACID)` Barlow SemiBold 18 pt `#E05C5C`
Subtitle: `Standard Stainless Pickle` Inter Regular 14 pt `#F0EDE8` at 60%

| Component | Concentration | Function |
|---|---|---|
| Nitric acid (HNO3) | 10-25% v/v (70-175 g/L) | Oxidizer; dissolves Cr-depleted layer; passivates |
| Hydrofluoric acid (HF) | 1-8% v/v (5-40 g/L) | Dissolves siliceous/refractory scale |
| Water | Balance | Always add acid to water |

- JetBrains Mono 13 pt for concentrations
- Temperature: `70-130 F (21-54 C)` JetBrains Mono 14 pt `#F0EDE8`
- Tag: `HEAVY SCALE CAPABILITY -- HIGHEST HAZARD` Inter Medium 12 pt `#E05C5C`

**Center -- HNO3 Only (X: 8.1", W: 7.3"):**

Rounded rect H: 9.0", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `HNO3 ONLY` Barlow SemiBold 18 pt `#E8A020`
Subtitle: `HF-Free Alternative` Inter Regular 14 pt `#F0EDE8` at 60%

| Component | Concentration | Function |
|---|---|---|
| Nitric acid (HNO3) | 15-30% v/v (105-210 g/L) | Oxidizer; passivator |

- Temperature: `70-140 F (21-60 C)`
- Note: `Slower on heavy scale but eliminates HF hazard` Inter Regular 12 pt `#F0EDE8`
- Tag: `LIGHT SCALE / PASSIVATION -- MODERATE HAZARD` Inter Medium 12 pt `#E8A020`

**Right -- Citric Acid (X: 15.7", W: 7.8"):**

Rounded rect H: 9.0", fill `#1E2435`, left accent 0.06" `#27AE60`.

Title: `CITRIC ACID` Barlow SemiBold 18 pt `#27AE60`
Subtitle: `Environmentally Preferred -- ASTM A967 Method 5` Inter Regular 14 pt `#F0EDE8` at 60%

| Component | Concentration | Function |
|---|---|---|
| Citric acid | 4-10% by weight | Mild complexing acid; passivator |

- Temperature: `70-160 F (21-71 C)`
- Note: `Primarily for passivation; limited descaling ability` Inter Regular 12 pt `#F0EDE8`
- Tag: `LOWEST HAZARD -- GROWING ADOPTION` Inter Medium 12 pt `#27AE60`

---

### ZONE 4 -- Makeup Procedure

**Section label:** `TANK MAKEUP -- HF SAFETY IS THE PRIORITY` -- Y: 15.2".

**BLOCK D -- Numbered Procedure (Y: 15.8" to 21.3")**

Seven numbered steps. Each step: rounded rect, full width (23.0"), H: 0.7", fill alternating `#1E2435` / `#252B3D`.

| Step | Instruction | Caution |
|---|---|---|
| 1 | Fill tank to 2/3 volume with city water at ambient temperature | Stainless pickle typically NOT heated for HNO3/HF |
| 2 | Add nitric acid (HNO3) SLOWLY with agitation | Exothermic -- add slowly; wear full PPE including face shield |
| 3 | MEASURE HF VOLUME PRECISELY before adding | HF is the most dangerous step. Use graduated cylinder. Double-check volume. |
| 4 | Add HF SLOWLY with agitation. Do NOT splash. | FULL CHEMICAL SPLASH SUIT, butyl gloves, face shield. Calcium gluconate gel at arm's reach. |
| 5 | Bring to operating volume with water | Verify total volume matches specification |
| 6 | Verify temperature (ambient or heat to spec) | Do NOT heat HNO3/HF above 130 F -- fuming increases dramatically |
| 7 | Titrate both free HNO3 and free HF before production | NEVER pickle without analytical verification of both acid concentrations |

Step number: Barlow Condensed ExtraBold 20 pt in circle.
Steps 3-4: circle fill `#E05C5C` at 30%, text `#E05C5C`.
Other steps: circle fill `#2EC4B6` at 20%, text `#2EC4B6`.
Instruction: Inter Medium 14 pt `#F0EDE8`.
Caution: Inter Regular 12 pt `#E05C5C` for HF steps, `#E8A020` for others.

---

### ZONE 5 -- Analytical Control

**Section label:** `ANALYTICAL CONTROL -- TWO ACIDS TO TRACK` -- Y: 21.7".

**BLOCK E -- Two-Column Panel (Y: 22.3" to 27.3")**

**Left -- Titration Methods (X: 0.5", W: 11.0"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#2EC4B6`.

Title: `DUAL-ACID TITRATION` Barlow SemiBold 18 pt `#2EC4B6`

| Test | Method | Endpoint |
|---|---|---|
| Free HNO3 | Titrate with NaOH to phenolphthalein | Report as % HNO3 or g/L |
| Free HF | Add saturated KNO3 to suppress HNO3, titrate with NaOH to phenolphthalein | Report as % HF or g/L |
| Total acid | Titrate directly (both acids together) | Cross-check against individual results |

- JetBrains Mono 12 pt for methods
- Frequency: `Every shift on production lines; daily minimum` Inter Medium 13 pt `#E8A020`
- Note: `Handling titration samples of HF-containing solution requires gloves and caution` Inter Regular 11 pt `#E05C5C`

**Right -- Dissolved Metal Monitoring (X: 12.0", W: 11.5"):**

Rounded rect H: 4.5", fill `#1E2435`, left accent 0.06" `#E8A020`.

Title: `DISSOLVED METALS -- WATCH THE COLOR` Barlow SemiBold 18 pt `#E8A020`

Body: Inter Regular 13 pt `#F0EDE8`:
```
Fresh bath: clear or pale yellow
As metals dissolve:
  - Green tint = chromium + nickel buildup
  - Deep green/blue-green = approaching dump
  - Dark brown-green = spent

Quantitative methods:
  - Specific gravity increase at constant acid
  - AA spectroscopy (if available)
  - Color chart comparison

Action level: > 40-50 g/L total metals
```

JetBrains Mono 14 pt `#E05C5C`: `> 50 g/L = DUMP`

---

### ZONE 6 -- Bath Life & Dump Criteria

**Section label:** `WHEN TO DUMP -- SHORTER LIFE THAN CARBON STEEL PICKLE` -- Y: 27.7".

**BLOCK F -- Dump Criteria Table (Y: 28.3" to 32.3")**

Column widths: Parameter (4.5") | Action Level (4.5") | Symptom (7.0") | Response (7.0")

Header row: fill `#E05C5C` at 25%, H: 0.5".

| Parameter | Action Level | Symptom | Response |
|---|---|---|---|
| Dissolved Metals (Cr + Ni + Fe) | > 40-50 g/L total | Solution turns deep green; pickle rate slows dramatically | Dump and rebuild; cannot be regenerated economically |
| Free HNO3 | Below 8% v/v despite additions | Acid consumed faster than replenished; poor oxidation | Add HNO3; if persistent, dump |
| Free HF | Below 0.5% v/v despite additions | Scale not dissolving; extended pickle times | Add HF cautiously; if persistent, dump |
| Bath Age (production) | 2-4 weeks typical | General degradation; color change | Scheduled dump; stainless pickle baths have short lives |

Data: Inter Regular 13 pt. Action levels: JetBrains Mono 14 pt `#E05C5C`.

**Callout below table:**
- Rounded rect W: 23.0", H: 0.6", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Text: `Stainless pickle baths have significantly shorter lives than carbon steel pickle baths. Chromium and nickel dissolve continuously and cannot be selectively removed. Plan for frequent dumps in your waste budget.` Inter Medium 13 pt `#E8A020`

---

### ZONE 7 -- Footer

Standard. Title: `Bath Preparation & Control -- Acid Pickling (Stainless Steel)`. Version `v1.0 -- 2026`.
Disclaimer: `Source: ASTM A380; ASTM A967; general industry knowledge. HF handling requires dedicated safety training. Citric acid passivation per ASTM A967 Method 5 is increasingly adopted as an HF-free alternative. Consult your process supplier for alloy-specific formulations.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Bath Preparation Control Acid Pickling Stainless Steel -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The three-bath hero comparison is the key design choice. Shops need to understand that they have OPTIONS beyond the traditional HNO3/HF mixed acid. The citric acid card being Emerald (positive) and the HNO3/HF card being Coral (hazard) creates an instant visual hierarchy of risk. The makeup procedure is the most safety-critical section -- steps 3 and 4 (HF addition) get Coral-filled step numbers to break the visual rhythm and force attention. The short bath life callout is practical intelligence that helps shops budget for waste treatment.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #366 -- Construction Workup v1.0*
*2026-04-26*
