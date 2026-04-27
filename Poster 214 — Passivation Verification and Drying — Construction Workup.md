---
Project: Plating Posters Inc
Poster Number: 214
Title: "Passivation (Stainless Steel) -- Verification, Post-Treatment & Drying"
Document Type: Construction Workup
Version: v1.0
Status: Active
Created: 2026-04-26T00:00:00
Author: Alaina (poster-designer)
Source Documents:
  - "Conversion Coating Clusters — Watson Research Brief (CC-08 Section 8.8)"
Technical Source: Passivation verification testing per ASTM A967 and AMS 2700, drying requirements, post-treatment options, and common defect identification. Covers copper sulfate test (Practice A), salt spray (Practice B), high humidity (Practice C), water immersion (Practice D), and ferroxyl test. Standards cross-reference including legacy QQ-P-35 and medical ASTM F86.
Process Scope: Stainless steel passivation -- Stage 7-8 verification, post-treatment, and drying (final stage)
Editions: Dark (flagship) + Light (accessible print)
Intended Use: Design specification document. Generation workflow -- Claude Chat (HTML artifact) -> Drew approval -> final production
tags:
  - PosterDesign
  - Passivation
  - StainlessSteel
  - Verification
  - Drying
  - PostTreatment
  - ConstructionWorkup
  - ClusterCC08
---

# Poster #214 -- Construction Workup
## Passivation (Stainless Steel) -- Verification, Post-Treatment & Drying

*Alaina -- Plating Posters Inc Poster Designer*
*v1.0 -- 2026-04-26*

This is the final poster in CC-08 -- the capstone of the Passivation cluster. Passivation is invisible. Unlike chromate or phosphate, there is no color change, no thickness to measure, no coating weight to calculate. The only way to know if passivation worked is to test for what should NOT be there: free iron. That makes verification the most important quality step in the entire passivation process.

Five verification methods are specified in ASTM A967, and each has strengths, limitations, and appropriate applications. The copper sulfate test is the most common (and the most misunderstood -- it does not work on free-machining grades). Salt spray and high humidity are the most stringent. The ferroxyl test is the most sensitive. This poster presents all five with clear pass/fail criteria and practical notes.

Drying is the deceptively simple step that causes real problems when done wrong. High-temperature oven drying causes thermal oxidation (heat tint) that defeats the purpose of passivation. Trapped moisture in crevices causes crevice corrosion. The rules are simple but violated constantly.

---

## Part 1 -- Workflow Orientation

### Design Capabilities for This Poster

Standard capability set.

### Limitations to Flag

1. **Verification test matrix hero (Block B -- HERO):** Five test methods with pass/fail criteria and applicability notes.
2. **Copper sulfate test detail (Block C):** The most common test -- deserves expanded coverage.
3. **Drying requirements (Block D):** Simple but critical rules.
4. **Standards reference (Block E):** ASTM A967, AMS 2700, QQ-P-35, ASTM F86, SEMI F42.
5. **Troubleshooting strip (Block F).**

---

## Part 2 -- Document Setup Instructions

Standard: 24x36", `#1A1F2E`, locked palette and fonts. Standard guides.

---

## Part 3 -- Layout Zones and Build Order

```
ZONE 1 -- HEADER BAND (0"--2.9")
  Block A: Headline + subheading + tagline

ZONE 2 -- VERIFICATION TEST MATRIX / HERO (2.9"--16.0" / ~13.1" tall)
  Block B: Five verification tests -- method, pass criteria, notes
  Block C: Copper sulfate test expanded detail

ZONE 3 -- DRYING REQUIREMENTS (16.0"--22.5" / ~6.5" tall)
  Block D: Drying rules, thermal oxide warning, crevice moisture warning

ZONE 4 -- STANDARDS & POST-TREATMENT (22.5"--28.5" / ~6.0" tall)
  Block E: Applicable standards + post-treatment options

ZONE 5 -- TROUBLESHOOTING QUICK HITS (28.5"--32.5" / ~4.0" tall)
  Block F: 4-problem strip

ZONE 6 -- FOOTER BAND (32.5"--36.0" / ~3.5" tall)
  Block G: Disclaimer + footer
```

---

## Part 4 -- Zone-by-Zone Build Specifications

### ZONE 1 -- Header Band

**BLOCK A -- Headline**
- Font: Barlow Condensed ExtraBold, 72 pt, `#F0EDE8`, letter spacing -4
- Text: `PASSIVATION (STAINLESS STEEL)`
- X: 0.5", Y: 0.5", W: 23.0"

**BLOCK A -- Subheading**
- Font: Barlow SemiBold, 36 pt, `#E8A020` (Amber)
- Text: `Stage 7-8 -- Verification, Post-Treatment & Drying`
- Y: 1.5"

**BLOCK A -- Tagline**
- Font: Barlow SemiBold, 20 pt, `#F0EDE8` at 65%
- Text: `Passivation is invisible. You cannot see it, measure it, or weigh it. The only proof is testing for what should NOT be there: free iron.`
- Y: 2.2"

---

### ZONE 2 -- Verification Test Matrix (HERO)

**Section label:**
- Centered. Y: 3.1". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `VERIFICATION TESTING -- PER ASTM A967`

---

**BLOCK B -- Five Verification Tests**

Y: 3.8" to 12.5". Five test cards stacked vertically.

Each card: Rounded rect, X: 0.5", W: 23.0", H: 1.5", fill `#1E2435`, radius 6, left accent 0.06".

**Card 1 -- Copper Sulfate Test (Practice A):**
- Left accent: `#E8A020`
- Badge: `PRACTICE A` fill `#E8A020`, text `#1A1F2E`
- Test name: `COPPER SULFATE TEST` Barlow SemiBold 18 pt `#E8A020`
- Method: `Immerse in CuSO4/H2SO4 solution for 6 minutes` JetBrains Mono 13 pt `#F0EDE8`
- Pass: `No copper color (pink/red) deposit on surface` Inter Medium 14 pt `#27AE60`
- Fail: `Pink/red copper deposits = free iron present` Inter Medium 13 pt `#E05C5C`
- Note: `Most common test. Does NOT work on free-machining grades (303, 416).` Inter Regular 12 pt `#F0EDE8` at 70%
- Y: 3.8"

**Card 2 -- Salt Spray (Practice B):**
- Left accent: `#2EC4B6`
- Badge: `PRACTICE B` fill `#2EC4B6`, text `#1A1F2E`
- Test name: `SALT SPRAY (ASTM B117)` Barlow SemiBold 18 pt `#2EC4B6`
- Method: `ASTM B117 salt spray chamber, 2--24 hours` JetBrains Mono 13 pt `#F0EDE8`
- Pass: `No rust` Inter Medium 14 pt `#27AE60`
- Note: `Duration depends on specification requirements. Aerospace commonly specifies 24 hr.` Inter Regular 12 pt `#F0EDE8` at 70%
- Y: 5.5"

**Card 3 -- High Humidity (Practice C):**
- Left accent: `#27AE60`
- Badge: `PRACTICE C` fill `#27AE60`, text `#1A1F2E`
- Test name: `HIGH HUMIDITY` Barlow SemiBold 18 pt `#27AE60`
- Method: `24 hours at 95% RH, 95 F (35 C)` JetBrains Mono 13 pt `#F0EDE8`
- Pass: `No rust` Inter Medium 14 pt `#27AE60`
- Note: `Most stringent short-term test. Highly reliable for all alloy families.` Inter Regular 12 pt `#F0EDE8` at 70%
- Y: 7.2"

**Card 4 -- Water Immersion (Practice D):**
- Left accent: `#2EC4B6`
- Badge: `PRACTICE D` fill `#2EC4B6`, text `#1A1F2E`
- Test name: `WATER IMMERSION` Barlow SemiBold 18 pt `#2EC4B6`
- Method: `Immerse in water for 24 hours` JetBrains Mono 13 pt `#F0EDE8`
- Pass: `No rust` Inter Medium 14 pt `#27AE60`
- Note: `Simple but effective. Use DI water to avoid mineral deposits that mask results.` Inter Regular 12 pt `#F0EDE8` at 70%
- Y: 8.9"

**Card 5 -- Ferroxyl Test:**
- Left accent: `#E8A020`
- Badge: `FERROXYL` fill `#E8A020`, text `#1A1F2E`
- Test name: `FERROXYL TEST` Barlow SemiBold 18 pt `#E8A020`
- Method: `Apply potassium ferricyanide / nitric acid solution` JetBrains Mono 13 pt `#F0EDE8`
- Pass: `No blue color` Inter Medium 14 pt `#27AE60`
- Fail: `Blue color (Turnbull's blue) = free iron present` Inter Medium 13 pt `#E05C5C`
- Note: `Most sensitive test. Detects trace free iron that copper sulfate may miss.` Inter Regular 12 pt `#F0EDE8` at 70%
- Y: 10.6"

---

**BLOCK C -- Copper Sulfate Test Expanded**

Y: 12.5" to 15.8". Two-panel detail.

**Left -- How It Works (X: 0.5", W: 14.0"):**
- Rounded rect, H: 3.0", fill `#1E2435`, left accent `#E8A020`
- Title: `COPPER SULFATE TEST -- HOW IT WORKS` Barlow SemiBold 16 pt `#E8A020`
- Content (Inter Regular 13 pt `#F0EDE8`):
```
Solution: CuSO4 dissolved in H2SO4
If FREE IRON is present:
  Fe0 + Cu2+ --> Fe2+ + Cu0 (copper deposits on iron)
  Result: pink/red copper color = FAIL

If surface is PROPERLY PASSIVATED:
  Cr2O3 passive film blocks iron exposure
  No reaction with CuSO4 solution
  Result: no copper color = PASS
```

**Right -- Limitations (X: 15.0", W: 8.5"):**
- Rounded rect, H: 3.0", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `LIMITATIONS` Barlow SemiBold 16 pt `#E05C5C`
- Content (Inter Regular 13 pt `#F0EDE8`):
```
Does NOT work on:
  - Free-machining grades (303, 416, 420F)
  - Sulfur/selenium inclusions give false positives
  - Use ferroxyl or salt spray instead

False negatives possible if:
  - Solution is exhausted (low Cu2+)
  - Surface was acid-etched (fresh surface)
  - Test time insufficient (< 6 min)
```

---

### ZONE 3 -- Drying Requirements

**Section label:**
- Centered. Y: 16.2". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `DRYING -- SIMPLER THAN YOU THINK, HARDER THAN YOU'D EXPECT`

**BLOCK D -- Drying Rules**

Y: 16.9" to 22.3". Three panels.

**Panel 1 -- Acceptable Methods (X: 0.5", W: 7.33"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#27AE60`
- Title: `ACCEPTABLE DRYING` Barlow SemiBold 18 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Air dry at ambient temperature
  -- Simplest, safest method

Warm forced air
  -- 120-150 F (49-66 C)
  -- Accelerates drying
  -- WELL below thermal oxide threshold

Compressed air blow-off
  -- For complex geometries
  -- Displaces trapped moisture
  -- Use oil-free, filtered air
```

**Panel 2 -- Do NOT Do (X: 8.08", W: 7.33"):**
- Rounded rect, H: 5.0", fill `#E05C5C` at 15%, border 2 pt `#E05C5C`
- Title: `DO NOT` Barlow Condensed ExtraBold 20 pt `#E05C5C`
- Content (Inter Medium 14 pt `#F0EDE8`):
```
HIGH-TEMPERATURE OVEN DRYING

Temperatures above 300 F (150 C) cause
thermal oxidation -- the blue/gold heat
tint that you just spent the entire
passivation process removing.

You are literally undoing the passivation.

Also: do NOT use shop rags to wipe dry.
Carbon steel particles embedded in shop
rags will contaminate the surface.
```

**Panel 3 -- Trapped Moisture (X: 15.67", W: 7.83"):**
- Rounded rect, H: 5.0", fill `#1E2435`, left accent `#E8A020`
- Title: `TRAPPED MOISTURE` Barlow SemiBold 18 pt `#E8A020`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Parts MUST be completely dry before
packaging or storage.

Trapped moisture causes:
  - Crevice corrosion (stagnant water
    depletes dissolved O2 in the crevice;
    passive film breaks down without O2)
  - Water staining on polished surfaces
  - Microbial growth (with citric residue)

For complex geometries:
  Rotate parts during drying
  Air blow blind holes and threads
  Extended warm air for assemblies
```

---

### ZONE 4 -- Standards & Post-Treatment

**Section label:**
- Centered. Y: 22.7". Barlow Condensed ExtraBold, 28 pt, `#F0EDE8`
- Text: `APPLICABLE STANDARDS & POST-TREATMENT`

**BLOCK E -- Two Panels**

Y: 23.4" to 28.3".

**Left -- Standards Reference (X: 0.5", W: 14.0"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#2EC4B6`
- Title: `KEY STANDARDS` Barlow SemiBold 18 pt `#2EC4B6`

| Standard | Scope |
|---|---|
| ASTM A967/A967M | Chemical passivation of stainless steel -- PRIMARY STANDARD |
| AMS 2700 | Passivation of corrosion resistant steels (aerospace) |
| ASTM A380 | Cleaning, descaling, and passivation (broader guidance) |
| QQ-P-35 (Canceled) | Legacy federal spec; superseded by ASTM A967; still on old drawings |
| ASTM F86 | Surface preparation of metallic surgical implants (medical) |
| SEMI F42 | Stainless steel evaluation for semiconductor applications |

Data: JetBrains Mono 11 pt. Standard column: Inter Medium 12 pt `#2EC4B6`.
Alternating rows: `#1E2435` / `#252B3D`.

**Right -- Post-Treatment (X: 15.0", W: 8.5"):**
- Rounded rect, H: 4.5", fill `#1E2435`, left accent `#27AE60`
- Title: `POST-TREATMENT OPTIONS` Barlow SemiBold 18 pt `#27AE60`
- Content (Inter Regular 14 pt `#F0EDE8`):
```
Normally NONE required.
The passive film IS the final surface.

For enhanced protection:

ELECTROPOLISH BEFORE PASSIVATION
  Removes surface roughness and embedded
  contaminants. Citric passivation after
  electropolish is becoming the standard
  aerospace/medical protocol.

PROTECTIVE PACKAGING
  VCI paper or bags for long-term storage
  of passivated parts. Prevents atmospheric
  corrosion during shipping.
```

---

### ZONE 5 -- Troubleshooting Quick Hits

**Section label:**
- Centered. Y: 28.7". Barlow Condensed ExtraBold, 24 pt, `#F0EDE8`
- Text: `QUICK TROUBLESHOOTING -- 4 COMMON PROBLEMS`

**BLOCK F -- Four Problem Cards**

Y: 29.4" to 32.3". Same construction as other CC-08 posters.

| Card | X | Problem | Cause | Fix |
|---|---|---|---|---|
| 1 | 0.5" | CuSO4 FALSE POSITIVE (303/416) | Free-machining alloy; sulfur inclusions react | Use ferroxyl or salt spray instead |
| 2 | 6.33" | RUST AFTER VERIFICATION PASS | Trapped moisture; inadequate drying; crevice geometry | Improve drying protocol; air blow; extend warm air |
| 3 | 12.16" | HEAT TINT FROM DRYING | Oven temperature too high (>300 F) | Use ambient or warm air only (<150 F) |
| 4 | 18.0" | FAILED SALT SPRAY | Insufficient passivation time; contaminated bath; wrong bath for alloy | Re-passivate; check bath chemistry; consult alloy guide (Poster 212) |

---

### ZONE 6 -- Footer Band

Standard footer. Title: `Passivation (Stainless Steel) -- Verification, Post-Treatment & Drying`. Version `v1.0 -- 2026`.

Disclaimer: `This poster is an educational reference tool. Verification testing methods shown are per ASTM A967/A967M and AMS 2700. Test selection and acceptance criteria vary by customer specification and application. QQ-P-35 is canceled and superseded by ASTM A967. Consult your process supplier and applicable engineering specification.`

---

## Parts 5--7

**Grouping:** 6 zones.
**Light Remap:** Standard table.
**Export:** Six files -- `Passivation Verification Drying -- {Dark,Light} -- {24x36,18x24,Digital}`.

---

## Design Notes

This poster completes the CC-08 Passivation cluster. The verification test matrix is the hero element -- it needs to be the first thing an operator sees when asked "how do I know if passivation worked?" The five ASTM A967 practices are laid out as individual cards with clear pass/fail criteria and practical notes. The expanded copper sulfate test detail addresses the most common source of confusion: why the test does not work on free-machining grades.

The drying section addresses a surprisingly common failure mode. High-temperature oven drying that causes heat tint is one of those mistakes that experienced operators know about but new operators make regularly. The "DO NOT" panel in Coral makes this impossible to miss.

The standards reference table provides traceability for quality managers and auditors -- every passivation shop should be able to point to the applicable spec. Including the canceled QQ-P-35 is important because legacy drawings still reference it.

---

*Alaina -- Plating Posters Inc Poster Designer*
*Poster #214 -- Construction Workup v1.0*
*2026-04-26*
