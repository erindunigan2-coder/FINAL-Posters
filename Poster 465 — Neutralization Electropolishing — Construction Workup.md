---
Project: Plating Posters Inc
Poster Number: 465
Title: "Neutralization -- Electropolishing"
Document Type: Construction Workup
Status: v1.0 -- Ready for Generation
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Specialty Advanced Clusters — Watson Research Brief (Cluster 7, Sections 7.6--7.8)"
Technical Source: Post-electropolishing neutralization and passivation. Citric acid or nitric acid treatment per ASTM A967 and ASTM A380. Enhances the Cr-enriched passive layer formed during EP. Critical for pharma, biotech, food, medical device applications.
Process Scope: Electropolishing -- neutralization/passivation (Stage 7 of 8)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Electropolishing
  - Neutralization
  - Passivation
  - ConstructionWorkup
  - SpecialtyAdvanced
---

# Poster #465 -- Construction Workup
## Neutralization -- Electropolishing

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

Post-EP neutralization/passivation is where the passive layer goes from "good" to "great." Electropolishing already enriches chromium at the stainless steel surface (the Cr:Fe ratio jumps from ~1.5:1 to 3:1--5:1), but a dedicated passivation step per ASTM A967 locks that in. This poster covers the chemistry (citric vs. nitric), the standards (ASTM A967, ASTM A380, ASME BPE), and the verification tests (ferroxyl, copper sulfate, water-break). For pharma/biotech, this step is not optional -- it is spec-required.

---

## Part 1 -- Workflow Orientation

### Limitations to Flag

1. **Citric vs. Nitric comparison (Block B -- HERO):** Side-by-side panels comparing the two dominant passivation chemistries.
2. **Standards matrix (Block D):** Which standard applies to which industry.
3. **Verification testing panel (Block E):** Ferroxyl test, copper sulfate test, and water-break test procedures.
4. **Cr:Fe enrichment callout (Block F):** Before/after EP and after passivation.

---

## Part 2 -- Document Setup

Standard: 24x36", `#1A1F2E`, locked palette and fonts.

**Horizontal guides:**
- 0.5" / 2.9" / 4.2" / 14.5" / 22.0" / 28.5" / 32.5" / 35.5"

---

## Part 3 -- Layout Zones

```
ZONE 1 -- HEADER BAND (0"--2.9")
ZONE 2 -- SEQUENCE STRIP (2.9"--4.2")
  Stage 7 highlighted (Amber)
ZONE 3 -- PASSIVATION CHEMISTRY HERO (4.2"--14.5" / ~10.3")
  Block B: Citric vs Nitric comparison
  Block C: Process parameters table
ZONE 4 -- STANDARDS & SPECIFICATIONS (14.5"--22.0" / ~7.5")
  Block D: Standards matrix (ASTM A967, A380, ASME BPE)
  Block E: Industry requirements
ZONE 5 -- VERIFICATION TESTING (22.0"--28.5" / ~6.5")
  Block F: Test procedures (ferroxyl, copper sulfate, water-break)
ZONE 6 -- Cr:Fe ENRICHMENT (28.5"--32.5" / ~4.0")
  Block G: Passive layer composition before/after
ZONE 7 -- FOOTER BAND (32.5"--36.0")
```

---

## Part 4 -- Zone-by-Zone Specifications

### ZONE 1 -- Header Band

**Headline:** `NEUTRALIZATION` -- 88 pt `#F0EDE8`. X: 0.5", Y: 0.5".
**Subheading:** `Electropolishing -- Stage 7 of 8 -- Passivation Enhancement` -- 36 pt `#E8A020` (Amber). Y: 1.5".
**Tagline:** `EP enriches chromium at the surface. Passivation locks it in. Citric or nitric acid per ASTM A967 -- the choice depends on your spec and your waste stream.` -- 20 pt `#F0EDE8` at 65%. Y: 2.1".

---

### ZONE 2 -- Sequence Orientation Strip

Stage 7 (`Neutralize/Passivate`) highlighted: fill `#E8A020`, text `#1A1F2E`. Others dimmed.

Below: `Before: Rinsed, acid-free electropolished surface --> After: Enhanced Cr-rich passive oxide layer verified by testing` -- Inter Regular, 13 pt, `#F0EDE8` at 60%.

---

### ZONE 3 -- Passivation Chemistry Hero

**Section label:** `PASSIVATION CHEMISTRY -- CITRIC VS. NITRIC` -- Y: 4.4".

---

**BLOCK B -- Two-Panel Comparison (Y: 5.0" to 11.5")**

**Left -- Citric Acid Passivation (X: 0.5", W: 11.0"):**
- Rounded rect, H: 6.0", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `CITRIC ACID PASSIVATION` Barlow SemiBold 22 pt `#27AE60`
- Subtitle: `ASTM A967 -- Practice C` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 160%):
```
Chemistry:  Citric acid 4--10% (w/v)
Temperature: Ambient to 60 C (140 F)
Time:       20--60 min
pH:         ~2 (as-mixed)
```

Advantages (Inter Regular 13 pt `#27AE60`, line height 155%):
```
+ Environmentally preferred -- biodegradable
+ No NOx fumes generated
+ Safer to handle than HNO3
+ Chelates free iron from surface
+ Lower wastewater treatment cost
+ Gaining industry acceptance rapidly
```

Limitation (Inter Regular 12 pt `#E8A020`):
```
Citric may not meet legacy specs that
specifically require nitric acid
```

**Right -- Nitric Acid Passivation (X: 12.0", W: 11.5"):**
- Rounded rect, H: 6.0", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `NITRIC ACID PASSIVATION` Barlow SemiBold 22 pt `#E8A020`
- Subtitle: `ASTM A967 -- Practice A/B` Barlow Condensed ExtraBold 14 pt `#F0EDE8` at 50%

Parameters (JetBrains Mono 13 pt `#F0EDE8`, line height 160%):
```
Chemistry:  HNO3 20--50% (v/v)
  Optional: + Na2Cr2O7 2--6 oz/gal
Temperature: Ambient to 60 C (140 F)
Time:       20--60 min
pH:         Strongly acid (< 1)
```

Advantages (Inter Regular 13 pt `#E8A020`, line height 155%):
```
+ Long-established industry standard
+ Strong oxidizer -- effective oxide builder
+ Well-documented in legacy specifications
+ Effective for all stainless grades
```

Limitations (Inter Regular 12 pt `#E05C5C`):
```
NOx fume generation -- ventilation required
Higher waste disposal cost
Dichromate addition adds Cr(VI) -- avoid
```

---

**BLOCK C -- Process Parameters Table (Y: 12.0" to 14.0")**

Compact table. Columns: Method (4.0") | Chemistry (5.0") | Temp (3.0") | Time (3.0") | Rinse After (4.0") | Spec (4.0")

| Method | Chemistry | Temp | Time | Rinse After | Spec |
|---|---|---|---|---|---|
| Citric A | 4--10% citric acid | 49--60 C | 20--30 min | DI water cascade | ASTM A967 Practice C |
| Citric B | 4--10% citric acid | Ambient | 30--60 min | DI water cascade | ASTM A967 Practice C |
| Nitric A | 20--25% HNO3 | Ambient | 30--60 min | DI water cascade | ASTM A967 Practice A |
| Nitric B | 20--50% HNO3 | 49--60 C | 20--30 min | DI water cascade | ASTM A967 Practice B |

Header: `#3A4055`, Barlow SemiBold 13 pt. Data: JetBrains Mono 11 pt `#F0EDE8`.

---

### ZONE 4 -- Standards & Specifications

**Section label:** `APPLICABLE STANDARDS` -- Y: 14.7".

---

**BLOCK D -- Standards Matrix (Y: 15.3" to 19.0")**

Table -- columns: Standard (5.0") | Scope (8.0") | Key Requirements (10.0")

| Standard | Scope | Key Requirements |
|---|---|---|
| ASTM A967/A967M | Chemical passivation treatments for SS parts | Defines citric and nitric acid practices; specifies test methods for verification |
| ASTM A380 | Cleaning, descaling, passivation of SS parts/equipment | Broader scope -- covers cleaning + passivation; references A967 for passivation details |
| ASME BPE | Bioprocessing equipment | Requires EP + passivation for product-contact surfaces; SF4 finish; specifies DI water rinse |
| SEMI F19 | Semiconductor gas/fluid systems | Ultra-clean surface requirements; passivation required after EP |
| FDA 21 CFR | Medical devices, food contact | General surface cleanliness and corrosion resistance; passivation is standard practice |

Header: `#3A4055`. Data: Inter Regular 12 pt `#F0EDE8`.

**BLOCK E -- Industry Requirements Callout (Y: 19.5" to 21.5")**

Two side-by-side cards:

**Left -- When Passivation Is Required (X: 0.5", W: 11.0"):**
- Rounded rect, H: 1.8", fill `#27AE60` at 15%, border 1 pt `#27AE60`
- Title: `ALWAYS PASSIVATE AFTER EP WHEN:` Barlow SemiBold 16 pt `#27AE60`
- List (Inter Regular 13 pt `#F0EDE8`):
```
- Pharma/biotech per ASME BPE
- Medical devices per FDA requirements
- Semiconductor per SEMI standards
- Any specification calling out ASTM A967
- Customer PO requires passivation
```

**Right -- When Passivation Is Optional (X: 12.0", W: 11.5"):**
- Rounded rect, H: 1.8", fill `#E8A020` at 15%, border 1 pt `#E8A020`
- Title: `PASSIVATION MAY BE OPTIONAL WHEN:` Barlow SemiBold 16 pt `#E8A020`
- List (Inter Regular 13 pt `#F0EDE8`):
```
- General industrial/decorative EP only
- No customer spec requires it
- EP itself provides adequate passive layer
- NOTE: Even optional, passivation is cheap
  insurance -- 20 min soak costs very little
```

---

### ZONE 5 -- Verification Testing

**Section label:** `PASSIVATION VERIFICATION TESTS` -- Y: 22.2".

---

**BLOCK F -- Three Test Cards (Y: 22.9" to 28.0")**

Three cards in a row:

**Card 1 -- Ferroxyl Test (X: 0.5", W: 7.33"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent 0.06" `#2EC4B6`
- Title: `FERROXYL TEST` Barlow SemiBold 16 pt `#2EC4B6`
- Subtitle: `ASTM A380` Inter Medium 12 pt `#F0EDE8` at 60%
- Body (Inter Regular 12 pt `#F0EDE8`, line height 155%):
```
Apply ferroxyl solution (K3Fe(CN)6
+ HNO3 in DI water) to surface.

PASS: No blue spots within 15 min
  (no free iron on surface)

FAIL: Blue spots indicate free iron --
  re-passivate or investigate
  contamination source
```
- Note: `Most common QC test for passivation` Inter Medium 11 pt `#27AE60`

**Card 2 -- Copper Sulfate Test (X: 8.33", W: 7.33"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent 0.06" `#E8A020`
- Title: `COPPER SULFATE TEST` Barlow SemiBold 16 pt `#E8A020`
- Subtitle: `ASTM A967 / ASTM A380` Inter Medium 12 pt `#F0EDE8` at 60%
- Body (Inter Regular 12 pt `#F0EDE8`, line height 155%):
```
Swab CuSO4 solution on surface.
Wait 6 min.

PASS: No copper color (pink/red)
  deposited on surface

FAIL: Copper deposits indicate active
  iron on surface -- passive layer
  is inadequate

Applicable to 300 and 400 series SS.
```

**Card 3 -- Water-Break Test (X: 16.16", W: 7.33"):**
- Rounded rect, H: 4.8", fill `#1E2435`, left accent 0.06" `#27AE60`
- Title: `WATER-BREAK TEST` Barlow SemiBold 16 pt `#27AE60`
- Subtitle: `Visual -- universal` Inter Medium 12 pt `#F0EDE8` at 60%
- Body (Inter Regular 12 pt `#F0EDE8`, line height 155%):
```
Spray or flow DI water over surface.

PASS: Water sheets uniformly with
  no beading or break-up

FAIL: Water beads or breaks indicate
  organic contamination or
  incomplete passivation

Simple, fast, non-destructive.
Use as first-pass screening.
```

---

### ZONE 6 -- Cr:Fe Enrichment

**Section label:** `PASSIVE LAYER COMPOSITION` -- Y: 28.7".

---

**BLOCK G -- Three-Stage Comparison Strip (Y: 29.4" to 32.0")**

Three cards in a row showing progressive Cr:Fe enrichment:

**Card 1 -- Mechanically Polished (X: 0.5", W: 7.33"):**
- Rounded rect, H: 2.3", fill `#1E2435`, top accent 4 pt `#C8D0D8`
- Title: `MECHANICAL POLISH` Barlow SemiBold 14 pt `#C8D0D8`
- Data: `Cr:Fe ratio ~1.5:1` JetBrains Mono 18 pt `#C8D0D8`
- Note: `Native passive oxide` Inter Regular 11 pt `#F0EDE8` at 60%

**Card 2 -- After Electropolishing (X: 8.33", W: 7.33"):**
- Rounded rect, H: 2.3", fill `#1E2435`, top accent 4 pt `#27AE60`
- Title: `AFTER EP` Barlow SemiBold 14 pt `#27AE60`
- Data: `Cr:Fe ratio 3:1 to 5:1` JetBrains Mono 18 pt `#27AE60`
- Note: `EP enriches Cr by selectively dissolving Fe` Inter Regular 11 pt `#F0EDE8` at 60%

**Card 3 -- After EP + Passivation (X: 16.16", W: 7.33"):**
- Rounded rect, H: 2.3", fill `#1E2435`, top accent 4 pt `#E8A020`
- Title: `AFTER EP + PASSIVATION` Barlow SemiBold 14 pt `#E8A020`
- Data: `Cr:Fe ratio 5:1+` JetBrains Mono 18 pt `#E8A020`
- Note: `Passivation further dissolves surface Fe, thickens Cr oxide` Inter Regular 11 pt `#F0EDE8` at 60%

---

### ZONE 7 -- Footer

Standard. Title: `Neutralization -- Electropolishing`. Version `v1.0 -- 2026`.

Disclaimer: `Source: General industry knowledge; ASTM A967; ASTM A380; ASME BPE. Passivation chemistry and verification requirements vary by specification and alloy grade. Consult your quality engineer and process supplier.`

---

## Parts 5--7

**Grouping:** 7 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Neutralization Electropolishing -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

The citric vs. nitric comparison (Block B) is the decision point for most shops -- citric is gaining ground fast because it is safer, cheaper to dispose of, and spec-compliant under ASTM A967. The verification test cards (Zone 5) give quality engineers the exact procedures they need. The Cr:Fe enrichment strip (Zone 6) provides the metallurgical "why" -- this is the science that justifies the 20--60 minute soak time to a cost-conscious production manager.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #465 -- Construction Workup v1.0*
*2026-04-26*
